#!/usr/bin/env python3
"""
extract_relationships.py — derive the relationships dataset from the entities
extraction, without inventing a single edge.

Background: the Supabase `relationships` table has been empty by design
(EnterpriseRoadmap Gate 2) because no research phase captured entity-to-entity
edges and deriving them from prose was (rightly) considered fabrication. This
tool takes the conservative middle path the CIF rules allow: it only emits edges
that are LITERALLY present in the already-extracted, already-evidenced entity
blocks of poc/entities.json.

Two edge kinds:

  project-entity   Every entity block states the entity's relationship to its
                   project (the block's `description` field) plus period,
                   exposure type and evidence. That IS a grounded edge; the
                   entities table holds the node, this file holds the edge.

  entity-mention   When an entity's description explicitly names ANOTHER
                   indexed entity (exact name match on word boundaries), that
                   is a co-occurrence the dossier itself asserted — e.g. the
                   Walrus block for Mysten Labs says "pencipta Sui". The edge
                   is tagged as a mention with the containing description as
                   evidence; it is NOT upgraded to a typed relation (founded /
                   invested / integrated) because the wording varies and typing
                   it would be the inference step this tool refuses to take.

Everything else stays out. No relation verbs guessed, no edges inferred from
co-occurrence across projects, no "probably the same entity" merges.

Usage:  python3 tools/extract_relationships.py
Output: poc/relationships.json
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTITIES = ROOT / "poc" / "entities.json"
OUT = ROOT / "poc" / "relationships.json"


def _norm(name: str) -> str:
    return re.sub(r"\s+", " ", name or "").strip().lower()


def main():
    data = json.loads(ENTITIES.read_text(encoding="utf-8"))

    # Global index of first-class entity names (appear as entity blocks
    # somewhere in the dataset). Mention edges may only point at these.
    name_index: dict[str, dict] = {}
    for project, ents in data.items():
        for e in ents:
            raw = (e.get("name") or "").strip()
            key = _norm(raw)
            if len(key) >= 3 and key not in name_index:
                name_index[key] = {"type": e.get("type") or "Unknown", "display": raw}

    # Pre-compile word-boundary matchers once per distinct name.
    matchers = {k: re.compile(rf"(?<![\w&]){re.escape(k)}(?![\w&])", re.I) for k in name_index}

    edges = []
    n_proj, n_mention = 0, 0
    for project, ents in data.items():
        slug = re.sub(r"[^a-z0-9]+", "-", project.lower()).strip("-")
        for e in ents:
            desc = (e.get("description") or "").strip()
            meta = e.get("metadata") or {}
            ename = (e.get("name") or "").strip()
            ename_key = _norm(ename)
            if not desc or len(ename_key) < 3:
                continue

            # 1) project-entity edge: the block's own statement of the
            #    entity's relationship to the project.
            edges.append({
                "id": f"rel-pe-{e.get('id', slug + '-' + ename_key)}",
                "kind": "project-entity",
                "sourceType": "project",
                "source": slug,
                "targetType": e.get("type") or "Unknown",
                "target": ename,
                "relation": desc,
                "period": meta.get("period") or None,
                "exposureType": meta.get("exposureType") or None,
                "evidenceLevel": meta.get("evidenceLevel") or None,
                "evidence": meta.get("evidence") or None,
                "viaEntityId": e.get("id"),
            })
            n_proj += 1

            # 2) entity-mention edges: other indexed entities named in the
            #    description, word-boundary matched, self excluded.
            for key, matcher in matchers.items():
                if key == ename_key or len(key) < 4:
                    continue
                if matcher.search(desc):
                    edges.append({
                        "id": f"rel-em-{e.get('id', slug + '-' + ename_key)}-{key.replace(' ', '-')}",
                        "kind": "entity-mention",
                        "sourceType": e.get("type") or "Unknown",
                        "source": ename,
                        "sourceProject": slug,
                        "targetType": name_index[key]["type"],
                        "target": name_index[key]["display"],
                        "relation": None,
                        "context": desc,
                        "evidenceLevel": meta.get("evidenceLevel") or None,
                        "evidence": meta.get("evidence") or None,
                        "viaEntityId": e.get("id"),
                    })
                    n_mention += 1

    out = {
        "meta": {
            "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            "source": "poc/entities.json (extract_entities.py output)",
            "edgeKinds": {
                "project-entity": "entity block's own statement of its relationship to the project",
                "entity-mention": "another indexed entity named in an entity description (co-occurrence, untyped by design)",
            },
            "edges": len(edges),
            "projectEntity": n_proj,
            "entityMention": n_mention,
        },
        "edges": edges,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ {len(edges)} edges ({n_proj} project-entity + {n_mention} entity-mention) -> {OUT}")


if __name__ == "__main__":
    main()
