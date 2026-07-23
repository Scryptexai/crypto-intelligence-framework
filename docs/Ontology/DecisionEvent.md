# DecisionEvent

## Purpose

Specify how knowledge about **a single significant decision made by a project** must be captured, structured,
and validated — the atomic causal unit CIF reasons over. This is the ontology's most important addition:
patterns emerge at the level of *decisions*, not projects, so cross-project pattern discovery requires this
unit to exist explicitly.

## Description

This file is a documentation container only. It defines *how* a decision must be captured — it must not
contain real project decisions, examples, or history. Actual Decision Event instances are produced downstream
(inside deep dossiers, §16/§19 of the Deep Research Brief) and inserted under this specification.

## Why This File Exists

A project is not one story — it is dozens to hundreds of consequential decisions (which consensus to adopt,
whether to launch permissionless, how to design an airdrop, when to unlock tokens, how to respond to a
controversy). Comparing *projects* hides the real pattern; comparing *decisions* reveals it. Two projects in
unrelated sectors (an L1 and a prediction market) can share the exact same Decision Event shape — this is the
unit that makes cross-sector, cross-era pattern discovery possible. Within the pipeline
(`Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`), DecisionEvent sits
inside Ontology as the structural bridge to Patterns: a Pattern (`docs/Patterns/*`,
`examples/PatternRegistry.md`) is a recurring *shape* observed across many DecisionEvent instances.

## Data Source

Deep dossiers (`examples/CaseStudies/*`), specifically their Historical Timeline (§16) and Knowledge
Extraction (§19) sections — extracted per the `docs/Protocol/Deep-Research-Brief.md` contract.

## Required Content

The following fields must eventually be filled by research (documentation of the schema only, not values):

- **Context** — the state of the world immediately before the decision (link to `docs/Ontology/Context.md`
  for the full Context Layer: industry state, competitor state, technology maturity, macro conditions, user/hunter
  population, liquidity conditions).
- **Problem / Opportunity** — what the team was facing (a bottleneck, a threat, an opening).
- **Trigger** — the specific event or pressure that forced the decision to be made *now*.
- **Decision** — what was actually chosen.
- **Alternatives Considered** — what else could have been chosen, and why it wasn't (if known/inferable).
- **Reason / Evidence** — the stated or inferable justification for the choice. Preserve conflicting or
  minority accounts rather than collapsing to one explanation (see Validation Rules).
- **Execution** — how the decision was implemented (mechanism, timeline).
- **Stakeholder Reactions** — how each affected group responded: Founder, VC, Retail, Community, Developer,
  Institution, Validator, Builder (same 8 POVs as the Success-Matrix in the Deep Research Brief) — each may
  react differently to the *same* decision.
- **Short-term Outcome** — the immediate, observable effect (days to weeks).
- **Long-term Outcome** — the durable, observable effect (months to years).
- **Observable Factors** — measurable data tied to this event (funding amounts, TVL, wallets, volume,
  developer counts — ref `docs/Ontology/Metrics.md`, `Funding.md`, `Adoption.md`).
- **Hidden Factors** — non-measurable but explanatory context (motivation, constraint, internal objective,
  strategic goal, risk tolerance, trade-off) — ref `docs/Ontology/Hidden.md`. Only recorded when the source
  gives explicit or strongly-evidenced grounds — never invented.
- **Evidence Level** — HIGH/MEDIUM/LOW per the Deep Research Brief §22 convention.

## Data Structure

```
DecisionEvent:
  project: <ref to Ontology/Identity>
  context: <ref to Ontology/Context.md snapshot>
  problem_or_opportunity: text
  trigger: text
  decision: text
  alternatives_considered: [text]
  reason_evidence: text (+ conflicting_accounts: [text] if any)
  execution: text
  stakeholder_reactions: { Founder, VC, Retail, Community, Developer, Institution, Validator, Builder }
  short_term_outcome: text
  long_term_outcome: text
  observable_factors: { ... }
  hidden_factors: { ... }
  evidence_level: HIGH | MEDIUM | LOW
```

## Validation Rules

- A DecisionEvent is a **causal chain**, not a fact list — every field must connect to the next
  (Context → Trigger → Decision → Reaction → Outcome).
- **Research is an investigator, not an analyst**: the source material should preserve competing
  explanations and minority views rather than pre-concluding "why it succeeded" — synthesis/conclusion is
  `docs/Reasoning/`'s job, not the research report's.
- Stakeholder Reactions must be recorded **per POV** — never collapse to one "the community reacted" verdict.
- Hidden Factors require textual grounding from the source; if absent, mark the field `unknown` rather than
  inferring silently.
- Every DecisionEvent must carry the Context snapshot it occurred under — a decision without its Context is
  not comparable to another decision (this is what prevents blind era-mismatched pattern matching).

## Used By

`examples/PatternRegistry.md` (a Pattern is a recurring DecisionEvent shape), `docs/Reasoning/AnalogEngine.md`,
`docs/Reasoning/Similarity.md`, `docs/Reasoning/Prediction.md`.

## Related Files

`docs/Ontology/Context.md`, `docs/Ontology/Hidden.md`, `docs/Success/*` (8-POV reactions),
`docs/Protocol/Deep-Research-Brief.md`, `examples/PatternRegistry.md`.

## Future Expansion

A dedicated `examples/DecisionEvents/` extraction layer (structured instances pulled out of dossiers) once
volume justifies it; for now, Decision Events live inline within each deep dossier's Timeline/Knowledge
Extraction sections to keep per-session cost flat.
