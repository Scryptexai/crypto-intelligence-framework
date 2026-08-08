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


def run_phase(name: str, num: int, key: str, messages: list, proj_dir: Path, base_url: str,
              token: str, model: str, plog) -> tuple:
    """Generate one ordinary phase (1-10), self-repairing format failures, and save it.

    Appends the prompt + final output to `messages` (mutating it, as the running Track C
    conversation), shrinking the prompt to a placeholder once the answer is in context.

    Returns (text, remaining_failures).
    """
    out_path = proj_dir / f"{num:02d}-{key}.docx"
    prompt_template = prompts.load_phase_prompt(num, key)
    prompt = prompt_template.replace("<NAMA PROJECT>", name) if num == 1 else prompt_template

    plog(f"phase {num:02d}-{key}: sending...")
    messages.append({"role": "user", "content": prompt})

    text, failures = repair.generate_phase(messages, num, key, name, base_url, token, model, plog)
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


def run_phase_11(name: str, base_url: str, token: str, model: str, proj_dir: Path) -> tuple:
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
                response = call_with_retries(messages, base_url, token, model,
                                             f"{name} phase {stage_key}",
                                             max_tokens=config.PHASE11_MAX_TOKENS)
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
