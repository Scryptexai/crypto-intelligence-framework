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

**Result:** pending — awaiting output.
