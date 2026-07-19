# Role: Ingest-Deep

**Goal:** turn ONE deep research report (a long-form monograph like the Ethereum report) into ONE
**deep case study** — the highest-quality, causal artifact that prediction reasons from.

**Throughput:** ~1 project per session. **Output location:** `examples/CaseStudies/<Project>.md`.

## When to use
The maintainer provides a deep, multi-section report on a single project (history, founders, tokenomics,
governance crises, price causality, competitor landscape, etc.). This is an *anchor* project.

## Steps

1. **Archive the source first.** Save the raw doc to `doc_backup/deep/<Project>_<YYYY-MM>_gemini.pdf` and a
   reflowed text version `.md` alongside it (see `doc_backup/README.md`). This is step 1, always.
2. **Extract the source.** If it is a PDF, extract and reflow the text to readable paragraphs first.
3. **Check the index.** If the project exists as a Summary elsewhere, this Deep dossier supersedes it —
   keep both but mark the Summary as "see deep case study" (do not silently delete).
4. **Write the dossier** at `examples/CaseStudies/<Project>.md` using the deep structure below. Map every
   section to the `docs/` ontology and link back to it.
5. **Extract patterns & lessons** — the causal takeaways (e.g. "complex multi-token → later simplified";
   "technical success can cause tokenomic harm"). These feed `docs/Patterns/` and `docs/Reasoning/`.
6. **Register** in `examples/DatasetIndex.md` with tier = Deep, and point its `Source` to the `doc_backup/` file.
7. **Provenance:** record the source (Deep Research / Gemini) and include the report's own citations.
8. **Commit & push.**

## Deep dossier structure (map to ontology)

Deep reports arrive in the **22-section structure** defined in `docs/Protocol/Deep-Research-Brief.md`.
The dossier mirrors those sections so ingestion is lossless. Mapping:

| Dossier section (from the 22-section brief) | Maps to |
|---------|---------|
| Identity, Classification | `docs/Ontology/Identity.md`, `docs/Taxonomy/*` |
| §2 Industry Background (pre-conditions) | context (why it existed) |
| §3 Origin, Team & genealogy | `docs/Ontology/Team.md`, `docs/Ontology/Governance.md` |
| §4 Innovation Analysis (+ archetype: FirstMover/FastFollower/Fork/Improvement) | `docs/Innovation/*` |
| §5,§10 Technology & Product Evolution | `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*` |
| §6 Funding Intelligence | `docs/Ontology/Funding.md` |
| §7 Community Intelligence | `docs/Ontology/Community.md`, `docs/Success/Community.md` |
| §8 Narrative Intelligence | `docs/Meta/Narratives.md` |
| §9 Competitive Landscape | `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md` |
| §11,§12 Tokenomics & Airdrop/Incentive | `docs/Ontology/Tokenomics.md`, `Incentives.md`, `docs/Patterns/Points,Mining,Referral` |
| §13 Token Lifecycle + price causality | `docs/TokenLifecycle/*`, `docs/MarketBehaviour/*`, `docs/Valuation/*` |
| §14 Business Intelligence | `docs/Ontology/Revenue.md`, `Adoption.md`, `Metrics.md` |
| Governance crises & resolutions | `docs/Ontology/Governance.md`, `Risks.md`, `Security.md`, `docs/Patterns/Failure.md`, `Recovery.md` |
| §16 Timeline · §17 Current Status | timeline + latest snapshot (`docs/Ontology/*`) |
| **§15 POV Success-Matrix** (8 POV, each with evidence level) | `docs/Success/*` |
| §18,§19 Lessons & Knowledge Extraction *(crown jewel)* | `docs/Patterns/*`, `docs/Ontology/*`, `docs/Schema/*` |
| **§20 Transferable Intelligence** *(crown jewel)* — rule candidates | `docs/Reasoning/*` |
| **§21 Open Questions** | research-gap field |
| **§22 Evidence Level** (HIGH/MED/LOW per key claim) | `docs/Reasoning/Confidence.md` |
| Related framework definitions + Sources | cross-links + provenance |

### Mandatory fields (do not skip)
- **POV Success-Matrix** — success/failure across all 8 POVs (Founder, VC, Retail, Community, Developer,
  Institution, Validator, Builder), each with a one-line reason and an evidence level. Never collapse to a
  single "success/fail" verdict.
- **Evidence Level** — tag important conclusions HIGH / MEDIUM / LOW with the reason.
- **Open Questions** — list what is still unvalidated.
- **§19 Knowledge Extraction + §20 Transferable Intelligence** — these are the highest-value sections; they
  are what the reasoning engine consumes. Always populate them explicitly.

## Quality bar
- Preserve **causality** ("X happened *because* Y"), not just facts — that is the point of a deep dossier.
- Keep numbers and dates faithful to the source; never round away or invent figures.
- Reusable Knowledge: each key fact should carry its *why / impact / lesson / industry link*.
