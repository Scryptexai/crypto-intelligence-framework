#!/usr/bin/env python3
"""
sync_supabase.py — push poc/*.json to Intelligence Workspace's real Postgres schema.

Target schema note (2026-08-01): earlier this session this script targeted a cif_-prefixed
schema designed independently in this repo. That schema was superseded once the frontend's
actual repo (github.com/scryptexai/intelligence-workspace — NOT the earlier scryptexai/cif
upload, which turned out to be stale/uncommitted work) was inspected directly: it ships a
complete Drizzle schema (src/db/schema.ts) and a resilient DB-backed data layer
(src/db/dataService.ts) already querying plain-named tables (`projects`, `knowledge_items`,
`evidence_items`, `entities`, `relationships`, `events`, `conflicts`, `qa_dimensions`,
`qa_phases`, `behavior_profiles`, `notes`, `saved_views`, `users`). That schema is the
source of truth now — this script writes to it directly (see supabase/schema.sql in that
repo, applied to the shared Supabase project via the "align_to_intelligence_workspace_
drizzle_schema" migration). cif_patterns/cif_backtests/cif_decision_events remain untouched
-- CIF's own pattern-library concern, no naming collision, not part of that schema.

Deterministic upsert, no LLM, stdlib only (no `requests`/`supabase-py` dependency — matches
the rest of tools/'s minimal-dependency convention, see requirements.txt). Talks to
Supabase's PostgREST API directly.

Requires two environment variables (never commit these — same treatment as the research
prompts, see docs/Protocol/Deep-Research-Brief.md's policy note):
    SUPABASE_URL               e.g. https://szumyjuvfjkobvcqswwd.supabase.co
    SUPABASE_SERVICE_ROLE_KEY  the service_role key — bypasses RLS, required because these
                                 tables' policies only grant SELECT to clients: writes are
                                 meant to happen ONLY through this script.

Usage:
    export SUPABASE_URL="https://<ref>.supabase.co"
    export SUPABASE_SERVICE_ROLE_KEY="..."
    python3 tools/sync_supabase.py             # upsert every table below
    python3 tools/sync_supabase.py --dry-run   # print the rows that would be sent, no network call
    python3 tools/sync_supabase.py --only projects,cif_patterns
"""
import argparse, json, os, re, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POC = ROOT / "poc"
TABLES = ("projects", "knowledge_items", "evidence_items", "entities", "relationships",
          "conflicts", "qa_dimensions",
          "qa_phases", "behavior_profiles", "cif_patterns", "cif_backtests",
          "cif_decision_events")


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load(name: str):
    p = POC / name
    if not p.exists():
        sys.exit(f"{p} not found — run ./run.sh (or tools/build_json.py) first.")
    return json.loads(p.read_text(encoding="utf-8"))


def load_optional(name: str) -> dict:
    p = POC / name
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


_SYMBOL_RE = re.compile(r"(?:^|\n)Symbol:\s*([A-Za-z0-9]+)")


def _extract_symbol(dossier_file: str) -> str | None:
    """Foundation Intelligence's 'Symbol: ARB' / 'Symbol: ZRO (HIGH)' line -- a real,
    literally-stated field, not guessed. Required NOT NULL by the `projects` table; falls
    back to the project's own name (still real, just less precise) rather than fabricating
    a ticker the dossier doesn't state."""
    path = ROOT / dossier_file
    if not path.exists():
        return None
    m = _SYMBOL_RE.search(path.read_text(encoding="utf-8"))
    return m.group(1).strip() if m else None


