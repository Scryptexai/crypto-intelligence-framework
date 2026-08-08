# Enterprise Roadmap — triage and sequencing

## Status

**Direction document, not a schedule.** Written 2026-08-08 after the maintainer proposed turning CIF from an
analysis dashboard into an enterprise-grade intelligence platform, with a module list modelled on Palantir
Foundry, Bloomberg Terminal, Chainalysis and Elliptic.

This file triages that list. It does **not** commit to building anything, and it does not override
`ApplicationBlueprint.md` — that stays the source of truth for positioning, trust architecture and
monetization. Where the proposal collided with locked rules, the rules were re-examined rather than assumed
correct; two of the three collisions turned out to be my own misreading, and the blueprint's §7 was amended
accordingly (see its Status entry for 2026-08-08).

## Ownership split (maintainer decision, 2026-08-08)

The same enterprise proposal was given to the frontend team. The work is divided:

| Lane | Owner | Covers |
|---|---|---|
| **Data integration** | this repo | Research pipeline and dataset scale, extraction contracts, entity/relationship data, Observable connectors, Supabase schema + sync, the data shape every surface reads |
| **Frontend + backend integration** | frontend team | Product surfaces, lineage/graph UI, memo rendering, auth/RBAC/SSO, white-label, API serving layer |

Everything below is tagged **[data]** or **[frontend]** so neither side plans into the other's lane. Where a
module needs both, the handoff is named explicitly — those are the rows most likely to stall, because each
side can look complete while the seam between them is not.

The practical consequence for this repo: a surface being unbuilt is **not** this lane's problem, but a
surface being unbuildable *because the data isn't there* is. Tier 1's `relationships` gap is the clearest
current example.

## Why the source list needed re-sorting

The proposal grouped modules by *layer* (ingestion / collaboration / compliance / intelligence / operations).
That grouping is how vendors describe finished platforms; it is not how a product with one maintainer and a
2.7%-complete dataset should sequence work. Sorting the same modules by **differentiation × prerequisite
readiness** produces a materially different order, and shows that several "new modules" are things CIF has
already half-built.

### The state everything below is sequenced against

Measured 2026-08-08, not estimated:

| | Now | Target |
|---|---:|---:|
| Curated projects | **27** | ~1000 (`CLAUDE.md`) |
| Patterns (`poc/patterns.json`) | 16 | — |
| Closed backtests (`tools/backtest.py`) | 3 | — |
| Projects with a CIF Score (`poc/qa.json`) | **1** (Arbitrum) | 27 |
| `entities` rows synced | 944 | — |
| `relationships` rows synced | **0** | — |
| Frontend reading real data | **connected** (maintainer, 2026-08-08) | — |

The frontend cutover is done, which removes what would otherwise have been the blocking gate. That shifts
the binding constraint onto this lane: the surfaces now render whatever the database holds, so **thin data
is immediately visible as a thin product**. Two rows above are the live examples — a CIF Score that exists
for 1 project of 27, and a `relationships` table with 0 rows behind a planned graph surface.

---

## Tier 1 — the actual moat (partially built; finish before starting anything new)

| Module (proposal's name) | What already exists | What is actually missing |
|---|---|---|
| Audit Trail & Data Lineage | Not a new module — it **is** `ApplicationBlueprint.md` §3's locked trust architecture. `evidence_items` (795 rows), Evidence Levels, per-fact citations, `qa_phases` coverage | **[frontend]** the per-claim lineage UI. **[data]** the traversal behind "impact analysis" (which Knowledge items depend on this fact) — today `relatedKnowledge`/`relatedEvents` are emitted empty by every extractor, deliberately, because linking them from prose would be inference. That is the handoff seam |
| Calibration track record | §9.3.3 specifies it precisely. 3 closed historical backtests | **The single highest-value gap.** Zero *live* graded calls. **[data]** a store for timestamped calls, their trigger conditions and resolutions — no table exists yet. **[frontend]** the public page. Neither side can start from the other's end |
| Automated pattern detection | `examples/PatternRegistry.md` (16 patterns), `tools/backtest.py` harness, per-pattern evidence | **[data]**, and it is dataset scale rather than code. 16 patterns grounded in 27 projects is thin; the same harness over 100+ projects is a different product |
| Entity resolution / graph | `docs/Ontology/Relationships.md` defines the model; `entities` has 944 rows | **[data]**, and it is a *data* gap not a feature gap: `relationships` has 0 rows because no phase captures entity-to-entity edges. `tools/extract_entities.py`'s docstring is explicit that deriving them from prose would be fabrication. The fix is a research-phase change upstream — a graph surface built today would render an empty canvas |

Three of the four are blocked on **dataset scale or a research-phase change**, not on engineering — which
puts them squarely in this lane. Calibration is the one that needs both sides, and it is also the highest
value, so it is worth agreeing the data contract for it early rather than discovering the mismatch later.

## Tier 2 — differentiated surfaces the data already supports — **[frontend]** builds, **[data]** supplies

`ApplicationBlueprint.md` §2b already designs eight of these and maps each to the phases it draws from:
due-diligence memo export, entity graph explorer, founder/team track-record lookup, red-flag scanner,
historical-analog comparison, Content Studio, portfolio with graded outcomes, structured query/API.

They need **no new research** — they are different views over data already collected. The proposal's
"Automated Investigation Workflow" and "Graph Investigation" are the same thing as §2b's entity graph and
structured query, arrived at from a different direction.

§8 lists their sequencing as an open question. Recommended order below is cheapest-and-most-provable first,
with what this lane owes each one — the useful column for planning here is the third:

| # | Surface | What **[data]** must supply first |
|---|---|---|
| 1 | Red-flag scanner | Nothing new — reads fields already extracted and synced |
| 2 | Due-diligence memo export | Nothing new for the body; CIF Score coverage (1/27 today) if the memo is meant to carry one |
| 3 | Founder/team lookup | Nothing new — `entities` is already cross-project (944 rows), this is the first surface that proves it |
| 4 | Historical-analog comparison | Nothing new for a manual N-way compare; a similarity ranking would be new data work |
| 5 | Entity graph explorer | **Blocked.** `relationships` = 0 rows; needs the research-phase change in Tier 1 |
| 6 | Structured query / API | Schema stability and documented field semantics — the contract, not the endpoint |

Rows 1–4 are unblocked from this lane today. Row 5 is the one to flag to the frontend team early, so it is
not scheduled against data that does not exist yet.

## Tier 3 — Observable connector layer (bounded) — **[data]**

Required by §9.3.2, and the reason §7's telemetry non-goal was reworded. Scope:

- A handful of sources — DefiLlama TVL, funding rounds, unlock schedules — **not 200 connectors**
- Daily refresh, not streaming
- Purpose is to sit **next to a pending read** as verifiable-today evidence, not to be a market-data feed
- Resolves §8's open question on the per-archetype Observable set (an L1 leads with TVL; an early-stage
  protocol leads with round/stage)

