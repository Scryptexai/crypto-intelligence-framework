# Ethereum — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Laporan Intelijen Crypto: Rekonstruksi Historis, Tokenomika, dan Evolusi
Sistemik Ethereum"* (no-table `.docx` rebuild) — merged with the prior comprehensive report (`.pdf`) that contributed
the Konflik-Zug genealogy, DAO/Parity governance-maturation, Krisis-Kas 2014, and 5-episode price-causality depth.
**Pipeline position:** Applications layer — the richest anchor artifact, structured against the full `docs/`
ontology and used as a primary analog for reasoning.
**Raw source archived:** `doc_backup/deep/Ethereum_2026-07_gemini.docx` (+ `.md` text extraction) — **rebuilt from the
higher-fidelity no-table `.docx`; prior `.pdf` retained** at `doc_backup/deep/Ethereum_2026-07_gemini.pdf`.
**Input note:** authored in the CIF no-table contract; extracted via `tools/extract.py` (0 tables, 0 chips,
23 sections); fidelity checked with `tools/reconcile.py`.

> Knowledge artifact (real curated data), not a documentation container. This is a **deep dossier**: it
> preserves *causality* (why events happened), which is the raw material for prediction. Conforms to
> `templates/CaseStudyTemplate.md`.

---

## 1. Identity
_ref: `docs/Ontology/Identity.md`_

- **Project:** Ethereum (ETH)
- **Category:** Smart-Contract Platform / Layer 1 — "World Computer"
- **Era:** 2013 (whitepaper) – sekarang (2026)
- **Innovation archetype:** First Mover pada platform kontrak pintar umum; Fast Follower pada konsensus
  (PoS) dan modular scaling.

## 2. Classification
_ref: `docs/Ontology/Classification.md`, `docs/Taxonomy/Sectors.md`, `docs/Taxonomy/Technologies.md`_

Layer 1 · General-purpose smart-contract platform · EVM · transisi PoW → PoS · roadmap modular (rollup-centric).

## 3. Pre-Conditions — Kegagalan Skrip Bitcoin (2009–2013)
_Konteks: mengapa Ethereum harus ada._

Lanskap 2009–2013 didominasi Bitcoin. Keterbatasan fundamental Bitcoin mendorong lahirnya Ethereum:
- **Script non-Turing-complete** (sengaja, oleh Satoshi, untuk mencegah DoS via loop tak terbatas / Halting Problem).
- **Model UTXO bersifat *stateless*** — tak bisa menyimpan/memperbarui status aplikasi dinamis.
- Upaya di atas Bitcoin (**Colored Coins**, **Mastercoin**, 2013) terhambat kekakuan skrip; altcoin independen
  (Lisk, BitShares, NXT) menghadapi **fragmentasi keamanan** (harus bootstrap miner set sendiri, rentan 51%).

Kesenjangan ini menuntut platform terpadu yang memisahkan lapisan konsensus/keamanan dari lapisan aplikasi,
dengan bahasa Turing-complete di tingkat protokol.

## 4. Visi & Team — Genealogi Pendirian
_ref: `docs/Ontology/Team.md`, `docs/Ontology/Governance.md`_

**Vitalik Buterin** (co-founder Bitcoin Magazine, 2012) merilis draf whitepaper pada **November 2013** —
visi **"World Computer"**: platform komputasi global terdesentralisasi via **Ethereum Virtual Machine (EVM)**,
mesin transisi status yang mengeksekusi bytecode Turing-complete.

**Delapan pendiri** (diresmikan di Zug, Swiss, 7 Juni 2014):
- **Vitalik Buterin** — pengonsep, whitepaper, pengarah transisi PoS.
- **Gavin Wood** — CTO pertama; Yellow Paper (spesifikasi EVM), bahasa Solidity, Whisper, DEVp2p.
- **Joseph Lubin** — pendanaan awal; mendirikan ConsenSys (MetaMask, Infura).
- **Charles Hoskinson** — CEO pertama EF; merancang struktur hukum Swiss.
- **Anthony Di Iorio** — modal awal operasional Toronto/Swiss.
- **Jeffrey Wilcke** — klien pertama dalam Go (**Geth**), kini klien eksekusi dominan.
- **Mihai Alisie** — rekan Bitcoin Magazine; operasional & yayasan Swiss.
- **Amir Chetrit** — rekan Colored Coins; koordinasi bisnis awal.

