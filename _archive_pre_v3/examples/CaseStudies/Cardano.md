# Cardano — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Laporan Analisis Sistematis Jaringan Cardano (ADA): Rekayasa Arsitektur,
Evolusi Tata Kelola, dan Masa Transisi Infrastruktur Desentralisasi"* (no-table `.docx` rebuild) — merged with the
prior comprehensive report (`.pdf`) that contributed the Hydra/Mithril/Leios, Ouroboros-parameter, ISPO, and RealFi depth.
**Pipeline position:** Applications layer — an anchor artifact structured against the full `docs/` ontology.
Serves as the **peer-reviewed / formal-methods "engineering-first" L1** analog: a Fast Follower that redesigned
from first principles (EUTXO, Ouroboros) rather than cloning EVM — contrast Ethereum (First Mover), Solana
(hardware-limit monolith), BNB (exchange-backed EVM clone).
**Raw source archived:** `doc_backup/deep/Cardano_2026-07_gemini.docx` (+ `.md` text extraction) — **rebuilt from the
higher-fidelity no-table `.docx`; prior `.pdf` retained** at `doc_backup/deep/Cardano_2026-07_gemini.pdf`.
**Input note:** authored in the CIF no-table contract; extracted via `tools/extract.py` (0 tables, 0 chips,
23 sections); fidelity checked with `tools/reconcile.py`.

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** Cardano (token: ADA).
- **Category:** Layer 1 / "generasi ketiga" smart-contract platform — peer-reviewed, formal-methods,
  UTXO-based, modular (CSL settlement + CCL computation).
- **Era:** 2015 (IOHK) – sekarang (pertengahan 2026).
- **Founders:** Charles Hoskinson & Jeremy Wood (via IOHK, kini **IOG**). Named: proyek dari matematikawan
  **Girolamo Cardano**; token **ADA** dari **Ada Lovelace**.
- **Innovation archetype:** **Fast Follower** yang **merancang ulang dari dasar** (bukan fork EVM); pendekatan
  *research-first / formal verification*. → `docs/Innovation/FastFollower.md`, `docs/Innovation/Timing.md`.

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

Layer 1 · model buku besar **Extended UTXO (EUTXO)** (deterministik) · konsensus **PoS Ouroboros** (Praos →
Leios) · bahasa **Plutus (Haskell)** → pivot **Aiken/OpShin/Scalus** · tata kelola on-chain **CIP-1694
(Voltaire)** · liquid staking **tanpa lock-up & tanpa slashing**. Arsitektur berlapis: **CSL** (Cardano
Settlement Layer) terpisah dari **CCL** (Cardano Computation Layer).

## 3. Pre-Conditions — Kelemahan Blockchain Gen-1/Gen-2 (2015–2017)
_Konteks: mengapa Cardano harus ada._
_ref: `docs/Meta/Narratives.md`, `docs/Ontology/Security.md`_

Tesis pendirian: **infrastruktur keuangan global tak boleh dibangun dengan metode *trial-and-error*.** Cardano
menyoroti tiga cacat struktural model **account-based** Ethereum:
- **Non-determinisme transaksi** — status akun global berubah dinamis; transaksi bisa **gagal di tengah
  eksekusi** namun **tetap membebankan gas** kepada pengguna.
- **Volatilitas gas & gas-war** — kebutuhan komputasi off-chain tak terprediksi → lelang biaya merugikan ritel.
- **Kerentanan kontrak** — sifat interaktif EVM mempermudah **re-entrancy** (The DAO, 2016 → hard fork memecah
  komunitas). *(Peristiwa yang sama didokumentasikan dari sisi Ethereum di `examples/CaseStudies/Ethereum.md` §7.)*

Jawaban Cardano: **verifikasi matematika ketat + metode formal** (ala rekayasa dirgantara) untuk menjamin
keamanan skrip **sebelum** deploy.

## 4. Origin & Team — Genealogi dari Perpecahan Ethereum
_ref: `docs/Ontology/Team.md`, `docs/Ontology/Governance.md`, `docs/Project/Philosophy.md`_

**Charles Hoskinson** (CEO awal Ethereum Foundation) berselisih dengan **Vitalik Buterin** pertengahan 2014:
Hoskinson mengusulkan Ethereum **for-profit** (struktur VC); Buterin bersikeras **non-profit**. Hoskinson
**keluar Juni 2014** → mendirikan **IOHK (2015)** bersama **Jeremy Wood**. *(Ini adalah sisi lain dari "Konflik
Zug" yang membuat Hoskinson keluar — lihat `examples/CaseStudies/Ethereum.md` §4; genealogi kausal langsung
antara dua anchor.)*

**Struktur tiga entitas** (pemisahan yurisdiksi & fungsi — sebuah pilihan tata kelola yang disengaja):
| Entitas | Yurisdiksi / bentuk | Peran |
|---|---|---|
| **IOG** (dahulu IOHK) | Hong Kong / AS, perusahaan teknik | Riset akademis, protokol kripto inti, rekayasa node, hard fork |
| **Cardano Foundation** | Zug, Swiss, yayasan nirlaba | Kepatuhan hukum, standardisasi, edukasi, relasi regulator |
| **Emurgo** | Jepang / Singapura, komersial | Akselerator adopsi dApp korporat, dana ventura, integrasi bisnis |

*Pelajaran kausal:* pemisahan tiga-entitas memberi legitimasi & disiplin regulasi, tetapi **memperlambat
eksekusi** (koordinasi lintas-entitas) — tema berulang (bandingkan trade-off nirlaba Ethereum). → `docs/Ontology/Governance.md`.

## 5. Innovation Analysis — EUTXO & Native Assets
_ref: `docs/Ontology/Innovation.md`, `docs/Innovation/FastFollower.md`, `docs/Innovation/CompetitiveMoat.md`, `docs/Ontology/Technology.md`_

