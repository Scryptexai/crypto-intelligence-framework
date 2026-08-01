#!/usr/bin/env python3
"""
sync_supabase.py — push poc/{projects,patterns,benchmarks,decision_events}.json to the CIF-owned
Supabase tables (cif_projects, cif_patterns, cif_backtests, cif_decision_events) described in
crypto-intelligence-framework's docs/Project/ApplicationBlueprint.md §10.1.

Deterministic upsert, no LLM, stdlib only (no `requests`/`supabase-py` dependency — matches the
rest of tools/'s minimal-dependency convention, see requirements.txt). Talks to Supabase's
PostgREST API directly.

Requires two environment variables (never commit these — same treatment as the research prompts,
see docs/Protocol/Deep-Research-Brief.md's policy note):
    SUPABASE_URL               e.g. https://szumyjuvfjkobvcqswwd.supabase.co
    SUPABASE_SERVICE_ROLE_KEY  the service_role key — bypasses RLS, required because these tables'
                                 policies only grant SELECT to clients (ApplicationBlueprint.md
                                 §10.1): writes are meant to happen ONLY through this script.

Usage:
    export SUPABASE_URL="https://<ref>.supabase.co"
    export SUPABASE_SERVICE_ROLE_KEY="..."
    python3 tools/sync_supabase.py             # upsert all four tables
    python3 tools/sync_supabase.py --dry-run   # print the rows that would be sent, no network call
    python3 tools/sync_supabase.py --only cif_projects,cif_patterns

Note (corrected 2026-07-27): an earlier version of this docstring claimed pattern_confidence,
trajectory_probability, observable, current_read, signal, evidence, comparables in cif_projects
were "intentionally left null/empty" pending a synthesis step that didn't exist. That was wrong —
those fields are populated for LayerZero (seeded via the AirdropOS frontend rebuild + this repo's
P7-P16 pattern promotion, applied by direct SQL rather than this script). This script's
project_rows()/pattern_rows() still describe the deterministic-roster fields it derives from
poc/*.json; it does not yet re-derive the richer per-project fields — don't assume running this
script alone reproduces everything currently live in cif_projects.
"""
import argparse, json, os, re, sys, urllib.error, urllib.request
from datetime import datetime as _dt, timezone as _tz
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POC = ROOT / "poc"
TABLES = ("cif_projects", "cif_patterns", "cif_backtests", "cif_decision_events", "cif_entities")


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def split_category(cat: str):
    """'Interoperability / Omnichain Messaging (Bridge, GMP, DVN security)' ->
    ['Interoperability', 'Omnichain Messaging', 'Bridge', 'GMP', 'DVN security']. category is a
    text[] column (filterable/taggable), not a single blob string -- verified against the live
    cif_projects.category value already synced for LayerZero, which splits exactly this way."""
    if not cat:
        return []
    m = re.search(r"\(([^)]*)\)", cat)
    paren = [x.strip() for x in m.group(1).split(",")] if m else []
    main = re.sub(r"\([^)]*\)", "", cat).strip()
    parts = [x.strip() for x in main.split("/")] if main else []
    return [p for p in (parts + paren) if p]


def load(name: str):
    p = POC / name
    if not p.exists():
        sys.exit(f"{p} not found — run ./run.sh (or tools/build_json.py) first.")
    return json.loads(p.read_text(encoding="utf-8"))


def project_rows():
    """poc/projects.json (build_json.py's roster shape) -> cif_projects columns.

    cif_projects was repurposed for Intelligence Workspace's Project contract (2026-08-01
    reset, see docs/Project/ApplicationBlueprint.md and the migration applied that day) --
    it no longer has AirdropOS-only columns like `tier`. Only fields this script can derive
    without guessing are populated: entity_count from poc/entities.json (a real count, not a
    fabricated one), status defaults to "active" as CIF's own curation-state label (every
    project in examples/CaseStudies/ is, by definition, actively tracked -- this is a
    workflow flag CIF assigns, not a claim about the project itself). symbol/tagline/
    description/color/accent/cifScore/confidence/qa/behavior have no deterministic source
    yet and are intentionally omitted so upsert leaves them untouched rather than nulling
    real data or guessing fake values -- see extract_knowledge.py/extract_qa.py (not yet
    built) for what would need to exist before those can be populated honestly."""
    entity_counts = {}
    entities_path = POC / "entities.json"
    if entities_path.exists():
        for project, ents in json.loads(entities_path.read_text(encoding="utf-8")).items():
            entity_counts[slugify(project)] = len(ents)

    rows = []
    for p in load("projects.json"):
        slug = slugify(p["n"])
        rows.append({
            "id": slug,
            "slug": slug,
            "name": p["n"],
            "category": split_category(p.get("cat", "")),
            "era": p.get("era") or None,
            "tags": p.get("tags", []),
            "source_file": p["file"],
            "status": "active",
            "entity_count": entity_counts.get(slug, 0),
            "knowledge_count": 0,
            "conflict_count": 0,
            "event_count": 0,
            "last_updated": _dt.now(_tz.utc).isoformat(),
            "last_activity_hours": 0,
        })
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
    """poc/entities.json (tools/extract_entities.py's shape) -> cif_entities columns.
    Composite id (project_slug, id) matches Intelligence Workspace's
    /projects/{slug}/entities/{id} route."""
    rows = []
    data = load("entities.json")
    for _project, entities in data.items():
        for e in entities:
            rows.append({
                "project_slug": e["projectSlug"],
                "id": e["id"],
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


BUILDERS = {
    "cif_projects": project_rows,
    "cif_patterns": pattern_rows,
    "cif_backtests": backtest_rows,
    "cif_decision_events": decision_event_rows,
    "cif_entities": entity_rows,
}


ON_CONFLICT = {
    # cif_entities has a composite primary key (project_slug, id) -- see the migration in
    # this session's Intelligence Workspace reset -- every other table keys on bare id.
    "cif_entities": "project_slug,id",
}


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
    ap = argparse.ArgumentParser(description="Sync poc/*.json to CIF's Supabase tables.")
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

    for t in targets:
        upsert(base_url, key, t, rows_by_table[t])
        print(f"✅ synced {t}: {len(rows_by_table[t])} row(s)")


if __name__ == "__main__":
    main()
