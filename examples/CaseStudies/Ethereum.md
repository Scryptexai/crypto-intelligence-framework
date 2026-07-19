# Ethereum — Deep Case Study

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (Gemini) — *"Laporan Riset Historis dan Analisis Arsitektural Protokol Ethereum:
Struktur Kausalitas Tata Kelola, Evolusi Tokenomics, dan Dinamika Komputer Dunia (2013–2026)"*.
**Pipeline position:** Applications layer — the richest anchor artifact, structured against the full `docs/`
ontology and used as a primary analog for reasoning.

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

### Krisis Kas 2014–2015 — *causal event*
EF menyimpan seluruh dana dalam **BTC**. Bear market (runtuhnya Mt. Gox) menjatuhkan BTC >80% → runway EF
menipis, terjadi PHK & potong gaji. **Kausalitas jangka panjang:** trauma ini menjelaskan mengapa di tiap
puncak bull (2017, 2021) EF rutin **menjual OTC puluhan ribu ETH** ke fiat — tindakan defensif (sering
dikritik ritel sebagai "menekan harga"). → lihat `docs/Ontology/Risks.md` (treasury risk).

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
| The Merge | 15 Sep 2022 | Transisi total ke **PoS** |
| Shapella | 12 Apr 2023 | Pembukaan withdrawal staking |
| Dencun | 13 Mar 2024 | **Proto-Danksharding (EIP-4844)**, blob space |
| Pectra | 7 Mei 2025 | EIP-7251 (naik batas stake); EIP-7702 (account abstraction) |
| Fusaka | 3 Des 2025 | PeerDAS, ePBS |
| Glamsterdam | ~pertengahan 2026 | Eksekusi paralel; gas limit blok 200M (rencana) |

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
  `examples/Pioneer/EigenLayer.md`.
- **RWA:** dominasi institusional — **BlackRock BUIDL** (Mar 2024, ERC-20, Securitize + BNY Mellon, SEC),
  AUM $2,4–2,9 miliar (2026); komposabilitas instan dengan USDC. → `docs/Ontology/Revenue.md`.