**Extended UTXO (EUTXO)** — memperluas UTXO Bitcoin dengan tiga komponen agar mendukung kontrak pintar kompleks:
1. **Datum** — wadah status arbitrer yang melekat pada UTXO (mesin status terdistribusi tanpa global state).
2. **Redeemer** — argumen masukan pembelanja untuk memenuhi logika skrip.
3. **Script Context** — data transaksi terenkapsulasi (inputs/outputs/fee/metadata).

*Dampak:* eksekusi **deklaratif & deterministik mutlak** — validasi bisa diverifikasi **off-chain sebelum
kirim**; jika lolos lokal, **dijamin sukses di mainnet** tanpa boros gas akibat kegagalan skrip. Mengeliminasi
kelas kerentanan re-entrancy pada transfer dasar.

**Native Multi-Assets** — token kustom di **ledger-level** (tanpa kontrak ERC-20/721); token diperlakukan
setara ADA → sub-cent fee, tanpa vektor bug kontrak pada transfer. *Pelajaran:* **memisahkan data aset dari
logika transfer** memangkas biaya & permukaan serangan (pola "Declarative Ledger Optimization", §19).

## 6. Technology Evolution — Lima Era
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`, `docs/Ontology/Infrastructure.md`_

| Era | Mulai | Fokus & rilis kunci |
|---|---|---|
| **Byron** | Sep 2017 | Model federasi (node IOHK/Emurgo/Foundation); dompet Daedalus & Yoroi; transfer ADA |
| **Shelley** | Jul 2020 | Desentralisasi penuh → **Ouroboros Praos**; ribuan **SPO**; liquid staking tanpa lock-up |
| **Goguen** | Sep 2021 | **Alonzo HF** → kontrak pintar **Plutus Core V1** (Haskell); metadata NFT **CIP-25** |
| **Basho** | Sep 2022 | **Vasil HF** → Plutus V2 (Reference Inputs, Inline Datums); **Hydra** (L2 state channels), **Mithril** (light client), **Ouroboros Leios** (paralel) |
| **Voltaire** | Sep 2024 | **Chang HF #1** → tata kelola on-chain **CIP-1694**; **Van Rossem HF** (PV11, 18 Jul 2026) — hard fork pertama yang **diajukan/divoting/diratifikasi sepenuhnya on-chain** (77,63% DReps) |

**Basho scaling stack:** **Hydra Head** (state channels isomorfik, latensi mikrodetik, sub-cent) · **Mithril**
(sertifikat multi-signature ambang → sinkronisasi node dari harian ke menit) · **Ouroboros Leios** (uji publik
**23 Jun 2026, "Musashi Dojo"**) memecah produksi blok jadi **Input / Endorser / Ranking Blocks** paralel →
target **10 TPS → >1.000 TPS**.

## 7. Funding / TGE — ICO Ritel-Sentris (2015–2017)
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md`, `docs/TokenLifecycle/TGE.md`_

**Crowdsale voucher (Sep 2015 – Jan 2017):** total **108.844,48 BTC = $62,24 juta** (avg $571,79/BTC); **>90%
investor Jepang** via **agen penjualan fisik** (bukan ICO online); harga voucher **$0,0024/ADA**; **25.927.070.538
ADA** redeemable. **9.912 pemilik unik** (9.835 personal + 77 company); 4 tranche (T4 terbesar 47,3% / 6.821 tiket).
KYC ketat; **warga AS & Tiongkok dilarang** (mitigasi risiko sekuritas). **~99% voucher berhasil ditebus** di fase
awal Byron (via Daedalus), memvalidasi eksekusi crowdsale.

**Alokasi genesis** (hard cap **45 miliar ADA**; **31.112.484.646 ADA** dicetak di genesis):
| Kategori | ADA | % genesis | Vesting |
|---|---|---|---|
| Peserta Penjualan Publik | 25.927.070.538 | **83,3%** | cair penuh sejak genesis |
| IOG (IOHK Treasury) | 2.463.071.701 | 7,9% | 1/3 cair, 1/3 Jun 2018, 1/3 Jun 2019 |
| Emurgo | 2.074.165.644 | 6,7% | modal komersial |
| Cardano Foundation | 648.176.761 | 2,1% | dana abadi nirlaba *(INKONSISTENSI: Figment catat 640 juta; CIF pakai angka genesis presisi-Lovelace, evidence HIGH)* |

*Pelajaran kausal:* **absennya VC Barat raksasa** menghindarkan ADA dari **tekanan jual (dumping)** terjadwal,
tetapi juga **minim modal promosi & pendanaan startup dApp** — sebagian menjelaskan kelambatan DeFi (§13). →
`docs/MarketBehaviour/Distribution.md`, `docs/Ontology/Risks.md`.

### Forensik distribusi BTC crowdsale — kontroversi transparansi (2025–26) *(causal governance event)*
Distribusi hasil crowdsale memicu **tuntutan transparansi** pertengahan 2025–awal 2026: **IOHK menerima ~54.000 BTC
(~50% hasil)** → asimetri alokasi modal antar-pendiri diperdebatkan; **7.168 BTC** ke Cardano Foundation (Swiss),
**1.090 BTC** ke entitas Isle of Man. Hoskinson mengklarifikasi **1.096 BTC dicairkan Mar 2016 @ $414/BTC (~$400rb)**
untuk bayar audit crowdsale (Michael Parsons, John Maguire, Bruce Milligan), **tetapi alamat on-chain penerima akhir
belum dipublikasi** → evidence forensik **MEDIUM** (§22). *Pelajaran: distribusi treasury pendiri era-ICO tanpa jejak
on-chain publik menjadi liabilitas kepercayaan bertahun-tahun kemudian.* → `docs/Ontology/Governance.md`, `docs/Patterns/Failure.md`.

## 8. Tokenomics — Emisi Meluruh & Parameter Ouroboros
_ref: `docs/Ontology/Tokenomics.md`, `docs/Ontology/Incentives.md`, `docs/Patterns/Mining.md`, `docs/MarketBehaviour/UnlockImpact.md`_

