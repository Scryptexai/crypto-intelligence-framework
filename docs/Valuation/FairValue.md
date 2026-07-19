# FairValue

## Purpose

Specify how knowledge about **the synthesised fair-value estimate** must be captured, structured, and validated within CIF's Valuation layer (Reasoning → Framework (Stage 5/6)).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the synthesised fair-value estimate and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the synthesised fair-value estimate is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Ontology metrics, Patterns, and comparable-project research.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Component lenses
- Weighting reference
- Range/output fields
- Explainability reference

## Data Structure

Valuation-lens specification: definition, inputs, formula/logic fields, output fields.

## Validation Rules

- Define the lens and its inputs, not valuations of real projects.
- Inputs must reference ontology metrics.
- No project valuations stored.
- Method must be explainable.

## Used By

Reasoning, ExitStrategy, and applications.

## Related Files

`docs/Ontology/Metrics.md`, `docs/Reasoning/*`, other Valuation files.

## Future Expansion

Additional valuation lenses and model inputs.
