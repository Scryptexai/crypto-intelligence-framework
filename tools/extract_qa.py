#!/usr/bin/env python3
"""
extract_qa.py — pull a structured QAReport out of a Track C (DeepSeek methodology)
dossier's Validation & Quality Assurance phase, for Intelligence Workspace's `QAReport`
contract (`scryptexai/intelligence-workspace`'s `src/lib/types/project.ts`):
    { total: number, dimensions: QADimension[], phases: QAPhase[] }

Track C only, deliberately -- same reasoning as extract_behavior.py. Track A/B's Conflict
Resolution phase (LayerZero) never produced a numeric, weighted six-dimension score; Track
C's Phase 11 prompt (docs/Protocol/Phased-Research-Prompts.md) explicitly does, in a
"CIF SCORE CALCULATION — v3.0" section with one consistent, parseable line per dimension:
    Kontribusi: <score> × <weight-as-fraction> = <contribution>

That section is used, NOT the earlier "CIF MANIFEST v3.0 / QUALITY SCORES" block that
appears near the top of the same phase — the two can genuinely disagree (verified on
Arbitrum.md: Manifest says 88.2/100, the detailed calculation says 81.6/100). This was
flagged as a real Track C authoring inconsistency earlier in this project's history (see
docs/Protocol/Phased-Research-Prompts.md's "Known gaps" section, "CIF Score ordering" item)
and the detailed calculation is the one the fix designated authoritative -- it shows its
work, the Manifest doesn't.

`phases` (QAPhase: {name, status, score, owner}) comes from the same section's "COVERAGE
REPORT — Multi-dimensional" table (one block per upstream phase, with a real Coverage %).
`status` and `owner` have no dossier source at all -- Track C never tags a phase as
Passed/Blocked/etc. or assigns an owner -- so both are set to fixed system defaults
("Passed" given the Manifest's own "Complete Phases: N dari N" claim, "CIF" as the
pipeline's own label) rather than guessed per-phase. `score` is the real Coverage %
number, not fabricated.

Usage:  python3 tools/extract_qa.py examples/CaseStudies/Arbitrum.md
Output: poc/qa.json  (merges/replaces entries for the parsed project)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poc" / "qa.json"

DIMENSION_KEYS = {
    "Research Quality": "research",
    "Consistency": "consistency",
    "Evidence": "evidence",
    "Coverage": "coverage",
    "Conflict": "conflict",
    "Knowledge": "knowledge",
}
_dim_alt = "|".join(re.escape(d) for d in DIMENSION_KEYS)

# Accepts BOTH shapes the dimension heading comes back in:
#
#   Research Quality (25%)     <- what Arbitrum's run produced, and all this used to accept
#   Research Quality:          <- what reset/phase_11_conflict.txt's template literally asks for
#
# Those two disagreeing is a real contract split, not model sloppiness: the prompt lists the
# weights once in a "Dimensi dan Bobot" block and then writes each dimension heading as a bare
# "Research Quality:", while this regex was written against Arbitrum's output, where the model
# had merged the weight into the heading. A model that follows the template exactly therefore
# parsed to zero dimensions and its whole CIF Score vanished with no error -- Aave, 2026-08-09,
# a complete 30,707-char audit that reached neither poc/qa.json nor Supabase.
#
# The weight is recovered from the Kontribusi multiplier when the heading omits it, so both
# shapes yield identical rows. Anchored to a whole line and capped at 600 chars of detail so a
# passing mention of "Coverage" in prose cannot open a block and swallow the next dimension.
DIM_BLOCK_RE = re.compile(
    rf"^({_dim_alt})[ \t]*(?:\((\d+)%\))?[ \t]*:?[ \t]*$\n"
    rf"(.{{0,600}}?)Kontribusi:\s*([\d.]+)\s*[×x]\s*([\d.]+)\s*=\s*([\d.]+)",
    re.S | re.M,
)


def _project_name(text):
    m = re.search(r"^#\s+(.+?)(?:\s+—|\s+-\s|$)", text, re.M)
    return m.group(1).strip() if m else None


def _slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _phase_blocks(coverage_body):
    """'Phase N — Category\n· Total: ...\n· Coverage: X%\n...' -> [(name, coverage_pct), ...]"""
    phases = []
    for m in re.finditer(r"(?:^|\n)(Phase \d+\s*—\s*[^\n]+)\n(.*?)(?=\nPhase \d+\s*—|\nOverall Coverage|\Z)",
                          coverage_body, re.S):
        name = m.group(1).strip()
        cov_m = re.search(r"Coverage:\s*(\d+)%", m.group(2))
        if cov_m:
            phases.append((name, int(cov_m.group(1))))
    return phases


def parse_qa(text, project_name):
    m = re.search(r"^## Validation & Quality Assurance.*?\n(.*?)(?=\n## |\Z)", text, re.S | re.M)
    body = m.group(1) if m else ""
    if not body:
        return None

    # Keyed by dimension, LAST occurrence wins. A report often states the six dimensions
    # twice -- once as a summary table, once as the worked calculation -- and appending both
    # gave EOS twelve qa_dimensions rows for six real dimensions, i.e. a product table saying
    # something untrue about the data. Last wins for the same reason the total does below:
    # the detailed calculation always comes after the summary.
    by_key = {}
    for dim_m in DIM_BLOCK_RE.finditer(body):
        label, weight_pct, detail, score, weight_frac, _contribution = dim_m.groups()
        # "Kontribusi: <score> × <weight fraction> = <contribution>" carries both numbers, so
        # the weight is available even when the heading is the bare "Research Quality:" form
        # that omits "(25%)". Rounded because the prompt writes 0.25/0.20/0.15/0.10.
        weight = int(weight_pct) if weight_pct else round(float(weight_frac) * 100)
        by_key[DIMENSION_KEYS[label]] = {
            "key": DIMENSION_KEYS[label],
            "label": label,
            "score": float(score),
            "weight": weight,
            "description": re.sub(r"\s+", " ", detail).strip(" ·\n"),
        }
    # Emit in DIMENSION_KEYS order rather than encounter order, so two projects' rows line up.
    dimensions = [by_key[k] for k in DIMENSION_KEYS.values() if k in by_key]
    if not dimensions:
        return None

    # Two "CIF SCORE: N/100" lines can appear (the early Manifest summary, then the detailed
    # calculation) and can genuinely disagree -- see module docstring. The detailed
    # calculation always comes last in the phase, so the LAST match is the authoritative one.
    # Case-insensitive: the prompt never dictates the casing, so reports write "CIF SCORE:",
    # "CIF Score:" and "Cif Score:" interchangeably. Uppercase-only matched Arbitrum -- the one
    # hand-run report the regex was written from -- and returned None for Notcoin, which had
    # the identical line in title case.
    total_matches = re.findall(r"(?i)CIF SCORE:\s*([\d.]+)\s*/\s*100", body)
    total = float(total_matches[-1]) if total_matches else None

    # Same casing problem, and it was the more expensive one: 22 of 28 projects wrote
    # "Coverage Report" in title case and so contributed zero qa_phases rows -- a coverage
    # table that was empty for four fifths of the dataset while reporting no error.
    cov_m = re.search(r"(?i)COVERAGE REPORT.*?\n(.*?)(?=\n(?i:CONFLICT REGISTER|CROSS-PHASE)|\Z)",
                      body, re.S)
    phases = []
    if cov_m:
        for name, coverage_pct in _phase_blocks(cov_m.group(1)):
            phases.append({"name": name, "status": "Passed", "score": coverage_pct, "owner": "CIF"})

    return {
        "projectSlug": _slugify(project_name),
        "total": total,
        "dimensions": dimensions,
        "phases": phases,
    }


def extract_from_dossier(path):
    text = path.read_text(encoding="utf-8")
    project_name = _project_name(text) or path.stem
    return project_name, parse_qa(text, project_name)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 tools/extract_qa.py <dossier.md> [more.md ...]")
    OUT.parent.mkdir(exist_ok=True)
    existing = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[extract_qa] skip (not found): {arg}", file=sys.stderr)
            continue
        project_name, report = extract_from_dossier(path)
        if report is None:
            print(f"[extract_qa] {project_name}: no CIF Score Calculation found (not a "
                  f"Track C dossier? skipped)", file=sys.stderr)
            continue
        existing[project_name] = report
        print(f"[extract_qa] {project_name}: total={report['total']}, "
              f"{len(report['dimensions'])} dimensions, {len(report['phases'])} phases")
    OUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
