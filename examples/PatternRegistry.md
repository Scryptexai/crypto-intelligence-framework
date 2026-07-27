# Pattern Registry (machine-readable)

> **⚠ 2026-07-26 dataset reset:** P1–P6 below were grounded in projects now moved to
> `_archive_pre_v3/` (P1/P2/P4 from `CrossAnalysis-ETH-Lido-EigenLayer.md`; P3 from
> `Batch-01-EvolutionAnalysis.md`; P5/P6 from `Ethereum.md` — none are LayerZero-sourced). Kept in place
> rather than archived, since the abstract reasoning (`Shape`/`Applies When`/`prediction`) is still valid
> framework knowledge independent of where its grounding examples currently live — but treat the `source`/
> `analogs` fields as pointing into `_archive_pre_v3/` until each pattern is re-grounded in a project that
> went through the Format v3 phased pipeline. See `examples/DatasetIndex.md`'s reset note for the full
> rationale.
>
> **2026-07-27 addition — P7–P16:** LayerZero's own Phase 10 (Knowledge Extraction) produced 10 "Pattern
> Candidates" (`examples/CaseStudies/LayerZero.md`, section `PATTERN CANDIDATES`) that were never promoted
> here. Added below as P7–P16, each honestly at `instances: 1` / LOW confidence (same convention already
> used for P5) — **single-instance, LayerZero-sourced only, not yet cross-project confirmed.** They are
> real, HIGH-evidence findings *within* LayerZero's dossier, not conjecture — but per this framework's own
> rule (a pattern requires recurrence across *unrelated* projects, `CLAUDE.md`), a 1-instance candidate stays
> LOW until a second project through the Format v3 pipeline confirms the same shape. Do not read "LOW" here
> as "weak evidence" — read it as "awaiting confirmation," and check each `validated` field for the actual
> citation.

Consolidated catalogue of the transferable patterns extracted from the deep dossiers and cross-project
analyses. This is the single place the reasoning layer (and `tools/build_json.py`) reads patterns from —
prose analyses remain the human explanation; this file is their structured index.

**Format (parsed by `tools/build_json.py`):** each pattern is a `## <ID> · <Name>` heading followed by
`- key: value` bullets. Keys: `triggers` (comma list), `instances` (int), `analogs` (comma list),
`source` (repo path), `validated` (optional), `prediction`, `watch` (semicolon list), `scope` (the
Context/era range this pattern was actually observed under — ref `docs/Ontology/Context.md`). Confidence is
derived from `instances` (≥3 HIGH · 2 MEDIUM · 1 LOW).

**Why `scope` exists:** a pattern is only a strong analog for a new project if the new project's Context
(hunter population, Sybil-detection maturity, tech maturity, macro conditions) resembles the Context the
pattern was actually observed under. A pattern with no stated scope should be treated as **weakly transferable**
until its era-boundaries are established — do not apply 2020–2021-era mechanics blindly to 2026-era projects.

---

## P1 · Efficiency → Concentration → Mitigation
- triggers: liquid-staking, restaking, efficiency
- instances: 3
- analogs: Lido, EigenLayer, Ethereum
- source: examples/CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md
- validated:
- prediction: Jika menang di efisiensi modal, sumber daya (stake) akan terkonsentrasi → muncul kekhawatiran sentralisasi & dorongan mitigasi terdistribusi (mis. DVT). Nilai harus dinilai bersama ada/tidaknya mitigasi.
- watch: dominance > ~1/3 dari share; absennya mitigasi desentralisasi
- scope: Berlaku pada era pasca-Merge (2022–sekarang) di mana solo-staking berbiaya tinggi (32 ETH) mendorong agregasi; bergantung pada masih adanya friksi solo-staking dan minimnya regulasi anti-konsentrasi. Belum diuji di rezim regulasi yang membatasi staking-pool.

## P2 · Rehypothecation → Correlated Cascading Failure
- triggers: restaking, lrt, looping, liquid-restaking
- instances: 3
- analogs: EigenLayer, ether.fi, Ethereum
- source: examples/CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md
- validated: Renzo ezETH depeg Apr 2024 (~$688, >$65jt liquidations)
- prediction: Menggunakan ulang aset yang sama menaikkan yield sekaligus korelasi kegagalan. Risiko depeg + cascading liquidations saat leverage looping unwinding.
- watch: LRT discount / depeg event; posisi looping di lending; akhir window airdrop + likuiditas tipis
- scope: Era restaking/LRT (2023–sekarang), saat leverage looping via lending market marak dan likuiditas sekunder LRT masih tipis. Bisa melemah jika desain LRT masa depan membatasi re-collateralization.

