# Role: Ingest-Batch

**Goal:** turn a summary batch (a table/report covering MANY projects) into ONE profile per project —
breadth for the dataset so patterns have enough samples.

**Throughput:** ~10–15 projects per session. **Output location:** `examples/Pioneer/<Project>.md`
(or `examples/Successful/`, `examples/Failed/` when the outcome is validated).

## When to use
The maintainer provides a curation batch (like Batch 01/02) with ~1 paragraph per field per project.

## Steps

1. **Archive the source first.** Save the raw doc to `doc_backup/batch/<Batch>_<YYYY-MM>_gemini.pdf` and a
   reflowed `.md` alongside it (see `doc_backup/README.md`). (Web-only batches have no source doc — skip.)
2. **Extract the source** (PDF → reflowed text).
3. **Check the index** for each project to avoid duplicates. Skip or update existing ones.
4. **Write one profile per project** using the summary structure below. Link each field to `docs/`.
5. **Register** every project in `examples/DatasetIndex.md` with tier = Summary, pointing `Source` to the
   `doc_backup/` file (or the citations, for web-only batches).
6. **Taxonomy:** collect any new categories/chains/technologies observed and note them for
   `docs/Taxonomy/*` (terms only — never project instances).
7. **Optional:** if the batch includes a cross-project analysis, write it to `examples/CaseStudies/Batch-NN-*.md`.
8. **Provenance** per file (Deep Research / Gemini, or Web research + citations). **Commit & push.**

## Summary profile structure

```
# <Project>
<provenance header: batch, source, pipeline position>
## Identity            (name, category, era, research priority)
## Classification      (sector / category / sub-category, ref Taxonomy)
## Community & Incentive
## Innovation
## Evolution Summary
## Why Selected        (key evolutionary metric + rationale)
## Official Links
## Related Framework Definitions   (links into docs/)
## Sources             (only for web-researched batches)
```

## Quality bar
- Faithful to source; do not embellish.
- Every profile must be comparable to the others (same fields) so patterns can be computed across them.
- Prefer promoting a high-value project to a **Deep** dossier later rather than over-inflating a summary.