- **Hard cap:** 45 miliar ADA · **TGE (Sep 2017):** 31,11 miliar · **Cadangan emisi:** 13,89 miliar.
- **Emisi meluruh:** tiap epoch (5 hari) dari cadangan dengan **ρ = 0,3%** → inflasi menurun eksponensial
  (tanpa inflasi abadi).
- **Parameter K = 500** → **saturation point ≈ 76 juta ADA/kolam** (di atas itu tak ada imbalan tambahan →
  mendorong distribusi delegasi). **A0 (pledge influence)** → mengurangi serangan Sybil kolam fiktif.
- **Reward Pot** (biaya tx + emisi baru): **80% konsensus** (SPO + delegator, setelah fixed fee min **170 ADA**
  + margin), **20% Treasury** on-chain (dana Catalyst).

Rumus imbalan kolam (IOG): `f(σ',λ') = R/(1+a0) · (σ' + λ'·a0·(σ' − λ'·(1−σ')/σ'))`, dengan `σ'` = rasio
taruhan efektif (batas `min(σ,1/k)`) dan `λ'` = rasio pledge (batas `min(λ,1/k)`).

## 9. Airdrop & Incentive — ISPO (Initial Stake Pool Offering)
_ref: `docs/Patterns/Points.md`, `docs/Success/Airdrop.md`, `docs/Ontology/Incentives.md`, `docs/Patterns/Liquidity.md`_

Cardano **menolak airdrop spekulatif instan** (dinilai memicu tekanan jual). Inovasi asli: **ISPO** —
memanfaatkan liquid staking non-custodial:
1. User **mendelegasikan** ADA ke SPO milik proyek baru (ADA **tetap** di dompet non-custodial user).
2. Jaringan memproduksi imbalan staking (~4–5% APY).
3. Proyek mengambil **100% imbalan ADA** sebagai modal, lalu mengirim **token kustom** proporsional ke user.

*(Shelley ITN 2019 memobilisasi **~40% pasokan beredar** terdelegasi ke node uji — bukti daya-tarik staking non-custodial.)*

**Keberhasilan:** **tanpa risiko pokok** (jika tim kabur, user hanya kehilangan potensi yield, bukan modal);
demokratisasi penggalangan dana tanpa dominasi VC. **Kegagalan:** **konsentrasi block-power sementara** (multi-
pool satu tim mendistorsi indeks desentralisasi Shelley); **tanpa filter kualitas** (proyek buruk menguras
imbalan ritel lalu merilis token tanpa fungsi). *Pola reusable, layak ditiru* (§18). → `docs/Success/Airdrop.md`.

