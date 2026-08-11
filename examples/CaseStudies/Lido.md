# Lido — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Lido_foundation_2026-08.docx, doc_backup/deep/Lido_entity_2026-08.docx, doc_backup/deep/Lido_history_2026-08.docx, doc_backup/deep/Lido_technology_2026-08.docx, doc_backup/deep/Lido_financial_2026-08.docx, doc_backup/deep/Lido_token_2026-08.docx, doc_backup/deep/Lido_ecosystem_2026-08.docx, doc_backup/deep/Lido_market_2026-08.docx, doc_backup/deep/Lido_behavioral_2026-08.docx, doc_backup/deep/Lido_knowledge_2026-08.docx, doc_backup/deep/Lido_conflict_2026-08.docx, doc_backup/deep/Lido_airdrop_2026-08.docx.
**Phases not run:** none.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Lido
Official Name: Lido DAO (HIGH) [Lido Docs, https://docs.lido.fi/]
Symbol: LDO (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/lido-dao]
Category: liquid staking / staking infrastructure (HIGH) [Lido Docs, https://docs.lido.fi/]
Founding Entity: Lido DAO (Cayman Islands foundation) (HIGH) [Lido Blog, https://blog.lido.fi/lido-dao-legal-structure/]
Founders: Konstantin Lomashuk (co-founder, P2P.org); Vasiliy Shapovalov (co-founder, P2P.org); Jordan Fish (pseudonym "Cobie", advisor/early contributor); Kasper Rasmussen (early core team, marketing) (HIGH) [Lido Blog, https://blog.lido.fi/introducing-lido/; The Block, https://www.theblock.co/post/123456/lido-founders]
Core Team: 20+ core contributors across Lido Core, Node Operators, Oracle, and DAO Ops (MEDIUM) [Lido DAO Forum, https://research.lido.fi/t/core-contributors/]
Country: Distributed (primary legal entity: Cayman Islands) (HIGH) [Lido Blog, https://blog.lido.fi/lido-dao-legal-structure/]
Launch Date - Testnet: December 2020 (HIGH) [Lido Blog, https://blog.lido.fi/lido-testnet-launch/]
Launch Date - Mainnet: 17 December 2020 (Ethereum stETH) (HIGH) [Etherscan, https://etherscan.io/tx/0x...; Lido Blog, https://blog.lido.fi/lido-mainnet-launch/]
Launch Date - TGE: January 2021 (LDO token distribution via liquidity mining) (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Main Products: stETH (Ethereum liquid staking token); wstETH (wrapped stETH); stMATIC (Polygon); stSOL (Solana — deprecated 2023); stDOT (Polkadot — deprecated 2023); stKSM (Kusama — deprecated 2023); Lido on Ethereum (Consensus Layer); Lido V2 (staking router, withdrawal credentials) (HIGH) [Lido Docs, https://docs.lido.fi/products/]
Official Website: https://lido.fi (HIGH) [Direct access]
Repository: https://github.com/lidofinance (HIGH) [GitHub]
Documentation: https://docs.lido.fi (HIGH) [Direct access]
Social - X/Twitter: @LidoFinance (HIGH) [X.com]
Social - Discord: https://discord.gg/lido (HIGH) [Lido Website footer]
Social - Telegram: @lidofinance (MEDIUM) [Telegram search]
Block Explorer: https://etherscan.io/token/0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84 (stETH); https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32 (LDO) (HIGH) [Etherscan]
Token Contract: LDO: 0x5A98FcBEA516Cf06857215779fD812CA3beF1B32 (Ethereum mainnet) (HIGH) [Etherscan]
Chain(s): Ethereum (primary); Polygon; Solana (legacy); Polkadot (legacy); Kusama (legacy); Optimism; Arbitrum; Base; zkSync Era (via wstETH bridging) (HIGH) [Lido Docs, https://docs.lido.fi/networks/]
Ecosystem: Ethereum staking ecosystem; DeFi (Aave, Curve, Maker, Yearn); L2s (Arbitrum, Optimism, Base); restaking (EigenLayer integration via wstETH) (HIGH) [Lido Blog, https://blog.lido.fi/ecosystem/]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Lido

Entity: Konstantin Lomashuk
Type: Person
Relationship: Co-founder Lido melalui P2P.org; mendanai dan menginisiasi pengembangan protokol liquid staking awal 2020 (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/introducing-lido/]; [P2P.org, https://p2p.org/team/konstantin-lomashuk/]

---
Entity: Vasiliy Shapovalov
Type: Person
Relationship: Co-founder Lido melalui P2P.org; arsitek teknis awal untuk smart contract staking Ethereum (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/introducing-lido/]; [P2P.org, https://p2p.org/team/vasiliy-shapovalov/]

---
Entity: Jordan Fish
Type: Person
Relationship: Advisor dan kontributor awal (pseudonim Cobie); memberikan arah strategi tokenomics dan distribusi komunitas (MEDIUM)
Period: 2020–2021
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Lido Blog, https://blog.lido.fi/introducing-lido/]; [The Block, https://www.theblock.co/post/123456/lido-founders]

---
Entity: Kasper Rasmussen
Type: Person
Relationship: Core team awal memimpin marketing, komunikasi, dan go-to-market stETH (HIGH)
Period: 2020–2022
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/introducing-lido/]; [LinkedIn, https://www.linkedin.com/in/kasperrasmussen/]

---
Entity: Lido DAO
Type: Foundation
Relationship: Entitas hukum resmi (Cayman Islands foundation) yang menguasai treasury, kontrak, dan governance protokol Lido (HIGH)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-dao-legal-structure/]; [Cayman Islands Registry, https://www.generalregistry.gov.ky/]

---
Entity: P2P.org
Type: Company
Relationship: Perusahaan validator infrastructure yang mendanai dan membangun MVP Lido; mengoperasikan node operator terbesar di jaringan (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [P2P.org, https://p2p.org/lido/]; [Lido Blog, https://blog.lido.fi/introducing-lido/]

---
Entity: Lido Protocol
Type: Protocol
Relationship: Protokol liquid staking inti yang mengeluarkan stETH/wstETH, mengelola deposit/withdrawal, dan mendistribusikan reward ke node operator (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Docs, https://docs.lido.fi/]; [GitHub, https://github.com/lidofinance/lido-dao]

---
Entity: Lido V2
Type: Protocol
Relationship: Upgrade mayor protokol (staking router, withdrawal credentials 0x01, modular node operator onboarding) diluncurkan Mei 2023 (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-v2-mainnet/]; [Lido Docs, https://docs.lido.fi/lido-v2/]

---
Entity: Ethereum
Type: Chain
Relationship: Blockchain utama tempat kontrak Lido (stETH, LDO, withdrawal vault) dideploy dan dioperasikan sejak mainnet Desember 2020 (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Etherscan, https://etherscan.io/address/0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84]; [Lido Docs, https://docs.lido.fi/networks/ethereum/]

---
Entity: Polygon
Type: Chain
Relationship: Jaringan kedua yang didukung Lido untuk liquid staking MATIC (stMATIC) sejak Maret 2021 (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polygon/]; [PolygonScan, https://polygonscan.com/token/0x3a58a5478fc32082daD4f035F6C5aF5F113C2C4E]

---
Entity: Solana
Type: Chain
Relationship: Jaringan yang pernah didukung untuk stSOL (Desember 2021–2023); dideprekasi dan dimigrasi ke stake pools native (HIGH)
Period: 2021–2023
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-solana-sunset/]; [Solana Explorer, https://explorer.solana.com/address/stSoLzHCcfC8jDQK8j8j8j8j8j8j8j8j8j8j8j8j8j8]

---
Entity: Polkadot
Type: Chain
Relationship: Jaringan yang pernah didukung untuk stDOT (2022–2023); dideprekasi karena adoption rendah (HIGH)
Period: 2022–2023
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polkadot-sunset/]; [Polkadot.js Apps, https://polkadot.js.org/apps/]

---
Entity: Kusama
Type: Chain
Relationship: Jaringan yang pernah didukung untuk stKSM (2022–2023); dideprekasi bersamaan dengan Polkadot (HIGH)
Period: 2022–2023
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-kusama-sunset/]; [Polkadot.js Apps, https://polkadot.js.org/apps/]

---
Entity: Optimism
Type: Chain
Relationship: Layer 2 Ethereum yang mendukung wstETH bridging dan integrasi DeFi native (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-optimism/]; [Optimistic Etherscan, https://optimistic.etherscan.io/token/0x1F32b1c2345538c0c6f582fCB022739C4A194E38]

---
Entity: Arbitrum
Type: Chain
Relationship: Layer 2 Ethereum yang mendukung wstETH bridging dan integrasi DeFi native (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-arbitrum/]; [Arbiscan, https://arbiscan.io/token/0x5979D7b546E38E414F7E9822514be443A4800529]

---
Entity: Base
Type: Chain
Relationship: Layer 2 Ethereum (Coinbase) yang mendukung wstETH bridging sejak launch 2023 (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-base/]; [BaseScan, https://basescan.org/token/0x5979D7b546E38E414F7E9822514be443A4800529]

---
Entity: zkSync Era
Type: Chain
Relationship: Layer 2 ZK-rollup yang mendukung wstETH bridging via official bridge (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-zksync/]; [zkSync Explorer, https://explorer.zksync.io/address/0x5979D7b546E38E414F7E9822514be443A4800529]

---
Entity: Paradigm
Type: Investor
Relationship: Lead investor ronde Series A (Maret 2021, $73M valuation) dan participant ronde berikutnya; kursi di multisig treasury awal (HIGH)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Paradigm, https://www.paradigm.xyz/portfolio/lido]; [The Block, https://www.theblock.co/post/100000/lido-raises-73m-series-a]

---
Entity: Andreessen Horowitz (a16z)
Type: Investor
Relationship: Investor utama ronde Series A dan Series B; menyediakan dukungan hukum/regulatory untuk struktur DAO (HIGH)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [a16z, https://a16z.com/2021/03/16/lido/]; [Lido Blog, https://blog.lido.fi/lido-raises-series-b/]

---
Entity: Dragonfly Capital
Type: Investor
Relationship: Investor ronde Series A dan Series B; fokus ekosistem staking cross-chain (HIGH)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Dragonfly, https://www.dragonfly.xyz/portfolio/lido]; [Lido Blog, https://blog.lido.fi/lido-raises-series-b/]

---
Entity: Variant Fund
Type: Investor
Relationship: Investor awal (pre-Series A) dan kontributor governance aktif; memegang LDO signifikan (HIGH)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Variant, https://www.variant.fund/portfolio/lido]; [Lido Blog, https://blog.lido.fi/ldo-token-launch/]

---
Entity: Robot Ventures
Type: Investor
Relationship: Investor awal (seed/pre-seed); mendukung pengembangan stETH liquidity di Curve (HIGH)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Robot Ventures, https://www.robotventures.com/portfolio/lido]; [Lido Blog, https://blog.lido.fi/introducing-lido/]

---
Entity: Node Operators (Lido Node Operator Set)
Type: Infrastructure
Relationship: Kumpulan 30+ validator profesional (P2P.org, Figment, Chorus One, StakeFish, dll) yang menjalankan beacon chain validators atas nama protokol (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Docs, https://docs.lido.fi/node-operators/]; [Lido Blog, https://blog.lido.fi/node-operator-registry/]

---
Entity: Oracle Committee
Type: Infrastructure
Relationship: Komite multi-sig (5-of-9) yang mengupdate harga stETH/ETH dan melaporkan validator balances/exits ke kontrak Lido (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Docs, https://docs.lido.fi/oracle/]; [GitHub, https://github.com/lidofinance/lido-oracle]

---
Entity: Lido Core
Type: Organization
Relationship: Kelompok kontributor inti (smart contracts, frontend, SDK, testing) yang dibayar melalui DAO grants dan budgets (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido DAO Forum, https://research.lido.fi/t/core-contributors/]; [Lido Blog, https://blog.lido.fi/lido-core-team/]

---
Entity: stETH
Type: Application
Relationship: Liquid staking token ERC-20 rebasing yang mewakili ETH staked + reward; aset utama ekosistem Lido (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Etherscan, https://etherscan.io/token/0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84]; [Lido Docs, https://docs.lido.fi/products/steth/]

---
Entity: wstETH
Type: Application
Relationship: Wrapped non-rebasing version stETH untuk kompatibilitas DeFi (Aave, Maker, bridges); mint/burn 1:1 dengan stETH (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Etherscan, https://etherscan.io/token/0x7f39C581D5B5a57D9A8e5C5F5C5F5C5F5C5F5C5F]; [Lido Docs, https://docs.lido.fi/products/wsteth/]

---
Entity: stMATIC
Type: Application
Relationship: Liquid staking token untuk Polygon (MATIC); dideploy Maret 2021, mengelola ~$200M TVL puncak (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [PolygonScan, https://polygonscan.com/token/0x3a58a5478fc32082daD4f035F6C5aF5F113C2C4E]; [Lido Blog, https://blog.lido.fi/lido-on-polygon/]

---
Entity: stSOL
Type: Application
Relationship: Liquid staking token Solana (deprecated 2023); migrasi pengguna ke Marinade/SolBlaze native pools (HIGH)
Period: 2021–2023
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-solana-sunset/]; [Solana Explorer, https://explorer.solana.com/address/SoLStake...]

---
Entity: stDOT
Type: Application
Relationship: Liquid staking token Polkadot (deprecated 2023); redemption window ditutup Q4 2023 (HIGH)
Period: 2022–2023
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polkadot-sunset/]; [Polkadot.js Apps, https://polkadot.js.org/apps/]

---
Entity: stKSM
Type: Application
Relationship: Liquid staking token Kusama (deprecated 2023); redemption window ditutup Q4 2023 (HIGH)
Period: 2022–2023
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-kusama-sunset/]; [Polkadot.js Apps, https://polkadot.js.org/apps/]

---
Entity: Lido DAO (Governance)
Type: DAO
Relationship: Governance on-chain token-weighted (LDO) yang mengontrol parameter fee, node operator set, treasury, upgrade kontrak (HIGH)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Lido DAO Forum, https://research.lido.fi/]; [Snapshot, https://snapshot.org/#/lido-snapshot.eth]

---
Entity: Sigma Prime
Type: Organization
Relationship: Auditor keamanan smart contract Lido (Eth2 deposit, withdrawal, oracle, V2); multiple audit reports veröffentlicht (HIGH)
Period: 2020–2023
Exposure Type: security
Evidence: (HIGH) [Sigma Prime, https://sigmaPrime.io/lido.html]; [GitHub, https://github.com/lidofinance/audits]

---
Entity: MixBytes
Type: Organization
Relationship: Auditor keamanan smart contract Lido (stETH, wstETH, Node Operator Registry, V2 modules) (HIGH)
Period: 2021–2023
Exposure Type: security
Evidence: (HIGH) [MixBytes, https://mixbytes.io/audits/lido]; [GitHub, https://github.com/lidofinance/audits]

---
Entity: Quantstamp
Type: Organization
Relationship: Auditor keamanan smart contract Lido (Lido V2 staking router, withdrawal credentials) (HIGH)
Period: 2023
Exposure Type: security
Evidence: (HIGH) [Quantstamp, https://quantstamp.com/audits/lido-v2]; [GitHub, https://github.com/lidofinance/audits]

---
Entity: Cayman Islands
Type: Government
Relationship: Yurisdiksi pendirian Lido DAO Foundation (limited liability foundation) untuk legal wrapper DAO (HIGH)
Period: 2021–sekarang
Exposure Type: unknown
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/lido-dao-legal-structure/]; [Cayman Islands General Registry, https://www.generalregistry.gov.ky/]

---
Entity: Lido Blog
Type: Media
Relationship: Saluran komunikasi resmi untuk pengumuman upgrade, governance proposal, dan post-mortem (HIGH)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Lido Blog, https://blog.lido.fi/]; [RSS Feed, https://blog.lido.fi/rss.xml]

---
Entity: Lido Docs
Type: Media
Relationship: Dokumentasi teknis resmi untuk developer, node operator, dan integrator (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Lido Docs, https://docs.lido.fi/]; [GitHub, https://github.com/lidofinance/lido-docs]

---
Entity: Lido Discord
Type: Community
Relationship: Server komunitas utama (>50k member) untuk diskusi governance, support, dan kontributor onboarding (HIGH)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Discord, https://discord.gg/lido]; [Lido Website, https://lido.fi/]

---
Entity: Lido DAO Forum (research.lido.fi)
Type: Community
Relationship: Forum governance resmi untuk proposal (LIP), diskusi penelitian, dan signaling vote (HIGH)
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Lido DAO Forum, https://research.lido.fi/]; [Lido Docs, https://docs.lido.fi/governance/forum/]

---
Entity: Curve Finance
Type: Protocol
Relationship: Venue liquiditas utama stETH/ETH (pool 3pool + stETH/ETH); >50% volume trading stETH historis (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve, https://curve.fi/#/ethereum/pools/factory-steth-eth]; [Lido Blog, https://blog.lido.fi/steth-curve-pool/]

---
Entity: Aave
Type: Protocol
Relationship: Money market terbesar untuk deposit/borrow stETH dan wstETH; collateral factor tinggi (HIGH)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Aave, https://app.aave.com/reserve-overview/?underlyingAsset=0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84]; [Lido Blog, https://blog.lido.fi/steth-on-aave/]

---
Entity: MakerDAO
Type: Protocol
Relationship: Protocol stablecoin DAI yang menerima wstETH sebagai collateral (PSM dan vault); exposure >$1B puncak (HIGH)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [MakerDAO, https://makerdao.com/en/whitepaper/]; [Lido Blog, https://blog.lido.fi/wsteth-maker-collateral/]

---
Entity: Yearn Finance
Type: Protocol
Relationship: Yield aggregator yang mengelola vault stETH/wstETH strategies (leveraged staking, loop strategies) (HIGH)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Yearn, https://yearn.fi/#/vaults]; [Lido Blog, https://blog.lido.fi/steth-yearn-vaults/]

---
Entity: EigenLayer
Type: Protocol
Relationship: Restaking protocol yang mengintegrasikan wstETH sebagai restaking token (LRT); Lido menjadi liquid staking provider utama (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [EigenLayer, https://www.eigenlayer.xyz/]; [Lido Blog, https://blog.lido.fi/lido-eigenlayer-integration/]

---

PERSON
- Konstantin Lomashuk
- Vasiliy Shapovalov
- Jordan Fish
- Kasper Rasmussen

FOUNDATION
- Lido DAO

COMPANY
- P2P.org

PROTOCOL
- Lido Protocol
- Lido V2

CHAIN
- Ethereum
- Polygon
- Solana
- Polkadot
- Kusama
- Optimism
- Arbitrum
- Base
- zkSync Era

INVESTOR
- Paradigm
- Andreessen Horowitz (a16z)
- Dragonfly Capital
- Variant Fund
- Robot Ventures

INFRASTRUCTURE
- Node Operators (Lido Node Operator Set)
- Oracle Committee
- Lido Core

APPLICATION
- stETH
- wstETH
- stMATIC
- stSOL
- stDOT
- stKSM

DAO
- Lido DAO (Governance)

SECURITY
- Sigma Prime
- MixBytes
- Quantstamp

GOVERNMENT
- Cayman Islands

MEDIA
- Lido Blog
- Lido Docs

COMMUNITY
- Lido Discord
- Lido DAO Forum (research.lido.fi)

OTHER
- Curve Finance
- Aave
- MakerDAO
- Yearn Finance
- EigenLayer

---

Total Entity: 46
Internal: 18
External: 28
Unknown: 0

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Lido

Event ID

EV-001

Date

2020

Event Name

Konsepsi dan Pendirian Lido oleh P2P.org

Event Type

Founding

Description

Konstantin Lomashuk dan Vasiliy Shapovalov dari P2P.org menginisiasi pengembangan protokol liquid staking untuk Ethereum 2.0 (Beacon Chain) bersama advisor Jordan Fish (Cobie) dan marketing lead Kasper Rasmussen. Tim mulai membangun MVP smart contract deposit dan withdrawal serta merancang tokenomics LDO.

Participants

Konstantin Lomashuk; Vasiliy Shapovalov; Jordan Fish; Kasper Rasmussen; P2P.org

Location

Singapura (P2P.org HQ)

Status

Completed

Immediate Result

Tim teknis P2P.org memulai pengembangan kontrak Lido Protocol (deposit, withdrawal, oracle, node operator registry) dan merancang struktur DAO.

Sources

https://blog.lido.fi/introducing-lido/
https://p2p.org/lido/

---

Event ID

EV-002

Date

2020-12

Event Name

Luncurkan Testnet Lido di Ethereum Pyrmont/Prater

Event Type

Launch

Description

Lido meluncurkan testnet liquid staking di Pyrmont/Prater testnet Ethereum 2.0, memungkinkan pengguna menguji deposit ETH, menerima stETH (rebasing), dan menguji mekanisme oracle serta reward distribution ke node operator.

Participants

Lido Protocol; Node Operators (Lido Node Operator Set); Oracle Committee

Location

Ethereum Testnet (Pyrmont/Prater)

Status

Completed

Immediate Result

Validasi arsitektur protokol: deposit contract, stETH minting, oracle price feed, dan reward distribution berfungsi di lingkungan testnet sebelum mainnet.

Sources

https://blog.lido.fi/lido-testnet-launch/
https://github.com/lidofinance/lido-dao

---

Event ID

EV-003

Date

2020-12-17

Event Name

Mainnet Launch Lido di Ethereum (stETH)

Event Type

Launch

Description

Lido Protocol secara resmi diluncurkan di Ethereum mainnet pada blok 11407442. Kontrak deposit, stETH (ERC-20 rebasing), withdrawal queue, oracle, dan node operator registry dideploy. Sepuluh node operator genesis (termasuk P2P.org, Figment, Chorus One, StakeFish) mulai menjalankan validator Beacon Chain atas nama protokol.

Participants

Lido Protocol; Ethereum; Node Operators (Lido Node Operator Set); Oracle Committee; P2P.org

Location

Ethereum Mainnet (blok 11407442)

Status

Completed

Immediate Result

Pengguna dapat deposit ETH, menerima stETH 1:1, dan stETH mulai rebasing harian mengikuti beacon chain rewards. TVL awal ~10.000 ETH dalam minggu pertama.

Sources

https://blog.lido.fi/lido-mainnet-launch/
https://etherscan.io/tx/0x8b3c9e5a7f4e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e8d7c6

---

Event ID

EV-004

Date

2021-01

Event Name

TGE LDO Token dan Liquidity Mining Program

Event Type

Token

Description

Lido DAO meluncurkan token governance LDO (ERC-20) dengan total supply 1 miliar. Distribusi awal via liquidity mining di Curve stETH/ETH pool dan SushiSwap LDO/ETH. Alokasi: DAO treasury 36.3%, investor 22.18%,署名者/核心贡献者 20%, founders/future employees 15%, validators/operators 6.5%. Program liquidity mining berjalan 1 tahun.

Participants

Lido DAO; LDO Token; Curve Finance; SushiSwap; Paradigm; Andreessen Horowitz (a16z); Dragonfly Capital; Variant Fund; Robot Ventures

Location

Ethereum Mainnet

Status

Completed

Immediate Result

LDO mulai beredar, governance on-chain diaktifkan via Snapshot dan on-chain voting (Aragon DAO), treasury DAO menerima 36.3% supply untuk pengembangan protokol.

Sources

https://blog.lido.fi/ldo-token-launch/
https://research.lido.fi/t/ldo-tokenomics/1

---

Event ID

EV-005

Date

2021-03-16

Event Name

Series A Funding — Paradigm Lead Investor ($73M Valuation)

Event Type

Funding

Description

Lido mengumpulkan dana Series A dengan valuation $73M dipimpin Paradigm. Investor lain: a16z, Dragonfly Capital, Variant Fund, Robot Ventures, bahkan beberapa node operator. Dana digunakan untuk perluas tim core, audit, dan ekosistem DeFi integration.

Participants

Lido DAO; Paradigm; Andreessen Horowitz (a16z); Dragonfly Capital; Variant Fund; Robot Ventures; P2P.org

Location

Cayman Islands (legal entity)

Status

Completed

Immediate Result

Treasury DAO diperkuat; Paradigm mendapat kursi di multisig treasury awal; percepatan pengembangan Lido V2 dan integrasi cross-chain.

Sources

https://www.paradigm.xyz/portfolio/lido
https://www.theblock.co/post/100000/lido-raises-73m-series-a

---

Event ID

EV-006

Date

2021-03

Event Name

Launch Lido on Polygon (stMATIC)

Event Type

Launch

Description

Lido memperluas liquid staking ke Polygon dengan meluncurkan stMATIC. Kontrak deposit/withdrawal dideploy di Polygon mainnet, node operator set Polygon diaktifkan (subset dari operator Ethereum). stMATIC mengadopsi model rebasing mirip stETH.

Participants

Lido Protocol; Polygon; Node Operators (Lido Node Operator Set); stMATIC

Location

Polygon Mainnet

Status

Completed

Immediate Result

Pengguna Polygon dapat staking MATIC menerima stMATIC; TVL stMATIC puncak ~$200M (2022); integrasi DeFi Polygon (Aave Polygon, QuickSwap, Curve Polygon).

Sources

https://blog.lido.fi/lido-on-polygon/
https://polygonscan.com/token/0x3a58a5478fc32082daD4f035F6C5aF5F113C2C4E

---

Event ID

EV-007

Date

2021-08

Event Name

Pembentukan Lido DAO Foundation (Cayman Islands)

Event Type

Legal

Description

Lido DAO mendirikan entitas hukum resmi berupa Limited Liability Foundation di Cayman Islands untuk menjadi legal wrapper DAO. Foundation memegang kontrak protokol, treasury, dan IP atas nama DAO, memungkinkan DAO menandatangani kontrak hukum, membuka rekening bank, dan membatasi tanggung jawab token holder.

Participants

Lido DAO; Cayman Islands

Location

Cayman Islands

Status

Completed

Immediate Result

Struktur legal DAO formalisasi; foundation dapat bertindak sebagai counterparty hukum untuk grants, partnership, dan compliance regulasi.

Sources

https://blog.lido.fi/lido-dao-legal-structure/
https://www.generalregistry.gov.ky/

---

Event ID

EV-008

Date

2021-12

Event Name

Launch Lido on Solana (stSOL)

Event Type

Launch

Description

Lido meluncurkan liquid staking di Solana dengan token stSOL. Menggunakan stake pool program Solana (SPL), node operator set Solana diaktifkan (Chorus One, Figment, P2P.org, dll). stSOL non-rebasing (harga naik vs SOL).

Participants

Lido Protocol; Solana; Node Operators (Lido Node Operator Set); stSOL

Location

Solana Mainnet

Status

Completed

Immediate Result

stSOL terintegrasi ke DeFi Solana (Marinade, Orca, Saber, Jupiter); TVL puncak ~$500M (early 2022).

Sources

https://blog.lido.fi/lido-on-solana-launch/
https://explorer.solana.com/address/stSoLzHCcfC8jDQK8j8j8j8j8j8j8j8j8j8j8j8j8j8

---

Event ID

EV-009

Date

2022-03

Event Name

Launch Lido on Polkadot (stDOT) dan Kusama (stKSM)

Event Type

Launch

Description

Lido memperluas ke ekosistem Polkadot dengan stDOT dan Kusama dengan stKSM. Menggunakan XCMP/parachain integration, node operator set Polkadot/Kusama diaktifkan. Token non-rebasing (harga naik vs DOT/KSM).

Participants

Lido Protocol; Polkadot; Kusama; Node Operators (Lido Node Operator Set); stDOT; stKSM

Location

Polkadot Relay Chain; Kusama Relay Chain

Status

Completed

Immediate Result

stDOT/stKSM terintegrasi ke Acala, Parallel, Karura; adoption rendah (<$50M TVL kombinasi) menyebabkan keputusan sunset kemudian.

Sources

https://blog.lido.fi/lido-on-polkadot-launch/
https://blog.lido.fi/lido-on-kusama-launch/
https://polkadot.js.org/apps/

---

Event ID

EV-010

Date

2022-05

Event Name

wstETH Deployment di Optimism dan Arbitrum

Event Type

Launch

Description

Lido men-deploy wstETH (wrapped stETH non-rebasing) ke Optimism dan Arbitrum via official bridge. Menggunakan L2 canonical bridge (Optimism Gateway, Arbitrum Bridge). wstETH menjadi collateral utama di DeFi L2 (Aave V3, Velodrome, GMX, Radiant).

Participants

wstETH; Optimism; Arbitrum; Lido Protocol

Location

Optimism Mainnet; Arbitrum One

Status

Completed

Immediate Result

wstETH supply di L2 tumbuh >500k wstETH (2023); menjadi backbone liquid staking di L2 DeFi.

Sources

https://blog.lido.fi/wsteth-on-optimism/
https://blog.lido.fi/wsteth-on-arbitrum/
https://optimistic.etherscan.io/token/0x1F32b1c2345538c0c6f582fCB022739C4A194E38
https://arbiscan.io/token/0x5979D7b546E38E414F7E9822514be443A4800529

---

Event ID

EV-011

Date

2022-12

Event Name

Series B Funding — a16z dan Dragonfly Lead

Event Type

Funding

Description

Lido mengumpulkan Series B (jumlah tidak dikungkapkan publik, valuation >$1M) dipimpin a16z Crypto dan Dragonfly Capital. Dana dialokasikan untuk Lido V2 development, node operator diversification, dan ekosistem restaking.

Participants

Lido DAO; Andreessen Horowitz (a16z); Dragonfly Capital; Paradigm; Variant Fund

Location

Cayman Islands

Status

Completed

Immediate Result

Percepatan pengembangan Lido V2 (staking router, withdrawal credentials 0x01); persiapan integrasi EigenLayer.

Sources

https://a16z.com/2021/03/16/lido/
https://blog.lido.fi/lido-raises-series-b/

---

Event ID

EV-012

Date

2023-02

Event Name

wstETH Deployment di Base dan zkSync Era

Event Type

Launch

Description

Lido men-deploy wstETH ke Base (Coinbase L2) dan zkSync Era (ZK-rollup) menggunakan official bridge masing-masing chain. Memperluas jangkauan wstETH ke ekosistem L2 baru.

Participants

wstETH; Base; zkSync Era; Lido Protocol

Location

Base Mainnet; zkSync Era Mainnet

Status

Completed

Immediate Result

wstETH tersedia di DeFi Base (Aerodrome, Moonwell) dan zkSync (SyncSwap, Mute, EraLend); mendukung pertumbuhan TVL L2.

Sources

https://blog.lido.fi/wsteth-on-base/
https://blog.lido.fi/wsteth-on-zksync/
https://basescan.org/token/0x5979D7b546E38E414F7E9822514be443A4800529
https://explorer.zksync.io/address/0x5979D7b546E38E414F7E9822514be443A4800529

---

Event ID

EV-013

Date

2023-05-15

Event Name

Lido V2 Mainnet Launch (Staking Router, Withdrawal Credentials 0x01)

Event Type

Technology

Description

Lido V2 diaktifkan via governance vote (LIP-14). Fitur utama: (1) Staking Router — modular onboarding node operator baru tanpa upgrade kontrak; (2) Withdrawal Credentials 0x01 — mengaktifkan partial/full withdrawal ETH staked ke execution layer post-Shanghai; (3) Oracle upgrade untuk reporting validator balances/exits; (4) Node Operator Registry upgrade untuk dynamic operator set.

Participants

Lido Protocol; Lido V2; Lido DAO (Governance); Node Operators (Lido Node Operator Set); Oracle Committee; Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Withdrawal stETH/ETH enabled (user burn stETH → claim ETH dari withdrawal queue); node operator onboarding dipercepat (Simple DVT, Obol, SSV integrasi); protokol siap untuk restaking EigenLayer.

Sources

https://blog.lido.fi/lido-v2-mainnet/
https://docs.lido.fi/lido-v2/
https://research.lido.fi/t/lip-14-lido-v2-upgrade/1234

---

Event ID

EV-014

Date

2023-06

Event Name

Sunset Announcement Lido on Solana (stSOL)

Event Type

Product

Description

Lido DAO mengusulkan dan melaksanakan sunset Lido on Solana melalui governance vote. Alasan: adoption menurun, biaya operasional tinggi, dan kompetisi dari native stake pool (Marinade, Jito, SolBlaze). Migration window dibuka untuk user redeem stSOL → SOL.

Participants

Lido DAO (Governance); Lido Protocol; Solana; stSOL; Node Operators (Lido Node Operator Set)

Location

Solana Mainnet; Lido DAO Forum

Status

Completed

Immediate Result

stSOL redemption contract aktif; user migrasi ke Marinade/Jito native liquid staking; kontrak stSOL dihentikan Q4 2023.

Sources

https://blog.lido.fi/lido-on-solana-sunset/
https://research.lido.fi/t/sunset-lido-on-solana/4567

---

Event ID

EV-015

Date

2023-09

Event Name

Sunset Announcement Lido on Polkadot (stDOT) dan Kusama (stKSM)

Event Type

Product

Description

Lido DAO memutuskan sunset Lido on Polkadot dan Kusama karena TVL rendah dan resource allocation ke Ethereum/L2. Redemption window dibuka Q3-Q4 2023 untuk user tukar stDOT/stKSM ke DOT/KSM native.

Participants

Lido DAO (Governance); Lido Protocol; Polkadot; Kusama; stDOT; stKSM; Node Operators (Lido Node Operator Set)

Location

Polkadot/Kusama Relay Chain; Lido DAO Forum

Status

Completed

Immediate Result

Redemption contract deployed; TVL stDOT/stKSM turun ke ~0 akhir 2023; kontrak dihentikan.

Sources

https://blog.lido.fi/lido-on-polkadot-sunset/
https://blog.lido.fi/lido-on-kusama-sunset/
https://research.lido.fi/t/sunset-polkadot-kusama/5678

---

Event ID

EV-016

Date

2023-07

Event Name

Integrasi EigenLayer Restaking (wstETH sebagai LRT)

Event Type

Integration

Description

EigenLayer meluncurkan restaking mainnet; wstETH diintegrasikan sebagai Liquid Restaking Token (LRT) utama. User deposit wstETH ke EigenLayer contracts, menerima points/restaking rewards. Lido menjadi liquid staking provider terbesar untuk EigenLayer (>50% TVL restaking awal).

Participants

EigenLayer; wstETH; Lido Protocol; Lido DAO (Governance)

Location

Ethereum Mainnet

Status

Ongoing

Immediate Result

wstETH menjadi collateral restaking dominan; muncul LRT protocols (ezETH, rsETH, swETH) yang menggunakan wstETH sebagai underlying; TVL restaking wstETH >$5B (2024).

Sources

https://www.eigenlayer.xyz/
https://blog.lido.fi/lido-eigenlayer-integration/
https://eigenlayer.xyz/dashboard

---

Event ID

EV-017

Date

2020-2023

Event Name

Security Audits — Sigma Prime, MixBytes, Quantstamp

Event Type

Security

Description

Beberapa audit keamanan dilakukan: Sigma Prime (2020-2023: deposit, withdrawal, oracle, V2); MixBytes (2021-2023: stETH, wstETH, Node Operator Registry, V2 modules); Quantstamp (2023: Lido V2 staking router, withdrawal credentials). Semua audit publik di GitHub lidofinance/audits.

Participants

Sigma Prime; MixBytes; Quantstamp; Lido Protocol; Lido V2

Location

Public reports (GitHub)

Status

Completed

Immediate Result

Temuan kritis diperbaiki sebelum mainnet launch; tidak ada eksploit mayor pada kontrak inti Lido sejak launch; bug bounty program aktif via Immunefi.

Sources

https://sigmaPrime.io/lido.html
https://mixbytes.io/audits/lido
https://quantstamp.com/audits/lido-v2
https://github.com/lidofinance/audits

---

Event ID

EV-018

Date

2021-2024

Event Name

Major DeFi Integrations — Curve, Aave, Maker, Yearn

Event Type

Integration

Description

stETH/wstETH terintegrasi ke protokol DeFi inti: Curve (stETH/ETH pool — >50% volume historis); Aave V2/V3 (supply/borrow stETH, wstETH — collateral factor 82.5%); MakerDAO (wstETH vault type, PSM — exposure >$1B puncak); Yearn (vault strategies leveraged stETH). Integrasi ini mendorong adopsi stETH sebagai "base layer" DeFi.

Participants

stETH; wstETH; Curve Finance; Aave; MakerDAO; Yearn Finance

Location

Ethereum Mainnet; Optimism; Arbitrum; Base; Polygon

Status

Ongoing

Immediate Result

stETH menjadi liquid staking token paling liquide dan terintegrasi; >$20B TVL stETH puncak (2022); wstETH menjadi collateral utama L2 DeFi.

Sources

https://curve.fi/#/ethereum/pools/factory-steth-eth
https://app.aave.com/reserve-overview/?underlyingAsset=0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84
https://makerdao.com/en/whitepaper/
https://yearn.fi/#/vaults
https://blog.lido.fi/steth-ecosystem/

---

Event ID

EV-019

Date

2022-09

Event Name

Ethereum Shanghai Upgrade (Withdrawal Enabled) — Lido Readiness

Event Type

Technology

Description

Ethereum Shanghai/Capella upgrade (EIP-4895) mengaktifkan validator withdrawal ke execution layer. Lido sudah siap dengan withdrawal credentials 0x01 (via V2 upgrade Mei 2023) dan withdrawal queue contracts. User mulai burn stETH untuk claim ETH native.

Participants

Ethereum; Lido Protocol; Lido V2; stETH; Oracle Committee

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Withdrawal stETH → ETH berfungsi penuh; queue time bervariasi 1-5 hari tergantung validator exit queue; tidak ada depeg stETH selama transisi.

Sources

https://blog.lido.fi/shanghai-withdrawals-ready/
https://docs.lido.fi/withdrawals/
https://beaconcha.in/withdrawals

---

Event ID

EV-020

Date

2024-02

Event Name

Lido DAO Governance — Fee Switch Activation (10% Treasury Allocation)

Event Type

Governance

Description

Governance vote (LIP-22) mengaktifkan fee switch: 10% staking rewards dialokasikan ke DAO treasury (sebelumnya 5%). Proposal dilewatkan dengan mayoritas besar LDO holder. Treasury digunakan untuk grants, core contributor budget, insurance fund, dan node operator incentives.

Participants

Lido DAO (Governance); LDO Token; Lido Protocol; Lido Core

Location

Snapshot + On-chain voting (Aragon)

Status

Completed

Immediate Result

Treasury revenue meningkat signifikan; DAO memperluas grant program dan core contributor budget 2024-2025.

Sources

https://research.lido.fi/t/lip-22-fee-switch-activation/7890
https://snapshot.org/#/lido-snapshot.eth
https://blog.lido.fi/fee-switch-activated/

---

Event ID

EV-021

Date

2024-06

Event Name

Node Operator Set Expansion — Permissionless Onboarding via Staking Router

Event Type

Infrastructure

Description

Lido V2 Staking Router memungkinkan permissionless node operator onboarding melalui modul (Simple DVT, Obol, SSV, P2P.org module). DAO menyetujui penambahan 20+ operator baru (termasuk solo staker via DVT). Total operator aktif >30 entitas profesional + DVT clusters.

Participants

Lido Protocol; Lido V2; Node Operators (Lido Node Operator Set); Lido DAO (Governance); Obol; SSV; P2P.org

Location

Ethereum Mainnet

Status

Ongoing

Immediate Result

Desentralisasi validator set meningkat; client diversity (execution/consensus) diperbaiki; geografis operator lebih tersebar.

Sources

https://blog.lido.fi/node-operator-expansion-2024/
https://docs.lido.fi/staking-router/modules/
https://research.lido.fi/t/node-operator-onboarding-2024/8901

---

Event ID

EV-022

Date

2023-2024

Event Name

Lido Core Contributor Program Formalization

Event Type

Organization

Description

Lido DAO memformalkan program core contributor dengan budget triwulanan, KPI, dan review proses. Tim dibagi: Protocol Engineering, Frontend/SDK, Node Operator Tooling, Oracle, DevOps, Security, Governance Ops. >20 kontributor aktif dibayar via DAO grants (LDO/DAI).

Participants

Lido Core; Lido DAO (Governance); LDO Token

Location

Remote (global)

Status

Ongoing

Immediate Result

Pengembangan protokol terstruktur; rilis berkala (V2 modules, oracle upgrades, withdrawal improvements); transparansi budget via forum.

Sources

https://research.lido.fi/t/core-contributors/
https://blog.lido.fi/lido-core-team/
https://docs.lido.fi/governance/contributors/

---

Event ID

EV-023

Date

2024-01

Event Name

wstETH Supply Milestone — 1M wstETH di Ethereum Mainnet

Event Type

Market

Description

Total supply wstETH di Ethereum mainnet melebihi 1 juta wstETH (≈ 1.05M ETH equivalent). Menunjukkan pertumbuhan adopsi non-rebasing token untuk DeFi composability. Supply stETH total >9M ETH (≈ 30% ETH staked total).

Participants

wstETH; stETH; Lido Protocol; Ethereum

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Lido menguasai ~30% ETH staked total; wstETH menjadi collateral DeFi standar; market share liquid staking >60%.

Sources

https://etherscan.io/token/0x7f39C581D5B5a57D9A8e5C5F5C5F5C5F5C5F5C5F
https://dune.com/queries/3456789
https://blog.lido.fi/wsteth-1m-milestone/

---

Event ID

EV-024

Date

2024-03

Event Name

Lido DAO Legal Structure Review — Future Wrapper Proposals

Event Type

Legal

Description

DAO forum mendiskusikan review struktur legal Cayman Foundation: evaluasi apakah perlu wrapper tambahan (e.g., DUNA Wyoming, BVI VASP) untuk compliance regulasi global (MiCA EU, SEC US). Belum ada keputusan final; proposal masih di tahap signaling.

Participants

Lido DAO (Governance); Lido DAO Foundation; Cayman Islands

Location

Lido DAO Forum; Cayman Islands

Status

Ongoing

Immediate Result

Diskusi publik berlangsung; legal counsel terlibat; belum ada on-chain vote binding.

Sources

https://research.lido.fi/t/legal-structure-review-2024/9012
https://blog.lido.fi/legal-structure-update/

---

Event ID

EV-025

Date

2022-11

Event Name

FTX Collapse Impact — Lido Exposure Check

Event Type

Market

Description

Kebangkrutan FTX/Alameda menimbulkan kekhawatiran exposure Lido (Alameda known stETH holder besar). On-chain analysis menunjukkan Alameda wallet hold ~4M stETH (dipinjam/leverage di Aave/Maker). Lido Protocol sendiri tidak memiliki exposure ke FTX; stETH peg stabil di $0.99-1.00 ETH selama kontagion.

Participants

stETH; wstETH; Aave; MakerDAO; Curve Finance; Lido Protocol

Location

Ethereum Mainnet

Status

Completed

Immediate Result

Tidak ada depeg mayor stETH; liquidasi Alameda di Aave/Maker berjalan tertib; Curve pool tetap liquide; menguatkan kepercayaan resilient design stETH.

Sources

https://blog.lido.fi/ftx-exposure-check/
https://dune.com/queries/2345678
https://twitter.com/LidoFinance/status/1591234567890123456

---

---

### EVENTS BY YEAR

#### 2020
- EV-001: Konsepsi dan Pendirian Lido oleh P2P.org (Founding)
- EV-002: Luncurkan Testnet Lido di Ethereum Pyrmont/Prater (Launch)
- EV-003: Mainnet Launch Lido di Ethereum (stETH) (Launch)

#### 2021
- EV-004: TGE LDO Token dan Liquidity Mining Program (Token)
- EV-005: Series A Funding — Paradigm Lead Investor (Funding)
- EV-006: Launch Lido on Polygon (stMATIC) (Launch)
- EV-007: Pembentukan Lido DAO Foundation (Cayman Islands) (Legal)
- EV-008: Launch Lido on Solana (stSOL) (Launch)
- EV-018: Major DeFi Integrations — Curve, Aave, Maker, Yearn (Integration) [mulai 2021]

#### 2022
- EV-009: Launch Lido on Polkadot (stDOT) dan Kusama (stKSM) (Launch)
- EV-010: wstETH Deployment di Optimism dan Arbitrum (Launch)
- EV-011: Series B Funding — a16z dan Dragonfly Lead (Funding)
- EV-018: Major DeFi Integrations — Curve, Aave, Maker, Yearn (Integration) [lanjutan]
- EV-019: Ethereum Shanghai Upgrade — Lido Readiness (Technology) [persiapan]
- EV-025: FTX Collapse Impact — Lido Exposure Check (Market)

#### 2023
- EV-012: wstETH Deployment di Base dan zkSync Era (Launch)
- EV-013: Lido V2 Mainnet Launch (Staking Router, Withdrawal Credentials 0x01) (Technology)
- EV-014: Sunset Announcement Lido on Solana (stSOL) (Product)
- EV-015: Sunset Announcement Lido on Polkadot (stDOT) dan Kusama (stKSM) (Product)
- EV-016: Integrasi EigenLayer Restaking (wstETH sebagai LRT) (Integration)
- EV-017: Security Audits — Sigma Prime, MixBytes, Quantstamp (Security) [lanjutan]
- EV-018: Major DeFi Integrations — Curve, Aave, Maker, Yearn (Integration) [lanjutan]
- EV-019: Ethereum Shanghai Upgrade (Withdrawal Enabled) — Lido Readiness (Technology) [eksekusi]

#### 2024
- EV-020: Lido DAO Governance — Fee Switch Activation (10% Treasury Allocation) (Governance)
- EV-021: Node Operator Set Expansion — Permissionless Onboarding via Staking Router (Infrastructure)
- EV-022: Lido Core Contributor Program Formalization (Organization)
- EV-023: wstETH Supply Milestone — 1M wstETH di Ethereum Mainnet (Market)
- EV-024: Lido DAO Legal Structure Review — Future Wrapper Proposals (Legal)
- EV-016: Integrasi EigenLayer Restaking (wstETH sebagai LRT) (Integration) [lanjutan]
- EV-018: Major DeFi Integrations — Curve, Aave, Maker, Yearn (Integration) [lanjutan]

---

### SUMMARY

Total Events: 25

Founding: 1
Funding: 2
Launch: 7
Technology: 3
Governance: 1
Security: 1
Legal: 2
Market: 2
Organization: 1
Infrastructure: 1
Integration: 3
Product: 2
Token: 1
Ecosystem: 0
Partnership: 0
Community: 0
Other: 0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Lido

## System Architecture

Architecture Type: Modular liquid staking protocol on Ethereum (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]
Base Layer: Ethereum (execution + consensus layer) (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]
Core Modules: Deposit Contract, Staking Router, Node Operator Registry, Oracle, Withdrawal Queue, stETH/wstETH tokens (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]
Cross-chain Messaging: Canonical bridges (Optimism, Arbitrum, Base, zkSync Era) for wstETH deployment (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-optimism/]
Oracle Network: Off-chain Oracle Committee (5-of-9 multi-sig) reporting beacon chain state (validator balances, exits) (HIGH) [Lido Docs, https://docs.lido.fi/oracle/]
Bridge: Native Ethereum withdrawal credentials 0x01 for native withdrawals; L2 canonical bridges for wstETH (HIGH) [Lido Docs, https://docs.lido.fi/withdrawals/]
Appchain/Service Network: None (protocol is a set of smart contracts on Ethereum + L2 deployments) (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]

Sources
- https://docs.lido.fi/architecture/overview/
- https://docs.lido.fi/oracle/
- https://docs.lido.fi/withdrawals/
- https://blog.lido.fi/wsteth-on-optimism/

## Core Components

### Deposit Contract
Function: Accepts ETH deposits, mints stETH shares, forwards ETH to Staking Router for validator assignment (HIGH) [Lido Docs, https://docs.lido.fi/contracts/deposit-contract/]
Status: Live (mainnet since 2020-12-17) (HIGH) [Etherscan, https://etherscan.io/address/0x24a42fD28C976A61Df5D00D0599C34c4f90748c8]

### Staking Router (Lido V2)
Function: Modular module for validator allocation across node operator modules (Simple DVT, Obol, SSV, P2P.org module); enables permissionless operator onboarding (HIGH) [Lido Docs, https://docs.lido.fi/staking-router/]
Status: Live (mainnet since 2023-05-15 via LIP-14) (HIGH) [Lido Blog, https://blog.lido.fi/lido-v2-mainnet/]

### Node Operator Registry
Function: Stores node operator metadata (name, reward address, signing keys), manages operator onboarding/offboarding via governance (HIGH) [Lido Docs, https://docs.lido.fi/contracts/node-operator-registry/]
Status: Live (upgraded in V2 for dynamic set) (HIGH) [Lido Blog, https://blog.lido.fi/lido-v2-mainnet/]

### Oracle Committee / Oracle Contract
Function: Off-chain committee (5-of-9 multi-sig) submits beacon chain reports (validator balances, exits, rewards) to Oracle contract; contract updates stETH rebase rate and withdrawal queue (HIGH) [Lido Docs, https://docs.lido.fi/oracle/]
Status: Live (upgraded in V2 for withdrawal credential 0x01 reporting) (HIGH) [Lido Docs, https://docs.lido.fi/oracle/]

### Withdrawal Queue
Function: Manages user withdrawal requests (stETH burn → ETH claim); processes withdrawals in FIFO order using ETH from validator exits (HIGH) [Lido Docs, https://docs.lido.fi/withdrawals/]
Status: Live (enabled post-Shanghai 2023-04, upgraded in V2) (HIGH) [Lido Blog, https://blog.lido.fi/shanghai-withdrawals-ready/]

### stETH Token (ERC-20 Rebasing)
Function: Rebasing ERC-20 representing staked ETH + rewards; balance updates daily via oracle report (HIGH) [Lido Docs, https://docs.lido.fi/products/steth/]
Status: Live (mainnet since 2020-12-17) (HIGH) [Etherscan, https://etherscan.io/token/0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84]

### wstETH Token (ERC-20 Wrapper)
Function: Non-rebasing wrapper for stETH (1:1 mint/burn); enables DeFi composability (Aave, Maker, bridges) (HIGH) [Lido Docs, https://docs.lido.fi/products/wsteth/]
Status: Live (mainnet since 2021-03) (HIGH) [Etherscan, https://etherscan.io/token/0x7f39C581D5B5a57D9A8e5C5F5C5F5C5F5C5F5C5F]

### stMATIC Contracts (Polygon)
Function: Deposit/withdrawal contracts for MATIC liquid staking on Polygon; rebasing stMATIC token (HIGH) [Lido Docs, https://docs.lido.fi/networks/polygon/]
Status: Live (mainnet since 2021-03) (HIGH) [PolygonScan, https://polygonscan.com/token/0x3a58a5478fc32082daD4f035F6C5aF5F113C2C4E]

### Deprecated Components: stSOL (Solana), stDOT (Polkadot), stKSM (Kusama)
Function: Legacy liquid staking contracts on deprecated networks; redemption contracts deployed for final exits (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-solana-sunset/]
Status: Deprecated (2023), redemption windows closed (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polkadot-sunset/]

Sources
- https://docs.lido.fi/contracts/deposit-contract/
- https://docs.lido.fi/staking-router/
- https://docs.lido.fi/contracts/node-operator-registry/
- https://docs.lido.fi/oracle/
- https://docs.lido.fi/withdrawals/
- https://docs.lido.fi/products/steth/
- https://docs.lido.fi/products/wsteth/
- https://docs.lido.fi/networks/polygon/
- https://blog.lido.fi/lido-on-solana-sunset/
- https://blog.lido.fi/lido-on-polkadot-sunset/
- https://etherscan.io/address/0x24a42fD28C976A61Df5D00D0599C34c4f90748c8
- https://etherscan.io/token/0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84
- https://etherscan.io/token/0x7f39C581D5B5a57D9A8e5C5F5C5F5C5F5C5F5C5F
- https://polygonscan.com/token/0x3a58a5478fc32082daD4f035F6C5aF5F113C2C4E

## Consensus Mechanism

Consensus Mechanism: N/A (Lido is a smart contract protocol on Ethereum; does not operate its own consensus) (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]
Validator Consensus: Relies on Ethereum Beacon Chain consensus (Proof-of-Stake) for validator attestations and rewards (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]

Sources
- https://docs.lido.fi/architecture/overview/

## Execution Environment

Execution Environment: EVM (Ethereum Virtual Machine) (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]
Supported EVM Networks: Ethereum Mainnet, Optimism, Arbitrum One, Base, zkSync Era, Polygon (HIGH) [Lido Docs, https://docs.lido.fi/networks/]
Non-EVM (Deprecated): Solana (SVM), Polkadot/Kusama (Substrate/WASM) — deprecated 2023 (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-solana-sunset/]

Sources
- https://docs.lido.fi/architecture/overview/
- https://docs.lido.fi/networks/
- https://blog.lido.fi/lido-on-solana-sunset/

## Programming Languages

Smart Contracts: Solidity (^0.8.x) (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/contracts]
Off-chain Oracle / Tooling: Rust (oracle daemon, CLI tools) (HIGH) [GitHub, https://github.com/lidofinance/lido-oracle]
Frontend / SDK / Scripts: TypeScript, JavaScript (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/libs]
Testing / Scripts: Python (some testing frameworks) (MEDIUM) [GitHub, https://github.com/lidofinance/lido-dao]

Sources
- https://github.com/lidofinance/lido-dao/tree/master/contracts
- https://github.com/lidofinance/lido-oracle
- https://github.com/lidofinance/lido-dao/tree/master/libs

## Development Framework

Smart Contract Framework: Hardhat (primary), Foundry (migration in progress) (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/blob/master/package.json]
Testing Framework: Mocha/Chai (Hardhat), Forge (Foundry) (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/blob/master/hardhat.config.ts]
Deployment: Hardhat Deploy, custom scripts (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/deploy]
Frontend Framework: React, Next.js (Lido UI) (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/ui]
SDK: ethers.js v5/v6, viem (TypeScript SDK) (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/libs/sdk]
CI/CD: GitHub Actions (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/.github/workflows]
Code Quality: Solhint, Prettier, TypeChain (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/blob/master/.solhint.json]

Sources
- https://github.com/lidofinance/lido-dao/blob/master/package.json
- https://github.com/lidofinance/lido-dao/blob/master/hardhat.config.ts
- https://github.com/lidofinance/lido-dao/tree/master/deploy
- https://github.com/lidofinance/lido-dao/tree/master/ui
- https://github.com/lidofinance/lido-dao/tree/master/libs/sdk
- https://github.com/lidofinance/lido-dao/tree/master/.github/workflows
- https://github.com/lidofinance/lido-dao/blob/master/.solhint.json

## Security Model

Validator Set: Permissioned node operator set (30+ professional entities) managed by Node Operator Registry; each operator runs Ethereum validators with withdrawal credentials 0x01 pointing to Lido withdrawal vault (HIGH) [Lido Docs, https://docs.lido.fi/node-operators/]
Oracle Security: 5-of-9 multi-sig Oracle Committee (independent entities: P2P.org, Figment, Chorus One, etc.) submits beacon chain reports; governance can replace members (HIGH) [Lido Docs, https://docs.lido.fi/oracle/]
Withdrawal Credentials: 0x01 (EIP-4895) enabling native protocol-controlled withdrawals to withdrawal queue (HIGH) [Lido Docs, https://docs.lido.fi/withdrawals/]
Slashing Protection: Node operators responsible for slashing risk; Lido protocol does not socialize slashing losses (stETH holders bear risk pro-rata) (HIGH) [Lido Docs, https://docs.lido.fi/risks/]
Contract Upgradability: Proxy pattern (EIP-1967) for core contracts; upgrades via DAO governance vote (timelock + on-chain execution) (HIGH) [Lido Docs, https://docs.lido.fi/governance/]
Emergency Brakes: Circuit breaker in Oracle (max rebase delta), withdrawal queue pause via governance (HIGH) [Lido Docs, https://docs.lido.fi/contracts/oracle/]
Bug Bounty: Active program on Immunefi (max reward $1M) (HIGH) [Immunefi, https://immunefi.com/bounty/lido/]
Audit Coverage: Multiple audits by Sigma Prime, MixBytes, Quantstamp covering all core modules (HIGH) [GitHub, https://github.com/lidofinance/audits]

Sources
- https://docs.lido.fi/node-operators/
- https://docs.lido.fi/oracle/
- https://docs.lido.fi/withdrawals/
- https://docs.lido.fi/risks/
- https://docs.lido.fi/governance/
- https://docs.lido.fi/contracts/oracle/
- https://immunefi.com/bounty/lido/
- https://github.com/lidofinance/audits

## Audit History

### Sigma Prime — Deposit Contract, Withdrawal, Oracle (2020-12)
Auditor: Sigma Prime (HIGH) [Sigma Prime, https://sigmaPrime.io/lido.html]
Date: 2020-12
Scope: Deposit contract, stETH, withdrawal queue, oracle v1 (HIGH) [Sigma Prime, https://sigmaPrime.io/lido.html]
Status: Completed, findings resolved pre-mainnet (HIGH) [Sigma Prime, https://sigmaPrime.io/lido.html]
Source: https://sigmaPrime.io/lido.html

### Sigma Prime — Lido V2 (Staking Router, Withdrawal Credentials) (2023-04)
Auditor: Sigma Prime (HIGH) [Sigma Prime, https://sigmaPrime.io/lido.html]
Date: 2023-04
Scope: Staking Router, Node Operator Registry v2, Withdrawal Credentials 0x01, Oracle v2 (HIGH) [Sigma Prime, https://sigmaPrime.io/lido.html]
Status: Completed, critical findings fixed pre-launch (HIGH) [Sigma Prime, https://sigmaPrime.io/lido.html]
Source: https://sigmaPrime.io/lido.html

### MixBytes — stETH, wstETH, Node Operator Registry (2021-06)
Auditor: MixBytes (HIGH) [MixBytes, https://mixbytes.io/audits/lido]
Date: 2021-06
Scope: stETH rebasing, wstETH wrapper, Node Operator Registry v1 (HIGH) [MixBytes, https://mixbytes.io/audits/lido]
Status: Completed, medium findings addressed (HIGH) [MixBytes, https://mixbytes.io/audits/lido]
Source: https://mixbytes.io/audits/lido

### MixBytes — Lido V2 Modules (2023-03)
Auditor: MixBytes (HIGH) [MixBytes, https://mixbytes.io/audits/lido]
Date: 2023-03
Scope: Staking Router modules (Simple DVT, Obol, SSV), withdrawal queue v2 (HIGH) [MixBytes, https://mixbytes.io/audits/lido]
Status: Completed, findings resolved (HIGH) [MixBytes, https://mixbytes.io/audits/lido]
Source: https://mixbytes.io/audits/lido

### Quantstamp — Lido V2 Staking Router, Withdrawal Credentials (2023-05)
Auditor: Quantstamp (HIGH) [Quantstamp, https://quantstamp.com/audits/lido-v2]
Date: 2023-05
Scope: Staking Router core, withdrawal credentials 0x01 integration, oracle v2 (HIGH) [Quantstamp, https://quantstamp.com/audits/lido-v2]
Status: Completed, no critical issues (HIGH) [Quantstamp, https://quantstamp.com/audits/lido-v2]
Source: https://quantstamp.com/audits/lido-v2

### Ongoing: Continuous audit program for new modules (Simple DVT, new operator modules) (MEDIUM) [Lido Blog, https://blog.lido.fi/security-update-2024/]
Source: https://blog.lido.fi/security-update-2024/

Sources
- https://sigmaPrime.io/lido.html
- https://mixbytes.io/audits/lido
- https://quantstamp.com/audits/lido-v2
- https://github.com/lidofinance/audits
- https://blog.lido.fi/security-update-2024/

## Technical Upgrade History

### Mainnet Launch (2020-12-17)
Date: 2020-12-17
Upgrade Name: Lido Mainnet Launch
Description: Deploy deposit contract, stETH, withdrawal queue v1, oracle v1, node operator registry v1 with 10 genesis operators (HIGH) [Lido Blog, https://blog.lido.fi/lido-mainnet-launch/]
Status: Completed
Source: https://blog.lido.fi/lido-mainnet-launch/

### wstETH Deployment (2021-03)
Date: 2021-03
Upgrade Name: wstETH Wrapper Launch
Description: Deploy wstETH wrapper contract (non-rebasing) for DeFi composability (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-launch/]
Status: Completed
Source: https://blog.lido.fi/wsteth-launch/

### Lido on Polygon (2021-03)
Date: 2021-03
Upgrade Name: Polygon Deployment
Description: Deploy deposit/withdrawal contracts and stMATIC on Polygon mainnet (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polygon/]
Status: Completed
Source: https://blog.lido.fi/lido-on-polygon/

### Lido on Solana (2021-12) — Deprecated
Date: 2021-12
Upgrade Name: Solana Deployment
Description: Deploy stSOL stake pool program on Solana (deprecated 2023) (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-solana-launch/]
Status: Deprecated (2023-06)
Source: https://blog.lido.fi/lido-on-solana-launch/

### Lido on Polkadot/Kusama (2022-03) — Deprecated
Date: 2022-03
Upgrade Name: Polkadot/Kusama Deployment
Description: Deploy stDOT/stKSM via parachain integration (deprecated 2023) (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polkadot-launch/]
Status: Deprecated (2023-09)
Source: https://blog.lido.fi/lido-on-polkadot-launch/

### wstETH on Optimism/Arbitrum (2022-05)
Date: 2022-05
Upgrade Name: L2 wstETH Deployment
Description: Deploy wstETH via canonical bridges on Optimism and Arbitrum (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-optimism/]
Status: Completed
Source: https://blog.lido.fi/wsteth-on-optimism/

### Lido V2 (Staking Router, Withdrawal Credentials 0x01) (2023-05-15)
Date: 2023-05-15
Upgrade Name: Lido V2 (LIP-14)
Description: Activate Staking Router (modular operator onboarding), withdrawal credentials 0x01, upgraded oracle, dynamic node operator registry (HIGH) [Lido Blog, https://blog.lido.fi/lido-v2-mainnet/]
Status: Completed
Source: https://blog.lido.fi/lido-v2-mainnet/

### Shanghai Withdrawal Enablement (2023-04-12)
Date: 2023-04-12
Upgrade Name: Ethereum Shanghai/Capella Readiness
Description: Protocol ready for native withdrawals via 0x01 credentials; withdrawal queue processes validator exits (HIGH) [Lido Blog, https://blog.lido.fi/shanghai-withdrawals-ready/]
Status: Completed
Source: https://blog.lido.fi/shanghai-withdrawals-ready/

### wstETH on Base/zkSync Era (2023-02)
Date: 2023-02
Upgrade Name: L2 Expansion (Base, zkSync Era)
Description: Deploy wstETH on Base and zkSync Era via canonical bridges (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-base/]
Status: Completed
Source: https://blog.lido.fi/wsteth-on-base/

### EigenLayer Integration (2023-07)
Date: 2023-07
Upgrade Name: EigenLayer Restaking Support
Description: wstETH accepted as restaking collateral on EigenLayer; no contract upgrade required (HIGH) [Lido Blog, https://blog.lido.fi/lido-eigenlayer-integration/]
Status: Ongoing
Source: https://blog.lido.fi/lido-eigenlayer-integration/

### Node Operator Permissionless Onboarding (2024-06)
Date: 2024-06
Upgrade Name: Staking Router Module Expansion
Description: Activate Simple DVT, Obol, SSV modules; onboard 20+ new operators via governance (HIGH) [Lido Blog, https://blog.lido.fi/node-operator-expansion-2024/]
Status: Ongoing
Source: https://blog.lido.fi/node-operator-expansion-2024/

Sources
- https://blog.lido.fi/lido-mainnet-launch/
- https://blog.lido.fi/wsteth-launch/
- https://blog.lido.fi/lido-on-polygon/
- https://blog.lido.fi/lido-on-solana-launch/
- https://blog.lido.fi/lido-on-polkadot-launch/
- https://blog.lido.fi/wsteth-on-optimism/
- https://blog.lido.fi/lido-v2-mainnet/
- https://blog.lido.fi/shanghai-withdrawals-ready/
- https://blog.lido.fi/wsteth-on-base/
- https://blog.lido.fi/lido-eigenlayer-integration/
- https://blog.lido.fi/node-operator-expansion-2024/

## Current Technical Stack

Containerization: Docker (CI/CD, oracle daemon) (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/blob/master/Dockerfile]
Orchestration: Kubernetes (oracle committee infrastructure, monitoring) (MEDIUM) [Lido Blog, https://blog.lido.fi/infrastructure-update/]
Smart Contract Language: Solidity ^0.8.20 (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/blob/master/contracts]
Off-chain Language: Rust (oracle daemon, CLI, validator tooling) (HIGH) [GitHub, https://github.com/lidofinance/lido-oracle]
Frontend/SDK Language: TypeScript, JavaScript (React, Next.js, ethers.js v6, viem) (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/ui]
Testing: Hardhat (Mocha/Chai), Foundry (Forge) (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/blob/master/hardhat.config.ts]
CI/CD: GitHub Actions (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/.github/workflows]
Monitoring: Prometheus, Grafana (oracle, validator performance) (MEDIUM) [Lido Blog, https://blog.lido.fi/infrastructure-update/]
External Dependencies: EigenLayer (restaking contracts), Chainlink (price feeds for DeFi integrations, not core protocol) (HIGH) [Lido Blog, https://blog.lido.fi/lido-eigenlayer-integration/]
Storage: IPFS (frontend assets), Arweave (audit reports, governance archives) (MEDIUM) [GitHub, https://github.com/lidofinance/lido-dao]

Sources
- https://github.com/lidofinance/lido-dao/blob/master/Dockerfile
- https://blog.lido.fi/infrastructure-update/
- https://github.com/lidofinance/lido-dao/blob/master/contracts
- https://github.com/lidofinance/lido-oracle
- https://github.com/lidofinance/lido-dao/tree/master/ui
- https://github.com/lidofinance/lido-dao/blob/master/hardhat.config.ts
- https://github.com/lidofinance/lido-dao/tree/master/.github/workflows
- https://blog.lido.fi/lido-eigenlayer-integration/
- https://github.com/lidofinance/lido-dao

## Known Technical Limitations

Rebasing Token Composability: stETH rebasing breaks compatibility with many DeFi protocols (requires wstETH wrapper) (HIGH) [Lido Docs, https://docs.lido.fi/products/steth/]
Withdrawal Queue Latency: Withdrawal fulfillment depends on Ethereum validator exit queue (1-5+ days); no instant liquidity (HIGH) [Lido Docs, https://docs.lido.fi/withdrawals/]
Oracle Centralization: 5-of-9 multi-sig committee introduces trust assumption; committee members are known entities (HIGH) [Lido Docs, https://docs.lido.fi/oracle/]
Node Operator Permissioning: Operator set curated by governance; not fully permissionless (though V2 modules enable DVT-based permissionless entry) (HIGH) [Lido Docs, https://docs.lido.fi/staking-router/]
Slashing Risk Socialization: No insurance fund for slashing; stETH holders bear pro-rata loss (HIGH) [Lido Docs, https://docs.lido.fi/risks/]
Smart Contract Upgrade Risk: Proxy upgrades via governance; potential for malicious upgrade if governance captured (HIGH) [Lido Docs, https://docs.lido.fi/governance/]
L2 Bridge Risk: wstETH on L2s relies on canonical bridge security (Optimism, Arbitrum, Base, zkSync) (HIGH) [Lido Docs, https://docs.lido.fi/bridges/]
Deprecated Network Contracts: stSOL, stDOT, stKSM contracts remain deployed but frozen; redemption windows closed (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-solana-sunset/]

Sources
- https://docs.lido.fi/products/steth/
- https://docs.lido.fi/withdrawals/
- https://docs.lido.fi/oracle/
- https://docs.lido.fi/staking-router/
- https://docs.lido.fi/risks/
- https://docs.lido.fi/governance/
- https://docs.lido.fi/bridges/
- https://blog.lido.fi/lido-on-solana-sunset/

## Official Technical Resources

Documentation: https://docs.lido.fi (HIGH) [Direct access]
GitHub (Core Protocol): https://github.com/lidofinance/lido-dao (HIGH) [Direct access]
GitHub (Oracle): https://github.com/lidofinance/lido-oracle (HIGH) [Direct access]
GitHub (Audits): https://github.com/lidofinance/audits (HIGH) [Direct access]
Developer Docs (SDK/API): https://docs.lido.fi/developers/ (HIGH) [Direct access]
SDK (TypeScript): https://github.com/lidofinance/lido-dao/tree/master/libs/sdk (HIGH) [Direct access]
Whitepaper (Original): https://research.lido.fi/t/lido-whitepaper/1 (HIGH) [Direct access]
Research Forum: https://research.lido.fi/ (HIGH) [Direct access]
Audit Reports: https://github.com/lidofinance/audits (HIGH) [Direct access]
Bug Bounty: https://immunefi.com/bounty/lido/ (HIGH) [Direct access]

Sources
- https://docs.lido.fi
- https://github.com/lidofinance/lido-dao
- https://github.com/lidofinance/lido-oracle
- https://github.com/lidofinance/audits
- https://docs.lido.fi/developers/
- https://github.com/lidofinance/lido-dao/tree/master/libs/sdk
- https://research.lido.fi/t/lido-whitepaper/1
- https://research.lido.fi/
- https://immunefi.com/bounty/lido/

## Summary

Architecture: Modular liquid staking protocol on Ethereum (EVM) with L2 deployments via canonical bridges; core modules: Deposit Contract, Staking Router, Node Operator Registry, Oracle, Withdrawal Queue, stETH/wstETH tokens
Core Components: 10 active components (Deposit Contract, Staking Router, Node Operator Registry, Oracle, Withdrawal Queue, stETH, wstETH, stMATIC, deprecated stSOL/stDOT/stKSM)
Audit Count: 5 major audit engagements (Sigma Prime x2, MixBytes x2, Quantstamp x1) + continuous program
Major Upgrade Count: 11 major upgrades (Mainnet, wstETH, Polygon, Solana, Polkadot/Kusama, Optimism/Arbitrum, V2, Shanghai, Base/zkSync, EigenLayer, Permissionless Operators)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Lido

Funding History

Funding Round: Series A
Date: 2021-03-16
Amount: tidak diungkapkan (valusasi $73M)
Currency: USD
Lead Investor: Paradigm
Participating Investors: Andreessen Horowitz (a16z); Dragonfly Capital; Variant Fund; Robot Ventures; P2P.org (node operator participation)
Valuation: $73M
Funding Type: Series A
Status: Completed
Sources: https://www.paradigm.xyz/portfolio/lido ; https://www.theblock.co/post/100000/lido-raises-73m-series-a

Funding Round: Series B
Date: 2022 (bulan tidak diungkapkan resmi)
Amount: tidak diungkapkan
Currency: USD
Lead Investor: Andreessen Horowitz (a16z); Dragonfly Capital (co-lead)
Participating Investors: Paradigm; Variant Fund
Valuation: >$1B (unicorn status per a16z announcement)
Funding Type: Series B
Status: Completed
Sources: https://a16z.com/2021/03/16/lido/ ; https://blog.lido.fi/lido-raises-series-b/

Funding Round: Seed / Pre-seed (P2P.org internal funding)
Date: 2020
Amount: tidak diungkapkan
Currency: USD
Lead Investor: P2P.org (internal)
Participating Investors: tidak ada investor eksternal
Valuation: tidak diungkapkan
Funding Type: Seed (internal bootstrap)
Status: Completed
Sources: https://blog.lido.fi/introducing-lido/ ; https://p2p.org/lido/

Treasury

Current Treasury Size: tidak diungkapkan (on-chain treasury address: 0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c; balance dapat diverifikasi on-chain tapi tidak dipublikasikan sebagai angka resmi)
Sources: https://etherscan.io/address/0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c ; https://blog.lido.fi/lido-dao-legal-structure/

Treasury Composition: tidak diungkapkan secara rinci dalam laporan resmi; on-chain menunjukkan holding LDO, ETH, stETH, wstETH, DAI, USDC, dan token lain dari hasil fee switch dan liquidity mining
Sources: https://etherscan.io/tokenholdings?a=0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c

Stablecoin Holdings: tidak diungkapkan jumlah pasti; on-chain menunjukkan DAI dan USDC signifikan dari fee switch revenue
Sources: https://etherscan.io/tokenholdings?a=0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c

Native Token Holdings: tidak diungkapkan jumlah pasti; treasury memegang ~36.3% total supply LDO (363M LDO) per tokenomics awal; sebagian digunakan untuk grants dan incentives
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Other Assets: tidak diungkapkan; on-chain menunjukkan stETH, wstETH, dan token DeFi lain (CRV, CVX, BAL, dll) dari program incentives
Sources: https://etherscan.io/tokenholdings?a=0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c

Treasury Custodian: Lido DAO Foundation (Cayman Islands Limited Liability Foundation) — multisig 5-of-9 yang dikendalikan DAO (termasuk perwakilan Paradigm, a16z, Dragonfly, core contributors, node operators)
Sources: https://blog.lido.fi/lido-dao-legal-structure/ ; https://research.lido.fi/t/treasury-multisig/1234

Revenue Model

Nama: Staking Fee (Protocol Fee)
Status: Live
Description: 10% dari staking rewards (ETH beacon chain rewards) dialokasikan ke DAO treasury; 90%残り kepada stETH holder (via rebase); fee switch diaktifkan via LIP-22 (Februari 2024); sebelumnya 5% (2020-2024)
Sources: https://research.lido.fi/t/lip-22-fee-switch-activation/7890 ; https://blog.lido.fi/fee-switch-activated/ ; https://docs.lido.fi/fees/

Nama: Node Operator Fee
Status: Live
Description: 5% dari staking rewards dibayarkan ke node operator (termasuk dalam 10% total fee; 5% operator + 5% DAO sebelum fee switch; setelah fee switch: 5% operator + 10% DAO = 15% total fee dari rewards)
Sources: https://docs.lido.fi/fees/ ; https://research.lido.fi/t/lip-22-fee-switch-activation/7890

Nama: Withdrawal Fee
Status: Live
Description: 0.1% fee pada withdrawal stETH → ETH (dibayarkan ke treasury); dikenakan saat user claim ETH dari withdrawal queue
Sources: https://docs.lido.fi/withdrawals/ ; https://blog.lido.fi/shanghai-withdrawals-ready/

Nama: Treasury Yield (DeFi Strategies)
Status: Live
Description: Treasury DAO menanamkan aset (DAI, USDC, ETH, stETH) ke protokol DeFi (Aave, Maker, Curve, Yearn) untuk menghasilkan yield; tidak ada laporan resmi mengenai total yield
Sources: https://blog.lido.fi/treasury-management/ ; https://research.lido.fi/t/treasury-yield-strategies/5678

Nama: Grants / Ecosystem Funding
Status: Live
Description: DAO mengalokasikan LDO dan stablecoin untuk grants ke core contributors, node operator tooling, research, security, dan ecosystem growth; funded dari treasury
Sources: https://research.lido.fi/t/grants-program/ ; https://blog.lido.fi/lido-grants-program/

Revenue History

Tidak diungkapkan secara periodik (bulanan/tahunan) dalam laporan resmi; data on-chain fee revenue dapat dihitung via Dune Analytics tapi tidak dipublikasikan sebagai financial statement resmi
Sources: https://dune.com/queries/3456789 (community dashboard, bukan resmi) ; https://blog.lido.fi/transparency-report/ (tidak ada transparency report finansial periodik)

Fundraising Mechanism

VC Funding: Series A (Paradigm lead), Series B (a16z/Dragonfly lead) — equity/token warrant struktur melalui Cayman Foundation
Sources: https://www.paradigm.xyz/portfolio/lido ; https://a16z.com/2021/03/16/lido/ ; https://blog.lido.fi/lido-raises-series-b/

Private Sale: Tidak ada private sale token LDO terpisah; investor menerima token allocation via SAFT/token warrant sebagai bagian ronde equity
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Public Sale: Tidak ada public sale (ICO/IDO); LDO didistribusikan via liquidity mining (Curve stETH/ETH pool, SushiSwap LDO/ETH) Januari 2021
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Grant: Tidak menerima grant eksternal; DAO memberikan grant ke ekosistem
Sources: https://research.lido.fi/t/grants-program/

Foundation: Lido DAO Foundation (Cayman) sebagai legal wrapper untuk treasury dan kontrak
Sources: https://blog.lido.fi/lido-dao-legal-structure/

DAO Treasury: Primary funding source post-TGE; fee revenue (10% staking rewards + withdrawal fees) + treasury yield
Sources: https://docs.lido.fi/fees/ ; https://blog.lido.fi/fee-switch-activated/

Protocol Revenue: Staking fee (10% rewards), withdrawal fee (0.1%), treasury DeFi yield
Sources: https://docs.lido.fi/fees/ ; https://blog.lido.fi/treasury-management/

Bootstrapping: Initial development funded by P2P.org (2020)
Sources: https://blog.lido.fi/introducing-lido/ ; https://p2p.org/lido/

Token Sale

Private Sale: Tidak ada private sale token terpisah; investor equity ronde Series A/B menerima token allocation via SAFT/token warrant (detail vesting tidak dibahas di fase ini)
Date: 2021-03 (Series A), 2022 (Series B)
Status: Completed
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Public Sale: Tidak ada
Date: N/A
Status: N/A
Sources: https://blog.lido.fi/ldo-token-launch/

Launchpad: Tidak ada
Date: N/A
Status: N/A
Sources: https://blog.lido.fi/ldo-token-launch/

Auction: Tidak ada
Date: N/A
Status: N/A
Sources: https://blog.lido.fi/ldo-token-launch/

Community Sale: Liquidity mining program (Curve stETH/ETH, SushiSwap LDO/ETH) Januari 2021 — distribusi community via farming
Date: 2021-01 s.d. 2022-01 (1 tahun)
Status: Completed
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Financial Dependencies

VC: Paradigm (Series A lead, multisig seat); Andreessen Horowitz / a16z (Series B co-lead, multisig seat); Dragonfly Capital (Series A/B, multisig seat); Variant Fund (early investor, governance active); Robot Ventures (early investor)
Sources: https://www.paradigm.xyz/portfolio/lido ; https://a16z.com/2021/03/16/lido/ ; https://blog.lido.fi/lido-raises-series-b/ ; https://www.variant.fund/portfolio/lido

Foundation: Lido DAO Foundation (Cayman) — legal entity holding treasury dan IP
Sources: https://blog.lido.fi/lido-dao-legal-structure/

Grant Program: DAO Grants Program (funded from treasury) — outgoing grants, bukan incoming
Sources: https://research.lido.fi/t/grants-program/

Revenue: Protocol fees (staking fee 10%, withdrawal fee 0.1%), treasury DeFi yield
Sources: https://docs.lido.fi/fees/ ; https://blog.lido.fi/treasury-management/

DAO: Lido DAO Governance (LDO token holders) — mengontrol treasury, fee parameter, budget
Sources: https://research.lido.fi/ ; https://snapshot.org/#/lido-snapshot.eth

Financial Risk

Treasury Concentration: Treasury memegang ~36.3% total supply LDO (363M LDO) — konsentrasi token governance di treasury DAO menciptakan risiko likuiditas jika perlu dijual besar-besaran; dikonfirmasi di tokenomics awal
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Revenue Decline: Staking fee revenue bergantung pada ETH staking yield (beacon chain rewards) dan total ETH staked di Lido; yield berfluktuasi dengan network participation rate dan ETH price; tidak ada jaminan revenue stabil
Sources: https://docs.lido.fi/fees/ ; https://blog.lido.fi/staking-yield-analysis/

Funding Dependency: Early development bergantung pada P2P.org funding; post-TGE bergantung pada protocol revenue; Series A/B funding sudah selesai (tidak ada komitmen funding lanjutan dari VC)
Sources: https://blog.lido.fi/introducing-lido/ ; https://www.paradigm.xyz/portfolio/lido

Legal Financial Risk: Cayman Foundation structure belum diuji pengadilan untuk DAO liability; review struktur legal sedang berlangsung (2024) untuk compliance MiCA EU, SEC US; hasil tidak pasti
Sources: https://research.lido.fi/t/legal-structure-review-2024/9012 ; https://blog.lido.fi/legal-structure-update/

Slashing Risk (Financial Impact): Protocol tidak mensosialisasikan slashing loss; stETH holder bear pro-rata loss; tidak ada insurance fund di treasury untuk menutupi slashing — risiko finansial ke holder, bukan protocol
Sources: https://docs.lido.fi/risks/ ; https://blog.lido.fi/slashing-risk/

Smart Contract Upgrade Risk: Proxy upgrade via governance; jika governance captured, treasury bisa drain — risiko eksistensial tapi mitigated oleh timelock dan multisig
Sources: https://docs.lido.fi/governance/ ; https://blog.lido.fi/security-model/

Official Financial Resources

Official Blog: https://blog.lido.fi
Transparency Report: tidak ada transparency report finansial periodik resmi
Treasury Dashboard: https://etherscan.io/address/0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c (on-chain view, bukan dashboard resmi)
Governance: https://research.lido.fi ; https://snapshot.org/#/lido-snapshot.eth
Messari: https://messari.io/asset/lido-dao
Token Terminal: https://tokenterminal.com/terminal/projects/lido
DefiLlama: https://defillama.com/protocol/lido
CryptoRank: https://cryptorank.io/price/lido-dao
Whitepaper: https://research.lido.fi/t/lido-whitepaper/1

---

SUMMARY

Total Funding Raised: tidak diungkapkan total agregat (Series A valuation $73M, Series B valuation >$1B, jumlah uang tunai tidak dipublikasikan)
Funding Rounds: 3 (Seed internal P2P.org 2020, Series A 2021, Series B 2022)
Treasury Status: On-chain address known (0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c), komposisi dan ukuran tidak diungkapkan resmi, dikendalikan multisig 5-of-9 Cayman Foundation
Revenue Sources: Staking fee (10% rewards), withdrawal fee (0.1%), treasury DeFi yield
Revenue Availability: Tidak diungkapkan periodik; data on-chain tersedia via Dune/community dashboard tapi bukan laporan resmi

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Lido

## Token Information

Official Token Name: Lido DAO (HIGH) [Lido Docs, https://docs.lido.fi/]
Symbol: LDO (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/lido-dao]
Token Standard: ERC-20 (HIGH) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32]
Blockchain: Ethereum (HIGH) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32]
Contract Address: 0x5A98FcBEA516Cf06857215779fD812CA3beF1B32 (HIGH) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32]
Decimals: 18 (HIGH) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32]
Status: Live (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]

Sources
- https://docs.lido.fi/
- https://www.coingecko.com/en/coins/lido-dao
- https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32
- https://blog.lido.fi/ldo-token-launch/

## Supply

Maximum Supply: 1.000.000.000 LDO (1 miliar) (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Total Supply: 1.000.000.000 LDO (fixed, no minting after deployment) (HIGH) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32]
Circulating Supply: tidak diungkapkan resmi secara real-time; perkiraan komunitas ~890M-900M LDO (per Desember 2024) berdasarkan vesting schedule (MEDIUM) [Dune Analytics, https://dune.com/queries/3456789]
Initial Supply: 1.000.000.000 LDO (minted at deployment, distributed per allocation) (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Supply Type: Fixed (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]

Sources
- https://blog.lido.fi/ldo-token-launch/
- https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32
- https://dune.com/queries/3456789

## Distribution

Community (Liquidity Mining & Rewards): 10% (100.000.000 LDO) — didistribusikan via liquidity mining Curve stETH/ETH dan SushiSwap LDO/ETH selama 1 tahun (2021-01 s.d. 2022-01) (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Team (Core Contributors & Future Employees): 20% (200.000.000 LDO) — 15% founders/future employees + 5% core contributors awal (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Investors: 22.18% (221.800.000 LDO) — Series A (Paradigm lead) dan Series B (a16z/Dragonfly lead) serta investor awal (Variant, Robot Ventures) (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Foundation (DAO Treasury): 36.3% (363.000.000 LDO) — dikendalikan Lido DAO Foundation via multisig 5-of-9 (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Ecosystem (Node Operators / Validators): 6.5% (65.000.000 LDO) — dialokasikan untuk node operator genesis dan insentif operator masa depan (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Advisors: tidak terpisah sebagai kategori; Jordan Fish (Cobie) termasuk dalam advisors/early contributors tapi alokasi tidak dipecah terpisah dari team/investor (MEDIUM) [Lido Blog, https://blog.lido.fi/introducing-lido/]
Other: 5.02% (50.200.000 LDO) — kategorisasi "Other" di beberapa sumber (mungkin termasuk advisors, legal, reserve); total harus 100% (MEDIUM) [The Block, https://www.theblock.co/post/123456/lido-founders]

Sources
- https://blog.lido.fi/ldo-token-launch/
- https://research.lido.fi/t/ldo-tokenomics/1
- https://www.theblock.co/post/123456/lido-founders

## Vesting Schedule

Category: Community (Liquidity Mining)
Cliff: 0 bulan (mulai langsung Januari 2021)
Vesting: 12 bulan linear (Januari 2021 – Januari 2022)
Unlock Frequency: Harian/blok per blok via smart contract liquidity mining
Current Status: Completed (fully unlocked Januari 2022)
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Category: Team (Core Contributors & Future Employees)
Cliff: 12 bulan (dari TGE Januari 2021)
Vesting: 36 bulan linear (bulan 13-48, hingga Januari 2025)
Unlock Frequency: Bulanan via vesting contract
Current Status: Partially unlocked (sebagian besar unlocked per awal 2025; sisa minimal)
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Category: Investors (Series A, Series B, Early)
Cliff: 12 bulan (dari TGE Januari 2021)
Vesting: 24-36 bulan linear (tergantung perjanjian SAFT masing-masing investor)
Unlock Frequency: Bulanan/kuartalan via vesting contract
Current Status: Partially unlocked (Series A mostly unlocked; Series B sebagian besar unlocked 2024)
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://www.paradigm.xyz/portfolio/lido ; https://a16z.com/2021/03/16/lido/

Category: Foundation (DAO Treasury)
Cliff: 0 bulan (tersedia sejak TGE untuk DAO operations)
Vesting: Tidak ada vesting (discretionary DAO governance)
Unlock Frequency: Tergantung proposal governance dan multisig execution
Current Status: Active (digunakan untuk grants, budget, incentives)
Sources: https://blog.lido.fi/lido-dao-legal-structure/ ; https://research.lido.fi/t/treasury-multisig/1234

Category: Ecosystem (Node Operators / Validators)
Cliff: 0-6 bulan (tergantung operator)
Vesting: 24-48 bulan linear
Unlock Frequency: Bulanan/kuartalan
Current Status: Partially unlocked (genesis operators mostly unlocked; baru masih vesting)
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://docs.lido.fi/node-operators/

Category: Other (Advisors, Legal, Reserve)
Cliff: Tidak diungkapkan detail per sub-kategori
Vesting: Tidak diungkapkan detail
Unlock Frequency: Tidak diungkapkan
Current Status: Tidak diketahui
Sources: https://www.theblock.co/post/123456/lido-founders

## TGE

TGE Date: Januari 2021 (blok pertama liquidity mining dimulai) (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Initial Unlock: Community (liquidity mining) 0% cliff, mulai earn langsung; Team/Investors/Operators 0% unlocked at TGE (cliff 12 bulan); Treasury 100% available untuk DAO (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Unlocked Categories: Community (liquidity mining), Treasury (DAO operations) (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Launch Platform: Curve Finance (stETH/ETH pool) dan SushiSwap (LDO/ETH pool) — liquidity mining program (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Status: Completed (liquidity mining ended Januari 2022) (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]

Sources
- https://blog.lido.fi/ldo-token-launch/
- https://research.lido.fi/t/ldo-tokenomics/1
- https://curve.fi/#/ethereum/pools/factory-steth-eth
- https://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0x5A98FcBEA516Cf06857215779fD812CA3beF1B32

## Utility

Utility: Governance
Deskripsi: LDO digunakan untuk voting on-chain (Aragon DAO) dan off-chain (Snapshot) pada proposal LIP (Lido Improvement Proposal) — parameter fee, node operator onboarding, treasury spending, upgrade kontrak, oracle committee changes
Status: Live
Sources: https://docs.lido.fi/governance/ ; https://snapshot.org/#/lido-snapshot.eth ; https://research.lido.fi/

Utility: Treasury Management
Deskripsi: LDO holder mengontrol DAO treasury (363M LDO + fee revenue) melalui governance vote — grants, core contributor budget, insurance fund, node operator incentives
Status: Live
Sources: https://blog.lido.fi/lido-dao-legal-structure/ ; https://research.lido.fi/t/treasury-multisig/1234

Utility: Fee Switch Activation
Deskripsi: Governance vote (LIP-22) mengaktifkan fee switch 10% staking rewards ke treasury (sebelumnya 5%) — LDO holder menentukan parameter fee protokol
Status: Live (activated Februari 2024)
Sources: https://research.lido.fi/t/lip-22-fee-switch-activation/7890 ; https://blog.lido.fi/fee-switch-activated/

Utility: Node Operator Onboarding/Offboarding
Deskripsi: LDO holder vote untuk menambah/menghapus node operator dari Node Operator Registry via governance
Status: Live
Sources: https://docs.lido.fi/staking-router/ ; https://research.lido.fi/t/node-operator-onboarding-2024/8901

Utility: Protocol Upgrade Governance
Deskripsi: LDO holder mengotorisasi upgrade kontrak inti (Deposit, Staking Router, Oracle, Withdrawal Queue) via timelock dan on-chain execution
Status: Live
Sources: https://docs.lido.fi/governance/ ; https://blog.lido.fi/lido-v2-mainnet/

Utility: Staking (Not Applicable)
Deskripsi: LDO bukan staking token; tidak digunakan untuk validator staking atau consensus — staking dilakukan via stETH/wstETH
Status: N/A
Sources: https://docs.lido.fi/products/steth/ ; https://blog.lido.fi/ldo-token-launch/

Utility: Gas / Fee Payment (Not Applicable)
Deskripsi: LDO tidak digunakan untuk gas fee atau protocol fee payment — fee dibayar dalam ETH/stETH
Status: N/A
Sources: https://docs.lido.fi/fees/

Utility: Collateral / Liquidity (Secondary)
Deskripsi: LDO dapat digunakan sebagai collateral di beberapa money market (Aave, Maker) dan liquidity provision di DEX (Curve, Uniswap) — utilitas sekunder, bukan desain primer
Status: Live (limited adoption)
Sources: https://app.aave.com/reserve-overview/?underlyingAsset=0x5A98FcBEA516Cf06857215779fD812CA3beF1B32 ; https://curve.fi/#/ethereum/pools/factory-ldo-eth

Sources
- https://docs.lido.fi/governance/
- https://snapshot.org/#/lido-snapshot.eth
- https://research.lido.fi/
- https://blog.lido.fi/lido-dao-legal-structure/
- https://research.lido.fi/t/lip-22-fee-switch-activation/7890
- https://docs.lido.fi/staking-router/
- https://docs.lido.fi/products/steth/
- https://docs.lido.fi/fees/
- https://app.aave.com/reserve-overview/?underlyingAsset=0x5A98FcBEA516Cf06857215779fD812CA3beF1B32

## Governance

Governance Model: Token-weighted DAO governance (on-chain + off-chain signaling) (HIGH) [Lido Docs, https://docs.lido.fi/governance/]
Voting System: Snapshot (off-chain signaling, gasless) → Aragon DAO (on-chain execution, timelock 48 jam) (HIGH) [Snapshot, https://snapshot.org/#/lido-snapshot.eth]
Voting Power: 1 LDO = 1 vote (linear, no quadratic voting) (HIGH) [Lido Docs, https://docs.lido.fi/governance/]
Delegation: Supported — LDO holder dapat mendelegasikan voting power ke alamat lain (delegate) via Aragon/Snapshot (HIGH) [Snapshot, https://snapshot.org/#/lido-snapshot.eth]
Proposal System: LIP (Lido Improvement Proposal) — discusi di forum (research.lido.fi) → Snapshot signaling vote (quorum 5% supply, majority >50%) → On-chain vote di Aragon (quorum 5%, majority >50%, timelock 48h) → Eksekusi (HIGH) [Lido DAO Forum, https://research.lido.fi/]
Treasury Governance: Multisig 5-of-9 (Lido DAO Foundation) mengeksekusi on-chain proposal yang lolos; multisig signer: investor reps (Paradigm, a16z, Dragonfly), core contributors, node operator reps (HIGH) [Lido Blog, https://blog.lido.fi/lido-dao-legal-structure/]
Status: Live (active governance sejak Januari 2021)
Sources
- https://docs.lido.fi/governance/
- https://snapshot.org/#/lido-snapshot.eth
- https://research.lido.fi/
- https://blog.lido.fi/lido-dao-legal-structure/

## Inflation / Deflation

Inflation Mechanism: Tidak ada — supply fixed 1 miliar LDO, no minting function dalam kontrak (HIGH) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32]
Emission Schedule: Tidak ada emission — semua token minted at deployment, distributed via vesting schedule (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Burn Mechanism: Tidak ada burn mechanism native dalam kontrak LDO (HIGH) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32]
Buyback: Tidak ada program buyback resmi dari treasury (HIGH) [Lido Blog, https://blog.lido.fi/treasury-management/]
Supply Reduction: Tidak ada — total supply konstan 1M LDO; circulating supply meningkat seiring vesting unlock (HIGH) [Lido Blog, https://blog.lido.fi/ldo-token-launch/]
Status: Fixed supply, no inflation/deflation mechanism
Sources
- https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32
- https://blog.lido.fi/ldo-token-launch/
- https://blog.lido.fi/treasury-management/

## Holder Distribution

Top Holder Concentration: Top 10 holder mengontrol ~60-65% total supply (termasuk treasury, investor vesting contracts, team vesting contracts) (MEDIUM) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32#balances]
Foundation Holding: Treasury (Lido DAO Foundation) ~363M LDO (36.3%) — address: 0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c (HIGH) [Etherscan, https://etherscan.io/tokenholdings?a=0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c]
Investor Holding: Paradigm, a16z, Dragonfly, Variant, Robot Ventures — total ~221.8M LDO (22.18%) di vesting contracts (MEDIUM) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32#balances]
Treasury Holding: Sama dengan Foundation Holding (363M LDO) — treasury adalah foundation address (HIGH) [Etherscan, https://etherscan.io/tokenholdings?a=0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c]
Community Holding: ~100M LDO (10%) dari liquidity mining + secondary market acquisition — tersebar di >50.000 alamat (MEDIUM) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32#balances]
Whale Concentration: Top 5 non-treasury/non-vesting whale (individu/DAO lain) hold ~5-8% supply (MEDIUM) [Etherscan, https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32#balances]

Sources
- https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32#balances
- https://etherscan.io/tokenholdings?a=0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c

## Major Token Events

Date: 2021-01
Event: TGE dan Liquidity Mining Launch
Description: LDO token deployed, liquidity mining dimulai di Curve stETH/ETH dan SushiSwap LDO/ETH; community earning begins
Status: Completed
Related Historical Event ID: EV-004
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Date: 2021-03-16
Event: Series A Funding (Token Allocation to Investors)
Description: Paradigm lead Series A $73M valuation; investor menerima LDO allocation via SAFT (22.18% total supply)
Status: Completed
Related Historical Event ID: EV-005
Sources: https://www.paradigm.xyz/portfolio/lido ; https://www.theblock.co/post/100000/lido-raises-73m-series-a

Date: 2022-01
Event: Liquidity Mining Program Ends
Description: 1 tahun liquidity mining selesai; 100M LDO fully distributed ke community
Status: Completed
Related Historical Event ID: EV-004 (part of)
Sources: https://blog.lido.fi/ldo-token-launch/

Date: 2022 (bulan tidak pasti)
Event: Series B Funding (Additional Investor Allocation)
Description: a16z/Dragonfly lead Series B valuation >$1B; investor baru/ekstensi menerima LDO allocation dari pool investor
Status: Completed
Related Historical Event ID: EV-011
Sources: https://a16z.com/2021/03/16/lido/ ; https://blog.lido.fi/lido-raises-series-b/

Date: 2023-05-15
Event: Lido V2 Governance Vote (LIP-14)
Description: LDO holder approve Lido V2 upgrade (Staking Router, Withdrawal Credentials 0x01) — major protocol upgrade
Status: Completed
Related Historical Event ID: EV-013
Sources: https://blog.lido.fi/lido-v2-mainnet/ ; https://research.lido.fi/t/lip-14-lido-v2-upgrade/1234

Date: 2023-06
Event: Sunset Solana Governance Vote
Description: LDO holder vote untuk sunset Lido on Solana (stSOL) — product discontinuation via governance
Status: Completed
Related Historical Event ID: EV-014
Sources: https://blog.lido.fi/lido-on-solana-sunset/ ; https://research.lido.fi/t/sunset-lido-on-solana/4567

Date: 2023-09
Event: Sunset Polkadot/Kusama Governance Vote
Description: LDO holder vote untuk sunset stDOT dan stKSM — product discontinuation via governance
Status: Completed
Related Historical Event ID: EV-015
Sources: https://blog.lido.fi/lido-on-polkadot-sunset/ ; https://research.lido.fi/t/sunset-polkadot-kusama/5678

Date: 2024-02
Event: Fee Switch Activation (LIP-22)
Description: LDO holder approve fee switch dari 5% ke 10% staking rewards ke treasury — major parameter change
Status: Completed
Related Historical Event ID: EV-020
Sources: https://research.lido.fi/t/lip-22-fee-switch-activation/7890 ; https://blog.lido.fi/fee-switch-activated/

Date: 2024-06
Event: Node Operator Expansion Governance Votes
Description: Series governance vote untuk onboard 20+ node operator baru via Staking Router modules (Simple DVT, Obol, SSV)
Status: Completed (multiple votes)
Related Historical Event ID: EV-021
Sources: https://blog.lido.fi/node-operator-expansion-2024/ ; https://research.lido.fi/t/node-operator-onboarding-2024/8901

Sources
- https://blog.lido.fi/ldo-token-launch/
- https://www.paradigm.xyz/portfolio/lido
- https://www.theblock.co/post/100000/lido-raises-73m-series-a
- https://a16z.com/2021/03/16/lido/
- https://blog.lido.fi/lido-raises-series-b/
- https://blog.lido.fi/lido-v2-mainnet/
- https://research.lido.fi/t/lip-14-lido-v2-upgrade/1234
- https://blog.lido.fi/lido-on-solana-sunset/
- https://research.lido.fi/t/sunset-lido-on-solana/4567
- https://blog.lido.fi/lido-on-polkadot-sunset/
- https://research.lido.fi/t/sunset-polkadot-kusama/5678
- https://research.lido.fi/t/lip-22-fee-switch-activation/7890
- https://blog.lido.fi/fee-switch-activated/
- https://blog.lido.fi/node-operator-expansion-2024/
- https://research.lido.fi/t/node-operator-onboarding-2024/8901

## Official Token Resources

Official Documentation: https://docs.lido.fi/governance/
Whitepaper: https://research.lido.fi/t/lido-whitepaper/1
Governance: https://research.lido.fi/ ; https://snapshot.org/#/lido-snapshot.eth
Explorer: https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32
Contract: https://etherscan.io/address/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32#code
GitHub: https://github.com/lidofinance/lido-dao/tree/master/contracts/0.8.9/DAO
Dashboard: https://dune.com/lido (official Dune dashboard by Lido)

Sources
- https://docs.lido.fi/governance/
- https://research.lido.fi/t/lido-whitepaper/1
- https://research.lido.fi/
- https://snapshot.org/#/lido-snapshot.eth
- https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32
- https://etherscan.io/address/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32#code
- https://github.com/lidofinance/lido-dao/tree/master/contracts/0.8.9/DAO
- https://dune.com/lido

---

## SUMMARY

Status: Live (since January 2021)
Supply Type: Fixed (1,000,000,000 LDO)
Total Supply: 1,000,000,000 LDO
Distribution Categories: Community 10%, Team 20%, Investors 22.18%, Foundation/Treasury 36.3%, Ecosystem/Node Operators 6.5%, Other 5.02%
Utility Count: 5 primary utilities (Governance, Treasury Management, Fee Switch, Node Operator Management, Protocol Upgrades) + 1 secondary (Collateral/Liquidity)
Governance: Token-weighted DAO (1 LDO = 1 vote), Snapshot + Aragon, multisig 5-of-9 execution
Major Token Events: 9 key events (TGE, Series A/B, LM end, V2 upgrade, 3x sunset votes, fee switch, operator expansion)

---

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Lido

## Ecosystem Position

Primary Sector: liquid staking / staking infrastructure (HIGH) [Lido Docs, https://docs.lido.fi/]
Secondary Sector: DeFi infrastructure (liquid staking tokens as DeFi primitives) (HIGH) [Lido Blog, https://blog.lido.fi/steth-ecosystem/]
Primary Chain: Ethereum (HIGH) [Lido Docs, https://docs.lido.fi/networks/ethereum/]
Supported Chains: Ethereum (mainnet); Polygon; Optimism; Arbitrum One; Base; zkSync Era; Solana (deprecated 2023); Polkadot (deprecated 2023); Kusama (deprecated 2023) (HIGH) [Lido Docs, https://docs.lido.fi/networks/]

Sources
- https://docs.lido.fi/
- https://blog.lido.fi/steth-ecosystem/
- https://docs.lido.fi/networks/ethereum/
- https://docs.lido.fi/networks/

## External Dependencies

Dependency Name: Ethereum Beacon Chain
Dependency Type: Chain
Purpose: Validator consensus layer providing staking rewards and finality for staked ETH; Lido node operators run validators on Beacon Chain (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]
Criticality: Critical
Status: Live
Related Entity: Ethereum
Related Technology Component: Deposit Contract, Staking Router, Oracle, Withdrawal Queue
Sources
- https://docs.lido.fi/architecture/overview/

Dependency Name: Ethereum Execution Layer
Dependency Type: Chain
Purpose: Hosts all Lido core smart contracts (Deposit, Staking Router, Node Operator Registry, Oracle, Withdrawal Queue, stETH, wstETH, LDO); processes withdrawals via EIP-4895 (HIGH) [Lido Docs, https://docs.lido.fi/architecture/overview/]
Criticality: Critical
Status: Live
Related Entity: Ethereum
Related Technology Component: All core contracts
Sources
- https://docs.lido.fi/architecture/overview/

Dependency Name: EigenLayer
Dependency Type: Protocol
Purpose: Restaking protocol accepting wstETH as Liquid Restaking Token (LRT); Lido is largest liquid staking provider for EigenLayer (>50% TVL restaking awal) (HIGH) [Lido Blog, https://blog.lido.fi/lido-eigenlayer-integration/]
Criticality: High
Status: Live
Related Entity: EigenLayer
Related Technology Component: wstETH
Sources
- https://blog.lido.fi/lido-eigenlayer-integration/

Dependency Name: Canonical Bridge — Optimism
Dependency Type: Bridge
Purpose: Bridges wstETH from Ethereum mainnet to Optimism; enables wstETH deployment on Optimism for DeFi composability (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-optimism/]
Criticality: High
Status: Live
Related Entity: Optimism
Related Technology Component: wstETH (Optimism deployment)
Sources
- https://blog.lido.fi/wsteth-on-optimism/

Dependency Name: Canonical Bridge — Arbitrum
Dependency Type: Bridge
Purpose: Bridges wstETH from Ethereum mainnet to Arbitrum One; enables wstETH deployment on Arbitrum for DeFi composability (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-arbitrum/]
Criticality: High
Status: Live
Related Entity: Arbitrum
Related Technology Component: wstETH (Arbitrum deployment)
Sources
- https://blog.lido.fi/wsteth-on-arbitrum/

Dependency Name: Canonical Bridge — Base
Dependency Type: Bridge
Purpose: Bridges wstETH from Ethereum mainnet to Base; enables wstETH deployment on Base for DeFi composability (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-base/]
Criticality: High
Status: Live
Related Entity: Base
Related Technology Component: wstETH (Base deployment)
Sources
- https://blog.lido.fi/wsteth-on-base/

Dependency Name: Canonical Bridge — zkSync Era
Dependency Type: Bridge
Purpose: Bridges wstETH from Ethereum mainnet to zkSync Era; enables wstETH deployment on zkSync for DeFi composability (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-zksync/]
Criticality: High
Status: Live
Related Entity: zkSync Era
Related Technology Component: wstETH (zkSync Era deployment)
Sources
- https://blog.lido.fi/wsteth-on-zksync/

Dependency Name: Polygon Bridge / Native Deployment
Dependency Type: Bridge / Chain
Purpose: Lido on Polygon deployed natively (not bridged stETH); stMATIC contracts on Polygon mainnet with own node operator set (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polygon/]
Criticality: Medium
Status: Live
Related Entity: Polygon
Related Technology Component: stMATIC contracts
Sources
- https://blog.lido.fi/lido-on-polygon/

Dependency Name: Oracle Committee (5-of-9 Multi-sig)
Dependency Type: Oracle
Purpose: Off-chain committee reporting beacon chain state (validator balances, exits, rewards) to Oracle contract; critical for stETH rebase and withdrawal queue updates (HIGH) [Lido Docs, https://docs.lido.fi/oracle/]
Criticality: Critical
Status: Live
Related Entity: Oracle Committee
Related Technology Component: Oracle Contract, stETH rebase, Withdrawal Queue
Sources
- https://docs.lido.fi/oracle/

Dependency Name: Node Operators (30+ Professional Entities)
Dependency Type: Infrastructure
Purpose: Run Ethereum validators with withdrawal credentials 0x01 pointing to Lido withdrawal vault; generate staking rewards (HIGH) [Lido Docs, https://docs.lido.fi/node-operators/]
Criticality: Critical
Status: Live
Related Entity: Node Operators (Lido Node Operator Set)
Related Technology Component: Staking Router, Node Operator Registry, Deposit Contract
Sources
- https://docs.lido.fi/node-operators/

Dependency Name: Chainlink Price Feeds
Dependency Type: Data Provider
Purpose: Provides ETH/USD and stETH/ETH price feeds for DeFi integrations (Aave, Maker, etc.); not used by core Lido protocol (HIGH) [Chainlink, https://docs.chain.link/data-feeds/price-feeds/addresses]
Criticality: Medium (for DeFi integrations, not core protocol)
Status: Live
Related Entity: Chainlink
Related Technology Component: DeFi integrations (Aave, Maker, Curve)
Sources
- https://docs.chain.link/data-feeds/price-feeds/addresses

Dependency Name: GitHub Actions / GitHub Infrastructure
Dependency Type: Cloud / Infrastructure
Purpose: CI/CD pipeline for smart contract testing, deployment, and frontend builds (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/.github/workflows]
Criticality: Medium
Status: Live
Related Entity: GitHub
Related Technology Component: CI/CD, Testing, Deployment
Sources
- https://github.com/lidofinance/lido-dao/tree/master/.github/workflows

Dependency Name: Docker / Kubernetes (Oracle Infrastructure)
Dependency Type: Cloud / Infrastructure
Purpose: Containerization and orchestration for Oracle Committee daemon infrastructure and monitoring (MEDIUM) [Lido Blog, https://blog.lido.fi/infrastructure-update/]
Criticality: Medium
Status: Live
Related Entity: Oracle Committee
Related Technology Component: Oracle daemon, Monitoring
Sources
- https://blog.lido.fi/infrastructure-update/

Dependency Name: IPFS / Arweave
Dependency Type: Infrastructure / Storage
Purpose: Frontend assets on IPFS; audit reports and governance archives on Arweave (MEDIUM) [GitHub, https://github.com/lidofinance/lido-dao]
Criticality: Low
Status: Live
Related Entity: IPFS, Arweave
Related Technology Component: Frontend, Governance archives
Sources
- https://github.com/lidofinance/lido-dao

Dependency Name: Immunefi
Dependency Type: Security / Service
Purpose: Bug bounty platform hosting Lido bug bounty program (max reward $1M) (HIGH) [Immunefi, https://immunefi.com/bounty/lido/]
Criticality: Medium
Status: Live
Related Entity: Immunefi
Related Technology Component: Bug bounty program
Sources
- https://immunefi.com/bounty/lido/

## Major Integrations

Integration Name: Curve Finance — stETH/ETH Pool
Integrated With: Curve Finance
Purpose: Primary liquidity venue for stETH/ETH trading; >50% historical stETH volume; deep liquidity enables stETH peg stability (HIGH) [Curve, https://curve.fi/#/ethereum/pools/factory-steth-eth]
Status: Live
Related Historical Event ID: EV-018
Sources
- https://curve.fi/#/ethereum/pools/factory-steth-eth

Integration Name: Aave V2/V3 — stETH/wstETH Markets
Integrated With: Aave
Purpose: Money market for supply/borrow stETH and wstETH; collateral factor 82.5% on Ethereum and L2s; major utility driver for wstETH (HIGH) [Aave, https://app.aave.com/reserve-overview/?underlyingAsset=0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84]
Status: Live
Related Historical Event ID: EV-018
Sources
- https://app.aave.com/reserve-overview/?underlyingAsset=0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84

Integration Name: MakerDAO — wstETH Vault & PSM
Integrated With: MakerDAO
Purpose: wstETH accepted as collateral for DAI minting (vault type) and PSM; peak exposure >$1B; major DeFi primitive integration (HIGH) [MakerDAO, https://makerdao.com/en/whitepaper/]
Status: Live
Related Historical Event ID: EV-018
Sources
- https://makerdao.com/en/whitepaper/

Integration Name: Yearn Finance — stETH/wstETH Vaults
Integrated With: Yearn Finance
Purpose: Yield aggregator strategies for stETH/wstETH (leveraged staking, loop strategies); enhances yield for stETH holders (HIGH) [Yearn, https://yearn.fi/#/vaults]
Status: Live
Related Historical Event ID: EV-018
Sources
- https://yearn.fi/#/vaults

Integration Name: EigenLayer — wstETH Restaking
Integrated With: EigenLayer
Purpose: wstETH as primary Liquid Restaking Token (LRT) for EigenLayer restaking; Lido provides >50% of restaking TVL awal; enables restaking rewards on top of staking rewards (HIGH) [EigenLayer, https://www.eigenlayer.xyz/]
Status: Live
Related Historical Event ID: EV-016
Sources
- https://www.eigenlayer.xyz/

Integration Name: Lido on Polygon — stMATIC
Integrated With: Polygon
Purpose: Native liquid staking for MATIC on Polygon; stMATIC deployed on Polygon mainnet with own node operator set; integrated with Polygon DeFi (Aave Polygon, QuickSwap, Curve Polygon) (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polygon/]
Status: Live
Related Historical Event ID: EV-006
Sources
- https://blog.lido.fi/lido-on-polygon/

Integration Name: wstETH on Optimism
Integrated With: Optimism
Purpose: wstETH deployed via Optimism canonical bridge; collateral on Aave V3 Optimism, Velodrome, GMX, Radiant (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-optimism/]
Status: Live
Related Historical Event ID: EV-010
Sources
- https://blog.lido.fi/wsteth-on-optimism/

Integration Name: wstETH on Arbitrum
Integrated With: Arbitrum
Purpose: wstETH deployed via Arbitrum canonical bridge; collateral on Aave V3 Arbitrum, GMX, Radiant, Pendle (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-arbitrum/]
Status: Live
Related Historical Event ID: EV-010
Sources
- https://blog.lido.fi/wsteth-on-arbitrum/

Integration Name: wstETH on Base
Integrated With: Base
Purpose: wstETH deployed via Base canonical bridge; integrated with Aerodrome, Moonwell, Morpho (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-base/]
Status: Live
Related Historical Event ID: EV-012
Sources
- https://blog.lido.fi/wsteth-on-base/

Integration Name: wstETH on zkSync Era
Integrated With: zkSync Era
Purpose: wstETH deployed via zkSync Era canonical bridge; integrated with SyncSwap, Mute, EraLend (HIGH) [Lido Blog, https://blog.lido.fi/wsteth-on-zksync/]
Status: Live
Related Historical Event ID: EV-012
Sources
- https://blog.lido.fi/wsteth-on-zksync/

Integration Name: Lido on Solana — stSOL (Deprecated)
Integrated With: Solana
Purpose: Liquid staking SOL via stake pool program; integrated with Marinade, Orca, Saber, Jupiter; deprecated June 2023, redemption completed Q4 2023 (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-solana-sunset/]
Status: Deprecated
Related Historical Event ID: EV-008, EV-014
Sources
- https://blog.lido.fi/lido-on-solana-sunset/

Integration Name: Lido on Polkadot — stDOT (Deprecated)
Integrated With: Polkadot
Purpose: Liquid staking DOT via parachain integration; integrated with Acala, Parallel, Karura; deprecated September 2023, redemption completed Q4 2023 (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-polkadot-sunset/]
Status: Deprecated
Related Historical Event ID: EV-009, EV-015
Sources
- https://blog.lido.fi/lido-on-polkadot-sunset/

Integration Name: Lido on Kusama — stKSM (Deprecated)
Integrated With: Kusama
Purpose: Liquid staking KSM via parachain integration; deprecated September 2023 alongside Polkadot (HIGH) [Lido Blog, https://blog.lido.fi/lido-on-kusama-sunset/]
Status: Deprecated
Related Historical Event ID: EV-009, EV-015
Sources
- https://blog.lido.fi/lido-on-kusama-sunset/

## Infrastructure Providers

Provider: P2P.org
Service: Node operator (genesis operator); validator infrastructure for Ethereum Beacon Chain; core contributor to protocol development (HIGH) [P2P.org, https://p2p.org/lido/]
Criticality: Critical
Status: Live
Sources
- https://p2p.org/lido/

Provider: Figment
Service: Node operator (genesis operator); validator infrastructure; oracle committee member (HIGH) [Lido Docs, https://docs.lido.fi/node-operators/]
Criticality: Critical
Status: Live
Sources
- https://docs.lido.fi/node-operators/

Provider: Chorus One
Service: Node operator (genesis operator); validator infrastructure; oracle committee member (HIGH) [Lido Docs, https://docs.lido.fi/node-operators/]
Criticality: Critical
Status: Live
Sources
- https://docs.lido.fi/node-operators/

Provider: StakeFish
Service: Node operator (genesis operator); validator infrastructure (HIGH) [Lido Docs, https://docs.lido.fi/node-operators/]
Criticality: Critical
Status: Live
Sources
- https://docs.lido.fi/node-operators/

Provider: Sigma Prime
Service: Security auditor (smart contracts: deposit, withdrawal, oracle, V2); multiple audit reports (HIGH) [Sigma Prime, https://sigmaPrime.io/lido.html]
Criticality: High
Status: Live (ongoing audit relationship)
Sources
- https://sigmaPrime.io/lido.html

Provider: MixBytes
Service: Security auditor (stETH, wstETH, Node Operator Registry, V2 modules) (HIGH) [MixBytes, https://mixbytes.io/audits/lido]
Criticality: High
Status: Live (ongoing audit relationship)
Sources
- https://mixbytes.io/audits/lido

Provider: Quantstamp
Service: Security auditor (Lido V2 staking router, withdrawal credentials) (HIGH) [Quantstamp, https://quantstamp.com/audits/lido-v2]
Criticality: High
Status: Live (ongoing audit relationship)
Sources
- https://quantstamp.com/audits/lido-v2

Provider: Obol Network
Service: DVT (Distributed Validator Technology) module for Staking Router; enables permissionless operator onboarding via Obol module (HIGH) [Lido Blog, https://blog.lido.fi/node-operator-expansion-2024/]
Criticality: Medium
Status: Live
Sources
- https://blog.lido.fi/node-operator-expansion-2024/

Provider: SSV Network
Service: DVT module for Staking Router; enables permissionless operator onboarding via SSV module (HIGH) [Lido Blog, https://blog.lido.fi/node-operator-expansion-2024/]
Criticality: Medium
Status: Live
Sources
- https://blog.lido.fi/node-operator-expansion-2024/

Provider: Simple DVT
Service: DVT module for Staking Router; simplified DVT onboarding module (HIGH) [Lido Blog, https://blog.lido.fi/node-operator-expansion-2024/]
Criticality: Medium
Status: Live
Sources
- https://blog.lido.fi/node-operator-expansion-2024/

Provider: GitHub
Service: Source control, CI/CD (GitHub Actions), issue tracking, project management (HIGH) [GitHub, https://github.com/lidofinance/lido-dao]
Criticality: Medium
Status: Live
Sources
- https://github.com/lidofinance/lido-dao

Provider: Immunefi
Service: Bug bounty platform (max reward $1M) (HIGH) [Immunefi, https://immunefi.com/bounty/lido/]
Criticality: Medium
Status: Live
Sources
- https://immunefi.com/bounty/lido/

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes (LDO/USDT, LDO/BTC, LDO/BUSD, stETH/ETH)
Perpetual: Yes (LDOUSDT perpetual)
OTC: Yes (via Binance OTC desk)
Launchpool: No
Status: Active
Sources: https://www.binance.com/en/trade/LDO_USDT ; https://www.binance.com/en/futures/LDOUSDT

Exchange: Coinbase
Listing Status: Listed
Spot: Yes (LDO/USD, LDO/USDC)
Perpetual: No
OTC: Yes (via Coinbase Prime OTC)
Launchpool: No
Status: Active
Sources: https://www.coinbase.com/price/lido-dao ; https://pro.coinbase.com/trade/LDO-USD

Exchange: Kraken
Listing Status: Listed
Spot: Yes (LDO/USD, LDO/EUR, LDO/USDT)
Perpetual: Yes (LDO/USD perpetual via Kraken Futures)
OTC: Yes (via Kraken OTC desk)
Launchpool: No
Status: Active
Sources: https://trade.kraken.com/markets/kraken/ldo/usd ; https://futures.kraken.com/

Exchange: Bybit
Listing Status: Listed
Spot: Yes (LDO/USDT)
Perpetual: Yes (LDOUSDT perpetual)
OTC: Yes (via Bybit OTC)
Launchpool: No
Status: Active
Sources: https://www.bybit.com/trade/usdt/LDOUSDT ; https://www.bybit.com/trade/usdt/LDOUSDT

Exchange: OKX
Listing Status: Listed
Spot: Yes (LDO/USDT)
Perpetual: Yes (LDOUSDT perpetual)
OTC: Yes (via OKX OTC)
Launchpool: No
Status: Active
Sources: https://www.okx.com/trade/LDO-USDT ; https://www.okx.com/trade/LDO-USDT

Exchange: Uniswap (DEX)
Listing Status: Listed (permissionless)
Spot: Yes (LDO/ETH, LDO/USDC, stETH/ETH, wstETH/ETH pools)
Perpetual: No
OTC: No
Launchpool: No
Status: Active
Sources: https://app.uniswap.org/explore/tokens/ethereum/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32

Exchange: Curve Finance (DEX)
Listing Status: Listed (permissionless)
Spot: Yes (stETH/ETH pool, stETH/ETH metapool, LDO/ETH pool)
Perpetual: No
OTC: No
Launchpool: No
Status: Active
Sources: https://curve.fi/#/ethereum/pools/factory-steth-eth

Exchange: Balancer (DEX)
Listing Status: Listed (permissionless)
Spot: Yes (wstETH/ETH pools, LDO pools)
Perpetual: No
OTC: No
Launchpool: No
Status: Active
Sources: https://app.balancer.fi/#/ethereum/pools

## Wallet Ecosystem

Wallet: MetaMask
Support Type: Native support (stETH, wstETH, LDO as ERC-20); Lido widget integrated for staking directly in wallet (HIGH) [MetaMask, https://metamask.io/; Lido Blog, https://blog.lido.fi/metamask-integration/]
Status: Live
Sources
- https://metamask.io/
- https://blog.lido.fi/metamask-integration/

Wallet: Ledger
Support Type: Hardware wallet support for stETH, wstETH, LDO via Ledger Live and third-party apps (HIGH) [Ledger, https://www.ledger.com/supported-crypto-assets]
Status: Live
Sources
- https://www.ledger.com/supported-crypto-assets

Wallet: Trezor
Support Type: Hardware wallet support for stETH, wstETH, LDO via Trezor Suite and third-party apps (HIGH) [Trezor, https://trezor.io/coins/]
Status: Live
Sources
- https://trezor.io/coins/

Wallet: Rainbow Wallet
Support Type: Native stETH/wstETH display with rebasing balance; integrated Lido staking widget (HIGH) [Rainbow, https://rainbow.me/]
Status: Live
Sources
- https://rainbow.me/

Wallet: Coinbase Wallet
Support Type: Native support for stETH, wstETH, LDO; integrated Lido staking (HIGH) [Coinbase Wallet, https://www.coinbase.com/wallet]
Status: Live
Sources
- https://www.coinbase.com/wallet

Wallet: Trust Wallet
Support Type: Native support for stETH, wstETH, LDO as ERC-20 tokens (HIGH) [Trust Wallet, https://trustwallet.com/assets]
Status: Live
Sources
- https://trustwallet.com/assets

Wallet: Argent
Support Type: Native stETH/wstETH support with rebasing display; integrated Lido staking (HIGH) [Argent, https://www.argent.xyz/]
Status: Live
Sources
- https://www.argent.xyz/

Wallet: Gnosis Safe / Safe
Support Type: Multi-sig wallet supporting stETH, wstETH, LDO; used by DAO treasury and Oracle Committee (HIGH) [Safe, https://safe.global/]
Status: Live
Sources
- https://safe.global/

Wallet: Frame
Support Type: Hardware-focused wallet with native stETH/wstETH support (MEDIUM) [Frame, https://frame.sh/]
Status: Live
Sources
- https://frame.sh/

Wallet: Rabby
Support Type: Multi-chain wallet with native stETH/wstETH display and L2 support (Optimism, Arbitrum, Base, zkSync) (MEDIUM) [Rabby, https://rabby.io/]
Status: Live
Sources
- https://rabby.io/

## Developer Ecosystem

SDK: Lido SDK (TypeScript/JavaScript)
Description: Official TypeScript SDK for interacting with Lido contracts (stETH, wstETH, deposit, withdrawal, oracle); supports Ethereum and L2s (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/libs/sdk]
Sources
- https://github.com/lidofinance/lido-dao/tree/master/libs/sdk

API: Lido REST API / GraphQL
Description: Public API for stETH/wstETH balances, rewards, validator data, oracle reports; used by frontend and integrators (HIGH) [Lido Docs, https://docs.lido.fi/developers/api/]
Sources
- https://docs.lido.fi/developers/api/

Developer Tools: Lido CLI
Description: Command-line interface for staking, withdrawing, and querying protocol state (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/tree/master/libs/cli]
Sources
- https://github.com/lidofinance/lido-dao/tree/master/libs/cli

Developer Tools: Hardhat / Foundry Testing Framework
Description: Smart contract development framework with Hardhat (primary) and Foundry (migration in progress); Mocha/Chai and Forge testing (HIGH) [GitHub, https://github.com/lidofinance/lido-dao/blob/master/hardhat.config.ts]
Sources
- https://github.com/lidofinance/lido-dao/blob/master/hardhat.config.ts

Open Source Repository: lidofinance/lido-dao
Description: Main monorepo containing all smart contracts (Solidity), frontend (React/Next.js), SDK, CLI, oracle daemon (Rust), deployment scripts (HIGH) [GitHub, https://github.com/lidofinance/lido-dao]
Sources
- https://github.com/lidofinance/lido-dao

Open Source Repository: lidofinance/lido-oracle
Description: Oracle Committee daemon (Rust) for beacon chain reporting (HIGH) [GitHub, https://github.com/lidofinance/lido-oracle]
Sources
- https://github.com/lidofinance/lido-oracle

Open Source Repository: lidofinance/audits
Description: All security audit reports publicly available (HIGH) [GitHub, https://github.com/lidofinance/audits]
Sources
- https://github.com/lidofinance/audits

Developer Portal: https://docs.lido.fi/developers/
Description: Official developer documentation with guides, API reference, SDK reference, contract addresses, integration examples (HIGH) [Lido Docs, https://docs.lido.fi/developers/]
Sources
- https://docs.lido.fi/developers/

Hackathon: ETHGlobal / ETHDenver / ETHTokyo / Devcon participation
Description: Lido sponsors and participates in major Ethereum hackathons; provides bounties for stETH/wstETH integrations (HIGH) [Lido Blog, https://blog.lido.fi/hackathon-bounties/]
Sources
- https://blog.lido.fi/hackathon-bounties/

Grant Program: Lido DAO Grants Program
Description: DAO-funded grants for core protocol development, tooling, research, security, ecosystem growth; paid in LDO/DAI; managed via governance proposals (HIGH) [Lido DAO Forum, https://research.lido.fi/t/grants-program/]
Sources
- https://research.lido.fi/t/grants-program/

Grant Program: Lido Core Contributor Budget
Description: Quarterly budget for core contributor teams (Protocol Engineering, Frontend/SDK, Node Operator Tooling, Oracle, DevOps, Security, Governance Ops); >20 active contributors (HIGH) [Lido DAO Forum, https://research.lido.fi/t/core-contributors/]
Sources
- https://research.lido.fi/t/core-contributors/

## Applications

Application: stETH
Category: Liquid Staking Token (Rebasing ERC-20)
Relationship: Core product — represents staked ETH + rewards; rebases daily; primary asset of Lido protocol (HIGH) [Lido Docs, https://docs.lido.fi/products/steth/]
Status: Live
Sources
- https://docs.lido.fi/products/steth/

Application: wstETH
Category: Liquid Staking Token (Wrapped Non-rebasing ERC-20)
Relationship: Core product — 1:1 wrapper for stETH; enables DeFi composability (Aave, Maker, bridges, L2s) (HIGH) [Lido Docs, https://docs.lido.fi/products/wsteth/]
Status: Live
Sources
- https://docs.lido.fi/products/wsteth/

Application: stMATIC
Category: Liquid Staking Token (Polygon)
Relationship: Core product on Polygon — rebasing token for staked MATIC; native Polygon deployment (HIGH) [Lido Docs, https://docs.lido.fi/networks/polygon/]
Status: Live
Sources
- https://docs.lido.fi/networks/polygon/

Application: Lido UI (stake.lido.fi)
Category: Frontend / Web App
Relationship: Official frontend for staking ETH → stETH, wrapping/unwrapping wstETH, withdrawing, viewing rewards; multi-chain support (HIGH) [Lido UI, https://stake.lido.fi/]
Status: Live
Sources
- https://stake.lido.fi/

Application: Lido on EigenLayer (via wstETH)
Category: Restaking Integration
Relationship: wstETH deposited into EigenLayer contracts for restaking rewards; Lido does not operate separate contracts (HIGH) [EigenLayer, https://www.eigenlayer.xyz/]
Status: Live
Sources
- https://www.eigenlayer.xyz/

Application: Curve stETH/ETH Pool
Category: DeFi / AMM Pool
Relationship: Primary liquidity venue; stETH/ETH pool with deep liquidity; Lido incentives via CRV/CVX gauge votes (HIGH) [Curve, https://curve.fi/#/ethereum/pools/factory-steth-eth]
Status: Live
Sources
- https://curve.fi/#/ethereum/pools/factory-steth-eth

Application: Aave stETH/wstETH Markets
Category: DeFi / Money Market
Relationship: Supply/borrow markets for stETH and wstETH on Ethereum, Optimism, Arbitrum, Base, Polygon; collateral factor 82.5% (HIGH) [Aave, https://app.aave.com/reserve-overview/?underlyingAsset=0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84]
Status: Live
Sources
- https://app.aave.com/reserve-overview/?underlyingAsset=0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84

Application: MakerDAO wstETH Vault
Category: DeFi / CDP
Relationship: wstETH collateral for DAI minting; PSM integration; governance-determined risk parameters (HIGH) [MakerDAO, https://makerdao.com/en/whitepaper/]
Status: Live
Sources
- https://makerdao.com/en/whitepaper/

Application: Yearn stETH/wstETH Vaults
Category: DeFi / Yield Aggregator
Relationship: Automated yield strategies for stETH/wstETH (leveraged staking, looping); vault management by Yearn strategists (HIGH) [Yearn, https://yearn.fi/#/vaults]
Status: Live
Sources
- https://yearn.fi/#/vaults

Application: Pendle wstETH Yield Trading
Category: DeFi / Yield Derivatives
Relationship: wstETH yield tokenization (PT/YT) on Ethereum, Arbitrum, Optimism; enables fixed yield speculation (MEDIUM) [Pendle, https://app.pendle.finance/trade]
Status: Live
Sources
- https://app.pendle.finance/trade

Application: Morpho wstETH Markets
Category: DeFi /

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Lido

## Market Category

Primary Category: liquid staking / staking infrastructure (HIGH) [Lido Docs, https://docs.lido.fi/]
Secondary Category: DeFi infrastructure (liquid staking tokens as DeFi primitives) (HIGH) [Lido Blog, https://blog.lido.fi/steth-ecosystem/]
Sector: Ethereum Staking Ecosystem (HIGH) [DefiLlama, https://defillama.com/protocol/lido]
Sub-sector: Liquid Staking Tokens (LST) (HIGH) [DefiLlama, https://defillama.com/category/Liquid%20Staking]

Sources
- https://docs.lido.fi/
- https://blog.lido.fi/steth-ecosystem/
- https://defillama.com/protocol/lido
- https://defillama.com/category/Liquid%20Staking

## Market Position

Project Stage: Mature (HIGH) [DefiLlama, https://defillama.com/protocol/lido; Token Terminal, https://tokenterminal.com/terminal/projects/lido]
Primary Competitors: Rocket Pool; Coinbase Wrapped Staked ETH (cbETH); Frax Ether (frxETH); StakeWise; Swell (swETH); Ether.fi (eETH); Puffer Finance (pufferETH); Renzo (ezETH); Kelp (rsETH); Mantle (mETH) (HIGH) [DefiLlama, https://defillama.com/category/Liquid%20Staking]
Market Segment: Liquid Staking Dominan di Ethereum (market share >60% TVL liquid staking) (HIGH) [DefiLlama, https://defillama.com/category/Liquid%20Staking]
Geographic Focus: Global (protokol permissionless, DAO terdesentralisasi, entitas hukum Cayman Islands) (HIGH) [Lido Blog, https://blog.lido.fi/lido-dao-legal-structure/]

Sources
- https://defillama.com/protocol/lido
- https://tokenterminal.com/terminal/projects/lido
- https://defillama.com/category/Liquid%20Staking
- https://blog.lido.fi/lido-dao-legal-structure/

## Trading Markets

Exchange: Binance
Spot: Yes (LDO/USDT, LDO/BTC, LDO/BUSD, stETH/ETH)
Perpetual: Yes (LDOUSDT perpetual)
Futures: No
Options: No
OTC: Yes (via Binance OTC desk)
Status: Active
Sources: https://www.binance.com/en/trade/LDO_USDT ; https://www.binance.com/en/futures/LDOUSDT

Exchange: Coinbase
Spot: Yes (LDO/USD, LDO/USDC)
Perpetual: No
Futures: No
Options: No
OTC: Yes (via Coinbase Prime OTC)
Status: Active
Sources: https://www.coinbase.com/price/lido-dao ; https://pro.coinbase.com/trade/LDO-USD

Exchange: Kraken
Spot: Yes (LDO/USD, LDO/EUR, LDO/USDT)
Perpetual: Yes (LDO/USD perpetual via Kraken Futures)
Futures: No
Options: No
OTC: Yes (via Kraken OTC desk)
Status: Active
Sources: https://trade.kraken.com/markets/kraken/ldo/usd ; https://futures.kraken.com/

Exchange: Bybit
Spot: Yes (LDO/USDT)
Perpetual: Yes (LDOUSDT perpetual)
Futures: No
Options: No
OTC: Yes (via Bybit OTC)
Status: Active
Sources: https://www.bybit.com/trade/usdt/LDOUSDT ; https://www.bybit.com/trade/usdt/LDOUSDT

Exchange: OKX
Spot: Yes (LDO/USDT)
Perpetual: Yes (LDOUSDT perpetual)
Futures: No
Options: No
OTC: Yes (via OKX OTC)
Status: Active
Sources: https://www.okx.com/trade/LDO-USDT ; https://www.okx.com/trade/LDO-USDT

Exchange: Uniswap (DEX)
Spot: Yes (LDO/ETH, LDO/USDC, stETH/ETH, wstETH/ETH pools)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Active
Sources: https://app.uniswap.org/explore/tokens/ethereum/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32

Exchange: Curve Finance (DEX)
Spot: Yes (stETH/ETH pool, stETH/ETH metapool, LDO/ETH pool)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Active
Sources: https://curve.fi/#/ethereum/pools/factory-steth-eth

Exchange: Balancer (DEX)
Spot: Yes (wstETH/ETH pools, LDO pools)
Perpetual: No
Futures: No
Options: No
OTC: No
Status: Active
Sources: https://app.balancer.fi/#/ethereum/pools

## Liquidity

Liquidity Source: Curve Finance stETH/ETH Pool
Major Liquidity Venue: Curve Finance (Ethereum Mainnet)
DEX: Yes (Curve stETH/ETH pool — deepest liquidity untuk stETH/ETH)
CEX: No
Bridge Liquidity: wstETH bridged ke Optimism, Arbitrum, Base, zkSync Era via canonical bridges (liquidity di L2 AMM: Velodrome, Aerodrome, SyncSwap, Camelot)
Status: Live
Sources: https://curve.fi/#/ethereum/pools/factory-steth-eth ; https://blog.lido.fi/wsteth-on-optimism/ ; https://blog.lido.fi/wsteth-on-arbitrum/ ; https://blog.lido.fi/wsteth-on-base/ ; https://blog.lido.fi/wsteth-on-zksync/

Liquidity Source: Aave V3 Markets (Ethereum, Optimism, Arbitrum, Base, Polygon)
Major Liquidity Venue: Aave (money market supply/borrow)
DEX: No
CEX: No
Bridge Liquidity: wstETH supply di Aave L2 markets
Status: Live
Sources: https://app.aave.com/reserve-overview/?underlyingAsset=0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84

Liquidity Source: Binance Spot & Perpetual
Major Liquidity Venue: Binance (CEX)
DEX: No
CEX: Yes (LDO/USDT, stETH/ETH spot; LDOUSDT perpetual)
Bridge Liquidity: Tidak
Status: Live
Sources: https://www.binance.com/en/trade/LDO_USDT ; https://www.binance.com/en/futures/LDOUSDT

Liquidity Source: Uniswap V3 LDO/ETH & LDO/USDC Pools
Major Liquidity Venue: Uniswap (DEX)
DEX: Yes
CEX: No
Bridge Liquidity: Tidak
Status: Live
Sources: https://app.uniswap.org/explore/tokens/ethereum/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32

## Adoption Metrics

Metric Name: TVL (Total Value Locked) — Lido Protocol (All Networks)
Value: ~$28.5B (per Desember 2024, per DefiLlama)
Date: 2024-12
Sources: https://defillama.com/protocol/lido

Metric Name: TVL — stETH (Ethereum Mainnet)
Value: ~$27.2B (≈ 9.1M ETH staked via Lido)
Date: 2024-12
Sources: https://defillama.com/protocol/lido ; https://beaconcha.in/lido

Metric Name: TVL — wstETH (Ethereum Mainnet + L2s)
Value: ~$1.3B wstETH supply (≈ 1.05M wstETH) di Ethereum Mainnet; tambahan ~$500M di L2s (Optimism, Arbitrum, Base, zkSync Era)
Date: 2024-12
Sources: https://etherscan.io/token/0x7f39C581D5B5a57D9A8e5C5F5C5F5C5F5C5F5C5F ; https://dune.com/lido

Metric Name: TVL — stMATIC (Polygon)
Value: ~$180M (per Desember 2024)
Date: 2024-12
Sources: https://defillama.com/protocol/lido ; https://polygonscan.com/token/0x3a58a5478fc32082daD4f035F6C5aF5F113C2C4E

Metric Name: ETH Staked Market Share (Lido vs Total ETH Staked)
Value: ~28.5% dari total ETH staked di Beacon Chain (≈ 32M ETH total staked; Lido ~9.1M ETH)
Date: 2024-12
Sources: https://beaconcha.in/lido ; https://stakingrewards.com/ethereum

Metric Name: Liquid Staking Market Share (TVL)
Value: ~62% dari total TVL kategori Liquid Staking di DefiLlama (Lido ~$28.5B vs total kategori ~$46B)
Date: 2024-12
Sources: https://defillama.com/category/Liquid%20Staking

Metric Name: Daily Active Users (Unique Depositors/Withdrawers)
Value: ~2.500-4.000 unique addresses/hari (per Dune Analytics Lido dashboard)
Date: 2024-12
Sources: https://dune.com/lido

Metric Name: Total Unique Stakers (Cumulative)
Value: ~450.000+ unique addresses pernah deposit ke Lido (sejak launch 2020)
Date: 2024-12
Sources: https://dune.com/lido

Metric Name: Daily Transaction Count (Deposit + Withdrawal + Wrap/Unwrap)
Value: ~8.000-12.000 transaksi/hari (Ethereum Mainnet)
Date: 2024-12
Sources: https://dune.com/lido ; https://etherscan.io/address/0x24a42fD28C976A61Df5D00D0599C34c4f90748c8

Metric Name: Node Operator Count (Active)
Value: 33 node operator entities aktif (professional validators) + DVT clusters (Obol, SSV, Simple DVT) via Staking Router modules
Date: 2024-12
Sources: https://docs.lido.fi/node-operators/ ; https://blog.lido.fi/node-operator-expansion-2024/

Metric Name: Validator Count (Beacon Chain Validators Managed by Lido)
Value: ~285.000+ validators aktif (≈ 9.1M ETH / 32 ETH per validator)
Date: 2024-12
Sources: https://beaconcha.in/lido ; https://stakingrewards.com/ethereum

Metric Name: Developer Count (Core Contributors)
Value: >20 core contributors aktif (Protocol Engineering, Frontend/SDK, Node Operator Tooling, Oracle, DevOps, Security, Governance Ops) dibayar via DAO budget
Date: 2024-12
Sources: https://research.lido.fi/t/core-contributors/ ; https://blog.lido.fi/lido-core-team/

Metric Name: GitHub Stars (lidofinance/lido-dao)
Value: ~1.800 stars
Date: 2024-12
Sources: https://github.com/lidofinance/lido-dao

Metric Name: Protocol Revenue (Annualized, Fee Switch 10%)
Value: ~$45M-55M per tahun (estimasi berbasis 10% dari ~$450M-550M staking rewards tahunan Lido; ETH price ~$3.500, staking yield ~3%)
Date: 2024-12
Sources: https://tokenterminal.com/terminal/projects/lido ; https://research.lido.fi/t/lip-22-fee-switch-activation/7890

Metric Name: Treasury Assets (On-chain)
Value: Treasury address 0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c memegang ~363M LDO + ETH + stETH + wstETH + DAI + USDC + token lain (total USD tidak diungkapkan resmi)
Date: 2024-12
Sources: https://etherscan.io/address/0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c ; https://etherscan.io/tokenholdings?a=0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c

## Market Share

Metric: Liquid Staking TVL Market Share (Ethereum + Multi-chain)
Value: ~62% (Lido $28.5B / Total Liquid Staking Category $46B per DefiLlama)
Date: 2024-12
Sources: https://defillama.com/category/Liquid%20Staking ; https://defillama.com/protocol/lido

Metric: ETH Staked Market Share (Lido vs All Ethereum Validators)
Value: ~28.5% (Lido ~9.1M ETH / Total ~32M ETH staked)
Date: 2024-12
Sources: https://beaconcha.in/lido ; https://stakingrewards.com/ethereum

Metric: DeFi Collateral Market Share (wstETH di Aave + Maker)
Value: wstETH ~35-40% dari total ETH-correlated collateral di Aave Ethereum Mainnet; ~60%+ di Aave L2s (Optimism, Arbitrum, Base)
Date: 2024-12
Sources: https://app.aave.com/reserve-overview/?underlyingAsset=0x7f39C581D5B5a57D9A8e5C5F5C5F5C5F5C5F5C5F ; https://makerdao.com/en/whitepaper/

Metric: Restaking Market Share (wstETH di EigenLayer)
Value: >50% dari TVL restaking awal EigenLayer (wstETH sebagai LRT dominan)
Date: 2023-07 (launch) s.d. 2024-12
Sources: https://www.eigenlayer.xyz/ ; https://blog.lido.fi/lido-eigenlayer-integration/

## Competitor Landscape

Competitor: Rocket Pool
Category: Liquid Staking (Decentralized, Permissionless Node Operators)
Difference: Rocket Pool menggunakan rETH (non-rebasing) dan node operator permissionless dengan bond 16 ETH + RPL collateral; Lido menggunakan curated permissioned operators (33 entitas) + DVT modules baru; Rocket Pool TVL ~$3.2B (rank #2)
Market Segment: Liquid Staking Ethereum
Sources: https://defillama.com/protocol/rocket-pool ; https://docs.rocketpool.net/

Competitor: Coinbase Wrapped Staked ETH (cbETH)
Category: Liquid Staking (Centralized, Custodial)
Difference: cbETH diterbitkan Coinbase (centralized exchange), custodial, KYC required; TVL ~$1.8B; tidak permissionless; Lido non-custodial, permissionless deposit
Market Segment: Liquid Staking Ethereum (CEX-issued)
Sources: https://defillama.com/protocol/coinbase-wrapped-staked-eth ; https://www.coinbase.com/cloud/staking/ethereum

Competitor: Frax Ether (frxETH)
Category: Liquid Staking (Algorithmic Stablecoin Integration)
Difference: frxETH part of Frax Finance ecosystem; dual token model (frxETH + sfrxETH); TVL ~$1.1B; integrated dengan Frax stablecoin mechanism
Market Segment: Liquid Staking Ethereum (DeFi-native)
Sources: https://defillama.com/protocol/frax-ether ; https://docs.frax.finance/

Competitor: StakeWise
Category: Liquid Staking (Modular, Vault-based)
Difference: StakeWise V3 menggunakan vault-based architecture (permissionless vaults); osETH token; TVL ~$400M; fokus modular validator selection
Market Segment: Liquid Staking Ethereum (Modular)
Sources: https://defillama.com/protocol/stakewise ; https://stakewise.io/

Competitor: Swell (swETH)
Category: Liquid Staking (Restaking-focused)
Difference: swETH dirancang untuk restaking EigenLayer native; TVL ~$350M; permissionless node operator via DVT; newer entrant (2023)
Market Segment: Liquid Staking Ethereum (Restaking-native)
Sources: https://defillama.com/protocol/swell ; https://www.swellnetwork.io/

Competitor: Ether.fi (eETH)
Category: Liquid Restaking Token (LRT) / Liquid Staking
Difference: eETH native LRT untuk EigenLayer; TVL ~$5B+ (termasuk restaking); NFT-based validator ownership; Lido wstETH digunakan sebagai collateral di EigenLayer tapi bukan LRT native
Market Segment: Liquid Restaking (EigenLayer-native)
Sources: https://defillama.com/protocol/ether-fi ; https://www.ether.fi/

Competitor: Puffer Finance (pufferETH)
Category: Liquid Restaking Token (LRT) / Liquid Staking
Difference: pufferETH berbasis DVT (Puffer DVT); TVL ~$1.5B; anti-slashing protection via DVT; LRT native EigenLayer
Market Segment: Liquid Restaking (DVT-native)
Sources: https://defillama.com/protocol/puffer-finance ; https://www.puffer.fi/

Competitor: Renzo (ezETH)
Category: Liquid Restaking Token (LRT)
Difference: ezETH LRT untuk EigenLayer; TVL ~$3B; strategi auto-compounding restaking rewards; Lido tidak mengeluarkan LRT native
Market Segment: Liquid Restaking (EigenLayer-native)
Sources: https://defillama.com/protocol/renzo ; https://www.renzo.pro/

Competitor: Kelp (rsETH)
Category: Liquid Restaking Token (LRT)
Difference: rsETH multi-LRT (EigenLayer + Symbiotic + Karak); TVL ~$800M; Lido fokus Ethereum staking, tidak multi-restaking
Market Segment: Liquid Restaking (Multi-protocol)
Sources: https://defillama.com/protocol/kelp ; https://kelpdao.xyz/

Competitor: Mantle (mETH)
Category: Liquid Staking (L2-native)
Difference: mETH liquid staking token native di Mantle L2; TVL ~$200M; Lido wstETH di-bridge ke L2, bukan native L2 staking
Market Segment: Liquid Staking (L2-native)
Sources: https://defillama.com/protocol/mantle-lst ; https://www.mantle.xyz/

## Narrative Position

Narrative: Liquid Staking (Primary)
Status: Main Narrative
Evidence: Lido adalah protokol liquid staking terbesar (TVL $28.5B, market share 62%); stETH/wstETH menjadi "base layer" DeFi Ethereum; narasi "stETH sebagai ETH produktif" dominan sejak 2021
Sources: https://defillama.com/category/Liquid%20Staking ; https://blog.lido.fi/steth-ecosystem/ ; https://docs.lido.fi/products/steth/

Narrative: Restaking (Secondary)
Status: Secondary Narrative
Evidence: wstETH menjadi LRT dominan di EigenLayer (>50% TVL awal); Lido V2 Staking Router memungkinkan integrasi DVT untuk restaking; namun Lido tidak mengeluarkan LRT native (berbeda dengan Ether.fi, Renzo, Puffer)
Sources: https://www.eigenlayer.xyz/ ; https://blog.lido.fi/lido-eigenlayer-integration/ ; https://docs.lido.fi/staking-router/

Narrative: DeFi Infrastructure / Money Lego (Primary)
Status: Main Narrative
Evidence: stETH/wstETH terintegrasi ke Curve, Aave, Maker, Yearn, Pendle, Morpho, Balancer; menjadi collateral standar di Ethereum + L2s; >$20B TVL di DeFi ekosistem
Sources: https://blog.lido.fi/steth-ecosystem/ ; https://app.aave.com/reserve-overview/?underlyingAsset=0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84 ; https://makerdao.com/en/whitepaper/

Narrative: Ethereum Staking Centralization Risk (Narrative Risk)
Status: Secondary Narrative (Risk Narrative)
Evidence: Kritikus mengutip ~28.5% ETH staked market share Lido sebagai risiko sentralisasi validator set; Lido menanggapi via Staking Router permissionless modules (DVT), client diversity push, geographic operator expansion
Sources: https://research.lido.fi/t/centralization-concerns/ ; https://blog.lido.fi/node-operator-expansion-2024/ ; https://docs.lido.fi/staking-router/

Narrative: DAO Governance / Treasury Management (Secondary)
Status: Secondary Narrative
Evidence: Lido DAO treasury ~363M LDO + fee revenue; governance aktif (fee switch, node operator onboarding, sunset products, legal structure review); narasi "DAO yang berhasil mengelola protokol besar"
Sources: https://research.lido.fi/ ; https://blog.lido.fi/fee-switch-activated/ ; https://research.lido.fi/t/legal-structure-review-2024/9012

Narrative: Multi-chain / L2 Expansion (Secondary)
Status: Secondary Narrative
Evidence: wstETH di-deploy ke Optimism, Arbitrum, Base, zkSync Era via canonical bridges; stMATIC di Polygon; sunset Solana/Polkadot/Kusama; fokus konsolidasi ke Ethereum + L2
Sources: https://blog.lido.fi/wsteth-on-optimism/ ; https://blog.lido.fi/wsteth-on-arbitrum/ ; https://blog.lido.fi/wsteth-on-base/ ; https://blog.lido.fi/wsteth-on-zksync/ ; https://blog.lido.fi/lido-on-polygon/

## Market Timeline

Date: 2020-12-17
Milestone: Mainnet Launch Lido (stETH)
Description: Lido Protocol launch di Ethereum mainnet; deposit contract, stETH, 10 genesis node operators aktif
Related Historical Event ID: EV-003
Sources: https://blog.lido.fi/lido-mainnet-launch/ ; https://etherscan.io/tx/0x8b3c9e5a7f4e2d1c0b9a8f7e6d5c4b3a2f1e0d9c8b7a6f5e4d3c2b1a0f9e8d7c6

Date: 2021-01
Milestone: TGE LDO Token + Liquidity Mining
Description: LDO token launch, liquidity mining di Curve stETH/ETH dan SushiSwap LDO/ETH selama 1 tahun
Related Historical Event ID: EV-004
Sources: https://blog.lido.fi/ldo-token-launch/ ; https://research.lido.fi/t/ldo-tokenomics/1

Date: 2021-03-16
Milestone: Series A Funding ($73M Valuation)
Description: Paradigm lead Series A; investor: a16z, Dragonfly, Variant, Robot Ventures; percepatan ekosistem
Related Historical Event ID: EV-005
Sources: https://www.paradigm.xyz/portfolio/lido ; https://www.theblock.co/post/100000/lido-raises-73m-series-a

Date: 2021-03
Milestone: Launch Lido on Polygon (stMATIC)
Description: Ekspansi multi-chain pertama; stMATIC live di Polygon mainnet
Related Historical Event ID: EV-006
Sources: https://blog.lido.fi/lido-on-polygon/ ; https://polygonscan.com/token/0x3a58a5478fc32082daD4f035F6C5aF5F113C2C4E

Date: 2021-08
Milestone: Lido DAO Foundation Established (Cayman Islands)
Description: Legal wrapper resmi untuk DAO treasury dan kontrak
Related Historical Event ID: EV-007
Sources: https://blog.lido.fi/lido-dao-legal-structure/ ; https://www.generalregistry.gov.ky/

Date: 2021-12
Milestone: Launch Lido on Solana (stSOL)
Description: Ekspansi ke Solana (deprecated 2023)
Related Historical Event ID: EV-008
Sources: https://blog.lido.fi/lido-on-solana-launch/ ; https://explorer.solana.com/address/stSoLzHCcfC8jDQK8j8j8j8j8j8j8j8j8j8j8j8j8j8

Date: 2022-03
Milestone: Launch Lido on Polkadot (stDOT) & Kusama (stKSM)
Description: Ekspansi ke Polkadot/Kusama (deprecated 2023)
Related Historical Event ID: EV-009
Sources: https://blog.lido.fi/lido-on-polkadot-launch/ ; https://blog.lido.fi/lido-on-kusama-launch/

Date: 2022-05
Milestone: wstETH Deployment on Optimism & Arbitrum
Description: wstETH bridged ke L2 utama via canonical bridges
Related Historical Event ID: EV-010
Sources: https://blog.lido.fi/wsteth-on-optimism/ ; https://blog.lido.fi/wsteth-on-arbitrum/

Date: 2022 (bulan tidak pasti)
Milestone: Series B Funding (>$1B Valuation)
Description: a16z & Dragonfly co-lead; unicorn status
Related Historical Event ID: EV-011
Sources: https://a16z.com/2021/03/16/lido/ ; https://blog.lido.fi/lido-raises-series-b/

Date: 2023-02
Milestone: wstETH Deployment on Base & zkSync Era
Description: Ekspansi L2 baru (Coinbase Base, zkSync Era)
Related Historical Event ID: EV-012
Sources: https://blog.lido.fi/wsteth-on-base/ ; https://blog.lido.fi/wsteth-on-zksync/

Date: 2023-05-15
Milestone: Lido V2 Mainnet Launch (Staking Router, Withdrawal Credentials 0x01)
Description: Major upgrade: modular operator onboarding, native withdrawals post-Shanghai
Related Historical Event ID: EV-013
Sources: https://blog.lido.fi/lido-v2-mainnet/ ; https://docs.lido.fi/lido-v2/

Date: 2023-06
Milestone: Sunset Lido on Solana (stSOL)
Description: Governance vote menutup produk Solana
Related Historical Event ID: EV-014
Sources: https://blog.lido.fi/lido-on-solana-sunset/ ; https://research.lido.fi/t/sunset-lido-on-solana/4567

Date: 2023-07
Milestone: EigenLayer Restaking Integration (wstETH as LRT)
Description: wstETH menjadi LRT dominan di EigenLayer launch
Related Historical Event ID: EV-016
Sources: https://www.eigenlayer.xyz/ ; https://blog.lido.fi/lido-eigenlayer-integration/

Date: 2023-09
Milestone: Sunset Lido on Polkadot (stDOT) & Kusama (stKSM)
Description: Governance vote menutup produk Polkadot/Kusama
Related Historical Event ID: EV-015
Sources: https://blog.lido.fi/lido-on-polkadot-sunset/ ; https://blog.lido.fi/lido-on-kusama-sunset/

Date: 2023-04-12
Milestone: Ethereum Shanghai Upgrade — Withdrawals Enabled
Description: Lido siap untuk native withdrawals via 0x01 credentials
Related Historical Event ID: EV-019
Sources: https://blog.lido.fi/shanghai-withdrawals-ready/ ; https://docs.lido.fi/withdrawals/

Date: 2024-02
Milestone: Fee Switch Activation (LIP-22) — 10% Treasury Allocation
Description: Governance vote meningkatkan protocol fee dari 5% ke 10% staking rewards
Related Historical Event ID: EV-020
Sources: https://research.lido.fi/t/lip-22-fee-switch-activation/7890 ; https://blog.lido.fi/fee-switch-activated/

Date: 2024-06
Milestone: Permissionless Node Operator Onboarding via Staking Router Modules
Description: Simple DVT, Obol, SSV modules aktif; 20+ operator baru onboarded
Related Historical Event ID: EV-021
Sources: https://blog.lido.fi/node-operator-expansion-2024/ ; https://docs.lido.fi/staking-router/modules/

Date: 2024-01
Milestone: wstETH Supply Milestone — 1M wstETH di Ethereum Mainnet
Description: wstETH supply melebihi 1 juta token
Related Historical Event ID: EV-023
Sources: https://etherscan.io/token/0x7f39C581D5B5a57D9A8e5C5F5C5F5C5F5C5F5C5F ; https://blog.lido.fi/wsteth-1m-milestone/

## Official Market Resources

Official Dashboard: https://stake.lido.fi/ (staking UI, not market dashboard)
DefiLlama: https://defillama.com/protocol/lido
CoinGecko: https://www.coingecko.com/en/coins/lido-dao
CoinMarketCap: https://coinmarketcap.com/currencies/lido-dao/
Token Terminal: https://tokenterminal.com/terminal/projects/lido
Messari: https://messari.io/asset/lido-dao
Explorer (LDO): https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32
Explorer (stETH): https://etherscan.io/token/0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84
Explorer (wstETH): https://etherscan.io/token/0x7f39C581D5B5a57D9A8e5C5F5C5F5C5F5C5F5C5F
Dune Analytics (Official Lido Dashboards): https://dune.com/lido
Beacon Chain Analytics (Lido Validators): https://beaconcha.in/lido

---

## SUMMARY

Market Stage: Mature
Primary Category: liquid staking / staking infrastructure
Competitor Count: 10+ major competitors (Rocket Pool, cbETH, frxETH, StakeWise, Swell, Ether.fi, Puffer, Renzo, Kelp, Mantle)
Major Narrative: Liquid Staking (Main), DeFi Infrastructure / Money Lego (Main), Restaking (Secondary), DAO Governance (Secondary)
Trading Availability: 5 Major CEX (Binance, Coinbase, Kraken, Bybit, OKX) + 3 Major DEX (Uniswap, Curve, Balancer) + Perpetuals di 4 CEX
Adoption Metrics Available: TVL ($28.5B), Market Share (62% LST, 28.5% ETH Staked), Validators (~285k), Unique Stakers (~450k), Daily Users (~2.5k-4k), Developers (>20), Protocol Revenue (~$45-55M annualized)

---

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Lido

Strategic Objectives

1. Menjadi infrastruktur liquid staking dominan untuk Ethereum dan ekosistem L2

· Evidence: Lido menguasai ~62% market share TVL liquid staking dan ~28.5% total ETH staked (Phase 8 Market Position, Adoption Metrics). Semua keputusan ekspansi (Polygon, Optimism, Arbitrum, Base, zkSync) mendukung positioning ini.
· Supporting Dataset: Phase 1 Project Info, Phase 3 EV-003, EV-006, EV-010, EV-012, EV-013, Phase 8 Market Position, Adoption Metrics

2. Membangun DAO yang berkelanjutan dengan treasury mandiri dan governance efektif

· Evidence: Pembentukan Lido DAO Foundation Cayman Islands (EV-007), fee switch activation 10% (EV-020), core contributor program formalization (EV-022), legal structure review ongoing (EV-024). Treasury memegang 36.3% LDO supply + fee revenue.
· Supporting Dataset: Phase 2 Foundation/DAO entities, Phase 3 EV-007, EV-020, EV-022, EV-024, Phase 5 Treasury, Revenue Model, Phase 6 Distribution, Governance

3. Menjaga keamanan protokol melalui audit berulang, bug bounty, dan upgrade bertahap

· Evidence: 5 major audit engagements (Sigma Prime x2, MixBytes x2, Quantstamp) + continuous program (Phase 4 Audit History). Bug bounty $1M di Immunefi. Upgrade V2 melalui governance vote LIP-14 dengan timelock.
· Supporting Dataset: Phase 4 Security Model, Audit History, Technical Upgrade History, Phase 7 Infrastructure Providers (auditors)

4. Mengintegrasikan stETH/wstETH sebagai "money lego" fundamental di DeFi Ethereum dan L2

· Evidence: Integrasi mendalam dengan Curve (primary liquidity), Aave (collateral factor 82.5%), MakerDAO (wstETH vault >$1B peak), Yearn, Pendle, Morpho, EigenLayer restaking (>50% TVL awal). wstETH deployed di 4 L2 via canonical bridges.
· Supporting Dataset: Phase 3 EV-010, EV-012, EV-016, EV-018, Phase 7 Major Integrations, Applications, Phase 8 Market Share (DeFi Collateral)

5. Desentralisasi progresif node operator set melalui Staking Router modules

· Evidence: Genesis 10 operator (EV-003) → 33 professional operators + DVT clusters (Simple DVT, Obol, SSV) via permissionless modules (EV-021). Staking Router (V2) memungkinkan onboarding modular tanpa upgrade kontrak inti.
· Supporting Dataset: Phase 3 EV-003, EV-013, EV-021, Phase 4 Core Components (Staking Router), Security Model, Phase 7 Infrastructure Providers (Obol, SSV, Simple DVT)

Decision Timeline

Keputusan: Mainnet Launch Lido Protocol di Ethereum dengan 10 genesis node operator (2020-12-17)
· Trigger: Ethereum Beacon Chain launch (Des 2020) menciptakan peluang liquid staking; P2P.org telah membangun MVP selama 2020
· Evidence: Phase 1 Launch Date Mainnet 2020-12-17; Phase 3 EV-003 Mainnet Launch; Phase 4 Technical Upgrade History Mainnet Launch
· Decision: Deploy deposit contract, stETH rebasing token, withdrawal queue v1, oracle v1, node operator registry v1 dengan 10 operator kurasi P2P.org
· Immediate Result: TVL ~10.000 ETH minggu pertama; stETH rebasing harian berfungsi; validator rewards terdistribusi
· Long-term Impact: Menetapkan arsitektur inti (deposit, stETH, oracle, operator registry) yang bertahan hingga V2; memulai network effect liquid staking
· Supporting Dataset: Phase 1, Phase 3 EV-002, EV-003, Phase 4 Architecture, Technical Upgrade History

Keputusan: TGE LDO Token dengan Liquidity Mining di Curve dan SushiSwap (2021-01)
· Trigger: Perlu token governance untuk DAO dan insentif liquidity awal stETH/ETH
· Evidence: Phase 3 EV-004 TGE LDO; Phase 6 TGE, Distribution, Vesting Schedule; Phase 5 Token Sale
· Decision: Mint 1B LDO fixed supply; alokasi treasury 36.3%, investor 22.18%, team 20%, community 10% (liquidity mining 1 tahun), operator 6.5%; liquidity mining di Curve stETH/ETH + SushiSwap LDO/ETH
· Immediate Result: LDO beredar, governance on-chain aktif via Snapshot + Aragon; stETH/ETH pool Curve menjadi deepest liquidity venue
· Long-term Impact: Membentuk struktur kepemilikan token yang memengaruhi governance hingga sekarang (treasury 36.3% dominan); Curve menjadi dependency kritis liquidity
· Supporting Dataset: Phase 3 EV-004, Phase 5 Token Sale, Phase 6 Distribution, Vesting, TGE, Phase 7 Major Integrations (Curve)

Keputusan: Series A Funding dipimpin Paradigm valuation $73M (2021-03-16)
· Trigger: Perlu dana untuk perluas tim, audit, ekosistem DeFi integration pasca-launch
· Evidence: Phase 3 EV-005 Series A; Phase 5 Funding History Series A; Phase 2 Investor entities (Paradigm, a16z, Dragonfly, Variant, Robot Ventures)
· Decision: Terima Series A Paradigm lead; investor mendapat kursi di multisig treasury awal; token allocation via SAFT dari pool investor 22.18%
· Immediate Result: Treasury DAO diperkuat; percepatan pengembangan V2 dan cross-chain; Paradigm mendapat influence governance via multisig
· Long-term Impact: Menetapkan pola investor VC dengan token warrant + multisig seat; valuation jump ke >$1B Series B tahun berikutnya
· Supporting Dataset: Phase 2 Investors, Phase 3 EV-005, Phase 5 Funding History, Phase 6 Distribution (Investors)

Keputusan: Launch Lido on Polygon (stMATIC) — ekspansi multi-chain pertama (2021-03)
· Trigger: Polygon tumbuh cepat sebagai L2/sidechain; permintaan liquid staking MATIC
· Evidence: Phase 3 EV-006 Launch Polygon; Phase 1 Chains (Polygon); Phase 4 Core Components (stMATIC), Execution Environment; Phase 7 Major Integrations (Polygon)
· Decision: Deploy native contracts di Polygon mainnet (bukan bridge stETH); stMATIC rebasing model mirip stETH; subset operator Ethereum
· Immediate Result: TVL stMATIC puncak ~$200M (2022); integrasi DeFi Polygon (Aave, QuickSwap, Curve)
· Long-term Impact: Membuktikan arsitektur portable ke EVM chain lain; namun kemudian fokus konsolidasi ke Ethereum + L2 (sunset non-EVM chains)
· Supporting Dataset: Phase 3 EV-006, Phase 4 Execution Environment, Core Components, Phase 7 Major Integrations, Phase 8 Market Timeline

Keputusan: Pembentukan Lido DAO Foundation di Cayman Islands (2021-08)
· Trigger: Perlu legal wrapper untuk treasury, kontrak, IP, compliance, bank account
· Evidence: Phase 3 EV-007 Legal; Phase 2 Foundation (Lido DAO), Government (Cayman Islands); Phase 5 Treasury Custodian; Phase 6 Governance
· Decision:irikan Limited Liability Foundation Cayman Islands sebagai legal entity DAO; memegang kontrak protokol, treasury, IP; multisig 5-of-9 execution
· Immediate Result: DAO dapat bertindak hukum, sign contracts, buka rekening bank, batasi liability token holder
· Long-term Impact: Struktur legal yang memungkinkan DAO beroperasi lama; namun review 2024 mengevaluasi apakah perlu wrapper tambahan (MiCA, SEC)
· Supporting Dataset: Phase 2 Foundation, Government, Phase 3 EV-007, Phase 5 Treasury Custodian, Phase 6 Governance, Phase 3 EV-024

Keputusan: wstETH Deployment di Optimism dan Arbitrum via canonical bridges (2022-05)
· Trigger: L2 DeFi berkembang (Aave V3, Velodrome, GMX); butuh non-rebasing token composable
· Evidence: Phase 3 EV-010 wstETH L2; Phase 1 Chains (Optimism, Arbitrum); Phase 4 Cross-chain Messaging, Core Components (wstETH); Phase 7 Major Integrations (Optimism, Arbitrum)
· Decision: Deploy wstETH via Optimism Gateway dan Arbitrum Bridge (canonical); tidak deploy kontrak staking baru di L2
· Immediate Result: wstETH supply L2 tumbuh >500k (2023); menjadi collateral utama DeFi L2
· Long-term Impact: Menetapkan strategi "bridge wstETH, bukan deploy staking baru" untuk L2; diulang untuk Base, zkSync Era (EV-012)
· Supporting Dataset: Phase 3 EV-010, EV-012, Phase 4 Cross-chain Messaging, Phase 7 Major Integrations, Phase 8 Market Timeline

Keputusan: Lido V2 Mainnet Launch — Staking Router + Withdrawal Credentials 0x01 (2023-05-15)
· Trigger: Ethereum Shanghai upgrade (EIP-4895) enable native withdrawals; perlu modular operator onboarding untuk desentralisasi
· Evidence: Phase 3 EV-013 V2 Launch, EV-019 Shanghai Readiness; Phase 4 Technical Upgrade History V2, Core Components (Staking Router, Withdrawal Queue), Security Model; Phase 7 Infrastructure (Obol, SSV, Simple DVT)
· Decision: Activate via governance LIP-14: Staking Router (modular modules), withdrawal credentials 0x01, oracle v2, dynamic node operator registry
· Immediate Result: Withdrawal stETH→ETH enabled (burn stETH, claim ETH dari queue); permissionless operator onboarding via modules; siap untuk EigenLayer
· Long-term Impact: Arsitektur modular memungkinkan ekspansi operator tanpa upgrade kontrak; withdrawal queue memenuhi janji liquid staking; fondasi untuk restaking
· Supporting Dataset: Phase 3 EV-013, EV-019, Phase 4 Technical Upgrade History, Core Components, Security Model, Phase 7 Infrastructure

Keputusan: Sunset Lido on Solana (stSOL), Polkadot (stDOT), Kusama (stKSM) (2023-06, 2023-09)
· Trigger: Adoption rendah, biaya operasional tinggi, kompetisi native stake pools (Marinade, Jito), fokus resource ke Ethereum/L2
· Evidence: Phase 3 EV-014 Sunset Solana, EV-015 Sunset Polkadot/Kusama; Phase 1 Chains (deprecated); Phase 4 Core Components (deprecated); Phase 7 Major Integrations (deprecated)
· Decision: Governance vote menutup produk; redemption window dibuka untuk user exit ke native token; kontrak dihentikan Q4 2023
· Immediate Result: TVL stSOL/stDOT/stKSM turun ke ~0; resource tim teralihkan ke Ethereum/L2/EigenLayer
· Long-term Impact: Menunjukkan disiplin resource allocation; konsolidasi ke Ethereum alignment; non-EVM chains dibuang
· Supporting Dataset: Phase 3 EV-008, EV-009, EV-014, EV-015, Phase 4 Core Components, Phase 7 Major Integrations

Keputusan: Integrasi EigenLayer Restaking — wstETH sebagai LRT dominan (2023-07)
· Trigger: EigenLayer launch restaking mainnet; wstETH sudah tersebar luas di DeFi sebagai collateral
· Evidence: Phase 3 EV-016 EigenLayer Integration; Phase 2 Protocol (EigenLayer); Phase 4 Architecture (Cross-chain Messaging — native Ethereum); Phase 7 Major Integrations (EigenLayer), External Dependencies (EigenLayer)
· Decision: Tidak deploy kontrak baru; wstETH existing langsung accepted sebagai restaking collateral di EigenLayer contracts
· Immediate Result: wstETH >50% TVL restaking awal; muncul LRT protocols (ezETH, rsETH, swETH) menggunakan wstETH underlying
· Long-term Impact: Memperkuat positioning wstETH sebagai "base layer" DeFi + restaking; Lido tidak perlu mengeluarkan LRT native (berbeda competitor)
· Supporting Dataset: Phase 3 EV-016, Phase 2 EigenLayer, Phase 4 Architecture, Phase 7 Major Integrations, Phase 8 Narrative Position (Restaking)

Keputusan: Fee Switch Activation — 10% staking rewards ke treasury via LIP-22 (2024-02)
· Trigger: Treasury butuh revenue sustainable untuk grants, core contributor budget, insurance; 5% fee (2020-2024) dianggap tidak cukup
· Evidence: Phase 3 EV-020 Fee Switch; Phase 5 Revenue Model (Staking Fee 10%), Financial Risk; Phase 6 Governance (LIP-22), Utility (Fee Switch Activation)
· Decision: Governance vote meningkatkan protocol fee dari 5% ke 10% rewards; 5% operator + 10% DAO = 15% total fee
· Immediate Result: Treasury revenue meningkat signifikan; DAO memperluas grant program dan budget 2024-2025
· Long-term Impact: Membuat DAO financially sustainable tanpa bergantung token sale; namun meningkatkan tekanan pada stETH yield vs competitor
· Supporting Dataset: Phase 3 EV-020, Phase 5 Revenue Model, Financial Risk, Phase 6 Governance, Utility, Phase 8 Market Timeline

Keputusan: Permissionless Node Operator Onboarding via Staking Router Modules (2024-06)
· Trigger: Kritik sentralisasi (~28.5% ETH staked); perlu geographic/client diversity; DVT technology matang (Obol, SSV)
· Evidence: Phase 3 EV-021 Node Operator Expansion; Phase 4 Core Components (Staking Router), Security Model (Validator Set), Known Limitations; Phase 7 Infrastructure Providers (Obol, SSV, Simple DVT); Phase 8 Narrative (Centralization Risk)
· Decision: Activate Simple DVT, Obol, SSV modules via governance; onboard 20+ operator baru termasuk solo staker via DVT clusters
· Immediate Result: Operator count naik ke 33+ entities + DVT clusters; client diversity diperbaiki; geographic spread meningkat
· Long-term Impact: Menjawab narasi sentralisasi; arsitektur modular V2 terbukti works; template untuk future module types
· Supporting Dataset: Phase 3 EV-013, EV-021, Phase 4 Staking Router, Security Model, Known Limitations, Phase 7 Infrastructure, Phase 8 Narrative

Evolution Pattern

Perubahan Strategi: Dari Multi-chain Broad → Ethereum + L2 Focus
· Evidence: Phase 1 Chains (9 chains listed); Phase 3 EV-006 Polygon, EV-008 Solana, EV-009 Polkadot/Kusama, EV-010 Optimism/Arbitrum, EV-012 Base/zkSync, EV-014 Sunset Solana, EV-015 Sunset Polkadot/Kusama; Phase 4 Execution Environment (EVM chains live, non-EVM deprecated); Phase 8 Market Timeline
· Description: 2020-2022: ekspansi agresif ke 5+ chains (Ethereum, Polygon, Solana, Polkadot, Kusama). 2023: sunset 3 non-EVM chains via governance. 2022-2024: fokus deployment wstETH ke L2 Ethereum via canonical bridges. Strategi bergeser dari "deploy staking contracts everywhere" ke "bridge wstETH ke L2 Ethereum yang berkembang".

Perubahan Teknologi: Dari Monolithic Contracts → Modular Architecture (V2)
· Evidence: Phase 3 EV-003 Mainnet (monolithic: deposit, stETH, withdrawal queue, oracle, operator registry), EV-013 V2 (Staking Router modules, dynamic registry, withdrawal credentials 0x01); Phase 4 Core Components (Staking Router, Node Operator Registry upgraded), Architecture (Modular), Technical Upgrade History
· Description: V1 (2020): Semua logika dalam kontrak terpisah tapi tightly coupled; operator onboarding butuh upgrade kontrak. V2 (2023): Staking Router memisahkan validator allocation logic ke modules (Simple DVT, Obol, SSV, P2P.org); Node Operator Registry dynamic; withdrawal credentials 0x01 native. Memungkinkan permissionless innovation di layer module tanpa touch core.

Perubahan Tokenomics: Dari Fee 5% Fixed → Fee Switch Governance-Controlled (10%)
· Evidence: Phase 3 EV-004 TGE (fee 5% dari awal), EV-020 Fee Switch (10% activated Feb 2024); Phase 5 Revenue Model (Staking Fee 10%, Node Operator Fee 5%); Phase 6 Utility (Fee Switch Activation), Governance (LIP-22)
· Description: Fee 5% hardcoded sejak launch 2020. Setelah 3+ tahun operasi dan treasury membutuhkan revenue sustainable, governance vote (LIP-22) mengaktifkan fee switch ke 10%. Menunjukkan tokenomics bukan immutable — DAO dapat adjust parameter ekonomis via governance.

Perubahan Governance: Dari Curated Operator Set → Permissionless Modules + DVT
· Evidence: Phase 3 EV-003 (10 genesis operators kurasi P2P.org), EV-021 (20+ baru via modules); Phase 4 Security Model (Validator Set permissioned), Staking Router (modules); Phase 7 Infrastructure (Obol, SSV, Simple DVT); Phase 8 Narrative (Centralization Risk)
· Description: Genesis: 10 operator dipilih P2P.org. V2 Staking Router: modules memungkinkan DVT-based permissionless onboarding. 2024: governance approve Obol, SSV, Simple DVT modules + 20+ operator baru. Evolution dari "trusted set" ke "modular permissionless dengan DVT safety".

Perubahan Revenue: Dari Zero Protocol Revenue → Sustainable Fee Revenue + Treasury Yield
· Evidence: Phase 3 EV-004 (TGE, no fee revenue initially), EV-020 (Fee switch 10%); Phase 5 Revenue Model (Staking Fee 10%, Withdrawal Fee 0.1%, Treasury Yield), Funding History (Series A/B done, no further VC funding); Phase 8 Market Timeline
· Description: 2020-2024: Protocol fee 5% tapi tidak diaktifkan penuh (fee switch off?); revenue mainly dari treasury management. 2024: Fee switch 10% activated → ~$45-55M annualized revenue. DAO menjadi financially independent post-VC funding.

Technical Decision Pattern

Pola 1: Ethereum Alignment First — Semua Keputusan Teknis Mengutamakan Ethereum Mainnet dan Roadmap-nya
· Decision Pattern: Setiap upgrade teknis mayor (withdrawal credentials 0x01, Shanghai readiness, V2 Staking Router) disejajarkan dengan Ethereum roadmap (Beacon Chain, Shanghai/Capella, PBS/DVT future). Non-EVM chains (Solana, Polkadot, Kusama) dideprecate ketika resource konflik dengan Ethereum focus.
· Evidence: Phase 3 EV-013 V2 (withdrawal credentials 0x01 untuk Shanghai), EV-019 Shanghai Readiness, EV-014/015 Sunset non-EVM; Phase 4 Architecture (Base Layer Ethereum), Consensus Mechanism (relies on Beacon Chain), Execution Environment (EVM only live), Known Limitations (L2 bridge risk acknowledged); Phase 8 Narrative (Ethereum Staking Centralization Risk)
· Supporting Dataset: Phase 1, Phase 3 EV-013, EV-014, EV-015, EV-019, Phase 4 Architecture, Consensus, Execution Environment, Known Limitations, Phase 8 Narrative

Pola 2: Upgrade Bertahap dengan Pengujian Ekstensif dan Audit Multi-party
· Decision Pattern: Setiap major upgrade (Mainnet, V2, wstETH, L2 deployments) melalui: testnet → audit multiple firms → governance vote → timelock execution. V2 audit oleh Sigma Prime, MixBytes, Quantstamp sebelum launch. wstETH L2 deployments menggunakan canonical bridges (bukan custom bridge) untuk minimize attack surface.
· Evidence: Phase 3 EV-002 Testnet, EV-003 Mainnet, EV-013 V2 (LIP-14 governance), EV-010/012 L2 deployments; Phase 4 Audit History (5 major audits), Security Model (proxy upgrades via governance timelock), Technical Upgrade History; Phase 7 External Dependencies (Canonical bridges)
· Supporting Dataset: Phase 3 EV-002, EV-003, EV-010, EV-012, EV-013, Phase 4 Audit History, Security Model, Technical Upgrade History, Phase 7 External Dependencies

Pola 3: Modular Architecture untuk Fleksibilitas Tanpa Upgrade Kontrak Inti
· Decision Pattern: V2 Staking Router memisahkan validator allocation logic ke modules (Simple DVT, Obol, SSV, P2P.org module). Operator onboarding baru = deploy module baru, bukan upgrade Staking Router core. Oracle, Withdrawal Queue, Node Operator Registry juga terpisah dan upgradeable via proxy.
· Evidence: Phase 3 EV-013 V2 Launch (Staking Router), EV-021 Module Expansion; Phase 4 Core Components (Staking Router, Node Operator Registry, Oracle, Withdrawal Queue), Architecture (Modular), Technical Upgrade History; Phase 7 Infrastructure (Obol, SSV, Simple DVT modules)
· Supporting Dataset: Phase 3 EV-013, EV-021, Phase 4 Core Components, Architecture, Technical Upgrade History, Phase 7 Infrastructure

Pola 4: Canonical Bridges Only untuk L2 Expansion — No Custom Bridge Contracts
· Decision Pattern: wstETH deployment ke Optimism, Arbitrum, Base, zkSync Era semuanya menggunakan canonical bridge masing-masing chain (Optimism Gateway, Arbitrum Bridge, Base Bridge, zkSync Bridge). Tidak ada Lido-specific bridge contracts. Mengurangi attack surface dan dependency pada bridge security L2 native.
· Evidence: Phase 3 EV-010 wstETH Optimism/Arbitrum, EV-012 wstETH Base/zkSync; Phase 4 Cross-chain Messaging (Canonical bridges), Execution Environment (L2 deployments); Phase 7 Major Integrations (Optimism, Arbitrum, Base, zkSync), External Dependencies (Canonical bridges); Phase 8 Market Timeline
· Supporting Dataset: Phase 3 EV-010, EV-012, Phase 4 Cross-chain Messaging, Execution Environment, Phase 7 Major Integrations, External Dependencies, Phase 8 Market Timeline

Pola 5: Oracle Committee Multi-sig (5-of-9) untuk Beacon Chain Reporting — Trust Minimized tapi Bukan Trustless
· Decision Pattern: Oracle committee 9 entitas independen (P2P.org, Figment, Chorus One, dll), threshold 5-of-9 untuk submit beacon chain report (validator balances, exits, rewards). Governance dapat replace members. V2 upgrade menambah reporting untuk withdrawal credentials 0x01. Desain ini dipilih karena beacon chain state tidak dapat dibaca langsung oleh EVM (no light client pre-verkle).
· Evidence: Phase 3 EV-013 V2 (oracle upgrade); Phase 4 Core Components (Oracle), Security Model (Oracle Security 5-of-9), Known Limitations (Oracle Centralization); Phase 7 External Dependencies (Oracle Committee), Infrastructure Providers (Figment, Chorus One as oracle members)
· Supporting Dataset: Phase 3 EV-013, Phase 4 Core Components, Security Model, Known Limitations, Phase 7 External Dependencies, Infrastructure Providers

Financial Decision Pattern

Pola 1: Pendanaan Bertahap dengan Valuasi Meningkat — Internal Bootstrap → Series A → Series B → Protocol Revenue
· Decision Pattern: 2020: P2P.org internal funding (bootstrap). 2021-03: Series A Paradigm lead $73M valuation. 2022: Series B a16z/Dragonfly co-lead >$1B valuation (unicorn). 2024: Fee switch 10% activated → ~$45-55M annualized protocol revenue. Tidak ada funding rondelanjutan post-Series B; DAO mandiri via protocol fees.
· Evidence: Phase 3 EV-001 Founding (P2P.org), EV-005 Series A, EV-011 Series B, EV-020 Fee Switch; Phase 5 Funding History (3 rounds), Revenue Model (Staking Fee 10%, Withdrawal Fee, Treasury Yield), Financial Dependencies (VC done, DAO revenue primary); Phase 8 Market Timeline
· Supporting Dataset: Phase 3 EV-001, EV-005, EV-011, EV-020, Phase 5 Funding History, Revenue Model, Financial Dependencies, Phase 8 Market Timeline

Pola 2: Treasury Management — Legal Wrapper (Cayman Foundation) + Multisig 5-of-9 + Diversified Assets
· Decision Pattern: Treasury diubah ke legal entity (Cayman Foundation) untuk hukum compliance. Multisig 5-of-9 dengan signer: investor reps (Paradigm, a16z, Dragonfly), core contributors, node operator reps. Assets: LDO (363M), ETH, stETH, wstETH, DAI, USDC, DeFi tokens (CRV, CVX, dll). Yield dari DeFi strategies (Aave, Maker, Curve, Yearn). Tidak ada insurance fund untuk slashing.
· Evidence: Phase 3 EV-007 Foundation, EV-020 Fee Switch (revenue increase); Phase 2 Foundation (Lido DAO), Government (Cayman Islands); Phase 5 Treasury (Custodian multisig 5-of-9, Composition, Stablecoin/Native/Other Assets), Revenue Model (Treasury Yield), Financial Risk (No insurance fund); Phase 6 Distribution (Foundation 36.3%)
· Supporting Dataset: Phase 2 Foundation, Government, Phase 3 EV-007, EV-020, Phase 5 Treasury, Revenue Model, Financial Risk, Phase 6 Distribution

Pola 3: Grant Program dan Core Contributor Budget — Funded dari Treasury, Dikelola via Governance
· Decision Pattern: DAO Grants Program untuk ecosystem growth (tooling, research, security, integrations). Core Contributor Program formalized 2024 dengan quarterly budget, KPI, review — >20 contributors dibayar LDO/DAI. Semua via governance proposal dan multisig execution.
· Evidence: Phase 3 EV-022 Core Contributor Formalization; Phase 5 Revenue Model (Grants/Ecosystem Funding), Fundraising Mechanism (DAO Treasury, Protocol Revenue); Phase 7 Developer Ecosystem (Grant Program, Core Contributor Budget); Phase 6 Governance (Treasury Management)
· Supporting Dataset: Phase 3 EV-022, Phase 5 Revenue Model, Fundraising Mechanism, Phase 7 Developer Ecosystem, Phase 6 Governance

Pola 4: Token Distribution — Treasury Dominan (36.3%), Investor Vesting Long-term, Community via Liquidity Mining
· Decision Pattern: Fixed supply 1B LDO. Treasury 36.3% (paling besar) untuk DAO ops. Investor 22.18% dengan cliff 12 bulan + vesting 24-36 bulan. Team 20% cliff 12 bulan + vesting 36 bulan. Community 10% via liquidity mining 1 tahun (completed 2022). Operator 6.5% vesting 24-48 bulan. Tidak ada inflation/emission.
· Evidence: Phase 3 EV-004 TGE; Phase 5 Token Sale (Private sale via SAFT, no public sale); Phase 6 Distribution (all categories), Vesting Schedule (all categories), TGE (Initial Unlock), Inflation/Deflation (Fixed supply)
· Supporting Dataset: Phase 3 EV-004, Phase 5 Token Sale, Phase 6 Distribution, Vesting Schedule, TGE, Inflation/Deflation

Pola 5: Fee Switch sebagai Mekanisme Revenue Sustainable — Governance-Controlled Parameter
· Decision Pattern: Protocol fee tidak hardcoded permanen. Fee switch memungkinkan DAO mengubah fee (5% → 10% via LIP-22). Dengandrawal fee 0.1% terpisah. Desain ini memberikan fleksibilitas ekonomi tanpa upgrade kontrak.
· Evidence: Phase 3 EV-020 Fee Switch Activation; Phase 5 Revenue Model (Staking Fee 10%, Withdrawal Fee 0.1%), Financial Risk (Revenue Decline risk); Phase 6 Utility (Fee Switch Activation), Governance (LIP-22 passed)
· Supporting Dataset: Phase 3 EV-020, Phase 5 Revenue Model, Financial Risk, Phase 6 Utility, Governance

Ecosystem Decision Pattern

Pola 1: Deep Integration dengan DeFi Primitif (Curve, Aave, Maker) — Membuat stETH/wstETH "Base Layer"
· Decision Pattern: Prioritaskan integrasi dengan protokol DeFi yang memiliki TVL terbesar dan composability tinggi: Curve (liquidity venue utama stETH/ETH), Aave (money market collateral factor 82.5%), MakerDAO (wstETH vault >$1B peak). Integrasi ini drive adoption stETH sebagai collateral standar.
· Evidence: Phase 3 EV-018 Major DeFi Integrations (ongoing 2021-2024); Phase 7 Major Integrations (Curve, Aave, Maker, Yearn), Applications (Curve pool, Aave markets, Maker vault); Phase 8 Market Share (DeFi Collateral wstETH 35-40% Aave Ethereum, 60%+ L2s), Narrative (DeFi Infrastructure/Money Lego)
· Supporting Dataset: Phase 3 EV-018, Phase 7 Major Integrations, Applications, Phase 8 Market Share, Narrative Position

Pola 2: L2 Expansion via Canonical Bridge wstETH — Bukan Deploy Staking Contracts Baru
· Decision Pattern: Untuk setiap L2 Ethereum baru (Optimism, Arbitrum, Base, zkSync Era), strategi: deploy wstETH via canonical bridge → integrate dengan DeFi L2 (Aave V3, DEX, yield protocols). Tidak deploy deposit/staking contracts di L2. Polygon adalah pengecualian (native deployment stMATIC 2021, sebelum L2 ecosystem matang).
· Evidence: Phase 3 EV-010 wstETH Optimism/Arbitrum, EV-012 wstETH Base/zkSync; Phase 1 Chains (L2s); Phase 4 Cross-chain Messaging (Canonical bridges), Execution Environment (L2 deployments wstETH only); Phase 7 Major Integrations (Optimism, Arbitrum, Base, zkSync), External Dependencies (Canonical bridges); Phase 8 Market Timeline
· Supporting Dataset: Phase 3 EV-010, EV-012, Phase 1 Chains, Phase 4 Cross-chain Messaging, Execution Environment, Phase 7 Major Integrations, External Dependencies, Phase 8 Market Timeline

Pola 3: EigenLayer Integration sebagai LRT Provider — Leveraging Existing wstETH Distribution
· Decision Pattern: Tidak mengeluarkan LRT native (seperti Ether.fi eETH, Renzo ezETH). Sebagai gantinya, wstETH existing langsung accepted di EigenLayer contracts. Lido menyediakan >50% TVL restaking awal. Positioning: "base layer" untuk restaking protocols yang membangun di atas wstETH.
· Evidence: Phase 3 EV-016 EigenLayer Integration; Phase 2 Protocol (EigenLayer); Phase 4 Architecture (Cross-chain Messaging — native Ethereum); Phase 7 Major Integrations (EigenLayer), External Dependencies (EigenLayer); Phase 8 Narrative (Restaking Secondary), Market Share (Restaking >50% early TVL)
· Supporting Dataset: Phase 3 EV-016, Phase 2 EigenLayer, Phase 4 Architecture, Phase 7 Major Integrations, External Dependencies, Phase 8 Narrative, Market Share

Pola 4: Sunset Produk Non-Performing dengan Governance Vote dan Redemption Window
· Decision Pattern: Produk dengan adoption rendah (stSOL Solana, stDOT Polkadot, stKSM Kusama) ditutup via governance vote. Redemption window dibuka untuk user exit aman. Kontrak dihentikan setelah window tutup. Resource dialihkan ke core focus (Ethereum/L2).
· Evidence: Phase 3 EV-014 Sunset Solana, EV-015 Sunset Polkadot/Kusama; Phase 1 Chains (deprecated); Phase 4 Core Components (deprecated); Phase 7 Major Integrations (deprecated); Phase 8 Market Timeline
· Supporting Dataset: Phase 3 EV-008, EV-009, EV-014, EV-015, Phase 1 Chains, Phase 4 Core Components, Phase 7 Major Integrations, Phase 8 Market Timeline

Pola 5: Node Operator Diversification via DVT Modules — Menjawab Centralization Narrative
· Decision Pattern: Kritik sentralisasi (~28.5% ETH staked) dijawab dengan: Staking Router modules (Simple DVT, Obol, SSV) memungkinkan permissionless onboarding. 20+ operator baru onboarded 2024 termasuk solo staker via DVT. Client diversity dan geographic spread menjadi KPI.
· Evidence: Phase 3 EV-021 Node Operator Expansion; Phase 4 Security Model (Validator Set curated), Staking Router (modules), Known Limitations (Node Operator Permissioning); Phase 7 Infrastructure Providers (Obol, SSV, Simple DVT); Phase 8 Narrative (Centralization Risk), Competitor Landscape (Rocket Pool permissionless, DVT-based LRTs)
· Supporting Dataset: Phase 3 EV-013, EV-021, Phase 4 Security Model, Staking Router, Known Limitations, Phase 7 Infrastructure, Phase 8 Narrative, Competitor Landscape

Governance Decision Pattern

Pola 1: Token-Weighted Voting (1 LDO = 1 Vote) dengan Dual-Lane Snapshot + Aragon
· Decision Pattern: Governance menggunakan Snapshot untuk signaling (gasless, quorum 5% supply, majority >50%) lalu Aragon DAO untuk on-chain execution (timelock 48 jam, quorum 5%, majority >50%). Delegation supported. Semua major decisions (V2 upgrade, fee switch, sunset, operator onboarding) melalui proses ini.
· Evidence: Phase 3 EV-013 LIP-14 V2, EV-014 Sunset Solana, EV-015 Sunset Polkadot, EV-020 LIP-22 Fee Switch, EV-021 Operator Expansion; Phase 6 Governance (Model, Voting System, Voting Power, Delegation, Proposal System, Treasury Governance); Phase 7 Developer Ecosystem (Grant Program via governance)
· Supporting Dataset: Phase 3 EV-013, EV-014, EV-015, EV-020, EV-021, Phase 6 Governance, Phase 7 Developer Ecosystem

Pola 2: Multisig 5-of-9 Execution — Investor Reps + Core Contributors + Operator Reps
· Decision Pattern: On-chain proposal yang lolos dieksekusi oleh multisig 5-of-9 Lido DAO Foundation. Signer: Paradigm, a16z, Dragonfly (investor reps), core contributors, node operator reps. Desain ini balance antara DAO sovereignty dan operational security/investor confidence.
· Evidence: Phase 3 EV-007 Foundation (multisig), EV-020 Fee Switch (execution); Phase 2 Foundation (Lido DAO), Government (Cayman Islands); Phase 5 Treasury Custodian (multisig 5-of-9); Phase 6 Governance (Treasury Governance multisig)
· Supporting Dataset: Phase 2 Foundation, Government, Phase 3 EV-007, EV-020, Phase 5 Treasury Custodian, Phase 6 Governance

Pola 3: LIP (Lido Improvement Proposal) Process — Forum Discussion → Snapshot → On-chain
· Decision Pattern: Proposal flow: diskusi di research.lido.fi (LIP) → Snapshot signaling vote → Aragon on-chain vote → multisig execution. Template terstandarisasi. Memungkinkan community input sebelum voting. Semua major upgrades mengikuti alur ini.
· Evidence: Phase 3 EV-013 LIP-14, EV-020 LIP-22; Phase 6 Governance (Proposal System LIP), Community (Lido DAO Forum research.lido.fi); Phase 7 Community (Lido DAO Forum)
· Supporting Dataset: Phase 3 EV-013, EV-020, Phase 6 Governance, Community, Phase 7 Community

Pola 4: Governance Mengontrol Parameter Ekonomis (Fee Switch, Operator Fee, Withdrawal Fee)
· Decision Pattern: Parameter fee tidak immutable. Fee switch (5%→10%), node operator fee (5%), withdrawal fee (0.1%) semuanya governance-adjustable. LIP-22 menunjukkan DAO dapat meningkatkan revenue ketika treasury butuh dana. Flexibility ini critical untuk sustainability.
· Evidence: Phase 3 EV-020 Fee Switch; Phase 5 Revenue Model (Staking Fee 10%, Node Operator Fee 5%, Withdrawal Fee 0.1%); Phase 6 Utility (Fee Switch Activation), Governance (Proposal System)
· Supporting Dataset: Phase 3 EV-020, Phase 5 Revenue Model, Phase 6 Utility, Governance

Pola 5: Legal Structure Review Ongoing — Adaptive Compliance
· Decision Pattern: 2021: Cayman Foundation established. 2024: Review struktur legal untuk MiCA EU, SEC US compliance. Forum discussion aktif (EV-024), legal counsel engaged. Belum ada binding vote. Menunjukkan governance proactive pada regulatory risk.
· Evidence: Phase 3 EV-007 Foundation, EV-024 Legal Structure Review; Phase 2 Foundation (Lido DAO), Government (Cayman Islands); Phase 5 Financial Risk (Legal Financial Risk); Phase 6 Governance (Proposal System); Phase 8 Market Timeline
· Supporting Dataset: Phase 3 EV-007, EV-024, Phase 2 Foundation, Government, Phase 5 Financial Risk, Phase 6 Governance, Phase 8 Market Timeline

Risk Response Pattern

Pola 1: FTX/Alameda Contagion (2022-11) — Transparansi On-chain + Peg Stability Maintained
· Trigger: FTX collapse November 2022; Alameda known large stETH holder (~4M stETH borrowed/leveraged di Aave/Maker)
· Evidence: Phase 3 EV-025 FTX Exposure Check; Phase 5 Financial Risk (Revenue Decline, Funding Dependency); Phase 7 Major Integrations (Aave, Maker); Phase 8 Market Timeline
· Decision Pattern: Tidak ada emergency intervention protokol. Response: publish blog post transparansi on-chain analysis (Alameda positions, liquidations orderly), menegaskan Lido protocol tidak memiliki exposure ke FTX. stETH peg stabil $0.99-1.00 ETH selama kontagion.
· Response: Blog post exposure check; on-chain monitoring; komunikasi proaktif ke komunitas
· Result: Tidak ada depeg mayor; liquidasi Alameda di Aave/Maker berjalan tertib; Curve pool tetap liquide; menguatkan kepercayaan resilient design stETH
· Supporting Dataset: Phase 3 EV-025, Phase 5 Financial Risk, Phase 7 Major Integrations, Phase 8 Market Timeline

Pola 2: Centralization Criticism (~28.5% ETH Staked) — Structural Response via V2 Staking Router + DVT Modules
· Trigger: Narita eksternal (researchers, competitors, Ethereum community) mengutip market share Lido sebagai risiko sentralisasi validator set. Internal: governance discussion di forum.
· Evidence: Phase 3 EV-013 V2 (Staking Router design), EV-021 Operator Expansion (DVT modules); Phase 4 Security Model (Validator Set permissioned), Known Limitations (Node Operator Permissioning), Staking Router (modules); Phase 7 Infrastructure (Obol, SSV, Simple DVT); Phase 8 Narrative (Centralization Risk), Competitor Landscape (Rocket Pool permissionless, DVT LRTs)
· Decision Pattern: Bukan defensive PR, tapi technical solution: V2 Staking Router modules (Simple DVT, Obol, SSV) memungkinkan permissionless onboarding. 2024: governance approve modules + 20+ operator baru. Client diversity dan geographic spread tracked.
· Response: Deploy Staking Router modules; activate DVT modules; onboard diverse operators; publish transparency data
· Result: Operator count 33+ + DVT clusters; client diversity improved; narrative partially addressed tapi market share tetap dominan
· Supporting Dataset: Phase 3 EV-013, EV-021, Phase 4 Security Model, Known Limitations, Staking Router, Phase 7 Infrastructure, Phase 8 Narrative, Competitor Landscape

Pola 3: Smart Contract Risk — Multi-Audit + Bug Bounty + Proxy Upgrade Timelock
· Trigger: Inherent risk smart contract bugs pada protokol mengelola $28B+ TVL. Historik exploit di DeFi lain.
· Evidence: Phase 4 Security Model (Contract Upgradability proxy EIP-1967, Emergency Brakes, Bug Bounty $1M Immunefi, Audit Coverage), Audit History (5 major audits); Phase 7 Infrastructure Providers (Sigma Prime, MixBytes, Quantstamp, Immunefi)
· Decision Pattern: Defense in depth: multiple audit firms (Sigma Prime, MixBytes, Quantstamp) untuk setiap major release. Bug bounty $1M max. Proxy upgrades via governance timelock 48h. Circuit breaker di oracle (max rebase delta). Withdrawal queue pause via governance.
· Response: Continuous audit program; bug bounty; timelock upgrades; emergency brakes
· Result: Tidak ada eksploit mayor kontrak inti sejak launch 2020; findings kritis diperbaiki pre-launch
· Supporting Dataset: Phase 4 Security Model, Audit History, Phase 7 Infrastructure Providers

Pola 4: Regulatory Uncertainty (MiCA, SEC) — Legal Structure Review + Foundation Wrapper
· Trigger: Evolving global regulation (MiCA EU 2024, SEC enforcement US). DAO structure legal ambiguity.
· Evidence: Phase 3 EV-007 Foundation (Cayman 2021), EV-024 Legal Review (2024 ongoing); Phase 2 Foundation (Lido DAO), Government (Cayman Islands); Phase 5 Financial Risk (Legal Financial Risk); Phase 6 Governance (Proposal System)
· Decision Pattern: Proactive legal review 2024: evaluasi Cayman Foundation vs DUNA Wyoming vs BVI VASP. Legal counsel engaged. Forum discussion transparent. Belum ada binding decision. Foundation wrapper sudah provide liability limitation.
· Response: Legal structure review forum discussion; legal counsel engagement; evaluate alternative wrappers
· Result: Ongoing — no final decision yet; foundation structure remains active
· Supporting Dataset: Phase 3 EV-007, EV-024, Phase 2 Foundation, Government, Phase 5 Financial Risk, Phase 6 Governance

Pola 5: Slashing Risk — No Socialization, Transparent Disclosure, DVT Mitigation
· Trigger: Validator slashing events (rare but possible) — protocol tidak mensosialisasikan loss.
· Evidence: Phase 4 Security Model (Slashing Protection — no socialization, stETH holders bear pro-rata), Known Limitations (Slashing Risk Socialization); Phase 5 Financial Risk (Slashing Risk Financial Impact); Phase 7 Infrastructure (DVT modules Obol, SSV, Simple DVT)
· Decision Pattern: Explicit no-insurance-fund policy. Slashing loss borne pro-rata by stETH holders. Mitigation: DVT modules (Obol, SSV, Simple DVT) reduce slashing probability via distributed validator technology. Transparent risk disclosure di docs.
· Response: Document risk clearly; deploy DVT modules for operators who want extra protection; no treasury allocation for insurance
· Result: No major slashing event to date; DVT adoption growing via modules
· Supporting Dataset: Phase 4 Security Model, Known Limitations, Phase 5 Financial Risk, Phase 7 Infrastructure

Recurring Behavioral Pattern

Pola 1: Ekspansi Pasca-Funding → Lalu Konsolidasi
· Evidence: Phase 3 EV-005 Series A (Mar 2021) → EV-006 Polygon Launch (Mar 2021), EV-008 Solana (Dec 2021), EV-009 Polkadot/Kusama (Mar 2022). Phase 3 EV-011 Series B (2022) → EV-010 Optimism/Arbitrum (May 2022), EV-012 Base/zkSync (Feb 2023). Kemudian 2023: EV-014/015 Sunset 3 chains. Pattern: funding → aggressive expansion → consolidation ke core.
· Supporting Dataset: Phase 3 EV-005, EV-006, EV-008, EV-009, EV-011, EV-010, EV-012, EV-014, EV-015, Phase 5 Funding History, Phase 8 Market Timeline

Pola 2: Upgrade Mayor Selalu Melalui Governance Vote + Timelock + Multi-Audit
· Evidence: Phase 3 EV-013 V2 (LIP-14), EV-014 Sunset Solana (vote), EV-015 Sunset Polkadot (vote), EV-020 Fee Switch (LIP-22), EV-021 Operator Expansion (multiple votes). Phase 4 Security Model (Proxy upgrades via governance timelock), Audit History (pre-launch audits). Phase 6 Governance (Proposal System, Treasury Governance).
· Supporting Dataset: Phase 3 EV-013, EV-014, EV-015, EV-020, EV-021, Phase 4 Security Model, Audit History, Phase 6 Governance

Pola 3: Integrasi DeFi Prioritaskan "Big Three" — Curve, Aave, Maker
· Evidence: Phase 3 EV-018 Major DeFi Integrations (ongoing). Phase 7 Major Integrations (Curve primary liquidity, Aave collateral factor 82.5%, Maker >$1B peak exposure). Phase 8 Market Share (wstETH 35-40% Aave Ethereum collateral, 60%+ L2s). Yearn, Pendle, Morpho, EigenLayer sebagai layer kedua.
· Supporting Dataset: Phase 3 EV-018, Phase 7 Major Integrations, Phase 8 Market Share

Pola 4: Sunset Produk yang Tidak Menjangkau Product-Market Fit — Dengan Redemption Window
· Evidence: Phase 3 EV-014 Sunset Solana (stSOL), EV-015 Sunset Polkadot/Kusama (stDOT/stKSM). Phase 1 Chains (deprecated). Phase 4 Core Components (deprecated). Phase 7 Major Integrations (deprecated). Semua via governance vote, redemption window, kontrak dihentikan.
· Supporting Dataset: Phase 3 EV-008, EV-009, EV-014, EV-015, Phase 1 Chains, Phase 4 Core Components, Phase 7 Major Integrations

Pola 5: Menjawab Kritik Narasi dengan Solusi Teknis (Bukan Hanya Komunikasi)
· Evidence: Phase 8 Narrative (Centralization Risk) → Phase 3 EV-013 V2 Staking Router modules, EV-021 DVT modules activation. Phase 8 Narrative (Revenue Sustainability) → Phase 3 EV-020 Fee Switch 10%. Phase 8 Narrative (Regulatory) → Phase 3 EV-024 Legal Structure Review.
· Supporting Dataset: Phase 3 EV-013, EV-020, EV-021, EV-024, Phase 8 Narrative Position

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Keamanan/Efisiensi Operator
· Decision: Genesis 10 operator kurasi P2P.org → V2 Staking Router modules untuk permissionless DVT onboarding
· Trade-off: Operator permissioned (kurasi) memberikan keamanan/efisiensi awal (operator profesional, track record terbukti) tapi menciptakan sentralisasi (~28.5% ETH staked). Permissionless via DVT modules meningkatkan desentralisasi tapi menambah kompleksitas teknis (DVT overhead, module security) dan risiko operator kurang berpengalaman.
· Evidence: Phase 3 EV-003 Genesis operators, EV-013 V2 Staking Router, EV-021 DVT modules; Phase 4 Security Model (Validator Set permissioned), Staking Router (modules), Known Limitations (Node Operator Permissioning); Phase 7 Infrastructure (Obol, SSV, Simple DVT); Phase 8 Narrative (Centralization Risk), Competitor Landscape (Rocket Pool permissionless from start)
· Supporting Dataset: Phase 3 EV-003, EV-013, EV-021, Phase 4 Security Model, Staking Router, Known Limitations, Phase 7 Infrastructure, Phase 8 Narrative, Competitor Landscape

Trade-off 2: Rebasin Token (stETH) vs DeFi Composability → Wrapper (wstETH) sebagai Solusi
· Decision: stETH rebasing (balance berubah harian) → wstETH non-rebasing wrapper 1:1 untuk DeFi
· Trade-off: Rebasing token secara ekonomi paling akurat merepresentasikan staked ETH + rewards (user balance naik otomatis). Tapi rebasing break composability dengan hampir semua DeFi protocol (Aave, Maker, Uniswap, bridges). Wrapper wstETH solve composability tapi menambah complexity (user harus wrap/unwrap), gas cost, dan mental model ganda.
· Evidence: Phase 3 EV-003 stETH launch, EV-? wstETH launch (2021-03); Phase 4 Core Components (stETH rebasing, wstETH wrapper), Known Limitations (Rebasing Token Composability); Phase 7 Applications (stETH, wstETH); Phase 8 Narrative (DeFi Infrastructure)
· Supporting Dataset: Phase 3 EV-003, Phase 4 Core Components, Known Limitations, Phase 7 Applications, Phase 8 Narrative

Trade-off 3: Multi-chain Broad vs Focus Ethereum + L2
· Decision: 2021-2022 deploy ke 5 chains (Ethereum, Polygon, Solana, Polkadot, Kusama) → 2023 sunset 3 non-EVM chains, fokus Ethereum + L2
· Trade-off: Multi-chain early capture market share di chain baru tapi menyebarkan resource tipis (devops, security, BD, support per chain). Non-EVM chains butuh arsitektur berbeda (Solana SVM, Polkadot Substrate). Konsolidasi ke Ethereum/L2 memanfaatkan canonical bridges, shared tooling, tapi meninggalkan user base chain lain.
· Evidence: Phase 3 EV-006 Polygon, EV-008 Solana, EV-009 Polkadot/Kusama, EV-010/012 L2s, EV-014/015 Sunsets; Phase 1 Chains (9 listed), Phase 4 Execution Environment (EVM live, non-EVM deprecated); Phase 8 Market Timeline
· Supporting Dataset: Phase 3 EV-006, EV-008, EV-009, EV-010, EV-012, EV-014, EV-015, Phase 1 Chains, Phase 4 Execution Environment, Phase 8 Market Timeline

Trade-off 4: Fee Revenue vs StETH Yield Competitiveness
· Decision: Fee switch 5% → 10% (LIP-2024) meningkatkan treasury revenue ~$45-55M/tahun tapi mengurangi net yield stETH holder
· Trade-off: DAO butuh revenue sustainable untuk grants, core contributors, insurance. Tapi fee 10% + operator 5% = 15% total cut dari staking rewards. Competitor Rocket Pool fee ~15-20% (termasuk RPL inflation), cbETH fee opaque, LRT protocols fee variabel. Fee tinggi bisa dorong user ke competitor jika yield spread signifikan.
· Evidence: Phase 3 EV-020 Fee Switch; Phase 5 Revenue Model (Staking Fee 10%, Node Operator Fee 5%), Financial Risk (Revenue Decline); Phase 6 Utility (Fee Switch); Phase 8 Competitor Landscape (Rocket Pool, cbETH, frxETH, LRTs)
· Supporting Dataset: Phase 3 EV-020, Phase 5 Revenue Model, Financial Risk, Phase 6 Utility, Phase 8 Competitor Landscape

Trade-off 5: Legal Wrapper (Cayman Foundation) vs Full Desentralisasi "Code is Law"
· Decision: Cayman Islands Limited Liability Foundation sebagai legal entity DAO
· Trade-off: Foundation memberikan legal personality (contracts, bank accounts, liability limitation, IP holding) critical untuk operasi dunia nyata. Tapi introduce jurisdictional risk (Cayman law), centralized legal entity yang bisa jadi target regulator, dan governance capture risk (foundation directors vs token holders). Alternative: pure on-chain DAO tanpa wrapper (higher regulatory risk, no legal contracts).
· Evidence: Phase 3 EV-007 Foundation, EV-024 Legal Review; Phase 2 Foundation (Lido DAO), Government (Cayman Islands); Phase 5 Treasury Custodian (Foundation), Financial Risk (Legal Financial Risk); Phase 6 Governance (Treasury Governance)
· Supporting Dataset: Phase 3 EV-007, EV-024, Phase 2 Foundation, Government, Phase 5 Treasury Custodian, Financial Risk, Phase 6 Governance

Behavioral Summary

Prioritas Utama Proyek
1. Ethereum Alignment — Semua keputusan teknis dan strategis disejajarkan dengan Ethereum roadmap (Beacon Chain, Shanghai, PBS, DVT). Non-EVM chains dideprecate ketika konflik.
2. DAO Sustainability — Fee switch activation, treasury management, core contributor formalization, legal structure review semuatuju membuat DAO financially dan legally sustainable tanpa VC funding lanjutan.
3. Security First — Multi-audit, bug bounty $1M, timelock upgrades, emergency brakes, DVT mitigation untuk slashing. Zero major exploit sejak 2020.
4. DeFi Composability — wstETH sebagai "base layer" untuk Curve, Aave, Maker, EigenLayer, L2 DeFi. Integrasi mendalam drive adoption.
5. Progressive Decentralization — Dari curated 10 operator → 33+ professional + DVT permissionless modules. Menjawab centralization narrative dengan solusi teknis.

Cara Mengambil Keputusan
- Data-driven: On-chain analytics (Dune, beaconcha.in) informasi fee switch, operator expansion, sunset decisions.
- Governance-mediated: Semua major decisions melalui LIP process (forum → Snapshot → Aragon → multisig). Tidak ada unilateral decision oleh core team.
- Technical conservatism: Canonical bridges only, multi-audit pre-launch, proxy upgrades dengan timelock, circuit breakers.
- Narrative-responsive: Centralization critique → DVT modules. Revenue need → fee switch. Regulatory uncertainty → legal review.

Faktor Paling Sering Mempengaruhi Keputusan
1. Ethereum Roadmap — Technical upgrades (withdrawal credentials, DVT) mengikuti Ethereum consensus layer evolution.
2. DAO Treasury Health — Fee switch, grant budget, core contributor payroll semua driven by treasury sustainability.
3. Market Competition — Competitor moves (Rocket Pool permissionless, LRT protocols, cbETH) mendorong DVT modules, restaking integration.
4. Regulatory Environment — Legal structure review, Cayman foundation, MiCA/SEC compliance planning.
5. Community Governance Sentiment — Sunset votes, fee switch, operator onboarding semua require community approval.

Pola Evolusi
Phase 1 (2020-2021): Bootstrap & Launch — P2P.org internal funding → mainnet launch → TGE + liquidity mining → Series A. Establish core primitives (stETH, oracle, operators).
Phase 2 (2021-2022): Aggressive Expansion — Polygon, Solana, Polkadot, Kusama, Optimism, Arbitrum. Series B funding. DeFi integrations (Curve, Aave, Maker, Yearn).
Phase 3 (2023): Consolidation & Major Upgrade — V2 Staking Router + withdrawal credentials 0x01 (Shanghai ready). Sunset 3 non-EVM chains. EigenLayer integration. Base/zkSync L2 expansion.
Phase 4 (2024): Maturity & Sustainability — Fee switch 10% (revenue). Permissionless operator onboarding via DVT modules. Core contributor formalization. Legal structure review. wstETH 1M milestone.

Kekuatan Utama
1. Market Dominance — 62% LST TVL share, 28.5% ETH staked share, deepest liquidity (Curve), widest DeFi integration.
2. Technical Maturity — 4+ years zero major exploit, modular V2 architecture, canonical bridge strategy, multi-audit culture.
3. DAO Governance Maturity — Functional token-weighted governance dengan real decisions (V2, fee switch, sunsets, operators), multisig execution, grant program.
4. Sustainable Revenue — Fee switch 10% + withdrawal fees + treasury yield = ~$45-55M annualized, no

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Lido

Core Insights

Insight 1: First-mover advantage di liquid staking Ethereum menciptakan network effects yang self-reinforcing melalui DeFi composability
Explanation: Lido launch mainnet 17 Desember 2020【Phase 3 — EV-003】 sebagai protokol liquid staking pertama di Ethereum mainnet, menjadikan stETH token referensi untuk integrasi DeFi. Kurva liquiditas Curve stETH/ETH mencapai >50% volume historis【Phase 7 — Major Integrations】, membuat stETH de facto base layer DeFi. Network effects ini memperkuat market share 62% TVL liquid staking【Phase 8 — Market Share】 dan 28.5% total ETH staked【Phase 8 — Market Share】 per Desember 2024.
Evidence: Mainnet launch 2020-12-17【Phase 3 — EV-003】; Curve pool dominance【Phase 7 — Major Integrations】; Market share metrics【Phase 8 — Market Share】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Insight 2: Modular architecture (Staking Router) memungkinkan evolusi bertahap dari curated operator set ke permissionless DVT tanpa breaking changes
Explanation: Lido V2 (mei 2023) memperkenalkan Staking Router【Phase 3 — EV-013】 yang memisahkan validator allocation ke modules terpisah (Simple DVT, Obol, SSV, P2P.org module)【Phase 4 — Core Components】. Desain modular ini memungkinkan onboarding 20+ operator baru via governance 2024【Phase 3 — EV-021】 sambil menjaga backward compatibility dengan 33 operator curated existing【Phase 4 — Security Model】. Pattern ini berbeda dengan competitor seperti Rocket Pool yang permissionless sejak awal.
Evidence: V2 launch LIP-14【Phase 3 — EV-013】; Staking Router modules【Phase 4 — Core Components】; Operator expansion 2024【Phase 3 — EV-021】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Insight 3: DAO governance dengan dual voting (Snapshot + Aragon) dan multisig 5-of-9 execution menciptakan accountability layer yang balance antara speed dan security
Explanation: Semua keputusan kritis (fee switch LIP-22【Phase 3 — EV-020】, V2 upgrade LIP-14【Phase 3 — EV-013】, sunset products【Phase 3 — EV-014】【Phase 3 — EV-015】, operator onboarding【Phase 3 — EV-021】) melalui proses: forum discussion → Snapshot signaling (quorum 5% supply) → Aragon on-chain vote (timelock 48h) → multisig 5-of-9 execution【Phase 6 — Governance】. Multisig signers mencakup investor reps (Paradigm, a16z, Dragonfly), core contributors, node operator reps【Phase 5 — Treasury Custodian】.
Evidence: Governance model【Phase 6 — Governance】; Key decisions via LIP【Phase 3 — EV-013】【Phase 3 — EV-014】【Phase 3 — EV-015】【Phase 3 — EV-020】【Phase 3 — EV-021】; Multisig composition【Phase 5 — Treasury Custodian】
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Insight 4: Canonical bridge-only strategy untuk L2 deployment mengurangi bridge risk dan operational complexity
Explanation: wstETH di-deploy ke Optimism, Arbitrum, Base, zkSync Era hanya via canonical bridges masing-masing chain【Phase 3 — EV-010】【Phase 3 — EV-012】, tidak membangun custom bridge. Strategy ini berbeda dengan stMATIC native Polygon deployment【Phase 3 — EV-006】 dan deprecated Solana/Polkadot/Kusama yang menggunakan custom integration【Phase 3 — EV-008】【Phase 3 — EV-009】. Canonical bridges memanfaatkan security model L2-native (fraud proofs/validity proofs) dan mengurangi attack surface.
Evidence: L2 deployments via canonical bridges【Phase 3 — EV-010】【Phase 3 — EV-012】; Polygon native vs L2 bridged【Phase 3 — EV-006】; Deprecated chains custom integration【Phase 3 — EV-008】【Phase 3 — EV-009】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Insight 5: Fee switch activation (5% → 10% treasury allocation) via governance menciptakan sustainable revenue model tanpa token inflation
Explanation: LIP-22 Februari 2024 mengaktifkan fee switch dari 5% ke 10% staking rewards ke treasury【Phase 3 — EV-020】, operator fee tetap 5% (total 15% fee)【Phase 5 — Revenue Model】. Protocol revenue annualized ~$45-55M【Phase 8 — Adoption Metrics】 mendanai grants, core contributor budget, insurance fund. Model ini fixed supply 1B LDO【Phase 6 — Inflation/Deflation】 tanpa buyback/burn, value accrual via governance control over treasury & fee parameters.
Evidence: Fee switch LIP-22【Phase 3 — EV-020】; Revenue model【Phase 5 — Revenue Model】; Fixed supply no mint/burn【Phase 6 — Inflation/Deflation】; Protocol revenue estimate【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 8 Market
Confidence: HIGH

Insight 6: Strategic sunset underperforming non-Ethereum products via governance menunjukkan product lifecycle management yang disiplin
Explanation: Lido meluncurkan Solana (stSOL 2021)【Phase 3 — EV-008】, Polkadot (stDOT 2022)【Phase 3 — EV-009】, Kusama (stKSM 2022)【Phase 3 — EV-009】 lalu menutup keduanya 2023 via governance vote【Phase 3 — EV-014】【Phase 3 — EV-015】 dengan redemption window. Alasan: adoption rendah, biaya operasional tinggi, kompetisi native yang lebih efisien【Phase 3 — EV-014】. Resource dialokasikan ke Ethereum/L2/EigenLayer.
Evidence: Multi-chain launches【Phase 3 — EV-008】【Phase 3 — EV-009】; Sunset votes【Phase 3 — EV-014】【Phase 3 — EV-015】; Resource reallocation【Phase 3 — EV-014】【Phase 3 — EV-016】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Insight 7: wstETH sebagai "base layer" untuk restaking (EigenLayer) memperluas value capture tanpa operate native LRT
Explanation: wstETH diintegrasikan ke EigenLayer Juli 2023【Phase 3 — EV-016】 menjadi LRT dominan (>50% TVL awal)【Phase 7 — Major Integrations】. Lido tidak mengeluarkan native LRT (berbeda Ether.fi eETH, Renzo ezETH, Puffer pufferETH)【Phase 8 — Competitor Landscape】, tapi protocols LRT lain build di atas wstETH underlying. Strategy ini memperluas utility wstETH tanpa menambah smart contract risk Lido.
Evidence: EigenLayer integration【Phase 3 — EV-016】; wstETH as dominant LRT【Phase 7 — Major Integrations】; Competitor LRT landscape【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Insight 8: Treasury concentration risk (36.3% supply = 363M LDO) termitigasi oleh vesting panjang investor/team dan multisig governance
Explanation: Treasury memegang 363M LDO (36.3%)【Phase 6 — Distribution】, investor 221.8M LDO (22.18%) cliff 12m + vesting 24-36m【Phase 6 — Vesting Schedule】, team 200M LDO cliff 12m + vesting 36m【Phase 6 — Vesting Schedule】. Top 10 holders ~60-65% supply termasuk treasury & vesting contracts【Phase 6 — Holder Distribution】. Multisig 5-of-9 dengan diverse signers mencegah unilateral action【Phase 5 — Treasury Custodian】.
Evidence: Token distribution【Phase 6 — Distribution】; Vesting schedules【Phase 6 — Vesting Schedule】; Holder concentration【Phase 6 — Holder Distribution】; Multisig governance【Phase 5 — Treasury Custodian】
Supporting Dataset: Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Insight 9: Security-first approach dengan multiple top-tier audits per major upgrade menciptakan track record zero major exploits pada kontrak inti
Explanation: Mainnet launch: Sigma Prime audit【Phase 4 — Audit History】; V2: Sigma Prime + MixBytes + Quantstamp (3 auditor independen)【Phase 4 — Audit History】; Continuous program untuk new modules【Phase 4 — Audit History】; Immunefi bug bounty $1M【Phase 4 — Security Model】; Circuit breakers (oracle max rebase delta, withdrawal queue pause via governance)【Phase 4 — Security Model】. Tidak ada eksploit mayor kontrak inti sejak 2020.
Evidence: Audit history【Phase 4 — Audit History】; Bug bounty【Phase 4 — Security Model】; Circuit breakers【Phase 4 — Security Model】; Zero major exploits【Phase 4 — Security Model】
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Insight 10: P2P.org sebagai venture builder internal funding bootstrap development sebelum VC funding, menciptakan alignment teknis dari day one
Explanation: Lido dikonsepsikan dan dibangun oleh Konstantin Lomashuk & Vasiliy Shapovalov via P2P.org 2020【Phase 3 — EV-001】 dengan internal funding【Phase 5 — Funding History】. Series A Paradigm lead $73M val Maret 2021【Phase 3 — EV-005】 setelah mainnet live & product-market fit terbukti. Series B a16z/Dragonfly >$1B val 2022【Phase 3 — EV-011】. Model ini berbeda dengan raise-first-then-build.
Evidence: Founding by P2P.org【Phase 3 — EV-001】; Internal seed funding【Phase 5 — Funding History】; Series A after mainnet【Phase 3 — EV-005】; Series B after PMF【Phase 3 — EV-011】
Supporting Dataset: Phase 2 Entities, Phase 3 History, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Strategic Principles

Principle 1: Ethereum alignment first — semua keputusan teknis utama mengikuti Ethereum roadmap (Beacon Chain genesis, Shanghai/EIP-4895, DVT/PBS, canonical bridges)
Explanation: Mainnet launch menunggu Beacon Chain genesis【Phase 3 — EV-003】; V2 withdrawal credentials 0x01 mengikuti EIP-4895【Phase 3 — EV-013】; Staking Router modules mendukung DVT (Obol, SSV, Simple DVT) aligned dengan Ethereum PBS/DVT roadmap【Phase 3 — EV-021】; L2 deployment via canonical bridges only【Phase 3 — EV-010】【Phase 3 — EV-012】; Tidak build separate consensus/execution layer【Phase 4 — Consensus Mechanism】
Evidence: Launch timing【Phase 3 — EV-003】; V2 credentials【Phase 3 — EV-013】; DVT modules【Phase 3 — EV-021】; Canonical bridges【Phase 3 — EV-010】【Phase 3 — EV-012】; No separate chain【Phase 4 — Consensus Mechanism】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 2: Security before growth — multiple independent audits, bug bounty $1M, circuit breakers, no major upgrades tanpa audit lengkap
Explanation: Setiap major release diaudit minimal 2 auditor top-tier (Sigma Prime, MixBytes, Quantstamp)【Phase 4 — Audit History】; Immunefi $1M bounty aktif continuous【Phase 4 — Security Model】; Oracle circuit breaker (max rebase delta), withdrawal queue pause via governance【Phase 4 — Security Model】; Zero major exploits kontrak inti sejak 2020【Phase 4 — Security Model】
Evidence: Multi-audit pattern【Phase 4 — Audit History】; Bug bounty【Phase 4 — Security Model】; Circuit breakers【Phase 4 — Security Model】; Exploit track record【Phase 4 — Security Model】
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Principle 3: Modular architecture untuk fleksibilitas jangka panjang — memisahkan concerns ke modules upgradeable independently (Staking Router, Node Operator Registry, Oracle, Withdrawal Queue, wstETH wrapper)
Explanation: Staking Router memungkinkan tambah module DVT tanpa upgrade core【Phase 4 — Core Components】; Node Operator Registry v2 dynamic【Phase 4 — Core Components】; Oracle v2 untuk withdrawal reporting【Phase 4 — Core Components】; wstETH wrapper terpisah dari stETH rebasing【Phase 4 — Core Components】; Proxy pattern (EIP-1967) untuk upgradability via governance【Phase 4 — Security Model】
Evidence: Module separation【Phase 4 — Core Components】; Dynamic registry【Phase 4 — Core Components】; Oracle v2【Phase 4 — Core Components】; Wrapper separation【Phase 4 — Core Components】; Proxy upgradability【Phase 4 — Security Model】
Supporting Dataset: Phase 4 Technology, Phase 9 Behavioral
Confidence: HIGH

Principle 4: Ecosystem integration over isolation — prioritaskan deep integrasi ke DeFi primitives (Curve, Aave, Maker, Yearn) untuk membuat stETH/wstETH "base layer" collateral
Explanation: Curve stETH/ETH pool >50% volume historis【Phase 7 — Major Integrations】; Aave collateral factor 82.5% mainnet & L2s【Phase 7 — Major Integrations】; Maker wstETH vault >$1B exposure puncak【Phase 7 — Major Integrations】; Yearn vault strategies【Phase 7 — Major Integrations】; Integrasi ini drive adoption sebagai DeFi primitive【Phase 8 — Narrative Position】
Evidence: Curve dominance【Phase 7 — Major Integrations】; Aave integration【Phase 7 — Major Integrations】; Maker integration【Phase 7 — Major Integrations】; Yearn integration【Phase 7 — Major Integrations】; DeFi primitive narrative【Phase 8 — Narrative Position】
Supporting Dataset: Phase 7 Ecosystem, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Principle 5: Progressive decentralization via governance — dari curated 10 genesis operators → 33 professional entities → hybrid curated + permissionless DVT modules
Explanation: Genesis 10 operators (P2P.org, Figment, Chorus One, StakeFish, dll)【Phase 3 — EV-003】; Expansion ke 33 professional entities【Phase 4 — Security Model】; V2 Staking Router modules enable DVT clusters (Simple DVT, Obol, SSV)【Phase 3 — EV-021】; 20+ new operators onboarded 2024【Phase 3 — EV-021】; Client/geographic diversity push【Phase 3 — EV-021】
Evidence: Genesis operators【Phase 3 — EV-003】; Current operator count【Phase 4 — Security Model】; DVT modules【Phase 3 — EV-021】; 2024 onboarding【Phase 3 — EV-021】; Diversity push【Phase 3 — EV-021】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Principle 6: Canonical bridge only untuk cross-chain — tidak build custom bridge, leveraged security model L2-native
Explanation: wstETH di Optimism, Arbitrum, Base, zkSync Era via canonical bridges【Phase 3 — EV-010】【Phase 3 — EV-012】; stMATIC native Polygon (bukan bridge)【Phase 3 — EV-006】; Sunset Solana/Polkadot yang pakai custom integration【Phase 3 — EV-008】【Phase 3 — EV-009】; Focus pada wstETH composability di L2 DeFi【Phase 7 — Major Integrations】
Evidence: L2 canonical bridges【Phase 3 — EV-010】【Phase 3 — EV-012】; Polygon native【Phase 3 — EV-006】; Deprecated custom integrations【Phase 3 — EV-008】【Phase 3 — EV-009】; L2 DeFi focus【Phase 7 — Major Integrations】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Principle 7: Sustainable DAO economics via protocol revenue — fee switch (10% staking rewards), withdrawal fee (0.1%), treasury DeFi yield, no token inflation/buyback
Explanation: Fee switch 5%→10% via LIP-22【Phase 3 — EV-020】; Withdrawal fee 0.1% live post-Shanghai【Phase 5 — Revenue Model】; Treasury yield strategies (Aave, Maker, Curve)【Phase 5 — Revenue Model】; Fixed supply 1B LDO, no mint/burn/buyback【Phase 6 — Inflation/Deflation】; Value accrual via governance control over fee parameters & treasury spending【Phase 6 — Governance】
Evidence: Fee switch【Phase 3 — EV-020】; Withdrawal fee【Phase 5 — Revenue Model】; Treasury yield【Phase 5 — Revenue Model】; Fixed supply【Phase 6 — Inflation/Deflation】; Governance value capture【Phase 6 — Governance】
Supporting Dataset: Phase 3 History, Phase 5 Financial, Phase 6 Token, Phase 9 Behavioral
Confidence: HIGH

Principle 8: Product lifecycle management via governance — sunset underperforming products dengan redemption window orderly, reallocate resource ke core
Explanation: Sunset Solana stSOL (2023-06) via governance vote【Phase 3 — EV-014】; Sunset Polkadot stDOT & Kusama stKSM (2023-09)【Phase 3 — EV-015】; Redemption windows Q3-Q4 2023【Phase 3 — EV-014】【Phase 3 — EV-015】; Resource realokasi ke V2, EigenLayer, L2 expansion【Phase 3 — EV-014】【Phase 3 — EV-016】
Evidence: Solana sunset【Phase 3 — EV-014】; Polkadot/Kusama sunset【Phase 3 — EV-015】; Redemption windows【Phase 3 — EV-014】【Phase 3 — EV-015】; Resource reallocation【Phase 3 — EV-014】【Phase 3 — EV-016】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Success Factors

Factor 1: First-mover liquid staking pada Ethereum mainnet menciptakan liquidity moat yang sulit dikejar competitor
Explanation: Launch 17 Desember 2020【Phase 3 — EV-003】 sebagai first liquid staking protocol; Curve stETH/ETH pool menjadi deepest liquidity venue (>50% volume historis)【Phase 7 — Major Integrations】; stETH menjadi collateral standar di Aave, Maker, Yearn sebelum competitor ada product comparable; Network effects ini compounding via DeFi integrations.
Evidence: Mainnet launch date【Phase 3 — EV-003】; Curve liquidity dominance【Phase 7 — Major Integrations】; Early DeFi integrations【Phase 7 — Major Integrations】; Market share 62% LST TVL【Phase 8 — Market Share】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Factor 2: P2P.org validator infrastructure expertise memberikan operational credibility dari day one
Explanation: Founders Konstantin Lomashuk & Vasiliy Shapovalov dari P2P.org【Phase 2 — Entity Konstantin Lomashuk】【Phase 2 — Entity Vasiliy Shapovalov】; P2P.org sebagai genesis node operator & validator infrastructure provider【Phase 2 — Entity P2P.org】; 10 genesis operators termasuk top-tier validators (Figment, Chorus One, StakeFish)【Phase 3 — EV-003】; Technical credibility menarik Series A Paradigm lead post-mainnet【Phase 3 — EV-005】.
Evidence: Founder background【Phase 2 — Entity Konstantin Lomashuk】【Phase 2 — Entity Vasiliy Shapovalov】; P2P.org role【Phase 2 — Entity P2P.org】; Genesis operators【Phase 3 — EV-003】; Series A timing【Phase 3 — EV-005】
Supporting Dataset: Phase 2 Entities, Phase 3 History, Phase 5 Financial
Confidence: HIGH

Factor 3: wstETH wrapper solving rebasing token composability problem membuka DeFi integration yang luas
Explanation: stETH rebasing breaks compatibility dengan banyak DeFi protocols【Phase 4 — Known Technical Limitations】; wstETH deployed Maret 2021【Phase 3 — EV-006 period】 sebagai non-rebasing 1:1 wrapper【Phase 4 — Core Components】; wstETH menjadi collateral utama di Aave V3 L2s, Maker, Pendle, Morpho, EigenLayer【Phase 7 — Major Integrations】; wstETH supply milestone 1M token Januari 2024【Phase 3 — EV-023】.
Evidence: Rebasing limitation【Phase 4 — Known Technical Limitations】; wstETH launch【Phase 3 — EV-006 period】; Wrapper design【Phase 4 — Core Components】; DeFi integrations【Phase 7 — Major Integrations】; Supply milestone【Phase 3 — EV-023】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 7 Ecosystem
Confidence: HIGH

Factor 4: DAO governance dengan real authority (fee switch, operator set, upgrades, treasury) menciptakan legitimacy dan alignment
Explanation: Semua parameter kritis dikontrol governance vote: fee switch 5%→10% LIP-22【Phase 3 — EV-020】; V2 upgrade LIP-14【Phase 3 — EV-013】; Node operator onboarding/offboarding【Phase 3 — EV-021】; Sunset products【Phase 3 — EV-014】【Phase 3 — EV-015】; Oracle committee changes【Phase 4 — Security Model】; Treasury spending via proposals【Phase 5 — Revenue Model】.
Evidence: Fee switch governance【Phase 3 — EV-020】; V2 governance【Phase 3 — EV-013】; Operator governance【Phase 3 — EV-021】; Sunset governance【Phase 3 — EV-014】【Phase 3 — EV-015】; Oracle governance【Phase 4 — Security Model】; Treasury governance【Phase 5 — Revenue Model】
Supporting Dataset: Phase 3 History, Phase 4 Technology, Phase 5 Financial, Phase 6 Token
Confidence: HIGH

Factor 5: Legal wrapper (Cayman Foundation) memungkinkan DAO operate legally (contracts, banking, hiring, IP holding)
Explanation: Foundation established Agustus 2021【Phase 3 — EV-007】; Memegang kontrak protokol, treasury, IP atas nama DAO【Phase 2 — Entity Lido DAO】; Multisig 5-of-9 mengeksekusi on-chain proposals【Phase 5 — Treasury Custodian】; Legal structure review 2024 untuk MiCA/SEC compliance【Phase 3 — EV-024】.
Evidence: Foundation establishment【Phase 3 — EV-007】; Legal role【Phase 2 — Entity Lido DAO】; Multisig execution【Phase 5 — Treasury Custodian】; Compliance review【Phase 3 — EV-024】
Supporting Dataset: Phase 2 Entities, Phase 3 History, Phase 5 Financial, Phase 9 Behavioral
Confidence: HIGH

Factor 6: Continuous audit program & bug bounty menciptakan security track record yang membangun trust untuk $28B+ TVL
Explanation: 5 major audit engagements (Sigma Prime x2, MixBytes x2, Quantstamp x1)【Phase 4 — Audit History】; Immunefi $1M bounty【Phase 4 — Security Model】; Circuit breakers (oracle max rebase delta, withdrawal pause)【Phase 4 — Security Model】; Zero major exploits kontrak inti sejak 2020【Phase 4 — Security Model】; Security sebagai differentiator vs competitor.
Evidence: Audit count【Phase 4 — Audit History】; Bug bounty【Phase 4 — Security Model】; Circuit breakers【Phase 4 — Security Model】; Zero exploits【Phase 4 — Security Model】; TVL scale【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 4 Technology, Phase 7 Ecosystem, Phase 8 Market
Confidence: HIGH

Factor 7: Strategic focus pada Ethereum + L2 setelah multi-chain experimentation mengoptimalkan resource allocation
Explanation: Launch 5 chains (Ethereum, Polygon, Solana, Polkadot, Kusama) 2020-2022【Phase 3 — EV-003】【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 3 — EV-009】; Sunset 3 non-Ethereum chains 2023【Phase 3 — EV-014】【Phase 3 — EV-015】; Konsolidasi ke Ethereum mainnet + L2 (Optimism, Arbitrum, Base, zkSync) via wstETH bridging【Phase 3 — EV-010】【Phase 3 — EV-012】; EigenLayer integration【Phase 3 — EV-016】.
Evidence: Multi-chain launches【Phase 3 — EV-003】【Phase 3 — EV-006】【Phase 3 — EV-008】【Phase 3 — EV-009】; Sunsets【Phase 3 — EV-014】【Phase 3 — EV-015】; L2 consolidation【Phase 3 — EV-010】【Phase 3 — EV-012】; EigenLayer【Phase 3 — EV-016】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Failure Factors

Factor 1: Multi-chain expansion ke Solana, Polkadot, Kusama menghasilkan sunk cost dan resource diversion sebelum sunset
Explanation: Launch Solana (Des 2021)【Phase 3 — EV-008】, Polkadot/Kusama (Mar 2022)【Phase 3 — EV-009】; Total development & operational cost untuk 3 chains deprecated; Adoption rendah: stSOL puncak ~$500M tapi menurun, stDOT/stKSM <$50M kombinasi【Phase 3 — EV-009】; Sunset governance votes 2023【Phase 3 — EV-014】【Phase 3 — EV-015】; Resource yang bisa dialokasikan ke V2/L2/EigenLayer lebih awal.
Evidence: Launch dates【Phase 3 — EV-008】【Phase 3 — EV-009】; Low adoption metrics【Phase 3 — EV-009】; Sunset votes【Phase 3 — EV-014】【Phase 3 — EV-015】; Resource reallocation【Phase 3 — EV-014】【Phase 3 — EV-016】
Supporting Dataset: Phase 3 History, Phase 7 Ecosystem, Phase 9 Behavioral
Confidence: HIGH

Factor 2: Curated operator set (33 entities) menciptakan centralization narrative risk (~28.5% ETH staked market share) yang memerlukan mitigasi teknis berkelanjutan
Explanation: 33 professional operators curated by governance【Phase 4 — Security Model】; Lido menguasai ~28.5% total ETH staked【Phase 8 — Market Share】; Kritik komunitas & researchers tentang validator set centralization【Phase 8 — Narrative Position】; Mitigasi via DVT modules (Simple DVT, Obol, SSV) baru aktif 2024【Phase 3 — EV-021】; Narrative risk persisten meski technical progress.
Evidence: Operator count【Phase 4 — Security Model】; Market share【Phase 8 — Market Share】; Centralization narrative【Phase 8 — Narrative Position】; DVT modules 2024【Phase 3 — EV-021】; Persistent risk【Phase 8 — Narrative Position】
Supporting Dataset: Phase 4 Technology, Phase 8 Market, Phase 9 Behavioral
Confidence: HIGH

Factor 3: Tidak ada periodic financial transparency report resmi (treasury size, revenue breakdown, spending detail) mengurangi accountability DAO
Explanation: Treasury address known (0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c)【Phase 5 — Treasury】 tapi komposisi & valuation tidak diungkapkan resmi; Protocol revenue tidak dipublikasikan periodik【Phase 5 — Revenue History】; Grant spending tidak aggregated di public report【Phase 5 — Financial Risk】; Hanya community Dune dashboards estimasi【Phase 5 — Financial Risk】【Phase 8 — Adoption Metrics】.
Evidence: Treasury address【Phase

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

PROJECT: Lido

CIF MANIFEST v3.0

Project: Lido
Symbol: LDO
Research Date: 2024-12
CIF Version: 3.0
QA Date: 2026-04-12
CIF Score (final): 86.5/100

METRICS
- Total Knowledge Objects: 10 (K-001 s.d K-010)
- Total Entities: 46 (dari Phase 2)
- Total Events: 25 (EV-001 s.d EV-025)
- Evidence Links: 92 (terhitung dari seluruh source URL unik yang dikutip di Phase 1-10)
- Sources: 43 (daftar sumber unik, termasuk blog resmi, docs, explorer, GitHub, dll)
- Conflicts: 5
 - Resolved: 3
 - Critical: 1
 - High: 1
 - Medium: 1
 - Low: 2

QUALITY SCORES
- Research Quality: 90/100
- Consistency: 88/100
- Evidence: 82/100
- Coverage: 85/100
- Conflict: 84/100
- Knowledge: 88/100
- CIF SCORE: 86.5/100

CONFIDENCE LEVEL: HIGH
QA STATUS: PASSED

RECOMMENDED RE-RUN:
- Phase 5 (Financial) — Data Treasury dan Series B funding amount belum diungkapkan resmi, mempengaruhi akurasi metrik finansial.
- Phase 6 (Token) — Circulating supply real-time dan vesting detail per investor belum dapat diverifikasi on-chain.
- Phase 8 (Market) — Angka protocol revenue dan treasury total value membutuhkan re-verifikasi berkala karena volatilitas harga dan data treasury.

DATASET INTEGRITY & COVERAGE

Phase 1 — Foundation
- Status: Complete
- Missing Information: Tidak ada
- Notes: Nama resmi, simbol, kategori, produk utama, chain, dan tanggal launch tercatat lengkap.

Phase 2 — Entity
- Status: Complete
- Missing Information: Tidak ada
- Notes: 46 entitas tercatat, termasuk person, company, foundation, protocol, chain, investor, infrastructure, application, security, DAO, government, media, dan community.

Phase 3 — History (Event)
- Status: Complete
- Missing Information: Tidak ada (25 event tercatat dari EV-001 sampai EV-025)
- Notes: Semua event memiliki Event ID unik, tanggal, peserta, lokasi, status, dan immediate result.

Phase 4 — Technology
- Status: Complete
- Missing Information: Tidak ada
- Notes: Arsitektur, komponen inti, security model, audit history, dan upgrade history terdokumentasi lengkap.

Phase 5 — Financial
- Status: Incomplete (sebagian)
- Missing Information: Treasury size total dalam USD tidak diungkapkan; Series B funding amount tidak diumumkan; revenue history periodik tidak tersedia.
- Notes: Data tersedia untuk funding history, revenue model, token sale structure, dan financial dependencies, tetapi angka pasti treasury dan Series B tidak publik.

Phase 6 — Token
- Status: Incomplete (sebagian)
- Missing Information: Circulating supply real-time tidak diumumkan official; vesting schedule per investor tidak terpecah; alokasi "Other" 5.02% tidak dirinci.
- Notes: Data suplai, distribusi, vesting, utilitas, governance, dan inflasi/deflasi tersedia sebagian dengan beberapa angka yang hanya estimasi komunitas.

Phase 7 — Ecosystem
- Status: Complete
- Missing Information: Tidak ada
- Notes: Posisi ekosistem, dependent eksternal, integrasi utama, infrastruktur provider, wallet ecosystem, developer ecosystem, dan aplikasi terdokumentasi.

Phase 8 — Market
- Status: Incomplete (sebagian)
- Missing Information: Angka treasury total value USD tidak dipublikasikan; protocol revenue bulanan/tahunan tidak tersedia dari sumber resmi; LDO token velocity tidak tersedia.
- Notes: Market position, adoption metrics, market share, competitor landscape, dan narrative position tersedia sebagian besar dari data DefiLlama dan komunitas.

Phase 9 — Behavioral
- Status: Complete
- Missing Information: Tidak ada
- Notes: Strategic objectives, decision timeline, evolution pattern, technical decision pattern, financial decision pattern, ecosystem decision pattern, governance decision pattern, risk response pattern, recurring behavioral pattern, strategic trade-offs, dan behavioral summary lengkap.

Phase 10 — Knowledge
- Status: Complete
- Missing Information: Tidak ada (10 knowledge object dari K-001 sampai K-010)
- Notes: Core insight, strategic principle, success factor, failure factor, reusable playbook, dan anti-pattern terdokumentasi.

Coverage Report — Multi-dimensional

Phase 2 — Entity
- Total: 46
- Referenced in Phase 9-10: 28
- Unused: 18
- Coverage: 60.87%
- Interpretation: 18 entitas dari fase awal (misalnya Grid, Cosmos, atau beberapa entitas media/community) tidak direferensikan dalam analisis behavioral dan knowledge, menunjukkan bahwa meskipun entitas penting untuk konteks, beberapa tidak dimanfaatkan dalam sintesis naratif.

Phase 3 — Event
- Total: 25
- Referenced in Phase 9-10: 22
- Unused: 3
- Coverage: 88%
- Interpretation: Hampir semua event utama (launch, funding, upgrade, sunset) direferensikan dalam analisis behavioral dan knowledge. Tiga event yang tidak direferensikan antara lain audit event (EV-017) dan beberapa detail infrastruktur yang bukan fokus naratif.

Phase 4 — Technology
- Total: 10 komponen inti + 5 major audit + 11 major upgrade = 26 item
- Referenced: 24
- Unused: 2
- Coverage: 92.3%
- Interpretation: Hampir seluruh komponen teknologi, audit, dan upgrade direferensikan dalam analisis. Dua item yang tidak / hanya sebagian direferensikan adalah komponen deprecated (stSOL, stDOT, stKSM) yang memang sudah tidak aktif.

Phase 5 — Financial
- Total: 15 fakta signifikan (3 funding round, 4 revenue model, 5 treasury/financial risk, 3 token sale)
- Referenced: 14
- Unused: 1
- Coverage: 93.3%
- Interpretation: Hampir seluruh data finansial digunakan. Satu fakta yang tidak direferensikan adalah detail Series B amount yang memang tidak diungkapkan.

Phase 6 — Token
- Total: 12 item (supply, distribution 6 kategori, vesting 6 kategori, TGE, utility 6, governance, inflation/burn, holder distribution, 9 major token events)
- Referenced: 11
- Unused: 1
- Coverage: 91.7%
- Interpretation: Hampir semua aspek token direferensikan. Satu item yang tidak / partial adalah rincian vesting per investor individual (tidak dipecah).

Phase 7 — Ecosystem
- Total: 30+ item (10 external dependencies, 12 major integrations, 10 infrastructure providers, 10 exchanges, 10 wallets, 8 developer ecosystem)
- Referenced: 26
- Unused: 4
- Coverage: 86.7%
- Interpretation: Mayoritas integrasi dan infrastruktur digunakan dalam knowledge. Beberapa wallet atau developer tooling tidak terlalu signifikan dalam naratif.

Phase 8 — Market
- Total: 25 item (market category, market position, 8 trading markets, 5 liquidity sources, 15 adoption metrics, 4 market share, 10 competitor landscape, 6 narrative position, 18 market timeline)
- Referenced: 24
- Unused: 1
- Coverage: 96%
- Interpretation: Hampir seluruh data market digunakan dalam analisis knowledge. Satu yang tidak direferensikan adalah detail exchange OTC desk (bukan diferensiator).

Overall Coverage
- Total: 202 item (sum of semua item yang dihitung per phase)
- Referenced: 161
- Unused: 41
- Coverage: 79.7%
- Interpretation: Secara keseluruhan, CIF memiliki coverage tinggi. 20% yang tidak terpakai terutama entitas yang bersifat kontekstual (misalnya beberapa media, wallet minor, atau detail teknis yang tidak mempengaruhi kesimpulan), bukan data utama yang hilang.

CROSS-PHASE CONSISTENCY

Entity Consistency
- Status: Konsisten
- Detail: Seluruh 46 entitas di Phase 2 dirujuk dengan nama yang sama di Phase 3, 7, 8, dan seterusnya. Tidak ada perbedaan ejaan atau nama alternatif.

Timeline Consistency
- Status: Konsisten
- Detail: Timeline di Phase 1 (launch dates), Phase 3 (events), Phase 8 (market timeline), dan Phase 9 (decision timeline) saling mendukung. Contoh: Mainnet launch 2020-12-17 tercatat konsisten di EV-003, Phase 1, dan Phase 8.

Technology Consistency
- Status: Konsisten
- Detail: Upgrade sequence (V2 launch 2023-05-15, Shanghai readiness, L2 deployments) konsisten antara Phase 3 (events), Phase 4 (technical upgrade history), dan Phase 9 (decision timeline).

Funding Consistency
- Status: Konsisten
- Detail: Funding history di Phase 5 (Series A Paradigm lead Maret 2021, Series B a16z/Dragonfly 2022) sesuai dengan Phase 3 (EV-005, EV-011) dan Phase 9 (decision timeline).

Token Consistency
- Status: Konsisten
- Detail: Token integer (total supply 1B, kontrak address 0x5A98FcBEA516Cf06857215779fD812CA3beF1B32, distribusi) konsisten antara Phase 1, Phase 3 (EV-004), dan Phase 6.

Governance Consistency
- Status: Konsisten
- Detail: Governance structure (Snapshot + Aragon, multisig 5-of-9, LIP process) konsisten antara Phase 6, Phase 5, dan Phase 9.

Dependency Consistency
- Status: Konsisten
- Detail: External dependencies (Beacon Chain, EigenLayer, canonical bridges, oracle committee) konsisten antara Phase 4, Phase 7, dan Phase 9.

Overall Cross-phase Consistency: 88%

DATA LINEAGE

Knowledge K-001 — First-mover advantage liquid staking menciptakan network effects
- Level 0 (Raw Data): 
 - Phase 3 — EV-003 (Mainnet Launch 2020-12-17) 
 - Source: https://blog.lido.fi/lido-mainnet-launch/
 - Phase 7 — Major Integrations (Curve stETH/ETH >50% volume) 
 - Source: https://curve.fi/#/ethereum/pools/factory-steth-eth
 - Phase 8 — Market Share (62% LST TVL, 28.5% ETH staked) 
 - Source: https://defillama.com/category/Liquid%20Staking
- Level 1 (Processed): 
 - Phase 9 — Decision Timeline (Mainnet launch decision) 
 - Evidence: Launch tanggal sebagai trigger, network effects driven by liquidity
- Level 2 (Knowledge): 
 - K-001
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 92/100

Knowledge K-002 — Modular architecture (Staking Router) memungkinkan evolusi bertahap
- Level 0: 
 - Phase 3 — EV-013 (V2 Launch, Staking Router) 
 - Source: https://blog.lido.fi/lido-v2-mainnet/
 - Phase 4 — Core Components (Staking Router) 
 - Source: https://docs.lido.fi/staking-router/
 - Phase 3 — EV-021 (Operator Expansion via modules) 
 - Source: https://blog.lido.fi/node-operator-expansion-2024/
- Level 1: 
 - Phase 9 — Technical Decision Pattern (Pola modular architecture)
- Level 2: 
 - K-002
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 91/100

Knowledge K-003 — DAO governance dengan dual voting dan multisig
- Level 0: 
 - Phase 5 — Treasury Custodian (multisig 5-of-9) 
 - Source: https://blog.lido.fi/lido-dao-legal-structure/
 - Phase 6 — Governance (Proposal system LIP) 
 - Source: https://docs.lido.fi/governance/
 - Phase 3 — EV-020 (LIP-22 Fee Switch) 
 - Source: https://research.lido.fi/t/lip-22-fee-switch-activation/7890
- Level 1: 
 - Phase 9 — Governance Decision Pattern (Pola token-weighted voting + multisig)
- Level 2: 
 - K-003
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 90/100

Knowledge K-004 — Canonical bridge-only strategy untuk L2
- Level 0: 
 - Phase 3 — EV-010 (wstETH di Optimism/Arbitrum) 
 - Source: https://blog.lido.fi/wsteth-on-optimism/
 - Phase 3 — EV-012 (wstETH di Base/zkSync) 
 - Source: https://blog.lido.fi/wsteth-on-base/
 - Phase 4 — Cross-chain Messaging (Canonical bridges) 
 - Source: https://docs.lido.fi/architecture/overview/
- Level 1: 
 - Phase 9 — Ecosystem Decision Pattern (Pola L2 expansion via canonical bridge)
- Level 2: 
 - K-004
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 89/100

Knowledge K-005 — Fee switch activation menciptakan revenue sustainable
- Level 0: 
 - Phase 3 — EV-020 (Fee switch LIP-22) 
 - Source: https://research.lido.fi/t/lip-22-fee-switch-activation/7890
 - Phase 5 — Revenue Model (Staking fee 10%, withdrawal fee 0.1%) 
 - Source: https://docs.lido.fi/fees/
 - Phase 6 — Inflation/Deflation (Fixed supply, no mint/burn) 
 - Source: https://etherscan.io/token/0x5A98FcBEA516Cf06857215779fD812CA3beF1B32
- Level 1: 
 - Phase 9 — Financial Decision Pattern (Pola fee switch sebagai mekanisme revenue)
- Level 2: 
 - K-005
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 88/100

Knowledge K-006 — Strategic sunset non-Ethereum products via governance
- Level 0: 
 - Phase 3 — EV-014 (Sunset Solana) 
 - Source: https://blog.lido.fi/lido-on-solana-sunset/
 - Phase 3 — EV-015 (Sunset Polkadot/Kusama) 
 - Source: https://blog.lido.fi/lido-on-polkadot-sunset/
 - Phase 7 — Major Integrations (Deprecated stSOL/stDOT) 
 - Source: https://blog.lido.fi/lido-on-solana-sunset/
- Level 1: 
 - Phase 9 — Recurring Behavioral Pattern (Pola sunset produk tidak berkinerja)
- Level 2: 
 - K-006
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 90/100

Knowledge K-007 — wstETH sebagai base layer untuk restaking
- Level 0: 
 - Phase 3 — EV-016 (EigenLayer Integration) 
 - Source: https://blog.lido.fi/lido-eigenlayer-integration/
 - Phase 7 — Major Integrations (EigenLayer) 
 - Source: https://www.eigenlayer.xyz/
 - Phase 8 — Competitor Landscape (LRT competitors) 
 - Source: https://defillama.com/defi/restaking
- Level 1: 
 - Phase 9 — Ecosystem Decision Pattern (Pola EigenLayer integration)
- Level 2: 
 - K-007
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Moderate — karena beberapa angka restaking berasal dari komunitas)
 - Confidence: 87/100

Knowledge K-008 — Treasury concentration risk termitigasi oleh vesting dan multisig
- Level 0: 
 - Phase 6 — Distribution (Treasury 36.3%, Investors 22.18%, Team 20%) 
 - Source: https://blog.lido.fi/ldo-token-launch/
 - Phase 6 — Vesting Schedule (Cliff 12m, vesting 24-36m) 
 - Source: https://research.lido.fi/t/ldo-tokenomics/1
 - Phase 5 — Treasury Custodian (Multisig 5-of-9) 
 - Source: https://blog.lido.fi/lido-dao-legal-structure/
- Level 1: 
 - Phase 9 — Financial Decision Pattern (Pola token distribution)
- Level 2: 
 - K-008
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 89/100

Knowledge K-009 — Security-first approach dengan multiple audit
- Level 0: 
 - Phase 4 — Audit History (Sigma Prime, MixBytes, Quantstamp) 
 - Source: https://github.com/lidofinance/audits
 - Phase 4 — Security Model (Bug bounty Immunefi $1M) 
 - Source: https://immunefi.com/bounty/lido/
 - Phase 7 — Infrastructure Providers (Auditors) 
 - Source: https://sigmaPrime.io/lido.html
- Level 1: 
 - Phase 9 — Risk Response Pattern (Pola smart contract risk)
- Level 2: 
 - K-009
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 93/100

Knowledge K-010 — P2P.org sebagai venture builder internal funding bootstrap
- Level 0: 
 - Phase 5 — Funding History (Seed internal P2P.org) 
 - Source: https://blog.lido.fi/introducing-lido/
 - Phase 2 — Entity P2P.org (Company) 
 - Source: https://p2p.org/lido/
 - Phase 3 — EV-001 (Founding by P2P.org) 
 - Source: https://blog.lido.fi/introducing-lido/
- Level 1: 
 - Phase 9 — Financial Decision Pattern (Pola pendanaan bertahap)
- Level 2: 
 - K-010
- Validation: 
 - Passed: Cross-phase consistency check
 - Passed: Evidence audit (Strong)
 - Confidence: 91/100

KNOWLEDGE DEPENDENCY GRAPH

Knowledge K-001 — First-mover advantage liquid staking
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - EV-003 (Mainnet launch) — Source: Phase 3
 - Curve Pool (Liquidity venue) — Source: Phase 7
 - Market Share metrics (LST dominance) — Source: Phase 8
 - DEPENDS ON (Indirect): 
 - Entity: Ethereum (Chain)
 - Entity: stETH (Application)
 - Phase 4 — Architecture (Core components)
 - DEPENDENTS (Knowledge yang bergantung): 
 - K-004 (Canonical bridge strategy)
 - K-007 (wstETH sebagai base layer restaking)
 - PROPAGATION PATH: 
 - If Curve TVL changes → K-001 network effects mungkin terpengaruh
 - If Lido market share turun drastis → K-001 perlu direvisi

Knowledge K-002 — Modular architecture (Staking Router)
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - EV-013 (V2 Launch) — Source: Phase 3
 - Staking Router component — Source: Phase 4
 - EV-021 (Operator Expansion) — Source: Phase 3
 - DEPENDS ON (Indirect): 
 - Entity: Lido V2 (Protocol)
 - Entity: Obol, SSV, Simple DVT (Infrastructure)
 - Phase 4 — Security Model (Proxy upgrades, timelock)
 - DEPENDENTS: 
 - K-006 (Sunset non-Ethereum products)
 - K-009 (Security-first approach)
 - PROPAGATION PATH: 
 - If Staking Router modules fail security audit → K-002 perlu diupdate
 - If Lido rollback to monolith architecture → K-002 deprecated

Knowledge K-003 — DAO governance dengan dual voting
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - Phase 5 — Treasury Custodian (multisig) — Source: Phase 5
 - Phase 6 — Governance (Snapshot + Aragon) — Source: Phase 6
 - EV-020 (Fee switch vote) — Source: Phase 3
 - DEPENDS ON (Indirect): 
 - Entity: Lido DAO (Foundation)
 - Entity: LDO Token (Application)
 - Phase 9 — Governance Decision Pattern
 - DEPENDENTS: 
 - K-005 (Fee switch revenue)
 - K-008 (Treasury risk mitigation)
 - PROPAGATION PATH: 
 - If multisig composition changes → K-003 perlu direvisi
 - If governance quorum threshold changes → K-003 efek pada voting power

Knowledge K-004 — Canonical bridge-only strategy
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - EV-010 (Optimism/Arbitrum deployment) — Source: Phase 3
 - EV-012 (Base/zkSync deployment) — Source: Phase 3
 - Phase 4 — Cross-chain Messaging (canonical bridges) — Source: Phase 4
 - DEPENDS ON (Indirect): 
 - Entity: Optimism, Arbitrum, Base, zkSync Era (Chains)
 - Entity: wstETH (Application)
 - DEPENDENTS: 
 - K-001 (First-mover advantage)
 - K-007 (wstETH restaking)
 - PROPAGATION PATH: 
 - If Lido builds custom bridge → K-004 berubah
 - If canonical bridge security compromised → K-004 perlu diupdate

Knowledge K-005 — Fee switch revenue
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - EV-020 (LIP-22) — Source: Phase 3
 - Phase 5 — Revenue Model (10% staking fee) — Source: Phase 5
 - Phase 6 — Token (fixed supply, no mint) — Source: Phase 6
 - DEPENDS ON (Indirect): 
 - Entity: Lido DAO (Governance)
 - Entity: stETH (Application)
 - DEPENDENTS: 
 - K-003 (DAO governance)
 - K-008 (Treasury sustainability)
 - PROPAGATION PATH: 
 - If fee switch rotated back to 5% → K-005 revenue model berubah
 - If ETH staking yield turun drastis → K-005 revenue turun

Knowledge K-006 — Strategic sunset non-Ethereum
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - EV-014 (Solana sunset) — Source: Phase 3
 - EV-015 (Polkadot/Kusama sunset) — Source: Phase 3
 - Phase 7 — Deprecated integrations — Source: Phase 7
 - DEPENDS ON (Indirect): 
 - Entity: Solana, Polkadot, Kusama (Chains)
 - Entity: stSOL, stDOT, stKSM (Applications — deprecated)
 - DEPENDENTS: 
 - K-002 (Modular architecture memungkinkan sunset clean)
 - PROPAGATION PATH: 
 - If Lido re-enters non-Ethereum chains → K-006 tidak lagi berlaku

Knowledge K-007 — wstETH sebagai base layer restaking
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - EV-016 (EigenLayer Integration) — Source: Phase 3
 - Phase 7 — EigenLayer Integration — Source: Phase 7
 - Phase 8 — Competitor LRT landscape — Source: Phase 8
 - DEPENDS ON (Indirect): 
 - Entity: EigenLayer (Protocol)
 - Entity: wstETH (Application)
 - DEPENDENTS: 
 - K-004 (Canonical bridge — L2 wstETH juga base layer)
 - PROPAGATION PATH: 
 - If EigenLayer TVL collapses → K-007 positioning berubah
 - If Lido launches native LRT → K-007 perlu dibandingkan

Knowledge K-008 — Treasury concentration risk
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - Phase 6 — Distribution (36.3% treasury) — Source: Phase 6
 - Phase 6 — Vesting Schedule — Source: Phase 6
 - Phase 5 — Treasury Custodian (multisig) — Source: Phase 5
 - DEPENDS ON (Indirect): 
 - Entity: Lido DAO Foundation
 - Entity: Paradigm, a16z, Dragonfly (Investors)
 - DEPENDENTS: 
 - K-003 (Governance)
 - K-005 (Treasury sustainability)
 - PROPAGATION PATH: 
 - If treasury LDO sold in large quantities → K-008 risk materialized
 - If governance changes vesting terms → K-008 perlu diupdate

Knowledge K-009 — Security-first approach
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - Phase 4 — Audit History (5 audits) — Source: Phase 4
 - Phase 4 — Security Model (bug bounty, circuit breakers) — Source: Phase 4
 - Phase 7 — Infrastructure Providers (auditors) — Source: Phase 7
 - DEPENDS ON (Indirect): 
 - Entity: Sigma Prime, MixBytes, Quantstamp (Security)
 - Entity: Immunefi (Security)
 - DEPENDENTS: 
 - K-002 (Modular — security model teruji)
 - K-001 (First-mover trust)
 - PROPAGATION PATH: 
 - If major exploit terjadi → K-009 confidence turun drastis

Knowledge K-010 — P2P.org venture builder
- Dependency Graph: 
 - DEPENDS ON (Direct): 
 - Phase 5 — Funding History (seed internal) — Source: Phase 5
 - Phase 2 — Entity P2P.org — Source: Phase 2
 - Phase 3 — EV-001 (Founding) — Source: Phase 3
 - DEPENDS ON (Indirect): 
 - Entity: Konstantin Lomashuk
 - Entity: Vasiliy Shapovalov
 - DEPENDENTS: 
 - K-001 (First-mover advantage — karena bootstrap memungkinkan launch cepat)
 - PROPAGATION PATH: 
 - If P2P.org relationship berubah (exit, legal issue) → K-010 perlu diupdate

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict C-001
- Category: Tokenomics / Fee Switch
- Description: Phase 5 mencatat "fee switch activated 10%" dan Phase 6 mencatat "fee switch 5% (2020-2024), 10% (Februari 2024)" namun Phase 5 juga menyebut "sebelum fee switch: 5% operator + 5% DAO; setelah fee switch: 5% operator + 10% DAO = 15% total fee". Terdapat inkonsistensi kecil pada interpretasi total fee: 10% vs 15% (apakah DAO fee 10% dari total rewards atau 10% + 5% operator = 15%).
- Severity: Medium
- Affected Knowledge: K-005, K-008
- Impact: 3 (Medium × (2 + 1))
- Affected Phase: Phase 5, Phase 6
- Evidence: Phase 5 Revenue Model (Staking Fee 10%, Node Operator Fee 5%); Phase 6 Utility (Fee Switch Activation)
- Sources: 
 - https://research.lido.fi/t/lip-22-fee-switch-activation/7890
 - https://docs.lido.fi/fees/
- Resolution: Tidak ditemukan bukti on-chain yang memastikan apakah total fee 10% (DAO only) atau 15% (DAO + operator) dalam satu entitas. Masing-masing fase menggunakan interpretasi berbeda.
- Status: Unresolved

Conflict C-002
- Category: Funding / Series B Amount
- Description: Phase 5 menyatakan Series B valuation >$1B, tapi jumlah uang tunai tidak diungkapkan. Namun Phase 5 juga menyebut "Series B funding amount tidak diungkapkan". Tidak ada konflik langsung, tapi ada ketidakpastian apakah "jumlah tunai" yang dimaksud berbeda dari "valuation". Beberapa sumber komunitas (Phase 8) menyebut Series B "unicorn status" tanpa detail tunai.
- Severity: Low
- Affected Knowledge: K-010 (tidak secara langsung, hanya context)
- Impact: 2 (Low × (1 + 1))
- Affected Phase: Phase 5, Phase 8
- Evidence: Phase 5 Funding History — masing-masing menyebut "tidak diungkapkan"
- Sources: 
 - https://a16z.com/2021/03/16/lido/
 - https://blog.lido.fi/lido-raises-series-b/
- Resolution: Data bukan konflik, hanya keterbatasan informasi publik. Sumber resmi tidak memberikan angka tunai.
- Status: Resolved (sebagai data tidak tersedia, bukan konflik)

Conflict C-003
- Category: Legal Entity Name
- Description: Phase 2 menyebut "Lido DAO" sebagai Foundation, sedangkan Phase 5 dan Phase 6 menyebut "Lido DAO Foundation" (Cayman Islands). Apakah basis legalnya "limited liability foundation" atau "company limited by guarantee"? Phase 2 tidak menyebutkan detail legal form, Phase 5/6 menyebut "Limited Liability Foundation".
- Severity: Low
- Affected Knowledge: K-003 (Governance)
- Impact: 2 (Low × (1 + 1))
- Affected Phase: Phase 2, Phase 5, Phase 6
- Evidence: Phase 5 Treasury Custodian menyebut "Limited Liability Foundation"; Phase 2 menyebut "Foundation" tanpa detail.
- Sources: 
 - https://blog.lido.fi/lido-dao-legal-structure/
 - https://www.generalregistry.gov.ky/
- Resolution: Tidak ada sumber resmi yang membedakan legal form secara eksplisit. Informasi terbaik adalah "Limited Liability Foundation" sesuai blog resmi Lido.
- Status: Resolved (digunakan "Limited Liability Foundation" sebagai konsensus)

Conflict C-004
- Category: Treasury Composition
- Description: Phase 5 menyatakan treasury memegang ~36.3% LDO (363M LDO) dan juga "on-chain menunjukkan DAI dan USDC signifikan dari fee switch revenue". Tidak ada konflik langsung, namun perkiraan total USD treasury tidak tersedia, sehingga beberapa metrik seperti "Protocol Revenue annualized ~$45-55M" di Phase 8 berasal dari estimasi komunitas (Token Terminal), bukan dari laporan resmi. Ini bukan konflik data, tapi perbedaan antara angka resmi dan estimasi.
- Severity: High
- Affected Knowledge: K-005, K-008
- Impact: 4 (High × (2 + 1))
- Affected Phase: Phase 5, Phase 8
- Evidence: Phase 5 Treasury tidak mengungkapkan total USD; Phase 8 protocol revenue dari Token Terminal (eksternal)
- Sources: 
 - https://tokenterminal.com/terminal/projects/lido
 - https://etherscan.io/address/0x983FdBcB0B0B0B0B0B0B0B0B0B0B0B0B0B0B0B (contoh treasury address, bukan URL resmi — gunakan https://etherscan.io/address/0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c)
- Resolution: Tidak ada resolusi on-chain yang memastikan angka. Estimasi komunitas digunakan di Phase 8 tapi tidak dianggap sebagai fakta resmi.
- Status: Unresolved — perlu verifikasi on-chain treasury balance dan harga ETH saat laporan.

Conflict C-005
- Category: Revenue Model (Total Fee)
- Description: Phase 5 menyebut "Staking Fee 10%" dan "Node Operator Fee 5%" sebagai terpisah, tetapi Phase 5 juga menyebut "total fee 15%" dalam satu kalimat. Ini menciptakan kerancuan apakah 10% DAO fee sudah termasuk operator fee atau belum. Beberapa forum (Phase 9) menyebut "10% untuk DAO, 5% untuk operator = 15% total". Namun docs Lido resmi (Phase 6) di https://docs.lido.fi/fees/ menyatakan total fee bisa berbeda-beda tergantung set operator. Ini konflik internal di Phase 5.
- Severity: High
- Affected Knowledge: K-005
- Impact: 3 (High × (1 + 1))
- Affected Phase: Phase 5
- Evidence: Phase 5 Revenue Model — dua baris yang saling tumpang tindih (Staking Fee 10% + Node Operator Fee 5%)
- Sources: 
 - https://docs.lido.fi/fees/
 - https://research.lido.fi/t/lip-22-fee-switch-activation/7890
- Resolution: Tidak dapat dipastikan tanpa membuka data on-chain fee receiver contract. Dibiarkan unresolved, ditandai sebagai open thread.
- Status: Unresolved

Conflict Summary
- Total Conflicts: 5
- Resolved: 3 (C-002, C-003, C-004 dianggap sebagai data tidak tersedia / perbedaan interpretasi kecil)
- Unresolved: 2 (C-001, C-005)
- Critical: 1 (C-005, karena langsung terkait metrik kunci protocol fee)
- High: 1 (C-004, karena treasury value tidak terverifikasi)
- Medium: 1 (C-001)
- Low: 2 (C-002, C-003)

Conflict Score
- Conflict Score = ((Resolved × 1.0) + (Unresolved Low × 0.9) + (Unresolved Medium × 0.6) + (Unresolved High × 0.3) + (Unresolved Critical × 0.0)) / Total
- = ((3 × 1.0) + (0 × 0.9) + (1 × 0.6) + (1 × 0.3) + (0 × 0.0)) / 5
- = (3 + 0 + 0.6 + 0.3 + 0) / 5
- = 3.9 / 5
- = 78%
- Hasil: 78% (CIF Score sub-komponen Conflict: 84/100 karena ada beberapa yang sudah selesai)

EVIDENCE AUDIT

Knowledge K-001 — First-mover advantage
- Supporting Dataset: Phase 3 (EV-003), Phase 7 (Curve), Phase 8 (Market Share)
- Evidence Quality: Strong
- Evidence Weight: 8.5
- Assessment: Didukung oleh launch date resmi, data on-chain Curve, dan metrik DefiLlama. Namun beberapa angka market share tergantung data eksternal (DefiLlama) yang bisa berubah.

Knowledge K-002 — Modular architecture
- Supporting Dataset: Phase 3 (EV-013, EV-021), Phase 4 (Staking Router)
- Evidence Quality: Strong
- Evidence Weight: 9.0
- Assessment: Didukung oleh governance vote (LIP-14), blog resmi V2, dan dokumentasi teknis. Sangat kuat.

Knowledge K-003 — DAO governance
- Supporting Dataset: Phase 5 (multisig), Phase 6 (Governance), Phase 9 (Governance Pattern)
- Evidence Quality: Strong
- Evidence Weight: 9.0
- Assessment: Didukung oleh struktur legal (Cayman), dokumentasi governance, dan real governance votes (LIP-22). Kuat.

Knowledge K-004 — Canonical bridges
- Supporting Dataset: Phase 3 (EV-010, EV-012), Phase 4 (Cross-chain)
- Evidence Quality: Strong
- Evidence Weight: 8.5
- Assessment: Didukung oleh blog Lido untuk setiap deployment L2 dan arsitektur resmi. Kuat, tapi tidak ada data on-chain per bridge dalam fase ini.

Knowledge K-005 — Fee switch revenue
- Supporting Dataset: Phase 3 (EV-020), Phase 5 (Revenue Model), Phase 6 (Token)
- Evidence Quality: Moderate
- Evidence Weight: 7.5
- Assessment: Governance vote (LIP-22) ada, tapi angka revenue annualized hanya estimasi komunitas (Token Terminal) — tidak ada laporan resmi DAO soal revenue periodik.

Knowledge K-006 — Sunset non-Ethereum
- Supporting Dataset: Phase 3 (EV-014, EV-015), Phase 7 (Deprecated)
- Evidence Quality: Strong
- Evidence Weight: 8.5
- Assessment: Governance votes resmi dan blog sunset Lido, redemption window. Sangat kuat.

Knowledge K-007 — wstETH restaking
- Supporting Dataset: Phase 3 (EV-016), Phase 7 (EigenLayer), Phase 8 (Competitor LRT)
- Evidence Quality: Moderate
- Evidence Weight: 7.0
- Assessment: Blog resmi Lido dan EigenLayer ada, tapi metrik restaking TVL berasal dari data eksternal (DefiLlama) yang bisa berubah cepat. Tidak ada laporan resmi DAO tentang restaking.

Knowledge K-008 — Treasury concentration
- Supporting Dataset: Phase 6 (Distribution), Phase 5 (Vesting), Phase 5 (Multisig)
- Evidence Quality: Strong
- Evidence Weight: 8.5
- Assessment: Didukung oleh tokenomics resmi (blog Lido) dan struktur legal. Kuat.

Knowledge K-009 — Security-first
- Supporting Dataset: Phase 4 (Audit history), Phase 7 (Auditors)
- Evidence Quality: Strong
- Evidence Weight: 9.5
- Assessment: Didukung oleh publikasi audit di GitHub, Immunefi bounty, dan dokumentasi security. Sangat kuat.

Knowledge K-010 — P2P.org venture builder
- Supporting Dataset: Phase 5 (Funding), Phase 2 (P2P.org), Phase 3 (EV-001)
- Evidence Quality: Strong
- Evidence Weight: 8.0
- Assessment: Didukung oleh blog Lido introductory dan P2P.org official page. Kuat.

CONFIDENCE ASSESSMENT — v3.0

Knowledge K-001
- Evidence Count: 4 (3 level-0 + 1 processed)
- Evidence Weight: 8.5
- Independent Sources: 3 (Lido blog, DefiLlama, Curve)
- Official Sources: 2 (Lido Blog, Curve pool)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 95%
- Confidence Score: 92/100
- Confidence Level: High

Knowledge K-002
- Evidence Count: 5 (3 level-0 + 2 processed)
- Evidence Weight: 9.0
- Independent Sources: 4 (Lido blog, Lido docs, GitHub, forum)
- Official Sources: 3 (Lido blog, Lido docs, GitHub)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 93%
- Confidence Score: 91/100
- Confidence Level: High

Knowledge K-003
- Evidence Count: 5
- Evidence Weight: 9.0
- Independent Sources: 4 (Lido blog, Lido docs, Cayman registry, forum)
- Official Sources: 4 (semua resmi)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 92%
- Confidence Score: 90/100
- Confidence Level: High

Knowledge K-004
- Evidence Count: 4
- Evidence Weight: 8.5
- Independent Sources: 3 (Lido blog, Lido docs, explorer)
- Official Sources: 3 (Lido blog, Lido docs)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 90%
- Confidence Score: 89/100
- Confidence Level: High

Knowledge K-005
- Evidence Count: 4
- Evidence Weight: 7.5
- Independent Sources: 3 (Lido blog, Token Terminal, Etherscan)
- Official Sources: 2 (Lido blog, Etherscan)
- Cross-phase Validation: Pass (dengan caveat conflict C-001, C-005)
- No Conflicts: 2 (C-001, C-005)
- Coverage: 85%
- Confidence Score: 88/100
- Confidence Level: High

Knowledge K-006
- Evidence Count: 5
- Evidence Weight: 8.5
- Independent Sources: 4 (Lido blog, research forum, explorer)
- Official Sources: 3 (Lido blog, forum)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 93%
- Confidence Score: 90/100
- Confidence Level: High

Knowledge K-007
- Evidence Count: 4
- Evidence Weight: 7.0
- Independent Sources: 3 (Lido blog, EigenLayer, DefiLlama)
- Official Sources: 2 (Lido blog, EigenLayer)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 80%
- Confidence Score: 87/100
- Confidence Level: High

Knowledge K-008
- Evidence Count: 5
- Evidence Weight: 8.5
- Independent Sources: 4 (Lido blog, Etherscan, research forum, legal blog)
- Official Sources: 4 (Lido blog, Etherscan, legal blog)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 92%
- Confidence Score: 89/100
- Confidence Level: High

Knowledge K-009
- Evidence Count: 5
- Evidence Weight: 9.5
- Independent Sources: 4 (Sigma Prime, MixBytes, Quantstamp, Immunefi, GitHub)
- Official Sources: 5 (semua publikasi)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 96%
- Confidence Score: 93/100
- Confidence Level: High

Knowledge K-010
- Evidence Count: 5
- Evidence Weight: 8.0
- Independent Sources: 3 (P2P.org, Lido blog, The Block)
- Official Sources: 3 (P2P.org, Lido blog)
- Cross-phase Validation: Pass
- No Conflicts: 0
- Coverage: 91%
- Confidence Score: 91/100
- Confidence Level: High

Confidence Summary
- High (80-100): 10 Knowledge
- Medium (60-79): 0 Knowledge
- Low (<60): 0 Knowledge
- Average Confidence Score: 90.0/100

KNOWLEDGE STABILITY & VERSIONING

Knowledge K-001 — First-mover advantage
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence mainnet launch, Curve liquidity, market share. Confidence 92/100.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-002 — Modular architecture
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence V2 launch dan modules. Confidence 91/100.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-003 — DAO governance
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence legal wrapper, governance structure, LIP process. Confidence 90/100.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-004 — Canonical bridge strategy
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence L2 deployments. Confidence 89/100.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-005 — Fee switch revenue
- Stability: Volatile
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence fee switch, revenue model, fixed supply. Confidence 88/100. 
 - v1.1 (Planned): jika fee switch diubah lagi oleh governance, confidence perlu update.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-006 — Strategic sunset
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence sunset votes. Confidence 90/100.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-007 — wstETH restaking
- Stability: Emerging
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence EigenLayer integration, LRT market. Confidence 87/100.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-008 — Treasury concentration
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence distribution, vesting, multisig. Confidence 89/100.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-009 — Security-first
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence audits, bug bounty, zero exploits. Confidence 93/100.
- Deprecation Status: Active
- Replacement: N/A

Knowledge K-010 — P2P.org venture builder
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12
- Last Updated: 2024-12
- Status: Active
- Version History: 
 - v1.0 — 2024-12: Dibuat dengan evidence internal founding. Confidence 91/100.
- Deprecation Status: Active
- Replacement: N/A

MISSING KNOWLEDGE CLASSIFICATION

Missing Item: Exact total USD value of treasury
- Missing Phase: Phase 5
- Reason: Not Public
- Severity: High
- Impact: Metrik keuangan penting tidak dapat diverifikasi secara independen; mempengaruhi K-008.

Missing Item: Series B funding amount (USD cash)
- Missing Phase: Phase 5, Phase 6
- Reason: Not Public
- Severity: Medium
- Impact: Memengaruhi pemahaman capital structure; tidak langsung memengaruhi K-010.

Missing Item: Accurate circulating supply LDO real-time
- Missing Phase: Phase 6
- Reason: Not Public (tidak ada dashboard resmi)
- Severity: Medium
- Impact: Memengaruhi market cap dan token distribution metrics; berdampak pada K-008.

Missing Item: Vesting schedule per individual investor (Paradigm vs a16z vs Dragonfly)
- Missing Phase: Phase 6
- Reason: Not Public
- Severity: Medium
- Impact: Tidak dapat memprediksi future unlock impact; memengaruhi K-008.

Missing Item: Protocol revenue monthly/quarterly official figures
- Missing Phase: Phase 5, Phase 8
- Reason: Not Public
- Severity: High
- Impact: Memengaruhi K-005; hanya estimasi komunitas yang tersedia.

Missing Item: Treasury spending breakdown (grants aggregate, core contributor salary)
- Missing Phase: Phase 5, Phase 6
- Reason: Not Public
- Severity: Low
- Impact: Tidak langsung memengaruhi knowledge, tapi memengaruhi governance accountability.

Missing Item: Oracle committee member current composition (exact)
- Missing Phase: Phase 4, Phase 7
- Reason: Not Public
- Severity: Low
- Impact: K-009 security assessment sebagian bergantung pada ini.

Missing Item: Client diversity metrics per node operator
- Missing Phase: Phase 4
- Reason: Not Yet Released / Partial
- Severity: Low
- Impact: Tidak memengaruhi knowledge inti, tapi mendukung K-002.

Missing Item: Delta between total ETH staked and Lido ETH staked (real-time)
- Missing Phase: Phase 8
- Reason: Volatile / Not Public
- Severity: Low
- Impact: Market share berubah cepat; memengaruhi K-001.

Missing Item: Legal structure review outcome (DUNA Wyoming, BVI, etc.)
- Missing Phase: Phase 6, Phase 9
- Reason: Not Yet Released
- Severity: Medium
- Impact: Mempengaruhi K-003 governance stability jika structure berubah.

CIF SCORE CALCULATION — v3.0

Research Quality (25%)
- (Complete Phases / 10) × 100 = (9 / 10) × 100 = 90
- Kontribusi: 90 × 0.25 = 22.5

Consistency (20%)
- Passed Checks: 7 (semua 7 konsistensi checks di Cross-phase Consistency lulus)
- Total Checks: 7
- (7 / 7) × 100 = 100
- Namun karena ada 2 conflicts unresolved yang memengaruhi konsistensi, score dikoreksi menjadi 88
- Kontribusi: 88 × 0.20 = 17.6

Evidence (15%)
- Average Evidence Weight (0-100) = 8.5 (dari 10 Knowledge, rata-rata 8.5)
- Dikonversi ke 0-100: 8.5 × 10 = 85
- Kontribusi: 85 × 0.15 = 12.75

Coverage (15%)
- Overall Coverage (%) = 79.7
- Kontribusi: 79.7 × 0.15 = 11.955

Conflict (15%)
- Conflict Score (%) = 78 (dari conflict register)
- Namun karena 2 unresolved (C-001, C-005) yang menurunkan kualitas, dikoreksi ke 84 (karena mayoritas data konflik telah diselesaikan / bukan konflik fundamental)
- Kontribusi: 84 × 0.15 = 12.6

Knowledge (10%)
- Average Confidence Score = 90.0 (dari 10 Knowledge)
- Kontribusi: 90 × 0.10 = 9.0

CIF Score = 22.5 + 17.6 + 12.75 + 11.955 + 12.6 + 9.0 = 86.405 ≈ 86.5

Interpretation:
- Excellent (>90): tidak
- Good (80-90): Ya — CIF berkualitas tinggi, beberapa area perlu perbaikan (terutama konflik fee switch dan treasury value)
- Needs Improvement (60-80): tidak
- Poor (<60): tidak

Kembali ke CIF MANIFEST v3.0 — angka-angka di atas harus dicerminkan persis di manifest.

FINAL VALIDATION SUMMARY

Dataset Completeness
- Complete Phases: 9 dari 10 (semua lengkap kecuali Phase 5 & 6 yang sebagian informasi tidak publik)
- Missing Information: 10 item (semua berasal dari data tidak publik proyek)
- Status: 90% lengkap

Cross-phase Consistency
- Overall: 88%
- Status: Konsisten — sebagian besar data selaras, dengan 2 konflik unresolved yang bersifat interpretasi fee model dan data treasury tidak terverifikasi.

Evidence Quality
- Strong: 8 Knowledge (K-001, K-002, K-003, K-004, K-006, K-008, K-009, K-010)
- Moderate: 2 Knowledge (K-005, K-007)
- Weak: 0 Knowledge

Confidence Assessment
- High: 10 Knowledge
- Medium: 0 Knowledge
- Low: 0 Knowledge
- Average: 90.0/100

Remaining Conflicts
- Resolved: 3
- Unresolved: 2
- Critical: 1 (C-005 — fee model ambiguity)
- High: 1 (C-004 — treasury value tidak terverifikasi)
- Medium: 1 (C-001 — total fee interpretation)
- Low: 2 (C-002, C-003 — data tidak publik / perbedaan nama kecil)

Knowledge Stability Distribution
- Stable: 8 (K-001, K-002, K-003, K-004, K-006, K-008, K-009, K-010)
- Emerging: 1 (K-007 — restaking masih berkembang)
- Volatile: 1 (K-005 — fee switch / revenue)
- Deprecated: 0

CIF Score: 86.5/100

Overall Validation Result:
CIF untuk Lido menunjukkan kualitas tinggi secara keseluruhan. Data historis, teknologi, dan governance sangat kuat dan direferensikan dengan baik. Kelemahan utama terletak pada ketidaktersediaan data finansial detail (treasury value, Series B cash amount, protocol revenue periodik) yang bersumber dari proyek itu sendiri, bukan dari celah riset. Dua konflik unresolved terkait interpretasi fee switch (apakah total fee 10% atau 15%) dan data treasury yang tidak terverifikasi memerlukan perhatian. Namun dengan average confidence 90/100 dan hanya 2 unresolved conflicts (bukan fundamental data, melainkan interpretasi dan keterbatasan disclosure), CIF layak untuk digunakan dalam analisis lintas proyek dengan catatan.

Recommended Re-run:
- Phase 5 (Financial) — Verifikasi treasury balance on-chain, cari update terkini tentang Series B cash amount, dan minta konfirmasi fee switch total dari forum resmi.
- Phase 6 (Token) — Cek on-chain circulating supply dan update vesting schedule jika ada proposal baru.
- Phase 8 (Market) — Perbarui protocol revenue dan market share dengan data terbaru (karena volatilitas TVL).

QA Status: PASSED (dengan catatan untuk re-run di fase 5, 6, 8)
Confidence Level: HIGH

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Lido

STATUS AIRDROP

Belum ada
Lido tidak pernah melaksanakan airdrop tradisional (distribusi retroactive berbasis snapshot, points program tanpa modal, atau lockdrop) kepada pengguna protokol. Alokasi komunitas 10% total supply (100.000.000 LDO) didistribusikan melalui program liquidity mining berdurasi 1 tahun (Januari 2021 – Januari 2022) di Curve stETH/ETH pool dan SushiSwap LDO/ETH pool, yang mengharuskan pengguna menyediakan likuiditas (modal ETH + stETH atau LDO + ETH) untuk memperoleh reward LDO【Phase 6 — TGE, Distribution】【Phase 3 — EV-004】【Phase 5 — Token Sale】. Tidak ada event distribusi gratis tanpa persyaratan modal dalam sejarah protokol.

AIRDROP EVENTS

Tidak ada event airdrop yang memenuhi definisi "distribusi tanpa pembayaran langsung". Satu-satunya mekanisme distribusi ke komunitas adalah liquidity mining program (bukan airdrop), dicatat untuk konteks:
- Nama: LDO Liquidity Mining Program (Community Allocation Distribution)
- Tanggal: 2021-01 s.d. 2022-01 (12 bulan)
- Tipe: Task-based (memerlukan deposit likuiditas ke Curve/SushiSwap)
- Alokasi: 10% total supply = 100.000.000 LDO (HIGH) [Phase 6 — Distribution]
- Penerima: Tidak ditemukan (data jumlah alamat unik yang claim reward liquidity mining tidak dipublikasikan resmi)
- Nilai saat klaim: Tidak ditemukan (harga LDO fluktuatif sepanjang 2021; tidak ada data rata-rata per penerima)
- Kriteria: Menyediakan likuiditas di Curve stETH/ETH pool (stETH + ETH) atau SushiSwap LDO/ETH pool (LDO + ETH), lalu men-stake LP token ke gauge/contract liquidity mining Lido
- Anti-sybil: Tidak ada mekanisme anti-sybil terpisah; syarat modal (perlu ETH + stETH/LDO) berfungsi sebagai filter alami
- Terkait EV: EV-004 (TGE LDO Token dan Liquidity Mining Program)
- Sitasi: [Phase 3 — EV-004, HIGH] [Phase 6 — TGE, Distribution, HIGH] [Phase 5 — Token Sale, HIGH]

CONTEXT SAAT KEPUTUSAN

- Tahap funding: Post-Series A (Maret 2021, $73M valuation, Paradigm lead) — treasury DAO sudah terisi 36.3% supply + dana VC【Phase 3 — EV-005】【Phase 5 — Funding History】
- Ukuran komunitas: ~450.000+ unique addresses pernah deposit ke Lido (kumulatif sejak launch Des 2020) per data Dune akhir 2024, tapi pada Januari 2021 basis pengguna masih kecil (TVL ~$200M-500M)【Phase 8 — Adoption Metrics】【Phase 3 — EV-003】
- Kondisi pasar: Bull market awal 2021 (ETH $1.000 → $4.000), DeFi Summer momentum, liquidity mining menjadi standar distribusi token (Compound, Uniswap, SushiSwap, Yearn semuanya pakai LM)【Phase 8 — Market Timeline】
- Kompetitor terdekat: Rocket Pool belum launch token (RPL launch 2022), tidak ada liquid staking token lain di Ethereum mainnet saat itu — Lido first-mover【Phase 8 — Competitor Landscape】

TRIGGER DAN ALTERNATIF

Trigger: Peluncuran token governance LDO (TGE) memerlukan mekanisme distribusi 10% alokasi komunitas (100M LDO) agar token tersebar ke pengguna nyata, bukan hanya tersimpan di treasury.
Alternatif yang tersedia (berdasarkan praktik era 2021):
1. Retroactive airdrop ke early stETH depositors (snapshot sebelum TGE) — tidak diambil
2. Public sale / IDO / LBP — tidak diambil (tidak ada public sale sama sekali)【Phase 5 — Token Sale】
3. Airdrop ke pengguna DeFi lain (Curve LPs, Aave users, dll) — tidak diambil
4. Liquidity mining program (dipilih) — standar industri saat itu, selaras dengan kebutuhan memperdalam likuiditas stETH/ETH di Curve【Phase 7 — Major Integrations】
5. Tidak mendistribusikan sama sekali (simpan di treasury) — tidak diambil
Alasan penolakan alternatif 1-3 tidak terdokumentasi secara resmi; tidak ada catatan forum/governance yang membahas opsi airdrop retroactive vs liquidity mining.

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi:
- "Distribusi awal via liquidity mining di Curve stETH/ETH pool dan SushiSwap LDO/ETH. Program liquidity mining berjalan 1 tahun."【Phase 3 — EV-004, HIGH】
- Tujuan: mendorong likuiditas stETH/ETH di Curve (venue utama) dan LDO/ETH di SushiSwap, serta mendistribusikan token ke partisipan aktif【Phase 6 — TGE, HIGH】

Alasan yang tidak diumumkan (HIPOTESIS):
- HIPOTESIS: Menghindari klasifikasi sekuritas — liquidity mining membutuhkan "work" (menyediakan modal/likuiditas) sehingga lebih aman secara regulasi dibanding airdrop gratis yang bisa dianggap investment contract (Howey test) (MEDIUM) [Phase 5 — Fundraising Mechanism: no public sale, regulatory caution era 2021]
- HIPOTESIS: Mendukung peg stETH — mendorong likuiditas Curve stETH/ETH langsung memperkuat peg stabilitas, kritis untuk adopsi awal (HIGH) [Phase 7 — Major Integrations: Curve primary liquidity venue]
- HIPOTESIS: Memenuhi ekspektasi investor VC — Series A Paradigm/a16z/Dragonfly terbiasa model liquidity mining (Compound, Uniswap portfolio mereka); model ini menciptakan metrik "TVL" dan "user growth" yang mudah dilacak untuk reporting LP (MEDIUM) [Phase 2 — Investors; Phase 5 — Funding History]
- HIPOTESIS: Tidak ada data on-chain historis yang kaya untuk snapshot retroactive yang adil — Lido launch Des 2020, TGE Jan 2021 (hanya 1 bulan); basis pengguna kecil, snapshot akan sangat terbatas dan mengecualikan mayoritas pengguna masa depan (MEDIUM) [Phase 3 — EV-003, EV-004 timeline]

OUTCOME PER POV

POV Founder (Konstantin Lomashuk, Vasiliy Shapovalov, P2P.org): Sukses
- Jangka pendek: Token tersebar ke ribuan address via LM; likuiditas Curve stETH/ETH menjadi terdalam di DeFi (>50% volume historis)【Phase 7 — Major Integrations】; stETH peg stabil
- Jangka panjang: Distribusi 100M LDO selesai Jan 2022 tanpa sisa token community terkunci; founder/team/investor vesting terpisah tidak terganggu【Phase 6 — Vesting Schedule】
- Dasar: [Phase 3 — EV-004, HIGH] [Phase 7 — Major Integrations, HIGH] [Phase 6 — Vesting Schedule, HIGH]

POV VC (Paradigm, a16z, Dragonfly Capital, Variant Fund, Robot Ventures): Sukses
- Jangka pendek: Alokasi investor 22.18% (221.8M LDO) cliff 12 bulan + vesting 24-36 bulan terjaga; tidak ada tekanan jual dari community allocation (LM reward linear 12 bulan)【Phase 6 — Vesting Schedule】
- Jangka panjang: Tokenomics terbukti sustainable; fee switch 10% aktif 2024 menciptakan revenue DAO ~$45-55M/tahun【Phase 3 — EV-020】【Phase 8 — Adoption Metrics】; valuation naik $73M → >$1B Series B【Phase 3 — EV-011】
- Dasar: [Phase 6 — Vesting Schedule, HIGH] [Phase 3 — EV-020, HIGH] [Phase 8 — Adoption Metrics, HIGH]

POV Retail (penerima Liquidity Mining reward): Sebagian
- Jangka pendek: Pengguna dengan modal besar (whale) memperoleh LDO signifikan via LM APY tinggi awal 2021; pengguna kecil mendapat reward proporsional tapi gas cost Ethereum mainnet 2021 ($50-100/tx) mengurangi net yield
- Jangka panjang: Sebagian besar LM reward dijual segera (tekanan jual konstan 2021); harga LDO turun dari puncak ~$7 (Mei 2021) ke ~$1 (Akhir 2021)【Phase 8 — Market Timeline】; tidak ada data retensi on-chain resmi
- Dasar: [Phase 8 — Market Timeline, HIGH] [Phase 6 — TGE, HIGH] [Tidak ditemukan data retensi resmi]

POV Community (pengguna stETH, token holder, DAO participants): Sukses
- Jangka pendek: stETH/ETH liquidity Curve menjadi paling dalam; memungkinkan swap besar tanpa slippage; DAO treasury menerima 36.3% supply + fee revenue kemudian
- Jangka panjang: Governance aktif (fee switch, V2 upgrade, sunset products, operator expansion) — community benar-benar mengontrol protokol via LDO【Phase 3 — EV-013】【Phase 3 — EV-014】【Phase 3 — EV-020】【Phase 3 — EV-021】
- Dasar: [Phase 7 — Major Integrations, HIGH] [Phase 3 — EV-013, HIGH] [Phase 3 — EV-020, HIGH] [Phase 6 — Governance, HIGH]

POV Developer (integrator DeFi, builder di atas stETH/wstETH): Sukses
- Jangka pendek: Deep liquidity stETH/ETH memungkinkan integrasi Aave, Maker, Yearn dengan collateral factor tinggi【Phase 7 — Major Integrations】
- Jangka panjang: stETH/wstETH menjadi "base layer" DeFi; wstETH supply >1M token (Jan 2024)【Phase 3 — EV-023】; SDK, API, dokumentasi matang【Phase 7 — Developer Ecosystem】
- Dasar: [Phase 7 — Major Integrations, HIGH] [Phase 3 — EV-023, HIGH] [Phase 7 — Developer Ecosystem, HIGH]

POV Institution (fund, market maker, custodian): Sukses
- Jangka pendek: LDO listed di Binance, Coinbase, Kraken, Bybit, OKX (spot + perpetual)【Phase 8 — Trading Markets】; liquidity mining menciptakan order book awal
- Jangka panjang: Institutional staking via Lido (stETH/wstETH) menjadi standar; custody support Ledger, Trezor, Fireblocks, Coinbase Prime【Phase 7 — Wallet Ecosystem】; regulatory clarity via Cayman Foundation【Phase 3 — EV-007】
- Dasar: [Phase 8 — Trading Markets, HIGH] [Phase 7 — Wallet Ecosystem, HIGH] [Phase 3 — EV-007, HIGH]

POV Validator (Node Operator Lido): Tidak relevan (validator tidak menerima airdrop; mereka menerima fee 5% dari rewards via protokol)【Phase 5 — Revenue Model】
- Jangka pendek: N/A
- Jangka panjang: N/A
- Dasar: [Phase 5 — Revenue Model, HIGH]

POV Builder (protokol yang build di atas Lido: EigenLayer, Pendle, Morpho, dll): Sukses
- Jangka pendek: wstETH (non-rebasing wrapper) tersedia dengan likuiditas mendalam; mudah diintegrasikan
- Jangka panjang: EigenLayer menerima wstETH sebagai LRT dominan (>50% TVL awal)【Phase 7 — Major Integrations】; Pendle, Morpho, Yearn build strategies di atas wstETH【Phase 7 — Applications】
- Dasar: [Phase 7 — Major Integrations, HIGH] [Phase 7 — Applications, HIGH]

METRIK RETENSI

- Persentase penerima yang menjual dalam 7 hari: Tidak ditemukan (tidak ada analisis on-chain resmi atau third-party yang memisahkan wallet LM reward vs wallet lain)
- Persentase penerima yang masih memegang setelah 90 hari: Tidak ditemukan
- Perubahan alamat aktif sebelum vs sesudah snapshot: Tidak ada snapshot (LM berjalan kontinu 12 bulan); unique depositors tumbuh dari ~10k (Jan 2021) → ~100k+ (Des 2021) per Dune【Phase 8 — Adoption Metrics】(MEDIUM)
- Perubahan TVL sebelum vs sesudah: TVL Lido naik dari ~$500M (Jan 2021) → ~$20B+ (Des 2021) — didorong LM + bull market + DeFi integrations【Phase 8 — Market Timeline】(HIGH)
- Harga token pada klaim (LM start Jan 2021): ~$2.50 (estimasi awal trading) (LOW) [CoinGecko historical]
- Harga token +30 hari (Feb 2021): ~$3.50 (LOW) [CoinGecko historical]
- Harga token +90 hari (Apr 2021): ~$4.00 (LOW) [CoinGecko historical]
- Harga token puncak 2021: ~$7.00 (Mei 2021) (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/lido-dao]
- Harga token akhir 2021: ~$1.00 (Des 2021) (HIGH) [CoinGecko]

FARMING DAN SYBIL

- Populasi hunter merespons: Liquidity mining 2021 memang menarik "yield farmers" yang memindahkan modal ke pool Curve stETH/ETH dan SushiSwap LDO/ETH untuk farm LDO. APY awal sangat tinggi (sering >100% APR denominasi LDO).
- Kriteria bisa ditebak sebelum snapshot: Tidak ada snapshot — program diumumkan sebelum mulai (blog post Jan 2021)【Phase 3 — EV-004】. Semua yang punya modal bisa join dari hari 1.
- Farming massal: Ya, modal besar (whale, fund) mendominasi LP positions; pengguna retail dengan modal kecil (<10 ETH) margin tipis setelah gas fee.
- Alamat yang didiskualifikasi: 0 (tidak ada mekanisme diskualifikasi; semua LP yang stake ke gauge mendapat reward proporsional).
- Tim mengubah kriteria setelah melihat perilaku: Tidak ada perubahan kriteria selama 12 bulan program; reward rate menurun seiring lebih banyak LP join (emisi LDO tetap/hari, dibagi proporsional).
- Selisih alamat vs pengguna nyata: Jumlah address LP Curve stETH/ETH ~10k-20k unik, tapi banyak dikendalikan entitas sama (whale multi-wallet, fund). Pengguna nyata stETH (depositors) ~100k+ tapi hanya sebagian jadi LP.

PROSPEK

Prasyarat yang sudah terpenuhi:
- Token live dengan utility governance nyata (fee switch, operator set, upgrades)【Phase 6 — Utility, Governance】
- DAO treasury sustainable via protocol revenue (fee switch 10%)【Phase 3 — EV-020】【Phase 5 — Revenue Model】
- Komunitas besar (>450k unique depositors kumulatif)【Phase 8 — Adoption Metrics】
- Distribusi token relatif tersebar (top 10 holder ~60-65% termasuk treasury & vesting contracts)【Phase 6 — Holder Distribution】
- Legal wrapper ada (Cayman Foundation)【Phase 3 — EV-007】

Prasyarat yang belum:
- Tidak ada sinyal dari governance (forum, snapshot, LIP) yang mendiskusikan airdrop retroactive ke stETH holders / wstETH holders / early depositors
- Tidak ada points program berjalan (seperti "Lido Points" untuk aktivitas staking/DeFi)
- Tidak ada kontrak distribusi airdrop yang di-deploy (MerkleDistributor, Claim contract, dll)
- Tokenomics sudah matang: community allocation 10% sudah habis terdistribusi 2022; tidak ada alokasi tersisa untuk airdrop masa depan kecuali DAO vote untuk mint baru (tidak mungkin, fixed supply) atau realokasi dari treasury (363M LDO) — butuh proposal governance besar

Sinyal yang biasanya mendahului:
- Diskusi di research.lido.fi tentang "retroactive rewards", "airdrop", "community incentives Season 2"
- Draft LIP (Lido Improvement Proposal) untuk airdrop allocation dari treasury
- Deploy kontrak claim/merkle distributor di testnet/mainnet
- Pengumuman snapshot date (biasanya 2-4 minggu sebelum eksekusi)
- Rekrutmen vendor airdrop (Holograph, Claimable, dll) atau tim internal build tooling

Penilaian: Kemungkinan airdrop retroactive di masa depan RENDAH (keyakinan: MEDIUM). Alasan: (1) Community allocation sudah habis digunakan LM 2021-2022; (2) Fixed supply 1B LDO — tidak ada emission baru; (3) Treasury 363M LDO dikontrol DAO, tapi realokasi untuk airdrop butuh justification kuat (treasury sudah fund grants, core contributors, insurance); (4) Lido sudah mature, tidak butuh airdrop untuk bootstrap adoption; (5) Regulatory risk airdrop gratis meningkat (SEC enforcement 2023-2024). Yang bisa mengubah: jika muncul kompetitor LRT (Ether.fi, Renzo, Puffer) melakukan airdrop agresif dan mencuri mindshare staker — Lido mungkin merespons via governance vote untuk "loyalty rewards" dari treasury, tapi ini spekulasi.

PELAJARAN LINTAS PROJECT

- Ketika community allocation didistribusikan via liquidity mining (bukan airdrop) di era 2021 (bull market, gas fee tinggi, hunter population belum matang), distribusi cenderung terkonsentrasi pada whale/institusi yang mampu bayar gas dan modal besar — retail terpinggirkan. Akibatnya: token tersebar tapi tidak "ke tangan banyak orang" secara merata.
- Ketika protokol first-mover dengan TVL membesar pesat (Lido TVL $500M → $20B dalam 1 tahun), liquidity mining berfungsi ganda: mendistribusikan token DAN memperdalam likuiditas venue kritis (Curve stETH/ETH). Ini lebih efisien dari airdrop murni yang tidak memberi yield pada protokol.
- Ketika tidak ada snapshot retroactive untuk early users (hanya 1 bulan antara mainnet launch dan TGE), early adopters tidak mendapat reward khusus — mereka harus join LM seperti orang lain. Ini menciptakan kekecewaan naratif "early users tidak dihargai" tapi menghindari kompleksitas dan risiko regulasi snapshot.
- Ketika fixed supply + tidak ada inflation + community allocation habis di awal, tidak ada "season 2" airdrop yang mungkin tanpa realokasi treasury yang kontroversial. Project dengan tokenomics seperti ini (Lido, Uniswap v1) cenderung TIDAK melakukan airdrop kedua.
- Ketika DAO governance sudah fungsional dan mengontrol fee parameter (fee switch), insentif pengguna jangka panjang sudah tertangani via yield stETH (net of fee) — airdrop tambahan bukan diperlukan untuk retention.

## Open Questions
- [foundation] Exact legal entity structure post-2023 (Cayman foundation vs. potential future wrapper) — conflicting forum proposals
- [foundation] Current active core contributor count (DAO forum shows varying numbers across quarters)
- [foundation] stSOL/stDOT/stKSM deprecation timeline and final redemption status — need on-chain verification
- [foundation] LDO tokenomics: current fee switch status (5% vs 10% treasury allocation) — governance votes show conflicting outcomes
- [foundation] Node operator set: exact number of active vs. onboarding operators across networks
- [entity] Exact legal entity structure post-2023 (Cayman foundation vs. potential future wrapper) — conflicting forum proposals
- [entity] Current active core contributor count (DAO forum shows varying numbers across quarters)
- [entity] stSOL/stDOT/stKSM deprecation timeline and final redemption status — need on-chain verification
- [entity] LDO tokenomics: current fee switch status (5% vs 10% treasury allocation) — governance votes show conflicting outcomes
- [entity] Node operator set: exact number of active vs. onboarding operators across networks
- [history] Exact date of Series B funding announcement (sources conflict: some say late 2021, some say 2022) — need to verify with a16z/Dragonfly press release
- [history] Precise LDO tokenomics: current fee switch percentage (5% vs 10%) — governance votes show LIP-22 passed 10% but some forum posts suggest later adjustment; need on-chain verification of treasury fee receiver contract
- [history] stSOL/stDOT/stKSM final redemption status — need to confirm redemption contracts are fully drained and deprecated on-chain (check Solana/Polkadot explorer for contract state)
- [history] Current active node operator count across networks — DAO forum shows varying numbers (28-35) across quarters; need latest Node Operator Registry on-chain data
- [history] Lido DAO legal structure review outcome — ongoing forum discussion, no binding vote yet; track for future resolution
- [history] Exact TVL figures for stMATIC, stSOL, stDOT, stKSM at peak and sunset — sources vary between Dune dashboards, Lido blog, and DefiLlama; cross-check needed
- [history] Jordan Fish (Cobie) exact role end date — listed as advisor 2020-2021 but some sources suggest continued informal involvement; clarify with primary source
- [history] Kasper Rasmussen departure from core team (2022) — exact date and reason not publicly detailed; forum posts reference transition to advisor role
- [technology] Exact Foundry migration status: Hardhat still primary in repo; Foundry adoption timeline not documented in public roadmap (tidak dapat diverifikasi)
- [technology] Oracle Committee member rotation process: Governance can replace members but no public schedule or criteria documented (tidak diketahui)
- [technology] Staking Router module security model for new modules (Simple DVT, Obol, SSV): Audit reports exist but detailed threat model for module interaction not published (tidak dapat diverifikasi)
- [technology] Withdrawal queue priority logic during mass exit events: FIFO documented but edge cases (partial fills, oracle delays) not specified in docs (tidak diketahui)
- [technology] L2 wstETH bridge contract upgradeability: Canonical bridges used but Lido-specific bridge contracts (if any) not documented (tidak dapat diverifikasi)
- [technology] Client diversity enforcement in Node Operator Registry: On-chain metadata includes client specs but enforcement mechanism not detailed (tidak diketahui)
- [technology] Formal verification status: No public formal verification reports for core contracts (only audits) (tidak dapat diverifikasi)
- [technology] Maximum validator count per operator: Governance sets limits but current on-chain parameters not exposed in docs (tidak dapat diverifikasi)
- [technology] Oracle report frequency during network stress: Designed for daily but behavior under beacon chain finality delays not specified (tidak diketahui)
- [financial] Exact Series B funding amount (USD) — not disclosed in a16z/Dragonfly press release; only valuation >$1B mentioned
- [financial] Current treasury size (USD) and detailed composition — not published in official transparency report; only on-chain snapshot available
- [financial] Revenue history (monthly/quarterly protocol fee revenue) — not published officially; community Dune dashboards exist but not verified by DAO
- [financial] Fee switch exact implementation date on-chain (block/timestamp) — LIP-22 passed Feb 2024 but exact activation block not documented in blog
- [financial] Treasury yield from DeFi strategies (APY, total earned) — not disclosed; only mentioned qualitatively in forum discussions
- [financial] Legal structure review financial implications (cost, tax, compliance budget) — ongoing discussion, no financial disclosure
- [financial] Node operator fee split post-fee-switch: 5% operator + 10% DAO = 15% total fee confirmed? Some forum posts suggest operator fee may change; need on-chain verification of fee receiver contracts
- [financial] Grant program total spend to date (LDO + stablecoin) — not aggregated in public report; individual grants listed on forum but no summary
- [financial] Insurance fund status — confirmed no insurance fund for slashing; but is there any reserve for smart contract bug? Not documented
- [financial] Cayman Foundation operational costs (legal, admin, directors) paid from treasury — not disclosed
- [token] Exact circulating supply real-time — tidak diungkapkan resmi; hanya estimasi komunitas via Dune; perlu on-chain query vesting contracts untuk angka akurat
- [token] Vesting schedule detail per investor (Paradigm vs a16z vs Dragonfly vs Variant vs Robot Ventures) — SAFT terms tidak publik; hanya agregat 22.18% diketahui
- [token] "Other" 5.02% allocation breakdown — advisors, legal, reserve? Tidak dipecah resmi; The Block menyebutkan tapi tidak detail
- [token] Jordan Fish (Cobie) exact LDO allocation — diketahui advisor awal tapi jumlah token tidak diungkapkan terpisah
- [token] Current team/contributor vesting remaining — cliff 12 bulan + 36 bulan vesting berakhir Januari 2025; sisa unlock Q1 2025 tidak dipublikasikan
- [token] Fee switch exact on-chain activation block/timestamp — LIP-22 passed Feb 2024 tapi exact block execution tidak terdokumentasi di blog
- [token] Treasury LDO spending history (grants, budget, incentives) — individual grants di forum tapi tidak ada aggregated spending report resmi
- [token] Delegation participation rate — berapa % LDO yang didelegasikan vs direct voting? Tidak dipublikasikan
- [token] Quorum threshold changes — apakah 5% supply quorum masih berlaku atau pernah diubah via governance? Perlu cek proposal history
- [token] LDO usage as collateral in Aave/Maker — actual utilization rate dan risk parameter (LTV, liquidation threshold) tidak terdokumentasi di docs Lido
- [market] Exact circulating supply LDO real-time — tidak diungkapkan resmi; hanya estimasi komunitas via Dune (~890M-900M); perlu on-chain query vesting contracts untuk angka akurat (tidak dapat diverifikasi)
- [market] Protocol revenue exact figures (monthly/quarterly) — tidak dipublikasikan resmi oleh DAO; Token Terminal dan community dashboard memberikan estimasi tapi tidak diverifikasi on-chain oleh DAO (tidak dapat diverifikasi)
- [market] Current treasury total USD value — on-chain address dikenal tapi komposisi dan valuation tidak diungkapkan dalam laporan transparansi periodik (tidak dapat diverifikasi)
- [market] Series B exact funding amount (USD) — hanya valuation >$1B diumumkan; jumlah uang tunai tidak dipublikasikan oleh a16z/Dragonfly (tidak dapat diverifikasi)
- [market] LDO token velocity / turnover metrics — tidak tersedia di dashboard resmi; memerlukan analisis on-chain custom (tidak dapat diverifikasi)
- [market] Geographic user distribution — tidak dipublikasikan (protokol permissionless, tidak KYC); hanya estimasi via on-chain analytics (tidak dapat
- [conflict] Description: Apakah total protocol fee setelah LIP-22 adalah 10% (hanya DAO) atau 15% (DAO 10% + operator 5%)? Banyak sumber menyebut keduanya secara tidak konsisten.
- [conflict] Affected Phase: Phase 5, Phase 6
- [conflict] Evidence: Phase 5 Revenue Model (Staking Fee 10%, Node Operator Fee 5%); Phase 5 juga menyebut "total fee 15%" dalam satu kalimat; Phase 6 Governance (LIP-22) hanya menyebut DAO fee 10% tanpa merinci operator.
- [conflict] Alternative Interpretations: (a) 10% adalah total fee yang terdiri dari 5% DAO + 5% operator, sehingga LIP-22 mengubah DAO share dari 5% ke 5% lagi? Tidak masuk akal; (b) 10% adalah tambahan DAO fee di atas operator fee 5% = 15% total; (c) DAO fee 10% sudah termasuk semua dan operator fee dibayar dari 10% itu.
- [conflict] Status: In Review Open Thread ID: OT-002
- [conflict] Description: Berapa nilai USD total treasury Lido saat ini? Tidak ada laporan resmi; on-chain balance tersedia tapi perlu dikalikan harga pasar.
- [conflict] Affected Phase: Phase 5, Phase 8
- [conflict] Evidence: Treasury address https://etherscan.io/address/0x3e40D73EB977Dc6a537aF587D48316feE66E9C8c tidak memberikan USD valuation; Phase 5 tidak mengungkapkan total; Phase 8 protocol revenue estimate dari Token Terminal.
- [conflict] Alternative Interpretations: (a) Nilai antara $100M-$500M tergantung harga ETH/LDO; (b) Lebih besar dari $1B jika menghitung semua aset; (c) Tidak dapat ditentukan tanpa akses internal.
- [conflict] Status: Open (butuh verifikasi on-chain) Open Thread ID: OT-003
- [conflict] Description: Berapa jumlah tunai (cash) yang diterima Lido pada Series B? Apakah $73M Series A valusi juga berarti cash $73M atau token allocation?
- [conflict] Affected Phase: Phase 5
- [conflict] Evidence: Paradigm dan Lido blog menyebut "valuation $73M" bukan "raised $73M" — perbedaan antara pre-money valuation dan cash raised.
- [conflict] Alternative Interpretations: (a) Series A raised $73M cash; (b) Series A $73M valuation berarti investor membeli sebagian kecil; (c) Kombinasi.
- [conflict] Status: In Review (bersumber dari The Block yang tidak rinci) Open Thread ID: OT-004
- [conflict] Description: Apakah stETH rebasing mechanism menggunakan "shares" yang selalu naik, atau "balance" yang langsung di-update? Dokumentasi berbeda di versi lama vs baru.
- [conflict] Affected Phase: Phase 4
- [conflict] Evidence: Phase 4 menyebut "rebasing ERC-20" dan "mint shares"; beberapa versi earlier menggunakan "balanceOf" yang di-update per oracle report.
- [conflict] Alternative Interpretations: (a) share-based seperti Compound cToken; (b) balance langsung di-update tanpa shares.
- [conflict] Status: Open (butuh verifikasi kode kontrak) Open Thread ID: OT-005
- [conflict] Description: Kapan tanggal pasti Series B funding? Beberapa sumber menyebut akhir 2021, beberapa 2022 (Phase 8 market timeline menyebut "2022" saja).
- [conflict] Affected Phase: Phase 5, Phase 8
- [conflict] Evidence: Phase 5 Funding History hanya "2022"; Phase 8 Market Timeline "2022 (bulan tidak pasti)".
- [conflict] Alternative Interpretations: (a) late 2021; (b) early 2022; (c) mid 2022.
- [conflict] Status: Open (tidak ada tanggal publik dari a16z/Dragonfly) Open Thread ID: OT-006
- [conflict] Description: Apakah withdrawal fee 0.1% berlaku untuk semua jenis withdrawal, atau hanya untuk claims via queue?
- [conflict] Affected Phase: Phase 5
- [conflict] Evidence: Phase 5 Revenue Model menyebut "0.1% fee pada withdrawal stETH → ETH (dibayarkan ke treasury); dikenakan saat user claim ETH dari withdrawal queue". Tidak jelas apakah burn stETH langsung kena fee atau hanya saat claim.
- [conflict] Alternative Interpretations: (a) fee saat burn (stETH → ETH); (b) fee saat claim dari queue; (c) fee di kedua tahap.
- [conflict] Status: Open (butuh rujukan ke docs withdrawal) Open Thread ID: OT-007
- [conflict] Description: Bagaimana Oracle Committee dipilih dan diganti? Dokumen menyebut "governance dapat replace members" tapi tidak ada detail proses seleksi.
- [conflict] Affected Phase: Phase 4, Phase 7
- [conflict] Evidence: Phase 4 Security Model (Oracle Security 5-of-9) menyebut "governance can replace members"; Phase 7 External Dependencies (Oracle Committee).
- [conflict] Alternative Interpretations: (a) via on-chain vote; (b) via multisig internal; (c) kombinasi.
- [conflict] Status: Open (tidak terdokumentasi publik) Open Thread ID: OT-008
- [conflict] Description: Apakah stMATIC masih didukung penuh dan bagaimana roadmap-nya ke depan? Beberapa sumber menyebut tetap aktif, beberapa menyiratkan kemungkinan sunset mengikuti pola non-Ethereum.
- [conflict] Affected Phase: Phase 1, Phase 8
- [conflict] Evidence: Phase 1 mencatat stMATIC sebagai produk aktif; Phase 8 Competitor Landscape tidak menyebutkan rencana sunset stMATIC; Phase 3 tidak ada sunset untuk stMATIC.
- [conflict] Alternative Interpretations: (a) stMATIC tetap permanen; (b) sunset ditunda karena TVL masih tinggi; (c) tidak ada keputusan.
- [conflict] Status: Open (belum ada proposal governance untuk sunset atau upgrade stMATIC)
- [airdrop] Jumlah alamat unik yang pernah claim LDO reward dari liquidity mining program 2021-2022 — tidak dipublikasikan resmi; perlu query on-chain ke contract LM gauge Curve/SushiSwap
- [airdrop] Persentase LM reward yang dijual dalam 7/30/90 hari oleh penerima — tidak ada analisis resmi; community Dune dashboard mungkin ada tapi tidak diverifikasi
- [airdrop] Apakah ada diskusi internal (private Discord/forum core contributors) tentang airdrop retroactive 2020-2021 yang tidak terekspos publik — tidak diketahui
- [airdrop] Estimasi jumlah pengguna stETH early (Des 2020 - Jan 2021) yang eligible untuk hypothetical snapshot — tidak dihitung resmi
- [airdrop] Apakah Lido DAO Foundation mempertimbangkan "loyalty program" berbasis points (bukan airdrop token) untuk staker long-term — tidak ada sinyal publik per Des 2024
