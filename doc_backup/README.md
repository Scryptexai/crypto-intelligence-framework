# doc_backup

## Purpose

Archive of the **raw source documents** (Deep Research / Gemini reports, and any original research inputs)
that were ingested into the knowledge layer. This makes the repository fully self-contained: if the `docs/`
architecture is ever revised, knowledge can be **re-processed from these originals without re-running research**.

## Why This Folder Exists

`examples/` holds the *structured output*; this folder holds the *raw input* it was built from. Keeping both
means every knowledge artifact is traceable to its source, and a future re-architecture never forces a redo
of the underlying research.

## The three layers (with this folder added)

| Jenis | Folder | Isi |
|-------|--------|-----|
| **Sumber mentah** | `doc_backup/` | Doc asli dari Gemini / riset (input) |
| **Container** | `docs/` | Dokumentasi & aturan |
| **Knowledge** | `examples/`, `tracking/` | Hasil terstruktur (output) |

## Source of Truth

The original research documents exactly as received. Never edited — only added.

## Input

Deep Research (Gemini) reports and other primary research documents provided by the maintainer.

## Output

A traceable, re-processable archive. Each knowledge artifact's `Source` in `examples/DatasetIndex.md` points here.

## Folder Structure

```
doc_backup/
├── deep/     # Sources behind Deep dossiers (examples/CaseStudies/*)
│   └── <Project>_<YYYY-MM>_gemini.pdf  (+ .md text extraction)
└── batch/    # Sources behind Summary batches (examples/Pioneer/*)
    └── <Batch>_<YYYY-MM>_gemini.pdf    (+ .md text extraction)
```

## Rules

1. **Store both** the original (PDF) and a reflowed text (`.md`) version — the text is searchable, diff-able,
   and re-processable without re-extraction.
2. **Naming:** `<Project|Batch>_<YYYY-MM>_<source>.{pdf,md}` so it maps to the batch/project and date.
3. **Never edit** an archived source; it is the immutable record. Corrections happen in `examples/`.
4. Every Ingest session (Deep/Batch) saves its source here as step 1 of its runbook.
5. Web-researched batches (no source document, e.g. Batch 02) have no file here — their provenance is the
   per-file citation list instead.

## Naming Convention

`deep/` and `batch/` subfolders; files `<Project|Batch>_<YYYY-MM>_gemini.{pdf,md}`.

## Future Expansion

Larger sources may be stored as text-only to keep the repository lean; an optional manifest can index every
source with a checksum.