## 10. Community & Governance — Catalyst, Intersect, & Krisis Fund 13
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Governance.md`, `docs/Success/Community.md`, `docs/Patterns/Failure.md`_

- **Project Catalyst** — pendanaan inovasi terdesentralisasi terbesar; **min 500 ADA** untuk propose/vote;
  kumulatif **$131,9 juta** ke **2.221 proposal terdanai** (1.673 selesai, 290 berjalan, 253 DNF); **3.257.805 suara**
  sepanjang seluruh fund. **ADA Army** ritel Jepang loyal (basis awal via agen luring).
- **Zero-slashing + no lock-up** → ritel merasa aman mendelegasikan tanpa kehilangan likuiditas.
- **Intersect MBO** (akhir 2023) — Member-Based Org yang mengalihkan kode sumber ke komunitas; kini **kelola
  perbendaharaan >345 juta ADA** + pimpin migrasi **multi-klien** (§12).
- **Ambassador Program** (Cardano Foundation).

### Plutokrasi Catalyst — paradoks 1-Lovelace-1-suara *(causal event)*
Data **Fund 10** menyingkap ketimpangan: **57.118 dompet / 4,5 miliar ADA terdaftar**, tapi hanya **13,7%** ADA
beredar ikut voting; golongan **1–5 juta ADA (hanya 1,35% partisipan) menguasai 33% suara**. Puncaknya **Fund 13
(9 Des 2024): Cardano Foundation kerahkan 180 juta ADA** → sepihak meloloskan **185 dari 1.800 proposal**,
mementahkan pilihan organik. Respons: **Fund 14 (Sep 2025)** CF membatasi diri ke **satu dompet 20 juta ADA**, hanya
jalur **"Partners & Products"** (budget 18,59 juta ADA / $12,61 juta; 131 dari 1.283 terdanai; 174.737 suara). Lalu
**Fund 15 & 16 ditangguhkan (Mar 2026)** saat operator beralih ke CF → **jeda pendanaan** memukul builder skala menengah
(→ verdict Builder Gagal, §16). *Pelajaran:* tata kelola stake-weighted rentan plutokrasi; butuh pembatasan diri/aturan. →
`docs/Patterns/Failure.md`, `docs/Ontology/Governance.md`.

**Voltaire (CIP-1694):** pembagian kekuasaan tripartit **DReps + SPOs + Constitutional Committee**; Konstitusi
Digital pertama diratifikasi **Buenos Aires (4–6 Des 2024) → on-chain 23 Feb 2025** (>75% DReps). **Plomin HF
(29 Jan 2025)** mengaktifkan tata kelola penuh DReps.

### Founder Governance Divestment — reset struktural 2026 *(crown governance pattern)*
Puncak desentralisasi: **Van Rossem HF (18 Jul 2026, PV11)** = hard fork pertama yang diajukan/divoting/diratifikasi
**sepenuhnya on-chain** (voting 13 Jul, DReps+SPOs+CC, tanpa kendali IOG) → aktif **zero-downtime**. Diikuti **IOG
memotong pengajuan anggaran kas-nya secara sengaja** dan **mentransfer rekayasa inti** (Haskell Node, Plutus, Daedalus,
Hydra) ke entitas eksternal **Se7en Labs & Teragone (Agu 2026)** di bawah pengawasan Intersect MBO. *Pola reusable:
protokol matang → serahkan repo ke org berbasis-anggota → pendiri divestasi anggaran → maintenance ke spesialis eksternal
→ kedaulatan teknis terdistribusi penuh* (§19). → `docs/Patterns/Recovery.md`, `docs/Ontology/Governance.md`.

## 11. Narrative Intelligence (peran per fase)
_ref: `docs/Meta/Narratives.md`, `docs/Patterns/Narrative.md`, `docs/Meta/MarketCycles.md`_

| Fase | Narasi | Peran |
|---|---|---|
| 2017–2020 | Riset akademis & verifikasi formal (peer-review) | **Pencipta** |
| 2021–2023 | **RealFi** & inklusi finansial / DID Afrika | **Pencipta** (Atala PRISM; Ethiopia; FaydaPass Mei 2025 + Visa/MOSIP; Maisha Namba Kenya) |
| 2021–2024 | DeFi Summer / AMM / L2 rollups | **Terlambat** (konkurensi EUTXO + kesulitan Haskell/Plutus) |
| 2024–2025 | Tata kelola konstitusional berdaulat on-chain | **Pencipta** (Konstitusi digital pertama) |
| 2026 | Likuiditas multi-rantai & privasi | **Pengikut aktif** (LayerZero; sidechain **Midnight**) |

Cross-link: `examples/Pioneer/LayerZero.md`; DID/identity ↔ `examples/Pioneer/WorldNetwork-Worldcoin.md`.

## 12. Product Evolution — Wallets & Language Pivot
_ref: `docs/Project/Roadmap.md`, `docs/Ontology/Adoption.md`_

- **Wallets:** Daedalus (2017, full-node) → Yoroi (2018, light, Emurgo) → **Lace (2023, IOG Web3)**.
- **Pivot bahasa kontrak** (mengatasi isolasi Haskell): **Aiken** (sintaks mirip Rust, kompilasi ke UPLC,
  kompilasi menit→detik, hemat ExUnits, test runner) — dominan; **OpShin** (Python); **Scalus** (Scala 3/JVM).
- **L2/scaling baru (2026):** **Midgard** (optimistic rollup, Anastasia Labs, deterministic fraud proofs);
  **zkFold & Eryx** (ZK compression); **Gummiworm** (rollup ala Hydra, Sundae Labs).
- **Multi-client node diversity (2026–27):** dari **Haskell Node tunggal** (single-point-of-failure) ke **multi-
  implementasi** — **Amaru/Acropolis (Rust)**, **Dingo (Go)** — dijadwalkan matang 2027; rekayasa diserahkan ke
  **Se7en Labs & Teragone** (Agu 2026, §10). *Pola defensif: keragaman klien = ketahanan sistemik.*
- **Midnight partner chain:** rantai privasi selektif (ZK) berbasis **token ganda NIGHT + DUST** & bahasa **Compact**
  (mirip TypeScript); distribusi **Glacier Drop** lintas-8-ekosistem (ADA/BTC/ETH/SOL/XRP/BNB/AVAX/BAT) untuk memperluas
  basis validator ke luar Cardano. → `docs/Ontology/Ecosystem.md`.

*Pelajaran:* pivot dari "Haskell-only akademis" ke **multi-bahasa + L2 + multi-klien** = koreksi strategis atas hambatan
adopsi developer & risiko single-client. → `docs/Innovation/ProductMarketFit.md`.

## 13. Competitive Landscape (pertengahan 2026)
_ref: `docs/Valuation/Competitors.md`, `docs/Valuation/ComparableProjects.md`, `docs/Meta/MarketCycles.md`_

| Parameter | **Cardano** | Ethereum | Solana | Sui |
|---|---|---|---|---|
| Ledger | **EUTXO** | Account | Account | Object |
| Bahasa | Plutus/Aiken | Solidity/EVM | Rust/C++ | Sui Move |
| Keamanan eksekusi | **Deterministik mutlak** | Non-deterministik | Non-deterministik | Deterministik dasar |
| TVL | **~$132 juta** | ~$38,24 mrd | ~$4 mrd | ~$850 juta |
| Outage | **0 (sempurna)** | sangat kuat | rentan saat padat | kuat |
| Staking | bebas kunci, **tanpa slashing** | dikunci, slashing | sebagian dikunci, slashing | dikunci |

**Unggul struktural:** imunitas outage (determinisme EUTXO), keamanan konsensus (no-slashing menarik delegator
ritel raksasa), kemandirian tata kelola (vs ketergantungan figur Buterin). **Kalah likuiditas DeFi:** **dilema
konkurensi UTXO** (satu UTXO = satu tx/blok → AMM sulit, butuh off-chain batching) & **isolasi bahasa Haskell**
(defisit developer; Aiken memperkecil tapi migrasi lambat). → `examples/CaseStudies/Solana.md`, `Ethereum.md`.

## 14. Token Lifecycle & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Valuation/FairValue.md`, `docs/Reasoning/Prediction.md`_

