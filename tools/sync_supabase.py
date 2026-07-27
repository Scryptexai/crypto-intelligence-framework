#!/usr/bin/env python3
"""
sync_supabase.py — push poc/{projects,patterns,benchmarks}.json to the CIF-owned Supabase tables
(cif_projects, cif_patterns, cif_backtests) described in
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
    python3 tools/sync_supabase.py             # upsert all three tables
    python3 tools/sync_supabase.py --dry-run   # print the rows that would be sent, no network call
    python3 tools/sync_supabase.py --only cif_projects,cif_patterns

Known limitation (by design, not a bug): pattern_confidence, trajectory_probability, observable,
current_read, signal, evidence, comparables in cif_projects are left null/empty. Those need a
per-project synthesis step (turning an 11-phase dossier into a UI-ready Current Read/Signal) that
does not exist yet — ApplicationBlueprint.md §8 lists this as an open question. Do not fabricate
placeholder values for them here; a null field is honest, a guessed one is not.
"""
import argparse, json, os, re, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POC = ROOT / "poc"
TABLES = ("cif_projects", "cif_patterns", "cif_backtests")


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
    """poc/projects.json (build_json.py's roster shape) -> cif_projects columns. Only the
    deterministic roster fields are populated -- see module docstring's Known limitation."""
    rows = []
    for p in load("projects.json"):
        rows.append({
            "id": slugify(p["n"]),
            "name": p["n"],
            "category": split_category(p.get("cat", "")),
            "tier": p["tier"].lower(),
            "era": p.get("era") or None,
            "tags": p.get("tags", []),
            "source_file": p["file"],
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


BUILDERS = {"cif_projects": project_rows, "cif_patterns": pattern_rows, "cif_backtests": backtest_rows}


def upsert(base_url: str, key: str, table: str, rows: list):
    if not rows:
        return
    url = f"{base_url.rstrip('/')}/rest/v1/{table}?on_conflict=id"
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
