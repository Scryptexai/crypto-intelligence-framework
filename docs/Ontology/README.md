# Ontology

## Purpose

Defines the **entity model of a crypto project** — the canonical set of dimensions (identity, technology, funding, team, tokenomics, etc.) that describe any project in CIF, plus the **causal unit** (`DecisionEvent`) and its two supporting layers (`Context`, `Hidden`) that patterns are actually discovered from.

## Why This Folder Exists

Reasoning is only possible over a consistent entity model. This folder specifies every attribute a project can have, so knowledge is captured uniformly across all projects. Critically, a project is not itself the unit patterns are found in — a project is dozens of **decisions**. `DecisionEvent` (Context → Trigger → Decision → Alternatives → Reason → Execution → Stakeholder Reactions → Outcome) is the atomic causal unit; `Context` records the era/conditions a decision occurred under (without which patterns get matched blindly across incompatible eras); `Hidden` records the non-measurable factors (motivation, constraint, trade-off) that explain the Observable ones.

## Source of Truth

Normalized entities produced by the Extraction layer.

## Input

Normalized entities from Extraction.

## Output

A complete, typed attribute model for crypto-project entities.

## Consumer

Patterns, Reasoning, Valuation, and Schema layers.

## Folder Structure

```
Ontology/
├── Identity.md         ├── Governance.md    ├── Metrics.md
├── Classification.md   ├── Tokenomics.md    ├── Innovation.md
├── Technology.md       ├── Incentives.md    ├── Success.md
├── Infrastructure.md   ├── Adoption.md      ├── Relationships.md
├── Funding.md          ├── Revenue.md       ├── DecisionEvent.md  (causal unit)
├── Team.md             ├── Security.md      ├── Context.md        (era/conditions layer)
├── Community.md        ├── Risks.md         └── Hidden.md         (non-measurable factors)
└── Ecosystem.md
```

## Workflow Position

Core of the `Ontology` stage in `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Define fields and types only.
2. Reference Taxonomy for controlled vocabularies.
3. No project values inside the model.

## Naming Convention

`PascalCase.md`, one dimension per file.

## Future Expansion

New dimensions, sub-attributes, and cross-entity relationships.
