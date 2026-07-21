#!/usr/bin/env python3
"""
backtest.py — CIF reasoning backtest harness (deterministic, no LLM/API).

Runs each case spec in examples/Benchmarks/cases/*.md through the SAME pattern-matching the PoC uses,
then scores whether the framework surfaced the patterns the real outcome demands.

- validation cases : out-of-sample real events (e.g. Renzo depeg). The real proof.
- consistency cases: in-sample sanity (pattern classifies its own domain correctly).
- control cases    : must fire NOTHING (guards against over-firing).

Reads patterns from examples/PatternRegistry.md (via build_json.parse_patterns).
Writes a scorecard to stdout and poc/benchmarks.json.

Run from repo root:  python3 tools/backtest.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_json  # reuse parse_patterns()

CASES_DIR = ROOT / "examples" / "Benchmarks" / "cases"
OUT = ROOT / "poc"

def parse_case(text):
    head = re.search(r"^#\s*(Backtest\s*\d+.*)$", text, re.M)
    fields = {}
    for line in text.splitlines():
        m = re.match(r"-\s*([a-zA-Z]+):\s*(.*)", line.strip())
        if m:
            fields[m.group(1).lower()] = m.group(2).strip()
    clist = lambda v: [x.strip() for x in v.split(",") if x.strip()] if v else []
    return {
        "title": head.group(1).strip() if head else "Untitled",
        "type": fields.get("type", "validation"),
        "category": fields.get("category", ""),
        "given": clist(fields.get("given", "")),
        "expect": clist(fields.get("expect", "")),
        "outcome": fields.get("outcome", ""),
        "source": fields.get("source", ""),
    }

def fire(patterns, given):
    g = set(given)
    return [p["id"] for p in patterns if set(p.get("triggers", [])) & g]

def score(case, fired):
    exp = set(case["expect"])
    fired_s = set(fired)
    if case["type"] == "control" or not exp:
        # control: PASS iff nothing fired
        return ("PASS" if not fired_s else "FALSE-FIRE"), 1.0 if not fired_s else 0.0, []
    hit = exp & fired_s
    recall = len(hit) / len(exp)
    if hit == exp:
        v = "PASS"
    elif hit:
        v = "PARTIAL"
    else:
        v = "FAIL"
    return v, recall, sorted(exp - fired_s)

def main():
    patterns = build_json.parse_patterns()
    files = sorted(CASES_DIR.glob("*.md"))
    if not files:
        sys.exit("no cases in examples/Benchmarks/cases/")
    results = []
    for f in files:
        c = parse_case(f.read_text(encoding="utf-8"))
        fired = fire(patterns, c["given"])
        verdict, recall, missed = score(c, fired)
        results.append({**c, "fired": fired, "verdict": verdict, "recall": round(recall, 2),
                        "missed": missed, "file": f"examples/Benchmarks/cases/{f.name}"})

    # scorecard
    W = 46
    print("\nCIF Backtest Harness — scorecard")
    print("=" * 72)
    for r in results:
        icon = {"PASS": "✅", "PARTIAL": "🟡", "FAIL": "❌", "FALSE-FIRE": "⚠️"}[r["verdict"]]
        print(f"{icon} {r['verdict']:10s} [{r['type']:11s}] {r['title'][:W]}")
        print(f"     given : {', '.join(r['given']) or '—'}")
        print(f"     fired : {', '.join(r['fired']) or '—'}   expect: {', '.join(r['expect']) or '(none)'}")
        if r["missed"]:
            print(f"     missed: {', '.join(r['missed'])}")
    print("=" * 72)
    scored = [r for r in results if r["type"] != "control"]
    passed = sum(1 for r in results if r["verdict"] == "PASS")
    avg_recall = round(sum(r["recall"] for r in scored) / len(scored), 2) if scored else 0
    print(f"PASS {passed}/{len(results)} · avg recall (non-control) {avg_recall} · "
          f"validation cases {sum(1 for r in results if r['type']=='validation')}")

    OUT.mkdir(exist_ok=True)
    (OUT / "benchmarks.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    # non-zero exit if any real (non-control) case fails outright — useful as a check
    if any(r["verdict"] == "FAIL" or r["verdict"] == "FALSE-FIRE" for r in results):
        sys.exit(1)

if __name__ == "__main__":
    main()
