# data_project/

## Purpose

Input folder for the **Format v3 phased pipeline**, hardened convention (Task 2, 2026-07-26). This is where
a project's 11 raw phase `.docx` files go before `./run.sh` assembles them into a Deep Dossier.

## Why This Folder Exists

`tools/ingest.py`'s `data_project` mode was built after a real incident: the older
`doc_backup/inbox/phased/<Project>/` convention's fuzzy filename matching silently dropped a phase file
whose name didn't exactly match its phase key (`03-historical.docx` was not recognized as the `history`
phase). This folder's naming contract is strict and machine-checked instead — see below.

## Folder Structure

```
data_project/
└── <project>/                    # lowercase, e.g. data_project/arbitrum/
    ├── 01-foundation.docx
    ├── 02-entity.docx
    ├── 03-history.docx
    ├── 04-technology.docx
    ├── 05-financial.docx
    ├── 06-token.docx
    ├── 07-ecosystem.docx
    ├── 08-market.docx
    ├── 09-behavioral.docx
    ├── 10-knowledge.docx
    └── 11-conflict.docx
```

**Naming contract (exact, not fuzzy):** `NN-<phasekey>.docx` (or `.pdf`) — `NN` is any 1–2 digit ordinal
(cosmetic; assembly order is always the fixed dependency order, not filename order), `<phasekey>` must be an
**exact** match to one of: `foundation`, `entity`, `history`, `technology`, `financial`, `token`, `ecosystem`,
`market`, `behavioral`, `knowledge`, `conflict`. Any filename that doesn't match, an unknown key, two files
mapping to the same key, or a missing phase → the whole project **hard-fails and writes nothing** (no
partial/misleading dossier) — see `tools/ingest.py`'s `process_data_project()` and `tools/README.md`.

Beyond the filename contract, each file's **content** is also verified before anything is written:
near-empty extraction, a `PROJECT:` header that doesn't match the folder name, zero Evidence Level tags
anywhere, citation-fallback overuse, and duplicate content across files in the same project all hard-fail —
see `validate_phase_content()` in `tools/ingest.py`.

## Source of Truth

Raw phase research output (Gemini / Claude-direct / another model), per
`docs/Protocol/Phased-Research-Prompts.md`. Currently empty — LayerZero (the first and only project through
this pipeline so far) still lives at `doc_backup/inbox/phased/LayerZero/`, which happens to already satisfy
this folder's naming contract (verified: `tools/ingest.py --type data_project --input
doc_backup/inbox/phased/LayerZero` passes cleanly) but has not been physically moved here — its
`PROMPTS-LOG.md` and supporting research files are heavily cross-referenced by path throughout
`examples/DatasetIndex.md`, so moving it was judged not worth the churn. **Every new project going forward
should be dropped directly into `data_project/<project>/`, not the older `doc_backup/inbox/phased/`
location.**

## Input

11 raw phase `.docx`/`.pdf` files per project, produced by running the Track A prompts in
`docs/Protocol/Phased-Research-Prompts.md` one phase at a time.

## Output

`examples/CaseStudies/<Project>.md` (the assembled Deep Dossier), via `./run.sh` or
`python tools/ingest.py --type data_project --input data_project/<project>`. Raw sources are archived
individually to `doc_backup/deep/<Project>_<phase>_<YYYY-MM>.docx`.

## Workflow Position

Part of the `Applications` layer of `Research → Knowledge → Ontology → Patterns → Reasoning → Framework →
Applications` — this folder is the raw-input side of `Ingest-Deep` (`docs/Protocol/Role-Ingest-Deep.md`),
analogous to `doc_backup/inbox/` for the older single-prompt formats.

## Rules

1. Exact filename contract — see above. No near-misses, no fuzzy matching.
2. One project per subfolder, lowercase name.
3. Content must pass `validate_phase_content()` — real citations, correct `PROJECT:` header, no
   near-empty phases.
4. `--allow-partial` / `--allow-unverified` exist for genuine edge cases (see `tools/README.md`) but are not
   a default habit — a hard-fail is telling you something is actually wrong.

## Related Files

`tools/ingest.py` (`process_data_project`, `validate_phase_content`, `detect_phase_key_strict`),
`tools/README.md` (full usage), `docs/Protocol/Phased-Research-Prompts.md` (the prompts that produce these
files, including step 3b's per-phase "what to attach" table and step 5's naming rule),
`docs/Protocol/Deep-Research-Brief.md` ("Format v3 — Dependency Pipeline"), `examples/DatasetIndex.md`
§ "Phased Deep Research Queue".
