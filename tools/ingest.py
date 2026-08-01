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
# deep v2 — Causal Event Graph 7-section format (docs/Protocol/Deep-Research-Brief.md "Format v2")
DEEP_V2_REF = {
    1: "`docs/Ontology/Context.md` (era/conditions snapshot)",
    2: "`docs/Innovation/*`, `docs/Ontology/Technology.md`, `docs/Ontology/Revenue.md`",
    3: "`docs/Ontology/DecisionEvent.md` (extract each DEV-NNN as one instance)",
    4: "`docs/Success/*` (POV Success-Matrix), `docs/Ontology/Community.md`",
    5: "`docs/Ontology/Metrics.md`, `docs/TokenLifecycle/*`, `docs/MarketBehaviour/*`, `docs/Valuation/*`",
    6: "`docs/Ontology/Hidden.md`, `docs/Reasoning/Confidence.md` (preserve disagreement, don't resolve it)",
    7: "synthesis — the only section allowed to conclude; ref `docs/Reasoning/Prediction.md`",
}
V2_SIGNAL = re.compile(r"CAUSAL EVENT GRAPH|CONTEXT\s*&\s*ENVIRONMENT|DECISION EVENTS", re.I)

def is_v2(sections) -> bool:
    """Heuristic: v2 (Causal Event Graph) has ~7 sections with distinctive ALL-CAPS titles."""
    return len(sections) <= 8 and any(V2_SIGNAL.search(t) for _, t, _ in sections)

# deep v3 — Dependency Pipeline (docs/Protocol/Deep-Research-Brief.md "Format v3")
# Ordered by information dependency (not topic) -- see brief for the full rationale.
PHASE_KEYS = ["foundation", "entity", "history", "technology", "financial", "token",
              "ecosystem", "market", "behavioral", "knowledge", "conflict"]
PHASE_META = {
    "foundation":  {"title": "Foundation Intelligence",
                     "ref": "`docs/Ontology/Identity.md`, `docs/Ontology/Team.md`"},
    "entity":      {"title": "Entity Intelligence",
                     "ref": "`docs/Ontology/Relationships.md` (entity graph)"},
    "history":     {"title": "Historical Intelligence",
                     "ref": "`docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)"},
    "technology":  {"title": "Technology Intelligence", "ref": "`docs/Ontology/Technology.md`"},
    "financial":   {"title": "Financial Intelligence",
                     "ref": "`docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`"},
    "token":       {"title": "Token Intelligence", "ref": "`docs/Ontology/Tokenomics.md`"},
    "ecosystem":   {"title": "Ecosystem Intelligence",
                     "ref": "`docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`"},
    "market":      {"title": "Market Intelligence",
                     "ref": "`docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`"},
    "behavioral":  {"title": "Behavioral Intelligence",
                     "ref": "`docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions"},
    "knowledge":   {"title": "Knowledge Extraction", "ref": "`docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)"},
    "conflict":    {"title": "Conflicting Evidence & Resolutions",
                     "ref": "`docs/Reasoning/Confidence.md` — INKONSISTENSI convention"},
}
OPEN_THREADS_RE = re.compile(r"(?im)^#{0,3}[^\n]{0,80}\bopen\s*threads?\b[^\n]*$")

def detect_phase_key(filename: str):
    """Match a phase key as a substring of the filename (case/punctuation-insensitive)."""
    key = re.sub(r"[^a-z]", "", filename.lower()).replace("behaviour", "behavior")
    for k in PHASE_KEYS:
        if k in key:
            return k
    return None

BIBLIOGRAPHY_RE = re.compile(r"(?im)^#{0,3}\s*(karya yang dikutip|daftar pustaka|sources?|references?|bibliography)\s*$")

