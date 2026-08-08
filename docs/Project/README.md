# Project

## Purpose

Documents CIF *as a project*: its vision, mission, philosophy, architecture, principles, scope, roadmap, and versioning approach.

## Why This Folder Exists

Before any knowledge is captured, the project's intent and boundaries must be explicit. This folder is the constitutional layer that every other folder inherits its rules from.

## Source of Truth

Authored by the CIF maintainers. Not derived from research.

## Input

The strategic intent of the maintainers.

## Output

A shared understanding of what CIF is, why it exists, and how it evolves.

## Consumer

Contributors, AI agents, and reviewers.

## Folder Structure

```
Project/
├── Vision.md
├── Mission.md
├── Philosophy.md
├── Architecture.md
├── Principles.md
├── Scope.md
├── Roadmap.md
├── Versioning.md
├── ApplicationBlueprint.md      ← product spec: positioning, trust architecture, monetization
├── EnterpriseRoadmap.md         ← enterprise module triage + sequencing gates + lane ownership
├── AirdropOS-UI-Audit.md        ← audit of the AirdropOS frontend against ApplicationBlueprint
└── AirdropOS-Rebuild-Prompt.md
```

**Read `ApplicationBlueprint.md` before changing anything user-facing** — it holds the locked decisions
(§3 trust architecture, §7 non-goals, §9 monetization) that every other document inherits.
`EnterpriseRoadmap.md` sequences longer-term modules on top of it and records which lane owns each:
data integration (this repo) vs. frontend/backend integration (the frontend team).

## Workflow Position

Foundational — sits above the pipeline and governs how every stage behaves.

## Rules

1. Describe intent and rules only.
2. No knowledge, no case data.
3. Keep aligned with the pipeline.

## Naming Convention

`PascalCase.md`.

## Future Expansion

Governance, licensing policy, and decision-records can be documented here later.
