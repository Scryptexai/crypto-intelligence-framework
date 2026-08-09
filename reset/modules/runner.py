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


def run_project(name: str, providers, dry_run: bool,
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

        # Phase 11 as FOUR sequential stages -- last resort only, same gate as Phase 9's split
        # (phases.run_phase). Reached when streaming has been turned off and no heavy-capable
        # provider is configured, i.e. the request would go out in the exact shape that hits
        # the gateway's ~300s non-streaming ceiling.
        #
        # Off by default since 2026-08-09. The split's justification was a measured 504 on
        # stage 11a, but that measurement predates the streaming fix -- the ceiling was an
        # artifact of sending a non-streaming request that returns no bytes until generation
        # finishes, not of Phase 11 being too large.
        #
        # Splitting is also unsound for this phase specifically, for a reason beyond timing:
        # 11d's own prompt instructs the model to "GABUNGKAN dengan seluruh temuan sebelumnya"
        # -- merge everything the earlier stages found. A model asked to restate prior findings
        # re-emits them in slightly different words, and a validation report is exactly where a
        # near-duplicate finding is indistinguishable from a second real one. An audit that
        # invents or double-counts its own findings is worse than no audit, because it reads
        # authoritative. The single-prompt path has no seam for that to happen at.
        #
        # And it is the empirically proven path: reset/phase_11_conflict.txt is the prompt that
        # produced data_project/Arbitrum/11-conflict.docx -- the only Phase 11 extract_qa.py has
        # ever parsed (total=81.6, 6 dimensions, 7 phases), with zero '## ' sub-headers to trip
        # that parser's section boundary. The staged path has never produced a parseable one.
        if num == 11 and not config.STREAM_RESPONSES and not phases_mod.has_heavy_provider(providers):
            stage_names = ", ".join(s[0] for s in config.PHASE11_STAGES)
            plog(f"phase 11-conflict: streaming off and no heavy provider -- falling back to "
                 f"{len(config.PHASE11_STAGES)} sequential stages ({stage_names}), which risks "
                 f"duplicated findings; prefer leaving streaming on...")
            if dry_run:
                out_path.write_text(
                    f"PROJECT: {name}\n\n[DRY RUN -- Phase 11 placeholder, "
                    f"{len(config.PHASE11_STAGES)}-stage split]\n", encoding="utf-8")
                plog(f"phase 11-conflict: [dry-run] wrote placeholder -> {out_path}")
                continue
            text, err = phases_mod.run_phase_11(name, providers, proj_dir)
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
                                                   providers, plog)
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

    # Finalise whenever the run actually covered phases 1-10, which is the input the quality
    # gate and every extractor read:
    #   10 -- Phase 11 deliberately deferred (the bulk-repair mode)
    #   11 -- the later per-project Phase 11 pass over an already-clean project
    #    0 -- an ordinary full run, all 11 phases in one go
    # A smaller --phases-limit is a partial/test run and is left alone: verify_10_phases would
    # fail on phases that were never asked for.
    #
    # 11 and 0 were added 2026-08-08. Without them a Phase 11 pass wrote 11-conflict.docx and
    # stopped -- the dossier was never rebuilt, so extract_qa.py kept parsing a dossier with no
    # Phase 11 in it and poc/qa.json stayed at one project no matter how many audits ran.
    if phases_limit in (0, 10, 11) and not dry_run:
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


def run_queue(projects: list, providers, dry_run: bool,
              phases_limit: int, output_root: Path, auto_sync: bool, parallel: int) -> int:
    """Returns how many projects failed, so the caller can exit non-zero.

    It used to return nothing and the process exited 0 whatever happened, which meant a
    driver script could not tell a completed project from a failed one. That matters when the
    gateway is having a bad hour: reset/run_pipeline_stages.sh uses the exit status to stop
    after a few consecutive failures instead of grinding through 25 projects that are all
    going to fail the same way.
    """
    failed = 0
    if parallel > 1:
        with ThreadPoolExecutor(max_workers=parallel) as pool:
            futures = {}
            for i, name in enumerate(projects):
                # Small stagger so N threads don't all hit the API in the same instant.
                if i:
                    time.sleep(5)
                futures[pool.submit(run_project, name, providers, dry_run,
                                    phases_limit, output_root, auto_sync)] = name
            for fut in as_completed(futures):
                name = futures[fut]
                try:
                    if not fut.result():
                        failed += 1
                except Exception as e:  # noqa: BLE001 -- one thread crashing must not kill others
                    log(f"[{name}] ✗✗ unexpected exception, this project's thread crashed: {e}")
                    failed += 1
    else:
        for i, name in enumerate(projects):
            if not run_project(name, providers, dry_run, phases_limit, output_root, auto_sync):
                failed += 1
            if i < len(projects) - 1:
                log(f"sleeping {config.PROJECT_SLEEP_SECONDS}s before next project...")
                time.sleep(config.PROJECT_SLEEP_SECONDS)

    log(f"All projects processed ({failed} failed). Check reset/failures.log for anything "
        f"that needs a manual re-run.")
    return failed
