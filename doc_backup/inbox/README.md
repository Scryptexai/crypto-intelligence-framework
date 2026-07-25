# inbox — raw research drop zones (anti-duplicate)

Drop raw reports here by type, then run `./run.sh` (or `python3 tools/ingest.py`). Each type has its own
folder so contexts never mix and maintenance stays clean. Ingest is **anti-duplicate**: a report whose
output dossier already exists is skipped, so re-running only processes newly added files.

```
inbox/
├── deep/       # 1 project / file (22-section Gemini, or 7-section v2)  -> examples/CaseStudies/<Project>.md
├── batch/      # N projects / file (summary, PROJECT: delim)            -> examples/Pioneer/<Project>.md
├── sentiment/  # 1 project / file (8-section Grok/X)                    -> examples/Sentiment/<Project>.md
└── phased/     # 1 project / FOLDER (Format v3, N phase files)          -> examples/CaseStudies/<Project>.md
```

Naming: `<Project>_<YYYY-MM>_gemini.docx` (deep/batch), `<Project>_<YYYY-MM>_grok.docx` (sentiment).
The name before the first `_` becomes the project name (deep/sentiment).

**`phased/`** is different from the other three: one **folder per project**
(`phased/<ProjectName>/`), containing one file per research phase actually run — any subset, any count
(elastic, per `docs/Protocol/Deep-Research-Brief.md` "Format v3 — Dependency Pipeline"). The **filename** must
contain the phase key as a substring (`foundation`, `entity`, `history`, `technology`, `financial`, `token`,
`ecosystem`, `market`, `behavioral`, `knowledge`, `conflict` — case-insensitive, e.g. `01-foundation.docx`),
and each file should end with an `Open Threads` heading + bullet list. `tools/ingest.py` assembles all present
phases into one dossier in dependency order — no LLM, no separate "Canonical Report Builder" prompt needed.
