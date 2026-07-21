# inbox — raw research drop zone

Drop deep-research `.docx` (or `.pdf`) files here, then run:

```
python3 tools/ingest.py
```

Each file becomes examples/CaseStudies/<Name>.md (auto-ingested), the source is archived to
doc_backup/deep/, and the JSON pipeline + backtest rebuild automatically.
File naming: <Project>_<YYYY-MM>_gemini.docx (the name before the first '_' becomes the project name).
