#!/usr/bin/env python3
"""
ingest.py — batch auto-ingest: raw .docx/.pdf -> CIF artifacts. NO LLM.

The reasoning already lives in the source report (Gemini deep / batch, or Grok sentiment); this program
only transforms+files it, deterministically. Three types, routed by inbox subfolder (or --type):

  deep      doc_backup/inbox/deep/       1 project/file (22 sections) -> examples/CaseStudies/<Project>.md
  batch     doc_backup/inbox/batch/      N projects/file (PROJECT: …) -> examples/Pioneer/<Project>.md
  sentiment doc_backup/inbox/sentiment/  1 project/file (8 sections)  -> examples/Sentiment/<Project>.md

Anti-duplicate: a report whose output already exists is skipped, so re-running only processes NEW files.

Usage:
    python3 tools/ingest.py                       # process all three inbox subfolders
    python3 tools/ingest.py --type deep --input P # a folder or files, forced type
    python3 tools/ingest.py --force               # overwrite existing outputs
    python3 tools/ingest.py --no-build            # skip build_json + backtest rebuild
"""
import argparse, datetime, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import extract

EXAMPLES = ROOT / "examples"
INBOX = ROOT / "doc_backup" / "inbox"
DEST = {"deep": EXAMPLES / "CaseStudies", "batch": EXAMPLES / "Pioneer", "sentiment": EXAMPLES / "Sentiment"}
ARCHIVE = {"deep": ROOT / "doc_backup" / "deep", "batch": ROOT / "doc_backup" / "batch",
           "sentiment": ROOT / "doc_backup" / "sentiment"}

# deep 22/23-section -> docs/ cross-links
DEEP_REF = {
    2: "context (why it existed)", 3: "`docs/Ontology/Identity.md`, `docs/Ontology/Team.md`",
    4: "`docs/Innovation/*`", 5: "`docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`",
    6: "`docs/Ontology/Funding.md`", 7: "`docs/Ontology/Community.md`, `docs/Success/Community.md`",
    8: "`docs/Meta/Narratives.md`", 9: "`docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`",
    10: "`docs/Ontology/Technology.md`, `docs/Innovation/Execution.md`", 11: "`docs/Ontology/Tokenomics.md`",
    12: "`docs/Ontology/Incentives.md`, `docs/Patterns/Points.md`, `docs/Patterns/Mining.md`, `docs/Patterns/Referral.md`",
    13: "`docs/TokenLifecycle/*`, `docs/MarketBehaviour/*`, `docs/Valuation/*`",
    14: "`docs/Ontology/Revenue.md`, `docs/Ontology/Adoption.md`, `docs/Ontology/Metrics.md`",
    15: "`docs/Success/*` (POV Success-Matrix)", 16: "timeline", 17: "`docs/Ontology/*` (current snapshot)",
    18: "`docs/Patterns/*`", 19: "`docs/Patterns/*`, `docs/Ontology/*`, `docs/Schema/*`",
    20: "`docs/Reasoning/*` (rule candidates)", 21: "research-gap field", 22: "`docs/Reasoning/Confidence.md`",
    23: "provenance",
}
# sentiment 8-section -> docs/ cross-links
SENT_REF = {
    1: "provenance & coverage", 2: "`docs/TokenLifecycle/*`, `docs/Meta/MarketCycles.md`",
    3: "`docs/Ontology/Community.md`, `docs/Success/Community.md`", 4: "`docs/Ontology/Community.md`",
    5: "`docs/Meta/Hype.md`, `docs/Reasoning/*` (divergence signal)", 6: "`docs/Patterns/Points.md` (farmed engagement)",
    7: "`docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `examples/PatternRegistry.md`",
    8: "`docs/Reasoning/Confidence.md`",
}

def extract_source(path: Path) -> str:
    low = path.suffix.lower()
    if low == ".docx":
        return extract.normalise(extract.extract_docx(str(path)))
    if low == ".pdf":
        return extract.normalise(extract.extract_pdf(str(path)))
    raise ValueError(f"unsupported: {path.name}")

def split_sections(md: str):
    parts = re.split(r"^##\s+(\d{1,2})\s+(.+)$", md, flags=re.M)
    return [(int(parts[i]), parts[i+1].strip(), parts[i+2].strip()) for i in range(1, len(parts), 3)]

def project_name(path: Path) -> str:
    return path.stem.split("_")[0].strip() or path.stem

def _archive(path: Path, kind: str, name: str) -> str:
    ARCHIVE[kind].mkdir(parents=True, exist_ok=True)
    src_name = path.name if "_" in path.stem else f"{name}_{datetime.date.today():%Y-%m}{path.suffix}"
    dest = ARCHIVE[kind] / src_name
    if path.resolve() != dest.resolve():
        shutil.copy2(path, dest)
    return f"doc_backup/{kind}/{dest.name}"

def _sections_md(sections, refmap):
    body = []
    for num, title, text in sections:
        body.append(f"\n## {num} {title}")
        if refmap.get(num):
            body.append(f"_ref: {refmap[num]}_")
        body.append("")
        body.append(text)
    return "\n".join(body).rstrip() + "\n"