def split_open_threads(text: str):
    """Split a phase document into (body, [threads]) on its 'Open Threads' heading, if present.
    Handles two shapes seen in real output: bulleted lines ("- ...") and plain narrative paragraphs
    with no bullets at all -- a strict bullets-only parser silently drops the entire section when a
    model writes threads as prose instead, which is real content loss, not a formatting nitpick. A
    trailing bibliography/citation-list heading (if Open Threads is followed by one) ends the
    threads section rather than being absorbed as more "threads"."""
    m = OPEN_THREADS_RE.search(text)
    if not m:
        return text.strip(), []
    body, tail = text[:m.start()].strip(), text[m.end():]

    b = BIBLIOGRAPHY_RE.search(tail)
    if b:
        tail = tail[:b.start()]

    lines = [ln.strip() for ln in tail.splitlines()]
    has_bullets = any(ln.startswith(("-", "*")) for ln in lines if ln)

    threads = []
    if has_bullets:
        # Bullet form: one thread per "- ..." line; a wrapped continuation line (doesn't start with
        # -/* but isn't blank) folds into the previous bullet instead of truncating it.
        for ln in lines:
            if not ln:
                continue
            if ln.startswith(("-", "*")):
                threads.append(ln.lstrip("-* \t"))
            elif threads:
                threads[-1] = f"{threads[-1]} {ln}"
    else:
        # Narrative form: no bullets anywhere -- treat each blank-line-separated paragraph as one
        # thread rather than discarding real content because it wasn't formatted as requested.
        for para in re.split(r"\n\s*\n", tail):
            p = " ".join(ln.strip() for ln in para.splitlines() if ln.strip())
            if p:
                threads.append(p)

    return body, threads

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

def norm(name: str) -> str:
    """Case/punctuation-insensitive key so 'BNBChain', 'BNB-Chain', 'bnb chain' collide as one project."""
    return re.sub(r"[^a-z0-9]", "", name.lower())

def find_existing(dest_dir: Path, name: str):
    """Anti-duplicate guard: find a file already representing this project even if its exact
    filename differs in case/punctuation from `name` (prevents silent near-duplicates at scale)."""
    if not dest_dir.exists():
        return None
    key = norm(name)
    for f in dest_dir.glob("*.md"):
        if f.name == "README.md":
            continue
        if norm(f.stem) == key:
            return f
    return None

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
    name = project_name(path)
    existing = find_existing(DEST["deep"], name)
    out = existing or (DEST["deep"] / f"{name}.md")
    if existing and not force:
        note = "" if existing.stem == name else f" (matched existing '{existing.stem}.md' — near-duplicate name)"
        return [("skip", name, f"dossier exists{note}")]
    md = extract_source(path); secs = split_sections(md)
    if len(secs) < 5:
        return [("warn", name, f"only {len(secs)} sections — check Input Formatting Contract")]
    v2 = is_v2(secs)
    refmap = DEEP_V2_REF if v2 else DEEP_REF
    brief_note = ("7-section Causal Event Graph brief (Format v2)" if v2
                  else "22-section brief")
    src = _archive(path, "deep", name)
    summary_dup = find_existing(DEST["batch"], name)
    supersede_note = (f"\n**Supersedes:** `examples/Pioneer/{summary_dup.name}` — same project now exists as "
                       f"a fuller Deep dossier; the Summary is redundant and should be reviewed for removal "
                       f"(not auto-deleted)." if summary_dup else "")
    head = (f"# {name} — Deep Case Study\n\n"
            f"**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**\n"
            f"**Source:** Deep Research (Gemini), {brief_note}. **Auto-ingested** by `tools/ingest.py` "
            f"(deterministic, no LLM) — structure & cross-links applied mechanically; the reasoning is the "
            f"source report's.\n**Raw source archived:** `{src}`.\n"
            f"**Sentiment companion:** `examples/Sentiment/{name}.md` (if present).{supersede_note}\n"
            f"**Input note:** extracted via `tools/extract.py` — {len(md)} chars, {len(secs)} sections"
            f"{' (v2 detected)' if v2 else ''}.\n\n"
            f"> Faithful restructure into CIF format — no fabrication, no distillation. Consider a periodic QC pass.\n\n---\n")
    out.write_text(head + _sections_md(secs, refmap), encoding="utf-8")
    msg = f"{len(secs)} sections -> examples/CaseStudies/{name}.md" + (" [v2]" if v2 else "")
    if summary_dup:
        msg += f"  ⚠ supersedes Pioneer/{summary_dup.name}"
    return [("ok", name, msg)]

