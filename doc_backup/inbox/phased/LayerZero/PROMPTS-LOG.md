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

**Result:** failed on its own core objective. All 13 pre-existing events received the fallback
placeholder ("[sumber tidak dapat diverifikasi ulang — perlu riset tambahan]") on **every single
field with no exception** — the model never actually attempted a source search, it just applied the
escape hatch universally. The 2 new events were researched well (Zero blockchain launch, DVN systemic
security fix) but the citation FORMAT regressed to the exact single-Evidence-line-at-the-end pattern
the prompt explicitly called out as the failure to avoid. The "Open Threads" (4 items) and "Kesimpulan
Strategis" sections from the source document were also silently dropped. Not committed to the repo —
see the attempt-3 prompt below.

## Phase 3 citation reformat, attempt 3 (drafted 2026-07-25, addressing attempt-2's fallback overuse)

Same objective as attempt 2, but: (1) explicitly caps fallback-placeholder usage to "a small minority
of fields, not the majority or all of them" since attempt 2 applied it universally instead of actually
searching; (2) the 2 new events are pasted in **already drafted** (verbatim from attempt 2's own
research, which was sound) so the model only has to fix their citation format, not re-research them —
removes the room for it to reintroduce the same single-Evidence-line failure while "researching"; (3)
explicitly requires Open Threads + Kesimpulan Strategis to survive, unchanged; (4) requires the source
list (Phase 3's 21 + Phase 4's 21) to be merged and de-duplicated at the end. Requires both the
pre-reformat Phase 3 draft (`Riset_Timeline_Kronologis_LayerZero.docx`) and the patched Phase 4 file
(`04-technology.docx`, since it demonstrates the correct inline-citation format and is the source for
the 2 new events) as context.

