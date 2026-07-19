# Protocol

## Purpose

Defines the **operating protocol** for working in this repository across many independent sessions:
the session flow every worker follows, and one runbook per role. It is what makes CIF buildable over
~150 sessions without losing context — because the process lives in the repo, not in any session's memory.

## Why This Folder Exists

Claude has no memory between sessions. The only durable context is what is written here and in the
knowledge layer. This folder encodes *how* each kind of session must behave so that output stays
consistent whether it is project #10 or project #990, done today or in three months.

## Source of Truth

Authored by the maintainers/architect. Governs process, not knowledge.

## Input

A session's declared role plus the data the maintainer provides (a research report, a batch, a project to track).

## Output

Consistent, index-registered knowledge artifacts committed to `examples/` or `tracking/`.

## Consumer

Every session (human or AI) that operates on the repository.

## Folder Structure

```
Protocol/
├── SessionProtocol.md     # The baseline flow every session follows
├── Role-Ingest-Deep.md    # Runbook: one deep research report → deep case study
├── Role-Ingest-Batch.md   # Runbook: summary batch → many project profiles
├── Role-Tracking.md       # Runbook: follow a live project over time
└── Role-Analysis.md       # Runbook: predict a new project via analogs
```

## Workflow Position

Cross-cutting / operational — governs how work enters the pipeline at every stage.

## Rules

1. Every session reads `CLAUDE.md` (auto) then this protocol before writing.
2. One role per session.
3. Always update `examples/DatasetIndex.md` in the same commit as new knowledge.
4. Record provenance and never fabricate.

## Naming Convention

`SessionProtocol.md` and `Role-<Name>.md` in `PascalCase`.

## Future Expansion

Additional roles (e.g. QC/Reconciliation, Taxonomy-Maintenance) and automation hooks.
