#!/usr/bin/env python3
"""
extract_entities.py — pull structured Entities out of a Format v3 dossier's Entity
Intelligence phase (docs/Ontology/Relationships.md).

That phase's real shape (verified against examples/CaseStudies/LayerZero.md) is one
paragraph per entity:

    Entity: <Name> (<HIGH|MEDIUM|LOW>) Type: <Type> Relationship: <prose> Period: <period>
    Exposure Type: <exposure> Evidence: <sources>

This is a project-centric relationship description ("how does this entity relate to
the project"), not entity-to-entity graph edges — so this tool only emits Entity rows,
never Relationship rows (source/target/type triples). Deriving graph edges from the
prose would mean guessing a subject/predicate/object that the text doesn't actually
assert, which CLAUDE.md's "don't fabricate" rule forbids; Relationship extraction stays
a known gap until a phase captures entity-to-entity edges explicitly.

Two fields never fabricated, left null intentionally:
  - `status` (Active/Dormant/Contested/Unknown in Intelligence Workspace's contract) —
    the dossier's Entity Intelligence phase never tags a lifecycle status, only a
    point-in-time "Period". Guessing "Active" for everyone would be fabricated precision.
  - `founded` — not part of this phase's fields at all.

`type` is normalised from the dossier's free-text vocabulary (Organization, Person,
Foundation, Investor, Protocol, Partner, Research Lab, ...) to Intelligence Workspace's
fixed EntityType enum via TYPE_MAP; anything with no confident mapping is left null
rather than force-fit into the nearest wrong bucket.

Two Entity Intelligence shapes are recognized (Track A/B vs. Track C — see
tools/extract_decision_events.py's module docstring for the same track split
applied to Decision Events):

  Track A/B — one packed paragraph per entity, confidence right after the name:
    Entity: <Name> (<HIGH|MEDIUM|LOW>) Type: <Type> Relationship: <prose>
    Period: <period> Exposure Type: <exposure> Evidence: <sources>

  Track C (DeepSeek methodology) — one field per line, blocks separated by a
  "---" rule, no confidence tag after the name (tags appear inline in
  Relationship/Evidence instead):
    Entity: <Name>
    Type: <Type>
    Relationship: <prose, often with inline (HIGH)/(MEDIUM)/(LOW) tags>
    Period: <period>
    Exposure Type: <exposure>
    Evidence: (<HIGH|MEDIUM|LOW>) [source, url]; [source, url]

Usage:  python3 tools/extract_entities.py examples/CaseStudies/LayerZero.md
Output: poc/entities.json  (merges/replaces entries for the parsed project)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "entities.json"

TYPE_MAP = {
    "organization": "Company",
    "company": "Company",
    "exchange": "Company",
    "person": "Person",
    "foundation": "Foundation",
    "investor": "Investor",
    "protocol": "Protocol",
    "partner": "Company",
    "research lab": "Security",
    "dao": "DAO",
    "government": "Government",
    "application": "Application",
}


def _normalise_type(raw):
    """Track C's Type vocabulary adds parenthetical qualifiers and '/'-joined compound
    types not in Track A/B ('Protocol (DeFi)', 'Person (Investor)', 'Media / Research Lab').
    Strip the qualifier, then try each '/'-alternative in order against TYPE_MAP; the
    first confident match wins, otherwise stays null (never guessed)."""
    if not raw:
        return None
    for alt in raw.split("/"):
        base = re.sub(r"\(.*?\)", "", alt).strip().lower()
        if base in TYPE_MAP:
            return TYPE_MAP[base]
    return None

ENTITY_RE = re.compile(
    r"^(?P<name>.+?)\s*\((?P<conf>HIGH|MEDIUM|LOW)\)\s*"
    r"Type:\s*(?P<type>.+?)\s*"
    r"Relationship:\s*(?P<relationship>.+?)\s*"
    r"Period:\s*(?P<period>.+?)\s*"
    r"Exposure Type:\s*(?P<exposure>.+?)\s*"
    r"Evidence:\s*(?P<evidence>.+)$",
    re.S,
)

ENTITY_BLOCK_LABELS = ["Type", "Relationship", "Period", "Exposure Type", "Evidence"]
_CONF_TAG_RE = re.compile(r"\((HIGH|MEDIUM|LOW)\)")


def _extract_block_field(block, label, all_labels):
    alt = "|".join(re.escape(l) for l in all_labels)
    m = re.search(
        rf"(?:^|\n)\s*{re.escape(label)}:\s*(.*?)(?=\n\s*(?:{alt}):|\Z)", block, re.S
    )
    return m.group(1).strip() if m else None


def _project_name(text):
    m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", text, re.M)
    return m.group(1).strip() if m else None


def _slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _make_entity(idx, project_name, name, entity_type, confidence, relationship, period,
                  exposure, evidence):
    # `metadata` is Intelligence Workspace's Record<string,string> catch-all (entity.ts) --
    # period/exposureType/evidence/evidenceLevel don't have dedicated columns in the Entity
    # contract, so they live there instead of being dropped.
    metadata = {}
    if confidence:
        metadata["evidenceLevel"] = confidence
    if period:
        metadata["period"] = period.strip()
    if exposure:
        metadata["exposureType"] = exposure.strip()
    if evidence:
        metadata["evidence"] = re.sub(r"\s+", " ", evidence).strip()
    return {
        "id": f"ENT-{idx:03d}",
        "projectSlug": _slugify(project_name),
        "name": re.sub(r"\s+", " ", name).strip(),
        "type": _normalise_type(entity_type),
        "status": None,
        "description": re.sub(r"\s+", " ", relationship).strip(),
        "founded": None,
        "relatedKnowledge": [],
        "relatedEvents": [],
        "metadata": metadata,
    }


def parse_entities(text, project_name):
    """Track A/B: one packed paragraph per entity."""
    chunks = re.split(r"(?:^|\n)Entity:\s*", text)[1:]
    entities = []
    for i, chunk in enumerate(chunks):
        m = ENTITY_RE.match(chunk.strip())
        if not m:
            continue
        entities.append(_make_entity(
            i + 1, project_name, m.group("name"), m.group("type"), m.group("conf"),
            m.group("relationship"), m.group("period"), m.group("exposure"), m.group("evidence"),
        ))
    return entities


def parse_entities_block(text, project_name):
    """Track C: one field per line, blocks separated by a '---' rule."""
    chunks = re.split(r"(?:^|\n)Entity:\s*", text)[1:]
    entities = []
    for i, chunk in enumerate(chunks):
        head, _, rest = chunk.partition("\n")
        name = head.strip()
        if not name:
            continue
        rest, _, _ = rest.partition("\n---")
        entity_type = _extract_block_field(rest, "Type", ENTITY_BLOCK_LABELS)
        relationship = _extract_block_field(rest, "Relationship", ENTITY_BLOCK_LABELS)
        period = _extract_block_field(rest, "Period", ENTITY_BLOCK_LABELS)
        exposure = _extract_block_field(rest, "Exposure Type", ENTITY_BLOCK_LABELS)
        evidence = _extract_block_field(rest, "Evidence", ENTITY_BLOCK_LABELS)
        if entity_type is None and relationship is None:
            continue
        conf_source = f"{evidence or ''} {relationship or ''}"
        conf_m = _CONF_TAG_RE.search(conf_source)
        entities.append(_make_entity(
            i + 1, project_name, name, entity_type, conf_m.group(1) if conf_m else None,
            relationship or "", period, exposure, evidence,
        ))
    return entities


def extract_from_dossier(path):
    text = path.read_text(encoding="utf-8")
    project_name = _project_name(text) or path.stem

    m = re.search(r"^## Entity Intelligence\n(.*?)(?=\n## )", text, re.S | re.M)
    body = m.group(1) if m else ""
    body = re.sub(r"^_ref:.*\n", "", body)
    body = re.sub(r"^PROJECT:.*\n", "", body, flags=re.M)

    entities = parse_entities(body, project_name) or parse_entities_block(body, project_name)
    return project_name, entities


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/extract_entities.py <dossier.md> [more.md ...]")
    OUT.parent.mkdir(exist_ok=True)
    existing = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[extract_entities] skip (not found): {arg}", file=sys.stderr)
            continue
        project_name, entities = extract_from_dossier(path)
        existing[project_name] = entities
        print(f"[extract_entities] {project_name}: {len(entities)} entit(y/ies)")
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