```
Tugas kamu: perbaiki dokumen timeline historis LayerZero (dokumen "Phase 3 LAMA" — 13 event tanpa
sitasi) dengan MENAMBAHKAN SITASI NYATA per sub-bagian, DAN menambahkan 2 event baru yang sudah
didraf di bawah (Peluncuran Zero blockchain 10 Feb 2026, dan Modifikasi Keamanan Sistemik DVN Mei 2026).

KEGAGALAN PADA PERCOBAAN SEBELUMNYA — WAJIB DIHINDARI:
Pada percobaan sebelumnya, SEMUA field di ke-13 event menerima teks placeholder
"[sumber tidak dapat diverifikasi ulang — perlu riset tambahan]" tanpa terkecuali — seolah tidak ada
satu pun sumber yang dicari. Ini TIDAK BOLEH terulang. Placeholder ini HANYA untuk kasus genuinely
tidak ada sumber yang bisa ditemukan setelah kamu benar-benar mencari — perkiraan realistis adalah
placeholder ini muncul di SEBAGIAN KECIL field saja (mungkin 1-3 dari puluhan field total), bukan
mayoritas atau semuanya. Gunakan sumber yang sudah ada di daftar "Karya yang dikutip" dokumen Phase 3
LAMA (21 sumber) sebagai titik awal pencarian, plus pencarian tambahan bila perlu.

CARA MENGISI CITATION: tempelkan sumber LANGSUNG setelah sub-bagian yang relevan (Trigger, tiap
sub-field Context Snapshot, Decision, Execution, Short-term Outcome, Long-term Outcome) — minimal 3
titik sitasi per event, JANGAN satu field "Evidence:" tunggal di akhir blok.

ATURAN MUTLAK UNTUK 13 EVENT LAMA:
- JANGAN tambah fakta baru, JANGAN riset ulang isi faktanya, JANGAN hapus atau ubah kalimat yang sudah
  ada — hanya SISIPKAN sitasi.
- JANGAN HAPUS seksi "Open Threads" (4 poin) dan "Kesimpulan Strategis" di akhir dokumen Phase 3 LAMA —
  salin ulang PERSIS sama seperti aslinya di akhir dokumen hasil (tidak perlu sitasi tambahan di
  seksi ini, itu memang analisis reflektif bukan klaim faktual).

UNTUK 2 EVENT BARU DI BAWAH: kontennya SUDAH BAGUS secara substansi (hasil riset percobaan
sebelumnya, sudah diverifikasi detail dan akurat) — JANGAN riset ulang dari nol, JANGAN ubah faktanya.
Tugasmu HANYA mengubah format sitasinya: dari satu "Evidence:" di akhir menjadi sitasi inline
menempel di tiap sub-bagian sejak kalimat pertama, sama seperti gaya dokumen Phase 4 BARU yang
terlampir (field-nya sudah tersitasi lengkap per klaim, jadikan itu contoh format yang benar). Untuk
2 tabel di bawah (Konfigurasi Topologi "Zero" dan Gelombang Migrasi Institusional), ubah jadi bullet
"Label: Isi (Evidence Level) [sumber]" satu baris per baris tabel — JANGAN pertahankan bentuk tabel di
output akhir.

=== EVENT BARU 1 ===
Date: 10 Februari 2026
Event: Peluncuran Blockchain "Zero" — Layer-1 Mandiri LayerZero (HIGH)
Trigger: Adanya kebutuhan struktural dan urgensi teknologi dari arsitektur keuangan terdesentralisasi
(DeFi) untuk memecahkan trilema skalabilitas (scalability trilemma) secara fisik, bukan sebatas
rekayasa kriptografi di lapisan antarmuka. Batasan ekstrem pada throughput (kemampuan transmisi data)
dan inefisiensi masif pada komputasi replikatif dari mesin virtual tradisional memaksa tim inti
menciptakan fondasi jaringan yang mampu mendukung penyelesaian pasar institusional (Wall Street)
secara on-chain dan nonstop (24/7). Menurut CEO Bryan Pellegrino, hambatan utama yang mencekik
eskalasi tersebut adalah kapasitas penyimpanan lapisan dasar (storage layer constraints), di mana
jaringan yang ada mewajibkan semua node untuk melakukan replikasi validasi secara homogen atas semua
data.
Context Snapshot:
  Industry state: Sektor infrastruktur blockchain sedang mengkalibrasi ulang sasarannya ke Wall
    Street, bertransisi dari taman bermain ritel menuju tulang punggung likuiditas global. Entitas
    kliring raksasa konvensional seperti DTCC (yang merampungkan 99% penyelesaian sekuritas Amerika
    Serikat), ditambah pembuat pasar terbesar Citadel Securities, serta ICE dan ARK Invest, secara
    proaktif terjun menuntut arsitektur blockchain privat, cepat, dan sanggup beroperasi secara masif
    melampaui hambatan geografis dan jam perdagangan reguler.
  Competitor state: Lanskap dominan Layer-1 yang ada, seperti Ethereum atau Solana, dibangun atas
    fondasi yang kaku secara komputasional (single-threaded dan homogen). Arsitektur ini menuntut
    setiap validator mengulang eksekusi dari transaksi yang sama, yang meskipun mengamankan jaringan
    secara konsisten, menciptakan plafon keras di mana jaringan terhebat (Solana) pun secara teoretis
    mentok di ~100.000 transaksi per detik (TPS), membatasi utilitas aplikasi frekuensi tinggi
    (High-Frequency Trading).
  Tech maturity: Laboratorium riset LayerZero telah memantapkan landasan mutakhir untuk mematahkan
    hukum batas tersebut melalui dua peluncuran riset radikal pada 2025. Yang pertama, makalah Quick
    Merkle Database (QMDB) yang berhasil menyuntikkan basis data tambahan (append-only authenticated
    database) yang mencetak tonggak 2,28 juta pembaruan keadaan (state updates) per detik di atas
    ukuran tes 15 miliar entri (10x lipat dari state size seluruh Ethereum tahun 2024), dengan rasio
    konsumsi memori hanya 2,3 byte per entri. Yang kedua, algoritma penjadwalan transaksi FAFO (Fast
    Ahead-of-Formation Optimization) memacu kinerja multi-core hingga menembus 1,1 juta transfer
    Ethereum murni per detik di lingkungan CPU tunggal.
  Macro conditions: Stabilitas iklim ekonomi makro dan kelelahan aset inflasioner (fiat) menyebabkan
    aliran kapital berbobot masif untuk menetap di ekosistem perpesanan lintas rantai. Hal ini
    divalidasi oleh keputusan Tether Investments yang menanam modal setara nilai strategis tinggi di
    ekosistem LayerZero pada hari yang sama, dipicu oleh capaian sirkulasi stablecoin perintis mereka,
    USDt0, yang sanggup meroket melampaui $70 miliar perputaran total tanpa hambatan (frictionless)
    selama 12 bulan terakhir. Ekosistem bergerak menjauh dari kebingungan bridging yang memperlambat
    laju modal.
  Hunter/user population: Di ranah ritel dan paus (whales), delegator kapital merasa kelelahan dan
    terisolasi dari proses validasi (staking). Ada permintaan tinggi terhadap mekanisme staking tanpa
    risiko kehancuran nilai (slashing risk) dari node yang melakukan kesalahan konfigurasi secara
    teknis, suatu beban hantu (ghost liability) yang ditakuti dalam jaringan tradisional seperti
    Ethereum Proof-of-Stake.
  VC climate: Laporan alokasi investasi kuartal awal 2026 menegaskan minat hiperbolik perusahaan modal
    ventura untuk mendanai infrastruktur yang membuktikan utilitas fundamental nyata, bukan sebatas
    kerangka modul jembatan. Sektor ventura agresif beralih dari peluncuran L2 generik yang usang (OP
    Stack forks) menuju pendanaan mesin validasi Zero-Knowledge (ZK) dan multi-core yang membawa
    dampak deflasioner.
  Narrative: Wacana pasar mengalami revolusi konseptual; dari "Jembatan Antar-Jaringan"
    (Interoperability Protocol) yang memfasilitasi perjalanan, LayerZero bertransformasi menjadi
    destinasinya sendiri—"Decentralized Multi-Core World Computer". Terbongkarnya narasi semu
    desentralisasi (The Noble Lie) di jaringan lama membangkitkan tesis bahwa pengukuhan independensi
    sejati sebuah rantai hanya dapat dicapai melalui validasi mikro (nano validators) yang
    mendemokratisasikan sistem penyelesaian langsung kepada publik luas.
Decision: Menghadapi konstelasi kekuatan finansial Wall Street dan kesiapan modul QMDB internal,
kepemimpinan LayerZero Labs di bawah Pellegrino dan Zarick meresmikan keputusan ekstrem dan berisiko
untuk tidak membatasi perusahaan sebagai lapisan interkoneksi belaka, melainkan bertransformasi
menjadi pesaing langsung Layer-1 raksasa. Mereka menolak peta jalan sentralisasi, menyepakati
arsitektur yang 100% immutable (tidak dapat diubah setelah implementasi basis), dengan arsitektur
pemisahan (decoupled architecture) eksklusif antara mesin eksekusi operasional dengan utilitas
verifikasi kriptografi ZK-Proofs.
Execution: Jaringan Zero diluncurkan secara struktural dengan mengimplementasikan topologi yang
memutus siklus redundan, melahirkan desain heterogen yang menyerupai cara kerja CPU multi-core modern.
Node di jaringan dibagi ketat menjadi dua kasta yang koheren. Pertama, Block Producers (berkemampuan
hardware skala perusahaan) yang bertugas mengeksekusi langsung rangkaian transaksi dan mencetak
validasi ZK (Zero-Knowledge Proofs). Kedua, Block Validators (pengguna kasual dengan hardware
konsumtif biasa) yang bertugas sebatas memverifikasi bukti kriptografi tersebut tanpa perlu meniru dan
mengulang proses komputasi yang mahal, membuat beban keikutsertaan turun ke titik mendekati nol. Untuk
pengamanan aset (staking), LayerZero menerapkan konsensus murni dan revolusioner Pure Delegated Proof
of Stake (PDPoS). Secara radikal, arsitektur ini mencabut kewajiban minimal modal penjaminan
(self-stake) dari validator dan sepenuhnya mengeliminasi risiko slashing di ranah lapisan konsensus;
memastikan kepemilikan ritel tidak akan pernah disita akibat cacat pengoperasian node. Lebih mendalam,
seluruh jaringan dimodularisasi menjadi "System Zone" khusus yang secara eksklusif memelihara
stabilitas delegasi validator dan pergerakan token fundamental ZRO, terpisah secara logis dari
"Atomicity Zones" paralel (dianalogikan sebagai aplikasi terpisah atau smart contracts) yang
mengakomodasi transaksi finansial institusional eksternal.
Detail arsitektur teknis (ubah jadi bullet bersitasi, JANGAN tabel):
  - Quick Merkle Database (QMDB): Database append-only dengan arsitektur twig-based yang mereduksi
    footprint menjadi 2,3 bytes/entri dengan 2,28 juta state updates/sec. Menembus plafon I/O-bound
    komputasi jaringan; memfasilitasi finalisasi ultra-cepat yang mensyaratkan 1 juta TPS teoretis.
  - Fast Ahead-of-Formation (FAFO): Lapisan optimisasi pra-blok (pre-block packing) untuk sinkronisasi
    minimal pada pengoperasian Rust EVM client. Membabat kelumpuhan single-thread dengan linearitas
    kinerja CPU multi-core; menghasilkan 1,1 juta transfer ETH murni/detik.
  - Pure Delegated Proof of Stake (PDPoS): Kerangka konsensus tanpa minimum stake yang secara mutlak
    menolak pemotongan penalti aset (no consensus-layer slashing). Melenyapkan kecenderungan
    pemusatan kekuasaan (tokenomics-driven centralization), menjamin yield minim risiko untuk
    delegator besar/ritel.
  - The System Zone vs Atomicity Zones: Pemisahan (decoupling) antara zona operasional sistem inti
    (peredaran ZRO/tata kelola) dan lingkungan zona kontrak pintar spesifik. Mengisolasi ledakan
    transaksi aplikasi (DDoS) dari mengganggu validasi keandalan fundamental konsensus keseluruhan
    jaringan.
  - Block Validators & Nano Validators: Lapisan jaringan di mana node hanya diwajibkan untuk menguji
    kebenaran ZK Proofs ketimbang mengulang rekam jejak eksekusi dari nol. Merealisasikan
    desentralisasi sejati melalui penghancuran rasio biaya masuk (infrastructure barriers); komputasi
    berat diserahkan ke Producers.
Short-term Outcome: Demonstrasi kemampuan publik ini melepaskan gelombang euforia valuasi yang tajam
terhadap aset perbendaharaan dasar mereka. Model insentif token ZRO direstrukturisasi secara instan
dengan janji aktivasi skema "Fee Switch" pasca-peluncuran. Skema ini mengarahkan persentase pajak
perpesanan lintas jaringan langsung menuju pusaran siklus penyerapan pembelian kembali dan pembakaran
suplai (buyback and burn), mengubah token ZRO dari aset pemerintahan nir-pendapatan (yang hanya
bersandar pada spekulasi hasil utilitas kelak) menjadi jangkar ekonomi berkarakteristik deflasi
(deflationary pressure) yang sangat menguntungkan di pasar.
Long-term Outcome: Dengan proyeksi penyebaran mainnet pada momentum musim gugur 2026, LayerZero
membingkai posisi absolutnya bukan semata memonopoli integrasi rantai melainkan membangun infrastruktur
pasar modal masa depan. Dukungan arsitektur institusional dari raksasa seperti DTCC dan Citadel
meletakkan prasyarat absolut untuk mendisrupsi dominasi bursa sentral (Wall Street), di mana efisiensi
ZK-Proofs dan keandalan multi-core akan mengakomodasi triliunan dolar volume perdagangan yang mengalir
selama 24 jam sehari, 7 hari seminggu dengan privasi yang sebelumnya mustahil dijamin jaringan publik.
Sumber mentah yang tersedia (petakan ke sub-bagian yang sesuai, jangan taruh sebagai satu blok akhir):
Publikasi Resmi LayerZero Labs "Zero Blockchain Announcement" (Februari 2026); Dokumen Teknis Zero
Positioning Paper; Repositori Arsitektur Riset QMDB dan FAFO (arXiv); LayerZero Unveils Zero Blockchain
To Revolutionize Wall Street - Evrim Ağacı; Zero - LayerZero Docs (docs.layerzero.network/chain);
arXiv:2501.05262v3 [cs.NI]; QMDB All The Things - commonware.xyz; FAFO whitepaper (arxiv.org/pdf/2507.10757
dan layerzero.network/publications/FAFO_Whitepaper.pdf); Tether Bets Big on LayerZero - Earnpark; Zero:
Technical Positioning Paper - layerzero.network/blog/zero-technical-positioning-paper.

=== EVENT BARU 2 ===
Date: Mei 2026
Event: Modifikasi Keamanan Sistemik DVN dan Eksodus Migrasi Klien Jembatan (HIGH)
Trigger: Ekosistem kriptografi didera kepanikan dan guncangan (trust collapse) destruktif menyusul
keberhasilan eksploitasi peretasan senilai $292 juta yang secara kejam menguras perbendaharaan 116.500
aset rsETH dari jembatan lapisan likuiditas Kelp DAO pada bulan April 2026 (catatan tanggal: insiden
Kelp DAO utama sudah tercatat di timeline sebagai April 2024 — verifikasi ulang apakah ini insiden yang
sama dirujuk-ulang di 2026 pasca litigasi, atau insiden Kelp DAO KEDUA yang terpisah di April 2026; jika
ambigu, tandai sebagai "(konflik/perlu verifikasi tanggal)" dan JANGAN memilih salah satu tanpa bukti).
Analisis forensik dan intelijen jaringan secara cepat mengonfirmasi bahwa kerentanan berasal dari
serangan Remote Procedure Call (RPC) beracun, didalangi oleh kelompok peretas proksi negara-bangsa
(Lazarus Group asal Korea Utara), yang berhasil meretas relai karena Kelp DAO menetapkan asumsi
keamanan secara fatal. Mereka menerapkan arsitektur validasi "1-of-1", di mana protokol itu secara
sepihak menyandarkan verifikasinya hanya pada jaring pengaman tunggal Decentralized Verifier Network
(DVN) kepunyaan LayerZero Labs, tanpa mengonfigurasi validator sekunder atau redundansi penyeimbang
sama sekali.
Context Snapshot:
  Industry state: Paradigma sentimen dari keamanan protokol (bridge security) tengah bermigrasi dari
    narasi euforia pertumbuhan teknis menuju realitas asuransi perlindungan asimetris. Insiden
    tersebut menjadi titik puncak kesabaran di mana institusi bervolume besar mulai menghitung ulang
    bahwa premi operasional atas jembatan yang tersertifikasi enterprise-grade jauh lebih murah
    ketimbang kehilangan miliaran dolar semalaman (zero-day wipeout).
  Competitor state: Manuver tanpa ampun dilancarkan oleh protokol interoperabilitas kompetitor seperti
    Chainlink CCIP, yang dengan sigap memanipulasi kecemasan ini menjadi senjata akuisisi klien.
    Mengedepankan fitur pemblokir kecepatan bawaan (built-in rate limits) dan jaringan tepercaya dari
    16 node entitas independen yang keamanannya telah diganjar sertifikat kelayakan kontrol komersial
    (ISO 27001 dan SOC 2 Type II), Chainlink menancapkan hegemoni kepercayaan baru di atas keruntuhan
    citra LayerZero.
  Tech maturity: Tesis modularitas dari infrastruktur (LayerZero V2) yang sempat dipuja karena
    menjunjung fleksibilitas Keamanan Milik Aplikasi (Application-Owned Security) kini terbongkar
    fatalitasnya. Filosofi desain yang memberikan kebebasan kustomisasi 100% bagi developer klien
    (dApps) tersebut secara empiris menjadi pisau bermata dua saat pengembang yang naif atau
    menghemat biaya (cost-cutting) justru gagal memahami kedalaman ancaman (threat modeling) dan
    tidak menerapkan perlindungan fundamental.
  Macro conditions: Pertumbuhan ekstrem dari instrumen Restaking dan ekosistem agregat Bitcoin DeFi
    (BTCfi) menumpuk miliaran kapital riil yang terpapar pada arsitektur penyelesaian perpesanan
    (settlement messaging). Keruntuhan titik temu ini bukan sekadar hilangnya dana tunggal, melainkan
    dapat menginjeksi triliunan utang macet (bad debt) ke tulang punggung platform pinjaman besar
    (misal Aave).
  Hunter/user population: Gelombang pesimisme ritel dan kepanikan modal meledak. Aktor finansial dari
    investor malaikat hingga entitas pengelolaan mandiri menarik keluar likuiditas lintas batas
    dengan panik dari ekosistem yang dibangun menggunakan pelengkap jaringan LayerZero yang belum
    dievaluasi ulang konfigurasinya.
  VC climate: Laporan komite manajemen risiko pemodal ventura (VC compliance board) merespons
    histeria eksploitasi Kelp DAO dengan memaksakan perombakan protokol terhadap anak-anak perusahaan
    inkubasi mereka, menitahkan migrasi ke infrastruktur jembatan mana pun yang mampu meredam
    atribusi hukum akibat penipuan simpul tunggal (single point of compromise).
  Narrative: Sektor Web3 secara vokal mendeklarasikan akhir dari kemewahan doktrin "Kode Bukan
    Tanggung Jawab Infrastruktur" (laissez-faire architecture). Publikasi dan opini menuntut bahwa
    penyedia perangkat lunak middleware tidak lagi pantas sekadar menjual alat; mereka wajib berperan
    sebagai sipir yang memaksakan standar keselamatan wajib minimal (guardrails) bagi integrasi smart
    contract.
Decision: Mengikuti eskalasi kebuntuan publik di mana entitas korporasi sempat secara reaktif
melemparkan beban tanggung jawab atas cacat peracunan semata-mata pada keteledoran konfigurasi Kelp
DAO ("1-of-1"), direksi eksekutif LayerZero Labs mengambil rute putar balik. Untuk menstabilkan
reputasi yang tergerus, mereka mengeluarkan deklarasi pengakuan resmi, menyadari "kesalahan kami" (we
made a mistake) dalam membiarkan DVN milik lab memvalidasi aset bernilai hiperbolik tanpa pengawasan,
serta menetapkan kebijakan penarikan dukungan untuk konfigurasi fatal sekelas itu tanpa kompromi.
Execution: Pagar perlindungan sistemik diinjeksi secara vertikal. LayerZero menyebarkan patch pada
lapisan akar klien (endpoints), mencabut (deprecate) opsi konfigurasi otorisasi "1-of-1" jika jaringan
verifikator yang digunakan adalah DVN kelolaan LayerZero Labs. Mereka memaksakan prasyarat tata letak
keamanan (security default) minimum untuk jalur perlintasan utama (high-value corridors) ke standar
konsensus "5-of-5", dan memberikan standar relaksasi absolut minimum "3-of-3" bagi rantai kecil yang
miskin ketersediaan verifikator komersial. Pada audit server proksi dalam (internal hygiene), mereka
menyingkirkan kunci pemegang multi-sig kuno (salah satu penandatangan kedapatan ceroboh pernah
menggunakan peranti dompet keras yang sama untuk transaksi pribadi tiga tahun lampau), mengganti
seluruh tata rotasi otorisasi kriptografis, menanamkan pertahanan deteksi anomali pada tingkat mesin
(localized anomaly detection), serta mengaktifkan ekosistem multi-sig baru bernama OneSig.
Detail eksodus institusional (ubah jadi bullet bersitasi, JANGAN tabel):
  - Kelp DAO: melakukan re-rute bridging untuk aset sisa rsETH akibat kerusakan hubungan dan sengketa
    publik atribusi pasca malapetaka peretasan 116.500 aset rsETH → migrasi ke Chainlink CCIP.
  - Solv Protocol: merelokasi $700 juta instrumen Bitcoin-backed (SolvBTC, xSolvBTC) demi proteksi
    infrastruktur dari isolasi konsensus jaringan 16 node bersertifikat CCIP → migrasi ke Chainlink
    CCIP.
  - Re.xyz: mengalihkan $475 juta parameter TVL institusional untuk bersandar pada mekanisme
    peredaman intrinsik batas laju (rate limit) di jaringan baru → migrasi ke Chainlink CCIP.
  - Kraken Exchange: memboikot utilitas LayerZero pada jembatan antarmuka spesifik (termasuk wrapped
    token kBTC) karena obsesi kepatuhan dan mandat sertifikasi keselamatan tipe SOC 2 → migrasi ke
    Chainlink CCIP.
  - Lombard: bergabung meruntuhkan likuiditas untuk menyelamatkan nilai di tengah iklim kerentanan dan
    ketidakstabilan arsitektur konfigurasi yang menular (contagion fear) → migrasi ke Chainlink CCIP.
Short-term Outcome: Eksekusi permintaan maaf dan perbaikan keamanan ini terlambat membius luka
industri. Kejadian ini melahirkan krisis migrasi paling masif di sektor Layer-0. Arus keluar kapital
agregat senilai lebih dari $4 miliar USD tumpah ruah dieksoduskan ke arah infrastruktur kompetitor,
Chainlink CCIP, dipimpin oleh raksasa-raksasa manajemen modal seperti Lombard, Re.xyz, Kraken (yang
memindahkan kBTC), dan Solv Protocol, meruntuhkan pangsa retensi eksklusivitas jaringan LayerZero.
Long-term Outcome: Merupakan fase transisi de-facto di mana "Kebebasan Penuh" dari aplikasi yang
memanfaatkan protokol infrastruktur interoperabilitas secara definitif berakhir. Ini memaksa arsitektur
LayerZero V2 berevolusi dari sekadar landasan pacu netral menjadi instrumen fasilitator yang bertangan
besi (paternalistic), memastikan masa depan penyatuan rantai blok tidak lagi bergantung pada kemahiran
tunggal dari rekayasawan pihak ketiga, dan menancapkan keandalan konfigurasi multisig (minimal 5-of-5
DVN) sebagai konstitusi wajib tak tergantikan untuk perpesanan finansial di dekade mendatang.
Sumber mentah yang tersedia (petakan ke sub-bagian yang sesuai, jangan taruh sebagai satu blok akhir):
Catatan Publik "Admitting Mistake" oleh LayerZero Labs (Mei 2026); LayerZero Backtracks After $292M
Kelp Hack, Admits Mistake and Tightens DVN Security - Binance Square; rsETH 攻击事件完整时间线#195 -
qiwihui/blog - GitHub; Lombard joins Chainlink CCIP as LayerZero exodus tops $4b - Bitget News;
LayerZero Says It 'Made a Mistake' in $292 Million Kelp Exploit - ueex.com; Lombard Joins $4B Exodus
from LayerZero to Chainlink CCIP After ... - KuCoin News.

=== ATURAN UMUM UNTUK SELURUH OUTPUT ===
UNTUK SEMUA (13 lama + 2 baru): pastikan SETIAP field (Date/Event/Trigger/Context Snapshot
sub-fields/Decision/Execution/Short-term Outcome/Long-term Outcome/Evidence) ada di baris terpisah,
bukan digabung jadi satu paragraf raksasa. Urutkan seluruh 15 event secara kronologis. Pertahankan
daftar "Karya yang dikutip" di akhir (gabungkan 21 sumber dari Phase 3 LAMA dengan sumber tambahan
yang kamu pakai untuk 2 event baru, beri nomor berkelanjutan, jangan duplikat entri untuk URL yang
sama).

Keluarkan hasil lengkapnya (15 event + Open Threads + Kesimpulan Strategis + Karya yang dikutip),
tanpa penjelasan tambahan.
```

