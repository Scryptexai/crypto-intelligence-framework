# DelayedPump

## Purpose

Specify how knowledge about **the delayed-pump behaviour** must be captured, structured, and validated within CIF's Market-behaviour layer (Patterns (Stage 4) — market behaviour).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the delayed-pump behaviour and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the delayed-pump behaviour is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Price/market research plus lifecycle and pattern context.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Definition
- Preconditions
- Signals
- Timing fields

## Data Structure

Behaviour archetype specification: definition, preconditions, signals, typical fields.

## Validation Rules

- Define the archetype generically.
- Preconditions/signals explicit.
- No dated price data.
- Link to lifecycle where relevant.

## Used By

Reasoning, Valuation, and ExitStrategy layers.

## Related Files

`docs/TokenLifecycle/*`, `docs/ExitStrategy/*`, other MarketBehaviour files.

## Future Expansion

Quantified behaviour classifiers and probability fields.