def process_sentiment(path, force):
    name = project_name(path)
    existing = find_existing(DEST["sentiment"], name)
    out = existing or (DEST["sentiment"] / f"{name}.md")
    if existing and not force:
        note = "" if existing.stem == name else f" (matched existing '{existing.stem}.md' — near-duplicate name)"
        return [("skip", name, f"sentiment exists{note}")]
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
        existing = find_existing(DEST["batch"], safe)
        out = existing or (DEST["batch"] / f"{safe}.md")
        if existing and not force:
            note = "" if existing.stem == safe else f" (matched existing '{existing.stem}.md' — near-duplicate name)"
            results.append(("skip", name, f"profile exists{note}")); continue
        head = (f"# {name}\n\n"
                f"**CIF Dataset — Summary Profile · Tier: Summary**\n"
                f"**Source:** Deep Research (Gemini) batch. **Auto-ingested** by `tools/ingest.py` "
                f"(deterministic, no LLM).\n**Raw source archived:** `{src}`.\n\n"
                f"_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Classification.md`, `docs/Ontology/Incentives.md`_\n\n---\n\n")
        out.write_text(head + block + "\n", encoding="utf-8")
        results.append(("ok", name, f"-> examples/Pioneer/{safe}.md"))
    return results

def process_phased_project(folder: Path, force: bool, dest_dir: Path = None):
    """Assemble one project's dossier from its doc_backup/inbox/phased/<Project>/ folder — deterministic,
    no LLM. See docs/Protocol/Deep-Research-Brief.md 'Format v3 -- Dependency Pipeline'."""
    name = folder.name
    dest_dir = dest_dir or DEST["deep"]
    existing = find_existing(dest_dir, name)
    out = existing or (dest_dir / f"{name}.md")
    if existing and not force:
        note = "" if existing.stem == name else f" (matched existing '{existing.stem}.md' — near-duplicate name)"
        return [("skip", name, f"dossier exists{note}")]

    files = sorted([*folder.glob("*.docx"), *folder.glob("*.pdf")])
    if not files:
        return [("warn", name, "no phase files found in folder")]

    phases, all_threads, unmatched, archived = {}, [], [], []
    for f in files:
        key = detect_phase_key(f.stem)
        if not key:
            unmatched.append(f.name)
            continue
        body, threads = split_open_threads(extract_source(f))
        phases[key] = body
        all_threads.extend(f"[{key}] {t}" for t in threads)
        archived.append(_archive(f, "deep", f"{name}_{key}"))

    if not phases:
        return [("warn", name, f"no recognizable phase files (got: {', '.join(f.name for f in files)})")]

    order = [k for k in PHASE_KEYS if k in phases]
    body_md = []
    for k in order:
        meta = PHASE_META[k]
        body_md.append(f"\n## {meta['title']}\n_ref: {meta['ref']}_\n\n{phases[k]}")
    if all_threads:
        body_md.append("\n## Open Questions\n" + "\n".join(f"- {t}" for t in all_threads))

    missing = [k for k in PHASE_KEYS if k not in phases]
    summary_dup = find_existing(DEST["batch"], name)
    supersede_note = (f"\n**Supersedes:** `examples/Pioneer/{summary_dup.name}` — same project now exists as "
                       f"a fuller Deep dossier; the Summary is redundant and should be reviewed for removal "
                       f"(not auto-deleted)." if summary_dup else "")
    head = (
        f"# {name} — Deep Case Study (Phased)\n\n"
        f"**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**\n"
        f"**Source:** Deep Research (Gemini), Format v3 Dependency Pipeline "
        f"({len(order)}/{len(PHASE_KEYS)} phases: {', '.join(order)}). **Auto-assembled** by `tools/ingest.py` "
        f"(deterministic, no LLM) — each phase extracted and concatenated in dependency order per "
        f"`docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.\n"
        f"**Raw sources archived:** {', '.join(archived)}.\n"
        f"**Phases not run:** {', '.join(missing) if missing else 'none'}.{supersede_note}\n\n"
        f"> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the "
        f"Conflict Resolution phase itself states. Consider a periodic QC pass.\n\n---\n"
    )
    out.write_text(head + "\n".join(body_md).strip() + "\n", encoding="utf-8")
    msg = f"{len(order)} phases -> {out.relative_to(ROOT)}"
    if unmatched:
        msg += f"  ⚠ unmatched files: {', '.join(unmatched)}"
    if summary_dup:
        msg += f"  ⚠ supersedes Pioneer/{summary_dup.name}"
    return [("ok", name, msg)]

