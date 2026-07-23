# Context

## Purpose

Specify how knowledge about **the state of the world a decision was made under** must be captured —
the "Context Layer" that makes a `DecisionEvent` comparable (or explicitly *not* comparable) to another.

## Description

This file is a documentation container only. It defines *how* context must be captured — it must not
contain real snapshots of any project's environment. Actual Context snapshots are produced downstream inside
deep dossiers and `DecisionEvent` instances, and inserted under this specification.

## Why This File Exists

The same decision produces different outcomes under different conditions. "Run an incentivized testnet with
a simple bridge-and-swap task" produced huge airdrops in 2021 (few hunters, immature Sybil detection, novel
task); the identical mechanic in 2026 produces a poor result (saturated hunter population, mature Sybil
detection, commoditized task). Without recording Context, the reasoning layer cannot tell these two
situations apart and will pattern-match blindly across eras — exactly the failure mode this file exists to
prevent. Context is what turns "this looks similar" into "this is/isn't actually comparable."

## Data Source

Deep dossiers (`examples/CaseStudies/*`) — particularly §2 Industry Background, §8 Narrative Intelligence,
and §9 Competitive Landscape of the `docs/Protocol/Deep-Research-Brief.md` contract — read as a snapshot at
the time of a specific `DecisionEvent`, not only as static background.

## Required Content

The following dimensions must eventually be filled by research (documentation of fields only, not values),
each a snapshot **at the point in time of a given decision**:

- **Industry State** — the maturity/phase of the sector at that time (ref `docs/Meta/MarketCycles.md`).
- **Competitor State** — who else existed, their approach, and relative position (ref `docs/Valuation/Competitors.md`).
- **Technology Maturity** — what was and wasn't technically possible/mature yet (ref `docs/Ontology/Technology.md`).
- **Macro Conditions** — broader market cycle, liquidity environment, risk appetite (ref `docs/Meta/MarketCycles.md`, `docs/Meta/Hype.md`).
- **User / Hunter Population** — size and sophistication of the participant base relevant to the decision
  (e.g. airdrop hunter count, Sybil-detection maturity, task complexity norms of that era) — ref
  `docs/Ontology/Community.md`, `docs/Patterns/Distribution.md`.
- **VC / Capital Climate** — funding availability and investor expectations at the time (ref `docs/Ontology/Funding.md`).
- **Liquidity Conditions** — depth of available capital/LP at the time (ref `docs/Valuation/*`).
- **Narrative Context** — which narrative(s) were dominant/emerging/fading (ref `docs/Meta/Narratives.md`).

## Data Structure

```
Context:
  as_of: <date/period>
  industry_state: text
  competitor_state: [ {competitor, approach, position} ]
  technology_maturity: text
  macro_conditions: text
  user_hunter_population: text
  vc_capital_climate: text
  liquidity_conditions: text
  narrative_context: [narrative_ref]
```

## Validation Rules

- Context is always a **snapshot at a point in time**, never a general/timeless description of the sector.
- A `DecisionEvent` without an attached Context snapshot is incomplete — do not omit it.
- When comparing two DecisionEvents (analog matching), the reasoning layer must weigh Context similarity
  explicitly, not assume it — two similar decisions under dissimilar Context are a weak analogy, not a strong one.
- Do not backfill Context with present-day knowledge the actors at the time did not have.

## Used By

`docs/Ontology/DecisionEvent.md`, `docs/Reasoning/Similarity.md`, `docs/Reasoning/AnalogEngine.md`,
`docs/Reasoning/Confidence.md` (era-mismatch should lower confidence, not just sector-mismatch),
`examples/PatternRegistry.md` (a pattern's `scope` field records the Context range it was observed under).

## Related Files

`docs/Ontology/DecisionEvent.md`, `docs/Meta/MarketCycles.md`, `docs/Meta/Narratives.md`,
`docs/Valuation/Competitors.md`, `docs/Ontology/Hidden.md`.

## Future Expansion

A quantified "era index" (e.g. hunter-population estimate, Sybil-maturity score) once enough DecisionEvents
exist to calibrate one.
