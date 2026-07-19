# Role: Ingest-Deep

**Goal:** turn ONE deep research report (a long-form monograph like the Ethereum report) into ONE
**deep case study** — the highest-quality, causal artifact that prediction reasons from.

**Throughput:** ~1 project per session. **Output location:** `examples/CaseStudies/<Project>.md`.

## When to use
The maintainer provides a deep, multi-section report on a single project (history, founders, tokenomics,
governance crises, price causality, competitor landscape, etc.). This is an *anchor* project.

## Steps

1. **Extract the source.** If it is a PDF, extract and reflow the text to readable paragraphs first.
2. **Check the index.** If the project exists as a Summary elsewhere, this Deep dossier supersedes it —
   keep both but mark the Summary as "see deep case study" (do not silently delete).
3. **Write the dossier** at `examples/CaseStudies/<Project>.md` using the deep structure below. Map every
   section to the `docs/` ontology and link back to it.
4. **Extract patterns & lessons** — the causal takeaways (e.g. "complex multi-token → later simplified";
   "technical success can cause tokenomic harm"). These feed `docs/Patterns/` and `docs/Reasoning/`.
5. **Register** in `examples/DatasetIndex.md` with tier = Deep.
6. **Provenance:** record the source (Deep Research / Gemini) and include the report's own citations.
7. **Commit & push.**

## Deep dossier structure (map to ontology)

| Section | Maps to |
|---------|---------|
| Identity, Classification | `docs/Ontology/Identity.md`, `docs/Taxonomy/*` |
| Pre-conditions / founding thesis | context (why it existed) |
| Team & genealogy (founders, splits) | `docs/Ontology/Team.md`, `docs/Ontology/Governance.md` |
| Funding / TGE / genesis allocation | `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md` |
| Technology & architecture evolution | `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*` |
| Governance crises & resolutions | `docs/Ontology/Governance.md`, `Risks.md`, `Security.md`, `docs/Patterns/Failure.md`, `Recovery.md` |
| Ecosystem / adoption / TVL | `docs/Ontology/Ecosystem.md`, `Adoption.md`, `Metrics.md` |
| Competitor landscape | `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md` |
| Tokenomics & price causality | `docs/MarketBehaviour/*`, `docs/Reasoning/Prediction.md` |
| Current state | `docs/Ontology/*` (latest snapshot) |
| Success evaluation (per stakeholder) | `docs/Success/*` |
| Extracted patterns & lessons | `docs/Patterns/*`, `docs/Reasoning/*` |
| Related framework definitions + Sources | cross-links + provenance |

## Quality bar
- Preserve **causality** ("X happened *because* Y"), not just facts — that is the point of a deep dossier.
- Keep numbers and dates faithful to the source; never round away or invent figures.
