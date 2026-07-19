# SellImmediately

## Purpose

Specify how knowledge about **the sell-immediately strategy** must be captured, structured, and validated within CIF's Exit-strategy layer (Framework → Applications (Stage 6/7)).

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. It scopes exactly what belongs to the sell-immediately strategy and nothing else, so the knowledge model stays modular and machine-readable.

## Why This File Exists

Within the pipeline (Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications), the sell-immediately strategy is a distinct unit that must be captured explicitly so downstream stages can reason over it consistently and traceably.

## Data Source

Reasoning outputs, MarketBehaviour, and valuation context.

## Required Content

The following must eventually be filled by research (documentation of fields only, not values):

- Definition
- Trigger conditions
- Action steps fields
- Risk fields

## Data Structure

Decision-playbook specification: definition, conditions, actions, risk fields.

## Validation Rules

- Define the strategy generically, not advice on real projects.
- Trigger conditions explicit.
- No personalised or real-time advice stored.
- Must be explainable and reversible in documentation.

## Used By

Applications and human decision-makers.

## Related Files

`docs/MarketBehaviour/*`, `docs/Valuation/*`, other ExitStrategy files.

## Future Expansion

Scenario-based playbooks and risk-parameterisation.