def project_rows():
    """poc/projects.json (build_json.py's roster shape) -> `projects` columns.

    Only fields this script can derive without guessing are populated: entity_count/
    knowledge_count from poc/{entities,knowledge}.json (real counts), cif_score from
    qa.json's `total` (Track C dossiers only), symbol from the dossier's own literal
    'Symbol: X' line (Foundation Intelligence phase). status defaults to "active" as CIF's
    own curation-state label (every project in examples/CaseStudies/ is, by definition,
    actively tracked -- a workflow flag CIF assigns, not a claim about the project itself).
    tagline/description/color/accent/conflict_count/event_count/coverage have no
    deterministic source yet and are intentionally omitted so upsert leaves them untouched."""
    # Counts entities the same way entity_rows() filters them (skips null `type`, see that
    # function's docstring) -- otherwise this stays out of sync with what's actually inserted,
    # exactly the bug caught by a 2026-08-02 Supabase audit (stored count 1 too high on both
    # projects, matching the entities excluded for missing type).
    entity_counts = {
        slugify(k): sum(1 for e in v if e.get("type")) for k, v in load_optional("entities.json").items()
    }
    knowledge_counts = {slugify(k): len(v) for k, v in load_optional("knowledge.json").items()}
    qa_by_slug = {slugify(k): v for k, v in load_optional("qa.json").items()}

    rows = []
    for p in load("projects.json"):
        slug = slugify(p["n"])
        row = {
            "id": slug,
            "slug": slug,
            "name": p["n"],
            "symbol": _extract_symbol(p["file"]) or p["n"],
            "status": "active",
            "tags": p.get("tags", []),
            "entity_count": entity_counts.get(slug, 0),
            "knowledge_count": knowledge_counts.get(slug, 0),
        }
        if slug in qa_by_slug and qa_by_slug[slug].get("total") is not None:
            row["cif_score"] = qa_by_slug[slug]["total"]
        rows.append(row)
    return rows


def pattern_rows():
    rows = []
    for p in load("patterns.json"):
        rows.append({
            "id": p["id"],
            "name": p["nm"],
            "confidence": p["confidence"],
            "instances": p["instances"],
            "scope": p.get("scope") or None,
            "analogs": p.get("analogs", []),
            "triggers": p.get("triggers", []),
            "source": p.get("src") or None,
            "prediction": p.get("pred") or None,
            "validation": p.get("val") or None,
            "watch": p.get("watch", []),
        })
    return rows


def backtest_rows():
    rows = []
    for b in load("benchmarks.json"):
        m = re.search(r"Backtest\s+(\d+)", b["title"])
        bid = f"backtest-{int(m.group(1)):02d}" if m else slugify(b["title"])
        rows.append({
            "id": bid,
            "title": b["title"],
            "type": b["type"],
            "category": b.get("category") or None,
            "given": b.get("given", []),
            "expect": b.get("expect", []),
            "fired": b.get("fired", []),
            "missed": b.get("missed", []),
            "outcome": b.get("outcome") or None,
            "source": b.get("source") or None,
            "verdict": b["verdict"],
            "recall": b.get("recall"),
            "file": b.get("file") or None,
        })
    return rows


def decision_event_rows():
    rows = []
    data = load("decision_events.json")
    for project, events in data.items():
        for i, e in enumerate(events):
            rows.append({
                "id": f"{slugify(project)}__{i:02d}",
                "project": project,
                "event_date": e.get("date") or None,
                "title": e.get("title") or None,
                "motivation": e.get("motivation"),
                "constraint_text": e.get("constraint"),
                "pressure": e.get("pressure"),
                "tradeoff": e.get("tradeoff"),
                "alternatives": e.get("alternatives"),
                "expectation_vs_actual": e.get("expectation_vs_actual"),
                "reactions": e.get("reactions") or {},
                "grounding": e.get("grounding"),
                "open_threads": e.get("open_threads"),
                # Track C fields (docs/Protocol/Phased-Research-Prompts.md, DeepSeek methodology) --
                # null for Track A/B events, which never had these; see extract_decision_events.py.
                "trigger": e.get("trigger"),
                "decision_evidence": e.get("evidence"),
                "decision_text": e.get("decision"),
                "immediate_result": e.get("immediate_result"),
                "long_term_impact": e.get("long_term_impact"),
                "supporting_dataset": e.get("supporting_dataset"),
            })
    return rows


def entity_rows():
    """poc/entities.json (tools/extract_entities.py's shape) -> `entities` columns.

    `entities.type` is NOT NULL in the real schema. extract_entities.py leaves `type` null
    for the small number of items where the dossier's free-text vocabulary had no confident
    mapping (see that tool's TYPE_MAP/_normalise_type) rather than guessing -- those rows are
    skipped here instead of force-filling a fabricated type, since a required column is not
    a license to invent a value the source doesn't support."""
    rows = []
    for _project, entities in load("entities.json").items():
        for e in entities:
            if not e.get("type"):
                continue
            rows.append({
                "id": e["id"],
                "project_slug": e["projectSlug"],
                "name": e.get("name"),
                "type": e.get("type"),
                "status": e.get("status"),
                "description": e.get("description"),
                "founded": e.get("founded"),
                "related_knowledge": e.get("relatedKnowledge", []),
                "related_events": e.get("relatedEvents", []),
                "metadata": e.get("metadata") or {},
            })
    return rows


