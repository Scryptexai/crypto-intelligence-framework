# Hidden

## Purpose

Specify how knowledge about **the non-measurable factors that explain a project's observable behavior** must
be captured — motivation, constraint, pressure, trade-off, internal objective, strategic goal, risk posture,
expectation. This is the deliberate counterpart to `docs/Ontology/Metrics.md` and the other Observable
dimensions.

## Description

This file is a documentation container only. It defines *how* hidden factors must be captured — it must not
contain real project data. Actual Hidden-factor content is produced downstream (within `DecisionEvent`
instances in deep dossiers) and inserted under this specification.

## Why This File Exists

Observable facts (funding amount, TVL, wallet count, token allocation %) describe *what happened*. They do
not, by themselves, explain *why*. "A project distributed 1 billion tokens for free" is Observable; "the
team held a treasury large enough that it didn't need near-term revenue, so it chose growth over
monetization" is Hidden — and it is the Hidden factor that actually explains the Observable one. Capturing
only Observable data leaves CIF unable to distinguish superficially similar events with different causes
(e.g. a large airdrop driven by treasury abundance vs. one driven by desperate liquidity bootstrapping) —
which is exactly the distinction that matters for prediction.

## Data Source

Deep dossiers — inferred *with textual grounding* from funding intelligence, founder/team statements,
governance discussions, and stated strategic rationale (never invented). Read alongside a `DecisionEvent`'s
Reason/Evidence field.

## Required Content

The following categories must eventually be filled by research (documentation of fields only, not values):

- **Motivation** — what the team was trying to achieve.
- **Constraint** — what limited their options (runway, technical debt, regulatory exposure, team size).
- **Pressure** — external forces acting on the decision (VC expectations, competitive threat, community demand).
- **Trade-off** — what was explicitly or implicitly given up by choosing one path.
- **Internal Objective** — a stated or strongly-evidenced internal goal (e.g. "prioritise decentralization
  over short-term revenue").
- **Strategic Goal** — the longer-horizon aim the decision served.
- **Risk Posture** — how much risk the team was willing to accept, and why.
- **Expectation** — what outcome the team believed the decision would produce.

## Data Structure

```
Hidden:
  motivation: text | unknown
  constraint: text | unknown
  pressure: text | unknown
  trade_off: text | unknown
  internal_objective: text | unknown
  strategic_goal: text | unknown
  risk_posture: text | unknown
  expectation: text | unknown
  grounding: <citation/quote reference — required whenever a field is not "unknown">
```

## Validation Rules

- **Never invent.** Every non-`unknown` field must be traceable to a source statement, interview, governance
  post, or strongly-evidenced inference explicitly marked as such — distinguish "the team said X" from
  "it is plausible that X".
- If a Hidden factor cannot be grounded, the field is `unknown` — this is a valid and expected value, not a
  gap to fill with speculation.
- Hidden factors support **Decision Events**; they are not collected standalone.

## Used By

`docs/Ontology/DecisionEvent.md`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Prediction.md`
(a prediction grounded partly in Hidden factors should say so, and carry correspondingly calibrated confidence).

## Related Files

`docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md`, `docs/Ontology/Metrics.md` (the Observable counterpart).

## Future Expansion

A taxonomy of recurring Hidden-factor archetypes (e.g. "treasury-abundance growth-first", "VC-pressure
liquidity-bootstrap") once enough DecisionEvents make the categories empirically stable.
