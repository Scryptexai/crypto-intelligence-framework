# TokenLifecycle

## Purpose

Documents the **lifecycle phases of a token/project** — pre-launch, testnet, mainnet, TGE, post-TGE, expansion, maturity, and decline.

## Why This Folder Exists

A project's signals mean different things at different phases. This folder defines each phase so reasoning is phase-aware.

## Source of Truth

Ontology, Patterns, and lifecycle research.

## Input

Ontology and lifecycle research.

## Output

Phase definitions with entry/exit conditions.

## Consumer

Reasoning and MarketBehaviour layers.

## Folder Structure

```
TokenLifecycle/
├── PreLaunch.md   ├── TGE.md       ├── Maturity.md
├── Testnet.md     ├── PostTGE.md   └── Decline.md
├── Mainnet.md     └── Expansion.md
```

## Workflow Position

Lifecycle sub-layer of the `Patterns` stage in `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Define phases generically.
2. Explicit transitions.
3. No dated project data.

## Naming Convention

`PascalCase.md`, ordered by lifecycle.

## Future Expansion

Sub-phases and transition indicators.
