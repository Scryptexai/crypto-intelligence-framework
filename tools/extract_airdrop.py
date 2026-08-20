#!/usr/bin/env python3
"""
extract_airdrop.py — pull a structured AirdropProfile out of a dossier's Phase 12 section.

    { status, events[], povOutcomes{}, priceTrajectory{}, retention[], gaps[], prospect{},
      lessons[] }

Reads only what Phase 12 literally wrote. It does not infer whether an airdrop "worked", does
not compute a success score, and does not compare projects -- all three are judgements the
prompt deliberately makes per-POV and per-era, and collapsing them into one number here would
throw away the distinction the phase exists to preserve (see reset/phase_12_airdrop.txt).

Section layout (fixed by the Phase 12 prompt):
    STATUS AIRDROP           -- one of four literal states -> status
    AIRDROP EVENTS           -- "AD-NNN: <title>" blocks with labelled fields -> events
    CONTEXT SAAT KEPUTUSAN   -- prose (kept as context)
    TRIGGER DAN ALTERNATIF   -- prose
    REASON                   -- stated vs unstated (kept whole; the split matters and is
                                deliberately not parsed into a claim)
    OUTCOME PER POV          -- "POV <Name>: <verdict>" + short/long term -> povOutcomes
    HARGA PASCA-DISTRIBUSI   -- four fixed price lines -> priceTrajectory
    METRIK RETENSI           -- labelled metric lines -> retention
    GAP YANG DIKETAHUI       -- what the sources do not contain -> gaps
    FARMING DAN SYBIL        -- prose
    PROSPEK                  -- labelled lines -> prospect
    PELAJARAN LINTAS PROJECT -> lessons
    OPEN THREADS             -- handled by ingest.py, not here

A project with no Phase 12 parses to nothing and is skipped, exactly like Track A/B dossiers
in the other extractors.

Usage:  python3 tools/extract_airdrop.py examples/CaseStudies/Arbitrum.md [more.md ...]
Output: poc/airdrop.json  (merges/replaces entries for the parsed project)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "airdrop.json"

SECTION_HEADERS = [
    "STATUS AIRDROP", "AIRDROP EVENTS", "CONTEXT SAAT KEPUTUSAN", "TRIGGER DAN ALTERNATIF",
    "REASON — YANG DINYATAKAN VS YANG TIDAK", "OUTCOME PER POV", "HARGA PASCA-DISTRIBUSI",
    "METRIK RETENSI", "GAP YANG DIKETAHUI", "FARMING DAN SYBIL", "PROSPEK",
    "PELAJARAN LINTAS PROJECT",
]
_header_alt = "|".join(re.escape(h) for h in SECTION_HEADERS)

POV_NAMES = ["Founder", "VC", "Retail", "Community", "Developer", "Institution",
             "Validator", "Builder"]
_pov_alt = "|".join(POV_NAMES)

VALID_STATUS = ["Sudah dilakukan", "Sedang berjalan", "Diumumkan belum eksekusi", "Belum ada"]

# The five verdicts the prompt asks for, and the phrasings reports actually used for them.
# Across 27 projects the model produced eight distinct strings for five meanings -- "Tidak
# relevan", "Tidak berlaku", "Tidak diterapkan" and "Tidak berkaitan" all mean the same thing,
# and "Gagal / Tidak relevan" packs two into one cell. Free text is fine in a report and
# useless in a column: a product cannot filter or count on it.
#
# Normalised here rather than in the prompt because both are needed and only one is reliable.
# The prompt keeps asking for the canonical five (a model that complies costs nothing extra);
# this mapping catches the ones that drift, and `verdictRaw` keeps the model's own words so a
# reader loses nothing -- "Tidak relevan (Blur bukan chain)" says more than the enum does.
_VERDICT_CANON = [
    ("sukses", "Sukses"),
    ("sebagian", "Sebagian"),
    ("gagal", "Gagal"),
    ("tidak diketahui", "Tidak diketahui"),
    ("tidak relevan", "Tidak relevan"),
    ("tidak berlaku", "Tidak relevan"),
    ("tidak diterapkan", "Tidak relevan"),
    ("tidak berkaitan", "Tidak relevan"),
    ("tidak ada", "Tidak relevan"),
]


def normalise_verdict(raw):
    """One of the five canonical verdicts, or None when nothing recognisable is present.

    First match wins on a lowercased substring test, and the list is ordered so a compound
    answer resolves to its more specific half: "Gagal / Tidak relevan" is a real outcome for
    the POV plus an aside, so it reads as Gagal.
    """
    if not raw:
        return None
    low = raw.lower()
    for needle, canon in _VERDICT_CANON:
        if needle in low:
            return canon
    return None

# Same markdown tolerance as extract_knowledge/_behavior: the model decorates headers with
# `##`/`**` despite being told not to, and undecorated matching is what keeps a cosmetic slip
# from hiding a whole section.
_HEADER_MARKUP_RE = re.compile(
    rf"(?im)^[ \t]*(?:#{{1,6}}[ \t]*)?\*{{0,2}}({_header_alt}|OPEN THREADS)\*{{0,2}}[ \t]*:?[ \t]*$")


def _normalise_headers(text):
    return _HEADER_MARKUP_RE.sub(r"\1", text)


def _project_name(text):
    m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", text, re.M)
    return m.group(1).strip() if m else None


def _slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _sections(body):
    """{header: text} for whichever of SECTION_HEADERS appear. Repeated headers are joined,
    not overwritten -- the same setdefault/append fix extract_knowledge needed after a
    recap header silently dropped 33 of 39 items.

    OPEN THREADS is a boundary but never a section. It is the last thing Phase 12 writes and
    is also bullet-shaped, so without it here the final real section (PELAJARAN LINTAS
    PROJECT) runs to end-of-body and swallows every open question as if it were a lesson --
    caught on the first synthetic test, which reported 3 lessons for a phase that had 2.
    tools/ingest.py lifts Open Threads into its own dossier section, so this only bites the
    spec-check path that reads a raw phase file, which is exactly where a repair loop would
    then be chasing a defect that isn't in the model's output.
    """
    matches = list(re.finditer(rf"(?:^|\n)({_header_alt}|OPEN THREADS)\s*\n", body))
    out = {}
    for i, m in enumerate(matches):
        header = m.group(1)
        if header == "OPEN THREADS":
            continue
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        out.setdefault(header, []).append(body[start:end])
    return {k: "\n".join(v) for k, v in out.items()}


def _field(block, label):
    """One `Label: value` line out of an AD-NNN block."""
    m = re.search(rf"(?im)^\s*{re.escape(label)}\s*:\s*(.+?)\s*$", block)
    return m.group(1).strip() if m else None


def _parse_events(section):
    events = []
    blocks = list(re.finditer(r"(?m)^\s*(AD-\d{3})\s*:\s*(.+?)\s*$", section))
    for i, m in enumerate(blocks):
        start = m.end()
        end = blocks[i + 1].start() if i + 1 < len(blocks) else len(section)
        block = section[start:end]
        events.append({
            "id": m.group(1),
            "title": m.group(2).strip(),
            "date": _field(block, "Tanggal"),
            "type": _field(block, "Tipe"),
            "allocation": _field(block, "Alokasi"),
            "recipients": _field(block, "Penerima"),
            "valueAtClaim": _field(block, "Nilai saat klaim"),
            "criteria": _field(block, "Kriteria"),
            "antiSybil": _field(block, "Anti-sybil"),
            "relatedEvent": _field(block, "Terkait EV"),
            "citation": _field(block, "Sitasi"),
        })
    return events


def _parse_pov(section):
    """{"founder": {"verdict", "qualifier", "shortTerm", "longTerm", "basis"}} per POV present.

    The heading may carry a parenthetical naming WHICH holders of that viewpoint are meant --
    "POV VC (Paradigm, Variant Fund)", "POV Retail (Season 1 claimers)". The first real Phase
    12 (Blur, 2026-08-10) did this on five of eight, and an earlier version of this regex
    demanded a colon straight after the name, so those five parsed as absent and the phase
    was reported broken. The qualifier is better output than the bare name, not worse, so it
    is captured rather than tolerated.
    """
    out = {}
    blocks = list(re.finditer(
        rf"(?m)^\s*POV\s+({_pov_alt})\s*(?:\(([^)]*)\))?\s*:\s*(.+?)\s*$", section))
    for i, m in enumerate(blocks):
        start = m.end()
        end = blocks[i + 1].start() if i + 1 < len(blocks) else len(section)
        block = section[start:end]

        def bullet(label):
            b = re.search(rf"(?im)^\s*[-·*]?\s*{label}\s*:\s*(.+?)\s*$", block)
            return b.group(1).strip() if b else None

        raw_verdict = m.group(3).strip()
        out[m.group(1).lower()] = {
            "verdict": normalise_verdict(raw_verdict),
            "verdictRaw": raw_verdict,
            "qualifier": (m.group(2) or "").strip() or None,
            "shortTerm": bullet("Jangka pendek"),
            "longTerm": bullet("Jangka panjang"),
            "basis": bullet("Dasar"),
        }
    return out


# The four price lines, in the order the prompt asks for them, mapped to the key each becomes,
# plus the pattern that recognises the label on the page. Each label is anchored to the start
# of its line, so one cannot shadow another.
#
# The patterns tolerate cosmetic drift the prompt does not ask for: an inserted "token", a
# parenthetical date after the label, "hari ke-30" for "+30 hari". Ethena wrote `Harga token
# pada klaim (TGE 2024-04-02): ~$0.50-$0.60` -- the right datum under a reworded label, which
# the strict form read as a missing line and sent into two regenerations. The label is
# cosmetic; the figure is the contract. The prompt keeps asking for the exact form (a model
# that complies costs nothing), and this catches the ones that drift -- the same split that
# already works for verdict/verdictRaw and for markdown-decorated headers.
PRICE_POINTS = [
    ("atClaim", "Harga saat klaim", r"Harga(?:\s+token)?\s+(?:saat|pada)\s+klaim"),
    ("day30", "Harga +30 hari", r"Harga(?:\s+token)?\s*(?:\+\s*30\s*hari|hari\s*ke-?\s*30)"),
    ("day90", "Harga +90 hari", r"Harga(?:\s+token)?\s*(?:\+\s*90\s*hari|hari\s*ke-?\s*90)"),
    ("peak12m", "Harga puncak 12 bulan pertama",
     r"Harga(?:\s+token)?\s+(?:puncak|tertinggi)(?:\s+12\s+bulan\s+pertama)?"),
]

_EVIDENCE_RE = re.compile(r"\((HIGH|MEDIUM|LOW)\)", re.I)
_DATE_RE = re.compile(r"\((\d{4}-\d{2}-\d{2})\)")
_SOURCE_RE = re.compile(r"\[([^\]]+)\]")
# A figure only counts when it is presented as money -- `1,20 USD`, `USD 1,20` or `$1,20`.
# A bare number in the same sentence is prose, not a price: "Tidak berlaku — belum genap 12
# bulan" parsed as $12.00 on the first round-trip test, which is exactly the kind of number
# that looks precise and is wrong (and would then be charted).
_AMOUNT_RE = re.compile(r"(?i)(?:(\d[\d.,]*)\s*USD\b|USD\s*(\d[\d.,]*)|\$\s*(\d[\d.,]*))")


def _parse_amount(head):
    """Best-effort USD figure out of the text before the first bracket. None when absent.

    Reports mix conventions in the same file -- the prompt is Indonesian, so `1,20` means one
    dollar twenty, but sources are quoted verbatim and CoinGecko writes `1.20`. Rather than
    pick one and silently mis-scale the other by 100, the last separator is classified by what
    follows it, which is convention-independent: a grouping mark is always followed by exactly
    three digits, so anything else is a decimal point. Exactly three digits is the one real tie
    (`1.200` the thousand vs `0.001` the sub-cent) and is read as grouping unless the integer
    part is a bare zero, which no thousands separator can produce.

    `raw` is always kept, so a figure this heuristic gets wrong is still visible to a reader
    and recoverable by a later re-parse.
    """
    m = _AMOUNT_RE.search(head)
    if not m:
        return None
    tok = next(g for g in m.groups() if g).rstrip(".,")
    seps = [i for i, ch in enumerate(tok) if ch in ".,"]
    if not seps:
        digits, frac = tok, ""
    else:
        last = seps[-1]
        after = len(tok) - last - 1
        repeated = len(seps) > 1 and tok[seps[-1]] == tok[seps[-2]]
        int_part = re.sub(r"[.,]", "", tok[:last])
        is_decimal = not repeated and (after != 3 or int_part == "0")
        if is_decimal:
            digits, frac = tok[:last], tok[last + 1:]
        else:
            digits, frac = tok, ""
    digits = re.sub(r"[.,]", "", digits)
    if not digits:
        return None
    try:
        return float(f"{digits}.{frac}" if frac else digits)
    except ValueError:
        return None


def _parse_price(section):
    """{key: {usd, date, source, evidence, raw}} for whichever of the four lines are present.

    This block is the answer to the question the retention section could never answer. Cohort
    sell-through ("% who sold within 7 days") was asked of 13 projects and found zero times --
    it needs per-address on-chain work that nobody publishes. Price at claim vs +90 days is in
    CoinGecko for almost every listed token and says the same thing: a recipient who held
    either gained or lost, and the number shows which.

    A missing line is absent from the dict rather than present-and-null, so a caller can tell
    "the model didn't write it" from "the model wrote Tidak berlaku" -- the second is a finding
    (no listing, or continuous distribution with no claim date) and the first is a defect.
    """
    out = {}
    for key, _label, pattern in PRICE_POINTS:
        m = re.search(rf"(?im)^\s*[-·*]?\s*{pattern}[^:\n]*:\s*(.+?)\s*$", section or "")
        if not m:
            continue
        raw = m.group(1).strip()
        head = re.split(r"[\[(]", raw, 1)[0]
        ev = _EVIDENCE_RE.search(raw)
        date = _DATE_RE.search(raw)
        src = _SOURCE_RE.search(raw)
        out[key] = {
            "usd": _parse_amount(head),
            "date": date.group(1) if date else None,
            "source": src.group(1).strip() if src else None,
            "evidence": ev.group(1).upper() if ev else None,
            "raw": raw,
        }
    return out


def _parse_lines(section):
    """Bullet or dash lines, cleaned -- used for retention metrics and lessons."""
    return [re.sub(r"\s+", " ", ln).strip(" -·*")
            for ln in re.findall(r"(?m)^\s*[-·*]\s*(.+?)\s*$", section or "")
            if ln.strip()]


def _parse_plain_lines(section):
    """Every non-empty line, bullet or not -- used for GAP YANG DIKETAHUI.

    The prompt asks for that section as one unadorned sentence ("Cohort penerima: ..."), so
    the bullet-only reader used elsewhere returns nothing for a section that is present and
    correct. A known gap that parses as absent is worse than useless: it reads as the model
    having skipped the section.
    """
    return [re.sub(r"\s+", " ", ln).strip(" -·*")
            for ln in (section or "").splitlines()
            if ln.strip(" -·*\t")]


def parse_airdrop(text, project_name):
    text = _normalise_headers(text)
    m = re.search(r"^## Airdrop Intelligence\n(.*?)(?=\n## |\Z)", text, re.S | re.M)
    body = m.group(1) if m else ""
    if not body.strip():
        return None
    sections = _sections(body)

    status_raw = (sections.get("STATUS AIRDROP") or "").strip()
    status = next((s for s in VALID_STATUS if s.lower() in status_raw.lower()), None)

    events = _parse_events(sections.get("AIRDROP EVENTS", ""))
    pov = _parse_pov(sections.get("OUTCOME PER POV", ""))

    prospect_sec = sections.get("PROSPEK", "")
    prospect = {
        "met": _field(prospect_sec, "Prasyarat yang sudah terpenuhi"),
        "unmet": _field(prospect_sec, "Prasyarat yang belum"),
        "signals": _field(prospect_sec, "Sinyal yang biasanya mendahului"),
        "assessment": _field(prospect_sec, "Penilaian"),
    }

    if not (status or events or pov):
        return None

    return {
        "projectSlug": _slugify(project_name),
        "status": status,
        "events": events,
        "povOutcomes": pov,
        "priceTrajectory": _parse_price(sections.get("HARGA PASCA-DISTRIBUSI", "")),
        "retention": _parse_lines(sections.get("METRIK RETENSI", "")),
        "gaps": _parse_plain_lines(sections.get("GAP YANG DIKETAHUI", "")),
        "prospect": prospect,
        "lessons": _parse_lines(sections.get("PELAJARAN LINTAS PROJECT", "")),
    }


def extract_from_dossier(path):
    text = path.read_text(encoding="utf-8")
    project_name = _project_name(text) or path.stem
    return project_name, parse_airdrop(text, project_name)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/extract_airdrop.py <dossier.md> [more.md ...]")
    OUT.parent.mkdir(exist_ok=True)
    existing = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[extract_airdrop] skip (not found): {arg}", file=sys.stderr)
            continue
        project_name, profile = extract_from_dossier(path)
        if profile is None:
            print(f"[extract_airdrop] {project_name}: no Phase 12 section (skipped)",
                  file=sys.stderr)
            continue
        existing[project_name] = profile
        print(f"[extract_airdrop] {project_name}: status={profile['status']!r}, "
              f"{len(profile['events'])} event(s), {len(profile['povOutcomes'])} POV, "
              f"{len(profile['priceTrajectory'])}/4 price point(s), "
              f"{len(profile['retention'])} retention metric(s)")
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
