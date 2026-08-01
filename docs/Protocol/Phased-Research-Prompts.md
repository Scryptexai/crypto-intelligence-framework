# Phased Research Prompts (Format v3)

## Policy note — why these live in the repo

`docs/Protocol/Deep-Research-Brief.md` states the paste-ready research prompt is kept external, in the
maintainer's local files, not in the repo. **The v3 phased prompts below are an explicit, scoped exception
(maintainer decision, 2026-07-25) — but the exception is about storage, not usage.** Actual usage is
unchanged: these are still pasted manually into Gemini (or another external research tool) exactly as before,
outside the repo, one phase at a time. What changes is only that a copy also lives here, so it (a) can't be
lost or accidentally deleted from a local machine, and (b) stays in the same place as, and in sync with, the
contract it implements (`Deep-Research-Brief.md`'s Format v3 section), the ontology it maps to, and the code
that ingests its output (`tools/ingest.py`) — one connected context instead of a prompt file sitting
disconnected from the pipeline it feeds. It is not a process change, and it does not make this file a
mandatory script to follow word-for-word forever — it's a backup with context, not new governance. The v1/v2
single-shot prompt is unaffected and stays external as before.

## How to use these

1. Pick a track: **Track A (Large/Anchor)** for projects with substantial history (Ethereum, Solana, BNB
   Chain, and similarly aged/complex projects) or **Track B (Small/Young)** for projects with thin history —
   pre-TGE, <1 year old, few entities. Track choice is a judgment call, not a hard rule; a "small" project that
   turns out to have surprising depth can graduate mid-research by picking up Track A's remaining phases.
2. **Focus on one project at a time through the whole pipeline before starting another** — see
   `examples/DatasetIndex.md` § "Phased Deep Research Queue" for the currently in-progress project and which
   phase is next. A finished foundation project is worth more than several half-finished ones.
3. Run each phase **in dependency order**. Before pasting a phase's prompt, paste a **Context Pack** as
   reference material — **not the full raw output of every prior phase.** Pasting all N-1 previous phases'
   full text into every later phase (a) grows without bound — by Phase 11 that's 10 full documents in one
   window — and (b) actively hurts quality: a model burying a fact of interest inside pages of unrelated
   prior narrative is more likely to drop or misplace it than one given a short, targeted reference (this is
   a documented LLM failure mode — recall degrades with irrelevant context volume, it isn't just a size
   limit). Each phase declares its **actual** dependencies, and only those go in the pack:
   - **Phase 1's own output is always included in full** — it's short (~20 single-line fields) and every
     later phase needs it.
   - From any other prior phase, include only an **index**, not the full text: entity names + types (from
     Phase 2), or event labels + dates (from Phase 3) — a one-line-per-item list the model can cross-reference
     names/dates against, not the full relationship/context/outcome prose behind each one. Include full prose
     from a specific prior phase only when the CURRENT phase's task genuinely requires it (e.g. Phase 9
     Behavioral needs Phase 3's full event bodies to analyze motive — an index of labels isn't enough there).
   - The maintainer running this doesn't have to hand-build these packs — they're produced alongside each new
     phase prompt (see `doc_backup/inbox/phased/<Project>/PROMPTS-LOG.md`, which logs the exact pack used).
   - For the last two phases (10 Knowledge Extraction, 11 Conflict Resolution), which legitimately need
     everything: use the **assembled dossier** (`./run.sh` / `tools/ingest.py --type phased` run against
     whatever phases are done so far) as the single context document instead of re-pasting every raw phase
     file separately — the tooling already exists to produce this, no reason to do it by hand.
