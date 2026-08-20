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
import json, os, sys
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

    "Curve": [
        {
            "id": "C-001",
            "projectSlug": "curve",
            "category": "Tokenomics",
            "title": "Komposisi distribusi non-komunitas (Team 30% vs shareholders 30%)",
            "description": "Phase 6 dataset mencatat Team 30%/Investors 3%/Foundation 3%/Employees 2%; sumber publik umum menyebut shareholders 30%/team 3%/early users 5%. Atribusi 30% supply berbeda penerimanya.",
            "severity": "High",
            "status": "Unresolved",
            "versionA": {"source": "Phase 6 dataset (pipeline)", "value": "Community 62%, Team 30% (2y vesting), Investors 3% (2y), Foundation 3% (4y), Employees 2% (2y)", "date": "", "url": "", "evidence": "Internal dataset"},
            "versionB": {"source": "Sumber publik umum (liputan pengumuman CRV Agu 2020)", "value": "Community 62%, shareholders 30%, team 3%, early users 5%", "date": "2020-08", "url": "", "evidence": "Tidak primer; agregasi liputan publik"},
            "resolution": "Keduanya dipertahankan; verifikasi dokumen primer Agustus 2020 diperlukan sebelum memilih.",
            "affectedKnowledge": ["K-002"],
            "affectedPhase": "Phase 6",
        },
    ],
    "Walrus": [
        {
            "id": "C-001",
            "projectSlug": "walrus",
            "category": "Tokenomics",
            "title": "Breakdown distribusi komunitas (43% reserve vs 10% airdrop)",
            "description": "Altcoin Buzz menyebut Community Reserve 43% dengan 690 juta token available at launch; Backpack Exchange memecah 10% community airdrop (4% pre-mainnet + 6% post-mainnet). Keduanya dapat konsisten namun tidak dikonfirmasi dokumen resmi.",
            "severity": "Medium",
            "status": "Unresolved",
            "versionA": {"source": "Altcoin Buzz", "value": "Community Reserve 43% (690 juta available at launch, linear unlock hingga Mar 2033)", "date": "2025-03", "url": "https://www.altcoinbuzz.io/reviews/walrus-protocol-mainnet-and-tge-are-coming/", "evidence": ""},
            "versionB": {"source": "Backpack Exchange Learn", "value": "Community airdrop 10% (4% pre-mainnet + 6% post-mainnet)", "date": "2025-05", "url": "https://learn.backpack.exchange/articles/what-is-walrus-a-programmable-decentralized-storage-network", "evidence": ""},
            "resolution": "Keduanya dipertahankan dengan flag INKONSISTENSI; dokumen tokenomics resmi Walrus diperlukan.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 6",
        },
    ],
    "Linea": [
        {
            "id": "C-002",
            "projectSlug": "linea",
            "category": "Timeline",
            "title": "Tanggal TGE LINEA (akhir Juli 2025 vs 10 September 2025)",
            "description": "Sumber pra-launch menyebut TGE akhir Juli 2025; realisasi pelaksanaan adalah 10 September 2025.",
            "severity": "Medium",
            "status": "Resolved",
            "versionA": {"source": "Bitrue (pra-launch)", "value": "TGE akhir Juli 2025", "date": "2025-07-15", "url": "https://www.bitrue.com/blog/linea-tokenomics-and-airdrop-eligibility", "evidence": "Artikel pra-launch"},
            "versionB": {"source": "The Block (pelaksanaan)", "value": "TGE 10 September 2025", "date": "2025-09-10", "url": "https://www.theblock.co/post/370206/consensys-ethereum-l2-linea-launches-tge-with-9-4-billion-token-airdrop-after-brief-outage", "evidence": "Liputan eksekusi"},
            "resolution": "Tanggal pelaksanaan 2025-09-10 dipakai (sumber eksekusi); laporan pra-launch dicatat sebagai ekspektasi yang meleset.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 1",
        },
    ],

    "Terra": [
        {
            "id": "C-003",
            "projectSlug": "terra",
            "category": "Token",
            "title": "LUNC total supply (~6.1T CoinGecko vs ~6.5T burn tracker)",
            "description": "CoinGecko melaporkan total supply ~6.1T LUNC (circulating ~5.8T); Lunc Burn tracker melaporkan ~6.5T. Perbedaan besar karena metodologi pelaporan (apakah supply pra-burn dihitung).",
            "severity": "High",
            "status": "Unresolved",
            "versionA": {"source": "CoinGecko", "value": "~6.1T LUNC total (circulating ~5.8T)", "date": "", "url": "https://www.coingecko.com/", "evidence": ""},
            "versionB": {"source": "Lunc Burn tracker", "value": "~6.5T LUNC", "date": "", "url": "", "evidence": "Komunitas burn tracker"},
            "resolution": "Perbedaan metodologi pelaporan (supply pra-burn vs pasca-burn). Tidak resolved.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 6",
        },
        {
            "id": "C-014",
            "projectSlug": "terra",
            "category": "Token",
            "title": "LUNA total=circulating 1,170,305,141 vs 200M community pool belum ter-spend",
            "description": "Phase 6 menulis total supply dan circulating supply sama (1,170,305,141 LUNA), padahal ada ~200M LUNA di community pool yang belum ter-spend — circulating efektif seharusnya lebih rendah.",
            "severity": "Medium",
            "status": "Unresolved",
            "versionA": {"source": "Phase 6 dataset", "value": "Total = circulating = 1,170,305,141 LUNA", "date": "", "url": "", "evidence": "Internal dataset"},
            "versionB": {"source": "On-chain community pool", "value": "~200,000,000 LUNA di community pool belum ter-spend", "date": "", "url": "", "evidence": "Catatan on-chain Terra 2.0"},
            "resolution": "Keduanya dipertahankan; circulating efektif bergantung pada apakah community pool dihitung. Tidak resolved.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 6",
        },
    ],
    "Cardano": [
        {
            "id": "C-001",
            "projectSlug": "cardano",
            "category": "Timeline",
            "title": "Definisi TGE ADA (akhir voucher Jan 2017 vs mainnet 29 Sep 2017)",
            "description": "Sumber berbeda mendefinisikan TGE ADA berbeda: akhir penjualan voucher Januari 2017, snapshot distribusi ke voucher holder, atau mainnet live 29 September 2017.",
            "severity": "High",
            "status": "Unresolved",
            "versionA": {"source": "Sumber penjualan voucher", "value": "TGE = akhir penjualan voucher, Januari 2017", "date": "2017-01", "url": "", "evidence": ""},
            "versionB": {"source": "Sumber mainnet", "value": "TGE = mainnet live, 29 September 2017", "date": "2017-09-29", "url": "", "evidence": ""},
            "resolution": "Kedua tanggal sahih untuk definisi berbeda (penjualan vs mainnet). Dataset memakai mainnet 2017-09-29 sebagai launch kanonikal; ambiguitas dicatat.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 1",
        },
        {
            "id": "C-003",
            "projectSlug": "cardano",
            "category": "Token",
            "title": "Jumlah ADA terjual (~25.9B Messari vs ~26.9B sumber lain)",
            "description": "Messari melaporkan ~25.9B ADA terjual selama penjualan; beberapa sumber lain menyebut ~26.9B termasuk alokasi tim/foundation.",
            "severity": "High",
            "status": "Unresolved",
            "versionA": {"source": "Messari", "value": "~25.9B ADA terjual", "date": "", "url": "https://messari.io/", "evidence": ""},
            "versionB": {"source": "Sumber lain (termasuk alokasi tim/foundation)", "value": "~26.9B ADA", "date": "", "url": "", "evidence": ""},
            "resolution": "Perbedaan cakupan (penjualan publik saja vs termasuk alokasi tim/foundation). Tidak resolved.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 5",
        },
    ],
    "SushiSwap": [
        {
            "id": "C-001",
            "projectSlug": "sushiswap",
            "category": "Token",
            "title": "Circulating supply SUSHI (~262M CoinGecko vs hard cap 250M)",
            "description": "CoinGecko melaporkan circulating supply ~262M SUSHI sementara max supply hard cap 250M SUSHI; Etherscan total supply menunjukkan ~249.9M. Angka circulating melampaui hard cap adalah anomali definisi.",
            "severity": "High",
            "status": "Unresolved",
            "versionA": {"source": "CoinGecko", "value": "Circulating ~262M SUSHI", "date": "", "url": "https://www.coingecko.com/", "evidence": ""},
            "versionB": {"source": "Etherscan", "value": "Total supply ~249.9M SUSHI (hard cap 250M)", "date": "", "url": "https://etherscan.io/", "evidence": ""},
            "resolution": "Anomali kemungkinan karena metodologi 'circulating' agregator (termasuk token yang secara teknis belum beredar). Tidak resolved.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 6",
        },
    ],
    "Uniswap": [
        {
            "id": "C-003",
            "projectSlug": "uniswap",
            "category": "Financial",
            "title": "Seed round amount (~$1M vs ~$2M)",
            "description": "Jumlah seed round tidak diungkap resmi; laporan media bervariasi antara ~$1M dan ~$2M.",
            "severity": "Low",
            "status": "Unresolved",
            "versionA": {"source": "Laporan media (sebagian)", "value": "~$1M", "date": "", "url": "", "evidence": ""},
            "versionB": {"source": "Laporan media (sebagian lain)", "value": "~$2M", "date": "", "url": "", "evidence": ""},
            "resolution": "Tidak ada disclosure resmi; dataset menulis '~$1M-$2M'. Tidak resolved.",
            "affectedKnowledge": [],
            "affectedPhase": "Phase 5",
        },
    ],
}

