#!/usr/bin/env python3
"""
extract_conflicts.py — pull structured Conflicts out of a Track C (DeepSeek methodology)
dossier's Conflict Resolution phase ("CONFLICT REGISTER WITH SEVERITY & IMPACT" section),
for Intelligence Workspace's `Conflict` contract
(`scryptexai/intelligence-workspace`'s `src/lib/types/conflict.ts`).

That section's real shape (verified against examples/CaseStudies/Arbitrum.md) is one field
per line per conflict block:

    Conflict C-NNN — <title>
    · Category: <text>
    · Description: <prose, usually naming 2-4 sources and their conflicting values>
    · Severity: <text>
    · Affected Knowledge: <K-### list or prose>
    · Impact: <text>
    · Affected Phase: <text>
    · Evidence: <source names, comma-separated>
    · Sources: <urls, comma-separated>
    · Resolution: <prose>
    · Status: <text>

NOT a general-purpose extractor -- deliberately hand-curated, and here's why:

Intelligence Workspace's `Conflict` type requires EXACTLY two sides (`versionA`/
`versionB`, each `{source, value, date, url, evidence}`). Of Arbitrum's 10 registered
conflicts, only 4 (C-001, C-004, C-008, C-009) name exactly two sources for exactly two
values, so the source<->value pairing is unambiguous. The other 6 (C-002, C-003, C-005,
C-006, C-007, C-010) cite 3-4 sources for 2-4 values with no reliable positional mapping
in free text -- automatically picking "the first two" or collapsing them would mean
inventing which source said which number, exactly the fabrication CLAUDE.md forbids.
Regexing the per-source `value`/`date` split out of the free-text Description also isn't
reliable across conflicts (formats vary: "X melaporkan A, sementara Y melaporkan B" vs
"X: A; Y: B" vs a table-less list) -- CONFLICTS below were read and transcribed by hand
from the dossier text, not derived by pattern-matching.

If a future dossier's Conflict Register has a cleaner, more uniform two-source shape,
extend CONFLICTS (or replace this with a real regex parser) rather than force this one
through automation it can't yet support reliably.

`category` is kept as the dossier's own literal value (Financial, Market, Token, ...)
rather than force-mapped onto Intelligence Workspace's narrower ConflictCategory enum
(Governance/Tokenomics/Security/Roadmap/Compliance/Data) -- same "don't fabricate a
mapping" reasoning as extract_events.py's `type` field. The `conflicts.category` column
is plain text, no DB-level enum constraint.

Usage:  python3 tools/extract_conflicts.py Arbitrum
Output: poc/conflicts.json  (merges/replaces entries for the parsed project)
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "conflicts.json"

# Hand-transcribed from examples/CaseStudies/Arbitrum.md's CONFLICT REGISTER
# (lines ~10368-10497), restricted to the 4 conflicts with an unambiguous 2-source split.
CONFLICTS = {
    "Arbitrum": [
        {
            "id": "C-001",
            "projectSlug": "arbitrum",
            "category": "Financial",
            "title": "Treasury Size ($1.21B vs $1.3B+)",
            "description": "Messari melaporkan $1.21B (per 31 Mei 2025), sementara KuCoin melaporkan $1.3B+. Perbedaan ~$90M (7%).",
            "severity": "Medium",
            "status": "Unresolved",
            "versionA": {"source": "Messari", "value": "$1.21B", "date": "2025-05-31", "url": "https://messari.io/", "evidence": "Treasury size, reported as of 31 May 2025"},
            "versionB": {"source": "KuCoin", "value": "$1.3B+", "date": "", "url": "https://www.kucoin.com/", "evidence": "More recent data than Messari's; exact capture date not stated"},
            "resolution": "Perbedaan disebabkan oleh waktu pengambilan data dan metodologi. Messari per 31 Mei 2025; KuCoin data lebih baru. Tidak resolved.",
            "affectedKnowledge": ["K-002"],
            "affectedPhase": "Phase 5",
        },
        {
            "id": "C-004",
            "projectSlug": "arbitrum",
            "category": "Market",
            "title": "Daily Transactions (4.7M vs 1.5M)",
            "description": "KuCoin melaporkan 4.7M daily transactions (Feb 2026), sementara Blockeden melaporkan 1.5M.",
            "severity": "High",
            "status": "Unresolved",
            "versionA": {"source": "KuCoin", "value": "4.7M daily transactions", "date": "2026-02", "url": "https://www.kucoin.com/", "evidence": ""},
            "versionB": {"source": "Blockeden", "value": "1.5M daily transactions", "date": "", "url": "https://blockeden.xyz/", "evidence": ""},
            "resolution": "Perbedaan karena periode waktu berbeda atau metodologi berbeda. Tidak resolved.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 8",
        },
        {
            "id": "C-008",
            "projectSlug": "arbitrum",
            "category": "Token",
            "title": "Distribution Percentages (42.78% vs 35.3% DAO)",
            "description": "The Block: 42.78% DAO Treasury; KuCoin: 35.3% DAO.",
            "severity": "High",
            "status": "Unresolved",
            "versionA": {"source": "The Block", "value": "42.78% DAO Treasury", "date": "", "url": "https://www.theblock.co/", "evidence": ""},
            "versionB": {"source": "KuCoin", "value": "35.3% DAO", "date": "", "url": "https://www.kucoin.com/", "evidence": ""},
            "resolution": "Perbedaan karena kategorisasi yang berbeda (DAO Treasury vs Foundation operational budget). Tidak resolved.",
            "affectedKnowledge": ["K-010"],
            "affectedPhase": "Phase 6",
        },
        {
            "id": "C-009",
            "projectSlug": "arbitrum",
            "category": "Governance",
            "title": "Voting Power Concentration (Top 10 ~50% vs ~85%)",
            "description": "Beberapa sumber menyebut top 10 addresses ~50%, sumber lain menyebut top 100 hold 60-85%.",
            "severity": "High",
            "status": "Unresolved",
            "versionA": {"source": "Phase 6 — Holder Distribution", "value": "Top 10 addresses ~50%", "date": "", "url": "", "evidence": "Internal dataset"},
            "versionB": {"source": "Phase 9 — Governance Decision Pattern", "value": "Top 100 hold 60-85%", "date": "", "url": "", "evidence": "Internal dataset"},
            "resolution": "Perbedaan karena cakupan analisis (top 10 vs top 100). Tidak resolved.",
            "affectedKnowledge": ["K-004", "K-005"],
            "affectedPhase": "Phase 6",
        },
    ],
}

SKIPPED = {
    "Arbitrum": ["C-002", "C-003", "C-005", "C-006", "C-007", "C-010"],
}


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 tools/extract_conflicts.py <ProjectName>  (must be a key in CONFLICTS)")
    project = sys.argv[1]
    if project not in CONFLICTS:
        sys.exit(f"no hand-curated conflicts for {project!r} -- see this file's module docstring "
                  f"for why this isn't a general regex extractor yet.")

    data = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    data[project] = CONFLICTS[project]
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    skipped = SKIPPED.get(project, [])
    print(f"✅ wrote {len(CONFLICTS[project])} conflict(s) for {project} -> {OUT}")
    if skipped:
        print(f"⚠️  skipped {len(skipped)} multi-source conflict(s) (ambiguous source->value mapping): "
              f"{', '.join(skipped)}")


if __name__ == "__main__":
    main()
