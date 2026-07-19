# Research

## Purpose

Documents **Stage 1** of the pipeline: how raw information about crypto projects is discovered, sourced, collected, verified, and quality-controlled before it becomes knowledge.

## Why This Folder Exists

Everything downstream depends on trustworthy inputs. This folder defines the disciplined process that guarantees inputs are sourced and verified consistently.

## Source of Truth

Deep Research (Gemini) and the primary/secondary sources it consults.

## Input

Whitepapers, dashboards, on-chain data, official and community sources.

## Output

Verified, provenance-tagged raw research ready for extraction.

## Consumer

The Extraction layer.

## Folder Structure

```
Research/
├── Sources.md
├── Verification.md
├── Collection.md
├── ResearchWorkflow.md
├── DeepResearch.md
└── QualityControl.md
```

## Workflow Position

Front of the pipeline — the `Research` step in `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`.

## Rules

1. Document process, not results.
2. Every source must be classifiable by reliability.
3. Research must be reproducible.

## Naming Convention

`PascalCase.md`.

## Future Expansion

Source APIs, crawler configs, and automated verification pipelines.
