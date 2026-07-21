#!/usr/bin/env python3
"""
ingest.py — batch auto-ingest: raw .docx/.pdf folder -> CIF deep dossiers. NO LLM.

Why this works without an LLM: the *reasoning* is already done by the Gemini 22-section
report (causality, §15 POV matrix, §19 knowledge extraction, §20 transferable rules,
§22 evidence levels). Claude's ingest job is mostly transform+file, which is deterministic:
  extract .docx -> parse the 23 numbered sections -> re-emit in CIF dossier format with
  the section->ontology cross-links auto-inserted -> archive the source -> rebuild JSON.

This gets ~90-95% of a hand-crafted dossier's value. What it does NOT do: distil/condense,
invent cross-links beyond the fixed map, or catch subtle inconsistencies — run a periodic
LLM/human QC pass on a sample for that. It never fabricates: output is the source, restructured.

Usage:
    python3 tools/ingest.py                     # process doc_backup/inbox/*.docx|pdf
    python3 tools/ingest.py --input PATH ...     # a folder or individual files
    python3 tools/ingest.py --force              # overwrite existing dossiers
    python3 tools/ingest.py --no-build           # skip the build_json/backtest rebuild
"""
import argparse, datetime, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import extract  # reuse extract_docx / extract_pdf / normalise

CASESTUDIES = ROOT / "examples" / "CaseStudies"
ARCHIVE = ROOT / "doc_backup" / "deep"
INBOX = ROOT / "doc_backup" / "inbox"

# section number -> docs/ cross-links (from docs/Protocol/Deep-Research-Brief.md mapping)
SECTION_REF = {
    2: "context (why it existed)",
    3: "`docs/Ontology/Identity.md`, `docs/Ontology/Team.md`",
    4: "`docs/Innovation/*`",
    5: "`docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`",
    6: "`docs/Ontology/Funding.md`",
    7: "`docs/Ontology/Community.md`, `docs/Success/Community.md`",
    8: "`docs/Meta/Narratives.md`",
    9: "`docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`",
    10: "`docs/Ontology/Technology.md`, `docs/Innovation/Execution.md`",
    11: "`docs/Ontology/Tokenomics.md`",
    12: "`docs/Ontology/Incentives.md`, `docs/Patterns/Points.md`, `docs/Patterns/Mining.md`, `docs/Patterns/Referral.md`",
    13: "`docs/TokenLifecycle/*`, `docs/MarketBehaviour/*`, `docs/Valuation/*`",
    14: "`docs/Ontology/Revenue.md`, `docs/Ontology/Adoption.md`, `docs/Ontology/Metrics.md`",
    15: "`docs/Success/*` (POV Success-Matrix)",
    16: "timeline",
    17: "`docs/Ontology/*` (current snapshot)",
    18: "`docs/Patterns/*`",
    19: "`docs/Patterns/*`, `docs/Ontology/*`, `docs/Schema/*`",
    20: "`docs/Reasoning/*` (rule candidates)",
    21: "research-gap field",
    22: "`docs/Reasoning/Confidence.md`",
    23: "provenance",
}

def extract_source(path: Path) -> str:
    low = path.suffix.lower()
    if low == ".docx":
        raw = extract.extract_docx(str(path))
    elif low == ".pdf":
        raw = extract.extract_pdf(str(path))
    else:
        raise ValueError(f"unsupported: {path.name}")
    return extract.normalise(raw)

def split_sections(md: str):
    """Return ordered [(num, title, body)] from '## N Title' headings."""
    parts = re.split(r"^##\s+(\d{1,2})\s+(.+)$", md, flags=re.M)
    # parts = [pre, num, title, body, num, title, body, ...]
    out = []
    for i in range(1, len(parts), 3):
        num = int(parts[i]); title = parts[i + 1].strip(); body = parts[i + 2].strip()
        out.append((num, title, body))
    return out

def project_name(path: Path) -> str:
    stem = path.stem  # filename without extension
    return stem.split("_")[0].strip() or stem