**Result:** failed worse than attempt 2 on the core objective, improved on scope preservation. Verified
by grep: 0 matches for "Evidence" and 0 matches for inline `[sumber N]` tags anywhere in the 13
pre-existing events — the model reproduced them near-verbatim with no citation attempt at all (not even
attempt-2's fallback placeholder). The 2 new events got bare `(HIGH)` tags on their bullet points but
still zero `[sumber]` references — untraceable. Structural defect: **two separate "Karya yang dikutip"
sections** appended (one unnumbered ~30-source list resembling the original bibliography, one numbered
~19-source list of new sources) — never merged, inconsistent formatting. Improvement: "Open Threads" (4
items) and "Kesimpulan Strategis" **did** survive verbatim this time (regression fixed from attempt 2).
Not committed to the repo.

**Root-cause read:** inline per-sub-field citation across a ~150-citation-point document (15 events ×
~10 sub-fields) appears to exceed reliable single-pass execution for this task — the same class of task
(Phase 1, ~20 fields; Phase 4, 11 fields) succeeded when the field count was an order of magnitude
smaller. Decision: descope attempt 4 to one `Evidence:` line per event (15 total, not per sub-field) —
see below.

## Phase 3 citation reformat, attempt 4 (drafted 2026-07-25, descoped after attempt-3 total citation failure)

Descoped from per-sub-field inline citation (attempts 2 and 3, both failed on this specifically) to one
`Evidence:` line per event — 15 total insertions instead of ~150. Reuses attempt-3's output as the base
(content and Open Threads/Kesimpulan Strategis were sound, only citation is missing) and asks the model
to do one narrow mechanical task: append one Evidence line per event drawing from the ~50 sources it
already collected across its own two (currently unmerged) bibliography lists, and merge those two lists
into one de-duplicated numbered list.

```
Tugas kamu sekarang HANYA MENGISI FIELD "Evidence:" pada dokumen timeline LayerZero di atas (dokumen
"Phase 3 attempt-3" — 15 event, isinya sudah bagus dan lengkap, HANYA sitasinya yang kosong total).
Ini BUKAN riset baru dan BUKAN reformat ulang isi.

MASALAH: dokumen ini TIDAK PUNYA satu pun field "Evidence:" di 15 event-nya, dan tidak ada satupun tag
[sumber N] di manapun — padahal dokumen ini sudah punya 2 daftar "Karya yang dikutip" berisi total
~50 sumber (yang kamu kumpulkan sendiri sebelumnya) yang sama sekali tidak dihubungkan ke fakta manapun.

TUGAS SEDERHANA KALI INI (skala lebih kecil dari percobaan sebelumnya, supaya benar-benar tuntas):
Untuk SETIAP dari 15 event (jangan lewatkan satupun), tambahkan SATU baris baru persis setelah
"Long-term Outcome:" event tersebut, dengan format:

Evidence: [sumber X, sumber Y, sumber Z] — <nama singkat 1-3 sumber yang paling relevan untuk event
ini, diambil dari salah satu dari 2 daftar "Karya yang dikutip" di akhir dokumen>

ATURAN:
- JANGAN ubah, hapus, atau tambah fakta apa pun di 15 event yang sudah ada — hanya SISIPKAN baris
  "Evidence:" baru di akhir tiap event.
- JANGAN ubah isi "Open Threads" atau "Kesimpulan Strategis" — salin ulang PERSIS sama.
- GABUNGKAN 2 daftar "Karya yang dikutip" yang saat ini terpisah (baris tanpa nomor + baris bernomor)
  menjadi SATU daftar bernomor berkelanjutan di akhir dokumen, hapus duplikat entri untuk URL yang sama.
  Field "Evidence:" di tiap event WAJIB merujuk ke nomor dari daftar gabungan ini.
- Pilih sumber yang PALING MASUK AKAL secara tematik untuk tiap event (contoh: event "Keruntuhan FTX"
  → cari sumber yang membahas FTX/Alameda/kepailitan di daftar; event "Peluncuran Blockchain Zero" →
  cari sumber yang membahas Zero blockchain/QMDB/FAFO). Kalau benar-benar tidak ada satupun sumber di
  daftar yang relevan untuk sebuah event, tulis "Evidence: [tidak ada sumber spesifik di daftar —
  perlu riset tambahan]" — tapi ini seharusnya jarang terjadi karena daftarnya sudah cukup lengkap.
- Field ini TIDAK perlu granular per sub-bagian (Trigger/Context Snapshot/Decision/dst) — cukup SATU
  baris Evidence per event, di bagian akhir event, seperti dicontohkan di atas.

Keluarkan hasil lengkapnya (15 event dengan Evidence terisi + Open Threads + Kesimpulan Strategis +
satu daftar Karya yang dikutip gabungan), tanpa penjelasan tambahan.
```

**Result:** superseded — never sent to Gemini. The maintainer instead ran a direct Claude research
pass (not Gemini) to build a sourced citation map for all 15 events, which turned out to be
categorically better: real, checkable URLs (CoinDesk, Chainalysis, QuillAudits, PR Newswire, arXiv,
official LayerZero/Tether blogs, court filings) mapped one-to-one to each event, plus explicit
fact-checking against those sources. See the finding and final synthesis below — this superseded
attempt 4 entirely.

## Phase 3 — Claude-direct citation research + final synthesis (2026-07-25)

Departure from the Gemini phased-prompt loop: the maintainer ran Claude's own research (not a Gemini
prompt) to build a sourced citation map for the 15-event timeline, uploaded as
`LayerZero_Labs__Sourced_Citation_Map_and_FactCheck_for_a_15Event...md`. This succeeded where 3 Gemini
attempts failed, and surfaced a critical error the phased pipeline had carried since Phase 3's original
run:

**Critical finding — Kelp DAO exploit date was wrong by two years.** Every prior draft (original Phase
3, both citation-reformat attempts, and Phase 4's Security Model / Audit History sections) dated the
$292M Kelp DAO exploit to **April 2024**, placed right after the LayerZero V2 launch (Jan 2024). The
citation research cross-verified against CoinDesk, Chainalysis, and QuillAudits and confirms the actual
date is **18 April 2026** — one incident, not two, and structurally it belongs *after* the "Zero"
blockchain launch (10 Feb 2026) and *immediately before* the DVN security-hardening event (May 2026),
which is explicitly a response to it. The old "April 2024" placement made the DVN fix read as
disconnected from its own trigger by two years; the corrected placement resolves that.

**Other corrections surfaced:** (1) the ~$2M seed round was led by Multicoin Capital + Sino Global
Capital, not Binance Labs (Binance Labs only joined at the Sept 2021 Series A — the old draft implied
continuity that didn't exist); (2) FTX-trapped treasury funds were $11.5M, not $10.7M; (3) the Stargate
acquisition's DAO approval date is 25 August 2025 (~95%/94.76%) — the old draft had an ambiguous
"August 2024/2025"; (4) the FTX Recovery Trust clawback suit was **settled 31 January 2025** — the old
draft implied it was still unresolved "legal limbo" into 2026; (5) the ZRO TGE price-drop path
"$4.79→$3.39 in 4 hours" could not be verified anywhere — the documented figure is a ~15% drop to
~$2.87 (Cryptopolitan/CoinMarketCap).

**Flagged as unverified (kept as explicit caveats, not silently removed):** the "23-50585" docket
number; the Nov 20 2023 Motion-to-Dismiss / Mar 12 2024 briefing dates (the MTD schedule actually found
in the docket runs Jan–Mar 2025, for the Amended Complaint); the "$111M+" clawback figure (reported
range is $21.37M–~$100M+ depending on components); the Alameda-estate 129M STG → 11.14M ZRO liquidation;
the "80M+ historical messages" metric (later sources cite 200M+); Ondo Finance's multi-DVN adoption;
and — most consequentially — **the entire 6-auditor roster in the already-committed Phase 4 document
(Trail of Bits, Zellic, Zokyo, Peckshield, Hacken, ClawSecure) could not be independently verified**,
with Zokyo specifically appearing only as a Series A Extension *investor* in one source, not an auditor.

**Synthesis performed directly (no further Gemini round needed):** merged attempt-3's sound event
content with this citation map — 15 events, each carrying one `Evidence:` line with 2-5 real URLs,
the Kelp DAO event moved to its correct chronological position and corrected to 18 April 2026, the
other four corrections applied inline (marked `[KOREKSI]`), the unverified items marked
`[TIDAK TERVERIFIKASI]` rather than silently dropped or silently trusted, Open Threads and Kesimpulan
Strategis preserved and extended with the new findings (FTX settlement, ex-COO Ari Litan departure,
audit-roster caveat), and a single de-duplicated 58-source bibliography. Verified structurally: 15/15
events have Date/Event/Evidence fields (`grep -c` check), and the corrected `.docx` passes
OOXML schema validation (`validate.py`).

**Active file:** `doc_backup/inbox/phased/LayerZero/03-historical.docx` (supersedes both
`03-historical-attempt3-nocitation.docx`, kept as archived source-of-record per this project's
superseded-version convention, and the original pre-citation Phase 3 draft).

**Follow-up patch applied to the already-committed Phase 4 file** (`04-technology.docx`): the two
"April 2024" Kelp DAO references (Security Model section, Hacken's audit-engagement date in Audit
History) corrected to April 2026 inline, and an Open Threads caveat added noting the 6-auditor roster
is unverified pending a direct check of LayerZero's own audit-disclosure page.

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

**Result:** citation quality was strong — all 11 fields broken into one claim per line, each with
Evidence Level + `[sumber N, domain]`, correctly cross-referenced to the existing 21-source bibliography
(verified: source numbers in the output match the original list, e.g. `[sumber 15, chaincatcher.com]` →
entry 15 = ChainCatcher). One real defect: the reformat pass **silently dropped the "Open Threads" (3
items) and "Karya yang dikutip" (21-source bibliography) sections** from the end of the document —
violates its own "JANGAN hapus fakta apa pun" rule, and without the bibliography the inline `[sumber N]`
tags are undecodable in isolation. Fixed by direct patch (no new Gemini round-trip needed, since the
dropped content was unchanged verbatim text, not new research): both sections appended back from the
pre-reformat source. **Active file:** `doc_backup/inbox/phased/LayerZero/04-technology.docx`.

## Phase 5 — Financial Intelligence (drafted 2026-07-25; REVISED twice — see notes below)

**Revision note 1:** the original version of this prompt told the model to "use Phase 1-4 outputs above as
context," implying all 4 raw documents needed to be re-pasted. That instruction was wrong and has been
corrected here — see the "Context Pack" fix in `Phased-Research-Prompts.md` § How to use these, point 3.
**Context actually needed for this phase:** paste Phase 1's finished output in full (short, cheap). Phase
2/3/4 are NOT needed in full — every fact this phase depends on from them is already injected directly
into the prompt below as a compact block, not left for the model to dig out of long documents.

**Revision note 2 (2026-07-25, before first send):** the "already known" facts and the Phase 2/3
cross-reference block below were written *before* Phase 3's citation research corrected several of the
same facts (see the "Claude-direct citation research" entry above). Caught and fixed prior to sending —
sending the stale version would have asked the model to "deepen" wrong facts, the same trap that produced
Phase 3's original errors. Corrected below: Series A's lead investor (Binance Labs, not just "Delphi
Digital/Multicoin continuation" — Binance Labs is absent from the pre-correction version entirely, which
was the actual gap); Coinbase Ventures/Tiger Global/Uniswap Labs moved from "seed" to Series A Extension
(where they actually participated, per The Block); the Series A Extension's lead is a 3-way co-lead
(Sequoia + FTX Ventures + a16z, per Forbes), not "led by a16z" alone; and — most importantly — the FTX
litigation is **already resolved** (settled 31 January 2025, per Phase 3), so the prompt no longer asks
"is it still ongoing" but asks for the settlement's financial terms instead. The unverified "$111M"
figure is now presented as unverified (reported range $21.37M–~$100M+) rather than as a stated fact.

```
Menggunakan output Foundation Intelligence (Phase 1) di atas sebagai konteks, bangun PROFIL FINANSIAL
untuk LayerZero. HANYA ekonomi pendanaan/pendapatan — JANGAN bahas tokenomics/alokasi supply (itu
Phase 6).

=== RONDE PENDANAAN YANG SUDAH DIKETAHUI — WAJIB DIPERDALAM DENGAN DETAIL, JANGAN CUMA DIULANG ===
- Seed — April 2021 — $2 juta — dipimpin Multicoin Capital dan Sino Global Capital
- Series A — September 2021 — $6 juta ($6,3 juta menurut satu sumber, ada selisih angka) — dipimpin
  bersama Binance Labs (investor baru di putaran ini) dan Multicoin Capital (lanjutan dari seed),
  partisipan baru: Delphi Digital
- Series A Extension — 30 Maret 2022 — $135 juta (valuasi $1 miliar, status unicorn) — co-lead 3 pihak:
  Sequoia Capital, FTX Ventures/Alameda Ventures, dan a16z crypto; partisipan lain: PayPal Ventures,
  Coinbase Ventures, Tiger Global, Uniswap Labs
- Series B — 4 April 2023 — $120 juta (valuasi $3 miliar) — TANPA lead investor tunggal, 33 investor
  termasuk a16z crypto (lanjutan), Sequoia (lanjutan), Circle Ventures, OKX Ventures, Christie's,
  Samsung Next, BOND, Lightspeed, OpenSea Ventures — total pendanaan kumulatif setelah putaran ini: $263 juta

CARI YANG BELUM ADA: Apakah ada ronde pendanaan LAIN yang belum tercatat (strategic round, token sale
pra-TGE di luar 4 ronde di atas)?

=== TERHUBUNG KE TEMUAN PHASE 2 & 3 — WAJIB DIJAWAB SECARA FINANSIAL DI SINI ===
Dari Phase 2: FTX Recovery Trust menggugat LayerZero Labs (Adv. Pro. No. 23-50492-JTD, Delaware) untuk
memulihkan dana — angka yang dilaporkan bervariasi tergantung komponen yang dihitung: $21,37 juta
(preference claim inti) hingga ~$86–100 juta+ (termasuk komponen ekuitas/pinjaman $45 juta). Angka
"$111 juta" yang beredar di draf-draf awal TIDAK ditemukan verbatim di sumber manapun — JANGAN
mengasumsikan angka ini benar, treat sebagai perlu diverifikasi ulang.
Dari Phase 3 (sudah dikoreksi dan dikonfirmasi via riset sitasi terpisah): gugatan ini SUDAH DISELESAIKAN
lewat settlement pada 31 Januari 2025 (dikonfirmasi The Block dan Invezz) — BUKAN "masih berjalan hingga
2026" seperti asumsi draf sebelumnya. LayerZero juga sempat membeli balik (buyback) 100% ekuitas dan waran
FTX/Alameda pada 10 November 2022 (sehari sebelum FTX mengajukan Chapter 11), dengan treasury independen
~$134 juta (~90% kas/stablecoin — rincian: $107 juta kas langsung + $27 juta on-chain per satu sumber),
dan $11,5 juta dana operasional yang tetap terjebak di FTX (bukan $10,7 juta seperti draf lama).
PERTANYAAN FINANSIAL YANG BELUM TERJAWAB:
- Berapa nilai FINAL settlement 31 Januari 2025 itu (angka riil yang dibayar/diselesaikan, bukan angka
  tuntutan awal $21,37 juta–$100 juta+)? Dari sumber mana pendanaannya (treasury? ronde baru?)?
- Apakah ada dampak terukur pada treasury/runway perusahaan akibat proses hukum 2022–2025 ini secara
  keseluruhan (biaya pengacara, dana yang akhirnya dibayarkan dalam settlement, dst)?

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

**Result:** superseded — never sent to Gemini. Following the Phase 3 precedent, the maintainer instead
ran Claude's own research directly, uploaded as
`LayerZero_Labs__Funding_Buybacks_and_Revenue_Economics_Through...md`. Same pattern as Phase 3: real,
checkable citations (Blockworks, DefiLlama, The Block, Law360, Epiq11 docket, Bitcoin Insider, Unchained,
Coinspeaker, Mitrade, Messari, official LayerZero/Tether blogs) mapped to specific facts, plus explicit
fact-checking. See the finding and synthesis below.

## Phase 5 — Claude-direct financial research + final synthesis (2026-07-25)

Cross-checked first against Phase 3's corrected facts (see the "Claude-direct citation research" entry
above) — everything lines up: Series A led by Binance Labs + Multicoin Capital, Series A Extension's
3-way co-lead (Sequoia/FTX Ventures/a16z), Coinbase Ventures/Tiger Global/Uniswap Labs as Extension
participants (not seed), and the 31 Jan 2025 FTX settlement. The financial research adds real depth here:
**the FTX settlement's dollar amount was never publicly disclosed at all** — not merely "not yet found,"
but confirmed via a dedicated docket/press search that no Rule 9019 motion or stipulation with a dollar
figure is publicly retrievable; the sole primary source is CEO Bryan Pellegrino's own X post, which
states only that the "original repurchase" and 40M ZRO were returned, not an amount. This sharpens Phase
3's "$111M is unverified" flag into "the true figure is confidential, full stop" — the reported figures
($21.37M / $86M / "$100M+") are all what FTX *sought*, never what was *paid*.

**Five real capital events surfaced that exist in no other phase's document:** a16z's $55M secondary ZRO
purchase (17 Apr 2025); the Stargate acquisition's actual cash mechanics ($110–120M headline, but only
$25M effective cash cost per LayerZero's own blog, since Stargate's treasury covered $95M of it); a 50M-
ZRO ($~150M combined-year) buyback from early investors (Sep 2025); a $10M discretionary Labs buyback
(Nov 2025); and undisclosed-size Tether/Citadel Securities/ARK Invest investments alongside the "Zero"
announcement (10 Feb 2026, Citadel's first-ever direct token purchase). None of these are priced equity
rounds — LayerZero has raised no new priced round since April 2023, funding everything since via token
buybacks and Stargate-derived revenue instead. Flagged in Open Threads as good future additions to Phase
3's timeline, not added there directly (out of scope for this phase).

**Revenue reality confirmed, not just claimed:** the fee switch is not live (three referendums held,
>96% approval each, but turnout only 3.71–13.01%), so LayerZero Foundation's protocol revenue is
effectively zero — DVN/Executor messaging fees (Messari: >$11.5M in Q1'24; DefiLlama: ~$3.59M annualized
now) flow to third-party operators, not the Foundation. The only real cash reaching the token is
Stargate revenue funding buybacks (~$1.2M of $2.4M Stargate revenue, Sep–Nov 2025). Messari's FDV
valuation scenarios ($290M bear to $19.11B bull) are explicitly projections, not realized revenue.

**Synthesis performed directly** (same rationale as Phase 3 — the research was sourced and precise
enough that a further Gemini round would only risk reintroducing citation loss): 4 funding rounds each
with per-field Evidence Level + real citations, a new "Peristiwa Modal Non-Round" section for the 5 token/
M&A/buyback events (no template slot existed for these — added rather than force-fitting them into
"Funding Round" blocks they don't structurally belong to), the FTX litigation section rewritten to state
the settlement amount as confirmed-undisclosed (not merely unverified) and the "$111M" figure retracted
outright, and an Open Threads section flagging the 5 non-round events as Phase 3 timeline candidates.
Verified structurally before committing: 4/4 Funding Round blocks present, OOXML schema validation
passed.

**Active file:** `doc_backup/inbox/phased/LayerZero/05-financial.docx`. Source research archived at
`05-financial-citation-map-research.md`.

## Phase 1 trim to v3 — scope-creep cleanup (2026-07-25, no new Gemini prompt needed)

**Finding (maintainer flagged, verified correct):** the active Phase 1 file (v2, the reformatted narrative)
was never actually scoped to the Foundation template. It carried ~50 fields instead of the ~20 the template
asks for, front-loading shallow previews of content that Phase 3 (History), Phase 4 (Technology), and the
pending Phase 5 (Financial) each later covered in far more depth — funding rounds, ULN/DVN architecture,
audit history, the Kelp DAO incident, the FTX lawsuit, the "Zero" roadmap, ZRO token allocation, and the
TGE market reaction were all already present in Phase 1, in one-line form. This is why the pipeline felt
like it wasn't progressing: later phases weren't repeating Phase 1 by mistake, they were going deeper on
topics Phase 1 had no business covering in the first place — Phase 1 telegraphed everything shallowly up
front, so genuine later depth read as déjà vu. Two sentences also broke Phase 1's own "facts only, no
analysis" rule ("Strategi Yurisdiksi" and "Konsekuensi Application-owned security" were both interpretive,
not factual).

**Fix — trimmed directly, no new Gemini round-trip needed** (all the source content already existed; this
was a mechanical dedup/reallocation, not new research):
- Old file archived: `doc_backup/deep/LayerZero_2026-07_phase1-outofscope-v2.docx` (kept as source of
  record, same pattern as every other superseded version this project).
- New active file: `doc_backup/inbox/phased/LayerZero/01-foundation.docx` — trimmed to the ~20-field
  template (Official Name/Symbol/Category/Founding Entity/Founders/Core Team/Country/Launch Dates/Main
  Products/channels/Token Contract/Chain/Ecosystem/Open Threads only). 17.7KB raw text → 2.5KB. Existing
  per-fact Evidence Level tags were preserved as-is (Phase 1 was, ironically, already the best-cited phase
  of the four so far — the citation failure only started at Phase 3).
- Content removed because a later phase already fully supersedes it: all 4 funding rounds (→ Phase 5),
  ULN/DVN architecture + security config + audit list + "Zero" roadmap + application-owned-security
  analysis (→ Phase 4), Kelp DAO incident + FTX lawsuit narrative + TGE reaction narrative (→ Phase 3), OFT
  burn-and-mint mechanism (→ already in Phase 4's Novelty Assessment).
- Content removed because it was pure interpretation, not fact (violated Phase 1's own rule): the
  jurisdiction-strategy sentence, the application-owned-security-consequence sentence.

**Content NOT superseded anywhere yet — carried forward here so it isn't lost, to be injected into the
named future phase's prompt when drafted:**
- **→ Phase 6 (Token Intelligence):** ZRO Genesis Allocation — Strategic Partners/Investors 32.20%
  (322,000,000 ZRO), Core Contributors/Team 25.50% (255,000,000), Community/Airdrop 38.30% (383,000,000),
  Tokens Repurchased 4.00% (40,000,000); Total Supply 1,000,000,000 ZRO hard-capped; Community distribution
  — 8.5% available at TGE, remainder over 36 months; Sybil Defense — self-report system (15% allocation
  bounty) + bounty hunter program; Proof-of-Donation mechanism — $0.10/ZRO donation (USDC/USDT/ETH) to
  Protocol Guild required to unlock the initial 8.5% claim; Protocol Guild proceeds — ~$18.5M, LayerZero
  Labs pledged matching up to $10M; market reaction — spot price fell 22% ($4.79→$3.39) in the first 4
  hours, community backlash calling the donation requirement a "pay-to-claim tax."
- **→ Phase 8 (Market Intelligence):** historical message metric (V1) — 80M+ messages processed; value
  transferred — $95B+ secured/facilitated; Stargate Finance TVL — peaked above $3B.
- **→ Phase 7 (Ecosystem Intelligence):** Tether launched USDT0 using LayerZero's OFT standard — needs a
  deeper integration-mechanics pass when Phase 7 is drafted (Phase 2 already has Tether as an entity, but
  the technical integration detail wasn't captured anywhere).

## Phase 6 — Token Intelligence (drafted 2026-07-25)

Context Pack: Phase 1 (full) + Phase 5 (full — needed in full here, not just an index, because Phase 6
must reconcile its Burn Mechanism/Inflation-Deflation fields against Phase 5's buyback findings without
contradicting them). Phase 2/3/4 not needed.

Known facts injected are the ZRO Genesis Allocation figures carried forward from the Phase 1 v2→v3 trim
(see that entry above), with the TGE price-drop figure corrected to match Phase 3's verified ~15%/~$2.87
finding instead of the old unverified "$4.79→$3.39" figure. Explicitly asks the model to reconcile the
Genesis Allocation's "Tokens Repurchased 4.00% (40M ZRO)" bucket against Phase 5's finding that 40M ZRO
was returned to strategic partners as part of the Jan 2025 FTX settlement — same number, provenance not
yet confirmed as the same event. Also asks it to determine whether Phase 5's two post-TGE buybacks
(Sept 2025 50M ZRO, Nov 2025 $10M) burn supply or just move it to treasury — a tokenomics mechanics
question Phase 5 didn't answer since it was out of that phase's scope (buyback economics, not token
mechanics).

```
Menggunakan output Foundation Intelligence (Phase 1) dan Financial Intelligence (Phase 5) di atas sebagai
konteks, bangun PROFIL TOKEN/TOKENOMICS untuk LayerZero (token ZRO). HANYA struktur token dan tata
kelolanya — JANGAN ulangi detail ronde pendanaan ekuitas atau treasury (itu sudah selesai di Phase 5).

=== YANG SUDAH DIKETAHUI — WAJIB DIPERDALAM DENGAN DETAIL, JANGAN CUMA DIULANG ===
- Total Supply: 1.000.000.000 ZRO, hard-capped (fixed supply, bukan inflasionary)
- Alokasi Genesis: Strategic Partners/Investors 32,20% (322.000.000 ZRO); Core Contributors/Team 25,50%
  (255.000.000 ZRO); Community/Airdrop 38,30% (383.000.000 ZRO); Tokens Repurchased 4,00% (40.000.000 ZRO)
- TGE (20 Juni 2024): 8,5% dari total suplai (85 juta ZRO) dapat diklaim saat peluncuran, sisanya dari
  alokasi Community di-vest selama 36 bulan
- Mekanisme klaim "Proof-of-Donation": pengklaim wajib mendonasikan $0,10/ZRO (USDC/USDT/ETH) ke Protocol
  Guild sebelum bisa mengklaim porsi 8,5% awal; proyeksi total donasi ~$18,5 juta, dengan LayerZero
  Foundation mencocokkan (matching) hingga $10 juta
- Sybil Defense: sistem self-report (bounty alokasi 15%) + program bounty hunter untuk memfilter dompet bot
  sebelum klaim
- Reaksi pasar: harga ZRO turun ~15% dalam 24 jam menjadi ~$2,87 menyusul pengumuman Proof-of-Donation
  (dikonfirmasi Phase 3 — BUKAN "$4,79 → $3,39 dalam 4 jam" yang beredar di draf-draf sangat awal dan
  TIDAK terverifikasi; JANGAN pakai angka lama itu)

=== TERHUBUNG KE TEMUAN PHASE 5 — WAJIB DIREKONSILIASI DI SINI ===
Phase 5 menemukan bahwa sebagai bagian dari settlement litigasi FTX (31 Januari 2025), LayerZero
mengembalikan **40 juta ZRO** ke mitra strategis — angka ini SAMA PERSIS dengan bucket "Tokens
Repurchased 4,00%" di alokasi genesis di atas. KONFIRMASI apakah ini memang bucket yang sama (dialokasikan
sejak genesis untuk skenario buyback semacam ini), atau kebetulan angka yang sama tapi asal-usulnya
berbeda — JANGAN mengasumsikan tanpa mengecek sumber.

Phase 5 juga menemukan DUA peristiwa buyback ZRO PASCA-TGE yang terpisah dari alokasi genesis di atas:
- September 2025: buyback 50 juta ZRO (5% suplai) dari investor awal/mitra strategis, ~$150 juta gabungan
  tahun berjalan (termasuk pembelian sekunder a16z $55 juta April 2025)
- November 2025: buyback diskresioner LayerZero Labs $10 juta di pasar terbuka
- Total: perusahaan menyatakan "$112,7 juta dideploy ke buyback ZRO sejak September 2025", mencakup
  19,77% dari total suplai
JELASKAN secara tokenomics: apakah token yang dibeli-balik ini DIBAKAR (burn, mengurangi total supply)
atau disimpan di treasury Foundation/Labs (tidak mengurangi circulating supply tapi mengubah kepemilikan)?
Ini krusial untuk field "Burn Mechanism" dan "Inflation/Deflation" di bawah — Phase 5 tidak menjawab
pertanyaan ini karena di luar cakupannya (ekonomi buyback, bukan mekanisme tokenomics).

=== YANG PERLU DICARI LEBIH DALAM (belum ada datanya) ===
- Jadwal vesting PERSIS untuk kategori Team (cliff berapa lama, durasi vesting) dan Investors — belum
  pernah tercatat spesifik di fase manapun sebelumnya
- Mekanisme governance ZRO — apakah ada voting on-chain, delegasi, atau murni advisory? (Phase 5 mencatat
  "referendum fee" dengan partisipasi 3,71%-13,01% — apakah ini SATU-SATUNYA mekanisme governance ZRO,
  atau ada mekanisme lain di luar fee-switch voting?)
- Status "Fee Switch" per hari ini — Phase 5 mencatat status ini DIPERDEBATKAN antar sumber sekunder
  (sebagian bilang aktif Desember 2025, sebagian bilang gagal kuorum ~40,6%) — CARI kepastian status
  terkini dan mekanisme persis buyback-and-burn yang akan dijalankan begitu aktif
- Holder concentration — berapa % suplai dipegang oleh top 10/50/100 wallet? Apakah data on-chain
  tersedia (Etherscan token holder distribution, dsb)?
- Apakah ada kategori alokasi genesis lain yang belum tercatat (advisor, ekosistem/grants, dst) di luar
  4 kategori (Strategic Partners/Team/Community/Tokens Repurchased) yang totalnya sudah 100%? Jika sudah
  100% tanpa sisa, konfirmasi ini eksplisit — jangan biarkan implisit.

=== FORMAT OUTPUT ===
Total Supply: <value> (Evidence Level) [sumber]
Supply Type: <fixed|inflationary> (Evidence Level) [sumber]
Distribution: <pecah jadi sub-bullet per kategori, MASING-MASING dengan sitasi sendiri>
  - Community: <%> (<jumlah ZRO>) (Evidence Level) [sumber]
  - Team: <%> (<jumlah ZRO>) (Evidence Level) [sumber]
  - Investors: <%> (<jumlah ZRO>) (Evidence Level) [sumber]
  - Tokens Repurchased: <%> (<jumlah ZRO>) (Evidence Level) [sumber]
  - <kategori lain jika ada>: <%> (Evidence Level) [sumber]
Allocation - Team: <cliff, durasi vesting> (Evidence Level) [sumber]
Allocation - Investors: <cliff, durasi vesting> (Evidence Level) [sumber]
Allocation - <kategori lain>: <cliff, durasi vesting> (Evidence Level) [sumber]
TGE Unlock: <% dari total suplai + kategori mana yang unlock> (Evidence Level) [sumber]
Emission Schedule: <value atau "n/a — fixed supply"> (Evidence Level) [sumber]
Utility: <pecah jadi sub-bullet, satu utilitas per baris, MASING-MASING dengan sitasi sendiri>
Governance Mechanism: <value — pecah jadi sub-bullet jika lebih dari 2 kalimat> (Evidence Level) [sumber]
Inflation/Deflation: <value — rekonsiliasi dengan temuan buyback Phase 5 di atas> (Evidence Level) [sumber]
Burn Mechanism: <value atau "none" — jelaskan status Fee Switch terkini> (Evidence Level) [sumber]
Holder Concentration: <value atau "belum dapat diukur"> (Evidence Level) [sumber]
Notable Token Flow: <value atau "n/a" — termasuk 2 buyback pasca-TGE dari Phase 5 jika relevan secara
  tokenomics> (Evidence Level) [sumber]
Status: <live|planned/pre-TGE>

Open Threads
- <hal yang masih belum pasti, bertentangan, atau perlu digali lebih lanjut>

=== ATURAN FORMAT (berlaku untuk seluruh jawaban) ===
- Tulis dalam BAHASA INDONESIA. Yang TIDAK diterjemahkan: nama produk/teknologi, nama orang, nama
  perusahaan, nama chain, dan URL.
- Ikuti template output di atas PERSIS — label field yang sama, urutan yang sama. Jangan reformat jadi
  prosa, jangan ganti nama field, jangan urutkan ulang.
- JANGAN gunakan tabel sama sekali.
- Satu fakta per baris. Tanggal lengkap, angka dengan satuan. Jangan membulatkan atau menghilangkan angka.
- Sebuah field TIDAK PERNAH berupa paragraf. Kalau isi yang mau ditulis lebih dari ~2 kalimat, WAJIB
  dipecah jadi sub-bullet di bawah label itu — satu klaim per sub-bullet, masing-masing diakhiri Evidence
  Level + sumbernya sendiri.
- JANGAN mengarang. Kalau tidak diketahui/tidak dapat diverifikasi, tulis "tidak diketahui" — jangan
  menebak atau mengisi kekosongan dengan klaim yang terdengar masuk akal tapi tidak bersumber.
- Kalau sebuah klaim diperdebatkan oleh sumber berbeda, catat eksplisit ("Sumber A bilang X, Sumber B
  bilang Y") — jangan diam-diam memilih salah satu.
- Sitasi WAJIB menempel di SETIAP fakta, di baris yang sama — bukan daftar pustaka di akhir. Daftar sumber
  di akhir tanpa kaitan per-fakta TIDAK bisa diterima.
- Evidence Level (HIGH/MEDIUM/LOW) di setiap klaim signifikan.
- Contoh gabungan: "Team: 25,50% (255.000.000 ZRO) (HIGH) [LayerZero Foundation blog, https://...]"
- JANGAN menganalisis atau berspekulasi soal kausalitas di luar cakupan fase ini — itu tugas fase Behavioral
  nanti.
- Awali output dengan: PROJECT: LayerZero
- Akhiri dengan heading "Open Threads" berisi daftar hal yang masih belum pasti/bertentangan/perlu digali
  lebih lanjut.
```

**Result:** rejected, not committed. Two disqualifying problems, one worse than anything seen in Phase 3.

(1) **Zero inline citations, again:** verified via grep — 0 matches for `[sumber` or a URL anywhere in the
document body (69 non-empty paragraphs). Every fact carries an Evidence Level tag `(HIGH)`/`(MEDIUM)`/
`(LOW)` but no source attached, despite the prompt giving an explicit worked example of the required
format. A 14-source bibliography exists at the end, unlinked to any individual fact — the identical
failure mode Phase 3 took 3 attempts to fix.

(2) **Prose quality regression, likely fabrication:** several fields degrade into single, page-length
run-on sentences stacking near-synonymous phrases with no added information (worst offender: the Fee
Switch effectiveness paragraph). More seriously, the draft claims TGE released **25% of supply
(250M ZRO)** — split into 8.5% retail-claimable + 5% to Foundation treasury + 11.5% reserved for a
rumored "Season 2 airdrop" — which contradicts the confirmed 8.5% TGE-claimable figure (established
across Phase 3 and Phase 5, and stated explicitly in this very prompt's "already known" block) with no
traceable source. Also claims the Fee Switch is "unconditionally active" since Feb 2026 following a 97%-
approval Referendum #3, without addressing Phase 5's noted quorum-failure reports for the same period.
Source quality is also markedly weaker than Phase 3/5 (token-unlock-tracker sites, one Binance Square
profile that reads as a bot account) vs. those phases' CoinDesk/The Block/Law360-tier sourcing.

Not patched or reformatted — the 25% claim specifically needs independent verification, not a citation
retrofit onto content that might be wrong. Following the Phase 3/5 precedent, a Claude-direct research
pass was commissioned instead (see below) rather than sending this back to Gemini.

## Phase 6 — Claude-direct tokenomics research (commissioned 2026-07-25)

Prompt sent to a separate Claude research session (not this pipeline's Gemini loop), asking it to
independently verify: the TGE-unlock contradiction (8.5% confirmed vs. the rejected draft's 25% claim),
the Fee Switch's actual activation status (active vs. quorum-failed), whether the two post-TGE ZRO
buybacks (Sept/Nov 2025) burn supply or move it to treasury, exact Team/Investor vesting terms, the full
scope of ZRO's governance mechanism, and whether any real holder-concentration data exists. Full prompt
text kept below for the record.

```
Research task: LayerZero (ZRO) tokenomics — sourced fact-check and citation map

Context: I'm building a structured tokenomics profile for LayerZero's ZRO token as part of a crypto
research pipeline. A previous research pass (from Gemini) produced several claims with NO verifiable
citations attached, and at least one figure that contradicts previously-confirmed facts. I need you to
independently verify the tokenomics facts below, find real checkable sources (prefer primary sources —
LayerZero Foundation's own blog/docs, or established crypto media like CoinDesk/The Block/Messari/
DefiLlama — over token-unlock-tracker aggregator sites, which should be used only for cross-checking,
not as primary evidence), and flag anything you cannot verify rather than guessing.

=== ALREADY CONFIRMED (from prior research passes, cross-verified across multiple sources) — treat as
ground truth, do not re-derive, but DO use to sanity-check anything that contradicts them ===
- Total Supply: 1,000,000,000 ZRO, fixed/hard-capped.
- Genesis allocation: Strategic Partners/Investors 32.20% (322,000,000 ZRO); Core Contributors/Team
  25.50% (255,000,000 ZRO); Community/Airdrop 38.30% (383,000,000 ZRO); Tokens Repurchased 4.00%
  (40,000,000 ZRO) — these four sum to exactly 100%.
- TGE was 20 June 2024. The claimable portion at TGE was 8.5% of total supply (85,000,000 ZRO), via
  the "Proof-of-Donation" mechanism (a $0.10/ZRO donation to Protocol Guild required to unlock a claim,
  paid in USDC/USDT/ETH, ~$18.5M projected total with LayerZero Foundation matching up to $10M).
- ZRO price fell ~15% in the first 24 hours post-TGE-announcement, to ~$2.87 (confirmed via
  Cryptopolitan/CoinMarketCap in an earlier research pass — NOT the "$4.79→$3.39" figure that circulated
  in very early drafts and was never verified).
- The 40,000,000 ZRO "Tokens Repurchased" genesis bucket is confirmed to be the same 40M ZRO that
  LayerZero returned to strategic partners as part of the FTX bankruptcy-estate litigation settlement
  (31 January 2025) — this was independently confirmed via a separate financial-research pass (Phase 5)
  and needs no further verification, just don't contradict it.
- Two post-TGE ZRO buyback events are confirmed real (from the Phase 5 financial research): a
  ~50,000,000 ZRO (~5% of supply) buyback from early investors/strategic partners in September 2025
  (part of a combined ~$150M-for-the-year figure that also includes a16z's separate $55M April 2025
  secondary purchase), and a $10M discretionary LayerZero Labs open-market buyback in November 2025.
  What is NOT yet confirmed: whether these bought-back tokens were actually BURNED (removed from total
  supply) or moved to Foundation/Labs treasury (not burned, just changed hands) — this is the single most
  important open question for this research pass.

=== NEEDS INDEPENDENT VERIFICATION — THIS IS THE CORE OF THE TASK ===

1. **TGE unlock percentage — resolve a direct contradiction.** A prior (Gemini) draft claimed the TGE
   released 25% of total supply (250,000,000 ZRO), broken down as: 8.5% (85M) claimable by retail users,
   5% (50M) to LayerZero Foundation treasury as "venture capital and DEX liquidity provisioning," and
   11.5% (115M) reserved in protocol treasury for a rumored "Season 2 airdrop" in H2 2026. This 25%
   figure and its breakdown could NOT be traced to any source in that draft and directly contradicts the
   confirmed 8.5% figure above. Find out: is there ANY credible source for a 25% TGE circulating-supply
   figure (as distinct from the 8.5% claimable-by-retail figure)? Or is 25% a fabrication/hallucination
   that should be discarded entirely? If you find NO support for it, say so explicitly — don't try to
   rationalize a middle-ground number.

2. **Fee Switch activation status — resolve as of today.** A prior draft claimed the Fee Switch was
   "unconditionally active" as of February 2026, following a Referendum #3 in December 2025 with 97%
   approval. Separately, other secondary sources (per an earlier financial research pass) reported the
   fee-switch vote failing to reach an ~40.6% quorum around the same period. These cannot both be true.
   Determine: is the Fee Switch actually live and burning fees today? What is the actual approval
   threshold/quorum requirement, and did the relevant referendum(s) actually meet it? Cite whatever
   official governance/on-chain source settles this (LayerZero Foundation governance portal, Snapshot
   space, or official blog announcement) rather than a secondary blog's summary.

3. **Do post-TGE ZRO buybacks burn supply or move it to treasury?** Specifically for the September 2025
   ~50M ZRO buyback and the November 2025 $10M Labs buyback: is there on-chain evidence (transfer to a
   verifiable burn address, e.g. 0x000...dead or similar) that the tokens were destroyed, or does the
   evidence point to them sitting in a Foundation/Labs-controlled treasury wallet? Two research camps are
   reportedly split on this (one calling it "burned," another calling it "buyback-and-accumulate,
   not burned") — find the on-chain transaction data yourself if possible (which address received the
   tokens?) rather than just repeating secondary commentary.

4. **Vesting schedule specifics for Team and Investors** — exact cliff length and vesting duration/
   cadence (e.g. "12-month cliff, then 24-month linear monthly vesting" or whatever the actual terms are)
   for the Core Contributors (25.50%) and Strategic Partners/Investors (32.20%) genesis buckets. A prior
   draft claimed 12-month cliff + 24-month linear vesting for both — verify this specifically, since it
   wasn't independently sourced in that draft either.

5. **Governance mechanism scope** — is the fee-switch referendum the ONLY on-chain governance ZRO holders
   get, or are there other decisions token holders vote on? What's the actual mechanism (Snapshot
   off-chain vote, on-chain binding vote, delegated voting, etc.)?

6. **Holder concentration** — is there ANY on-chain data (Etherscan token holder distribution, or a
   dashboard like Nansen/Arkham) showing top 10/50/100 wallet concentration for ZRO? A prior draft
   claimed this was completely unmeasurable — confirm or find what's actually available.

=== OUTPUT FORMAT ===
Please structure your findings the same way as before: a short TL;DR of the most important
corrections/confirmations, then Key Findings organized by the numbered questions above (with real,
checkable URLs attached to every specific claim — not a bibliography dump at the end disconnected from
individual facts), then Recommendations for what to state as fact vs. flag as unverified/contested, then
Caveats for anything you couldn't fully resolve. Prioritize primary sources (LayerZero's own
blog/docs/governance portal) and reputable crypto media (CoinDesk, The Block, Messari, DefiLlama) over
token-unlock-aggregator sites or low-effort blogs — if an aggregator site is the only source you can find
for something, say so explicitly rather than presenting it with unearned confidence.
```

**Result:** succeeded — decisively resolved both disqualifying problems from the rejected draft, with
primary sources (LayerZero Foundation's own "Introducing ZRO" and "The ZRO Token" blog posts, its
governance/fee-switch page, its buyback tracker) for the load-bearing claims.

(1) **TGE 25% claim confirmed fabricated.** The real breakdown: 8.5% (85M ZRO) retail-claimable via the
retroactive airdrop, plus 5% of total supply unlocked at launch from the "Ecosystem and Growth" sub-
bucket (grants/programs/liquidity) — roughly **13.5% unlocked at TGE, not 25%**. The rejected draft's
specific 8.5%/5%/11.5% split and its "Season 2 airdrop" framing for the 11.5% piece traces to no source.

(2) **Fee Switch confirmed NEVER activated**, contradicting the rejected draft's "unconditionally active
since Feb 2026" claim outright. All 4 semi-annual referendums (Dec 2024 / Jun 2025 / Dec 2025 / Jun 2026)
show "Outcome: Off" on the Foundation's own governance page — Referendum #3 (Dec 2025) got ~97% "Yes"
among votes cast but only 3.71% turnout, failing its 40.59% dynamic quorum. The rejected draft appears to
have conflated "97% approved" with "activated," missing the quorum failure entirely. Several mid-tier
outlets (0xprocessing, a CoinMarketCap AI page, KuCoin explainers) repeat the same false "activated"
claim — flagged in Open Threads as a trap for future phases that might cite them.

(3) **Post-TGE buybacks confirmed HELD in treasury, not burned** — DefiLlama's methodology and the
Foundation's own language ("removes supply from the investor unlock schedule," "re-locked until Zero
mainnet") both point to reallocation, not destruction. Total supply remains 1B; only circulating float
is affected. This closes the "burn vs. treasury" question Phase 5 explicitly left open. The $112.7M /
19.77%-of-supply buyback aggregate matches Phase 5's figures exactly — cross-phase consistency confirmed.

(4) **Vesting terms confirmed**: Strategic Partners and Core Contributors both on a 3-year schedule
(1-year cliff, then 24 months monthly linear) — matching what the *rejected* draft had claimed for this
one specific item, even though it carried no citation there. The "Tokens Repurchased" (4%) bucket has no
officially disclosed vesting schedule; aggregator models (tokenradar.ai, DropsTab) are estimates only.

(5) **Governance scope confirmed narrow**: only the fee-switch referendum exists at the protocol level,
binding (controls an immutable on-chain contract, not advisory), single-chain token-weighted voting with
no delegation confirmed. (6) **Holder concentration**: resolved from "cannot be measured" to a properly
caveated partial picture — ZRO is an OFT with supply concentrated on Arbitrum (not Ethereum, where
Etherscan/CoinCarp concentration figures are near-zero and therefore misleading); Arbiscan's Top-N table
couldn't be extracted, but named signals exist (Nansen: one entity accumulated 2.6% of supply via 9
Coinbase-Prime-funded wallets in March 2026; Foundation's own data: one entity responsible for 37.9% of
all unlocked-ZRO sales to date).

Also surfaced a new open question not previously flagged anywhere: **circulating supply has no agreed
figure** — trackers range from 252M (DefiLlama) to 514M (Foundation's own "unlocked" figure) depending
entirely on whether re-locked Foundation holdings count as circulating.

Synthesized directly into the template format (no further Gemini round needed — same rationale as Phase
3/5): every field cited per-fact, the two corrected claims marked `[KOREKSI]` with the reasoning kept
inline rather than silently overwritten, Open Threads covering the unresolved circulating-supply range,
the unconfirmed delegation claim, and the false-activation trap for future phases to avoid. Verified
structurally before committing (all required template fields present) and OOXML schema validation
passed.

**Active file:** `doc_backup/inbox/phased/LayerZero/06-token.docx`. Source research archived at
`06-token-citation-map-research.md`.

## Phase 7 — Ecosystem Intelligence (drafted 2026-07-26)

Context Pack: Phase 1 (full) + a Phase 2 index (76 entity names + types only, no relationship prose —
just enough for the model to know who's already mapped and go deeper instead of re-deriving). Explicitly
caps the "Integration Partner" block to significant partners only (LayerZero connects to 165+ chains and
hundreds/thousands of dApps — the Phase 2 prompt deliberately deferred that long tail to this phase, but
enumerating all of it produces an unusable wall of low-value entries). Injects the Tether/USDT0 mechanics
gap carried forward since the Phase 1 v2→v3 trim, and explicitly asks the model to mark the "Zero"
blockchain's institutional partnerships (DTCC/Citadel/ICE/ARK/Google Cloud, announced Feb 2026) as
"announced-only" unless it finds concrete evidence of live deployment. Repeats the Phase 6 prose-collapse
warning verbatim in the format rules, since that failure mode could recur here given the sprawling scope.

```
Menggunakan output Foundation Intelligence (Phase 1) di atas sebagai konteks, bangun PROFIL EKOSISTEM/
HUBUNGAN EKSTERNAL untuk LayerZero. Bedakan tegas "integrasi diumumkan" vs "integrasi live dan benar-benar
dipakai" — ini penekanan paling penting di fase ini, karena beberapa kemitraan LayerZero (terutama yang
terkait blockchain "Zero", diumumkan Februari 2026) masih berstatus rencana/eksplorasi, bukan sudah
berjalan.

