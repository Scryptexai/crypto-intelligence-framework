# Reasoning

## Purpose

Specifies the **inference engine**: scoring, weighting, confidence, similarity, the analog engine, decision trees, explainability, and prediction — how CIF turns structured knowledge into judgements.

## Why This Folder Exists

This is where structured knowledge becomes analysis. The folder documents the mechanisms of reasoning so they are transparent and auditable.

## Source of Truth

Structured knowledge from Ontology, Patterns, and prior stages.

## Input

All upstream structured knowledge.

## Output

A documented, explainable reasoning specification.

## Consumer

Valuation, ExitStrategy, and applications.

## Folder Structure

```
Reasoning/
├── Scoring.md      ├── Similarity.md    ├── Explainability.md
├── Weighting.md    ├── AnalogEngine.md  └── Prediction.md
├── Confidence.md   └── DecisionTree.md
```

## Workflow Position

The `Reasoning` stage of `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Describe mechanisms only.
2. Everything must be explainable.
3. No stored real-project inferences.

## Naming Convention

`PascalCase.md`.

## Future Expansion

ML-assisted reasoning and continuous learning.
