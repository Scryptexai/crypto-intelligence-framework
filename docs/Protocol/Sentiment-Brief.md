# Sentiment Brief (canonical)

The **contract** for the third document type: X-Engagement / Sentiment reports (produced in Grok, which has X
access; the paste-ready prompt is kept external — see the "Grok prompt" note below). A sentiment report is a
**companion** to a fundamental deep dossier — it captures how the community and the project *felt and
communicated at the time*, per phase. Read this before ingesting any sentiment report.

- **Fundamental** (`examples/CaseStudies/<Project>.md`) — what happened & why. Source: Gemini.
- **Sentiment** (`examples/Sentiment/<Project>.md`) — how it was perceived, per phase. Source: **X only** (Grok).
- The two are **linked both ways** and kept in **separate modules** so contexts never mix.

## Division of labor — X-ONLY (this is the whole point)

Grok's job is **exclusively the X sentiment layer**. Everything non-X — dates, events, milestones, numbers,
anchors — is **already captured in the uploaded Gemini fundamental report**; Grok must **reference those from
the report** ("per laporan Gemini"), and must **not** search news/blogs/Wikipedia/Messari/market sites or
re-verify them. Re-fetching external context is off-task, redundant, and dilutes the one thing X access
uniquely provides: the crowd's voice at the time.

**Why this is a moat:** historical point-in-time X sentiment is ephemeral (posts deleted, algorithms change).
Capturing it now — with real X evidence and evidence-tags — is hard to replicate. The alpha is the
**divergence** between fundamentals (Gemini) and sentiment (X) — a signal fundamentals alone cannot give.

## Non-negotiable honesty rules (this is what keeps the moat credible)

1. **X evidence, not external re-search.** In each phase, the verifiable evidence is a **real X permalink**
   (a `x.com/…` post/thread). Fundamental context is cited as **"per laporan Gemini"** (no external URL). If no
   X post can be linked, write `no linkable X post found` and give aggregate mood only.
2. **Never fabricate tweets, handles, or permalinks.** If a specific post/handle can't be surfaced, describe
   the *aggregate mood* instead ("narasi dominan Q3-2021 …"). A made-up @user or link poisons the dataset.
3. **Evidence Level** per phase: `HIGH` = strong, consistent X signal (volume + multiple notable voices);
   `MEDIUM`/`LOW` = thin or ambiguous X signal.
4. **Concrete X signals required**, not vague prose: approximate engagement volume (low/med/high/spike),
   polarity, dominant on-X narrative, and notable KOL handles + the gist of what they said (permalink if any).
5. **Time-stamp every phase** (dates taken from the Gemini report); align to `docs/TokenLifecycle/`.
6. **Note the bias.** X skews Retail/hype/English → strong for Retail & Community POV, weak for
   Institution & Developer → lower their confidence. Say so. Include a **capture date**.

## The 8 sections (input contract)

1. **Overview & Coverage** — project, periode yang dicakup, sumber (**X only** + laporan Gemini untuk konteks), metode, bias, capture date.
2. **Sentiment Timeline by Phase** — untuk tiap fase (pre-launch / testnet / TGE / +30d / +90d / momen krisis /
   current), field wajib berurutan: `Fase`, `Timestamp` (dari laporan Gemini), `Polarity`, `X engagement volume`,
   `Dominant narrative on X`, `Notable X voices` (handle + gist + permalink), `X evidence` (permalink / "no linkable X post found"),
   `Sampled mood` (agregat), `Evidence Level`.
3. **Community Voice** — dipisah (pakai bullet `Label: Value`, bukan prosa): `Retail`, `KOL/Influencer`,
   `Builder/Developer`. Apa yang mereka katakan & rasakan **di X**.
4. **Project Voice** — bagaimana tim berkomunikasi saat itu (announcement style, respon krisis, transparansi).
5. **Sentiment ↔ Fundamental Divergence** *(crown jewel)* — di mana mood menyimpang dari fundamental
   (euforia vs lemah → dump risk; apatis vs kuat → akumulasi); lag narasi vs harga.
6. **Engagement Authenticity** — organik vs farmed/bot/insentif; relevan untuk pola airdrop/points.
7. **Extracted Sentiment Patterns** — pola reusable (hype-cycle timing, community resilience, narrative-shift,
   capitulation) → feed `docs/Meta/*` + `examples/PatternRegistry.md`.
8. **Evidence Level & Provenance** — ringkasan keyakinan per kesimpulan kunci + daftar sumber (numbered, `Title — URL`).

## Input Formatting Contract (WAJIB — sama disiplin dengan Deep brief)

Written for machine reasoning; parsed by `tools/ingest.py --type sentiment`.
1. `.docx`, markdown-only, single column, no tables, no citation chips (paste plain text).
2. **Numbered headings, one line each:** `# 1 Overview & Coverage` … `# 8 Evidence Level & Provenance`.
3. **No tables** → nested `Label: Value` bullets, in **every** section (Community Voice too — not prose). Per phase example:
   ```
   - Fase: TGE (Nov 2021)
     - Timestamp: Nov 2021 (per laporan Gemini)
     - Polarity: Bull (euforia tinggi)
     - X engagement volume: spike (lonjakan mention pasca-NFT hype)
     - Dominant narrative on X: "Solana ETH-killer, musim NFT"
     - Notable X voices: @akun — inti pendapat — https://x.com/…
     - X evidence: https://x.com/…  (atau "no linkable X post found")
     - Sampled mood: retail euforia, sebagian skeptis pasca-outage
     - Evidence Level: HIGH
   ```
4. **X-only.** Fundamental context = "per laporan Gemini" (no external URL). Verifiable evidence = **x.com permalink**.
5. **No fabricated quotes/handles/permalinks.** Aggregate mood only when nothing can be linked.
6. `# 8` — ringkasan keyakinan + daftar X permalink yang dipakai (bukan URL berita eksternal).

## Grok prompt

The ready-to-paste Grok prompt is an **external working tool** (used inside Grok, not the framework) and is
kept in the maintainer's local files — intentionally **not** stored here. This brief keeps only the *contract*
the ingest depends on (the 8 sections + Input Formatting Contract above). Any Grok prompt must produce output
that conforms to that contract.

## Ingest & scope

- Save each report as `examples/Sentiment/<Project>.md` via `python3 tools/ingest.py` (drop docx in
  `doc_backup/inbox/sentiment/`). Anti-duplicate: existing sentiment dossiers are skipped.
- **Prioritise** projects where sentiment was decisive: meme, airdrop/points, hype-driven, and failures
  (Terra/FTX/StepN). Pure infra (Chainlink) needs less. Sentiment research is 1-per-1 (a Grok reset per
  project); the **ingest still batches** all resulting docx at once.