=== INDEKS ENTITAS DARI PHASE 2 (nama + tipe saja — JANGAN ulangi relationship/context penuh, cukup
gunakan untuk mencocokkan nama persis dan tahu siapa yang SUDAH terpetakan, supaya kamu bisa MEMPERDALAM,
bukan mengulang) ===
LayerZero Labs Ltd. (Organization); Optimistic Labs Limited (Organization); LayerZero Labs Canada Inc.
(Organization); LayerZero Foundation (Foundation); Bryan Pellegrino (Person); Ryan Zarick (Person);
Caleb Banister (Person); Chainlink (Partner); Chainlink CCIP (Protocol); Google Cloud (Partner);
Polyhedra (Partner); Alameda Ventures / FTX Group (Investor); Protocol Guild (Foundation); Stargate
Finance (Protocol); Tether (Partner); Trail of Bits (Research); Zellic (Research); Zokyo (Research);
Peckshield (Research); Hacken (Research); Kelp DAO (Protocol); a16z crypto (Investor); Sequoia Capital
(Investor); Binance Labs (Investor); Multicoin Capital (Investor); PayPal Ventures (Investor); Circle
Ventures (Investor); OKX Ventures (Investor); Delphi Digital (Investor); BOND (Investor); Christie's
(Investor); Samsung Next (Investor); OpenSea (Investor); Polygon Ventures (Investor); DeFiance Capital
(Investor); Spartan Group (Investor); Sino Global Capital (Investor); Coinbase Ventures (Investor);
EigenLabs / EigenLayer (Partner); Nethermind (Partner); Animoca Brands (Partner); Horizen Labs (Partner);
Delegate (Partner); Radiant Capital (Protocol); Ondo Finance (Protocol); Paxos (Protocol); Ethena
(Protocol); EtherFi (Protocol); Keeta (Partner); IDEX (Protocol); Binance (Exchange); Coinbase (Exchange);
Kraken (Exchange); OKX (Exchange); Bybit (Exchange); KuCoin (Exchange); MEXC (Exchange); Bitget (Exchange);
HTX/Huobi (Exchange); Uphold (Exchange); Uniswap (Exchange); SushiSwap (Exchange); PancakeSwap (Exchange);
TraderJoe (Exchange); Hashflow (Protocol); Immunefi (Partner); United States Bankruptcy Court for the
District of Delaware (Government); FTX Recovery Trust (Organization); University of New Hampshire (IOL)
(Research); CrowdStrike (Partner); Mandiant (Partner); zeroShadow (Partner); Halborn (Research); Certik
(Research); Quantstamp (Research); Chain EVM dan Non-EVM Terintegrasi — 165+ (Product, BELUM dirinci
satu-per-satu — ini tugas fase ini)

