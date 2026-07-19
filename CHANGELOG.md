# CHANGELOG

## Purpose

Document the *purpose and rules* of the project changelog — the running record of notable changes to the repository's structure and documentation.

## Description

This file is a documentation container only. It defines *how* knowledge must be captured — it must not contain knowledge, real project data, examples, or history. Actual content is produced downstream by Deep Research and inserted under this specification. This file specifies how changes will be logged; it does not yet contain project history. Historical entries are added over time as the repository evolves.

## Why This File Exists

The changelog records changes to the framework's structure, not to crypto knowledge. It exists so the evolution of the repository is transparent and reversible.

## Data Source

Maintainer commits and structural changes to the repository.

## Required Content

The following must be recorded per release (documentation of format only):

- Version identifier
- Date
- Added / Changed / Deprecated / Removed sections
- Reference to affected folders or files

## Data Structure

Reverse-chronological list of versioned entries following the Keep a Changelog style.

## Validation Rules

- Newest entries on top.
- Each entry tied to a version from `docs/Project/Versioning.md`.
- Describe structural changes, never knowledge content.
- One entry per notable change.

## Used By

Maintainers, contributors, and reviewers.

## Related Files

`docs/Project/Versioning.md`, root `README.md`, `CONTRIBUTING.md`.

## Future Expansion

Automated changelog generation from commits.