DATA_PROJECT_ROOT = ROOT / "data_project"
PHASE_FILE_RE = re.compile(r"^(\d{1,2})-([a-z]+)\.(docx|pdf)$", re.IGNORECASE)

def detect_phase_key_strict(filename: str) -> str:
    """Strict phase-file naming for data_project/<project>/: '<NN>-<key>.<ext>', key must be an
    EXACT match against PHASE_KEYS (not a substring test). Raises ValueError with an actionable
    message on any mismatch. Replaces the old fuzzy detect_phase_key(), which silently dropped
    '03-historical.docx' from the LayerZero dossier because "history" is not a substring of
    "historical" -- see doc_backup/inbox/phased/LayerZero/PROMPTS-LOG.md for the incident."""
    m = PHASE_FILE_RE.match(filename)
    if not m:
        raise ValueError(
            f"'{filename}' does not match the required '<NN>-<phasekey>.docx|pdf' naming "
            f"(e.g. '03-history.docx'). Valid phase keys: {', '.join(PHASE_KEYS)}."
        )
    key = m.group(2).lower().replace("behaviour", "behavior")
    if key not in PHASE_KEYS:
        raise ValueError(
            f"'{filename}': phase key '{key}' is not one of the 11 valid keys: "
            f"{', '.join(PHASE_KEYS)}."
        )
    return key

MIN_PHASE_CHARS = 400
EVIDENCE_TAG_RE = re.compile(r"\((?:HIGH|MEDIUM|LOW|TIDAK ADA KONFLIK)\)")
PROJECT_HEADER_RE = re.compile(r"(?im)^PROJECT:\s*(.+)$")
FALLBACK_PLACEHOLDER_RE = re.compile(r"\[sumber tidak dapat diverifikasi ulang\]", re.I)

