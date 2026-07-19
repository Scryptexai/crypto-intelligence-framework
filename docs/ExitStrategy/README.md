# ExitStrategy

## Purpose

Documents the **decision and exit playbooks** — sell immediately, partial sell, hold, rebuy, profit taking, risk management, and historical comparison — the action layer of the framework.

## Why This Folder Exists

Analysis only matters if it informs action. This folder defines reusable decision playbooks that translate reasoning into strategy templates.

## Source of Truth

Reasoning outputs, MarketBehaviour, and valuation context.

## Input

Reasoning outputs and market/valuation context.

## Output

Generic decision playbooks with trigger conditions.

## Consumer

Applications and analysts.

## Folder Structure

```
ExitStrategy/
├── SellImmediately.md  ├── Rebuy.md         ├── RiskManagement.md
├── PartialSell.md      ├── ProfitTaking.md  └── HistoricalComparison.md
└── Hold.md
```

## Workflow Position

Action layer bridging `Framework` and `Applications` in `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Define strategies generically.
2. Explicit triggers.
3. Never store real-time or personal advice.

## Naming Convention

`PascalCase.md`.

## Future Expansion

Scenario playbooks and parameterised risk rules.
