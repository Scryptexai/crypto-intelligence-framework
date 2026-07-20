#!/usr/bin/env python3
"""
reconcile.py — fidelity audit: are the source's key figures represented in the dossier?

Run AFTER writing a deep dossier. Diffs the extracted source (from extract.py, or the
archived doc_backup/deep/<Project>_*.md) against the finished dossier and reports which
KEY FIGURES (currency, percentages, unit-suffixed magnitudes, large integers) are not
represented. A clean report is the per-ingest fidelity proof kept for later audit.

This is a HEURISTIC for human review, not a correctness proof:
  - Unit-aware: "juta"=1e6, "miliar/mrd"=1e9, "jt"=1e6, "ribu/rb"=1e3, K/M/B/T — so a
    figure written "$145 juta" in the dossier matches "145,000,000" in the source
    (this is why a naive digit compare over-reports).
  - Matches on normalised numeric value within a small relative tolerance, so a faithful
    rounding ($72,248,571 -> $72,25 juta) counts as covered, not missing.
  - It cannot judge whether a value is attached to the RIGHT label — that stays human.

Usage:
    python tools/reconcile.py SOURCE.md DOSSIER.md
Exit code 0 always (report-only); read the printed COVERAGE / POSSIBLY MISSING lines.
"""
import argparse
import re
import sys

UNIT = {
    "triliun": 1e12, "trillion": 1e12, "t": 1e12,
    "miliar": 1e9, "milyar": 1e9, "mrd": 1e9, "billion": 1e9, "b": 1e9,
    "juta": 1e6, "jt": 1e6, "million": 1e6, "mn": 1e6, "m": 1e6,
    "ribu": 1e3, "rb": 1e3, "thousand": 1e3, "k": 1e3,
}
UNIT_RE = "|".join(sorted(UNIT, key=len, reverse=True))

# A figure: optional $, a number (US or Indonesian separators), optional magnitude unit.
FIG_RE = re.compile(
    r"(?P<cur>\$|Rp|USD\s?)?\s*(?P<num>\d[\d.,]*\d|\d)\s*(?P<unit>%s)?\b" % UNIT_RE,
    re.IGNORECASE,
)


GROUPED = re.compile(r"^\d{1,3}([.,]\d{3})+$")  # pure thousands grouping: 3.170.000 / 1,205,128


def to_number(numstr: str, unit: str | None) -> float | None:
    s = numstr.strip()
    if "," in s and "." in s:
        # both present -> last separator is the decimal point, the other groups thousands
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif GROUPED.match(s):
        s = s.replace(".", "").replace(",", "")  # thousands grouping (incl. "10.000", "519.700")
    else:
        # single separator, not clean grouping -> treat as decimal
        s = s.replace(",", ".")
    try:
        v = float(s)
    except ValueError:
        return None
    if unit:
        v *= UNIT.get(unit.lower(), 1)
    return v


def preprocess(text: str) -> str:
    """Drop URLs and everything from the bibliography onward (reference IDs are not data)."""
    text = re.sub(r"https?://\S+", " ", text)
    cut = re.search(r"(?im)^#{0,3}\s*\d{0,2}\s*(Karya yang dikutip|Sources)\b", text)
    return text[: cut.start()] if cut else text


def numbers(text: str, want_percent: bool) -> set:
    """Normalised numeric values in text. Percent values are tagged (v, '%')."""
    vals = set()
    # percentages
    for m in re.finditer(r"(\d[\d.,]*)\s*%", text):
        v = to_number(m.group(1), None)
        if v is not None:
            vals.add(round(v, 2))
    if want_percent:
        return vals
    for m in FIG_RE.finditer(text):
        num, unit, cur = m.group("num"), m.group("unit"), m.group("cur")
        v = to_number(num, unit)
        if v is None:
            continue
        # keep only "significant" figures: has $, a unit, or magnitude >= 1000
        if cur or unit or v >= 1000:
            vals.add(v)
    return vals


def covered(target: float, pool: set, rel_tol: float = 0.01) -> bool:
    for v in pool:
        if target == 0:
            if v == 0:
                return True
            continue
        if abs(v - target) / abs(target) <= rel_tol:
            return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser(description="Audit: source key figures represented in dossier?")
    ap.add_argument("source")
    ap.add_argument("dossier")
    ap.add_argument("--tol", type=float, default=0.01, help="relative tolerance (default 0.01 = 1%%)")
    args = ap.parse_args()

    src = preprocess(open(args.source).read())
    dos = preprocess(open(args.dossier).read())

    report_lines = []
    total_missing = 0
    for label, want_pct in (("figures", False), ("percentages", True)):
        s_vals = numbers(src, want_pct)
        d_vals = numbers(dos, want_pct)
        missing = sorted(v for v in s_vals if not covered(v, d_vals, args.tol))
        total_missing += len(missing)
        cov = 100.0 * (len(s_vals) - len(missing)) / len(s_vals) if s_vals else 100.0
        report_lines.append(f"{label:12s}: {len(s_vals):4d} in source | coverage {cov:5.1f}% | {len(missing)} possibly missing")
        for v in missing:
            shown = f"{v:.2f}%" if want_pct else (f"{v:,.0f}" if v >= 1 else f"{v}")
            report_lines.append(f"    MISSING: {shown}")

    print(f"=== reconcile: {args.source}  vs  {args.dossier} ===")
    print("\n".join(report_lines))
    print(f"--- {total_missing} figure(s) flagged for human review "
          f"(rounding / format / genuinely dropped — verify each) ---")


if __name__ == "__main__":
    main()
