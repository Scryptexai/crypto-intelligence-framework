#!/usr/bin/env python3
"""
extract_events.py — pull structured timeline Events out of a Track C (DeepSeek
methodology) dossier's Historical Intelligence phase, for Intelligence Workspace's
`TimelineEvent` contract (`scryptexai/intelligence-workspace`'s `src/lib/types/event.ts`).

Track C only. That phase's real shape (verified against examples/CaseStudies/Arbitrum.md,
which is the only dossier in this dataset that carries it -- LayerZero is Track A/B and has
no `EV-\\d+` event list at all) is one field per line per event block, separated by a "---"
rule:

    Event ID / <EV-NNN>
    Date / <date>
    Event Name / <name>
    Event Type / <type>
    Description / <description>
    Participants / <name; name; ...>
    Location / <location>
    Status / <status>
    Immediate Result / <result>
    Sources / <url>\\n<url>\\n...

Fields never fabricated:
  - `type` is kept as the dossier's own literal "Event Type" value (Research, Founding,
    Funding, Launch, Technology, Governance, Security, Legal, Integration, Market, Token,
    Organization, Community, Other, ...) rather than force-mapped onto Intelligence
    Workspace's narrower fixed enum -- several literal values here (Research, Organization,
    Community, Other) have no confident match in that enum, and guessing one would be
    exactly the invented-precision the maintainer has repeatedly ruled out elsewhere in
    this tools/ directory (see extract_entities.py, extract_knowledge.py). The events
    table's `type` column is plain text with no DB-level enum constraint, so this is safe.
  - `source`/`url` -- the dossier lists 1-N raw citation URLs per event with no named
    outlet, so `source` is set to the fixed provenance label "CIF Research Dossier" (same
    convention as evidence_rows() in tools/sync_supabase.py) and `url` is the first listed
    Sources URL (if any).
  - `impact` (High/Medium/Low) -- not tagged per-event anywhere in this phase; left unset
    so the `events` table's own column default ("Medium") applies rather than guessing.
  - `affectedKnowledge` -- resolving which K-### items an event affects would mean
    name/topic matching prose across phases, which is inference, not extraction; stays
    an empty array (same reasoning as extract_knowledge.py's `relatedKnowledge`).

Usage:  python3 tools/extract_events.py examples/CaseStudies/Arbitrum.md
Output: poc/events.json  (merges/replaces entries for the parsed project)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "events.json"

BLOCK_RE = re.compile(
    r"Event ID\n\n(?P<id>EV-\d+)\n\n"
    r"Date\n\n(?P<date>.+?)\n\n"
    r"Event Name\n\n(?P<name>.+?)\n\n"
    r"Event Type\n\n(?P<type>.+?)\n\n"
    r"Description\n\n(?P<description>.+?)\n\n"
    r"Participants\n\n(?P<participants>.+?)\n\n"
    r"Location\n\n(?P<location>.+?)\n\n"
    r"Status\n\n(?P<status>.+?)\n\n"
    r"Immediate Result\n\n(?P<result>.+?)\n\n"
    r"Sources\n\n(?P<sources>.+?)\n\n---",
    re.S,
)


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def extract_project_name(text: str) -> str:
    m = re.search(r"^PROJECT:\s*(.+)$", text, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s*(.+?)\s*—", text, re.M)
    return m.group(1).strip() if m else ""


def parse_events(text: str, project_slug: str) -> list[dict]:
    hist_match = re.search(r"^## Historical Intelligence\n(.*?)(?=\n^## )", text, re.S | re.M)
    if not hist_match:
        return []
    section = hist_match.group(1)
    # BLOCK_RE's trailing "---" is the delimiter *before* the next block; append one
    # sentinel "---" so the final event in the section (which has no following block) matches.
    rows = []
    for m in BLOCK_RE.finditer(section + "\n\n---"):
        sources = [s.strip() for s in m.group("sources").strip().splitlines() if s.strip()]
        participants = [p.strip() for p in m.group("participants").split(";") if p.strip()]
        rows.append({
            "id": m.group("id"),
            "projectSlug": project_slug,
            "name": m.group("name").strip(),
            "date": m.group("date").strip(),
            "type": m.group("type").strip(),
            "participants": participants,
            "description": m.group("description").strip(),
            "result": m.group("result").strip(),
            "source": "CIF Research Dossier",
            "url": sources[0] if sources else None,
            "affectedKnowledge": [],
            "_location": m.group("location").strip(),
            "_status": m.group("status").strip(),
        })
    return rows


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 tools/extract_events.py <path-to-dossier.md>")
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    project_name = extract_project_name(text)
    if not project_name:
        sys.exit("could not find project name (PROJECT: <Name> header)")
    slug = slugify(project_name)

    events = parse_events(text, slug)
    if not events:
        sys.exit(f"no Historical Intelligence EV-### blocks found in {path} "
                  f"(Track A/B dossiers don't carry this format)")

    data = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    data[project_name] = events
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ extracted {len(events)} event(s) for {project_name} -> {OUT}")


if __name__ == "__main__":
    main()