## P3 · Multi-token → Simplification
- triggers: multi-token
- instances: 2
- analogs: Helium, Synthetix
- source: examples/CaseStudies/Batch-01-EvolutionAnalysis.md
- validated:
- prediction: Tokenomics multi-token yang rumit cenderung disederhanakan ke aset tunggal seiring project matang.
- watch: distorsi insentif antar-token; beban kognitif user
- scope: Lintas-era (diamati 2017–2025 di DeFi & DePIN) — tampak cukup timeless karena akar masalahnya (beban kognitif user, distorsi insentif) bukan fungsi kondisi pasar tertentu. Confidence tetap MEDIUM karena baru 2 instance.

## P4 · Airdrop-without-product → Post-TGE dump
- triggers: airdrop, points
- instances: 2
- analogs: ether.fi, LayerZero, Ethena
- source: examples/CaseStudies/CrossAnalysis-ETH-Lido-EigenLayer.md
- validated: Renzo REZ (alokasi 5%, exit farmer pasca-window)
- prediction: Airdrop/points tanpa produk & usage nyata → farmer keluar pasca-TGE → tekanan jual. Airdrop dengan produk dominan lebih dulu (Uniswap/Hyperliquid) → retensi jauh lebih baik.
- watch: alokasi airdrop kecil/membingungkan; aktivitas hanya untuk poin; unlock/vesting pasca-TGE
- scope: **Era-sensitif — jangan diterapkan buta.** Diamati 2020–2024 saat populasi airdrop-hunter masih tumbuh dan deteksi Sybil belum matang. Mekanisme "task mudah → JP besar" era 2021 (bridge-and-swap sederhana) TIDAK sebanding dengan era 2025–2026 (hunter jenuh, deteksi Sybil matang, task lebih rumit) — bandingkan Context (`docs/Ontology/Context.md`) target sebelum menerapkan, jangan hanya cocokkan mekanik permukaan.

## P5 · Technical success → Tokenomic harm
- triggers: fee-burn, upgrade, l2
- instances: 1
- analogs: Ethereum
- source: examples/CaseStudies/Ethereum.md
- validated: ETH Dencun (2024) → net-inflasi
- prediction: Upgrade yang memindah aktivitas keluar dari mekanisme value-accrual bisa merusak tesis token walau sukses teknis.
- watch: burn/revenue turun pasca-upgrade
- scope: Baru 1 instance (Ethereum/EIP-1559 era 2021–2024) — berlaku spesifik pada desain tokenomics yang value-accrual-nya terikat langsung ke throughput/kemacetan L1. Transferabilitas ke desain lain belum tervalidasi; confidence LOW sampai ada instance kedua.

## P6 · First-mover + standard = strongest moat
- triggers: first-mover, smart-contract, amm
- instances: 2
- analogs: Ethereum, Uniswap
- source: examples/CaseStudies/Ethereum.md
- validated:
- prediction: First mover yang menjadi standar developer punya moat retensi terkuat, mengalahkan pesaing 'lebih cepat/murah'.
- watch: apakah pesaing mengadopsi standarnya
- scope: Lintas-era (2015–sekarang) — bergantung pada adanya biaya migrasi developer yang nyata (tooling, likuiditas, efek jaringan), bukan pada kondisi pasar tertentu. Relatif timeless dibanding P4, tapi tetap MEDIUM karena baru 2 instance.

## P7 · Buyback ekuitas darurat sebagai perisai hukum pra-kepailitan
- triggers: buyback, treasury, kepailitan-pihak-ketiga, litigasi
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Buyback 100% ekuitas & waran token dari FTX Ventures/Alameda Research (~$134 juta, treasury internal, tanpa utang baru), 11 November 2022 — sehari sebelum kebangkrutan FTX.
- prediction: Proyek dengan investor yang tiba-tiba bangkrut/berskandal, dan kas internal cukup, akan memburu balik ekuitas/waran investor tsb secepatnya untuk mengunci kontrol sebelum kurator kepailitan bisa membekukan opsi korporat — berisiko dituduh preferential transfer & memicu litigasi, tapi biasanya berhasil secara jangka pendek.
- watch: investor utama masuk proses kepailitan/skandal besar; treasury proyek cukup besar untuk buyback tanpa utang baru; litigasi menyusul dari kurator/estate
- scope: Baru 1 instance (LayerZero, Nov 2022, era kolaps FTX). Confidence LOW sampai proyek lain dengan situasi serupa masuk lewat pipeline v3.

