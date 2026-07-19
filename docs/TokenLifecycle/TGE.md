# TGE

## Purpose

Specify how knowledge about **the token generation event** must be captured, structured, and validated within CIF's Token lifecycle layer (Patterns (Stage 4) — lifecycle).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the token generation event and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the token generation event is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Ontology, Patterns, and lifecycle research.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Definition
- Entry criteria
- Signals
- Exit criteria

## Data Structure

Phase specification: definition, entry/exit conditions, typical signals, fields.

## Validation Rules

- Define the phase generically.
- Entry/exit conditions must be explicit.
- No dated project data.
- Link neighbouring phases.

## Used By

Reasoning, MarketBehaviour, and Valuation layers.

## Related Files

Adjacent TokenLifecycle files, `docs/MarketBehaviour/*`.

## Future Expansion

Finer-grained sub-phases and phase-transition indicators.
