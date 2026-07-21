# inbox — raw research drop zones (anti-duplicate)

Drop raw reports here by type, then run `./run.sh` (or `python3 tools/ingest.py`). Each type has its own
folder so contexts never mix and maintenance stays clean. Ingest is **anti-duplicate**: a report whose
output dossier already exists is skipped, so re-running only processes newly added files.

```
inbox/
├── deep/       # 1 project / file (22-section Gemini)      -> examples/CaseStudies/<Project>.md
├── batch/      # N projects / file (summary, PROJECT: delim) -> examples/Pioneer/<Project>.md
└── sentiment/  # 1 project / file (8-section Grok/X)        -> examples/Sentiment/<Project>.md
```

Naming: `<Project>_<YYYY-MM>_gemini.docx` (deep/batch), `<Project>_<YYYY-MM>_grok.docx` (sentiment).
The name before the first `_` becomes the project name (deep/sentiment).