=== TENTANG SKALA — PENTING, supaya hasil tidak jadi daftar tak berguna ===
LayerZero terhubung ke 165+ chain dan ratusan/ribuan dApp. JANGAN coba mendaftarkan semuanya satu per
satu. Untuk blok "Integration Partner", batasi HANYA pada partner yang SIGNIFIKAN — chain besar dengan
TVL/volume tinggi, dApp yang sudah muncul di fase-fase sebelumnya (lihat indeks Phase 2 di atas: Stargate,
Radiant Capital, Ondo Finance, Ethena, EtherFi, Kelp DAO, IDEX, Hashflow, Paxos, Keeta), atau kemitraan
institusional besar (Tether/USDT0, DTCC, Citadel Securities, ICE, ARK Invest, Google Cloud). Untuk
chain/dApp yang jumlahnya masif dan tidak signifikan secara individual, cukup rangkum di field "Developer
Ecosystem" atau "Applications Built On It" secara agregat (contoh: "165+ chain terintegrasi per dokumentasi
resmi, termasuk X/Y/Z tier-1 yang signifikan secara individual — lihat blok Integration Partner").

=== YANG SUDAH DIKETAHUI — WAJIB DIPERDALAM DENGAN DETAIL, JANGAN CUMA DIULANG ===
- Tether meluncurkan USDT0 menggunakan standar OFT (Omnichain Fungible Token) milik LayerZero — belum
  pernah direkam mekanisme integrasi TEKNISNYA di fase manapun sebelumnya. USDT0 sendiri sudah memfasilitasi
  >$70 miliar volume transfer lintas-rantai dalam 12 bulan (per riset Phase 3). CARI: bagaimana persis
  USDT0 dibangun di atas OFT — apakah lock-and-mint atau native burn-and-mint? Chain mana saja yang sudah
  live?
