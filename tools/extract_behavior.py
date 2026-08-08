#!/usr/bin/env python3
"""
extract_behavior.py — pull a structured BehaviorProfile out of a Track C (DeepSeek
methodology) dossier's Behavioral Intelligence phase, for Intelligence Workspace's
`BehaviorProfile` contract (`scryptexai/intelligence-workspace`'s `src/lib/types/project.ts`):
    { strategicObjectives: string[], decisionPatterns: string[],
      riskResponse: string[], tradeOffs: string[] }

Track C only, deliberately. Track A/B's Behavioral Intelligence phase (LayerZero) never
asked for these four groupings as distinct labeled sections — only Decision Events (see
extract_decision_events.py). Track C's Phase 9 prompt (docs/Protocol/Phased-Research-Prompts.md)
explicitly requests "Strategic Objectives", "Decision Patterns", "Risk Response Patterns",
"Strategic Trade-offs" as their own sections, and the resulting dossier (examples/CaseStudies/
Arbitrum.md) actually contains them verbatim, with item titles already labeled ("Pola N:
<title>", "Trade-off N: <title>"). This tool extracts those literal titles -- it does not
synthesize, paraphrase, or infer new statements from prose (the maintainer explicitly rejected
that approach as too error-prone, 2026-08-01). A dossier with none of these headers produces an
empty profile rather than a guessed one.

Section layout (fixed by the Phase 9 Track C prompt):
    Strategic Objectives          -- numbered list "1. <title>" -> strategicObjectives
    Decision Timeline             -- (Decision Events, handled by extract_decision_events.py)
    Evolution Pattern             -- (not part of BehaviorProfile)
    Technical Decision Pattern    -- "Pola N: <title>" -> decisionPatterns
    Financial Decision Pattern    -- "Pola N: <title>" -> decisionPatterns
    Ecosystem Decision Pattern    -- "Pola N: <title>" -> decisionPatterns
    Governance Decision Pattern   -- "Pola N: <title>" -> decisionPatterns
    Risk Response Pattern         -- "Pola N: <title>" -> riskResponse (kept separate --
                                      this is the one grouping Intelligence Workspace's
                                      contract names explicitly)
    Recurring Behavioral Pattern  -- "Pola N: <title>" -> decisionPatterns
    Strategic Trade-offs          -- "Trade-off N: <title>" -> tradeOffs

Usage:  python3 tools/extract_behavior.py examples/CaseStudies/Arbitrum.md
Output: poc/behavior.json  (merges/replaces entries for the parsed project)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "behavior.json"

# Order matters: sections are sliced between consecutive headers found in this list.
SECTION_HEADERS = [
    "Strategic Objectives", "Decision Timeline", "Evolution Pattern",
    "Technical Decision Pattern", "Financial Decision Pattern",
    "Ecosystem Decision Pattern", "Governance Decision Pattern",
    "Risk Response Pattern", "Recurring Behavioral Pattern", "Strategic Trade-offs",
]
DECISION_PATTERN_SECTIONS = {
    "Technical Decision Pattern", "Financial Decision Pattern",
    "Ecosystem Decision Pattern", "Governance Decision Pattern",
    "Recurring Behavioral Pattern",
}

_header_alt = "|".join(re.escape(h) for h in SECTION_HEADERS)

# Same markdown-tolerance fix as extract_knowledge.py's _normalise_headers -- see that module's
# docstring for the full rationale. Includes the trailing recap headers that aren't parsed as
# item sections but still have to lose their markup so they can't break the phase boundary.
_ALL_INTERNAL_HEADERS = SECTION_HEADERS + ["Behavioral Summary", "Open Threads"]
_internal_header_alt = "|".join(re.escape(h) for h in _ALL_INTERNAL_HEADERS)
_HEADER_MARKUP_RE = re.compile(
    rf"(?im)^[ \t]*(?:#{{1,6}}[ \t]*)?\*{{0,2}}({_internal_header_alt})\*{{0,2}}[ \t]*:?[ \t]*$"
)


def _normalise_headers(text):
    """Strip `## `/`### `/`**...**` decoration off this phase's internal section headers.
    The model adds it routinely despite the prompt asking for bare text; left in place it both
    hides the headers from _sections() and truncates the phase body at the boundary lookahead."""
    return _HEADER_MARKUP_RE.sub(r"\1", text)


def _project_name(text):
    m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", text, re.M)
    return m.group(1).strip() if m else None


def _slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _sections(body):
    """{header: section_text} for whichever of SECTION_HEADERS actually appear, in order."""
    matches = list(re.finditer(rf"(?:^|\n)({_header_alt})\s*\n", body))
    out = {}
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        out.setdefault(m.group(1), []).append(body[start:end])
    return {k: "\n".join(v) for k, v in out.items()}


def parse_behavior(text, project_name):
    text = _normalise_headers(text)
    # Boundary pinned to the phase that actually follows Behavioral Intelligence (Knowledge
    # Extraction), or end of file -- not a bare `\n## ` that any internal header could trip.
    m = re.search(r"^## Behavioral Intelligence\n(.*?)(?=\n## Knowledge Extraction|\Z)",
                   text, re.S | re.M)
    body = m.group(1) if m else ""
    sections = _sections(body)

    strategic_objectives = [
        re.sub(r"\s+", " ", t).strip()
        for t in re.findall(r"(?:^|\n)\d+\.\s+(.+)", sections.get("Strategic Objectives", ""))
    ]
    risk_response = [
        re.sub(r"\s+", " ", t).strip()
        for t in re.findall(r"(?:^|\n)Pola\s+\d+:\s*(.+)", sections.get("Risk Response Pattern", ""))
    ]
    decision_patterns = []
    for header in DECISION_PATTERN_SECTIONS:
        decision_patterns += [
            re.sub(r"\s+", " ", t).strip()
            for t in re.findall(r"(?:^|\n)Pola\s+\d+:\s*(.+)", sections.get(header, ""))
        ]
    trade_offs = [
        re.sub(r"\s+", " ", t).strip()
        for t in re.findall(r"(?:^|\n)Trade-off\s+\d+:\s*(.+)", sections.get("Strategic Trade-offs", ""))
    ]

    return {
        "projectSlug": _slugify(project_name),
        "strategicObjectives": strategic_objectives,
        "decisionPatterns": decision_patterns,
        "riskResponse": risk_response,
        "tradeOffs": trade_offs,
    }


def extract_from_dossier(path):
    text = path.read_text(encoding="utf-8")
    project_name = _project_name(text) or path.stem
    return project_name, parse_behavior(text, project_name)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/extract_behavior.py <dossier.md> [more.md ...]")
    OUT.parent.mkdir(exist_ok=True)
    existing = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[extract_behavior] skip (not found): {arg}", file=sys.stderr)
            continue
        project_name, profile = extract_from_dossier(path)
        total = (len(profile["strategicObjectives"]) + len(profile["decisionPatterns"])
                 + len(profile["riskResponse"]) + len(profile["tradeOffs"]))
        if total == 0:
            print(f"[extract_behavior] {project_name}: 0 items (not a Track C dossier? skipped)",
                  file=sys.stderr)
            continue
        existing[project_name] = profile
        print(f"[extract_behavior] {project_name}: {len(profile['strategicObjectives'])} objectives, "
              f"{len(profile['decisionPatterns'])} patterns, {len(profile['riskResponse'])} risk "
              f"responses, {len(profile['tradeOffs'])} trade-offs")
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