def validate_phase_content(filename: str, project_name: str, text: str) -> list:
    """Content-level checks beyond filename matching -- the strict filename contract
    (detect_phase_key_strict) only proves a file is NAMED correctly, not that its content is real,
    belongs to this project, or meets the Deep Research Brief's citation contract. Catches the two
    failure classes actually observed this session: (1) near-zero-citation drafts that took 2-3
    rejected Gemini attempts each to catch by hand in LayerZero Phase 3/4/6 -- exactly the kind of
    defect a human reviewer can miss at 1000-project scale; (2) a wrong/misfiled project's content
    landing in this folder. Returns a list of FAIL reasons (empty = passed)."""
    reasons = []
    stripped = text.strip()
    if len(stripped) < MIN_PHASE_CHARS:
        reasons.append(
            f"content suspiciously short ({len(stripped)} chars, minimum {MIN_PHASE_CHARS}) -- "
            f"likely a broken/empty/placeholder extraction, not a real phase report"
        )

    m = PROJECT_HEADER_RE.search(text)
    if not m:
        reasons.append(
            "no 'PROJECT: <Name>' header found -- required by the Deep Research Brief format contract "
            "(see docs/Protocol/Deep-Research-Brief.md); cannot confirm which project this file belongs to"
        )
    else:
        declared = re.sub(r"[^a-z0-9]", "", m.group(1).lower())
        folder = re.sub(r"[^a-z0-9]", "", project_name.lower())
        if declared and folder and declared != folder and declared not in folder and folder not in declared:
            reasons.append(
                f"PROJECT header says '{m.group(1).strip()}' but this is the '{project_name}' folder -- "
                f"likely misfiled content from a different project"
            )

    if not EVIDENCE_TAG_RE.search(text):
        reasons.append(
            "zero Evidence Level tags found -- (HIGH)/(MEDIUM)/(LOW) per-fact citation is required by the "
            "format contract; this is the exact 'empty citations' failure mode rejected 2-3 times each in "
            "LayerZero Phase 3/4/6 before a working draft was accepted"
        )

    fallback_hits = len(FALLBACK_PLACEHOLDER_RE.findall(text))
    fact_count = max(len(EVIDENCE_TAG_RE.findall(text)), 1)
    if fallback_hits > 0 and fallback_hits >= fact_count:
        reasons.append(
            f"'[sumber tidak dapat diverifikasi ulang]' fallback used {fallback_hits} time(s), matching or "
            f"exceeding the {fact_count} real Evidence Level tag(s) found -- looks like blanket fallback "
            f"overuse rather than genuine per-fact citation (the Phase 3 attempt-2 failure mode)"
        )
    return reasons

def _content_hash(text: str) -> str:
    import hashlib
    norm = re.sub(r"\s+", " ", text.strip().lower())
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()

