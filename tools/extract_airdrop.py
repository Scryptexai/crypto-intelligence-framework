#!/usr/bin/env python3
"""
extract_airdrop.py — pull a structured AirdropProfile out of a dossier's Phase 12 section.

    { status, events[], povOutcomes{}, retention[], prospect{}, lessons[] }

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
    METRIK RETENSI           -- labelled metric lines -> retention
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
    "REASON — YANG DINYATAKAN VS YANG TIDAK", "OUTCOME PER POV", "METRIK RETENSI",
    "FARMING DAN SYBIL", "PROSPEK", "PELAJARAN LINTAS PROJECT",
]
_header_alt = "|".join(re.escape(h) for h in SECTION_HEADERS)

POV_NAMES = ["Founder", "VC", "Retail", "Community", "Developer", "Institution",
             "Validator", "Builder"]
_pov_alt = "|".join(POV_NAMES)

VALID_STATUS = ["Sudah dilakukan", "Sedang berjalan", "Diumumkan belum eksekusi", "Belum ada"]

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
    """{"founder": {"verdict", "shortTerm", "longTerm", "basis"}} for whichever POVs appear."""
    out = {}
    blocks = list(re.finditer(rf"(?m)^\s*POV\s+({_pov_alt})\s*:\s*(.+?)\s*$", section))
    for i, m in enumerate(blocks):
        start = m.end()
        end = blocks[i + 1].start() if i + 1 < len(blocks) else len(section)
        block = section[start:end]

        def bullet(label):
            b = re.search(rf"(?im)^\s*[-·*]?\s*{label}\s*:\s*(.+?)\s*$", block)
            return b.group(1).strip() if b else None

        out[m.group(1).lower()] = {
            "verdict": m.group(2).strip(),
            "shortTerm": bullet("Jangka pendek"),
            "longTerm": bullet("Jangka panjang"),
            "basis": bullet("Dasar"),
        }
    return out


def _parse_lines(section):
    """Bullet or dash lines, cleaned -- used for retention metrics and lessons."""
    return [re.sub(r"\s+", " ", ln).strip(" -·*")
            for ln in re.findall(r"(?m)^\s*[-·*]\s*(.+?)\s*$", section or "")
            if ln.strip()]


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
        "retention": _parse_lines(sections.get("METRIK RETENSI", "")),
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
              f"{len(profile['retention'])} retention metric(s)")
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
