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
    python3 tools/sync_supabase.py             # upsert every table in TABLES below
    python3 tools/sync_supabase.py --dry-run   # print the rows that would be sent, no network call
    python3 tools/sync_supabase.py --only projects,entities
"""
import argparse, json, os, re, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POC = ROOT / "poc"
# Synced by default: the tables this script writes. Verified against the live schema
# 2026-08-11 -- 17 tables, of which relationships is empty by design and
# users/saved_views/notes belong to the frontend. The four airdrop_* tables carry Phase 12
# (created 2026-08-11, schema agreed with the maintainer before creation per CLAUDE.md).
TABLES = ("projects", "knowledge_items", "evidence_items", "entities", "events", "conflicts",
          "qa_dimensions", "qa_phases", "behavior_profiles",
          "airdrop_profiles", "airdrop_events", "airdrop_pov_outcomes", "airdrop_retention")

# Buildable but NOT synced by default: the older AirdropOS-style schema, which lives in a
# different Supabase project. Requesting them against the CIF project returns PGRST205
# ("Could not find the table 'public.cif_patterns' in the schema cache") -- and because that
# is a hard failure, `./run.sh sync` exited non-zero on every single run and closed with an
# alarming 404 right after nine successful upserts. Reachable deliberately when pointed at the
# project that does have them:  --only cif_patterns,cif_backtests,cif_decision_events
LEGACY_TABLES = ("cif_patterns", "cif_backtests", "cif_decision_events")


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


def event_rows():
    """poc/events.json (tools/extract_events.py's shape) -> `events` columns.

    `_location`/`_status` are extractor-only reference fields (no column in the real
    schema) and are dropped here rather than smuggled into `metadata`-less `events`."""
    rows = []
    for _project, events in load_optional("events.json").items():
        for e in events:
            rows.append({
                "id": e["id"],
                "project_slug": e["projectSlug"],
                "name": e.get("name"),
                "date": e.get("date"),
                "type": e.get("type"),
                "participants": e.get("participants", []),
                "description": e.get("description"),
                "result": e.get("result"),
                "source": e.get("source"),
                "url": e.get("url"),
                "affected_knowledge": e.get("affectedKnowledge", []),
            })
    return rows


def conflict_rows():
    """poc/conflicts.json (tools/extract_conflicts.py's hand-curated shape) -> `conflicts`
    columns."""
    rows = []
    for _project, items in load_optional("conflicts.json").items():
        for c in items:
            rows.append({
                "id": c["id"],
                "project_slug": c["projectSlug"],
                "category": c.get("category"),
                "title": c.get("title"),
                "description": c.get("description"),
                "severity": c.get("severity") or "Medium",
                "status": c.get("status") or "Unresolved",
                "version_a": c["versionA"],
                "version_b": c["versionB"],
                "resolution": c.get("resolution"),
                "affected_knowledge": c.get("affectedKnowledge", []),
                "affected_phase": c.get("affectedPhase"),
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


# ---------------------------------------------------------------------------
# Phase 12 — Airdrop Intelligence. Four tables from one poc/airdrop.json.
#
# Everything stays text, matching the schema: reports state ranges and
# qualifications ("2023-05 hingga 2023-11", "12% dari total supply (360.000.000
# BLUR)") that parsing into date/numeric would have to guess at, and a guessed
# value that looks precise is worse than the honest string.
# ---------------------------------------------------------------------------

def airdrop_profile_rows():
    """One row per project, PK=project_slug."""
    rows = []
    for project, prof in load_optional("airdrop.json").items():
        prospect = prof.get("prospect") or {}
        rows.append({
            "project_slug": slugify(project),
            "status": prof.get("status") or "Belum ada",
            "prospect_met": prospect.get("met"),
            "prospect_unmet": prospect.get("unmet"),
            "prospect_signals": prospect.get("signals"),
            "prospect_note": prospect.get("assessment"),
        })
    return rows


def airdrop_event_rows():
    """One row per distribution wave. id is slug-prefixed because AD-001 restarts at 1 in
    every project -- the same collision that put duplicate EV-001 ids into `events` and made
    a bulk upsert fail with Postgres 21000 (ON CONFLICT cannot affect a row twice)."""
    rows = []
    for project, prof in load_optional("airdrop.json").items():
        slug = slugify(project)
        for i, ev in enumerate(prof.get("events") or [], start=1):
            rows.append({
                "id": f"{slug}-{ev['id']}",
                "project_slug": slug,
                "seq": i,
                "title": ev.get("title"),
                "event_date": ev.get("date"),
                "type": ev.get("type"),
                "allocation": ev.get("allocation"),
                "recipients": ev.get("recipients"),
                "value_at_claim": ev.get("valueAtClaim"),
                "criteria": ev.get("criteria"),
                "anti_sybil": ev.get("antiSybil"),
                "related_event": ev.get("relatedEvent"),
                "citation": ev.get("citation"),
            })
    return rows


def airdrop_pov_rows():
    """Eight rows per project. A POV that does not apply is stored as "Tidak relevan" rather
    than skipped: a missing row and a deliberate not-applicable are different facts, and
    keeping them apart is the point of the per-POV format."""
    rows = []
    for project, prof in load_optional("airdrop.json").items():
        slug = slugify(project)
        for pov, out in (prof.get("povOutcomes") or {}).items():
            rows.append({
                "id": f"{slug}-{pov}",
                "project_slug": slug,
                "pov": pov,
                "verdict": out.get("verdict"),
                "verdict_raw": out.get("verdictRaw"),
                "qualifier": out.get("qualifier"),
                "short_term": out.get("shortTerm"),
                "long_term": out.get("longTerm"),
                "basis": out.get("basis"),
            })
    return rows


def airdrop_retention_rows():
    rows = []
    for project, prof in load_optional("airdrop.json").items():
        slug = slugify(project)
        for i, metric in enumerate(prof.get("retention") or [], start=1):
            rows.append({"id": f"{slug}-r{i}", "project_slug": slug,
                         "seq": i, "metric": metric})
    return rows


BUILDERS = {
    "projects": project_rows,
    "knowledge_items": knowledge_rows,
    "evidence_items": evidence_rows,
    "entities": entity_rows,
    "events": event_rows,
    "conflicts": conflict_rows,
    "qa_dimensions": qa_dimension_rows,
    "qa_phases": qa_phase_rows,
    "behavior_profiles": behavior_rows,
    "airdrop_profiles": airdrop_profile_rows,
    "airdrop_events": airdrop_event_rows,
    "airdrop_pov_outcomes": airdrop_pov_rows,
    "airdrop_retention": airdrop_retention_rows,
    "cif_patterns": pattern_rows,
    "cif_backtests": backtest_rows,
    "cif_decision_events": decision_event_rows,
}

ON_CONFLICT = {
    # These two are keyed by project_slug directly, not `id`.
    "behavior_profiles": "project_slug",
    "airdrop_profiles": "project_slug",
}

# Insertion order matters for FK integrity: projects before anything referencing
# projects.slug, entities before relationships/evidence_items->knowledge_items chains,
# knowledge_items before evidence_items.
ORDER = ["projects", "entities", "knowledge_items", "evidence_items", "events", "conflicts",
         "qa_dimensions", "qa_phases", "behavior_profiles",
         # all four airdrop_* tables FK to projects.slug, so they follow projects
         "airdrop_profiles", "airdrop_events", "airdrop_pov_outcomes", "airdrop_retention",
         "cif_patterns", "cif_backtests", "cif_decision_events"]


CHUNK_SIZE = 500


def _post_batch(base_url: str, key: str, table: str, rows: list):
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


def upsert(base_url: str, key: str, table: str, rows: list):
    """Upsert rows, grouped by their exact key set and chunked.

    PostgREST requires every object in one bulk POST to carry an IDENTICAL set of keys --
    a mismatch fails the whole request with PGRST102 "All object keys must match". Several
    row builders here deliberately OMIT a field rather than send null, so that an upsert
    leaves the existing column untouched instead of blanking it (see project_rows'
    docstring: cif_score is only present for projects that actually have a QA score, which
    today is Track C dossiers with Phase 11 run). With 2 projects that happened to be
    uniform; at 26 projects one row carried cif_score and 25 did not, so every sync died
    before writing anything. Grouping by key set keeps the omit-means-leave-alone semantics
    intact while satisfying PostgREST -- rather than forcing nulls in, which would silently
    wipe real scores on every future sync. Chunking additionally keeps a single request from
    carrying the full table (entities is already 1109 rows)."""
    if not rows:
        return
    groups = {}
    for row in rows:
        groups.setdefault(tuple(sorted(row.keys())), []).append(row)
    for group in groups.values():
        for i in range(0, len(group), CHUNK_SIZE):
            _post_batch(base_url, key, table, group[i:i + CHUNK_SIZE])


def main():
    ap = argparse.ArgumentParser(description="Sync poc/*.json to Intelligence Workspace's Supabase tables.")
    ap.add_argument("--dry-run", action="store_true", help="print rows, make no network calls")
    ap.add_argument("--only", help="comma-separated subset of: " + ",".join(TABLES)
                                   + " (or, for the other Supabase project, "
                                   + ",".join(LEGACY_TABLES) + ")")
    args = ap.parse_args()

    selectable = TABLES + LEGACY_TABLES
    targets = args.only.split(",") if args.only else list(TABLES)
    unknown = [t for t in targets if t not in selectable]
    if unknown:
        sys.exit(f"unknown table(s): {', '.join(unknown)} — valid: {', '.join(selectable)}")

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

    # ORDER decides both sequence and inclusion, so a table missing from it is built and then
    # silently dropped -- rows counted in --dry-run, never posted, no error. The four
    # airdrop_* tables were one edit away from exactly that. Fail loudly instead: an omission
    # here is always a mistake, never a choice.
    unordered = sorted(set(targets) - set(ORDER))
    if unordered:
        sys.exit(f"table(s) {', '.join(unordered)} are in TABLES/--only but missing from ORDER, "
                 f"so they would be built and never sent. Add them to ORDER, after any table "
                 f"they reference by foreign key.")

    for t in [t for t in ORDER if t in targets]:
        upsert(base_url, key, t, rows_by_table[t])
        print(f"✅ synced {t}: {len(rows_by_table[t])} row(s)")


if __name__ == "__main__":
    main()
