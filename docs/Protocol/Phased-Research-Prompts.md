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

## Related Files

`docs/Protocol/Deep-Research-Brief.md` (the "Format v3 — Dependency Pipeline" section this operationalizes),
`docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md`, `docs/Ontology/Hidden.md`,
`docs/Ontology/Relationships.md` (entity graph + `exposure_type`, for cross-project contagion mapping),
`examples/DatasetIndex.md` § "Phased Deep Research Queue" (progress tracking), `examples/PatternRegistry.md`,
`tools/ingest.py` (`process_phased_project` — legacy fuzzy-matching folder convention; `process_data_project`
+ `validate_phase_content` — hardened `data_project/<project>/` convention, use this for new projects),
`tools/README.md` (usage + the content-verification checks), `doc_backup/inbox/README.md`.
