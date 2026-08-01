#!/usr/bin/env python3
"""
extract_knowledge.py — pull structured Knowledge Items out of a Track C (DeepSeek
methodology) dossier's Knowledge Extraction phase, for Intelligence Workspace's
`KnowledgeItem` contract (`scryptexai/cif`'s `src/lib/types/knowledge.ts`).

Track C only, deliberately -- same reasoning as extract_behavior.py/extract_qa.py. Track
A/B's Knowledge Extraction phase (LayerZero) produces a POV success-matrix (per-stakeholder
verdict) plus free-form Lessons Learned, not discrete named items -- forcing that into
KnowledgeItem's shape would mean guessing a name/category/confidence the source never
states, which the maintainer explicitly rejected (2026-08-01: "lebih baik bangun dari nol
data field-nya karena kalau diderivasi rentan error salah baca"). Track C's Phase 10 prompt
instead produces genuinely itemized, labeled entries across seven sections (verified against
examples/CaseStudies/Arbitrum.md):

    Core Insights        (Insight N: <title> / Explanation / Evidence / Supporting Dataset / Confidence)
    Strategic Principles  (Principle N: <title> / Description / Evidence)
    Success Factors        (Factor N: <title> / Evidence / Supporting Dataset)
    Failure Factors         (Factor N: <title> / Description / Lesson / Supporting Dataset)
    Decision Framework    (Step N: <title> / Description / Evidence)
    Reusable Playbook       (Playbook N: <title> / Description / Evidence / Applicability)
    Anti-patterns            (Anti-pattern N: <title> / Description / Evidence / Warning)

A trailing "Lessons Learned" / "Knowledge Summary" section is a recap restating the same
items in one-line form -- it is used only as an end-of-phase boundary marker, never parsed
for new items, to avoid double-counting.

Fields never fabricated:
  - `confidence` (0-100) is populated ONLY where the item literally carries a
    "Confidence: High|Medium|Low" tag (Core Insights only) -- mapped via a fixed,
    documented scale (HIGH=90, MEDIUM=60, LOW=30), never guessed for sections without the
    tag.
  - `status` (Stable/Emerging/Volatile/Deprecated) and `updatedAt` have no source at all
    and stay null -- Track C never tags a knowledge item's lifecycle state or edit date.
  - `evidence` (KnowledgeItem's structured Evidence[] -- id/eventId/eventName/date/source/
    url/weight 1-5/note) stays an EMPTY array rather than force-fitting the item's raw
    Evidence/Lesson/Warning text into that shape: the dossier's Evidence field is often a
    multi-citation paragraph, not one gradable claim, and assigning a numeric weight to it
    would be exactly the kind of invented precision the maintainer ruled out. The raw text
    is preserved in full inside `description` instead, so no information is lost.
  - `relatedKnowledge` stays empty -- resolving it would mean name-matching prose across
    items, which is inference, not extraction.
  - `dependencies` (event ids) is populated with literal `EV-\\d+` references pulled out of
    the item's "Supporting Dataset" field -- a plain regex grep of IDs the text already
    states, not a guess.
  - `author` has no per-item source either; set to the fixed system label "CIF" (this
    pipeline's own provenance marker, not a claimed human author).

Usage:  python3 tools/extract_knowledge.py examples/CaseStudies/Arbitrum.md
Output: poc/knowledge.json  (merges/replaces entries for the parsed project)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "knowledge.json"

CONFIDENCE_SCALE = {"high": 90, "medium": 60, "low": 30}

# (section header, item-word regex, category label). Order matters -- sections are sliced
# between consecutive headers found from this list; "Lessons Learned" is a boundary only.
SECTIONS = [
    ("Core Insights", "Insight", "Core Insight"),
    ("Strategic Principles", "Principle", "Strategic Principle"),
    ("Success Factors", "Factor", "Success Factor"),
    ("Failure Factors", "Factor", "Failure Factor"),
    ("Decision Framework", "Step", "Decision Framework"),
    ("Reusable Playbook", "Playbook", "Reusable Playbook"),
    ("Anti-patterns", "Anti-pattern", "Anti-pattern"),
    ("Lessons Learned", None, None),  # boundary marker only, never parsed
]
FIELD_LABELS = ["Description", "Explanation", "Evidence", "Supporting Dataset", "Confidence",
                 "Lesson", "Warning", "Applicability"]
_header_alt = "|".join(re.escape(h) for h, _, _ in SECTIONS)
_field_alt = "|".join(re.escape(l) for l in FIELD_LABELS)


def _project_name(text):
    m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", text, re.M)
    return m.group(1).strip() if m else None


def _slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _sections(body):
    matches = list(re.finditer(rf"(?:^|\n)({_header_alt})\s*\n", body))
    out = {}
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        out[m.group(1)] = body[start:end]
    return out


def _extract_field(block, label):
    m = re.search(
        rf"(?:^|\n)\s*·?\s*{re.escape(label)}:\s*(.*?)(?=\n\s*·?\s*(?:{_field_alt}):|\Z)",
        block, re.S,
    )
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def parse_knowledge(text, project_name):
    m = re.search(r"^## Knowledge Extraction\n(.*?)(?=\n## )", text, re.S | re.M)
    body = m.group(1) if m else ""
    sections = _sections(body)

    items = []
    idx = 0
    for header, item_word, category in SECTIONS:
        if item_word is None or header not in sections:
            continue
        section_body = sections[header]
        chunks = re.split(rf"(?:^|\n){re.escape(item_word)}\s+\d+:\s*", section_body)[1:]
        for chunk in chunks:
            head, _, rest = chunk.partition("\n")
            name = head.strip()
            if not name:
                continue
            idx += 1
            fields = {label: _extract_field(rest, label) for label in FIELD_LABELS}
            description = fields["Description"] or fields["Explanation"] or ""
            extra = fields["Lesson"] or fields["Warning"] or fields["Applicability"]
            if extra:
                description = f"{description} — {extra}" if description else extra
            confidence = None
            if fields["Confidence"]:
                confidence = CONFIDENCE_SCALE.get(fields["Confidence"].strip().lower())
            dep_source = f"{fields['Supporting Dataset'] or ''} {fields['Evidence'] or ''}"
            dependencies = sorted(set(re.findall(r"EV-\d+", dep_source)))
            if fields["Evidence"]:
                description = f"{description}\n\nEvidence: {fields['Evidence']}"
            items.append({
                "id": f"K-{idx:03d}",
                "projectSlug": _slugify(project_name),
                "name": name,
                "category": category,
                "description": description.strip(),
                "confidence": confidence,
                "status": None,
                "updatedAt": None,
                "author": "CIF",
                "evidence": [],
                "relatedKnowledge": [],
                "dependencies": dependencies,
            })
    return items


def extract_from_dossier(path):
    text = path.read_text(encoding="utf-8")
    project_name = _project_name(text) or path.stem
    return project_name, parse_knowledge(text, project_name)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/extract_knowledge.py <dossier.md> [more.md ...]")
    OUT.parent.mkdir(exist_ok=True)
    existing = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[extract_knowledge] skip (not found): {arg}", file=sys.stderr)
            continue
        project_name, items = extract_from_dossier(path)
        if not items:
            print(f"[extract_knowledge] {project_name}: 0 items (not a Track C dossier? skipped)",
                  file=sys.stderr)
            continue
        existing[project_name] = items
        print(f"[extract_knowledge] {project_name}: {len(items)} knowledge item(s)")
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
