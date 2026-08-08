"""
runner.py — per-project orchestration and the multi-project queue.

run_project owns one project end to end: resume what exists, generate what doesn't,
verify, promote, chain to ingest/extract/sync. run_queue owns the sequential and parallel
loops over projects.txt.
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from . import config, phases as phases_mod, pipeline, prompts, validate
from .logs import log, log_failure, log_needs_review, project_logger


def run_project(name: str, base_url: str, token: str, model: str, dry_run: bool,
                phases_limit: int, output_root: Path, auto_sync: bool = False) -> bool:
    """True if every requested phase completed (generated or resumed from disk), False if a
    phase failed permanently -- in which case later phases for this project are skipped (they
    need this one's output as context) but the run continues to the NEXT project rather than
    aborting everything."""
    plog = project_logger(name)
    plog("=== starting ===")
    proj_dir = output_root / name
    proj_dir.mkdir(parents=True, exist_ok=True)
    messages: list = []  # running chat history -- Track C's "one continuous chat" methodology
    unresolved: dict = {}  # phase label -> failed check names that survived self-repair

    todo = config.PHASES[:phases_limit] if phases_limit else config.PHASES

    for idx, (num, key) in enumerate(todo):
        out_path = proj_dir / f"{num:02d}-{key}.docx"

        if phases_mod.existing_phase_ok(out_path):
            plog(f"phase {num:02d}-{key}: already done, resuming (loading into context, no API call)")
            if num == 11:
                # Phase 11 is self-contained (built from the files on disk, not the running
                # conversation) and nothing later depends on it -- there is no phase 12 that
                # would need it appended to `messages`, unlike phases 1-10.
                continue
            messages.append({"role": "user", "content": prompts.prompt_placeholder(num, key)})
            messages.append({"role": "assistant",
                             "content": out_path.read_text(encoding="utf-8")})
            continue

        if num == 11:
            stage_names = ", ".join(s[0] for s in config.PHASE11_STAGES)
            plog(f"phase 11-conflict: sending as {len(config.PHASE11_STAGES)} smaller sequential "
                 f"stages ({stage_names}) -- see run_phase_11()'s docstring for why...")
            if dry_run:
                out_path.write_text(
                    f"PROJECT: {name}\n\n[DRY RUN -- Phase 11 placeholder, "
                    f"{len(config.PHASE11_STAGES)}-stage split]\n", encoding="utf-8")
                plog(f"phase 11-conflict: [dry-run] wrote placeholder -> {out_path}")
                continue
            text, err = phases_mod.run_phase_11(name, base_url, token, model, proj_dir)
            if err is not None:
                plog(f"✗✗ {name} phase 11-conflict permanently failed, giving up on this "
                     f"project for now: {err}")
                log_failure(name, num, key, err)
                plog("(re-run this script later and it will resume from here)")
                return False
            out_path.write_text(text, encoding="utf-8")
            plog(f"phase 11-conflict: done ({len(text)} chars, "
                 f"{len(config.PHASE11_STAGES)}-stage split) -> {out_path}")
            continue

        if dry_run:
            fake = f"PROJECT: {name}\n\n[DRY RUN -- no real API call made for phase {num:02d}-{key}]\n"
            out_path.write_text(fake, encoding="utf-8")
            messages.append({"role": "user", "content": prompts.prompt_placeholder(num, key)})
            messages.append({"role": "assistant", "content": fake})
            plog(f"phase {num:02d}-{key}: [dry-run] wrote placeholder -> {out_path}")
        else:
            try:
                _, failures = phases_mod.run_phase(name, num, key, messages, proj_dir,
                                                   base_url, token, model, plog)
            except Exception as e:  # noqa: BLE001
                plog(f"✗✗ {name} phase {num:02d}-{key} permanently failed, giving up on this "
                     f"project for now: {e}")
                log_failure(name, num, key, e)
                plog(f"(later phases for {name} need this one's output, so skipping the rest "
                     f"of {name} -- re-run this script later and it will resume from here)")
                return False
            if failures:
                unresolved[f"{num:02d}-{key}"] = [c.name for c, _ in failures]

        if idx < len(todo) - 1:
            plog(f"sleeping {config.PHASE_SLEEP_SECONDS}s before next phase...")
            time.sleep(config.PHASE_SLEEP_SECONDS)

    if unresolved:
        plog(f"⚠ phases saved with unresolved spec checks: {unresolved} "
             f"(see reset/repairs.log -- a check failing across many projects is a prompt bug)")

    # --phases-limit 10 is the explicit signal that Phase 11 is being deliberately deferred:
    # run every project through 1-10 first, do Phase 11 per-project later. Run the real
    # quality gate and auto-promote on a pass.
    if phases_limit == 10 and not dry_run:
        _finalise(name, proj_dir, output_root, auto_sync, plog)
    return True


def _finalise(name: str, proj_dir: Path, output_root: Path, auto_sync: bool, plog) -> None:
    ok, report = validate.verify_10_phases(name, proj_dir)
    plog(f"verify_10_phases: entities={report['entities']} events={report['events']} "
         f"decisions={report['decisions']} knowledge={report['knowledge']} "
         f"-- {'PASS' if ok else 'FAIL'}")
    if not ok:
        log_needs_review(name, report)
        plog(f"=== ✗ verification FAILED -- at least one of phases 2/3/9/10 didn't extract any "
             f"rows despite passing the citation check. NOT promoted to data_project/. Logged "
             f"to {config.REVIEW_LOG.name} for manual review; output stays in "
             f"{output_root}/{name}/. ===")
        return

    if output_root != config.DATA_PROJECT_ROOT:
        pipeline.promote_to_data_project(name, proj_dir)
        plog(f"=== verified + promoted: phases 1-10 copied to data_project/{name}/ (Phase 11 "
             f"still pending -- 11-conflict.docx stays the empty scaffold). ===")
    else:
        plog("=== verified (already writing directly to data_project/, nothing to promote). ===")

    with config._pipeline_lock:
        chain_ok, chain_status = pipeline.run_ingest_extract_sync(name, auto_sync)
    plog(f"=== ingest/extract/sync chain: {chain_status} "
         f"({'ok' if chain_ok else 'FAILED'}) ===")


def run_queue(projects: list, base_url: str, token: str, model: str, dry_run: bool,
              phases_limit: int, output_root: Path, auto_sync: bool, parallel: int) -> None:
    if parallel > 1:
        with ThreadPoolExecutor(max_workers=parallel) as pool:
            futures = {}
            for i, name in enumerate(projects):
                # Small stagger so N threads don't all hit the API in the same instant.
                if i:
                    time.sleep(5)
                futures[pool.submit(run_project, name, base_url, token, model, dry_run,
                                    phases_limit, output_root, auto_sync)] = name
            for fut in as_completed(futures):
                name = futures[fut]
                try:
                    fut.result()
                except Exception as e:  # noqa: BLE001 -- one thread crashing must not kill others
                    log(f"[{name}] ✗✗ unexpected exception, this project's thread crashed: {e}")
    else:
        for i, name in enumerate(projects):
            run_project(name, base_url, token, model, dry_run, phases_limit, output_root,
                        auto_sync)
            if i < len(projects) - 1:
                log(f"sleeping {config.PROJECT_SLEEP_SECONDS}s before next project...")
                time.sleep(config.PROJECT_SLEEP_SECONDS)

    log("All projects processed. Check reset/failures.log for anything that needs a manual re-run.")