SKIPPED = {
    "Arbitrum": ["C-002", "C-003", "C-005", "C-006", "C-007", "C-010"],
}


# ---------------------------------------------------------------------------
# Conservative uniform-format parser (added 2026-08-20)
#
# The Track C pipeline produced uniform Conflict Register blocks across most
# dossiers:  "Conflict C-NNN" + Category/Description/Severity/Status/
# Resolution/Affected Knowledge/Affected Phase/Sources lines (bare or '- '
# bulleted). The structured fields parse reliably; the ONLY unreliable part is
# pairing versionA/versionB from the free-text Description. So this parser
# emits a conflict row ONLY when the Description matches one of two strict
# two-side patterns AND both sides carry a figure -- everything else is
# skipped with a logged reason, exactly per the module docstring's rule
# against inventing source<->value mappings.
# ---------------------------------------------------------------------------
import re

_FIELD_NAMES = ["Category", "Description", "Severity", "Affected Knowledge",
                "Impact", "Affected Phase", "Evidence", "Sources", "Resolution", "Status"]


def _parse_fields(block: str) -> dict:
    out = {}
    for name in _FIELD_NAMES:
        m = re.search(rf"^[- ]*{re.escape(name)}:\s*(.+?)\s*$", block, re.M)
        if m:
            out[name.lower().replace(" ", "_")] = m.group(1).strip()
    return out


