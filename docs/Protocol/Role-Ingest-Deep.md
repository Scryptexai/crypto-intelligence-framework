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
| §2 Industry Background (pre-conditions) | **`docs/Ontology/Context.md`** snapshot (industry/competitor/macro state as of the events discussed) |
| §3 Origin, Team & genealogy | `docs/Ontology/Team.md`, `docs/Ontology/Governance.md` |
| §4 Innovation Analysis (+ archetype: FirstMover/FastFollower/Fork/Improvement) | `docs/Innovation/*` |
| §5,§10 Technology & Product Evolution | `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*` |
| §6 Funding Intelligence | `docs/Ontology/Funding.md` (Observable) + `docs/Ontology/Hidden.md` if strategic rationale is stated |
| §7 Community Intelligence | `docs/Ontology/Community.md`, `docs/Success/Community.md` |
| §8 Narrative Intelligence | `docs/Meta/Narratives.md` → feeds `docs/Ontology/Context.md` |
| §9 Competitive Landscape | `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md` → feeds `docs/Ontology/Context.md` |
| §11,§12 Tokenomics & Airdrop/Incentive | `docs/Ontology/Tokenomics.md`, `Incentives.md`, `docs/Patterns/Points,Mining,Referral` |
| §13 Token Lifecycle + price causality | `docs/TokenLifecycle/*`, `docs/MarketBehaviour/*`, `docs/Valuation/*` |
| §14 Business Intelligence | `docs/Ontology/Revenue.md`, `Adoption.md`, `Metrics.md` |
| Governance crises & resolutions | `docs/Ontology/Governance.md`, `Risks.md`, `Security.md`, `docs/Patterns/Failure.md`, `Recovery.md` — **write each major crisis/turning point as a `docs/Ontology/DecisionEvent.md` instance** |
| §16 Timeline · §17 Current Status | timeline — **extract each major turning point as a `DecisionEvent`** + latest snapshot (`docs/Ontology/*`) |
| **§15 POV Success-Matrix** (8 POV, each with evidence level) | `docs/Success/*` — doubles as the Stakeholder Reactions field of any `DecisionEvent` |
| §18,§19 Lessons & Knowledge Extraction *(crown jewel)* | `docs/Patterns/*`, `docs/Ontology/*`, `docs/Schema/*`, **`docs/Ontology/DecisionEvent.md`** |
| **§20 Transferable Intelligence** *(crown jewel)* — rule candidates | `docs/Reasoning/*` — state the **Context range** (`scope`) each rule holds under |
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
- **Decision Events** — identify the project's major turning points (a pivot, a crisis response, a launch
  design choice) as explicit `docs/Ontology/DecisionEvent.md` instances: Context → Trigger → Decision →
  Alternatives → Reason/Evidence → Execution → Stakeholder Reactions (8 POV) → Short/Long-term Outcome. This
  is the unit patterns are actually discovered from — a project is many Decision Events, not one story.
- **Context per Decision Event** — record the industry/competitor/tech/macro/hunter-population/VC-climate
  state *at that time* (`docs/Ontology/Context.md`). Never let a decision's outcome be compared to another
  project's without also comparing their Context — this is what prevents blind era-mismatched analogies.
- **Observable vs Hidden** — record measurable facts (`docs/Ontology/Metrics.md` etc.) separately from
  non-measurable explanatory factors (`docs/Ontology/Hidden.md`: motivation, constraint, trade-off). Ground
  Hidden factors in the source or mark `unknown` — never invent them.
- **Preserve conflicting evidence.** Do not let the dossier pre-conclude "why it succeeded" — keep competing
  explanations and minority accounts where the source has them; synthesis is `docs/Reasoning/`'s job.

## Quality bar
- Preserve **causality** ("X happened *because* Y"), not just facts — that is the point of a deep dossier.
- Keep numbers and dates faithful to the source; never round away or invent figures.
- Reusable Knowledge: each key fact should carry its *why / impact / lesson / industry link*.