Penasihat/kontributor: Dmitry Buterin, Taylor Gerring, Stephan Tual, **Vlad Zamfir** (peneliti PoS/Casper).

### Konflik Zug & Perpecahan Ideologis (Juni 2014) — *causal event*
Dua faksi: **for-profit** (Hoskinson, Di Iorio — VC, produk proprietary) vs **non-profit** (Buterin —
platform netral terdesentralisasi). Buterin memenangkan arah non-profit; Ethereum bernaung di bawah
**Ethereum Foundation (Stiftung Ethereum)**, Swiss. Akibatnya:
- Hoskinson keluar → mendirikan **Cardano**.
- Amir Chetrit dikeluarkan dari inti.
- Di Iorio mundur (Jaxx; keluar kripto 2021).
- **Gavin Wood** keluar 2016 → **Parity Technologies** & **Polkadot/Web3 Foundation**.
- Lubin → **ConsenSys** sebagai mesin komersial tanpa merusak status nirlaba EF.

**Pelajaran kausal:** struktur nirlaba menjaga netralitas kredibel Ethereum, tetapi **mengorbankan kecepatan
eksekusi** karena bergantung pada konsensus sosial yang berliku — tema yang berulang sepanjang sejarahnya.

## 5. Funding / TGE — Crowdsale & Krisis Kas
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Tokenomics.md`_

Crowdsale **22 Juli – 2 September 2014** (pra-TGE).

**Tabel — Alokasi Genesis:**
| Parameter | Nilai |
|---|---|
| Total dana terkumpul | 31.529–31.591 BTC (~$18,4 juta saat itu) |
| Harga awal | 1 BTC : 2.000 ETH (14 hari pertama) ≈ $0,311/ETH |
| Harga akhir | menurun linier hingga 1 BTC : 1.337 ETH |
| Terjual (presale) | 60.102.216 ETH (~83,5% pasokan genesis) |
| Dana abadi (Foundation) | 6.000.000 ETH (8,3%) |
| Kontributor awal | 6.009.990,50 ETH (8,3%) |
| **Total pasokan genesis** | **72.009.990,50 ETH** |

**Hibah strategis:** **Peter Thiel Fellowship $100.000** (Jun 2014) ke Vitalik untuk pengembangan platform dasar.

### Krisis Kas 2014–2015 — *causal event*
EF menyimpan seluruh dana dalam **BTC**. Bear market (runtuhnya Mt. Gox) menjatuhkan BTC >80% → runway EF
menipis, terjadi PHK & potong gaji. **Kausalitas jangka panjang:** trauma ini menjelaskan mengapa di tiap
puncak bull (2017, 2021) EF rutin **menjual OTC puluhan ribu ETH** ke fiat — tindakan defensif (sering
dikritik ritel sebagai "menekan harga"). → lihat `docs/Ontology/Risks.md` (treasury risk).

### Pivot Perbendaharaan ke Native Yield (2025–2026) — *causal evolution*
Reformasi kas: alih-alih **menjual spot** (yang dulu menekan harga), EF kini **mendelegasikan ETH ke staking +
DeFi lending terkurasi** untuk membiayai operasi dari *native yield* — menghentikan trauma "EF menjual di puncak":
- **Feb 2025:** **45.000 ETH** ke **Spark, Aave Prime, Aave Core, Compound** (kredit DeFi).
- **Okt 2025:** **2.400 ETH + $6 juta** stablecoin ke **Morpho** (likuiditas).
- **Feb 2026:** **70.000 ETH** ke kontrak staking institusional terdistribusi (deposit tahap-1 **2.016 ETH**, 24 Feb).
- **8 Apr 2026:** penjualan kas operasional **terakhir** 5.000 ETH → **$11,1 juta** (~$2.220,76/ETH).

*Pelajaran kausal:* treasury besar bergeser dari **likuidasi spot** ke **yield-bearing self-funding** — sinyal
kematangan + penghapusan tekanan-jual reputasional. → `examples/CaseStudies/Aave.md`, `docs/Ontology/Revenue.md`.

## 6. Technology & Architecture — Timeline Hard Fork
_ref: `docs/Ontology/Technology.md`, `docs/TokenLifecycle/*`_

| Upgrade | Tanggal | Fokus inovasi |
|---|---|---|
| Frontier | 30 Jul 2015 | Mainnet pertama, PoW Ethash (blok #0) |
| Homestead | 14 Mar 2016 | Kematangan protokol, keamanan EVM |
| Byzantium | 16 Okt 2017 | Privasi via zk-SNARKs |
| Constantinople | 28 Feb 2019 | Efisiensi gas; CREATE2 |
| Muir Glacier | 2 Jan 2020 | Penundaan difficulty bomb |
| Beacon Chain | 1 Des 2020 | Rantai PoS paralel |
| London | 5 Agu 2021 | **EIP-1559** (restrukturisasi fee market + burn) |
| The Merge | 15 Sep 2022 | Transisi total ke **PoS** (konsumsi energi **−99,9%**) |
| Shapella | 12 Apr 2023 | Pembukaan withdrawal staking |
| Dencun | 13 Mar 2024 | **Proto-Danksharding (EIP-4844)**, blob space |
| Pectra | 7 Mei 2025 | **EIP-7251 (MaxEB)** 32→**2.048 ETH** (konsolidasi validator); **EIP-7702** (EOA→smart-wallet sementara); **EIP-2537** (precompile BLS12-381); **EIP-7610** (cegah overwrite akun, persiapan Verkle) |
| Fusaka | 3 Des 2025 | **EIP-7594 (PeerDAS)** data-availability sampling; **EIP-7691** blob per-blok target 6→**16** (maks 24); gas limit L1 45M→**150M** |
| Glamsterdam | ~pertengahan 2026 | **ePBS** (Enshrined Proposer-Builder Separation); eksekusi paralel L1; native ZK proving |

**Keluarga standar ERC (moat komposabilitas):** **ERC-20** (fungible, Nov 2015, Vogelsteller/Buterin) · **ERC-721**
(NFT, Jan 2018) · **ERC-1155** (multi-token, Enjin, −60% biaya batch) · **ERC-2612** (permit EIP-712) · **ERC-3009**
(transfer-with-authorization, dipakai USDC) · **ERC-4337** (account abstraction tanpa ubah konsensus) · **ERC-4626**
(tokenized vault, standar yield DeFi) · **ERC-7683** (cross-chain intent, Across/Uniswap) · **ERC-7802** (crosschain
mint/burn native). *Standardisasi bottom-up (ERC/EIP) = inovasi tanpa intervensi tim inti (§14 rule).*

### Paradoks Skalabilitas: Modular vs Monolitik
Rencana awal **Execution Sharding** (64 shard) ditinggalkan karena kompleksitas sinkronisasi lintas-shard.
**2020: "A Rollup-Centric Ethereum Roadmap"** (Buterin) → geser eksekusi harian ke **L2 rollups** (Arbitrum,
Optimism, Base); L1 didefinisikan ulang sebagai lapisan **settlement + data availability**. Puncaknya
**Dencun (EIP-4844)** memperkenalkan **blob** (ruang data murah terpisah dari gas eksekusi). Kontras:
**Solana** memilih **monolitik** (Sealevel parallel execution + Proof of History) demi menghindari
fragmentasi likuiditas antar-L2. → `docs/Taxonomy/Technologies.md`, `docs/Valuation/Competitors.md`.

## 7. Governance Crises — Kode Gagal, Konsensus Sosial Menang
_ref: `docs/Ontology/Governance.md`, `docs/Ontology/Security.md`, `docs/Ontology/Risks.md`, `docs/Patterns/Failure.md`, `docs/Patterns/Recovery.md`_

### The DAO Hack (Juni 2016)
The DAO (Christoph Jentzsch / Slock.it, Apr 2016) mengumpulkan **11,5% pasokan ETH** (~$150 juta). 17 Juni
2016: eksploitasi **reentrancy** (pelanggaran pola *Checks-Effects-Interactions* — transfer dana sebelum
memperbarui saldo). Penyerang menguras **3,6 juta ETH** ke Child DAO. Komunitas terpecah:
1. **Imutabilitas ("Code is Law")** vs 2. **Intervensi pragmatis** (membiarkan peretas menguasai >10% pasokan
akan mematikan Ethereum di fase awal). Coin vote + hashrate vote → mayoritas mendukung pemulihan. **20 Juli
2016**, hard fork blok #1.920.000 memindahkan dana ke kontrak pemulihan. Faksi minoritas melanjutkan rantai
asli → **Ethereum Classic (ETC)**. *Pelajaran: konsensus sosial > aturan protokol.*

### Parity Multi-Sig Freeze (November 2017)
6 Nov 2017: "devops199" tak sengaja memicu `selfdestruct` pada **kontrak library master** Parity yang tak
terinisialisasi (dipakai via `delegatecall` oleh banyak dompet). **513.774 ETH** ($150–300 juta) **membeku**.
Proposal **EIP-999** (Gavin Wood/Parity) untuk memulihkan **ditolak** komunitas karena **fork fatigue** &
penolakan **moral hazard**. *Pelajaran: 2016 komunitas mau fork darurat; 2017 memilih imutabilitas di atas
kerugian pengguna — pematangan norma tata kelola.*

## 8. Ecosystem — DeFi, Staking, Restaking, RWA
_ref: `docs/Ontology/Ecosystem.md`, `docs/Ontology/Adoption.md`, `docs/Ontology/Metrics.md`, `docs/Valuation/TVL.md`_

**Tabel — Evolusi TVL L1:**
| Tahun | TVL L1 | Narasi dominan |
|---|---|---|
| 2020 | $675 juta | Kelahiran DeFi, yield farming, AMM (Uniswap, Aave) |
| 2021 (peak) | $180–255 miliar | Puncak spekulasi DeFi; gas ratusan dolar |
| 2023 | $40–50 miliar | Konsolidasi bear; transisi PoS |
| 2025/2026 | $55–56 miliar | Dominasi restaking; RWA; L2 memproses ritel harian |

- **Liquid Staking:** solo staking butuh 32 ETH → **Lido** (stETH) tumbuh pesat. Risiko **sentralisasi**
  (Lido >⅓ staking ETH) → mitigasi **DVT** (Obol, SSV) memecah kunci validator. → cross-link
  `examples/Pioneer/Lido.md`.
- **Restaking:** ledakan **EigenLayer** (2024–2025) — restaking ETH/LST untuk mengamankan AVS; LRT (eETH,
  ezETH via Ether.fi/Renzo/KelpDAO). Risiko sistemik **collateral looping** / cascading slashing. → cross-link
  `examples/CaseStudies/EigenLayer.md`.
- **RWA:** dominasi institusional — **BlackRock BUIDL** (Mar 2024, ERC-20, Securitize + BNY Mellon, SEC),
  AUM $2,4–2,9 miliar (2026); komposabilitas instan dengan USDC. → `docs/Ontology/Revenue.md`.

### Lanskap L2 (30 Mei 2026) — TVS kolektif **$48,78 miliar** di **118 rantai**
| L2 | TVS | Pangsa | Karakter |
|---|---|---|---|
| **Arbitrum One** | $20,5 mrd | **42,02%** | kedalaman TVS institusional |
| **Base** (Coinbase) | $11,9 mrd | 24,40% | volume ritel harian tertinggi |
| **Polygon PoS** | $4,49 mrd | 9,20% | — |
| **Hyperliquid** | $3,46 mrd | 7,09% | perp-DEX appchain |
| **OP Mainnet** | $1,5 mrd | 3,07% | OP Stack asli |
| **Mantle** | $1,41 mrd | 2,90% | — |
| **Starknet** | $525 juta | 1,08% | ZK-rollup |

**Aktivitas (29 Mei 2026):** L1 **2,32 juta tx/hari** @ 2,52 Mgas/s (peran settlement) vs **L2 gabungan 27,24 juta
tx/hari** @ 78,68 Mgas/s — bukti pergeseran eksekusi ritel ke L2. **L2 incentive war:** World Chain (gas gratis via
World ID biometrik), Mode (80% sequencer-fee-share ke dev), Blast (auto-yield native → Lido/MakerDAO). → `examples/Pioneer/Optimism.md`, `examples/Pioneer/WorldNetwork-Worldcoin.md`.

### Metrik staking (Jul 2026)
**~40,8 juta ETH ter-stake** (**33,49%** pasokan; *alt 39,7 juta / ~32%*); **883.724 validator** (*alt 1,24 juta —
beda indeks validator non-aktif, evidence LOW*); **entry queue 2.499.792 ETH** (tunggu **43 hari 10 jam**); **APR 2,64%**
base (all-in **3,1–3,3%** dgn MEV-Boost). **EIP-7251 compounding (Mei 2026):** 12.431 node kelola ~10,3 juta ETH (>26%
jaminan). **Liquid staking:** $25,6 mrd / 14,4 juta ETH di **33 protokol**; **restaking >$15 mrd** (EigenLayer). → `examples/CaseStudies/EigenLayer.md`, `examples/Pioneer/Lido.md`.

## 9. Competitor Landscape (lintas siklus)
_ref: `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

| Fase | Kompetitor | Karakter | Dampak ke Ethereum |
|---|---|---|---|
| 1 (2015–17) | Lisk, BitShares, NXT | app-specific, PoS awal | ETH unggul via ekosistem EVM |
| 2 (2017–20) | EOS, NEO, Cardano | DPoS, TPS tinggi | Urgensi migrasi ke PoS |
| 3 (2020–24) | Solana, Avalanche, BNB | throughput tinggi, gas murah | Peta jalan bergeser L1-sharding → L2 rollup |
| 4 (2024–26) | Solana (monolitik) vs L2s | 1 lapisan vs modular | Tekanan turunkan biaya DA di L1 |

**Dominasi L1 terukur (Mar 2026):** **TVL** ETH >$56 mrd vs Solana $6,9 mrd / BNB $6 mrd / TRON $4,11 mrd / Ripple
$49 juta · **stablecoin** ETH **$159 mrd** vs Solana $15 mrd / BNB $14 mrd · **RWA** ETH **$15,2 mrd** vs BNB $3 mrd /
Solana $2,1 mrd. → ETH menang telak di jaminan nilai institusional meski kalah kecepatan/biaya di L1.

## 10. Tokenomics & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Reasoning/Prediction.md`, `docs/Ontology/Tokenomics.md`_

**Tabel — Metrik Harga ETH:**
| Metrik | Nilai | Kondisi |
|---|---|---|
| Harga ICO | $0,311 | Jul–Sep 2014 |
| **ATL** | **$0,42** *(alt $0,43)* | 21 Okt 2015 |
| Bubble #1 | ~$1.400 | Jan 2018 (mania ICO) |
| **ATH** | **$4.946,05** *(alt $4.953,73)* | 24 Agu 2025 (arus masuk ETF spot) |
| Drawdown 2026 | $1.780–1.870 (−~62% dari ATH) | Q1–Q2 2026 (rotasi makro pasca-halving BTC) |
| Pasokan maks | tak terbatas (infinite) | ditentukan aturan emisi |
| Inflasi bersih (mid-2026) | **~0,83%/th** (Q1 2026 ~0,23%) | emisi staking > burn EIP-1559 pasca-Dencun |

**Akumulasi perbendaharaan (2026) — "reserve asset" institusional:** *entitas:* **Bitmine 5,3 juta ETH** (~$11 mrd;
4,7 juta di-stake) · **BlackRock iShares 3 juta** (~$6,5 mrd) · Coinbase Custody 4,2 juta · Binance 4 juta · Upbit
1,7 juta. *individu:* **Rain Lohmus 250rb** (dompet terkunci, kunci hilang) · **Joseph Lubin 243rb** · **Vitalik 224rb**
(~$475 juta, akses penuh) · Jeffrey Wilcke 116rb · James Fickel 49rb. Likuiditas bebas di CEX **anjlok ke ~16 juta ETH**
(low multi-tahun) → memperkuat tesis **undervalued** on-chain. → `docs/MarketBehaviour/Distribution.md`, `docs/Valuation/FairValue.md`.

**Kausalitas 5 episode harga:**
1. **ICO Mania (2017):** ETH ~$1.400 (Jan 2018) — setiap ICO ERC-20 menuntut ETH → lonjakan permintaan.
2. **Bear 2018:** <$80 akhir 2018 — tim ICO melikuidasi ETH untuk operasional + penertiban SEC.
3. **DeFi & NFT (2020–21):** ATH $4.800+ (Nov 2021) — likuiditas global pasca-pandemi + yield farming + NFT.
4. **Dencun (2024–26) — Hilangnya Deflasi:** sukses teknis (gas L2 turun >90%) **justru** menurunkan
   pendapatan L1. Emisi dipangkas **~88%** pasca-Merge (pra-Merge ~4%/th, ~**13.000 ETH/hari** → pasca ~0,5%/th,
   ~1.700–2.000 ETH/hari); **EIP-1559 burn kumulatif ~4,3–4,6 juta ETH** sejak Agu 2021 (variasi tracker ~1 juta ETH,
   evidence LOW). Karena burn sebanding kemacetan L1, migrasi tx ke blob menurunkan burn **di bawah emisi** → ETH kembali
   **net-inflasi** (~0,83%/th); hilangnya narasi "Ultra Sound Money" memicu underperformance vs BTC/SOL. *Contoh utama:
   sukses teknis → dampak tokenomik negatif tak terduga.*
5. **Yen Carry Unwind (awal 2026):** pengetatan BOJ → penutupan carry trade Yen → liquidity squeeze/derisking
   → ETH turun dari >$3.000 ke ~$1.500–1.800 (pertengahan 2026). *Contoh: korelasi makro global.* →
   `docs/MarketBehaviour/MarketCorrelation.md`.

## 11. Current State (2025–2026)
_ref: `docs/Ontology/Metrics.md`, `docs/Ontology/Team.md`, `docs/Ontology/Risks.md`_

Fundamental kuat: rekor volume transaksi harian (L1+L2), **dominasi stablecoin ~$159 miliar** (>½ pasokan global;
$175,72 mrd stablecoin di L1 vs $18,22 mrd di L2 per 29 Mei 2026), **RWA >$15,2 miliar**, DeFi TVL L1 >$56 miliar, ETF/ETP
~$14 miliar. Adopsi institusi memuncak: **BlackRock iShares Staked ETH Trust (ETHB)** rilis **12 Mar 2026** ($155 juta
arus masuk hari-1) — produk ETF pertama berdividen staking native. **~11.000 pengembang aktif** EVM (Mei 2026).

Namun **krisis koordinasi EF:** restrukturisasi awal 2025 mendelegasikan riset inti ke luar yayasan → hengkang
peneliti senior (Carl Beek, Julian Ma, koordinator hard fork **Tim Beiko**) pertengahan 2026. Keragaman klien
(Geth, Nethermind, Besu) menjaga operasional, tetapi hilangnya penengah mempersulit koordinasi upgrade
(Glamsterdam, Hegota).

## 12. POV Success-Matrix (§15)
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`, `docs/Reasoning/Confidence.md`_

Success is **not binary** — verdict per point-of-view, each with an evidence level (see
`docs/Protocol/Deep-Research-Brief.md`). Ethereum = keberhasilan mutlak di **infrastruktur & standar industri**
(EVM = "OS" Web3), tetapi hasilnya berbeda tergantung POV:

| POV | Verdict | Alasan | Evidence |
|-----|---------|--------|----------|
| **Founder** | ✅ Sukses | Misi platform netral tercapai; tapi tata kelola desentralisasi membatasi kendali arah cepat | HIGH |
| **VC** | ✅ Sukses | Likuiditas pasar terdalam; fondasi portofolio Web3 | HIGH |
| **Retail** | ⚠️ Campuran | Native yield via staking, tapi tesis kelangkaan runtuh pasca-Dencun → underperform vs BTC/SOL | MEDIUM |
| **Community** | ✅ Sukses | Menang ideologi (desentralisasi, tolak kompromi keamanan); harga = fragmentasi likuiditas & UX | HIGH |
| **Developer** | ✅ Sukses | Ekosistem paling matang, dokumentasi terlengkap, keamanan ekonomi terbesar | HIGH |
| **Institution** | ✅ Sukses | Dominasi RWA (BUIDL BlackRock), stablecoin ~$160 miliar, komposabilitas TradFi↔DeFi | HIGH |
| **Validator** | ⚠️ Campuran | Native yield PoS, tapi sentralisasi Lido & risiko cascading restaking menekan solo-validator | MEDIUM |
| **Builder (L2/AVS)** | ✅ Sukses | OP Stack/rollup + restaking membuka ruang bangun baru; tapi fragmentasi likuiditas | MEDIUM–HIGH |

**Takeaway:** proyek yang sama bisa "menang" di infrastruktur/institusi namun "seri" di retail/validator —
inilah kenapa verdict harus per-POV, bukan satu label.

## 13. Knowledge Extraction — Patterns & Lessons (§18–19)
_ref: `docs/Patterns/*`, `docs/Reasoning/*` — bahan analog untuk prediksi proyek lain._

1. **Konsensus sosial menimpa "Code is Law"** saat krisis sistemik (The DAO). → `Patterns/Recovery.md`
2. **Norma imutabilitas mengeras seiring waktu** (EIP-999 ditolak). → `Patterns/Failure.md`
3. **Kas volatil tunggal = risiko** (trauma 2014 → penjualan OTC defensif). → `Ontology/Risks.md`
4. **Sukses teknis dapat merusak tokenomics** (Dencun → net-inflasi). → `Reasoning/Prediction.md`
5. **First Mover + ekosistem/standar (EVM) = moat terkuat**, mengalahkan pesaing "lebih cepat". →
   `Innovation/CompetitiveMoat.md`
6. **Sentralisasi efisiensi-modal** (Lido) memicu mitigasi terdistribusi (DVT). → `Patterns/NetworkEffect.md`
7. **Aset kripto makin terkorelasi makro global** (Yen carry). → `MarketBehaviour/MarketCorrelation.md`
8. **Modular L2 Migration → L1 Burn Dampening** *(crown tokenomics pattern)* — blob (EIP-4844) turunkan biaya DA L2 →
   migrasi tx ritel keluar L1 → kepadatan L1 mereda → burn EIP-1559 anjlok < emisi staking → pasokan balik ke
   inflasi lunak (~0,83%/th). *Sukses skalabilitas menggerus mekanisme value-accrual.* → `docs/Reasoning/Prediction.md`.
9. **Open Institutional Staking Accumulation Loop** — persetujuan ETF spot → hapus risiko klasifikasi hukum → ETF
   dividen-staking native → kustodian tarik ETH dari spot → kunci ke Beacon Chain → float bebas CEX anjlok → kepercayaan
   operator institusi naik. *Regulasi → penyerapan pasokan struktural.* → `docs/Patterns/Flywheel.md`, `docs/Success/Adoption.md`.

## 14. Transferable Intelligence (§20)
_ref: `docs/Reasoning/*` — rule candidates untuk mengevaluasi project baru._

Rule kandidat (berlaku umum, layak jadi aturan reasoning):
- **R1:** Platform "First Mover + standar developer" (spt EVM) > pesaing "lebih cepat/murah" dalam retensi
  jangka panjang. Cek: apakah project menciptakan standar yang diadopsi pesaing?
- **R2:** Sukses teknis yang menurunkan pendapatan/burn protokol dapat merusak tesis token. Cek: apakah
  upgrade menggeser aktivitas ke luar mekanisme value-accrual?
- **R3:** Inovasi efisiensi-modal akan mengonsentrasikan sumber daya → nilai proyek harus dinilai bersama
  mitigasi desentralisasinya (ada/tidak).
- **R4:** Treasury aset-tunggal volatil = risiko kelangsungan; diversifikasi + **native-yield self-funding** (bukan
  likuidasi spot) = sinyal kematangan. *(EF pivot 2025–26.)*
- **R5 — Developer Retention Law:** nilai jangka-panjang L1 ∝ retensi pengembang aktif (**>5.000**); gagal membangun
  komunitas dev mandiri dalam **3 tahun** pasca-mainnet → proyeksi kematian sistemik. *(ETH ~11.000 dev.)*
- **R6 — Security Budget Dominance:** L1 smart-contract wajib pimpin pangsa **stablecoin >40% global** untuk bertahan
  sebagai lapisan penyelesaian utama; gagal → rotasi jaminan ke pesaing.
- **R7 — EIP-1559 Burn Sensitivity (khusus-EVM):** deflasi hanya bekerja bila gas L1 di atas ambang kemacetan; ukur
  **penetrasi tx L2 dinamis**, bukan volume total — sukses L2 dapat mematikan tesis deflasi.

Khusus-Ethereum (jangan digeneralisasi): skala efek jaringan EVM, momen historis 2014–2015, dan status
"reserve asset" DeFi — sulit direplikasi project baru.

## 15. Open Questions (§21)
_Research gap — belum tervalidasi, untuk sesi berikutnya._
- Apakah net-inflasi pasca-Dencun permanen atau pulih saat aktivitas L1 naik? (evidence: LOW)
- Dampak jangka panjang krisis koordinasi Ethereum Foundation terhadap kecepatan rilis upgrade? (LOW)
- Seberapa besar risiko sistemik restaking (cascading slashing) benar-benar terwujud vs teoretis? (MEDIUM)

## 16. Evidence Level — kesimpulan kunci (§22)
| Kesimpulan | Evidence | Alasan |
|---|---|---|
| EVM jadi standar industri | HIGH | Kompetitor EVM-compatible, 1jt+ developer |
| Konsensus sosial > kode saat krisis | HIGH | Dua preseden terdokumentasi (The DAO, EIP-999) |
| Dencun → net-inflasi | HIGH | Mekanisme EIP-1559 + data burn/emisi |
| Underperformance akibat "hilang Ultra Sound Money" | MEDIUM | Multi-faktor (termasuk makro Yen) |
| Risiko cascading restaking | MEDIUM | Sebagian besar masih teoretis/model |

## 17. Related Framework Definitions
- Ontology: `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Governance.md`,
  `Security.md`, `Risks.md`, `Technology.md`, `Ecosystem.md`, `Metrics.md`, `Revenue.md`
- Patterns: `docs/Patterns/Failure.md`, `Recovery.md`, `NetworkEffect.md`
- Lifecycle: `docs/TokenLifecycle/*` (Frontier→Merge→Dencun→…)
- Market: `docs/MarketBehaviour/MarketCorrelation.md`, `docs/Valuation/Competitors.md`, `docs/Valuation/TVL.md`
- Success: `docs/Success/*`
- Cross-project: `examples/Pioneer/Lido.md`, `examples/CaseStudies/EigenLayer.md`, `examples/Pioneer/Uniswap.md`,
  `examples/CaseStudies/Aave.md`, `examples/Pioneer/Optimism.md`, `examples/CaseStudies/Celestia.md`

## 18. Sources
_Deep Research provenance. The source report cites **81 references**; key primary sources below._

- History of Ethereum — ethereum.org — https://ethereum.org/ethereum-history-founder-and-ownership/
- Who Founded Ethereum — Ledger Academy — https://www.ledger.com/academy/topics/blockchain/ethereum-founder
- Ethereum — Wikipedia — https://en.wikipedia.org/wiki/Ethereum
- Launching the Ether Sale — Ethereum Foundation Blog — https://blog.ethereum.org/2014/07/22/launching-the-ether-sale
- Ethereum roadmap — ethereum.org — https://ethereum.org/roadmap/
- The DAO Hack — Cybereason — https://www.cybereason.com/blog/malicious-life-podcast-the-ethereum-dao-hack
- What is a Re-Entrancy Attack? — Quantstamp — https://quantstamp.com/blog/what-is-a-re-entrancy-attack
- The Evolving Debate Over EIP-999 — Bitcoin Magazine — https://bitcoinmagazine.com/business/evolving-debate-over-eip-999-can-or-should-trapped-ether-be-freed
- Ethereum's Pectra Upgrade — Crypto.com — https://crypto.com/en/university/ethereum-pectra-prague-electra-upgrade
- EIP-1559 Explained — Eco — https://eco.com/support/en/articles/14796247-eip-1559-explained-fee-market-reform
- Breakdown of Ethereum Supply Distribution — Galaxy — https://www.galaxy.com/insights/research/breakdown-of-ethereum-supply-distribution-since-genesis
- Mitigating Challenges in Ethereum PoS (EigenLayer & Lido) — arXiv — https://arxiv.org/html/2410.23422v2
- Financial Dynamics and Interconnected Risk of Liquid Restaking — arXiv — https://arxiv.org/html/2604.03274v1
- Ethereum's tokenized RWA market tops $17B — The Block — https://www.theblock.co/post/390130/ethereum-tokenized-rwa-market-jump
- Eight Ethereum Foundation Researchers Have Quit in 2026 — Phemex — https://phemex.com/blogs/ethereum-foundation-researchers-quitting-2026
- Ether Total Supply — Etherscan — https://etherscan.io/stat/supply
- ETH price — CoinGecko — https://www.coingecko.com/en/coins/ethereum
- The Eight Kings: The Split of Ethereum Founders — ChainCatcher — https://www.chaincatcher.com/en/article/2194242
- What is the Ethereum Pectra Upgrade — CoinGecko Learn — https://www.coingecko.com/learn/what-is-ethereum-pectra-upgrade
- L2BEAT — TVS Metrics & Scaling Activity — https://l2beat.com/scaling/tvs
- World Chain vs Mode vs Blast — Newer L2s Compared — Eco — https://eco.com/support/en/articles/14798713-world-chain-vs-mode-vs-blast-2026-newer-l2s-compared
- Ethereum Three-Body Problem (supply/fee/ETF) — Phemex — https://phemex.com/blogs/ethereum-three-body-problem-supply-fee-etf-march-19

_(Full bibliography retained in the original Deep Research reports — no-table `.docx` rebuild (≈40 sources) + prior
`.pdf` (81 sources) — both archived at `doc_backup/deep/Ethereum_2026-07_gemini.{docx,md,pdf}`.)_