_PAIR_PATTERNS = [
    # "X melaporkan A, sementara Y melaporkan B"
    re.compile(r"(.{2,80}?)\s+(?:melaporkan|mencatat|menyebut|mengatakan)\s+(.{3,100}?),\s+"
               r"sementara\s+(.{2,80}?)\s+(?:melaporkan|mencatat|menyebut|mengatakan)\s+(.{3,100}?)(?:\.|$)"),
    # "X: A; Y: B"
    re.compile(r"(.{2,80}?):\s+(.{3,100}?);\s+(.{2,80}?):\s+(.{3,100}?)(?:\.|$)"),
    # "80,000 BTC (Nansen) dan 80,394 BTC (Blockchain.com)" -- values lead, sources in parens
    re.compile(r"([\d][\d.,]*\s*%?[^(),]{0,20}?)\s*\((.{2,60}?)\)\s*(?:dan|vs\.?|,)\s+"
               r"([\d][\d.,]*\s*%?[^(),]{0,20}?)\s*\((.{2,60}?)\)"),
    # "X menyebut A, beberapa sumber lain menyebut B"
    re.compile(r"(.{2,80}?)\s+menyebut\s+(.{3,60}?),\s+((?:beberapa sumber lain|sumber lain|sumber lainnya)[^,.]{0,40}?)"
               r"\s+menyebut\s+(.{3,60}?)(?:\.|$)"),
]

# Track C registers also AUDIT consistency -- blocks that conclude "no real conflict"
# ("Konsisten", "tidak ada konflik") are audit notes, not conflicts, and must not enter
# the table even when a pattern happens to match their wording.
_NOT_A_CONFLICT_RE = re.compile(r"\b(?:konsisten|tidak ada konflik|bukan konflik|no conflict)\b", re.I)