## P8 · Keamanan yang didelegasikan penuh ke aplikasi (application-owned security) tanpa guardrail wajib
- triggers: delegated-security, application-owned, misconfiguration, dvn
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Insiden Kelp DAO, 18 April 2026 (~$292 juta) — konfigurasi klien 1-of-1 DVN, bukan bug inti protokol.
- prediction: Infrastruktur yang memberi developer kontrol penuh atas parameter keamanan tanpa batas minimum wajib menarik developer lewat fleksibilitas, tapi risiko sistemik menumpuk di sisi klien — insiden besar pertama akan dipersepsikan sebagai kegagalan protokol keseluruhan, bukan cuma kesalahan konfigurasi satu klien.
- watch: tidak ada guardrail/minimum keamanan wajib di layer messaging/bridging; insiden besar pertama akibat salah konfigurasi klien
- scope: Baru 1 instance (LayerZero V2 + insiden Kelp DAO, 2024–2026). Confidence LOW.

## P9 · Permintaan maaf + perbaikan teknis pasca-insiden tidak memulihkan kepercayaan institusional yang sudah retak
- triggers: post-incident, apology, institutional-trust, capital-exodus
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Modifikasi DVN + permintaan maaf publik Mei 2026, tapi eksodus modal $7,24 miliar ke Chainlink CCIP berlanjut hingga Juli 2026.
- prediction: Setelah insiden yang mengungkap kerentanan sistemik pada infrastruktur berbasis kepercayaan, perbaikan teknis yang benar secara substansi tetap tidak menghentikan migrasi modal institusional — pemulihan kepercayaan makan waktu jauh lebih lama daripada waktu perbaikan teknisnya.
- watch: migrasi modal institusional berlanjut berbulan-bulan setelah fix diumumkan; TVL/volume tidak pulih ke level pra-insiden dalam waktu perbaikan
- scope: Baru 1 instance (LayerZero, 2026). Confidence LOW.

## P10 · Mekanisme governance/deflasi mati karena apati pemilih struktural, walau approval mayoritas tinggi
- triggers: governance-apathy, quorum-failure, fee-switch, voter-turnout
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Fee Switch referendum LayerZero gagal kuorum 4 kali berturut-turut meski >96% approval di antara yang memilih.
- prediction: Mekanisme tata kelola on-chain berambang kuorum tinggi akan tetap tidak aktif meski dukungan substantif nyaris bulat, karena partisipasi pemegang token besar & tak terkoordinasi secara struktural rendah — proyek akan dipaksa mencari jalur nilai-tangkap alternatif di luar mekanisme yang gated governance.
- watch: approval tinggi (>90%) tapi turnout gagal kuorum berulang kali; proyek mengumumkan mekanisme value-capture alternatif di luar jalur governance
- scope: Baru 1 instance (LayerZero Fee Switch, 2025–2026). Confidence LOW — berpotensi lintas-proyek governance-token berambang-kuorum tinggi manapun, tapi belum terkonfirmasi di luar LayerZero.

## P11 · Pivot dari infrastruktur murni ke pesaing L1 saat token utility gagal menangkap nilai
- triggers: infra-to-l1-pivot, value-capture-failure, governance-gridlock
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Peluncuran Zero (L1 milik LayerZero sendiri), 10 Februari 2026, setelah Fee Switch gagal aktif akibat kuorum.
- prediction: Proyek middleware/interoperabilitas dengan token governance yang gagal mengaktifkan mekanisme value-capture on-chain (mis. fee switch) akan berpindah dari "protokol murni" menjadi "L1 sendiri", memberi token utilitas baru (gas/staking/governance) yang tidak bergantung pada mekanisme lama yang macet.
- watch: fee-switch/value-capture on-chain proyek gagal aktif berulang kali; pengumuman L1/chain sendiri menyusul
- scope: Baru 1 instance (LayerZero, 2026). Confidence LOW — berkaitan erat dengan P10 (hubungan sebab-akibat langsung).

