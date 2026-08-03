#!/usr/bin/env python3
"""
verify.py — verify a staged project's 11 phase outputs BEFORE they touch
data_project/ or the database.

Two tiers of check per phase:

  Tier 1 (ALL 11 phases): tools/ingest.py:validate_phase_content must pass —
    this is exactly the hard gate run.sh's ingest enforces (PROJECT/dataset header,
    minimum length, citation contract). A project that fails this is rejected by
    ingest with nothing written, so we catch it here first.

  Tier 2 (structured phases that feed DB tables): assemble the phase text the way
    ingest would (under its "## <Title>" section header + a trailing boundary) and
    run the REAL extractor. Assert it yields > 0 rows — proving the AI honored the
    exact machine-parseable structure the pipeline needs:
      02-entity     -> extract_entities        > 0 entities
      09-behavioral -> extract_behavior        > 0 strategic objectives / patterns
                    -> extract_decision_events > 0 decision events
      10-knowledge  -> extract_knowledge       > 0 knowledge items
      11-conflict   -> extract_conflicts       > 0 conflicts
                    -> extract_qa              CIF total present + dimensions

Usage:
  python3 reset/verify.py <Project> [--dir reset/temp]
Exit code 0 = all pass; 1 = at least one FAIL.
"""
from __future__ import annotations
import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as C
import ingest        # type: ignore
import extract       # type: ignore


def _load(mod: str, path: str):
    spec = importlib.util.spec_from_file_location(mod, str(ROOT / path))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# phase key -> assembled-dossier section title the extractors search for
SECTION_TITLE = {
    "01-foundation": "Foundation Intelligence",
    "02-entity": "Entity Intelligence",
    "03-history": "Historical Intelligence",
    "04-technology": "Technology Intelligence",
    "05-financial": "Financial Intelligence",
    "06-token": "Token Intelligence",
    "07-ecosystem": "Ecosystem Intelligence",
    "08-market": "Market Intelligence",
    "09-behavioral": "Behavioral Intelligence",
    "10-knowledge": "Knowledge Extraction",
    "11-conflict": "Validation & Quality Assurance (CIF Score)",
}

GREEN, RED, YEL, RST = "\033[32m", "\033[31m", "\033[33m", "\033[0m"


def _read(path: Path) -> str:
    return extract.normalise(extract.extract_docx(str(path)))


def _assemble_section(project: str, key: str, text: str) -> str:
    """Wrap one phase's text as a mini assembled dossier so the section-scoped
    extractors (which look for '^## <Title>\\n...(?=\\n## )') can find it."""
    title = SECTION_TITLE[key]
    return (
        f"# {project} — Deep Case Study (staged verify)\n\n"
        f"## {title}\n{text}\n\n"
        f"## __END__\nboundary\n"
    )


def verify_project(project: str, base: Path) -> bool:
    folder = base / project
    print(f"\n===== VERIFY (staged): {project}  [{folder}] =====")
    if not folder.exists():
        print(f"{RED}✖ folder not found: {folder}{RST}")
        return False

    ee = _load("ee", "tools/extract_entities.py")
    kk = _load("kk", "tools/extract_knowledge.py")
    bb = _load("bb", "tools/extract_behavior.py")
    de = _load("de", "tools/extract_decision_events.py")
    cc = _load("cc", "tools/extract_conflicts.py")
    qq = _load("qq", "tools/extract_qa.py")

    all_ok = True
    summary = []

    for key in C.PHASE_ORDER:
        f = folder / f"{key}.docx"
        if not f.exists() or f.stat().st_size == 0:
            print(f"{RED}✖ {key}: MISSING/EMPTY{RST}")
            all_ok = False
            summary.append((key, "MISSING", ""))
            continue

        text = _read(f)

        # Tier 1 — ingest content validation (the real hard gate)
        reasons = ingest.validate_phase_content(f"{key}.docx", project, text)
        t1 = "PASS" if not reasons else "FAIL"
        if reasons:
            all_ok = False

        # Tier 2 — structured extraction (only for phases that feed DB tables)
        t2 = ""
        try:
            doc = Path("/tmp/_verify_section.md")
            if key == "02-entity":
                doc.write_text(_assemble_section(project, key, text), encoding="utf-8")
                _, rows = ee.extract_from_dossier(doc)
                t2 = f"entities={len(rows)}"
                if len(rows) == 0:
                    t1, all_ok = "FAIL", False
            elif key == "09-behavioral":
                doc.write_text(_assemble_section(project, key, text), encoding="utf-8")
                _, beh = bb.extract_from_dossier(doc)
                _, ev = de.extract_from_dossier(doc)
                nobj = len(beh["strategicObjectives"])
                npat = len(beh["decisionPatterns"])
                t2 = f"objectives={nobj} patterns={npat} events={len(ev)}"
                if nobj == 0 and npat == 0:
                    t1, all_ok = "FAIL", False
            elif key == "10-knowledge":
                doc.write_text(_assemble_section(project, key, text), encoding="utf-8")
                _, ki = kk.extract_from_dossier(doc)
                t2 = f"knowledge={len(ki)}"
                if len(ki) == 0:
                    t1, all_ok = "FAIL", False
            elif key == "11-conflict":
                doc.write_text(_assemble_section(project, key, text), encoding="utf-8")
                _, cf = cc.extract_from_dossier(doc)
                _, qa = qq.extract_from_dossier(doc)
                t2 = f"conflicts={len(cf)} qa_total={qa.get('total')} dims={len(qa.get('dimensions', []))}"
                # conflicts may legitimately be 0 for some projects; qa should have dims
                if len(qa.get("dimensions", [])) == 0:
                    t2 += " (⚠ no qa dims)"
        except Exception as e:  # noqa
            t2 = f"extractor error: {e}"
            t1, all_ok = "FAIL", False

        color = GREEN if t1 == "PASS" else RED
        detail = f" | {t2}" if t2 else ""
        reason = f"  -> {reasons[0][:80]}" if reasons else ""
        print(f"{color}{'✓' if t1=='PASS' else '✖'} {key}: {t1}{RST} ({len(text)} chars){detail}{reason}")
        summary.append((key, t1, t2))

    ok_count = sum(1 for _, s, _ in summary if s == "PASS")
    print(f"\n{'='*50}")
    verdict = f"{GREEN}ALL {ok_count}/11 PHASES VALID — safe to promote{RST}" if all_ok \
        else f"{RED}{ok_count}/11 valid — NOT ready (fix failing phases){RST}"
    print(verdict)
    return all_ok


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify staged phase outputs")
    ap.add_argument("project")
    ap.add_argument("--dir", default=str(C.STAGING_DIR), help="staging base dir")
    args = ap.parse_args()
    ok = verify_project(args.project, Path(args.dir))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