def knowledge_rows():
    """poc/knowledge.json (tools/extract_knowledge.py's shape) -> `knowledge_items` columns
    (Track C dossiers only -- see that tool's docstring). Per-citation Evidence[] now has a
    real home (the separate `evidence_items` table, see evidence_rows()) instead of being
    folded into description text."""
    rows = []
    for _project, items in load("knowledge.json").items():
        for k in items:
            rows.append({
                "id": k["id"],
                "project_slug": k["projectSlug"],
                "name": k.get("name"),
                "category": k.get("category"),
                "description": k.get("description"),
                "confidence": k.get("confidence") or 0,
                "status": k.get("status") or "Stable",
                "updated_at": k.get("updatedAt"),
                "author": k.get("author"),
                "related_knowledge": k.get("relatedKnowledge", []),
                "dependencies": k.get("dependencies", []),
            })
    return rows


def evidence_rows():
    """poc/knowledge.json's raw Evidence text -> one `evidence_items` row per knowledge item
    that has one. `weight` uses the column's own documented default (1, "lowest/default"),
    not a fabricated per-citation grade -- extract_knowledge.py deliberately never invents a
    1-5 rating for a multi-citation paragraph (see that tool's docstring)."""
    rows = []
    for _project, items in load("knowledge.json").items():
        for k in items:
            note = k.get("evidenceText")
            if not note:
                continue
            rows.append({
                "id": f"{k['id']}-ev1",
                "knowledge_id": k["id"],
                "event_id": None,
                "event_name": "CIF Research Dossier",
                "date": None,
                "source": "CIF Research Dossier",
                "url": None,
                "weight": 1,
                "note": note,
                "sort_order": 0,
            })
    return rows


def qa_dimension_rows():
    """poc/qa.json -> `qa_dimensions` columns (one row per dimension per project)."""
    rows = []
    for project, report in load_optional("qa.json").items():
        slug = slugify(project)
        for d in report.get("dimensions", []):
            rows.append({
                "id": f"{slug}-{d['key']}",
                "project_slug": slug,
                "key": d["key"],
                "label": d["label"],
                "score": d.get("score") or 0,
                "weight": d.get("weight") or 0,
                "description": d.get("description"),
            })
    return rows


def qa_phase_rows():
    """poc/qa.json -> `qa_phases` columns (one row per upstream phase per project)."""
    rows = []
    for project, report in load_optional("qa.json").items():
        slug = slugify(project)
        for i, ph in enumerate(report.get("phases", [])):
            rows.append({
                "id": f"{slug}-phase-{i:02d}",
                "project_slug": slug,
                "name": ph["name"],
                "status": ph.get("status") or "Not Started",
                "score": ph.get("score") or 0,
                "owner": ph.get("owner"),
                "sort_order": i,
            })
    return rows


def behavior_rows():
    """poc/behavior.json -> `behavior_profiles` columns (one row per project, PK=project_slug)."""
    rows = []
    for project, profile in load_optional("behavior.json").items():
        rows.append({
            "project_slug": slugify(project),
            "strategic_objectives": profile.get("strategicObjectives", []),
            "decision_patterns": profile.get("decisionPatterns", []),
            "risk_response": profile.get("riskResponse", []),
            "trade_offs": profile.get("tradeOffs", []),
        })
    return rows


def conflict_rows():
    """poc/conflicts.json -> `conflicts` columns (one row per conflict per project).

    Root-cause fix: the frontend (Conflict Center) reads the `conflicts` table but this
    sync never populated it. Source data exists in data_project/*/11-conflict.docx; the
    remaining upstream step is extract_conflicts.py emitting poc/conflicts.json. Until then
    load_optional() returns {} and this yields [] -> sync skips the table (no crash).
    """
    rows = []
    for project, items in load_optional("conflicts.json").items():
        slug = slugify(project)
        for i, c in enumerate(items):
            cid = str(c.get("id") or f"CONF-{i+1:03d}")
            rows.append({
                "id": cid if cid.startswith(slug) else f"{slug}-{cid}",
                "project_slug": slug,
                "category": c.get("category"),
                "title": c.get("title") or c.get("name") or "Untitled conflict",
                "description": c.get("description"),
                "severity": c.get("severity") or "Medium",
                "status": c.get("status") or "Unresolved",
                "version_a": c.get("versionA") or c.get("version_a") or {},
                "version_b": c.get("versionB") or c.get("version_b") or {},
                "resolution": c.get("resolution"),
                "affected_knowledge": c.get("affectedKnowledge") or c.get("affected_knowledge") or [],
                "affected_phase": c.get("affectedPhase") or c.get("affected_phase"),
                "updated_at": c.get("updatedAt") or c.get("updated_at"),
            })
    return rows


