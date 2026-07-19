# Similarity

## Purpose

Specify how knowledge about **similarity measurement between projects/patterns** must be captured, structured, and validated within CIF's Reasoning engine layer (Reasoning (Stage 5)).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to similarity measurement between projects/patterns and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), similarity measurement between projects/patterns is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Structured knowledge from Ontology, Patterns, and prior stages.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Similarity definition
- Feature inputs
- Distance/metric fields
- Thresholds

## Data Structure

Method specification: inputs, logic, outputs, and explainability of one reasoning component.

## Validation Rules

- Describe the mechanism, not conclusions about real projects.
- Inputs/outputs must be explicit.
- Must be explainable.
- No stored inferences about real projects.

## Used By

Valuation, ExitStrategy, and applications.

## Related Files

Other Reasoning files, `docs/Schema/*`, all upstream knowledge layers.

## Future Expansion

Model integration, probabilistic reasoning, and learning loops.
