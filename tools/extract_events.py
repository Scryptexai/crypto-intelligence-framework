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
    """The assembled dossier's H1 title first, the phase file's own 'PROJECT:' header second.

    That order matters and used to be reversed. `projects.slug` -- which `events.project_slug`
    has a foreign key to -- is derived from the dossier title (ingest.py writes it from the
    data_project/<Folder> name), while the PROJECT: header carries whatever the model wrote,
    which is often a longer trade name: "Kamino" vs "Kamino Finance" slugged to `kamino` vs
    `kamino-finance`, and the whole events sync died on a FK violation. Every sibling extractor
    already keys off the H1, so this simply stops events.py being the odd one out. The
    PROJECT: fallback is still needed for the raw single-phase files that verify_10_phases
    feeds in, which have no H1 at all."""
    m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", text, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r"^PROJECT:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def parse_events(text: str, project_slug: str) -> list[dict]:
    # Boundary pinned to the phase that follows Historical Intelligence (Technology Intelligence)
    # rather than a bare `\n## `, so a markdown-formatted internal header inside Phase 3 (year
    # groupings, RINGKASAN, Open Threads) can't truncate the body and zero out every event.
    hist_match = re.search(r"^## Historical Intelligence\n(.*?)(?=\n^## Technology Intelligence|\Z)",
                            text, re.S | re.M)
    if not hist_match:
        return []
    section = hist_match.group(1)
    # BLOCK_RE's trailing "---" is the delimiter *before* the next block; append one
    # sentinel "---" so the final event in the section (which has no following block) matches.
    rows = []
    blocks = list(BLOCK_RE.finditer(section + "\n\n---"))
    if not blocks:
        return _parse_events_track_a(section, project_slug)
    for m in blocks:
        sources = [s.strip() for s in m.group("sources").strip().splitlines() if s.strip()]
        participants = [p.strip() for p in m.group("participants").split(";") if p.strip()]
        rows.append({
            # Prefixed with the project slug because Intelligence Workspace's `events` table
            # keys on a bare `id`, so it must be unique across every project ever synced --
            # not just within one dossier. The dossier's own numbering restarts at EV-001 for
            # each project, so 25 projects produced 25 rows all claiming id "EV-001" and the
            # upsert died with "ON CONFLICT DO UPDATE command cannot affect row a second time"
            # (Postgres 21000) before writing anything. Same convention extract_entities.py
            # already uses (<slug>-ENT-NNN) for exactly this reason; the original EV-NNN stays
            # readable as the id's suffix and is unchanged in the prose citations that use it.
            "id": f"{project_slug}-{m.group('id')}",
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


# Track A dossiers (e.g. LayerZero, assembled from the pre-v3 staged pipeline) carry
# chronological blocks shaped as `Date: ... / Event: ... / Trigger: ... / Decision: ... /
# Execution: ... / Short-term Outcome: ... / Long-term Outcome: ... / Evidence: ...` instead
# of Track C's EV-### blocks. Same rule as everywhere else: parse what is literally there,
# no invented fields -- absent Track C-only fields stay empty.
TA_BLOCK_START = re.compile(r"^Date:\s*(.+?)\s*$", re.M)
TA_EV_RE = re.compile(r"^Event:\s*(.+?)\s*$", re.M)
TA_URL_RE = re.compile(r"https?://[^\s\]；;]+")


def _ta_field(block: str, label: str) -> str:
    m = re.search(rf"^{re.escape(label)}:\s*(.*?)(?=\n\n[A-Z][a-z\-() ]+:|\Z)", block, re.S | re.M)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def _parse_events_track_a(section: str, project_slug: str) -> list[dict]:
    starts = [m.start() for m in TA_BLOCK_START.finditer(section)]
    rows = []
    for i, st in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(section)
        block = section[st:end]
        dm = TA_BLOCK_START.match(block)
        em = TA_EV_RE.search(block)
        if not dm or not em:
            continue
        date = dm.group(1).strip()
        name = re.sub(r"\s*\((HIGH|MEDIUM|LOW)\)\s*$", "", em.group(1)).strip()
        trigger = _ta_field(block, "Trigger")
        decision = _ta_field(block, "Decision")
        execution = _ta_field(block, "Execution")
        short_term = _ta_field(block, "Short-term Outcome")
        long_term = _ta_field(block, "Long-term Outcome")
        evidence = _ta_field(block, "Evidence")
        urls = TA_URL_RE.findall(evidence)
        desc = " | ".join(x for x in [
            f"Trigger: {trigger}" if trigger else "",
            f"Decision: {decision}" if decision else "",
            f"Execution: {execution}" if execution else "",
        ] if x)
        result = " | ".join(x for x in [
            f"Short-term: {short_term}" if short_term else "",
            f"Long-term: {long_term}" if long_term else "",
        ] if x)
        rows.append({
            "id": f"{project_slug}-TA-{i + 1:03d}",
            "projectSlug": project_slug,
            "name": name,
            "date": date,
            "type": "Historical (Track A)",
            "participants": [],
            "description": desc,
            "result": result,
            "source": "CIF Research Dossier",
            "url": urls[0] if urls else None,
            "affectedKnowledge": [],
            "_location": "",
            "_status": "",
        })
    return rows


def main():
    # Accepts N dossiers, like every sibling extractor -- a single-file-only signature meant
    # `./run.sh` could not batch this script the way it batches the others, so poc/events.json
    # silently went stale on every manual build. A dossier with no EV-### blocks (Track A/B)
    # is skipped with a note instead of aborting the whole batch.
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/extract_events.py <dossier.md> [more.md ...]")

    data = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[extract_events] skip (not found): {arg}", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        project_name = extract_project_name(text)
        if not project_name:
            print(f"[extract_events] skip ({path.name}): no 'PROJECT: <Name>' header",
                  file=sys.stderr)
            continue
        events = parse_events(text, slugify(project_name))
        if not events:
            print(f"[extract_events] {project_name}: no Historical Intelligence EV-### blocks "
                  f"(Track A/B dossier? skipped)", file=sys.stderr)
            continue
        data[project_name] = events
        print(f"✅ extracted {len(events)} event(s) for {project_name}")

    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
