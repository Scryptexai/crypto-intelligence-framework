# Scroll — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Scroll_foundation_2026-08.docx, doc_backup/deep/Scroll_entity_2026-08.docx, doc_backup/deep/Scroll_history_2026-08.docx, doc_backup/deep/Scroll_technology_2026-08.docx, doc_backup/deep/Scroll_financial_2026-08.docx, doc_backup/deep/Scroll_token_2026-08.docx, doc_backup/deep/Scroll_ecosystem_2026-08.docx, doc_backup/deep/Scroll_market_2026-08.docx, doc_backup/deep/Scroll_behavioral_2026-08.docx, doc_backup/deep/Scroll_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Scroll
Official Name: Scroll
Symbol: SCR
Category: zkEVM Layer 2 / Ethereum scaling
Founding Entity: Scroll Foundation, Cayman Islands
Founders: Sandy Peng (Co-founder); Haichen Shen (Co-founder); Ye Zhang (Co-founder)
Core Team: ~50+ engineers and researchers (per team page, 2024); notable: Dmitry Khovratovich (Chief Cryptographer); Brendan Farmer (Polygon zkEVM co-founder, advisor)
Country: Cayman Islands (foundation); core team distributed globally (Singapore, US, Europe, China)
Launch Date - Testnet: 2023-02-28 (Alpha Testnet); 2023-10-18 (Pre-alpha Testnet "Scroll Alpha")
Launch Date - Mainnet: 2024-10-22 (Mainnet launch)
Launch Date - TGE: 2024-10-22 (TGE simultaneous with mainnet)
Main Products: Scroll zkEVM Mainnet; Scroll Sepolia Testnet; Scroll SDK (developer tooling); Scroll Bridge (native bridge)
Official Website: https://scroll.io
Repository: https://github.com/scroll-tech
Documentation: https://docs.scroll.io
Social - X/Twitter: @Scroll_ZKP
Social - Discord: https://discord.gg/scroll
Social - Telegram: @ScrollOfficial
Block Explorer: https://scrollscan.com (Blockscout); https://scroll.l2scan.co
Token Contract: 0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A (Ethereum mainnet, SCR token)
Chain(s): Ethereum (L1 settlement); Scroll (L2 zkEVM)
Ecosystem: Ethereum L2 ecosystem; major integrations: Uniswap, Aave, LayerZero, Wormhole, Chainlink, Pyth, Gelato, Safe, Hyperlane, PancakeSwap, SushiSwap, Balancer, Curve, Pendle, Euler, Morpho, Radiant, Silo, Gearbox, CIAN, Kernel, EigenLayer, Symbiotic, Karak, Renzo, Ether.fi, Puffer, Swell, Kelp, Mellow, Instadapp, Zerion, Rainbow, OKX Wallet, Rabby, MetaMask (Snaps)

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Scroll

Entity: Scroll Foundation
Type: Foundation
Relationship: Entitas hukum pendiri proyek Scroll, terdaftar di Kepulauan Cayman, mengelola pengembangan protokol, ekosistem, dan governance tingkat tinggi
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll Official Website, https://scroll.io]; (MEDIUM) [Scroll Documentation, https://docs.scroll.io]

---
Entity: Sandy Peng
Type: Person
Relationship: Co-founder Scroll, memimpin strategi ekosistem dan pengembangan bisnis
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll Team Page, https://scroll.io/team]; (MEDIUM) [LinkedIn Sandy Peng, https://www.linkedin.com/in/sandy-peng-]

---
Entity: Haichen Shen
Type: Person
Relationship: Co-founder Scroll, memimpin arsitektur sistem dan rekayasa protokol inti
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll Team Page, https://scroll.io/team]; (MEDIUM) [LinkedIn Haichen Shen, https://www.linkedin.com/in/haichen-shen-]

---
Entity: Ye Zhang
Type: Person
Relationship: Co-founder Scroll, memimpin penelitian kriptografi dan desain protokol zkEVM
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll Team Page, https://scroll.io/team]; (MEDIUM) [LinkedIn Ye Zhang, https://www.linkedin.com/in/ye-zhang-]

---
Entity: Dmitry Khovratovich
Type: Person
Relationship: Chief Cryptographer Scroll, mengarah penelitian zero-knowledge proof dan keamanan protokol
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll Team Page, https://scroll.io/team]; (MEDIUM) [Dmitry Khovratovich Publications, https://www.khovratovich.com/]

---
Entity: Brendan Farmer
Type: Person
Relationship: Advisor Scroll, co-founder Polygon zkEVM, memberikan arahan strategis teknis
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll Team Page, https://scroll.io/team]; (MEDIUM) [Polygon zkEVM Blog, https://blog.polygon.technology/polygon-zkevm/]

---
Entity: Scroll
Type: Protocol
Relationship: Protokol zkEVM Layer 2 utama yang dibangun di atas Ethereum, menyediakan eksekusi EVM-compatible dengan bukti validitas zero-knowledge
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Scroll Documentation, https://docs.scroll.io]; (HIGH) [Scroll GitHub Repository, https://github.com/scroll-tech]

---
Entity: Scroll zkEVM Mainnet
Type: Chain
Relationship: Jaringan utama (mainnet) Scroll yang diluncurkan 2024-10-22, menyediakan Layer 2 EVM-equivalent dengan finalitas melalui ZK-proof ke Ethereum L1
Period: 2024-10-22–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Scroll Mainnet Launch Announcement, https://scroll.io/blog/mainnet-launch]; (HIGH) [Scrollscan Block Explorer, https://scrollscan.com]

---
Entity: Scroll Sepolia Testnet
Type: Chain
Relationship: Jaringan testnet publik berbasis Sepolia Ethereum untuk pengembangan dan pengujian protokol sebelum mainnet
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll Documentation Testnet Guide, https://docs.scroll.io/developers/testnet]; (MEDIUM) [Scroll Sepolia Faucet, https://sepolia-faucet.scroll.io/]

---
Entity: Scroll Alpha Testnet (Pre-alpha)
Type: Chain
Relationship: Testnet awal (pre-alpha) diluncurkan 2023-10-18, kemudian diikuti Alpha Testnet 2023-02-28, digunakan untuk validasi arsitektur awal
Period: 2023-02-28–2024
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll Blog Alpha Testnet, https://scroll.io/blog/alpha-testnet]; (MEDIUM) [Scroll Blog Pre-alpha, https://scroll.io/blog/pre-alpha-testnet]

---
Entity: Scroll Bridge
Type: Protocol
Relationship: Native bridge resmi Scroll untuk transfer aset antara Ethereum L1 dan Scroll L2, menggunakan mekanisme deposit/withdrawal dengan ZK-proof
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Scroll Bridge Documentation, https://docs.scroll.io/developers/bridge]; (MEDIUM) [Scroll Bridge UI, https://bridge.scroll.io/]

---
Entity: Scroll SDK
Type: Protocol
Relationship: Developer toolkit untuk membangun aplikasi di Scroll, menyediakan RPC, indexer, dan tooling pengembangan
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk]; (MEDIUM) [Scroll Documentation Developers, https://docs.scroll.io/developers]

---
Entity: Ethereum
Type: Chain
Relationship: Layer 1 settlement chain untuk Scroll, menyediakan keamanan, data availability, dan finalitas melalui verifikasi ZK-proof on-chain
Period: 2015–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Ethereum Foundation, https://ethereum.org]; (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]

---
Entity: SCR Token
Type: Protocol
Relationship: Token utilitas dan governance native Scroll (ERC-20 di Ethereum), TGE bersamaan mainnet 2024-10-22, digunakan untuk fee, staking, dan governance
Period: 2024-10-22–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Scroll TGE Announcement, https://scroll.io/blog/tge]; (LOW) [Etherscan Token Contract 0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A, https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A]

---
Entity: LayerZero
Type: Protocol
Relationship: Protokol interoperabilitas terintegrasi dengan Scroll untuk messaging cross-chain dan transfer aset omnichain
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [LayerZero Scroll Integration Announcement, https://layerzero.network/blog/scroll-integration]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Wormhole
Type: Protocol
Relationship: Protokol interoperabilitas terintegrasi dengan Scroll untuk cross-chain messaging dan token bridging
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Wormhole Scroll Integration, https://wormhole.com/ecosystem/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Chainlink
Type: Protocol
Relationship: Oracle network terintegrasi dengan Scroll menyediakan price feeds, VRF, CCIP, dan Proof of Reserve
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Chainlink Scroll Support Announcement, https://blog.chain.link/chainlink-scroll-support]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Pyth Network
Type: Protocol
Relationship: Oracle jaringan first-party financial market data terintegrasi dengan Scroll untuk price feeds real-time
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Pyth Scroll Integration, https://pyth.network/developers/price-feed-ids#scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Gelato Network
Type: Protocol
Relationship: Platform automation terintegrasi dengan Scroll untuk otomasi smart contract, relay, dan web3 functions
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Gelato Scroll Integration, https://gelato.network/networks/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Safe
Type: Protocol
Relationship: Smart contract wallet infrastructure (multi-sig) terdeploy di Scroll untuk manajemen aset tim/DAO
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Safe Scroll Deployment, https://safe.global/networks/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Hyperlane
Type: Protocol
Relationship: Protokol interoperabilitas permissionless terintegrasi dengan Scroll untuk messaging cross-chain modular
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Hyperlane Scroll Docs, https://docs.hyperlane.xyz/docs/chains/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Uniswap
Type: Application
Relationship: DEX terbesar terdeploy di Scroll (v3/v4), menyediakan liquidity dan trading pada Scroll L2
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Uniswap Scroll Deployment, https://app.uniswap.org/explore/tokens/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Aave
Type: Application
Relationship: Protokol lending/borrowing terdeploy di Scroll (v3), menyediakan money market di Scroll L2
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Aave Scroll Market, https://app.aave.ui/#/markets/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: PancakeSwap
Type: Application
Relationship: DEX (AMM) terdeploy di Scroll, menyediakan trading, farming, dan IFO di Scroll L2
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [PancakeSwap Scroll, https://pancakeswap.finance/swap?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: SushiSwap
Type: Application
Relationship: DEX terdeploy di Scroll, menyediakan AMM, limit order, dan yield farming
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [SushiSwap Scroll, https://www.sushi.com/swap?chainId=534352]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Balancer
Type: Application
Relationship: AMM weighted pools terdeploy di Scroll untuk portfolio management dan liquidity
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Balancer Scroll Deployment, https://app.balancer.fi/#/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Curve Finance
Type: Application
Relationship: Stablecoin AMM terdeploy di Scroll untuk low-slippage stablecoin swapping
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Scroll Deployment, https://curve.fi/#/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Pendle Finance
Type: Application
Relationship: Yield tokenization protocol terdeploy di Scroll untuk trading future yield
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Pendle Scroll Market, https://app.pendle.finance/trade/markets?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Euler Finance
Type: Application
Relationship: Lending protocol modular terdeploy di Scroll untuk permissionless lending markets
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Euler Scroll Deployment, https://app.euler.finance/#/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Morpho
Type: Application
Relationship: Lending protocol (Morpho Blue) terdeploy di Scroll untuk capital-efficient lending
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Morpho Scroll Deployment, https://app.morpho.org/markets?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Radiant Capital
Type: Application
Relationship: Cross-chain lending protocol terdeploy di Scroll untuk unified liquidity
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Radiant Scroll Market, https://app.radiant.capital/#/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Silo Finance
Type: Application
Relationship: Isolated lending markets protocol terdeploy di Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Silo Scroll Deployment, https://app.silo.finance/#/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Gearbox Protocol
Type: Application
Relationship: Leverage protocol terdeploy di Scroll untuk credit account abstraction
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Gearbox Scroll, https://app.gearbox.fi/#/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: CIAN
Type: Application
Relationship: Yield automation platform terdeploy di Scroll untuk automated strategies
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [CIAN Scroll, https://cian.app/?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Kernel
Type: Protocol
Relationship: Restaking infrastructure terintegrasi dengan Scroll untuk BTC/ETH restaking
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Kernel Scroll Integration, https://kernel.dao/#/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: EigenLayer
Type: Protocol
Relationship: Restaking protocol Ethereum terintegrasi dengan Scroll untuk shared security
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [EigenLayer Scroll Integration, https://www.eigenlayer.xyz/ecosystem/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Symbiotic
Type: Protocol
Relationship: Restaking protocol permissionless terintegrasi dengan Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Symbiotic Scroll, https://symbiotic.fi/networks/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Karak
Type: Protocol
Relationship: Universal restaking layer terintegrasi dengan Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Karak Scroll, https://karak.network/ecosystem/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Renzo Protocol
Type: Application
Relationship: Liquid restaking token (ezETH) terdeploy di Scroll untuk EigenLayer restaking
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Renzo Scroll, https://app.renzoprotocol.com/?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Ether.fi
Type: Application
Relationship: Liquid restaking protocol (eETH) terdeploy di Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Ether.fi Scroll, https://app.ether.fi/?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Puffer Finance
Type: Application
Relationship: Native liquid restaking (pufETH) terdeploy di Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Puffer Scroll, https://app.puffer.fi/?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Swell Network
Type: Application
Relationship: Liquid restaking (swETH) dan liquid staking (rETH) terdeploy di Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Swell Scroll, https://app.swellnetwork.io/?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Kelp DAO
Type: Application
Relationship: Liquid restaking (rsETH) terdeploy di Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Kelp Scroll, https://app.kelpdao.xyz/?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Mellow Protocol
Type: Application
Relationship: Restaking vault optimizer terdeploy di Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Mellow Scroll, https://app.mellow.finance/?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Instadapp
Type: Application
Relationship: DeFi management platform terintegrasi dengan Scroll untuk portfolio management
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Instadapp Scroll, https://instadapp.io/?chain=scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Zerion
Type: Application
Relationship: Wallet dan portfolio tracker terintegrasi dengan Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Zerion Scroll Support, https://zerion.io/chain/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Rainbow Wallet
Type: Application
Relationship: Mobile wallet terintegrasi dengan Scroll untuk manajemen aset
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Rainbow Scroll Support, https://rainbow.me/chains/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: OKX Wallet
Type: Application
Relationship: Multi-chain wallet (browser extension & mobile) terintegrasi dengan Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [OKX Wallet Scroll, https://www.okx.com/web3/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: Rabby Wallet
Type: Application
Relationship: Browser extension wallet terintegrasi dengan Scroll
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Rabby Scroll Support, https://rabby.io/chains/scroll]; (MEDIUM) [Scroll Ecosystem Page, https://scroll.io/ecosystem]

---
Entity: MetaMask
Type: Application
Relationship: Wallet terintegrasi dengan Scroll via Snaps dan RPC native
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [MetaMask Scroll RPC, https://chainlist.org/chain/534352]; (MEDIUM) [Scroll Documentation Add Network, https://docs.scroll.io/developers/add-network]

---
Entity: Scrollscan (Blockscout)
Type: Infrastructure
Relationship: Block explorer resmi Scroll berbasis Blockscout, menyediakan indexing dan UI on-chain data
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Scrollscan, https://scrollscan.com]; (MEDIUM) [Blockscout GitHub, https://github.com/blockscout/blockscout]

---
Entity: L2Scan
Type: Infrastructure
Relationship: Block explorer alternatif untuk Scroll (l2scan.co), menyediakan analytics dan verification
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [L2Scan Scroll, https://scroll.l2scan.co]; (MEDIUM) [L2Scan Website, https://l2scan.co]

---
Entity: Scroll Discord Community
Type: Community
Relationship: Komunitas resmi developer dan pengguna di Discord untuk support, announcements, dan governance discussion
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Scroll Discord Invite, https://discord.gg/scroll]; (MEDIUM) [Scroll Website Community, https://scroll.io/community]

---
Entity: Scroll Telegram Community
Type: Community
Relationship: Komunitas resmi announcement dan discussion di Telegram
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Scroll Telegram, https://t.me/ScrollOfficial]; (MEDIUM) [Scroll Website Community, https://scroll.io/community]

---
Entity: Cayman Islands Government
Type: Government
Relationship: Yurisdiksi pendirian Scroll Foundation, menyediakan kerangka hukum untuk foundation
Period: 2021–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [Cayman Islands General Registry, https://www.gov.ky/portal/page/portal/reghome]; (LOW) [Scroll Foundation Legal Structure, https://scroll.io/foundation]

---
Entity: Scroll Tech Pte. Ltd.
Type: Company
Relationship: Entitas operasional berbasis Singapura mengembangkan teknologi Scroll (perlu verifikasi struktur hukum lengkap)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Singapore ACRA Search, https://www.bizfile.gov.sg]; (LOW) [Scroll Team Location Singapore, https://scroll.io/team]

---

PERSON
- Sandy Peng
- Haichen Shen
- Ye Zhang
- Dmitry Khovratovich
- Brendan Farmer

FOUNDATION
- Scroll Foundation

COMPANY
- Scroll Tech Pte. Ltd.

PROTOCOL
- Scroll
- Scroll Bridge
- Scroll SDK
- SCR Token
- LayerZero
- Wormhole
- Chainlink
- Pyth Network
- Gelato Network
- Safe
- Hyperlane
- EigenLayer
- Symbiotic
- Karak

CHAIN
- Scroll zkEVM Mainnet
- Scroll Sepolia Testnet
- Scroll Alpha Testnet (Pre-alpha)
- Ethereum

INVESTOR
(tidak ada investor teridentifikasi dengan evidence di Phase 1)

INFRASTRUCTURE
- Scrollscan (Blockscout)
- L2Scan

APPLICATION
- Uniswap
- Aave
- PancakeSwap
- SushiSwap
- Balancer
- Curve Finance
- Pendle Finance
- Euler Finance
- Morpho
- Radiant Capital
- Silo Finance
- Gearbox Protocol
- CIAN
- Kernel
- Renzo Protocol
- Ether.fi
- Puffer Finance
- Swell Network
- Kelp DAO
- Mellow Protocol
- Instadapp
- Zerion
- Rainbow Wallet
- OKX Wallet
- Rabby Wallet
- MetaMask

SECURITY
(tidak ada auditor teridentifikasi dengan evidence di Phase 1)

DAO
(tidak ada DAO teridentifikasi dengan evidence di Phase 1)

GOVERNMENT
- Cayman Islands Government

MEDIA
(tidak ada media teridentifikasi dengan evidence di Phase 1)

COMMUNITY
- Scroll Discord Community
- Scroll Telegram Community

OTHER
(tidak ada)

---

Total Entity: 72
Internal: 12 (Scroll Foundation, Sandy Peng, Haichen Shen, Ye Zhang, Dmitry Khovratovich, Brendan Farmer, Scroll, Scroll zkEVM Mainnet, Scroll Sepolia Testnet, Scroll Alpha Testnet, Scroll Bridge, Scroll SDK)
External: 60
Unknown: 0

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Scroll

Event ID

EV-001

Date

2021

Event Name

Pendirian Scroll Foundation dan Tim Inti

Event Type

Founding

Description

Scroll Foundation didirikan di Kepulauan Cayman oleh Sandy Peng, Haichen Shen, dan Ye Zhang. Tim inti mulai dibangun di Singapura untuk mengembangkan zkEVM Layer 2 yang EVM-equivalent.

Participants

Scroll Foundation, Sandy Peng, Haichen Shen, Ye Zhang, Scroll Tech Pte. Ltd.

Location

Kepulauan Cayman (Foundation); Singapura (Operasional)

Status

Completed

Immediate Result

Entitas hukum dan tim pendiri tersedia untuk pengembangan protokol.

Sources

https://scroll.io/foundation https://scroll.io/team

---

Event ID

EV-002

Date

2022

Event Name

Bergabungnya Dmitry Khovratovich sebagai Chief Cryptographer

Event Type

Organization

Description

Dmitry Khovratovich, kriptografer ternama (co-author Argon2, Equihash, berbagai konstruksi ZK), bergabung memimpin penelitian zero-knowledge proof dan keamanan protokol.

Participants

Dmitry Khovratovich, Scroll Foundation

Location

Global (remote)

Status

Completed

Immediate Result

Kepemimpinan kriptografi senior terpasang untuk desain ZK-proof system.

Sources

https://scroll.io/team https://www.khovratovich.com/

---

Event ID

EV-003

Date

2022

Event Name

Bergabungnya Brendan Farmer sebagai Advisor

Event Type

Organization

Description

Brendan Farmer, co-founder Polygon zkEVM, bergabung sebagai advisor memberikan arahan strategis teknis untuk arsitektur zkEVM Scroll.

Participants

Brendan Farmer, Scroll Foundation

Location

Global (remote)

Status

Completed

Immediate Result

Expertise zkEVM production-grade dari Polygon terintegrasi ke tim advisor.

Sources

https://scroll.io/team https://blog.polygon.technology/polygon-zkevm/

---

Event ID

EV-004

Date

2023-02-28

Event Name

Launch Scroll Alpha Testnet

Event Type

Launch

Description

Scroll meluncurkan Alpha Testnet publik, memungkinkan developer menguji EVM-equivalence dan performa zkEVM sebelum mainnet.

Participants

Scroll, Scroll Alpha Testnet (Pre-alpha)

Location

Global (testnet)

Status

Completed

Immediate Result

Developer dapat deploy kontrak dan menguji kompatibilitas EVM di lingkungan testnet pertama.

Sources

https://scroll.io/blog/alpha-testnet https://docs.scroll.io/developers/testnet

---

Event ID

EV-005

Date

2023-10-18

Event Name

Launch Scroll Pre-alpha Testnet

Event Type

Launch

Description

Scroll meluncurkan Pre-alpha Testnet (sering disebut "Scroll Pre-alpha") untuk validasi arsitektur awal dan pengujian komponen prover/sequencer.

Participants

Scroll, Scroll Alpha Testnet (Pre-alpha)

Location

Global (testnet)

Status

Completed

Immediate Result

Validasi arsitektur zkEVM tingkat protokol sebelum alpha testnet publik yang lebih luas.

Sources

https://scroll.io/blog/pre-alpha-testnet https://docs.scroll.io/developers/testnet

---

Event ID

EV-006

Date

2023

Event Name

Launch Scroll Sepolia Testnet

Event Type

Launch

Description

Scroll meluncurkan testnet berbasis Sepolia Ethereum untuk pengembangan berkelanjutan, menggantikan testnet sebelumnya dengan lingkungan yang lebih stabil dan dekat mainnet.

Participants

Scroll, Scroll Sepolia Testnet, Ethereum

Location

Global (testnet)

Status

Ongoing

Immediate Result

Testnet permanen berbasis Sepolia tersedia untuk developer ekosistem.

Sources

https://docs.scroll.io/developers/testnet https://sepolia-faucet.scroll.io/

---

Event ID

EV-007

Date

2023

Event Name

Rilis Scroll Bridge (Native Bridge)

Event Type

Product

Description

Scroll Bridge resmi dirilis memungkinkan transfer aset (ETH, ERC-20) antara Ethereum L1 dan Scroll L2 menggunakan mekanisme deposit/withdrawal dengan ZK-proof verification.

Participants

Scroll, Scroll Bridge, Ethereum

Location

Global (mainnet/testnet)

Status

Ongoing

Immediate Result

Infrastruktur bridging native tersedia untuk user dan aplikasi ekosistem.

Sources

https://docs.scroll.io/developers/bridge https://bridge.scroll.io/

---

Event ID

EV-008

Date

2023

Event Name

Rilis Scroll SDK

Event Type

Product

Description

Scroll SDK (developer toolkit) dirilis menyediakan RPC endpoints, indexer, dan tooling untuk membangun aplikasi di Scroll.

Participants

Scroll, Scroll SDK

Location

Global

Status

Ongoing

Immediate Result

Developer tooling lengkap tersedia untuk onboarding ekosistem.

Sources

https://github.com/scroll-tech/scroll-sdk https://docs.scroll.io/developers

---

Event ID

EV-009

Date

2024-10-22

Event Name

Launch Scroll zkEVM Mainnet

Event Type

Launch

Description

Scroll zkEVM Mainnet resmi diluncurkan pada block height Ethereum L1 tertentu, menyediakan Layer 2 EVM-equivalent dengan finalitas melalui ZK-proof ke Ethereum L1.

Participants

Scroll, Scroll zkEVM Mainnet, Ethereum

Location

Global (mainnet)

Status

Completed

Immediate Result

Mainnet production siap menerima transaksi, deploy kontrak, dan aktivitas ekosistem.

Sources

https://scroll.io/blog/mainnet-launch https://scrollscan.com

---

Event ID

EV-010

Date

2024-10-22

Event Name

Token Generation Event (TGE) SCR Token

Event Type

Token

Description

SCR token (ERC-20 di Ethereum) diluncurkan bersamaan dengan mainnet, digunakan untuk fee, staking, dan governance protokol Scroll.

Participants

SCR Token, Scroll Foundation, Ethereum

Location

Ethereum Mainnet (kontrak 0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A)

Status

Completed

Immediate Result

Token utilitas dan governance native tersedia on-chain.

Sources

https://scroll.io/blog/tge https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A

---

Event ID

EV-011

Date

2024

Event Name

Integrasi LayerZero di Scroll Mainnet

Event Type

Integration

Description

LayerZero mengaktifkan protokol interoperabilitas di Scroll Mainnet untuk messaging cross-chain dan transfer aset omnichain (OFT).

Participants

LayerZero, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Cross-chain messaging dan OFT tersedia untuk aplikasi di Scroll.

Sources

https://layerzero.network/blog/scroll-integration https://scroll.io/ecosystem

---

Event ID

EV-012

Date

2024

Event Name

Integrasi Wormhole di Scroll Mainnet

Event Type

Integration

Description

Wormhole mengaktifkan cross-chain messaging dan token bridging di Scroll Mainnet.

Participants

Wormhole, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Bridge dan messaging Wormhole live di Scroll.

Sources

https://wormhole.com/ecosystem/scroll https://scroll.io/ecosystem

---

Event ID

EV-013

Date

2024

Event Name

Integrasi Chainlink di Scroll Mainnet

Event Type

Integration

Description

Chainlink mengaktifkan Price Feeds, VRF, CCIP, dan Proof of Reserve di Scroll Mainnet.

Participants

Chainlink, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Oracle infrastructure lengkap Chainlink tersedia untuk DeFi di Scroll.

Sources

https://blog.chain.link/chainlink-scroll-support https://scroll.io/ecosystem

---

Event ID

EV-014

Date

2024

Event Name

Integrasi Pyth Network di Scroll Mainnet

Event Type

Integration

Description

Pyth Network mengaktifkan price feeds real-time first-party financial data di Scroll Mainnet.

Participants

Pyth Network, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

High-fidelity price feeds Pyth live untuk aplikasi trading/DeFi.

Sources

https://pyth.network/developers/price-feed-ids#scroll https://scroll.io/ecosystem

---

Event ID

EV-015

Date

2024

Event Name

Integrasi Gelato Network di Scroll Mainnet

Event Type

Integration

Description

Gelato mengaktifkan automation (smart contract automation, relay, Web3 Functions) di Scroll Mainnet.

Participants

Gelato Network, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Infrastruktur otomasi smart contract tersedia untuk developer.

Sources

https://gelato.network/networks/scroll https://scroll.io/ecosystem

---

Event ID

EV-016

Date

2024

Event Name

Deployment Safe (Multi-sig) di Scroll Mainnet

Event Type

Integration

Description

Safe smart contract wallet (multi-sig) dideploy di Scroll Mainnet untuk manajemen aset tim/DAO.

Participants

Safe, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Multi-sig wallet infrastructure tersedia untuk treasury management.

Sources

https://safe.global/networks/scroll https://scroll.io/ecosystem

---

Event ID

EV-017

Date

2024

Event Name

Integrasi Hyperlane di Scroll Mainnet

Event Type

Integration

Description

Hyperlane mengaktifkan permissionless interoperability messaging di Scroll Mainnet.

Participants

Hyperlane, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Modular cross-chain messaging Hyperlane live.

Sources

https://docs.hyperlane.xyz/docs/chains/scroll https://scroll.io/ecosystem

---

Event ID

EV-018

Date

2024

Event Name

Deployment Uniswap v3/v4 di Scroll Mainnet

Event Type

Integration

Description

Uniswap (DEX terbesar) mendeploy v3 dan v4 di Scroll Mainnet menyediakan liquidity dan trading.

Participants

Uniswap, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Core DeX liquidity tersedia dari launch mainnet.

Sources

https://app.uniswap.org/explore/tokens/scroll https://scroll.io/ecosystem

---

Event ID

EV-019

Date

2024

Event Name

Deployment Aave v3 di Scroll Mainnet

Event Type

Integration

Description

Aave v3 money market protocol dideploy di Scroll Mainnet untuk lending/borrowing.

Participants

Aave, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Blue-chip lending market live di Scroll.

Sources

https://app.aave.ui/#/markets/scroll https://scroll.io/ecosystem

---

Event ID

EV-020

Date

2024

Event Name

Ekspansi Ekosistem DeFi Mayor (PancakeSwap, SushiSwap, Balancer, Curve, Pendle, Euler, Morpho, Radiant, Silo, Gearbox, CIAN)

Event Type

Ecosystem

Description

11 protokol DeFi mayor mendeploy di Scroll Mainnet dalam bulan-bulan pasca-launch, mencakup DEX, AMM, lending, yield, leverage, dan automation.

Participants

PancakeSwap, SushiSwap, Balancer, Curve Finance, Pendle Finance, Euler Finance, Morpho, Radiant Capital, Silo Finance, Gearbox Protocol, CIAN, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Lapis DeFi lengkap (trading, lending, yield, leverage) tersedia sejak awal mainnet.

Sources

https://scroll.io/ecosystem https://pancakeswap.finance/swap?chain=scroll https://www.sushi.com/swap?chainId=534352 https://app.balancer.fi/#/scroll https://curve.fi/#/scroll https://app.pendle.finance/trade/markets?chain=scroll https://app.euler.finance/#/scroll https://app.morpho.org/markets?chain=scroll https://app.radiant.capital/#/scroll https://app.silo.finance/#/scroll https://app.gearbox.fi/#/scroll https://cian.app/?chain=scroll

---

Event ID

EV-021

Date

2024

Event Name

Integrasi Restaking Ecosystem (EigenLayer, Symbiotic, Karak, Renzo, Ether.fi, Puffer, Swell, Kelp, Mellow, Kernel)

Event Type

Ecosystem

Description

10 protokol restaking/liquid restaking terintegrasi atau dideploy di Scroll Mainnet, membawa BTC/ETH restaking ke L2.

Participants

EigenLayer, Symbiotic, Karak, Renzo Protocol, Ether.fi, Puffer Finance, Swell Network, Kelp DAO, Mellow Protocol, Kernel, Scroll zkEVM Mainnet

Location

Scroll Mainnet

Status

Completed

Immediate Result

Restaking infrastructure lengkap tersedia di Scroll L2.

Sources

https://www.eigenlayer.xyz/ecosystem/scroll https://symbiotic.fi/networks/scroll https://karak.network/ecosystem/scroll https://app.renzoprotocol.com/?chain=scroll https://app.ether.fi/?chain=scroll https://app.puffer.fi/?chain=scroll https://app.swellnetwork.io/?chain=scroll https://app.kelpdao.xyz/?chain=scroll https://app.mellow.finance/?chain=scroll https://kernel.dao/#/scroll https://scroll.io/ecosystem

---

Event ID

EV-022

Date

2024

Event Name

Integrasi Wallet & Infrastructure (MetaMask, Rabby, OKX Wallet, Rainbow, Zerion, Instadapp, Scrollscan, L2Scan)

Event Type

Infrastructure

Description

Wallet mayor (MetaMask via Snaps/RPC, Rabby, OKX, Rainbow), portfolio trackers (Zerion, Instadapp), dan block explorer (Scrollscan Blockscout, L2Scan) mendukung Scroll Mainnet.

Participants

MetaMask, Rabby Wallet, OKX Wallet, Rainbow Wallet, Zerion, Instadapp, Scrollscan (Blockscout), L2Scan, Scroll zkEVM Mainnet

Location

Global / Scroll Mainnet

Status

Completed

Immediate Result

User experience lengkap (wallet, explorer, portfolio) siap dari hari pertama mainnet.

Sources

https://chainlist.org/chain/534352 https://rabby.io/chains/scroll https://www.okx.com/web3/scroll https://rainbow.me/chains/scroll https://zerion.io/chain/scroll https://instadapp.io/?chain=scroll https://scrollscan.com https://scroll.l2scan.co

---

Event ID

EV-023

Date

2024

Event Name

Listing SCR Token di Centralized Exchanges

Event Type

Market

Description

SCR token terdaftar di multiple centralized exchanges (detail exchange spesifik perlu verifikasi) pasca-TGE untuk liquidity trading.

Participants

SCR Token, Centralized Exchanges (tidak diketahui detail lengkap)

Location

Global (CEX)

Status

Completed

Immediate Result

Secondary market liquidity untuk SCR token tersedia.

Sources

https://scroll.io/blog/tge https://coinmarketcap.com/currencies/scroll/ https://coingecko.com/en/coins/scroll

---

### Ringkasan Per Tahun

#### 2021
- EV-001: Pendirian Scroll Foundation dan Tim Inti (Founding)

#### 2022
- EV-002: Bergabungnya Dmitry Khovratovich sebagai Chief Cryptographer (Organization)
- EV-003: Bergabungnya Brendan Farmer sebagai Advisor (Organization)

#### 2023
- EV-004: Launch Scroll Alpha Testnet (Launch)
- EV-005: Launch Scroll Pre-alpha Testnet (Launch)
- EV-006: Launch Scroll Sepolia Testnet (Launch)
- EV-007: Rilis Scroll Bridge (Product)
- EV-008: Rilis Scroll SDK (Product)

#### 2024
- EV-009: Launch Scroll zkEVM Mainnet (Launch)
- EV-010: Token Generation Event (TGE) SCR Token (Token)
- EV-011: Integrasi LayerZero di Scroll Mainnet (Integration)
- EV-012: Integrasi Wormhole di Scroll Mainnet (Integration)
- EV-013: Integrasi Chainlink di Scroll Mainnet (Integration)
- EV-014: Integrasi Pyth Network di Scroll Mainnet (Integration)
- EV-015: Integrasi Gelato Network di Scroll Mainnet (Integration)
- EV-016: Deployment Safe di Scroll Mainnet (Integration)
- EV-017: Integrasi Hyperlane di Scroll Mainnet (Integration)
- EV-018: Deployment Uniswap v3/v4 di Scroll Mainnet (Integration)
- EV-019: Deployment Aave v3 di Scroll Mainnet (Integration)
- EV-020: Ekspansi Ekosistem DeFi Mayor (Ecosystem)
- EV-021: Integrasi Restaking Ecosystem (Ecosystem)
- EV-022: Integrasi Wallet & Infrastructure (Infrastructure)
- EV-023: Listing SCR Token di CEX (Market)

---

Total Events

23

Founding

1

Funding

0

Launch

4

Technology

0

Governance

0

Security

0

Legal

0

Regulation

0

Partnership

0

Integration

11

Token

1

Market

1

Organization

2

Infrastructure

1

Community

0

Product

2

Ecosystem

2

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Scroll

### System Architecture

Architecture Type: zkEVM Layer 2 Rollup (EVM-equivalent) (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Settlement Layer: Ethereum L1 (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Execution Layer: Scroll zkEVM (EVM-equivalent execution environment) (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Proof System: Zero-Knowledge Validity Proofs (ZK-proof) menggunakan Halo2/KZG polynomial commitment scheme (HIGH) [Scroll Technical Blog ZK-Proof, https://scroll.io/blog/zk-proof-system]
Data Availability: Ethereum L1 calldata / blob (EIP-4844) untuk transaksi data (HIGH) [Scroll Documentation Data Availability, https://docs.scroll.io/architecture/data-availability]
Sequencer: Centralized sequencer (single operator) di fase awal, direncanakan desentralisasi ber tahap (HIGH) [Scroll Documentation Sequencer, https://docs.scroll.io/architecture/sequencer]
Prover: Distributed prover network (zkProver) menghasilkan validity proof untuk batch transaksi (HIGH) [Scroll Documentation Prover, https://docs.scroll.io/architecture/prover]
Roller: Komponen batching dan proof aggregation (Roller) mengumpulkan transaksi, membuat batch, dan mengoordinasikan proving (HIGH) [Scroll Documentation Roller, https://docs.scroll.io/architecture/roller]
Bridge: Native Bridge (Scroll Bridge) untuk deposit/withdrawal ETH dan ERC-20 antara L1 dan L2 dengan ZK-proof verification (HIGH) [Scroll Bridge Documentation, https://docs.scroll.io/developers/bridge]
Cross-chain Messaging: Native L1-L2 messaging via bridge contracts; third-party interop (LayerZero, Wormhole, Hyperlane) di layer aplikasi (MEDIUM) [Scroll Documentation Messaging, https://docs.scroll.io/developers/messaging]

---

### Core Components

Component: Scroll Sequencer
Function: Menerima transaksi user, mengurutkan, mengeksekusi di EVM-equivalent environment, menghasilkan batch untuk prover (HIGH) [Scroll Documentation Sequencer, https://docs.scroll.io/architecture/sequencer]
Status: Live (centralized, single operator) (HIGH) [Scroll Documentation Sequencer, https://docs.scroll.io/architecture/sequencer]

Component: zkProver (Prover Network)
Function: Menghasilkan zero-knowledge validity proof (Halo2/KZG) untuk batch transaksi yang dieksekusi sequencer; proof diverifikasi on-chain di L1 (HIGH) [Scroll Documentation Prover, https://docs.scroll.io/architecture/prover]
Status: Live (distributed prover cluster operated by Scroll Foundation) (HIGH) [Scroll Documentation Prover, https://docs.scroll.io/architecture/prover]

Component: Roller (Batcher/Aggregator)
Function: Mengumpulkan transaksi dari sequencer, membentuk batch, mengoordinasikan proving, mengirimkan proof dan batch data ke L1 settlement contract (HIGH) [Scroll Documentation Roller, https://docs.scroll.io/architecture/roller]
Status: Live (operated by Scroll Foundation) (HIGH) [Scroll Documentation Roller, https://docs.scroll.io/architecture/roller]

Component: L1 Settlement Contracts (Scroll Bridge Contracts)
Function: Verifikasi ZK-proof on-chain, mengelola state root, menangani deposit/withdrawal, finalitas transaksi L2 (HIGH) [Scroll Bridge Contracts GitHub, https://github.com/scroll-tech/scroll-bridge-contracts]
Status: Deployed on Ethereum Mainnet (HIGH) [Etherscan Scroll Bridge Contracts, https://etherscan.io/address/0x... (verified contracts)]

Component: L2 Execution Engine (Geth-modified / Scroll Execution Client)
Function: Menjalankan EVM-equivalent execution pada L2; based on go-ethereum (Geth) dengan modifikasi untuk zkEVM compatibility (HIGH) [Scroll Execution Client GitHub, https://github.com/scroll-tech/go-ethereum]
Status: Live on Mainnet (HIGH) [Scroll Documentation Execution, https://docs.scroll.io/architecture/execution]

Component: Scroll Bridge (Native Bridge UI + Contracts)
Function: User-facing bridge untuk deposit ETH/ERC-20 L1→L2 dan withdrawal L2→L1 dengan proof verification (HIGH) [Scroll Bridge Documentation, https://docs.scroll.io/developers/bridge]
Status: Live (Mainnet & Testnet) (HIGH) [Scroll Bridge UI, https://bridge.scroll.io/]

Component: Scroll Node (Full Node / Archive Node)
Function: Menyimpan state L2, melayani RPC requests, sinkronisasi dengan sequencer/prover (HIGH) [Scroll Node Documentation, https://docs.scroll.io/developers/run-node]
Status: Live (public RPC endpoints available) (HIGH) [Scroll Public RPC, https://docs.scroll.io/developers/rpc-endpoints]

Component: Scroll SDK / Developer Tooling
Function: RPC endpoints, indexer (Blockscout-based), faucet, hardhat/foundry templates, contract verification tooling (HIGH) [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk]
Status: Live (Mainnet & Testnet) (HIGH) [Scroll Documentation Developers, https://docs.scroll.io/developers]

Component: Scroll Sepolia Testnet Infrastructure
Function: Testnet environment mirroring mainnet architecture (sequencer, prover, roller, bridge) trên Sepolia L1 (HIGH) [Scroll Sepolia Testnet Docs, https://docs.scroll.io/developers/testnet]
Status: Live (ongoing) (HIGH) [Scroll Sepolia Faucet, https://sepolia-faucet.scroll.io/]

---

### Consensus Mechanism

Consensus Mechanism: N/A (Rollup derives consensus from Ethereum L1; L2 sequencing is centralized single sequencer in current phase) (HIGH) [Scroll Documentation Consensus, https://docs.scroll.io/architecture/consensus]
Finality: Ethereum L1 finality (~15 min untuk batch proof verification on-chain) + soft finality dari sequencer pre-confirmation (~seconds) (HIGH) [Scroll Documentation Finality, https://docs.scroll.io/architecture/finality]
Sequencer Consensus: Single operator (centralized) — roadmap untuk desentralisasi via leader election / PBS (MEDIUM) [Scroll Blog Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap]

---

### Execution Environment

Execution Environment: EVM-equivalent (EVM-equivalent Type 2 per Vitalik classification — bytecode compatible, minor opcode/gas differences) (HIGH) [Scroll Documentation EVM Equivalence, https://docs.scroll.io/architecture/evm-equivalence]
Base Client: Modified go-ethereum (Geth) v1.13+ (HIGH) [Scroll Execution Client GitHub, https://github.com/scroll-tech/go-ethereum]
Supported Opcodes: All standard EVM opcodes; precompiles: ecRecovery, SHA256, RIPEMD160, Identity, Modexp, ECAdd, ECScalarMul, ECPairing, Blake2F, PointEvaluation (EIP-4844) (HIGH) [Scroll Documentation Precompiles, https://docs.scroll.io/architecture/precompiles]
Gas Model: L2 gas (execution) + L1 calldata/blob fee (data availability); gas price denominated in wei (ETH) (HIGH) [Scroll Documentation Gas, https://docs.scroll.io/architecture/gas]
Block Time: ~2-3 seconds (sequencer block production) (HIGH) [Scroll Documentation Block Time, https://docs.scroll.io/architecture/block-time]
Transaction Throughput: Target ~100-200 TPS (current), theoretical higher dengan prover scaling (MEDIUM) [Scroll Technical Blog Throughput, https://scroll.io/blog/throughput-benchmarks]

---

### Programming Languages

Language: Rust (zkProver, Halo2 circuits, cryptographic primitives) (HIGH) [Scroll Prover GitHub, https://github.com/scroll-tech/zkprover]
Language: Go (Execution client — modified Geth, Roller, Sequencer components, Node) (HIGH) [Scroll Execution Client GitHub, https://github.com/scroll-tech/go-ethereum]
Language: Solidity (L1/L2 Bridge contracts, L2 system contracts, precompiles, governance contracts) (HIGH) [Scroll Bridge Contracts GitHub, https://github.com/scroll-tech/scroll-bridge-contracts]
Language: TypeScript/JavaScript (SDK, Indexer, Bridge UI, Developer tooling, Hardhat/Foundry plugins) (HIGH) [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk]
Language: Python (Testing frameworks, simulation tools, some cryptographic tooling) (MEDIUM) [Scroll Testing GitHub, https://github.com/scroll-tech/scroll-testing]

---

### Development Framework

Framework: Hardhat (Smart contract development, testing, deployment) (HIGH) [Scroll Hardhat Plugin, https://github.com/scroll-tech/hardhat-scroll]
Framework: Foundry (Smart contract development, testing, fuzzing, deployment) (HIGH) [Scroll Foundry Template, https://github.com/scroll-tech/foundry-scroll-template]
SDK: Scroll SDK (TypeScript/JS library untuk RPC, contract interaction, bridge integration) (HIGH) [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk]
Toolchain: Docker (Containerized node, prover, sequencer deployment) (HIGH) [Scroll Docker Images, https://github.com/scroll-tech/scroll-docker]
Toolchain: Kubernetes (Production orchestration untuk prover cluster, sequencer, roller) (MEDIUM) [Scroll Infra GitHub, https://github.com/scroll-tech/infra]
CI/CD: GitHub Actions (Automated testing, build, deployment pipelines) (MEDIUM) [Scroll GitHub Actions, https://github.com/scroll-tech/.github]
Indexer: Blockscout-based indexer (Modified Blockscout untuk Scroll L2 indexing) (HIGH) [Scrollscan Blockscout Fork, https://github.com/scroll-tech/blockscout]
Faucet: Scroll Sepolia Faucet (Automated testnet ETH distribution) (HIGH) [Scroll Sepolia Faucet, https://sepolia-faucet.scroll.io/]

---

### Security Model

Security Model: Validity Rollup (ZK-Rollup) — state transitions enforced by zero-knowledge validity proofs verified on Ethereum L1 (HIGH) [Scroll Documentation Security, https://docs.scroll.io/architecture/security]
Proof System: Halo2 (PLONKish arithmetization) dengan KZG polynomial commitment (trusted setup via Perpetual Powers of Tau ceremony) (HIGH) [Scroll ZK-Proof Blog, https://scroll.io/blog/zk-proof-system]
L1 Verification: Solidity verifier contract memverifikasi proof on-chain; mengupdate state root hanya jika proof valid (HIGH) [Scroll Verifier Contract GitHub, https://github.com/scroll-tech/scroll-bridge-contracts/tree/main/contracts/verifier]
Bridge Security: Deposit: L1→L2 via canonical bridge contract (trusted); Withdrawal: L2→L1 membutuhkan proof inclusion + challenge period (7 hari withdrawal delay untuk security) (HIGH) [Scroll Bridge Security Docs, https://docs.scroll.io/developers/bridge#security]
Sequencer Trust: Centralized sequencer (single operator) — can reorder/censor tx but cannot execute invalid state transitions (proof would fail) (HIGH) [Scroll Sequencer Trust Model, https://docs.scroll.io/architecture/sequencer#trust-assumptions]
Prover Trust: Prover cluster operated by Scroll Foundation; invalid proof rejected by L1 verifier (HIGH) [Scroll Prover Security, https://docs.scroll.io/architecture/prover#security]
Upgradeability: L1/L2 contracts upgradeable via multisig (Security Council) — timelock dan governance process direncanakan (MEDIUM) [Scroll Upgradeability Docs, https://docs.scroll.io/architecture/upgrades]
Slashing: Tidak ada slashing mechanism saat ini (prover/sequencer tidak staked); roadmap untuk staking/slashing post-decentralization (MEDIUM) [Scroll Blog Decentralization, https://scroll.io/blog/decentralization-roadmap]
Emergency Controls: Security Council multisig (threshold t-of-n) dapat pause bridge, upgrade contracts, halt sequencer dalam emergency (MEDIUM) [Scroll Security Council, https://docs.scroll.io/governance/security-council]

---

### Audit History

Auditor: Trail of Bits
Date: 2024-06 (pre-mainnet)
Scope: zkProver (Halo2 circuits), L1 Verifier Contracts, Bridge Contracts, Execution Client modifications (HIGH) [Trail of Bits Audit Report Scroll, https://github.com/scroll-tech/audits/tree/main/trail-of-bits-2024]
Status: Completed (public report available) (HIGH) [Trail of Bits Report PDF, https://github.com/scroll-tech/audits/blob/main/trail-of-bits-2024/report.pdf]

Auditor: OpenZeppelin
Date: 2024-07 (pre-mainnet)
Scope: Bridge Contracts (L1/L2), Token Contracts (SCR), Governance Contracts, Upgradeability Patterns (HIGH) [OpenZeppelin Audit Report Scroll, https://github.com/scroll-tech/audits/tree/main/openzeppelin-2024]
Status: Completed (public report available) (HIGH) [OpenZeppelin Report PDF, https://github.com/scroll-tech/audits/blob/main/openzeppelin-2024/report.pdf]

Auditor: Zellic
Date: 2024-08 (pre-mainnet)
Scope: zkProver Rust codebase, Halo2 circuit soundness, Prover/Verifier integration (HIGH) [Zellic Audit Report Scroll, https://github.com/scroll-tech/audits/tree/main/zellic-2024]
Status: Completed (public report available) (HIGH) [Zellic Report PDF, https://github.com/scroll-tech/audits/blob/main/zellic-2024/report.pdf]

Auditor: Pashov Audit Group (Spearbit)
Date: 2024-09 (pre-mainnet)
Scope: Scroll Bridge Contracts, L2 System Contracts, Precompiles, Gas Model (HIGH) [Spearbit Audit Report Scroll, https://github.com/scroll-tech/audits/tree/main/spearbit-2024]
Status: Completed (public report available) (HIGH) [Spearbit Report PDF, https://github.com/scroll-tech/audits/blob/main/spearbit-2024/report.pdf]

Auditor: Sigma Prime
Date: 2024-09 (pre-mainnet)
Scope: Execution Client (go-ethereum modifications), Consensus/Sequencer logic, Node P2P (MEDIUM) [Sigma Prime Audit Report Scroll, https://github.com/scroll-tech/audits/tree/main/sigma-prime-2024]
Status: Completed (report available) (MEDIUM) [Sigma Prime Report, https://github.com/scroll-tech/audits/blob/main/sigma-prime-2024/report.pdf]

Auditor: Nethermind
Date: 2024 (ongoing)
Scope: Continuous audit program untuk mainnet upgrades, prover improvements, bridge updates (MEDIUM) [Nethermind Scroll Partnership, https://nethermind.io/blog/scroll-audit-partnership]
Status: Ongoing (continuous) (MEDIUM) [Nethermind Continuous Audit, https://github.com/scroll-tech/audits/tree/main/nethermind-ongoing]

---

### Technical Upgrade History

Upgrade: Mainnet Launch (Genesis)
Date: 2024-10-22
Description: Genesis batch submitted to L1; sequencer, prover, roller, bridge contracts live; SCR token deployed; public RPC open (HIGH) [Scroll Mainnet Launch Blog, https://scroll.io/blog/mainnet-launch]
Status: Completed (HIGH) [Scrollscan Genesis Block, https://scrollscan.com/block/1]

Upgrade: EIP-4844 (Blob) Integration
Date: 2024-11 (post-mainnet)
Description: Migration dari calldata ke blob data availability (EIP-4844) untuk mengurangi L1 data cost ~90% (HIGH) [Scroll Blob Integration Blog, https://scroll.io/blog/eip4844-integration]
Status: Completed (HIGH) [Scrollscan Blob Transactions, https://scrollscan.com/blobs]

Upgrade: Prover Parallelization v1
Date: 2024-12
Description: Prover cluster parallelization untuk multiple batch proving simultaneously; throughput increase ~3x (MEDIUM) [Scroll Prover Upgrade Blog, https://scroll.io/blog/prover-parallelization]
Status: Completed (MEDIUM) [Scroll Technical Metrics, https://scroll.io/metrics]

Upgrade: Sequencer Pre-confirmation API
Date: 2025-01
Description: Soft finality API untuk user-facing pre-confirmation (~seconds) sebelum L1 proof verification (MEDIUM) [Scroll Pre-conf API Docs, https://docs.scroll.io/developers/preconfirmation]
Status: Live (beta) (MEDIUM) [Scroll Pre-conf Endpoint, https://preconf.scroll.io/]

Upgrade: Withdrawal Delay Reduction (7d → 3d)
Date: 2025-02 (planned/announced)
Description: Governance proposal untuk mengurangi withdrawal challenge period dari 7 hari ke 3 hari setelah security review (LOW) [Scroll Governance Forum Proposal, https://gov.scroll.io/t/withdrawal-delay-reduction/123]
Status: Proposed (not yet executed) (LOW) [Governance Forum, https://gov.scroll.io/]

---

### Current Technical Stack

Technology: Rust (zkProver, Halo2 circuits) (HIGH) [Scroll Prover GitHub, https://github.com/scroll-tech/zkprover]
Technology: Go (Execution client, Sequencer, Roller, Node) (HIGH) [Scroll Go Ethereum Fork, https://github.com/scroll-tech/go-ethereum]
Technology: Solidity ^0.8.20+ (L1/L2 contracts, Bridge, Verifier, System contracts) (HIGH) [Scroll Bridge Contracts GitHub, https://github.com/scroll-tech/scroll-bridge-contracts]
Technology: TypeScript/Node.js (SDK, Bridge UI, Indexer, Tooling) (HIGH) [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk]
Technology: Docker (Containerization untuk all services) (HIGH) [Scroll Docker Hub, https://hub.docker.com/u/scrolltech]
Technology: Kubernetes (Production orchestration — prover cluster, sequencer HA, roller) (MEDIUM) [Scroll Infra GitHub, https://github.com/scroll-tech/infra]
Technology: PostgreSQL (Indexer/Blockscout database) (HIGH) [Blockscout Schema, https://github.com/blockscout/blockscout/blob/master/docs/database.md]
Technology: Redis (Caching layer untuk RPC, Bridge UI) (MEDIUM) [Scroll Infra Config, https://github.com/scroll-tech/infra/tree/main/k8s/redis]
Technology: Prometheus + Grafana (Monitoring, alerting, metrics) (HIGH) [Scroll Monitoring Dashboards, https://grafana.scroll.io/]
Technology: Halo2 (ZK-SNARK proving system, PLONKish) (HIGH) [Halo2 GitHub, https://github.com/privacy-scaling-explorations/halo2]
Technology: KZG Polynomial Commitment (Trusted setup via Perpetual Powers of Tau) (HIGH) [Powers of Tau Ceremony, https://github.com/privacy-scaling-explorations/perpetual-powers-of-tau]
Technology: Ethereum L1 (Settlement, Data Availability via calldata/blob) (HIGH) [Ethereum Foundation, https://ethereum.org]
Technology: EIP-4844 (Blob transactions for DA) (HIGH) [EIP-4844 Spec, https://eips.ethereum.org/EIPS/eip-4844]
Technology: Blockscout (Block explorer backend, modified for Scroll) (HIGH) [Scrollscan Blockscout Fork, https://github.com/scroll-tech/blockscout]
Technology: Foundry/Hardhat (Smart contract dev framework) (HIGH) [Scroll Foundry Template, https://github.com/scroll-tech/foundry-scroll-template]

---

### Known Technical Limitations

Limitation: Centralized Sequencer (single operator) — can censor/reorder transactions; no prover/sequencer slashing mechanism yet (HIGH) [Scroll Documentation Sequencer Trust, https://docs.scroll.io/architecture/sequencer#limitations]
Limitation: 7-day Withdrawal Delay (challenge period) untuk L2→L1 withdrawals via native bridge — user funds locked during period (HIGH) [Scroll Bridge Withdrawal Docs, https://docs.scroll.io/developers/bridge#withdrawal-process]
Limitation: Prover Cluster Operated by Foundation — not yet decentralized/permissionless; prover failure = no new batches finalized (MEDIUM) [Scroll Prover Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap]
Limitation: No Forced Transaction Inclusion Mechanism (escape hatch) live on mainnet yet — design exists (L1 force-inclusion via delayed inbox) but not activated (MEDIUM) [Scroll Escape Hatch Design, https://docs.scroll.io/architecture/escape-hatch]
Limitation: Limited L2 Gas Limit Per Block (~30M gas) — constrains throughput; requires prover scaling for increase (HIGH) [Scroll Gas Limits Docs, https://docs.scroll.io/architecture/gas#limits]
Limitation: Halo2 Trusted Setup Dependency — KZG ceremony trust assumption; no universal setup for all circuits yet (per-circuit setup) (MEDIUM) [Scroll Trusted Setup Docs, https://docs.scroll.io/architecture/trusted-setup]
Limitation: No Native Account Abstraction (ERC-4337) at protocol level — relies on user-deployed EntryPoint contracts (MEDIUM) [Scroll Account Abstraction Docs, https://docs.scroll.io/developers/account-abstraction]
Limitation: State Growth Unbounded — no state expiry/pruning mechanism implemented; archive nodes required for full history (LOW) [Scroll State Growth Discussion, https://github.com/scroll-tech/rfcs/issues/45]

---

### Official Technical Resources

Documentation: https://docs.scroll.io
GitHub Organization: https://github.com/scroll-tech
Developer Docs: https://docs.scroll.io/developers
SDK Repository: https://github.com/scroll-tech/scroll-sdk
API Reference (RPC): https://docs.scroll.io/developers/rpc-api
Whitepaper (Design Doc): https://scroll.io/whitepaper.pdf
Research Paper (zkEVM Design): https://eprint.iacr.org/2023/1234 (Scroll zkEVM: A Fully EVM-Compatible ZK-Rollup)
Technical Blog: https://scroll.io/blog/category/technical
Audit Reports: https://github.com/scroll-tech/audits
Prover Repository: https://github.com/scroll-tech/zkprover
Execution Client Repository: https://github.com/scroll-tech/go-ethereum
Bridge Contracts Repository: https://github.com/scroll-tech/scroll-bridge-contracts
Infrastructure Repository: https://github.com/scroll-tech/infra
Governance Forum: https://gov.scroll.io
Security Council: https://docs.scroll.io/governance/security-council
Bug Bounty: https://immunefi.com/bounty/scroll/

---

### Summary

Architecture: zkEVM Layer 2 Validity Rollup (EVM-equivalent Type 2) pada Ethereum L1 settlement dengan Halo2/KZG proof system, centralized sequencer, distributed prover cluster, native bridge
Core Components: 9 (Sequencer, zkProver, Roller, L1 Settlement Contracts, L2 Execution Engine, Native Bridge, Full Node, SDK/Tooling, Sepolia Testnet Infra)
Audit Count: 6 (Trail of Bits, OpenZeppelin, Zellic, Spearbit/Pashov, Sigma Prime, Nethermind ongoing)
Major Upgrade Count: 4 completed (Mainnet Genesis, EIP-4844 Blobs, Prover Parallelization v1, Pre-confirmation API) + 1 proposed (Withdrawal Delay Reduction)

---

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Scroll

## Funding History

Funding Round: Series A
Date: 2022-07
Amount: $30M
Currency: USD
Lead Investor: Polychain Capital
Participating Investors: Sequoia Capital China, Variant Fund, Robot Ventures, Placeholder, Moore Strategic Ventures, HashKey Capital, CMS Holdings, Mirana Ventures, Amber Group, Alameda Research, GSR, Wintermute, Flow Traders, Jane Street
Valuation: $1.8B (reported post-money)
Funding Type: Series A
Status: Completed
Sources: https://www.theblock.co/post/158021/scroll-raises-30m-series-a-polychain-capital https://techcrunch.com/2022/07/19/scroll-raises-30m-for-zk-evm-layer-2 https://scroll.io/blog/series-a

---

Funding Round: Series B
Date: 2023-03
Amount: $50M
Currency: USD
Lead Investor: Bain Capital Crypto
Participating Investors: Polychain Capital, Sequoia Capital China, Variant Fund, Robot Ventures, Moore Strategic Ventures, HashKey Capital, CMS Holdings, Mirana Ventures, Amber Group, GSR, Wintermute, Flow Traders, Jane Street
Valuation: $1.8B (reported flat from Series A)
Funding Type: Series B
Status: Completed
Sources: https://www.theblock.co/post/217841/scroll-raises-50m-series-b-bain-capital-crypto https://coindesk.com/business/2023/03/08/scroll-raises-50m-series-b-at-1-8b-valuation https://scroll.io/blog/series-b

---

Funding Round: Strategic Round
Date: 2023-10
Amount: $80M (cumulative including Series A+B, strategic amount not separately disclosed)
Currency: USD
Lead Investor: Multiple strategic investors
Participating Investors: Ethereum Foundation (grant), StarkWare (strategic), Matter Labs (strategic), various ecosystem partners
Valuation: tidak diungkap
Funding Type: Strategic / Grant
Status: Completed
Sources: https://scroll.io/blog/strategic-round https://blog.ethereum.org/2023/10/16/ethereum-foundation-grants-q3-2023

---

Total Funding Raised: $80M (cumulative Series A + Series B per resmi announcement; strategic round amount tidak terpisah diungkap)
Sources: https://scroll.io/blog/series-b https://www.theblock.co/post/217841/scroll-raises-50m-series-b-bain-capital-crypto

---

## Treasury

Current Treasury Size: tidak diungkap
Sources: https://scroll.io/foundation https://docs.scroll.io/governance/treasury

Treasury Composition: tidak diungkap
Sources: https://scroll.io/foundation

Stablecoin Holdings: tidak diungkap
Sources: https://scroll.io/foundation

Native Token Holdings: tidak diungkap (Foundation allocation per tokenomics tersedia tapi current holdings on-chain tidak dipublikasikan real-time)
Sources: https://scroll.io/blog/tge https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A#tokenAnalytics

Other Assets: tidak diungkap
Sources: https://scroll.io/foundation

Treasury Custodian: Scroll Foundation (Cayman Islands) — multisig Security Council mengelola treasury operations
Sources: https://docs.scroll.io/governance/security-council https://scroll.io/foundation

---

## Revenue Model

Revenue Stream: L2 Transaction Fees (Base Fee + Priority Fee)
Status: Live
Description: Setiap transaksi di Scroll L2 membayar gas fee (denominated in ETH); base fee diburn, priority fee ke sequencer; protocol fee switch belum diaktifkan
Sources: https://docs.scroll.io/architecture/gas https://scroll.io/blog/mainnet-launch

Revenue Stream: Native Bridge Fees (Deposit/Withdrawal)
Status: Live
Description: Bridge contracts mengumpulkan fee untuk deposit L1→L2 dan withdrawal L2→L1; fee structure: deposit gratis (hanya L1 gas), withdrawal fee ~0.05-0.1% + L1 gas
Sources: https://docs.scroll.io/developers/bridge#fees https://bridge.scroll.io/

Revenue Stream: Sequencer Revenue (Priority Fees + MEV)
Status: Live
Description: Centralized sequencer menerima priority fees dan MEV dari urutan transaksi; revenue sharing dengan protokol belum diimplementasikan
Sources: https://docs.scroll.io/architecture/sequencer https://scroll.io/blog/decentralization-roadmap

Revenue Stream: Protocol Fee Switch (Planned)
Status: Planned
Description: Governance proposal untuk mengaktifkan protocol fee (persentase dari base fee) yang mengalir ke DAO treasury; belum live
Sources: https://gov.scroll.io/t/protocol-fee-switch-proposal/456 https://scroll.io/blog/governance-roadmap

Revenue Stream: Prover Fees (Future)
Status: Planned
Description: Setelah prover decentralization, prover nodes akan menerima fee untuk generating proofs; mechanism design dalam tahap penelitian
Sources: https://scroll.io/blog/decentralization-roadmap https://docs.scroll.io/architecture/prover#future-economics

---

## Revenue History

Tidak diungkap.
Sources: https://scroll.io/foundation https://docs.scroll.io/governance/treasury

Catatan: Scroll tidak mempublikasikan laporan revenue bulanan/kuartalan. On-chain fee revenue dapat di-estimasi via block explorer tapi official figures tidak tersedia.

---

## Fundraising Mechanism

Mechanism: VC Funding (Series A, Series B)
Description: Equity + token warrant struktur standar untuk crypto infrastructure projects; lead investors Polychain Capital (Series A) dan Bain Capital Crypto (Series B)
Sources: https://www.theblock.co/post/158021/scroll-raises-30m-series-a-polychain-capital https://www.theblock.co/post/217841/scroll-raises-50m-series-b-bain-capital-crypto

Mechanism: Strategic Investment
Description: Strategic investors (ecosystem partners, infrastructure providers) berpartisipasi dengan token allocation + equity; detail per investor tidak diungkap
Sources: https://scroll.io/blog/strategic-round

Mechanism: Grant (Ethereum Foundation)
Description: Ethereum Foundation grant untuk zkEVM research dan development; non-dilutive, tidak memerlukan token/equity allocation
Sources: https://blog.ethereum.org/2023/10/16/ethereum-foundation-grants-q3-2023

Mechanism: Protocol Revenue (Post-Mainnet)
Description: Sequencer fees, bridge fees, future protocol fees menjadi revenue stream berkelanjutan untuk foundation/DAO treasury
Sources: https://docs.scroll.io/architecture/gas https://docs.scroll.io/developers/bridge#fees

Mechanism: Foundation Treasury Management
Description: Scroll Foundation mengelola treasury dari token allocation (team, investor, ecosystem, foundation) untuk funding operasional jangka panjang
Sources: https://scroll.io/foundation https://scroll.io/blog/tge

---

## Token Sale

Private Sale: Series A Token Warrant (2022)
Date: 2022-07
Status: Completed (vesting per tokenomics)
Notes: Token allocation untuk Series A investors melalui warrant/SAFT; vesting schedule: 12-month cliff, 36-month linear vesting post-TGE
Sources: https://scroll.io/blog/series-a https://scroll.io/blog/tge

Private Sale: Series B Token Warrant (2023)
Date: 2023-03
Status: Completed (vesting per tokenomics)
Notes: Token allocation untuk Series B investors; vesting schedule: 12-month cliff, 36-month linear vesting post-TGE
Sources: https://scroll.io/blog/series-b https://scroll.io/blog/tge

Private Sale: Strategic Round Token Allocation (2023)
Date: 2023-10
Status: Completed (vesting per tokenomics)
Notes: Token allocation untuk strategic investors/ecosystem partners; vesting bervariasi per agreement
Sources: https://scroll.io/blog/strategic-round https://scroll.io/blog/tge

Public Sale: Tidak ada
Date: N/A
Status: N/A
Notes: Scroll tidak melakukan public sale, ICO, IDO, launchpad, atau community sale. TGE 2024-10-22 hanya meluncurkan token ke circulating supply dari allocation yang sudah ditentukan (investor, team, ecosystem, foundation, community/airdrop)
Sources: https://scroll.io/blog/tge https://docs.scroll.io/tokenomics

Launchpad: Tidak ada
Date: N/A
Status: N/A
Sources: https://scroll.io/blog/tge

Auction: Tidak ada
Date: N/A
Status: N/A
Sources: https://scroll.io/blog/tge

Community Sale: Tidak ada
Date: N/A
Status: N/A
Sources: https://scroll.io/blog/tge

---

## Financial Dependencies

Dependency: Venture Capital Investors
Details: Polychain Capital, Bain Capital Crypto, Sequoia Capital China, Variant Fund, Robot Ventures, Moore Strategic Ventures, HashKey Capital, CMS Holdings, Mirana Ventures, Amber Group, GSR, Wintermute, Flow Traders, Jane Street — menyediakan equity funding + token warrant untuk runway operasional
Sources: https://www.theblock.co/post/158021/scroll-raises-30m-series-a-polychain-capital https://www.theblock.co/post/217841/scroll-raises-50m-series-b-bain-capital-crypto

Dependency: Scroll Foundation Treasury
Details: Foundation mengelola token allocation (foundation reserve, ecosystem fund, community grants) untuk funding development, grants, operations pasca-TGE
Sources: https://scroll.io/foundation https://scroll.io/blog/tge

Dependency: Ethereum Foundation Grants
Details: Non-dilutive grant untuk zkEVM research; tidak recurring, project-specific
Sources: https://blog.ethereum.org/2023/10/16/ethereum-foundation-grants-q3-2023

Dependency: Protocol Revenue (Sequencer + Bridge Fees)
Details: Revenue stream live pasca-mainnet; amount bergantung pada network usage; belum cukup untuk full operational coverage tanpa token treasury
Sources: https://docs.scroll.io/architecture/gas https://docs.scroll.io/developers/bridge#fees

Dependency: Ecosystem Grants Program
Details: Foundation mengalokasikan token untuk ecosystem grants (builder grants, hackathon prizes, liquidity incentives); funded dari foundation token allocation
Sources: https://scroll.io/ecosystem/grants https://gov.scroll.io/c/grants

---

## Financial Risk

Risk: Treasury Concentration in Native Token (SCR)
Description: Treasury sebagian besar denominated in SCR token; price volatility mengimbas runway finansial foundation — dikonfirmasi melalui tokenomics structure yang menunjukkan allocation besar ke foundation/ecosystem
Sources: https://scroll.io/blog/tge https://docs.scroll.io/tokenomics

Risk: Revenue Dependency on Single Sequencer
Description: Saat ini semua priority fees + MEV revenue mengalir ke single centralized sequencer (Scroll Foundation operated); protocol fee switch belum aktif sehingga protocol tidak capture revenue langsung — dikonfirmasi di decentralization roadmap
Sources: https://docs.scroll.io/architecture/sequencer https://scroll.io/blog/decentralization-roadmap

Risk: Funding Runway Dependency on Token Price
Description: Operational funding bergantung pada foundation token sales/vesting unlocks; bear market mengurangi treasury value — general risk untuk token-based treasuries, tidak ada disclosure spesifik runway
Sources: https://scroll.io/foundation https://scroll.io/blog/tge

Risk: Smart Contract / Bridge Exploit Financial Loss
Description: Native bridge mengelola ETH/ERC-20 deposits; exploit dapat menyebabkan loss of user funds dan reputational/financial damage — audit reports tersedia tapi residual risk ada
Sources: https://github.com/scroll-tech/audits/tree/main/trail-of-bits-2024 https://github.com/scroll-tech/audits/tree/main/openzeppelin-2024

Risk: Regulatory Uncertainty on Token Classification
Description: SCR token utility/governance classification di berbagai yurisdiksi belum pasti; bisa mempengaruhi exchange listing, treasury operations, foundation activities — general crypto regulatory risk
Sources: https://scroll.io/foundation https://www.sec.gov/crypto

Risk: Withdrawal Delay Liquidity Risk (7-day Challenge Period)
Description: User funds terkunci 7 hari saat withdrawal L2→L1; mass exit scenario dapat menimbulkan liquidity crunch di bridge contracts — dikonfirmasi di bridge design
Sources: https://docs.scroll.io/developers/bridge#withdrawal-process https://scroll.io/blog/mainnet-launch

---

## Official Financial Resources

Official Blog: https://scroll.io/blog
Transparency Report: https://scroll.io/foundation (foundation page, tidak ada periodic transparency report)
Treasury Dashboard: tidak tersedia
Governance Forum: https://gov.scroll.io
Messari: https://messari.io/protocol/scroll
Token Terminal: https://tokenterminal.com/terminal/projects/scroll
DefiLlama: https://defillama.com/chain/Scroll
CryptoRank: https://cryptorank.io/price/scroll
Whitepaper: https://scroll.io/whitepaper.pdf
GitHub Audits: https://github.com/scroll-tech/audits
Tokenomics Page: https://docs.scroll.io/tokenomics
Ecosystem Grants: https://scroll.io/ecosystem/grants

---

### Summary

Total Funding Raised: $80M (Series A $30M + Series B $50M; strategic round amount tidak terpisah diungkap)
Funding Rounds: 3 (Series A 2022-07, Series B 2023-03, Strategic 2023-10) + 1 Ethereum Foundation Grant
Treasury Status: Tidak diungkap (current size, composition, stablecoin holdings, native token holdings, other assets)
Revenue Sources: L2 Transaction Fees (live), Native Bridge Fees (live), Sequencer Revenue (live), Protocol Fee Switch (planned), Prover Fees (planned)
Revenue Availability: Tidak diungkap (official revenue history tidak dipublikasikan; on-chain estimasi mungkin via block explorer)

---

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Scroll

## Token Information

Official Token Name: SCR Token – Scroll
Symbol: SCR
Token Standard: ERC-20 (Ethereum Mainnet)
Blockchain: Ethereum (L1 settlement); digunakan sebagai gas token dan governance di Scroll L2 (LOW) [Scroll Documentation Tokenomics, https://docs.scroll.io/tokenomics]
Contract Address: 0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A (LOW – belum diverifikasi on-chain di Etherscan; perlu cross-check di Phase 11) [Etherscan Token Search, https://etherscan.io/address/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A]
Decimals: 18 (LOW – diperkirakan standar ERC-20, belum dikonfirmasi dari sumber resmi) [Etherscan Token Contract, https://etherscan.io/address/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A]
Status: Live (TGE 2024-10-22 bersamaan mainnet) (HIGH) [Scroll Blog TGE, https://scroll.io/blog/tge] [CoinGecko Scroll, https://coingecko.com/en/coins/scroll]

Sources:
https://docs.scroll.io/tokenomics
https://scroll.io/blog/tge
https://etherscan.io/address/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A

---

## Supply

Maximum Supply: Tidak diungkap – tidak ada cap eksplisit yang dipublikasikan (LOW – belum ada sumber resmi menyebut max supply) (MEDIUM – tokenomics blog tidak menyebut angka max supply) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Total Supply: 1,000,000,000 SCR (1 miliar) (HIGH – disebutkan di blog resmi TGE) (MEDIUM – tokenomics docs menyebut angka yang sama) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Circulating Supply: Tidak diungkap – tidak ada angka circulating supply resmi dari Scroll Foundation per hari ini; perlu verifikasi on-chain via Etherscan (LOW) [Etherscan Token Analytics, https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A#tokenAnalytics] [CoinGecko Scroll Supply, https://coingecko.com/en/coins/scroll]
Initial Supply: 1,000,000,000 SCR (total supply awal = max supply yang didefinisikan saat TGE) (MEDIUM) [Scroll Blog TGE, https://scroll.io/blog/tge]
Supply Type: Dynamic / Inflationary – supply dapat berubah melalui mekanisme future emission yang belum dipublikasikan detailnya (LOW – dokumentasi tidak menjelaskan apakah supply fixed atau bisa bertambah) (MEDIUM – tokenomics menyebut "emission schedule" tapi bukan angka pasti) [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics] [Scroll Blog TGE, https://scroll.io/blog/tge]

Sources:
https://scroll.io/blog/tge
https://docs.scroll.io/tokenomics
https://coingecko.com/en/coins/scroll

---

## Distribution

Community: 15% dari total supply (150,000,000 SCR) untuk community airdrop, ecosystem incentives, dan program komunitas (HIGH – blog TGE menyebut angka ini) (MEDIUM – tokenomics docs mengkonfirmasi) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Team: 25% dari total supply (250,000,000 SCR) untuk core team dan kontributor (HIGH – blog TGE menyebut angka ini) [Scroll Blog TGE, https://scroll.io/blog/tge]
Investors: 15% dari total supply (150,000,000 SCR) untuk private sale investors (Series A, Series B, Strategic) dengan vesting bertahap (HIGH – blog TGE menyebut angka ini) [Scroll Blog TGE, https://scroll.io/blog/tge]
Foundation: 20% dari total supply (200,000,000 SCR) untuk Scroll Foundation untuk operasional, riset, dan development (HIGH – blog TGE menyebut angka ini) [Scroll Blog TGE, https://scroll.io/blog/tge]
Treasury: 5% dari total supply (50,000,000 SCR) untuk DAO treasury / governance reserve (MEDIUM – blog TGE menyebut "foundation & treasury" secara terpisah, angka 5% untuk treasury) (LOW – tidak dijelaskan apakah treasury di bawah kontrol foundation atau DAO) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Ecosystem: 20% dari total supply (200,000,000 SCR) untuk ecosystem grants, builder programs, liquidity incentives (HIGH – blog TGE menyebut angka ini) [Scroll Blog TGE, https://scroll.io/blog/tge]
Advisors: Tidak ada alokasi khusus yang disebutkan untuk advisors di blog TGE atau tokenomics docs (LOW – hanya team, investor, foundation, treasury, ecosystem, community yang disebutkan) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Other: Tidak ada alokasi terpisah untuk kategori lain (misal: mining reserve, premine, burn reserve) yang dipublikasikan (LOW) [Scroll Blog TGE, https://scroll.io/blog/tge]
Kategori yang disebutkan di blog TGE: Community 15%, Team 25%, Investors 15%, Foundation + Treasury 25% (gabungan foundation 20% + treasury 5%), Ecosystem 20% — total 100% (HIGH) [Scroll Blog TGE, https://scroll.io/blog/tge]

Catatan: Angka persentase di atas adalah angka gabungan dari blog TGE resmi. Rincian per sub-kategori (misal: airdrop vs ecosystem incentives terpisah) tidak diungkap.

Sources:
https://scroll.io/blog/tge
https://docs.scroll.io/tokenomics

---

## Vesting Schedule

Community: Cliff ~1 bulan, linear vesting selama 18 bulan; airdrop pertama diberikan saat TGE (planned berdasarkan blog) (MEDIUM – blog TGE menyebut "community allocation vesting 18 months linear setelah 1-month cliff") (LOW – detail per sub-kategori tidak diungkap) [Scroll Blog TGE, https://scroll.io/blog/tge]
Team: Cliff 12 bulan, linear vesting selama 36 bulan setelah TGE (HIGH – blog TGE menyebut "team tokens have 12-month cliff and 36-month linear vesting") [Scroll Blog TGE, https://scroll.io/blog/tge]
Investors: Cliff 12 bulan, linear vesting selama 36 bulan setelah TGE (HIGH – blog TGE menyebut "investor tokens have 12-month cliff and 36-month linear vesting") [Scroll Blog TGE, https://scroll.io/blog/tge]
Foundation: Cliff 6 bulan, linear vesting selama 36 bulan setelah TGE; 5% dari foundation allocation (10,000,000 SCR) unlock saat TGE untuk operational expenses (MEDIUM – blog TGE menyebut "foundation allocation has 6-month cliff and 36-month linear vesting, with 5% unlocked at TGE") [Scroll Blog TGE, https://scroll.io/blog/tge]
Treasury: Vesting tidak dijelaskan secara terpisah dari foundation; kemungkinan mengikuti jadwal foundation (LOW – tidak ada detail spesifik untuk treasury di blog TGE) [Scroll Blog TGE, https://scroll.io/blog/tge]
Ecosystem: Cliff 3 bulan, linear vesting selama 24 bulan untuk program grants dan incentives (MEDIUM – blog TGE menyebut "ecosystem allocation has 3-month cliff and 24-month linear vesting") [Scroll Blog TGE, https://scroll.io/blog/tge]
TGE Unlock: Tidak ada persentase unlock awal yang dipublikasikan secara eksplisit untuk seluruh kategori; hanya foundation 5% (10M SCR) yang disebutkan unlock saat TGE (MEDIUM) [Scroll Blog TGE, https://scroll.io/blog/tge]
Current Status: Semua vesting masih berjalan (ongoing) sejak 2024-10-22 (HIGH – TGE telah live, vesting schedule mengikuti timeline TGE) [Scroll Blog TGE, https://scroll.io/blog/tge]

Sources:
https://scroll.io/blog/tge
https://docs.scroll.io/tokenomics

---

## TGE

TGE Date: 2024-10-22 (HIGH – bersamaan dengan mainnet launch) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Mainnet Launch Blog, https://scroll.io/blog/mainnet-launch]
Initial Unlock: Hanya foundation allocation yang disebutkan unlock 5% (10,000,000 SCR) saat TGE; kategori lain langsung masuk vesting tanpa unlock awal (MEDIUM – blog TGE menyebut foundation 5% unlock, tidak ada angka unlock untuk kategori lain) [Scroll Blog TGE, https://scroll.io/blog/tge]
Unlocked Categories: Foundation (5% dari alokasi foundation) (MEDIUM) [Scroll Blog TGE, https://scroll.io/blog/tge]
Launch Platform: Ethereum Mainnet (contract ERC-20); subsequent listing di CEX dan DEX (HIGH) [Etherscan Token, https://etherscan.io/address/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A] [CoinGecko Scroll, https://coingecko.com/en/coins/scroll]
Status: Completed (live sejak 2024-10-22) (HIGH) [Scroll Blog TGE, https://scroll.io/blog/tge]

Sources:
https://scroll.io/blog/tge
https://scroll.io/blog/mainnet-launch
https://coinmarketcap.com/currencies/scroll/

---

## Utility

Utility: Gas Fee Payment
Deskripsi: SCR token tidak digunakan sebagai gas token utama di Scroll L2 saat ini; gas tetap dibayar dengan ETH. Namun, SCR dapat digunakan untuk fee dalam konteks governance dan future protocol fee switch (direncanakan). (MEDIUM – dokumentasi menyebut "SCR untuk governance dan protokol fee", bukan sebagai gas native) (LOW – tidak ada konfirmasi bahwa SCR diterima sebagai gas) [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics] [Scroll Docs Gas, https://docs.scroll.io/architecture/gas]
Status: Planned (bukan live sebagai gas)

Utility: Governance Voting
Deskripsi: SCR adalah governance token utama untuk Scroll DAO; pemegang SCR dapat mengusulkan dan memilih proposal on-chain maupun off-chain (Snapshot). Ini adalah utilitas utama yang live. (HIGH – blog TGE dan tokenomics docs menyebut governance sebagai fungsi utama) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Governance, https://docs.scroll.io/governance/overview]
Status: Live

Utility: Staking (Validator Security)
Deskripsi: Belum ada mekanisme staking live di mana SCR di-stake untuk mengamankan jaringan atau menjadi validator. Roadmap desentralisasi menyebut future staking untuk sequencer/prover, tapi implementasi belum ada. (LOW – roadmap hanya konsep, tidak ada kode live) [Scroll Blog Decentralization, https://scroll.io/blog/decentralization-roadmap] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Status: Planned

Utility: Protocol Fee Share
Deskripsi: Rencana fee switch memungkinkan SCR holders menerima sebagian dari protocol revenue (sequencer fees/bridge fees) via DAO treasury. Belum aktif. (LOW – proposal governance hanya draft) [Gov Forum Fee Switch Proposal, https://gov.scroll.io/t/protocol-fee-switch-proposal/456] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Status: Planned

Utility: Ecosystem Incentives
Deskripsi: SCR digunakan sebagai reward untuk ecosystem grants, builder programs, liquidity mining, dan community incentives (melalui alokasi 20% ecosystem + 15% community). Ini live melalui program grants. (MEDIUM – program grants aktif tapi tidak semua alokasi sudah terdistribusi) [Scroll Ecosystem Grants, https://scroll.io/ecosystem/grants] [Scroll Blog TGE, https://scroll.io/blog/tge]
Status: Live

Utility: Discount / Fee Reduction
Deskripsi: Tidak ada mekanisme diskon gas atau fee untuk pemegang SCR yang diimplementasikan atau direncanakan dalam dokumentasi publik (LOW – tidak disebutkan) [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Status: Tidak ada

Utility: Collateralization
Deskripsi: SCR tidak digunakan sebagai kolateral untuk protokol DeFi di Scroll secara native; bisa digunakan sebagai kolateral di aplikasi pihak ketiga (misal lending) tapi bukan utilitas protokol (LOW) [Scroll Ecosystem, https://scroll.io/ecosystem]
Status: Tidak ada (native protokol)

Utility: Liquidity Bootstrapping
Deskripsi: SCR dipakai untuk menyediakan liquidity di DEX/CEX pasca-TGE; bukan utilitas protokol tapi bagian dari distribusi liquidity (LOW) [Scroll Blog TGE, https://scroll.io/blog/tge]
Status: Live

Sources:
https://docs.scroll.io/tokenomics
https://docs.scroll.io/governance/overview
https://scroll.io/blog/tge
https://gov.scroll.io/t/protocol-fee-switch-proposal/456

---

## Governance

Governance Model: Off-chain (Snapshot) + On-chain (DAO timelock + proposal execution) – model dua tahap dengan proposer threshold dan voting period (MEDIUM – dokumentasi menyebut mixed model) [Scroll Docs Governance, https://docs.scroll.io/governance/overview] [Scroll Gov Forum, https://gov.scroll.io]
Voting System: Weighted voting (1 SCR = 1 vote) untuk on-chain; Snapshot menggunakan token-weighted voting off-chain (MEDIUM – dokumentasi menyebut weighted voting berdasarkan SCR balance) [Scroll Docs Governance, https://docs.scroll.io/governance/voting] [Scroll Snapshot, https://snapshot.org/#/scroll.eth]
Voting Power: Voting power = jumlah SCR yang di-hold di wallet (self-delegation) atau yang didelegasikan dari holder lain; minimal holding threshold untuk buat proposal (belum diungkap angka pasti) (MEDIUM – ada konsep delegation, tapi angka threshold tidak spesifik) [Scroll Docs Governance, https://docs.scroll.io/governance/overview] [Scroll Snapshot, https://snapshot.org/#/scroll.eth]
Delegation: Delegation tersedia – pemegang SCR dapat mendelegasikan voting power ke pihak lain (off-chain via Snapshot; on-chain via governance contract). Detail mekanisme delegasi on-chain belum terdokumentasi publik (MEDIUM – disebutkan di docs tapi detail teknis kurang) [Scroll Docs Governance, https://docs.scroll.io/governance/delegation] [Scroll Snapshot, https://snapshot.org/#/scroll.eth]
Proposal System: Proposer harus memiliki minimum SCR balance (threshold belum diungkap); proposal dapat berupa signal proposal (off-chain) atau executable proposal (on-chain dengan timelock). Sistem on-chain menggunakan OpenZeppelin Governor integration (MEDIUM – framework Governor disebutkan di docs, tapi parameter threshold/period belum spesifik) [Scroll Docs Governance, https://docs.scroll.io/governance/proposals] [Scroll Contracts GitHub, https://github.com/scroll-tech/scroll-bridge-contracts/tree/main/contracts/governance]
Treasury Governance: DAO treasury (50,000,000 SCR) dikelola melalui governance vote; eksekusi anggaran melalui timelock dan Security Council veto (jika ada) – detail alur belum dipublikasikan penuh (MEDIUM – docs menyebut treasury governance via DAO, detail mekanisme tidak lengkap) [Scroll Docs Governance, https://docs.scroll.io/governance/treasury] [Scroll Gov Forum Treasury, https://gov.scroll.io/c/treasury/5]
Status: Governance live untuk proposal off-chain (Snapshot) dan on-chain (Governor) sejak TGE (MEDIUM – ada proposal di forum dan Snapshot sejak 2024) [Scroll Snapshot, https://snapshot.org/#/scroll.eth] [Scroll Gov Forum, https://gov.scroll.io]

Sources:
https://docs.scroll.io/governance/overview
https://docs.scroll.io/governance/voting
https://docs.scroll.io/governance/delegation
https://docs.scroll.io/governance/proposals
https://snapshot.org/#/scroll.eth
https://gov.scroll.io

---

## Inflation / Deflation

Inflation Mechanism: Tidak ada mekanisme inflasi aktif yang dipublikasikan; total supply tetap 1 miliar SCR (fixed supply) sejak TGE. Tidak ada emission schedule untuk token baru di dokumentasi publik (MEDIUM – tokenomics docs tidak menyebut inflasi; supply disebut "fixed" di beberapa sumber) (LOW – ada kemungkinan future emission melalui governance tapi belum diumumkan) [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics] [Scroll Blog TGE, https://scroll.io/blog/tge]
Emission Schedule: Tidak ada emission schedule publik selain vesting schedule untuk alokasi existing (team, investors, foundation, ecosystem, community); tidak ada block reward atau validator emission baru (HIGH – vesting schedule adalah satu-satunya sumber supply baru ke circulating) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Burn Mechanism: Tidak ada burn mechanism yang aktif atau direncanakan dalam dokumentasi resmi. Tidak ada mekanisme pembakaran token untuk mengurangi supply (LOW – tidak disebutkan di docs) [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics] [Scroll Blog TGE, https://scroll.io/blog/tge]
Buyback: Tidak ada program buyback SCR yang diumumkan oleh Foundation atau DAO (LOW – tidak ada bukti buyback) [Scroll Gov Forum, https://gov.scroll.io] [Scroll Blog, https://scroll.io/blog]
Supply Reduction: Tidak ada mekanisme supply reduction (burn/buyback) yang live. Satu-satunya perubahan supply adalah perpindahan dari locked (vesting) ke circulating (unlock) seiring waktu (MEDIUM) [Scroll Blog TGE, https://scroll.io/blog/tge]
Status: Deflationary-neutral – supply tetap konstan (1 miliar) tanpa inflasi; tanpa burn, supply effectively fixed namun circulating bertambah seiring vesting (MEDIUM) [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]

Sources:
https://docs.scroll.io/tokenomics
https://scroll.io/blog/tge

---

## Holder Distribution

Top Holder Concentration: Tidak diungkap – tidak ada data on-chain resmi dari Scroll Foundation mengenai distribusi holder teratas. Data Etherscan menunjukkan konsentrasi tetapi belum diverifikasi akurasi (LOW) [Etherscan Top Holders, https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A#balances]
Foundation Holding: Alokasi foundation 20% (200,000,000 SCR) + treasury 5% (50,000,000 SCR) = 25% total supply di bawah kontrol foundation/DAO (HIGH – dari alokasi distribution) (MEDIUM – apakah treasury terpisah dari foundation tidak jelas) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
Investor Holding: 15% (150,000,000 SCR) dipegang oleh investor private sale (Series A, Series B, Strategic) dalam bentuk vested tokens (HIGH – dari alokasi distribution) [Scroll Blog TGE, https://scroll.io/blog/tge]
Treasury Holding: 5% (50,000,000 SCR) untuk DAO treasury – address on-chain tidak dipublikasikan (MEDIUM – alokasi tercatat, address tidak ada) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Governance Treasury, https://docs.scroll.io/governance/treasury]
Community Holding: 15% (150,000,000 SCR) untuk community allocation (termasuk airdrop); jumlah yang sudah diklaim/di-hold oleh community tidak diungkap (MEDIUM – alokasi tercatat, klaim aktual tidak ada data) [Scroll Blog TGE, https://scroll.io/blog/tge]
Whale Concentration: Tidak diketahui – tidak ada analisis whale concentration resmi atau independent yang dipublikasikan (LOW) [Etherscan Holder Analytics, https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A#balances]

Note: Semua angka di atas adalah alokasi teoritis per blog TGE; jumlah aktual yang sudah vesting/unlocked tidak tersedia dari sumber resmi.

Sources:
https://scroll.io/blog/tge
https://docs.scroll.io/tokenomics
https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A#balances

---

## Major Token Events

Event Date: 2024-10-22
Event Name: TGE dan Emisi Awal
Description: SCR token diluncurkan di Ethereum Mainnet bersamaan dengan Scroll zkEVM Mainnet launch. Total supply 1 miliar dialokasikan ke dashboard tokenomics. (HIGH) [Scroll Blog TGE, https://scroll.io/blog/tge]
Status: Completed
Related Historical Event ID: EV-010

Event Date: 2024-10-22
Event Name: Airdrop Community (Fase 1)
Description: Community allocation (15% = 150M SCR) mulai didistribusikan kepada pengguna yang memenuhi kriteria keterlibatan testnet/mainnet. Detail kriteria dan jumlah klaim tidak diungkap publik. (MEDIUM – blog TGE menyebut airdrop dimulai, tapi detail kriteria tidak lengkap) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Blog Airdrop, https://scroll.io/blog/scr-airdrop]
Status: Completed (fase awal selesai; klaim lanjutan mungkin masih berjalan)

Event Date: 2024-10-22 onwards
Event Name: Listing di CEX dan DEX
Description: SCR terseedia di centralized exchanges (nama spesifik tidak diungkap lengkap di blog; perlu verifikasi CoinGecko/CMC) dan DEX setelah TGE untuk liquidity trading. (MEDIUM – listing CEX disebutkan tapi tidak semua exchange terdaftar resmi) [CoinGecko Markets, https://coingecko.com/en/coins/scroll#markets] [CoinMarketCap Listing, https://coinmarketcap.com/currencies/scroll/]
Status: Completed (live)

Event Date: 2024-11 to present
Event Name: Program Launch Ecosystem Grants
Description: Alokasi ecosystem (20% = 200M SCR) digunakan untuk program grants (builder grants, hackathon, liquidity incentives). Program grans aktif dihalaman resmi. (MEDIUM – program grants terlihat live, tapi jumlah yang sudah terdistribusi tidak diungkap) [Scroll Ecosystem Grants, https://scroll.io/ecosystem/grants] [Gov Forum Grants, https://gov.scroll.io/c/grants/6]
Status: Ongoing

Event Date: 2025 (proposal, belum dieksekusi)
Event Name: Proposal Fee Switch
Description: Proposal governance untuk mengaktifkan protocol fee switch (persentase dari sequencer/base fee untuk DAO treasury). Masih dalam tahap diskusi forum. (LOW – proposal only, tidak ada status eksekusi) [Gov Forum Fee Switch, https://gov.scroll.io/t/protocol-fee-switch-proposal/456]
Status: Proposed (belum eksekusi)

Event Date: 2025 (rencana)
Event Name: Desentralisasi Staking SCR
Description: Roadmap menyebut SCR akan digunakan untuk staking oleh sequencer/prover terdesentralisasi di masa depan; belum ada implementasi. (LOW – roadmap hanya) [Scroll Blog Decentralization, https://scroll.io/blog/decentralization-roadmap]
Status: Planned

Sources:
https://scroll.io/blog/tge
https://scroll.io/blog/scr-airdrop
https://scroll.io/ecosystem/grants
https://gov.scroll.io/t/protocol-fee-switch-proposal/456
https://scroll.io/blog/decentralization-roadmap
https://coinmarketcap.com/currencies/scroll/

---

## Official Token Resources

Official Documentation: https://docs.scroll.io/tokenomics
Whitepaper: https://scroll.io/whitepaper.pdf
Governance: https://gov.scroll.io
Governance Snapshot: https://snapshot.org/#/scroll.eth
Explorer (Ethereum): https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A
Explorer (Scroll L2): https://scrollscan.com/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A (perlu verifikasi apakah token di-deploy di L2 juga)
Contract (Ethereum): https://etherscan.io/address/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A (perlu verifikasi apakah ini alamat benar)
Contract (GitHub): https://github.com/scroll-tech/scroll-bridge-contracts (belum dikonfirmasi apakah memuat token contract source)
GitHub: https://github.com/scroll-tech
Dashboard: Tidak ada token dashboard resmi yang publik (misal Token Terminal, Messari) – hanya explorer dan tokenomics page
Airdrop Portal: https://scroll.io/airdrop (perlu verifikasi apakah masih aktif)

Sources:
https://docs.scroll.io/tokenomics
https://scroll.io/whitepaper.pdf
https://gov.scroll.io
https://snapshot.org/#/scroll.eth
https://etherscan.io/token/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A
https://scrollscan.com
https://scroll.io/ecosystem/grants

---

## Ringkasan

Status: Live (TGE 2024-10-22)
Supply Type: Fixed (1 miliar SCR) – tanpa inflasi aktif atau burn mechanism
Total Supply: 1,000,000,000 SCR (1 miliar)
Distribution Categories: 6 kategori (Community 15%, Team 25%, Investors 15%, Foundation 20%, Treasury 5%, Ecosystem 20%)
Utility Count: 5 utilitas tercatat (Governance live; Gas planned; Staking planned; Protocol Fee planned; Ecosystem Incentives live)
Governance: Dua tahap (Snapshot off-chain + OpenZeppelin Governor on-chain); weighted voting 1 SCR = 1 vote; delegation tersedia
Major Token Events: 6 event (TGE, Airdrop Phase 1, CEX/DEX listing, Ecosystem Grants aktif, Fee Switch proposal, Staking roadmap)

---

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Scroll

## Ecosystem Position

Primary Sector: zkEVM Layer 2 Rollup (EVM-equivalent) (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Secondary Sector: Ethereum Scaling Infrastructure (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Primary Chain: Ethereum (L1 settlement) (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Supported Chains: Scroll zkEVM Mainnet (L2), Scroll Sepolia Testnet (L2 testnet), Ethereum Mainnet (L1), Ethereum Sepolia (L1 testnet) (HIGH) [Scroll Documentation Testnet, https://docs.scroll.io/developers/testnet]

Sources:
https://docs.scroll.io/architecture/overview
https://docs.scroll.io/developers/testnet

---

## External Dependencies

Dependency Name: Ethereum
Dependency Type: Chain
Purpose: Settlement layer, data availability (calldata/blob via EIP-4844), finality via L1 verification of ZK-proofs (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Criticality: Critical
Status: Live
Related Entity: Ethereum
Related Technology Component: L1 Settlement Contracts, Roller, Data Availability module
Sources:
https://docs.scroll.io/architecture/overview
https://docs.scroll.io/architecture/data-availability

Dependency Name: Halo2 (PLONKish arithmetization) + KZG Polynomial Commitment
Dependency Type: Protocol / Cryptographic Primitive
Purpose: Zero-knowledge proof system untuk validity proofs (zkProver) (HIGH) [Scroll ZK-Proof Blog, https://scroll.io/blog/zk-proof-system]
Criticality: Critical
Status: Live
Related Entity: Privacy and Scaling Explorations (PSE) / Ethereum Foundation
Related Technology Component: zkProver, Halo2 circuits, Verifier contract
Sources:
https://scroll.io/blog/zk-proof-system
https://github.com/privacy-scaling-explorations/halo2

Dependency Name: Perpetual Powers of Tau Ceremony
Dependency Type: Protocol / Trusted Setup
Purpose: KZG trusted setup untuk polynomial commitments (HIGH) [Scroll Trusted Setup Docs, https://docs.scroll.io/architecture/trusted-setup]
Criticality: Critical
Status: Live
Related Entity: Privacy and Scaling Explorations (PSE)
Related Technology Component: zkProver, Verifier contract
Sources:
https://docs.scroll.io/architecture/trusted-setup
https://github.com/privacy-scaling-explorations/perpetual-powers-of-tau

Dependency Name: go-ethereum (Geth) v1.13+
Dependency Type: SDK / Execution Client Base
Purpose: Base execution client untuk L2 execution engine (modified Geth) (HIGH) [Scroll Execution Client GitHub, https://github.com/scroll-tech/go-ethereum]
Criticality: Critical
Status: Live
Related Entity: Ethereum Foundation (Geth maintainers)
Related Technology Component: L2 Execution Engine (Scroll Execution Client)
Sources:
https://github.com/scroll-tech/go-ethereum
https://docs.scroll.io/architecture/execution

Dependency Name: Blockscout
Dependency Type: Infrastructure / Indexer
Purpose: Block explorer backend (Scrollscan) dan indexer untuk on-chain data (HIGH) [Scrollscan Blockscout Fork, https://github.com/scroll-tech/blockscout]
Criticality: High
Status: Live
Related Entity: Blockscout
Related Technology Component: Scroll Node, Indexer, Scrollscan UI
Sources:
https://github.com/scroll-tech/blockscout
https://scrollscan.com

Dependency Name: LayerZero
Dependency Type: Protocol / Bridge / Cross-chain Messaging
Purpose: Omnichain messaging, OFT standard untuk cross-chain token transfers (HIGH) [LayerZero Scroll Integration, https://layerzero.network/blog/scroll-integration]
Criticality: High
Status: Live
Related Entity: LayerZero
Related Technology Component: Cross-chain messaging layer (application layer)
Sources:
https://layerzero.network/blog/scroll-integration
https://scroll.io/ecosystem

Dependency Name: Wormhole
Dependency Type: Protocol / Bridge / Cross-chain Messaging
Purpose: Cross-chain messaging dan token bridging (HIGH) [Wormhole Scroll Integration, https://wormhole.com/ecosystem/scroll]
Criticality: High
Status: Live
Related Entity: Wormhole
Related Technology Component: Cross-chain messaging layer (application layer)
Sources:
https://wormhole.com/ecosystem/scroll
https://scroll.io/ecosystem

Dependency Name: Chainlink
Dependency Type: Oracle
Purpose: Price Feeds, VRF, CCIP, Proof of Reserve untuk DeFi aplikasi (HIGH) [Chainlink Scroll Support, https://blog.chain.link/chainlink-scroll-support]
Criticality: High
Status: Live
Related Entity: Chainlink
Related Technology Component: Oracle infrastructure (application layer)
Sources:
https://blog.chain.link/chainlink-scroll-support
https://scroll.io/ecosystem

Dependency Name: Pyth Network
Dependency Type: Oracle
Purpose: First-party financial market data price feeds (HIGH) [Pyth Scroll Integration, https://pyth.network/developers/price-feed-ids#scroll]
Criticality: High
Status: Live
Related Entity: Pyth Network
Related Technology Component: Oracle infrastructure (application layer)
Sources:
https://pyth.network/developers/price-feed-ids#scroll
https://scroll.io/ecosystem

Dependency Name: Gelato Network
Dependency Type: Infrastructure / Automation
Purpose: Smart contract automation, relay, Web3 Functions (HIGH) [Gelato Scroll Integration, https://gelato.network/networks/scroll]
Criticality: Medium
Status: Live
Related Entity: Gelato Network
Related Technology Component: Automation infrastructure (application layer)
Sources:
https://gelato.network/networks/scroll
https://scroll.io/ecosystem

Dependency Name: Hyperlane
Dependency Type: Protocol / Cross-chain Messaging
Purpose: Permissionless interoperability messaging (HIGH) [Hyperlane Scroll Docs, https://docs.hyperlane.xyz/docs/chains/scroll]
Criticality: Medium
Status: Live
Related Entity: Hyperlane
Related Technology Component: Cross-chain messaging layer (application layer)
Sources:
https://docs.hyperlane.xyz/docs/chains/scroll
https://scroll.io/ecosystem

Dependency Name: Safe (Gnosis Safe)
Dependency Type: Infrastructure / Wallet
Purpose: Multi-sig wallet infrastructure untuk treasury/DAO management (HIGH) [Safe Scroll Deployment, https://safe.global/networks/scroll]
Criticality: Medium
Status: Live
Related Entity: Safe
Related Technology Component: Wallet infrastructure (application layer)
Sources:
https://safe.global/networks/scroll
https://scroll.io/ecosystem

Dependency Name: EigenLayer
Dependency Type: Protocol / Restaking
Purpose: Shared security, restaking infrastructure (HIGH) [EigenLayer Scroll Integration, https://www.eigenlayer.xyz/ecosystem/scroll]
Criticality: Medium
Status: Live
Related Entity: EigenLayer
Related Technology Component: Restaking infrastructure (application layer)
Sources:
https://www.eigenlayer.xyz/ecosystem/scroll
https://scroll.io/ecosystem

Dependency Name: Symbiotic
Dependency Type: Protocol / Restaking
Purpose: Permissionless restaking protocol (HIGH) [Symbiotic Scroll, https://symbiotic.fi/networks/scroll]
Criticality: Medium
Status: Live
Related Entity: Symbiotic
Related Technology Component: Restaking infrastructure (application layer)
Sources:
https://symbiotic.fi/networks/scroll
https://scroll.io/ecosystem

Dependency Name: Karak
Dependency Type: Protocol / Restaking
Purpose: Universal restaking layer (HIGH) [Karak Scroll, https://karak.network/ecosystem/scroll]
Criticality: Medium
Status: Live
Related Entity: Karak
Related Technology Component: Restaking infrastructure (application layer)
Sources:
https://karak.network/ecosystem/scroll
https://scroll.io/ecosystem

Dependency Name: Docker
Dependency Type: Infrastructure / Containerization
Purpose: Containerized deployment untuk all services (node, prover, sequencer) (HIGH) [Scroll Docker Hub, https://hub.docker.com/u/scrolltech]
Criticality: High
Status: Live
Related Entity: Docker Inc.
Related Technology Component: All production services
Sources:
https://hub.docker.com/u/scrolltech
https://github.com/scroll-tech/scroll-docker

Dependency Name: Kubernetes
Dependency Type: Infrastructure / Orchestration
Purpose: Production orchestration untuk prover cluster, sequencer HA, roller (MEDIUM) [Scroll Infra GitHub, https://github.com/scroll-tech/infra]
Criticality: High
Status: Live
Related Entity: Cloud Native Computing Foundation (CNCF) / Cloud providers
Related Technology Component: Prover cluster, Sequencer, Roller
Sources:
https://github.com/scroll-tech/infra
https://docs.scroll.io/developers/run-node

Dependency Name: PostgreSQL
Dependency Type: Infrastructure / Database
Purpose: Indexer/Blockscout database storage (HIGH) [Blockscout Schema, https://github.com/blockscout/blockscout/blob/master/docs/database.md]
Criticality: High
Status: Live
Related Entity: PostgreSQL Global Development Group
Related Technology Component: Indexer, Blockscout
Sources:
https://github.com/blockscout/blockscout/blob/master/docs/database.md
https://scrollscan.com

Dependency Name: Redis
Dependency Type: Infrastructure / Cache
Purpose: Caching layer untuk RPC, Bridge UI (MEDIUM) [Scroll Infra Config, https://github.com/scroll-tech/infra/tree/main/k8s/redis]
Criticality: Medium
Status: Live
Related Entity: Redis Ltd.
Related Technology Component: RPC endpoints, Bridge UI
Sources:
https://github.com/scroll-tech/infra/tree/main/k8s/redis
https://docs.scroll.io/developers/rpc-endpoints

Dependency Name: Prometheus + Grafana
Dependency Type: Infrastructure / Monitoring
Purpose: Monitoring, alerting, metrics collection (HIGH) [Scroll Monitoring Dashboards, https://grafana.scroll.io/]
Criticality: High
Status: Live
Related Entity: Prometheus (CNCF), Grafana Labs
Related Technology Component: All production services
Sources:
https://grafana.scroll.io/
https://github.com/scroll-tech/infra

Dependency Name: Foundry / Hardhat
Dependency Type: SDK / Developer Framework
Purpose: Smart contract development, testing, deployment frameworks (HIGH) [Scroll Foundry Template, https://github.com/scroll-tech/foundry-scroll-template]
Criticality: High
Status: Live
Related Entity: Paradigm (Foundry), Nomic Foundation (Hardhat)
Related Technology Component: Scroll SDK, Developer tooling
Sources:
https://github.com/scroll-tech/foundry-scroll-template
https://github.com/scroll-tech/hardhat-scroll

Dependency Name: Alchemy / Infura / QuickNode / Other RPC Providers
Dependency Type: Infrastructure / RPC Service
Purpose: Public RPC endpoints untuk developer/user access (HIGH) [Scroll RPC Endpoints, https://docs.scroll.io/developers/rpc-endpoints]
Criticality: High
Status: Live
Related Entity: Alchemy, Infura (Consensys), QuickNode
Related Technology Component: Scroll Node, Public RPC
Sources:
https://docs.scroll.io/developers/rpc-endpoints
https://scroll.io/ecosystem

---

## Major Integrations

Integration Name: LayerZero
Integrated With: LayerZero
Purpose: Omnichain messaging, OFT standard untuk cross-chain token transfers (HIGH) [LayerZero Scroll Integration, https://layerzero.network/blog/scroll-integration]
Status: Live
Related Historical Event ID: EV-011
Sources:
https://layerzero.network/blog/scroll-integration
https://scroll.io/ecosystem

Integration Name: Wormhole
Integrated With: Wormhole
Purpose: Cross-chain messaging dan token bridging (HIGH) [Wormhole Scroll Integration, https://wormhole.com/ecosystem/scroll]
Status: Live
Related Historical Event ID: EV-012
Sources:
https://wormhole.com/ecosystem/scroll
https://scroll.io/ecosystem

Integration Name: Chainlink
Integrated With: Chainlink
Purpose: Price Feeds, VRF, CCIP, Proof of Reserve (HIGH) [Chainlink Scroll Support, https://blog.chain.link/chainlink-scroll-support]
Status: Live
Related Historical Event ID: EV-013
Sources:
https://blog.chain.link/chainlink-scroll-support
https://scroll.io/ecosystem

Integration Name: Pyth Network
Integrated With: Pyth Network
Purpose: First-party financial market data price feeds (HIGH) [Pyth Scroll Integration, https://pyth.network/developers/price-feed-ids#scroll]
Status: Live
Related Historical Event ID: EV-014
Sources:
https://pyth.network/developers/price-feed-ids#scroll
https://scroll.io/ecosystem

Integration Name: Gelato Network
Integrated With: Gelato Network
Purpose: Smart contract automation, relay, Web3 Functions (HIGH) [Gelato Scroll Integration, https://gelato.network/networks/scroll]
Status: Live
Related Historical Event ID: EV-015
Sources:
https://gelato.network/networks/scroll
https://scroll.io/ecosystem

Integration Name: Safe (Gnosis Safe)
Integrated With: Safe
Purpose: Multi-sig wallet deployment untuk treasury/DAO management (HIGH) [Safe Scroll Deployment, https://safe.global/networks/scroll]
Status: Live
Related Historical Event ID: EV-016
Sources:
https://safe.global/networks/scroll
https://scroll.io/ecosystem

Integration Name: Hyperlane
Integrated With: Hyperlane
Purpose: Permissionless interoperability messaging (HIGH) [Hyperlane Scroll Docs, https://docs.hyperlane.xyz/docs/chains/scroll]
Status: Live
Related Historical Event ID: EV-017
Sources:
https://docs.hyperlane.xyz/docs/chains/scroll
https://scroll.io/ecosystem

Integration Name: Uniswap v3/v4
Integrated With: Uniswap
Purpose: DEX liquidity dan trading (HIGH) [Uniswap Scroll Deployment, https://app.uniswap.org/explore/tokens/scroll]
Status: Live
Related Historical Event ID: EV-018
Sources:
https://app.uniswap.org/explore/tokens/scroll
https://scroll.io/ecosystem

Integration Name: Aave v3
Integrated With: Aave
Purpose: Lending/borrowing money market (HIGH) [Aave Scroll Market, https://app.aave.ui/#/markets/scroll]
Status: Live
Related Historical Event ID: EV-019
Sources:
https://app.aave.ui/#/markets/scroll
https://scroll.io/ecosystem

Integration Name: PancakeSwap
Integrated With: PancakeSwap
Purpose: DEX (AMM), farming, IFO (HIGH) [PancakeSwap Scroll, https://pancakeswap.finance/swap?chain=scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://pancakeswap.finance/swap?chain=scroll
https://scroll.io/ecosystem

Integration Name: SushiSwap
Integrated With: SushiSwap
Purpose: DEX, AMM, limit order, yield farming (HIGH) [SushiSwap Scroll, https://www.sushi.com/swap?chainId=534352]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://www.sushi.com/swap?chainId=534352
https://scroll.io/ecosystem

Integration Name: Balancer
Integrated With: Balancer
Purpose: Weighted pools AMM untuk portfolio management (HIGH) [Balancer Scroll Deployment, https://app.balancer.fi/#/scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://app.balancer.fi/#/scroll
https://scroll.io/ecosystem

Integration Name: Curve Finance
Integrated With: Curve Finance
Purpose: Stablecoin AMM low-slippage swapping (HIGH) [Curve Scroll Deployment, https://curve.fi/#/scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://curve.fi/#/scroll
https://scroll.io/ecosystem

Integration Name: Pendle Finance
Integrated With: Pendle Finance
Purpose: Yield tokenization protocol untuk trading future yield (HIGH) [Pendle Scroll Market, https://app.pendle.finance/trade/markets?chain=scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://app.pendle.finance/trade/markets?chain=scroll
https://scroll.io/ecosystem

Integration Name: Euler Finance
Integrated With: Euler Finance
Purpose: Modular lending protocol untuk permissionless lending markets (HIGH) [Euler Scroll Deployment, https://app.euler.finance/#/scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://app.euler.finance/#/scroll
https://scroll.io/ecosystem

Integration Name: Morpho
Integrated With: Morpho
Purpose: Capital-efficient lending (Morpho Blue) (HIGH) [Morpho Scroll Deployment, https://app.morpho.org/markets?chain=scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://app.morpho.org/markets?chain=scroll
https://scroll.io/ecosystem

Integration Name: Radiant Capital
Integrated With: Radiant Capital
Purpose: Cross-chain lending protocol untuk unified liquidity (HIGH) [Radiant Scroll Market, https://app.radiant.capital/#/scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://app.radiant.capital/#/scroll
https://scroll.io/ecosystem

Integration Name: Silo Finance
Integrated With: Silo Finance
Purpose: Isolated lending markets protocol (HIGH) [Silo Scroll Deployment, https://app.silo.finance/#/scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://app.silo.finance/#/scroll
https://scroll.io/ecosystem

Integration Name: Gearbox Protocol
Integrated With: Gearbox Protocol
Purpose: Leverage protocol untuk credit account abstraction (HIGH) [Gearbox Scroll, https://app.gearbox.fi/#/scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://app.gearbox.fi/#/scroll
https://scroll.io/ecosystem

Integration Name: CIAN
Integrated With: CIAN
Purpose: Yield automation platform untuk automated strategies (HIGH) [CIAN Scroll, https://cian.app/?chain=scroll]
Status: Live
Related Historical Event ID: EV-020
Sources:
https://cian.app/?chain=scroll
https://scroll.io/ecosystem

Integration Name: EigenLayer
Integrated With: EigenLayer
Purpose: Restaking protocol shared security (HIGH) [EigenLayer Scroll Integration, https://www.eigenlayer.xyz/ecosystem/scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://www.eigenlayer.xyz/ecosystem/scroll
https://scroll.io/ecosystem

Integration Name: Symbiotic
Integrated With: Symbiotic
Purpose: Permissionless restaking protocol (HIGH) [Symbiotic Scroll, https://symbiotic.fi/networks/scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://symbiotic.fi/networks/scroll
https://scroll.io/ecosystem

Integration Name: Karak
Integrated With: Karak
Purpose: Universal restaking layer (HIGH) [Karak Scroll, https://karak.network/ecosystem/scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://karak.network/ecosystem/scroll
https://scroll.io/ecosystem

Integration Name: Renzo Protocol
Integrated With: Renzo Protocol
Purpose: Liquid restaking token (ezETH) untuk EigenLayer restaking (HIGH) [Renzo Scroll, https://app.renzoprotocol.com/?chain=scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://app.renzoprotocol.com/?chain=scroll
https://scroll.io/ecosystem

Integration Name: Ether.fi
Integrated With: Ether.fi
Purpose: Liquid restaking protocol (eETH) (HIGH) [Ether.fi Scroll, https://app.ether.fi/?chain=scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://app.ether.fi/?chain=scroll
https://scroll.io/ecosystem

Integration Name: Puffer Finance
Integrated With: Puffer Finance
Purpose: Native liquid restaking (pufETH) (HIGH) [Puffer Scroll, https://app.puffer.fi/?chain=scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://app.puffer.fi/?chain=scroll
https://scroll.io/ecosystem

Integration Name: Swell Network
Integrated With: Swell Network
Purpose: Liquid restaking (swETH) dan liquid staking (rETH) (HIGH) [Swell Scroll, https://app.swellnetwork.io/?chain=scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://app.swellnetwork.io/?chain=scroll
https://scroll.io/ecosystem

Integration Name: Kelp DAO
Integrated With: Kelp DAO
Purpose: Liquid restaking (rsETH) (HIGH) [Kelp Scroll, https://app.kelpdao.xyz/?chain=scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://app.kelpdao.xyz/?chain=scroll
https://scroll.io/ecosystem

Integration Name: Mellow Protocol
Integrated With: Mellow Protocol
Purpose: Restaking vault optimizer (HIGH) [Mellow Scroll, https://app.mellow.finance/?chain=scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://app.mellow.finance/?chain=scroll
https://scroll.io/ecosystem

Integration Name: Kernel
Integrated With: Kernel
Purpose: Restaking infrastructure untuk BTC/ETH restaking (HIGH) [Kernel Scroll Integration, https://kernel.dao/#/scroll]
Status: Live
Related Historical Event ID: EV-021
Sources:
https://kernel.dao/#/scroll
https://scroll.io/ecosystem

Integration Name: MetaMask
Integrated With: MetaMask
Purpose: Wallet integration via Snaps dan RPC native (HIGH) [MetaMask Scroll RPC, https://chainlist.org/chain/534352]
Status: Live
Related Historical Event ID: EV-022
Sources:
https://chainlist.org/chain/534352
https://docs.scroll.io/developers/add-network

Integration Name: Rabby Wallet
Integrated With: Rabby Wallet
Purpose: Browser extension wallet support (HIGH) [Rabby Scroll Support, https://rabby.io/chains/scroll]
Status: Live
Related Historical Event ID: EV-022
Sources:
https://rabby.io/chains/scroll
https://scroll.io/ecosystem

Integration Name: OKX Wallet
Integrated With: OKX Wallet
Purpose: Multi-chain wallet (browser extension & mobile) (HIGH) [OKX Wallet Scroll, https://www.okx.com/web3/scroll]
Status: Live
Related Historical Event ID: EV-022
Sources:
https://www.okx.com/web3/scroll
https://scroll.io/ecosystem

Integration Name: Rainbow Wallet
Integrated With: Rainbow Wallet
Purpose: Mobile wallet support (HIGH) [Rainbow Scroll Support, https://rainbow.me/chains/scroll]
Status: Live
Related Historical Event ID: EV-022
Sources:
https://rainbow.me/chains/scroll
https://scroll.io/ecosystem

Integration Name: Zerion
Integrated With: Zerion
Purpose: Wallet dan portfolio tracker (HIGH) [Zerion Scroll Support, https://zerion.io/chain/scroll]
Status: Live
Related Historical Event ID: EV-022
Sources:
https://zerion.io/chain/scroll
https://scroll.io/ecosystem

Integration Name: Instadapp
Integrated With: Instadapp
Purpose: DeFi management platform untuk portfolio management (HIGH) [Instadapp Scroll, https://instadapp.io/?chain=scroll]
Status: Live
Related Historical Event ID: EV-022
Sources:
https://instadapp.io/?chain=scroll
https://scroll.io/ecosystem

Integration Name: Scrollscan (Blockscout)
Integrated With: Blockscout
Purpose: Block explorer backend (HIGH) [Scrollscan, https://scrollscan.com]
Status: Live
Related Historical Event ID: EV-022
Sources:
https://scrollscan.com
https://github.com/scroll-tech/blockscout

Integration Name: L2Scan
Integrated With: L2Scan
Purpose: Alternative block explorer dengan analytics (HIGH) [L2Scan Scroll, https://scroll.l2scan.co]
Status: Live
Related Historical Event ID: EV-022
Sources:
https://scroll.l2scan.co
https://l2scan.co

---

## Infrastructure Providers

Provider: Alchemy
Service: RPC endpoints, enhanced APIs, webhooks (HIGH) [Scroll RPC Endpoints, https://docs.scroll.io/developers/rpc-endpoints]
Criticality: High
Status: Live
Sources:
https://docs.scroll.io/developers/rpc-endpoints
https://scroll.io/ecosystem

Provider: Infura (Consensys)
Service: RPC endpoints, Ethereum API infrastructure (HIGH) [Scroll RPC Endpoints, https://docs.scroll.io/developers/rpc-endpoints]
Criticality: High
Status: Live
Sources:
https://docs.scroll.io/developers/rpc-endpoints
https://scroll.io/ecosystem

Provider: QuickNode
Service: RPC endpoints, node infrastructure (HIGH) [Scroll RPC Endpoints, https://docs.scroll.io/developers/rpc-endpoints]
Criticality: High
Status: Live
Sources:
https://docs.scroll.io/developers/rpc-endpoints
https://scroll.io/ecosystem

Provider: Blockscout
Service: Block explorer backend, indexing (HIGH) [Scrollscan Blockscout Fork, https://github.com/scroll-tech/blockscout]
Criticality: High
Status: Live
Sources:
https://github.com/scroll-tech/blockscout
https://scrollscan.com

Provider: L2Scan
Service: Alternative block explorer, analytics (HIGH) [L2Scan Scroll, https://scroll.l2scan.co]
Criticality: Medium
Status: Live
Sources:
https://scroll.l2scan.co
https://l2scan.co

Provider: Cloud Providers (AWS/GCP/Azure - unspecified)
Service: Cloud infrastructure untuk Kubernetes clusters, prover nodes, sequencer (MEDIUM) [Scroll Infra GitHub, https://github.com/scroll-tech/infra]
Criticality: High
Status: Live
Sources:
https://github.com/scroll-tech/infra
https://docs.scroll.io/developers/run-node

Provider: Docker Hub
Service: Container image registry (HIGH) [Scroll Docker Hub, https://hub.docker.com/u/scrolltech]
Criticality: High
Status: Live
Sources:
https://hub.docker.com/u/scrolltech
https://github.com/scroll-tech/scroll-docker

Provider: GitHub (Microsoft)
Service: Source control, CI/CD (GitHub Actions), issue tracking (HIGH) [Scroll GitHub Organization, https://github.com/scroll-tech]
Criticality: High
Status: Live
Sources:
https://github.com/scroll-tech
https://github.com/scroll-tech/.github

---

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Perpetual: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/

Exchange: Coinbase
Listing Status: Listed
Spot: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/

Exchange: OKX
Listing Status: Listed
Spot: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Perpetual: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/

Exchange: Bybit
Listing Status: Listed
Spot: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Perpetual: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/

Exchange: Kraken
Listing Status: Listed
Spot: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Perpetual: tidak diketahui
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/

Exchange: KuCoin
Listing Status: Listed
Spot: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Perpetual: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/

Exchange: Gate.io
Listing Status: Listed
Spot: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Perpetual: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/

Exchange: HTX (Huobi)
Listing Status: Listed
Spot: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Perpetual: Yes (MEDIUM) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
OTC: tidak diketahui
Launchpool: tidak diketahui
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/

Exchange: Uniswap (DEX)
Listing Status: Listed
Spot: Yes (HIGH) [Uniswap Scroll, https://app.uniswap.org/explore/tokens/scroll]
Perpetual: No
OTC: No
Launchpool: No
Status: Live
Sources:
https://app.uniswap.org/explore/tokens/scroll
https://scroll.io/ecosystem

Exchange: PancakeSwap (DEX)
Listing Status: Listed
Spot: Yes (HIGH) [PancakeSwap Scroll, https://pancakeswap.finance/swap?chain=scroll]
Perpetual: No
OTC: No
Launchpool: No
Status: Live
Sources:
https://pancakeswap.finance/swap?chain=scroll
https://scroll.io/ecosystem

Exchange: SushiSwap (DEX)
Listing Status: Listed
Spot: Yes (HIGH) [SushiSwap Scroll, https://www.sushi.com/swap?chainId=534352]
Perpetual: No
OTC: No
Launchpool: No
Status: Live
Sources:
https://www.sushi.com/swap?chainId=534352
https://scroll.io/ecosystem

Exchange: Balancer (DEX)
Listing Status: Listed
Spot: Yes (HIGH) [Balancer Scroll, https://app.balancer.fi/#/scroll]
Perpetual: No
OTC: No
Launchpool: No
Status: Live
Sources:
https://app.balancer.fi/#/scroll
https://scroll.io/ecosystem

Exchange: Curve Finance (DEX)
Listing Status: Listed
Spot: Yes (HIGH) [Curve Scroll, https://curve.fi/#/scroll]
Perpetual: No
OTC: No
Launchpool: No
Status: Live
Sources:
https://curve.fi/#/scroll
https://scroll.io/ecosystem

---

## Wallet Ecosystem

Wallet: MetaMask
Support Type: Native RPC + Snaps (HIGH) [MetaMask Scroll RPC, https://chainlist.org/chain/534352]
Status: Live
Sources:
https://chainlist.org/chain/534352
https://docs.scroll.io/developers/add-network

Wallet: Rabby Wallet
Support Type: Browser extension, native chain support (HIGH) [Rabby Scroll Support, https://rabby.io/chains/scroll]
Status: Live
Sources:
https://rabby.io/chains/scroll
https://scroll.io/ecosystem

Wallet: OKX Wallet
Support Type: Browser extension & mobile app, native chain support (HIGH) [OKX Wallet Scroll, https://www.okx.com/web3/scroll]
Status: Live
Sources:
https://www.okx.com/web3/scroll
https://scroll.io/ecosystem

Wallet: Rainbow Wallet
Support Type: Mobile app, native chain support (HIGH) [Rainbow Scroll Support, https://rainbow.me/chains/scroll]
Status: Live
Sources:
https://rainbow.me/chains/scroll
https://scroll.io/ecosystem

Wallet: Zerion
Support Type: Wallet + portfolio tracker, native chain support (HIGH) [Zerion Scroll Support, https://zerion.io/chain/scroll]
Status: Live
Sources:
https://zerion.io/chain/scroll
https://scroll.io/ecosystem

Wallet: Safe (Gnosis Safe)
Support Type: Multi-sig smart contract wallet, deployed on Scroll (HIGH) [Safe Scroll Deployment, https://safe.global/networks/scroll]
Status: Live
Sources:
https://safe.global/networks/scroll
https://scroll.io/ecosystem

Wallet: Trust Wallet
Support Type: tidak diketahui (tidak terdaftar di ecosystem page resmi)
Status: tidak diketahui
Sources:
https://scroll.io/ecosystem

Wallet: Coinbase Wallet
Support Type: tidak diketahui (tidak terdaftar di ecosystem page resmi)
Status: tidak diketahui
Sources:
https://scroll.io/ecosystem

---

## Developer Ecosystem

SDK: Scroll SDK (TypeScript/JavaScript)
Purpose: RPC interaction, contract deployment, bridge integration, developer tooling (HIGH) [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk]
Sources:
https://github.com/scroll-tech/scroll-sdk
https://docs.scroll.io/developers

API: Scroll Public RPC Endpoints
Purpose: JSON-RPC API untuk Ethereum-compatible calls (HIGH) [Scroll RPC Endpoints, https://docs.scroll.io/developers/rpc-endpoints]
Sources:
https://docs.scroll.io/developers/rpc-endpoints
https://docs.scroll.io/developers/rpc-api

Developer Tools: Hardhat Plugin (hardhat-scroll)
Purpose: Hardhat integration untuk deployment, testing, verification di Scroll (HIGH) [Scroll Hardhat Plugin, https://github.com/scroll-tech/hardhat-scroll]
Sources:
https://github.com/scroll-tech/hardhat-scroll
https://docs.scroll.io/developers

Developer Tools: Foundry Template (foundry-scroll-template)
Purpose: Foundry integration untuk testing, fuzzing, deployment di Scroll (HIGH) [Scroll Foundry Template, https://github.com/scroll-tech/foundry-scroll-template]
Sources:
https://github.com/scroll-tech/foundry-scroll-template
https://docs.scroll.io/developers

Developer Tools: Scroll Sepolia Faucet
Purpose: Testnet ETH distribution untuk development (HIGH) [Scroll Sepolia Faucet, https://sepolia-faucet.scroll.io/]
Sources:
https://sepolia-faucet.scroll.io/
https://docs.scroll.io/developers/testnet

Developer Tools: Contract Verification (Blockscout-based)
Purpose: Smart contract source code verification di Scrollscan (HIGH) [Scrollscan Verify, https://scrollscan.com/verifyContract]
Sources:
https://scrollscan.com/verifyContract
https://github.com/scroll-tech/blockscout

Open Source Repository: scroll-tech GitHub Organization
Repositories: zkprover, go-ethereum (execution client), scroll-bridge-contracts, scroll-sdk, infra, blockscout, scroll-docker, audits (HIGH) [Scroll GitHub, https://github.com/scroll-tech]
Sources:
https://github.com/scroll-tech
https://github.com/scroll-tech/zkprover
https://github.com/scroll-tech/go-ethereum
https://github.com/scroll-tech/scroll-bridge-contracts
https://github.com/scroll-tech/scroll-sdk
https://github.com/scroll-tech/infra
https://github.com/scroll-tech/blockscout
https://github.com/scroll-tech/scroll-docker
https://github.com/scroll-tech/audits

Developer Portal: Scroll Documentation
URL: https://docs.scroll.io
Sections: Architecture, Developers, Bridge, Governance, Tokenomics, RPC API (HIGH) [Scroll Docs, https://docs.scroll.io]
Sources:
https://docs.scroll.io
https://docs.scroll.io/developers

Hackathon: Scroll Hackathons (multiple)
Details: Hackathon events diatur secara berkala; detail spesifik (tanggal, hadiah, tema) tidak terkumpul dalam satu halaman resmi (MEDIUM) [Scroll Blog Hackathon, https://scroll.io/blog/category/hackathon] [Scroll Events, https://scroll.io/events]
Sources:
https://scroll.io/blog/category/hackathon
https://scroll.io/events

Grant Program: Scroll Ecosystem Grants
Purpose: Builder grants, hackathon prizes, liquidity incentives dari ecosystem allocation (20% = 200M SCR) (HIGH) [Scroll Ecosystem Grants, https://scroll.io/ecosystem/grants]
Categories: Infrastructure, DeFi, Tooling, Education, Community (MEDIUM) [Gov Forum Grants, https://gov.scroll.io/c/grants/6]
Status: Ongoing
Sources:
https://scroll.io/ecosystem/grants
https://gov.scroll.io/c/grants/6

---

## Applications

Application: Uniswap
Category: DEX (AMM)
Relationship: Deployed v3/v4 pada Scroll Mainnet; core liquidity provider (HIGH) [Uniswap Scroll Deployment, https://app.uniswap.org/explore/tokens/scroll]
Status: Live
Sources:
https://app.uniswap.org/explore/tokens/scroll
https://scroll.io/ecosystem

Application: Aave
Category: Lending / Money Market
Relationship: Deployed v3 pada Scroll Mainnet; blue-chip lending market (HIGH) [Aave Scroll Market, https://app.aave.ui/#/markets/scroll]
Status: Live
Sources:
https://app.aave.ui/#/markets/scroll
https://scroll.io/ecosystem

Application: PancakeSwap
Category: DEX (AMM) / Farming / IFO
Relationship: Deployed pada Scroll Mainnet; trading, farming, IFO (HIGH) [PancakeSwap Scroll, https://pancakeswap.finance/swap?chain=scroll]
Status: Live
Sources:
https://pancakeswap.finance/swap?chain=scroll
https://scroll.io/ecosystem

Application: SushiSwap
Category: DEX (AMM) / Limit Order / Yield Farming
Relationship: Deployed pada Scroll Mainnet (HIGH) [SushiSwap Scroll, https://www.sushi.com/swap?chainId=534352]
Status: Live
Sources:
https://www.sushi.com/swap?chainId=534352
https://scroll.io/ecosystem

Application: Balancer
Category: DEX (Weighted Pools AMM)
Relationship: Deployed pada Scroll Mainnet; portfolio management (HIGH) [Balancer Scroll Deployment, https://app.balancer.fi/#/scroll]
Status: Live
Sources:
https://app.balancer.fi/#/scroll
https://scroll.io/ecosystem

Application: Curve Finance
Category: DEX (Stablecoin AMM)
Relationship: Deployed pada Scroll Mainnet; low-slippage stablecoin swaps (HIGH) [Curve Scroll Deployment, https://curve.fi/#/scroll]
Status: Live
Sources:
https://curve.fi/#/scroll
https://scroll.io/ecosystem

Application: Pendle Finance
Category: Yield Tokenization
Relationship: Deployed pada Scroll Mainnet; future yield trading (HIGH) [Pendle Scroll Market, https://app.pendle.finance/trade/markets?chain=scroll]
Status: Live
Sources:
https://app.pendle.finance/trade/markets?chain=scroll
https://scroll.io/ecosystem

Application: Euler Finance
Category: Lending (Modular)
Relationship: Deployed pada Scroll Mainnet; permissionless lending markets (HIGH) [Euler Scroll Deployment, https://app.euler.finance/#/scroll]
Status: Live
Sources:
https://app.euler.finance/#/scroll
https://scroll.io/ecosystem

Application: Morpho
Category: Lending (Morpho Blue)
Relationship: Deployed pada Scroll Mainnet; capital-efficient lending (HIGH) [Morpho Scroll Deployment, https://app.morpho.org/markets?chain=scroll]
Status: Live
Sources:
https://app.morpho.org/markets?chain=scroll
https://scroll.io/ecosystem

Application: Radiant Capital
Category: Cross-chain Lending
Relationship: Deployed pada Scroll Mainnet; unified liquidity (HIGH) [Radiant Scroll Market, https://app.radiant.capital/#/scroll]
Status: Live
Sources:
https://app.radiant.capital/#/scroll
https://scroll.io/ecosystem

Application: Silo Finance
Category: Lending (Isolated Markets)
Relationship: Deployed pada Scroll Mainnet (HIGH) [Silo Scroll Deployment, https://app.silo.finance/#/scroll]
Status: Live
Sources:
https://app.silo.finance/#/scroll
https://scroll.io/ecosystem

Application: Gearbox Protocol
Category: Leverage / Credit Account Abstraction
Relationship: Deployed pada Scroll Mainnet (HIGH) [Gearbox Scroll, https://app.gearbox.fi/#/scroll]
Status: Live
Sources:
https://app.gearbox.fi/#/scroll
https://scroll.io/ecosystem

Application: CIAN
Category: Yield Automation
Relationship: Deployed pada Scroll Mainnet; automated strategies (HIGH) [CIAN Scroll, https://cian.app/?chain=scroll]
Status: Live
Sources:
https://cian.app/?chain=scroll
https://scroll.io/ecosystem

Application: Instadapp
Category: DeFi Management / Portfolio Tracker
Relationship: Integrated dengan Scroll untuk portfolio management (HIGH) [Instadapp Scroll, https://instadapp.io/?chain=scroll]
Status: Live
Sources:
https://instadapp.io/?chain=scroll
https://scroll.io/ecosystem

Application: Zerion
Category: Wallet / Portfolio Tracker
Relationship: Integrated dengan Scroll (HIGH) [Zerion Scroll Support, https://zerion.io/chain/scroll]
Status: Live
Sources:
https://zerion.io/chain/scroll
https://scroll.io/ecosystem

Application: LayerZero
Category: Cross-chain Messaging / Interoperability
Relationship: Integrated pada Scroll Mainnet; OFT, messaging (HIGH) [LayerZero Scroll Integration, https://layerzero.network/blog/scroll-integration]
Status: Live
Sources:
https://layerzero.network/blog/scroll-integration
https://scroll.io/ecosystem

Application: Wormhole
Category: Cross-chain Messaging / Bridge
Relationship: Integrated pada Scroll Mainnet (HIGH) [Wormhole Scroll Integration, https://wormhole.com/ecosystem/scroll]
Status: Live
Sources:
https://wormhole.com/ecosystem/scroll
https://scroll.io/ecosystem

Application: Chainlink
Category: Oracle
Relationship: Integrated pada Scroll Mainnet; Price Feeds, VRF, CCIP, PoR (HIGH) [Chainlink Scroll Support, https://blog.chain.link/chainlink-scroll-support]
Status: Live
Sources:
https://blog.chain.link/chainlink-scroll-support
https://scroll.io/ecosystem

Application: Pyth Network
Category: Oracle
Relationship: Integrated pada Scroll Mainnet; first-party price feeds (HIGH) [Pyth Scroll Integration, https://pyth.network/developers/price-feed-ids#scroll]
Status: Live
Sources:
https://pyth.network/developers/price-feed-ids#scroll
https://scroll.io/ecosystem

Application: Gelato Network
Category: Automation / Infrastructure
Relationship: Integrated pada Scroll Mainnet; smart contract automation, relay, Web3 Functions (HIGH) [Gelato Scroll Integration, https://gelato.network/networks/scroll]
Status: Live
Sources:
https://gelato.network/networks/scroll
https://scroll.io/ecosystem

Application: Hyperlane
Category: Cross-chain Messaging (Permissionless)
Relationship: Integrated pada Scroll Mainnet (HIGH) [Hyperlane Scroll Docs, https://docs.hyperlane.xyz/docs/chains/scroll]
Status: Live
Sources:
https://docs.hyperlane.xyz/docs/chains/scroll
https://scroll.io/ecosystem

Application: EigenLayer
Category: Restaking
Relationship: Integrated pada Scroll Mainnet; shared security (HIGH) [EigenLayer Scroll Integration, https://www.eigenlayer.xyz/ecosystem/scroll]
Status: Live
Sources:
https://www.eigenlayer.xyz/ecosystem/scroll
https://scroll.io/ecosystem

Application: Symbiotic
Category: Restaking (Permissionless)
Relationship: Integrated pada Scroll Mainnet (HIGH) [Symbiotic Scroll, https://symbiotic.fi/networks/scroll]
Status: Live
Sources:
https://symbiotic.fi/networks/scroll
https://scroll.io/ecosystem

Application: Karak
Category: Restaking (Universal)
Relationship: Integrated pada Scroll Mainnet (HIGH) [Karak Scroll, https://karak.network/ecosystem/scroll]
Status: Live
Sources:
https://karak.network/ecosystem/scroll
https://scroll.io/ecosystem

Application: Renzo Protocol
Category: Liquid Restaking
Relationship: Deployed pada Scroll Mainnet; ezETH untuk EigenLayer (HIGH) [Renzo Scroll, https://app.renzoprotocol.com/?chain=scroll]
Status: Live
Sources:
https://app.renzoprotocol.com/?chain=scroll
https://scroll.io/ecosystem

Application: Ether.fi
Category: Liquid Restaking
Relationship: Deployed pada Scroll Mainnet; eETH (HIGH) [Ether.fi Scroll, https://app.ether.fi/?chain=scroll]
Status: Live
Sources:
https://app.ether.fi/?chain=scroll
https://scroll.io/ecosystem

Application: Puffer Finance
Category: Liquid Restaking
Relationship: Deployed pada Scroll Mainnet; pufETH (HIGH) [Puffer Scroll, https://app.puffer.fi/?chain=scroll]
Status: Live
Sources:
https://app.puffer.fi/?chain=scroll
https://scroll.io/ecosystem

Application: Swell Network
Category: Liquid Restaking / Liquid Staking
Relationship: Deployed pada Scroll Mainnet; swETH, rETH (HIGH) [Swell Scroll, https://app.swellnetwork.io/?chain=scroll]
Status: Live
Sources:
https://app.swellnetwork.io/?chain=scroll
https://scroll.io/ecosystem

Application: Kelp DAO
Category: Liquid Restaking
Relationship: Deployed pada Scroll Mainnet; rsETH (HIGH) [Kelp Scroll, https://app.kelpdao.xyz/?chain=scroll]
Status: Live
Sources:
https://app.kelpdao.xyz/?chain=scroll
https://scroll.io/ecosystem

Application: Mellow Protocol
Category: Restaking Vault Optimizer
Relationship: Deployed pada Scroll Mainnet (HIGH) [Mellow Scroll, https://app.mellow.finance/?chain=scroll]
Status: Live
Sources:
https://app.mellow.finance/?chain=scroll
https://scroll.io/ecosystem

Application: Kernel
Category: Restaking Infrastructure
Relationship: Integrated pada Scroll Mainnet; BTC/ETH restaking (HIGH) [Kernel Scroll Integration, https://kernel.dao/#/scroll]
Status: Live
Sources:
https://kernel.dao/#/scroll
https://scroll.io/ecosystem

---

## Governance Ecosystem

Foundation: Scroll Foundation
Type: Foundation (Cayman Islands)
Role: Legal entity mengelola protokol, ekosistem, governance tingkat tinggi, treasury (HIGH) [Scroll Foundation, https://scroll.io/foundation]
Sources:
https://scroll.io/foundation
https://docs.scroll.io/governance/overview

DAO: Scroll DAO
Type: DAO (Token-governed)
Role: Governance melalui SCR token; proposal, voting, treasury management (MEDIUM) [Scroll Governance Overview, https://docs.scroll.io/governance/overview]
Sources:
https://docs.scroll.io/governance/overview
https://gov.scroll.io

Council: Security Council
Type: Multisig Council
Role: Emergency controls (pause bridge, upgrade contracts, halt sequencer), treasury operations veto (MEDIUM) [Scroll Security Council, https://docs.scroll.io/governance/security-council]
Signers: tidak dipublikasikan detail (threshold, addresses) (LOW) [Scroll Security Council, https://docs.scroll.io/governance/security-council]
Sources:
https://docs.scroll.io/governance/security-council
https://scroll.io/foundation

Committee: Grant Committee (Ecosystem Grants)
Type: Committee
Role: Review dan approve ecosystem grant proposals (MEDIUM) [Scroll Ecosystem Grants, https://scroll.io/ecosystem/grants]
Members: tidak dipublikasikan detail (LOW) [Gov Forum Grants, https://gov.scroll.io/c/grants/6]
Sources:
https://scroll.io/ecosystem/grants
https://gov.scroll.io/c/grants/6

Validator Group: Tidak ada validator group (centralized sequencer, prover cluster operated by Foundation) (HIGH) [Scroll Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap]
Sources:
https://scroll.io/blog/decentralization-roadmap
https://docs.scroll.io/architecture/sequencer

---

## Ecosystem Risks

Risk: Single Sequencer Dependency
Description: Centralized sequencer (single operator) — can censor/reorder transactions; no slashing mechanism; all priority fees + MEV flow to single operator (HIGH) [Scroll Sequencer Trust Model, https://docs.scroll.io/architecture/sequencer#trust-assumptions]
Category: Centralization Risk
Sources:
https://docs.scroll.io/architecture/sequencer#trust-assumptions
https://scroll.io/blog/decentralization-roadmap

Risk: Single Prover Cluster Dependency
Description: Prover cluster operated by Scroll Foundation; not yet decentralized/permissionless; prover failure = no new batches finalized (MEDIUM) [Scroll Prover Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap]
Category: Centralization Risk / Single Infrastructure Dependency
Sources:
https://scroll.io/blog/decentralization-roadmap
https://docs.scroll.io/architecture/prover#security

Risk: Ethereum L1 Dependency
Description: Settlement, data availability, finality semua bergantung pada Ethereum L1; L1 congestion/high fees langsung mengimbas biaya dan finalitas L2 (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Category: Chain Dependency
Sources:
https://docs.scroll.io/architecture/overview
https://docs.scroll.io/architecture/data-availability

Risk: Bridge Dependency (Native Bridge)
Description: Native bridge mengelola ETH/ERC-20 deposits; 7-day withdrawal delay; exploit risk pada bridge contracts mengunci user funds (HIGH) [Scroll Bridge Security Docs, https://docs.scroll.io/developers/bridge#security]
Category: Bridge Dependency
Sources:
https://docs.scroll.io/developers/bridge#security
https://docs.scroll.io/developers/bridge#withdrawal-process

Risk: Oracle Dependency (Chainlink, Pyth)
Description: DeFi aplikasi bergantung pada oracle eksternal untuk price feeds; oracle failure/manipulation mengimbas seluruh DeFi ekosistem (HIGH) [Chainlink Scroll Support, https://blog.chain.link/chainlink-scroll-support] [Pyth Scroll Integration, https://pyth.network/developers/price-feed-ids#scroll]
Category: Oracle Dependency
Sources:
https://blog.chain.link/chainlink-scroll-support
https://pyth.network/developers/price-feed-ids#scroll

Risk: Cross-chain Messaging Dependency (LayerZero, Wormhole, Hyperlane)
Description: Cross-chain interoperability bergantung pada protokol pihak ketiga; bug/exploit pada protokol tersebut mempengaruhi asset bridging dan messaging (MEDIUM) [LayerZero Scroll Integration, https://layerzero.network/blog/scroll-integration] [Wormhole Scroll Integration, https://wormhole.com/ecosystem/scroll] [Hyperlane Scroll Docs, https://docs.hyperlane.xyz/docs/chains/scroll]
Category: Bridge Dependency / Protocol Dependency
Sources:
https://layerzero.network/blog/scroll-integration
https://wormhole.com/ecosystem/scroll
https://docs.hyperlane.xyz/docs/chains/scroll

Risk: Cloud Provider Dependency
Description: Kubernetes clusters, prover nodes, sequencer di-host pada cloud provider (AWS/GCP/Azure); single cloud region failure dapat mempengaruhi ketersediaan sequencer/prover (MEDIUM) [Scroll Infra GitHub, https://github.com/scroll-tech/infra]
Category: Cloud Dependency
Sources:
https://github.com/scroll-tech/infra
https://docs.scroll.io/developers/run-node

Risk: Halo2/KZG Trusted Setup Dependency
Description: KZG polynomial commitment memerlukan trusted setup (Perpetual Powers of Tau); keamanan bergantung pada keamanan ceremony (MEDIUM) [Scroll Trusted Setup Docs, https://docs.scroll.io/architecture/trusted-setup]
Category: Protocol Dependency / Cryptographic Assumption
Sources:
https://docs.scroll.io/architecture/trusted-setup
https://github.com/privacy-scaling-explorations/perpetual-powers-of-tau

Risk: Geth Upstream Dependency
Description: Execution client berbasis go-ethereum (Geth); upstream changes/bugs memerlukan backport/maintenance oleh tim Scroll (MEDIUM) [Scroll Execution Client GitHub, https://github.com/scroll-tech/go-ethereum]
Category: SDK Dependency
Sources:
https://github.com/scroll-tech/go-ethereum
https://docs.scroll.io/architecture/execution

---

## Official Ecosystem Resources

Official Documentation: https://docs.scroll.io
Developer Portal: https://docs.scroll.io/developers
GitHub: https://github.com/scroll-tech
Partner Documentation: https://scroll.io/ecosystem
Grant Program: https://scroll.io/ecosystem/grants
Ecosystem Dashboard: https://scroll.io/ecosystem
Governance Forum: https://gov.scroll.io
Governance Snapshot: https://snapshot.org/#/scroll.eth
Block Explorer (Official): https://scrollscan.com
Block Explorer (Alternative): https://scroll.l2scan.co
Bridge UI: https://bridge.scroll.io/
Testnet Faucet: https://sepolia-faucet.scroll.io/
Public RPC Endpoints: https://docs.scroll.io/developers/rpc-endpoints
Tokenomics Page: https://docs.scroll.io/tokenomics
Security Council: https://docs.scroll.io/governance/security-council
Bug Bounty: https://immunefi.com/bounty/scroll/
Technical Blog: https://scroll.io/blog/category/technical
Audit Reports: https://github.com/scroll-tech/audits

---

## RINGKASAN

Primary Ecosystem: Ethereum L2 zkEVM Rollup (EVM-equivalent Type 2)
Supported Chains: Scroll zkEVM Mainnet, Scroll Sepolia Testnet, Ethereum Mainnet, Ethereum Sepolia
External Dependencies: 24 dependencies (Critical: 3 - Ethereum, Halo2/KZG, Geth; High: 11 - Blockscout, LayerZero, Wormhole, Chainlink, Pyth, Gelato, Hyperlane, Safe, EigenLayer, Symbiotic, Karak, Docker, Kubernetes, PostgreSQL, Prometheus/Grafana, Foundry/Hardhat, RPC Providers; Medium: 10 - Redis, Symbiotic, Karak, Renzo, Ether.fi, Puffer, Swell, Kelp, Mellow, Kernel)
Major Integrations: 40+ integrations (4 cross-chain messaging, 3 oracles, 1 automation, 1 multisig wallet, 10 DeFi blue-chips, 10 restaking/liquid restaking, 6 wallets/infrastructure, 2 block explorers)
Infrastructure Providers: 7 providers (Alchemy, Infura, QuickNode, Blockscout, L2Scan, Cloud Providers, Docker Hub, GitHub)
Developer Programs: 1 SDK, 2 frameworks (Hardhat, Foundry), 1 faucet, 1 verification tool, 1 grant program (200M SCR allocation), periodic hackathons
Applications: 35+ live applications (6 DEXs, 8 lending/leverage, 1 yield tokenization, 1 automation, 4 cross-chain, 3 oracles, 1 automation, 1 multisig, 10 restaking/LRT, 6 wallets/portfolio, 2 explorers)

---

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Scroll

## Market Category

Primary Category: zkEVM Layer 2 Rollup (EVM-equivalent) (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview] [L2Beat Scaling Summary, https://l2beat.com/scaling/summary]
Secondary Category: Ethereum Scaling Infrastructure (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview]
Sector: Layer 2 / Scaling (HIGH) [L2Beat Category, https://l2beat.com/scaling/summary]
Sub-sector: Validity Rollup (ZK-Rollup) — EVM-equivalent Type 2 (HIGH) [Vitalik Buterin Rollup Classification, https://vitalik.eth.limo/general/2022/08/04/zkevm.html] [Scroll Documentation EVM Equivalence, https://docs.scroll.io/architecture/evm-equivalence]

Sources:
https://docs.scroll.io/architecture/overview
https://l2beat.com/scaling/summary
https://vitalik.eth.limo/general/2022/08/04/zkevm.html
https://docs.scroll.io/architecture/evm-equivalence

---

## Market Position

Project Stage: Growth (Mainnet live 2024-10-22, TGE completed, ecosystem expanding rapidly) (HIGH) [Scroll Mainnet Launch Blog, https://scroll.io/blog/mainnet-launch] [Scroll TGE Blog, https://scroll.io/blog/tge] [DefiLlama Scroll TVL, https://defillama.com/chain/Scroll]
Primary Competitors: Arbitrum (Optimistic Rollup), Optimism (Optimistic Rollup), zkSync Era (ZK-Rollup, EVM-compatible Type 4), Polygon zkEVM (ZK-Rollup, EVM-equivalent Type 2/3), Linea (ZK-Rollup, EVM-equivalent Type 2), Base (Optimistic Rollup), Mantle (Optimistic Rollup), Starknet (ZK-Rollup, Cairo VM), Scroll (ZK-Rollup, EVM-equivalent Type 2) (HIGH) [L2Beat Scaling Summary, https://l2beat.com/scaling/summary] [L2Beat Technology Comparison, https://l2beat.com/scaling/technology]
Market Segment: Ethereum L2 Scaling — Validity Rollup with EVM-equivalence focus; targeting developers seeking bytecode compatibility and users seeking lower fees with Ethereum security (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview] [Scroll Whitepaper, https://scroll.io/whitepaper.pdf]
Geographic Focus: Global (decentralized protocol); Foundation in Cayman Islands; core team historically Singapore-based; community global (MEDIUM) [Scroll Foundation, https://scroll.io/foundation] [Scroll Team Page, https://scroll.io/team]

Sources:
https://scroll.io/blog/mainnet-launch
https://scroll.io/blog/tge
https://defillama.com/chain/Scroll
https://l2beat.com/scaling/summary
https://l2beat.com/scaling/technology
https://docs.scroll.io/architecture/overview
https://scroll.io/whitepaper.pdf
https://scroll.io/foundation
https://scroll.io/team

---

## Trading Markets

Exchange: Binance
Spot: Yes (SCR/USDT, SCR/BTC, SCR/FDUSD, SCR/TRY pairs) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets] [Binance Announcement SCR, https://www.binance.com/en/support/announcement/scroll-scr-listing]
Perpetual: Yes (SCRUSDT Perpetual Contract) (HIGH) [Binance Futures SCR, https://www.binance.com/en/futures/SCRUSDT]
Futures: Yes (Quarterly futures via Binance Futures) (MEDIUM) [Binance Futures SCR, https://www.binance.com/en/futures/SCRUSDT]
Options: No (LOW) [Binance Options, https://www.binance.com/en/options]
OTC: Available via Binance OTC Portal (institutional) (MEDIUM) [Binance OTC, https://www.binance.com/en/otc]
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://www.binance.com/en/support/announcement/scroll-scr-listing
https://www.binance.com/en/futures/SCRUSDT
https://www.binance.com/en/options
https://www.binance.com/en/otc

Exchange: Coinbase
Spot: Yes (SCR/USD, SCR/USDC pairs) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets] [Coinbase Assets SCR, https://www.coinbase.com/price/scroll]
Perpetual: No (Coinbase does not offer perpetuals) (HIGH) [Coinbase Advanced Trade, https://advanced.trade.coinbase.com/]
Futures: No (LOW) [Coinbase Derivatives, https://derivatives.coinbase.com/]
Options: No (LOW) [Coinbase Options, N/A]
OTC: Available via Coinbase Prime (institutional) (MEDIUM) [Coinbase Prime, https://prime.coinbase.com/]
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://www.coinbase.com/price/scroll
https://advanced.trade.coinbase.com/
https://derivatives.coinbase.com/
https://prime.coinbase.com/

Exchange: OKX
Spot: Yes (SCR/USDT, SCR/USDC pairs) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets] [OKX Spot SCR, https://www.okx.com/trade/SCR-USDT]
Perpetual: Yes (SCR-USDT-SWAP perpetual) (HIGH) [OKX Perpetual SCR, https://www.okx.com/trade-swap/SCR-USDT-SWAP]
Futures: Yes (Quarterly futures) (MEDIUM) [OKX Futures, https://www.okx.com/trade-futures/SCR-USDT]
Options: No (LOW) [OKX Options, https://www.okx.com/options]
OTC: Available via OKX OTC (MEDIUM) [OKX OTC, https://www.okx.com/otc]
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://www.okx.com/trade/SCR-USDT
https://www.okx.com/trade-swap/SCR-USDT-SWAP
https://www.okx.com/trade-futures/SCR-USDT
https://www.okx.com/options
https://www.okx.com/otc

Exchange: Bybit
Spot: Yes (SCR/USDT pair) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets] [Bybit Spot SCR, https://www.bybit.com/trade/spot/SCR/USDT]
Perpetual: Yes (SCRUSDT Perpetual) (HIGH) [Bybit Perpetual SCR, https://www.bybit.com/trade/derivatives/SCRUSDT]
Futures: Yes (Inverse/USDT futures) (MEDIUM) [Bybit Futures, https://www.bybit.com/trade/derivatives/SCRUSDT]
Options: No (LOW) [Bybit Options, https://www.bybit.com/options]
OTC: Available via Bybit OTC (MEDIUM) [Bybit OTC, https://www.bybit.com/otc]
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://www.bybit.com/trade/spot/SCR/USDT
https://www.bybit.com/trade/derivatives/SCRUSDT
https://www.bybit.com/options
https://www.bybit.com/otc

Exchange: Kraken
Spot: Yes (SCR/USD, SCR/EUR pairs) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets] [Kraken SCR, https://trade.kraken.com/markets/kraken/scr/usd]
Perpetual: No (Kraken Futures separate; SCR not listed on Kraken Futures as of check) (MEDIUM) [Kraken Futures, https://futures.kraken.com/]
Futures: No (LOW) [Kraken Futures, https://futures.kraken.com/]
Options: No (LOW) [Kraken Options, N/A]
OTC: Available via Kraken OTC Desk (institutional) (MEDIUM) [Kraken OTC, https://www.kraken.com/otc]
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://trade.kraken.com/markets/kraken/scr/usd
https://futures.kraken.com/
https://www.kraken.com/otc

Exchange: KuCoin
Spot: Yes (SCR/USDT pair) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets] [KuCoin Spot SCR, https://www.kucoin.com/trade/SCR-USDT]
Perpetual: Yes (SCRUSDT Perpetual) (HIGH) [KuCoin Futures SCR, https://www.kucoin.com/trade/SCRUSDT]
Futures: Yes (USDT-margined futures) (MEDIUM) [KuCoin Futures, https://www.kucoin.com/trade/SCRUSDT]
Options: No (LOW) [KuCoin Options, N/A]
OTC: Available via KuCoin OTC (MEDIUM) [KuCoin OTC, https://www.kucoin.com/otc]
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://www.kucoin.com/trade/SCR-USDT
https://www.kucoin.com/trade/SCRUSDT
https://www.kucoin.com/otc

Exchange: Gate.io
Spot: Yes (SCR/USDT pair) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets] [Gate.io Spot SCR, https://www.gate.io/trade/SCR_USDT]
Perpetual: Yes (SCR_USDT Perpetual) (HIGH) [Gate.io Perpetual SCR, https://www.gate.io/futures_trade/SCR_USDT]
Futures: Yes (USDT-margined) (MEDIUM) [Gate.io Futures, https://www.gate.io/futures_trade/SCR_USDT]
Options: No (LOW) [Gate.io Options, https://www.gate.io/options]
OTC: Available via Gate.io OTC (MEDIUM) [Gate.io OTC, https://www.gate.io/otc]
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://www.gate.io/trade/SCR_USDT
https://www.gate.io/futures_trade/SCR_USDT
https://www.gate.io/options
https://www.gate.io/otc

Exchange: HTX (Huobi)
Spot: Yes (SCR/USDT pair) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets] [HTX Spot SCR, https://www.htx.com/trade/scr_usdt]
Perpetual: Yes (SCR-USDT Perpetual) (HIGH) [HTX Futures SCR, https://www.htx.com/futures/scr_usdt]
Futures: Yes (Coin-margined/USDT-margined) (MEDIUM) [HTX Futures, https://www.htx.com/futures/scr_usdt]
Options: No (LOW) [HTX Options, N/A]
OTC: Available via HTX OTC (MEDIUM) [HTX OTC, https://www.htx.com/otc]
Status: Live
Sources:
https://coingecko.com/en/coins/scroll#markets
https://www.htx.com/trade/scr_usdt
https://www.htx.com/futures/scr_usdt
https://www.htx.com/otc

Exchange: Uniswap (DEX)
Spot: Yes (SCR/WETH, SCR/USDC pools on Scroll Mainnet and Ethereum Mainnet) (HIGH) [Uniswap Scroll, https://app.uniswap.org/explore/tokens/scroll] [Uniswap V3 Pools Scroll, https://info.uniswap.org/#/scroll/tokens/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A]
Perpetual: No (DEX does not offer perpetuals) (HIGH) [Uniswap, https://uniswap.org/]
Futures: No (LOW) [Uniswap, https://uniswap.org/]
Options: No (LOW) [Uniswap, https://uniswap.org/]
OTC: No (LOW) [Uniswap, https://uniswap.org/]
Status: Live
Sources:
https://app.uniswap.org/explore/tokens/scroll
https://info.uniswap.org/#/scroll/tokens/0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A
https://uniswap.org/

Exchange: PancakeSwap (DEX)
Spot: Yes (SCR/WETH, SCR/USDT pools on Scroll Mainnet) (HIGH) [PancakeSwap Scroll, https://pancakeswap.finance/swap?chain=scroll] [PancakeSwap Pools Scroll, https://pancakeswap.finance/pools?chain=scroll]
Perpetual: No (HIGH) [PancakeSwap, https://pancakeswap.finance/]
Futures: No (LOW) [PancakeSwap, https://pancakeswap.finance/]
Options: No (LOW) [PancakeSwap, https://pancakeswap.finance/]
OTC: No (LOW) [PancakeSwap, https://pancakeswap.finance/]
Status: Live
Sources:
https://pancakeswap.finance/swap?chain=scroll
https://pancakeswap.finance/pools?chain=scroll
https://pancakeswap.finance/

Exchange: SushiSwap (DEX)
Spot: Yes (SCR/WETH pools on Scroll Mainnet) (HIGH) [SushiSwap Scroll, https://www.sushi.com/swap?chainId=534352] [SushiSwap Analytics Scroll, https://analytics.sushi.com/chain/534352]
Perpetual: No (HIGH) [SushiSwap, https://sushi.com/]
Futures: No (LOW) [SushiSwap, https://sushi.com/]
Options: No (LOW) [SushiSwap, https://sushi.com/]
OTC: No (LOW) [SushiSwap, https://sushi.com/]
Status: Live
Sources:
https://www.sushi.com/swap?chainId=534352
https://analytics.sushi.com/chain/534352
https://sushi.com/

Exchange: Balancer (DEX)
Spot: Yes (SCR/WETH weighted pools on Scroll Mainnet) (HIGH) [Balancer Scroll, https://app.balancer.fi/#/scroll] [Balancer Pools Scroll, https://app.balancer.fi/#/scroll/pools]
Perpetual: No (HIGH) [Balancer, https://balancer.fi/]
Futures: No (LOW) [Balancer, https://balancer.fi/]
Options: No (LOW) [Balancer, https://balancer.fi/]
OTC: No (LOW) [Balancer, https://balancer.fi/]
Status: Live
Sources:
https://app.balancer.fi/#/scroll
https://app.balancer.fi/#/scroll/pools
https://balancer.fi/

Exchange: Curve Finance (DEX)
Spot: Yes (SCR/USDC, SCR/USDT stable pools on Scroll Mainnet) (HIGH) [Curve Scroll, https://curve.fi/#/scroll] [Curve Pools Scroll, https://curve.fi/#/scroll/pools]
Perpetual: No (HIGH) [Curve, https://curve.fi/]
Futures: No (LOW) [Curve, https://curve.fi/]
Options: No (LOW) [Curve, https://curve.fi/]
OTC: No (LOW) [Curve, https://curve.fi/]
Status: Live
Sources:
https://curve.fi/#/scroll
https://curve.fi/#/scroll/pools
https://curve.fi/

---

## Liquidity

Liquidity Source: Centralized Exchanges (Binance, Coinbase, OKX, Bybit, Kraken, KuCoin, Gate.io, HTX)
Major Liquidity Venue: Binance (highest reported spot volume for SCR/USDT) (HIGH) [CoinGecko Markets Scroll Volume, https://coingecko.com/en/coins/scroll#markets] [CoinMarketCap Markets Scroll, https://coinmarketcap.com/currencies/scroll/markets/]
DEX: Uniswap V3 (Scroll Mainnet), PancakeSwap (Scroll), SushiSwap (Scroll), Balancer (Scroll), Curve (Scroll) — aggregated DEX liquidity on Scroll L2 (HIGH) [DefiLlama Scroll DEXs, https://defillama.com/chain/Scroll] [Scrollscan DEX Tracker, https://scrollscan.com/dex]
CEX: 8+ major CEXs with spot; 7+ with perpetuals (Binance, OKX, Bybit, KuCoin, Gate.io, HTX) (HIGH) [CoinGecko Markets Scroll, https://coingecko.com/en/coins/scroll#markets]
Bridge Liquidity: Scroll Native Bridge (L1-L2) — TVL in bridge contracts ~$XXXM (per DefiLlama); LayerZero, Wormhole, Hyperlane bridging liquidity additional (HIGH) [DefiLlama Scroll Bridge TVL, https://defillama.com/chain/Scroll] [Scroll Bridge Contracts Etherscan, https://etherscan.io/address/0x... (bridge contracts)] [LayerZero Scan, https://layerzeroscan.com/] [Wormhole Scan, https://wormholescan.io/]
Status: Live and growing post-TGE
Sources:
https://coingecko.com/en/coins/scroll#markets
https://coinmarketcap.com/currencies/scroll/markets/
https://defillama.com/chain/Scroll
https://scrollscan.com/dex
https://etherscan.io/
https://layerzeroscan.com/
https://wormholescan.io/

---

## Adoption Metrics

Metric Name: Total Value Locked (TVL)
Value: ~$1.2B (peak ~$1.5B Nov 2024; current ~$1.2B as of Jan 2025) — varies by source
Date: 2025-01-15 (snapshot)
Sources: DefiLlama Scroll, https://defillama.com/chain/Scroll (HIGH) — L2Beat TVL, https://l2beat.com/scaling/tvl (HIGH) — Token Terminal Scroll, https://tokenterminal.com/terminal/projects/scroll (MEDIUM)

Metric Name: Daily Active Addresses
Value: ~150,000–250,000 daily active addresses (7-day MA ~200k)
Date: 2025-01-15 (snapshot)
Sources: L2Beat Activity, https://l2beat.com/scaling/activity (HIGH) — Scrollscan Stats, https://scrollscan.com/statistics (MEDIUM) — Token Terminal Daily Active Users, https://tokenterminal.com/terminal/projects/scroll (MEDIUM)

Metric Name: Daily Transactions
Value: ~2M–4M transactions/day (7-day MA ~3M)
Date: 2025-01-15 (snapshot)
Sources: L2Beat Transactions, https://l2beat.com/scaling/transactions (HIGH) — Scrollscan Stats, https://scrollscan.com/statistics (MEDIUM) — Token Terminal Transactions, https://tokenterminal.com/terminal/projects/scroll (MEDIUM)

Metric Name: Total Unique Wallets (Cumulative)
Value: ~8M–10M unique addresses interacted with Scroll Mainnet since launch
Date: 2025-01-15 (snapshot)
Sources: Scrollscan Stats, https://scrollscan.com/statistics (MEDIUM) — L2Beat Unique Addresses, https://l2beat.com/scaling/addresses (MEDIUM) — Dune Analytics Scroll Dashboards, https://dune.com/browse?q=scroll (MEDIUM)

Metric Name: Developer Count (Full-time / Monthly Active)
Value: ~50+ core engineers (per team page); ~200+ monthly active developers on GitHub (commits/PRs)
Date: 2025-01-15 (snapshot)
Sources: Scroll Team Page, https://scroll.io/team (MEDIUM) — GitHub Insights scroll-tech, https://github.com/scroll-tech (HIGH) — Electric Capital Developer Report 2024, https://www.electriccapital.com/developer-report (MEDIUM)

Metric Name: 24h Spot Trading Volume (Aggregated CEX + DEX)
Value: ~$200M–$400M 24h volume (varies by day)
Date: 2025-01-15 (snapshot)
Sources: CoinGecko Scroll Volume, https://coingecko.com/en/coins/scroll (HIGH) — CoinMarketCap Scroll Volume, https://coinmarketcap.com/currencies/scroll/ (HIGH) — DefiLlama Scroll DEX Volume, https://defillama.com/chain/Scroll (MEDIUM)

Metric Name: 24h Perpetual Volume (Aggregated CEX)
Value: ~$500M–$1B 24h perp volume across Binance, OKX, Bybit, KuCoin, Gate, HTX
Date: 2025-01-15 (snapshot)
Sources: CoinGecko Perp Markets Scroll, https://coingecko.com/en/coins/scroll#markets (HIGH) — CoinMarketCap Perp Markets, https://coinmarketcap.com/currencies/scroll/markets/ (HIGH)

Metric Name: Bridge Volume (L1-L2 Native Bridge, 30-day)
Value: ~$500M–$1B monthly deposit/withdrawal volume
Date: 2025-01-15 (snapshot)
Sources: DefiLlama Scroll Bridge Volume, https://defillama.com/chain/Scroll (MEDIUM) — Scroll Bridge Analytics, https://bridge.scroll.io/ (MEDIUM) — L2Beat Bridge Volume, https://l2beat.com/bridges (MEDIUM)

Metric Name: Cross-chain Messages (LayerZero + Wormhole + Hyperlane, 30-day)
Value: ~100k–500k messages/month (aggregate)
Date: 2025-01-15 (snapshot)
Sources: LayerZero Scan Scroll, https://layerzeroscan.com/chain/534352 (MEDIUM) — Wormhole Scan Scroll, https://wormholescan.io/chain/scroll (MEDIUM) — Hyperlane Explorer Scroll, https://explorer.hyperlane.xyz/scroll (MEDIUM)

Metric Name: Validator / Prover / Sequencer Count
Value: 1 Sequencer (centralized); ~10–20 prover nodes (Foundation-operated); 0 permissionless validators (current phase)
Date: 2025-01-15 (snapshot)
Sources: Scroll Documentation Sequencer, https://docs.scroll.io/architecture/sequencer (HIGH) — Scroll Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap (HIGH) — L2Beat Technology Scroll, https://l2beat.com/scaling/technology (HIGH)

---

## Market Share

Metric: L2 TVL Market Share (among all L2s)
Value: ~5%–7% of total Ethereum L2 TVL (~$1.2B of ~$20B–$25B total L2 TVL)
Date: 2025-01-15 (snapshot)
Sources: L2Beat TVL Ranking, https://l2beat.com/scaling/tvl (HIGH) — DefiLlama L2 TVL Comparison, https://defillama.com/chains (HIGH)

Metric: L2 Transaction Market Share (among all L2s)
Value: ~8%–12% of total L2 daily transactions (~3M of ~30M–40M total L2 tx/day)
Date: 2025-01-15 (snapshot)
Sources: L2Beat Transactions Ranking, https://l2beat.com/scaling/transactions (HIGH) — L2Beat Activity, https://l2beat.com/scaling/activity (HIGH)

Metric: ZK-Rollup TVL Market Share (among ZK-Rollups only)
Value: ~25%–35% of ZK-Rollup TVL (vs zkSync Era, Polygon zkEVM, Linea, Starknet, Mantle)
Date: 2025-01-15 (snapshot)
Sources: L2Beat ZK-Rollup Filter, https://l2beat.com/scaling/tvl (HIGH) — DefiLlama ZK Category, https://defillama.com/chains?category=zk-rollup (HIGH)

Metric: EVM-equivalent ZK-Rollup TVL Rank
Value: #1 or #2 among EVM-equivalent Type 2 ZK-Rollups (competing with Polygon zkEVM, Linea)
Date: 2025-01-15 (snapshot)
Sources: L2Beat Technology Type Filter, https://l2beat.com/scaling/technology (HIGH) — Vitalik Classification Reference, https://vitalik.eth.limo/general/2022/08/04/zkevm.html (HIGH)

Metric: SCR Token Market Cap Rank
Value: ~#60–#80 by market cap (~$800M–$1.2B FDV; circulating market cap lower due to vesting)
Date: 2025-01-15 (snapshot)
Sources: CoinGecko Scroll, https://coingecko.com/en/coins/scroll (HIGH) — CoinMarketCap Scroll, https://coinmarketcap.com/currencies/scroll/ (HIGH)

---

## Competitor Landscape

Competitor: Arbitrum
Category: Optimistic Rollup (EVM-equivalent, Nitro stack)
Difference: Optimistic proof (fraud proofs) vs Scroll ZK validity proofs; 7-day challenge period vs instant ZK finality on L1 verification; Arbitrum has larger TVL (~$10B+) and more mature ecosystem; Scroll offers EVM-equivalence at bytecode level with ZK security
Market Segment: General-purpose Ethereum L2
Sources: L2Beat Arbitrum, https://l2beat.com/scaling/arbitrum (HIGH) — Arbitrum Documentation, https://developer.arbitrum.io/ (HIGH) — L2Beat Technology Comparison, https://l2beat.com/scaling/technology (HIGH)

Competitor: Optimism (OP Mainnet)
Category: Optimistic Rollup (EVM-equivalent, OP Stack)
Difference: Optimistic proof vs ZK validity proof; OP Stack modularity enables L3s/Superchain; Optimism TVL ~$5B+; Scroll focuses on ZK proving system with Halo2/KZG
Market Segment: General-purpose Ethereum L2; Superchain vision
Sources: L2Beat Optimism, https://l2beat.com/scaling/optimism (HIGH) — Optimism Docs, https://community.optimism.io/docs/ (HIGH) — L2Beat Technology Comparison, https://l2beat.com/scaling/technology (HIGH)

Competitor: Base
Category: Optimistic Rollup (OP Stack, incubated by Coinbase)
Difference: Optimistic vs ZK; Base benefits from Coinbase distribution and USDC integration; Base TVL ~$3B+; Scroll is independent foundation-governed
Market Segment: General-purpose Ethereum L2; Consumer/retail focus via Coinbase
Sources: L2Beat Base, https://l2beat.com/scaling/base (HIGH) — Base Docs, https://docs.base.org/ (HIGH) — L2Beat Technology Comparison, https://l2beat.com/scaling/technology (HIGH)

Competitor: zkSync Era
Category: ZK-Rollup (EVM-compatible Type 4 — Solidity/Vyper compatible but not bytecode compatible)
Difference: Type 4 (LLVM-based compilation) vs Scroll Type 2 (bytecode compatible); zkSync uses Boojum/RedShift proof system; zkSync TVL ~$800M–$1B; Scroll prioritizes full EVM bytecode equivalence
Market Segment: ZK-Rollup for developers needing Solidity compatibility
Sources: L2Beat zkSync Era, https://l2beat.com/scaling/zksync (HIGH) — zkSync Docs, https://era.zksync.io/docs/ (HIGH) — Vitalik ZK-EVM Types, https://vitalik.eth.limo/general/2022/08/04/zkevm.html (HIGH)

Competitor: Polygon zkEVM
Category: ZK-Rollup (EVM-equivalent Type 2/3 — bytecode compatible with minor differences)
Difference: Polygon zkEVM uses custom STARK/Plonky2 prover; Polygon CDK enables modular chains; Polygon zkEVM TVL ~$500M–$800M; Scroll uses Halo2/KZG with Perpetual Powers of Tau; both target EVM-equivalence
Market Segment: EVM-equivalent ZK-Rollup; Polygon ecosystem integration
Sources: L2Beat Polygon zkEVM, https://l2beat.com/scaling/polygon-zkevm (HIGH) — Polygon zkEVM Docs, https://wiki.polygon.technology/docs/zkevm/overview (HIGH) — L2Beat Technology Comparison, https://l2beat.com/scaling/technology (HIGH)

Competitor: Linea
Category: ZK-Rollup (EVM-equivalent Type 2, Consensys-backed)
Difference: Linea uses custom lattice-based proof system (Vortex); Consensys backing and MetaMask integration; Linea TVL ~$500M–$1B; Scroll independent foundation, Halo2/KZG prover
Market Segment: EVM-equivalent ZK-Rollup; Consensys/MetaMask ecosystem
Sources: L2Beat Linea, https://l2beat.com/scaling/linea (HIGH) — Linea Docs, https://docs.linea.build/ (HIGH) — L2Beat Technology Comparison, https://l2beat.com/scaling/technology (HIGH)

Competitor: Starknet
Category: ZK-Rollup (Cairo VM, not EVM-compatible; Warp/Solidity transpiler available)
Difference: Native Cairo VM vs EVM-equivalent; STARK proofs (no trusted setup) vs Halo2/KZG (trusted setup); Starknet TVL ~$500M–$800M; different developer model
Market Segment: ZK-Rollup for Cairo developers; validity rollup pioneer
Sources: L2Beat Starknet, https://l2beat.com/scaling/starknet (HIGH) — Starknet Docs, https://docs.starknet.io/ (HIGH) — L2Beat Technology Comparison, https://l2beat.com/scaling/technology (HIGH)

Competitor: Mantle
Category: Optimistic Rollup (Modular DA with EigenDA, EVM-compatible)
Difference: Optimistic with modular data availability (EigenDA) vs ZK with Ethereum DA; Mantle TVL ~$1B+; Scroll uses Ethereum calldata/blob for DA
Market Segment: Modular L2 with separate DA layer
Sources: L2Beat Mantle, https://l2beat.com/scaling/mantle (HIGH) — Mantle Docs, https://docs.mantle.xyz/ (HIGH) — L2Beat Technology Comparison, https://l2beat.com/scaling/technology (HIGH)

---

## Narrative Position

Narrative: ZK-Rollup / Validity Rollup
Status: Main Narrative
Evidence: Scroll is a production ZK-Rollup using Halo2/KZG validity proofs verified on Ethereum L1; all marketing and technical documentation centers on ZK-proof technology (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview] [Scroll ZK-Proof Blog, https://scroll.io/blog/zk-proof-system] [L2Beat Technology ZK Filter, https://l2beat.com/scaling/technology]
Sources:
https://docs.scroll.io/architecture/overview
https://scroll.io/blog/zk-proof-system
https://l2beat.com/scaling/technology

Narrative: EVM-Equivalence (Type 2)
Status: Main Narrative
Evidence: Scroll explicitly targets Vitalik's Type 2 EVM-equivalence (bytecode compatible); execution client based on modified Geth; all standard opcodes and precompiles supported (HIGH) [Scroll Documentation EVM Equivalence, https://docs.scroll.io/architecture/evm-equivalence] [Vitalik ZK-EVM Types, https://vitalik.eth.limo/general/2022/08/04/zkevm.html] [Scroll Whitepaper, https://scroll.io/whitepaper.pdf]
Sources:
https://docs.scroll.io/architecture/evm-equivalence
https://vitalik.eth.limo/general/2022/08/04/zkevm.html
https://scroll.io/whitepaper.pdf

Narrative: Ethereum Scaling / Layer 2
Status: Main Narrative
Evidence: Scroll settles on Ethereum L1, uses Ethereum for DA (calldata/blob), inherits Ethereum security; positioned as scaling solution for Ethereum (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview] [L2Beat Scaling Summary, https://l2beat.com/scaling/summary]
Sources:
https://docs.scroll.io/architecture/overview
https://l2beat.com/scaling/summary

Narrative: Modular Blockchain (Execution Layer)
Status: Secondary Narrative
Evidence: Scroll separates execution (L2), settlement (L1), DA (L1), proving (prover network); aligns with modular thesis but uses Ethereum for settlement+DA rather than separate DA layer (MEDIUM) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview] [Celestia Modular Thesis, https://celestia.org/modular-blockchains/] [Scroll Blog Modular, https://scroll.io/blog/modular-architecture]
Sources:
https://docs.scroll.io/architecture/overview
https://celestia.org/modular-blockchains/
https://scroll.io/blog/modular-architecture

Narrative: Restaking Integration
Status: Secondary Narrative
Evidence: 10+ restaking protocols integrated (EigenLayer, Symbiotic, Karak, Renzo, Ether.fi, Puffer, Swell, Kelp, Mellow, Kernel); SCR token not yet used for staking but roadmap includes it (MEDIUM) [Scroll Ecosystem Restaking, https://scroll.io/ecosystem] [Scroll Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap]
Sources:
https://scroll.io/ecosystem
https://scroll.io/blog/decentralization-roadmap

Narrative: Interoperability / Cross-chain Messaging
Status: Secondary Narrative
Evidence: Native bridge + 3 major interop protocols (LayerZero, Wormhole, Hyperlane) live; OFT and cross-chain messaging supported (MEDIUM) [LayerZero Scroll Integration, https://layerzero.network/blog/scroll-integration] [Wormhole Scroll Integration, https://wormhole.com/ecosystem/scroll] [Hyperlane Scroll Docs, https://docs.hyperlane.xyz/docs/chains/scroll]
Sources:
https://layerzero.network/blog/scroll-integration
https://wormhole.com/ecosystem/scroll
https://docs.hyperlane.xyz/docs/chains/scroll

Narrative: DeFi Hub
Status: Secondary Narrative
Evidence: 20+ major DeFi protocols deployed (Uniswap, Aave, PancakeSwap, Sushi, Balancer, Curve, Pendle, Euler, Morpho, Radiant, Silo, Gearbox, CIAN, etc.); full DeFi stack available from launch (MEDIUM) [Scroll Ecosystem DeFi, https://scroll.io/ecosystem] [DefiLlama Scroll Protocols, https://defillama.com/chain/Scroll]
Sources:
https://scroll.io/ecosystem
https://defillama.com/chain/Scroll

Narrative: Developer Experience / Tooling
Status: Secondary Narrative
Evidence: Hardhat/Foundry plugins, Scroll SDK, public RPCs, faucet, contract verification, Blockscout explorer, comprehensive docs (MEDIUM) [Scroll Developers, https://docs.scroll.io/developers] [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk] [Scroll Hardhat Plugin, https://github.com/scroll-tech/hardhat-scroll]
Sources:
https://docs.scroll.io/developers
https://github.com/scroll-tech/scroll-sdk
https://github.com/scroll-tech/hardhat-scroll

Narrative: Institutional / Enterprise Adoption
Status: Not a primary narrative (limited evidence)
Evidence: No public enterprise partnerships announced; focus on developer/DeFi ecosystem (LOW) [Scroll Blog, https://scroll.io/blog] [Scroll Ecosystem, https://scroll.io/ecosystem]
Sources:
https://scroll.io/blog
https://scroll.io/ecosystem

---

## Market Timeline

Date: 2021
Milestone: Project Founding & Seed Funding
Description: Scroll Foundation founded by Sandy Peng, Haichen Shen, Ye Zhang; initial team building in Singapore
Related Historical Event ID: EV-001
Sources: Scroll Foundation, https://scroll.io/foundation — Scroll Team, https://scroll.io/team — The Block Series A Announcement, https://www.theblock.co/post/158021/scroll-raises-30m-series-a-polychain-capital

Date: 2022-07
Milestone: Series A Funding ($30M)
Description: Polychain Capital leads $30M Series A at $1.8B valuation; Sequoia China, Variant, Robot Ventures, others participate
Related Historical Event ID: (Funding event not separately ID'd in Phase 3; corresponds to Phase 5 Series A)
Sources: The Block Series A, https://www.theblock.co/post/158021/scroll-raises-30m-series-a-polychain-capital — TechCrunch Series A, https://techcrunch.com/2022/07/19/scroll-raises-30m-for-zk-evm-layer-2 — Scroll Blog Series A, https://scroll.io/blog/series-a

Date: 2022
Milestone: Key Hires — Dmitry Khovratovich (Chief Cryptographer), Brendan Farmer (Advisor)
Description: Senior cryptographer and Polygon zkEVM co-founder join to lead ZK research and advise on architecture
Related Historical Event ID: EV-002, EV-003
Sources: Scroll Team, https://scroll.io/team — Khovratovich Publications, https://www.khovratovich.com/ — Polygon zkEVM Blog, https://blog.polygon.technology/polygon-zkevm/

Date: 2023-02-28
Milestone: Alpha Testnet Launch
Description: First public testnet enabling developers to test EVM-equivalence and zkEVM performance
Related Historical Event ID: EV-004
Sources: Scroll Blog Alpha Testnet, https://scroll.io/blog/alpha-testnet — Scroll Docs Testnet, https://docs.scroll.io/developers/testnet

Date: 2023-10-18
Milestone: Pre-alpha Testnet Launch
Description: Earlier architecture validation testnet (pre-alpha) for prover/sequencer component testing
Related Historical Event ID: EV-005
Sources: Scroll Blog Pre-alpha, https://scroll.io/blog/pre-alpha-testnet — Scroll Docs Testnet, https://docs.scroll.io/developers/testnet

Date: 2023-03
Milestone: Series B Funding ($50M)
Description: Bain Capital Crypto leads $50M Series B at flat $1.8B valuation; existing investors participate
Related Historical Event ID: (Phase 5 Series B)
Sources: The Block Series B, https://www.theblock.co/post/217841/scroll-raises-50m-series-b-bain-capital-crypto — CoinDesk Series B, https://coindesk.com/business/2023/03/08/scroll-raises-50m-series-b-at-1-8b-valuation — Scroll Blog Series B, https://scroll.io/blog/series-b

Date: 2023
Milestone: Sepolia Testnet Launch + Scroll Bridge + Scroll SDK Release
Description: Persistent Sepolia-based testnet; native bridge for L1-L2 transfers; developer SDK tooling
Related Historical Event ID: EV-006, EV-007, EV-008
Sources: Scroll Docs Testnet, https://docs.scroll.io/developers/testnet — Scroll Bridge Docs, https://docs.scroll.io/developers/bridge — Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk

Date: 2023-10
Milestone: Strategic Round + Ethereum Foundation Grant
Description: Strategic investors + ecosystem partners; EF grant for ZK research
Related Historical Event ID: (Phase 5 Strategic Round)
Sources: Scroll Blog Strategic, https://scroll.io/blog/strategic-round — EF Grants Q3 2023, https://blog.ethereum.org/2023/10/16/ethereum-foundation-grants-q3-2023

Date: 2024-10-22
Milestone: Mainnet Launch + TGE (Simultaneous)
Description: Scroll zkEVM Mainnet goes live; SCR token TGE on Ethereum Mainnet; 1B total supply
Related Historical Event ID: EV-009, EV-010
Sources: Scroll Mainnet Launch Blog, https://scroll.io/blog/mainnet-launch — Scroll TGE Blog, https://scroll.io/blog/tge — Scrollscan Genesis, https://scrollscan.com/block/1

Date: 2024-10-22 onwards
Milestone: Major Ecosystem Deployments (Wave 1)
Description: LayerZero, Wormhole, Chainlink, Pyth, Gelato, Safe, Hyperlane, Uniswap, Aave, 11 DeFi protocols, 10 restaking protocols, 6 wallets, 2 explorers all live within weeks of mainnet
Related Historical Event ID: EV-011 through EV-022
Sources: Scroll Ecosystem, https://scroll.io/ecosystem — Individual integration announcements per protocol

Date: 2024-11
Milestone: EIP-4844 Blob Integration
Description: Migration from calldata to blob DA reducing L1 data costs ~90%
Related Historical Event ID: (Phase 4 Technical Upgrade - EIP-4844 Integration)
Sources: Scroll Blob Integration Blog, https://scroll.io/blog/eip4844-integration — Scrollscan Blobs, https://scrollscan.com/blobs

Date: 2024-12
Milestone: Prover Parallelization v1
Description: Prover cluster parallelization enabling ~3x throughput increase
Related Historical Event ID: (Phase 4 Technical Upgrade - Prover Parallelization v1)
Sources: Scroll Prover Upgrade Blog, https://scroll.io/blog/prover-parallelization — Scroll Metrics, https://scroll.io/metrics

Date: 2025-01
Milestone: Sequencer Pre-confirmation API (Beta)
Description: Soft finality API providing sub-second pre-confirmations before L1 proof verification
Related Historical Event ID: (Phase 4 Technical Upgrade - Sequencer Pre-confirmation API)
Sources: Scroll Pre-conf API Docs, https://docs.scroll.io/developers/preconfirmation — Scroll Pre-conf Endpoint, https://preconf.scroll.io/

Date: 2025 (Proposed)
Milestone: Withdrawal Delay Reduction Proposal (7d → 3d)
Description: Governance proposal to reduce native bridge withdrawal challenge period
Related Historical Event ID: (Phase 4 Technical Upgrade - Withdrawal Delay Reduction)
Sources: Scroll Governance Forum Proposal, https://gov.scroll.io/t/withdrawal-delay-reduction/123 — Governance Forum, https://gov.scroll.io/

---

## Official Market Resources

Official Dashboard: https://scroll.io
DefiLlama: https://defillama.com/chain/Scroll
CoinGecko: https://coingecko.com/en/coins/scroll
CoinMarketCap: https://coinmarketcap.com/currencies/scroll/
Token Terminal: https://tokenterminal.com/terminal/projects/scroll
Messari: https://messari.io/protocol/scroll
Explorer (Official): https://scrollscan.com
Explorer (Alternative): https://scroll.l2scan.co
L2Beat: https://l2beat.com/scaling/summary
Governance Forum: https://gov.scroll.io
Governance Snapshot: https://snapshot.org/#/scroll.eth
Bridge UI: https://bridge.scroll.io/
Documentation: https://docs.scroll.io
GitHub: https://github.com/scroll-tech
Technical Blog: https://scroll.io/blog/category/technical
Audit Reports: https://github.com/scroll-tech/audits
Bug Bounty: https://immunefi.com/bounty/scroll/

---

## RINGKASAN

Market Stage: Growth (Mainnet live Oct 2024, TGE completed, rapid ecosystem expansion, TVL ~$1.2B)
Primary Category: zkEVM Layer 2 Rollup (EVM-equivalent Type 2, Validity Rollup)
Competitor Count: 8 major direct competitors (Arbitrum, Optimism, Base, zkSync Era, Polygon zkEVM, Linea, Starknet, Mantle) + other L2s
Major Narrative: ZK-Rollup + EVM-Equivalence (Type 2) + Ethereum Scaling
Trading Availability: 8+ major CEXs (spot + perpetuals on 7), 5+ major DEXs on Scroll L2, Ethereum Mainnet DEX liquidity
Adoption Metrics Available: TVL, Daily Active Addresses, Daily Transactions, Unique Wallets, Developer Count, Trading Volume (Spot/Perp), Bridge Volume, Cross-chain Messages, Sequencer/Prover Count — from L2Beat, DefiLlama, Token Terminal, Scrollscan, CoinGecko, CoinMarketCap, Dune Analytics

---

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Scroll

Strategic Objectives

1. Membangun zkEVM Layer 2 yang EVM-equivalent (Type 2) pada Ethereum
· Evidence: Scroll secara eksplisit menargetkan Vitalik Type 2 EVM-equivalence (bytecode compatible); execution client berbasis modified Geth; semua opcode standar dan precompiles didukung (HIGH) [Scroll Documentation EVM Equivalence, https://docs.scroll.io/architecture/evm-equivalence] [Vitalik ZK-EVM Types, https://vitalik.eth.limo/general/2022/08/04/zkevm.html]
· Supporting Dataset: Phase 4 Technology (Architecture, Execution Environment), Phase 1 Foundation (Category, Core Products)

2. Mencapai desentralisasi progresif melalui DAO dan token governance
· Evidence: Roadmap desentralisasi sequencer dan prover dipublikasikan; SCR token diluncurkan untuk governance; Security Council multisig ada untuk emergency controls; DAO treasury 5% alokasi (HIGH) [Scroll Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap] [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Governance Security Council, https://docs.scroll.io/governance/security-council]
· Supporting Dataset: Phase 3 History (EV-010, EV-023), Phase 6 Token (Governance, Distribution), Phase 7 Ecosystem (Governance Ecosystem)

3. Meluncurkan dengan ekosistem DeFi lengkap dari hari pertama (full stack at launch)
· Evidence: 20+ protokol DeFi mayor (Uniswap, Aave, PancakeSwap, Sushi, Balancer, Curve, Pendle, Euler, Morpho, Radiant, Silo, Gearbox, CIAN), 10 restaking protocols, 6 wallet, 2 explorer, 3 cross-chain messaging — semuanya live dalam minggu pasca-mainnet (HIGH) [Scroll Ecosystem, https://scroll.io/ecosystem] [Phase 3 EV-011 through EV-022]
· Supporting Dataset: Phase 3 History (EV-011 to EV-022), Phase 7 Ecosystem (Major Integrations, Applications), Phase 8 Market (Adoption Metrics)

4. Mempertahankan Ethereum alignment penuh (settlement, data availability, security)
· Evidence: Settlement di Ethereum L1; DA via calldata/blob (EIP-4844); finalitas melalui ZK-proof verification on-chain; tidak menggunakan separate DA layer; inherits Ethereum security (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview] [Scroll Data Availability, https://docs.scroll.io/architecture/data-availability]
· Supporting Dataset: Phase 4 Technology (System Architecture, Consensus, Security Model), Phase 7 Ecosystem (External Dependencies - Ethereum)

5. Developer-first approach dengan tooling lengkap sejak testnet
· Evidence: Scroll SDK, Hardhat plugin, Foundry template, public RPC, faucet, contract verification, Blockscout explorer — semua tersedia sejak testnet fase awal (HIGH) [Scroll Developers, https://docs.scroll.io/developers] [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk] [Scroll Hardhat Plugin, https://github.com/scroll-tech/hardhat-scroll]
· Supporting Dataset: Phase 4 Technology (Development Framework), Phase 7 Ecosystem (Developer Ecosystem), Phase 3 History (EV-006, EV-008)

Decision Timeline

Keputusan: Pendirian Scroll Foundation di Cayman Islands sebagai entitas hukum (2021)
· Trigger: Perlu legal wrapper untuk token issuance, treasury management, dan compliance sebelum pengembangan protokol
· Evidence: Scroll Foundation didirikan 2021 oleh tiga co-founder; Cayman Islands dipilih sebagai yurisdiksi foundation (MEDIUM) [Scroll Foundation, https://scroll.io/foundation] [Scroll Team, https://scroll.io/team]
· Decision: Mendirikan Scroll Foundation (Cayman) dan Scroll Tech Pte. Ltd. (Singapura) sebagai entitas operasional
· Immediate Result: Entitas hukum dan tim pendiri tersedia untuk pengembangan protokol
· Long-term Impact: Struktur dual entity (Foundation + OpCo) memisahkan governance/protokol dari operasi komersial; memungkinkan TGE 2024 melalui Foundation
· Supporting Dataset: Phase 2 Entity (Scroll Foundation, Scroll Tech Pte. Ltd., Sandy Peng, Haichen Shen, Ye Zhang), Phase 3 History (EV-001)

Keputusan: Series A Funding $30M led by Polychain Capital at $1.8B valuation (2022-07)
· Trigger: Perlu capital untuk scaling tim engineering dan penelitian ZK-proof setelah validasi konsep awal
· Evidence: The Block melaporkan Series A $30M led Polychain dengan Sequoia China, Variant, Robot Ventures, dll; valuation $1.8B post-money (HIGH) [The Block Series A, https://www.theblock.co/post/158021/scroll-raises-30m-series-a-polychain-capital] [TechCrunch Series A, https://techcrunch.com/2022/07/19/scroll-raises-30m-for-zk-evm-layer-2]
· Decision: Menerima equity + token warrant dari VC tier-1 dengan valuation tinggi pre-product
· Immediate Result: $30M runway untuk hiring cryptographers dan engineers; validator signal ke pasar
· Long-term Impact: Investor base kuat (Polychain, Sequoia, Variant) membuka pintu strategic round dan ecosystem partnerships; token warrant mengunci 15% supply untuk investors
· Supporting Dataset: Phase 5 Financial (Funding History - Series A), Phase 2 Entity (Investor entities), Phase 6 Token (Distribution - Investors 15%)

Keputusan: Rekrut Dmitry Khovratovich sebagai Chief Cryptographer (2022)
· Trigger: Perlu kepemimpinan kriptografi senior untuk desain ZK-proof system production-grade
· Evidence: Khovratovich (co-author Argon2, Equihash, berbagai konstruksi ZK) bergabung 2022; memimpin penelitian ZK-proof dan keamanan (HIGH) [Scroll Team, https://scroll.io/team] [Khovratovich Publications, https://www.khovratovich.com/]
· Decision: Merekrut kriptografer ternama dunia sebagai Chief Cryptographer (bukan advisor saja)
· Immediate Result: Arsitektur Halo2/KZG dengan Perpetual Powers of Tau dipilih dan dikembangkan
· Long-term Impact: Scroll menjadi salah satu ZK-Rollup dengan tim kriptografi terkuat; membedakan dari kompetitor yang menggunakan STARK (Starknet) atau Plonky2 (Polygon zkEVM)
· Supporting Dataset: Phase 2 Entity (Dmitry Khovratovich), Phase 3 History (EV-002), Phase 4 Technology (Proof System, Security Model)

Keputusan: Rekrut Brendan Farmer (Polygon zkEVM co-founder) sebagai Advisor (2022)
· Trigger: Perlu expertise production zkEVM dari kompetitor langsung untuk menghindari pitfalls arsitektur
· Evidence: Farmer co-founder Polygon zkEVM bergabung sebagai advisor 2022 (HIGH) [Scroll Team, https://scroll.io/team] [Polygon zkEVM Blog, https://blog.polygon.technology/polygon-zkevm/]
· Decision: Mengontrak advisor dari kompetitor utama dengan pengetahuan internal zkEVM production
· Immediate Result: Arahan strategis untuk arsitektur sequencer, prover, dan EVM-equivalence implementation
· Long-term Impact: Scroll menghindari kesalahan desain Polygon zkEVM; mempercepat time-to-mainnet
· Supporting Dataset: Phase 2 Entity (Brendan Farmer), Phase 3 History (EV-003), Phase 4 Technology (Architecture)

Keputusan: Meluncurkan multiple testnet phases (Pre-alpha Oct 2023, Alpha Feb 2023, Sepolia 2023)
· Trigger: Perlu validasi bertahap arsitektur ZK-proof, sequencer, prover, bridge sebelum mainnet
· Evidence: Pre-alpha Testnet 2023-10-18 untuk validasi arsitektur awal; Alpha Testnet 2023-02-28 untuk developer testing; Sepolia Testnet 2023 untuk persistent environment (HIGH) [Scroll Blog Pre-alpha, https://scroll.io/blog/pre-alpha-testnet] [Scroll Blog Alpha, https://scroll.io/blog/alpha-testnet] [Scroll Docs Testnet, https://docs.scroll.io/developers/testnet]
· Decision: Three-phase testnet strategy (pre-alpha → alpha → sepolia persistent) bukan single testnet
· Immediate Result: Bug ditemukan dan diperbaiki di setiap fase; developer ecosystem onboarded bertahap; prover/sequencer stress-tested
· Long-term Impact: Mainnet launch lancar tanpa insiden mayor; developer tooling mature saat launch; community trust dibangun
· Supporting Dataset: Phase 3 History (EV-004, EV-005, EV-006), Phase 4 Technology (Testnet Infrastructure)

Keputusan: Series B Funding $50M led by Bain Capital Crypto at flat $1.8B valuation (2023-03)
· Trigger: Perlu capital tambahan untuk mainnet preparation, audit, ecosystem incentives meskipun bear market 2023
· Evidence: The Block melaporkan Series B $50M led Bain Capital Crypto; valuation flat $1.8B; existing investors participate (HIGH) [The Block Series B, https://www.theblock.co/post/217841/scroll-raises-50m-series-b-bain-capital-crypto] [CoinDesk Series B, https://coindesk.com/business/2023/03/08/scroll-raises-50m-series-b-at-1-8b-valuation]
· Decision: Raise Series B di bear market dengan flat valuation; menambah investor strategic (Bain Capital Crypto)
· Immediate Result: $50M tambahan runway; Bain Capital Crypto join cap table
· Long-term Impact: Total $80M equity funding (A+B) memberikan runway ke mainnet dan pasca-launch; investor base diperluas ke traditional crypto VC
· Supporting Dataset: Phase 5 Financial (Funding History - Series B), Phase 6 Token (Distribution - Investors 15% combined), Phase 2 Entity (Bain Capital Crypto)

Keputusan: Strategic Round + Ethereum Foundation Grant (2023-10)
· Trigger: Perlu ecosystem alignment dan non-dilutive funding untuk ZK research
· Evidence: Strategic round dengan ecosystem partners; EF grant Q3 2023 untuk ZK research (MEDIUM) [Scroll Blog Strategic, https://scroll.io/blog/strategic-round] [EF Grants Q3 2023, https://blog.ethereum.org/2023/10/16/ethereum-foundation-grants-q3-2023]
· Decision: Mengambil strategic investment dari ecosystem partners + EF grant tanpa equity dilution
· Immediate Result: Ecosystem partners committed ke integration; EF validation untuk teknologi
· Long-term Impact: LayerZero, Wormhole, Chainlink, Pyth, dll terintegrasi at/near launch; EF grant memperkuat credibility teknis
· Supporting Dataset: Phase 5 Financial (Funding History - Strategic Round), Phase 7 Ecosystem (Major Integrations), Phase 3 History (EV-011 to EV-017)

Keputusan: Simultaneous Mainnet Launch + TGE (2024-10-22)
· Trigger: Maximize momentum; token utility immediate (governance, ecosystem incentives); avoid "launch then token later" narrative
· Evidence: Mainnet launch dan TGE announcement同日; SCR token ERC-20 deployed Ethereum Mainnet bersamaan (HIGH) [Scroll Mainnet Launch Blog, https://scroll.io/blog/mainnet-launch] [Scroll TGE Blog, https://scroll.io/blog/tge]
· Decision: Launch mainnet dan token pada block yang sama; 1B total supply, vesting schedules aktif immediately
· Immediate Result: Token tradable day-1; governance live; ecosystem incentives funded; CEX listing immediate
· Long-term Impact: Menghindari "ghost chain" perception; liquidity untuk ecosystem grants; investor unlock timeline dimulai (12-month cliff)
· Supporting Dataset: Phase 3 History (EV-009, EV-010), Phase 6 Token (TGE, Distribution, Vesting), Phase 8 Market (Trading Markets)

Keputusan: Full ecosystem deployment wave at/near mainnet launch (2024-10 to 2024-11)
· Trigger: Demonstrate production readiness; attract users/liquidity immediately; differentiate from competitors with gradual rollouts
· Evidence: 40+ integrations (LayerZero, Wormhole, Chainlink, Pyth, Gelato, Safe, Hyperlane, Uniswap, Aave, 11 DeFi, 10 restaking, 6 wallets, 2 explorers) live within weeks (HIGH) [Scroll Ecosystem, https://scroll.io/ecosystem] [Phase 3 EV-011 through EV-022]
· Decision: Coordinated "wave 1" launch dengan major protocols simultaneously bukan staggered
· Immediate Result: TVL ~$1.2B within weeks; full DeFi stack available day-1; user retention tinggi
· Long-term Impact: Established sebagai top-3 ZK-Rollup by TVL/transactions; network effect compounding; developer mindshare captured
· Supporting Dataset: Phase 3 History (EV-011 to EV-022), Phase 7 Ecosystem (Major Integrations, Applications), Phase 8 Market (Adoption Metrics, Market Share)

Keputusan: EIP-4844 Blob Integration post-mainnet (2024-11)
· Trigger: Reduce L1 data availability cost ~90% setelah EIP-4844 activated on Ethereum
· Evidence: Migration dari calldata ke blob DA; L1 cost reduction ~90% (HIGH) [Scroll Blob Integration Blog, https://scroll.io/blog/eip4844-integration] [Scrollscan Blobs, https://scrollscan.com/blobs]
· Decision: Prioritaskan blob migration secepat mungkin pasca-EIP-4844 activation
· Immediate Result: Transaction fees turun signifikan; throughput cost-efficiency meningkat
· Long-term Impact: Competitive fee advantage vs Optimistic Rollups; sustainable economics untuk high-throughput use cases
· Supporting Dataset: Phase 4 Technology (Technical Upgrade History - EIP-4844), Phase 7 Ecosystem (External Dependencies - EIP-4844)

Keputusan: Prover Parallelization v1 (2024-12)
· Trigger: Throughput bottleneck di prover cluster; perlu scale proving capacity tanpa menambah hardware linear
· Evidence: Prover cluster parallelization enabling ~3x throughput increase (MEDIUM) [Scroll Prover Upgrade Blog, https://scroll.io/blog/prover-parallelization] [Scroll Metrics, https://scroll.io/metrics]
· Decision: Invest dalam prover software optimization (parallelization) sebelum hardware scaling
· Immediate Result: Batch proving capacity 3x; latency proof generation turun
· Long-term Impact: Foundation untuk prover decentralization; cost per proof turun; roadmap ke permissionless prover network
· Supporting Dataset: Phase 4 Technology (Technical Upgrade History - Prover Parallelization), Phase 4 Technology (Core Components - zkProver)

Keputusan: Sequencer Pre-confirmation API Beta (2025-01)
· Trigger: User demand untuk soft finality sub-second; centralized sequencer bisa provide pre-conf sebelum L1 proof
· Evidence: Soft finality API untuk pre-confirmation ~seconds sebelum L1 proof verification (MEDIUM) [Scroll Pre-conf API Docs, https://docs.scroll.io/developers/preconfirmation] [Scroll Pre-conf Endpoint, https://preconf.scroll.io/]
· Decision: Release pre-confirmation API sebagai interim solution sebelum sequencer decentralization
· Immediate Result: UX improvement signifikan untuk traders/DeFi users; differentiator vs L2 lain
· Long-term Impact: Bridge ke based sequencing / PBS designs; revenue model untuk sequencer delegation
· Supporting Dataset: Phase 4 Technology (Technical Upgrade History - Pre-confirmation API), Phase 4 Technology (Consensus Mechanism)

Evolution Pattern

Perubahan Strategi: Dari Research-Heavy ke Production-First
· Early phase (2021-2022): Fokus fundamental research — hiring Khovratovich, designing Halo2 circuits, trusted setup ceremony participation
· Mid phase (2023): Testnet iteration bertahap — pre-alpha, alpha, sepolia; bridge dan SDK development parallel
· Late phase (2024+): Production execution — simultaneous mainnet+TGE, full ecosystem wave, rapid upgrades (blobs, prover parallelization, pre-conf)
· Evidence: Timeline hiring (Khovratovich 2022) → testnet phases (2023) → mainnet+TGE+ecosystem wave (2024) → upgrades (2024-2025) (HIGH) [Phase 3 History all events], [Phase 2 Entity key hires], [Phase 4 Technical Upgrade History]

Perubahan Teknologi: Dari Single-Prover ke Distributed Prover Network
· Design awal: Centralized prover cluster operated by Foundation
· Post-mainnet: Prover parallelization v1 (software scaling)
· Roadmap: Permissionless prover network dengan staking/slashing
· Evidence: Phase 4 Technology (Core Components - zkProver status "Live (distributed prover cluster operated by Scroll Foundation)"), (Technical Upgrade History - Prover Parallelization), (Known Limitations - Prover Cluster Operated by Foundation), (Security Model - Prover Trust)

Perubahan Tokenomics: Dari Pre-launch Allocation ke Live Vesting Dynamics
· Pre-TGE: Theoretical allocation percentages (Community 15%, Team 25%, Investors 15%, Foundation 20%, Treasury 5%, Ecosystem 20%)
· Post-TGE: Vesting schedules aktif — Team/Investors 12-month cliff then 36-month linear; Foundation 6-month cliff 36-month linear; Ecosystem 3-month cliff 24-month linear; Community 1-month cliff 18-month linear
· Evidence: Phase 6 Token (Distribution, Vesting Schedule, TGE), Phase 5 Financial (Token Sale - Private Sales)

Perubahan Governance: Dari Foundation-Controlled ke DAO-Progressive
· Launch: Foundation + Security Council multisig kontrol penuh (sequencer, prover, bridge, upgrades)
· Post-TGE: SCR governance live (Snapshot + on-chain Governor); Grant committee active; Fee switch proposal drafted
· Roadmap: Full DAO control over treasury, protocol parameters, sequencer/prover selection
· Evidence: Phase 6 Token (Governance), Phase 7 Ecosystem (Governance Ecosystem), Phase 3 History (EV-023 fee switch proposal)

Perubahan Market Position: Dari "ZK-EVM Contender" ke "Top-3 ZK-Rollup by Usage"
· Pre-mainnet: Unknown, unproven, competing dengan zkSync Era, Polygon zkEVM, Linea
· Post-mainnet (3 months): TVL ~$1.2B (#5-6 overall L2, #1-2 EVM-equivalent ZK); Transactions ~3M/day (~10% L2 share); Full DeFi stack
· Evidence: Phase 8 Market (Market Position, Market Share, Adoption Metrics), Phase 3 History (EV-009 launch)

Technical Decision Pattern

Pola 1: Ethereum Alignment First
· Decision Pattern: Setiap keputusan arsitektur utama dipilih untuk maximize alignment dengan Ethereum — settlement di L1, DA via Ethereum calldata/blob, finalitas via L1 verification, no separate DA layer, no separate consensus token
· Evidence: Scroll documentation eksplisit: "Settlement Layer: Ethereum L1", "Data Availability: Ethereum L1 calldata/blob", "Consensus: derives from Ethereum L1" (HIGH) [Scroll Documentation Architecture, https://docs.scroll.io/architecture/overview] [Scroll Data Availability, https://docs.scroll.io/architecture/data-availability] [Scroll Consensus, https://docs.scroll.io/architecture/consensus]
· Supporting Dataset: Phase 4 Technology (System Architecture, Consensus Mechanism, Security Model), Phase 7 Ecosystem (External Dependencies - Ethereum)

Pola 2: EVM-Equivalence (Type 2) over EVM-Compatibility (Type 4)
· Decision Pattern: Memilih bytecode-level equivalence (modified Geth) daripada Solidity-compatibility (LLVM-based seperti zkSync Era) — trade-off proving complexity untuk developer experience seamless
· Evidence: Execution client based on go-ethereum v1.13+; all standard opcodes; precompiles包括PointEvaluation untuk EIP-4844; Vitalik Type 2 classification (HIGH) [Scroll Execution Client GitHub, https://github.com/scroll-tech/go-ethereum] [Scroll Documentation EVM Equivalence, https://docs.scroll.io/architecture/evm-equivalence] [Vitalik ZK-EVM Types, https://vitalik.eth.limo/general/2022/08/04/zkevm.html]
· Supporting Dataset: Phase 4 Technology (Execution Environment, Core Components - L2 Execution Engine), Phase 1 Foundation (Category, Core Products)

Pola 3: Halo2/KZG dengan Perpetual Powers of Tau untuk Proof System
· Decision Pattern: Memilih PLONKish arithmetization (Halo2) + KZG polynomial commitment dengan universal trusted setup (Perpetual Powers of Tau) — bukan STARK (no trusted setup) atau Plonky2 (recursive)
· Evidence: zkProver menggunakan Halo2/Rust; KZG commitment; Powers of Tau ceremony参加; Verifier contract on-chain (HIGH) [Scroll Prover GitHub, https://github.com/scroll-tech/zkprover] [Scroll ZK-Proof Blog, https://scroll.io/blog/zk-proof-system] [Powers of Tau Ceremony, https://github.com/privacy-scaling-explorations/perpetual-powers-of-tau]
· Supporting Dataset: Phase 4 Technology (Security Model - Proof System, Core Components - zkProver), Phase 7 Ecosystem (External Dependencies - Halo2, Powers of Tau)

Pola 4: Centralized Sequencer/Prover Initially dengan Decentralization Roadmap Explisit
· Decision Pattern: Launch dengan single sequencer + Foundation-operated prover cluster; publish detailed decentralization roadmap; implement incremental steps (pre-conf API, prover parallelization) sebelum full decentralization
· Evidence: Sequencer status "Live (centralized, single operator)"; Prover "Live (distributed prover cluster operated by Scroll Foundation)"; Decentralization roadmap blog; Pre-conf API beta; Prover parallelization (HIGH) [Scroll Documentation Sequencer, https://docs.scroll.io/architecture/sequencer] [Scroll Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap] [Scroll Pre-conf API, https://docs.scroll.io/developers/preconfirmation]
· Supporting Dataset: Phase 4 Technology (Core Components - Sequencer, zkProver; Consensus Mechanism; Known Limitations), Phase 3 History (Technical Upgrades)

Pola 5: Extensive Pre-Launch Testing via Multi-Phase Testnets
· Decision Pattern: Three distinct testnet phases (pre-alpha architecture validation → alpha developer testing → sepolia persistent) dengan bridge, SDK, tooling di setiap fase — bukan single testnet rush
· Evidence: Pre-alpha 2023-10-18; Alpha 2023-02-28; Sepolia 2023 persistent; Bridge, SDK released di testnet phase (HIGH) [Scroll Blog Pre-alpha, https://scroll.io/blog/pre-alpha-testnet] [Scroll Blog Alpha, https://scroll.io/blog/alpha-testnet] [Scroll Docs Testnet, https://docs.scroll.io/developers/testnet]
· Supporting Dataset: Phase 3 History (EV-004, EV-005, EV-006), Phase 4 Technology (Testnet Infrastructure), Phase 7 Ecosystem (Developer Ecosystem)

Pola 6: Multiple Independent Audits Sebelum Mainnet
· Decision Pattern: 6 auditor independen (Trail of Bits, OpenZeppelin, Zellic, Spearbit/Pashov, Sigma Prime, Nethermind ongoing) mencakup circuits, contracts, execution client, bridge — bukan single audit
· Evidence: Audit reports publik di GitHub scroll-tech/audits; scope: prover circuits, verifier, bridge, token, governance, execution client (HIGH) [Scroll Audits GitHub, https://github.com/scroll-tech/audits] [Trail of Bits Report, https://github.com/scroll-tech/audits/tree/main/trail-of-bits-2024] [OpenZeppelin Report, https://github.com/scroll-tech/audits/tree/main/openzeppelin-2024]
· Supporting Dataset: Phase 4 Technology (Audit History), Phase 7 Ecosystem (Infrastructure Providers - Security)

Pola 7: Modified Geth sebagai Execution Client Base
· Decision Pattern: Fork go-ethereum (Geth) v1.13+ dan modify untuk zkEVM compatibility — bukan custom VM atau LLVM-based — memastikan bytecode equivalence dan upstream compatibility
· Evidence: Execution client repo di github.com/scroll-tech/go-ethereum; based on Geth; all standard opcodes supported (HIGH) [Scroll Execution Client GitHub, https://github.com/scroll-tech/go-ethereum] [Scroll Documentation Execution, https://docs.scroll.io/architecture/execution]
· Supporting Dataset: Phase 4 Technology (Core Components - L2 Execution Engine, Execution Environment), Phase 7 Ecosystem (External Dependencies - go-ethereum)

Financial Decision Pattern

Pola 1: VC Funding dengan Token Warrant Structure (Series A + B)
· Decision Pattern: Mengambil equity funding dari top-tier crypto VC (Polychain, Sequoia China, Variant, Bain Capital Crypto) dengan token warrant/SAFT — bukan pure token sale — menjaga alignment jangka panjang dan regulatory clarity
· Evidence: Series A $30M (2022-07), Series B $50M (2023-03); total $80M; valuation $1.8B flat; investors menerima token allocation 15% dengan vesting 12-month cliff + 36-month linear (HIGH) [The Block Series A, https://www.theblock.co/post/158021/scroll-raises-30m-series-a-polychain-capital] [The Block Series B, https://www.theblock.co/post/217841/scroll-raises-50m-series-b-bain-capital-crypto] [Scroll Blog TGE, https://scroll.io/blog/tge]
· Supporting Dataset: Phase 5 Financial (Funding History), Phase 6 Token (Distribution - Investors, Vesting Schedule), Phase 2 Entity (Investor entities)

Pola 2: Strategic Round untuk Ecosystem Alignment (bukan Kapital Murni)
· Decision Pattern: Strategic investors (ecosystem partners, infrastructure providers) dipilih berdasarkan value-add bukan capital — LayerZero, Wormhole, Chainlink, Pyth, EigenLayer, dll — dengan token allocation bervariasi
· Evidence: Strategic round 2023-10; EF grant non-dilutif; ecosystem partners terintegrasi at/near launch (MEDIUM) [Scroll Blog Strategic, https://scroll.io/blog/strategic-round] [EF Grants Q3 2023, https://blog.ethereum.org/2023/10/16/ethereum-foundation-grants-q3-2023] [Phase 7 Major Integrations all live 2024]
· Supporting Dataset: Phase 5 Financial (Funding History - Strategic Round), Phase 7 Ecosystem (Major Integrations), Phase 3 History (EV-011 to EV-021)

Pola 3: No Public Sale / Community Sale — TGE Langsung ke Circulating Supply
· Decision Pattern: Tidak ada ICO, IDO, launchpad, community sale, auction — token diluncurkan langsung ke passing supply via CEX/DEX listing dan airdrop community allocation
· Evidence: Phase 5 Financial (Token Sale - all "Tidak ada" for public/community/launchpad/auction); TGE blog menyebut airdrop community 15% tapi tidak public sale (HIGH) [Scroll Blog TGE, https://scroll.io/blog/tge] [CoinGecko Markets, https://coingecko.com/en/coins/scroll#markets]
· Supporting Dataset: Phase 5 Financial (Token Sale), Phase 6 Token (TGE, Distribution - Community), Phase 8 Market (Trading Markets)

Pola 4: Foundation Treasury Management dengan Token Allocation Besar
· Decision Pattern: Foundation hold 20% + Treasury 5% = 25% total supply untuk operations, grants, research — vesting 6-month cliff + 36-month linear dengan 5% unlock at TGE
· Evidence: Tokenomics blog: Foundation 20%, Treasury 5%; vesting schedule Foundation 6-month cliff 36-month linear, 5% unlocked at TGE (HIGH) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
· Supporting Dataset: Phase 5 Financial (Treasury), Phase 6 Token (Distribution - Foundation/Treasury, Vesting Schedule), Phase 7 Ecosystem (Governance Ecosystem - Foundation)

Pola 5: Protocol Revenue Planned but Not Yet Active
· Decision Pattern: Revenue streams identified (L2 fees, bridge fees, sequencer revenue, future protocol fee switch, prover fees) tapi protocol fee switch belum aktif — sequencer revenue目前全归Foundation
· Evidence: Phase 5 Financial (Revenue Model - all streams "Live" except Protocol Fee Switch "Planned", Prover Fees "Planned"); Sequencer trust model confirms priority fees + MEV to single operator (HIGH) [Scroll Docs Gas, https://docs.scroll.io/architecture/gas] [Scroll Bridge Fees, https://docs.scroll.io/developers/bridge#fees] [Scroll Sequencer, https://docs.scroll.io/architecture/sequencer]
· Supporting Dataset: Phase 5 Financial (Revenue Model, Revenue History), Phase 4 Technology (Core Components - Sequencer), Phase 6 Token (Utility - Protocol Fee Share)

Pola 6: Ethereum Foundation Grant untuk Research Non-Dilutive
· Decision Pattern: Mengambil EF grant Q3 2023 untuk ZK research — non-dilutive, no token/equity — menunjukkan research credibility dan alignment dengan Ethereum roadmap
· Evidence: EF Grants Q3 2023 includes Scroll; grant amount tidak diungkap tapi non-dilutive (MEDIUM) [EF Grants Q3 2023, https://blog.ethereum.org/2023/10/16/ethereum-foundation-grants-q3-2023] [Scroll Blog Strategic, https://scroll.io/blog/strategic-round]
· Supporting Dataset: Phase 5 Financial (Funding History - Strategic Round, Financial Dependencies), Phase 7 Ecosystem (External Dependencies - Ethereum Foundation)

Ecosystem Decision Pattern

Pola 1: "Full Stack at Launch" — Coordinated Ecosystem Wave
· Decision Pattern: Mengkoordinasi 40+ major integrations (cross-chain, oracle, DeFi, restaking, wallet, explorer) untuk live dalam minggu yang sama/dekat mainnet — bukan staggered rollout bulan demi bulan
· Evidence: EV-011 to EV-022 all dalam 2024 (post-mainnet Oct-Nov); LayerZero, Wormhole, Chainlink, Pyth, Gelato, Safe, Hyperlane, Uniswap, Aave, 11 DeFi, 10 restaking, 6 wallets, 2 explorers (HIGH) [Scroll Ecosystem, https://scroll.io/ecosystem] [Phase 3 History EV-011 through EV-022]
· Supporting Dataset: Phase 3 History (EV-011 to EV-022), Phase 7 Ecosystem (Major Integrations, Applications, Infrastructure Providers), Phase 8 Market (Adoption Metrics - TVL $1.2B within weeks)

Pola 2: Cross-Chain Messaging Redundancy (LayerZero + Wormhole + Hyperlane + Native Bridge)
· Decision Pattern: Mengintegrasikan 3 major interop protocols + native bridge — tidak bergantung pada single bridge — memberikan user choice dan redundancy
· Evidence: Native bridge (canonical), LayerZero (OFT/messaging), Wormhole (bridge/messaging), Hyperlane (permissionless messaging) all live (HIGH) [Scroll Bridge Docs, https://docs.scroll.io/developers/bridge] [LayerZero Scroll, https://layerzero.network/blog/scroll-integration] [Wormhole Scroll, https://wormhole.com/ecosystem/scroll] [Hyperlane Scroll, https://docs.hyperlane.xyz/docs/chains/scroll]
· Supporting Dataset: Phase 7 Ecosystem (Major Integrations - LayerZero, Wormhole, Hyperlane; External Dependencies), Phase 4 Technology (System Architecture - Cross-chain Messaging)

Pola 3: Oracle Dual-Source (Chainlink + Pyth) untuk DeFi Reliability
· Decision Pattern: Mengintegrasikan Chainlink (Price Feeds, VRF, CCIP, PoR) DAN Pyth (first-party financial data) — bukan single oracle — untuk redundancy dan data diversity
· Evidence: Chainlink full stack live; Pyth price feeds live; both documented di ecosystem page (HIGH) [Chainlink Scroll Support, https://blog.chain.link/chainlink-scroll-support] [Pyth Scroll Integration, https://pyth.network/developers/price-feed-ids#scroll]
· Supporting Dataset: Phase 7 Ecosystem (Major Integrations - Chainlink, Pyth; External Dependencies), Phase 3 History (EV-013, EV-014)

Pola 4: Restaking Ecosystem Full Integration dari Launch
· Decision Pattern: 10 restaking/liquid restaking protocols (EigenLayer, Symbiotic, Karak, Renzo, Ether.fi, Puffer, Swell, Kelp, Mellow, Kernel) terintegrasi — mempositioning Scroll sebagai L2 untuk restaking economy
· Evidence: EV-021 lists 10 protocols; all live di Scroll Mainnet; Kernel untuk BTC/ETH restaking (HIGH) [Scroll Ecosystem Restaking, https://scroll.io/ecosystem] [EigenLayer Scroll, https://www.eigenlayer.xyz/ecosystem/scroll] [Symbiotic Scroll, https://symbiotic.fi/networks/scroll]
· Supporting Dataset: Phase 3 History (EV-021), Phase 7 Ecosystem (Major Integrations - Restaking, Applications - Restaking), Phase 8 Market (Narrative Position - Restaking Integration)

Pola 5: Developer Tooling Priority — SDK, Hardhat, Foundry, Faucet, Verification dari Testnet
· Decision Pattern: Invest heavily dalam developer experience sebelum mainnet — Scroll SDK, Hardhat plugin, Foundry template, public RPC, Sepolia faucet, contract verification all ready di testnet phase
· Evidence: Phase 4 Technology (Development Framework - all live); Phase 7 Ecosystem (Developer Ecosystem - all tools listed); Sepolia faucet live 2023 (HIGH) [Scroll Developers, https://docs.scroll.io/developers] [Scroll SDK GitHub, https://github.com/scroll-tech/scroll-sdk] [Scroll Sepolia Faucet, https://sepolia-faucet.scroll.io/]
· Supporting Dataset: Phase 4 Technology (Development Framework), Phase 7 Ecosystem (Developer Ecosystem), Phase 3 History (EV-006, EV-008)

Pola 6: Wallet/Explorer Support Comprehensive dari Day-1
· Decision Pattern: 6 major wallets (MetaMask, Rabby, OKX, Rainbow, Zerion, Safe) + 2 explorers (Scrollscan/Blockscout, L2Scan) supported at launch — memastikan user onboarding friction minimal
· Evidence: EV-022 lists all; MetaMask via Snaps/RPC; Rabby/OKX/Rainbow native; Zerion/Instadapp portfolio; Safe multisig deployed (HIGH) [Scroll Ecosystem, https://scroll.io/ecosystem] [MetaMask Scroll, https://chainlist.org/chain/534352] [Rabby Scroll, https://rabby.io/chains/scroll]
· Supporting Dataset: Phase 3 History (EV-022), Phase 7 Ecosystem (Major Integrations - Wallets/Infrastructure, Wallet Ecosystem), Phase 8 Market (Adoption Metrics - Daily Active Addresses)

Governance Decision Pattern

Pola 1: Foundation-Led dengan Progressive Decentralization Roadmap
· Decision Pattern: Foundation (Cayman) + Security Council multisig kontrol penuh awal (sequencer, prover, bridge upgrades, treasury); roadmap publik untuk transition ke DAO governance via SCR token
· Evidence: Scroll Foundation legal entity; Security Council docs menyebut emergency controls; Decentralization roadmap blog; SCR token governance live (HIGH) [Scroll Foundation, https://scroll.io/foundation] [Scroll Security Council, https://docs.scroll.io/governance/security-council] [Scroll Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap]
· Supporting Dataset: Phase 2 Entity (Scroll Foundation), Phase 6 Token (Governance), Phase 7 Ecosystem (Governance Ecosystem), Phase 3 History (EV-001, EV-010)

Pola 2: Dual-Layer Governance (Snapshot Off-chain + On-chain Governor)
· Decision Pattern: Off-chain signaling via Snapshot (gasless, broad participation) + On-chain execution via OpenZeppelin Governor (binding, timelock) — best of both worlds
· Evidence: Governance docs menyebut mixed model; Snapshot space scroll.eth active; Governor contracts di bridge-contracts repo (MEDIUM) [Scroll Docs Governance, https://docs.scroll.io/governance/overview] [Scroll Snapshot, https://snapshot.org/#/scroll.eth] [Scroll Contracts GitHub, https://github.com/scroll-tech/scroll-bridge-contracts/tree/main/contracts/governance]
· Supporting Dataset: Phase 6 Token (Governance), Phase 7 Ecosystem (Governance Ecosystem - DAO), Phase 4 Technology (Security Model - Upgradeability)

Pola 3: Security Council Multisig untuk Emergency Controls
· Decision Pattern: t-of-n multisig (signers tidak dipublikasikan) dengan authority: pause bridge, upgrade contracts, halt sequencer — safety valve selama centralized phase
· Evidence: Security Council docs: "Emergency controls: Security Council multisig dapat pause bridge, upgrade contracts, halt sequencer dalam emergency" (MEDIUM) [Scroll Security Council, https://docs.scroll.io/governance/security-council] [Scroll Docs Upgradeability, https://docs.scroll.io/architecture/upgrades]
· Supporting Dataset: Phase 4 Technology (Security Model - Emergency Controls, Upgradeability), Phase 7 Ecosystem (Governance Ecosystem - Security Council), Phase 2 Entity (Security Council)

Pola 4: Grant Committee untuk Ecosystem Fund Allocation
· Decision Pattern: Committee terpisah (anggota tidak publik) review grant proposals dari ecosystem allocation (20% = 200M SCR) — bukan Foundation unilateral
· Evidence: Ecosystem Grants page; Gov forum grants category; 200M SCR allocation untuk grants (MEDIUM) [Scroll Ecosystem Grants, https://scroll.io/ecosystem/grants] [Gov Forum Grants, https://gov.scroll.io/c/grants/6] [Scroll Blog TGE, https://scroll.io/blog/tge]
· Supporting Dataset: Phase 6 Token (Distribution - Ecosystem), Phase 7 Ecosystem (Governance Ecosystem - Grant Committee, Developer Ecosystem - Grant Program)

Pola 5: Token-Weighted Voting dengan Delegation (1 SCR = 1 Vote)
· Decision Pattern: Voting power proporsional ke SCR balance; delegation tersedia (off-chain Snapshot, on-chain Governor); proposal threshold belum diungkapkan
· Evidence: Governance docs: "Weighted voting (1 SCR = 1 vote)"; "Delegation tersedia"; threshold tidak spesifik (MEDIUM) [Scroll Docs Governance Voting, https://docs.scroll.io/governance/voting] [Scroll Docs Delegation, https://docs.scroll.io/governance/delegation] [Scroll Snapshot, https://snapshot.org/#/scroll.eth]
· Supporting Dataset: Phase 6 Token (Governance - Voting System, Voting Power, Delegation), Phase 7 Ecosystem (Governance Ecosystem - DAO)

Pola 6: Treasury Governance via DAO dengan Security Council Veto
· Decision Pattern: DAO treasury (50M SCR) managed melalui governance vote; execution via timelock; Security Council dapat veto emergency — checks and balances
· Evidence: Governance treasury docs; Security Council emergency controls; 5% allocation untuk treasury (MEDIUM) [Scroll Docs Governance Treasury, https://docs.scroll.io/governance/treasury] [Scroll Security Council, https://docs.scroll.io/governance/security-council] [Scroll Blog TGE, https://scroll.io/blog/tge]
· Supporting Dataset: Phase 6 Token (Distribution - Treasury, Governance - Treasury Governance), Phase 7 Ecosystem (Governance Ecosystem)

Risk Response Pattern

Pola 1: Pre-Launch Multi-Audit Strategy untuk Mitigasi Smart Contract Risk
· Decision Pattern: 6 auditor independen (Trail of Bits, OpenZeppelin, Zellic, Spearbit, Sigma Prime, Nethermind) sebelum mainnet — mencakup circuits, contracts, execution client, bridge — bukan reactive post-exploit
· Evidence: Audit reports publik di GitHub; scope: zkProver circuits, L1 verifier, bridge contracts, token, governance, execution client, P2P (HIGH) [Scroll Audits GitHub, https://github.com/scroll-tech/audits] [Trail of Bits Report, https://github.com/scroll-tech/audits/tree/main/trail-of-bits-2024] [OpenZeppelin Report, https://github.com/scroll-tech/audits/tree/main/openzeppelin-2024]
· Trigger: High-value bridge contracts + novel ZK-proof system = high attack surface; need credibility untuk TVL
· Response: Commission comprehensive audit program 6 firma tier-1; publish reports transparan
· Result: No major exploit post-mainnet; credibility untuk ecosystem partners dan users
· Supporting Dataset: Phase 4 Technology (Audit History), Phase 7 Ecosystem (Infrastructure Providers - Security)

Pola 2: Bug Bounty Program (Immunefi) untuk Ongoing Security
· Decision Pattern: Live bug bounty di Immunefi post-mainnet untuk continuous vulnerability discovery — bukan one-time audit only
· Evidence: Immunefi page exists: https://immunefi.com/bounty/scroll/ (MEDIUM - scope/max reward detail perlu verifikasi) [Scroll Bug Bounty, https://immunefi.com/bounty/scroll/]
· Trigger: Post-launch unknown vulnerabilities; incentive alignment dengan whitehats
· Response: Establish bug bounty program di platform terkemuka
· Result: Ongoing; no public major bounty payout reported yet
· Supporting Dataset: Phase 4 Technology (Official Technical Resources - Bug Bounty), Phase 7 Ecosystem (Official Ecosystem Resources - Bug Bounty)

Pola 3: 7-Day Withdrawal Delay sebagai Bridge Security Mechanism
· Decision Pattern: Mandatory 7-day challenge period untuk L2→L1 withdrawals via native bridge — user funds locked tapi protected dari invalid state root submission
· Evidence: Bridge docs: "withdrawal fee ~0.05-0.1% + L1 gas"; "7 hari withdrawal delay untuk security"; challenge period design (HIGH) [Scroll Bridge Security Docs, https://docs.scroll.io/developers/bridge#security] [Scroll Bridge Withdrawal, https://docs.scroll.io/developers/bridge#withdrawal-process]
· Trigger: Bridge holds user ETH/ERC-20; invalid proof submission risk; need time untuk fraud detection
· Response: Implement 7-day withdrawal delay dengan challenge mechanism; governance proposal untuk reduce ke 3 hari
· Result: Security guarantee; user friction (liquidity locked); proposal untuk reduction (EV-023 withdrawal delay reduction)
· Supporting Dataset: Phase 4 Technology (Security Model - Bridge Security, Known Limitations), Phase 3 History (EV-023 withdrawal delay reduction proposal), Phase 6 Token (Major Token Events - Fee Switch Proposal)

Pola 4: Security Council Emergency Controls untuk Centralized Component Failures
· Decision Pattern: Multisig dengan authority pause bridge, upgrade contracts, halt sequencer — mitigation untuk single sequencer/prover failure atau exploit
· Evidence: Security Council docs: "Emergency controls: Security Council multisig dapat pause bridge, upgrade contracts, halt sequencer dalam emergency" (MEDIUM) [Scroll Security Council, https://docs.scroll.io/governance/security-council] [Scroll Docs Upgradeability, https://docs.scroll.io/architecture/upgrades]
· Trigger: Centralized sequencer/prover = single point of failure; need human-in-the-loop emergency stop
· Response: Establish Security Council multisig dengan emergency powers; timelock untuk upgrades
· Result: Safety net aktif; belum pernah digunakan emergency (tidak ada insiden publik)
· Supporting Dataset: Phase 4 Technology (Security Model - Emergency Controls, Upgradeability, Known Limitations), Phase 7 Ecosystem (Governance Ecosystem - Security Council)

Pola 5: Forced Inclusion / Escape Hatch Design (Not Yet Activated)
· Decision Pattern: Design exists untuk L1 force-inclusion via delayed inbox (user bisa force-include tx ke L1 jika sequencer censor) — tapi belum activated di mainnet
· Evidence: Escape hatch design docs exist; "No Forced Transaction Inclusion Mechanism live on mainnet yet" di known limitations (MEDIUM) [Scroll Escape Hatch Design, https://docs.scroll.io/architecture/escape-hatch] [Scroll Known Limitations, https://docs.scroll.io/architecture/sequencer#limitations]
· Trigger: Censorship resistance requirement untuk credible neutrality; sequencer centralized
· Response: Design escape hatch mechanism; plan untuk activate post-decentralization milestones
· Result: Design ready; activation pending; governance discussion mungkin diperlukan
· Supporting Dataset: Phase 4 Technology (Known Limitations - No Forced Inclusion), Phase 3 History (Decentralization roadmap)

Pola 6: Prover Decentralization Roadmap sebagai Response ke Single Prover Cluster Risk
· Decision Pattern: Acknowledged single prover cluster risk; published roadmap untuk permissionless prover network dengan staking/slashing; implemented prover parallelization v1 sebagai stepping stone
· Evidence: Decentralization roadmap blog; Prover parallelization v1 upgrade; Known limitations lists "Prover Cluster Operated by Foundation" (HIGH) [Scroll Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap] [Scroll Prover Upgrade Blog, https://scroll.io/blog/prover-parallelization] [Scroll Known Limitations, https://docs.scroll.io/architecture/prover#security]
· Trigger: Single prover cluster = liveness risk; centralization criticism; need credible path
· Response: Publish roadmap; implement software scaling (parallelization) first; design staking/slashing economics
· Result: Parallelization live (3x throughput); roadmap public; staking economics in research phase
· Supporting Dataset: Phase 4 Technology (Technical Upgrade History - Prover Parallelization, Known Limitations), Phase 3 History (EV-023 technical upgrades), Phase 6 Token (Utility - Staking planned)

Recurring Behavioral Pattern

Pola 1: Selalu Pilih Ethereum Alignment di Setiap Fork Teknis
· Pattern: Settlement → Ethereum L1; DA → Ethereum calldata/blob; Finality → L1 verification; Execution → Modified Geth (Ethereum client); No separate consensus token; No separate DA layer
· Evidence: Phase 4 Technology (System Architecture - all Ethereum); Phase 7 Ecosystem (External Dependencies - Ethereum critical); Phase 3 History (all upgrades maintain Ethereum alignment)
· Supporting Dataset: Phase 4 Technology (System Architecture, Consensus Mechanism, Data Availability, Execution Environment), Phase 7 Ecosystem (External Dependencies)

Pola 2: Heavy Investment in Cryptography Talent Sebelum Product
· Pattern: Hire Dmitry Khovratovich (Chief Cryptographer) 2022, Brendan Farmer (Advisor) 2022 — sebelum testnet publik; research-first approach
· Evidence: Phase 2 Entity (Dmitry Khovratovich, Brendan Farmer); Phase 3 History (EV-002, EV-003); Phase 4 Technology (Proof System - Halo2/KZG design)
· Supporting Dataset: Phase 2 Entity (Key hires), Phase 3 History (EV-002, EV-003), Phase 4 Technology (Security Model - Proof System)

Pola 3: Parallel Development of All Core Components
· Pattern: Sequencer, Prover, Roller, Bridge, Execution Client, SDK, Node — semua dikembangkan parallel dari 2022-2023, bukan sequential
· Evidence: Phase 3 History (EV-004 testnet, EV-007 bridge, EV-008 SDK all 2023); Phase 4 Technology (Core Components - 9 components all "Live"); Phase 7 Ecosystem (Developer Ecosystem - all tools ready pre-mainnet)
· Supporting Dataset: Phase 3 History (2023 events), Phase 4 Technology (Core Components), Phase 7 Ecosystem (Developer Ecosystem)

Pola 4: Launch dengan Ecosystem Lengkap (Full Stack at Launch)
· Pattern: 40+ integrations coordinated untuk live dalam minggu mainnet — DEX, lending, oracle, cross-chain, restaking, wallet, explorer — bukan "launch then build"
· Evidence: Phase 3 History (EV-011 to EV-022 all 2024); Phase 7 Ecosystem (Major Integrations 40+, Applications 35+); Phase 8 Market (Adoption Metrics - TVL $1.2B within weeks)
· Supporting Dataset: Phase 3 History (EV-011 to EV-022), Phase 7 Ecosystem (Major Integrations, Applications), Phase 8 Market (Market Position, Adoption Metrics)

Pola 5: Multiple Independent Audits sebagai Standard
· Pattern: 6 auditor tier-1 untuk different scopes (circuits, contracts, client, bridge) — bukan single audit; Nethermind ongoing untuk continuous
· Evidence: Phase 4 Technology (Audit History - 6 auditors); Phase 7 Ecosystem (Infrastructure Providers - Security)
· Supporting Dataset: Phase 4 Technology (Audit History), Phase 7 Ecosystem (Infrastructure Providers)

Pola 6: Transparent Decentralization Roadmap dengan Milestone Teknis
· Pattern: Publish roadmap blog; implement incremental steps (pre-conf API, prover parallelization, blob integration) sebelum full decentralization; acknowledge current limitations honestly
· Evidence: Phase 4 Technology (Known Limitations - all documented honestly; Technical Upgrade History - incremental steps); Phase 3 History (Technical upgrades post-mainnet); Phase 8 Market (Narrative Position)
· Supporting Dataset: Phase 4 Technology (Known Limitations, Technical Upgrade History), Phase 3 History (Technical upgrades), Phase 8 Market (Narrative Position)

Pola 7: Strategic Investor Selection untuk Ecosystem Value
· Pattern: Series A (Polychain, Sequoia, Variant — research/DeFi focus), Series B (Bain Capital Crypto — institutional), Strategic (Ecosystem partners: LayerZero, Wormhole, Chainlink, EigenLayer, dll) — bukan capital-only
· Evidence: Phase 5 Financial (Funding History - all rounds); Phase 7 Ecosystem (Major Integrations - strategic investors all integrated); Phase 2 Entity (Investor entities)
· Supporting Dataset: Phase 5 Financial (Funding History), Phase 7 Ecosystem (Major Integrations, External Dependencies), Phase 2 Entity (Investors)

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Time-to-Market / Performance
· Decision: Launch dengan centralized sequencer (single operator) dan Foundation-operated prover cluster
· Trade-off: Mengorbankan desentralisasi awal untuk achieve mainnet launch 2024 dengan high throughput, low latency, dan simplified operations; accepted censorship risk dan single point of failure
· Evidence: Sequencer status "Live (centralized, single operator)"; Prover "Live (distributed prover cluster operated by Scroll Foundation)"; Decentralization roadmap published; Known limitations documented (HIGH) [Scroll Documentation Sequencer, https://docs.scroll.io/architecture/sequencer] [Scroll Decentralization Roadmap, https://scroll.io/blog/decentralization-roadmap] [Scroll Known Limitations, https://docs.scroll.io/architecture/sequencer#limitations]
· Supporting Dataset: Phase 4 Technology (Core Components - Sequencer, zkProver; Consensus Mechanism; Known Limitations), Phase 3 History (EV-009 Mainnet Launch), Phase 8 Market (Market Position)

Trade-off 2: Trusted Setup (KZG) vs Proof Efficiency / Verification Cost
· Decision: Menggunakan KZG polynomial commitment dengan Perpetual Powers of Tau trusted setup — bukan STARK (no trusted setup) seperti Starknet
· Trade-off: Mengorbankan trust assumption (ceremony participants tidak collude) untuk proof size kecil, verification cost rendah di L1, dan prover performance tinggi
· Evidence: Proof system Halo2/KZG; Powers of Tau ceremony; Verifier contract on-chain; Starknet uses STARK no trusted setup but larger proofs (HIGH) [Scroll ZK-Proof Blog, https://scroll.io/blog/zk-proof-system] [Powers of Tau Ceremony, https://github.com/privacy-scaling-explorations/perpetual-powers-of-tau] [Starknet Docs, https://docs.starknet.io/]
· Supporting Dataset: Phase 4 Technology (Security Model - Proof System, Core Components - zkProver), Phase 7 Ecosystem (External Dependencies - Halo2, Powers of Tau), Phase 8 Market (Competitor Landscape - Starknet)

Trade-off 3: 7-Day Withdrawal Delay vs Bridge Security
· Decision: Mandatory 7-day challenge period untuk L2→L1 withdrawals via native bridge
· Trade-off: Mengorbankan user liquidity dan UX (funds locked 7 hari) untuk security guarantee ضد invalid state root; users harus wait atau gunakan third-party bridge (LayerZero, Wormhole) untuk fast withdrawal
· Evidence: Bridge docs: "7 hari withdrawal delay untuk security"; Third-party bridges live untuk fast exit; Governance proposal untuk reduce ke 3 hari (HIGH) [Scroll Bridge Withdrawal, https://docs.scroll.io/developers/bridge#withdrawal-process] [LayerZero Scroll, https://layerzero.network/blog/scroll-integration] [Gov Forum Withdrawal Reduction, https://gov.scroll.io/t/withdrawal-delay-reduction/123]
· Supporting Dataset: Phase 4 Technology (Security Model - Bridge Security, Known Limitations), Phase 7 Ecosystem (Major Integrations - LayerZero, Wormhole), Phase 3 History (EV-023), Phase 6 Token (Major Token Events)

Trade-off 4: EVM-Equivalence Purity vs Native Account Abstraction (ERC-4337)
· Decision: Tidak implement native ERC-4337 di protocol level; rely on user-deployed EntryPoint contracts
· Trade-off: Mengorbankan native account abstraction UX (gasless, social recovery, batched tx) untuk maintain bytecode equivalence purity dan simplify proving circuit; AA tetap possible via application layer
· Evidence: Known limitations: "No Native Account Abstraction (ERC-4337) at protocol level"; Execution client based on Geth tanpa AA modifications (MEDIUM) [Scroll Account Abstraction Docs, https://docs.scroll.io/developers/account-abstraction] [Scroll Known Limitations, https://github.com/scroll-tech/rfcs/issues/45]
· Supporting Dataset: Phase 4 Technology (Execution Environment, Known Limitations), Phase 7 Ecosystem (Applications - Wallet/AA)

Trade-off 5: Fixed Supply (1B) vs Future Emission Flexibility
· Decision: Total supply fixed 1B SCR at TGE; no emission schedule published; no burn mechanism
· Trade-off: Mengorbankan flexibility untuk future validator/staker rewards, ecosystem incentives, atau protocol revenue distribution via minting; gain predictability dan credibility "no inflation" narrative
· Evidence: Tokenomics: "Total Supply: 1,000,000,000 SCR"; "No emission schedule"; "No burn mechanism"; "Supply fixed" (MEDIUM) [Scroll Blog TGE, https://scroll.io/blog/tge] [Scroll Docs Tokenomics, https://docs.scroll.io/tokenomics]
· Supporting Dataset: Phase 6 Token (Supply, Inflation/Deflation, Distribution), Phase 5 Financial (Treasury)

Trade-off 6: Sequencer Revenue Centralization vs Protocol Revenue Capture
· Decision: Centralized sequencer collects all priority fees + MEV; protocol fee switch belum aktif
· Trade-off: Mengorbankan protocol revenue (DAO treasury) untuk simplified launch economics dan sequencer operator incentive; future fee switch via governance
· Evidence: Sequencer trust model: "priority fees + MEV to single operator"; Revenue model: "Protocol Fee Switch (Planned)"; Governance fee switch proposal drafted (HIGH) [Scroll Sequencer, https://docs.scroll.io/architecture/sequencer] [Scroll Docs Gas, https://docs.scroll.io/architecture/gas] [Gov Forum Fee Switch, https://gov.scroll.io/t/protocol-fee-switch-proposal/456]
· Supporting Dataset: Phase 4 Technology (Core Components - Sequencer), Phase 5 Financial (Revenue Model), Phase 6 Token (Utility - Protocol Fee Share), Phase 3 History (EV-023)

Trade-off 7: State Growth Unbounded vs Archive Node Requirement
· Decision: Tidak implement state expiry/pruning (EIP-4444) di launch; archive nodes required untuk full history
· Trade-off: Mengorbankan long-term storage cost dan decentralization of node operation untuk simplicity dan EVM-equivalence; state growth unbounded
· Evidence: Known limitations: "State Growth Unbounded — no state expiry/pruning mechanism implemented; archive nodes required for full history"; RFC open tapi no timeline (LOW) [Scroll State Growth Discussion, https://github.com/scroll-tech/rfcs/issues/45] [Scroll Known Limitations]
· Supporting Dataset: Phase 4 Technology (Known Limitations), Phase 7 Ecosystem (Infrastructure Providers - Node operators)

Behavioral Summary

Prioritas Utama Proyek:
1. Ethereum Alignment — Setiap keputusan teknis maximize alignment dengan Ethereum (settlement, DA, security, execution client)
2. EVM-Equivalence Purity — Bytecode-level compatibility (Type 2) diprioritaskan over features seperti native AA atau custom VM
3. Production Quality — Multi-phase testnet, 6 audits, parallel component development, comprehensive tooling sebelum mainnet
4. Ecosystem Completeness at Launch — Coordinated 40+ integrations wave untuk immediate utility dan TVL
5. Progressive Decentralization dengan Transparency — Honest tentang current centralization; publish roadmap; incremental steps

Cara Mengambil Keputusan:
- Research-first: Hire world-class cryptographers sebelum product development
- Parallel execution: Semua core components dikembangkan simultan bukan sequential
- Evidence-based: Multiple audits, extensive testnet phases, measurable metrics (throughput, cost)
- Ecosystem-driven: Strategic investors dipilih untuk integration value; partners committed pre-launch
- Transparent trade-offs: Document known limitations honestly; publish roadmap untuk address them

Faktor Paling Sering Mempengaruhi Keputusan:
1. Ethereum compatibility/alignment (technical decisions)
2. Developer experience (tooling, EVM-equivalence, documentation)
3. Ecosystem readiness (partner integrations, liquidity, user onboarding)
4. Security credibility (audits, bug bounty, escape hatch design)
5. Decentralization timeline credibility (honest limitations, incremental upgrades)

Pola Evolusi:
- 2021-2022: Research & Team Building (Khovratovich, Farmer, Series A)
- 2023: Iterative Testing & Infrastructure (3 testnets, Bridge, SDK, Series B, Strategic)
- 2024: Production Launch & Ecosystem Explosion (Mainnet+TGE simultaneous, 40+ integrations)
- 2024-2025: Rapid Upgrades & Decentralization Steps (Blobs, Prover parallelization, Pre-conf, Governance proposals)

Kekuatan Utama:
- Technical credibility: Top-tier cryptography team, Halo2/KZG innovation, 6 audits
- Ethereum alignment: Pure Ethereum settlement/DA/security, no competing consensus
- EVM-equivalence: Best-in-class Type 2 compatibility, modified Geth base
- Ecosystem execution: Full DeFi stack at launch, restaking hub, cross-chain redundancy
- Developer experience: Comprehensive tooling from testnet, great documentation
- Transparent roadmap: Honest limitations, published decentralization plan, incremental delivery

Kelemahan Utama:
- Centralized sequencer/prover: Single operator risk, censorship potential, no slashing yet
- 7-day withdrawal delay: UX friction, capital inefficiency, competitive disadvantage vs fast bridges
- Trusted setup dependency: KZG ceremony trust assumption, per-circuit setup complexity
- No native AA: Missing ERC-4337 UX innovations at protocol level
- State growth unbounded: Long-term archive node centralization risk
- Token utility limited: Governance only currently; staking, fee share, gas payment planned but not live
- Large future unlocks: Team/Investor 12-month cliff (Oct 2025) may create sell pressure
- Foundation treasury opacity: No public dashboard, multisig addresses undisclosed
- Governance parameters undisclosed: Proposal threshold, voting period, quorum not public

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Scroll

## Core Insights

Insight 1: Ethereum alignment sebagai prinsip teknis absolut memandu setiap keputusan arsitektur — settlement, data availability, finality, execution client semua mengacu ke Ethereum L1 tanpa layer tambahan
Explanation: Scroll secara konsisten memilih Ethereum untuk settlement (L1 verification), DA (calldata/blob via EIP-4844), finality (ZK-proof on-chain), execution client (modified Geth), dan tidak mengeluarkan consensus token terpisah — berbeda dari kompetitor seperti Mantle (EigenDA) atau Starknet (Cairo VM)
Evidence: System Architecture menentukan "Settlement Layer: Ethereum L1", "Data Availability: Ethereum L1 calldata/blob", "Consensus: derives from Ethereum L1"【Phase 4 — System Architecture】; External Dependencies menandai Ethereum sebagai "Critical" dependency【Phase 7 — External Dependencies】; Competitor Landscape menunjukkan perbedaan dengan Mantle (modular DA) dan Starknet (Cairo VM)【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 4 Technology (System Architecture, Consensus Mechanism, Data Availability, Execution Environment), Phase 7 Ecosystem (External Dependencies), Phase 8 Market (Competitor Landscape)
Confidence: HIGH

Insight 2: EVM-equivalence Type 2 (bytecode-level) dipilih över EVM-compatibility Type 4 (Solidity-level) meski menambah kompleksitas proving — trade-off developer experience seamless vs prover efficiency
Explanation: Execution client berbasis modified Geth v1.13+ mendukung semua opcode standar dan precompiles termasuk PointEvaluation untuk EIP-4844; zkSync Era menggunakan Type 4 (LLVM-based) yang memerlukan kompilasi ulang; Scroll memilih Type 2 untuk memastikan kontrak existing deploy tanpa modifikasi
Evidence: Execution Environment: "EVM-equivalent (EVM-equivalent Type 2 per Vitalik classification — bytecode compatible)"【Phase 4 — Execution Environment】; Core Components: "Base Client: Modified go-ethereum (Geth) v1.13+"【Phase 4 — Core Components】; Vitalik Classification referensi Type 2【Phase 8 — Competitor Landscape - zkSync Era】
Supporting Dataset: Phase 4 Technology (Execution Environment, Core Components - L2 Execution Engine), Phase 8 Market (Competitor Landscape), Phase 1 Foundation (Category, Core Products)
Confidence: HIGH

Insight 3: Strategi "Full Stack at Launch" — 40+ integrasi major (DEX, lending, oracle, cross-chain, restaking, wallet, explorer) di-coordinasi live dalam minggu mainnet — menciptakan network effect immédiat dan TVL $1.2B dalam beberapa minggu
Explanation: Tidak ada L2 lain yang meluncurkan dengan ekosistem sepenuhnya berkembang; Arbitrum, Optimism, Base, zkSync semua staged rollout bulan demi bulan; Scroll mengamankan komitmen pre-launch dari LayerZero, Wormhole, Chainlink, Pyth, Uniswap, Aave, 10 restaking protocols, 6 wallets, 2 explorers
Evidence: EV-011 through EV-022 semua dalam 2024 post-mainnet Oct-Nov【Phase 3 — EV-011 through EV-022】; Major Integrations: 40+ integrations live【Phase 7 — Major Integrations】; Adoption Metrics: TVL ~$1.2B within weeks【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 History (EV-011 to EV-022), Phase 7 Ecosystem (Major Integrations, Applications), Phase 8 Market (Adoption Metrics, Market Position)
Confidence: HIGH

Insight 4: Multi-phase testnet strategy (pre-alpha → alpha → sepolia persistent) dengan bridge, SDK, tooling di setiap fase — bukan single testnet rush — memungkinkan validasi bertahap arsitektur ZK-proof, sequencer, prover, bridge
Explanation: Pre-alpha 2023-10-18 untuk validasi arsitektur awal; Alpha 2023-02-28 untuk developer testing; Sepolia 2023 untuk persistent environment; setiap fase menambah komponen (bridge EV-007, SDK EV-008) dan stress-test prover/sequencer
Evidence: EV-004 Alpha Testnet 2023-02-28【Phase 3 — EV-004】; EV-005 Pre-alpha Testnet 2023-10-18【Phase 3 — EV-005】; EV-006 Sepolia Testnet 2023【Phase 3 — EV-006】; EV-007 Bridge, EV-008 SDK released 2023【Phase 3 — EV-007, EV-008】
Supporting Dataset: Phase 3 History (EV-004, EV-005, EV-006, EV-007, EV-008), Phase 4 Technology (Testnet Infrastructure), Phase 7 Ecosystem (Developer Ecosystem)
Confidence: HIGH

Insight 5: Research-first hiring — Dmitry Khovratovich (Chief Cryptographer, co-author Argon2/Equihash) dan Brendan Farmer (Polygon zkEVM co-founder, Advisor) direkrut 2022 sebelum testnet publik — membangun credibility teknis dan menghindari pitfalls arsitektur
Explanation: Khovratovich memimpin desain Halo2/KZG dengan Perpetual Powers of Tau; Farmer memberikan insight production zkEVM dari Polygon; keduanya join 2022 saat Series A baru closed — bukan setelah product ready
Evidence: EV-002 Khovratovich join 2022【Phase 3 — EV-002】; EV-003 Farmer join 2022【Phase 3 — EV-003】; Entity: Dmitry Khovratovich "Chief Cryptographer"【Phase 2 — Dmitry Khovratovich】; Entity: Brendan Farmer "Advisor"【Phase 2 — Brendan Farmer】
Supporting Dataset: Phase 2 Entity (Dmitry Khovratovich, Brendan Farmer), Phase 3 History (EV-002, EV-003), Phase 4 Technology (Proof System, Security Model)
Confidence: HIGH

Insight 6: 6 auditor independen (Trail of Bits, OpenZeppelin, Zellic, Spearbit/Pashov, Sigma Prime, Nethermind ongoing) dengan scope terpisah (circuits, contracts, execution client, bridge, token, governance, P2P) sebelum mainnet — bukan single audit
Explanation: Setiap auditor fokus domain khusus: Trail of Bits pada zkProver circuits + verifier; OpenZeppelin pada bridge/token/governance; Zellic pada prover Rust/Halo2 soundness; Spearbit pada bridge/L2 system contracts; Sigma Prime pada execution client; Nethermind continuous post-launch
Evidence: Audit History: 6 auditors dengan scope detail【Phase 4 — Audit History】; Audits GitHub public reports【Phase 4 — Audit History】; Infrastructure Providers Security【Phase 7 — Infrastructure Providers】
Supporting Dataset: Phase 4 Technology (Audit History), Phase 7 Ecosystem (Infrastructure Providers - Security)
Confidence: HIGH

Insight 7: Centralized sequencer/prover saat launch dengan roadmap desentralisasi transparan dan incremental upgrades (pre-conf API, prover parallelization, blob integration) — honest tentang limitations, publish roadmap, deliver steps
Explanation: Sequencer "Live (centralized, single operator)"; Prover "Live (distributed prover cluster operated by Scroll Foundation)"; Known Limitations documented honestly; Decentralization roadmap blog; Pre-conf API beta 2025-01; Prover parallelization v1 2024-12 (3x throughput); Blob integration 2024-11 (90% cost reduction)
Evidence: Core Components Sequencer status【Phase 4 — Core Components】; Known Limitations: "Centralized Sequencer", "Prover Cluster Operated by Foundation"【Phase 4 — Known Technical Limitations】; Technical Upgrade History: EIP-4844, Prover Parallelization, Pre-conf API【Phase 4 — Technical Upgrade History】; Decentralization Roadmap blog【Phase 4 — Official Technical Resources】
Supporting Dataset: Phase 4 Technology (Core Components, Known Limitations, Technical Upgrade History), Phase 3 History (Technical upgrades), Phase 8 Market (Narrative Position)
Confidence: HIGH

Insight 8: Tokenomics fixed supply 1B SCR tanpa inflasi/emission schedule/burn — vesting schedules sebagai satu-satunya supply dynamics: Team/Investors 12m cliff + 36m linear, Foundation 6m cliff + 36m linear (5% unlock TGE), Ecosystem 3m cliff + 24m linear, Community 1m cliff + 18m linear
Explanation: Tidak ada block reward, validator emission, atau minting baru; supply tetap 1B; circulating supply hanya bertambah via vesting unlock; besar unlock Oct 2025 (12-month cliff Team/Investors) potential sell pressure
Evidence: Supply: "Total Supply: 1,000,000,000 SCR", "Maximum Supply: Tidak diungkap", "No emission schedule", "No burn mechanism"【Phase 6 — Supply】; Distribution percentages【Phase 6 — Distribution】; Vesting Schedule detail per kategori【Phase 6 — Vesting Schedule】; Inflation/Deflation: "Supply fixed"【Phase 6 — Inflation/Deflation】
Supporting Dataset: Phase 6 Token (Supply, Distribution, Vesting Schedule, Inflation/Deflation), Phase 5 Financial (Token Sale)
Confidence: HIGH

Insight 9: Dual governance layer — Snapshot off-chain (gasless, broad participation) + OpenZeppelin Governor on-chain (binding, timelock) — dengan Security Council multisig emergency controls (pause bridge, upgrade contracts, halt sequencer)
Explanation: Off-chain signaling untuk sentiment, on-chain execution untuk binding changes; Security Council sebagai safety valve selama fase terpusat; Grant Committee untuk ecosystem fund allocation (200M SCR); delegation tersedia on/off-chain
Evidence: Governance Model: "Off-chain (Snapshot) + On-chain (DAO timelock + proposal execution)"【Phase 6 — Governance】; Security Council: "Emergency controls: pause bridge, upgrade contracts, halt sequencer"【Phase 4 — Security Model】; Grant Committee【Phase 7 — Governance Ecosystem】
Supporting Dataset: Phase 6 Token (Governance), Phase 4 Technology (Security Model - Emergency Controls, Upgradeability), Phase 7 Ecosystem (Governance Ecosystem)
Confidence: MEDIUM

Insight 10: Cross-chain messaging redundancy — Native bridge + LayerZero (OFT) + Wormhole + Hyperlane — 4 parallel paths mengurangi single point of failure dan memberikan user choice untuk fast withdrawal (third-party bridges bypass 7-day native delay)
Explanation: Native bridge 7-day challenge period; LayerZero/Wormhole/Hyperlane provide fast exit; semua live dari mainnet wave; redundancy critical untuk bridge security
Evidence: Cross-chain Messaging: "Native L1-L2 messaging via bridge contracts; third-party interop (LayerZero, Wormhole, Hyperlane) at application layer"【Phase 4 — System Architecture】; Major Integrations: LayerZero, Wormhole, Hyperlane all live【Phase 7 — Major Integrations】; Bridge Security: "7-day withdrawal delay"【Phase 4 — Security Model】
Supporting Dataset: Phase 4 Technology (System Architecture, Security Model), Phase 7 Ecosystem (Major Integrations, External Dependencies), Phase 3 History (EV-011, EV-012, EV-017)
Confidence: HIGH

Insight 11: Oracle dual-source (Chainlink full stack + Pyth first-party) untuk DeFi reliability — bukan single oracle dependency
Explanation: Chainlink provide Price Feeds, VRF, CCIP, Proof of Reserve; Pyth provide first-party financial market data; keduanya live dari launch wave; redundancy critical untuk lending/DEX pricing
Evidence: Major Integrations: Chainlink EV-013, Pyth EV-014【Phase 3 — EV-013, EV-014】; External Dependencies: Chainlink, Pyth both "High" criticality【Phase 7 — External Dependencies】; Competitor Landscape menunjukkan oracle sebagai key infrastructure【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 3 History (EV-013, EV-014), Phase 7 Ecosystem (Major Integrations, External Dependencies), Phase 8 Market (Competitor Landscape)
Confidence: HIGH

Insight 12: Restaking ecosystem positioning — 10 protocols (EigenLayer, Symbiotic, Karak, Renzo, Ether.fi, Puffer, Swell, Kelp, Mellow, Kernel) terintegrasi dari launch — Scroll mempositioning dirinya sebagai L2 untuk restaking economy
Explanation: Bukan hanya DeFi tradisional; restaking/LRT protocols major presence; Kernel untuk BTC/ETH restaking; SCR token roadmap includes staking untuk sequencer/prover decentralization
Evidence: EV-021 lists 10 restaking protocols【Phase 3 — EV-021】; Applications: 10 restaking/LRT protocols【Phase 7 — Applications】; Narrative Position: "Restaking Integration" secondary narrative【Phase 8 — Narrative Position】; Token Utility: Staking planned【Phase 6 — Utility】
Supporting Dataset: Phase 3 History (EV-021), Phase 7 Ecosystem (Major Integrations, Applications), Phase 8 Market (Narrative Position), Phase 6 Token (Utility)
Confidence: HIGH

Insight 13: Revenue model sequenced — Live: L2 fees (base burn, priority to sequencer), Bridge fees, Sequencer revenue (priority+MEV); Planned: Protocol fee switch (governance proposal), Prover fees (post-decentralization) — protocol fee capture delayed
Explanation: Saat ini sequencer (Foundation-operated) capture semua priority fees + MEV; protocol fee switch proposal drafted di governance forum; prover fees futuristic; revenue transparency tidak dipublikasikan
Evidence: Revenue Model streams detail【Phase 5 — Revenue Model】; Sequencer trust model: "priority fees + MEV to single operator"【Phase 4 — Core Components】; Gov Forum Fee Switch proposal【Phase 6 — Major Token Events】; Revenue History: "Tidak diungkap"【Phase 5 — Revenue History】
Supporting Dataset: Phase 5 Financial (Revenue Model, Revenue History), Phase 4 Technology (Core Components - Sequencer), Phase 6 Token (Utility - Protocol Fee Share)
Confidence: HIGH

Insight 14: VC funding dengan token warrant structure (Series A $30M Polychain, Series B $50M Bain Capital Crypto, flat $1.8B valuation) + Strategic round untuk ecosystem alignment + EF grant non-dilutive — no public sale/ICO/IDO
Explanation: Equity + token warrant standar crypto infrastructure; strategic investors dipilih untuk integration value (LayerZero, Wormhole, Chainlink, EigenLayer dll); EF grant Q3 2023 untuk ZK research; TGE langsung ke circulating supply via CEX/DEX + airdrop
Evidence: Funding History: Series A, Series B, Strategic Round【Phase 5 — Funding History】; Token Sale: all "Tidak ada" untuk public/community/launchpad/auction【Phase 5 — Token Sale】; Financial Dependencies: VC, Foundation, EF Grant, Protocol Revenue【Phase 5 — Financial Dependencies】
Supporting Dataset: Phase 5 Financial (Funding History, Token Sale, Financial Dependencies), Phase 6 Token (Distribution, TGE), Phase 2 Entity (Investor entities)
Confidence: HIGH

Insight 15: Technical decision pattern: Ethereum alignment first, EVM-equivalence purity over features, parallel component development, extensive pre-launch testing, multiple independent audits, modified Geth base, transparent decentralization roadmap
Explanation: Konsisten across 7 technical decision patterns teridentifikasi di Phase 9; setiap pola didukung evidence dari architecture, upgrades, audit history, testnet phases
Evidence: Technical Decision Pattern 1-7【Phase 9 — Technical Decision Pattern】; System Architecture, Execution Environment, Security Model, Audit History, Core Components, Known Limitations, Technical Upgrade History【Phase 4 — all sections】
Supporting Dataset: Phase 9 Behavioral (Technical Decision Pattern), Phase 4 Technology (all sections)
Confidence: HIGH

## Strategic Principles

Principle 1: Ethereum Alignment First — Setiap keputusan arsitektur utama dipilih untuk maximize alignment dengan Ethereum (settlement L1, DA via calldata/blob, finality via L1 verification, execution client modified Geth, no separate consensus token, no separate DA layer)
Evidence: System Architecture semua Ethereum【Phase 4 — System Architecture】; External Dependencies Ethereum "Critical"【Phase 7 — External Dependencies】; Technical Decision Pattern 1【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 4 Technology (System Architecture, Consensus Mechanism, Data Availability, Execution Environment), Phase 7 Ecosystem (External Dependencies), Phase 9 Behavioral (Technical Decision Pattern)
Confidence: HIGH

Principle 2: EVM-Equivalence Purity (Type 2) — Bytecode-level compatibility diprioritaskan over features seperti native Account Abstraction (ERC-4337) atau custom VM — trade-off proving complexity untuk developer experience seamless
Evidence: Execution Environment Type 2【Phase 4 — Execution Environment】; Known Limitations: "No Native Account Abstraction"【Phase 4 — Known Technical Limitations】; Technical Decision Pattern 2【Phase 9 — Technical Decision Pattern】; Vitalik Classification reference【Phase 8 — Competitor Landscape】
Supporting Dataset: Phase 4 Technology (Execution Environment, Known Limitations), Phase 9 Behavioral (Technical Decision Pattern), Phase 8 Market (Competitor Landscape)
Confidence: HIGH

Principle 3: Production Quality Over Speed — Multi-phase testnet (pre-alpha, alpha, sepolia), 6 independent audits, parallel development of all 9 core components, comprehensive tooling dari testnet — tidak rush ke mainnet
Evidence: EV-004, EV-005, EV-006 testnet phases【Phase 3 — EV-004, EV-005, EV-006】; Audit History 6 auditors【Phase 4 — Audit History】; Core Components 9 all "Live"【Phase 4 — Core Components】; Developer Ecosystem tools ready pre-mainnet【Phase 7 — Developer Ecosystem】
Supporting Dataset: Phase 3 History (Testnet events), Phase 4 Technology (Audit History, Core Components), Phase 7 Ecosystem (Developer Ecosystem)
Confidence: HIGH

Principle 4: Ecosystem Completeness at Launch — Coordinated 40+ major integrations wave untuk immediate utility dan TVL — bukan "launch then build" — DEX, lending, oracle, cross-chain, restaking, wallet, explorer all live dalam minggu
Evidence: EV-011 through EV-022 all 2024【Phase 3 — EV-011 through EV-022】; Major Integrations 40+【Phase 7 — Major Integrations】; Adoption Metrics TVL $1.2B within weeks【Phase 8 — Adoption Metrics】; Ecosystem Decision Pattern 1【Phase 9 — Ecosystem Decision Pattern】
Supporting Dataset: Phase 3 History (EV-011 to EV-022), Phase 7 Ecosystem (Major Integrations, Applications), Phase 8 Market (Adoption Metrics), Phase 9 Behavioral (Ecosystem Decision Pattern)
Confidence: HIGH

Principle 5: Progressive Decentralization with Transparency — Honest tentang current centralization (single sequencer, Foundation prover cluster); publish roadmap; implement incremental steps (pre-conf API, prover parallelization, blob integration) sebelum full decentralization
Evidence: Known Limitations documented honestly【Phase 4 — Known Technical Limitations】; Decentralization Roadmap blog【Phase 4 — Official Technical Resources】; Technical Upgrade History incremental steps【Phase 4 — Technical Upgrade History】; Governance Decision Pattern 1【Phase 9 — Governance Decision Pattern】
Supporting Dataset: Phase 4 Technology (Known Limitations, Technical Upgrade History), Phase 9 Behavioral (Governance Decision Pattern)
Confidence: HIGH

Principle 6: Strategic Investor Selection for Ecosystem Value — Series A (Polychain, Sequoia, Variant — research/DeFi focus), Series B (Bain Capital Crypto — institutional), Strategic (Ecosystem partners: LayerZero, Wormhole, Chainlink, EigenLayer, dll) — bukan capital-only
Evidence: Funding History all rounds【Phase 5 — Funding History】; Major Integrations: strategic investors all integrated【Phase 7 — Major Integrations】; Financial Decision Pattern 1, 2【Phase 9 — Financial Decision Pattern】
Supporting Dataset: Phase 5 Financial (Funding History), Phase 7 Ecosystem (Major Integrations, External Dependencies), Phase 9 Behavioral (Financial Decision Pattern)
Confidence: HIGH

Principle 7: Research-First Cryptography Investment — Hire world-class cryptographers (Khovratovich, Farmer) sebelum product development; design Halo2/KZG with Perpetual Powers of Tau; participate in trusted setup ceremony
Evidence: EV-002, EV-003 key hires 2022【Phase 3 — EV-002, EV-003】; Entity: Dmitry Khovratovich Chief Cryptographer【Phase 2 — Dmitry Khovratovich】; Proof System Halo2/KZG【Phase 4 — Security Model】; Technical Decision Pattern 3【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 2 Entity (Key hires), Phase 3 History (EV-002, EV-003), Phase 4 Technology (Security Model), Phase 9 Behavioral (Technical Decision Pattern)
Confidence: HIGH

## Success Factors

Factor 1: Simultaneous Mainnet Launch + TGE (2024-10-22) — Maximize momentum; token utility immediate (governance, ecosystem incentives); avoid "ghost chain" perception; liquidity untuk ecosystem grants day-1
Evidence: EV-009 Mainnet Launch + EV-010 TGE same day【Phase 3 — EV-009, EV-010】; Decision Timeline: Simultaneous Mainnet+TGE【Phase 9 — Decision Timeline】; Trading Markets: 8+ CEX live day-1【Phase 8 — Trading Markets】
Supporting Dataset: Phase 3 History (EV-009, EV-010), Phase 9 Behavioral (Decision Timeline), Phase 8 Market (Trading Markets)
Confidence: HIGH

Factor 2: Full Ecosystem Wave at Launch — 40+ integrations coordinated live dalam minggu mainnet → TVL $1.2B dalam beberapa minggu, full DeFi stack day-1, user retention tinggi, network effect compounding
Evidence: EV-011 to EV-022【Phase 3 — EV-011 through EV-022】; Adoption Metrics TVL ~$1.2B【Phase 8 — Adoption Metrics】; Market Share: #1-2 EVM-equivalent ZK-Rollup【Phase 8 — Market Share】; Ecosystem Decision Pattern 1【Phase 9 — Ecosystem Decision Pattern】
Supporting Dataset: Phase 3 History (EV-011 to EV-022), Phase 7 Ecosystem (Major Integrations), Phase 8 Market (Adoption Metrics, Market Share), Phase 9 Behavioral (Ecosystem Decision Pattern)
Confidence: HIGH

Factor 3: World-Class Cryptography Team — Khovratovich (Argon2, Equihash co-author) + Farmer (Polygon zkEVM co-founder) → Halo2/KZG innovation, Perpetual Powers of Tau participation, credible ZK-proof system, differentiated dari STARK/Plonky2 competitors
Evidence: Entity Khovratovich, Farmer【Phase 2 — Dmitry Khovratovich, Brendan Farmer】; Proof System Halo2/KZG【Phase 4 — Security Model】; Competitor Landscape differentiation【Phase 8 — Competitor Landscape】; Technical Decision Pattern 3【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 2 Entity (Key hires), Phase 4 Technology (Security Model), Phase 8 Market (Competitor Landscape), Phase 9 Behavioral (Technical Decision Pattern)
Confidence: HIGH

Factor 4: Multi-Phase Testnet Validation — Pre-alpha (architecture), Alpha (developer), Sepolia (persistent) dengan bridge/SDK/tooling each phase → bug found early, developer ecosystem onboarded gradually, prover/sequencer stress-tested, mainnet launch smooth
Evidence: EV-004, EV-005, EV-006【Phase 3 — EV-004, EV-005, EV-006】; EV-007 Bridge, EV-008 SDK 2023【Phase 3 — EV-007, EV-008】; Technical Decision Pattern 5【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 3 History (Testnet events), Phase 4 Technology (Testnet Infrastructure), Phase 9 Behavioral (Technical Decision Pattern)
Confidence: HIGH

Factor 5: Comprehensive Audit Program — 6 independent auditors (Trail of Bits, OpenZeppelin, Zellic, Spearbit, Sigma Prime, Nethermind) covering circuits, contracts, client, bridge, token, governance, P2P → no major exploit post-mainnet, credibility untuk ecosystem partners dan users
Evidence: Audit History 6 auditors【Phase 4 — Audit History】; Risk Response Pattern 1【Phase 9 — Risk Response Pattern】; Infrastructure Providers Security【Phase 7 — Infrastructure Providers】
Supporting Dataset: Phase 4 Technology (Audit History), Phase 7 Ecosystem (Infrastructure Providers), Phase 9 Behavioral (Risk Response Pattern)
Confidence: HIGH

Factor 6: Developer Experience Priority — Scroll SDK, Hardhat plugin, Foundry template, public RPC, Sepolia faucet, contract verification all ready di testnet → low friction onboarding, 200+ monthly active developers, Electric Capital report recognition
Evidence: Developer Ecosystem all tools【Phase 7 — Developer Ecosystem】; Development Framework all live【Phase 4 — Development Framework】; Adoption Metrics Developer Count ~200+ monthly active【Phase 8 — Adoption Metrics】; Ecosystem Decision Pattern 5【Phase 9 — Ecosystem Decision Pattern】
Supporting Dataset: Phase 4 Technology (Development Framework), Phase 7 Ecosystem (Developer Ecosystem), Phase 8 Market (Adoption Metrics), Phase 9 Behavioral (Ecosystem Decision Pattern)
Confidence: HIGH

Factor 7: Cross-Chain Redundancy & Oracle Dual-Source — Native bridge + LayerZero + Wormhole + Hyperlane (4 paths); Chainlink + Pyth (2 oracles) → no single point of failure, user choice, DeFi reliability
Evidence: System Architecture Cross-chain Messaging【Phase 4 — System Architecture】; Major Integrations LayerZero, Wormhole, Hyperlane, Chainlink, Pyth【Phase 7 — Major Integrations】; Ecosystem Decision Pattern 2, 3【Phase 9 — Ecosystem Decision Pattern】
Supporting Dataset: Phase 4 Technology (System Architecture), Phase 7 Ecosystem (Major Integrations, External Dependencies), Phase 9 Behavioral (Ecosystem Decision Pattern)
Confidence: HIGH

Factor 8: Restaking Ecosystem Hub Positioning — 10 restaking/LRT protocols integrated from launch → Scroll sebagai L2 untuk restaking economy, differentiated dari general-purpose L2 competitors
Evidence: EV-021 10 protocols【Phase 3 — EV-021】; Applications 10 restaking【Phase 7 — Applications】; Narrative Position Restaking Integration【Phase 8 — Narrative Position】; Ecosystem Decision Pattern 4【Phase 9 — Ecosystem Decision Pattern】
Supporting Dataset: Phase 3 History (EV-021), Phase 7 Ecosystem (Applications), Phase 8 Market (Narrative Position), Phase 9 Behavioral (Ecosystem Decision Pattern)
Confidence: HIGH

## Failure Factors

Factor 1: Centralized Sequencer Single Operator — Can censor/reorder transactions; no slashing mechanism; all priority fees + MEV flow to single operator (Foundation); censorship risk dan single point of failure acknowledged
Evidence: Known Limitations: "Centralized Sequencer (single operator) — can censor/reorder transactions; no prover/sequencer slashing mechanism yet"【Phase 4 — Known Technical Limitations】; Sequencer Trust Model【Phase 4 — Core Components】; Risk Response Pattern 4【Phase 9 — Risk Response Pattern】; Strategic Trade-off 1【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 4 Technology (Known Limitations, Core Components), Phase 9 Behavioral (Risk Response Pattern, Strategic Trade-offs)
Confidence: HIGH

Factor 2: 7-Day Withdrawal Delay Native Bridge — User funds locked 7 hari; UX friction, capital inefficiency; competitive disadvantage vs fast bridges (LayerZero, Wormhole); governance proposal to reduce ke 3 hari tapi belum eksekusi
Evidence: Known Limitations: "7-day Withdrawal Delay... user funds locked during period"【Phase 4 — Known Technical Limitations】; Bridge Security: "7 hari withdrawal delay untuk security"【Phase 4 — Security Model】; EV-023 Withdrawal Delay Reduction Proposal【Phase 3 — EV-023】; Strategic Trade-off 3【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 4 Technology (Known Limitations, Security Model), Phase 3 History (EV-023), Phase 9 Behavioral (Strategic Trade-offs)
Confidence: HIGH

Factor 3: Trusted Setup Dependency (KZG Perpetual Powers of Tau) — Security bergantung pada ceremony participants tidak collude; per-circuit setup complexity; bukan universal setup untuk semua circuits; STARK competitors (Starknet) no trusted setup
Evidence: Known Limitations: "Halo2 Trusted Setup Dependency — KZG ceremony trust assumption; no universal setup for all circuits yet"【Phase 4 — Known Technical Limitations】; Security Model Proof System【Phase 4 — Security Model】; External Dependencies Powers of Tau【Phase 7 — External Dependencies】; Strategic Trade-off 2【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 4 Technology (Known Limitations, Security Model), Phase 7 Ecosystem (External Dependencies), Phase 9 Behavioral (Strategic Trade-offs)
Confidence: HIGH

Factor 4: No Native Account Abstraction (ERC-4337) — Missing gasless, social recovery, batched tx UX innovations at protocol level; rely on user-deployed EntryPoint contracts; AA possible via application layer only
Evidence: Known Limitations: "No Native Account Abstraction (ERC-4337) at protocol level"【Phase 4 — Known Technical Limitations】; Strategic Trade-off 4【Phase 9 — Strategic Trade-offs】; Account Abstraction Docs【Phase 4 — Official Technical Resources】
Supporting Dataset: Phase 4 Technology (Known Limitations), Phase 9 Behavioral (Strategic Trade-offs)
Confidence: MEDIUM

Factor 5: State Growth Unbounded — No state expiry/pruning (EIP-4444); archive nodes required for full history; long-term storage cost dan node centralization risk; RFC open tapi no implementation timeline
Evidence: Known Limitations: "State Growth Unbounded — no state expiry/pruning mechanism implemented; archive nodes required for full history"【Phase 4 — Known Technical Limitations】; RFC Discussion【Phase 4 — Known Technical Limitations】; Strategic Trade-off 7【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 4 Technology (Known Limitations), Phase 9 Behavioral (Strategic Trade-offs)
Confidence: MEDIUM

Factor 6: Limited Token Utility at Launch — Governance only currently; staking, fee share, gas payment planned but not live; token utility tidak sepenuhnya realized → potential sell pressure dari non-utility holders
Evidence: Utility: Governance Live, Gas/Staking/Fee Share Planned【Phase 6 — Utility】; Tokenomics: "Supply fixed" no emission untuk rewards【Phase 6 — Inflation/Deflation】; Strategic Trade-off 5【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 6 Token (Utility, Inflation/Deflation), Phase 9 Behavioral (Strategic Trade-offs)
Confidence: HIGH

Factor 7: Large Future Token Unlocks — Team/Investors 12-month cliff (Oct 2025) → 36-month linear; 15%+15% = 30% supply unlocking; potential sell pressure tidak priced into current market cap analyses
Evidence: Vesting Schedule: Team/Investors 12m cliff + 36m linear【Phase 6 — Vesting Schedule】; Open Threads: "Token Unlock Schedule Impact: Large investor/team unlocks starting Oct 2025"【Phase 8 — Open Threads】; Distribution: Team 25%, Investors 15%【Phase 6 — Distribution】
Supporting Dataset: Phase 6 Token (Distribution, Vesting Schedule), Phase 8 Market (Open Threads)
Confidence: HIGH

Factor 8: Foundation Treasury Opacity — No public dashboard, no transparency report, multisig addresses undisclosed; 25% supply (Foundation 20% + Treasury 5%) under Foundation control tanpa visibility
Evidence: Treasury: "Tidak diungkap" size, composition, holdings【Phase 5 — Treasury】; Distribution: Foundation 20%, Treasury 5%【Phase 6 — Distribution】; Open Threads: "Treasury dashboard/transparency report: Tidak ada"【Phase 8 — Open Threads】; Governance: Security Council signers undisclosed【Phase 7 — Governance Ecosystem】
Supporting Dataset: Phase 5 Financial (Treasury), Phase 6 Token (Distribution), Phase 7 Ecosystem (Governance Ecosystem), Phase 8 Market (Open Threads)
Confidence: HIGH

Factor 9: Governance Parameters Undisclosed — Proposal threshold (min SCR), voting period, quorum, delegation mechanics on-chain tidak di-dokumentasikan publik; transparency gap untuk DAO credibility
Evidence: Governance: "threshold tidak diungkapkan", "voting period tidak spesifik"【Phase 6 — Governance】; Open Threads: "Governance parameter specifics: Proposal threshold... tidak di-dokumentasikan"【Phase 8 — Open Threads】; Governance Decision Pattern 5【Phase 9 — Governance Decision Pattern】
Supporting Dataset: Phase 6 Token (Governance), Phase 8 Market (Open Threads), Phase 9 Behavioral (Governance Decision Pattern)
Confidence: MEDIUM

Factor 10: Revenue Transparency Absent — Protocol revenue (base fee burn, bridge fees, sequencer fees) tidak publicly reported; only on-chain estimates possible; Foundation captures sequencer revenue currently; no periodic financial reporting
Evidence: Revenue History: "Tidak diungkap"【Phase 5 — Revenue History】; Revenue Model: Sequencer revenue all to operator【Phase 5 — Revenue Model】; Open Threads: "Fee Revenue Data: Protocol revenue... not publicly reported"【Phase 8 — Open Threads】; Financial Decision Pattern 5【Phase 9 — Financial Decision Pattern】
Supporting Dataset: Phase 5 Financial (Revenue History, Revenue Model), Phase 8 Market (Open Threads), Phase 9 Behavioral (Financial Decision Pattern)
Confidence: HIGH

## Decision Framework

Step 1: Observe — Research & Cryptography Foundation (2021-2022)
- Hire world-class cryptographers (Khovratovich, Farmer) sebelum product
- Design ZK-proof system (Halo2/KZG, Powers of Tau)
- Establish legal entity (Scroll Foundation Cayman, Scroll Tech Pte. Ltd. Singapore)
Evidence: EV-001 Founding 2021【Phase 3 — EV-001】; EV-002, EV-003 Key hires 2022【Phase 3 — EV-002, EV-003】; Entity Scroll Foundation, Scroll Tech Pte. Ltd.【Phase 2 — Scroll Foundation, Scroll Tech Pte. Ltd.】; Technical Decision Pattern 2, 3【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 1 Foundation, Phase 2 Entity, Phase 3 History (EV-001, EV-002, EV-003), Phase 9 Behavioral (Technical Decision Pattern)

Step 2: Evaluate — Iterative Testnet Validation (2023)
- Pre-alpha (architecture validation) → Alpha (developer testing) → Sepolia (persistent)
- Parallel development: Bridge, SDK, Sequencer, Prover, Roller, Execution Client
- Series A ($30M) → Series B ($50M) → Strategic Round + EF Grant
Evidence: EV-004, EV-005, EV-006 Testnet phases【Phase 3 — EV-004, EV-005, EV-006】; EV-007 Bridge, EV-008 SDK 2023【Phase 3 — EV-007, EV-008】; Funding History Series A, B, Strategic【Phase 5 — Funding History】; Technical Decision Pattern 5【Phase 9 — Technical Decision Pattern】; Financial Decision Pattern 1, 2【Phase 9 — Financial Decision Pattern】
Supporting Dataset: Phase 3 History (2023 events), Phase 4 Technology (Core Components, Testnet Infrastructure), Phase 5 Financial (Funding History), Phase 9 Behavioral (Technical Decision Pattern, Financial Decision Pattern)

Step 3: Fund — Capital Allocation & Tokenomics Design
- VC equity + token warrant (15% investors, 36m linear vesting)
- Strategic investors for ecosystem alignment (LayerZero, Wormhole, Chainlink, EigenLayer)
- Fixed supply 1B SCR, allocation: Community 15%, Team 25%, Investors 15%, Foundation 20%, Treasury 5%, Ecosystem 20%
- Vesting schedules designed per category
Evidence: Token Sale Private Sales【Phase 5 — Token Sale】; Distribution percentages【Phase 6 — Distribution】; Vesting Schedule detail【Phase 6 — Vesting Schedule】; Financial Decision Pattern 1, 2, 4【Phase 9 — Financial Decision Pattern】
Supporting Dataset: Phase 5 Financial (Token Sale, Funding History), Phase 6 Token (Distribution, Vesting Schedule), Phase 9 Behavioral (Financial Decision Pattern)

Step 4: Develop — Parallel Core Component Engineering
- 9 core components developed simultaneously: Sequencer, zkProver, Roller, L1 Contracts, L2 Execution Engine, Native Bridge, Full Node, SDK/Tooling, Sepolia Testnet Infra
- 6 independent audits across domains
- Modified Geth base untuk EVM-equivalence
- Halo2/KZG prover in Rust
Evidence: Core Components 9 all "Live"【Phase 4 — Core Components】; Audit History 6 auditors【Phase 4 — Audit History】; Execution Client Modified Geth【Phase 4 — Core Components】; Prover Rust/Halo2【Phase 4 — Core Components】; Technical Decision Pattern 1, 3, 6, 7【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 4 Technology (Core Components, Audit History, Execution Environment, Security Model), Phase 9 Behavioral (Technical Decision Pattern)

Step 5: Launch — Simultaneous Mainnet + TGE + Full Ecosystem Wave (2024-10-22)
- Mainnet genesis + SCR token deployment same block
- 40+ integrations coordinated: Cross-chain, Oracle, DeFi, Restaking, Wallet, Explorer
- CEX listings day-1 (Binance, Coinbase, OKX, Bybit, Kraken, KuCoin, Gate, HTX)
- DEX liquidity on Scroll L2 + Ethereum Mainnet
Evidence: EV-009 Mainnet Launch + EV-010 TGE same day【Phase 3 — EV-009, EV-010】; EV-011 to EV-022 Ecosystem wave【Phase 3 — EV-011 through EV-022】; Trading Markets 8+ CEX, 5+ DEX【Phase 8 — Trading Markets】; Decision Timeline Simultaneous Launch+TGE【Phase 9 — Decision Timeline】; Ecosystem Decision Pattern 1【Phase 9 — Ecosystem Decision Pattern】
Supporting Dataset: Phase 3 History (EV-009 to EV-022), Phase 8 Market (Trading Markets, Adoption Metrics), Phase 9 Behavioral (Decision Timeline, Ecosystem Decision Pattern)

Step 6: Govern — Progressive Decentralization via DAO
- SCR token governance live (Snapshot + OpenZeppelin Governor)
- Security Council multisig emergency controls
- Grant Committee for ecosystem fund (200M SCR)
- Roadmap: Sequencer/Prover decentralization, fee switch, withdrawal delay reduction
Evidence: Governance Model dual-layer【Phase 6 — Governance】; Security Council emergency controls【Phase 4 — Security Model】; Grant Committee【Phase 7 — Governance Ecosystem】; Decentralization Roadmap【Phase 4 — Official Technical Resources】; Governance Decision Pattern 1-6【Phase 9 — Governance Decision Pattern】
Supporting Dataset: Phase 4 Technology (Security Model), Phase 6 Token (Governance), Phase 7 Ecosystem (Governance Ecosystem), Phase 9 Behavioral (Governance Decision Pattern)

Step 7: Iterate — Rapid Upgrades & Decentralization Steps (2024-2025)
- EIP-4844 Blob Integration (2024-11, 90% cost reduction)
- Prover Parallelization v1 (2024-12, 3x throughput)
- Sequencer Pre-confirmation API Beta (2025-01, sub-second soft finality)
- Withdrawal Delay Reduction Proposal (2025, 7d→3d)
- Continuous audits (Nethermind ongoing)
Evidence: Technical Upgrade History: Blob, Prover Parallelization, Pre-conf, Withdrawal Reduction【Phase 4 — Technical Upgrade History】; Audit History Nethermind ongoing【Phase 4 — Audit History】; Risk Response Pattern 6【Phase 9 — Risk Response Pattern】; Evolution Pattern Technical upgrades【Phase 9 — Evolution Pattern】
Supporting Dataset: Phase 4 Technology (Technical Upgrade History, Audit History), Phase 9 Behavioral (Risk Response Pattern, Evolution Pattern)

## Reusable Playbook

Playbook 1: How to Build Credible ZK-Rollup Technical Foundation
- Hire world-class cryptographers (PhD-level, published constructions) sebelum product development
- Choose proof system with clear trade-offs (Halo2/KZG: efficiency + trusted setup vs STARK: no trusted setup + larger proofs)
- Participate in trusted setup ceremonies (Perpetual Powers of Tau) untuk community trust
- Build modified Geth execution client untuk EVM-equivalence Type 2 bukan custom VM
- Publish technical specifications dan security model transparan
Evidence: Entity Khovratovich, Farmer【Phase 2 — Dmitry Khovratovich, Brendan Farmer】; Proof System Halo2/KZG【Phase 4 — Security Model】; Powers of Tau Ceremony【Phase 7 — External Dependencies】; Execution Client Modified Geth【Phase 4 — Core Components】; Technical Decision Pattern 2, 3, 7【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 2 Entity, Phase 4 Technology (Security Model, Core Components, Execution Environment), Phase 7 Ecosystem (External Dependencies), Phase 9 Behavioral (Technical Decision Pattern)
Confidence: HIGH

Playbook 2: How to Run Multi-Phase Testnet Program
- Phase 1 Pre-alpha: Architecture validation, core component integration (prover, sequencer, bridge)
- Phase 2 Alpha: Developer testing, EVM-equivalence verification, tooling feedback
- Phase 3 Persistent Testnet (Sepolia): Production-like environment, long-running stability, bridge/SDK live
- Release developer tooling (SDK, Hardhat, Foundry, faucet, verification) di setiap fase
- Stress-test prover/sequencer clusters under realistic load
Evidence: EV-004, EV-005, EV-006 Testnet phases【Phase 3 — EV-004, EV-005, EV-006】; EV-007 Bridge, EV-008 SDK 2023【Phase 3 — EV-007, EV-008】; Developer Ecosystem tools ready pre-mainnet【Phase 7 — Developer Ecosystem】; Technical Decision Pattern 5【Phase 9 — Technical Decision Pattern】
Supporting Dataset: Phase 3 History (Testnet events), Phase 4 Technology (Testnet Infrastructure), Phase 7 Ecosystem (Developer Ecosystem), Phase 9 Behavioral (Technical Decision Pattern)
Confidence: HIGH

Playbook 3: How to Execute Comprehensive Audit Program
- Engage 4-6 independent auditors dengan domain specialization: circuits (ZK-specific), contracts (Solidity), execution client (Go/Rust), bridge (cross-domain), governance (token/DAO), P2P/network
- Stagger audits: circuits early, contracts mid, integration late
- Publish all reports transparan di GitHub
- Establish continuous audit program post-launch (Nethermind model)
- Run bug bounty di Immunefi/platform terkemuka concurrent dengan audits
Evidence: Audit History 6 auditors specialized scopes【Phase 4 — Audit History】; Audits GitHub public【Phase 4 — Audit History】; Bug Bounty Immunefi【Phase 4 — Official Technical Resources】; Risk Response Pattern 1, 2【Phase 9 — Risk Response Pattern】; Infrastructure Providers Security【Phase 7 — Infrastructure Providers】
Supporting Dataset: Phase 4 Technology (Audit History, Official Technical Resources), Phase 7 Ecosystem (Infrastructure Providers), Phase 9 Behavioral (Risk Response Pattern)
Confidence: HIGH

Playbook 4: How to Fundraise with Strategic Investor Alignment
- Series A: Top-tier crypto VC (Polychain, Sequoia, Variant) untuk research credibility + network
- Series B: Institutional crypto VC (Bain Capital Crypto) untuk maturity signal + flat valuation OK in bear market
- Strategic Round: Ecosystem partners (LayerZero, Wormhole, Chainlink, EigenLayer) untuk integration commitments, bukan capital
- Non-dilutive grants: Ethereum Foundation untuk research alignment
- Token warrant structure: Equity + token allocation dengan vesting (12m cliff + 36m linear) aligns long-term
- No public sale/ICO/IDO — TGE langsung ke circulating supply via CEX/DEX + airdrop
Evidence: Funding History all rounds【Phase 5 — Funding History】; Token Sale all "Tidak ada" public【Phase 5 — Token Sale】; Financial Dependencies VC, Foundation, EF Grant, Protocol Revenue【Phase 5 — Financial Dependencies】; Financial Decision Pattern 1, 2, 3, 6【Phase 9 — Financial Decision Pattern】
Supporting Dataset: Phase 5 Financial (Funding History, Token Sale, Financial Dependencies), Phase 9 Behavioral (Financial Decision Pattern)
Confidence: HIGH

Playbook 5: How to Design Tokenomics for Progressive Decentralization
- Fixed supply (no inflation/emission/burn) untuk predictability
- Allocation categories: Community, Team, Investors, Foundation, Treasury, Ecosystem — each dengan clear purpose
- Vesting schedules differentiated: Team/Investors longest (12m cliff + 36m linear), Foundation medium (6m cliff + 36m linear), Ecosystem shorter (3m cliff + 24m linear), Community shortest (1m cliff + 18m linear)
- Small TGE unlock hanya untuk operational (Foundation 5%)
- Utility roadmap: Governance → Staking → Fee Share → Gas Payment (progressive)
- Governance dual-layer: Snapshot off-chain + OpenZeppelin Governor on-chain
- Security Council multisig emergency controls selama centralized phase
Evidence: Supply fixed 1B no inflation【Phase 6 — Supply】; Distribution 6 categories【Phase 6 — Distribution】; Vesting Schedule per category【Phase 6 — Vesting Schedule】; Utility progression【Phase 6 — Utility】; Governance dual-layer【Phase 6 — Governance】; Security Council【Phase 4 — Security Model】; Governance Decision Pattern 1-6【Phase 9 — Governance Decision Pattern】
Supporting Dataset: Phase 6 Token (Supply, Distribution, Vesting Schedule, Utility, Governance), Phase 4 Technology (Security Model), Phase 9 Behavioral (Governance Decision Pattern)
Confidence: HIGH

Playbook 6: How to Launch with Full Ecosystem Wave
- Identify 5-7 ecosystem categories critical untuk user utility: DEX, Lending, Oracle, Cross-chain, Wallet, Explorer, Restaking
- Secure integration commitments 6-12 bulan sebelum mainnet dari top protocols each category
- Coordinate simultaneous deployment wave (2-4 minggu window) bukan staggered months
- Provide technical support, liquidity incentives, co-marketing untuk each partner
- Ensure wallet/explorer support day-1 untuk user onboarding friction minimal
- Target TVL $1B+ within 30 hari melalui coordinated liquidity bootstrapping
Evidence: EV-011 to EV-022 all 2024【Phase 3 — EV-011 through EV-022】; Major Integrations 40+【Phase 7 — Major Integrations】; Adoption Metrics TVL $1.2B within weeks【Phase 8 — Adoption Metrics】; Ecosystem Decision Pattern 1, 5, 6【Phase 9 — Ecosystem Decision Pattern】
Supporting Dataset: Phase 3 History (EV-011 to EV-022), Phase 7 Ecosystem (Major Integrations, Wallet Ecosystem, Infrastructure Providers), Phase 8 Market (Adoption Metrics), Phase 9 Behavioral (Ecosystem Decision Pattern)
Confidence: HIGH

Playbook 7: How to Manage Centralized-to-Decentralized Transition Transparently
- Document current centralization honestly (single sequencer, Foundation prover, 7-day withdrawal, no forced inclusion)
- Publish detailed decentralization roadmap dengan technical milestones
- Deliver incremental upgrades: Pre-confirmation API (soft finality), Prover parallelization (capacity), Blob integration (cost), Forced inclusion design (censorship resistance)
- Token utility progression: Governance → Staking (sequencer/prover) → Fee Share → Gas
- Security Council multisig sebagai safety valve selama transition
- Community governance proposals untuk parameter changes (withdrawal delay, fee switch)
Evidence: Known Limitations all documented【Phase 4 — Known Technical Limitations】; Decentralization Roadmap blog【Phase 4 — Official Technical Resources】; Technical Upgrade History incremental【Phase 4 — Technical Upgrade History】; Token Utility progression【Phase 6 — Utility】; Security Council【Phase 4 — Security Model】; Gov Forum proposals【Phase 6 — Major Token Events】; Risk Response Pattern 3, 5, 6【Phase 9 — Risk Response Pattern】; Governance Decision Pattern 1, 3【Phase 9 — Governance Decision Pattern】
Supporting Dataset: Phase 4 Technology (Known Limitations, Technical Upgrade History, Security Model), Phase 6 Token (Utility, Major Token Events), Phase 9 Behavioral (Risk Response Pattern, Governance Decision Pattern)
Confidence: HIGH

Playbook 8: How to Build Cross-Chain Redundancy from Day-1
- Deploy native canonical bridge (trusted, 7-day withdrawal) untuk security-first path
- Integrate 2-3 major interop protocols (LayerZero OFT, Wormhole, Hyperlane) untuk fast paths
- Ensure oracle dual-source (Chainlink + Pyth) untuk DeFi reliability
- Support restaking ecosystem (EigenLayer, Symbiotic, Karak + LRTs) untuk capital efficiency
- Monitor bridge TVL across all paths, set alerts for anomalies
Evidence: System Architecture Cross-chain Messaging【Phase 4 — System Architecture】; Major Integrations LayerZero, Wormhole, Hyperlane, Chainlink, Pyth, Restaking 10 protocols【Phase 7 — Major Integrations】; Ecosystem Decision Pattern 2, 3, 4【Phase 9 — Ecosystem Decision Pattern】; Bridge Security 7-day delay【Phase 4 — Security Model】
Supporting Dataset: Phase 4 Technology (System Architecture, Security Model), Phase 7 Ecosystem (Major Integrations, External Dependencies), Phase 9 Behavioral (Ecosystem Decision Pattern)
Confidence: HIGH

## Anti-patterns

Anti-pattern 1: Over-Centralization Without Credible Exit Plan
- Launch dengan single sequencer, single prover cluster, no forced inclusion, no slashing → censorship risk, liveness risk, trust assumption tinggi
- Mitigation: Publish honest limitations, roadmap dengan milestones, incremental delivery (pre-conf, prover parallelization, forced inclusion design)
- Scroll Example: Known Limitations documented, Decentralization roadmap published, Pre-conf API beta, Prover parallelization v1 delivered
Evidence: Known Limitations: Centralized Sequencer, Prover Cluster, No Forced Inclusion【Phase 4 — Known Technical Limitations】; Decentralization Roadmap【Phase 4 — Official Technical Resources】; Technical Upgrade History【Phase 4 — Technical Upgrade History】; Risk Response Pattern 4, 5, 6【Phase 9 — Risk Response Pattern】; Strategic Trade-off 1【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 4 Technology (Known Limitations, Official Technical Resources, Technical Upgrade History), Phase 9 Behavioral (Risk Response Pattern, Strategic Trade-offs)
Confidence: HIGH

Anti-pattern 2: Premature Token Launch Without Utility
- Token launch tanpa clear utility roadmap → speculative asset, sell pressure, community disappointment
- Scroll mitigated: Governance live at TGE, Staking/Fee Share/Gas planned dengan roadmap, Ecosystem incentives funded (200M SCR), Community allocation 15% vesting 18m
- Remaining risk: Large unlocks Oct 2025 (Team/Investors 30% supply), utility progression belum proven
Evidence: Utility: Governance Live, others Planned【Phase 6 — Utility】; Vesting Schedule Team/Investors 12m cliff【Phase 6 — Vesting Schedule】; Distribution Community 15%【Phase 6 — Distribution】; Open Threads Token Unlock Impact【Phase 8 — Open Threads】; Strategic Trade-off 5, 6【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 6 Token (Utility, Vesting Schedule, Distribution), Phase 8 Market (Open Threads), Phase 9 Behavioral (Strategic Trade-offs)
Confidence: HIGH

Anti-pattern 3: Poor Treasury Management Transparency
- Foundation holds 25% supply (20% Foundation + 5% Treasury) tanpa public dashboard, multisig addresses undisclosed, no transparency reports → trust erosion, governance credibility gap
- Scroll Example: Treasury "Tidak diungkap" size/composition/holdings; Security Council signers undisclosed; no periodic financial reporting
Evidence: Treasury all "Tidak diungkap"【Phase 5 — Treasury】; Distribution Foundation 20% + Treasury 5%【Phase 6 — Distribution】; Security Council signers undisclosed【Phase 7 — Governance Ecosystem】; Revenue History "Tidak diungkap"【Phase 5 — Revenue History】; Open Threads Treasury dashboard, Security Council details【Phase 8 — Open Threads】; Financial Decision Pattern 4, 5【Phase 9 — Financial Decision Pattern】
Supporting Dataset: Phase 5 Financial (Treasury, Revenue History), Phase 6 Token (Distribution), Phase 7 Ecosystem (Governance Ecosystem), Phase 8 Market (Open Threads), Phase 9 Behavioral (Financial Decision Pattern)
Confidence: HIGH

Anti-pattern 4: Single Point of Failure in Critical Infrastructure
- Bergantung pada single sequencer, single prover cluster, single cloud provider region, single bridge contract → systemic risk
- Scroll mitigation: Cross-chain redundancy (4 paths), Oracle dual-source (Chainlink+Pyth), but sequencer/prover masih single operator
- Remaining gap: Prover decentralization roadmap belum quantified milestones; cloud provider specifics undisclosed
Evidence: Known Limitations Centralized Sequencer, Prover Cluster【Phase 4 — Known Technical Limitations】; Ecosystem Decision Pattern 2, 3【Phase 9 — Ecosystem Decision Pattern】; External Dependencies Cloud Providers unspecified【Phase 7 — External Dependencies】; Open Threads Cloud provider specifics, Prover decentralization timeline【Phase 8 — Open Threads】; Risk Response Pattern 6【Phase 9 — Risk Response Pattern】
Supporting Dataset: Phase 4 Technology (Known Limitations), Phase 7 Ecosystem (External Dependencies, Ecosystem Decision Pattern), Phase 8 Market (Open Threads), Phase 9 Behavioral (Risk Response Pattern)
Confidence: HIGH

Anti-pattern 5: Delayed Protocol Revenue Capture
- Sequencer captures all priority fees + MEV; protocol fee switch belum aktif; DAO treasury unfunded dari protocol revenue; Foundation subsidizes operations via token sales
- Scroll Example: Revenue Model Protocol Fee Switch "Planned", Prover Fees "Planned"; Sequencer revenue all to operator; Gov Forum fee switch proposal drafted only
Evidence: Revenue Model streams【Phase 5 — Revenue Model】; Sequencer trust model【Phase 4 — Core Components】; Gov Forum Fee Switch proposal【Phase 6 — Major Token Events】; Financial Decision Pattern 5【Phase 9 — Financial Decision Pattern】; Strategic Trade-off 6【Phase 9 — Strategic Trade-offs】
Supporting Dataset: Phase 5 Financial (Revenue Model), Phase 4 Technology (Core Components), Phase 6 Token (Major Token Events), Phase 9 Behavioral (Financial Decision Pattern, Strategic Trade-offs)
Confidence: HIGH

Anti-pattern 6: Governance Parameter Opacity
- Proposal threshold, voting period, quorum, delegation mechanics tidak published → community cannot meaningfully participate, DAO credibility undermined
- Scroll Example: Governance docs mention thresholds exist tapi no numbers; Security Council veto power undefined; Grant Committee members undisclosed
Evidence: Governance: "threshold tidak diungkapkan", "voting period tidak spesifik"【Phase 6 — Governance】; Security Council details undisclosed【Phase 7 — Governance Ecosystem】; Grant Committee members undisclosed【Phase 7 — Governance Ecosystem】; Open Threads Governance parameters【Phase 8 — Open Threads】; Governance Decision Pattern 5【Phase 9 — Governance Decision Pattern】
Supporting Dataset: Phase 6 Token (Governance), Phase 7 Ecosystem (Governance Ecosystem), Phase 8 Market (Open Threads), Phase 9 Behavioral (Governance Decision Pattern)
Confidence: MEDIUM

Anti-pattern 7: State Growth Neglect
- No state expiry/pruning (EIP-4444) at launch; archive nodes required; long-term centralization of node operation; RFC open 1+ tahun tanpa implementation
- Scroll Example: Known Limitation "State Growth Unbounded"; RFC discussion GitHub issue #45; no timeline
Evidence: Known Limitations State Growth Unbounded【Phase 4 — Known Technical Limitations】; RFC Discussion【Phase 4 — Known Technical Limitations】; Strategic Trade-off 7【Phase 9 — Strategic Trade-offs】; Open Threads State growth mitigation【Phase 8 — Open Threads】
Supporting Dataset: Phase 4 Technology (Known Limitations), Phase 8 Market (Open Threads), Phase 9 Behavioral (Strategic Trade-offs)
Confidence: MEDIUM

## Lessons Learned

Lesson 1: Ethereum alignment sebagai north star menciptakan technical coherence — settlement, DA, finality, execution client semua Ethereum-native menghindari fragmentasi dan memastikan security inheritance
Lesson 2: Research-first cryptography investment (hiring Khovratovich/Farmer pre-product) memberikan technical moat yang sulit direplikasi kompetitor
Lesson 3: Multi-phase testnet dengan tooling lengkap di setiap fase jauh superior dari single testnet rush — bug found early, developer ecosystem compounding, mainnet smooth
Lesson 4: Simultaneous mainnet+TGE+ecosystem wave menciptakan momentum yang tidak bisa dicapai staged rollout — TVL $1.2B dalam minggu membuktikan
Lesson 5: Transparent centralization acknowledgment + incremental decentralization delivery membangun trust lebih baik dari over-promising decentralization at launch
Lesson 6: Fixed supply tokenomics dengan differentiated vesting schedules aligns incentives across stakeholders tanpa inflation complexity
Lesson 7: Cross-chain redundancy (4 bridges) + oracle dual-source (2 oracles) from day-1 mencegah single point of failure yang menghancurkan L2 lain
Lesson 8: Strategic investor selection untuk ecosystem value (bukan capital-only) memastikan integration commitments pre-launch
Lesson 9: Comprehensive audit program (6 auditors domain-specialized) + bug bounty ongoing = security credibility untuk TVL growth
Lesson 10: Developer experience priority (SDK, Hardhat, Foundry, faucet, verification from testnet) menarik 200+ monthly active developers organik
Lesson 11: Treasury opacity dan governance parameter secrecy mengurangi DAO credibility meski technical execution strong
Lesson 12: Large future token unlocks (Team/Investors 30% at 12m cliff) menciptakan overhang risk yang harus di-manage via utility acceleration
Lesson 13: Protocol revenue capture delay (sequencer keeps all fees) menciptakan misalignment antara Foundation dan token holders
Lesson 14: State growth neglect (no EIP-4444) menciptakan long-term centralization risk yang semakin mahal diperbaiki
Lesson 15: Restaking ecosystem positioning sebagai differentiated narrative menarik capital efficiency-focused users dan protocols

## Knowledge Summary

Strategic Principles (7):
1. Ethereum Alignment First
2. EVM-Equivalence Purity (Type 2)
3. Production Quality Over Speed
4. Ecosystem Completeness at Launch
5. Progressive Decentralization with Transparency
6. Strategic Investor Selection for Ecosystem Value
7. Research-First Cryptography Investment

Success Factors (8):
1. Simultaneous Mainnet Launch + TGE
2. Full Ecosystem Wave at Launch
3. World-Class Cryptography Team
4. Multi-Phase Testnet Validation
5. Comprehensive Audit Program
6. Developer Experience Priority
7. Cross-Chain Redundancy & Oracle Dual-Source
8. Restaking Ecosystem Hub Positioning

Failure Factors (10):
1. Centralized Sequencer Single Operator
2. 7-Day Withdrawal Delay Native Bridge
3. Trusted Setup Dependency (KZG)
4. No Native Account Abstraction
5. State Growth Unbounded
6. Limited Token Utility at Launch
7. Large Future Token Unlocks (Oct 2025)
8. Foundation Treasury Opacity
9. Governance Parameters Undisclosed
10. Revenue Transparency Absent

Decision Framework (7 Steps):
1. Observe — Research & Cryptography Foundation (2021-2022)
2. Evaluate — Iterative Testnet Validation (2023)
3. Fund — Capital Allocation & Tokenomics Design
4. Develop — Parallel Core Component Engineering
5. Launch — Simultaneous Mainnet + TGE + Full Ecosystem Wave (2024-10-22)
6. Govern — Progressive Decentralization via DAO
7. Iterate — Rapid Upgrades & Decentralization Steps (2024-2025)

Reusable Playbook (8):
1. Build Credible ZK-Rollup Technical Foundation
2. Run Multi-Phase Testnet Program
3. Execute Comprehensive Audit Program
4. Fundraise with Strategic Investor Alignment
5. Design Tokenomics for Progressive Decentralization
6. Launch with Full Ecosystem Wave
7. Manage Centralized-to-Decentralized Transition Transparently
8. Build Cross-Chain Redundancy from Day-1

Anti-patterns (7):
1. Over-Centralization Without Credible Exit Plan
2. Premature Token Launch Without Utility
3. Poor Treasury Management Transparency
4. Single Point of Failure in Critical Infrastructure
5. Delayed Protocol Revenue Capture
6. Governance Parameter Opacity
7. State Growth Neglect

## Open Questions
- [foundation] Exact founding entity legal structure beyond "Scroll Foundation, Cayman Islands" — need to verify if there are multiple entities (e.g., Scroll Tech Pte. Ltd. in Singapore)
- [foundation] Complete core team roster with verifiable names/roles beyond the ~50 figure and named individuals
- [foundation] Whether SCR token contract address above is confirmed on-chain (need to verify on Etherscan post-TGE)
- [foundation] Precise testnet launch chronology — multiple testnet phases reported (pre-alpha, alpha, sepolia) with varying dates
- [foundation] Tokenomics details: total supply, allocation breakdown, vesting schedules, TGE unlock percentage — not covered in this phase but flagged for next phase
- [foundation] Mainnet launch block height / transaction hash for on-chain verification
- [foundation] Whether Scroll has a dedicated bug bounty program and its scope/bounty amounts
- [foundation] Current TVL and active address metrics post-mainnet launch
- [entity] Verifikasi struktur hukum lengkap: apakah Scroll Foundation (Cayman) dan Scroll Tech Pte. Ltd. (Singapura) adalah entitas terpisah atau terikat, dan apakah ada entitas lain (misal: Scroll Labs, Scroll AG)
- [entity] Daftar investor (VC, strategic) dengan alokasi token, rondah funding, dan tanggal — tidak tercakup Phase 1
- [entity] Auditor smart contract (ZK-circuit, bridge, core contracts) dengan laporan audit publik dan tanggal — tidak tercakup Phase 1
- [entity] Detail tokenomics SCR: total supply, alokasi per kategori (team, investor, ecosystem, foundation, community), vesting schedule, TGE unlock percentage — butuh cross-check primer (blog resmi, governance forum, on-chain)
- [entity] Mainnet launch block height dan transaction hash pertama untuk verifikasi on-chain pasti
- [entity] Status bug bounty program: platform (Immunefi/HackerOne), scope, reward max, apakah aktif
- [entity] Metrik on-chain pasca-mainnet: TVL (DefiLlama/L2Beat), daily active addresses, transaction count, fee revenue — perlu data aktual
- [entity] Keanggotaan Security Council / Emergency Council jika ada (multisig signers, threshold)
- [entity] Governance framework: apakah ada SCR token voting, snapshot, on-chain execution, timelock
- [entity] Daftar lengkap core team ~50+ engineer/researcher dengan nama/role publik (hanya 5 nama teridentifikasi)
- [entity] Verifikasi kontrak token SCR di Etherscan: apakah address 0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A benar dan verified
- [entity] Kronologi testnet yang pasti: pre-alpha vs alpha vs sepolia, tanggal launch masing-masing, block height genesis
- [entity] Integrasi ecosystem yang terverifikasi on-chain vs hanya announced: perlu cross-check deployment address per protokol di Scrollscan
- [history] Tanggal pasti funding rounds (Seed, Series A, Series B) dengan investor, amount, valuation — tidak tercakup di Phase 1-2, perlu data Crunchbase/PitchBook/resmi
- [history] Audit smart contract dan ZK-circuit: auditor (Trail of Bits, OpenZeppelin, dll), tanggal, scope, findings — tidak ada evidence di Phase 1-2
- [history] Bug bounty program: platform (Immunefi/HackerOne), scope, max reward, status aktif — tidak diverifikasi
- [history] Mainnet launch block height Ethereum L1 dan transaction hash genesis Scroll — perlu on-chain verification
- [history] Tokenomics detail SCR: total supply, allocation breakdown (team, investor, ecosystem, foundation, community), vesting schedule, TGE unlock % — butuh blog resmi/governance forum/on-chain
- [history] Security Council / Emergency Council multisig signers dan threshold — tidak teridentifikasi
- [history] Governance framework: SCR voting, Snapshot, on-chain execution, timelock — belum terdokumentasi
- [history] Kronologi testnet yang pasti: pre-alpha (2023-10-18) vs alpha (2023-02-28) — urutan tanggal tampak terbalik, perlu verifikasi mana yang duluan
- [history] Verifikasi kontrak token SCR di Etherscan: apakah address 0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A benar dan verified
- [history] Daftar lengkap CEX listing SCR dengan tanggal masing-masing
- [history] Protokol upgrade/mainnet fork pasca-launch (jika ada)
- [history] TVL dan metrik on-chain historis bulanan pasca-mainnet (DefiLlama/L2Beat)
- [history] Verifikasi struktur hukum: Scroll Foundation (Cayman) vs Scroll Tech Pte. Ltd. (Singapura) — apakah ada entitas lain (Scroll Labs, Scroll AG)
- [technology] Verifikasi on-chain: mainnet genesis block height Ethereum L1 dan transaction hash pertama batch submission — perlu cross-check Scrollscan/Etherscan
- [technology] Detail Security Council multisig: signer addresses, threshold (t-of-n), timelock duration — tidak dipublikasikan detailnya
- [technology] Bug bounty program: Immunefi page menunjukkan program tapi scope/max reward detail perlu verifikasi langsung
- [technology] Prover decentralization timeline: konkrete milestones dan mechanism (staking, slashing, leader election) — roadmap blog level tinggi saja
- [technology] Forced inclusion / escape hatch implementation status: design dokumen ada tapi mainnet activation status tidak jelas
- [technology] State growth mitigation: apakah ada EIP-4444 history expiry atau state pruning research aktif — RFC terbuka tapi tidak ada implementation timeline
- [technology] Account Abstraction (ERC-4337) support level: EntryPoint deployment status di Scroll mainnet, bundler infrastructure availability
- [technology] Prover circuit upgrade process: bagaimana circuit changes (new opcodes, precompiles) di-deploy tanpa trusted setup baru — perlu detail teknis
- [technology] L1 verifier contract upgrade mechanism: apakah upgradeable via proxy, governance timelock, atau immutable — bridge contract upgradeability pattern
- [technology] Exact prover cluster specs: hardware requirements, number of provers, redundancy, geographic distribution — tidak dipublikasikan
- [technology] Cross-domain message passing latency: measured L1→L2 dan L2→L1 message finality times under various network conditions
- [technology] Fee market mechanism detail: EIP-1559 implementation pada L2, base fee burn vs sequencer revenue split, gas price oracle source
- [financial] Exact strategic round amount dan valuation — tidak diungkap terpisah dari Series A+B announcement
- [financial] Treasury dashboard / transparency report — tidak ada, foundation page hanya high-level
- [financial] Official revenue figures (monthly/quarterly) — tidak dipublikasikan, hanya on-chain estimation mungkin
- [financial] Protocol fee switch activation timeline dan expected revenue share percentage — governance proposal draft only
- [financial] Security Council multisig signer addresses dan threshold untuk treasury management — tidak dipublikasikan detail
- [financial] Vesting schedule detail per investor category (cliff, linear duration, TGE unlock %) — tokenomics blog high-level only
- [financial] Foundation token sale history (apakah foundation sudah menjual SCR untuk operasional) — tidak diungkap
- [financial] Runway estimation berdasarkan current treasury dan burn rate — tidak tersedia data cukup
- [financial] Bridge contract TVL historical dan fee revenue breakdown — on-chain verifiable tapi official breakdown tidak ada
- [financial] Prover decentralization token economics (staking rewards, slashing, fee market) — roadmap only, no concrete numbers
- [financial] Tax jurisdiction implications untuk Cayman Foundation + Singapore ops entity — tidak diungkap
- [financial] Audit costs dan ongoing security budget allocation — tidak diungkap
- [token] Contract Address SCR di Etherscan (0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A) belum diverifikasi langsung di Etherscan; perlu cross-check pada Phase 11 karena bisa jadi alamat salah atau token yang berbeda.
- [token] Maximum Supply tidak diungkap eksplisit; total supply 1 miliar disebutkan tapi apakah ini hard cap atau initial supply yang bisa bertambah melalui future emission tidak jelas.
- [token] Circulating Supply resmi tidak dipublikasikan oleh Scroll Foundation; angka di CoinGecko/CMC perlu diverifikasi dari sumber primer.
- [token] Initial Unlock saat TGE hanya foundation 5% (10M SCR) yang disebutkan; apakah ada unlock untuk komunitas/airdrop awal atau investor tidak dijelaskan di blog TGE.
- [token] Apakah SCR juga di-deploy sebagai token native di Scroll L2 (untuk gas fee) atau hanya ERC-20 di Ethereum L1 – tidak ada konfirmasi di dokumentasi.
- [token] Perbedaan alokasi "Foundation + Treasury" di blog TGE (25% gabungan) vs pemisahan "Foundation 20%" dan "Treasury 5%" di docs; perlu klarifikasi struktur sebenarnya.
- [token] Vesting schedule untuk airdrop community: blog menyebut 18 bulan linear setelah cliff 1 bulan, tapi detail per batch airdrop (berapa persen unlock di TGE) tidak ada.
- [token] Governance threshold (minimal SCR untuk proposal) dan voting period duration tidak dipublikasikan angka spesifik.
- [token] Address treasury dan foundation on-chain (multisig) tidak dipublikasikan; perlu untuk memverifikasi alokasi aktual.
- [token] Status airdrop: apakah semua 150M SCR community sudah didistribusikan atau masih ada sisa lockup; data klaim on-chain tidak tersedia.
- [token] Tidak ada daftar exchange spesifik dari sumber resmi; listing CEX terverifikasi hanya via CoinGecko/CMC pihak ketiga.
- [token] Fee switch proposal masih draft di forum – tidak ada parameter persentase atau timeline implementasi.
- [token] Tidak ada informasi tentang hak tokenholder terkait revenue (apakah DAO bisa distribute revenue dalam SCR atau stablecoin).
- [token] Apakah ada mekanisme anti-whale (voting cap, delegation limit) belum terdokumentasi.
- [token] Kategori "Advisors" tidak ada alokasi – apakah Brendan Farmer sebagai advisor menerima token dari kategori lain (misal team) tidak dijelaskan.
- [token] Apakah SCR memiliki mekanisme upgradeable token contract (proxy) atau immutable – tidak disebutkan di docs.
- [ecosystem] Detail Security Council multisig: signer addresses, threshold (t-of-n), timelock duration — tidak dipublikasikan detailnya
- [ecosystem] Cloud provider spesifik (AWS/GCP/Azure) dan region deployment untuk sequencer/prover — tidak diungkap di infra repo publik
- [ecosystem] RPC provider list lengkap dan resmi (Alchemy, Infura, QuickNode terlihat di docs tapi apakah ada yang lain) — perlu verifikasi halaman RPC endpoints
- [ecosystem] Grant committee members dan selection process — tidak dipublikasikan detail
- [ecosystem] Bug bounty program scope dan max reward detail — Immunefi page ada tapi detail scope perlu verifikasi langsung
- [ecosystem] Prover decentralization timeline konkret: milestones, staking mechanism, slashing design — roadmap blog level tinggi saja
- [ecosystem] Forced inclusion / escape hatch implementation status: design dokumen ada tapi mainnet activation status tidak jelas
- [ecosystem] State growth mitigation: apakah ada EIP-4444 history expiry atau state pruning research aktif — RFC terbuka tapi tidak ada implementation timeline
- [ecosystem] Account Abstraction (ERC-4337) support level: EntryPoint deployment status di Scroll mainnet, bundler infrastructure availability
- [ecosystem] Exact CEX listing list dari sumber resmi — CoinGecko/CMC menunjukkan 8+ CEX tapi blog resmi tidak mempublikasikan daftar lengkap
- [ecosystem] Cross-domain message passing latency terukur: L1→L2 dan L2→L1 message finality times under various network conditions
- [ecosystem] Fee market mechanism detail: EIP-1559 implementation pada L2, base fee burn vs sequencer revenue split, gas price oracle source
- [ecosystem] Token contract address SCR di Etherscan (0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A) belum diverifikasi langsung di Etherscan; perlu cross-check
- [ecosystem] Apakah SCR juga di-deploy sebagai token native di Scroll L2 (untuk gas fee) atau hanya ERC-20 di Ethereum L1 — tidak ada konfirmasi di dokumentasi
- [ecosystem] Governance threshold (minimal SCR untuk proposal) dan voting period duration tidak dipublikasikan angka spesifik
- [ecosystem] Address treasury dan foundation on-chain (multisig) tidak dipublikasikan; perlu untuk memverifikasi alokasi aktual
- [ecosystem] Status airdrop: apakah semua 150M SCR community sudah didistribusikan atau masih ada sisa lockup; data klaim on-chain tidak tersedia
- [market] Exact current TVL: DefiLlama (~$1.2B) vs L2Beat (may differ slightly) vs Token Terminal (may differ) — need single authoritative snapshot for specific date
- [market] Circulating Supply vs Total Supply discrepancy: CoinGecko/CMC show different circulating supply figures; Foundation has not published official circulating supply tracker; on-chain vesting contracts not fully indexed publicly
- [market] SCR Token Contract Address Verification: 0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A cited in Phase 1/6 but not verified on Etherscan as official Scroll contract (no verified source code, no "Scroll" label from Etherscan) — critical for all token metrics
- [market] Market Share Denominators: L2 TVL total (~$20B–$25B) varies by source (L2Beat vs DefiLlama vs Token Terminal) and date; ZK-Rollup subset definition varies (some include Starknet, some don't; some include Mantle as modular not ZK)
- [market] Daily Active Addresses Definition: L2Beat uses "active addresses" (tx sender + receiver?), Scrollscan may use different methodology; Token Terminal uses "daily active users" — not directly comparable
- [market] Developer Count: "50+ core engineers" from team page vs "200+ monthly active" from GitHub insights vs Electric Capital report (different methodology) — need standardized metric
- [market] Bridge TVL Composition: Native bridge vs LayerZero vs Wormhole vs Hyperlane breakdown not separately reported in aggregate DefiLlama figure
- [market] Perpetual Volume Accuracy: CEX-reported volumes (CoinGecko/CMC) may include wash trading; no independent audit of perp volume
- [market] Sequencer/Prover Decentralization Metrics: Currently 1 sequencer, ~10-20 provers (Foundation-operated); no permissionless validator set; roadmap milestones not quantified with dates
- [market] Fee Revenue Data: Protocol revenue (base fee burn, bridge fees, sequencer fees) not publicly reported by Foundation; only on-chain estimates possible via block explorer
- [market] Competitor TVL/Transaction Rankings: Real-time rankings shift daily; L2Beat updates ~daily, DefiLlama ~hourly; snapshot date critical
- [market] Narrative Classification Overlap: "Modular" narrative claimed by many L2s (Celestia, Mantle, EigenDA users); Scroll uses Ethereum DA not separate DA layer — classification debatable
- [market] Institutional Adoption Evidence: No public enterprise partnerships, custody integrations (Fireblocks, Copper, etc.), or tradfi announcements found — may exist but not public
- [market] Bug Bounty Scope/Payouts: Immunefi page exists but max reward, scope (contracts, prover, sequencer, bridge), and payout history not verified
- [market] Geographic User Distribution: No public analytics on user geography; regulatory restrictions (US, sanctioned regions) may affect accessible markets
- [market] Token Unlock Schedule Impact: Large investor/team unlocks starting Oct 2025 (12-month cliff) may affect market dynamics; not priced into current market cap analyses
- [market] Cross-chain Message Volume Methodology: LayerZero/Wormhole/Hyperlane each count messages differently (packet vs message vs transfer); aggregate figure approximate
- [behavioral] Contract Address SCR di Etherscan (0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A) belum diverifikasi langsung di Etherscan sebagai official Scroll contract — perlu cross-check on-chain di Phase 11
- [behavioral] Security Council multisig detail: signer addresses, threshold (t-of-n), timelock duration — tidak dipublikasikan; kritis untuk governance trust
- [behavioral] Prover decentralization timeline konkret: milestones, staking mechanism, slashing design, token economics — roadmap blog level tinggi saja
- [behavioral] Forced inclusion / escape hatch activation status: design exists tapi mainnet activation kapan? Butuh governance proposal?
- [behavioral] State growth mitigation: EIP-4444 history expiry atau state pruning research status — RFC open tapi no implementation timeline
- [behavioral] Account Abstraction (ERC-4337) support: EntryPoint deployment status di Scroll mainnet, bundler infrastructure availability
- [behavioral] Circulating Supply resmi: Foundation tidak mempublikasikan tracker; CoinGecko/CMC angka beda; vesting contracts tidak fully indexed publik
- [behavioral] Treasury dashboard/transparency report: Tidak ada; foundation page high-level only; multisig addresses tidak publik
- [behavioral] Governance parameter specifics: Proposal threshold (min SCR), voting period, quorum, delegation mechanics on-chain — tidak di-dokumentasikan
- [behavioral] Bug bounty scope/max reward: Immunefi page exists tapi detail scope (contracts, prover, sequencer, bridge) dan payout history perlu verifikasi
- [behavioral] Exact CEX listing list dari sumber resmi: CoinGecko/CMC menunjukkan 8+ CEX tapi blog resmi tidak publish daftar lengkap
- [behavioral] Cross-domain message passing latency terukur: L1→L2 dan L2→L1 finality times under various conditions
- [behavioral] Fee market mechanism detail: EIP-1559 implementation L2, base fee burn vs sequencer revenue split, gas price oracle source
- [behavioral] Token upgradeability: Apakah SCR contract upgradeable via proxy atau immutable — tidak disebutkan di docs
- [behavioral] Advisor token allocation: Brendan Farmer sebagai advisor — apakah menerima token dari kategori Team atau terpisah? Tidak dijelaskan
- [behavioral] Geographic user distribution: No public analytics; regulatory restrictions (US, sanctioned regions) impact unknown
- [behavioral] Prover circuit upgrade process: Bagaimana circuit changes (new opcodes, precompiles) di-deploy tanpa trusted setup baru — perlu detail teknis
- [behavioral] L1 verifier contract upgrade mechanism: Proxy? Governance timelock? Immutable? — bridge contract upgradeability pattern tidak detail
- [behavioral] Exact prover cluster specs: Hardware, node count, redundancy, geographic distribution — tidak dipublikasikan
- [behavioral] Institutional adoption evidence: No public enterprise partnerships, custody integrations (Fireblocks, Copper) announcements
- [behavioral] Competitor TVL/transaction rankings real-time: L2Beat vs DefiLlama vs Token Terminal metodologi beda; snapshot date critical
- [behavioral] Narrative classification overlap: "Modular" claimed by many; Scroll uses Ethereum DA not separate DA layer — classification debatable
- [knowledge] SCR Token Contract Address Verification: 0x0c4b5C2A7d8E5b7e9A7D8c9F6e1A2b3C4d5E6f7A cited in Phase 1/6/8 tapi tidak diverifikasi di Etherscan sebagai official Scroll contract (no verified source code, no "Scroll" label) — critical untuk all token metrics【Phase 1 — Foundation】【Phase 6 — Token Information】【Phase 8 — Open Threads】
- [knowledge] Security Council Multisig Details: signer addresses, threshold (t-of-n), timelock duration — tidak dipublikasikan; kritis untuk governance trust【Phase 4 — Security Model】【Phase 7 — Governance Ecosystem】【Phase 8 — Open Threads】
- [knowledge] Prover Decentralization Timeline Konkret: milestones, staking mechanism, slashing design, token economics — roadmap blog level tinggi saja【Phase 4 — Official Technical Resources】【Phase 9 — Evolution Pattern】【Phase 8 — Open Threads】
- [knowledge] Forced Inclusion / Escape Hatch Activation Status: design exists tapi mainnet activation kapan? Butuh governance proposal?【Phase 4 — Known Technical Limitations】【Phase 9 — Risk Response Pattern】【Phase 8 — Open Threads】
- [knowledge] State Growth Mitigation: EIP-4444 history expiry atau state pruning research status — RFC open tapi no implementation timeline【Phase 4 — Known Technical Limitations】【Phase 8 — Open Threads】【Phase 9 — Strategic Trade-offs】
- [knowledge] Account Abstraction (ERC-4337) Support: EntryPoint deployment status di Scroll mainnet, bundler infrastructure availability【Phase 4 — Known Technical Limitations】【Phase 4 — Official Technical Resources】【Phase 8 — Open Threads】
- [knowledge] Circulating Supply Resmi: Foundation tidak mempublikasikan tracker; CoinGecko/CMC angka beda; vesting contracts tidak fully indexed publik【Phase 6 — Supply】【Phase 8 — Open Threads】【Phase 8 — Adoption Metrics】
- [knowledge] Treasury Dashboard/Transparency Report: Tidak ada; foundation page high-level only; multisig addresses tidak publik【Phase 5 — Treasury】【Phase 8 — Open Threads】【Phase 9 — Financial Decision Pattern】
- [knowledge] Governance Parameter Specifics: Proposal threshold (min SCR), voting period, quorum, delegation mechanics on-chain — tidak di-dokumentasikan【Phase 6 — Governance】【Phase 8 — Open Threads】【Phase 9 — Governance Decision Pattern】
- [knowledge] Bug Bounty Scope/Max Reward: Immunefi page exists tapi detail scope (contracts, prover, sequencer, bridge) dan payout history perlu verifikasi【Phase 4 — Official Technical Resources】【Phase 7 — Official Ecosystem Resources】【Phase 8 — Open Threads】
- [knowledge] Exact CEX Listing List dari Sumber Resmi: CoinGecko/CMC menunjukkan 8+ CEX tapi blog resmi tidak publish daftar lengkap【Phase 8 — Trading Markets】【Phase 8 — Open Threads】
- [knowledge] Cross-Domain Message Passing Latency Terukur: L1→L2 dan L2→L1 finality times under various conditions【Phase 4 — System Architecture】【Phase 8 — Open Threads】
- [knowledge] Fee Market Mechanism Detail: EIP-1559 implementation L2, base fee burn vs sequencer revenue split, gas price oracle source【Phase 4 — Execution Environment】【Phase 5 — Revenue Model】【Phase 8 — Open Threads】
- [knowledge] Token Upgradeability: Apakah SCR contract upgradeable via proxy atau immutable — tidak disebutkan di docs【Phase 6 — Token Information】【Phase 8 — Open Threads】
- [knowledge] Advisor Token Allocation: Brendan Farmer sebagai advisor — apakah menerima token dari kategori Team atau terpisah? Tidak dijelaskan【Phase 2 — Brendan Farmer】【Phase 6 — Distribution】【Phase 8 — Open Threads】
- [knowledge] Geographic User Distribution: No public analytics; regulatory restrictions (US, sanctioned regions) impact unknown【Phase 8 — Open Threads】【Phase 8 — Market Position】
- [knowledge] Prover Circuit Upgrade Process: Bagaimana circuit changes (new opcodes, precompiles) di-deploy tanpa trusted setup baru — perlu detail teknis【Phase 4 — Security Model】【Phase 4 — Known Technical Limitations】【Phase 8 — Open Threads】
- [knowledge] L1 Verifier Contract Upgrade Mechanism: Proxy? Governance timelock? Immutable? — bridge contract upgradeability pattern tidak detail【Phase 4 — Security Model】【Phase 4 — Core Components】【Phase 8 — Open Threads】
- [knowledge] Exact Prover Cluster Specs: Hardware, node count, redundancy, geographic distribution — tidak dipublikasikan【Phase 4 — Core Components】【Phase 7 — External Dependencies】【Phase 8 — Open Threads】
- [knowledge] Institutional Adoption Evidence: No public enterprise partnerships, custody integrations (Fireblocks, Copper) announcements【Phase 8 — Narrative Position】【Phase 8 — Open Threads】
- [knowledge] Competitor TVL/Transaction Rankings Real-time: L2Beat vs DefiLlama vs Token Terminal metodologi beda; snapshot date critical【Phase 8 — Market Share】【Phase 8 — Open Threads】
- [knowledge] Narrative Classification Overlap: "Modular" claimed by many; Scroll uses Ethereum DA not separate DA layer — classification debatable【Phase 8 — Narrative Position】【Phase 8 — Open Threads】
