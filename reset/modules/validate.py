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
        if num == 11:
            continue  # deliberately deferred; has no extractor contract to test
        path = proj_dir / f"{num:02d}-{key}.docx"
        if not path.exists():
            out[f"{num:02d}-{key}"] = ["missing"]
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text.strip()) < config.MIN_PHASE_CHARS:
            out[f"{num:02d}-{key}"] = ["empty"]
            continue
        failed = specs.run_checks(num, key, name, text)
        out[f"{num:02d}-{key}"] = [c.name for c, _ in failed] or ["ok"]
    return out
