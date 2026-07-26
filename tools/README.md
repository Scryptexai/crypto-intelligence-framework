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

## `ingest.py` — batch auto-file raw docx/pdf → CIF artifacts (no LLM)

Deterministic; the reasoning already lives in the source report, this only transforms+files it.
Four inbox-routed types (`deep`, `batch`, `sentiment`, `phased`) plus the hardened `data_project`
pipeline below. See the file's own docstring and `--help` for the routing rules.

### `data_project/<project>/` — hardened per-project 11-phase assembler

The successor to the `phased` mode's `doc_backup/inbox/phased/<Project>/` convention, built after a
real incident: a phase file named `03-historical.docx` was silently dropped from a dossier assembly
because the old matcher tested phase keys as a loose substring of the filename, and `"history"` is
not a substring of `"historical"` (see `doc_backup/inbox/phased/LayerZero/PROMPTS-LOG.md`). The failure
was silent — the run still reported `✅ ok`, just with one phase missing from the dossier.

`data_project` replaces substring matching with a **strict, hard-failing contract**:

```
data_project/<project>/NN-<phasekey>.docx   e.g. data_project/layerzero/03-history.docx
```

- `NN` — any 1–2 digit ordinal (cosmetic; assembly order is always the fixed dependency order, not
  filename order).
- `<phasekey>` — must be an **exact** match (not substring) to one of the 11 keys: `foundation`,
  `entity`, `history`, `technology`, `financial`, `token`, `ecosystem`, `market`, `behavioral`,
  `knowledge`, `conflict`.
- Any filename that doesn't match the pattern, uses an unknown key, or collides with another file on
  the same key → the whole project **raises and writes nothing** (no partial/misleading dossier).
  A missing phase also raises unless `--allow-partial` is passed explicitly.

**Content-level verification** (`validate_phase_content()`), on top of the filename contract — a
correct filename proves nothing about whether the *content* is real, complete, or belongs to this
project. Runs on every file before anything is written or archived:
- content shorter than 400 chars → broken/empty extraction.
- no `PROJECT: <Name>` header, or the header names a different project than the folder → likely
  misfiled/wrong-project content.
- zero `(HIGH)`/`(MEDIUM)`/`(LOW)`/`(TIDAK ADA KONFLIK)` Evidence Level tags anywhere → the exact
  "empty citations" failure mode that took 2–3 rejected drafts each to catch by hand in LayerZero
  Phase 3/4/6 before this check existed.
- the `[sumber tidak dapat diverifikasi ulang]` fallback phrase used as often or more than real
  Evidence Level tags → blanket fallback overuse instead of genuine per-fact citation (Phase 3
  attempt-2's failure mode).
- two files in the same project with identical extracted content (whitespace-normalised hash) →
  likely the same file saved under two phase names by mistake.

Any failure → **raises and writes nothing** for that file's project, listing every file and every
reason found (not just the first). Override with `--allow-unverified` if a human has reviewed the
flagged file and it's a false positive — not recommended as a default habit.

```
python tools/ingest.py --type data_project --input data_project/layerzero
python tools/ingest.py                                   # also scans data_project/ by default
python tools/ingest.py --type data_project --allow-partial --input data_project/arbitrum
python tools/ingest.py --type data_project --allow-unverified --input data_project/arbitrum
```

The process exits non-zero if any `data_project` folder fails validation, so it's safe to gate on in
a script — **`run.sh` already does this correctly**: a failed project is logged and skipped (nothing
written for it), `build_json.py`/`backtest.py` still run against whatever *did* ingest successfully,
and only `run.sh`'s own final exit code carries the failure signal (don't let a shell wrapper's
`set -e` swallow that distinction and abort the whole pipeline on one bad project — see `run.sh`'s
`run_ingest()`). The older `phased` mode (fuzzy matching, soft warnings, no content verification)
still works unchanged for LayerZero's own folder (`doc_backup/inbox/phased/LayerZero/`, which happens
to already satisfy the `data_project` filename contract too — verified by running it through
`process_data_project()` directly). New projects should use `data_project/<project>/`.