3b. **Per-phase Context Pack — quick reference (Track A).** The rule in step 3 is general; this is what it
   resolves to for each phase, so you don't have to re-derive it each time (this was a real point of
   confusion running the pipeline for the first time on LayerZero — "which file do I attach for Phase 5?"):

   | Phase | Attach |
   |---|---|
   | 1 Foundation | (nothing — first phase) |
   | 2 Entity | Phase 1, full |
   | 3 Historical | Phase 1 full + Phase 2 index (names/types) |
   | 4 Technology | Phase 1 full + Phase 2/3 index |
   | 5 Financial | Phase 1 full + Phase 2/3/4 index |
   | 6 Token | Phase 1 full + Phase 2–5 index |
   | 7 Ecosystem | Phase 1 full + Phase 2–6 index |
   | 8 Market | Phase 1 full + Phase 2–7 index (+ Sentiment companion if it exists — see step 4) |
   | 9 Behavioral | Phase 1 full + Phase 3 **full** (motive analysis needs the actual event bodies, an index of labels isn't enough) + Phase 2/4–8 index |
   | 10 Knowledge Extraction | the **assembled dossier** (`./run.sh`), not individual phase files |
   | 11 Conflict Resolution | the **assembled dossier** (`./run.sh`) + your own running list of discrepancies noticed while drafting phases 1–10 (see "Seed the Conflict Resolution phase" below — don't rely on an open-ended "find conflicts" prompt alone) |

4. If the project already has a `examples/Sentiment/<Project>.md` companion (Grok/X), paste it as additional
   context for **Phase 8 (Market/Ecosystem) and the Conflict Resolution phase** — Gemini's research is
   secondary/aggregated evidence (what's been written about the project); Grok's is primary/live evidence
   (what the community is saying right now, with real post citations). A gap between the two — Gemini's
   sources say the community is positive, Grok's live scan says sentiment soured last week — is exactly the
   kind of `INKONSISTENSI` this pipeline exists to surface, not smooth over.
5. Export each phase's raw output as its own `.docx`, named `NN-<phasekey>.docx` with the **exact** phase
   key (`foundation`, `entity`, `history`, `technology`, `financial`, `token`, `ecosystem`, `market`,
   `behavioral`, `knowledge`, `conflict`) — e.g. `03-history.docx`, not `03-historical.docx` (a
   near-miss like that silently dropped a whole phase from LayerZero's first dossier assembly before this
   convention existed). For **new projects**, drop all of a project's phase files into
   `data_project/<project>/` (lowercase, e.g. `data_project/arbitrum/`) and run `./run.sh` —
   `tools/ingest.py`'s hardened `data_project` mode assembles them automatically, no LLM needed for that
   step, and hard-fails with a clear reason (not a silent partial dossier) if a filename doesn't match or
   content verification fails. See `tools/README.md` for the full contract. (The older
   `doc_backup/inbox/phased/<ProjectName>/` convention, fuzzy filename matching, no content verification —
   still works for in-flight projects but should not be used for new ones.)
6. Every prompt below shares the same closing/format rules — defined once, not repeated per phase. Every
   phase output must follow the literal template given (field names, order) — a template exists specifically
   so output is comparable across projects instead of free-form and inconsistent.

## Shared rules (apply to every phase prompt)

**Language note:** the prompt bodies below (§Track A/B) and this rules block are written in **Bahasa
Indonesia**, because that's what was actually sent and actually worked — LayerZero's real Phase 1 attempt
was sent in English and failed (came back as an unparseable narrative report, had to be reformatted from
scratch); every phase from Phase 2 onward was drafted natively in Indonesian and succeeded. This is not a
stylistic preference, it's what's evidenced in `doc_backup/inbox/phased/LayerZero/PROMPTS-LOG.md`. Keep
these paste-ready blocks in Indonesian when updating this file — don't drift back to English drafts.

Append this block to **every** phase prompt before sending it:

```
ATURAN FORMAT (berlaku untuk seluruh jawaban):
- Tulis dalam BAHASA INDONESIA. Yang TIDAK diterjemahkan: nama produk/teknologi (Ultra Light Node, DVN,
  OFT, Proof-of-Donation), nama orang, nama perusahaan, nama chain, dan URL. Menerjemahkan istilah teknis
  membuatnya tidak bisa dicocokkan dengan dossier project lain.
- Ikuti template output yang diberikan untuk fase ini PERSIS — label field yang sama, urutan yang sama.
  Jangan reformat jadi prosa, jangan ganti nama field, jangan urutkan ulang. Bentuk yang konsisten lintas
  project adalah tujuannya; jawaban bebas-bentuk tidak bisa dibandingkan nanti.
- Output berupa bullet "Label: Isi". JANGAN GUNAKAN TABEL SAMA SEKALI — bahkan untuk data yang
  "terstruktur" sekalipun. Tabel Word bisa selamat lewat proses ekstraksi tapi berubah jadi bentuk
  dua-baris-per-fakta yang janggal; daftar bullet datar tidak begitu.
- Satu fakta per baris. Tanggal lengkap, angka dengan satuan. Jangan pernah membulatkan atau menghilangkan
  angka.
- **Sebuah field TIDAK PERNAH berupa paragraf.** Kalau isi yang mau ditulis di bawah satu label lebih dari
  ~2 kalimat, WAJIB dipecah jadi sub-bullet — satu klaim per sub-bullet, masing-masing diakhiri Evidence
  Level + sumbernya sendiri. (Pelajaran dari kegagalan nyata: beberapa fase awal LayerZero menulis satu
  paragraf raksasa penuh sinonim di bawah satu label dengan satu sitasi di ujung — atau tanpa sitasi sama
  sekali — dan semua jejak sumbernya hilang dalam prosesnya. Fase lain yang menulis blok pendek berulang
  per-item TIDAK gagal seperti ini. Bedanya ada di ukuran blok: sitasi-sambil-jalan selamat,
  sitasi-setelah-paragraf-panjang tidak. Jangan ulangi kegagalan itu di jawabanmu.)
- JANGAN mengarang. Kalau sesuatu tidak diketahui atau tidak dapat diverifikasi, tulis "tidak diketahui" —
  jangan menebak, jangan menyimpulkan diam-diam, jangan mengisi kekosongan dengan klaim yang terdengar
  masuk akal tapi tidak bersumber.
- Kalau tidak menemukan sumber untuk sebuah fakta, CARI LEBIH KERAS dulu sebelum menyerah — pakai fallback
  "tidak dapat diverifikasi" di MAKSIMAL 1-2 field di seluruh jawabanmu. Kalau kamu memakainya lebih dari
  itu, kamu belum cukup keras mencari, bukan benar-benar menemui project yang tidak bisa disumberkan.
  (Pelajaran dari kegagalan nyata: satu percobaan memakai fallback ini di SEMUA field alih-alih mencari —
  hasilnya lebih buruk daripada cakupan sebagian dengan sitasi asli.)
- Angka atau persentase spesifik dari satu sumber saja BUKAN otomatis benar — berlaku khusus untuk
  tokenomics (persentase TGE, status fee-switch, ukuran treasury). Cross-check klaim kuantitatif yang
  krusial ke sumber primer project (blog resmi, halaman governance, data on-chain) sebelum melaporkannya
  sebagai fakta. (Pelajaran dari kegagalan nyata: sebuah angka unlock TGE yang fabricated dari sumber
  sekunder kualitas rendah tidak terbantahkan sampai ada pass independen yang menangkapnya.)
- Kalau sebuah klaim diperdebatkan oleh sumber berbeda, catat eksplisit ("Sumber A bilang X, Sumber B
  bilang Y") — jangan diam-diam memilih salah satu.
- Sitasi WAJIB menempel di SETIAP fakta, di baris yang sama — BUKAN daftar pustaka di akhir tanpa kaitan
  per-fakta. Daftar sumber di bawah tanpa keterkaitan ke fakta individual TIDAK BISA DITERIMA — itu membuat
  setiap klaim individual tidak bisa diverifikasi, satu hal yang tidak bisa ditoleransi kerangka kerja ini.
- Beri Evidence Level — HIGH (beberapa sumber independen sepakat) / MEDIUM (satu sumber kredibel) / LOW
  (inferensi, sumber tunggal lemah, atau diperdebatkan) — di setiap klaim signifikan, bukan cuma di fase
  Conflict Resolution.
- Gabungannya, setiap baris fakta terlihat seperti: "Amount: $6.5M (HIGH) [Messari, https://...]".
- JANGAN menganalisis, menyimpulkan, atau berspekulasi soal kausalitas di luar yang diminta tugas fase ini
  — fase-fase berikutnya yang menangani sintesis; tugas fase ini lebih sempit dari itu.
- Awali output dengan: PROJECT: <Nama>
- Akhiri output dengan heading "Open Threads" diikuti daftar bullet hal-hal yang kamu temukan tidak pasti,
  bertentangan, atau perlu digali lebih dalam — serahkan ke fase berikutnya, jangan menebak sudah selesai.
```

## Known failure patterns (learned running this pipeline end-to-end on LayerZero, 2026-07)

LayerZero is the first project to complete all 11 Track A phases — several phases needed 2–3 attempts before
producing a usable result. These are the concrete failure modes hit, so the next project doesn't re-discover
them the slow way. `tools/ingest.py`'s `data_project` mode now hard-checks some of these automatically
(`validate_phase_content()` — see `tools/README.md`), but the model-facing prompt guidance below still
matters since the automated check can only catch a defect after the fact, not prevent the model from
producing it.

- **Escape-hatch overuse.** When a citation-search instruction is hard, some models apply a
  "cannot re-verify source" fallback phrase to *every* field instead of actually searching — Phase 3's
  second attempt did this to all 13 pre-existing events, with zero real search attempted. If you see this
  starting, add an explicit cap to the prompt: *"Use the 'cannot verify' fallback on at most 1–2 fields
  total — if you're about to use it more than that, you are not searching hard enough; try harder before
  falling back."* `tools/ingest.py`'s `validate_phase_content()` now flags this automatically when the
  fallback phrase appears as often or more than real Evidence Level tags.
- **Two failed attempts on the same instruction from the same model → switch model or method, don't
  re-prompt a third time the same way.** Phase 3 and Phase 6 each failed twice on citation attachment
  before a *different* approach (a direct citation-mapping research pass instead of re-prompting the
  research model) succeeded decisively. A third attempt with the same model and a slightly-reworded prompt
  is unlikely to fix a failure mode the model has now repeated twice.
- **A reformat/patch pass can silently drop existing sections even when told not to.** Phase 4's citation
  reformat dropped the "Open Threads" and full bibliography sections despite the prompt's explicit
  "don't delete facts" rule. When reformatting an existing draft (not researching from scratch), diff the
  reformatted output's section list against the original's before accepting — don't just spot-check content
  quality.
- **A single source's specific number/percentage is not automatically true, especially for tokenomics.**
  Phase 6's first attempt confidently reported a 25% TGE unlock figure that turned out to be fabricated (the
  real figure, confirmed against the project's own primary sources, was ~13.5%). Any load-bearing
  quantitative claim — TGE %, fee-switch status, treasury size — should be corroborated against a primary
  source (official blog/governance page) before being accepted, not taken from a single secondary mention.
- **Seed the Conflict Resolution phase with a running list, don't rely on a fully open "find conflicts"
  prompt alone.** While drafting phases 1–10, keep a running note of numbers/claims that looked shaky or
  inconsistent across phases (differing figures for the same metric, an Open Thread that never got resolved
  by a later phase). Feed that list into Phase 11 explicitly, asking the model to verify each one against the
  actual assembled dossier text (not just copy the list back) *and* find anything else on its own. LayerZero's
  Phase 11 caught 12 seeded items plus 17 more found independently — a purely open-ended prompt would likely
  have missed some of the seeded ones, since a model scanning a 2000+ line assembled dossier cold doesn't
  reliably surface every discrepancy without a checklist to verify against.

---

## Track A — Large / Anchor Projects (full 11 phases)

Use for projects with substantial history and complexity: Ethereum, Solana, BNB Chain, Avalanche, Polkadot,
Cosmos, LayerZero, and comparable anchor projects. Each phase below is a separate prompt — paste the prior
phase's finished output as context before running the next one.

### Phase 1 — Foundation Intelligence
```
Kamu adalah investigator riset crypto yang sedang membangun dossier fondasi faktual untuk <NAMA PROJECT>.
Fase ini HANYA mengumpulkan FAKTA — tidak ada analisis, interpretasi, atau "kenapa".

Isi template PERSIS ini (tulis "tidak diketahui" untuk apa pun yang tidak dapat diverifikasi — jangan
menebak):

PROJECT: <Nama>
Official Name: <nilai>
Symbol: <nilai>
Category: <nilai — spesifik, contoh "cross-chain messaging / interoperability", bukan cuma "infra">
Founding Entity: <nama badan hukum, yurisdiksi>
Founders: <nama1 (peran); nama2 (peran); ... — atau "anonim/pseudonim — <handle>">
Core Team: <ukuran/nama yang bisa diverifikasi, atau "tidak diungkap">
Country: <nilai>
Launch Date - Testnet: <tanggal atau "n/a">
Launch Date - Mainnet: <tanggal atau "n/a">
Launch Date - TGE: <tanggal atau "pre-TGE">
Main Products: <daftar dipisah titik-koma>
Official Website: <url>
Repository: <url>
Documentation: <url>
Social - X/Twitter: <handle>
Social - Discord: <invite/handle>
Social - Telegram: <handle>
Block Explorer: <url>
Token Contract: <alamat, chain — atau "belum di-deploy">
Chain(s): <nilai>
Ecosystem: <nilai>

Open Threads
- <hal yang masih belum pasti>
```

### Phase 2 — Entity Intelligence
```
Menggunakan output Foundation Intelligence (Phase 1) di atas sebagai konteks, bangun ENTITY GRAPH untuk
<NAMA PROJECT> — SEMUA organisasi, orang, investor, exchange, partner, protokol, developer, produk, DAO,
badan pemerintah, media, atau lembaga riset yang terhubung ke project ini. Ini adalah PEMETAAN HUBUNGAN,
bukan analisis sebab-akibat — catat SIAPA terhubung dan BAGAIMANA, bukan kenapa atau dampaknya (itu tugas
fase Behavioral nanti). Jangan lewatkan entitas yang terlihat kecil/minor.

Untuk SETIAP entitas, ulangi blok ini:

Entity: <nama>
Type: <Organization|Person|Investor|Foundation|Exchange|Partner|Protocol|Developer|Product|DAO|Government|Media|Research Lab>
Relationship: <bentuk hubungannya, contoh: "memimpin ronde Series A", "core contributor 2021-2023">
Period: <mulai–selesai, atau "mulai–sekarang", atau "tidak diketahui">
Exposure Type: <financial-collateral|technical-integration|liquidity-dependency|shared-investor-only|narrative-correlated-only|unknown>
  (financial-collateral = memegang/pernah memegang aset project ini sebagai treasury/jaminan;
  technical-integration = bergantung pada infrastruktur project ini agar berfungsi (atau sebaliknya);
  liquidity-dependency = tempat likuiditas utama; shared-investor-only = cuma berbagi investor yang sama,
  tanpa hubungan operasional; narrative-correlated-only = cuma satu label sektor yang sama. Pilih kategori
  PALING KUAT yang berlaku, bukan yang paling gampang dipilih.)
Evidence: <sumber>
---

Open Threads
- <hal yang masih belum pasti>
```

### Phase 3 — Historical Intelligence
```
Menggunakan output Foundation dan Entity Intelligence (Phase 1-2) di atas sebagai konteks, bangun LINI MASA
KRONOLOGIS untuk <NAMA PROJECT> — ini adalah TULANG PUNGGUNG FAKTUAL yang dirujuk semua fase berikutnya.
Cakup seluruh sejarah dari pendirian sampai sekarang; JANGAN lewatkan event yang tidak nyaman (gangguan
layanan, kontroversi, inisiatif yang gagal, sengketa governance).

Untuk SETIAP event besar, berurutan berdasarkan tanggal, ulangi blok ini:

Date: <YYYY-MM-DD atau presisi terbaik yang tersedia>
Event: <label singkat>
Trigger: <penyebab langsung yang bisa diobservasi — bukan spekulasi soal motif>
Context Snapshot (per tanggal ini): Industry state: <...> | Competitor state: <...> | Tech maturity: <...>
  | Macro conditions: <...> | Hunter/user population (kalau relevan buat airdrop): <...> | VC climate: <...>
  | Narrative: <...>
  (Lewati sub-field yang benar-benar tidak relevan, tapi JANGAN lewati baris Context-nya sama sekali — ini
  yang membuat fase-fase berikutnya tidak salah mencocokkan pola event ini ke era yang tidak sebanding.)
Decision: <apa yang diputuskan/dilakukan>
Execution: <bagaimana persisnya dijalankan secara operasional — beda dari keputusannya sendiri>
Short-term Outcome: <efek dalam rentang minggu-bulan>
Long-term Outcome: <efek dalam horizon lebih panjang, atau "terlalu dini untuk dinilai">
Evidence: <sumber>
---

Open Threads
- <hal yang masih belum pasti>
```

### Phase 4 — Technology Intelligence
```
Menggunakan output fase-fase sebelumnya sebagai konteks, laporkan PROFIL TEKNOLOGI <NAMA PROJECT>. Teknologi
SAJA — jangan bahas token/market/finansial (itu tugas fase lain).

Architecture: <nilai>
Consensus Mechanism: <nilai atau "n/a">
VM / Execution Environment: <nilai>
Languages/Frameworks: <nilai>
Security Model: <nilai>
Audit History: <auditor — tanggal — cakupan; ulangi per audit, atau "tidak diungkap">
Scalability Approach: <nilai>
Known Limits: <nilai>
Protocol Evolution: <nama upgrade — tanggal — apa yang berubah secara teknis; ulangi per upgrade>
Current Roadmap: <nilai>
Novelty Assessment: <apa yang benar-benar baru vs. adaptasi dari yang sudah ada, dengan dasarnya>

Open Threads
- <hal yang masih belum pasti>
```

### Phase 5 — Financial Intelligence
```
Menggunakan output fase-fase sebelumnya sebagai konteks, laporkan PROFIL FINANSIAL <NAMA PROJECT>. Ekonomi
pendanaan/revenue — BUKAN tokenomics (itu tugas Phase 6).

Untuk SETIAP ronde pendanaan, ulangi blok ini:
Funding Round: <tipe, contoh Seed/Series A>
  Date: <nilai>  Amount: <nilai + mata uang>  Lead Investor: <nilai>
  Participating Investors: <nilai>  Valuation: <nilai atau "tidak diungkap">
---

Lalu, sekali saja:
Treasury Size: <nilai atau "tidak diungkap">
Treasury Composition: <nilai>
Revenue Model: <nilai>
Revenue Figures: <nilai + tanggal, atau "tidak diungkap">
Burn Rate: <nilai, atau "estimasi X — dasar perhitungan: ...", atau "tidak diungkap">
Token Sale Structure: <syarat & jumlah public/private — BUKAN persentase alokasi, itu tugas Phase 6>
Runway Estimate: <nilai + dasar perhitungan, atau "tidak dapat dihitung">

Open Threads
- <hal yang masih belum pasti>
```

### Phase 6 — Token Intelligence
```
Menggunakan output fase-fase sebelumnya sebagai konteks, laporkan PROFIL TOKEN/TOKENOMICS <NAMA PROJECT>.
Kalau masih pre-TGE, tandai SETIAP field di bawah secara eksplisit sebagai "rencana" dan tandai bagian yang
masih belum diputuskan. INGAT aturan cross-check di ATURAN FORMAT — angka spesifik seperti persentase TGE
unlock atau status fee-switch WAJIB dicek ke sumber primer sebelum dilaporkan.

Total Supply: <nilai>
Supply Type: <fixed|inflationary>
Distribution: Community <%>, Team <%>, Investors <%>, Treasury <%>, Ecosystem <%>, Other <label:%>
Allocation - Team: <cliff, vesting>
Allocation - Investors: <cliff, vesting>
Allocation - <kategori lain>: <cliff, vesting>
TGE Unlock: <% dari total supply + kategori mana saja>
Emission Schedule: <nilai atau "n/a — fixed supply">
Utility: <daftar bullet>
Governance Mechanism: <nilai>
Inflation/Deflation: <nilai>
Burn Mechanism: <nilai atau "tidak ada">
Holder Concentration: <nilai atau "belum dapat diukur">
Notable Token Flow: <nilai atau "n/a">
Status: <live|planned/pre-TGE>

Open Threads
- <hal yang masih belum pasti>
```

### Phase 7 — Ecosystem Intelligence
```
Menggunakan output Foundation Intelligence (Phase 1) dan indeks entitas dari Phase 2 di atas sebagai
konteks, bangun PROFIL EKOSISTEM/HUBUNGAN EKSTERNAL <NAMA PROJECT>. Bedakan tegas "integrasi diumumkan" vs
"integrasi live dan benar-benar dipakai" — ini penekanan paling penting di fase ini.

Kalau project ini terhubung ke banyak chain/dApp (skala besar): JANGAN coba mendaftarkan semuanya satu per
satu. Batasi blok "Integration Partner" HANYA pada partner yang benar-benar SIGNIFIKAN (chain/dApp dengan
TVL atau volume tinggi, atau yang sudah muncul di fase-fase sebelumnya) — untuk yang jumlahnya masif dan
tidak signifikan secara individual, rangkum saja secara agregat di field yang relevan (Developer
Ecosystem / Applications Built On It).

Untuk SETIAP integration partner (yang signifikan), ulangi blok ini:
Integration Partner: <nama>
  What it does: <nilai> (Evidence Level) [sumber]
  Status: <live|announced-only> (Evidence Level) [sumber]
---

Lalu, sekali saja (setiap baris tetap wajib punya sitasinya sendiri):
Developer Ecosystem: <nilai>
Applications Built On It: <daftar>
Wallet Support: <daftar>
Exchange Listings: <ringkasan tier/breadth — di luar yang sudah tercatat di Entity Intelligence>
Oracle Integrations: <daftar>
Bridge Integrations: <daftar>
Infra/Tooling Providers: <daftar>
Community Size/Activity: <angka Discord/TG/forum + tanggal>

Open Threads
- <hal yang masih belum pasti>
```

### Phase 8 — Market Intelligence
```
Menggunakan output fase-fase sebelumnya sebagai konteks, laporkan PROFIL MARKET <NAMA PROJECT>. Market saja
— bukan KENAPA (itu tugas Behavioral Intelligence, fase berikutnya). Kalau ada companion
`examples/Sentiment/<Project>.md` (Grok/X) yang disertakan sebagai konteks, cross-check klaim
narasi/komunitasmu terhadap itu secara eksplisit.

Narrative(s): <nilai — catat mana yang diinisiasi project ini vs. cuma mengikuti>

Untuk SETIAP kompetitor/era, ulangi blok ini:
Competitor: <nama>   Era: <kapan mereka bersaing>   Positioning vs. them: <nilai>
---

Lalu, sekali saja:
Adoption Metrics: <metrik: nilai (tanggal); ulangi per metrik>
TVL History: <nilai: tanggal; ulangi titik infleksi penting, atau "n/a">
Volume History: <nilai: tanggal; ulangi titik infleksi penting>
Market Share: <nilai atau "tidak dapat dihitung">
Market Cycles Operated Through: <daftar, dengan tanggal dan efek yang teramati spesifik ke project ini>
Current Status: <growing|declining|stagnant|dormant|recovering> — basis: <observasi apa yang mendasari ini>

Open Threads
- <hal yang masih belum pasti, termasuk gap terhadap companion Sentiment kalau ada>
```

### Phase 9 — Behavioral Intelligence
```
Menggunakan SELURUH output fase sebelumnya sebagai konteks — TERUTAMA Historical, Financial, dan Token
Intelligence — fase ini adalah LAPISAN KAUSAL sesungguhnya dari kerangka kerja ini. Landaskan SETIAP jawaban
pada pernyataan publik, wawancara, pos governance, atau inferensi yang berdasar-kuat (label mana yang
dipakai); tulis "tidak diketahui" daripada berspekulasi tanpa dasar.

Untuk SETIAP decision event besar dari Historical Intelligence, ulangi blok ini:

Decision Event: <nama/tanggal, SAMA PERSIS dengan Historical Intelligence — salin persis, jangan parafrase>
  Motivation: <kenapa keputusan ini diambil, atau "tidak diketahui">
  Constraint: <apa yang membatasi opsi — runway, utang teknis, eksposur regulasi, ukuran tim — atau
    "tidak diketahui">
  Pressure: <kekuatan eksternal yang bekerja — ekspektasi VC, ancaman kompetitif, tuntutan komunitas —
    atau "tidak diketahui">
  Trade-off: <apa yang dikorbankan dengan memilih jalur ini, atau "tidak diketahui">
  Alternative(s) Considered: <apa lagi yang mungkin tersedia dan kenapa tidak dipilih, atau "tidak
    diketahui">
  Expectation vs. Actual: <apa yang tim harapkan terjadi vs. apa yang benar-benar terjadi, atau "tidak
    diketahui">
  Stakeholder Reactions:
    Founder: <reaksi/dampak atau "tidak ada reaksi signifikan">
    VC: <...>
    Retail: <...>
    Community: <...>
    Developer: <...>
    Institution: <...>
    Validator: <...>
    Builder: <...>
  Grounding: <statement | interview | governance post | inferensi berdasar-kuat — label yang mana>
---

Open Threads
- <hal yang masih belum pasti>
```

### Phase 10 — Knowledge Extraction
```
Menggunakan SELURUH output fase sebelumnya sebagai konteks, ekstrak PENGETAHUAN YANG DAPAT DIBACA MESIN dari
semua yang sudah dikumpulkan soal <NAMA PROJECT>. JANGAN menciptakan pattern dari satu tebakan tanpa dasar —
setiap kandidat pattern WAJIB bisa dilacak ke event/fakta konkret yang sudah dilaporkan.

POV Success-Matrix (vonis di TINGKAT PROYEK, bukan per-event):
  Founder: <success|failure|mixed — alasan — Evidence Level>
  VC: <...>
  Retail: <...>
  Community: <...>
  Developer: <...>
  Institution: <...>
  Validator: <...>
  Builder: <...>

Lessons Learned:
  Biggest mistake: <apa — untuk dihindari — kutip event spesifik>
  Biggest win: <apa — untuk ditiru — kutip event spesifik>

Entity/Relationship Addendum: <apa saja yang terlewat di Entity Intelligence, atau "tidak ada">

Untuk SETIAP kandidat pattern, ulangi blok ini. Ingat: pattern yang berguna adalah SHAPE keputusan yang bisa
berulang di project lain yang TIDAK terkait (lihat docs/Ontology/DecisionEvent.md) — field "Applies When"
harus menjelaskan KONDISI STRUKTURAL yang membuat pattern ini relevan di project lain, bukan sekadar
mengulang mekanisme spesifik project ini:
Pattern Candidate: <nama>
  Shape: <deskripsi shape keputusan yang bisa berulang>
  Drawn From: <event/fakta spesifik yang dikutip, dengan nama/tanggal>
  Applies When: <kondisi struktural yang membuat ini transfer ke project lain — bukan cuma mekanik>
---

Open Threads
- <hal yang masih belum pasti>
```

### Phase 11 — Conflict Resolution
```
Ini adalah pass MERGE-ONLY. JANGAN meriset apapun yang baru. Baca ulang SELURUH output fase sebelumnya untuk
<NAMA PROJECT> yang disertakan sebagai konteks — termasuk companion `examples/Sentiment/<Project>.md` kalau
ada — dan identifikasi SETIAP tempat di mana:
- Dua fase (atau dua sumber di dalam satu fase) melaporkan angka berbeda untuk fakta yang sama
- Sebuah klaim di satu fase dikontradiksi, dipersulit, atau diragukan oleh sesuatu di fase lain
- Narasi riset utama berbeda dari pembacaan live companion Sentiment/Grok (kalau ada) — misal sumber riset
  menggambarkan sentimen komunitas positif berdasarkan materi lama, tapi scan live X di companion Sentiment
  menunjukkan sentimen sudah memburuk, atau sebaliknya
- Sebuah "Open Thread" dari fase awal tidak pernah benar-benar diselesaikan oleh fase berikutnya

Untuk SETIAP konflik yang ditemukan, ulangi blok ini:
INKONSISTENSI: <apa yang berkonflik>
  Source A: <fase + nilai/klaim>
  Source B: <fase + nilai/klaim>
  Evidence Level: <LOW, atau MEDIUM kalau salah satu sumber jelas lebih otoritatif — jelaskan kenapa>
---

Kalau BENAR-BENAR tidak ada konflik ditemukan sama sekali, tulis eksplisit "No conflicts found." — jangan
dikosongkan begitu saja.

Open Threads
- <hanya kalau ada yang BENAR-BENAR masih belum terselesaikan bahkan setelah pass ini>
```

---

## Track B — Small / Young Projects (condensed, 7 phases)

Use for projects with thin history: pre-TGE, under ~1 year old, few entities, limited market data. The
dependency order and the enrichments above (Context Snapshot, Execution, Stakeholder Reactions, POV Matrix,
Evidence Level, Current Status) all still apply — condensing means merging phases, not dropping fields.

### Phase 1 — Foundation & Entity Intelligence
```
Kamu adalah investigator riset crypto yang sedang membangun dossier fondasi faktual untuk <NAMA PROJECT>,
sebuah project muda/kecil. HANYA FAKTA.

Part A — Foundation (isi template ini):
PROJECT: <Nama>
Official Name / Symbol / Category / Founding Entity / Founders / Core Team / Country: <masing-masing>
Launch Date - Testnet / Mainnet / TGE: <masing-masing, atau "n/a"/"pre-TGE">
Main Products / Website / Repository / Documentation / Socials / Explorer: <masing-masing>
Token Contract / Chain(s) / Ecosystem: <masing-masing>

Part B — Entity graph (ulangi per entitas):
Entity: <nama>   Type: <...>   Relationship: <...>   Period: <...>
Exposure Type: <financial-collateral|technical-integration|liquidity-dependency|shared-investor-only|narrative-correlated-only|unknown>
Evidence: <sumber>
---

Daftar entitas project muda wajar kalau pendek — laporkan persis apa yang ada, jangan dipaksa panjang.

Open Threads
- <hal yang masih belum pasti>
```

### Phase 2 — Historical Intelligence
```
Menggunakan output Foundation & Entity (Phase 1) di atas sebagai konteks, bangun LINI MASA KRONOLOGIS untuk
<NAMA PROJECT>. Project muda wajar kalau event-nya sedikit — laporkan yang ada secara lengkap, jangan
mengarang event pengisi.

Untuk SETIAP event, ulangi:
Date: <...>   Event: <...>   Trigger: <...>
Context Snapshot (per tanggal ini): Industry/Competitor/Tech maturity/Macro/Hunter-population/VC climate/
  Narrative — <isi yang relevan>
Decision: <...>   Execution: <...>
Short-term Outcome: <...>   Long-term Outcome: <... atau "terlalu dini untuk dinilai">
Evidence: <sumber>
---

Open Threads
- <hal yang masih belum pasti>
```

### Phase 3 — Technology Intelligence
```
Menggunakan output fase-fase sebelumnya sebagai konteks, laporkan PROFIL TEKNOLOGI <NAMA PROJECT>:
Architecture, Consensus (kalau relevan), VM/Execution Environment, Languages/Frameworks, Security Model,
Audit Status, Scalability Approach, Roadmap. Teknologi saja. Tegaskan mana yang sudah live vs. baru
rencana/diumumkan.

Open Threads
- <hal yang masih belum pasti>
```

### Phase 4 — Financial & Token Intelligence
```
Menggunakan output fase-fase sebelumnya sebagai konteks, laporkan profil FINANSIAL DAN TOKEN <NAMA PROJECT>
sekaligus — digabung karena pendanaan dan desain token project muda biasanya cukup tipis untuk dicakup
bersama.

Financial: Funding Round(s) (tipe/tanggal/jumlah/investor/valuasi, ulangi per ronde), Treasury, Revenue
Model, Token Sale Structure.

Token: Total Supply, Distribution %, Allocation cliffs/vesting per kategori, TGE Unlock %, Emission,
Utility, Governance Mechanism, Status (live|planned).

Kalau masih pre-TGE, tandai setiap field "rencana" secara eksplisit dan tandai bagian yang belum diputuskan.
INGAT aturan cross-check di ATURAN FORMAT untuk angka tokenomics.

Open Threads
- <hal yang masih belum pasti>
```

### Phase 5 — Ecosystem & Market Intelligence
```
Menggunakan output fase-fase sebelumnya sebagai konteks, laporkan profil EKOSISTEM DAN MARKET <NAMA
PROJECT> sekaligus.

Ecosystem: Integration Partner (nama, fungsinya, live|announced-only — ulangi per partner), Developer
Ecosystem, Wallet Support, Exchange Listings, Community Size/Activity.

Market: Narrative(s) (diinisiasi vs. cuma mengikuti), Competitors (ulangi per kompetitor/era), Adoption
Metrics (dengan tanggal), TVL/Volume kalau relevan, Current Status (growing|declining|stagnant|dormant|
recovering + basis).

Kalau ada companion `examples/Sentiment/<Project>.md`, cross-check klaim komunitas terhadap itu.

Open Threads
- <hal yang masih belum pasti, termasuk gap terhadap companion Sentiment>
```

### Phase 6 — Behavioral Intelligence
```
Menggunakan SELURUH output fase sebelumnya sebagai konteks — JANGAN dipersempit fase ini meski project-nya
masih muda, ini tetap lapisan kausal utamanya.

Untuk SETIAP decision event dari Historical Intelligence, ulangi:
Decision Event: <nama/tanggal>
  Motivation / Constraint / Pressure / Trade-off / Alternative(s) Considered / Expectation vs. Actual:
  <masing-masing, atau "tidak diketahui">
  Stakeholder Reactions: Founder/VC/Retail/Community/Developer/Institution/Validator/Builder —
  <masing-masing, atau "tidak ada reaksi signifikan">
  Grounding: <statement|interview|governance post|inferensi berdasar-kuat — label yang mana>
---

Open Threads
- <hal yang masih belum pasti>
```

### Phase 7 — Knowledge & Conflict Synthesis
```
Menggabungkan Knowledge Extraction dan Conflict Resolution jadi satu pass penutup.

Part A — Knowledge Extraction:
POV Success-Matrix: Founder/VC/Retail/Community/Developer/Institution/Validator/Builder — <vonis + alasan +
  Evidence Level, masing-masing>
Lessons Learned: Biggest mistake (untuk dihindari) / Biggest win (untuk ditiru) — kutip event spesifiknya.
Pattern Candidate (ulangi per kandidat): Name / Shape / Drawn From / Applies When.

Part B — Conflict Resolution (merge-only, JANGAN meriset baru; sertakan companion Sentiment kalau ada):
ulangi per konflik —
INKONSISTENSI: <apa yang berkonflik>   Source A: <...>   Source B: <...>   Evidence Level: <LOW|MEDIUM +
  kenapa>
---
Kalau tidak ada konflik ditemukan, tulis eksplisit "No conflicts found."

Open Threads
- <hanya kalau ada yang benar-benar masih belum terselesaikan>
```

## Track C — DeepSeek Methodology (v3.1, full 11 phases + Validation)

### Why DeepSeek instead of Gemini/Claude/Kimi/Qwen/GPT (maintainer decision, 2026-07-29)

Maintainer evaluated five options before settling on DeepSeek as the primary research model (first full run:
Arbitrum, `data_project/Arbitrum/`):

- **Gemini** (Track A/B above): loses context or drifts off the CIF goal across a long multi-phase run.
- **Claude**: strong, clear output, but limited to 2-3 deep-research runs per day — too slow for the target
  pace of roughly one project per session.
- **Kimi**: needs a paid account upgrade to reach a research-capable model.
- **Qwen**: research isn't robust enough — output comes back 50-70% summarized/fabricated rather than
  sourced.
- **GPT**: context window too limited for an 11-phase run, and output can't be exported or bulk-copied —
  only manual select-and-scroll copy, unworkable for a 500-1000-line report.
- **DeepSeek** (chosen): 100% free, no daily reset limit (paste straight into chat, no plugin/tool
  activation needed), and a 1M-token context window — the biggest factor, since it lets Phase 1 through
  Phase 11 be sent **sequentially in one continuous chat**, with no context loss and no `.docx` upload.

### How this changes the workflow vs. Track A's Context Pack

Track A/B above were designed around a **limited-context model** — step 3's "Context Pack" discipline
(attach an index, not the full prior phase, per the `3b` table) exists specifically to work around that
limit. DeepSeek's 1M-token window removes the constraint: run Track C phases **in one sitting, in the same
chat, back to back.** Export each phase's raw answer straight to `.docx` per the existing naming contract
(`NN-<phasekey>.docx`, § step 5 above) — the chat transcript itself is the Context Pack.

**Project name goes in ONCE, in Phase 1, and nowhere else (maintainer rule, applies to every future
project).** The 11 phases are one continuous, uninterrupted chat — not 11 separate conversations — so the
project name only needs to be stated the first time. Paste Phase 1's prompt with the project name filled
in; every phase from Phase 2 onward is pasted right after it in the same chat with no project-name field at
all — the model already knows which project it's researching from everything already in the conversation.
None of the Phase 2–11 prompts below carry a `PROJECT:` line for this reason — don't add one back when
using these for a new project, and don't re-type the project name into later phases either.

### Fixed vs. the original DeepSeek run (Arbitrum, 2026-07)

Prompts below are corrected against the actual set used to research Arbitrum: the redundant `PROJECT:
ARBITRUM` (or, in one case, `PROJECT: <NAMA PROJECT>`) header line was removed from every phase after Phase
1 — it violated the "state it once" rule above (a leftover from an earlier draft, not a deliberate design);
`04-technology`/`05-financial` were transposed at the file-name level (the content itself was already
correct, the file names weren't) — fixed, file names now match `PHASE_KEYS`; Phase 4's prompt additionally
had a duplicated, malformed placeholder line instead of a real instruction —
`menggunakan phase phase sebelum nya sebagai konteks` — removed, since the correctly-worded version of the
same instruction already exists a few lines later in the same prompt; Phase 3's stray extra blank lines
after the title normalized to match its siblings' spacing; Phase 11's title line given the same `#` heading
marker every other phase uses; Phase 11 also gained an explicit rule (§16 of its ATURAN UMUM) that the CIF
Score Calculation section must be computed *before* the CIF Manifest's summary numbers are written, and the
Manifest must copy its finished result — the real Arbitrum run computed the Manifest's `CIF SCORE: 88.2/100`
before the detailed calculation existed, then the detailed calculation section further down the same
document independently arrived at `81.6/100` from different Coverage/Conflict inputs, and nothing caught
the two final numbers disagreeing. No field, rule, or scope instruction beyond these was removed or
reworded — this is filename/placeholder/typo/sequencing-level cleanup only, verified against the real
generated `data_project/Arbitrum/*.docx` output (10/11 phases pass `tools/ingest.py`'s
`validate_phase_content` cleanly; the 11th, `11-conflict.docx`, is a separate open item — see below).

### Phase 1 — Foundation Intelligence
```
# PHASE 1 — FOUNDATION INTELLIGENCE

Kamu adalah investigator riset crypto yang sedang membangun dossier fondasi faktual untuk <NAMA PROJECT>.
Fase ini HANYA mengumpulkan FAKTA — tidak ada analisis, interpretasi, atau "kenapa".

Isi template PERSIS ini (tulis "tidak diketahui" untuk apa pun yang tidak dapat diverifikasi — jangan
menebak):

PROJECT: <Nama>
Official Name: <nilai>
Symbol: <nilai>
Category: <nilai — spesifik, contoh "cross-chain messaging / interoperability", bukan cuma "infra">
Founding Entity: <nama badan hukum, yurisdiksi>
Founders: <nama1 (peran); nama2 (peran); ... — atau "anonim/pseudonim — <handle>">
Core Team: <ukuran/nama yang bisa diverifikasi, atau "tidak diungkap">
Country: <nilai>
Launch Date - Testnet: <tanggal atau "n/a">
Launch Date - Mainnet: <tanggal atau "n/a">
Launch Date - TGE: <tanggal atau "pre-TGE">
Main Products: <daftar dipisah titik-koma>
Official Website: <url>
Repository: <url>
Documentation: <url>
Social - X/Twitter: <handle>
Social - Discord: <invite/handle>
Social - Telegram: <handle>
Block Explorer: <url>
Token Contract: <alamat, chain — atau "belum di-deploy">
Chain(s): <nilai>
Ecosystem: <nilai>

Open Threads
- <hal yang masih belum pasti>
```

### Phase 2 — Entity Intelligence
```
# PHASE 2 — ENTITY INTELLIGENCE

========================================================

PERAN

Anda adalah seorang OpenAI Deep Research yang bertugas membangun Entity Intelligence Dataset.

Fokus phase ini BUKAN menganalisis hubungan.

Fokus phase ini adalah mengidentifikasi seluruh ENTITAS yang memiliki keberadaan nyata dalam sejarah proyek.

Output phase ini akan menjadi daftar NODE untuk Graph Intelligence.

========================================================

CONTEXT DEPENDENCIES

WAJIB membaca hasil fase berikut sebagai konteks sebelum memulai.

1. 01-foundation

Gunakan untuk memahami Official Name, Symbol, Category, Founding Entity, Main Products, Chain(s), dan
Ecosystem.

========================================================

PERTANYAAN UTAMA

"Siapa saja entitas yang terlibat dalam proyek ini?"

BUKAN

"Bagaimana mereka saling berhubungan?"

========================================================

DEFINISI ENTITY

Entity adalah setiap individu, organisasi, institusi, protokol, aplikasi, chain, foundation, DAO, perusahaan, investor, regulator, maupun sistem yang memiliki identitas yang dapat dibedakan.

Contoh:

Founder

Core Team

Foundation

Company

Protocol

Blockchain

Bridge

Oracle

Exchange

Wallet

VC

Investor

Market Maker

Auditor

Government

DAO

Developer Group

Research Lab

Enterprise

Media

Community Organization

Application

Infrastructure Provider

========================================================

YANG TIDAK BOLEH DILAKUKAN

Jangan menjelaskan:

- hubungan antar entity
- partnership
- collaboration
- dependency
- pengaruh
- token
- teknologi
- timeline
- market
- governance
- analisis

Phase ini HANYA membuat katalog entity.

========================================================

UNTUK SETIAP ENTITY

## Nama

Nama resmi.

--------------------------------------------------------

## Alias

Nama lain apabila ada.

Jika tidak ada tulis:

Tidak ada.

--------------------------------------------------------

## Jenis

Pilih SATU kategori.

Founder

Person

Company

Foundation

Protocol

Blockchain

Application

Exchange

Wallet

Investor

VC

DAO

Government

Research Lab

Infrastructure Provider

Security

Auditor

Media

Community

Enterprise

Service Provider

Lainnya

--------------------------------------------------------

## Internal / External

Internal

atau

External

--------------------------------------------------------

## Status

Active

Inactive

Merged

Acquired

Defunct

Historical

Unknown

--------------------------------------------------------

## Fungsi Utama

Tuliskan fungsi utama entity terhadap proyek.

Contoh:

Funding

Development

Security

Liquidity

Infrastructure

Research

Governance

Community

Distribution

Compliance

Application

========================================================

## Deskripsi Singkat

Maksimum 2 kalimat.

Jangan membuat biografi.

Jangan membuat sejarah.

Hanya menjelaskan siapa entity tersebut.

========================================================

## Periode Keterlibatan

Contoh

2021–Sekarang

2022–2023

Tidak diketahui

========================================================

## Bukti

Cantumkan sumber.

Jika terdapat konflik sumber,
catat seluruh versi.

========================================================

SETELAH SEMUA ENTITY

Kelompokkan berdasarkan:

PERSON

FOUNDATION

COMPANY

PROTOCOL

CHAIN

INVESTOR

INFRASTRUCTURE

APPLICATION

SECURITY

DAO

GOVERNMENT

MEDIA

COMMUNITY

OTHER

========================================================

BUAT RINGKASAN

Total Entity

Internal

External

Unknown

========================================================

ATURAN

- JANGAN menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Setiap entity WAJIB memiliki bagian "Sources" yang berisi minimal satu sumber yang dapat diverifikasi.
- Jangan menggunakan hyperlink tersembunyi, ikon (🔗), atau anchor text; setiap sumber WAJIB ditulis sebagai URL lengkap (https://...) agar tetap terbawa saat disalin ke DOCX dan dapat diverifikasi.
- Jangan menjelaskan hubungan antar entity.
- Jangan membuat graph.
- Jangan menjelaskan alasan hubungan.
- Jangan membuat analisis.
- Jangan membahas teknologi.
- Jangan membahas timeline.
- Jangan membahas token.
- Jangan membahas market.
- Jangan membahas governance.
- Jangan membuat kesimpulan.
- Fokus hanya pada identifikasi entity.
- Satu entity hanya muncul SATU kali.
- Jika suatu entity memiliki banyak fungsi, tetap buat SATU entri dengan fungsi utama dan sebutkan fungsi tambahan secara singkat bila diperlukan.
```

### Phase 3 — Historical Intelligence
```
# PHASE 3 — HISTORICAL INTELLIGENCE

========================================================

PERAN

Anda adalah seorang AI Deep Research yang bertugas membangun Historical Intelligence Dataset.

Menggunakan output Foundation dan Entity Intelligence (Phase 1-2) di atas sebagai konteks

Fase ini bertujuan membangun timeline faktual lengkap mengenai seluruh perjalanan proyek.

Output fase ini akan menjadi Event Dataset yang digunakan oleh seluruh fase berikutnya.

========================================================

PERTANYAAN UTAMA

"Apa saja peristiwa penting yang terjadi sepanjang sejarah proyek ini?"

========================================================

RUANG LINGKUP

Cari seluruh peristiwa penting sejak proyek pertama kali muncul hingga saat ini.

Termasuk tetapi tidak terbatas pada:

• Founding

• Company Formation

• Whitepaper

• Testnet

• Mainnet

• Funding

• Acquisition

• Partnership Announcement

• Major Integration

• Protocol Upgrade

• Token Launch

• Governance Vote

• Security Incident

• Exploit

• Audit

• Fork

• Validator Update

• Major Product Release

• Ecosystem Expansion

• Exchange Listing

• Regulatory Action

• Lawsuit

• Leadership Change

• Foundation Formation

• Treasury Event

• Community Event

• Rebranding

• Shutdown

• Migration

• Major Failure

• Recovery

• Any historically significant event

========================================================

UNTUK SETIAP EVENT

## Event ID

Gunakan format:

EV-001

EV-002

EV-003

========================================================

## Date

Gunakan tanggal paling akurat.

YYYY-MM-DD

Jika hanya bulan diketahui:

YYYY-MM

Jika hanya tahun:

YYYY

========================================================

## Event Name

Nama singkat.

========================================================

## Event Type

Pilih SATU.

Founding

Funding

Launch

Technology

Governance

Security

Legal

Regulation

Partnership

Integration

Token

Market

Organization

Infrastructure

Community

Product

Ecosystem

Other

========================================================

## Description

Jelaskan fakta yang terjadi.

Maksimum 3 kalimat.

Jangan memberikan opini.

========================================================

## Participants

Daftar entity yang terlibat.

Gunakan nama yang sama dengan Phase 2.

========================================================

## Location

Jika relevan.

========================================================

## Status

Completed

Ongoing

Cancelled

Unknown

========================================================

## Immediate Result

Apa hasil langsung dari event tersebut.

Fakta saja.

========================================================

## Sources

Minimal satu URL lengkap.

Jangan menggunakan hyperlink tersembunyi.

Gunakan URL lengkap.

========================================================

SETELAH SELURUH EVENT

Kelompokkan berdasarkan tahun.

========================================================

BUAT RINGKASAN

Total Events

Founding

Funding

Technology

Security

Governance

Legal

Market

Other

========================================================

Open Threads

Tuliskan seluruh event yang masih memiliki konflik tanggal,
konflik sumber,
atau informasi yang belum dapat diverifikasi.

========================================================

ATURAN

- Fokus hanya pada kronologi faktual.
- Jangan menjelaskan motivasi.
- Jangan menjelaskan penyebab psikologis.
- Jangan menjelaskan trade-off.
- Jangan menjelaskan tekanan eksternal.
- Jangan menjelaskan strategi.
- Jangan menjelaskan analisis.
- Jangan membuat kesimpulan.
- Setiap event hanya muncul satu kali.
- Gunakan nama entity yang konsisten dengan Phase 2.
- Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Setiap event WAJIB memiliki bagian "Sources" yang berisi minimal satu sumber yang dapat diverifikasi.
- Jangan menggunakan hyperlink tersembunyi, ikon (🔗), atau anchor text; setiap sumber WAJIB ditulis sebagai URL lengkap (https://...) agar tetap terbawa saat disalin ke DOCX dan dapat diverifikasi.
```

### Phase 4 — Technology Intelligence
```
# PHASE 4 — TECHNOLOGY INTELLIGENCE

========================================================

PERAN

Anda adalah AI Deep Research yang bertugas membangun Technology Intelligence Dataset.

Menggunakan output fase-fase sebelumnya sebagai konteks

Fokus phase ini adalah mendokumentasikan seluruh karakteristik teknis proyek.

Output phase ini akan menjadi Technical Dataset yang dapat dibandingkan lintas proyek.

========================================================

PERTANYAAN UTAMA

"Bagaimana proyek ini dibangun dan bagaimana sistemnya bekerja secara teknis?"

========================================================

CAKUPAN

Laporkan seluruh aspek teknis yang dapat diverifikasi.

Jangan melakukan penilaian.

Jangan membandingkan.

Jangan memberikan opini.

========================================================

## System Architecture

Jelaskan arsitektur tingkat tinggi.

Contoh:

Layer 1

Layer 2

Rollup

Modular

Cross-chain Messaging

Oracle Network

Bridge

Appchain

Service Network

========================================================

## Core Components

Daftar seluruh komponen utama.

Contoh

Endpoint

DVN

Executor

Relayer

Sequencer

Validator

Indexer

Bridge

Messaging Layer

Settlement Layer

Execution Layer

Storage

Coordinator

dll.

Untuk setiap komponen:

Nama

Fungsi

Status

========================================================

## Consensus Mechanism

Jika ada.

Jika tidak relevan tulis

N/A

========================================================

## Execution Environment

Contoh

EVM

Move VM

SVM

WASM

CosmWasm

Native

========================================================

## Programming Languages

Daftar bahasa pemrograman utama.

========================================================

## Development Framework

SDK

Library

Framework

Toolchain

========================================================

## Security Model

Jelaskan bagaimana sistem diamankan.

Contoh

Validator

DVN

Multi Sig

Threshold Signature

Proof

Light Client

zk

TEE

========================================================

## Audit History

Untuk setiap audit

Auditor

Tanggal

Scope

Status

Source

========================================================

## Technical Upgrade History

Untuk setiap upgrade

Tanggal

Nama Upgrade

Deskripsi Singkat

Status

========================================================

## Current Technical Stack

Daftar teknologi yang digunakan.

Misalnya

Docker

Kubernetes

Rust

Solidity

Cosmos SDK

EigenLayer

Chainlink

IPFS

Arweave

EigenDA

dll.

========================================================

## Known Technical Limitations

Laporkan keterbatasan teknis yang dikonfirmasi oleh dokumentasi resmi,
audit,
atau developer.

Jangan membuat asumsi.

========================================================

## Official Technical Resources

Documentation

GitHub

Developer Docs

SDK

API

Whitepaper

Research Paper

Masing-masing berupa URL lengkap.

========================================================

BUAT RINGKASAN

Architecture

Core Components

Audit Count

Major Upgrade Count

========================================================

Open Threads

Tuliskan teknologi yang masih:

- belum didokumentasikan
- masih experimental
- masih roadmap resmi tetapi belum live
- memiliki informasi yang saling bertentangan

========================================================

ATURAN

- Fokus hanya pada aspek teknis yang dapat diverifikasi.
- Jangan membahas tokenomics.
- Jangan membahas pendanaan.
- Jangan membahas market.
- Jangan membahas partnership.
- Jangan membahas governance.
- Jangan membahas roadmap bisnis.
- Jangan memberikan penilaian seperti "lebih baik", "lebih inovatif", atau "lebih unggul".
- Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Setiap bagian WAJIB memiliki "Sources" dengan minimal satu URL lengkap yang dapat diverifikasi.
- Jangan menggunakan hyperlink tersembunyi, ikon (🔗), atau anchor text; setiap sumber WAJIB ditulis sebagai URL lengkap (https://...) agar tetap terbawa saat disalin ke DOCX dan dapat diverifikasi.
```

### Phase 5 — Financial Intelligence
```
# PHASE 5 — FINANCIAL INTELLIGENCE

========================================================

PERAN

Anda adalah AI Deep Research yang bertugas membangun Financial Intelligence Dataset.

Menggunakan output fase-fase sebelumnya sebagai konteks
01-foundation + 02-entity + 03-history + 04-technology

Fokus phase ini adalah mendokumentasikan seluruh informasi finansial proyek yang dapat diverifikasi.

Output phase ini akan menjadi Financial Dataset yang dapat dibandingkan lintas proyek.

========================================================

PERTANYAAN UTAMA

"Bagaimana proyek ini memperoleh, mengelola, dan menggunakan sumber daya keuangannya?"

========================================================

CAKUPAN

Laporkan seluruh informasi finansial yang tersedia dari sumber resmi maupun sumber kredibel.

Jangan membuat estimasi jika tidak didukung data.

Jangan memberikan opini.

========================================================

## Funding History

Untuk SETIAP ronde pendanaan

Funding Round

Date

Amount

Currency

Lead Investor

Participating Investors

Valuation

Funding Type

(Seed / Strategic / Private / Series A / Series B / Public Sale / Grant / Treasury Injection / Others)

Status

Completed

Announced

Cancelled

Sources

(URL lengkap)

--------------------------------------------------------

## Treasury

Current Treasury Size

Treasury Composition

Stablecoin Holdings

Native Token Holdings

Other Assets

Treasury Custodian

Jika tidak diketahui, tulis:

Tidak diungkap.

Sources

--------------------------------------------------------

## Revenue Model

Jelaskan seluruh sumber pendapatan yang telah dikonfirmasi.

Contoh

Protocol Fees

Subscription

Bridge Fees

Licensing

Validator Rewards

Staking Fees

MEV

Enterprise Service

Treasury Yield

Grant

Lainnya

Untuk setiap revenue stream

Nama

Status

Live

Planned

Discontinued

Sources

--------------------------------------------------------

## Revenue History

Jika tersedia

Tanggal

Revenue

Period

Sources

Jika tidak tersedia

Tuliskan

Tidak diungkap.

--------------------------------------------------------

## Fundraising Mechanism

Jelaskan bagaimana proyek memperoleh modal.

Contoh

VC Funding

Private Sale

Public Sale

Grant

Foundation

DAO Treasury

Protocol Revenue

Bootstrapping

--------------------------------------------------------

## Token Sale

Jika ada

Private Sale

Public Sale

Launchpad

Auction

Community Sale

Tanggal

Status

Sources

Catatan:

Jangan membahas distribusi token maupun vesting.
Itu adalah Phase 6.

--------------------------------------------------------

## Financial Dependencies

Daftar pihak yang menjadi sumber pendanaan utama.

Contoh

VC

Foundation

Grant Program

Revenue

DAO

Sources

--------------------------------------------------------

## Financial Risk

Laporkan HANYA risiko finansial yang dikonfirmasi oleh:

- laporan resmi
- governance
- audit
- disclosure
- regulator

Contoh

Treasury Concentration

Revenue Decline

Funding Dependency

Debt

Legal Financial Risk

Jangan membuat opini.

--------------------------------------------------------

## Official Financial Resources

Official Blog

Transparency Report

Treasury Dashboard

Governance

Messari

Token Terminal

DefiLlama

CryptoRank

Whitepaper

Semua berupa URL lengkap.

========================================================

BUAT RINGKASAN

Total Funding Raised

Funding Rounds

Treasury Status

Revenue Sources

Revenue Availability

========================================================

Open Threads

Tuliskan seluruh informasi finansial yang:

- belum dipublikasikan
- memiliki konflik angka
- tidak dapat diverifikasi
- masih berubah

========================================================

ATURAN

- Fokus hanya pada data finansial yang dapat diverifikasi.
- Jangan menghitung Burn Rate sendiri.
- Jangan menghitung Runway sendiri.
- Jangan memperkirakan valuasi jika tidak diumumkan.
- Jangan membahas tokenomics, distribusi token, vesting, maupun utilitas token.
- Jangan memberikan opini mengenai kesehatan finansial proyek.
- Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Setiap bagian WAJIB memiliki "Sources" dengan minimal satu URL lengkap yang dapat diverifikasi.
- Jangan menggunakan hyperlink tersembunyi, ikon (🔗), atau anchor text; setiap sumber WAJIB ditulis sebagai URL lengkap (https://...) agar tetap terbawa saat disalin ke DOCX dan dapat diverifikasi.
```

### Phase 6 — Token Intelligence
```
# PHASE 6 — TOKEN INTELLIGENCE

========================================================

PERAN

Anda adalah OpenAI Deep Research yang bertugas membangun Token Intelligence Dataset.

Fase ini hanya berfokus pada desain, distribusi, utilitas, ekonomi, dan tata kelola token.

Output fase ini akan menjadi Token Dataset yang dapat dibandingkan secara konsisten antar proyek.

========================================================

CONTEXT DEPENDENCIES

Sebelum memulai riset, baca dan gunakan seluruh dokumen berikut sebagai konteks.

WAJIB

1. 01-foundation

Gunakan untuk memahami:

- Official Name
- Symbol
- Category
- Founding Entity
- Main Products
- Chain(s)
- Ecosystem
- Launch Date
- Status Project

--------------------------------------------------------

2. 02-entity

Gunakan untuk memahami:

- Foundation
- Investor
- VC
- DAO
- Exchange
- Market Maker
- Treasury Manager
- Governance Entity
- Token Issuer

Pastikan seluruh nama entity tetap konsisten.

--------------------------------------------------------

3. 03-history

Gunakan untuk memahami:

- Historical Event
- Funding Event
- Governance Event
- TGE Event
- Upgrade
- Treasury Event
- Token Related Event

Gunakan Event ID apabila merujuk ke event tertentu.

--------------------------------------------------------

4. 04-technology

Gunakan untuk memahami:

- Technical Architecture
- Consensus
- Validator
- Staking
- Protocol Fee
- Security Model
- Burn Mechanism
- Technical Dependencies

Bagian ini digunakan untuk memahami utilitas token secara teknis.

--------------------------------------------------------

5. 05-financial

Gunakan untuk memahami:

- Funding History
- Private Sale
- Public Sale
- Treasury
- Revenue Model
- Financial Dependencies
- Token Sale History

Bagian ini menjadi referensi utama apabila terdapat hubungan antara token dan pendanaan.

========================================================

PRIORITAS REFERENSI

Jika terjadi konflik antar dokumen gunakan prioritas berikut.

Priority 1

Dokumentasi resmi project

Priority 2

Whitepaper

Priority 3

Governance

Priority 4

Foundation / Blog Resmi

Priority 5

GitHub

Priority 6

Dashboard resmi

Priority 7

Sumber pihak ketiga terpercaya

Jika konflik tidak dapat diselesaikan,

JANGAN memilih salah satu.

Laporkan seluruh versi pada bagian Open Threads.

========================================================

PERTANYAAN UTAMA

"Bagaimana desain token proyek ini dibangun dan bagaimana token tersebut berfungsi di dalam ekosistem?"

========================================================

RUANG LINGKUP

Laporkan seluruh informasi token yang dapat diverifikasi.

Jangan membuat asumsi.

Jangan melakukan analisis.

Jangan membandingkan dengan proyek lain.

========================================================

## Token Information

Official Token Name

Symbol

Token Standard

Blockchain

Contract Address

Decimals

Status

(Live / Planned / Pre-TGE)

Sources

--------------------------------------------------------

## Supply

Maximum Supply

Total Supply

Circulating Supply

Initial Supply

Supply Type

(Fixed / Inflationary / Dynamic)

Sources

--------------------------------------------------------

## Distribution

Community

Team

Investors

Foundation

Treasury

Ecosystem

Advisors

Other

Jika Pre-TGE,

tandai sebagai

Planned.

Sources

--------------------------------------------------------

## Vesting Schedule

Untuk setiap kategori

Category

Cliff

Vesting

Unlock Frequency

Current Status

Sources

--------------------------------------------------------

## TGE

TGE Date

Initial Unlock

Unlocked Categories

Launch Platform

Status

Sources

--------------------------------------------------------

## Utility

Untuk setiap utilitas token

Utility

Deskripsi

Status

(Live / Planned)

Sources

Contoh

Governance

Gas

Staking

Validator

Security

Fee Payment

Incentive

Reward

Collateral

Liquidity

========================================================

## Governance

Governance Model

Voting System

Voting Power

Delegation

Proposal System

Treasury Governance

Status

Sources

========================================================

## Inflation / Deflation

Inflation Mechanism

Emission Schedule

Burn Mechanism

Buyback

Supply Reduction

Status

Sources

========================================================

## Holder Distribution

Top Holder Concentration

Foundation Holding

Investor Holding

Treasury Holding

Community Holding

Whale Concentration

Sources

========================================================

## Major Token Events

Untuk setiap event

Date

Event

Description

Status

Related Historical Event ID

Sources

========================================================

## Official Token Resources

Official Documentation

Whitepaper

Governance

Explorer

Contract

GitHub

Dashboard

Semua harus berupa URL lengkap.

========================================================

BUAT RINGKASAN

Status

Supply Type

Total Supply

Distribution Categories

Utility Count

Governance

Major Token Events

========================================================

Open Threads

Tuliskan seluruh informasi token yang:

- belum dipublikasikan
- memiliki konflik angka
- memiliki konflik sumber
- belum dapat diverifikasi
- masih berupa proposal
- masih menunggu governance

========================================================

ATURAN

- Fokus hanya pada informasi token yang dapat diverifikasi.
- Jangan membahas pendanaan perusahaan kecuali berkaitan langsung dengan token.
- Jangan membahas market, harga, volume, atau sentimen.
- Jangan membahas analisis investasi.
- Jangan memberikan opini mengenai tokenomics.
- Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Setiap bagian WAJIB memiliki "Sources" yang berisi minimal satu URL lengkap yang dapat diverifikasi.
- Jangan menggunakan hyperlink tersembunyi, ikon (🔗), atau anchor text; setiap sumber WAJIB ditulis sebagai URL lengkap (https://...) agar tetap terbawa saat disalin ke DOCX dan dapat diverifikasi.
- Gunakan nama Entity yang sama persis dengan Phase 2.
- Gunakan Event ID yang sama persis dengan Phase 3 apabila merujuk pada suatu peristiwa.
- Jika terdapat perbedaan informasi antara dokumen konteks dan hasil riset terbaru, JANGAN memilih salah satu secara sepihak. Laporkan seluruh versi beserta sumbernya pada bagian Open Threads untuk diverifikasi pada Phase 11 (Conflict Resolution).
```

### Phase 7 — Ecosystem & Dependency Intelligence
```
# PHASE 7 — ECOSYSTEM & DEPENDENCY INTELLIGENCE

========================================================

PERAN

Anda adalah OpenAI Deep Research yang bertugas membangun Ecosystem & Dependency Intelligence Dataset.

Fase ini bertujuan memetakan bagaimana proyek berinteraksi, bergantung, dan terhubung dengan ekosistem blockchain yang lebih luas.

Output fase ini akan menjadi Ecosystem & Dependency Dataset.

========================================================

CONTEXT DEPENDENCIES

Sebelum memulai riset, baca dan gunakan seluruh dokumen berikut sebagai konteks.

========================================================

WAJIB

1. 01-foundation

Gunakan untuk memahami:

- Official Name
- Category
- Main Products
- Chain(s)
- Ecosystem
- Status Project

--------------------------------------------------------

2. 02-entity

Gunakan seluruh isi dokumen.

Fokus:

- Semua Entity
- Company
- Foundation
- Protocol
- Chain
- Exchange
- Wallet
- Oracle
- Infrastructure Provider
- Developer
- DAO
- Government
- Community

Gunakan nama Entity yang sama persis.

--------------------------------------------------------

3. 03-history

Gunakan untuk memahami:

- Partnership Event
- Integration Event
- Ecosystem Expansion
- Exchange Listing
- Governance Event
- Major Product Release

Gunakan Event ID apabila merujuk pada suatu event.

--------------------------------------------------------

4. 04-technology

Gunakan untuk memahami:

- Architecture
- Core Components
- Technical Dependencies
- External Technical Dependencies
- Security Model

Gunakan bagian ini untuk memahami dependency teknis.

--------------------------------------------------------

5. 05-financial

Gunakan untuk memahami:

- Funding History
- Financial Dependencies
- Treasury
- Revenue Source

Bagian ini membantu mengidentifikasi dependency finansial terhadap pihak luar.

--------------------------------------------------------

6. 06-token

Gunakan untuk memahami:

- Utility
- Governance
- Validator
- Staking
- Token Distribution
- Holder Distribution

Bagian ini membantu memahami hubungan token terhadap ekosistem.

========================================================

PRIORITAS REFERENSI

Priority 1

Official Documentation

Priority 2

Official Blog

Priority 3

Whitepaper

Priority 4

GitHub

Priority 5

Governance

Priority 6

Official Dashboard

Priority 7

Partner Documentation

Priority 8

Sumber pihak ketiga terpercaya

Jika terjadi konflik informasi,

JANGAN memilih salah satu.

Laporkan seluruh versi pada Open Threads.

========================================================

PERTANYAAN UTAMA

"Bagaimana proyek ini berinteraksi dan bergantung pada ekosistem eksternal?"

========================================================

RUANG LINGKUP

Laporkan hubungan yang dapat diverifikasi.

Jangan membuat asumsi.

Jangan memberikan opini.

Jangan membahas sentimen pasar.

========================================================

## Ecosystem Position

Kategori Ekosistem

Primary Sector

Secondary Sector

Primary Chain

Supported Chains

Sources

--------------------------------------------------------

## External Dependencies

Untuk setiap dependency

Dependency Name

Dependency Type

(Protocol / Chain / Oracle / Bridge / Cloud / Infrastructure / SDK / Data Provider / Security / Service)

Purpose

Criticality

(Critical / High / Medium / Low)

Status

(Live / Planned)

Related Entity

Related Technology Component

Sources

--------------------------------------------------------

## Major Integrations

Untuk setiap integration

Integration Name

Integrated With

Purpose

Status

(Live / Beta / Planned / Deprecated)

Related Historical Event ID

Sources

--------------------------------------------------------

## Infrastructure Providers

Untuk setiap provider

Provider

Service

Criticality

Status

Sources

--------------------------------------------------------

## Exchange Ecosystem

Exchange

Listing Status

Spot

Perpetual

OTC

Launchpool

Status

Sources

--------------------------------------------------------

## Wallet Ecosystem

Wallet

Support Type

Status

Sources

--------------------------------------------------------

## Developer Ecosystem

SDK

API

Developer Tools

Open Source Repository

Developer Portal

Hackathon

Grant Program

Sources

--------------------------------------------------------

## Applications

Untuk setiap aplikasi

Application

Category

Relationship

Status

Sources

--------------------------------------------------------

## Governance Ecosystem

Foundation

DAO

Council

Committee

Validator Group

Sources

--------------------------------------------------------

## Ecosystem Risks

Laporkan hanya risiko yang telah dikonfirmasi.

Contoh

Single Infrastructure Dependency

Cloud Dependency

Bridge Dependency

Oracle Dependency

Chain Dependency

Centralization Risk

Sources

========================================================

## Official Ecosystem Resources

Official Documentation

Developer Portal

GitHub

Partner Documentation

Grant Program

Ecosystem Dashboard

Semua berupa URL lengkap.

========================================================

BUAT RINGKASAN

Primary Ecosystem

Supported Chains

External Dependencies

Major Integrations

Infrastructure Providers

Developer Programs

Applications

========================================================

Open Threads

Tuliskan seluruh dependency atau integration yang:

- belum dikonfirmasi
- masih diumumkan
- masih beta
- memiliki konflik sumber
- belum dapat diverifikasi

========================================================

ATURAN

- Fokus hanya pada hubungan ekosistem yang dapat diverifikasi.
- Jangan menjelaskan motivasi partnership.
- Jangan membahas sentimen pasar.
- Jangan membahas harga token.
- Jangan membahas analisis kompetitor.
- Jangan memberikan opini mengenai kualitas integrasi.
- Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Setiap bagian WAJIB memiliki "Sources" yang berisi minimal satu URL lengkap yang dapat diverifikasi.
- Jangan menggunakan hyperlink tersembunyi, ikon (🔗), atau anchor text; setiap sumber WAJIB ditulis sebagai URL lengkap (https://...) agar tetap terbawa saat disalin ke DOCX dan dapat diverifikasi.
- Gunakan nama Entity yang sama persis dengan Phase 2.
- Gunakan Event ID yang sama persis dengan Phase 3 apabila merujuk pada suatu peristiwa.
- Jika terdapat perbedaan informasi antara dokumen konteks dan hasil riset terbaru, JANGAN memilih salah satu secara sepihak. Laporkan seluruh versi beserta sumbernya pada bagian Open Threads untuk diverifikasi pada Phase 11 (Conflict Resolution).
```

### Phase 8 — Market Intelligence
```
# PHASE 8 — MARKET INTELLIGENCE

========================================================

PERAN

Anda adalah OpenAI Deep Research yang bertugas membangun Market Intelligence Dataset.

Fase ini bertujuan mendokumentasikan posisi proyek di pasar berdasarkan data yang dapat diverifikasi.

Output fase ini akan menjadi Market Dataset.

========================================================

CONTEXT DEPENDENCIES

Sebelum memulai riset, baca dan gunakan seluruh dokumen berikut sebagai konteks.

========================================================

WAJIB BACA ULANG

1. 01-foundation

Gunakan untuk memahami:

- Official Name
- Symbol
- Category
- Main Products
- Chain(s)
- Ecosystem
- Launch Date
- Status Project

--------------------------------------------------------

2. 02-entity

Gunakan seluruh isi dokumen.

Fokus:

- Competitor
- Exchange
- Market Maker
- Foundation
- Investor
- Community
- Protocol
- Chain

Gunakan nama Entity yang sama persis.

--------------------------------------------------------

3. 03-history

Gunakan untuk memahami:

- Launch Event
- TGE Event
- Exchange Listing
- Partnership
- Major Upgrade
- Major Product Release
- Market Related Event

Gunakan Event ID apabila merujuk pada event.

--------------------------------------------------------

4. 04-technology

Gunakan untuk memahami:

- Architecture
- Core Components
- Technical Advantage
- Supported Chains

Gunakan hanya untuk memahami posisi teknologi di pasar.

--------------------------------------------------------

5. 05-financial

Gunakan untuk memahami:

- Funding History
- Treasury
- Revenue
- Revenue Model

Bagian ini digunakan sebagai konteks market maturity.

--------------------------------------------------------

6. 06-token

Gunakan untuk memahami:

- Token Status
- TGE
- Utility
- Supply
- Governance

Bagian ini digunakan untuk memahami status token di pasar.

--------------------------------------------------------

7. 07-ecosystem

Gunakan seluruh isi dokumen.

Fokus:

- Major Integrations
- Ecosystem Position
- External Dependencies
- Applications
- Developer Ecosystem
- Supported Chains

========================================================

PRIORITAS REFERENSI

Priority 1

Official Dashboard

Priority 2

DefiLlama

Priority 3

Token Terminal

Priority 4

CoinGecko

Priority 5

CoinMarketCap

Priority 6

Messari

Priority 7

Official Blog

Priority 8

Official Documentation

Priority 9

Sumber pihak ketiga terpercaya

Jika terjadi konflik data,

laporkan seluruh versi.

========================================================

PERTANYAAN UTAMA

"Bagaimana posisi proyek ini di pasar berdasarkan data yang dapat diverifikasi?"

========================================================

RUANG LINGKUP

Laporkan data market.

Jangan memberikan opini.

Jangan memberikan rekomendasi investasi.

========================================================

## Market Category

Primary Category

Secondary Category

Sector

Sub-sector

Sources

--------------------------------------------------------

## Market Position

Project Stage

(Pre-TGE / Early / Growth / Mature)

Primary Competitors

Market Segment

Geographic Focus (jika ada)

Sources

--------------------------------------------------------

## Trading Markets

Untuk setiap market

Exchange

Spot

Perpetual

Futures

Options

OTC

Status

Sources

--------------------------------------------------------

## Liquidity

Liquidity Source

Major Liquidity Venue

DEX

CEX

Bridge Liquidity

Status

Sources

--------------------------------------------------------

## Adoption Metrics

Untuk setiap metrik

Metric Name

Value

Date

Sources

Contoh

TVL

Daily Active Users

Transactions

Wallets

Developer Count

Volume

Bridge Volume

Messages

Validator Count

========================================================

## Market Share

Jika tersedia

Metric

Value

Date

Sources

Jika tidak tersedia

Tuliskan

Tidak tersedia.

========================================================

## Competitor Landscape

Untuk setiap kompetitor

Competitor

Category

Difference

Market Segment

Sources

========================================================

## Narrative Position

Laporkan narasi pasar yang dapat diverifikasi.

Contoh

AI

Modular

Restaking

Interoperability

Gaming

RWA

DePIN

L2

Intent

Chain Abstraction

Untuk setiap narrative

Narrative

Status

(Main Narrative / Secondary Narrative)

Evidence

Sources

========================================================

## Market Timeline

Untuk setiap market milestone

Date

Milestone

Description

Related Historical Event ID

Sources

========================================================

## Official Market Resources

Official Dashboard

DefiLlama

CoinGecko

CoinMarketCap

Token Terminal

Messari

Explorer

Semua berupa URL lengkap.

========================================================

BUAT RINGKASAN

Market Stage

Primary Category

Competitor Count

Major Narrative

Trading Availability

Adoption Metrics Available

========================================================

Open Threads

Tuliskan seluruh data market yang:

- belum tersedia
- memiliki konflik angka
- memiliki konflik sumber
- masih berubah
- belum dapat diverifikasi

========================================================

ATURAN

- Fokus hanya pada data pasar yang dapat diverifikasi.
- Jangan memberikan opini investasi.
- Jangan membahas sentimen komunitas.
- Jangan menjelaskan motivasi pasar.
- Jangan membuat prediksi harga.
- Jangan membuat prediksi adopsi.
- Jangan memberikan penilaian terhadap kompetitor.
- Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Setiap bagian WAJIB memiliki "Sources" yang berisi minimal satu URL lengkap yang dapat diverifikasi.
- Jangan menggunakan hyperlink tersembunyi, ikon (🔗), atau anchor text; setiap sumber WAJIB ditulis sebagai URL lengkap (https://...) agar tetap terbawa saat disalin ke DOCX dan dapat diverifikasi.
- Gunakan nama Entity yang sama persis dengan Phase 2.
- Gunakan Event ID yang sama persis dengan Phase 3 apabila merujuk pada suatu peristiwa.
- Jika terdapat perbedaan informasi antara dokumen konteks dan hasil riset terbaru, JANGAN memilih salah satu secara sepihak. Laporkan seluruh versi beserta sumbernya pada bagian Open Threads untuk diverifikasi pada Phase 11 (Conflict Resolution).
```

### Phase 9 — Behavioral Intelligence
```
# PHASE 9 — BEHAVIORAL INTELLIGENCE

========================================================

PERAN

Anda adalah OpenAI Deep Research yang bertugas membangun Behavioral Intelligence.

Fase ini bertujuan menganalisis pola pengambilan keputusan, strategi, prioritas, dan evolusi proyek berdasarkan seluruh dataset yang telah dikumpulkan.

Output fase ini adalah Behavioral Intelligence Report.

========================================================

CONTEXT DEPENDENCIES

WAJIB membaca seluruh dataset berikut sebelum melakukan analisis.

========================================================

1. 01-foundation

Gunakan untuk memahami

- visi
- misi
- kategori
- positioning
- tujuan proyek

--------------------------------------------------------

2. 02-entity

Gunakan seluruh isi dokumen.

Fokus

- seluruh entity
- founder
- foundation
- investor
- DAO
- governance
- exchange
- partner

Analisis bagaimana masing-masing entity memengaruhi keputusan proyek.

--------------------------------------------------------

3. 03-history

Gunakan seluruh isi dokumen.

Fokus

- seluruh historical event
- timeline
- participant
- event result

Gunakan Event ID apabila merujuk suatu peristiwa.

========================================================

4. 04-technology

Gunakan untuk memahami

- architecture evolution
- technical dependency
- consensus
- security model
- technical limitation

Analisis bagaimana faktor teknis memengaruhi keputusan proyek.

--------------------------------------------------------

5. 05-financial

Gunakan untuk memahami

- funding
- treasury
- revenue
- financial dependency

Analisis bagaimana kondisi finansial memengaruhi strategi.

--------------------------------------------------------

6. 06-token

Gunakan untuk memahami

- governance
- utility
- distribution
- staking
- inflation
- vesting

Analisis bagaimana tokenomics memengaruhi perilaku proyek.

--------------------------------------------------------

7. 07-ecosystem

Gunakan untuk memahami

- integrations
- ecosystem dependency
- infrastructure
- developer ecosystem

Analisis bagaimana hubungan eksternal memengaruhi keputusan.

--------------------------------------------------------

8. 08-market

Gunakan untuk memahami

- market position
- competitors
- adoption metrics
- narratives

Analisis bagaimana kondisi pasar memengaruhi strategi proyek.

========================================================

PERTANYAAN UTAMA

"Mengapa proyek ini mengambil keputusan-keputusan tersebut?"

========================================================

RUANG LINGKUP

Gunakan seluruh dataset sebelumnya.

Jangan menambah fakta baru.

Gunakan fakta yang sudah ada untuk menjelaskan hubungan sebab-akibat.

========================================================

## Strategic Objectives

Apa tujuan strategis utama proyek.

Dukung dengan bukti.

========================================================

## Decision Timeline

Untuk setiap keputusan penting

Decision

Date

Trigger

Evidence

Decision

Immediate Result

Long-term Impact

Related Historical Event ID

Supporting Dataset

========================================================

## Evolution Pattern

Bagaimana proyek berevolusi dari waktu ke waktu.

Misalnya

- perubahan strategi
- perubahan teknologi
- perubahan tokenomics
- perubahan governance

========================================================

## Technical Decision Pattern

Identifikasi pola keputusan teknis.

Contoh

- memilih modular architecture

Mengapa?

Gunakan bukti.

========================================================

## Financial Decision Pattern

Identifikasi pola keputusan finansial.

Contoh

- fundraising
- treasury
- grant

Mengapa dilakukan.

Gunakan bukti.

========================================================

## Ecosystem Decision Pattern

Identifikasi pola

- partnership

- integration

- expansion

Mengapa dilakukan.

========================================================

## Governance Decision Pattern

Identifikasi pola

- voting

- proposal

- DAO

- foundation

========================================================

## Risk Response Pattern

Identifikasi bagaimana proyek merespons

- exploit

- market crash

- regulation

- security incident

- governance conflict

========================================================

## Recurring Behavioral Pattern

Identifikasi pola yang berulang.

Misalnya

- selalu memilih partner tertentu

- selalu ekspansi setelah funding

- selalu upgrade setelah exploit

Gunakan bukti.

========================================================

## Strategic Trade-offs

Identifikasi trade-off yang dibuat proyek.

Misalnya

- decentralization vs scalability

- security vs usability

- growth vs sustainability

Trade-off harus didukung bukti.

========================================================

## Behavioral Summary

Ringkas

- Prioritas utama proyek
- Cara mengambil keputusan
- Faktor yang paling sering memengaruhi keputusan
- Pola evolusi
- Kekuatan utama
- Kelemahan utama

========================================================

Open Threads

Laporkan seluruh kesimpulan yang:

- memiliki lebih dari satu interpretasi
- tidak memiliki bukti yang cukup
- memerlukan verifikasi tambahan

========================================================

ATURAN

- Jangan mengumpulkan fakta baru apabila sudah tersedia pada dataset sebelumnya.
- Semua analisis harus mengacu pada dataset Phase 1–8.
- Setiap kesimpulan WAJIB menyebutkan Supporting Dataset (misalnya: Phase 3 Event H-014, Phase 5 Funding History, Phase 7 Major Integrations).
- Jangan membuat asumsi tanpa bukti.
- Jika terdapat lebih dari satu kemungkinan penyebab, jelaskan seluruh alternatif beserta tingkat keyakinannya.
- Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Setiap bagian WAJIB memiliki bagian **Evidence** dan **Sources**.
- Semua Sources harus ditulis sebagai URL lengkap (https://...).
- Gunakan nama Entity yang sama persis dengan Phase 2.
- Gunakan Event ID yang sama persis dengan Phase 3.
- Jika analisis bertentangan dengan fakta pada dataset sebelumnya, jangan memilih salah satu. Laporkan konflik tersebut pada Open Threads untuk diselesaikan pada Phase 11 (Conflict Resolution).
```

Note: this phase's "Decision Timeline" schema (Trigger / Evidence / Decision / Immediate Result /
Long-term Impact) is intentionally different from Track A/B's "Decision Event" schema
(Motivation/Constraint/Pressure/Trade-off/Alternative(s) Considered/Expectation vs. Actual/8-POV
Stakeholder Reactions) — see "Known gaps vs. current tooling" below.

### Phase 10 — Knowledge Extraction
```
# PHASE 10 — KNOWLEDGE EXTRACTION

========================================================

PERAN

Anda adalah OpenAI Deep Research yang bertugas membangun Knowledge Extraction Report.

Fase ini bertujuan mengekstrak pengetahuan, pola, prinsip, dan insight dari seluruh hasil penelitian sebelumnya.

Output fase ini adalah Knowledge Base yang dapat digunakan kembali pada analisis proyek lain.

========================================================

CONTEXT DEPENDENCIES

WAJIB membaca seluruh dataset berikut.

========================================================

1. 01-foundation.docx

Gunakan untuk memahami

- Vision
- Mission
- Category
- Positioning
- Core Objective

--------------------------------------------------------

2. 02-entity.docx

Gunakan seluruh isi.

Fokus

- seluruh entity
- role entity
- dependency
- governance entity

========================================================

3. 03-history.docx

Gunakan seluruh isi.

Fokus

- seluruh event
- timeline
- milestone
- historical evolution

========================================================

4. 04-technology.docx

Gunakan

- architecture
- technical evolution
- technical limitation
- security

========================================================

5. 05-financial.docx

Gunakan

- funding
- treasury
- revenue
- financial dependency

========================================================

6. 06-token.docx

Gunakan

- governance
- utility
- tokenomics
- vesting
- staking

========================================================

7. 07-ecosystem.docx

Gunakan

- integrations
- dependency
- ecosystem evolution

========================================================

8. 08-market.docx

Gunakan

- adoption
- market position
- competitor
- narrative

========================================================

9. 09-behavioral.docx

Gunakan seluruh isi.

Fokus

- Decision Pattern
- Strategic Objective
- Trade-off
- Behavioral Pattern
- Risk Response
- Evolution Pattern

========================================================

PERTANYAAN UTAMA

"Pelajaran, prinsip, dan pola apa yang dapat digeneralisasi dari proyek ini?"

========================================================

RUANG LINGKUP

Gunakan seluruh dataset sebelumnya.

Jangan melakukan riset baru.

Jangan menambahkan fakta baru.

Semua knowledge harus berasal dari evidence yang telah tersedia.

========================================================

## Core Insights

Identifikasi insight utama.

Untuk setiap insight

Insight

Explanation

Evidence

Supporting Dataset

Confidence

========================================================

## Strategic Principles

Identifikasi prinsip strategis yang konsisten.

Misalnya

- modular first

- ecosystem first

- security before growth

- community driven

========================================================

## Success Factors

Identifikasi faktor yang paling berkontribusi terhadap keberhasilan proyek.

Harus didukung evidence.

========================================================

## Failure Factors

Identifikasi faktor yang menyebabkan

- keterlambatan

- kegagalan

- konflik

- exploit

Harus didukung evidence.

========================================================

## Decision Framework

Rekonstruksi bagaimana proyek membuat keputusan.

Contoh

Observe

↓

Evaluate

↓

Fund

↓

Develop

↓

Launch

↓

Govern

Gunakan evidence.

========================================================

## Reusable Playbook

Tuliskan praktik yang dapat diterapkan pada proyek lain.

Misalnya

- cara membangun ecosystem

- cara melakukan fundraising

- cara melakukan governance

Harus didukung evidence.

========================================================

## Anti-patterns

Identifikasi pola yang sebaiknya dihindari.

Misalnya

- over-centralization

- premature scaling

- poor treasury management

Harus didukung evidence.

========================================================

## Lessons Learned

Ringkas pelajaran utama.

========================================================

## Knowledge Summary

Ringkas

- Strategic Principles
- Success Factors
- Failure Factors
- Decision Framework
- Reusable Playbook
- Anti-patterns

========================================================

Open Threads

Tuliskan seluruh insight yang

- memiliki evidence lemah
- memiliki interpretasi ganda
- belum dapat digeneralisasi

========================================================

ATURAN

- Jangan melakukan riset baru.
- Jangan membuat fakta baru.
- Semua insight harus berasal dari dataset Phase 1–9.
- Setiap insight WAJIB memiliki:
  - Evidence
  - Supporting Dataset
  - Confidence (High / Medium / Low)
- Evidence harus mengacu pada dataset internal (contoh: Phase 3 Event H-014, Phase 5 Funding History, Phase 9 Decision Pattern).
- Sources harus berupa URL lengkap yang berasal dari dataset sebelumnya; jangan menambahkan sumber baru.
- Bedakan dengan jelas antara fakta, interpretasi, dan generalisasi.
- Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing dari file DOCX.
- Gunakan nama Entity yang sama persis dengan Phase 2.
- Gunakan Event ID yang sama persis dengan Phase 3.
- Jika sebuah insight didukung oleh evidence yang saling bertentangan, jangan memilih salah satu. Catat konflik tersebut pada Open Threads untuk diselesaikan pada Phase 11.
```

### Phase 11 — Validation & Quality Assurance
```
# PHASE 11 — VALIDATION & QUALITY ASSURANCE

---

PERAN

Anda adalah AI Deep Research yang bertugas melakukan audit kualitas dan validasi akhir terhadap seluruh hasil CIF (Crypto Intelligence Framework).

Fase ini bertujuan memverifikasi konsistensi, menyelesaikan konflik informasi, mengidentifikasi celah data, menentukan tingkat kepercayaan, membangun knowledge dependency graph, dan menghasilkan CIF Score yang objektif.

Output fase ini adalah CIF Validation Report v3.0.

---

CONTEXT DEPENDENCIES

WAJIB membaca seluruh dataset berikut sebelum melakukan audit.

1. 01-foundation.docx

- Official Name, Symbol, Category
- Main Products, Chain(s), Ecosystem
- Launch Dates, Status

2. 02-entity.docx

- Seluruh Entity (Person, Company, Foundation, Protocol, Chain, Investor, Infrastructure, Application, Security, DAO, Government, Media, Other)
- Pastikan nama Entity konsisten

3. 03-history.docx

- Seluruh Event (EV-001 s.d EV-XXX)
- Timeline, Participant, Result
- Pastikan Event ID konsisten

4. 04-technology.docx

- Architecture, Core Components
- Technical Dependencies, Security Model
- Upgrade Timeline

5. 05-financial.docx

- Funding History, Treasury
- Revenue Model, Financial Dependencies
- Token Sale History

6. 06-token.docx

- Supply, Distribution, Vesting
- Utility, Governance
- Inflation/Deflation, Holder Distribution

7. 07-ecosystem.docx

- Ecosystem Position, External Dependencies
- Major Integrations, Infrastructure Providers
- Applications, Developer Ecosystem

8. 08-market.docx

- Market Category, Market Position
- Adoption Metrics, Market Share
- Competitor Landscape, Narrative Position

9. 09-behavioral.docx

- Seluruh Strategic Objectives, Decision Timeline
- Decision Patterns, Risk Response Patterns
- Strategic Trade-offs, Behavioral Summary

10. 10-knowledge.docx

- Seluruh Knowledge Objects (K-001 s.d K-XXX)
- Core Insights, Strategic Principles
- Success/Failure Factors, Reusable Playbook, Anti-patterns

---

PERTANYAAN UTAMA

"Apakah seluruh hasil CIF dapat dipertanggungjawabkan, seberapa tinggi kualitasnya, dan bagaimana knowledge ini akan berevolusi ketika data berubah?"

---

RUANG LINGKUP

Audit seluruh dataset Phase 1–10.

Jangan melakukan riset baru.

Jangan menambah fakta baru.

Semua analisis harus berasal dari evidence yang sudah tersedia.

---

OUTPUT STRUCTURE

Gunakan struktur berikut. Jangan menggunakan tabel dalam bentuk apa pun. Seluruh output harus berupa heading, sub-heading, dan bullet agar mudah diparsing ke format DOCX.

---

CIF MANIFEST v3.0

Buat ringkasan eksekutif satu halaman.

Format:

```
CIF MANIFEST v3.0

Project: <Nama>
Symbol: <Symbol>
Research Date: <YYYY-MM-DD>
CIF Version: 3.0
QA Date: <YYYY-MM-DD>

METRICS
Total Knowledge Objects: <angka>
Total Entities: <angka>
Total Events: <angka>
Evidence Links: <angka>
Sources: <angka>
Conflicts: <angka>
  ├── Resolved: <angka>
  ├── Critical: <angka>
  ├── High: <angka>
  ├── Medium: <angka>
  └── Low: <angka>

QUALITY SCORES
Research Quality: <score>/100
Consistency: <score>/100
Evidence: <score>/100
Coverage: <score>/100
Conflict: <score>/100
Knowledge: <score>/100
CIF SCORE: <score>/100

CONFIDENCE LEVEL: <HIGH / MEDIUM / LOW>
QA STATUS: <PASSED / FAILED / REVIEW NEEDED>

RECOMMENDED RE-RUN:
  - Phase <X> — <Reason>
  - Phase <Y> — <Reason>
```

---

DATASET INTEGRITY & COVERAGE

Periksa setiap phase.

Untuk setiap phase, laporkan:

· Status: Complete / Incomplete
· Missing Information: <daftar atau "Tidak ada">
· Notes: <catatan tambahan>

Coverage Report — Multi-dimensional

Untuk setiap phase, hitung coverage:

· Phase 2 — Entity
  · Total: <angka>
  · Referenced in Phase 9-10: <angka>
  · Unused: <angka>
  · Coverage: <persentase>%
  · Interpretation: <analisis singkat>
· Phase 3 — Event
  · Total: <angka>
  · Referenced in Phase 9-10: <angka>
  · Unused: <angka>
  · Coverage: <persentase>%
  · Interpretation: <analisis singkat>
· Phase 4 — Technology
  · Total: <angka komponen>
  · Referenced: <angka>
  · Unused: <angka>
  · Coverage: <persentase>%
· Phase 5 — Financial
  · Total: <angka fakta>
  · Referenced: <angka>
  · Unused: <angka>
  · Coverage: <persentase>%
· Phase 6 — Token
  · Total: <angka item>
  · Referenced: <angka>
  · Unused: <angka>
  · Coverage: <persentase>%
· Phase 7 — Ecosystem
  · Total: <angka item>
  · Referenced: <angka>
  · Unused: <angka>
  · Coverage: <persentase>%
· Phase 8 — Market
  · Total: <angka item>
  · Referenced: <angka>
  · Unused: <angka>
  · Coverage: <persentase>%
· Overall Coverage
  · Total: <sum semua>
  · Referenced: <sum referenced>
  · Unused: <sum unused>
  · Coverage: <persentase>%
  · Interpretation: <apa arti angka ini>

---

CROSS-PHASE CONSISTENCY

Periksa konsistensi antar phase.

Entity Consistency

· Status: Konsisten / Tidak Konsisten
· Detail: <entity yang sama muncul dengan nama yang sama>

Timeline Consistency

· Status: Konsisten / Tidak Konsisten
· Detail: <timeline di Phase 1, 3, 8, 9 saling mendukung>

Technology Consistency

· Status: Konsisten / Tidak Konsisten
· Detail: <upgrade sequence konsisten>

Funding Consistency

· Status: Konsisten / Tidak Konsisten
· Detail: <funding history di Phase 5 sesuai dengan Phase 3>

Token Consistency

· Status: Konsisten / Tidak Konsisten
· Detail: <token info di Phase 6 sesuai dengan Phase 1 dan 3>

Governance Consistency

· Status: Konsisten / Tidak Konsisten
· Detail: <governance structure konsisten>

Dependency Consistency

· Status: Konsisten / Tidak Konsisten
· Detail: <external dependencies konsisten>

Overall Cross-phase Consistency: <persentase>%

---

DATA LINEAGE

Untuk setiap Knowledge Object (K-001 s.d K-XXX), buat lineage traceability.

Format:

Knowledge K-<XX> — <Nama Knowledge>

Lineage:

```
Level 0 (Raw Data — Events / Metrics / Integrations)
  ├── Phase <X> — <Item ID> (<Deskripsi singkat>)
  │   └── Source: <URL>
  ├── Phase <X> — <Item ID> (<Deskripsi singkat>)
  │   └── Source: <URL>
  └── Phase <X> — <Item ID> (<Deskripsi singkat>)
      └── Source: <URL>

Level 1 (Processed — Pattern Identification)
  └── Phase 9 — <Pattern Name>
      └── Evidence: <evidence summary>

Level 2 (Knowledge)
  └── Knowledge K-<XX> — <Nama Knowledge>

Validation:
  ├── Passed: Cross-phase consistency check
  ├── Passed: Evidence audit (<Strong / Moderate / Weak>)
  └── Confidence: <score>/100
```

---

KNOWLEDGE DEPENDENCY GRAPH

Untuk setiap Knowledge Object, buat dependency graph.

Format:

Knowledge K-<XX> — <Nama Knowledge>

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-<XX>                                                  │
│ <Nama Knowledge>                                        │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── <Item ID> — <Deskripsi>                             │
│ │   └── Source: Phase <X>                               │
│ ├── <Item ID> — <Deskripsi>                             │
│ │   └── Source: Phase <X>                               │
│ └── <Item ID> — <Deskripsi>                             │
│     └── Source: Phase <X>                               │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── <Entity Name> (Entity)                              │
│ ├── <Entity Name> (Entity)                              │
│ └── <Phase> — <Dataset>                                 │
│                                                         │
│ DEPENDENTS (Knowledge yang bergantung pada K-<XX>)      │
│ ├── K-<YY> — <Nama>                                     │
│ └── K-<ZZ> — <Nama>                                     │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If <Item ID> changes → K-<XX> may change               │
│ If <Item ID> changes → K-<XX> may change               │
└──────────────────────────────────────────────────────────┘
```

---

CONFLICT REGISTER WITH SEVERITY & IMPACT

Identifikasi seluruh konflik informasi antar sumber.

Untuk setiap conflict, laporkan:

· Conflict ID: C-<XXX>
· Category: <kategori>
· Description: <deskripsi konflik>
· Severity: Critical / High / Medium / Low
· Affected Knowledge: <daftar K-XX yang terpengaruh>
· Impact: <angka> (Severity × (Affected Knowledge Count + 1))
· Affected Phase: Phase <X>
· Evidence: <evidence>
· Sources: <URL1>, <URL2>
· Resolution: <penjelasan>
· Status: Resolved / Unresolved

Kriteria Severity:

· Critical: Mempengaruhi keakuratan fundamental; dapat menyesatkan pengambil keputusan (Wrong Contract Address, Wrong Total Supply)
· High: Mempengaruhi metrik utama; perbedaan signifikan (TGE Date berbeda, TVL berbeda 50%)
· Medium: Perbedaan numerik tapi dalam rentang yang dapat diterima (Treasury Size $1.21B vs $1.3B)
· Low: Perbedaan kecil; tidak mempengaruhi kesimpulan (Tanggal launch berbeda 1 hari karena zona waktu)

Conflict Summary:

· Total Conflicts: <angka>
· Resolved: <angka>
· Unresolved: <angka>
· Critical: <angka>
· High: <angka>
· Medium: <angka>
· Low: <angka>

Conflict Score:

```
Conflict Score = 
  (Resolved × 1.0) +
  (Unresolved Low × 0.9) +
  (Unresolved Medium × 0.6) +
  (Unresolved High × 0.3) +
  (Unresolved Critical × 0.0)
────────────────────────────────────
        Total Conflicts
```

Hasil: <angka>%

---

EVIDENCE AUDIT

Periksa seluruh insight di Phase 9 dan Phase 10.

Untuk setiap Knowledge, laporkan:

· Knowledge: K-<XX> — <Nama>
· Supporting Dataset: <Phase X, Phase Y>
· Evidence Quality: Strong / Moderate / Weak
· Evidence Weight: <0-10>
· Assessment: <analisis singkat>

Evidence Weight Criteria:

· Governance Vote (On-chain): 10
· Official Documentation: 10
· GitHub Commit: 9
· Explorer Data: 9
· Official Blog: 8
· Whitepaper: 8
· Foundation Transparency Report: 8
· Messari / Token Terminal: 7
· Research Paper: 7
· News (Major): 6
· Forum Discussion: 6
· News (Minor): 5
· Third-party Blog: 4
· Twitter / Social: 3

---

CONFIDENCE ASSESSMENT — v3.0

Gunakan formula yang menggabungkan Evidence Weight dan Source Diversity.

Source Diversity Score:

· Jika total weight > 20: 10/10 (High)
· Jika total weight 10-20: 5/10 (Medium)
· Jika total weight < 10: 2/10 (Low)

Untuk setiap Knowledge, laporkan:

· Knowledge: K-<XX> — <Nama>
· Evidence Count: <angka>
· Evidence Weight: <rata-rata>
· Independent Sources: <angka>
· Official Sources: <angka>
· Source Diversity: <0-10>
· Cross-phase Validation: Pass / Fail
· No Conflicts: 0 conflicts / <angka conflicts>
· Coverage: <persentase>%
· Confidence Score: <0-100>
· Confidence Level: High / Medium / Low

Confidence Score Formula (v3.0):

```
Confidence Score = 
  (Evidence Count × 10) +
  (Evidence Weight × 5) +
  (Independent Sources × 10) +
  (Official Sources × 15) +
  (Cross-phase Validation × 15) +
  (No Conflicts × 10) +
  (Coverage × 10)
────────────────────────────────────
        Max Score = 100
```

Confidence Summary:

· High (80-100): <angka> Knowledge
· Medium (60-79): <angka> Knowledge
· Low (<60): <angka> Knowledge
· Average Confidence Score: <angka>/100

---

KNOWLEDGE STABILITY & VERSIONING

Untuk setiap Knowledge Object, tentukan stabilitas dan buat version history.

Stability Categories:

· Stable: Tidak akan berubah kecuali ada perubahan fundamental
· Emerging: Masih berkembang, data baru mungkin mengubah insight
· Volatile: Sangat tergantung pada data terbaru
· Deprecated: Tidak lagi relevan

Format:

Knowledge K-<XX> — <Nama Knowledge>

Stability: <Stable / Emerging / Volatile / Deprecated>
Current Version: <vX.Y>
Created: <YYYY-MM-DD>
Last Updated: <YYYY-MM-DD>
Status: Active / Deprecated

Version History:

· v1.0 — <YYYY-MM-DD>
  · Created with evidence: <daftar evidence>
  · Confidence: <score>/100
· v1.1 — <YYYY-MM-DD> (Planned / Executed)
  · Trigger: <apa yang memicu perubahan>
  · Expected Change: <apa yang berubah>
  · Confidence Change: <old> → <new>

Deprecation Status: Active / Deprecated
Replacement: <K-XX jika deprecated>

---

MISSING KNOWLEDGE CLASSIFICATION

Identifikasi data yang tidak tersedia.

Format:

Missing Item Phase Missing Reason Severity Impact
<Item> Phase <X> <Reason> <High/Medium/Low> <Impact>

Missing Reason Categories:

· Not Public: Data ada tetapi tidak dipublikasikan oleh proyek
· Never Existed: Data memang tidak pernah ada
· Deprecated: Data pernah ada tetapi sudah tidak relevan
· Not Applicable: Tidak relevan untuk proyek ini
· Not Yet Released: Akan dirilis di masa depan
· Unknown: Tidak diketahui penyebabnya

---

CIF SCORE CALCULATION — v3.0

Hitung CIF Score berdasarkan 6 dimensi.

Dimensi dan Bobot:

· Research Quality: 25%
· Consistency: 20%
· Evidence: 15%
· Coverage: 15%
· Conflict: 15%
· Knowledge: 10%

Perhitungan:

Research Quality:

· (Complete Phases / 10) × 100 = <score>
· Kontribusi: <score> × 0.25 = <value>

Consistency:

· (Passed Checks / Total Checks) × 100 = <score>
· Kontribusi: <score> × 0.20 = <value>

Evidence:

· Average Evidence Weight (0-100) = <score>
· Kontribusi: <score> × 0.15 = <value>

Coverage:

· Overall Coverage (%) = <score>
· Kontribusi: <score> × 0.15 = <value>

Conflict:

· Conflict Score (%) = <score>
· Kontribusi: <score> × 0.15 = <value>

Knowledge:

· Average Confidence Score = <score>
· Kontribusi: <score> × 0.10 = <value>

CIF Score = SUM of all contributions = <angka>/100

Interpretation:

· Excellent (>90): CIF siap pakai untuk analisis lintas proyek
· Good (80-90): CIF berkualitas tinggi, beberapa area perlu perbaikan
· Needs Improvement (60-80): CIF usable, perbaikan disarankan
· Poor (<60): CIF perlu re-run

PENTING: angka CIF Score di sini adalah HASIL FINAL. Kembali ke bagian CIF MANIFEST v3.0 di awal laporan dan
salin angka Research Quality / Consistency / Evidence / Coverage / Conflict / Knowledge / CIF SCORE dari
perhitungan di atas — JANGAN biarkan Manifest berisi angka yang dihitung terpisah atau lebih dulu. Manifest
bukan sumber angka, ia melaporkan ULANG angka dari sini.

---

FINAL VALIDATION SUMMARY

Ringkas seluruh temuan.

Dataset Completeness:

· Complete Phases: <angka> dari 10
· Missing Information: <angka> item, semua dicatat
· Status: <persentase>% lengkap

Cross-phase Consistency:

· Overall: <persentase>%
· Status: Konsisten / Tidak Konsisten

Evidence Quality:

· Strong: <angka> Knowledge
· Moderate: <angka> Knowledge
· Weak: <angka> Knowledge

Confidence Assessment:

· High: <angka> Knowledge
· Medium: <angka> Knowledge
· Low: <angka> Knowledge
· Average: <angka>/100

Remaining Conflicts:

· Resolved: <angka>
· Unresolved: <angka>
· Critical: <angka>
· High: <angka>
· Medium: <angka>
· Low: <angka>

Knowledge Stability Distribution:

· Stable: <angka>
· Emerging: <angka>
· Volatile: <angka>
· Deprecated: <angka>

CIF Score: <angka>/100

Overall Validation Result:
<Paragraf singkat tentang kualitas CIF secara keseluruhan>

Recommended Re-run:

· Phase <X> — <Reason>
· Phase <Y> — <Reason>

QA Status: PASSED / FAILED / REVIEW NEEDED

Confidence Level: HIGH / MEDIUM / LOW

---

Open Threads

Tuliskan seluruh informasi yang:

· memiliki lebih dari satu interpretasi
· memiliki evidence lemah
· memerlukan verifikasi tambahan
· masih berubah
· memiliki konflik yang belum terselesaikan

Format:

Open Thread ID: OT-<XX>

· Description: <deskripsi>
· Affected Phase: Phase <X>
· Evidence: <evidence>
· Alternative Interpretations: <daftar>
· Status: Open / In Review

---

ATURAN UMUM

1. Jangan melakukan riset baru.
2. Jangan membuat interpretasi baru di luar evidence yang ada.
3. Jangan mengubah fakta dari dataset sebelumnya.
4. Semua konflik WAJIB menyebutkan:
   · Evidence
   · Supporting Dataset
   · Sources (URL lengkap)
5. Jika konflik tidak dapat diselesaikan menggunakan evidence yang tersedia, tandai sebagai Unresolved.
6. Jangan menggunakan tabel dalam bentuk apa pun; seluruh output harus berupa heading, sub-heading, dan bullet.
7. Semua Sources harus berupa URL lengkap (https://...), bukan hyperlink tersembunyi atau anchor text.
8. Gunakan nama Entity yang sama persis dengan Phase 2.
9. Gunakan Event ID yang sama persis dengan Phase 3 (EV-XXX).
10. Gunakan Knowledge ID yang sama persis dengan Phase 10 (K-XXX).
11. Confidence Score menggunakan formula v3.0.
12. Conflict Impact = Severity × (Affected Knowledge Count + 1).
13. Stabilitas Knowledge menggunakan klasifikasi Stable / Emerging / Volatile / Deprecated.
14. Missing Knowledge menggunakan klasifikasi Not Public / Never Existed / Deprecated / Not Applicable / Not Yet Released / Unknown.
15. Jika terdapat konflik antara formula dan interpretasi manual, laporkan keduanya dan tandai sebagai Open Thread.
16. CIF Score WAJIB dihitung SETELAH bagian "CIF SCORE CALCULATION — v3.0" selesai dihitung lengkap
    (Research Quality, Consistency, Evidence, Coverage, Conflict, Knowledge, lalu jumlah akhirnya). Tulis
    bagian CIF MANIFEST v3.0 di awal laporan TERAKHIR, setelah seluruh perhitungan detail selesai, dan salin
    angka-angkanya persis dari hasil kalkulasi tersebut — JANGAN mengisi angka di Manifest lebih dulu lalu
    menghitung ulang secara terpisah di bagian CIF Score Calculation. Kedua bagian WAJIB melaporkan angka
    yang sama persis.
```

### Known gaps vs. current tooling (open items)

Documented here rather than silently worked around, so the next person running Track C knows what's not
wired up yet:

- ~~Phase 11's filename/header need to fit `tools/ingest.py`'s contract~~ — **resolved.** Corrected after
  actually testing it: `validate_phase_content()`'s `PROJECT_HEADER_RE` is case-insensitive and searches the
  whole text (not just line 1), so it already matched the `Project: Arbitrum` line nested inside the real
  Phase 11's `CIF MANIFEST v3.0` block — the header was never actually a problem. The real, verified gap was
  that the assembled dossier's section title always said "Conflicting Evidence & Resolutions" for phase 11
  regardless of content shape, mislabeling the Validation Report. `tools/ingest.py`'s `phase_meta()` now
  detects the `CIF VALIDATION REPORT` / `CIF MANIFEST` signal and swaps in "Validation & Quality Assurance
  (CIF Score)" instead; `"conflict"` stays the phase key and `11-conflict.docx` stays the filename (no data
  migration needed), Track A/B content is unaffected (verified no regression). Also added a `--model` flag
  to `tools/ingest.py` (default `Gemini`) so the dossier's "Source:" line doesn't wrongly credit Gemini for
  a DeepSeek-researched project — pass `--model DeepSeek` when running Track C projects through
  `tools/ingest.py --type data_project`.
- ~~The real Arbitrum run's `CIF SCORE` was internally inconsistent~~ — **resolved**: Phase 11's ATURAN UMUM
  §16 above now requires computing the CIF Score Calculation section first and copying its result into the
  Manifest, not the reverse.
- **Phase 9's "Decision Timeline" (Trigger/Evidence/Decision/Immediate Result/Long-term Impact) doesn't
  match `tools/extract_decision_events.py`'s expected "Decision Event" schema**
  (Motivation/Constraint/Pressure/Trade-off/Alternative(s) Considered/Expectation vs. Actual/8-POV
  Stakeholder Reactions, from Track A/B above). Running the extractor against a Track C dossier currently
  yields zero decision events, silently — it needs a second parser branch for this shape, or Track C's
  prompt needs its own 8-POV field added. Neither has been done yet.
- **ASCII box-drawing diagrams in the Knowledge Dependency Graph section get visually mangled** by
  `tools/extract.py`'s `normalise()` — it collapses runs of 2+ spaces for ordinary paragraph reflow, which
  also destroys the diagram's column alignment. No data is lost (every line survives, just misaligned); this
  only matters if a human is expected to read the rendered box art rather than an LLM parsing the semantic
  content.

## Related Files

`docs/Protocol/Deep-Research-Brief.md` (the "Format v3 — Dependency Pipeline" section this operationalizes),
`docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md`, `docs/Ontology/Hidden.md`,
`docs/Ontology/Relationships.md` (entity graph + `exposure_type`, for cross-project contagion mapping),
`examples/DatasetIndex.md` § "Phased Deep Research Queue" (progress tracking), `examples/PatternRegistry.md`,
`tools/ingest.py` (`process_phased_project` — legacy fuzzy-matching folder convention; `process_data_project`
+ `validate_phase_content` — hardened `data_project/<project>/` convention, use this for new projects),
`tools/README.md` (usage + the content-verification checks), `doc_backup/inbox/README.md`.
