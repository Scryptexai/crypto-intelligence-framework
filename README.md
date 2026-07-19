# Crypto Intelligence Framework (CIF)

## Purpose

CIF is a **Knowledge Repository**, not a source-code project. It is the structured, self-documenting foundation that turns raw crypto research into a reasoning system capable of analysing, classifying, and predicting the behaviour of crypto projects.

## Why This Folder Exists

The crypto domain is fragmented across whitepapers, dashboards, social channels, and on-chain data. CIF exists to give that scattered information a single, disciplined structure so that both AI and humans can consume it without additional explanation. Every folder and file documents its own function — the repository is designed to be understood by reading it.

## Source of Truth

This repository is the source of truth for the *structure and rules* of CIF knowledge. Knowledge values themselves originate from Deep Research (Gemini) and are inserted under the specifications defined here.

## Input

Raw research output, extracted entities, and curated crypto knowledge produced by Deep Research.

## Output

A structured, validated, machine-readable knowledge base and reasoning framework for crypto projects.

## Consumer

Downstream AI reasoning modules, analysts, and any application built on top of the framework.

## Folder Structure

```
crypto-intelligence-framework/
├── docs/          # The knowledge model: ontology, taxonomy, patterns, reasoning, schema
├── templates/     # Reusable capture templates for research and knowledge entry
├── examples/      # Slots for validated case studies and benchmarks (containers only)
├── assets/        # Diagrams, images, icons supporting the documentation
└── archive/       # Deprecated or superseded material
```

## Workflow Position

This repository spans the entire pipeline:

`Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`

`docs/Research` and `docs/Extraction` sit at the front; `docs/Ontology`, `docs/Taxonomy` and `docs/Meta` form the knowledge/ontology layer; `docs/Patterns`, `docs/Innovation`, `docs/Success`, `docs/TokenLifecycle`, `docs/MarketBehaviour` form the pattern layer; `docs/Reasoning`, `docs/Valuation`, `docs/ExitStrategy` form the reasoning/framework layer; `examples` represents applications.

## Rules

1. This repository builds **containers**, not knowledge.
2. Never store real project data, history, or examples inside documentation files.
3. Every folder must contain a `README.md`; every knowledge file must follow the file format.
4. Knowledge is inserted only through the structures defined in `docs/Schema` and `templates/`.

## Naming Convention

Folders use `PascalCase` or lowercase domain names. Documentation files use `PascalCase.md`. Every folder's entry point is `README.md`.

## Future Expansion

New knowledge domains, additional reasoning modules, API/serving layers, and generated knowledge-graph exports can be added without changing the documented pipeline.
