# Liquidity

## Purpose

Specify how knowledge about **liquidity dynamics patterns** must be captured, structured, and validated within CIF's Patterns layer (Patterns (Stage 4)).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to liquidity dynamics patterns and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), liquidity dynamics patterns is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Candidate patterns from Extraction plus cross-project research.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Definition
- Liquidity sources
- Signals
- Risk fields

## Data Structure

Pattern specification: name, definition, trigger conditions, signals, outcomes fields.

## Validation Rules

- Define the pattern generically, not instances.
- Conditions and signals must be explicit.
- No real project examples stored.
- Link to PatternSchema.

## Used By

Reasoning, MarketBehaviour, and Valuation layers.

## Related Files

`docs/Schema/PatternSchema.md`, `docs/MarketBehaviour/*`, other Patterns files.

## Future Expansion

New patterns and quantified pattern-detection signals.
