#!/usr/bin/env python3
"""
extract_decision_events.py — pull structured Decision Events out of a Format v3
dossier's Behavioral Intelligence phase (+ any "Decision Event:" addenda logged
under Open Questions, which is where a later phase sometimes appends more
events discovered after Phase 9 ran — see LayerZero.md's Open Questions section).

Decision Event is the actual unit of analysis for this framework (CLAUDE.md:
"the unit of analysis is not the Project — it is the Decision Event"), but
until now nothing extracted it into structured data — it only existed as prose
in the dossier. This is deterministic text parsing (no LLM), matching the
project's existing tools/build_json.py convention: read markdown, emit JSON.

Two Phase 9 prompt shapes are recognized (docs/Protocol/Phased-Research-Prompts.md
Track A/B vs. Track C), because they capture genuinely different things, not just
a reformatting of the same fields — output events carry both shapes' fields, null
where the source prompt never asked for that field (never fabricated to fill it):

  Track A/B "Decision Event: <date> — <title>" blocks
    -> Motivation/Constraint/Pressure/Trade-off/Alternative(s) Considered/
       Expectation vs. Actual/8-POV Stakeholder Reactions/Grounding

  Track C "Keputusan: <title> (<year>)" blocks (DeepSeek methodology)
    -> Trigger/Evidence/Decision/Immediate Result/Long-term Impact/Supporting
       Dataset. Track C's Decision Timeline was never designed to capture
       per-stakeholder reactions the way Track A/B's was, so `reactions` stays
       an empty dict for these events rather than guessing at one.

Usage:  python3 tools/extract_decision_events.py examples/CaseStudies/LayerZero.md
Output: poc/decision_events.json  (merges/replaces entries for the parsed project)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "decision_events.json"

FIELD_LABELS = [
    "Motivation", "Constraint", "Pressure", "Trade-off",
    "Alternative(s) Considered", "Expectation vs. Actual",
    "Stakeholder Reactions",
    "Founder", "VC", "Retail", "Community", "Developer", "Institution", "Validator", "Builder",
    "Grounding", "Open Threads",
]
POV_LABELS = ["Founder", "VC", "Retail", "Community", "Developer", "Institution", "Validator", "Builder"]

KEPUTUSAN_LABELS = ["Trigger", "Evidence", "Decision", "Immediate Result", "Long-term Impact",
                     "Supporting Dataset"]

_label_alt = "|".join(re.escape(l) for l in FIELD_LABELS)
_keputusan_label_alt = "|".join(re.escape(l) for l in KEPUTUSAN_LABELS)

# Every event dict carries the full union of both shapes' keys, so downstream consumers
# (tools/sync_supabase.py, AirdropOS) see one stable schema regardless of which track produced
# a given event -- unpopulated keys are None/{}, never guessed at.
EMPTY_EVENT_FIELDS = {
    "motivation": None, "constraint": None, "pressure": None, "tradeoff": None,
    "alternatives": None, "expectation_vs_actual": None, "reactions": {}, "grounding": None,
    "trigger": None, "evidence": None, "decision": None, "immediate_result": None,
    "long_term_impact": None, "supporting_dataset": None,
}


def _project_name(text):
    m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", text, re.M)
    return m.group(1).strip() if m else None


def _extract_field(block, label, all_labels_alt, bullet=False):
    """bullet=True additionally tolerates a leading '· ' marker before the label (Track C's
    Decision Timeline fields are written as bullets, Track A/B's are not)."""
    prefix = r"·?\s*" if bullet else ""
    pattern = re.compile(
        rf"(?:^|\n)\s*{prefix}{re.escape(label)}:\s*(.*?)(?=\n\s*{prefix}(?:{all_labels_alt}):|\Z)",
        re.S,
    )
    m = pattern.search(block)
    return m.group(1).strip() if m else None


def parse_events(text, project_name):
    """text: the sub-range of a dossier containing 'Decision Event: ...' blocks
    (Behavioral Intelligence phase body, optionally concatenated with any
    Open-Questions addendum). Bullet-list dossiers prefix every line with
    '- [behavioral] ' — stripped here so both formats parse identically."""
    cleaned = re.sub(r"^- \[behavioral\]\s*", "", text, flags=re.M)
    chunks = re.split(r"(?:^|\n)Decision Event:\s*", cleaned)[1:]
    events = []
    for chunk in chunks:
        head, _, rest = chunk.partition("\n")
        head = head.strip()
        m = re.match(r"(.+?)\s*—\s*(.+)", head)
        date, title = (m.group(1).strip(), m.group(2).strip()) if m else (head, "")
        fields = {}
        for label in FIELD_LABELS:
            val = _extract_field(rest, label, _label_alt)
            if val:
                fields[label] = re.sub(r"\s+", " ", val).strip()
        reactions = {pov: fields.pop(pov) for pov in POV_LABELS if pov in fields}
        events.append({
            "project": project_name,
            "date": date,
            "title": title,
            **EMPTY_EVENT_FIELDS,
            "motivation": fields.get("Motivation"),
            "constraint": fields.get("Constraint"),
            "pressure": fields.get("Pressure"),
            "tradeoff": fields.get("Trade-off"),
            "alternatives": fields.get("Alternative(s) Considered"),
            "expectation_vs_actual": fields.get("Expectation vs. Actual"),
            "reactions": reactions,
            "grounding": fields.get("Grounding"),
            "open_threads": fields.get("Open Threads"),
        })
    return events


def parse_keputusan_events(text, project_name):
    """Track C shape: 'Keputusan: <title> (<year>)' blocks under Phase 9's Decision Timeline
    (docs/Protocol/Phased-Research-Prompts.md, DeepSeek methodology), fields written as
    '· Label: value' bullets instead of Track A/B's bare 'Label: value' lines."""
    chunks = re.split(r"(?:^|\n)Keputusan:\s*", text)[1:]
    events = []
    for chunk in chunks:
        head, _, rest = chunk.partition("\n")
        head = head.strip()
        # Trailing parenthetical is the date/period -- "(2018)", "(2024-2025)", but also seen with a
        # month name, "(April 2026)" -- accept any parenthetical content rather than digits-only, since
        # sort_key() below just needs *a* 4-digit year somewhere in the string, not a strict format.
        m = re.match(r"(.+?)\s*\(([^()]+)\)\s*$", head)
        title, date = (m.group(1).strip(), m.group(2).strip()) if m else (head, None)
        fields = {}
        for label in KEPUTUSAN_LABELS:
            val = _extract_field(rest, label, _keputusan_label_alt, bullet=True)
            if val:
                fields[label] = re.sub(r"\s+", " ", val).strip()
        events.append({
            "project": project_name,
            "date": date,
            "title": title,
            **EMPTY_EVENT_FIELDS,
            "trigger": fields.get("Trigger"),
            "evidence": fields.get("Evidence"),
            "decision": fields.get("Decision"),
            "immediate_result": fields.get("Immediate Result"),
            "long_term_impact": fields.get("Long-term Impact"),
            "supporting_dataset": fields.get("Supporting Dataset"),
            "open_threads": None,
        })
    return events


def extract_from_dossier(path):
    text = path.read_text(encoding="utf-8")
    project_name = _project_name(text) or path.stem

    m = re.search(r"^## Behavioral Intelligence\n(.*?)(?=\n## )", text, re.S | re.M)
    behavioral_body = m.group(1) if m else ""

    m2 = re.search(r"^## Open Questions\n(.*?)(?=\n## |\Z)", text, re.S | re.M)
    open_questions_body = m2.group(1) if m2 else ""
    addendum_lines = []
    for ln in open_questions_body.splitlines():
        s = ln.strip()
        if not s.startswith("- [behavioral]"):
            continue
        # A bare "- [behavioral] Open Threads" (no colon) is a whole-dossier
        # recap heading, not a per-event field — it comes after the last real
        # event and its own bullet list has no "Label:" shape at all, so
        # without this cutoff the last event's `open_threads` field would
        # swallow that entire trailing recap (seen with LayerZero.md).
        if s[len("- [behavioral]"):].strip() == "Open Threads":
            break
        addendum_lines.append(ln)
    addendum = "\n".join(addendum_lines)

    events = (parse_events(behavioral_body, project_name) + parse_events(addendum, project_name)
              + parse_keputusan_events(behavioral_body, project_name)
              + parse_keputusan_events(addendum, project_name))

    def sort_key(e):
        m = re.search(r"(\d{4})", e["date"] or "")
        return (int(m.group(1)) if m else 0, e["date"] or "")
    events.sort(key=sort_key)
    return project_name, events


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/extract_decision_events.py <dossier.md> [more.md ...]")
    OUT.parent.mkdir(exist_ok=True)
    existing = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[extract_decision_events] skip (not found): {arg}", file=sys.stderr)
            continue
        project_name, events = extract_from_dossier(path)
        existing[project_name] = events
        print(f"[extract_decision_events] {project_name}: {len(events)} decision event(s)")
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
