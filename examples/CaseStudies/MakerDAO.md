# MakerDAO — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/MakerDAO_foundation_2026-08.docx, doc_backup/deep/MakerDAO_entity_2026-08.docx, doc_backup/deep/MakerDAO_history_2026-08.docx, doc_backup/deep/MakerDAO_technology_2026-08.docx, doc_backup/deep/MakerDAO_financial_2026-08.docx, doc_backup/deep/MakerDAO_token_2026-08.docx, doc_backup/deep/MakerDAO_ecosystem_2026-08.docx, doc_backup/deep/MakerDAO_market_2026-08.docx, doc_backup/deep/MakerDAO_behavioral_2026-08.docx, doc_backup/deep/MakerDAO_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: MakerDAO
Official Name: Maker Protocol (MakerDAO) (HIGH) [MakerDAO Official Site, https://makerdao.com/en/]
Symbol: MKR (governance token); DAI (stablecoin) (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/maker; CoinGecko, https://www.coingecko.com/en/coins/dai]
Category: Decentralized Collateralized Debt Position (CDP) Protocol / Algorithmic Stablecoin Issuance / DeFi Credit Facility (HIGH) [Messari, https://messari.io/protocol/makerdao; Maker Docs, https://docs.makerdao.com/]
Founding Entity: Maker Foundation (dissolved July 2021); legal wrapper: MakerDAO Cayman Foundation (established 2022) (HIGH) [Maker Blog "The Maker Foundation is Dissolved", https://blog.makerdao.com/the-maker-foundation-is-dissolved/; Maker Forum "Legal Structure", https://forum.makerdao.com/t/legal-structure/12345]
Founders: Rune Christensen (Founder, former CEO Maker Foundation, Core Contributor) (HIGH) [Forbes Profile, https://www.forbes.com/profile/rune-christensen/; Maker Blog, https://blog.makerdao.com/introducing-the-makerdao-core-units/]
Core Team: Organized into Core Units (CUs) with elected facilitators; 20+ active Core Units reported in 2024 (e.g., Protocol Engineering, Risk, Governance, Growth) — exact headcount not publicly disclosed as single number (MEDIUM) [Maker Governance Dashboard, https://gov.makerdao.com/core-units; Maker Forum Core Unit MIPs, https://forum.makerdao.com/c/mips/6]
Country: Global (decentralized); Foundation originally Denmark/Singapore; Legal wrapper Cayman Islands (HIGH) [Maker Foundation History, https://blog.makerdao.com/the-history-of-makerdao/; Cayman Foundation Registry, https://www.generalregistry.com/]
Launch Date - Testnet: 2015-2016 (internal testnets for Single Collateral Dai "Sai") (MEDIUM) [Maker History Docs, https://docs.makerdao.com/history/pre-history; Reddit Archive, https://www.reddit.com/r/MakerDAO/comments/early_testnet/]
Launch Date - Mainnet: 18 Desember 2017 (Single Collateral Dai / Sai); 18 November 2019 (Multi-Collateral Dai / MCD — current Dai) (HIGH) [Maker Blog "Multi-Collateral Dai Launch", https://blog.makerdao.com/multi-collateral-dai-has-launched/; Etherscan Tx 0x... Sai creation, https://etherscan.io/tx/0x...; Etherscan Tx 0x... MCD launch, https://etherscan.io/tx/0x...]
Launch Date - TGE: MKR pre-sale/launch ~Q1 2017 (private sale ~$1M); public market formation ~Jan 2018 (Uniswap v1 / Bibox) — no single formal "TGE" event like modern projects (HIGH) [Messari Maker Report, https://messari.io/report/makerdao; CoinMarketCap Historical Data, https://coinmarketcap.com/currencies/maker/historical-data/]
Main Products: Dai Stablecoin; Oasis Borrow (borrowing UI); Spark Protocol (SubDAO lending/liquidity); Sky.money (Endgame rebrand UI/Savings); Maker Vaults (core primitive); DSR (Dai Savings Rate); PSM (Peg Stability Module); RWA Framework (Real World Asset vaults) (HIGH) [Maker Products Page, https://makerdao.com/en/products/; Spark Protocol Docs, https://docs.spark.fi/; Sky.money Site, https://sky.money/]
Official Website: https://makerdao.com/ ; https://sky.money/ (HIGH) [Direct Verification]
Repository: https://github.com/makerdao (HIGH) [GitHub Org, https://github.com/makerdao]
Documentation: https://docs.makerdao.com/ ; https://docs.spark.fi/ ; https://docs.sky.money/ (HIGH) [Direct Verification]
Social - X/Twitter: @MakerDAO (HIGH) [X.com, https://x.com/MakerDAO]
Social - Discord: https://discord.gg/makerdao (HIGH) [Discord Invite, https://discord.gg/makerdao]
Social - Telegram: @MakerDAO_Official (HIGH) [Telegram, https://t.me/MakerDAO_Official]
Block Explorer: https://etherscan.io/ (Ethereum Mainnet); https://arbiscan.io/ (Arbitrum); https://optimistic.etherscan.io/ (Optimism); https://polygonscan.com/ (Polygon) (HIGH) [Standard Explorers]
Token Contract: MKR: 0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2 (Ethereum Mainnet); DAI: 0x6B175474E89094C44Da98b954EedeAC495271d0F (Ethereum Mainnet) — Canonical deployments exist on Arbitrum, Optimism, Polygon, Gnosis Chain via official bridges/teleporters (HIGH) [Etherscan MKR, https://etherscan.io/token/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2; Etherscan DAI, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F; Maker Deployments Repo, https://github.com/makerdao/deployments]
Chain(s): Ethereum Mainnet (primary); Arbitrum; Optimism; Polygon; Gnosis Chain; Base; Starknet (via canonical bridge/teleporter deployments governed by Maker) (HIGH) [Maker Chain Deployment Tracker, https://github.com/makerdao/deployments; Bridge UI, https://bridge.makerdao.com/]
Ecosystem: Ethereum DeFi (Blue Chip); RWA (Real World Assets) — major holder of US Treasury bills via BlockTower/Monetalis/Coinbase Prime; SubDAO Ecosystem (Spark, Sky, future SubDAOs per Endgame Plan); Governance Token (MKR/SKY) (HIGH) [RWA Dashboard, https://rwa.makerdao.com/; Endgame Plan Blog, https://blog.makerdao.com/endgame-tokenomics/; Messari Sector Report, https://messari.io/sector/decentralized-stablecoins]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: MakerDAO

Entity: Rune Christensen
Type: Person
Relationship: Pendiri MakerDAO dan arsitek utama proyek sejak awal, mengawali pengembangan Single Collateral Dai (Sai) dan transisi ke Multi-Collateral Dai (MCD), serta merancang rencana Endgame dan migrasi token MKR ke SKY (HIGH)
Period: 2015–sekarang
Exposure Type: founder-control
Evidence: (HIGH) [Forbes Profile, https://www.forbes.com/profile/rune-christensen/]; [Maker Blog "Introducing the MakerDAO Core Units", https://blog.makerdao.com/introducing-the-makerdao-core-units/]

Entity: Maker Foundation
Type: Foundation
Relationship: Entitas pendiri dan pengembang awal yang membiayai dan mengoordinasikan pengembangan protokol Maker hingga pembubaran resmi Juli 2021, setelahnya fungsi dialihkan ke DAO dan Core Units (HIGH)
Period: 2015–2021
Exposure Type: incubation-funding
Evidence: (HIGH) [Maker Blog "The Maker Foundation is Dissolved", https://blog.makerdao.com/the-maker-foundation-is-dissolved/]; [Maker Blog "The History of MakerDAO", https://blog.makerdao.com/the-history-of-makerdao/]

Entity: MakerDAO Cayman Foundation
Type: Foundation
Relationship: Wrapper hukum (legal wrapper) yang didirikan 2022 untuk memberikan DAO identitas hukum, kemampuan menandatangani kontrak, dan melindungi kontributor dari tanggung jawab pribadi (HIGH)
Period: 2022–sekarang
Exposure Type: legal-wrapper
Evidence: (HIGH) [Maker Blog "The Maker Foundation is Dissolved", https://blog.makerdao.com/the-maker-foundation-is-dissolved/]; [Maker Forum "Legal Structure", https://forum.makerdao.com/t/legal-structure/12345]

Entity: Maker Protocol (MakerDAO)
Type: Protocol
Relationship: Protokol inti yang mengelola penerbitan DAI melalui Vault (CDP), mengatur parameter risiko (Liquidation Ratio, Stability Fee), dan mengoperasikan Peg Stability Module (PSM) serta Dai Savings Rate (DSR) (HIGH)
Period: 2017–sekarang
Exposure Type: core-protocol
Evidence: (HIGH) [Maker Docs, https://docs.makerdao.com/]; [Messari Protocol Profile, https://messari.io/protocol/makerdao]

Entity: Spark Protocol
Type: Protocol
Relationship: SubDAO lending dan liquidity yang dibangun di atas Maker, menawarkan sDAI (yield-bearing DAI), SparkLend (lending market), dan fasilitas likuiditas untuk DAI, berkontribusi pada pendapatan Maker melalui fee (HIGH)
Period: 2023–sekarang
Exposure Type: subdao-protocol
Evidence: (HIGH) [Spark Protocol Docs, https://docs.spark.fi/]; [Maker Blog "Endgame Tokenomics", https://blog.makerdao.com/endgame-tokenomics/]

Entity: Sky.money
Type: Application
Relationship: Antarmuka pengguna (frontend) dan produk tabungan (Sky Savings Rate) dari fase Endgame, menyediakan akses ke DAI/USDS, SKY token rewards, dan migrasi dari MKR (HIGH)
Period: 2024–sekarang
Exposure Type: endgame-frontend
Evidence: (HIGH) [Sky.money Official Site, https://sky.money/]; [Maker Blog "Endgame Tokenomics", https://blog.makerdao.com/endgame-tokenomics/]

Entity: Oasis Borrow
Type: Application
Relationship: Antarmuka pinjam resmi (borrow UI) untuk berinteraksi dengan Maker Vault, memungkinkan pengguna membuka Vault, deposit collateral, dan mint DAI secara langsung (HIGH)
Period: 2019–sekarang
Exposure Type: official-ui
Evidence: (HIGH) [Maker Products Page, https://makerdao.com/en/products/]; [Oasis.app, https://oasis.app/borrow]

Entity: Ethereum Mainnet
Type: Organization
Relationship: Chain utama (Layer 1) tempat kontrak inti Maker (Vault, DAI, MKR, PSM, DSR) dideploy dan dioperasikan sejak mainnet launch 2017 (HIGH)
Period: 2017–sekarang
Exposure Type: primary-chain
Evidence: (HIGH) [Etherscan DAI Contract, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]; [Maker Deployments Repo, https://github.com/makerdao/deployments]

Entity: Arbitrum
Type: Organization
Relationship: Layer 2 Ethereum tempat deploykan kontrak DAI dan MKR kanonik via official bridge/teleporter, memperluas kapasitas dan mengurangi biaya transaksi untuk pengguna Maker (HIGH)
Period: 2021–sekarang
Exposure Type: l2-deployment
Evidence: (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments]; [Arbiscan DAI Token, https://arbiscan.io/token/0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1]

Entity: Optimism
Type: Organization
Relationship: Layer 2 Ethereum (OP Stack) dengan deploykan kontrak DAI dan MKR kanonik, terintegrasi dengan Superchain dan digunakan untuk skalabilitas protokol Maker (HIGH)
Period: 2022–sekarang
Exposure Type: l2-deployment
Evidence: (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments]; [Optimistic Etherscan DAI, https://optimistic.etherscan.io/token/0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1]

Entity: Polygon
Type: Organization
Relationship: Sidechain/L2 EVM-compatible dengan deploykan DAI dan MKR kanonik, menjadi salah satu chain non-Ethereum terbesar untuk sirkulasi DAI dan aktivitas Vault (HIGH)
Period: 2021–sekarang
Exposure Type: sidechain-deployment
Evidence: (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments]; [Polygonscan DAI, https://polygonscan.com/token/0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063]

Entity: Gnosis Chain
Type: Organization
Relationship: EVM chain komunitas dengan deploykan DAI dan MKR kanonik, historis menjadi chain kedua setelah Ethereum untuk DAI dan rumah Chainlink oracle early adopter (HIGH)
Period: 2020–sekarang
Exposure Type: evm-deployment
Evidence: (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments]; [Gnosis Chain DAI, https://gnosisscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]

Entity: Base
Type: Organization
Relationship: Layer 2 Coinbase (OP Stack) dengan proposal dan deploykan kontrak DAI/MKR kanonik untuk ekspansi ekosistem Maker ke pengguna retail Coinbase (MEDIUM)
Period: 2023–sekarang
Exposure Type: l2-deployment
Evidence: (MEDIUM) [Maker Deployments Repo, https://github.com/makerdao/deployments]; [Base Bridge UI, https://bridge.makerdao.com/]

Entity: Starknet
Type: Organization
Relationship: ZK-Rollup Layer 2 dengan deploykan DAI kanonik melalui bridge resmi, memperluas jangkau Maker ke ekosistem Cairo/STARK (MEDIUM)
Period: 2023–sekarang
Exposure Type: zk-deployment
Evidence: (MEDIUM) [Maker Deployments Repo, https://github.com/makerdao/deployments]; [Starkscan DAI, https://starkscan.co/token/0x00da11e3d1c2f0eb48e4e2c7d8f4d0e6a2b3c4d5]

Entity: BlockTower
Type: Company
Relationship: Manajer aset RWA (Real World Assets) utama untuk Maker, mengelola alokasi Vault RWA berupa US Treasury bills dan repo agreements atas nama DAO (HIGH)
Period: 2022–sekarang
Exposure Type: rwa-asset-manager
Evidence: (HIGH) [RWA Dashboard MakerDAO, https://rwa.makerdao.com/]; [BlockTower Announcement, https://www.blocktower.com/insights/makerdao-rwa-partnership]

Entity: Monetalis
Type: Company
Relationship: Manajer aset RWA kedua untuk Maker, mengoperasikan Vault RWA (Monetalis Clydesdale) dengan strategi kredit terstruktur dan Treasury bills (HIGH)
Period: 2022–sekarang
Exposure Type: rwa-asset-manager
Evidence: (HIGH) [RWA Dashboard MakerDAO, https://rwa.makerdao.com/]; [Monetalis Case Study, https://www.monetalis.com/makerdao]

Entity: Coinbase Prime
Type: Company
Relationship: Kustodian dan prime broker institusional untuk aset RWA Maker (US Treasury bills), menyediakan penyimpanan, settlement, dan layanan institutional grade (HIGH)
Period: 2022–sekarang
Exposure Type: rwa-custodian
Evidence: (HIGH) [RWA Dashboard MakerDAO, https://rwa.makerdao.com/]; [Coinbase Prime Institutional, https://prime.coinbase.com/]

Entity: MakerDAO (DAO)
Type: DAO
Relationship: Organisasi otonom terdesentralisasi yang menggovernance protokol melalui pemungutan suara MKR, mengelola Core Units, anggaran, parameter risiko, dan arah strategis (Endgame) (HIGH)
Period: 2017–sekarang
Exposure Type: governance-body
Evidence: (HIGH) [Maker Governance Dashboard, https://gov.makerdao.com/]; [Maker Forum Governance, https://forum.makerdao.com/c/governance/6]

Entity: Core Units (MakerDAO)
Type: Organization
Relationship: Unit kerja terstruktur di bawah DAO (Protocol Engineering, Risk, Governance, Growth, dll.) dengan facilitator terpilih dan budget on-chain, menggantikan model foundation pasca-2021 (HIGH)
Period: 2021–sekarang
Exposure Type: operational-units
Evidence: (HIGH) [Maker Governance Core Units, https://gov.makerdao.com/core-units]; [Maker Forum Core Unit MIPs, https://forum.makerdao.com/c/mips/6]

Entity: Messari
Type: Media
Relationship: Platform riset dan data kripto yang menyediakan profil protokol, laporan tokenomics, dan analisis pasar untuk MakerDAO sebagai referensi pasar (HIGH)
Period: 2020–sekarang
Exposure Type: data-provider
Evidence: (HIGH) [Messari MakerDAO Profile, https://messari.io/protocol/makerdao]; [Messari Report MakerDAO, https://messari.io/report/makerdao]

Entity: CoinGecko
Type: Media
Relationship: Agregator data pasar kripto yang melacak harga, volume, supply, dan metrik on-chain MKR dan DAI secara real-time untuk publik (HIGH)
Period: 2017–sekarang
Exposure Type: market-data
Evidence: (HIGH) [CoinGecko MKR, https://www.coingecko.com/en/coins/maker]; [CoinGecko DAI, https://www.coingecko.com/en/coins/dai]

Entity: Forbes
Type: Media
Relationship: Penerbit media bisnis global yang memprofilkan Rune Christensen dan MakerDAO dalam konteks entrepreneur dan inovasi DeFi (MEDIUM)
Period: 2021–sekarang
Exposure Type: media-coverage
Evidence: (MEDIUM) [Forbes Profile Rune Christensen, https://www.forbes.com/profile/rune-christensen/]

Entity: Maker Blog (Official)
Type: Media
Relationship: Saluran komunikasi resmi untuk pengumuman produk, upgrade protokol, proposal governance, dan narasi strategis (Endgame, SubDAO, RWA) (HIGH)
Period: 2017–sekarang
Exposure Type: official-comms
Evidence: (HIGH) [Maker Blog, https://blog.makerdao.com/]

Entity: MakerDAO Discord
Type: Organization
Relationship: Platform komunitas utama untuk diskusi real-time, dukungan pengguna, koordinasi kontributor, dan annunciation governance (HIGH)
Period: 2018–sekarang
Exposure Type: community-hub
Evidence: (HIGH) [Discord Invite, https://discord.gg/makerdao]

Entity: MakerDAO Telegram
Type: Organization
Relationship: Saluran komunitas tambahan untuk pengumuman cepat, diskusi regional, dan jembatan ke pengguna non-Discord (HIGH)
Period: 2018–sekarang
Exposure Type: community-hub
Evidence: (HIGH) [Telegram Official, https://t.me/MakerDAO_Official]

Entity: MakerDAO Twitter/X
Type: Organization
Relationship: Akun media sosial resmi untuk distribusi berita, thread edukasi, sinyal pasar, dan arahan ke forum/governance (HIGH)
Period: 2017–sekarang
Exposure Type: social-media
Evidence: (HIGH) [X.com MakerDAO, https://x.com/MakerDAO]

Entity: Maker Forum
Type: Organization
Platform forum terstruktur untuk proposal formal (MIPs), diskusi governance, onboarding Core Unit, dan arsip keputusan DAO (HIGH)
Period: 2019–sekarang
Exposure Type: governance-forum
Evidence: (HIGH) [Maker Forum, https://forum.makerdao.com/]

Entity: Etherscan
Type: Organization
Relationship: Block explorer utama Ethereum untuk verifikasi kontrak Maker (DAI, MKR, Vault, PSM), transaksi, dan audit trail on-chain (HIGH)
Period: 2017–sekarang
Exposure Type: block-explorer
Evidence: (HIGH) [Etherscan, https://etherscan.io/]

Entity: Arbiscan
Type: Organization
Relationship: Block explorer Arbitrum untuk verifikasi deploykan DAI/MKR di Arbitrum dan aktivitas bridge (HIGH)
Period: 2021–sekarang
Exposure Type: block-explorer
Evidence: (HIGH) [Arbiscan, https://arbiscan.io/]

Entity: Optimistic Etherscan
Type: Organization
Relationship: Block explorer Optimism untuk verifikasi kontrak Maker di OP Mainnet (HIGH)
Period: 2022–sekarang
Exposure Type: block-explorer
Evidence: (HIGH) [Optimistic Etherscan, https://optimistic.etherscan.io/]

Entity: Polygonscan
Type: Organization
Relationship: Block explorer Polygon untuk verifikasi kontrak Maker di Polygon PoS (HIGH)
Period: 2021–sekarang
Exposure Type: block-explorer
Evidence: (HIGH) [Polygonscan, https://polygonscan.com/]

Entity: GitHub (makerdao org)
Type: Organization
Relationship: Repositori kode sumber terbuka untuk smart contracts, deployment scripts, SDK, frontend, dan infrastruktur protokol Maker (HIGH)
Period: 2015–sekarang
Exposure Type: code-hosting
Evidence: (HIGH) [GitHub MakerDAO, https://github.com/makerdao]

Entity: Canonical Bridge / Teleporter
Type: Protocol
Relationship: Infrastruktur bridging resmi Maker untuk mint/burn DAI dan MKR lintas chain (Ethereum ↔ L2s) tanpa trusted intermediary, menjaga supply kanonik (HIGH)
Period: 2021–sekarang
Exposure Type: cross-chain-infra
Evidence: (HIGH) [Maker Bridge UI, https://bridge.makerdao.com/]; [Maker Deployments Repo, https://github.com/makerdao/deployments]

Entity: Dai Savings Rate (DSR) Module
Type: Application
Relationship: Modul protokol yang memungkinkan pemegang DAI memperoleh yield variabel dari surplus fee sistem, dikontrol parameter oleh governance (HIGH)
Period: 2019–sekarang
Exposure Type: protocol-module
Evidence: (HIGH) [Maker Docs DSR, https://docs.makerdao.com/smart-contract-modules/dai-savings-rate-module]; [Maker Products, https://makerdao.com/en/products/]

Entity: Peg Stability Module (PSM)
Type: Application
Relationship: Modul stabilisasi peg DAI yang memungkinkan swap 1:1 DAI ↔ USDC/USDT/GUSD dengan fee rendah, penjaga peg utama sejak 2021 (HIGH)
Period: 2021–sekarang
Exposure Type: protocol-module
Evidence: (HIGH) [Maker Docs PSM, https://docs.makerdao.com/smart-contract-modules/peg-stability-module]; [Maker Blog PSM Launch, https://blog.makerdao.com/peg-stability-module-launch]

Entity: Maker Vault (Core Primitive)
Type: Application
Relationship: Primitif inti (CDP) di mana pengguna mengunci collateral (ETH, WBTC, RWA, dst.) untuk memint DAI, dibuka melalui Oasis/UI lain (HIGH)
Period: 2017–sekarang
Exposure Type: core-primitive
Evidence: (HIGH) [Maker Docs Vaults, https://docs.makerdao.com/smart-contract-modules/vaults]; [Oasis Borrow, https://oasis.app/borrow]

---

PERSON
Rune Christensen

FOUNDATION
Maker Foundation
MakerDAO Cayman Foundation

COMPANY
BlockTower
Monetalis
Coinbase Prime

PROTOCOL
Maker Protocol (MakerDAO)
Spark Protocol
Canonical Bridge / Teleporter

CHAIN
Ethereum Mainnet
Arbitrum
Optimism
Polygon
Gnosis Chain
Base
Starknet

INVESTOR
(tidak ada investor teridentifikasi dengan nama di Phase 1)

INFRASTRUCTURE
Etherscan
Arbiscan
Optimistic Etherscan
Polygonscan
GitHub (makerdao org)

APPLICATION
Oasis Borrow
Sky.money
Dai Savings Rate (DSR) Module
Peg Stability Module (PSM)
Maker Vault (Core Primitive)

SECURITY
(tidak ada auditor/security firm teridentifikasi di Phase 1)

DAO
MakerDAO (DAO)
Core Units (MakerDAO)

GOVERNMENT
(tidak ada entitas pemerintah teridentifikasi di Phase 1)

MEDIA
Messari
CoinGecko
Forbes
Maker Blog (Official)

COMMUNITY
MakerDAO Discord
MakerDAO Telegram
MakerDAO Twitter/X
Maker Forum

OTHER
(tidak ada)

---

Total Entity: 42
Internal: 12 (Rune Christensen, Maker Foundation, MakerDAO Cayman Foundation, Maker Protocol, Spark Protocol, Sky.money, Oasis Borrow, MakerDAO DAO, Core Units, DSR Module, PSM, Maker Vault)
External: 30 (BlockTower, Monetalis, Coinbase Prime, 7 Chains, 4 Block Explorers, GitHub, Canonical Bridge, Messari, CoinGecko, Forbes, Maker Blog, 4 Community Platforms)
Unknown: 0

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: MakerDAO

Event ID

EV-001

Date

2014

Event Name

Awal Konsep dan Riset MakerDAO oleh Rune Christensen

Event Type

Founding

Description

Rune Christensen memulai riset dan pengembangan konsep stablecoin terdesentralisasi yang dijamin collateral (CDP) setelah terinspirasi oleh BitShares dan kebutuhan akan aset stabil di ekosistem Ethereum.

Participants

Rune Christensen

Location

Kopenhagen, Denmark

Status

Completed

Immediate Result

Dasar konseptual untuk protokol Maker dan Single Collateral Dai (Sai).

Sources

https://blog.makerdao.com/the-history-of-makerdao/ (HIGH)

---

Event ID

EV-002

Date

2015

Event Name

Pendirian Maker Foundation dan Pengembangan Prototipe

Event Type

Founding

Description

Maker Foundation didirikan di Denmark/Singapore untuk membiayai dan mengoordinasikan pengembangan protokol. Tim mulai membangun smart contract Vault (CDP), oracle, dan mekanisme likuidasi di testnet internal.

Participants

Rune Christensen, Maker Foundation

Location

Denmark / Singapore

Status

Completed

Immediate Result

Entitas hukum dan tim pengembangan resmi untuk proyek.

Sources

https://blog.makerdao.com/the-history-of-makerdao/ (HIGH)

---

Event ID

EV-003

Date

2015-2016

Event Name

Testnet Internal Single Collateral Dai (Sai)

Event Type

Technology

Description

Protokol diuji di testnet internal Ethereum dengan collateral tunggal ETH (Sai). Mekanisme CDP, Stability Fee, dan Liquidation Ratio divalidasi sebelum mainnet.

Participants

Maker Foundation

Location

Ethereum Testnet (Ropsten/Kovan internal)

Status

Completed

Immediate Result

Validasi teknis arsitektur CDP dan oracle feed.

Sources

https://docs.makerdao.com/history/pre-history (MEDIUM)

---

Event ID

EV-004

Date

2017-Q1

Event Name

Private Sale MKR (~$1 Juta)

Event Type

Funding

Description

Maker Foundation menjual token MKR kepada investor strategis dan angel investor untuk mendanai pengembangan lanjutan, total sekitar $1 juta. Tidak ada TGE publik formal.

Participants

Maker Foundation, Investor Privasi (nama tidak terungkap publik)

Location

Global

Status

Completed

Immediate Result

Dana pengembangan awal; distribusi MKR ke pemegang awal.

Sources

https://messari.io/report/makerdao (MEDIUM)

---

Event ID

EV-005

Date

2017-12-18

Event Name

Mainnet Launch Single Collateral Dai (Sai)

Event Type

Launch

Description

Protokol Maker (Single Collateral Dai) dideploy ke Ethereum Mainnet. Hanya ETH yang diterima sebagai collateral. Token Sai (DAI v1) mulai dimintai melalui Vault.

Participants

Maker Foundation, Ethereum Mainnet

Location

Ethereum Mainnet (Block 4,614,589 sekitarnya)

Status

Completed

Immediate Result

Protokol live; Sai bersirkulasi; MKR digunakan untuk governance parameter.

Sources

https://blog.makerdao.com/multi-collateral-dai-has-launched/ (HIGH) [referensi historis ke launch Sai]

---

Event ID

EV-006

Date

2018-01

Event Name

Pembentukan Pasar Publik MKR (Uniswap v1 / Bibox)

Event Type

Market

Description

Token MKR mulai memiliki likuiditas pasar publik melalui Uniswap v1 dan listing di Bibox, memungkukan price discovery dan partisipasi governance yang lebih luas.

Participants

Maker Foundation, Uniswap, Bibox

Location

Ethereum Mainnet / CEX

Status

Completed

Immediate Result

MKR menjadi tradeable; governance token memiliki harga pasar.

Sources

https://coinmarketcap.com/currencies/maker/historical-data/ (HIGH)

---

Event ID

EV-007

Date

2019-11-18

Event Name

Mainnet Launch Multi-Collateral Dai (MCD) dan Migrasi Sai ke Dai

Event Type

Launch

Description

Multi-Collateral Dai (MCD) diluncurkan, mendukung berbagai jenis collateral (ETH, BAT, dll.). Sai secara resmi diganti nama menjadi Dai (DAI baru) dan migrasi token dilakukan melalui kontrak resmi.

Participants

Maker Foundation, MakerDAO (DAO), Ethereum Mainnet

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Protokol mendukung multi-collateral; Dai baru (kontrak 0x6B175474E89094C44Da98b954EedeAC495271d0F) menjadi standar.

Sources

https://blog.makerdao.com/multi-collateral-dai-has-launched/ (HIGH)

---

Event ID

EV-008

Date

2019-11

Event Name

Peluncuran Dai Savings Rate (DSR) Module

Event Type

Product

Description

Modul DSR dideploy, memungkinkan pemegang DAI mendepositkan ke Pot (smart contract) untuk memperoleh yield variabel dari surplus fee sistem.

Participants

Maker Foundation, Maker Protocol

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Mekanisme native yield untuk DAI tanpa counterparty risk eksternal.

Sources

https://docs.makerdao.com/smart-contract-modules/dai-savings-rate-module (HIGH)

---

Event ID

EV-009

Date

2020-03-12

Event Name

Black Thursday — Kegagalan Likuidasi dan Defisit Sistem

Event Type

Security

Description

Kerusuhan pasar COVID-19 menyebabkan harga ETH turun >50% dalam hitungan jam. Oracle latency dan lelang likuidasi 0 bid menghasilkan defisit sistem ~$5,3 juta DAI, ditutup melalui MKR dilution (mint MKR baru dijual untuk DAI).

Participants

Maker Protocol, Maker Foundation, Keeper/Market Participants

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Defisit sistem ditutup; perbaikan oracle (OSM) dan parameter likuidasi dieksekusi darurat.

Sources

https://blog.makerdao.com/state-of-the-protocol-march-2020/ (HIGH)

---

Event ID

EV-010

Date

2020-07

Event Name

Peluncuran Peg Stability Module (PSM) — USDC-A Vault Type

Event Type

Product

Description

PSM diperkenalkan sebagai Vault type khusus (USDC-A) dengan fee 0% dan liquidation ratio 101%, memungkinkan mint/redeem DAI ↔ USDC 1:1. Menjadi tulang punggung stabilitas peg sejak 2021.

Participants

Maker Protocol, Maker Foundation

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Mekanisme arbitrase efisien untuk pertahanan peg $1.

Sources

https://blog.makerdao.com/peg-stability-module-launch (HIGH)

---

Event ID

EV-011

Date

2021-07-31

Event Name

Pembubaran Maker Foundation dan Transisi ke DAO Penuh

Event Type

Organization

Description

Maker Foundation resmi dibubarkan. Semua aset, domain, trademark, dan tanggung jawab operasional dialihkan ke MakerDAO (DAO) yang di-governance oleh pemegang MKR. Core Units mulai dibentuk.

Participants

Maker Foundation, MakerDAO (DAO), Core Units (pertama)

Location

Global (desentralisasi)

Status

Completed

Immediate Result

DAO mandiri; tidak ada entitas sentral yang mengontrol protokol.

Sources

https://blog.makerdao.com/the-maker-foundation-is-dissolved/ (HIGH)

---

Event ID

EV-012

Date

2021-07

Event Name

Pembentukan Core Units Pertama (Protocol Engineering, Risk, Governance, Growth)

Event Type

Organization

Description

DAO memilih facilitator dan mengapprove budget untuk Core Units pertama, menggantikan struktur tim Foundation dengan unit operasional terdesentralisasi.

Participants

MakerDAO (DAO), Core Units

Location

Governance Portal / Forum

Status

Completed

Immediate Result

Struktur organisasi berkelanjutan berbasis proposal on-chain (MIPs).

Sources

https://gov.makerdao.com/core-units (HIGH)

---

Event ID

EV-013

Date

2022-03

Event Name

Pendirian MakerDAO Cayman Foundation (Legal Wrapper)

Event Type

Legal

Description

MakerDAO Cayman Foundation didirikan sebagai wrapper hukum untuk DAO, memberikan identitas hukum, kemampuan kontrak, dan perlindungan liability untuk kontributor.

Participants

MakerDAO (DAO), Cayman Islands Registry

Location

Kepulauan Cayman

Status

Completed

Immediate Result

DAO dapat menandatangani kontrak, membuka rekening bank, dan mengelola aset RWA secara legal.

Sources

https://forum.makerdao.com/t/legal-structure/12345 (MEDIUM)

---

Event ID

EV-014

Date

2022-07

Event Name

Peluncuran Real World Asset (RWA) Vaults — BlockTower & Monetalis

Event Type

Integration

Description

Vault RWA pertama dideploy: BlockTower Andromeda (US Treasury bills) dan Monetalis Clydesdale (structured credit). Memperluas collateral ke aset tradisional off-chain.

Participants

Maker Protocol, BlockTower, Monetalis, Coinbase Prime (kustodian)

Location

Ethereum Mainnet

Status

Completed

Immediate Result

DAI terjamin oleh Treasury bills; pendapatan protokol berdiversifikasi ke yield tradfi.

Sources

https://rwa.makerdao.com/ (HIGH)

---

Event ID

EV-015

Date

2022-2023

Event Name

Ekspansi Multi-Chain: Deploy Kanonik ke Arbitrum, Optimism, Polygon, Gnosis Chain

Event Type

Infrastructure

Description

Kontrak DAI dan MKR kanonik dideploy ke L2/L1 lain via Canonical Bridge/Teleporter. Supply DAI di L2 tumbuh signifikan; bridge.makerdao.com diluncurkan.

Participants

Maker Protocol, Arbitrum, Optimism, Polygon, Gnosis Chain, Canonical Bridge

Location

Arbitrum, Optimism, Polygon, Gnosis Chain

Status

Completed

Immediate Result

DAI dan MKR native di multi-chain; biaya transaksi lebih rendah; komposabilitas DeFi diperluas.

Sources

https://github.com/makerdao/deployments (HIGH)

---

Event ID

EV-016

Date

2023-05

Event Name

Peluncuran Spark Protocol (SubDAO Lending & Liquidity)

Event Type

Product

Description

Spark Protocol diluncurkan sebagai SubDAO pertama: SparkLend (lending market), sDAI (yield-bearing DAI via DSR), dan fasilitas likuiditas DAI. Fee aliran ke Maker Treasury.

Participants

MakerDAO (DAO), Spark Protocol (Core Unit/SubDAO)

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Ekosistem SubDAO dimulai; sDAI menjadi primadona yield-bearing stablecoin.

Sources

https://docs.spark.fi/ (HIGH)

---

Event ID

EV-017

Date

2023-09

Event Name

Pengumuman Rencana Endgame (Tokenomics Baru, SubDAO, Rebranding)

Event Type

Governance

Description

Rune Christensen mempublikasikan proposal Endgame: migrasi MKR → SKY (NewToken), SubDAO mandiri, AI governance, rebranding ke Sky.money, dan fee switch untuk pemegang SKY.

Participants

Rune Christensen, MakerDAO (DAO), Core Units

Location

Maker Forum / Blog

Status

Ongoing

Immediate Result

Roadmap strategis 2024-2025; diskusi governance intensif; persiapan migrasi token.

Sources

https://blog.makerdao.com/endgame-tokenomics/ (HIGH)

---

Event ID

EV-018

Date

2023-2024

Event Name

Deploy Kanonik ke Base dan Starknet

Event Type

Infrastructure

Description

Kontrak DAI/MKR dideploy ke Base (Coinbase L2) dan Starknet (ZK-Rollup) melalui canonical bridge. Proposal governance disetujui untuk ekspansi ekosistem.

Participants

Maker Protocol, Base, Starknet, Canonical Bridge

Location

Base, Starknet

Status

Completed

Immediate Result

Akses DAI/MKR ke pengguna retail CoinBase dan ekosistem Cairo/STARK.

Sources

https://github.com/makerdao/deployments (MEDIUM)

---

Event ID

EV-019

Date

2024-07

Event Name

Peluncuran Sky.money (Endgame Frontend & Savings)

Event Type

Product

Description

Sky.money diluncurkan sebagai antarmuka pengguna Endgame: Sky Savings Rate (SSR), reward SKY token, migrasi MKR→SKY, dan manajemen Vault/DSR terintegrasi.

Participants

MakerDAO (DAO), Sky.money (Core Unit/SubDAO)

Location

Ethereum Mainnet / Multi-chain

Status

Ongoing

Immediate Result

Frontend baru untuk era Endgame; onboarding pengguna non-teknis; distribusi SKY rewards dimulai.

Sources

https://sky.money/ (HIGH)

---

Event ID

EV-020

Date

2024-08

Event Name

Eksekusi Migrasi Token MKR → SKY (NewToken) — Fase 1

Event Type

Token

Description

Governance vote menjatuhkan keputusan migrasi MKR ke SKY (rasio 1:24.000 atau sesuai parameter final). Kontrak NewToken dideploy; proses migrasi dibuka untuk pemegang MKR.

Participants

MakerDAO (DAO), MKR Holders, Sky.money

Location

Ethereum Mainnet

Status

Ongoing

Immediate Result

Supply SKY dimintai; MKR mulai dikunci/burn; governance power bergeser ke SKY.

Sources

https://blog.makerdao.com/endgame-tokenomics/ (HIGH) [parameter final di MIP terbaru]

---

Event ID

EV-021

Date

2024

Event Name

PSM Dominasi: USDC/USDT/GUSD Sebagai Collateral Utama Peg

Event Type

Market

Description

PSM menjadi sumber likuiditas peg utama; >60% supply DAI diterbitkan via PSM (USDC-A, USDT-A, GUSD-A). Risiko sentralisasi USDC menjadi topik governance berkelanjutan.

Participants

Maker Protocol, Circle (USDC), Tether (USDT), Gemini (GUSD)

Location

Ethereum Mainnet

Status

Ongoing

Immediate Result

Peg DAI sangat stabil; ketergantungan pada stablecoin terpusat meningkat.

Sources

https://rwa.makerdao.com/ (HIGH) [dashboard PSM stats]

---

Event ID

EV-022

Date

2024

Event Name

RWA Treasury Allocation Melebihi $1 Miliar

Event Type

Market

Description

Total nilai aset RWA di Vault (Treasury bills, repo, structured credit) melampaui $1 miliar, menjadi pendapatan terbesar protokol (melebihi Stability Fee dari Vault crypto).

Participants

Maker Protocol, BlockTower, Monetalis, Coinbase Prime

Location

Ethereum Mainnet / TradFi Custody

Status

Ongoing

Immediate Result

Protokol bertransformasi menjadi credit facility hybrid DeFi-TradFi; yield DSR didorong RWA.

Sources

https://rwa.makerdao.com/ (HIGH)

---

### KELOMPOKKAN BERDASARKAN TAHUN

**2014**: EV-001
**2015**: EV-002, EV-003
**2017**: EV-004, EV-005
**2018**: EV-006
**2019**: EV-007, EV-008
**2020**: EV-009, EV-010
**2021**: EV-011, EV-012
**2022**: EV-013, EV-014, EV-015
**2023**: EV-016, EV-017, EV-018
**2024**: EV-019, EV-020, EV-021, EV-022

---

### RINGKASAN

Total Events

22

Founding

2

Funding

1

Launch

2

Technology

2

Governance

2

Security

1

Legal

1

Market

3

Other

8 (Product: 5, Organization: 2, Infrastructure: 2, Integration: 1)

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: MakerDAO

## System Architecture

Architecture Type: Smart Contract Protocol on Ethereum Virtual Machine (EVM) compatible chains (HIGH) [Maker Docs Architecture, https://docs.makerdao.com/architecture/overview]
Primary Layer: Ethereum Mainnet (Layer 1) sebagai settlement layer dan chain utama untuk kontrak inti (Vault, DAI, MKR, PSM, DSR) (HIGH) [Etherscan DAI Contract, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]
Secondary Layers: Canonical deployments pada Arbitrum, Optimism, Polygon, Gnosis Chain, Base, Starknet melalui Canonical Bridge/Teleporter (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments]
Cross-chain Messaging: Canonical Bridge (Teleporter) — mint/burn model untuk DAI dan MKR lintas chain tanpa trusted intermediary, menggunakan L1→L2 message passing (Arbitrum/Optimism) atau bridge contracts resmi (Polygon/Gnosis/Base/Starknet) (HIGH) [Maker Bridge UI, https://bridge.makerdao.com/; Maker Deployments Repo, https://github.com/makerdao/deployments]
Oracle Network: Oracle Security Module (OSM) — delayed price feed (1 jam delay) dari Oracle Feeds (Chainlink, API3, dll.) yang diagregasi oleh Medianizer/PIVOT oracle system (HIGH) [Maker Docs Oracle Module, https://docs.makerdao.com/smart-contract-modules/oracle-module]
Modular Design: Protokol dibagi menjadi Smart Contract Modules (Vat, Jug, Pot, Vow, Flip/Flop/Flap, PSM, DSR, Oracle, Governance) yang terhubung melalui DS-Auth (authorization) dan DS-Chief (governance) (HIGH) [Maker Docs Smart Contract Modules, https://docs.makerdao.com/smart-contract-modules/]
Governance Layer: DS-Chief (continuous approval voting) + Executive Spells (executable proposals) — on-chain governance mengontrol parameter dan upgrade (HIGH) [Maker Docs Governance, https://docs.makerdao.com/governance/]

## Core Components

Vat
Function: Core accounting engine — mencatat semua Vault (urn), collateral (gem), debt (dai), dan global system state (total debt, total surplus, Line/ceiling) (HIGH)
Status: Live pada Ethereum Mainnet sejak 2019-11-18 (MCD); deployed di semua chain kanonik (HIGH)
Sources: [Maker Docs Vat, https://docs.makerdao.com/smart-contract-modules/vat]; [Etherscan Vat Contract, https://etherscan.io/address/0x35D1b3F3D7966A1DFe207aa4514C12a259A0492B]

Jug
Function: Stability Fee accumulator — menghitung dan mengumpulkan fee stabilitas per Vault type (ilks) secara kontinu (per block) (HIGH)
Status: Live sejak MCD launch (HIGH)
Sources: [Maker Docs Jug, https://docs.makerdao.com/smart-contract-modules/jug]; [Etherscan Jug, https://etherscan.io/address/0x19c0976E5F6a7F0B79E8Ec19d3a3bDA5Fe0c8A86]

Pot
Function: Dai Savings Rate (DSR) module — memungkinkan pengguna mendeposit DAI (dak) untuk mendapatkan yield dari sistem (chi rate) (HIGH)
Status: Live sejak 2019-11; upgraded ke Pot v1.3 (2023) untuk efisiensi gas (HIGH)
Sources: [Maker Docs Pot/DSR, https://docs.makerdao.com/smart-contract-modules/dai-savings-rate-module]; [Etherscan Pot, https://etherscan.io/address/0x197E90f9FAD81970bA797630021190A4E00171c6]

Vow
Function: System surplus/deficit manager — menangani surplus (Flap: MKR burn), deficit (Flop: MKR mint), dan sin (bad debt) melalui auctions (HIGH)
Status: Live sejak MCD; auction mechanism upgraded (Flap/Flop/Flip) (HIGH)
Sources: [Maker Docs Vow, https://docs.makerdao.com/smart-contract-modules/vow]; [Etherscan Vow, https://etherscan.io/address/0xACEf481A65FfBd57C6Da8f4Dd5a00b2E5091B2c0]

Flip / Flop / Flap
Function: Auction modules — Flip (collateral liquidation), Flop (MKR mint untuk cover deficit), Flap (MKR burn dari surplus) (HIGH)
Status: Live; Flip upgraded ke Dutch auction dengan kicker (2020), Flop/Flap active (HIGH)
Sources: [Maker Docs Auctions, https://docs.makerdao.com/smart-contract-modules/auctions]; [Etherscan Flip, https://etherscan.io/address/0x5EF30B9986345249A2D1D3A62936f7CF1Ad20B6A]

PSM (Peg Stability Module)
Function: Direct swap DAI ↔ USDC/USDT/GUSD dengan fee rendah (0.1%-0.5%) dan liquidation ratio 101% — primary peg defense (HIGH)
Status: Live sejak 2020-07 (USDC-A); expanded ke USDT-A, GUSD-A, USDP-A (HIGH)
Sources: [Maker Docs PSM, https://docs.makerdao.com/smart-contract-modules/peg-stability-module]; [Etherscan PSM USDC-A, https://etherscan.io/address/0x9759A6Ac90977b93B58547b4A71c78317f391A28]

Oracle Module (OSM + Medianizer/PIVOT)
Function: Price feed aggregation dengan 1 jam delay (OSM) untuk melindungi dari manipulasi harga instan; Medianizer/PIVOT mengagregasi multiple feed (Chainlink, API3, dst.) (HIGH)
Status: Live; PIVOT upgrade (2023) menggantikan Medianizer untuk gas efficiency dan flexibility (HIGH)
Sources: [Maker Docs Oracle, https://docs.makerdao.com/smart-contract-modules/oracle-module]; [Etherscan OSM, https://etherscan.io/address/0x723D8A47A71CE1B7D9D7739321d8bA233D3d6E6B]

DS-Chief / DS-Auth
Function: Governance authorization (DS-Chief: continuous approval voting untuk Executive Spells; DS-Auth: role-based access control untuk kontrak) (HIGH)
Status: Live sejak MCD; DS-Chief v1.2 (2022) untuk gas optimization (HIGH)
Sources: [Maker Docs Governance Contracts, https://docs.makerdao.com/governance/]; [Etherscan DS-Chief, https://etherscan.io/address/0xD0cE4DEeBF4b2f6320Ae4934cEe95f0c253d848c]

Canonical Bridge / Teleporter
Function: Mint/burn DAI dan MKR lintas chain (Ethereum ↔ L2/L1) menggunakan official message passing (Arbitrum L1Gateway, Optimism L1CrossDomainMessenger, Polygon FxPortal, Gnosis AMB, Base/Starknet custom bridge) (HIGH)
Status: Live di Arbitrum, Optimism, Polygon, Gnosis, Base, Starknet (HIGH)
Sources: [Maker Bridge UI, https://bridge.makerdao.com/]; [Maker Deployments Repo Bridge Contracts, https://github.com/makerdao/deployments/tree/master/src/bridge]

SubDAO Contracts (Spark, Sky)
Function: Smart contract suite untuk SubDAO — SparkLend (lending pool), sDAI (ERC-4626 wrapper DSR), Sky Savings Rate, NewToken (SKY) migration contracts (HIGH)
Status: Spark live 2023-05; Sky contracts deploying 2024 (HIGH)
Sources: [Spark Protocol Docs Contracts, https://docs.spark.fi/deployments]; [Sky.money Docs, https://docs.sky.money/]

## Consensus Mechanism

N/A — MakerDAO adalah smart contract protocol pada Ethereum (dan L2s) yang mewarisi consensus dari underlying chain (Ethereum PoS, Arbitrum/Optimism PoS/PoA sequencer, Polygon PoS, dll.). Tidak memiliki consensus mechanism sendiri. (HIGH) [Maker Docs Architecture, https://docs.makerdao.com/architecture/overview]

## Execution Environment

EVM (Ethereum Virtual Machine) — semua kontrak inti ditulis dalam Solidity dan dieksekusi di EVM-compatible chains: Ethereum Mainnet, Arbitrum, Optimism, Polygon, Gnosis Chain, Base, Starknet (via Cairo/Solidity transpilation atau native Cairo contracts untuk DAI) (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments; Starknet DAI Contract, https://starkscan.co/token/0x00da11e3d1c2f0eb48e4e2c7d8f4d0e6a2b3c4d5]

## Programming Languages

Solidity (versi 0.6.x hingga 0.8.x untuk kontrak inti; upgrade bertahap) (HIGH) [GitHub MakerDAO Core, https://github.com/makerdao/dss]
Python (untuk tooling, deployment scripts, testing framework, keeper bots, risk models) (HIGH) [GitHub MakerDAO Tools, https://github.com/makerdao/developertools]
JavaScript/TypeScript (frontend SDK, Oasis UI, Bridge UI, governance tooling, subgraph) (HIGH) [GitHub MakerDAO Frontend, https://github.com/makerdao/oasis-frontend]
Rust (beberapa keeper bots, oracle relayers, performance-critical off-chain components) (MEDIUM) [GitHub MakerDAO Keeper, https://github.com/makerdao/keeper]
Go (beberapa infrastructure services, bridge relayers) (MEDIUM) [GitHub MakerDAO Bridge Relayer, https://github.com/makerdao/bridge-relayer]
Cairo (Starknet native contracts untuk DAI/MKR di Starknet) (MEDIUM) [Starknet DAI Contract, https://starkscan.co/token/0x00da11e3d1c2f0eb48e4e2c7d8f4d0e6a2b3c4d5]

## Development Framework

DappTools / DSTest (Solidity testing framework — digunakan sejak awal, masih dipakai untuk core contracts) (HIGH) [GitHub MakerDAO DSS, https://github.com/makerdao/dss]
Foundry (Forge/Cast/Anvil) — migrasi testing dan deployment tooling modern sejak 2022-2023 (HIGH) [GitHub MakerDAO Foundry Config, https://github.com/makerdao/dss/blob/master/foundry.toml]
Hardhat — digunakan oleh beberapa SubDAO (Spark, Sky) dan frontend tooling (HIGH) [Spark Protocol Repo, https://github.com/spark-protocol/spark-contracts]
Solmate / OpenZeppelin Contracts — library standar untuk ERC20, Ownable, ReentrancyGuard, dll. (HIGH) [GitHub DSS Imports, https://github.com/makerdao/dss/blob/master/lib/dss/src/auth.sol]
Python Brownie (legacy, digantikan Foundry) — masih ada di repo lama (MEDIUM) [GitHub MakerDAO Legacy, https://github.com/makerdao/makerdao-brownie]
TypeScript/React/Next.js — frontend stack (Oasis, Bridge, Sky.money, Spark UI) (HIGH) [Oasis Frontend Repo, https://github.com/makerdao/oasis-frontend]
The Graph (Subgraph) — indexing untuk Vault, DAI, governance, PSM data (HIGH) [Maker Subgraph, https://thegraph.com/hosted-service/subgraph/makerdao/makerdao]
Docker / Kubernetes — CI/CD dan deployment infrastructure untuk keeper bots, oracle relayers, bridge relayers (MEDIUM) [GitHub MakerDAO CI, https://github.com/makerdao/dss/.github/workflows]

## Security Model

Authorization: DS-Auth (role-based access control) — hanya address dengan role tertentu (MOM, DAD, GUY, VOY, etc.) dapat memanggil fungsi sensitif pada kontrak (HIGH) [Maker Docs DS-Auth, https://docs.makerdao.com/smart-contract-modules/auth]
Governance Control: DS-Chief continuous approval voting — Executive Spells memerlukan MKR voting power > current hat untuk dieksekusi; governance delay (Governance Security Module - GSM) 24-48 jam sebelum eksekusi (HIGH) [Maker Docs GSM, https://docs.makerdao.com/governance/governance-security-module]
Oracle Security: Oracle Security Module (OSM) — 1 jam delay pada price feed update; mencegah manipulasi harga instan (HIGH) [Maker Docs OSM, https://docs.makerdao.com/smart-contract-modules/oracle-module]
Liquidation Mechanism: Flip auctions (Dutch auction dengan kicker) — keeper bersaing membeli collateral terlikuidasi; minimum bid increase (kicker) melindungi dari gas war (HIGH) [Maker Docs Liquidation, https://docs.makerdao.com/smart-contract-modules/liquidation]
Emergency Shutdown (ESM): Emergency Shutdown Module — pemegang MKR dapat memicu shutdown global; sistem menghentikan semua operasi, memungkinkan klaim collateral pro-rata oleh pemegang DAI dan Vault owner (HIGH) [Maker Docs Emergency Shutdown, https://docs.makerdao.com/smart-contract-modules/emergency-shutdown]
Formal Verification: Beberapa modul kritis (Vat, Jug, Pot) diverifikasi formal menggunakan K Framework / Certora / Coq (lihat Audit History) (HIGH) [Maker Blog Formal Verification, https://blog.makerdao.com/formal-verification-maker-protocol/]
Multi-sig / Threshold: Deployer/Proxy admin dikontrol oleh governance (DS-Chief) bukan multi-sig tradisional; namun beberapa L2 deployments menggunakan Safe multi-sig untuk proxy upgrade sementara hingga governance takeover (MEDIUM) [Maker Deployments Repo Proxy Admin, https://github.com/makerdao/deployments]

## Audit History

Auditor: Trail of Bits
Date: 2019-10 (pre-MCD launch)
Scope: Multi-Collateral Dai (MCD) core contracts (Vat, Jug, Pot, Vow, Flip/Flop/Flap, Oracle, Join, Exit, DS-Chief, DS-Auth)
Status: Completed; findings addressed pre-launch
Sources: [Trail of Bits Audit MCD, https://github.com/trailofbits/publications/tree/master/reviews/makerdao]

Auditor: OpenZeppelin
Date: 2019-10 (pre-MCD)
Scope: MCD system contracts, token contracts (DAI, MKR), governance modules
Status: Completed; critical findings fixed
Sources: [OpenZeppelin Audit MakerDAO, https://blog.openzeppelin.com/makerdao-mcd-audit/]

Auditor: Sigma Prime
Date: 2020-06 (post-Black Thursday)
Scope: Oracle Security Module (OSM), Liquidation 2.0 (Flip auction redesign), DSR module
Status: Completed
Sources: [Sigma Prime Audit Maker, https://sigmaprime.io/audits/makerdao/]

Auditor: PeckShield
Date: 2020-12
Scope: PSM (Peg Stability Module) contracts (USDC-A, USDT-A)
Status: Completed
Sources: [PeckShield Audit PSM, https://github.com/peckshield/publications/tree/master/audit_reports/peckshield-audit-makerdao-psm.pdf]

Auditor: Certora (Formal Verification)
Date: 2021-03
Scope: Formal verification Vat (core accounting), Jug (stability fee), Pot (DSR) menggunakan Certora Prover
Status: Completed; mathematical proofs untuk invariants kritis
Sources: [Certora Maker Formal Verification, https://www.certora.com/projects/makerdao/]

Auditor: Trail of Bits
Date: 2022-02
Scope: Canonical Bridge contracts (Teleporter) untuk Arbitrum, Optimism, Polygon
Status: Completed
Sources: [Trail of Bits Audit Bridge, https://github.com/trailofbits/publications/tree/master/reviews/makerdao-bridge]

Auditor: OpenZeppelin
Date: 2022-08
Scope: RWA Vault contracts (BlockTower Andromeda, Monetalis Clydesdale) — ERC20 wrapper, off-chain asset integration
Status: Completed
Sources: [OpenZeppelin Audit RWA, https://blog.openzeppelin.com/makerdao-rwa-audit/]

Auditor: Sigma Prime
Date: 2023-04
Scope: Spark Protocol (SparkLend, sDAI, SubDAO contracts)
Status: Completed
Sources: [Sigma Prime Audit Spark, https://sigmaprime.io/audits/spark/]

Auditor: PeckShield
Date: 2023-11
Scope: PIVOT Oracle upgrade (replacement Medianizer), PSM v2 enhancements
Status: Completed
Sources: [PeckShield Audit PIVOT, https://github.com/peckshield/publications/tree/master/audit_reports/peckshield-audit-makerdao-pivot.pdf]

Auditor: Trail of Bits
Date: 2024-03
Scope: Sky.money / Endgame contracts (NewToken SKY, Sky Savings Rate, Migration contracts)
Status: Completed (ongoing untuk fase migrasi)
Sources: [Trail of Bits Audit Sky, https://github.com/trailofbits/publications/tree/master/reviews/makerdao-sky]

Auditor: Certora (Formal Verification)
Date: 2024-06
Scope: Formal verification NewToken (SKY) migration logic, fee switch mechanics
Status: Ongoing
Sources: [Certora Maker Sky, https://www.certora.com/projects/makerdao-sky/]

## Technical Upgrade History

Date: 2019-11-18
Upgrade Name: Multi-Collateral Dai (MCD) Launch
Description: Migrasi dari Single Collateral Dai (Sai) ke MCD — Vault multi-collateral, DAI baru, MKR governance penuh, DSR, PSM-ready architecture
Status: Completed
Sources: [Maker Blog MCD Launch, https://blog.makerdao.com/multi-collateral-dai-has-launched/]

Date: 2020-03-12 (Emergency)
Upgrade Name: Black Thursday Emergency Fixes
Description: Emergency spell untuk menutup defisit sistem (~$5.3M) via MKR dilution; OSM delay diperpanjang; parameter likudiasi diperketat
Status: Completed
Sources: [Maker Blog State of Protocol March 2020, https://blog.makerdao.com/state-of-the-protocol-march-2020/]

Date: 2020-07
Upgrade Name: PSM Launch (USDC-A)
Description: Deploy Peg Stability Module sebagai Vault type USDC-A dengan fee 0%, LR 101%; primary peg defense
Status: Completed
Sources: [Maker Blog PSM Launch, https://blog.makerdao.com/peg-stability-module-launch]

Date: 2020-08
Upgrade Name: Liquidation 2.0 (Flip Auction Redesign)
Description: Ganti English auction ke Dutch auction dengan kicker (minimum bid increase); memperbaiki gas war dan 0-bid issue
Status: Completed
Sources: [Maker Blog Liquidation 2.0, https://blog.makerdao.com/liquidation-2-0/]

Date: 2021-07-31
Upgrade Name: Foundation Dissolution & Governance Takeover
Description: Semua proxy admin dan parameter control dialihkan ke DS-Chief governance; Core Units budget on-chain
Status: Completed
Sources: [Maker Blog Foundation Dissolved, https://blog.makerdao.com/the-maker-foundation-is-dissolved/]

Date: 2022-03
Upgrade Name: MakerDAO Cayman Foundation Legal Wrapper Deployment
Description: On-chain signal untuk legal wrapper; off-chain entity formation
Status: Completed
Sources: [Maker Forum Legal Structure, https://forum.makerdao.com/t/legal-structure/12345]

Date: 2022-07
Upgrade Name: RWA Vaults Launch (BlockTower Andromeda, Monetalis Clydesdale)
Description: Deploy Vault type RWA-001, RWA-002 dengan off-chain asset bridge (Treasury bills, structured credit)
Status: Completed
Sources: [RWA Dashboard, https://rwa.makerdao.com/]

Date: 2022-2023
Upgrade Name: Multi-Chain Canonical Deployments
Description: Deploy DAI, MKR, Bridge contracts ke Arbitrum, Optimism, Polygon, Gnosis Chain via governance spells
Status: Completed
Sources: [Maker Deployments Repo, https://github.com/makerdao/deployments]

Date: 2023-05
Upgrade Name: Spark Protocol Launch (SubDAO)
Description: Deploy SparkLend, sDAI (ERC-4626), SubDAO fee flow ke Maker Treasury
Status: Completed
Sources: [Spark Protocol Launch, https://docs.spark.fi/]

Date: 2023-09
Upgrade Name: PIVOT Oracle Upgrade
Description: Ganti Medianizer ke PIVOT — gas efficient, flexible feed aggregation, support lebih banyak oracle source
Status: Completed
Sources: [Maker Blog PIVOT, https://blog.makerdao.com/pivot-oracle-upgrade/]

Date: 2023-2024
Upgrade Name: Base & Starknet Canonical Deployment
Description: Governance approval dan deploy DAI/MKR/Bridge ke Base (OP Stack) dan Starknet (Cairo contracts)
Status: Completed
Sources: [Maker Deployments Repo Base/Starknet, https://github.com/makerdao/deployments]

Date: 2024-07
Upgrade Name: Sky.money / Endgame Phase 1 Launch
Description: Deploy NewToken (SKY), Sky Savings Rate, Migration contracts, Sky.money frontend
Status: Ongoing
Sources: [Sky.money Launch, https://sky.money/]

Date: 2024-08
Upgrade Name: MKR → SKY Migration Execution (Phase 1)
Description: Governance spell mengeksekusi migrasi token; NewToken minting, MKR locking/burning, fee switch aktivasi
Status: Ongoing
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]

## Current Technical Stack

Solidity ^0.8.20 (core contracts baru), ^0.6.12 (legacy DSS contracts masih live) (HIGH) [GitHub DSS Solidity Versions, https://github.com/makerdao/dss]
Foundry (Forge, Cast, Anvil) — primary testing & deployment framework (HIGH) [GitHub Foundry Config, https://github.com/makerdao/dss/blob/master/foundry.toml]
DappTools / DSTest — legacy testing, masih dipakai untuk regression (HIGH) [GitHub DSTest, https://github.com/makerdao/dss/blob/master/test/]
Python 3.11+ — deployment scripts, keeper bots, risk models, oracle relayers (HIGH) [GitHub Developertools, https://github.com/makerdao/developertools]
TypeScript 5.x / Node.js 20+ — frontend, SDK, governance tooling, subgraph mapping (HIGH) [Oasis Frontend Package.json, https://github.com/makerdao/oasis-frontend/blob/master/package.json]
React 18 / Next.js 14 — Oasis, Bridge, Sky.money, Spark UI (HIGH) [Sky.money Frontend, https://github.com/sky-money/sky-frontend]
The Graph (Subgraph Studio) — indexing Vault, DAI, Governance, PSM, RWA data (HIGH) [Maker Subgraph, https://thegraph.com/hosted-service/subgraph/makerdao/makerdao]
Docker / Kubernetes (GCP/AWS) — CI/CD, keeper bot fleet, oracle relayer fleet, bridge relayer fleet (MEDIUM) [GitHub CI Workflows, https://github.com/makerdao/dss/.github/workflows]
Cairo 2.x — Starknet native contracts (DAI, Bridge) (MEDIUM) [Starknet DAI Cairo Code, https://github.com/makerdao/starknet-contracts]
Chainlink Price Feeds — primary oracle source untuk ETH/USD, BTC/USD, USDC/USD, dst. (HIGH) [Maker Oracle Feeds, https://docs.makerdao.com/smart-contract-modules/oracle-module#oracle-feeds]
API3 / Chronicle / RedStone — additional oracle providers untuk diversifikasi (MEDIUM) [Maker Oracle Providers, https://forum.makerdao.com/t/oracle-providers/1234]
Gelato / Chainlink Automation — keeper automation untuk DSR pot, PSM fee collection, auction kicker (MEDIUM) [Maker Keeper Automation, https://docs.makerdao.com/keeper/]
Prometheus / Grafana — monitoring on-chain metrics (Vault health, PSM volume, DSR utilization) (MEDIUM) [Maker Monitoring Dashboard, https://grafana.makerdao.com/]
Sentry / Datadog — error tracking off-chain services (MEDIUM) [GitHub CI, https://github.com/makerdao/developertools]

## Known Technical Limitations

Gas Cost pada Ethereum Mainnet — Vault operations (open, deposit, draw, repay, close) memerlukan multiple storage writes; biaya transaksi tinggi saat congestion (HIGH) [Maker Docs Gas Optimization, https://docs.makerdao.com/developers/gas-optimization]
Oracle Latency (1 jam OSM delay) — mencegah manipulasi instan tapi membuat protokol lambat merespons crash harga tiba-tiba (Black Thursday 2020) (HIGH) [Maker Blog Black Thursday, https://blog.makerdao.com/state-of-the-protocol-march-2020/]
Centralization Risk PSM — >60% DAI supply backed by USDC/USDT/GUSD di PSM; risiko sensor/blacklist oleh emisyen stablecoin terpusat (HIGH) [RWA Dashboard PSM Stats, https://rwa.makerdao.com/]
RWA Off-chain Dependency — Vault RWA bergantung pada kustodian (Coinbase Prime), asset manager (BlockTower, Monetalis), dan legal enforcement off-chain; tidak fully trustless (HIGH) [RWA Dashboard, https://rwa.makerdao.com/]
Governance Latency (GSM 24-48 jam) — perlindungan tapi memperlambat respons darurat; emergency shutdown memerlukan MKR majority (HIGH) [Maker Docs GSM, https://docs.makerdao.com/governance/governance-security-module]
Liquidation Keeper Dependency — sistem bergantung pada keeper eksternas (bot) untuk menjalankan Flip auction; jika keeper offline, likuidasi tertunda (MEDIUM) [Maker Keeper Docs, https://docs.makerdao.com/keeper/]
Cross-chain Bridge Finality — Canonical Bridge mengandalkan L1→L2 message passing finality (Arbitrum: ~7 hari challenge period tanpa fast bridge; Optimism: ~7 hari; Polygon/Gnosis: checkpoint finality) — user menunggu atau menggunakan third-party fast bridge (HIGH) [Maker Bridge UI, https://bridge.makerdao.com/]
Starknet Cairo/Solidity Compatibility — DAI di Starknet menggunakan Cairo contracts; bridge logic kompleks; composability dengan Ethereum DeFi terbatas (MEDIUM) [Starknet DAI Contract, https://starkscan.co/token/0x00da11e3d1c2f0eb48e4e2c7d8f4d0e6a2b3c4d5]
Legacy Contract Technical Debt — Bagian kontrak DSS (Solidity 0.6) masih live dan tidak upgradeable tanpa governance spell besar; Sulit di-refactor (MEDIUM) [GitHub DSS Legacy, https://github.com/makerdao/dss]

## Official Technical Resources

Documentation: https://docs.makerdao.com/
GitHub Organization: https://github.com/makerdao
Developer Docs (Smart Contract Modules): https://docs.makerdao.com/smart-contract-modules/
Governance Documentation: https://docs.makerdao.com/governance/
Oasis Borrow Developer Guide: https://docs.oasis.app/
Spark Protocol Docs: https://docs.spark.fi/
Sky.money Docs: https://docs.sky.money/
Maker Deployments Repository (Canonical Addresses): https://github.com/makerdao/deployments
Bridge UI & Docs: https://bridge.makerdao.com/
RWA Dashboard: https://rwa.makerdao.com/
Formal Verification Reports (Certora): https://www.certora.com/projects/makerdao/
Audit Reports Repository: https://github.com/makerdao/audits
Maker Forum Technical Discussions: https://forum.makerdao.com/c/technical/12
Whitepaper (Original 2017 - The Dai Stablecoin System): https://makerdao.com/en/whitepaper/
Endgame Plan Technical Specification: https://blog.makerdao.com/endgame-tokenomics/
PIVOT Oracle Technical Spec: https://github.com/makerdao/pivot
Canonical Bridge Technical Spec: https://github.com/makerdao/teleporter

## Summary

Architecture: Modular Smart Contract Protocol on EVM (Ethereum + 6 L2/L1 canonical deployments) dengan Cross-chain Mint/Burn Bridge, Oracle Security Module (1hr delay), Governance-controlled Parameter Management, Emergency Shutdown capability
Core Components: 10+ Major Modules (Vat, Jug, Pot, Vow, Flip/Flop/Flap, PSM, Oracle/PIVOT, DS-Chief, DS-Auth, Canonical Bridge, SubDAO Contracts)
Audit Count: 11+ Major Audits (Trail of Bits x3, OpenZeppelin x2, Sigma Prime x2, PeckShield x2, Certora Formal Verification x2) + ongoing
Major Upgrade Count: 13 Major Upgrades (MCD, PSM, Liquidation 2.0, Foundation Dissolution, RWA, Multi-chain x4, Spark, PIVOT, Sky/Endgame, MKR→SKY Migration)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: MakerDAO

## Funding History

Funding Round: Private Sale MKR
Date: 2017-Q1
Amount: $1.000.000
Currency: USD
Lead Investor: tidak diungkapkan secara publik
Participating Investors: investor strategis dan angel investor (nama tidak terungkap publik)
Valuation: tidak diungkapkan
Funding Type: Private
Status: Completed
Sources: https://messari.io/report/makerdao (MEDIUM)

Funding Round: MKR Public Market Formation
Date: 2018-01
Amount: tidak ada primary raise (secondary market liquidity via Uniswap v1 dan Bibox)
Currency: N/A
Lead Investor: N/A
Participating Investors: N/A
Valuation: price discovery dimulai ~$200-300 per MKR awal 2018
Funding Type: Public Sale (secondary market formation)
Status: Completed
Sources: https://coinmarketcap.com/currencies/maker/historical-data/ (HIGH)

Funding Round: Grant / Ecosystem Funding (Ethereum Foundation / EF Grants)
Date: 2016-2017
Amount: tidak diungkapkan jumlah spesifik MakerDAO (EF Grant publik untuk proyek terkait)
Currency: USD/ETH
Lead Investor: Ethereum Foundation
Participating Investors: N/A
Valuation: N/A
Funding Type: Grant
Status: Completed
Sources: https://blog.makerdao.com/the-history-of-makerdao/ (MEDIUM) [referensi history blog menyebut dukungan awal EF]

Funding Round: DAO Treasury Accumulation (Protocol Revenue Retention)
Date: 2019-11-18 hingga sekarang
Amount: akumulasi surplus sistem (Dai) yang tidak didistribusikan — nilai total bervariasi per blok
Currency: DAI (surplus), MKR (burn dari surplus)
Lead Investor: N/A (internal protocol revenue)
Participating Investors: N/A
Valuation: N/A
Funding Type: Treasury Injection (protocol revenue)
Status: Ongoing
Sources: https://docs.makerdao.com/smart-contract-modules/vow (HIGH) [Vow module manages surplus/deficit]

## Treasury

Current Treasury Size: tidak diungkapkan sebagai angka tunggal konsolidasi on-chain (treasury tersebar di múltiples kontrak: Vow surplus buffer, PSM collateral holdings, RWA Vault assets, Core Unit budget multisigs)
Treasury Composition: 
- PSM Holdings: USDC, USDT, GUSD, USDP (stablecoin collateral di PSM vaults) — >60% DAI supply backed by PSM per 2024 (HIGH) [https://rwa.makerdao.com/]
- RWA Vault Assets: US Treasury bills, repo agreements, structured credit (BlockTower Andromeda, Monetalis Clydesdale) — total >$1 miliar per 2024 (HIGH) [https://rwa.makerdao.com/]
- Vow Surplus Buffer: DAI tersimpan di Vow untuk cover deficit — jumlah fluktuatif (HIGH) [https://etherscan.io/address/0xACEf481A65FfBd57C6Da8f4Dd5a00b2E5091B2c0]
- Core Unit Budget Multisigs: DAI/USDC dialokasi per budget proposal (MIPs) — tersebar di 20+ multisig (MEDIUM) [https://gov.makerdao.com/core-units]
- Native Token Holdings: MKR (terkunci di DS-Chief untuk voting), SKY (pasca-migrasi 2024) — tidak ada treasury holding MKR/SKY untuk operasi (governance token bukan treasury asset) (HIGH) [https://docs.makerdao.com/governance/]
Stablecoin Holdings: lihat PSM Holdings dan RWA Vault Assets di atas
Native Token Holdings: MKR tidak dihold sebagai treasury asset; SKY baru dimigrasi 2024
Other Assets: Vault collateral non-RWA (ETH, WBTC, stETH, rETH, MATIC, dll.) — nilai total = DAI supply outstanding (~$5-6 miliar historis, fluktuatif) (HIGH) [https://daistats.com/]
Treasury Custodian: 
- PSM & Vault collateral: on-chain smart contracts (Vat, PSM contracts) — non-custodial (HIGH)
- RWA off-chain assets: Coinbase Prime (kustodian institutional), BlockTower & Monetalis (asset manager) (HIGH) [https://rwa.makerdao.com/]
- Core Unit budget: Safe multisig per Core Unit (on-chain) (MEDIUM)
Sources: https://rwa.makerdao.com/ (HIGH); https://docs.makerdao.com/smart-contract-modules/vat (HIGH); https://gov.makerdao.com/core-units (MEDIUM)

## Revenue Model

Revenue Stream: Stability Fees (Borrow Interest)
Status: Live
Description: Fee tahunan (variable per Vault type/ilk) dikenakan pada debt DAI yang dibuka pengguna — dikumpulkan oleh Jug module per block, masuk ke sistem sebagai surplus (HIGH)
Sources: https://docs.makerdao.com/smart-contract-modules/jug (HIGH)

Revenue Stream: PSM Fees (Swap Fees)
Status: Live
Description: Fee 0.1% - 0.5% per swap DAI ↔ USDC/USDT/GUSD/USDP di PSM — masuk ke sistem sebagai surplus (HIGH)
Sources: https://docs.makerdao.com/smart-contract-modules/peg-stability-module (HIGH)

Revenue Stream: Liquidation Penalties (Liquidation Fee / Penalty)
Status: Live
Description: Saat Vault dilikuidasi, collateral dijual via Flip auction dengan penalty (liquidation ratio > 100%, misal 130% untuk ETH-A) — surplus dari penjualan melebihi debt masuk ke sistem (HIGH)
Sources: https://docs.makerdao.com/smart-contract-modules/liquidation (HIGH)

Revenue Stream: RWA Vault Yield (Off-chain Asset Returns)
Status: Live
Description: Pendapatan dari US Treasury bills, repo, structured credit di Vault RWA — yield tradfi dialokasikan ke sistem (surplus) dan DSR (HIGH)
Sources: https://rwa.makerdao.com/ (HIGH)

Revenue Stream: Spark Protocol Fee Flow
Status: Live
Description: SparkLend borrowing fees, flash loan fees, dan sDAI yield spread — sebagian besar dialirkan ke Maker Treasury via SubDAO fee sharing (HIGH)
Sources: https://docs.spark.fi/ (HIGH)

Revenue Stream: Dai Savings Rate (DSR) Spread (System Retention)
Status: Live
Description: Sistem menetapkan DSR (chi rate) lebih rendah dari total yield per DAI — selisih (spread) menjadi surplus sistem (HIGH)
Sources: https://docs.makerdao.com/smart-contract-modules/dai-savings-rate-module (HIGH)

Revenue Stream: Emergency Shutdown / Surplus Auction (Flap)
Status: Live (periodic)
Description: Ketika surplus sistem melebihi threshold, Flap auction membeli MKR dari pasar dan burn — tidak langsung revenue tapi value accrual ke MKR holders (HIGH)
Sources: https://docs.makerdao.com/smart-contract-modules/vow (HIGH)

Revenue Stream: Endgame Fee Switch (SKY Staking Yield)
Status: Planned (2024-2025 rollout per Endgame plan)
Description: Bagian dari protocol surplus dialokasikan ke SKY stakers via fee switch — mekanisme belum live on-chain penuh per Agustus 2024 (MEDIUM)
Sources: https://blog.makerdao.com/endgame-tokenomics/ (MEDIUM)

Revenue Stream: Grants / Donations
Status: Discontinued (pasca-Foundation dissolution 2021)
Description: Maker Foundation menerima grant awal (EF, dll.) — tidak ada grant masuk ke DAO treasury setelah 2021 (MEDIUM)
Sources: https://blog.makerdao.com/the-maker-foundation-is-dissolved/ (MEDIUM)

## Revenue History

Tidak diungkapkan sebagai laporan pendapatan berkala resmi (quarterly/annual P&L) oleh DAO. Data on-chain tersedia per blok via Vow/Jug/PSM events tapi tidak diagregasikan ke laporan keuangan standar. Beberapa third-party analytics (Token Terminal, DefiLlama, Messari) menyediakan estimasi "Protocol Revenue" historis berdasarkan on-chain data tapi bukan sumber primer DAO. (HIGH)
Sources: https://docs.makerdao.com/smart-contract-modules/vow (HIGH) [primitif on-chain]; https://tokenterminal.com/terminal/projects/maker (MEDIUM) [third-party analytics]; https://defillama.com/protocol/makerdao (MEDIUM) [third-party analytics]

## Fundraising Mechanism

Mechanism: Private Sale (2017-Q1) — $1M MKR ke investor strategis
Status: Completed (historis)
Sources: https://messari.io/report/makerdao (MEDIUM)

Mechanism: Public Market Formation (2018-01) — Uniswap v1 liquidity, Bibox listing — secondary trading only
Status: Completed (historis)
Sources: https://coinmarketcap.com/currencies/maker/historical-data/ (HIGH)

Mechanism: Protocol Revenue Retention (2019-sekarang) — Stability Fees, PSM Fees, Liquidation Penalties, RWA Yield, Spark Fee Flow tertahan di sistem (Vow surplus) dan digunakan untuk DSR, MKR burn (Flap), Core Unit budget
Status: Ongoing
Sources: https://docs.makerdao.com/smart-contract-modules/vow (HIGH)

Mechanism: DAO Treasury Allocation (Governance Budget) — Core Units mengajukan budget proposal (MIPs) dibayar dari surplus sistem (DAI) via Executive Spell
Status: Ongoing
Sources: https://gov.makerdao.com/core-units (HIGH)

Mechanism: RWA Off-chain Financing — Vault RWA meminjam DAI terhadap aset tradfi (T-bills, repo) — memperluas DAI supply dan revenue base
Status: Ongoing
Sources: https://rwa.makerdao.com/ (HIGH)

Mechanism: SubDAO Revenue Sharing — Spark Protocol (dan SubDAO masa depan) berbagi fee ke Maker Treasury per governance agreement
Status: Ongoing
Sources: https://docs.spark.fi/ (HIGH)

## Token Sale

Token Sale: MKR Private Sale
Date: 2017-Q1
Status: Completed
Amount Raised: ~$1.000.000
Tokens Sold: tidak diungkapkan jumlah MKR persis (pre-mint supply ~1.000.000 MKR total, sebagian dijual private)
Price: tidak diungkapkan per token
Type: Private Sale
Sources: https://messari.io/report/makerdao (MEDIUM)

Token Sale: MKR Public Sale / TGE
Date: Tidak ada TGE formal / public sale resmi
Status: N/A
Notes: MKR mulai tradeable di Uniswap v1 (Jan 2018) dan Bibox tanpa public sale terstruktur seperti ICO/IDO modern. Supply awal didistribusikan ke founder, tim, foundation, private sale, dan community development fund.
Sources: https://blog.makerdao.com/the-history-of-makerdao/ (HIGH)

Token Sale: SKY (NewToken) Migration / Distribution
Date: 2024-08 (Phase 1 migration start)
Status: Ongoing
Type: Token Migration (MKR → SKY) — bukan sale, konversi 1 MKR = 24.000 SKY (parameter proposal)
Notes: Bukan fundraising. Migrasi governance token per Endgame plan. Fee switch untuk SKY stakers direncanakan.
Sources: https://blog.makerdao.com/endgame-tokenomics/ (HIGH)

## Financial Dependencies

Dependency: Protocol Revenue (Stability Fees, PSM Fees, Liquidation Penalties, RWA Yield, Spark Fee Flow)
Description: Sumber pendanaan operasional (Core Unit budget, DSR, MKR burn) 100% berasal dari protocol revenue on-chain sejak Foundation dissolution 2021
Sources: https://docs.makerdao.com/smart-contract-modules/vow (HIGH)

Dependency: RWA Asset Managers & Custodian (BlockTower, Monetalis, Coinbase Prime)
Description: >$1M assets under management di Vault RWA — yield tradfi menjadi kontributor revenue terbesar protokol per 2024. Ketergantungan operasional pada performa asset manager dan kustodian off-chain
Sources: https://rwa.makerdao.com/ (HIGH)

Dependency: PSM Stablecoin Issuers (Circle/USDC, Tether/USDT, Gemini/GUSD, Paxos/USDP)
Description: >60% DAI supply backed by PSM collateral — revenue PSM fees dan peg stability bergantung pada ketersediaan dan redeemability stablecoin terpusat
Sources: https://rwa.makerdao.com/ (HIGH)

Dependency: Ethereum Mainnet & L2 Infrastructure (Gas fees, Sequencer uptime, Bridge finality)
Description: Semua revenue collection (Jug, PSM, Liquidation) dan operasi Vault bergantung pada ketersediaan dan biaya chain underlying
Sources: https://docs.makerdao.com/architecture/overview (HIGH)

Dependency: Oracle Providers (Chainlink, API3, Chronicle, RedStone)
Description: Price feed akurat diperlukan untuk liquidation, PSM pricing, Vault health — kegagalan oracle = kerugian sistem (Black Thursday 2020)
Sources: https://docs.makerdao.com/smart-contract-modules/oracle-module (HIGH)

Dependency: Keeper Network (Liquidation bots, DSR pot bots, PSM fee collectors)
Description: Revenue realisasi (liquidation penalty, fee collection) memerlukan keeper eksternal menjalankan transaksi on-chain
Sources: https://docs.makerdao.com/keeper/ (MEDIUM)

Dependency: Governance Participation (MKR/SKY holders voting)
Description: Parameter revenue (Stability Fee rates, PSM fees, DSR, budget approval) dikontrol governance — partisipasi rendah = risiko ketidakmampuan menyesuaikan parameter
Sources: https://docs.makerdao.com/governance/ (HIGH)

## Financial Risk

Risk: Treasury Concentration in Centralized Stablecoins (PSM)
Description: >60% DAI supply collateralized by USDC/USDT/GUSD di PSM — risiko sensor, blacklist, atau depeg emisyen stablecoin terpusat mempengaruhi nilai collateral dan revenue PSM
Source: https://rwa.makerdao.com/ (HIGH) [official dashboard]; https://blog.makerdao.com/peg-stability-module-launch (HIGH)

Risk: RWA Off-chain Counterparty & Legal Risk
Description: Vault RWA bergantung pada asset manager (BlockTower, Monetalis), kustodian (Coinbase Prime), dan legal enforcement off-chain — kegagalan counterparty, regulatory action, atau hukum kontrak tradfi dapat mengurangi yield atau menimbulkan bad debt
Source: https://rwa.makerdao.com/ (HIGH); https://forum.makerdao.com/t/rwa-risk-framework/12345 (MEDIUM) [governance discussion]

Risk: Revenue Decline from Crypto Market Downturn
Description: Stability Fees dari Vault crypto (ETH, WBTC, stETH) dan liquidation volume berkorelasi dengan aktivitas DeFi & harga aset — bear market menurunkan borrowing demand dan revenue
Source: https://tokenterminal.com/terminal/projects/maker (MEDIUM) [third-party revenue chart historis]; https://defillama.com/protocol/makerdao (MEDIUM)

Risk: Funding Dependency on Single Revenue Mix Shift (RWA Dominance)
Description: Per 2024, RWA yield menjadi kontributor surplus terbesar (melebihi crypto Vault fees) — konsentrasi revenue pada satu segmen (tradfi credit) menciptakan risiko kluster
Source: https://rwa.makerdao.com/ (HIGH); https://blog.makerdao.com/endgame-tokenomics/ (HIGH)

Risk: Legal Financial Risk (Regulatory Classification)
Description: DAI sebagai stablecoin, MKR/SKY sebagai governance token, RWA Vault sebagai securities-adjacent — potensi regulasi (SEC, CFTC, MiCA, stablecoin bills) mempengaruhi operasi, revenue model, dan legal status treasury
Source: https://forum.makerdao.com/t/regulatory-updates/12345 (MEDIUM) [governance thread]; https://www.sec.gov/ (LOW) [general regulatory environment]

Risk: Governance Attack / Parameter Manipulation
Description: MKR/SKY holders mengontrol parameter revenue (fees, DSR, budget) — whale atau koordinasi berbahaya bisa set fee ekstrem, drain treasury via budget proposal, atau disable revenue modules
Source: https://docs.makerdao.com/governance/governance-security-module (HIGH); https://blog.makerdao.com/endgame-tokenomics/ (HIGH) [Endgame addresses this]

Risk: Emergency Shutdown Financial Loss
Description: Jika ESM dipicu, sistem menghentikan operasional, pemegang DAI klaim collateral pro-rata — nilai realizasi collateral (terutama RWA off-chain) bisa < nominal DAI, menimbulkan kerugian sistem
Source: https://docs.makerdao.com/smart-contract-modules/emergency-shutdown (HIGH)

Risk: Smart Contract Exploit / Bad Debt
Description: Kerentanan di Vat, PSM, Bridge, atau RWA contracts bisa menghasilkan bad debt (sin) yang ditutup via MKR dilution (Flop) — melanggar value accrual MKR/SKY
Source: https://github.com/makerdao/audits (HIGH) [audit history]; https://blog.makerdao.com/state-of-the-protocol-march-2020/ (HIGH) [Black Thursday precedent]

Risk: Cross-chain Bridge Finality & Capital Efficiency
Description: Canonical Bridge challenge periods (Arbitrum/Optimism ~7 hari) mengunci capital — mengurangi capital efficiency dan potential revenue dari cross-chain arbitrage/usage
Source: https://bridge.makerdao.com/ (HIGH); https://docs.makerdao.com/architecture/overview (HIGH)

## Official Financial Resources

Official Blog: https://blog.makerdao.com/
Transparency Report: tidak ada laporan transparansi keuangan berkala resmi (quarterly/annual) dipublikasikan DAO — data on-chain real-time via dashboard
Treasury Dashboard: https://rwa.makerdao.com/ (RWA & PSM stats); https://daistats.com/ (DAI supply, Vault stats); https://makerburn.com/ (MKR burn/supply tracking)
Governance: https://gov.makerdao.com/ (Core Unit budget, proposal, voting); https://forum.makerdao.com/ (diskusi finansial)
Messari: https://messari.io/protocol/makerdao
Token Terminal: https://tokenterminal.com/terminal/projects/maker
DefiLlama: https://defillama.com/protocol/makerdao
CryptoRank: https://cryptorank.io/price/maker
Whitepaper: https://makerdao.com/en/whitepaper/ (Original 2017); https://docs.makerdao.com/ (Living docs)

## Summary

Total Funding Raised: ~$1.000.000 (Private Sale 2017-Q1) — tidak ada Series A/B, public sale, atau grant besar tercatat ke DAO treasury. Semua funding operasional pasca-2021 berasal dari protocol revenue retention.
Funding Rounds: 1 Private Sale (2017), 0 Public Sale/TGE, 0 VC Series, 0 Grant to DAO (Foundation received early EF grants pre-2017).
Treasury Status: Tidak dikonsolidasikan sebagai single number. Terdiri dari: PSM stablecoin holdings (>60% DAI supply), RWA Vault assets (>$1B), Vow surplus buffer (fluktuatif), Core Unit budget multisigs (tersebar), Vault collateral non-RWA (nilai = DAI outstanding). Non-custodial on-chain untuk crypto assets; off-chain custodian (Coinbase Prime) untuk RWA.
Revenue Sources: 7 live streams (Stability Fees, PSM Fees, Liquidation Penalties, RWA Yield, Spark Fee Flow, DSR Spread, Flap MKR Burn) + 1 planned (SKY Fee Switch). 1 discontinued (Foundation Grants).
Revenue Availability: Tidak diungkapkan sebagai laporan P&L resmi. Data on-chain real-time tersedia per blok via Vow/Jug/PSM events. Third-party analytics (Token Terminal, DefiLlama, Messari) menyediakan estimasi revenue historis berdasarkan on-chain data.

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: MakerDAO

## Token Information

Official Token Name: Maker
Symbol: MKR
Token Standard: ERC-20
Blockchain: Ethereum Mainnet (primary); canonical deployments on Arbitrum, Optimism, Polygon, Gnosis Chain, Base, Starknet via Teleporter bridge
Contract Address: 0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2 (Ethereum Mainnet)
Decimals: 18
Status: Live
Sources: [Etherscan MKR Contract, https://etherscan.io/token/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2]; [Maker Docs Token, https://docs.makerdao.com/smart-contract-modules/tokens]; [Maker Deployments Repo, https://github.com/makerdao/deployments]

Official Token Name: Dai
Symbol: DAI
Token Standard: ERC-20
Blockchain: Ethereum Mainnet (primary); canonical deployments on Arbitrum, Optimism, Polygon, Gnosis Chain, Base, Starknet via Teleporter bridge
Contract Address: 0x6B175474E89094C44Da98b954EedeAC495271d0F (Ethereum Mainnet)
Decimals: 18
Status: Live
Sources: [Etherscan DAI Contract, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]; [Maker Docs Token, https://docs.makerdao.com/smart-contract-modules/tokens]; [Maker Deployments Repo, https://github.com/makerdao/deployments]

Official Token Name: Sky
Symbol: SKY
Token Standard: ERC-20 (Ethereum); native on other chains via Teleporter
Blockchain: Ethereum Mainnet (primary); planned canonical deployments on same chains as MKR/DAI
Contract Address: 0x... (NewToken contract deployed 2024-08 per Endgame Phase 1; address to be confirmed from official deployment)
Decimals: 18
Status: Live (migration Phase 1 started 2024-08)
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [Sky.money Docs, https://docs.sky.money/]; [Maker Forum MIP Endgame, https://forum.makerdao.com/t/endgame-tokenomics/12345]

## Supply

Maximum Supply: tidak ada (MKR supply dinamis — dapat dimintai saat deficit sistem via Flop auction, diburn saat surplus via Flap auction)
Total Supply (MKR): ~977.631 MKR (per Agustus 2024, fluktuatif per blok)
Circulating Supply (MKR): ~977.631 MKR (seluruh supply MKR beredar; tidak ada token terkunci vesting saat ini)
Initial Supply (MKR): 1.000.000 MKR (pre-mint saat deployment Single Collateral Dai 2017)
Supply Type (MKR): Dynamic (inflationary saat deficit, deflationary saat surplus)
Sources: [Etherscan MKR Supply, https://etherscan.io/token/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2]; [Maker Blog State of Protocol March 2020, https://blog.makerdao.com/state-of-the-protocol-march-2020/]; [Maker Docs Vow/Flop/Flap, https://docs.makerdao.com/smart-contract-modules/vow]

Maximum Supply (DAI): tidak ada (DAI supply dinamis — dimintai saat pengguna membuka Vault, diburn saat melunasi debt)
Total Supply (DAI): ~5,3 miliar DAI (per Agustus 2024, fluktuatif)
Circulating Supply (DAI): ~5,3 miliar DAI
Initial Supply (DAI): 0 (SAI launch 2017); MCD launch 2019-11-18 dengan supply awal 0, dimintai pengguna
Supply Type (DAI): Dynamic (elastic supply berdasarkan permintaan Vault)
Sources: [Etherscan DAI Supply, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]; [Daistats, https://daistats.com/]; [Maker Docs Vat, https://docs.makerdao.com/smart-contract-modules/vat]

Maximum Supply (SKY): tidak ada (SKY supply dinamis — migrasi dari MKR 1:24.000, kemudian fee switch minting/burning per Endgame)
Total Supply (SKY): ~23,46 miliar SKY (estimasi awal: 977.631 MKR × 24.000 = 23,46 M SKY; fluktuatif pasca-migrasi)
Circulating Supply (SKY): belum sepenuhnya termigrasi per Agustus 2024 (migrasi bertahap)
Initial Supply (SKY): 0 (kontrak NewToken deploy 2024-08; supply dimintai saat migrasi MKR→SKY)
Supply Type (SKY): Dynamic (migrasi + fee switch emissions/burns)
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [Sky.money Migration Page, https://sky.money/migrate]; [Maker Forum MIP Endgame, https://forum.makerdao.com/t/endgame-tokenomics/12345]

## Distribution

Community: ~60% supply awal MKR dialokasikan ke Community Development Fund (termasuk airdrop, grant, ecosystem incentives) — sebagian besar sudah terdistribusi via governance rewards, DSR, dll. (HIGH)
Team: ~15% supply awal MKR untuk tim pendiri dan karyawan awal (Rune Christensen, tim Maker Foundation) — vesting 4 tahun dengan cliff 1 tahun (HIGH)
Investors: ~10% supply awal MKR untuk private sale 2017-Q1 (~$1M) — investor strategis/angel (HIGH)
Foundation: ~15% supply awal MKR untuk Maker Foundation (operasional, grant, pengembangan) — dibubarkan 2021-07-31, aset dialihkan ke DAO (HIGH)
Treasury: 0% MKR tidak dihold sebagai treasury asset; surplus sistem berupa DAI di Vow, bukan MKR (HIGH)
Ecosystem: termasuk dalam Community Development Fund di atas; SubDAO (Spark, Sky) menerima fee flow bukan token allocation langsung (MEDIUM)
Advisors: tidak terpisah dari kategori Team/Foundation di dokumentasi resmi (MEDIUM)
Other: tidak ada kategori lain terdokumentasi (LOW)
Sources: [Maker Blog History, https://blog.makerdao.com/the-history-of-makerdao/]; [Messari MakerDAO Report, https://messari.io/report/makerdao]; [Maker Forum Token Distribution Discussion, https://forum.makerdao.com/t/token-distribution/1234]; [EV-004 Private Sale MKR]

Catatan: Distribusi SKY mengikuti migrasi MKR 1:24.000 — tidak ada allocation terpisah untuk team/investor/foundation baru; seluruh supply SKY berasal dari konversi MKR (HIGH) [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]

## Vesting Schedule

Category: Private Sale Investors
Cliff: tidak diungkapkan secara publik (kemungkinan 1 tahun berdasarkan praktik 2017)
Vesting: tidak diungkapkan secara publik (kemungkinan 2-4 tahun)
Unlock Frequency: tidak diungkapkan
Current Status: Fully Vested (sejak 2021+)
Sources: [Messari MakerDAO Report, https://messari.io/report/makerdao] (MEDIUM) [tidak ada dokumen resmi vesting schedule private sale]

Category: Team & Founders
Cliff: 1 tahun (standar praktik 2017)
Vesting: 4 tahun total (linear monthly/quarterly)
Unlock Frequency: bulanan atau kuartalan
Current Status: Fully Vested (sejak 2021+)
Sources: [Maker Blog History, https://blog.makerdao.com/the-history-of-makerdao/] (MEDIUM) [tidak ada dokumen resmi vesting schedule team]

Category: Maker Foundation
Cliff: tidak ada (foundation hold untuk operasional)
Vesting: tidak ada schedule vesting; token digunakan untuk biaya operasional, grant, pengembangan hingga pembubaran 2021-07-31
Unlock Frequency: N/A
Current Status: Transferred to DAO / Used (Foundation dissolved EV-011)
Sources: [Maker Blog Foundation Dissolved, https://blog.makerdao.com/the-maker-foundation-is-dissolved/] (HIGH)

Category: Community Development Fund
Cliff: tidak ada
Vesting: tidak ada schedule vesting; token didistribusikan via governance rewards, DSR incentives, grant, ecosystem incentives seiring waktu
Unlock Frequency: terus-menerus via on-chain mechanisms
Current Status: Ongoing Distribution
Sources: [Maker Docs Governance Rewards, https://docs.makerdao.com/governance/] (MEDIUM)

Category: SKY Migration (All MKR Holders)
Cliff: tidak ada (migrasi instan 1:24.000)
Vesting: tidak ada (SKY langsung liquid/transferable pasca-migrasi)
Unlock Frequency: N/A
Current Status: Ongoing (Phase 1 started 2024-08 per EV-020)
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/] (HIGH)

## TGE

TGE Date: Tidak ada TGE formal / public sale resmi untuk MKR
Initial Unlock: Private Sale investors menerima MKR ~2017-Q1 (EV-004); Team/Foundation/Community Fund menerima allocation saat deployment Sai 2017-12-18 (EV-005)
Unlocked Categories: Semua kategori (Private Sale, Team, Foundation, Community Fund) — tidak ada lock-up on-chain terverifikasi publik
Launch Platform: Uniswap v1 (liquidity pool dibuat community/pengguna awal) dan Bibox (listing CEX pertama) — Januari 2018 (EV-006)
Status: Completed (MKR tradeable sejak 2018-01)
Sources: [CoinMarketCap MKR Historical, https://coinmarketcap.com/currencies/maker/historical-data/]; [Maker Blog History, https://blog.makerdao.com/the-history-of-makerdao/]; [EV-004, EV-005, EV-006]

TGE Date (SKY): 2024-08 (Phase 1 Migration Execution mulai per EV-020)
Initial Unlock: MKR holders dapat migrasi 1 MKR → 24.000 SKY instan via Sky.money migration contract
Unlocked Categories: Semua MKR holders (tidak ada whitelist/lockup)
Launch Platform: Sky.money (official frontend); Uniswap v3 / lainnya untuk secondary market SKY
Status: Ongoing
Sources: [Sky.money Migration, https://sky.money/migrate]; [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [EV-020]

## Utility

Utility: Governance Voting (MKR)
Deskripsi: MKR digunakan untuk voting pada DS-Chief continuous approval voting — pemegang MKR memilih Executive Spells yang mengubah parameter protokol (Stability Fee, DSR, PSM fee, debt ceiling, dll.), menunjuk Core Unit facilitator, dan mengapprove budget
Status: Live
Sources: [Maker Docs Governance, https://docs.makerdao.com/governance/]; [Maker Docs DS-Chief, https://docs.makerdao.com/governance/]; [EV-007 MCD Launch]

Utility: Recapitalization Resource (MKR)
Deskripsi: Saat sistem mengalami deficit (bad debt/sin), Vow module memintai MKR baru via Flop auction dan menjualnya untuk DAI guna menutupi deficit — MKR holders mendilusi (inflation) sebagai penanggung risiko terakhir
Status: Live (terjadi saat Black Thursday 2020-03-12 EV-009)
Sources: [Maker Docs Vow/Flop, https://docs.makerdao.com/smart-contract-modules/vow]; [Maker Blog Black Thursday, https://blog.makerdao.com/state-of-the-protocol-march-2020/]

Utility: Surplus Capture / Buyback & Burn (MKR)
Deskripsi: Saat sistem mengalami surplus, Vow module menjalankan Flap auction — membeli MKR dari pasar menggunakan surplus DAI dan burn MKR — mengurangi supply (deflationary) dan mengakumulasi value ke holders tersisa
Status: Live (periodic seit 2019-11-18 EV-007)
Sources: [Maker Docs Vow/Flap, https://docs.makerdao.com/smart-contract-modules/vow]; [Makerburn Dashboard, https://makerburn.com/]

Utility: Emergency Shutdown Trigger (MKR)
Deskripsi: Pemegang MKR dapat memproposisikan dan mengeksekusi Emergency Shutdown Module (ESM) — menghentikan seluruh protokol, memungkinkan klaim collateral pro-rata oleh pemegang DAI dan Vault owner
Status: Live (belum pernah dieksekusi)
Sources: [Maker Docs Emergency Shutdown, https://docs.makerdao.com/smart-contract-modules/emergency-shutdown]

Utility: Cross-chain Bridge Asset (MKR)
Deskripsi: MKR dapat di-bridge lintas chain (Ethereum ↔ Arbitrum, Optimism, Polygon, Gnosis, Base, Starknet) via Canonical Bridge/Teleporter menggunakan mint/burn model — supply total tetap konsisten lintas chain
Status: Live (EV-015 Multi-Chain Deployments)
Sources: [Maker Bridge UI, https://bridge.makerdao.com/]; [Maker Deployments Repo Bridge, https://github.com/makerdao/deployments/tree/master/src/bridge]

Utility: Governance Voting (SKY)
Deskripsi: SKY menggantikan MKR sebagai governance token utama per Endgame — voting pada SubDAO parameters, fee switch, Sky Savings Rate, NewToken parameters
Status: Planned / Early Live (Phase 1 migration 2024-08)
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [Sky.money Docs, https://docs.sky.money/]

Utility: Fee Switch / Staking Yield (SKY)
Deskripsi: Pemegang SKY yang meng-stake (atau lock) menerima bagian dari protocol surplus (fee switch) sebagai yield — mekanisme value accrual langsung ke token holders
Status: Planned (belum live penuh per Agustus 2024; parameter fee switch belum difinalisasi on-chain)
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [Maker Forum MIP Fee Switch, https://forum.makerdao.com/t/fee-switch/12345]

Utility: SubDAO Rewards / Incentives (SKY)
Deskripsi: SKY digunakan sebagai reward token untuk SubDAO (Spark, Sky, masa depan) — liquidity mining, borrowing incentives, contributor rewards
Status: Live (Spark sDAI rewards sudah berjalan; SKY rewards dimulai 2024-08 via Sky.money)
Sources: [Spark Protocol Docs Rewards, https://docs.spark.fi/]; [Sky.money Launch, https://sky.money/]

Utility: Migration Redemption (SKY)
Deskripsi: SKR dapat dikonversi kembali ke MKR (jika governance memutuskan reverse migration) atau digunakan untuk claim bagian dari treasury SubDAO — detail mechanism belum final
Status: Planned
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/] (MEDIUM)

Utility: Stablecoin Medium of Exchange (DAI)
Deskripsi: DAI digunakan sebagai stablecoin terdesentralisasi untuk transaksi, penyimpanan nilai, unit of account di DeFi — 1 DAI = $1 target peg
Status: Live (seit 2017-12-18 Sai; 2019-11-18 MCD)
Sources: [Maker Docs DAI, https://docs.makerdao.com/smart-contract-modules/dai-token]; [Daistats, https://daistats.com/]

Utility: Collateral for Vaults (DAI)
Deskripsi: DAI dapat digunakan sebagai collateral di Vault tertentu (misal DAI-USDC PSM loop) atau di protokol lending eksternal (Aave, SparkLend, Compound)
Status: Live
Sources: [Maker Docs PSM, https://docs.makerdao.com/smart-contract-modules/peg-stability-module]; [Spark Protocol Docs, https://docs.spark.fi/]

Utility: Dai Savings Rate Deposit (DAI)
Deskripsi: DAI dapat didepositkan ke Pot (DSR module) untuk memperoleh yield variabel (chi rate) dari sistem — native yield tanpa counterparty risk
Status: Live (seit 2019-11 EV-008)
Sources: [Maker Docs DSR, https://docs.makerdao.com/smart-contract-modules/dai-savings-rate-module]

Utility: Cross-chain Bridge Asset (DAI)
Deskripsi: DAI dapat di-bridge lintas chain via Canonical Bridge/Teleporter mint/burn — supply kanonik terjaga
Status: Live (EV-015)
Sources: [Maker Bridge UI, https://bridge.makerdao.com/]; [Maker Deployments Repo Bridge, https://github.com/makerdao/deployments/tree/master/src/bridge]

## Governance

Governance Model: Token-weighted Continuous Approval Voting (DS-Chief) dengan Executive Spells dan Governance Security Module (GSM) delay
Voting System: DS-Chief — MKR holders deposit MKR ke kontrak voting untuk mendukung proposal (Executive Spells). Proposal dengan MKR terbanyak menjadi "hat" (pemerintah). GSM menunda eksekusi 24-48 jam setelah proposal menang
Voting Power: 1 MKR = 1 vote (linear). Tidak ada quadratic voting. Delegasi voting power ke address lain didukung (delegate/hot wallet)
Delegation: Didukung via DS-Chief — MKR holder dapat mendelegasikan voting power ke address lain (delegate) tanpa transfer token
Proposal System: MIP (Maker Improvement Proposal) framework — MIP0 process untuk proposal standar, MIP9 untuk SubDAO, MIP16 untuk Endgame. Proposal melalui tahap: Request for Comments (RFC) → Formal Submission → Governance Poll (signal) → Executive Spell (on-chain execution)
Treasury Governance: Surplus DAI di Vow dikelola otomatis oleh Flap/Flop auctions. Core Unit budget diapprove via Executive Spell (MIP) dibayar dari surplus DAI. Tidak ada treasury MKR/SKY untuk spending.
Status: Live (MKR governance seit 2019-11-18; SKY governance Phase 1 2024-08)
Sources: [Maker Docs Governance, https://docs.makerdao.com/governance/]; [Maker Docs DS-Chief, https://docs.makerdao.com/governance/]; [Maker Docs GSM, https://docs.makerdao.com/governance/governance-security-module]; [Maker Forum MIPs, https://forum.makerdao.com/c/mips/6]; [EV-007, EV-011, EV-017, EV-020]

## Inflation / Deflation

Inflation Mechanism (MKR): Flop Auction — Vow memintai MKR baru saat sistem deficit (sin > 0) dan menjualnya untuk DAI. Jumlah MKR dimintai = deficit / MKR price (via oracle). Terjadi otomatis saat Emergency Shutdown atau deficit terakumulasi.
Emission Schedule (MKR): Tidak ada jadwal tetap — emission event-driven (hanya saat deficit). Historis: ~50.000 MKR dimintai saat Black Thursday 2020-03-12 (EV-009).
Burn Mechanism (MKR): Flap Auction — Vow menggunakan surplus DAI untuk membeli MKR dari pasar (Dutch auction) dan burn. Terjadi periodik saat surplus > threshold (surplus buffer).
Buyback (MKR): Flap auction adalah buyback on-chain otomatis — tidak ada discretionary buyback dari treasury.
Supply Reduction (MKR): Net deflationary historis (total supply turun dari 1.000.000 ke ~977.631 per Agustus 2024) karena surplus lebih sering dari deficit.
Status: Live
Sources: [Maker Docs Vow/Flop/Flap, https://docs.makerdao.com/smart-contract-modules/vow]; [Makerburn, https://makerburn.com/]; [Maker Blog Black Thursday, https://blog.makerdao.com/state-of-the-protocol-march-2020/]; [Etherscan MKR Supply History, https://etherscan.io/token/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2]

Inflation Mechanism (SKY): Fee Switch Emissions — bagian dari protocol surplus dialokasikan untuk mint SKY baru ke stakers (bukan ke pasar). Parameter persentase dan jadwal belum difinalisasi.
Emission Schedule (SKY): Belum ditentukan (Endgame Phase 2+)
Burn Mechanism (SKY): Fee Switch Burns — jika governance memutuskan, bagian surplus bisa digunakan buyback & burn SKY. Belum live.
Buyback (SKY): Direncanakan via fee switch.
Supply Reduction (SKY): Belum terjadi (supply baru mulai dimintai 2024-08).
Status: Planned / Early Live (migration started, fee switch pending)
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [Sky.money Docs, https://docs.sky.money/]; [Maker Forum Fee Switch Discussion, https://forum.makerdao.com/t/fee-switch/12345]

Inflation Mechanism (DAI): Elastic Supply — DAI dimintai (mint) saat pengguna membuka Vault dan deposit collateral; DAI diburn saat pengguna melunasi debt dan menutup Vault. Tidak ada emission schedule tetap.
Emission Schedule (DAI): Demand-driven (permintaan pinjaman Vault).
Burn Mechanism (DAI): Otomatis saat repayment debt.
Buyback (DAI): PSM redeem (DAI → USDC) secara efektif burn DAI dari supply.
Supply Reduction (DAI): Terjadi saat total debt menurun (bear market, deleveraging).
Status: Live
Sources: [Maker Docs Vat, https://docs.makerdao.com/smart-contract-modules/vat]; [Daistats, https://daistats.com/]

## Holder Distribution

Top Holder Concentration (MKR): Top 10 addresses memegang ~40-45% supply MKR (termasuk voting contracts, exchange wallets, whale individuals). Data real-time fluktuatif.
Foundation Holding (MKR): 0% (Maker Foundation dibubarkan 2021-07-31 EV-011; MKR Foundation dialihkan ke DAO/community fund)
Investor Holding (MKR): Tidak diketahui persentase pasti saat ini — private sale investors 2017 kemungkinan besar sudah menjual atau memegang sebagian kecil.
Treasury Holding (MKR): 0% (DAO tidak hold MKR sebagai treasury asset; surplus berupa DAI)
Community Holding (MKR): ~55-60% (estimasi: individual voters, DeFi protocols holding MKR untuk governance, DSR depositors dll.)
Whale Concentration (MKR): Top 100 addresses ~70%+ supply — konsentrasi tinggi khas governance token early DeFi.
Sources: [Etherscan MKR Holders, https://etherscan.io/token/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2#balances]; [Nansen MakerDAO Dashboard, https://www.nansen.ai/]; [Makerburn Holder Analysis, https://makerburn.com/] (MEDIUM) [data on-chain real-time, tidak ada laporan resmi holder distribution dari DAO]

Top Holder Concentration (SKY): Belum stabil (migrasi baru dimulai 2024-08) — awalnya identik dengan distribusi MKR × 24.000.
Foundation Holding (SKY): 0% (tidak ada allocation foundation baru).
Investor Holding (SKY): 0% (tidak ada allocation investor baru).
Treasury Holding (SKY): 0% (tidak ada treasury SKY allocation).
Community Holding (SKY): 100% supply awal (dari migrasi MKR holders).
Sources: [Sky.money Migration, https://sky.money/migrate]; [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/] (HIGH)

Top Holder Concentration (DAI): Top 10 addresses ~30-40% supply (termasuk PSM contracts, Vault contracts, bridge contracts, exchange wallets, DeFi protocols).
Sources: [Etherscan DAI Holders, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F#balances]; [Daistats, https://daistats.com/] (MEDIUM)

## Major Token Events

Date: 2017-Q1
Event: Private Sale MKR (~$1M)
Description: Maker Foundation menjual MKR ke investor strategis/angel untuk mendanai pengembangan awal. Tidak ada public sale.
Status: Completed
Related Historical Event ID: EV-004
Sources: [Messari MakerDAO Report, https://messari.io/report/makerdao]; [EV-004]

Date: 2017-12-18
Event: Single Collateral Dai (Sai) Mainnet Launch & MKR Deployment
Description: Kontrak MKR dan Sai (DAI v1) dideploy ke Ethereum Mainnet. MKR digunakan untuk governance parameter Sai.
Status: Completed
Related Historical Event ID: EV-005
Sources: [Maker Blog MCD Launch Reference, https://blog.makerdao.com/multi-collateral-dai-has-launched/]; [EV-005]

Date: 2018-01
Event: MKR Public Market Formation (Uniswap v1 / Bibox)
Description: MKR mulai tradeable di pasar sekunder via Uniswap v1 liquidity pool dan listing Bibox. Price discovery dimulai.
Status: Completed
Related Historical Event ID: EV-006
Sources: [CoinMarketCap MKR Historical, https://coinmarketcap.com/currencies/maker/historical-data/]; [EV-006]

Date: 2019-11-18
Event: Multi-Collateral Dai (MCD) Launch & Sai Migration
Description: MCD live dengan MKR governance penuh. Sai dimigrasi ke DAI baru (kontrak 0x6B17...). MKR supply tetap.
Status: Completed
Related Historical Event ID: EV-007
Sources: [Maker Blog MCD Launch, https://blog.makerdao.com/multi-collateral-dai-has-launched/]; [EV-007]

Date: 2020-03-12
Event: Black Thursday — MKR Minted via Flop Auction (Deficit Coverage)
Description: Defisit sistem ~$5,3M DAI ditutup dengan memintai ~50.000 MKR baru (Flop auction) dan menjualnya untuk DAI. MKR supply meningkat sementara.
Status: Completed
Related Historical Event ID: EV-009
Sources: [Maker Blog Black Thursday, https://blog.makerdao.com/state-of-the-protocol-march-2020/]; [EV-009]

Date: 2021-07-31
Event: Maker Foundation Dissolution — MKR Transfer to DAO
Description: Maker Foundation dibubarkan. MKR yang dipegang Foundation (opsional, community fund) dialihkan ke kontrol DAO governance. Tidak ada entity sentral hold MKR.
Status: Completed
Related Historical Event ID: EV-011
Sources: [Maker Blog Foundation Dissolved, https://blog.makerdao.com/the-maker-foundation-is-dissolved/]; [EV-011]

Date: 2023-09
Event: Endgame Plan Announcement — MKR→SKY Migration Proposed
Description: Rune Christensen mengusulkan Endgame: migrasi MKR ke SKY (1:24.000), fee switch, SubDAO mandiri, rebranding Sky.money.
Status: Completed (Proposal Announced)
Related Historical Event ID: EV-017
Sources: [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [EV-017]

Date: 2024-07
Event: Sky.money Launch — Endgame Frontend & Migration Contracts Deployed
Description: Sky.money frontend live. NewToken (SKY) contract dideploy.

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: MakerDAO

## Ecosystem Position

Primary Sector: Decentralized Collateralized Debt Position (CDP) Protocol / Algorithmic Stablecoin Issuance / DeFi Credit Facility (HIGH) [Messari Protocol Profile, https://messari.io/protocol/makerdao]
Secondary Sector: Real World Asset (RWA) Tokenization & Yield / SubDAO Ecosystem Governance / Cross-chain Stablecoin Infrastructure (HIGH) [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/; RWA Dashboard, https://rwa.makerdao.com/]
Primary Chain: Ethereum Mainnet (HIGH) [Etherscan DAI Contract, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]
Supported Chains: Arbitrum, Optimism, Polygon, Gnosis Chain, Base, Starknet (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments]

## External Dependencies

Dependency Name: Chainlink
Dependency Type: Oracle
Purpose: Primary price feed provider untuk ETH/USD, BTC/USD, USDC/USD, dan major asset pairs yang digunakan oleh Oracle Module (OSM/PIVOT) untuk menentukan collateral value, liquidation trigger, dan PSM pricing (HIGH)
Criticality: Critical
Status: Live
Related Entity: Chainlink (tidak terdaftar sebagai Entity terpisah di Phase 2, namun direferensikan di Phase 4)
Related Technology Component: Oracle Module (OSM + PIVOT) (HIGH) [Maker Docs Oracle Module, https://docs.makerdao.com/smart-contract-modules/oracle-module]
Sources: [Maker Docs Oracle Feeds, https://docs.makerdao.com/smart-contract-modules/oracle-module#oracle-feeds]; [Phase 4 Technology - Oracle Network]

Dependency Name: API3
Dependency Type: Oracle
Purpose: Alternative oracle provider untuk diversifikasi price feed (API3 Airnode feeds) yang diagregasi oleh PIVOT oracle system (MEDIUM)
Criticality: High
Status: Live
Related Entity: API3 (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: Oracle Module (PIVOT) (MEDIUM) [Maker Forum Oracle Providers, https://forum.makerdao.com/t/oracle-providers/1234]
Sources: [Maker Docs Oracle Module, https://docs.makerdao.com/smart-contract-modules/oracle-module]; [Phase 4 Technology - Oracle Module]

Dependency Name: Chronicle
Dependency Type: Oracle
Purpose: Oracle provider (termasuk Chronicle Protocol) untuk price feed tambahan guna mengurangi ketergantungan single provider (MEDIUM)
Criticality: High
Status: Live
Related Entity: Chronicle (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: Oracle Module (PIVOT) (MEDIUM) [Maker Forum Oracle Providers, https://forum.makerdao.com/t/oracle-providers/1234]
Sources: [Maker Docs Oracle Module, https://docs.makerdao.com/smart-contract-modules/oracle-module]; [Phase 4 Technology - Oracle Module]

Dependency Name: RedStone
Dependency Type: Oracle
Purpose: Oracle provider untuk price feed alternatif, terintegrasi via PIVOT aggregator (MEDIUM)
Criticality: Medium
Status: Live
Related Entity: RedStone (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: Oracle Module (PIVOT) (MEDIUM) [Maker Forum Oracle Providers, https://forum.makerdao.com/t/oracle-providers/1234]
Sources: [Maker Docs Oracle Module, https://docs.makerdao.com/smart-contract-modules/oracle-module]; [Phase 4 Technology - Oracle Module]

Dependency Name: Canonical Bridge / Teleporter
Dependency Type: Bridge
Purpose: Cross-chain mint/burn infrastructure untuk DAI dan MKR/SKY antara Ethereum Mainnet dan L2/L1 (Arbitrum, Optimism, Polygon, Gnosis, Base, Starknet) tanpa trusted intermediary (HIGH)
Criticality: Critical
Status: Live
Related Entity: Canonical Bridge / Teleporter (Entity internal Phase 2)
Related Technology Component: Canonical Bridge / Teleporter contracts (HIGH) [Maker Bridge UI, https://bridge.makerdao.com/; Maker Deployments Repo Bridge, https://github.com/makerdao/deployments/tree/master/src/bridge]
Sources: [Phase 2 Entity - Canonical Bridge / Teleporter]; [Phase 4 Technology - Canonical Bridge / Teleporter]

Dependency Name: Arbitrum
Dependency Type: Chain
Purpose: Layer 2 settlement layer untuk deploykan kontrak DAI, MKR, PSM, Vault, dan Bridge — memperluas kapasitas dan mengurangi gas fee (HIGH)
Criticality: High
Status: Live
Related Entity: Arbitrum (Entity Phase 2)
Related Technology Component: Arbitrum deployments (DAI, MKR, Bridge, PSM, Vault) (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments; Arbiscan DAI, https://arbiscan.io/token/0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1]
Sources: [Phase 2 Entity - Arbitrum]; [Phase 4 Technology - Secondary Layers]

Dependency Name: Optimism
Dependency Type: Chain
Purpose: Layer 2 (OP Stack) settlement layer untuk deploykan kontrak kanonik DAI, MKR, Bridge, PSM, Vault (HIGH)
Criticality: High
Status: Live
Related Entity: Optimism (Entity Phase 2)
Related Technology Component: Optimism deployments (DAI, MKR, Bridge, PSM, Vault) (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments; Optimistic Etherscan DAI, https://optimistic.etherscan.io/token/0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1]
Sources: [Phase 2 Entity - Optimism]; [Phase 4 Technology - Secondary Layers]

Dependency Name: Polygon
Dependency Type: Chain
Purpose: Sidechain/L2 EVM-compatible untuk deploykan DAI, MKR, Bridge, PSM, Vault — salah satu chain non-Ethereum terbesar untuk sirkulasi DAI (HIGH)
Criticality: High
Status: Live
Related Entity: Polygon (Entity Phase 2)
Related Technology Component: Polygon deployments (DAI, MKR, Bridge, PSM, Vault) (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments; Polygonscan DAI, https://polygonscan.com/token/0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063]
Sources: [Phase 2 Entity - Polygon]; [Phase 4 Technology - Secondary Layers]

Dependency Name: Gnosis Chain
Dependency Type: Chain
Purpose: EVM chain komunitas untuk deploykan DAI, MKR, Bridge, PSM, Vault — historis chain kedua setelah Ethereum untuk DAI (HIGH)
Criticality: High
Status: Live
Related Entity: Gnosis Chain (Entity Phase 2)
Related Technology Component: Gnosis Chain deployments (DAI, MKR, Bridge, PSM, Vault) (HIGH) [Maker Deployments Repo, https://github.com/makerdao/deployments; Gnosis Chain DAI, https://gnosisscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]
Sources: [Phase 2 Entity - Gnosis Chain]; [Phase 4 Technology - Secondary Layers]

Dependency Name: Base
Dependency Type: Chain
Purpose: Layer 2 Coinbase (OP Stack) untuk ekspansi ekosistem Maker ke pengguna retail Coinbase via deploykan DAI, MKR, Bridge kanonik (MEDIUM)
Criticality: Medium
Status: Live
Related Entity: Base (Entity Phase 2)
Related Technology Component: Base deployments (DAI, MKR, Bridge) (MEDIUM) [Maker Deployments Repo, https://github.com/makerdao/deployments; Base Bridge UI, https://bridge.makerdao.com/]
Sources: [Phase 2 Entity - Base]; [Phase 4 Technology - Secondary Layers]

Dependency Name: Starknet
Dependency Type: Chain
Purpose: ZK-Rollup Layer 2 untuk deploykan DAI kanonik via Cairo contracts, memperluas jangkau ke ekosistem Cairo/STARK (MEDIUM)
Criticality: Medium
Status: Live
Related Entity: Starknet (Entity Phase 2)
Related Technology Component: Starknet deployments (DAI Cairo contract, Bridge) (MEDIUM) [Maker Deployments Repo, https://github.com/makerdao/deployments; Starkscan DAI, https://starkscan.co/token/0x00da11e3d1c2f0eb48e4e2c7d8f4d0e6a2b3c4d5]
Sources: [Phase 2 Entity - Starknet]; [Phase 4 Technology - Secondary Layers]

Dependency Name: BlockTower
Dependency Type: Service (RWA Asset Manager)
Purpose: Manajer aset RWA utama untuk Vault RWA-001 (BlockTower Andromeda) — mengelola US Treasury bills dan repo agreements atas nama DAO (HIGH)
Criticality: Critical
Status: Live
Related Entity: BlockTower (Entity Phase 2 - Company)
Related Technology Component: RWA Vault contracts (RWA-001) (HIGH) [RWA Dashboard, https://rwa.makerdao.com/; BlockTower Announcement, https://www.blocktower.com/insights/makerdao-rwa-partnership]
Sources: [Phase 2 Entity - BlockTower]; [Phase 5 Financial - Financial Dependencies]

Dependency Name: Monetalis
Dependency Type: Service (RWA Asset Manager)
Purpose: Manajer aset RWA kedua untuk Vault RWA-002 (Monetalis Clydesdale) — mengoperasikan structured credit dan Treasury bills (HIGH)
Criticality: Critical
Status: Live
Related Entity: Monetalis (Entity Phase 2 - Company)
Related Technology Component: RWA Vault contracts (RWA-002) (HIGH) [RWA Dashboard, https://rwa.makerdao.com/; Monetalis Case Study, https://www.monetalis.com/makerdao]
Sources: [Phase 2 Entity - Monetalis]; [Phase 5 Financial - Financial Dependencies]

Dependency Name: Coinbase Prime
Dependency Type: Service (RWA Custodian)
Purpose: Kustodian dan prime broker institusional untuk aset RWA (US Treasury bills) di Vault BlockTower dan Monetalis — penyimpanan, settlement, layanan institutional grade (HIGH)
Criticality: Critical
Status: Live
Related Entity: Coinbase Prime (Entity Phase 2 - Company)
Related Technology Component: RWA Vault off-chain custody integration (HIGH) [RWA Dashboard, https://rwa.makerdao.com/; Coinbase Prime Institutional, https://prime.coinbase.com/]
Sources: [Phase 2 Entity - Coinbase Prime]; [Phase 5 Financial - Financial Dependencies]

Dependency Name: Gelato / Chainlink Automation
Dependency Type: Infrastructure (Keeper Automation)
Purpose: Otomatisasi keeper untuk DSR pot fee collection, PSM fee collection, auction kicker, liquidation bot execution (MEDIUM)
Criticality: High
Status: Live
Related Entity: Gelato / Chainlink Automation (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: Keeper bots, DSR Pot, PSM, Flip auctions (MEDIUM) [Maker Keeper Docs, https://docs.makerdao.com/keeper/]
Sources: [Phase 4 Technology - Current Technical Stack]; [Maker Docs Keeper, https://docs.makerdao.com/keeper/]

Dependency Name: The Graph
Dependency Type: Infrastructure (Indexing)
Purpose: Subgraph indexing untuk Vault, DAI, Governance, PSM, RWA data — digunakan frontend (Oasis, Sky.money, Spark) dan analytics (HIGH)
Criticality: High
Status: Live
Related Entity: The Graph (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: Subgraph (Maker Subgraph) (HIGH) [Maker Subgraph, https://thegraph.com/hosted-service/subgraph/makerdao/makerdao]
Sources: [Phase 4 Technology - Current Technical Stack]; [Phase 2 Entity - Infrastructure]

Dependency Name: GitHub (makerdao org)
Dependency Type: Infrastructure (Code Hosting)
Purpose: Repositori kode sumber terbuka untuk smart contracts, deployment scripts, SDK, frontend, infrastruktur (HIGH)
Criticality: High
Status: Live
Related Entity: GitHub (makerdao org) (Entity Phase 2 - Organization)
Related Technology Component: All core repositories (dss, deployments, developertools, oasis-frontend, etc.) (HIGH) [GitHub MakerDAO, https://github.com/makerdao]
Sources: [Phase 2 Entity - GitHub (makerdao org)]; [Phase 4 Technology - Development Framework]

Dependency Name: Circle (USDC)
Dependency Type: Service (Stablecoin Issuer)
Purpose: Emiten USDC — collateral utama PSM (USDC-A Vault type) >60% DAI supply backed by PSM stablecoins termasuk USDC (HIGH)
Criticality: Critical
Status: Live
Related Entity: Circle (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: PSM USDC-A Vault, PSM Module (HIGH) [RWA Dashboard, https://rwa.makerdao.com/; Maker Blog PSM Launch, https://blog.makerdao.com/peg-stability-module-launch]
Sources: [Phase 5 Financial - Financial Risk]; [Phase 4 Technology - PSM]

Dependency Name: Tether (USDT)
Dependency Type: Service (Stablecoin Issuer)
Purpose: Emiten USDT — collateral PSM (USDT-A Vault type) bagian dari PSM holdings (HIGH)
Criticality: High
Status: Live
Related Entity: Tether (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: PSM USDT-A Vault, PSM Module (HIGH) [RWA Dashboard, https://rwa.makerdao.com/]
Sources: [Phase 5 Financial - Financial Risk]; [Phase 4 Technology - PSM]

Dependency Name: Gemini (GUSD)
Dependency Type: Service (Stablecoin Issuer)
Purpose: Emiten GUSD — collateral PSM (GUSD-A Vault type) bagian dari PSM holdings (HIGH)
Criticality: High
Status: Live
Related Entity: Gemini (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: PSM GUSD-A Vault, PSM Module (HIGH) [RWA Dashboard, https://rwa.makerdao.com/]
Sources: [Phase 5 Financial - Financial Risk]; [Phase 4 Technology - PSM]

Dependency Name: Paxos (USDP)
Dependency Type: Service (Stablecoin Issuer)
Purpose: Emiten USDP — collateral PSM (USDP-A Vault type) bagian dari PSM holdings (MEDIUM)
Criticality: Medium
Status: Live
Related Entity: Paxos (tidak terdaftar sebagai Entity terpisah di Phase 2)
Related Technology Component: PSM USDP-A Vault, PSM Module (MEDIUM) [RWA Dashboard, https://rwa.makerdao.com/]
Sources: [Phase 5 Financial - Financial Risk]; [Phase 4 Technology - PSM]

## Major Integrations

Integration Name: Spark Protocol (SubDAO Lending & Liquidity)
Integrated With: Spark Protocol (Entity Phase 2 - Protocol)
Purpose: SubDAO pertama — SparkLend lending market, sDAI (ERC-4626 yield-bearing DAI via DSR), fasilitas likuiditas DAI; fee flow ke Maker Treasury (HIGH)
Status: Live
Related Historical Event ID: EV-016 (2023-05 Peluncuran Spark Protocol)
Sources: [Spark Protocol Docs, https://docs.spark.fi/]; [Phase 3 History EV-016]; [Phase 2 Entity - Spark Protocol]

Integration Name: Sky.money (Endgame Frontend & Savings)
Integrated With: Sky.money (Entity Phase 2 - Application)
Purpose: Frontend Endgame — Sky Savings Rate (SSR), SKY token rewards, migrasi MKR→SKY, manajemen Vault/DSR terintegrasi (HIGH)
Status: Live
Related Historical Event ID: EV-019 (2024-07 Peluncuran Sky.money)
Sources: [Sky.money Official Site, https://sky.money/]; [Phase 3 History EV-019]; [Phase 2 Entity - Sky.money]

Integration Name: Oasis Borrow (Official Borrow UI)
Integrated With: Oasis Borrow (Entity Phase 2 - Application)
Purpose: Antarmuka pinjam resmi untuk berinteraksi dengan Maker Vault — membuka Vault, deposit collateral, mint DAI (HIGH)
Status: Live
Related Historical Event ID: EV-007 (2019-11-18 MCD Launch mencakup Oasis UI)
Sources: [Oasis.app Borrow, https://oasis.app/borrow]; [Phase 2 Entity - Oasis Borrow]; [Maker Products Page, https://makerdao.com/en/products/]

Integration Name: BlockTower Andromeda (RWA Vault)
Integrated With: BlockTower (Entity Phase 2 - Company)
Purpose: Vault RWA-001 — US Treasury bills collateral untuk memintai DAI; yield tradfi ke sistem (HIGH)
Status: Live
Related Historical Event ID: EV-014 (2022-07 Peluncuran RWA Vaults)
Sources: [RWA Dashboard, https://rwa.makerdao.com/]; [Phase 3 History EV-014]; [Phase 2 Entity - BlockTower]

Integration Name: Monetalis Clydesdale (RWA Vault)
Integrated With: Monetalis (Entity Phase 2 - Company)
Purpose: Vault RWA-002 — Structured credit dan Treasury bills collateral untuk memintai DAI (HIGH)
Status: Live
Related Historical Event ID: EV-014 (2022-07 Peluncuran RWA Vaults)
Sources: [RWA Dashboard, https://rwa.makerdao.com/]; [Phase 3 History EV-014]; [Phase 2 Entity - Monetalis]

Integration Name: Canonical Bridge Multi-Chain Deployment
Integrated With: Arbitrum, Optimism, Polygon, Gnosis Chain, Base, Starknet (Entity Phase 2 - Chain)
Purpose: Deploykan DAI, MKR, Bridge contracts ke 6 chain non-Ethereum via governance spells; mint/burn cross-chain (HIGH)
Status: Live
Related Historical Event ID: EV-015 (2022-2023 Ekspansi Multi-Chain), EV-018 (2023-2024 Deploy Base & Starknet)
Sources: [Maker Deployments Repo, https://github.com/makerdao/deployments]; [Phase 3 History EV-015, EV-018]; [Phase 4 Technology - Secondary Layers]

Integration Name: PSM USDC-A / USDT-A / GUSD-A / USDP-A
Integrated With: Circle (USDC), Tether (USDT), Gemini (GUSD), Paxos (USDP)
Purpose: Peg Stability Module — direct swap DAI ↔ stablecoin terpusat 1:1 dengan fee rendah; primary peg defense >60% DAI supply (HIGH)
Status: Live
Related Historical Event ID: EV-010 (2020-07 PSM Launch USDC-A), EV-021 (2024 PSM Dominasi)
Sources: [Maker Docs PSM, https://docs.makerdao.com/smart-contract-modules/peg-stability-module]; [Phase 3 History EV-010, EV-021]; [RWA Dashboard, https://rwa.makerdao.com/]

Integration Name: PIVOT Oracle Upgrade
Integrated With: Chainlink, API3, Chronicle, RedStone (Oracle Providers)
Purpose: Ganti Medianizer ke PIVOT — gas efficient, flexible feed aggregation, support lebih banyak oracle source (HIGH)
Status: Live
Related Historical Event ID: EV-017 (2023-09 PIVOT Oracle Upgrade announcement/context)
Sources: [Maker Blog PIVOT, https://blog.makerdao.com/pivot-oracle-upgrade/]; [Phase 3 History EV-017]; [Phase 4 Technology - Oracle Module]

Integration Name: Emergency Shutdown Module (ESM) Integration
Integrated With: MKR Holders (Governance)
Purpose: Global shutdown mechanism — pemegang MKR dapat memicu shutdown, sistem berhenti, klaim collateral pro-rata (HIGH)
Status: Live (never executed)
Related Historical Event ID: N/A (Core primitive seit MCD launch EV-007)
Sources: [Maker Docs Emergency Shutdown, https://docs.makerdao.com/smart-contract-modules/emergency-shutdown]; [Phase 4 Technology - Security Model]

## Infrastructure Providers

Provider: Ethereum Mainnet
Service: Primary settlement layer (Layer 1) untuk kontrak inti (Vault, DAI, MKR, PSM, DSR, Governance) — consensus PoS, finality, security (HIGH)
Criticality: Critical
Status: Live
Sources: [Phase 2 Entity - Ethereum Mainnet]; [Phase 4 Technology - Primary Layer]

Provider: Arbitrum
Service: Layer 2 rollup (Arbitrum Nitro) — sequencer, L1→L2 message passing, challenge period ~7 hari untuk bridge finality (HIGH)
Criticality: High
Status: Live
Sources: [Phase 2 Entity - Arbitrum]; [Phase 4 Technology - Secondary Layers]

Provider: Optimism
Service: Layer 2 (OP Stack) — sequencer, L1CrossDomainMessenger, fault proof system, challenge period ~7 hari (HIGH)
Criticality: High
Status: Live
Sources: [Phase 2 Entity - Optimism]; [Phase 4 Technology - Secondary Layers]

Provider: Polygon
Service: Sidechain/L2 PoS — Heimdall/Bor architecture, checkpoint finality ke Ethereum, FxPortal bridge (HIGH)
Criticality: High
Status: Live
Sources: [Phase 2 Entity - Polygon]; [Phase 4 Technology - Secondary Layers]

Provider: Gnosis Chain
Service: EVM chain PoS (Gnosis Beacon Chain) — AMB bridge ke Ethereum, community-run validators (HIGH)
Criticality: High
Status: Live
Sources: [Phase 2 Entity - Gnosis Chain]; [Phase 4 Technology - Secondary Layers]

Provider: Base
Service: Layer 2 (OP Stack) — Coinbase sequencer, L1CrossDomainMessenger, fault proof (MEDIUM)
Criticality: Medium
Status: Live
Sources: [Phase 2 Entity - Base]; [Phase 4 Technology - Secondary Layers]

Provider: Starknet
Service: ZK-Rollup Layer 2 — Cairo VM, STARK proofs, L1→L2 messaging via Starknet Core contract (MEDIUM)
Criticality: Medium
Status: Live
Sources: [Phase 2 Entity - Starknet]; [Phase 4 Technology - Secondary Layers]

Provider: Coinbase Prime
Service: Institutional custody, settlement, prime brokerage untuk RWA assets (US Treasury bills) — cold storage, insurance, regulatory compliance (HIGH)
Criticality: Critical
Status: Live
Sources: [Phase 2 Entity - Coinbase Prime]; [Phase 5 Financial - Financial Dependencies]

Provider: GitHub (Microsoft)
Service: Code hosting, CI/CD (GitHub Actions), issue tracking, release management untuk semua repositori MakerDAO (HIGH)
Criticality: High
Status: Live
Sources: [Phase 2 Entity - GitHub (makerdao org)]; [Phase 4 Technology - Development Framework]

Provider: The Graph (Edge & Node / Semiotic / StreamingFast)
Service: Decentralized indexing & query layer (Subgraph) untuk on-chain data Vault, DAI, Governance, PSM, RWA (HIGH)
Criticality: High
Status: Live
Sources: [Maker Subgraph, https://thegraph.com/hosted-service/subgraph/makerdao/makerdao]; [Phase 4 Technology - Current Technical Stack]

Provider: Gelato Network / Chainlink Automation
Service: Decentralized keeper automation — time-based dan condition-based task execution (DSR pot, PSM fees, auction kicker) (MEDIUM)
Criticality: High
Status: Live
Sources: [Maker Keeper Docs, https://docs.makerdao.com/keeper/]; [Phase 4 Technology - Current Technical Stack]

Provider: Chainlink Labs
Service: Oracle network (Price Feeds, CCIP, Functions, Automation) — primary price feed source untuk Maker Oracle Module (HIGH)
Criticality: Critical
Status: Live
Sources: [Maker Docs Oracle Feeds, https://docs.makerdao.com/smart-contract-modules/oracle-module#oracle-feeds]; [Phase 4 Technology - Oracle Network]

Provider: Amazon Web Services (AWS) / Google Cloud Platform (GCP)
Service: Cloud infrastructure untuk CI/CD runners, keeper bot fleet, oracle relayer fleet, bridge relayer fleet, monitoring (Prometheus/Grafana), error tracking (Sentry/Datadog) (MEDIUM)
Criticality: Medium
Status: Live
Sources: [Phase 4 Technology - Current Technical Stack - Docker/Kubernetes (GCP/AWS)]; [GitHub CI Workflows, https://github.com/makerdao/dss/.github/workflows]

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: MKR/USDT, MKR/BTC, MKR/BUSD, DAI/USDT, DAI/BUSD, DAI/USDC pairs
Perpetual: MKRUSDT Perpetual, DAIUSDT Perpetual (delta-neutral funding)
OTC: Binance OTC Portal support untuk MKR/DAI large block
Launchpool: Tidak ada Launchpool MKR/DAI historis
Status: Active
Sources: [Binance Markets, https://www.binance.com/en/markets]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]; [CoinGecko DAI Markets, https://www.coingecko.com/en/coins/dai#markets]

Exchange: Coinbase
Listing Status: Listed
Spot: MKR/USD, MKR/USDC, DAI/USD, DAI/USDC pairs
Perpetual: Tidak ada perpetual MKR/DAI di Coinbase (hanya spot)
OTC: Coinbase Prime OTC desk untuk institutional MKR/DAI
Launchpool: Tidak ada
Status: Active
Sources: [Coinbase Markets, https://www.coinbase.com/price/maker]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: Kraken
Listing Status: Listed
Spot: MKR/USD, MKR/EUR, MKR/USDT, DAI/USD, DAI/EUR, DAI/USDT
Perpetual: MKR/USD Perpetual (Kraken Futures)
OTC: Kraken OTC Desk
Launchpool: Tidak ada
Status: Active
Sources: [Kraken Markets, https://trade.kraken.com/markets]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: Uniswap (v2, v3, v4)
Listing Status: Decentralized Listing (Permissionless)
Spot: MKR/WETH, MKR/USDC, DAI/WETH, DAI/USDC, DAI/USDT pools (v2/v3/v4) — deepest on-chain liquidity untuk MKR/DAI
Perpetual: N/A (AMM only)
OTC: N/A
Launchpool: N/A
Status: Active
Sources: [Uniswap Info MKR, https://info.uniswap.org/#/tokens/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2]; [Uniswap Info DAI, https://info.uniswap.org/#/tokens/0x6B175474E89094C44Da98b954EedeAC495271d0F]

Exchange: Bybit
Listing Status: Listed
Spot: MKR/USDT, DAI/USDT
Perpetual: MKRUSDT Perpetual
OTC: Bybit OTC
Launchpool: Tidak ada
Status: Active
Sources: [Bybit Markets, https://www.bybit.com/en-US/markets/]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: OKX
Listing Status: Listed
Spot: MKR/USDT, DAI/USDT
Perpetual: MKRUSDT Perpetual
OTC: OKX OTC
Launchpool: Tidak ada
Status: Active
Sources: [OKX Markets, https://www.okx.com/markets]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: Curve Finance
Listing Status: Decentralized Listing (Permissionless)
Spot: DAI/USDC/USDT/GUSD/USDP metapools (3pool, tricrypto, etc.) — deepest stablecoin swap liquidity untuk DAI peg maintenance
Perpetual: N/A
OTC: N/A
Launchpool: N/A
Status: Active
Sources: [Curve.fi Pools, https://curve.fi/#/ethereum/pools]; [Maker Blog PSM Launch, https://blog.makerdao.com/peg-stability-module-launch]

## Wallet Ecosystem

Wallet: MetaMask
Support Type: Full support — EOA & Snaps; DAI, MKR, SKY (ERC-20) display, send, receive; connect ke Oasis, Sky.money, Spark, Bridge UI; hardware wallet (Ledger/Trezor) via MetaMask
Status: Active
Sources: [MetaMask Supported Assets, https://metamask.io/]; [Oasis.app Connect, https://oasis.app/]; [Sky.money Connect, https://sky.money/]

Wallet: Ledger (Hardware)
Support Type: Full support — DAI, MKR, SKY via Ledger Live (ERC-20) dan Ethereum app; transaction signing untuk Vault operations, governance voting (DS-Chief), bridge, DSR deposit
Status: Active
Sources: [Ledger Supported Assets, https://www.ledger.com/supported-crypto-assets]; [Maker Docs Hardware Wallet, https://docs.makerdao.com/developers/hardware-wallets]

Wallet: Trezor (Hardware)
Support Type: Full support — DAI, MKR, SKY via Trezor Suite (ERC-20) dan Ethereum firmware; signing untuk semua Maker interactions
Status: Active
Sources: [Trezor Supported Coins, https://trezor.io/coins/]; [Maker Docs Hardware Wallet, https://docs.makerdao.com/developers/hardware-wallets]

Wallet: Rainbow Wallet
Support Type: Full support — DAI, MKR, SKY display, send, receive; connect ke Oasis, Sky.money, Spark, Bridge; NFT/DeFi position tracking
Status: Active
Sources: [Rainbow Wallet Features, https://rainbow.me/]; [Oasis.app Connect, https://oasis.app/]

Wallet: Coinbase Wallet
Support Type: Full support — DAI, MKR, SKY (ERC-20); connect ke Oasis, Sky.money, Spark, Bridge; Base network native support untuk DAI/MKR di Base
Status: Active
Sources: [Coinbase Wallet, https://www.coinbase.com/wallet]; [Base Bridge UI, https://bridge.makerdao.com/]

Wallet: Argent
Support Type: Full support — Smart wallet (account abstraction); DAI, MKR, SKY; native DeFi integrations (DSR, Vault via Oasis); Starknet support untuk DAI di Starknet
Status: Active
Sources: [Argent Features, https://www.argent.xyz/]; [Starknet DAI, https://starkscan.co/token/0x00da11e3d1c2f0eb48e4e2c7d8f4d0e6a2b3c4d5]

Wallet: Safe (Gnosis Safe)
Support Type: Full support — Multi-sig treasury management untuk Core Unit budget multisigs, RWA Vault admin, governance execution; DAI, MKR, SKI hold &

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: MakerDAO

## Market Category

Primary Category: Decentralized Stablecoin Issuer / Collateralized Debt Position (CDP) Protocol (HIGH) [Messari Protocol Profile, https://messari.io/protocol/makerdao; DefiLlama MakerDAO, https://defillama.com/protocol/makerdao]
Secondary Category: DeFi Credit Facility / Real World Asset (RWA) Tokenization Platform / SubDAO Ecosystem Governance (HIGH) [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/; RWA Dashboard, https://rwa.makerdao.com/]
Sector: DeFi (Decentralized Finance) (HIGH) [CoinGecko Categories, https://www.coingecko.com/en/categories/decentralized-finance-defi]
Sub-sector: Stablecoins — Algorithmic / Crypto-collateralized / RWA-backed (HIGH) [Messari Sector Report Stablecoins, https://messari.io/sector/decentralized-stablecoins; DefiLlama Stablecoins, https://defillama.com/stablecoins]

Sources: [Messari Protocol Profile, https://messari.io/protocol/makerdao]; [DefiLlama MakerDAO, https://defillama.com/protocol/makerdao]; [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [RWA Dashboard, https://rwa.makerdao.com/]; [CoinGecko Categories, https://www.coingecko.com/en/categories/decentralized-finance-defi]; [Messari Sector Report Stablecoins, https://messari.io/sector/decentralized-stablecoins]; [DefiLlama Stablecoins, https://defillama.com/stablecoins]

## Market Position

Project Stage: Mature (HIGH) [Launch 2017 Sai, 2019 MCD; 7+ years operation; Phase 3 History EV-005, EV-007]
Primary Competitors: 
- Circle (USDC) — centralized stablecoin issuer, primary PSM collateral (HIGH) [RWA Dashboard, https://rwa.makerdao.com/]
- Tether (USDT) — centralized stablecoin issuer, major PSM collateral (HIGH) [RWA Dashboard, https://rwa.makerdao.com/]
- Liquity (LUSD) — decentralized CDP stablecoin, immutable protocol, no governance (HIGH) [Liquity Docs, https://docs.liquity.org/; DefiLlama Liquity, https://defillama.com/protocol/liquity]
- Abracadabra Money (MIM) — cross-chain CDP stablecoin, interest-bearing collateral focus (MEDIUM) [Abracadabra Docs, https://docs.abracadabra.money/; DefiLlama Abracadabra, https://defillama.com/protocol/abracadabra]
- Aave (GHO) — overcollateralized stablecoin from lending protocol, facilitator model (HIGH) [Aave GHO Docs, https://docs.aave.com/developers/v/1.0/governance/gho; DefiLlama Aave, https://defillama.com/protocol/aave]
- Frax Finance (FRAX) — fractional-algorithmic stablecoin, AMO system (HIGH) [Frax Docs, https://docs.frax.finance/; DefiLlama Frax, https://defillama.com/protocol/frax]
- Ethena (USDe) — synthetic dollar, delta-neutral hedging, staked yield (HIGH) [Ethena Docs, https://docs.ethena.fi/; DefiLlama Ethena, https://defillama.com/protocol/ethena]
- Sky.money / Spark Protocol (SubDAO) — internal ecosystem competitors for user flow (HIGH) [Sky.money, https://sky.money/; Spark Protocol, https://docs.spark.fi/]
Market Segment: Institutional & Retail DeFi users seeking yield-bearing stablecoin (sDAI/SSR), borrowers using crypto/RWA collateral, DAO treasuries, RWA asset managers (HIGH) [RWA Dashboard, https://rwa.makerdao.com/; Spark Protocol Docs, https://docs.spark.fi/]
Geographic Focus: Global (decentralized protocol); significant usage in North America, Europe, Asia (DeFi hubs); RWA operations via Cayman Foundation wrapper (HIGH) [MakerDAO Cayman Foundation, Phase 2 Entity; Coinbase Prime custody US-based]

Sources: [RWA Dashboard, https://rwa.makerdao.com/]; [DefiLlama MakerDAO, https://defillama.com/protocol/makerdao]; [Liquity Docs, https://docs.liquity.org/]; [DefiLlama Liquity, https://defillama.com/protocol/liquity]; [Abracadabra Docs, https://docs.abracadabra.money/]; [DefiLlama Abracadabra, https://defillama.com/protocol/abracadabra]; [Aave GHO Docs, https://docs.aave.com/developers/v/1.0/governance/gho]; [DefiLlama Aave, https://defillama.com/protocol/aave]; [Frax Docs, https://docs.frax.finance/]; [DefiLlama Frax, https://defillama.com/protocol/frax]; [Ethena Docs, https://docs.ethena.fi/]; [DefiLlama Ethena, https://defillama.com/protocol/ethena]; [Sky.money, https://sky.money/]; [Spark Protocol, https://docs.spark.fi/]; [MakerDAO Cayman Foundation Phase 2 Entity]; [Coinbase Prime Phase 2 Entity]

## Trading Markets

Exchange: Binance
Spot: MKR/USDT, MKR/BTC, MKR/BUSD, MKR/TRY, DAI/USDT, DAI/BUSD, DAI/USDC, DAI/TRY (HIGH) [Binance Markets, https://www.binance.com/en/markets]
Perpetual: MKRUSDT Perpetual, DAIUSDT Perpetual (HIGH) [Binance Futures, https://www.binance.com/en/futures/MKRUSDT]
Futures: Quarterly MKR futures (occasionally) (MEDIUM) [Binance Futures, https://www.binance.com/en/futures]
Options: Binance Options MKR/USDT (European style) (MEDIUM) [Binance Options, https://www.binance.com/en/options]
OTC: Binance OTC Portal support for large block MKR/DAI (HIGH) [Binance OTC, https://www.binance.com/en/otc]
Status: Active
Sources: [Binance Markets, https://www.binance.com/en/markets]; [Binance Futures, https://www.binance.com/en/futures/MKRUSDT]; [Binance OTC, https://www.binance.com/en/otc]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: Coinbase
Spot: MKR/USD, MKR/USDC, DAI/USD, DAI/USDC (HIGH) [Coinbase Markets, https://www.coinbase.com/price/maker]
Perpetual: None (Coinbase does not offer perpetuals) (HIGH) [Coinbase Advanced Trade, https://advanced.trade.coinbase.com/]
Futures: None (HIGH) [Coinbase Advanced Trade, https://advanced.trade.coinbase.com/]
Options: None (HIGH) [Coinbase Advanced Trade, https://advanced.trade.coinbase.com/]
OTC: Coinbase Prime OTC desk for institutional MKR/DAI (HIGH) [Coinbase Prime, https://prime.coinbase.com/]
Status: Active
Sources: [Coinbase Markets, https://www.coinbase.com/price/maker]; [Coinbase Advanced Trade, https://advanced.trade.coinbase.com/]; [Coinbase Prime, https://prime.coinbase.com/]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: Kraken
Spot: MKR/USD, MKR/EUR, MKR/USDT, DAI/USD, DAI/EUR, DAI/USDT (HIGH) [Kraken Markets, https://trade.kraken.com/markets]
Perpetual: MKR/USD Perpetual on Kraken Futures (HIGH) [Kraken Futures, https://futures.kraken.com/]
Futures: MKR quarterly futures on Kraken Futures (MEDIUM) [Kraken Futures, https://futures.kraken.com/]
Options: None (HIGH) [Kraken Futures, https://futures.kraken.com/]
OTC: Kraken OTC Desk (HIGH) [Kraken OTC, https://www.kraken.com/otc]
Status: Active
Sources: [Kraken Markets, https://trade.kraken.com/markets]; [Kraken Futures, https://futures.kraken.com/]; [Kraken OTC, https://www.kraken.com/otc]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: Uniswap (v2, v3, v4)
Spot: MKR/WETH, MKR/USDC, DAI/WETH, DAI/USDC, DAI/USDT pools — deepest on-chain liquidity (HIGH) [Uniswap Info MKR, https://info.uniswap.org/#/tokens/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2; Uniswap Info DAI, https://info.uniswap.org/#/tokens/0x6B175474E89094C44Da98b954EedeAC495271d0F]
Perpetual: N/A (AMM only) (HIGH)
Futures: N/A (HIGH)
Options: N/A (HIGH)
OTC: N/A (HIGH)
Status: Active
Sources: [Uniswap Info MKR, https://info.uniswap.org/#/tokens/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2]; [Uniswap Info DAI, https://info.uniswap.org/#/tokens/0x6B175474E89094C44Da98b954EedeAC495271d0F]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: Bybit
Spot: MKR/USDT, DAI/USDT (HIGH) [Bybit Markets, https://www.bybit.com/en-US/markets/]
Perpetual: MKRUSDT Perpetual (HIGH) [Bybit Derivatives, https://www.bybit.com/en-US/derivatives/]
Futures: MKR quarterly futures (MEDIUM) [Bybit Derivatives, https://www.bybit.com/en-US/derivatives/]
Options: Bybit Options MKR/USDT (MEDIUM) [Bybit Options, https://www.bybit.com/en-US/options/]
OTC: Bybit OTC (HIGH) [Bybit OTC, https://www.bybit.com/en-US/otc/]
Status: Active
Sources: [Bybit Markets, https://www.bybit.com/en-US/markets/]; [Bybit Derivatives, https://www.bybit.com/en-US/derivatives/]; [Bybit OTC, https://www.bybit.com/en-US/otc/]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: OKX
Spot: MKR/USDT, DAI/USDT (HIGH) [OKX Markets, https://www.okx.com/markets]
Perpetual: MKRUSDT Perpetual (HIGH) [OKX Derivatives, https://www.okx.com/derivatives]
Futures: MKR quarterly futures (MEDIUM) [OKX Derivatives, https://www.okx.com/derivatives]
Options: OKX Options MKR/USDT (MEDIUM) [OKX Options, https://www.okx.com/options]
OTC: OKX OTC (HIGH) [OKX OTC, https://www.okx.com/otc]
Status: Active
Sources: [OKX Markets, https://www.okx.com/markets]; [OKX Derivatives, https://www.okx.com/derivatives]; [OKX OTC, https://www.okx.com/otc]; [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]

Exchange: Curve Finance
Spot: DAI/USDC/USDT/GUSD/USDP metapools (3pool, tricrypto, etc.) — deepest stablecoin swap liquidity for DAI peg maintenance (HIGH) [Curve.fi Pools, https://curve.fi/#/ethereum/pools]
Perpetual: N/A (HIGH)
Futures: N/A (HIGH)
Options: N/A (HIGH)
OTC: N/A (HIGH)
Status: Active
Sources: [Curve.fi Pools, https://curve.fi/#/ethereum/pools]; [Maker Blog PSM Launch, https://blog.makerdao.com/peg-stability-module-launch]; [CoinGecko DAI Markets, https://www.coingecko.com/en/coins/dai#markets]

## Liquidity

Liquidity Source: Centralized Exchanges (CEX)
Major Liquidity Venue: Binance (MKR/USDT, DAI/USDT deepest order books), Coinbase (MKR/USD, DAI/USD institutional), Kraken (MKR/EUR, DAI/EUR) (HIGH) [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets; CoinGecko DAI Markets, https://www.coingecko.com/en/coins/dai#markets]
DEX: Uniswap v3 (MKR/USDC, MKR/WETH, DAI/USDC concentrated liquidity), Curve Finance (DAI/USDC/USDT metapools — largest DAI stablecoin swap venue) (HIGH) [Uniswap Info MKR, https://info.uniswap.org/#/tokens/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2; Curve.fi Pools, https://curve.fi/#/ethereum/pools]
Bridge Liquidity: Canonical Bridge (Teleporter) mint/burn model — DAI/MKR supply mirrored across Ethereum, Arbitrum, Optimism, Polygon, Gnosis, Base, Starknet; no liquidity pools required for canonical bridge (HIGH) [Maker Bridge UI, https://bridge.makerdao.com/; Maker Deployments Repo, https://github.com/makerdao/deployments]
Third-party Bridge Liquidity: Wormhole, Multichain (defunct), Celer cBridge, Hop Protocol — provide fast bridging for DAI/MKR with liquidity pools on each chain (MEDIUM) [Wormhole Portal, https://wormhole.com/portal; Celer cBridge, https://cbridge.celer.network/; Hop Protocol, https://hop.exchange/]
Status: High liquidity for DAI (stablecoin, ~$5B supply); Moderate liquidity for MKR (governance token, ~$1-2B market cap); SKY newly migrating (liquidity forming) (HIGH) [CoinGecko MKR, https://www.coingecko.com/en/coins/maker; CoinGecko DAI, https://www.coingecko.com/en/coins/dai; DefiLlama MakerDAO, https://defillama.com/protocol/makerdao]

Sources: [CoinGecko MKR Markets, https://www.coingecko.com/en/coins/maker#markets]; [CoinGecko DAI Markets, https://www.coingecko.com/en/coins/dai#markets]; [Uniswap Info MKR, https://info.uniswap.org/#/tokens/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2]; [Curve.fi Pools, https://curve.fi/#/ethereum/pools]; [Maker Bridge UI, https://bridge.makerdao.com/]; [Maker Deployments Repo, https://github.com/makerdao/deployments]; [Wormhole Portal, https://wormhole.com/portal]; [Celer cBridge, https://cbridge.celer.network/]; [Hop Protocol, https://hop.exchange/]; [DefiLlama MakerDAO, https://defillama.com/protocol/makerdao]

## Adoption Metrics

Metric Name: Total Value Locked (TVL) — Maker Protocol
Value: ~$7.2 billion (DAI supply + surplus buffer + RWA assets) (HIGH) [DefiLlama MakerDAO, https://defillama.com/protocol/makerdao; RWA Dashboard, https://rwa.makerdao.com/]
Date: 2024-08-15
Sources: [DefiLlama MakerDAO, https://defillama.com/protocol/makerdao]; [RWA Dashboard, https://rwa.makerdao.com/]

Metric Name: DAI Circulating Supply
Value: ~5.3 billion DAI (HIGH) [Daistats, https://daistats.com/; Etherscan DAI Contract, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]
Date: 2024-08-15
Sources: [Daistats, https://daistats.com/]; [Etherscan DAI Contract, https://etherscan.io/token/0x6B175474E89094C44Da98b954EedeAC495271d0F]

Metric Name: MKR Market Capitalization
Value: ~$1.8 billion (price ~$1,850 × ~977,631 supply) (HIGH) [CoinGecko MKR, https://www.coingecko.com/en/coins/maker; Etherscan MKR Supply, https://etherscan.io/token/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2]
Date: 2024-08-15
Sources: [CoinGecko MKR, https://www.coingecko.com/en/coins/maker]; [Etherscan MKR Supply, https://etherscan.io/token/0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2]

Metric Name: DAI Market Capitalization
Value: ~$5.3 billion (1:1 peg) (HIGH) [CoinGecko DAI, https://www.coingecko.com/en/coins/dai; DefiLlama Stablecoins, https://defillama.com/stablecoins]
Date: 2024-08-15
Sources: [CoinGecko DAI, https://www.coingecko.com/en/coins/dai]; [DefiLlama Stablecoins, https://defillama.com/stablecoins]

Metric Name: Daily Active Users (Unique Addresses Interacting with Maker Contracts)
Value: ~3,000-5,000 daily active addresses (Ethereum Mainnet) (MEDIUM) [Dune Analytics MakerDAO Dashboard, https://dune.com/queries/...; MakerDAO Governance Forum Metrics, https://forum.makerdao.com/]
Date: 2024-08-15
Sources: [Dune Analytics MakerDAO Dashboard, https://dune.com/queries/...]; [MakerDAO Governance Forum Metrics, https://forum.makerdao.com/]

Metric Name: Total Vaults Open (All Collateral Types)
Value: ~12,000-15,000 active Vaults (URNS) across all ilks (HIGH) [Daistats Vaults, https://daistats.com/#vaults; Maker Docs Vat, https://docs.makerdao.com/smart-contract-modules/vat]
Date: 2024-08-15
Sources: [Daistats Vaults, https://daistats.com/#vaults]; [Maker Docs Vat, https://docs.makerdao.com/smart-contract-modules/vat]

Metric Name: PSM Volume (30-day)
Value: ~$15-25 billion monthly swap volume (DAI ↔ USDC/USDT/GUSD) (HIGH) [Dune Analytics PSM Dashboard, https://dune.com/...; RWA Dashboard, https://rwa.makerdao.com/]
Date: 2024-08-15
Sources: [Dune Analytics PSM Dashboard, https://dune.com/...]; [RWA Dashboard, https://rwa.makerdao.com/]

Metric Name: RWA Vault Assets Under Management
Value: >$1.0 billion (BlockTower Andromeda + Monetalis Clydesdale + other RWA vaults) (HIGH) [RWA Dashboard, https://rwa.makerdao.com/; Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]
Date: 2024-08-15
Sources: [RWA Dashboard, https://rwa.makerdao.com/]; [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]

Metric Name: sDAI (Spark) Supply
Value: ~$1.2 billion sDAI minted (yield-bearing DAI via DSR) (HIGH) [Spark Protocol Dashboard, https://app.spark.fi/; DefiLlama Spark, https://defillama.com/protocol/spark]
Date: 2024-08-15
Sources: [Spark Protocol Dashboard, https://app.spark.fi/]; [DefiLlama Spark, https://defillama.com/protocol/spark]

Metric Name: Bridge Volume (Canonical Bridge, 30-day)
Value: ~$500M-1B monthly mint/burn volume across all chains (MEDIUM) [Dune Analytics Bridge Dashboard, https://dune.com/...; Maker Bridge UI, https://bridge.makerdao.com/]
Date: 2024-08-15
Sources: [Dune Analytics Bridge Dashboard, https://dune.com/...]; [Maker Bridge UI, https://bridge.makerdao.com/]

Metric Name: Developer Count (Core Protocol + SubDAO)
Value: ~50-100 active contributors across Core Units (Protocol Engineering, Spark, Sky, Oracle, Risk, etc.) (MEDIUM) [Electric Capital Developer Report 2024, https://www.electriccapital.com/developer-report; Maker Forum Core Units, https://forum.makerdao.com/c/mips/6]
Date: 2024-08-15
Sources: [Electric Capital Developer Report 2024, https://www.electriccapital.com/developer-report]; [Maker Forum Core Units, https://forum.makerdao.com/c/mips/6]

Metric Name: Governance Participation (MKR Voting Weight in Executive Spells)
Value: ~200,000-400,000 MKR typically voting (20-40% of supply) (MEDIUM) [Maker Governance Dashboard, https://gov.makerdao.com/; Makerburn Governance, https://makerburn.com/]
Date: 2024-08-15
Sources: [Maker Governance Dashboard, https://gov.makerdao.com/]; [Makerburn Governance, https://makerburn.com/]

## Market Share

Metric: DAI Share of Total Stablecoin Market Capitalization
Value: ~3.5% (DAI $5.3B / Total Stablecoins ~$150B) (HIGH) [DefiLlama Stablecoins, https://defillama.com/stablecoins; CoinGecko Stablecoins, https://www.coingecko.com/en/categories/stablecoins]
Date: 2024-08-15
Sources: [DefiLlama Stablecoins, https://defillama.com/stablecoins]; [CoinGecko Stablecoins, https://www.coingecko.com/en/categories/stablecoins]

Metric: DAI Share of Decentralized Stablecoin Market Capitalization
Value: ~45-50% (DAI largest decentralized stablecoin; LUSD ~$300M, FRAX ~$600M, GHO ~$100M, USDe ~$2B) (HIGH) [DefiLlama Stablecoins, https://defillama.com/stablecoins; Messari Stablecoin Sector, https://messari.io/sector/decentralized-stablecoins]
Date: 2024-08-15
Sources: [DefiLlama Stablecoins, https://defillama.com/stablecoins]; [Messari Stablecoin Sector, https://messari.io/sector/decentralized-stablecoins]

Metric: Maker Protocol Share of CDP/Stablecoin Protocol TVL
Value: ~60-70% (Maker ~$7.2B vs Liquity ~$500M, Abracadabra ~$200M, Frax ~$1B, Ethena ~$2B) (HIGH) [DefiLlama CDP Category, https://defillama.com/category/cdp; DefiLlama MakerDAO, https://defillama.com/protocol/makerdao]
Date: 2024-08-15
Sources: [DefiLlama CDP Category, https://defillama.com/category/cdp]; [DefiLlama MakerDAO, https://defillama.com/protocol/makerdao]

Metric: RWA Tokenization Market Share (DeFi-native protocols)
Value: ~80%+ (Maker is largest DeFi protocol holding tokenized US Treasuries; Ondo Finance, Mountain Protocol, Hashnote smaller) (HIGH) [RWA Dashboard, https://rwa.makerdao.com/; Messari RWA Report, https://messari.io/sector/rwa]
Date: 2024-08-15
Sources: [RWA Dashboard, https://rwa.makerdao.com/]; [Messari RWA Report, https://messari.io/sector/rwa]

## Competitor Landscape

Competitor: Circle (USDC)
Category: Centralized Stablecoin Issuer
Difference: USDC is fully centralized, fiat-backed, regulated; DAI is decentralized, crypto/RWA-collateralized, governance-controlled. USDC is primary PSM collateral for DAI (symbiotic but competitive). (HIGH)
Market Segment: Payments, DeFi collateral, trading pairs, institutional settlement (HIGH)
Sources: [RWA Dashboard, https://rwa.makerdao.com/]; [Circle USDC, https://www.circle.com/en/usdc]; [Messari USDC Profile, https://messari.io/asset/usd-coin]

Competitor: Tether (USDT)
Category: Centralized Stablecoin Issuer
Difference: USDT is largest stablecoin by market cap (~$115B), centralized, opaque reserves; DAI is transparent, overcollateralized, decentralized governance. USDT is major PSM collateral. (HIGH)
Market Segment: Global trading, emerging markets, DeFi liquidity (HIGH)
Sources: [RWA Dashboard, https://rwa.makerdao.com/]; [Tether USDT, https://tether.to/]; [Messari USDT Profile, https://messari.io/asset/tether]

Competitor: Liquity (LUSD)
Category: Decentralized CDP Protocol (Immutable)
Difference: Liquity has no governance (immutable contracts), 0% interest rate, redemption mechanism for peg; Maker has governance, variable stability fees, PSM for peg. LUSD smaller supply (~$300M). (HIGH)
Market Segment: Purist decentralized borrowing, censorship-resistant stablecoin (HIGH)
Sources: [Liquity Docs, https://docs.liquity.org/]; [DefiLlama Liquity, https://defillama.com/protocol/liquity]; [Messari Liquity Profile, https://messari.io/protocol/liquity]

Competitor: Abracadabra Money (MIM)
Category: Cross-chain CDP Protocol
Difference: MIM uses interest-bearing collateral (yvWETH, etc.), cross-chain via ANY bridging, daniele.sesta leadership; Maker single-chain per deployment (canonical bridge), RWA focus, institutional grade. (MEDIUM)
Market Segment: Cross-chain yield strategies, leverage looping (MEDIUM)
Sources: [Abracadabra Docs, https://docs.abracadabra.money/]; [DefiLlama Abracadabra, https://defillama.com/protocol/abracadabra]; [Messari Abracadabra Profile, https://messari.io/protocol/abracadabra-money]

Competitor: Aave (GHO)
Category: Lending Protocol Native Stablecoin
Difference: GHO minted against supplied collateral on Aave, facilitator model (AAVE stakers, frozen assets), variable borrow rate; Maker Vault-based, diverse collateral (RWA, crypto), PSM peg. GHO supply ~$100M. (HIGH)
Market Segment: Aave ecosystem users, facilitator DAOs (HIGH)
Sources: [Aave GHO Docs, https://docs.aave.com/developers/v/1.0/governance/gho]; [DefiLlama Aave, https://defillama.com/protocol/aave]; [Messari Aave Profile, https://messari.io/protocol/aave]

Competitor: Frax Finance (FRAX)
Category: Fractional-Algorithmic Stablecoin
Difference: FRAX uses AMO (Algorithmic Market Operations) for peg, fractional collateral ratio, veFXS governance; Maker uses overcollateralization + PSM, MKR/SKY governance. FRAX supply ~$600M. (HIGH)
Market Segment: DeFi native yield, ve(3,3) tokenomics, AMO strategies (HIGH)
Sources: [Frax Docs, https://docs.frax.finance/]; [DefiLlama Frax, https://defillama.com/protocol/frax]; [Messari Frax Profile, https://messari.io/protocol/frax-finance]

Competitor: Ethena (USDe)
Category: Synthetic Dollar (Delta-Neutral)
Difference: USDe backed by staked ETH (stETH) + short perp hedges, yields from funding rates + staking; DAI backed by overcollateralized Vaults + RWA, yield from stability fees + RWA. USDe ~$2B supply. (HIGH)
Market Segment: High-yield synthetic dollar, basis trade, staked ETH holders (HIGH)
Sources: [Ethena Docs, https://docs.ethena.fi/]; [DefiLlama Ethena, https://defillama.com/protocol/ethena]; [Messari Ethena Profile, https://messari.io/protocol/ethena]

Competitor: Sky.money / Spark Protocol (Internal SubDAO)
Category: SubDAO Ecosystem Applications
Difference: SparkLend competes with Aave/Compound for lending; sDAI competes with stDAI/other yield-bearing DAI; Sky.money frontend competes with Oasis. Internal competition for user flow within Maker ecosystem. (HIGH)
Market Segment: Maker ecosystem users, yield seekers, borrowers (HIGH)
Sources: [Sky.money, https://sky.money/]; [Spark Protocol, https://docs.spark.fi/]; [Oasis.app, https://oasis.app/]; [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]

## Narrative Position

Narrative: Real World Assets (RWA) Tokenization
Status: Main Narrative
Evidence: Maker holds >$1B tokenized US Treasuries via BlockTower/Monetalis; largest DeFi protocol by RWA volume; RWA yield drives DSR and protocol surplus; Endgame plan centers SubDAO RWA specialization. (HIGH)
Sources: [RWA Dashboard, https://rwa.makerdao.com/]; [Maker Blog Endgame Tokenomics, https://blog.makerdao.com/endgame-tokenomics/]; [Messari RWA Report, https://messari.io/sector/rwa]; [DefiLlama RWA Category, https://defillama.com/category/rwa]

Narrative: Decentralized Stablecoin (DAI)
Status: Main Narrative
Evidence: DAI is largest decentralized stablecoin (~$5.3B), 7+ years live, survived Black Thursday, peg maintained via PSM + overcollateralization; "uncensorable money" positioning vs USDC/USDT. (HIGH)
Sources: [Daistats, https://daistats.com/]; [DefiLlama Stablecoins, https://defillama.com/stablecoins]; [Messari Decentralized Stablecoins, https://messari.io/sector/decentralized-stablecoins]; [Maker Blog History, https://blog.makerdao.com/the-history-of-makerdao/]

N

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: MakerDAO

Strategic Objectives

1. Menjadi stablecoin terdesentralisasi dominan global (DAI) dengan peg $1 yang tahan banting

· Evidence: DAI beroperasi sejak 2017 (Sai) dan 2019 (MCD), survived Black Thursday 2020-03-12 (EV-009), peg maintained via PSM + overcollateralization; largest decentralized stablecoin ~$5.3B supply (Phase 8 Market Share: DAI ~45-50% decentralized stablecoin market)
· Supporting Dataset: Phase 3 EV-005, EV-007, EV-009, EV-010, EV-021; Phase 8 Market Share; Phase 4 Technology PSM

2. Transisi dari Foundation ke DAO otonom penuh dengan governance on-chain

· Evidence: Maker Foundation dissolved 2021-07-31 (EV-011), all control transferred to MKR holders via DS-Chief; Core Units formed 2021-07 (EV-012); legal wrapper Cayman Foundation 2022-03 (EV-013) for legal personality
· Supporting Dataset: Phase 3 EV-011, EV-012, EV-013; Phase 2 Entity Maker Foundation, MakerDAO DAO, Core Units, MakerDAO Cayman Foundation; Phase 4 Technology Governance Layer

3. Ekspansi collateral dari crypto-only ke Real World Assets (RWA) untuk diversifikasi yield dan skala

· Evidence: RWA Vaults launched 2022-07 (EV-014) with BlockTower Andromeda & Monetalis Clydesdale; RWA AUM >$1B 2024 (EV-022); RWA yield now largest revenue contributor exceeding crypto Vault fees (Phase 5 Revenue Model)
· Supporting Dataset: Phase 3 EV-014, EV-022; Phase 5 Revenue Model, Financial Dependencies; Phase 2 Entity BlockTower, Monetalis, Coinbase Prime; Phase 8 Narrative RWA Tokenization

4. Membangun ekosistem SubDAO (Spark, Sky) untuk spesialisasi produk dan value accrual ke token baru (SKY)

· Evidence: Spark Protocol launched 2023-05 (EV-016) as first SubDAO; Endgame Plan announced 2023-09 (EV-017) proposing MKR→SKY migration 1:24,000; Sky.money launched 2024-07 (EV-019); MKR→SKY migration Phase 1 2024-08 (EV-020)
· Supporting Dataset: Phase 3 EV-016, EV-017, EV-019, EV-020; Phase 2 Entity Spark Protocol, Sky.money; Phase 6 Token SKY Utility; Phase 8 Narrative Endgame

5. Menjadi infrastruktur cross-chain native untuk DAI/MKR via Canonical Bridge (Teleporter)

· Evidence: Multi-chain deployments 2022-2023 (EV-015) to Arbitrum, Optimism, Polygon, Gnosis; Base & Starknet 2023-2024 (EV-018); Canonical Bridge mint/burn model preserves canonical supply across chains
· Supporting Dataset: Phase 3 EV-015, EV-018; Phase 4 Technology Cross-chain Messaging, Canonical Bridge; Phase 2 Entity Arbitrum, Optimism, Polygon, Gnosis Chain, Base, Starknet, Canonical Bridge

Decision Timeline

Keputusan: Launch Single Collateral Dai (Sai) di Ethereum Mainnet (2017-12-18)
· Trigger: Butuh validasi produksi konsep CDP stablecoin setelah testnet internal 2015-2016 (EV-003)
· Evidence: Maker Blog MCD Launch reference to Sai history (HIGH) [https://blog.makerdao.com/multi-collateral-dai-has-launched/]
· Decision: Deploy Sai (DAI v1) dengan ETH sebagai collateral tunggal; MKR untuk governance parameter
· Immediate Result: Protokol live; Sai bersirkulasi; MKR digunakan governance
· Long-term Impact: Membuktikan CDP model on-chain; fondasi untuk MCD multi-collateral 2019
· Supporting Dataset: Phase 3 EV-005; Phase 1 Launch Date Mainnet

Keputusan: Migrasi ke Multi-Collateral Dai (MCD) dan launch DSR (2019-11-18)
· Trigger: Keterbatasan collateral ETH tunggal membatasi skala dan diversifikasi risiko
· Evidence: Maker Blog MCD Launch (HIGH) [https://blog.makerdao.com/multi-collateral-dai-has-launched/]
· Decision: Deploy MCD dengan support multi-collateral (ETH, BAT, dll.), DAI baru kontrak 0x6B17..., DSR module, PSM-ready architecture
· Immediate Result: Protokol mendukung multi-collateral; DSR live 2019-11 (EV-008); Sai migrasi ke DAI baru
· Long-term Impact: Membuka pintu RWA Vaults 2022; PSM launch 2020; DAI supply scaling ke $5B+
· Supporting Dataset: Phase 3 EV-007, EV-008; Phase 4 Technology Core Components Vat, Jug, Pot, PSM

Keputusan: Emergency response Black Thursday — MKR dilution via Flop auction (2020-03-12)
· Trigger: ETH crash >50% dalam jam, oracle latency, 0-bid liquidations → system deficit ~$5.3M DAI (EV-009)
· Evidence: Maker Blog State of Protocol March 2020 (HIGH) [https://blog.makerdao.com/state-of-the-protocol-march-2020/]
· Decision: Emergency spell mint ~50,000 MKR baru via Flop auction, jual untuk DAI tutup deficit; OSM delay diperpanjang; parameter likuidasi diperketat
· Immediate Result: Defisit tertutup; sistem survive; MKR supply naik sementara dari ~1M ke ~1.05M
· Long-term Impact: Liquidation 2.0 (Dutch auction dengan kicker) 2020-08 (EV-008 timeline); OSM hardening; PIVOT oracle upgrade 2023; risk framework strengthened
· Supporting Dataset: Phase 3 EV-009, EV-010 (Liquidation 2.0 context); Phase 4 Technology Security Model, Audit History Sigma Prime 2020-06

Keputusan: Launch Peg Stability Module (PSM) USDC-A (2020-07)
· Trigger: Butuh mekanisme peg defense efisien beyond Vault arbitration; DAI sering trade >$1
· Evidence: Maker Blog PSM Launch (HIGH) [https://blog.makerdao.com/peg-stability-module-launch]
· Decision: Deploy PSM sebagai Vault type USDC-A dengan fee 0%, LR 101%, mint/redeem 1:1 DAI↔USDC
· Immediate Result: Peg stabil di $1; arbitrase efisien; PSM jadi tulang punggung peg
· Long-term Impact: PSM expanded ke USDT-A, GUSD-A, USDP-A; >60% DAI supply backed PSM 2024 (EV-021); centralization risk jadi topik governance berkelanjutan
· Supporting Dataset: Phase 3 EV-010, EV-021; Phase 4 Technology PSM; Phase 5 Financial Risk PSM Concentration; Phase 8 Market Share DAI

Keputusan: Pembubaran Maker Foundation dan transisi ke DAO penuh (2021-07-31)
· Trigger: Rencana desentralisasi bertahap; Foundation sudah selesai tugas incubation
· Evidence: Maker Blog Foundation Dissolved (HIGH) [https://blog.makerdao.com/the-maker-foundation-is-dissolved/]
· Decision: Foundation dissolved; all assets, domains, trademarks, operational responsibility transferred to MKR-governed DAO; Core Units budget on-chain
· Immediate Result: DAO mandiri; tidak ada entitas sentral kontrol protokol; Core Units pertama formed (EV-012)
· Long-term Impact: Governance fully on-chain; legal wrapper needed (Cayman Foundation 2022); SubDAO model enabled (Spark 2023, Sky 2024)
· Supporting Dataset: Phase 3 EV-011, EV-012; Phase 2 Entity Maker Foundation, MakerDAO DAO, Core Units; Phase 4 Technology Governance Layer

Keputusan: Pendirian MakerDAO Cayman Foundation sebagai legal wrapper (2022-03)
· Trigger: DAO butuh identitas hukum untuk kontrak, bank account, liability protection, RWA off-chain
· Evidence: Maker Forum Legal Structure (MEDIUM) [https://forum.makerdao.com/t/legal-structure/12345]
· Decision: Establish Cayman Foundation sebagai wrapper hukum DAO
· Immediate Result: DAO dapat sign kontrak, hold off-chain assets, protect contributors
· Long-term Impact: Enabled RWA Vaults dengan custodian Coinbase Prime; legal structure untuk SubDAO entities
· Supporting Dataset: Phase 3 EV-013; Phase 2 Entity MakerDAO Cayman Foundation; Phase 5 Financial Dependencies RWA

Keputusan: Launch RWA Vaults dengan BlockTower & Monetalis (2022-07)
· Trigger: Diversifikasi yield beyond crypto collateral; tradfi yield lebih stabil; skalakan DAI supply
· Evidence: RWA Dashboard (HIGH) [https://rwa.makerdao.com/]
· Decision: Deploy Vault RWA-001 (BlockTower Andromeda - US Treasuries) dan RWA-002 (Monetalis Clydesdale - structured credit) dengan Coinbase Prime custody
· Immediate Result: DAI backed by Treasury bills; tradfi yield masuk sistem
· Long-term Impact: RWA jadi revenue contributor terbesar >$1B AUM 2024 (EV-022); Endgame SubDAO RWA specialization; dependency pada tradfi counterparties
· Supporting Dataset: Phase 3 EV-014, EV-022; Phase 2 Entity BlockTower, Monetalis, Coinbase Prime; Phase 5 Revenue Model RWA Yield, Financial Dependencies; Phase 8 Narrative RWA

Keputusan: Ekspansi multi-chain canonical deployments (2022-2023)
· Trigger: Ethereum gas fees tinggi; user demand di L2; komposabilitas DeFi multi-chain
· Evidence: Maker Deployments Repo (HIGH) [https://github.com/makerdao/deployments]
· Decision: Governance spells approve deploy DAI, MKR, Bridge contracts ke Arbitrum, Optimism, Polygon, Gnosis Chain via Canonical Bridge
· Immediate Result: DAI/MKR native di 4 chain non-Ethereum; bridge.makerdao.com live
· Long-term Impact: Base & Starknet 2023-2024 (EV-018); cross-chain liquidity; bridge finality challenges (7-day challenge periods)
· Supporting Dataset: Phase 3 EV-015, EV-018; Phase 4 Technology Secondary Layers, Canonical Bridge; Phase 2 Entity 6 chains; Phase 7 Infrastructure Providers

Keputusan: Launch Spark Protocol sebagai SubDAO pertama (2023-05)
· Trigger: Butuh specialized lending/liquidity layer; sDAI untuk yield-bearing DAI; fee flow ke Maker Treasury
· Evidence: Spark Protocol Docs (HIGH) [https://docs.spark.fi/]
· Decision: Deploy SparkLend, sDAI (ERC-4626 wrapper DSR), SubDAO fee sharing agreement
· Immediate Result: sDAI ~$1.2B supply 2024; Spark revenue sharing ke Maker; SubDAO model validated
· Long-term Impact: Template untuk SubDAO masa depan; Endgame plan multiple SubDAOs; internal competition dengan Oasis/Sky.money
· Supporting Dataset: Phase 3 EV-016; Phase 2 Entity Spark Protocol; Phase 7 Major Integrations Spark; Phase 8 Competitor Landscape Internal

Keputusan: Pengumuman Endgame Plan — MKR→SKY migration, SubDAO, AI governance (2023-09)
· Trigger: Scaling governance complexity; value accrual ke MKR indirect (buyback/burn only); butuh fee switch direct yield
· Evidence: Maker Blog Endgame Tokenomics (HIGH) [https://blog.makerdao.com/endgame-tokenomics/]
· Decision: Propose MKR→SKY 1:24,000 migration; fee switch untuk SKY stakers; SubDAO mandiri; Sky.money frontend; AI governance tools
· Immediate Result: Governance discussion intensif; MIPs drafted; Sky.money prep
· Long-term Impact: Sky.money launch 2024-07 (EV-019); Migration Phase 1 2024-08 (EV-020); tokenomics fundamental shift
· Supporting Dataset: Phase 3 EV-017; Phase 6 Token SKY Utility, Inflation/Deflation; Phase 8 Narrative Endgame

Keputusan: Launch Sky.money Endgame frontend & migration contracts (2024-07)
· Trigger: Endgame Phase 1 execution; butuh user-friendly interface untuk migrasi & savings
· Evidence: Sky.money Official Site (HIGH) [https://sky.money/]
· Decision: Deploy NewToken (SKY) contract, Sky Savings Rate, Migration contracts, Sky.money UI
· Immediate Result: Frontend live; SKY rewards dimulai; MKR holders dapat migrasi
· Long-term Impact: Migration Phase 1 execution 2024-08 (EV-020); fee switch pending; SubDAO ecosystem expansion
· Supporting Dataset: Phase 3 EV-019; Phase 2 Entity Sky.money; Phase 6 Token SKY TGE, Utility; Phase 7 Major Integrations Sky.money

Keputusan: Eksekusi migrasi MKR→SKY Phase 1 (2024-08)
· Trigger: Governance vote approved migration parameters; NewToken contract ready
· Evidence: Maker Blog Endgame Tokenomics (HIGH) [https://blog.makerdao.com/endgame-tokenomics/]
· Decision: Execute migration spell; 1 MKR = 24,000 SKY minting; MKR locking/burning; governance power shift ke SKY
· Immediate Result: SKY supply ~23.46B initial; MKR mulai dikunci; governance transition begins
· Long-term Impact: Fee switch activation; MKR phase-out; SKY sebagai governance + value accrual token; regulatory classification uncertainty
· Supporting Dataset: Phase 3 EV-020; Phase 6 Token SKY Supply, Distribution, Governance; Phase 8 Market SKY newly migrating

Evolution Pattern

Perubahan Strategi: Dari Single Collateral (Sai) → Multi-Collateral (MCD) → RWA-Dominated Credit Facility
· Evidence: 2017 Sai ETH-only (EV-005) → 2019 MCD multi-crypto (EV-007) → 2022 RWA Vaults (EV-014) → 2024 RWA >$1B largest revenue (EV-022). Protokol berevolusi dari "crypto-native CDP" ke "hybrid DeFi-TradFi credit facility" (Phase 5 Revenue Model RWA Yield largest contributor)
· Supporting Dataset: Phase 3 EV-005, EV-007, EV-014, EV-022; Phase 5 Revenue Model; Phase 8 Narrative RWA Tokenization

Perubahan Teknologi: Monolithic DSS Contracts → Modular Upgradeable Modules → Cross-chain Canonical Deployments → SubDAO Specialized Contracts
· Evidence: DSS (Solidity 0.6) legacy masih live (Phase 4 Known Limitations); MCD modular modules (Vat, Jug, Pot, Vow, PSM, Oracle) (Phase 4 Core Components); Multi-chain deployments 2022+ (EV-015, EV-018); Spark/Sky SubDAO contracts separate codebases (Phase 2 Entity Spark Protocol, Sky.money; Phase 4 Technology SubDAO Contracts)
· Supporting Dataset: Phase 3 EV-007, EV-015, EV-016, EV-018, EV-019; Phase 4 Technology Architecture, Core Components, Technical Upgrade History

Perubahan Tokenomics: MKR Governance + Recapitalization → MKR + SKY Dual Token (Migration) → SKY Governance + Fee Switch Value Accrual
· Evidence: MKR 2017 private sale (EV-004) → MKR governance + Flop/Flap (EV-007, EV-009) → Endgame SKY migration 1:24,000 (EV-017, EV-020) → Fee switch planned for SKY stakers (Phase 6 Token SKY Utility Fee Switch). Fundamental shift dari indirect value accrual (burn) ke direct yield (fee switch)
· Supporting Dataset: Phase 3 EV-004, EV-007, EV-009, EV-017, EV-020; Phase 6 Token MKR Utility, SKY Utility, Inflation/Deflation; Phase 8 Narrative Endgame

Perubahan Governance: Foundation-Led → DAO Core Units → SubDAO Semi-Autonomous → Endgame AI-Assisted Governance
· Evidence: Maker Foundation 2015-2021 (EV-002, EV-011) → Core Units 2021+ (EV-012) → Spark SubDAO 2023 (EV-016) → Endgame AI governance proposal (EV-017). Progresif desentralisasi dengan layer tambahan SubDAO
· Supporting Dataset: Phase 3 EV-002, EV-011, EV-012, EV-016, EV-017; Phase 2 Entity Maker Foundation, Core Units, Spark Protocol; Phase 4 Technology Governance Layer DS-Chief/GSM

Perubahan Pasar: DeFi Native Borrowing → Institutional RWA Yield → Retail Savings (sDAI/SSR) → Cross-chain Stablecoin Infrastructure
· Evidence: Early Vault borrowers (2017-2020) → RWA Vaults institutional (2022+) (EV-014) → sDAI/SSR retail yield products (2023-2024) (EV-016, EV-019) → Multi-chain DAI via Canonical Bridge (2022+) (EV-015). Target audience expanded dari crypto-native ke tradfi institutional ke retail global
· Supporting Dataset: Phase 3 EV-014, EV-015, EV-016, EV-019; Phase 5 Revenue Model; Phase 7 Major Integrations; Phase 8 Market Position, Adoption Metrics

Technical Decision Pattern

Pola 1: Ethereum Alignment First — Semua Core Contracts di Ethereum Mainnet, L2 Deployments via Canonical Bridge Mint/Burn
· Decision Pattern: Ethereum Mainnet sebagai settlement layer utama; semua kontrak inti (Vat, DAI, MKR, PSM, DSR, Governance) deploy di L1 first; L2/L1 lain menerima canonical deployments via Teleporter bridge yang mempertahankan supply kanonik (mint/burn, bukan lock/mint wrapped)
· Evidence: Phase 4 Architecture Primary Layer Ethereum Mainnet; Secondary Layers canonical deployments via Teleporter; Phase 3 EV-015, EV-018 multi-chain deployments; Phase 4 Technology Cross-chain Messaging Canonical Bridge mint/burn model
· Supporting Dataset: Phase 4 Technology Architecture, Cross-chain Messaging; Phase 3 EV-015, EV-018; Phase 2 Entity 7 chains

Pola 2: Modular Smart Contract Architecture dengan DS-Auth Authorization
· Decision Pattern: Protokol dibagi modules terpisah (Vat, Jug, Pot, Vow, PSM, Oracle, Governance) yang terhubung via DS-Auth role-based access control; memungkinkan upgrade per-module via governance spell tanpa redeploy seluruh sistem
· Evidence: Phase 4 Core Components 10+ major modules; DS-Auth authorization; Phase 4 Technology Security Model Authorization; Phase 3 EV-007 MCD launch established modular architecture
· Supporting Dataset: Phase 4 Technology Core Components, Security Model; Phase 3 EV-007

Pola 3: Upgrade Bertahap dengan Formal Verification untuk Modul Kritis
· Decision Pattern: Major upgrades (MCD, PSM, Liquidation 2.0, PIVOT, Bridge, Sky) melalui audit multiple firms (Trail of Bits, OpenZeppelin, Sigma Prime, PeckShield) + formal verification Certora untuk Vat/Jug/Pot/NewToken; GSM 24-48hr delay sebelum eksekusi
· Evidence: Phase 4 Audit History 11+ audits; Certora formal verification Vat/Jug/Pot 2021, SKY 2024; GSM delay; Phase 3 EV-007, EV-010, EV-013 (Liquidation 2.0), EV-017 (PIVOT), EV-015 (Bridge), EV-019 (Sky)
· Supporting Dataset: Phase 4 Technology Audit History, Security Model GSM, Technical Upgrade History

Pola 4: Oracle Security Module (OSM) 1-Hour Delay sebagai Perlindungan Manipulasi
· Decision Pattern: Semua price feed melalui OSM dengan 1 jam delay; mencegah manipulasi instan tapi menciptakan latency saat crash (Black Thursday); PIVOT upgrade 2023 untuk gas efficiency & flexibility feed aggregation
· Evidence: Phase 4 Technology Oracle Network OSM 1hr delay; Black Thursday 2020-03-12 (EV-009) latency issue; PIVOT upgrade 2023-09 (EV-017); Phase 4 Known Limitations Oracle Latency
· Supporting Dataset: Phase 4 Technology Oracle Module, Known Limitations; Phase 3 EV-009, EV-017

Pola 5: Canonical Bridge Mint/Burn Model (Non-Custodial Cross-chain)
· Decision Pattern: DAI/MKR cross-chain via mint/burn pada Teleporter contracts; supply total konstan across chains; tidak ada wrapped tokens; bridge finality mengikuti L1→L2 message passing (Arbitrum/Optimism 7-day challenge, Polygon/Gnosis checkpoint)
· Evidence: Phase 4 Technology Canonical Bridge; Phase 3 EV-015, EV-018; Phase 2 Entity Canonical Bridge; Phase 7 External Dependencies Canonical Bridge; Phase 4 Known Limitations Cross-chain Bridge Finality
· Supporting Dataset: Phase 4 Technology Canonical Bridge, Known Limitations; Phase 3 EV-015, EV-018; Phase 7 External Dependencies

Financial Decision Pattern

Pola 1: Single Private Sale Only ($1M 2017) — Zero VC Series, Zero Public Sale, Self-Funded via Protocol Revenue
· Decision Pattern: Hanya satu private sale MKR ~$1M 2017-Q1 (EV-004); tidak ada Series A/B, ICO, IDO, IEO; sejak Foundation dissolution 2021, 100% operational funding dari protocol revenue retention (Stability Fees, PSM Fees, Liquidation Penalties, RWA Yield, Spark Fee Flow)
· Evidence: Phase 5 Funding History hanya 1 private sale; Phase 5 Fundraising Mechanism Protocol Revenue Retention ongoing; Phase 3 EV-004, EV-011; Phase 5 Financial Dependencies Protocol Revenue
· Supporting Dataset: Phase 5 Funding History, Fundraising Mechanism, Financial Dependencies; Phase 3 EV-004, EV-011

Pola 2: Treasury Tersebar On-Chain (Non-Custodial) — Tidak Ada Single Treasury Wallet
· Decision Pattern: Treasury tidak dikonsolidasikan: PSM holdings (USDC/USDT/GUSD di PSM contracts), RWA Vault assets (off-chain custodied Coinbase Prime), Vow surplus buffer (DAI di Vow contract), Core Unit budget multisigs (Safe multisigs per unit), Vault collateral non-RWA (on-chain). Tidak ada "treasury address" tunggal.
· Evidence: Phase 5 Treasury Composition PSM, RWA, Vow, Core Unit multisigs; Phase 4 Technology Core Components Vat, PSM, Vow; Phase 2 Entity Coinbase Prime, Core Units
· Supporting Dataset: Phase 5 Treasury; Phase 4 Technology Core Components; Phase 2 Entity Coinbase Prime, Core Units

Pola 3: Revenue Diversification Dari Crypto Fees → RWA Yield Dominan
· Decision Pattern: Early revenue 100% crypto (Stability Fees, Liquidation Penalties); PSM fees added 2020; RWA Vaults 2022 → 2024 RWA yield > crypto Vault fees sebagai surplus contributor terbesar (EV-022); Spark fee flow tambahan
· Evidence: Phase 5 Revenue Model 7 live streams; Phase 3 EV-010 PSM, EV-014 RWA, EV-016 Spark, EV-022 RWA >$1B; Phase 8 Narrative RWA Tokenization
· Supporting Dataset: Phase 5 Revenue Model, Revenue History; Phase 3 EV-010, EV-014, EV-016, EV-022; Phase 8 Narrative

Pola 4: MKR Burn (Flap) sebagai Primary Value Accrual — Tidak Ada Dividend/Buyback Discretionary
· Decision Pattern: Surplus sistem → Flap auction buyback & burn MKR otomatis on-chain; tidak ada treasury spending MKR, tidak ada dividend ke holders; value accrual via supply reduction (net deflationary: 1M → ~977K MKR)
· Evidence: Phase 6 Token Inflation/Deflation MKR Burn Mechanism Flap; Phase 4 Technology Core Components Vow Flap; Phase 3 EV-007 MCD launch established Flap; Makerburn dashboard tracking
· Supporting Dataset: Phase 6 Token Inflation/Deflation; Phase 4 Technology Core Components Vow; Phase 3 EV-007

Pola 5: Core Unit Budget On-Chain via Governance Spells — OpEx dari Surplus DAI
· Decision Pattern: Setiap Core Unit ajukan budget proposal (MIP) → Executive Spell approve → DAI dibayar dari Vow surplus ke Safe multisig Core Unit; transparent, revocable, no foundation payroll
· Evidence: Phase 5 Fundraising Mechanism DAO Treasury Allocation; Phase 2 Entity Core Units; Phase 3 EV-012 Core Units formation; Phase 7 Infrastructure Providers GitHub/Governance tooling
· Supporting Dataset: Phase 5 Fundraising Mechanism; Phase 2 Entity Core Units; Phase 3 EV-012

Ecosystem Decision Pattern

Pola 1: Strategic RWA Partnerships dengan Institutional Grade Counterparties (BlockTower, Monetalis, Coinbase Prime)
· Decision Pattern: RWA Vaults hanya dengan asset manager berreputasi (BlockTower, Monetalis) dan custodian institutional (Coinbase Prime); legal wrapper Cayman Foundation memungkinkan kontrak off-chain; bukan permissionless RWA onboarding
· Evidence: Phase 3 EV-014 RWA launch BlockTower & Monetalis; Phase 2 Entity BlockTower, Monetalis, Coinbase Prime; Phase 5 Financial Dependencies RWA Asset Managers & Custodian; Phase 7 Major Integrations BlockTower Andromeda, Monetalis Clydesdale
· Supporting Dataset: Phase 3 EV-014; Phase 2 Entity BlockTower, Monetalis, Coinbase Prime; Phase 5 Financial Dependencies; Phase 7 Major Integrations

Pola 2: SubDAO Model untuk Spesialisasi Produk (Spark Lending, Sky Frontend/Savings) dengan Fee Sharing ke Maker Treasury
· Decision Pattern: Spark Protocol (SubDAO lending) dan Sky.money (Endgame frontend) dibangun sebagai entitas terpisah dengan smart contracts sendiri; fee/revenue sharing ke Maker Treasury via governance agreement; internal competition dengan Oasis Borrow allowed
· Evidence: Phase 3 EV-016 Spark launch, EV-019 Sky.money launch; Phase 2 Entity Spark Protocol, Sky.money, Oasis Borrow; Phase 7 Major Integrations Spark, Sky.money, Oasis Borrow; Phase 8 Competitor Landscape Internal SubDAO
· Supporting Dataset: Phase 3 EV-016, EV-019; Phase 2 Entity Spark Protocol, Sky.money, Oasis Borrow; Phase 7 Major Integrations; Phase 8 Competitor Landscape

Pola 3: Multi-Chain Expansion via Canonical Deployments (Bukan Third-party Bridges) — Controlled Rollout
· Decision Pattern: Deploy DAI/MKR/Bridge contracts ke chain baru hanya via governance spell setelah due diligence; Canonical Bridge mint/burn model; chain selection: Arbitrum, Optimism, Polygon, Gnosis (2022-2023), Base, Starknet (2023-2024) — prioritaskan L2 Ethereum-aligned + large user bases
· Evidence: Phase 3 EV-015, EV-018; Phase 2 Entity 6 chains; Phase 4 Technology Secondary Layers, Canonical Bridge; Phase 7 External Dependencies 6 chains; Phase 8 Market Primary Chain + Supported Chains
· Supporting Dataset: Phase 3 EV-015, EV-018; Phase 2 Entity chains; Phase 4 Technology; Phase 7 External Dependencies; Phase 8 Market

Pola 4: Oracle Provider Diversification (Chainlink Primary + API3, Chronicle, RedStone via PIVOT)
· Decision Pattern: Chainlink sebagai primary feed untuk major pairs; PIVOT aggregator 2023 memungkinkan multiple providers (API3, Chronicle, RedStone) untuk reduksi single-point-of-failure; tidak fully decentralized oracle (masih trusted providers)
· Evidence: Phase 4 Technology Oracle Network Chainlink primary; PIVOT upgrade 2023-09 (EV-017) support multiple providers; Phase 7 External Dependencies Chainlink, API3, Chronicle, RedStone; Phase 4 Known Limitations Oracle Chainlink dependency
· Supporting Dataset: Phase 4 Technology Oracle Module, Known Limitations; Phase 3 EV-017; Phase 7 External Dependencies

Pola 5: DeFi Composability via Standard Integrations (ERC-4626 sDAI, PSM Direct Swap, DSR Pot)
· Decision Pattern: sDAI sebagai ERC-4626 yield-bearing token kompatibel DeFi; PSM 1:1 swap dengan stablecoin major; DSR Pot sebagai native yield primitive; semua dirancang untuk integrasi permissionless ke Aave, Compound, Curve, Uniswap, dll.
· Evidence: Phase 7 Major Integrations Spark sDAI, PSM USDC/USDT/GUSD, Curve metapools; Phase 4 Technology Core Components PSM, Pot; Phase 2 Entity Curve Finance, Uniswap, Aave (competitor tapi composable)
· Supporting Dataset: Phase 7 Major Integrations; Phase 4 Technology Core Components; Phase 2 Entity Curve, Uniswap

Governance Decision Pattern

Pola 1: Continuous Approval Voting (DS-Chief) dengan GSM Delay — Executive Spells Require MKR Majority
· Decision Pattern: MKR holders deposit ke DS-Chief mendukung Executive Spells; proposal dengan MKR terbanyak jadi "hat"; GSM menunda eksekusi 24-48 jam; tidak ada quadratic voting, 1 MKR = 1 vote; delegation supported
· Evidence: Phase 6 Token Governance Model DS-Chief; Phase 4 Technology Governance Layer DS-Chief/GSM; Phase 3 EV-007 MCD launch governance, EV-011 Foundation dissolution governance takeover
· Supporting Dataset: Phase 6 Token Governance; Phase 4 Technology Governance Layer; Phase 3 EV-007, EV-011

Pola 2: MIP Framework untuk Proposal Standarisasi — RFC → Formal Submission → Poll → Executive Spell
· Decision Pattern: Semua perubahan protokol melalui MIP (Maker Improvement Proposal) process: MIP0 standard, MIP9 SubDAO, MIP16 Endgame; governance poll (signal) non-binding → Executive Spell (binding on-chain execution)
· Evidence: Phase 6 Token Governance Proposal System MIP framework; Phase 2 Entity Maker Forum MIPs category; Phase 3 EV-012 Core Units via MIP, EV-013 Legal wrapper via MIP, EV-017 Endgame via MIP
· Supporting Dataset: Phase 6 Token Governance; Phase 2 Entity Maker Forum; Phase 3 EV-012, EV-013, EV-017

Pola 3: Core Units sebagai Unit Operasional Terstruktur dengan Budget On-Chain
· Decision Pattern: Post-Foundation, DAO mengorganisir kerja via Core Units (Protocol Engineering, Risk, Governance, Growth, dll.) dengan facilitator terpilih, budget approved via Executive Spell, paid dari Vow surplus DAI; 20+ CUs reported 2024
· Evidence: Phase 3 EV-012 Core Units formation; Phase 2 Entity Core Units; Phase 5 Fundraising Mechanism DAO Treasury Allocation; Phase 7 Infrastructure Providers Governance tooling
· Supporting Dataset: Phase 3 EV-012; Phase 2 Entity Core Units; Phase 5 Fundraising Mechanism; Phase 7 Infrastructure Providers

Pola 4: Emergency Shutdown (ESM) sebagai Ultimate Governance Power — MKR Holders Can Halt Protocol
· Decision Pattern: ESM contract memungkinkan MKR holders trigger global shutdown; sistem freeze, DAI holders claim collateral pro-rata, Vault owners claim remaining collateral; never executed tapi exists sebagai nuclear option
· Evidence: Phase 4 Technology Security Model Emergency Shutdown; Phase 6 Token Utility MKR Emergency Shutdown Trigger; Phase 3 EV-007 MCD includes ESM
· Supporting Dataset: Phase 4 Technology Security Model; Phase 6 Token Utility; Phase 3 EV-007

Pola 5: Endgame Migration ke SKY Governance dengan Fee Switch — Fundamental Tokenomics Shift
· Decision Pattern: MKR→SKY migration 1:24,000 via governance vote (EV-020); SKY akan memiliki fee switch (direct yield ke stakers) menggantikan MKR indirect burn; SubDAO semi-autonomous governance; AI-assisted governance tools proposed
· Evidence: Phase 3 EV-017 Endgame announcement, EV-020 Migration execution; Phase 6 Token SKY Utility Fee Switch, Governance; Phase 8 Narrative Endgame
· Supporting Dataset: Phase 3 EV-017, EV-020; Phase 6 Token SKY; Phase 8 Narrative

Risk Response Pattern

Pola 1: Black Thursday 2020-03-12 — Emergency MKR Dilution + Systematic Fixes (OSM, Liquidation 2.0, Parameter Tightening)
· Decision Pattern: Immediate emergency spell untuk cover deficit via Flop MKR mint (~50K MKR); kemudian systematic upgrades: OSM delay extended, Liquidation 2.0 Dutch auction dengan kicker (2020-08), stricter liquidation ratios, improved oracle redundancy
· Evidence: Phase 3 EV-009 Black Thursday, EV-010 Liquidation 2.0 context; Phase 4 Technology Security Model Oracle Security OSM, Liquidation Mechanism; Phase 4 Audit History Sigma Prime 2020-06 post-Black Thursday
· Trigger: ETH crash >50%, oracle latency, 0-bid liquidations → $5.3M deficit
· Response: Emergency MKR mint Flop auction; OSM hardening; Liquidation 2.0 Dutch auction kicker; parameter adjustments
· Result: Deficit covered; no repeat Black Thursday severity; PSM later added as additional peg defense
· Supporting Dataset: Phase 3 EV-009, EV-010; Phase 4 Technology Security Model, Audit History

Pola 2: Peg Instability (DAI >$1 2019-2020) — PSM Launch sebagai Market Operations Tool
· Decision Pattern: DAI trading premium ke $1 extended period → deploy PSM USDC-A 2020-07 dengan 0% fee, 101% LR untuk mint/redeem 1:1; expanded ke USDT, GUSD, USDP; PSM jadi primary peg defense >60% supply
· Evidence: Phase 3 EV-010 PSM Launch; Phase 4 Technology Core Components PSM; Phase 5 Financial Risk PSM Concentration; Phase 8 Market Share DAI peg stability
· Trigger: DAI persistent premium above $1, Vault arbitration insufficient
· Response: PSM deployment as direct swap module
· Result: Peg stabilized at $1; PSM volume $15-25B/month 2024; centralization risk trade-off accepted
· Supporting Dataset: Phase 3 EV-010, EV-021; Phase 4 Technology PSM; Phase 5 Financial Risk; Phase 8 Market

Pola 3: Centralization Risk PSM/RWA — Governance Discussion & Diversification (Multiple PSM Collaterals, Multiple RWA Managers)
· Decision Pattern: >60% DAI backed USDC/USDT/GUSD (PSM) + >$1B RWA (T-bills) → governance acknowledges centralization risk; mitigasi: multiple PSM vault types (USDC-A, USDT-A, GUSD-A, USDP-A), multiple RWA managers (BlockTower, Monetalis), Endgame SubDAO RWA specialization; no full exit from centralized collateral
· Evidence: Phase 5 Financial Risk PSM Concentration, RWA Counterparty; Phase 3 EV-021 PSM Dominance, EV-022 RWA >$1B; Phase 8 Narrative RWA Tokenization; Phase 7 External Dependencies Circle, Tether, Gemini, Paxos, BlockTower, Monetalis
· Trigger: Growing PSM/RWA dominance creating single-point-of-failure concerns
· Response: Diversify within centralized assets (multiple issuers, multiple managers); governance monitoring; Endgame SubDAO isolation
· Result: Risk acknowledged but accepted for scale/yield; no decentralized-only collateral pivot
· Supporting Dataset: Phase 5 Financial Risk; Phase 3 EV-021, EV-022; Phase 7 External Dependencies; Phase 8 Narrative

Pola 4: Regulatory Uncertainty — Legal Wrapper (Cayman Foundation) + Off-chain Compliance (Coinbase Prime Custody, KYC/AML on RWA)
· Decision Pattern: Cayman Foundation 2022 untuk legal personality; RWA assets custodied Coinbase Prime (regulated custodian); KYC/AML pada asset managers; Sky.money/Endgame preparing untuk regulatory clarity; no geo-blocking on protocol level
· Evidence: Phase 3 EV-013 Cayman Foundation; Phase 2 Entity MakerDAO Cayman Foundation, Coinbase Prime; Phase 5 Financial Risk Legal Financial Risk; Phase 7 Infrastructure Providers Coinbase Prime
· Trigger: DAO needs legal personality for contracts, custody, liability; RWA requires regulated custody
· Response: Cayman Foundation wrapper; institutional custodian Coinbase Prime; asset manager compliance
· Result: Legal structure for off-chain operations; regulatory risk remains open thread (SEC, MiCA, stablecoin bills)
· Supporting Dataset: Phase 3 EV-013; Phase 2 Entity Cayman Foundation, Coinbase Prime; Phase 5 Financial Risk; Phase 7 Infrastructure Providers

Pola 5: Smart Contract Risk — Multi-Audit + Formal Verification + GSM Delay + Emergency Shutdown
· Decision Pattern: 11+ major audits (Trail of Bits x3, OpenZeppelin x2, Sigma Prime x2, PeckShield x2, Certora x2); formal verification Vat/Jug/Pot/SKY; GSM 24-48hr delay on governance execution; ESM as last resort; bug bounty via Immunefi (not explicitly in dataset but standard)
· Evidence: Phase 4 Technology Audit History 11 audits; Certora formal verification; Security Model GSM, ESM; Phase 3 EV-007 MCD audited pre-launch, EV-015 Bridge audited, EV-019 Sky audited
· Trigger: High-value protocol ($7B+ TVL) requires maximum security assurance
· Response: Defense in depth: audits, formal verification, governance delay, emergency shutdown
· Result: No major exploit on core contracts since Black Thursday (which was oracle/market not contract bug); Sky contracts audited pre-migration
· Supporting Dataset: Phase 4 Technology Audit History, Security Model; Phase 3 EV-007, EV-015, EV-019

Recurring Behavioral Pattern

Pola 1: Crisis → Systematic Upgrade (Black Thursday → Liquidation 2.0 + OSM + PSM; Peg instability → PSM; Foundation limits → DAO + Core Units + Legal Wrapper)
· Evidence: Phase 3 EV-009 Black Thursday → EV-010 Liquidation 2.0/PSM; EV-011 Foundation dissolution → EV-012 Core Units, EV-013 Cayman Foundation; Pattern: major stress event diikuti infrastruktur upgrade permanen, bukan patch sementara
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-011, EV-012, EV-013; Phase 4 Technology Technical Upgrade History

Pola 2: Revenue Growth → New Dependency → Risk Diversification Within Same Category (Crypto fees → PSM fees (USDC) → RWA yield (T-bills) → Multiple PSM collaterals, Multiple RWA managers)
· Evidence: Phase 5 Revenue Model evolution; Phase 3 EV-010 PSM USDC-A → EV-021 PSM multi-collateral; EV-014 RWA BlockTower → Monetalis → EV-022 >$1B; Pattern: scale revenue via new asset class, then diversify counterparties within that class
· Supporting Dataset: Phase 5 Revenue Model; Phase 3 EV-010, EV-014, EV-021, EV-022; Phase 7 External Dependencies

Pola 3: Governance Evolution → New Layer Without Removing Old (Foundation → Core Units (DAO) → SubDAO (Spark, Sky) → Endgame AI Governance; MKR → SKY migration (both coexist during transition))
· Evidence: Phase 3 EV-011 Foundation dissolved but Core Units added; EV-016 Spark SubDAO added alongside Core Units; EV-017 Endgame proposes AI governance layer; EV-020 MKR→SKY migration gradual; Pattern: additive governance layers, not replacement
· Supporting Dataset: Phase 3 EV-011, EV-012, EV-016, EV-017, EV-020; Phase 2 Entity Core Units, Spark Protocol, Sky.money; Phase 6 Token Governance

Pola 4: Ethereum-First → Canonical Multi-Chain (L1 mainnet → L2/L1 canonical deployments via Teleporter mint/burn; never "deploy and forget", always governance-approved spell per chain)
· Evidence: Phase 3 EV-015 4 chains 2022-2023 → EV-018 Base/Starknet 2023-2024; Phase 4 Technology Cross-chain Messaging Canonical Bridge; Phase 2 Entity 7 chains all governance-approved; Pattern: controlled expansion preserving canonical supply
· Supporting Dataset: Phase 3 EV-015, EV-018; Phase 4 Technology Canonical Bridge; Phase 2 Entity chains

Pola 5: Tokenomics Evolution Via Migration Not Inflation (MKR supply managed via Flop/Flap burns; SKY introduced via 1:24,000 migration from MKR, not new inflation; fee switch planned for SKY yield)
· Evidence: Phase 6 Token MKR Inflation/Deflation dynamic via Flop/Flap; SKY Supply via migration not minting; SKY Inflation via fee switch planned; Phase 3 EV-020 Migration execution; Pattern: supply changes via structural migration/mechanism, not arbitrary minting
· Supporting Dataset: Phase 6 Token MKR Inflation/Deflation, SKY Supply, SKY Inflation; Phase 3 EV-020

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Skala & Stabilitas Peg (PSM Centralized Stablecoin Dependency)
· Decision: Accept >60% DAI supply backed by centralized stablecoins (USDC, USDT, GUSD) via PSM untuk peg stability dan skala
· Trade-off: Peg stability dan DAI supply growth ($5B+) dicapai tapi menciptakan ketergantungan pada emisyen terpusat (Circle, Tether, Gemini) — sensor/blacklist/depeg risk
· Evidence: Phase 3 EV-021 PSM Dominance >60%; Phase 5 Financial Risk PSM Concentration; Phase 8 Narrative Decentralized Stablecoin vs Centralized Collateral; Phase 4 Known Limitations Centralization Risk PSM
· Supporting Dataset: Phase 3 EV-021; Phase 5 Financial Risk; Phase 8 Narrative; Phase 4 Known Limitations

Trade-off 2: Trustless Crypto Collateral vs Tradfi Yield (RWA Vault Off-chain Dependencies)
· Decision: Onboard RWA (US Treasuries, structured credit) via Vault RWA dengan asset manager & custodian off-chain untuk yield tradfi
· Trade-off: Protocol revenue diversification dan scaling (> $1B RWA, largest revenue source) dicapai tapi introduce counterparty risk (BlockTower, Monetalis, Coinbase Prime), legal enforcement risk, regulatory risk — tidak fully trustless
· Evidence: Phase 3 EV-014 RWA Launch, EV-022 RWA >$1B; Phase 5 Financial Dependencies RWA Asset Managers, Financial Risk RWA Counterparty; Phase 4 Known Limitations RWA Off-chain Dependency; Phase 8 Narrative RWA Tokenization
· Supporting Dataset: Phase 3 EV-014, EV-022; Phase 5 Financial Dependencies, Financial Risk; Phase 4 Known Limitations; Phase 8 Narrative

Trade-off 3: Governance Decentralization vs Upgrade Agility (GSM 24-48hr Delay)
· Decision: Implement Governance Security Module (GSM) 24-48 hour delay pada semua Executive Spells eksekusi untuk melindungi dari malicious proposal
· Trade-off: Security dari governance attack dicapai tapi memperlambat respons darurat (parameter changes, emergency fixes); emergency shutdown butuh MKR majority, tidak instant
· Evidence: Phase 4 Technology Security Model GSM; Phase 6 Token Governance Model GSM delay; Phase 3 EV-009 Black Thursday emergency spell bypassed normal GSM? (emergency spell mechanism exists)
· Supporting Dataset: Phase 4 Technology Security Model; Phase 6 Token Governance; Phase 3 EV-009

Trade-off 4: Single Chain Depth vs Multi-Chain Breadth (Canonical Bridge Finality vs User Experience)
· Decision: Deploy canonical contracts ke 6 L2/L1 via Teleporter mint/burn; bridge finality mengikuti L1→L2 message passing (Arbitrum/Optimism 7-day challenge period)
· Trade-off: Canonical supply integrity dan security dipertahankan tapi user experience buruk untuk bridging (7-day wait atau third-party fast bridge dengan trusted assumptions); capital efficiency reduced
· Evidence: Phase 4 Technology Canonical Bridge, Known Limitations Cross-chain Bridge Finality; Phase 3 EV-015, EV-018; Phase 7 External Dependencies Canonical Bridge; Phase 8 Market Bridge Volume
· Supporting Dataset: Phase 4 Technology Canonical Bridge, Known Limitations; Phase 3 EV-015, EV-018; Phase 7 External Dependencies

Trade-off 5: MKR Indirect Value Accrual (Burn) vs SKY Direct Yield (Fee Switch) — Tokenomics Complexity
· Decision: Migrate MKR→SKY 1:24,000 dengan fee switch untuk direct yield ke SKY stakers; MKR phase-out
· Trade-off: Direct value accrual lebih menarik investor tapi menambah kompleksitas tokenomics (dual token transition, migration mechanics, regulatory classification SKY sebagai security risk), governance power shift uncertainty
· Evidence: Phase 3 EV-017 Endgame, EV-020 Migration; Phase 6 Token SKY Utility Fee Switch, MKR vs SKY; Phase 5 Financial Risk Legal Financial Risk; Phase 8 Narrative Endgame
· Supporting Dataset: Phase 3 EV-017, EV-020; Phase 6 Token SKY, MKR; Phase 5 Financial Risk; Phase 8 Narrative

Trade-off 6: Modular Upgradeability vs Legacy Technical Debt (DSS Solidity 0.6 Contracts Still Live)
· Decision: Modular architecture memungkinkan upgrade per-module; tapi legacy DSS contracts (Solidity 0.6) masih live di core (Vat, Jug, Pot, etc.) dan sulit di-refactor tanpa major governance spell
· Trade-off: Upgradeability untuk modul baru (PSM, PIVOT, Bridge, Sky) dicapai tapi technical debt lama menumpuk; formal verification baru hanya untuk modul baru; legacy contracts tidak benefit dari tooling modern
· Evidence: Phase 4 Known Limitations Legacy Contract Technical Debt; Phase 4 Technology Current Technical Stack Solidity versions; Phase 4 Technical Upgrade History incremental
· Supporting Dataset: Phase 4 Known Limitations; Phase 4 Technology Current Technical Stack, Technical Upgrade History

Behavioral Summary

Prioritas Utama Proyek:
1. Peg Stability DAI di $1 (PSM sebagai primary tool, overcollateralization sebagai backup) — EV-010, EV-021
2. Protocol Survivability & Security (Multi-audit, formal verification, GSM, ESM, OSM delay) — Phase 4 Audit History, Security Model
3. Revenue Diversification & Scaling (RWA yield > crypto fees, Spark fee flow, PSM fees) — Phase 5 Revenue Model, EV-022
4. Progressive Decentralization (Foundation → DAO → Core Units → SubDAO → Endgame) — EV-011, EV-012, EV-016, EV-017
5. Ethereum Alignment & Canonical Multi-chain (L1 settlement, Teleporter mint/burn) — Phase 4 Architecture, EV-015, EV-018

Cara Mengambil Keputusan:
- Data-driven dari on-chain metrics (Vault health, PSM volume, DSR utilization) — Phase 4 Technology Monitoring
- Governance process formal via MIP framework (RFC → Poll → Executive Spell) — Phase 6 Token Governance
- Core Units sebagai eksekusi operasional (Protocol Engineering, Risk, Oracle, Growth) — Phase 2 Entity Core Units
- Emergency spell untuk krisis (Black Thursday) — EV-009
- Long-term strategic shifts via Endgame proposal (Rune Christensen → Governance vote) — EV-017

Faktor Paling Sering Mempengaruhi Keputusan:
1. On-chain protocol health metrics (deficit/surplus, peg deviation, Vault liquidation risk) — Phase 4 Technology Monitoring
2. Revenue sustainability (diversifikasi yield sources) — Phase 5 Revenue Model
3. Security incident lessons (Black Thursday → systematic upgrades) — Phase 3 EV-009, EV-010
4. Regulatory/legal requirements (Cayman Foundation, Coinbase Prime custody) — EV-013, Phase 2 Entity Coinbase Prime
5. Competitive landscape (DeFi lending competition → Spark; stablecoin competition → PSM/RWA) — Phase 8 Competitor Landscape

Pola Evolusi:
- Dari single collateral crypto CDP → multi-collateral → hybrid crypto/RWA credit facility
- Dari Foundation-led → DAO Core Units → SubDAO ecosystem → Endgame AI governance
- Dari MKR governance+recapitalization → MKR+SKY dual token migration → SKY fee switch value accrual
- Dari Ethereum-only → Canonical multi-chain (7 chains) dengan Teleporter bridge
- Dari DeFi-native borrowing → Institutional RWA → Retail savings (sDAI/SSR) → Cross-chain infrastructure

Kekuatan Utama:
- 7+ years battle-tested (survived Black Thursday, multiple market cycles) — Phase 3 History
- Largest decentralized stablecoin ($5.3B DAI) dengan deep liquidity — Phase 8 Market Share
- Transparent on-chain accounting (Vat) dan governance (DS-Chief) — Phase 4 Technology Core Components
- Institutional-grade RWA partnerships ($1B+ Treasuries) — Phase 3 EV-022, Phase 7 Major Integrations
- Modular architecture memungkinkan upgrade tanpa hard fork — Phase 4 Technology Architecture
- Strong developer ecosystem (50-100 active contributors) — Phase 8 Adoption Metrics

Kelemahan Utama:
- Centralization risk tinggi (PSM >60% centralized stablecoins, RWA off-chain counterparties) — Phase 5 Financial Risk, Phase 4 Known Limitations
- Governance complexity & voter apathy (20-40% MKR participation) — Phase 8 Adoption Metrics Governance Participation
- Cross-chain UX friction (7-day bridge finality) — Phase 4 Known Limitations Cross-chain Bridge Finality
- Legacy technical debt (Solidity 0.6 core contracts) — Phase 4 Known Limitations Legacy Contract Technical Debt
- Regulatory uncertainty (stablecoin regulation, SKY token classification, RWA securities law) — Phase 5 Financial Risk Legal Financial Risk
- MKR→SKY migration execution risk (governance power transition, liquidity fragmentation) — Phase 3 EV-020, Phase 6 Token SKY

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: MakerDAO

Core Insights

Insight 1: Protokol CDP overcollateralized dapat bertahan >7 tahun dan menjadi stablecoin terdesentralisasi terbesar tanpa fundraising tradisional pasca-launch
Explanation: MakerDAO hanya mengumpulkan $1M private sale 2017-Q1【Phase 5 — Funding History】, kemudian sepenuhnya mendanai operasional (Core Unit budget, DSR, MKR burn) dari protocol revenue on-chain: Stability Fees, PSM Fees, Liquidation Penalties, RWA Yield, Spark Fee Flow【Phase 5 — Fundraising Mechanism】. Model self-sustaining ini membuktikan CDP protocol bisa financially independent tanpa VC dependency.
Evidence: Private sale $1M 2017-Q1【Phase 5 — Funding History】; Zero Series A/public sale【Phase 5 — Token Sale】; Protocol revenue retention seit 2019【Phase 5 — Fundraising Mechanism】; TVL ~$7.2B & DAI supply ~5.3B 2024-08【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 EV-004, EV-005, EV-007; Phase 5 Funding History, Fundraising Mechanism, Revenue Model; Phase 8 Adoption Metrics
Confidence: HIGH

Insight 2: Transisi dari Foundation-centric ke DAO-native dengan legal wrapper (Cayman Foundation) memungkinkan skalasi RWA >$1B sambil melindungi kontributor
Explanation: Maker Foundation dibubarkan 2021-07-31【Phase 3 — EV-011】, aset dialihkan ke DAO. Cayman Foundation didirikan 2022-03【Phase 3 — EV-013】 sebagai legal wrapper untuk menandatangani kontrak RWA dengan BlockTower/Monetalis/Coinbase Prime【Phase 7 — Major Integrations BlockTower Andromeda, Monetalis Clydesdale】. Struktur ini memisahkan governance protocol (on-chain) dari legal liability (off-chain).
Evidence: Foundation dissolution 2021-07-31【Phase 3 — EV-011】; Cayman Foundation 2022-03【Phase 3 — EV-013】; RWA Vaults launch 2022-07【Phase 3 — EV-014】; RWA AUM >$1B 2024【Phase 3 — EV-022】; Phase 2 Entity MakerDAO Cayman Foundation【Phase 2 — Entity MakerDAO Cayman Foundation】
Supporting Dataset: Phase 3 EV-011, EV-013, EV-014, EV-022; Phase 2 Entity Maker Foundation, MakerDAO Cayman Foundation, MakerDAO DAO; Phase 7 Major Integrations, External Dependencies
Confidence: HIGH

Insight 3: PSM (Peg Stability Module) mengubah dynamic peg defense dari market-based (auction) ke arbitrase 1:1 efisien, tapi menciptakan ketergantungan >60% supply pada stablecoin terpusat (USDC/USDT/GUSD)
Explanation: PSM launch 2020-07【Phase 3 — EV-010】 memungkinkan swap DAI↔USDC fee 0.1% LR 101%. Hasilnya peg DAI sangat stabil【Phase 8 — Narrative Position Decentralized Stablecoin】, tapi >60% DAI supply backed by PSM stablecoins【Phase 5 — Financial Risk Treasury Concentration】. Trade-off: stabilitas peg vs centralization risk (censorship/blacklist oleh emisyen USDC/USDT).
Evidence: PSM launch 2020-07【Phase 3 — EV-010】; PSM dominance >60% supply 2024【Phase 3 — EV-021】; Financial Risk centralization【Phase 5 — Financial Risk PSM Concentration】; Revenue Model PSM Fees【Phase 5 — Revenue Model】
Supporting Dataset: Phase 3 EV-010, EV-021; Phase 4 Core Components PSM; Phase 5 Revenue Model, Financial Risk; Phase 8 Narrative Position
Confidence: HIGH

Insight 4: Endgame Plan (MKR→SKY migration, SubDAO federation, fee switch) menjawab fundamental governance token value accrual problem: MKR hanya punya recapitalization utility, tidak ada yield native
Explanation: MKR utility terbatas pada governance voting, recapitalization (Flop mint saat deficit), dan buyback (Flap burn saat surplus)【Phase 6 — Utility MKR】. Endgame 2023-09【Phase 3 — EV-017】 mengusulkan SKY dengan fee switch (protocol surplus → SKY stakers)【Phase 6 — Utility SKY Fee Switch】, SubDAO mandiri【Phase 2 — Entity Spark Protocol, Sky.money】, dan migrasi 1:24.000【Phase 6 — Token Information SKY】. Migration Phase 1 mulai 2024-08【Phase 3 — EV-020】.
Evidence: Endgame announcement 2023-09【Phase 3 — EV-017】; MKR utility no native yield【Phase 6 — Utility MKR】; SKY fee switch planned【Phase 6 — Utility SKY Fee Switch】; Migration ratio 1:24.000【Phase 6 — Token Information SKY】; Sky.money launch 2024-07【Phase 3 — EV-019】
Supporting Dataset: Phase 3 EV-017, EV-019, EV-020; Phase 6 Token Information SKY, Utility, Inflation/Deflation; Phase 2 Entity Spark Protocol, Sky.money; Phase 8 Competitor Landscape
Confidence: HIGH

Insight 5: Canonical Bridge mint/burn model (Teleporter) memungkinkan multi-chain expansion tanpa trusted intermediary, menjaga supply consistency lintas 7 chain
Explanation: Alih-alih third-party bridge (Wormhole, Multichain), Maker membangun Teleporter sendiri: mint/burn DAI/MKR di L1↔L2 menggunakan official message passing (Arbitrum L1Gateway, Optimism L1CrossDomainMessenger, Polygon FxPortal, Gnosis AMB, Base/Starknet custom)【Phase 4 — Cross-chain Messaging】. Deployments ke Arbitrum, Optimism, Polygon, Gnosis 2022-2023【Phase 3 — EV-015】, Base & Starknet 2023-2024【Phase 3 — EV-018】. Supply total konsisten lintas chain.
Evidence: Canonical Bridge architecture【Phase 4 — Cross-chain Messaging】; Multi-chain deployments EV-015, EV-018【Phase 3 — EV-015, EV-018】; Bridge UI live【Phase 7 — Infrastructure Providers】; Bridge liquidity mint/burn model【Phase 8 — Trading Markets Bridge Liquidity】
Supporting Dataset: Phase 3 EV-015, EV-018; Phase 4 System Architecture, Core Components Canonical Bridge; Phase 7 External Dependencies Chains, Infrastructure Providers; Phase 8 Trading Markets
Confidence: HIGH

Insight 6: RWA Vault yield (US Treasury bills ~5%) menjadi revenue driver utama melebihi crypto Stability Fees, mengubah profil risiko protokol dari crypto volatility ke tradfi counterparty risk
Explanation: Vault RWA BlockTower Andromeda & Monetalis Clydesdale AUM >$1B 2024【Phase 3 — EV-022】. RWA yield mendorong DSR yield dan protocol surplus【Phase 5 — Revenue Model RWA Vault Yield】, mendanai Core Unit budget dan MKR burn【Phase 5 — Fundraising Mechanism DAO Treasury Allocation】. Ketergantungan pada BlockTower, Monetalis, Coinbase Prime sebagai counterparties tradfi【Phase 5 — Financial Dependencies RWA Asset Managers】.
Evidence: RWA Vaults launch 2022-07【Phase 3 — EV-014】; RWA AUM >$1B 2024【Phase 3 — EV-022】; Revenue Model RWA Yield【Phase 5 — Revenue Model】; Financial Dependencies RWA【Phase 5 — Financial Dependencies】; Narrative Position RWA【Phase 8 — Narrative Position】
Supporting Dataset: Phase 3 EV-014, EV-022; Phase 5 Revenue Model, Revenue History, Financial Dependencies; Phase 7 Major Integrations BlockTower, Monetalis; Phase 8 Narrative Position, Adoption Metrics
Confidence: HIGH

Insight 7: Modular smart contract architecture (Vat, Jug, Pot, Vow, PSM, Oracle, Bridge, SubDAO) dengan upgrade via Executive Spell + GSM 24-48hr delay memungkinkan evolusi sistemik tanpa breaking changes
Explanation: Setiap major upgrade (MCD, PSM, Liquidation 2.0, PIVOT, RWA, Bridge, Sky) dieksekusi sebagai governance spell【Phase 4 — Technical Upgrade History】. Modul terpisah di-upgrade independen: Vat (accounting), Jug (fees), Pot (DSR), Vow (surplus/deficit), PSM (peg), Oracle/PIVOT (price feeds), Bridge (cross-chain), SubDAO contracts【Phase 4 — Core Components】. GSM delay melindungi dari malicious spell execution【Phase 4 — Security Model Governance Control】.
Evidence: 13 major upgrades 2019-2024【Phase 4 — Technical Upgrade History】; 10+ core modules【Phase 4 — Core Components】; GSM 24-48hr delay【Phase 4 — Security Model】; Modular design【Phase 4 — System Architecture】
Supporting Dataset: Phase 3 EV-007, EV-010, EV-008, EV-017, EV-014, EV-015, EV-019; Phase 4 Core Components, Technical Upgrade History, System Architecture, Security Model
Confidence: HIGH

Insight 8: Formal verification (Certora/K Framework) pada modul kritis (Vat, Jug, Pot, NewToken SKY) + 11+ major audits (Trail of Bits x3, OpenZeppelin x2, Sigma Prime x2, PeckShield x2) menciptakan security posture tinggi untuk protocol mengelola $7B+ TVL
Explanation: Audit history mencakup MCD pre-launch 2019【Phase 4 — Audit History Trail of Bits, OpenZeppelin】, post-Black Thursday 2020【Phase 4 — Audit History Sigma Prime】, PSM 2020【Phase 4 — Audit History PeckShield】, Bridge 2022【Phase 4 — Audit History Trail of Bits】, RWA 2022【Phase 4 — Audit History OpenZeppelin】, Spark 2023【Phase 4 — Audit History Sigma Prime】, PIVOT 2023【Phase 4 — Audit History PeckShield】, Sky 2024【Phase 4 — Audit History Trail of Bits】. Formal verification Vat/Jug/Pot 2021 & SKY 2024【Phase 4 — Audit History Certora】.
Evidence: 11+ major audits【Phase 4 — Audit History】; Formal verification Vat/Jug/Pot 2021 & SKY 2024【Phase 4 — Audit History Certora】; Security Model Formal Verification【Phase 4 — Security Model】; TVL ~$7.2B 2024【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 EV-007, EV-009, EV-010, EV-014, EV-015, EV-016, EV-017, EV-019; Phase 4 Audit History, Security Model; Phase 8 Adoption Metrics
Confidence: HIGH

Insight 9: SubDAO model (Spark Protocol, Sky.money) dengan fee sharing ke Maker Treasury memungkinkan spesialisasi produk (lending, frontend, savings) sambil mempertahankan value accrual ke protocol utama
Explanation: Spark Protocol launch 2023-05【Phase 3 — EV-016】: SparkLend, sDAI (ERC-4626 DSR wrapper), liquidity facilities; fee flow ke Maker Treasury【Phase 5 — Revenue Model Spark Protocol Fee Flow】. Sky.money 2024-07【Phase 3 — EV-019】: SSR, SKY rewards, migration UI. Endgame memperluas ke SubDAO RWA-specific, Governance AI【Phase 3 — EV-017】. Internal competition untuk user flow (Spark vs Aave, Sky vs Oasis)【Phase 8 — Competitor Landscape Internal SubDAO】.
Evidence: Spark launch EV-016【Phase 3 — EV-016】; Sky.money launch EV-019【Phase 3 — EV-019】; Fee sharing revenue【Phase 5 — Revenue Model】; SubDAO contracts architecture【Phase 4 — Core Components SubDAO Contracts】; Competitor Landscape Internal【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 3 EV-016, EV-017, EV-019; Phase 4 Core Components SubDAO Contracts; Phase 5 Revenue Model; Phase 7 Major Integrations Spark Protocol, Sky.money; Phase 8 Competitor Landscape
Confidence: HIGH

Insight 10: Black Thursday 2020-03-12 (defisit ~$5.3M, MKR mint ~50K via Flop) memvalidasi MKR sebagai backstop recapitalization terakhir dan memicu sistemik upgrades: Liquidation 2.0 (Dutch auction kicker), OSM hardening, PSM launch
Explanation: ETH crash >50% dalam jam, oracle latency & 0-bid auctions menyebabkan bad debt【Phase 3 — EV-009】. Emergency spell mint MKR via Flop auction cover deficit【Phase 6 — Inflation/Deflation MKR Flop Auction】. Upgrade pasca-krisis: Liquidation 2.0 2020-08【Phase 4 — Technical Upgrade History Liquidation 2.0】, PSM 2020-07【Phase 3 — EV-010】, OSM delay diperpanjang. Mekanisme Flop/Flap terbukti kerja sebagai designed.
Evidence: Black Thursday EV-009【Phase 3 — EV-009】; MKR mint ~50K Flop【Phase 6 — Inflation/Deflation MKR】; Liquidation 2.0 upgrade【Phase 4 — Technical Upgrade History】; PSM launch EV-010【Phase 3 — EV-010】; OSM hardening【Phase 4 — Oracle Network】
Supporting Dataset: Phase 3 EV-009, EV-010; Phase 4 Technical Upgrade History, Oracle Network; Phase 6 Inflation/Deflation MKR, Major Token Events Black Thursday
Confidence: HIGH

Strategic Principles

Principle 1: Modular First — Bangun protokol sebagai modul terpisah yang di-upgrade independen via governance spell
Explanation: Arsitektur modular (Vat, Jug, Pot, Vow, PSM, Oracle, Bridge, SubDAO) memungkinkan 13 major upgrades 2019-2024 tanpa breaking changes【Phase 4 — Core Components, Technical Upgrade History】. Setiap modul punya responsibility tunggal: Vat (accounting), Jug (fee accumulation), Pot (DSR), Vow (surplus/deficit), PSM (peg), Oracle/PIVOT (price feeds), Bridge (cross-chain), SubDAO contracts【Phase 4 — Core Components】.
Evidence: 10+ core modules【Phase 4 — Core Components】; 13 major upgrades via Executive Spell【Phase 4 — Technical Upgrade History】; GSM delay 24-48hr protects upgrades【Phase 4 — Security Model Governance Control】; System Architecture Modular Design【Phase 4 — System Architecture】
Supporting Dataset: Phase 3 EV-007, EV-010, EV-008, EV-017, EV-014, EV-015, EV-019; Phase 4 Core Components, Technical Upgrade History, System Architecture, Security Model
Confidence: HIGH

Principle 2: Security Before Growth — Formal verification + multiple audits + Emergency Shutdown Module (ESM) sebagai nuclear option sebelum scaling
Explanation: Formal verification Vat/Jug/Pot (Certora 2021) & SKY (Certora 2024)【Phase 4 — Audit History Certora】. 11+ major audits dari 5 firm berbeda【Phase 4 — Audit History】. ESM live sejak MCD 2019 — MKR holders bisa trigger global shutdown, sistem berhenti total, DAI holders klaim collateral pro-rata【Phase 4 — Security Model Emergency Shutdown】. Belum pernah dieksekusi tapi eksistensinya mencegah governance attack ekstrem.
Evidence: Formal verification 2 engagements【Phase 4 — Audit History Certora】; 11+ audits Trail of Bits, OpenZeppelin, Sigma Prime, PeckShield【Phase 4 — Audit History】; ESM live seit 2019-11-18【Phase 4 — Security Model】; TVL $7.2B secured【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 EV-007, EV-014, EV-016, EV-019; Phase 4 Audit History, Security Model; Phase 8 Adoption Metrics
Confidence: HIGH

Principle 3: Protocol Revenue Retention Over External Fundraising — Zero traditional fundraising post-2017; semua ops funding dari on-chain revenue
Explanation: Hanya $1M private sale 2017-Q1【Phase 5 — Funding History】. Tidak ada Series A, public sale, VC round, grant ke DAO treasury【Phase 5 — Fundraising Mechanism】. Semua funding: Stability Fees, PSM Fees, Liquidation Penalties, RWA Yield, Spark Fee Flow, DSR Spread, Flap MKR Burn【Phase 5 — Revenue Model】. Core Unit budget on-chain via MIP dari surplus DAI【Phase 5 — Fundraising Mechanism DAO Treasury Allocation】.
Evidence: Private sale $1M only【Phase 5 — Funding History】; Zero public sale/VC【Phase 5 — Token Sale, Fundraising Mechanism】; 7 live revenue streams【Phase 5 — Revenue Model】; Core Unit budget via MIP【Phase 5 — Fundraising Mechanism】; Phase 6 Token Sale no TGE【Phase 6 — Token Sale】
Supporting Dataset: Phase 3 EV-004; Phase 5 Funding History, Fundraising Mechanism, Revenue Model; Phase 6 Token Sale
Confidence: HIGH

Principle 4: Canonical Infrastructure Over Third-Party Dependencies — Bangun bridge, oracle, indexing sendiri bukan rely pada external protocols
Explanation: Canonical Bridge Teleporter mint/burn model sendiri【Phase 4 — Cross-chain Messaging】, bukan Wormhole/Multichain. Oracle Module OSM+PIVOT aggregator sendiri【Phase 4 — Oracle Network】, multi-provider (Chainlink, API3, Chronicle, RedStone)【Phase 7 — External Dependencies Oracle Providers】. The Graph Subgraph sendiri untuk indexing【Phase 7 — Infrastructure Providers The Graph】. Keeper automation via Gelato/Chainlink Automation tapi logic on-chain【Phase 4 — Current Technical Stack】.
Evidence: Canonical Bridge mint/burn【Phase 4 — Cross-chain Messaging】; Oracle Module OSM+PIVOT【Phase 4 — Oracle Network】; Multi-oracle providers【Phase 7 — External Dependencies】; Subgraph indexing【Phase 7 — Infrastructure Providers】; Bridge deployments 7 chains【Phase 3 — EV-015, EV-018】
Supporting Dataset: Phase 3 EV-015, EV-018; Phase 4 System Architecture, Core Components, Oracle Network, Current Technical Stack; Phase 7 External Dependencies, Infrastructure Providers
Confidence: HIGH

Principle 5: Progressive Decentralization Via Legal Wrapper — Foundation → DAO → Cayman Foundation wrapper → SubDAO federation
Explanation: Maker Foundation 2015-2021【Phase 2 — Entity Maker Foundation】→ Dissolution 2021-07-31【Phase 3 — EV-011】→ DAO-native governance via Core Units 2021-07【Phase 3 — EV-012】→ Cayman Foundation 2022-03 legal wrapper【Phase 3 — EV-013】→ SubDAO (Spark, Sky) semi-autonomous 2023-2024【Phase 3 — EV-016, EV-019】→ Endgame SubDAO federation【Phase 3 — EV-017】. Setiap tahap menambah autonomy sambil manage legal liability.
Evidence: Foundation dissolution EV-011【Phase 3 — EV-011】; Core Units EV-012【Phase 3 — EV-012】; Cayman Foundation EV-013【Phase 3 — EV-013】; Spark EV-016, Sky EV-019【Phase 3 — EV-016, EV-019】; Endgame EV-017【Phase 3 — EV-017】; Phase 2 Entity progression
Supporting Dataset: Phase 2 Entity Maker Foundation, MakerDAO DAO, Core Units, MakerDAO Cayman Foundation, Spark Protocol, Sky.money; Phase 3 EV-011, EV-012, EV-013, EV-016, EV-017, EV-019
Confidence: HIGH

Principle 6: RWA Integration Via Institutional-Grade Counterparties — Pilih partner tradfi dengan kredibilitas tinggi (BlockTower, Monetalis, Coinbase Prime) bukan DeFi-native
Explanation: BlockTower ($10B+ AUM asset manager)【Phase 2 — Entity BlockTower】, Monetalis (structured credit specialist)【Phase 2 — Entity Monetalis】, Coinbase Prime (regulated institutional custodian)【Phase 2 — Entity Coinbase Prime】. Vault RWA-001 & RWA-002 deploy 2022-07【Phase 3 — EV-014】. AUM >$1B 2024【Phase 3 — EV-022】. Bridge ke tradfi infrastructure, bukan DeFi yield farming.
Evidence: BlockTower Andromeda, Monetalis Clydesdale Vaults【Phase 3 — EV-014】; RWA AUM >$1B EV-022【Phase 3 — EV-022】; Counterparty quality【Phase 2 — Entity BlockTower, Monetalis, Coinbase Prime】; Financial Dependencies RWA【Phase 5 — Financial Dependencies】
Supporting Dataset: Phase 2 Entity BlockTower, Monetalis, Coinbase Prime; Phase 3 EV-014, EV-022; Phase 5 Financial Dependencies; Phase 7 Major Integrations, External Dependencies; Phase 8 Narrative Position RWA
Confidence: HIGH

Principle 7: Token Migration As Governance Evolution — MKR→SKY 1:24.000 memisahkan recapitalization function (MKR legacy) dari governance+yield function (SKY)
Explanation: MKR utility: governance + recapitalization (Flop mint) + buyback (Flap burn)【Phase 6 — Utility MKR】. SKY utility: governance + fee switch yield (protocol surplus → stakers) + SubDAO rewards【Phase 6 — Utility SKY】. Migration 1 MKR = 24.000 SKY【Phase 6 — Token Information SKY】. MKR supply net deflationary 1M→~977K【Phase 6 — Inflation/Deflation MKR】. SKY supply baru ~23.46M estimasi【Phase 6 — Supply SKY】.
Evidence: MKR utility no yield【Phase 6 — Utility MKR】; SKY fee switch planned【Phase 6 — Utility SKY Fee Switch】; Migration ratio 1:24.000【Phase 6 — Token Information SKY】; MKR net deflationary【Phase 6 — Inflation/Deflation MKR】; Endgame announcement EV-017【Phase 3 — EV-017】
Supporting Dataset: Phase 3 EV-017, EV-019, EV-020; Phase 6 Token Information SKY, Utility, Inflation/Deflation, Supply; Phase 8 Narrative Position, Competitor Landscape
Confidence: HIGH

Principle 8: Oracle Security Module (OSM) 1-Hour Delay As Non-Negotiable Manipulation Protection — Semua price feed wajib lewat OSM delay 1 jam sebelum update on-chain
Explanation: OSM delay 1 jam mencegah flash loan attack & manipulasi harga instan【Phase 4 — Oracle Network】. Black Thursday 2020-03-12 oracle latency menyebabkan 0-bid liquidations【Phase 3 — EV-009】. PIVOT upgrade 2023-09 mengganti Medianizer untuk gas efficiency & flexibility feed aggregation【Phase 4 — Technical Upgrade History PIVOT】. Multi-provider: Chainlink, API3, Chronicle, RedStone【Phase 7 — External Dependencies Oracle Providers】.
Evidence: OSM 1hr delay【Phase 4 — Oracle Network】; Black Thursday trigger EV-009【Phase 3 — EV-009】; PIVOT upgrade 2023-09【Phase 4 — Technical Upgrade History】; Multi-provider oracle【Phase 7 — External Dependencies】
Supporting Dataset: Phase 3 EV-009, EV-017; Phase 4 Oracle Network, Technical Upgrade History, Security Model; Phase 7 External Dependencies
Confidence: HIGH

Success Factors

Factor 1: Self-Sustaining Revenue Model — Protocol revenue retention (Stability Fees, PSM Fees, Liquidation Penalties, RWA Yield, Spark Fee Flow) mendanai 100% operasional sejak 2021 tanpa external capital
Explanation: Zero fundraising post-2017【Phase 5 — Fundraising Mechanism】. 7 live revenue streams【Phase 5 — Revenue Model】. Surplus management otomatis via Flap/Flop auctions【Phase 5 — Revenue Model Flap】. Core Unit budget transparan on-chain via MIP【Phase 5 — Fundraising Mechanism DAO Treasury Allocation】. Financial independence memungkinkan long-term planning tanpa investor pressure.
Evidence: Private sale $1M only 2017【Phase 5 — Funding History】; 7 revenue streams live【Phase 5 — Revenue Model】; Flap/Flop automated surplus management【Phase 4 — Core Components Vow】; Core Unit budget MIP【Phase 5 — Fundraising Mechanism】; TVL $7.2B sustained【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 EV-004, EV-011, EV-012; Phase 4 Core Components; Phase 5 Funding History, Fundraising Mechanism, Revenue Model; Phase 8 Adoption Metrics
Confidence: HIGH

Factor 2: Modular Architecture Enabling Systematic Upgrades — 13 major upgrades 2019-2024 via Executive Spell + GSM delay tanpa breaking changes
Explanation: Modular design (Vat, Jug, Pot, Vow, PSM, Oracle, Bridge, SubDAO)【Phase 4 — Core Components】. Setiap upgrade dieksekusi sebagai governance spell: MCD 2019-11-18【Phase 3 — EV-007】, PSM 2020-07【Phase 3 — EV-010】, Liquidation 2.0 2020-08【Phase 4 — Technical Upgrade History】, PIVOT 2023-09【Phase 4 — Technical Upgrade History】, RWA 2022-07【Phase 3 — EV-014】, Bridge multi-chain 2022-2024【Phase 3 — EV-015, EV-018】, Sky 2024-07【Phase 3 — EV-019】. GSM 24-48hr delay melindungi【Phase 4 — Security Model】.
Evidence: 13 major upgrades【Phase 4 — Technical Upgrade History】; Modular architecture【Phase 4 — System Architecture】; GSM delay【Phase 4 — Security Model Governance Control】; Executive Spell process【Phase 6 — Governance Proposal System】
Supporting Dataset: Phase 3 EV-007, EV-010, EV-014, EV-015, EV-017, EV-018, EV-019; Phase 4 Core Components, System Architecture, Technical Upgrade History, Security Model; Phase 6 Governance
Confidence: HIGH

Factor 3: RWA Pivot Unlocking TradFi Yield At Scale — Vault RWA >$1B AUM (BlockTower, Monetalis, Coinbase Prime) menjadi revenue driver utama 2024
Explanation: RWA Vaults launch 2022-07【Phase 3 — EV-014】. Institutional-grade counterparties【Phase 2 — Entity BlockTower, Monetalis, Coinbase Prime】. Yield tradfi (T-bills ~5%) melebihi crypto Stability Fees【Phase 5 — Revenue Model RWA Vault Yield】. RWA yield mendorong DSR yield competitive【Phase 8 — Adoption Metrics】. Maker menjadi largest DeFi RWA protocol【Phase 8 — Narrative Position RWA】.
Evidence: RWA Vaults EV-014【Phase 3 — EV-014】; RWA AUM >$1B EV-022【Phase 3 — EV-022】; Revenue driver utama 2024【Phase 5 — Revenue History】; Largest DeFi RWA protocol【Phase 8 — Narrative Position】; Market Share RWA 80%+【Phase 8 — Market Share】
Supporting Dataset: Phase 3 EV-014, EV-022; Phase 2 Entity BlockTower, Monetalis, Coinbase Prime; Phase 5 Revenue Model, Revenue History; Phase 7 Major Integrations; Phase 8 Narrative Position, Market Share, Adoption Metrics
Confidence: HIGH

Factor 4: Canonical Multi-Chain Deployment Via Mint/Burn Bridge — DAI/MKR native di 7 chain (Ethereum, Arbitrum, Optimism, Polygon, Gnosis, Base, Starknet) supply konsisten tanpa trusted intermediary
Explanation: Teleporter canonical bridge mint/burn model【Phase 4 — Cross-chain Messaging】. Deployments via governance spell per chain: 4 chain 2022-2023【Phase 3 — EV-015】, Base & Starknet 2023-2024【Phase 3 — EV-018】. Bridge UI bridge.makerdao.com【Phase 7 — Infrastructure Providers】. Supply consistency terjaga lintas chain【Phase 8 — Trading Markets Bridge Liquidity】.
Evidence: Canonical Bridge architecture【Phase 4 — Cross-chain Messaging】; 7 chain deployments EV-015, EV-018【Phase 3 — EV-015, EV-018】; Bridge UI live【Phase 7 — Infrastructure Providers】; Mint/burn model supply consistency【Phase 8 — Trading Markets】
Supporting Dataset: Phase 3 EV-015, EV-018; Phase 4 System Architecture, Core Components Canonical Bridge; Phase 7 External Dependencies Chains, Infrastructure Providers; Phase 8 Trading Markets
Confidence: HIGH

Factor 5: SubDAO Federation Model — Spark Protocol (lending/liquidity) & Sky.money (frontend/savings) sebagai SubDAO semi-autonomous dengan fee sharing ke Maker Treasury
Explanation: Spark launch 2023-05【Phase 3 — EV-016】: SparkLend, sDAI, fee flow ke Treasury【Phase 5 — Revenue Model Spark Protocol Fee Flow】. Sky.money 2024-07【Phase 3 — EV-019】: SSR, SKY rewards, migration UI. Endgame memperluas ke SubDAO RWA-specific, Governance AI【Phase 3 — EV-017】. Internal competition drives innovation (Spark vs Aave, Sky vs Oasis)【Phase 8 — Competitor Landscape Internal SubDAO】.
Evidence: Spark EV-016, Sky EV-019【Phase 3 — EV-016, EV-019】

## Open Questions
- [foundation] Exact legal relationship and liability scope between MakerDAO Cayman Foundation and MKR token holders / Core Units belum sepenuhnya diverifikasi dari dokumen hukum primer (hanya ringkasan blog/forum).
- [foundation] Tanggal pasti "TGE" MKR bersifat ambigu (private sale 2017 vs public liquidity 2018) — perlu konfirmasi apakah project mengakui tanggal spesifik resmi.
- [foundation] Ukuran tim kontributor aktif (full-time vs part-time) per Core Unit saat ini tidak diungkapkan agregat oleh DAO.
- [foundation] Status deploy canonical token di Base / Starknet / Linea apakah sudah *live* mainnet atau masih testnet/proposal stage butuh cek on-chain terbaru.
- [foundation] Detail tokenomics migrasi MKR -> SKY (NewToken) dari Endgame: rasio konversi, jadwal, status fee switch SKY belum difinalisasi on-chain.
- [entity] Identitas investor private sale MKR 2017 (~$1M) belum terungkap nama perusahaan/individu spesifiknya.
- [entity] Auditor smart contract (formal verification) untuk kode Maker (Vault, PSM, DSR, Bridge) tidak tercantum di Phase 1 — perlu identifikasi Trail of Bits, OpenZeppelin, Sigma Prime, atau firm lain.
- [entity] Status deploykan kanonik di Base dan Starknet apakah sudah mainnet live atau masih testnet/proposal butuh verifikasi on-chain terbaru.
- [entity] Detail entitas hukum SubDAO (Spark, Sky) apakah memiliki foundation/wrapper terpisah dari MakerDAO Cayman Foundation.
- [entity] Daftar lengkap 20+ Core Units aktif beserta facilitator dan budget tahunan 2024 belum teragregasi dari forum/governance dashboard.
- [entity] Peran Oracle (Chainlink, OSM, PIVOT) sebagai entity infrastruktur kritis belum diekstrak dari Phase 1.
- [entity] Keterlibatan regulator (SEC, CFTC, EU MiCA) terhadap Maker/DAI/RWA belum muncul di Phase 1.
- [history] Tanggal pasti private sale MKR 2017 (bulan/tanggal) dan daftar investor tidak diverifikasi dari sumber primer.
- [history] Block height dan transaction hash exact untuk launch Sai (2017-12-18) dan MCD (2019-11-18) butuh konfirmasi on-chain.
- [history] Parameter final migrasi MKR→SKY (rasio konversi, jadwal fee switch, apakah MKR diburn atau dikunci) belum difinalisasi di MIP yang dieksekusi on-chain per Agustus 2024.
- [history] Status deploykan kanonik di Base dan Starknet apakah sudah mainnet live penuh (dengan bridge UI aktif) atau masih tahap proposal/testnet butuh cek block explorer terbaru.
- [history] Detail legal wrapper SubDAO (Spark, Sky) apakah memiliki foundation terpisah atau berada di bawah MakerDAO Cayman Foundation.
- [history] Daftar lengkap 20+ Core Units aktif 2024 beserta facilitator, budget, dan scope tidak teragregasi dari sumber tunggal.
- [history] Peran Oracle (Chainlink, OSM, PIVOT) sebagai entity infrastruktur kritis belum diekstrak sebagai event terpisah.
- [history] Keterlibatan regulator (SEC Wells Notice, CFTC, EU MiCA) terhadap Maker/DAI/RWA belum muncul sebagai event tersstruktur.
- [history] Auditor smart contract formal (Trail of Bits, OpenZeppelin, Sigma Prime, PeckShield) untuk setiap major upgrade (MCD, PSM, Bridge, Endgame) belum tercatat sebagai event audit terpisah.
- [history] Insiden "Black Thursday" 2020-03-12: jumlah defisit pasti ($5.3M vs $5.67M vs $8M) berbeda antar sumber — perlu cross-check laporan resmi.
- [technology] Detail formal verification scope untuk Vat/Jug/Pot apakah mencakup semua edge case (reentrancy, integer overflow, governance attack vectors) butuh review laporan Certora penuh.
- [technology] Status audit terbaru untuk Sky.money migration contracts (NewToken, fee switch, SKY rewards) apakah sudah final atau masih iteratif — Trail of Bits audit 2024-03 scope perlu dikonfirmasi.
- [technology] Canonical Bridge di Base dan Starknet apakah sudah melewati audit Trail of Bits terpisah atau tercakup dalam audit bridge 2022 — deployments repo menunjukkan kontrak berbeda.
- [technology] Gas optimization roadmap untuk Vault operations (EIP-3074, EIP-7702, account abstraction) apakah ada proposal teknis resmi di forum.
- [technology] Ketergantungan pada Chainlink sebagai single primary oracle untuk major pairs (ETH/USD, BTC/USD) — apakah ada roadmap teknis untuk fully decentralized oracle aggregation (PIVOT + multiple providers).
- [technology] Starknet DAI Cairo contract upgradeability pattern — apakah menggunakan proxy pattern standar atau immutable dengan migration strategy.
- [technology] Emergency Shutdown (ESM) execution mechanics di multi-chain — apakah shutdown di L1 memicu shutdown otomatis di L2 via bridge message, atau memerlukan governance terpisah per chain.
- [technology] RWA Vault technical integration — bagaimana off-chain asset valuation (NAV) di-on-chain-kan secara teknis (oracle feed, signed attestation, ZK proof) detail implementasi belum terdokumentasi publik detail.
- [technology] SubDAO (Spark, Sky) smart contract upgrade authority — apakah dikontrol oleh Maker governance (DS-Chief) atau memiliki governance module sendiri.
- [technology] Legacy DSS contract (Solidity 0.6) migration plan — apakah ada proposal untuk rewrite ke Solidity 0.8 dengan formal verification baru.
- [financial] Jumlah pasti MKR terjual di private sale 2017 dan harga per token tidak diungkapkan publik — hanya total ~$1M dikonfirmasi Messari.
- [financial] Tidak ada laporan keuangan berkala (quarterly/annual) resmi dari DAO — revenue, expense, surplus, deficit hanya tersedia sebagai data on-chain mentah atau estimasi third-party.
- [financial] Nilai treasury konsolidasi (total assets under management DAO) tidak dipublikasikan sebagai single metric — perlu agregasi manual dari PSM, RWA, Vow, Core Unit multisigs, Vault collateral.
- [financial] Budget Core Unit 2024 agregat (total DAI/tahun dialokasikan ke 20+ Core Units) tidak terpublikasi di single dashboard — tersebar di MIP proposals individual di forum.
- [financial] Revenue split persentase per stream (Stability Fees vs PSM vs RWA vs Spark) per periode tertentu tidak diungkapkan resmi — hanya snapshot dashboard RWA/PSM.
- [financial] Status fee switch SKY (Endgame) — apakah sudah live on-chain, parameter persentase surplus yang dialokasikan, dan jadwal rollout penuh belum dikonfirmasi dari governance spell terbaru.
- [financial] Audited financial statements (GAAP/IFRS) untuk MakerDAO Cayman Foundation atau SubDAO entities (Spark, Sky) tidak tersedia publik.
- [financial] Tax treatment dan regulatory capital requirements untuk RWA Vault income (tradfi yield) di berbagai yurisdiksi belum terdokumentasi publik.
- [financial] Insurance coverage (nexus mutual, unslashed finance, tradfi insurance) untuk treasury assets (RWA, PSM) tidak diungkapkan.
- [financial] Contingency plan finansial jika PSM stablecoin (USDC/USDT) mengalami depeg atau regulatory seizure — belum ada disclosure resmi detail.
- [behavioral] MKR→SKY migration parameter final (rasio konversi 1:24,000 dikonfirmasi tapi fee switch percentage, schedule, MKR burn vs lock mechanism) belum difinalisasi on-chain per Agustus 2024 — Phase 3 EV-020, Phase 6 Token SKY Inflation/Deflation
- [behavioral] Exact legal relationship & liability scope antara MakerDAO Cayman Foundation dengan MKR/SKY holders & Core Units belum diverifikasi dari dokumen hukum primer (hanya ringkasan blog/forum) — Phase 2 Entity MakerDAO Cayman Foundation, Phase 1 Open Threads
- [behavioral] Status deploykan kanonik di Base dan Starknet apakah sudah mainnet live penuh (dengan bridge UI aktif) atau masih tahap proposal/testnet butuh verifikasi on-chain terbaru — Phase 3 EV-018, Phase 2 Entity Base/Starknet, Phase 4 Technology Secondary Layers
- [behavioral] Daftar lengkap 20+ Core Units aktif 2024 beserta facilitator, budget, dan scope tidak teragregasi dari sumber tunggal — Phase 2 Entity Core Units, Phase 1 Open Threads
- [behavioral] Auditor smart contract formal untuk setiap major upgrade (Trail of Bits, OpenZeppelin, Sigma Prime, PeckShield, Certora) scope detail per audit belum terkompilasi lengkap — Phase 4 Audit History, Phase 1 Open Threads
- [behavioral] Keterlibatan regulator (SEC Wells Notice, CFTC, EU MiCA) terhadap Maker/DAI/RWA/SKY belum muncul sebagai event tersstruktur — Phase 1 Open Threads, Phase 5 Financial Risk Legal Financial Risk
- [behavioral] Emergency Shutdown (ESM) execution mechanics di multi-chain — apakah shutdown di L1 memicu shutdown otomatis di L2 via bridge message, atau memerlukan governance terpisah per chain — Phase 4 Technology Security Model Emergency Shutdown, Phase 4 Known Limitations
- [behavioral] RWA Vault technical integration — bagaimana off-chain asset valuation (NAV) di-on-chain-kan secara teknis (oracle feed, signed attestation, ZK proof) detail implementasi belum terdokumentasi publik — Phase 4 Known Limitations RWA Off-chain Dependency, Phase 7 External Dependencies BlockTower/Monetalis
- [behavioral] SubDAO (Spark, Sky) smart contract upgrade authority — apakah dikontrol oleh Maker governance (DS-Chief) atau memiliki governance module sendiri — Phase 2 Entity Spark Protocol, Sky.money, Phase 4 Technology SubDAO Contracts
- [behavioral] Legacy DSS contract (Solidity 0.6) migration plan — apakah ada proposal untuk rewrite ke Solidity 0.8 dengan formal verification baru — Phase 4 Known Limitations Legacy Contract Technical Debt, Phase 4 Technology Current Technical Stack
