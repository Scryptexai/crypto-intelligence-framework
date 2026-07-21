# Session Protocol

The baseline flow **every** session follows, regardless of role.

## 0. Bootstrap
- `CLAUDE.md` is read automatically. It tells you what CIF is, the two layers, and the golden rules.
- Identify the **role** for this session (the maintainer states it, or infer from the request).
- Open the matching runbook in `docs/Protocol/Role-*.md`.

## 1. Sync FIRST (mandatory — do this before anything else)
- Sessions run in **parallel** and each is a separate worker with its own working copy. Sibling sessions
  (other Ingest/Analysis sessions) may have pushed new dossiers you cannot see yet.
- Run `git fetch origin` then fast-forward your branch (`git pull --ff-only origin <branch>`) **before**
  reading or counting anything. Skipping this makes the dataset look smaller than it is (a stale checkout,
  not data loss).
- Re-read `examples/DatasetIndex.md` **after** syncing so counts and the dedup guard reflect reality.

## 2. Orient (cheap reads only)
- Read `examples/DatasetIndex.md` — the map of everything already curated (dedup guard).
- Do **not** read the whole dataset. Read only what the role needs (index + templates + the new data +
  any specific analog files the task points to). This keeps per-session context flat as the dataset grows.

## 3. Do the role's work
- Follow the role runbook step by step.
- Ground every claim in the provided research or cited web sources. Never fabricate.
- Structure knowledge against the `docs/` ontology and link back to it.

## 4. Register
- Add/update the row(s) in `examples/DatasetIndex.md` (project name, category, era, priority, tier, file, source).
- If new taxonomy terms appeared, note them (see Taxonomy handling in the ingest runbooks).

## 5. Provenance
- Every artifact records its **source** (Deep Research / Gemini, or Web research + citations) and **tier**
  (Deep / Summary / Tracking).

## 6. Commit & push
- Commit with a clear message; push to the working branch.
- The knowledge artifact + the index update go in the **same commit**.
- If the push is rejected because a sibling session pushed first, `git pull --ff-only` (or rebase) then push
  again — never force-push over a sibling's work.

## Guard rails
- **Dedup:** if the project already exists in the index, update it — do not create a duplicate.
- **Layer discipline:** knowledge → `examples/` or `tracking/`; `docs/` stays documentation-only.
- **Confidence, not certainty:** predictions are probabilistic and carry a confidence grounded in how many
  historical instances support the pattern.
