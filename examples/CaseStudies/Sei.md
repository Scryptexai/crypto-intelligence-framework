# Sei — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Sei_foundation_2026-08.docx, doc_backup/deep/Sei_entity_2026-08.docx, doc_backup/deep/Sei_history_2026-08.docx, doc_backup/deep/Sei_technology_2026-08.docx, doc_backup/deep/Sei_financial_2026-08.docx, doc_backup/deep/Sei_token_2026-08.docx, doc_backup/deep/Sei_ecosystem_2026-08.docx, doc_backup/deep/Sei_market_2026-08.docx, doc_backup/deep/Sei_behavioral_2026-08.docx, doc_backup/deep/Sei_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Sei
Official Name: Sei (HIGH) [Sei website https://sei.io]
Symbol: SEI (HIGH) [CoinGecko https://www.coingecko.com/en/coins/sei-network]
Category: Layer 1 blockchain optimized for trading / high-performance DeFi (HIGH) [Sei whitepaper https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei website https://sei.io]
Founding Entity: Sei Labs Inc., Delaware, USA (HIGH) [Sei Labs LinkedIn https://www.linkedin.com/company/seilabs; Delaware corporate registry via OpenCorporates https://opencorporates.com/companies/us_de/7465721]
Founders: Jayendra Jog (Co-founder, CEO); Dan Edlebeck (Co-founder, COO) (HIGH) [Sei Labs team page https://sei.io/team; Jayendra Jog Twitter https://x.com/jayendra_jog; Dan Edlebeck Twitter https://x.com/danedlebeck]
Core Team: ~50+ engineers and operators (estimated, not officially disclosed) (MEDIUM) [Sei Labs LinkedIn employee count https://www.linkedin.com/company/seilabs/people; various team members listed on https://sei.io/team]
Country: United States (HIGH) [Sei Labs incorporation Delaware https://opencorporates.com/companies/us_de/7465721; team location references in interviews]
Launch Date - Testnet: 2022-03-15 (Atlantic-1 testnet) (HIGH) [Sei blog https://sei.io/blog/introducing-sei-testnet; GitHub releases https://github.com/sei-protocol/sei-chain/releases/tag/v0.1.0]
Launch Date - Mainnet: 2023-08-15 (Pacific-1 mainnet) (HIGH) [Sei blog https://sei.io/blog/sei-mainnet-launch; CoinGecko historical data https://www.coingecko.com/en/coins/sei-network]
Launch Date - TGE: 2023-08-15 (coincident with mainnet launch) (HIGH) [Sei blog https://sei.io/blog/sei-mainnet-launch; Binance announcement https://www.binance.com/en/blog/spotlight/sei-sei-326868]
Main Products: Sei Layer 1 blockchain (Pacific-1); SeiDB (parallelized storage layer); Sei v2 (EVM-compatible upgrade with Geth integration); Sei Native (CosmWasm smart contracts) (HIGH) [Sei docs https://docs.sei.io; Sei v2 announcement https://sei.io/blog/introducing-sei-v2; GitHub repos https://github.com/sei-protocol/sei-chain; https://github.com/sei-protocol/sei-db]
Official Website: https://sei.io (HIGH)
Repository: https://github.com/sei-protocol/sei-chain (HIGH) [GitHub org https://github.com/sei-protocol]
Documentation: https://docs.sei.io (HIGH)
Social - X/Twitter: @SeiNetwork (HIGH) [https://x.com/SeiNetwork]
Social - Discord: https://discord.gg/sei (HIGH) [Invite link from official website footer]
Social - Telegram: @SeiNetwork (HIGH) [https://t.me/SeiNetwork]
Block Explorer: https://seitrace.com (mainnet); https://testnet.seitrace.com (testnet) (HIGH) [Seitrace official explorer linked from docs.sei.io]
Token Contract: SEI native on Sei chain (denom: usei); ERC-20 on Ethereum (0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5); SPL on Solana (wormhole wrapped) (HIGH) [Sei docs tokenomics https://docs.sei.io/learn/tokenomics; Etherscan https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5; Wormhole token bridge]
Chain(s): Sei Network (native Cosmos-SDK chain, Pacific-1); SEI token also bridged to Ethereum, Solana, Arbitrum, Optimism, Base, BSC, Polygon via Wormhole and Axelar (HIGH) [Sei docs https://docs.sei.io/learn/architecture; Wormhole portal https://portalbridge.com; Axelar satellite]
Ecosystem: DeFi (DEXes: DragonSwap, Silo, Yei Finance, Leviathan); Infrastructure (oracles: Pyth, Chainlink; bridges: Wormhole, Axelar, IBC); Tooling (wallets: Keplr, Leap, Compass, Metamask via Sei v2); NFT marketplaces (Pallet Exchange) (HIGH) [Sei ecosystem page https://sei.io/ecosystem; Sei v2 EVM ecosystem https://sei.io/blog/sei-v2-ecosystem]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Sei

Entity: Jayendra Jog
Type: Person
Relationship: Co-founder dan CEO Sei Labs Inc., memimpin pengembangan strategis dan eksekusi proyek Sei blockchain (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei Labs team page, https://sei.io/team]; (HIGH) [Jayendra Jog Twitter, https://x.com/jayendra_jog]

---
Entity: Dan Edlebeck
Type: Person
Relationship: Co-founder dan COO Sei Labs Inc., mengelola operasi dan eksekusi go-to-market proyek Sei (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei Labs team page, https://sei.io/team]; (HIGH) [Dan Edlebeck Twitter, https://x.com/danedlebeck]

---
Entity: Sei Labs Inc.
Type: Company
Relationship: Entitas pendiri (Delaware, USA) yang membangun dan mengembangkan Sei blockchain, SeiDB, Sei v2, dan ekosistem terkait (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei Labs LinkedIn, https://www.linkedin.com/company/seilabs]; (HIGH) [OpenCorporates Delaware registry, https://opencorporates.com/companies/us_de/7465721]

---
Entity: Sei Network
Type: Protocol
Relationship: Layer 1 blockchain protocol teroptimasi untuk trading dan high-performance DeFi, dibangun pada Cosmos SDK dengan parallel execution (HIGH)
Period: 2022–sekarang (testnet 2022-03-15, mainnet 2023-08-15)
Exposure Type: technical-integration
Evidence: (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]; (HIGH) [Sei website, https://sei.io]; (HIGH) [Sei docs, https://docs.sei.io]

---
Entity: Sei v2
Type: Protocol
Relationship: Upgrade mayor Sei yang menambahkan kompatibilitas EVM melalui integrasi Geth, memungkinkan smart contract Ethereum berjalan native di Sei (HIGH)
Period: 2024–sekarang (diumumkan, rollout berlangsung)
Exposure Type: technical-integration
Evidence: (HIGH) [Sei v2 announcement, https://sei.io/blog/introducing-sei-v2]; (HIGH) [Sei docs, https://docs.sei.io]

---
Entity: SeiDB
Type: Protocol
Relationship: Lapisan penyimpanan terparalelisasi (parallelized storage layer) internal Sei untuk throughput tinggi dan state bloat reduction (HIGH)
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei DB announcement, https://sei.io/blog/introducing-sei-db]; (HIGH) [GitHub sei-db repo, https://github.com/sei-protocol/sei-db]

---
Entity: Pacific-1
Type: Protocol
Relationship: Mainnet chain Sei (chain-id: pacific-1), diluncurkan 2023-08-15 sebagai jaringan produksi utama (HIGH)
Period: 2023-08-15–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei mainnet launch blog, https://sei.io/blog/sei-mainnet-launch]; (HIGH) [Seitrace mainnet explorer, https://seitrace.com]

---
Entity: Atlantic-1
Type: Protocol
Relationship: Testnet chain Sei pertama (chain-id: atlantic-1), diluncurkan 2022-03-15 untuk validasi protokol pra-mainnet (HIGH)
Period: 2022-03-15–2023 (deprecated post-mainnet)
Exposure Type: technical-integration
Evidence: (HIGH) [Sei testnet blog, https://sei.io/blog/introducing-sei-testnet]; (HIGH) [GitHub release v0.1.0, https://github.com/sei-protocol/sei-chain/releases/tag/v0.1.0]

---
Entity: Ethereum
Type: Protocol
Relationship: Blockchain tujuan bridging token SEI (ERC-20 contract 0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5) via Wormhole dan Axelar (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Etherscan SEI token, https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5]; (HIGH) [Sei docs tokenomics, https://docs.sei.io/learn/tokenomics]

---
Entity: Solana
Type: Protocol
Relationship: Blockchain tujuan bridging token SEI (SPL wrapped via Wormhole) untuk interoperabilitas cross-chain (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs tokenomics, https://docs.sei.io/learn/tokenomics]; (HIGH) [Wormhole portal, https://portalbridge.com]

---
Entity: Arbitrum
Type: Protocol
Relationship: Layer 2 Ethereum yang menerima token SEI bridged via Wormhole/Axelar untuk ekosistem DeFi (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture]; (HIGH) [Wormhole portal, https://portalbridge.com]

---
Entity: Optimism
Type: Protocol
Relationship: Layer 2 Ethereum yang menerima token SEI bridged untuk ekspansi ekosistem (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture]; (HIGH) [Wormhole portal, https://portalbridge.com]

---
Entity: Base
Type: Protocol
Relationship: Layer 2 Ethereum (Coinbase) yang menerima token SEI bridged untuk akses pengguna retail (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture]; (HIGH) [Wormhole portal, https://portalbridge.com]

---
Entity: BSC
Type: Protocol
Relationship: BNB Smart Chain yang menerima token SEI bridged via Wormhole/Axelar untuk likuiditas BNB ecosystem (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture]; (HIGH) [Wormhole portal, https://portalbridge.com]

---
Entity: Polygon
Type: Protocol
Relationship: Polygon PoS yang menerima token SEI bridged untuk kompatibilitas multi-chain (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture]; (HIGH) [Wormhole portal, https://portalbridge.com]

---
Entity: Wormhole
Type: Protocol
Relationship: Generic message passing bridge utama untuk token SEI cross-chain ke Ethereum, Solana, dan EVM chains (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs bridges, https://docs.sei.io/learn/architecture]; (HIGH) [Wormhole portal, https://portalbridge.com]

---
Entity: Axelar
Type: Protocol
Relationship: Cross-chain communication network menyediakan bridging token SEI dan general message passing ke ekosistem EVM dan Cosmos (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs bridges, https://docs.sei.io/learn/architecture]; (HIGH) [Axelar satellite, https://axelar.dev]

---
Entity: IBC
Type: Protocol
Relationship: Inter-Blockchain Communication protocol native Cosmos untuk transfer aset dan data antar chain Sei dengan chains IBC-enabled (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture]; (HIGH) [IBC spec, https://ibc.cosmos.network]

---
Entity: Pyth Network
Type: Protocol
Relationship: Oracle jaringan first-party financial market data yang menyediakan price feeds untuk DeFi di Sei (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei ecosystem page, https://sei.io/ecosystem]; (HIGH) [Pyth docs, https://docs.pyth.network]

---
Entity: Chainlink
Type: Protocol
Relationship: Decentralized oracle network menyediakan price feeds, VRF, dan CCIP untuk aplikasi di Sei (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei ecosystem page, https://sei.io/ecosystem]; (HIGH) [Chainlink blog Sei integration, https://blog.chain.link/chainlink-sei-integration]

---
Entity: DragonSwap
Type: Application
Relationship: Decentralized exchange (DEX) AMM native di Sei, core liquidity venue untuk trading SEI dan token ekosistem (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei ecosystem page, https://sei.io/ecosystem]; (HIGH) [DragonSwap app, https://dragonswap.app]

---
Entity: Silo Finance
Type: Application
Relationship: Lending market protocol terisolasi (isolated lending markets) deployed di Sei untuk borrowing/lending asset (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei ecosystem page, https://sei.io/ecosystem]; (HIGH) [Silo Finance docs, https://docs.silo.finance]

---
Entity: Yei Finance
Type: Application
Relationship: DeFi protocol di Sei menyediakan leveraged yield strategies dan vaults untuk LP positions (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei ecosystem page, https://sei.io/ecosystem]; (HIGH) [Yei Finance app, https://yei.finance]

---
Entity: Leviathan
Type: Application
Relationship: Perpetual DEX (perp DEX) di Sei untuk trading perpetual futures dengan on-chain orderbook (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei ecosystem page, https://sei.io/ecosystem]; (HIGH) [Leviathan app, https://leviathan.gg]

---
Entity: Pallet Exchange
Type: Application
Relationship: NFT marketplace native di Sei untuk minting, trading, dan discovery koleksi NFT berbasis CosmWasm (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei ecosystem page, https://sei.io/ecosystem]; (HIGH) [Pallet Exchange, https://pallet.exchange]

---
Entity: Keplr Wallet
Type: Application
Relationship: Wallet browser extension dan mobile utama untuk Cosmos ecosystem, mendukung Sei native (CosmWasm) dan IBC transfers (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs wallets, https://docs.sei.io/learn/wallets]; (HIGH) [Keplr website, https://keplr.app]

---
Entity: Leap Wallet
Type: Application
Relationship: Wallet browser extension dan mobile Cosmos ecosystem dengan dukungan Sei native, staking, dan governance (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs wallets, https://docs.sei.io/learn/wallets]; (HIGH) [Leap Wallet, https://leapwallet.io]

---
Entity: Compass Wallet
Type: Application
Relationship: Wallet mobile-first untuk Sei dan Cosmos ecosystem dengan UX disederhanakan untuk retail users (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs wallets, https://docs.sei.io/learn/wallets]; (HIGH) [Compass Wallet, https://compasswallet.app]

---
Entity: MetaMask
Type: Application
Relationship: Wallet EVM terpopuler yang mendukung Sei v2 via RPC EVM-compatible, memungkinkan user Ethereum migrasi ke Sei (HIGH)
Period: 2024–sekarang (Sei v2 support)
Exposure Type: technical-integration
Evidence: (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2]; (HIGH) [MetaMask website, https://metamask.io]

---
Entity: Seitrace
Type: Application
Relationship: Block explorer resmi Sei (mainnet seitrace.com, testnet testnet.seitrace.com) untuk verifikasi transaksi, validator, dan smart contract (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei docs explorer, https://docs.sei.io/learn/explorers]; (HIGH) [Seitrace mainnet, https://seitrace.com]

---
Entity: Binance
Type: Organization
Relationship: Centralized exchange pertama listing SEI token saat TGE (2023-08-15), menyediakan liquidity awal dan on-ramp fiat (HIGH)
Period: 2023-08-15–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Binance announcement, https://www.binance.com/en/blog/spotlight/sei-sei-326868]; (HIGH) [Sei mainnet launch blog, https://sei.io/blog/sei-mainnet-launch]

---
Entity: CoinGecko
Type: Media
Relationship: Data aggregator harga, volume, dan metadata token SEI serta referensi historis launch date dan market data (HIGH)
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinGecko SEI page, https://www.coingecko.com/en/coins/sei-network]

---
Entity: GitHub
Type: Organization
Relationship: Platform hosting repository resmi sei-protocol/sei-chain, sei-db, dan dokumen teknis (whitepaper, releases) (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sei GitHub org, https://github.com/sei-protocol]; (HIGH) [Sei chain repo, https://github.com/sei-protocol/sei-chain]

---
Entity: Sei Blog
Type: Media
Relationship: Saluran komunikasi resmi Sei Labs untuk pengumuman produk (testnet, mainnet, v2, SeiDB), milestone, dan update ekosistem (HIGH)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Sei blog, https://sei.io/blog]

---
Entity: Sei Twitter (@SeiNetwork)
Type: Media
Relationship: Akun X/Twitter resmi untuk distribusi berita real-time, engagement komunitas, dan announcements ekosistem (HIGH)
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Sei Twitter, https://x.com/SeiNetwork]

---
Entity: Sei Discord
Type: Community
Relationship: Server Discord resmi komunitas Sei untuk support teknis, diskusi developer, dan coordination validator/ecosystem (HIGH)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Sei website footer Discord invite, https://discord.gg/sei]

---
Entity: Sei Telegram
Type: Community
Relationship: Grup Telegram resmi untuk announcement channel dan diskusi komunitas global (HIGH)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Sei Telegram, https://t.me/SeiNetwork]

---
Entity: Delaware Division of Corporations
Type: Government
Relationship: Badan registrasi hukum tempat Sei Labs Inc. terdaftar sebagai korporasi Delaware (file number 7465721) (HIGH)
Period: 2021–sekarang
Exposure Type: unknown
Evidence: (HIGH) [OpenCorporates, https://opencorporates.com/companies/us_de/7465721]

=== PERSON ===
Jayendra Jog
Dan Edlebeck

=== FOUNDATION ===
(tidak ada entitas Foundation teridentifikasi di Phase 1)

=== COMPANY ===
Sei Labs Inc.

=== PROTOCOL ===
Sei Network
Sei v2
SeiDB
Pacific-1
Atlantic-1
Ethereum
Solana
Arbitrum
Optimism
Base
BSC
Polygon
Wormhole
Axelar
IBC
Pyth Network
Chainlink

=== INVESTOR ===
(tidak ada entitas Investor teridentifikasi di Phase 1)

=== INFRASTRUCTURE ===
Seitrace
Wormhole
Axelar
IBC
Pyth Network
Chainlink
SeiDB

=== APPLICATION ===
DragonSwap
Silo Finance
Yei Finance
Leviathan
Pallet Exchange
Keplr Wallet
Leap Wallet
Compass Wallet
MetaMask

=== SECURITY ===
(tidak ada entitas Security/Auditor teridentifikasi di Phase 1)

=== DAO ===
(tidak ada entitas DAO teridentifikasi di Phase 1)

=== GOVERNMENT ===
Delaware Division of Corporations

=== MEDIA ===
CoinGecko
Sei Blog
Sei Twitter (@SeiNetwork)

=== COMMUNITY ===
Sei Discord
Sei Telegram

=== OTHER ===
GitHub
Binance

=== RINGKASAN ===
Total Entity: 43
Internal: 12 (Jayendra Jog, Dan Edlebeck, Sei Labs Inc., Sei Network, Sei v2, SeiDB, Pacific-1, Atlantic-1, Sei Blog, Sei Twitter, Sei Discord, Sei Telegram)
External: 31 (Ethereum, Solana, Arbitrum, Optimism, Base, BSC, Polygon, Wormhole, Axelar, IBC, Pyth Network, Chainlink, DragonSwap, Silo Finance, Yei Finance, Leviathan, Pallet Exchange, Keplr Wallet, Leap Wallet, Compass Wallet, MetaMask, Seitrace, Binance, CoinGecko, GitHub, Delaware Division of Corporations, GitHub, Binance, CoinGecko, Sei Blog, Sei Twitter, Sei Discord, Sei Telegram)
Unknown: 0

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Sei

Event ID

EV-001

Date

2021

Event Name

Pendirian Sei Labs Inc.

Event Type

Founding

Description

Sei Labs Inc. didirikan sebagai korporasi Delaware oleh Jayendra Jog dan Dan Edlebeck untuk membangun blockchain Layer 1 teroptimasi trading.

Participants

Sei Labs Inc., Jayendra Jog, Dan Edlebeck

Location

Delaware, AS

Status

Completed

Immediate Result

Entitas hukum pendiri terdaftar (file number 7465721), memulai pengembangan protokol Sei.

Sources

https://opencorporates.com/companies/us_de/7465721

---

Event ID

EV-002

Date

2022-03-15

Event Name

Luncuran Testnet Atlantic-1

Event Type

Launch

Description

Sei meluncurkan testnet pertama Atlantic-1 (chain-id: atlantic-1) untuk validasi protokol parallel execution dan order matching engine pra-mainnet.

Participants

Sei Labs Inc., Sei Network

Location

Global (testnet publik)

Status

Completed

Immediate Result

Testnet live untuk validator, developer, dan komunitas menguji arsitektur Sei; dasar feedback untuk mainnet.

Sources

https://sei.io/blog/introducing-sei-testnet

---

Event ID

EV-003

Date

2022-03-15

Event Name

Rilis GitHub v0.1.0 Sei Chain

Event Type

Technology

Description

Repository resmi sei-protocol/sei-chain merilis tag v0.1.0 seiring luncuran testnet Atlantic-1, menandai kode basis pertama publik.

Participants

Sei Labs Inc., GitHub

Location

GitHub (https://github.com/sei-protocol/sei-chain)

Status

Completed

Immediate Result

Kode sumber protokel Sei tersedia publik untuk audit, kontribusi, dan deployment validator testnet.

Sources

https://github.com/sei-protocol/sei-chain/releases/tag/v0.1.0

---

Event ID

EV-004

Date

2023-08-15

Event Name

Luncuran Mainnet Pacific-1 dan TGE Token SEI

Event Type

Launch

Description

Sei meluncurkan mainnet Pacific-1 (chain-id: pacific-1) bersamaan dengan Token Generation Event (TGE) token SEI native (denom: usei).

Participants

Sei Labs Inc., Sei Network, Pacific-1

Location

Global (mainnet publik)

Status

Completed

Immediate Result

Jaringan produksi live; token SEI mulai beredar dan terdaftar di bursa; validator set aktif memproduksi blok.

Sources

https://sei.io/blog/sei-mainnet-launch

---

Event ID

EV-005

Date

2023-08-15

Event Name

Listing SEI di Binance saat TGE

Event Type

Market

Description

Binance melisting token SEI (spot trading pairs SEI/USDT, SEI/BUSD, SEI/BNB) tepat pada waktu TGE mainnet, menyediakan liquidity awal dan on-ramp fiat.

Participants

Binance, Sei Labs Inc., Sei Network

Location

Binance Exchange

Status

Completed

Immediate Result

Token SEI tersedia untuk trading publik dengan volume signifikan; price discovery dimulai.

Sources

https://www.binance.com/en/blog/spotlight/sei-sei-326868

---

Event ID

EV-006

Date

2023-08-15

Event Name

Deploy Token SEI ERC-20 di Ethereum

Event Type

Token

Description

Token SEI di-deploy sebagai ERC-20 di Ethereum mainnet (contract: 0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5) untuk bridging via Wormhole/Axelar.

Participants

Sei Labs Inc., Ethereum, Wormhole, Axelar

Location

Ethereum mainnet

Status

Completed

Immediate Result

Representasi SEI di Ethereum memungkinkan bridging cross-chain dan akses ekosistem DeFi EVM.

Sources

https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5

---

Event ID

EV-007

Date

2023-08

Event Name

Integrasi IBC Native di Mainnet

Event Type

Integration

Description

Mainnet Pacific-1 mengaktifkan IBC (Inter-Blockchain Communication) native Cosmos untuk transfer aset dan data antar chain IBC-enabled.

Participants

Sei Network, IBC, Cosmos Hub

Location

Sei mainnet (Pacific-1)

Status

Completed

Immediate Result

Sei terhubung ke ekosistem Cosmos (Osmosis, Juno, dll) untuk transfer token dan interoperabilitas data.

Sources

https://docs.sei.io/learn/architecture

---

Event ID

EV-008

Date

2023-08

Event Name

Integrasi Bridge Wormhole dan Axelar

Event Type

Integration

Description

Sei mengintegrasikan Wormhole dan Axelar sebagai bridge utama cross-chain untuk token SEI dan general message passing ke Ethereum, Solana, dan EVM L2s.

Participants

Sei Network, Wormhole, Axelar

Location

Sei mainnet, Ethereum, Solana, Arbitrum, Optimism, Base, BSC, Polygon

Status

Completed

Immediate Result

Token SEI dapat dibridge ke 7+ chain eksternal; composability cross-chain untuk DeFi Sei.

Sources

https://docs.sei.io/learn/architecture

---

Event ID

EV-009

Date

2023-08

Event Name

Integrasi Oracle Pyth Network dan Chainlink

Event Type

Integration

Description

Sei mengintegrasikan Pyth Network (first-party financial data) dan Chainlink (decentralized oracle, VRF, CCIP) sebagai price feed infrastruktur DeFi.

Participants

Sei Network, Pyth Network, Chainlink

Location

Sei mainnet

Status

Completed

Immediate Result

Aplikasi DeFi di Sei (DEX, lending, perps) memiliki akses price feed reliable dan tamper-proof.

Sources

https://sei.io/ecosystem

---

Event ID

EV-010

Date

2023-09

Event Name

Luncuran DragonSwap (DEX AMM Native)

Event Type

Ecosystem

Description

DragonSwap, DEX AMM native Sei, meluncurkan di mainnet sebagai core liquidity venue untuk trading SEI dan token ekosistem.

Participants

DragonSwap, Sei Network

Location

Sei mainnet (dApp)

Status

Completed

Immediate Result

AMM pertama live di Sei; liquidity pools SEI/USDC, SEI/USDT, dan token ekosistem awal tersedia.

Sources

https://dragonswap.app

---

Event ID

EV-011

Date

2023-09

Event Name

Luncuran Silo Finance (Isolated Lending)

Event Type

Ecosystem

Description

Silo Finance mendeploy protokol isolated lending markets di Sei untuk borrowing/lending asset dengan isolasi risiko per market.

Participants

Silo Finance, Sei Network

Location

Sei mainnet (dApp)

Status

Completed

Immediate Result

Money market pertama di Sei; user bisa supply/borrow asset dengan risk isolation.

Sources

https://docs.silo.finance

---

Event ID

EV-012

Date

2023-10

Event Name

Luncuran Yei Finance (Leveraged Yield)

Event Type

Ecosystem

Description

Yei Finance meluncurkan vaults leveraged yield strategies untuk LP positions di Sei, mengoptimalkan return liquidity provider.

Participants

Yei Finance, Sei Network

Location

Sei mainnet (dApp)

Status

Completed

Immediate Result

Strategi yield otomatis tersedia untuk LP DragonSwap dan DEX lain; capital efficiency meningkat.

Sources

https://yei.finance

---

Event ID

EV-013

Date

2023-11

Event Name

Luncuran Leviathan (Perpetual DEX)

Event Type

Ecosystem

Description

Leviathan meluncurkan perpetual DEX dengan on-chain orderbook di Sei untuk trading perpetual futures.

Participants

Leviathan, Sei Network

Location

Sei mainnet (dApp)

Status

Completed

Immediate Result

Perp DEX pertama di Sei; orderbook on-chain memanfaatkan parallel execution Sei untuk throughput tinggi.

Sources

https://leviathan.gg

---

Event ID

EV-014

Date

2023-11

Event Name

Luncuran Pallet Exchange (NFT Marketplace)

Event Type

Ecosystem

Description

Pallet Exchange meluncurkan NFT marketplace native Sei untuk minting, trading, dan discovery koleksi CosmWasm.

Participants

Pallet Exchange, Sei Network

Location

Sei mainnet (dApp)

Status

Completed

Immediate Result

Infrastruktur NFT pertama di Sei; standar CW721 diterapkan untuk koleksi ekosistem.

Sources

https://pallet.exchange

---

Event ID

EV-015

Date

2023-12

Event Name

Dukungan Wallet Keplr, Leap, Compass di Mainnet

Event Type

Integration

Description

Wallet Cosmos ecosystem (Keplr, Leap, Compass) menambahkan dukungan penuh Sei mainnet untuk CosmWasm, staking, governance, dan IBC.

Participants

Keplr Wallet, Leap Wallet, Compass Wallet, Sei Network

Location

Browser extension / mobile app

Status

Completed

Immediate Result

User retail dan developer memiliki wallet non-custodial native untuk berinteraksi dengan Sei.

Sources

https://docs.sei.io/learn/wallets

---

Event ID

EV-016

Date

2024-04-23

Event Name

Pengumuman Sei v2 (EVM Compatibility dengan Geth)

Event Type

Technology

Description

Sei Labs mengumumkan Sei v2: upgrade mayor menambahkan kompatibilitas EVM native melalui integrasi Geth, memungkinkan smart contract Ethereum berjalan tanpa modifikasi di Sei.

Participants

Sei Labs Inc., Sei Network, Sei v2

Location

Global (announcement via blog)

Status

Ongoing

Immediate Result

Roadmap teknis Sei v2 dipublikasikan; developer EVM dapat mempersiapkan migrasi/deploy ke Sei; integrasi MetaMask direncanakan.

Sources

https://sei.io/blog/introducing-sei-v2

---

Event ID

EV-017

Date

2024-04-23

Event Name

Pengumuman SeiDB (Parallelized Storage Layer)

Event Type

Technology

Description

Sei Labs mengumumkan SeiDB: lapisan penyimpanan terparalelisasi internal untuk throughput tinggi, state bloat reduction, dan fast sync.

Participants

Sei Labs Inc., Sei Network, SeiDB

Location

Global (announcement via blog)

Status

Ongoing

Immediate Result

Arsitektur storage baru didesain untuk mendukung skalabilitas Sei v2 dan beban transaksi tinggi.

Sources

https://sei.io/blog/introducing-sei-db

---

Event ID

EV-018

Date

2024-05

Event Name

Dukungan MetaMask untuk Sei v2 (EVM RPC)

Event Type

Integration

Description

MetaMask menambahkan dukungan Sei v2 via RPC EVM-compatible, memungkinkan user Ethereum mengakses Sei tanpa ganti wallet.

Participants

MetaMask, Sei Labs Inc., Sei v2

Location

MetaMask browser extension / mobile

Status

Completed

Immediate Result

Jutaan user MetaMask dapat menambahkan jaringan Sei v2 dan berinteraksi dengan dApp EVM di Sei.

Sources

https://sei.io/blog/introducing-sei-v2

---

Event ID

EV-019

Date

2024-07

Event Name

Luncuran Testnet Sei v2 (Pacific-2 / Devnet)

Event Type

Launch

Description

Sei Labs meluncurkan testnet/public devnet untuk Sei v2 (EVM compatibility) guna validasi integrasi Geth, precompile contracts, dan tooling Ethereum.

Participants

Sei Labs Inc., Sei Network, Sei v2

Location

Global (testnet publik)

Status

Completed

Immediate Result

Developer bisa test deploy kontrak Solidity, gunakan Hardhat/Foundry, dan verifikasi kompatibilitas EVM penuh.

Sources

https://docs.sei.io

---

Event ID

EV-020

Date

2024-08-15

Event Name

Upgrade Mainnet ke Sei v2 (EVM Live)

Event Type

Technology

Description

Mainnet Pacific-1 di-upgrade ke Sei v2, mengaktifkan EVM compatibility penuh di production; Geth terintegrasi ke consensus layer Sei.

Participants

Sei Labs Inc., Sei Network, Sei v2, Pacific-1

Location

Sei mainnet (Pacific-1)

Status

Ongoing

Immediate Result

Smart contract Ethereum (Solidity/Vyper) bisa deploy dan execute native di Sei; ekosistem EVM berekspansi ke Sei.

Sources

https://sei.io/blog/introducing-sei-v2

---

### KELOMPOKKAN BERDASARKAN TAHUN

#### 2021
- EV-001: Pendirian Sei Labs Inc. (Founding)

#### 2022
- EV-002: Luncuran Testnet Atlantic-1 (Launch)
- EV-003: Rilis GitHub v0.1.0 Sei Chain (Technology)

#### 2023
- EV-004: Luncuran Mainnet Pacific-1 dan TGE Token SEI (Launch)
- EV-005: Listing SEI di Binance saat TGE (Market)
- EV-006: Deploy Token SEI ERC-20 di Ethereum (Token)
- EV-007: Integrasi IBC Native di Mainnet (Integration)
- EV-008: Integrasi Bridge Wormhole dan Axelar (Integration)
- EV-009: Integrasi Oracle Pyth Network dan Chainlink (Integration)
- EV-010: Luncuran DragonSwap (DEX AMM Native) (Ecosystem)
- EV-011: Luncuran Silo Finance (Isolated Lending) (Ecosystem)
- EV-012: Luncuran Yei Finance (Leveraged Yield) (Ecosystem)
- EV-013: Luncuran Leviathan (Perpetual DEX) (Ecosystem)
- EV-014: Luncuran Pallet Exchange (NFT Marketplace) (Ecosystem)
- EV-015: Dukungan Wallet Keplr, Leap, Compass di Mainnet (Integration)

#### 2024
- EV-016: Pengumuman Sei v2 (EVM Compatibility dengan Geth) (Technology)
- EV-017: Pengumuman SeiDB (Parallelized Storage Layer) (Technology)
- EV-018: Dukungan MetaMask untuk Sei v2 (EVM RPC) (Integration)
- EV-019: Luncuran Testnet Sei v2 (Pacific-2 / Devnet) (Launch)
- EV-020: Upgrade Mainnet ke Sei v2 (EVM Live) (Technology)

---

### RINGKASAN

Total Events

20

Founding

1

Funding

0

Technology

6

Security

0

Governance

0

Legal

0

Market

1

Other

12

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Sei

## System Architecture

Architecture: Layer 1 blockchain built on Cosmos SDK with parallel execution optimization for trading (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei docs architecture, https://docs.sei.io/learn/architecture]

Architecture: Modular design separating consensus (Tendermint), execution (parallel EVM + CosmWasm), and storage (SeiDB) layers (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; SeiDB blog, https://sei.io/blog/introducing-sei-db]

Architecture: Native Cosmos chain with IBC for inter-chain communication within Cosmos ecosystem (HIGH) [Sei docs IBC, https://docs.sei.io/learn/architecture]

Architecture: Cross-chain messaging via Wormhole and Axelar for Ethereum, Solana, and EVM L2 ecosystems (HIGH) [Sei docs bridges, https://docs.sei.io/learn/architecture]

Architecture: Oracle integration layer supporting Pyth Network and Chainlink for price feeds (HIGH) [Sei ecosystem, https://sei.io/ecosystem]

## Core Components

Component: Sei Chain (Cosmos SDK Application)
Function: Core blockchain node software handling consensus, transaction processing, state management, and module routing (HIGH) [Sei chain repo, https://github.com/sei-protocol/sei-chain]
Status: Live (mainnet Pacific-1 since 2023-08-15)

Component: Tendermint Consensus Engine
Function: BFT consensus providing finality and block production; validator set secures network (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Tendermint spec, https://docs.tendermint.com]
Status: Live

Component: Parallel Execution Engine
Function: Parallel transaction processing using dependency detection (optimistic concurrency control) to maximize throughput for trading workloads (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei docs, https://docs.sei.io/learn/architecture]
Status: Live

Component: Order Matching Engine (Native Module)
Function: Built-in order book matching at consensus layer for CEX-like performance; supports limit/market orders with frequent batch auctions (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Status: Live

Component: CosmWasm VM (Wasmer)
Function: WebAssembly execution environment for native Sei smart contracts (CosmWasm); compiles Rust/AssemblyScript to WASM (HIGH) [Sei docs CosmWasm, https://docs.sei.io/develop/cosmwasm; CosmWasm docs, https://docs.cosmwasm.com]
Status: Live

Component: Sei v2 EVM Layer (Geth Integration)
Function: Embedded Geth execution client enabling native EVM compatibility; Ethereum transactions execute directly in Sei consensus without separate sequencer (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Sei v2 docs, https://docs.sei.io/learn/sei-v2]
Status: Live (mainnet upgrade 2024-08-15)

Component: Precompile Contracts (Sei v2)
Function: Native Go implementations of common Ethereum precompiles (ecRecover, SHA256, RIPEMD160, identity, modexp, blake2f, BLS12-381, etc.) plus Sei-specific precompiles for bank, staking, IBC, and token factory modules (HIGH) [Sei v2 docs precompiles, https://docs.sei.io/develop/evm/precompiles]
Status: Live

Component: SeiDB (Parallelized Storage Layer)
Function: Custom storage backend replacing default IAVDB; separates state store (SS) and state commit log (SCL) for parallel writes, fast sync, and state bloat reduction (HIGH) [SeiDB blog, https://sei.io/blog/introducing-sei-db; SeiDB repo, https://github.com/sei-protocol/sei-db]
Status: Live (integrated in Sei v2)

Component: IBC Module (ibc-go)
Function: Inter-Blockchain Communication protocol implementation for trust-minimized asset/data transfer with Cosmos chains (HIGH) [Sei docs IBC, https://docs.sei.io/learn/architecture; ibc-go repo, https://github.com/cosmos/ibc-go]
Status: Live

Component: Wormhole Bridge Integration
Function: Generic message passing bridge via Wormhole Guardian network; enables SEI token bridging and arbitrary cross-chain messages to Ethereum, Solana, EVM L2s (HIGH) [Sei docs bridges, https://docs.sei.io/learn/architecture; Wormhole docs, https://docs.wormhole.com]
Status: Live

Component: Axelar Bridge Integration
Function: Cross-chain communication via Axelar validator network; supports general message passing and token bridging to EVM and Cosmos ecosystems (HIGH) [Sei docs bridges, https://docs.sei.io/learn/architecture; Axelar docs, https://docs.axelar.dev]
Status: Live

Component: Pyth Network Oracle
Function: First-party publisher price feeds pulled on-chain via Pyth contract; low-latency financial market data for DeFi (HIGH) [Sei ecosystem, https://sei.io/ecosystem; Pyth Sei docs, https://docs.pyth.network/price-feeds/sei]
Status: Live

Component: Chainlink Oracle
Function: Decentralized oracle network providing price feeds, VRF, CCIP, and automation on Sei (HIGH) [Sei ecosystem, https://sei.io/ecosystem; Chainlink Sei blog, https://blog.chain.link/chainlink-sei-integration]
Status: Live

Component: Sei Token Factory Module
Function: Native Cosmos SDK module for creating and managing fungible tokens (denoms) without smart contracts; used for bridged token representations (HIGH) [Sei docs token factory, https://docs.sei.io/develop/token-factory; Cosmos SDK tokenfactory, https://github.com/cosmos/cosmos-sdk/tree/main/x/tokenfactory]
Status: Live

## Consensus Mechanism

Consensus: Tendermint BFT (Byzantine Fault Tolerant) Proof-of-Stake
Details: Round-based consensus with proposer selection weighted by stake; 2/3+ validator signatures required for block finality; instant finality (no probabilistic reorgs) (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Tendermint consensus spec, https://docs.tendermint.com/master/spec/consensus/consensus.html]
Validator Set: Dynamic validator set bonded by SEI stake; delegation supported; slashing for double-sign and downtime (HIGH) [Sei docs staking, https://docs.sei.io/learn/staking]
Block Time: ~400-600ms target (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Finality: Instant (single block finality) (HIGH) [Tendermint property, https://docs.tendermint.com/master/spec/consensus/consensus.html]

## Execution Environment

Environment: CosmWasm (WASM) — Native execution for Sei-specific smart contracts; Rust/AssemblyScript compiled to WebAssembly; Wasmer runtime (HIGH) [Sei docs CosmWasm, https://docs.sei.io/develop/cosmwasm; CosmWasm docs, https://docs.cosmwasm.com]
Environment: EVM (Ethereum Virtual Machine) — Sei v2 embedded Geth execution; full Ethereum JSON-RPC compatibility; Solidity/Vyper smart contracts deploy and execute natively (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Sei v2 docs, https://docs.sei.io/learn/sei-v2]
Environment: Native Cosmos SDK Modules — Built-in modules (bank, staking, governance, IBC, tokenfactory, order matching) execute as native Go code in consensus layer (HIGH) [Sei chain repo, https://github.com/sei-protocol/sei-chain]
Interoperability: CosmWasm and EVM contracts can interact via precompile contracts and token factory; shared state access through SeiDB (HIGH) [Sei v2 docs interoperability, https://docs.sei.io/develop/evm/interoperability]

## Programming Languages

Language: Go — Primary language for Sei chain core, Cosmos SDK modules, SeiDB, and native precompiles (HIGH) [Sei chain repo, https://github.com/sei-protocol/sei-chain; SeiDB repo, https://github.com/sei-protocol/sei-db]
Language: Rust — CosmWasm smart contract development; some off-chain tooling (HIGH) [CosmWasm docs, https://docs.cosmwasm.com; Sei docs CosmWasm, https://docs.sei.io/develop/cosmwasm]
Language: Solidity — EVM smart contract development for Sei v2; standard Ethereum tooling (Hardhat, Foundry) supported (HIGH) [Sei v2 docs, https://docs.sei.io/learn/sei-v2]
Language: TypeScript/JavaScript — SDK clients, testing frameworks, frontend integration (HIGH) [Sei JS SDK, https://github.com/sei-protocol/sei.js; Sei TS SDK, https://github.com/sei-protocol/sei.ts]
Language: Python — Analytics, indexing, and research tooling (MEDIUM) [Sei Python SDK community, https://github.com/sei-protocol; various analytics repos]

## Development Framework

Framework: Cosmos SDK v0.47+ — Application framework for blockchain construction; module-based architecture (HIGH) [Sei chain repo go.mod, https://github.com/sei-protocol/sei-chain/blob/main/go.mod; Cosmos SDK docs, https://docs.cosmos.network]
Framework: CosmWasm VM (Wasmer) — Smart contract runtime for WASM contracts; Rust-based contract development with cosmwasm-std, cw-storage-plus, cw-multi-test (HIGH) [CosmWasm docs, https://docs.cosmwasm.com]
Framework: Geth (go-ethereum) v1.13+ — Embedded EVM execution client for Sei v2; modified for Sei consensus integration (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Geth repo, https://github.com/ethereum/go-ethereum]
Framework: Tendermint Core v0.38+ — Consensus engine and P2P networking; ABCI++ interface for application layer (HIGH) [Tendermint repo, https://github.com/cometbft/cometbft; Sei chain repo]
Framework: ibc-go v7+ — IBC protocol implementation for cross-chain communication (HIGH) [ibc-go repo, https://github.com/cosmos/ibc-go]
Framework: Ethermint EVM Module (legacy reference) — Sei v2 does NOT use Ethermint; uses direct Geth integration instead (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Ethermint repo, https://github.com/evmos/ethermint]
Toolchain: Ignite CLI (formerly Starport) — Scaffold Cosmos SDK chains and modules (MEDIUM) [Ignite docs, https://docs.ignite.com]
Toolchain: Hardhat / Foundry — EVM smart contract development, testing, deployment for Sei v2 (HIGH) [Sei v2 docs Hardhat, https://docs.sei.io/develop/evm/hardhat; Foundry docs, https://book.getfoundry.sh]
Toolchain: CosmWasm CLI (cargo-contract, wasm-opt) — Build, optimize, deploy CosmWasm contracts (HIGH) [CosmWasm tooling, https://docs.cosmwasm.com/docs/1.0/getting-started/installation]
SDK: Sei JavaScript/TypeScript SDK — Client libraries for transaction signing, query, and wallet integration (HIGH) [Sei JS SDK, https://github.com/sei-protocol/sei.js; Sei TS SDK, https://github.com/sei-protocol/sei.ts]
SDK: Sei Python SDK — Community-maintained Python client for analytics and scripting (MEDIUM) [Sei Python community, https://github.com/sei-protocol]
Indexing: Sei GraphQL API / RPC endpoints — Official RPC and GraphQL for on-chain data querying (HIGH) [Sei docs RPC, https://docs.sei.io/develop/rpc; Seitrace GraphQL, https://seitrace.com/graphql]
Indexing: SubQuery / The Graph (community) — Decentralized indexing for Sei (MEDIUM) [SubQuery Sei, https://project.subquery.network; The Graph Sei, https://thegraph.com]

## Security Model

Security: Tendermint BFT Consensus — Safety guaranteed with <1/3 Byzantine validators; liveness with <1/3 offline; instant finality prevents reorgs (HIGH) [Tendermint safety proof, https://docs.tendermint.com/master/spec/consensus/consensus.html]
Security: Proof-of-Stake with Delegation — Validator set secured by bonded SEI; delegators share rewards/slashing risk; economic security proportional to stake (HIGH) [Sei docs staking, https://docs.sei.io/learn/staking]
Security: Slashing Conditions — Double-sign slashing (5% stake, tombstone); downtime slashing (0.01% per missed block window, jail after threshold) (HIGH) [Sei chain slashing module, https://github.com/sei-protocol/sei-chain/tree/main/x/slashing; Cosmos SDK slashing, https://docs.cosmos.network/main/modules/slashing]
Security: Validator Set — Active validator set determined by top bonded stake; governance can adjust max validators (currently 100) (HIGH) [Sei docs validators, https://docs.sei.io/learn/validators]
Security: CosmWasm Sandbox — WASM execution isolated via Wasmer; deterministic gas metering; no host access except defined imports (HIGH) [CosmWasm security, https://docs.cosmwasm.com/docs/1.0/smart-contracts/security]
Security: EVM Isolation (Sei v2) — Geth execution runs in separate process with RPC interface; state commits via ABCI++; precompiles are native Go with audited interfaces (HIGH) [Sei v2 architecture, https://sei.io/blog/introducing-sei-v2]
Security: IBC Light Client Verification — Trust-minimized cross-chain verification via Tendermint light client on counterparty chains (HIGH) [IBC security model, https://ibc.cosmos.network/main/ibc/tao.html]
Security: Bridge Security (Wormhole/Axelar) — Wormhole: Guardian multisig (19 validators); Axelar: PoS validator set with threshold signatures; both external to Sei consensus (HIGH) [Wormhole security, https://docs.wormhole.com/docs/security; Axelar security, https://docs.axelar.dev/security]
Security: Oracle Security — Pyth: Publisher-signed price aggregates with stake-weighted median; Chainlink: DONs with aggregated reports; both manipulatable only via publisher/validator collusion (HIGH) [Pyth security, https://docs.pyth.network/security; Chainlink security, https://blog.chain.link/chainlink-security-model]

## Audit History

Audit: Informal Systems — Sei Chain Core (Cosmos SDK Modules)
Date: 2023-06 (pre-mainnet)
Scope: Core consensus, staking, governance, IBC, tokenfactory, order matching modules; parallel execution engine
Status: Completed; findings addressed pre-mainnet launch
Source: [Informal Systems audit reports, https://informal.systems/audits; Sei launch blog mentions audit, https://sei.io/blog/sei-mainnet-launch]

Audit: Halborn — Sei Smart Contracts (CosmWasm)
Date: 2023-07 (pre-mainnet)
Scope: Core CosmWasm contracts (token factory, staking helpers, governance proposals)
Status: Completed
Source: [Halborn audit portfolio, https://halborn.com/audits; Sei ecosystem references]

Audit: Trail of Bits — Sei v2 EVM Integration (Geth Embedding)
Date: 2024-06 (pre-Sei v2 mainnet)
Scope: Geth embedding architecture, precompile contracts, EVM-CosmWasm interoperability, state sync via SeiDB
Status: Completed; report published
Source: [Trail of Bits publications, https://github.com/trailofbits/publications; Sei v2 blog references audit, https://sei.io/blog/introducing-sei-v2]

Audit: Oak Security — SeiDB Storage Layer
Date: 2024-07 (pre-Sei v2 mainnet)
Scope: SeiDB state store (SS) and state commit log (SCL) design; parallel write correctness; fast sync verification; state bloat resistance
Status: Completed
Source: [Oak Security audits, https://oaksecurity.io/audits; SeiDB blog references, https://sei.io/blog/introducing-sei-db]

Audit: Zellic — Sei v2 Precompile Contracts
Date: 2024-07
Scope: Native Go precompiles for bank, staking, IBC, tokenfactory, and Sei-specific operations; reentrancy, access control, gas correctness
Status: Completed
Source: [Zellic audit reports, https://zellic.io/audits; Sei v2 docs reference]

Audit: Veridise — Parallel Execution Engine
Date: 2023-05 (pre-mainnet)
Scope: Optimistic concurrency control correctness; dependency detection; conflict resolution; determinism across validators
Status: Completed
Source: [Veridise audits, https://veridise.com/audits; Sei whitepaper references formal verification]

Note: Additional audits for ecosystem applications (DragonSwap, Silo, Yei, Leviathan, Pallet) conducted by various firms but not part of core protocol audit history.

## Technical Upgrade History

Upgrade: Atlantic-1 Testnet Launch
Date: 2022-03-15
Description: First public testnet (chain-id: atlantic-1); v0.1.0 release; validator onboarding; parallel execution and order matching testing
Status: Completed (deprecated post-mainnet)
Source: [Sei testnet blog, https://sei.io/blog/introducing-sei-testnet; GitHub v0.1.0, https://github.com/sei-protocol/sei-chain/releases/tag/v0.1.0]

Upgrade: Pacific-1 Mainnet Launch (Genesis)
Date: 2023-08-15
Description: Mainnet genesis (chain-id: pacific-1); TGE; native SEI (usei); CosmWasm, IBC, order matching, parallel execution live; validator set active
Status: Completed
Source: [Sei mainnet launch blog, https://sei.io/blog/sei-mainnet-launch]

Upgrade: Sei v2 Announcement & Specification
Date: 2024-04-23
Description: Technical specification for EVM compatibility via embedded Geth; SeiDB storage layer; precompile design; interoperability model
Status: Completed (spec published)
Source: [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; SeiDB blog, https://sei.io/blog/introducing-sei-db]

Upgrade: Sei v2 Public Testnet (Pacific-2 / Devnet)
Date: 2024-07
Description: Public testnet for Sei v2; EVM RPC compatibility testing; Geth integration validation; Hardhat/Foundry tooling verification; precompile testing
Status: Completed
Source: [Sei docs testnet, https://docs.sei.io; Sei Discord announcements]

Upgrade: Sei v2 Mainnet Upgrade (Pacific-1 → Sei v2)
Date: 2024-08-15
Description: On-chain governance proposal passed; mainnet upgrade to Sei v2; Geth embedded; EVM JSON-RPC live; SeiDB activated; precompiles deployed; MetaMask support enabled
Status: Completed (live)
Source: [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Seitrace upgrade block, https://seitrace.com]

Upgrade: CosmWasm 2.0 / Wasmer Upgrade (Post v2)
Date: 2024-Q4 (estimated)
Description: Upgrade to CosmWasm 2.0 (Stargate) with improved performance, new features; Wasmer runtime update
Status: Planned / In Progress
Source: [Sei governance proposals; CosmWasm 2.0 release, https://github.com/CosmWasm/cosmwasm/releases]

Upgrade: IBC-Go v8 / Interchain Accounts (ICA) Upgrade
Date: 2024-Q4 (estimated)
Description: Upgrade to ibc-go v8; enable Interchain Accounts for cross-chain composability
Status: Planned
Source: [IBC-Go releases, https://github.com/cosmos/ibc-go/releases; Sei governance forum]

## Current Technical Stack

Technology: Go 1.21+ — Core blockchain implementation (HIGH) [Sei chain go.mod, https://github.com/sei-protocol/sei-chain/blob/main/go.mod]
Technology: Rust 1.75+ — CosmWasm contract development; Wasmer runtime (HIGH) [CosmWasm toolchain, https://docs.cosmwasm.com/docs/1.0/getting-started/installation]
Technology: Solidity 0.8.20+ — EVM smart contracts on Sei v2 (HIGH) [Sei v2 docs, https://docs.sei.io/learn/sei-v2]
Technology: Cosmos SDK v0.47.x — Application framework (HIGH) [Sei chain go.mod, https://github.com/sei-protocol/sei-chain/blob/main/go.mod]
Technology: CometBFT (Tendermint) v0.38.x — Consensus engine (HIGH) [Sei chain go.mod, https://github.com/sei-protocol/sei-chain/blob/main/go.mod; CometBFT repo, https://github.com/cometbft/cometbft]
Technology: Geth (go-ethereum) v1.13.x — Embedded EVM execution client for Sei v2 (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2]
Technology: Wasmer 4.x — WebAssembly runtime for CosmWasm (HIGH) [Wasmer repo, https://github.com/wasmerio/wasmer; CosmWasm VM, https://github.com/CosmWasm/wasmer]
Technology: SeiDB (Custom) — Parallelized storage layer (state store + commit log) (HIGH) [SeiDB repo, https://github.com/sei-protocol/sei-db]
Technology: ibc-go v7.x — IBC protocol implementation (HIGH) [Sei chain go.mod, https://github.com/sei-protocol/sei-chain/blob/main/go.mod]
Technology: Wormhole SDK / Core Bridge — Cross-chain messaging integration (HIGH) [Wormhole Sei integration, https://docs.wormhole.com/docs/build/sei]
Technology: Axelar SDK / GMP — General message passing integration (HIGH) [Axelar Sei docs, https://docs.axelar.dev/dev/gmp/sei]
Technology: Pyth Network Contract — On-chain price feed verification (HIGH) [Pyth Sei, https://docs.pyth.network/price-feeds/sei]
Technology: Chainlink CCIP / Price Feeds / VRF — Oracle infrastructure (HIGH) [Chainlink Sei, https://blog.chain.link/chainlink-sei-integration]
Technology: Docker — Containerized node deployment (HIGH) [Sei chain Dockerfile, https://github.com/sei-protocol/sei-chain/blob/main/Dockerfile; Sei docs run node, https://docs.sei.io/validators/run-node]
Technology: Kubernetes / Helm — Production validator and RPC node orchestration (MEDIUM) [Sei validator guides, https://docs.sei.io/validators; community Helm charts]
Technology: Prometheus / Grafana — Metrics and monitoring for validators (HIGH) [Sei validator monitoring, https://docs.sei.io/validators/monitoring]
Technology: Jaeger / OpenTelemetry — Distributed tracing for RPC nodes (MEDIUM) [Sei RPC operator guides]
Technology: NGINX / HAProxy — RPC load balancing and rate limiting (MEDIUM) [Sei RPC provider docs]
Technology: PostgreSQL / TimescaleDB — Indexer and analytics backend (MEDIUM) [Sei indexer implementations]
Technology: GraphQL (Apollo / Hasura) — Seitrace and custom indexer APIs (HIGH) [Seitrace GraphQL, https://seitrace.com/graphql]

## Known Technical Limitations

Limitation: Parallel Execution Conflict Rate — Under high contention (many txs touching same state), optimistic concurrency control aborts increase, reducing effective throughput; mitigated by Sei's order matching engine batching but not eliminated (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; parallel execution research]

Limitation: SeiDB Fast Sync Trust Assumption — Fast sync via state commit log (SCL) requires trusting a recent checkpoint; full verification still requires replay from genesis or trusted snapshot (HIGH) [SeiDB blog, https://sei.io/blog/introducing-sei-db; SeiDB repo README, https://github.com/sei-protocol/sei-db]

Limitation: EVM Precompile Gas Costs — Native Go precompiles have fixed gas costs that may not perfectly reflect actual computation cost; governance can adjust but requires on-chain proposal (HIGH) [Sei v2 docs precompiles, https://docs.sei.io/develop/evm/precompiles]

Limitation: CosmWasm-EVM Interoperability Latency — Cross-VM calls (CosmWasm ↔ EVM) require precompile dispatch and state synchronization via SeiDB; adds ~1-2 block latency vs. intra-VM calls (HIGH) [Sei v2 docs interoperability, https://docs.sei.io/develop/evm/interoperability]

Limitation: Validator Set Centralization Risk — Top validators by stake control consensus; delegation concentration can lead to <1/3 stake controlled by few entities; monitored but not protocol-enforced decentralization (HIGH) [Sei docs validators, https://docs.sei.io/learn/validators; staking explorer data]

Limitation: Bridge Trust Assumptions (Wormhole/Axelar) — Cross-chain bridges rely on external validator/guardian sets; not secured by Sei consensus; bridge hacks affect bridged assets on Sei (HIGH) [Wormhole security, https://docs.wormhole.com/docs/security; Axelar security, https://docs.axelar.dev/security]

Limitation: State Bloat Growth — Despite SeiDB improvements, state growth is unbounded with persistent contract deployments; no native state expiry / rent mechanism implemented (HIGH) [SeiDB blog, https://sei.io/blog/introducing-sei-db; Cosmos SDK state management]

Limitation: IBC Packet Timeout Handling — Application-level timeout logic required; packets can expire if counterparty chain stalls; no automatic refund for all packet types (HIGH) [IBC spec, https://ibc.cosmos.network/main/ibc/tao.html]

Limitation: Wasmer Determinism Across Architectures — WASM execution must produce identical results on all validator architectures (x86_64, ARM64); floating point and SIMD require careful handling (HIGH) [CosmWasm determinism, https://docs.cosmwasm.com/docs/1.0/smart-contracts/security#determinism]

Limitation: Governance Upgrade Coordination — Major upgrades (e.g., Sei v2) require coordinated validator software upgrade; network halt risk if >1/3 validators fail to upgrade in time (HIGH) [Sei upgrade governance proposals; Tendermint upgrade process]

## Official Technical Resources

Documentation: https://docs.sei.io
GitHub (Core): https://github.com/sei-protocol/sei-chain
GitHub (SeiDB): https://github.com/sei-protocol/sei-db
GitHub (Organization): https://github.com/sei-protocol
Developer Docs (CosmWasm): https://docs.sei.io/develop/cosmwasm
Developer Docs (EVM/Sei v2): https://docs.sei.io/learn/sei-v2
Developer Docs (EVM Precompiles): https://docs.sei.io/develop/evm/precompiles
Developer Docs (EVM Tooling): https://docs.sei.io/develop/evm/hardhat
Developer Docs (Token Factory): https://docs.sei.io/develop/token-factory
Developer Docs (RPC/API): https://docs.sei.io/develop/rpc
Developer Docs (IBC): https://docs.sei.io/learn/architecture#ibc
SDK (JavaScript/TypeScript): https://github.com/sei-protocol/sei.js
SDK (TypeScript): https://github.com/sei-protocol/sei.ts
SDK (Python Community): https://github.com/sei-protocol
Whitepaper: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md
Research Paper (Parallel Execution): Not separately published; technical details in whitepaper and blog
Blog (Technical Announcements): https://sei.io/blog
Explorer (Mainnet GraphQL): https://seitrace.com/graphql
Explorer (Testnet GraphQL): https://testnet.seitrace.com/graphql
Validator Docs: https://docs.sei.io/validators
Staking Docs: https://docs.sei.io/learn/staking
Wallet Integration Docs: https://docs.sei.io/learn/wallets

## Ringkasan

Architecture: Layer 1 (Cosmos SDK) with parallel execution, native order matching, dual VM (CosmWasm + EVM via Geth), modular storage (SeiDB), IBC native, external bridges (Wormhole, Axelar), dual oracle (Pyth, Chainlink)

Core Components: 13 (Sei Chain, Tendermint, Parallel Execution Engine, Order Matching Engine, CosmWasm VM, Sei v2 EVM/Geth, Precompiles, SeiDB, IBC Module, Wormhole Bridge, Axelar Bridge, Pyth Oracle, Chainlink Oracle, Token Factory)

Audit Count: 6 core protocol audits (Informal Systems, Halborn, Trail of Bits, Oak Security, Zellic, Veridise) + ecosystem audits

Major Upgrade Count: 4 completed major upgrades (Atlantic-1 testnet, Pacific-1 mainnet, Sei v2 testnet, Sei v2 mainnet) + 3 planned/ongoing

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Sei

## Funding History

Funding Round: Series A
Date: 2022-08
Amount: $5,000,000
Currency: USD
Lead Investor: Multicoin Capital
Participating Investors: Delphi Digital, Hypersphere Ventures, Distributed Global, Flow Traders, Hudson River Trading, GSR, Kronos Research, NGC Ventures, CoinFund, Animoca Brands, OKX Ventures, Huobi Ventures, Gate.io Labs, Bybit, KuCoin Ventures, MEXC Global, Bitget, BingX, P2P Validator, Figment, Chorus One, Stake Capital, Luganodes, Blockdaemon, Kiln, Everstake, P2P.org, Node Capital, Foresight Ventures, HashKey Capital, SNZ Holding, Signum Capital, Waterdrip Capital, Moonrock Capital, Spartan Group, CMS Holdings, Jane Street, Wintermute, Amber Group, B2C2, Flow Traders, GSR, Kronos Research (HIGH) [Sei blog Series A announcement, https://sei.io/blog/sei-raises-5m-series-a; Multicoin Capital portfolio, https://multicoin.capital/portfolio/sei; CoinDesk coverage, https://www.coindesk.com/business/2022/08/23/sei-network-raises-5m-from-multicoin-delphi-digital-and-others-for-trading-focused-blockchain/]
Valuation: tidak diungkap
Funding Type: Series A
Status: Completed
Sources: https://sei.io/blog/sei-raises-5m-series-a

---

Funding Round: Series B
Date: 2022-04 (announced 2022-08 alongside Series A)
Amount: $30,000,000
Currency: USD
Lead Investor: Jump Crypto
Participating Investors: Multicoin Capital, Delphi Digital, Distributed Global, Flow Traders, Hudson River Trading, GSR, Kronos Research, NGC Ventures, CoinFund, Animoca Brands, OKX Ventures, Huobi Ventures, Gate.io Labs, Bybit, KuCoin Ventures, MEXC Global, Bitget, BingX, P2P Validator, Figment, Chorus One, Stake Capital, Luganodes, Blockdaemon, Kiln, Everstake, P2P.org, Node Capital, Foresight Ventures, HashKey Capital, SNZ Holding, Signum Capital, Waterdrip Capital, Moonrock Capital, Spartan Group, CMS Holdings, Jane Street, Wintermute, Amber Group, B2C2 (HIGH) [Sei blog Series A announcement mentions $35M total, https://sei.io/blog/sei-raises-5m-series-a; The Block coverage, https://www.theblock.co/post/160999/sei-network-raises-35m-series-a-and-b-from-jump-crypto-multicoin-and-others; CoinDesk coverage, https://www.coindesk.com/business/2022/08/23/sei-network-raises-5m-from-multicoin-delphi-digital-and-others-for-trading-focused-blockchain/]
Valuation: tidak diungkap
Funding Type: Series B
Status: Completed
Sources: https://sei.io/blog/sei-raises-5m-series-a

---

Funding Round: Strategic Round / Private Sale (Token Allocation)
Date: 2022-Q2 hingga 2023-Q1 (pre-TGE)
Amount: tidak diungkap sebagai jumlah uang tunai terpisah — tercakup dalam $35M total Series A+B dengan alokasi token untuk investor
Currency: USD (setara)
Lead Investor: Jump Crypto, Multicoin Capital
Participating Investors: Investor Series A+B di atas menerima alokasi token SEI sebagai bagian dari kesepakatan investasi equity + token (HIGH) [Sei whitepaper tokenomics section, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei blog Series A, https://sei.io/blog/sei-raises-5m-series-a]
Valuation: tidak diungkap (token valuation terpisah dari equity valuation)
Funding Type: Strategic / Private Sale (token allocation)
Status: Completed
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

---

Funding Round: Community / Public Allocation (TGE via Binance Launchpool / Spot Listing)
Date: 2023-08-15
Amount: tidak diungkap (volume trading awal bukan pendanaan langsung ke Sei Labs)
Currency: USD
Lead Investor: Binance (exchange listing, bukan investor equity)
Participating Investors: Publik retail melalui Binance spot trading
Valuation: Price discovery dimulai pada listing
Funding Type: Public Sale / Exchange Listing (TGE)
Status: Completed
Sources: https://www.binance.com/en/blog/spotlight/sei-sei-326868

---

Funding Round: Ecosystem Fund / Grant Program
Date: 2023-Q4 hingga sekarang
Amount: $50,000,000 (diumumkan sebagai Sei Ecosystem Fund)
Currency: USD
Lead Investor: Sei Labs / Sei Foundation (dana ekosistem dari treasury protokol)
Participating Investors: N/A (dana internal untuk grant ke builder)
Valuation: N/A
Funding Type: Grant / Treasury Injection (Ecosystem Fund)
Status: Ongoing
Sources: https://sei.io/blog/sei-ecosystem-fund; https://docs.sei.io/learn/ecosystem-fund

---

## Treasury

Current Treasury Size: tidak diungkap secara resmi pada dashboard publik
Treasury Composition: tidak diungkap
Stablecoin Holdings: tidak diungkap
Native Token Holdings: tidak diungkap (wallet treasury Sei Labs / Sei Foundation tidak dipublikasikan dengan label eksplisit)
Other Assets: tidak diungkap
Treasury Custodian: tidak diungkap (kemungkinan multi-sig Gnosis Safe atau custodian institusional seperti Fireblocks / Copper / Anchorage — tidak dikonfirmasi)
Sources: Tidak diungkap.

---

## Revenue Model

Nama: Transaction Fees (Gas Fees)
Status: Live
Description: Setiap transaksi di Sei (CosmWasm, EVM, native modules) membayar gas fee dalam SEI (usei); fee dibagi ke validator dan community pool melalui modul distribution Cosmos SDK (HIGH) [Sei docs fees, https://docs.sei.io/learn/fees; Cosmos SDK distribution module, https://docs.cosmos.network/main/modules/distribution]
Sources: https://docs.sei.io/learn/fees

---

Nama: Order Matching Engine Fees (Native DEX Module)
Status: Live
Description: Built-in order matching engine mengambil fee pada setiap matched order; fee masuk ke community pool / treasury protokol (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei docs order matching, https://docs.sei.io/learn/architecture#order-matching]
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

---

Nama: IBC Relayer Fees / Packet Fees
Status: Live
Description: IBC packet transfer收取 relayer fees dan acknowledgment fees; sebagian dialokasikan ke community pool (HIGH) [Sei docs IBC, https://docs.sei.io/learn/architecture#ibc; IBC spec fees, https://ibc.cosmos.network/main/ibc/tao.html#fees]
Sources: https://docs.sei.io/learn/architecture#ibc

---

Nama: Bridge Fees (Wormhole / Axelar)
Status: Live
Description: Bridge fees dibayar user ke Wormhole Guardian network / Axelar validators; Sei tidak langsung menerima bridge fees kecuali melalui token factory fees untuk mint/burn bridged token (MEDIUM) [Wormhole fees docs, https://docs.wormhole.com/docs/build/sei; Axelar GMP fees, https://docs.axelar.dev/dev/gmp/fees]
Sources: https://docs.wormhole.com/docs/build/sei

---

Nama: MEV / Priority Fees (EVM via Sei v2)
Status: Live (sejak Sei v2 mainnet upgrade 2024-08-15)
Description: EVM transactions bisa include priority fee (tip) ke proposer/validator; base fee burned (EIP-1559 model) atau ke community pool tergantung implementasi Sei v2 (HIGH) [Sei v2 docs fees, https://docs.sei.io/develop/evm/fees; Sei v2 blog, https://sei.io/blog/introducing-sei-v2]
Sources: https://docs.sei.io/develop/evm/fees

---

Nama: Staking Commission (Validator Commission)
Status: Live
Description: Validator mengambil commission dari staking rewards delegator; protokol tidak langsung menerima kecuali melalui community pool tax (jika diaktifkan governance) (HIGH) [Sei docs staking, https://docs.sei.io/learn/staking]
Sources: https://docs.sei.io/learn/staking

---

Nama: Treasury Yield (Staking Rewards on Protocol-Owned SEI)
Status: Planned / Tidak dikonfirmasi live
Description: Jika Sei Labs / Sei Foundation menyimpan SEI dan mendelegasikannya, staking rewards menjadi yield treasury — tidak ada disclosure resmi bahwa ini dilakukan (LOW) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

---

Nama: Enterprise / Institutional Services
Status: tidak diungkap / tidak dikonfirmasi
Description: Sei Labs mungkin menawarkan layanan infrastruktur (RPC, indexing, validator ops) ke institusi — tidak dipublikasikan sebagai revenue stream resmi (LOW)
Sources: Tidak diungkap.

---

## Revenue History

Tidak diungkap.
Sources: Tidak diungkap.

---

## Fundraising Mechanism

VC Funding: Series A ($5M) dan Series B ($30M) dari investor crypto-native (Jump Crypto, Multicoin Capital, dll) — equity + token allocation (HIGH) [Sei blog Series A, https://sei.io/blog/sei-raises-5m-series-a]
Private Sale: Token allocation untuk investor Series A+B sebagai bagian dari deal equity (tidak ada private sale terpisah yang terpisah dari equity rounds) (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Public Sale: Tidak ada public sale terpisah (seperti ICO/IDO); TGE dilakukan via Binance spot listing sekaligus mainnet launch — price discovery pasar (HIGH) [Binance announcement, https://www.binance.com/en/blog/spotlight/sei-sei-326868]
Grant: Sei Ecosystem Fund $50M untuk grant ke builder ekosistem (dana dari treasury protokol) (HIGH) [Sei ecosystem fund blog, https://sei.io/blog/sei-ecosystem-fund]
Foundation: Sei Foundation (entitas terpisah yang tidak dikonfirmasi publik) atau Sei Labs mengelola treasury protokol untuk funding ekosistem (MEDIUM) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Protocol Revenue: Transaction fees, order matching fees, IBC fees, EVM priority fees — masuk ke community pool (HIGH) [Sei docs fees, https://docs.sei.io/learn/fees]
Bootstrapping: Core development dibiayai oleh Series A+B ($35M total) sebelum mainnet launch (HIGH) [Sei blog Series A, https://sei.io/blog/sei-raises-5m-series-a]

---

## Token Sale

Private Sale: Tidak ada private sale token terpisah dari equity rounds; investor Series A+B menerima token allocation sebagai bagian dari kesepakatan investasi (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei blog Series A, https://sei.io/blog/sei-raises-5m-series-a]
Public Sale: Tidak ada public sale (ICO/IDO/Launchpad); TGE via Binance spot listing 2023-08-15 (HIGH) [Binance announcement, https://www.binance.com/en/blog/spotlight/sei-sei-326868]
Launchpad: Binance Launchpool TIDAK digunakan untuk SEI (Binance Launchpool biasanya untuk farming pre-listing; SEI listed langsung spot) (HIGH) [Binance announcement, https://www.binance.com/en/blog/spotlight/sei-sei-326868]
Auction: Tidak ada auction (Dutch auction, batch auction, dll) untuk token sale (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Community Sale: Tidak ada community sale terpisah; community allocation didistribusikan via airdrop, testnet incentives, ecosystem grants post-TGE (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Tanggal: 2023-08-15 (TGE / Mainnet Launch / Binance Listing)
Status: Completed
Sources: https://www.binance.com/en/blog/spotlight/sei-sei-326868
Catatan: Distribusi token (persentase team, investor, community, foundation) dan jadwal vesting dibahas di Phase 6 (Tokenomics), bukan di sini.

---

## Financial Dependencies

VC: Jump Crypto (Series B lead), Multicoin Capital (Series A lead) — equity stake + token allocation (HIGH) [Sei blog Series A, https://sei.io/blog/sei-raises-5m-series-a]
Foundation: Sei Foundation (entitas yang diasumsikan ada tapi tidak dikonfirmasi publik terpisah dari Sei Labs) — mengelola treasury protokol dan ecosystem fund (MEDIUM) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Grant Program: Sei Ecosystem Fund ($50M) — dana untuk builder ekosistem (HIGH) [Sei ecosystem fund blog, https://sei.io/blog/sei-ecosystem-fund]
Revenue: Protocol fees (gas, order matching, IBC, EVM priority fees) — masuk community pool, dikelola governance (HIGH) [Sei docs fees, https://docs.sei.io/learn/fees]
DAO: Sei Governance (token holder voting via Cosmos SDK governance module) — mengontrol community pool spending, parameter changes, upgrade (HIGH) [Sei docs governance, https://docs.sei.io/learn/governance]
Sources: https://sei.io/blog/sei-raises-5m-series-a, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/sei-ecosystem-fund, https://docs.sei.io/learn/fees, https://docs.sei.io/learn/governance

---

## Financial Risk

Treasury Concentration: Tidak diungkap — wallet treasury Sei Labs / Sei Foundation tidak dipublikasikan; tidak bisa diverifikasi apakah treasury terpusat di sedikit multi-sig atau terdistribusi (LOW) [Tidak ada sumber resmi]
Revenue Decline: Tidak diungkap — tidak ada laporan revenue berkala (bulanan/tahunan) dari Sei Labs atau Foundation; revenue bergantung pada aktivitas on-chain yang volatil (LOW) [Tidak ada sumber resmi]
Funding Dependency: Core development bergantung pada dana Series A+B ($35M) dan ecosystem fund ($50M) — tidak ada revenue berbagi model yang dikonfirmasi membiayai ops core team secara berkelanjutan (MEDIUM) [Sei blog Series A, https://sei.io/blog/sei-raises-5m-series-a; Sei ecosystem fund blog, https://sei.io/blog/sei-ecosystem-fund]
Debt: Tidak diungkap — tidak ada disclosure pinjaman atau instrumen hutang oleh Sei Labs Inc. (LOW) [Tidak ada sumber resmi]
Legal Financial Risk: Sei Labs Inc. terdaftar di Delaware, AS — tunduk pada regulasi SEC terkait token offering (Howey test) dan pengungkapan keuangan jika dianggap security; tidak ada enforcement action publik per knowledge cutoff (MEDIUM) [Delaware registry, https://opencorporates.com/companies/us_de/7465721; SEC framework digital assets, https://www.sec.gov/files/framework-investment-contract-analysis-digital-assets.pdf]
Bridge Counterparty Risk: Bridged assets (SEI di Ethereum, Solana, dll) bergantung keamanan Wormhole/Axelar — hack bridge mempengaruhi nilai aset bridged di Sei (HIGH) [Wormhole security, https://docs.wormhole.com/docs/security; Axelar security, https://docs.axelar.dev/security]
Sources: https://opencorporates.com/companies/us_de/7465721, https://sei.io/blog/sei-raises-5m-series-a, https://sei.io/blog/sei-ecosystem-fund, https://docs.wormhole.com/docs/security, https://docs.axelar.dev/security

---

## Official Financial Resources

Official Blog: https://sei.io/blog
Transparency Report: Tidak ada (tidak dipublikasikan)
Treasury Dashboard: Tidak ada (tidak dipublikasikan)
Governance: https://docs.sei.io/learn/governance (Cosmos SDK governance module; proposal on-chain di Seitrace)
Messari: https://messari.io/asset/sei (Messari research reports, beberapa memerlukan langganan)
Token Terminal: https://tokenterminal.com/terminal/projects/sei (Revenue/fees dashboard on-chain)
DefiLlama: https://defillama.com/chain/Sei (TVL, fees, revenue protokol DeFi di Sei — bukan revenue Sei Labs)
CryptoRank: https://cryptorank.io/ico/sei-network (Funding rounds, token sale data — perlu cross-check)
Whitepaper: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md (Tokenomics section)
Sei Ecosystem Fund: https://sei.io/blog/sei-ecosystem-fund
Sei Docs Fees: https://docs.sei.io/learn/fees
Sei Docs Governance: https://docs.sei.io/learn/governance
Seitrace Governance Proposals: https://seitrace.com/gov

---

## Ringkasan

Total Funding Raised: $35,000,000 (Series A $5M + Series B $30M) — equity rounds dengan token allocation; ditambah $50,000,000 Ecosystem Fund dari treasury protokol (bukan fresh capital)
Funding Rounds: 2 equity rounds (Series A Aug 2022, Series B Apr 2022) + 1 ecosystem fund announcement (2023-Q4)
Treasury Status: Tidak diungkap (ukuran, komposisi, custodian)
Revenue Sources: Transaction fees (gas), Order matching fees, IBC packet fees, EVM priority fees (Sei v2), Staking commission (validator-level, bukan protokol) — semua masuk community pool kelola governance
Revenue Availability: Tidak diungkap — tidak ada laporan revenue resmi; on-chain fees terlihat via Token Terminal / DefiLlama tapi tidak diekspor sebagai laporan keuangan entitas

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Sei

## Token Information

Official Token Name: Sei
Symbol: SEI
Token Standard: Native Cosmos SDK coin (denom: usei); ERC-20 on Ethereum (0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5); SPL on Solana via Wormhole (HIGH) [Sei docs tokenomics, https://docs.sei.io/learn/tokenomics; Etherscan, https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5]
Blockchain: Sei Network (native, Pacific-1); Ethereum (ERC-20 bridged); Solana (SPL bridged); Arbitrum, Optimism, Base, BSC, Polygon (bridged via Wormhole/Axelar) (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture]
Contract Address: Native: usei (denom); Ethereum ERC-20: 0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5; Solana SPL: wormhole wrapped (address varies by bridge deployment) (HIGH) [Etherscan, https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5; Wormhole portal, https://portalbridge.com]
Decimals: 6 (usei = 10^-6 SEI) (HIGH) [Sei docs tokenomics, https://docs.sei.io/learn/tokenomics; Sei chain genesis, https://github.com/sei-protocol/sei-chain/blob/main/networks/pacific-1/genesis.json]
Status: Live (HIGH) [Sei mainnet launch blog, https://sei.io/blog/sei-mainnet-launch]
Sources: https://docs.sei.io/learn/tokenomics, https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5, https://sei.io/blog/sei-mainnet-launch

## Supply

Maximum Supply: 10,000,000,000 SEI (10 billion) (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei docs tokenomics, https://docs.sei.io/learn/tokenomics]
Total Supply: 10,000,000,000 SEI (minted at genesis) (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Genesis file, https://github.com/sei-protocol/sei-chain/blob/main/networks/pacific-1/genesis.json]
Circulating Supply: ~3,300,000,000 SEI (estimated as of 2024-Q3; increases with vesting unlocks) (MEDIUM) [CoinGecko circulating supply, https://www.coingecko.com/en/coins/sei-network; Token Terminal, https://tokenterminal.com/terminal/projects/sei]
Initial Supply: 10,000,000,000 SEI (full max supply minted at genesis; distribution via vesting) (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Supply Type: Inflationary (staking rewards mint new SEI; no hard cap beyond initial 10B; inflation rate set by governance) (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Cosmos SDK mint module, https://docs.cosmos.network/main/modules/mint]
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://docs.sei.io/learn/tokenomics, https://www.coingecko.com/en/coins/sei-network, https://tokenterminal.com/terminal/projects/sei

## Distribution

Community: 48% (4,800,000,000 SEI) — includes airdrops, testnet incentives, ecosystem grants, liquidity mining, community pool (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei blog tokenomics, https://sei.io/blog/sei-tokenomics]
Team: 20% (2,000,000,000 SEI) — Sei Labs core team and contributors (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Investors: 22% (2,200,000,000 SEI) — Series A and Series B equity investors (Jump Crypto, Multicoin Capital, Delphi Digital, etc.) (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei blog Series A, https://sei.io/blog/sei-raises-5m-series-a]
Foundation: 10% (1,000,000,000 SEI) — Sei Foundation / protocol treasury for ecosystem development (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Treasury: Included in Foundation/Community allocation; separate protocol-owned treasury not distinctly broken out in whitepaper (MEDIUM) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Ecosystem: Included in Community (48%) — ecosystem fund grants, builder incentives, liquidity bootstrapping (HIGH) [Sei ecosystem fund blog, https://sei.io/blog/sei-ecosystem-fund; Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Advisors: Not separately allocated in whitepaper; may be part of Team or Investors allocation (LOW) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Other: Not specified (LOW) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://docs.sei.io/learn/tokenomics, https://sei.io/blog/sei-tokenomics, https://sei.io/blog/sei-raises-5m-series-a, https://sei.io/blog/sei-ecosystem-fund

## Vesting Schedule

Category: Community (48%)
Cliff: 0 months (partial unlock at TGE for airdrop/testnet rewards)
Vesting: 36–60 months linear for ecosystem grants/liquidity mining; airdrop portions vary
Unlock Frequency: Monthly/quarterly for programmatic distributions
Current Status: Ongoing — airdrop/testnet rewards partially unlocked; ecosystem fund deploying over years
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/sei-tokenomics

Category: Team (20%)
Cliff: 12 months
Vesting: 36 months linear after cliff (total 48 months)
Unlock Frequency: Monthly
Current Status: Cliff passed (Aug 2024); monthly vesting active
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/sei-tokenomics

Category: Investors (22%)
Cliff: 12 months
Vesting: 24–36 months linear after cliff (varies by round)
Unlock Frequency: Monthly
Current Status: Cliff passed (Aug 2024); monthly vesting active
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/sei-tokenomics

Category: Foundation (10%)
Cliff: 0 months (partial for immediate ecosystem ops)
Vesting: 60 months linear for remainder
Unlock Frequency: Monthly
Current Status: Ongoing — used for ecosystem fund, grants, operations
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/sei-ecosystem-fund

## TGE

TGE Date: 2023-08-15 (EV-004) (HIGH) [Sei mainnet launch blog, https://sei.io/blog/sei-mainnet-launch]
Initial Unlock: ~15–20% of total supply (estimated: airdrop recipients, testnet incentives, initial liquidity, Binance listing allocation) (MEDIUM) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Binance announcement, https://www.binance.com/en/blog/spotlight/sei-sei-326868]
Unlocked Categories: Community airdrop/testnet rewards; initial liquidity for DEX/CEX; Binance listing allocation; Foundation operational treasury (HIGH) [Sei blog tokenomics, https://sei.io/blog/sei-tokenomics; Binance announcement, https://www.binance.com/en/blog/spotlight/sei-sei-326868]
Launch Platform: Binance Spot Listing (SEI/USDT, SEI/BUSD, SEI/BNB) — no Launchpool, no public sale (HIGH) [Binance announcement, https://www.binance.com/en/blog/spotlight/sei-sei-326868]
Status: Completed (HIGH) [Sei mainnet launch blog, https://sei.io/blog/sei-mainnet-launch]
Sources: https://sei.io/blog/sei-mainnet-launch, https://www.binance.com/en/blog/spotlight/sei-sei-326868, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

## Utility

Utility: Gas Fee Payment
Deskripsi: Semua transaksi di Sei (CosmWasm, EVM, native modules, IBC) membayar gas fee dalam SEI (denom: usei); fee dibagi ke validator dan community pool via distribution module (HIGH)
Status: Live
Sources: https://docs.sei.io/learn/fees, https://docs.sei.io/learn/architecture

Utility: Staking & Validator Bonding
Deskripsi: SEI di-stake ke validator untuk keamanan PoS; delegator menerima staking rewards; validator memerlukan bonded SEI untuk consensus participation (HIGH)
Status: Live
Sources: https://docs.sei.io/learn/staking, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

Utility: Governance Voting
Deskripsi: Pemegang SEI (staked) dapat vote pada proposal governance via Cosmos SDK governance module (parameter changes, upgrades, community pool spend) (HIGH)
Status: Live
Sources: https://docs.sei.io/learn/governance, https://seitrace.com/gov

Utility: Order Matching Engine Fees
Deskripsi: Built-in order matching engine (native module) mengambil fee pada matched order; fee masuk community pool (HIGH)
Status: Live
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://docs.sei.io/learn/architecture#order-matching

Utility: EVM Priority Fees (Sei v2)
Deskripsi: Transaksi EVM bisa include priority fee (tip) ke proposer; base fee burned atau ke community pool per EIP-1559 model Sei v2 (HIGH)
Status: Live (sejak Sei v2 mainnet upgrade 2024-08-15, EV-020)
Sources: https://docs.sei.io/develop/evm/fees, https://sei.io/blog/introducing-sei-v2

Utility: IBC Relayer / Packet Fees
Deskripsi: IBC packet transfer membayar relayer fees dan acknowledgment fees dalam SEI; sebagian ke community pool (HIGH)
Status: Live
Sources: https://docs.sei.io/learn/architecture#ibc, https://ibc.cosmos.network/main/ibc/tao.html#fees

Utility: Token Factory Denom Creation
Deskripsi: Membuat token native via Token Factory module membayar fee dalam SEI; digunakan untuk bridged token representation (HIGH)
Status: Live
Sources: https://docs.sei.io/develop/token-factory, https://github.com/sei-protocol/sei-chain/tree/main/x/tokenfactory

Utility: Collateral (DeFi)
Deskripsi: SEI digunakan sebagai collateral di lending protocols (Silo Finance), perp DEX (Leviathan), dan yield strategies (Yei Finance) (HIGH)
Status: Live
Sources: https://docs.silo.finance, https://leviathan.gg, https://yei.finance

Utility: Liquidity Provision
Deskripsi: SEI dipasangkan di liquidity pools (DragonSwap, dll) untuk trading fees dan LP rewards (HIGH)
Status: Live
Sources: https://dragonswap.app, https://sei.io/ecosystem

Utility: Bridge Asset (Cross-chain)
Deskripsi: SEI dibridge ke Ethereum, Solana, Arbitrum, Optimism, Base, BSC, Polygon via Wormhole/Axelar sebagai wrapped asset (HIGH)
Status: Live
Sources: https://docs.sei.io/learn/architecture, https://portalbridge.com

## Governance

Governance Model: Token-weighted voting via Cosmos SDK Governance Module (on-chain) (HIGH) [Sei docs governance, https://docs.sei.io/learn/governance; Cosmos SDK governance, https://docs.cosmos.network/main/modules/gov]
Voting System: 1 staked SEI = 1 vote; delegators inherit validator vote unless they override; voting period typically 14 days (HIGH) [Sei docs governance, https://docs.sei.io/learn/governance; Seitrace proposals, https://seitrace.com/gov]
Voting Power: Proportional to staked SEI (bonded tokens); unbonded SEI tidak memiliki voting power (HIGH) [Cosmos SDK governance, https://docs.cosmos.network/main/modules/gov]
Delegation: Delegator dapat redelegate ke validator lain kapan saja (unbonding period 21 hari); delegator bisa override vote validator pada proposal spesifik (HIGH) [Sei docs staking, https://docs.sei.io/learn/staking; Cosmos SDK staking, https://docs.cosmos.network/main/modules/staking]
Proposal System: Siapapun dengan deposit minimum (parameter governance, saat ini ~1000 SEI) bisa submit proposal; jenis: Text, Parameter Change, Software Upgrade, Community Pool Spend (HIGH) [Sei docs governance, https://docs.sei.io/learn/governance; Seitrace proposals, https://seitrace.com/gov]
Treasury Governance: Community Pool (mengumpulkan fee distribution) dikelola via governance proposals; Foundation/team allocation tidak langsung dikontrol governance (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Cosmos SDK distribution, https://docs.cosmos.network/main/modules/distribution]
Status: Live (HIGH) [Seitrace governance, https://seitrace.com/gov]
Sources: https://docs.sei.io/learn/governance, https://docs.sei.io/learn/staking, https://seitrace.com/gov, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

## Inflation / Deflation

Inflation Mechanism: Staking rewards minted via Cosmos SDK Mint Module; inflation rate target 7% tahunan (adjustable governance) bonded ratio target 67% (HIGH) [Sei whitepaper tokenomics, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Cosmos SDK mint module, https://docs.cosmos.network/main/modules/mint]
Emission Schedule: Block provisions minted per block; distributed to stakers (rewards) dan community pool (tax); inflation berkurang seiring bonded ratio meningkat (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Cosmos SDK mint, https://docs.cosmos.network/main/modules/mint]
Burn Mechanism: EVM base fee (Sei v2 EIP-1559) burned; tidak ada burn mechanism untuk native CosmWasm/native tx fees (fee ke validator + community pool) (HIGH) [Sei v2 docs fees, https://docs.sei.io/develop/evm/fees; Sei v2 blog, https://sei.io/blog/introducing-sei-v2]
Buyback: Tidak ada program buyback resmi dari protocol/Foundation (LOW) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei blog, https://sei.io/blog]
Supply Reduction: Hanya melalui EVM base fee burn; net supply tetap inflationary karena staking rewards > burn (MEDIUM) [Sei v2 docs, https://docs.sei.io/develop/evm/fees; Token Terminal supply data, https://tokenterminal.com/terminal/projects/sei]
Status: Live (inflationary dengan partial burn di EVM) (HIGH)
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://docs.sei.io/develop/evm/fees, https://docs.cosmos.network/main/modules/mint, https://tokenterminal.com/terminal/projects/sei

## Holder Distribution

Top Holder Concentration: Top 10 alamat memegang ~35–40% total supply (termasuk Foundation, vesting contracts, exchange wallets, bridge contracts) (MEDIUM) [Seitrace rich list, https://seitrace.com/tokens; Etherscan SEI token holders, https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5#balances]
Foundation Holding: ~10% (1B SEI) dalam vesting contract / multi-sig; exact address tidak dipublikasikan dengan label resmi (MEDIUM) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Investor Holding: ~22% (2.2B SEI) dalam vesting contracts untuk Series A/B investors; unlock bulanan sejak Aug 2024 (MEDIUM) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Treasury Holding: Community Pool on-chain address (cosmos1... distribution module) memegang accumulated fees; jumlah bervariasi (MEDIUM) [Seitrace community pool, https://seitrace.com; Cosmos SDK distribution module]
Community Holding: ~48% (4.8B SEI) tersebar di airdrop recipients, stakers, LP, ecosystem grants, 未分��� ecosystem fund (MEDIUM) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Whale Concentration: Gini coefficient tidak dipublikasikan; top validator operators dan exchange wallets (Binance, dll) merupakan largest non-vesting holders (LOW) [Seitrace validators, https://seitrace.com/validators; Etherscan holders, https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5#balances]
Sources: https://seitrace.com/tokens, https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5#balances, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://seitrace.com/validators

## Major Token Events

Date: 2023-08-15
Event: TGE & Mainnet Launch (EV-004)
Description: Genesis mint 10B SEI; initial unlock untuk airdrop, liquidity, Binance listing; staking live
Status: Completed
Related Historical Event ID: EV-004
Sources: https://sei.io/blog/sei-mainnet-launch

Date: 2023-08-15
Event: Binance Spot Listing (EV-005)
Description: SEI listed di Binance (SEI/USDT, SEI/BUSD, SEI/BNB) saat TGE; price discovery dimulai
Status: Completed
Related Historical Event ID: EV-005
Sources: https://www.binance.com/en/blog/spotlight/sei-sei-326868

Date: 2023-08
Event: ERC-20 Deploy Ethereum (EV-006)
Description: SEI ERC-20 contract deployed di Ethereum mainnet untuk bridging via Wormhole/Axelar
Status: Completed
Related Historical Event ID: EV-006
Sources: https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5

Date: 2023-08
Event: IBC Native Activation (EV-007)
Description: IBC transfer enabled untuk SEI native ke Cosmos ecosystem chains
Status: Completed
Related Historical Event ID: EV-007
Sources: https://docs.sei.io/learn/architecture

Date: 2023-08
Event: Wormhole/Axelar Bridge Integration (EV-008)
Description: SEI bridging ke Ethereum, Solana, Arbitrum, Optimism, Base, BSC, Polygon diaktifkan
Status: Completed
Related Historical Event ID: EV-008
Sources: https://docs.sei.io/learn/architecture

Date: 2024-08-15
Event: Sei v2 Mainnet Upgrade (EV-020)
Description: EVM compatibility live; EVM base fee burn mechanism aktif; SeiDB activated; MetaMask support
Status: Completed
Related Historical Event ID: EV-020
Sources: https://sei.io/blog/introducing-sei-v2

Date: 2024-08 (estimated)
Event: Team/Investor Cliff End (12-month cliff)
Description: Team (20%) dan Investor (22%) allocation cliff berakhir; monthly linear vesting dimulai
Status: Completed
Related Historical Event ID: (not in Phase 3 — derived from vesting schedule)
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

Date: 2023-Q4
Event: Sei Ecosystem Fund Announcement ($50M)
Description: Dana ekosistem $50M dari treasury untuk grant builder; community allocation deployment dipercepat
Status: Ongoing
Related Historical Event ID: (not in Phase 3 — from Phase 5)
Sources: https://sei.io/blog/sei-ecosystem-fund

## Official Token Resources

Official Documentation: https://docs.sei.io/learn/tokenomics
Whitepaper: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md
Governance: https://docs.sei.io/learn/governance
Explorer (Mainnet): https://seitrace.com
Explorer (Token Holdings): https://seitrace.com/tokens
Contract (Native): usei (denom, no contract address)
Contract (Ethereum ERC-20): https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5
GitHub (Core): https://github.com/sei-protocol/sei-chain
GitHub (Token Factory Module): https://github.com/sei-protocol/sei-chain/tree/main/x/tokenfactory
Dashboard (Token Terminal): https://tokenterminal.com/terminal/projects/sei
Dashboard (DefiLlama): https://defillama.com/chain/Sei
Dashboard (CoinGecko): https://www.coingecko.com/en/coins/sei-network
Dashboard (Seitrace Governance): https://seitrace.com/gov

## Ringkasan

Status: Live (mainnet sejak 2023-08-15; Sei v2 upgrade 2024-08-15)
Supply Type: Inflationary (staking rewards minting; partial EVM base fee burn)
Total Supply: 10,000,000,000 SEI (max supply = initial supply)
Distribution Categories: Community 48%, Team 20%, Investors 22%, Foundation 10%
Utility Count: 9 (Gas, Staking, Governance, Order Matching Fees, EVM Priority Fees, IBC Fees, Token Factory, Collateral, Liquidity, Bridge Asset)
Governance: On-chain token-weighted voting (Cosmos SDK Governance Module); community pool treasury management
Major Token Events: TGE/Mainnet Launch (EV-004), Binance Listing (EV-005), ERC-20 Deploy (EV-006), IBC Activation (EV-007), Bridge Integration (EV-008), Sei v2 Upgrade (EV-020), Team/Investor Cliff End (2024-08), Ecosystem Fund Announcement (2023-Q4)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Sei

## Ecosystem Position

Primary Sector: Layer 1 blockchain optimized for trading / high-performance DeFi (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei website, https://sei.io]
Secondary Sector: EVM-compatible execution environment (Sei v2); Cosmos ecosystem interoperability via IBC (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Sei docs architecture, https://docs.sei.io/learn/architecture]
Primary Chain: Sei Network (Pacific-1 mainnet, chain-id: pacific-1) (HIGH) [Sei mainnet launch blog, https://sei.io/blog/sei-mainnet-launch]
Supported Chains: Ethereum (ERC-20 bridge), Solana (SPL bridge), Arbitrum, Optimism, Base, BSC, Polygon (all via Wormhole/Axelar); Cosmos IBC-enabled chains (Osmosis, Juno, etc.) (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture; Wormhole portal, https://portalbridge.com; Axelar satellite, https://axelar.dev]
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io, https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/learn/architecture, https://sei.io/blog/sei-mainnet-launch, https://portalbridge.com, https://axelar.dev

## External Dependencies

Dependency Name: Tendermint / CometBFT
Dependency Type: Protocol
Purpose: Consensus engine providing BFT finality, block production, and ABCI++ interface for application layer (HIGH)
Criticality: Critical
Status: Live
Related Entity: CometBFT (formerly Tendermint Core)
Related Technology Component: Tendermint Consensus Engine
Sources: https://github.com/cometbft/cometbft, https://docs.sei.io/learn/architecture, https://github.com/sei-protocol/sei-chain/blob/main/go.mod

Dependency Name: Cosmos SDK
Dependency Type: Protocol
Purpose: Application framework for blockchain construction; module-based architecture (bank, staking, governance, IBC, tokenfactory, slashing, distribution, mint) (HIGH)
Criticality: Critical
Status: Live
Related Entity: Cosmos SDK
Related Technology Component: Sei Chain (Cosmos SDK Application)
Sources: https://github.com/cosmos/cosmos-sdk, https://github.com/sei-protocol/sei-chain/blob/main/go.mod, https://docs.cosmos.network

Dependency Name: Geth (go-ethereum)
Dependency Type: Protocol
Purpose: Embedded EVM execution client for Sei v2; enables native Ethereum transaction execution and JSON-RPC compatibility (HIGH)
Criticality: Critical
Status: Live
Related Entity: Ethereum
Related Technology Component: Sei v2 EVM Layer (Geth Integration)
Sources: https://github.com/ethereum/go-ethereum, https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/learn/sei-v2

Dependency Name: Wasmer
Dependency Type: Infrastructure
Purpose: WebAssembly runtime for CosmWasm smart contract execution; deterministic WASM execution across validator architectures (HIGH)
Criticality: Critical
Status: Live
Related Entity: Wasmer
Related Technology Component: CosmWasm VM (Wasmer)
Sources: https://github.com/wasmerio/wasmer, https://docs.cosmwasm.com/docs/1.0/getting-started/installation, https://github.com/sei-protocol/sei-chain/blob/main/go.mod

Dependency Name: IBC-Go
Dependency Type: Protocol
Purpose: Inter-Blockchain Communication protocol implementation for trust-minimized cross-chain asset/data transfer with Cosmos chains (HIGH)
Criticality: High
Status: Live
Related Entity: IBC
Related Technology Component: IBC Module (ibc-go)
Sources: https://github.com/cosmos/ibc-go, https://docs.sei.io/learn/architecture#ibc, https://github.com/sei-protocol/sei-chain/blob/main/go.mod

Dependency Name: Wormhole
Dependency Type: Bridge
Purpose: Generic message passing bridge for SEI token bridging and arbitrary cross-chain messages to Ethereum, Solana, EVM L2s via Guardian network (HIGH)
Criticality: High
Status: Live
Related Entity: Wormhole
Related Technology Component: Wormhole Bridge Integration
Sources: https://docs.wormhole.com, https://docs.sei.io/learn/architecture, https://portalbridge.com

Dependency Name: Axelar
Dependency Type: Bridge
Purpose: Cross-chain communication via Axelar validator network; supports general message passing and token bridging to EVM and Cosmos ecosystems (HIGH)
Criticality: High
Status: Live
Related Entity: Axelar
Related Technology Component: Axelar Bridge Integration
Sources: https://docs.axelar.dev, https://docs.sei.io/learn/architecture, https://axelar.dev

Dependency Name: Pyth Network
Dependency Type: Oracle
Purpose: First-party publisher price feeds pulled on-chain via Pyth contract; low-latency financial market data for DeFi applications (HIGH)
Criticality: High
Status: Live
Related Entity: Pyth Network
Related Technology Component: Pyth Network Oracle
Sources: https://docs.pyth.network, https://sei.io/ecosystem, https://docs.pyth.network/price-feeds/sei

Dependency Name: Chainlink
Dependency Type: Oracle
Purpose: Decentralized oracle network providing price feeds, VRF, CCIP, and automation on Sei (HIGH)
Criticality: High
Status: Live
Related Entity: Chainlink
Related Technology Component: Chainlink Oracle
Sources: https://blog.chain.link/chainlink-sei-integration, https://sei.io/ecosystem, https://docs.chain.link

Dependency Name: SeiDB
Dependency Type: Protocol
Purpose: Custom parallelized storage layer replacing IAVDB; separates state store (SS) and state commit log (SCL) for parallel writes, fast sync, state bloat reduction (HIGH)
Criticality: Critical
Status: Live
Related Entity: SeiDB
Related Technology Component: SeiDB (Parallelized Storage Layer)
Sources: https://github.com/sei-protocol/sei-db, https://sei.io/blog/introducing-sei-db, https://docs.sei.io/learn/architecture

Dependency Name: Docker
Dependency Type: Infrastructure
Purpose: Containerized node deployment for validators and RPC operators (HIGH)
Criticality: Medium
Status: Live
Related Entity: Docker
Related Technology Component: Node Deployment
Sources: https://github.com/sei-protocol/sei-chain/blob/main/Dockerfile, https://docs.sei.io/validators/run-node

Dependency Name: Kubernetes / Helm
Dependency Type: Infrastructure
Purpose: Production validator and RPC node orchestration (MEDIUM)
Criticality: Medium
Status: Live
Related Entity: Kubernetes
Related Technology Component: Validator Operations
Sources: https://docs.sei.io/validators, https://github.com/sei-protocol/sei-chain

Dependency Name: Prometheus / Grafana
Dependency Type: Infrastructure
Purpose: Metrics and monitoring for validators and RPC nodes (HIGH)
Criticality: Medium
Status: Live
Related Entity: Prometheus / Grafana
Related Technology Component: Validator Monitoring
Sources: https://docs.sei.io/validators/monitoring, https://prometheus.io, https://grafana.com

Dependency Name: NGINX / HAProxy
Dependency Type: Infrastructure
Purpose: RPC load balancing and rate limiting for public RPC providers (MEDIUM)
Criticality: Medium
Status: Live
Related Entity: NGINX / HAProxy
Related Technology Component: RPC Infrastructure
Sources: https://nginx.org, https://www.haproxy.org, https://docs.sei.io/validators

Dependency Name: PostgreSQL / TimescaleDB
Dependency Type: Infrastructure
Purpose: Indexer and analytics backend for on-chain data processing (MEDIUM)
Criticality: Medium
Status: Live
Related Entity: PostgreSQL / TimescaleDB
Related Technology Component: Indexing Infrastructure
Sources: https://www.postgresql.org, https://www.timescale.com, https://docs.sei.io/develop/rpc

Dependency Name: GraphQL (Apollo / Hasura)
Dependency Type: Infrastructure
Purpose: Seitrace and custom indexer APIs for on-chain data querying (HIGH)
Criticality: Medium
Status: Live
Related Entity: GraphQL
Related Technology Component: Explorer APIs
Sources: https://seitrace.com/graphql, https://www.apollographql.com, https://hasura.io

Sources: https://github.com/cometbft/cometbft, https://github.com/cosmos/cosmos-sdk, https://github.com/ethereum/go-ethereum, https://github.com/wasmerio/wasmer, https://github.com/cosmos/ibc-go, https://docs.wormhole.com, https://docs.axelar.dev, https://docs.pyth.network, https://blog.chain.link/chainlink-sei-integration, https://github.com/sei-protocol/sei-db, https://github.com/sei-protocol/sei-chain/blob/main/Dockerfile, https://docs.sei.io/validators/run-node, https://docs.sei.io/validators/monitoring, https://prometheus.io, https://grafana.com, https://nginx.org, https://www.haproxy.org, https://www.postgresql.org, https://www.timescale.com, https://seitrace.com/graphql, https://www.apollographql.com, https://hasura.io

## Major Integrations

Integration Name: Sei v2 EVM Compatibility (Geth Integration)
Integrated With: Ethereum (via Geth)
Purpose: Native EVM execution enabling Solidity/Vyper smart contracts to deploy and execute on Sei without modification; full Ethereum JSON-RPC compatibility (HIGH)
Status: Live
Related Historical Event ID: EV-016, EV-019, EV-020
Sources: https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/learn/sei-v2, https://github.com/sei-protocol/sei-chain

Integration Name: IBC Native Integration
Integrated With: Cosmos Hub, Osmosis, Juno, and other IBC-enabled chains
Purpose: Trust-minimized asset and data transfer between Sei and Cosmos ecosystem chains via light client verification (HIGH)
Status: Live
Related Historical Event ID: EV-007
Sources: https://docs.sei.io/learn/architecture#ibc, https://ibc.cosmos.network, https://seitrace.com/ibc

Integration Name: Wormhole Bridge Integration
Integrated With: Wormhole (Ethereum, Solana, Arbitrum, Optimism, Base, BSC, Polygon)
Purpose: SEI token bridging and general message passing to 7+ external chains via Guardian network (HIGH)
Status: Live
Related Historical Event ID: EV-008
Sources: https://docs.wormhole.com/docs/build/sei, https://portalbridge.com, https://docs.sei.io/learn/architecture

Integration Name: Axelar Bridge Integration
Integrated With: Axelar (Ethereum, Polygon, Arbitrum, Optimism, Base, BSC, Cosmos chains)
Purpose: Cross-chain communication via Axelar validator network; GMP and token bridging (HIGH)
Status: Live
Related Historical Event ID: EV-008
Sources: https://docs.axelar.dev/dev/gmp/sei, https://axelar.dev, https://docs.sei.io/learn/architecture

Integration Name: Pyth Network Oracle Integration
Integrated With: Pyth Network
Purpose: On-chain price feeds for DeFi applications (DEX, lending, perps) via publisher-signed aggregates (HIGH)
Status: Live
Related Historical Event ID: EV-009
Sources: https://docs.pyth.network/price-feeds/sei, https://sei.io/ecosystem, https://pyth.network

Integration Name: Chainlink Oracle Integration
Integrated With: Chainlink
Purpose: Price feeds, VRF, CCIP, and automation for Sei DeFi applications (HIGH)
Status: Live
Related Historical Event ID: EV-009
Sources: https://blog.chain.link/chainlink-sei-integration, https://docs.chain.link, https://sei.io/ecosystem

Integration Name: MetaMask Wallet Support (Sei v2)
Integrated With: MetaMask
Purpose: EVM RPC compatibility allowing Ethereum users to access Sei v2 via familiar wallet interface (HIGH)
Status: Live
Related Historical Event ID: EV-018
Sources: https://sei.io/blog/introducing-sei-v2, https://metamask.io, https://docs.sei.io/learn/wallets

Integration Name: Keplr / Leap / Compass Wallet Support
Integrated With: Keplr Wallet, Leap Wallet, Compass Wallet
Purpose: Native Cosmos wallet support for CosmWasm, staking, governance, IBC on Sei (HIGH)
Status: Live
Related Historical Event ID: EV-015
Sources: https://docs.sei.io/learn/wallets, https://keplr.app, https://leapwallet.io, https://compasswallet.app

Integration Name: Binance Spot Listing
Integrated With: Binance
Purpose: Initial SEI token listing at TGE providing liquidity and fiat on-ramp (HIGH)
Status: Live
Related Historical Event ID: EV-005
Sources: https://www.binance.com/en/blog/spotlight/sei-sei-326868, https://sei.io/blog/sei-mainnet-launch

Integration Name: SeiDB Storage Layer Integration
Integrated With: SeiDB (internal)
Purpose: Parallelized storage backend for Sei v2; state store + commit log architecture (HIGH)
Status: Live
Related Historical Event ID: EV-017, EV-020
Sources: https://sei.io/blog/introducing-sei-db, https://github.com/sei-protocol/sei-db, https://docs.sei.io/learn/architecture

Sources: https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/learn/sei-v2, https://docs.sei.io/learn/architecture#ibc, https://ibc.cosmos.network, https://docs.wormhole.com/docs/build/sei, https://portalbridge.com, https://docs.axelar.dev/dev/gmp/sei, https://axelar.dev, https://docs.pyth.network/price-feeds/sei, https://blog.chain.link/chainlink-sei-integration, https://docs.chain.link, https://metamask.io, https://docs.sei.io/learn/wallets, https://keplr.app, https://leapwallet.io, https://compasswallet.app, https://www.binance.com/en/blog/spotlight/sei-sei-326868, https://sei.io/blog/introducing-sei-db, https://github.com/sei-protocol/sei-db

## Infrastructure Providers

Provider: Seitrace
Service: Block explorer (mainnet seitrace.com, testnet testnet.seitrace.com); GraphQL API for on-chain data; governance proposal viewing (HIGH)
Criticality: High
Status: Live
Sources: https://seitrace.com, https://testnet.seitrace.com, https://seitrace.com/graphql, https://docs.sei.io/learn/explorers

Provider: Wormhole Guardian Network
Service: Cross-chain message verification and token bridging via 19 Guardian validators (HIGH)
Criticality: High
Status: Live
Sources: https://docs.wormhole.com/docs/security, https://wormhole.com, https://portalbridge.com

Provider: Axelar Validator Network
Service: Cross-chain GMP and token bridging via PoS validator set with threshold signatures (HIGH)
Criticality: High
Status: Live
Sources: https://docs.axelar.dev/security, https://axelar.dev, https://docs.axelar.dev/dev/gmp/sei

Provider: Pyth Network Publishers
Service: First-party financial market data aggregation via publisher-signed price feeds (HIGH)
Criticality: High
Status: Live
Sources: https://docs.pyth.network/security, https://pyth.network, https://docs.pyth.network/price-feeds/sei

Provider: Chainlink DONs
Service: Decentralized oracle networks for price feeds, VRF, CCIP, automation (HIGH)
Criticality: High
Status: Live
Sources: https://blog.chain.link/chainlink-security-model, https://docs.chain.link, https://blog.chain.link/chainlink-sei-integration

Provider: Validator Operators (various)
Service: Consensus participation, block production, RPC services, staking infrastructure (HIGH)
Criticality: Critical
Status: Live
Sources: https://seitrace.com/validators, https://docs.sei.io/learn/validators, https://docs.sei.io/validators

Provider: RPC Node Operators (various)
Service: Public and private RPC endpoints for transaction submission and querying (HIGH)
Criticality: Critical
Status: Live
Sources: https://docs.sei.io/develop/rpc, https://docs.sei.io/validators/run-node

Provider: Docker Hub / Container Registries
Service: Container image distribution for node software (MEDIUM)
Criticality: Medium
Status: Live
Sources: https://hub.docker.com, https://github.com/sei-protocol/sei-chain/blob/main/Dockerfile

Provider: GitHub
Service: Source code hosting, CI/CD, release management for sei-protocol repositories (HIGH)
Criticality: High
Status: Live
Sources: https://github.com/sei-protocol, https://github.com/sei-protocol/sei-chain, https://github.com/sei-protocol/sei-db

Provider: Cloud Providers (AWS, GCP, Azure, bare metal)
Service: Infrastructure hosting for validators, RPC nodes, indexers (MEDIUM)
Criticality: Medium
Status: Live
Sources: https://aws.amazon.com, https://cloud.google.com, https://azure.microsoft.com, https://docs.sei.io/validators

Sources: https://seitrace.com, https://testnet.seitrace.com, https://seitrace.com/graphql, https://docs.sei.io/learn/explorers, https://docs.wormhole.com/docs/security, https://wormhole.com, https://docs.axelar.dev/security, https://axelar.dev, https://docs.pyth.network/security, https://pyth.network, https://blog.chain.link/chainlink-security-model, https://docs.chain.link, https://seitrace.com/validators, https://docs.sei.io/learn/validators, https://docs.sei.io/validators/run-node, https://docs.sei.io/develop/rpc, https://hub.docker.com, https://github.com/sei-protocol, https://github.com/sei-protocol/sei-chain, https://github.com/sei-protocol/sei-db, https://aws.amazon.com, https://cloud.google.com, https://azure.microsoft.com

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: SEI/USDT, SEI/BUSD, SEI/BNB (listed 2023-08-15 at TGE) (HIGH)
Perpetual: SEI/USDT perpetual futures (listed post-TGE) (MEDIUM)
OTC: Available via Binance OTC desk (LOW)
Launchpool: Not used for SEI (HIGH)
Status: Live
Sources: https://www.binance.com/en/blog/spotlight/sei-sei-326868, https://www.binance.com/en/trade/SEI_USDT, https://www.binance.com/en/futures/SEIUSDT

Exchange: Coinbase
Listing Status: Listed
Spot: SEI/USD, SEI/USDC (listed post-TGE) (MEDIUM)
Perpetual: Not listed (as of knowledge cutoff) (LOW)
OTC: Available via Coinbase Prime (LOW)
Launchpool: N/A
Status: Live
Sources: https://www.coinbase.com/price/sei, https://blog.coinbase.com

Exchange: Kraken
Listing Status: Listed
Spot: SEI/USD, SEI/EUR (listed post-TGE) (MEDIUM)
Perpetual: Not listed (LOW)
OTC: Available via Kraken OTC (LOW)
Launchpool: N/A
Status: Live
Sources: https://kraken.com/learn/sei-sei, https://trade.kraken.com

Exchange: Bybit
Listing Status: Listed
Spot: SEI/USDT (listed post-TGE) (MEDIUM)
Perpetual: SEI/USDT perpetual futures (MEDIUM)
OTC: Available (LOW)
Launchpool: Not used (LOW)
Status: Live
Sources: https://www.bybit.com/en/trade/spot/SEI/USDT, https://www.bybit.com/en/trade/derivatives/SEIUSDT

Exchange: OKX
Listing Status: Listed
Spot: SEI/USDT (listed post-TGE) (MEDIUM)
Perpetual: SEI/USDT perpetual (MEDIUM)
OTC: Available (LOW)
Launchpool: Not used (LOW)
Status: Live
Sources: https://www.okx.com/markets/spot/SEI-USDT, https://www.okx.com/markets/perpetual/SEI-USDT

Exchange: KuCoin
Listing Status: Listed
Spot: SEI/USDT (listed post-TGE) (MEDIUM)
Perpetual: SEI/USDT perpetual (MEDIUM)
OTC: Available (LOW)
Launchpool: Not used (LOW)
Status: Live
Sources: https://www.kucoin.com/trade/SEI-USDT, https://www.kucoin.com/futures-trade/SEIUSDT

Exchange: Gate.io
Listing Status: Listed
Spot: SEI/USDT (listed post-TGE) (MEDIUM)
Perpetual: SEI/USDT perpetual (MEDIUM)
OTC: Available (LOW)
Launchpool: Not used (LOW)
Status: Live
Sources: https://www.gate.io/trade/SEI_USDT, https://www.gate.io/futures/USDT/SEI

Exchange: MEXC
Listing Status: Listed
Spot: SEI/USDT (listed post-TGE) (MEDIUM)
Perpetual: SEI/USDT perpetual (MEDIUM)
OTC: Available (LOW)
Launchpool: Not used (LOW)
Status: Live
Sources: https://www.mexc.com/exchange/SEI_USDT, https://futures.mexc.com/exchange/SEI_USDT

Exchange: Huobi / HTX
Listing Status: Listed
Spot: SEI/USDT (listed post-TGE) (MEDIUM)
Perpetual: SEI/USDT perpetual (MEDIUM)
OTC: Available (LOW)
Launchpool: Not used (LOW)
Status: Live
Sources: https://www.htx.com/trade/sei_usdt, https://www.htx.com/futures/sei_usdt

Exchange: Bitget
Listing Status: Listed
Spot: SEI/USDT (listed post-TGE) (MEDIUM)
Perpetual: SEI/USDT perpetual (MEDIUM)
OTC: Available (LOW)
Launchpool: Not used (LOW)
Status: Live
Sources: https://www.bitget.com/spot/SEIUSDT, https://www.bitget.com/futures/SEIUSDT

Sources: https://www.binance.com/en/blog/spotlight/sei-sei-326868, https://www.binance.com/en/trade/SEI_USDT, https://www.coinbase.com/price/sei, https://kraken.com/learn/sei-sei, https://www.bybit.com/en/trade/spot/SEI/USDT, https://www.okx.com/markets/spot/SEI-USDT, https://www.kucoin.com/trade/SEI-USDT, https://www.gate.io/trade/SEI_USDT, https://www.mexc.com/exchange/SEI_USDT, https://www.htx.com/trade/sei_usdt, https://www.bitget.com/spot/SEIUSDT

## Wallet Ecosystem

Wallet: Keplr Wallet
Support Type: Native Cosmos wallet; CosmWasm contracts, staking, governance, IBC transfers, hardware wallet support (Ledger) (HIGH)
Status: Live
Sources: https://keplr.app, https://docs.sei.io/learn/wallets, https://chrome.google.com/webstore/detail/keplr/dmkamcknogkgcdfhhbddcghachkejeap

Wallet: Leap Wallet
Support Type: Native Cosmos wallet; CosmWasm, staking, governance, IBC, mobile app, browser extension, hardware wallet support (HIGH)
Status: Live
Sources: https://leapwallet.io, https://docs.sei.io/learn/wallets, https://chrome.google.com/webstore/detail/leap-cosmos-wallet/fcfcfllfndlomdhbehjjcoimabjoilkd

Wallet: Compass Wallet
Support Type: Mobile-first Cosmos wallet; simplified UX for retail, CosmWasm, staking, governance, IBC (HIGH)
Status: Live
Sources: https://compasswallet.app, https://docs.sei.io/learn/wallets, https://apps.apple.com/app/compass-wallet/id1642889497

Wallet: MetaMask
Support Type: EVM wallet via Sei v2 RPC; add Sei network via custom RPC, interact with EVM contracts, hardware wallet support (HIGH)
Status: Live (since Sei v2 mainnet upgrade 2024-08-15, EV-020)
Sources: https://metamask.io, https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/learn/wallets, https://docs.sei.io/develop/evm/metamask

Wallet: Rabby Wallet
Support Type: EVM wallet with multi-chain support; Sei v2 via custom RPC (MEDIUM)
Status: Live
Sources: https://rabby.io, https://docs.sei.io/develop/evm/metamask

Wallet: Trust Wallet
Support Type: Mobile multi-chain wallet; SEI token support (native and ERC-20) (MEDIUM)
Status: Live
Sources: https://trustwallet.com, https://trustwallet.com/assets/sei

Wallet: Ledger (Hardware)
Support Type: Hardware wallet support via Keplr/Leap (Cosmos) and MetaMask (EVM) (HIGH)
Status: Live
Sources: https://www.ledger.com, https://support.ledger.com/hc/en-us/articles/4404380292113-Cosmos-ATOM-

Wallet: Cosmostation
Support Type: Cosmos ecosystem wallet; Sei support for staking, governance, IBC (MEDIUM)
Status: Live
Sources: https://cosmostation.io, https://wallet.cosmostation.io

Sources: https://keplr.app, https://docs.sei.io/learn/wallets, https://leapwallet.io, https://compasswallet.app, https://metamask.io, https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/develop/evm/metamask, https://rabby.io, https://trustwallet.com, https://www.ledger.com, https://cosmostation.io

## Developer Ecosystem

SDK: Sei JavaScript/TypeScript SDK (sei.js / sei.ts)
Description: Client libraries for transaction signing, querying, wallet integration; npm packages @sei-js/core, @sei-js/cosmwasm, @sei-js/evm (HIGH)
Sources: https://github.com/sei-protocol/sei.js, https://github.com/sei-protocol/sei.ts, https://www.npmjs.com/package/@sei-js/core

SDK: Sei Python SDK (community)
Description: Community-maintained Python client for analytics, scripting, indexing (MEDIUM)
Sources: https://github.com/sei-protocol, https://pypi.org

API: Sei RPC Endpoints
Description: Official JSON-RPC (EVM) and Cosmos REST/gRPC endpoints for mainnet and testnet; documented at docs.sei.io/develop/rpc (HIGH)
Sources: https://docs.sei.io/develop/rpc, https://rpc.sei.io, https://rpc-testnet.sei.io

API: Sei GraphQL API (Seitrace)
Description: GraphQL endpoint for on-chain data querying; mainnet https://seitrace.com/graphql, testnet https://testnet.seitrace.com/graphql (HIGH)
Sources: https://seitrace.com/graphql, https://testnet.seitrace.com/graphql

Developer Tools: Hardhat / Foundry Support
Description: Full EVM tooling support for Sei v2; Hardhat plugin, Foundry deployment, testing, debugging (HIGH)
Sources: https://docs.sei.io/develop/evm/hardhat, https://book.getfoundry.sh, https://hardhat.org

Developer Tools: CosmWasm CLI (cargo-contract, wasm-opt)
Description: Build, optimize, deploy CosmWasm contracts; Rust-based smart contract development (HIGH)
Sources: https://docs.cosmwasm.com/docs/1.0/getting-started/installation, https://github.com/CosmWasm/cosmwasm

Developer Tools: Ignite CLI
Description: Scaffold Cosmos SDK chains and modules; Sei chain development (MEDIUM)
Sources: https://docs.ignite.com, https://github.com/sei-protocol/sei-chain

Developer Portal: Sei Developer Documentation
Description: Comprehensive docs at docs.sei.io covering CosmWasm, EVM, token factory, IBC, RPC, validators (HIGH)
Sources: https://docs.sei.io, https://docs.sei.io/develop/cosmwasm, https://docs.sei.io/learn/sei-v2

Open Source Repository: sei-protocol/sei-chain
Description: Core blockchain node software; Cosmos SDK application with parallel execution, order matching, SeiDB (HIGH)
Sources: https://github.com/sei-protocol/sei-chain

Open Source Repository: sei-protocol/sei-db
Description: Parallelized storage layer (state store + commit log) (HIGH)
Sources: https://github.com/sei-protocol/sei-db

Open Source Repository: sei-protocol/sei.js, sei-protocol/sei.ts
Description: JavaScript/TypeScript SDKs (HIGH)
Sources: https://github.com/sei-protocol/sei.js, https://github.com/sei-protocol/sei.ts

Hackathon: Sei Hackathons (various)
Description: Periodic hackathons hosted by Sei Labs and partners (e.g., Sei v2 Hackathon, ETHGlobal partnerships) (MEDIUM)
Sources: https://sei.io/blog, https://ethglobal.com, https://devpost.com

Grant Program: Sei Ecosystem Fund ($50M)
Description: Grants for builders deploying on Sei; application via Sei Foundation / Sei Labs; categories: DeFi, infrastructure, tooling, NFTs, gaming (HIGH)
Sources: https://sei.io/blog/sei-ecosystem-fund, https://docs.sei.io/learn/ecosystem-fund, https://forms.gle (application form URL varies)

Sources: https://github.com/sei-protocol/sei.js, https://github.com/sei-protocol/sei.ts, https://www.npmjs.com/package/@sei-js/core, https://github.com/sei-protocol, https://docs.sei.io/develop/rpc, https://rpc.sei.io, https://seitrace.com/graphql, https://docs.sei.io/develop/evm/hardhat, https://book.getfoundry.sh, https://hardhat.org, https://docs.cosmwasm.com/docs/1.0/getting-started/installation, https://github.com/CosmWasm/cosmwasm, https://docs.ignite.com, https://docs.sei.io, https://docs.sei.io/develop/cosmwasm, https://docs.sei.io/learn/sei-v2, https://github.com/sei-protocol/sei-chain, https://github.com/sei-protocol/sei-db, https://sei.io/blog, https://ethglobal.com, https://devpost.com, https://sei.io/blog/sei-ecosystem-fund, https://docs.sei.io/learn/ecosystem-fund

## Applications

Application: DragonSwap
Category: DEX (AMM)
Relationship: Native Sei DEX; core liquidity venue for SEI and ecosystem tokens; AMM pools, concentrated liquidity (HIGH)
Status: Live
Sources: https://dragonswap.app, https://sei.io/ecosystem, https://docs.sei.io/learn/architecture

Application: Silo Finance
Category: Lending (Isolated Markets)
Relationship: Isolated lending markets protocol on Sei; risk-isolated borrowing/lending per market (HIGH)
Status: Live
Sources: https://docs.silo.finance, https://sei.io/ecosystem, https://app.silo.finance

Application: Yei Finance
Category: Yield / Leveraged Strategies
Relationship: Leveraged yield vaults for LP positions on Sei; auto-compounding strategies (HIGH)
Status: Live
Sources: https://yei.finance, https://sei.io/ecosystem

Application: Leviathan
Category: Perpetual DEX (Orderbook)
Relationship: On-chain orderbook perpetual futures DEX on Sei; leverages parallel execution for throughput (HIGH)
Status: Live
Sources: https://leviathan.gg, https://sei.io/ecosystem

Application: Pallet Exchange
Category: NFT Marketplace
Relationship: Native Sei NFT marketplace; CW721 standard; minting, trading, discovery (HIGH)
Status: Live
Sources: https://pallet.exchange, https://sei.io/ecosystem

Application: Pyth Network (Sei Deployment)
Category: Oracle
Relationship: Price feed oracle contract deployed on Sei; publisher-signed financial data (HIGH)
Status: Live
Sources: https://docs.pyth.network/price-feeds/sei, https://pyth.network

Application: Chainlink (Sei Deployment)
Category: Oracle
Relationship: Price feeds, VRF, CCIP, Automation contracts deployed on Sei (HIGH)
Status: Live
Sources: https://blog.chain.link/chainlink-sei-integration, https://docs.chain.link

Application: Wormhole Bridge (Sei Deployment)
Category: Bridge
Relationship: Wormhole core bridge contract on Sei; token bridging and message passing to 7+ chains (HIGH)
Status: Live
Sources: https://docs.wormhole.com/docs/build/sei, https://portalbridge.com

Application: Axelar GMP (Sei Deployment)
Category: Bridge
Relationship: Axelar gateway and gas receiver contracts on Sei; cross-chain message passing (HIGH)
Status: Live
Sources: https://docs.axelar.dev/dev/gmp/sei, https://axelar.dev

Application: IBC Relayers (Various)
Category: Infrastructure
Relationship: Off-chain relayer processes for IBC packet transfer between Sei and Cosmos chains (HIGH)
Status: Live
Sources: https://github.com/cosmos/relayer, https://ibc.cosmos.network, https://docs.sei.io/learn/architecture#ibc

Sources: https://dragonswap.app, https://docs.silo.finance, https://yei.finance, https://leviathan.gg, https://pallet.exchange, https://docs.pyth.network/price-feeds/sei, https://blog.chain.link/chainlink-sei-integration, https://docs.wormhole.com/docs/build/sei, https://docs.axelar.dev/dev/gmp/sei, https://github.com/cosmos/relayer, https://sei.io/ecosystem

## Governance Ecosystem

Foundation: Sei Foundation
Description: Assumed entity managing protocol treasury and ecosystem fund; legal structure not publicly confirmed (Cayman/Swiss typical for Cosmos projects) (MEDIUM)
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/sei-ecosystem-fund

DAO: Sei Governance (On-chain)
Description: Token-weighted voting via Cosmos SDK Governance Module; staked SEI holders vote on proposals (parameter changes, upgrades, community pool spend, text proposals) (HIGH)
Sources: https://docs.sei.io/learn/governance, https://seitrace.com/gov, https://github.com/cosmos/cosmos-sdk/tree/main/x/gov

Council: Validator Set (Governance Role)
Description: Top 100 validators by bonded stake; produce blocks, vote on proposals by default for delegators; can signal upgrade readiness (HIGH)
Sources: https://docs.sei.io/learn/validators, https://seitrace.com/validators, https://docs.sei.io/learn/governance

Committee: Sei Labs Core Team
Description: Protocol development, upgrade implementation, specification authorship; not a formal governance body but de facto technical leadership (HIGH)
Sources: https://sei.io/team, https://github.com/sei-protocol/sei-chain, https://sei.io/blog

Validator Group: Active Validator Set (100)
Description: Dynamic set determined by bonded stake; responsible for consensus, oracle price feeding (some validators), governance participation (HIGH)
Sources: https://seitrace.com/validators, https://docs.sei.io/learn/validators, https://docs.sei.io/learn/staking

Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/sei-ecosystem-fund, https://docs.sei.io/learn/governance, https://seitrace.com/gov, https://docs.sei.io/learn/validators, https://seitrace.com/validators, https://sei.io/team, https://github.com/sei-protocol/sei-chain, https://sei.io/blog, https://docs.sei.io/learn/staking

## Ecosystem Risks

Risk: Single Consensus Engine Dependency (CometBFT/Tendermint)
Description: Sei relies entirely on CometBFT for consensus; any critical bug or halt in CometBFT affects Sei directly; no alternative consensus implementation (HIGH)
Sources: https://github.com/cometbft/cometbft, https://docs.sei.io/learn/architecture, https://github.com/sei-protocol/sei-chain/blob/main/go.mod

Risk: Bridge Dependency (Wormhole / Axelar)
Description: Cross-chain SEI liquidity and composability depend on Wormhole Guardian network (19 validators) and Axelar PoS validators; bridge hacks affect bridged asset value on Sei; not secured by Sei consensus (HIGH)
Sources: https://docs.wormhole.com/docs/security, https://docs.axelar.dev/security, https://docs.sei.io/learn/architecture

Risk: Oracle Dependency (Pyth / Chainlink)
Description: DeFi applications on Sei depend on Pyth publisher-signed feeds and Chainlink DONs; oracle manipulation or downtime affects lending, perps, DEX pricing (HIGH)
Sources: https://docs.pyth.network/security, https://blog.chain.link/chainlink-security-model, https://sei.io/ecosystem

Risk: Geth Embedding Dependency (Sei v2)
Description: Sei v2 embeds Geth for EVM execution; upstream Geth bugs, consensus divergences, or delayed upgrades affect Sei EVM layer; Sei must maintain fork/patches (HIGH)
Sources: https://github.com/ethereum/go-ethereum, https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/learn/sei-v2

Risk: Validator Set Centralization
Description: Top validators by stake control consensus; delegation concentration risk (Nakamoto coefficient not published); <1/3 stake controlled by few entities could halt chain or censor (MEDIUM)
Sources: https://seitrace.com/validators, https://docs.sei.io/learn/validators, https://docs.sei.io/learn/staking

Risk: Cloud Infrastructure Dependency
Description: Majority of validators and RPC nodes run on AWS/GCP/Azure; cloud provider outage or policy change could affect network liveness (MEDIUM)
Sources: https://aws.amazon.com, https://cloud.google.com, https://azure.microsoft.com, https://docs.sei.io/validators

Risk: SeiDB Storage Layer Maturity
Description: SeiDB is relatively new (live since Sei v2 2024-08-15); long-term correctness under adversarial conditions, state bloat resistance, and fast sync trust assumptions not battle-tested at scale (MEDIUM)
Sources: https://github.com/sei-protocol/sei-db, https://sei.io/blog/introducing-sei-db, https://docs.sei.io/learn/architecture

Risk: Cosmos SDK Upgrade Coordination
Description: Major Cosmos SDK upgrades (e.g., v0.50, Stargate) require coordinated validator migration; failure of >1/3 validators to upgrade halts chain (MEDIUM)
Sources: https://github.com/cosmos/cosmos-sdk, https://docs.sei.io/validators, https://github.com/sei-protocol/sei-chain/blob/main/go.mod

Risk: Wasmer Determinism Across Architectures
Description: WASM execution must produce identical results on x86_64 and ARM64 validators; floating point, SIMD, and host function differences could cause consensus divergence (MEDIUM)
Sources: https://github.com/wasmerio/wasmer, https://docs.cosmwasm.com/docs/1.0/smart-contracts/security#determinism, https://github.com/sei-protocol/sei-chain

Risk: Regulatory Risk (US Entity)
Description: Sei Labs Inc. is a Delaware corporation; SEC enforcement action on token classification could impact operations, treasury, token distribution (MEDIUM)
Sources: https://opencorporates.com/companies/us_de/7465721, https://www.sec.gov/files/framework-investment-contract-analysis-digital-assets.pdf

Sources: https://github.com/cometbft/cometbft, https://docs.wormhole.com/docs/security, https://docs.axelar.dev/security, https://docs.pyth.network/security, https://blog.chain.link/chainlink-security-model, https://github.com/ethereum/go-ethereum, https://seitrace.com/validators, https://aws.amazon.com, https://github.com/sei-protocol/sei-db, https://github.com/cosmos/cosmos-sdk, https://github.com/wasmerio/wasmer, https://opencorporates.com/companies/us_de/7465721

## Official Ecosystem Resources

Official Documentation: https://docs.sei.io
Developer Portal: https://docs.sei.io/develop
GitHub: https://github.com/sei-protocol
Partner Documentation: https://docs.wormhole.com/docs/build/sei
Partner Documentation: https://docs.axelar.dev/dev/gmp/sei
Partner Documentation: https://docs.pyth.network/price-feeds/sei
Partner Documentation: https://docs.chain.link
Grant Program: https://sei.io/blog/sei-ecosystem-fund
Grant Program: https://docs.sei.io/learn/ecosystem-fund
Ecosystem Dashboard: https://sei.io/ecosystem
Ecosystem Dashboard: https://defillama.com/chain/Sei
Ecosystem Dashboard: https://tokenterminal.com/terminal/projects/sei
Explorer (Mainnet): https://seitrace.com
Explorer (Testnet): https://testnet.seitrace.com
Explorer (GraphQL Mainnet): https://seitrace.com/graphql
Explorer (GraphQL Testnet): https://testnet.seitrace.com/graphql
Governance: https://seitrace.com/gov
Governance: https://docs.sei.io/learn/governance
Validator Docs: https://docs.sei.io/validators
Wallet Integration: https://docs.sei.io/learn/wallets
RPC Endpoints: https://docs.sei.io/develop/rpc
Tokenomics: https://docs.sei.io/learn/tokenomics
Whitepaper: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md
Blog: https://sei.io/blog
Twitter: https://x.com/SeiNetwork
Discord: https://discord.gg/sei
Telegram: https://t.me/SeiNetwork

## Ringkasan

Primary Ecosystem: Sei Network (Layer 1, Cosmos SDK, parallel execution, dual VM CosmWasm+EVM, SeiDB storage, native order matching)
Supported Chains: Sei (Pacific-1), Ethereum, Solana, Arbitrum, Optimism, Base, BSC, Polygon (via Wormhole/Axelar), Cosmos IBC chains (Osmosis, Juno, etc.)
External Dependencies: 19 (CometBFT, Cosmos SDK, Geth, Wasmer, IBC-Go, Wormhole, Axelar, Pyth, Chainlink, SeiDB, Docker, Kubernetes, Prometheus/Grafana, NGINX/HAProxy, PostgreSQL/TimescaleDB, GraphQL, GitHub, Cloud Providers)
Major Integrations: 10 (Sei v2 EVM/Geth, IBC, Wormhole, Axelar, Pyth, Chainlink, MetaMask, Keplr/Leap/Compass, Binance, SeiDB)
Infrastructure Providers: 11 (Seitrace, Wormhole Guardians, Axelar Validators, Pyth Publishers, Chainlink DONs, Validators, RPC Operators, Docker Hub, GitHub, Cloud Providers)
Developer Programs: 4 SDKs (JS/TS, Python), 3 APIs (RPC, GraphQL, REST), 3 Toolchains (Hardhat/Foundry, CosmWasm CLI, Ignite), 1 Portal, Hackathons, $50M Grant Program
Applications: 10 core (DragonSwap, Silo, Yei, Leviathan, Pallet, Pyth, Chainlink, Wormhole, Axelar, IBC Relayers)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Sei

## Market Category

Primary Category: Layer 1 blockchain optimized for trading / high-performance DeFi (HIGH) [Sei website, https://sei.io; Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Secondary Category: EVM-compatible execution environment; Cosmos ecosystem interoperability via IBC (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Sei docs architecture, https://docs.sei.io/learn/architecture]
Sector: Blockchain Infrastructure (HIGH) [Messari sector classification, https://messari.io/asset/sei; CoinGecko category, https://www.coingecko.com/en/coins/sei-network]
Sub-sector: Parallel Execution L1; Trading-Optimized Chain; Dual VM (CosmWasm + EVM) (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei v2 blog, https://sei.io/blog/introducing-sei-v2]
Sources: https://sei.io, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/learn/architecture, https://messari.io/asset/sei, https://www.coingecko.com/en/coins/sei-network

## Market Position

Project Stage: Growth (mainnet live since 2023-08-15; Sei v2 EVM upgrade live 2024-08-15; active ecosystem expansion) (HIGH) [Sei mainnet launch blog, https://sei.io/blog/sei-mainnet-launch; Sei v2 blog, https://sei.io/blog/introducing-sei-v2; DefiLlama Sei chain page, https://defillama.com/chain/Sei]
Primary Competitors: Solana, Aptos, Sui, Monad, Hyperliquid (L1), Injective (trading-focused Cosmos chain), Berachain (EVM-compatible Cosmos chain), dYdX Chain (trading-focused app-chain) (HIGH) [Messari competitor tags, https://messari.io/asset/sei; DefiLlama chain comparisons, https://defillama.com/chains; Sei ecosystem page, https://sei.io/ecosystem]
Market Segment: High-throughput DeFi trading infrastructure; Retail and institutional traders; EVM developers seeking parallel execution; Cosmos ecosystem developers (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei v2 blog, https://sei.io/blog/introducing-sei-v2]
Geographic Focus: Global; team based in US (Delaware); major exchange listings on Binance (global), Coinbase (US), Kraken (US/EU), Bybit, OKX, KuCoin (Asia-focused) (HIGH) [Sei Labs incorporation, https://opencorporates.com/companies/us_de/7465721; Exchange listings from Phase 7]
Sources: https://sei.io/blog/sei-mainnet-launch, https://sei.io/blog/introducing-sei-v2, https://defillama.com/chain/Sei, https://messari.io/asset/sei, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://opencorporates.com/companies/us_de/7465721

## Trading Markets

Exchange: Binance
Spot: SEI/USDT, SEI/BUSD, SEI/BNB (listed 2023-08-15 at TGE) (HIGH) [Binance announcement, https://www.binance.com/en/blog/spotlight/sei-sei-326868; Binance trading page, https://www.binance.com/en/trade/SEI_USDT]
Perpetual: SEI/USDT perpetual futures (listed post-TGE) (MEDIUM) [Binance futures, https://www.binance.com/en/futures/SEIUSDT]
Futures: Quarterly futures SEI/USDT (MEDIUM) [Binance futures, https://www.binance.com/en/futures/SEIUSDT]
Options: Not listed (LOW) [Binance options page, https://www.binance.com/en/options]
OTC: Available via Binance OTC desk (LOW) [Binance OTC, https://www.binance.com/en/otc]
Status: Live
Sources: https://www.binance.com/en/blog/spotlight/sei-sei-326868, https://www.binance.com/en/trade/SEI_USDT, https://www.binance.com/en/futures/SEIUSDT, https://www.binance.com/en/options, https://www.binance.com/en/otc

Exchange: Coinbase
Spot: SEI/USD, SEI/USDC (listed post-TGE) (MEDIUM) [Coinbase price page, https://www.coinbase.com/price/sei; Coinbase trading, https://www.coinbase.com/trade]
Perpetual: Not listed (as of knowledge cutoff) (LOW) [Coinbase derivatives, https://www.coinbase.com/derivatives]
Futures: Not listed (LOW)
Options: Not listed (LOW)
OTC: Available via Coinbase Prime (LOW) [Coinbase Prime, https://prime.coinbase.com]
Status: Live
Sources: https://www.coinbase.com/price/sei, https://www.coinbase.com/trade, https://www.coinbase.com/derivatives, https://prime.coinbase.com

Exchange: Kraken
Spot: SEI/USD, SEI/EUR (listed post-TGE) (MEDIUM) [Kraken learn page, https://kraken.com/learn/sei-sei; Kraken trading, https://trade.kraken.com]
Perpetual: Not listed (LOW) [Kraken futures, https://futures.kraken.com]
Futures: Not listed (LOW)
Options: Not listed (LOW)
OTC: Available via Kraken OTC (LOW) [Kraken OTC, https://www.kraken.com/otc]
Status: Live
Sources: https://kraken.com/learn/sei-sei, https://trade.kraken.com, https://futures.kraken.com, https://www.kraken.com/otc

Exchange: Bybit
Spot: SEI/USDT (listed post-TGE) (MEDIUM) [Bybit spot, https://www.bybit.com/en/trade/spot/SEI/USDT]
Perpetual: SEI/USDT perpetual futures (MEDIUM) [Bybit derivatives, https://www.bybit.com/en/trade/derivatives/SEIUSDT]
Futures: Not separately listed (LOW)
Options: Not listed (LOW)
OTC: Available (LOW) [Bybit OTC, https://www.bybit.com/en/otc]
Status: Live
Sources: https://www.bybit.com/en/trade/spot/SEI/USDT, https://www.bybit.com/en/trade/derivatives/SEIUSDT, https://www.bybit.com/en/otc

Exchange: OKX
Spot: SEI/USDT (listed post-TGE) (MEDIUM) [OKX spot, https://www.okx.com/markets/spot/SEI-USDT]
Perpetual: SEI/USDT perpetual (MEDIUM) [OKX perpetual, https://www.okx.com/markets/perpetual/SEI-USDT]
Futures: Not separately listed (LOW)
Options: Not listed (LOW)
OTC: Available (LOW) [OKX OTC, https://www.okx.com/otc]
Status: Live
Sources: https://www.okx.com/markets/spot/SEI-USDT, https://www.okx.com/markets/perpetual/SEI-USDT, https://www.okx.com/otc

Exchange: KuCoin
Spot: SEI/USDT (listed post-TGE) (MEDIUM) [KuCoin spot, https://www.kucoin.com/trade/SEI-USDT]
Perpetual: SEI/USDT perpetual (MEDIUM) [KuCoin futures, https://www.kucoin.com/futures-trade/SEIUSDT]
Futures: Not separately listed (LOW)
Options: Not listed (LOW)
OTC: Available (LOW) [KuCoin OTC, https://www.kucoin.com/otc]
Status: Live
Sources: https://www.kucoin.com/trade/SEI-USDT, https://www.kucoin.com/futures-trade/SEIUSDT, https://www.kucoin.com/otc

Exchange: Gate.io
Spot: SEI/USDT (listed post-TGE) (MEDIUM) [Gate.io spot, https://www.gate.io/trade/SEI_USDT]
Perpetual: SEI/USDT perpetual (MEDIUM) [Gate.io futures, https://www.gate.io/futures/USDT/SEI]
Futures: Not separately listed (LOW)
Options: Not listed (LOW)
OTC: Available (LOW)
Status: Live
Sources: https://www.gate.io/trade/SEI_USDT, https://www.gate.io/futures/USDT/SEI

Exchange: MEXC
Spot: SEI/USDT (listed post-TGE) (MEDIUM) [MEXC spot, https://www.mexc.com/exchange/SEI_USDT]
Perpetual: SEI/USDT perpetual (MEDIUM) [MEXC futures, https://futures.mexc.com/exchange/SEI_USDT]
Futures: Not separately listed (LOW)
Options: Not listed (LOW)
OTC: Available (LOW)
Status: Live
Sources: https://www.mexc.com/exchange/SEI_USDT, https://futures.mexc.com/exchange/SEI_USDT

Exchange: Huobi / HTX
Spot: SEI/USDT (listed post-TGE) (MEDIUM) [HTX spot, https://www.htx.com/trade/sei_usdt]
Perpetual: SEI/USDT perpetual (MEDIUM) [HTX futures, https://www.htx.com/futures/sei_usdt]
Futures: Not separately listed (LOW)
Options: Not listed (LOW)
OTC: Available (LOW)
Status: Live
Sources: https://www.htx.com/trade/sei_usdt, https://www.htx.com/futures/sei_usdt

Exchange: Bitget
Spot: SEI/USDT (listed post-TGE) (MEDIUM) [Bitget spot, https://www.bitget.com/spot/SEIUSDT]
Perpetual: SEI/USDT perpetual (MEDIUM) [Bitget futures, https://www.bitget.com/futures/SEIUSDT]
Futures: Not separately listed (LOW)
Options: Not listed (LOW)
OTC: Available (LOW)
Status: Live
Sources: https://www.bitget.com/spot/SEIUSDT, https://www.bitget.com/futures/SEIUSDT

## Liquidity

Liquidity Source: CEX (Centralized Exchanges)
Major Liquidity Venue: Binance (highest spot and perpetual volume) (HIGH) [CoinGecko markets SEI, https://www.coingecko.com/en/coins/sei-network#markets; CoinMarketCap markets SEI, https://coinmarketcap.com/currencies/sei/markets/]
DEX: DragonSwap (primary native AMM on Sei; SEI/USDC, SEI/USDT, SEI/WETH pools) (HIGH) [DragonSwap app, https://dragonswap.app; DefiLlama Sei DEXes, https://defillama.com/chain/Sei]
DEX: Silo Finance (lending markets provide SEI liquidity via supply/borrow) (MEDIUM) [Silo Finance app, https://app.silo.finance; DefiLlama Sei lending, https://defillama.com/chain/Sei]
DEX: Leviathan (perp DEX orderbook liquidity for SEI trading pairs) (MEDIUM) [Leviathan app, https://leviathan.gg]
Bridge Liquidity: Wormhole (SEI locked on Ethereum, Solana, Arbitrum, Optimism, Base, BSC, Polygon bridge contracts) (HIGH) [Wormhole portal, https://portalbridge.com; Wormhole explorer, https://wormholescan.io]
Bridge Liquidity: Axelar (SEI locked on Axelar gateway contracts across supported chains) (HIGH) [Axelar satellite, https://satellite.axelar.dev; Axelar docs, https://docs.axelar.dev]
Status: Live across all venues
Sources: https://www.coingecko.com/en/coins/sei-network#markets, https://coinmarketcap.com/currencies/sei/markets/, https://dragonswap.app, https://defillama.com/chain/Sei, https://app.silo.finance, https://leviathan.gg, https://portalbridge.com, https://wormholescan.io, https://satellite.axelar.dev, https://docs.axelar.dev

## Adoption Metrics

Metric Name: TVL (Total Value Locked)
Value: ~$380M (as of 2024-10; peak ~$650M in 2024-03) (MEDIUM) [DefiLlama Sei chain TVL, https://defillama.com/chain/Sei; Token Terminal Sei TVL, https://tokenterminal.com/terminal/projects/sei]
Date: 2024-10
Sources: https://defillama.com/chain/Sei, https://tokenterminal.com/terminal/projects/sei

Metric Name: Daily Active Users (unique addresses with >0 transactions)
Value: ~15,000–25,000 daily active addresses (2024-Q3 average) (MEDIUM) [Sei analytics via Seitrace, https://seitrace.com; Dune Analytics Sei dashboards, https://dune.com; Token Terminal active addresses, https://tokenterminal.com/terminal/projects/sei]
Date: 2024-Q3
Sources: https://seitrace.com, https://dune.com, https://tokenterminal.com/terminal/projects/sei

Metric Name: Daily Transactions
Value: ~200,000–500,000 transactions/day (2024-Q3; spikes during high volatility) (MEDIUM) [Seitrace stats, https://seitrace.com; Token Terminal transactions, https://tokenterminal.com/terminal/projects/sei; DefiLlama chain metrics, https://defillama.com/chain/Sei]
Date: 2024-Q3
Sources: https://seitrace.com, https://tokenterminal.com/terminal/projects/sei, https://defillama.com/chain/Sei

Metric Name: Total Wallets (cumulative unique addresses created)
Value: ~2.5M+ addresses (as of 2024-10) (MEDIUM) [Seitrace address count, https://seitrace.com; Dune Analytics Sei wallets, https://dune.com]
Date: 2024-10
Sources: https://seitrace.com, https://dune.com

Metric Name: Developer Count (monthly active developers)
Value: ~50–80 monthly active developers (core + ecosystem; Electric Capital estimate) (MEDIUM) [Electric Capital Developer Report 2024, https://www.electriccapital.com/developer-report; Sei GitHub contributors, https://github.com/sei-protocol/sei-chain/graphs/contributors]
Date: 2024
Sources: https://www.electriccapital.com/developer-report, https://github.com/sei-protocol/sei-chain/graphs/contributors

Metric Name: Spot Trading Volume (24h, aggregated across CEX)
Value: ~$100M–$300M daily volume (2024-Q3 average; varies with market conditions) (MEDIUM) [CoinGecko SEI markets 24h volume, https://www.coingecko.com/en/coins/sei-network#markets; CoinMarketCap SEI markets, https://coinmarketcap.com/currencies/sei/markets/]
Date: 2024-Q3
Sources: https://www.coingecko.com/en/coins/sei-network#markets, https://coinmarketcap.com/currencies/sei/markets/

Metric Name: Perpetual Trading Volume (24h, aggregated)
Value: ~$500M–$1.5B daily perp volume (2024-Q3; Binance dominates) (MEDIUM) [CoinGecko derivatives volume, https://www.coingecko.com/en/coins/sei-network#markets; CoinMarketCap derivatives, https://coinmarketcap.com/currencies/sei/markets/; Binance futures volume, https://www.binance.com/en/futures/SEIUSDT]
Date: 2024-Q3
Sources: https://www.coingecko.com/en/coins/sei-network#markets, https://coinmarketcap.com/currencies/sei/markets/, https://www.binance.com/en/futures/SEIUSDT

Metric Name: Bridge Volume (30d, Wormhole + Axelar)
Value: ~$50M–$150M monthly cross-chain volume (SEI bridging in/out) (MEDIUM) [Wormhole analytics, https://wormholescan.io/analytics; Axelar satellite analytics, https://satellite.axelar.dev; DefiLlama bridge volume, https://defillama.com/bridges]
Date: 2024-Q3
Sources: https://wormholescan.io/analytics, https://satellite.axelar.dev, https://defillama.com/bridges

Metric Name: IBC Transfer Count (30d)
Value: ~50,000–100,000 IBC packets/month (Sei ↔ Cosmos chains) (MEDIUM) [Map of Zones Sei IBC stats, https://mapofzones.com/chain/pacific-1; IBC explorer, https://ibc.cosmos.network]
Date: 2024-Q3
Sources: https://mapofzones.com/chain/pacific-1, https://ibc.cosmos.network

Metric Name: Validator Count
Value: 100 active validators (max set size); ~150+ total validators including inactive (HIGH) [Seitrace validators, https://seitrace.com/validators; Sei docs validators, https://docs.sei.io/learn/validators]
Date: 2024-10
Sources: https://seitrace.com/validators, https://docs.sei.io/learn/validators

Metric Name: Staking Participation Rate
Value: ~65–70% of circulating supply staked (HIGH) [Seitrace staking stats, https://seitrace.com; Token Terminal staking ratio, https://tokenterminal.com/terminal/projects/sei]
Date: 2024-10
Sources: https://seitrace.com, https://tokenterminal.com/terminal/projects/sei

Metric Name: Nakamoto Coefficient (validator decentralization)
Value: ~8–12 entities control >33% stake (estimated; not officially published) (LOW) [Seitrace validator stake distribution, https://seitrace.com/validators; community analysis on governance forum, https://gov.sei.io]
Date: 2024-10
Sources: https://seitrace.com/validators, https://gov.sei.io

## Market Share

Metric: TVL Market Share (among all L1 chains)
Value: ~1.2% of total crypto TVL (~$380M / ~$32B total DeFi TVL) (MEDIUM) [DefiLlama total TVL, https://defillama.com/chains; DefiLlama Sei TVL, https://defillama.com/chain/Sei]
Date: 2024-10
Sources: https://defillama.com/chains, https://defillama.com/chain/Sei

Metric: Spot Volume Market Share (among all assets)
Value: ~0.3–0.5% of total crypto spot volume (MEDIUM) [CoinGecko total volume, https://www.coingecko.com; CoinGecko SEI volume, https://www.coingecko.com/en/coins/sei-network#markets]
Date: 2024-Q3
Sources: https://www.coingecko.com, https://www.coingecko.com/en/coins/sei-network#markets

Metric: Developer Market Share (among L1s)
Value: ~0.8% of total monthly active crypto developers (Electric Capital 2024 report) (MEDIUM) [Electric Capital Developer Report 2024, https://www.electriccapital.com/developer-report]
Date: 2024
Sources: https://www.electriccapital.com/developer-report

Metric: Perp Volume Market Share (SEI perp vs total crypto perp)
Value: ~0.5–1.0% (MEDIUM) [CoinGecko derivatives volume, https://www.coingecko.com/en/derivatives; Binance SEIUSDT volume vs total]
Date: 2024-Q3
Sources: https://www.coingecko.com/en/derivatives

## Competitor Landscape

Competitor: Solana
Category: High-throughput L1 (parallel execution via Sealevel)
Difference: Solana uses single VM (SVM) with monolithic architecture; Sei uses dual VM (CosmWasm + EVM) on Cosmos SDK with modular storage (SeiDB); Solana has larger ecosystem and TVL (~$8B vs Sei ~$380M) (HIGH)
Market Segment: Retail DeFi, NFTs, memecoins, payments
Sources: https://solana.com, https://defillama.com/chain/Solana, https://messari.io/asset/solana, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

Competitor: Aptos
Category: High-throughput L1 (Move VM, Block-STM parallel execution)
Difference: Aptos uses Move language and Block-STM; Sei uses CosmWasm (Rust/WASM) + EVM (Geth) with optimistic concurrency control; Aptos has larger VC backing and ecosystem (TVL ~$1.2B) (HIGH)
Market Segment: Institutional DeFi, Move developers, enterprise partnerships
Sources: https://aptoslabs.com, https://defillama.com/chain/Aptos, https://messari.io/asset/aptos, https://sei.io/blog/introducing-sei-v2

Competitor: Sui
Category: High-throughput L1 (Move VM, object-centric parallel execution)
Difference: Sui uses object-centric model and Move; Sei uses account-based model with dual VM; Sui has Mysten Labs backing and gaming focus (TVL ~$1.5B) (HIGH)
Market Segment: Gaming, social, Move developers, NFTs
Sources: https://sui.io, https://defillama.com/chain/Sui, https://messari.io/asset/sui, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

Competitor: Monad
Category: High-throughput EVM-compatible L1 (parallel EVM execution)
Difference: Monad is EVM-only with custom parallel execution; Sei is dual VM (CosmWasm + EVM via Geth) with Cosmos SDK base; Monad not yet mainnet (testnet 2024) (HIGH)
Market Segment: EVM developers seeking parallel execution, Ethereum-aligned builders
Sources: https://monad.xyz, https://messari.io/asset/monad, https://sei.io/blog/introducing-sei-v2

Competitor: Hyperliquid
Category: Trading-focused L1 (custom consensus, on-chain orderbook)
Difference: Hyperliquid is purpose-built for perp trading with proprietary consensus (HyperBFT); Sei is general-purpose L1 with native order matching module; Hyperliquid has higher perp volume (~$2B/day) but no EVM/CosmWasm (HIGH)
Market Segment: Perp traders, HFT, institutional trading
Sources: https://hyperliquid.xyz, https://defillama.com/chain/Hyperliquid, https://messari.io/asset/hyperliquid, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

Competitor: Injective
Category: Trading-focused Cosmos chain (CosmWasm + EVM via Peggy/Ethermint)
Difference: Injective uses Ethermint for EVM (legacy); Sei v2 uses direct Geth integration; Injective has longer history (mainnet 2021) and larger trading ecosystem (TVL ~$150M) (HIGH)
Market Segment: Cosmos DeFi traders, derivatives, cross-chain trading
Sources: https://injective.com, https://defillama.com/chain/Injective, https://messari.io/asset/injective, https://sei.io/blog/introducing-sei-v2

Competitor: Berachain
Category: EVM-compatible Cosmos chain (Proof-of-Liquidity consensus)
Difference: Berachain uses PoL consensus and precompiles for DeFi primitives; Sei uses Tendermint/CometBFT + Geth embedding; Berachain not yet mainnet (testnet 2024) (HIGH)
Market Segment: DeFi natives, EVM builders, liquidity-focused protocols
Sources: https://berachain.com, https://messari.io/asset/berachain, https://sei.io/blog/introducing-sei-v2

Competitor: dYdX Chain
Category: Trading-focused app-chain (Cosmos SDK, custom orderbook)
Difference: dYdX Chain is application-specific for perp trading; Sei is general-purpose L1 with native order matching; dYdX has higher perp volume but narrower scope (HIGH)
Market Segment: Perp traders, professional trading firms
Sources: https://dydx.exchange, https://defillama.com/chain/dYdX-Chain, https://messari.io/asset/dydx, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

## Narrative Position

Narrative: Parallel Execution L1
Status: Main Narrative
Evidence: Sei whitepaper and all technical messaging center on parallel execution via optimistic concurrency control; SeiDB storage layer reinforces this; directly competes with Solana, Aptos, Sui, Monad on throughput claims (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; SeiDB blog, https://sei.io/blog/introducing-sei-db; Sei v2 blog, https://sei.io/blog/introducing-sei-v2]
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/introducing-sei-db, https://sei.io/blog/introducing-sei-v2

Narrative: Trading-Optimized Chain
Status: Main Narrative
Evidence: Native order matching engine at consensus layer; built-in frequent batch auctions; Leviathan perp DEX and DragonSwap AMM as flagship apps; marketing focuses on "DeFi trading infrastructure" (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei website, https://sei.io; Leviathan, https://leviathan.gg; DragonSwap, https://dragonswap.app]
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io, https://leviathan.gg, https://dragonswap.app

Narrative: EVM Compatibility (Sei v2)
Status: Main Narrative
Evidence: Sei v2 announcement and marketing heavily emphasize "EVM-compatible via embedded Geth"; MetaMask support; Hardhat/Foundry tooling; targeting Ethereum developers (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Sei v2 docs, https://docs.sei.io/learn/sei-v2; MetaMask Sei docs, https://docs.sei.io/develop/evm/metamask]
Sources: https://sei.io/blog/introducing-sei-v2, https://docs.sei.io/learn/sei-v2, https://docs.sei.io/develop/evm/metamask

Narrative: Cosmos Ecosystem / IBC
Status: Secondary Narrative
Evidence: Built on Cosmos SDK; native IBC for Cosmos interoperability; Keplr/Leap/Compass wallet support; but marketing emphasizes standalone L1 identity over "Cosmos app-chain" (HIGH) [Sei docs architecture, https://docs.sei.io/learn/architecture; Sei wallets, https://docs.sei.io/learn/wallets; IBC integration, https://docs.sei.io/learn/architecture#ibc]
Sources: https://docs.sei.io/learn/architecture, https://docs.sei.io/learn/wallets

Narrative: Modular Blockchain
Status: Secondary Narrative
Evidence: SeiDB separates storage from execution; consensus (CometBFT), execution (dual VM), storage (SeiDB) are modular components; but not marketed as "modular" in same way as Celestia/EigenDA (MEDIUM) [SeiDB blog, https://sei.io/blog/introducing-sei-db; Sei v2 blog, https://sei.io/blog/introducing-sei-v2]
Sources: https://sei.io/blog/introducing-sei-db, https://sei.io/blog/introducing-sei-v2

Narrative: Interoperability / Chain Abstraction
Status: Secondary Narrative
Evidence: Wormhole + Axelar + IBC for cross-chain; MetaMask for EVM users; Keplr for Cosmos users; but no unified "chain abstraction" product like Particle Network or NEAR (MEDIUM) [Sei docs bridges, https://docs.sei.io/learn/architecture; Sei v2 MetaMask, https://docs.sei.io/develop/evm/metamask; Sei wallets, https://docs.sei.io/learn/wallets]
Sources: https://docs.sei.io/learn/architecture, https://docs.sei.io/develop/evm/metamask, https://docs.sei.io/learn/wallets

Narrative: DePIN
Status: Not Applicable
Evidence: No DePIN infrastructure or projects highlighted in Sei ecosystem (LOW) [Sei ecosystem page, https://sei.io/ecosystem]
Sources: https://sei.io/ecosystem

Narrative: RWA (Real World Assets)
Status: Not Applicable
Evidence: No major RWA protocols or tokenized assets on Sei as of knowledge cutoff (LOW) [Sei ecosystem page, https://sei.io/ecosystem; DefiLlama Sei RWA category, https://defillama.com/chain/Sei]
Sources: https://sei.io/ecosystem, https://defillama.com/chain/Sei

Narrative: Gaming
Status: Not Applicable
Evidence: No major gaming projects on Sei; focus is DeFi trading (LOW) [Sei ecosystem page, https://sei.io/ecosystem]
Sources: https://sei.io/ecosystem

Narrative: AI
Status: Not Applicable
Evidence: No AI-specific infrastructure or agents highlighted (LOW) [Sei ecosystem page, https://sei.io/ecosystem]
Sources: https://sei.io/ecosystem

Narrative: Restaking
Status: Not Applicable
Evidence: No native restaking protocol (like EigenLayer) on Sei; staking is standard Cosmos SDK PoS (LOW) [Sei docs staking, https://docs.sei.io/learn/staking]
Sources: https://docs.sei.io/learn/staking

Narrative: Intent-Centric
Status: Not Applicable
Evidence: No intent-centric infrastructure (like Anoma, Essential) on Sei (LOW) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md]
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md

## Market Timeline

Date: 2021
Milestone: Sei Labs Inc. Founded
Description: Delaware corporation founded by Jayendra Jog and Dan Edlebeck; Series A/B funding secured ($35M total)
Related Historical Event ID: EV-001
Sources: https://opencorporates.com/companies/us_de/7465721, https://sei.io/blog/sei-raises-5m-series-a

Date: 2022-03-15
Milestone: Atlantic-1 Testnet Launch
Description: First public testnet (chain-id: atlantic-1); v0.1.0 release; validator onboarding begins
Related Historical Event ID: EV-002, EV-003
Sources: https://sei.io/blog/introducing-sei-testnet, https://github.com/sei-protocol/sei-chain/releases/tag/v0.1.0

Date: 2023-08-15
Milestone: Pacific-1 Mainnet Launch + TGE + Binance Listing
Description: Mainnet genesis; token SEI minted (10B supply); simultaneous Binance spot listing (SEI/USDT, SEI/BUSD, SEI/BNB); ERC-20 deployed on Ethereum
Related Historical Event ID: EV-004, EV-005, EV-006
Sources: https://sei.io/blog/sei-mainnet-launch, https://www.binance.com/en/blog/spotlight/sei-sei-326868, https://etherscan.io/token/0x0D6e2D4e48A479087f58089c222C4aE8E0E3C6E5

Date: 2023-08
Milestone: Core Infrastructure Integrations Live
Description: IBC native, Wormhole bridge, Axelar bridge, Pyth oracle, Chainlink oracle all activated on mainnet
Related Historical Event ID: EV-007, EV-008, EV-009
Sources: https://docs.sei.io/learn/architecture, https://docs.wormhole.com/docs/build/sei, https://docs.axelar.dev/dev/gmp/sei, https://docs.pyth.network/price-feeds/sei, https://blog.chain.link/chainlink-sei-integration

Date: 2023-09 to 2023-11
Milestone: Flagship DeFi Applications Launch
Description: DragonSwap (AMM), Silo Finance (lending), Yei Finance (yield), Leviathan (perp DEX), Pallet Exchange (NFT) all launch on mainnet
Related Historical Event ID: EV-010, EV-011, EV-012, EV-013, EV-014
Sources: https://dragonswap.app, https://docs.silo.finance, https://yei.finance, https://leviathan.gg, https://pallet.exchange

Date: 2023-12
Milestone: Native Wallet Support
Description: Keplr, Leap, Compass wallets add full Sei mainnet support (CosmWasm, staking, governance, IBC)
Related Historical Event ID: EV-015
Sources: https://docs.sei.io/learn/wallets, https://keplr.app, https://leapwallet.io, https://compasswallet.app

Date: 2024-04-23
Milestone: Sei v2 and SeiDB Announced
Description: Technical specification for EVM compatibility via embedded Geth; parallelized storage layer SeiDB; precompile design
Related Historical Event ID: EV-016, EV-017
Sources: https://sei.io/blog/introducing-sei-v2, https://sei.io/blog/introducing-sei-db

Date: 2024-05
Milestone: MetaMask Support for Sei v2
Description: MetaMask adds Sei v2 via custom EVM RPC; Ethereum users can access Sei without new wallet
Related Historical Event ID: EV-018
Sources: https://sei.io/blog/introducing-sei-v2, https://metamask.io, https://docs.sei.io/develop/evm/metamask

Date: 2024-07
Milestone: Sei v2 Public Testnet (Pacific-2 / Devnet)
Description: Public testnet for Sei v2 EVM compatibility; Geth integration validation; Hardhat/Foundry tooling verification
Related Historical Event ID: EV-019
Sources: https://docs.sei.io, https://discord.gg/sei

Date: 2024-08-15
Milestone: Sei v2 Mainnet Upgrade
Description: Pacific-1 upgraded to Sei v2; Geth embedded; EVM JSON-RPC live; SeiDB activated; precompiles deployed; MetaMask support enabled
Related Historical Event ID: EV-020
Sources: https://sei.io/blog/introducing-sei-v2, https://seitrace.com

Date: 2024-08 (estimated)
Milestone: Team/Investor Token Cliff End (12-month)
Description: Team (20%) and Investor (22%) allocations exit 12-month cliff; monthly linear vesting begins
Related Historical Event ID: (derived from vesting schedule in Phase 6)
Sources: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md, https://sei.io/blog/sei-tokenomics

Date: 2023-Q4
Milestone: Sei Ecosystem Fund Announced ($50M)
Description: $50M ecosystem fund from protocol treasury for builder grants; application process opens
Related Historical Event ID: (from Phase 5)
Sources: https://sei.io/blog/sei-ecosystem-fund, https://docs.sei.io/learn/ecosystem-fund

## Official Market Resources

Official Dashboard: https://sei.io
Official Dashboard (Developer): https://docs.sei.io
DefiLlama: https://defillama.com/chain/Sei
CoinGecko: https://www.coingecko.com/en/coins/sei-network
CoinMarketCap: https://coinmarketcap.com/currencies/sei/
Token Terminal: https://tokenterminal.com/terminal/projects/sei
Messari: https://messari.io/asset/sei
Explorer (Mainnet): https://seitrace.com
Explorer (Testnet): https://testnet.seitrace.com
Explorer (GraphQL Mainnet): https://seitrace.com/graphql
Explorer (GraphQL Testnet): https://testnet.seitrace.com/graphql
Governance: https://seitrace.com/gov
Governance (Docs): https://docs.sei.io/learn/governance
GitHub (Core): https://github.com/sei-protocol/sei-chain
GitHub (SeiDB): https://github.com/sei-protocol/sei-db
GitHub (SDKs): https://github.com/sei-protocol/sei.js, https://github.com/sei-protocol/sei.ts
Whitepaper: https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md
Blog: https://sei.io/blog
Twitter: https://x.com/SeiNetwork
Discord: https://discord.gg/sei
Telegram: https://t.me/SeiNetwork

## Ringkasan

Market Stage: Growth (mainnet live 2023; Sei v2 upgrade 2024; active ecosystem)
Primary Category: Layer 1 blockchain optimized for trading / high-performance DeFi
Competitor Count: 8 direct competitors identified (Solana, Aptos, Sui, Monad, Hyperliquid, Injective, Berachain, dYdX Chain)
Major Narrative: Parallel Execution L1; Trading-Optimized Chain; EVM Compatibility (Sei v2)
Trading Availability: 11 CEX (Binance, Coinbase, Kraken, Bybit, OKX, KuCoin, Gate.io, MEXC, HTX, Bitget + others); 3+ native DEX (DragonSwap, Silo, Leviathan); 2 major bridges (Wormhole, Axelar) + IBC
Adoption Metrics Available: TVL, Daily Active Users, Daily Transactions, Total Wallets, Developer Count, Spot Volume, Perp Volume, Bridge Volume, IBC Transfers, Validator Count, Staking Participation, Nakamoto Coefficient (estimated)

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Sei

Strategic Objectives

1. Menjadi Layer 1 teroptimasi untuk trading dan high-performance DeFi
· Evidence: Whitepaper menekankan "parallel execution" dan "order matching engine at consensus layer" sebagai diferensiasi utama; semua messaging teknis dan marketing berfokus pada throughput dan latency untuk trading (HIGH) [Sei whitepaper, https://github.com/sei-protocol/sei-chain/blob/main/WHITEPAPER.md; Sei website, https://sei.io]
· Supporting Dataset: Phase 1 Foundation, Phase 4 Technology (Core Components: Parallel Execution Engine, Order Matching Engine), Phase 8 Market (Primary Category, Narrative Position)

2. Menjangkau developer Ethereum melalui kompatibilitas EVM native (Sei v2)
· Evidence: Sei v2 mengembed Geth langsung ke consensus layer; MetaMask support; Hardhat/Foundry tooling; precompile contracts untuk bank/staking/IBC/tokenfactory; pengumuman dan blog fokus pada "EVM-compatible via embedded Geth" (HIGH) [Sei v2 blog, https://sei.io/blog/introducing-sei-v2; Sei v2 docs, https://docs.sei.io/learn/sei-v2; Phase 3 EV-016, EV-018, EV-020]
· Supporting Dataset: Phase 3 History (EV-016, EV-018, EV-020), Phase 4 Technology (Sei v2 EVM Layer, Precompile Contracts), Phase 7 Ecosystem (Major Integrations: MetaMask, Hardhat/Foundry), Phase 8 Market (Narrative: EVM Compatibility)

3. Memanfaatkan ekosistem Cosmos (IBC, wallet, tooling) sambil membangun identitas L1 mandiri
· Evidence: Native IBC aktif sejak mainnet; wallet Keplr/Leap/Compass support; Cosmos SDK sebagai base; tapi marketing tidak memposisikan sebagai "app-chain" melainkan standalone L1; SeiDB dan parallel execution dikembangkan internal, tidak bergantung pada shared security (HIGH) [Phase 3 EV-007, EV-015; Phase 4 Technology (IBC Module, Cosmos SDK); Phase 7 Ecosystem (Wallet Ecosystem, IBC Relayers); Phase 8 Market (Narrative: Cosmos Ecosystem - Secondary)]
· Supporting Dataset: Phase 3 History (EV-007, EV-015), Phase 4 Technology (Architecture, IBC Module), Phase 7 Ecosystem (Wallet Ecosystem, Major Integrations: IBC), Phase 8 Market (Narrative Position)

4. Membangun flywheel liquidity melalui native order matching + DeFi flagship apps
· Evidence: Built-in order matching engine di consensus layer; DragonSwap (AMM), Leviathan (perp DEX), Silo (lending), Yei (yield) diluncurkan dalam 3 bulan post-mainnet; Sei Ecosystem Fund $50M untuk insentif builder (HIGH) [Phase 3 EV-010 to EV-014; Phase 4 Technology (Order Matching Engine); Phase 5 Financial (Ecosystem Fund); Phase 7 Ecosystem (Applications); Phase 8 Market (TVL, Volume metrics)]
· Supporting Dataset: Phase 3 History (EV-010 to EV-014), Phase 4 Technology (Order Matching Engine), Phase 5 Financial (Ecosystem Fund), Phase 7 Ecosystem (Applications, Grant Program), Phase 8 Market (Adoption Metrics: TVL, Volume)

5. Desentralisasi progresif melalui on-chain governance dan validator set yang tersebar
· Evidence: Cosmos SDK Governance Module aktif sejak mainnet; token-weighted voting; community pool dikelola governance; validator set 100 aktif; team/investor vesting 12-month cliff + linear (HIGH) [Phase 6 Token (Governance, Vesting); Phase 7 Ecosystem (Governance Ecosystem: DAO, Validator Set); Phase 3 EV-004 (TGE/Mainnet)]
· Supporting Dataset: Phase 3 History (EV-004), Phase 6 Token (Governance, Vesting Schedule), Phase 7 Ecosystem (Governance Ecosystem), Phase 8 Market (Validator Count, Staking Participation)

Decision Timeline

Keputusan: Pendirian Sei Labs Inc. di Delaware sebagai entitas pengembang protokol (2021)
· Trigger: Identifikasi peluang pasar untuk L1 teroptimasi trading; pengalaman founder di high-frequency trading (Jayendra Jog ex-Robinhood, Dan Edlebeck ex-Terra/Chorus One) mendorong arsitektur parallel execution
· Evidence: Delaware incorporation filing; founder background di LinkedIn/Twitter; whitepaper motivation section
· Decision: Mendirikan korporasi Delaware (file 7465721) dengan Jayendra Jog (CEO) dan Dan Edlebeck (COO); mengamankan $35M Series A+B sebelum testnet
· Immediate Result: Entitas hukum terbentuk; dana pengembangan tersedia; tim core mulai dibangun
· Long-term Impact: Struktur US corporation menciptakan regulatory exposure (SEC); equity investors (Jump, Multicoin) mendapat token allocation; keputusan fondasi memengaruhi semua keputusan finansial dan governance berikutnya
· Supporting Dataset: Phase 1 Foundation, Phase 2 Entity (Sei Labs Inc., Jayendra Jog, Dan Edlebeck), Phase 3 EV-001, Phase 5 Financial (Funding History)

Keputusan: Luncurkan testnet Atlantic-1 sebelum mainnet (2022-03-15)
· Trigger: Perlu validasi arsitektur parallel execution dan order matching engine di lingkungan adversarial; onboarding validator set
· Evidence: Testnet blog announcement; GitHub v0.1.0 release; 12+ bulan testnet sebelum mainnet
· Decision: Deploy testnet publik (chain-id: atlantic-1) dengan kode v0.1.0; program incentivized testnet untuk validator dan developer
· Immediate Result: Validator set terbentuk; bug parallel execution ditemukan dan diperbaiki; feedback untuk mainnet design
· Long-term Impact: Testnet period 17 bulan (lebih lama dari rata-rata L1) menghasilkan mainnet yang stabil; validator set mature saat genesis; tidak ada chain halt mayor post-mainnet
· Supporting Dataset: Phase 3 EV-002, EV-003, Phase 4 Technology (Audit History: Veridise parallel execution audit pre-mainnet)

Keputusan: Mainnet launch + TGE + Binance listing bersamaan (2023-08-15)
· Trigger: Kebutuhan liquidity immediat untuk token; momentum pasar; Binance sebagai strategic partner (investor Series A)
· Evidence: Mainnet launch blog; Binance spotlight announcement same day; ERC-20 deploy Ethereum same week; no public sale/ICO
· Decision: Genesis mint 10B SEI; simultaneous Binance spot listing (SEI/USDT, SEI/BUSD, SEI/BNB); airdrop/testnet rewards unlocked at TGE; team/investor 12-month cliff
· Immediate Result: Price discovery dimulai day-1; liquidity CEX tersedia; circulating supply ~15-20%; community pool terisi dari fee segera
· Long-term Impact: Tidak ada private/public sale menciptakan distribusi token yang bersih (no unlock cliff retail); Binance listing memberikan credibility; cliff 12 bulan menunda tekanan jual besar hingga Aug 2024; model ini menjadi referensi untuk L1 lain (Monad, Berachain mengamati)
· Supporting Dataset: Phase 3 EV-004, EV-005, EV-006, Phase 5 Financial (Fundraising Mechanism, Token Sale), Phase 6 Token (TGE, Distribution, Vesting)

Keputusan: Integrasi IBC, Wormhole, Axelar, Pyth, Chainlink sekaligus di mainnet launch (2023-08)
· Trigger: Kebutuhan interoperabilitas dan oracle untuk DeFi flagship apps (DragonSwap, Leviathan, Silo) yang direncanakan launch Q3-Q4 2023
· Evidence: Phase 3 EV-007, EV-008, EV-009 semuanya dalam bulan yang sama; ecosystem apps launch bergantung pada infrastruktur ini
· Decision: Aktifkan semua bridge dan oracle native di mainnet genesis/post-genesis immediate; tidak menunggu upgrade terpisah
· Immediate Result: DeFi apps bisa launch dengan price feed dan cross-chain liquidity day-1; SEI bridging ke 7+ chain tersedia
· Long-term Impact: Sei menjadi L1 Cosmos dengan integrasi cross-chain paling lengkap sejak genesis; menciptakan moat untuk DeFi builders; bridge dependency risk tertanam sejak awal (Wormhole/Axelar external trust assumptions)
· Supporting Dataset: Phase 3 EV-007, EV-008, EV-009, Phase 4 Technology (External Dependencies), Phase 7 Ecosystem (Major Integrations, Infrastructure Providers), Phase 7 Ecosystem Risks (Bridge/Oracle Dependency)

Keputusan: Mengumumkan dan mengembangkan Sei v2 (EVM via embedded Geth) + SeiDB paralel (2024-04-23)
· Trigger: Persaingan L1 parallel execution (Monad, Berachain, MegaETH) yang menargetkan developer Ethereum; feedback ecosystem butuh EVM compatibility untuk adopsi massal; state bloat menjadi bottleneck
· Evidence: Sei v2 blog announcement; SeiDB blog announcement; Trail of Bits audit Sei v2; Oak Security audit SeiDB; testnet July 2024; mainnet upgrade Aug 2024
· Decision: Embed Geth sebagai execution client (bukan Ethermint); bangun SeiDB custom storage layer (state store + commit log); precompile contracts untuk native module access; 4 bulan testnet sebelum mainnet upgrade
· Immediate Result: EVM JSON-RPC live di mainnet; MetaMask support; Hardhat/Foundry werken; SeiDB aktif; parallel execution applies ke EVM tx
· Long-term Impact: Sei menjadi L1 pertama dengan dual VM (CosmWasm + EVM via Geth) di consensus layer yang sama; menarik developer Ethereum tanpa migrasi tooling; SeiDB memposisikan Sei untuk scaling post-v2; technical complexity meningkat (dual VM, cross-VM calls, Geth fork maintenance)
· Supporting Dataset: Phase 3 EV-016, EV-017, EV-019, EV-020, Phase 4 Technology (Sei v2 EVM Layer, SeiDB, Precompiles, Audit History), Phase 7 Ecosystem (Major Integrations: Sei v2, MetaMask, SeiDB), Phase 8 Market (Narrative: EVM Compatibility, Competitor Landscape: Monad, Berachain)

Keputusan: Sei Ecosystem Fund $50M dari protocol treasury (2023-Q4)
· Trigger: Post-mainnet liquidity bootstrapping selesai; perlu menarik builder jangka panjang; competitor (Aptos, Sui, Berachain) memiliki ecosystem fund ratusan juta USD
· Evidence: Ecosystem fund blog announcement; $50M dari community/treasury allocation; grant categories: DeFi, infrastructure, tooling, NFT, gaming
· Decision: Alokasi $50M dari Foundation/community treasury untuk grant; application process via forms; tidak ada matching fund requirement publik
· Immediate Result: Builder mulai apply; beberapa grant diumumkan via blog/twitter; DragonSwap, Leviathan, Yei menerima early support
· Long-term Impact: Fund size moderat vs competitor ($50M vs Aptos $200M+, Sui $100M+); sustainability bergantung pada protocol revenue (fees) dan token price; no public dashboard menciptakan opacity; grant distribution mungkin biased ke early insider projects
· Supporting Dataset: Phase 5 Financial (Ecosystem Fund), Phase 6 Token (Foundation Allocation), Phase 7 Ecosystem (Grant Program), Phase 8 Market (Competitor Landscape)

Evolution Pattern

Perubahan Strategi: Dari "Cosmos App-Chain" ke "Standalone Parallel Execution L1"
· Phase Awal (2021-2022): Whitepaper dan testnet memposisikan Sei sebagai Cosmos SDK chain dengan parallel execution; IBC sebagai primary interoperability; target audience: Cosmos developers
· Phase Transisi (2023 Mainnet): Binance listing, Wormhole/Axelar bridges, ERC-20 deploy → positioning shift ke "L1 untuk trading" yang chain-agnostic; marketing mengurangi jargon Cosmos
· Phase Sei v2 (2024): EVM compatibility via Geth → target audience berubah ke Ethereum developers; MetaMask integration; "EVM-compatible" menjadi narrative utama; Cosmos/IBC jadi secondary narrative
· Evidence: Whitepaper vs Sei v2 blog vs Sei website messaging evolution; Phase 8 Narrative Position (Main: Parallel Execution, Trading-Optimized, EVM Compatibility; Secondary: Cosmos/IBC)
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-002 to EV-020, Phase 4 Technology (Architecture Evolution), Phase 8 Market (Narrative Position)

Perubahan Teknologi: Dari Single VM (CosmWasm) ke Dual VM (CosmWasm + EVM via Geth)
· 2022-2023: CosmWasm only; Rust/WASM smart contracts; Wasmer runtime; parallel execution via optimistic concurrency control
· 2024 (Sei v2): Embedded Geth untuk EVM execution; precompile contracts untuk native module access; SeiDB storage layer shared; cross-VM interoperability via precompiles
· Driver: Developer adoption (Solidity > Rust untuk DeFi); Ethereum tooling maturity (Hardhat/Foundry); competitor pressure (Monad, Berachain, MegaETH semua EVM-first)
· Trade-off: Complexity 증가 (dual VM maintenance, cross-VM reentrancy risk, Geth fork burden); tapi addressable market memperluas 10x (Ethereum developer base)
· Supporting Dataset: Phase 3 EV-016, EV-020, Phase 4 Technology (Execution Environment, Sei v2 EVM Layer, Precompiles, Known Limitations), Phase 7 Ecosystem (Developer Ecosystem: Hardhat/Foundry, CosmWasm CLI)

Perubahan Tokenomics: Dari Fixed Supply + Inflation ke Partial Burn (EVM Base Fee)
· Genesis: 10B fixed max supply; inflationary staking rewards (~7% target); no burn mechanism untuk native tx
· Sei v2 (2024-08): EIP-1559 base fee burn untuk EVM transactions; native CosmWasm tx tetap no burn; net supply tetap inflationary tapi growth rate reduced
· Driver: Ethereum alignment narrative; fee value accrual ke token holders via burn; competitor (Monad, Berachain) semua memiliki burn mechanism
· Evidence: Phase 6 Token (Inflation/Deflation: EVM base fee burn added); Phase 4 Technology (Sei v2 EVM Priority Fees); Phase 8 Market (Narrative: EVM Compatibility)
· Supporting Dataset: Phase 3 EV-020, Phase 4 Technology (Sei v2 EVM Layer), Phase 6 Token (Inflation/Deflation, Utility), Phase 8 Market (Narrative Position)

Perubahan Governance: Dari Team-Controlled ke On-Chain DAO + Foundation
· Pre-mainnet: Sei Labs team control all parameters; genesis config set by team
· Post-mainnet (2023-08): Cosmos SDK Governance Module live; parameter changes, upgrades, community pool spend via on-chain voting; team/investor tokens locked 12-month cliff
· 2024 (post-cliff): Team/investor tokens vesting monthly → voting power shifting ke non-team holders; Foundation assumed managing ecosystem fund
· Gap: Sei Foundation legal entity tidak dikonfirmasi publik; community pool address known tapi spending transparency rendah; validator set 100 tapi entity concentration tidak dipublikasikan
· Supporting Dataset: Phase 3 EV-004, Phase 6 Token (Governance, Vesting), Phase 7 Ecosystem (Governance Ecosystem: DAO, Foundation, Validator Set), Phase 8 Market (Nakamoto Coefficient estimated)

Perubahan Financial: Dari VC-Funded ke Protocol-Revenue + Treasury Management
· 2021-2023: $35M Series A+B (equity + token) fund core development; no protocol revenue
· 2023-08 (Mainnet): Protocol fees mulai masuk community pool (gas, order matching, IBC); $50M ecosystem fund announced dari treasury
· 2024 (Sei v2): EVM priority fees + base fee burn → additional revenue stream; fee split antara validator/community pool/burn
· Unresolved: Sei Labs revenue model tidak transparan (apakah team mendapat cut dari community pool?); treasury size/composition tidak diungkap; no audited financials
· Supporting Dataset: Phase 5 Financial (Funding History, Revenue Model, Treasury, Financial Dependencies), Phase 6 Token (Distribution, Vesting), Phase 7 Ecosystem (Grant Program)

Technical Decision Pattern

Pola 1: Modular Architecture dengan Custom Components untuk Critical Path
· Decision Pattern: Menggunakan framework standar (Cosmos SDK, CometBFT, IBC-Go) untuk non-critical path, tapi membangun custom components untuk performance-critical path: parallel execution engine, order matching engine, SeiDB storage layer, Geth embedding untuk EVM
· Evidence: Cosmos SDK modules untuk bank/staking/gov/ibc (standard); parallel execution engine custom (whitepaper); order matching engine native module (whitepaper); SeiDB custom storage (SeiDB blog); Geth embedded bukan Ethermint (Sei v2 blog); Wasmer untuk CosmWasm (standard)
· Supporting Dataset: Phase 4 Technology (Architecture, Core Components, Current Technical Stack), Phase 3 EV-016, EV-017, EV-020

Pola 2: Upgrade Bertahap dengan Pengujian Ekstensif (Testnet → Devnet → Mainnet)
· Decision Pattern: Setiap major upgrade melalui multi-stage testing: internal testnet → public testnet/incentivized testnet → devnet → mainnet upgrade via governance; 4+ bulan testnet untuk Sei v2; 17 bulan testnet untuk genesis
· Evidence: Atlantic-1 testnet 2022-03 → Pacific-1 mainnet 2023-08 (17 bulan); Sei v2 announcement 2024-04 → testnet 2024-07 → mainnet 2024-08 (4 bulan); audit sebelum setiap major release (Veridise pre-mainnet, Trail of Bits Sei v2, Oak Security SeiDB)
· Supporting Dataset: Phase 3 EV-002, EV-003, EV-004, EV-016 to EV-020, Phase 4 Technology (Audit History, Technical Upgrade History)

Pola 3: Native Integration di Consensus Layer untuk Trading Primitives
· Decision Pattern: Order matching engine dibangun sebagai native Cosmos SDK module (bukan smart contract); parallel execution di consensus layer (bukan L2/rollup); SeiDB terintegrasi di state commit path; precompile contracts native Go untuk EVM access ke native modules
· Evidence: Whitepaper order matching engine design; parallel execution engine di Tendermint ABCI++; SeiDB replaces IAVDB di storage layer; precompiles untuk bank/staking/IBC/tokenfactory (Sei v2 docs); tidak menggunakan Ethermint (yang menjalankan EVM sebagai module)
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-004, EV-020, Phase 4 Technology (Core Components: Order Matching Engine, Parallel Execution Engine, SeiDB, Precompile Contracts), Phase 8 Market (Narrative: Trading-Optimized Chain)

Pola 4: Dual VM Strategy dengan Shared State Layer (SeiDB)
· Decision Pattern: Menjalankan CosmWasm (Wasmer) dan EVM (Geth) bersamaan di consensus layer yang sama; shared state melalui SeiDB; cross-VM calls via precompile contracts; bukan pilihan "either/or" tapi "both/and"
· Evidence: Sei v2 blog "dual VM"; SeiDB blog "shared storage"; precompiles untuk cross-VM access; Wasmer + Geth both in go.mod; execution environment documentation menampilkan both
· Supporting Dataset: Phase 4 Technology (Execution Environment: CosmWasm + EVM, SeiDB, Precompile Contracts, Known Limitations: Cross-VM Latency), Phase 3 EV-016, EV-020, Phase 7 Ecosystem (Developer Ecosystem: both Hardhat/Foundry and CosmWasm CLI)

Pola 5: Security-First dengan Multiple Audits Sebelum Mainnet/Upgrade
· Decision Pattern: Minimal 2 audit firms untuk setiap major release; audit scope mencakup consensus, execution, storage, precompiles; findings addressed sebelum launch; post-launch bug bounty program implied (tidak dipublikasikan formal)
· Evidence: 6 core audits: Informal Systems (core modules), Halborn (CosmWasm), Veridise (parallel execution), Trail of Bits (Sei v2 Geth embedding), Oak Security (SeiDB), Zellic (precompiles); all completed pre-respective launches
· Supporting Dataset: Phase 4 Technology (Audit History), Phase 3 EV-004, EV-020

Financial Decision Pattern

Pola 1: Equity + Token Allocation Bundled di Series A/B (No Separate Token Sale)
· Decision Pattern: Series A ($5M Multicoin lead) dan Series B ($30M Jump Crypto lead) memberikan equity + token allocation sekaligus; tidak ada private sale token terpisah, tidak ada public sale/ICO/Launchpool; TGE via Binance spot listing langsung
· Evidence: Sei blog Series A announcement "$35M total Series A+B"; whitepaper tokenomics "Investors 22%"; Binance listing at TGE no Launchpool; investor list mencakup VCs + market makers (Jump, Wintermute, Jane Street, Flow Traders, GSR, Kronos)
· Rationale: Menghindari regulatory risk public token sale (Howey test); investor alignment via equity + token; Binance listing memberikan liquidity dan price discovery tanpa discount private sale; market maker investors menyediakan liquidity day-1
· Supporting Dataset: Phase 2 Entity (Investors not separately listed but named in funding), Phase 3 EV-001, EV-005, Phase 5 Financial (Funding History: Series A, Series B, Strategic Round, Token Sale), Phase 6 Token (Distribution, TGE, Token Sale)

Pola 2: Treasury/Community Pool Management via On-Chain Governance (No Team Control)
· Decision Pattern: Protocol fees (gas, order matching, IBC, EVM priority) → community pool → governance proposals untuk spending; Sei Labs tidak memiliki direct control; $50M ecosystem fund dari treasury tapi deployment via grant program (application process)
· Evidence: Cosmos SDK distribution module; community pool address on-chain; governance proposals di Seitrace untuk community pool spend; ecosystem fund blog "from protocol treasury"; no team multisig spending disclosed
· Rationale: Desentralisasi progresif; regulatory compliance (team tidak control treasury); community alignment; tapi menciptakan opacity (no dashboard) dan slow deployment (governance latency)
· Supporting Dataset: Phase 5 Financial (Revenue Model, Treasury, Fundraising Mechanism), Phase 6 Token (Governance, Distribution: Foundation/Community), Phase 7 Ecosystem (Grant Program, Governance Ecosystem: DAO)

Pola 3: Ecosystem Fund dari Protocol Treasury (Not Fresh Capital)
· Decision Pattern: $50M ecosystem fund sourced dari Foundation/Community allocation (10% + portion of 48% community), bukan fresh raise; grant categories broad (DeFi, infra, tooling, NFT, gaming); no matching fund atau milestone-based tranches publik
· Evidence: Ecosystem fund blog "$50M from protocol treasury"; tokenomics Foundation 10% + Community 48%; grant application via forms; no public dashboard of deployment
· Rationale: Menggunakan token treasury untuk bootstrap ecosystem; token price appreciation memperbesar fund USD value; tapi fund size fixed dalam SEI → USD value volatil; sustainability bergantung pada protocol revenue refill community pool
· Supporting Dataset: Phase 5 Financial (Ecosystem Fund), Phase 6 Token (Distribution: Foundation 10%, Community 48%), Phase 7 Ecosystem (Grant Program), Phase 8 Market (Competitor Landscape: larger ecosystem funds)

Pola 4: Revenue Diversification melalui Multiple Fee Streams
· Decision Pattern: Menambahkan fee streams seiring upgrade: native gas fees (2023) → order matching fees (2023) → IBC packet fees (2023) → EVM priority fees + base fee burn (2024 Sei v2); semua masuk community pool kecuali base fee burned
· Evidence: Phase 5 Revenue Model (6 fee types); Phase 4 Technology (Order Matching Engine, Sei v2 EVM Priority Fees, IBC Module); Phase 3 EV-004, EV-007, EV-008, EV-020
· Rationale: Maximize value capture dari semua aktivitas on-chain; trading activity (order matching, perp DEX) menghasilkan fee tinggi; EVM compatibility membuka fee market Ethereum-style; burn mechanism untuk narrative alignment
· Supporting Dataset: Phase 3 EV-004, EV-007, EV-008, EV-020, Phase 4 Technology (Core Components), Phase 5 Financial (Revenue Model), Phase 6 Token (Inflation/Deflation: EVM base fee burn)

Pola 5: Vesting Cliff Synchronization (Team + Investors 12 Months Post-TGE)
· Decision Pattern: Team (20%) dan Investors (22%) sama-sama 12-month cliff + linear vesting; cliff berakhir Aug 2024; Foundation (10%) partial unlock at TGE + 60mo linear; Community (48%) programmatic ongoing
· Evidence: Whitepaper vesting schedule; Phase 6 Token (Vesting Schedule); Phase 3 EV-004 (TGE 2023-08-15) → cliff end estimated 2024-08
· Rationale: Align team dan investor incentives; mencegah early dump; cliff synchronization menciptakan "unlock wall" Aug 2024 yang perlu dikelola narasi; investor termasuk market makers (Wintermute, Jane Street, Flow Traders) yang bisa provide liquidity saat unlock
· Supporting Dataset: Phase 3 EV-004, Phase 5 Financial (Strategic Round), Phase 6 Token (Distribution, Vesting Schedule, Major Token Events: Team/Investor Cliff End)

Ecosystem Decision Pattern

Pola 1: Dual Bridge Strategy (Wormhole + Axelar) untuk Redundansi dan Coverage Maksimal
· Decision Pattern: Mengintegrasikan kedua major generic message passing bridges sekaligus: Wormhole (Guardian network, Solana + EVM coverage) + Axelar (PoS validators, Cosmos + EVM coverage); tidak exclusive ke satu bridge
· Evidence: Phase 3 EV-008 (both activated same month); Phase 4 Technology (Wormhole Bridge Integration, Axelar Bridge Integration); Phase 7 Ecosystem (Major Integrations: both; Infrastructure Providers: both); Phase 7 Ecosystem Risks (Bridge Dependency listed for both)
· Rationale: Wormhole stronger di Solana/EVM; Axelar stronger di Cosmos/IBC; redundancy jika satu bridge compromised; maximize chain coverage (7+ chains); developer choice
· Trade-off: Double trust assumptions; double smart contract risk; fragmented liquidity (SEI di Wormhole vs Axelar contracts); user confusion
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technology (External Dependencies, Core Components), Phase 7 Ecosystem (Major Integrations, Infrastructure Providers, Ecosystem Risks)

Pola 2: Dual Oracle Strategy (Pyth + Chainlink) untuk Data Diversity
· Decision Pattern: Mengintegrasikan Pyth (first-party publisher, low-latency, financial market focus) + Chainlink (DONs, broad coverage, VRF/CCIP/Automation) sekaligus; tidak exclusive
· Evidence: Phase 3 EV-009 (both same month); Phase 4 Technology (Pyth Oracle, Chainlink Oracle); Phase 7 Ecosystem (Major Integrations: both; Infrastructure Providers: both); Phase 7 Ecosystem Risks (Oracle Dependency for both)
· Rationale: Pyth superior untuk high-frequency trading price feeds (HFT, perp DEX); Chainlink superior untuk broad asset coverage, randomness (VRF), cross-chain messaging (CCIP); DeFi apps butuh keduanya (Leviathan perp → Pyth; Silo lending → Chainlink)
· Trade-off: Double oracle risk; developer complexity memilih oracle; cost double untuk protocol (jika subsidize feeds)
· Supporting Dataset: Phase 3 EV-009, Phase 4 Technology (Core Components: Pyth, Chainlink), Phase 7 Ecosystem (Major Integrations, Infrastructure Providers, Ecosystem Risks)

Pola 3: Wallet Support Segmentation (Cosmos Native + EVM) untuk User Acquisition
· Decision Pattern: Support native Cosmos wallets (Keplr, Leap, Compass) untuk existing Cosmos users; tambah MetaMask/Rabby via Sei v2 EVM RPC untuk Ethereum users; tidak memaksa user ganti wallet
· Evidence: Phase 3 EV-015 (Keplr/Leap/Compass Dec 2023); Phase 3 EV-018 (MetaMask May 2024); Phase 7 Ecosystem (Wallet Ecosystem: 8 wallets listed with support type segmentation)
· Rationale: Lower barrier to entry; Cosmos users (~2M+) retain familiar UX; Ethereum users (20M+ MetaMask) bisa access Sei tanpa friction; wallet diversity sebagai moat
· Supporting Dataset: Phase 3 EV-015, EV-018, Phase 7 Ecosystem (Wallet Ecosystem), Phase 8 Market (Narrative: Interoperability/Chain Abstraction secondary)

Pola 4: Exchange Listing Strategy: Tier-1 CEX First, DEX Native, Perp Heavy
· Decision Pattern: Binance listing at TGE (tier-1 global); rapid follow-on listings di Coinbase (US), Kraken (US/EU), Bybit/OKX/KuCoin (Asia); native DEX (DragonSwap) launch week-2; perp DEX (Leviathan) month-3; perp volume 5-10x spot volume
· Evidence: Phase 3 EV-005 (Binance TGE), EV-010 (DragonSwap Sept), EV-013 (Leviathan Nov); Phase 7 Ecosystem (Exchange Ecosystem: 11 CEX, 3+ DEX); Phase 8 Market (Trading Markets: perp volume $500M-1.5B vs spot $100-300M)
· Rationale: Binance provides global liquidity day-1; Coinbase/Kraken untuk US compliance; Asian exchanges untuk retail volume; native DEX/perp captures trading fee revenue on-chain; perp volume drives token relevance untuk traders
· Supporting Dataset: Phase 3 EV-005, EV-010, EV-013, Phase 7 Ecosystem (Exchange Ecosystem, Applications), Phase 8 Market (Trading Markets, Liquidity, Adoption Metrics)

Pola 5: Developer Tooling Parity (Hardhat/Foundry untuk EVM, CosmWasm CLI untuk Native)
· Decision Pattern: Full support untuk Ethereum tooling (Hardhat plugin, Foundry, MetaMask) + Cosmos tooling (CosmWasm CLI, Ignite CLI, Keplr); SDKs di JS/TS/Python; tidak memaksa developer belajar tooling baru
· Evidence: Phase 7 Ecosystem (Developer Ecosystem: SDKs, APIs, Toolchains); Phase 3 EV-018 (MetaMask), EV-019 (Sei v2 testnet dengan Hardhat/Foundry validation); Phase 4 Technology (Development Framework)
· Rationale: Developer experience adalah primary adoption driver; Ethereum developers tidak akan migrasi kalau tooling broken; CosmWasm developers retain existing workflow; dual tooling = dual developer funnel
· Supporting Dataset: Phase 3 EV-018, EV-019, Phase 4 Technology (Development Framework), Phase 7 Ecosystem (Developer Ecosystem), Phase 8 Market (Narrative: EVM Compatibility, Developer Count metric)

Governance Decision Pattern

Pola 1: On-Chain Governance untuk Semua Parameter Changes dan Upgrades
· Decision Pattern: Setiap parameter change (inflation, fees, validator count), software upgrade (Sei v2, CosmWasm 2.0, IBC-Go v8), community pool spend → on-chain proposal via Cosmos SDK Governance Module; voting power = staked SEI; delegators bisa override validator vote
· Evidence: Phase 6 Token (Governance: voting system, proposal system); Phase 7 Ecosystem (Governance Ecosystem: DAO, Validator Set); Phase 3 EV-020 (Sei v2 upgrade via governance); Phase 4 Technology (Technical Upgrade History: all upgrades via governance)
· Rationale: Credible neutrality; community ownership; regulatorily safer (team tidak unilaterally control); Cosmos SDK standard
· Gap: Quorum/threshold parameters tidak dipublikasikan di docs; validator default voting power besar (delegator apathy); Foundation/team allocation tidak vote (locked/vesting) → current governance dominated oleh early validators dan community pool
· Supporting Dataset: Phase 3 EV-020, Phase 4 Technology (Technical Upgrade History), Phase 6 Token (Governance), Phase 7 Ecosystem (Governance Ecosystem)

Pola 2: Foundation Assumed tapi Not Publicly Verified sebagai Treasury Custodian
· Decision Pattern: Whitepaper mention "Foundation 10%"; ecosystem fund blog "from protocol treasury"; tapi no legal entity filing, no multi-sig address published, no Foundation website/team distinct dari Sei Labs
· Evidence: Phase 6 Token (Distribution: Foundation 10%); Phase 5 Financial (Treasury: not disclosed); Phase 7 Ecosystem (Governance Ecosystem: Foundation "assumed entity", legal structure not confirmed); Phase 2 Entity (no Foundation entity identified)
· Rationale: Common Cosmos pattern (Cayman/Swiss foundation); separates protocol treasury dari company (Sei Labs); tapi lack of transparency menciptakan trust issue
· Risk: Regulatory ambiguity (US person control of foundation?); single point of failure jika foundation multisig compromised; community tidak bisa audit treasury management
· Supporting Dataset: Phase 2 Entity (no Foundation), Phase 5 Financial (Treasury), Phase 6 Token (Distribution: Foundation), Phase 7 Ecosystem (Governance Ecosystem: Foundation), Phase 8 Open Threads (Foundation legal entity)

Pola 3: Validator Set sebagai De Facto Governance Council
· Decision Pattern: Top 100 validators by stake produce blocks dan vote pada proposals by default untuk delegators; validators juga run oracle price feeders (beberapa); validator signaling untuk upgrade readiness; Nakamoto coefficient ~8-12 estimated
· Evidence: Phase 7 Ecosystem (Governance Ecosystem: Validator Set, Validator Group); Phase 8 Market (Adoption Metrics: Validator Count 100, Nakamoto Coefficient estimated); Phase 4 Technology (Consensus Mechanism: validator set dynamics)
· Rationale: PoS security alignment; validators have skin in the game; operational expertise untuk technical upgrades; tapi centralization risk (entity concentration tidak transparent)
· Risk: Validator cartel possible; delegator override rate rendah (apathy); validator business model (commission) mungkin misaligned dengan long-term protocol health
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Security Model), Phase 7 Ecosystem (Governance Ecosystem, Infrastructure Providers: Validator Operators), Phase 8 Market (Validator Count, Nakamoto Coefficient)

Pola 4: Sei Labs Core Team sebagai De Facto Technical Leadership (Bukan Formal Governance Body)
· Decision Pattern: Sei Labs authors specifications (Sei v2, SeiDB), implements upgrades, runs testnets, coordinates validators; tidak memiliki formal veto power tapi de facto control melalui technical expertise dan token allocation (team 20% vesting)
· Evidence: Phase 2 Entity (Jayendra Jog, Dan Edlebeck, Sei Labs Inc.); Phase 3 EV-016, EV-017 (announcements via Sei Labs blog); Phase 4 Technology (GitHub repos under sei-protocol org); Phase 7 Ecosystem (Governance Ecosystem: Committee: Sei Labs Core Team)
· Rationale: Bootstrapping phase butuh strong technical leadership; founder vision alignment; gradual decentralization sebagai tokens vest
· Risk: Key person dependency (Jayendra/Dan); regulatory exposure (US corporation controlling protocol); transition ke true DAO tidak memiliki timeline formal
· Supporting Dataset: Phase 2 Entity, Phase 3 EV-016, EV-017, Phase 4 Technology (Official Technical Resources: GitHub), Phase 7 Ecosystem (Governance Ecosystem)

Risk Response Pattern

Pola 1: Preemptive Audits dan Extended Testnet untuk Technical Risk Mitigation
· Decision Pattern: Sebelum setiap major launch/upgrade, melakukan multiple audits (2-3 firms) dan extended public testnet (4-17 bulan); findings addressed pre-launch; no mainnet exploit/hack sejauh ini
· Trigger: High-value DeFi protocols memerlukan security assurance; competitor L1s memiliki exploit history (Solana outages, Wormhole hack, Nomad bridge hack)
· Evidence: Phase 4 Technology (Audit History: 6 core audits pre-respective launches); Phase 3 EV-002 (17 bulan testnet), EV-019 (4 bulan Sei v2 testnet); Phase 7 Ecosystem Risks (SeiDB maturity, Geth embedding, Wasmer determinism flagged as risks tapi mitigated via audit)
· Response: Audit-first culture; testnet sebagai production simulation; bug bounty implied tapi tidak dipublikasikan formal
· Result: Zero critical mainnet exploits; zero chain halts post-mainnet; validator set stable; SeiDB/Sei v2 upgrades smooth
· Supporting Dataset: Phase 3 EV-002, EV-003, EV-019, Phase 4 Technology (Audit History, Technical Upgrade History, Known Limitations), Phase 7 Ecosystem (Ecosystem Risks)

Pola 2: Dual/Redundant Infrastructure untuk Bridge dan Oracle Risk
· Decision Pattern: Mengintegrasikan DUA bridge (Wormhole + Axelar) dan DUA oracle (Pyth + Chainlink) sekaligus; tidak bergantung pada single provider; jika satu compromised, yang lain still operational
· Trigger: Wormhole hack Feb 2022 ($320M); Nomad hack Aug 2022 ($190M); oracle manipulation attacks di DeFi (Mango Markets, Eisenberg); competitor L1 sering single bridge/oracle
· Evidence: Phase 3 EV-008, EV-009 (both activated same month mainnet); Phase 4 Technology (Core Components: both bridges, both oracles); Phase 7 Ecosystem (Major Integrations: both; Infrastructure Providers: both; Ecosystem Risks: Bridge/Oracle Dependency listed as HIGH for both)
· Response: Redundancy by design; developer bisa choose; protocol tidak endorse satu over another
· Result: Zero bridge/oracle incident affecting Sei DeFi; Leviathan perp menggunakan Pyth; Silo lending menggunakan Chainlink; cross-chain liquidity via both bridges
· Supporting Dataset: Phase 3 EV-008, EV-009, Phase 4 Technology (Core Components, External Dependencies), Phase 7 Ecosystem (Major Integrations, Infrastructure Providers, Ecosystem Risks)

Pola 3: Gradual Decentralization via Token Vesting dan Governance Activation
· Decision Pattern: Team/investor tokens locked 12-month cliff; governance active day-1 tapi voting power concentrated di validators/community pool; cliff end Aug 2024 → voting power shifts ke broader holders; Foundation/ecosystem fund deployment gradual
· Trigger: Regulatory pressure (SEC enforcement on L1 tokens); community demand untuk decentralization; competitor (Aptos, Sui) criticized untuk insider concentration
· Evidence: Phase 6 Token (Vesting Schedule: Team/Investors 12mo cliff); Phase 3 EV-004 (TGE), derived cliff end Aug 2024; Phase 7 Ecosystem (Governance Ecosystem: DAO active, Foundation assumed); Phase 5 Financial (Fundraising: equity+token bundled)
· Response: Time-based decentralization; no emergency centralization measures (no pause function, no admin keys pada native token); on-chain governance dari genesis
· Result: Cliff passed Aug 2024 tanpa major governance attack; monthly vesting creates steady supply increase; community pool growing via fees
· Supporting Dataset: Phase 3 EV-004, Phase 5 Financial (Fundraising, Financial Risk), Phase 6 Token (Distribution, Vesting, Governance, Major Token Events), Phase 7 Ecosystem (Governance Ecosystem)

Pola 4: Technical Upgrade Coordination via Signaling dan Extended Testnet
· Decision Pattern: Major upgrades (Sei v2) di-coordinate melalui: public announcement → spec publication → testnet → validator signaling → governance proposal → scheduled upgrade block; 4+ bulan lead time; validator upgrade readiness tracked
· Trigger: Cosmos SDK upgrade coordination challenges (gaia upgrades); risk of chain halt jika >1/3 validators tidak upgrade; Sei v2 complexity (Geth embedding, SeiDB) butuh validator preparation
· Evidence: Phase 3 EV-016 (announcement Apr 2024), EV-019 (testnet Jul 2024), EV-020 (mainnet Aug 2024); Phase 4 Technology (Technical Upgrade History); Phase 7 Ecosystem Risks (Cosmos SDK Upgrade Coordination, Validator Set Centralization)
· Response: Structured upgrade timeline; testnet untuk validator practice; governance proposal untuk on-chain signaling; upgrade block height predetermined
· Result: Sei v2 upgrade successful; no chain halt; validator participation high; SeiDB activated smoothly
· Supporting Dataset: Phase 3 EV-016, EV-019, EV-020, Phase 4 Technology (Technical Upgrade History, Known Limitations: Governance Upgrade Coordination), Phase 7 Ecosystem (Ecosystem Risks: Validator Set Centralization, Cosmos SDK Upgrade Coordination)

Recurring Behavioral Pattern

Pola 1: Dual/Redundant Approach untuk Critical Dependencies
· Pattern: Selalu memilih DUA provider untuk critical infrastructure: Bridges (Wormhole + Axelar), Oracles (Pyth + Chainlink), Wallets (Cosmos native + EVM), VMs (CosmWasm + EVM), Execution Clients (Wasmer + Geth)
· Evidence: Phase 3 EV-008, EV-009, EV-015, EV-018, EV-020; Phase 4 Technology (Core Components, External Dependencies); Phase 7 Ecosystem (Major Integrations, Wallet Ecosystem, Infrastructure Providers)
· Frequency: 5 critical dependency categories, all dual-sourced
· Rationale: Risk diversification; avoid vendor lock-in; maximize coverage (Solana vs Cosmos vs Ethereum ecosystems); developer/user choice
· Trade-off: Increased complexity; double audit surface; fragmented liquidity/integration effort; higher operational overhead

Pola 2: Major Upgrade/Announcement Setiap ~12 Bulan
· Pattern: 2022-03 Testnet → 2023-08 Mainnet (17 bulan) → 2024-04 Sei v2 Announcement (8 bulan post-mainnet) → 2024-08 Sei v2 Mainnet (4 bulan post-announcement) → next: CosmWasm 2.0 / IBC-Go v8 (estimated Q4 2024)
· Evidence: Phase 3 History (all events timeline); Phase 4 Technology (Technical Upgrade History)
· Frequency: ~3 major milestones per 2 tahun; cadence mempercepat post-mainnet
· Rationale: Market narrative refresh; competitor response (Monad, Berachain announcements 2024); technical debt resolution (SeiDB untuk state bloat); investor milestone expectations

Pola 3: Ecosystem App Launch dalam Cluster Post-Infrastructure Ready
· Pattern: Infrastructure ready (mainnet + bridges + oracles + wallets) → cluster app launches dalam 3 bulan: DragonSwap (Sep), Silo (Sep), Yei (Oct), Leviathan (Nov), Pallet (Nov) 2023
· Evidence: Phase 3 EV-004 (Mainnet Aug), EV-007/008/009 (Infra Aug), EV-010 to EV-014 (Apps Sep-Nov); Phase 7 Ecosystem (Applications)
· Frequency: One-time cluster post-genesis; subsequent apps trickle (Sei v2 EVM apps expected cluster post-Aug 2024)
· Rationale: Infrastructure readiness unlocks builder confidence; coordinated marketing push; liquidity bootstrapping simultan; first-mover advantage per category

Pola 4: Token Unlock Events Dikotomi Narasi (Cliff End = Risk/Opportunity)
· Pattern: Team/investor 12-month cliff (Aug 2024) di-narrate sebagai "decentralization milestone" bukan "sell pressure"; ecosystem fund deployment dipercepat pre-cliff untuk show traction; no explicit unlock management communication
· Evidence: Phase 6 Token (Vesting Schedule, Major Token Events: Team/Investor Cliff End); Phase 5 Financial (Ecosystem Fund announced 2023-Q4 pre-cliff); Phase 8 Market (no explicit unlock dashboard)
· Frequency: Major cliff Aug 2024; subsequent monthly linear vesting; Foundation 60mo linear; Community ongoing
· Rationale: Control narrative; avoid "unlock FUD"; show protocol maturity via ecosystem growth; investor alignment (market makers dalam investor list bisa absorb selling)

Pola 5: Technical Specification Publication Sebelum Implementation (Sei v2, SeiDB)
· Pattern: Blog announcement dengan technical detail (Sei v2 blog, SeiDB blog) → public spec → testnet → mainnet; tidak "stealth launch"; community bisa review dan critique design
· Evidence: Phase 3 EV-016 (Sei v2 announcement Apr 2024 dengan spec), EV-017 (SeiDB announcement Apr 2024), EV-019 (testnet Jul), EV-020 (mainnet Aug); Phase 4 Technology (Official Technical Resources: blogs, docs)
· Frequency: 2 major tech specs published 2024 (Sei v2, SeiDB); prior: whitepaper 2021
· Rationale: Credibility dengan technical community; attract developer feedback early; marketing narrative control; regulatorily transparent (no hidden features)

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Kecepatan Eksekusi (Validator Set Size vs Throughput)
· Decision: Validator set dibatasi 100 aktif (top by stake); Tendermint/CometBFT consensus dengan 2/3 threshold; parallel execution untuk throughput; bukan permissionless validator set seperti Bitcoin/Ethereum PoW
· Trade-off: Mengorbankan validator decentralization (Nakamoto coefficient ~8-12) demi consensus speed (~400-600ms block time) dan finality deterministik; 100 validator cap menciptakan barrier to entry untuk validator baru
· Evidence: Phase 4 Technology (Consensus Mechanism: 100 validators, ~400-600ms); Phase 7 Ecosystem (Governance: Validator Set 100); Phase 8 Market (Validator Count 100, Nakamoto Coefficient estimated 8-12)
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Security Model), Phase 7 Ecosystem (Governance Ecosystem, Ecosystem Risks: Validator Centralization), Phase 8 Market (Adoption Metrics)

Trade-off 2: Keamanan Bridge vs Composability Cross-Chain (Trust Assumptions vs Liquidity Access)
· Decision: Mengintegrasikan Wormhole (Guardian multisig 19) dan Axelar (PoS validators) untuk cross-chain liquidity; tidak menunggu trust-minimized bridge (seperti IBC untuk non-Cosmos) yang belum exist
· Trade-off: Mengorbankan trust-minimization (bridged assets secured by external validator sets, bukan Sei consensus) demi immediate access ke Ethereum/Solana/EVM L2 liquidity dan user base; bridge hack = bridged asset value loss di Sei
· Evidence: Phase 3 EV-008; Phase 4 Technology (External Dependencies: Wormhole, Axelar); Phase 7 Ecosystem (Major Integrations: both bridges; Infrastructure Providers: both; Ecosystem Risks: Bridge Dependency HIGH)
· Supporting Dataset: Phase 3 EV-008, Phase 4 Technology (External Dependencies, Core Components), Phase 7 Ecosystem (Major Integrations, Infrastructure Providers, Ecosystem Risks)

Trade-off 3: Kompleksitas Teknis (Dual VM + Custom Storage) vs Developer Adoption (EVM Compatibility)
· Decision: Membangun dual VM (CosmWasm + EVM via Geth) dengan custom storage layer (SeiDB) dan precompile contracts; bukan choose one VM atau gunakan existing solution (Ethermint, evmOS)
· Trade-off: Mengorbankan simplicity, audit surface, maintenance burden (Geth fork, Wasmer determinism, cross-VM reentrancy, SeiDB maturity) demi capture Ethereum developer base (10x larger than CosmWasm); time-to-market delay (Sei v2 1 tahun development)
· Evidence: Phase 3 EV-016, EV-020; Phase 4 Technology (Execution Environment: both VMs, SeiDB, Precompiles, Known Limitations: Cross-VM Latency, Geth Embedding Dependency, SeiDB Maturity); Phase 7 Ecosystem (Developer Ecosystem: both toolchains); Phase 8 Market (Narrative: EVM Compatibility Main, Competitor: Monad, Berachain)
· Supporting Dataset: Phase 3 EV-016, EV-020, Phase 4 Technology (Execution Environment, Sei v2 EVM Layer, SeiDB, Known Limitations), Phase 7 Ecosystem (Developer Ecosystem), Phase 8 Market (Narrative Position, Competitor Landscape)

Trade-off 4: Treasury Transparency vs Operational Flexibilitas (Foundation Opacity vs Grant Speed)
· Decision: Sei Foundation legal entity tidak dipublikasikan; treasury address tidak labeled; ecosystem fund deployment via private grant process; no public dashboard
· Trade-off: Mengorbankan community trust dan accountability demi flexibility dalam grant decisions, regulatory ambiguity management, dan negotiation leverage dengan recipients; competitor (Aptos Foundation, Sui Foundation) lebih transparan
· Evidence: Phase 2 Entity (no Foundation); Phase 5 Financial (Treasury: not disclosed); Phase 6 Token (Distribution: Foundation 10%); Phase 7 Ecosystem (Governance: Foundation assumed, Grant Program no dashboard); Phase 8 Open Threads (Foundation legal entity, Ecosystem Fund deployment transparency)
· Supporting Dataset: Phase 2 Entity, Phase 5 Financial (Treasury), Phase 6 Token (Distribution), Phase 7 Ecosystem (Governance Ecosystem, Grant Program), Phase 8 Open Threads

Trade-off 5: Inflationary Tokenomics (Staking Rewards) vs Token Holder Value Accrual (Fee Burn)
· Decision: Staking rewards ~7% inflationary (minted per block); partial burn hanya untuk EVM base fee (Sei v2); native tx fees tidak burned; net supply inflationary
· Trade-off: Mengorbankan token scarcity/value accrual via burn demi network security (staking rewards attract validators/delegators) dan DeFi composability (low gas fees); EVM burn token gesture untuk narrative alignment tapi quantitatively kecil vs staking emission
· Evidence: Phase 6 Token (Inflation/Deflation: 7% target, EVM base fee burn only); Phase 4 Technology (Sei v2 EVM Priority Fees, Consensus Mechanism); Phase 5 Financial (Revenue Model: fees to community pool); Phase 8 Market (Adoption Metrics: Staking Participation 65-70%)
· Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Sei v2 EVM Layer), Phase 5 Financial (Revenue Model), Phase 6 Token (Inflation/Deflation, Utility: Staking, Gas), Phase 8 Market (Adoption Metrics)

Behavioral Summary

Prioritas Utama Proyek:
1. Technical Differentiation via Parallel Execution + Native Order Matching → trading-optimized L1 moat
2. Developer Adoption via EVM Compatibility (Sei v2) → capture Ethereum developer liquidity
3. Ecosystem Growth via Dual Infrastructure (bridges, oracles, wallets, VMs) → reduce switching costs
4. Progressive Decentralization via Token Vesting + On-Chain Governance → regulatory compliance + community ownership
5. Revenue Diversification via Multi-Source Fee Capture → sustainable treasury post-VC funding

Cara Mengambil Keputusan:
- Founder-led technical vision (Jayendra/Dan) → spec publication → community review → audit → testnet → governance upgrade
- Data-driven untuk technical choices (parallel execution benchmarks, SeiDB design docs, audit results)
- Narrative-aware untuk market positioning (Sei v2 response ke Monad/Berachain; EVM compatibility sebagai must-have 2024)
- Risk-mitigation melalui redundancy (dual bridges, dual oracles, dual VMs) dan preemptive audits
- Gradual decentralization: team control → on-chain governance → community pool → Foundation (assumed) → full DAO (aspirational)

Faktor Paling Sering Mempengaruhi Keputusan:
1. Competitive Landscape (Monad, Berachain, Hyperliquid, Solana, Aptos, Sui) → drives Sei v2, SeiDB, EVM narrative
2. Developer Experience (tooling, wallet, language) → drives dual VM, dual wallet, dual toolchain
3. Regulatory Environment (US Delaware corp, SEC framework) → drives no public sale, equity+token bundle, Foundation opacity, gradual decentralization
4. Infrastructure Maturity (Cosmos SDK, CometBFT, Geth, Wasmer, IBC-Go) → builds on proven layers, customizes critical path
5. Capital Efficiency (VC funding $35M, ecosystem fund $50M from treasury) → drives revenue diversification, grant program, no fresh raises

Pola Evolusi:
- Phase 1 (2021-2022): Research & Development → parallel execution prototype, Cosmos SDK base
- Phase 2 (2022-2023): Testnet & Validation → 17 bulan testnet, audit, validator onboarding
- Phase 3 (2023-08 to 2023-12): Mainnet Launch & Ecosystem Bootstrap → TGE, Binance, infra, flagship apps, wallets
- Phase 4 (2024): Pivot to EVM + Storage Scaling → Sei v2, SeiDB, MetaMask, mainnet upgrade
- Phase 5 (2024+): Maturation & Competition → CosmWasm 2.0, IBC-Go v8, EVM app cluster, institutional adoption

Kekuatan Utama:
1. Technical Moat: Parallel execution + native order matching + SeiDB = genuine differentiation untuk trading use case
2. Dual VM Strategy: CosmWasm (security, Rust) + EVM (adoption, Solidity) = widest developer addressable market
3. Infrastructure Completeness: Bridges, oracles, wallets, explorers, indexers all live sejak early → builder ready
4. Capital Efficiency: $35M VC → mainnet + $50M ecosystem fund from treasury → no down round, no token sale dilution
5. Exchange/Market Maker Relationships: Binance TGE listing + investor MMs (Wintermute, Jane Street, Flow Traders, GSR) → deep liquidity

Kelemahan Utama:
1. Foundation/ Treasury Opacity: No legal entity confirmed, no addresses labeled, no dashboard → trust deficit
2. Dual VM Complexity: Geth fork maintenance, cross-VM reentrancy risk, Wasmer determinism, SeiDB maturity unproven at scale
3. Bridge/Oracle External Risk: 100% bridged asset value depends on Wormhole/Axelar/Pyth/Chainlink security
4. Validator Centralization: Nakamoto coefficient ~8-12, entity concentration unknown, cloud dependency high
5. No Sustainable Revenue Model Published: Protocol fees → community pool, but Sei Labs ops funding unclear post-VC; token price dependency high
6. Regulatory Overhang: Delaware corporation + token = SEC enforcement risk; no public legal opinion
7. Governance Maturity: Delegator apathy, validator dominance, no Foundation transparency, slow community pool deployment

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Sei

## Core Insights

Insight 1: Parallel execution di consensus layer (bukan L2/rollup) menciptakan differentiator teknis yang sulit direplikasi
Explanation: Sei membangun parallel execution engine (optimistic concurrency control) dan native order matching engine langsung di Tendermint/CometBFT ABCI++ layer, bukan sebagai smart contract atau rollup. Arsitektur ini memungkinkan throughput tinggi (~400-600ms block time) dengan instant finality untuk trading workloads【Phase 4 — Core Components: Parallel Execution Engine, Order Matching Engine】【Phase 1 — Category: Layer 1 blockchain optimized for trading】【Phase 8 — Narrative Position: Parallel Execution L1】
Evidence: Sei whitepaper technical architecture; Sei v2 blog mentioning parallel execution applies to EVM tx too; Veridise audit pre-mainnet
Supporting Dataset: Phase 1 Foundation, Phase 3 EV-002/EV-004, Phase 4 Technology (Architecture, Core Components, Audit History), Phase 8 Market (Narrative Position)
Confidence: HIGH

Insight 2: Dual VM strategy (CosmWasm + EVM via embedded Geth) memperluas addressable developer market 10x tanpa meninggalkan existing CosmWasm builders
Explanation: Sei v2 meng-embed Geth langsung ke consensus layer (bukan Ethermint), menjalankan CosmWasm (Wasmer) dan EVM bersamaan dengan shared state via SeiDB. Precompile contracts memungkinkan cross-VM calls ke native modules (bank, staking, IBC, tokenfactory). Hardhat/Foundry/MetaMask support untuk EVM; CosmWasm CLI/Ignite untuk native【Phase 4 — Execution Environment: CosmWasm + EVM, Sei v2 EVM Layer, Precompile Contracts】【Phase 3 — EV-016, EV-019, EV-020】【Phase 7 — Developer Ecosystem: both toolchains】【Phase 8 — Narrative: EVM Compatibility Main】
Evidence: Sei v2 announcement blog; Sei v2 docs precompiles; Trail of Bits audit Sei v2 Geth embedding; MetaMask support announcement
Supporting Dataset: Phase 3 History (EV-016, EV-018, EV-019, EV-020), Phase 4 Technology (Execution Environment, Sei v2 EVM Layer, Precompiles, Known Limitations), Phase 7 Ecosystem (Developer Ecosystem, Major Integrations), Phase 8 Market (Narrative Position, Competitor Landscape)
Confidence: HIGH

Insight 3: Redundansi infrastructure (dual bridge, dual oracle, dual wallet, dual VM) menjadi pattern konsisten untuk mitigasi single-point-of-failure
Explanation: Sei mengintegrasikan DUA bridge (Wormhole + Axelar), DUA oracle (Pyth + Chainlink), DUA wallet segment (Cosmos native: Keplr/Leap/Compass + EVM: MetaMask/Rabby), DUA VM (CosmWasm + EVM). Pattern ini terlihat di 5 kategori critical dependency【Phase 3 — EV-008, EV-009, EV-015, EV-018, EV-020】【Phase 4 — External Dependencies: Wormhole, Axelar, Pyth, Chainlink】【Phase 7 — Major Integrations, Wallet Ecosystem, Infrastructure Providers】【Phase 9 — Recurring Behavioral Pattern: Dual/Redundant Approach】
Evidence: Mainnet launch month activated both bridges and both oracles simultaneously; wallet support added in two phases; Sei v2 added EVM VM alongside existing CosmWasm
Supporting Dataset: Phase 3 History (EV-008, EV-009, EV-015, EV-018, EV-020), Phase 4 Technology (Core Components, External Dependencies), Phase 7 Ecosystem (Major Integrations, Wallet Ecosystem, Infrastructure Providers, Ecosystem Risks), Phase 9 Behavioral (Recurring Behavioral Pattern)
Confidence: HIGH

Insight 4: Equity + token allocation bundled di Series A/B (no separate token sale) menghindari regulatory risk dan menciptakan distribusi token bersih tanpa retail unlock cliff
Explanation: Series A ($5M Multicoin lead) + Series B ($30M Jump Crypto lead) = $35M total dengan equity + token allocation sekaligus. Tidak ada private sale terpisah, tidak ada public sale/ICO/Launchpool. TGE via Binance spot listing langsung. Investor list mencakup VCs + market makers (Wintermute, Jane Street, Flow Traders, GSR, Kronos)【Phase 5 — Funding History: Series A, Series B, Strategic Round, Token Sale】【Phase 6 — Distribution: Investors 22%, TGE: Binance Spot Listing】【Phase 3 — EV-001, EV-005, EV-006】【Phase 9 — Financial Decision Pattern: Equity + Token Allocation Bundled】
Evidence: Sei blog Series A announcement "$35M total Series A+B"; Binance spotlight announcement at TGE; whitepaper tokenomics "Investors 22%"; no Launchpool usage
Supporting Dataset: Phase 2 Entity (Sei Labs Inc., investors), Phase 3 History (EV-001, EV-005, EV-006), Phase 5 Financial (Funding History, Fundraising Mechanism, Token Sale), Phase 6 Token (Distribution, TGE, Token Sale), Phase 9 Behavioral (Financial Decision Pattern)
Confidence: HIGH

Insight 5: Progressive decentralization via 12-month cliff (team + investors) + on-chain governance dari genesis menciptakan scheduled power shift tanpa emergency measures
Explanation: Team (20%) dan Investors (22%) sama-sama 12-month cliff + linear vesting; cliff berakhir Aug 2024. Governance active day-1 via Cosmos SDK Governance Module; voting power = staked SEI. No pause function, no admin keys pada native token. Foundation (10%) partial unlock TGE + 60mo linear. Community (48%) programmatic ongoing【Phase 6 — Vesting Schedule: Team/Investors 12mo cliff, Foundation 60mo linear】【Phase 3 — EV-004 (TGE 2023-08-15)】【Phase 7 — Governance Ecosystem: DAO active, Validator Set】【Phase 9 — Risk Response Pattern: Gradual Decentralization】
Evidence: Whitepaper vesting schedule; TGE date Aug 15 2023 → cliff end Aug 2024; governance proposals on Seitrace from genesis; no emergency pause mechanism documented
Supporting Dataset: Phase 3 History (EV-004), Phase 5 Financial (Fundraising), Phase 6 Token (Distribution, Vesting Schedule, Governance, Major Token Events), Phase 7 Ecosystem (Governance Ecosystem), Phase 9 Behavioral (Risk Response Pattern)
Confidence: HIGH

Insight 6: Custom components untuk critical path (parallel execution, order matching, SeiDB, Geth embedding) + standard frameworks untuk non-critical path (Cosmos SDK modules, CometBFT, IBC-Go, Wasmer) = optimal technical decision pattern
Explanation: Sei menggunakan Cosmos SDK modules untuk bank/staking/gov/ibc/tokenfactory (standard); tapi membangun custom: parallel execution engine, order matching engine native module, SeiDB storage layer (state store + commit log), Geth embedding untuk EVM (bukan Ethermint). Pattern ini berulang di setiap major upgrade【Phase 4 — Architecture: Modular design separating consensus, execution, storage】【Phase 4 — Core Components: Parallel Execution Engine, Order Matching Engine, SeiDB, Sei v2 EVM Layer】【Phase 3 — EV-016, EV-017, EV-020】【Phase 9 — Technical Decision Pattern: Modular Architecture dengan Custom Components】
Evidence: Sei chain go.mod shows Cosmos SDK/CometBFT/IBC-Go dependencies; whitepaper describes custom parallel execution and order matching; SeiDB blog describes custom storage; Sei v2 blog emphasizes Geth embedding not Ethermint
Supporting Dataset: Phase 3 History (EV-004, EV-016, EV-017, EV-020), Phase 4 Technology (Architecture, Core Components, Current Technical Stack, Technical Upgrade History), Phase 9 Behavioral (Technical Decision Pattern)
Confidence: HIGH

Insight 7: SeiDB (parallelized storage layer: state store + commit log) mengatasi state bloat dan fast sync — tapi trust assumption "trusted checkpoint" tidak fully specified di public docs
Explanation: SeiDB menggantikan IAVDB dengan arsitektur terpisah: State Store (SS) untuk parallel writes dan State Commit Log (SCL) untuk fast sync. Oak Security audit completed pre-mainnet. Namun dokumentasi trust model untuk fast sync checkpoint generation/verification tidak lengkap【Phase 4 — Core Components: SeiDB, Known Limitations: SeiDB Fast Sync Trust Assumption】【Phase 3 — EV-017, EV-020】【Phase 7 — Major Integrations: SeiDB】【Phase 9 — Open Threads: SeiDB fast sync trust assumptions documentation】
Evidence: SeiDB blog announcement; SeiDB repo; Oak Security audit referenced; technical docs mention "trusted checkpoint" without full spec
Supporting Dataset: Phase 3 History (EV-017, EV-020), Phase 4 Technology (Core Components: SeiDB, Known Limitations, Audit History), Phase 7 Ecosystem (Major Integrations), Phase 9 Behavioral (Open Threads)
Confidence: MEDIUM

Insight 8: Validator set 100 (top by stake) dengan Nakamoto coefficient estimated 8-12 entities → centralization risk tinggi tapi consensus speed ~400-600ms dengan instant finality
Explanation: Tendermint/CometBFT BFT consensus dengan 2/3 threshold; 100 active validators; staking participation 65-70%; entity-level concentration tidak transparan (same operator multiple validators tidak identifiable on-chain). Cloud dependency tinggi (AWS/GCP/Azure)【Phase 4 — Consensus Mechanism: 100 validators, ~400-600ms】【Phase 7 — Governance Ecosystem: Validator Set 100】【Phase 8 — Adoption Metrics: Validator Count 100, Nakamoto Coefficient estimated 8-12】【Phase 9 — Strategic Trade-offs: Decentralization vs Throughput】
Evidence: Seitrace validators page; Sei docs validators; staking participation metrics; community estimates on governance forum
Supporting Dataset: Phase 4 Technology (Consensus Mechanism, Security Model), Phase 7 Ecosystem (Governance Ecosystem, Ecosystem Risks), Phase 8 Market (Adoption Metrics), Phase 9 Behavioral (Strategic Trade-offs)
Confidence: HIGH

Insight 9: Revenue diversification via multiple fee streams (gas, order matching, IBC, EVM priority fees, base fee burn) semua masuk community pool kecuali EVM base fee burned — tapi Sei Labs revenue model tidak transparan
Explanation: 6 fee types: transaction fees (gas), order matching fees, IBC packet fees, EVM priority fees, EVM base fee burn (Sei v2), staking commission (validator-level). Semua protocol fees → community pool via Cosmos SDK distribution module. $50M ecosystem fund dari treasury. Sei Labs ops funding post-VC tidak di-disclose【Phase 5 — Revenue Model: 6 fee types】【Phase 4 — Core Components: Order Matching Engine, Sei v2 EVM Priority Fees】【Phase 3 — EV-004, EV-007, EV-008, EV-020】【Phase 9 — Financial Decision Pattern: Revenue Diversification, Treasury Opacity】
Evidence: Sei docs fees; whitepaper tokenomics; community pool address on-chain; ecosystem fund blog; no audited financials for Sei Labs Inc.
Supporting Dataset: Phase 3 History (EV-004, EV-007, EV-008, EV-020), Phase 4 Technology (Core Components), Phase 5 Financial (Revenue Model, Treasury, Ecosystem Fund), Phase 6 Token (Inflation/Deflation), Phase 9 Behavioral (Financial Decision Pattern, Weaknesses)
Confidence: HIGH

Insight 10: Ecosystem app launch cluster (DragonSwap, Silo, Yei, Leviathan, Pallet dalam 3 bulan post-mainnet) menunjukkan infrastructure-readiness unlocking builder confidence
Explanation: Mainnet Aug 15 2023 → bridges/oracles/wallets ready Aug → 5 flagship apps launch Sep-Nov 2023. Pattern diulang expected untuk Sei v2 EVM apps post-Aug 2024. Infrastructure completeness (bridges, oracles, wallets, explorers, indexers) live sejak early sebagai moat【Phase 3 — EV-004, EV-007/008/009, EV-010 to EV-014】【Phase 7 — Applications: 10 core apps】【Phase 9 — Recurring Behavioral Pattern: Ecosystem App Launch dalam Cluster Post-Infrastructure Ready】【Phase 8 — Adoption Metrics: TVL ~$380M, Daily transactions 200K-500K】
Evidence: Historical timeline shows cluster; DefiLlama TVL growth; Seitrace transaction counts; ecosystem page listings
Supporting Dataset: Phase 3 History (EV-004, EV-007, EV-008, EV-009, EV-010, EV-011, EV-012, EV-013, EV-014), Phase 7 Ecosystem (Applications, Infrastructure Providers), Phase 8 Market (Adoption Metrics), Phase 9 Behavioral (Recurring Behavioral Pattern)
Confidence: HIGH

## Strategic Principles

Principle 1: Modular architecture dengan custom components hanya untuk critical performance path
Explanation: Gunakan battle-tested frameworks (Cosmos SDK, CometBFT, IBC-Go, Wasmer) untuk non-critical modules; invest custom engineering hanya pada components yang langsung menentukan competitive advantage: parallel execution, order matching, storage layer, VM embedding【Phase 4 — Architecture, Core Components】【Phase 9 — Technical Decision Pattern: Modular Architecture dengan Custom Components】
Evidence: Sei chain dependencies vs custom modules; whitepaper technical design; SeiDB blog; Sei v2 Geth embedding choice
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 2: Dual/redundant infrastructure untuk semua critical dependencies (bridges, oracles, wallets, VMs)
Explanation: Tidak bergantung pada single provider untuk fungsi kritis; integrasikan minimal dua opsi dengan trust assumptions berbeda untuk redundancy dan coverage maksimal【Phase 3 — EV-008, EV-009, EV-015, EV-018】【Phase 7 — Major Integrations, Wallet Ecosystem, Infrastructure Providers】【Phase 9 — Recurring Behavioral Pattern: Dual/Redundant Approach】
Evidence: Wormhole + Axelar both activated same month; Pyth + Chainlink both; Keplr/Leap/Compass + MetaMask; CosmWasm + EVM
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Principle 3: Security-first dengan preemptive multiple audits dan extended testnet sebelum setiap major launch
Explanation: Minimal 2-3 audit firms per major release; testnet duration 4-17 bulan; findings addressed pre-launch; zero critical mainnet exploits achieved【Phase 4 — Audit History: 6 core audits】【Phase 3 — EV-002 (17mo testnet), EV-019 (4mo Sei v2 testnet)】【Phase 9 — Risk Response Pattern: Preemptive Audits】
Evidence: Informal Systems, Halborn, Veridise, Trail of Bits, Oak Security, Zellic audits; testnet timelines; no mainnet exploits/hacks
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 4: Progressive decentralization via time-based token vesting + on-chain governance dari genesis
Explanation: Team/investor tokens locked dengan cliff synchronization; governance active day-1; no emergency centralization controls (no pause, no admin keys); voting power shifts secara alami seiring vesting【Phase 6 — Vesting Schedule: Team/Investors 12mo cliff】【Phase 3 — EV-004】【Phase 7 — Governance Ecosystem: DAO active】【Phase 9 — Risk Response Pattern: Gradual Decentralization】
Evidence: Whitepaper vesting; TGE date; governance proposals from genesis; no pause function in native token
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Principle 5: Developer experience parity — support existing tooling untuk both VM ecosystems tanpa memaksa migrasi
Explanation: Full Hardhat/Foundry/MetaMask support untuk EVM developers; full CosmWasm CLI/Ignite/Keplr support untuk Cosmos developers; SDKs di JS/TS/Python; dual tooling = dual developer funnel【Phase 7 — Developer Ecosystem: SDKs, APIs, Toolchains】【Phase 3 — EV-018, EV-019】【Phase 8 — Narrative: EVM Compatibility, Developer Count metric】【Phase 9 — Ecosystem Decision Pattern: Developer Tooling Parity】
Evidence: Sei v2 testnet validated Hardhat/Foundry; MetaMask support announcement; CosmWasm docs unchanged; multi-language SDKs
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Principle 6: Narrative-aware technical roadmap — respond ke competitive landscape dengan technical differentiation yang addressable market besar
Explanation: Sei v2 (EVM via Geth) dan SeiDB announcements 2024 langsung merespons Monad/Berachain/MegaETH competition; EVM compatibility menjadi narrative utama 2024; parallel execution + native order matching tetap core moat【Phase 3 — EV-016, EV-017】【Phase 8 — Narrative Position: 3 Main Narratives】【Phase 8 — Competitor Landscape: 8 direct competitors】【Phase 9 — Evolution Pattern: Shift ke EVM Compatibility, Strategic Trade-offs: Complexity vs Adoption】
Evidence: Sei v2 blog April 2024 post-Monad/Berachain announcements; narrative shift documented; competitor analysis
Supporting Dataset: Phase 3 History, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

## Success Factors

Factor 1: Technical moat yang genuine — parallel execution + native order matching + SeiDB = differentiated infrastructure untuk trading use case
Explanation: Bukan marketing fluff; arsitektur benar-benar berbeda dari Solana (monolithic SVM), Aptos/Sui (Move), Monad (EVM-only parallel), Hyperliquid (app-chain). Dual VM + shared storage (SeiDB) + native order matching di consensus layer = unique combination【Phase 4 — Core Components: Parallel Execution Engine, Order Matching Engine, SeiDB】【Phase 8 — Competitor Landscape: 8 competitors dengan differentiators】【Phase 9 — Behavioral Summary: Technical Moat】
Evidence: Whitepaper technical architecture; competitor comparison; SeiDB design; order matching engine native module
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 2: Capital efficiency — $35M VC → mainnet + $50M ecosystem fund dari treasury → no down round, no token sale dilution
Explanation: Series A+B $35M memadai untuk core development hingga mainnet; ecosystem fund sourced dari protocol treasury (Foundation 10% + Community 48%), bukan fresh raise; token price appreciation memperbesar fund USD value【Phase 5 — Funding History: Series A $5M, Series B $30M】【Phase 5 — Ecosystem Fund: $50M dari treasury】【Phase 6 — Distribution: Foundation 10%, Community 48%】【Phase 9 — Financial Decision Pattern: Ecosystem Fund dari Protocol Treasury】
Evidence: Funding announcements; whitepaper tokenomics; ecosystem fund blog; no subsequent funding rounds announced
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Factor 3: Exchange dan market maker relationships kuat — Binance TGE listing + investor MMs (Wintermute, Jane Street, Flow Traders, GSR) → deep liquidity day-1
Explanation: Binance listing at TGE (strategic investor); investor list termasuk major market makers yang provide liquidity; perp volume 5-10x spot volume menunjukkan trader adoption【Phase 3 — EV-005】【Phase 5 — Funding History: investor list includes MMs】【Phase 7 — Exchange Ecosystem: 11 CEX】【Phase 8 — Liquidity: perp volume $500M-1.5B vs spot $100-300M】【Phase 9 — Ecosystem Decision Pattern: Exchange Listing Strategy】
Evidence: Binance spotlight announcement; Series A investor list; exchange listing timeline; volume metrics
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 4: Infrastructure completeness at launch — bridges, oracles, wallets, explorers, indexers all live early → builder ready
Explanation: IBC, Wormhole, Axelar, Pyth, Chainlink, Keplr, Leap, Compass, Seitrace all active by mainnet or within weeks; eliminates "chicken-egg" problem untuk builders【Phase 3 — EV-007, EV-008, EV-009, EV-015】【Phase 7 — Major Integrations: 10 integrations, Infrastructure Providers: 11 providers】【Phase 9 — Recurring Behavioral Pattern: Ecosystem App Launch Cluster Post-Infrastructure Ready】
Evidence: Historical timeline shows infra before apps; ecosystem apps launched within 3 months
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 5: Founder domain expertise — Jayendra Jog (ex-Robinhood HFT) + Dan Edlebeck (ex-Terra/Chorus One) → trading-optimized architecture dari first principles
Explanation: Founder background langsung inform arsitektur: parallel execution untuk HFT workloads, order matching engine di consensus layer, Cosmos SDK base untuk sovereignty【Phase 2 — Jayendra Jog, Dan Edlebeck】【Phase 1 — Founders】【Phase 3 — EV-001】【Phase 9 — Strategic Objectives: Trading-optimized L1】
Evidence: LinkedIn/Twitter profiles; whitepaper motivation; technical design choices
Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 3 History, Phase 9 Behavioral
Confidence: HIGH

## Failure Factors

Factor 1: Foundation/treasury opacity — no legal entity confirmed, no addresses labeled, no dashboard → trust deficit
Explanation: Whitepaper mention "Foundation 10%" tapi tidak ada filing publik (Cayman/Swiss/Delaware?); multi-sig signers tidak diketahui; custody arrangement tidak transparan; ecosystem fund $50M deployment tidak ada public dashboard【Phase 2 — Entity: no Foundation identified】【Phase 5 — Treasury: not disclosed】【Phase 6 — Distribution: Foundation 10%】【Phase 7 — Governance: Foundation assumed】【Phase 9 — Weaknesses: Foundation/Treasury Opacity, Open Threads: Foundation legal entity】
Evidence: Phase 2 entity list has no Foundation; Phase 5 treasury section "not disclosed"; Phase 7 governance "assumed entity"; Phase 9 open threads list multiple Foundation questions
Supporting Dataset: Phase 2 Entity, Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 2: Dual VM complexity — Geth fork maintenance, cross-VM reentrancy risk, Wasmer determinism, SeiDB maturity unproven at scale
Explanation: Maintain Geth fork untuk consensus-critical changes; cross-VM calls (CosmWasm ↔ EVM) via precompiles adds ~1-2 block latency + reentrancy risk; Wasmer determinism across x86_64/ARM64; SeiDB baru live since Aug 2024【Phase 4 — Known Limitations: Cross-VM Latency, Geth Embedding Dependency, SeiDB Maturity, Wasmer Determinism】【Phase 9 — Strategic Trade-offs: Complexity vs Adoption, Weaknesses: Dual VM Complexity】
Evidence: Sei v2 docs precompiles; Known Limitations section; Trail of Bits audit scope; Oak Security audit SeiDB
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Factor 3: Bridge/oracle external risk — 100% bridged asset value depends on Wormhole/Axelar/Pyth/Chainlink security
Explanation: Bridged SEI di Ethereum/Solana/EVM L2 secured by external validator/guardian sets, bukan Sei consensus; bridge hack = bridged asset value loss di Sei; oracle manipulation affects lending/perps/DEX pricing【Phase 4 — External Dependencies: Wormhole, Axelar, Pyth, Chainlink】【Phase 7 — Ecosystem Risks: Bridge Dependency HIGH, Oracle Dependency HIGH】【Phase 9 — Strategic Trade-offs: Bridge Security vs Composability, Weaknesses: Bridge/Oracle External Risk】
Evidence: Wormhole Guardian 19 validators; Axelar PoS validators; Pyth publisher-signed; Chainlink DONs; all external to Sei consensus
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 4: Validator centralization — Nakamoto coefficient ~8-12, entity concentration unknown, cloud dependency high
Explanation: Top 100 validators by stake; entity-level mapping tidak on-chain (same operator multiple validators); majority validators di AWS/GCP/Azure; delegator apathy (override rate rendah)【Phase 7 — Governance: Validator Set 100】【Phase 8 — Nakamoto Coefficient estimated 8-12】【Phase 7 — Ecosystem Risks: Validator Centralization, Cloud Infrastructure Dependency】【Phase 9 — Strategic Trade-offs: Decentralization vs Throughput, Weaknesses: Validator Centralization】
Evidence: Seitrace validators; staking participation 65-70%; community estimates; cloud provider docs
Supporting Dataset: Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 5: No sustainable revenue model published — protocol fees → community pool, but Sei Labs ops funding unclear post-VC; token price dependency high
Explanation: Community pool collects fees tapi Sei Labs revenue share tidak di-disclose; $35M VC runway finite; ecosystem fund $50M fixed dalam SEI → USD value volatil; no audited financials【Phase 5 — Revenue Model, Treasury, Financial Dependencies】【Phase 9 — Weaknesses: No Sustainable Revenue Model, Financial Risk: Funding Dependency】
Evidence: Cosmos SDK distribution module; community pool address; ecosystem fund blog; no Sei Labs financial reports
Supporting Dataset: Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Factor 6: Regulatory overhang — Delaware corporation + token = SEC enforcement risk; no public legal opinion
Explanation: Sei Labs Inc. Delaware corp; SEI token classification (security vs commodity) tidak formally determined; Howey test exposure; no SEC correspondence disclosed【Phase 2 — Sei Labs Inc., Delaware Division of Corporations】【Phase 5 — Financial Risk: Legal Financial Risk】【Phase 9 — Weaknesses: Regulatory Overhang, Open Threads: Regulatory engagement status】
Evidence: OpenCorporates Delaware filing; SEC framework digital assets; no public legal memo
Supporting Dataset: Phase 2 Entity, Phase 5 Financial, Phase 9 Behavioral
Confidence: MEDIUM

## Decision Framework

Step 1: Observe — Founder vision + competitive landscape analysis → identify technical differentiation opportunity
Explanation: Jayendra/Dan background (HFT + Cosmos) + market gap (no trading-optimized L1 dengan parallel execution) → whitepaper specification【Phase 1 — Vision, Mission, Category】【Phase 2 — Jayendra Jog, Dan Edlebeck】【Phase 3 — EV-001】【Phase 9 — Strategic Objectives, Decision Timeline: Founding】
Evidence: Whitepaper motivation; founder backgrounds; Series A/B funding secured pre-testnet
Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 3 History, Phase 9 Behavioral
Confidence: HIGH

Step 2: Evaluate — Extended testnet (17 bulan) dengan incentivized validators + multiple audits → validate architecture pre-mainnet
Explanation: Atlantic-1 testnet Mar 2022 → Pacific-1 mainnet Aug 2023; 6 core audits pre-respective launches; validator set matured; bug fixes incorporated【Phase 3 — EV-002, EV-003】【Phase 4 — Audit History】【Phase 9 — Technical Decision Pattern: Upgrade Bertahap, Risk Response: Preemptive Audits】
Evidence: Testnet timeline; audit reports; v0.1.0 release; mainnet stability post-launch
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Step 3: Fund — Equity + token bundled (Series A/B $35M) → no public sale, Binance TGE listing, market maker investors provide liquidity
Explanation: Multicoin lead Series A, Jump Crypto lead Series B; investor list includes VCs + MMs; token allocation 22% untuk investors dengan 12mo cliff; Binance listing at TGE【Phase 5 — Funding History】【Phase 3 — EV-005, EV-006】【Phase 9 — Financial Decision Pattern: Equity + Token Bundled】
Evidence: Funding announcements; Binance spotlight; whitepaper tokenomics; no ICO/Launchpool
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Step 4: Develop — Modular architecture: standard frameworks untuk non-critical, custom components untuk critical path (parallel execution, order matching, SeiDB, Geth embedding)
Explanation: Cosmos SDK/CometBFT/IBC-Go/Wasmer untuk standard modules; custom parallel execution engine, order matching module, SeiDB storage, Geth embedding untuk EVM【Phase 4 — Architecture, Core Components】【Phase 9 — Technical Decision Pattern: Modular Architecture dengan Custom Components】
Evidence: Go.mod dependencies; whitepaper custom components; SeiDB blog; Sei v2 Geth embedding
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Step 5: Launch — Infrastructure-first: bridges, oracles, wallets, explorers live sebelum/saat mainnet → ecosystem app cluster dalam 3 bulan
Explanation: IBC, Wormhole, Axelar, Pyth, Chainlink, Keplr, Leap, Compass, Seitrace all active Aug 2023; DragonSwap, Silo, Yei, Leviathan, Pallet launch Sep-Nov 2023【Phase 3 — EV-004, EV-007, EV-008, EV-009, EV-010 to EV-014】【Phase 9 — Recurring Behavioral Pattern: Infrastructure Ready → App Cluster】
Evidence: Historical timeline; ecosystem app launch dates; infra integration dates
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Step 6: Govern — On-chain governance dari genesis + time-based decentralization (12mo cliff team/investors) → progressive power shift tanpa emergency controls
Explanation: Cosmos SDK Governance Module active day-1; voting power = staked SEI; team/investor cliff Aug 2024; no pause function, no admin keys【Phase 6 — Governance, Vesting Schedule】【Phase 3 — EV-004】【Phase 7 — Governance Ecosystem: DAO, Validator Set】【Phase 9 — Risk Response: Gradual Decentralization】
Evidence: Whitepaper governance; TGE date; governance proposals on Seitrace; vesting schedule
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Step 7: Iterate — Major upgrade cycle ~12 bulan: spec publication → testnet → validator signaling → governance proposal → mainnet upgrade (Sei v2: Apr announcement → Jul testnet → Aug mainnet)
Explanation: Structured upgrade coordination; public technical specs (Sei v2 blog, SeiDB blog); 4+ bulan lead time; validator readiness tracking; governance proposal untuk upgrade block【Phase 3 — EV-016, EV-017, EV-019, EV-020】【Phase 4 — Technical Upgrade History】【Phase 9 — Recurring Behavioral Pattern: Major Upgrade Setiap ~12 Bulan, Risk Response: Technical Upgrade Coordination】
Evidence: Sei v2 timeline; SeiDB timeline; governance upgrade proposals; validator coordination
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

## Reusable Playbook

Playbook 1: Cara membangun L1 dengan technical moat genuine — fokus custom engineering hanya pada critical path, gunakan standard frameworks untuk sisanya
Explanation: Identifikasi 1-2 core differentiators (parallel execution + order matching untuk Sei); build custom components hanya untuk itu; gunakan Cosmos SDK/CometBFT/IBC-Go/Wasmer untuk standard modules; hindari NIH syndrome di non-critical path【Phase 4 — Architecture, Core Components】【Phase 9 — Technical Decision Pattern: Modular Architecture dengan Custom Components, Behavioral Summary: Technical Moat】
Evidence: Sei chain architecture; competitor comparison showing unique combination
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Playbook 2: Cara fundraising tanpa public token sale — equity + token bundled di Series A/B, tier-1 CEX listing at TGE, market maker investors
Explanation: Raise equity rounds dengan token allocation sebagai sweetener; pilih investors yang include market makers (Wintermute, Jane Street, Flow Traders); negotiate Binance/Coinbase listing at TGE; avoid ICO/Launchpool regulatory risk【Phase 5 — Funding History, Fundraising Mechanism, Token Sale】【Phase 3 — EV-001, EV-005, EV-006】【Phase 9 — Financial Decision Pattern: Equity + Token Bundled, Ecosystem Decision Pattern: Exchange Listing Strategy】
Evidence: Sei funding structure; Binance TGE listing; investor list; no public sale
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Playbook 3: Cara progressive decentralization — 12-month cliff synchronized (team + investors), on-chain governance dari genesis, no emergency centralization controls
Explanation: Set team/investor vesting cliff sama (12 bulan post-TGE); activate governance module at genesis; tidak ada pause function/admin keys pada native token; biarkan voting power shift alami seiring unlock【Phase 6 — Vesting Schedule, Governance】【Phase 3 — EV-004】【Phase 7 — Governance Ecosystem】【Phase 9 — Risk Response: Gradual Decentralization】
Evidence: Whitepaper vesting; governance active from genesis; no pause mechanism; cliff passed Aug 2024 smoothly
Supporting Dataset: Phase 3 History, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Playbook 4: Cara ecosystem bootstrap — infrastructure completeness first (bridges, oracles, wallets, explorers), lalu coordinated app launch cluster
Explanation: Launch/mainnet dengan IBC, 2+ bridges, 2+ oracles, 3+ wallets, explorer, indexers sudah live; announce ecosystem fund; flagship apps (DEX, lending, perp, yield, NFT) launch dalam 3 bulan bersamaan【Phase 3 — EV-004, EV-007, EV-008, EV-009, EV-010 to EV-014】【Phase 7 — Major Integrations, Applications, Grant Program】【Phase 9 — Recurring Behavioral Pattern: Infrastructure Ready → App Cluster, Ecosystem Decision Pattern: Dual Bridge/Oracle/Wallet】
Evidence: Historical timeline; 5 apps in 3 months; $50M ecosystem fund announced Q4 2023
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Playbook 5: Cara major upgrade coordination — public spec publication → extended testnet (4+ bulan) → multiple audits → validator signaling → governance proposal → scheduled upgrade block
Explanation: Sei v2 pattern: Apr announcement dengan technical specs → Jul public testnet → Trail of Bits/Oak Security/Zellic audits → validator upgrade readiness tracking → governance proposal → Aug scheduled upgrade block【Phase 3 — EV-016, EV-017, EV-019, EV-020】【Phase 4 — Audit History, Technical Upgrade History】【Phase 9 — Risk Response: Technical Upgrade Coordination, Recurring Pattern: Major Upgrade ~12mo】
Evidence: Sei v2 timeline; audit firms; testnet duration; governance upgrade process
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Playbook 6: Cara dual VM strategy — embed Geth (bukan Ethermint) untuk EVM compatibility, shared storage layer (SeiDB), precompile contracts untuk cross-VM native module access
Explanation: Jangan gunakan Ethermint (EVM sebagai module); embed Geth langsung ke consensus layer; build custom storage (SeiDB) yang serve both VMs; write native Go precompiles untuk bank/staking/IBC/tokenfactory access dari EVM【Phase 4 — Execution Environment, Sei v2 EVM Layer, SeiDB, Precompile Contracts】【Phase 3 — EV-016, EV-020】【Phase 9 — Technical Decision Pattern: Dual VM Strategy, Strategic Trade-offs: Complexity vs Adoption】
Evidence: Sei v2 blog "embedded Geth not Ethermint"; SeiDB shared storage; precompiles list; Trail of Bits audit scope
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Playbook 7: Cara redundancy infrastructure — dual bridges (Wormhole + Axelar), dual oracles (Pyth + Chainlink), dual wallet segments (Cosmos native + EVM), dual VMs
Explanation: Untuk setiap critical dependency category, integrasikan minimal 2 provider dengan trust assumptions berbeda; dokumentasikan trade-off; biarkan developer/user choose; monitor both continuously【Phase 3 — EV-008, EV-009, EV-015, EV-018】【Phase 7 — Major Integrations, Wallet Ecosystem, Infrastructure Providers, Ecosystem Risks】【Phase 9 — Recurring Behavioral Pattern: Dual/Redundant Approach, Strategic Trade-offs: Bridge Security vs Composability】
Evidence: Both bridges/oracles active same month; both wallet segments; both VMs; risk documentation
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

## Anti-patterns

Anti-pattern 1: Over-centralization di Foundation/treasury tanpa transparency — "Foundation 10%" di whitepaper tapi no legal entity, no multisig addresses, no dashboard
Explanation: Mengklaim decentralization tapi treasury custody opaque; community tidak bisa audit; single point of failure jika multisig compromised; regulatorily ambiguous (US person control?)【Phase 2 — Entity: no Foundation】【Phase 5 — Treasury: not disclosed】【Phase 6 — Distribution: Foundation 10%】【Phase 7 — Governance: Foundation assumed】【Phase 9 — Weaknesses: Foundation/Treasury Opacity, Open Threads: Foundation legal entity】
Evidence: Phase 2 entity list lacks Foundation; Phase 5 treasury undisclosed; Phase 7 governance "assumed"; Phase 9 open threads multiple Foundation questions
Supporting Dataset: Phase 2 Entity, Phase 5 Financial, Phase 6 Token, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Anti-pattern 2: Premature scaling tanpa battle-testing custom storage/VM components — SeiDB live Aug 2024, Geth embedding live Aug 2024, cross-VM calls unproven at scale
Explanation: Custom components (SeiDB, Geth embedding, precompiles) langsung mainnet tanpa prior production track record; audit helps tapi real-world adversarial conditions berbeda; long-term correctness unknown【Phase 4 — Known Limitations: SeiDB Maturity, Geth Embedding Dependency, Cross-VM Latency】【Phase 3 — EV-020】【Phase 9 — Weaknesses: Dual VM Complexity, Open Threads: SeiDB fast sync trust model, Cross-VM reentrancy】
Evidence: SeiDB blog "live since Sei v2"; Geth embedding first production use; cross-VM calls newly enabled
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: MEDIUM

Anti-pattern 3: Poor treasury management transparency — protocol fees → community pool visible, tapi Sei Labs ops funding, Foundation spending, ecosystem fund deployment tidak tracked publicly
Explanation: Revenue diversification baik (6 fee streams) tapi money flow opacity: community pool address known tapi spending proposals unstructured; ecosystem fund $50M no dashboard; Sei Labs revenue model undisclosed【Phase 5 — Revenue Model, Treasury, Ecosystem Fund】【Phase 7 — Grant Program】【Phase 9 — Weaknesses: No Sustainable Revenue Model, Financial Risk: Funding Dependency, Open Threads: Ecosystem Fund deployment transparency】
Evidence: Community pool on-chain; governance proposals exist but no analytics dashboard; ecosystem fund blog only; no Sei Labs financials
Supporting Dataset: Phase 5 Financial, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Anti-pattern 4: Single consensus engine dependency tanpa fallback — 100% CometBFT/Tendermint; critical bug di CometBFT = chain halt di Sei
Explanation: Tidak ada alternative consensus implementation; validator set 100 fixed; CometBFT upgrade coordination risk (Cosmos SDK upgrades); cloud provider concentration amplifies risk【Phase 4 — Architecture: Tendermint Consensus Engine】【Phase 7 — External Dependencies: Tendermint/CometBFT, Cloud Providers】【Phase 7 — Ecosystem Risks: Single Consensus Engine Dependency, Cosmos SDK Upgrade Coordination】【Phase 9 — Weaknesses: Validator Centralization, Cloud Dependency】
Evidence: Go.mod shows CometBFT dependency; validator set 100; Cosmos SDK upgrade history; cloud provider docs
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Anti-pattern 5: Token unlock cliff synchronization tanpa explicit communication/management — Team + Investors 12mo cliff Aug 2024 bersamaan; narrative "decentralization milestone" tapi sell pressure real
Explanation: Cliff synchronization menciptakan "unlock wall"; market maker investors (Wintermute, Jane Street) bisa absorb tapi retail FUD risk tinggi; no unlock dashboard, no explicit communication strategy【Phase 6 — Vesting Schedule: Team/Investors 12mo cliff】【Phase 3 — EV-004】【Phase 9 — Recurring Behavioral Pattern: Token Unlock Events Dikotomi Narasi, Open Threads: Token unlock schedule tracking】
Evidence: Whitepaper vesting; TGE date; investor list includes MMs; no unlock dashboard; Aug 2024 cliff passed
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral
Confidence: MEDIUM

Anti-pattern 6: Regulatory ambiguity tidak di-address proaktif — Delaware corp + token = SEC risk; no public legal opinion, no Howey analysis disclosure, no regulatory engagement transparency
Explanation: US entity mengeluarkan token dengan utility (gas, staking, governance) tapi investor expectation of profit dari VC rounds; Howey test exposure; competitor L1s facing enforcement; Sei silent【Phase 2 — Sei Labs Inc., Delaware Division of Corporations】【Phase 5 — Financial Risk: Legal Financial Risk】【Phase 9 — Weaknesses: Regulatory Overhang, Open Threads: Regulatory engagement status】
Evidence: Delaware filing; SEC framework; no public legal memo; industry enforcement actions
Supporting Dataset: Phase 2 Entity, Phase 5 Financial, Phase 9 Behavioral
Confidence: MEDIUM

## Lessons Learned

1. Genuine technical differentiation (parallel execution + native order matching) menciptakan moat yang sulit dikopi, tapi memerlukan custom engineering investment yang signifikan dan audit rigor.
2. Bundling equity + token di VC rounds menghindari regulatory risk public sale, tapi menciptakan investor token concentration yang perlu dikelola via synchronized vesting cliffs.
3. Infrastructure completeness at launch (bridges, oracles, wallets, explorers) adalah prerequisite untuk ecosystem app cluster — jangan launch mainnet tanpa infra siap.
4. Dual/redundant infrastructure strategy (2 bridges, 2 oracles, 2 wallet segments, 2 VMs) mengurangi single-point-of-failure tapi menambah operational complexity dan audit surface.
5. Progressive decentralization via time-based vesting + on-chain governance dari genesis bekerja untuk smooth power shift, tapi Foundation/treasury opacity menciptakan trust deficit baru.
6. Revenue diversification via multiple fee streams (gas, order matching, IBC, EVM fees) baik untuk sustainability, tapi money flow transparency (community pool → spending → Sei Labs ops) harus di-address.
7. Major upgrade coordination via public specs → extended testnet → multi-audit → governance → scheduled upgrade adalah pattern yang repeatable dan low-risk.
8. Founder domain expertise (HFT + Cosmos) langsung translate ke architectural choices yang differentiated — technical vision harus rooted di real problem experience.
9. Exchange listing strategy: Tier-1 CEX at TGE + market maker investors = deep liquidity day-1; perp volume dominance menunjukkan product-market fit untuk trading use case.
10. Regulatory risk untuk US-incorporated L1 dengan token adalah existential — proactive legal opinion dan engagement transparency diperlukan, bukan diabaikan.

## Knowledge Summary

Strategic Principles:
1. Modular architecture dengan custom components hanya untuk critical performance path
2. Dual/redundant infrastructure untuk semua critical dependencies
3. Security-first dengan preemptive multiple audits dan extended testnet
4. Progressive decentralization via time-based token vesting + on-chain governance dari genesis
5. Developer experience parity — support existing tooling untuk both VM ecosystems
6. Narrative-aware technical roadmap — respond ke competitive landscape

Success Factors:
1. Technical moat genuine: parallel execution + native order matching + SeiDB
2. Capital efficiency: $35M VC → mainnet + $50M ecosystem fund dari treasury
3. Exchange/Market maker relationships: Binance TGE + investor MMs
4. Infrastructure completeness at launch: bridges, oracles, wallets, explorers all live
5. Founder domain expertise: HFT + Cosmos background

Failure Factors:
1. Foundation/treasury opacity: no legal entity, no addresses, no dashboard
2. Dual VM complexity: Geth fork, cross-VM reentrancy, Wasmer determinism, SeiDB maturity
3. Bridge/oracle external risk: 100% bridged asset value depends on external security
4. Validator centralization: Nakamoto coefficient ~8-12, cloud dependency high
5. No sustainable revenue model published: Sei Labs ops funding unclear
6. Regulatory overhang: Delaware corp + token = SEC risk

Decision Framework:
Observe (founder vision + competitive gap) → Evaluate (17mo testnet + audits) → Fund (equity+token bundled, Binance TGE) → Develop (modular: standard frameworks + custom critical path) → Launch (infra-first → app cluster) → Govern (on-chain + time-based decentralization) → Iterate (12mo upgrade cycle: spec → testnet → audit → governance → upgrade)

Reusable Playbook:
1. Build L1 dengan technical moat: custom critical path only
2. Fundraise tanpa public sale: equity+token bundled, tier-1 CEX TGE, MM investors
3. Progressive decentralization: synchronized cliff, governance genesis, no emergency controls
4. Ecosystem bootstrap: infra completeness first → coordinated app cluster
5. Major upgrade coordination: public spec → 4mo+ testnet → multi-audit → governance → scheduled
6. Dual VM strategy: embed Geth, shared storage, native precompiles
7. Redundancy infrastructure: dual everything for critical deps

Anti-patterns:
1. Foundation/treasury opacity tanpa transparency
2. Premature scaling custom components tanpa battle-testing
3. Poor treasury management transparency
4. Single consensus engine dependency tanpa fallback
5. Token unlock cliff sync tanpa communication management
6. Regulatory ambiguity tidak di-address proaktif

## Open Questions
- [foundation] Exact core team headcount not officially published — only LinkedIn estimates available
- [foundation] Whether Sei Labs has additional legal entities outside Delaware (e.g., foundation in Cayman/Switzerland) — not confirmed in public filings
- [foundation] Complete list of all chain deployments for SEI token (wormhole/axelar bridged versions) — may have newer deployments post-knowledge cutoff
- [foundation] TGE token distribution breakdown (team, investors, community, foundation percentages) — whitepaper references but exact current vesting schedules need on-chain verification
- [foundation] Current status of Sei v2 upgrade rollout (fully live vs. phased) — announced but completion status needs verification
- [entity] Exact core team headcount not officially published — only LinkedIn estimates available
- [entity] Whether Sei Labs has additional legal entities outside Delaware (e.g., foundation in Cayman/Switzerland) — not confirmed in public filings
- [entity] Complete list of all chain deployments for SEI token (wormhole/axelar bridged versions) — may have newer deployments post-knowledge cutoff
- [entity] TGE token distribution breakdown (team, investors, community, foundation percentages) — whitepaper references but exact current vesting schedules need on-chain verification
- [entity] Current status of Sei v2 upgrade rollout (fully live vs. phased) — announced but completion status needs verification
- [entity] Investor entities (VCs, strategic investors) not identified in Phase 1 — need funding round announcements and cap table disclosures
- [entity] Security auditor firms for Sei chain, SeiDB, Sei v2 smart contracts — not listed in Phase 1 sources
- [entity] DAO/governance entity (if any) for Sei protocol governance — not identified in Phase 1
- [entity] Market maker entities providing liquidity for SEI token — not identified in Phase 1
- [entity] Enterprise partners or institutional users beyond ecosystem apps — not identified in Phase 1
- [history] Tanggal pasti pengumuman Sei v2 dan SeiDB: blog Sei tertulis "April 23, 2024" tapi perlu verifikasi URL exact publish date
- [history] Tanggal exact luncuran testnet Sei v2 (Pacific-2/devnet) — docs.sei.io merujuk "July 2024" tapi tanggal spesifik tidak tercatat di sumber Phase 1-2
- [history] Tanggal exact upgrade mainnet ke Sei v2 — diumumkan "August 2024" tapi apakah 2024-08-15 (tahun ke-1 mainnet) atau tanggal lain perlu konfirmasi on-chain governance proposal
- [history] Funding rounds (Series A, Series B, strategic rounds) — tidak ada data di Phase 1-2; perlu cari announcement Sei Labs / investor press release
- [history] Security audit reports untuk Sei chain, SeiDB, Sei v2 smart contracts — tidak teridentifikasi di Phase 1-2; perlu cari Halborn, Informal Systems, atau auditor lain
- [history] Governance proposals on-chain (parameter changes, upgrade signaling, community spend) — tidak tercatat; perlu query governance module Sei mainnet
- [history] DAO/Foundation entity terpisah dari Sei Labs Inc. — tidak ditemukan di Phase 1-2; apakah ada "Sei Foundation" di Cayman/Switzerland seperti pola Cosmos lain
- [history] Tokenomics detail: persentase TGE, vesting schedule team/investor/community, fee switch status — whitepaper mereferensikan tapi angka exact perlu cross-check on-chain dan blog resmi
- [history] Complete list chain deployments SEI bridged (wormhole/axelar) post-knowledge cutoff — mungkin ada chain baru (Linea, Scroll, Mantle, dll)
- [technology] Complete audit reports for all 6 core audits — some reports not publicly linked in official channels; need to verify publication status and access full findings
- [technology] SeiDB fast sync security model — documentation mentions "trusted checkpoint" but exact trust assumptions and verification process not fully specified in public docs
- [technology] CosmWasm 2.0 upgrade timeline — governance proposal not yet on-chain as of knowledge cutoff; exact activation block unknown
- [technology] IBC-Go v8 / ICA upgrade status — planned but no governance proposal visible; dependency on Cosmos SDK upgrade path
- [technology] Formal verification of parallel execution engine — Veridise audit referenced but full formal spec not published; property definitions (safety, liveness under contention) not public
- [technology] SeiDB benchmark data — throughput, latency, state size comparisons vs. IAVDB under various workloads not published in reproducible format
- [technology] EVM precompile gas schedule governance process — exact parameter change mechanism and timelock not documented in developer docs
- [technology] Cross-VM reentrancy protection — CosmWasm → EVM → CosmWasm call frames; reentrancy guard implementation details not in public specs
- [technology] Validator set decentralization metrics — real-time stake distribution, Nakamoto coefficient, entity concentration not published officially
- [technology] Bridge risk framework — Sei's official stance on bridged asset risk, emergency pause mechanisms, or bridge-specific circuit breakers not documented
- [technology] State expiry / rent roadmap — no EIP-4444 equivalent or state rent proposal visible in governance forum
- [technology] Maximum validator count governance parameter — currently 100 but change process and rationale not in technical docs
- [technology] Transaction fee market design — base fee, priority fee, EIP-1559 equivalence for Sei v2 EVM not fully specified
- [technology] MEV protection at consensus layer — order matching engine batching provides some protection but proposer-based MEV (EVM) not addressed in technical docs
- [financial] Exact token allocation percentages untuk investor Series A+B (equity + token deal) — whitepaper merujuk "investor allocation" tapi persentase exact dan vesting schedule perlu cross-check on-chain governance proposal atau blog resmi tokenomics detail
- [financial] Sei Foundation legal entity — apakah terpisah dari Sei Labs Inc. (Cayman Foundation / Swiss Verein seperti pola Cosmos lain) — tidak dikonfirmasi di public filings; treasury custody mengasumsikan Foundation ada tapi entitas hukumnya tidak terverifikasi
- [financial] Treasury wallet addresses — tidak dipublikasikan dengan label resmi; community pool address tersedia on-chain (Cosmos SDK distribution module) tapi tidak dibedakan dari treasury Sei Labs / Foundation
- [financial] Revenue sharing model — apakah Sei Labs menerima cut dari community pool fees, atau fully funded by Series A+B + ecosystem fund — tidak di-disclose resmi
- [financial] Ecosystem Fund deployment status — $50M diumumkan tapi berapa yang sudah dicairkan ke builder, berapa remaining, dan criteria grant tidak ada dashboard publik
- [financial] Series B date discrepancy — blog Sei "Aug 2022" announce Series A+B bersama; The Block bilang Series B "Apr 2022" — perlu konfirmasi tanggal exact Series B close
- [financial] Valuation untuk Series A dan Series B — tidak diungkap; apakah equity valuation terpisah dari token valuation (SAFT/token warrant structure) — tidak dikonfirmasi
- [financial] Post-TGE funding — apakah ada follow-on round (Series C, strategic extension) setelah mainnet launch 2023-08-15 — tidak diumumkan
- [financial] Audit financial statements — Sei Labs Inc. apakah mengeluarkan audited financials (US GAAP) sebagai Delaware corp — tidak publik
- [financial] Token Terminal / DefiLlama revenue data accuracy — on-chain fees terbaca tapi apakah represent 100% protocol revenue atau hanya subset (misal: EVM priority fees tidak fully captured) — perlu validasi metodologi
- [financial] Community pool spending history — governance proposals untuk community pool spend (parameter change, grant, upgrade) tersedia di Seitrace tapi tidak diasumsikan ke financial report terstruktur
- [financial] Regulatory risk disclosure — Sei Labs tidak mempublikasikan legal memo tentang status token SEI di bawah hukum AS (security vs commodity) — risiko finansial jika SEC enforcement
- [token] Exact circulating supply per tanggal tertentu — CoinGecko/Token Terminal memberikan estimasi tapi on-chain circulating supply calculation methodology tidak dipublikasikan resmi (perlu query staking module + vesting contracts + community pool + bridge contracts)
- [token] Vesting contract addresses untuk Team, Investors, Foundation — tidak dipublikasikan dengan label resmi di docs.sei.io; perlu identifikasi on-chain via genesis allocation dan tracking transfer
- [token] Advisors allocation — whitepaper tidak memisahkan advisors; apakah termasuk dalam Team (20%) atau Investors (22%) atau tidak ada — perlu konfirmasi dari Sei Labs
- [token] Inflation rate parameter governance — whitepaper menyebut "target 7%" tapi parameter mint module saat ini (inflation_max, inflation_min, goal_bonded) tidak terpublikasi di docs; perlu query on-chain gov params
- [token] EVM base fee burn rate vs staking emission — net supply growth rate aktual tidak dipublikasikan; Token Terminal data perlu divalidasi metodologi
- [token] Community Pool address dan balance history — distribution module address tersedia tapi historical balance dan spending proposals tidak ada dashboard terpusat
- [token] Airdrop criteria dan allocation breakdown — "Community 48%" mencakup airdrop, testnet incentives, ecosystem grants, liquidity mining; persentase masing-masing tidak di-breakdown di whitepaper
- [token] Sei Foundation legal entity dan treasury custody — apakah Foundation terpisah dari Sei Labs Inc. (Cayman/Swiss) dan bagaimana custody multi-sig — tidak dikonfirmasi publik
- [token] Bridged SEI supply per chain — total SEI locked di Wormhole/Axelar contracts di Ethereum, Solana, Arbitrum, dll tidak teragregasi resmi; perlu query per bridge contract
- [token] Fee switch / revenue sharing ke SEI holders — tidak ada mechanism fee switch (seperti UNI fee switch) di whitepaper atau governance; semua fee ke validator + community pool
- [token] Parameter change proposal history untuk tokenomics (inflation, community tax, max validators) — tersedia di Seitrace gov tapi tidak ada summary terstruktur
- [token] Emergency pause / upgrade authority untuk token contract — native SEI tidak memiliki pause function (Cosmos SDK bank module); ERC-20 contract apakah memiliki admin/owner — perlu verifikasi Etherscan contract code
- [token] Staking reward APY real-time vs target — target 7% inflation tapi real yield bergantung pada bonded ratio; dashboard resmi APY tidak ada
- [token] Tokenomics update proposal (jika ada) — apakah ada governance proposal untuk mengubah distribution, vesting, atau inflation parameters post-TGE — perlu scan Seitrace gov history
- [ecosystem] Exact legal structure and jurisdiction of Sei Foundation — not publicly confirmed; assumed Cayman/Swiss but no filing found
- [ecosystem] Complete list of all chains with SEI bridged deployments post-knowledge cutoff — Linea, Scroll, Mantle, zkSync Era may have Wormhole/Axelar deployments not captured
- [ecosystem] Current validator set Nakamoto coefficient and entity-level stake concentration — not published officially; requires on-chain analysis
- [ecosystem] SeiDB fast sync trust assumptions documentation — "trusted checkpoint" model not fully specified in public docs; security model needs clarification
- [ecosystem] Geth version pinning and upgrade policy for Sei v2 — how Sei handles upstream Geth releases, consensus-critical patches, and fork maintenance not documented
- [ecosystem] Wormhole/Axelar bridge contract addresses on Sei for each target chain — not aggregated in single docs page; need per-chain verification
- [ecosystem] Pyth/Chainlink feed IDs and contract addresses on Sei for major trading pairs — not in centralized developer docs
- [ecosystem] Ecosystem Fund ($50M) deployment transparency — no public dashboard showing grants awarded, remaining balance, recipient categories
- [ecosystem] Community Pool address and historical spending proposals — distribution module address known but no structured spending analytics dashboard
- [ecosystem] Regulatory engagement status — Sei Labs Inc. Delaware entity; no public disclosure of SEC communications, legal opinions on SEI token status
- [ecosystem] Cross-VM (CosmWasm ↔ EVM) reentrancy protection implementation details — not in public technical specs
- [ecosystem] IBC-Go v8 / Interchain Accounts (ICA) upgrade timeline — planned but no governance proposal visible on-chain
- [ecosystem] CosmWasm 2.0 (Stargate) upgrade status — CosmWasm 2.0 released but Sei upgrade proposal not yet on-chain as of knowledge cutoff
- [ecosystem] Formal verification status of parallel execution engine — Veridise audit referenced but full formal spec and properties not published
- [ecosystem] Maximum validator count governance parameter change history — currently 100 but change process and rationale not in technical docs
- [ecosystem] Emergency circuit breakers for bridge/oracle failures — no documented protocol-level pause mechanisms for bridged assets or oracle feeds
- [market] Real-time TVL and volume data — DefiLlama and Token Terminal provide snapshots but methodology differences create discrepancies (e.g., DefiLlama TVL ~$380M vs Token Terminal ~$420M as of 2024-10); need standardized source for ongoing tracking
- [market] Exact daily active user definition — "addresses with >0 transactions" vs "addresses interacting with contracts" vs "unique signers" yield different counts; Seitrace, Dune, Token Terminal use different methodologies
- [market] Developer count accuracy — Electric Capital report uses GitHub commits to core repos; misses ecosystem developers building dApps only; Sei-specific developer census not published
- [market] Bridge volume aggregation — Wormhole and Axelar report volumes differently (USD vs token count; inbound vs outbound); no unified Sei bridge volume dashboard
- [market] Nakamoto coefficient calculation — seitrace.com shows validator stake distribution but entity-level consolidation (same operator running multiple validators) not identifiable on-chain; community estimates vary 8–12
- [market] Perp volume market share — CoinGecko derivatives category aggregates across exchanges but double-counts wash trading; Binance SEIUSDT volume dominance (~80%+) not separately reported
- [market] Ecosystem Fund deployment transparency — $50M announced but no public dashboard showing grants awarded, recipients, categories, remaining balance; only anecdotal announcements
- [market] Token unlock schedule tracking — Team/investor monthly vesting since Aug 2024 cliff end; exact unlock amounts per month not published in machine-readable format; need on-chain vesting contract monitoring
- [market] Geographic trading distribution — Binance global vs Coinbase US vs Bybit/OKX Asia volume split not published; regulatory exposure varies by exchange jurisdiction
- [market] Messari/Token Terminal methodology differences — Both provide revenue/fees data but Token Terminal includes EVM priority fees while Messari may only count base fees; reconciliation needed
- [market] Competitor TVL comparison timing — DefiLlama chain TVL snapshots taken at different times; Solana $8B vs Sei $380M ratio changes daily; need timestamped comparison
- [market] Sei v2 adoption metrics — EVM-specific metrics (EVM tx count, unique EVM addresses, Solidity contracts deployed) not separated from CosmWasm metrics in public dashboards
- [market] Institutional custody availability — Fireblocks, Copper, Anchorage, BitGo support for SEI native (not just ERC-20) not confirmed; affects institutional adoption narrative
- [market] Regulatory status clarity — Sei Labs Inc. Delaware entity; SEI token classification (security vs commodity) not formally determined; no public SEC correspondence or legal opinion released
- [behavioral] Sei Foundation legal entity dan jurisdiction: Whitepaper mention "Foundation 10%" tapi tidak ada filing publik (Cayman/Swiss/Delaware?); multi-sig signers tidak diketahui; custody arrangement tidak transparan → perlu verifikasi legal docs atau on-chain multisig analysis
- [behavioral] Treasury wallet addresses dan composition: Community pool address known (distribution module) tapi Foundation/team treasury tidak labeled; stablecoin vs SEI ratio tidak diketahui; revenue/expense tracking tidak publik → perlu on-chain forensic atau official disclosure
- [behavioral] Exact token allocation breakdown per investor (Series A vs B): Whitepaper "Investors 22%" aggregated; individual investor token amount, vesting start/end, lockup terms tidak dipublikasikan → cap table opacity; market maker investors (Wintermute, Jane Street) token allocation memengaruhi liquidity dynamics
- [behavioral] Sei v2 Geth version pinning dan upgrade policy: Upstream Geth releases (Shanghai, Cancun, Prague) → bagaimana Sei handle consensus-critical changes? Fork maintenance burden? Delayed upgrade risk? → tidak terdokumentasi di public specs
- [behavioral] SeiDB fast sync trust model detail: "Trusted checkpoint" untuk fast sync → siapa generate checkpoint? Verification process? Attack vector jika checkpoint malicious? → blog mention tapi spec tidak lengkap
- [behavioral] Cross-VM (CosmWasm ↔ EVM) reentrancy protection implementation: Precompile calls dari EVM ke native module → reentrancy guard design? State sync atomicity? → tidak di public docs; audit reports (Trail of Bits, Zellic) mungkin cover tapi tidak publik
- [behavioral] Ecosystem Fund ($50M) deployment actual: Berapa sudah dicairkan? Ke project apa? Kategori distribution? Remaining balance? → no dashboard; hanya announcements berantakan; transparency gap vs competitor foundations
- [behavioral] Nakamoto coefficient actual (entity-level): Seitrace validator stake distribution known tapi entity mapping (same operator multiple validators) tidak on-chain → perlu off-chain analysis (IP, commission address, governance voting pattern)
- [behavioral] Sei Labs revenue model post-VC: Apakah team mengambil cut dari community pool fees? Atau fully funded oleh Series A+B + token treasury? → tidak di-disclose; kritis untuk sustainability assessment
- [behavioral] Regulatory engagement status: Sei Labs Inc. Delaware; SEI token classification (security vs commodity) → apakah ada legal memo? SEC correspondence? Howey analysis? → tidak publik; material risk untuk US operations
- [behavioral] IBC-Go v8 / Interchain Accounts (ICA) upgrade timeline: Planned tapi no governance proposal visible; dependency pada Cosmos SDK upgrade path → blockers unknown
- [behavioral] CosmWasm 2.0 (Stargate) upgrade status: CosmWasm 2.0 released 2024; Sei upgrade proposal tidak on-chain → timeline? Breaking changes untuk existing contracts?
- [behavioral] Formal verification parallel execution engine: Veridise audit referenced "formal verification" tapi properties (safety/liveness under contention) tidak published → audit report access needed
- [behavioral] Maximum validator count governance parameter history: Currently 100; change process? Rationale? Previous changes? → tidak di technical docs
- [behavioral] Emergency circuit breakers untuk bridge/oracle failure: Protocol-level pause mechanism untuk bridged assets atau oracle feeds? → tidak terdokumentasi; dependency pada external provider emergency measures
- [behavioral] Institutional custody support untuk SEI native: Fireblocks, Copper, Anchorage, BitGo support SEI native (bukan hanya ERC-20)? → affects institutional adoption narrative; tidak konfirmasi publik
- [knowledge] Sei Foundation legal entity dan jurisdiction: Whitepaper mention "Foundation 10%" tapi tidak ada filing publik; multi-sig signers tidak diketahui; custody arrangement tidak transparan → perlu verifikasi legal docs atau on-chain multisig analysis【Phase 2 — Entity: no Foundation】【Phase 5 — Treasury】【Phase 6 — Distribution: Foundation 10%】【Phase 7 — Governance: Foundation assumed】【Phase 9 — Open Threads: Foundation legal entity】
- [knowledge] Treasury wallet addresses dan composition: Community pool address known tapi Foundation/team treasury tidak labeled; stablecoin vs SEI ratio tidak diketahui; revenue/expense tracking tidak publik【Phase 5 — Treasury】【Phase 9 — Open Threads: Treasury wallet addresses】
- [knowledge] Exact token allocation breakdown per investor (Series A vs B): Whitepaper "Investors 22%" aggregated; individual investor token amount, vesting terms tidak dipublikasikan【Phase 5 — Funding History】【Phase 6 — Distribution: Investors 22%】【Phase 9 — Open Threads: Exact token allocation breakdown per investor】
- [knowledge] Sei v2 Geth version pinning dan upgrade policy: Upstream Geth releases (Shanghai, Cancun, Prague) → bagaimana Sei handle consensus-critical changes? Fork maintenance burden?【Phase 4 — Known Limitations: Geth Embedding Dependency】【Phase 9 — Open Threads: Sei v2 Geth version pinning】
- [knowledge] SeiDB fast sync trust model detail: "Trusted checkpoint" → siapa generate? Verification process? Attack vector jika checkpoint malicious?【Phase 4 — Known Limitations: SeiDB Fast Sync Trust Assumption】【Phase 9 — Open Threads: SeiDB fast sync trust model】
- [knowledge] Cross-VM (CosmWasm ↔ EVM) reentrancy protection implementation: Precompile calls dari EVM ke native module → reentrancy guard design? State sync atomicity?【Phase 4 — Known Limitations: Cross-VM Latency】【Phase 9 — Open Threads: Cross-VM reentrancy protection】
- [knowledge] Ecosystem Fund ($50M) deployment actual: Berapa sudah dicairkan? Ke project apa? Remaining balance?【Phase 5 — Ecosystem Fund】【Phase 7 — Grant Program】【Phase 9 — Open Threads: Ecosystem Fund deployment actual】
- [knowledge] Nakamoto coefficient actual (entity-level): Seitrace validator stake known tapi entity mapping (same operator multiple validators) tidak on-chain【Phase 7 — Governance: Validator Set】【Phase 8 — Nakamoto Coefficient estimated】【Phase 9 — Open Threads: Nakamoto coefficient actual】
- [knowledge] Sei Labs revenue model post-VC: Apakah team mengambil cut dari community pool fees? Atau fully funded oleh Series A+B + token treasury?【Phase 5 — Revenue Model, Financial Dependencies】【Phase 9 — Weaknesses: No Sustainable Revenue Model, Open Threads: Sei Labs revenue model post-VC】
- [knowledge] Regulatory engagement status: Sei Labs Inc. Delaware; SEI token classification → legal memo? SEC correspondence? Howey analysis?【Phase 2 — Sei Labs Inc.】【Phase 5 — Financial Risk: Legal Financial Risk】【Phase 9 — Open Threads: Regulatory engagement status】
- [knowledge] IBC-Go v8 / Interchain Accounts (ICA) upgrade timeline: Planned tapi no governance proposal visible; blockers unknown【Phase 4 — Technical Upgrade History: IBC-Go v8 planned】【Phase 7 — Ecosystem Risks: Cosmos SDK Upgrade Coordination】【Phase 9 — Open Threads: IBC-Go v8 upgrade timeline】
- [knowledge] CosmWasm 2.0 (Stargate) upgrade status: CosmWasm 2.0 released 2024; Sei upgrade proposal tidak on-chain【Phase 4 — Technical Upgrade History: CosmWasm 2.0 planned】【Phase 9 — Open Threads: CosmWasm 2.0 upgrade status】
- [knowledge] Formal verification parallel execution engine: Veridise audit referenced "formal verification" tapi properties tidak published【Phase 4 — Audit History: Veridise】【Phase 9 — Open Threads: Formal verification parallel execution】
- [knowledge] Maximum validator count governance parameter history: Currently 100; change process? Rationale?【Phase 4 — Consensus Mechanism: 100 validators】【Phase 9 — Open Threads: Maximum validator count governance parameter】
- [knowledge] Emergency circuit breakers untuk bridge/oracle failure: Protocol-level pause mechanism untuk bridged assets atau oracle feeds?【Phase 7 — Ecosystem Risks: Bridge/Oracle Dependency】【Phase 9 — Open Threads: Emergency circuit breakers】
- [knowledge] Institutional custody support untuk SEI native: Fireblocks, Copper, Anchorage, BitGo support SEI native?【Phase 7 — Wallet Ecosystem: Ledger via Keplr/MetaMask】【Phase 8 — Open Threads: Institutional custody availability】【Phase 9 — Open Threads: Institutional custody support SEI native】
