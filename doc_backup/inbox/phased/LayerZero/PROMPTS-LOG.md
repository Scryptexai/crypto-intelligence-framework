# LayerZero — Phase Prompt Log

Exact prompt text actually sent for each phase (with LayerZero-specific context injected — the
project-specific known-facts, mandatory-entity, and open-thread injections are NOT part of the generic
template in `docs/Protocol/Phased-Research-Prompts.md`, so they only exist here). Kept alongside the raw
`.docx` outputs in this folder so a future session can see exactly what was asked, not just what came back —
same reasoning as why the generic prompts live in the repo at all (see that file's Policy Note).

## Phase 1 — Foundation Intelligence (sent 2026-07-25)

```
You are a crypto research investigator building a factual foundation dossier on LayerZero. This phase
collects FACTS ONLY — no analysis, no interpretation, no "why."

Fill this exact template (write "unknown" for anything unverifiable — do not guess):

PROJECT: LayerZero
Official Name: <value>
Symbol: <value>
Category: <value — be specific, e.g. "cross-chain messaging / interoperability", not just "infra">
Founding Entity: <legal name, jurisdiction>
Founders: <name1 (role); name2 (role); ... — or "anonymous/pseudonymous — <handle>">
Core Team: <size/notable names, or "undisclosed">
Country: <value>
Launch Date - Testnet: <date or "n/a">
Launch Date - Mainnet: <date or "n/a">
Launch Date - TGE: <date or "pre-TGE">
Main Products: <semicolon-separated list>
Official Website: <url>
Repository: <url>
Documentation: <url>
Social - X/Twitter: <handle>
Social - Discord: <invite/handle>
Social - Telegram: <handle>
Block Explorer: <url>
Token Contract: <address, chain — or "not yet deployed">
Chain(s): <value>
Ecosystem: <value>

Open Threads
- <anything uncertain>

[+ shared FORMAT RULES from Phased-Research-Prompts.md, at the time: English/mixed language allowed,
tables not yet forbidden, citation rule present but weaker — these were tightened AFTER this run, see
Phase 2 below]
```

**Result:** narrative-form English report, not template-compliant (see `DatasetIndex.md` § Phased Deep
Research Queue for the full quality note). A reformat pass was requested (see below) rather than a full
re-run, since the underlying research was sound.

## Phase 1 reformat pass (sent 2026-07-25, same day)

```
Tugas kamu sekarang HANYA MEMFORMAT ULANG laporan LayerZero di atas. Ini BUKAN riset baru.

ATURAN MUTLAK:
- JANGAN tambah fakta baru. JANGAN riset ulang. JANGAN hapus fakta apa pun yang sudah ada.
- Semua angka, tanggal, nama, dan alamat kontrak harus sama persis dengan laporan di atas.
- Kalau di laporan atas ada dua sumber yang berbeda soal hal yang sama (misal jumlah chain
  "50+" vs "165+"), JANGAN pilih salah satu — tulis keduanya dan tandai sebagai konflik.

FORMAT YANG DIMINTA:
1. Bahasa Indonesia untuk semua kalimat dan label. TAPI biarkan tetap dalam bahasa aslinya:
   nama produk/teknologi (Ultra Light Node, DVN, OFT, Proof-of-Donation, Stargate),
   nama orang, nama perusahaan, nama chain, dan URL.
2. HAPUS SEMUA TABEL. Ubah setiap baris tabel menjadi bullet "Label: Isi" satu fakta per baris.
   Contoh: "- Symbol: ZRO (HIGH) [sumber 1, 27]"
3. Setiap fakta WAJIB diakhiri dengan:
   (a) Evidence Level: HIGH kalau beberapa sumber independen sepakat, MEDIUM kalau satu sumber
       kredibel, LOW kalau cuma inferensi atau ada perselisihan.
   (b) Nomor sumber dari daftar "Karya yang dikutip" di laporan atas — dalam kurung siku.
   Kalau kamu benar-benar tidak bisa menemukan sumbernya di daftar itu, tulis [sumber tidak
   terpetakan] — JANGAN mengarang nomor sumber.
4. Susun dengan urutan bagian seperti ini:
   PROJECT: LayerZero
   ## Identitas Dasar
   ## Entitas Pendiri & Legal
   ## Produk Utama
   ## Kanal Resmi
   ## Kontrak & Chain
5. Tutup dengan bagian:
   ## Open Threads
   - (daftar hal yang masih belum pasti / bertentangan / perlu diverifikasi di fase berikutnya)

Mulai sekarang, keluarkan hasil format ulangnya saja tanpa penjelasan tambahan.
```

**Result:** clean, parseable, Indonesian. Diffed against the original — all numeric facts survived; 8
proper-noun items (Chainlink, Google Cloud, Polyhedra, Chainlink CCIP, Bridging Trilemma,
SendUln302/ReceiveUln302/ReadLib1002) were silently dropped. Both files kept — see `DatasetIndex.md`.
This gap is *why* the FORMAT RULES in `Phased-Research-Prompts.md` gained the explicit
"never drop a proper noun" instruction before Phase 2 was sent.

## Phase 2 — Entity Intelligence (sent 2026-07-25)

```
Menggunakan output Foundation Intelligence (Phase 1) di atas sebagai konteks, sekarang bangun
ENTITY GRAPH untuk LayerZero — yaitu SEMUA entitas yang punya hubungan dengan proyek ini.

Ini adalah PEMETAAN HUBUNGAN, bukan analisis sebab-akibat. Catat SIAPA terhubung dan BAGAIMANA
bentuk hubungannya. JANGAN membahas kenapa, dampaknya, atau siapa yang untung/rugi — itu tugas
fase berikutnya.

=== CAKUPAN YANG DIMINTA ===
Cari entitas dari kategori berikut:
- Investor (semua ronde pendanaan, termasuk yang sudah bermasalah/bangkrut)
- Organisasi & badan hukum (termasuk entitas afiliasi, anak perusahaan, yayasan)
- Orang (founder, core team, advisor, mantan anggota kunci yang sudah keluar)
- Exchange (yang melisting ZRO)
- Partner & integrasi teknis (protokol/aplikasi yang membangun di atas LayerZero)
- Penyedia infrastruktur keamanan (Oracle, DVN, relayer, auditor)
- DAO / badan tata kelola
- Regulator / pengadilan / pemerintah (jika ada keterlibatan hukum)
- Media / lembaga riset yang punya hubungan formal (bukan sekadar meliput)

WAJIB ADA (terlewat di fase sebelumnya — pastikan masuk):
- Chainlink — perannya sebagai penyedia Oracle di arsitektur LayerZero V1
- Google Cloud — perannya sebagai opsi DVN di V2
- Polyhedra — perannya sebagai opsi DVN di V2
- Chainlink CCIP — perannya sebagai opsi DVN di V2
- Alameda Ventures / FTX Group — hubungan pendanaan dan sengketa kepailitannya
- Protocol Guild — penerima dana mekanisme Proof-of-Donation
- Stargate Finance — hubungannya setelah digabung ke ekosistem ZRO
- Tether — terkait peluncuran USDT0 memakai standar OFT
- Semua auditor yang sudah disebut: Trail of Bits, Zellic, Zokyo, Peckshield, Hacken

TENTANG SKALA: LayerZero terhubung ke 165+ chain dan ratusan dApp. JANGAN daftarkan semuanya
satu per satu. Untuk chain dan dApp yang jumlahnya masif, kelompokkan saja (contoh: "Chain EVM
terintegrasi — 165+, lihat Phase 7 Ecosystem") dan cukup sebutkan secara individual yang
BENAR-BENAR SIGNIFIKAN saja (misal chain besar, atau integrasi yang punya nilai/volume besar).
Fase 7 (Ecosystem Intelligence) yang akan menangani daftar panjangnya.

=== PERTANYAAN TERBUKA DARI PHASE 1 YANG HARUS DIJAWAB DI SINI ===
1. Konflik badan hukum: "LayerZero Labs Ltd." vs "Optimistic Labs Limited" (keduanya British
   Virgin Islands). Apakah ini dua entitas berbeda, entitas yang berganti nama, atau
   hubungan induk-anak perusahaan? Jika tetap tidak jelas, catat sebagai konflik yang belum
   terselesaikan — JANGAN memilih salah satu tanpa bukti.
2. Ukuran tim inti (core team) — apakah ada nama-nama anggota tim kunci selain tiga founder
   yang bisa diverifikasi?

=== FORMAT OUTPUT ===
Untuk SETIAP entitas, ulangi blok ini persis:

Entity: <nama>
Type: <Organization | Person | Investor | Foundation | Exchange | Partner | Protocol | Developer | Product | DAO | Government | Media | Research Lab>
Relationship: <bentuk hubungannya, contoh: "memimpin ronde Series B", "penyedia Oracle di V1">
Period: <mulai–selesai, atau "mulai–sekarang", atau "unknown">
Exposure Type: <financial-collateral | technical-integration | liquidity-dependency | shared-investor-only | narrative-correlated-only | unknown>
Evidence: <nama sumber + URL>
---

PENJELASAN "Exposure Type" (pilih yang PALING KUAT, bukan yang paling mudah):
- financial-collateral = entitas ini memegang/pernah memegang aset LayerZero sebagai treasury,
  jaminan, atau cadangan — ATAU sebaliknya, LayerZero memegang aset entitas tersebut.
  Ini hubungan paling berbahaya kalau salah satu pihak gagal.
- technical-integration = LayerZero bergantung pada infrastruktur entitas ini agar berfungsi,
  atau sebaliknya (contoh: Oracle, DVN, bridge, execution layer).
- liquidity-dependency = entitas ini adalah tempat likuiditas utama atau market maker.
- shared-investor-only = hanya berbagi investor yang sama, TIDAK ada ketergantungan operasional.
- narrative-correlated-only = hanya satu kategori/narasi pasar, tanpa hubungan operasional nyata.
- unknown = hubungan ada tapi jenis eksposurnya belum bisa dipastikan. Jangan menebak.

Tutup dengan:

Open Threads
- (daftar hal yang masih belum pasti, bertentangan, atau perlu diverifikasi di fase berikutnya)

=== ATURAN FORMAT (berlaku untuk seluruh jawaban) ===
- Tulis dalam BAHASA INDONESIA. Yang TIDAK diterjemahkan: nama produk/teknologi (Ultra Light
  Node, DVN, OFT), nama orang, nama perusahaan, nama chain, dan URL.
- JANGAN gunakan tabel sama sekali. Semua dalam bentuk "Label: Isi", satu fakta per baris.
- Sumber WAJIB menempel di baris fakta itu sendiri (di field Evidence), BUKAN dikumpulkan
  jadi daftar pustaka di akhir. Daftar sumber di bawah tanpa kaitan per-fakta TIDAK diterima.
- Setiap entitas diberi Evidence Level: HIGH (beberapa sumber independen sepakat), MEDIUM
  (satu sumber kredibel), LOW (inferensi atau ada perselisihan). Tulis setelah nama entitas,
  contoh: "Entity: a16z (HIGH)".
- JANGAN mengarang. Kalau tidak terverifikasi, tulis "unknown" — jangan diisi tebakan.
- Kalau dua sumber berbeda soal hal yang sama, tulis KEDUANYA dan tandai "(konflik)".
- JANGAN menghilangkan nama diri apa pun yang muncul di sumber — setiap nama perusahaan,
  produk, atau orang yang disebut harus tetap tertulis.
- Awali output dengan: PROJECT: LayerZero
```

**Result:** clean pass, 76 entities, all 13 mandatory entities present, `exposure_type` correctly varied.
Minor deviation: fields joined into one paragraph per entity instead of one field per line — addressed in
the Phase 3 prompt below. See `DatasetIndex.md` for the full quality note.

## Phase 3 — Historical Intelligence (sent 2026-07-25)

```
Menggunakan output Foundation Intelligence (Phase 1) dan Entity Intelligence (Phase 2) di atas
sebagai konteks, bangun TIMELINE KRONOLOGIS untuk LayerZero — FONDASI FAKTUAL yang akan dirujuk
oleh semua fase berikutnya. Ini BELUM analisis sebab-motivasi (itu tugas Phase 9 Behavioral) —
fokus di sini adalah APA yang terjadi, KAPAN, DIPICU APA, dan APA HASILNYA.

=== EVENT YANG SUDAH DIKETAHUI — WAJIB MASUK TIMELINE (perdalam, jangan lewatkan) ===
- Mei 2021: Publikasi whitepaper "LayerZero: Trustless Omnichain Interoperability Protocol"
- April 2021: Seed round $2 juta
- September 2021: Series A $6 juta; sekitar waktu ini juga mainnet/deployment awal V1
- Awal 2022: Peluncuran Stargate Finance
- Maret 2022: Series A Extension $135 juta (valuasi $1 miliar) — dengan FTX Ventures/Alameda
  sebagai salah satu backer
- November 2022: Keruntuhan FTX — bagaimana ini berdampak ke LayerZero sebagai penerima dana FTX?
- April 2023: Series B $120 juta (valuasi $3 miliar) — terjadi TEPAT setelah keruntuhan FTX dan
  di tengah "crypto winter", ini perlu dijelaskan kronologinya dengan hati-hati
- 2023 (kapan tepatnya?): FTX Recovery Trust mengajukan gugatan clawback terhadap LayerZero Labs
- Januari 2024: Peluncuran LayerZero V2 (arsitektur DVN)
- April 2024: Insiden eksploitasi Kelp DAO ($292 juta) akibat konfigurasi DVN 1-of-1
- 20 Juni 2024: TGE token ZRO + mekanisme "Proof-of-Donation" + reaksi komunitas negatif +
  harga anjlok 22% dalam 4 jam pertama
- Governance: merger Stargate Finance (STG) ke dalam ekosistem ZRO — kapan tepatnya dan
  bagaimana prosesnya (voting? keputusan sepihak?)

=== YANG PERLU DICARI LEBIH DALAM (belum ada datanya) ===
- Tanggal pasti testnet (masih "unknown" dari Phase 1)
- Detail proses hukum FTX Recovery Trust vs LayerZero — tanggal filing gugatan, tanggal
  respons LayerZero, status terkini (menang/kalah/settlement/masih berjalan?)
- Apakah ada insiden keamanan/eksploitasi LAIN selain Kelp DAO?
- Apakah ada perubahan besar pada tim (kepergian/kedatangan eksekutif kunci) sepanjang sejarah?
- Milestone adopsi penting: kapan LayerZero pertama kali menembus 50 chain? 100 chain? 165 chain?
- Preferensi governance/keputusan protokol besar lainnya yang belum tercatat

=== FORMAT OUTPUT ===
Untuk SETIAP event, dalam urutan kronologis (paling lama duluan), tulis blok ini dengan SETIAP
FIELD DI BARIS TERPISAH (jangan digabung jadi satu paragraf seperti Phase 2 kemarin):

Date: <YYYY-MM-DD atau presisi terbaik yang tersedia>
Event: <label singkat>
Trigger: <penyebab langsung yang bisa diobservasi — BUKAN spekulasi motif>
Context Snapshot (kondisi era saat tanggal ini):
  Industry state: <kondisi industri crypto/interoperability saat itu>
  Competitor state: <siapa kompetitor utama saat itu dan posisinya>
  Tech maturity: <seberapa matang teknologi cross-chain saat itu>
  Macro conditions: <kondisi makro — bull/bear market, suku bunga, dst>
  Hunter/user population: <kalau relevan dengan airdrop — populasi pemburu airdrop saat itu>
  VC climate: <iklim pendanaan VC crypto saat itu — royal atau ketat>
  Narrative: <narasi crypto yang dominan saat itu>
  (boleh lewati sub-field yang benar-benar tidak relevan, tapi JANGAN lewati seluruh blok Context)
Decision: <apa yang diputuskan/dilakukan>
Execution: <BAGAIMANA keputusan itu benar-benar dijalankan secara operasional — beda dari
  keputusannya sendiri>
Short-term Outcome: <efek dalam hitungan minggu-bulan>
Long-term Outcome: <efek jangka panjang, atau "terlalu dini untuk dinilai">
Evidence: <sumber>
---

Kalau sebuah event melibatkan entitas yang sudah dipetakan di Phase 2 (misal Chainlink,
Alameda Ventures/FTX Group, FTX Recovery Trust), SEBUTKAN NAMA ENTITASNYA PERSIS seperti di
Phase 2 — supaya event ini bisa disambungkan ke entity graph nanti.

Tutup dengan:

Open Threads
- (hal yang masih belum pasti, bertentangan, atau perlu digali lebih lanjut)

=== ATURAN FORMAT (berlaku untuk seluruh jawaban) ===
- Tulis dalam BAHASA INDONESIA. Yang TIDAK diterjemahkan: nama produk/teknologi, nama orang,
  nama perusahaan, nama chain, dan URL.
- SETIAP FIELD DI BARIS SENDIRI — jangan gabung Date/Event/Trigger dst jadi satu paragraf.
- JANGAN gunakan tabel sama sekali.
- Sumber WAJIB menempel di field Evidence pada blok event itu sendiri, BUKAN dikumpulkan jadi
  daftar pustaka terpisah di akhir tanpa kaitan per-event.
- Evidence Level (HIGH/MEDIUM/LOW) untuk tiap event — taruh setelah label "Event:", contoh:
  "Event: Peluncuran LayerZero V2 (HIGH)".
- JANGAN mengarang. Kalau tidak terverifikasi, tulis "unknown".
- Kalau dua sumber beda soal tanggal/detail yang sama, tulis KEDUANYA dan tandai "(konflik)".
- JANGAN hilangkan nama diri (orang/perusahaan/produk) yang muncul di sumber.
- JANGAN analisis motivasi atau spekulasi sebab-akibat mendalam — itu tugas Phase 9. Trigger
  di sini cukup penyebab yang bisa diobservasi langsung, bukan "kenapa secara strategis."
- Cakup SELURUH sejarah dari awal berdiri sampai sekarang. JANGAN lewati event yang tidak
  nyaman (insiden keamanan, kontroversi, sengketa hukum) — timeline yang lengkap justru intinya.
- Awali output dengan: PROJECT: LayerZero
```

**Result:** content excellent (all 13 known events present + 4 valuable bonus findings: FTX equity
buyback, FTX lawsuit Motion-to-Dismiss timeline, second-order Radiant Capital exploit, DVN diversification
response), Context Snapshot/Execution/Short+Long-term Outcome all 13/13. Two problems found: (1) all 13
`Evidence:` fields were empty ("Evidence:." — no source attached) despite the rule being stated and
tightened twice already — same failure mode as the original Phase 1 attempt. (2) fields were joined into
one flowing paragraph per event instead of one field per line (same deviation as Phase 2) — cosmetic, not
blocking, since ingestion treats the whole event block as one span. A citation-only reformat pass was
requested (see below), mirroring the Phase 1 reformat. Minor gap: Trail of Bits (a Phase 2 entity) is never
referenced in the Phase 3 timeline — flagged, not blocking.

## Phase 3 citation reformat pass (sent 2026-07-25, same day; REVISED after Phase 4 surfaced 2 missing events)

```
Tugas kamu sekarang MEMPERBAIKI CITATION pada timeline LayerZero di atas, DAN menambahkan 2 event yang
baru terungkap dari riset Phase 4 (Technology Intelligence) yang belum ada di timeline ini. Bagian
citation BUKAN riset baru — bagian 2 event baru BOLEH riset baru (perdalam, jangan cuma satu baris).

MASALAH 1 — CITATION: semua 13 blok event punya field "Evidence:" KOSONG. Ini tidak bisa diterima —
setiap fakta harus bisa dilacak ke sumbernya.

MASALAH 2 — 2 EVENT HILANG: Phase 4 mengungkap dua peristiwa nyata sesudah Agustus 2024/2025 (event
terakhir di timeline ini saat ini) yang belum masuk timeline:
- Peluncuran blockchain "Zero" — 10 Februari 2026 — Layer-1 mandiri LayerZero (Decentralized Multi-Core
  World Computer, konsensus "Pure Delegated Proof of Stake", target 10.000 TPS, modul "System Zone" untuk
  saldo ZRO omnichain dan fee switch).
- Modifikasi keamanan sistemik DVN — Mei 2026 — menanggapi insiden Kelp DAO (April 2024), tim inti
  memblokir kemampuan klien menunjuk DVN LayerZero Labs dalam konfigurasi "1-of-1", memaksa minimum
  5-of-5 untuk DVN internal LayerZero Labs.

CARA MENGISI CITATION — PENTING, INI PERBAIKAN DARI KEGAGALAN SEBELUMNYA: satu field "Evidence:" tunggal
di AKHIR seluruh blok event (yang berisi 8+ sub-fakta: Trigger, 7 sub-field Context Snapshot, Decision,
Execution, 2 Outcome) TERBUKTI GAGAL — itulah yang terjadi di draf ini. Sebagai gantinya, tempelkan sumber
LANGSUNG setelah sub-bagian yang paling relevan, jadi minimal 3 titik sitasi per event, bukan 1:
  Trigger: ... (HIGH/MEDIUM/LOW) [sumber]
  Context Snapshot: ... (boleh 1 sitasi untuk seluruh Context Snapshot kalau satu sumber sama menjelaskan
    semuanya, atau per-sub-field kalau sumbernya beda-beda)
  Decision/Execution: ... (HIGH/MEDIUM/LOW) [sumber]
  Short-term/Long-term Outcome: ... (HIGH/MEDIUM/LOW) [sumber]
Field "Evidence:" di akhir blok tetap ada, tapi isinya boleh ringkasan/sumber utama saja — sitasi yang
SUNGGUHAN menempel di sub-bagian seperti di atas, bukan menunggu sampai akhir blok.

ATURAN MUTLAK UNTUK 13 EVENT YANG SUDAH ADA:
- JANGAN tambah fakta baru pada 13 event ini. JANGAN riset ulang. JANGAN hapus atau ubah fakta apa pun
  yang sudah ada (isi Date/Event/Trigger/Context Snapshot/Decision/Execution/Short-term Outcome/Long-term
  Outcome semuanya harus identik dengan versi di atas, kata per kata — kamu HANYA menyisipkan sitasi di
  antara/sesudah kalimat yang sudah ada, tidak mengubah kalimatnya).
- Kalau kamu benar-benar tidak bisa menemukan sumber spesifik untuk sebuah sub-bagian, tulis
  "[sumber tidak dapat diverifikasi ulang — perlu riset tambahan]" — JANGAN mengarang URL atau nama
  sumber yang tidak pernah kamu gunakan.

UNTUK 2 EVENT BARU: tulis blok LENGKAP dengan format yang SAMA PERSIS seperti 13 event di atas —
Date/Event/Trigger/Context Snapshot (semua sub-field)/Decision/Execution/Short-term Outcome/Long-term
Outcome — riset dan isi sungguhan, JANGAN cuma satu kalimat. Sitasi WAJIB menempel per sub-bagian SEJAK
AWAL kamu menulisnya (pakai cara sitasi di atas, jangan ulangi kesalahan yang sama). Sambungkan ke entitas
Phase 2 jika relevan (LayerZero Labs, Kelp DAO, dst — sebut nama persis seperti Phase 2).

UNTUK SEMUA (13 lama + 2 baru): pastikan SETIAP field (Date/Event/Trigger/Context Snapshot/.../Evidence)
ada di baris terpisah, bukan digabung jadi satu paragraf. Urutkan seluruh 15 event secara kronologis.

Mulai sekarang, keluarkan hasil lengkapnya (seluruh 15 blok event), tanpa penjelasan tambahan.
```

**Result:** pending — awaiting output.

## Phase 4 — Technology Intelligence (sent 2026-07-25)

```
Menggunakan output Foundation Intelligence (Phase 1), Entity Intelligence (Phase 2), dan Historical
Intelligence (Phase 3) di atas sebagai konteks, bangun PROFIL TEKNOLOGI untuk LayerZero. HANYA teknologi —
JANGAN bahas token, tokenomics, atau topik finansial (itu Phase 5 dan 6).

=== YANG SUDAH DIKETAHUI — WAJIB DIPERDALAM, JANGAN DILEWATKAN ===
- Arsitektur V1: model "Ultra Light Node" (ULN) — memisahkan verifikasi pesan (Oracle) dari relay pesan
  (Relayer), dua pihak independen yang harus sepakat sebelum pesan dieksekusi.
- Arsitektur V2 (diluncurkan Januari 2024): model DVN (Decentralized Verifier Network) yang menggantikan
  Oracle+Relayer tunggal — developer bisa memilih/menyusun sendiri kombinasi DVN yang memverifikasi pesan
  mereka ("configurable security stack").
- Nama-nama library Endpoint yang HILANG dari Phase 1 dan perlu direcover di sini secara teknis:
  SendUln302, ReceiveUln302, ReadLib1002 — apa fungsi masing-masing dalam arsitektur V2?
- Konfigurasi DVN 1-of-1 pada Kelp DAO (April 2024, kerugian $292 juta dari Phase 3) — SECARA TEKNIS apa
  artinya "1-of-1", kenapa ini rentan, dan bagaimana ini berbeda dari konfigurasi DVN yang direkomendasikan
  (multi-DVN)?
- Auditor yang sudah dipetakan di Phase 2: Trail of Bits, Zellic, Zokyo, Peckshield, Hacken — untuk
  KOMPONEN APA masing-masing melakukan audit, dan KAPAN?
- Framing "Bridging Trilemma" (hilang dari Phase 1, perlu direcover) — apa klaim LayerZero soal trilema ini
  (trade-off antara trustlessness, generalizability/extensibility, dan cost/latency yang menurut mereka
  diselesaikan oleh arsitektur mereka) dan bagaimana ini dibandingkan dengan pendekatan trilema lain
  (misal Nakamoto trilemma, blockchain trilemma) yang sudah umum di industri?
- Roadmap blockchain "Zero" (jika ada rencana chain/layer sendiri di luar messaging protocol) — statusnya
  sekarang apa?
- Chainlink sebagai penyedia Oracle di V1, dan Chainlink CCIP / Google Cloud / Polyhedra sebagai opsi DVN
  di V2 (dari Phase 2) — secara TEKNIS bagaimana masing-masing terintegrasi ke stack LayerZero?

=== FORMAT OUTPUT ===
Architecture: <value>
Consensus Mechanism: <value atau "n/a">
VM / Execution Environment: <value>
Languages/Frameworks: <value>
Security Model: <value — termasuk penjelasan ULN vs DVN, dan makna teknis konfigurasi N-of-M>
Audit History: <auditor — tanggal — cakupan audit; ulangi per audit, atau "tidak diungkapkan">
Scalability Approach: <value>
Known Limits: <value — termasuk apa yang membuat insiden Kelp DAO mungkin terjadi secara teknis>
Protocol Evolution: <nama upgrade — tanggal — apa yang berubah secara teknis; ulangi per upgrade,
  WAJIB cakup transisi V1 → V2>
Current Roadmap: <value — termasuk status roadmap "Zero" kalau ada>
Novelty Assessment: <apa yang benar-benar baru vs. adaptasi dari teknologi sebelumnya, dengan dasar —
  termasuk evaluasi klaim "Bridging Trilemma" mereka>

Open Threads
- <hal yang masih belum pasti, bertentangan, atau perlu digali lebih lanjut>

[+ FORMAT RULES yang sama seperti fase sebelumnya: Bahasa Indonesia, tanpa tabel, satu fakta per baris,
Evidence + Evidence Level menempel di tiap fakta, jangan mengarang, awali dengan "PROJECT: LayerZero"]
```

**Result:** technically excellent — deep, precise recovery of every requested item (SendUln302/
ReceiveUln302/ReadLib1002 mechanics, Kelp DAO 1-of-1 explained down to the RPC-poisoning mechanism,
all 5 Phase 2 auditors with scope+dates, Bridging Trilemma vs. Nakamoto/Blockchain trilemma, "Zero"
blockchain roadmap — which turned out to already be LIVE as of 10 Feb 2026, not just planned). Bonus
find: a 6th auditor, **ClawSecure** (Feb 2026), not present in Phase 2's entity graph — flagged as a
Phase 2 gap to recover, same pattern as Chainlink/Google Cloud/Polyhedra were for Phase 1→2. Also
surfaced 2 real historical events (Zero launch Feb 2026, DVN systemic security fix May 2026) not present
in Phase 3's timeline — folded into the revised Phase 3 reformat prompt above instead of a separate pass.

**Same citation failure as Phase 1 (original) and Phase 3: zero inline Evidence/Evidence Level anywhere
in the document** (verified: 0 matches for "(HIGH)"/"(MEDIUM)"/"(LOW)", 0 inline source citations) —
a 21-source bibliography exists at the end, unlinked to individual facts. Third occurrence of this exact
failure mode despite the rule being present since Phase 1 and repeatedly tightened. A citation-only
reformat pass was requested below.

## Phase 4 citation reformat pass (sent 2026-07-25, same day)

```
Tugas kamu sekarang HANYA MEMPERBAIKI CITATION pada profil teknologi LayerZero di atas. Ini BUKAN riset
baru.

MASALAH: TIDAK ADA satu pun fakta di 11 field (Architecture, Consensus Mechanism, VM/Execution
Environment, Languages/Frameworks, Security Model, Audit History, Scalability Approach, Known Limits,
Protocol Evolution, Current Roadmap, Novelty Assessment) yang punya Evidence Level atau sumber
terlampir. ini tidak bisa diterima — setiap klaim teknis harus bisa dilacak ke sumbernya, apalagi klaim
sedetail ini.

ATURAN MUTLAK:
- JANGAN tambah fakta baru. JANGAN riset ulang. JANGAN hapus atau ubah fakta apa pun yang sudah ada —
  setiap kalimat harus identik dengan versi di atas, kata per kata.
- Pecah setiap field yang berisi paragraf panjang (seperti Architecture, Security Model, Known Limits,
  Novelty Assessment) menjadi BEBERAPA BARIS FAKTA TERPISAH — satu klaim teknis per baris — bukan satu
  paragraf raksasa. Ini bukan menghapus/meringkas isi, hanya memecah paragraf yang sudah ada menjadi
  bullet-bullet "Label: klaim (Evidence Level) [sumber]".
- Untuk SETIAP baris fakta, tempelkan Evidence Level (HIGH/MEDIUM/LOW) dan sumber konkret dari daftar
  "Karya yang dikutip" di atas — format: "(HIGH) [sumber 6, docs.layerzero.network]".
- Kalau kamu benar-benar tidak bisa memetakan sebuah fakta ke sumber spesifik dari daftar itu, tulis
  "[sumber tidak terpetakan]" — JANGAN mengarang nomor atau nama sumber.
- Untuk Audit History dan Protocol Evolution yang sudah berbentuk daftar per-item, cukup tempelkan
  Evidence Level + sumber ke tiap item, tidak perlu dipecah lagi.

Mulai sekarang, keluarkan hasil perbaikannya saja (seluruh 11 field, lengkap), tanpa penjelasan
tambahan.
```

**Result:** pending — awaiting output.

## Phase 5 — Financial Intelligence (sent 2026-07-25; REVISED same day — see note below)

**Revision note:** the original version of this prompt told the model to "use Phase 1-4 outputs above as
context," implying all 4 raw documents needed to be re-pasted. That instruction was wrong and has been
corrected here — see the "Context Pack" fix in `Phased-Research-Prompts.md` § How to use these, point 3.
**Context actually needed for this phase:** paste Phase 1's finished output in full (short, cheap). Phase
2/3/4 are NOT needed in full — every fact this phase depends on from them is already injected directly
into the prompt below as a compact block, not left for the model to dig out of long documents.

```
Menggunakan output Foundation Intelligence (Phase 1) di atas sebagai konteks, bangun PROFIL FINANSIAL
untuk LayerZero. HANYA ekonomi pendanaan/pendapatan — JANGAN bahas tokenomics/alokasi supply (itu
Phase 6).

=== RONDE PENDANAAN YANG SUDAH DIKETAHUI — WAJIB DIPERDALAM DENGAN DETAIL, JANGAN CUMA DIULANG ===
- Seed — April 2021 — $2 juta — investor termasuk Multicoin Capital, Coinbase Ventures
- Series A — September 2021 — $6 juta — investor termasuk Delphi Digital, Multicoin Capital (lanjutan)
- Series A Extension — Maret 2022 — $135 juta (valuasi $1 miliar, status unicorn) — dipimpin a16z crypto,
  investor lain: Sequoia Capital, PayPal Ventures, Alameda Ventures/FTX Group
- Series B — April 2023 — $120 juta (valuasi $3 miliar) — investor termasuk a16z crypto (lanjutan),
  Sequoia Capital (lanjutan), Circle Ventures, OKX Ventures, Christie's, Samsung Next

CARI YANG BELUM ADA: lead investor pasti untuk Seed dan Series A (siapa yang MEMIMPIN, bukan cuma
berpartisipasi)? Apakah ada ronde pendanaan LAIN yang belum tercatat (strategic round, token sale
pra-TGE di luar 4 ronde di atas)?

=== TERHUBUNG KE TEMUAN PHASE 2 & 3 — WAJIB DIJAWAB SECARA FINANSIAL DI SINI ===
Dari Phase 2: FTX Recovery Trust menggugat LayerZero Labs untuk memulihkan **$70 juta investasi ekuitas**
dan **$41 juta transfer preferensial (clawback)** — total exposure finansial ~$111 juta.
Dari Phase 3: proses hukum berjalan September 2023 (filing) hingga Maret 2024 (penyelesaian briefing atas
Motion to Dismiss), dan LayerZero disebut sempat membeli balik (buyback) saham ekuitas FTX.
PERTANYAAN FINANSIAL YANG BELUM TERJAWAB:
- Bagaimana status litigasi ini SEKARANG (2026)? Menang, kalah, settlement (berapa nilainya kalau ada),
  atau masih berjalan?
- Apakah LayerZero benar-benar membayar kembali sebagian/seluruh $111 juta itu? Berapa nilai buyback
  ekuitas FTX yang disebut di Phase 3, dan dari mana dananya (treasury? ronde pendanaan baru?)?
- Apakah ada dampak pada treasury/runway perusahaan akibat kewajiban hukum ini?

=== FORMAT OUTPUT ===
Untuk SETIAP ronde pendanaan, ulangi blok ini (setiap baris di dalam blok pakai sitasinya sendiri, JANGAN
satu Evidence untuk seluruh blok):
Funding Round: <tipe>
  Date: <value> (Evidence Level) [sumber]
  Amount: <value + mata uang> (Evidence Level) [sumber]
  Lead Investor: <value> (Evidence Level) [sumber]
  Participating Investors: <value> (Evidence Level) [sumber]
  Valuation: <value atau "tidak diungkapkan"> (Evidence Level) [sumber]
---

Lalu, sekali saja (SETIAP baris di bawah ini WAJIB punya sitasinya sendiri — kalau jawabannya butuh lebih
dari 2 kalimat, pecah jadi sub-bullet, masing-masing dengan sitasi sendiri, JANGAN satu paragraf besar
tanpa sitasi seperti yang terjadi di Phase 4):
Treasury Size: <value atau "tidak diungkapkan"> (Evidence Level) [sumber]
Treasury Composition: <value> (Evidence Level) [sumber]
Revenue Model: <value> (Evidence Level) [sumber]
Revenue Figures: <value + tanggal, atau "tidak diungkapkan"> (Evidence Level) [sumber]
Burn Rate: <value, atau "estimasi X — dasar perhitungan: ...", atau "tidak diungkapkan"> (Evidence Level)
  [sumber]
Token Sale Structure: <syarat public/private sale + jumlahnya — BUKAN alokasi %, itu Phase 6>
  (Evidence Level) [sumber]
Runway Estimate: <value + dasar perhitungan, atau "tidak dapat dihitung"> (Evidence Level) [sumber]
FTX Litigation Financial Impact: <ringkasan status terkini + angka riil yang dibayar/masih jadi
  kewajiban — pecah jadi beberapa sub-bullet kalau perlu, MASING-MASING dengan sitasi sendiri>

Open Threads
- <hal yang masih belum pasti, bertentangan, atau perlu digali lebih lanjut>

[+ FORMAT RULES yang sama seperti fase sebelumnya, DITEGASKAN ULANG karena sudah gagal 3 kali berturut-
turut di fase sebelumnya: Bahasa Indonesia, tanpa tabel, sitasi menempel LANGSUNG di baris faktanya
sendiri (bukan dikumpulkan di akhir), field/baris tidak boleh berupa paragraf panjang tanpa sitasi —
kalau lebih dari 2 kalimat WAJIB dipecah jadi sub-bullet bersitasi, jangan mengarang, awali dengan
"PROJECT: LayerZero"]
```

**Result:** pending — awaiting output.
