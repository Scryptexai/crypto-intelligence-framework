"""
phases.py — generating a single phase, and the four-stage Phase 11.

Phases 1-10 go through repair.generate_phase (spec-checked, self-correcting). Phase 11 has
no extractor contract to check against and keeps its own staged flow.
"""
import re
import time
from pathlib import Path

from . import config, prompts, repair
from .api import call_with_retries
from .logs import log


def existing_phase_ok(path: Path) -> bool:
    return path.exists() and len(path.read_text(encoding="utf-8").strip()) >= config.MIN_PHASE_CHARS


def _has_heavy_provider(providers) -> bool:
    """True when some provider in the chain can take a heavy phase as a single call.

    When one exists, Phase 9 and Phase 11 go back to their original single-prompt design and
    the staged workarounds are skipped entirely: the gateway is still tried first (the rule is
    to exhaust the free endpoint before spending), api.call_with_retries rotates on the
    capacity failure, and after the first such rotation it stops re-proving the limit for the
    rest of the run.
    """
    if isinstance(providers, config.Provider):
        providers = [providers]
    return any(getattr(p, "heavy_capable", False) for p in providers)


def _run_staged_phase_9(name: str, messages: list, proj_dir: Path, providers, plog) -> str:
    """Phase 9 as three sequential calls on the running conversation (config.PHASE9_STAGES).

    Same root cause as Phase 11's four-stage split: the gateway kills any single generation
    past ~300s (HTTP 504 at 310s and 306s on two consecutive Lido attempts, 2026-08-08).

    It is the OUTPUT that decides this, not the input -- see config.PHASE9_STAGES for the
    measured table. Phase 10 carries MORE context (45,459 tok vs 38,983) and still finishes;
    Phase 9 just has the largest output of any phase (8,436 tok), which at this backend's
    ~26-28 tok/s lands at 301-324s, barely over the wall. Three stages put each call at
    ~2,800 output tokens / ~100-110s. The input stays whole -- it is the phases 1-8 context
    and is what makes the analysis possible.

    Unlike Phase 11, these stages run ON the running conversation rather than a freshly built
    one: Phase 9 is pure analysis over phases 1-8 and needs that context, and each completed
    stage stays in the conversation so a later stage can refer back to what it already
    established instead of contradicting it.

    Per-stage resumability via 09-stage-*.tmp mirrors run_phase_11: if stage 9c times out,
    re-running does not pay for 9a and 9b again.
    """
    parts = []
    for stage_key, prompt_file in config.PHASE9_STAGES:
        tmp_path = proj_dir / f"09-stage-{stage_key}.tmp"
        if tmp_path.exists() and len(tmp_path.read_text(encoding="utf-8").strip()) >= 200:
            response = tmp_path.read_text(encoding="utf-8")
            plog(f"phase {stage_key}: already done, resuming from {tmp_path.name} (no API call)")
        else:
            plog(f"phase {stage_key}: sending ({prompt_file})...")
            messages.append({"role": "user",
                             "content": prompts.load_stage_prompt(prompt_file)})
            response = call_with_retries(messages, providers,
                                         f"{name} phase {stage_key}", heavy=True)
            tmp_path.write_text(response, encoding="utf-8")
            messages.append({"role": "assistant", "content": response})
            # Shrink the stage prompt now its answer is in context, same reasoning as
            # prompts.prompt_placeholder for ordinary phases.
            messages[-2]["content"] = f"[Phase {stage_key} instructions were sent here; " \
                                      f"see that stage's output below.]"
            plog(f"phase {stage_key}: done ({len(response)} chars)")
            if stage_key != config.PHASE9_STAGES[-1][0]:
                time.sleep(config.PHASE_SLEEP_SECONDS)
        parts.append(response.strip())

    combined = prompts.ensure_project_header("\n\n".join(parts), name)
    for stage_key, _ in config.PHASE9_STAGES:
        (proj_dir / f"09-stage-{stage_key}.tmp").unlink(missing_ok=True)
    return combined