| Titik | Nilai | Kondisi |
|---|---|---|
| ICO voucher | $0,0024 | 2015–17 |
| Buka bursa (Bittrex) | ~$0,03 | Okt 2017 |
| Pump #1 | **$0,72 → $0,52–1,30** | Des 2017–Jan 2018 (gelembung ritel; peak intraday ~$1,11–1,30) |
| **ATL** | **$0,01925** | **12 Mar 2020** (likuidasi massal COVID "Black Thursday") |
| Bear 2018 | −>90% → ~$0,04 | akhir 2018 (crypto winter) |
| **ATH** | **$3,09** *(alt $3,10)* (MC >$90 mrd, #3 dunia) | 1 Sep 2021 (demam Alonzo + likuiditas global) |
| Konsolidasi 2025–26 | **$0,16–0,35** (−~95% dari ATH) | pertengahan 2026 (rotasi modal ke rantai ber-DeFi tinggi) |

*_Catatan kurasi:_ rebuild `.docx` **menyelesaikan** inkonsistensi ATL yang ditandai versi sebelumnya (dulu tercatat
"$0,01735 Okt 2017" — mustahil vs harga buka $0,03): ATL sebenarnya **$0,01925 pada 12 Mar 2020** (krisis likuiditas
COVID), konsisten dengan lini masa. Evidence: HIGH. → `docs/Research/Verification.md`.

**Fair value:** **MC/TVL ratio ~66,49×** (MC ~$6,194 mrd / TVL ~$137 juta; vs Ethereum <10×) — tertinggi di industri.
**Overvalued** dari sisi pemanfaatan modal DeFi (utilitas dApp harian minim, ditopang loyalitas holder jangka panjang +
efek figur Hoskinson) **vs Undervalued** dari sisi infrastruktur (ADA ter-stake pasif tanpa lock dalam proporsi besar;
konversi sebagian kecil ke DeFi bisa melipatgandakan TVL). Kepastian **SEC: ADA = komoditas, bukan sekuritas** menghapus
risiko hukum bagi manajer dana besar. → `docs/Valuation/FairValue.md`, `docs/Valuation/FDV.md`.

## 15. Business Intelligence & Real-World Adoption
_ref: `docs/Ontology/Revenue.md`, `docs/Valuation/Revenue.md`, `docs/Ontology/Metrics.md`, `docs/Success/Adoption.md`_

**Metrik DeFi (Apr–Jul 2026):** TVL **~$133,8 juta (Apr)** → **~$137 juta** (rank ~27); **volume harian DEX/perps
~$371–374 juta**; MC **$10,5 mrd (Mei, ADA $0,30)** → **~$6 mrd (Jul, ADA $0,16)**. *Kesenjangan lebar antara
keamanan tinggi & pemanfaatan komersial rendah.*

**Protokol DeFi domestik (Apr 2026):** Minswap (DEX, $33,3jt, ~25% dominasi, migrasi V2/Aiken) · Danogo (DEX, $16,3jt) ·
WingRiders ($5jt) · Indigo (CDP/sintetis, $6,21jt) · Liqwid (lending, $10–15jt). **Aiken** dipakai **>75%** pengembang
(sensus 2025). **Stablecoin:** **Djed** (Jan 2023, COTI, overcollateralized 400–800%) · **USDM** (Mar 2024, Mehen,
fiat-backed 1:1) · **USDA** (Feb 2025, EMURGO/Anzens) · **Circle USDCx** (Feb 2026, native via CCTP ke **50+ rantai**,
**36% pangsa stablecoin** Cardano). *(Konteks makro: stablecoin non-USD global $1,4 mrd vs USD $300 mrd.)*

**Adopsi riil (RealFi):** **Syngenta India** (registrasi >15.000 petani + DID + citra satelit) · **Trivolve
Tech** (>100.000 dokumen forensik hukum on-chain) · **Atala PRISM Ethiopia** (ID digital 5 juta siswa + 750rb guru) ·
**kompatibilitas standar CMTAT Swiss** (sekuritas teregulasi). *Kekuatan Cardano ada di adopsi institusi/pemerintah,
bukan DeFi spekulatif.* → `docs/Success/Adoption.md`.

## 16. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

Success **tidak biner** — verdict per point-of-view + evidence level (8 POV per `docs/Protocol/Deep-Research-Brief.md`):

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** (`Success/Founder.md`) | ⚠️ Campuran | Membuktikan rekayasa peer-review → blockchain tangguh tanpa outage; tapi "keras kepala" menunda rilis pasar → kehilangan momentum emas DeFi | HIGH |
| **VC** (`Success/VC.md`) | ⚠️ Campuran | Sebagian VC via Emurgo untung di ATH 2021; tapi ICO ritel-sentris + tanpa dumping menghalangi VC mendominasi tata kelola/harga | MEDIUM |
| **Retail** (`Success/Community.md`) | ⚠️ Campuran | Liquid staking teraman (no lock-up/no slashing, yield pasif); tapi banyak ritel beli di puncak & terjebak ISPO gagal | MEDIUM |
| **Community** (`Success/Community.md`) | ✅ Sukses | Komunitas organik terkuat; Catalyst $130jt/1.800 proyek; konstitusi on-chain — meski krisis plutokrasi Fund 13 | HIGH |
| **Developer** (`Success/Developer.md`) | ⚠️ Campuran | EUTXO membebaskan dari re-entrancy; tapi kurva Haskell curam + konkurensi UTXO memperlambat rilis | MEDIUM |
| **Institution** (`Success/Adoption.md`) | ✅ Sukses | Audit formal + kepatuhan CMTAT Swiss + konstitusi → legalitas untuk sekuritas on-chain (Syngenta, Trivolve) | HIGH |
| **Validator/SPO** (`Success/Protocol.md`) | ⚠️ Campuran | Pembagian imbalan transparan berpihak kolam kecil; tapi persaingan delegator menekan margin ke batas minimum protokol | MEDIUM |
| **Builder (dApp/DeFi)** (`Success/Ecosystem.md`) | ❌ Tertinggal | TVL rank-27, likuiditas dangkal, konkurensi UTXO memaksa off-chain batching; efek jaringan kalah dari EVM/Solana | MEDIUM–HIGH |

**Takeaway:** Cardano **menang di community & institution** (keamanan, legalitas, tata kelola) namun **tertinggal
di builder/DeFi** — profil kebalikan dari BNB/Solana yang kuat di ritel/likuiditas tetapi lemah di
desentralisasi. Trade-off inti: **rekayasa formal → keandalan, dengan ongkos kecepatan pasar.**

## 17. Historical Timeline
_ref: `docs/TokenLifecycle/*`_

- **Jun 2014** — Hoskinson keluar dari Ethereum (dispute non-profit vs for-profit dgn Buterin).
- **Mar 2015** — IOHK didirikan (Hoskinson + Wood). **Sep 2015–Jan 2017** — crowdsale voucher 108.844 BTC / $62,24 juta. **Mar 2016** — 1.096 BTC untuk audit (Parsons/Maguire/Milligan).
- **29 Sep 2017** — genesis mainnet (Era Byron); ADA buka ~$0,03. **10 Jan 2018** — Yoroi (Emurgo). **Des 2017–Jan 2018** — pump ritel $0,72→$1,30.
- **12 Mar 2020** — **ATL $0,01925** (COVID). **29 Jul 2020** — **Shelley HF** (PoS terdesentralisasi). **Apr 2021** — kemitraan Ethiopia (Atala PRISM, 5jt siswa).
- **1 Sep 2021** — **ATH $3,09** (MC >$90 mrd). **12 Sep 2021** — **Alonzo HF** (Plutus V1, Era Goguen). **Okt 2021** — 318,2 juta ADA voucher tak-terklaim → 6 alamat staking.
- **22 Sep 2022** — **Vasil HF** (Plutus V2). **18 Nov 2022** — pengumuman **Midnight**. **Jan 2023** — stablecoin **Djed** (COTI). **11 Apr 2023** — **Lace 1.0** (IOG). **Des 2023** — 25 repo pertama → **Intersect MBO**.
- **16 Mar 2024** — stablecoin **USDM** (Mehen). **1 Sep 2024** — **Chang HF #1** (Era Voltaire, CIP-1694 bootstrap). **4–6 Des 2024** — Konvensi Konstitusional. **9 Des 2024** — kontroversi **Fund 13** (180 juta ADA yayasan → 185/1.800 proposal).
- **29 Jan 2025** — **Plomin HF** (tata kelola penuh DReps). **Feb 2025** — stablecoin **USDA** (EMURGO/Anzens). **23 Feb 2025** — Konstitusi Digital diratifikasi on-chain (>75%). **Sep 2025** — Fund 14 (CF dibatasi 20 juta ADA).
- **Feb 2026** — **Circle USDCx** mainnet (CCTP 50+ rantai). **Mar 2026** — **Fund 15 & 16 ditangguhkan** (jeda pendanaan builder). **18 Jun 2026** — ADA 5yr-low ~$0,16. **23 Jun 2026** — testnet **Leios "Musashi Dojo"** (target >1.000 TPS). **Jun 2026** — **Lace v1.17** (sinkron instan).
- **13 Jul 2026** — voting on-chain Van Rossem (DReps+SPOs+CC). **18 Jul 2026** — **Van Rossem HF** (PV11) aktif zero-downtime — hard fork pertama sepenuhnya on-chain. **Agu 2026** — IOG transfer Haskell Node/Plutus/Daedalus/Hydra ke **Se7en Labs & Teragone**.

## 18. Current Status & Lessons Learned
_ref: `docs/TokenLifecycle/Maturity.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`_

**Status (pertengahan 2026):** *"Transisi Struktural & Pemulihan Sistemik"* — harga di 5yr-low (~$0,16, kelelahan
ritel atas TVL rank-27), **tetapi** ketahanan protokol tertinggi sepanjang sejarah: Voltaire beroperasi penuh
(DReps + CC); **Intersect MBO kelola perbendaharaan >345 juta ADA**; migrasi **multi-klien** (Haskell/Rust/Go, matang
2027) + handoff rekayasa ke Se7en Labs/Teragone menandai transisi dari ketergantungan IOG ke **jaringan mandiri**. Van
Rossem HF zero-downtime + Leios testnet. **Bukan** dead chain; menanti Leios untuk membuka adopsi komersial skala besar.

**Kesalahan terbesar (antipatterns):**
1. **Analysis paralysis** — kesempurnaan akademis menunda kontrak pintar bertahun-tahun → kehilangan momentum DeFi.
2. **Friction-heavy DX** — mewajibkan Haskell tanpa jembatan bahasa populer di masa krusial awal.

**Praktik terbaik (replicate):**
1. **Pemisahan CSL/CCL** — melindungi rantai utama dari malafungsi skrip dApp.
2. **Hard Fork Combinator (HFC)** — upgrade ledger masif **tanpa downtime & tanpa rantai pecahan**.
3. **Model ISPO** — penggalangan dana komunitas aman-pokok, layak ditiru.

## 19. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*`, `docs/Schema/PatternSchema.md`_

1. **Declarative Ledger Optimization (DLO)** — pisahkan data statis aset dari logika transfer di ledger utama →
   transfer token tanpa VM kontrak, biaya sub-cent, hilangkan vektor bug transfer. → `docs/Ontology/Technology.md`.
2. **Zero-Slashing Liquid Trust (ZSLT)** — delegasi non-custodial tanpa penahanan & tanpa slashing → partisipasi
   staking sangat tinggi (>60%) → imunitas pengambilalihan konsensus. → `docs/Ontology/Security.md`.
3. **Research-First → Time-to-Market Debt** — verifikasi formal menaikkan keandalan tetapi menumpuk **utang
   kecepatan pasar**; incumbent merebut likuiditas duluan. → `docs/Innovation/Timing.md`, `docs/Patterns/Failure.md`.
4. **Retail-Centric ISPO Fundraising** — alihkan yield staking (bukan pokok) sebagai modal proyek → demokratis &
   aman-pokok, tapi tanpa filter kualitas + konsentrasi block-power sementara. → `docs/Success/Airdrop.md`.
5. **Stake-Weighted Governance → Plutocracy Risk** — 1-koin-1-suara rentan didominasi pemegang besar (Fund 13);
   butuh self-limit/aturan. → `docs/Patterns/Failure.md`, `docs/Ontology/Governance.md`.
6. **UTXO Concurrency Constraint** — satu UTXO = satu tx/blok → AMM butuh off-chain batching, mematikan
   komposabilitas atomik murni; hambatan struktural DeFi. → `docs/Reasoning/Prediction.md`.
7. **On-Chain-Ratified Hard Fork (HFC)** — upgrade tanpa downtime + ratifikasi on-chain = sinyal kematangan
   tata kelola & infrastruktur. → `docs/Patterns/Recovery.md`.
8. **Founder Governance Divestment** *(crown pattern, rebuild)* — protokol capai kematangan teknis → repo diserahkan ke
   org berbasis-anggota (Intersect MBO) → **pendiri sengaja memotong pengajuan anggaran kas-nya** → maintenance node
   dialihkan ke spesialis eksternal (Se7en Labs/Teragone) → kedaulatan teknis terdistribusi penuh. Sinyal desentralisasi
   *tertinggi*: proyek bertahan **tanpa ketergantungan penciptanya**. → `docs/Patterns/Recovery.md`, `docs/Ontology/Governance.md`.
9. **ICO Treasury Opacity Liability** — distribusi hasil crowdsale era-ICO (54.000 BTC IOHK, 1.096 BTC audit) **tanpa
   jejak alamat on-chain publik** menjadi **liabilitas kepercayaan** yang meletus bertahun-tahun kemudian. → `docs/Patterns/Failure.md`.

### Entitas & relasi ontologi (kandidat Knowledge Graph)
_ref: `docs/Schema/KnowledgeGraph.md`, `docs/Schema/EntityRelationship.md`_
- `[Cardano] —utilizesLedgerModel→ [EUTXO]` · `[EUTXO] —encapsulatesData→ [Datum, Redeemer, Script_Context]`
- `[Cardano] —governedBy→ [CIP-1694]` · `[CIP-1694] —empowersVoters→ [DReps, SPOs, Constitutional_Committee]`
- `[Ouroboros_Leios] —implementsParallelism→ [Input/Endorser/Ranking_Blocks]`
- `[ISPO] —redirectsRewards→ [ADA_Block_Rewards]` · `[Aiken] —compilesTo→ [Untyped_Plutus_Core]`
- `[Charles_Hoskinson] —departedFrom→ [Ethereum]` · `—founded→ [IOHK/IOG]` · `[Djed] —backedByExogenous→ [ADA]`

## 20. Transferable Intelligence (§20) — rule candidates untuk L1 baru
_ref: `docs/Reasoning/AnalogEngine.md`, `docs/Reasoning/Weighting.md`, `docs/Reasoning/Confidence.md`_

- **R1 — SpecRatio_DeFi = MarketCap / TVL:** jika **>50×** selama **>2 tahun** pada platform kontrak-pintar
  aktif → simpulkan **defisit utilitas operasional** (kesulitan bahasa, konkurensi ledger, atau tiadanya
  jembatan likuiditas lintas-rantai). *(Cardano ~66,49× = kasus utama.)*
- **R2 — HFC Metric:** bedakan hard fork konvensional (downtime/pecah) dari **combinator-based zero-downtime**;
  yang punya HFC layak skor kesiapan infrastruktur lebih tinggi.
- **R3 — SSRI (Staking Slashing Risk Index):** konsensus **tanpa slashing** → loyalitas delegasi ritel tinggi →
  pertahanan konsensus stabil; L1 baru dengan liquid-staking-no-slashing layak bobot keamanan lebih tinggi.
- **R4 — Research-vs-Market Timing:** rekayasa formal menaikkan keandalan tetapi menurunkan time-to-market;
  timbang bersama window narasi pasar.
- **Khusus-Cardano (jangan digeneralisasi):** kepastian hukum **Konstitusi on-chain** (nilai bagi institusi);
  **keterbatasan konkurensi EUTXO** (dApp tak bisa mengadopsi mentah logika EVM — wajib off-chain batching).

## 21. Open Questions (§21)
_Research gap — belum tervalidasi, untuk sesi berikutnya._
1. Apakah **Leios** menuntaskan kendala konkurensi UTXO di bawah beban DeFi padat, atau Cardano tetap butuh L2
   non-isomorfik untuk merebut likuiditas? (evidence: MEDIUM)
2. Bagaimana CIP-1694 mencegah **DEX proxy voting** (tim dApp memakai ADA liquidity-provider sebagai suara proxy
   raksasa atas kas perbendaharaan)? (LOW)
3. Saat emisi cadangan menyusut eksponensial, mampukah **biaya transaksi** mendanai ribuan SPO + Treasury tanpa
   emisi baru? (LOW)
4. Dapatkah **Se7en Labs** (portofolio didominasi rekayasa HFC-chain Solana) mengadopsi disiplin **spesifikasi formal**
   ketat untuk memelihara Haskell Node Cardano secara andal? (MEDIUM)
5. Seberapa besar dampak **jeda Catalyst Fund 15 & 16** terhadap retensi builder dApp skala menengah sepanjang 2026? (MEDIUM)

## 22. Evidence Level — kesimpulan kunci (§22)
_ref: `docs/Reasoning/Confidence.md`, `docs/Research/Verification.md`_

| Kesimpulan | Evidence | Alasan |
|---|---|---|
| EUTXO menawarkan determinisme transaksi mutlak off-chain | **HIGH** | Makalah formal IOG + performa Aiken→UPLC |
| Voltaire mengalihkan kendali parameter & Treasury ke komunitas | **HIGH** | On-chain: Chang HF, CIP-1694, Konstitusi diratifikasi DReps |
| ISPO melindungi pokok dana ritel dari penipuan developer | **HIGH** | ADA tak pernah pindah dari dompet non-custodial |
| Leios membawa L1 Cardano >1.000 TPS konsisten | **MEDIUM** | Simulasi + testnet "Musashi Dojo"; keandalan mainnet padat belum terbukti |
| Aiken memicu migrasi massal developer EVM ke Cardano | **LOW** | Efek jaringan likuiditas EVM/Solana masih dominan |

## 23. Related Framework Definitions
- **Ontology:** `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Incentives.md`,
  `Governance.md`, `Security.md`, `Risks.md`, `Technology.md`, `Innovation.md`, `Ecosystem.md`, `Community.md`,
  `Infrastructure.md`, `Metrics.md`, `Revenue.md`, `Adoption.md`
- **Innovation:** `docs/Innovation/FastFollower.md`, `Timing.md`, `CompetitiveMoat.md`, `ProductMarketFit.md`
- **Patterns:** `docs/Patterns/Failure.md`, `Recovery.md`, `Liquidity.md`, `Points.md`, `Mining.md`, `Narrative.md`
- **Lifecycle:** `docs/TokenLifecycle/*` (Byron→Shelley→Goguen→Basho→Voltaire)
- **Market/Valuation:** `docs/MarketBehaviour/UnlockImpact.md`, `Distribution.md`; `docs/Valuation/FairValue.md`, `FDV.md`, `Competitors.md`, `ComparableProjects.md`, `TVL.md`; `docs/Meta/Narratives.md`
- **Reasoning:** `docs/Reasoning/Prediction.md`, `AnalogEngine.md`, `Confidence.md`, `Weighting.md`
- **Success:** `docs/Success/*` · **Schema:** `docs/Schema/KnowledgeGraph.md`, `EntityRelationship.md`, `PatternSchema.md`
- **Cross-project analogs:** `examples/CaseStudies/Ethereum.md` (Hoskinson genealogy — sisi lain Konflik Zug; EUTXO vs account),
  `examples/CaseStudies/Solana.md` & `BNBChain.md` (rival yang menang likuiditas/ritel tetapi lemah desentralisasi),
  `examples/Pioneer/LayerZero.md` (integrasi lintas-rantai 2026), `examples/Pioneer/WorldNetwork-Worldcoin.md` (analog DID/identitas)

## 24. Sources
_Deep Research provenance (Gemini). Laporan sumber mengutip **75 referensi**; sumber primer/kunci di bawah._

- Cardano Roadmap — roadmap.cardano.org — https://roadmap.cardano.org/
- The Extended UTXO Model — Cardano Developer Portal — https://developers.cardano.org/docs/developers/curriculum/fundamentals/core-concepts/eutxo/
- The Extended UTXO Model (paper) — Plutus / Intersect — https://plutus.cardano.intersectmbo.org/resources/eutxo-paper.pdf
- Cardano's Voltaire Governance: Complete Specification and Research Program — arXiv — https://arxiv.org/html/2607.11601v1
- The Evolution of Cardano Governance: A Brief History — Intersect MBO — https://www.intersectmbo.org/news/the-evolution-of-cardano-governance-a-brief-history
- Cardano Completes First Fully On-Chain Governance Hard Fork — KuCoin — https://www.kucoin.com/news/flash/cardano-completes-first-fully-on-chain-governance-hard-fork
- Development phases and eras — Cardano Docs — https://docs.cardano.org/about-cardano/evolution/eras-and-phases
- Cardano — DeFi TVL, Fees, & Revenue — DefiLlama — https://defillama.com/chain/cardano
- Cardano (ADA) Price Today, June 22, 2026: $0.16 at Five-Year Low, Ouroboros Leios Testnet — Pintu News — https://pintu.co.id/en/news/281193-cardano-ada-price-today-june-22-2026
- Cardano Catalyst: When Decentralized Governance Becomes Plutocracy — Medium (Cem Karaca) — https://medium.com/@cem.karaca/cardano-catalyst-when-decentralized-governance-becomes-plutocracy-cb726e21d697
- Cardano Foundation & Project Catalyst F13: Follow Up — Cardano Foundation — https://cardanofoundation.org/blog/project-catalyst-f13-follow-up
- Initial Stake Pool Offering (ISPO) Meaning in Crypto — Tangem — https://tangem.com/en/glossary/initial-stake-pool-offering-ispo/
- Disrupting DeFi: How Aiken Changed the Cardano Landscape In Less Than A Year — Medium (Lenfi) — https://medium.com/@lenfi/disrupting-defi-how-aiken-changed-the-cardano-landscape-in-less-than-a-year-946c113d4636
- Hydra | Cardano Docs — https://docs.cardano.org/developer-resources/scalability-solutions/hydra
- Mithril: powering lightweight access to the Cardano blockchain — IOG — https://www.iog.io/news/mithril-powering-lightweight-access-to-the-cardano-blockchain
- Cardano launches blockchain deployment in Ethiopia with 5M students — AppsAfrica — https://www.appsafrica.com/cardano-launches-blockchain-deployment-in-ethiopia-with-5m-students/
- Ethereum vs Cardano Statistics 2026: TVL, Staking, Devs — CoinLaw — https://coinlaw.io/ethereum-vs-cardano-statistics/
- Cardano (ADA) Live Tokenomics — TokenInsight — https://tokeninsight.com/en/coins/cardano/tokenomics
- Cardano's Missing 1,096 Bitcoin: Hoskinson Explains the $70M BTC Mystery — CCN — https://www.ccn.com/news/crypto/cardano-missing-1096-bitcoin-hoskinson-explains-70m-btc-mystery/
- What did IOHK/EMURGO/CF do with the initial BTC funds raised — Cardano Forum — https://forum.cardano.org/t/what-did-iohk-emurgo-cf-do-with-the-initial-btc-funds-raised/17679
- Cardano Approves First Major Hard Fork Since Voltaire Era (Van Rossem) — The Coin Republic — https://www.thecoinrepublic.com/2026/07/16/cardano-news-cardano-approves-first-major-hard-fork-since-voltaire-era/
- Project Catalyst F13 Proposal Selections — Cardano Foundation — https://cardanofoundation.org/blog/project-catalyst-f13-proposal-selections
- Cardano's Project Catalyst Is Changing Hands — The Pause Forces Builders to Face a Brutal Funding Gap — CryptoSlate — https://cryptoslate.com/cardanos-project-catalyst-is-changing-hands-and-the-pause-is-forcing-builders-to-face-a-brutal-funding-gap/
- Cardano Genesis (config) — cardano.org — https://cardano.org/genesis/

_(Full bibliography retained in the original Deep Research reports — no-table `.docx` rebuild (≈40 sources) +
prior `.pdf` (75 sources) — both archived at `doc_backup/deep/Cardano_2026-07_gemini.{docx,md,pdf}`.)_