def _try_pair(description: str):
    """(versionA, versionB) when a strict two-side split exists, else None."""
    for idx, pat in enumerate(_PAIR_PATTERNS):
        m = pat.search(description)
        if not m:
            continue
        g = tuple(x.strip() for x in m.groups())
        if idx == 2:
            # values lead, sources in parentheses: (valueA, sourceA, valueB, sourceB)
            va, sa, vb, sb = g
        else:
            sa, va, sb, vb = g
        # Source captures can swallow leading prose ("...tercatat berbeda antar sumber —
        # Phase 3 (EV-012)"); keep only the tail after the last dash/comma when long.
        def _clean_source(s: str) -> str:
            if len(s) > 40:
                for sep in ("—", "–", ",", ":"):
                    if sep in s:
                        tail = s.rsplit(sep, 1)[1].strip()
                        if tail:
                            s = tail
            return s
        sa, sb = _clean_source(sa), _clean_source(sb)
        # Both VALUES must carry a figure, otherwise the "pair" is qualitative
        # prose and the mapping would be a guess.
        if re.search(r"\d", va) and re.search(r"\d", vb):
            return ({"source": sa, "value": va, "date": "", "url": "", "evidence": ""},
                    {"source": sb, "value": vb, "date": "", "url": "", "evidence": ""})
    return None


def parse_dossier_conflicts(project: str):
    """(rows, skipped) from a dossier's Conflict Register -- pairing-only extraction."""
    path = ROOT / "examples" / "CaseStudies" / f"{project}.md"
    if not path.exists():
        return [], []
    text = path.read_text(encoding="utf-8")
    # Heading shapes: "Conflict C-001" and "Conflict C-001 — <title>"
    parts = re.split(r"^Conflict (C-\d+)(?:\s*[—–-]\s*(.*?))?\s*$", text, flags=re.M)
    rows, skipped = [], []
    for i in range(1, len(parts), 3):
        cid, title_hint, body = parts[i], (parts[i + 1] or "").strip(), parts[i + 2]
        body = body.split("\n## ")[0]  # don't run past the next dossier section
        f = _parse_fields(body)
        if not f.get("description"):
            skipped.append((cid, "no parseable Description"))
            continue
        if _NOT_A_CONFLICT_RE.search(f["description"]):
            skipped.append((cid, "audit note: explicitly consistent, not a conflict"))
            continue
        pair = _try_pair(f["description"])
        if pair is None:
            skipped.append((cid, "no unambiguous two-side source<->value pairing"))
            continue
        title = title_hint or f["description"][:90]
        ak = [k.strip() for k in f.get("affected_knowledge", "").split(",") if k.strip()]
        rows.append({
            "id": cid,
            "projectSlug": re.sub(r"[^a-z0-9]+", "-", project.lower()).strip("-"),
            "category": f.get("category", ""),
            "title": title,
            "description": f["description"],
            "severity": f.get("severity", ""),
            "status": f.get("status", ""),
            "versionA": pair[0],
            "versionB": pair[1],
            "resolution": f.get("resolution", ""),
            "affectedKnowledge": ak,
            "affectedPhase": f.get("affected_phase", ""),
        })
    return rows, skipped


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 tools/extract_conflicts.py <ProjectName|--all>")
    target = sys.argv[1]

    if target == "--all":
        projects = sorted(f[:-3] for f in os.listdir(ROOT / "examples" / "CaseStudies")
                          if f.endswith(".md") and f != "README.md")
    else:
        projects = [target]

    data = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    total_written = total_skipped = 0
    for project in projects:
        rows = list(CONFLICTS.get(project, []))  # hand-curated always wins
        hand_ids = {r["id"] for r in rows}
        parsed, skipped = parse_dossier_conflicts(project)
        rows += [r for r in parsed if r["id"] not in hand_ids]
        skipped = [s for s in skipped if s[0] not in hand_ids]
        skipped += [(cid, "ambiguous (hand-skip list)") for cid in SKIPPED.get(project, [])]
        if rows:
            data[project] = rows
            total_written += len(rows)
        elif project in data:
            # A stale entry (e.g. from a merge) whose conflicts no longer survive the
            # pairing rules must go -- keeping it would re-publish a dropped row forever.
            del data[project]
        total_skipped += len(skipped)
        if target != "--all" or rows:
            print(f"{project}: wrote {len(rows)} conflict(s)"
                  + (f" ({len(CONFLICTS.get(project, []))} hand-curated)" if CONFLICTS.get(project) else "")
                  + f", skipped {len(skipped)} ambiguous")
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ total: {total_written} conflicts across {sum(1 for p in projects if p in data)} project(s) -> {OUT}; "
          f"{total_skipped} skipped (ambiguous pairing)")


if __name__ == "__main__":
    main()
