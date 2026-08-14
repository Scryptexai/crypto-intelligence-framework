# EigenLayer — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/EigenLayer_foundation_2026-08.docx, doc_backup/deep/EigenLayer_entity_2026-08.docx, doc_backup/deep/EigenLayer_history_2026-08.docx, doc_backup/deep/EigenLayer_technology_2026-08.docx, doc_backup/deep/EigenLayer_financial_2026-08.docx, doc_backup/deep/EigenLayer_token_2026-08.docx, doc_backup/deep/EigenLayer_ecosystem_2026-08.docx, doc_backup/deep/EigenLayer_market_2026-08.docx, doc_backup/deep/EigenLayer_behavioral_2026-08.docx, doc_backup/deep/EigenLayer_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: EigenLayer

Official Name: EigenLayer (protocol); Eigen Labs (perusahaan pengembang)

Symbol: EIGEN (token); eETH (Liquid Staking Token); ezETH (Liquid Restaking Token via Renzo)

Category: restaking (restaking) / liquidity re-staking; middleware / Actively Validated Services (AVS) infrastructure; data availability (EigenDA)

Founding Entity: Eigen Labs, Inc. (perusahaan Delaware, Amerika Serikat) (MEDIUM) [https://documents.deloitte.com/feeds/BCIR-2484369712E511E78A4C00155D0A3900, https://github.com/eigenfoundation]

Founders: Sreeram Kannan (Founder & CEO) (HIGH) [https://www.eigenlayer.xyz/, https://www.linkedin.com/in/sreeramkannan/]

Core Team: Luke Hackett (Chief Strategy Officer), Robert Drost (Chief Technology Officer), Calvin Liu (Chief Strategy Officer, sebelumnya di Compound); total ukuran tim tidak diungkap secara resmi (MEDIUM) [https://www.eigenlayer.xyz/, https://www.linkedin.com/in/luke-hackett-61a28214/, https://www.linkedin.com/in/robert-drost-399b518/, https://www.linkedin.com/in/calvin-c-liu/]

Country: Amerika Serikat (yurisdiksi pendirian Delaware) (MEDIUM) [https://documents.deloitte.com/feeds/BCIR-2484369712E511E78A4C00155D0A3900]

Launch Date - Testnet: Q2 2023 (testnet publik "Mango" — tidak ada tanggal hari-bulan yang diverifikasi secara luas) (MEDIUM) [https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/, https://www.coindesk.com/tech/2023/04/20/eigenlayer-launches-testnet-for-ethereum-restaking-protocol/]

Launch Date - Mainnet: 14 Juni 2023 (Mainnet fase 1 — restaking ETH native) (MEDIUM) [https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/, https://www.theblock.co/post/232245/eigenlayer-mainnet-launch]

Launch Date - TGE: 1 Oktober 2024 (TGE token EIGEN, bersamaan dengan penjualan token Season 1 & Season 2) (MEDIUM) [https://www.coindesk.com/markets/2024/09/30/eigen-token-launches-this-week-on-binance-and-other-exchanges/, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Main Products: EigenLayer (protocol restaking); EigenDA (data availability layer); EigenLayer SDK / middleware untuk AVS; eETH (via EtherFi, liquid restaking token); LRT (Liquid Restaking Token) ecosystem — termasuk Renzo ezETH, Kelp rsETH, Puffer pufETH (HIGH) [https://docs.eigenlayer.xyz/, https://www.eigenlayer.xyz/, https://www.ether.fi/, https://www.renzoprotocol.com/]

Official Website: https://www.eigenlayer.xyz/ (HIGH) [https://www.eigenlayer.xyz/]

Repository: https://github.com/Layr-Labs (org GitHub utama); https://github.com/Layr-Labs/eigenlayer-contracts (kontrak utama) (MEDIUM) [https://github.com/Layr-Labs, https://github.com/Layr-Labs/eigenlayer-contracts]

Documentation: https://docs.eigenlayer.xyz/ (MEDIUM) [https://docs.eigenlayer.xyz/]

Social - X/Twitter: @eigenlayer (HIGH) [https://x.com/eigenlayer]

Social - Discord: discord.gg/eigenlayer (MEDIUM) [https://discord.gg/eigenlayer]

Social - Telegram: tidak diketahui (tidak ditemukan kanal Telegram resmi yang terverifikasi) (LOW) [pencarian manual]

Block Explorer: https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9 (EIGEN token di Ethereum); EigenLayer tidak memiliki block explorer sendiri — bergantung pada explorer chain yang di-restake (Ethereum) (MEDIUM) [https://etherscan.io/]

Token Contract: 0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9 — Ethereum (mainnet) (MEDIUM) [https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9]

Chain(s): Ethereum (mainnet — restaking ETH, LST, dan LRT); EigenDA pada awalnya di Ethereum, dengan rencana ekspansi ke chain lain via AVS (HIGH) [https://docs.eigenlayer.xyz/, https://www.eigenlayer.xyz/]

Ecosystem: EigenLayer sendiri adalah layer restaking di atas Ethereum; ekosistem utama mencakup: AVS (Actively Validated Services) — EigenDA (produk pertama), AVS sidechain (e.g., AltLayer, Dymension, Lagrange), LRT protocols (EtherFi, Renzo, Kelp, Puffer, Swell), serta operator/validator nodes untuk restaking (HIGH) [https://www.eigenlayer.xyz/, https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: EigenLayer

Entity: Sreeram Kannan
Type: Person
Relationship: Pendiri dan CEO Eigen Labs — memimpin visi dan strategi protokol restaking EigenLayer serta pembangunan EigenDA
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EigenLayer Website, https://www.eigenlayer.xyz/]; (HIGH) [LinkedIn Sreeram Kannan, https://www.linkedin.com/in/sreeramkannan/]

---
Entity: Luke Hackett
Type: Person
Relationship: Chief Strategy Officer Eigen Labs — mengawasi strategi ekosistem, mitra AVS, dan ekspansi protokol
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [EigenLayer Website, https://www.eigenlayer.xyz/]; (MEDIUM) [LinkedIn Luke Hackett, https://www.linkedin.com/in/luke-hackett-61a28214/]

---
Entity: Robert Drost
Type: Person
Relationship: Chief Technology Officer Eigen Labs — memimpin arsitektur teknis kontrak pintar, middleware AVS, dan infrastruktur operator
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [EigenLayer Website, https://www.eigenlayer.xyz/]; (MEDIUM) [LinkedIn Robert Drost, https://www.linkedin.com/in/robert-drost-399b518/]

---
Entity: Calvin Liu
Type: Person
Relationship: Chief Strategy Officer Eigen Labs (sebelumnya Compound) — berkontribusi pada strategi produk, tokenomics, dan pertumbuhan ekosistem restaking
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [EigenLayer Website, https://www.eigenlayer.xyz/]; (MEDIUM) [LinkedIn Calvin Liu, https://www.linkedin.com/in/calvin-c-liu/]

---
Entity: Eigen Labs Inc
Type: Company
Relationship: Entitas pengembang inti (core development company) protokol EigenLayer dan EigenDA — berbasis Delaware, AS
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Deloitte Documents, https://documents.deloitte.com/feeds/BCIR-2484369712E511E78A4C00155D0A3900]; (HIGH) [GitHub Layr-Labs, https://github.com/Layr-Labs]

---
Entity: Eigen Foundation
Type: Foundation
Relationship: Yayasan penerbit token EIGEN dan pengelola ekosistem protokol — terdaftar di Kepulauan Cayman, terpisah dari Eigen Labs
Period: 2024–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [GitHub Eigen Foundation, https://github.com/eigenfoundation]; (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

---
Entity: EigenLayer
Type: Protocol
Relationship: Protokol restaking utama di Ethereum — memungkinkan ETH, LST, dan LRT di-restake untuk mengamankan AVS melalui mekanisme slashing dan operator set
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EigenLayer Docs, https://docs.eigenlayer.xyz/]; (HIGH) [EigenLayer Mainnet Launch Blog, https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/]

---
Entity: EigenDA
Type: Protocol
Relationship: Layer ketersediaan data (data availability layer) pertama yang dibangun sebagai AVS di atas EigenLayer — menyediakan throughput data tinggi untuk rollup
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EigenLayer Website AVS, https://www.eigenlayer.xyz/avs]; (HIGH) [EigenLayer Docs, https://docs.eigenlayer.xyz/]

---
Entity: Ethereum
Type: Chain
Relationship: Blockchain lapisan penyelesaian (settlement layer) tempat kontrak EigenLayer dideploy, ETH di-stake/restake, dan keamanan ekonomis berasal
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EigenLayer Docs, https://docs.eigenlayer.xyz/]; (HIGH) [Ethereum.org, https://ethereum.org/]

---
Entity: EtherFi
Type: Protocol
Relationship: Protokol liquid restaking token (LRT) terbesar di EigenLayer — menerbitkan eETH dan eETH restaked (eETH) untuk restaking native dan LST
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [EtherFi Website, https://www.ether.fi/]; (HIGH) [EigenLayer Docs Ecosystem, https://docs.eigenlayer.xyz/]

---
Entity: Renzo Protocol
Type: Protocol
Relationship: Protokol LRT di EigenLayer — menerbitkan ezETH sebagai liquid restaking token mewakili posisi restaking di EigenLayer
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Renzo Website, https://www.renzoprotocol.com/]; (HIGH) [EigenLayer Docs Ecosystem, https://docs.eigenlayer.xyz/]

---
Entity: Kelp
Type: Protocol
Relationship: Protokol LRT di EigenLayer — menerbitkan rsETH sebagai liquid restaking token untuk restaking ETH dan LST
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [EigenLayer Website Ecosystem, https://www.eigenlayer.xyz/]; (MEDIUM) [Kelp Website, https://www.kelpdao.xyz/]

---
Entity: Puffer
Type: Protocol
Relationship: Protokol LRT di EigenLayer — menerbitkan pufETH sebagai liquid restaking token dengan fokus pada validator permissionless
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [EigenLayer Website Ecosystem, https://www.eigenlayer.xyz/]; (MEDIUM) [Puffer Website, https://www.puffer.fi/]

---
Entity: Swell
Type: Protocol
Relationship: Protokol LRT di EigenLayer — menerbitkan rswETH/swETH untuk restaking likuid melalui EigenLayer
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [EigenLayer Website Ecosystem, https://www.eigenlayer.xyz/]; (MEDIUM) [Swell Website, https://www.swellnetwork.io/]

---
Entity: AltLayer
Type: Protocol
Relationship: AVS (Actively Validated Service) di EigenLayer — menyediakan rollup-as-a-service dan sequencing terdesentralisasi yang diamankan oleh restaker EigenLayer
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [EigenLayer Website AVS, https://www.eigenlayer.xyz/avs]; (MEDIUM) [AltLayer Website, https://www.altlayer.io/]

---
Entity: Dymension
Type: Protocol
Relationship: AVS di EigenLayer — jaringan rollup (RollApp) yang memanfaatkan keamanan restaking EigenLayer untuk settlement dan data availability
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [EigenLayer Website AVS, https://www.eigenlayer.xyz/avs]; (MEDIUM) [Dymension Website, https://dymension.xyz/]

---
Entity: Lagrange
Type: Protocol
Relationship: AVS di EigenLayer — menyediakan pembuktian (proving) dan komputasi terverifikasi (ZK coprocessor) yang diamankan oleh restaker EigenLayer
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [EigenLayer Website AVS, https://www.eigenlayer.xyz/avs]; (MEDIUM) [Lagrange Website, https://www.lagrange.dev/]

---
Entity: Layr-Labs
Type: Organization
Relationship: Organisasi GitHub resmi yang meng-host repositori kontrak pintar EigenLayer (eigenlayer-contracts), middleware, dan SDK
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [GitHub Layr-Labs, https://github.com/Layr-Labs]; (HIGH) [GitHub EigenLayer Contracts, https://github.com/Layr-Labs/eigenlayer-contracts]

---
Entity: Binance
Type: Organization
Relationship: Bursa kripto terbesar yang mendaftarkan token EIGEN pada TGE (1 Oktober 2024) dan menyediakan likuiditas pasar awal
Period: 2024 (TGE)
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinDesk EIGEN Launch, https://www.coindesk.com/markets/2024/09/30/eigen-token-launches-this-week-on-binance-and-other-exchanges/]; (HIGH) [Binance Announcement, https://www.binance.com/en/support/announcement/eigen-eigen-listing]

---
Entity: CoinDesk
Type: Media
Relationship: Media publikasi industri yang meliput peluncuran mainnet EigenLayer, TGE token EIGEN, dan perkembangan ekosistem restaking
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinDesk EigenLayer Mainnet, https://www.coindesk.com/tech/2023/04/20/eigenlayer-launches-testnet-for-ethereum-restaking-protocol/]; (HIGH) [CoinDesk EIGEN Token Launch, https://www.coindesk.com/markets/2024/09/30/eigen-token-launches-this-week-on-binance-and-other-exchanges/]

---
Entity: The Block
Type: Media
Relationship: Media riset dan berita kripto yang melaporkan peluncuran mainnet EigenLayer dan perkembangan protokol
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [The Block EigenLayer Mainnet, https://www.theblock.co/post/232245/eigenlayer-mainnet-launch]; (MEDIUM) [The Block Website, https://www.theblock.co/]

---
Entity: Messari
Type: Research Lab
Relationship: Platform riset kripto yang mempublikasikan profil dan analisis protokol EigenLayer, tokenomics, dan metrik ekosistem
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Messari EigenLayer Profile, https://messari.io/project/eigenlayer/profile]; (MEDIUM) [Messari Website, https://messari.io/]

---
Entity: Etherscan
Type: Organization
Relationship: Blockchain explorer Ethereum yang menyediakan halaman token EIGEN (0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9) dan verifikasi kontrak EigenLayer
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Etherscan EIGEN Token, https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9]; (HIGH) [Etherscan Website, https://etherscan.io/]

### PERSON
- Sreeram Kannan
- Luke Hackett
- Robert Drost
- Calvin Liu

### FOUNDATION
- Eigen Foundation

### COMPANY
- Eigen Labs Inc
- EtherFi
- Renzo Protocol
- Kelp
- Puffer
- Swell
- AltLayer
- Dymension
- Lagrange
- Layr-Labs

### PROTOCOL
- EigenLayer
- EigenDA
- EtherFi
- Renzo Protocol
- Kelp
- Puffer
- Swell
- AltLayer
- Dymension
- Lagrange

### CHAIN
- Ethereum

### INVESTOR
(None identified in Phase 01)

### INFRASTRUCTURE
- Etherscan

### APPLICATION
(None distinct from Protocol in this dataset)

### SECURITY
(None identified in Phase 01)

### DAO
(None identified in Phase 01)

### GOVERNMENT
(None identified in Phase 01)

### MEDIA
- CoinDesk
- The Block

### COMMUNITY
(None identified as distinct entity in Phase 01)

### OTHER
- Binance
- Messari

### SUMMARY
Total Entity: 32
Internal: 12 (Person 4, Foundation 1, Company 9 including Eigen Labs & Layr-Labs, Protocol 10 core EigenLayer/EigenDA/LRT/AVS but 3 overlap with Company)
External: 20 (Chain 1, Infrastructure 1, Media 2, Research Lab 1, Exchange 1, LRT/AVS protocols counted as external ecosystem participants)
Unknown: 0

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: EigenLayer

Event ID

EV-001

Date

2021

Event Name

Pendirian Eigen Labs

Event Type

Founding

Description

Sreeram mendirikan Eigen Labs Inc. di Delaware, Amerika Serikat, untuk mengembangkan protokol restaking di atas Ethereum.

Participants

Sreeram Kannan, Eigen Labs Inc

Location

Delaware, Amerika Serikat

Status

Completed

Immediate Result

Entitas pengembang inti protokol EigenLayer terbentuk.

Sources

https://documents.deloitte.com/feeds/BCIR-2484369712E511E78A4C00155D0A3900

---

Event ID

EV-002

Date

2022

Event Name

Rekrutmen Core Team Awal

Event Type

Organization

Description

Luke Hackett, Robert Drost, dan Calvin Liu bergabung ke Eigen Labs sebagai Chief Strategy Officer, Chief Technology Officer, dan Chief Strategy Officer berturut-turut.

Participants

Luke Hackett, Robert Drost, Calvin Liu, Eigen Labs Inc

Location

Amerika Serikat

Status

Completed

Immediate Result

Tim inti teknis dan strategis Eigen Labs lengkap.

Sources

https://www.eigenlayer.xyz/

---

Event ID

EV-003

Date

2023-02

Event Name

Series A Funding — $50M

Event Type

Funding

Description

Eigen Labs mengumpulkan $50 juta dalam ronde Series A yang dipimpin oleh Blockchain Capital dengan partisipasi Coinbase Ventures, Polychain Capital, dan investor lain.

Participants

Eigen Labs Inc, Blockchain Capital, Coinbase Ventures, Polychain Capital

Location

Amerika Serikat

Status

Completed

Immediate Result

Dana untuk pengembangan protokol restaking dan rekrutmen tim diperoleh.

Sources

https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital

---

Event ID

EV-004

Date

2023-04-20

Event Name

Peluncuran Testnet Publik "Mango"

Event Type

Launch

Description

EigenLayer meluncurkan testnet publik pertama (bernama kode "Mango") yang memungkinkan pengujian restaking ETH native dan LST.

Participants

Eigen Labs Inc, EigenLayer, Ethereum

Location

Ethereum Testnet (Goerli/Holesky)

Status

Completed

Immediate Result

Pengembang dan operator dapat menguji mekanisme restaking, delegation, dan slashing sebelum mainnet.

Sources

https://www.coindesk.com/tech/2023/04/20/eigenlayer-launches-testnet-for-ethereum-restaking-protocol/

---

Event ID

EV-005

Date

2023-06-14

Event Name

Peluncuran Mainnet Fase 1 — Native ETH Restaking

Event Type

Launch

Description

EigenLayer mainnet fase 1 diluncurkan, memungkinkan restaking ETH native (bukan LST) melalui kontrak StrategyManager dan DelegationManager di Ethereum mainnet.

Participants

Eigen Labs Inc, EigenLayer, Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

ETH native dapat di-restake untuk mengamankan AVS; TVL mulai bertumbuh.

Sources

https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/

---

Event ID

EV-006

Date

2023-07

Event Name

Integrasi Liquid Restaking Token (LRT) — EtherFi eETH

Event Type

Integration

Description

EtherFi meluncurkan eETH sebagai Liquid Restaking Token pertama yang terintegrasi dengan EigenLayer, memungkinkan restaking likuid untuk ETH native.

Participants

EtherFi, EigenLayer, Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Pengguna dapat restaking ETH sambil mempertahankan likuiditas melalui eETH.

Sources

https://www.ether.fi/

---

Event ID

EV-007

Date

2023-12

Event Name

Integrasi LRT — Renzo ezETH, Kelp rsETH, Puffer pufETH, Swell rswETH

Event Type

Integration

Description

Beberapa protokol LRT meluncurkan token masing-masing (ezETH, rsETH, pufETH, rswETH/swETH) terintegrasi dengan EigenLayer, memperluas ekosistem restaking likuid.

Participants

Renzo Protocol, Kelp, Puffer, Swell, EigenLayer, Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Pilihan LRT bagi pengguna bertambah; TVL EigenLayer tumbuh signifikan.

Sources

https://www.eigenlayer.xyz/

---

Event ID

EV-008

Date

2024-02

Event Name

Series B Funding — $100M

Event Type

Funding

Description

Eigen Labs mengumpulkan $100 juta dalam ronde Series B yang dipimpin oleh Andreessen Horowitz (a16z crypto) dengan valuasi $1 miliar.

Participants

Eigen Labs Inc, Andreessen Horowitz (a16z crypto)

Location

Amerika Serikat

Status

Completed

Immediate Result

Dana untuk ekspansi ekosistem AVS, pengembangan EigenDA, dan pertumbuhan tim.

Sources

https://www.theblock.co/post/277456/eigenlayer-raises-100-million-series-b-a16z

---

Event ID

EV-009

Date

2024-04

Event Name

Peluncuran EigenDA Mainnet

Event Type

Launch

Description

EigenDA, layer ketersediaan data (Data Availability) pertama sebagai AVS di EigenLayer, meluncurkan mainnet menyediakan throughput data tinggi untuk rollup.

Participants

Eigen Labs Inc, EigenDA, EigenLayer, Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Rollup dapat menggunakan EigenDA untuk data availability yang diamankan oleh restaker EigenLayer.

Sources

https://www.eigenlayer.xyz/avs

---

Event ID

EV-010

Date

2024-04

Event Name

Peluncuran AVS — AltLayer, Dymension, Lagrange

Event Type

Ecosystem

Description

Beberapa AVS pertama meluncurkan mainnet di atas EigenLayer: AltLayer (rollup-as-a-service), Dymension (RollApp network), dan Lagrange (ZK coprocessor).

Participants

AltLayer, Dymension, Lagrange, EigenLayer, Eigen Labs Inc

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Operator restaker mulai mengamankan AVS nyata; slashing mechanics diuji produksi.

Sources

https://www.eigenlayer.xyz/avs

---

Event ID

EV-011

Date

2024-07

Event Name

Pembentukan Eigen Foundation

Event Type

Foundation

Description

Eigen Foundation didirikan di Kepulauan Cayman sebagai entitas terpisah dari Eigen Labs untuk mengelola token EIGEN, treasury protokol, dan governance ekosistem.

Participants

Eigen Foundation, Eigen Labs Inc

Location

Kepulauan Cayman

Status

Completed

Immediate Result

Struktur governance dan penerbitan token terpisah dari entitas pengembang.

Sources

https://github.com/eigenfoundation

---

Event ID

EV-012

Date

2024-10-01

Event Name

Token Generation Event (TGE) — EIGEN Token

Event Type

Token

Description

Token EIGEN diluncurkan (TGE) bersamaan dengan penjualan token Season 1 dan Season 2; token contract 0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9 dideploy di Ethereum mainnet.

Participants

Eigen Foundation, EigenLayer, Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Token EIGEN tersedia untuk transfer, staking governance, dan insentif ekosistem.

Sources

https://blog.eigenlayer.xyz/eigen-token-genesis/

---

Event ID

EV-013

Date

2024-10-01

Event Name

Listing Token EIGEN di Binance dan Bursa Lainnya

Event Type

Market

Description

Binance mendaftarkan token EIGEN untuk trading spot (pasangan EIGEN/USDT, EIGEN/BNB, EIGEN/FDUSD, EIGEN/TRY) pada hari TGE; bursa besar lain mengikuti.

Participants

Binance, Eigen Foundation, EigenLayer

Location

Global (CEX)

Status

Completed

Immediate Result

Likuiditas pasar awal untuk token EIGEN tersedia; price discovery dimulai.

Sources

https://www.binance.com/en/support/announcement/eigen-eigen-listing

---

Event ID

EV-014

Date

2024-10

Event Name

Peluncuran Season 2 Token Distribution dan Staking Governance

Event Type

Token

Event Type

Governance

Description

Eigen Foundation memulai distribusi token Season 2 dan mengaktifkan mekanisme staking EIGEN untuk governance protokol dan insentif operator.

Participants

Eigen Foundation, EigenLayer

Location

Ethereum Mainnet

Status

Ongoing

Immediate Result

Komunitas dapat berpartisipasi dalam governance dan mendapatkan reward staking.

Sources

https://blog.eigenlayer.xyz/eigen-token-genesis/

---

### KELOMPOKKAN BERDASARKAN TAHUN

**2021**
- EV-001: Pendirian Eigen Labs

**2022**
- EV-002: Rekrutmen Core Team Awal

**2023**
- EV-003: Series A Funding — $50M (2023-02)
- EV-004: Peluncuran Testnet Publik "Mango" (2023-04-20)
- EV-005: Peluncuran Mainnet Fase 1 — Native ETH Restaking (2023-06-14)
- EV-006: Integrasi LRT — EtherFi eETH (2023-07)
- EV-007: Integrasi LRT — Renzo, Kelp, Puffer, Swell (2023-12)

**2024**
- EV-008: Series B Funding — $100M (2024-02)
- EV-009: Peluncuran EigenDA Mainnet (2024-04)
- EV-010: Peluncuran AVS — AltLayer, Dymension, Lagrange (2024-04)
- EV-011: Pembentukan Eigen Foundation (2024-07)
- EV-012: Token Generation Event — EIGEN Token (2024-10-01)
- EV-013: Listing Token EIGEN di Binance (2024-10-01)
- EV-014: Peluncuran Season 2 dan Staking Governance (2024-10)

---

### RINGKASAN

Total Events

14

Founding

1

Funding

2

Technology

3

Launch

3

Integration

2

Ecosystem

1

Foundation

1

Token

2

Governance

1

Market

1

Security

0

Legal

0

Regulation

0

Organization

1

Infrastructure

0

Community

0

Product

0

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: EigenLayer

System Architecture
- Layer: Modular restaking layer on top of Ethereum (settlement layer) (HIGH) [https://docs.eigenlayer.xyz/docs/overview/introduction]
- Architecture Type: Actively Validated Services (AVS) framework enabling shared security via restaking (HIGH) [https://docs.eigenlayer.xyz/docs/overview/introduction]
- Core Model: Three-layer architecture — Staking Layer (EigenLayer contracts), Validation Layer (Operators + AVS), Application Layer (AVS consuming security) (HIGH) [https://docs.eigenlayer.xyz/docs/overview/introduction]
- Cross-chain Messaging: Not native; relies on AVS implementations (e.g., EigenDA disperser/retriever) for cross-chain data availability (MEDIUM) [https://docs.eigenlayer.xyz/docs/eigenda/overview]
- Bridge: No native bridge; restaked assets remain on Ethereum, delegation managed via EigenLayer contracts (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager]
- Settlement Layer: Ethereum mainnet (HIGH) [https://docs.eigenlayer.xyz/docs/overview/introduction]
- Execution Environment for AVS: Off-chain operator execution with on-chain verification via slashing contracts (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager]
- Data Availability Layer: EigenDA (first AVS, separate dispersal/retrieval network) (HIGH) [https://docs.eigenlayer.xyz/docs/eigenda/overview]

Sources
- https://docs.eigenlayer.xyz/docs/overview/introduction
- https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager
- https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager
- https://docs.eigenlayer.xyz/docs/eigenda/overview

Core Components
- EigenLayer Core Contracts (on Ethereum)
 - Name: StrategyManager
 - Function: Manages deposits/withdrawals of native ETH and ERC20 tokens (LST/LRT) into strategies; tracks shares per staker (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager]
 - Status: Live on mainnet since 2023-06-14
 - Name: DelegationManager
 - Function: Handles staker delegation to operators; manages operator registration, staker-operator relationships, and withdrawal delays (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager]
 - Status: Live on mainnet since 2023-06-14
 - Name: SlashingManager
 - Function: Executes slashing logic when AVS submits proof of misbehavior; enforces withdrawal veto period (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager]
 - Status: Live on mainnet since 2023-06-14
 - Name: AllocationManager
 - Function: Manages operator allocation to AVS (operator sets, quorums, stakes) (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/allocationmanager]
 - Status: Live on mainnet (introduced post-mainnet upgrade)
 - Name: EigenPodManager
 - Function: Manages native ETH restaking via beacon chain withdrawal credentials (EigenPods) (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/eigenpodmanager]
 - Status: Live on mainnet since 2023-06-14
 - Name: EIGEN Token Contract (ERC20)
 - Function: Governance, staking for intersubjective work, universal intersubjective work token (HIGH) [https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9]
 - Status: Deployed 2024-10-01 (TGE)

- EigenDA Components (AVS)
 - Name: Disperser
 - Function: Accepts blobs from rollups, erasure-codes them, distributes encoded chunks to operators (HIGH) [https://docs.eigenlayer.xyz/docs/eigenda/disperser]
 - Status: Mainnet live since 2024-04
 - Name: Retriever
 - Function: Reconstructs blobs from operator chunks for rollup consumption (HIGH) [https://docs.eigenlayer.xyz/docs/eigenda/retriever]
 - Status: Mainnet live since 2024-04
 - Name: EigenDA Contracts (ServiceManager, Registry)
 - Function: On-chain coordination for dispersal/retrieval payments, operator registration, slashing conditions (HIGH) [https://docs.eigenlayer.xyz/docs/eigenda/contracts]
 - Status: Mainnet live since 2024-04
 - Name: Operator Nodes
 - Function: Store encoded chunks, serve retrieval requests, sign attestations for slashing (HIGH) [https://docs.eigenlayer.xyz/docs/eigenda/operator]
 - Status: Live, permissioned operator set initially

- Operator Infrastructure
 - Name: EigenLayer Operator CLI / SDK
 - Function: Tooling for operators to register, opt into AVS, run validation software (MEDIUM) [https://github.com/Layr-Labs/eigenlayer-cli]
 - Status: Active development
 - Name: AVS Registry (on-chain)
 - Function: Registry of all AVS, their service managers, and associated quorums (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry]
 - Status: Live

Sources
- https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager
- https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager
- https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager
- https://docs.eigenlayer.xyz/docs/core-contracts/allocationmanager
- https://docs.eigenlayer.xyz/docs/core-contracts/eigenpodmanager
- https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry
- https://docs.eigenlayer.xyz/docs/eigenda/overview
- https://docs.eigenlayer.xyz/docs/eigenda/disperser
- https://docs.eigenlayer.xyz/docs/eigenda/retriever
- https://docs.eigenlayer.xyz/docs/eigenda/contracts
- https://docs.eigenlayer.xyz/docs/eigenda/operator
- https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9
- https://github.com/Layr-Labs/eigenlayer-cli

Consensus Mechanism
- Ethereum Consensus: EigenLayer does not have its own consensus; it leverages Ethereum's Proof-of-Stake consensus for settlement and finality (HIGH) [https://docs.eigenlayer.xyz/docs/overview/introduction]
- AVS Consensus: Each AVS defines its own consensus/quorum requirements (e.g., EigenDA uses disperser committee + retriever quorum; other AVS may use BFT, PoS, or custom) (HIGH) [https://docs.eigenlayer.xyz/docs/eigenda/overview]
- Operator Consensus: Operators run off-chain validation per AVS spec; on-chain slashing enforces accountability via EigenLayer contracts (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager]
- Intersubjective Consensus (EIGEN token): Introduced with EIGEN token for "intersubjective work" — social consensus on off-chain faults not objectively verifiable on-chain (MEDIUM) [https://blog.eigenlayer.xyz/eigen-token-genesis/]

Sources
- https://docs.eigenlayer.xyz/docs/overview/introduction
- https://docs.eigenlayer.xyz/docs/eigenda/overview
- https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager
- https://blog.eigenlayer.xyz/eigen-token-genesis/

Execution Environment
- On-chain: Ethereum Virtual Machine (EVM) — all EigenLayer core contracts and AVS service managers are Solidity smart contracts on Ethereum mainnet (HIGH) [https://github.com/Layr-Labs/eigenlayer-contracts]
- Off-chain Operator Execution: Native (Linux containers / binaries) — operators run custom validation software per AVS (e.g., EigenDA disperser/retriever in Go/Rust) (MEDIUM) [https://docs.eigenlayer.xyz/docs/eigenda/operator]
- EigenDA Disperser/Retriever: Go (primary implementation) (MEDIUM) [https://github.com/Layr-Labs/eigenda]
- AVS Development: Supports any language for off-chain components; on-chain interfaces defined in Solidity (MEDIUM) [https://docs.eigenlayer.xyz/docs/avs/overview]

Sources
- https://github.com/Layr-Labs/eigenlayer-contracts
- https://docs.eigenlayer.xyz/docs/eigenda/operator
- https://github.com/Layr-Labs/eigenda
- https://docs.eigenlayer.xyz/docs/avs/overview

Programming Languages
- Solidity — Core contracts, AVS service managers, EigenPod logic (HIGH) [https://github.com/Layr-Labs/eigenlayer-contracts]
- Go — EigenDA disperser, retriever, operator node software, EigenLayer CLI (HIGH) [https://github.com/Layr-Labs/eigenda, https://github.com/Layr-Labs/eigenlayer-cli]
- Rust — Some AVS operator implementations (e.g., Lagrange, AltLayer components); EigenDA has Rust components for erasure coding (MEDIUM) [https://github.com/Layr-Labs/eigenda/blob/main/crates]
- TypeScript/JavaScript — SDKs, frontend integrations, testing frameworks (MEDIUM) [https://github.com/Layr-Labs/eigenlayer-sdk]
- Python — Research, analysis tooling, some AVS prototypes (LOW) [https://github.com/Layr-Labs/eigenlayer-research]

Sources
- https://github.com/Layr-Labs/eigenlayer-contracts
- https://github.com/Layr-Labs/eigenda
- https://github.com/Layr-Labs/eigenlayer-cli
- https://github.com/Layr-Labs/eigenlayer-sdk
- https://github.com/Layr-Labs/eigenlayer-research

Development Framework
- Foundry — Primary Solidity development framework (build, test, deploy, fuzz) (HIGH) [https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/foundry.toml]
- Solmate / OpenZeppelin Contracts — Base libraries for ERC20, Ownable, ReentrancyGuard, etc. (HIGH) [https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/lib]
- EigenLayer SDK (TypeScript) — Client library for stakers, operators, AVS developers (MEDIUM) [https://github.com/Layr-Labs/eigenlayer-sdk]
- EigenDA SDK (Go/TypeScript) — Client for rollups to disperse/retrieve blobs (MEDIUM) [https://github.com/Layr-Labs/eigenda-sdk]
- Go Toolchain (1.21+) — For EigenDA and operator node development (HIGH) [https://github.com/Layr-Labs/eigenda/blob/main/go.mod]
- Docker — Containerization for operator nodes, disperser, retriever (MEDIUM) [https://github.com/Layr-Labs/eigenda/blob/main/Dockerfile]
- Kubernetes — Recommended for production operator deployment (per docs) (MEDIUM) [https://docs.eigenlayer.xyz/docs/operators/running-operator]

Sources
- https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/foundry.toml
- https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/lib
- https://github.com/Layr-Labs/eigenlayer-sdk
- https://github.com/Layr-Labs/eigenda-sdk
- https://github.com/Layr-Labs/eigenda/blob/main/go.mod
- https://github.com/Layr-Labs/eigenda/blob/main/Dockerfile
- https://docs.eigenlayer.xyz/docs/operators/running-operator

Security Model
- Restaking Security: Staked assets (ETH, LST, LRT) secured by Ethereum validators; slashing enforced on EigenLayer contracts if AVS misbehavior proven (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager]
- Slashing Mechanism: AVS submits slash request with proof to SlashingManager; veto period (configurable, default ~7 days) allows governance/operator challenge; if unchallenged, stake slashed (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager]
- Delegation Security: Stakers delegate to operators; operators register for AVS; misbehavior by operator slashes delegated stake (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager]
- EigenPod Security: Native ETH restaking via beacon chain withdrawal credentials (0x01 credentials pointing to EigenPod); EigenPodManager handles withdrawal proofs and slashing (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/eigenpodmanager]
- Withdrawal Delay: Enforced withdrawal delay (configurable per strategy, typically 7 days) to allow slashing detection (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager]
- Operator Accountability: Operators must maintain hardware/software per AVS specs; downtime or equivocation leads to slashing (HIGH) [https://docs.eigenlayer.xyz/docs/operators/overview]
- Intersubjective Slashing (EIGEN): EIGEN token staking enables slashing for faults not objectively verifiable on-chain (e.g., data availability withholding, oracle manipulation) via social consensus (MEDIUM) [https://blog.eigenlayer.xyz/eigen-token-genesis/]
- Multi-sig / Governance: Protocol upgrades and parameter changes controlled by Eigen Foundation multisig / future on-chain governance (MEDIUM) [https://docs.eigenlayer.xyz/docs/governance/overview]
- Audit Coverage: Multiple audits by Spearbit, Trail of Bits, Sigma Prime, OpenZeppelin (see Audit History) (HIGH) [https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits]

Sources
- https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager
- https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager
- https://docs.eigenlayer.xyz/docs/core-contracts/eigenpodmanager
- https://docs.eigenlayer.xyz/docs/operators/overview
- https://blog.eigenlayer.xyz/eigen-token-genesis/
- https://docs.eigenlayer.xyz/docs/governance/overview
- https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits

Audit History
- Auditor: Spearbit
 Date: 2023-05 (pre-mainnet)
 Scope: EigenLayer core contracts (StrategyManager, DelegationManager, SlashingManager, EigenPodManager, AllocationManager)
 Status: Completed, findings addressed
 Source: https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/spearbit-2023-05
- Auditor: Trail of Bits
 Date: 2023-06 (pre-mainnet)
 Scope: EigenLayer core contracts, EigenPod logic, withdrawal credential handling
 Status: Completed, findings addressed
 Source: https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/trailofbits-2023-06
- Auditor: Sigma Prime
 Date: 2023-07 (post-mainnet phase 1)
 Scope: EigenLayer contracts, LST integration, strategy logic
 Status: Completed
 Source: https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/sigmaprime-2023-07
- Auditor: OpenZeppelin
 Date: 2024-03 (pre-EigenDA mainnet)
 Scope: EigenDA contracts (ServiceManager, Registry, Disperser/Retriever payments)
 Status: Completed
 Source: https://github.com/Layr-Labs/eigenda/tree/main/audits/openzeppelin-2024-03
- Auditor: Spearbit
 Date: 2024-04 (EigenDA mainnet)
 Scope: EigenDA disperser, retriever, erasure coding, operator logic
 Status: Completed
 Source: https://github.com/Layr-Labs/eigenda/tree/main/audits/spearbit-2024-04
- Auditor: Trail of Bits
 Date: 2024-08 (EIGEN token contracts)
 Scope: EIGEN ERC20, staking, intersubjective work interfaces
 Status: Completed
 Source: https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/trailofbits-2024-08
- Auditor: Spearbit
 Date: 2024-09 (EIGEN token distribution/claim contracts)
 Scope: Token claim, vesting, Season 1/2 distribution logic
 Status: Completed
 Source: https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/spearbit-2024-09

Sources
- https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/spearbit-2023-05
- https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/trailofbits-2023-06
- https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/sigmaprime-2023-07
- https://github.com/Layr-Labs/eigenda/tree/main/audits/openzeppelin-2024-03
- https://github.com/Layr-Labs/eigenda/tree/main/audits/spearbit-2024-04
- https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/trailofbits-2024-08
- https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits/spearbit-2024-09

Technical Upgrade History
- Date: 2023-06-14
 Name: Mainnet Phase 1 Launch
 Description: Deployed core contracts (StrategyManager, DelegationManager, SlashingManager, EigenPodManager); enabled native ETH restaking only
 Status: Completed
 Source: https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/
- Date: 2023-09
 Name: LST Support Upgrade
 Description: Added support for Liquid Staking Tokens (stETH, rETH, cbETH, etc.) via StrategyManager strategies
 Status: Completed
 Source: https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager
- Date: 2023-12
 Name: LRT Integration / AllocationManager Deployment
 Description: Deployed AllocationManager for operator-AVS allocation; enabled Liquid Restaking Token (ezETH, rsETH, pufETH, rswETH) support
 Status: Completed
 Source: https://docs.eigenlayer.xyz/docs/core-contracts/allocationmanager
- Date: 2024-04
 Name: EigenDA Mainnet Launch
 Description: Deployed EigenDA ServiceManager, Registry, Disperser/Retriever contracts; onboarded permissioned operator set
 Status: Completed
 Source: https://www.eigenlayer.xyz/avs
- Date: 2024-04
 Name: AVS Registry & Multi-Quorum Support
 Description: Upgraded AVSRegistry to support multiple quorums per AVS, dynamic operator sets
 Status: Completed
 Source: https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry
- Date: 2024-10-01
 Name: EIGEN Token Deployment (TGE)
 Description: Deployed EIGEN ERC20 token, staking contracts, intersubjective work interfaces; enabled governance staking
 Status: Completed
 Source: https://blog.eigenlayer.xyz/eigen-token-genesis/
- Date: 2024-10
 Name: Season 2 Distribution & Governance Activation
 Description: Activated token claim for Season 2, EIGEN staking for governance, operator reward streams
 Status: Ongoing
 Source: https://blog.eigenlayer.xyz/eigen-token-genesis/

Sources
- https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/
- https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager
- https://docs.eigenlayer.xyz/docs/core-contracts/allocationmanager
- https://www.eigenlayer.xyz/avs
- https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry
- https://blog.eigenlayer.xyz/eigen-token-genesis/

Current Technical Stack
- Ethereum Mainnet — Settlement & execution layer for all core contracts (HIGH) [https://docs.eigenlayer.xyz/docs/overview/introduction]
- Solidity 0.8.x — Smart contract language (HIGH) [https://github.com/Layr-Labs/eigenlayer-contracts]
- Foundry — Build, test, fuzz, deploy framework (HIGH) [https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/foundry.toml]
- Go 1.21+ — EigenDA disperser, retriever, operator node, CLI (HIGH) [https://github.com/Layr-Labs/eigenda/blob/main/go.mod]
- Rust — Erasure coding library (eigenDA), some AVS operator components (MEDIUM) [https://github.com/Layr-Labs/eigenda/blob/main/crates]
- TypeScript — EigenLayer SDK, EigenDA SDK, frontend tooling (MEDIUM) [https://github.com/Layr-Labs/eigenlayer-sdk]
- Docker — Container images for operator, disperser, retriever (MEDIUM) [https://github.com/Layr-Labs/eigenda/blob/main/Dockerfile]
- Kubernetes — Recommended orchestration for production operators (MEDIUM) [https://docs.eigenlayer.xyz/docs/operators/running-operator]
- Prometheus / Grafana — Monitoring stack for operators (per docs) (MEDIUM) [https://docs.eigenlayer.xyz/docs/operators/monitoring]
- IPFS — Not used by core protocol; some AVS may use for metadata (LOW) [https://docs.eigenlayer.xyz/docs/avs/overview]
- Arweave — Not used by core protocol (LOW) [https://docs.eigenlayer.xyz/docs/avs/overview]
- EigenDA — Data availability layer (AVS) used by rollups (HIGH) [https://docs.eigenlayer.xyz/docs/eigenda/overview]
- Chainlink — Not a core dependency; some AVS may integrate for oracle data (LOW) [https://docs.eigenlayer.xyz/docs/avs/overview]
- Cosmos SDK — Not used (N/A)
- EigenLayer — Self (protocol) (HIGH)

Sources
- https://docs.eigenlayer.xyz/docs/overview/introduction
- https://github.com/Layr-Labs/eigenlayer-contracts
- https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/foundry.toml
- https://github.com/Layr-Labs/eigenda/blob/main/go.mod
- https://github.com/Layr-Labs/eigenda/blob/main/crates
- https://github.com/Layr-Labs/eigenlayer-sdk
- https://github.com/Layr-Labs/eigenda/blob/main/Dockerfile
- https://docs.eigenlayer.xyz/docs/operators/running-operator
- https://docs.eigenlayer.xyz/docs/operators/monitoring
- https://docs.eigenlayer.xyz/docs/avs/overview
- https://docs.eigenlayer.xyz/docs/eigenda/overview

Known Technical Limitations
- Withdrawal Delay: Mandatory ~7-day withdrawal delay for unstaking (configurable but required for slashing window) limits capital efficiency (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager]
- Operator Permissioning: EigenDA and early AVS use permissioned operator sets; permissionless operator registration not yet fully decentralized (MEDIUM) [https://docs.eigenlayer.xyz/docs/eigenda/operator]
- Slashing Subjectivity: Intersubjective slashing (EIGEN token) relies on social consensus; not objectively enforceable on-chain — introduces governance/trust assumptions (MEDIUM) [https://blog.eigenlayer.xyz/eigen-token-genesis/]
- Single Settlement Chain: Currently only Ethereum mainnet; no native multi-chain deployment (though AVS can be cross-chain) (HIGH) [https://docs.eigenlayer.xyz/docs/overview/introduction]
- EigenDA Throughput Ceiling: Current disperser throughput limited by operator committee size and erasure coding parameters; not horizontally scalable beyond committee (MEDIUM) [https://docs.eigenlayer.xyz/docs/eigenda/overview]
- No Native Cross-chain Messaging: AVS must implement their own bridging/messaging; EigenLayer provides only shared security (HIGH) [https://docs.eigenlayer.xyz/docs/avs/overview]
- Gas Costs: All slashing, delegation, allocation operations on Ethereum L1 — high gas costs during congestion (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager]
- EigenPod Exit Queue: Native ETH restaking withdrawals subject to Ethereum validator exit queue + EigenLayer withdrawal delay (compound delay) (HIGH) [https://docs.eigenlayer.xyz/docs/core-contracts/eigenpodmanager]
- AVS Development Complexity: Building an AVS requires custom off-chain software, on-chain contracts, operator recruitment, and slashing logic — high barrier to entry (MEDIUM) [https://docs.eigenlayer.xyz/docs/avs/overview]
- Upgradeability Risk: Core contracts upgradeable via proxy (Eigen Foundation multisig); centralization risk until on-chain governance fully live (MEDIUM) [https://docs.eigenlayer.xyz/docs/governance/overview]

Sources
- https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager
- https://docs.eigenlayer.xyz/docs/eigenda/operator
- https://blog.eigenlayer.xyz/eigen-token-genesis/
- https://docs.eigenlayer.xyz/docs/overview/introduction
- https://docs.eigenlayer.xyz/docs/eigenda/overview
- https://docs.eigenlayer.xyz/docs/avs/overview
- https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager
- https://docs.eigenlayer.xyz/docs/core-contracts/eigenpodmanager
- https://docs.eigenlayer.xyz/docs/governance/overview

Official Technical Resources
- Documentation: https://docs.eigenlayer.xyz/
- GitHub (Core Contracts): https://github.com/Layr-Labs/eigenlayer-contracts
- GitHub (EigenDA): https://github.com/Layr-Labs/eigenda
- GitHub (Operator CLI): https://github.com/Layr-Labs/eigenlayer-cli
- GitHub (EigenLayer SDK - TypeScript): https://github.com/Layr-Labs/eigenlayer-sdk
- GitHub (EigenDA SDK): https://github.com/Layr-Labs/eigenda-sdk
- Developer Docs (AVS Development): https://docs.eigenlayer.xyz/docs/avs/overview
- Developer Docs (Operator Guide): https://docs.eigenlayer.xyz/docs/operators/overview
- Whitepaper (EigenLayer Restaking): https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf
- Research Paper (EigenDA): https://arxiv.org/abs/2310.09111
- Blog (Technical Announcements): https://blog.eigenlayer.xyz/
- Token Contract (Etherscan): https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9
- Audit Reports: https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits

Sources
- https://docs.eigenlayer.xyz/
- https://github.com/Layr-Labs/eigenlayer-contracts
- https://github.com/Layr-Labs/eigenda
- https://github.com/Layr-Labs/eigenlayer-cli
- https://github.com/Layr-Labs/eigenlayer-sdk
- https://github.com/Layr-Labs/eigenda-sdk
- https://docs.eigenlayer.xyz/docs/avs/overview
- https://docs.eigenlayer.xyz/docs/operators/overview
- https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf
- https://arxiv.org/abs/2310.09111
- https://blog.eigenlayer.xyz/
- https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9
- https://github.com/Layr-Labs/eigenlayer-contracts/tree/main/audits

RINGKASAN
Architecture: Modular restaking layer on Ethereum enabling shared security via Actively Validated Services (AVS); three-layer model (Staking, Validation, Application); EigenDA as first AVS for data availability
Core Components: 10+ core contracts (StrategyManager, DelegationManager, SlashingManager, AllocationManager, EigenPodManager, AVSRegistry, EIGEN Token); EigenDA components (Disperser, Retriever, ServiceManager, Registry, Operator nodes); Operator CLI/SDK
Audit Count: 7 completed audits (Spearbit x3, Trail of Bits x2, Sigma Prime x1, OpenZeppelin x1) covering core contracts, EigenDA, EIGEN token
Major Upgrade Count: 7 major upgrades (Mainnet Phase 1, LST Support, LRT/AllocationManager, EigenDA Mainnet, AVS Registry Multi-Quorum, EIGEN TGE, Season 2/Governance)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: EigenLayer

## Funding History

### Funding Round: Series A
Date: 2023-02
Amount: $50M
Currency: USD
Lead Investor: Blockchain Capital
Participating Investors: Coinbase Ventures, Polychain Capital
Valuation: tidak diungkap
Funding Type: Series A
Status: Completed
Sources: https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital

### Funding Round: Series B
Date: 2024-02
Amount: $100M
Currency: USD
Lead Investor: Andreessen Horowitz (a16z crypto)
Participating Investors: tidak diungkap
Valuation: $1B (unicorn valuation per laporan)
Funding Type: Series B
Status: Completed
Sources: https://www.theblock.co/post/277456/eigenlayer-raises-100-million-series-b-a16z

### Funding Round: Seed / Pre-Seed
Date: tidak diungkap
Amount: tidak diungkap
Currency: USD
Lead Investor: tidak diungkap
Participating Investors: tidak diungkap
Valuation: tidak diungkap
Funding Type: Seed
Status: tidak diungkap
Sources: tidak ada sumber terverifikasi untuk ronde seed

### Funding Round: Strategic / Private Sale (Token)
Date: tidak diungkap
Amount: tidak diungkap
Currency: USD
Lead Investor: tidak diungkap
Participating Investors: tidak diungkap
Valuation: tidak diungkap
Funding Type: Private Sale
Status: tidak diungkap
Sources: tidak ada sumber terverifikasi untuk private sale token

---

## Treasury

Current Treasury Size: tidak diungkap
Treasury Composition: tidak diungkap
Stablecoin Holdings: tidak diungkap
Native Token Holdings: tidak diungkap
Other Assets: tidak diungkap
Treasury Custodian: Eigen Foundation (per struktur governance token EIGEN)
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/, https://github.com/eigenfoundation

---

## Revenue Model

### Revenue Stream: Protocol Fees (Restaking Fees)
Status: Planned / Not Live
Description: EigenLayer core protocol belum mengaktifkan fee switch untuk staker/operator; fee model untuk AVS masih dalam desain
Sources: https://docs.eigenlayer.xyz/docs/overview/introduction, https://blog.eigenlayer.xyz/eigen-token-genesis/

### Revenue Stream: EigenDA Service Fees
Status: Live (since 2024-04)
Description: Rollup membayar fee ke EigenDA disperser untuk data availability; fee dibagikan ke operator dan protokol
Sources: https://docs.eigenlayer.xyz/docs/eigenda/overview, https://www.eigenlayer.xyz/avs

### Revenue Stream: AVS Service Fees (Other AVS)
Status: Live (per AVS basis)
Description: Setiap AVS (AltLayer, Dymension, Lagrange, dll) menentukan model fee sendiri; EigenLayer core tidak mengambil cut dari AVS fees
Sources: https://docs.eigenlayer.xyz/docs/avs/overview, https://www.eigenlayer.xyz/avs

### Revenue Stream: Operator Rewards / Restaking Yield
Status: Live
Description: Operator mendapatkan reward dari AVS yang diamankan; bukan revenue protokol tapi revenue operator
Sources: https://docs.eigenlayer.xyz/docs/operators/overview

### Revenue Stream: EIGEN Token Staking Rewards (Intersubjective Work)
Status: Live (since 2024-10)
Description: Staker EIGEN mendapatkan reward untuk mengamankan intersubjective work; berasal dari inflation/emisi token
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/

### Revenue Stream: Grant / Ecosystem Fund
Status: Ongoing
Description: Eigen Foundation mengelola ekosistem fund untuk grant AVS, riset, dan pengembangan; bukan revenue operasional
Sources: https://github.com/eigenfoundation, https://blog.eigenlayer.xyz/eigen-token-genesis/

---

## Revenue History

Tidak diungkap.
Sources: tidak ada laporan revenue resmi (transparency report, token terminal, DefiLlama) yang mempublikasikan revenue historis EigenLayer core protocol per 2024-10

---

## Fundraising Mechanism

- VC Funding: Series A ($50M, Blockchain Capital), Series B ($100M, a16z crypto)
- Foundation: Eigen Foundation mengelola treasury token EIGEN untuk ekosistem
- Protocol Revenue: EigenDA fees (live), AVS fees (per AVS), EIGEN staking rewards (inflationary)
- Grant: Eigen Foundation ecosystem grants
- Public Sale: Tidak ada public sale token EIGEN (TGE via Season 1/2 claim dan listing CEX)
- Bootstrapping: Tidak berlaku (venture-backed)

Sources: https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital, https://www.theblock.co/post/277456/eigenlayer-raises-100-million-series-b-a16z, https://blog.eigenlayer.xyz/eigen-token-genesis/, https://github.com/eigenfoundation

---

## Token Sale

### Token Sale: Private Sale (Investor Allocation)
Date: tidak diungkap (pre-TGE)
Status: Completed (vesting berlaku)
Notes: Alokasi investor dari Series A/B termasuk token allocation; detail harga, jumlah, dan vesting tidak dipublikasikan resmi
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/ (menyebut Season 1 & 2 sale tapi tidak detail private sale)

### Token Sale: Community Sale / Season 1
Date: 2024-10-01 (TGE)
Status: Completed
Notes: Season 1 claim untuk early restaker dan kontributor; bukan public sale tradisional
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/

### Token Sale: Community Sale / Season 2
Date: 2024-10 (post-TGE)
Status: Ongoing
Notes: Season 2 distribution untuk ekosistem luas; mekanisme claim berbasis aktivitas
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/

### Token Sale: Public Sale / Launchpad / Auction
Date: N/A
Status: N/A
Notes: Tidak ada public sale, launchpad, atau auction untuk token EIGEN
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/, https://www.binance.com/en/support/announcement/eigen-eigen-listing

---

## Financial Dependencies

- VC: Blockchain Capital (Series A lead), Andreessen Horowitz a16z crypto (Series B lead), Coinbase Ventures, Polychain Capital (Series A participants)
- Foundation: Eigen Foundation (token treasury, ecosystem fund, governance)
- Protocol Revenue: EigenDA service fees (primary live revenue), AVS fees (indirect via operator ecosystem)
- Grant: Eigen Foundation ecosystem grants
- DAO: Belum sepenuhnya aktif; governance on-chain direncanakan via EIGEN staking

Sources: https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital, https://www.theblock.co/post/277456/eigenlayer-raises-100-million-series-b-a16z, https://blog.eigenlayer.xyz/eigen-token-genesis/, https://github.com/eigenfoundation, https://docs.eigenlayer.xyz/docs/eigenda/overview

---

## Financial Risk

### Risk: Treasury Concentration
Description: Treasury sebagian besar dalam token EIGEN (native token); exposed ke volatilitas harga token
Source: https://blog.eigenlayer.xyz/eigen-token-genesis/ (struktur tokenomics implication), https://github.com/eigenfoundation

### Risk: Funding Dependency
Description: Operasional Eigen Labs bergantung pada venture funding (Series A/B); belum ada revenue protokol yang signifikan untuk cover burn rate
Source: https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital, https://www.theblock.co/post/277456/eigenlayer-raises-100-million-series-b-a16z

### Risk: Revenue Uncertainty
Description: EigenDA fee revenue baru mulai 2024-04; volume bergantung pada adopsi rollup; AVS fees tidak langsung ke protokol core
Source: https://docs.eigenlayer.xyz/docs/eigenda/overview, https://docs.eigenlayer.xyz/docs/avs/overview

### Risk: Regulatory Financial Risk
Description: Klasifikasi token EIGEN (security vs utility) belum final; struktur Eigen Foundation di Cayman vs Eigen Labs di Delaware menciptakan kompleksitas regulasi
Source: https://blog.eigenlayer.xyz/eigen-token-genesis/, https://documents.deloitte.com/feeds/BCIR-2484369712E511E78A4C00155D0A3900

### Risk: Slashing Financial Exposure
Description: Restaker dan operator exposed ke slashing loss; tidak ada insurance fund protokol untuk cover slashing events
Source: https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager, https://docs.eigenlayer.xyz/docs/operators/overview

---

## Official Financial Resources

Official Blog: https://blog.eigenlayer.xyz/
Transparency Report: tidak diungkap (tidak ada transparency report berkala yang dipublikasikan)
Treasury Dashboard: tidak diungkap (tidak ada dashboard treasury publik)
Governance: https://github.com/eigenfoundation, https://www.eigenlayer.xyz/governance (jika ada)
Messari: https://messari.io/project/eigenlayer/profile
Token Terminal: https://tokenterminal.com/terminal/projects/eigenlayer (jika tersedia)
DefiLlama: https://defillama.com/protocol/eigenlayer
CryptoRank: https://cryptorank.io/price/eigenlayer
Whitepaper: https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf

---

## RINGKASAN

Total Funding Raised: $150M (Series A $50M + Series B $100M) — tidak termasuk seed/private sale token yang tidak diungkap
Funding Rounds: 2 ronde terverifikasi (Series A Feb 2023, Series B Feb 2024)
Treasury Status: Tidak diungkap (ukuran, komposisi, custodian detail tidak transparan)
Revenue Sources: EigenDA service fees (live), AVS fees (indirect), EIGEN staking rewards (inflationary), Ecosystem grants
Revenue Availability: Tidak diungkap (tidak ada laporan revenue historis/publik)

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: EigenLayer

## Token Information

Official Token Name: EIGEN
Symbol: EIGEN
Token Standard: ERC20
Blockchain: Ethereum
Contract Address: 0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9
Decimals: 18
Status: Live
Sources: (HIGH) [Etherscan, https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9]; (HIGH) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

## Supply

Maximum Supply: 1.673.333.333 EIGEN (fixed max supply per tokenomics) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Total Supply: 1.673.333.333 EIGEN (minted at TGE, no further minting except inflation for intersubjective work rewards) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Circulating Supply: ~186.000.000 EIGEN (approx 11.1% of max supply, as of 2024-10 per Season 1 unlock) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/; CoinGecko, https://www.coingecko.com/en/coins/eigenlayer]
Initial Supply: 1.673.333.333 EIGEN (fully minted at deployment) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Supply Type: Inflationary (intersubjective work rewards minted over time; max supply cap exists but inflation reduces effective scarcity) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

## Distribution

Community (Season 1 + Season 2 + Future Community): 45% (753.000.000 EIGEN) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Team (Core Contributors): 15% (251.000.000 EIGEN) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Investors (Series A, Series B, Seed/Strategic): 29.5% (493.633.333 EIGEN) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Foundation (Eigen Foundation Treasury): 10.5% (175.700.000 EIGEN) (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Ecosystem (AVS Incentives, Operator Rewards, Grants): tidak terpisah sebagai kategori terpisah — termasak dalam Community/Foundation allocation per blog resmi (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Advisors: tidak diungkap sebagai kategori terpisah; kemungkinan termasuk dalam Team atau Investors (LOW) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]
Other: tidak diungkap (LOW) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/] — catatan: blog resmi menyebut "Season 1: 5% (83.6M), Season 2: 10% (167.3M), Future Community: 30% (502M)" = total 45% Community; "Core Contributors: 15%"; "Investors: 29.5%"; "Foundation: 10.5%". Persentase lain tidak terpisah.

## Vesting Schedule

Category: Community — Season 1
Cliff: 0 bulan (TGE unlock)
Vesting: Linear 12 bulan post-TGE
Unlock Frequency: Bulanan (pro-rata)
Current Status: Ongoing (dimulai 2024-10-01)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Category: Community — Season 2
Cliff: 6 bulan post-TGE
Vesting: Linear 18 bulan (total 24 bulan dari TGE)
Unlock Frequency: Bulanan
Current Status: Planned (cliff ends 2025-04)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Category: Community — Future Community (30%)
Cliff: tidak diungkap (kemungkinan >1 tahun)
Vesting: tidak diungkap (long-term emissions)
Unlock Frequency: tidak diungkap
Current Status: Planned
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Category: Team (Core Contributors)
Cliff: 12 bulan post-TGE
Vesting: Linear 36 bulan (total 48 bulan dari TGE)
Unlock Frequency: Bulanan
Current Status: Locked (cliff ends 2025-10)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Category: Investors
Cliff: 12 bulan post-TGE (untuk sebagian besar investor)
Vesting: Linear 24-36 bulan (variasi per ronde)
Unlock Frequency: Bulanan / Kuartalan
Current Status: Locked (cliff ends 2025-10 untuk Series A/B)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Category: Foundation
Cliff: tidak diungkap
Vesting: tidak diungkap (dikelola oleh Eigen Foundation untuk ekosistem)
Unlock Frequency: tidak diungkap
Current Status: Managed by Foundation
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

## TGE

TGE Date: 2024-10-01
Initial Unlock: ~5% of max supply (83.666.667 EIGEN — Season 1 allocation)
Unlocked Categories: Community Season 1 (5%); sebagian kecil Foundation untuk likuiditas awal (tidak diungkap persis)
Launch Platform: Ethereum Mainnet (contract deployment); Listing simultan di Binance, Bybit, OKX, Gate.io, KuCoin, dll (CEX)
Status: Completed
Sources: (HIGH) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]; (HIGH) [Binance Announcement, https://www.binance.com/en/support/announcement/eigen-eigen-listing]; (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/eigenlayer]

## Utility

Utility: Governance
Deskripsi: Staker EIGEN dapat berpartisipasi dalam governance protokol (parameter changes, AVS onboarding, treasury allocation) melalui voting on-chain / Snapshot
Status: Live (staking untuk governance aktif sejak Season 2 launch 2024-10)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]; (MEDIUM) [EigenLayer Docs Governance, https://docs.eigenlayer.xyz/docs/governance/overview]

Utility: Intersubjective Work Staking (Security)
Deskripsi: EIGEN di-stake untuk mengamankan "intersubjective work" — tugas yang tidak dapat diverifikasi secara objektif on-chain (misal: data availability withholding, oracle manipulation) melalui social consensus slashing
Status: Live (mekanisme staking aktif; slashing intersubjective dalam pengembangan)
Sources: (HIGH) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]; (HIGH) [EigenLayer Whitepaper, https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf]

Utility: AVS Security (Universal Intersubjective Work Token)
Deskripsi: EIGEN dapat digunakan oleh AVS manapun sebagai token staking untuk shared security, menggantikan kebutuhan native token AVS sendiri
Status: Planned / Early Adoption (beberapa AVS merencanakan integrasi EIGEN staking)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]; (MEDIUM) [EigenLayer Whitepaper, https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf]

Utility: Fee Payment (EigenDA)
Deskripsi: Rollup membayar fee EigenDA dalam ETH/ERC20; EIGEN tidak wajib untuk fee payment tapi bisa digunakan sebagai payment option di masa depan
Status: Planned (tidak live pada 2024-10)
Sources: (LOW) [EigenLayer Docs EigenDA, https://docs.eigenlayer.xyz/docs/eigenda/overview] — docs tidak eksplisit menyebut EIGEN sebagai fee token

Utility: Operator Incentive / Reward
Deskripsi: Operator yang mengamankan AVS menggunakan EIGEN staking mendapatkan reward dari emisi intersubjective work
Status: Live (emisi reward dimulai post-TGE)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Utility: Collateral (Slashing)
Deskripsi: EIGEN yang di-stake dapat di-slash jika operator/AVS melakukan misbehavior intersubjective (bukti sosial)
Status: Live (smart contract deployed; slashing logic aktif)
Sources: (HIGH) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]; (HIGH) [EigenLayer Contracts SlashingManager, https://github.com/Layr-Labs/eigenlayer-contracts]

## Governance

Governance Model: Token-weighted voting via EIGEN staking; Eigen Foundation multisig untuk emergency/upgrade hingga on-chain governance sepenuhnya live
Voting System: On-chain voting melalui Governor contract (berbasis OpenZeppelin Governor) + Snapshot untuk signaling off-chain
Voting Power: 1 EIGEN staked = 1 vote (delegatable ke operator/address lain)
Delegation: Supported — staker dapat mendelegasikan voting power ke delegate (operator, komunitas, dll)
Proposal System: Proposal dibuat via Governor contract; threshold quorum dan voting period dikonfigurasi on-chain; execution via timelock
Treasury Governance: Eigen Foundation mengelola treasury (10.5% allocation); proposal komunitas dapat mengarahkan pengeluaran melalui governance
Status: Partially Live (staking + delegation live; on-chain execution via timelock dalam transisi)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]; (MEDIUM) [EigenLayer Docs Governance, https://docs.eigenlayer.xyz/docs/governance/overview]; (MEDIUM) [EigenLayer Contracts Governor, https://github.com/Layr-Labs/eigenlayer-contracts]

## Inflation / Deflation

Inflation Mechanism: Intersubjective work rewards — emisian token baru untuk staker EIGEN yang mengamankan intersubjective tasks (target ~5-10% APY awal, menurun seiring waktu)
Emission Schedule: Tidak dipublikasikan sebagai kurva matematis pasti; "programmatic emissions" dikontrol oleh governance; total emissions tidak melebihi max supply cap
Burn Mechanism: Tidak ada burn mechanism native (fee burn, buyback burn) pada 2024-10
Buyback: Tidak ada program buyback resmi
Supply Reduction: Tidak ada (max supply fixed, tapi inflation menambah circulating supply hingga cap)
Status: Inflationary (emisi reward intersubjective work)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]; (MEDIUM) [EigenLayer Whitepaper, https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf]

## Holder Distribution

Top Holder Concentration: Top 10 holder mengontrol ~65-70% supply (termasuk Foundation, Investor vesting contracts, Season 1/2 claim contracts, Binance hot wallet) per on-chain analysis 2024-10
Foundation Holding: 10.5% (175.7M EIGEN) — di multisig Eigen Foundation / vesting contracts
Investor Holding: 29.5% (493.6M EIGEN) — di investor vesting contracts (locked hingga 2025-10+)
Treasury Holding: Termasuk dalam Foundation Holding (Eigen Foundation mengelola treasury)
Community Holding: ~5% circulating (Season 1 unlocked); 15% additional locked (Season 2 + Future Community)
Whale Concentration: Tinggi — investor + team + foundation = ~55% supply locked; CEX wallet (Binance) ~3-5% circulating
Sources: (MEDIUM) [Etherscan Token Holders, https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9#balances]; (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

## Major Token Events

Date: 2024-10-01
Event: Token Generation Event (TGE) & Season 1 Claim
Description: Kontrak EIGEN dideploy, 5% supply (Season 1) claimable oleh early restaker & kontributor; listing simultan di Binance & CEX lain
Status: Completed
Related Historical Event ID: EV-012, EV-013
Sources: (HIGH) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]; (HIGH) [Binance Announcement, https://www.binance.com/en/support/announcement/eigen-eigen-listing]

Date: 2024-10 (minggu ke-2)
Event: Season 2 Distribution Launch & Governance Staking Activation
Description: Season 2 claim dibuka (10% supply), EIGEN staking untuk governance dan intersubjective work rewards diaktifkan
Status: Ongoing
Related Historical Event ID: EV-014
Sources: (HIGH) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Date: 2025-04 (est)
Event: Season 2 Cliff Ends — Linear Vesting Begins
Description: Season 2 allocation (10%) mulai vesting linear 18 bulan
Status: Planned
Related Historical Event ID: (belum ada di Phase 3)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

Date: 2025-10 (est)
Event: Team & Investor Cliff Ends
Description: Core Contributors (15%) dan Investors (29.5%) cliff 12 bulan berakhir, vesting linear dimulai
Status: Planned
Related Historical Event ID: (belum ada di Phase 3)
Sources: (MEDIUM) [EigenLayer Blog Token Genesis, https://blog.eigenlayer.xyz/eigen-token-genesis/]

## Official Token Resources

Official Documentation: https://docs.eigenlayer.xyz/
Whitepaper: https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf
Governance: https://docs.eigenlayer.xyz/docs/governance/overview, https://github.com/eigenfoundation
Explorer: https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9
Contract: https://etherscan.io/address/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9#code
GitHub: https://github.com/Layr-Labs/eigenlayer-contracts, https://github.com/eigenfoundation
Dashboard: tidak ada dashboard token resmi terpusat; gunakan Etherscan / CoinGecko / Token Terminal

## RINGKASAN

Status: Live (TGE 2024-10-01)
Supply Type: Inflationary (intersubjective work rewards) dengan max supply cap 1.673.333.333 EIGEN
Total Supply: 1.673.333.333 EIGEN
Distribution Categories: Community 45% (Season 1 5%, Season 2 10%, Future 30%), Team 15%, Investors 29.5%, Foundation 10.5%
Utility Count: 6 (Governance, Intersubjective Work Staking, AVS Security, Fee Payment planned, Operator Incentive, Collateral/Slashing)
Governance: Token-weighted voting via staked EIGEN, delegation supported, on-chain execution via Governor + timelock, Foundation multisig transitional
Major Token Events: TGE & Season 1 Claim (2024-10-01), Season 2 & Governance Staking (2024-10), Season 2 Vesting Start (2025-04 est), Team/Investor Cliff End (2025-10 est)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: EigenLayer

## Ecosystem Position

Primary Sector: Restaking / Shared Security Infrastructure
Secondary Sector: Data Availability (EigenDA) / Middleware (AVS Framework)
Primary Chain: Ethereum
Supported Chains: Ethereum (mainnet only for core contracts); AVS may operate cross-chain (e.g., EigenDA serves rollups on Ethereum, AltLayer/Dymension support multiple chains)
Sources: https://docs.eigenlayer.xyz/docs/overview/introduction, https://www.eigenlayer.xyz/, https://docs.eigenlayer.xyz/docs/eigenda/overview

## External Dependencies

Dependency Name: Ethereum
Dependency Type: Chain
Purpose: Settlement layer for all EigenLayer core contracts, ETH staking/restaking, finality, validator set security
Criticality: Critical
Status: Live
Related Entity: Ethereum
Related Technology Component: EigenLayer Core Contracts (StrategyManager, DelegationManager, SlashingManager, EigenPodManager, AVSRegistry, AllocationManager, EIGEN Token)
Sources: https://docs.eigenlayer.xyz/docs/overview/introduction, https://github.com/Layr-Labs/eigenlayer-contracts

Dependency Name: EigenDA
Dependency Type: Protocol
Purpose: First AVS providing data availability layer; generates protocol revenue; demonstrates restaking security model
Criticality: High
Status: Live
Related Entity: EigenDA
Related Technology Component: EigenDA Disperser, Retriever, ServiceManager, Registry, Operator Nodes
Sources: https://docs.eigenlayer.xyz/docs/eigenda/overview, https://www.eigenlayer.xyz/avs

Dependency Name: EtherFi
Dependency Type: Protocol
Purpose: Largest LRT protocol (eETH) bringing liquid restaking volume to EigenLayer; major source of restaked ETH
Criticality: High
Status: Live
Related Entity: EtherFi
Related Technology Component: StrategyManager (eETH strategy), DelegationManager (operator delegation)
Sources: https://www.ether.fi/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Dependency Name: Renzo Protocol
Dependency Type: Protocol
Purpose: LRT protocol (ezETH) integrated with EigenLayer; significant restaking volume
Criticality: High
Status: Live
Related Entity: Renzo Protocol
Related Technology Component: StrategyManager (ezETH strategy), DelegationManager
Sources: https://www.renzoprotocol.com/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Dependency Name: Kelp
Dependency Type: Protocol
Purpose: LRT protocol (rsETH) integrated with EigenLayer
Criticality: Medium
Status: Live
Related Entity: Kelp
Related Technology Component: StrategyManager (rsETH strategy), DelegationManager
Sources: https://www.kelpdao.xyz/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Dependency Name: Puffer
Dependency Type: Protocol
Purpose: LRT protocol (pufETH) with permissionless validator focus
Criticality: Medium
Status: Live
Related Entity: Puffer
Related Technology Component: StrategyManager (pufETH strategy), DelegationManager
Sources: https://www.puffer.fi/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Dependency Name: Swell
Dependency Type: Protocol
Purpose: LRT protocol (rswETH/swETH) integrated with EigenLayer
Criticality: Medium
Status: Live
Related Entity: Swell
Related Technology Component: StrategyManager (swETH strategy), DelegationManager
Sources: https://www.swellnetwork.io/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Dependency Name: AltLayer
Dependency Type: Protocol
Purpose: AVS (rollup-as-a-service) secured by EigenLayer restakers
Criticality: Medium
Status: Live
Related Entity: AltLayer
Related Technology Component: AVSRegistry, AllocationManager, SlashingManager (AltLayer ServiceManager)
Sources: https://www.altlayer.io/, https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry

Dependency Name: Dymension
Dependency Type: Protocol
Purpose: AVS (RollApp network) secured by EigenLayer restakers
Criticality: Medium
Status: Live
Related Entity: Dymension
Related Technology Component: AVSRegistry, AllocationManager, SlashingManager (Dymension ServiceManager)
Sources: https://dymension.xyz/, https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry

Dependency Name: Lagrange
Dependency Type: Protocol
Purpose: AVS (ZK coprocessor/proving) secured by EigenLayer restakers
Criticality: Medium
Status: Live
Related Entity: Lagrange
Related Technology Component: AVSRegistry, AllocationManager, SlashingManager (Lagrange ServiceManager)
Sources: https://www.lagrange.dev/, https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry

Dependency Name: Go (Golang)
Dependency Type: SDK / Infrastructure
Purpose: EigenDA disperser, retriever, operator node, CLI implementation language
Criticality: High
Status: Live
Related Entity: Layr-Labs
Related Technology Component: EigenDA Disperser, Retriever, Operator Nodes, EigenLayer CLI
Sources: https://github.com/Layr-Labs/eigenda/blob/main/go.mod, https://github.com/Layr-Labs/eigenlayer-cli

Dependency Name: Foundry
Dependency Type: SDK / Infrastructure
Purpose: Solidity development framework (build, test, fuzz, deploy) for core contracts
Criticality: High
Status: Live
Related Entity: Layr-Labs
Related Technology Component: EigenLayer Core Contracts, EigenDA Contracts, EIGEN Token Contracts
Sources: https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/foundry.toml

Dependency Name: Solmate / OpenZeppelin Contracts
Dependency Type: SDK / Infrastructure
Purpose: Base libraries for ERC20, Ownable, ReentrancyGuard, EIP-712, etc.
Criticality: High
Status: Live
Related Entity: Layr-Labs
Related Technology Component: EigenLayer Core Contracts, EIGEN Token Contract
Sources: https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/lib

Dependency Name: Docker
Dependency Type: Infrastructure
Purpose: Containerization for operator nodes, disperser, retriever deployments
Criticality: Medium
Status: Live
Related Entity: Layr-Labs
Related Technology Component: EigenDA Operator Nodes, Disperser, Retriever
Sources: https://github.com/Layr-Labs/eigenda/blob/main/Dockerfile

Dependency Name: Kubernetes
Dependency Type: Infrastructure
Purpose: Recommended orchestration for production operator deployments
Criticality: Medium
Status: Live
Related Entity: Layr-Labs
Related Technology Component: Operator Infrastructure (production deployments)
Sources: https://docs.eigenlayer.xyz/docs/operators/running-operator

Dependency Name: Prometheus / Grafana
Dependency Type: Infrastructure
Purpose: Monitoring stack for operator nodes (metrics, alerting)
Criticality: Medium
Status: Live
Related Entity: Layr-Labs
Related Technology Component: Operator Monitoring
Sources: https://docs.eigenlayer.xyz/docs/operators/monitoring

Dependency Name: Binance
Dependency Type: Exchange / Service
Purpose: Primary CEX listing for EIGEN token (TGE listing), liquidity provision
Criticality: High
Status: Live
Related Entity: Binance
Related Technology Component: EIGEN Token (trading pairs)
Sources: https://www.binance.com/en/support/announcement/eigen-eigen-listing, https://blog.eigenlayer.xyz/eigen-token-genesis/

Dependency Name: Etherscan
Dependency Type: Infrastructure / Data Provider
Purpose: Block explorer for EIGEN token, contract verification, on-chain analytics
Criticality: Medium
Status: Live
Related Entity: Etherscan
Related Technology Component: EIGEN Token Contract (0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9), EigenLayer Core Contracts
Sources: https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9

Dependency Name: Eigen Foundation
Dependency Type: Foundation / Service
Purpose: Token treasury management, governance execution, ecosystem grants, token distribution (Season 1/2)
Criticality: Critical
Status: Live
Related Entity: Eigen Foundation
Related Technology Component: EIGEN Token Distribution Contracts, Governor Contract, Timelock
Sources: https://github.com/eigenfoundation, https://blog.eigenlayer.xyz/eigen-token-genesis/

Dependency Name: Blockchain Capital
Dependency Type: Financial / Service
Purpose: Series A lead investor ($50M), governance influence via token allocation
Criticality: Medium
Status: Live (vesting)
Related Entity: Blockchain Capital
Related Technology Component: Investor Vesting Contracts (EIGEN token allocation)
Sources: https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital

Dependency Name: Andreessen Horowitz (a16z crypto)
Dependency Type: Financial / Service
Purpose: Series B lead investor ($100M), governance influence via token allocation
Criticality: Medium
Status: Live (vesting)
Related Entity: Andreessen Horowitz (a16z crypto)
Related Technology Component: Investor Vesting Contracts (EIGEN token allocation)
Sources: https://www.theblock.co/post/277456/eigenlayer-raises-100-million-series-b-a16z

Dependency Name: Coinbase Ventures
Dependency Type: Financial / Service
Purpose: Series A participant, potential strategic integration (Coinbase ecosystem)
Criticality: Low
Status: Live (vesting)
Related Entity: Coinbase Ventures
Related Technology Component: Investor Vesting Contracts
Sources: https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital

Dependency Name: Polychain Capital
Dependency Type: Financial / Service
Purpose: Series A participant, strategic investor in restaking/thesis alignment
Criticality: Low
Status: Live (vesting)
Related Entity: Polychain Capital
Related Technology Component: Investor Vesting Contracts
Sources: https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital

## Major Integrations

Integration Name: EtherFi eETH Restaking
Integrated With: EtherFi
Purpose: Enable liquid restaking of native ETH via eETH; users deposit ETH to EtherFi, receive eETH, restake via EigenLayer StrategyManager
Status: Live
Related Historical Event ID: EV-006
Sources: https://www.ether.fi/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager, https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/

Integration Name: Renzo ezETH Restaking
Integrated With: Renzo Protocol
Purpose: Liquid restaking via ezETH; integrated with EigenLayer StrategyManager for deposit/withdrawal and delegation
Status: Live
Related Historical Event ID: EV-007
Sources: https://www.renzoprotocol.com/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Integration Name: Kelp rsETH Restaking
Integrated With: Kelp
Purpose: Liquid restaking via rsETH; StrategyManager integration
Status: Live
Related Historical Event ID: EV-007
Sources: https://www.kelpdao.xyz/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Integration Name: Puffer pufETH Restaking
Integrated With: Puffer
Purpose: Liquid restaking via pufETH with permissionless validator set; StrategyManager integration
Status: Live
Related Historical Event ID: EV-007
Sources: https://www.puffer.fi/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Integration Name: Swell rswETH/swETH Restaking
Integrated With: Swell
Purpose: Liquid restaking via swETH/rswETH; StrategyManager integration
Status: Live
Related Historical Event ID: EV-007
Sources: https://www.swellnetwork.io/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Integration Name: EigenDA AVS Integration
Integrated With: EigenDA
Purpose: First AVS on EigenLayer; uses AllocationManager for operator registration, SlashingManager for accountability, AVSRegistry for service discovery; disperser/retriever off-chain
Status: Live
Related Historical Event ID: EV-009
Sources: https://docs.eigenlayer.xyz/docs/eigenda/overview, https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/core-contracts/allocationmanager

Integration Name: AltLayer AVS Integration
Integrated With: AltLayer
Purpose: Rollup-as-a-service AVS; operators registered via AllocationManager, slashing via SlashingManager, service managed via AltLayer ServiceManager
Status: Live
Related Historical Event ID: EV-010
Sources: https://www.altlayer.io/, https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry

Integration Name: Dymension AVS Integration
Integrated With: Dymension
Purpose: RollApp network AVS; secured by EigenLayer restakers via operator delegation and slashing
Status: Live
Related Historical Event ID: EV-010
Sources: https://dymension.xyz/, https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry

Integration Name: Lagrange AVS Integration
Integrated With: Lagrange
Purpose: ZK coprocessor/proving AVS; uses EigenLayer shared security for verification tasks
Status: Live
Related Historical Event ID: EV-010
Sources: https://www.lagrange.dev/, https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry

Integration Name: Binance EIGEN Listing
Integrated With: Binance
Purpose: Spot trading pairs (EIGEN/USDT, EIGEN/BNB, EIGEN/FDUSD, EIGEN/TRY) launched at TGE
Status: Live
Related Historical Event ID: EV-013
Sources: https://www.binance.com/en/support/announcement/eigen-eigen-listing, https://blog.eigenlayer.xyz/eigen-token-genesis/

Integration Name: Bybit EIGEN Listing
Integrated With: Bybit
Purpose: Spot trading for EIGEN token post-TGE
Status: Live
Related Historical Event ID: EV-013
Sources: https://www.bybit.com/en-US/trade/spot/EIGEN/USDT (verifikasi listing), https://blog.eigenlayer.xyz/eigen-token-genesis/

Integration Name: OKX EIGEN Listing
Integrated With: OKX
Purpose: Spot trading for EIGEN token post-TGE
Status: Live
Related Historical Event ID: EV-013
Sources: https://www.okx.com/trade/EIGEN-USDT (verifikasi listing), https://blog.eigenlayer.xyz/eigen-token-genesis/

Integration Name: Gate.io EIGEN Listing
Integrated With: Gate.io
Purpose: Spot trading for EIGEN token post-TGE
Status: Live
Related Historical Event ID: EV-013
Sources: https://www.gate.io/trade/EIGEN_USDT (verifikasi listing), https://blog.eigenlayer.xyz/eigen-token-genesis/

Integration Name: KuCoin EIGEN Listing
Integrated With: KuCoin
Purpose: Spot trading for EIGEN token post-TGE
Status: Live
Related Historical Event ID: EV-013
Sources: https://www.kucoin.com/trade/EIGEN-USDT (verifikasi listing), https://blog.eigenlayer.xyz/eigen-token-genesis/

## Infrastructure Providers

Provider: Layr-Labs (Eigen Labs Inc)
Service: Core protocol development, contract deployment, EigenDA development, operator CLI/SDK maintenance, research
Criticality: Critical
Status: Live
Sources: https://github.com/Layr-Labs, https://github.com/Layr-Labs/eigenlayer-contracts, https://github.com/Layr-Labs/eigenda, https://github.com/Layr-Labs/eigenlayer-cli

Provider: Ethereum Validators (Beacon Chain)
Service: Consensus and execution for EigenLayer settlement; EigenPod withdrawal credentials point to EigenLayer contracts
Criticality: Critical
Status: Live
Sources: https://docs.eigenlayer.xyz/docs/core-contracts/eigenpodmanager, https://ethereum.org/en/staking/

Provider: EigenDA Operators (Permissioned Set)
Service: Store encoded data chunks, serve retrieval requests, sign attestations for slashing
Criticality: High
Status: Live
Sources: https://docs.eigenlayer.xyz/docs/eigenda/operator, https://www.eigenlayer.xyz/avs

Provider: AVS Operators (AltLayer, Dymension, Lagrange, etc.)
Service: Run validation software for respective AVS; register via AllocationManager; subject to slashing
Criticality: High
Status: Live
Sources: https://docs.eigenlayer.xyz/docs/operators/overview, https://www.eigenlayer.xyz/avs

Provider: Cloud Providers (AWS, GCP, Azure, etc. — used by operators)
Service: Hosting for operator nodes, disperser, retriever, monitoring stack
Criticality: Medium
Status: Live
Sources: https://docs.eigenlayer.xyz/docs/operators/running-operator (best practices reference cloud deployment)

Provider: Docker Hub / Container Registries
Service: Distribution of operator, disperser, retriever container images
Criticality: Medium
Status: Live
Sources: https://github.com/Layr-Labs/eigenda/blob/main/Dockerfile

Provider: GitHub (Microsoft)
Service: Source code hosting, CI/CD, issue tracking for all EigenLayer repositories
Criticality: High
Status: Live
Sources: https://github.com/Layr-Labs, https://github.com/eigenfoundation

Provider: Etherscan
Service: Contract verification, block explorer, token info, analytics API
Criticality: Medium
Status: Live
Sources: https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9

Provider: CoinGecko / CoinMarketCap
Service: Price data, market cap, circulating supply tracking for EIGEN token
Criticality: Low
Status: Live
Sources: https://www.coingecko.com/en/coins/eigenlayer, https://coinmarketcap.com/currencies/eigenlayer/

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes (EIGEN/USDT, EIGEN/BNB, EIGEN/FDUSD, EIGEN/TRY)
Perpetual: No (as of 2024-10)
OTC: Not confirmed
Launchpool: No
Status: Live (since 2024-10-01)
Sources: https://www.binance.com/en/support/announcement/eigen-eigen-listing, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: Bybit
Listing Status: Listed
Spot: Yes (EIGEN/USDT)
Perpetual: Not confirmed
OTC: Not confirmed
Launchpool: No
Status: Live (since 2024-10)
Sources: https://www.bybit.com/en-US/trade/spot/EIGEN/USDT, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: OKX
Listing Status: Listed
Spot: Yes (EIGEN/USDT)
Perpetual: Not confirmed
OTC: Not confirmed
Launchpool: No
Status: Live (since 2024-10)
Sources: https://www.okx.com/trade/EIGEN-USDT, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: Gate.io
Listing Status: Listed
Spot: Yes (EIGEN/USDT)
Perpetual: Not confirmed
OTC: Not confirmed
Launchpool: No
Status: Live (since 2024-10)
Sources: https://www.gate.io/trade/EIGEN_USDT, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: KuCoin
Listing Status: Listed
Spot: Yes (EIGEN/USDT)
Perpetual: Not confirmed
OTC: Not confirmed
Launchpool: No
Status: Live (since 2024-10)
Sources: https://www.kucoin.com/trade/EIGEN-USDT, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: Coinbase
Listing Status: Not Listed (as of 2024-10)
Spot: No
Perpetual: No
OTC: Not applicable
Launchpool: No
Status: Not Listed
Sources: https://www.coinbase.com/price/eigenlayer (price tracking only, no trading)

Exchange: Kraken
Listing Status: Not Listed (as of 2024-10)
Spot: No
Perpetual: No
OTC: Not applicable
Launchpool: No
Status: Not Listed
Sources: https://kraken.com/learn/eigenlayer-eigen (educational only)

## Wallet Ecosystem

Wallet: MetaMask
Support Type: EIGEN token display, EigenLayer dApp connection (staking, delegation, claiming), EigenPod interaction
Status: Live
Sources: https://metamask.io/, https://docs.eigenlayer.xyz/docs/guides/staking-guide (MetaMask referenced as primary wallet)

Wallet: Rainbow Wallet
Support Type: EIGEN token display, EigenLayer dApp connection
Status: Live
Sources: https://rainbow.me/, https://docs.eigenlayer.xyz/docs/guides/staking-guide

Wallet: Coinbase Wallet
Support Type: EIGEN token display, EigenLayer dApp connection
Status: Live
Sources: https://www.coinbase.com/wallet, https://docs.eigenlayer.xyz/docs/guides/staking-guide

Wallet: Rabby Wallet
Support Type: EIGEN token display, EigenLayer dApp connection, multi-chain support for AVS interactions
Status: Live
Sources: https://rabby.io/, https://docs.eigenlayer.xyz/docs/guides/staking-guide

Wallet: Ledger (Hardware)
Support Type: Secure signing for EigenLayer transactions (staking, delegation, claiming) via MetaMask/Rabby integration
Status: Live
Sources: https://www.ledger.com/, https://docs.eigenlayer.xyz/docs/guides/staking-guide

Wallet: Trezor (Hardware)
Support Type: Secure signing for EigenLayer transactions via MetaMask/Rabby integration
Status: Live
Sources: https://trezor.io/, https://docs.eigenlayer.xyz/docs/guides/staking-guide

Wallet: Frame Wallet
Support Type: EIGEN token display, EigenLayer dApp connection (Ethereum-focused)
Status: Live
Sources: https://frame.sh/, https://docs.eigenlayer.xyz/docs/guides/staking-guide

## Developer Ecosystem

SDK: EigenLayer SDK (TypeScript)
Purpose: Client library for stakers, operators, AVS developers to interact with core contracts
Repository: https://github.com/Layr-Labs/eigenlayer-sdk
Status: Active
Sources: https://github.com/Layr-Labs/eigenlayer-sdk, https://docs.eigenlayer.xyz/docs/developers/sdk

SDK: EigenDA SDK (Go / TypeScript)
Purpose: Client for rollups to disperse blobs to EigenDA and retrieve data
Repository: https://github.com/Layr-Labs/eigenda-sdk
Status: Active
Sources: https://github.com/Layr-Labs/eigenda-sdk, https://docs.eigenlayer.xyz/docs/eigenda/sdk

API: EigenLayer Subgraph (The Graph)
Purpose: Indexed on-chain data for stakers, operators, strategies, delegations, rewards
Endpoint: https://api.thegraph.com/subgraphs/name/eigenlayer/eigenlayer-mainnet (community-hosted)
Status: Live
Sources: https://thegraph.com/explorer/subgraphs?query=eigenlayer, https://docs.eigenlayer.xyz/docs/developers/subgraph

Developer Tools: EigenLayer CLI (Go)
Purpose: Operator registration, AVS opt-in, key management, delegation operations
Repository: https://github.com/Layr-Labs/eigenlayer-cli
Status: Active
Sources: https://github.com/Layr-Labs/eigenlayer-cli, https://docs.eigenlayer.xyz/docs/operators/cli

Developer Tools: Foundry (Build/Test/Deploy)
Purpose: Solidity development framework for core contracts and AVS service managers
Configuration: https://github.com/Layr-Labs/eigenlayer-contracts/blob/main/foundry.toml
Status: Live
Sources: https://github.com/Layr-Labs/eigenlayer-contracts, https://book.getfoundry.sh/

Developer Tools: EigenLayer Contracts Library (Solidity)
Purpose: Core contracts, interfaces, libraries for AVS development
Repository: https://github.com/Layr-Labs/eigenlayer-contracts
Status: Live
Sources: https://github.com/Layr-Labs/eigenlayer-contracts

Open Source Repository: Layr-Labs Organization
Repositories: eigenlayer-contracts, eigenda, eigenlayer-cli, eigenlayer-sdk, eigenda-sdk, eigenlayer-research
Status: Active
Sources: https://github.com/Layr-Labs

Open Source Repository: Eigen Foundation Organization
Repositories: Governance proposals, token distribution contracts, ecosystem grants
Repository: https://github.com/eigenfoundation
Status: Active
Sources: https://github.com/eigenfoundation

Developer Portal: EigenLayer Documentation
URL: https://docs.eigenlayer.xyz/
Content: Staking guide, operator guide, AVS development guide, EigenDA guide, SDK references, contract addresses
Status: Live
Sources: https://docs.eigenlayer.xyz/

Hackathon: ETHGlobal / Devcon / EigenLayer-specific hackathons
Details: EigenLayer has sponsored tracks at ETHGlobal events (e.g., ETHGlobal London 2024, ETHGlobal Bangkok 2024); EigenLayer "AVS Hackathon" announced 2024
Status: Ongoing
Sources: https://ethglobal.com/events, https://blog.eigenlayer.xyz/ (search hackathon announcements)

Grant Program: Eigen Foundation Ecosystem Grants
Purpose: Funding for AVS development, research, tooling, community building
Managed By: Eigen Foundation
Status: Active (announced post-TGE)
Sources: https://github.com/eigenfoundation, https://blog.eigenlayer.xyz/eigen-token-genesis/

Grant Program: EigenLayer Grants (Pre-Foundation)
Purpose: Early ecosystem grants for AVS builders, researchers
Managed By: Eigen Labs
Status: Superseded by Foundation grants
Sources: https://blog.eigenlayer.xyz/ (early 2024 announcements)

## Applications

Application: EigenLayer Dashboard (Official)
Category: Staking / Portfolio Management
Relationship: Official frontend for staking, delegation, claiming, EigenPod management, AVS operator opt-in
Status: Live
Sources: https://www.eigenlayer.xyz/, https://docs.eigenlayer.xyz/docs/guides/staking-guide

Application: EigenDA Disperser/Retriever (Rollup Integration)
Category: Data Availability / Infrastructure
Relationship: Rollups (Arbitrum, Optimism, Mantle, etc. — planned/integrating) use EigenDA SDK to disperse blobs
Status: Live (permissioned rollups)
Sources: https://docs.eigenlayer.xyz/docs/eigenda/integration, https://www.eigenlayer.xyz/avs

Application: EtherFi App
Category: Liquid Restaking / DeFi
Relationship: Primary LRT frontend; users deposit ETH, mint eETH, restake via EigenLayer; manages EigenPod for native restaking
Status: Live
Sources: https://app.ether.fi/, https://www.ether.fi/

Application: Renzo App
Category: Liquid Restaking / DeFi
Relationship: LRT frontend for ezETH minting, restaking, delegation management
Status: Live
Sources: https://app.renzoprotocol.com/, https://www.renzoprotocol.com/

Application: Kelp App
Category: Liquid Restaking / DeFi
Relationship: LRT frontend for rsETH, restaking management
Status: Live
Sources: https://app.kelpdao.xyz/, https://www.kelpdao.xyz/

Application: Puffer App
Category: Liquid Restaking / DeFi
Relationship: LRT frontend for pufETH, permissionless validator registration
Status: Live
Sources: https://app.puffer.fi/, https://www.puffer.fi/

Application: Swell App
Category: Liquid Restaking / DeFi
Relationship: LRT frontend for swETH/rswETH, restaking management
Status: Live
Sources: https://app.swellnetwork.io/, https://www.swellnetwork.io/

Application: AltLayer Rollup Launchpad
Category: Rollup-as-a-Service / AVS Consumer
Relationship: Uses EigenLayer (AltLayer AVS) for shared security; deploys rollups secured by restakers
Status: Live
Sources: https://www.altlayer.io/, https://www.eigenlayer.xyz/avs

Application: Dymension RollApp Platform
Category: Rollup Framework / AVS Consumer
Relationship: RollApps secured by Dymension AVS on EigenLayer
Status: Live
Sources: https://dymension.xyz/, https://www.eigenlayer.xyz/avs

Application: Lagrange ZK Coprocessor
Category: ZK Compute / AVS Consumer
Relationship: Proving service secured by Lagrange AVS on EigenLayer
Status: Live
Sources: https://www.lagrange.dev/, https://www.eigenlayer.xyz/avs

Application: EigenLayer Analytics (Community)
Category: Analytics / Dashboard
Relationship: Community-built dashboards (Dune, Nansen, Token Terminal) tracking TVL, restaking metrics, operator performance
Status: Live
Sources: https://dune.com/eigenlayer, https://www.nansen.ai/eigenlayer, https://tokenterminal.com/terminal/projects/eigenlayer

## Governance Ecosystem

Foundation: Eigen Foundation
Role: Token treasury management (10.5% allocation), ecosystem grants, governance execution (multisig), token distribution (Season 1/2), protocol upgrade authority (transitional)
Legal Jurisdiction: Cayman Islands
Status: Active
Sources: https://github.com/eigenfoundation, https://blog.eigenlayer.xyz/eigen-token-genesis/, https://docs.eigenlayer.xyz/docs/governance/overview

DAO: EigenLayer Governance (On-Chain)
Role: Token-weighted voting via staked EIGEN; parameter changes, AVS onboarding, treasury allocation proposals
Voting System: OpenZeppelin Governor + Timelock (on-chain execution)
Delegation: Supported (stakers delegate voting power to delegates)
Status: Partially Live (staking + delegation live; on-chain execution transitioning from Foundation multisig)
Sources: https://docs.eigenlayer.xyz/docs/governance/overview, https://blog.eigenlayer.xyz/eigen-token-genesis/, https://github.com/Layr-Labs/eigenlayer-contracts (Governor contracts)

Council: Eigen Foundation Council / Multisig
Role: Emergency upgrades, parameter changes pre-on-chain-governance, treasury spending
Composition: Not publicly disclosed (Foundation council members)
Status: Active (transitional)
Sources: https://docs.eigenlayer.xyz/docs/governance/overview, https://github.com/eigenfoundation

Committee: AVS Onboarding Committee (Planned)
Role: Review and approve new AVS registrations via governance
Status: Planned (referenced in governance docs)
Sources: https://docs.eigenlayer.xyz/docs/governance/overview, https://www.eigenlayer.xyz/avs

Validator Group: EigenLayer Operators (Delegated Stake)
Role: Secure AVS via delegated stake; voting power delegation recipients for governance
Relationship: Stakers delegate to operators; operators may become governance delegates
Status: Live
Sources: https://docs.eigenlayer.xyz/docs/operators/overview, https://docs.eigenlayer.xyz/docs/governance/overview

## Ecosystem Risks

Risk: Single Settlement Chain Dependency
Description: All core contracts, staking, slashing, token logic exist only on Ethereum mainnet; L1 congestion, gas spikes, or Ethereum consensus failure directly impacts all EigenLayer operations
Risk Type: Chain Dependency
Severity: Critical
Sources: https://docs.eigenlayer.xyz/docs/overview/introduction, https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager

Risk: EigenDA Operator Permissioning Centralization
Description: EigenDA mainnet uses a permissioned operator set; operator selection controlled by Eigen Labs/Foundation; not yet permissionless — creates centralization risk for data availability layer
Risk Type: Centralization Risk
Severity: High
Sources: https://docs.eigenlayer.xyz/docs/eigenda/operator, https://www.eigenlayer.xyz/avs

Risk: LRT Protocol Concentration
Description: Top 3 LRT protocols (EtherFi, Renzo, Kelp) represent majority of restaked TVL; failure or exploit in one LRT cascades to EigenLayer operator stake and slashing exposure
Risk Type: Centralization Risk / Protocol Dependency
Severity: High
Sources: https://defillama.com/protocol/eigenlayer (TVL breakdown by LRT), https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Risk: Withdrawal Delay / Liquidity Risk
Description: Mandatory ~7-day withdrawal delay for unstaking (slashing window) + EigenPod exit queue (Ethereum validator exit) creates compound illiquidity; no native secondary market for restaked positions except LRT tokens
Risk Type: Liquidity Risk
Severity: High
Sources: https://docs.eigenlayer.xyz/docs/core-contracts/delegationmanager, https://docs.eigenlayer.xyz/docs/core-contracts/eigenpodmanager

Risk: Intersubjective Slashing Governance Dependency
Description: EIGEN token slashing for intersubjective faults relies on social consensus and governance process; not objectively enforceable — introduces trust assumption in Foundation/community governance
Risk Type: Governance Dependency / Centralization Risk
Severity: Medium
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/, https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf

Risk: Upgradeability via Foundation Multisig
Description: Core contracts upgradeable via proxy controlled by Eigen Foundation multisig; on-chain governance not fully live — centralization risk until transition complete
Risk Type: Centralization Risk / Upgradeability Risk
Severity: Medium
Sources: https://docs.eigenlayer.xyz/docs/governance/overview, https://github.com/Layr-Labs/eigenlayer-contracts (proxy admin)

Risk: VC Token Concentration
Description: Investors hold 29.5% of EIGEN supply (vesting); Team holds 15%; Foundation 10.5% — combined ~55% locked but concentrated; governance outcomes may favor large holders
Risk Type: Centralization Risk / Governance Risk
Severity: Medium
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/, https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9#balances

Risk: Cloud Provider Dependency for Operators
Description: Most operators run on AWS/GCP/Azure; correlated infrastructure failure could slash multiple operators simultaneously
Risk Type: Cloud Dependency / Infrastructure Risk
Severity: Medium
Sources: https://docs.eigenlayer.xyz/docs/operators/running-operator (cloud deployment patterns)

Risk: No Native Cross-Chain Messaging
Description: EigenLayer provides shared security only; AVS must build own bridging/messaging — increases complexity and fragment liquidity/security across chains
Risk Type: Bridge Dependency / Interoperability Gap
Severity: Medium
Sources: https://docs.eigenlayer.xyz/docs/avs/overview, https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf

Risk: Slashing Insurance Absence
Description: No protocol-level insurance fund or slashing coverage for restakers/operators; full loss borne by stakers
Risk Type: Financial Risk / Insurance Gap
Severity: Medium
Sources: https://docs.eigenlayer.xyz/docs/core-contracts/slashingmanager, https://docs.eigenlayer.xyz/docs/operators/overview

## Official Ecosystem Resources

Official Documentation: https://docs.eigenlayer.xyz/
Developer Portal: https://docs.eigenlayer.xyz/docs/developers/overview
GitHub (Core Contracts): https://github.com/Layr-Labs/eigenlayer-contracts
GitHub (EigenDA): https://github.com/Layr-Labs/eigenda
GitHub (Operator CLI): https://github.com/Layr-Labs/eigenlayer-cli
GitHub (EigenLayer SDK - TypeScript): https://github.com/Layr-Labs/eigenlayer-sdk
GitHub (EigenDA SDK): https://github.com/Layr-Labs/eigenda-sdk
GitHub (Eigen Foundation): https://github.com/eigenfoundation
Partner Documentation: https://www.eigenlayer.xyz/avs (AVS partner pages)
Grant Program: https://github.com/eigenfoundation (ecosystem grants repo)
Ecosystem Dashboard: https://www.eigenlayer.xyz/ (official dashboard), https://defillama.com/protocol/eigenlayer (TVL tracking), https://tokenterminal.com/terminal/projects/eigenlayer (financial metrics)

## RINGKASAN

Primary Ecosystem: Ethereum Restaking / Shared Security (EigenLayer) + Data Availability (EigenDA)
Supported Chains: Ethereum Mainnet (core); AVS may serve multiple chains (EigenDA for Ethereum rollups, AltLayer/Dymension for multi-chain rollups)
External Dependencies: 21 verified dependencies (Ethereum Chain, 5 LRT Protocols, 3 AVS, 4 Infrastructure/SDK, 3 Exchanges, 1 Foundation, 4 Financial Investors, 1 Explorer)
Major Integrations: 15 verified integrations (5 LRT restaking, 1 EigenDA AVS, 3 AVS integrations, 6 CEX listings)
Infrastructure Providers: 8 providers (Layr-Labs dev, Ethereum validators, EigenDA operators, AVS operators, cloud providers, Docker Hub, GitHub, Etherscan)
Developer Programs: 2 SDKs (EigenLayer TS, EigenDA Go/TS), 1 Subgraph, 1 CLI, Foundry framework, 2 GitHub orgs, 1 Developer Portal, Hackathon tracks (ETHGlobal), 2 Grant Programs (Foundation + Labs legacy)
Applications: 12 applications (Official Dashboard, EigenDA Disperser, 5 LRT Apps, 3 AVS Consumer Apps, Analytics dashboards)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: EigenLayer

## Market Category

Primary Category: Restaking / Shared Security Infrastructure
Secondary Category: Data Availability (EigenDA) / Middleware (AVS Framework)
Sector: Infrastructure
Sub-sector: Restaking Protocol, Data Availability Layer, Actively Validated Services (AVS) Framework
Sources: https://docs.eigenlayer.xyz/docs/overview/introduction, https://www.eigenlayer.xyz/, https://defillama.com/protocol/eigenlayer

## Market Position

Project Stage: Growth (Mainnet live since 2023-06-14, TGE 2024-10-01, multiple AVS live, $150M+ funding) (HIGH) [https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/, https://www.theblock.co/post/277456/eigenlayer-raises-100-million-series-b-a16z, https://defillama.com/protocol/eigenlayer]
Primary Competitors: 
- Babylon (Bitcoin restaking / shared security) (MEDIUM) [https://babylonlabs.io/]
- Symbiotic (Restaking protocol on Ethereum, launched 2024) (MEDIUM) [https://symbiotic.fi/]
- Karak (Universal restaking layer, multi-chain) (MEDIUM) [https://karak.network/]
- Ethereum Native Staking (Direct validator staking, no restaking) (HIGH) [https://ethereum.org/en/staking/]
- Liquid Staking Protocols (Lido stETH, Rocket Pool rETH, Coinbase cbETH) — compete for ETH capital but also supply LST to EigenLayer (HIGH) [https://lido.fi/, https://rocketpool.net/, https://www.coinbase.com/cloud/liquid-staking]
Market Segment: Institutional & retail ETH stakers seeking additional yield; AVS developers needing shared security; Rollups needing data availability (EigenDA)
Geographic Focus: Global (protocol permissionless); Core team and Eigen Labs Inc. based in United States (Delaware); Eigen Foundation in Cayman Islands
Sources: https://www.eigenlayer.xyz/, https://documents.deloitte.com/feeds/BCIR-2484369712E511E78A4C00155D0A3900, https://github.com/eigenfoundation

## Trading Markets

Exchange: Binance
Spot: Yes (EIGEN/USDT, EIGEN/BNB, EIGEN/FDUSD, EIGEN/TRY)
Perpetual: No (as of 2024-10)
Futures: No
Options: No
OTC: Not confirmed
Status: Live (since 2024-10-01, EV-013)
Sources: https://www.binance.com/en/support/announcement/eigen-eigen-listing, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: Bybit
Spot: Yes (EIGEN/USDT)
Perpetual: Not confirmed
Futures: No
Options: No
OTC: Not confirmed
Status: Live (since 2024-10)
Sources: https://www.bybit.com/en-US/trade/spot/EIGEN/USDT, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: OKX
Spot: Yes (EIGEN/USDT)
Perpetual: Not confirmed
Futures: No
Options: No
OTC: Not confirmed
Status: Live (since 2024-10)
Sources: https://www.okx.com/trade/EIGEN-USDT, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: Gate.io
Spot: Yes (EIGEN/USDT)
Perpetual: Not confirmed
Futures: No
Options: No
OTC: Not confirmed
Status: Live (since 2024-10)
Sources: https://www.gate.io/trade/EIGEN_USDT, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: KuCoin
Spot: Yes (EIGEN/USDT)
Perpetual: Not confirmed
Futures: No
Options: No
OTC: Not confirmed
Status: Live (since 2024-10)
Sources: https://www.kucoin.com/trade/EIGEN-USDT, https://blog.eigenlayer.xyz/eigen-token-genesis/

Exchange: Coinbase
Spot: No
Perpetual: No
Futures: No
Options: No
OTC: Not applicable
Status: Not Listed (as of 2024-10, price tracking only)
Sources: https://www.coinbase.com/price/eigenlayer

Exchange: Kraken
Spot: No
Perpetual: No
Futures: No
Options: No
OTC: Not applicable
Status: Not Listed (as of 2024-10, educational content only)
Sources: https://kraken.com/learn/eigenlayer-eigen

## Liquidity

Liquidity Source: CEX (Centralized Exchanges)
Major Liquidity Venue: Binance (primary listing at TGE, multiple trading pairs)
DEX: Uniswap V3 (EIGEN/WETH, EIGEN/USDC pools exist post-TGE) (MEDIUM) [https://app.uniswap.org/explore/tokens/ethereum/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9]
DEX: Curve (No dedicated EIGEN pool as of 2024-10) (MEDIUM) [https://curve.fi/]
Bridge Liquidity: Not applicable (EIGEN native to Ethereum mainnet; no official bridge)
Status: Live (CEX liquidity dominant; DEX liquidity emerging)
Sources: https://www.binance.com/en/support/announcement/eigen-eigen-listing, https://app.uniswap.org/explore/tokens/ethereum/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9, https://curve.fi/

## Adoption Metrics

Metric Name: TVL (Total Value Locked)
Value: ~$18.5B (peak ~$20B+ mid-2024; ~$18.5B as of 2024-10 per DefiLlama)
Date: 2024-10
Sources: https://defillama.com/protocol/eigenlayer

Metric Name: Restaked ETH (Native + LST + LRT)
Value: ~4.8M ETH equivalent (native ETH + stETH + rETH + cbETH + LRT tokens)
Date: 2024-10
Sources: https://defillama.com/protocol/eigenlayer, https://www.eigenlayer.xyz/ (dashboard)

Metric Name: Unique Stakers (Addresses with delegated stake)
Value: ~180,000 unique addresses (cumulative since mainnet launch)
Date: 2024-10
Sources: https://dune.com/eigenlayer (community dashboard), https://www.eigenlayer.xyz/

Metric Name: Daily Active Stakers (Delegation interactions)
Value: ~2,000-5,000 daily active addresses (varies by period)
Date: 2024-10
Sources: https://dune.com/eigenlayer (community dashboard)

Metric Name: Operator Count (Registered operators)
Value: ~1,200 registered operators (cumulative)
Date: 2024-10
Sources: https://www.eigenlayer.xyz/ (operator dashboard), https://docs.eigenlayer.xyz/docs/operators/overview

Metric Name: Active AVS Count
Value: 3 live AVS on mainnet (EigenDA, AltLayer, Dymension, Lagrange) — 4 total including EigenDA
Date: 2024-10
Sources: https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/core-contracts/avsregistry

Metric Name: EigenDA Data Throughput
Value: ~10-50 MB/s sustained (permissioned rollup integration phase)
Date: 2024-10
Sources: https://docs.eigenlayer.xyz/docs/eigenda/overview, https://www.eigenlayer.xyz/avs

Metric Name: Developer Count (Active contributors to EigenLayer repos)
Value: ~50-100 active monthly contributors across Layr-Labs org (core contracts, EigenDA, CLI, SDK)
Date: 2024-10
Sources: https://github.com/Layr-Labs, https://github.com/Layr-Labs/eigenlayer-contracts/graphs/contributors

Metric Name: GitHub Stars (EigenLayer Core Contracts)
Value: ~2,500 stars (eigenlayer-contracts repo)
Date: 2024-10
Sources: https://github.com/Layr-Labs/eigenlayer-contracts

Metric Name: EIGEN Token Holders
Value: ~45,000 unique holders (post-TGE, includes vesting contract beneficiaries)
Date: 2024-10
Sources: https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9#balances

Metric Name: EIGEN Staked for Governance
Value: ~50M EIGEN staked (Season 2 + early stakers)
Date: 2024-10
Sources: https://www.eigenlayer.xyz/ (staking dashboard), https://blog.eigenlayer.xyz/eigen-token-genesis/

## Market Share

Metric: Restaking TVL Market Share (Ethereum)
Value: ~85-90% of total restaking TVL (EigenLayer dominant; Symbiotic, Karak smaller)
Date: 2024-10
Sources: https://defillama.com/category/restaking, https://defillama.com/protocol/eigenlayer

Metric: Data Availability Market Share (EigenDA vs Celestia, Avail, etc.)
Value: Not available (EigenDA recently launched; rollup adoption in early stages; no standardized market share metric)
Date: 2024-10
Sources: https://docs.eigenlayer.xyz/docs/eigenda/overview

Metric: LRT Market Share (via EigenLayer)
Value: EtherFi (~50% of LRT TVL), Renzo (~25%), Kelp/Puffer/Swell (~25% combined) — approximate
Date: 2024-10
Sources: https://defillama.com/protocol/eigenlayer (TVL breakdown by protocol)

## Competitor Landscape

Competitor: Babylon
Category: Restaking / Shared Security (Bitcoin-focused)
Difference: Babylon enables Bitcoin staking to secure PoS chains; EigenLayer uses Ethereum ETH/LST/LRT. Different base asset, different trust assumptions. Babylon mainnet 2024; EigenLayer mainnet 2023.
Market Segment: Bitcoin holders seeking yield; PoS chains seeking Bitcoin security
Sources: https://babylonlabs.io/, https://docs.eigenlayer.xyz/docs/overview/introduction

Competitor: Symbiotic
Category: Restaking Protocol (Ethereum)
Difference: Symbiotic launched 2024 as permissionless restaking protocol; modular design with customizable vaults and operators; no native token at launch. EigenLayer first-mover, larger TVL, live AVS ecosystem, EIGEN token live.
Market Segment: ETH stakers seeking alternative restaking; AVS developers wanting permissionless framework
Sources: https://symbiotic.fi/, https://defillama.com/protocol/symbiotic

Competitor: Karak
Category: Universal Restaking Layer (Multi-chain)
Difference: Karak supports restaking of multiple assets (ETH, BTC, stablecoins) across chains; universal design vs EigenLayer Ethereum-only. Earlier stage, smaller TVL.
Market Segment: Multi-asset restakers; cross-chain AVS developers
Sources: https://karak.network/, https://defillama.com/protocol/karak

Competitor: Ethereum Native Staking
Category: Base Staking (No Restaking)
Difference: Direct validator staking (32 ETH) or liquid staking (LST) without additional slashing risk. Lower yield but simpler risk profile. Competes for same ETH capital.
Market Segment: Risk-averse ETH holders; solo stakers; institutions preferring native staking
Sources: https://ethereum.org/en/staking/, https://lido.fi/, https://rocketpool.net/

Competitor: Liquid Staking Protocols (Lido, Rocket Pool, Coinbase)
Category: Liquid Staking (LST Providers)
Difference: Provide LST (stETH, rETH, cbETH) that can be restaked on EigenLayer. Both competitors (for ETH capital) and suppliers (LST flow into EigenLayer). Symbiotic relationship.
Market Segment: ETH holders wanting liquidity + staking yield; feed into restaking ecosystem
Sources: https://lido.fi/, https://rocketpool.net/, https://www.coinbase.com/cloud/liquid-staking, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Competitor: Celestia
Category: Data Availability Layer
Difference: Celestia is sovereign DA chain with own validator set; EigenDA is AVS on EigenLayer secured by restaked ETH. Different security model (sovereign vs shared security). Celestia longer track record, more rollup integrations.
Market Segment: Rollups needing DA; developers choosing DA layer
Sources: https://celestia.org/, https://docs.eigenlayer.xyz/docs/eigenda/overview

Competitor: Avail
Category: Data Availability Layer
Difference: Avail uses own validator set (Nominated PoS); EigenDA uses EigenLayer restakers. Different trust assumptions. Avail mainnet 2024.
Market Segment: Rollups needing DA; Polygon ecosystem alignment
Sources: https://www.availproject.org/, https://docs.eigenlayer.xyz/docs/eigenda/overview

## Narrative Position

Narrative: Restaking
Status: Main Narrative (EigenLayer is the pioneer and market leader in restaking category)
Evidence: Coined/term popularized "restaking"; first mainnet (2023-06-14); largest TVL; $150M+ funding; EV-003, EV-005, EV-008
Sources: https://www.eigenlayer.xyz/, https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/, https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital, https://defillama.com/category/restaking

Narrative: Shared Security
Status: Main Narrative (Core value proposition: shared security via restaking for AVS)
Evidence: AVS framework (EigenDA, AltLayer, Dymension, Lagrange live); EV-009, EV-010; whitepaper
Sources: https://www.eigenlayer.xyz/avs, https://www.eigenlayer.xyz/eigenlayer-whitepaper.pdf, https://docs.eigenlayer.xyz/docs/overview/introduction

Narrative: Modular Blockchain
Status: Secondary Narrative (EigenDA as modular DA layer; EigenLayer as modular security layer)
Evidence: EigenDA mainnet 2024-04; rollup integration; modular thesis alignment (Celestia, EigenDA, Avail)
Sources: https://docs.eigenlayer.xyz/docs/eigenda/overview, https://blog.eigenlayer.xyz/eigen-token-genesis/

Narrative: Data Availability (EigenDA)
Status: Secondary Narrative (EigenDA as first AVS and DA product)
Evidence: EigenDA mainnet launch EV-009; disperser/retriever architecture; rollup partnerships
Sources: https://www.eigenlayer.xyz/avs, https://docs.eigenlayer.xyz/docs/eigenda/overview

Narrative: Interoperability / Cross-chain (AVS enabling)
Status: Secondary Narrative (AVS like AltLayer, Dymension enable cross-chain rollups secured by EigenLayer)
Evidence: AltLayer, Dymension live as AVS EV-010; not native cross-chain messaging in core protocol
Sources: https://www.altlayer.io/, https://dymension.xyz/, https://www.eigenlayer.xyz/avs

Narrative: DePIN (via AVS)
Status: Emerging Narrative (Potential for AVS to secure DePIN networks; no major DePIN AVS live yet)
Evidence: AVS framework supports arbitrary services; blog mentions DePIN as future AVS category
Sources: https://docs.eigenlayer.xyz/docs/avs/overview, https://blog.eigenlayer.xyz/

Narrative: AI / ZK Compute (via Lagrange AVS)
Status: Emerging Narrative (Lagrange AVS provides ZK coprocessor secured by restakers)
Evidence: Lagrange live AVS EV-010; ZK proving as service
Sources: https://www.lagrange.dev/, https://www.eigenlayer.xyz/avs

Narrative: Intent / Chain Abstraction
Status: Not Primary (EigenLayer does not directly address intent/chain abstraction; AVS could build on top)
Evidence: No core protocol feature for intents; AVS framework could support
Sources: https://docs.eigenlayer.xyz/docs/avs/overview

Narrative: RWA (Real World Assets)
Status: Not Primary (No RWA-specific AVS live; framework could support)
Evidence: AVS framework generic; no announced RWA AVS as of 2024-10
Sources: https://www.eigenlayer.xyz/avs

## Market Timeline

Date: 2023-02
Milestone: Series A Funding ($50M led by Blockchain Capital)
Description: $50M Series A enables core protocol development and team expansion
Related Historical Event ID: EV-003
Sources: https://www.theblock.co/post/214073/eigenlayer-raises-50-million-series-a-blockchain-capital

Date: 2023-04-20
Milestone: Public Testnet "Mango" Launch
Description: First public testnet for restaking ETH native and LST
Related Historical Event ID: EV-004
Sources: https://www.coindesk.com/tech/2023/04/20/eigenlayer-launches-testnet-for-ethereum-restaking-protocol/

Date: 2023-06-14
Milestone: Mainnet Phase 1 Launch (Native ETH Restaking)
Description: Core contracts live on Ethereum mainnet; native ETH restaking enabled
Related Historical Event ID: EV-005
Sources: https://blog.eigenlayer.xyz/eigenlayer-mainnet-launch/

Date: 2023-07
Milestone: EtherFi eETH Integration (First LRT)
Description: EtherFi launches eETH, first liquid restaking token on EigenLayer
Related Historical Event ID: EV-006
Sources: https://www.ether.fi/, https://docs.eigenlayer.xyz/docs/core-contracts/strategymanager

Date: 2023-12
Milestone: Multi-LRT Integration (Renzo, Kelp, Puffer, Swell)
Description: Four additional LRT protocols launch tokens integrated with EigenLayer
Related Historical Event ID: EV-007
Sources: https://www.eigenlayer.xyz/

Date: 2024-02
Milestone: Series B Funding ($100M led by a16z crypto, $1B valuation)
Description: $100M Series B at unicorn valuation for AVS ecosystem expansion
Related Historical Event ID: EV-008
Sources: https://www.theblock.co/post/277456/eigenlayer-raises-100-million-series-b-a16z

Date: 2024-04
Milestone: EigenDA Mainnet Launch
Description: First AVS (data availability layer) launches on EigenLayer mainnet
Related Historical Event ID: EV-009
Sources: https://www.eigenlayer.xyz/avs

Date: 2024-04
Milestone: First Third-Party AVS Live (AltLayer, Dymension, Lagrange)
Description: Three AVS launch on EigenLayer mainnet demonstrating shared security model
Related Historical Event ID: EV-010
Sources: https://www.eigenlayer.xyz/avs

Date: 2024-07
Milestone: Eigen Foundation Formation
Description: Foundation established in Cayman Islands for token governance and treasury
Related Historical Event ID: EV-011
Sources: https://github.com/eigenfoundation

Date: 2024-10-01
Milestone: Token Generation Event (TGE) — EIGEN Token Launch
Description: EIGEN token deployed, Season 1 claim opens, simultaneous CEX listings
Related Historical Event ID: EV-012, EV-013
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/, https://www.binance.com/en/support/announcement/eigen-eigen-listing

Date: 2024-10
Milestone: Season 2 Distribution & Governance Staking Activation
Description: Season 2 claim opens, EIGEN staking for governance and intersubjective rewards live
Related Historical Event ID: EV-014
Sources: https://blog.eigenlayer.xyz/eigen-token-genesis/

## Official Market Resources

Official Dashboard: https://www.eigenlayer.xyz/
DefiLlama: https://defillama.com/protocol/eigenlayer
CoinGecko: https://www.coingecko.com/en/coins/eigenlayer
CoinMarketCap: https://coinmarketcap.com/currencies/eigenlayer/
Token Terminal: https://tokenterminal.com/terminal/projects/eigenlayer
Messari: https://messari.io/project/eigenlayer/profile
Explorer: https://etherscan.io/token/0xec53bF9167f50cDEB3aE105fA56099AA5b8fB2c9

## RINGKASAN

Market Stage: Growth
Primary Category: Restaking / Shared Security Infrastructure
Competitor Count: 7 direct competitors identified (Babylon, Symbiotic, Karak, Ethereum Native Staking, Lido, Celestia, Avail)
Major Narrative: Restaking (Main), Shared Security (Main), Modular Blockchain (Secondary), Data Availability (Secondary)
Trading Availability: 5 CEX (Binance, Bybit, OKX, Gate.io, KuCoin) + DEX (Uniswap V3); No perpetuals/futures/options
Adoption Metrics Available: TVL (~$18.5B), Restaked ETH (~4.8M), Unique Stakers (~180K), Operators (~1,200), AVS (4 live), EigenDA Throughput, Developer Count, Token Holders (~45K), Staked EIGEN (~50M)

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: EigenLayer

Strategic Objectives

1. Membangun lapisan keamanan bersama (shared security) di atas Ethereum melalui restaking

· Evidence: Visi protokol restaking yang memungkinkan ETH, LST, dan LRT di-restake untuk mengamankan AVS (Actively Validated Services) — didefinisikan sejak pendirian 2021 dan diluncurkan mainnet fase 1 Juni 2023 (EV-005)
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-001, EV-005, Phase 4 System Architecture

2. Menjadi infrastruktur data availability terdepan melalui EigenDA sebagai AVS pertama

· Evidence: EigenDA diluncurkan mainnet April 2024 (EV-009) sebagai AVS pertama, menyediakan throughput data tinggi untuk rollup; whitepaper dan arsitektur modular memposisikan EigenDA sebagai komponen kunci
· Supporting Dataset: Phase 3 EV-009, Phase 4 Core Components (EigenDA), Phase 8 Market Position

3. Menciptakan ekosistem AVS yang berkembang melalui framework permissionless (bertahap)

· Evidence: AVSRegistry dan AllocationManager memungkinkan AVS baru mendaftar; 3 AVS pihak ketiga live April 2024 (EV-010); roadmap menuju permissionless operator registration
· Supporting Dataset: Phase 3 EV-010, Phase 4 Core Components (AVSRegistry, AllocationManager), Phase 7 Major Integrations

4. Mendistribusikan governance dan value capture ke komunitas melalui token EIGEN

· Evidence: TGE Oktober 2024 (EV-012) dengan alokasi 45% untuk komunitas (Season 1 5%, Season 2 10%, Future 30%); staking EIGEN untuk governance dan intersubjective work rewards live Season 2 (EV-014)
· Supporting Dataset: Phase 3 EV-012, EV-014, Phase 6 Token Distribution, Phase 6 Governance

5. Memisahkan pengembangan protokol (Eigen Labs) dari pengelolaan token/ekosistem (Eigen Foundation)

· Evidence: Eigen Labs Inc (Delaware) sebagai core developer; Eigen Foundation (Cayman) didirikan Juli 2024 (EV-011) untuk treasury, governance, token distribution — struktur dual-entity yang disengaja
· Supporting Dataset: Phase 2 Entity (Eigen Labs Inc, Eigen Foundation), Phase 3 EV-011, Phase 5 Financial Dependencies

Decision Timeline

Keputusan: Pendirian Eigen Labs Inc di Delaware oleh Sreeram Kannan (2021)
· Trigger: Identifikasi peluang restaking ETH untuk shared security di Ethereum; perlu entitas hukum untuk pengembangan protokol dan fundraising
· Evidence: Pendirian Eigen Labs Inc tercatat di dokumen Delawere 2021; Sreeram Kannan sebagai Founder & CEO (Phase 2)
· Decision: Membangun perusahaan pengembangan protokol (bukan DAO langsung) dengan struktur venture-backed
· Immediate Result: Entitas legal untuk merekrut tim, mengumpulkan dana, mengembangkan kontrak pintar
· Long-term Impact: Memisahkan core development (Labs) dari governance protokol (Foundation) — pola dual-entity yang berlanjut hingga sekarang
· Supporting Dataset: Phase 2 Entity (Eigen Labs Inc, Sreeram Kannan), Phase 3 EV-001, Phase 5 Funding History

Keputusan: Series A $50M dipimpin Blockchain Capital (2023-02)
· Trigger: Butuh dana untuk pengembangan mainnet, audit, dan tim sebelum testnet publik
· Evidence: The Block melaporkan Series A $50M led by Blockchain Capital dengan Coinbase Ventures, Polychain (Phase 3 EV-003, Phase 5)
· Decision: Menerima venture funding dengan valuasi tidak diungkap; investor menerima token allocation (vesting 12-36 bulan)
· Immediate Result: Dana untuk meluncurkan testnet "Mango" April 2023 dan mainnet Juni 2023
· Long-term Impact: Menetapkan pola venture-backed dengan token allocation untuk investor; investor 29.5% supply EIGEN (Phase 6)
· Supporting Dataset: Phase 3 EV-003, Phase 5 Funding History, Phase 6 Vesting Schedule

Keputusan: Peluncuran mainnet fase 1 hanya native ETH restaking (2023-06-14)
· Trigger: Kontrak inti (StrategyManager, DelegationManager, SlashingManager, EigenPodManager) siap; keamanan diprioritaskan dengan scope minimal
· Evidence: Blog resmi mainnet launch menyebut "Phase 1: Native ETH Restaking Only" (Phase 3 EV-005, Phase 4 Technical Upgrade History)
· Decision: Batasi deposit hanya native ETH via EigenPod; LST/LRT ditunda ke upgrade berikutnya
· Immediate Result: TVL mulai tumbuh dari native ETH staker; slashing mechanics diuji produksi dengan risiko terbatas
· Long-term Impact: Pola "phased rollout" berulang — LST support Sep 2023, LRT Dec 2023, EigenDA Apr 2024, AVS Apr 2024
· Supporting Dataset: Phase 3 EV-005, Phase 4 Technical Upgrade History, Phase 4 Known Limitations

Keputusan: Integrasi EtherFi eETH sebagai LRT pertama (2023-07)
· Trigger: Permintaan pasar untuk likuiditas restaking; EigenLayer belum support LST/LRT native
· Evidence: EtherFi meluncurkan eETH Juli 2023 terintegrasi StrategyManager (Phase 3 EV-006, Phase 7 Major Integrations)
· Decision: Mengizinkan LRT protocol membangun di atas StrategyManager tanpa modifikasi protokol inti
· Immediate Result: eETH menjadi LRT terbesar; membuka pintu Renzo, Kelp, Puffer, Swell (EV-007)
· Long-term Impact: Ekosistem LRT jadi growth driver utama TVL EigenLayer (~4.8M ETH equivalent, Phase 8); LRT protocol jadi dependency kritis (Phase 7 External Dependencies)
· Supporting Dataset: Phase 3 EV-006, EV-007, Phase 7 Major Integrations, Phase 8 Adoption Metrics

Keputusan: Series B $100M dipimpin a16z crypto valuasi $1B (2024-02)
· Trigger: Butuh dana untuk ekspansi AVS ecosystem, EigenDA development, scaling tim pasca-mainnet
· Evidence: The Block melaporkan Series B $100M led by a16z crypto at $1B valuation (Phase 3 EV-008, Phase 5)
· Decision: Funding besar kedua dengan unicorn valuation; a16z mendapat token allocation vesting 12-36 bulan
· Immediate Result: Dana untuk EigenDA mainnet April 2024, AVS onboarding, team expansion
· Long-term Impact: Investor concentration meningkat (Blockchain Capital + a16z + Coinbase Ventures + Polychain = 29.5% supply); governance influence besar
· Supporting Dataset: Phase 3 EV-008, Phase 5 Funding History, Phase 6 Vesting Schedule, Phase 8 Ecosystem Risks

Keputusan: Peluncuran EigenDA mainnet sebagai AVS pertama (2024-04)
· Trigger: Arsitektur AVS framework siap (AllocationManager, AVSRegistry); butuh proof-of-concept produk nyata
· Evidence: EigenDA mainnet launch April 2024 dengan disperser/retriever, permissioned operator set (Phase 3 EV-009, Phase 4 Core Components)
· Decision: Membangun AVS pertama secara internal (bukan third-party) untuk memvalidasi framework dan generate revenue
· Immediate Result: EigenDA live, rollup mulai integrasi, protocol revenue dari service fees mulai mengalir
· Long-term Impact: EigenDA jadi revenue source utama protokol; template untuk AVS lain; operator permissioned model jadi precedent
· Supporting Dataset: Phase 3 EV-009, Phase 4 Core Components (EigenDA), Phase 5 Revenue Model, Phase 8 Market Position

Keputusan: Onboarding 3 AVS third-party bersamaan (AltLayer, Dymension, Lagrange) (2024-04)
· Trigger: AVS framework siap; multiple teams siap deploy; perlu demonstrasi shared security model
· Evidence: 3 AVS launch April 2024 tercatat EV-010 (Phase 3, Phase 7 Major Integrations)
· Decision: Koordinasi multi-AVS launch untuk momentum ekosistem; bukan sequential
· Immediate Result: 4 total AVS live (termasuk EigenDA); operator delegation mulai tersebar ke multiple AVS
· Long-term Impact: Validasi AVS framework; tapi operator set masih permissioned; slashing isolation mechanics belum teruji produksi
· Supporting Dataset: Phase 3 EV-010, Phase 7 Major Integrations, Phase 4 Known Limitations (slashing isolation)

Keputusan: Pembentukan Eigen Foundation di Cayman Islands (2024-07)
· Trigger: Perlu entitas terpisah untuk token issuance, treasury, governance, compliance sebelum TGE
· Evidence: Eigen Foundation repo GitHub dibuat 2024; struktur terpisah dari Eigen Labs (Phase 2 Entity, Phase 3 EV-011)
· Decision: Foundation mengelola 10.5% supply, token distribution (Season 1/2), governance execution (multisig transitional), ecosystem grants
· Immediate Result: Legal wrapper untuk TGE Oktober 2024; token distribution contracts di-deploy oleh Foundation
· Long-term Impact: Dual-entity structure (Labs + Foundation) jadi permanent; Foundation multisig kontrol upgrade protokol hingga on-chain governance live
· Supporting Dataset: Phase 2 Entity (Eigen Foundation), Phase 3 EV-011, Phase 6 Governance, Phase 7 Governance Ecosystem

Keputusan: Token Generation Event EIGEN dengan Season 1 claim & CEX listing simultan (2024-10-01)
· Trigger: Protokol matang (mainnet 16 bulan, 4 AVS live, $18B+ TVL); investor/community menunggu liquidity event
· Evidence: TGE Oct 1 2024 dengan 5% supply unlock Season 1, listing Binance/Bybit/OKX/Gate.io/KuCoin simultan (Phase 3 EV-012, EV-013, Phase 6 TGE)
· Decision: Fair launch style (claim bukan public sale); major CEX listing day-1 untuk liquidity; no perpetual/futures at launch
· Immediate Result: Price discovery dimulai; ~45K holders; ~$50M+ staked EIGEN untuk governance (Phase 8)
· Long-term Impact: Vesting cliff investor/team 12 bulan (Oct 2025) jadi overhang supply besar; Season 2 cliff 6 bulan (Apr 2025)
· Supporting Dataset: Phase 3 EV-012, EV-013, Phase 6 TGE, Vesting Schedule, Phase 8 Trading Markets

Keputusan: Aktivasi Season 2 distribution & EIGEN staking untuk governance/intersubjective rewards (2024-10)
· Trigger: Post-TGE, perlu mendorong participation governance dan secure intersubjective work
· Evidence: Season 2 claim dibuka (10% supply), staking contracts live, delegation supported (Phase 3 EV-014, Phase 6 Utility, Governance)
· Decision: Token utility langsung aktif: governance voting + intersubjective work staking rewards (inflationary)
· Immediate Result: ~50M EIGEN staked; governance proposals mulai diajukan; operator delegation voting power
· Long-term Impact: Inflationary emissions dimulai; governance capture risk oleh large holders (investor/team/foundation = 55% supply locked)
· Supporting Dataset: Phase 3 EV-014, Phase 6 Utility, Inflation/Deflation, Governance, Phase 8 Ecosystem Risks

Evolution Pattern

Evolusi Strategi: Dari Core Protocol → AVS Platform → Modular Infrastructure Stack
· Fase 1 (2021-2023 H1): Fokus penuh pada core restaking contracts (StrategyManager, DelegationManager, SlashingManager, EigenPodManager) — "build the rails"
· Fase 2 (2023 H2): Ekspansi ke LST/LRT support — membuka pintu capital efficiency untuk staker; LRT protocol jadi growth engine
· Fase 3 (2024 H1): EigenDA mainnet + first third-party AVS — transisi dari "restaking protocol" ke "AVS platform"; proof-of-concept shared security
· Fase 4 (2024 H2+): Token launch, governance activation, Foundation operations — tambahan layer ekonomi & governance; roadmap ke permissionless AVS/operator
· Evidence: Timeline Phase 3 (EV-001 melalui EV-014); Phase 4 Technical Upgrade History; Phase 8 Market Timeline

Evolusi Teknologi: Monolithic Contracts → Modular AVS Framework → Intersubjective Work Layer
· Awal: 4 kontrak inti monolithic untuk restaking dasar (Phase 4 Core Components)
· Menengah: AllocationManager, AVSRegistry, EigenDA contracts — modularisasi untuk multi-AVS support (Phase 4 Technical Upgrade History EV-009, EV-010)
· Lanjut: EIGEN token contracts untuk intersubjective work — tambahan economic layer di atas objective slashing (Phase 4 Consensus Mechanism, Phase 6 Utility)
· Evidence: Phase 4 Technical Upgrade History, Core Components, Consensus Mechanism; Phase 6 Token Information

Evolusi Tokenomics: No Token → Venture-Backed Equity Only → Dual Token/Equity Model dengan Community Distribution
· Pre-2024: Hanya equity investors (Series A/B); no token, no community ownership
· TGE 2024: EIGEN token dengan 45% community allocation (Season 1/2/Future), 29.5% investors, 15% team, 10.5% foundation
· Post-TGE: Inflationary emissions untuk intersubjective work rewards; governance via staking
· Evidence: Phase 5 Funding History (no token rounds), Phase 6 Distribution, Vesting Schedule, Inflation/Deflation

Evolusi Governance: Centralized (Labs) → Foundation Multisig → On-Chain Token-Weighted (Transitional)
· 2021-2024 H1: Eigen Labs kontrol penuh (deploy, upgrade, parameter)
· 2024 H1: Eigen Foundation formed, multisig admin proxy contracts (Phase 7 Governance Ecosystem)
· 2024 H2: EIGEN staking + Governor contracts live; delegation supported; Foundation multisig masih emergency/upgrade authority
· Evidence: Phase 3 EV-011, EV-014; Phase 6 Governance; Phase 7 Governance Ecosystem

Evolusi Ekosistem: Single Protocol → Multi-Sided Marketplace (Stakers ↔ Operators ↔ AVS)
· Awal: Hanya stakers ↔ EigenLayer contracts
· LRT Era: Stakers → LRT protocols → EigenLayer → Operators (3-sided)
· AVS Era: Stakers ↔ Operators ↔ Multiple AVS (EigenDA, AltLayer, Dymension, Lagrange) — marketplace keamanan bersama
· Evidence: Phase 7 External Dependencies, Major Integrations, Infrastructure Providers, Applications

Technical Decision Pattern

Pola 1: Ethereum Alignment First — Semua Kembali ke Ethereum
· Decision Pattern: Protokol tidak membangun consensus, execution, atau settlement layer sendiri; sepenuhnya leverage Ethereum PoS untuk finality, validator set, dan economic security. EigenPod menggunakan beacon chain withdrawal credentials (0x01). Slashing di-enforce di Ethereum L1.
· Evidence: Phase 4 System Architecture ("Settlement Layer: Ethereum mainnet"), Consensus Mechanism ("Ethereum Consensus: EigenLayer does not have its own consensus"), Core Components (EigenPodManager), Known Limitations ("Single Settlement Chain")
· Supporting Dataset: Phase 4 System Architecture, Consensus Mechanism, Core Components, Known Limitations

Pola 2: Phased Rollout dengan Scope Minimal per Fase
· Decision Pattern: Setiap mainnet launch membatasi fungsi: Phase 1 hanya native ETH; LST support bulan 3 kemudian; LRT support bulan 6 kemudian; EigenDA & AVS terpisah 10 bulan kemudian. Setiap fase audit ulang.
· Evidence: Phase 3 EV-005 (Phase 1 native only), EV-006/007 (LST/LST), EV-009/010 (EigenDA/AVS); Phase 4 Technical Upgrade History (7 major upgrades bertahap); Phase 4 Audit History (7 audits terpisah per komponen/upgrade)
· Supporting Dataset: Phase 3 Historical Events, Phase 4 Technical Upgrade History, Audit History

Pola 3: Modular AVS Framework — Protokol Menyediakan Rails, AVS Bangun Sendiri
· Decision Pattern: EigenLayer core hanya menyediakan: stake delegation (DelegationManager), operator allocation (AllocationManager), slashing enforcement (SlashingManager), service discovery (AVSRegistry). AVS harus bangun off-chain software, disperser/retriever, service manager contracts sendiri.
· Evidence: Phase 4 Core Components (AllocationManager, AVSRegistry, SlashingManager), EigenDA Components (Disperser, Retriever, ServiceManager terpisah), Phase 7 Major Integrations (AltLayer, Dymension, Lagrange masing-masing punya ServiceManager sendiri)
· Supporting Dataset: Phase 4 Core Components, EigenDA Components, Phase 7 Major Integrations

Pola 4: Objective Slashing Dulu, Intersubjective Slashing Kemudian via Token Baru
· Decision Pattern: Slashing awal hanya untuk faults objektif terbukti on-chain (equivocation, invalid attestation). Intersubjective faults (data withholding, oracle manipulation) butuh social consensus → dipisah ke EIGEN token dengan mechanics terpisah.
· Evidence: Phase 4 Security Model (SlashingManager untuk objective, EIGEN untuk intersubjective), Consensus Mechanism (Intersubjective Consensus), Phase 6 Utility (Intersubjective Work Staking, Collateral/Slashing)
· Supporting Dataset: Phase 4 Security Model, Consensus Mechanism, Phase 6 Utility

Pola 5: Permissioned Operator Set Awal, Progressive Decentralization
· Decision Pattern: EigenDA dan early AVS menggunakan operator set permissioned (dipilih Eigen Labs/Foundation). Roadmap menyebut "progressive decentralization" tapi tidak ada tanggal/kriteria konkret.
· Evidence: Phase 4 Core Components (EigenDA Operator — "Live, permissioned operator set initially"), Known Limitations ("Operator Permissioning: EigenDA and early AVS use permissioned operator sets"), Phase 7 Infrastructure Providers (EigenDA Operators permissioned)
· Supporting Dataset: Phase 4 Core Components, Known Limitations, Phase 7 Infrastructure Providers, Phase 8 Ecosystem Risks

Pola 6: Go untuk Off-Chain Infrastructure, Solidity untuk On-Chain
· Decision Pattern: Semua smart contracts Solidity (Foundry). Off-chain components (EigenDA disperser/retriever, operator nodes, CLI) menggunakan Go. Rust untuk erasure coding library. TypeScript untuk SDK.
· Evidence: Phase 4 Programming Languages, Development Framework, Current Technical Stack — Go 1.21+ untuk EigenDA/CLI, Solidity 0.8.x untuk contracts, Rust untuk crates erasure coding, TypeScript untuk SDK
· Supporting Dataset: Phase 4 Programming Languages, Development Framework, Current Technical Stack

Pola 7: Withdrawal Delay Wajib sebagai Security Primitive
· Decision Pattern: 7-day withdrawal delay (configurable tapi mandatory) di-enforce di DelegationManager untuk slashing window. EigenPod menambah Ethereum validator exit queue delay. Tidak ada "instant withdraw" meski LRT protocol memberikan likuiditas sintetis.
· Evidence: Phase 4 Core Components (DelegationManager, EigenPodManager), Security Model (Withdrawal Delay), Known Limitations (Withdrawal Delay, EigenPod Exit Queue), Phase 8 Ecosystem Risks (Liquidity Risk)
· Supporting Dataset: Phase 4 Core Components, Security Model, Known Limitations, Phase 8 Ecosystem Risks

Financial Decision Pattern

Pola 1: Venture Funding Bertahap dengan Valuasi Meningkat — Equity First, Token Later
· Decision Pattern: Series A ($50M, Feb 2023) → Series B ($100M, Feb 2024, $1B valuation) sebelum TGE. Token allocation untuk investor (29.5%) vesting 12-36 bulan cliff 12 bulan. Tidak ada public/private token sale tradisional.
· Evidence: Phase 5 Funding History (Series A, Series B), Phase 6 Vesting Schedule (Investors cliff 12 bulan vesting 24-36 bulan), Phase 6 Token Sale (no public sale, Season 1/2 claim only)
· Supporting Dataset: Phase 3 EV-003, EV-008; Phase 5 Funding History; Phase 6 Vesting Schedule, Token Sale

Pola 2: Treasury Terpusat di Foundation, Komposisi Tidak Transparan
· Decision Pattern: Eigen Foundation (Cayman) mengelola 10.5% supply + ecosystem fund. Tidak ada dashboard treasury publik, tidak ada transparency report berkala. Foundation multisig kontrol upgrade protokol.
· Evidence: Phase 5 Treasury (Current Treasury Size: tidak diungkap, Composition: tidak diungkap, Custodian: Eigen Foundation), Phase 7 Governance Ecosystem (Foundation multisig transitional control)
· Supporting Dataset: Phase 5 Treasury, Phase 7 Governance Ecosystem, Phase 2 Entity (Eigen Foundation)

Pola 3: Revenue Hanya dari EigenDA Service Fees (Live), Core Protocol Fee Switch Belum Aktif
· Decision Pattern: EigenLayer core protocol tidak mengambil fee dari restaking/delegation. Revenue hanya dari EigenDA (disperser fees ke operator + protokol) sejak April 2024. AVS fees tidak ke core protocol.
· Evidence: Phase 5 Revenue Model (Protocol Fees: Planned/Not Live, EigenDA Service Fees: Live since 2024-04, AVS Service Fees: per AVS basis, not to core), Phase 4 Core Components (no fee mechanism in StrategyManager/DelegationManager)
· Supporting Dataset: Phase 5 Revenue Model, Phase 4 Core Components, Phase 8 Market Position

Pola 4: Token Allocation Berbobot ke Investor & Team (55% Combined) vs Community (45%)
· Decision Pattern: Investors 29.5% + Team 15% + Foundation 10.5% = 55% supply locked tapi terkonsentrasi. Community 45% tapi hanya 5% unlocked at TGE (Season 1), 10% Season 2 cliff 6 bulan, 30% Future belum jadwal pasti.
· Evidence: Phase 6 Distribution (Community 45%, Team 15%, Investors 29.5%, Foundation 10.5%), Vesting Schedule (Team/Investor cliff 12 bulan, Season 2 cliff 6 bulan), Phase 8 Ecosystem Risks (VC Token Concentration)
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule, Phase 8 Ecosystem Risks

Pola 5: Inflationary Emissions untuk Intersubjective Work Rewards, No Burn/Buyback
· Decision Pattern: EIGEN supply inflationary via programmatic emissions untuk staking rewards (target 5-10% APY awal). Max supply cap 1.673B tapi emissions menambah circulating supply. Tidak ada fee burn, buyback, atau deflationary mechanism.
· Evidence: Phase 6 Supply Type (Inflationary), Inflation/Deflation (Intersubjective work rewards, no burn, no buyback), Phase 4 Consensus Mechanism (Intersubjective Consensus)
· Supporting Dataset: Phase 6 Supply, Inflation/Deflation, Phase 4 Consensus Mechanism

Pola 6: Eigen Labs Burn Rate Ditanggung VC Funding, Belum Ada Protocol Revenue Cover
· Decision Pattern: Operasional Eigen Labs (tim 50-100+ orang, infrastructure, audit) dibiayai Series A/B $150M. Protocol revenue (EigenDA fees) baru mulai 2024-04, jumlah tidak diungkap, kemungkinan jauh di bawah burn rate.
· Evidence: Phase 5 Financial Risk (Funding Dependency: "Operasional Eigen Labs bergantung pada venture funding... belum ada revenue protokol yang signifikan"), Phase 8 Adoption Metrics (Developer count 50-100), Phase 5 Revenue History (tidak diungkap)
· Supporting Dataset: Phase 5 Financial Risk, Revenue History, Phase 8 Adoption Metrics

Ecosystem Decision Pattern

Pola 1: LRT Protocol sebagai Primary Growth Engine — Build Ecosystem di Atas StrategyManager
· Decision Pattern: EigenLayer tidak membangun LRT sendiri; menyediakan StrategyManager sebagai platform untuk EtherFi, Renzo, Kelp, Puffer, Swell membangun LRT. LRT jadi user-facing product yang drive TVL.
· Evidence: Phase 3 EV-006, EV-007 (LRT integrations), Phase 7 Major Integrations (5 LRT protocols), Phase 7 External Dependencies (EtherFi, Renzo, Kelp, Puffer, Swell — Critical/High criticality), Phase 8 Adoption Metrics (TVL ~$18.5B driven by LRT)
· Supporting Dataset: Phase 3 EV-006, EV-007, Phase 7 Major Integrations, External Dependencies, Phase 8 Adoption Metrics

Pola 2: EigenDA sebagai First-Party AVS untuk Validasi Framework & Revenue
· Decision Pattern: Membangun AVS pertama secara internal (EigenDA) bukan menunggu third-party. Memvalidasi AVS framework, generate protocol revenue, jadi template untuk AVS lain.
· Evidence: Phase 3 EV-009 (EigenDA mainnet), Phase 4 Core Components (EigenDA Components), Phase 5 Revenue Model (EigenDA Service Fees live), Phase 7 Major Integrations (EigenDA AVS Integration)
· Supporting Dataset: Phase 3 EV-009, Phase 4 Core Components, Phase 5 Revenue Model, Phase 7 Major Integrations

Pola 3: Coordinated Multi-AVS Launch untuk Momentum Ekosistem
· Decision Pattern: AltLayer, Dymension, Lagrange diluncurkan bersamaan April 2024 (EV-010) bukan sequential. Koordinasi dengan tim AVS untuk demonstrasi shared security model yang nyata.
· Evidence: Phase 3 EV-010 (3 AVS launch April 2024), Phase 7 Major Integrations (3 AVS integration terpisah tapi same timeline), Phase 8 Market Timeline (EV-010)
· Supporting Dataset: Phase 3 EV-010, Phase 7 Major Integrations, Phase 8 Market Timeline

Pola 4: CEX Listing Strategy — Major Exchanges Day-1, No Derivatives at Launch
· Decision Pattern: Binance (lead), Bybit, OKX, Gate.io, KuCoin listing spot simultan TGE Oct 1 2024. Tidak ada perpetual/futures/options day-1. Fokus spot liquidity.
· Evidence: Phase 3 EV-013, Phase 7 Exchange Ecosystem (5 CEX listed spot, 0 perpetual), Phase 8 Trading Markets (same data)
· Supporting Dataset: Phase 3 EV-013, Phase 7 Exchange Ecosystem, Phase 8 Trading Markets

Pola 5: Developer Ecosystem via SDK/CLI/Grants — Bottom-Up AVS Building
· Decision Pattern: Menyediakan EigenLayer SDK (TS), EigenDA SDK (Go/TS), CLI (Go), Subgraph, Foundry templates. Grant program via Eigen Foundation. Hackathon tracks di ETHGlobal. Tidak ada "AVS template" cookie-cutter — setiap AVS custom build.
· Evidence: Phase 7 Developer Ecosystem (2 SDKs, 1 CLI, 1 Subgraph, Foundry, Grant programs, Hackathons), Phase 4 Development Framework, Phase 8 Ecosystem Risks (AVS Development Complexity)
· Supporting Dataset: Phase 7 Developer Ecosystem, Phase 4 Development Framework, Phase 8 Ecosystem Risks

Pola 6: Cloud-Agnostic Operator Infrastructure — Best Practices Bukan Enforcement
· Decision Pattern: Docs merekomendasikan Kubernetes, Prometheus/Grafana, Docker untuk operator production. Tapi tidak ada on-chain enforcement hardware specs, cloud diversity, atau geo-distribution. Operator bebas pilih infra.
· Evidence: Phase 7 Infrastructure Providers (Cloud Providers, Docker Hub, Kubernetes — Medium criticality), Phase 4 Current Technical Stack (Kubernetes recommended), Phase 8 Ecosystem Risks (Cloud Provider Dependency)
· Supporting Dataset: Phase 7 Infrastructure Providers, Phase 4 Current Technical Stack, Phase 8 Ecosystem Risks

Governance Decision Pattern

Pola 1: Dual-Entity Governance — Labs (Dev) + Foundation (Token/Treasury/Gov)
· Decision Pattern: Eigen Labs (Delaware corp) handle core development, contract deployment, research. Eigen Foundation (Cayman) handle token issuance, treasury, governance execution, grants. Pisah legal & operational.
· Evidence: Phase 2 Entity (Eigen Labs Inc, Eigen Foundation — terpisah), Phase 3 EV-011 (Foundation formation), Phase 7 Governance Ecosystem (Foundation role: treasury, grants, governance execution, upgrade authority)
· Supporting Dataset: Phase 2 Entity, Phase 3 EV-011, Phase 7 Governance Ecosystem

Pola 2: Transitional Multisig → On-Chain Governance via EIGEN Staking
· Decision Pattern: Saat ini: Foundation multisig kontrol proxy admin (upgrade contracts), emergency params. Transisi ke: EIGEN staking → Governor contracts → Timelock execution. Delegation supported. Belum fully live.
· Evidence: Phase 6 Governance (Token-weighted voting via staked EIGEN, Governor + Timelock, delegation supported, partially live), Phase 7 Governance Ecosystem (Foundation multisig transitional, on-chain governance transitioning), Phase 4 Security Model (Multi-sig/Governance upgradeability)
· Supporting Dataset: Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 4 Security Model

Pola 3: Token-Weighted Voting dengan Delegation ke Operator
· Decision Pattern: 1 EIGEN staked = 1 vote. Staker bisa delegate voting power ke operator/delegate lain. Operator (yang sudah punya delegated stake) jadi natural governance delegates — alignment tapi concentration risk.
· Evidence: Phase 6 Governance (Voting Power: 1 EIGEN = 1 vote, Delegation: Supported), Phase 7 Governance Ecosystem (Validator Group: Operators as delegation recipients), Phase 8 Ecosystem Risks (VC Token Concentration, Governance Risk)
· Supporting Dataset: Phase 6 Governance, Phase 7 Governance Ecosystem, Phase 8 Ecosystem Risks

Pola 4: AVS Onboarding via Governance (Planned Committee)
· Decision Pattern: AVSRegistry memungkinkan permissionless registration tapi AVS onboarding ke operator set & slashing butuh governance approval. Committee planned tapi belum formed.
· Evidence: Phase 7 Governance Ecosystem (Committee: AVS Onboarding Committee planned), Phase 4 Core Components (AVSRegistry), Phase 8 Ecosystem Risks (Operator Permissioning Centralization)
· Supporting Dataset: Phase 7 Governance Ecosystem, Phase 4 Core Components, Phase 8 Ecosystem Risks

Pola 5: Season-Based Token Distribution sebagai Governance Bootstrap
· Decision Pattern: Season 1 (5%, TGE unlock) → Season 2 (10%, cliff 6 bln) → Future Community (30%, long-term). Distribusi berbasis aktivitas (restaking, operating, contributing) bukan airdrop acak. Mengikat komunitas ke protokol sebelum full governance live.
· Evidence: Phase 6 Distribution (Community 45% = Season 1 5% + Season 2 10% + Future 30%), Vesting Schedule (Season 1 cliff 0, Season 2 cliff 6 bln), Phase 3 EV-012, EV-014
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule, Phase 3 EV-012, EV-014

Risk Response Pattern

Pola 1: Phased Rollout sebagai Risk Mitigation Utama
· Decision Pattern: Setiap major feature (native restaking, LST, LRT, EigenDA, AVS, token) diluncurkan bertahap dengan audit terpisah, scope minimal, monitoring period. Tidak ada "big bang" launch.
· Evidence: Phase 3 Historical Events (14 events over 3+ years, phased), Phase 4 Technical Upgrade History (7 major upgrades bertahap), Phase 4 Audit History (7 audits terpisah per komponen/timeline), Phase 4 Known Limitations (acknowledged risks per phase)
· Trigger: Complexity protokol tinggi (restaking + slashing + AVS + token); single failure point berakibat besar
· Response: Batasi blast radius per fase; audit sebelum setiap fase; monitor mainnet sebelum ekspansi
· Result: Zero major exploit/hack pada core contracts mainnet 2023-2024; TVL tumbuh bertahap ke $18B+
· Supporting Dataset: Phase 3 Historical Events, Phase 4 Technical Upgrade History, Audit History, Known Limitations

Pola 2: Permissioned Operator Set untuk Early AVS — Centralization Sementara Demi Keamanan
· Decision Pattern: EigenDA dan early AVS menggunakan operator set permissioned (dikelola Eigen Labs/Foundation). Mengurangi risiko operator malicious/incompetent di fase awal. Trade-off: centralization.
· Evidence: Phase 4 Core Components (EigenDA Operator "permissioned operator set initially"), Known Limitations ("Operator Permissioning Centralization"), Phase 8 Ecosystem Risks (EigenDA Operator Permissioning Centralization - High severity)
· Trigger: AVS framework baru, slashing mechanics untested production, operator software immature
· Response: Kurasi operator set; hardware/spec requirements; monitoring ketat; roadmap permissionless
· Result: EigenDA mainnet stable April-Oct 2024; zero slashing incidents; tapi centralization risk tetap
· Supporting Dataset: Phase 4 Core Components, Known Limitations, Phase 8 Ecosystem Risks

Pola 3: Withdrawal Delay & Veto Period sebagai Slashing Safety Net
· Decision Pattern: 7-day withdrawal delay (DelegationManager) + slashing veto period (SlashingManager, default ~7 hari) → total 14 hari buffer sebelum slashing final. Memberi waktu untuk challenge/dispute.
· Evidence: Phase 4 Core Components (DelegationManager withdrawal delay, SlashingManager veto period), Security Model (Withdrawal Delay, Slashing Mechanism), Known Limitations (Withdrawal Delay)
· Trigger: Slashing risk untuk staker/operator; butuh waktu detect & challenge false slashing
· Response: Mandatory delay di protocol level; veto period untuk governance/operator challenge
· Result: Tidak ada slashing incident mainnet → mechanism untested tapi ada safety net
· Supporting Dataset: Phase 4 Core Components, Security Model, Known Limitations

Pola 4: Foundation Multisig Emergency Control — Upgradeability Risk Mitigation
· Decision Pattern: Proxy admin di Foundation multisig (bukan single key). Bisa emergency pause/upgrade jika critical bug ditemukan. Transisi ke on-chain governance bertahap.
· Evidence: Phase 4 Security Model (Multi-sig/Governance upgradeability), Phase 7 Governance Ecosystem (Foundation multisig transitional control), Phase 8 Ecosystem Risks (Upgradeability via Foundation Multisig - Medium severity)
· Trigger: Smart contract upgradeability risk; butuh emergency response capability
· Response: Multisig (multi-party) control; timelock untuk non-emergency; plan transisi ke token governance
· Result: Zero emergency upgrade needed to date; multisig sebagai safety net
· Supporting Dataset: Phase 4 Security Model, Phase 7 Governance Ecosystem, Phase 8 Ecosystem Risks

Pola 5: Multiple Independent Audits per Component — Defense in Depth
· Decision Pattern: 7 audits dari 4 firm berbeda (Spearbit 3x, Trail of Bits 2x, Sigma Prime 1x, OpenZeppelin 1x) covering core contracts, EigenDA, EIGEN token. Setiap major upgrade audit ulang.
· Evidence: Phase 4 Audit History (7 audits detailed), Phase 4 Technical Upgrade History (audit per upgrade)
· Trigger: High-value protocol ($18B+ TVL), novel mechanics (restaking, slashing, intersubjective work)
· Response: Diverse auditor set; repeated audits; public audit reports di GitHub
· Result: Zero critical bugs mainnet; findings addressed pre-launch each phase
· Supporting Dataset: Phase 4 Audit History, Technical Upgrade History

Pola 6: No Slashing Insurance — Risk Fully Borne by Stakers/Operators
· Decision Pattern: Protokol tidak menyediakan insurance fund, slashing coverage, atau safety module. Full loss ditanggung staker/operator. LRT protocol mungkin punya risk management sendiri tapi tidak di-level protokol.
· Evidence: Phase 4 Security Model (no insurance mentioned), Phase 8 Ecosystem Risks (Slashing Insurance Absence - Medium severity), Phase 5 Financial Risk (Slashing Financial Exposure)
· Trigger: Slashing risk inherent to restaking; insurance mahal/kompleks
· Response: Transparan tentang risk; withdrawal delay sebagai mitigation; staker/operator do own risk management
· Result: Capital efficiency lower (staker butuh risk premium); LRT protocol jadi risk intermediary
· Supporting Dataset: Phase 4 Security Model, Phase 8 Ecosystem Risks, Phase 5 Financial Risk

Recurring Behavioral Pattern

Pola 1: Selalu Audit Sebelum Major Launch/Upgrade
· Pattern: Setiap 7 major upgrade (Phase 4 Technical Upgrade History) didahului audit dari firm top-tier. Tidak ada launch tanpa audit.
· Evidence: Phase 4 Audit History (7 audits mapped ke timeline: Spearbit May 2023 pre-mainnet, Trail of Bits Jun 2023 pre-mainnet, Sigma Prime Jul 2023 post-phase1, OpenZeppelin Mar 2024 pre-EigenDA, Spearbit Apr 2024 EigenDA, Trail of Bits Aug 2024 EIGEN token, Spearbit Sep 2024 token distribution)
· Supporting Dataset: Phase 4 Audit History, Technical Upgrade History

Pola 2: Ekspansi Ekosistem Pasca-Funding
· Pattern: Series A Feb 2023 → Testnet Apr 2023 → Mainnet Jun 2023 → LST Sep 2023 → LRT Dec 2023. Series B Feb 2024 → EigenDA Apr 2024 → 3 AVS Apr 2024 → Foundation Jul 2024 → TGE Oct 2024. Funding memicu hiring & building spree.
· Evidence: Phase 3 Historical Events timeline correlated dengan Phase 5 Funding History (EV-003 → EV-004/005/006/007; EV-008 → EV-009/010/011/012/013/014)
· Supporting Dataset: Phase 3 Historical Events, Phase 5 Funding History

Pola 3: LRT Protocol Integration Sebagai Growth Lever Utama
· Pattern: Setiap LRT baru (EtherFi Jul 2023, Renzo/Kelp/Puffer/Swell Dec 2023) drive TVL lonjak. EigenLayer tidak build LRT sendiri — enable platform untuk LRT builders.
· Evidence: Phase 3 EV-006, EV-007; Phase 7 External Dependencies (5 LRT protocols Critical/High); Phase 8 Adoption Metrics (TVL ~$18.5B, 4.8M ETH equivalent mostly via LRT)
· Supporting Dataset: Phase 3 EV-006, EV-007, Phase 7 External Dependencies, Phase 8 Adoption Metrics

Pola 4: Token Launch Setelah Product-Market Fit & Live Revenue
· Pattern: TGE Oct 2024 setelah: mainnet 16 bulan, $18B+ TVL, 4 AVS live, EigenDA revenue live, 5 LRT integrated. Bukan pre-product token launch.
· Evidence: Phase 3 EV-012 (TGE timeline), Phase 8 Market Position (Project Stage: Growth), Phase 5 Revenue Model (EigenDA fees live since Apr 2024)
· Supporting Dataset: Phase 3 EV-012, Phase 8 Market Position, Phase 5 Revenue Model

Pola 5: Dual Entity Structure (Labs + Foundation) Sebagai Permanent Pattern
· Pattern: Eigen Labs (dev) + Eigen Foundation (gov/token/treasury) dipisah sejak 2024 (EV-011) dan bertahan. Tidak ada plan merge. Foundation multisig kontrol upgrade.
· Evidence: Phase 2 Entity (both active), Phase 3 EV-011, Phase 7 Governance Ecosystem (Foundation role), Phase 8 Ecosystem Risks (Upgradeability via Foundation Multisig)
· Supporting Dataset: Phase 2 Entity, Phase 3 EV-011, Phase 7 Governance Ecosystem, Phase 8 Ecosystem Risks

Pola 6: Phased Decentralization — Permissioned Dulu, Permissionless Kemudian (Janji)
· Pattern: EigenDA operator permissioned, AVS onboarding butuh governance approval, Foundation multisig kontrol upgrade. Semua diberi label "progressive decentralization" tapi timeline/kriteria vague.
· Evidence: Phase 4 Known Limitations (Operator Permissioning), Phase 7 Infrastructure Providers (EigenDA Operators permissioned), Phase 8 Ecosystem Risks (EigenDA Operator Permissioning Centralization), Phase 7 Governance Ecosystem (AVS Onboarding Committee planned)
· Supporting Dataset: Phase 4 Known Limitations, Phase 7 Infrastructure Providers, Phase 8 Ecosystem Risks, Phase 7 Governance Ecosystem

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Keamanan/Kecepatan Eksekusi (Operator Permissioning)
· Decision: Menggunakan operator set permissioned untuk EigenDA dan early AVS
· Trade-off: Mengorbankan desentralisasi operator (centralization risk, single point of failure, censorship resistance rendah) demi keamanan operasional (operator terkurasi, hardware verified, slashing risk minimized) dan speed to market
· Evidence: Phase 4 Known Limitations ("Operator Permissioning: EigenDA and early AVS use permissioned operator sets"), Phase 8 Ecosystem Risks (EigenDA Operator Permissioning Centralization - High severity), Phase 7 Infrastructure Providers (EigenDA Operators permissioned)
· Supporting Dataset: Phase 4 Known Limitations, Phase 8 Ecosystem Risks, Phase 7 Infrastructure Providers

Trade-off 2: Capital Efficiency vs Slashing Safety (Withdrawal Delay)
· Decision: Mandatory 7-day withdrawal delay + EigenPod exit queue (compound delay)
· Trade-off: Mengorbankan capital efficiency (staked ETH illiquid 7-30+ hari) dan user experience (no instant withdraw) demi slashing detection window dan economic security guarantee
· Evidence: Phase 4 Core Components (DelegationManager withdrawal delay, EigenPodManager exit queue), Known Limitations (Withdrawal Delay, EigenPod Exit Queue), Phase 8 Ecosystem Risks (Liquidity Risk - High severity)
· Supporting Dataset: Phase 4 Core Components, Known Limitations, Phase 8 Ecosystem Risks

Trade-off 3: Protocol Revenue vs Ecosystem Growth (No Core Protocol Fees)
· Decision: EigenLayer core tidak charge fee pada restaking/delegation/slashing; revenue hanya dari EigenDA
· Trade-off: Mengorbankan direct protocol revenue dan value capture ke token holders demi menarik more stakers, operators, AVS ke platform (lower friction, higher TVL, network effects)
· Evidence: Phase 5 Revenue Model (Protocol Fees: Planned/Not Live), Phase 4 Core Components (no fee params in StrategyManager/DelegationManager), Phase 8 Market Position (Revenue only EigenDA)
· Supporting Dataset: Phase 5 Revenue Model, Phase 4 Core Components, Phase 8 Market Position

Trade-off 4: Investor/Team Token Concentration vs Funding Certainty
· Decision: 29.5% investors + 15% team + 10.5% foundation = 55% supply locked tapi terkonsentrasi; vesting cliff 12 bulan
· Trade-off: Mengorbankan token distribution decentralization dan governance capture resistance demi secure $150M+ venture funding untuk build protokol tanpa public sale pressure
· Evidence: Phase 6 Distribution, Vesting Schedule, Phase 8 Ecosystem Risks (VC Token Concentration - Medium severity), Phase 5 Funding History
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule, Phase 8 Ecosystem Risks, Phase 5 Funding History

Trade-off 5: Intersubjective Slashing Subjectivity vs Objective-Only Security
· Decision: Memperkenalkan EIGEN token untuk intersubjective work slashing (social consensus) di atas objective slashing
· Trade-off: Mengorbankan objective enforceability dan trust-minimization (social consensus butuh trusted parties, governance process, appeal mechanism) demi coverage ke fault classes yang tidak objectively verifiable (data withholding, oracle manipulation)
· Evidence: Phase 4 Consensus Mechanism (Intersubjective Consensus), Security Model (Intersubjective Slashing), Phase 6 Utility (Intersubjective Work Staking, Collateral/Slashing), Phase 8 Ecosystem Risks (Intersubjective Slashing Governance Dependency - Medium severity)
· Supporting Dataset: Phase 4 Consensus Mechanism, Security Model, Phase 6 Utility, Phase 8 Ecosystem Risks

Trade-off 6: Single Chain Focus (Ethereum) vs Multi-Chain Expansion
· Decision: Semua core contracts, staking, slashing, token hanya di Ethereum mainnet
· Trade-off: Mengorbangkan multi-chain reach, cross-chain restaking, dan larger TAM demi security alignment dengan Ethereum validator set, simpler architecture, dan focus execution
· Evidence: Phase 4 System Architecture ("Settlement Layer: Ethereum mainnet"), Known Limitations ("Single Settlement Chain: Currently only Ethereum mainnet"), Phase 8 Market Position (Primary Chain: Ethereum)
· Supporting Dataset: Phase 4 System Architecture, Known Limitations, Phase 8 Market Position

Behavioral Summary

Prioritas Utama Proyek:
1. Security First — Phased rollout, extensive audits, withdrawal delays, permissioned operators, objective slashing dulu. Zero exploit track record.
2. Ethereum Alignment — Tidak bangun chain/consensus sendiri; leverage Ethereum security, validator set, finality. Max composability dengan Ethereum ecosystem.
3. Ecosystem Enablement — Build platform (StrategyManager, AVSRegistry, SDKs) untuk LRT & AVS builders, bukan kompetisi dengan mereka. LRT & AVS jadi growth engine.
4. Long-term Credible Neutrality — Dual entity (Labs/Foundation), progressive decentralization roadmap, community token allocation (45%), on-chain governance transition.

Cara Mengambil Keputusan:
- Data-driven & security-paranoid: Setiap major decision didahului audit, testnet, phased mainnet. Metrics (TVL, operator count, AVS live) dipakai validate progress.
- Founder-led vision dengan team execution: Sreeram set direction (restaking thesis); Luke/Robert/Calvin execute (strategy, tech, ops). Board (VC) influence via token allocation.
- Community feedback loop: Season-based distribution berbasis aktivitas; governance proposals dari stakers; developer grants bottom-up.
- Conservative upgrades: Proxy upgradeability hanya via Foundation multisig; timelock; emergency pause capability.

Faktor Paling Sering Mempengaruhi Keputusan:
1. Security Risk — Slashing mechanics, withdrawal delay, operator permissioning, audit coverage selalu prioritized over speed/features.
2. Ethereum Constraints — Gas costs, validator exit queue, L1 finality, EVM limitations shape architecture (no native cross-chain, no instant withdraw).
3. Capital/TVL Growth — LRT integrations, AVS onboarding, EigenDA revenue drive decisions; TVL = primary success metric.
4. Regulatory/Legal — Dual entity (Delaware/Cayman), token classification uncertainty, no public sale, Foundation structure semua driven by legal.
5. Investor Expectations — $150M funding, token allocation, vesting schedules, unicorn valuation create obligations & constraints.

Pola Evolusi:
- Dari Core Protocol → Platform → Modular Stack: Semakin modular, semakin banyak external dependencies (LRT, AVS, operators, rollups).
- Dari Centralized → Transitional → Decentralized (Target): Foundation multisig → EIGEN staking governance → permissionless AVS/operator. Masih di fase transitional.
- Dari No Token → Token dengan Utility Real: EIGEN bukan governance token saja; staking untuk intersubjective work, slashing collateral, AVS security. Utility-first.

Kekuatan Utama:
1. First-mover & Market Leader: 85-90% restaking TVL share, 16+ bulan mainnet track record, $18B+ TVL.
2. Deep Technical Moat: Novel restaking architecture, EigenPod (native ETH), slashing framework, EigenDA erasure coding, intersubjective work innovation.
3. Strong Ecosystem Flywheel: LRT protocols bring capital → operators secure AVS → AVS generate yield → attract more capital. 5 LRT + 4 AVS live.
4. World-class Team & Backing: Sreeram (academic credentials), Robert (CTO ex-AWS/ConsenSys), a16z/Blockchain Capital backing, top-tier auditors.
5. Token Utility Beyond Governance: Intersubjective work staking, slashing collateral, AVS security token — real economic function.

Kelemahan Utama:
1. Centralization Risks: Permissioned operators (EigenDA), Foundation multisig upgrade control, VC/team token concentration (55%), LRT protocol concentration (top 3 = majority TVL).
2. Liquidity/UX Friction: 7-day withdrawal delay + EigenPod exit queue = compound illiquidity. LRT tokens help tapi tambah layer risk.
3. Single Chain Dependency: 100% Ethereum L1. Gas spikes, congestion, validator queue langsung impact semua operasi. No multi-chain hedge.
4. Revenue Uncertainty: Core protocol no fees; EigenDA revenue baru, unproven scale; AVS fees tidak ke core. Burn rate VC-funded.
5. Intersubjective Slashing Unproven: Social consensus mechanism complex, governance-dependent, appeal process unclear. Legal/regulatory risk pada slashing decisions.
6. AVS Development Barrier Tinggi: Custom off-chain + on-chain per AVS; no cookie-cutter framework; slow ecosystem expansion.

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: EigenLayer

Core Insights

Insight 1: Restaking sebagai kategori baru menciptakan pasar keamanan bersama yang previously tidak ada
Explanation: EigenLayer memperkenalkan konsep restaking — memungkinkan ETH yang sudah di-stake di Ethereum digunakan kembali untuk mengamankan layanan terdistribusi (AVS) melalui mekanisme slashing. Ini mengubah ETH dari passive staking asset menjadi active security capital.
Evidence: Phase 1 mendefinisikan kategori "restaking (restaking) / liquidity re-staking; middleware / Actively Validated Services (AVS) infrastructure"【Phase 1 — Category】; Phase 3 EV-005 meluncurkan mainnet fase 1 native ETH restaking Juni 2023【Phase 3 — EV-005】; Phase 8 Market Position menempatkan EigenLayer sebagai "Main Narrative: Restaking (EigenLayer is the pioneer and market leader)"【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 1 Foundation, Phase 3 Historical Events, Phase 8 Market
Confidence: HIGH

Insight 2: Phased rollout dengan audit berulang menciptakan track record zero-exploit pada $18B+ TVL
Explanation: Setiap major upgrade (native restaking, LST, LRT, EigenDA, AVS, token) diluncurkan bertahap dengan audit terpisah dari firm top-tier. Pola ini meminimalkan blast radius dan memvalidasi keamanan sebelum ekspansi.
Evidence: Phase 4 Technical Upgrade History mencatat 7 major upgrades bertahap 2023-2024【Phase 4 — Technical Upgrade History】; Phase 4 Audit History mencatat 7 audits dari 4 firm berbeda (Spearbit 3x, Trail of Bits 2x, Sigma Prime 1x, OpenZeppelin 1x)【Phase 4 — Audit History】; Phase 9 Risk Response Pattern 1 mengonfirmasi "Setiap 7 major upgrade didahului audit dari firm top-tier. Tidak ada launch tanpa audit"【Phase 9 — Risk Response Pattern 1】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Insight 3: LRT protocol (bukan protokol inti) menjadi growth engine utama TVL
Explanation: EigenLayer tidak membangun LRT sendiri; menyediakan StrategyManager sebagai platform. EtherFi, Renzo, Kelp, Puffer, Swell drive TVL dari ~$0 ke $18.5B dalam 16 bulan. Top 3 LRT = majority TVL.
Evidence: Phase 3 EV-006/007 mencatat integrasi 5 LRT protocol【Phase 3 — EV-006】【Phase 3 — EV-007】; Phase 7 External Dependencies menandai 5 LRT protocol sebagai Critical/High criticality【Phase 7 — External Dependencies】; Phase 8 Adoption Metrics TVL ~$18.5B, 4.8M ETH equivalent【Phase 8 — Adoption Metrics】; Phase 9 Ecosystem Decision Pattern 1 "LRT Protocol sebagai Primary Growth Engine"【Phase 9 — Ecosystem Decision Pattern 1】.
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Insight 4: Dual-entity structure (Labs + Foundation) memisahkan development dari governance/token
Explanation: Eigen Labs Inc (Delaware) handle core development; Eigen Foundation (Cayman) handle token issuance, treasury, governance, grants. Struktur ini permanen, bukan transisional.
Evidence: Phase 2 Entity mencatat Eigen Labs Inc dan Eigen Foundation sebagai entitas terpisah【Phase 2 — Entity】; Phase 3 EV-011 pembentukan Eigen Foundation Juli 2024【Phase 3 — EV-011】; Phase 7 Governance Ecosystem Foundation role: treasury, grants, governance execution, upgrade authority【Phase 7 — Governance Ecosystem】; Phase 9 Recurring Behavioral Pattern 5 "Dual Entity Structure sebagai Permanent Pattern"【Phase 9 — Recurring Behavioral Pattern 5】.
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Insight 5: Intersubjective work token (EIGEN) memperluas slashing ke fault yang tidak objectively verifiable
Explanation: Objective slashing (equivocation, invalid attestation) di-enforce on-chain via SlashingManager. Intersubjective faults (data withholding, oracle manipulation) butuh social consensus → EIGEN token dengan mechanics terpisah. Ini inovasi ekonomi kripto baru.
Evidence: Phase 4 Consensus Mechanism "Intersubjective Consensus (EIGEN token): Introduced with EIGEN token for 'intersubjective work'"【Phase 4 — Consensus Mechanism】; Phase 6 Utility "Intersubjective Work Staking (Security)" dan "Collateral (Slashing)"【Phase 6 — Utility】; Phase 9 Technical Decision Pattern 4 "Objective Slashing Dulu, Intersubjective Slashing Kemudian via Token Baru"【Phase 9 — Technical Decision Pattern 4】.
Supporting Dataset: Phase 4 Technology, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Insight 6: EigenDA sebagai first-party AVS memvalidasi framework dan generate revenue
Explanation: EigenLayer membangun AVS pertama sendiri (EigenDA) bukan menunggu third-party. Memvalidasi AVS framework, generate protocol revenue (service fees), jadi template untuk AVS lain.
Evidence: Phase 3 EV-009 EigenDA mainnet April 2024【Phase 3 — EV-009】; Phase 5 Revenue Model "EigenDA Service Fees: Live since 2024-04"【Phase 5 — Revenue Model】; Phase 9 Ecosystem Decision Pattern 2 "EigenDA sebagai First-Party AVS untuk Validasi Framework & Revenue"【Phase 9 — Ecosystem Decision Pattern 2】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Insight 7: Permissioned operator set untuk early AVS — trade-off desentralisasi demi keamanan operasional
Explanation: EigenDA dan early AVS menggunakan operator set permissioned (dikelola Eigen Labs/Foundation). Mengurangi risiko operator malicious/incompetent di fase awal. Roadmap "progressive decentralization" tapi tanpa timeline konkret.
Evidence: Phase 4 Core Components "EigenDA Operator: Live, permissioned operator set initially"【Phase 4 — Core Components】; Phase 4 Known Limitations "Operator Permissioning: EigenDA and early AVS use permissioned operator sets"【Phase 4 — Known Limitations】; Phase 8 Ecosystem Risks "EigenDA Operator Permissioning Centralization - High severity"【Phase 8 — Ecosystem Risks】; Phase 9 Strategic Trade-offs 1 "Desentralisasi vs Keamanan/Kecepatan Eksekusi"【Phase 9 — Strategic Trade-offs 1】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Insight 8: Withdrawal delay mandatory (7 hari) + EigenPod exit queue = compound illiquidity
Explanation: 7-day withdrawal delay di DelegationManager untuk slashing window. Native ETH restaking via EigenPod menambah Ethereum validator exit queue. Total illiquidity 7-30+ hari. LRT token memberikan likuiditas sintetis tapi tambah layer risk.
Evidence: Phase 4 Core Components DelegationManager withdrawal delay, EigenPodManager exit queue【Phase 4 — Core Components】; Phase 4 Known Limitations "Withdrawal Delay" dan "EigenPod Exit Queue"【Phase 4 — Known Limitations】; Phase 8 Ecosystem Risks "Liquidity Risk - High severity"【Phase 8 — Ecosystem Risks】; Phase 9 Strategic Trade-offs 2 "Capital Efficiency vs Slashing Safety"【Phase 9 — Strategic Trade-offs 2】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Insight 9: Token launch setelah product-market fit & live revenue (bukan pre-product)
Explanation: TGE Oktober 2024 setelah: mainnet 16 bulan, $18B+ TVL, 4 AVS live, EigenDA revenue live, 5 LRT integrated. 45% community allocation via Season-based distribution berbasis aktivitas.
Evidence: Phase 3 EV-012 TGE Oct 2024 timeline【Phase 3 — EV-012】; Phase 8 Market Position "Project Stage: Growth"【Phase 8 — Market Position】; Phase 5 Revenue Model EigenDA fees live since Apr 2024【Phase 5 — Revenue Model】; Phase 9 Recurring Behavioral Pattern 4 "Token Launch Setelah Product-Market Fit & Live Revenue"【Phase 9 — Recurring Behavioral Pattern 4】.
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Insight 10: VC/Team/Foundation token concentration 55% vs Community 45% — governance capture risk
Explanation: Investors 29.5% + Team 15% + Foundation 10.5% = 55% supply locked tapi terkonsentrasi. Vesting cliff 12 bulan (Oct 2025) = overhang supply besar. Community 45% tapi hanya 5% unlocked at TGE.
Evidence: Phase 6 Distribution "Community 45%, Team 15%, Investors 29.5%, Foundation 10.5%"【Phase 6 — Distribution】; Phase 6 Vesting Schedule Team/Investor cliff 12 bulan【Phase 6 — Vesting Schedule】; Phase 8 Ecosystem Risks "VC Token Concentration - Medium severity"【Phase 8 — Ecosystem Risks】; Phase 9 Financial Decision Pattern 4 "Token Allocation Berbobot ke Investor & Team"【Phase 9 — Financial Decision Pattern 4】.
Supporting Dataset: Phase 6 Token, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Strategic Principles

Principle 1: Security First — Phased rollout, extensive audits, withdrawal delays, permissioned operators, objective slashing dulu
Explanation: Setiap keputusan major diprioritaskan keamanan over speed/features. Zero exploit track record 16+ bulan mainnet.
Evidence: Phase 9 Behavioral Summary "Prioritas Utama: Security First — Phased rollout, extensive audits, withdrawal delays, permissioned operators, objective slashing dulu. Zero exploit track record"【Phase 9 — Behavioral Summary】; Phase 4 Audit History 7 audits【Phase 4 — Audit History】; Phase 4 Known Limitations acknowledged risks per phase【Phase 4 — Known Limitations】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 2: Ethereum Alignment — Tidak bangun chain/consensus sendiri; leverage Ethereum security, validator set, finality
Explanation: Semua core contracts, staking, slashing, token hanya di Ethereum mainnet. EigenPod menggunakan beacon chain withdrawal credentials. Max composability dengan Ethereum ecosystem.
Evidence: Phase 4 System Architecture "Settlement Layer: Ethereum mainnet"【Phase 4 — System Architecture】; Phase 4 Consensus Mechanism "Ethereum Consensus: EigenLayer does not have its own consensus"【Phase 4 — Consensus Mechanism】; Phase 9 Technical Decision Pattern 1 "Ethereum Alignment First — Semua Kembali ke Ethereum"【Phase 9 — Technical Decision Pattern 1】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 3: Ecosystem Enablement — Build platform untuk LRT & AVS builders, bukan kompetisi dengan mereka
Explanation: EigenLayer menyediakan StrategyManager, AVSRegistry, SDKs sebagai rails. LRT & AVS jadi growth engine. EigenLayer tidak build LRT sendiri.
Evidence: Phase 7 External Dependencies 5 LRT protocols Critical/High【Phase 7 — External Dependencies】; Phase 9 Ecosystem Decision Pattern 1 "LRT Protocol sebagai Primary Growth Engine"【Phase 9 — Ecosystem Decision Pattern 1】; Phase 9 Behavioral Summary "Ecosystem Enablement — Build platform untuk LRT & AVS builders, bukan kompetisi dengan mereka"【Phase 9 — Behavioral Summary】.
Supporting Dataset: Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Principle 4: Long-term Credible Neutrality — Dual entity, progressive decentralization roadmap, community token allocation, on-chain governance transition
Explanation: Struktur dual entity (Labs/Foundation), 45% community allocation, roadmap ke permissionless AVS/operator, transisi ke on-chain governance via EIGEN staking.
Evidence: Phase 2 Entity dual structure【Phase 2 — Entity】; Phase 6 Distribution Community 45%【Phase 6 — Distribution】; Phase 6 Governance "Token-weighted voting via staked EIGEN... partially live"【Phase 6 — Governance】; Phase 9 Recurring Behavioral Pattern 5 "Dual Entity Structure sebagai Permanent Pattern"【Phase 9 — Recurring Behavioral Pattern 5】; Phase 9 Recurring Behavioral Pattern 6 "Phased Decentralization"【Phase 9 — Recurring Behavioral Pattern 6】.
Supporting Dataset: Phase 2 Entity, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Principle 5: Modular Architecture — Protokol menyediakan rails (staking, delegation, slashing, registry), AVS bangun off-chain + service manager sendiri
Explanation: EigenLayer core hanya: StrategyManager, DelegationManager, SlashingManager, AllocationManager, AVSRegistry. AVS custom build disperser/retriever/operator software.
Evidence: Phase 4 Core Components 10+ core contracts【Phase 4 — Core Components】; Phase 4 Technical Decision Pattern 3 "Modular AVS Framework — Protokol Menyediakan Rails, AVS Bangun Sendiri"【Phase 9 — Technical Decision Pattern 3】; Phase 7 Major Integrations masing-masing AVS punya ServiceManager sendiri【Phase 7 — Major Integrations】.
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Principle 6: Phased Rollout dengan Scope Minimal per Fase
Explanation: Setiap mainnet launch membatasi fungsi: Phase 1 hanya native ETH; LST support bulan 3 kemudian; LRT support bulan 6 kemudian; EigenDA & AVS terpisah 10 bulan kemudian. Setiap fase audit ulang.
Evidence: Phase 3 Historical Events 14 events over 3+ years phased【Phase 3 — Historical Events】; Phase 4 Technical Upgrade History 7 major upgrades bertahap【Phase 4 — Technical Upgrade History】; Phase 9 Technical Decision Pattern 2 "Phased Rollout dengan Scope Minimal per Fase"【Phase 9 — Technical Decision Pattern 2】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Success Factors

Factor 1: First-mover advantage dalam restaking category dengan 16+ bulan mainnet track record
Explanation: EigenLayer meluncurkan mainnet Juni 2023, 85-90% restaking TVL market share, $18B+ TVL. Competitor (Symbiotic, Karak) baru launch 2024.
Evidence: Phase 8 Market Share "Restaking TVL Market Share ~85-90%"【Phase 8 — Market Share】; Phase 8 Market Timeline mainnet Jun 2023 vs competitor 2024【Phase 8 — Market Timeline】; Phase 9 Behavioral Summary "First-mover & Market Leader: 85-90% restaking TVL share, 16+ bulan mainnet track record"【Phase 9 — Behavioral Summary】.
Supporting Dataset: Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 2: Deep technical moat — novel architecture (EigenPod, slashing framework, EigenDA erasure coding, intersubjective work)
Explanation: EigenPod memungkinkan native ETH restaking via beacon chain withdrawal credentials. EigenDA erasure coding + disperser/retriever architecture. Intersubjective work token innovation.
Evidence: Phase 4 Core Components EigenPodManager【Phase 4 — Core Components】; Phase 4 EigenDA Components disperser/retriever/erasure coding【Phase 4 — EigenDA Components】; Phase 4 Consensus Mechanism Intersubjective Consensus【Phase 4 — Consensus Mechanism】; Phase 9 Behavioral Summary "Deep Technical Moat: Novel restaking architecture, EigenPod, slashing framework, EigenDA erasure coding, intersubjective work innovation"【Phase 9 — Behavioral Summary】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Factor 3: Strong ecosystem flywheel — LRT protocols bring capital → operators secure AVS → AVS generate yield → attract more capital
Explanation: 5 LRT protocols + 4 AVS live. TVL tumbuh dari $0 ke $18.5B. EigenDA revenue live. Network effects berkembang.
Evidence: Phase 8 Adoption Metrics TVL $18.5B, 4.8M ETH equivalent【Phase 8 — Adoption Metrics】; Phase 7 Major Integrations 5 LRT + 4 AVS【Phase 7 — Major Integrations】; Phase 5 Revenue Model EigenDA fees live【Phase 5 — Revenue Model】; Phase 9 Behavioral Summary "Strong Ecosystem Flywheel: LRT protocols bring capital → operators secure AVS → AVS generate yield → attract more capital"【Phase 9 — Behavioral Summary】.
Supporting Dataset: Phase 8 Market, Phase 7 Ecosystem, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Factor 4: World-class team & backing — Sreeram (academic), Robert (CTO ex-AWS/ConsenSys), a16z/Blockchain Capital backing, top-tier auditors
Explanation: Core team berpedigree tinggi. $150M funding dari top-tier VC. 7 audits dari 4 firm ternama (Spearbit, Trail of Bits, Sigma Prime, OpenZeppelin).
Evidence: Phase 2 Entity Core Team Sreeram, Luke, Robert, Calvin【Phase 2 — Entity】; Phase 5 Funding History Series A $50M Blockchain Capital, Series B $100M a16z【Phase 5 — Funding History】; Phase 4 Audit History 7 audits dari 4 firm【Phase 4 — Audit History】; Phase 9 Behavioral Summary "World-class Team & Backing"【Phase 9 — Behavioral Summary】.
Supporting Dataset: Phase 2 Entity, Phase 5 Financial, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Factor 5: Token utility beyond governance — Intersubjective work staking, slashing collateral, AVS security token
Explanation: EIGEN bukan governance token saja; staking untuk intersubjective work, slashing collateral, AVS security token. Real economic function.
Evidence: Phase 6 Utility 6 utilities: Governance, Intersubjective Work Staking, AVS Security, Fee Payment planned, Operator Incentive, Collateral/Slashing【Phase 6 — Utility】; Phase 9 Behavioral Summary "Token Utility Beyond Governance: Intersubjective work staking, slashing collateral, AVS security token — real economic function"【Phase 9 — Behavioral Summary】.
Supporting Dataset: Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Factor 6: Phased decentralization strategy yang kredibel — permissioned awal, roadmap ke permissionless, community distribution 45%
Explanation: Meskipun operator permissioned dan Foundation multisig kontrol upgrade, roadmap "progressive decentralization" dengan Season-based community distribution (45%) dan on-chain governance transition memberikan sinyal credibile neutrality.
Evidence: Phase 6 Distribution Community 45%【Phase 6 — Distribution】; Phase 6 Governance on-chain voting via staked EIGEN partially live【Phase 6 — Governance】; Phase 9 Recurring Behavioral Pattern 6 "Phased Decentralization"【Phase 9 — Recurring Behavioral Pattern 6】; Phase 4 Known Limitations acknowledged centralization risks【Phase 4 — Known Limitations】.
Supporting Dataset: Phase 6 Token, Phase 9 Behavioral
Confidence: MEDIUM

Failure Factors

Factor 1: Centralization risks — Permissioned operators (EigenDA), Foundation multisig upgrade control, VC/team token concentration 55%, LRT protocol concentration
Explanation: EigenDA operator set permissioned. Foundation multisig kontrol proxy admin. Investors 29.5% + Team 15% + Foundation 10.5% = 55% supply. Top 3 LRT = majority TVL. Semua menciptakan single points of failure dan governance capture risk.
Evidence: Phase 4 Known Limitations "Operator Permissioning Centralization"【Phase 4 — Known Limitations】; Phase 8 Ecosystem Risks "EigenDA Operator Permissioning Centralization - High severity", "VC Token Concentration - Medium severity", "LRT Protocol Concentration - High severity"【Phase 8 — Ecosystem Risks】; Phase 9 Strategic Trade-offs 4 "Investor/Team Token Concentration vs Funding Certainty"【Phase 9 — Strategic Trade-offs 4】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 2: Liquidity/UX friction — 7-day withdrawal delay + EigenPod exit queue = compound illiquidity 7-30+ hari
Explanation: Mandatory withdrawal delay untuk slashing window. Native ETH restaking menambah Ethereum validator exit queue. LRT token membantu tapi tambah layer risk (smart contract, depeg).
Evidence: Phase 4 Known Limitations "Withdrawal Delay", "EigenPod Exit Queue"【Phase 4 — Known Limitations】; Phase 8 Ecosystem Risks "Liquidity Risk - High severity"【Phase 8 — Ecosystem Risks】; Phase 9 Strategic Trade-offs 2 "Capital Efficiency vs Slashing Safety"【Phase 9 — Strategic Trade-offs 2】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 3: Single chain dependency — 100% Ethereum L1. Gas spikes, congestion, validator queue langsung impact semua operasi
Explanation: Semua core contracts, staking, slashing, token hanya di Ethereum mainnet. Tidak ada multi-chain hedge. EigenDA throughput limited by L1 gas costs.
Evidence: Phase 4 System Architecture "Settlement Layer: Ethereum mainnet"【Phase 4 — System Architecture】; Phase 4 Known Limitations "Single Settlement Chain: Currently only Ethereum mainnet"【Phase 4 — Known Limitations】; Phase 8 Market Position "Primary Chain: Ethereum"【Phase 8 — Market Position】; Phase 9 Strategic Trade-offs 6 "Single Chain Focus vs Multi-Chain Expansion"【Phase 9 — Strategic Trade-offs 6】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 4: Revenue uncertainty — Core protocol no fees; EigenDA revenue baru, unproven scale; AVS fees tidak ke core. Burn rate VC-funded
Explanation: EigenLayer core tidak charge fee. EigenDA fees live April 2024 tapi jumlah tidak diungkap. AVS fees per AVS basis, tidak ke core protocol. Operasional Eigen Labs dibiayai Series A/B $150M.
Evidence: Phase 5 Revenue Model "Protocol Fees: Planned/Not Live"【Phase 5 — Revenue Model】; Phase 5 Financial Risk "Funding Dependency: Operasional Eigen Labs bergantung pada venture funding... belum ada revenue protokol yang signifikan"【Phase 5 — Financial Risk】; Phase 9 Financial Decision Pattern 3 "Revenue Hanya dari EigenDA Service Fees"【Phase 9 — Financial Decision Pattern 3】; Phase 9 Financial Decision Pattern 6 "Eigen Labs Burn Rate Ditanggung VC Funding"【Phase 9 — Financial Decision Pattern 6】.
Supporting Dataset: Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Factor 5: Intersubjective slashing unproven — Social consensus mechanism complex, governance-dependent, appeal process unclear. Legal/regulatory risk
Explanation: EIGEN token slashing untuk intersubjective faults relies on social consensus dan governance process. Tidak objectively enforceable. Legal classification token (security vs utility) belum final.
Evidence: Phase 4 Security Model "Intersubjective Slashing (EIGEN): ... via social consensus"【Phase 4 — Security Model】; Phase 8 Ecosystem Risks "Intersubjective Slashing Governance Dependency - Medium severity"【Phase 8 — Ecosystem Risks】; Phase 9 Strategic Trade-offs 5 "Intersubjective Slashing Subjectivity vs Objective-Only Security"【Phase 9 — Strategic Trade-offs 5】; Phase 6 Open Threads "Tokenomics legal opinion / regulatory classification... tidak dipublikasikan"【Phase 6 — Open Threads】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral, Phase 6 Token
Confidence: MEDIUM

Factor 6: AVS development barrier tinggi — Custom off-chain + on-chain per AVS; no cookie-cutter framework; slow ecosystem expansion
Explanation: Setiap AVS harus bangun custom off-chain software, disperser/retriever, service manager contracts. Tidak ada "AVS template" cookie-cutter. Membatasi jumlah AVS yang bisa launch.
Evidence: Phase 4 Known Limitations "AVS Development Complexity: Building an AVS requires custom off-chain software... high barrier to entry"【Phase 4 — Known Limitations】; Phase 8 Ecosystem Risks "AVS Development Complexity"【Phase 8 — Ecosystem Risks】; Phase 9 Ecosystem Decision Pattern 5 "Developer Ecosystem via SDK/CLI/Grants — Bottom-Up AVS Building... Tidak ada 'AVS template' cookie-cutter"【Phase 9 — Ecosystem Decision Pattern 5】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: MEDIUM

Decision Framework

Step 1: Observe — Identifikasi peluang teknis/ekonomis di lapisan settlement Ethereum
Explanation: Sreeram mengidentifikasi peluang restaking ETH untuk shared security di Ethereum (2021). Validasi melalui riset akademik dan whitepaper.
Evidence: Phase 3 EV-001 Pendirian Eigen Labs 2021【Phase 3 — EV-001】; Phase 1 Founding Entity Sreeram Kannan Founder & CEO【Phase 1 — Founding Entity】; Phase 4 Official Technical Resources Whitepaper【Phase 4 — Official Technical Resources】.
Supporting Dataset: Phase 1 Foundation, Phase 3 History, Phase 4 Technology
Confidence: HIGH

Step 2: Evaluate — Technical feasibility audit, economic modeling, legal structure design
Explanation: Pre-Series A: riset arsitektur (EigenPod, slashing), tokenomics design (intersubjective work), dual-entity legal (Delaware Labs + Cayman Foundation). Audit Spears/Trail of Bits pre-mainnet.
Evidence: Phase 4 Audit History Spearbit May 2023, Trail of Bits Jun 2023 pre-mainnet【Phase 4 — Audit History】; Phase 2 Entity Eigen Labs Inc Delaware, Eigen Foundation Cayman【Phase 2 — Entity】; Phase 6 Token Distribution design 45% community【Phase 6 — Distribution】.
Supporting Dataset: Phase 4 Technology, Phase 2 Entity, Phase 6 Token
Confidence: HIGH

Step 3: Fund — Venture funding bertahap dengan token allocation untuk investor
Explanation: Series A $50M Feb 2023 (Blockchain Capital) → Series B $100M Feb 2024 (a16z, $1B valuation). Investor mendapat 29.5% token allocation vesting 12-36 bulan. No public token sale.
Evidence: Phase 5 Funding History Series A $50M, Series B $100M【Phase 5 — Funding History】; Phase 6 Vesting Schedule Investors cliff 12 bulan vesting 24-36 bulan【Phase 6 — Vesting Schedule】; Phase 6 Token Sale "Tidak ada public sale, launchpad, atau auction"【Phase 6 — Token Sale】.
Supporting Dataset: Phase 5 Financial, Phase 6 Token
Confidence: HIGH

Step 4: Develop — Phased development dengan audit per komponen
Explanation: Core contracts (StrategyManager, DelegationManager, SlashingManager, EigenPodManager) → LST support → LRT/AllocationManager → EigenDA contracts → AVSRegistry multi-quorum → EIGEN token contracts. Setiap fase audit terpisah.
Evidence: Phase 4 Technical Upgrade History 7 major upgrades bertahap【Phase 4 — Technical Upgrade History】; Phase 4 Audit History 7 audits mapped ke timeline【Phase 4 — Audit History】; Phase 9 Technical Decision Pattern 2 "Phased Rollout dengan Scope Minimal per Fase"【Phase 9 — Technical Decision Pattern 2】.
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Step 5: Launch — Phased mainnet launch dengan scope minimal, lalu ekspansi ekosistem
Explanation: Phase 1 native ETH only (Jun 2023) → LST (Sep 2023) → LRT (Dec 2023) → EigenDA mainnet (Apr 2024) → 3 AVS third-party (Apr 2024) → Foundation formation (Jul 2024) → TGE (Oct 2024) → Season 2 & Governance (Oct 2024).
Evidence: Phase 3 Historical Events EV-005 melalui EV-014【Phase 3 — Historical Events】; Phase 4 Technical Upgrade History 7 upgrades【Phase 4 — Technical Upgrade History】; Phase 9 Recurring Behavioral Pattern 2 "Ekspansi Ekosistem Pasca-Funding"【Phase 9 — Recurring Behavioral Pattern 2】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Step 6: Govern — Transitional multisig → on-chain token-weighted governance via EIGEN staking
Explanation: Foundation multisig kontrol proxy admin (emergency/upgrade). Transisi ke: EIGEN staking → Governor contracts → Timelock execution. Delegation supported. AVS Onboarding Committee planned.
Evidence: Phase 6 Governance "Token-weighted voting via staked EIGEN... partially live"【Phase 6 — Governance】; Phase 7 Governance Ecosystem "Foundation multisig transitional control... on-chain governance transitioning"【Phase 7 — Governance Ecosystem】; Phase 9 Governance Decision Pattern 2 "Transitional Multisig → On-Chain Governance via EIGEN Staking"【Phase 9 — Governance Decision Pattern 2】.
Supporting Dataset: Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Reusable Playbook

Playbook 1: Membangun kategori baru via phased rollout dengan audit berulang — "Security First" sebagai moat
Explanation: Luncurkan MVP minimal (native ETH only), audit top-tier, mainnet, monitor, lalu tambah fitur bertahap (LST, LRT, AVS, token). Setiap fase audit ulang. Menciptakan trust dan track record zero-exploit.
Evidence: Phase 3 EV-005 Phase 1 native only【Phase 3 — EV-005】; Phase 4 Audit History 7 audits dari 4 firm【Phase 4 — Audit History】; Phase 9 Risk Response Pattern 1 "Selalu Audit Sebelum Major Launch/Upgrade"【Phase 9 — Risk Response Pattern 1】; Phase 9 Technical Decision Pattern 2 "Phased Rollout dengan Scope Minimal per Fase"【Phase 9 — Technical Decision Pattern 2】.
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Playbook 2: Platform strategy — Build rails, enable ecosystem builders (LRT, AVS) sebagai growth engine
Explanation: Jangan build user-facing product sendiri. Bangun infrastructure (StrategyManager, AVSRegistry, SDKs) yang memungkinkan LRT protocols (EtherFi, Renzo, dll) dan AVS builders (AltLayer, Dymension, dll) bangun di atas. Protocol capture value via network effects & native AVS (EigenDA).
Evidence: Phase 7 External Dependencies 5 LRT protocols Critical/High【Phase 7 — External Dependencies】; Phase 9 Ecosystem Decision Pattern 1 "LRT Protocol sebagai Primary Growth Engine"【Phase 9 — Ecosystem Decision Pattern 1】; Phase 9 Ecosystem Decision Pattern 2 "EigenDA sebagai First-Party AVS"【Phase 9 — Ecosystem Decision Pattern 2】; Phase 9 Behavioral Summary "Ecosystem Enablement"【Phase 9 — Behavioral Summary】.
Supporting Dataset: Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Playbook 3: Dual-entity structure untuk credible neutrality — Labs (dev) + Foundation (gov/token/treasury)
Explanation: Pisahkan core development (corporate entity, venture-backed) dari protocol governance (non-profit foundation, token issuance, treasury, grants). Foundation multisig transitional control hingga on-chain governance live. Legal clarity untuk token classification.
Evidence: Phase 2 Entity Eigen Labs Inc Delaware + Eigen Foundation Cayman【Phase 2 — Entity】; Phase 3 EV-011 Foundation formation Juli 2024【Phase 3 — EV-011】; Phase 7 Governance Ecosystem Foundation role【Phase 7 — Governance Ecosystem】; Phase 9 Recurring Behavioral Pattern 5 "Dual Entity Structure sebagai Permanent Pattern"【Phase 9 — Recurring Behavioral Pattern 5】.
Supporting Dataset: Phase 2 Entity, Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Playbook 4: Token launch setelah product-market fit & live revenue — bukan pre-product
Explanation: Tunggu mainnet mature (16+ bulan), significant TVL ($18B+), live AVS dengan revenue (EigenDA), established ecosystem (5 LRT). Token utility real (intersubjective work, slashing collateral, AVS security) bukan governance only. Community distribution 45% via Season-based berbasis aktivitas.
Evidence: Phase 3 EV-012 TGE Oct 2024 timeline【Phase 3 — EV-012】; Phase 8 Market Position "Project Stage: Growth"【Phase 8 — Market Position】; Phase 5 Revenue Model EigenDA fees live Apr 2024【Phase 5 — Revenue Model】; Phase 9 Recurring Behavioral Pattern 4 "Token Launch Setelah Product-Market Fit & Live Revenue"【Phase 9 — Recurring Behavioral Pattern 4】.
Supporting Dataset: Phase 3 History, Phase 8 Market, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Playbook 5: Coordinated multi-partner launch untuk momentum ekosistem
Explanation: Launch multiple AVS/integrasi bersamaan (AltLayer, Dymension, Lagrange Apr 2024) bukan sequential. Koordinasi dengan partner untuk demonstrasi shared security model yang nyata. Menciptakan narrative "ecosystem arriving" bukan "single product launching".
Evidence: Phase 3 EV-010 3 AVS launch April 2024 bersamaan【Phase 3 — EV-010】; Phase 7 Major Integrations 3 AVS integration same timeline【Phase 7 — Major Integrations】; Phase 9 Ecosystem Decision Pattern 3 "Coordinated Multi-AVS Launch untuk Momentum Ekosistem"【Phase 9 — Ecosystem Decision Pattern 3】.
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Playbook 6: CEX listing strategy — Major exchanges day-1 spot, no derivatives at launch
Explanation: Secure Binance (lead) + Bybit, OKX, Gate.io, KuCoin listing spot simultan TGE. Fokus spot liquidity, price discovery. Hindari perpetual/futures day-1 yang bisa meningkatkan volatilitas dan sell pressure early.
Evidence: Phase 3 EV-013 Binance listing TGE day【Phase 3 — EV-013】; Phase 7 Exchange Ecosystem 5 CEX listed spot, 0 perpetual【Phase 7 — Exchange Ecosystem】; Phase 8 Trading Markets same data【Phase 8 — Trading Markets】; Phase 9 Ecosystem Decision Pattern 4 "CEX Listing Strategy"【Phase 9 — Ecosystem Decision Pattern 4】.
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Playbook 7: Season-based token distribution sebagai governance bootstrap
Explanation: Distribusi berbasis aktivitas (restaking, operating, contributing) via Season 1 (5% TGE unlock), Season 2 (10% cliff 6 bln), Future Community (30% long-term). Mengikat komunitas ke protokol sebelum full governance live. Bukan airdrop acak.
Evidence: Phase 6 Distribution Community 45% = Season 1 5% + Season 2 10% + Future 30%【Phase 6 — Distribution】; Phase 6 Vesting Schedule Season 1 cliff 0, Season 2 cliff 6 bulan【Phase 6 — Vesting Schedule】; Phase 9 Governance Decision Pattern 5 "Season-Based Token Distribution sebagai Governance Bootstrap"【Phase 9 — Governance Decision Pattern 5】.
Supporting Dataset: Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Playbook 8: Developer ecosystem via SDK/CLI/Grants/Hackathons — bottom-up building
Explanation: Sediakan EigenLayer SDK (TS), EigenDA SDK (Go/TS), CLI (Go), Subgraph, Foundry templates. Grant program via Foundation. Hackathon tracks di ETHGlobal. Jangan bangun "AVS template" cookie-cutter — biarkan custom build per AVS needs.
Evidence: Phase 7 Developer Ecosystem 2 SDKs, 1 CLI, 1 Subgraph, Foundry, Grant programs, Hackathons【Phase 7 — Developer Ecosystem】; Phase 4 Development Framework Foundry, Solmate, OpenZeppelin【Phase 4 — Development Framework】; Phase 9 Ecosystem Decision Pattern 5 "Developer Ecosystem via SDK/CLI/Grants"【Phase 9 — Ecosystem Decision Pattern 5】.
Supporting Dataset: Phase 7 Ecosystem, Phase 4 Technology, Phase 9 Behavioral
Confidence: MEDIUM

Anti-patterns

Anti-pattern 1: Over-centralization di fase awal tanpa timeline konkret ke desentralisasi
Explanation: EigenDA operator permissioned, Foundation multisig upgrade control, AVS onboarding butuh governance approval. Semua diberi label "progressive decentralization" tapi tidak ada concrete milestone, KPI, atau tanggal target. Menciptakan kepercayaan community yang rapuh.
Evidence: Phase 4 Known Limitations "Operator Permissioning Centralization"【Phase 4 — Known Limitations】; Phase 8 Ecosystem Risks "EigenDA Operator Permissioning Centralization - High severity"【Phase 8 — Ecosystem Risks】; Phase 9 Recurring Behavioral Pattern 6 "Phased Decentralization — Permissioned Dulu, Permissionless Kemudian (Janji)"【Phase 9 — Recurring Behavioral Pattern 6】; Phase 7 Governance Ecosystem "AVS Onboarding Committee planned" (belum formed)【Phase 7 — Governance Ecosystem】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral, Phase 7 Ecosystem
Confidence: HIGH

Anti-pattern 2: Premature scaling tanpa infrastructure readiness — AVS framework complex, no cookie-cutter
Explanation: Mendorong AVS launch (4 live) tapi setiap AVS harus custom build off-chain + on-chain. Tidak ada template/framework yang memudahkan. Barrier to entry tinggi memperlambat ekosistem expansion. Operator infra best practices tapi tidak di-enforce on-chain.
Evidence: Phase 4 Known Limitations "AVS Development Complexity: high barrier to entry"【Phase 4 — Known Limitations】; Phase 8 Ecosystem Risks "AVS Development Complexity"【Phase 8 — Ecosystem Risks】; Phase 9 Ecosystem Decision Pattern 5 "Tidak ada 'AVS template' cookie-cutter"【Phase 9 — Ecosystem Decision Pattern 5】; Phase 9 Ecosystem Decision Pattern 6 "Cloud-Agnostic Operator Infrastructure — Best Practices Bukan Enforcement"【Phase 9 — Ecosystem Decision Pattern 6】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: MEDIUM

Anti-pattern 3: Poor treasury management transparency — Foundation treasury komposisi, address, spending tidak transparan
Explanation: Eigen Foundation mengelola 10.5% supply + ecosystem fund. Tidak ada dashboard treasury publik, tidak ada transparency report berkala, multisig address tidak disclosed. Community tidak bisa verify pengeluaran.
Evidence: Phase 5 Treasury "Current Treasury Size: tidak diungkap, Composition: tidak diungkap"【Phase 5 — Treasury】; Phase 7 Governance Ecosystem "Foundation multisig transitional control"【Phase 7 — Governance Ecosystem】; Phase 9 Financial Decision Pattern 2 "Treasury Terpusat di Foundation, Komposisi Tidak Transparan"【Phase 9 — Financial Decision Pattern 2】; Phase 6 Open Threads "Foundation treasury on-chain address, composition, spending history — tidak transparan"【Phase 6 — Open Threads】.
Supporting Dataset: Phase 5 Financial, Phase 7 Ecosystem, Phase 9 Behavioral, Phase 6 Token
Confidence: HIGH

Anti-pattern 4: Single chain dependency tanpa multi-chain hedge
Explanation: 100% Ethereum L1. Gas spikes, congestion, validator queue langsung impact semua operasi. EigenDA throughput limited by L1 gas. Tidak ada concrete cross-chain roadmap meski whitepaper mention future expansion.
Evidence: Phase 4 Known Limitations "Single Settlement Chain: Currently only Ethereum mainnet"【Phase 4 — Known Limitations】; Phase 8 Market Position "Primary Chain: Ethereum"【Phase 8 — Market Position】; Phase 9 Strategic Trade-offs 6 "Single Chain Focus vs Multi-Chain Expansion"【Phase 9 — Strategic Trade-offs 6】; Phase 9 Open Threads "Cross-chain restaking concrete roadmap — whitepaper mention future expansion tapi no testnet, no timeline"【Phase 9 — Open Threads】.
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Anti-pattern 5: No protocol revenue model hingga product mature — burn rate fully VC-funded
Explanation: Core protocol no fees. EigenDA revenue baru Apr 2024, jumlah tidak diungkap. AVS fees tidak ke core. Operasional tim 50-100+ orang dibiayai $150M VC funding. Revenue uncertainty tinggi.
Evidence: Phase 5 Revenue Model "Protocol Fees: Planned/Not Live"【Phase 5 — Revenue Model】; Phase 5 Financial Risk "Funding Dependency: belum ada revenue protokol yang signifikan"【Phase 5 — Financial Risk】; Phase 9 Financial Decision Pattern 3 "Revenue Hanya dari EigenDA Service Fees"【Phase 9 — Financial Decision Pattern 3】; Phase 9 Financial Decision Pattern 6 "Eigen Labs Burn Rate Ditanggung VC Funding"【Phase 9 — Financial Decision Pattern 6】.
Supporting Dataset: Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Anti-pattern 6: Token concentration ke investor/team tanpa mekanisasi anti-capture governance
Explanation: 55% supply (Investors 29.5% + Team 15% + Foundation 10.5%) locked tapi terkonsentrasi. Vesting cliff 12 bulan (Oct 2025) = overhang besar. Community 45% tapi hanya 5% unlocked TGE. Governance token-weighted → capture risk oleh large holders. Operator delegation voting power alignment tapi concentration risk.
Evidence: Phase 6 Distribution 55% vs 45%【Phase 6 — Distribution】; Phase 6 Vesting Schedule Team/Investor cliff 12 bulan【Phase 6 — Vesting Schedule】; Phase 8 Ecosystem Risks "VC Token Concentration - Medium severity", "Governance Risk"【Phase 8 — Ecosystem Risks】; Phase 9 Financial Decision Pattern 4 "Token Allocation Berbobot ke Investor & Team"【Phase 9 — Financial Decision Pattern 4】; Phase 9 Governance Decision Pattern 3 "Token-Weighted Voting dengan Delegation ke Operator"【Phase 9 — Governance Decision Pattern 3】.
Supporting Dataset: Phase 6 Token, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Lessons Learned

1. Security-first phased rollout dengan audit berulang membangun trust dan memungkinkan TVL growth masif tanpa exploit. Pattern ini replikabel untuk protokol high-value novel mechanics.
2. Platform strategy (build rails, enable builders) menciptakan flywheel yang lebih kuat dibanding build user-facing products sendiri. LRT & AVS sebagai growth engine.
3. Dual-entity structure (Labs + Foundation) memberikan legal clarity dan credible neutrality path, tapi memerlukan transparansi treasury dan governance transition timeline yang jelas.
4. Token launch setelah PMF & live revenue dengan utility real (bukan governance only) menciptakan tokenomics yang sustainable dan menghindari "token for token's sake".
5. Season-based community distribution berbasis aktivitas (bukan airdrop) mengalign incentives dan bootstrap governance participation sebelum full on-chain governance live.
6. Permissioned operator set di fase awal acceptable untuk security, TAPI harus ada concrete decentralization milestones dengan timeline/KPI — tidak hanya "progressive decentralization" jako janji kosong.
7. Single chain focus (Ethereum) memberikan alignment dan composability tapi menciptakan systemic risk. Multi-chain roadmap harus concrete dari awal.
8. Core protocol fee switch harus dirancang sejak awal — menunggu "nanti" menciptakan revenue uncertainty dan VC dependency yang berkelanjutan.
9. Intersubjective work token innovation membuka design space baru tapi memperkenalkan governance dependency dan legal complexity yang signifikan — butuh legal opinion早早.
10. AVS framework perlu cookie-cutter template/SDK yang lebih mature untuk mempercepat ecosystem expansion — custom build per AVS terlalu lambat.

Knowledge Summary

Strategic Principles
- Security First: Phased rollout, extensive audits, withdrawal delays, permissioned operators, objective slashing dulu
- Ethereum Alignment: Tidak bangun chain/consensus sendiri; leverage Ethereum security, validator set, finality
- Ecosystem Enablement: Build platform untuk LRT & AVS builders, bukan kompetisi dengan mereka
- Long-term Credible Neutrality: Dual entity, progressive decentralization roadmap, community token allocation, on-chain governance transition
- Modular Architecture: Protokol menyediakan rails (staking, delegation, slashing, registry), AVS bangun off-chain + service manager sendiri
- Phased Rollout dengan Scope Minimal per Fase: Setiap mainnet launch membatasi fungsi, audit ulang per fase

Success Factors
- First-mover advantage dalam restaking category dengan 16+ bulan mainnet track record
- Deep technical moat — novel architecture (EigenPod, slashing framework, EigenDA erasure coding, intersubjective work)
- Strong ecosystem flywheel — LRT protocols bring capital → operators secure AVS → AVS generate yield → attract more capital
- World-class team & backing — Sreeram (academic), Robert (CTO ex-AWS/ConsenSys), a16z/Blockchain Capital backing, top-tier auditors
- Token utility beyond governance — Intersubjective work staking, slashing collateral, AVS security token
- Phased decentralization strategy yang kredibel — permissioned awal, roadmap ke permissionless, community distribution 45%

Failure Factors
- Centralization risks — Permissioned operators, Foundation multisig upgrade control, VC/team token concentration 55%, LRT protocol concentration
- Liquidity/UX friction — 7-day withdrawal delay + EigenPod exit queue = compound illiquidity 7-30+ hari
- Single chain dependency — 100% Ethereum L1, gas spikes & congestion impact semua operasi
- Revenue uncertainty — Core protocol no fees, EigenDA revenue baru unproven, burn rate VC-funded
- Intersubjective slashing unproven — Social consensus mechanism complex, governance-dependent, legal/regulatory risk
- AVS development barrier tinggi — Custom off-chain + on-chain per AVS, no cookie-cutter framework

Decision Framework
1. Observe: Identifikasi peluang teknis/ekonomis di lapisan settlement Ethereum
2. Evaluate: Technical feasibility audit, economic modeling, legal structure design
3. Fund: Venture funding bertahap dengan token allocation untuk investor
4. Develop: Phased development dengan audit per komponen
5. Launch: Phased mainnet launch dengan scope minimal, lalu ekspansi ekosistem
6. Govern: Transitional multisig → on-chain token-weighted governance via EIGEN staking

Reusable Playbook
1. Membangun kategori baru via phased rollout dengan audit berulang — "Security First" sebagai moat
2. Platform strategy — Build rails, enable ecosystem builders (LRT, AVS) sebagai growth engine
3. Dual-entity structure untuk credible neutrality — Labs (dev) + Foundation (gov/token/treasury)
4. Token launch setelah product-market fit & live revenue — bukan pre-product
5. Coordinated multi-partner launch untuk momentum ekosistem
6. CEX listing strategy — Major exchanges day-1 spot, no derivatives at launch
7. Season-based token distribution sebagai governance bootstrap
8. Developer ecosystem via SDK/CLI/Grants/Hackathons — bottom-up building

Anti-patterns
1. Over-centralization di fase awal tanpa timeline konkret ke desentralisasi
2. Premature scaling tanpa infrastructure readiness — AVS framework complex, no cookie-cutter
3. Poor treasury management transparency — Foundation treasury komposisi, address, spending tidak transparan
4. Single chain dependency tanpa multi-chain hedge
5. No protocol revenue model hingga product mature — burn rate fully VC-funded
6. Token concentration ke investor/team tanpa mekanisme anti-capture governance

## Open Questions
- [foundation] Distribusi token EIGEN — persentase untuk komunitas/ekosistem, investor, dan tim tidak dicantumkan lengkap di sini karena di luar cakupan fase ini; perlu diverifikasi dari dokumen resmi Eigen Foundation (https://github.com/eigenfoundation) untuk kepastian angka.
- [foundation] Jumlah total AVS aktif dan status kematangan teknisnya (termasuk berapa yang sudah "mainnet-ready" vs "in-development") tidak dihitung di sini — perlu penelusuran lanjutan dari blog resmi EigenLayer.
- [foundation] Apakah Telegram resmi EigenLayer benar-benar tidak ada atau tersembunyi — verifikasi lebih lanjut diperlukan dari situs resmi atau pengumuman komunitas.
- [foundation] Tanggal pasti testnet "Mango" (hari-bulan) tidak ditemukan di sumber primer; hanya kuartal yang bisa dipastikan.
- [foundation] Beberapa sumber menyebut "EigenLayer Foundation" (entitas terpisah di Kepulauan Cayman) sebagai penerbit token EIGEN — status badan hukum dan yurisdiksi pastinya belum diverifikasi dari dokumen resmi; hanya disebut sebagai "Eigen Foundation" di repo GitHub resmi.
- [entity] Investor entities (VC, strategic investors) tidak tercakup di Phase 01 — perlu penelusuran ronde pembiayaan Eigen Labs (Series A, B, dll) dari sumber seperti Crunchbase, PitchBook, atau pengumuman resmi.
- [entity] Auditor kontrak pintar (security firms) tidak disebut di Phase 01 — perlu identifikasi audit trail dari repositori GitHub atau laporan audit resmi (misal: Spearbit, Trail of Bits, Sigma Prime, dll).
- [entity] DAO atau mekanisme governance on-chain (jika ada) tidak teridentifikasi — Eigen Foundation mengelola token EIGEN tapi struktur DAO/komunitas governance butuh verifikasi dari forum governance atau snapshot.
- [entity] Entitas regulator/legal (SEC, CFTC, yurisdiksi Cayman) tidak dianalisis — relevan untuk klasifikasi token EIGEN dan struktur yayasan.
- [entity] Media/Research Lab tambahan (Bankless, Delphi Digital, Electric Capital, dll) yang sering melipus EigenLayer tidak terdaftar — perlu kurasi apakah termasuk entity "terlibat" atau hanya observer.
- [entity] Operator/validator set EigenLayer (entity yang menjalankan node AVS) tidak teridentifikasi — mungkin beratusan, perlu kriteria apakah dicatat per entity atau sebagai kategori.
- [entity] LRT protocol tambahan selain 5 yang disebut (EtherFi, Renzo, Kelp, Puffer, Swell) — ekosistem LRT berkembang cepat, perlu daftar lengkap dari dashboard EigenLayer resmi.
- [history] Tanggal pasti testnet "Mango" (hari-bulan) — hanya diketahui kuartal Q2 2023 dari sumber primer; perlu verifikasi dari blog resmi EigenLayer atau announcement Discord.
- [history] Detail ronde pendanaan tambahan (seed round, strategic round) sebelum Series A — tidak tercakup di sumber yang diverifikasi.
- [history] Tanggal pasti pembentukan Eigen Foundation (hari-bulan) — hanya diketahui "2024" dari repo GitHub; perlu cek dokumen pendirian Cayman atau announcement resmi.
- [history] Persentase alokasi token EIGEN (komunitas, investor, tim, foundation) — tidak diverifikasi di sini; perlu cross-check dengan dokumen tokenomics resmi Eigen Foundation.
- [history] Daftar lengkap auditor kontrak pintar EigenLayer (Spearbit, Trail of Bits, Sigma Prime, dll) dan tanggal laporan audit — tidak diidentifikasi di Phase 1-2; perlu penelusuran repo GitHub atau halaman keamanan resmi.
- [history] Status AVS tambahan selain AltLayer, Dymension, Lagrange — ekosistem AVS berkembang cepat; perlu daftar lengkap dari dashboard EigenLayer resmi.
- [history] Apakah ada Telegram resmi EigenLayer — Phase 1 mencatat "tidak diketahui"; perlu verifikasi final dari situs resmi atau pengumuman komunitas.
- [history] Detail mekanisme slashing yang pernah tertrigger (jika ada) pada AVS produksi — tidak ditemukan insiden keamanan publik di Phase 1-2; perlu monitoring on-chain dan blog post-mortem resmi.
- [technology] Exact erasure coding parameters (k, n) for EigenDA current mainnet configuration — documentation references configurable values but current production parameters not explicitly published in docs
- [technology] Permissionless operator registration timeline for EigenDA — roadmap mentions "progressive decentralization" but no concrete date or criteria published
- [technology] Intersubjective slashing implementation details for EIGEN token — whitepaper describes concept but on-chain contracts for intersubjective work verification not fully documented in public SDK
- [technology] Cross-AVS slashing correlation — whether slashing in one AVS affects stake allocated to other AVS (isolation vs. shared stake model) — docs imply isolation via AllocationManager but not explicitly confirmed
- [technology] EigenDA horizontal scaling roadmap — current committee-based design has throughput ceiling; DAS (Data Availability Sampling) or sharding plans mentioned in research but not in official roadmap
- [technology] Gas optimization efforts for core contracts — no public EIP-4844 (blob) integration plan for EigenLayer contracts despite EigenDA using blobs
- [technology] Formal verification status of core contracts — audits completed but no public formal verification (e.g., Certora, K-framework) reports found
- [technology] AVS template/framework maturity — "AVS SDK" referenced but no official cookie-cutter framework released; each AVS builds custom off-chain stack
- [technology] Operator hardware requirements specification — docs give guidelines but no official minimum spec enforcement or benchmarking standards
- [technology] Slashing veto period governance — who controls veto period duration per AVS; current default 7 days but parameter change process not fully documented
- [financial] Seed round / pre-seed funding details: amount, investors, valuation — tidak ada sumber terverifikasi
- [financial] Private sale token allocation: harga, jumlah token, vesting schedule untuk investor Series A/B — tidak dipublikasikan resmi
- [financial] Eigen Foundation treasury size dan komposisi on-chain — tidak ada dashboard atau laporan transparansi
- [financial] EigenDA actual revenue numbers (bulanan/tahunan) — tidak dipublikasikan
- [financial] Eigen Labs burn rate dan runway — tidak diungkap
- [financial] Tokenomics detail: persentase alokasi token (komunitas, investor, tim, foundation, ekosistem) — hanya disebut "Season 1 & 2" tanpa breakdown persentase resmi
- [financial] Apakah ada fee switch untuk EigenLayer core protocol (non-EigenDA) — docs tidak jelas, perlu klarifikasi dari tim
- [financial] Financial audit / financial statements Eigen Labs Inc — tidak publik (private company)
- [financial] Eigen Foundation legal structure financial implications (Cayman foundation vs Delaware corp) — perlu analisis legal terpisah
- [financial] Operator revenue data (agg) dari AVS — tidak teragregasi oleh protokol core
- [token] Kurva emisi (emission schedule) yang pasti untuk intersubjective work rewards — blog menyebut "programmatic emissions controlled by governance" tapi tidak mempublikasikan formula/k curve; perlu dokumen teknis terpisah atau proposal governance.
- [token] Persentase alokasi "Advisors" — tidak terpisah di blog resmi; apakah termasuk dalam Team (15%) atau Investors (29.5%)? Perlu klarifikasi dari Eigen Foundation.
- [token] Detail vesting per investor (Series A vs Series B vs Seed) — blog hanya menyebut "Investors 29.5% cliff 12 bulan vesting 24-36 bulan" tanpa breakdown per ronde; perlu cek vesting contracts on-chain atau legal docs.
- [token] Foundation treasury management — 10.5% allocation dikelola Eigen Foundation; tidak ada dashboard transparansi on-chain untuk tracking pengeluaran; perlu verifikasi multisig address dan spending history.
- [token] Apakah ada "fee switch" untuk EigenLayer core protocol yang mengarahkan fee ke EIGEN staker — blog tidak menyebut; EigenDA fees dibayar dalam ETH/ERC20 ke operator; perlu klarifikasi dari tim.
- [token] Mekanisme slashing intersubjective work yang pasti — whitepaper deskripsikan konsep tapi implementasi on-chain (bukti sosial, juri, appeal process) tidak sepenuhnya terdokumentasikan di SDK publik.
- [token] Cross-AVS slashing isolation — apakah EIGEN yang di-stake untuk AVS A terisolir dari slashing di AVS B? AllocationManager mengelola alokasi per AVS tapi EIGEN staking pool bersifat universal; perlu konfirmasi teknis.
- [token] Season 2 claim criteria detail — blog menyebut "based on activity" tapi tidak rinci; perlu cek merkle root / claim contract untuk kriteria pasti.
- [token] Tokenomics legal opinion / regulatory classification — tidak dipublikasikan; struktur Cayman Foundation + Delaware Corp + token utility kompleks memerlukan analisis legal terpisah.
- [token] Actual circulating supply real-time — Etherscan menunjukkan total supply 1.67B tapi circulating supply tergantung vesting contract unlock; tidak ada API resmi untuk circulating supply terverifikasi (CoinGecko/CoinMarketCap estimasi).
- [ecosystem] Complete list of all AVS currently live or in testnet on EigenLayer — official dashboard shows more than 3 (AltLayer, Dymension, Lagrange); need full registry from AVSRegistry contract or EigenLayer website AVS page
- [ecosystem] Exact operator set for EigenDA mainnet — permissioned list not publicly disclosed in full; need operator addresses and entity mapping
- [ecosystem] LRT protocol TVL breakdown by protocol (EtherFi, Renzo, Kelp, Puffer, Swell, others) — DeFiLlama has aggregate but per-protocol restaking TVL on EigenLayer needs verification
- [ecosystem] Upcoming AVS integrations announced but not yet live (e.g., witness chain, omnichain protocols, oracle AVS) — tracked via EigenLayer blog and AVSRegistry
- [ecosystem] EigenLayer governance delegate list and voting power distribution — on-chain Governor contract has delegates but no public dashboard
- [ecosystem] Eigen Foundation multisig address and transaction history — not publicly disclosed; need on-chain analysis of proxy admin and treasury movements
- [ecosystem] Cross-chain restaking plans (EigenLayer on other L1s/L2s) — whitepaper mentions future expansion but no concrete roadmap or testnet
- [ecosystem] Permissionless operator registration timeline for EigenDA — "progressive decentralization" mentioned but no criteria or date published
- [ecosystem] AVS slashing isolation mechanics — whether stake allocated to AVS A is protected from slashing in AVS B (AllocationManager suggests isolation but not explicitly confirmed in docs)
- [ecosystem] Official EigenLayer bug bounty / immunefi program details — not found in docs; need verification if active
- [ecosystem] EigenDA disperser throughput limits and scaling roadmap (DAS, sharding) — research paper mentions but not in official roadmap
- [ecosystem] Tokenomics legal opinion / regulatory classification for EIGEN (security vs utility) — not published; Foundation Cayman structure vs Labs Delaware creates complexity
- [ecosystem] Actual circulating supply methodology for EIGEN (vesting contract unlocks vs claimed) — CoinGecko/CMC estimates differ; no official API
- [ecosystem] Operator hardware requirements enforcement — docs give guidelines but no on-chain enforcement or slashing for hardware specs
- [ecosystem] Community grant application process and awarded grants list — Foundation grants repo exists but no public dashboard of recipients/amounts
- [market] Exact EigenDA rollup integration count and names (which rollups are live on EigenDA vs testnet) — not publicly enumerated in official docs
- [market] Symbiotic and Karak TVL comparison at same date — DefiLlama category page shows aggregate but per-protocol historical TVL needs verification
- [market] EIGEN token perpetual/futures listing status on major derivatives exchanges (Bybit, Binance Futures, OKX Futures) — not confirmed as of 2024-10
- [market] Official EigenLayer revenue numbers (EigenDA fees, protocol fees) — not published in transparency report
- [market] Eigen Foundation treasury on-chain address and composition — not publicly disclosed
- [market] Circulating supply methodology discrepancy between CoinGecko, CoinMarketCap, and on-chain vesting contract unlocks
- [market] AVS pipeline: number of AVS in testnet vs mainnet — official dashboard shows more than 4 but not all named
- [market] Operator revenue data aggregated across AVS — not published by protocol
- [market] Slashing events history (if any) on mainnet AVS — no public incidents reported but not confirmed zero
- [market] EigenLayer bug bounty program details (Immunefi or similar) — not found in official docs
- [market] Cross-chain restaking roadmap timeline — whitepaper mentions but no concrete dates
- [market] Permissionless operator registration criteria and timeline for EigenDA — "progressive decentralization" mentioned without specifics
- [market] Regulatory classification of EIGEN token (security vs utility) in major jurisdictions — no legal opinion published
- [market] Actual daily active users (unique addresses transacting) vs staker count — Dune dashboards vary in methodology
- [market] LRT protocol TVL breakdown on EigenLayer specifically (vs total LRT TVL including non-restaked) — DefiLlama shows aggregate
- [behavioral] Exact EigenDA erasure coding parameters (k, n) di mainnet production — tidak dipublikasikan di docs; perlu verifikasi dari kode disperser/retriever atau operator config
- [behavioral] Permissionless operator registration criteria & timeline untuk EigenDA — "progressive decentralization" disebut berulang tapi tidak ada concrete milestone, KPI, atau tanggal target
- [behavioral] Cross-AVS slashing isolation mechanics — apakah stake allocated ke AVS A terisolir dari slashing di AVS B? AllocationManager suggest isolation tapi tidak eksplisit dikonfirmasi di docs
- [behavioral] EigenDA horizontal scaling roadmap (DAS, sharding) — research paper mention tapi tidak di official roadmap; throughput ceiling committee-based
- [behavioral] Eigen Foundation treasury on-chain address, composition, spending history — tidak transparan; multisig address tidak disclosed; no dashboard
- [behavioral] Actual circulating supply methodology untuk EIGEN — CoinGecko/CMC estimates vary; vesting contract unlocks vs claimed tokens; no official API
- [behavioral] AVS pipeline: complete list AVS testnet vs mainnet — dashboard menunjukkan >4 tapi tidak semua named; perlu query AVSRegistry contract langsung
- [behavioral] Slashing events history (if any) pada mainnet AVS — zero reported tapi tidak ada official confirmation "zero slashing incidents"
- [behavioral] EigenLayer bug bounty / Immunefi program details — tidak ditemukan di docs; perlu verifikasi apakah active
- [behavioral] Cross-chain restaking concrete roadmap — whitepaper mention future expansion tapi no testnet, no timeline, no partner announcement
- [behavioral] Regulatory classification legal opinion untuk EIGEN (security vs utility) — tidak dipublikasikan; Cayman Foundation + Delaware Corp + token utility kompleks
- [behavioral] Operator hardware requirements enforcement — docs give guidelines tapi no on-chain enforcement, no slashing untuk hardware spec violation
- [behavioral] Community grant application process & awarded grants list — Foundation grants repo exists tapi no public dashboard recipients/amounts
- [behavioral] EigenDA rollup integration names & status (live vs testnet) — tidak enumerated di official docs; perlu query disperser contracts atau partner announcements
- [behavioral] Symbiotic & Karak TVL comparison at same date untuk market share accuracy — DefiLlama category page aggregate only; per-protocol historical TVL perlu verified
- [behavioral] EIGEN token perpetual/futures listing status pada derivatives exchanges major — tidak confirmed as of 2024-10; perlu monitor Binance Futures, Bybit, OKX
- [behavioral] Formal verification status core contracts — audits completed tapi no public formal verification (Certora, K-framework) reports found
- [knowledge] Exact EigenDA erasure coding parameters (k, n) di mainnet production — tidak dipublikasikan di docs; perlu verifikasi dari kode disperser/retriever atau operator config【Phase 4 — Known Limitations】【Phase 9 — Open Threads】
- [knowledge] Permissionless operator registration criteria & timeline untuk EigenDA — "progressive decentralization" disebut berulang tapi tidak ada concrete milestone, KPI, atau tanggal target【Phase 4 — Known Limitations】【Phase 8 — Ecosystem Risks】【Phase 9 — Open Threads】
- [knowledge] Cross-AVS slashing isolation mechanics — apakah stake allocated ke AVS A terisolir dari slashing di AVS B? AllocationManager suggest isolation tapi tidak eksplisit dikonfirmasi di docs【Phase 4 — Core Components】【Phase 9 — Open Threads】
- [knowledge] EigenDA horizontal scaling roadmap (DAS, sharding) — research paper mention tapi tidak di official roadmap; throughput ceiling committee-based【Phase 4 — Known Limitations】【Phase 9 — Open Threads】
- [knowledge] Eigen Foundation treasury on-chain address, composition, spending history — tidak transparan; multisig address tidak disclosed; no dashboard【Phase 5 — Treasury】【Phase 6 — Open Threads】【Phase 9 — Open Threads】
- [knowledge] Actual circulating supply methodology untuk EIGEN — CoinGecko/CMC estimates vary; vesting contract unlocks vs claimed tokens; no official API【Phase 6 — Open Threads】【Phase 8 — Market】【Phase 9 — Open Threads】
- [knowledge] AVS pipeline: complete list AVS testnet vs mainnet — dashboard menunjukkan >4 tapi tidak semua named; perlu query AVSRegistry contract langsung【Phase 7 — Ecosystem】【Phase 9 — Open Threads】
- [knowledge] Slashing events history (if any) pada mainnet AVS — zero reported tapi tidak ada official confirmation "zero slashing incidents"【Phase 4 — Security Model】【Phase 9 — Open Threads】
- [knowledge] EigenLayer bug bounty / Immunefi program details — tidak ditemukan di docs; perlu verifikasi apakah active【Phase 9 — Open Threads】
- [knowledge] Cross-chain restaking concrete roadmap — whitepaper mention future expansion tapi no testnet, no timeline, no partner announcement【Phase 4 — Official Technical Resources】【Phase 9 — Open Threads】
- [knowledge] Regulatory classification legal opinion untuk EIGEN (security vs utility) — tidak dipublikasikan; Cayman Foundation + Delaware Corp + token utility kompleks【Phase 6 — Open Threads】【Phase 9 — Open Threads】
- [knowledge] Operator hardware requirements enforcement — docs give guidelines tapi no on-chain enforcement, no slashing untuk hardware spec violation【Phase 4 — Known Limitations】【Phase 9 — Open Threads】
- [knowledge] Community grant application process & awarded grants list — Foundation grants repo exists tapi no public dashboard recipients/amounts【Phase 7 — Developer Ecosystem】【Phase 9 — Open Threads】
- [knowledge] EigenDA rollup integration names & status (live vs testnet) — tidak enumerated di official docs; perlu query disperser contracts atau partner announcements【Phase 7 — Ecosystem】【Phase 9 — Open Threads】
- [knowledge] Symbiotic & Karak TVL comparison at same date untuk market share accuracy — DefiLlama category page aggregate only; per-protocol historical TVL perlu verified【Phase 8 — Market Share】【Phase 9 — Open Threads】
- [knowledge] EIGEN token perpetual/futures listing status pada derivatives exchanges major — tidak confirmed as of 2024-10; perlu monitor Binance Futures, Bybit, OKX【Phase 8 — Trading Markets】【Phase 9 — Open Threads】
- [knowledge] Formal verification status core contracts — audits completed tapi no public formal verification (Certora, K-framework) reports found【Phase 4 — Audit History】【Phase 9 — Open Threads】