def relationship_rows():
    """poc/relationships.json -> `relationships` columns (entity-graph edges).

    Root-cause fix: the frontend Entity Graph reads the `relationships` table but this sync
    never populated it (edges came out empty). source/target must reference entities.id (FK).
    Remaining upstream step: extract_relationships.py emitting poc/relationships.json.
    Until then this yields [] -> sync skips the table (no crash, forward-compatible).
    """
    rows = []
    for project, items in load_optional("relationships.json").items():
        slug = slugify(project)
        for i, r in enumerate(items):
            rid = str(r.get("id") or f"REL-{i+1:03d}")
            rows.append({
                "id": rid if rid.startswith(slug) else f"{slug}-{rid}",
                "project_slug": slug,
                "source": r.get("source"),
                "target": r.get("target"),
                "type": r.get("type") or "related",
            })
    return rows



BUILDERS = {
    "projects": project_rows,
    "knowledge_items": knowledge_rows,
    "evidence_items": evidence_rows,
    "entities": entity_rows,
    "relationships": relationship_rows,
    "conflicts": conflict_rows,
    "qa_dimensions": qa_dimension_rows,
    "qa_phases": qa_phase_rows,
    "behavior_profiles": behavior_rows,
    "cif_patterns": pattern_rows,
    "cif_backtests": backtest_rows,
    "cif_decision_events": decision_event_rows,
}

ON_CONFLICT = {
    # behavior_profiles is keyed by project_slug directly, not `id`.
    "behavior_profiles": "project_slug",
}

# Insertion order matters for FK integrity: projects before anything referencing
# projects.slug, entities before relationships/evidence_items->knowledge_items chains,
# knowledge_items before evidence_items.
ORDER = ["projects", "entities", "relationships", "knowledge_items", "conflicts", "evidence_items", "qa_dimensions",
         "qa_phases", "behavior_profiles", "cif_patterns", "cif_backtests",
         "cif_decision_events"]


def upsert(base_url: str, key: str, table: str, rows: list):
    if not rows:
        return
    conflict_target = ON_CONFLICT.get(table, "id")
    url = f"{base_url.rstrip('/')}/rest/v1/{table}?on_conflict={conflict_target}"
    body = json.dumps(rows).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates,return=minimal",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            resp.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        sys.exit(f"upsert into {table} failed: HTTP {e.code}\n{detail}")


def main():
    ap = argparse.ArgumentParser(description="Sync poc/*.json to Intelligence Workspace's Supabase tables.")
    ap.add_argument("--dry-run", action="store_true", help="print rows, make no network calls")
    ap.add_argument("--only", help="comma-separated subset of: " + ",".join(TABLES))
    args = ap.parse_args()

    targets = args.only.split(",") if args.only else list(TABLES)
    unknown = [t for t in targets if t not in TABLES]
    if unknown:
        sys.exit(f"unknown table(s): {', '.join(unknown)} — valid: {', '.join(TABLES)}")

    rows_by_table = {t: BUILDERS[t]() for t in targets}

    if args.dry_run:
        for t in targets:
            print(f"=== {t}: {len(rows_by_table[t])} row(s) ===")
            print(json.dumps(rows_by_table[t], ensure_ascii=False, indent=2))
        return

    base_url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not base_url or not key:
        sys.exit("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set (see this file's docstring). "
                  "Use --dry-run to preview without them.")

    for t in [t for t in ORDER if t in targets]:
        upsert(base_url, key, t, rows_by_table[t])
        print(f"✅ synced {t}: {len(rows_by_table[t])} row(s)")


if __name__ == "__main__":
    main()