- DVN (Decentralized Verifier Network) providers yang sudah dipetakan di Phase 2 sebagai Partner: Chainlink
  CCIP, Google Cloud, Polyhedra, EigenLabs/EigenLayer, Nethermind, Animoca Brands, Horizen Labs, Delegate —
  ini masuk kategori "Oracle Integrations" DAN "Infra/Tooling Providers" di format output; JANGAN ulangi
  penjelasan teknis DVN dari Phase 4, fokus di sini pada STATUS masing-masing (live/announced) dan skala
  adopsi (berapa banyak OApp yang benar-benar memakai tiap DVN ini per hari ini).
- Kemitraan institusional "Zero" blockchain (diumumkan 10 Februari 2026): DTCC, Citadel Securities,
  Intercontinental Exchange (ICE), ARK Invest, Google Cloud — per riset Phase 3/5/6, ini SEBAGIAN BESAR
  masih level "eksplorasi"/investasi strategis, BUKAN deployment yang sudah selesai; mainnet Zero
  ditargetkan musim gugur 2026. TANDAI status "announced-only" untuk kemitraan ini kecuali kamu menemukan
  bukti konkret sudah live.
- Exchange listing ZRO sudah dipetakan di Phase 2 (11 exchange: Binance/Coinbase/Kraken/OKX/Bybit/KuCoin/
  MEXC/Bitget/HTX/Uphold + 4 DEX: Uniswap/SushiSwap/PancakeSwap/TraderJoe) — field "Exchange Listings" di
  sini JANGAN mengulang daftar itu, tapi tambahkan yang BELUM ada: tier/breadth (spot vs derivatives vs
  margin), kedalaman likuiditas/volume harian jika tersedia, dan listing BARU yang belum tercatat di Phase 2.

=== YANG PERLU DICARI LEBIH DALAM (belum ada datanya di fase manapun) ===
- Dukungan wallet (Wallet Support) — belum pernah dicatat sama sekali di fase manapun sebelumnya. Wallet
  mana yang mendukung interaksi lintas-rantai LayerZero secara native (MetaMask, Rabby, Trust Wallet, dst)?
- Ukuran dan aktivitas komunitas (Discord/Telegram/forum) dengan angka dan tanggal konkret — belum pernah
  dicatat.
- Developer ecosystem: berapa banyak smart contract yang sudah dideploy memakai LayerZero (Phase 6
  menyebutkan "50.000+ smart contract" dalam konteks auto-burn fee switch — verifikasi ulang angka ini
  untuk konteks developer ecosystem, atau cari angka yang lebih relevan/terkini)?
- Bridge Integrations — di luar DVN, apakah ada jembatan pihak ketiga lain (bukan DVN) yang terintegrasi
  atau berkompetisi langsung di rute yang sama?

=== FORMAT OUTPUT ===
Untuk SETIAP integration partner (batasi ke yang signifikan, lihat instruksi skala di atas), ulangi blok
ini (setiap baris pakai sitasinya sendiri):
Integration Partner: <nama>
  What it does: <value> (Evidence Level) [sumber]
  Status: <live|announced-only> (Evidence Level) [sumber]
---

Lalu, sekali saja (SETIAP baris WAJIB punya sitasinya sendiri — kalau jawabannya butuh lebih dari 2
kalimat, pecah jadi sub-bullet, masing-masing dengan sitasi sendiri):
Developer Ecosystem: <value> (Evidence Level) [sumber]
Applications Built On It: <daftar, pecah jadi sub-bullet per aplikasi signifikan> (Evidence Level) [sumber]
Wallet Support: <daftar> (Evidence Level) [sumber]
Exchange Listings: <ringkasan tier/breadth di luar yang sudah ada di Phase 2 — JANGAN ulang daftar exchange
  Phase 2> (Evidence Level) [sumber]
Oracle Integrations: <daftar DVN dari indeks Phase 2 + status live/announced masing-masing> (Evidence
  Level) [sumber]
Bridge Integrations: <value atau "n/a"> (Evidence Level) [sumber]
Infra/Tooling Providers: <value> (Evidence Level) [sumber]
Community Size/Activity: <angka Discord/TG/forum + tanggal> (Evidence Level) [sumber]

Open Threads
- <hal yang masih belum pasti, bertentangan, atau perlu digali lebih lanjut>

=== ATURAN FORMAT (berlaku untuk seluruh jawaban) ===
- Tulis dalam BAHASA INDONESIA. Yang TIDAK diterjemahkan: nama produk/teknologi, nama orang, nama
  perusahaan, nama chain, dan URL.
- Ikuti template output di atas PERSIS — label field yang sama, urutan yang sama. Jangan reformat jadi
  prosa, jangan ganti nama field, jangan urutkan ulang.
- JANGAN gunakan tabel sama sekali.
- Satu fakta per baris. Tanggal lengkap, angka dengan satuan. Jangan membulatkan atau menghilangkan angka.
- Sebuah field TIDAK PERNAH berupa paragraf — apalagi satu kalimat raksasa berisi bertumpuk-tumpuk sinonim
  tanpa informasi baru (ini kegagalan nyata yang terjadi di percobaan Phase 6 sebelumnya — JANGAN ulangi).
  Kalau isi yang mau ditulis lebih dari ~2 kalimat, WAJIB dipecah jadi sub-bullet di bawah label itu — satu
  klaim per sub-bullet, masing-masing diakhiri Evidence Level + sumbernya sendiri.
- JANGAN mengarang. Kalau tidak diketahui/tidak dapat diverifikasi, tulis "tidak diketahui" — jangan
  menebak atau mengisi kekosongan dengan klaim yang terdengar masuk akal tapi tidak bersumber.
