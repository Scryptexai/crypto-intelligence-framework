# tools/ — Ingest support tooling

Deterministic helpers for the **Ingest-Deep** runbook (`docs/Protocol/Role-Ingest-Deep.md`).
No LLM, no API, no network. **Quality-preserving:** these scripts never write a dossier — the
knowledge synthesis (source → causal dossier) stays human/LLM reasoning. They only industrialise
the two mechanical steps around it: **extraction** and **audit**.

This directory is infrastructure, not a layer of the knowledge model — it does not hold project
data (`examples/`, `tracking/`), documentation (`docs/`), or raw sources (`doc_backup/`).

## `extract.py` — source → clean markdown (runbook step 1)

```
python tools/extract.py doc_backup/deep/<Project>_<YYYY-MM>_gemini.docx -o /tmp/<project>.md
python tools/extract.py <report>.pdf -o /tmp/<project>.md      # pypdf; needs `cffi` for some PDFs
```

- `.docx`: walks the body in document order; **reconstructs Word tables row-by-row**
  (`<w:tbl>/<w:tr>/<w:tc>` → `Label: Value` bullets) so no cell is scrambled. A flat text sweep
  loses column↔row association — this is the bug it avoids for legacy (pre-contract) sources.
- `.pdf`: `pypdf.extract_text()`, wrapped lines rejoined.
- Both: strips citation chips, normalises numbered section titles to `## N Title`.

New sources authored under the **Input Formatting Contract** (`docs/Protocol/Deep-Research-Brief.md`)
carry no tables at all, so extraction is trivially lossless — the table logic is for older docs.

## `reconcile.py` — fidelity audit stamp (run after writing the dossier)

```
python tools/reconcile.py doc_backup/deep/<Project>_<YYYY-MM>_gemini.md examples/CaseStudies/<Project>.md
```

Reports which **key figures** (currency, %, unit-suffixed magnitudes, large integers) in the source
are not represented in the finished dossier. **Unit-aware** (`juta`=1e6, `miliar/mrd`=1e9, …) and
matches on normalised numeric value within tolerance, so `$145 juta` ↔ `145,000,000` and a faithful
rounding (`$72,248,571 → $72,25 juta`) both count as covered.

It is a **heuristic for human review**, not a correctness proof: it flags candidates to double-check
and **cannot** verify a value is attached to the correct label — that judgement stays with the curator.
A clean report is the per-ingest fidelity evidence retained for the later dataset audit.
