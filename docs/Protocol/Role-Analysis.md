# Role: Analysis

**Goal:** given a NEW project, predict its likely direction by analogy to the curated history — with an
explicit, calibrated confidence and a transparent reasoning trail.

**Output location:** a report to the maintainer, and/or `tracking/<Project>/prediction.md` if it is tracked.

## When to use
The maintainer asks "where is project X heading?" or "what does the data say about this new launch?"

## Steps (mirrors `docs/Reasoning/`)

1. **Profile the target** — capture the new project's known facts into the standard fields (category, stage,
   incentives, tokenomics, team, narrative). Note what is unknown.
2. **Retrieve analogs** (`docs/Reasoning/Similarity.md`) — from `examples/DatasetIndex.md`, pull the handful
   of historical projects most similar by category, stage, incentive design, and market context. **Read only
   those files**, not the whole dataset.
3. **Match patterns** (`docs/Patterns/*`, `docs/Reasoning/AnalogEngine.md`) — identify which documented
   patterns the target matches (flywheel, ponzinomics, unlock impact, tokenomics-simplification, etc.).
4. **Predict** (`docs/Reasoning/Prediction.md`) — state the likely path (e.g. market behaviour archetype,
   lifecycle trajectory, key risks) drawn from what the analogs did.
5. **Confidence** (`docs/Reasoning/Confidence.md`) — grade it by *how many* independent historical instances
   support the pattern and how close the analogs are. More instances + closer analogs → higher confidence.
6. **Explain** (`docs/Reasoning/Explainability.md`) — show the analogs and patterns used, so the prediction
   is auditable, never a black box.

## Output shape

```
Target: <project>  |  Stage: <lifecycle>  |  Category: <taxonomy>
Analogs used: <projectA (link)>, <projectB (link)>, ...
Patterns matched: <pattern (link)>, ...
Prediction: <likely direction / behaviour / risks>
Confidence: <Low / Medium / High> — because <N instances, closeness of analogs>
Watch-for signals: <what would confirm or break the prediction>
```

## Rules
- **Probabilistic, not certain.** Always attach confidence and the evidence behind it.
- **Cite analogs by file.** No prediction without named historical support.
- If tracked, write the result into `tracking/<Project>/prediction.md` and leave Actual Outcome open.
