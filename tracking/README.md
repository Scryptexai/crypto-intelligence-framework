# tracking

## Purpose

Holds **living records** for projects the maintainer is actively working on or following. Unlike
`examples/` (validated history), `tracking/` captures projects *as they unfold* — so the dataset grows
from real-time observation and, crucially, from **predictions checked against real outcomes**.

## Why This Folder Exists

History alone is static. The most valuable data is a prediction that later comes true (or fails): it
validates a pattern and improves confidence scores. This folder is where that feedback loop lives.

## Source of Truth

Live observation by the maintainer + analysis-role predictions. Provenance recorded per entry.

## Input

A project being worked/farmed (testnet, points, pre-TGE, new launch) and ongoing observations.

## Output

Per-project living dossier + dated log + prediction-vs-outcome record.

## Consumer

The Analysis role (as new analogs), and the maintainer tracking their active projects.

## Folder Structure

```
tracking/
├── _template/          # Copy this to start a new tracked project
│   ├── dossier.md      # Profile (same fields as a summary profile)
│   ├── log.md          # Append-only dated observations, newest on top
│   └── prediction.md   # Prediction + confidence + (later) actual outcome
└── <Project>/          # One folder per tracked project
```

## Workflow Position

Feeds back into `Patterns → Reasoning`: confirmed predictions become validated data points that raise
confidence. Matured projects are promoted to `examples/Successful/` or `examples/Failed/`.

## Rules

1. One folder per tracked project; scaffold from `_template/`.
2. `log.md` is append-only and dated; never rewrite history.
3. Every prediction records confidence + the analogs used, and leaves an Actual Outcome field open.
4. Register each tracked project in `examples/DatasetIndex.md` (tier = Tracking).

## Naming Convention

`tracking/<ProjectName>/` in `PascalCase`; fixed file names `dossier.md`, `log.md`, `prediction.md`.

## Future Expansion

Automated status refresh, alerting on lifecycle transitions, and outcome-driven confidence recalibration.