def run_phase(name: str, num: int, key: str, messages: list, proj_dir: Path, providers,
              plog) -> tuple:
    """Generate one ordinary phase (1-10), self-repairing format failures, and save it.

    Appends the prompt + final output to `messages` (mutating it, as the running Track C
    conversation), shrinking the prompt to a placeholder once the answer is in context.

    Returns (text, remaining_failures).
    """
    out_path = proj_dir / f"{num:02d}-{key}.docx"

    if num == 9 and not _has_heavy_provider(providers):
        # No provider can take Phase 9 in one call, so fall back to three stages (see
        # _run_staged_phase_9). The stages already appended themselves to `messages`, so the
        # single-prompt bookkeeping below is skipped. Spec checks still run against the
        # assembled result; self-repair is deliberately NOT applied, because a repair asks for
        # a complete rewrite in one call -- exactly what cannot finish inside the timeout here.
        #
        # Splitting is the correct remedy for THIS gateway, not a workaround: the limit it
        # hits is generation time, and cutting the output per call is the only lever that
        # moves it (config.PHASE9_STAGES has the measurements). It is skipped entirely when a
        # faster provider is available, since one call is simpler and re-pays no prefill.
        from . import specs
        text = _run_staged_phase_9(name, messages, proj_dir, providers, plog)
        failures = specs.run_checks(num, key, name, text)
        if failures:
            plog(f"phase {num:02d}-{key}: ⚠ assembled from stages but {len(failures)} check(s) "
                 f"still failing: {', '.join(c.name for c, _ in failures)}")
        text, failures = _keep_better(out_path, text, failures, num, key, name, plog)
        out_path.write_text(text, encoding="utf-8")
        plog(f"phase {num:02d}-{key}: done ({len(text)} chars, "
             f"{len(config.PHASE9_STAGES)}-stage split) -> {out_path}")
        return text, failures

    prompt_template = prompts.load_phase_prompt(num, key)
    prompt = prompt_template.replace("<NAMA PROJECT>", name) if num == 1 else prompt_template

    plog(f"phase {num:02d}-{key}: sending...")
    messages.append({"role": "user", "content": prompt})

    text, failures = repair.generate_phase(messages, num, key, name, providers, plog)
    text, failures = _keep_better(out_path, text, failures, num, key, name, plog)

    out_path.write_text(text, encoding="utf-8")
    messages.append({"role": "assistant", "content": text})
    # This phase is complete -- shrink its just-sent full prompt (needed for the call that
    # just happened) to a short marker so it isn't re-sent in full on every later phase's
    # request. The real output right below it is untouched.
    messages[-2]["content"] = prompts.prompt_placeholder(num, key)
    plog(f"phase {num:02d}-{key}: done ({len(text)} chars) -> {out_path}")
    return text, failures


def _keep_better(out_path: Path, text: str, failures: list, num: int, key: str, name: str,
                 plog) -> tuple:
    """When --redo-phases set the previous version aside as <file>.bak, keep whichever of the
    two is actually better and drop the backup.

    "Better" = fewer failed spec checks; ties go to the longer text, because the failure this
    guards against is a regeneration that answers with a fraction of the content (a 622-char
    stub replacing a complete 25KB phase, observed 2026-08-08) while tripping the same number
    of checks as the real thing it overwrote.

    Without this, --redo-phases was a one-way destructive operation: the old file was deleted
    up front and whatever came back took its place, good or not.
    """
    backup = out_path.with_suffix(".docx.bak")
    if not backup.exists():
        return text, failures

    old_text = backup.read_text(encoding="utf-8")
    from . import specs
    old_failures = specs.run_checks(num, key, name, old_text)

    new_better = (len(failures), -len(text)) <= (len(old_failures), -len(old_text))
    if new_better:
        plog(f"phase {num:02d}-{key}: keeping the NEW output "
             f"({len(failures)} failed check(s), {len(text)} chars) over the previous version "
             f"({len(old_failures)} failed, {len(old_text)} chars)")
        backup.unlink()
        return text, failures

    plog(f"phase {num:02d}-{key}: ⚠ regeneration was WORSE "
         f"({len(failures)} failed check(s), {len(text)} chars) than the version it replaced "
         f"({len(old_failures)} failed, {len(old_text)} chars) -- restoring the previous "
         f"version and discarding the new one")
    backup.unlink()
    return old_text, old_failures


