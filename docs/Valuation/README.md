# Valuation

## Purpose

Documents the **valuation lenses** — FDV, market cap, TVL, revenue, user base, competitors, comparable projects, and fair value — used to reason about how a project should be priced.

## Why This Folder Exists

Valuation is where knowledge becomes an investable judgement. This folder defines each lens and its inputs so valuations are consistent and explainable.

## Source of Truth

Ontology metrics, Patterns, and comparable-project research.

## Input

Ontology metrics and comparables research.

## Output

Structured valuation-lens definitions.

## Consumer

Reasoning and ExitStrategy layers.

## Folder Structure

```
Valuation/
├── FDV.md        ├── Revenue.md    ├── Competitors.md
├── MarketCap.md  ├── UserBase.md   ├── ComparableProjects.md
├── TVL.md        └── FairValue.md
```

## Workflow Position

Bridges the `Reasoning` and `Framework` stages of `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Define lens + inputs only.
2. Inputs reference ontology metrics.
3. No project valuations stored.

## Naming Convention

`PascalCase.md`.

## Future Expansion

Model-driven valuation and scenario ranges.