## 9. Competitor Landscape (lintas siklus)
_ref: `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

| Fase | Kompetitor | Karakter | Dampak ke Ethereum |
|---|---|---|---|
| 1 (2015–17) | Lisk, BitShares, NXT | app-specific, PoS awal | ETH unggul via ekosistem EVM |
| 2 (2017–20) | EOS, NEO, Cardano | DPoS, TPS tinggi | Urgensi migrasi ke PoS |
| 3 (2020–24) | Solana, Avalanche, BNB | throughput tinggi, gas murah | Peta jalan bergeser L1-sharding → L2 rollup |
| 4 (2024–26) | Solana (monolitik) vs L2s | 1 lapisan vs modular | Tekanan turunkan biaya DA di L1 |

## 10. Tokenomics & Price Causality
_ref: `docs/MarketBehaviour/*`, `docs/Reasoning/Prediction.md`, `docs/Ontology/Tokenomics.md`_

**Tabel — Metrik Harga ETH:**
| Metrik | Nilai | Kondisi |
|---|---|---|
| Harga ICO | $0,311 | Jul–Sep 2014 |
| ATL | $0,42–0,43 | Okt 2015 |
| ATH | $4.891–4.955 | Nov 2021 & Agu 2025 |
| Pasokan maks | tak terbatas (infinite) | ditentukan aturan emisi |
| Pasokan beredar (2026) | ~120,7 juta ETH | inflasi bersih ~0,18%/th |

**Kausalitas 5 episode harga:**
1. **ICO Mania (2017):** ETH ~$1.400 (Jan 2018) — setiap ICO ERC-20 menuntut ETH → lonjakan permintaan.
2. **Bear 2018:** <$80 akhir 2018 — tim ICO melikuidasi ETH untuk operasional + penertiban SEC.
3. **DeFi & NFT (2020–21):** ATH $4.800+ (Nov 2021) — likuiditas global pasca-pandemi + yield farming + NFT.
4. **Dencun (2024–26) — Hilangnya Deflasi:** sukses teknis (gas L2 turun >90%) **justru** menurunkan
   pendapatan L1. Karena **EIP-1559 burn** sebanding kemacetan L1, migrasi transaksi ke blob space menurunkan
   burn di bawah emisi (~1.700–1.800 ETH/hari) → ETH kembali **net-inflasi**; hilangnya narasi "Ultra Sound
   Money" memicu underperformance vs BTC/SOL (2025–awal 2026). *Contoh utama: sukses teknis → dampak tokenomik
   negatif tak terduga.*
5. **Yen Carry Unwind (awal 2026):** pengetatan BOJ → penutupan carry trade Yen → liquidity squeeze/derisking
   → ETH turun dari >$3.000 ke ~$1.500–1.800 (pertengahan 2026). *Contoh: korelasi makro global.* →
   `docs/MarketBehaviour/MarketCorrelation.md`.

## 11. Current State (2025–2026)
_ref: `docs/Ontology/Metrics.md`, `docs/Ontology/Team.md`, `docs/Ontology/Risks.md`_

Fundamental kuat: rekor volume transaksi harian (L1+L2), dominasi stablecoin ~$160 miliar, RWA >$15 miliar.
Namun **krisis koordinasi EF:** restrukturisasi awal 2025 mendelegasikan riset inti ke luar yayasan → hengkang
peneliti senior (Carl Beek, Julian Ma, koordinator hard fork **Tim Beiko**) pertengahan 2026. Keragaman klien
(Geth, Nethermind, Besu) menjaga operasional, tetapi hilangnya penengah mempersulit koordinasi upgrade
(Glamsterdam, Hegota).

## 12. Success Evaluation — Enam Perspektif
_ref: `docs/Success/*`, `docs/Reasoning/Explainability.md`_

Ethereum = **keberhasilan mutlak dalam infrastruktur & penciptaan standar industri** (EVM = "OS" Web3;
kompetitor pun EVM-compatible).
1. **Founder** (`Success/Founder.md`): misi platform netral tercapai; tapi tata kelola desentralisasi
   membatasi kendali arah yang cepat.
2. **VC** (`Success/VC.md`): likuiditas pasar terdalam; fondasi portofolio Web3.
3. **Investor**: ETH jadi aset produktif (native yield via staking); tapi tesis kelangkaan direvisi pasca-Dencun.
4. **Community** (`Success/Community.md`): menang ideologi (desentralisasi, tolak kompromi keamanan); harga =
   fragmentasi likuiditas & kebingungan UX.
5. **Developer** (`Success/Developer.md`): ekosistem paling matang, dokumentasi terlengkap, keamanan ekonomi terbesar.
6. **End-user**: L2 menekan biaya ke sub-sen; tapi bridging, fragmentasi saldo, risiko eksploitasi tetap jadi hambatan.

## 13. Extracted Patterns & Lessons (untuk Reasoning)
_ref: `docs/Patterns/*`, `docs/Reasoning/*` — bahan analog untuk prediksi proyek lain._

1. **Konsensus sosial menimpa "Code is Law"** saat krisis sistemik (The DAO). → `Patterns/Recovery.md`
2. **Norma imutabilitas mengeras seiring waktu** (EIP-999 ditolak). → `Patterns/Failure.md`
3. **Kas volatil tunggal = risiko** (trauma 2014 → penjualan OTC defensif). → `Ontology/Risks.md`
4. **Sukses teknis dapat merusak tokenomics** (Dencun → net-inflasi). → `Reasoning/Prediction.md`
5. **First Mover + ekosistem/standar (EVM) = moat terkuat**, mengalahkan pesaing "lebih cepat". →
   `Innovation/CompetitiveMoat.md`
6. **Sentralisasi efisiensi-modal** (Lido) memicu mitigasi terdistribusi (DVT). → `Patterns/NetworkEffect.md`
7. **Aset kripto makin terkorelasi makro global** (Yen carry). → `MarketBehaviour/MarketCorrelation.md`

## 14. Related Framework Definitions
- Ontology: `docs/Ontology/Identity.md`, `Team.md`, `Funding.md`, `Tokenomics.md`, `Governance.md`,
  `Security.md`, `Risks.md`, `Technology.md`, `Ecosystem.md`, `Metrics.md`, `Revenue.md`
- Patterns: `docs/Patterns/Failure.md`, `Recovery.md`, `NetworkEffect.md`
- Lifecycle: `docs/TokenLifecycle/*` (Frontier→Merge→Dencun→…)
- Market: `docs/MarketBehaviour/MarketCorrelation.md`, `docs/Valuation/Competitors.md`, `docs/Valuation/TVL.md`
- Success: `docs/Success/*`
- Cross-project: `examples/Pioneer/Lido.md`, `examples/Pioneer/EigenLayer.md`, `examples/Pioneer/Uniswap.md`,
  `examples/Pioneer/Aave.md`, `examples/Pioneer/Optimism.md`, `examples/Pioneer/Celestia.md`

## 15. Sources
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

_(Full 81-source bibliography retained in the original Deep Research report.)_