The proposal's "Schema Mapping" and "Dynamic Ontology" are, in CIF's case, already solved by the 11-phase
contract plus `tools/extract_*.py`: every source is normalised into the same phase structure by construction.
What CIF lacks is not a semantic layer — it is entity-to-entity edges (Tier 1).

## Tier 4 — team & enterprise plumbing (commodity, demand-gated) — **[frontend]**

RBAC, workspaces, task/approval workflow, activity feed and notifications, SSO/SAML/OIDC, SCIM provisioning,
white-label and custom branding, Slack/Teams/Notion integrations.

All of it is real enterprise-software work, and none of it differentiates CIF from anyone. It is also the
most expensive tier to build and maintain. **Gate: build when a named paying prospect is blocked on a
specific item** — not in anticipation. Today nobody is asking, because nobody can see real data yet.

Two carve-outs that are *not* commodity and belong in Tier 2 instead:

- **Enterprise API** — §9.2 already names it as a Pro direction, and §2b explains why it is differentiated
  here: the data model answers questions like "every project where a Series A closed within five months of a
  security incident", which is not a generic CRUD API over rows.
- **Webhooks on conflict/score change** — cheap, and it is the natural delivery mechanism for §9.4's
  "signal being watched" rather than a generic integration feature.

## Tier 5 — reconsidered or declined, with reasons recorded

| Item | Disposition |
|---|---|
| Predictive CIF Score ("will reach 92 in 3 months") | **Declined**, now an explicit §7 non-goal. CIF Score measures our research completeness, not project health; forecasting it predicts our own future diligence. The underlying want — a forward-looking read on the *project* — is already specified, and better, as §9.4's Trajectory Probability |
| Data versioning & branching ("what if this conflict resolved?") | **Deferred.** Foundry-scale machinery for a 27-dossier corpus with one editor. Revisit past a few hundred projects **and** multiple concurrent editors — the second condition matters more than the first |
| CIF Certification Program | **Declined as a product module.** Training and certification are company activities (marketing, enablement). Nothing to build in the platform until there is an audience to certify |
| Sentiment analysis | **Dormant, revivable.** Never a locked non-goal — the blueprint had simply never taken a position (now recorded in §8). Needs a specific job: an Observable-layer input, or a *divergence* signal where crowd sentiment disagrees with the Current Read. The second is the more interesting product |
| Anomaly detection on coverage ("Coverage dropped 20% this week") | **Fold into maintainer-ops**, not a user surface — it is a signal about our pipeline's health, adjacent to the CIF Score forecasting problem above |

## Sequencing gates

Measurable preconditions, so the roadmap cannot be entered out of order:

| Gate | Condition | Unlocks | Owner |
|---|---|---|---|
| **0** | Frontend reads real Supabase data | Everything — **met 2026-08-08** | frontend |
| **1** | Dataset ≥100 projects, Phase 11 run for the anchor set | Pattern work at credible scale; CIF Score as a real headline number | data |
| **2** | A research phase captures entity-to-entity edges; `relationships` non-empty | Entity graph explorer (Tier 2 #5) | data |
| **3** | A store for timestamped calls + trigger conditions + graded resolutions exists | Calibration track record — needs both lanes; agree the contract before either starts | data + frontend |
| **4** | ≥10 live calls whose resolution window has passed, graded publicly, wrong ones included | Publishing the calibration score — the moat | both |
| **5** | A named prospect blocked on a specific plumbing item | That item only, from Tier 4 | frontend |

With Gate 0 met, the ordering pressure inverts. The pipeline work through 2026-08-08 (streaming fix,
self-repair loop, quality gates) made the research side reliable, and the surfaces now render whatever the
database holds — so from here **the dataset is the product**. Gates 1 and 2 are this lane's critical path;
Gate 3 is the one that needs a conversation between lanes before code is written on either side.

## Related files

- `docs/Project/ApplicationBlueprint.md` — positioning, trust architecture, monetization (source of truth)
- `docs/Project/Roadmap.md` — project-level roadmap this sits under
- `docs/Ontology/Relationships.md` — the entity-graph model behind Tier 1's data gap
- `examples/PatternRegistry.md`, `tools/backtest.py` — the pattern/calibration machinery
- `reset/README.md` — the research pipeline that feeds all of it
