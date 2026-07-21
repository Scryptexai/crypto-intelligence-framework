# Sentiment Brief (canonical)

The **maintainer's canonical prompt for the third document type: X-Engagement / Sentiment reports** (via
Grok, which has X access). A sentiment report is a **companion** to a fundamental deep dossier — it captures
how the community and the project *felt and communicated at the time*, per phase. Read this before ingesting
any sentiment report.

- **Fundamental** (`examples/CaseStudies/<Project>.md`) — what happened & why. Source: Gemini.
- **Sentiment** (`examples/Sentiment/<Project>.md`) — how it was perceived, per phase. Source: Grok/X.
- The two are **linked both ways** and kept in **separate modules** so contexts never mix.

**Why this is a moat:** historical point-in-time sentiment is ephemeral (posts deleted, algorithms change).
Capturing it now, triangulated and evidence-tagged, is hard to replicate. The alpha is the **divergence**
between fundamentals and sentiment — a class of signal fundamentals alone cannot give.

## Non-negotiable honesty rules (this is what keeps the moat credible)

1. **Separate VERIFIED anchors from SAMPLED sentiment.**
   - *Verified* = a documented event or an archived quote **with a link** (news, forum, Wayback, market data).
   - *Sampled* = aggregate mood characterised from X sampling (Grok). Never present sampled as fact.
2. **Never fabricate specific tweets/quotes.** If a specific post cannot be linked, describe the *aggregate
   mood* instead ("narasi dominan Q3-2021 …"). A made-up @user quote poisons the dataset.
3. **Triangulate.** ≥2 independent sources agreeing → `Evidence Level: HIGH`. Single source (Grok only) →
   `MEDIUM`/`LOW`.
4. **Time-stamp every phase.** Sentiment without a date is noise; align to `docs/TokenLifecycle/`.
5. **Note the bias.** X skews Retail/hype/English → strong for Retail & Community POV, weak for
   Institution & Developer. Say so.
6. **Provenance + capture date** on every section: `via Grok/X (captured <YYYY-MM-DD>)` vs `archived (URL)`.

## The 8 sections (input contract)

1. **Overview & Coverage** — project, periode yang dicakup, sumber (Grok/X + arsip berita/forum/market), metode, bias.
2. **Sentiment Timeline by Phase** — untuk tiap fase (pre-launch / testnet / TGE / +30d / +90d / momen krisis /
   current): `Polarity` (bull/bear/neutral + skala), `Engagement volume` (kasar), `Dominant narrative`,
   `Verified anchors` (event + URL), `Sampled mood` (agregat), `Evidence Level`.
3. **Community Voice** — dipisah: `Retail`, `KOL/Influencer`, `Builder/Developer`. Apa yang mereka katakan & rasakan.
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
3. **No tables** → nested `Label: Value` bullets. Per phase example:
   ```
   - Fase: TGE (Nov 2021)
     - Polarity: Bull (euforia tinggi)
     - Engagement volume: sangat tinggi
     - Dominant narrative: "Solana ETH-killer, musim NFT"
     - Verified anchor: Degenerate Ape mint Agu 2021 — <URL>; outage 14 Sep 2021 — <URL>
     - Sampled mood: retail euforia, sebagian skeptis pasca-outage
     - Evidence Level: HIGH
   ```
4. **Separate `Verified anchor:` (with URL) from `Sampled mood:`** in every phase. Non-negotiable.
5. **No fabricated quotes.** Aggregate mood only, unless a quote has an archive URL.
6. `# 8` sources as numbered `Title — URL`.

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
