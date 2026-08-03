#!/usr/bin/env python3
"""
extract_conflicts.py — pull structured Conflicts out of a Format v3 dossier's
"Validation & Quality Assurance (CIF Score)" phase, specifically its
"CONFLICT REGISTER WITH SEVERITY & IMPACT" block.

Root-cause context: the Intelligence Workspace frontend renders a Conflict Center
from the `conflicts` table, but no extractor ever produced poc/conflicts.json, so
sync_supabase.py had nothing to push and the table stayed empty ("data tidak load").
The dossier DOES state conflicts explicitly in a clean, parseable register — this
tool extracts them faithfully (no fabrication; only literally-stated fields).

Mapping to Intelligence Workspace's `conflicts` columns (src/lib/types/conflict.ts):
  - id                 -> "{slug}-C-NNN" (bare PK globally unique, like entities/knowledge)
  - title              -> text after the em dash on the "Conflict C-NNN —" line
  - category/description/severity/status/resolution/affected_phase -> literal fields
  - affected_knowledge -> ["{slug}-K-NNN", ...] (referential; [] when "Tidak ada")
  - version_a/version_b -> {source, value, date, url, evidence} built ONLY from the
                          entry's own Evidence + Sources lines (value = description).

Dossiers without the register parse to 0 conflicts (safe).

Usage:  python3 tools/extract_conflicts.py examples/CaseStudies/Arbitrum.md [more.md ...]
Output: poc/conflicts.json  (merges/replaces entries for the parsed project)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "conflicts.json"

FIELD_LABELS = [
    "Category", "Description", "Severity", "Affected Knowledge", "Impact",
    "Affected Phase", "Evidence", "Sources", "Resolution", "Status",
]
_FIELD_ALT = "|".join(re.escape(l) for l in FIELD_LABELS)
SEVERITY_MAP = {"critical": "Critical", "high": "High", "medium": "Medium", "low": "Low"}


def _slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _project_name(text):
    m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", text, re.M)
    return m.group(1).strip() if m else None


def _research_date(text):
    m = re.search(r"Research Date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text)
    return m.group(1) if m else ""


def _field(block, label):
    m = re.search(
        rf"(?:^|\n)\s*·?\s*{re.escape(label)}:\s*(.*?)(?=\n\s*·?\s*(?:{_FIELD_ALT}):|\Z)",
        block, re.S,
    )
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def _severity(raw):
    return SEVERITY_MAP.get((raw or "").strip().lower(), "Medium")


def _status(raw, resolution):
    if raw:
        low = raw.strip().lower()
        if low.startswith("resolved"):
            return "Resolved"
        if low.startswith("unresolved"):
            return "Unresolved"
    if resolution and re.search(r"\bresolved\b", resolution, re.I) and not re.search(
        r"tidak resolved|not resolved|belum", resolution, re.I
    ):
        return "Resolved"
    return "Unresolved"


def _affected_knowledge(raw, slug):
    if not raw:
        return []
    return [f"{slug}-K-{int(n):03d}" for n in re.findall(r"K-?\s*0*([0-9]+)", raw)]


def _split_sources(raw):
    if not raw:
        return []
    return [u.strip().rstrip(").,;") for u in re.findall(r"https?://[^\s,;)]+", raw)]


def _source_names(evidence):
    if not evidence:
        return []
    cleaned = re.sub(r"\(https?://[^)]*\)", "", evidence)
    cleaned = re.sub(r"https?://[^\s,;)]+", "", cleaned)
    return [p.strip() for p in re.split(r"[,;]", cleaned) if p.strip()]


def _versions(evidence, sources_raw, description, date):
    urls = _split_sources(sources_raw)
    names = _source_names(evidence)

    def mk(i):
        return {
            "source": names[i] if i < len(names) else f"Source {chr(65 + i)}",
            "value": description or "",
            "date": date or "",
            "url": urls[i] if i < len(urls) else "",
            "evidence": evidence or "",
        }

    return mk(0), mk(1)


def parse_conflicts(text, project_name):
    slug = _slugify(project_name)
    date = _research_date(text)
    reg = re.search(r"CONFLICT REGISTER.*?(?=\n[A-Z][A-Z &]{6,}\n|\n## |\Z)", text, re.S)
    body = reg.group(0) if reg else text

    chunks = re.split(r"(?:^|\n)Conflict\s+(C-?\s*\d+)\s*[—-]\s*", body)
    conflicts = []
    for i in range(1, len(chunks) - 1, 2):
        raw_id, block = chunks[i], chunks[i + 1]
        title = block.split("\n", 1)[0].strip()
        num = re.search(r"(\d+)", raw_id)
        cid = f"{slug}-C-{int(num.group(1)):03d}" if num else f"{slug}-C-{(i // 2) + 1:03d}"
        description = _field(block, "Description") or ""
        resolution = _field(block, "Resolution")
        evidence = _field(block, "Evidence")
        vA, vB = _versions(evidence, _field(block, "Sources"), description, date)
        conflicts.append({
            "id": cid,
            "projectSlug": slug,
            "category": _field(block, "Category") or "Data",
            "title": re.sub(r"\s+", " ", title).strip() or cid,
            "description": description,
            "severity": _severity(_field(block, "Severity")),
            "status": _status(_field(block, "Status"), resolution),
            "versionA": vA,
            "versionB": vB,
            "resolution": resolution or None,
            "affectedKnowledge": _affected_knowledge(_field(block, "Affected Knowledge"), slug),
            "affectedPhase": _field(block, "Affected Phase") or "",
            "updatedAt": date,
        })
    return conflicts


def extract_from_dossier(path):
    text = path.read_text(encoding="utf-8")
    project_name = _project_name(text) or path.stem
    return project_name, parse_conflicts(text, project_name)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/extract_conflicts.py <dossier.md> [more.md ...]")
    OUT.parent.mkdir(exist_ok=True)
    existing = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[extract_conflicts] skip (not found): {arg}", file=sys.stderr)
            continue
        project_name, conflicts = extract_from_dossier(path)
        existing[project_name] = conflicts
        print(f"[extract_conflicts] {project_name}: {len(conflicts)} conflict(s)")
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
