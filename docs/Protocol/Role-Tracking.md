# Role: Tracking

**Goal:** follow a project the maintainer is actively working on / farming, and keep a **living record**
so the dataset grows not only from history but from unfolding, real-time observation.

**Output location:** `tracking/<Project>/` (dossier + log + prediction).

## When to use
The maintainer is engaging with a live project (testnet, points campaign, pre-TGE, new launch) and wants
its evolution captured over time — and, crucially, wants predictions checked against real outcomes.

## Structure (copy from `tracking/_template/`)

```
tracking/<Project>/
├── dossier.md      # The profile (same fields as a summary profile), updated as facts change
├── log.md          # Append-only, dated observations. Newest at top.
└── prediction.md   # Predictions made + later the ACTUAL outcome (the feedback loop)
```

## Steps

1. **Check the index / tracking/** — is this project already tracked? If yes, update; else scaffold from template.
2. **dossier.md:** capture/refresh identity, category, stage (`docs/TokenLifecycle/`), incentives, and status.
3. **log.md:** add a dated entry for what happened this session ("2026-07-19: testnet incentives live").
4. **prediction.md:** using `Role-Analysis` logic, record the predicted direction + confidence + the analogs
   used. Leave an **Actual Outcome** field blank to be filled when reality is known.
5. **Register** in `examples/DatasetIndex.md` with tier = Tracking (status: active).
6. **Commit & push.**

## Why the feedback loop matters
When a tracked project's outcome becomes known, fill in **Actual Outcome** in `prediction.md`. A confirmed
prediction becomes a **new validated historical data point** → the pattern that produced it gets stronger →
`docs/Reasoning/Confidence.md` scores improve. This is the flywheel: working on more projects makes the
whole system more accurate, not just larger.

## Promotion
A tracked project that matures (reaches an outcome) can be promoted to `examples/Successful/` or
`examples/Failed/` as a validated study, and its prediction-vs-outcome archived.
