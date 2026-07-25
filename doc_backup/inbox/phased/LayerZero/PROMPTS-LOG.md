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
