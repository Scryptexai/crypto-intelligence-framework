# docs — The CIF Knowledge Model

## Purpose

`docs` holds the complete documentation of the CIF knowledge model: how crypto knowledge is researched, extracted, structured (ontology & taxonomy), organised into patterns, reasoned over, and schematised.

## Why This Folder Exists

It exists to separate the *definition* of the knowledge model from the eventual knowledge itself. Each subfolder documents one layer of the pipeline so that the whole model is legible and modular.

## Source of Truth

Source of truth for the structure, vocabulary, and rules of every knowledge layer.

## Input

Research findings and extracted entities flowing in from the research stage.

## Output

A layered set of specifications that downstream reasoning and applications rely on.

## Consumer

Reasoning modules, schema/database mappers, and human analysts.

## Folder Structure

```
docs/
├── Project/          # Meta: vision, mission, principles, scope of CIF itself
├── Research/         # Stage 1 — how knowledge is gathered
├── Extraction/       # Stage 2 — turning research into structured entities
├── Ontology/         # Stage 3 — the entity model of a crypto project
├── Taxonomy/         # Stage 3 — classification vocabularies
├── Meta/             # Stage 3 — narratives, cycles, market meta-layer
├── Innovation/       # Stage 4 — innovation assessment dimensions
├── Success/          # Stage 4 — success-factor dimensions
├── Patterns/         # Stage 4 — recurring behavioural/economic patterns
├── TokenLifecycle/   # Stage 4 — lifecycle phases of a token
├── MarketBehaviour/  # Stage 4 — post-launch market behaviour archetypes
├── Valuation/        # Stage 5/6 — valuation lenses
├── ExitStrategy/     # Stage 6/7 — decision & exit playbooks
├── Reasoning/        # Stage 5 — the inference engine specification
└── Schema/           # Cross-cutting — structural contracts for all layers
```

## Workflow Position

`docs` is the backbone of the pipeline `Research → Knowledge → Ontology → Patterns → Reasoning → Framework → Applications`, covering every stage except the final Applications layer (represented by `examples/`).

## Rules

1. Each subfolder documents exactly one layer and links to its neighbours.
2. No knowledge values live here — only structure, vocabulary, and rules.
3. Every subfolder has a `README.md` plus topic files.

## Naming Convention

Subfolders in `PascalCase`; files in `PascalCase.md`.

## Future Expansion

Additional layers (e.g. Regulation, Sentiment, Governance-Deep) can be added as new subfolders.