- Kalau sebuah klaim diperdebatkan oleh sumber berbeda, catat eksplisit ("Sumber A bilang X, Sumber B
  bilang Y") — jangan diam-diam memilih salah satu.
- Sitasi WAJIB menempel di SETIAP fakta, di baris yang sama — bukan daftar pustaka di akhir tanpa kaitan
  per-fakta.
- Evidence Level (HIGH/MEDIUM/LOW) di setiap klaim signifikan.
- JANGAN menganalisis atau berspekulasi soal kausalitas di luar cakupan fase ini — itu tugas fase
  Behavioral nanti.
- Awali output dengan: PROJECT: LayerZero
- Akhiri dengan heading "Open Threads" berisi daftar hal yang masih belum pasti/bertentangan/perlu digali
  lebih lanjut.
```

**Result:** succeeded — run through DeepSeek instead of Gemini (the maintainer hit a Claude usage limit and
found Gemini's own Phase 7 attempt incomplete, so tried a third model on the same prompt). First
non-Gemini, non-manual-research pass in this project, and the strongest first-attempt result of any
LayerZero phase to date: format followed correctly, citations attached per-fact throughout (63 bracketed
source+date citations across 87 non-empty lines), and the live-vs-announced-only distinction applied
correctly without prompting twice — Keeta and Tether/USDT0 marked live with mechanism detail (USDT0 uses
both lock-and-mint on Ethereum and burn-and-mint on other chains, resolving the Tether integration-
mechanics gap carried since the Phase 1 trim), while Citadel Securities/DTCC/ICE/ARK Invest/Google Cloud
(all part of the Feb 2026 "Zero" announcement) are correctly marked announced-only with the exact
"evaluating/looking into/exploring" language from source quoted as the basis.

Cross-checks cleanly against every prior phase: the 8 DVN providers match Phase 2's entity list exactly,
the Zero-blockchain partnership set matches Phase 3/5/6's "still exploration-stage" framing, and the
11 CEX + 4 DEX exchange list is correctly *not* re-derived, just cited as already covered. Two DVN
providers (EigenLabs/EigenLayer, Delegate) honestly marked "status tidak diketahui / LOW" rather than
guessed. Open Threads properly surfaces every cross-source numeric conflict it found rather than
silently picking one: chain count (165+ vs 170+ vs 80+ across different sources/dates), dApp count
(80+ vs 300+ vs 750+), and three different Telegram member counts from what may be different channels.

One quality gap versus the Phase 3/5/6 Claude-direct research: citations are domain+date only
(e.g. "[www.theblock.co, 23 Juli 2026]"), not full URLs — traceable but less immediately checkable.
Not a blocker; noted for awareness, not corrected, since fabricating URLs would be worse than citing
without one.

Committed with only a mechanical format conversion (plain text to `.docx`, matching house style) — no
content changes, since nothing here needed correcting the way Phase 6's Gemini draft did.

**Active file:** `doc_backup/inbox/phased/LayerZero/07-ecosystem.docx`. Raw DeepSeek output archived at
`07-ecosystem-deepseek-raw.txt`.

## Phase 8 — Market Intelligence (drafted 2026-07-26)

Context Pack: Phase 1 (full) + a Phase 3 index (event labels + dates only, no full Trigger/Context/
Decision/Execution/Outcome bodies — just enough for "Market Cycles Operated Through" to anchor real dates
rather than vague eras). No `examples/Sentiment/LayerZero.md` companion exists for this project, so the
prompt explicitly says to ignore that cross-check instruction rather than leave it dangling. Competitor,
adoption-metric, and TVL facts from Phases 3/4/5/6/7 are injected directly as compact figures rather than
requiring those documents to be uploaded in full.

The single most important injected fact: the >$4B (May 2026) growing to >$7.2B (Jul 2026) institutional
exodus to Chainlink CCIP, discovered in Phase 3's research, is explicitly flagged as the likely most
consequential fact for this phase's "Current Status" and "Market Share" fields — with an explicit
instruction not to present only the growth side (Zero blockchain, Tether/Citadel/ARK investments) without
the erosion side (the exodus), since both are happening simultaneously.

```
Menggunakan output Foundation Intelligence (Phase 1) di atas sebagai konteks, bangun PROFIL PASAR untuk
LayerZero. HANYA pasar — BUKAN kenapa (itu tugas fase Behavioral Intelligence berikutnya). Tidak ada
companion Sentiment (Grok/X) yang tersedia untuk proyek ini — abaikan instruksi cross-check itu.

=== INDEKS EVENT DARI PHASE 3 (nama + tanggal saja — JANGAN ulangi Trigger/Context Snapshot/Decision/
Execution/Outcome penuh, cukup gunakan untuk menandai era/siklus pasar yang relevan di field "Market
Cycles Operated Through") ===
1 April 2021 — Putaran Pendanaan Seed $2 Juta; Mei 2021 — Publikasi Whitepaper; 16 September 2021 —
Series A $6 Juta & Mainnet V1; Kuartal Pertama 2022 — Peluncuran Stargate Finance; 30 Maret 2022 — Series
A Extension $135 Juta; 11 November 2022 — Keruntuhan FTX; 4 April 2023 — Series B $120 Juta; 2023 —
Ekspansi 50+ Chain; September 2023–31 Januari 2025 — Gugatan Clawback FTX (settled); 29 Januari 2024 —
Peluncuran LayerZero V2; 20 Juni 2024 — TGE ZRO & "Proof-of-Donation"; 10-25 Agustus 2025 — Akuisisi
Stargate Finance; 10 Februari 2026 — Peluncuran Blockchain "Zero"; 18 April 2026 — Insiden Eksploitasi
Kelp DAO ($292 Juta); Mei 2026 — Modifikasi Keamanan Sistemik DVN & Eksodus ke Chainlink CCIP

=== YANG SUDAH DIKETAHUI — WAJIB DIPERDALAM DENGAN DETAIL, JANGAN CUMA DIULANG ===
- Kompetitor yang sudah teridentifikasi di fase-fase sebelumnya: Wormhole (rival jembatan/messaging sejak
  V1, sempat mengajukan tawaran tandingan $120 juta saat akuisisi Stargate Agustus 2025), Cosmos IBC
  (rival arsitektur sejak era whitepaper 2021), Chainlink CCIP (AWALNYA mitra/opsi DVN di V2, BERUBAH jadi
  kompetitor langsung setelah eksodus migrasi klien pasca-insiden Kelp DAO Mei 2026), Axelar dan Hyperlane
  (disebut sebagai protokol messaging lintas-rantai sejenis di riset Phase 4).
- Metrik adopsi (PERHATIAN — angka lama "80 juta+ pesan" dari draf sangat awal SUDAH USANG, dikonfirmasi
  di Phase 3; gunakan angka lebih baru di bawah sebagai basis, tapi CARI angka TERKINI per tanggal riset
  kamu karena ini bisa saja sudah berubah lagi):
  - Pertumbuhan volume pesan: 66.000+ (Juni 2022) → 1,7 juta+ (Juni 2024), kenaikan 4x (Messari, Agustus
    2024, per riset Phase 7)
  - Total pesan diproses: 159-160 juta (per riset Phase 5/6, pertengahan 2026)
  - Total nilai ditransfer kumulatif: $225-260 miliar lintas 165+ chain (per riset Phase 5/6)
  - Total smart contract yang mendeploy LayerZero: 50.000+ hingga 54.000+ tergantung sumber/tanggal
    (Phase 6 & 7) — flag rentang ini, jangan pilih satu angka tanpa menyebut sumber+tanggal
- TVL Stargate Finance: sempat mencapai puncak >$3 miliar (menurut catatan Phase 1 trim) — VERIFIKASI
  ulang angka ini dan cari histori TVL Stargate dari puncak hingga sekarang, termasuk efek akuisisi
  Agustus 2025 dan insiden Kelp DAO April 2026 terhadap TVL.
- PERISTIWA PALING PENTING untuk "Current Status" dan "Market Share" — jangan dilewatkan: pasca insiden
  Kelp DAO (18 April 2026) dan pengakuan kesalahan DVN oleh LayerZero (Mei 2026), terjadi eksodus migrasi
  modal institusional senilai >$4 miliar (per Mei 2026) yang terus tumbuh menjadi >$7,2 miliar per Juli
  2026 ke kompetitor Chainlink CCIP (Lombard, Solv Protocol, Re.xyz, Kraken, Mantle $2,5 miliar, Virtuals
  $700 juta, Yuzu Money $54,5 juta — semua pindah). Ini KEMUNGKINAN BESAR peristiwa paling signifikan bagi
  posisi pasar LayerZero saat ini — pastikan field "Current Status" dan "Market Share" merefleksikan
  ketegangan antara PERTUMBUHAN institusional (Zero blockchain, investasi Tether/Citadel/ARK Februari
  2026) DAN EROSI pangsa pasar akibat eksodus ini secara bersamaan — JANGAN sajikan hanya salah satu sisi.

=== YANG PERLU DICARI LEBIH DALAM (belum ada datanya di fase manapun) ===
- Market share LayerZero vs Wormhole vs Axelar vs Chainlink CCIP dalam volume pesan/TVL lintas-rantai —
  apakah ada data pembanding kuantitatif (DefiLlama bridge rankings, dsb)?
- Narasi pasar yang LayerZero ikuti vs yang mereka ciptakan sendiri — draf sebelumnya (Phase 3/4) mencatat
  LayerZero mengklaim menyelesaikan "Bridging Trilemma" (narasi yang mereka CIPTAKAN sendiri) dan
  belakangan mengklaim jadi "Decentralized Multi-Core World Computer" (narasi Zero blockchain) — apakah
  ada narasi PASAR LEBIH BESAR yang mereka IKUTI (misal narasi "RWA tokenization", "chain abstraction",
  "institutional DeFi")? Bedakan tegas mana yang originated vs followed.
- Riwayat TVL/volume Stargate Finance dengan tanggal-tanggal kunci (peluncuran Maret 2022, puncak, efek
  akuisisi Agustus 2025, efek insiden Kelp DAO April 2026, kondisi saat ini)
- Siklus pasar yang benar-benar dilalui LayerZero dan efek TERUKUR pada proyek ini secara spesifik (bukan
  makro umum) — misal: bagaimana crypto winter 2022 memengaruhi TVL/volume LayerZero secara spesifik,
  bukan cuma kondisi pasar umum yang sudah dicatat di Phase 3?

=== FORMAT OUTPUT ===
Narrative(s): <value — tandai jelas mana yang originated (LayerZero menciptakan) vs followed (LayerZero
  mengikuti narasi pasar yang lebih besar), pecah jadi sub-bullet per narasi> (Evidence Level) [sumber]

Untuk SETIAP kompetitor/era, ulangi blok ini:
Competitor: <nama>
  Era: <kapan mereka bersaing> (Evidence Level) [sumber]
  Positioning vs. them: <value> (Evidence Level) [sumber]
---

Lalu, sekali saja (SETIAP baris WAJIB punya sitasinya sendiri):
Adoption Metrics: <metric: value (tanggal); ulangi per metrik, pecah jadi sub-bullet> (Evidence Level)
  [sumber]
TVL History: <value: tanggal; ulangi titik infleksi kunci, atau "n/a"> (Evidence Level) [sumber]
Volume History: <value: tanggal; ulangi titik infleksi kunci> (Evidence Level) [sumber]
Market Share: <value atau "tidak dapat dihitung" — WAJIB bahas efek eksodus Chainlink CCIP di sini>
  (Evidence Level) [sumber]
Market Cycles Operated Through: <daftar, dengan tanggal dan efek TERUKUR yang teramati pada proyek ini
  secara spesifik — pecah jadi sub-bullet per siklus> (Evidence Level) [sumber]
Current Status: <growing|declining|stagnant|dormant|recovering — atau kombinasi/nuansa jika kondisinya
  memang campuran (lihat catatan eksodus Chainlink CCIP di atas)> — basis: <observasi apa yang mendukung
  ini> (Evidence Level) [sumber]

Open Threads
- <hal yang masih belum pasti, bertentangan, atau perlu digali lebih lanjut>

=== ATURAN FORMAT (berlaku untuk seluruh jawaban) ===
- Tulis dalam BAHASA INDONESIA. Yang TIDAK diterjemahkan: nama produk/teknologi, nama orang, nama
  perusahaan, nama chain, dan URL.
- Ikuti template output di atas PERSIS — label field yang sama, urutan yang sama. Jangan reformat jadi
  prosa, jangan ganti nama field, jangan urutkan ulang.
- JANGAN gunakan tabel sama sekali.
- Satu fakta per baris. Tanggal lengkap, angka dengan satuan. Jangan membulatkan atau menghilangkan angka.
- Sebuah field TIDAK PERNAH berupa paragraf — apalagi satu kalimat raksasa berisi bertumpuk-tumpuk sinonim
  tanpa informasi baru. Kalau isi yang mau ditulis lebih dari ~2 kalimat, WAJIB dipecah jadi sub-bullet di
  bawah label itu — satu klaim per sub-bullet, masing-masing diakhiri Evidence Level + sumbernya sendiri.
- JANGAN mengarang. Kalau tidak diketahui/tidak dapat diverifikasi, tulis "tidak diketahui" — jangan
  menebak atau mengisi kekosongan dengan klaim yang terdengar masuk akal tapi tidak bersumber.
- Kalau sebuah klaim diperdebatkan oleh sumber berbeda, catat eksplisit ("Sumber A bilang X, Sumber B
  bilang Y") — jangan diam-diam memilih salah satu.
- Sitasi WAJIB menempel di SETIAP fakta, di baris yang sama — bukan daftar pustaka di akhir tanpa kaitan
  per-fakta. Sebutkan setidaknya nama domain sumber + tanggal per klaim (URL lengkap kalau tersedia).
- Evidence Level (HIGH/MEDIUM/LOW) di setiap klaim signifikan.
- JANGAN menganalisis atau berspekulasi soal kausalitas (kenapa sesuatu terjadi) di luar cakupan fase ini
  — itu tugas fase Behavioral berikutnya. Fase ini murni APA yang terjadi di pasar, bukan MENGAPA.
- Awali output dengan: PROJECT: LayerZero
- Akhiri dengan heading "Open Threads" berisi daftar hal yang masih belum pasti/bertentangan/perlu digali
  lebih lanjut.
```

**Result:** pending — awaiting output.
