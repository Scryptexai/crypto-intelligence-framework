#!/usr/bin/env python3
"""
extract_relationships.py — derive entity-graph edges (source/target/type) for the
Intelligence Workspace `relationships` table.

Root-cause context: the frontend Entity Graph reads the `relationships` table, but
extract_entities.py deliberately never emitted edges (its docstring: deriving edges
from prose would "guess a subject/predicate/object the text doesn't actually assert"
— CLAUDE.md's no-fabrication rule). Result: the table stayed empty and the graph had
zero connecting lines ("data tidak load").

Faithful approach (no fabrication): we emit an edge A -> B ONLY when entity A's own
Relationship/description prose (as already extracted into poc/entities.json) LITERALLY
names another known entity B of the SAME project. The edge is asserted by the text
itself (A's dossier paragraph mentions B by name); we never invent endpoints. The
predicate `type` is taken from an explicit keyword in that same sentence, falling back
to the neutral "related" when no keyword is stated (again, not guessing a specific
relation the text doesn't support).

Guards against noise / false edges:
  - target name must be >= 5 chars and match on word boundaries, case-insensitive
  - self-edges skipped; (source,target) de-duplicated (first/strongest keyword wins)
  - matches only within the same project's entity set (ids are project-prefixed)

Reads:  poc/entities.json   (produced by tools/extract_entities.py — run it first)
Output: poc/relationships.json  (keyed by project name, same convention as entities)

Usage:  python3 tools/extract_relationships.py            # all projects in entities.json
        python3 tools/extract_relationships.py Arbitrum   # optional subset by project name
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTITIES = ROOT / "poc" / "entities.json"
OUT = ROOT / "poc" / "relationships.json"

# Ordered: first keyword found in the sentence wins (most specific -> least).
TYPE_KEYWORDS = [
    (r"co-?founder|cofounder|didirikan oleh|mendirikan", "co-founder"),
    (r"founded|pendiri|founder", "founded"),
    (r"invest|investor|backed|pendanaan|memimpin putaran|led the round", "invested"),
    (r"acquir|akuisisi|mengakuisisi", "acquired"),
    (r"partner|kemitraan|kolaborasi|integrasi|integrat", "partner"),
    (r"audit|mengaudit", "audits"),
    (r"advisor|penasihat|advises", "advisor"),
    (r"member|director|dewan|anggota|seat|board", "member"),
    (r"develop|membangun|mengembangkan|core (dev|team)|builds|pengembang", "develops"),
    (r"operates|mengoperasikan|operator", "operates"),
    (r"grant|hibah|funds|mendanai", "funds"),
    (r"subsidiary|anak perusahaan|owned by|dimiliki", "subsidiary"),
]


def _norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def _rel_type(text):
    low = (text or "").lower()
    for pat, label in TYPE_KEYWORDS:
        if re.search(pat, low):
            return label
    return "related"


def _canonical(name):
    """Loose canonical form of an entity name for robust literal matching:
    drop legal suffixes/parentheticals so 'Offchain Labs' matches 'Offchain Labs, Inc.'."""
    n = re.sub(r"\(.*?\)", "", name)
    n = re.sub(r"\b(Inc|Ltd|LLC|Labs|Foundation|Corp|Co|PBC|Ltda|BV|AG|GmbH)\b\.?", "", n, flags=re.I)
    return _norm(n)


def build_edges(entities):
    """entities: list of {id,name,description,...} for ONE project."""
    # Candidate targets: (compiled word-boundary regex, entity) for names long enough
    targets = []
    for e in entities:
        for variant in {e["name"], _canonical(e["name"])}:
            v = variant.strip()
            if len(v) >= 5:
                targets.append((re.compile(rf"\b{re.escape(v)}\b", re.I), e))

    edges = []
    seen = set()
    for src in entities:
        prose = src.get("description") or ""
        if not prose:
            continue
        for pat, tgt in targets:
            if tgt["id"] == src["id"]:
                continue
            if pat.search(prose):
                key = (src["id"], tgt["id"])
                if key in seen:
                    continue
                seen.add(key)
                edges.append({
                    "source": src["id"],
                    "target": tgt["id"],
                    "type": _rel_type(prose),
                })
    return edges


def main():
    if not ENTITIES.exists():
        sys.exit(f"{ENTITIES} not found — run tools/extract_entities.py first.")
    data = json.loads(ENTITIES.read_text(encoding="utf-8"))
    only = set(sys.argv[1:])
    existing = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}

    for project_name, entities in data.items():
        if only and project_name not in only:
            continue
        # Only entities with a non-null `type` are synced to the `entities` table
        # (sync_supabase.py entity_rows() skips null-type). Edges must reference
        # existing entity ids or the relationships FK insert fails, so filter to
        # the same set here.
        entities = [e for e in entities if e.get("type")]
        edges = build_edges(entities)
        slug = re.sub(r"[^a-z0-9]+", "-", project_name.lower()).strip("-")
        rows = [
            {"id": f"{slug}-REL-{i + 1:03d}", "projectSlug": slug, **e}
            for i, e in enumerate(edges)
        ]
        existing[project_name] = rows
        print(f"[extract_relationships] {project_name}: {len(rows)} edge(s)")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
