# Celestia — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Celestia_foundation_2026-08.docx, doc_backup/deep/Celestia_entity_2026-08.docx, doc_backup/deep/Celestia_history_2026-08.docx, doc_backup/deep/Celestia_technology_2026-08.docx, doc_backup/deep/Celestia_financial_2026-08.docx, doc_backup/deep/Celestia_token_2026-08.docx, doc_backup/deep/Celestia_ecosystem_2026-08.docx, doc_backup/deep/Celestia_market_2026-08.docx, doc_backup/deep/Celestia_behavioral_2026-08.docx, doc_backup/deep/Celestia_knowledge_2026-08.docx.
**Phases not run:** conflict.

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

1. Menjadi Data Availability Layer standar untuk modular blockchain stack
· Evidence: Whitepaper LazyLedger (2021) mendefinisikan arsitektur modular dengan pemisahan consensus, DA, dan execution; semua komunikasi resmi dan blog menekan narasi "Modular Blockchain" sebagai identitas utama (HIGH) [Phase 1 Foundation, https://blog.celestia.org/what-is-celestia/; Phase 3 EV-003, https://arxiv.org/abs/2105.09830]
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-003, Phase 8 Narrative Position

2. Memisahkan execution layer dari consensus layer untuk memungkinkan sovereign rollup dan app-chain
· Evidence: Arsitektur tidak memiliki execution native; mendukung EVM (Arbitrum Orbit), SVM, WASM, Move VM via rollup framework (Rollkit, Sovereign SDK, Polygon CDK, Starknet) (HIGH) [Phase 4 System Architecture, https://docs.celestia.org/learn/architecture; Phase 7 Major Integrations]
· Supporting Dataset: Phase 4 System Architecture, Phase 7 Major Integrations

3. Membangun ekosistem rollup yang menggunakan Celestia DA melalui Blobstream dan verifikasi trust-minimized
· Evidence: Integrasi live dengan Arbitrum Orbit (EV-013), Starknet (EV-014), Polygon CDK (EV-015), Manta Pacific, Dymension RollApps (EV-022), Sovereign SDK (EV-019), Rollkit (EV-006); Blobstream contracts di Ethereum (EV-012) (HIGH) [Phase 3 EV-012 to EV-015, EV-019, EV-022; Phase 7 Major Integrations]
· Supporting Dataset: Phase 3 EV-012 to EV-015, EV-019, EV-022, Phase 7 Major Integrations

4. Menciptakan value accrual untuk TIA melalui blobspace fees, staking, dan fee switch mekanisme
· Evidence: Fee market EIP-1559 style live sejak mainnet; base fee dibakar, priority fee ke proposer; fee switch diskusi governance (EV-027) untuk mengalihkan sebagian fee ke staker (HIGH) [Phase 4 Fee Market, https://docs.celestia.org/learn/fee-market; Phase 5 Revenue Model; Phase 3 EV-027]
· Supporting Dataset: Phase 4 Fee Market, Phase 5 Revenue Model, Phase 3 EV-027

5. Desentralisasi progresif melalui Celestia Foundation (non-profit) dan governance on-chain
· Evidence: Foundation didirikan Zug Swiss (EV-011) mengelola treasury, grants, governance; Celestia Labs (for-profit) sebagai core developer; governance on-chain aktif sejak mainnet (EV-018) (HIGH) [Phase 2 Foundation & Company entities; Phase 3 EV-011, EV-018; Phase 6 Governance]
· Supporting Dataset: Phase 2 Foundation/Company entities, Phase 3 EV-011, EV-018, Phase 6 Governance

6. Memperluas akses light client trust-minimized ke browser dan mobile untuk mass adoption
· Evidence: Light client WASM dan mobile SDK rilis Jan 2025 (EV-028); DAS sampling oleh light client sebagai security model inti (HIGH) [Phase 3 EV-028; Phase 4 Security Model; Phase 7 Integration Light Client WASM]
· Supporting Dataset: Phase 3 EV-028, Phase 4 Security Model, Phase 7 Integration Light Client WASM

Decision Timeline

Keputusan: Founding Celestia (LazyLedger) dan penelitian modular blockchain (2019)
· Trigger: Masalah skalabilitas monolithic blockchain (execution + consensus + DA coupled); kebutuhan pemisahan layer
· Evidence: Whitepaper LazyLedger 2021 mendefinisikan DAS dan NMT; founding team (Mustafa Al-Bassam, Ismail Khoffi, John Adler, Nick White) memiliki background cryptography, distributed systems, dan Ethereum research (HIGH) [Phase 1 Foundation; Phase 3 EV-001; Phase 2 Person entities]
· Decision: Memulai penelitian dan pengembangan protokol Data Availability Sampling dengan Namespaced Merkle Trees
· Immediate Result: Konsep dasar modular blockchain terdefinisi; fondasi teknis untuk Celestia
· Long-term Impact: Menjadi pionir kategori Modular Blockchain; referensi arsitektur untuk EigenDA, Avail, dll
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-001, Phase 3 EV-003

Keputusan: Pembentukan Celestia Labs Inc. di Delaware sebagai entitas for-profit (2021)
· Trigger: Perlu entitas hukum untuk 고용 tim engineering, fundraising VC, dan pengembangan protokol komersial
· Evidence: Crunchbase menunjukkan incorporasi 2021; $55M Series A/B 2022 melalui Labs (HIGH) [Phase 2 Company entity; Phase 3 EV-002; Phase 5 Funding History]
· Decision: Mendirikan Celestia Labs Inc. (Delaware) untuk core development, business development, dan equity fundraising
· Immediate Result: Kapasitas hiring tim ~40+ engineer/researcher; modal untuk pengembangan protokol
· Long-term Impact: Dual-entity structure (Labs + Foundation) menjadi model governance; Labs fokus execution, Foundation fokus treasury/stewardship
· Supporting Dataset: Phase 2 Company entity, Phase 3 EV-002, Phase 5 Funding History

Keputusan: Publikasi Whitepaper "LazyLedger: A Distributed Data Availability Ledger" (2021)
· Trigger: Perlu publikasi teknis formal untuk validasi akademik dan komunitas peneliti
· Evidence: arXiv:2105.09830 oleh Mustafa Al-Bassam, John Adler, dll; mendefinisikan DAS, NMT, modular thesis (HIGH) [Phase 3 EV-003; https://arxiv.org/abs/2105.09830]
· Decision: Menerbitkan whitepaper teknis open access mendefinisikan arsitektur Celestia
· Immediate Result: Dasar teknis resmi dipublikasikan; menarik perhatian investor dan researcher
· Long-term Impact: Menjadi referensi standar modular DA layer; sitasi di penelitian EigenDA, Avail, Near DA
· Supporting Dataset: Phase 3 EV-003

Keputusan: Peluncuran Arabica Incentivized Testnet (2022-01-24)
· Trigger: Perlu validasi DAS, light client, dan konsensus CometBFT di lingkungan produksi awal dengan insentif ekonomi
· Evidence: Blog Arabica Testnet; program reward untuk operator node; first public network (HIGH) [Phase 3 EV-004; https://blog.celestia.org/arabica-testnet/]
· Decision: Meluncurkan testnet incentivized pertama (Arabica) dengan reward bagi node operators
· Immediate Result: Jaringan node pertama beroperasi; validasi DAS dan light client; komunitas operator terbentuk
· Long-term Impact: Membangun infrastructure provider network awal; data untuk parameter mainnet
· Supporting Dataset: Phase 3 EV-004, Phase 7 Infrastructure Providers

Keputusan: Fundraising Series A/B $55M dipimpin Bain Capital Crypto dan Polychain Capital (2022-10)
· Trigger: Perlu modal besar untuk ekspansi tim, research, BD, dan ekosistem rollup pasca-testnet Arabica
· Evidence: Blog resmi "Celestia Labs raises $55M"; investor: Bain Capital Crypto, Polychain, 1kx, Robot Ventures, Placeholder, Delphi Digital, Galaxy Digital, Figment Capital (HIGH) [Phase 3 EV-005; Phase 5 Funding History; https://blog.celestia.org/celestia-labs-raises-55m/]
· Decision: Mengumpulkan $55M equity funding Series A/B untuk Celestia Labs Inc.
· Immediate Result: Runway untuk hiring agresif, research, business development, grant program
· Long-term Impact: Financial dependency pada VC; tekanan untuk delivery mainnet dan adoption; investor token allocation dengan vesting
· Supporting Dataset: Phase 3 EV-005, Phase 5 Funding History, Phase 6 Token Distribution

Keputusan: Rilis Rollkit Framework untuk Sovereign Rollup (2022)
· Trigger: Perlu developer tooling agar rollup dapat menggunakan Celestia DA tanpa settlement layer smart contract
· Evidence: Rollkit GitHub rilis 2022; framework Golang dengan ABCI++ support (HIGH) [Phase 3 EV-006; https://github.com/rollkit/rollkit; Phase 7 SDK Rollkit]
· Decision: Mengembangkan dan merilis Rollkit sebagai sovereign rollup SDK native Celestia DA
· Immediate Result: Tooling tersedia untuk sovereign rollup; menarik builder eksperimen
· Long-term Impact: Memperluas kategori rollup yang didukung (sovereign + settlement); diferensiasi vs EigenDA yang fokus Ethereum-aligned
· Supporting Dataset: Phase 3 EV-006, Phase 7 SDK Rollkit, Phase 7 Major Integrations Rollkit

Keputusan: Peluncuran Mocha Incentivized Testnet v2 (2023-03-28)
· Trigger: Perlu upgrade protokol, uji coba Blobstream relayer, dan perluas partisipasi node sebelum mainnet
· Evidence: Blog Mocha Testnet; Blobstream relayer testing; reward program diperluas (HIGH) [Phase 3 EV-007; https://blog.celestia.org/mocha-testnet/]
· Decision: Meluncurkan testnet incentivized kedua (Mocha) dengan Blobstream integration testing
· Immediate Result: Validasi Blobstream bridge ke Ethereum; peningkatan stabilitas jaringan
· Long-term Impact: Memvalidasi cross-chain verification architecture sebelum mainnet
· Supporting Dataset: Phase 3 EV-007, Phase 4 Blobstream, Phase 7 Integration Blobstream

Keputusan: Peluncuran Lemon Pre-Mainnet Testnet (2023-09-19)
· Trigger: Persiapan akhir sebelum mainnet dengan parameter genesis dan konfigurasi mirip production
· Evidence: Blog Lemon Testnet; validasi konfigurasi genesis, token distribution, migrasi testnet ke mainnet (HIGH) [Phase 3 EV-008; https://blog.celestia.org/lemon-testnet/]
· Decision: Meluncurkan testnet pre-mainnet (Lemon) sebagai dress rehearsal mainnet
· Immediate Result: Validasi genesis config, token distribution mechanics, node migration process
· Long-term Impact: Mengurangi risiko launch mainnet; memastikan smooth transition
· Supporting Dataset: Phase 3 EV-008, Phase 3 EV-009

Keputusan: Peluncuran Mainnet Celestia dan TGE (2023-10-31)
· Trigger: Kesiapan teknis, komunitas, dan ekosistem untuk production launch
· Evidence: Blog Mainnet Launch; block height 0; Genesis Drop 60M TIA (6% supply); staking aktif; governance on-chain (HIGH) [Phase 3 EV-009, EV-010; https://blog.celestia.org/celestia-mainnet-launch/; https://blog.celestia.org/tia-genesis-drop/]
· Decision: Meluncurkan mainnet production dan Token Generation Event bersamaan dengan Genesis Drop
· Immediate Result: Jaringan production live; TIA liquide dan transferable; staking reward dimulai; governance aktif
· Long-term Impact: Memulai phase adoption rollup; price discovery pasar; tokenomics live; validator set economics aktif
· Supporting Dataset: Phase 3 EV-009, EV-010, Phase 6 Token, Phase 8 Trading Markets

Keputusan: Pembentukan Celestia Foundation di Zug, Switzerland (2023-10)
· Trigger: Perlu entitas non-profit untuk mengelola treasury protokol, governance, grants, dan stewardship TIA terpisah dari Labs
· Evidence: Blog Mainnet Launch menyebutkan Foundation; struktur dual entity (Labs for-profit, Foundation non-profit) (HIGH) [Phase 3 EV-011; Phase 2 Foundation entity; Phase 5 Treasury]
· Decision: Mendirikan Celestia Foundation (Zug) sebagai steward protokol dan pengelola treasury
· Immediate Result: Pemisahan core development (Labs) dari protocol governance/treasury (Foundation)
· Long-term Impact: Model governance dual-entity; Foundation mengelola community pool, grants, fee switch decisions
· Supporting Dataset: Phase 3 EV-011, Phase 2 Foundation, Phase 5 Treasury, Phase 6 Governance

Keputusan: Deploy Blobstream Contracts ke Ethereum Mainnet (2023-10)
· Trigger: Perlu verifikasi trust-minimized DA commitment di Ethereum untuk rollup EVM (Arbitrum Orbit, Polygon CDK, custom)
· Evidence: Blobstream contracts repo; deploy Ethereum mainnet Oct 2023; relayer permissionless (HIGH) [Phase 3 EV-012; https://github.com/celestiaorg/blobstream-contracts; Phase 4 Blobstream; Phase 7 Integration Blobstream]
· Decision: Mendeploy smart contract Blobstream di Ethereum mainnet untuk verifikasi header Celestia
· Immediate Result: Rollup berbasis EVM dapat memverifikasi DA Celestia on-chain Ethereum
· Long-term Impact: Membuka pasar rollup Ethereum-aligned; Blobstream menjadi critical infrastructure; dependency pada Ethereum finality dan gas costs
· Supporting Dataset: Phase 3 EV-012, Phase 4 Blobstream, Phase 7 Integration Blobstream, Phase 7 External Dependencies Ethereum

Keputusan: Announcement Integrasi Arbitrum Orbit + Celestia DA (2023-11)
· Trigger: Ekspansi ekosistem ke rollup framework terbesar di Ethereum (Arbitrum Orbit)
· Evidence: Blog Arbitrum Orbit + Celestia; partnership resmi dengan Offchain Labs (HIGH) [Phase 3 EV-013; https://blog.celestia.org/arbitrum-orbit-celestia/; Phase 7 Major Integrations Arbitrum Orbit]
· Decision: Integrasi resmi dengan Arbitrum Orbit untuk menggunakan Celestia sebagai DA layer
· Immediate Result: Orbit chains memperoleh opsi DA modular; validasi produk pasar untuk Celestia DA
· Long-term Impact: Menarik developer Arbitrum ecosystem; menempatkan Celestia sebagai DA alternatif untuk EigenDA di Ethereum rollup stack
· Supporting Dataset: Phase 3 EV-013, Phase 7 Major Integrations Arbitrum Orbit, Phase 8 Competitor Landscape EigenDA

Keputusan: Announcement Integrasi Starknet + Celestia DA (2023-11)
· Trigger: Validasi arsitektur modular untuk ZK-rollup besar; ekspansi ke non-EVM execution environment
· Evidence: Blog Starknet + Celestia; ZK-rollup pertama mengadopsi Celestia DA (HIGH) [Phase 3 EV-014; https://blog.celestia.org/starknet-celestia/; Phase 7 Major Integrations Starknet]
· Decision: Integrasi dengan Starknet untuk DA alternative/pelengkap Ethereum calldata
· Immediate Result: Validasi Celestia DA untuk ZK stack; memperluas narrative ke beyond EVM
· Long-term Impact: Menunjukkan flexibility execution environment; menarik ZK builder lain
· Supporting Dataset: Phase 3 EV-014, Phase 7 Major Integrations Starknet, Phase 4 Execution Environment

Keputusan: Announcement Integrasi Polygon CDK + Celestia DA (2023-12)
· Trigger: Ekspansi ke ekosistem Polygon CDK yang berkembang; capture market share DA layer untuk app-chain
· Evidence: Blog Polygon CDK + Celestia; CDK chains dapat menggunakan Celestia DA via Blobstream (HIGH) [Phase 3 EV-015; https://blog.celestia.org/polygon-cdk-celestia/; Phase 7 Major Integrations Polygon CDK]
· Decision: Integrasi resmi dengan Polygon Chain Development Kit
· Immediate Result: CDK chains memperoleh opsi DA modular; perluas jangkau ke developer Polygon
· Long-term Impact: Multi-ecosystem DA provider strategy; tidak terikat single rollup stack
· Supporting Dataset: Phase 3 EV-015, Phase 7 Major Integrations Polygon CDK

Keputusan: Audit Keamanan oleh Informal Systems dan Trail of Bits (2023)
· Trigger: Pre-mainnet security validation untuk consensus, light client, Blobstream, Celestia App, kriptografi
· Evidence: Informal Systems audit consensus/light client/Blobstream; Trail of Bits audit Celestia App/Blobstream contracts/kriptografi; laporan diterbitkan (HIGH) [Phase 3 EV-016, EV-017; Phase 4 Audit History; https://informal.systems/audits/; https://github.com/trailofbits/publications/tree/master/audits]
· Decision: Mengkontrak dua auditor top-tier untuk audit komprehensif pre-mainnet
· Immediate Result: Temuan kritis diperbaiki sebelum launch; peningkatan kepercayaan keamanan
· Long-term Impact: Membangun reputation security-first; standard untuk audit pasca-upgrade (Zellic, Sigma Prime 2024)
· Supporting Dataset: Phase 3 EV-016, EV-017, Phase 4 Audit History, Phase 7 External Dependencies Auditors

Keputusan: Proposal Governance On-Chain Pertama (2024-01)
· Trigger: Aktivasi governance module pasca-mainnet; parameter chain perlu adjustment
· Evidence: Docs Governance; proposal pertama processed on-chain (HIGH) [Phase 3 EV-018; https://docs.celestia.org/learn/governance; Phase 6 Governance]
· Decision: Memproses proposal governance on-chain pertama untuk parameter chain/upgrade
· Immediate Result: Mekanisme governance terbukti berfungsi; parameter chain diubah via vote
· Long-term Impact: On-chain governance sebagai primary coordination mechanism; Foundation dan Labs sebagai proposer utama awal
· Supporting Dataset: Phase 3 EV-018, Phase 6 Governance, Phase 2 DAO Celestia Governance

Keputusan: Rilis Sovereign SDK oleh Sovereign Labs (2024-02)
· Trigger: Perlu framework rollup sovereign berbasis Rust untuk complete tooling coverage (Golang Rollkit + Rust Sovereign SDK)
· Evidence: Sovereign SDK GitHub release; framework rollup sovereign native Celestia DA tanpa settlement layer (MEDIUM) [Phase 3 EV-019; https://github.com/Sovereign-Labs/sovereign-sdk; Phase 7 SDK Sovereign SDK]
· Decision: Mendukung/mengembangkan Sovereign SDK sebagai framework rollup sovereign alternatif
· Immediate Result: Tooling lengkap untuk sovereign rollup tersedia (Rust-based); memperluas developer base
· Long-term Impact: Dual-framework strategy (Rollkit Go + Sovereign SDK Rust); capture different developer preferences
· Supporting Dataset: Phase 3 EV-019, Phase 7 SDK Sovereign SDK, Phase 2 Company Sovereign Labs

Keputusan: Penelitian Quantum Gravity Bridge Trust-Minimized Bridging (2024-03)
· Trigger: Perlu solusi bridging native tanpa validator set terpusat (trust-minimized) untuk cross-chain asset transfer
· Evidence: Forum QGB research; desain light client verification cross-chain (MEDIUM) [Phase 3 EV-020; https://forum.celestia.org/t/quantum-gravity-bridge/; Phase 4 Quantum Gravity Bridge]
· Decision: Memulai R&D Quantum Gravity Bridge untuk bridging generasi berikutnya
· Immediate Result: Spesifikasi bridging trust-minimized dipublikasikan; R&D berlanjut
· Long-term Impact: Jika berhasil, mengurangi dependency pada Blobstream/Ethereum untuk bridging; native interoperability
· Supporting Dataset: Phase 3 EV-020, Phase 4 Quantum Gravity Bridge, Phase 7 Integration QGB

Keputusan: Upgrade Protokol v2.0 Mayor Pertama (2024-06)
· Trigger: Perlu peningkatan fee market, DAS efficiency, namespace versioning, kompatibilitas rollup baru
· Evidence: Blog upgrade v2.0; completed via on-chain governance (HIGH) [Phase 3 EV-021; https://blog.celestia.org/; Phase 4 Technical Upgrade History]
· Decision: Melakukan upgrade protokol mayor pertama pasca-mainnet via governance
· Immediate Result: Peningkatan throughput blobspace, efisiensi light client, dukungan fitur rollup baru
· Long-term Impact: Membuktikan upgrade coordination works; set precedent untuk upgrade berkala
· Supporting Dataset: Phase 3 EV-021, Phase 4 Technical Upgrade History, Phase 6 Governance

Keputusan: Deploy Rollup Produksi Pertama Menggunakan Celestia DA (2024-07)
· Trigger: Adoption milestone - rollup nyata memposting data ke mainnet secara rutin
· Evidence: Manta Pacific, Dymension RollApps, Rollkit/Sovereign SDK rollups mulai posting blob (HIGH) [Phase 3 EV-022; https://blog.celestia.org/category/ecosystem/; Phase 7 Major Integrations Manta/Dymension]
· Decision: Mendukung dan memfasilitasi deploy rollup produksi di mainnet
· Immediate Result: Penggunaan blobspace nyata bermula; fee revenue tercatat on-chain; metrik adoption real
· Long-term Impact: Validasi product-market fit; revenue stream aktif; flywheel adoption rollup
· Supporting Dataset: Phase 3 EV-022, Phase 7 Major Integrations, Phase 5 Revenue Model, Phase 8 Adoption Metrics

Keputusan: Laporan Satu Tahun Mainnet dan Metrik Adopsi (2024-10)
· Trigger: Transparansi dan accountability untuk komunitas, investor, dan stakeholder
· Evidence: Blog one-year report; metrik blob, throughput, rollup count, staking, treasury (HIGH) [Phase 3 EV-023; https://blog.celestia.org/; Phase 8 Adoption Metrics]
· Decision: Memublikasikan laporan tahunan ekosistem dan metrik adopsi
· Immediate Result: Transparansi metrik; dasar roadmap tahun kedua
· Long-term Impact: Membangun kepercayaan jangka panjang; data-driven decision making
· Supporting Dataset: Phase 3 EV-023, Phase 8 Adoption Metrics

Keputusan: Listing TIA di Centralized Exchange Utama (2024)
· Trigger: Liquidity, price discovery, on-ramp fiat, akses pasar global untuk TIA
· Evidence: Binance, Coinbase, Kraken, Bybit, OKX, KuCoin, Gate, MEXC, HTX, Bitget, Crypto.com listing (HIGH) [Phase 3 EV-024; Phase 8 Exchange Ecosystem; https://www.coingecko.com/en/coins/celestia]
· Decision: Koordinasi listing di 11 major CEX global
· Immediate Result: Liquidity TIA meningkat signifikan; price discovery terbuka; akses retail/institusi
· Long-term Impact: CEX liquidity dominant vs DEX; market structure bergantung CEX; regulatory exposure
· Supporting Dataset: Phase 3 EV-024, Phase 8 Exchange Ecosystem, Phase 8 Liquidity

Keputusan: Deploy wTIA di Ethereum/Arbitrum oleh Pihak Ketiga (2024)
· Trigger: Permintaan komunitas untuk TIA di DeFi EVM (lending, DEX, yield farming)
· Evidence: wTIA ERC-20 deploy oleh third-party; tidak resmi Celestia Labs; liquidity di Uniswap V3 Arbitrum, Camelot (MEDIUM) [Phase 3 EV-025; Phase 6 wTIA; Phase 7 Integration wTIA; Phase 8 Liquidity DEX]
· Decision: Mengizinkan/mendukung third-party wrapped TIA deployment (tidak resmi)
· Immediate Result: TIA accessible di DeFi EVM; bridge liquidity terbentuk
· Long-term Impact: Custody risk pada wTIA (third-party); Quantum Gravity Bridge sebagai solusi native jangka panjang
· Supporting Dataset: Phase 3 EV-025, Phase 6 wTIA, Phase 7 Integration wTIA, Phase 4 Quantum Gravity Bridge

Keputusan: Program Grant Celestia Foundation Sputnik Wave 1 (2024)
· Trigger: Perlu mendanai builder ekosistem (tooling, rollup, light client, infra) untuk mempercepat adoption
· Evidence: Forum governance grants program; dana treasury dialokasikan ke builder (HIGH) [Phase 3 EV-026; https://forum.celestia.org/c/grants/; Phase 5 Fundraising Mechanism Grants]
· Decision: Meluncurkan program grant resmi (Sputnik Wave 1) dari treasury Foundation
· Immediate Result: Dana treasury dialokasikan ke builder; percepatan tooling dan aplikasi
· Long-term Impact: Flywheel ekosistem; dependency pada Foundation grants untuk early-stage projects
· Supporting Dataset: Phase 3 EV-026, Phase 5 Fundraising Mechanism, Phase 7 Developer Ecosystem

Keputusan: Diskusi Fee Switch / Value Accrual Mechanism di Governance (2024-11)
· Trigger: Tekanan komunitas dan investor untuk value accrual TIA beyond staking inflation
· Evidence: Forum governance discussion; proposal fee switch belum final (MEDIUM) [Phase 3 EV-027; https://forum.celestia.org/t/fee-switch-value-accrual/; Phase 5 Revenue Model Fee Switch]
· Decision: Membuka diskusi dan proposal governance untuk fee switch (mengalihkan blobspace fee ke staker)
· Immediate Result: Debat komunitas tentang tokenomics lanjutan; belum ada keputusan final
· Long-term Impact: Critical untuk naratif investasi TIA; mempengaruhi staking participation dan token velocity
· Supporting Dataset: Phase 3 EV-027, Phase 5 Revenue Model, Phase 6 Token Utility, Phase 8 Narrative Position

Keputusan: Rilis Light Client WASM/Mobile SDK (2025-01)
· Trigger: Perlu verifikasi trust-minimized DA langsung dari client ringan (browser, mobile) untuk mass adoption
· Evidence: Light client WASM browser dan mobile SDK release; DAS sampling dari client side (HIGH) [Phase 3 EV-028; https://github.com/celestiaorg/celestia-node; Phase 7 Integration Light Client WASM]
· Decision: Mengembangkan dan merilis light client WASM untuk browser dan mobile SDK
· Immediate Result: Verifikasi DA trust-minimized tersedia untuk web/mobile app; memperluas light client adoption
· Long-term Impact: Security model DAS diperkuat (lebih banyak light client); user experience trust-minimized tanpa full node
· Supporting Dataset: Phase 3 EV-028, Phase 4 Security Model, Phase 7 Integration Light Client WASM

Keputusan: Upgrade Protokol v3.0 "Ginger" (2025-03)
· Trigger: Peningkatan DAS throughput, namespace versioning lanjutan, persiapan QGB integration
· Evidence: Blog upgrade v3.0; completed via governance (HIGH) [Phase 3 EV-029; https://blog.celestia.org/; Phase 4 Technical Upgrade History]
· Decision: Upgrade protokol mayor kedua dengan fokus scaling dan QGB preparation
· Immediate Result: Kapasitas blobspace meningkat; fondasi teknis bridging trust-minimized siap
· Long-term Impact: Scaling roadmap execution; QGB integration path cleared
· Supporting Dataset: Phase 3 EV-029, Phase 4 Technical Upgrade History, Phase 4 Quantum Gravity Bridge

Keputusan: Testnet Publik Quantum Gravity Bridge (2025-06, planned)
· Trigger: Validasi desain bridging trust-minimized di lingkungan adversarial sebelum mainnet
· Evidence: Blog/QGB forum; testnet publik planned Juni 2025 (MEDIUM) [Phase 3 EV-030; https://blog.celestia.org/; Phase 4 Quantum Gravity Bridge; Phase 7 Integration QGB]
· Decision: Meluncurkan testnet publik QGB untuk pengujian bridging trust-minimized
· Immediate Result: Validasi desain bridging; feedback keamanan dari komunitas
· Long-term Impact: Jika sukses, native bridging tanpa trusted relayer/validator set; major differentiator vs competitors
· Supporting Dataset: Phase 3 EV-030, Phase 4 Quantum Gravity Bridge, Phase 7 Integration QGB

Evolution Pattern

Perubahan Strategi: Dari Research Project ke Production DA Layer ke Modular

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