def build_dossier(name: str, sections, src_rel: str, stats: str) -> str:
    today = datetime.date.today().strftime("%Y-%m")
    head = (
        f"# {name} — Deep Case Study\n\n"
        f"**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**\n"
        f"**Source:** Deep Research (Gemini), 22-section brief. "
        f"**Auto-ingested** by `tools/ingest.py` (deterministic, no LLM) — structure & cross-links applied "
        f"mechanically; the reasoning is the source report's.\n"
        f"**Raw source archived:** `{src_rel}`.\n"
        f"**Input note:** {stats}\n\n"
        f"> Knowledge artifact (real curated data). Faithful restructure of the source into CIF format — "
        f"no fabrication, no distillation. Sections map to the `docs/` ontology via the fixed brief mapping. "
        f"Conforms to `templates/CaseStudyTemplate.md`. Consider a periodic LLM/human QC pass.\n\n---\n"
    )
    body = []
    for num, title, text in sections:
        ref = SECTION_REF.get(num)
        body.append(f"\n## {num} {title}")
        if ref:
            body.append(f"_ref: {ref}_")
        body.append("")
        body.append(text)
    return head + "\n".join(body).rstrip() + "\n"

def process(path: Path, force: bool):
    name = project_name(path)
    out = CASESTUDIES / f"{name}.md"
    if out.exists() and not force:
        return ("skip", name, "dossier exists (use --force)")
    md = extract_source(path)
    sections = split_sections(md)
    if len(sections) < 5:
        return ("warn", name, f"only {len(sections)} sections detected — check Input Formatting Contract")
    # archive the raw source (if not already inside doc_backup/deep)
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    src_name = path.name if "_" in path.stem else f"{name}_{datetime.date.today():%Y-%m}_gemini{path.suffix}"
    archived = ARCHIVE / src_name
    if path.resolve() != archived.resolve():
        shutil.copy2(path, archived)
    src_rel = f"doc_backup/deep/{archived.name}"
    stats = f"extracted via tools/extract.py — {len(md)} chars, {len(sections)} sections."
    out.write_text(build_dossier(name, sections, src_rel, stats), encoding="utf-8")
    return ("ok", name, f"{len(sections)} sections -> examples/CaseStudies/{name}.md")

def main():
    ap = argparse.ArgumentParser(description="Batch auto-ingest raw docx/pdf -> CIF deep dossiers.")
    ap.add_argument("--input", nargs="*", help="folder(s) or file(s); default doc_backup/inbox/")
    ap.add_argument("--force", action="store_true", help="overwrite existing dossiers")
    ap.add_argument("--no-build", action="store_true", help="skip build_json + backtest rebuild")
    args = ap.parse_args()

    targets = []
    inputs = args.input or [str(INBOX)]
    for inp in inputs:
        p = Path(inp)
        if p.is_dir():
            targets += sorted([*p.glob("*.docx"), *p.glob("*.pdf")])
        elif p.is_file():
            targets.append(p)
    if not targets:
        print(f"No .docx/.pdf found. Drop files in {INBOX} or pass --input PATH.")
        return

    CASESTUDIES.mkdir(parents=True, exist_ok=True)
    print(f"ingest: {len(targets)} file(s)\n" + "-" * 60)
    done = []
    for t in targets:
        status, name, msg = process(t, args.force)
        icon = {"ok": "✅", "skip": "⏭️", "warn": "⚠️"}[status]
        print(f"{icon} {name:16s} {msg}")
        if status == "ok":
            done.append(name)
    print("-" * 60)
    print(f"ingested {len(done)} dossier(s): {', '.join(done) or '—'}")

    if done and not args.no_build:
        print("\nrebuilding JSON + running backtest...")
        subprocess.run([sys.executable, str(ROOT / "tools" / "build_json.py")], check=False)
        subprocess.run([sys.executable, str(ROOT / "tools" / "backtest.py")], check=False)
    if done:
        print("\nNote: build_json.py auto-discovers new dossiers from examples/CaseStudies/ — "
              "no DatasetIndex edit needed for the pipeline. Refine category/era in DatasetIndex.md when convenient.")

if __name__ == "__main__":
    main()
