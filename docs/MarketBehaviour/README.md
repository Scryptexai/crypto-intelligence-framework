# MarketBehaviour

## Purpose

Documents **post-launch market-behaviour archetypes** — immediate pump, delayed pump, slow growth, sideways, death spiral, double pump, recovery, distribution, unlock impact, and market correlation.

## Why This Folder Exists

How a token behaves after launch is a decision-critical signal. This folder defines each behaviour archetype so reasoning and exit strategies can map to it.

## Source of Truth

Price/market research plus lifecycle and pattern context.

## Input

Market research and lifecycle context.

## Output

Generic behaviour-archetype definitions.

## Consumer

Reasoning, Valuation, and ExitStrategy layers.

## Folder Structure

```
MarketBehaviour/
├── ImmediatePump.md  ├── DeathSpiral.md   ├── Distribution.md
├── DelayedPump.md    ├── DoublePump.md    ├── UnlockImpact.md
├── SlowGrowth.md     ├── Recovery.md      └── MarketCorrelation.md
└── Sideways.md
```

## Workflow Position

Behaviour sub-layer of the `Patterns` stage feeding `Reasoning` in `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Define archetypes generically.
2. Explicit preconditions.
3. No dated price data.

## Naming Convention

`PascalCase.md`.

## Future Expansion

Probabilistic behaviour classification.