## P12 · "Proof-of-Donation" — donasi wajib sebagai filter klaim token memicu backlash "pajak ekstraksi"
- triggers: proof-of-donation, claim-mechanism, airdrop-backlash
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Mekanisme klaim LayerZero, 20 Juni 2024, mewajibkan donasi kecil per token ke protocol guild; direspons negatif oleh ritel sebagai "pajak klaim".
- prediction: Airdrop/TGE besar yang mewajibkan donasi pihak ketiga sebagai syarat klaim (filter spekulan + narasi barang publik) akan memicu backlash ritel jangka pendek yang dipersepsikan sebagai pajak paksa, meski niat desainnya defensif (mengurangi tekanan jual).
- watch: syarat klaim mencakup pembayaran/donasi wajib; sentimen ritel di media sosial menyebutnya "pajak"/"biaya klaim"
- scope: Baru 1 instance (LayerZero, Juni 2024). Confidence LOW.

## P13 · Akuisisi DAO memilih sinergi strategis di atas tawaran tunai lebih tinggi dari pesaing
- triggers: dao-acquisition, competing-bid, strategic-synergy
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Akuisisi Stargate oleh LayerZero (10–25 Agustus 2025), dipilih DAO Stargate meski Wormhole menawarkan $120 juta tunai lebih tinggi.
- prediction: Saat DAO matang menerima banyak tawaran akuisisi, tawaran dengan nilai nominal lebih rendah tapi sinergi strategis/kepercayaan jangka panjang yang jelas bisa mengalahkan tawaran tunai lebih tinggi dari pesaing — keputusan DAO tidak selalu rasional-finansial murni.
- watch: lebih dari satu tawaran akuisisi bersaing dengan selisih nominal signifikan; tawaran yang menang bukan yang tertinggi secara tunai
- scope: Baru 1 instance (LayerZero–Stargate, 2025). Confidence LOW.

## P14 · Riset internal (breakthrough teknis) memicu pivot arsitektur besar sebelum teruji produksi
- triggers: internal-research, technical-breakthrough, unproven-production
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: QMDB & FAFO (riset internal) mendasari peluncuran Zero (L1), 10 Februari 2026, masih tahap proof-of-concept.
- prediction: Terobosan riset internal (database/algoritma baru) yang secara teoritis mengatasi batasan skalabilitas akan memicu proyek mengumumkan pivot arsitektur besar dan menarik investasi — sebelum implementasi produksi benar-benar teruji di dunia nyata.
- watch: pengumuman pivot besar merujuk riset internal yang belum publikasi/audit independen; klaim skalabilitas belum ada data produksi live
- scope: Baru 1 instance (LayerZero, 2026). Confidence LOW.

## P15 · Model dual-verification bergantung pada asumsi non-kolusi yang rapuh
- triggers: dual-verification, single-point-of-failure, dvn, oracle-relayer
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Insiden Kelp DAO — kompromi 1-of-1 DVN meruntuhkan asumsi non-kolusi arsitektur dual-verification LayerZero V2.
- prediction: Arsitektur keamanan yang memisahkan verifikasi dan eksekusi ke pihak independen (mis. Oracle+Relayer, atau DVN+Executor) tetap punya titik kegagalan tunggal jika salah satu pihak dikompromi/dikonfigurasi terlalu longgar — "independen di atas kertas" tidak menjamin non-kolusi/non-kompromi di praktik.
- watch: konfigurasi verifier di bawah ambang aman (mis. 1-of-1 alih-alih multi-pihak); insiden akibat kompromi satu pihak verifikasi
- scope: Baru 1 instance (LayerZero, 2024–2026). Confidence LOW — berkaitan erat dengan P8.

## P16 · Ketergantungan pendapatan pada satu aplikasi/aset (stablecoin) unggulan
- triggers: revenue-concentration, stablecoin-dependency, flagship-dapp
- instances: 1
- analogs: LayerZero
- source: examples/CaseStudies/LayerZero.md
- validated: Pendapatan buyback LayerZero bertumpu pada TVL Stargate (stablecoin cross-chain); insiden Kelp DAO April 2026 turut menekan TVL Stargate.
- prediction: Proyek infrastruktur yang pendapatannya terkonsentrasi pada satu flagship dApp/kelas aset (mis. stablecoin) rentan terhadap penurunan pendapatan berantai saat TVL aplikasi tsb turun akibat insiden keamanan atau kompetisi dari solusi native — mekanisme buyback/value-capture yang bergantung pada pendapatan itu ikut melemah.
- watch: konsentrasi pendapatan >50% dari satu dApp/aset; kompetisi solusi native (mis. stablecoin native chain) muncul
- scope: Baru 1 instance (LayerZero–Stargate, 2026). Confidence LOW.
