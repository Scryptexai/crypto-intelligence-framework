# Benchmarks

## Purpose

Container for reference benchmarks.

## Why This Folder Exists

Reference benchmark artifacts used to **test and calibrate the reasoning layer** — the durable "proof it
works". Each case pairs a set of pre-outcome signals with the real, known outcome; the harness checks whether
the framework's patterns surface what the outcome demands. This is how we prove the knowledge is functional,
repeatably, as the dataset grows.

## Source of Truth

The backtest cases (`cases/*.md`) and the pattern catalogue (`examples/PatternRegistry.md`).

## How to run

```
python3 tools/backtest.py
```
Reads every `cases/*.md`, matches its `given` signals against the patterns, and prints a scorecard
(also writes `poc/benchmarks.json`). Exit code is non-zero if any real case FAILs or a control over-fires —
usable as a CI check.

## Case types

- **validation** — out-of-sample real events (the real proof, e.g. Renzo ezETH depeg).
- **consistency** — in-sample sanity (a pattern classifies its own domain correctly).
- **control** — must fire nothing (guards against over-firing).

## Latest result

`PASS 3/3 · avg recall (non-control) 1.0` — Renzo LRT depeg fires P1/P2/P4; Helium multi-token fires P3;
the oracle control fires nothing.

## Input

Completed template-based knowledge artifacts.

## Output

Reference artifacts for framework validation.

## Consumer

Reviewers and the reasoning-validation process.

## Folder Structure

```
Benchmarks/
└── cases/
    ├── Backtest-01_Renzo-LRT-Depeg.md      # validation (out-of-sample, real)
    ├── Backtest-02_Helium-MultiToken.md    # consistency (in-sample sanity)
    └── Backtest-03_Oracle-Control.md       # control (must fire nothing)
```

Each case file: `type`, `category`, `given` (signals), `expect` (pattern IDs the outcome demands),
`outcome` (what really happened), `source`. Add a new case = add a file here and re-run the harness.

## Workflow Position

Part of the `Applications` layer of `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Empty until validated artifacts exist.
2. Artifacts must follow the templates/schema.
3. No speculative data.

## Naming Convention

Artifacts follow the relevant template naming in `PascalCase.md`.

## Future Expansion

A growing curated library of reference benchmarks.