def process_data_project(folder: Path, force: bool, allow_partial: bool = False,
                          allow_unverified: bool = False, dest_dir: Path = None):
    """Assemble one project's dossier from data_project/<project>/ -- hardened successor to
    process_phased_project(). Exact filename contract (see detect_phase_key_strict) plus
    content-level verification (validate_phase_content); hard-fails (raises ValueError) on any
    unmatched file, duplicate phase key, duplicate file content, failed content verification, or --
    unless allow_partial -- an incomplete phase set, instead of the old function's silent
    soft-warning behaviour. A raised error means NOTHING is written for this project: no
    partial/misleading/unverified dossier."""
    name = folder.name
    dest_dir = dest_dir or DEST["deep"]
    existing = find_existing(dest_dir, name)
    out = existing or (dest_dir / f"{name}.md")
    if existing and not force:
        note = "" if existing.stem == name else f" (matched existing '{existing.stem}.md' — near-duplicate name)"
        return [("skip", name, f"dossier exists{note}")]

    files = sorted([*folder.glob("*.docx"), *folder.glob("*.pdf")])
    if not files:
        return [("warn", name, "no phase files found in folder")]

    # Pass 1: detect/extract/validate only -- NO archiving yet. A project that fails any check below
    # must leave doc_backup/deep/ untouched, same as it leaves the dossier unwritten: "verification
    # failed" must mean nothing happened, not "the dossier wasn't written but the raw file still got
    # copied into the permanent archive."
    phases, all_threads, seen, seen_hashes, verify_fails, raw_by_file = {}, [], {}, {}, [], {}
    for f in files:
        key = detect_phase_key_strict(f.name)
        if key in seen:
            raise ValueError(
                f"[{name}] duplicate phase '{key}': both '{seen[key]}' and '{f.name}' map to it. "
                f"Remove or rename one before ingesting."
            )
        seen[key] = f.name
        try:
            raw = extract_source(f)
        except Exception as e:
            # A raw extraction failure (corrupt file, unreadable encoding, etc.) must fail this
            # one project cleanly -- same "nothing written" contract as a validation failure --
            # not crash the whole ingest run for every other project queued behind it.
            raise ValueError(f"[{name}] failed to extract '{f.name}': {e}") from e
        raw_by_file[f.name] = (key, raw)

        h = _content_hash(raw)
        if h in seen_hashes:
            raise ValueError(
                f"[{name}] duplicate content: '{seen_hashes[h]}' and '{f.name}' have identical extracted "
                f"text (normalised) -- likely the same file saved under two phase names by mistake."
            )
        seen_hashes[h] = f.name

        fails = validate_phase_content(f.name, name, raw)
        if fails:
            verify_fails.append((f.name, fails))

    if verify_fails and not allow_unverified:
        lines = [f"[{name}] content verification failed for {len(verify_fails)} file(s):"]
        for fname, fails in verify_fails:
            lines.append(f"  {fname}:")
            lines.extend(f"    - {r}" for r in fails)
        lines.append("Pass --allow-unverified to assemble anyway (not recommended without human review).")
        raise ValueError("\n".join(lines))

    missing = [k for k in PHASE_KEYS if k not in {v[0] for v in raw_by_file.values()}]
    if missing and not allow_partial:
        raise ValueError(
            f"[{name}] incomplete: missing phase(s) {', '.join(missing)} "
            f"({len(raw_by_file)}/{len(PHASE_KEYS)} present). Pass --allow-partial to assemble anyway."
        )

    # Pass 2: only now, with every check passed, split Open Threads and archive raw sources.
    archived = []
    for fname, (key, raw) in raw_by_file.items():
        body, threads = split_open_threads(raw)
        phases[key] = body
        all_threads.extend(f"[{key}] {t}" for t in threads)
        archived.append(_archive(folder / fname, "deep", f"{name}_{key}"))

    order = [k for k in PHASE_KEYS if k in phases]
    body_md = []
    for k in order:
        meta = PHASE_META[k]
        body_md.append(f"\n## {meta['title']}\n_ref: {meta['ref']}_\n\n{phases[k]}")
    if all_threads:
        body_md.append("\n## Open Questions\n" + "\n".join(f"- {t}" for t in all_threads))

    summary_dup = find_existing(DEST["batch"], name)
    supersede_note = (f"\n**Supersedes:** `examples/Pioneer/{summary_dup.name}` — same project now exists as "
                       f"a fuller Deep dossier; the Summary is redundant and should be reviewed for removal "
                       f"(not auto-deleted)." if summary_dup else "")
    head = (
        f"# {name} — Deep Case Study (Phased)\n\n"
        f"**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**\n"
        f"**Source:** Deep Research (Gemini), Format v3 Dependency Pipeline "
        f"({len(order)}/{len(PHASE_KEYS)} phases: {', '.join(order)}). **Auto-assembled** by `tools/ingest.py` "
        f"(deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in "
        f"dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.\n"
        f"**Raw sources archived:** {', '.join(archived)}.\n"
        f"**Phases not run:** {', '.join(missing) if missing else 'none'}.{supersede_note}\n\n"
        f"> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the "
        f"Conflict Resolution phase itself states. Consider a periodic QC pass.\n\n---\n"
    )
    out.write_text(head + "\n".join(body_md).strip() + "\n", encoding="utf-8")
    return [("ok", name, f"{len(order)} phases -> {out.relative_to(ROOT)}")]

def gather_data_projects(inputs=None):
    """Yield project folders under data_project/ (or --input folders when --type data_project)."""
    bases = [Path(p) for p in inputs] if inputs else [DATA_PROJECT_ROOT]
    for base in bases:
        if not base.exists():
            continue
        if list(base.glob("*.docx")) + list(base.glob("*.pdf")):
            yield base
        else:
            for d in sorted(p for p in base.iterdir() if p.is_dir()):
                yield d