def process_deep(path, force):
    name = project_name(path); out = DEST["deep"] / f"{name}.md"
    if out.exists() and not force:
        return [("skip", name, "dossier exists")]
    md = extract_source(path); secs = split_sections(md)
    if len(secs) < 5:
        return [("warn", name, f"only {len(secs)} sections — check Input Formatting Contract")]
    src = _archive(path, "deep", name)
    head = (f"# {name} — Deep Case Study\n\n"
            f"**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**\n"
            f"**Source:** Deep Research (Gemini), 22-section brief. **Auto-ingested** by `tools/ingest.py` "
            f"(deterministic, no LLM) — structure & cross-links applied mechanically; the reasoning is the "
            f"source report's.\n**Raw source archived:** `{src}`.\n"
            f"**Sentiment companion:** `examples/Sentiment/{name}.md` (if present).\n"
            f"**Input note:** extracted via `tools/extract.py` — {len(md)} chars, {len(secs)} sections.\n\n"
            f"> Faithful restructure into CIF format — no fabrication, no distillation. Consider a periodic QC pass.\n\n---\n")
    out.write_text(head + _sections_md(secs, DEEP_REF), encoding="utf-8")
    return [("ok", name, f"{len(secs)} sections -> examples/CaseStudies/{name}.md")]

def process_sentiment(path, force):
    name = project_name(path); out = DEST["sentiment"] / f"{name}.md"
    if out.exists() and not force:
        return [("skip", name, "sentiment exists")]
    md = extract_source(path); secs = split_sections(md)
    if len(secs) < 3:
        return [("warn", name, f"only {len(secs)} sections — check Sentiment Brief contract")]
    src = _archive(path, "sentiment", name)
    head = (f"# {name} — Sentiment Dossier\n\n"
            f"**CIF Dataset — Sentiment · Tier: Sentiment (companion)**\n"
            f"**Source:** Grok/X sentiment reconstruction, 8-section Sentiment Brief. **Auto-ingested** "
            f"(deterministic, no LLM).\n**Raw source archived:** `{src}`.\n"
            f"**Fundamental companion:** `examples/CaseStudies/{name}.md`.\n"
            f"**Input note:** {len(md)} chars, {len(secs)} sections.\n\n"
            f"> Sentiment is triangulated & evidence-tagged (see `docs/Protocol/Sentiment-Brief.md`). "
            f"Verified anchors (URL) are separated from sampled mood; no fabricated quotes. X skews retail/hype.\n\n---\n")
    out.write_text(head + _sections_md(secs, SENT_REF), encoding="utf-8")
    return [("ok", name, f"{len(secs)} sections -> examples/Sentiment/{name}.md")]

def process_batch(path, force):
    """Split a multi-project batch doc on 'PROJECT: <Name>' delimiters -> one Pioneer profile each."""
    md = extract_source(path)
    chunks = re.split(r"(?im)^\s*PROJECT:\s*(.+?)\s*$", md)
    src = _archive(path, "batch", project_name(path))
    results = []
    if len(chunks) < 3:
        return [("warn", path.stem, "no 'PROJECT: <Name>' delimiters — see batch contract in inbox README")]
    for i in range(1, len(chunks), 2):
        name = chunks[i].strip(); block = chunks[i+1].strip()
        safe = re.sub(r"[^A-Za-z0-9()./ -]", "", name).strip().replace(" ", "-") or f"proj{i}"
        out = DEST["batch"] / f"{safe}.md"
        if out.exists() and not force:
            results.append(("skip", name, "profile exists")); continue
        head = (f"# {name}\n\n"
                f"**CIF Dataset — Summary Profile · Tier: Summary**\n"
                f"**Source:** Deep Research (Gemini) batch. **Auto-ingested** by `tools/ingest.py` "
                f"(deterministic, no LLM).\n**Raw source archived:** `{src}`.\n\n"
                f"_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Classification.md`, `docs/Ontology/Incentives.md`_\n\n---\n\n")
        out.write_text(head + block + "\n", encoding="utf-8")
        results.append(("ok", name, f"-> examples/Pioneer/{safe}.md"))
    return results

PROCESSORS = {"deep": process_deep, "batch": process_batch, "sentiment": process_sentiment}

def gather(inputs, kind_hint):
    """Yield (path, kind)."""
    for inp in inputs:
        p = Path(inp)
        if p.is_dir():
            for f in sorted([*p.glob("*.docx"), *p.glob("*.pdf")]):
                yield f, kind_hint
        elif p.is_file():
            yield p, kind_hint

def main():
    ap = argparse.ArgumentParser(description="Batch auto-ingest raw docx/pdf -> CIF artifacts.")
    ap.add_argument("--type", choices=["deep", "batch", "sentiment"], help="force type (for --input)")
    ap.add_argument("--input", nargs="*", help="folder(s)/file(s); default = the three inbox subfolders")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--no-build", action="store_true")
    args = ap.parse_args()

    jobs = []
    if args.input:
        if not args.type:
            sys.exit("--input requires --type deep|batch|sentiment")
        jobs = list(gather(args.input, args.type))
    else:
        for kind in ("deep", "batch", "sentiment"):
            jobs += list(gather([INBOX / kind], kind))

    if not jobs:
        print(f"No .docx/.pdf found. Drop files in {INBOX}/(deep|batch|sentiment)/ or pass --input --type.")
        return

    print(f"ingest: {len(jobs)} file(s)\n" + "-" * 64)
    counts = {"ok": 0, "skip": 0, "warn": 0}
    icons = {"ok": "✅", "skip": "⏭️", "warn": "⚠️"}
    for path, kind in jobs:
        for status, name, msg in PROCESSORS[kind](path, args.force):
            print(f"{icons[status]} [{kind:9s}] {name:18s} {msg}")
            counts[status] += 1
    print("-" * 64)
    print(f"new: {counts['ok']}  skipped(dup): {counts['skip']}  warnings: {counts['warn']}")

    if counts["ok"] and not args.no_build:
        print("\nrebuilding JSON + backtest...")
        subprocess.run([sys.executable, str(ROOT / "tools" / "build_json.py")], check=False)
        subprocess.run([sys.executable, str(ROOT / "tools" / "backtest.py")], check=False)

if __name__ == "__main__":
    main()
