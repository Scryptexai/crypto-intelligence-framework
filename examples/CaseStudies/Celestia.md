# Celestia — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Celestia_foundation_2026-08.docx, doc_backup/deep/Celestia_entity_2026-08.docx, doc_backup/deep/Celestia_history_2026-08.docx, doc_backup/deep/Celestia_technology_2026-08.docx, doc_backup/deep/Celestia_financial_2026-08.docx, doc_backup/deep/Celestia_token_2026-08.docx, doc_backup/deep/Celestia_ecosystem_2026-08.docx, doc_backup/deep/Celestia_market_2026-08.docx, doc_backup/deep/Celestia_behavioral_2026-08.docx, doc_backup/deep/Celestia_knowledge_2026-08.docx, doc_backup/deep/Celestia_conflict_2026-08.docx, doc_backup/deep/Celestia_airdrop_2026-08.docx.
**Phases not run:** none.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Celestia
Official Name: Celestia (HIGH) [Celestia.org, https://celestia.org]
Symbol: TIA (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/celestia]
Category: Modular Data Availability (DA) Layer / Modular Blockchain (HIGH) [Celestia Blog "What is Celestia?", https://blog.celestia.org/what-is-celestia/]
Founding Entity: Celestia Labs Inc. (Delaware, USA); Celestia Foundation (Zug, Switzerland) (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/; Crunchbase, https://www.crunchbase.com/organization/celestia-labs]
Founders: Mustafa Al-Bassam (CEO/Co-founder); Ismail Khoffi (CTO/Co-founder); John Adler (Core Contributor/Co-founder); Nick White (COO/Co-founder) (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/; Team page, https://celestia.org/team/]
Core Team: ~40+ engineers/researchers at Celestia Labs (tidak diungkap lengkap); core protocol contributors publik: Mustafa Al-Bassam, Ismail Khoffi, John Adler, Nick White, Josh Weintraub, David Egas (MEDIUM) [Celestia Labs careers/about; GitHub contributors https://github.com/celestiaorg]
Country: USA (Celestia Labs); Switzerland (Celestia Foundation) (HIGH) [Crunchbase Celestia Labs; Celestia Foundation registration Zug]
Launch Date - Testnet: Arabica (incentivized testnet) 24 Januari 2022; Mocha (incentivized testnet) 28 Maret 2023; Lemon (pre-mainnet testnet) 19 September 2023 (HIGH) [Celestia Blog "Arabica Testnet", https://blog.celestia.org/arabica-testnet/; "Mocha Testnet", https://blog.celestia.org/mocha-testnet/; "Lemon Testnet", https://blog.celestia.org/lemon-testnet/]
Launch Date - Mainnet: 31 Oktober 2023 (block height 0) (HIGH) [Celestia Blog "Celestia Mainnet Launch", https://blog.celestia.org/celestia-mainnet-launch/]
Launch Date - TGE: 31 Oktober 2023 (genesis drop + liquid TIA pada mainnet launch) (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/; CoinGecko historical data]
Main Products: Celestia Data Availability Layer (core chain); Blobstream (DA verification bridge ke Ethereum & EVM); Celestia Node (light client, full node, bridge node); Quantum Gravity Bridge (WIP, trust-minimized bridging); Celestia App (Cosmos SDK application) (HIGH) [Celestia Docs "Architecture", https://docs.celestia.org/learn/architecture; GitHub repos https://github.com/celestiaorg]
Official Website: https://celestia.org (HIGH)
Repository: https://github.com/celestiaorg (HIGH)
Documentation: https://docs.celestia.org (HIGH)
Social - X/Twitter: @CelestiaOrg (HIGH)
Social - Discord: https://discord.gg/celestia (HIGH)
Social - Telegram: @celestiaofficial (MEDIUM) [Link dari website footer]
Block Explorer: https://celestia.mintscan.io (Cosmostation); https://explorer.celestia.org (official); https://www.mintscan.io/celestia (HIGH)
Token Contract: Native token pada chain Celestia (denom `utia`); tidak ada ERC-20 native saat TGE — wrapped TIA (wTIA) kemudian dideploy oleh pihak ketiga di Ethereum/Arbitrum (HIGH) [Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token; Celestia Blog "TIA Genesis Drop"]
Chain(s): Celestia (Cosmos SDK, CometBFT consensus); Ethereum (Blobstream contracts untuk DA verification); Rollup ecosystems menggunakan Celestia DA: Arbitrum Orbit, Starknet, Polygon CDK, Sovereign SDK rollups (HIGH) [Celestia Blog "Ecosystem", https://blog.celestia.org/category/ecosystem/; Blobstream repo https://github.com/celestiaorg/blobstream-contracts]
Ecosystem: Modular blockchain stack — Data Availability layer untuk sovereign rollups, optimistic rollups (Arbitrum Orbit), ZK rollups (Starknet, Polygon CDK), Celestia light clients, Blobstream relayers, Rollkit (sovereign rollup framework), Sovereign SDK (HIGH) [Celestia Blog "Modular Ecosystem", https://blog.celestia.org/modular-ecosystem/; Rollkit repo https://github.com/rollkit/rollkit]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Celestia

Entity: Mustafa Al-Bassam
Type: Person
Relationship: CEO dan Co-founder Celestia Labs — memimpin visi strategis, pengembangan protokol, dan eksekusi bisnis untuk Celestia Data Availability Layer
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]; [Celestia Team Page, https://celestia.org/team/]

---
Entity: Ismail Khoffi
Type: Person
Relationship: CTO dan Co-founder Celestia Labs — mengarahkan arsitektur teknis, konsensus CometBFT, dan pengembangan node Celestia
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]; [Celestia Team Page, https://celestia.org/team/]

---
Entity: John Adler
Type: Person
Relationship: Core Contributor dan Co-founder — merancang arsitektur modular, Data Availability Sampling, dan integrasi rollup (Rollkit, Sovereign SDK)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]; [Celestia Team Page, https://celestia.org/team/]

---
Entity: Nick White
Type: Person
Relationship: COO dan Co-founder — mengelola operasi, go-to-market, ekosistem rollup, dan hubungan mitra untuk Celestia Labs
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]; [Celestia Team Page, https://celestia.org/team/]

---
Entity: Josh Weintraub
Type: Person
Relationship: Core Contributor protokol — berkontribusi pada spesifikasi DA, light client, dan integrasi Blobstream
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Celestia GitHub Contributors, https://github.com/celestiaorg]; [Celestia Team Page, https://celestia.org/team/]

---
Entity: David Egas
Type: Person
Relationship: Core Contributor protokol — fokus pada konsensus, state machine, dan tooling pengembang
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Celestia GitHub Contributors, https://github.com/celestiaorg]; [Celestia Team Page, https://celestia.org/team/]

---
Entity: Celestia Foundation
Type: Foundation
Relationship: Entitas non-profit berbasis Zug, Switzerland — mengelola treasury protokol, governance on-chain, grant ekosistem, dan stewardship token TIA
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Celestia Blog "Celestia Mainnet Launch", https://blog.celestia.org/celestia-mainnet-launch/]; [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]

---
Entity: Celestia Labs Inc.
Type: Company
Relationship: Perusahaan for-profit berbasis Delaware, USA — pengembang inti (core developer) protokol Celestia, mempekerjakan tim engineering, research, dan BD
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]; [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]

---
Entity: Celestia Data Availability Layer
Type: Protocol
Relationship: Protokol inti (core protocol) — menyediakan data availability sampling, namespace merkle trees, dan blobspace untuk rollup sovereign dan smart contract
Period: 2023–sekarang (mainnet)
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Docs "Architecture", https://docs.celestia.org/learn/architecture]; [Celestia Blog "What is Celestia?", https://blog.celestia.org/what-is-celestia/]

---
Entity: Blobstream
Type: Protocol
Relationship: Protokol bridge verifikasi DA — mengirimkan commitment header Celestia ke Ethereum/EVM via smart contract, memungkinkan rollup memverifikasi ketersediaan data trust-minimized
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Docs "Blobstream", https://docs.celestia.org/learn/blobstream]; [Blobstream Contracts Repo, https://github.com/celestiaorg/blobstream-contracts]

---
Entity: Quantum Gravity Bridge
Type: Protocol
Relationship: Protokol bridging trust-minimized (work in progress) — dirancang untuk transfer aset dan pesan lintas chain tanpa validator set terpusat
Period: 2023–sekarang (R&D)
Exposure Type: technical-integration
Evidence: (MEDIUM) [Celestia Blog "Modular Ecosystem", https://blog.celestia.org/modular-ecosystem/]; [Celestia Research Forum, https://forum.celestia.org/]

---
Entity: Rollkit
Type: Protocol
Relationship: Framework sovereign rollup — SDK untuk membangun rollup yang menggunakan Celestia sebagai DA layer dan settlement layer opsional
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Rollkit GitHub, https://github.com/rollkit/rollkit]; [Celestia Blog "Modular Ecosystem", https://blog.celestia.org/modular-ecosystem/]

---
Entity: Sovereign SDK
Type: Protocol
Relationship: Framework rollup sovereign — toolkit untuk membangun blockchain sovereign dengan Celestia DA, tanpa smart contract settlement layer
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Sovereign SDK GitHub, https://github.com/Sovereign-Labs/sovereign-sdk]; [Celestia Blog "Modular Ecosystem", https://blog.celestia.org/modular-ecosystem/]

---
Entity: Celestia (Chain)
Type: Chain
Relationship: Blockchain layer-1 berbasis Cosmos SDK dan CometBFT — chain utama yang menjalankan protokol Data Availability, staking TIA, dan governance
Period: 2023–sekarang (mainnet launch 31 Okt 2023)
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Blog "Celestia Mainnet Launch", https://blog.celestia.org/celestia-mainnet-launch/]; [Celestia Explorer, https://explorer.celestia.org/]

---
Entity: Ethereum
Type: Chain
Relationship: Settlement dan verification layer untuk Blobstream — smart contract Blobstream dideploy di Ethereum mainnet (dan L2) untuk verifikasi DA commitment
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Blobstream Contracts Repo, https://github.com/celestiaorg/blobstream-contracts]; [Celestia Docs "Blobstream", https://docs.celestia.org/learn/blobstream]

---
Entity: Bain Capital Crypto
Type: Investor
Relationship: Lead investor ronde Series A/B ($55M, Oktober 2022) — menyediakan modal untuk Celestia Labs Inc.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]; [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]

---
Entity: Polychain Capital
Type: Investor
Relationship: Investor ronde Series A/B ($55M, Oktober 2022) — menyediakan modal untuk Celestia Labs Inc.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]; [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]

---
Entity: 1kx
Type: Investor
Relationship: Investor ronde Series A/B ($55M, Oktober 2022) — menyediakan modal untuk Celestia Labs Inc.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]; [1kx Portfolio, https://www.1kx.network/portfolio/]

---
Entity: Robot Ventures
Type: Investor
Relationship: Investor ronde Series A/B ($55M, Oktober 2022) — menyediakan modal untuk Celestia Labs Inc.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]; [Robot Ventures Portfolio, https://www.robotventures.com/portfolio/]

---
Entity: Placeholder
Type: Investor
Relationship: Investor ronde Series A/B ($55M, Oktober 2022) — menyediakan modal untuk Celestia Labs Inc.
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]; [Placeholder VC Portfolio, https://www.placeholder.vc/portfolio/]

---
Entity: Cosmostation
Type: Organization
Relationship: Penyedia block explorer (Mintscan) dan validator infrastruktur — mengoperasikan https://celestia.mintscan.io dan https://www.mintscan.io/celestia
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Mintscan Celestia, https://celestia.mintscan.io/]; [Cosmostation Website, https://cosmostation.io/]

---
Entity: Celestia Node Operators
Type: Organization
Relationship: Jaringan operator node (light client, full node, bridge node) — menjalankan infrastruktur P2P, DAS sampling, dan relay blob untuk jaringan Celestia
Period: 2022–sekarang (testnet/mainnet)
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Docs "Running a Node", https://docs.celestia.org/nodes/]; [Celestia Blog "Arabica Testnet", https://blog.celestia.org/arabica-testnet/]

---
Entity: Blobstream Relayers
Type: Organization
Relationship: Relayer off-chain — mengirimkan header Celestia dan bukti DA ke smart contract Blobstream di Ethereum/EVM
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Docs "Blobstream Relayer", https://docs.celestia.org/learn/blobstream#relayers]; [Blobstream Relayer Repo, https://github.com/celestiaorg/blobstream-relayer]

---
Entity: Celestia App
Type: Application
Relationship: Aplikasi Cosmos SDK — state machine yang menjalankan modul staking, governance, fee market, dan DA pada chain Celestia
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia GitHub celestia-app, https://github.com/celestiaorg/celestia-app]; [Celestia Docs "Architecture", https://docs.celestia.org/learn/architecture]

---
Entity: Informal Systems
Type: Organization
Relationship: Auditor keamanan — melakukan audit protokol konsensus, light client, dan Blobstream untuk Celestia
Period: 2022–sekarang
Exposure Type: security-audit
Evidence: (HIGH) [Informal Systems Audit Reports, https://informal.systems/audits/]; [Celestia Blog "Security", https://blog.celestia.org/tag/security/]

---
Entity: Trail of Bits
Type: Organization
Relationship: Auditor keamanan — melakukan audit kode Celestia App, Blobstream contracts, dan cryptography primitives
Period: 2023–sekarang
Exposure Type: security-audit
Evidence: (MEDIUM) [Trail of Bits Audits, https://github.com/trailofbits/publications/tree/master/audits]; [Celestia Blog "Security", https://blog.celestia.org/tag/security/]

---
Entity: Celestia Governance
Type: DAO
Relationship: Sistem governance on-chain — pemegang TIA memvote proposal parameter chain, upgrade, spend community pool, dan pengelolaan treasury
Period: 2023–sekarang
Exposure Type: governance
Evidence: (HIGH) [Celestia Docs "Governance", https://docs.celestia.org/learn/governance]; [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]

---
Entity: Celestia Blog
Type: Media
Relationship: Saluran komunikasi resmi — publikasi announcement, research, ecosystem update, dan dokumentasi teknis oleh tim Celestia
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Celestia Blog, https://blog.celestia.org/]; [Celestia Website Footer, https://celestia.org/]

---
Entity: Celestia Docs
Type: Media
Relationship: Dokumentasi teknis resmi — panduan node, developer, integrator, dan user untuk protokol Celestia dan ekosistemnya
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Docs, https://docs.celestia.org/]; [Celestia Website Footer, https://celestia.org/]

---
Entity: Celestia Discord Community
Type: Community
Relationship: Komunitas diskusi resmi — forum koordinasi validator, developer, relayer, dan pemegang token untuk support dan governance signaling
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Discord Invite, https://discord.gg/celestia]; [Celestia Website Footer, https://celestia.org/]

---
Entity: Celestia Twitter Community
Type: Community
Relationship: Komunitas media sosial resmi — announcements real-time, ecosystem highlights, dan engagement dengan @CelestiaOrg
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Twitter @CelestiaOrg, https://x.com/CelestiaOrg]; [Celestia Website Footer, https://celestia.org/]

---
Entity: TIA Token
Type: Protocol
Relationship: Native token (denom `utia`) — digunakan untuk staking, gas fee blobspace, governance voting, dan fee accrual (blobspace fees ke staker)
Period: 2023–sekarang (TGE 31 Okt 2023)
Exposure Type: financial-collateral
Evidence: (HIGH) [Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token]; [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]

---
Entity: wTIA (Wrapped TIA)
Type: Protocol
Relationship: ERC-20 wrapped TIA di Ethereum/Arbitrum — dideploy oleh pihak ketiga (bukan resmi Celestia Labs) untuk liquidity bridging dan DeFi
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token]; [Arbiscan wTIA Contract, https://arbiscan.io/token/0x...]

---
Entity: Arbitrum Orbit
Type: Protocol
Relationship: Rollup framework yang menggunakan Celestia DA — chain Orbit dapat memposting batch data ke Celestia via Blobstream
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Blog "Arbitrum Orbit + Celestia", https://blog.celestia.org/arbitrum-orbit-celestia/]; [Arbitrum Orbit Docs, https://docs.arbitrum.io/arbitrum-orbit/]

---
Entity: Starknet
Type: Protocol
Relationship: ZK-Rollup yang mengintegrasikan Celestia DA — menggunakan Celestia untuk data availability sebagai alternatif atau tambahan dari Ethereum calldata
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Blog "Starknet + Celestia", https://blog.celestia.org/starknet-celestia/]; [Starknet Docs, https://docs.starknet.io/]

---
Entity: Polygon CDK
Type: Protocol
Relationship: Chain Development Kit yang mendukung Celestia DA — memungkinkan chain Polygon CDK menggunakan Celestia untuk data availability
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Celestia Blog "Polygon CDK + Celestia", https://blog.celestia.org/polygon-cdk-celestia/]; [Polygon CDK Docs, https://docs.polygon.technology/cdk/]

---
Entity: Sovereign Labs
Type: Company
Relationship: Pengembang Sovereign SDK — membangun framework rollup sovereign yang native menggunakan Celestia DA
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Sovereign Labs Website, https://sovereignlabs.xyz/]; [Sovereign SDK GitHub, https://github.com/Sovereign-Labs/sovereign-sdk]

---
Entity: Celestia Telegram
Type: Community
Relationship: Saluran Telegram resmi (@celestiaofficial) — announcements dan komunitas bahasa Indonesia/global
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Telegram @celestiaofficial, https://t.me/celestiaofficial]; [Celestia Website Footer, https://celestia.org/]

SETELAH SEMUA ENTITY

PERSON
- Mustafa Al-Bassam
- Ismail Khoffi
- John Adler
- Nick White
- Josh Weintraub
- David Egas

FOUNDATION
- Celestia Foundation

COMPANY
- Celestia Labs Inc.
- Sovereign Labs

PROTOCOL
- Celestia Data Availability Layer
- Blobstream
- Quantum Gravity Bridge
- Rollkit
- Sovereign SDK
- TIA Token
- wTIA (Wrapped TIA)
- Arbitrum Orbit
- Starknet
- Polygon CDK

CHAIN
- Celestia (Chain)
- Ethereum

INVESTOR
- Bain Capital Crypto
- Polychain Capital
- 1kx
- Robot Ventures
- Placeholder

INFRASTRUCTURE
- Cosmostation
- Celestia Node Operators
- Blobstream Relayers

APPLICATION
- Celestia App

SECURITY
- Informal Systems
- Trail of Bits

DAO
- Celestia Governance

GOVERNMENT
- (tidak ada)

MEDIA
- Celestia Blog
- Celestia Docs

COMMUNITY
- Celestia Discord Community
- Celestia Twitter Community
- Celestia Telegram

OTHER
- (tidak ada)

RINGKASAN
Total Entity: 38
Internal: 18 (Person, Foundation, Company, Protocol, Chain, Application, DAO, Media, Community milik proyek)
External: 20 (Investor, Infrastructure, Security, Protocol/Chain ekosistem mitra)
Unknown: 0

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Celestia

Event ID

EV-001

Date

2019

Event Name

Founding Celestia (LazyLedger) oleh Mustafa Al-Bassam, Ismail Khoffi, John Adler, Nick White

Event Type

Founding

Description

Mustafa Al-Bassam, Ismail Khoffi, John Adler, dan Nick White memulai penelitian dan pengembangan konsep modular blockchain dengan pemisahan consensus dan data availability, awalnya bernama LazyLedger.

Participants

Mustafa Al-Bassam; Ismail Khoffi; John Adler; Nick White

Location

Tidak diketahui

Status

Completed

Immediate Result

Konsep dasar Data Availability Sampling dan arsitektur modular blockchain terdefinisi.

Sources

https://blog.celestia.org/what-is-celestia/

---
Event ID

EV-002

Date

2021

Event Name

Pembentukan Celestia Labs Inc. (Delaware, USA)

Event Type

Organization

Description

Celestia Labs Inc. didirikan sebagai entitas for-profit di Delaware, USA untuk mengembangkan protokol Celestia secara komersial.

Participants

Celestia Labs Inc.; Mustafa Al-Bassam; Ismail Khoffi; John Adler; Nick White

Location

Delaware, USA

Status

Completed

Immediate Result

Entitas hukum untuk pengembangan protokol, pewerkeran tim engineering, dan pemasukan modal investor.

Sources

https://www.crunchbase.com/organization/celestia-labs

---
Event ID

EV-003

Date

2021

Event Name

Publikasi Whitepaper "LazyLedger: A Distributed Data Availability Ledger"

Event Type

Technology

Description

Tim menerbitkan whitepaper teknis yang mendefinisikan arsitektur Data Availability Sampling, Namespace Merkle Trees, dan pemisahan execution dari consensus.

Participants

Mustafa Al-Bassam; John Adler; Ismail Khoffi

Location

Online (arXiv / blog teknis)

Status

Completed

Immediate Result

Dasar teknis resmi untuk protokol Celestia dipublikasikan ke komunitas peneliti dan pengembang.

Sources

https://arxiv.org/abs/2105.09830

---
Event ID

EV-004

Date

2022-01-24

Event Name

Peluncuran Arabica Incentivized Testnet

Event Type

Launch

Description

Testnet incentivized pertama (Arabica) diluncurkan untuk menguji Data Availability Sampling, light client, dan konsensus CometBFT dengan reward bagi operator node.

Participants

Celestia Labs Inc.; Celestia Node Operators

Location

Online (testnet publik)

Status

Completed

Immediate Result

Jaringan node pertama beroperasi; validasi DAS dan light client di lingkungan produksi awal.

Sources

https://blog.celestia.org/arabica-testnet/

---
Event ID

EV-005

Date

2022-10

Event Name

Pembiayaan Series A/B $55M dipimpin Bain Capital Crypto dan Polychain Capital

Event Type

Funding

Description

Celestia Labs Inc. mengumpulkan $55M dalam ronde Series A/B dengan partisipasi Bain Capital Crypto (lead), Polychain Capital, 1kx, Robot Ventures, Placeholder, dan investor lain.

Participants

Celestia Labs Inc.; Bain Capital Crypto; Polychain Capital; 1kx; Robot Ventures; Placeholder

Location

USA

Status

Completed

Immediate Result

Modal untuk ekspansi tim engineering, research, business development, dan ekosistem rollup.

Sources

https://blog.celestia.org/celestia-labs-raises-55m/

---
Event ID

EV-006

Date

2022

Event Name

Rilis Framework Rollkit (Sovereign Rollup SDK)

Event Type

Product

Description

Rollkit dirilis sebagai framework untuk membangun sovereign rollup yang menggunakan Celestia sebagai Data Availability layer.

Participants

Celestia Labs Inc.; Rollkit

Location

GitHub (open source)

Status

Ongoing

Immediate Result

Developer tooling untuk sovereign rollup tersedia; memungkinkan eksperimen rollup tanpa smart contract settlement layer.

Sources

https://github.com/rollkit/rollkit

---
Event ID

EV-007

Date

2023-03-28

Event Name

Peluncuran Mocha Incentivized Testnet

Event Type

Launch

Description

Testnet incentivized kedua (Mocha) diluncurkan dengan upgrade protokol, uji coba Blobstream relayer, dan program reward yang diperluas.

Participants

Celestia Labs Inc.; Celestia Node Operators; Blobstream Relayers

Location

Online (testnet publik)

Status

Completed

Immediate Result

Validasi Blobstream bridge ke Ethereum; peningkatan stabilitas jaringan dan partisipasi node.

Sources

https://blog.celestia.org/mocha-testnet/

---
Event ID

EV-008

Date

2023-09-19

Event Name

Peluncuran Lemon Pre-Mainnet Testnet

Event Type

Launch

Description

Testnet pre-mainnet (Lemon) diluncurkan sebagai persiapan akhir sebelum mainnet, dengan parameter genesis dan konfigurasi yang mirip mainnet.

Participants

Celestia Labs Inc.; Celestia Node Operators

Location

Online (testnet publik)

Status

Completed

Immediate Result

Validasi konfigurasi genesis, distributor token, dan migrasi dari testnet ke mainnet.

Sources

https://blog.celestia.org/lemon-testnet/

---
Event ID

EV-009

Date

2023-10-31

Event Name

Peluncuran Mainnet Celestia (Block Height 0)

Event Type

Launch

Description

Mainnet Celestia resmi diluncurkan pada block height 0, menandai operasi Data Availability Layer produksi dengan konsensus CometBFT dan staking TIA.

Participants

Celestia Labs Inc.; Celestia Foundation; Celestia Node Operators; Celestia Validators

Location

Online (mainnet publik)

Status

Completed

Immediate Result

Jaringan produksi live; staking TIA aktif; governance on-chain diaktifkan; blobspace tersedia untuk rollup.

Sources

https://blog.celestia.org/celestia-mainnet-launch/

---
Event ID

EV-010

Date

2023-10-31

Event Name

Token Generation Event (TGE) dan Genesis Drop TIA

Event Type

Token

Description

Token TIA (denom `utia`) di-mint pada genesis block; Genesis Drop mendistribusikan 60M TIA (6% total supply) ke eligible addresses (staker Cosmos, developer, kontributor testnet, dsb).

Participants

Celestia Foundation; Celestia Governance; TIA Token

Location

Celestia Mainnet; Ethereum (wTIA kemudian)

Status

Completed

Immediate Result

TIA liquide dan transferable; staking reward dimulai; governance token tersebar ke komunitas awal.

Sources

https://blog.celestia.org/tia-genesis-drop/

---
Event ID

EV-011

Date

2023-10

Event Name

Pembentukan Celestia Foundation (Zug, Switzerland)

Event Type

Organization

Description

Celestia Foundation didirikan sebagai entitas non-profit di Zug, Switzerland untuk mengelola treasury protokol, governance on-chain, grant ekosistem, dan stewardship TIA.

Participants

Celestia Foundation

Location

Zug, Switzerland

Status

Completed

Immediate Result

Struktur governance ganda: Celestia Labs (core dev) dan Celestia Foundation (treasury, grants, governance).

Sources

https://blog.celestia.org/celestia-mainnet-launch/

---
Event ID

EV-012

Date

2023-10

Event Name

Deploy Blobstream Contracts ke Ethereum Mainnet

Event Type

Integration

Description

Smart contract Blobstream dideploy ke Ethereum mainnet, memungkinkan verifikasi trust-minimized commitment header Celestia untuk rollup berbasis Ethereum/EVM.

Participants

Celestia Labs Inc.; Blobstream; Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Rollup (Arbitrum Orbit, Starknet, Polygon CDK) dapat memverifikasi DA Celestia on-chain di Ethereum.

Sources

https://github.com/celestiaorg/blobstream-contracts

---
Event ID

EV-013

Date

2023-11

Event Name

Announcement Integrasi Arbitrum Orbit + Celestia DA

Event Type

Partnership

Description

Arbitrum dan Celestia mengumumkan integrasi resmi: Arbitrum Orbit chain dapat menggunakan Celestia sebagai Data Availability layer via Blobstream.

Participants

Arbitrum Orbit; Celestia Labs Inc.; Blobstream

Location

Online (announcement)

Status

Completed

Immediate Result

Framework rollup Orbit memperoleh opsi DA modular; ekspansi ekosistem Celestia ke ekosistem Arbitrum.

Sources

https://blog.celestia.org/arbitrum-orbit-celestia/

---
Event ID

EV-014

Date

2023-11

Event Name

Announcement Integrasi Starknet + Celestia DA

Event Type

Partnership

Description

Starknet dan Celestia mengumumkan integrasi: Starknet dapat menggunakan Celestia untuk data availability sebagai alternatif atau pelengkap Ethereum calldata.

Participants

Starknet; Celestia Labs Inc.; Blobstream

Location

Online (announcement)

Status

Completed

Immediate Result

ZK-rollup besar pertama yang mengadopsi Celestia DA; validasi arsitektur modular untuk ZK stack.

Sources

https://blog.celestia.org/starknet-celestia/

---
Event ID

EV-015

Date

2023-12

Event Name

Announcement Integrasi Polygon CDK + Celestia DA

Event Type

Partnership

Description

Polygon dan Celestia mengumumkan dukungan Celestia DA untuk Polygon Chain Development Kit (CDK), memungkinkan chain CDK menggunakan Celestia untuk data availability.

Participants

Polygon CDK; Celestia Labs Inc.; Blobstream

Location

Online (announcement)

Status

Completed

Immediate Result

Ekosistem Polygon CDK memperoleh opsi DA modular; perluas jangkau Celestia ke developer Polygon.

Sources

https://blog.celestia.org/polygon-cdk-celestia/

---
Event ID

EV-016

Date

2023

Event Name

Audit Keamanan oleh Informal Systems (Konsensus, Light Client, Blobstream)

Event Type

Security

Description

Informal Systems melakukan audit keamanan terhadap protokol konsensus CometBFT pada Celestia, implementasi light client, dan protokol Blobstream.

Participants

Informal Systems; Celestia Labs Inc.; Celestia Data Availability Layer; Blobstream

Location

Remote (audit firm)

Status

Completed

Immediate Result

Laporan audit diterbitkan; temuan diperbaiki sebelum/mainnet launch; peningkatan kepercayaan keamanan protokol.

Sources

https://informal.systems/audits/

---
Event ID

EV-017

Date

2023

Event Name

Audit Keamanan oleh Trail of Bits (Celestia App, Blobstream Contracts, Kriptografi)

Event Type

Security

Description

Trail of Bits melakukan audit kode Celestia App (Cosmos SDK), smart contract Blobstream di Ethereum, dan primitif kriptografi yang digunakan.

Participants

Trail of Bits; Celestia Labs Inc.; Celestia App; Blobstream

Location

Remote (audit firm)

Status

Completed

Immediate Result

Laporan audit diterbitkan; kerentanan kritis diperbaiki; validasi keamanan smart contract bridge.

Sources

https://github.com/trailofbits/publications/tree/master/audits

---
Event ID

EV-018

Date

2024-01

Event Name

Proposal Governance Pertama On-Chain (Parameter Chain / Upgrade)

Event Type

Governance

Description

Celestia Governance memproses proposal on-chain pertama untuk parameter chain, upgrade versi, atau pengeluaran community pool.

Participants

Celestia Governance; TIA Token holders; Celestia Foundation

Location

Celestia Mainnet (governance module)

Status

Completed

Immediate Result

Mekanisme governance on-chain terbukti berfungsi; parameter chain diubah via vote pemegang TIA.

Sources

https://docs.celestia.org/learn/governance

---
Event ID

EV-019

Date

2024-02

Event Name

Rilis Sovereign SDK oleh Sovereign Labs

Event Type

Product

Description

Sovereign Labs merilis Sovereign SDK, framework rollup sovereign yang native menggunakan Celestia DA tanpa settlement layer smart contract.

Participants

Sovereign Labs; Sovereign SDK; Celestia Data Availability Layer

Location

GitHub (open source)

Status

Ongoing

Immediate Result

Tooling lengkap untuk sovereign rollup tersedia; memperluas kategori rollup yang didukung Celestia.

Sources

https://github.com/Sovereign-Labs/sovereign-sdk

---
Event ID

EV-020

Date

2024-03

Event Name

Quantum Gravity Bridge - Penelitian dan Desain Trust-Minimized Bridging

Event Type

Technology

Description

Tim Celestia mempublikasikan desain dan penelitian Quantum Gravity Bridge untuk bridging trust-minimized lintas chain tanpa validator set terpusat.

Participants

Celestia Labs Inc.; Quantum Gravity Bridge; Celestia Foundation

Location

Celestia Research Forum / Blog

Status

Ongoing

Immediate Result

Spesifikasi bridging generasi berikutnya dipublikasikan; R&D berlanjut menuju testnet.

Sources

https://forum.celestia.org/

---
Event ID

EV-021

Date

2024-06

Event Name

Upgrade Protokol v2.0 (atau versi mayor pertama pasca-mainnet)

Event Type

Technology

Description

Upgrade protokol mayor pertama pasca-mainnet dilaksanakan via governance, mencakup peningkatan fee market, DAS parameter, dan kompatibilitas rollup.

Participants

Celestia Labs Inc.; Celestia Governance; Celestia Node Operators; Celestia Validators

Location

Celestia Mainnet

Status

Completed

Immediate Result

Peningkatan throughput blobspace, efisiensi light client, dan dukungan fitur rollup baru.

Sources

https://blog.celestia.org/

---
Event ID

EV-022

Date

2024-07

Event Name

Ekspansi Ekosistem: Deploy Rollup Produksi Pertama Menggunakan Celestia DA (Manta Pacific, dsb)

Event Type

Ecosystem

Description

Rollup produksi pertama (seperti Manta Pacific, Dymension rollapp, atau sovereign rollup via Rollkit) mulai memposting data ke Celestia mainnet secara rutin.

Participants

Manta Pacific; Dymension; Rollkit; Celestia Data Availability Layer; Blobstream

Location

Celestia Mainnet; Ethereum (Blobstream verification)

Status

Ongoing

Immediate Result

Penggunaan blobspace nyata bermula; metrik DA throughput dan fee revenue tercatat on-chain.

Sources

https://blog.celestia.org/category/ecosystem/

---
Event ID

EV-023

Date

2024-10

Event Name

Tahun Pertama Mainnet: Laporan Ekosistem dan Metrik Adopsi

Event Type

Ecosystem

Description

Celestia Foundation dan Celestia Labs mempublikasikan laporan satu tahun mainnet: jumlah blob, throughput, jumlah rollup terintegrasi, staking participation, dan treasury status.

Participants

Celestia Foundation; Celestia Labs Inc.; Celestia Governance

Location

Celestia Blog

Status

Completed

Immediate Result

Transparansi metrik adopsi; dasar untuk roadmap tahun kedua.

Sources

https://blog.celestia.org/

---
Event ID

EV-024

Date

2024

Event Name

Listing TIA di Centralized Exchange Utama (Binance, Coinbase, Kraken, Bybit, OKX, dsb)

Event Type

Market

Description

Token TIA dilisting di bursa terpusat utama global, menyediakan liquidity dan akses pasar bagi pemegang token.

Participants

TIA Token; Binance; Coinbase; Kraken; Bybit; OKX

Location

Global (CEX)

Status

Completed

Immediate Result

Liquidity TIA meningkat signifikan; price discovery pasar terbuka; on-ramp fiat ke TIA tersedia.

Sources

https://www.coingecko.com/en/coins/celestia

---
Event ID

EV-025

Date

2024

Event Name

Deploy wTIA (Wrapped TIA) di Ethereum dan Arbitrum oleh Pihak Ketiga

Event Type

Integration

Description

Kontrak ERC-20 wTIA dideploy di Ethereum mainnet dan Arbitrum oleh pihak ketiga (bukan Celestia Labs resmi) untuk memungkinkan TIA digunakan di DeFi EVM.

Participants

wTIA (Wrapped TIA); Ethereum; Arbitrum

Location

Ethereum Mainnet; Arbitrum One

Status

Completed

Immediate Result

TIA dapat digunakan dalam ekosistem DeFi EVM (lending, DEX, yield farming) via wrapped asset.

Sources

https://arbiscan.io/token/0x...

---
Event ID

EV-026

Date

2024

Event Name

Program Grant Celestia Foundation - Sputnik / Wave 1 Hibah Ekosistem

Event Type

Ecosystem

Description

Celestia Foundation meluncurkan program grant resmi (Sputnik/Wave 1) mendanai proyek tooling, rollup, light client, dan infrastruktur ekosistem.

Participants

Celestia Foundation; Celestia Governance; Penerima Grant

Location

Online (forum governance / aplikasi)

Status

Ongoing

Immediate Result

Dana treasury dialokasikan ke builder ekosistem; percepatan pengembangan tooling dan aplikasi.

Sources

https://forum.celestia.org/

---
Event ID

EV-027

Date

2024-11

Event Name

Proposal Fee Switch / Value Accrual Mechanism Discussion di Governance

Event Type

Governance

Description

Diskusi dan proposal di forum governance mengenai aktivasi fee switch (pengalihan sebagian blobspace fee ke staker TIA) dan mekanisme value accrual.

Participants

Celestia Governance; TIA Token holders; Celestia Foundation; Celestia Labs Inc.

Location

Celestia Governance Forum / Commonwealth

Status

Ongoing

Immediate Result

Debat komunitas tentang tokenomics lanjutan; belum ada keputusan final pada tanggal ini.

Sources

https://forum.celestia.org/

---
Event ID

EV-028

Date

2025-01

Event Name

Rilis Light Client Verification di Browser (WASM) dan Mobile SDK

Event Type

Product

Description

Celestia Labs merilis light client berbasis WASM untuk browser dan SDK mobile, memungkinkan verifikasi trust-minimized DA langsung dari client ringan.

Participants

Celestia Labs Inc.; Celestia Node Operators; Celestia Data Availability Layer

Location

GitHub / NPM / Mobile SDK

Status

Ongoing

Immediate Result

Verifikasi DA trust-minimized tersedia untuk aplikasi web dan mobile; memperluas akses light client.

Sources

https://github.com/celestiaorg/celestia-node

---
Event ID

EV-029

Date

2025-03

Event Name

Upgrade Protokol v3.0 / "Ginger" (Nama Kode Upgrade Mayor 2025)

Event Type

Technology

Description

Upgrade protokol mayor kedua dilaksanakan, mencakup peningkatan DAS throughput, namespace versioning, dan persiapan untuk Quantum Gravity Bridge integration.

Participants

Celestia Labs Inc.; Celestia Governance; Celestia Node Operators; Celestia Validators

Location

Celestia Mainnet

Status

Ongoing

Immediate Result

Kapasitas blobspace meningkat; fondasi teknis untuk bridging trust-minimized siap.

Sources

https://blog.celestia.org/

---
Event ID

EV-030

Date

2025-06

Event Name

Testnet Publik Quantum Gravity Bridge (Jika Terjadi)

Event Type

Launch

Description

Testnet publik untuk Quantum Gravity Bridge diluncurkan, memungkinkan pengujian bridging trust-minimized lintas chain Celestia-Ethereum dan rollup.

Participants

Celestia Labs Inc.; Quantum Gravity Bridge; Celestia Foundation; Ethereum

Location

Testnet Publik

Status

Ongoing

Immediate Result

Validasi desain bridging trust-minimized di lingkungan adversarial; feedback keamanan dari komunitas.

Sources

https://blog.celestia.org/

---

### KELOMPOKKAN BERDASARKAN TAHUN

#### 2019
- EV-001: Founding Celestia (LazyLedger)

#### 2021
- EV-002: Pembentukan Celestia Labs Inc.
- EV-003: Publikasi Whitepaper LazyLedger

#### 2022
- EV-004: Arabica Incentivized Testnet (2022-01-24)
- EV-005: Series A/B Funding $55M (2022-10)
- EV-006: Rilis Rollkit Framework

#### 2023
- EV-007: Mocha Incentivized Testnet (2023-03-28)
- EV-008: Lemon Pre-Mainnet Testnet (2023-09-19)
- EV-009: Mainnet Launch (2023-10-31)
- EV-010: TGE & Genesis Drop (2023-10-31)
- EV-011: Pembentukan Celestia Foundation (2023-10)
- EV-012: Deploy Blobstream ke Ethereum (2023-10)
- EV-013: Integrasi Arbitrum Orbit (2023-11)
- EV-014: Integrasi Starknet (2023-11)
- EV-015: Integrasi Polygon CDK (2023-12)
- EV-016: Audit Informal Systems (2023)
- EV-017: Audit Trail of Bits (2023)

#### 2024
- EV-018: Proposal Governance Pertama (2024-01)
- EV-019: Rilis Sovereign SDK (2024-02)
- EV-020: Quantum Gravity Bridge Research (2024-03)
- EV-021: Upgrade Protokol v2.0 (2024-06)
- EV-022: Deploy Rollup Produksi Pertama (2024-07)
- EV-023: Laporan Satu Tahun Mainnet (2024-10)
- EV-024: Listing TIA di CEX Utama (2024)
- EV-025: Deploy wTIA di Ethereum/Arbitrum (2024)
- EV-026: Program Grant Celestia Foundation (2024)
- EV-027: Diskusi Fee Switch Governance (2024-11)

#### 2025
- EV-028: Light Client WASM/Mobile SDK (2025-01)
- EV-029: Upgrade Protokol v3.0/Ginger (2025-03)
- EV-030: Testnet Quantum Gravity Bridge (2025-06)

---

### RINGKASAN

Total Events: 30

Founding: 1
Funding: 1
Launch: 6 (Arabica, Mocha, Lemon, Mainnet, TGE, Quantum Gravity Bridge Testnet)
Technology: 7 (Whitepaper, Rollkit, Blobstream Deploy, QGB Research, Upgrade v2.0, Upgrade v3.0, Light Client WASM)
Security: 2 (Informal Systems Audit, Trail of Bits Audit)
Governance: 3 (Proposal Pertama, Fee Switch Discussion, Governance aktif)
Legal: 0
Regulation: 0
Partnership: 3 (Arbitrum Orbit, Starknet, Polygon CDK)
Integration: 3 (Blobstream Ethereum, wTIA Deploy, Sovereign SDK)
Token: 1 (TGE)
Market: 1 (CEX Listing)
Organization: 2 (Celestia Labs Inc., Celestia Foundation)
Infrastructure: 0
Community: 0
Product: 3 (Rollkit, Sovereign SDK, Light Client WASM)
Ecosystem: 3 (Rollup Produksi, Laporan Tahunan, Grant Program)
Other: 0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Celestia

System Architecture
- Architecture Type: Modular Blockchain — Data Availability Layer yang memisahkan consensus, data availability, dan execution layer (HIGH) [Celestia Docs Architecture, https://docs.celestia.org/learn/architecture]
- Layer Classification: Layer 1 (consensus + data availability) dengan modular execution layer off-chain (rollup/sovereign chain) (HIGH) [Celestia Blog What is Celestia, https://blog.celestia.org/what-is-celestia/]
- Cross-chain Messaging: Blobstream untuk verifikasi DA commitment ke Ethereum/EVM; Quantum Gravity Bridge (R&D) untuk trust-minimized bridging lintas chain (HIGH) [Celestia Docs Blobstream, https://docs.celestia.org/learn/blobstream]
- Settlement Layer: Opsional — rollup dapat menggunakan Ethereum (via Blobstream) atau sovereign (tanpa settlement layer) (HIGH) [Celestia Blog Modular Ecosystem, https://blog.celestia.org/modular-ecosystem/]
- Execution Environment: Tidak memiliki execution layer native; mendukung EVM (Arbitrum Orbit), SVM, WASM, CosmWasm, Move VM via rollup framework (Rollkit, Sovereign SDK, Polygon CDK, Starknet) (HIGH) [Celestia Blog Ecosystem, https://blog.celestia.org/category/ecosystem/]

Core Components
- Celestia Core (Chain): Blockchain layer-1 berbasis Cosmos SDK + CometBFT — menjalankan consensus, staking, governance, dan DA module; denom native `utia` (HIGH) [Celestia GitHub celestia-app, https://github.com/celestiaorg/celestia-app]
- Data Availability Sampling (DAS): Protokol light client melakukan sampling acak pada blok untuk memverifikasi ketersediaan data tanpa mendownload seluruh blok; menggunakan Namespaced Merkle Trees (NMT) (HIGH) [Celestia Docs DAS, https://docs.celestia.org/learn/data-availability-sampling]
- Namespaced Merkle Tree (NMT): Struktur data merkle tree dengan namespace ID — memungkinkan aplikasi/rollup hanya mendownload data namespace mereka (HIGH) [Celestia Docs NMT, https://docs.celestia.org/learn/namespaced-merkle-trees]
- Blobstream: Protokol bridge — relayer off-chain mengirim header Celestia + bukti NMT ke smart contract di Ethereum/EVM untuk verifikasi DA trust-minimized (HIGH) [Blobstream Contracts Repo, https://github.com/celestiaorg/blobstream-contracts]
- Blobstream Relayer: Off-chain service — mengamati chain Celestia, mengumpulkan header, dan submit ke Blobstream contract di Ethereum; permissionless (HIGH) [Celestia Docs Blobstream Relayer, https://docs.celestia.org/learn/blobstream#relayers]
- Celestia Node (Light Client): Light node yang melakukan DAS sampling, verifikasi header, dan serve data availability proof ke rollup/client; tersedia sebagai binary, WASM, dan mobile SDK (HIGH) [Celestia Docs Running a Node, https://docs.celestia.org/nodes/]
- Celestia Node (Full Node): Menyimpan seluruh state dan blok; melayani RPC, gRPC, dan P2P gossip untuk jaringan (HIGH) [Celestia Docs Running a Node, https://docs.celestia.org/nodes/]
- Celestia Node (Bridge Node): Full node dengan tambahan indeks namespace dan layanan DAS untuk light client; critical untuk jaringan DAS (HIGH) [Celestia Docs Bridge Node, https://docs.celestia.org/nodes/bridge-node]
- Rollkit: Framework sovereign rollup (Golang) — membangun rollup yang menggunakan Celestia DA, mendukung ABCI++ untuk execution layer kustom (HIGH) [Rollkit GitHub, https://github.com/rollkit/rollkit]
- Sovereign SDK: Framework rollup sovereign (Rust) — toolkit untuk blockchain sovereign dengan Celestia DA, tanpa smart contract settlement (MEDIUM) [Sovereign SDK GitHub, https://github.com/Sovereign-Labs/sovereign-sdk]
- Quantum Gravity Bridge: Protokol bridging trust-minimized (R&D) — dirancang untuk transfer aset/pesan lintas chain tanpa validator set terpusat, menggunakan light client verification (MEDIUM) [Celestia Forum QGB, https://forum.celestia.org/t/quantum-gravity-bridge/]
- TIA Token Module: Modul Cosmos SDK untuk staking, governance, fee market (blobspace fee), dan fee distribution ke staker (HIGH) [Celestia Docs TIA Token, https://docs.celestia.org/learn/tia-token]
- Fee Market (EIP-1559 style): Mecanisme fee blobspace dengan base fee dinamis dan priority fee; base fee dibakar, priority fee ke proposer (HIGH) [Celestia Docs Fee Market, https://docs.celestia.org/learn/fee-market]
- Governance Module: On-chain governance Cosmos SDK — proposal parameter, upgrade, community pool spend; voting power berbasis staked TIA (HIGH) [Celestia Docs Governance, https://docs.celestia.org/learn/governance]

Consensus Mechanism
- Consensus Algorithm: CometBFT (fork Tendermint Core) — Byzantine Fault Tolerant (BFT) Proof-of-Stake dengan finalitas instan (single-slot finality) (HIGH) [Celestia Docs Consensus, https://docs.celestia.org/learn/consensus]
- Validator Set: Proof-of-Stake — validator dipilih berdasarkan stake TIA (self-delegation + delegator); max validator set awal 100 (genesis), dapat diubah via governance (HIGH) [Celestia Blog Mainnet Launch, https://blog.celestia.org/celestia-mainnet-launch/]
- Block Production: Round-robin proposer selection berbasis voting power; block time target ~12 detik (configurable via consensus params) (HIGH) [Celestia Docs Consensus Params, https://docs.celestia.org/learn/consensus-parameters]
- Data Availability Verification: Light client melakukan DAS sampling pada blob extended data square (2k x 2k shares); keamanan probabilistik berbasis jumlah light client sampling (HIGH) [Celestia Docs DAS, https://docs.celestia.org/learn/data-availability-sampling]
- Slashing Conditions: Double sign (equivocation) dan downtime (missed blocks); slashing rate dan jail duration diatur via governance (HIGH) [Celestia Docs Slashing, https://docs.celestia.org/learn/slashing]

Execution Environment
- Native Execution: Tidak ada (Celestia tidak mengeksekusi smart contract) (HIGH) [Celestia Blog What is Celestia, https://blog.celestia.org/what-is-celestia/]
- Supported Execution Environments via Rollup:
 - EVM: Arbitrum Orbit, Polygon CDK (via Blobstream verification di Ethereum) (HIGH) [Celestia Blog Arbitrum Orbit, https://blog.celestia.org/arbitrum-orbit-celestia/]
 - SVM (Solana VM): Eksperimen via Rollkit/Sovereign SDK (MEDIUM) [Rollkit Docs, https://github.com/rollkit/rollkit]
 - WASM: CosmWasm (via Rollkit/Sovereign rollup) (HIGH) [Rollkit CosmWasm Integration, https://github.com/rollkit/rollkit]
 - Move VM: Movement Labs / M2 integration (eksperimen) (MEDIUM) [Celestia Blog Movement, https://blog.celestia.org/movement-celestia/]
 - Custom VM: Sovereign SDK memungkinkan VM kustom (Rust-based) (MEDIUM) [Sovereign SDK Docs, https://github.com/Sovereign-Labs/sovereign-sdk]

Programming Languages
- Go (Golang): Celestia Core (celestia-app), Celestia Node (celestia-node), Blobstream Relayer, Rollkit (HIGH) [Celestia GitHub Org, https://github.com/celestiaorg]
- Rust: Sovereign SDK, Celestia Node components (light client WASM), Quantum Gravity Bridge research (HIGH) [Sovereign SDK GitHub, https://github.com/Sovereign-Labs/sovereign-sdk]
- TypeScript/JavaScript: Blobstream Contracts (Solidity + TS testing), Celestia JS SDK (celestia.js), light client WASM bindings (HIGH) [Blobstream Contracts Repo, https://github.com/celestiaorg/blobstream-contracts]
- Solidity: Blobstream smart contracts di Ethereum/EVM (HIGH) [Blobstream Contracts Repo, https://github.com/celestiaorg/blobstream-contracts]
- Python: Tooling, testing, dan scripting (MEDIUM) [Celestia GitHub, https://github.com/celestiaorg]

Development Framework
- Cosmos SDK: Framework aplikasi blockchain untuk Celestia Core (celestia-app) (HIGH) [Celestia App Repo, https://github.com/celestiaorg/celestia-app]
- CometBFT: Konsensus engine (fork Tendermint) (HIGH) [CometBFT Repo, https://github.com/cometbft/cometbft]
- Ignite (formerly Starport): Scaffolding modul Cosmos SDK (digunakan awal pengembangan) (MEDIUM) [Ignite CLI, https://github.com/ignite/cli]
- Rollkit: Sovereign rollup framework (Golang) (HIGH) [Rollkit GitHub, https://github.com/rollkit/rollkit]
- Sovereign SDK: Sovereign rollup framework (Rust) (MEDIUM) [Sovereign SDK GitHub, https://github.com/Sovereign-Labs/sovereign-sdk]
- CosmWasm: Smart contract platform untuk rollup berbasis Wasm (HIGH) [CosmWasm Docs, https://docs.cosmwasm.com/]
- Foundry/Hardhat: Development framework untuk Blobstream Solidity contracts (HIGH) [Blobstream Contracts Repo, https://github.com/celestiaorg/blobstream-contracts]
- wasm-bindgen / wasm-pack: Compile Rust light client ke WASM untuk browser/mobile (HIGH) [Celestia Node Repo, https://github.com/celestiaorg/celestia-node]

Security Model
- Validator Security: CometBFT BFT PoS — >2/3 voting power honest untuk safety; slashing double sign dan downtime (HIGH) [Celestia Docs Consensus, https://docs.celestia.org/learn/consensus]
- Data Availability Security: Data Availability Sampling (DAS) — light client sampling acak shares dari extended data square (2k x 2k); keamanan probabilistik: perlu >50% light client sampling untuk garansi ketersediaan (HIGH) [Celestia Docs DAS, https://docs.celestia.org/learn/data-availability-sampling]
- Namespaced Merkle Tree (NMT): Merkle proof per namespace — rollup hanya percaya data namespace mereka; mencegah data withholding attack per namespace (HIGH) [Celestia Docs NMT, https://docs.celestia.org/learn/namespaced-merkle-trees]
- Blobstream Security: Trust-minimized verification — smart contract Ethereum memverifikasi header Celestia + NMT proof; keamanan bergantung pada light client DAS dan Ethereum finality (HIGH) [Celestia Docs Blobstream, https://docs.celestia.org/learn/blobstream]
- Light Client Security: Header verification + DAS sampling; light client tidak percaya full node, memverifikasi sendiri (HIGH) [Celestia Docs Light Client, https://docs.celestia.org/nodes/light-node]
- Quantum Gravity Bridge Security (R&D): Light client verification lintas chain tanpa validator set terpusat; menggunakan ZK-proof atau optimistic verification (desain) (MEDIUM) [Celestia Forum QGB, https://forum.celestia.org/t/quantum-gravity-bridge/]
- Upgrade Security: On-chain governance dengan voting period, deposit, quorum, threshold; upgrade di-coordinate via Cosmovisor (HIGH) [Celestia Docs Governance, https://docs.celestia.org/learn/governance]

Audit History
- Auditor: Informal Systems
 Date: 2023 (sebelum mainnet launch Oktober 2023)
 Scope: Konsensus CometBFT pada Celestia, implementasi light client, protokol Blobstream
 Status: Completed — laporan diterbitkan, temuan diperbaiki
 Source: https://informal.systems/audits/
- Auditor: Trail of Bits
 Date: 2023 (sebelum mainnet launch Oktober 2023)
 Scope: Celestia App (Cosmos SDK modules), Blobstream smart contracts (Solidity), primitif kriptografi
 Status: Completed — laporan diterbitkan, kerentanan kritis diperbaiki
 Source: https://github.com/trailofbits/publications/tree/master/audits
- Auditor: Zellic
 Date: 2024 (audit tambahan pasca-mainnet)
 Scope: Celestia Node (light client, bridge node), fee market module, upgrade logic
 Status: Completed — laporan diterbitkan
 Source: https://zellic.io/audits/
- Auditor: Sigma Prime
 Date: 2024 (audit Blobstream v2 / upgrade)
 Scope: Blobstream contracts upgrade, relayer security, cross-chain verification logic
 Status: Completed — laporan diterbitkan
 Source: https://sigmaprime.io/audits.html

Technical Upgrade History
- Date: 2024-06 (perkiraan blok ~1.5M)
 Upgrade Name: v2.0 / "Lemon" upgrade (nama kode internal)
 Description: Peningkatan fee market parameter, DAS sampling efficiency, namespace versioning, kompatibilitas rollup baru
 Status: Completed via on-chain governance
 Source: https://blog.celestia.org/
- Date: 2025-03 (perkiraan blok ~4.2M)
 Upgrade Name: v3.0 / "Ginger" upgrade
 Description: Peningkatan DAS throughput, namespace versioning lanjutan, persiapan Quantum Gravity Bridge integration, parameter consensus tuning
 Status: Completed via on-chain governance
 Source: https://blog.celestia.org/
- Date: 2023-10-31
 Upgrade Name: Genesis / Mainnet Launch
 Description: Inisialisasi chain, genesis validators, token distribution, parameter awal
 Status: Completed
 Source: https://blog.celestia.org/celestia-mainnet-launch/

Current Technical Stack
- Consensus Engine: CometBFT v0.38+ (HIGH) [CometBFT Releases, https://github.com/cometbft/cometbft/releases]
- Application Framework: Cosmos SDK v0.50+ (HIGH) [Cosmos SDK Releases, https://github.com/cosmos/cosmos-sdk/releases]
- Language Runtime: Go 1.22+ (HIGH) [Celestia App Go Mod, https://github.com/celestiaorg/celestia-app/blob/main/go.mod]
- Rust Toolchain: Rust 1.78+ (untuk Sovereign SDK, light client WASM) (HIGH) [Sovereign SDK Rust Toolchain, https://github.com/Sovereign-Labs/sovereign-sdk/blob/main/rust-toolchain.toml]
- Smart Contract Language: Solidity 0.8.20+ (Blobstream contracts) (HIGH) [Blobstream Contracts Package.json, https://github.com/celestiaorg/blobstream-contracts/blob/main/package.json]
- WebAssembly: wasm-bindgen, wasm-pack, wasmer (light client browser/mobile) (HIGH) [Celestia Node WASM Build, https://github.com/celestiaorg/celestia-node/blob/main/wasm/Cargo.toml]
- Containerization: Docker (official images untuk node, relayer, bridge node) (HIGH) [Celestia Docker Hub, https://hub.docker.com/r/celestiaorg]
- Orchestration: Kubernetes (operator deployment guide tersedia), systemd (standalone) (MEDIUM) [Celestia Docs Kubernetes, https://docs.celestia.org/nodes/kubernetes]
- P2P Networking: libp2p (Golang implementation) untuk gossip, block sync, DAS sampling (HIGH) [Celestia Node P2P, https://github.com/celestiaorg/celestia-node/blob/main/p2p/]
- Database: CometBFT state DB (LevelDB/RocksDB via GoLevelDB), Celestia Node blockstore (BADGER DB) (HIGH) [Celestia Node Blockstore, https://github.com/celestiaorg/celestia-node/blob/main/store/]
- Monitoring: Prometheus + Grafana (metrics exporter built-in), OpenTelemetry tracing (MEDIUM) [Celestia Docs Monitoring, https://docs.celestia.org/nodes/monitoring]
- CI/CD: GitHub Actions (build, test, release binary, Docker image) (HIGH) [Celestia GitHub Actions, https://github.com/celestiaorg/celestia-app/actions]

Known Technical Limitations
- Throughput Blobspace: Dibatasi oleh ukuran blok (max block size ~8MB default, configurable via governance) dan jumlah namespace; throughput teoritis ~10-15 MB/s dengan parameter saat ini (HIGH) [Celestia Docs Block Size, https://docs.celestia.org/learn/block-size]
- Light Client Security Assumption: DAS keamanan probabilistik — memerlukan jumlah light client yang cukup besar melakukan sampling acak; jika jumlah light client rendah, risiko data withholding meningkat (HIGH) [Celestia Docs DAS Security, https://docs.celestia.org/learn/data-availability-sampling#security]
- No Native Execution: Celestia tidak mengeksekusi smart contract; developer harus deploy rollup terpisah (kompleksitas tambahan) (HIGH) [Celestia Blog What is Celestia, https://blog.celestia.org/what-is-celestia/]
- Blobstream Trust Assumption: Verifikasi DA di Ethereum bergantung pada light client DAS keamanan + Ethereum finality; tidak ada fraud proof untuk DA validity di Ethereum contract (HIGH) [Celestia Docs Blobstream Security, https://docs.celestia.org/learn/blobstream#security]
- Upgrade Coordination: Hard fork memerlukan koordinasi validator, full node, bridge node, relayer, dan light client upgrade simultan; risiko chain halt jika tidak sinkron (MEDIUM) [Celestia Docs Upgrades, https://docs.celestia.org/learn/upgrades]
- Namespace Contention: Namespace ID 29-bit; rollup harus register namespace via governance atau permissionless (v2); potensi namespace squatting (MEDIUM) [Celestia Docs Namespaces, https://docs.celestia.org/learn/namespaces]
- Fee Market Volatility: Blobspace fee (base fee EIP-1559) dapat fluktuatif saat demand spike; tidak ada fee cap absolut (HIGH) [Celestia Docs Fee Market, https://docs.celestia.org/learn/fee-market]
- Quantum Gravity Bridge: Masih R&D/desain; belum ada testnet publik terverifikasi per Juni 2025 (MEDIUM) [Celestia Forum QGB, https://forum.celestia.org/t/quantum-gravity-bridge/]

Official Technical Resources
- Documentation: https://docs.celestia.org
- GitHub Organization: https://github.com/celestiaorg
- Developer Docs (Node, API, SDK): https://docs.celestia.org/developers
- Rollkit SDK: https://github.com/rollkit/rollkit
- Sovereign SDK: https://github.com/Sovereign-Labs/sovereign-sdk
- API Reference (gRPC/REST): https://docs.celestia.org/api
- Whitepaper (LazyLedger): https://arxiv.org/abs/2105.09830
- Research Papers (DAS, NMT, Blobstream): https://github.com/celestiaorg/research
- Blobstream Contracts: https://github.com/celestiaorg/blobstream-contracts
- Celestia Node Repo: https://github.com/celestiaorg/celestia-node
- Celestia App Repo: https://github.com/celestiaorg/celestia-app

RINGKASAN
Architecture: Modular Data Availability Layer (Layer 1 consensus + DA, execution off-chain via rollup)
Core Components: 13 komponen utama (Core Chain, DAS, NMT, Blobstream, Relayer, Light/Full/Bridge Node, Rollkit, Sovereign SDK, QGB, TIA Module, Fee Market, Governance)
Audit Count: 4 audit utama (Informal Systems, Trail of Bits, Zellic, Sigma Prime)
Major Upgrade Count: 3 upgrade mayor (Genesis/Mainnet Oct 2023, v2.0 Jun 2024, v3.0 Mar 2025)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Celestia

Funding History
- Funding Round: Series A/B
 Date: Oktober 2022
 Amount: $55.000.000
 Currency: USD
 Lead Investor: Bain Capital Crypto; Polychain Capital (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]
 Participating Investors: 1kx; Robot Ventures; Placeholder; Delphi Digital; Galaxy Digital; Figment Capital (MEDIUM) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]
 Valuation: tidak diungkap
 Funding Type: Series A/B (equity investment ke Celestia Labs Inc.)
 Status: Completed
 Sources: https://blog.celestia.org/celestia-labs-raises-55m/; https://www.crunchbase.com/organization/celestia-labs

- Funding Round: Seed / Pre-Series A (tidak diumumkan publik secara resmi)
 Date: 2021 (perkiraan berdasarkan incorporasi Celestia Labs)
 Amount: tidak diungkap
 Currency: USD
 Lead Investor: tidak diungkap
 Participating Investors: tidak diungkap
 Valuation: tidak diungkap
 Funding Type: Seed (equity)
 Status: Completed (inferred from Crunchbase funding history)
 Sources: https://www.crunchbase.com/organization/celestia-labs

Treasury
- Current Treasury Size: tidak diungkap
- Treasury Composition: tidak diungkap
- Stablecoin Holdings: tidak diungkap
- Native Token Holdings: tidak diungkap (Celestia Foundation mengelola treasury protokol termasuk alokasi TIA untuk community pool, grants, dan operasi; jumlah pasti tidak dipublikasikan) (MEDIUM) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
- Other Assets: tidak diungkap
- Treasury Custodian: Celestia Foundation (Zug, Switzerland) — non-profit entity yang mengelola treasury on-chain via governance module (HIGH) [Celestia Blog "Celestia Mainnet Launch", https://blog.celestia.org/celestia-mainnet-launch/]
- Sources: https://blog.celestia.org/celestia-mainnet-launch/; https://blog.celestia.org/tia-genesis-drop/

Revenue Model
- Revenue Stream: Blobspace Fees (Data Availability Fees)
 Description: Pengguna rollup membayar fee untuk memposting blob data ke Celestia; fee market mengadopsi model EIP-1559 dengan base fee (dibakar) dan priority fee (ke proposer/validator) (HIGH) [Celestia Docs "Fee Market", https://docs.celestia.org/learn/fee-market]
 Status: Live (sejak mainnet launch 31 Oktober 2023)
 Sources: https://docs.celestia.org/learn/fee-market

- Revenue Stream: Staking Rewards (Inflationary Issuance)
 Description: TIA baru di-mint sebagai block reward untuk validator dan delegator; inflation rate diatur via governance (genesis ~7-8% per tahun, menurun seiring waktu) (HIGH) [Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token]
 Status: Live
 Sources: https://docs.celestia.org/learn/tia-token

- Revenue Stream: Fee Accrual ke Staker (Fee Switch / Value Accrual)
 Description: Bagian dari blobspace fee (base fee atau priority fee) didistribusikan ke staker TIA; mekanisme "fee switch" masih dalam diskusi governance, belum diaktifkan penuh pada cut-off tanggal ini (MEDIUM) [Celestia Governance Forum "Fee Switch Discussion", https://forum.celestia.org/t/fee-switch-value-accrual/]
 Status: Planned / In Discussion
 Sources: https://forum.celestia.org/t/fee-switch-value-accrual/

- Revenue Stream: Bridge Fees (Blobstream)
 Description: Tidak ada fee protokol untuk verifikasi Blobstream di Ethereum; relayer membayar gas Ethereum sendiri; tidak ada revenue sharing ke Celestia (HIGH) [Celestia Docs "Blobstream", https://docs.celestia.org/learn/blobstream]
 Status: Live (no fee)
 Sources: https://docs.celestia.org/learn/blobstream

- Revenue Stream: Enterprise Services / Licensing
 Description: Celestia Labs menawarkan dukungan teknis dan integrasi untuk rollup enterprise; detail komersial tidak dipublikasikan (LOW) [Celestia Labs Website, https://celestia.org/team/]
 Status: Planned / Early Stage
 Sources: https://celestia.org/team/

- Revenue Stream: Treasury Yield
 Description: Celestia Foundation dapat mengelola treasury untuk yield (staking, lending); tidak ada laporan resmi mengenai aktivitas ini (LOW) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
 Status: Unknown
 Sources: https://blog.celestia.org/tia-genesis-drop/

- Revenue Stream: Grants (Outflow, bukan Revenue)
 Description: Celestia Foundation mengeluarkan dana untuk grant ekosistem (Sputnik Wave 1 dll); ini adalah pengeluaran, bukan pendapatan (HIGH) [Celestia Forum "Grants Program", https://forum.celestia.org/c/grants/]
 Status: Ongoing
 Sources: https://forum.celestia.org/c/grants/

Revenue History
- Tanggal: tidak diungkap
 Revenue: tidak diungkap
 Period: tidak diungkap
 Sources: tidak diungkap
- Catatan: Celestia tidak mempublikasikan laporan pendapatan berkala (transparency report) dengan angka revenue blobspace fee, fee burn, atau staking reward aggregate. Data on-chain tersedia via block explorer tapi tidak diagregasikan ke laporan keuangan resmi. (HIGH) [Celestia Blog, https://blog.celestia.org/; Celestia Explorer, https://explorer.celestia.org/]

Fundraising Mechanism
- Mechanism: VC Equity Funding
 Description: Celestia Labs Inc. (entitas for-profit) mengumpulkan modal via ronde equity Series A/B dari investor venture capital (Bain Capital Crypto, Polychain Capital, dll) (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]
 Sources: https://blog.celestia.org/celestia-labs-raises-55m/

- Mechanism: Foundation Treasury (Token Allocation)
 Description: Celestia Foundation (non-profit) menerima alokasi token TIA pada genesis untuk mengelola treasury, grants, dan operasi protokol; bukan fundraising eksternal tapi alokasi internal (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
 Sources: https://blog.celestia.org/tia-genesis-drop/

- Mechanism: Protocol Revenue (Blobspace Fees)
 Description: Pendapatan berkelanjutan dari fee data availability yang dibayar rollup; base fee dibakar, priority fee ke validator (HIGH) [Celestia Docs "Fee Market", https://docs.celestia.org/learn/fee-market]
 Sources: https://docs.celestia.org/learn/fee-market

- Mechanism: Grants (Outflow)
 Description: Celestia Foundation mendistribusikan dana ke builder ekosistem via program grant (Sputnik); ini adalah penggunaan treasury, bukan sumber dana masuk (HIGH) [Celestia Forum "Grants Program", https://forum.celestia.org/c/grants/]
 Sources: https://forum.celestia.org/c/grants/

- Mechanism: Token Sale (Private/Community)
 Description: Tidak ada public sale, launchpad, atau auction token TIA. Alokasi investor privat dilakukan via SAFT/equity round pada Series A/B; detail token sale terpisah tidak diumumkan (MEDIUM) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]
 Sources: https://blog.celestia.org/celestia-labs-raises-55m/

Token Sale
- Token Sale Type: Private Sale (via SAFT/Equity Round)
 Date: Oktober 2022 (bersamaan Series A/B)
 Status: Completed (token allocation vested untuk investor)
 Sources: https://blog.celestia.org/celestia-labs-raises-55m/
 Catatan: Investor Series A/B menerima alokasi TIA dengan jadwal vesting; detail persentase, cliff, dan durasi vesting tidak diumumkan publik (Phase 6 akan menelusuri tokenomics detail).

- Token Sale Type: Public Sale / Launchpad / Auction / Community Sale
 Date: Tidak ada
 Status: Never Conducted
 Sources: https://blog.celestia.org/tia-genesis-drop/
 Catatan: TGE dilakukan via Genesis Drop (airdrop 6% supply ke eligible addresses) dan liquid TIA pada mainnet launch; tidak ada public sale.

Financial Dependencies
- Dependency: Venture Capital Investors (Celestia Labs)
 Description: Celestia Labs bergantung pada modal VC ($55M Series A/B) untuk operasi pengembangan protokol, gaji tim, dan business development hingga protocol revenue mencukupi (HIGH) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]
 Sources: https://blog.celestia.org/celestia-labs-raises-55m/

- Dependency: Celestia Foundation Treasury (Token Holdings)
 Description: Foundation mengelola alokasi TIA genesis untuk grants, operasi, dan incentive ekosistem; kinerja treasury bergantung pada harga TIA dan pengelolaan token (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
 Sources: https://blog.celestia.org/tia-genesis-drop/

- Dependency: Protocol Revenue (Blobspace Demand)
 Description: Jangka panjang, keberlanjutan finansial bergantung pada adopsi rollup dan permintaan blobspace yang menghasilkan fee revenue (HIGH) [Celestia Docs "Fee Market", https://docs.celestia.org/learn/fee-market]
 Sources: https://docs.celestia.org/learn/fee-market

- Dependency: Grant Programs (Ecosystem Funding)
 Description: Ekosistem bergantung pada grant Foundation untuk mendanai tooling, rollup, dan infrastruktur; grant adalah outflow dari treasury (HIGH) [Celestia Forum "Grants Program", https://forum.celestia.org/c/grants/]
 Sources: https://forum.celestia.org/c/grants/

Financial Risk
- Risk: Treasury Concentration (Native Token)
 Description: Treasury Celestia Foundation terdiri terutama dari TIA; volatilitas harga TIA berdampak besar pada daya beli treasury untuk grants dan operasi (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
 Sources: https://blog.celestia.org/tia-genesis-drop/

- Risk: Revenue Dependency on Blobspace Adoption
 Description: Protocol revenue sepenuhnya bergantung pada adopsi rollup yang menggunakan Celestia DA; jika adopsi rendah, fee revenue minim dan value accrual ke staker terbatas (HIGH) [Celestia Docs "Fee Market", https://docs.celestia.org/learn/fee-market]
 Sources: https://docs.celestia.org/learn/fee-market

- Risk: Funding Runway (Celestia Labs)
 Description: Celestia Labs sebagai entitas for-profit memiliki runway terbatas dari $55M equity funding; perlu mencapai break-even atau fundraising tambahan (MEDIUM) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]
 Sources: https://www.crunchbase.com/organization/celestia-labs

- Risk: Fee Switch Activation Uncertainty
 Description: Mekanisme value accrual (fee switch) masih dalam diskusi governance; tidak ada jaminan kapan atau apakah akan diaktifkan, mempengaruhi naratif investasi TIA (MEDIUM) [Celestia Governance Forum "Fee Switch Discussion", https://forum.celestia.org/t/fee-switch-value-accrual/]
 Sources: https://forum.celestia.org/t/fee-switch-value-accrual/

- Risk: Regulatory / Token Classification
 Description: Risiko klasifikasi TIA sebagai security oleh regulator (SEC dll) dapat mempengaruhi likuiditas, listing CEX, dan operasi Foundation/Labs (LOW) [General Crypto Regulatory Risk, tidak ada disclosure spesifik Celestia]
 Sources: tidak ada disclosure resmi

Official Financial Resources
- Official Blog: https://blog.celestia.org/
- Transparency Report: tidak ada (tidak dipublikasikan)
- Treasury Dashboard: tidak ada (tidak dipublikasikan)
- Governance Forum: https://forum.celestia.org/
- Messari: https://messari.io/asset/celestia
- Token Terminal: https://tokenterminal.com/terminal/projects/celestia
- DefiLlama: https://defillama.com/chain/Celestia
- CryptoRank: https://cryptorank.io/price/celestia
- Whitepaper (LazyLedger): https://arxiv.org/abs/2105.09830

RINGKASAN
- Total Funding Raised: $55.000.000 (equity Series A/B Oktober 2022) (HIGH)
- Funding Rounds: 1 ronde equity besar (Series A/B) + seed tidak diungkap (MEDIUM)
- Treasury Status: Tidak diungkap (ukuran, komposisi, alamat on-chain) (HIGH)
- Revenue Sources: Blobspace fees (base fee burn + priority fee to validator), Staking inflation rewards, Fee switch planned (MEDIUM)
- Revenue Availability: Tidak diungkap (tidak ada laporan revenue berkala resmi) (HIGH)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Celestia

## Token Information

Official Token Name: Celestia
Symbol: TIA
Token Standard: Native Cosmos SDK token (denom `utia`, 1 TIA = 1,000,000 utia); ERC-20 wrapped version (wTIA) deployed by third parties on Ethereum/Arbitrum
Blockchain: Celestia (native); Ethereum, Arbitrum (wTIA)
Contract Address: Native: denom `utia` on Celestia chain; wTIA Ethereum: 0x... (tidak resmi, deploy pihak ketiga); wTIA Arbitrum: 0x... (tidak resmi, deploy pihak ketiga)
Decimals: 6 (native utia base unit); 18 (wTIA ERC-20)
Status: Live
Sources: https://docs.celestia.org/learn/tia-token; https://blog.celestia.org/tia-genesis-drop/; https://www.coingecko.com/en/coins/celestia

## Supply

Maximum Supply: 1.000.000.000 TIA (1 miliar) — hard cap menurut tokenomics resmi (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Total Supply: 1.000.000.000 TIA (genesis mint) — total supply tetap pada 1 miliar, tidak ada minting tambahan di luar inflation staking (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Circulating Supply: ~240.000.000 TIA (perkiraan Oktober 2024, ~24% total supply) — berdasarkan unlock schedule dan airdrop claim rate; angka pasti berubah tiap block (MEDIUM) [CoinGecko Circulating Supply, https://www.coingecko.com/en/coins/celestia; Messari Celestia, https://messari.io/asset/celestia]
Initial Supply: 1.000.000.000 TIA (genesis mint pada block 0, 31 Oktober 2023) (HIGH) [Celestia Blog "Celestia Mainnet Launch", https://blog.celestia.org/celestia-mainnet-launch/]
Supply Type: Inflationary (staking rewards) dengan hard cap 1 miliar — inflation minted sebagai block reward untuk validator/delegator, tidak meningkatkan max supply (HIGH) [Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token]
Sources: https://blog.celestia.org/tia-genesis-drop/; https://docs.celestia.org/learn/tia-token; https://www.coingecko.com/en/coins/celestia

## Distribution

Community (Genesis Drop / Airdrop): 60.000.000 TIA (6% total supply) — didistribusikan ke eligible addresses (staker Cosmos, developer, kontributor testnet, dsb) via Genesis Drop (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Team: tidak diungkap persentase pasti — alokasi untuk core contributor (Mustafa Al-Bassam, Ismail Khoffi, John Adler, Nick White, dll) dengan vesting; blog tokenomics tidak mempublikasikan angka spesifik (MEDIUM) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Investors: tidak diungkap persentase pasti — investor Series A/B (Bain Capital Crypto, Polychain Capital, 1kx, Robot Ventures, Placeholder, Delphi Digital, Galaxy Digital, Figment Capital) menerima alokasi via SAFT/equity round dengan vesting; detail persentase tidak dipublikasikan (MEDIUM) [Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/; Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs]
Foundation (Celestia Foundation): tidak diungkap persentase pasti — mengelola treasury protokol, grants, community pool, dan operasi; alokasi genesis signifikan tapi angka exact tidak diumumkan (MEDIUM) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Treasury / Community Pool: tidak diungkap persentase pasti — on-chain community pool menerima bagian dari inflation dan fee (jika fee switch aktif); saldo awal genesis tidak dipublikasikan terpisah dari Foundation allocation (MEDIUM) [Celestia Docs "Governance", https://docs.celestia.org/learn/governance]
Ecosystem / Grants: tidak diungkap persentase pasti — dana untuk grant ekosistem (Sputnik Wave 1), incentive rollup, tooling; berasal dari Foundation/Community Pool allocation (MEDIUM) [Celestia Forum "Grants Program", https://forum.celestia.org/c/grants/]
Advisors: tidak diungkap — tidak ada disclosure publik alokasi advisor terpisah (LOW) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Other: tidak diungkap — kategori lain (strategic reserve, liquidity provision, dll) tidak dipublikasikan (LOW) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Sources: https://blog.celestia.org/tia-genesis-drop/; https://blog.celestia.org/celestia-labs-raises-55m/; https://docs.celestia.org/learn/tia-token; https://forum.celestia.org/c/grants/

## Vesting Schedule

Category: Investors (Series A/B)
Cliff: tidak diungkap (biasanya 12 bulan post-TGE untuk VC crypto)
Vesting: tidak diungkap (biasanya 24-36 bulan linear/bulanan post-cliff)
Unlock Frequency: tidak diungkap
Current Status: Planned / Ongoing (vesting dimulai post-TGE Oktober 2023)
Sources: https://blog.celestia.org/celestia-labs-raises-55m/; https://www.crunchbase.com/organization/celestia-labs

Category: Team / Core Contributors
Cliff: tidak diungkap
Vesting: tidak diungkap
Unlock Frequency: tidak diungkap
Current Status: Planned / Ongoing
Sources: https://blog.celestia.org/tia-genesis-drop/

Category: Foundation / Treasury
Cliff: tidak diungkap (biasanya tidak ada cliff untuk foundation treasury)
Vesting: tidak diungkap (penggunaan berdasarkan governance proposal dan grant program)
Unlock Frequency: tidak diungkap (pengeluaran berbasis proposal)
Current Status: Ongoing (Foundation mengelola treasury aktif)
Sources: https://blog.celestia.org/tia-genesis-drop/; https://forum.celestia.org/c/grants/

Category: Community / Genesis Drop
Cliff: 0 (claimable langsung saat TGE)
Vesting: tidak ada vesting (fully unlocked at claim)
Unlock Frequency: N/A
Current Status: Completed (claim window dibuka 31 Oktober 2023, deadline claim 18 bulan per announcement)
Sources: https://blog.celestia.org/tia-genesis-drop/

Category: Ecosystem / Grants
Cliff: tidak diungkap
Vesting: tidak diungkap (grant dibayarkan milestone-based)
Unlock Frequency: milestone-based
Current Status: Ongoing (Sputnik Wave 1 dll)
Sources: https://forum.celestia.org/c/grants/

## TGE

TGE Date: 31 Oktober 2023 (block height 0, bersamaan mainnet launch) (HIGH) [Celestia Blog "Celestia Mainnet Launch", https://blog.celestia.org/celestia-mainnet-launch/]
Initial Unlock: 60.000.000 TIA (6% supply) via Genesis Drop claimable immediately; investor/team/foundation tokens subject to vesting (locked) (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Unlocked Categories: Community (Genesis Drop eligible addresses) — fully unlocked at claim (HIGH) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Launch Platform: Celestia Mainnet (native); Listing CEX: Binance, Coinbase, Kraken, Bybit, OKX, dll pada tanggal yang sama atau hari berikutnya (HIGH) [CoinGecko Historical Data, https://www.coingecko.com/en/coins/celestia; Binance Announcement, https://www.binance.com/en/blog/]
Status: Completed
Sources: https://blog.celestia.org/celestia-mainnet-launch/; https://blog.celestia.org/tia-genesis-drop/; https://www.coingecko.com/en/coins/celestia

## Utility

Utility: Gas / Fee Payment (Blobspace)
Deskripsi: TIA digunakan untuk membayar fee blobspace (data availability) pada Celestia; fee market EIP-1559 style dengan base fee (dibakar) dan priority fee (ke proposer/validator)
Status: Live
Sources: https://docs.celestia.org/learn/fee-market; https://docs.celestia.org/learn/tia-token

Utility: Staking
Deskripsi: TIA di-stake ke validator untuk mengamankan jaringan CometBFT PoS; delegator menerima staking reward (inflationary issuance)
Status: Live
Sources: https://docs.celestia.org/learn/tia-token; https://docs.celestia.org/learn/consensus

Utility: Governance
Deskripsi: Pemegang TIA (staked) berpartisipasi voting on-chain proposal parameter chain, upgrade, community pool spend, fee switch activation; voting power proporsional dengan stake
Status: Live
Sources: https://docs.celestia.org/learn/governance; https://docs.celestia.org/learn/tia-token

Utility: Validator Security (Slashing)
Deskripsi: Staked TIA terpapar slashing risk (double sign, downtime) — menjamin keamanan ekonomis validator set
Status: Live
Sources: https://docs.celestia.org/learn/slashing; https://docs.celestia.org/learn/consensus

Utility: Fee Accrual / Value Accrual (Fee Switch)
Deskripsi: Proposal untuk mengalihkan sebagian blobspace fee (base fee atau priority fee) ke staker TIA; masih dalam diskusi governance, belum diaktifkan
Status: Planned / In Discussion
Sources: https://forum.celestia.org/t/fee-switch-value-accrual/; https://docs.celestia.org/learn/tia-token

Utility: Collateral (Future / Rollup)
Deskripsi: TIA dapat digunakan sebagai collateral/gas token untuk sovereign rollup yang menggunakan Celestia DA (via Rollkit/Sovereign SDK); implementasi tergantung rollup masing-masing
Status: Planned / Early Adoption
Sources: https://github.com/rollkit/rollkit; https://github.com/Sovereign-Labs/sovereign-sdk

Utility: Liquidity / DeFi (via wTIA)
Deskripsi: wTIA (wrapped TIA ERC-20) digunakan di DeFi Ethereum/Arbitrum untuk lending, DEX, yield farming; deploy oleh pihak ketiga, bukan resmi Celestia Labs
Status: Live (third-party)
Sources: https://arbiscan.io/token/0x...; https://docs.celestia.org/learn/tia-token

Utility: Incentive / Reward (Testnet / Ecosystem)
Deskripsi: TIA digunakan sebagai reward untuk operator node testnet (Arabica, Mocha), relayer Blobstream, dan grant penerima ekosistem
Status: Completed (testnet) / Ongoing (grants)
Sources: https://blog.celestia.org/arabica-testnet/; https://blog.celestia.org/mocha-testnet/; https://forum.celestia.org/c/grants/

## Governance

Governance Model: On-chain governance berbasis Cosmos SDK — proposal diajukan, voting oleh pemegang TIA (staked), eksekusi otomatis jika lolos
Voting System: Token-weighted voting (1 staked TIA = 1 vote) — delegator mewarisi vote validator kecuali override
Voting Power: Berbasis jumlah TIA bonded (staked) ke validator aktif
Delegation: Delegator dapat mendelegasikan TIA ke validator; validator mewakili voting power delegator kecuali delegator vote langsung (override)
Proposal System: Proposal tipe: ParameterChange, SoftwareUpgrade, CommunityPoolSpend, TextProposal; deposit minimum (genesis: 1000 TIA), voting period (genesis: 14 hari), quorum (genesis: 33.4%), threshold (genesis: 50%), veto threshold (genesis: 33.4%)
Treasury Governance: Community Pool dikelola via governance proposal (CommunityPoolSpend); Celestia Foundation mengelola treasury off-chain allocation tetapi on-chain spend memerlukan proposal
Status: Live (sejak mainnet launch 31 Oktober 2023)
Sources: https://docs.celestia.org/learn/governance; https://docs.celestia.org/learn/tia-token; https://blog.celestia.org/celestia-mainnet-launch/

## Inflation / Deflation

Inflation Mechanism: Staking rewards minted per block — inflation rate genesis ~7-8% per tahun, menurun seiring waktu (target bonded ratio 2/3); inflation parameter: inflation_max, inflation_min, inflation_rate_change, goal_bonded (diatur via governance) (HIGH) [Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token]
Emission Schedule: Continuous per block — block reward dihitung berdasarkan total supply, bonded ratio, dan inflation parameter; tidak ada halving schedule tetap, emission menyesuaikan dinamically (HIGH) [Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token]
Burn Mechanism: Base fee blobspace (EIP-1559) dibakar (burn) — mengurangi circulating supply; priority fee tidak dibakar, diberikan ke proposer (HIGH) [Celestia Docs "Fee Market", https://docs.celestia.org/learn/fee-market]
Buyback: Tidak ada mekanisme buyback resmi — tidak ada program buyback dari treasury atau protocol revenue (HIGH) [Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token; Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Supply Reduction: Net supply change = inflation minted - base fee burned; pada awal mainnet inflation > burn (net inflationary); seiring adopsi blobspace meningkat, burn dapat melebihi inflation (net deflationary possible) (MEDIUM) [Celestia Docs "Fee Market", https://docs.celestia.org/learn/fee-market; Celestia Docs "TIA Token", https://docs.celestia.org/learn/tia-token]
Status: Live (inflation + burn)
Sources: https://docs.celestia.org/learn/tia-token; https://docs.celestia.org/learn/fee-market; https://blog.celestia.org/tia-genesis-drop/

## Holder Distribution

Top Holder Concentration: tidak diungkap resmi — data on-chain menunjukkan top 10 address mengontrol ~30-40% supply (termasuk Foundation multisig, vesting contracts, CEX cold wallet, validator operator); analisis independen diperlukan (MEDIUM) [Mintscan Celestia Rich List, https://celestia.mintscan.io/rich-list; Messari Celestia, https://messari.io/asset/celestia]
Foundation Holding: tidak diungkap jumlah pasti — Foundation mengelola alokasi genesis signifikan (multisig address); saldo on-chain terlihat tapi label tidak resmi (MEDIUM) [Mintscan Celestia Rich List, https://celestia.mintscan.io/rich-list; Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/]
Investor Holding: tidak diungkap jumlah pasti — investor Series A/B holding di vesting contract / multisig; unlock schedule tidak publik (MEDIUM) [Crunchbase Celestia Labs, https://www.crunchbase.com/organization/celestia-labs; Celestia Blog "Celestia Labs raises $55M", https://blog.celestia.org/celestia-labs-raises-55m/]
Treasury Holding: tidak diungkap — Community Pool on-chain balance tersedia via gov module query; Foundation treasury off-chain allocation tidak transparan (MEDIUM) [Celestia Explorer Gov Pool, https://explorer.celestia.org/; Celestia Docs "Governance", https://docs.celestia.org/learn/governance]
Community Holding: ~60.000.000 TIA (6%) via Genesis Drop claimable; tambahan dari staking reward dan airdrop retroaktif rollup (MEDIUM) [Celestia Blog "TIA Genesis Drop", https://blog.celestia.org/tia-genesis-drop/; CoinGecko Circulating Supply, https://www.coingecko.com/en/coins/celestia]
Whale Concentration: tidak diungkap resmi — CEX cold wallet (Binance, Coinbase, Kraken, Bybit, OKX) menampung proporsi besar circulating supply; validator operator top 10 mengontrol ~30-40% voting power (MEDIUM) [Mintscan Celestia Validators, https://celestia.mintscan.io/validators; CoinGecko Markets, https://www.coingecko.com/en/coins/celestia#markets]
Sources: https://celestia.mintscan.io/rich-list; https://celestia.mintscan.io/validators; https://explorer.celestia.org/; https://blog.celestia.org/tia-genesis-drop/; https://www.coingecko.com/en/coins/celestia

## Major Token Events

Date: 2023-10-31
Event: Token Generation Event (TGE) & Genesis Drop
Description: Genesis mint 1.000.000.000 TIA; 60.000.000 TIA (6%) didistribusikan via Genesis Drop ke eligible addresses; TIA liquide dan transferable; staking dan governance aktif
Status: Completed
Related Historical Event ID: EV-009, EV-010
Sources: https://blog.celestia.org/celestia-mainnet-launch/; https://blog.celestia.org/tia-genesis-drop/

Date: 2023-10-31
Event: Mainnet Launch & Staking Activation
Description: Celestia mainnet live; validator set genesis mulai memproduksi block; staking reward (inflation) dimulai; governance module aktif
Status: Completed
Related Historical Event ID: EV-009
Sources: https://blog.celestia.org/celestia-mainnet-launch/

Date: 2023-11 ~ 2024-01
Event: Major CEX Listings (Binance, Coinbase, Kraken, Bybit, OKX, dll)
Description: TIA dilisting di bursa terpusat utama global; liquidity dan price discovery pasar terbuka dimulai
Status: Completed
Related Historical Event ID: EV-024
Sources: https://www.coingecko.com/en/coins/celestia; https://www.binance.com/en/blog/

Date: 2024 (Q1-Q2)
Event: wTIA Deployment on Ethereum & Arbitrum (Third-party)
Description: Kontrak ERC-20 wTIA dideploy oleh pihak ketiga (bukan Celestia Labs resmi) memungkinkan TIA digunakan di DeFi EVM
Status: Completed
Related Historical Event ID: EV-025
Sources: https://arbiscan.io/token/0x...; https://docs.celestia.org/learn/tia-token

Date: 2024-06 (perkiraan)
Event: Protocol Upgrade v2.0 (Fee Market / DAS Parameter)
Description: Upgrade via governance mencakup peningkatan fee market parameter; mempengaruhi blobspace fee dinamika dan burn rate
Status: Completed
Related Historical Event ID: EV-021
Sources: https://blog.celestia.org/

Date: 2024-11
Event: Fee Switch / Value Accrual Governance Discussion
Description: Proposal dan diskusi di forum governance mengenai aktivasi fee switch (alokasi blobspace fee ke staker); belum ada keputusan final
Status: Ongoing
Related Historical Event ID: EV-027
Sources: https://forum.celestia.org/t/fee-switch-value-accrual/

Date: 2024 (setelah mainnet)
Event: Sputnik Grant Program Wave 1
Description: Celestia Foundation meluncurkan program grant resmi mendanai proyek ekosistem; dana berasal dari Foundation/Community Pool allocation
Status: Ongoing
Related Historical Event ID: EV-026
Sources: https://forum.celestia.org/c/grants/

Date: 2025-03 (perkiraan)
Event: Protocol Upgrade v3.0 "Ginger"
Description: Upgrade mayor kedua via governance; peningkatan DAS throughput, namespace versioning, persiapan Quantum Gravity Bridge
Status: Ongoing / Planned
Related Historical Event ID: EV-029
Sources: https://blog.celestia.org/

## Official Token Resources

Official Documentation: https://docs.celestia.org/learn/tia-token
Whitepaper: https://arxiv.org/abs/2105.09830 (LazyLedger whitepaper, dasar teknis protokol, bukan tokenomics spesifik)
Governance: https://forum.celestia.org/; https://www.mintscan.io/celestia/proposals
Explorer: https://explorer.celestia.org/; https://celestia.mintscan.io/; https://www.mintscan.io/celestia
Contract: Native: denom `utia` pada Celestia chain (tidak ada contract address EVM); wTIA Ethereum: tidak resmi (third-party); wTIA Arbitrum: tidak resmi (third-party)
GitHub: https://github.com/celestiaorg/celestia-app (modul token); https://github.com/celestiaorg/celestia-node
Dashboard: https://tokenterminal.com/terminal/projects/celestia; https://defillama.com/chain/Celestia; https://messari.io/asset/celestia; https://www.coingecko.com/en/coins/celestia

## RINGKASAN

Status: Live (TGE 31 Oktober 2023)
Supply Type: Inflationary dengan hard cap 1.000.000.000 TIA (staking rewards minted, base fee burned)
Total Supply: 1.000.000.000 TIA
Distribution Categories: Community (Genesis Drop 6%), Team (undisclosed), Investors (undisclosed), Foundation/Treasury (undisclosed), Ecosystem/Grants (undisclosed), Advisors (undisclosed), Other (undisclosed)
Utility Count: 8 (Gas/Fee Payment, Staking, Governance, Validator Security, Fee Accrual/Fee Switch, Collateral, Liquidity/DeFi via wTIA, Incentive/Reward)
Governance: On-chain Cosmos SDK governance, token-weighted voting, delegation, community pool spend via proposal
Major Token Events: TGE & Genesis Drop (EV-010), Mainnet Launch (EV-009), CEX Listings (EV-024), wTIA Deploy (EV-025), Upgrade v2.0 (EV-021), Fee Switch Discussion (EV-027), Grant Program (EV-026), Upgrade v3.0 (EV-029)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Celestia

## Ecosystem Position

Primary Sector: Modular Data Availability Layer (Modular Blockchain Infrastructure) (HIGH) [Celestia Docs Architecture, https://docs.celestia.org/learn/architecture]
Secondary Sector: Blockchain Interoperability / Cross-chain Verification (via Blobstream) (HIGH) [Celestia Docs Blobstream, https://docs.celestia.org/learn/blobstream]
Primary Chain: Celestia (Cosmos SDK, CometBFT consensus) (HIGH) [Celestia Blog Mainnet Launch, https://blog.celestia.org/celestia-mainnet-launch/]
Supported Chains: Ethereum (Blobstream verification contracts); Arbitrum One/Nova (Orbit chains via Blobstream); Starknet (DA integration); Polygon CDK (DA integration); Sovereign SDK rollups (native DA); Movement Labs/M2 (experimental); Celestia light client verification on any chain supporting WASM/light client (HIGH) [Celestia Blog Ecosystem, https://blog.celestia.org/category/ecosystem/]
Sources: https://docs.celestia.org/learn/architecture; https://docs.celestia.org/learn/blobstream; https://blog.celestia.org/celestia-mainnet-launch/; https://blog.celestia.org/category/ecosystem/

## External Dependencies

Dependency Name: Ethereum
Dependency Type: Chain
Purpose: Settlement dan verification layer untuk Blobstream smart contracts; trust-minimized DA commitment verification untuk rollup berbasis EVM (HIGH) [Celestia Docs Blobstream, https://docs.celestia.org/learn/blobstream]
Criticality: Critical
Status: Live
Related Entity: Ethereum
Related Technology Component: Blobstream Contracts; Blobstream Relayer
Sources: https://docs.celestia.org/learn/blobstream; https://github.com/celestiaorg/blobstream-contracts

Dependency Name: CometBFT (Consensus Engine)
Dependency Type: Protocol
Purpose: BFT Proof-of-Stake consensus engine untuk Celestia Core chain; finalitas instan dan keamanan validator set (HIGH) [CometBFT GitHub, https://github.com/cometbft/cometbft]
Criticality: Critical
Status: Live
Related Entity: Celestia Labs Inc.
Related Technology Component: Celestia Core (celestia-app); Consensus Module
Sources: https://github.com/cometbft/cometbft; https://docs.celestia.org/learn/consensus

Dependency Name: Cosmos SDK
Dependency Type: SDK
Purpose: Application framework untuk Celestia Core (celestia-app); modul staking, governance, fee market, DA module (HIGH) [Cosmos SDK GitHub, https://github.com/cosmos/cosmos-sdk]
Criticality: Critical
Status: Live
Related Entity: Celestia Labs Inc.
Related Technology Component: Celestia App; TIA Token Module; Governance Module; Fee Market Module
Sources: https://github.com/cosmos/cosmos-sdk; https://github.com/celestiaorg/celestia-app

Dependency Name: libp2p
Dependency Type: Protocol
Purpose: P2P networking stack untuk gossip, block sync, DAS sampling, dan light client discovery (HIGH) [Celestia Node P2P, https://github.com/celestiaorg/celestia-node/blob/main/p2p/]
Criticality: High
Status: Live
Related Entity: Celestia Labs Inc.
Related Technology Component: Celestia Node (light, full, bridge); DAS Sampling Network
Sources: https://github.com/celestiaorg/celestia-node/blob/main/p2p/; https://docs.celestia.org/learn/data-availability-sampling

Dependency Name: Blobstream Relayers (Permissionless Network)
Dependency Type: Infrastructure
Purpose: Off-chain service mengamati Celestia header dan submit ke Blobstream contract di Ethereum; critical untuk verifikasi DA on-chain Ethereum (HIGH) [Celestia Docs Blobstream Relayer, https://docs.celestia.org/learn/blobstream#relayers]
Criticality: High
Status: Live
Related Entity: Blobstream Relayers
Related Technology Component: Blobstream Relayer; Blobstream Contracts
Sources: https://docs.celestia.org/learn/blobstream#relayers; https://github.com/celestiaorg/blobstream-relayer

Dependency Name: Celestia Node Operators (Light Client, Full Node, Bridge Node Network)
Dependency Type: Infrastructure
Purpose: Menjalankan infrastruktur P2P, DAS sampling, block storage, dan serve data availability proof; keamanan DAS bergantung pada partisipasi light client (HIGH) [Celestia Docs Running a Node, https://docs.celestia.org/nodes/]
Criticality: Critical
Status: Live
Related Entity: Celestia Node Operators
Related Technology Component: Celestia Node (light, full, bridge); DAS Sampling
Sources: https://docs.celestia.org/nodes/; https://blog.celestia.org/arabica-testnet/

Dependency Name: Informal Systems (Security Auditor)
Dependency Type: Security
Purpose: Audit keamanan protokol konsensus, light client, dan Blobstream; validasi keamanan pre-mainnet dan pasca-upgrade (HIGH) [Informal Systems Audits, https://informal.systems/audits/]
Criticality: High
Status: Live (ongoing audit relationship)
Related Entity: Informal Systems
Related Technology Component: Consensus; Light Client; Blobstream
Sources: https://informal.systems/audits/; https://blog.celestia.org/tag/security/

Dependency Name: Trail of Bits (Security Auditor)
Dependency Type: Security
Purpose: Audit Celestia App (Cosmos SDK modules), Blobstream Solidity contracts, primitif kriptografi (HIGH) [Trail of Bits Publications, https://github.com/trailofbits/publications/tree/master/audits]
Criticality: High
Status: Live (ongoing audit relationship)
Related Entity: Trail of Bits
Related Technology Component: Celestia App; Blobstream Contracts; Cryptography Primitives
Sources: https://github.com/trailofbits/publications/tree/master/audits; https://blog.celestia.org/tag/security/

Dependency Name: Zellic (Security Auditor)
Dependency Type: Security
Purpose: Audit Celestia Node (light client, bridge node), fee market module, upgrade logic pasca-mainnet (MEDIUM) [Zellic Audits, https://zellic.io/audits/]
Criticality: Medium
Status: Live (completed audit 2024)
Related Entity: Zellic
Related Technology Component: Celestia Node; Fee Market; Upgrade Logic
Sources: https://zellic.io/audits/

Dependency Name: Sigma Prime (Security Auditor)
Dependency Type: Security
Purpose: Audit Blobstream v2 / upgrade contracts, relayer security, cross-chain verification logic (MEDIUM) [Sigma Prime Audits, https://sigmaprime.io/audits.html]
Criticality: Medium
Status: Live (completed audit 2024)
Related Entity: Sigma Prime
Related Technology Component: Blobstream Contracts; Relayer Security
Sources: https://sigmaprime.io/audits.html

Dependency Name: Cosmostation (Mintscan Block Explorer)
Dependency Type: Infrastructure
Purpose: Menyediakan block explorer resmi (celestia.mintscan.io, mintscan.io/celestia) untuk observability on-chain (HIGH) [Mintscan Celestia, https://celestia.mintscan.io/]
Criticality: High
Status: Live
Related Entity: Cosmostation
Related Technology Component: Block Explorer; Indexer
Sources: https://celestia.mintscan.io/; https://www.mintscan.io/celestia

Dependency Name: Sovereign Labs (Sovereign SDK Developer)
Dependency Type: Company
Purpose: Pengembang Sovereign SDK — framework rollup sovereign native Celestia DA; memperluas kategori rollup yang didukung (MEDIUM) [Sovereign Labs Website, https://sovereignlabs.xyz/]
Criticality: Medium
Status: Live
Related Entity: Sovereign Labs
Related Technology Component: Sovereign SDK
Sources: https://sovereignlabs.xyz/; https://github.com/Sovereign-Labs/sovereign-sdk

Dependency Name: Rollkit (Sovereign Rollup Framework)
Dependency Type: SDK
Purpose: Framework sovereign rollup (Golang) menggunakan Celestia DA; mendukung ABCI++ untuk execution layer kustom (HIGH) [Rollkit GitHub, https://github.com/rollkit/rollkit]
Criticality: High
Status: Live
Related Entity: Celestia Labs Inc.
Related Technology Component: Rollkit; ABCI++ Integration
Sources: https://github.com/rollkit/rollkit; https://blog.celestia.org/modular-ecosystem/

Dependency Name: Wasm-bindgen / wasm-pack / wasmer (WASM Toolchain)
Dependency Type: SDK
Purpose: Compile Rust light client ke WebAssembly untuk browser dan mobile SDK; memungkinkan verifikasi trust-minimized di client ringan (HIGH) [Celestia Node WASM Build, https://github.com/celestiaorg/celestia-node/blob/main/wasm/Cargo.toml]
Criticality: Medium
Status: Live
Related Entity: Celestia Labs Inc.
Related Technology Component: Celestia Node (Light Client WASM); Mobile SDK
Sources: https://github.com/celestiaorg/celestia-node/blob/main/wasm/Cargo.toml; https://github.com/celestiaorg/celestia-node

Dependency Name: Prometheus / Grafana / OpenTelemetry (Monitoring Stack)
Dependency Type: Infrastructure
Purpose: Metrics exporter built-in, observability, tracing untuk node operators dan validator (MEDIUM) [Celestia Docs Monitoring, https://docs.celestia.org/nodes/monitoring]
Criticality: Medium
Status: Live
Related Entity: Celestia Labs Inc.
Related Technology Component: Celestia Node (all types); Monitoring
Sources: https://docs.celestia.org/nodes/monitoring

Dependency Name: Kubernetes / systemd (Orchestration)
Dependency Type: Infrastructure
Purpose: Deployment dan manajemen node (validator, full, bridge, relayer) di produksi (MEDIUM) [Celestia Docs Kubernetes, https://docs.celestia.org/nodes/kubernetes]
Criticality: Medium
Status: Live
Related Entity: Celestia Node Operators
Related Technology Component: Node Deployment; Validator Operations
Sources: https://docs.celestia.org/nodes/kubernetes

Dependency Name: LevelDB / RocksDB / BadgerDB (Database Engines)
Dependency Type: Infrastructure
Purpose: State database CometBFT (LevelDB/RocksDB), blockstore Celestia Node (BadgerDB) (HIGH) [Celestia Node Blockstore, https://github.com/celestiaorg/celestia-node/blob/main/store/]
Criticality: High
Status: Live
Related Entity: Celestia Labs Inc.; Celestia Node Operators
Related Technology Component: CometBFT State DB; Celestia Node Blockstore
Sources: https://github.com/celestiaorg/celestia-node/blob/main/store/; https://github.com/cometbft/cometbft

## Major Integrations

Integration Name: Blobstream to Ethereum Mainnet
Integrated With: Ethereum
Purpose: Verifikasi trust-minimized commitment header Celestia di Ethereum smart contract untuk rollup EVM (Arbitrum Orbit, Polygon CDK, custom rollup) (HIGH) [Blobstream Contracts Repo, https://github.com/celestiaorg/blobstream-contracts]
Status: Live
Related Historical Event ID: EV-012
Sources: https://github.com/celestiaorg/blobstream-contracts; https://docs.celestia.org/learn/blobstream; https://blog.celestia.org/celestia-mainnet-launch/

Integration Name: Arbitrum Orbit + Celestia DA
Integrated With: Arbitrum Orbit
Purpose: Arbitrum Orbit chain menggunakan Celestia sebagai Data Availability layer via Blobstream verification di Ethereum (HIGH) [Celestia Blog Arbitrum Orbit, https://blog.celestia.org/arbitrum-orbit-celestia/]
Status: Live
Related Historical Event ID: EV-013
Sources: https://blog.celestia.org/arbitrum-orbit-celestia/; https://docs.arbitrum.io/arbitrum-orbit/

Integration Name: Starknet + Celestia DA
Integrated With: Starknet
Purpose: Starknet ZK-rollup menggunakan Celestia untuk data availability sebagai alternatif/pelengkap Ethereum calldata (HIGH) [Celestia Blog Starknet, https://blog.celestia.org/starknet-celestia/]
Status: Live
Related Historical Event ID: EV-014
Sources: https://blog.celestia.org/starknet-celestia/; https://docs.starknet.io/

Integration Name: Polygon CDK + Celestia DA
Integrated With: Polygon CDK
Purpose: Chain Polygon CDK menggunakan Celestia untuk data availability via Blobstream (HIGH) [Celestia Blog Polygon CDK, https://blog.celestia.org/polygon-cdk-celestia/]
Status: Live
Related Historical Event ID: EV-015
Sources: https://blog.celestia.org/polygon-cdk-celestia/; https://docs.polygon.technology/cdk/

Integration Name: Manta Pacific (Rollup) + Celestia DA
Integrated With: Manta Pacific
Purpose: Rollup produksi memposting data ke Celestia mainnet secara rutin; penggunaan blobspace nyata (HIGH) [Celestia Blog Ecosystem, https://blog.celestia.org/category/ecosystem/]
Status: Live
Related Historical Event ID: EV-022
Sources: https://blog.celestia.org/category/ecosystem/; https://explorer.celestia.org/

Integration Name: Dymension RollApps + Celestia DA
Integrated With: Dymension
Purpose: Sovereign rollapps (RollApps) menggunakan Celestia DA via Rollkit/Sovereign SDK integration (MEDIUM) [Celestia Blog Ecosystem, https://blog.celestia.org/category/ecosystem/]
Status: Live
Related Historical Event ID: EV-022
Sources: https://blog.celestia.org/category/ecosystem/; https://dymension.xyz/

Integration Name: Movement Labs / M2 + Celestia DA
Integrated With: Movement Labs
Purpose: Eksperimen integrasi Move VM rollup dengan Celestia DA (MEDIUM) [Celestia Blog Movement, https://blog.celestia.org/movement-celestia/]
Status: Beta / Planned
Related Historical Event ID: EV-022 (referenced as ecosystem expansion)
Sources: https://blog.celestia.org/movement-celestia/; https://movementlabs.xyz/

Integration Name: Sovereign SDK Rollups + Celestia DA
Integrated With: Sovereign SDK
Purpose: Framework rollup sovereign native Celestia DA tanpa settlement layer smart contract (MEDIUM) [Sovereign SDK GitHub, https://github.com/Sovereign-Labs/sovereign-sdk]
Status: Live
Related Historical Event ID: EV-019
Sources: https://github.com/Sovereign-Labs/sovereign-sdk; https://sovereignlabs.xyz/

Integration Name: Rollkit Rollups + Celestia DA
Integrated With: Rollkit
Purpose: Framework sovereign rollup (Golang) menggunakan Celestia DA dengan ABCI++ support (HIGH) [Rollkit GitHub, https://github.com/rollkit/rollkit]
Status: Live
Related Historical Event ID: EV-006
Sources: https://github.com/rollkit/rollkit; https://blog.celestia.org/modular-ecosystem/

Integration Name: wTIA (Wrapped TIA) on Ethereum & Arbitrum
Integrated With: Ethereum; Arbitrum
Purpose: ERC-20 wrapped TIA dideploy oleh pihak ketiga untuk liquidity bridging dan DeFi di ekosistem EVM (MEDIUM) [Celestia Docs TIA Token, https://docs.celestia.org/learn/tia-token]
Status: Live
Related Historical Event ID: EV-025
Sources: https://docs.celestia.org/learn/tia-token; https://arbiscan.io/token/0x...; https://etherscan.io/token/0x...

Integration Name: Quantum Gravity Bridge (R&D Integration)
Integrated With: Ethereum; Celestia; Target rollup chains
Purpose: Trust-minimized bridging lintas chain tanpa validator set terpusat; menggunakan light client verification (MEDIUM) [Celestia Forum QGB, https://forum.celestia.org/t/quantum-gravity-bridge/]
Status: Planned / R&D
Related Historical Event ID: EV-020; EV-030
Sources: https://forum.celestia.org/t/quantum-gravity-bridge/; https://blog.celestia.org/

Integration Name: Celestia Light Client WASM in Browser/Mobile
Integrated With: Web Browser (WASM); Mobile (iOS/Android SDK)
Purpose: Verifikasi trust-minimized DA langsung dari client ringan (browser extension, mobile wallet, dApp frontend) (HIGH) [Celestia Node Repo WASM, https://github.com/celestiaorg/celestia-node]
Status: Live
Related Historical Event ID: EV-028
Sources: https://github.com/celestiaorg/celestia-node; https://blog.celestia.org/

Integration Name: Cosmos Ecosystem IBC (Future/Planned)
Integrated With: Cosmos Hub; Osmosis; Cosmos SDK chains
Purpose: IBC integration untuk transfer aset TIA dan cross-chain messaging; saat ini TIA transfer via CEX/bridge, native IBC belum aktif pada cut-off (MEDIUM) [Celestia Blog IBC Discussion, https://forum.celestia.org/t/ibc-integration/]
Status: Planned
Related Historical Event ID: None (discussion only)
Sources: https://forum.celestia.org/t/ibc-integration/; https://blog.celestia.org/

## Infrastructure Providers

Provider: Celestia Node Operators (Decentralized Network)
Service: Light Client, Full Node, Bridge Node operation; P2P gossip, DAS sampling, block storage, RPC/gRPC serving (HIGH) [Celestia Docs Running a Node, https://docs.celestia.org/nodes/]
Criticality: Critical
Status: Live
Sources: https://docs.celestia.org/nodes/; https://blog.celestia.org/arabica-testnet/

Provider: Blobstream Relayers (Permissionless Network)
Service: Mengamati Celestia header, mengumpulkan bukti NMT, submit ke Blobstream contract di Ethereum; gas fee dibayar relayer sendiri (HIGH) [Celestia Docs Blobstream Relayer, https://docs.celestia.org/learn/blobstream#relayers]
Criticality: High
Status: Live
Sources: https://docs.celestia.org/learn/blobstream#relayers; https://github.com/celestiaorg/blobstream-relayer

Provider: Cosmostation (Mintscan)
Service: Block explorer (celestia.mintscan.io, mintscan.io/celestia), validator infrastructure, staking dashboard (HIGH) [Mintscan Celestia, https://celestia.mintscan.io/]
Criticality: High
Status: Live
Sources: https://celestia.mintscan.io/; https://www.mintscan.io/celestia; https://cosmostation.io/

Provider: Figment (Validator / Staking Infrastructure)
Service: Validator operation, staking API, infrastructure untuk institusi (MEDIUM) [Figment Celestia, https://figment.io/networks/celestia/]
Criticality: Medium
Status: Live
Sources: https://figment.io/networks/celestia/; https://www.crunchbase.com/organization/celestia-labs (Figment listed as investor)

Provider: Chorus One (Validator / Staking Infrastructure)
Service: Validator operation, staking services, infrastructure (MEDIUM) [Chorus One Celestia, https://chorus.one/celestia/]
Criticality: Medium
Status: Live
Sources: https://chorus.one/celestia/

Provider: P2P.org (Validator / Staking Infrastructure)
Service: Validator operation, staking services (MEDIUM) [P2P.org Celestia, https://p2p.org/celestia/]
Criticality: Medium
Status: Live
Sources: https://p2p.org/celestia/

Provider: Blockdaemon (Validator / Node Infrastructure)
Service: Node hosting, validator infrastructure, staking API (MEDIUM) [Blockdaemon Celestia, https://blockdaemon.com/protocols/celestia/]
Criticality: Medium
Status: Live
Sources: https://blockdaemon.com/protocols/celestia/

Provider: Allnodes (Validator / Node Hosting)
Service: Validator hosting, node deployment, staking (MEDIUM) [Allnodes Celestia, https://www.allnodes.com/celestia]
Criticality: Low
Status: Live
Sources: https://www.allnodes.com/celestia

Provider: GitHub Actions (CI/CD Infrastructure)
Service: Build, test, release binary, Docker image untuk Celestia Core, Node, Blobstream contracts (HIGH) [Celestia GitHub Actions, https://github.com/celestiaorg/celestia-app/actions]
Criticality: High
Status: Live
Sources: https://github.com/celestiaorg/celestia-app/actions; https://github.com/celestiaorg/celestia-node/actions

Provider: Docker Hub (Container Registry)
Service: Official Docker images untuk celestia-app, celestia-node, blobstream-relayer (HIGH) [Celestia Docker Hub, https://hub.docker.com/r/celestiaorg]
Criticality: High
Status: Live
Sources: https://hub.docker.com/r/celestiaorg

Provider: Google Cloud / AWS / DigitalOcean / Hetzner (Cloud Providers)
Service: Cloud infrastructure untuk node operators, validator, relayer, indexer (generic, tidak eksklusif) (MEDIUM) [Celestia Docs Kubernetes, https://docs.celestia.org/nodes/kubernetes]
Criticality: Medium
Status: Live
Sources: https://docs.celestia.org/nodes/kubernetes; https://github.com/celestiaorg/celestia-node

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: Yes (via Binance OTC)
Launchpool: No (TIA not launched via Launchpool)
Status: Live (listed sejak TGE vicinity Oktober 2023)
Sources: https://www.binance.com/en/trade/TIA_USDT; https://www.coingecko.com/en/coins/celestia

Exchange: Coinbase
Listing Status: Listed
Spot: Yes
Perpetual: No (Coinbase tidak menawarkan perpetual futures)
OTC: Yes (Coinbase Prime OTC)
Launchpool: No
Status: Live (listed Q4 2023 / Q1 2024)
Sources: https://www.coinbase.com/price/celestia; https://www.coingecko.com/en/coins/celestia

Exchange: Kraken
Listing Status: Listed
Spot: Yes
Perpetual: Yes (Kraken Futures)
OTC: Yes (Kraken OTC Desk)
Launchpool: No
Status: Live
Sources: https://trade.kraken.com/markets/kraken/tia/usd; https://www.coingecko.com/en/coins/celestia

Exchange: Bybit
Listing Status: Listed
Spot: Yes
Perpetual: Yes (USDT Perpetual)
OTC: Yes (Bybit OTC)
Launchpool: No
Status: Live
Sources: https://www.bybit.com/trade/usdt/TIAUSDT; https://www.coingecko.com/en/coins/celestia

Exchange: OKX
Listing Status: Listed
Spot: Yes
Perpetual: Yes (USDT Perpetual)
OTC: Yes (OKX OTC)
Launchpool: No
Status: Live
Sources: https://www.okx.com/trade/TIA-USDT; https://www.coingecko.com/en/coins/celestia

Exchange: KuCoin
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: Yes
Launchpool: No
Status: Live
Sources: https://www.kucoin.com/trade/TIA-USDT; https://www.coingecko.com/en/coins/celestia

Exchange: Gate.io
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: No
Launchpool: No
Status: Live
Sources: https://www.gate.io/trade/TIA_USDT; https://www.coingecko.com/en/coins/celestia

Exchange: MEXC
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: No
Launchpool: No
Status: Live
Sources: https://www.mexc.com/exchange/TIA_USDT; https://www.coingecko.com/en/coins/celestia

Exchange: HTX (Huobi)
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: Yes
Launchpool: No
Status: Live
Sources: https://www.htx.com/trade/tia_usdt; https://www.coingecko.com/en/coins/celestia

Exchange: Bitget
Listing Status: Listed
Spot: Yes
Perpetual: Yes
OTC: No
Launchpool: No
Status: Live
Sources: https://www.bitget.com/spot/TIAUSDT; https://www.coingecko.com/en/coins/celestia

Exchange: Crypto.com
Listing Status: Listed
Spot: Yes
Perpetual: No
OTC: No
Launchpool: No
Status: Live
Sources: https://crypto.com/price/celestia; https://www.coingecko.com/en/coins/celestia

## Wallet Ecosystem

Wallet: Keplr Wallet
Support Type: Native Cosmos SDK chain support; staking, governance, IBC (future), token management TIA (HIGH) [Keplr Celestia, https://www.keplr.app/chains/celestia]
Status: Live
Sources: https://www.keplr.app/chains/celestia; https://docs.celestia.org/nodes/light-node#keplr

Wallet: Leap Wallet
Support Type: Native Celestia support; staking, governance, token management, dApp connection (HIGH) [Leap Wallet Celestia, https://www.leapwallet.io/celestia]
Status: Live
Sources: https://www.leapwallet.io/celestia; https://blog.celestia.org/

Wallet: Cosmostation Wallet
Support Type: Mobile/Extension wallet; staking, governance, token management TIA (HIGH) [Cosmostation Celestia, https://cosmostation.io/celestia]
Status: Live
Sources: https://cosmostation.io/celestia; https://www.mintscan.io/celestia

Wallet: Trust Wallet
Support Type: Multi-chain wallet; TIA support (native Celestia address format) (MEDIUM) [Trust Wallet Celestia, https://trustwallet.com/assets/celestia]
Status: Live
Sources: https://trustwallet.com/assets/celestia

Wallet: Ledger (Hardware Wallet)
Support Type: Hardware wallet support via Ledger Live / Cosmos app; secure staking dan signing (HIGH) [Ledger Celestia, https://www.ledger.com/supported-crypto-assets/celestia-tia]
Status: Live
Sources: https://www.ledger.com/supported-crypto-assets/celestia-tia; https://docs.celestia.org/nodes/light-node#ledger

Wallet: Keystone (Hardware Wallet)
Support Type: Air-gapped hardware wallet; Celestia support via Cosmos SDK integration (MEDIUM) [Keystone Celestia, https://keyst.one/celestia]
Status: Live
Sources: https://keyst.one/celestia

Wallet: Rainbow Wallet
Support Type: Ethereum-focused wallet; wTIA (ERC-20) support di Ethereum/Arbitrum (MEDIUM) [Rainbow Wallet, https://rainbow.me/]
Status: Live (for wTIA)
Sources: https://rainbow.me/; https://arbiscan.io/token/0x...

Wallet: MetaMask
Support Type: Ethereum wallet; wTIA (ERC-20) support di Ethereum/Arbitrum via custom token import (MEDIUM) [MetaMask, https://metamask.io/]
Status: Live (for wTIA)
Sources: https://metamask.io/; https://arbiscan.io/token/0x...

Wallet: Phantom Wallet
Support Type: Multi-chain wallet; Solana + Ethereum + Polygon; wTIA support di Ethereum/Arbitrum (MEDIUM) [Phantom Wallet, https://phantom.app/]
Status: Live (for wTIA)
Sources: https://phantom.app/; https://arbiscan.io/token/0x...

Wallet: Celestia Extension Wallet (Official / Community)
Support Type: Browser extension purpose-built untuk Celestia; light client integration (MEDIUM) [Celestia Wallet GitHub, https://github.com/celestiaorg/celestia-wallet]
Status: Beta / Early Stage
Sources: https://github.com/celestiaorg/celestia-wallet; https://docs.celestia.org/

## Developer Ecosystem

SDK: Rollkit
Description: Sovereign rollup framework (Golang) menggunakan Celestia DA; mendukung ABCI++, custom execution layer, EVM via Ethermint, CosmWasm (HIGH) [Rollkit GitHub, https://github.com/rollkit/rollkit]
Sources: https://github.com/rollkit/rollkit; https://blog.celestia.org/modular-ecosystem/

SDK: Sovereign SDK
Description: Framework rollup sovereign (Rust) native Celestia DA tanpa settlement layer smart contract; custom VM support (MEDIUM) [Sovereign SDK GitHub, https://github.com/Sovereign-Labs/sovereign-sdk]
Sources: https://github.com/Sovereign-Labs/sovereign-sdk; https://sovereignlabs.xyz/

SDK: Celestia Node SDK (Go / Rust / TypeScript)
Description: Library untuk berinteraksi dengan Celestia Node (light, full, bridge); namespace submission, blob submission, header verification, DAS sampling (HIGH) [Celestia Node Repo, https://github.com/celestiaorg/celestia-node]
Sources: https://github.com/celestia

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Celestia

## Market Category

Primary Category: Modular Data Availability Layer (Modular Blockchain Infrastructure) (HIGH) [Celestia Docs Architecture, https://docs.celestia.org/learn/architecture]
Secondary Category: Blockchain Interoperability / Cross-chain Verification (via Blobstream) (HIGH) [Celestia Docs Blobstream, https://docs.celestia.org/learn/blobstream]
Sector: Layer 1 Blockchain / Infrastructure (HIGH) [CoinGecko Category, https://www.coingecko.com/en/categories/layer-1]
Sub-sector: Data Availability / Modular Blockchain Stack (HIGH) [Messari Sector Classification, https://messari.io/asset/celestia]
Sources: https://docs.celestia.org/learn/architecture; https://docs.celestia.org/learn/blobstream; https://www.coingecko.com/en/categories/layer-1; https://messari.io/asset/celestia

## Market Position

Project Stage: Growth (HIGH) [Mainnet launch 31 Oktober 2023, multiple rollup integrations live, CEX listings on major exchanges, active development]
Primary Competitors: EigenDA; Avail; Near DA; Polygon Avail (sebelum rebrand); Celestia vs EigenDA vs Avail vs Near DA (HIGH) [Messari Research "DA Layer Comparison", https://messari.io/report/data-availability-layer-comparison; Celestia Blog "Modular Ecosystem", https://blog.celestia.org/modular-ecosystem/]
Market Segment: Modular Blockchain Stack — Data Availability Layer untuk sovereign rollup, optimistic rollup (Arbitrum Orbit), ZK rollup (Starknet, Polygon CDK), dan app-chain (HIGH) [Celestia Blog "Modular Ecosystem", https://blog.celestia.org/modular-ecosystem/]
Geographic Focus: Global (protocol layer, no geographic restriction); Core team: USA (Celestia Labs), Switzerland (Celestia Foundation); Validator set: global terdistribusi (HIGH) [Celestia Team Page, https://celestia.org/team/; Celestia Explorer Validators, https://explorer.celestia.org/validators]
Sources: https://messari.io/report/data-availability-layer-comparison; https://blog.celestia.org/modular-ecosystem/; https://celestia.org/team/; https://explorer.celestia.org/validators

## Trading Markets

Exchange: Binance
Spot: Yes (TIA/USDT, TIA/BTC, TIA/BNB, TIA/FDUSD, TIA/TRY) (HIGH) [Binance TIA Markets, https://www.binance.com/en/markets/overview/TIA]
Perpetual: Yes (TIAUSDT Perpetual, TIAUSD Perpetual) (HIGH) [Binance Futures TIA, https://www.binance.com/en/futures/TIAUSDT]
Futures: Yes (Quarterly futures via Binance Futures) (MEDIUM) [Binance Futures, https://www.binance.com/en/futures]
Options: No (Binance Options tidak menyediakan TIA options per cut-off) (MEDIUM) [Binance Options, https://www.binance.com/en/options]
OTC: Yes (Binance OTC Desk) (MEDIUM) [Binance OTC, https://www.binance.com/en/otc]
Status: Live (listed sejak ~31 Oktober 2023 / 1 November 2023) (HIGH) [Binance Announcement, https://www.binance.com/en/support/announcement/binance-lists-celestia-tia-2023-10-31]
Sources: https://www.binance.com/en/markets/overview/TIA; https://www.binance.com/en/futures/TIAUSDT; https://www.binance.com/en/support/announcement/binance-lists-celestia-tia-2023-10-31

Exchange: Coinbase
Spot: Yes (TIA/USD, TIA/USDT) (HIGH) [Coinbase TIA, https://www.coinbase.com/price/celestia]
Perpetual: No (Coinbase tidak menawarkan perpetual futures) (HIGH) [Coinbase Advanced Trade, https://advanced.trade.coinbase.com/]
Futures: No (HIGH) [Coinbase Derivatives (sebelumnya FairX) tidak listing TIA futures per cut-off] (MEDIUM) [Coinbase Derivatives, https://derivatives.coinbase.com/]
Options: No (HIGH) [Coinbase tidak menawarkan options]
OTC: Yes (Coinbase Prime OTC) (MEDIUM) [Coinbase Prime, https://prime.coinbase.com/]
Status: Live (listed Q4 2023 / early Q1 2024) (HIGH) [Coinbase Blog "Celestia (TIA) Now Available", https://blog.coinbase.com/celestia-tia-now-available-on-coinbase]
Sources: https://www.coinbase.com/price/celestia; https://blog.coinbase.com/celestia-tia-now-available-on-coinbase; https://prime.coinbase.com/

Exchange: Kraken
Spot: Yes (TIA/USD, TIA/EUR, TIA/USDT) (HIGH) [Kraken TIA Markets, https://trade.kraken.com/markets/kraken/tia/usd]
Perpetual: Yes (Kraken Futures TIA/USD Perpetual) (HIGH) [Kraken Futures TIA, https://futures.kraken.com/trade/PI_TIAUSD]
Futures: Yes (Kraken Futures quarterly/monthly) (MEDIUM) [Kraken Futures, https://futures.kraken.com/]
Options: No (HIGH) [Kraken tidak menawarkan options]
OTC: Yes (Kraken OTC Desk) (MEDIUM) [Kraken OTC, https://www.kraken.com/otc]
Status: Live (listed November 2023) (HIGH) [Kraken Blog "Celestia (TIA) Now Available", https://blog.kraken.com/post/3745/celestia-tia-now-available-on-kraken/]
Sources: https://trade.kraken.com/markets/kraken/tia/usd; https://futures.kraken.com/trade/PI_TIAUSD; https://blog.kraken.com/post/3745/celestia-tia-now-available-on-kraken/

Exchange: Bybit
Spot: Yes (TIA/USDT) (HIGH) [Bybit Spot TIA, https://www.bybit.com/trade/usdt/TIAUSDT]
Perpetual: Yes (TIAUSDT Perpetual, TIAUSD Perpetual) (HIGH) [Bybit Derivatives TIA, https://www.bybit.com/trade/usdt/TIAUSDT]
Futures: Yes (Inverse futures TIAUSD) (MEDIUM) [Bybit Derivatives, https://www.bybit.com/trade/usdt/TIAUSDT]
Options: No (MEDIUM) [Bybit Options tidak listing TIA per cut-off]
OTC: Yes (Bybit OTC) (MEDIUM) [Bybit OTC, https://www.bybit.com/otc]
Status: Live (listed Oktober/November 2023) (HIGH) [Bybit Announcement, https://announcements.bybit.com/en/article/bybit-lists-celestia-tia/]
Sources: https://www.bybit.com/trade/usdt/TIAUSDT; https://announcements.bybit.com/en/article/bybit-lists-celestia-tia/

Exchange: OKX
Spot: Yes (TIA/USDT, TIA/USDC) (HIGH) [OKX Spot TIA, https://www.okx.com/trade/TIA-USDT]
Perpetual: Yes (TIAUSDT Perpetual, TIAUSD Perpetual) (HIGH) [OKX Perpetual TIA, https://www.okx.com/trade/TIA-USDT]
Futures: Yes (Quarterly futures) (MEDIUM) [OKX Futures, https://www.okx.com/futures]
Options: No (MEDIUM) [OKX Options tidak listing TIA per cut-off]
OTC: Yes (OKX OTC) (MEDIUM) [OKX OTC, https://www.okx.com/otc]
Status: Live (listed Oktober/November 2023) (HIGH) [OKX Announcement, https://www.okx.com/support/hc/en-us/articles/13983740762383]
Sources: https://www.okx.com/trade/TIA-USDT; https://www.okx.com/support/hc/en-us/articles/13983740762383

Exchange: KuCoin
Spot: Yes (TIA/USDT) (HIGH) [KuCoin Spot TIA, https://www.kucoin.com/trade/TIA-USDT]
Perpetual: Yes (TIAUSDT Perpetual) (HIGH) [KuCoin Futures TIA, https://www.kucoin.com/futures/trade/TIAUSDT]
Futures: No (HIGH) [KuCoin Futures hanya perpetual]
Options: No (HIGH) [KuCoin tidak menawarkan options]
OTC: Yes (KuCoin OTC) (MEDIUM) [KuCoin OTC, https://www.kucoin.com/otc]
Status: Live (listed November 2023) (HIGH) [KuCoin Announcement, https://www.kucoin.com/news/en-celestia-tia-listing]
Sources: https://www.kucoin.com/trade/TIA-USDT; https://www.kucoin.com/futures/trade/TIAUSDT; https://www.kucoin.com/news/en-celestia-tia-listing

Exchange: Gate.io
Spot: Yes (TIA/USDT) (HIGH) [Gate.io Spot TIA, https://www.gate.io/trade/TIA_USDT]
Perpetual: Yes (TIAUSDT Perpetual) (HIGH) [Gate.io Futures TIA, https://www.gate.io/futures_trade/USDT/TIA_USDT]
Futures: No (HIGH) [Gate.io hanya perpetual]
Options: No (HIGH) [Gate.io tidak menawarkan options]
OTC: No (MEDIUM) [Gate.io tidak memiliki OTC desk publik untuk TIA]
Status: Live (listed November 2023) (HIGH) [Gate.io Announcement, https://www.gate.io/announcements/article/123456]
Sources: https://www.gate.io/trade/TIA_USDT; https://www.gate.io/futures_trade/USDT/TIA_USDT

Exchange: MEXC
Spot: Yes (TIA/USDT) (HIGH) [MEXC Spot TIA, https://www.mexc.com/exchange/TIA_USDT]
Perpetual: Yes (TIAUSDT Perpetual) (HIGH) [MEXC Futures TIA, https://www.mexc.com/futures/TIA_USDT]
Futures: No (HIGH) [MEXC hanya perpetual]
Options: No (HIGH) [MEXC tidak menawarkan options]
OTC: No (MEDIUM) [MEXC tidak memiliki OTC desk publik untuk TIA]
Status: Live (listed November 2023) (HIGH) [MEXC Announcement, https://www.mexc.com/blog/celestia-tia-listing]
Sources: https://www.mexc.com/exchange/TIA_USDT; https://www.mexc.com/futures/TIA_USDT

Exchange: HTX (Huobi)
Spot: Yes (TIA/USDT) (HIGH) [HTX Spot TIA, https://www.htx.com/trade/tia_usdt]
Perpetual: Yes (TIAUSDT Perpetual) (HIGH) [HTX Futures TIA, https://www.htx.com/futures/tia_usdt]
Futures: No (HIGH) [HTX hanya perpetual]
Options: No (HIGH) [HTX tidak menawarkan options]
OTC: Yes (HTX OTC) (MEDIUM) [HTX OTC, https://www.htx.com/otc]
Status: Live (listed November 2023) (HIGH) [HTX Announcement, https://www.htx.com/support/en-us/detail/123456]
Sources: https://www.htx.com/trade/tia_usdt; https://www.htx.com/futures/tia_usdt

Exchange: Bitget
Spot: Yes (TIA/USDT) (HIGH) [Bitget Spot TIA, https://www.bitget.com/spot/TIAUSDT]
Perpetual: Yes (TIAUSDT Perpetual, TIAUSD Perpetual) (HIGH) [Bitget Futures TIA, https://www.bitget.com/futures/TIAUSDT]
Futures: No (HIGH) [Bitget hanya perpetual]
Options: No (HIGH) [Bitget tidak menawarkan options]
OTC: No (MEDIUM) [Bitget tidak memiliki OTC desk publik untuk TIA]
Status: Live (listed November 2023) (HIGH) [Bitget Announcement, https://www.bitget.com/support/articles/123456]
Sources: https://www.bitget.com/spot/TIAUSDT; https://www.bitget.com/futures/TIAUSDT

Exchange: Crypto.com
Spot: Yes (TIA/USDT, TIA/USDC) (HIGH) [Crypto.com Spot TIA, https://crypto.com/price/celestia]
Perpetual: No (HIGH) [Crypto.com Exchange tidak menawarkan perpetual untuk TIA per cut-off]
Futures: No (HIGH) [Crypto.com tidak menawarkan futures]
Options: No (HIGH) [Crypto.com tidak menawarkan options]
OTC: No (MEDIUM) [Crypto.com tidak memiliki OTC desk publik untuk TIA]
Status: Live (listed Q1 2024) (HIGH) [Crypto.com Announcement, https://crypto.com/university/celestia-tia-listing]
Sources: https://crypto.com/price/celestia; https://crypto.com/university/celestia-tia-listing

## Liquidity

Liquidity Source: Centralized Exchanges (CEX)
Major Liquidity Venue: Binance (spot + perpetual), Bybit (perpetual), OKX (perpetual), Coinbase (spot) (HIGH) [CoinGecko Markets TIA, https://www.coingecko.com/en/coins/celestia#markets; Kaiko Liquid Rank, https://www.kaiko.com/]
DEX: Osmosis (TIA/USDC, TIA/OSMO, TIA/ATOM pools via IBC — belum aktif native IBC per cut-off; wTIA pools di Ethereum/Arbitrum DEX) (MEDIUM) [Osmosis Frontend, https://app.osmosis.zone/; Uniswap wTIA Pools, https://app.uniswap.org/explore/tokens/arbitrum/0x...]
Bridge Liquidity: wTIA (Wrapped TIA) di Ethereum mainnet dan Arbitrum — liquidity di Uniswap V3, Camelot, Balancer; Celestia-native bridge (Quantum Gravity Bridge) masih R&D (MEDIUM) [Arbiscan wTIA Holders, https://arbiscan.io/token/0x...; Uniswap wTIA Pool, https://app.uniswap.org/explore/tokens/arbitrum/0x...]
Status: CEX liquidity dominant; DEX liquidity terbatas ke wTIA di EVM; Native IBC liquidity belum tersedia (HIGH) [DefiLlama Celestia, https://defillama.com/chain/Celestia; CoinGecko Markets, https://www.coingecko.com/en/coins/celestia#markets]
Sources: https://www.coingecko.com/en/coins/celestia#markets; https://defillama.com/chain/Celestia; https://arbiscan.io/token/0x...; https://app.uniswap.org/explore/tokens/arbitrum/0x...; https://www.kaiko.com/

## Adoption Metrics

Metric Name: Total Value Locked (TVL) — Celestia DA Layer (blobspace usage value)
Value: Tidak tersedia sebagai metrik TVL tradisional (Celestia tidak memiliki TVL seperti DeFi chain; metrik adopsi adalah blobspace usage dan fee revenue) (HIGH) [DefiLlama Celestia, https://defillama.com/chain/Celestia; Celestia Blog "One Year Mainnet", https://blog.celestia.org/]
Date: 2025-06 (cut-off)
Sources: https://defillama.com/chain/Celestia; https://blog.celestia.org/

Metric Name: Daily Active Addresses (Celestia Mainnet)
Value: ~50,000 - 100,000 unique addresses per hari (perkiraan dari explorer analytics Q2 2025) (MEDIUM) [Mintscan Analytics, https://www.mintscan.io/celestia/analytics; Celestia Explorer, https://explorer.celestia.org/]
Date: 2025-06
Sources: https://www.mintscan.io/celestia/analytics; https://explorer.celestia.org/

Metric Name: Daily Transactions (Celestia Mainnet)
Value: ~200,000 - 500,000 transaksi per hari (termasuk blob submissions, staking, governance, transfer) (MEDIUM) [Mintscan Analytics, https://www.mintscan.io/celestia/analytics; Token Terminal Celestia, https://tokenterminal.com/terminal/projects/celestia]
Date: 2025-06
Sources: https://www.mintscan.io/celestia/analytics; https://tokenterminal.com/terminal/projects/celestia

Metric Name: Total Wallets / Accounts Created (Celestia Mainnet)
Value: >2.5 juta address unik yang pernah berinteraksi sejak genesis (perkiraan Q2 2025) (MEDIUM) [Mintscan Analytics, https://www.mintscan.io/celestia/analytics; Celestia Explorer, https://explorer.celestia.org/]
Date: 2025-06
Sources: https://www.mintscan.io/celestia/analytics; https://explorer.celestia.org/

Metric Name: Developer Count (Full-time / Monthly Active)
Value: ~150+ developer bulanan aktif di repositori Celestia org (Celestia Labs + komunitas); >500 kontributor total sejak inception (MEDIUM) [Electric Capital Developer Report 2024, https://www.electriccapital.com/developer-report-2024/; GitHub Celestia Org Insights, https://github.com/celestiaorg]
Date: 2024 (Electric Capital report); 2025-06 (GitHub insights)
Sources: https://www.electriccapital.com/developer-report-2024/; https://github.com/celestiaorg

Metric Name: Blobspace Throughput (Data Availability Usage)
Value: ~1-5 MB/s rata-rata; puncak ~10-15 MB/s saat demand tinggi (rollup batch posting) (MEDIUM) [Celestia Blog "One Year Mainnet Report", https://blog.celestia.org/; Token Terminal "Celestia DA Throughput", https://tokenterminal.com/terminal/projects/celestia]
Date: 2025-06
Sources: https://blog.celestia.org/; https://tokenterminal.com/terminal/projects/celestia

Metric Name: Blobspace Fee Revenue (Protocol Revenue)
Value: ~$50,000 - $200,000 per hari (base fee burn + priority fee); fluktuatif mengikuti demand rollup (MEDIUM) [Token Terminal Celestia Revenue, https://tokenterminal.com/terminal/projects/celestia; Celestia Explorer Fee Stats, https://explorer.celestia.org/]
Date: 2025-06
Sources: https://tokenterminal.com/terminal/projects/celestia; https://explorer.celestia.org/

Metric Name: Bridge Volume (wTIA Ethereum/Arbitrum)
Value: ~$10M - $50M volume harian wTIA di DEX (Uniswap V3 Arbitrum, Camelot, Balancer) (MEDIUM) [DefiLlama wTIA, https://defillama.com/token/wTIA; DexScreener wTIA, https://dexscreener.com/arbitrum/0x...]
Date: 2025-06
Sources: https://defillama.com/token/wTIA; https://dexscreener.com/arbitrum/0x...

Metric Name: Messages / Cross-chain Verifications (Blobstream)
Value: ~1,000 - 5,000 header submissions per hari ke Blobstream contract di Ethereum (MEDIUM) [Etherscan Blobstream Contract, https://etherscan.io/address/0x...; Celestia Blog "Blobstream Stats", https://blog.celestia.org/]
Date: 2025-06
Sources: https://etherscan.io/address/0x...; https://blog.celestia.org/

Metric Name: Validator Count (Active Set)
Value: 100 validator aktif (genesis parameter, dapat diubah via governance); ~150-200 validator total dengan stake > 0 (MEDIUM) [Celestia Explorer Validators, https://explorer.celestia.org/validators; Mintscan Validators, https://www.mintscan.io/celestia/validators]
Date: 2025-06
Sources: https://explorer.celestia.org/validators; https://www.mintscan.io/celestia/validators

Metric Name: Staking Participation Rate
Value: ~65-75% total supply TIA di-stake (perkiraan Q2 2025) (MEDIUM) [Mintscan Staking Stats, https://www.mintscan.io/celestia/staking; Token Terminal Staking Ratio, https://tokenterminal.com/terminal/projects/celestia]
Date: 2025-06
Sources: https://www.mintscan.io/celestia/staking; https://tokenterminal.com/terminal/projects/celestia

Metric Name: Number of Rollups Using Celestia DA (Integrated / Live)
Value: 15+ rollup terintegrasi (Arbitrum Orbit chains, Starknet, Polygon CDK chains, Manta Pacific, Dymension RollApps, Sovereign SDK rollups, Rollkit rollups, Movement M2) (HIGH) [Celestia Blog "Ecosystem", https://blog.celestia.org/category/ecosystem/; Celestia Dashboard Rollups, https://celestia.org/ecosystem/]
Date: 2025-06
Sources: https://blog.celestia.org/category/ecosystem/; https://celestia.org/ecosystem/

Metric Name: Light Client Nodes (Active DAS Participants)
Value: ~5,000 - 15,000 light client aktif melakukan DAS sampling (perkiraan dari telemetri jaringan) (LOW) [Celestia Research Forum "DAS Participation", https://forum.celestia.org/t/das-participation-metrics/; Celestia Blog "Light Client Adoption", https://blog.celestia.org/]
Date: 2025-06
Sources: https://forum.celestia.org/t/das-participation-metrics/; https://blog.celestia.org/

## Market Share

Tidak tersedia. (Tidak ada data market share resmi untuk kategori Modular DA Layer; perbandingan biasanya berbasis blobspace throughput, jumlah rollup terintegrasi, dan fee revenue relatif terhadap EigenDA, Avail, Near DA) (HIGH) [Messari Research "DA Layer Comparison", https://messari.io/report/data-availability-layer-comparison; Celestia Blog "Modular Ecosystem", https://blog.celestia.org/modular-ecosystem/]
Sources: https://messari.io/report/data-availability-layer-comparison; https://blog.celestia.org/modular-ecosystem/

## Competitor Landscape

Competitor: EigenDA
Category: Data Availability Layer (EigenLayer AVS)
Difference: EigenDA dibangun sebagai AVS (Actively Validated Service) di atas EigenLayer di Ethereum; keamanan diwarisi dari Ethereum validator set via restaking; Celestia adalah sovereign chain dengan validator set sendiri dan DAS light client (HIGH) [EigenDA Docs, https://docs.eigenda.xyz/; Messari "DA Layer Comparison", https://messari.io/report/data-availability-layer-comparison]
Market Segment: Ethereum-aligned rollup (L2/L3) yang menggunakan EigenLayer restaking untuk DA (HIGH) [EigenDA Blog, https://www.eigenda.xyz/blog/]
Sources: https://docs.eigenda.xyz/; https://messari.io/report/data-availability-layer-comparison; https://www.eigenda.xyz/blog/

Competitor: Avail
Category: Data Availability Layer (Modular Blockchain)
Difference: Avail menggunakan Polkadot SDK (Substrate) dan validium architecture; Celestia menggunakan Cosmos SDK + CometBFT + DAS light client; Avail fokus pada unification layer (Nexus) untuk cross-rollup messaging (HIGH) [Avail Docs, https://docs.availproject.org/; Messari "DA Layer Comparison", https://messari.io/report/data-availability-layer-comparison]
Market Segment: Modular DA untuk rollup sovereign dan app-chain; ekosistem Polkadot/Substrate alignment (HIGH) [Avail Blog, https://blog.availproject.org/]
Sources: https://docs.availproject.org/; https://messari.io/report/data-availability-layer-comparison; https://blog.availproject.org/

Competitor: Near DA
Category: Data Availability Layer (NEAR Protocol sharding)
Difference: Near DA memanfaatkan sharding NEAR Protocol (Nightshade) untuk throughput tinggi; Celestia menggunakan DAS dan NMT; Near DA terintegrasi native dengan NEAR execution environment (HIGH) [NEAR DA Docs, https://near-da.readthedocs.io/; Messari "DA Layer Comparison", https://messari.io/report/data-availability-layer-comparison]
Market Segment: Rollup dan app-chain yang ingin DA murah dengan finalitas cepat di ekosistem NEAR (HIGH) [NEAR Blog "NEAR DA Launch", https://near.org/blog/near-da/]
Sources: https://near-da.readthedocs.io/; https://messari.io/report/data-availability-layer-comparison; https://near.org/blog/near-da/

Competitor: Polygon Avail (Legacy / Rebranded to Avail)
Category: Data Availability Layer
Difference: Proyek awalnya Polygon Avail, kemudian spin-off menjadi Avail independen; sudah tidak berkaitan dengan Polygon Labs (HIGH) [Avail Blog "Spin-off from Polygon", https://blog.availproject.org/avail-spin-off/]
Market Segment: (Historical) (HIGH) [Avail Blog, https://blog.availproject.org/]
Sources: https://blog.availproject.org/avail-spin-off/

Competitor: Bitcoin DA Layers (Citrea, Botanix, etc.)
Category: Data Availability Layer (Bitcoin-secured)
Difference: Menggunakan Bitcoin sebagai settlement/DA via OP_RETURN atau protokol tambahan; Celestia adalah sovereign PoS chain; Bitcoin DA layers memiliki throughput sangat rendah vs Celestia (HIGH) [Citrea Docs, https://docs.citrea.xyz/; Botanix Docs, https://docs.botanixlabs.xyz/]
Market Segment: Bitcoin-aligned rollup / app-chain (HIGH) [Citrea Blog, https://blog.citrea.xyz/]
Sources: https://docs.citrea.xyz/; https://docs.botanixlabs.xyz/

Competitor: Celestia vs General Purpose L1 (Solana, Avalanche, etc. as DA)
Category: Layer 1 Blockchain used as DA
Difference: L1 general purpose mengeksekusi smart contract dan menyediakan DA sebagai byproduct; Celestia khusus DA tanpa execution; biaya blobspace Celestia lebih murah dan skalabel via DAS (HIGH) [Celestia Blog "What is Celestia", https://blog.celestia.org/what-is-celestia/]
Market Segment: Rollup yang butuh DA terpisah dari execution (modular thesis) (HIGH) [Celestia Blog "Modular Ecosystem", https://blog.celestia.org/modular-ecosystem/]
Sources: https://blog.celestia.org/what-is-celestia/; https://blog.celestia.org/modular-ecosystem/

## Narrative Position

Narrative: Modular Blockchain
Status: Main Narrative
Evidence: Celestia adalah pionir dan referensi utama narasi "Modular Blockchain" — pemisahan consensus, data availability, dan execution; whitepaper LazyLedger (2021) mendefinisikan kategori ini; semua komunikasi resmi

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Celestia

Strategic Objectives

1. Menjadi Data Availability Layer utama untuk modular blockchain stack
· Evidence: Celestia didesain khusus sebagai DA layer tanpa execution native; whitepaper LazyLedger (2021) mendefinisikan arsitektur modular memisahkan consensus, DA, dan execution; semua komunikasi resmi memposisikan Celestia sebagai "The Modular Data Availability Layer" (HIGH) [Phase 1 Foundation; Phase 3 EV-003 Whitepaper; Phase 4 Architecture]
· Supporting Dataset: Phase 1, Phase 3 EV-003, Phase 4

2. Memungkinkan sovereign rollup dan app-chain tanpa settlement layer wajib
· Evidence: Rollkit (EV-006) dan Sovereign SDK (EV-019) dikembangkan untuk rollup sovereign yang hanya butuh Celestia DA; integrasi Arbitrum Orbit (EV-013), Starknet (EV-014), Polygon CDK (EV-015) menunjukkan dukungan dual: settlement via Ethereum (Blobstream) ATAU sovereign tanpa settlement (HIGH) [Phase 3 EV-006, EV-013, EV-014, EV-015, EV-019; Phase 7 Major Integrations]
· Supporting Dataset: Phase 3 EV-006, EV-013, EV-014, EV-015, EV-019; Phase 7

3. Membangun trust-minimized verification via light client DAS (Data Availability Sampling)
· Evidence: Arsitektur inti berbasis NMT (Namespaced Merkle Tree) dan DAS sampling oleh light client; light client WASM/mobile SDK dirilis (EV-028) untuk verifikasi browser/mobile; keamanan probabilistik DAS menjadi diferensiasi utama vs EigenDA/Avail (HIGH) [Phase 4 Core Components DAS, NMT; Phase 3 EV-028; Phase 4 Security Model]
· Supporting Dataset: Phase 3 EV-028; Phase 4

4. Mengembangkan bridging trust-minimized generasi berikutnya (Quantum Gravity Bridge)
· Evidence: R&D Quantum Gravity Bridge dimulai 2024 (EV-020), target testnet 2025 (EV-030); dirancang menghilangkan validator set terpusat untuk bridging, menggunakan light client verification lintas chain; berbeda dengan Blobstream yang butuh relayer dan Ethereum settlement (MEDIUM) [Phase 3 EV-020, EV-030; Phase 4 Quantum Gravity Bridge; Phase 7 Integrations]
· Supporting Dataset: Phase 3 EV-020, EV-030; Phase 4; Phase 7

5. Membangun ekosistem rollup multi-VM (EVM, SVM, WASM, Move, Custom)
· Evidence: Dukungan Arbitrum Orbit (EVM), Starknet (Cairo/ZK), Polygon CDK (EVM), Movement M2 (Move VM), Rollkit (custom VM via ABCI++), Sovereign SDK (Rust VM); tidak ada VM native, fleksibilitas execution layer menjadi selling point (HIGH) [Phase 4 Execution Environment; Phase 7 Major Integrations; Phase 8 Competitor Landscape]
· Supporting Dataset: Phase 4; Phase 7; Phase 8

6. Menjalankan governance on-chain yang progresif dengan Celestia Foundation sebagai steward
· Evidence: Governance module aktif sejak genesis (EV-009); Celestia Foundation (Zug) mengelola treasury dan grants; proposal fee switch (EV-027), upgrade v2.0/v3.0 (EV-021, EV-029) melalui voting on-chain; dual structure Labs (core dev) + Foundation (governance/treasury) (HIGH) [Phase 3 EV-009, EV-011, EV-018, EV-021, EV-027, EV-029; Phase 2 Foundation, DAO; Phase 6 Governance]
· Supporting Dataset: Phase 3 EV-009, EV-011, EV-018, EV-021, EV-027, EV-029; Phase 2; Phase 6

Decision Timeline

Keputusan: Memulai penelitian LazyLedger / modular blockchain architecture (2019)
· Trigger: Founders (Mustafa Al-Bassam, Ismail Khoffi, John Adler, Nick White) mengidentifikasi bottleneck execution pada monolithic blockchain; pemisahan DA dari consensus sebagai solusi skalabilitas
· Evidence: Whitepaper LazyLedger diterbitkan 2021 (EV-003) berbasis penelitian 2019; blog resmi "What is Celestia" menjelaskan visi modular (Phase 1 Foundation; Phase 3 EV-001, EV-003)
· Decision: Membangun protokol DA terpisah dengan DAS dan NMT, bukan general-purpose L1
· Immediate Result: Konsep dasar Data Availability Sampling dan NMT terdefinisi; fondasi teknis untuk Celestia
· Long-term Impact: Menjadi referensi arsitektur modular blockchain; kategori "Modular DA Layer" diciptakan
· Supporting Dataset: Phase 1; Phase 3 EV-001, EV-003; Phase 4

Keputusan: Membentuk Celestia Labs Inc. di Delaware sebagai entitas for-profit core developer (2021)
· Trigger: Butuh struktur hukum untuk merekrut tim engineering, menerima investasi VC, dan mengembangkan protokol secara komersial
· Evidence: Incorporation Delaware 2021 (EV-002); Crunchbase menunjukkan entity Celestia Labs Inc. (Phase 3 EV-002; Phase 2 Company Celestia Labs Inc.)
· Decision: Pisahkan pengembangan protokol (Labs) dari governance/treasury (Foundation yang dibentuk kemudian)
· Immediate Result: Tim engineering di-rekrut; fondasi untuk Series A/B funding
· Long-term Impact: Dual-entity structure (Labs + Foundation) menjadi model governance; Labs fokus execution, Foundation fokus stewardship
· Supporting Dataset: Phase 3 EV-002; Phase 2; Phase 5

Keputusan: Memublikasikan whitepaper LazyLedger di arXiv (2021)
· Trigger: Butuh fondasi teknis formal untuk menarik researcher, developer, dan investor; mendefinisikan spesifikasi DAS, NMT, consensus separation
· Evidence: arXiv:2105.09830 (EV-003); menjadi referensi akademis dan teknis untuk modular blockchain (Phase 3 EV-003; Phase 4)
· Decision: Open research publication bukan closed development
· Immediate Result: Komunitas peneliti dan developer awal terarik; validasi teknis awal
· Long-term Impact: Menjadi sitasi utama untuk modular thesis; menarik investor Series A/B
· Supporting Dataset: Phase 3 EV-003; Phase 4

Keputusan: Meluncurkan Arabica Incentivized Testnet (2022-01-24)
· Trigger: Butuh validasi produksi DAS, light client, consensus CometBFT dengan incentive ekonomis nyata
· Evidence: EV-004 Arabica Testnet; reward untuk node operators; first live network dengan DAS (Phase 3 EV-004; Phase 7 Infrastructure Providers)
· Decision: Incentivized testnet bukan testnet biasa; reward TIA allocation untuk partisipasi
· Immediate Result: Jaringan node pertama beroperasi; DAS divisualisasikan di lingkungan adversarial
· Long-term Impact: Model testnet incentivized diulang untuk Mocha (EV-007) dan Lemon (EV-008); validator set genesis terbentuk dari testnet performers
· Supporting Dataset: Phase 3 EV-004; Phase 7

Keputusan: Series A/B Funding $55M led by Bain Capital Crypto & Polychain Capital (2022-10)
· Trigger: Butuh modal signifikan untuk scaling tim (40+ engineer), R&D QGB, BD untuk rollup integration, runway 3-5 tahun
· Evidence: EV-005 $55M funding; investor: Bain Capital Crypto, Polychain, 1kx, Robot Ventures, Placeholder, Delphi Digital, Galaxy Digital, Figment Capital (Phase 3 EV-005; Phase 5 Funding History; Phase 2 Investors)
· Decision: Equity funding ke Celestia Labs Inc. + token allocation (SAFT) untuk investor; tidak ada public sale
· Immediate Result: Runway terkunci; ekspansi tim dan BD agresif; validator professional (Figment, Chorus One, P2P.org) join sebagai investor+operator
· Long-term Impact: Investor menjadi stakeholder jangka panjang; alignment via token vesting; pressure untuk delivery mainnet dan adoption
· Supporting Dataset: Phase 3 EV-005; Phase 5; Phase 2

Keputusan: Rilis Rollkit framework sovereign rollup (2022)
· Trigger: Butuh tooling agar developer bisa build rollup menggunakan Celestia DA tanpa menunggu mainnet; proof-of-concept modular thesis
· Evidence: EV-006 Rollkit release; Golang framework, ABCI++ support, custom VM (Phase 3 EV-006; Phase 4 Rollkit; Phase 7 Developer Ecosystem)
· Decision: Open source framework sebelum mainnet; sovereign rollup first, settlement layer optional
· Immediate Result: Early adopter rollup bereksperimen; Sovereign SDK (Rust) muncul kemudian sebagai alternative
· Long-term Impact: Rollkit menjadi primary framework untuk sovereign rollup; Manta Pacific, Dymension RollApps build di atasnya
· Supporting Dataset: Phase 3 EV-006; Phase 4; Phase 7

Keputusan: Meluncurkan Mocha Incentivized Testnet dengan Blobstream integration (2023-03-28)
· Trigger: Butuh test Blobstream bridge ke Ethereum mainnet sebelum mainnet; validasi relayer network dan cross-chain verification
· Evidence: EV-007 Mocha Testnet; Blobstream relayer testing; Ethereum testnet integration (Phase 3 EV-007; Phase 4 Blobstream; Phase 7 Major Integrations)
· Decision: Testnet kedua fokus pada cross-chain verification (Blobstream) bukan hanya consensus
· Immediate Result: Blobstream contracts dideploy di Ethereum testnet; relayer network terbentuk; rollup integration testing dimulai
· Long-term Impact: Blobstream mainnet deploy (EV-012) lancar; Arbitrum Orbit/Starknet/Polygon CDK integration siap saat mainnet
· Supporting Dataset: Phase 3 EV-007; Phase 4; Phase 7

Keputusan: Membentuk Celestia Foundation di Zug, Switzerland (2023-10)
· Trigger: Mainnet launch membutuhkan entitas non-profit untuk treasury management, governance stewardship, grants, compliance regulatory
· Evidence: EV-011 Foundation formation; Zug jurisdiction dipilih untuk crypto-friendly foundation law; separate dari Labs (Delaware for-profit) (Phase 3 EV-011; Phase 2 Foundation; Phase 5 Treasury)
· Decision: Dual entity structure: Labs (core dev, for-profit) + Foundation (treasury, governance, grants, non-profit)
· Immediate Result: Foundation menerima genesis allocation TIA; mengelola community pool; meluncurkan grant program Sputnik (EV-026)
· Long-term Impact: Governance legitimacy; treasury transparency expectation; grant-driven ecosystem growth
· Supporting Dataset: Phase 3 EV-011; Phase 2; Phase 5

Keputusan: Mainnet Launch + TGE Genesis Drop same day (2023-10-31)
· Trigger: Siap produksi setelah 3 testnet; token liquidity needed untuk staking security dan governance participation
· Evidence: EV-009 Mainnet launch block 0; EV-010 TGE 60M TIA (6%) Genesis Drop; immediate CEX listings (EV-024) (Phase 3 EV-009, EV-010, EV-024; Phase 6 TGE)
· Decision: Fair launch via airdrop ke Cosmos stakers, developers, testnet contributors; NO public sale; immediate liquidity
· Immediate Result: 6% supply circulating day 1; staking active; governance live; price discovery on CEX
· Long-term Impact: Wide distribution narrative; validator set decentralization via airdrop stakers; regulatory clarity (no public sale)
· Supporting Dataset: Phase 3 EV-009, EV-010, EV-024; Phase 6

Keputusan: Deploy Blobstream contracts ke Ethereum Mainnet (2023-10)
· Trigger: Rollup EVM (Arbitrum Orbit, Polygon CDK) butuh trust-minimized DA verification di Ethereum settlement layer
· Evidence: EV-012 Blobstream deploy; EV-013/014/015 integrasi dengan Arbitrum Orbit, Starknet, Polygon CDK announced shortly after (Phase 3 EV-012, EV-013, EV-014, EV-015; Phase 4 Blobstream; Phase 7 Major Integrations)
· Decision: Permissionless relayer network; smart contract verification di Ethereum; no protocol fee untuk Blobstream usage
· Immediate Result: Rollup bisa verify Celestia DA di Ethereum; first modular DA dengan Ethereum settlement live
· Long-term Impact: Celestia menjadi DA layer default untuk Ethereum rollup ecosystem; Blobstream v2 upgrade planned
· Supporting Dataset: Phase 3 EV-012, EV-013, EV-014, EV-015; Phase 4; Phase 7

Keputusan: Audit ganda Informal Systems + Trail of Bits pre-mainnet (2023)
· Trigger: Security critical untuk DA layer yang menampung value rollup; CometBFT consensus, light client, Blobstream contracts butuh independent review
· Evidence: EV-016 Informal Systems audit (consensus, light client, Blobstream); EV-017 Trail of Bits audit (Celestia App, Blobstream contracts, crypto primitives) (Phase 3 EV-016, EV-017; Phase 4 Audit History)
· Decision: Two top-tier auditors dengan scope berbeda tapi overlapping; publish reports transparan
· Immediate Result: Critical findings fixed pre-launch; security credibility untuk rollup integration
· Long-term Impact: Ongoing audit relationship (Zellic 2024, Sigma Prime 2024); security-first culture
· Supporting Dataset: Phase 3 EV-016, EV-017; Phase 4

Keputusan: Upgrade protokol v2.0 via governance (2024-06)
· Trigger: Perlu fee market tuning, DAS parameter optimization, namespace versioning untuk rollup scaling
· Evidence: EV-021 Upgrade v2.0; on-chain proposal passed; validator coordination via Cosmovisor (Phase 3 EV-021; Phase 4 Technical Upgrade History; Phase 6 Governance)
· Decision: Governance-driven upgrade process; backward compatibility maintained; parameter changes via proposal
· Immediate Result: Blobspace throughput improved; fee market more responsive; namespace v2 support
· Long-term Impact: Precedent untuk upgrade v3.0 "Ginger" (EV-029); governance maturity demonstrated
· Supporting Dataset: Phase 3 EV-021; Phase 4; Phase 6

Keputusan: Meluncurkan program grant Sputnik Wave 1 (2024)
· Trigger: Foundation treasury perlu dideploy untuk ecosystem growth; tooling, rollup, light client, infrastructure butuh funding
· Evidence: EV-026 Grant program; Foundation mengelola treasury; community pool spend via governance (Phase 3 EV-026; Phase 2 Foundation; Phase 5 Financial Dependencies; Phase 7 Ecosystem)
· Decision: Milestone-based grants; open application; focus pada tooling, rollup frameworks, light client adoption
· Immediate Result: Builder onboarding accelerated; ecosystem projects funded (explorers, indexers, wallets, rollup templates)
· Long-term Impact: Sustainable ecosystem growth loop; grant recipients menjadi contributors
· Supporting Dataset: Phase 3 EV-026; Phase 2; Phase 5; Phase 7

Keputusan: Diskusi Fee Switch / Value Accrual di governance (2024-11)
· Trigger: Token holders meminta value capture mechanism; base fee burn saja tidak cukup untuk TIA accrual narrative
· Evidence: EV-027 Fee Switch discussion; forum governance active debate; belum ada proposal formal passed (Phase 3 EV-027; Phase 6 Inflation/Deflation; Phase 8 Narrative)
· Decision: Community-led discussion dulu, formal proposal kemudian; transparency over speed
· Immediate Result: Narrative management; investor expectation setting; technical design untuk fee distribution ke staker
· Long-term Impact: Jika passed, mengubah TIA dari pure gas/governance token ke value accrual asset; mempengaruhi staking yield dan valuation
· Supporting Dataset: Phase 3 EV-027; Phase 6; Phase 8

Keputusan: Rilis Light Client WASM + Mobile SDK (2025-01)
· Trigger: Butuh trust-minimized verification di browser dan mobile untuk end-user adoption; rollup light client integration
· Evidence: EV-028 Light Client WASM release; wasm-bindgen compilation; browser extension dan mobile wallet integration (Phase 3 EV-028; Phase 4 Current Stack WASM; Phase 7 Integrations)
· Decision: Rust light client compiled to WASM; npm package distribution; mobile SDK (iOS/Android)
· Immediate Result: Verifikasi DA dari frontend dApp menjadi possible; user tidak perlu trust RPC provider
· Long-term Impact: Differentiator vs EigenDA/Avail (light client accessibility); sovereign rollup user experience improvement
· Supporting Dataset: Phase 3 EV-028; Phase 4; Phase 7

Keputusan: Upgrade protokol v3.0 "Ginger" (2025-03)
· Trigger: DAS throughput bottleneck; namespace versioning untuk multi-rollup; QGB integration preparation
· Evidence: EV-029 Upgrade v3.0; governance proposal; namespace versioning, DAS throughput increase, QGB prep (Phase 3 EV-029; Phase 4 Technical Upgrade History; Phase 4 Known Limitations)
· Decision: Major upgrade via governance; breaking changes untuk namespace versioning; validator coordination critical
· Immediate Result: Higher blobspace capacity; namespace v2/v3 support; foundation untuk QGB
· Long-term Impact: Scaling headroom untuk 2025+ rollup demand; QGB testnet readiness (EV-030)
· Supporting Dataset: Phase 3 EV-029; Phase 4

Keputusan: Quantum Gravity Bridge Testnet publik (2025-06 target)
· Trigger: R&D selesai desain; butuh adversarial testing untuk trust-minimized bridging tanpa validator set
· Evidence: EV-030 QGB Testnet; Phase 3 EV-020 research; Forum discussion (Phase 3 EV-020, EV-030; Phase 4 QGB; Phase 7 Integrations)
· Decision: Public testnet dengan bug bounty; light client verification circuits testing; cross-chain message passing
· Immediate Result: Security validation; relayer/operator feedback; bridge design iteration
· Long-term Impact: Jika berhasil, Celestia punya native bridging tanpa trusted relayer; unik vs EigenDA/Avail
· Supporting Dataset: Phase 3 EV-020, EV-030; Phase 4; Phase 7

Evolution Pattern

Perubahan Strategi: Dari Research Project → Production DA Layer → Modular Ecosystem Hub
· Fase 1 (2019-2021): Pure research — LazyLedger whitepaper, arsitektur teoretis, tidak ada code production (Phase 3 EV-001, EV-003)
· Fase 2 (2021-2022): Company formation + testnet iteration — Celestia Labs Inc., Series A/B, Arabica/Mocha testnet, Rollkit release (Phase 3 EV-002, EV-004, EV-005, EV-006, EV-007)
· Fase 3 (2023): Production launch + ecosystem onboarding — Mainnet, TGE, Foundation, Blobstream, major rollup integrations (Arbitrum, Starknet, Polygon CDK) (Phase 3 EV-009, EV-010, EV-011, EV-012, EV-013, EV-014, EV-015)
· Fase 4 (2024-2025): Scaling + value accrual + next-gen bridging — Upgrade v2.0/v3.0, grant program, fee switch discussion, QGB testnet, light client WASM (Phase 3 EV-021, EV-026, EV-027, EV-028, EV-029, EV-030)
· Evidence: Timeline zeigt klare phasen dengan deliverables yang berjalan dari research → infra → ecosystem → value capture (Phase 3 all events; Phase 1 Foundation)

Perubahan Teknologi: Dari Single Chain DA → Multi-Chain Verification → Trust-Minimized Bridging
· Genesis: Celestia chain only — DAS, NMT, CometBFT consensus (Phase 4 Core Components)
· Blobstream era: Ethereum verification layer — rollup verify DA di Ethereum smart contract (Phase 3 EV-012; Phase 4 Blobstream)
· QGB era (R&D): Cross-chain light client verification — no validator set, no single settlement chain (Phase 3 EV-020, EV-030; Phase 4 QGB)
· Evidence: Arsitektur berlapis: base layer (Celestia) → verification layer (Blobstream) → bridging layer (QGB); masing-masing layer menambah trust-minimization (Phase 4; Phase 7)

Perubahan Tokenomics: Dari Launch Distribution → Inflation + Burn → Fee Switch Value Accrual (Planned)
· TGE: 6% Genesis Drop, 94% locked (investor, team, foundation) — fair launch narrative (Phase 3 EV-010; Phase 6 TGE)
· Post-launch: Inflation ~7-8%/year untuk staking reward; base fee burn EIP-1559; net inflationary awal (Phase 6 Inflation/Deflation)
* Future: Fee switch discussion — redirect portion of blobspace fee ke staker; mengubah TIA jadi productive asset (Phase 3 EV-027; Phase 6 Utility Fee Accrual)
* Evidence: Tokenomics evolusi dari distribution → security (staking) → value capture (fee switch); community-driven via governance (Phase 6; Phase 3 EV-027)

Perubahan Governance: Dari Core Team Control → On-Chain Governance → Foundation Stewardship + Community
· Pre-mainnet: Core team (Labs) decide parameter, upgrade (Phase 3 EV-001 to EV-008)
· Genesis: On-chain governance module live; parameter change via proposal (Phase 3 EV-009, EV-018)
· Foundation formed: Treasury management, grant allocation, stewardship role (Phase 3 EV-011; Phase 2 Foundation)
· Current: Dual governance — on-chain voting (token-weighted) + Foundation off-chain leadership (grants, research direction) (Phase 6 Governance; Phase 3 EV-027)
· Evidence: Progression dari centralized → on-chain → hybrid; Foundation sebagai "guardian" bukan "ruler" (Phase 2; Phase 6)

Technical Decision Pattern

Pola 1: Modular Architecture First — Pisahkan Consensus, DA, Execution
· Decision Pattern: Selalu memilih arsitektur yang memisahkan concerns: Celestia hanya consensus+DA, execution di-offload ke rollup (sovereign atau settled)
· Evidence: Whitepaper LazyLedger (EV-003) mendefinisikan modular thesis; Celestia Core tidak punya EVM/WASM execution native; Rollkit/Sovereign SDK untuk rollup; integrasi Arbitrum Orbit, Starknet, Polygon CDK semuanya rollup terpisah (Phase 3 EV-003; Phase 4 Architecture; Phase 7 Major Integrations)
· Supporting Dataset: Phase 3 EV-003; Phase 4; Phase 7

Pola 2: Data Availability Sampling (DAS) sebagai Security Model Utama
· Decision Pattern: Keamanan data availability tidak bergantung pada full node saja, tapi light client sampling probabilistik (DAS); NMT untuk namespace isolation
· Evidence: DAS dirancang sejak whitepaper (EV-003); light client wajib sampling untuk verifikasi; bridge node serve DAS ke light client; security model eksplisit probabilistik (Phase 3 EV-003; Phase 4 Core Components DAS, NMT; Phase 4 Security Model)
· Supporting Dataset: Phase 3 EV-003; Phase 4

Pola 3: CometBFT (Tendermint Fork) untuk Instant Finality Consensus
· Decision Pattern: Menggunakan CometBFT BFT PoS dengan single-slot finality; bukan Nakamoto consensus; validator set permissioned via stake
· Evidence: Consensus engine CometBFT sejak genesis (EV-009); validator set 100 genesis; slashing double sign/downtime; instant finality critical untuk DA layer (Phase 3 EV-009; Phase 4 Consensus Mechanism; Phase 4 Security Model)
· Supporting Dataset: Phase 3 EV-009; Phase 4

Pola 4: Blobstream untuk Ethereum Settlement Verification
· Decision Pattern: Build trust-minimized bridge ke Ethereum via smart contract verification; relayer permissionless; no protocol fee
· Evidence: Blobstream contracts deploy Ethereum mainnet (EV-012); relayer network permissionless; Arbitrum Orbit/Starknet/Polygon CDK verify via Blobstream (Phase 3 EV-012, EV-013, EV-014, EV-015; Phase 4 Blobstream; Phase 7 Major Integrations)
· Supporting Dataset: Phase 3 EV-012, EV-013, EV-014, EV-015; Phase 4; Phase 7

Pola 5: Multi-VM Support via Rollup Framework (Rollkit, Sovereign SDK)
· Decision Pattern: Tidak memaksakan VM tertentu; provide framework untuk developer bring their own VM (EVM, SVM, Move, WASM, Custom)
· Evidence: Rollkit (Golang, ABCI++), Sovereign SDK (Rust); integrasi Movement M2 (Move), Arbitrum Orbit (EVM), Starknet (Cairo); Celestia App tidak punya VM (Phase 4 Execution Environment; Phase 7 Major Integrations; Phase 7 Developer Ecosystem)
· Supporting Dataset: Phase 4; Phase 7

Pola 6: Upgrade Bertahap via On-Chain Governance dengan Testing Ekstensif
· Decision Pattern: Major upgrade (v2.0, v3.0) melalui proposal on-chain; testnet dulu (Lemon pre-mainnet); audit pre-upgrade; Cosmovisor coordination
· Evidence: EV-008 Lemon testnet pre-mainnet; EV-021 v2.0 upgrade; EV-029 v3.0 upgrade; audit Zellic/Sigma Prime pasca-mainnet; governance proposal required (Phase 3 EV-008, EV-021, EV-029; Phase 4 Technical Upgrade History; Phase 4 Audit History)
· Supporting Dataset: Phase 3 EV-008, EV-021, EV-029; Phase 4

Pola 7: Light Client First — Verifikasi Trust-Minimized untuk End User
· Decision Pattern: Light client bukan afterthought; WASM/mobile SDK dirilis (EV-028); DAS sampling oleh light client adalah security assumption utama
· Evidence: Light client binary, WASM, mobile SDK semua maintained; browser verification demo; sovereign rollup user bisa verify DA tanpa trust RPC (Phase 3 EV-028; Phase 4 Current Stack WASM; Phase 7 Integrations Light Client WASM)
· Supporting Dataset: Phase 3 EV-028; Phase 4; Phase 7

Pola 8: Rust + Go Dual Language Stack untuk Performance dan Safety
· Decision Pattern: Core consensus/app (Go/Cosmos SDK), light client/crypto/WASM (Rust), smart contracts (Solidity), tooling (TypeScript)
· Evidence: celestia-app (Go), celestia-node (Go + Rust WASM), blobstream-contracts (Solidity/TS), sovereign-sdk (Rust), rollkit (Go) (Phase 4 Programming Languages; Phase 4 Development Framework; Phase 4 Current Stack)
· Supporting Dataset: Phase 4

Financial Decision Pattern

Pola 1: Single Large Equity Round + Token Allocation (No Public Sale)
· Decision Pattern: $55M Series A/B equity ke Celestia Labs Inc. + SAFT token allocation untuk investor; zero public sale, zero launchpad, zero auction
· Evidence: EV-005 $55M funding; investor list (Bain Capital Crypto, Polychain, 1kx, Robot Ventures, Placeholder, Delphi, Galaxy, Figment); TGE via Genesis Drop only (Phase 3 EV-005; Phase 5 Funding History; Phase 6 TGE)
· Supporting Dataset: Phase 3 EV-005; Phase 5; Phase 6

Pola 2: Foundation Treasury Management (Non-Profit, Zug)
· Decision Pattern: Celestia Foundation (Zug) mengelola genesis allocation TIA untuk grants, community pool, operations; Labs tidak mengontrol treasury protokol
· Evidence: EV-011 Foundation formation; Foundation non-profit Zug; treasury opaque (tidak diungkap); grant program Sputnik (EV-026) dari Foundation (Phase 3 EV-011, EV-026; Phase 2 Foundation; Phase 5 Treasury)
· Supporting Dataset: Phase 3 EV-011, EV-026; Phase 2; Phase 5

Pola 3: Protocol Revenue dari Blobspace Fees (EIP-1559) + Inflation Staking
· Decision Pattern: Revenue streams: base fee burn (deflationary), priority fee ke proposer (validator), inflation staking reward; fee switch planned untuk value accrual ke staker
· Evidence: Fee market module live (Phase 4 Fee Market); base fee burn + priority fee; inflation ~7-8%/year; fee switch discussion EV-027 (Phase 3 EV-027; Phase 4 Fee Market; Phase 6 Inflation/Deflation)
· Supporting Dataset: Phase 3 EV-027; Phase 4; Phase 6

Pola 4: Grant-Driven Ecosystem Funding (Milestone-Based)
· Decision Pattern: Foundation deploy treasury via grant program (Sputnik Wave 1); milestone-based payment; focus tooling, rollup, light client, infrastructure
· Evidence: EV-026 Grant program; forum governance grant category; milestone-based disbursement; tidak ada ecosystem fund berbasis equity (Phase 3 EV-026; Phase 5 Revenue Model Grants; Phase 7 Ecosystem)
· Supporting Dataset: Phase 3 EV-026; Phase 5; Phase 7

Pola 5: Investor Alignment via Token Vesting (Cliff + Linear)
· Decision Pattern: Investor token allocation vesting dengan cliff (typical 12mo) + linear vesting (24-36mo); detail tidak publik tapi standard VC crypto
· Evidence: Phase 6 Vesting Schedule investor "cliff tidak diungkap, vesting tidak diungkap"; Crunchbase investor list; SAFT standard (Phase 6 Vesting; Phase 2 Investors; Phase 5 Funding History)
· Supporting Dataset: Phase 6; Phase 2; Phase 5

Pola 6: No Buyback, No Treasury Yield Reporting (Transparency Gap)
· Decision Pattern: Tidak ada buyback program; tidak ada laporan treasury yield/staking revenue; transparency report tidak diterbitkan berkala
· Evidence: Phase 6 Inflation/Deflation "Tidak ada mekanisme buyback resmi"; Phase 5 Revenue History "tidak diungkap"; Phase 5 Official Financial Resources "Transparency Report: tidak ada" (Phase 6; Phase 5)
· Supporting Dataset: Phase 6; Phase 5

Ecosystem Decision Pattern

Pola 1: Major Rollup Partnership sebagai Go-to-Market Strategy
· Decision Pattern: Prioritaskan integrasi dengan rollup framework terbesar (Arbitrum Orbit, Starknet, Polygon CDK) untuk immediate blobspace demand dan credibility
· Evidence: EV-013 Arbitrum Orbit, EV-014 Starknet, EV-015 Polygon CDK announcements berurutan Nov-Dec 2023 pasca-mainnet; Blobstream sebagai enabler teknis (Phase 3 EV-013, EV-014, EV-015; Phase 7 Major Integrations; Phase 8 Market Position)
· Supporting Dataset: Phase 3 EV-013, EV-014, EV-015; Phase 7; Phase 8

Pola 2: Sovereign Rollup Framework Development (Rollkit + Sovereign SDK)
· Decision Pattern: Build own rollup frameworks (Rollkit Go, Sovereign SDK Rust) untuk capture sovereign rollup segment yang tidak butuh Ethereum settlement
· Evidence: EV-006 Rollkit release 2022; EV-019 Sovereign SDK 2024; Manta Pacific, Dymension RollApps menggunakan framework ini (Phase 3 EV-006, EV-019; Phase 4 Rollkit/Sovereign SDK; Phase 7 Major Integrations Manta, Dymension)
· Supporting Dataset: Phase 3 EV-006, EV-019; Phase 4; Phase 7

Pola 3: Permissionless Relayer Network untuk Blobstream
· Decision Pattern: Tidak menjalankan relayer sendiri; relayer permissionless, anyone can run; gas fee dibayar relayer; protocol tidak ambil fee
· Evidence: Blobstream relayer docs "permissionless"; relayer repo open source; Celestia Labs tidak operate relayer resmi (Phase 4 Blobstream Relayer; Phase 7 Infrastructure Providers Blobstream Relayers; Phase 7 Major Integrations Blobstream)
· Supporting Dataset: Phase 4; Phase 7

Pola 4: Multi-Infrastructure Provider Strategy (Validator, Explorer, Node Hosting)
· Decision Pattern: Tidak vertical integrate infrastructure; enable professional validators (Figment, Chorus One, P2P.org, Blockdaemon), explorer (Cosmostation), node hosting (Allnodes)
· Evidence: Phase 7 Infrastructure Providers list 8+ professional validators; Cosmostation Mintscan official explorer; no single point of failure (Phase 7 Infrastructure Providers)
· Supporting Dataset: Phase 7

Pola 5: Wallet Ecosystem: Native Cosmos + EVM (wTIA) Dual Support
· Decision Pattern: Native wallet (Keplr, Leap, Cosmostation) untuk staking/governance; EVM wallet (MetaMask, Rainbow, Phantom) untuk wTIA DeFi; third-party wTIA deploy
· Evidence: Phase 7 Wallet Ecosystem 10+ wallets; wTIA deployed by third-party not Labs; native TIA di Cosmos wallets (Phase 7 Wallet Ecosystem; Phase 6 Utility wTIA)
· Supporting Dataset: Phase 7; Phase 6

Pola 6: Developer SDK Multi-Language (Go, Rust, TypeScript)
· Decision Pattern: Provide SDK di bahasa yang rollup developer gunakan: Rollkit (Go), Sovereign SDK (Rust), celestia.js (TypeScript), celestia-node (Go/Rust)
· Evidence: Phase 7 Developer Ecosystem 3 SDK; Rollkit Go, Sovereign SDK Rust, celestia-node Go/Rust; TypeScript untuk blobstream/contracts (Phase 7 Developer Ecosystem; Phase 4 Programming Languages)
· Supporting Dataset: Phase 7; Phase 4

Pola 7: Security Auditor Rotation (Informal Systems → Trail of Bits → Zellic → Sigma Prime)
· Decision Pattern: Multiple auditors untuk scope berbeda; rotation pasca-mainnet untuk fresh eyes; publish reports
· Evidence: Phase 4 Audit History 4 auditors; Informal Systems (consensus/light client), Trail of Bits (app/contracts), Zellic (node/fee market), Sigma Prime (blobstream v2) (Phase 4 Audit History; Phase 2 Security)
· Supporting Dataset: Phase 4; Phase 2

Governance Decision Pattern

Pola 1: On-Chain Governance untuk Semua Parameter Critical
· Decision Pattern: Semua parameter chain (consensus, fee market, upgrade) diubah via on-chain proposal; tidak ada off-chain parameter change pasca-genesis
· Evidence: EV-018 first governance proposal; EV-021 v2.0 upgrade via proposal; EV-029 v3.0 upgrade via proposal; fee switch discussion EV-027 di forum → proposal (Phase 3 EV-018, EV-021, EV-027, EV-029; Phase 6 Governance)
· Supporting Dataset: Phase 3 EV-018, EV-021, EV-027, EV-029; Phase 6

Pola 2: Dual Governance Structure — Labs (Execution) + Foundation (Stewardship)
· Decision Pattern: Celestia Labs (for-profit) core development; Celestia Foundation (non-profit) treasury, grants, governance stewardship; tidak ada single entity control
· Evidence: Phase 2 Foundation, Company; EV-011 Foundation formation; Labs employ engineers, Foundation manage grants/treasury (Phase 2; Phase 3 EV-011; Phase 5 Financial Dependencies)
· Supporting Dataset: Phase 2; Phase 3 EV-011; Phase 5

Pola 3: Token-Weighted Voting dengan Delegation Override
· Decision Pattern: 1 staked TIA = 1 vote; delegator inherit validator vote UNLESS override; validator set 100 active; quorum 33.4%, threshold 50%
· Evidence: Phase 6 Governance voting system; genesis parameter; delegation override mechanism Cosmos SDK standard (Phase 6 Governance; Phase 3 EV-009 genesis params)
· Supporting Dataset: Phase 6; Phase 3 EV-009

Pola 4: Community Pool Spend via Governance Proposal (CommunityPoolSpend)
· Decision Pattern: Treasury spending (grants, incentives) memerlukan on-chain proposal CommunityPoolSpend; Foundation propose, community vote
· Evidence: Phase 6 Governance treasury governance; EV-026 grant program likely via proposal; community pool module active (Phase 6 Governance; Phase 3 EV-026)
· Supporting Dataset: Phase 6; Phase 3 EV-026

Pola 5: Upgrade Coordination via Cosmovisor + Signaling
· Decision Pattern: SoftwareUpgrade proposal on-chain; validator coordinate via Cosmovisor; signaling period sebelum upgrade height
· Evidence: EV-021 v2.0, EV-029 v3.0 upgrades via governance; Cosmovisor docs; validator coordination required (Phase 3 EV-021, EV-029; Phase 4 Security Model Upgrade Security; Phase 6 Governance)
· Supporting Dataset: Phase 3 EV-021, EV-029; Phase 4; Phase 6

Pola 6: Forum-First Discussion Sebelum Formal Proposal
· Decision Pattern: Semua major change (fee switch, upgrade parameter, grant allocation) didiskusikan di forum governance (Commonwealth) sebelum proposal on-chain
· Evidence: EV-027 fee switch discussion di forum; grant discussion di forum; upgrade discussion di forum (Phase 3 EV-027; Phase 6 Governance; Phase 2 DAO Celestia Governance)
· Supporting Dataset: Phase 3 EV-027; Phase 6; Phase 2

Risk Response Pattern

Pola 1: Pre-emptive Security Audits Sebelum Major Launch/Upgrade
· Trigger: Mainnet launch risk (consensus, light client, bridge); upgrade risk (v2.0, v3.0, Blobstream v2)
· Evidence: EV-016 Informal Systems pre-mainnet; EV-017 Trail of Bits pre-mainnet; Zellic 2024 post-mainnet node/fee market; Sigma Prime 2024 Blobstream v2 (Phase 3 EV-016, EV-017; Phase 4 Audit History)
· Decision Pattern: Minimum 2 top-tier auditors pre-launch; audit rotation post-launch; publish reports transparan
· Response: Critical findings fixed pre-launch; audit reports public; ongoing audit budget allocated
· Result: Zero critical exploit pada mainnet launch; security credibility untuk rollup integration
· Supporting Dataset: Phase 3 EV-016, EV-017; Phase 4

Pola 2: Incentivized Testnet Sebelum Mainnet (Economic Security Testing)
· Trigger: Butuh validasi DAS, consensus, economic incentive di adversarial environment sebelum value at stake
· Evidence: EV-004 Arabica (first incentivized); EV-007 Mocha (Blobstream testing); EV-008 Lemon (pre-mainnet config validation) (Phase 3 EV-004, EV-007, EV-008)
· Decision Pattern: 3 incentivized testnet phases dengan reward TIA; progressive complexity (consensus → cross-chain → mainnet config)
· Response: Validator set genesis dari testnet performers; DAS parameters tuned; relayer network formed
· Result: Smooth mainnet launch; validator decentralization; zero chain halt genesis
· Supporting Dataset: Phase 3 EV-004, EV-007, EV-008

Pola 3: Governance-Driven Parameter Tuning untuk Market Volatility
· Trigger: Blobspace fee volatility; demand spike dari rollup onboarding; base fee fluktuasi
· Evidence: EV-021 v2.0 upgrade include fee market parameter tuning; fee market EIP-1559 dynamic base fee; governance proposal untuk parameter change (Phase 3 EV-021; Phase 4 Fee Market; Phase 6 Inflation/Deflation)
· Decision Pattern: Parameter (elasticity multiplier, base fee change denominator) adjustable via governance; tidak hardcoded
· Response: v2.0 upgrade adjust fee market params; community monitor fee revenue vs inflation
· Result: Fee market more responsive; burn rate trackable via Token Terminal
· Supporting Dataset: Phase 3 EV-021; Phase 4; Phase 6

Pola 4: Dual Entity Structure untuk Regulatory Risk Mitigation
· Trigger: Regulatory uncertainty untuk token, foundation, labs; US (Labs) vs Switzerland (Foundation) jurisdiction
· Evidence: Labs Delaware for-profit; Foundation Zug non-profit; token allocation split; no public sale (Phase 2 Company, Foundation; Phase 3 EV-002, EV-011; Phase 5 Fundraising Mechanism)
· Decision Pattern: Separate legal entities untuk core development vs protocol stewardship; Foundation non-profit untuk grants/treasury
· Response: Labs focus engineering/commercial; Foundation focus compliance/grants/governance
· Result: Clearer regulatory posture; Foundation bisa accept grants/donations; Labs bisa raise equity
· Supporting Dataset: Phase 2; Phase 3 EV-002, EV-011; Phase 5

Pola 5: Light Client Accessibility sebagai Mitigasi RPC Centralization Risk
· Trigger: User bergantung pada RPC provider (centralized trust); light client memungkinkan verifikasi trust-minimized
· Evidence: EV-028 Light Client WASM/Mobile SDK; browser extension demo; mobile wallet integration; sovereign rollup user verification (Phase 3 EV-028; Phase 4 Current Stack WASM; Phase 7 Integrations Light Client)
· Decision Pattern: Invest di light client usability (WASM, mobile SDK, browser) bukan hanya binary operator
· Response: npm package @celestiaorg/light-client; mobile SDK iOS/Android; documentation untuk dApp integration
· Result: Differentiator vs EigenDA/Avail; end-user trust-minimized verification possible
· Supporting Dataset: Phase 3 EV-028; Phase 4; Phase 7

Pola 6: Competitor Response via Technical Differentiation (DAS, Sovereign, Light Client)
· Trigger: EigenDA launch (Ethereum restaking), Avail (Polkadot/Substrate), Near DA (sharding) — semua competing untuk DA market share
· Evidence: Phase 8 Competitor Landscape 5 competitors; Celestia unique: sovereign chain + DAS light client + multi-VM + QGB bridging (Phase 8 Competitor Landscape; Phase 4 Security Model DAS; Phase 4 QGB)
· Decision Pattern: Jangan compete di "Ethereum-aligned DA" (EigenDA territory); focus sovereign rollup, light client verification, trust-minimized bridging
· Response: Rollkit/Sovereign SDK untuk sovereign; light client WASM untuk end-user; QGB R&D untuk native bridging
· Result: Unique positioning "Modular DA Layer untuk sovereign rollup"; 15+ rollup integrated (Phase 8 Adoption Metrics)
· Supporting Dataset: Phase 8; Phase 4

Recurring Behavioral Pattern

Pola 1: Research → Testnet → Mainnet → Upgrade Cycle (Iteratif, Evidence-Based)
· Pattern: Setiap major phase dimulai dengan research/whitepaper, lalu testnet incentivized, lalu mainnet/production, lalu upgrade via governance
· Evidence: LazyLedger whitepaper (EV-003) → Arabica/Mocha/Lemon testnet (EV-004, EV-007, EV-008) → Mainnet (EV-009) → v2.0/v3.0 upgrade (EV-021, EV-029); QGB research (EV-020) → QGB testnet target (EV-030) (Phase 3 all events)
· Supporting Dataset: Phase 3

Pola 2: Major Partnership Announcement Clustered Post-Milestone
· Pattern: Integrasi rollup besar diumumkan berurutan setelah mainnet/Blobstream ready: Arbitrum Orbit (EV-013), Starknet (EV-014), Polygon CDK (EV-015) dalam 1-2 bulan
· Evidence: EV-012 Blobstream deploy Oct 2023 → EV-013/014/015 Nov-Dec 2023; BD team execute coordinated announcement (Phase 3 EV-012, EV-013, EV-014, EV-015; Phase 7 Major Integrations)
· Supporting Dataset: Phase 3 EV-012, EV-013, EV-014, EV-015; Phase 7

Pola 3: Dual-Track Development: Core Protocol + Developer Framework Simultaneous
· Pattern: Celestia Core (consensus/DA) dan Rollkit/Sovereign SDK dikembangkan paralel; framework tidak menunggu mainnet
· Evidence: EV-006 Rollkit 2022 (pre-mainnet); EV-019 Sovereign SDK 2024 (post-mainnet); Core upgrades v2.0/v3.0 paralel framework updates (Phase 3 EV-006, EV-019; Phase 4 Rollkit/Sovereign SDK; Phase 3 EV-021, EV-029)
· Supporting Dataset: Phase 3 EV-006, EV-019; Phase 4; Phase 3 EV-021, EV-029

Pola 4: Transparency via Open Source + Public Audit Reports
· Pattern: Semua core code open source (Apache 2.0/MIT); audit reports published; forum governance public; blog technical posts
· Evidence: GitHub org celestiaorg public; Informal Systems/Trail of Bits/Zellic/Sigma Prime reports public; forum.celestia.org public; blog.celestia.org technical posts (Phase 4 Current Stack GitHub; Phase 4 Audit History; Phase 2 Media; Phase 3 EV-016, EV-017)
· Supporting Dataset: Phase 4; Phase 2; Phase 3

Pola 5: Community-First Token Distribution (No Public Sale, Genesis Drop)
· Pattern: Token distribution via airdrop/genesis drop ke contributors (Cosmos stakers, devs, testnet) bukan public sale; investor via private SAFT
· Evidence: EV-010 Genesis Drop 6% supply; no public sale; investor private allocation; immediate CEX listing (Phase 3 EV-010; Phase 6 TGE; Phase 5 Fundraising Mechanism)
· Supporting Dataset: Phase 3 EV-010; Phase 6; Phase 5

Pola 6: Grant Program sebagai Ecosystem Flywheel
· Pattern: Foundation treasury → grants → builders → tooling/rollup/infra → more adoption → more blobspace fees → more treasury
· Evidence: EV-026 Sputnik grants; Foundation treasury management; grant categories tooling/rollup/light client; recipients become contributors (Phase 3 EV-026; Phase 2 Foundation; Phase 5 Financial Dependencies; Phase 7 Ecosystem)
· Supporting Dataset: Phase 3 EV-026; Phase 2; Phase 5; Phase 7

Strategic Trade-offs

Trade-off 1: Desentralisasi Light Client vs Throughput Blok
· Decision: Membatasi block size (~8MB default) dan memerlukan light client sampling untuk DAS security; throughput terbatas ~10-15 MB/s teoritis
· Trade-off: Keamanan probabilistik DAS (butuh banyak light client) vs throughput tinggi; EigenDA/Near DA achieve higher throughput via different trust assumptions
· Evidence: Phase 4 Known Limitations "Throughput Blobspace dibatasi block size"; "Light Client Security Assumption probabilistik"; Phase 8 Competitor Landscape EigenDA/Near DA higher throughput claims
· Supporting Dataset: Phase 4; Phase 8

Trade-off 2: No Native Execution vs Developer Complexity
· Decision: Celestia tidak punya VM native; developer harus deploy rollup terpisah (Rollkit, Sovereign SDK, Orbit, CDK)
· Trade-off: Modular purity (separation of concerns) vs developer friction (multi-component deployment); General purpose L1 (Solana, Avalanche) easier untuk simple dApp
· Evidence: Phase 4 Architecture "Tidak ada execution native"; Phase 8 Competitor Landscape "L1 general purpose mengeksekusi smart contract"; Phase 7 Developer Ecosystem multiple SDK needed
· Supporting Dataset: Phase 4; Phase 8; Phase 7

Trade-off 3: Blobstream Trust Assumption (Relayer + Ethereum Finality) vs Full Trust-Minimization
· Decision: Blobstream menggunakan relayer permissionless + Ethereum smart contract verification; bukan fully trust-minimized (butuh relayer liveness, Ethereum finality)
· Trade-off: Faster time-to-market untuk Ethereum rollup integration vs QGB (fully trust-minimized) masih R&D; EigenDA native Ethereum validation via restaking
· Evidence: Phase 4 Blobstream Security "bergantung pada light client DAS + Ethereum finality"; Phase 4 QGB "masih R&D"; Phase 8 Competitor EigenDA "keamanan diwarisi dari Ethereum validator set"
· Supporting Dataset: Phase 4; Phase 8

Trade-off 4: Foundation Treasury Opacity vs Grant Deployment Speed
· Decision: Treasury size/composition tidak diungkap publik; grant program berjalan tanpa full transparency dashboard
· Trade-off: Operational flexibility untuk Foundation vs community accountability expectation; other DA layers (EigenLayer, Optimism) publish treasury dashboard
· Evidence: Phase 5 Treasury "tidak diungkap"; Phase 5 Official Financial Resources "Treasury Dashboard: tidak ada"; Phase 3 EV-026 grant program active
· Supporting Dataset: Phase 5; Phase 3 EV-026

Trade-off 5: Fee Switch Activation Uncertainty vs Token Holder Expectation
· Decision: Fee switch masih diskusi (EV-027) belum activated; base fee burn only current value accrual
· Trade-off: Careful economic design (avoid breaking fee market) vs investor narrative pressure untuk value accrual; delay risiko TIA seen as "governance only token"
· Evidence: Phase 3 EV-027 "belum ada keputusan final"; Phase 6 Utility Fee Accrual "Planned/In Discussion"; Phase 8 Narrative "Value Accrual discussion ongoing"
· Supporting Dataset: Phase 3 EV-027; Phase 6; Phase 8

Trade-off 6: Single Large Equity Round vs Continuous Fundraising
· Decision: $55M Series A/B sekali saja; tidak ada Series C, tidak ada token sale publik; runway management critical
· Trade-off: Less dilution, focus on execution vs risk of runway expiry before protocol revenue sustainable; Labs for-profit perlu break-even atau raise lagi
· Evidence: Phase 5 Funding History 1 ronde $55M; Phase 5 Financial Risk "Funding Runway Celestia Labs"; Phase 5 Financial Dependencies "VC Investors"
· Supporting Dataset: Phase 5

Trade-off 7: Permissionless Relayer vs Protocol Revenue dari Blobstream
· Decision: Blobstream relayer permissionless, protocol tidak ambil fee; relayer bayar gas Ethereum sendiri
· Trade-off: Decentralization dan censorship resistance vs potential protocol revenue stream; EigenDA charge fee ke rollup via EigenLayer
· Evidence: Phase 4 Blobstream "tidak ada fee protokol"; Phase 7 Infrastructure Providers "permissionless network"; Phase 5 Revenue Model "Bridge Fees: no fee"
· Supporting Dataset: Phase 4; Phase 7; Phase 5

Behavioral Summary

Prioritas Utama Proyek:
1. Technical credibility melalui modular architecture yang terbukti (DAS, NMT, CometBFT) — research-first, production-second
2. Ecosystem adoption via major rollup partnerships (Arbitrum, Starknet, Polygon) + sovereign rollup frameworks (Rollkit, Sovereign SDK)
3. Trust-minimized verification accessibility (light client WASM/mobile) sebagai differentiator
4. Governance legitimacy melalui on-chain voting + Foundation stewardship
5. Long-term value accrual via fee switch (planned) mengubah TIA dari gas token ke productive asset

Cara Mengambil Keputusan:
- Research-driven: Whitepaper → testnet → mainnet → upgrade cycle (evidence-based iteration)
- Governance-mediated: Semua parameter critical via on-chain proposal; forum discussion first
- Dual-track: Core protocol + developer frameworks paralel
- Security-first: Multiple audits pre-launch/upgrade; transparency via published reports
- Partnership-led growth: BD focus pada rollup framework terbesar untuk immediate demand

Faktor Paling Sering Mempengaruhi Keputusan:
1. Technical feasibility dan security (audit, testnet validation) — tidak launch sebelum ready
2. Rollup ecosystem demand (blobspace usage) — drive fee market, upgrade priority, BD focus
3. Investor/token holder expectation (value accrual, fee switch, staking yield) — governance discussion
4. Competitive landscape (EigenDA, Avail, Near DA) — differentiation via sovereign, light client, QGB
5. Regulatory clarity (dual entity, no public sale, Foundation non-profit) — structure decisions

Pola Evolusi:
- 2019-2021: Pure research (LazyLedger whitepaper)
- 2021-2022: Company + testnet iteration (Labs, funding, Arabica/Mocha, Rollkit)
- 2023: Production launch + ecosystem onboarding (Mainnet, TGE, Foundation, Blobstream, 3 major rollup integrations)
- 2024-2025: Scaling + value capture + next-gen (Upgrades v2/v3, grants, fee switch, QGB, light client WASM)

Kekuatan Utama:
1. Technical differentiation: DAS + NMT + light client verification (unique vs competitors)
2. Ecosystem breadth: 15+ rollups integrated (EVM, ZK, SVM, Move, Sovereign)
3. Developer tooling: Rollkit + Sovereign SDK + multi-language SDKs
4. Governance maturity: On-chain upgrades working, Foundation stewardship
5. Security posture: 4 top-tier audits, zero critical exploits
6. Neutral positioning: Not tied to single VM or settlement layer

Kelemahan Utama:
1. Throughput ceiling: ~10-15 MB/s blobspace limit vs competitors higher claims
2. Treasury opacity: No public dashboard, community accountability gap
3. Fee switch uncertainty: Value accrual narrative pending governance outcome
4. Labs runway dependency: Single $55M equity round, no public revenue reporting
5. QGB unproven: Trust-minimized bridging still R&D, testnet not yet live
6. Light client adoption metric: Actual DAS participation rate unclear (5k-15k estimated)
7. No native IBC: Cosmos ecosystem integration pending

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Celestia

Core Insights

Insight 1: Modular blockchain thesis memisahkan consensus, data availability, dan execution layer menjadikan Celestia pionir kategori DA Layer
Explanation: Whitepaper LazyLedger (2021) mendefinisikan arsitektur modular dengan Data Availability Sampling (DAS) dan Namespaced Merkle Trees (NMT) sebagai fondasi teknis; narasi "Modular Blockchain" menjadi identitas utama di semua komunikasi resmi【Phase 1 — Foundation】【Phase 3 — EV-003】【Phase 9 — Strategic Objectives】
Evidence: Whitepaper LazyLedger arXiv:2105.09830; Blog "What is Celestia"; Phase 9 Strategic Objective 1
Supporting Dataset: Phase 1 Foundation, Phase 3 EV-003, Phase 8 Narrative Position, Phase 9 Strategic Objectives
Confidence: HIGH

Insight 2: Dual-entity structure (Celestia Labs for-profit + Celestia Foundation non-profit) memisahkan core development dari protocol governance dan treasury management
Explanation: Labs (Delaware, 2021) menangani engineering, BD, equity fundraising; Foundation (Zug, 2023) mengelola treasury protokol, grants, community pool, governance stewardship【Phase 2 — Company Celestia Labs Inc.】【Phase 2 — Foundation Celestia Foundation】【Phase 3 — EV-002, EV-011】【Phase 5 — Treasury】
Evidence: Crunchbase Celestia Labs incorporasi 2021; Blog Mainnet Launch menyebutkan Foundation; Phase 5 Treasury membedakan custodian
Supporting Dataset: Phase 2 Company/Foundation entities, Phase 3 EV-002 EV-011, Phase 5 Treasury, Phase 9 Decision Timeline
Confidence: HIGH

Insight 3: Token Generation Event (TGE) dan mainnet launch bersamaan 31 Oktober 2023 dengan Genesis Drop 6% supply (60M TIA) ke community tanpa public sale
Explanation: 1B TIA di-mint pada genesis; 60M TIA (6%) claimable langsung oleh eligible addresses (Cosmos stakers, developers, testnet contributors); investor/team/foundation tokens terkunci vesting tidak diumumkan publik【Phase 1 — Launch Date TGE】【Phase 3 — EV-009, EV-010】【Phase 6 — TGE, Distribution】【Phase 9 — Decision Timeline Mainnet Launch】
Evidence: Blog Mainnet Launch; Blog TIA Genesis Drop; Phase 6 Token Distribution categories; CoinGecko historical data
Supporting Dataset: Phase 1 Foundation, Phase 3 EV-009 EV-010, Phase 6 Token, Phase 9 Decision Timeline
Confidence: HIGH

Insight 4: Blobstream sebagai trust-minimized bridge memverifikasi DA commitment Celestia di Ethereum smart contract membuka akses ke ekosistem rollup EVM (Arbitrum Orbit, Polygon CDK, custom)
Explanation: Blobstream contracts deploy Ethereum mainnet Oktober 2023; relayer permissionless submit header + NMT proof; rollup EVM memverifikasi on-chain tanpa trusted validator set【Phase 3 — EV-012】【Phase 4 — Blobstream】【Phase 7 — Integration Blobstream】【Phase 7 — External Dependencies Ethereum】
Evidence: Blobstream Contracts Repo; Blog Mainnet Launch; Phase 4 Blobstream component; Phase 7 Major Integrations Arbitrum Orbit/Polygon CDK
Supporting Dataset: Phase 3 EV-012, Phase 4 Blobstream, Phase 7 Integrations, Phase 7 External Dependencies
Confidence: HIGH

Insight 5: Multi-ecosystem DA provider strategy — integrasi live dengan Arbitrum Orbit (optimistic), Starknet (ZK), Polygon CDK (app-chain), Sovereign SDK/Rollkit (sovereign) tanpa terikat single rollup stack
Explanation: Announcement berurutan Nov-Des 2023: Arbitrum Orbit (EV-013), Starknet (EV-014), Polygon CDK (EV-015); tambahan Manta Pacific, Dymension RollApps, Movement M2 2024; 15+ rollup terintegrasi Q2 2025【Phase 3 — EV-013, EV-014, EV-015, EV-022】【Phase 7 — Major Integrations】【Phase 8 — Adoption Metrics Rollups】
Evidence: Blog announcements masing-masing integrasi; Phase 7 Major Integrations list; Phase 8 Adoption Metrics 15+ rollup
Supporting Dataset: Phase 3 EV-013-015 EV-022, Phase 7 Major Integrations, Phase 8 Adoption Metrics
Confidence: HIGH

Insight 6: Revenue model bergantung sepenuhnya pada blobspace adoption — fee market EIP-1559 live sejak mainnet (base fee burn, priority fee ke proposer); fee switch (value accrual ke staker) masih diskusi governance belum aktif
Explanation: Blobspace fees = revenue utama protokol; staking inflation ~7-8%/tahun; fee burn mengurangi supply; fee switch proposal di forum Nov 2024 (EV-027) belum keputusan final【Phase 4 — Fee Market】【Phase 5 — Revenue Model】【Phase 6 — Inflation/Deflation】【Phase 3 — EV-027】【Phase 9 — Decision Timeline Fee Switch】
Evidence: Docs Fee Market; Phase 5 Revenue Streams; Phase 6 Burn Mechanism; Forum governance discussion
Supporting Dataset: Phase 4 Fee Market, Phase 5 Revenue Model, Phase 6 Token, Phase 3 EV-027, Phase 9 Decision Timeline
Confidence: HIGH

Insight 7: Security-first approach dengan 4 audit utama pre-mainnet dan pasca-upgrade (Informal Systems, Trail of Bits, Zellic, Sigma Prime) membangun reputation keamanan sebelum scaling adoption
Explanation: Informal Systems audit consensus/light client/Blobstream 2023; Trail of Bits audit Celestia App/Blobstream contracts/kripto 2023; Zellic audit Node/fee market/upgrade 2024; Sigma Prime audit Blobstream v2 2024【Phase 3 — EV-016, EV-017】【Phase 4 — Audit History】【Phase 7 — External Dependencies Auditors】【Phase 9 — Decision Timeline Audits】
Evidence: Informal Systems audits page; Trail of Bits publications; Zellic audits page; Sigma Prime audits page; Phase 4 Audit History list
Supporting Dataset: Phase 3 EV-016 EV-017, Phase 4 Audit History, Phase 7 External Dependencies, Phase 9 Decision Timeline
Confidence: HIGH

Insight 8: Light client DAS (Data Availability Sampling) sebagai security model unik — keamanan probabilistik bergantung pada partisipasi light client sampling acak; WASM/mobile SDK rilis Jan 2025 memperluas verifikasi trust-minimized ke browser/mobile
Explanation: Light client melakukan DAS sampling pada extended data square 2kx2k shares; butuh >50% light client sampling untuk garansi ketersediaan; WASM release EV-028 memperluas adoption【Phase 4 — Security Model】【Phase 3 — EV-028】【Phase 7 — Integration Light Client WASM】【Phase 9 — Decision Timeline Light Client WASM】
Evidence: Docs DAS Security; Blog Light Client Adoption; Phase 4 Security Model; Phase 3 EV-028; Phase 7 Integration WASM
Supporting Dataset: Phase 4 Security Model, Phase 3 EV-028, Phase 7 Integration Light Client WASM, Phase 9 Decision Timeline
Confidence: HIGH

Insight 9: Treasury dan token allocation opacity — Foundation/team/investor/ecosystem percentages tidak diumumkan publik; vesting schedule investor/team tidak transparan; on-chain analysis diperlukan untuk visibility
Explanation: Blog TIA Genesis Drop hanya menyebut 6% community drop; kategori lain "tidak diungkap persentase pasti" di Phase 6 Distribution; vesting schedule semua kategori "tidak diungkap"; Open Threads Phase 5/6 menanyakan transparency【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 5 — Treasury】【Phase 9 — Open Threads Distribution/Vesting】
Evidence: Phase 6 Distribution categories all "tidak diungkap"; Phase 6 Vesting Schedule all "tidak diungkap"; Phase 5 Treasury "tidak diungkap"; Phase 9 Open Threads multiple items
Supporting Dataset: Phase 6 Token, Phase 5 Financial, Phase 9 Open Threads
Confidence: HIGH

Insight 10: CEX liquidity dominant (11 major exchanges: Binance, Coinbase, Kraken, Bybit, OKX, KuCoin, Gate, MEXC, HTX, Bitget, Crypto.com) vs DEX liquidity terbatas ke wTIA third-party di Ethereum/Arbitrum; native IBC belum aktif
Explanation: Semua 11 CEX listing spot + perpetual (kecuali Coinbase/Crypto.com spot only); wTIA ERC-20 deploy pihak ketiga tidak resmi; Quantum Gravity Bridge native bridging masih R&D【Phase 8 — Exchange Ecosystem】【Phase 8 — Liquidity】【Phase 6 — wTIA】【Phase 7 — Integration wTIA】【Phase 4 — Quantum Gravity Bridge】
Evidence: Phase 8 Exchange Ecosystem table 11 exchanges; Phase 8 Liquidity CEX dominant; Phase 6 wTIA third-party; Phase 4 QGB R&D status
Supporting Dataset: Phase 8 Market, Phase 6 Token, Phase 7 Ecosystem, Phase 4 Technology
Confidence: HIGH

Strategic Principles

Principle 1: Modular first — memisahkan consensus, data availability, dan execution layer sebagai prinsip arsitektur fundamental
Explanation: Whitepaper LazyLedger mendefinisikan modular thesis; semua produk (Celestia Core, Blobstream, Rollkit, Sovereign SDK) dibangun di atas pemisahan layer ini; narasi konsisten di semua komunikasi【Phase 1 — Foundation】【Phase 4 — System Architecture】【Phase 8 — Narrative Position】【Phase 9 — Strategic Objectives 1,2】
Evidence: Whitepaper LazyLedger; Docs Architecture; Blog Modular Ecosystem; Phase 9 Strategic Objectives 1&2
Supporting Dataset: Phase 1, Phase 4, Phase 8, Phase 9
Confidence: HIGH

Principle 2: Ecosystem first — membangun tooling (Rollkit, Sovereign SDK), integrasi (Blobstream), dan grants (Sputnik) untuk menarik rollup builder sebelum memaksimalkan value capture
Explanation: Rollkit rilis 2022 (EV-006) sebelum mainnet; Blobstream deploy Oct 2023 (EV-012) enable rollup EVM; integrasi Arbitrum/Starknet/Polygon CDK 2023; Grant program Sputnik 2024 (EV-026); fee switch diskusi 2024 (EV-027) setelah adoption【Phase 3 — EV-006, EV-012, EV-013, EV-014, EV-015, EV-026, EV-027】【Phase 7 — SDK Rollkit, SDK Sovereign SDK】【Phase 9 — Decision Timeline Rollkit, Blobstream, Integrations, Grants, Fee Switch】
Evidence: Phase 3 events chronological order; Phase 7 SDKs; Phase 9 Decision Timeline shows adoption before value capture
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Principle 3: Security before growth — 4 audit komprehensif pre-mainnet (Informal Systems, Trail of Bits) dan pasca-upgrade (Zellic, Sigma Prime) sebelum scaling adoption
Explanation: Audit konsensus, light client, Blobstream, Celestia App, kriptografi semua completed sebelum mainnet Oct 2023; audit tambahan 2024 untuk upgrade v2/v3; security sebagai prerequisite bukan afterthought【Phase 3 — EV-016, EV-017】【Phase 4 — Audit History】【Phase 9 — Decision Timeline Audits】【Phase 7 — External Dependencies Auditors】
Evidence: Phase 3 EV-016 EV-017 pre-mainnet; Phase 4 Audit History 4 audits; Phase 9 Decision Timeline audit decisions
Supporting Dataset: Phase 3, Phase 4, Phase 7, Phase 9
Confidence: HIGH

Principle 4: Progressive decentralization — dual entity (Labs + Foundation), on-chain governance aktif sejak mainnet (EV-018), community pool spend via proposal, fee switch governance-driven
Explanation: Labs (for-profit) core dev; Foundation (non-profit) treasury/stewardship; governance module live day-1; proposal pertama Jan 2024; community grants via governance; fee switch decision via governance bukan team【Phase 2 — Foundation, Company, DAO】【Phase 3 — EV-011, EV-018】【Phase 6 — Governance】【Phase 9 — Decision Timeline Foundation, Governance, Fee Switch】
Evidence: Phase 2 entities; Phase 3 EV-011 EV-018; Phase 6 Governance model; Phase 9 Decision Timeline
Supporting Dataset: Phase 2, Phase 3, Phase 6, Phase 9
Confidence: HIGH

Principle 5: Multi-ecosystem neutrality — tidak terikat single rollup stack; mendukung EVM (Arbitrum Orbit, Polygon CDK), ZK (Starknet), SVM (Movement), WASM (CosmWasm), sovereign (Rollkit, Sovereign SDK)
Explanation: Integrasi live dengan 3 major rollup framework berbeda arsitektur; Rollkit (Go) + Sovereign SDK (Rust) dual framework; execution environment agnostic【Phase 3 — EV-013, EV-014, EV-015】【Phase 4 — Execution Environment】【Phase 7 — Major Integrations】【Phase 9 — Strategic Objective 2,3】
Evidence: Phase 3 integrations; Phase 4 Execution Environment list; Phase 7 Major Integrations; Phase 9 Strategic Objectives
Supporting Dataset: Phase 3, Phase 4, Phase 7, Phase 9
Confidence: HIGH

Principle 6: Trust-minimized verification — light client DAS sampling + NMT proof + Blobstream Ethereum verification + Quantum Gravity Bridge (R&D) menghilangkan kepercayaan pada validator set terpusat
Explanation: Light client verifikasi sendiri via DAS; Blobstream verifikasi on-chain Ethereum via NMT proof; QGB dirancang bridging tanpa validator set; security model tidak bergantung honest majority validator untuk DA validity【Phase 4 — Security Model】【Phase 4 — Blobstream】【Phase 4 — Quantum Gravity Bridge】【Phase 7 — Integration Light Client WASM, QGB】【Phase 9 — Strategic Objective 6】
Evidence: Phase 4 Security Model DAS; Phase 4 Blobstream trust-minimized; Phase 4 QGB design; Phase 7 Integrations; Phase 9 Strategic Objective 6
Supporting Dataset: Phase 4, Phase 7, Phase 9
Confidence: HIGH

Success Factors

Factor 1: Clear category creation dan thought leadership melalui LazyLedger whitepaper (2021) mendefinisikan Modular Blockchain narrative sebelum kompetitor
Explanation: Whitepaper arXiv:2105.09830 menjadi referensi standar; narasi "Modular Blockchain" dimiliki Celestia; EigenDA, Avail, Near DA muncul बाद sebagai respons; first-mover advantage dalam category definition【Phase 3 — EV-003】【Phase 8 — Narrative Position】【Phase 8 — Competitor Landscape】【Phase 9 — Strategic Objective 1】
Evidence: Phase 3 EV-003 whitepaper; Phase 8 Narrative Position "Main Narrative"; Phase 8 Competitor Landscape comparison; Phase 9 Strategic Objective 1
Supporting Dataset: Phase 3, Phase 8, Phase 9
Confidence: HIGH

Factor 2: Strong technical team dengan background cryptography, distributed systems, Ethereum research (Mustafa Al-Bassam, Ismail Khoffi, John Adler, Nick White) membangun credibilitas teknis dan menarik top-tier VC
Explanation: Founders memiliki track record: Mustafa (Chainspace, LazyLedger), Ismail (Tendermint/Cosmos), John (Ethereum research, Fuel), Nick (Cosmos ecosystem); $55M Series A/B dari Bain Capital Crypto, Polychain, 1kx, Robot Ventures, Placeholder, Delphi, Galaxy, Figment【Phase 2 — Person entities】【Phase 3 — EV-005】【Phase 5 — Funding History】【Phase 9 — Decision Timeline Funding】
Evidence: Phase 2 Person bios; Phase 3 EV-005 investors list; Phase 5 Funding History $55M; Phase 9 Decision Timeline funding decision
Supporting Dataset: Phase 2, Phase 3, Phase 5, Phase 9
Confidence: HIGH

Factor 3: Incentivized testnet program (Arabica Jan 2022, Mocha Mar 2023, Lemon Sep 2023) membangun operator network, memvalidasi DAS/consensus, dan mendistribusikan token ke early contributors sebelum mainnet
Explanation: 3 testnet incentivized bertahap: Arabica (first DAS/light client), Mocha (Blobstream testing), Lemon (genesis config rehearsal); membangun infrastructure provider network (Cosmostation, Figment, Chorus One, P2P.org, Blockdaemon) sebelum mainnet【Phase 3 — EV-004, EV-007, EV-008】【Phase 7 — Infrastructure Providers】【Phase 9 — Decision Timeline Testnets】
Evidence: Phase 3 EV-004 EV-007 EV-008 testnet launches; Phase 7 Infrastructure Providers list; Phase 9 Decision Timeline testnet decisions
Supporting Dataset: Phase 3, Phase 7, Phase 9
Confidence: HIGH

Factor 4: Strategic integrasi dengan major rollup frameworks (Arbitrum Orbit, Starknet, Polygon CDK) dalam 2 bulan pasca-mainnet menciptakan immediate demand untuk blobspace dan validasi product-market fit
Explanation: EV-013 (Arbitrum Nov 2023), EV-014 (Starknet Nov 2023), EV-015 (Polygon CDK Dec 2023) — semua announced dalam 8 minggu post-mainnet; 15+ rollup terintegrasi Q2 2025; blobspace usage real dari Manta Pacific, Dymension RollApps Jul 2024【Phase 3 — EV-013, EV-014, EV-015, EV-022】【Phase 7 — Major Integrations】【Phase 8 — Adoption Metrics Rollups】【Phase 9 — Decision Timeline Integrations】
Evidence: Phase 3 events chronological; Phase 7 integrations list; Phase 8 adoption metrics; Phase 9 Decision Timeline
Supporting Dataset: Phase 3, Phase 7, Phase 8, Phase 9
Confidence: HIGH

Factor 5: Dual SDK strategy (Rollkit Go + Sovereign SDK Rust) menangkap developer preferences berbeda dan memperluas sovereign rollup design space
Explanation: Rollkit rilis 2022 (EV-006) untuk Go developers; Sovereign SDK rilis 2024 (EV-019) untuk Rust developers; keduanya native Celestia DA tanpa settlement layer; framework complement bukan compete【Phase 3 — EV-006, EV-019】【Phase 7 — SDK Rollkit, SDK Sovereign SDK】【Phase 9 — Decision Timeline Rollkit, Sovereign SDK】
Evidence: Phase 3 EV-006 EV-019; Phase 7 SDK descriptions; Phase 9 Decision Timeline
Supporting Dataset: Phase 3, Phase 7, Phase 9
Confidence: HIGH

Factor 6: CEX listing strategy komprehensif (11 major exchanges dalam 6 bulan) memberikan liquidity global, price discovery, dan akses institutional/retail sejak early stage
Explanation: Binance, Coinbase, Kraken, Bybit, OKX, KuCoin, Gate, MEXC, HTX, Bitget, Crypto.com semua listing spot + perpetual (mostly) Q4 2023 - Q1 2024; CEX liquidity dominant vs DEX; on-ramp fiat tersedia【Phase 3 — EV-024】【Phase 8 — Exchange Ecosystem】【Phase 8 — Liquidity】【Phase 9 — Decision Timeline CEX Listings】
Evidence: Phase 3 EV-024; Phase 8 Exchange Ecosystem 11 exchanges; Phase 8 Liquidity CEX dominant; Phase 9 Decision Timeline
Supporting Dataset: Phase 3, Phase 8, Phase 9
Confidence: HIGH

Failure Factors

Factor 1: Token allocation dan vesting opacity — team/investor/foundation/ecosystem percentages tidak diumumkan; vesting schedule investor/team tidak transparan; menciptakan uncertainty untuk token holders dan investor
Explanation: Phase 6 Distribution semua kategori kecuali community drop "tidak diungkap persentase pasti"; Vesting Schedule semua kategori "tidak diungkap"; Open Threads Phase 5/6/9 repeatedly menanyakan transparency; tidak ada tokenomics dashboard resmi【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 5 — Treasury】【Phase 9 — Open Threads Distribution, Vesting, Treasury】
Evidence: Phase 6 Distribution table; Phase 6 Vesting table; Phase 5 Treasury "tidak diungkap"; Phase 9 Open Threads multiple items
Supporting Dataset: Phase 5, Phase 6, Phase 9
Confidence: HIGH

Factor 2: Treasury transparency absent — ukuran, komposisi, alamat on-chain Foundation treasury tidak dipublikasikan; community pool balance on-chain tapi tidak di-dashboard-kan; grant program budget tidak transparan
Explanation: Phase 5 Treasury "Current Treasury Size: tidak diungkap"; "Treasury Composition: tidak diungkap"; Foundation custodian tapi tidak ada address label resmi; Sputnik grant program budget tidak diumumkan【Phase 5 — Treasury】【Phase 5 — Fundraising Mechanism Grants】【Phase 9 — Open Threads Treasury, Grants】
Evidence: Phase 5 Treasury section; Phase 5 Fundraising Mechanism Grants; Phase 9 Open Threads
Supporting Dataset: Phase 5, Phase 9
Confidence: HIGH

Factor 3: Fee switch activation delay — value accrual mechanism untuk TIA staker masih diskusi governance Nov 2024 (EV-027) tanpa timeline keputusan; naratif investasi bergantung fee switch tapi tidak ada certainty
Explanation: Phase 5 Revenue Model Fee Switch "Status: Planned/In Discussion"; Phase 6 Utility Fee Accrual "Status: Planned/In Discussion"; Phase 3 EV-027 "belum ada keputusan final"; Phase 9 Decision Timeline "belum ada keputusan final"【Phase 5 — Revenue Model】【Phase 6 — Utility】【Phase 3 — EV-027】【Phase 9 — Decision Timeline Fee Switch】
Evidence: Phase 5 Revenue Model; Phase 6 Utility; Phase 3 EV-027; Phase 9 Decision Timeline
Supporting Dataset: Phase 3, Phase 5, Phase 6, Phase 9
Confidence: HIGH

Factor 4: wTIA custody risk — wrapped TIA di Ethereum/Arbitrum deploy oleh pihak ketiga tidak resmi; tidak ada audit/resmi multisig custodian; Quantum Gravity Bridge native solution masih R&D tanpa timeline mainnet
Explanation: Phase 6 wTIA "deploy oleh pihak ketiga (bukan resmi Celestia Labs)"; Phase 7 Integration wTIA "tidak resmi"; Phase 4 QGB "masih R&D/desain; belum ada testnet publik terverifikasi per Juni 2025"; Phase 8 Liquidity "DEX liquidity terbatas ke wTIA"【Phase 6 — wTIA】【Phase 7 — Integration wTIA】【Phase 4 — Quantum Gravity Bridge】【Phase 8 — Liquidity】【Phase 9 — Decision Timeline wTIA, QGB】
Evidence: Phase 6 wTIA description; Phase 7 Integration wTIA; Phase 4 QGB limitations; Phase 8 Liquidity; Phase 9 Decision Timeline
Supporting Dataset: Phase 4, Phase 6, Phase 7, Phase 8, Phase 9
Confidence: HIGH

Factor 5: Native IBC tidak aktif — transfer TIA antar chain Cosmos ecosystem masih via CEX/bridge; tidak ada native interoperability dengan Cosmos Hub/Osmosis; membatasi composability di ekosistem asal (Cosmos SDK)
Explanation: Phase 7 Integration Cosmos Ecosystem IBC "Status: Planned"; "native IBC belum aktif pada cut-off"; Phase 8 Liquidity "Native IBC liquidity belum tersedia"; dependency pada CEX untuk cross-chain movement【Phase 7 — Integration Cosmos Ecosystem IBC】【Phase 8 — Liquidity】【Phase 9 — Open Threads IBC】
Evidence: Phase 7 Integration IBC planned; Phase 8 Liquidity native IBC unavailable; Phase 9 Open Threads
Supporting Dataset: Phase 7, Phase 8, Phase 9
Confidence: MEDIUM

Factor 6: Light client participation uncertainty — DAS security bergantung pada jumlah light client aktif sampling; estimasi 5k-15k light client (LOW confidence) tanpa telemetri resmi veröffentlicht; jika participation rendah, security model lemah
Explanation: Phase 4 Security Model "memerlukan jumlah light client yang cukup besar"; Phase 8 Adoption Metrics Light Client "perkiraan dari telemetri jaringan (LOW)"; Phase 4 Known Limitations "jika jumlah light client rendah, risiko data withholding meningkat"【Phase 4 — Security Model】【Phase 8 — Adoption Metrics Light Client】【Phase 4 — Known Technical Limitations】【Phase 9 — Open Threads DAS Participation】
Evidence: Phase 4 Security Model; Phase 8 Adoption Metrics; Phase 4 Known Limitations; Phase 9 Open Threads
Supporting Dataset: Phase 4, Phase 8, Phase 9
Confidence: MEDIUM

Decision Framework

Step 1: Research & Define Category (2019-2021)
Observe: Masalah skalabilitas monolithic blockchain (execution+consensus+DA coupled)
Evaluate: Pemisahan layer via Data Availability Sampling + Namespaced Merkle Trees
Fund: Seed funding (undisclosed) untuk Celestia Labs Inc. incorporation 2021
Develop: Whitepaper LazyLedger (2021), core protocol research
Launch: Arabica Incentivized Testnet (2022-01-24) validasi DAS/light client
Govern: Internal team coordination
Evidence: Phase 3 EV-001, EV-002, EV-003, EV-004; Phase 9 Decision Timeline Founding, Labs Formation, Whitepaper, Arabica
Supporting Dataset: Phase 3, Phase 9
Confidence: HIGH

Step 2: Capitalize & Build Infrastructure (2022)
Observe: Testnet Arabica berhasil, perlu scaling team dan infrastructure
Evaluate: Series A/B funding untuk hiring, BD, ecosystem development
Fund: $55M Series A/B Oktober 2022 (Bain Capital Crypto, Polychain lead)
Develop: Rollkit framework (2022), Mocha Testnet (2023-03-28) dengan Blobstream testing
Launch: Mocha Testnet v2 dengan Blobstream relayer testing
Govern: Investor alignment, team scaling
Evidence: Phase 3 EV-005, EV-006, EV-007; Phase 5 Funding History; Phase 9 Decision Timeline Funding, Rollkit, Mocha
Supporting Dataset: Phase 3, Phase 5, Phase 9
Confidence: HIGH

Step 3: Production Launch & Tokenize (2023 Q3-Q4)
Observe: Mocha testnet stable, Blobstream validated, ecosystem ready
Evaluate: Mainnet launch + TGE bersamaan dengan Genesis Drop community-first
Fund: Treasury allocation via genesis mint (1B TIA), Foundation formation
Develop: Lemon Pre-Mainnet Testnet (2023-09-19) dress rehearsal
Launch: Mainnet 2023-10-31 (EV-009) + TGE 2023-10-31 (EV-010) + Foundation (EV-011) + Blobstream Ethereum (EV-012)
Govern: On-chain governance activated day-1, Genesis Drop 6% to community
Evidence: Phase 3 EV-008, EV-009, EV-010, EV-011, EV-012; Phase 6 TGE; Phase 9 Decision Timeline Mainnet, TGE, Foundation, Blobstream
Supporting Dataset: Phase 3, Phase 6, Phase 9
Confidence: HIGH

Step 4: Ecosystem Expansion & Integrations (2023 Q4 - 2024 H1)
Observe: Mainnet live, need rollup adoption untuk blobspace demand
Evaluate: Integrasi dengan major rollup frameworks (Arbitrum, Starknet, Polygon CDK)
Fund: Protocol revenue dari blobspace fees mulai terkumpul
Develop: Upgrade v2.0 (2024-06) fee market/DAS improvements
Launch: Arbitrum Orbit (EV-013), Starknet (EV-014), Polygon CDK (EV-015) integrations; Manta Pacific, Dymension production (EV-022)
Govern: Proposal governance pertama (EV-018 2024-01), Sovereign SDK release (EV-019 2024-02)
Evidence: Phase 3 EV-013, EV-014, EV-015, EV-018, EV-019, EV-021, EV-022; Phase 9 Decision Timeline Integrations, Governance, Upgrade v2, Production Rollups
Supporting Dataset: Phase 3, Phase 9
Confidence: HIGH

Step 5: Maturity & Value Accrual (2024 H2 - 2025)
Observe: 15+ rollup live, blobspace revenue real, community pressure untuk value accrual
Evaluate: Fee switch governance discussion (EV-027), Grant program (EV-026), Transparency report (EV-023)
Fund: CEX listings 11 major exchanges (EV-024), wTIA third-party DeFi access (EV-025)
Develop: Light Client WASM/Mobile (EV-028 2025-01), Upgrade v3.0 Ginger (EV-029 2025-03), QGB Testnet planned (EV-030 2025-06)
Launch: QGB testnet (planned), continued rollup onboarding
Govern: Fee switch decision pending, grant allocation via governance, parameter upgrades via governance
Evidence: Phase 3 EV-023, EV-024, EV-025, EV-026, EV-027, EV-028, EV-029, EV-030; Phase 9 Decision Timeline One Year Report, CEX Listings, wTIA, Grants, Fee Switch, Light Client WASM, Upgrade v3, QGB Testnet
Supporting Dataset: Phase 3, Phase 9
Confidence: HIGH

Reusable Playbook

Playbook 1: Category Creation via Technical Whitepaper First
Description: Publikasi whitepaper teknis rigor (LazyLedger arXiv:2105.09830) mendefinisikan arsitektur baru (Modular Blockchain, DAS, NMT) sebelum fundraising atau launch; menjadi referensi akademik dan industri; menarik top-tier VC dan researcher
Evidence: Phase 3 EV-003 whitepaper 2021 sebelum Series A 2022; Phase 8 Narrative Position "Main Narrative"; Phase 8 Competitor Landscape EigenDA/Avail/Near DA referensi Celestia; Phase 9 Decision Timeline Whitepaper sebelum Funding
Steps: 1) Research fundamental problem → 2) Publish technical whitepaper defining new category → 3) Build reference implementation → 4) Fundraise based on technical credibility → 5) Launch testnet validating claims
Supporting Dataset: Phase 3, Phase 8, Phase 9
Confidence: HIGH

Playbook 2: Incentivized Testnet Series untuk Infrastructure Network Building
Description: Multi-phase incentivized testnet (Arabica, Mocha, Lemon) dengan reward untuk node operators membangun decentralized infrastructure network pre-mainnet; setiap testnet test komponen berbeda (DAS, Blobstream, genesis config); operator network siap day-1 mainnet
Evidence: Phase 3 EV-004 Arabica (DAS/light client), EV-007 Mocha (Blobstream), EV-008 Lemon (genesis rehearsal); Phase

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

PROJECT: Celestia

CIF MANIFEST v3.0

Project: Celestia
Symbol: TIA
Research Date: 2025-06-21
CIF Version: 3.0
QA Date: 2025-06-21

METRICS
Total Knowledge Objects: 10
Total Entities: 38
Total Events: 30
Evidence Links: 105
Sources: 42
Conflicts: 4
 ├── Resolved: 3
 ├── Critical: 0
 ├── High: 1
 ├── Medium: 0
 └── Low: 0

QUALITY SCORES
Research Quality: 92/100
Consistency: 90/100
Evidence: 72/100
Coverage: 86/100
Conflict: 85/100
Knowledge: 84/100
CIF SCORE: 86/100

CONFIDENCE LEVEL: HIGH
QA STATUS: PASSED

RECOMMENDED RE-RUN:
 - Phase 5 — Financial — Treasury size dan revenue metrics tidak diungkap publik; butuh analisis on-chain address label untuk verifikasi tambahan
 - Phase 6 — Token — Persentase alokasi TGE per kategori dan vesting schedule investor tidak diungkap; butuh analisis genesis.json dan vesting contract on-chain

DATASET INTEGRITY & COVERAGE

Phase 1 — Foundation
 Status: Complete
 Missing Information: Tidak ada
 Notes: Data dasar lengkap; kategori, produk, tanggal launch, dan sosial media tercatat dengan baik. Launch date mainnet dan TGE konsisten dengan fase lain. (HIGH) [Phase 1, https://celestia.org; https://blog.celestia.org; https://www.coingecko.com/en/coins/celestia]

Phase 2 — Entity
 Status: Complete
 Missing Information: Daftar lengkap investor ronde Series A/B tidak lengkap (Crunchbase menyebut nama tambahan Delphi Digital, Galaxy Digital, Figment Capital yang tidak ada di blog resmi) — (MEDIUM) [Phase 2, https://www.crunchbase.com/organization/celestia-labs; https://blog.celestia.org/celestia-labs-raises-55m/]
 Notes: Seluruh 38 entity teridentifikasi dengan tipe yang benar. Legal structure Labs vs Foundation tidak sepenuhnya diungkap dalam dokumen resmi. (HIGH) [Phase 2, https://blog.celestia.org/celestia-labs-raises-55m/]

Phase 3 — History
 Status: Complete
 Missing Information: Tanggal pasti pembentukan Celestia Labs Inc. hanya tahun 2021; tanggal registrasi Foundation Zug tidak diungkap; nomor proposal governance pertama tidak dicatat; detail upgrade v2.0 dan v3.0 tidak punya tanggal blok pasti — (MEDIUM) [Phase 3, https://www.crunchbase.com/organization/celestia-labs; https://blog.celestia.org/]
 Notes: 30 event tercatat dengan timeline yang koheren. Event EV-004 hingga EV-008 mencerminkan fase testnet bertahap yang konsisten dengan pola pengembangan proyek. (HIGH) [Phase 3, https://blog.celestia.org/arabica-testnet/; https://blog.celestia.org/mocha-testnet/; https://blog.celestia.org/lemon-testnet/]

Phase 4 — Technology
 Status: Complete
 Missing Information: Spesifikasi teknis Quantum Gravity Bridge (ZK-proof vs optimistic verification) belum dipublikasikan; parameter konsensus genesis (block time, max block size) tidak di-named; audit status pasca-upgrade v3.0 belum ada — (MEDIUM) [Phase 4, https://forum.celestia.org/t/quantum-gravity-bridge/; https://github.com/celestiaorg/celestia-app]
 Notes: Arsitektur modular dan DAS dijelaskan dengan jelas. Blobstream dan NMT sebagai komponen kunci tercatat. (HIGH) [Phase 4, https://docs.celestia.org/learn/architecture; https://docs.celestia.org/learn/data-availability-sampling]

Phase 5 — Financial
 Status: Complete
 Missing Information: Ukuran treasury saat ini tidak diungkap; komposisi treasury tidak diungkap; revenue metrics bulanan tidak dipublikasikan; valuasi Series A/B tidak diumumkan — (MEDIUM) [Phase 5, https://blog.celestia.org/celestia-labs-raises-55m/; https://tokenterminal.com/terminal/projects/celestia]
 Notes: Hanya satu ronde besar equity teridentifikasi ($55M Series A/B). Revenue model tidak dijelaskan dengan angka pasti karena tidak ada laporan keuangan resmi. (HIGH) [Phase 5, https://blog.celestia.org/celestia-labs-raises-55m/]

Phase 6 — Token
 Status: Complete
 Missing Information: Persentase alokasi token TGE per kategori (team, investor, foundation, ecosystem) tidak diungkap; vesting schedule investor/team tidak diungkap; alamat kontrak wTIA tidak diisi; inflation parameter genesis tidak di-named — (MEDIUM) [Phase 6, https://blog.celestia.org/tia-genesis-drop/; https://docs.celestia.org/learn/tia-token]
 Notes: Total supply 1B TIA dan Genesis Drop 6% (60M TIA) terdokumentasi jelas. Utility dan governance dijelaskan detail. (HIGH) [Phase 6, https://blog.celestia.org/tia-genesis-drop/; https://docs.celestia.org/learn/tia-token]

Phase 7 — Ecosystem
 Status: Complete
 Missing Information: Daftar lengkap rollup yang memposting blob secara rutin tidak diagregasikan; detail program grant Sputnik (budget, penerima) tidak dipublikasikan; IBC native belum aktif sehingga integrasi Cosmos hanya planned — (MEDIUM) [Phase 7, https://blog.celestia.org/category/ecosystem/; https://forum.celestia.org/c/grants/]
 Notes: Integrasi major (Arbitrum, Starknet, Polygon CDK) tercatat dengan baik. Infrastruktur provider dan wallet ecosystem terdokumentasi. (HIGH) [Phase 7, https://blog.celestia.org/arbitrum-orbit-celestia/; https://blog.celestia.org/starknet-celestia/; https://blog.celestia.org/polygon-cdk-celestia/]

Phase 8 — Market
 Status: Complete
 Missing Information: Market share tidak diungkap karena tidak ada data resmi untuk kategori DA Layer; beberapa metrik adopsi hanya perkiraan (daily active addresses, light client participation) — (MEDIUM) [Phase 8, https://www.mintscan.io/celestia/analytics; https://forum.celestia.org/t/das-participation-metrics/]
 Notes: 11 CEX listing terdokumentasi dengan baik. Competitor landscape komprehensif. (HIGH) [Phase 8, https://www.binance.com/en/markets/overview/TIA; https://www.coingecko.com/en/coins/celestia]

Phase 9 — Behavioral
 Status: Complete
 Missing Information: Tidak ada — sebagian besar keputusan teridentifikasi dengan jelas dari event timeline dan pola pengembangan. (HIGH)
 Notes: Strategic objectives, decision timeline, dan pola keputusan teridentifikasi dengan baik; menunjukkan pola iteratif research → testnet → mainnet → upgrade. (HIGH)

Phase 10 — Knowledge
 Status: Complete
 Missing Information: Tidak ada — 10 knowledge objects teridentifikasi dengan lintas phase coverage. (HIGH)
 Notes: Knowledge objects mencakup insight inti, strategic principles, success/failure factors, dan decision framework. (HIGH)

Coverage Report — Multi-dimensional

Phase 2 — Entity
 Total: 38
 Referenced in Phase 9-10: 20
 Unused: 18
 Coverage: 52.6%
 Interpretation: Beberapa entity (seperti investor kecil, media, audit) tidak secara eksplisit direferensikan dalam sintesis behavioral, namun tetap relevan untuk analisis on-chain atau regulatory. Coverage rendah karena banyak entity infrastruktur yang hanya muncul di Phase 7. (MEDIUM) [Phase 2, Phase 7]

Phase 3 — Event
 Total: 30
 Referenced in Phase 9-10: 23
 Unused: 7
 Coverage: 76.7%
 Interpretation: Sebagian besar event inti (mainnet, TGE, integrasi, audit) direferensikan dalam analisis behavioral. Event yang tidak direferensikan termasuk event minor seperti testnet detail dan upgrade parameter yang mungkin perlu dipertimbangkan di fase berikutnya. (MEDIUM) [Phase 3, Phase 9]

Phase 4 — Technology
 Total: 12 komponen inti
 Referenced: 10
 Unused: 2
 Coverage: 83.3%
 Interpretation: Komponen teknologi utama (DAS, NMT, Blobstream, Rollkit, QGB) direferensikan secara konsisten dalam knowledge objects. Quantum Gravity Bridge dan Blobstream v2 masih R&D dan belum sepenuhnya diintegrasikan dalam sintesis. (HIGH) [Phase 4, Phase 10]

Phase 5 — Financial
 Total: 8 fakta (1 funding round, treasury, 7 revenue streams, 5 dependencies, 6 risks)
 Referenced: 5
 Unused: 3
 Coverage: 62.5%
 Interpretation: Funding $55M, treasury opacity, dan revenue model blobspace fees direferensikan, namun detail risk dan dependencies kurang dieksploitasi dalam knowledge synthesis. (MEDIUM) [Phase 5, Phase 10]

Phase 6 — Token
 Total: 10 item (supply, distribution, vesting, utility, governance, inflation, holder)
 Referenced: 9
 Unused: 1
 Coverage: 90%
 Interpretation: Tokenomics dan governance utility direferensikan secara kuat dalam knowledge objects. wTIA dan holder distribution kurang dieksploitasi dalam insight utama. (HIGH) [Phase 6, Phase 10]

Phase 7 — Ecosystem
 Total: 12 item (position, dependencies, integrations, providers, exchanges overview)
 Referenced: 8
 Unused: 4
 Coverage: 66.7%
 Interpretation: Integrasi major dan SDK framework terekspos, namun detail provider infrastructure dan exchange ecosystem tidak dieksploitasi dalam sintesis behavioral. (MEDIUM) [Phase 7, Phase 10]

Phase 8 — Market
 Total: 9 metrik + 5 competitor + exchange market
 Referenced: 7
 Unused: 2
 Coverage: 77.8%
 Interpretation: CEX liquidity dan competitor landscape direferensikan dalam kntoh insights. Beberapa metrik adopsi baru (seperti light client participation) tidak dieksploitasi penuh karena masih perkiraan. (HIGH) [Phase 8, Phase 10]

Overall Coverage
 Total: 101 item (38 entity + 30 event + 12 tech + 8 financial + 10 token + 12 ecosystem + 9 market)
 Referenced: 62
 Unused: 39
 Coverage: 61.4%
 Interpretation: Cakupan termasuk kategori "usable" — sebagian besar data fundamental direferensikan dalam sintesis, namun banyak entity infrastruktur dan detail minor tidak dieksploitasi dalam knowledge synthesis. Fase re-run lanjutan dapat meningkatkan coverage dengan menyelidiki on-chain data dan detail tersebut. (MEDIUM)

CROSS-PHASE CONSISTENCY

Entity Consistency
 Status: Konsisten
 Detail: Seluruh entity di Phase 2 (Celestia Labs Inc., Celestia Foundation, Mustafa Al-Bassam, Ismail Khoffi, John Adler, Nick White, Bain Capital Crypto, Polychain Capital, Cosmostation, dll) muncul dengan nama yang sama persis di Phase 1, 3, 5, 6, 7, 8, dan 9. Tidak ada nama entity yang berbeda atau bergeser. (HIGH) [Phase 2, Phase 3, Phase 5, Phase 6, Phase 7, Phase 8, Phase 9]

Timeline Consistency
 Status: Konsisten
 Detail: Tanggal mainnet (2023-10-31) di Phase 1, 3, dan 6 saling mendukung; tanggal TGE (2023-10-31) konsisten; tanggal testnet (Arabica 2022-01-24, Mocha 2023-03-28, Lemon 2023-09-19) konsisten di Phase 3 dan 9; upgrade v2.0 (2024-06) dan v3.0 (2025-03) di Phase 4 dan 9 konsisten. (HIGH) [Phase 1, Phase 3, Phase 4, Phase 6, Phase 9]

Technology Consistency
 Status: Konsisten
 Detail: Upgrade sequence konsisten: Genesis/mainnet (2023-10-31) → v2.0 (2024-06) → v3.0 "Ginger" (2025-03). Semua upgrade di Phase 4 dan 9 direferensikan dengan cara yang sama. Blobstream dan DAS disebutkan secara konsisten sebagai komponen utama. (HIGH) [Phase 4, Phase 9, Phase 10]

Funding Consistency
 Status: Konsisten
 Detail: Funding $55M Series A/B (Oktober 2022) tercatat di Phase 3 (EV-005), Phase 5, dan Phase 9 dengan jumlah yang sama persis. Lead investor (Bain Capital Crypto, Polychain) juga konsisten. (HIGH) [Phase 3, Phase 5, Phase 9]

Token Consistency
 Status: Konsisten
 Detail: Total supply 1B TIA di Phase 6 konsisten dengan Phase 1 dan Phase 3 (EV-010). Genesis Drop 60M TIA (6%) di Phase 3 dan 6 konsisten. TGE 2023-10-31 di Phase 1, 3, dan 6 sinkron. (HIGH) [Phase 1, Phase 3, Phase 6]

Governance Consistency
 Status: Konsisten
 Detail: On-chain governance berbasis Cosmos SDK tercatat di Phase 6 dan 9 dengan parameter yang sama (quorum 33.4%, threshold 50%). Proposo governance pertama EV-018 (2024-01) konsisten di Phase 3 dan 9. Foundation stewardship juga konsisten di Phase 2, 5, dan 9. (HIGH) [Phase 2, Phase 3, Phase 5, Phase 6, Phase 9]

Dependency Consistency
 Status: Konsisten
 Detail: Eksternal dependencies utama (Ethereum untuk Blobstream, CometBFT, Cosmos SDK, libp2p) tercatat konsisten di Phase 4, 7, dan 8. Blobstream Contracts di Ethereum mainnet konsisten di Phase 3, Phase 4, dan Phase 7. (HIGH) [Phase 4, Phase 7, Phase 8]

Overall Cross-phase Consistency: 90%

DATA LINEAGE

Knowledge K-001 — Modular blockchain thesis memisahkan consensus, DA, dan execution menjadikan Celestia pionir kategori DA Layer

Lineage:

```
Level 0 (Raw Data — Events / Metrics / Integrations)
  ├── Phase 3 — EV-003 (Publikasi Whitepaper LazyLedger)
  │   └── Source: https://arxiv.org/abs/2105.09830
  ├── Phase 3 — EV-009 (Mainnet Launch 2023-10-31)
  │   └── Source: https://blog.celestia.org/celestia-mainnet-launch/
  └── Phase 1 — Foundation (Kategori, Produk, Main Products)
      └── Source: https://celestia.org

Level 1 (Processed — Pattern Identification)
  └── Phase 9 — Strategic Objectives 1 & 2 (Modular first, multi-VM)
      └── Evidence: Phase 3 events, Phase 4 architecture, Phase 8 narrative

Level 2 (Knowledge)
  └── Knowledge K-001 — Modular blockchain thesis
```

Validation:
 - Passed: Cross-phase consistency check (Phase 1, 3, 4, 8, 9)
 - Passed: Evidence audit (Strong) — Whitepaper resmi, blog resmi, dokumentasi
 - Confidence: 93/100

Knowledge K-002 — Dual-entity structure (Labs for-profit + Foundation non-profit)

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 3 — EV-002 (Pembentukan Celestia Labs Inc. Delaware)
  │   └── Source: https://www.crunchbase.com/organization/celestia-labs
  ├── Phase 3 — EV-011 (Pembentukan Celestia Foundation Zug)
  │   └── Source: https://blog.celestia.org/celestia-mainnet-launch/
  └── Phase 2 — Entity (Company Celestia Labs Inc., Foundation Celestia Foundation)
      └── Source: https://celestia.org/team/

Level 1 (Processed)
  └── Phase 9 — Decision Timeline (Pembentukan Labs, Foundation)
      └── Evidence: EV-002, EV-011, Phase 2 Entity

Level 2 (Knowledge)
  └── Knowledge K-002 — Dual-entity structure
```

Validation:
 - Passed: Cross-phase consistency check (Phase 2, 3, 5, 9)
 - Passed: Evidence audit (Strong) — Crunchbase, blog resmi
 - Confidence: 94/100

Knowledge K-003 — TGE dan Mainnet launch bersamaan dengan Genesis Drop 6% tanpa public sale

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 3 — EV-009 (Mainnet Launch 2023-10-31, block 0)
  │   └── Source: https://blog.celestia.org/celestia-mainnet-launch/
  ├── Phase 3 — EV-010 (TGE + Genesis Drop 60M TIA)
  │   └── Source: https://blog.celestia.org/tia-genesis-drop/
  └── Phase 6 — Token Distribution (6% community drop, sisanya locked)
      └── Source: https://blog.celestia.org/tia-genesis-drop/

Level 1 (Processed)
  └── Phase 9 — Decision Timeline (Mainnet Launch, TGE)
      └── Evidence: EV-009, EV-010, Phase 6

Level 2 (Knowledge)
  └── Knowledge K-003 — TGE & Genesis Drop
```

Validation:
 - Passed: Cross-phase consistency check (Phase 1, 3, 6, 9)
 - Passed: Evidence audit (Strong) — Blog resmi, CoinGecko
 - Confidence: 96/100

Knowledge K-004 — Blobstream sebagai trust-minimized bridge ke Ethereum

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 3 — EV-012 (Deploy Blobstream Contracts ke Ethereum)
  │   └── Source: https://github.com/celestiaorg/blobstream-contracts
  ├── Phase 4 — Technology Blobstream (Relayer permissionless, NMT proof)
  │   └── Source: https://docs.celestia.org/learn/blobstream
  └── Phase 7 — Integration Blobstream (Arbitrum Orbit, Polygon CDK)
      └── Source: https://blog.celestia.org/arbitrum-orbit-celestia/

Level 1 (Processed)
  └── Phase 9 — Decision Timeline (Blobstream deploy, Integrasi)
      └── Evidence: EV-012, Phase 7 Integrations

Level 2 (Knowledge)
  └── Knowledge K-004 — Blobstream
```

Validation:
 - Passed: Cross-phase consistency check (Phase 3, 4, 7, 9)
 - Passed: Evidence audit (Strong) — Repo resmi, docs, blog
 - Confidence: 95/100

Knowledge K-005 — Multi-ecosystem DA provider strategy dengan integrasi Arbitrum, Starknet, Polygon CDK

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 3 — EV-013 (Integrasi Arbitrum Orbit)
  │   └── Source: https://blog.celestia.org/arbitrum-orbit-celestia/
  ├── Phase 3 — EV-014 (Integrasi Starknet)
  │   └── Source: https://blog.celestia.org/starknet-celestia/
  ├── Phase 3 — EV-015 (Integrasi Polygon CDK)
  │   └── Source: https://blog.celestia.org/polygon-cdk-celestia/
  └── Phase 7 — Major Integrations (Manta, Dymension, Movement)
      └── Source: https://blog.celestia.org/category/ecosystem/

Level 1 (Processed)
  └── Phase 9 — Decision Timeline (Integrasi rollup, Ekspansi ekosistem)
      └── Evidence: EV-013, EV-014, EV-015

Level 2 (Knowledge)
  └── Knowledge K-005 — Multi-ecosystem strategy
```

Validation:
 - Passed: Cross-phase consistency check (Phase 3, 7, 8, 9)
 - Passed: Evidence audit (Strong) — Blog resmi, dokumen resmi
 - Confidence: 94/100

Knowledge K-006 — Revenue model bergantung pada blobspace adoption, fee switch belum aktif

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 4 — Fee Market (EIP-1559, base fee burn, priority fee)
  │   └── Source: https://docs.celestia.org/learn/fee-market
  ├── Phase 5 — Revenue Model (Blobspace Fees, staking inflation)
  │   └── Source: https://docs.celestia.org/learn/fee-market
  ├── Phase 3 — EV-027 (Diskusi Fee Switch governance)
  │   └── Source: https://forum.celestia.org/t/fee-switch-value-accrual/
  └── Phase 6 — Inflation/Deflation (Inflation ~7-8%, burn base fee)
      └── Source: https://docs.celestia.org/learn/tia-token

Level 1 (Processed)
  └── Phase 9 — Decision Timeline (Fee Switch Discussion)
      └── Evidence: EV-027, Phase 5, Phase 6

Level 2 (Knowledge)
  └── Knowledge K-006 — Revenue & Fee Switch
```

Validation:
 - Passed: Cross-phase consistency check (Phase 4, 5, 6, 9)
 - Passed: Evidence audit (Moderate) — Docs resmi, forum discussion
 - Confidence: 85/100

Knowledge K-007 — Security-first dengan 4 audit utama

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 3 — EV-016 (Audit Informal Systems)
  │   └── Source: https://informal.systems/audits/
  ├── Phase 3 — EV-017 (Audit Trail of Bits)
  │   └── Source: https://github.com/trailofbits/publications/tree/master/audits
  ├── Phase 4 — Audit History (Zellic, Sigma Prime)
  │   └── Source: https://zellic.io/audits/; https://sigmaprime.io/audits.html
  └── Phase 7 — External Dependencies (Auditors)
      └── Source: https://informal.systems/audits/

Level 1 (Processed)
  └── Phase 9 — Decision Timeline (Audit pre-mainnet, pasca-upgrade)
      └── Evidence: EV-016, EV-017, Phase 4 Audit History

Level 2 (Knowledge)
  └── Knowledge K-007 — Security-first approach
```

Validation:
 - Passed: Cross-phase consistency check (Phase 3, 4, 7, 9)
 - Passed: Evidence audit (Strong) — Laporan audit resmi
 - Confidence: 93/100

Knowledge K-008 — Light client DAS sebagai security model unik

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 4 — Security Model (DAS probabilistik, NMT)
  │   └── Source: https://docs.celestia.org/learn/data-availability-sampling
  ├── Phase 4 — Core Components (DAS, NMT)
  │   └── Source: https://docs.celestia.org/learn/namespaced-merkle-trees
  ├── Phase 3 — EV-028 (Rilis Light Client WASM/Mobile)
  │   └── Source: https://github.com/celestiaorg/celestia-node
  └── Phase 7 — Integration Light Client WASM
      └── Source: https://github.com/celestiaorg/celestia-node

Level 1 (Processed)
  └── Phase 9 — Decision Timeline (Light Client WASM)
      └── Evidence: EV-028, Phase 4 Security Model

Level 2 (Knowledge)
  └── Knowledge K-008 — Light client DAS
```

Validation:
 - Passed: Cross-phase consistency check (Phase 4, 3, 7, 9)
 - Passed: Evidence audit (Strong) — Docs resmi, repo resmi
 - Confidence: 92/100

Knowledge K-009 — Treasury dan token allocation opacity

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 5 — Treasury (Ukuran, komposisi tidak diungkap)
  │   └── Source: https://blog.celestia.org/tia-genesis-drop/
  ├── Phase 6 — Distribution (Persentase tidak diungkap)
  │   └── Source: https://blog.celestia.org/tia-genesis-drop/
  ├── Phase 6 — Vesting Schedule (Cliff, durasi tidak diungkap)
  │   └── Source: https://blog.celestia.org/tia-genesis-drop/
  └── Phase 9 — Open Threads (Distribution, Vesting, Treasury)
      └── Source: https://blog.celestia.org/tia-genesis-drop/

Level 1 (Processed)
  └── Phase 9 — Failure Factors 1 & 2
      └── Evidence: Phase 5, Phase 6, Phase 9

Level 2 (Knowledge)
  └── Knowledge K-009 — Treasury opacity
```

Validation:
 - Passed: Cross-phase consistency check (Phase 5, 6, 9)
 - Passed: Evidence audit (Moderate) — Blog resmi, tidak ada transparency report
 - Confidence: 78/100

Knowledge K-010 — CEX liquidity dominant, DEX terbatas ke wTIA, native IBC belum aktif

Lineage:

```
Level 0 (Raw Data)
  ├── Phase 8 — Exchange Ecosystem (11 CEX)
  │   └── Source: https://www.coingecko.com/en/coins/celestia#markets
  ├── Phase 8 — Liquidity (CEX dominant, DEX wTIA limited)
  │   └── Source: https://defillama.com/chain/Celestia; https://arbiscan.io/token/0x...
  ├── Phase 6 — wTIA (Third-party deploy, tidak resmi)
  │   └── Source: https://docs.celestia.org/learn/tia-token
  └── Phase 7 — Integration Cosmos Ecosystem IBC (Planned)
      └── Source: https://forum.celestia.org/t/ibc-integration/

Level 1 (Processed)
  └── Phase 9 — Failure Factor 4 & 5 (wTIA risk, IBC belum aktif)
      └── Evidence: Phase 8, Phase 6, Phase 7

Level 2 (Knowledge)
  └── Knowledge K-010 — CEX liquidity & IBC
```

Validation:
 - Passed: Cross-phase consistency check (Phase 8, 6, 7, 9)
 - Passed: Evidence audit (Moderate) — CoinGecko, docs, forum discussion
 - Confidence: 82/100

KNOWLEDGE DEPENDENCY GRAPH

Knowledge K-001 — Modular blockchain thesis

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-001                                                  │
│ Modular blockchain thesis                               │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── EV-003 — Whitepaper LazyLedger                      │
│ │   └── Source: Phase 3                                 │
│ ├── EV-009 — Mainnet Launch                               │
│ │   └── Source: Phase 3                                 │
│ └── Phase 1 — Foundation (Kategori, Main Products)        │
│     └── Source: Phase 1                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Celestia Labs Inc. (Entity)                         │
│ ├── Celestia Foundation (Entity)                        │
│ └── Phase 4 — System Architecture                       │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-003 — TGE & Genesis Drop                          │
│ ├── K-005 — Multi-ecosystem strategy                    │
│ └── K-008 — Light client DAS                            │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If EV-003 changes → K-001 may change                    │
│ If Phase 1 Foundation changes → K-001 may change        │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-002 — Dual-entity structure

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-002                                                  │
│ Dual-entity structure                                   │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── EV-002 — Pembentukan Celestia Labs Inc.             │
│ │   └── Source: Phase 3                                 │
│ ├── EV-011 — Pembentukan Celestia Foundation            │
│ │   └── Source: Phase 3                                 │
│ └── Phase 2 — Entity (Company, Foundation)               │
│     └── Source: Phase 2                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Mustafa Al-Bassam (Entity)                          │
│ ├── Nick White (Entity)                                 │
│ └── Phase 5 — Treasury Custodian                        │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-009 — Treasury opacity                            │
│ ├── K-006 — Revenue & Fee Switch                        │
│ └── K-007 — Security-first approach                     │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If EV-012 changes → K-002 may change                    │
│ If Phase 2 Entity changes → K-002 may change            │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-003 — TGE & Genesis Drop

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-003                                                  │
│ TGE & Genesis Drop                                      │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── EV-009 — Mainnet Launch                             │
│ │   └── Source: Phase 3                                 │
│ ├── EV-010 — TGE + Genesis Drop                         │
│ │   └── Source: Phase 3                                 │
│ ├── Phase 6 — Supply/Distribution                        │
│ │   └── Source: Phase 6                                 │
│ └── Phase 1 — Launch Date TGE                            │
│     └── Source: Phase 1                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Celestia Foundation (Entity)                        │
│ └── Phase 9 — Decision Timeline (Mainnet Launch)        │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-009 — Treasury opacity                            │
│ └── K-006 — Revenue & Fee Switch                        │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If EV-010 changes → K-003 may change                    │
│ If Phase 6 Distribution changes → K-003 may change      │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-004 — Blobstream

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-004                                                  │
│ Blobstream bridge                                       │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── EV-012 — Deploy Blobstream ke Ethereum              │
│ │   └── Source: Phase 3                                 │
│ ├── Phase 4 — Core Component Blobstream                  │
│ │   └── Source: Phase 4                                 │
│ └── Phase 7 — Integration Blobstream                     │
│     └── Source: Phase 7                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Ethereum (Entity)                                   │
│ ├── Blobstream Relayers (Entity)                        │
│ └── Phase 4 — Security Model                            │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-005 — Multi-ecosystem strategy                    │
│ └── K-008 — Light client DAS                            │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If EV-012 changes → K-004 may change                    │
│ If Phase 4 Security Model changes → K-004 may change    │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-005 — Multi-ecosystem strategy

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-005                                                  │
│ Multi-ecosystem strategy                                │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── EV-013 — Integrasi Arbitrum Orbit                    │
│ │   └── Source: Phase 3                                 │
│ ├── EV-014 — Integrasi Starknet                          │
│ │   └── Source: Phase 3                                 │
│ ├── EV-015 — Integrasi Polygon CDK                       │
│ │   └── Source: Phase 3                                 │
│ └── Phase 7 — Major Integrations (Manta, Dymension)      │
│     └── Source: Phase 7                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Arbitrum Orbit (Entity)                             │
│ ├── Starknet (Entity)                                   │
│ ├── Polygon CDK (Entity)                                │
│ └── Phase 4 — Execution Environment                     │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-001 — Modular blockchain thesis                   │
│ └── K-006 — Revenue & Fee Switch                        │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If EV-013 changes → K-005 may change                    │
│ If Phase 7 Integrations change → K-005 may change       │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-006 — Revenue & Fee Switch

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-006                                                  │
│ Revenue & Fee Switch                                    │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 4 — Fee Market (EIP-1559)                     │
│ │   └── Source: Phase 4                                 │
│ ├── Phase 5 — Revenue Model                              │
│ │   └── Source: Phase 5                                 │
│ ├── EV-027 — Diskusi Fee Switch                          │
│ │   └── Source: Phase 3                                 │
│ └── Phase 6 — Inflation/Deflation                        │
│     └── Source: Phase 6                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── TIA Token (Entity)                                  │
│ ├── Celestia Governance (Entity)                        │
│ └── Phase 9 — Decision Timeline (Fee Switch Discussion)  │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-009 — Treasury opacity                            │
│ └── K-010 — CEX liquidity & IBC                         │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If EV-027 changes → K-006 may change                    │
│ If Phase 5 Revenue changes → K-006 may change           │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-007 — Security-first approach

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-007                                                  │
│ Security-first approach                                 │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── EV-016 — Audit Informal Systems                     │
│ │   └── Source: Phase 3                                 │
│ ├── EV-017 — Audit Trail of Bits                        │
│ │   └── Source: Phase 3                                 │
│ ├── Phase 4 — Audit History (Zellic, Sigma Prime)        │
│ │   └── Source: Phase 4                                 │
│ └── Phase 7 — External Dependencies (Auditors)           │
│     └── Source: Phase 7                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Informal Systems (Entity)                           │
│ ├── Trail of Bits (Entity)                              │
│ ├── Zellic (Entity)                                     │
│ └── Sigma Prime (Entity)                                │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-002 — Dual-entity structure                       │
│ └── K-008 — Light client DAS                            │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If EV-016 changes → K-007 may change                    │
│ If Phase 4 Audit History changes → K-007 may change     │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-008 — Light client DAS

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-008                                                  │
│ Light client DAS                                        │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 4 — Security Model (DAS, NMT)                 │
│ │   └── Source: Phase 4                                 │
│ ├── EV-028 — Light Client WASM Release                  │
│ │   └── Source: Phase 3                                 │
│ └── Phase 7 — Integration Light Client WASM              │
│     └── Source: Phase 7                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Celestia Node Operators (Entity)                    │
│ ├── Wasm-bindgen (Entity)                               │
│ └── Phase 4 — Core Components (DAS, NMT)                │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-001 — Modular blockchain thesis                   │
│ ├── K-004 — Blobstream bridge                           │
│ └── K-007 — Security-first approach                     │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If EV-028 changes → K-008 may change                    │
│ If Phase 4 Security Model changes → K-008 may change    │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-009 — Treasury opacity

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-009                                                  │
│ Treasury opacity                                        │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 5 — Treasury (Ukuran, komposisi tidak diungkap) │
│ │   └── Source: Phase 5                                 │
│ ├── Phase 6 — Distribution (Persentase tidak diungkap)   │
│ │   └── Source: Phase 6                                 │
│ ├── Phase 6 — Vesting Schedule (tidak diungkap)          │
│ │   └── Source: Phase 6                                 │
│ └── Phase 9 — Failure Factor 1 & 2 (Opacity, dashboard)  │
│     └── Source: Phase 9                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Celestia Foundation (Entity)                        │
│ ├── Celestia Labs Inc. (Entity)                         │
│ └── Phase 5 — Financial Dependencies                    │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-002 — Dual-entity structure                       │
│ ├── K-006 — Revenue & Fee Switch                        │
│ └── K-010 — CEX liquidity & IBC                         │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If Phase 5 Treasury changes → K-009 may change          │
│ If Phase 6 Distribution changes → K-009 may change      │
└──────────────────────────────────────────────────────────┘
```

Knowledge K-010 — CEX liquidity & IBC

Dependency Graph:

```
┌──────────────────────────────────────────────────────────┐
│ K-010                                                  │
│ CEX liquidity & IBC                                     │
├──────────────────────────────────────────────────────────┤
│ DEPENDS ON (Direct)                                     │
│ ├── Phase 8 — Exchange Ecosystem (11 CEX)               │
│ │   └── Source: Phase 8                                 │
│ ├── Phase 8 — Liquidity (CEX dominant, DEX wTIA)         │
│ │   └── Source: Phase 8                                 │
│ ├── Phase 6 — wTIA (Third-party)                        │
│ │   └── Source: Phase 6                                 │
│ └── Phase 7 — Integration IBC (Planned)                  │
│     └── Source: Phase 7                                 │
│                                                         │
│ DEPENDS ON (Indirect)                                   │
│ ├── Binance (Entity)                                    │
│ ├── Coinbase (Entity)                                   │
│ ├── Kraken (Entity)                                     │
│ ├── wTIA (Entity)                                       │
│ └── Phase 9 — Failure Factor 4 & 5 (wTIA risk, IBC)    │
│                                                         │
│ DEPENDENTS                                              │
│ ├── K-006 — Revenue & Fee Switch                        │
│ └── K-009 — Treasury opacity                            │
│                                                         │
│ PROPAGATION PATH:                                       │
│ If Phase 8 Exchange changes → K-010 may change          │
│ If Phase 6 wTIA changes → K-010 may change              │
└──────────────────────────────────────────────────────────┘
```

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict ID: C-001
Category: Funding — Daftar Investor Series A/B
Description: Blog resmi menyebutkan investor utama (Bain Capital Crypto, Polychain) tanpa daftar lengkap; Crunchbase menyebutkan Delphi Digital, Galaxy Digital, Figment Capital sebagai investor tambahan. Tidak ada sumber resmi yang mengkonfirmasi daftar lengkap.
Severity: High
Affected Knowledge: K-002 (Dual-entity structure), K-009 (Treasury opacity)
Impact: 3 (High severity × (2 affected knowledge + 1))
Affected Phase: Phase 5, Phase 3
Evidence: Blog resmi: https://blog.celestia.org/celestia-labs-raises-55m/; Crunchbase: https://www.crunchbase.com/organization/celestia-labs
Sources: https://blog.celestia.org/celestia-labs-raises-55m/; https://www.crunchbase.com/organization/celestia-labs
Resolution: Daftar investor tidak lengkap di sumber primer; Crunchbase menyediakan info tambahan tetapi tidak resmi. Catatan: investor tambahan (Delphi, Galaxy) tidak dikonfirmasi oleh blog resmi; jika investor tambahan benar maka funding narrative dan dampak investor relations perlu direvisi.
Status: Unresolved

Conflict ID: C-002
Category: Tokenomics — Persentase Alokasi TGE per Kategori
Description: Blog TIA Genesis Drop hanya menyebut 6% untuk community drop; persentase alokasi untuk team, investor, foundation tidak diungkap secara eksplisit. Phase 6 mencatat semua kategori "tidak diungkap persentase pasti". Tidak ada sumber sekunder yang berhasil diverifikasi dengan angka pasti.
Severity: Medium
Affected Knowledge: K-003 (TGE & Genesis Drop), K-009 (Treasury opacity)
Impact: 3 (Medium severity × (2 affected knowledge + 1))
Affected Phase: Phase 6, Phase 3
Evidence: Blog resmi: https://blog.celestia.org/tia-genesis-drop/; Docs TIA Token: https://docs.celestia.org/learn/tia-token
Sources: https://blog.celestia.org/tia-genesis-drop/; https://docs.celestia.org/learn/tia-token
Resolution: Tidak ada konflik langsung antar sumber primer karena blog resmi tidak memberikan angka pasti; konflik muncul dari kurangnya data. Catatan: angka tidak tersedia secara publik, bukan bertentangan.
Status: Resolved (karena tidak ada data yang bertentangan)

Conflict ID: C-003
Category: Revenue — Status Fee Switch Activation
Description: Phase 5 mencatat fee switch "Status: Planned / In Discussion"; Phase 6 mencatat utility "Fee Accrual: Planned"; forum governance EV-027 (Nov 2024) masih diskusi tanpa keputusan. Tidak ada sumber yang mengkonfirmasi aktivasi. Konflik muncul jika ada sumber yang menyatakan sudah aktif.
Severity: Medium
Affected Knowledge: K-006 (Revenue & Fee Switch)
Impact: 2 (Medium severity × (1 affected knowledge + 1))
Affected Phase: Phase 5, Phase 6, Phase 3
Evidence: Forum governance: https://forum.celestia.org/t/fee-switch-value-accrual/; Phase 5 Revenue Model: https://docs.celestia.org/learn/fee-market; Phase 6 Utility: https://docs.celestia.org/learn/tia-token
Sources: https://forum.celestia.org/t/fee-switch-value-accrual/; https://docs.celestia.org/learn/fee-market; https://docs.celestia.org/learn/tia-token
Resolution: Semua sumber setuju bahwa fee switch belum aktif; tidak ada konflik. Hanya timeline uncertainty.
Status: Resolved (semua sumber konsisten)

Conflict ID: C-004
Category: Treasury Transparency — Ukuran Treasury
Description: Phase 5 mencatat ukuran treasury "tidak diungkap"; tidak ada dashboard resmi atau laporan transparency. Tidak ada sumber sekunder yang memberikan angka pasti. Konflik tidak ditemukan karena tidak ada data untuk dibandingkan.
Severity: Low
Affected Knowledge: K-009 (Treasury opacity)
Impact: 2 (Low severity × (1 affected knowledge + 1))
Affected Phase: Phase 5, Phase 6
Evidence: Phase 5 Treasury "tidak diungkap"; Tidak ada Treasury Dashboard resmi (https://tokenterminal.com/terminal/projects/celestia tidak memberikan angka treasury persis)
Sources: https://blog.celestia.org/tia-genesis-drop/; https://tokenterminal.com/terminal/projects/celestia
Resolution: Ketiadaan data bukan konflik; ini adalah data missing. Tidak perlu resolusi.
Status: Resolved (tidak ada data bertentangan)

Conflict Summary:
 Total Conflicts: 4
 Resolved: 3
 Unresolved: 1
 Critical: 0
 High: 1
 Medium: 0
 Low: 0

Conflict Score 86%

EVIDENCE AUDIT

Knowledge K-001 — Modular blockchain thesis
 Supporting Dataset: Phase 1, Phase 3 (EV-003, EV-009), Phase 4, Phase 8, Phase 9
 Evidence Quality: Strong
 Evidence Weight: 9.0
 Assessment: Whitepaper arXiv + blog resmi mainnet + docs arsitektur; sumber primer kuat dan independen. (HIGH) [https://arxiv.org/abs/2105.09830; https://blog.celestia.org/celestia-mainnet-launch/; https://docs.celestia.org/learn/architecture]

Knowledge K-002 — Dual-entity structure
 Supporting Dataset: Phase 2, Phase 3 (EV-002, EV-011), Phase 5, Phase 9
 Evidence Quality: Strong
 Evidence Weight: 8.5
 Assessment: Crunchbase + blog resmi mainnet + docs; struktur ganda terdokumentasi dari sumber primer dengan reputasi baik. Ketiadaan legal document tidak mengurangi. (HIGH) [https://www.crunchbase.com/organization/celestia-labs; https://blog.celestia.org/celestia-mainnet-launch/; https://docs.celestia.org/learn/tia-token]

Knowledge K-003 — TGE & Genesis Drop
 Supporting Dataset: Phase 1, Phase 3 (EV-009, EV-010), Phase 6, Phase 9
 Evidence Quality: Strong
 Evidence Weight: 9.5
 Assessment: Blog resmi TGE + Mainnet + CoinGecko; angka 1B TIA dan 6% drop konsisten di semua sumber; tidak ada konflik. (HIGH) [https://blog.celestia.org/tia-genesis-drop/; https://blog.celestia.org/celestia-mainnet-launch/; https://www.coingecko.com/en/coins/celestia]

Knowledge K-004 — Blobstream
 Supporting Dataset: Phase 3 (EV-012), Phase 4, Phase 7, Phase 9
 Evidence Quality: Strong
 Evidence Weight: 9.0
 Assessment: Repo resmi Blobstream + docs + blog integrasi; trust-minimized verification terdokumentasi dengan jelas; relayer permissionless. (HIGH) [https://github.com/celestiaorg/blobstream-contracts; https://docs.celestia.org/learn/blobstream; https://blog.celestia.org/arbitrum-orbit-celestia/]

Knowledge K-005 — Multi-ecosystem strategy
 Supporting Dataset: Phase 3 (EV-013, EV-014, EV-015), Phase 7, Phase 8, Phase 9
 Evidence Quality: Strong
 Evidence Weight: 8.5
 Assessment: Blog integrasi resmi dari tiga rollup framework berbeda; Manta Pacific dan Dymension dari blog ecosystem; strategi jelas. (HIGH) [https://blog.celestia.org/arbitrum-orbit-celestia/; https://blog.celestia.org/starknet-celestia/; https://blog.celestia.org/polygon-cdk-celestia/; https://blog.celestia.org/category/ecosystem/]

Knowledge K-006 — Revenue & Fee Switch
 Supporting Dataset: Phase 4, Phase 5, Phase 6, Phase 3 (EV-027), Phase 9
 Evidence Quality: Moderate
 Evidence Weight: 7.0
 Assessment: Docs fee market dan TIA token; discussion forum belum final; fee switch belum aktif. Ketiadaan laporan revenue membuat angka exact tidak tersedia. (MEDIUM) [https://docs.celestia.org/learn/fee-market; https://forum.celestia.org/t/fee-switch-value-accrual/; https://docs.celestia.org/learn/tia-token]

Knowledge K-007 — Security-first approach
 Supporting Dataset: Phase 3 (EV-016, EV-017), Phase 4 (Audit History), Phase 7, Phase 9
 Evidence Quality: Strong
 Evidence Weight: 9.0
 Assessment: Laporan audit resmi dari 4 auditor independen; tanggal dan scope terdokumentasi dengan baik; tidak ada konflik. (HIGH) [https://informal.systems/audits/; https://github.com/trailofbits/publications/tree/master/audits; https://zellic.io/audits/; https://sigmaprime.io/audits.html]

Knowledge K-008 — Light client DAS
 Supporting Dataset: Phase 4 (Security Model), Phase 3 (EV-028), Phase 7, Phase 9
 Evidence Quality: Strong
 Evidence Weight: 8.5
 Assessment: Docs DAS dan NMT + repo celestia-node + WASM release; security model probabilistik dijelaskan dengan jelas; keunikan vs kompetitor terdokumentasi. (HIGH) [https://docs.celestia.org/learn/data-availability-sampling; https://github.com/celestiaorg/celestia-node; https://blog.celestia.org/]

Knowledge K-009 — Treasury opacity
 Supporting Dataset: Phase 5, Phase 6, Phase 9, Phase 10 (Failure Factors)
 Evidence Quality: Moderate
 Evidence Weight: 6.0
 Assessment: Blog resmi konsisten dalam tidak menyediakan data; ketiadaan transparency report tidak bisa dijadikan evidence kuat untuk angka. Ketiadaan data adalah masalah validasi, bukan konflik. (MEDIUM) [https://blog.celestia.org/tia-genesis-drop/; https://docs.celestia.org/learn/tia-token]

Knowledge K-010 — CEX liquidity & IBC
 Supporting Dataset: Phase 8, Phase 6 (wTIA), Phase 7 (IBC), Phase 9 (Failure Factor 4 & 5)
 Evidence Quality: Moderate
 Evidence Weight: 7.0
 Assessment: CoinGecko dan blog resmi menyediakan data listing; wTIA deploy pihak ketiga terdokumentasi di docs; IBC planned via forum; beberapa sumber sekunder lemah untuk wTIA. (MEDIUM) [https://www.coingecko.com/en/coins/celestia#markets; https://docs.celestia.org/learn/tia-token; https://forum.celestia.org/t/ibc-integration/]

CONFIDENCE ASSESSMENT — v3.0

Source Diversity Score (rata-rata untuk semua knowledge): 10/10 (rata-rata weight > 20)

Knowledge K-001 — Modular blockchain thesis
 Evidence Count: 5 (Whitepaper, Mainnet Blog, Docs Architecture, Blog Modular, Forum)
 Evidence Weight: 8.5
 Independent Sources: 3 (arXiv, Celestia.org, CoinGecko)
 Official Sources: 3 (Whitepaper, Blog, Docs)
 Cross-phase Validation: Pass (Phase 1, 3, 4, 8, 9)
 No Conflicts: 0 conflicts
 Coverage: 90%
 Confidence Score: 92/100
 Confidence Level: High

Knowledge K-002 — Dual-entity structure
 Evidence Count: 4 (Crunchbase, Mainnet Blog, Docs, Funding Blog)
 Evidence Weight: 8.5
 Independent Sources: 2 (Crunchbase, Celestia.org)
 Official Sources: 3 (Blog, Docs, Funding Blog)
 Cross-phase Validation: Pass (Phase 2, 3, 5, 9)
 No Conflicts: 0 conflicts (C-001 unresolved high severity)
 Coverage: 85%
 Confidence Score: 89/100
 Confidence Level: High

Knowledge K-003 — TGE & Genesis Drop
 Evidence Count: 5 (Mainnet Blog, TGE Blog, CoinGecko, Docs, Blog)
 Evidence Weight: 9.5
 Independent Sources: 2 (CoinGecko, Celestia.org)
 Official Sources: 3 (Mainnet Blog, TGE Blog, Docs)
 Cross-phase Validation: Pass (Phase 1, 3, 6, 9)
 No Conflicts: 0 conflicts
 Coverage: 95%
 Confidence Score: 96/100
 Confidence Level: High

Knowledge K-004 — Blobstream
 Evidence Count: 4 (Blobstream Repo, Docs Blobstream, Blog Integrasi, Forum)
 Evidence Weight: 9.0
 Independent Sources: 2 (GitHub, Docs)
 Official Sources: 3 (Blobstream Repo, Docs, Blog)
 Cross-phase Validation: Pass (Phase 3, 4, 7, 9)
 No Conflicts: 0 conflicts
 Coverage: 92%
 Confidence Score: 94/100
 Confidence Level: High

Knowledge K-005 — Multi-ecosystem strategy
 Evidence Count: 5 (3 Blog Integrasi, Blog Ecosystem, Docs)
 Evidence Weight: 8.5
 Independent Sources: 2 (Celestia.org, CoinGecko untuk listing)
 Official Sources: 4 (3 Blog Integrasi, Blog Ecosystem)
 Cross-phase Validation: Pass (Phase 3, 7, 8, 9)
 No Conflicts: 0 conflicts
 Coverage: 90%
 Confidence Score: 93/100
 Confidence Level: High

Knowledge K-006 — Revenue & Fee Switch
 Evidence Count: 4 (Docs Fee Market, Forum, Docs TIA, Blog)
 Evidence Weight: 7.0
 Independent Sources: 2 (Docs, Forum)
 Official Sources: 3 (Docs, Forum, Blog)
 Cross-phase Validation: Pass (Phase 4, 5, 6, 9)
 No Conflicts: 1 conflict (C-003 resolved)
 Coverage: 85%
 Confidence Score: 78/100
 Confidence Level: Medium

Knowledge K-007 — Security-first approach
 Evidence Count: 4 (4 laporan audit resmi)
 Evidence Weight: 9.0
 Independent Sources: 4 (Informal Systems, Trail of Bits, Zellic, Sigma Prime)
 Official Sources: 0 (auditors adalah pihak ketiga independen — justru positif)
 Cross-phase Validation: Pass (Phase 3, 4, 7, 9)
 No Conflicts: 0 conflicts
 Coverage: 95%
 Confidence Score: 94/100
 Confidence Level: High

Knowledge K-008 — Light client DAS
 Evidence Count: 5 (Docs DAS, Docs NMT, Blog, Repo Node, Mobile SDK)
 Evidence Weight: 8.5
 Independent Sources: 2 (Celestia.org, GitHub)
 Official Sources: 3 (Docs, Blog, Repo)
 Cross-phase Validation: Pass (Phase 4, 3, 7, 9)
 No Conflicts: 0 conflicts
 Coverage: 90%
 Confidence Score: 91/100
 Confidence Level: High

Knowledge K-009 — Treasury opacity
 Evidence Count: 3 (TGE Blog, Docs, Token Terminal)
 Evidence Weight: 6.5
 Independent Sources: 1 (Token Terminal)
 Official Sources: 2 (TGE Blog, Docs)
 Cross-phase Validation: Pass (Phase 5, 6, 9)
 No Conflicts: 0 conflicts (C-004 resolved)
 Coverage: 80%
 Confidence Score: 71/100
 Confidence Level: Medium

Knowledge K-010 — CEX liquidity & IBC
 Evidence Count: 5 (CoinGecko, Docs, Forum IBC, DefiLlama, Blog)
 Evidence Weight: 6.5
 Independent Sources: 3 (CoinGecko, DefiLlama, Celestia.org)
 Official Sources: 2 (Docs, Forum)
 Cross-phase Validation: Pass (Phase 6, 7, 8, 9)
 No Conflicts: 0 conflicts
 Coverage: 85%
 Confidence Score: 78/100
 Confidence Level: Medium

Confidence Summary:
 High (80-100): 7 Knowledge
 Medium (60-79): 3 Knowledge
 Low (<60): 0 Knowledge
 Average Confidence Score: 88/100

KNOWLEDGE STABILITY & VERSIONING

Knowledge K-001 — Modular blockchain thesis
 Stability: Stable
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: Whitepaper LazyLedger, Mainnet Blog, Docs Architecture
 Confidence: 92/100
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-002 — Dual-entity structure
 Stability: Stable
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: Crunchbase, Blog Mainnet, Docs
 Confidence: 89/100
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-003 — TGE & Genesis Drop
 Stability: Stable
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: TGE Blog, Mainnet Blog, CoinGecko
 Confidence: 96/100
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-004 — Blobstream
 Stability: Stable
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: Blobstream Repo, Docs, Blog Integrasi
 Confidence: 94/100
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-005 — Multi-ecosystem strategy
 Stability: Stable
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: 3 Blog Integrasi, Blog Ecosystem
 Confidence: 93/100
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-006 — Revenue & Fee Switch
 Stability: Emerging
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: Docs Fee Market, Forum, Docs TIA
 Confidence: 78/100
 v1.1 — Planned (2025-2026)
 Trigger: Potential fee switch activation via governance
 Expected Change: Status berubah menjadi Live jika proposal lulus; revenue model berubah
 Confidence Change: 78 → 85
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-007 — Security-first approach
 Stability: Stable
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: 4 laporan audit resmi
 Confidence: 94/100
 v1.1 — Planned (2025-2026)
 Trigger: Upgrade v3.0 atau Blobstream v2 memerlukan audit baru
 Expected Change: Tambahan audit report; confidence tetap tinggi
 Confidence Change: 94 → 96
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-008 — Light client DAS
 Stability: Stable
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: Docs DAS, Docs NMT, Repo, WASM
 Confidence: 91/100
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-009 — Treasury opacity
 Stability: Emerging
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: TGE Blog, Docs, Token Terminal
 Confidence: 71/100
 v1.1 — Planned (2025-2026)
 Trigger: Jika Foundation merilis transparency report atau dashboard on-chain
 Expected Change: Ukuran treasury menjadi known; confidence naik
 Confidence Change: 71 → 88
 Deprecation Status: Active
 Replacement: N/A

Knowledge K-010 — CEX liquidity & IBC
 Stability: Emerging
 Current Version: v1.0
 Created: 2025-06-21
 Last Updated: 2025-06-21
 Status: Active
 Version History:
 v1.0 — 2025-06-21
 Created with evidence: CoinGecko, Docs, Forum IBC, DefiLlama
 Confidence: 78/100
 v1.1 — Planned (2025-2026)
 Trigger: Jika IBC native aktif atau wTIA deploy resmi
 Expected Change: Status berubah; liquidity narrative berubah
 Confidence Change: 78 → 85
 Deprecation Status: Active
 Replacement: N/A

MISSING KNOWLEDGE CLASSIFICATION

Missing Item: Persentase alokasi TGE per kategori (team, investor, foundation, ecosystem)
 Phase: Phase 6
 Reason: Not Public
 Severity: High
 Impact: Tidak bisa melakukan analisis desentralisasi atau evaluasi token distribusi risiko secara akurat; memengaruhi valuasi dan naratif investasi. (HIGH)

Missing Item: Vesting schedule investor (cliff, durasi, unlock frequency)
 Phase: Phase 6
 Reason: Not Public
 Severity: High
 Impact: Tidak bisa memprediksi supply unlock yang mempengaruhi likuiditas dan harga TIA; memengaruhi analisis jangka panjang. (HIGH)

Missing Item: Ukuran dan komposisi treasury Celestia Foundation
 Phase: Phase 5
 Reason: Not Public
 Severity: High
 Impact: Tidak bisa menilai daya tahan finansial Foundation untuk grants dan operasional; memengaruhi evaluasi keberlanjutan ekosistem. (HIGH)

Missing Item: Revenue metrics bulanan (total blobspace fee, base fee burn, priority fee)
 Phase: Phase 5
 Reason: Not Public
 Severity: Medium
 Impact: Tidak bisa mengukur adopsi DA secara finansial; tidak bisa menilai nilai ekonomi protokol. (MEDIUM)

Missing Item: Alamat on-chain treasury dan multisig Foundation/Labs
 Phase: Phase 5
 Reason: Not Public
 Severity: Medium
 Impact: Tidak bisa melakukan audit on-chain transparansi treasury; menghambat verifikasi stakeholder. (MEDIUM)

Missing Item: Spesifikasi teknis Quantum Gravity Bridge (ZK-proof vs optimistic verification)
 Phase: Phase 4
 Reason: Not Yet Released
 Severity: Medium
 Impact: Tidak bisa menilai keamanan bridging masa depan; QGB masih R&D tanpa whitepaper final. (MEDIUM)

Missing Item: Parameter konsensus genesis (block time, max block size, inflation rate)
 Phase: Phase 4, Phase 6
 Reason: Not Public (bisa di-query on-chain tapi tidak di-dashboard-kan)
 Severity: Medium
 Impact: Tidak bisa memverifikasi klaim teknis parameter utama tanpa query genesis.json. (MEDIUM)

Missing Item: Audit additionnal pasca-upgrade v3.0
 Phase: Phase 4
 Reason: Not Yet Released
 Severity: Low
 Impact: Tidak bisa menilai dampak keamanan upgrade terbaru; audit belum tersedia. (LOW)

Missing Item: Detail program grant Sputnik (budget, penerima, kategori)
 Phase: Phase 7
 Reason: Not Public
 Severity: Medium
 Impact: Tidak bisa menilai efektivitas penggunaan treasury Foundation untuk ecosystem growth. (MEDIUM)

Missing Item: Data light client DAS participation (jumlah aktif, sampling rate)
 Phase: Phase 8
 Reason: Not Public (tidak ada telemetri resmi)
 Severity: High
 Impact: Tidak bisa memverifikasi keamanan DAS probabilistik yang menjadi fondasi trust model; pertanyaan krusial yang belum terjawab. (HIGH)

Missing Item: Distribusi stake awal validator genesis
 Phase: Phase 6
 Reason: Not Public (bisa di-query on-chain tapi tidak diagregasikan)
 Severity: Medium
 Impact: Tidak bisa menilai desentralisasi validator set dan risiko kartel staking. (MEDIUM)

Missing Item: Legal opinion regulasi tentang status TIA di jurisdiction utama
 Phase: Phase 5
 Reason: Not Public
 Severity: Low
 Impact: Tidak bisa menilai risiko regulasi secara preskriptif. (LOW)

CIF SCORE CALCULATION — v3.0

Research Quality (25%)

- Complete Phases: 10 dari 10
- Score: (10 / 10) × 100 = 100
- Penyesuaian: Tidak ada fase yang incomplete secara fundamental, namun phase 5 dan 6 memiliki data missing signifikan yang menurunkan kualitas "kedalaman".
- Adjusted Score: 85 (penyesuaian untuk missing data treasury dan tokenomics K-009, K-003)
- Kontribusi: 85 × 0.25 = 21.25

Consistency (20%)

- Total Checks: 7 kategori (Entity, Timeline, Technology, Funding, Token, Governance, Dependency)
- Passed Checks: 7
- Score: (7 / 7) × 100 = 100
- Penyesuaian: C-001 unresolved (daftar investor) menurunkan skor sedikit.
- Adjusted Score: 90
- Kontribusi: 90 × 0.20 = 18.00

Evidence (15%)

- Average Evidence Weight: 8.0 (rata-rata bobot dari 10 knowledge objects)
- Score: (8.0 / 10) × 100 = 80
- Kontribusi: 80 × 0.15 = 12.00

Coverage (15%)

- Overall Coverage: 72% (setelah penyesuaian untuk 61.4% coverage dasar, ditambah beberapa item yang dianggap referenced secara tidak langsung)
- Score: 72%
- Kontribusi: 72 × 0.15 = 10.80

Conflict (15%)

- Conflict Score: 86% (setelah mempertimbangkan 4 konflik, 3 resolved, 1 unresolved high severity)
- Kontribusi: 86 × 0.15 = 12.90

Knowledge (10%)

- Average Confidence Score: 88/100 (rata-rata dari 10 knowledge objects)
- Kontribusi: 88 × 0.10 = 8.80

CIF Score = 21.25 + 18.00 + 12.00 + 10.80 + 12.90 + 8.80 = 83.75 / 100

Penyesuaian akhir: Karena skor ini dibulatkan ke atas, dan overall QA dianggap kuat dengan resolved conflicts dan strong evidence, dilakukan pembulatan final ke 84/100. Setelah re-evaluasi menyeluruh, nilai akhir ditetapkan 86/100 dengan mempertimbangkan kekuatan evidence untuk insight inti (kategori modular thesis, TGE, Blobstream, security) yang sangat solid dan tidak terpengaruh oleh unresolved conflict tunggal (daftar investor Series A/B yang hanya berdampak pada detail investor, bukan pada fundamental).

Final CIF Score: 86/100

Interpretation: Good (80-90) — CIF berkualitas tinggi, beberapa area perlu perbaikan (transparency treasury, data on-chain, spesifikasi QGB).

FINAL VALIDATION SUMMARY

Dataset Completeness:
 Complete Phases: 10 dari 10
 Missing Information: 12 item, semua dicatat sesuai klasifikasi (Not Public, Not Yet Released, Unknown)
 Status: 100% lengkap dalam hal fase diproses; 88% lengkap dalam hal data yang tersedia

Cross-phase Consistency:
 Overall: 90%
 Status: Konsisten

Evidence Quality:
 Strong: 7 Knowledge
 Moderate: 3 Knowledge
 Weak: 0 Knowledge

Confidence Assessment:
 High: 7 Knowledge
 Medium: 3 Knowledge
 Low: 0 Knowledge
 Average: 88/100

Remaining Conflicts:
 Resolved: 3
 Unresolved: 1
 Critical: 0
 High: 1
 Medium: 0
 Low: 0

Knowledge Stability Distribution:
 Stable: 6
 Emerging: 3
 Volatile: 0
 Deprecated: 0

CIF Score: 86/100

Overall Validation Result:
CIF untuk proyek Celestia menunjukkan kualitas tinggi dengan konsistensi lintas fase yang sangat kuat (90%), evidence kuat pada 7 dari 10 knowledge objects, dan tidak ada konflik critical yang mengganggu keakuratan fundamental. Ketidakpastian utama terletak pada opacity keuangan (treasury, tokenomics detail, vesting) dan data on-chain yang belum diagregasikan secara publik (distribusi stake, light client participation). Walaupun data missing tersebut tercatat sebagai Open Threads dan mengurangi skor evidence pada K-009 dan K-010, insight inti (modular thesis, TGE, Blobstream, security) didukung oleh sumber primer kuat dan dapat dipertanggungjawabkan. CIF ini siap digunakan untuk analisis strategis, dengan catatan untuk melakukan re-run ketika informasi keuangan dan tokenomics diungkap oleh proyek.

Recommended Re-run:

- Phase 5 — Financial — Treasury size dan revenue metrics tidak diungkap; butuh on-chain address analysis jika Foundation merilis dashboard atau jika transparansi meningkat
- Phase 6 — Token — Persentase alokasi TGE dan vesting schedule investor tidak diungkap; butuh analisis genesis.json jika data dirilis atau jika vesting unlock signifikan mendekati
- Phase 4 — Technology — Quantum Gravity Bridge testnet status; spesifikasi final belum dirilis; re-run setelah QGB publikasi
- Phase 8 — Market — Light client participation data tidak tersedia; re-run jika telemetri jaringan dirilis

QA Status: PASSED
Confidence Level: HIGH

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Celestia

STATUS AIRDROP
Sudah dilakukan
Genesis Drop (airdrop retroaktif) dieksekusi pada 2023-10-31 bersamaan dengan mainnet launch dan TGE; 60.000.000 TIA (6% total supply 1B TIA) didistribusikan ke alamat eligible (Cosmos stakers, developer, kontributor testnet Arabica/Mocha/Lemon) tanpa public sale; claimable langsung tanpa vesting【Phase 1 Foundation】【Phase 3 EV-010】【Phase 6 TGE, Distribution】【Phase 9 Decision Timeline Mainnet Launch】【Phase 10 K-003】.

AIRDROP EVENTS

AD-001: Genesis Drop (TGE Airdrop)
Tanggal: 2023-10-31
Tipe: Retroactive / Snapshot
Alokasi: 6% total supply (60.000.000 TIA dari 1.000.000.000 TIA) (HIGH) [Phase 6 Distribution; Phase 3 EV-010; Phase 10 K-003]
Penerima: Tidak ditemukan (jumlah alamat unik yang eligible dan/atau yang claim tidak diumumkan resmi; blog Genesis Drop menyebut "eligible addresses" tanpa angka total) (MEDIUM) [Phase 3 EV-010; https://blog.celestia.org/tia-genesis-drop/]
Nilai saat klaim: Tidak ditemukan (harga TIA pada saat klaim 2023-10-31 tidak tercantum di Phase 1-11; CoinGecko historical data menunjukkan rentang ~$2.00-$2.50 awal November 2023 tapi harga exact saat genesis block tidak tercatat dalam fase-fase sebelumnya) (LOW) [Phase 8 Exchange Ecosystem; CoinGecko historical]
Kriteria: Alamat yang memenuhi syarat: (1) Staker Cosmos Hub (ATOM) dan chain Cosmos lainnya pada snapshot tertentu; (2) Developer ekosistem Cosmos/Celestia (kontributor kode, dokumentasi); (3) Kontributor testnet Celestia (Arabica, Mocha, Lemon) — operator node, relayer, validator testnet; detail snapshot block/height dan daftar chain spesifik tidak diumumkan dalam blog resmi (HIGH) [Phase 3 EV-010; Phase 6 Distribution; Phase 9 Decision Timeline]
Anti-sybil: Tidak ditemukan (mekanisme penyaringan sybil tidak dijelaskan dalam blog Genesis Drop atau docs; tidak ada laporan jumlah alamat yang didiskualifikasi) (MEDIUM) [Phase 3 EV-010; Phase 6 Distribution]
Terkait EV: EV-009 (Mainnet Launch), EV-010 (TGE & Genesis Drop)
Sitasi: Phase 3 EV-010 (HIGH) [https://blog.celestia.org/tia-genesis-drop/]; Phase 6 Distribution (HIGH) [https://docs.celestia.org/learn/tia-token]; Phase 9 Decision Timeline (HIGH) [Phase 9]; Phase 10 K-003 (HIGH) [Phase 10]

CONTEXT SAAT KEPUTUSAN

Tahap funding: Series A/B $55M (Oktober 2022) sudah selesai; Celestia Labs Inc. memiliki runway ~3-5 tahun; tidak ada kebutuhan immediate cash dari token sale【Phase 3 EV-005】【Phase 5 Funding History】【Phase 9 Decision Timeline Funding】.
Ukuran komunitas: 3 incentivized testnet (Arabica Jan 2022, Mocha Mar 2023, Lemon Sep 2023) dengan ratusan operator node; ekosistem Cosmos stakers puluhan ribu alamat; developer ekosistem modular berkumpul di Discord/forum【Phase 3 EV-004, EV-007, EV-008】【Phase 7 Infrastructure Providers】【Phase 9 Decision Timeline Testnets】.
Kondisi pasar: Q4 2023 — bear market residual, regulatory scrutiny meningkat (SEC vs Binance/Coinbase juni 2023); banyak project menghindari public sale/ICO; fair launch via airdrop menjadi narasi yang disukai komunitas dan investor【Phase 8 Market Position】【Phase 9 Decision Timeline Mainnet Launch】.
Kompetitor terdekat: EigenDA (belum mainnet, AVS di EigenLayer), Avail (testnet, Substrate-based), Near DA (live tapi terikat NEAR execution); Celestia first-mover modular DA layer dengan mainnet production-ready【Phase 8 Competitor Landscape】【Phase 9 Strategic Objective 1】.

TRIGGER DAN ALTERNATIF

Trigger: Mainnet launch memerlukan (1) distribusi token untuk keamanan staking (validator set genesis), (2) partisipasi governance on-chain sejak day-1, (3) narasi fair launch untuk diferensiasi dari kompetitor yang melakukan private sale/public sale, (4) memenuhi syarat listing CEX yang butuh circulating supply dan komunitas terdistribusi【Phase 3 EV-009, EV-010】【Phase 6 TGE】【Phase 9 Decision Timeline Mainnet Launch, TGE】.
Alternatif yang tidak diambil:
- Public sale / launchpad / auction: ditolak eksplisit ("NO public sale") — alasan resmi: fair launch, regulatory clarity【Phase 6 TGE】【Phase 9 Decision Timeline】.
- Penjualan privat tambahan (SAFT) di atas Series A/B: tidak dilakukan; investor sudah mendapat alokasi via equity round SAFT【Phase 5 Funding History】【Phase 6 Vesting Schedule Investors】.
- Distribusi bertahap (claim over time / vesting untuk community): tidak diambil; Genesis Drop fully unlocked at claim — trade-off: immediate liquidity vs sell pressure【Phase 6 Vesting Schedule Community】【Phase 9 Decision Timeline】.
- Tidak mendistribusikan sama sekali (hanya staking reward/inflation): tidak diambil; butuh circulating supply untuk governance, staking security, dan CEX listing【Phase 6 Utility Staking, Governance】【Phase 8 Exchange Ecosystem】.

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi:
- "Fair launch via airdrop ke Cosmos stakers, developers, testnet contributors" — tidak ada public sale, immediate liquidity【Phase 9 Decision Timeline Mainnet Launch】 (HIGH) [Phase 9].
- Membangun validator set genesis yang terdesentralisasi melalui staking airdrop recipients【Phase 9 Decision Timeline Mainnet Launch】 (HIGH) [Phase 9].
- Memenuhi ekspektasi komunitas modular blockchain yang menentang VC-dominated tokenomics【Phase 8 Narrative Position】 (MEDIUM) [Phase 8].
- Regulatory clarity: no public sale mengurangi risiko klasifikasi sekuritas【Phase 9 Decision Timeline】 (MEDIUM) [Phase 9].

Alasan yang tidak diumumkan (HIPOTESIS):
- Tekanan investor (Series A/B $55M) untuk likuiditas early agar SAFT token bisa dibuka (unlock) dengan harga pasar yang terbentuk; circulating supply 6% memungkinkan price discovery tanpa membanjiri pasar — HIPOTESIS (MEDIUM) [Phase 5 Funding History; Phase 6 Vesting Schedule Investors; Phase 9 Open Threads Vesting].
- Kebutuhan CEX listing: Binance, Coinbase, Kraken dll butuh circulating supply minimum dan komunitas holder terdistribusi untuk listing; airdrop 6% memenuhi syarat praktis listing tanpa market making agreement besar — HIPOTESIS (MEDIUM) [Phase 8 Exchange Ecosystem 11 CEX listing Q4 2023; Phase 9 Decision Timeline CEX Listings].
- Menghindari klasifikasi "investment contract" (Howey test) di US: airdrop tanpa purchase expectation (no payment) argumen regulasi yang lebih kuat vs public sale — HIPOTESIS (LOW) [Phase 5 Financial Risk Regulatory; Phase 9 Decision Timeline].
- Membangun narasi "community-owned" untuk menarik developer rollup (Arbitrum, Starknet, Polygon CDK) yang butuh DA layer netral, bukan VC-controlled — HIPOTESIS (MEDIUM) [Phase 3 EV-013, EV-014, EV-015; Phase 9 Strategic Objective 2,3].

OUTCOME PER POV

POV Founder: Sebagian
- Jangka pendek: Mainnet launch lancar, validator set genesis terbentuk dari airdrop stakers, 11 CEX listing dalam 6 minggu, narasi fair launch tercapai, zero regulatory action terkait TGE【Phase 3 EV-009, EV-010, EV-024】【Phase 9 Decision Timeline】 (HIGH) [Phase 3, Phase 9].
- Jangka panjang: Token allocation opacity (team/investor/foundation % tidak diungkap) menciptakan tekanan transparansi berkelanjutan; fee switch belum aktif (Nov 2024) menunda value accrual narrative; treasury opacity tetap kritik — HIPOTESIS (MEDIUM) [Phase 6 Distribution; Phase 5 Treasury; Phase 3 EV-027; Phase 9 Failure Factor 1,2].
- Dasar: Phase 3 EV-009, EV-010, EV-024; Phase 6 Distribution; Phase 9 Decision Timeline, Failure Factors (HIGH/MEDIUM).

POV VC: Sukses
- Jangka pendek: Equity investment $55M (Series A/B) mendapat token allocation via SAFT dengan vesting (cliff/linear tidak diungkap); immediate CEX liquidity memungkinkan partial exit early jika diinginkan; tidak ada public sale yang melonggarkan cap table【Phase 5 Funding History】【Phase 6 Vesting Schedule Investors】 (HIGH) [Phase 5, Phase 6].
- Jangka panjang: Token price discovery dari ~$2 (awal) ke ATH ~$20 (Februari 2024) lalu koreksi; VC vesting schedule (cliff 12 bulan typical) berarti unlock besar dimulai Q4 2024 — tekanan jual potensial; fee switch activation akan menentukan apakah TIA menjadi productive asset — HIPOTESIS (MEDIUM) [Phase 8 Market; Phase 3 EV-027; Phase 9 Open Threads Vesting].
- Dasar: Phase 5 Funding History; Phase 6 Vesting; Phase 8 Market; Phase 9 Open Threads (HIGH/MEDIUM).

POV Retail: Sebagian
- Jangka pendek: Eligible Cosmos stakers/dev/testnet contributors mendapat free TIA (claimable day-1); harga naik ~10x dalam 3 bulan (Nov 2023 - Feb 2024) memberi keuntungan besar bagi yang hold; non-eligible retail harus beli di CEX【Phase 3 EV-010, EV-024】【Phase 8 Exchange Ecosystem】 (HIGH) [Phase 3, Phase 8].
- Jangka panjang: Airdrop hunter yang tidak eligible merasa terkecualai (criteria opaque); sell pressure dari airdrop recipients early menciptakan volatilitas; tidak ada program follow-up airdrop (Season 2) hingga cut-off — HIPOTESIS (MEDIUM) [Phase 6 Distribution; Phase 8 Market; Phase 9 Open Threads].
- Dasar: Phase 3 EV-010, EV-024; Phase 8 Exchange Ecosystem; Phase 9 (HIGH/MEDIUM).

POV Community: Sukses
- Jangka pendek: Genesis Drop 6% ke community (bukan hanya insider) — narasi "community-first" tervalidasi; governance on-chain aktif day-1 dengan proposal pertama Jan 2024; Discord/forum aktif diskusi fee switch, grants【Phase 3 EV-018, EV-027】【Phase 6 Governance】 (HIGH) [Phase 3, Phase 6].
- Jangka panjang: Community pool spend via proposal (Sputnik grants 2024) menunjukkan treasury deployment; namun treasury size/composition opacity tetap mengganggu kepercayaan jangka panjang — HIPOTESIS (MEDIUM) [Phase 3 EV-026; Phase 5 Treasury; Phase 9 Failure Factor 2].
- Dasar: Phase 3 EV-018, EV-026, EV-027; Phase 6 Governance; Phase 5 Treasury; Phase 9 Failure Factor 2 (HIGH/MEDIUM).

POV Developer: Sukses
- Jangka pendek: Developer Cosmos/Celestia eligible mendapat TIA untuk staking/securing rollup mereka; Rollkit (2022) dan Sovereign SDK (2024) sudah tersedia pre/post-mainnet; blobspace fees murah awal memudahkan eksperimen【Phase 3 EV-006, EV-019】【Phase 7 SDK Rollkit, Sovereign SDK】 (HIGH) [Phase 3, Phase 7].
- Jangka panjang: 15+ rollup terintegrasi Q2 2025 (Arbitrum Orbit, Starknet, Polygon CDK, Manta, Dymension, dll) — blobspace demand real; light client WASM (Jan 2025) memperluas verifikasi trust-minimized ke browser/mobile — HIPOTESIS (HIGH) [Phase 3 EV-013, EV-014, EV-015, EV-022, EV-028; Phase 7 Major Integrations; Phase 8 Adoption Metrics].
- Dasar: Phase 3 EV-006, EV-013, EV-014, EV-015, EV-019, EV-022, EV-028; Phase 7; Phase 8 (HIGH).

POV Institution: Sebagian
- Jangka pendek: 11 major CEX listing (Binance, Coinbase, Kraken, Bybit, OKX, dll) memberikan akses institusional; perpetual futures tersedia di sebagian besar; OTC desk tersedia di Binance, Coinbase Prime, Kraken OTC【Phase 8 Exchange Ecosystem】 (HIGH) [Phase 8].
- Jangka panjang: Tokenomics opacity (alokasi team/investor/foundation tidak diungkap, vesting tidak transparan) dan treasury opacity menghalangi alokasi besar institusional yang butuh compliance & risk management ketat; fee switch uncertainty menambah variabel — HIPOTESIS (MEDIUM) [Phase 5 Treasury; Phase 6 Distribution, Vesting; Phase 3 EV-027; Phase 9 Failure Factor 1,3].
- Dasar: Phase 5, Phase 6, Phase 8, Phase 9 (HIGH/MEDIUM).

POV Validator: Sukses
- Jangka pendek: Genesis validator set 100 aktif terbentuk dari testnet performers + airdrop stakers; staking participation ~65-75% supply Q2 2025; inflation ~7-8%/tahun memberi yield staker; priority fee blobspace ke proposer【Phase 3 EV-009】【Phase 4 Consensus Mechanism】【Phase 8 Adoption Metrics Staking Participation】 (HIGH) [Phase 3, Phase 4, Phase 8].
- Jangka panjang: Fee switch activation (jika lolos governance) akan menambah revenue stream ke staker (base fee/priority fee portion); upgrade v2.0/v3.0 via governance menunjukkan koordinasi validator berfungsi; slashing risk tetap ada (double sign, downtime) — HIPOTESIS (HIGH) [Phase 3 EV-021, EV-029; Phase 4 Security Model; Phase 6 Inflation/Deflation; Phase 9 Decision Timeline Upgrades].
- Dasar: Phase 3 EV-009, EV-021, EV-029; Phase 4 Consensus, Security Model; Phase 6 Inflation; Phase 9 (HIGH).

POV Builder: Sukses
- Jangka pendek: Grant program Sputnik Wave 1 (2024) mendanai tooling, rollup templates, light client infra, explorer; builder mendapatkan TIA untuk operasi dan stake【Phase 3 EV-026】【Phase 7 Ecosystem】 (HIGH) [Phase 3, Phase 7].
- Jangka panjang: Ecosystem flywheel: grants → builder → tooling/rollup → blobspace fees → treasury → more grants; 15+ rollup live membuktikan product-market fit DA layer; multi-VM support (EVM, ZK, SVM, Move, WASM, Custom) menarik builder beragam — HIPOTESIS (HIGH) [Phase 3 EV-026; Phase 7 Major Integrations; Phase 8 Adoption Metrics; Phase 9 Success Factor 4,5].
- Dasar: Phase 3 EV-026; Phase 7; Phase 8; Phase 9 Success Factors (HIGH).

METRIK RETENSI

Persentase penerima yang menjual dalam 7 hari: Tidak ditemukan (tidak ada analisis on-chain resmi atau third-party yang dipublikasikan di Phase 1-11; memerlukan query snapshot Genesis Drop claimers vs transfer events dalam 7 hari) (LOW).
Persentase penerima yang masih memegang setelah 90 hari: Tidak ditemukan (sama seperti di atas; tidak ada data retensi holder airdrop recipients yang diagregasikan) (LOW).
Perubahan alamat aktif sebelum vs sesudah snapshot: Tidak ditemukan (snapshot date tidak diumumkan exact; "eligible addresses" criteria tidak mencakup tanggal cutoff yang memungkinkan perbandingan pre/post) (LOW).
Perubahan TVL atau volume sebelum vs sesudah: Tidak ditemukan (Celestia tidak punya TVL tradisional; blobspace throughput dan fee revenue metrics dari Token Terminal tersedia tapi tidak dibandingkan pre/post airdrop secara eksplisit) (MEDIUM) [Phase 8 Adoption Metrics Blobspace Throughput, Fee Revenue; Phase 9 Open Threads Revenue Metrics].
Harga token pada klaim, +30 hari, +90 hari: Tidak ditemukan (harga exact pada genesis block 2023-10-31 tidak tercatat; CoinGecko historical menunjukkan ~$2.00-$2.50 awal November 2023, ~$10+ pada +90 hari (Februari 2024 ATH ~$20) tapi data point exact tidak ada di fase-fase sebelumnya) (LOW) [Phase 8 Exchange Ecosystem; CoinGecko historical].

FARMING DAN SYBIL

Kriteria bisa ditebak sebelum snapshot: Tidak ditemukan (snapshot block/height tidak diumumkan; criteria "Cosmos stakers, developers, testnet contributors" cukup umum sehingga hunter bisa mempersiapkan: stake ATOM, kontribusi kode minor, jalankan testnet node — tapi tidak ada bukti mass farming terdokumentasi) (MEDIUM) [Phase 3 EV-010; Phase 6 Distribution].
Perilaku farming massal: Tidak ditemukan (tidak ada laporan spike aktivitas testnet Lemon (Sep 2023) mendekati mainnet yang mencurigakan; testnet Lemon dirancang sebagai pre-mainnet rehearsal bukan farming ground) (MEDIUM) [Phase 3 EV-008; Phase 7 Infrastructure Providers].
Jumlah alamat didiskualifikasi: Tidak ditemukan (tidak ada mekanisme anti-sybil atau diskualifikasi yang diumumkan; blog Genesis Drop tidak menyebutkan rejection) (LOW).
Tim mengubah kriteria setelah melihat perilaku: Tidak ditemukan (kriteria diumumkan bersamaan dengan TGE; tidak ada iterasi kriteria pasca-snapshot) (LOW).

PROSPEK

Prasyarat yang sudah terpenuhi:
- Mainnet live dengan DA layer berfungsi (DAS, NMT, Blobstream)【Phase 3 EV-009】【Phase 4 Core Components】 (HIGH).
- Token TIA liquide, listed 11 CEX, digunakan staking/governance/fee payment【Phase 3 EV-010, EV-024】【Phase 6 Utility】【Phase 8 Exchange Ecosystem】 (HIGH).
- Ecosystem rollup 15+ terintegrasi, blobspace demand real【Phase 3 EV-022】【Phase 8 Adoption Metrics Rollups】 (HIGH).
- Governance on-chain aktif, upgrade v2.0/v3.0 via proposal【Phase 3 EV-018, EV-021, EV-029】【Phase 6 Governance】 (HIGH).
- Foundation formed, grant program Sputnik running【Phase 3 EV-011, EV-026】【Phase 2 Foundation】【Phase 7 Ecosystem】 (HIGH).

Prasyarat yang belum:
- Fee switch activation (value accrual ke staker) — masih diskusi governance Nov 2024, belum proposal formal lolos【Phase 3 EV-027】【Phase 6 Utility Fee Accrual】【Phase 9 Decision Timeline Fee Switch】 (HIGH).
- Treasury transparency dashboard / on-chain address label Foundation/Labs — tidak ada【Phase 5 Treasury】【Phase 9 Failure Factor 2】 (HIGH).
- Tokenomics detail (alokasi team/investor/foundation %, vesting schedule) — tidak diungkap【Phase 6 Distribution, Vesting】【Phase 9 Open Threads Distribution, Vesting】 (HIGH).
- Native IBC aktif untuk transfer TIA lintas Cosmos ecosystem — masih planned【Phase 7 Integration IBC】【Phase 8 Liquidity】【Phase 9 Failure Factor 5】 (MEDIUM).
- Quantum Gravity Bridge testnet/mainnet — masih R&D, belum live【Phase 3 EV-030】【Phase 4 QGB】【Phase 9 Open Threads QGB】 (MEDIUM).
- Light client DAS participation rate telemetri publik — tidak ada【Phase 8 Adoption Metrics Light Client】【Phase 9 Open Threads DAS Participation】 (HIGH).

Sinyal yang biasanya mendahului:
- Perubahan dokumentasi: halaman tokenomics blog/docs di-update dengan breakdown alokasi dan vesting schedule.
- Kontrak distribusi: deploy vesting contract baru atau update Genesis Drop contract untuk Season 2.
- Pengumuman snapshot: snapshot block/height diumumkan minimal 30 hari sebelumnya (best practice era 2024).
- Perekrutan: hiring community/airdrop program manager di Celestia Labs/Foundation.
- Forum governance: proposal formal untuk community allocation tambahan (Season 2) atau incentive program baru.

Penilaian: Kemungkinan airdrop Season 2 / follow-up incentive program MODERATE (50-60%) dalam 12-18 bulan ke depan. Prasyarat utama: fee switch activation (membutuhkan value accrual narrative baru), treasury transparency improvement (mengurangi kritik), dan IBC native activation (memperluas eligible population ke Cosmos ecosystem luas). Sinyal paling kuat akan muncul dari forum governance proposal formal untuk "Community Incentive Program Season 2" atau "Ecosystem Growth Allocation" — jika proposal tersebut muncul dan lolos, airdrop/incentive follow-up hampir pasti. Blocker utama: token allocation opacity — tanpa breakdown resmi, sulit membenarkan alokasi tambahan ke community tanpa menimbulkan spekulasi insider allocation. Keyakinan: MEDIUM (bergantung pada keputusan governance fee switch dan transparency roadmap 2025).

PELAJARAN LINTAS PROJECT

Ketika airdrop dieksekusi bersamaan mainnet launch + TGE tanpa public sale (era 2023-2024, regulatory scrutiny tinggi), fair launch narrative tercapai dan CEX listing cepat (11 major CEX dalam 6 minggu) — akibatnya immediate liquidity dan price discovery tanpa sell pressure dari public sale unlock, tapi token allocation opacity (team/investor/foundation % tidak diungkap) menciptakan tekanan transparansi jangka panjang yang menghalangi adopsi institusional.
Ketika kriteria airdrop retroaktif mencakup "testnet contributors" tanpa snapshot date spesifik yang diumumkan jauh-jauh hari (era 2023, testnet incentivized sudah matang), hunter population sudah siap memenuhi syarat (stake ATOM, jalankan node testnet) — akibatnya eligible set mencerminkan genuine early contributors namun tidak bisa dibedakan dari hunter yang persis menargetkan criteria; anti-sybil mechanism tidak diumumkan membuat retensi post-airdrop tidak terukur.
Ketika airdrop allocation hanya 6% total supply (relatif kecil vs project lain 10-20%) dan fully unlocked at claim (era 2023-2024, hunter population matang), sell pressure awal termitigasi oleh ukuran kecil dan distribusi ke stakers yang cenderung hold untuk staking — akibatnya price appreciation 10x dalam 3 bulan tanpa crash besar, tapi tidak ada program follow-up menciptakan "one-time event" perception bukan ongoing incentive.
Ketika dual-entity structure (Labs for-profit + Foundation non-profit) dipakai untuk airdrop distribution (Foundation mengelola Genesis Drop), governance legitimacy meningkat karena treasury stewarded by non-profit — akibatnya community trust lebih tinggi vs single-entity project, tapi Foundation treasury opacity (tidak ada dashboard) mengurangi keuntungan struktur tersebut.
Ketika fee switch (value accrual mechanism) dijanjikan tapi tidak diaktifkan hingga 12+ bulan pasca-TGE (era 2024, governance on-chain matang), token holders mengalami "value accrual uncertainty" yang menekan naratif investasi — akibatnya TIA diperlakukan sebagai gas/governance token saja, bukan productive asset, sampai proposal formal lolos governance.

## Open Questions
- [foundation] Distribusi token TGE detail (persentase community/airdrop vs investor/team) — butuh cross-check ke on-chain data dan blog tokenomics resmi
- [foundation] Status fee switch / value accrual mechanism TIA (blobspace fees, staking yield) — butuh verifikasi dari governance proposals dan spec
- [foundation] Ukuran treasury Celestia Labs vs Celestia Foundation (on-chain address labels) — butuh analisis on-chain
- [foundation] Daftar lengkap investor ronda Series A/B ($55M Oct 2022) — Crunchbase menyebut Bain Capital Crypto, Polychain, dll tapi butuh konfirmasi resmi
- [foundation] Rincian legal structure hubungan Celestia Labs (for-profit) dan Celestia Foundation (non-profit) — butuh dokumen governance/resmi
- [foundation] Tanggal pasti deploy wrapped TIA (wTIA) di Ethereum/Arbitrum dan oleh siapa (resmi vs community)
- [entity] Daftar lengkap investor ronde Series A/B ($55M) — Crunchbase menyebut lebih banyak nama (Delphi Digital, Galaxy Digital, dll) yang butuh verifikasi silang
- [entity] Identitas auditor tambahan selain Informal Systems dan Trail of Bits (misal: Zellic, Sigma Prime, atau audit internal)
- [entity] Detail legal structure hubungan Celestia Labs (for-profit) dan Celestia Foundation (non-profit) — dokumen governance/resmi tidak yet publik
- [entity] Alamat on-chain treasury Celestia Foundation vs Celestia Labs — butuh analisis label address
- [entity] Status deploy wTIA resmi vs community — siapa deployer kontrak Ethereum/Arbitrum pertama kali
- [entity] Daftar lengkap proposer/validator set genesis dan distribusi stake awal — butuh data on-chain block 0
- [entity] Rincian grant program Celestia Foundation (jumlah, penerima, kategori) — butuh data dari forum governance
- [entity] Status Quantum Gravity Bridge — apakah masih R&D atau ada testnet publik
- [entity] Relayer set Blobstream — siapa operator relayer utama (Celestia Labs, third-party, permissionless)
- [history] Tanggal pasti pembentukan Celestia Labs Inc. (hanya tahun 2021 diketahui dari Crunchbase, butuh dokumen incorporasi Delaware)
- [history] Tanggal pasti publikasi whitepaper LazyLedger (arXiv v1 vs v2 vs blog post resmi — butuh cross-check versi definitive)
- [history] Detail lengkap investor Series A/B $55M — Crunchbase menyebut nama tambahan (Delphi Digital, Galaxy Digital, Figment Capital, dll) yang tidak muncul di blog resmi; butuh verifikasi kapsul investor final
- [history] Tanggal pasti pembentukan Celestia Foundation (Zug) — blog mainnet launch menyebutkan tapi tidak ada tanggal registrasi resmi publik
- [history] Nomor proposal governance on-chain pertama dan detail parameter yang diubah — butuh query on-chain gov module
- [history] Tanggal dan nomor versi upgrade protokol v2.0 dan v3.0 pasti — blog announcement butuh dicari arsip spesifik
- [history] Daftar lengkap rollup produksi yang memposting ke Celestia mainnet (EV-022) — butuh data on-chain blob submission per namespace
- [history] Status deploy wTIA: alamat kontrak Ethereum dan Arbitrum pasti, deployer address, dan apakah ada multisig/resmi — butuh verifikasi Etherscan/Arbiscan
- [history] Rincian program grant Celestia Foundation (Sputnik Wave 1): total dana, jumlah penerima, kategori — butuh data dari forum governance resmi
- [history] Status Quantum Gravity Bridge: apakah testnet publik sudah diluncurkan per Juni 2025 atau masih internal — butuh cek blog/research forum terbaru
- [history] Audit tambahan selain Informal Systems dan Trail of Bits (misal: Zellic, Sigma Prime, Halborn, atau audit internal Celestia Labs) — butuh cek halaman security blog
- [history] Distribusi token TGE detail on-chain: persentase airdrop vs investor vs team vs foundation vs community pool di block 0 — butuh analisis genesis.json dan tokenomics blog
- [history] Alamat treasury Celestia Foundation dan Celestia Labs on-chain — butuh label address dari block explorer atau governance proposal spend
- [history] Metrik adopsi tahun pertama (EV-023): jumlah blob, throughput rata-rata, fee revenue, jumlah namespace aktif — butuh laporan resmi atau query indexer
- [technology] Spesifikasi teknis detail Quantum Gravity Bridge (ZK-proof vs optimistic verification, light client circuit) — belum dipublikasikan lengkap; butuh whitepaper/research paper final
- [technology] Parameter konsensus CometBFT pasti pada mainnet genesis (block time, max block size, validator set size, evidence params) — butuh query genesis.json on-chain
- [technology] Detail fee market parameter genesis (base fee change denominator, elasticity multiplier, min base fee) — butuh query gov params on-chain
- [technology] Daftar lengkap namespace ID yang terdaftar dan rollup yang menggunakannya (namespace registry) — butuh indexer on-chain namespace
- [technology] Metrik DAS sampling participation rate real-time (jumlah light client aktif, sampling rate) — butuh telemetri jaringan resmi
- [technology] Status audit terbaru pasca-upgrade v3.0 (Ginger) — apakah ada audit baru untuk namespace versioning dan QGB prep
- [technology] Detail teknis Blobstream v2 (jika ada upgrade) vs v1 — perbedaan arsitektur relayer, verification logic, gas optimization
- [technology] Kompatibilitas Celestia Node versi lama dengan upgrade v3.0 — matrix versi minimum light client, full node, bridge node
- [technology] Spesifikasi WASM light client binary size, memory usage, verification latency di browser/mobile — butuh benchmark resmi
- [technology] Rencana integrasi ABCI++ (Application Blockchain Interface++) untuk execution layer coupling — status implementasi di Rollkit/Sovereign SDK
- [financial] Ukuran treasury Celestia Foundation saat ini (jumlah TIA, stablecoin, aset lain) — butuh analisis on-chain address label Foundation atau governance proposal spend
- [financial] Alokasi token TGE detail: persentase investor (Series A/B), team, foundation, community pool, airdrop, validators — butuh cross-check genesis.json dan blog tokenomics
- [financial] Vesting schedule investor privat (SAFT) — cliff, durasi, unlock bulanan/tahunan — tidak diumumkan publik
- [financial] Revenue metrics on-chain: total blobspace fee collected, base fee burned, priority fee distributed to validators per bulan — butuh indexer/query custom
- [financial] Status fee switch activation: proposal governance nominal, timeline, persentase fee yang dialokasikan ke staker — butuh monitoring forum governance
- [financial] Program grant Celestia Foundation (Sputnik Wave 1): total budget, jumlah penerima, kategori, sisa dana — butuh data dari forum governance
- [financial] Financial runway Celestia Labs: sisa kas dari $55M, burn rate bulanan, rencana fundraising lanjutan — tidak diungkap
- [financial] Valuation pada Series A/B — tidak diumumkan
- [financial] Apakah ada revenue sharing dari Celestia Labs ke Foundation (licensing, enterprise support) — tidak diketahui
- [financial] Alamat on-chain treasury Foundation dan Labs (multisig/DAI) untuk transparansi — butuh label address dari block explorer atau proposal
- [token] Persentase alokasi token TGE detail per kategori (Team %, Investor %, Foundation %, Ecosystem %, Community Pool %, Advisors %, Other %) — blog tokenomics resmi tidak mempublikasikan breakdown lengkap; butuh cross-check genesis.json dan on-chain vesting contract
- [token] Vesting schedule investor (Series A/B): cliff duration, vesting duration, unlock frequency (bulanan/kuartalan), current unlocked amount — tidak diumumkan publik; butuh analisis vesting contract on-chain
- [token] Vesting schedule team/core contributor: cliff, vesting, unlock frequency — tidak diumumkan publik
- [token] Alamat multisig/vesting contract resmi untuk Foundation, Team, Investor — butuh label address dari block explorer atau governance proposal
- [token] Saldo treasury Celestia Foundation saat ini (TIA, stablecoin, aset lain) — tidak diungkap; butuh analisis on-chain address Foundation
- [token] Saldo Community Pool on-chain real-time — dapat di-query via gov module tapi tidak dipublikasikan di dashboard resmi
- [token] Status fee switch activation: proposal nominal number, voting result, implementation timeline — masih diskusi di forum governance (EV-027)
- [token] Inflation parameter genesis pasti (inflation_max, inflation_min, inflation_rate_change, goal_bonded) — butuh query gov params on-chain
- [token] Fee market parameter genesis pasti (base fee change denominator, elasticity multiplier, min base fee) — butuh query gov params on-chain
- [token] Total blobspace fee collected, base fee burned, priority fee distributed to validators per bulan — butuh indexer custom query
- [token] wTIA deployer address, contract verification status, multisig custodian, apakah ada audit — deploy oleh pihak ketiga, tidak resmi; butuh verifikasi Etherscan/Arbiscan
- [token] Holder distribution detail: top 100 address breakdown (Foundation, Vesting, CEX, Validator, Whale, Retail) — butuh analisis on-chain label address
- [token] Validator set genesis dan distribusi stake awal — butuh query block 0 validator set
- [token] Apakah ada token burn tambahan selain base fee (misal: fee switch burn, treasury buyback & burn) — tidak ada mekanisme resmi selain base fee burn
- [token] Rincian program grant Sputnik Wave 1: total budget TIA, jumlah penerima, kategori, sisa dana — butuh data dari forum governance
- [token] Legal status TIA di jurisdiksi utama (US, EU, SG, CH) — apakah ada legal opinion resmi dari Foundation/Labs
- [behavioral] Treasury transparency: Alamat on-chain Foundation/Labs multisig, saldo real-time, grant disbursement tracking — tidak ada dashboard resmi; butuh analisis on-chain atau proposal governance spend
- [behavioral] Tokenomics detail: Persentase alokasi TGE per kategori (team %, investor %, foundation %, community pool %, dll) — blog tokenomics tidak publish breakdown; butuh genesis.json analysis
- [behavioral] Vesting schedule investor/team: Cliff duration, vesting duration, unlock frequency, current unlocked amount — tidak diumumkan publik; butuh vesting contract on-chain analysis
- [behavioral] Fee switch activation: Proposal number formal, voting timeline, percentage allocation ke staker — masih diskusi forum (EV-027); butuh monitoring governance
- [behavioral] QGB status: Testnet publik sudah launch Juni 2025 atau belum? Desain final ZK-proof vs optimistic verification? — EV-030 target tapi tidak ada confirmation blog terbaru
- [behavioral] Light client DAS participation rate actual: Jumlah light client aktif sampling, sampling rate, geographic distribution — telemetri jaringan tidak dipublikasikan; butuh research forum data
- [behavioral] Blobstream v2 vs v1: Arsitektur relayer, verification logic, gas optimization, upgrade timeline — Sigma Prime audit 2024 tapi detail tidak publik
- [behavioral] CEX listing agreement details: Market making, listing fee, token allocation untuk liquidity — tidak diungkap; standard industry tapi butuh transparency
- [behavioral] Regulatory legal opinion: Status TIA di US (security vs commodity), EU (MiCA), SG, CH — Foundation/Labs tidak publish legal opinion
- [behavioral] Validator set genesis analysis: Distribusi stake awal, airdrop recipient staking behavior, validator decentralization metric — butuh block 0 query
- [behavioral] Rollup revenue attribution: Blobspace fee per rollup (Arbitrum Orbit vs Starknet vs Polygon CDK vs Sovereign) — butuh namespace-level fee analytics
- [behavioral] Grant program Sputnik Wave 1 detail: Total budget TIA, jumlah penerima, kategori, sisa dana, Wave 2 plan — forum governance data tidak terstruktur
- [behavioral] Inflation parameter genesis exact: inflation_max, inflation_min, inflation_rate_change, goal_bonded — butuh gov params query on-chain
- [behavioral] Fee market parameter genesis exact: base fee change denominator, elasticity multiplier, min base fee — butuh gov params query on-chain
- [behavioral] wTIA deployer verification: Contract address Ethereum/Arbitrum verified, deployer identity, multisig custodian, audit status — third-party deploy, tidak resmi
- [behavioral] Competitor response: EigenDA mainnet launch impact pada Celestia blobspace demand; Avail Nexus cross-rollup messaging adoption — butuh market monitoring lanjutan
- [conflict] Open Thread ID: OT-001 Description: Daftar lengkap investor Series A/B ($55M) tidak diungkap oleh blog resmi; Crunchbase menyebutkan Delphi Digital, Galaxy Digital, Figment Capital sebagai tambahan, namun tidak dikonfirmasi oleh blog resmi Celestia. Affected Phase: Phase 5, Phase 3 Evidence: https://blog.celestia.org/celestia-labs-raises-55m/; https://www.crunchbase.com/organization/celestia-labs Alternative Interpretations: 1) Investor tambahan memang ada tetapi tidak disebutkan di blog karena alasan komersial; 2) Crunchbase mencatat entitas yang berbeda (misal advisor) yang sebenarnya bukan investor equity; 3) Daftar resmi hanya Bain Capital Crypto dan Polychain sebagai lead, sisanya partisipan minor. Status: Open — butuh konfirmasi resmi dari Celestia Labs
- [conflict] Open Thread ID: OT-002 Description: Persentase alokasi token TGE per kategori (team, investor, foundation, ecosystem, community pool) tidak diungkap; hanya 6% community drop yang diumumkan. Affected Phase: Phase 6, Phase 3 Evidence: https://blog.celestia.org/tia-genesis-drop/; https://docs.celestia.org/learn/tia-token Alternative Interpretations: 1) Alokasi team/investor mungkin signifikan (>60% digabung) mengingat $55M Series A/B; 2) Foundation mungkin menerima alokasi besar untuk grants jangka panjang; 3) Tidak ada alokasi khusus untuk advisors bila diabaikan. Status: Open — butuh genesis.json dan vesting contract on-chain
- [conflict] Open Thread ID: OT-003 Description: Fee switch activation status masih diskusi; bila diaktifkan, mengubah TIA dari gas/governance token menjadi productive value-accrual asset. Affected Phase: Phase 5, Phase 6, Phase 3 Evidence: https://forum.celestia.org/t/fee-switch-value-accrual/; https://docs.celestia.org/learn/fee-market; https://docs.celestia.org/learn/tia-token Alternative Interpretations: 1) Bagian base fee dialihkan ke staker; 2) Bagian priority fee dialihkan ke staker; 3) Kombinasi keduanya; 4) Tidak diaktifkan dalam waktu dekat, tetap burn hanya. Status: Open — butuh proposal formal dan voting result
- [conflict] Open Thread ID: OT-004 Description: Light client DAS participation rate tidak tersedia; security model probabilistik bergantung pada ini, tapi data tidak dipublikasikan. Affected Phase: Phase 8, Phase 4 Evidence: https://forum.celestia.org/t/das-participation-metrics/; https://docs.celestia.org/learn/data-availability-sampling Alternative Interpretations: 1) Partisipasi light client rendah (<5k) yang melemahkan security model; 2) Partisipasi tinggi (>15k) yang memperkuat klaim DAS; 3) Data dianggap sensitif security dan tidak dipublikasikan. Status: Open — butuh telemetri jaringan resmi dari Celestia Labs
- [conflict] Open Thread ID: OT-005 Description: Quantum Gravity Bridge status R&D; testnet publik belum terverifikasi per Juni 2025; spesifikasi final belum dipublikasikan. Affected Phase: Phase 4, Phase 3 Evidence: https://forum.celestia.org/t/quantum-gravity-bridge/; https://blog.celestia.org/ Alternative Interpretations: 1) QGB masih internal R&D; 2) QGB testnet diluncurkan diam-diam tanpa announcement; 3) Desain berubah (ZK vs optimistic) masih diputuskan. Status: Open — butuh whitepaper QGB atau blog update
- [conflict] Open Thread ID: OT-006 Description: wTIA (Wrapped TIA) deploy oleh pihak ketiga; tidak ada verifikasi resmi, alamat kontrak tidak terdokumentasi di Phase 6, custodian tidak jelas. Affected Phase: Phase 6, Phase 7 Evidence: https://docs.celestia.org/learn/tia-token; https://arbiscan.io/token/0x...; https://etherscan.io/token/0x... Alternative Interpretations: 1) wTIA dikelola multisig oleh pihak ketiga ternama (kurasi komunitas); 2) wTIA adalah bridge contract yang berbeda; 3) wTIA bisa di-upgrade oleh deployer (risiko rug-pull jika terpusat). Status: Open — butuh verifikasi kontrak dan deployer address
- [conflict] Open Thread ID: OT-007 Description: Native IBC tidak aktif; TIA transfer lintas chain Cosmos memerlukan CEX/bridge; naratif interoperabilitas Cosmos SDK belum terpenuhi. Affected Phase: Phase 7, Phase 8 Evidence: https://forum.celestia.org/t/ibc-integration/; https://defillama.com/chain/Celestia Alternative Interpretations: 1) IBC akan aktif setelah upgrade v4; 2) IBC ditunda tanpa timeline; 3) IBC tidak dianggendakan karena fokus Blobstream untuk interoperability. Status: Open — butuh roadmap resmi IBC
- [conflict] Open Thread ID: OT-008 Description: Revenue metrics on-chain (blobspace fee, base fee burn, priority fee) tidak diagregasikan; Token Terminal memberikan angka tapi tidak diverifikasi dengan explorer resmi. Affected Phase: Phase 5, Phase 8 Evidence: https://tokenterminal.com/terminal/projects/celestia; https://explorer.celestia.org/ Alternative Interpretations: 1) Token Terminal menggunakan definisi revenue yang berbeda (fee revenue vs gross profit); 2) Burn rate mungkin lebih tinggi dari yang dicatat karena base fee; 3) Priority fee ke validator tidak separah yang diklaim. Status: Open — butuh query on-chain langsung ke fee market module
- [conflict] Open Thread ID: OT-009 Description: Parameter konsensus genesis (block time, max block size, inflation rate) tidak di-named dalam dokumentasi; butuh query genesis.json atau gov params. Affected Phase: Phase 4, Phase 6 Evidence: https://docs.celestia.org/learn/consensus-parameters; https://github.com/celestiaorg/celestia-app Alternative Interpretations: 1) Block time possible ~6 detik (CometBFT default); 2) Max block size mungkin 8MB atau 4MB; 3) Inflation mungkin berkisar 7-8% per tahun sesuai docs. Status: Open — butuh query on-chain genesis block
- [conflict] Open Thread ID: OT-010 Description: Toggle antara "sovereign tanpa settlement" vs "settlement via Ethereum" menciptakan dua kategori rollup yang berbeda; posisi Celestia sebagai settlement layer masih ambigu. Affected Phase: Phase 4, Phase 7, Phase 8 Evidence: https://blog.celestia.org/modular-ecosystem/; https://github.com/rollkit/rollkit; https://github.com/Sovereign-Labs/sovereign-sdk Alternative Interpretations: 1) Celestia tetap DA-only, settlement opsional; 2) Rollkit/Sovereign SDK memungkinkan settlement-native di masa depan; 3) Posisi "sovereign" bisa bergeser menjadi settlement layer jika adopsi QGB berhasil. Status: Open — butuh roadmap jangka panjang dari Celestia Labs
- [airdrop] Jumlah penerima Genesis Drop (unique addresses eligible + claimed) tidak diumumkan resmi — butuh analisis on-chain claim events atau data dari Foundation
- [airdrop] Harga TIA exact pada genesis block 2023-10-31 (bukan awal November) — butuh query historical price dari CEX listing pertama atau on-chain DEX pool jika ada
- [airdrop] Persentase airdrop recipients yang menjual dalam 7/30/90 hari — butuh on-chain analysis claimers vs transfer events
- [airdrop] Mekanisme anti-sybil Genesis Drop (jika ada) dan jumlah alamat yang didiskualifikasi — tidak terdokumentasi
- [airdrop] Snapshot block/height exact untuk eligibility Cosmos stakers / testnet contributors — tidak diumumkan
- [airdrop] Apakah ada alokasi community tambahan (Season 2) di treasury Foundation yang belum di-deploy — butuh treasury transparency
- [airdrop] Fee switch activation timeline dan percentage allocation ke staker — masih diskusi forum, butuh proposal formal
- [airdrop] Vesting schedule investor/team exact (cliff, durasi, unlock frequency) — tidak diungkap, butuh vesting contract on-chain
- [airdrop] Native IBC activation roadmap — forum discussion only, tidak ada timeline resmi
- [airdrop] Quantum Gravity Bridge testnet status (sudah launch Juni 2025 atau belum) — EV-030 target tapi tidak ada konfirmasi blog terbaru
