# FDV

## Purpose

Specify how knowledge about **the fully-diluted-valuation lens** must be captured, structured, and validated within CIF's Valuation layer (Reasoning → Framework (Stage 5/6)).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the fully-diluted-valuation lens and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the fully-diluted-valuation lens is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Ontology metrics, Patterns, and comparable-project research.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Definition
- Required inputs
- Calculation logic fields
- Interpretation guidance fields

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