def gather_phased_projects(inputs=None):
    """Yield project folders under doc_backup/inbox/phased/ (or --input folders when --type phased)."""
    bases = [Path(p) for p in inputs] if inputs else [INBOX / "phased"]
    for base in bases:
        if not base.exists():
            continue
        # a folder containing phase docx/pdf directly IS a project; otherwise treat its children as projects
        if list(base.glob("*.docx")) + list(base.glob("*.pdf")):
            yield base
        else:
            for d in sorted(p for p in base.iterdir() if p.is_dir()):
                yield d

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
    ap.add_argument("--type", choices=["deep", "batch", "sentiment", "phased", "data_project"],
                     help="force type (for --input)")
    ap.add_argument("--input", nargs="*", help="folder(s)/file(s); default = the inbox subfolders + data_project/")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--allow-partial", action="store_true",
                     help="data_project only: assemble even if fewer than 11/11 phases are present")
    ap.add_argument("--allow-unverified", action="store_true",
                     help="data_project only: assemble even if content verification fails "
                          "(near-empty content, wrong PROJECT header, zero citations, fallback overuse)")
    ap.add_argument("--no-build", action="store_true")
    args = ap.parse_args()

    jobs, phased_projects, data_projects = [], [], []
    if args.input:
        if not args.type:
            sys.exit("--input requires --type deep|batch|sentiment|phased|data_project")
        if args.type == "phased":
            phased_projects = list(gather_phased_projects(args.input))
        elif args.type == "data_project":
            data_projects = list(gather_data_projects(args.input))
        else:
            jobs = list(gather(args.input, args.type))
    else:
        for kind in ("deep", "batch", "sentiment"):
            jobs += list(gather([INBOX / kind], kind))
        phased_projects = list(gather_phased_projects())
        data_projects = list(gather_data_projects())

    if not jobs and not phased_projects and not data_projects:
        print(f"No .docx/.pdf found. Drop files in {INBOX}/(deep|batch|sentiment|phased)/ or {DATA_PROJECT_ROOT}/, "
              f"or pass --input --type.")
        return

    print(f"ingest: {len(jobs)} file(s), {len(phased_projects)} phased project(s), "
          f"{len(data_projects)} data_project(s)\n" + "-" * 64)
    counts = {"ok": 0, "skip": 0, "warn": 0, "error": 0}
    icons = {"ok": "✅", "skip": "⏭️", "warn": "⚠️", "error": "❌"}
    for path, kind in jobs:
        for status, name, msg in PROCESSORS[kind](path, args.force):
            print(f"{icons[status]} [{kind:9s}] {name:18s} {msg}")
            counts[status] += 1
    for folder in phased_projects:
        for status, name, msg in process_phased_project(folder, args.force):
            print(f"{icons[status]} [{'phased':9s}] {name:18s} {msg}")
            counts[status] += 1
    for folder in data_projects:
        try:
            results = process_data_project(folder, args.force, args.allow_partial, args.allow_unverified)
        except ValueError as e:
            print(f"❌ [data_project] {folder.name:18s} {e}")
            counts["error"] += 1
            continue
        for status, name, msg in results:
            print(f"{icons[status]} [{'data_pr':9s}] {name:18s} {msg}")
            counts[status] += 1
    print("-" * 64)
    print(f"new: {counts['ok']}  skipped(dup): {counts['skip']}  warnings: {counts['warn']}  errors: {counts['error']}")
    if counts["error"]:
        print("\n⛔ one or more data_project folders failed hard validation — nothing was written for them. "
              "Fix the filenames/contents listed above and re-run.")

    if counts["error"]:
        sys.exit(1)

    if counts["ok"] and not args.no_build:
        print("\nrebuilding JSON + backtest...")
        subprocess.run([sys.executable, str(ROOT / "tools" / "build_json.py")], check=False)
        subprocess.run([sys.executable, str(ROOT / "tools" / "backtest.py")], check=False)

if __name__ == "__main__":
    main()
