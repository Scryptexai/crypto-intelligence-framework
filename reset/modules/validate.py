"""
validate.py — the project-level quality gate run after all 10 phases exist.

specs.py checks ONE phase as it comes off the wire (so it can be repaired immediately);
this module checks the FINISHED project against the same real extractors, and is what
decides whether a project is allowed into data_project/ and onward to the database.

Both layers are kept because they fail differently: a phase can pass its own check and
still leave the project short (e.g. phase 9 parses its Decision Timeline but the file was
truncated before Strategic Trade-offs), and a project assembled from resumed files that
predate a prompt fix never went through the per-phase check at all.
"""
from pathlib import Path

from . import specs

import ingest as _ingest  # OPTIONAL_PHASE_KEYS -- phases that may legitimately be absent
import extract_entities as _extract_entities
import extract_events as _extract_events
import extract_decision_events as _extract_decision_events
import extract_knowledge as _extract_knowledge


def verify_10_phases(name: str, proj_dir: Path) -> tuple:
    """Runs phases 2/3/9/10 through the real extractors -- these are the phases with a strict
    machine-format contract a model can drift away from (markdown headers, missing item
    numbers, wrong field labels) while still writing genuinely researched, well-cited prose
    that sails through tools/ingest.py's citation-density check. Confirmed live, 2026-08-05:
    all four of Blast's phases 2/3/9/10 passed that check yet extracted zero rows each.

    Returns (all_ok, report) -- report always carries all four keys with the extracted count,
    0 when the phase file is missing or nothing parsed, so a caller can log exactly what is
    short even when all_ok is False.
    """
    report = {"entities": 0, "events": 0, "decisions": 0, "knowledge": 0}

    entity_text = specs.wrap_phase_file(proj_dir, 2, "entity")
    if entity_text:
        rows = (_extract_entities.parse_entities(entity_text, name)
                or _extract_entities.parse_entities_block(entity_text, name))
        report["entities"] = len(rows)

    history_text = specs.wrap_phase_file(proj_dir, 3, "history")
    if history_text:
        report["events"] = len(_extract_events.parse_events(history_text, name.lower()))

    behavioral_path = proj_dir / "09-behavioral.docx"
    if behavioral_path.exists():
        report["decisions"] = len(_extract_decision_events.parse_keputusan_events(
            behavioral_path.read_text(encoding="utf-8"), name))

    knowledge_text = specs.wrap_phase_file(proj_dir, 10, "knowledge")
    if knowledge_text:
        report["knowledge"] = len(_extract_knowledge.parse_knowledge(knowledge_text, name))

    return all(v > 0 for v in report.values()), report


def diagnose_project(name: str, proj_dir: Path) -> dict:
    """Per-phase verdict for a project already on disk -- what is missing, empty, junk, or
    malformed, without calling the API. This is the report `--audit` prints, and the basis
    for deciding which specific phases need regenerating rather than restarting a project.

    Verdicts: "missing", "empty", plus any failed check names from specs.run_checks, or "ok".
    """
    out = {}
    from . import config
    for num, key in config.PHASES:
        if num in (11, 12):
            # Audited separately, by cli._audit_json's phase11/phase12 buckets.
            #
            # Phase 12 joined phase 11 here on 2026-08-11, when adding the price_block check
            # reproduced L3 in a new shape: a phase-12 file that FAILS its checks marked the
            # project broken(12), which dropped it out of `clean`, out of phase11_done, and
            # therefore out of phase12_bad -- the one bucket that would have regenerated it.
            # `--stages phase12` printed "13 broken" and "nothing to do" in the same run.
            #
            # A phase cannot be graded in two places that disagree about the consequence. The
            # phase11/phase12 buckets own both because they are what the driver acts on; a
            # failure there produces a targeted --redo-phases, whereas a failure here produces
            # a project the driver refuses to touch.
            continue
        path = proj_dir / f"{num:02d}-{key}.docx"
        if not path.exists():
            # An OPTIONAL phase that was never generated is not a defect. Missed when Phase 12
            # landed, and it broke the whole pipeline within the hour: every one of the 27
            # projects turned "broken(12)", which emptied phase11_todo, which made
            # `--stages phase11` report "nothing to do" and skip the entire queue. A phase
            # added today cannot retroactively invalidate work finished yesterday -- the same
            # rule ingest.py's OPTIONAL_PHASE_KEYS already encodes, applied here too.
            if key in _ingest.OPTIONAL_PHASE_KEYS:
                continue
            out[f"{num:02d}-{key}"] = ["missing"]
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text.strip()) < config.MIN_PHASE_CHARS:
            # Same reasoning as the missing case: an empty scaffold for an optional phase is
            # the absence of that phase, not a broken one. Covered explicitly because
            # data_project folders routinely carry 0-byte placeholders (every project has one
            # for 11-conflict.docx), so the moment anything creates 12-airdrop.docx as a
            # scaffold the "missing" branch above stops firing and this one takes over.
            if key in _ingest.OPTIONAL_PHASE_KEYS:
                continue
            out[f"{num:02d}-{key}"] = ["empty"]
            continue
        failed = specs.run_checks(num, key, name, text)
        out[f"{num:02d}-{key}"] = [c.name for c, _ in failed] or ["ok"]
    return out