def run_phase_11(name: str, providers, proj_dir: Path) -> tuple:
    """Phase 11 (Validation & QA) as four smaller, sequential API calls (PHASE11_STAGES)
    instead of one call appended to the full 10-phase running conversation.

    History of this design, in the order things were actually tried:
      1. Single call appending to the full 10-phase conversation -- failed with an opaque JSON
         parse error (later traced to an HTML fallback page from a misconfigured base URL).
      2. Split into 2 calls with fresh, narrowly-scoped context per call. Built for a
         request-SIZE hypothesis that turned out wrong for the failures being chased, but the
         "fresh context read from disk, not accumulated chat" technique was sound and stays.
      3. Real root cause of the original failures: ANTHROPIC_BASE_URL had been corrupted (a
         stray "export" appended by a copy-paste), so every request hit a nonexistent path and
         the gateway's SPA served its own frontend HTML back with HTTP 200 -- nothing to do
         with size, headers, or the model.
      4. With the URL fixed, a NEW and real failure appeared: HTTP 504 on stage 11a,
         reproducible. Measured cause: the backend is slow (~2-6 tok/s observed) and 11a's ASK
         was a much larger completion than one ordinary phase. The bottleneck is generation
         TIME, so each stage's OUTPUT ask had to shrink too -- hence four stages, each roughly
         one ordinary phase's worth of output.

    Each stage gets a freshly built, narrowly-scoped context read from the phase files on
    disk for ITS OWN phase range, plus only the immediately-preceding stage's response. No
    fact is dropped: every stage examines its assigned phases' full raw text, and a later
    stage's link back to earlier phases is via the accumulated findings text.

    Returns (combined_text_or_None, error_or_None).
    """
    def stage_tmp_path(stage_key: str) -> Path:
        return proj_dir / f"11-stage-{stage_key}.tmp"

    # Every stage's own response is kept and concatenated: each stage is asked only for NEW
    # sections, never to reprint what came before, so the assembled document needs all four.
    # (An earlier version kept only the final stage's response, silently dropping every raw
    # Inventory listing from 11a-11c -- exactly the value loss this design exists to avoid.)
    all_responses = []
    prior_response = None
    prior_stage_label = None
    for stage_key, prompt_file, phase_specs in config.PHASE11_STAGES:
        tmp_path = stage_tmp_path(stage_key)
        # Per-stage resumability: a stage's response is saved the moment it succeeds, so if a
        # LATER stage fails and the project is re-run, the completed stages load from disk
        # instead of burning a fresh call (and its PHASE_SLEEP_SECONDS wait) each time.
        if tmp_path.exists() and len(tmp_path.read_text(encoding="utf-8").strip()) >= config.MIN_PHASE_CHARS:
            response = tmp_path.read_text(encoding="utf-8")
            log(f"  [{name}] phase {stage_key}: already done, resuming from {tmp_path.name} "
                f"(no API call)")
        else:
            prompt = prompts.inject_phase_dataset(
                prompts.load_stage_prompt(prompt_file), proj_dir, phase_specs)
            if prior_response is None:
                messages = [{"role": "user", "content": prompt}]
            else:
                messages = [
                    {"role": "user", "content": f"[Phase {prior_stage_label} instructions and "
                                                f"its phase dataset were sent here; see that "
                                                f"stage's full findings below.]"},
                    {"role": "assistant", "content": prior_response},
                    {"role": "user", "content": prompt},
                ]
            try:
                response = call_with_retries(messages, providers,
                                             f"{name} phase {stage_key}",
                                             max_tokens=config.PHASE11_MAX_TOKENS,
                                             heavy=True)
            except Exception as e:  # noqa: BLE001
                return None, e
            tmp_path.write_text(response, encoding="utf-8")

        all_responses.append(response)
        prior_response = response
        prior_stage_label = stage_key
        if stage_key != config.PHASE11_STAGES[-1][0]:
            time.sleep(config.PHASE_SLEEP_SECONDS)

    # The Manifest only exists in the LAST stage's response (11d is the only stage asked to
    # produce it) -- pull it out and move it to the front, matching the real Arbitrum dossier's
    # structure (CIF VALIDATION REPORT v3.0 -> CIF MANIFEST v3.0 -> everything else).
    manifest, last_rest = prompts.extract_manifest_block(all_responses[-1])
    body_sections = [r.strip() for r in all_responses[:-1]] + [last_rest]
    if manifest:
        combined = (f"CIF VALIDATION REPORT v3.0\n\n---\n\n{manifest}\n\n---\n\n"
                    + "\n\n---\n\n".join(body_sections))
    else:
        combined = "\n\n---\n\n".join(r.strip() for r in all_responses)
    combined = prompts.ensure_project_header(combined, name)

    # Success -- the stage .tmp files are folded into the real 11-conflict.docx output and
    # would otherwise sit around as stale leftovers if Phase 11 were ever re-run.
    for stage_key, _, _ in config.PHASE11_STAGES:
        stage_tmp_path(stage_key).unlink(missing_ok=True)

    return combined, None
