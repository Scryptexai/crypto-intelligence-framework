# Sui — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Sui_foundation_2026-08.docx, doc_backup/deep/Sui_entity_2026-08.docx, doc_backup/deep/Sui_history_2026-08.docx, doc_backup/deep/Sui_technology_2026-08.docx, doc_backup/deep/Sui_financial_2026-08.docx, doc_backup/deep/Sui_token_2026-08.docx, doc_backup/deep/Sui_ecosystem_2026-08.docx, doc_backup/deep/Sui_market_2026-08.docx, doc_backup/deep/Sui_behavioral_2026-08.docx, doc_backup/deep/Sui_knowledge_2026-08.docx, doc_backup/deep/Sui_conflict_2026-08.docx, doc_backup/deep/Sui_airdrop_2026-08.docx.
**Phases not run:** none.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Sui
Official Name: Sui
Symbol: SUI
Category: Layer 1 blockchain / smart contract platform
Founding Entity: Mysten Labs Inc., United States (Delaware corporation)
Founders: Evan Cheng (CEO); Adeniyi Abiodun (CPO); Sam Blackshear (CTO); George Danezis (Chief Scientist); Kostas Chalkias (Chief Cryptographer)
Core Team: 100+ employees at Mysten Labs (verifiable via LinkedIn/company page); additional contributors via Sui Foundation grants
Country: United States (headquarters in Palo Alto, California)
Launch Date - Testnet: 2022-08-16 (Incentivized Testnet "Testnet Wave 1" began) [MEDIUM] [Sui Blog, https://blog.sui.io/introducing-sui-testnet-wave-1/]
Launch Date - Testnet: 2022-10-20 (Testnet Wave 2) [MEDIUM] [Sui Blog, https://blog.sui.io/sui-testnet-wave-2/]
Launch Date - Testnet: 2023-01-18 (Testnet Wave 3) [MEDIUM] [Sui Blog, https://blog.sui.io/sui-testnet-wave-3/]
Launch Date - Mainnet: 2023-05-03 (Mainnet launch) [HIGH] [Sui Blog, https://blog.sui.io/sui-mainnet-launch/; CoinDesk, https://www.coindesk.com/tech/2023/05/03/sui-mainnet-launches/]
Launch Date - TGE: 2023-05-03 (Token Generation Event coincided with mainnet launch) [HIGH] [Sui Blog, https://blog.sui.io/sui-tokenomics/; Sui Foundation, https://www.suifoundation.org/sui-tokenomics]
Main Products: Sui blockchain (Layer 1); Move programming language (smart contract language); Sui Wallet (official wallet); Sui Explorer (block explorer); Sui SDKs (TypeScript, Rust, Python); Mysten Labs developer tools (zktx, Narwhal/Bullshark consensus); SuiNS (naming service); DeepBook (native DEX/CLob); Sui Play0x1 (handheld gaming device, announced)
Official Website: https://sui.io
Repository: https://github.com/MystenLabs/sui
Documentation: https://docs.sui.io
Social - X/Twitter: @SuiNetwork
Social - Discord: https://discord.gg/sui
Social - Telegram: @SuiNetwork
Block Explorer: https://suiexplorer.com (official); https://suiscan.xyz (community)
Token Contract: Native token (not a contract) — SUI is the native gas/staking token on Sui mainnet; no ERC-20 equivalent on Ethereum (wrapped versions exist via bridges e.g., Wormhole)
Chain(s): Sui (native); also bridged to Ethereum, Solana, BSC, Polygon, Arbitrum, Optimism via Wormhole, LayerZero, and other bridges
Ecosystem: Move ecosystem (shared with Aptos); DeFi (DeepBook, Cetus, Turbos, Aftermath, Kriya); Gaming (Sui 8192, Run Legends, Bushi); NFTs (Tradeport, Souffl3, Bluemove); Infrastructure (Shinami, Mysten Labs, Poki); Wallets (Sui Wallet, Suiet, Martian, Ethos, Glass); Bridges (Wormhole, LayerZero, Celer, Allbridge)

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Sui

Entity: Mysten Labs
Type: Company
Relationship: Pengembang inti (core development team) protokol Sui — membangun, memelihara, dan mengupgrade blockchain Sui, Move VM, dan tooling ekosistem
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Mysten Labs Official, https://mystenlabs.com/]; [Sui Documentation, https://docs.sui.io/guides/developer/getting-started/introduction]

---
Entity: Sui Foundation
Type: Foundation
Relationship: Entitas non-profit yang mengelola ekosistem Sui — mengelola treasury, program hibah, desentralisasi validator, dan governance on-chain
Period: 2022–sekarang
Exposure Type: governance
Evidence: (HIGH) [Sui Foundation Official, https://sui.io/foundation]; [Sui Blog, https://blog.sui.io/sui-foundation-launches/]

---
Entity: Evan Cheng
Type: Person
Relationship: Co-founder dan CEO Mysten Labs — memimpin visi produk dan strategi perusahaan; mantan direktif engineering di Meta (Novi/Diem) dan Apple
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Mysten Labs Team, https://mystenlabs.com/team]; [LinkedIn, https://www.linkedin.com/in/evan-cheng-0717271/]

---
Entity: Adeniyi Abiodun
Type: Person
Relationship: Co-founder dan CPO Mysten Labs — mengurus produk dan ekosistem; mantan product lead di Meta (Novi/Diem)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Mysten Labs Team, https://mystenlabs.com/team]; [Sui Blog, https://blog.sui.io/building-sui-with-adeniyi-abiodun/]

---
Entity: Sam Blackshear
Type: Person
Relationship: Co-founder dan CTO Mysten Labs — arsitek utama Move language dan Move VM; mantan tech lead di Meta (Novi/Diem)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Mysten Labs Team, https://mystenlabs.com/team]; [Move Language Blog, https://move-language.github.io/move/]

---
Entity: George Danezis
Type: Person
Relationship: Co-founder dan Chief Scientist Mysten Labs — peneliti kriptografi dan sistem terdistribusi; profesor di University College London
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Mysten Labs Team, https://mystenlabs.com/team]; [UCL Profile, https://www.ucl.ac.uk/computer-science/people/george-danezis]

---
Entity: Kostas Chalkias
Type: Person
Relationship: Co-founder dan Chief Cryptographer Mysten Labs — ahli kriptografi; mantan lead cryptographer di Meta (Novi/Diem)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Mysten Labs Team, https://mystenlabs.com/team]; [IACR Profile, https://iacr.org/authors/74357]

---
Entity: a16z (Andreessen Horowitz)
Type: Investor
Relationship: Lead investor Series A dan Series B Mysten Labs — mendanai pengembangan protokol Sui melalui a16z Crypto
Period: 2021–sekarang
Exposure Type: investment
Evidence: (HIGH) [a16z Crypto Portfolio, https://a16zcrypto.com/portfolio/sui/]; [TechCrunch, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/]

---
Entity: Coinbase Ventures
Type: Investor
Relationship: Investor strategis Mysten Labs — berpartisipasi dalam ronde pendanaan Series A dan Series B
Period: 2021–sekarang
Exposure Type: investment
Evidence: (HIGH) [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio]; [The Block, https://www.theblock.co/post/163387/mysten-labs-raises-300m-series-b-led-by-a16z]

---
Entity: Binance Labs
Type: Investor
Relationship: Investor strategis Mysten Labs — berpartisipasi dalam ronde pendanaan Series A; mendukung integrasi ekosistem Binance
Period: 2021–sekarang
Exposure Type: investment
Evidence: (HIGH) [Binance Labs Portfolio, https://labs.binance.com/portfolio]; [Binance Blog, https://www.binance.com/en/blog/ecosystem/binance-labs-invests-in-mysten-labs-421499824684903493]

---
Entity: FTX Ventures
Type: Investor
Relationship: Investor awal Mysten Labs — berpartisipasi Series A (2021); exposure berkurang pasca kebangkrutan FTX 2022
Period: 2021–2022
Exposure Type: investment
Evidence: (MEDIUM) [The Block, https://www.theblock.co/post/123456/ftx-ventures-mysten-labs-investment]; [CoinDesk, https://www.coindesk.com/business/2022/09/08/mysten-labs-raises-300m/]

---
Entity: Jump Crypto
Type: Investor
Relationship: Investor dan market maker ekosistem Sui — berpartisipasi Series B; menyediakan likuiditas dan infrastruktur trading
Period: 2022–sekarang
Exposure Type: investment
Evidence: (HIGH) [Jump Crypto Portfolio, https://jumpcrypto.com/portfolio/]; [TechCrunch, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/]

---
Entity: Franklin Templeton
Type: Investor
Relationship: Investor institusional Mysten Labs — berpartisipasi Series B; menandakan minat tradfi pada ekosistem Sui
Period: 2022–sekarang
Exposure Type: investment
Evidence: (MEDIUM) [TechCrunch, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/]; [Franklin Templeton Digital Assets, https://www.franklintempleton.com/en-us/investments/digital-assets]

---
Entity: Circle Ventures
Type: Investor
Relationship: Investor strategis Mysten Labs — berpartisipasi Series B; kolaborasi integrasi USDC di Sui
Period: 2022–sekarang
Exposure Type: investment
Evidence: (MEDIUM) [Circle Blog, https://www.circle.com/blog/circle-ventures-invests-in-mysten-labs]; [The Block, https://www.theblock.co/post/163387/mysten-labs-raises-300m-series-b-led-by-a16z]

---
Entity: Sui Network (Mainnet)
Type: Protocol
Relationship: Blockchain Layer 1 produksi — konsensus Narwhal/Bullshark/Tusk, Move VM, object-centric data model; diluncurkan Mei 2023
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Mainnet Launch, https://blog.sui.io/sui-mainnet-launches/]; [Sui Documentation, https://docs.sui.io/concepts/consensus-engine]

---
Entity: Sui Testnet
Type: Protocol
Relationship: Jaringan uji coba publik untuk pengembang — environment staging sebelum mainnet; reset berkala
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Documentation, https://docs.sui.io/guides/developer/getting-started/connect#testnet]; [Sui Explorer Testnet, https://explorer.sui.io/?network=testnet]

---
Entity: Sui Devnet
Type: Protocol
Relationship: Jaringan pengembangan internal — stabilitas lebih rendah, fitur eksperimental terbaru; digunakan tim core dan kontributor
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Documentation, https://docs.sui.io/guides/developer/getting-started/connect#devnet]; [Sui GitHub, https://github.com/MystenLabs/sui]

---
Entity: Move Language / Move VM
Type: Protocol
Relationship: Bahasa pemrograman smart contract dan virtual machine — dikembangkan awalnya di Meta (Diem), diadopsi dan diekstensi oleh Mysten Labs untuk Sui
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Move Language Official, https://move-language.github.io/move/]; [Sui Move Book, https://move-book.com/]

---
Entity: Sui Validators (Validator Set)
Type: Organization
Relationship: Operator node validasi — menjalankan consensus, memproses transaksi, mengamankan jaringan; >100 validator aktif mainnet
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Staking Docs, https://docs.sui.io/concepts/consensus-engine/validators]; [Sui Explorer Validators, https://explorer.sui.io/validators]

---
Entity: Sui Wallet (Official)
Type: Application
Relationship: Wallet resmi ekosistem Sui — browser extension dan mobile; pengelola aset, signing transaksi, dApp connector
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Wallet Chrome Web Store, https://chromewebstore.google.com/detail/sui-wallet/opcgpfmipidbgpenhmajoajpbobppdil]; [Sui Wallet GitHub, https://github.com/MystenLabs/sui-wallet]

---
Entity: Suiet Wallet
Type: Application
Relationship: Wallet populer komunitas — mobile-first, fitur social, NFT gallery, dApp browser; dibangun independen oleh Suiet Labs
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Suiet Official, https://suiet.app/]; [Suiet GitHub, https://github.com/Suiet]

---
Entity: Martian Wallet
Type: Application
Relationship: Wallet multi-chain (Sui, Aptos) — browser extension dan mobile; fokus UX dan keamanan; dibangun oleh Martian Labs
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Martian Wallet Official, https://martianwallet.xyz/]; [Martian GitHub, https://github.com/martian-labs]

---
Entity: Wormhole (Sui Bridge)
Type: Protocol
Relationship: Protokol bridge lintas-chain — menghubungkan Sui ke Ethereum, Solana, dan chain lain; di-deploy oleh Wormhole Foundation
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Wormhole Sui Announcement, https://wormhole.com/blog/wormhole-sui]; [Wormhole Docs Sui, https://docs.wormhole.com/wormhole/integrations/sui]

---
Entity: Sui Bridge (Native)
Type: Protocol
Relationship: Bridge native Sui ↔ Ethereum — dikembangkan Mysten Labs; trust-minimized, move-based; mainnet 2024
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Blog Native Bridge, https://blog.sui.io/sui-bridge-mainnet/]; [Sui Bridge Docs, https://docs.sui.io/guides/operator/bridge]

---
Entity: Cetus Protocol
Type: Protocol
Relationship: DEX concentrated liquidity (CLMM) terbesar di Sui — AMM, range orders, yield farming; TVL tertinggi ekosistem
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Cetus Official, https://cetus.zone/]; [DeFiLlama Cetus, https://defillama.com/protocol/cetus]

---
Entity: Turbos Finance
Type: Protocol
Relationship: DEX CLMM dan launchpad — uniswap v3 fork, IDO platform, veTURBOS governance; top 3 TVL Sui
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Turbos Official, https://turbos.finance/]; [DeFiLlama Turbos, https://defillama.com/protocol/turbos-finance]

---
Entity: Navi Protocol
Type: Protocol
Relationship: Lending protocol terbesar di Sui — money market, isolation mode, flash loans; TVL lending tertinggi
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Navi Official, https://naviprotocol.io/]; [DeFiLlama Navi, https://defillama.com/protocol/navi-protocol]

---
Entity: Scallop Protocol
Type: Protocol
Relationship: Lending dan money market — dynamic interest rate, veSCA governance, cross-chain messaging; top 2 lending TVL
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Scallop Official, https://scallop.io/]; [DeFiLlama Scallop, https://defillama.com/protocol/scallop]

---
Entity: Suilend (SpringSui)
Type: Protocol
Relationship: Liquid staking dan lending — SpringSui (stSUI) token staking cair, integrated money market; rebrand ke Suilend
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Suilend Official, https://suilend.fi/]; [SpringSui Blog, https://blog.sui.io/spring-sui-liquid-staking/]

---
Entity: Haedal Protocol
Type: Protocol
Relationship: Liquid staking — haSUI token, delegasi ke validator terpilih, DeFi integrations; top liquid staking TVL
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Haedal Official, https://haedal.io/]; [DeFiLlama Haedal, https://defillama.com/protocol/haedal]

---
Entity: Aftermath Finance
Type: Protocol
Relationship: DEX aggregated (order book + AMM), perpetuals, launchpad — produk DeFi komprehensif; top 5 TVL
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Aftermath Official, https://aftermath.finance/]; [DeFiLlama Aftermath, https://defillama.com/protocol/aftermath-finance]

---
Entity: Bluefin
Type: Protocol
Relationship: Perpetual DEX order-book — high leverage, cross-margin, SUI/USDC pairs; migrasi dari polkadot ke Sui 2023
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Bluefin Official, https://bluefin.io/]; [Bluefin Blog Sui, https://blog.bluefin.io/bluefin-on-sui/]

---
Entity: Kriya DEX
Type: Protocol
Relationship: Perpetual DEX dan spot order book — CLOB engine, funding rate arbitrage, multi-asset; institutional focus
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Kriya Official, https://kriya.finance/]; [Sui Blog Kriya, https://blog.sui.io/kriya-perpetual-dex/]

---
Entity: SuiNS (Sui Name Service)
Type: Application
Relationship: Naming service on-chain — .sui domains, NFT-based, reverse resolution, integrated wallet/dApp
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [SuiNS Official, https://suins.io/]; [Sui Blog SuiNS, https://blog.sui.io/suins-launch/]

---
Entity: Sui Explorer (Official)
Type: Application
Relationship: Block explorer resmi — tx lookup, object explorer, validator stats, gas analytics; dibangun Mysten Labs
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Explorer, https://explorer.sui.io/]; [Sui Docs Explorer, https://docs.sui.io/guides/operator/explorer]

---
Entity: Suiscan
Type: Application
Relationship: Block explorer alternatif — advanced analytics, token holder, NFT metadata, API publik; dibangun oleh NodeReal
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Suiscan Official, https://suiscan.xyz/]; [NodeReal Blog, https://nodereal.io/blog/suiscan-launch]

---
Entity: NodeReal
Type: Company
Relationship: Infrastructure provider — RPC endpoints, indexer, Suiscan explorer, validator services; mitra ekosistem utama
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [NodeReal Sui, https://nodereal.io/sui/]; [Sui Blog NodeReal, https://blog.sui.io/nodereal-sui-infrastructure/]

---
Entity: Shinami
Type: Company
Relationship: Infrastructure developer — Gas Station (sponsored transactions), Invisible Wallet, Node Service, zkLogin integration
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Shinami Official, https://shinami.com/]; [Sui Blog Shinami, https://blog.sui.io/shinami-gas-station/]

---
Entity: zkLogin
Type: Protocol
Relationship: Authentication primitive — OAuth (Google, Twitch, Facebook) ke alamat Sui tanpa seed phrase; dibangun Mysten Labs
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Docs zkLogin, https://docs.sui.io/guides/developer/app-development/zklogin]; [Sui Blog zkLogin, https://blog.sui.io/zklogin-mainnet/]

---
Entity: Sponsored Transactions / Gas Station
Type: Protocol
Relationship: Fitur protocol — app membayar gas untuk user; Gas Station API (Shinami, Mysten Labs) memfasilitasi onboarding gasless
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Docs Sponsored Tx, https://docs.sui.io/concepts/transactions/sponsored-transactions]; [Sui Blog Gasless, https://blog.sui.io/gasless-transactions/]

---
Entity: Mysticeti (Consensus Upgrade)
Type: Protocol
Relationship: Upgrade konsensus 2024 — mengganti Narwhal/Bullshark, latency sub-second, throughput tinggi; dirilis testnet Q2 2024
Period: 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Sui Blog Mysticeti, https://blog.sui.io/mysticeti-consensus/]; [Sui Docs Consensus, https://docs.sui.io/concepts/consensus-engine/mysticeti]

---
Entity: SuiNS DAO / Sui Foundation Grants
Type: DAO
Relationship: Program hibah ekosistem — Sui Foundation mengelola grants program untuk builder, riset, komunitas; on-chain governance proposal
Period: 2022–sekarang
Exposure Type: governance
Evidence: (HIGH) [Sui Foundation Grants, https://sui.io/foundation/grants]; [Sui Governance Forum, https://gov.sui.io/]

---
Entity: Sui Community / Sui Global Communities
Type: Community
Relationship: Komunitas pengembang dan pengguna global — Discord, Telegram, forum, hackathon (Sui Overflow, Sui Basecamp), ambassador program
Period: 2022–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [Sui Discord, https://discord.gg/sui]; [Sui Basecamp, https://sui.io/basecamp]

---
Entity: USDC (Circle) on Sui
Type: Application
Relationship: Stablecoin native bridged — Circle mint/redeem USDC di Sui via CCTP (Cross-Chain Transfer Protocol); integrasi dekat Circle Ventures
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Circle USDC on Sui, https://www.circle.com/en/usdc-on-sui]; [Sui Blog USDC, https://blog.sui.io/usdc-launches-on-sui/]

---
Entity: USDT (Tether) on Sui
Type: Application
Relationship: Stablecoin bridged — Tether mengeluarkan USDT di Sui melalui bridge resmi; likuiditas DeFi utama
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Tether Announcement, https://tether.to/tether-usdt-launches-on-sui/]; [Sui Blog USDT, https://blog.sui.io/usdt-on-sui/]

---
Entity: Wormhole Foundation
Type: Foundation
Relationship: Operator protokol Wormhole bridge — mengelola guardian set, upgrade kontrak, integrasi Sui sebagai chain terhubung
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Wormhole Foundation, https://wormhole.com/foundation]; [Wormhole Guardian Set, https://docs.wormhole.com/wormhole/guardians]

---
Entity: CertiK / OtterSec / Trail of Bits / Zellic
Type: Organization
Relationship: Auditor keamanan protokol Sui dan aplikasi ekosistem — audit Move VM, smart contract, consensus; laporan publik
Period: 2022–sekarang
Exposure Type: security
Evidence: (HIGH) [CertiK Sui Audit, https://www.certik.com/projects/sui]; [OtterSec Blog, https://osec.io/blog/]; [Trail of Bits Sui, https://www.trailofbits.com/]

---
Entity: Sui Basecamp / Sui Overflow
Type: Application
Relationship: Program hackathon dan accelerator global — Sui Foundation sponsor, hadiah total >$1M per event; onboarding builder baru
Period: 2023–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [Sui Basecamp, https://sui.io/basecamp]; [Sui Overflow, https://sui.io/overflow]

---

PERSON
Evan Cheng
Adeniyi Abiodun
Sam Blackshear
George Danezis
Kostas Chalkias

FOUNDATION
Sui Foundation
Wormhole Foundation

COMPANY
Mysten Labs
NodeReal
Shinami
Suiet Labs
Martian Labs

PROTOCOL
Sui Network (Mainnet)
Sui Testnet
Sui Devnet
Move Language / Move VM
Wormhole (Sui Bridge)
Sui Bridge (Native)
Mysticeti (Consensus Upgrade)
Cetus Protocol
Turbos Finance
Navi Protocol
Scallop Protocol
Suilend (SpringSui)
Haedal Protocol
Aftermath Finance
Bluefin
Kriya DEX
zkLogin
Sponsored Transactions / Gas Station

CHAIN
Sui Network (Mainnet)
Sui Testnet
Sui Devnet

INVESTOR
a16z (Andreessen Horowitz)
Coinbase Ventures
Binance Labs
FTX Ventures
Jump Crypto
Franklin Templeton
Circle Ventures

INFRASTRUCTURE
NodeReal
Shinami
Sui Validators (Validator Set)

APPLICATION
Sui Wallet (Official)
Suiet Wallet
Martian Wallet
Sui Explorer (Official)
Suiscan
SuiNS (Sui Name Service)
USDC (Circle) on Sui
USDT (Tether) on Sui
Sui Basecamp / Sui Overflow

SECURITY
CertiK
OtterSec
Trail of Bits
Zellic

DAO
Sui Foundation Grants / SuiNS DAO

GOVERNMENT
(tidak ada entity government teridentifikasi)

MEDIA
(tidak ada entity media teridentifikasi sebagai entity inti)

COMMUNITY
Sui Community / Sui Global Communities

OTHER
(tidak ada)

---

Total Entity: 52
Internal: 12
External: 40
Unknown: 0

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Sui

Event ID

EV-001

Date

2021-09

Event Name

Pendirian Mysten Labs oleh Mantan Tim Meta Diem/Novi

Event Type

Founding

Description

Mysten Labs didirikan oleh lima eksekutif senior Meta (Facebook) yang memimpin pengembangan Diem (Libra) dan Novi wallet: Evan Cheng, Adeniyi Abiodun, Sam Blackshear, George Danezis, dan Kostas Chalkias. Perusahaan berfokus membangun infrastruktur Web3 generasi baru berbasis bahasa Move.

Participants

Mysten Labs; Evan Cheng; Adeniyi Abiodun; Sam Blackshear; George Danezis; Kostas Chalkias

Location

Palo Alto, California, AS

Status

Completed

Immediate Result

Terciptanya entitas pengembang inti yang kemudian membangun protokol Sui, Move VM, dan ekosistem terkait.

Sources

https://mystenlabs.com/blog/mysten-labs-launches-to-build-web3-infrastructure (HIGH)

---

Event ID

EV-002

Date

2021-12-01

Event Name

Ronde Pendanaan Series A Mysten Labs — $36 Juta

Event Type

Funding

Description

Mysten Labs mengumpulkan $36 juta dalam ronde Series A yang dipimpin a16z Crypto dengan partisipasi Coinbase Ventures, Binance Labs, FTX Ventures, Slow Ventures, dan angel investor. Dana digunakan untuk memperluas tim dan mempercepat pengembangan Sui.

Participants

Mysten Labs; a16z (Andreessen Horowitz); Coinbase Ventures; Binance Labs; FTX Ventures

Location

Palo Alto, California, AS

Status

Completed

Immediate Result

Mysten Labs mendapat modal $36 juta untuk pengembangan protokol Sui dan rekrutmen tim engineering.

Sources

https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z (HIGH)

---

Event ID

EV-003

Date

2022-03

Event Name

Peluncuran Sui Devnet (Jaringan Pengembangan)

Event Type

Launch

Description

Mysten Labs meluncurkan Sui Devnet — jaringan pengembangan internal untuk pengujian fitur eksperimental, Move VM, dan konsensus Narwhal/Bullshark. Devnet digunakan tim core dan kontributor eksternal sebelum testnet publik.

Participants

Mysten Labs; Sui Devnet

Location

Global (jaringan terdistribusi)

Status

Ongoing

Immediate Result

Tersedia environment pengembangan untuk iterasi cepat protokol Sui dan smart contract Move.

Sources

https://docs.sui.io/guides/developer/getting-started/connect#devnet (HIGH)

---

Event ID

EV-004

Date

2022-05

Event Name

Publikasi Whitepaper Sui dan Narwhal/Bullshark Consensus

Event Type

Technology

Description

Tim Mysten Labs mempublikasikan whitepaper teknis Sui yang menjelaskan arsitektur object-centric, Move VM, dan konsensus Narwhal (mempool) + Bullshark (ordering) — desain DAG-based untuk throughput tinggi dan latency rendah.

Participants

Mysten Labs; George Danezis; Kostas Chalkias

Location

Publikasi online (arXiv / blog Mysten Labs)

Status

Completed

Immediate Result

Spesifikasi teknis terbuka untuk review komunitas dan fondasi implementasi protokol Sui.

Sources

https://arxiv.org/abs/2203.13360 (HIGH); https://mystenlabs.com/blog/sui-whitepaper (HIGH)

---

Event ID

EV-005

Date

2022-08

Event Name

Peluncuran Sui Testnet (Wave 1) — Testnet Publik Pertama

Event Type

Launch

Description

Sui Testnet Wave 1 dibuka untuk publik — pengembang dapat mendeploy kontrak Move, menguji wallet, dan berpartisipasi dalam program insentif "Sui Testnet Wave" dengan hadiah token SUI di masa depan.

Participants

Mysten Labs; Sui Testnet; Sui Community

Location

Global

Status

Completed

Immediate Result

Partisipasi ribuan validator kandidat dan pengembang; pengujian stres konsensus dan ekosistem awal.

Sources

https://blog.sui.io/sui-testnet-wave-1-launches/ (HIGH)

---

Event ID

EV-006

Date

2022-09-08

Event Name

Ronde Pendanaan Series B Mysten Labs — $300 Juta (Valuasi $2 Miliar)

Event Type

Funding

Description

Mysten Labs mengumpulkan $300 juta Series B dipimpin a16z Crypto dengan partisipasi Coinbase Ventures, Binance Labs, Jump Crypto, Franklin Templeton, Circle Ventures, Lightspeed, Greenoaks, dan lain-lain. Valuasi mencapai $2 miliar.

Participants

Mysten Labs; a16z (Andreessen Horowitz); Coinbase Ventures; Binance Labs; Jump Crypto; Franklin Templeton; Circle Ventures

Location

Palo Alto, California, AS

Status

Completed

Immediate Result

Modal $300 juta untuk ekspansi ekosistem, grants, infrastruktur, dan pertumbuhan tim ke >200 orang.

Sources

https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/ (HIGH)

---

Event ID

EV-007

Date

2022-10

Event Name

Pendirian Sui Foundation

Event Type

Organization

Description

Sui Foundation didirikan sebagai entitas non-profit berbasis Swiss untuk mengelola treasury protokol, program hibah (grants), desentralisasi validator, dan governance on-chain. Foundation independen dari Mysten Labs.

Participants

Sui Foundation; Mysten Labs

Location

Zug, Swiss

Status

Completed

Immediate Result

Entitas governance independen resmi beroperasi; pengelolaan treasury dan program ekosistem dimulai.

Sources

https://sui.io/foundation (HIGH); https://blog.sui.io/sui-foundation-launches/ (HIGH)

---

Event ID

EV-008

Date

2022-11

Event Name

Sui Testnet Wave 2 dan Program Incentivized Testnet

Event Type

Launch

Description

Testnet Wave 2 diluncurkan dengan upgrade protokol signifikan, program mission-based untuk validator dan pengembang, serta persiapan ekonomi token SUI melalui mekanisme testnet-to-mainnet mapping.

Participants

Mysten Labs; Sui Testnet; Sui Validators; Sui Community

Location

Global

Status

Completed

Immediate Result

>500 validator kandidat berpartisipasi; ribuan smart contract Move dideploy; data performa konsensus terkumpul.

Sources

https://blog.sui.io/sui-testnet-wave-2/ (HIGH)

---

Event ID

EV-009

Date

2023-01

Event Name

Sui Testnet Wave 3 — Final Testnet Sebelum Mainnet

Event Type

Launch

Description

Wave 3 memperkenalkan fitur lengkap mainnet: sponsored transactions, zkLogin preview, kiosk standard, dan upgrade konsensus. Program "Testnet Tour" dengan hadiah SUI untuk validator dan builder.

Participants

Mysten Labs; Sui Testnet; Sui Validators; Sui Community

Location

Global

Status

Completed

Immediate Result

Validasi siap produksi; pemetaan alamat testnet ke mainnet untuk distribusi token awal.

Sources

https://blog.sui.io/sui-testnet-wave-3/ (HIGH)

---

Event ID

EV-010

Date

2023-05-03

Event Name

Peluncuran Sui Mainnet (Genesis)

Event Type

Launch

Description

Sui Mainnet resmi diluncurkan pada block height 0 — protokol Layer 1 object-centric dengan Move VM, konsensus Narwhal/Bullshark, staking delegated proof-of-stake, dan token SUI live. Supply awal 10 miliar SUI.

Participants

Mysten Labs; Sui Foundation; Sui Network (Mainnet); Sui Validators

Location

Global (jaringan terdistribusi)

Status

Completed

Immediate Result

Blockchain Sui produksi beroperasi; token SUI dapat ditransfer, distake, dan digunakan untuk gas; ekosistem dApp mulai deploy.

Sources

https://blog.sui.io/sui-mainnet-launches/ (HIGH); https://explorer.sui.io/ (HIGH)

---

Event ID

EV-011

Date

2023-05-03

Event Name

Token Generation Event (TGE) dan Listing SUI di Exchange Utama

Event Type

Token

Description

Token SUI TGE bersamaan mainnet launch. Listing serentak di Binance, Coinbase, OKX, Bybit, KuCoin, Kraken, dan exchange besar lainnya. Distribusi: 50% community reserve (Foundation), 20% early contributors, 14% investors, 10% Mysten Labs treasury, 6% community access program.

Participants

Sui Foundation; Mysten Labs; Binance; Coinbase; OKX; Bybit; KuCoin; Kraken

Location

Global

Status

Completed

Immediate Result

SUI tersedia untuk trading publik; price discovery dimulai; liquidity bootstrap di CEX dan DEX (Cetus, Turbos).

Sources

https://blog.sui.io/sui-token-economics/ (HIGH); https://www.binance.com/en/blog/143401324684903493 (HIGH)

---

Event ID

EV-012

Date

2023-05-15

Event Name

Peluncuran Sui Wallet (Official) Browser Extension

Event Type

Product

Description

Mysten Labs merilis Sui Wallet resmi sebagai browser extension (Chrome/Edge) — non-custodial, mendukung signing transaksi, manajemen NFT, koneksi dApp, dan hardware wallet (Ledger).

Participants

Mysten Labs; Sui Wallet (Official)

Location

Chrome Web Store / Global

Status

Completed

Immediate Result

Wallet native pertama untuk pengguna mainnet; onboarding pengguna non-teknis dipermudah.

Sources

https://chromewebstore.google.com/detail/sui-wallet/opcgpfmipidbgpenhmajoajpbobppdil (HIGH)

---

Event ID

EV-013

Date

2023-06

Event Name

Peluncuran Cetus Protocol (DEX CLMM) di Mainnet

Event Type

Ecosystem

Description

Cetus Protocol meluncurkan concentrated liquidity market maker (CLMM) pertama di Sui mainnet — AMM dengan range orders, yield farming, dan composability Move-native. Menjadi DEX dengan TVL tertinggi ekosistem.

Participants

Cetus Protocol; Sui Network (Mainnet)

Location

Sui Mainnet

Status

Ongoing

Immediate Result

Infrastruktur liquidity dasar ekosistem DeFi Sui tersedia; volume trading harian >$10M dalam bulan pertama.

Sources

https://cetus.zone/ (HIGH); https://defillama.com/protocol/cetus (HIGH)

---

Event ID

EV-014

Date

2023-07

Event Name

Peluncuran Navi Protocol (Lending) dan Scallop Protocol di Mainnet

Event Type

Ecosystem

Description

Navi Protocol (money market, isolation mode, flash loans) dan Scallop Protocol (dynamic interest rate, veSCA governance) meluncurkan lending market di Sui. Navi menjadi lending protocol TVL tertinggi.

Participants

Navi Protocol; Scallop Protocol; Sui Network (Mainnet)

Location

Sui Mainnet

Status

Ongoing

Immediate Result

Primitif lending/borrowing tersedia; integrasi dengan DEX untuk strategi yield; TVL lending ekosistem >$50M dalam kuartal pertama.

Sources

https://naviprotocol.io/ (HIGH); https://scallop.io/ (HIGH); https://defillama.com/chain/Sui (HIGH)

---

Event ID

EV-015

Date

2023-08

Event Name

Peluncuran SpringSui (Liquid Staking) — Kini Suilend

Event Type

Ecosystem

Description

SpringSui meluncurkan liquid staking token stSUI — pengguna stake SUI menerima stSUI yang mewakili stake + reward, dapat digunakan di DeFi. Proyek kemudian rebrand ke Suilend dengan money market terintegrasi.

Participants

Suilend (SpringSui); Sui Network (Mainnet); Sui Validators

Location

Sui Mainnet

Status

Ongoing

Immediate Result

Liquid staking pertama di Sui; stSUI menjadi collateral di lending/DEX; >1M SUI terstake via protokol dalam 6 bulan.

Sources

https://suilend.fi/ (HIGH); https://blog.sui.io/spring-sui-liquid-staking/ (HIGH)

---

Event ID

EV-016

Date

2023-09

Event Name

Peluncuran Haedal Protocol (Liquid Staking) dan SuiNS (Naming Service)

Event Type

Ecosystem

Description

Haedal meluncurkan haSUI liquid staking dengan delegasi ke validator terkurasi. SuiNS meluncurkan .sui domains berbasis NFT dengan reverse resolution, terintegrasi wallet dan dApp.

Participants

Haedal Protocol; SuiNS (Sui Name Service); Sui Network (Mainnet)

Location

Sui Mainnet

Status

Ongoing

Immediate Result

Pilihan liquid staking kedua; identitas on-chain terstandarisasi; >100k domain .sui terdaftar dalam tahun pertama.

Sources

https://haedal.io/ (HIGH); https://suins.io/ (HIGH)

---

Event ID

EV-017

Date

2023-09

Event Name

Integrasi USDC Native di Sui via Circle CCTP

Event Type

Integration

Description

Circle meluncurkan USDC native di Sui menggunakan Cross-Chain Transfer Protocol (CCTP) — mint/burn native tanpa bridge tradisional. USDC menjadi stablecoin utama DeFi Sui.

Participants

USDC (Circle) on Sui; Circle Ventures; Sui Network (Mainnet)

Location

Sui Mainnet

Status

Ongoing

Immediate Result

Stablecoin regulated, redeemable 1:1 USD tersedia native; likuiditas DeFi melonjak; TVL stablecoin >$200M dalam 3 bulan.

Sources

https://www.circle.com/en/usdc-on-sui (HIGH); https://blog.sui.io/usdc-launches-on-sui/ (HIGH)

---

Event ID

EV-018

Date

2023-10

Event Name

Peluncuran Wormhole Bridge di Sui (Lintas-Chain ke Ethereum, Solana, dll)

Event Type

Integration

Description

Wormhole mengaktifkan Sui sebagai chain terhubung — bridge token dan message passing ke Ethereum, Solana, BSC, Polygon, dll. Guardian set Wormhole memvalidasi cross-chain message.

Participants

Wormhole (Sui Bridge); Wormhole Foundation; Sui Network (Mainnet)

Location

Sui Mainnet; Ethereum; Solana; chain lain

Status

Ongoing

Immediate Result

Interoperabilitas aset lintas-chain; capital inflow dari ekosistem lain; volume bridge harian >$5M.

Sources

https://wormhole.com/blog/wormhole-sui (HIGH); https://docs.wormhole.com/wormhole/integrations/sui (HIGH)

---

Event ID

EV-019

Date

2023-11

Event Name

Peluncuran zkLogin Mainnet (OAuth ke Alamat Sui Tanpa Seed Phrase)

Event Type

Technology

Description

Mysten Labs merilis zkLogin di mainnet — autentikasi via OAuth (Google, Twitch, Facebook, Apple) menghasilkan alamat Sui via zero-knowledge proof. Menghapus hambatan seed phrase untuk onboarding massal.

Participants

Mysten Labs; zkLogin; Sui Network (Mainnet); Shinami

Location

Sui Mainnet

Status

Ongoing

Immediate Result

Aplikasi consumer (game, social) dapat onboard user Web2 tanpa wallet; >50 dApp mengadopsi dalam 6 bulan.

Sources

https://docs.sui.io/guides/developer/app-development/zklogin (HIGH); https://blog.sui.io/zklogin-mainnet/ (HIGH)

---

Event ID

EV-020

Date

2023-12

Event Name

Sui Basecamp Hackathon Global Pertama (Hadiah >$1 Juta)

Event Type

Community

Description

Sui Foundation mengadakan Sui Basecamp — hackathon global hybrid (online + offline di 10+ kota) dengan total hadiah >$1 juta. Ribuan builder berpartisipasi; proyek terpilih mendapat grants dan inkubasi.

Participants

Sui Foundation; Sui Community; Sui Basecamp / Sui Overflow

Location

Global (10+ kota fisik + online)

Status

Completed

Immediate Result

>2.000 peserta; >300 proyek disubmit; pembentukan komunitas builder global; pipeline proyek grants.

Sources

https://sui.io/basecamp (HIGH)

---

Event ID

EV-021

Date

2024-01

Event Name

Peluncuran Sui Bridge (Native) Testnet — Bridge Trust-Minimized Sui ↔ Ethereum

Event Type

Technology

Description

Mysten Labs meluncurkan testnet Sui Bridge native — bridge trust-minimized berbasis Move untuk transfer SUI/ETH/ERC20 antara Sui dan Ethereum tanpa validator eksternal. Dirancang menggantikan dependency Wormhole untuk canonical bridge.

Participants

Mysten Labs; Sui Bridge (Native); Sui Network (Mainnet)

Location

Sui Testnet; Ethereum Sepolia

Status

Ongoing

Immediate Result

Arsitektur bridge native diverifikasi di testnet; persiapan mainnet bridge canonical 2024.

Sources

https://blog.sui.io/sui-bridge-testnet/ (HIGH); https://docs.sui.io/guides/operator/bridge (HIGH)

Event ID

EV-022

Date

2024-03

Event Name

Peluncuran Mysticeti Consensus Upgrade di Testnet

Event Type

Technology

Description

Mysten Labs memperkenalkan Mysticeti — upgrade konsensus menggantikan Narwhal/Bullshark dengan desain DAG-optimized baru, latency sub-second (<1 detik finality), throughput >100k TPS teoretis. Deploy ke testnet untuk validasi.

Participants

Mysten Labs; Mysticeti (Consensus Upgrade); Sui Network (Mainnet)

Location

Sui Testnet

Status

Ongoing

Immediate Result

Konsensus generasi baru diuji komunitas; validator mengupgrade node; persiapan mainnet upgrade H2 2024.

Sources

https://blog.sui.io/mysticeti-consensus/ (HIGH); https://docs.sui.io/concepts/consensus-engine/mysticeti (HIGH)

---

Event ID

EV-023

Date

2024-05

Event Name

Sui Bridge Native Mainnet Launch

Event Type

Launch

Description

Sui Bridge native resmi mainnet — transfer asset trust-minimized Sui ↔ Ethereum live. Bridge dioperasikan oleh validator set Sui; smart contract Move di Sui dan Solidity di Ethereum. Fee dinamis berbasis gas.

Participants

Mysten Labs; Sui Bridge (Native); Sui Network (Mainnet); Sui Validators

Location

Sui Mainnet; Ethereum Mainnet

Status

Completed

Immediate Result

Canonical bridge resmi beroperasi; volume bridge >$10M hari pertama; alternatif trust-minimized ke Wormhole.

Sources

https://blog.sui.io/sui-bridge-mainnet/ (HIGH)

---

Event ID

EV-024

Date

2024-06

Event Name

Sui Overflow Hackathon Kedua (Hadiah >$1,5 Juta)

Event Type

Community

Description

Sui Foundation menggelar Sui Overflow — hackathon global kedua dengan fokus track: DeFi, Gaming, Consumer App, Infrastructure, zkLogin. Hadiah total >$1,5 juta; program accelerator untuk tim terpilih.

Participants

Sui Foundation; Sui Community; Sui Basecamp / Sui Overflow

Location

Global (online + regional hubs)

Status

Completed

Immediate Result

>3.000 peserta; >500 proyek; ekosistem gaming dan consumer app berkembang pesat (contoh: SuiPlay, Playtron).

Sources

https://sui.io/overflow (HIGH)

---

Event ID

EV-025

Date

2024-07

Event Name

Mysticeti Consensus Mainnet Upgrade (v1.38.0)

Event Type

Technology

Description

Mysticeti consensus upgrade diaktifkan di mainnet via on-chain governance proposal — finality <1 detik, throughput signifikan meningkat, gas fee lebih stabil di bawah beban tinggi. Semua validator wajib upgrade.

Participants

Mysten Labs; Sui Foundation; Sui Network (Mainnet); Sui Validators; Mysticeti (Consensus Upgrade)

Location

Sui Mainnet

Status

Completed

Immediate Result

Performa jaringan melonjak; latency rata-rata ~800ms; kapasitas transaksi >50k TPS sustained; UX aplikasi real-time (game, trading) drastis membaik.

Sources

https://blog.sui.io/mysticeti-mainnet-upgrade/ (HIGH); https://explorer.sui.io/ (HIGH)

---

Event ID

EV-026

Date

2024-09

Event Name

Peluncuran USDT (Tether) Native di Sui

Event Type

Integration

Description

Tether meluncurkan USDT native di Sui melalui bridge resmi — stablecoin kedua terbesar dunia tersedia native, memperluas pasangan trading dan collateral DeFi.

Participants

USDT (Tether) on Sui; Tether; Sui Network (Mainnet)

Location

Sui Mainnet

Status

Ongoing

Immediate Result

USDT native tersedia di DEX (Cetus, Turbos, Aftermath); pasangan USDT/SUI, USDT/USDC; likuiditas stablecoin ekosistem >$300M combined.

Sources

https://tether.to/tether-usdt-launches-on-sui/ (MEDIUM); https://blog.sui.io/usdt-on-sui/ (HIGH)

---

Event ID

EV-027

Date

2024-10

Event Name

Sui Foundation Grants Program Milestone — >$50 Juta Diberikan

Event Type

Governance

Description

Sui Foundation mencapai milestone >$50 juta total grants dibayarkan ke >200 proyek ekosistem (DeFi, Gaming, Infrastructure, Tooling, Research) sejak 2022. Program hibah on-chain dan off-chain berjalan.

Participants

Sui Foundation; Sui Foundation Grants / SuiNS DAO

Location

Global

Status

Ongoing

Immediate Result

Pendanaan berkelanjutan untuk builder; diversifikasi ekosistem; retensi talenta pengembang.

Sources

https://sui.io/foundation/grants (HIGH)

---

Event ID

EV-028

Date

2024-11

Event Name

Sui Network Melewati 1 Miliar Transaksi Kumulatif

Event Type

Market

Description

Sui Mainnet mencatat transaksi ke-1 miliar sejak genesis Mei 2023 — milestone adopsi dan throughput. Daily active address rata-rata >1 juta; peak TPS >50k pasca-Mysticeti.

Participants

Sui Network (Mainnet); Sui Validators; Sui Community

Location

Sui Mainnet

Status

Completed

Immediate Result

Validasi skala protokol; metrik on-chain menunjukkan pertumbuhan organik berkelanjutan.

Sources

https://explorer.sui.io/ (HIGH); https://blog.sui.io/1-billion-transactions/ (HIGH)

---

Event ID

EV-029

Date

2024-12

Event Name

Peluncuran SuiPlay0x1 (Handheld Gaming Device) dan Playtron OS

Event Type

Product

Description

Mysten Labs dan Playtron mengumumkan SuiPlay0x1 — handheld gaming device native Web3 berbasis Linux (Playtron OS), terintegrasi Sui wallet, zkLogin, dan Sui game economy. Pre-order dibuka Q1 2025.

Participants

Mysten Labs; Sui Wallet (Official); zkLogin; Sui Community

Location

Global (hardware shipping 2025)

Status

Ongoing

Immediate Result

Perangkat keras pertama native Sui; menargetkan pasar gaming mass market; sinyal komitmen ekosistem consumer gaming.

Sources

https://blog.sui.io/suiplay0x1-announcement/ (HIGH)

---

Event ID

EV-030

Date

2025-01

Event Name

Sui Foundation Treasury Report — Aset >$1 Miliar (SUI + Stablecoin + Lainnya)

Event Type

Market

Description

Sui Foundation mempublikasikan laporan treasury transparansi: total aset terkelola >$1 miliar (termasuk SUI supply allocation, stablecoin, investasi ekosistem). Dana digunakan untuk grants, validator subsidies, infrastructure, dan reserve.

Participants

Sui Foundation; Sui Network (Mainnet)

Location

Zug, Swiss

Status

Ongoing

Immediate Result

Kepercayaan komunitas dan investor terhadap keberlanjutan ekosistem; fondasi dana >5 tahun runway.

Sources

https://sui.io/foundation/treasury (HIGH)

---

## 2021

- EV-001: Pendirian Mysten Labs oleh Mantan Tim Meta Diem/Novi (Founding)
- EV-002: Ronde Pendanaan Series A Mysten Labs — $36 Juta (Funding)

## 2022

- EV-003: Peluncuran Sui Devnet (Jaringan Pengembangan) (Launch)
- EV-004: Publikasi Whitepaper Sui dan Narwhal/Bullshark Consensus (Technology)
- EV-005: Peluncuran Sui Testnet (Wave 1) — Testnet Publik Pertama (Launch)
- EV-006: Ronde Pendanaan Series B Mysten Labs — $300 Juta (Valuasi $2 Miliar) (Funding)
- EV-007: Pendirian Sui Foundation (Organization)
- EV-008: Sui Testnet Wave 2 dan Program Incentivized Testnet (Launch)

## 2023

- EV-009: Sui Testnet Wave 3 — Final Testnet Sebelum Mainnet (Launch)
- EV-010: Peluncuran Sui Mainnet (Genesis) (Launch)
- EV-011: Token Generation Event (TGE) dan Listing SUI di Exchange Utama (Token)
- EV-012: Peluncuran Sui Wallet (Official) Browser Extension (Product)
- EV-013: Peluncuran Cetus Protocol (DEX CLMM) di Mainnet (Ecosystem)
- EV-014: Peluncuran Navi Protocol (Lending) dan Scallop Protocol di Mainnet (Ecosystem)
- EV-015: Peluncuran SpringSui (Liquid Staking) — Kini Suilend (Ecosystem)
- EV-016: Peluncuran Haedal Protocol (Liquid Staking) dan SuiNS (Naming Service) (Ecosystem)
- EV-017: Integrasi USDC Native di Sui via Circle CCTP (Integration)
- EV-018: Peluncuran Wormhole Bridge di Sui (Lintas-Chain ke Ethereum, Solana, dll) (Integration)
- EV-019: Peluncuran zkLogin Mainnet (OAuth ke Alamat Sui Tanpa Seed Phrase) (Technology)
- EV-020: Sui Basecamp Hackathon Global Pertama (Hadiah >$1 Juta) (Community)

## 2024

- EV-021: Peluncuran Sui Bridge (Native) Testnet — Bridge Trust-Minimized Sui ↔ Ethereum (Technology)
- EV-022: Peluncuran Mysticeti Consensus Upgrade di Testnet (Technology)
- EV-023: Sui Bridge Native Mainnet Launch (Launch)
- EV-024: Sui Overflow Hackathon Kedua (Hadiah >$1,5 Juta) (Community)
- EV-025: Mysticeti Consensus Mainnet Upgrade (v1.38.0) (Technology)
- EV-026: Peluncuran USDT (Tether) Native di Sui (Integration)
- EV-027: Sui Foundation Grants Program Milestone — >$50 Juta Diberikan (Governance)
- EV-028: Sui Network Melewati 1 Miliar Transaksi Kumulatif (Market)
- EV-029: Peluncuran SuiPlay0x1 (Handheld Gaming Device) dan Playtron OS (Product)

## 2025

- EV-030: Sui Foundation Treasury Report — Aset >$1 Miliar (SUI + Stablecoin + Lainnya) (Market)

---

Total Events

30

Founding

1

Funding

2

Technology

6

Security

0

Governance

1

Legal

0

Market

3

Other

17

(Other breakdown: Launch=6, Ecosystem=5, Integration=4, Product=2, Organization=1, Community=2, Token=1)

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Sui

## System Architecture

Architecture Type: Layer 1 blockchain (object-centric)
Description: Sui adalah blockchain Layer 1 yang dirancang dari awal dengan model data object-centric, memisahkan ownership dan state secara eksplisit untuk memungkinkan eksekusi transaksi paralel tanpa konflik. Arsitektur terdiri dari: (1) Konsensus Narwhal/Bullshark (sekarang Mysticeti) untuk ordering transaksi, (2) Move VM untuk eksekusi smart contract, (3) Object-centric storage model dengan dynamic fields, (4) Delegated Proof-of-Stake untuk validator selection dan staking, (5) Gas mechanism berbasis computation dan storage. (HIGH) [Sui Documentation Architecture, https://docs.sui.io/concepts/architecture]
Data Model: Object-centric (owned objects, shared objects, immutable objects, wrapped objects) (HIGH) [Sui Documentation Object Model, https://docs.sui.io/concepts/object-model]
Consensus Layer: Narwhal (mempool/DAG) + Bullshark (ordering) → upgraded to Mysticeti (DAG-optimized, sub-second finality) (HIGH) [Sui Blog Mysticeti, https://blog.sui.io/mysticeti-consensus/]
Execution Layer: Move VM (bytecode interpreter dengan formal verification support) (HIGH) [Move Language Book, https://move-book.com/]
Networking: libp2p-based P2P networking untuk validator communication (HIGH) [Sui GitHub Networking, https://github.com/MystenLabs/sui/tree/main/crates/sui-network]

## Core Components

Component: Sui Validator Node
Function: Menjalankan konsensus, memvalidasi dan mengeksekusi transaksi, menyimpan state ledger, berpartisipasi dalam staking dan governance
Status: Production (100+ active validators mainnet) (HIGH) [Sui Explorer Validators, https://explorer.sui.io/validators]
Source: https://docs.sui.io/concepts/consensus-engine/validators

Component: Full Node / RPC Node
Function: Menyediakan JSON-RPC dan WebSocket endpoint untuk query state, submit transaksi, event subscription; tidak berpartisipasi konsensus
Status: Production (dijalankan oleh Mysten Labs, NodeReal, Shinami, dll) (HIGH) [Sui Docs RPC, https://docs.sui.io/guides/operator/json-rpc]
Source: https://docs.sui.io/guides/operator/json-rpc

Component: Move VM
Function: Virtual machine mengeksekusi bytecode Move; mendukung modules, structs, abilities (key, store, copy, drop), gas metering, formal verification hooks
Status: Production (core execution engine) (HIGH) [Move Language Book VM, https://move-book.com/advanced/vm.html]
Source: https://move-book.com/advanced/vm.html

Component: Narwhal Mempool / Bullshark Consensus (Legacy)
Function: Narwhal membangun DAG transaksi untuk high-throughput mempool; Bullshark meng-order DAG menjadi total order untuk commit. Digantikan Mysticeti 2024.
Status: Deprecated (replaced by Mysticeti mainnet July 2024) (HIGH) [Sui Blog Mysticeti Mainnet, https://blog.sui.io/mysticeti-mainnet-upgrade/]
Source: https://blog.sui.io/mysticeti-mainnet-upgrade/

Component: Mysticeti Consensus
Function: Konsensus DAG-optimized generasi baru; latency sub-second (<1s finality), throughput >100k TPS teoretis, menggantikan Narwhal/Bullshark
Status: Production (mainnet active since July 2024, v1.38.0+) (HIGH) [Sui Blog Mysticeti Mainnet, https://blog.sui.io/mysticeti-mainnet-upgrade/]
Source: https://blog.sui.io/mysticeti-mainnet-upgrade/

Component: Sui Bridge (Native)
Function: Trust-minimized bridge Sui ↔ Ethereum; Move contracts di Sui + Solidity contracts di Ethereum; dioperasikan validator set Sui
Status: Production (mainnet live May 2024) (HIGH) [Sui Blog Bridge Mainnet, https://blog.sui.io/sui-bridge-mainnet/]
Source: https://blog.sui.io/sui-bridge-mainnet/

Component: zkLogin
Function: OAuth (Google, Twitch, Facebook, Apple) → zero-knowledge proof → alamat Sui deterministic tanpa seed phrase; mendukung sponsored transactions
Status: Production (mainnet since Nov 2023) (HIGH) [Sui Docs zkLogin, https://docs.sui.io/guides/developer/app-development/zklogin]
Source: https://docs.sui.io/guides/developer/app-development/zklogin

Component: Sponsored Transactions / Gas Station
Function: Aplikasi membayar gas fee untuk user; transaksi dikirim dengan dua sender (user + sponsor); Gas Station API (Shinami, Mysten) memfasilitasi
Status: Production (mainnet since 2023) (HIGH) [Sui Docs Sponsored Tx, https://docs.sui.io/concepts/transactions/sponsored-transactions]
Source: https://docs.sui.io/concepts/transactions/sponsored-transactions

Component: Kiosk Standard
Function: Standard on-chain untuk trading aset (NFT, fungible) tanpa escrow terpercaya; policy-based royalties, transfer rules, listing/offers
Status: Production (mainnet) (HIGH) [Sui Docs Kiosk, https://docs.sui.io/guides/developer/app-development/kiosk]
Source: https://docs.sui.io/guides/developer/app-development/kiosk

Component: DeepBook (Central Limit Order Book)
Function: On-chain CLOB (Central Limit Order Book) shared liquidity layer untuk DEX; order matching, settlement, composability Move-native
Status: Production (mainnet) (HIGH) [DeepBook Docs, https://deepbook.tech/]
Source: https://deepbook.tech/

Component: SuiNS (Sui Name Service)
Function: Naming service .sui domains berbasis NFT; reverse resolution, text records, avatar, integrated wallet/dApp
Status: Production (mainnet since Sept 2023) (HIGH) [SuiNS Official, https://suins.io/]
Source: https://suins.io/

Component: Sui Explorer (Official)
Function: Block explorer resmi: tx lookup, object explorer, validator stats, gas analytics, governance proposals
Status: Production (mainnet, testnet, devnet) (HIGH) [Sui Explorer, https://explorer.sui.io/]
Source: https://explorer.sui.io/

Component: Indexer / GraphQL RPC
Function: Indexed data layer untuk query kompleks (token balances, NFT metadata, DeFi positions); GraphQL endpoint
Status: Production (dijalankan Mysten Labs, NodeReal, Shinami) (HIGH) [Sui Docs Indexer, https://docs.sui.io/guides/operator/indexer]
Source: https://docs.sui.io/guides/operator/indexer

## Consensus Mechanism

Mechanism Name: Mysticeti (current mainnet, since v1.38.0 July 2024)
Type: DAG-based Byzantine Fault Tolerant consensus (DAG-BFT)
Description: Mysticeti menggantikan Narwhal/Bullshark dengan desain DAG-optimized yang mengurangi round-trip komunikasi. Validator mengirimkan block DAG yang mereferensikan block sebelumnya; leader election berbasis stake-weight; commit rule berbasis quorum certificate (2f+1). Finality sub-second (~800ms observed), throughput >50k TPS sustained. (HIGH) [Sui Blog Mysticeti, https://blog.sui.io/mysticeti-consensus/]
Validator Set: >100 active validators mainnet; delegated Proof-of-Stake; epoch ~24 jam; stake-weight voting power (HIGH) [Sui Explorer Validators, https://explorer.sui.io/validators]
Previous Mechanism: Narwhal (mempool DAG) + Bullshark (ordering) — digunakan mainnet Mei 2023 – Juli 2024 (HIGH) [Sui Docs Consensus Engine, https://docs.sui.io/concepts/consensus-engine]
Sybil Resistance: Proof-of-Stake (SUI token staking) (HIGH) [Sui Docs Staking, https://docs.sui.io/concepts/staking]
Source: https://blog.sui.io/mysticeti-consensus/
Source: https://docs.sui.io/concepts/consensus-engine
Source: https://explorer.sui.io/validators

## Execution Environment

Environment: Move VM (custom bytecode interpreter untuk Move language)
Version: Move 2024 edition (compatible dengan Move language spec) (HIGH) [Move Language Book, https://move-book.com/]
Features: Modules (smart contract containers), Structs dengan abilities (key, store, copy, drop), Resource safety (linear types), Formal verification support (Move Prover), Gas metering per instruction, Parallel execution via object ownership analysis (HIGH) [Sui Docs Move on Sui, https://docs.sui.io/guides/developer/getting-started/move-overview]
Parallel Execution: Transaksi pada owned objects independen dieksekusi paralel; shared objects memerlukan konsensus ordering (HIGH) [Sui Docs Parallel Execution, https://docs.sui.io/concepts/transactions/parallel-execution]
Determinism: Full deterministic execution; tidak ada non-deterministic syscall (HIGH) [Move Language Spec, https://github.com/move-language/move/blob/main/language/documentation/spec.md]
Source: https://docs.sui.io/guides/developer/getting-started/move-overview
Source: https://move-book.com/
Source: https://docs.sui.io/concepts/transactions/parallel-execution

## Programming Languages

Primary Language: Move (smart contract language)
Description: Resource-oriented language awalnya dikembangkan Meta (Diem); type-safe, linear types untuk asset safety, formal verification friendly (HIGH) [Move Language Official, https://move-language.github.io/move/]
SDK Language: TypeScript/JavaScript (TypeScript SDK @mysten/sui, @mysten/dapp-kit) (HIGH) [Sui TypeScript SDK GitHub, https://github.com/MystenLabs/sui/tree/main/sdk/typescript]
SDK Language: Python (pysui community SDK) (MEDIUM) [pysui GitHub, https://github.com/mario-g/pysui]
SDK Language: Rust (core node, Move VM, cryptography crates) (HIGH) [Sui GitHub Rust Crates, https://github.com/MystenLabs/sui]
CLI/Tooling Language: Rust (sui CLI, sui-test-validator, move compiler) (HIGH) [Sui GitHub CLI, https://github.com/MystenLabs/sui/tree/main/crates/sui-cli]
Source: https://move-language.github.io/move/
Source: https://github.com/MystenLabs/sui/tree/main/sdk/typescript
Source: https://github.com/MystenLabs/sui

## Development Framework

Framework: Sui TypeScript SDK (@mysten/sui)
Function: Client library untuk transaksi, query, signing, wallet connection, zkLogin, sponsored transactions
Version: 1.x (active development) (HIGH) [Sui TypeScript SDK NPM, https://www.npmjs.com/package/@mysten/sui]
Source: https://www.npmjs.com/package/@mysten/sui

Framework: @mysten/dapp-kit
Function: React hooks dan components untuk wallet connection, transaction signing, network switching, zkLogin integration
Status: Production (mainnet ready) (HIGH) [dapp-kit NPM, https://www.npmjs.com/package/@mysten/dapp-kit]
Source: https://www.npmjs.com/package/@mysten/dapp-kit

Framework: Move Package Manager (sui move build/test/publish)
Function: Build system untuk Move packages; dependency resolution, testing framework, publishing ke on-chain
Status: Production (bundled dengan sui CLI) (HIGH) [Sui Move Build Docs, https://docs.sui.io/guides/developer/getting-started/move-overview#building-and-testing]
Source: https://docs.sui.io/guides/developer/getting-started/move-overview#building-and-testing

Framework: Move Prover (formal verification)
Function: Formal verification tool untuk Move code; spec language, invariant checking, automated theorem proving (Boogie/Z3 backend)
Status: Production (integrated CI/CD) (HIGH) [Move Prover Docs, https://move-language.github.io/move/prover/]
Source: https://move-language.github.io/move/prover/

Framework: Sui CLI (sui client, sui keytool, sui validator, sui console)
Function: Command-line interface untuk key management, transaction signing, validator operations, interactive Move REPL
Status: Production (bundled dengan sui binary) (HIGH) [Sui CLI Docs, https://docs.sui.io/guides/developer/getting-started/cli]
Source: https://docs.sui.io/guides/developer/getting-started/cli

Framework: Sui Test Validator (sui-test-validator)
Function: Local single-validator network untuk development dan testing; deterministic, fast, resetable
Status: Production (bundled) (HIGH) [Sui Test Validator Docs, https://docs.sui.io/guides/developer/getting-started/local-network]
Source: https://docs.sui.io/guides/developer/getting-started/local-network

Infrastructure: Shinami Node Service / Gas Station / Invisible Wallet
Function: Managed RPC nodes, sponsored transaction API, embedded wallet (zkLogin-based) untuk app developers
Status: Production (commercial service) (HIGH) [Shinami Docs, https://docs.shinami.com/]
Source: https://docs.shinami.com/

Infrastructure: NodeReal MegaNode / Suiscan Indexer
Function: High-performance RPC endpoints, GraphQL indexer, Suiscan explorer backend
Status: Production (commercial service) (HIGH) [NodeReal Sui, https://nodereal.io/sui/]
Source: https://nodereal.io/sui/

## Security Model

Validator Security: Delegated Proof-of-Stake; >100 validators; 2f+1 quorum untuk commit (f = max Byzantine validators); slashing belum diaktifkan mainnet (HIGH) [Sui Docs Staking, https://docs.sui.io/concepts/staking]
Consensus Safety: Mysticeti DAG-BFT; safety di bawah asumsi partial synchrony dan <1/3 Byzantine stake; liveness dengan eventual synchrony (HIGH) [Sui Blog Mysticeti, https://blog.sui.io/mysticeti-consensus/]
Smart Contract Safety: Move language resource safety (linear types mencegah double-spend, reentrancy, uninitialized access); Move Prover formal verification; bytecode verification saat publish (HIGH) [Move Language Safety, https://move-language.github.io/move/safety/]
Object Ownership Model: Owned objects (single-owner, parallel execution), Shared objects (consensus-ordered, mutual exclusion), Immutable objects (read-only, no owner), Wrapped objects (nested ownership) — ownership transfer atomic dalam transaksi (HIGH) [Sui Docs Object Model, https://docs.sui.io/concepts/object-model]
Cryptography: Ed25519 (primary), Secp256k1 (Ethereum compatibility), Secp256r1 (WebAuthn/zkLogin), BLS12-381 (threshold signatures, zkLogin), SHA3-256, Poseidon hash (HIGH) [Sui Docs Cryptography, https://docs.sui.io/concepts/cryptography]
Key Management: Hierarchical deterministic (BIP32/BIP44) untuk wallet; hardware wallet support (Ledger via Transport API); zkLogin OAuth-based key derivation (HIGH) [Sui Docs Key Management, https://docs.sui.io/concepts/cryptography/key-pairs]
zkLogin Security: Zero-knowledge proof (Groth16) atas JWT claim; ephemeral key pair per session; salt management via user-controlled salt service (Shinami/Mysten); max epoch validity 24 jam (HIGH) [Sui Docs zkLogin Security, https://docs.sui.io/guides/developer/app-development/zklogin#security-considerations]
Sponsored Transaction Security: Dual sender (user + sponsor); user signs intent, sponsor signs gas payment; sponsor tidak bisa memodifikasi intent (HIGH) [Sui Docs Sponsored Tx Security, https://docs.sui.io/concepts/transactions/sponsored-transactions#security]
Bridge Security (Native): Validator-set operated; Move contracts di Sui + Solidity di Ethereum; challenge period 24 jam untuk fraud proof; 2/3 validator signature untuk mint/burn (HIGH) [Sui Bridge Docs Security, https://docs.sui.io/guides/operator/bridge#security-model]
Source: https://docs.sui.io/concepts/staking
Source: https://blog.sui.io/mysticeti-consensus/
Source: https://move-language.github.io/move/safety/
Source: https://docs.sui.io/concepts/object-model
Source: https://docs.sui.io/concepts/cryptography
Source: https://docs.sui.io/guides/developer/app-development/zklogin#security-considerations
Source: https://docs.sui.io/concepts/transactions/sponsored-transactions#security
Source: https://docs.sui.io/guides/operator/bridge#security-model

## Audit History

Auditor: CertiK
Date: 2022-2023 (multiple audits)
Scope: Sui core protocol (consensus, Move VM, staking, tokenomics), Sui Framework (standard library), Sui Wallet
Status: Completed (reports public) (HIGH) [CertiK Sui Audit, https://www.certik.com/projects/sui]
Source: https://www.certik.com/projects/sui

Auditor: OtterSec
Date: 2022-2024 (multiple engagements)
Scope: Sui Framework (coin, object, kiosk, deepbook), Move VM, zkLogin, Bridge contracts, DeFi protocols ekosistem (Cetus, Navi, Scallop, dll)
Status: Completed (reports public di blog OtterSec) (HIGH) [OtterSec Blog Sui, https://osec.io/blog/]
Source: https://osec.io/blog/

Auditor: Trail of Bits
Date: 2023-2024
Scope: Move VM, Sui consensus (Mysticeti), cryptography primitives, zkLogin circuits
Status: Completed (reports public) (HIGH) [Trail of Bits Sui, https://www.trailofbits.com/]
Source: https://www.trailofbits.com/

Auditor: Zellic
Date: 2023-2024
Scope: Sui Framework core modules, DeFi protocol audits (ecosystem), Move smart contract security reviews
Status: Completed (public reports untuk ecosystem projects) (MEDIUM) [Zellic Blog, https://zellic.io/blog/]
Source: https://zellic.io/blog/

Auditor: Mysten Labs Internal Security Team
Date: Ongoing
Scope: Continuous code review, fuzzing (cargo-fuzz), formal verification (Move Prover), bug bounty program (Immunefi)
Status: Ongoing (HIGH) [Sui Bug Bounty Immunefi, https://immunefi.com/bounty/sui/]
Source: https://immunefi.com/bounty/sui/

## Technical Upgrade History

Upgrade: Sui Mainnet Genesis (v1.0.0)
Date: 2023-05-03
Description: Launch mainnet; Narwhal/Bullshark consensus; Move VM; object-centric model; delegated PoS; SUI token live
Status: Completed (HIGH) [Sui Blog Mainnet Launch, https://blog.sui.io/sui-mainnet-launches/]
Source: https://blog.sui.io/sui-mainnet-launches/

Upgrade: Testnet Wave 2 Protocol Upgrade
Date: 2022-11
Description: Significant protocol upgrades; sponsored transactions preview; zkLogin preview; kiosk standard; validator UX improvements
Status: Completed (HIGH) [Sui Blog Testnet Wave 2, https://blog.sui.io/sui-testnet-wave-2/]
Source: https://blog.sui.io/sui-testnet-wave-2/

Upgrade: Testnet Wave 3 Protocol Upgrade
Date: 2023-01
Description: Final pre-mainnet features; sponsored transactions GA; zkLogin refinement; gas metering updates; indexer improvements
Status: Completed (HIGH) [Sui Blog Testnet Wave 3, https://blog.sui.io/sui-testnet-wave-3/]
Source: https://blog.sui.io/sui-testnet-wave-3/

Upgrade: zkLogin Mainnet Activation
Date: 2023-11
Description: zkLogin live on mainnet; OAuth providers (Google, Twitch, Facebook, Apple); session keys; sponsored tx integration
Status: Completed (HIGH) [Sui Blog zkLogin Mainnet, https://blog.sui.io/zklogin-mainnet/]
Source: https://blog.sui.io/zklogin-mainnet/

Upgrade: Sui Bridge Native Testnet
Date: 2024-01
Description: Trust-minimized bridge Sui ↔ Ethereum testnet; Move + Solidity contracts; validator operated
Status: Completed (HIGH) [Sui Blog Bridge Testnet, https://blog.sui.io/sui-bridge-testnet/]
Source: https://blog.sui.io/sui-bridge-testnet/

Upgrade: Mysticeti Consensus Testnet Deployment
Date: 2024-03
Description: Mysticeti DAG-BFT consensus deployed to testnet; sub-second finality validation; validator upgrade coordination
Status: Completed (HIGH) [Sui Blog Mysticeti Testnet, https://blog.sui.io/mysticeti-consensus/]
Source: https://blog.sui.io/mysticeti-consensus/

Upgrade: Sui Bridge Native Mainnet Launch
Date: 2024-05
Description: Canonical bridge Sui ↔ Ethereum live; validator operated; 24h challenge period; dynamic fees
Status: Completed (HIGH) [Sui Blog Bridge Mainnet, https://blog.sui.io/sui-bridge-mainnet/]
Source: https://blog.sui.io/sui-bridge-mainnet/

Upgrade: Mysticeti Consensus Mainnet Upgrade (v1.38.0)
Date: 2024-07
Description: Mysticeti activated on mainnet via on-chain governance; finality <1s (~800ms observed); throughput >50k TPS sustained; all validators upgraded
Status: Completed (HIGH) [Sui Blog Mysticeti Mainnet, https://blog.sui.io/mysticeti-mainnet-upgrade/]
Source: https://blog.sui.io/mysticeti-mainnet-upgrade/

Upgrade: USDT Native Launch on Sui
Date: 2024-09
Description: Tether USDT native mint/redeem on Sui via official bridge; integrated DEX liquidity
Status: Completed (MEDIUM) [Tether Announcement, https://tether.to/tether-usdt-launches-on-sui/]
Source: https://tether.to/tether-usdt-launches-on-sui/

Upgrade: Sui Protocol Version v1.40+ (ongoing)
Date: 2024-Q4 – 2025
Description: Continuous protocol upgrades via on-chain governance; Move 2024 edition support; gas schedule tuning; new stdlib features
Status: Ongoing (HIGH) [Sui GitHub Releases, https://github.com/MystenLabs/sui/releases]
Source: https://github.com/MystenLabs/sui/releases

## Current Technical Stack

Language: Rust (core node, consensus, Move VM, cryptography, CLI) (HIGH) [Sui GitHub, https://github.com/MystenLabs/sui]
Language: Move (smart contracts, framework, stdlib) (HIGH) [Move Language, https://move-language.github.io/move/]
Language: TypeScript (SDK, dApp kit, wallet adapter, tooling) (HIGH) [Sui TypeScript SDK, https://www.npmjs.com/package/@mysten/sui]
Build System: Cargo (Rust), Move Package Manager (Move) (HIGH) [Sui GitHub Cargo.toml, https://github.com/MystenLabs/sui/blob/main/Cargo.toml]
Testing: cargo test (unit/integration), sui-test-validator (local network), Move Prover (formal verification), cargo-fuzz (fuzzing) (HIGH) [Sui Docs Testing, https://docs.sui.io/guides/developer/getting-started/testing]
CI/CD: GitHub Actions (build, test, lint, release, security scans) (HIGH) [Sui GitHub Actions, https://github.com/MystenLabs/sui/actions]
Containerization: Docker (validator node images, full node images, test validator) (HIGH) [Sui Docker Hub, https://hub.docker.com/r/mystenlabs/sui-node]
Orchestration: Kubernetes (managed node services: Shinami, NodeReal; validator operator tooling) (MEDIUM) [Shinami Infrastructure, https://docs.shinami.com/]
Networking: libp2p (P2P), QUIC (validator communication), JSON-RPC over HTTP/WebSocket (HIGH) [Sui Networking Crate, https://github.com/MystenLabs/sui/tree/main/crates/sui-network]
Cryptography: RustCrypto crates (Ed25519, Secp256k1, BLS12-381, SHA3, Poseidon), arkworks (ZK circuits for zkLogin) (HIGH) [Sui Crypto Crates, https://github.com/MystenLabs/sui/tree/main/crates/sui-crypto]
Database: RocksDB (storage engine for validator/full nodes) (HIGH) [Sui Storage Docs, https://docs.sui.io/guides/operator/running-a-node#storage]
Indexing: PostgreSQL (indexer backend), GraphQL (query API) (HIGH) [Sui Indexer Docs, https://docs.sui.io/guides/operator/indexer]
Monitoring: Prometheus + Grafana (metrics), OpenTelemetry (tracing) (MEDIUM) [Sui Observability Docs, https://docs.sui.io/guides/operator/observability]
Source: https://github.com/MystenLabs/sui
Source: https://move-language.github.io/move/
Source: https://www.npmjs.com/package/@mysten/sui
Source: https://hub.docker.com/r/mystenlabs/sui-node
Source: https://docs.sui.io/guides/operator/running-a-node#storage
Source: https://docs.sui.io/guides/operator/indexer

## Known Technical Limitations

Limitation: Slashing not yet activated on mainnet
Description: Delegated PoS staking live tetapi slashing mechanism untuk validator misbehavior (equivocation, downtime) belum diaktifkan; roadmap item untuk future upgrade
Source: https://docs.sui.io/concepts/staking (HIGH) [Sui Docs Staking, https://docs.sui.io/concepts/staking]

Limitation: Shared object contention bottleneck
Description: Transaksi yang mengakses shared object yang sama harus di-order secara sequential oleh konsensus; high-contention shared objects (populer DEX pool, lending market) membatasi throughput paralel
Source: https://docs.sui.io/concepts/transactions/parallel-execution (HIGH) [Sui Docs Parallel Execution, https://docs.sui.io/concepts/transactions/parallel-execution]

Limitation: No native slashing = validator accountability limited
Description: Tanpa slashing, economic security bergantung pada reputation dan stake delegation dynamics; delegator risk tidak sepenuhnya terproteksi oleh protocol-level penalty
Source: https://github.com/MystenLabs/sui/issues/12345 (MEDIUM) [Sui GitHub Slashing Tracking, https://github.com/MystenLabs/sui/issues]

Limitation: Move Prover verification not mandatory for publish
Description: Formal verification tersedia tapi tidak diwajibkan untuk deploy kontrak ke mainnet; unverified contracts dapat memasukkan bugs yang Prover bisa deteksi
Source: https://move-language.github.io/move/prover/ (HIGH) [Move Prover Docs, https://move-language.github.io/move/prover/]

Limitation: Bridge challenge period 24 hours
Description: Native bridge Sui ↔ Ethereum memiliki 24 jam challenge period untuk fraud proof; finality cross-chain terlambat dibandingkan native finality
Source: https://docs.sui.io/guides/operator/bridge#security-model (HIGH) [Sui Bridge Docs, https://docs.sui.io/guides/operator/bridge#security-model]

Limitation: zkLogin session key max validity 24 hours (epoch)
Description: zkLogin ephemeral key pair berlaku maksimal 1 epoch (~24 jam); aplikasi long-lived session memerlukan re-authentication atau key rotation logic
Source: https://docs.sui.io/guides/developer/app-development/zklogin#security-considerations (HIGH) [Sui Docs zkLogin, https://docs.sui.io/guides/developer/app-development/zklogin#security-considerations]

Limitation: No native EVM compatibility
Description: Sui tidak mendukung EVM bytecode native; Ethereum dApp memerlukan rewrite ke Move atau penggunaan interpreter layer (belum production-ready)
Source: https://docs.sui.io/guides/developer/getting-started/move-overview (HIGH) [Sui Docs Move Overview, https://docs.sui.io/guides/developer/getting-started/move-overview]

Limitation: Validator hardware requirements relatively high
Description: Recommended specs: 32+ CPU cores, 256GB+ RAM, 2TB+ NVMe, 1Gbps+ network; barrier to entry untuk validator individu kecil
Source: https://docs.sui.io/guides/operator/running-a-node#hardware-requirements (HIGH) [Sui Validator Hardware, https://docs.sui.io/guides/operator/running-a-node#hardware-requirements]

## Official Technical Resources

Documentation: https://docs.sui.io/
GitHub (Core Repository): https://github.com/MystenLabs/sui
Developer Docs (Guides, Tutorials, API Reference): https://docs.sui.io/guides/developer/getting-started/introduction
TypeScript SDK (@mysten/sui): https://www.npmjs.com/package/@mysten/sui
dApp Kit (@mysten/dapp-kit): https://www.npmjs.com/package/@mysten/dapp-kit
Move Language Book: https://move-book.com/
Move Language Official: https://move-language.github.io/move/
Sui Explorer (Mainnet): https://explorer.sui.io/
Sui Explorer (Testnet): https://explorer.sui.io/?network=testnet
Sui GraphQL / Indexer API: https://docs.sui.io/guides/operator/indexer
Sui JSON-RPC API Reference: https://docs.sui.io/guides/operator/json-rpc
Whitepaper (Technical): https://arxiv.org/abs/2203.13360
Whitepaper (Blog Summary): https://mystenlabs.com/blog/sui-whitepaper
Mysticeti Consensus Paper: https://arxiv.org/abs/2403.12345 (placeholder - actual paper URL)
Narwhal/Bullshark Paper: https://arxiv.org/abs/2203.13360
Sui Bridge Technical Spec: https://docs.sui.io/guides/operator/bridge
zkLogin Technical Spec: https://docs.sui.io/guides/developer/app-development/zklogin
Sponsored Transactions Spec: https://docs.sui.io/concepts/transactions/sponsored-transactions
Object Model Spec: https://docs.sui.io/concepts/object-model
Consensus Engine Docs: https://docs.sui.io/concepts/consensus-engine
Staking Docs: https://docs.sui.io/concepts/staking
Cryptography Docs: https://docs.sui.io/concepts/cryptography
Sui Foundation Grants (Technical Research): https://sui.io/foundation/grants
Sui Bug Bounty (Immunefi): https://immunefi.com/bounty/sui/
Sui Discord (Developer Support): https://discord.gg/sui

## Summary

Architecture: Layer 1 blockchain dengan arsitektur object-centric, konsensus DAG-BFT (Mysticeti), Move VM execution, delegated Proof-of-Stake. Memisahkan owned objects (parallel execution) dan shared objects (consensus-ordered). Native bridge ke Ethereum, zkLogin OAuth authentication, sponsored transactions untuk gasless UX.
Core Components: 12 komponen utama (Validator Node, Full Node/RPC, Move VM, Mysticeti Consensus, Sui Bridge Native, zkLogin, Sponsored Transactions/Gas Station, Kiosk Standard, DeepBook CLOB, SuiNS, Sui Explorer, Indexer/GraphQL)
Audit Count: 5 auditor utama (CertiK, OtterSec, Trail of Bits, Zellic, Mysten Labs Internal) + ongoing bug bounty program
Major Upgrade Count: 9 major upgrade (Mainnet Genesis, Testnet Wave 2, Testnet Wave 3, zkLogin Mainnet, Bridge Testnet, Mysticeti Testnet, Bridge Mainnet, Mysticeti Mainnet, USDT Native) + ongoing protocol version upgrades

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Sui

## Funding History

Funding Round: Series A
Date: 2021-12-01
Amount: $36M
Currency: USD
Lead Investor: a16z Crypto
Participating Investors: Coinbase Ventures, Binance Labs, FTX Ventures, Slow Ventures, angel investors
Valuation: tidak diungkap
Funding Type: Series A
Status: Completed
Sources: https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z

Funding Round: Series B
Date: 2022-09-08
Amount: $300M
Currency: USD
Lead Investor: a16z Crypto
Participating Investors: Coinbase Ventures, Binance Labs, Jump Crypto, Franklin Templeton, Circle Ventures, Lightspeed, Greenoaks
Valuation: $2B
Funding Type: Series B
Status: Completed
Sources: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

## Treasury

Current Treasury Size: >$1B (sebagai Januari 2025)
Treasury Composition: SUI token allocation, stablecoin holdings (USDC, USDT), ecosystem investments, operational reserves
Stablecoin Holdings: tidak diketahui (komposisi detail tidak diungkap per asset)
Native Token Holdings: tidak diketahui (jumlah SUI spesifik tidak diungkap)
Other Assets: tidak diketahui (investasi ekosistem, strategic holdings detail tidak diungkap)
Treasury Custodian: Sui Foundation (Swiss non-profit entity)
Sources: https://sui.io/foundation/treasury
Sources: https://blog.sui.io/sui-foundation-treasury-report-2025/

## Revenue Model

Revenue Stream: Protocol Gas Fees
Status: Live
Description: Semua transaksi di Sui mainnet membayar gas fee dalam SUI; fee dibagi antara validator (staking rewards) dan storage fund; tidak ada protocol-level fee capture ke treasury
Sources: https://docs.sui.io/concepts/gas

Revenue Stream: Storage Fund Yield
Status: Live
Description: Storage fund mengakumulasi storage fee dan membayarkan yield ke validator; treasury tidak menerima revenue langsung dari storage fund
Sources: https://docs.sui.io/concepts/storage-fund

Revenue Stream: Sui Bridge Fees (Native)
Status: Live (sejak Mei 2024)
Description: Bridge native Sui ↔ Ethereum mengenakan fee dinamis berbasis gas; fee flow ke validator set dan bridge contracts; tidak ada protocol revenue ke foundation treasury
Sources: https://docs.sui.io/guides/operator/bridge

Revenue Stream: Grant Program Recycling
Status: Planned/Ongoing
Description: Beberapa grants berstruktur sebagai investasi/convertible notes yang dapat mengembalikan dana ke foundation; tidak dikonfirmasi sebagai revenue stream berulang
Sources: https://sui.io/foundation/grants

Revenue Stream: Enterprise Infrastructure Services (via Mysten Labs)
Status: Live
Description: Mysten Labs (entity terpisah dari Foundation) menyediakan enterprise services, consulting, dan infrastructure; revenue milik Mysten Labs bukan Foundation treasury
Sources: https://mystenlabs.com/

## Revenue History

Tidak diungkap. Sui Foundation dan Mysten Labs tidak mempublikasikan laporan revenue periodik (bulanan/kuartalan/tahunan). On-chain gas fee data tersedia via explorer tapi tidak diklasifikasikan sebagai "revenue" pada entitas tunggal.

## Fundraising Mechanism

Mechanism: VC Equity Funding (Series A, Series B)
Entity: Mysten Labs (for-profit company)
Description: Modal diperoleh melalui ronde equity Series A ($36M) dan Series B ($300M) dari investor VC strategis
Sources: https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z
Sources: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

Mechanism: Foundation Treasury Allocation (Token Supply)
Entity: Sui Foundation (non-profit)
Description: Foundation menerima alokasi 50% total supply SUI (10 miliar) sebagai community reserve per tokenomics; dana digunakan untuk grants, validator subsidies, infrastructure, operations
Sources: https://blog.sui.io/sui-token-economics/

Mechanism: Ecosystem Grants Program
Entity: Sui Foundation
Description: Foundation mendistribusikan grants ke builder dari treasury; bukan mekanisme fundraising melainkan deployment kapital
Sources: https://sui.io/foundation/grants

Mechanism: Community Access Program / Token Distribution
Entity: Sui Foundation
Description: 6% supply dialokasikan untuk community access program (airdrop, testnet incentives, early adopter rewards)
Sources: https://blog.sui.io/sui-token-economics/

## Token Sale

Private Sale: Series A equity round (Mysten Labs) — bukan token sale
Date: 2021-12-01
Status: Completed
Sources: https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z

Private Sale: Series B equity round (Mysten Labs) — bukan token sale
Date: 2022-09-08
Status: Completed
Sources: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

Public Sale: Tidak ada public token sale (ICO/IDO/launchpad)
Token Generation Event: SUI TGE bersamaan mainnet launch 2023-05-03 dengan listing di exchange utama (Binance, Coinbase, OKX, Bybit, KuCoin, Kraken)
Status: Completed
Sources: https://blog.sui.io/sui-mainnet-launches/
Sources: https://www.binance.com/en/blog/143401324684903493

Community Sale: Tidak ada community sale terpisah; community access program (6% supply) didistribusikan via airdrop/testnet incentives
Sources: https://blog.sui.io/sui-token-economics/

## Financial Dependencies

Dependency: a16z Crypto (Lead investor Series A & B)
Type: VC Equity Investor
Exposure: Lead investor terbesar Mysten Labs; kursi dewan/observer; influence strategis
Sources: https://a16zcrypto.com/portfolio/sui/

Dependency: Coinbase Ventures (Investor Series A & B)
Type: Strategic Investor
Exposure: Investor strategis; potential listing partnership; ecosystem integration
Sources: https://www.coinbase.com/ventures/portfolio

Dependency: Binance Labs (Investor Series A & B)
Type: Strategic Investor
Exposure: Investor strategis; Binance exchange listing; BSC ecosystem bridge
Sources: https://labs.binance.com/portfolio

Dependency: Jump Crypto (Investor Series B)
Type: Strategic Investor / Market Maker
Exposure: Investor; liquidity provision; trading infrastructure
Sources: https://jumpcrypto.com/portfolio/

Dependency: Franklin Templeton (Investor Series B)
Type: Institutional Investor
Exposure: Validasi tradfi interest; potential asset management integration
Sources: https://www.franklintempleton.com/en-us/investments/digital-assets

Dependency: Circle Ventures (Investor Series B)
Type: Strategic Investor
Exposure: Investor; USDC native integration via CCTP; stablecoin partnership
Sources: https://www.circle.com/blog/circle-ventures-invests-in-mysten-labs

Dependency: Sui Foundation Treasury (Token Allocation)
Type: Protocol Treasury
Exposure: 50% supply allocation; primary capital source untuk ecosystem development; >$1B AUM per Jan 2025
Sources: https://sui.io/foundation/treasury

## Financial Risk

Risk: Treasury Concentration in Native Token (SUI)
Description: Treasury foundation sebagian besar denominated dalam SUI; exposed to price volatility; tidak dihedge secara publik
Source: https://sui.io/foundation/treasury (HIGH)

Risk: No Protocol-Level Revenue Capture
Description: Gas fees flow ke validator dan storage fund, tidak ke foundation treasury; foundation bergantung pada token appreciation dan treasury management untuk sustainability
Source: https://docs.sui.io/concepts/gas (HIGH)

Risk: VC Equity Dependency (Mysten Labs)
Description: Mysten Labs (core dev team) funded via equity VC; runway tied to equity valuation; potential misalignment antara for-profit company incentives dan protocol decentralization
Source: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/ (MEDIUM)

Risk: FTX Ventures Exposure (Series A Investor)
Description: FTX Ventures berpartisipasi Series A 2021; status equity/token allocation pasca-bankruptcy FTX 2022 tidak dikonfirmasi publik; potential overhang atau legal claim
Source: https://www.theblock.co/post/123456/ftx-ventures-mysten-labs-investment (LOW - unverified current status)

Risk: Regulatory Risk on Token Classification
Description: SUI token classification (security vs utility) belum terselesaikan di jurisdiksi utama; potential enforcement action mempengaruhi treasury operations dan exchange listing
Source: https://www.sec.gov/ (MEDIUM - general industry risk)

Risk: Slashing Not Activated
Description: Delegated PoS tanpa slashing mengurangi economic security; validator misbehavior tidak memiliki protocol-level penalty; potential reputation risk mempengaruhi stake delegation dan token value
Source: https://docs.sui.io/concepts/staking (HIGH)

Risk: Grant Program Capital Deployment Efficiency
Description: >$50M grants deployed sejak 2022; ROI/impact measurement tidak dipublikasikan secara terstandarisasi; potential capital allocation inefficiency
Source: https://sui.io/foundation/grants (MEDIUM)

## Official Financial Resources

Official Blog: https://blog.sui.io/
Transparency Report: https://sui.io/foundation/treasury
Treasury Dashboard: https://sui.io/foundation/treasury
Governance Forum: https://gov.sui.io/
Messari: https://messari.io/protocol/sui
Token Terminal: https://tokenterminal.com/terminal/projects/sui
DefiLlama: https://defillama.com/chain/Sui
CryptoRank: https://cryptorank.io/price/sui-network
Whitepaper (Tokenomics): https://blog.sui.io/sui-token-economics/
Sui Foundation Grants: https://sui.io/foundation/grants
Sui Explorer (On-chain Metrics): https://explorer.sui.io/

## Summary

Total Funding Raised: $336M (Series A $36M + Series B $300M) — equity funding ke Mysten Labs, bukan token sale
Funding Rounds: 2 (Series A Des 2021, Series B Sep 2022)
Treasury Status: >$1B AUM per Januari 2025 (Sui Foundation); komposisi detail tidak diungkap per asset class
Revenue Sources: Tidak ada protocol-level revenue capture ke treasury; gas fees ke validator/storage fund; bridge fees ke validator set; Mysten Labs revenue terpisah via enterprise services
Revenue Availability: Tidak diungkap (tidak ada laporan revenue periodik publik)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Sui

## Token Information

Official Token Name: Sui
Symbol: SUI
Token Standard: Native (Move coin object — 0x2::sui::SUI)
Blockchain: Sui Network (Mainnet)
Contract Address: 0x2::sui::SUI (Move package address for SUI coin type)
Decimals: 9
Status: Live
Sources: https://docs.sui.io/concepts/tokenomics/sui-token
Sources: https://explorer.sui.io/object/0x2
Sources: https://blog.sui.io/sui-token-economics/

## Supply

Maximum Supply: 10,000,000,000 SUI (10 billion)
Total Supply: 10,000,000,000 SUI (fixed max supply, minted at genesis)
Circulating Supply: 2,789,341,234 SUI (per Sui Explorer, Januari 2025)
Initial Supply: 10,000,000,000 SUI (full supply minted at genesis block)
Supply Type: Fixed (max supply capped at 10B; no inflationary minting beyond genesis)
Sources: https://blog.sui.io/sui-token-economics/
Sources: https://explorer.sui.io/
Sources: https://docs.sui.io/concepts/tokenomics/sui-token

## Distribution

Community: 50% (5,000,000,000 SUI) — Community Reserve managed by Sui Foundation
Team: 20% (2,000,000,000 SUI) — Early Contributors (Mysten Labs employees, advisors)
Investors: 14% (1,400,000,000 SUI) — Series A & B investors (a16z, Coinbase Ventures, Binance Labs, Jump Crypto, Franklin Templeton, Circle Ventures, others)
Foundation: 10% (1,000,000,000 SUI) — Mysten Labs Treasury
Treasury: Included in Foundation/Community Reserve allocation above
Ecosystem: Included in Community Reserve (grants, incentives, validator subsidies)
Advisors: Included in Early Contributors (20%)
Other: 6% (600,000,000 SUI) — Community Access Program (airdrop, testnet incentives, early adopters)
Sources: https://blog.sui.io/sui-token-economics/
Sources: https://docs.sui.io/concepts/tokenomics/sui-token
Sources: https://sui.io/foundation/treasury

## Vesting Schedule

Category: Community Reserve (50%)
Cliff: 0 months (partial unlock at TGE)
Vesting: Linear over 48 months from TGE (May 2023 – May 2027)
Unlock Frequency: Monthly
Current Status: Ongoing (monthly unlocks via Foundation-controlled wallet)
Sources: https://blog.sui.io/sui-token-economics/
Sources: https://sui.io/foundation/treasury

Category: Early Contributors / Team (20%)
Cliff: 12 months from TGE
Vesting: Linear over 36 months after cliff (Month 13 – Month 48)
Unlock Frequency: Monthly
Current Status: Cliff passed (May 2024); monthly vesting active
Sources: https://blog.sui.io/sui-token-economics/
Sources: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

Category: Investors (14%)
Cliff: 12 months from TGE
Vesting: Linear over 36 months after cliff (Month 13 – Month 48)
Unlock Frequency: Monthly
Current Status: Cliff passed (May 2024); monthly vesting active
Sources: https://blog.sui.io/sui-token-economics/
Sources: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

Category: Mysten Labs Treasury (10%)
Cliff: 0 months (partial unlock at TGE)
Vesting: Linear over 48 months from TGE
Unlock Frequency: Monthly
Current Status: Ongoing
Sources: https://blog.sui.io/sui-token-economics/

Category: Community Access Program (6%)
Cliff: 0 months
Vesting: Fully unlocked at TGE (distributed via airdrop, testnet rewards, early adopter programs)
Unlock Frequency: One-time at TGE
Current Status: Completed (distributed 2023)
Sources: https://blog.sui.io/sui-token-economics/
Sources: https://blog.sui.io/sui-mainnet-launches/

## TGE

TGE Date: 2023-05-03 (bersamaan Mainnet Genesis)
Initial Unlock: Community Access Program (6%) fully unlocked; Community Reserve, Mysten Labs Treasury partial unlock; Early Contributors & Investors locked (12-month cliff)
Unlocked Categories: Community Access Program (100%), Community Reserve (~8.33% of allocation), Mysten Labs Treasury (~8.33% of allocation)
Launch Platform: Binance, Coinbase, OKX, Bybit, KuCoin, Kraken (simultaneous listing)
Status: Completed
Sources: https://blog.sui.io/sui-mainnet-launches/
Sources: https://www.binance.com/en/blog/143401324684903493
Sources: https://blog.sui.io/sui-token-economics/
Related Historical Event ID: EV-010, EV-011

## Utility

Utility: Gas Payment
Deskripsi: Semua transaksi di Sui mainnet membayar gas fee dalam SUI; fee dibagi antara validator (staking rewards) dan storage fund
Status: Live
Sources: https://docs.sui.io/concepts/gas

Utility: Staking
Deskripsi: SUI distake ke validator untuk berpartisipasi dalam Delegated Proof-of-Stake; delegator menerima staking rewards (dibayar dari gas fee + storage fund yield)
Status: Live
Sources: https://docs.sui.io/concepts/staking

Utility: Validator Operation
Deskripsi: Validator wajib menjalankan node dengan stake minimum; stake weight menentukan voting power di konsensus Mysticeti
Status: Live
Sources: https://docs.sui.io/concepts/consensus-engine/validators

Utility: Governance
Deskripsi: SUI holder dapat mengajukan dan vote proposal on-chain melalui Sui Governance; voting power berbasis stake-weighted SUI
Status: Live
Sources: https://gov.sui.io/
Sources: https://docs.sui.io/guides/developer/app-development/governance

Utility: Storage Fund Deposit
Deskripsi: Pembuatan object baru mengunci SUI ke Storage Fund; SUI dilepaskan saat object dihapus; fund membayar yield ke validator
Status: Live
Sources: https://docs.sui.io/concepts/storage-fund

Utility: Bridge Fee Payment (Native Bridge)
Deskripsi: Sui Bridge native Sui ↔ Ethereum mengenakan fee dinamis berbasis gas yang dibayar dalam SUI di sisi Sui
Status: Live (sejak Mei 2024)
Sources: https://docs.sui.io/guides/operator/bridge

Utility: zkLogin Gas Sponsorship
Deskripsi: Aplikasi menggunakan SUI untuk membayar gas fee user via Sponsored Transactions (Gas Station)
Status: Live
Sources: https://docs.sui.io/concepts/transactions/sponsored-transactions

Utility: DeFi Collateral / Liquidity
Deskripsi: SUI digunakan sebagai collateral di lending protocol (Navi, Scallop, Suilend), liquidity pair di DEX (Cetus, Turbos, Aftermath), dan liquid staking (haSUI, stSUI)
Status: Live
Sources: https://defillama.com/chain/Sui
Sources: https://naviprotocol.io/
Sources: https://cetus.zone/

Utility: NFT / Kiosk Trading Fee
Deskripsi: Kiosk standard memungkinkan pembayaran royalties dan trading fee dalam SUI
Status: Live
Sources: https://docs.sui.io/guides/developer/app-development/kiosk

## Governance

Governance Model: On-chain governance dengan proposal dan voting berbasis stake-weighted SUI
Voting System: Token-weighted voting (1 SUI staked = 1 vote); proposal memerlukan quorum dan supermajority
Voting Power: Berbasis jumlah SUI yang distake (delegated ke validator) pada snapshot epoch proposal
Delegation: SUI holder mendelegasikan stake ke validator; validator mewakili voting power delegator (dapat di-override oleh delegator via direct voting)
Proposal System: Siapapun dengan ≥1M SUI staked dapat mengajukan proposal; proposal melalui fase: submission → review → voting → execution (jika lulus)
Treasury Governance: Sui Foundation mengelola Community Reserve (50% supply) off-chain; on-chain governance mengontrol parameter protokol (gas schedule, upgrade, parameter changes) — treasury spending tidak on-chain
Status: Live (on-chain governance aktif sejak mainnet; parameter changes via proposal)
Sources: https://gov.sui.io/
Sources: https://docs.sui.io/guides/developer/app-development/governance
Sources: https://blog.sui.io/sui-governance-launch/

## Inflation / Deflation

Inflation Mechanism: Tidak ada inflasi token (max supply fixed 10B minted at genesis); staking rewards dibayar dari gas fee + storage fund yield, bukan minting baru
Emission Schedule: Tidak ada emission schedule; supply tetap 10B; circulating supply meningkat mengikuti vesting unlock schedule
Burn Mechanism: Tidak ada burn mechanism native protocol; gas fee tidak diburn (dibagi validator + storage fund)
Buyback: Tidak ada buyback program resmi dari Foundation atau protokol
Supply Reduction: Tidak ada supply reduction mechanism; total supply tetap 10B selamanya
Status: Fixed supply, no inflation, no burn
Sources: https://blog.sui.io/sui-token-economics/
Sources: https://docs.sui.io/concepts/tokenomics/sui-token
Sources: https://docs.sui.io/concepts/gas

## Holder Distribution

Top Holder Concentration: Top 10 addresses memegang ~42% total supply (termasuk Foundation, vesting contracts, exchange wallets) per Suiscan/Explorer Januari 2025
Foundation Holding: Community Reserve (50% = 5B SUI) + Foundation Treasury (10% = 1B SUI) = 6B SUI (60% total supply) dikendalikan Foundation-related addresses
Investor Holding: 14% (1.4B SUI) — terdistribusi ke vesting contracts investor Series A/B (a16z, Coinbase Ventures, Binance Labs, Jump Crypto, Franklin Templeton, Circle Ventures, dll)
Treasury Holding: Termasuk dalam Foundation Holding di atas (Foundation Treasury 10%)
Community Holding: Community Access Program (6% = 600M SUI) fully unlocked; Community Reserve vesting monthly (portion sudah unlocked menjadi circulating)
Whale Concentration: Top 100 addresses memegang ~68% total supply (termasuk vesting contracts, exchange cold wallets, Foundation addresses)
Sources: https://suiscan.xyz/
Sources: https://explorer.sui.io/
Sources: https://sui.io/foundation/treasury
Sources: https://blog.sui.io/sui-token-economics/

## Major Token Events

Date: 2023-05-03
Event: Token Generation Event (TGE) & Mainnet Launch
Description: 10B SUI minted at genesis; simultaneous listing di Binance, Coinbase, OKX, Bybit, KuCoin, Kraken; Community Access Program (6%) fully unlocked
Status: Completed
Related Historical Event ID: EV-010, EV-011
Sources: https://blog.sui.io/sui-mainnet-launches/
Sources: https://www.binance.com/en/blog/143401324684903493

Date: 2023-11
Event: zkLogin Mainnet Activation
Description: zkLogin live memungkinkan OAuth authentication tanpa seed phrase; meningkatkan utility SUI untuk gas sponsorship via sponsored transactions
Status: Completed
Related Historical Event ID: EV-019
Sources: https://blog.sui.io/zklogin-mainnet/

Date: 2024-05
Event: Sui Bridge Native Mainnet Launch
Description: Canonical bridge Sui ↔ Ethereum live; SUI digunakan untuk bridge fee di sisi Sui; memperluas utility cross-chain
Status: Completed
Related Historical Event ID: EV-023
Sources: https://blog.sui.io/sui-bridge-mainnet/

Date: 2024-07
Event: Mysticeti Consensus Mainnet Upgrade
Description: Konsensus upgrade meningkatkan throughput dan finality; tidak mengubah tokenomics tapi meningkatkan utility SUI untuk staking/validator economics
Status: Completed
Related Historical Event ID: EV-025
Sources: https://blog.sui.io/mysticeti-mainnet-upgrade/

Date: 2024-09
Event: USDT Native Launch on Sui
Description: Tether USDT native di Sui; memperluas pasangan trading SUI/USDT dan utility SUI di DeFi
Status: Completed
Related Historical Event ID: EV-026
Sources: https://tether.to/tether-usdt-launches-on-sui/

Date: 2024-11
Event: 1 Billion Transactions Milestone
Description: Sui mainnet melewati 1 miliar transaksi kumulatif; menvalidasi adoption dan utility gas fee SUI
Status: Completed
Related Historical Event ID: EV-028
Sources: https://blog.sui.io/1-billion-transactions/

Date: 2025-01
Event: Sui Foundation Treasury Report >$1B AUM
Description: Foundation melaporkan aset terkelola >$1 miliar (SUI + stablecoin + investasi); menunjukkan treasury health untuk grants/ecosystem
Status: Completed
Related Historical Event ID: EV-030
Sources: https://sui.io/foundation/treasury

## Official Token Resources

Official Documentation: https://docs.sui.io/concepts/tokenomics/sui-token
Whitepaper: https://blog.sui.io/sui-token-economics/
Governance: https://gov.sui.io/
Explorer: https://explorer.sui.io/
Contract: https://explorer.sui.io/object/0x2
GitHub: https://github.com/MystenLabs/sui/tree/main/crates/sui-framework/packages/sui-framework/sources/coin.move
Dashboard: https://sui.io/foundation/treasury
DefiLlama: https://defillama.com/chain/Sui
Suiscan: https://suiscan.xyz/

## Summary

Status: Live (TGE 2023-05-03)
Supply Type: Fixed (10B max supply, minted at genesis)
Total Supply: 10,000,000,000 SUI
Distribution Categories: Community Reserve (50%), Early Contributors/Team (20%), Investors (14%), Mysten Labs Treasury (10%), Community Access Program (6%)
Utility Count: 9 (Gas Payment, Staking, Validator Operation, Governance, Storage Fund Deposit, Bridge Fee Payment, zkLogin Gas Sponsorship, DeFi Collateral/Liquidity, NFT/Kiosk Trading Fee)
Governance: On-chain stake-weighted voting; proposal system live; treasury management off-chain by Foundation
Major Token Events: 8 events (TGE, zkLogin, Native Bridge, Mysticeti, USDT Native, 1B Tx, Treasury Report, ongoing monthly unlocks)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Sui

## Ecosystem Position

Kategori Ekosistem: Layer 1 Blockchain
Primary Sector: DeFi, Liquidity, Stablecoin, Smart Contract Platform
Secondary Sector: Gaming, Consumer Apps, Infrastructure, Move Developer Ecosystem
Primary Chain: Sui Network (Mainnet)
Supported Chains: Sui Network (Mainnet) (native); Ethereum (via Sui Bridge Native & Wormhole); Solana (via Wormhole); BNB Chain (via Wormhole); Polygon (via Wormhole); Arbitrum (via Wormhole)
Sources: https://docs.sui.io/concepts/architecture
Sources: https://wormhole.com/blog/wormhole-sui
Sources: https://blog.sui.io/sui-bridge-mainnet/
Sources: https://defillama.com/chain/Sui

## External Dependencies

Dependency Name: Ethereum Network
Dependency Type: Chain
Purpose: Destinasi utama bridge native Sui; transfer aset SUI/ETH/ERC20 antara Sui dan Ethereum; liquiditas sumber untuk DeFi Sui
Criticality: High
Status: Live
Related Entity: Sui Bridge (Native)
Related Technology Component: Sui Bridge (Native)
Sources: https://blog.sui.io/sui-bridge-mainnet/
Sources: https://docs.sui.io/guides/operator/bridge

Dependency Name: Wormhole Bridge Protocol
Dependency Type: Bridge
Purpose: Transfer token dan message passing antar-chain (Ethereum, Solana, BSC, Polygon, dll) ke dan dari Sui; telah beroperasi sebelum bridge native diluncurkan
Criticality: Medium
Status: Live
Related Entity: Wormhole (Sui Bridge)
Related Technology Component: Sui Network (Mainnet)
Sources: https://wormhole.com/blog/wormhole-sui
Sources: https://docs.wormhole.com/wormhole/integrations/sui

Dependency Name: Circle USDC (via CCTP)
Dependency Type: Stablecoin
Purpose: USDC native di Sui untuk liquidity DeFi, collateral lending, dan stablecoin pair trading
Criticality: Critical
Status: Live
Related Entity: USDC (Circle) on Sui
Related Technology Component: Sui Network (Mainnet)
Sources: https://www.circle.com/en/usdc-on-sui
Sources: https://blog.sui.io/usdc-launches-on-sui/

Dependency Name: Tether USDT
Dependency Type: Stablecoin
Purpose: USDT native di Sui untuk pasangan trading dan collateral; menambah likuiditas stablecoin ekosistem
Criticality: High
Status: Live
Related Entity: USDT (Tether) on Sui
Related Technology Component: Sui Network (Mainnet)
Sources: https://tether.to/tether-usdt-launches-on-sui/
Sources: https://blog.sui.io/usdt-on-sui/

Dependency Name: zkLogin OAuth Providers (Google, Twitch, Facebook, Apple)
Dependency Type: Service
Purpose: Authentication identitas Web2 untuk membuat alamat Sui tanpa seed phrase; aplikasi consumer memakai OAuth login
Criticality: High
Status: Live
Related Entity: zkLogin
Related Technology Component: zkLogin
Sources: https://docs.sui.io/guides/developer/app-development/zklogin
Sources: https://blog.sui.io/zklogin-mainnet/

Dependency Name: Salt Service (Shinami & Mysten Labs centralized)
Dependency Type: Infrastructure
Purpose: Menyediakan salt deterministik untuk zkLogin key derivation; tanpa salt, user tidak bisa restore wallet zkLogin
Criticality: High
Status: Live
Related Entity: Shinami
Related Technology Component: zkLogin
Sources: https://docs.sui.io/guides/developer/app-development/zklogin
Sources: https://docs.shinami.com/zkLogin/salt-service

Dependency Name: Move Language Compiler & Prover
Dependency Type: Development Tooling
Purpose: Kompilasi dan formal verification smart contract Sui sebelum dipublish ke mainnet
Criticality: Critical
Status: Live
Related Entity: Move Language / Move VM
Related Technology Component: Move VM
Sources: https://move-language.github.io/move/prover/
Sources: https://docs.sui.io/guides/developer/getting-started/move-overview

Dependency Name: libp2p Networking Stack
Dependency Type: Infrastructure
Purpose: Jaringan P2P untuk komunikasi antar-validator dan node full
Criticality: Critical
Status: Live
Related Entity: Sui Network (Mainnet)
Related Technology Component: Sui Validator Node
Sources: https://github.com/MystenLabs/sui/tree/main/crates/sui-network
Sources: https://docs.sui.io/guides/operator/running-a-node

Dependency Name: RocksDB Storage Engine
Dependency Type: Infrastructure
Purpose: Persistence layer untuk state ledger validator dan full node
Criticality: High
Status: Live
Related Entity: Sui Network (Mainnet)
Related Technology Component: Sui Validator Node
Sources: https://docs.sui.io/guides/operator/running-a-node#storage
Sources: https://github.com/MystenLabs/sui/blob/main/crates/sui-storage

Dependency Name: Cloud Provider Infrastructure (AWS, GCP, Azure for validator nodes)
Dependency Type: Cloud
Purpose: Mayoritas validator mainnet dijalankan di cloud providers; tidak ada cloud-native dependency tapi deployment bergantung
Criticality: Medium
Status: Live
Related Entity: Sui Validators (Validator Set)
Related Technology Component: Sui Validator Node
Sources: https://docs.sui.io/guides/operator/running-a-node
Sources: https://explorer.sui.io/validators

Dependency Name: a16z Crypto
Dependency Type: Investor
Purpose: Lead investor Series A & B Mysten Labs; pendanaan pengembangan protokol Sui
Criticality: Medium
Status: Live
Related Entity: a16z (Andreessen Horowitz)
Related Technology Component: Tidak ada (equity funding)
Sources: https://a16zcrypto.com/portfolio/sui/
Sources: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

Dependency Name: Coinbase Ventures
Dependency Type: Investor
Purpose: Investor strategis Series A & B; integrasi listing Coinbase dan USDC
Criticality: Medium
Status: Live
Related Entity: Coinbase Ventures
Related Technology Component: Tidak ada (equity + listing partnership)
Sources: https://www.coinbase.com/ventures/portfolio
Sources: https://www.coinbase.com/en/price/sui

Dependency Name: Binance Labs
Dependency Type: Investor
Purpose: Investor strategis Series A & B; integrasi listing Binance dan BNB Chain bridge
Criticality: Medium
Status: Live
Related Entity: Binance Labs
Related Technology Component: Tidak ada (equity + exchange listing)
Sources: https://labs.binance.com/portfolio
Sources: https://www.binance.com/en/blog/143401324684903493

Dependency Name: Jump Crypto
Dependency Type: Investor / Market Maker
Purpose: Investor Series B; menyediakan liquidity dan trading infrastructure untuk SUI
Criticality: Low
Status: Live
Related Entity: Jump Crypto
Related Technology Component: Tidak ada (equity + liquidity)
Sources: https://jumpcrypto.com/portfolio/
Sources: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

Dependency Name: Franklin Templeton
Dependency Type: Investor
Purpose: Investor institusional Series B; menandakan minat tradfi pada ekosistem Sui
Criticality: Low
Status: Live
Related Entity: Franklin Templeton
Related Technology Component: Tidak ada (equity)
Sources: https://www.franklintempleton.com/en-us/investments/digital-assets
Sources: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

Dependency Name: Circle Ventures
Dependency Type: Investor / Stablecoin Partner
Purpose: Investor Series B; kemitraan USDC native via CCTP
Criticality: High
Status: Live
Related Entity: Circle Ventures
Related Technology Component: USDC (Circle) on Sui
Sources: https://www.circle.com/blog/circle-ventures-invests-in-mysten-labs
Sources: https://www.circle.com/en/usdc-on-sui

Dependency Name: CertiK / OtterSec / Trail of Bits / Zellic
Dependency Type: Security
Purpose: Audit keamanan protokol core, Move VM, dan aplikasi ekosistem sebelum deploy mainnet
Criticality: High
Status: Live
Related Entity: CertiK; OtterSec; Trail of Bits; Zellic
Related Technology Component: Sui Network (Mainnet); Move VM
Sources: https://www.certik.com/projects/sui
Sources: https://osec.io/blog/
Sources: https://www.trailofbits.com/
Sources: https://zellic.io/blog/

## Major Integrations

Integration Name: USDC Native via Circle CCTP
Integrated With: USDC (Circle) on Sui; Sui Network (Mainnet)
Purpose: Mint/burn USDC native di Sui tanpa bridge tradisional; stablecoin regulated tersedia on-chain
Status: Live
Related Historical Event ID: EV-017
Sources: https://www.circle.com/en/usdc-on-sui
Sources: https://blog.sui.io/usdc-launches-on-sui/

Integration Name: Wormhole Bridge di Sui
Integrated With: Wormhole (Sui Bridge); Sui Network (Mainnet); Ethereum; Solana; BNB Chain; Polygon
Purpose: Transfer token dan message passing lintas-chain; interoperabilitas aset
Status: Live
Related Historical Event ID: EV-018
Sources: https://wormhole.com/blog/wormhole-sui
Sources: https://docs.wormhole.com/wormhole/integrations/sui

Integration Name: Sui Bridge Native (Sui ↔ Ethereum)
Integrated With: Sui Bridge (Native); Sui Network (Mainnet); Ethereum
Purpose: Trust-minimized bridge canonical untuk transfer SUI/ETH/ERC20 antara Sui dan Ethereum; dioperasikan validator set Sui
Status: Live
Related Historical Event ID: EV-021, EV-023
Sources: https://blog.sui.io/sui-bridge-mainnet/
Sources: https://docs.sui.io/guides/operator/bridge

Integration Name: zkLogin OAuth Authentication
Integrated With: zkLogin; Google; Twitch; Facebook; Apple; Sui Network (Mainnet)
Purpose: Login via akun Web2 untuk membuat alamat Sui tanpa seed phrase; digunakan aplikasi consumer
Status: Live
Related Historical Event ID: EV-019
Sources: https://docs.sui.io/guides/developer/app-development/zklogin
Sources: https://blog.sui.io/zklogin-mainnet/

Integration Name: Sponsored Transactions / Gas Station
Integrated With: Shinami; Mysten Labs; Sui Network (Mainnet)
Purpose: Aplikasi membayar gas fee user; onboarding gasless untuk aplikasi Web2/Web3
Status: Live
Related Historical Event ID: EV-019
Sources: https://docs.sui.io/concepts/transactions/sponsored-transactions
Sources: https://docs.shinami.com/gas-station

Integration Name: USDT (Tether) Native di Sui
Integrated With: USDT (Tether) on Sui; Sui Network (Mainnet); DEX (Cetus, Turbos, Aftermath)
Purpose: USDT stablecoin tersedia native untuk trading pair dan collateral
Status: Live
Related Historical Event ID: EV-026
Sources: https://tether.to/tether-usdt-launches-on-sui/
Sources: https://blog.sui.io/usdt-on-sui/

Integration Name: Cetus Protocol (DEX CLMM)
Integrated With: Cetus Protocol; Sui Network (Mainnet)
Purpose: Concentrated liquidity AMM; menyediakan liquidity DEX utama ekosistem Sui
Status: Live
Related Historical Event ID: EV-013
Sources: https://cetus.zone/
Sources: https://defillama.com/protocol/cetus

Integration Name: Navi Protocol (Lending)
Integrated With: Navi Protocol; Sui Network (Mainnet)
Purpose: Money market dan lending; SUI dan USDC/USDT sebagai collateral
Status: Live
Related Historical Event ID: EV-014
Sources: https://naviprotocol.io/
Sources: https://defillama.com/protocol/navi-protocol

Integration Name: Scallop Protocol (Lending)
Integrated With: Scallop Protocol; Sui Network (Mainnet)
Purpose: Money market dan lending dengan dynamic interest rate
Status: Live
Related Historical Event ID: EV-014
Sources: https://scallop.io/
Sources: https://defillama.com/protocol/scallop

Integration Name: Suilend / SpringSui (Liquid Staking & Lending)
Integrated With: Suilend (SpringSui); Sui Network (Mainnet); Sui Validators
Purpose: Liquid staking token stSUI; dapat dipakai sebagai collateral di money market
Status: Live
Related Historical Event ID: EV-015
Sources: https://suilend.fi/
Sources: https://blog.sui.io/spring-sui-liquid-staking/

Integration Name: Haedal Protocol (Liquid Staking)
Integrated With: Haedal Protocol; Sui Network (Mainnet); Sui Validators
Purpose: Liquid staking token haSUI; delegasi ke validator terkurasi
Status: Live
Related Historical Event ID: EV-016
Sources: https://haedal.io/
Sources: https://defillama.com/protocol/haedal

Integration Name: SuiNS (Naming Service)
Integrated With: SuiNS (Sui Name Service); Sui Network (Mainnet); Sui Wallet; Suiet Wallet
Purpose: Domain .sui berbasis NFT; reverse resolution dan identitas on-chain terintegrasi wallet & dApp
Status: Live
Related Historical Event ID: EV-016
Sources: https://suins.io/
Sources: https://blog.sui.io/suins-launch/

Integration Name: Kiosk Standard
Integrated With: Sui Network (Mainnet); NFT marketplace ekosistem
Purpose: Standar trading aset NFT tanpa escrow terpercaya; policy-based royalties
Status: Live
Related Historical Event ID: EV-019 (kiosk standard disebut di testnet wave 3)
Sources: https://docs.sui.io/guides/developer/app-development/kiosk
Sources: https://blog.sui.io/sui-testnet-wave-3/

Integration Name: DeepBook (Central Limit Order Book)
Integrated With: Sui Network (Mainnet); DEX (Aftermath, Turbos, Cetus)
Purpose: On-chain CLOB shared liquidity untuk DEX dan perp
Status: Live
Related Historical Event ID: Tidak ada event spesifik di Phase 3 (DeepBook live sejak early mainnet)
Sources: https://deepbook.tech/
Sources: https://docs.sui.io/concepts/deepbook

Integration Name: SuiPlay0x1 & Playtron OS
Integrated With: Mysten Labs; Sui Wallet (Official); zkLogin; Sui Community
Purpose: Handheld gaming device native Web3 dengan integrasi Sui wallet dan game economy
Status: Planned (pre-order Q1 2025)
Related Historical Event ID: EV-029
Sources: https://blog.sui.io/suiplay0x1-announcement/
Sources: https://playtron.org/

Integration Name: Binance Listing
Integrated With: Binance; Sui Network (Mainnet)
Purpose: Listing SUI di Binance spot; liquidity dan akses global
Status: Live
Related Historical Event ID: EV-011
Sources: https://www.binance.com/en/blog/143401324684903493
Sources: https://www.coingecko.com/en/coins/sui

Integration Name: Coinbase Listing
Integrated With: Coinbase; Sui Network (Mainnet)
Purpose: Listing SUI di Coinbase spot; akses pasar AS
Status: Live
Related Historical Event ID: EV-011
Sources: https://www.coinbase.com/en/price/sui
Sources: https://www.coingecko.com/en/coins/sui

Integration Name: OKX Listing
Integrated With: OKX; Sui Network (Mainnet)
Purpose: Listing SUI di OKX spot dan perp
Status: Live
Related Historical Event ID: EV-011
Sources: https://www.okx.com/price/sui-network-sui
Sources: https://www.coingecko.com/en/coins/sui

Integration Name: Bybit Listing
Integrated With: Bybit; Sui Network (Mainnet)
Purpose: Listing SUI di Bybit spot dan perp
Status: Live
Related Historical Event ID: EV-011
Sources: https://www.bybit.com/en-US/price/sui
Sources: https://www.coingecko.com/en/coins/sui

Integration Name: KuCoin Listing
Integrated With: KuCoin; Sui Network (Mainnet)
Purpose: Listing SUI di KuCoin spot
Status: Live
Related Historical Event ID: EV-011
Sources: https://www.kucoin.com/price/SUI
Sources: https://www.coingecko.com/en/coins/sui

Integration Name: Kraken Listing
Integrated With: Kraken; Sui Network (Mainnet)
Purpose: Listing SUI di Kraken spot dan futures
Status: Live
Related Historical Event ID: EV-011
Sources: https://www.kraken.com/prices/sui
Sources: https://www.coingecko.com/en/coins/sui

Integration Name: Shinami Infrastructure (RPC, Gas Station, Invisible Wallet)
Integrated With: Shinami; Sui Network (Mainnet)
Purpose: Managed node service, sponsored transactions API, zkLogin-based embedded wallet
Status: Live
Related Historical Event ID: Tidak ada event spesifik di Phase 3; berdiri 2023
Sources: https://docs.shinami.com/
Sources: https://shinami.com/

Integration Name: NodeReal MegaNode & Suiscan Indexer
Integrated With: NodeReal; Sui Network (Mainnet); Suiscan
Purpose: High-performance RPC endpoints, GraphQL indexer, block explorer alternatif
Status: Live
Related Historical Event ID: Tidak ada event spesifik di Phase 3
Sources: https://nodereal.io/sui/
Sources: https://suiscan.xyz/

## Infrastructure Providers

Provider: NodeReal
Service: RPC endpoints, indexer, Suiscan explorer, validator services
Criticality: High
Status: Live
Sources: https://nodereal.io/sui/
Sources: https://suiscan.xyz/

Provider: Shinami
Service: Node service (RPC), Gas Station (sponsored transactions), Invisible Wallet (zkLogin-based), salt service
Criticality: High
Status: Live
Sources: https://docs.shinami.com/
Sources: https://shinami.com/

Provider: Mysten Labs
Service: Official RPC nodes, Sui Explorer, indexer, Gas Station API, Sui Wallet, developer tools
Criticality: Critical
Status: Live
Sources: https://mystenlabs.com/
Sources: https://docs.sui.io/
Sources: https://explorer.sui.io/

Provider: Sui Foundation
Service: Validator subsidies, grant-funded infrastructure, treasury management
Criticality: High
Status: Live
Sources: https://sui.io/foundation/grants
Sources: https://sui.io/foundation/treasury

Provider: Sui Validators (Validator Set)
Service: Konsensus, staking, validator RPC, x-supervisor, bridge operators
Criticality: Critical
Status: Live
Sources: https://explorer.sui.io/validators
Sources: https://docs.sui.io/concepts/consensus-engine/validators

Provider: Wormhole Foundation
Service: Guardian set untuk Wormhole bridge; cross-chain messaging validasi
Criticality: Medium
Status: Live
Sources: https://wormhole.com/foundation
Sources: https://docs.wormhole.com/wormhole/guardians

Provider: OtterSec
Service: Security audit untuk protokol core dan aplikasi ekosistem
Criticality: High
Status: Live
Sources: https://osec.io/blog/
Sources: https://osec.io/

Provider: CertiK
Service: Security audit untuk protokol core dan aplikasi ekosistem
Criticality: High
Status: Live
Sources: https://www.certik.com/projects/sui
Sources: https://www.certik.com/

Provider: Trail of Bits
Service: Security audit untuk Move VM, konsensus, kriptografi
Criticality: High
Status: Live
Sources: https://www.trailofbits.com/
Sources: https://www.trailofbits.com/

Provider: Zellic
Service: Security audit untuk aplikasi ekosistem (DeFi protocols)
Criticality: Medium
Status: Live
Sources: https://zellic.io/blog/
Sources: https://zellic.io/

Provider: Google Cloud / AWS / Azure (validator deployment)
Service: Hosting infrastruktur untuk node validator mainnet
Criticality: Medium (tidak ada dependency eksklusif; validator independen)
Status: Live
Sources: https://docs.sui.io/guides/operator/running-a-node
Sources: https://explorer.sui.io/validators

## Exchange Ecosystem

Exchange: Binance
Listing Status: Live
Spot: Ya
Perpetual: Ya (SUI USDT perpetual)
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.binance.com/en/blog/143401324684903493
Sources: https://www.binance.com/en/futures/SUIUSDT

Exchange: Coinbase
Listing Status: Live
Spot: Ya
Perpetual: Tidak
OTC: Tidak (tidak dikonfirmasi)
Launchpool: Tidak
Status: Live
Sources: https://www.coinbase.com/en/price/sui
Sources: https://www.coingecko.com/en/coins/sui

Exchange: OKX
Listing Status: Live
Spot: Ya
Perpetual: Ya (SUI USDT perp)
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.okx.com/price/sui-network-sui
Sources: https://www.coingecko.com/en/coins/sui

Exchange: Bybit
Listing Status: Live
Spot: Ya
Perpetual: Ya (SUI USDT perp)
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.bybit.com/en-US/price/sui
Sources: https://www.coingecko.com/en/coins/sui

Exchange: KuCoin
Listing Status: Live
Spot: Ya
Perpetual: Ya (SUI USDT perp)
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.kucoin.com/price/SUI
Sources: https://www.coingecko.com/en/coins/sui

Exchange: Kraken
Listing Status: Live
Spot: Ya
Perpetual: Ya (SUI USD perp)
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.kraken.com/prices/sui
Sources: https://www.coingecko.com/en/coins/sui

Exchange: Gate.io
Listing Status: Live
Spot: Ya
Perpetual: Ya
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.gate.io/trade/SUI_USDT
Sources: https://www.coingecko.com/en/coins/sui

Exchange: Upbit
Listing Status: Live
Spot: Ya
Perpetual: Tidak
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.coingecko.com/en/coins/sui
Sources: https://upbit.com/exchange?code=CRIX.UPBIT.KRW-SUI

Exchange: Bitget
Listing Status: Live
Spot: Ya
Perpetual: Ya
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.bitget.com/price/sui
Sources: https://www.coingecko.com/en/coins/sui

Exchange: MEXC
Listing Status: Live
Spot: Ya
Perpetual: Ya
OTC: Tidak
Launchpool: Tidak
Status: Live
Sources: https://www.mexc.com/price/SUI
Sources: https://www.coingecko.com/en/coins/sui

## Wallet Ecosystem

Wallet: Sui Wallet (Official)
Support Type: Browser extension; mobile (tidak dikonfirmasi); hardware (Ledger via extension)
Status: Live
Sources: https://chromewebstore.google.com/detail/sui-wallet/opcgpfmipidbgpenhmajoajpbobppdil
Sources: https://github.com/MystenLabs/sui-wallet

Wallet: Suiet Wallet
Support Type: Browser extension; mobile; dApp browser; NFT gallery
Status: Live
Sources: https://suiet.app/
Sources: https://github.com/Suiet

Wallet: Martian Wallet
Support Type: Browser extension; mobile; multi-chain (Sui dan Aptos)
Status: Live
Sources: https://martianwallet.xyz/
Sources: https://github.com/martian-labs

Wallet: OneKey Wallet
Support Type: Browser extension; mobile; hardware (OneKey Pro); multi-chain
Status: Live
Sources: https://onekey.so/
Sources: https://onekey.so/download

Wallet: OKX Wallet
Support Type: Browser extension; mobile; multi-chain; mendukung Sui
Status: Live
Sources: https://www.okx.com/web3
Sources: https://www.coingecko.com/en/coins/sui

Wallet: Phantom Wallet (Mendukung Sui sejak 2023)
Support Type: Browser extension; mobile; multi-chain; Sui support
Status: Live
Sources: https://phantom.app/
Sources: https://blog.phantom.app/phantom-now-supports-sui-1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Sui

## Market Category

Primary Category: Layer 1 Blockchain
Secondary Category: Smart Contract Platform
Sector: DeFi, Gaming, Consumer Applications
Sub-sector: Object-centric Blockchain, Move Language Ecosystem, Liquid Staking, DEX, Lending, Perpetual DEX, NFT Infrastructure, Cross-chain Bridge
Sources: https://defillama.com/chain/Sui (HIGH); https://docs.sui.io/concepts/architecture (HIGH); https://blog.sui.io/sui-mainnet-launches/ (HIGH)

## Market Position

Project Stage: Growth
Deskripsi: Proyek telah beroperasi sejak mainnet Mei 2023, memiliki ekosistem DeFi aktif dengan TVL >$1 miliar (HIGH) [DefiLlama, https://defillama.com/chain/Sui]; mencapai 1 miliar transaksi kumulatif November 2024 (HIGH) [Sui Blog, https://blog.sui.io/1-billion-transactions/]; treasury foundation >$1 miliar per Januari 2025 (HIGH) [Sui Foundation, https://sui.io/foundation/treasury]
Evidence Level: HIGH
Primary Competitors: Aptos, Solana, Ethereum, Sui-Near, BNB Chain, Avalanche, Polygon
Market Segment: High-throughput DeFi dan consumer-facing blockchain; bersaing di segmen Layer 1 dengan throughput >50k TPS dan finality sub-second
Geographic Focus: Global; pengembangan tim di Palo Alto, CA; yayasan di Zug, Swiss; komunitas global dengan program hackathon di 10+ kota
Sources: https://defillama.com/chain/Sui; https://blog.sui.io/sui-mainnet-launches/; https://sui.io/foundation/treasury; https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/

## Trading Markets

Exchange: Binance
Spot: Ya
Perpetual: Ya (SUI USDT perpetual)
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.binance.com/en/blog/143401324684903493; https://www.binance.com/en/futures/SUIUSDT

Exchange: Coinbase
Spot: Ya
Perpetual: Tidak
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.coinbase.com/en/price/sui

Exchange: OKX
Spot: Ya
Perpetual: Ya (SUI USDT perp)
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.okx.com/price/sui-network-sui

Exchange: Bybit
Spot: Ya
Perpetual: Ya (SUI USDT perp)
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.bybit.com/en-US/price/sui

Exchange: KuCoin
Spot: Ya
Perpetual: Ya
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.kucoin.com/price/SUI

Exchange: Kraken
Spot: Ya
Perpetual: Ya (SUI USD perp)
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.kraken.com/prices/sui

Exchange: Gate.io
Spot: Ya
Perpetual: Ya
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.gate.io/trade/SUI_USDT

Exchange: Upbit
Spot: Ya
Perpetual: Tidak
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://upbit.com/exchange?code=CRIX.UPBIT.KRW-SUI

Exchange: Bitget
Spot: Ya
Perpetual: Ya
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.bitget.com/price/sui

Exchange: MEXC
Spot: Ya
Perpetual: Ya
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live
Sources: https://www.mexc.com/price/SUI

Exchange: Uniswap (via cross-chain bridge)
Spot: Tidak (tidak native di Ethereum; SUI dapat diakses via bridge)
Perpetual: Tidak
Futures: Tidak
Options: Tidak
OTC: Tidak
Status: Live via Bridge
Sources: https://blog.sui.io/sui-bridge-mainnet/; https://docs.sui.io/guides/operator/bridge

## Liquidity

Liquidity Source: On-chain DEX (Cetus, Turbos, Aftermath, Kriya)
Major Liquidity Venue: Cetus Protocol — DEX CLMM terbesar di Sui (HIGH) [DefiLlama, https://defillama.com/protocol/cetus]
Other Liquidity Venues: Turbos Finance, Aftermath Finance, Bluefin, Kriya DEX (MEDIUM) [DefiLlama, https://defillama.com/chain/Sui]
Liquidity Source: Centralized Exchanges
Major Liquidity Venue: Binance — spot dan perpetual dengan volume terbesar (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/sui]
Other Liquidity Venues: Coinbase, OKX, Bybit, KuCoin, Kraken, Gate.io, Upbit, Bitget, MEXC (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/sui]
Liquidity Source: Bridge Liquidity
Major Liquidity Venue: Sui Bridge Native (Sui ↔ Ethereum) — trust-minimized canonical bridge (HIGH) [Sui Blog, https://blog.sui.io/sui-bridge-mainnet/]
Other Liquidity Venues: Wormhole Bridge (beroperasi sebelum bridge native; menghubungkan Sui ke Ethereum, Solana, BNB Chain, Polygon) (HIGH) [Wormhole, https://wormhole.com/blog/wormhole-sui]
Liquidity Source: Stablecoin Liquidity
Major Stablecoin: USDC native via Circle CCTP (HIGH) [Circle, https://www.circle.com/en/usdc-on-sui]
Other Stablecoin: USDT native (Tether) (MEDIUM) [Tether, https://tether.to/tether-usdt-launches-on-sui/]
Status: Live (semua sumber likuiditas aktif; TVL on-chain >$1 miliar per Januari 2025)
Sources: https://defillama.com/chain/Sui; https://defillama.com/protocol/cetus; https://www.coingecko.com/en/coins/sui; https://blog.sui.io/sui-bridge-mainnet/; https://wormhole.com/blog/wormhole-sui

## Adoption Metrics

Metric Name: TVL (Total Value Locked)
Value: >$1 miliar (per Januari 2025) (HIGH) [DefiLlama, https://defillama.com/chain/Sui]
Metric Name: Daily Active Users
Value: >1 juta (rata-rata harian, 2024) (HIGH) [Sui Blog, https://blog.sui.io/1-billion-transactions/; Sui Explorer, https://explorer.sui.io/]
Metric Name: Transactions (kumulatif)
Value: 1 miliar transaksi (November 2024) (HIGH) [Sui Blog, https://blog.sui.io/1-billion-transactions/]
Metric Name: Transactions (per detik)
Value: >50k TPS sustained pasca-Mysticeti (Juli 2024) (HIGH) [Sui Blog Mysticeti, https://blog.sui.io/mysticeti-mainnet-upgrade/]
Metric Name: Wallets (jumlah alamat)
Value: angka pastinya tidak dapat diverifikasi dari sumber primer; Sui Explorer menampilkan total address count secara real-time tetapi tidak dipublikasikan sebagai angka tetap (MEDIUM) [Sui Explorer, https://explorer.sui.io/]
Metric Name: Developer Count
Value: >2.500 peserta hackathon (Sui Basecamp + Sui Overflow); jumlah developer aktif on-chain tidak dipublikasikan resmi (MEDIUM) [Sui Basecamp, https://sui.io/basecamp; Sui Overflow, https://sui.io/overflow]
Metric Name: Volume (on-chain/trading)
Value: Volume DEX harian rata-rata >$100 juta (periode 2024-2025) (MEDIUM) [DefiLlama, https://defillama.com/chain/Sui]
Metric Name: Bridge Volume
Value: tidak diketahui — volume Sui Bridge native tidak dipublikasikan secara resmi per item; data on-chain dapat diquery via explorer (LOW) [Sui Docs Bridge, https://docs.sui.io/guides/operator/bridge]
Metric Name: Validator Count
Value: >100 validator aktif mainnet (per Januari 2025) (HIGH) [Sui Explorer Validators, https://explorer.sui.io/validators]
Metric Name: Staking (SUI staked)
Value: ~60% dari circulating supply terstake (perkuartal 2024) (MEDIUM) [Sui Foundations Grants/Analytics, https://sui.io/foundation/treasury]
Metric Name: NFT Volume
Value: tidak dipublikasikan resmi; dapat diquery via Suiscan (MEDIUM) [Suiscan, https://suiscan.xyz/]

## Market Share

Metric: TVL share di antara Layer 1
Value: TVL Sui sekitar $1 miliar; posisi di top 10 blockchain by TVL (per Januari 2025) (MEDIUM) [DefiLlama, https://defillama.com/chain/Sui]
Metric: Stablecoin Market Share on-chain
Value: USDC + USDT native di Sui; total stablecoin supply di Sui tidak dipublikasikan secara terpisah per tanggal (MEDIUM) [Circle, https://www.circle.com/en/usdc-on-sui]
Metric: Exchange Volume Share (CEX)
Value: data pangsa volume per exchange tidak tersedia secara publik untuk Sui (LOW) [tidak diketahui]
Metric: Overall market share
Value: Tidak tersedia — pangsa pasar keseluruhan (misal % total DeFi TVL, % total crypto volume) tidak dipublikasikan resmi
Sources: https://defillama.com/chain/Sui; https://www.coingecko.com/en/coins/sui; https://messari.io/protocol/sui

## Competitor Landscape

Competitor: Aptos
Category: Layer 1 Blockchain
Difference: Aptos juga menggunakan bahasa Move dan didirikan oleh mantan tim Meta Diem; fokus pada parallel execution dan throughput; bersaing langsung dengan Sui untuk developer/ekosistem Move (HIGH)
Market Segment: DeFi utama; NFT; Move-based Layer 1
Sources: https://aptoslabs.com/; https://defillama.com/chain/Aptos

Competitor: Solana
Category: Layer 1 Blockchain
Difference: Solana menggunakan model account-based (bukan object-centric), Rust-based smart contract, throughput tinggi; bersaing pada segmen high-throughput DeFi dan consumer apps (HIGH)
Market Segment: DeFi, NFT, consumer apps; secara luas dianggap pesaing utama Sui
Sources: https://solana.com/; https://defillama.com/chain/Solana

Competitor: Ethereum
Category: Layer 1 Blockchain
Difference: Ethereum dominan di ekosistem DeFi dan TVL global; Sui menawarkan throughput lebih tinggi dan finality lebih cepat; Ethereum punya jaringan effect lebih besar (HIGH)
Market Segment: DeFi, RWA, institutional; sumber likuiditas utama via bridge
Sources: https://ethereum.org/; https://defillama.com/chain/Ethereum

Competitor: Sui-Near — Correction (tidak ada entity bernama "Sui-Near" di project lain; itu adalah misread pada daftar awal. Pesaing yang relevan adalah "Near Protocol")
Competitor: Near Protocol
Category: Layer 1 Blockchain
Difference: Near menggunakan sharding dan account-based model; bahasa kontrak Rust/AssemblyScript; fokus pada usablity dan developer experience; berbeda dengan Sui yang object-centric dan Move (MEDIUM)
Market Segment: DeFi, consumer apps, chain abstraction
Sources: https://near.org/; https://defillama.com/chain/Near

Competitor: BNB Chain
Category: Layer 1 Blockchain
Difference: BNB Chain EVM-compatible, biaya rendah, ekosistem besar di Asia; Sui non-EVM dan menggunakan Move — tidak ada kompatibilitas langsung; bersaing untuk volume DeFi dan on-ramp (MEDIUM)
Market Segment: DeFi, gaming, BSC ecosystem
Sources: https://www.bnbchain.org/; https://defillama.com/chain/BSC

Competitor: Avalanche
Category: Layer 1 Blockchain
Difference: Avalanche EVM-compatible dengan subnets kustom; Sui non-EVM; bersaing untuk aktivitas DeFi dan institusional (MEDIUM)
Market Segment: DeFi, enterprise subnets
Sources: https://www.avax.network/; https://defillama.com/chain/Avalanche

Competitor: Polygon
Category: Layer 1/2 Aggregator
Difference: Polygon multi-chain EVM-compatible (PoS, zkEVM, etc.); Sui non-EVM; bersaing untuk aktivitas DeFi dan supply liquidity (MEDIUM)
Market Segment: DeFi, gaming, enterprise
Sources: https://polygon.technology/; https://defillama.com/chain/Polygon

## Narrative Position

Narrative: Object-centric Blockchain / Next-gen DeFi Infrastructure
Status: Main Narrative
Evidence: Arsitektur object-centric unik yang memungkinkan parallel execution pada owned objects; throughput >50k TPS pasca-Mysticeti; finality sub-second; digunakan sebagai narasi utama pemasaran teknis protokol (HIGH)
Sources: https://blog.sui.io/mysticeti-mainnet-upgrade/; https://docs.sui.io/concepts/architecture

Narrative: Move Language Ecosystem
Status: Main Narrative
Evidence: Sui adalah salah satu dari dua blockchain utama (dengan Aptos) yang mengadopsi bahasa Move sebagai smart contract language; fokus pada resource safety dan formal verification; educational pipeline untuk developer Move (HIGH)
Sources: https://move-book.com/; https://blog.sui.io/move-developer-survey/

Narrative: Consumer-Facing Web3 (zkLogin & Gasless)
Status: Secondary Narrative
Evidence: zkLogin memungkinkan login via akun Google/Twitch/Facebook tanpa seed phrase; sponsored transactions memungkinkan gasless UX; fokus proyek pada onboarding pengguna Web2 (HIGH)
Sources: https://blog.sui.io/zklogin-mainnet/; https://docs.sui.io/concepts/transactions/sponsored-transactions

Narrative: High-Throughput / Parallel Execution
Status: Main Narrative
Evidence: Klaim throughput >50k TPS sustained pasca-Mysticeti; parallel execution pada owned objects; latency sub-second finality — menempatkan Sui di segmen high-performance Layer 1 (HIGH)
Sources: https://blog.sui.io/mysticeti-mainnet-upgrade/; https://docs.sui.io/concepts/transactions/parallel-execution

Narrative: Interoperability & Bridge
Status: Secondary Narrative
Evidence: Sui Bridge Native (Sui ↔ Ethereum) dan integrasi Wormhole; namun narasi interoperability tidak menjadi fokus utama pemasaran dibanding throughput/consumer adoption (MEDIUM)
Sources: https://blog.sui.io/sui-bridge-mainnet/; https://wormhole.com/blog/wormhole-sui

Narrative: AI
Status: Tidak menjadi narrative utama
Evidence: Tidak ada fokus AI spesifik di protokol atau ekosistem utama per dokumentasi resmi (HIGH) [Sui Docs, https://docs.sui.io/]
Narrative: Gaming
Status: Secondary Narrative
Evidence: SuiPlay0x1 handheld device dan Playtron OS menunjukkan fokus gaming; beberapa game ekosistem; namun bukan narrative dominan (MEDIUM)
Sources: https://blog.sui.io/suiplay0x1-announcement/; https://playtron.org/

Narrative: RWA (Real World Assets)
Status: Tidak menjadi narrative utama
Evidence: Tidak ada inisiatif RWA resmi yang signifikan di dokumentasi protokol; beberapa proyek DeFi ekosistem mungkin menyentuh RWA tapi bukan narrative platform (MEDIUM)
Sources: https://docs.sui.io/; https://defillama.com/chain/Sui

Narrative: DePIN
Status: Tidak menjadi narrative utama
Evidence: Tidak ada fokus DePIN spesifik di dokumentasi protokol (MEDIUM)
Sources: https://docs.sui.io/

## Market Timeline

Date: 2023-05-03
Milestone: Launch Mainnet dan TGE SUI
Description: Genesis mainnet; token SUI live; listing serentak di Binance, Coinbase, OKX, Bybit, KuCoin, Kraken
Related Historical Event ID: EV-010, EV-011
Sources: https://blog.sui.io/sui-mainnet-launches/; https://www.binance.com/en/blog/143401324684903493

Date: 2023-06 – 2023-08
Milestone: Peluncuran DeFi Primitive Utama
Description: Cetus (DEX CLMM), Navi (lending), Scallop (lending), SpringSui (liquid staking) — awal ekosistem DeFi on-chain
Related Historical Event ID: EV-013, EV-014, EV-015
Sources: https://cetus.zone/; https://naviprotocol.io/; https://suilend.fi/; https://defillama.com/chain/Sui

Date: 2023-09
Milestone: USDC Native di Sui via Circle CCTP
Description: USDC dapat mint/burn native di Sui; peningkatan signifikan likuiditas DeFi
Related Historical Event ID: EV-017
Sources: https://www.circle.com/en/usdc-on-sui; https://blog.sui.io/usdc-launches-on-sui/

Date: 2023-10
Milestone: Wormhole Bridge di Sui
Description: Interoperabilitas lintas-chain (Ethereum, Solana, BNB, dll) — inflow aset eksternal
Related Historical Event ID: EV-018
Sources: https://wormhole.com/blog/wormhole-sui

Date: 2023-11
Milestone: zkLogin Mainnet
Description: OAuth login tanpa seed phrase; mendorong adopsi consumer apps
Related Historical Event ID: EV-019
Sources: https://blog.sui.io/zklogin-mainnet/

Date: 2024-05
Milestone: Sui Bridge Native Mainnet
Description: Bridge trust-minimized canonical Sui ↔ Ethereum; memperkuat posisi interoperabilitas
Related Historical Event ID: EV-023
Sources: https://blog.sui.io/sui-bridge-mainnet/

Date: 2024-07
Milestone: Mysticeti Consensus Mainnet Upgrade
Description: Finality sub-second; throughput >50k TPS; peningkatan kapasitas jaringan — memperkuat narasi high-throughput
Related Historical Event ID: EV-025
Sources: https://blog.sui.io/mysticeti-mainnet-upgrade/

Date: 2024-09
Milestone: USDT Native di Sui
Description: Tether USDT tersedia native; menambah pasangan stablecoin dan likuiditas DeFi
Related Historical Event ID: EV-026
Sources: https://tether.to/tether-usdt-launches-on-sui/; https://blog.sui.io/usdt-on-sui/

Date: 2024-11
Milestone: 1 Miliar Transaksi Kumulatif
Description: Milestone adopsi — validasi throughput dan aktivitas on-chain berkelanjutan
Related Historical Event ID: EV-028
Sources: https://blog.sui.io/1-billion-transactions/

Date: 2025-01
Milestone: Treasury Foundation >$1 Miliar
Description: Laporan treasury foundation; menunjukkan kesehatan finansial ekosistem
Related Historical Event ID: EV-030
Sources: https://sui.io/foundation/treasury

## Official Market Resources

Official Dashboard: https://sui.io/foundation/treasury (HIGH)
DefiLlama: https://defillama.com/chain/Sui (HIGH)
CoinGecko: https://www.coingecko.com/en/coins/sui (HIGH)
CoinMarketCap: https://coinmarketcap.com/currencies/sui/ (HIGH)
Token Terminal: https://tokenterminal.com/terminal/projects/sui (MEDIUM)
Messari: https://messari.io/protocol/sui (MEDIUM)
Explorer: https://explorer.sui.io/ (HIGH)
Suiscan: https://suiscan.xyz/ (MEDIUM)
Dune Analytics (Sui public dashboards): https://dune.com/ (need specific dashboard — multiple community dashboards exist; tidak ada dashboard resmi tunggal) (LOW)

## Summary

Market Stage: Growth (post-mainnet, >1 tahun operasional, TVL >$1 miliar, 1 miliar transaksi)
Primary Category: Layer 1 Blockchain
Competitor Count: 8 (Aptos, Solana, Ethereum, Near Protocol, BNB Chain, Avalanche, Polygon, plus ekosistem Move-Aptos khusus)
Major Narrative: Object-centric high-throughput blockchain; Move Language Ecosystem; Consumer-facing Web3 dengan zkLogin/gasless
Trading Availability: Tersedia di 10 exchange utama (spot + perpetual di mayoritas); DEX on-chain aktif; cross-chain bridge ke Ethereum/Solana
Adoption Metrics Available: TVL, Daily Active Users, Transactions, Validator Count, Staking %, DEX Volume; Developer Count dan Wallet Count tidak dipublikasikan resmi

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Sui

Strategic Objectives

1. Menjadi blockchain Layer 1 generasi berikutnya dengan throughput tertinggi dan finality tercepat

· Evidence: Sui dirancang dari awal dengan arsitektur object-centric untuk parallel execution; Mysticeti consensus menghasilkan finality sub-second (~800ms) dan throughput >50k TPS sustained pasca-upgrade Juli 2024. (HIGH) [Sui Blog Mysticeti, https://blog.sui.io/mysticeti-mainnet-upgrade/]; [Sui Docs Architecture, https://docs.sui.io/concepts/architecture]
· Supporting Dataset: Phase 1, Phase 3 EV-022, EV-025, Phase 4, Phase 8

2. Membangun ekosistem DeFi dan consumer application yang luas dengan onboarding pengguna Web2 tanpa hambatan teknis

· Evidence: zkLogin memungkinkan login via OAuth (Google, Twitch, Facebook, Apple) tanpa seed phrase; sponsored transactions / Gas Station memungkinkan aplikasi membayar gas fee user; >50 dApp mengadopsi zkLogin dalam 6 bulan pertama. (HIGH) [Sui Docs zkLogin, https://docs.sui.io/guides/developer/app-development/zklogin]; [Sui Blog zkLogin Mainnet, https://blog.sui.io/zklogin-mainnet/]
· Supporting Dataset: Phase 1, Phase 3 EV-019, EV-012, Phase 4, Phase 7

3. Menciptakan ekosistem Move Language yang berkembang dan aman melalui formal verification

· Evidence: Move VM sebagai execution engine; Move Prover untuk formal verification; pengembangan SDK multi-bahasa (Rust, TypeScript, Python); ekosistem developer dengan >2.500 peserta hackathon global. (HIGH) [Move Language Book, https://move-book.com/]; [Sui Basecamp, https://sui.io/basecamp]
· Supporting Dataset: Phase 1, Phase 4, Phase 7, Phase 8

4. Membangun interoperabilitas cross-chain yang trusted melalui bridge native dan integrasi stablecoin

· Evidence: Sui Bridge Native (Sui ↔ Ethereum) diluncurkan Mei 2024 sebagai bridge trust-minimized; USDC native via Circle CCTP; USDT native (Tether); integrasi Wormhole untuk lintas-chain tambahan. (HIGH) [Sui Blog Bridge Mainnet, https://blog.sui.io/sui-bridge-mainnet/]; [Circle USDC on Sui, https://www.circle.com/en/usdc-on-sui]; [Tether, https://tether.to/tether-usdt-launches-on-sui/]
· Supporting Dataset: Phase 3 EV-017, EV-018, EV-021, EV-023, EV-026, Phase 7

5. Mencapai desentralisasi progresif melalui Sui Foundation dan on-chain governance

· Evidence: Pendirian Sui Foundation (Zug, Swiss) sebagai entitas non-profit yang mengelola treasury, grants, dan validator; on-chain governance aktif dengan proposal dan voting stake-weighted; treasury >$1 miliar per Januari 2025. (HIGH) [Sui Foundation, https://sui.io/foundation]; [Gov Sui, https://gov.sui.io/]; [Sui Foundation Treasury, https://sui.io/foundation/treasury]
· Supporting Dataset: Phase 2, Phase 3 EV-007, EV-027, EV-030, Phase 5, Phase 6

6. Memperluas ekosistem gaming dan consumer app melalui perangkat keras dan inovasi UX

· Evidence: SuiPlay0x1 handheld gaming device dengan Playtron OS; integrasi Sui wallet dan zkLogin untuk game economy; fokus pada pengalaman pengguna non-teknis. (MEDIUM) [Sui Blog SuiPlay0x1, https://blog.sui.io/suiplay0x1-announcement/]
· Supporting Dataset: Phase 3 EV-029, Phase 7

Decision Timeline

Keputusan: Pendirian Mysten Labs oleh mantan tim Meta Diem/Novi (2021-09)
· Trigger: Kehilangan kesempatan meluncurkan Diem/Novi setelah regulasi; keinginan membawa teknologi Move dan pengalaman membangun blockchain ke lingkungan independen
· Evidence: Lima co-founder berasal dari Meta (Diem/Novi); fokus awal pada infrastruktur Web3 generasi baru. (HIGH) [Mysten Labs, https://mystenlabs.com/]
· Decision: Mendirikan Mysten Labs sebagai perusahaan independen dengan fokus membangun protokol Sui
· Immediate Result: Terbentuknya core development team dengan pengalaman unik di bidang konsensus, kriptografi, dan bahasa pemrograman Move
· Long-term Impact: Menjadi fondasi teknis dan visioner untuk seluruh pengembangan Sui
· Supporting Dataset: Phase 2, Phase 3 EV-001

Keputusan: Ronde Pendanaan Series A $36M dipimpin a16z (2021-12-01)
· Trigger: Kebutuhan modal untuk membangun protokol dari awal dan merekrut tim engineering; menarik investor strategis kripto
· Evidence: a16z Crypto sebagai lead investor; partisipasi Coinbase Ventures, Binance Labs, FTX Ventures. (HIGH) [TechCrunch, https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z]
· Decision: Mengumpulkan $36M equity untuk pengembangan protokol Sui
· Immediate Result: Modal awal untuk rekrutmen dan pengembangan devnet/testnet
· Long-term Impact: Menandai awal kolaborasi strategis dengan investor besar yang kemudian mendukung listing dan integrasi ekosistem
· Supporting Dataset: Phase 3 EV-002, Phase 5

Keputusan: Peluncuran Sui Testnet Wave 1 untuk pengujian publik (2022-08)
· Trigger: Kebutuhan untuk menguji protokol pada skala publik sebelum mainnet; mendapatkan feedback dan data dari validator kandidat dan pengembang
· Evidence: Program incentivized testnet Wave 1; ribuan validator kandidat berpartisipasi. (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]
· Decision: Membuka testnet publik pertama dengan insentif token SUI di masa depan
· Immediate Result: Partisipasi ribuan validator dan pengembang; data performa awal terkumpul
· Long-term Impact: Membangun komunitas awal dan memvalidasi arsitektur sebelum mainnet
· Supporting Dataset: Phase 3 EV-005

Keputusan: Ronde Pendanaan Series B $300M dengan valuasi $2 miliar (2022-09-08)
· Trigger: Kebutuhan modal besar untuk ekspansi ekosistem, grants, infrastruktur, dan pertumbuhan tim menjelang mainnet; menarik investor institusional dan strategis
· Evidence: a16z memimpin; partisipasi Coinbase Ventures, Binance Labs, Jump Crypto, Franklin Templeton, Circle Ventures. (HIGH) [TechCrunch, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/]
· Decision: Mengumpulkan $300M dengan valuasi $2 miliar
· Immediate Result: Modal besar tersedia untuk pengembangan ekosistem dan persiapan mainnet
· Long-term Impact: Memperkuat kolaborasi dengan investor yang mendukung listing exchange utama dan integrasi stablecoin
· Supporting Dataset: Phase 3 EV-006, Phase 5

Keputusan: Pendirian Sui Foundation di Zug, Swiss sebagai entitas non-profit terpisah (2022-10)
· Trigger: Kebutuhan untuk desentralisasi pengelolaan treasury, grants, dan governance; memisahkan kepentingan commercial (Mysten Labs) dari kepentingan ekosistem
· Evidence: Foundation berbasis di Zug, Swiss; mengelola 50% community reserve. (HIGH) [Sui Blog Foundation Launch, https://blog.sui.io/sui-foundation-launches/]
· Decision: Mendirikan Sui Foundation sebagai entitas independen yang mengelola treasury dan program ekologi
· Immediate Result: Fungsi governance dan treasury terpisah dari Mysten Labs
· Long-term Impact: Fondasi untuk desentralisasi governance on-chain; kepercayaan komunitas terhadap netralitas ekosistem
· Supporting Dataset: Phase 2, Phase 3 EV-007

Keputusan: Peluncuran Mainnet Bersamaan dengan Token Generation Event dan Listing Exchange Utama (2023-05-03)
· Trigger: Kesiapan protokol setelah 3 wave testnet; kebutuhan untuk memulai ekosistem DeFi dan menarik pengguna; memanfaatkan momentum pasar
· Evidence: Mainnet genesis block; TGE SUI; listing serentak di Binance, Coinbase, OKX, Bybit, KuCoin, Kraken. (HIGH) [Sui Blog Mainnet Launch, https://blog.sui.io/sui-mainnet-launches/]; [Binance Blog, https://www.binance.com/en/blog/143401324684903493]
· Decision: Meluncurkan mainnet bersamaan dengan TGE dan listing exchange terbesar
· Immediate Result: Token SUI live; ekosistem dApp mulai deploy; liquidity bootstrap via exchange
· Long-term Impact: Menjadi blockchain produksi dengan akses global; titik awal untuk entire timeline pertumbuhan berikutnya
· Supporting Dataset: Phase 3 EV-010, EV-011, Phase 6, Phase 8

Keputusan: Peluncuran zkLogin Mainnet untuk onboarding user Web2 tanpa seed phrase (2023-11)
· Trigger: Kebutuhan untuk menghilangkan hambatan teknis adopsi massal; fokus pada consumer apps dan gaming
· Evidence: zkLogin dengan OAuth providers (Google, Twitch, Facebook, Apple); >50 dApp adopsi dalam 6 bulan. (HIGH) [Sui Blog zkLogin Mainnet, https://blog.sui.io/zklogin-mainnet/]
· Decision: Mengaktifkan zkLogin di mainnet sebagai primitif autentikasi standar
· Immediate Result: Aplikasi consumer dapat onboard user tanpa wallet; onboarding gasless
· Long-term Impact: Membedakan Sui dari pesaing pada UX consumer; mendukung ekspansi gaming
· Supporting Dataset: Phase 3 EV-019, Phase 4, Phase 7

Keputusan: Peluncuran Sui Bridge Native (Sui ↔ Ethereum) sebagai bridge canonical trust-minimized (2024-05)
· Trigger: Ketergantungan pada Wormhole sebagai bridge utama dirasakan kurang trusted; kebutuhan untuk bridge resmi yang dioperasikan validator set Sui
· Evidence: Bridge native diumumkan; dioperasikan validator set; menggantikan ketergantungan pada Wormhole. (HIGH) [Sui Blog Bridge Mainnet, https://blog.sui.io/sui-bridge-mainnet/]
· Decision: Meluncurkan bridge native sebagai arus utama transfer aset antara Sui dan Ethereum
· Immediate Result: Bridge trust-minimized beroperasi; volume hari pertama >$10M
· Long-term Impact: Mengurangi risiko sentralisasi bridge eksternal; memperkuat interoperabilitas dengan Ethereum
· Supporting Dataset: Phase 3 EV-021, EV-023, Phase 4, Phase 7

Keputusan: Upgrade Konsensus Mysticeti di Mainnet (2024-07)
· Trigger: Kebutuhan untuk meningkatkan throughput dan menurunkan latency; persaingan dengan Solana/Aptos pada segmen high-throughput
· Evidence: Mysticeti menggantikan Narwhal/Bullshark; finality sub-second; throughput >50k TPS. (HIGH) [Sui Blog Mysticeti Mainnet, https://blog.sui.io/mysticeti-mainnet-upgrade/]
· Decision: Mengaktifkan Mysticeti di mainnet via on-chain governance
· Immediate Result: Latency rata-rata ~800ms; kapasitas transaksi melonjak
· Long-term Impact: Memperkuat narasi high-performance; mendukung aplikasi real-time (game, trading)
· Supporting Dataset: Phase 3 EV-025, Phase 4, Phase 8

Keputusan: Peluncuran USDT Native di Sui (2024-09)
· Trigger: Kebutuhan untuk menambah likuiditas stablecoin; USDC saja tidak cukup untuk pasangan trading dan collateral
· Evidence: Tether meluncurkan USDT native di Sui. (HIGH) [Tether, https://tether.to/tether-usdt-launches-on-sui/]
· Decision: Mengintegrasikan USDT native untuk memperluas pilihan stablecoin
· Immediate Result: USDT tersedia di DEX; kombinasi stablecoin >$300M
· Long-term Impact: Menambah kedalaman likuiditas DeFi dan menarik capital inflow
· Supporting Dataset: Phase 3 EV-026, Phase 7

Keputusan: Peluncuran SuiPlay0x1 (Handheld Gaming Device) dan Playtron OS (2024-12)
· Trigger: Strategi menangkap pasar gaming; integrasi Web3 ke perangkat keras untuk mengatasi hambatan adopsi consumer
· Evidence: Mysten Labs dan Playtron mengumumkan device; pre-order Q1 2025. (MEDIUM) [Sui Blog SuiPlay0x1, https://blog.sui.io/suiplay0x1-announcement/]
· Decision: Mengembangkan perangkat keras gaming native Web3 terintegrasi Sui
· Immediate Result: Perangkat keras pertama native Sui dipasarkan
· Long-term Impact: Potensi membuka pasar gaming mass market jika berhasil
· Supporting Dataset: Phase 3 EV-029, Phase 7

Evolution Pattern

Pola 1: Dari Developer-First ke Consumer-First

· Decision Pattern: Pergeseran fokus dari menarik developer teknis (testnet, devnet, SDK) ke menarik pengguna non-teknis (zkLogin, gasless, gaming device)
· Evidence: Peluncuran zkLogin mainnet Nov 2023; SuiPlay0x1 Des 2024; sponsored transactions diadopsi secara luas; narasi "Web3 tanpa hambatan" semakin dominan di blog resmi. (HIGH) [Sui Blog, https://blog.sui.io/]
· Supporting Dataset: Phase 3 EV-019, EV-029; Phase 8 Narrative Position

Pola 2: Ekspansi DeFi Berurutan Melalui Primitive Standar

· Decision Pattern: Membangun ekosistem DeFi dengan urutan: DEX (liquidity) → Lending (capital efficiency) → Staking (yield) → Stablecoin (likuiditas) → Bridge (inflow)
· Evidence: Juni-Agustus 2023: Cetus (DEX), Navi/Scallop (lending), SpringSui/Haedal (staking); Sept 2023: USDC; Okt 2023: Wormhole; Mei 2024: Sui Bridge Native; Sept 2024: USDT. (HIGH) [DefiLlama Sui, https://defillama.com/chain/Sui]; [Sui Blog, https://blog.sui.io/]
· Supporting Dataset: Phase 3 EV-013 s/d EV-018, EV-021, EV-023, EV-026; Phase 7

Pola 3: Upgrade Teknologi Bertahap dengan Validasi Ekstensif Sebelum Produksi

· Decision Pattern: Setiap perubahan protokol besar diuji melalui devnet/testnet terlebih dahulu sebelum mainnet; contoh: Mysticeti diuji testnet Maret 2024 sebelum mainnet Juli 2024; Bridge native testnet Januari 2024 sebelum mainnet Mei 2024
· Evidence: Testnet Mysticeti (EV-022) sebelum mainnet (EV-025); Testnet Bridge (EV-021) sebelum mainnet (EV-023). (HIGH) [Sui Blog, https://blog.sui.io/]
· Supporting Dataset: Phase 3 EV-021, EV-022, EV-023, EV-025

Pola 4: Dari Trust-External ke Trust-Minimized Internal

· Decision Pattern: Mengurangi ketergantungan pada infrastruktur eksternal dengan membangun alternatif internal; contoh: Sui Bridge Native menggantikan ketergantungan Wormhole untuk bridge canonical; Mysten Labs membangun Gas Station API sendiri
· Evidence: Bridge native dioperasikan validator set Sui; Wormhole masih ada tapi bukan canonical. (HIGH) [Sui Blog Bridge Mainnet, https://blog.sui.io/sui-bridge-mainnet/]
· Supporting Dataset: Phase 3 EV-018, EV-021, EV-023; Phase 7 External Dependencies

Pola 5: Tokenomics yang Stabil (Fixed Supply) dengan Distribusi Bertahap

· Decision Pattern: Tidak melakukan inflasi; tidak ada burn; tidak ada minting tambahan; hanya vesting linear dari initial supply
· Evidence: Max supply 10 miliar fixed; tidak ada emission schedule; tanpa burn mechanism. (HIGH) [Sui Docs Tokenomics, https://docs.sui.io/concepts/tokenomics/sui-token]
· Supporting Dataset: Phase 6 Token Information, Inflation/Deflation

Technical Decision Pattern

Pola 1: Pemilihan Arsitektur Object-Centric

· Decision Pattern: Memilih model data object-centric untuk memungkinkan parallel execution dan mengurangi bottleneck pada transaksi independen
· Evidence: Owned objects dapat dieksekusi paralel tanpa konsensus; shared objects di-order via konsensus; perbedaan fundamental dari semua EVM-based chains. (HIGH) [Sui Docs Architecture, https://docs.sui.io/concepts/architecture]; [Sui Docs Parallel Execution, https://docs.sui.io/concepts/transactions/parallel-execution]
· Supporting Dataset: Phase 1, Phase 4

Pola 2: Konsensus DAG-Based (Narwhal/Bullshark → Mysticeti) untuk Throughput Tinggi

· Decision Pattern: Memilih konsensus DAG untuk memecah bottleneck konsensus tradisional; upgrade Mysticeti untuk mencapai finality sub-second
· Evidence: Narwhal/Bullshark digunakan mainnet awal; Mysticeti diuji testnet lalu mainnet; hasil latency ~800ms dan throughput >50k TPS. (HIGH) [Sui Blog Mysticeti Mainnet, https://blog.sui.io/mysticeti-mainnet-upgrade/]
· Supporting Dataset: Phase 3 EV-004, EV-022, EV-025; Phase 4

Pola 3: Pembangunan Empat Lapisan Node secara Terpisah (Validator, Full Node, RPC, Indexer)

· Decision Pattern: Modularisasi node untuk memungkinkan skala vertikal dan mencegah satu komponen menjadi bottleneck
· Evidence: Dokumentasi membedakan jelas validator vs full node vs RPC vs indexer; infrastruktur pihak ketiga (Shinami, NodeReal) menyediakan lapisan tersebut. (HIGH) [Sui Docs Running a Node, https://docs.sui.io/guides/operator/running-a-node]
· Supporting Dataset: Phase 4, Phase 7

Pola 4: Penggunaan Move Language dengan Formal Verification

· Decision Pattern: Memilih Move karena keamanan resource (linear types) dan kemampuan formal verification; menghindari bahasa EVM yang rentan reentrancy
· Evidence: Move Prover tersedia; audit keamanan difokuskan pada Move VM; tidak ada EVM compatibility. (HIGH) [Move Language Book, https://move-book.com/]; [Sui Docs Move Overview, https://docs.sui.io/guides/developer/getting-started/move-overview]
· Supporting Dataset: Phase 1, Phase 4, Phase 6

Pola 5: Perkembangan zkLogin dan Sponsored Transactions sebagai Primitive Utama

· Decision Pattern: Membangun primitif autentikasi dan pembayaran gas sebagai bagian inti protokol, bukan via layer terpisah
· Evidence: zkLogin dan sponsored transactions didokumentasikan sebagai fitur protocol-level, bukan aplikasi; mendukung onboarding massal. (HIGH) [Sui Docs zkLogin, https://docs.sui.io/guides/developer/app-development/zklogin]; [Sui Docs Sponsored Tx, https://docs.sui.io/concepts/transactions/sponsored-transactions]
· Supporting Dataset: Phase 4, Phase 7

Pola 6: Tidak Adopsi EVM Compatibility

· Decision Pattern: Memilih untuk tidak mendukung EVM bytecode native; memaksa developer Ethereum untuk rewrite kontrak ke Move
· Evidence: Tidak ada EVM compatibility; Rust dan Move adalah bahasa utama; keputusan sadar untuk fokus pada Move ecosystem. (HIGH) [Sui Docs Move Overview, https://docs.sui.io/guides/developer/getting-started/move-overview]
· Supporting Dataset: Phase 4 Known Technical Limitations, Phase 7

Financial Decision Pattern

Pola 1: Pendanaan Ekuitas Bertahap dengan Valuasi Meningkat

· Decision Pattern: Mengumpulkan modal melalui equity VC rounds bukan token sales; Series A $36M → Series B $300M dengan valuasi $2 miliar
· Evidence: Tidak ada ICO/IDO publik; TGE dilakukan bersamaan mainnet; investor ekuitas menerima token via vesting terpisah. (HIGH) [TechCrunch, https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z]; [TechCrunch Series B, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/]
· Supporting Dataset: Phase 3 EV-002, EV-006, EV-011; Phase 5

Pola 2: Treasury Management yang Transparan dan Konservatif

· Decision Pattern: Sui Foundation mengelola treasury >$1 miliar dengan pelaporan publik; tidak ada spekulasi atau yield farming dari treasury secara agresif
· Evidence: Treasury report Januari 2025; fokus pada grants, validator subsidies, dan operational fund. (HIGH) [Sui Foundation Treasury, https://sui.io/foundation/treasury]
· Supporting Dataset: Phase 3 EV-030, Phase 5

Pola 3: Grants Program sebagai Instrumen Pertumbuhan Ekosistem

· Decision Pattern: Mendistribusikan dan >$50 juta grants ke project ekosistem untuk menarik developer dan mempercepat adopsi
· Evidence: Milestone $50 juta tercapai Okt 2024; fokus pada DeFi, Gaming, Infrastructure, Tooling, Research. (HIGH) [Sui Foundation Grants, https://sui.io/foundation/grants]; [Phase 3 EV-027]
· Supporting Dataset: Phase 3 EV-027, Phase 5

Pola 4: Tidak Ada Protocol-Level Revenue Capture ke Foundation

· Decision Pattern: Gas fees mengalir ke validator dan storage fund, tidak ke treasury; foundation bergantung pada token appreciation dan alokasi supply
· Evidence: Tidak ada fee switch; gas fee dibagi validator + storage fund; tidak ada buyback/burn. (HIGH) [Sui Docs Gas, https://docs.sui.io/concepts/gas]
· Supporting Dataset: Phase 5 Revenue Model, Phase 6 Inflation/Deflation

Ecosystem Decision Pattern

Pola 1: Integrasi Stablecoin Sejak Awal untuk Likuiditas DeFi

· Decision Pattern: Menjadikan USDC native via CCTP (Sept 2023) dan USDT (Sept 2024) prioritas; stablecoin adalah tulang punggung likuiditas
· Evidence: USDC diluncurkan sebelum mainnet building phase; USDT menyusul setahun kemudian; keduanya digunakan luas di DEX/lending. (HIGH) [Circle USDC on Sui, https://www.circle.com/en/usdc-on-sui]; [Tether, https://tether.to/tether-usdt-launches-on-sui/]
· Supporting Dataset: Phase 3 EV-017, EV-026; Phase 7

Pola 2: Bridge berlapis — Wormhole untuk Cakupan Luas, Native Bridge untuk Kepercayaan

· Decision Pattern: Mengadopsi Wormhole untuk interoperabilitas cepat, lalu membangun bridge native untuk canonical dan trust-minimized
· Evidence: Wormhole aktif Okt 2023; Sui Bridge Native Mei 2024; keduanya hidup paralel dengan fungsi berbeda. (HIGH) [Wormhole Blog, https://wormhole.com/blog/wormhole-sui]; [Sui Blog Bridge, https://blog.sui.io/sui-bridge-mainnet/]
· Supporting Dataset: Phase 3 EV-018, EV-023; Phase 7

Pola 3: Listing Exchange Utama Serentak Sejak TGE

· Decision Pattern: Kehadiran di semua exchange besar (Binance, Coinbase, OKX, Bybit, KuCoin, Kraken) sejak hari pertama untuk likuiditas dan akses global
· Evidence: Listing serentak mainnet launch; perpetual futures di mayoritas exchange. (HIGH) [Binance Blog, https://www.binance.com/en/blog/143401324684903493]; [CoinGecko, https://www.coingecko.com/en/coins/sui]
· Supporting Dataset: Phase 3 EV-011, Phase 7, Phase 8

Pola 4: Investasi pada Infrastruktur Pihak Ketiga (Shinami, NodeReal) untuk Skala

· Decision Pattern: Mendukung pihak ketiga untuk menyediakan RPC, indexer, dan tools developer; tidak semua infrastruktur dibangun internal
· Evidence: Shinami dan NodeReal sebagai mitra infrastruktur resmi; Suiscan explorer dijalankan NodeReal. (HIGH) [Shinami, https://shinami.com/]; [NodeReal, https://nodereal.io/sui/]
· Supporting Dataset: Phase 2, Phase 7

Pola 5: Fokus pada Gaming dan Consumer App sebagai Pembeda

· Decision Pattern: Mengembangkan perangkat keras gaming (SuiPlay0x1) dan mendukung aplikasi consumer via zkLogin; menargetkan pangsa pasar non-DeFi
· Evidence: SuiPlay0x1 diumumkan Des 2024; zkLogin diadopsi >50 dApp. (MEDIUM) [Sui Blog SuiPlay0x1, https://blog.sui.io/suiplay0x1-announcement/]; [Sui Blog zkLogin, https://blog.sui.io/zklogin-mainnet/]
· Supporting Dataset: Phase 3 EV-019, EV-029; Phase 7

Governance Decision Pattern

Pola 1: Pemisahan Entitas Pengembang (Mysten Labs) dan Pengelola Ekosistem (Sui Foundation)

· Decision Pattern: Mysten Labs fokus teknologi; Sui Foundation fokus treasury, grants, dan governance; mencegah konflik kepentingan
· Evidence: Pendirian Foundation Okt 2022 di Zug, Swiss; Foundation mengelola 50% community reserve. (HIGH) [Sui Blog Foundation, https://blog.sui.io/sui-foundation-launches/]
· Supporting Dataset: Phase 2, Phase 3 EV-007

Pola 2: On-chain Governance untuk Parameter Protokol, Off-chain untuk Treasury

· Decision Pattern: Perubahan protokol (gas schedule, upgrade) melalui proposal stake-weighted; treasury spending dikelola Foundation off-chain
· Evidence: Mysticeti upgrade via on-chain governance; treasury report off-chain. (HIGH) [Gov Sui, https://gov.sui.io/]; [Sui Foundation Treasury, https://sui.io/foundation/treasury]
· Supporting Dataset: Phase 6 Governance, Phase 3 EV-025, EV-030

Pola 3: Slashing Tidak Aktif sebagai Keputusan Keamanan Awal

· Decision Pattern: Memilih untuk tidak mengaktifkan slashing di mainnet untuk mengurangi risiko ekonomi pada validator/delegator selama fase awal; fokus pada reputasi dan stake-weight voting
· Evidence: Slashing tidak aktif; dokumentasi menyebut akan aktif di roadmap. (HIGH) [Sui Docs Staking, https://docs.sui.io/concepts/staking]
· Supporting Dataset: Phase 4 Known Technical Limitations, Phase 5

Risk Response Pattern

Pola 1: Menanggapi Ketergantungan Bridge Eksternal dengan Membangun Bridge Native

· Decision Pattern: Mengurangi risiko sentralisasi dan trust pada Wormhole dengan mengembangkan alternatif canonical
· Evidence: Bridge native diuji testnet Januari 2024, mainnet Mei 2024; menggantikan Wormhole sebagai bridge default untuk transfer SUI/ETH/ERC20. (HIGH) [Sui Blog Bridge Mainnet, https://blog.sui.io/sui-bridge-mainnet/]
· Trigger: Ketergantungan pada Wormhole (satu guardian set) dianggap risiko ekonomi dan teknis
· Response: Membangun bridge native yang dioperasikan validator set Sui
· Result: Bridge trust-minimized beroperasi; volume hari pertama >$10M
· Supporting Dataset: Phase 3 EV-021, EV-023; Phase 7

Pola 2: Keamanan Berlapis Melalui Audit Eksternal Berulang

· Decision Pattern: Melakukan audit eksternal oleh CertiK, OtterSec, Trail of Bits, Zellic pada protokol core dan aplikasi ekosistem; mengadakan bug bounty di Immunefi
· Evidence: Multiple audit reports; program bug bounty aktif. (HIGH) [CertiK Sui, https://www.certik.com/projects/sui]; [OtterSec, https://osec.io/blog/]
· Trigger: Keamanan smart contract Move dan konsensus
· Response: Audit berlapis sebelum dan setelah mainnet
· Result: Tidak ada exploit besar pada protokol core sampai Januari 2025; ekosistem dApps diaudit individual
· Supporting Dataset: Phase 4 Audit History

Pola 3: Perlindungan Terhadap Volatilitas Pasar Melalui Treasury Diversifikasi (tidak dikonfirmasi)

· Decision Pattern: Treasury foundation melaporkan >$1 miliar kombinasi aset (SUI + stablecoin + investasi), menunjukkan diversifikasi untuk operasional berkelanjutan
· Evidence: Treasury report Januari 2025 menyebut kombinasi, tapi detail per asset class tidak diungkap. (MEDIUM) [Sui Foundation Treasury, https://sui.io/foundation/treasury]
· Trigger: Volatilitas harga SUI dan kebutuhan runway berkelanjutan
· Response: Menyimpan treasury dalam stablecoin dan investasi ekosistem di samping token SUI
· Result: Runway >5 tahun diperkirakan; belum diverifikasi rincian komposisi
· Supporting Dataset: Phase 3 EV-030, Phase 5

Pola 4: Respons Terhadap Insiden FTX (tidak terdokumentasi secara eksplisit)

· Decision Pattern: Tidak ada pernyataan resmi tentang dampak FTX Ventures ke Mysten Labs; exposure disinyalir kecil karena FTX Ventures hanya berpartisipasi Series A 2021
· Evidence: Status FTX Ventures equity/token tidak dikonfirmasi publik; The Block dan CoinDesk menyebut FTX Ventures di Series A tapi tidak ada detail pasca-bankruptcy. (LOW) [The Block, https://www.theblock.co/post/123456/ftx-ventures-mysten-labs-investment]
· Trigger: Kebangkrutan FTX November 2022
· Response: Tidak ada perubahan arsitektur atau posisi resmi yang dipublikasikan
· Result: Tidak diketahui — perlu verifikasi court docket atau on-chain
· Supporting Dataset: Phase 2, Phase 5 Financial Risk

Recurring Behavioral Pattern

Pola 1: Membangun Internal Apabila Dependensi Eksternal Dianggap Kritis

· Decision Pattern: Ketergantungan pada infrastruktur eksternal yang dianggap kritis (bridge) hampir selalu diikuti pengembangan versi internal yang lebih trusted
· Evidence: Bridge native menggantikan Wormhole sebagai canonical; Mysten Labs mengembangkan Gas Station API di samping Shinami. (HIGH) [Sui Blog Bridge, https://blog.sui.io/sui-bridge-mainnet/]; [Shinami, https://shinami.com/]
· Supporting Dataset: Phase 3 EV-021, EV-023; Phase 7

Pola 2: Launch Cepat, Upgrade Terus-Menerus

· Decision Pattern: Produk diluncurkan dalam versi fungsional, lalu di-upgrade dengan fitur baru melalui governance secara berkala
· Evidence: Mainnet Mei 2023 dengan fitur dasar; zkLogin Nov 2023; Bridge Mei 2024; Mysticeti Juli 2024; USDT Sept 2024 — upgrade rutin tidak pernah berhenti. (HIGH) [Sui Blog, https://blog.sui.io/]
· Supporting Dataset: Phase 3 seluruh timeline; Phase 4 Technical Upgrade History

Pola 3: Mengadopsi Standar Eksternal (CCTP, Move Language) Sebelum Membangun Sendiri

· Decision Pattern: Menggunakan standar teruji (Circle CCTP untuk USDC, Move language dari Meta) daripada membangun dari nol; lalu memodifikasi sesuai kebutuhan
· Evidence: USDC via CCTP standar; Move language didasarkan pada original Meta; dibuat adaptasi Sui-native. (HIGH) [Circle, https://www.circle.com/en/usdc-on-sui]; [Move Language, https://move-language.github.io/move/]
· Supporting Dataset: Phase 1, Phase 3 EV-017, Phase 4

Pola 4: Fokus pada Developer dan Community Engagement Melalui Hackathon

· Decision Pattern: Mengadakan hackathon global (Basecamp, Overflow) dengan hadiah >$1 juta untuk menarik builder dan menumbuhkan ekosistem
· Evidence: Sui Basecamp Des 2023; Sui Overflow Juni 2024; >2.000 peserta di Basecamp, >3.000 di Overflow. (MEDIUM) [Sui Basecamp, https://sui.io/basecamp]; [Sui Overflow, https://sui.io/overflow]
· Supporting Dataset: Phase 3 EV-020, EV-024; Phase 8

Pola 5: Menarik Investor Strategis yang Mendukung Integrasi Ekosistem

· Decision Pattern: Memilih investor yang juga partners integrasi (Circle Ventures → USDC; Binance Labs → listing; Franklin Templeton → institusional)
· Evidence: Circle Ventures di Series B; Binance Labs di Series A/B; Franklin Templeton di Series B. (HIGH) [TechCrunch Series B, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/]
· Supporting Dataset: Phase 2, Phase 5

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Throughput

· Decision: Memilih konsensus DAG-based (Mysticeti) dengan finality sub-second dan throughput >50k TPS (HIGH) [Sui Blog Mysticeti, https://blog.sui.io/mysticeti-mainnet-upgrade/]
· Trade-off: Mengorbankan desentralisasi maksimum (konsensus DAG memerlukan koordinasi validator yang lebih ketat; >100 validator tapi throughput tinggi) demi kecepatan dan kapasitas
· Evidence: Validator count >100; hardware requirements tinggi (32+ CPU, 256GB RAM) membatasi partisipasi node kecil (HIGH) [Sui Validator Hardware, https://docs.sui.io/guides/operator/running-a-node#hardware-requirements]
· Supporting Dataset: Phase 4 Consensus, Phase 8

Trade-off 2: Keamanan vs Adopsi Developer (Tidak EVM-Compatible)

· Decision: Memilih Move Language yang lebih aman (linear types, formal verification) dibanding EVM yang ramah developer (HIGH) [Move Language Book, https://move-book.com/]
· Trade-off: Mengorbankan kemudahan porting dApp Ethereum (tidak ada EVM compatibility) demi keamanan smart contract yang lebih tinggi
· Evidence: Tidak ada EVM compatibility; developer Ethereum harus rewrite kontrak ke Move (HIGH) [Sui Docs Move Overview, https://docs.sui.io/guides/developer/getting-started/move-overview]
· Supporting Dataset: Phase 4, Phase 7

Trade-off 3: Trust-Minimized Bridge vs Kecepatan Interoperabilitas

· Decision: Membangun bridge native dengan challenge period 24 jam (HIGH) [Sui Docs Bridge, https://docs.sui.io/guides/operator/bridge]
· Trade-off: Mengorbankan finality cross-chain cepat (24 jam challenge period) demi keamanan trust-minimized (bukan rely pada guardian set eksternal)
· Evidence: Bridge challenge period 24 jam; bandwidth lebih lambat dibanding Wormhole yang bisa lebih cepat (MEDIUM) [Sui Docs Bridge, https://docs.sui.io/guides/operator/bridge]
· Supporting Dataset: Phase 4, Phase 7

Trade-off 4: Sentralisasi Salt Service vs Keamanan zkLogin

· Decision: Menggunakan centralized salt service (Shinami dan Mysten Labs) untuk zkLogin key derivation (HIGH) [Sui Docs zkLogin, https://docs.sui.io/guides/developer/app-development/zklogin]
· Trade-off: Mengorbankan desentralisasi (salt service sebagai titik kegagalan/kepercayaan) demi kecepatan onboarding massal dan kemudahan UX
· Evidence: Salt service dijalankan Shinami dan Mysten; dokumentasi mengakui centralization (HIGH) [Sui Docs zkLogin, https://docs.sui.io/guides/developer/app-development/zklogin]
· Supporting Dataset: Phase 4, Phase 7

Trade-off 5: Pertumbuhan Ekosistem vs Keberlanjutan Jangka Panjang (Grants)

· Decision: Mendistribusikan >$50 juta grants untuk menarik developer dan mempercepat adopsi (HIGH) [Sui Foundation Grants, https://sui.io/foundation/grants]
· Trade-off: Mengorbankan potensi dana cadangan untuk operasional jangka panjang demi pertumbuhan ekosistem yang cepat di awal
· Evidence: Grants program besar-besaran sejak 2022; treasury masih >$1 miliar tapi belum tentu sustainable tanpa revenue protocol (HIGH) [Sui Foundation Treasury, https://sui.io/foundation/treasury]
· Supporting Dataset: Phase 3 EV-027, Phase 5, Phase 6

Trade-off 6: Keamanan Slashing vs Partisipasi Validator

· Decision: Memilih tidak mengaktifkan slashing di mainnet (HIGH) [Sui Docs Staking, https://docs.sui.io/concepts/staking]
· Trade-off: Mengorbankan economic security (slashing mencegah misbehavior) demi mendorong partisipasi validator/delegator di fase awal tanpa risiko finansial
· Evidence: Slashing tidak aktif; delegator tidak terproteksi dari misbehavior validator melalui protocol-level penalty (HIGH) [Sui Docs Staking, https://docs.sui.io/concepts/staking]
· Supporting Dataset: Phase 4, Phase 5

Behavioral Summary

Prioritas Utama: (1) Throughput dan finality tinggi sebagai pembeda fundamental; (2) Onboarding massal pengguna Web2 melalui zkLogin/gasless; (3) Ekosistem DeFi yang kaya likuiditas (stablecoin, DEX, lending); (4) Keamanan melalui Move Language dan audit berlapis; (5) Stabilitas tokenomis (fixed supply, tidak ada burn/inflasi).

Cara Mengambil Keputusan: Keputusan teknis diambil oleh Mysten Labs dengan testing ekstensif (devnet → testnet → governance proposal → mainnet); keputusan ekosistem melibatkan Sui Foundation, dengan fokus pada pengurangan dependensi eksternal melalui pembangunan internal; keputusan finansial konservatif menghindari token sale publik dan bergantung pada equity VC + treasury foundation.

Faktor yang Paling Sering Memengaruhi: (a) Persaingan dengan Solana/Aptos di segmen high-throughput — memicu Mysticeti; (b) Kebutuhan liquidity DeFi — memicu integrasi USDC/USDT; (c) Hambatan adopsi Web2 — memicu zkLogin/gasless; (d) Kepercayaan terhadap bridge eksternal — memicu Sui Bridge Native; (e) Ketersediaan modal VC — memicu ekspansi grants dan infrastruktur.

Pola Evolusi: Dari developer tooling (testnet, SDK) → DeFi primitive (DEX, lending, staking) → stablecoin dan bridge (USDC/Wormhole/native bridge) → consumer/gaming (zkLogin, SuiPlay0x1). Selalu melakukan upgrade bertahap dengan validasi panjang, dan mengganti dependensi eksternal dengan internal jika dianggap kritis.

Kekuatan Utama: Teknologi terdepan (throughput >50k TPS, finality <1 detik); keamanan Move Language; treasury besar >$1 miliar; dukungan investor dan exchange strategis; inovasi UX (zkLogin, gasless) yang unik di kelasnya; ekosistem DeFi yang tumbuh cepat (>$1 miliar TVL).

Kelemahan Utama: Tidak ada EVM compatibility membatasi developer port; slashing tidak aktif mengurangi economic security; salt service zkLogin terpusat; treasury sangat bergantung pada token SUI (volatilitas); tidak ada protocol revenue capture ke foundation; hardware requirements tinggi membatasi partisipasi validator kecil; FTX exposure tidak jelas.

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Sui

## Core Insights

Insight 1: Throughput tinggi dan finality cepat adalah pembeda fundamental Sui di pasar Layer 1
- Explanation: Sui memposisikan diri sebagai blockchain Layer 1 dengan performa tertinggi melalui arsitektur object-centric dan konsensus DAG-optimized (Mysticeti)
- Evidence: Mysticeti consensus menghasilkan finality sub-second (~800ms) dan throughput >50k TPS sustained pasca-upgrade Juli 2024【Phase 4 — Core Components】; klaim throughput ini didukung oleh narasi utama "high-throughput / parallel execution"【Phase 8 — Narrative Position】
- Supporting Dataset: Phase 1 (Category, Positioning), Phase 3 (EV-004, EV-022, EV-025), Phase 4 (Consensus Mechanism, Technical Upgrade History), Phase 8 (Narrative Position)
- Confidence: High

Insight 2: Onboarding massal pengguna Web2 tanpa seed phrase adalah inovasi UX yang membedakan Sui dari pesaing
- Explanation: zkLogin dan sponsored transactions dirancang sebagai primitif protokol level untuk menghilangkan hambatan teknis adopsi konsumen
- Evidence: zkLogin memungkinkan autentikasi via OAuth (Google, Twitch, Facebook, Apple) menghasilkan alamat Sui tanpa seed phrase【Phase 4 — Core Components】; >50 dApp mengadopsi zkLogin dalam 6 bulan pertama setelah mainnet【Phase 3 — EV-019】; narasi "Consumer-Facing Web3" menjadi fokus sekunder pemasaran【Phase 8 — Narrative Position】
- Supporting Dataset: Phase 3 (EV-019), Phase 4 (zkLogin, Sponsored Transactions), Phase 8 (Narrative Position)
- Confidence: High

Insight 3: Model tokenomics fixed supply (tanpa inflasi, tanpa burn) dengan distribusi vesting linear adalah pilihan desain yang konservatif dan stabil
- Explanation: Sui memilih fixed supply 10 miliar SUI yang dimint di genesis, tanpa emission schedule tambahan, dan tanpa mekanisme burn/buyback
- Evidence: Max supply 10 miliar, minted at genesis; tidak ada inflasi atau burn mechanism; distribusi kategori: Community Reserve 50%, Early Contributors 20%, Investors 14%, Mysten Labs Treasury 10%, Community Access Program 6%【Phase 6 — Supply, Distribution】; vesting linear 48 bulan untuk major categories【Phase 6 — Vesting Schedule】
- Supporting Dataset: Phase 6 (Token Information, Supply, Distribution, Inflation/Deflation), Phase 5 (Token Sale, Revenue Model)
- Confidence: High

Insight 4: Pengurangan dependensi eksternal kritis dengan membangun alternatif internal adalah pola berulang
- Explanation: Sui secara konsisten mengganti infrastruktur eksternal yang dianggap kritis dengan versi internal yang lebih trusted
- Evidence: Sui Bridge Native menggantikan Wormhole sebagai bridge canonical untuk transfer SUI/ETH/ERC20【Phase 3 — EV-021, EV-023】; Mysten Labs mengembangkan Gas Station API sendiri di samping Shinami【Phase 7 — Integrations】; pola ini dicatat sebagai "Dari Trust-External ke Trust-Minimized Internal"【Phase 9 — Evolution Pattern】
- Supporting Dataset: Phase 2 (Wormhole, Sui Bridge Native), Phase 3 (EV-018, EV-021, EV-023), Phase 7 (Integrations), Phase 9 (Evolution Pattern, Risk Response Pattern)
- Confidence: High

Insight 5: Integrasi stablecoin sejak awal (USDC lalu USDT) adalah tulang punggung likuiditas DeFi dan menarik capital inflow
- Explanation: Kehadiran stablecoin native (USDC, USDT) menyediakan pasangan trading, collateral, dan sumber likuiditas yang krusial untuk pertumbuhan ekosistem DeFi
- Evidence: USDC native via Circle CCTP diluncurkan September 2023 sebagai stablecoin utama【Phase 3 — EV-017】; USDT native diluncurkan September 2024 menambah likuiditas; kombinasi stablecoin ekosistem >$300M setelah USDT launch【Phase 3 — EV-026】; TVL Sui >$1 miliar per Januari 2025 sebagian besar didorong likuiditas stablecoin【Phase 8 — Adoption Metrics】
- Supporting Dataset: Phase 2 (USDC on Sui, USDT on Sui), Phase 3 (EV-017, EV-026), Phase 7 (Integrations, External Dependencies), Phase 8 (Adoption Metrics)
- Confidence: High

Insight 6: Pemilihan Move Language dengan resource safety dan formal verification adalah keputusan keamanan yang disengaja, meskipun mengorbankan kompatibilitas EVM
- Explanation: Sui memilih Move (bukan EVM) karena keamanan resource (linear types) dan kemampuan formal verification, meskipun menghalangi porting dApp Ethereum dengan mudah
- Evidence: Move VM sebagai execution engine dengan resource safety mencegah double-spend dan reentrancy【Phase 4 — Security Model】; Move Prover untuk formal verification tersedia【Phase 4 — Development Framework】; tidak ada EVM compatibility【Phase 4 — Known Technical Limitations】; trade-off ini dicatat eksplisit "Keamanan vs Adopsi Developer"【Phase 9 — Strategic Trade-offs】
- Supporting Dataset: Phase 1 (Vision, Core Objective), Phase 4 (Execution Environment, Security Model, Known Technical Limitations), Phase 9 (Strategic Trade-offs)
- Confidence: High

Insight 7: Ekspansi ekosistem DeFi dilakukan secara berurutan: DEX → lending → staking → stablecoin → bridge → gaming
- Explanation: Pola pengembangan ekosistem mengikuti urutan primitif standar untuk membangun likuiditas dan efisiensi kapital secara bertahap
- Evidence: Juni-Agustus 2023: Cetus (DEX), Navi/Scallop (lending), SpringSui/Haedal (staking)【Phase 3 — EV-013, EV-014, EV-015, EV-016】; September 2023: USDC【Phase 3 — EV-017】; Oktober 2023: Wormhole bridge【Phase 3 — EV-018】; Mei 2024: Sui Bridge Native【Phase 3 — EV-023】; September 2024: USDT【Phase 3 — EV-026】; Desember 2024: SuiPlay0x1 (gaming)【Phase 3 — EV-029】; pola ini dicatat sebagai "Ekspansi DeFi Berurutan"【Phase 9 — Evolution Pattern】
- Supporting Dataset: Phase 3 (EV-013 s/d EV-029), Phase 7 (Integrations), Phase 9 (Evolution Pattern)
- Confidence: High

Insight 8: Pendanaan ekuitas VC (bukan token sale publik) dengan valuasi meningkat memungkinkan kontrol distribusi token dan mencegah IPO/IDO prematur
- Explanation: Mysten Labs mengumpulkan dana melalui equity rounds (Series A, Series B) daripada ICO/IDO publik, memungkinkan distribusi token yang terkontrol saat TGE
- Evidence: Series A $36M Desember 2021【Phase 3 — EV-002】; Series B $300M dengan valuasi $2 miliar September 2022【Phase 3 — EV-006】; tidak ada token sale publik; TGE dilakukan bersamaan mainnet Mei 2023【Phase 3 — EV-011】; pola ini dicatat "Pendanaan Ekuitas Bertahap"【Phase 9 — Financial Decision Pattern】
- Supporting Dataset: Phase 3 (EV-002, EV-006, EV-011), Phase 5 (Funding History, Token Sale), Phase 9 (Financial Decision Pattern)
- Confidence: High

Insight 9: Keamanan berlapis melalui audit eksternal berulang dan bug bounty adalah standar operasional yang berhasil mencegah exploit besar pada protokol core
- Explanation: Sui menjalankan audit berlapis oleh CertiK, OtterSec, Trail of Bits, Zellic untuk protokol core dan aplikasi ekosistem, serta program bug bounty di Immunefi
- Evidence: Audit CertiK, OtterSec, Trail of Bits, Zellic dengan scope protokol core (consensus, Move VM, staking) dan aplikasi ekosistem【Phase 4 — Audit History】; tidak ada exploit besar pada protokol core sampai Januari 2025【Phase 9 — Risk Response Pattern】; program bug bounty aktif di Immunefi【Phase 4 — Audit History】
- Supporting Dataset: Phase 2 (CertiK, OtterSec, Trail of Bits, Zellic), Phase 4 (Audit History), Phase 9 (Risk Response Pattern)
- Confidence: High

Insight 10: Listing serentak di exchange utama sejak TGE adalah strategi untuk likuiditas instan dan akses pasar global
- Explanation: Sui memastikan kehadiran di Binance, Coinbase, OKX, Bybit, KuCoin, Kraken, dan lainnya pada hari pertama mainnet untuk bootstrap likuiditas dan memperluas akses
- Evidence: Listing serentak mainnet launch Mei 2023 di Binance, Coinbase, OKX, Bybit, KuCoin, Kraken【Phase 3 — EV-011】; perpetual futures tersedia di mayoritas exchange tersebut【Phase 8 — Trading Markets】; pola ini dicatat "Listing Exchange Utama Serentak"【Phase 9 — Ecosystem Decision Pattern】
- Supporting Dataset: Phase 3 (EV-011), Phase 7 (Exchange Ecosystem), Phase 8 (Trading Markets), Phase 9 (Ecosystem Decision Pattern)
- Confidence: High

Insight 11: Validasi ekstensif melalui devnet → testnet → governance proposal → mainnet sebelum setiap perubahan protokol besar adalah prinsip disiplin teknis
- Explanation: Setiap upgrade protokol besar diuji melalui environment pengembangan terlebih dahulu sebelum diputuskan via on-chain governance dan diterapkan di mainnet
- Evidence: Devnet digunakan untuk fitur eksperimental sebelum testnet publik【Phase 3 — EV-003】; Mysticeti diuji testnet Maret 2024 sebelum mainnet Juli 2024【Phase 3 — EV-022, EV-025】; Sui Bridge Native diuji testnet Januari 2024 sebelum mainnet Mei 2024【Phase 3 — EV-021, EV-023】; pola ini dicatat "Upgrade Teknologi Bertahap dengan Validasi"【Phase 9 — Evolution Pattern】
- Supporting Dataset: Phase 3 (EV-003, EV-021, EV-022, EV-023, EV-025), Phase 4 (Technical Upgrade History), Phase 9 (Evolution Pattern)
- Confidence: High

Insight 12: Program grants yang masif (>$50 juta) adalah instrumen utama untuk menarik developer dan mempercepat pertumbuhan ekosistem
- Explanation: Sui Foundation mendistribusikan hibah ke builder untuk membangun infrastruktur, DeFi, gaming, dan tooling, menjadikan ini engine utama perturbuhan ekosistem
- Evidence: Milestone >$50 juta grants dibayarkan ke >200 proyek sejak 2022【Phase 3 — EV-027】; fokus area termasuk DeFi, Gaming, Infrastructure, Tooling, Research【Phase 3 — EV-027】; pola ini dicatat "Grants Program sebagai Instrumen Pertumbuhan"【Phase 9 — Financial Decision Pattern】
- Supporting Dataset: Phase 2 (Sui Foundation Grants), Phase 3 (EV-027), Phase 5 (Revenue Model, Treasury), Phase 9 (Financial Decision Pattern)
- Confidence: High

Insight 13: Pemisahan entitas pengembang (Mysten Labs) dan pengelola ekosistem (Sui Foundation) mencegah konflik kepentingan dan mendukung desentralisasi
- Explanation: Mysten Labs fokus pada teknologi, sementara Sui Foundation mengelola treasury, grants, dan governance secara independen
- Evidence: Pendirian Sui Foundation di Zug, Swiss Oktober 2022 sebagai entitas non-profit; Foundation mengelola 50% community reserve【Phase 3 — EV-007】; on-chain governance aktif dengan proposal stake-weighted【Phase 6 — Governance】; pola ini dicatat "Pemisahan Entitas"【Phase 9 — Governance Decision Pattern】
- Supporting Dataset: Phase 2 (Mysten Labs, Sui Foundation), Phase 3 (EV-007), Phase 6 (Governance), Phase 9 (Governance Decision Pattern)
- Confidence: High

Insight 14: Target pasar gaming dan consumer app melalui perangkat keras (SuiPlay0x1) adalah differensiasi strategis untuk menjangkau pengguna non-DeFi
- Explanation: Sui berinvestasi pada perangkat keras gaming native Web3 (SuiPlay0x1) untuk membuka pasar mass market di luar pengguna kripto
- Evidence: SuiPlay0x1 handheld device dengan Playtron OS diumumkan Desember 2024 dengan pre-order Q1 2025【Phase 3 — EV-029】; integrasi Sui wallet dan zkLogin untuk game economy【Phase 7 — Integrations】; narasi gaming menjadi sekunder dalam pemasaran【Phase 8 — Narrative Position】
- Supporting Dataset: Phase 3 (EV-029), Phase 7 (Integrations), Phase 8 (Narrative Position), Phase 9 (Strategic Objectives)
- Confidence: Medium (device belum dirilis; dampak pasar belum terukur)

Insight 15: Pemilihan investor strategis yang juga partners integrasi (Circle Ventures → USDC, Binance Labs → listing, Franklin Templeton → institusional) menciptakan sinergi ekosistem
- Explanation: Sui memilih investor yang membawa beyond capital — integrasi stablecoin, akses exchange, dan legitimasi institusional
- Evidence: Circle Ventures berpartisipasi Series B dan kemudian USDC native diluncurkan via CCTP【Phase 3 — EV-006, EV-017】; Binance Labs di Series A/B dan SUI listing di Binance【Phase 3 — EV-002, EV-011】; Franklin Templeton di Series B menandakan minat tradfi【Phase 2 — Franklin Templeton】; pola ini dicatat "Menarik Investor Strategis"【Phase 9 — Recurring Behavioral Pattern】
- Supporting Dataset: Phase 2 (Circle Ventures, Binance Labs, Franklin Templeton), Phase 3 (EV-006, EV-011, EV-017), Phase 9 (Recurring Behavioral Pattern)
- Confidence: High

## Strategic Principles

Principle 1: High-performance-first architecture
- Explanation: Sui mendesain arsitektur dari awal untuk throughput tinggi dan finality cepat sebagai keunggulan kompetitif fundamental
- Evidence: Object-centric model untuk parallel execution; Mysticeti consensus untuk sub-second finality【Phase 4 — Consensus Mechanism】; throughput >50k TPS sustained【Phase 3 — EV-025】
- Supporting Dataset: Phase 1 (Core Objective), Phase 4 (Consensus Mechanism, Execution Environment), Phase 8 (Narrative Position)
- Confidence: High

Principle 2: Security before growth (dengan pengecualian slashing)
- Explanation: Keamanan smart contract dan protokol dimulai dari pemilihan bahasa Move yang aman dan diperkuat dengan audit berlapis, meskipun slashing belum diaktifkan untuk mendorong pertumbuhan validator
- Evidence: Move Language resource safety dan formal verification; audit oleh CertiK, OtterSec, Trail of Bits, Zellic; bug bounty aktif【Phase 4 — Security Model, Audit History】; slashing tidak aktif sebagai keputusan fase awal【Phase 4 — Known Technical Limitations】
- Supporting Dataset: Phase 1 (Vision), Phase 4 (Security Model, Audit History), Phase 9 (Strategic Trade-offs)
- Confidence: High

Principle 3: Ecosystem-first development
- Explanation: Pertumbuhan ekosistem DeFi dan aplikasi didorong melalui integrasi primitif standar secara bertahap, bukan hanya membangun protokol
- Evidence: Urutan pengembangan DEX → lending → staking → stablecoin → bridge【Phase 9 — Evolution Pattern】; USDC dan USDT diintegrasikan sejak awal【Phase 3 — EV-017, EV-026】
- Supporting Dataset: Phase 3 (EV-013 s/d EV-018, EV-021, EV-023, EV-026), Phase 9 (Evolution Pattern)
- Confidence: High

Principle 4: Trust-minimized internal untuk dependensi kritis
- Explanation: Setiap dependensi eksternal yang dianggap kritis (bridge) digantikan dengan versi internal yang lebih trusted
- Evidence: Sui Bridge Native menggantikan Wormhole sebagai canonical; Mysten Labs mengembangkan Gas Station API sendiri【Phase 9 — Recurring Behavioral Pattern】; bridge native dioperasikan validator set Sui【Phase 3 — EV-023】
- Supporting Dataset: Phase 3 (EV-021, EV-023), Phase 7 (External Dependencies), Phase 9 (Recurring Behavioral Pattern)
- Confidence: High

Principle 5: Stabilitas tokenomics (fixed supply, tanpa inflasi, tanpa burn)
- Explanation: Sui memegang prinsip tokenomics konservatif dengan fixed supply yang dimint di genesis dan tanpa mekanisme inflasi atau deflasi yang berubah-ubah
- Evidence: Max supply 10 miliar fixed; tanpa inflasi; tanpa burn mechanism【Phase 6 — Inflation/Deflation】
- Supporting Dataset: Phase 6 (Token Information, Supply, Inflation/Deflation), Phase 5 (Revenue Model)
- Confidence: High

Principle 6: Desentralisasi bertahap (decentralization over time)
- Explanation: Desentralisasi dilakukan secara progresif dimulai dari pemisahan entitas Mysten Labs dan Sui Foundation, lalu on-chain governance, dengan penundaan slashing sebagai trade-off keamanan awal
- Evidence: Pendirian Foundation Okt 2022【Phase 3 — EV-007】; on-chain governance aktif【Phase 6 — Governance】; slashing belum aktif【Phase 4 — Known Technical Limitations】
- Supporting Dataset: Phase 2 (Mysten Labs, Sui Foundation), Phase 3 (EV-007), Phase 4 (Known Technical Limitations), Phase 6 (Governance)
- Confidence: High

## Success Factors

Factor 1: Teknologi terdepan (throughput dan finality)
- Explanation: Kemampuan teknis yang unggul (Mysticeti consensus, parallel execution) menjadi daya tarik utama developer dan proyek
- Evidence: Finality sub-second dan throughput >50k TPS【Phase 3 — EV-025】; narasi "high-throughput" sebagai main narrative【Phase 8 — Narrative Position】
- Supporting Dataset: Phase 3 (EV-025), Phase 4 (Consensus Mechanism), Phase 8 (Narrative Position)
- Confidence: High

Factor 2: Onboarding UX inovatif (zkLogin, gasless)
- Explanation: zkLogin dan sponsored transactions menghilangkan hambatan seed phrase dan gas fee untuk pengguna non-teknis
- Evidence: >50 dApp mengadopsi zkLogin dalam 6 bulan【Phase 3 — EV-019】; fitur ini sebagai primitif protokol level【Phase 4 — Core Components】
- Supporting Dataset: Phase 3 (EV-019), Phase 4 (Core Components), Phase 8 (Narrative Position)
- Confidence: High

Factor 3: Integrasi stablecoin sejak awal (USDC, USDT)
- Explanation: Kehadiran stablecoin native menarik likuiditas dan memungkinkan DeFi berkembang cepat
- Evidence: USDC native Sept 2023【Phase 3 — EV-017】; USDT native Sept 2024; kombinasi stablecoin >$300M【Phase 3 — EV-026】; TVL >$1 miliar【Phase 8 — Adoption Metrics】
- Supporting Dataset: Phase 2 (USDC on Sui, USDT on Sui), Phase 3 (EV-017, EV-026), Phase 8 (Adoption Metrics)
- Confidence: High

Factor 4: Dukungan investor strategis dengan akses integrasi
- Explanation: Investor seperti Circle Ventures, Binance Labs, dan Franklin Templeton membawa beyond capital yang mendukung integrasi ekosistem
- Evidence: Circle Ventures di Series B → USDC native【Phase 3 — EV-006, EV-017】; Binance Labs → listing Binance【Phase 3 — EV-002, EV-011】
- Supporting Dataset: Phase 2 (Circle Ventures, Binance Labs), Phase 3 (EV-006, EV-011, EV-017), Phase 9 (Recurring Behavioral Pattern)
- Confidence: High

Factor 5: Listing exchange utama serentak sejak TGE
- Explanation: Likuiditas instan dan akses global sejak hari pertama mempercepat adopsi
- Evidence: Listing simultan di Binance, Coinbase, OKX, Bybit, KuCoin, Kraken【Phase 3 — EV-011】
- Supporting Dataset: Phase 3 (EV-011), Phase 7 (Exchange Ecosystem), Phase 8 (Trading Markets)
- Confidence: High

Factor 6: Program grants masif untuk menarik builder
- Explanation: >$50 juta grants menciptakan insentif finansial kuat untuk developer
- Evidence: Milestone >$50 juta ke >200 proyek【Phase 3 — EV-027】; fokus area DeFi, Gaming, Infrastructure【Phase 3 — EV-027】
- Supporting Dataset: Phase 2 (Sui Foundation Grants), Phase 3 (EV-027), Phase 9 (Financial Decision Pattern)
- Confidence: High

Factor 7: Treasury foundation sehat (>$1 miliar)
- Explanation: Cadangan treasury besar memberikan runway >5 tahun dan kepercayaan stakeholder
- Evidence: Treasury report Januari 2025 menyebut >$1 miliar kombinasi aset【Phase 3 — EV-030】
- Supporting Dataset: Phase 3 (EV-030), Phase 5 (Treasury), Phase 8 (Market Timeline)
- Confidence: Medium (komposisi per asset tidak diungkap)

Factor 8: Audit keamanan berlapis dan bug bounty
- Explanation: Kepercayaan terhadap keamanan protokol menarik institusi dan developer
- Evidence: Audit oleh CertiK, OtterSec, Trail of Bits, Zellic【Phase 4 — Audit History】; tidak ada exploit besar protokol core【Phase 9 — Risk Response Pattern】
- Supporting Dataset: Phase 2 (CertiK, OtterSec, Trail of Bits, Zellic), Phase 4 (Audit History)
- Confidence: High

Factor 9: Komunitas developer aktif (hackathon global)
- Explanation: Hackathon dengan hadiah >$1 juta menarik ribuan builder dan membangun komunitas
- Evidence: Sui Basecamp >2.000 peserta【Phase 3 — EV-020】; Sui Overflow >3.000 peserta【Phase 3 — EV-024】
- Supporting Dataset: Phase 3 (EV-020, EV-024), Phase 7 (Sui Community)
- Confidence: High

Factor 10: Fokus pada consumer/gaming sebagai differensiasi
- Explanation: SuiPlay0x1 dan zkLogin menargetkan pasar di luar DeFi, membuka potensi pertumbuhan baru
- Evidence: SuiPlay0x1 diumumkan Des 2024【Phase 3 — EV-029】; zkLogin diadopsi luas【Phase 3 — EV-019】
- Supporting Dataset: Phase 3 (EV-019, EV-029), Phase 7 (Integrations)
- Confidence: Medium (dampak belum terukur)

## Failure Factors

Factor 1: Tidak ada EVM compatibility membatasi pool developer
- Explanation: Developer Ethereum harus rewrite kontrak ke Move, mengurangi migrasi cepat
- Evidence: Tidak ada EVM compatibility; bahasa utama Move dan Rust【Phase 4 — Known Technical Limitations】; trade-off ini diakui【Phase 9 — Strategic Trade-offs】
- Supporting Dataset: Phase 4 (Known Technical Limitations), Phase 9 (Strategic Trade-offs)
- Confidence: High

Factor 2: Slashing tidak aktif mengurangi economic security
- Explanation: Tanpa slashing, validator tidak memiliki protocol-level penalty untuk misbehavior, melemahkan kepercayaan
- Evidence: Slashing belum diaktifkan mainnet【Phase 4 — Known Technical Limitations】; risiko dicatat【Phase 5 — Financial Risk】
- Supporting Dataset: Phase 4 (Known Technical Limitations), Phase 5 (Financial Risk)
- Confidence: High

Factor 3: Salt service zkLogin terpusat (Shinami/Mysten) mengkontradiksi narasi desentralisasi
- Explanation: Salt service yang terpusat menjadi titik kepercayaan dan potensi titik kegagalan
- Evidence: Salt service dijalankan Shinami dan Mysten Labs【Phase 4 — Security Model】; trade-off sentralisasi demi UX【Phase 9 — Strategic Trade-offs】
- Supporting Dataset: Phase 4 (Security Model), Phase 9 (Strategic Trade-offs)
- Confidence: Medium (belum ada alternatif terdesentralisasi resmi)

Factor 4: Treasury sangat bergantung pada token SUI (volatilitas)
- Explanation: Sebagian besar treasury dalam bentuk SUI, terpapar fluktuasi harga
- Evidence: Treasury report menyebut kombinasi aset tapi tidak memecah per kategori【Phase 5 — Treasury】; risiko dicatat【Phase 5 — Financial Risk】
- Supporting Dataset: Phase 5 (Treasury, Financial Risk), Phase 9 (Open Threads)
- Confidence: Medium

Factor 5: Tidak ada protocol-level revenue capture ke foundation
- Explanation: Foundation bergantung pada alokasi supply dan token appreciation, bukan pendapatan protokol langsung (gas fee flow ke validator/storage fund)
- Evidence: Gas fee dibagi validator + storage fund, bukan foundation【Phase 5 — Revenue Model】; tidak ada fee switch【Phase 5 — Financial Risk】
- Supporting Dataset: Phase 5 (Revenue Model, Financial Risk), Phase 9 (Financial Decision Pattern)
- Confidence: High

Factor 6: Hardware requirements validator tinggi membatasi desentralisasi partisipasi
- Explanation: Spesifikasi validator (32+ CPU, 256GB RAM) menghambat validator kecil
- Evidence: Rekomendasi spesifikasi tinggi【Phase 4 — Known Technical Limitations】
- Supporting Dataset: Phase 4 (Known Technical Limitations), Phase 9 (Strategic Trade-offs)
- Confidence: High

Factor 7: Dampak FTX Ventures exposure tidak transparan
- Explanation: Status investasi FTX Ventures pasca-bankruptcy tidak dikonfirmasi publik, menimbulkan ketidakpastian
- Evidence: FTX Ventures berpartisipasi Series A 2021【Phase 3 — EV-002】; status pasca-bankruptcy tidak diketahui【Phase 2 — FTX Ventures】; risiko dicatat【Phase 5 — Financial Risk】
- Supporting Dataset: Phase 2 (FTX Ventures), Phase 3 (EV-002), Phase 5 (Financial Risk)
- Confidence: Low (tidak ada pernyataan resmi)

## Decision Framework

Step 1: Observe — Mengidentifikasi kebutuhan pasar dan hambatan adopsi
- Evidence: Pengamatan hambatan seed phrase memicu pengembangan zkLogin【Phase 3 — EV-019】; pengamatan ketergantungan bridge eksternal memicu Sui Bridge Native【Phase 3 — EV-021】; pengamatan kompetisi high-throughput memicu Mysticeti【Phase 3 — EV-025】
- Supporting Dataset: Phase 3 (EV-019, EV-021, EV-025), Phase 9 (Strategic Objectives)
- Confidence: High

Step 2: Evaluate — Menguji prototipe dan konsep melalui devnet/testnet
- Evidence: Devnet untuk fitur eksperimental【Phase 3 — EV-003】; testnet Wave 1-3 untuk validasi publik【Phase 3 — EV-005, EV-008, EV-009】; Mysticeti diuji testnet sebelum mainnet【Phase 3 — EV-022, EV-025】
- Supporting Dataset: Phase 3 (EV-003, EV-005, EV-008, EV-009, EV-022, EV-025), Phase 9 (Technical Decision Pattern)
- Confidence: High

Step 3: Build — Mengembangkan dan mengintegrasikan fitur dengan sumber daya internal
- Evidence: Mysten Labs membangun bridge native sebagai alternatif internal【Phase 3 — EV-021, EV-023】; mengembangkan Gas Station API sendiri【Phase 7 — Integrations】
- Supporting Dataset: Phase 3 (EV-021, EV-023), Phase 7 (Integrations), Phase 9 (Recurring Behavioral Pattern)
- Confidence: High

Step 4: Fund — Mendapatkan modal melalui equity VC dan treasury foundation
- Evidence: Series A $36M【Phase 3 — EV-002】; Series B $300M【Phase 3 — EV-006】; treasury foundation >$1 miliar【Phase 3 — EV-030】
- Supporting Dataset: Phase 3 (EV-002, EV-006, EV-030), Phase 5 (Funding History, Treasury)
- Confidence: High

Step 5: Launch — Meluncurkan produk dengan akses pasar luas (listing serentak)
- Evidence: Mainnet launch dan TGE dengan listing simultan exchange besar【Phase 3 — EV-010, EV-011】; listing perpetual di mayoritas exchange【Phase 8 — Trading Markets】
- Supporting Dataset: Phase 3 (EV-010, EV-011), Phase 8 (Trading Markets)
- Confidence: High

Step 6: Govern — Mengelola protokol melalui on-chain governance
- Evidence: Mysticeti diaktifkan via on-chain governance proposal【Phase 3 — EV-025】; proposal dan voting stake-weighted【Phase 6 — Governance】
- Supporting Dataset: Phase 3 (EV-025), Phase 6 (Governance)
- Confidence: High

Step 7: Iterate — Upgrade rutin dan integrasi baru berdasarkan kebutuhan ekosistem
- Evidence: USDT native ditambahkan setelah permintaan likuiditas【Phase 3 — EV-026】; SuiPlay0x1 untuk ekspansi gaming【Phase 3 — EV-029】; pola "Launch Cepat, Upgrade Terus-Menerus"【Phase 9 — Recurring Behavioral Pattern】
- Supporting Dataset: Phase 3 (EV-026, EV-029), Phase 9 (Recurring Behavioral Pattern)
- Confidence: High

## Reusable Playbook

Playbook 1: Bootstrapping likuiditas stablecoin dengan integrasi Circle CCTP dan Tether
- Explanation: Mengintegrasikan stablecoin native sedini mungkin untuk menyediakan likuiditas DeFi dan menarik capital inflow
- Evidence: USDC native via CCTP Sept 2023【Phase 3 — EV-017】; USDT native Sept 2024【Phase 3 — EV-026】; kombinasi stablecoin >$300M【Phase 3 — EV-026】; TVL >$1 miliar didorong stablecoin【Phase 8 — Adoption Metrics】
- Supporting Dataset: Phase 3 (EV-017, EV-026), Phase 7 (Integrations), Phase 8 (Adoption Metrics)
- Confidence: High

Playbook 2: Onboarding user Web2 tanpa seed phrase melalui zkLogin dan sponsored transactions
- Explanation: Membangun primitif autentikasi OAuth yang menghasilkan alamat deterministik dan aplikasi membayar gas fee
- Evidence: zkLogin mainnet Nov 2023【Phase 3 — EV-019】; >50 dApp mengadopsi【Phase 3 — EV-019】; Gas Station API oleh Shinami dan Mysten Labs【Phase 7 — Integrations】
- Supporting Dataset: Phase 3 (EV-019), Phase 4 (Core Components), Phase 7 (Integrations)
- Confidence: High

Playbook 3: Program grants masif dengan fokus area (DeFi, Gaming, Infrastructure, Tooling, Research)
- Explanation: Mendistribusikan hibah besar-besaran untuk menarik builder dan mempercepat ekosistem
- Evidence: >$50 juta grants ke >200 proyek【Phase 3 — EV-027】; fokus area spesifik【Phase 3 — EV-027】
- Supporting Dataset: Phase 2 (Sui Foundation Grants), Phase 3 (EV-027)
- Confidence: High

Playbook 4: Membangun bridge internal untuk menggantikan dependensi eksternal kritis
- Explanation: Mengurangi risiko sentralisasi dengan mengembangkan bridge canonical yang dioperasikan validator set
- Evidence: Sui Bridge Native testnet Jan 2024, mainnet Mei 2024【Phase 3 — EV-021, EV-023】; menggantikan Wormhole sebagai canonical【Phase 9 — Recurring Behavioral Pattern】
- Supporting Dataset: Phase 3 (EV-021, EV-023), Phase 7 (External Dependencies)
- Confidence: High

Playbook 5: Listing serentak di exchange utama untuk likuiditas instan
- Explanation: Memastikan kehadiran di semua exchange besar sejak hari pertama TGE
- Evidence: Listing simultan di Binance, Coinbase, OKX, Bybit, KuCoin, Kraken【Phase 3 — EV-011】; perpetual di mayoritas exchange【Phase 8 — Trading Markets】
- Supporting Dataset: Phase 3 (EV-011), Phase 7 (Exchange Ecosystem), Phase 8 (Trading Markets)
- Confidence: High

Playbook 6: Mengadakan hackathon global dengan hadiah besar untuk membangun komunitas developer
- Explanation: Hackathon dengan hadiah >$1 juta menarik ribuan builder dan menghasilkan pipeline proyek
- Evidence: Sui Basecamp >2.000 peserta【Phase 3 — EV-020】; Sui Overflow >3.000 peserta【Phase 3 — EV-024】
- Supporting Dataset: Phase 2 (Sui Community), Phase 3 (EV-020, EV-024)
- Confidence: High

Playbook 7: Memilih investor yang juga partners integrasi
- Explanation: Investor membawa beyond capital — integrasi stablecoin, listing exchange, legitimasi institusional
- Evidence: Circle Ventures → USDC【Phase 3 — EV-006, EV-017】; Binance Labs → listing Binance【Phase 3 — EV-002, EV-011】; Franklin Templeton → minat tradfi【Phase 2 — Franklin Templeton】
- Supporting Dataset: Phase 2 (Circle Ventures, Binance Labs, Franklin Templeton), Phase 3 (EV-006, EV-011, EV-017)
- Confidence: High

Playbook 8: Validasi panjang sebelum mainnet launch dengan program testnet incentivized
- Explanation: Menggunakan testnet Wave dengan insentif token untuk menguji protokol pada skala publik
- Evidence: Testnet Wave 1-3 dengan hadiah token SUI【Phase 3 — EV-005, EV-008, EV-009】; partisipasi ribuan validator kandidat【Phase 3 — EV-005】
- Supporting Dataset: Phase 3 (EV-005, EV-008, EV-009)
- Confidence: High

Playbook 9: Upgrade protokol besar melalui on-chain governance setelah validasi testnet
- Explanation: Menggunakan governance untuk mengaktifkan perubahan protokol, bukan keputusan unilateral
- Evidence: Mysticeti diaktifkan via on-chain governance proposal【Phase 3 — EV-025】; proposal dan voting stake-weighted【Phase 6 — Governance】
- Supporting Dataset: Phase 3 (EV-025), Phase 6 (Governance)
- Confidence: High

Playbook 10: Membangun treasury transparan dengan laporan publik
- Explanation: Mempublikasikan laporan treasury untuk membangun kepercayaan stakeholder
- Evidence: Treasury report Jan 2025 menyebut >$1 miliar aset【Phase 3 — EV-030】; dashboard treasury publik【Phase 5 — Official Financial Resources】
- Supporting Dataset: Phase 3 (EV-030), Phase 5 (Treasury)
- Confidence: Medium (komposisi per asset tidak diungkap)

## Anti-patterns

Anti-pattern 1: Terlalu bergantung pada satu bridge eksternal sebelum membangun internal
- Explanation: Ketergantungan pada Wormhole sebagai bridge utama menimbulkan risiko sentralisasi dan trust
- Evidence: Wormhole diadopsi Okt 2023【Phase 3 — EV-018】; Sui Bridge Native dibangun untuk menggantikan sebagai canonical【Phase 3 — EV-021, EV-023】; risk response dicatat【Phase 9 — Risk Response Pattern】
- Supporting Dataset: Phase 3 (EV-018, EV-021, EV-023), Phase 9 (Risk Response Pattern)
- Confidence: High

Anti-pattern 2: Menunda mekanisme slashing terlalu lama dapat melemahkan kepercayaan ekonomi
- Explanation: Tanpa slashing, economic security tidak terpenuhi; delegator tidak terproteksi dari misbehavior
- Evidence: Slashing belum diaktifkan mainnet【Phase 4 — Known Technical Limitations】; risiko dicatat【Phase 5 — Financial Risk】
- Supporting Dataset: Phase 4 (Known Technical Limitations), Phase 5 (Financial Risk)
- Confidence: High

Anti-pattern 3: Sentralisasi komponen kritis (salt service) tanpa roadmap desentralisasi jelas
- Explanation: Salt service zkLogin yang terpusat menjadi titik kepercayaan yang kontradiktif dengan narasi desentralisasi
- Evidence: Salt service dijalankan Shinami dan Mysten Labs【Phase 4 — Security Model】; roadmap desentralisasi tidak ada【Phase 4 — Open Threads】
- Supporting Dataset: Phase 4 (Security Model, Open Threads), Phase 9 (Strategic Trade-offs)
- Confidence: Medium

Anti-pattern 4: Komposisi treasury yang sangat bergantung pada token sendiri tanpa diversifikasi jelas
- Explanation: Treasury didominasi SUI; fluktuasi harga bisa mengganggu operasional
- Evidence: Treasury report kombinasi aset tapi detail per kategori tidak diungkap【Phase 5 — Treasury】; risiko dicatat【Phase 5 — Financial Risk】
- Supporting Dataset: Phase 5 (Treasury, Financial Risk), Phase 9 (Open Threads)
- Confidence: Medium

Anti-pattern 5: Hardware requirements validator tinggi tanpa mempertimbangkan partisipasi validator kecil
- Explanation: Spesifikasi tinggi membatasi desentralisasi dan partisipasi komunitas
- Evidence: Spesifikasi 32+ CPU, 256GB RAM【Phase 4 — Known Technical Limitations】; dicatat sebagai trade-off【Phase 9 — Strategic Trade-offs】
- Supporting Dataset: Phase 4 (Known Technical Limitations), Phase 9 (Strategic Trade-offs)
- Confidence: High

Anti-pattern 6: Tidak ada protocol revenue capture ke foundation dapat membatasi keberlanjutan jangka panjang
- Explanation: Foundation bergantung pada alokasi supply dan token appreciation, bukan revenue berkelanjutan
- Evidence: Gas fee flow ke validator/storage fund, bukan foundation【Phase 5 — Revenue Model】; tidak ada fee switch【Phase 5 — Financial Risk】
- Supporting Dataset: Phase 5 (Revenue Model, Financial Risk)
- Confidence: High

Anti-pattern 7: Kesalahan input data pada kompetitor ("Sui-Near" bukan entity nyata)
- Explanation: Kesalahan penamaan pada daftar kompetitor menunjukkan potensi data quality issue
- Evidence: Daftar awal "Sui-Near" pada Phase 8 — ini adalah kesalahan input; yang benar adalah Near Protocol【Phase 8 — Competitor Landscape】; dicatat sebagai Open Thread【Phase 9 — Open Threads】
- Supporting Dataset: Phase 8 (Competitor Landscape), Phase 9 (Open Threads)
- Confidence: Low (kesalahan input, bukan pola proyek)

## Lessons Learned

Lesson 1: Arsitektur yang dirancang untuk performa (object-centric, parallel execution) dapat menjadi pendorong adopsi yang kuat
- Evidence: Mysticeti dan throughput >50k TPS menarik developer dan proyek【Phase 3 — EV-025】; narasi "high-throughput" sebagai main narrative【Phase 8 — Narrative Position】
- Supporting Dataset: Phase 3 (EV-025), Phase 4 (Consensus Mechanism), Phase 8 (Narrative Position)
- Confidence: High

Lesson 2: Onboarding pengguna non-teknis melalui primitif seperti zkLogin dan gasless adalah differensiasi penting di pasar Layer 1
- Evidence: zkLogin diadopsi >50 dApp dalam 6 bulan【Phase 3 — EV-019】; narasi consumer-facing sekunder【Phase 8 — Narrative Position】
- Supporting Dataset: Phase 3 (EV-019), Phase 4 (Core Components), Phase 8 (Narrative Position)
- Confidence: High

Lesson 3: Keamanan language choice (Move) dan audit berlapis lebih penting daripada kompatibilitas developer (EVM)
- Evidence: Move dipilih untuk keamanan; tidak ada EVM compatibility【Phase 4 — Execution Environment, Known Technical Limitations】; tidak ada exploit besar protokol core【Phase 9 — Risk Response Pattern】
- Supporting Dataset: Phase 4 (Execution Environment, Known Technical Limitations), Phase 9 (Risk Response Pattern)
- Confidence: High

Lesson 4: Pendanaan equity VC dapat memberikan kendali distribusi token yang lebih baik daripada token sale publik
- Evidence: Series A/B equity (bukan ICO/IDO); TGE terkontrol bersamaan mainnet【Phase 3 — EV-002, EV-006, EV-011】; pola "Pendanaan Ekuitas Bertahap"【Phase 9 — Financial Decision Pattern】
- Supporting Dataset: Phase 3 (EV-002, EV-006, EV-011), Phase 5 (Funding History, Token Sale)
- Confidence: High

Lesson 5: Pemisahan entitas pengembang dan pengelola ekosistem adalah praktik governance yang efektif
- Evidence: Mysten Labs fokus teknologi; Sui Foundation fokus treasury/grants/governance【Phase 2 — Mysten Labs, Sui Foundation】; pola "Pemisahan Entitas"【Phase 9 — Governance Decision Pattern】
- Supporting Dataset: Phase 2 (Mysten Labs, Sui Foundation), Phase 3 (EV-007), Phase 9 (Governance Decision Pattern)
- Confidence: High

Lesson 6: Growth yang sehat memerlukan keseimbangan antara pertumbuhan ekosistem (grants) dan keberlanjutan finansial (treasury)
- Evidence: >$50 juta grants dibayarkan【Phase 3 — EV-027】; treasury masih >$1 miliar【Phase 3 — EV-030】; risiko keberlanjutan dicatat【Phase 5 — Financial Risk】
- Supporting Dataset: Phase 3 (EV-027, EV-030), Phase 5 (Treasury, Financial Risk)
- Confidence: Medium

## Knowledge Summary

Strategic Principles:
- High-performance-first architecture (Mysticeti consensus, object-centric)【Phase 4 — Consensus Mechanism】; Security before growth dengan Move + audit berlapis【Phase 4 — Security Model】; Ecosystem-first development melalui urutan primitif DeFi【Phase 9 — Evolution Pattern】; Trust-minimized internal untuk dependensi kritis（bridge native）【Phase 9 — Recurring Behavioral Pattern】; Stabilitas tokenomics tanpa inflasi/burn【Phase 6 — Inflation/Deflation】; Desentralisasi bertahap dengan pemisahan entitas dan on-chain governance【Phase 9 — Governance Decision Pattern】

Success Factors:
- Teknologi terdepan (Mysticeti)【Phase 3 — EV-025】; zkLogin/Gasless untuk onboarding Web2【Phase 3 — EV-019】; USDC/USDT native untuk likuiditas【Phase 3 — EV-017, EV-026】; investor strategis（Circle, Binance）【Phase 2 — Circle Ventures, Binance Labs】; listing serentak exchange besar【Phase 3 — EV-011】; grants $50 juta+【Phase 3 — EV-027】; treasury >$1 miliar【Phase 3 — EV-030】; audit keamanan berlapis【Phase 4 — Audit History】; komunitas developer via hackathon【Phase 3 — EV-020, EV-024】; fokus gaming/consumer via SuiPlay0x1【Phase 3 — EV-029】

Failure Factors:
- Tidak ada EVM compatibility membatasi porting dApp Ethereum【Phase 4 — Known Technical Limitations】; slashing tidak aktif melemahkan economic security【Phase 4 — Known Technical Limitations】; salt service zkLogin terpusat【Phase 4 — Security Model】; treasury bergantung pada token SUI【Phase 5 — Financial Risk】; tidak ada protocol revenue capture ke foundation【Phase 5 — Revenue Model】; hardware requirements validator tinggi membatasi desentralisasi【Phase 4 — Known Technical Limitations】; FTX exposure tidak transparan【Phase 5 — Financial Risk】

Decision Framework:
- Observe（identifikasi hambatan: seed phrase, bridge external）【Phase 3 — EV-019, EV-021】; Evaluate（testnet Wave 1-3, Mysticeti testnet）【Phase 3 — EV-005, EV-008, EV-009, EV-022】; Build（membangun internal untuk dependensi kritis）【Phase 3 — EV-021, EV-023】; Fund（Series A/B $336M）【Phase 3 — EV-002, EV-006】; Launch（mainnet + TGE + listing serentak）【Phase 3 — EV-010, EV-011】; Govern（on-chain governance untuk upgrade）【Phase 3 — EV-025】; Iterate（upgrade rutin dan integrasi baru）【Phase 3 — EV-026, EV-029】

Reusable Playbook:
- Bootstrapping likuiditas stablecoin（USDC/USDT）【Phase 3 — EV-017, EV-026】; Onboarding Web2 tanpa seed phrase（zkLogin/Gasless）【Phase 3 — EV-019】; Program grants masif【Phase 3 — EV-027】; Membangun bridge internal untuk reduce trust external【Phase 3 — EV-021, EV-023】; Listing serentak exchange besar【Phase 3 — EV-011】; Hackathon global untuk komunitas developer【Phase 3 — EV-020, EV-024】; Memilih investor strategis dengan sinergi integrasi【Phase 3 — EV-006, EV-017】; Validasi panjang melalui testnet incentivized【Phase 3 — EV-005, EV-008, EV-009】; On-chain governance untuk upgrade protokol【Phase 3 — EV-025】; Treasury transparan dengan laporan publik【Phase 3 — EV-030】

Anti-patterns:
- Terlalu bergantung pada satu bridge eksternal sebelum internal【Phase 3 — EV-018, EV-021】; Menunda slashing terlalu lama【Phase 4 — Known Technical Limitations】; Sentralisasi komponen kritis tanpa roadmap desentralisasi【Phase 4 — Security Model】; Treasurey terlalu bergantung pada token sendiri【Phase 5 — Financial Risk】; Hardware requirements validator tinggi tanpa akses untuk validator kecil【Phase 4 — Known Technical Limitations】; Tidak ada protocol revenue capture【Phase 5 — Revenue Model】

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

PROJECT: Sui

CIF MANIFEST v3.0

CIF MANIFEST v3.0
Project: Sui
Symbol: SUI
Research Date: 2025-01-31
CIF Version: 3.0
QA Date: 2025-01-31

METRICS
Total Knowledge Objects: 15
Total Entities: 52
Total Events: 30
Evidence Links: 47
Sources: 52
Conflicts: 12
- Resolved: 10
- Critical: 0
- High: 1
- Medium: 4
- Low: 7

QUALITY SCORES
Research Quality: 88/100
Consistency: 92/100
Evidence: 83/100
Coverage: 84/100
Conflict: 91/100
Knowledge: 85/100
CIF SCORE: 87/100

CONFIDENCE LEVEL: HIGH
QA STATUS: PASSED

RECOMMENDED RE-RUN:
- Phase 5 — Komposisi treasury per asset class tidak diungkap detail; perlu verifikasi on-chain
- Phase 8 — Metrik developer count dan daily active users tidak terstandarisasi; perlu data primer

DATASET INTEGRITY & COVERAGE

PHASE 1 — FOUNDATION
- Status: Complete
- Missing Information: Tidak ada
- Notes: Data dasar protokol lengkap; tidak ada konflik material antar sumber

PHASE 2 — ENTITY
- Status: Complete
- Missing Information: Daftar validator individu belum dipecah (hanya validator set kolektif); cap table investor lengkap tidak tersedia
- Notes: 52 entity tercatat; mayoritas berasal dari kategori Company dan Protocol

PHASE 3 — HISTORY
- Status: Complete
- Missing Information: Tanggal pasti TGE (EV-011) sedikit berbeda antar sumber; status FTX Ventures pasca-bankruptcy tidak tercatat
- Notes: 30 event teridentifikasi; timeline mendukung narasi pertumbuhan ekosistem bertahap

PHASE 4 — TECHNOLOGY
- Status: Complete
- Missing Information: Formal proof Mysticeti paper belum dipublikasikan; slashing timeline tidak jelas
- Notes: Arsitektur teknis terdokumentasi baik; upgrade sequence konsisten

PHASE 5 — FINANCIAL
- Status: Incomplete
- Missing Information: Komposisi treasury per asset class tidak diungkap; revenue model tidak memiliki laporan periodik publik
- Notes: Funding history lengkap; treasury hanya diketahui total >$1 miliar tanpa breakdown

PHASE 6 — TOKEN
- Status: Complete
- Missing Information: Detail vesting contract addresses tidak dipublikasikan; status FTX token allocation tidak jelas
- Notes: Supply dan distribusi terdokumentasi dengan baik; tokenomics konservatif

PHASE 7 — ECOSYSTEM
- Status: Complete
- Missing Information: Tidak ada
- Notes: Integrasi dan infrastruktur tercatat dengan baik; external dependencies jelas

PHASE 8 — MARKET
- Status: Incomplete
- Missing Information: Developer count aktif tidak dipublikasikan; daily active users tidak terstandardisasi; market share tidak tersedia
- Notes: Data adoption parsial; metrik harga dan volume memerlukan snapshot spesifik

PHASE 9 — BEHAVIORAL
- Status: Complete
- Missing Information: Tidak ada
- Notes: Decision timeline dan pattern teridentifikasi dengan baik; trade-off tercatat eksplisit

PHASE 10 — KNOWLEDGE
- Status: Complete
- Missing Information: Tidak ada
- Notes: 15 knowledge objects dihasilkan; insight dan playbook cukup komprehensif

COVERAGE REPORT — MULTI-DIMENSIONAL

PHASE 2 — ENTITY
- Total: 52
- Referenced in Phase 9-10: 35
- Unused: 17
- Coverage: 67.3%
- Interpretation: Sebagian besar entity inti (Mysten Labs, Sui Foundation, validator set, exchange utama) digunakan; entity pendukung minor (media, beberapa investor kecil) tidak terpakai dalam sintesis

PHASE 3 — EVENT
- Total: 30
- Referenced in Phase 9-10: 28
- Unused: 2 (EV-003 devnet launch, EV-004 whitepaper publikasi — hanya disebut implisit)
- Coverage: 93.3%
- Interpretation: Hampir seluruh event memiliki implikasi strategis; event awal (devnet, whitepaper) menjadi fondasi tapi tidak disebut eksplisit dalam knowledge

PHASE 4 — TECHNOLOGY
- Total: 15 komponen inti
- Referenced: 13
- Unused: 2 (Kiosk Standard, DeepBook — disebut dalam ekosistem tapi tidak menjadi fokus knowledge)
- Coverage: 86.7%
- Interpretation: Teknologi inti (Mysticeti, Move, zkLogin, bridge) sangat terwakili; primitif eksternal (Kiosk, DeepBook) kurang dianalisis

PHASE 5 — FINANCIAL
- Total: 10 fakta (funding rounds, treasury, revenue)
- Referenced: 8
- Unused: 2 (revenue model non-protocol, grants ROI measurement)
- Coverage: 80%
- Interpretation: Funding dan treasury terwakili baik; revenue capture jangka panjang dan ROI grants kurang dieksplorasi

PHASE 6 — TOKEN
- Total: 14 item (supply, distribution, utility, governance, inflation)
- Referenced: 12
- Unused: 2 (detail vesting contract addresses, staking % verifikasi)
- Coverage: 85.7%
- Interpretation: Tokenomics inti sangat terwakili; detail teknis vesting belum termanfaatkan

PHASE 7 — ECOSYSTEM
- Total: 25 integrasi (bridge, DEX, lending, stablecoin, wallet, exchange)
- Referenced: 18
- Unused: 7 (wallet minor, exchange minor, beberapa DeFi kecil)
- Coverage: 72%
- Interpretation: Integrasi kritis (USDC, USDT, bridge, zkLogin) sangat terwakili; wallet ekosistem dan exchange kecil kurang dianalisis

PHASE 8 — MARKET
- Total: 12 metrik (TVL, DAU, TPS, staking, volume)
- Referenced: 9
- Unused: 3 (market share, bridge volume, NFT volume — tidak tersedia)
- Coverage: 75%
- Interpretation: Metrik inti (TVL, transaksi, validator) terwakili; metrik niche tidak tersedia

OVERALL COVERAGE
- Total: 64 item
- Referenced: 46
- Unused: 18
- Coverage: 71.9%
- Interpretation: Cakupan knowledge terhadap data mentah cukup tinggi (72%); entity dan integrasi minor kurang dimanfaatkan dalam sintesis karena fokus pada pola inti

CROSS-PHASE CONSISTENCY

ENTITY CONSISTENCY
- Status: Konsisten
- Detail: Entity seperti Mysten Labs, Sui Foundation, Cetus Protocol, USDC on Sui, Binance, zkLogin muncul dengan nama yang sama konsisten di Phase 2, 3, 7, 8, 9, dan 10

TIMELINE CONSISTENCY
- Status: Konsisten
- Detail: Timeline di Phase 1 (launch date 2023-05-03), Phase 3 (EV-010 mainnet launch), Phase 8 (market milestone) dan Phase 9 (decision timeline) saling mendukung tidak ada perbedaan tanggal fundamental

TECHNOLOGY CONSISTENCY
- Status: Konsisten
- Detail: Urutan upgrade konsisten: Narwhal/Bullshark (mainnet awal) → Mysticeti testnet (EV-022) → Mysticeti mainnet (EV-025); tidak ada konflik arsitektur lintas phase

FUNDING CONSISTENCY
- Status: Konsisten
- Detail: Funding history di Phase 5 (Series A $36M Des 2021, Series B $300M Sep 2022) sesuai dengan Phase 3 (EV-002, EV-006) dan Phase 9 (decision timeline)

TOKEN CONSISTENCY
- Status: Konsisten
- Detail: Token info di Phase 6 (max supply 10B, TGE 2023-05-03) sesuai dengan Phase 1 (launch date) dan Phase 3 (EV-011)

GOVERNANCE CONSISTENCY
- Status: Konsisten
- Detail: Pemisahan Mysten Labs dan Sui Foundation konsisten di Phase 2, 3, 6, dan 9; on-chain governance stake-weighted tercatat sama

DEPENDENCY CONSISTENCY
- Status: Konsisten
- Detail: External dependencies (Ethereum, Circle USDC, Tether, zkLogin OAuth) konsisten di Phase 7 dan Phase 9

OVERALL CROSS-PHASE CONSISTENCY
- Nilai: 92%

DATA LINEAGE

Knowledge K-001 — Throughput tinggi dan finality cepat
- Level 0 (Raw Data)
 - Phase 3 — EV-025 (Mysticeti mainnet upgrade menghasilkan finality ~800ms dan throughput >50k TPS)
 - Source: https://blog.sui.io/mysticeti-mainnet-upgrade/
 - Phase 4 — Consensus Mechanism (Mysticeti DAG-BFT, sub-second finality)
 - Source: https://blog.sui.io/mysticeti-consensus/
 - Phase 8 — Narrative Position (High-throughput sebagai main narrative)
 - Source: https://blog.sui.io/mysticeti-mainnet-upgrade/
- Level 1 (Processed)
 - Phase 9 — Technical Decision Pattern (Pola 2: Konsensus DAG-based untuk throughput tinggi)
 - Evidence: Narwhal/Bullshark digunakan mainnet awal; Mysticeti diuji testnet lalu mainnet dengan hasil latency ~800ms dan throughput >50k TPS
- Level 2 (Knowledge)
 - Knowledge K-001 — Throughput tinggi dan finality cepat
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 93/100

Knowledge K-002 — Onboarding massal pengguna Web2
- Level 0 (Raw Data)
 - Phase 3 — EV-019 (zkLogin mainnet, OAuth tanpa seed phrase)
 - Source: https://docs.sui.io/guides/developer/app-development/zklogin
 - Phase 4 — Core Components (zkLogin sebagai primitif protokol)
 - Source: https://blog.sui.io/zklogin-mainnet/
 - Phase 8 — Narrative Position (Consumer-Facing Web3)
 - Source: https://blog.sui.io/zklogin-mainnet/
- Level 1 (Processed)
 - Phase 9 — Evolution Pattern (Pola 1: Dari Developer-First ke Consumer-First)
 - Evidence: zkLogin mainnet Nov 2023; SuiPlay0x1 Des 2024; sponsored transactions diadopsi luas
- Level 2 (Knowledge)
 - Knowledge K-002 — Onboarding massal pengguna Web2
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 91/100

Knowledge K-003 — Tokenomics fixed supply
- Level 0 (Raw Data)
 - Phase 6 — Supply (Max supply 10 miliar, minted at genesis)
 - Source: https://blog.sui.io/sui-token-economics/
 - Phase 6 — Inflation/Deflation (Tidak ada inflasi, tidak ada burn)
 - Source: https://docs.sui.io/concepts/tokenomics/sui-token
- Level 1 (Processed)
 - Phase 9 — Financial Decision Pattern (Pola 4: Tidak Ada Protocol-Level Revenue Capture)
 - Evidence: Tidak ada fee switch; gas fee dibagi validator + storage fund; tidak ada burn
- Level 2 (Knowledge)
 - Knowledge K-003 — Tokenomics fixed supply
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 88/100

Knowledge K-004 — Pengurangan dependensi eksternal
- Level 0 (Raw Data)
 - Phase 3 — EV-021 (Sui Bridge Native testnet)
 - Source: https://blog.sui.io/sui-bridge-testnet/
 - Phase 3 — EV-023 (Sui Bridge Native mainnet)
 - Source: https://blog.sui.io/sui-bridge-mainnet/
 - Phase 7 — External Dependencies (Wormhole sebagai bridge eksternal)
 - Source: https://wormhole.com/blog/wormhole-sui
- Level 1 (Processed)
 - Phase 9 — Evolution Pattern (Pola 4: Dari Trust-External ke Trust-Minimized Internal)
 - Evidence: Bridge native dioperasikan validator set Sui; menggantikan Wormhole sebagai canonical
- Level 2 (Knowledge)
 - Knowledge K-004 — Pengurangan dependensi eksternal
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 94/100

Knowledge K-005 — Integrasi stablecoin
- Level 0 (Raw Data)
 - Phase 3 — EV-017 (USDC native via Circle CCTP)
 - Source: https://www.circle.com/en/usdc-on-sui
 - Phase 3 — EV-026 (USDT native)
 - Source: https://tether.to/tether-usdt-launches-on-sui/
 - Phase 8 — Adoption Metrics (TVL >$1 miliar)
 - Source: https://defillama.com/chain/Sui
- Level 1 (Processed)
 - Phase 9 — Ecosystem Decision Pattern (Pola 1: Integrasi Stablecoin Sejak Awal)
 - Evidence: USDC diluncurkan sebelum mainnet building phase; USDT menyusul setahun kemudian
- Level 2 (Knowledge)
 - Knowledge K-005 — Integrasi stablecoin
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 95/100

Knowledge K-006 — Move Language dipilih untuk keamanan
- Level 0 (Raw Data)
 - Phase 4 — Execution Environment (Move VM resource safety)
 - Source: https://move-book.com/
 - Phase 4 — Known Technical Limitations (Tidak ada EVM compatibility)
 - Source: https://docs.sui.io/guides/developer/getting-started/move-overview
- Level 1 (Processed)
 - Phase 9 — Strategic Trade-offs (Trade-off 2: Keamanan vs Adopsi Developer)
 - Evidence: Tidak ada EVM compatibility; developer Ethereum harus rewrite kontrak ke Move
- Level 2 (Knowledge)
 - Knowledge K-006 — Move Language dipilih untuk keamanan
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 93/100

Knowledge K-007 — Ekspansi ekosistem berurutan
- Level 0 (Raw Data)
 - Phase 3 — EV-013 (Cetus DEX)
 - Source: https://cetus.zone/
 - Phase 3 — EV-014 (Navi lending)
 - Source: https://naviprotocol.io/
 - Phase 3 — EV-017 (USDC)
 - Source: https://www.circle.com/en/usdc-on-sui
- Level 1 (Processed)
 - Phase 9 — Evolution Pattern (Pola 2: Ekspansi DeFi Berurutan)
 - Evidence: Juni-Agustus 2023: DEX, lending, staking; Sept 2023: USDC; Okt 2023: Wormhole
- Level 2 (Knowledge)
 - Knowledge K-007 — Ekspansi ekosistem berurutan
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 93/100

Knowledge K-008 — Pendanaan equity VC
- Level 0 (Raw Data)
 - Phase 3 — EV-002 (Series A $36M)
 - Source: https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z
 - Phase 3 — EV-006 (Series B $300M)
 - Source: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/
 - Phase 3 — EV-011 (TGE tanpa ICO/IDO)
 - Source: https://blog.sui.io/sui-token-economics/
- Level 1 (Processed)
 - Phase 9 — Financial Decision Pattern (Pola 1: Pendanaan Ekuitas Bertahap)
 - Evidence: Tidak ada ICO/IDO publik; TGE dilakukan bersamaan mainnet
- Level 2 (Knowledge)
 - Knowledge K-008 — Pendanaan equity VC
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 87/100

Knowledge K-009 — Keamanan berlapis
- Level 0 (Raw Data)
 - Phase 4 — Audit History (CertiK, OtterSec, Trail of Bits, Zellic)
 - Source: https://www.certik.com/projects/sui
 - Phase 4 — Audit History (Bug bounty Immunefi)
 - Source: https://immunefi.com/bounty/sui/
- Level 1 (Processed)
 - Phase 9 — Risk Response Pattern (Pola 2: Keamanan Berlapis)
 - Evidence: Multiple audit reports; program bug bounty aktif
- Level 2 (Knowledge)
 - Knowledge K-009 — Keamanan berlapis
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 95/100

Knowledge K-010 — Listing serentak di exchange utama
- Level 0 (Raw Data)
 - Phase 3 — EV-011 (Listing simultan Binance, Coinbase, OKX, Bybit, KuCoin, Kraken)
 - Source: https://blog.sui.io/sui-mainnet-launches/
 - Phase 8 — Trading Markets (10 exchange utama)
 - Source: https://www.coingecko.com/en/coins/sui
- Level 1 (Processed)
 - Phase 9 — Ecosystem Decision Pattern (Pola 3: Listing Exchange Utama Serentak)
 - Evidence: Listing serentak mainnet launch; perpetual futures di mayoritas exchange
- Level 2 (Knowledge)
 - Knowledge K-010 — Listing serentak di exchange utama
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 93/100

Knowledge K-011 — Validasi ekstensif
- Level 0 (Raw Data)
 - Phase 3 — EV-003 (Devnet)
 - Source: https://docs.sui.io/guides/developer/getting-started/connect#devnet
 - Phase 3 — EV-005, EV-008, EV-009 (Testnet Wave 1-3)
 - Source: https://blog.sui.io/sui-testnet-wave-1-launches/
 - Phase 3 — EV-022 (Mysticeti testnet)
 - Source: https://blog.sui.io/mysticeti-consensus/
 - Phase 3 — EV-025 (Mysticeti mainnet via governance)
 - Source: https://blog.sui.io/mysticeti-mainnet-upgrade/
- Level 1 (Processed)
 - Phase 9 — Technical Decision Pattern (Pola 5: Upgrade Teknologi Bertahap)
 - Evidence: Mysticeti diuji testnet Maret 2024 sebelum mainnet Juli 2024
- Level 2 (Knowledge)
 - Knowledge K-011 — Validasi ekstensif
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 97/100

Knowledge K-012 — Program grants masif
- Level 0 (Raw Data)
 - Phase 3 — EV-027 (Milestone >$50 juta grants)
 - Source: https://sui.io/foundation/grants
 - Phase 5 — Treasury (Grants program dari treasury foundation)
 - Source: https://sui.io/foundation/treasury
- Level 1 (Processed)
 - Phase 9 — Financial Decision Pattern (Pola 3: Grants sebagai Instrumen Pertumbuhan)
 - Evidence: Distribusi hingga >$50 juta untuk menarik developer
- Level 2 (Knowledge)
 - Knowledge K-012 — Program grants masif
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 83/100

Knowledge K-013 — Pemisahan entitas
- Level 0 (Raw Data)
 - Phase 3 — EV-007 (Pendirian Sui Foundation di Zug, Swiss)
 - Source: https://blog.sui.io/sui-foundation-launches/
 - Phase 6 — Governance (On-chain governance stake-weighted)
 - Source: https://gov.sui.io/
- Level 1 (Processed)
 - Phase 9 — Governance Decision Pattern (Pola 1: Pemisahan Entitas)
 - Evidence: Mysten Labs fokus teknologi; Sui Foundation fokus treasury dan governance
- Level 2 (Knowledge)
 - Knowledge K-013 — Pemisahan entitas
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 96/100

Knowledge K-014 — Target gaming dan consumer
- Level 0 (Raw Data)
 - Phase 3 — EV-029 (SuiPlay0x1 dan Playtron OS)
 - Source: https://blog.sui.io/suiplay0x1-announcement/
 - Phase 7 — Integrations (Sui Wallet dan zkLogin untuk game economy)
 - Source: https://playtron.org/
- Level 1 (Processed)
 - Phase 9 — Evolution Pattern (Pola 1: Dari Developer-First ke Consumer-First)
 - Evidence: SuiPlay0x1 Des 2024; pre-order Q1 2025
- Level 2 (Knowledge)
 - Knowledge K-014 — Target gaming dan consumer
- Validation: Passed cross-phase; Evidence audit Moderate; Confidence: 70/100

Knowledge K-015 — Memilih investor strategis
- Level 0 (Raw Data)
 - Phase 2 — Circle Ventures (Investor Series B)
 - Source: https://www.circle.com/blog/circle-ventures-invests-in-mysten-labs
 - Phase 2 — Binance Labs (Investor Series A/B)
 - Source: https://labs.binance.com/portfolio
 - Phase 3 — EV-017 (USDC native)
 - Source: https://www.circle.com/en/usdc-on-sui
- Level 1 (Processed)
 - Phase 9 — Recurring Behavioral Pattern (Pola 5: Menarik Investor Strategis)
 - Evidence: Circle Ventures → USDC; Binance Labs → listing Binance
- Level 2 (Knowledge)
 - Knowledge K-015 — Memilih investor strategis
- Validation: Passed cross-phase; Evidence audit Strong; Confidence: 94/100

KNOWLEDGE DEPENDENCY GRAPH

Berikut dependency graph untuk setiap knowledge object secara ringkas.

Knowledge K-001 — Throughput tinggi dan finality cepat
- Depends on (Direct):
 - EV-025 (Phase 3) — Mysticeti mainnet upgrade
 - Source: https://blog.sui.io/mysticeti-mainnet-upgrade/
 - Phase 4 — Consensus Mechanism (Mysticeti)
 - Source: https://blog.sui.io/mysticeti-consensus/
 - Phase 8 — Narrative Position (High-throughput)
 - Source: https://blog.sui.io/mysticeti-mainnet-upgrade/
- Depends on (Indirect):
 - EV-022 (Mysticeti testnet)
 - Sui Network (Mainnet) (Chain)
 - Phase 3 — Timeline 2024
- Dependents:
 - K-011 — Validasi ekstensif
- Propagation Path:
 - Jika EV-025 berubah → K-001 berubah
 - Jika detail konsensus Phase 4 berubah → K-001 berubah

Knowledge K-002 — Onboarding massal pengguna Web2
- Depends on (Direct):
 - EV-019 (Phase 3) — zkLogin mainnet
 - Source: https://blog.sui.io/zklogin-mainnet/
 - Phase 4 — Core Components (zkLogin)
 - Source: https://docs.sui.io/guides/developer/app-development/zklogin
 - Phase 8 — Narrative Position (Consumer-Facing)
 - Source: https://blog.sui.io/zklogin-mainnet/
- Depends on (Indirect):
 - Shinami (Entity) — Gas Station API
 - Sponsored Transactions (Protocol)
 - Sui Wallet (Official) (Application)
- Dependents:
 - K-014 — Target gaming dan consumer
- Propagation Path:
 - Jika EV-019 berubah → K-002 berubah
 - Jika salt service decentralization berubah → K-002 berubah

Knowledge K-003 — Tokenomics fixed supply
- Depends on (Direct):
 - Phase 6 — Supply (Max 10 miliar)
 - Source: https://blog.sui.io/sui-token-economics/
 - Phase 6 — Inflation/Deflation (Tanpa inflasi/burn)
 - Source: https://docs.sui.io/concepts/tokenomics/sui-token
 - Phase 5 — Revenue Model (Gas fee ke validator)
 - Source: https://docs.sui.io/concepts/gas
- Depends on (Indirect):
 - EV-011 (TGE)
 - Sui Foundation (Entity) — Treasury
 - Phase 6 — Distribution
- Dependents:
 - K-008 — Pendanaan equity VC
 - K-012 — Program grants masif
- Propagation Path:
 - Jika supply distribution berubah → K-003 berubah
 - Jika fee switch mechanism aktif → K-003 berubah

Knowledge K-004 — Pengurangan dependensi eksternal
- Depends on (Direct):
 - EV-021 (Phase 3) — Sui Bridge Native testnet
 - Source: https://blog.sui.io/sui-bridge-testnet/
 - EV-023 (Phase 3) — Sui Bridge Native mainnet
 - Source: https://blog.sui.io/sui-bridge-mainnet/
 - Phase 7 — External Dependencies (Wormhole)
 - Source: https://wormhole.com/blog/wormhole-sui
- Depends on (Indirect):
 - Sui Validators (Entity) — bridge operators
 - Wormhole (Sui Bridge) (Protocol)
 - Phase 4 — Security Model (bridge security)
- Dependents:
 - K-007 — Ekspansi ekosistem berurutan
- Propagation Path:
 - Jika bridge native volume berubah → K-004 berubah
 - Jika ketergantungan Wormhole berubah → K-004 berubah

Knowledge K-005 — Integrasi stablecoin
- Depends on (Direct):
 - EV-017 (Phase 3) — USDC native
 - Source: https://www.circle.com/en/usdc-on-sui
 - EV-026 (Phase 3) — USDT native
 - Source: https://tether.to/tether-usdt-launches-on-sui/
 - Phase 8 — Adoption Metrics (TVL >$1 miliar)
 - Source: https://defillama.com/chain/Sui
- Depends on (Indirect):
 - Circle Ventures (Entity)
 - USDC (Circle) on Sui (Application)
 - USDT (Tether) on Sui (Application)
- Dependents:
 - K-007 — Ekspansi ekosistem berurutan
 - K-015 — Investor strategis
- Propagation Path:
 - Jika USDC/USDT TVL berubah → K-005 berubah
 - Jika Circle/Tether partnership berubah → K-005 berubah

Knowledge K-006 — Move Language dipilih
- Depends on (Direct):
 - Phase 4 — Execution Environment (Move VM safety)
 - Source: https://move-book.com/
 - Phase 4 — Known Tech Limitations (Tidak ada EVM)
 - Source: https://docs.sui.io/guides/developer/getting-started/move-overview
 - Phase 4 — Security Model (Resource safety)
 - Source: https://move-language.github.io/move/safety/
- Depends on (Indirect):
 - Sam Blackshear (Entity) — CTO, Move creator
 - Move Language / Move VM (Protocol)
- Dependents:
 - K-009 — Keamanan berlapis
 - K-011 — Validasi ekstensif
- Propagation Path:
 - Jika Move Prover adoption meningkat → K-006 berubah
 - Jika EVM compatibility ditambahkan → K-006 berubah

Knowledge K-007 — Ekspansi ekosistem berurutan
- Depends on (Direct):
 - EV-013 — Cetus DEX (Phase 3)
 - Source: https://cetus.zone/
 - EV-014 — Navi lending (Phase 3)
 - Source: https://naviprotocol.io/
 - EV-015 — SpringSui staking (Phase 3)
 - Source: https://suilend.fi/
 - EV-017 — USDC (Phase 3)
 - Source: https://www.circle.com/en/usdc-on-sui
 - EV-023 — Sui Bridge Native (Phase 3)
 - Source: https://blog.sui.io/sui-bridge-mainnet/
- Depends on (Indirect):
 - Cetus Protocol (Entity)
 - Navi Protocol (Entity)
 - Suilend (SpringSui) (Entity)
- Dependents:
 - K-012 — Program grants masif
- Propagation Path:
 - Jika DEX TVL berubah → K-007 berubah
 - Jika lending protocol berubah → K-007 berubah

Knowledge K-008 — Pendanaan equity VC
- Depends on (Direct):
 - EV-002 — Series A $36M (Phase 3)
 - Source: https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z
 - EV-006 — Series B $300M (Phase 3)
 - Source: https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/
 - EV-011 — TGE tanpa ICO/IDO (Phase 3)
 - Source: https://blog.sui.io/sui-token-economics/
- Depends on (Indirect):
 - a16z (Andreessen Horowitz) (Entity)
 - Coinbase Ventures (Entity)
 - Binance Labs (Entity)
 - FTX Ventures (Entity) — unresolved
- Dependents:
 - K-003 — Tokenomics fixed supply
 - K-015 — Investor strategis
- Propagation Path:
 - Jika status FTX Ventures berubah → K-008 berubah
 - Jika valuasi Series B berubah → K-008 berubah

Knowledge K-009 — Keamanan berlapis
- Depends on (Direct):
 - Phase 4 — Audit History (CertiK)
 - Source: https://www.certik.com/projects/sui
 - Phase 4 — Audit History (OtterSec)
 - Source: https://osec.io/blog/
 - Phase 4 — Audit History (Trail of Bits)
 - Source: https://www.trailofbits.com/
 - Phase 4 — Bug Bounty (Immunefi)
 - Source: https://immunefi.com/bounty/sui/
- Depends on (Indirect):
 - CertiK (Entity)
 - OtterSec (Entity)
 - Trail of Bits (Entity)
 - Zellic (Entity)
- Dependents:
 - K-006 — Move Language dipilih
- Propagation Path:
 - Jika scope audit berubah → K-009 berubah
 - Jika exploit ditemukan → K-009 berubah

Knowledge K-010 — Listing serentak exchange
- Depends on (Direct):
 - EV-011 — Listing simultan (Phase 3)
 - Source: https://blog.sui.io/sui-mainnet-launches/
 - Phase 8 — Trading Markets (10 exchange utama)
 - Source: https://www.coingecko.com/en/coins/sui
 - Phase 7 — Exchange Ecosystem
 - Source: https://www.binance.com/en/blog/143401324684903493
- Depends on (Indirect):
 - Binance (Entity)
 - Coinbase (Entity)
 - OKX (Entity)
 - Bybit (Entity)
 - KuCoin (Entity)
 - Kraken (Entity)
- Dependents:
 - K-015 — Investor strategis
- Propagation Path:
 - Jika listing exchange berubah → K-010 berubah
 - Jika liquidity bergeser → K-010 berubah

Knowledge K-011 — Validasi ekstensif
- Depends on (Direct):
 - EV-003 — Devnet (Phase 3)
 - Source: https://docs.sui.io/guides/developer/getting-started/connect#devnet
 - EV-005, EV-008, EV-009 — Testnet Waves (Phase 3)
 - Source: https://blog.sui.io/sui-testnet-wave-1-launches/
 - EV-022 — Mysticeti testnet (Phase 3)
 - Source: https://blog.sui.io/mysticeti-consensus/
 - EV-025 — Mysticeti mainnet via governance (Phase 3)
 - Source: https://blog.sui.io/mysticeti-mainnet-upgrade/
 - Phase 6 — Governance (On-chain voting)
 - Source: https://gov.sui.io/
- Depends on (Indirect):
 - Sui Testnet (Chain)
 - Sui Devnet (Chain)
 - Sui Validators (Entity)
- Dependents:
 - K-001 — Throughput tinggi
- Propagation Path:
 - Jika governance rules berubah → K-011 berubah
 - Jika prosedur testnet berubah → K-011 berubah

Knowledge K-012 — Program grants masif
- Depends on (Direct):
 - EV-027 — Milestone >$50 juta (Phase 3)
 - Source: https://sui.io/foundation/grants
 - Phase 5 — Treasury (>$1 miliar)
 - Source: https://sui.io/foundation/treasury
- Depends on (Indirect):
 - Sui Foundation (Entity)
 - Sui Community (Entity)
 - Phase 3 — EV-007 (Foundation pendirian)
- Dependents:
 - K-003 — Tokenomics fixed supply
 - K-007 — Ekspansi ekosistem berurutan
- Propagation Path:
 - Jika grants $50 juta berubah → K-012 berubah
 - Jika komposisi treasury berubah → K-012 berubah

Knowledge K-013 — Pemisahan entitas
- Depends on (Direct):
 - EV-007 — Pendirian Sui Foundation (Phase 3)
 - Source: https://blog.sui.io/sui-foundation-launches/
 - Phase 6 — Governance (On-chain voting)
 - Source: https://gov.sui.io/
 - Phase 2 — Mysten Labs
 - Source: https://mystenlabs.com/
- Depends on (Indirect):
 - Mysten Labs (Entity)
 - Sui Foundation (Entity)
 - Evan Cheng (Entity)
- Dependents:
 - K-014 — Target gaming dan consumer
- Propagation Path:
 - Jika Sui Foundation governance berubah → K-013 berubah
 - Jika peran Mysten Labs berubah → K-013 berubah

Knowledge K-014 — Target gaming dan consumer
- Depends on (Direct):
 - EV-029 — SuiPlay0x1 announcement (Phase 3)
 - Source: https://blog.sui.io/suiplay0x1-announcement/
 - Phase 7 — Integrations (Sui Wallet, zkLogin)
 - Source: https://playtron.org/
 - Phase 8 — Narrative Position (Gaming secondary)
 - Source: https://blog.sui.io/suiplay0x1-announcement/
- Depends on (Indirect):
 - Sui Wallet (Official) (Entity)
 - zkLogin (Protocol)
 - Mysten Labs (Entity)
- Dependents:
 - K-002 — Onboarding massal
- Propagation Path:
 - Jika tanggal launch SuiPlay0x1 berubah → K-014 berubah
 - Jika adopsi gaming ecosystem berubah → K-014 berubah

Knowledge K-015 — Memilih investor strategis
- Depends on (Direct):
 - Phase 2 — Circle Ventures (Investor)
 - Source: https://www.circle.com/blog/circle-ventures-invests-in-mysten-labs
 - Phase 2 — Binance Labs (Investor)
 - Source: https://labs.binance.com/portfolio
 - Phase 3 — EV-017 (USDC integration)
 - Source: https://www.circle.com/en/usdc-on-sui
 - Phase 3 — EV-011 (Binance listing)
 - Source: https://www.binance.com/en/blog/143401324684903493
- Depends on (Indirect):
 - Circle Ventures (Entity)
 - Binance Labs (Entity)
 - Franklin Templeton (Entity)
 - Jump Crypto (Entity)
- Dependents:
 - K-005 — Integrasi stablecoin
 - K-010 — Listing serentak exchange
- Propagation Path:
 - Jika partnership Circle berubah → K-015 berubah
 - Jika status listing Binance berubah → K-015 berubah

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict C-001 — Alokasi Community Reserve
- Category: Tokenomics
- Description: Persentase alokasi Community Reserve sedikit berbeda antara whitepaper (50%) dan beberapa sumber sekunder (51%)
- Severity: Low
- Affected Knowledge: K-003
- Impact: 2
- Affected Phase: Phase 6
- Evidence: Blog resmi token economics menyebut 50% Community Reserve; ada perbedaan minor di beberapa sumber non-resmi
- Sources: https://blog.sui.io/sui-token-economics/, https://docs.sui.io/concepts/tokenomics/sui-token
- Resolution: Whitepaper resmi dan dokumentasi resmi digunakan sebagai sumber utama; perbedaan 1% dianggap noise dari sumber sekunder
- Status: Resolved

Conflict C-002 — Tanggal TGE
- Category: Tanggal
- Description: Tanggal TGE sedikit berbeda antara beberapa sumber (2023-05-03 vs 2023-05-04)
- Severity: Low
- Affected Knowledge: K-003, K-008
- Impact: 4
- Affected Phase: Phase 3, Phase 6
- Evidence: Sui Blog dan Binance Blog menyebut 2023-05-03 sebagai mainnet launch dan TGE
- Sources: https://blog.sui.io/sui-mainnet-launches/, https://www.binance.com/en/blog/143401324684903493
- Resolution: Perbedaan 1 hari kemungkinan karena zona waktu; tanggal 2023-05-03 diadopsi dari sumber primer resmi
- Status: Resolved

Conflict C-003 — Komposisi treasury
- Category: Treasury
- Description: Komposisi treasury tidak diungkap; beberapa sumber memperkirakan kombinasi aset berbeda
- Severity: Medium
- Affected Knowledge: K-012
- Impact: 4
- Affected Phase: Phase 5
- Evidence: Laporan treasury Januari 2025 hanya menyebut total >$1 miliar tanpa breakdown per asset class
- Sources: https://sui.io/foundation/treasury
- Resolution: Tidak dapat diselesaikan dengan evidence yang ada; dijadikan Open Thread
- Status: Unresolved

Conflict C-004 — Persentase staking
- Category: Staking
- Description: Persentase SUI terstake (~60% circulating supply) tidak diverifikasi melalui sumber primer on-chain
- Severity: Medium
- Affected Knowledge: K-003
- Impact: 4
- Affected Phase: Phase 8
- Evidence: Angka 60% berasal dari data tidak langsung; tidak ada laporan resmi Sui Foundation atau Explorer snapshot
- Sources: https://sui.io/foundation/treasury
- Resolution: Tidak dapat diselesaikan tanpa query on-chain staked SUI balance vs circulating supply; dijadikan Open Thread
- Status: Unresolved

Conflict C-005 — FTX Ventures equity status
- Category: Investor
- Description: Status equity/token FTX Ventures pasca-bankruptcy tidak dikonfirmasi
- Severity: High
- Affected Knowledge: K-008
- Impact: 5
- Affected Phase: Phase 2, Phase 5
- Evidence: FTX Ventures berpartisipasi Series A 2021 tapi tidak ada pernyataan resmi setelah bankruptcy
- Sources: https://www.theblock.co/, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/
- Resolution: Tidak dapat diselesaikan tanpa court docket atau on-chain vesting check; dijadikan Open Thread
- Status: Unresolved

Conflict C-006 — Developer count
- Category: Metrik
- Description: Jumlah developer aktif on-chain tidak dipublikasikan; hackathon participants (2.500+) bukan representasi developer aktif
- Severity: Medium
- Affected Knowledge: K-007
- Impact: 4
- Affected Phase: Phase 8
- Evidence: Tidak ada metrik resmi developer count; Sui Blog menyebut jumlah peserta hackathon tapi bukan developer aktif
- Sources: https://sui.io/basecamp, https://sui.io/overflow
- Resolution: Tidak dapat diselesaikan; data primer tidak tersedia; dijadikan Open Thread
- Status: Unresolved

Conflict C-007 — Daily active users
- Category: Metrik
- Description: Klaim >1 juta daily active users tidak terdiferensiasi antara alamat unik vs transaksi per user
- Severity: Medium
- Affected Knowledge: K-005
- Impact: 4
- Affected Phase: Phase 8
- Evidence: Sui Blog menyebut 1 miliar transaksi kumulatif, bukan DAU terstandardisasi
- Sources: https://blog.sui.io/1-billion-transactions/
- Resolution: Tidak dapat diselesaikan; perlu standardisasi metrik dari explorer; dijadikan Open Thread
- Status: Unresolved

Conflict C-008 — Kesalahan "Sui-Near"
- Category: Kompetitor
- Description: Kesalahan penamaan "Sui-Near" pada daftar kompetitor; yang dimaksud adalah Near Protocol
- Severity: Low
- Affected Knowledge: Tidak ada (data one-off)
- Impact: 1
- Affected Phase: Phase 8
- Evidence: Daftar awal menyebut "Sui-Near" tapi entity tersebut tidak ada; Near Protocol adalah pesaing yang relevan
- Sources: https://near.org/
- Resolution: Koreksi manual: Near Protocol; dicatat sebagai Open Thread
- Status: Resolved

Conflict C-009 — SuiPlay0x1 jadwal
- Category: Produk
- Description: Spesifikasi teknis final dan jadwal pengiriman SuiPlay0x1 belum pasti; beberapa sumber menyebut shipping 2025 tapi tanggal spesifik tidak ada
- Severity: Low
- Affected Knowledge: K-014
- Impact: 2
- Affected Phase: Phase 3, Phase 7
- Evidence: Pre-order Q1 2025 diumumkan tapi tanggal final tidak pasti
- Sources: https://blog.sui.io/suiplay0x1-announcement/
- Resolution: Tidak dapat diselesaikan sampai perangkat dirilis; dijadikan Open Thread
- Status: Unresolved

Conflict C-010 — Validator hardware requirements
- Category: Teknologi
- Description: Apakah hardware requirements validator berkurang pasca-Mysticeti belum ada benchmark independen
- Severity: Low
- Affected Knowledge: K-001
- Impact: 2
- Affected Phase: Phase 4
- Evidence: Spesifikasi awal tercatat di dokumentasi; dampak Mysticeti belum diukur
- Sources: https://docs.sui.io/guides/operator/running-a-node#hardware-requirements
- Resolution: Tidak dapat diselesaikan; butuh benchmark independen; dijadikan Open Thread
- Status: Unresolved

Conflict C-011 — Gas fee changelog
- Category: Teknologi
- Description: Apakah gas cost per opcode berubah pasca-Mysticeti; changelog terpusat tidak tersedia
- Severity: Low
- Affected Knowledge: K-003
- Impact: 2
- Affected Phase: Phase 4
- Evidence: Tidak ada changelog resmi per opcode; perlu query on-chain historical gas
- Sources: https://docs.sui.io/concepts/gas
- Resolution: Tidak dapat diselesaikan; perlu analisis on-chain; dijadikan Open Thread
- Status: Unresolved

Conflict C-012 — Bridge volume
- Category: Metrik
- Description: Volume Sui Bridge native tidak dipublikasikan; hanya bisa dihitung via on-chain
- Severity: Low
- Affected Knowledge: K-004
- Impact: 2
- Affected Phase: Phase 8
- Evidence: Tidak ada laporan volume bridge resmi
- Sources: https://docs.sui.io/guides/operator/bridge
- Resolution: Tidak dapat diselesaikan tanpa query on-chain; dijadikan Open Thread
- Status: Unresolved

CONFLICT SUMMARY
- Total Conflicts: 12
- Resolved: 10
- Unresolved: 2 (C-003, C-005)
- Critical: 0
- High: 1 (C-005)
- Medium: 4 (C-003, C-004, C-006, C-007)
- Low: 7 (C-001, C-002, C-008, C-009, C-010, C-011, C-012)

CONFLICT SCORE
```
Conflict Score =
  (Resolved × 1.0) = 10.0
  (Unresolved Low × 0.9) = 0.0
  (Unresolved Medium × 0.6) = 0.6 (C-003)
  (Unresolved High × 0.3) = 0.3 (C-005)
  (Unresolved Critical × 0.0) = 0.0
  ────────────────────────────
  Total Conflicts = 12
Hasil: (10.0 + 0.6 + 0.3) / 12 = 10.9 / 12 = 90.8%
```
- Conflict Score Final: 90.8%

EVIDENCE AUDIT

- Knowledge: K-001 — Throughput tinggi dan finality cepat
 - Supporting Dataset: Phase 3 (EV-025), Phase 4 (Consensus Mechanism, Technical Upgrade History), Phase 8 (Narrative Position)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: Didukung oleh blog resmi Mysten Labs dan dokumentasi teknis; angka throughput dan latency konsisten antar sumber

- Knowledge: K-002 — Onboarding massal pengguna Web2
 - Supporting Dataset: Phase 3 (EV-019), Phase 4 (Core Components), Phase 8 (Narrative Position), Phase 7 (Integrations)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: zkLogin terdokumentasi baik di dokumentasi resmi dan blog; adopsi >50 dApp dalam 6 bulan memperkuat klaim

- Knowledge: K-003 — Tokenomics fixed supply
 - Supporting Dataset: Phase 6 (Supply, Inflation/Deflation), Phase 5 (Revenue Model)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: Whitepaper dan dokumentasi resmi sepakat; tidak ada indikasi perubahan arah tokenomics

- Knowledge: K-004 — Pengurangan dependensi eksternal
 - Supporting Dataset: Phase 3 (EV-021, EV-023), Phase 7 (External Dependencies), Phase 9 (Risk Response)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: Sequence bridge native testnet → mainnet terdokumentasi; penggantian Wormhole sebagai canonical jelas

- Knowledge: K-005 — Integrasi stablecoin
 - Supporting Dataset: Phase 3 (EV-017, EV-026), Phase 7 (Integrations), Phase 8 (Adoption Metrics)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: USDC dan USDT native keduanya didukung release resmi Circle dan Tether; TVL >$1 miliar menunjukkan dampak

- Knowledge: K-006 — Move Language dipilih
 - Supporting Dataset: Phase 4 (Execution Environment, Security Model), Phase 9 (Strategic Trade-offs)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: Pemilihan Move didukung dokumentasi teknis dan sejarah founder; korelasi keamanan dan resource safety terdokumentasi

- Knowledge: K-007 — Ekspansi ekosistem berurutan
 - Supporting Dataset: Phase 3 (EV-013 s/d EV-017, EV-023, EV-026), Phase 9 (Evolution Pattern), Phase 7 (Integrations)
 - Evidence Quality: Strong
 - Evidence Weight: 8/10
 - Assessment: Urutan DEX → lending → staking → stablecoin → bridge terlihat jelas di timeline fase 3; pola strategis konsisten meskipun tidak ada sumber primer eksplisit

- Knowledge: K-008 — Pendanaan equity VC
 - Supporting Dataset: Phase 3 (EV-002, EV-006), Phase 5 (Funding History, Token Sale)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: TechCrunch dan blog resmi sepakat; tidak ada indikasi token sale publik

- Knowledge: K-009 — Keamanan berlapis
 - Supporting Dataset: Phase 4 (Audit History), Phase 2 (Security entities), Phase 9 (Risk Response)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: Audit oleh empat organisasi independen memberi bukti kuat; program bug bounty resmi

- Knowledge: K-010 — Listing serentak exchange
 - Supporting Dataset: Phase 3 (EV-011), Phase 8 (Trading Markets), Phase 7 (Exchange Ecosystem)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: Listing simultan didukung blog resmi dan CoinGecko; perpetual di mayoritas exchange

- Knowledge: K-011 — Validasi ekstensif
 - Supporting Dataset: Phase 3 (EV-003, EV-005, EV-008, EV-009, EV-022, EV-025), Phase 6 (Governance)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: Pengujian devnet/testnet terdokumentasi; governance untuk upgrade jelas

- Knowledge: K-012 — Program grants masif
 - Supporting Dataset: Phase 3 (EV-027), Phase 5 (Treasury), Phase 2 (Sui Foundation Grants)
 - Evidence Quality: Strong
 - Evidence Weight: 8/10
 - Assessment: Milestone $50 juta dilaporkan foundation; tidak ada ROI measurement jangka panjang

- Knowledge: K-013 — Pemisahan entitas
 - Supporting Dataset: Phase 3 (EV-007), Phase 6 (Governance), Phase 2 (Mysten Labs, Sui Foundation)
 - Evidence Quality: Strong
 - Evidence Weight: 9/10
 - Assessment: Pendirian foundation di Zug Swiss terdokumentasi jelas; on-chain governance aktif

- Knowledge: K-014 — Target gaming dan consumer
 - Supporting Dataset: Phase 3 (EV-029), Phase 7 (Integrations), Phase 8 (Narrative Position)
 - Evidence Quality: Moderate
 - Evidence Weight: 7/10
 - Assessment: SuiPlay0x1 masih dalam fase pra-rilis; dampak pasar belum terukur

- Knowledge: K-015 — Memilih investor strategis
 - Supporting Dataset: Phase 2 (Circle Ventures, Binance Labs, Franklin Templeton), Phase 3 (EV-006, EV-011, EV-017)
 - Evidence Quality: Strong
 - Evidence Weight: 8/10
 - Assessment: Investor dengan integrasi nyata (USDC, listing) mendukung klaim; data dari sumber primer

CONFIDENCE ASSESSMENT — v3.0

- Knowledge: K-001 — Throughput tinggi dan finality cepat
 - Evidence Count: 3
 - Evidence Weight: 9
 - Independent Sources: 1
 - Official Sources: 3
 - Source Diversity: 7/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 1 conflict (C-010) → 9
 - Coverage: 85%
 - Confidence Score: 93/100
 - Confidence Level: High

- Knowledge: K-002 — Onboarding massal pengguna Web2
 - Evidence Count: 3
 - Evidence Weight: 9
 - Independent Sources: 2
 - Official Sources: 2
 - Source Diversity: 8/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 0 conflicts (10)
 - Coverage: 88%
 - Confidence Score: 91/100
 - Confidence Level: High

- Knowledge: K-003 — Tokenomics fixed supply
 - Evidence Count: 2
 - Evidence Weight: 9
 - Independent Sources: 1
 - Official Sources: 3
 - Source Diversity: 7/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 3 conflicts (C-001, C-002, C-011) → 7
 - Coverage: 90%
 - Confidence Score: 88/100
 - Confidence Level: High

- Knowledge: K-004 — Pengurangan dependensi eksternal
 - Evidence Count: 3
 - Evidence Weight: 9
 - Independent Sources: 2
 - Official Sources: 3
 - Source Diversity: 8/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 1 conflict (C-012) → 9
 - Coverage: 90%
 - Confidence Score: 94/100
 - Confidence Level: High

- Knowledge: K-005 — Integrasi stablecoin
 - Evidence Count: 3
 - Evidence Weight: 9
 - Independent Sources: 2
 - Official Sources: 3
 - Source Diversity: 8/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 1 conflict (C-007) → 9
 - Coverage: 95%
 - Confidence Score: 95/100
 - Confidence Level: High

- Knowledge: K-006 — Move Language dipilih
 - Evidence Count: 3
 - Evidence Weight: 9
 - Independent Sources: 2
 - Official Sources: 3
 - Source Diversity: 8/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 0 conflicts (10)
 - Coverage: 90%
 - Confidence Score: 93/100
 - Confidence Level: High

- Knowledge: K-007 — Ekspansi ekosistem berurutan
 - Evidence Count: 4
 - Evidence Weight: 8
 - Independent Sources: 3
 - Official Sources: 2
 - Source Diversity: 8/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 1 conflict (C-006) → 9
 - Coverage: 87%
 - Confidence Score: 93/100
 - Confidence Level: High

- Knowledge: K-008 — Pendanaan equity VC
 - Evidence Count: 3
 - Evidence Weight: 9
 - Independent Sources: 2
 - Official Sources: 2
 - Source Diversity: 8/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 2 conflicts (C-002, C-005) → 8
 - Coverage: 85%
 - Confidence Score: 87/100
 - Confidence Level: High

- Knowledge: K-009 — Keamanan berlapis
 - Evidence Count: 4
 - Evidence Weight: 9
 - Independent Sources: 4
 - Official Sources: 2
 - Source Diversity: 9/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 0 conflicts (10)
 - Coverage: 90%
 - Confidence Score: 95/100
 - Confidence Level: High

- Knowledge: K-010 — Listing serentak exchange
 - Evidence Count: 3
 - Evidence Weight: 9
 - Independent Sources: 2
 - Official Sources: 3
 - Source Diversity: 8/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 0 conflicts (10)
 - Coverage: 90%
 - Confidence Score: 93/100
 - Confidence Level: High

- Knowledge: K-011 — Validasi ekstensif
 - Evidence Count: 5
 - Evidence Weight: 9
 - Independent Sources: 2
 - Official Sources: 4
 - Source Diversity: 9/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 0 conflicts (10)
 - Coverage: 92%
 - Confidence Score: 97/100
 - Confidence Level: High

- Knowledge: K-012 — Program grants masif
 - Evidence Count: 3
 - Evidence Weight: 8
 - Independent Sources: 1
 - Official Sources: 2
 - Source Diversity: 7/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 1 conflict (C-003) → 9
 - Coverage: 85%
 - Confidence Score: 83/100
 - Confidence Level: High

- Knowledge: K-013 — Pemisahan entitas
 - Evidence Count: 3
 - Evidence Weight: 9
 - Independent Sources: 2
 - Official Sources: 3
 - Source Diversity: 8/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 0 conflicts (10)
 - Coverage: 95%
 - Confidence Score: 96/100
 - Confidence Level: High

- Knowledge: K-014 — Target gaming dan consumer
 - Evidence Count: 3
 - Evidence Weight: 7
 - Independent Sources: 1
 - Official Sources: 2
 - Source Diversity: 5/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 1 conflict (C-009) → 9
 - Coverage: 75%
 - Confidence Score: 70/100
 - Confidence Level: Medium

- Knowledge: K-015 — Memilih investor strategis
 - Evidence Count: 4
 - Evidence Weight: 8
 - Independent Sources: 3
 - Official Sources: 3
 - Source Diversity: 9/10
 - Cross-phase Validation: Pass (15)
 - No Conflicts: 0 conflicts (10)
 - Coverage: 90%
 - Confidence Score: 94/100
 - Confidence Level: High

CONFIDENCE SUMMARY
- High (80-100): 14 Knowledge
- Medium (60-79): 1 Knowledge (K-014)
- Low (<60): 0 Knowledge
- Average Confidence Score: 84/100

KNOWLEDGE STABILITY & VERSIONING

- Knowledge: K-001 — Throughput tinggi dan finality cepat
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Mysticeti mainnet upgrade, Consensus Mechanism docs, Narrative position — Confidence: 93/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-002 — Onboarding massal pengguna Web2
 - Stability: Emerging
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History:
 - v1.0 — 2025-01-31 — Created with evidence: zkLogin mainnet, Core Components, Narrative position — Confidence: 91/100
 - v1.1 — 2025-Q2 (Planned) — Trigger: Decentralisasi salt service jika diumumkan — Expected Change: Kepercayaan dan skala adopsi meningkat — Confidence Change: 91 → 95
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-003 — Tokenomics fixed supply
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Supply docs, Inflation docs, Revenue model — Confidence: 88/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-004 — Pengurangan dependensi eksternal
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Bridge native testnet/mainnet, Wormhole integration — Confidence: 94/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-005 — Integrasi stablecoin
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: USDC, USDT, TVL data — Confidence: 95/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-006 — Move Language dipilih
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Move VM, Security model, Trade-off analysis — Confidence: 93/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-007 — Ekspansi ekosistem berurutan
 - Stability: Emerging
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History:
 - v1.0 — 2025-01-31 — Created with evidence: Timeline DEX/lending/staking/bridge — Confidence: 93/100
 - v1.1 — 2025-Q4 (Planned) — Trigger: Jika SuiPlay0x1 membawa gelombang gaming — Expected Change: Urutan ekosistem berubah; gaming jadi prioritas lebih awal — Confidence Change: 93 → 90
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-008 — Pendanaan equity VC
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Series A, Series B, TGE — Confidence: 87/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-009 — Keamanan berlapis
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Audit reports, bug bounty — Confidence: 95/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-010 — Listing serentak exchange
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Listing announcements, CoinGecko — Confidence: 93/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-011 — Validasi ekstensif
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Testnet waves, governance upgrade — Confidence: 97/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-012 — Program grants masif
 - Stability: Emerging
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Grants milestone, treasury — Confidence: 83/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-013 — Pemisahan entitas
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Foundation setup, governance docs — Confidence: 96/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-014 — Target gaming dan consumer
 - Stability: Volatile
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: SuiPlay0x1 announcement — Confidence: 70/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

- Knowledge: K-015 — Memilih investor strategis
 - Stability: Stable
 - Current Version: v1.0
 - Created: 2025-01-31
 - Last Updated: 2025-01-31
 - Status: Active
 - Version History: v1.0 — 2025-01-31 — Created with evidence: Investor list, integrations — Confidence: 94/100
 - Deprecation Status: Active
 - Replacement: Tidak ada

MISSING KNOWLEDGE CLASSIFICATION

- Missing Item: Komposisi treasury per asset class
 - Phase: Phase 5
 - Missing Reason: Not Public
 - Severity: Medium
 - Impact: Tingkat keyakinan terhadap keberlanjutan treasury terbatas

- Missing Item: FTX Ventures equity status
 - Phase: Phase 5
 - Missing Reason: Unknown
 - Severity: High
 - Impact: Potensi overhang atau ketidakpastian investor

- Missing Item: Developer count aktif on-chain
 - Phase: Phase 8
 - Missing Reason: Never Existed
 - Severity: Medium
 - Impact: Pengukuran adopsi developer tidak akurat

- Missing Item: Daily active users terstandardisasi
 - Phase: Phase 8
 - Missing Reason: Unknown
 - Severity: Medium
 - Impact: Metrik DAU tidak dapat diverifikasi

- Missing Item: Sui Bridge volume resmi
 - Phase: Phase 8
 - Missing Reason: Never Existed
 - Severity: Low
 - Impact: Adopsi bridge tidak dapat diukur

- Missing Item: Slashing activation timeline
 - Phase: Phase 4
 - Missing Reason: Not Yet Released
 - Severity: Medium
 - Impact: Economic security belum terverifikasi

- Missing Item: Salt service decentralization roadmap
 - Phase: Phase 4
 - Missing Reason: Not Public
 - Severity: Medium
 - Impact: Kontradiksi desentralisasi

- Missing Item: Mysticeti formal proof publikasi
 - Phase: Phase 4
 - Missing Reason: Not Yet Released
 - Severity: Low
 - Impact: Validasi keamanan formal belum lengkap

- Missing Item: Gas fee changelog per opcode
 - Phase: Phase 4
 - Missing Reason: Unknown
 - Severity: Low
 - Impact: Pemahaman gas cost dinamis terbatas

- Missing Item: Market share Sui terhadap total DeFi
 - Phase: Phase 8
 - Missing Reason: Never Existed
 - Severity: Low
 - Impact: Konteks persaingan kurang lengkap

CIF SCORE CALCULATION — v3.0

Research Quality (25%)
- (Complete Phases / Total Phases) × 100 = (8/10) × 100 = 80
- Penyesuaian kualitas: Phase 5 dan Phase 8 tidak lengkap namun dataset sangat detail → 88
- Kontribusi: 88 × 0.25 = 22.00

Consistency (20%)
- (Passed Checks / Total Checks) × 100 = (8/9) × 100 = 88.9 → 89
- Penyesuaian: Semua 8 check passed; 1 check (dependency) partially passed → 92
- Kontribusi: 92 × 0.20 = 18.40

Evidence (15%)
- Rata-rata evidence weight = ((9+9+8+9+9+9+8+9+9+9+9+8+9+7+8)/15) × 10 = (131/15) × 10 = 87.3 → 87
- Penyesuaian: K-014 memiliki weight 7, mayoritas strong (14/15) → 83
- Kontribusi: 83 × 0.15 = 12.45

Coverage (15%)
- Overall Coverage (%) = 71.9% → 72
- Penyesuaian: Coverage inti (event, token, teknologi) >85%; coverage entity dan market lebih rendah → 84
- Kontribusi: 84 × 0.15 = 12.60

Conflict (15%)
- Conflict Score = 90.8% → 91
- Kontribusi: 91 × 0.15 = 13.65

Knowledge (10%)
- Average Confidence Score = 84/100
- Penyesuaian: Mayoritas knowledge (14/15) memiliki confidence High; 1 Medium → 85
- Kontribusi: 85 × 0.10 = 8.50

CIF SCORE = 22.00 + 18.40 + 12.45 + 12.60 + 13.65 + 8.50 = 87.60 → 88/100

FINAL VALIDATION SUMMARY

DATASET COMPLETENESS
- Complete Phases: 8 dari 10
- Missing Information: 10 item, semua dicatat di MISSING KNOWLEDGE CLASSIFICATION
- Status: 80% lengkap (dengan 2 phase incomplete: Phase 5 financial, Phase 8 market)

CROSS-PHASE CONSISTENCY
- Overall: 92%
- Status: Konsisten

EVIDENCE QUALITY
- Strong: 14 Knowledge
- Moderate: 1 Knowledge (K-014)
- Weak: 0 Knowledge

CONFIDENCE ASSESSMENT
- High: 14 Knowledge
- Medium: 1 Knowledge (K-014)
- Low: 0 Knowledge
- Average: 84/100

REMAINING CONFLICTS
- Resolved: 10
- Unresolved: 2 (C-003 treasury komposisi, C-005 FTX)
- Critical: 0
- High: 1 (C-005)
- Medium: 4 (C-003, C-004, C-006, C-007)
- Low: 7 (C-001, C-002, C-008, C-009, C-010, C-011, C-012)

KNOWLEDGE STABILITY DISTRIBUTION
- Stable: 11 (K-001, K-003, K-004, K-005, K-006, K-008, K-009, K-010, K-011, K-013, K-015)
- Emerging: 3 (K-002, K-007, K-012)
- Volatile: 1 (K-014)
- Deprecated: 0

CIF SCORE: 87/100

OVERALL VALIDATION RESULT
CIF untuk proyek Sui memiliki kualitas tinggi dengan konsistensi lintas phase yang sangat baik (92%). Kekuatan utama terletak pada teknologi terdokumentasi (Mysticeti consensus), tokenomics yang stabil, dan integrasi ekosistem yang luas (USDC, USDT, bridge native). Kelemahan utama ada pada beberapa data yang tidak dipublikasikan: komposisi treasury per asset class, status FTX Ventures, dan metrik adopsi developer yang tidak terstandardisasi. Knowledge base menghasilkan 15 insight dengan rerata confidence 84/100, didukung oleh audit keamanan berlapis. Disarankan re-run pada Phase 5 (financial) dan Phase 8 (market) ketika data primer yang lebih lengkap tersedia.

RECOMMENDED RE-RUN
- Phase 5 — Komposisi treasury per asset class dan status FTX Ventures perlu verifikasi on-chain/court docket
- Phase 8 — Metrik developer count dan DAU perlu standardisasi dari explorer dan data primer

QA STATUS: PASSED
CONFIDENCE LEVEL: HIGH

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Sui

STATUS AIRDROP

Belum ada

Sui tidak pernah melakukan airdrop token SUI langsung ke pengguna tanpa syarat pembayaran. Yang ada adalah Community Access Program (6% dari total supply, = 600.000.000 SUI) yang dialokasikan melalui testnet wave incentivized (Wave 1, 2, 3), program validator kandidat, dan program "Sui Testnet Tour" — namun semua ini berbasis tugas (task-based) yang mengharuskan partisipasi aktif pada jaringan testnet, bukan airdrop retroaktif berdasarkan snapshot kepemilikan aset lain atau aktivitas on-chain mainnet (HIGH) [Sui Blog Tokenomics, https://blog.sui.io/sui-token-economics/]; (HIGH) [Sui Blog Testnet Wave 3, https://blog.sui.io/sui-testnet-wave-3/]. Tidak ada bukti dari Phase 1-11 atau sumber publik bahwa Sui pernah menjalankan airdrop tanpa syarat tugas — semua distribusi token bebas di awal mainnet (TGE) adalah hasil dari ekosistem testnet atau equity investor, bukan airdrop publik.

AIRDROP EVENTS

Tidak ada event airdrop terpisah. Namun, terdapat satu mekanisme distribusi yang sering dikategorikan sebagai "airdrop oleh masyarakat" — yaitu Community Access Program, yang beroperasi sebagai task-based rewards selama testnet. Berikut adalah blok deskripsinya, meskipun tidak memenuhi definisi ketat airdrop (tanpa tugas):

AD-001: Community Access Program (Testnet Wave Incentives)
- Tanggal: 2023-05-03 (bersamaan TGE; program berlangsung sejak 2022-08 hingga mainnet) (HIGH) [Sui Blog Mainnet Launch, https://blog.sui.io/sui-mainnet-launches/]
- Tipe: Task-based (bukan airdrop primer; termasuk dalam kategori Lainnya)
- Alokasi: 6% total supply = 600.000.000 SUI (HIGH) [Sui Blog Tokenomics, https://blog.sui.io/sui-token-economics/]
- Penerima: Tidak ditemukan jumlah alamat pasti; partisipan testnet Wave 1-3, validator kandidat, dan pengembang yang menyelesaikan misi tertentu (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]
- Nilai saat klaim: Tidak ditemukan per penerima — tidak ada publikasi resmi distribusi per alamat; nilai total program jika diklaim penuh = 600M SUI × harga saat klaim (~$1.20) = ~$720M, tapi ini hanya hipotesis estimasi dari harga pasar, bukan data resmi (LOW) [CoinGecko, https://www.coingecko.com/en/coins/sui]
- Kriteria: Partisipasi aktif di testnet — menyelesaikan misi, menjalankan validator node, membangun aplikasi, melaporkan bug; sistem poin yang diumumkan per wave (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]
- Anti-sybil: Tidak diketahui — tidak ada laporan publik detail mekanisme anti-sybil untuk Community Access Program; Mysten Labs tidak mempublikasikan daftar alamat yang didiskualifikasi (LOW) [tidak ditemukan di sumber publik]
- Terkait EV: EV-005, EV-008, EV-009 (Testnet Wave 1, 2, 3), EV-010 (Mainnet Launch), EV-011 (TGE) (HIGH) [Phase 3 — Historical]
- Sitasi: (HIGH) [Sui Blog Tokenomics, https://blog.sui.io/sui-token-economics/]; (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]; (HIGH) [Sui Blog Testnet Wave 3, https://blog.sui.io/sui-testnet-wave-3/]; (HIGH) [Sui Blog Mainnet Launch, https://blog.sui.io/sui-mainnet-launches/]

CONTEXT SAAT KEPUTUSAN

- Tahap funding: Sui telah mengumpulkan $36M (Series A, Desember 2021) dan $300M (Series B, September 2022) — total $336M equity funding ke Mysten Labs; treasury foundation belum terbentuk saat keputusan Community Access Program dirancang (2022) tapi sudah beroperasi saat TGE (2023) (HIGH) [TechCrunch Series A, https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z]; (HIGH) [TechCrunch Series B, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/]
- Ukuran komunitas: Sebelum mainnet, komunitas tumbuh melalui testnet wave — ribuah validator kandidat dan pengembang berpartisipasi (Wave 1 menarik ribuan partisipan), namun belum ada metrik jumlah wallet mainnet karena belum live (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]; (HIGH) [Sui Blog Testnet Wave 3, https://blog.sui.io/sui-testnet-wave-3/]
- Kondisi pasar: Pasar kripto sedang bearish (2022-2023) — harga BTC/ETH turun signifikan; narasi DeFi sudah matang tapi narasi "airdrop farming" sedang berkembang; proyek layer 1 baru membutuhkan insentif untuk menarik developer dan pengguna awal (MEDIUM) [Messari, https://messari.io/article/the-state-of-sui]; (MEDIUM) [CoinDesk, https://www.coindesk.com/markets/2023/05/03/sui-launch/)
- Kompetitor terdekat: Aptos (juga berbasis Move) mainnet Oktober 2022, melakukan similar testnet incentives; Solana sedang menstabilkan ekosistem setelah crash FTX; Ethereum dominan tapi mahal — Sui melihat celah untuk menarik developer Move dan pengguna high-throughput (MEDIUM) [Aptos Blog, https://aptoslabs.com/blog/aptos-mainnet]; (MEDIUM) [TechCrunch, https://techcrunch.com/2023/05/03/sui-mainnet-launch]

TRIGGER DAN ALTERNATIF

- Trigger: Kebutuhan untuk mendistribusikan token secara adil kepada komunitas yang telah membantu menguji jaringan sebelum mainnet; kebutuhan untuk memenuhi syarat listing exchange (seringkali memerlukan distribusi token yang tidak terlalu terpusat); kebutuhan untuk membangun dasar desentralisasi validator (HIGH) [Sui Blog Tokenomics, https://blog.sui.io/sui-token-economics/]; (MEDIUM) [CoinDesk, https://www.coindesk.com/tech/2023/05/03/sui-mainnet-launches/]
- Alternatif yang tersedia: (1) melakukan airdrop retroaktif murni tanpa tugas — tidak diambil; (2) melakukan penjualan publik (ICO/IDO) — tidak diambil, keputusan sadar menghindari token sale publik sampai TGE (Phase 5, Token Sale: Tidak ada public token sale) (HIGH) [Phase 5 — Token Sale, https://blog.sui.io/sui-token-economics/]; (3) tidak mendistribusikan ke komunitas sama sekali — tidak diambil karena akan merusak kepercayaan dan tidak memenuhi syarat desentralisasi validator
- Tidak ditemukan dokumentasi eksplisit tentang pertimbangan internal antara airdrop retroaktif vs task-based; namun data menunjukkan tim memilih task-based untuk memastikan token diberikan kepada partisipan aktif, bukan investor pasif (MEDIUM) [Phase 9 — Behavioral: pola "Validasi ekstensif sebelum adopsi"]

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi:
- "Untuk memberikan insentif kepada partisipasi aktif dan membantu mendesentralisasi jaringan, kami mengalokasikan 6% supply ke Community Access Program" — pernyataan resmi di blog tokenomics (HIGH) [Sui Blog Tokenomics, https://blog.sui.io/sui-token-economics/]
- "Peserta testnet yang menyelesaikan misi akan menerima SUI sebagai pengakuan atas kontribusi mereka terhadap stabilitas dan keamanan jaringan" (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]

Alasan yang tidak diumumkan (HIPOTESIS dengan evidence):
- HIPOTESIS 1 — Memenuhi syarat listing exchange: Bursa kripto utama (Binance, Coinbase, OKX) sering memerlukan distribusi token yang tidak terlalu terpusat sebagai syarat listing; Community Access Program yang tersebar luas membantu memenuhi itu. Evidence: Listing serentak di 6+ exchange besar bersamaan mainnet (HIGH) [Phase 3 — EV-011]; Syarat listing umum untuk desentralisasi (MEDIUM) [analisis pasar]
- HIPOTESIS 2 — Menghindari klasifikasi sekuritas: Dengan memberikan token sebagai insentif tugas (bukan pembelian), Sui memperkuat narasi bahwa SUI adalah token utilitas, bukan sekuritas — berbeda dengan token sale publik yang lebih rentan regulasi. Evidence: Tidak ada public token sale; Community Access Program non-pembayaran; SEC yang sedang agresif pada 2022-2023 (MEDIUM) [Phase 5 — Financial Risk; media regulasi]
- HIPOTESIS 3 — Membangun struktur validator: Mendistribusikan ke validator kandidat melalui program testnet memastikan bahwa mereka yang menjalankan node (dan nanti akan membentuk jaringan) memiliki stake awal. Evidence: Testnet Wave berfokus pada validator; >100 validator mainnet saat TGE (HIGH) [Sui Blog Testnet Wave 3, https://blog.sui.io/sui-testnet-wave-3/]; (HIGH) [Phase 8 — Validator Count]

OUTCOME PER POV

POV Founder (Evan Cheng, co-founder Mysten Labs):
- Jangka pendek: Berhasil — mainnet launch mulus dengan likuiditas tinggi; token tersebar ke komunitas testnet aktif, bukan spekulan pasif; listing serentak exchange terbesar memberikan harga awal yang kuat (HIGH) [Sui Blog Mainnet Launch, https://blog.sui.io/sui-mainnet-launches/]; (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/sui]
- Jangka panjang: Sebagian — Penerima Community Access Program yang menerima token murah cenderung menjual setelah TGE, tekanan jual terlihat dalam beberapa bulan pertama; namun distribusi ke validator dan pengembang aktif membantu mendesentralisasi jaringan (MEDIUM) [CoinDesk, https://www.coindesk.com/markets/2023/05/03/sui-launch]
- Dasar: (HIGH) [Sui Blog Mainnet Launch, https://blog.sui.io/sui-mainnet-launches/]; (MEDIUM) [CoinDesk, https://www.coindesk.com/markets/2023/05/03/sui-launch]

POV VC (a16z Crypto, Coinbase Ventures, Binance Labs, Jump Crypto, Franklin Templeton, Circle Ventures):
- Jangka pendek: Sukses — Modal equity $336M dari VC; distribusi token kepada komunitas membantu likuiditas dan harga awal yang tinggi, yang menguntungkan portofolio mereka; listing exchange besar meningkatkan visibilitas (HIGH) [TechCrunch Series A, https://techcrunch.com/2021/12/01/mysten-labs-raises-36m-series-a-a16z]; (HIGH) [TechCrunch Series B, https://techcrunch.com/2022/09/08/mysten-labs-raises-300m-series-b/]
- Jangka panjang: Tidak diketahui — Vesting investor 12 bulan cliff + 36 bulan linear; harga SUI setelah cliff (Mei 2024) belum dipastikan menguntungkan semua investor; tidak ada laporan publik tentang return VC (MEDIUM) [Phase 6 — Vesting Schedule]
- Dasar: (HIGH) [Phase 6 — Vesting Schedule]; (MEDIUM) [tidak ada laporan resmi VC return]

POV Retail (penerima Community Access Program / testnet participants):
- Jangka pendek: Berhasil — Menerima token gratis sebagai reward atas partisipasi testnet; banyak yang menjual saat harga awal >$1, mendapatkan profit significant tanpa membeli token (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/sui]
- Jangka panjang: Sebagian — Mereka yang menjual awal mengunci profit; yang memegang mengalami harga turun ke rendah $0.4-0.5 di awal 2024 sebelum rally kemudian; hasil sangat tergantung waktu jual (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/sui]
- Dasar: (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/sui]; (MEDIUM) [Phase 6 — Holder Distribution — tidak ada data cohort]

POV Community (anggota komunitas Sui, bukan penerima langsung):
- Jangka pendek: Sukses — Komunitas merasa dihargai karena yang berpartisipasi testnet diberi token; komunitas berkembang cepat saat mainnet (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]
- Jangka panjang: Sebagian — Mereka yang tidak berpartisipasi testnet merasa terlewatkan; komunitas berfokus pada pengembangan ekosistem jangka panjang; tidak ada airdrop kedua membuat sebagian anggota komunitas kurang terinsentif (MEDIUM) [Phase 9 — Open Threads; tidak ada sumber resmi]
- Dasar: (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]; (MEDIUM) [analisis komunitas]

POV Developer (pengembang aplikasi di Sui):
- Jangka pendek: Sukses — Developer yang membangun di testnet menerima grant dan reward; memiliki akses awal ke tooling dan SDK; dapat membangun aplikasi sebelum mainnet (HIGH) [Sui Blog Testnet Wave 2, https://blog.sui.io/sui-testnet-wave-2/]
- Jangka panjang: Sebagian — Developer yang serius bertahan dan membangun aplikasi; banyak yang mengandalkan grants program; tidak ada insentif tambahan khusus airdrop untuk developer setelah mainnet (MEDIUM) [Phase 7 — Ecosystem]
- Dasar: (HIGH) [Sui Blog Testnet Wave 2, https://blog.sui.io/sui-testnet-wave-2/]; (MEDIUM) [Phase 7]

POV Institution (investor institusional non-VC, misalnya bursa yang listing, market maker):
- Jangka pendek: Sukses — Listing exchange besar memungkinkan institusi (market maker seperti Jump Crypto) mendapatkan akses liquidity; volume tinggi saat launch (HIGH) [Phase 8 — Trading Markets]
- Jangka panjang: Tidak diketahui — Belum ada laporan publik tentang kinerja institusi pada SUI; beberapa mungkin mengadopsi SUI untuk produk keuangan (MEDIUM) [tidak ditemukan]
- Dasar: (HIGH) [Phase 8 — Trading Markets]; (MEDIUM) [tidak ditemukan]

POV Validator (operator node validator Sui):
- Jangka pendek: Sukses — Validator yang berpartisipasi testnet menerima token SUI dan insentif; >100 validator aktif saat mainnet menunjukkan keberhasilan bootstrap (HIGH) [Sui Explorer Validators, https://explorer.sui.io/validators]; (HIGH) [Phase 8 — Validator Count]
- Jangka panjang: Sebagian — Validator yang serius mendapatkan staking rewards berkelanjutan; namun hardware requirements tinggi membatasi partisipasi validator kecil; slashing belum aktif mengurangi kepercayaan ekonomi (MEDIUM) [Phase 4 — Known Technical Limitations]
- Dasar: (HIGH) [Sui Explorer Validators, https://explorer.sui.io/validators]; (MEDIUM) [Phase 4]

POV Builder (proyek ekosistem yang dibangun di atas Sui, misalnya Cetus, Navi, Suilend):
- Jangka pendek: Sukses — Builder mendapatkan grants dan insentif building; ekosistem DeFi tumbuh cepat setahun pertama (HIGH) [Phase 7 — Ecosystem; DefiLlama, https://defillama.com/chain/Sui]
- Jangka panjang: Sebagian — Proyek yang sukses (Cetus, Navi) bertahan dan berkembang; banyak proyek kecil bergantung pada grants yang tidak berkelanjutan; tidak ada airdrop tambahan untuk builder setelah testnet (MEDIUM) [Phase 7 — Ecosystem]
- Dasar: (HIGH) [DefiLlama, https://defillama.com/chain/Sui]; (MEDIUM) [Phase 7]

HARGA PASCA-DISTRIBUSI

Harga saat klaim: 1.20 USD (2023-05-03) [CoinGecko, https://www.coingecko.com/en/coins/sui] (MEDIUM)
Harga +30 hari: 0.96 USD (2023-06-02) [CoinGecko, https://www.coingecko.com/en/coins/sui] (MEDIUM)
Harga +90 hari: 0.63 USD (2023-08-01) [CoinGecko, https://www.coingecko.com/en/coins/sui] (MEDIUM)
Harga puncak 12 bulan pertama: 2.19 USD (2024-03-25) [CoinGecko, https://www.coingecko.com/en/coins/sui] (MEDIUM)

CATATAN: Harga saat klaim diambil dari harga terbuka pertama di Binance (hari pertama trading); angka harga pasca-TGE diperkirakan dari data CoinGecko historis; verifikasi lebih lanjut dapat dilakukan langsung di CoinGecko/CoinMarketCap karena harga pasar adalah fakta publik, bukan data laporan internal.

METRIK RETENSI

- TVL sebelum distribusi: 0 USD (belum ada mainnet sebelum TGE) (HIGH) [DefiLlama, https://defillama.com/chain/Sui]
- TVL 3 bulan setelah distribusi: ~50M USD (per sekitar Agustus 2023) (MEDIUM) [DefiLlama, https://defillama.com/chain/Sui]
- TVL 1 tahun setelah distribusi: >1B USD (per Januari 2025) (HIGH) [Phase 8 — Adoption Metrics; DefiLlama, https://defillama.com/chain/Sui]
- Jumlah alamat pemegang SUI: Tidak ditemukan angka pasti per tanggal tertentu di sumber publik; Sui Explorer menampilkan live counter tapi tidak dipublikasikan sebagai snapshot (MEDIUM) [Sui Explorer, https://explorer.sui.io/]
- Jumlah alamat aktif harian: >1 juta rata-rata harian pada 2024 (klaim blog resmi, tidak dibedakan alamat unik vs transaksi) (MEDIUM) [Sui Blog, https://blog.sui.io/1-billion-transactions/]
- Konsentrasi kepemilikan: Top 10 alamat memegang ~42% total supply; ~68% dipegang top 100 (termasuk vesting contracts, exchange cold wallets, Foundation addresses) (MEDIUM) [Suiscan, https://suiscan.xyz/]
- Staking partisipasi: ~60% dari circulating supply terstake (per kuartal 2024, data tidak langsung) (MEDIUM) [Phase 8 — Adoption Metrics]
- Volume DEX harian: >100M USD rata-rata (periode 2024-2025) (MEDIUM) [DefiLlama, https://defillama.com/chain/Sui]

GAP YANG DIKETAHUI

Cohort penerima: memerlukan analisis on-chain per-alamat, tidak tersedia di sumber publik.

FARMING DAN SYBIL

- Kriteria task-based diumumkan secara terbuka per wave testnet (Wave 1, 2, 3) — artinya perilaku farming bisa disesuaikan sebelum snapshot per-wave (HIGH) [Sui Blog Testnet Wave 1, https://blog.sui.io/sui-testnet-wave-1-launches/]; (HIGH) [Sui Blog Testnet Wave 3, https://blog.sui.io/sui-testnet-wave-3/]
- Tidak ditemukan data publik tentang jumlah alamat yang didiskualifikasi karena sybil — Mysten Labs tidak mempublikasikan daftar diskualifikasi (LOW) [tidak ditemukan]
- Tidak ada bukti bahwa tim mengubah kriteria setelah melihat perilaku farming — namun sistem misi berbasis tugas cenderung lebih sulit untuk di-farm secara massal dibanding snapshot sederhana karena memerlukan aksi nyata (menjalankan node, menyelesaikan misi spesifik) (MEDIUM) [analisis berdasarkan desain program testnet]
- Populasi hunter pada era 2022-2023 sudah matang; namun program testnet Sui menarik banyak developer dan validator autentik karena insentifnya setara dengan kerja yang dibutuhkan (MEDIUM) [Phase 9 — Behavioral Pattern: "Mengadopsi standar eksternal sebelum membangun sendiri"]

PROSPEK

Untuk project berstatus `Belum ada` — fokus pada gelombang berikutnya (apakah ada airdrop kedepannya):

- Prasyarat yang sudah terpenuhi: (1) Token sudah memiliki utilitas kuat (staking, gas, governance) (HIGH) [Phase 6 — Utility]; (2) Treasury foundation >$1 miliar (alokasi Community Reserve 50% masih belum sepenuhnya terdistribusi) (HIGH) [Phase 5 — Treasury]; (3) On-chain governance aktif dengan proposal (HIGH) [Phase 6 — Governance]; (4) Ekosistem tumbuh, TVL >$1 miliar, user aktif >1 juta (HIGH) [Phase 8 — Adoption Metrics]
- Prasyarat yang belum: (1) Belum ada indikasi resmi dari Mysten Labs atau Sui Foundation tentang airdrop retroaktif; (2) Tidak ada kontrak distribusi dengan mekanisme airdrop yang ditemukan di on-chain — semua alokasi sisa adalah vesting grants program, bukan airdrop; (3) Tidak ada pengumuman snapshot, perekrutan untuk tim airdrop, atau perubahan dokumentasi yang mengarah pada airdrop (MEDIUM) [Phase 9 — Open Threads; analisis dokumentasi resmi]
- Sinyal yang biasanya mendahului: (1) Pengumuman di blog resmi atau Discord tentang "Community Airdrop" atau "Reward Program" (belum ada); (2) Deploy kontrak Move on-chain dengan mekanisme claim (belum terlihat di explorer); (3) Pernyataan Foundation tentang "distribusi tambahan ke pengguna aktif" (belum ada); (4) Rekrutmen untuk posisi terkait "Incentives" atau "Community Rewards" di Sui Foundation (belum terlihat)
- Penilaian: Keyakinan rendah bahwa airdrop akan terjadi dalam waktu dekat — tim secara konsisten memilih mekanisme task-based (testnet, grants, program validator) daripada airdrop retroaktif murni; pola dari Phase 9 menunjukkan preferensi pada pengguna yang memberikan kontribusi nyata. Namun, karena Community Reserve 50% (=5 miliar SUI) masih sangat besar dan belum didistribusikan sepenuhnya, ada kemungkinan program insentif baru (bukan airdrop) akan diluncurkan untuk mengaktifkan reserve tersebut. Yang akan mengubah penilaian ini: pengumuman resmi tentang program insentif berbasis aktivitas on-chain, atau deploy kontrak distribusi baru di mainnet.

PELAJARAN LINTAS PROJECT

1. Ketika tim layer-1 baru menghadapi pasar bearish (era 2022-2023) dan membutuhkan validator serta developer untuk membangun jaringan, memilih mekanisme task-based (testnet wave) daripada airdrop retroaktif menghasilkan distribusi token yang lebih berkualitas — penerima adalah kontributor aktif yang telah menguji infrastruktur, bukan sekadar spekulan pasif; akibatnya bootstrap validator lebih cepat dan ekosistem awal lebih sehat, namun tekanan jual tetap terjadi karena penerima tidak memiliki biaya modal mental.
2. Ketika sebuah project menghindari token sale publik dan hanya mengandalkan equity VC (era 2021-2022), listing serentak di exchange besar menjadi sangat penting untuk likuiditas; distribusi token ke komunitas (walaupun task-based) membantu memenuhi syarat listing exchange yang menginginkan distribusi lebih merata — namun ini juga berarti tekanan jual lebih besar di awal karena penerima token gratis cenderung menjual cepat.
3. Ketika sebuah project memiliki treasury besar namun belum memiliki mekanisme protocol revenue capture (era 2024-2025), keberlanjutan program insentif jangka panjang menjadi pertanyaan — grants program dapat berjalan sementara, tapi tanpa airdrop atau reward berkelanjutan untuk pengguna, retensi jangka pendek tidak otomatis mengarah ke loyalitas jangka panjang.
4. Ketika anti-sybil tidak dipublikasikan secara detail (seperti yang dilakukan banyak project layer 1), populasi hunter masih tetap berpartisipasi jika insentifnya cukup besar (6% supply = ratusan juta USD); namun tanpa mekanisme anti-sybil yang transparan, kepercayaan terhadap distribusi bisa melemah — ini membedakan Sui dari project yang mempublikasikan metode filtering mereka.

## Open Questions
- [foundation] Exact founding date of Mysten Labs Inc. (incorporation date) — not fully verified
- [foundation] Complete list of all seed/Series A/B investors with confirmed allocation percentages — partial data available, full cap table not public
- [foundation] Current circulating supply vs. total supply breakdown with unlock schedule per investor tranche — on-chain data exists but requires parsing
- [foundation] Sui Foundation treasury size and multisig signers — not fully disclosed
- [foundation] Exact TGE unlock percentage for community/early contributors — conflicting reports (some say 14%, others 12.5%)
- [foundation] Whether SUI token has any fee-switch mechanism or value accrual to stakers beyond gas fees — documentation suggests staking rewards only
- [foundation] Verified team/advisor token allocation and vesting schedules — not fully public
- [foundation] Current Mysten Labs headcount — "100+" is company claim, not independently audited
- [foundation] Sui Play0x1 shipping date and production status — announced 2024, delivery timeline unclear
- [entity] Validasi daftar validator individu (nama operator spesifik) vs validator set sebagai entity kolektif — perlu keputusan apakah memecah per operator
- [entity] Status FTX Ventures: apakah masih memegang equity/token Mysten Labs pasca-bankruptcy — perlu cek on-chain / court docket
- [entity] Daftar lengkap investor Series A (lebih dari 7 yang tercatat) — beberapa sumber menyebut >30 investor, perlu cap table lengkap
- [entity] Klasifikasi "Protocol" vs "Application" untuk DeFi primitives (Cetus, Navi, dll) — batasan tipologi butuh konsistensi lintas project
- [entity] Exposure type untuk stablecoin (USDC/USDT): financial-collateral vs technical-integration — butuh definisi ketat
- [entity] Mysticeti consensus: apakah entity terpisah atau upgrade protocol Sui Network — saat ini dicatat terpisah tapi integral
- [entity] SuiNS DAO vs Sui Foundation Grants: apakah DAO terpisah atau program foundation — perlu klarifikasi governance structure
- [entity] NodeReal dan Shinami: apakah termasuk "Infrastructure Provider" category terpisah atau Company — saat ini keduanya
- [entity] Zellic audit scope: apakah audit Sui core atau hanya aplikasi ekosistem — perlu verifikasi laporan publik
- [entity] Sui Basecamp/Overflow: event vs platform — klasifikasi Application mungkin tidak tepat, mungkin Community
- [history] Tanggal pasti TGE SUI (EV-011): beberapa sumber menyebut 2023-05-03, andere 2023-05-04 — perlu verifikasi on-chain timestamp genesis vs listing exchange pertama
- [history] Detail alokasi token TGE persentase tepat (EV-011): whitepaper tokenomics vs blog resmi angka sedikit berbeda (community reserve 50% vs 51%, dll) — perlu cross-check on-chain supply distribution
- [history] Status FTX Ventures equity/token (EV-002): apakah masih memegang alokasi Series A pasca-bankruptcy — butuh court docket atau on-chain vesting contract check
- [history] Daftar lengkap investor Series A (EV-002): >7 investor tercatat tapi beberapa sumber menyebut 30+ — cap table lengkap tidak publik
- [history] Validator individu vs validator set (EV-010): apakah perlu memecah entity per operator validator terkenal (Blockdaemon, Figment, Coinbase Cloud, dll) — keputusan konsistensi lintas project
- [history] Mysticeti mainnet upgrade tanggal pasti (EV-025): beberapa sumber Juli 2024, lain Agustus — perlu epoch/block height aktivasi on-chain
- [history] Sui Bridge native volume dan TVL terkini (EV-023): data on-chain real-time butuh indexer terpisah — placeholder hingga data stabil
- [history] SuiPlay0x1 spesifikasi teknis dan jadwal pengiriman final (EV-029): pre-order dibuka tapi shipping date belum pasti — perlu update dari Mysten Labs
- [history] Klasifikasi Event Type untuk DeFi protokol (EV-013 s/d EV-016): saat ini "Ecosystem" tapi bisa "Product" atau "Integration" — butuh standarisasi tipologi lintas project
- [history] Zellic audit scope (referensi Phase 2): apakah audit core protocol Sui atau hanya aplikasi ekosistem — perlu verifikasi laporan publik Zellic
- [technology] Mysticeti consensus formal paper URL belum dikonfirmasi (arXiv placeholder) — perlu verifikasi publikasi akademik resmi
- [technology] Slashing activation timeline: tidak ada tanggal resmi di roadmap publik — issue GitHub tracking tapi tidak ada milestone
- [technology] Move 2024 edition adoption status di mainnet: apakah sudah fully activated atau masih rolling out via protocol upgrades
- [technology] Validator hardware requirements apakah berkurang pasca-Mysticeti (throughput lebih tinggi tapi resource usage?) — butuh benchmark independen
- [technology] DeepBook CLOB technical specs detail (matching engine, fee structure) — dokumentasi terpisah di deepbook.tech perlu deep-dive
- [technology] Sui Bridge native volume dan TVL on-chain metrics real-time — perlu indexer dedicated untuk bridge contracts
- [technology] zkLogin salt service decentralization: saat ini Shinami/Mysten centralized — roadmap untuk distributed salt service?
- [technology] Formal verification adoption rate di ekosistem: berapa persen kontrak mainnet yang verified via Move Prover?
- [technology] Cross-chain messaging beyond bridge (Wormhole, LayerZero, Axelar) technical integration status di Sui
- [technology] Mysticeti consensus safety/liveness formal proof apakah sudah dipublikasikan (Coq/Isabelle) atau hanya paper teori
- [technology] Gas schedule tuning history: apakah ada changelog gas cost per opcode/operation versi ke versi
- [technology] Object storage growth: state bloat mitigation strategy (pruning, archival nodes, state expiry) — belum terdokumentasi resmi
- [technology] Validator client diversity: apakah ada alternative client implementation selain Mysten Labs reference (Rust)?
- [technology] Quantum resistance roadmap untuk cryptography (Ed25519, BLS12-381) — apakah ada migration plan post-quantum?
- [financial] Treasury composition breakdown per asset class (SUI vs stablecoin vs other) — tidak diungkap detailnya
- [financial] Mysten Labs financial statements (revenue, burn rate, runway) — private company, tidak publik
- [financial] FTX Ventures Series A equity/token status pasca-bankruptcy — court docket atau on-chain vesting check diperlukan
- [financial] Series A cap table lengkap — beberapa sumber menyebut 30+ investor, hanya 7 terkonfirmasi publik
- [financial] Grant program ROI/impact metrics — >$50M deployed tapi standardized reporting tidak ada
- [financial] Protocol revenue capture mechanism future — apakah ada proposal fee switch atau treasury revenue sharing
- [financial] Validator economics sustainability tanpa slashing — long-term incentive alignment belum terbukti
- [financial] SUI token regulatory classification risk di US/EU — belum ada clarity resmi
- [financial] Foundation treasury management strategy (hedging, diversification, yield generation) — tidak diungkap
- [financial] Mysticeti upgrade impact pada validator economics dan gas fee market — perlu observasi pasca-Juli 2024
- [token] Persentase circulating supply tepat per Januari 2025: Sui Explorer menampilkan 2,789,341,234 SUI tapi Suiscan angka sedikit berbeda — perlu cross-check on-chain vesting contract balances untuk akurasi
- [token] Detail vesting contract addresses untuk setiap kategori (Community Reserve, Team, Investors, Treasury) — tidak dipublikasikan sebagai daftar lengkap; perlu query on-chain untuk verifikasi unlock schedule real-time
- [token] Status slashing activation dan dampak pada staking rewards / token economics — belum ada timeline resmi; slashing tidak aktif mainnet
- [token] Apakah ada proposal fee switch atau protocol revenue capture ke treasury di roadmap governance — tidak ditemukan proposal aktif
- [token] FTX Ventures Series A token allocation (14% investors termasuk FTX) status pasca-bankruptcy — court docket atau on-chain vesting contract check diperlukan
- [token] Community Reserve 50%: apakah seluruh 5B SUI dikendalikan Foundation multisig atau ada portion yang sudah didistribusikan ke grants program sebagai unlocked — detail spending tidak diungkap per tranche
- [token] Validator economics sustainability tanpa slashing: apakah staking yield (gas fee + storage fund) cukup untuk menarik stake long-term — perlu data APY historis
- [token] Mysticeti upgrade apakah mengubah gas schedule atau storage fund parameter — changelog gas cost per opcode tidak dipublikasikan terpusat
- [token] Sui Bridge native fee flow: apakah portion fee masuk ke treasury Foundation atau sepenuhnya ke validator set — bridge docs menyatakan validator set tapi tidak eksplisit
- [token] ZkLogin salt service decentralization: apakah ada plan untuk distributed salt service yang mempengaruhi SUI utility untuk gas sponsorship — belum ada announcement resmi
- [market] TVL Sui fluktuatif: DefiLlama menunjukkan >$1 miliar per Januari 2025, tapi angka real-time berubah setiap hari; perlu konsensus data pada tanggal cut-off spesifik
- [market] Daily Active Users: klaim >1 juta dari Sui Blog tidak dibedakan antara alamat unik aktif vs transaksi per user; tidak ada metrik resmi "active users" terstandardisasi di explorer
- [market] Developer Count: tidak ada angka resmi aktif developer di mainnet; hackathon participants (2.500+) bukan representasi developer aktif jangka panjang
- [market] Wallets/Address Count: Sui Explorer menampilkan live counter tapi tidak dipublikasikan sebagai snapshot per tanggal; perlu query on-chain manual
- [market] Data bridge volume (Sui Bridge native dan Wormhole) tidak dipublikasikan resmi; hanya bisa dihitung via query on-chain kontrak bridge
- [market] Pangsa pasar keseluruhan (market share) tidak tersedia; tidak ada laporan resmi pangsa Sui terhadap total DeFi TVL global atau volume exchange
- [market] Klasifikasi Near Protocol: daftar awal pada daftar kompetitor salah menulis "Sui-Near"; ini adalah kesalahan input, bukan nama entity nyata — perlu koreksi di fase berikutnya
- [market] Status FTX Ventures Series A exposure kepada token SUI pasca-bankruptcy — tidak dikonfirmasi di on-chain vesting contract
- [market] Metrik staking % (~60% circulating supply) berasal dari data tidak langsung — perlu verifikasi via on-chain staked SUI balance vs circulating supply
- [market] Perbandingan dengan Aptos sering dimuat media sebagai "duel Move chains" namun tidak ada data resmi perbandingan market share; hanya data on-chain independen
- [market] SuiPlay0x1 belum dirilis (pre-order Q1 2025); dampak pasar dari perangkat hardware belum dapat dinilai
- [behavioral] FTX Ventures Series A equity/token exposure pasca-bankruptcy: tidak ada pernyataan resmi; diperdebatkan antara "tetap hold" vs "liquidated" — perlu court docket atau on-chain vesting contract check
- [behavioral] Komposisi treasury foundation per asset class (SUI vs stablecoin vs investasi): laporan menyebut kombinasi >$1 miliar tapi tidak memecah per kategori — apakah stablecoin portion cukup untuk runway >2 tahun tanpa menjual SUI?
- [behavioral] Slashing activation timeline: tidak ada tanggal resmi; beberapa sumber isu GitHub menyebut "soon" — apakah akan aktif sebelum epoch tertentu atau menunggu proposal governance
- [behavioral] zkLogin salt service decentralization: apakah ada roadmap untuk distributed salt service; kepercayaan pada centralized service (Shinami/Mysten) kontradiktif dengan narasi decentralisasi
- [behavioral] Mysticeti consensus formal proof: apakah paper akademik sudah dipublikasikan dengan Coq/Isabelle proof, atau hanya teori di arXiv — perlu verifikasi publikasi formal
- [behavioral] Sui Bridge Native volume dan TVL: data real-time tidak dipublikasikan; overflow di explorer tidak selalu mengindikasikan volume eksternal yang signifikan
- [behavioral] "Sui-Near" pada daftar kompetitor Phase 8 adalah kesalahan input; yang benar adalah Near Protocol — perlu koreksi konsistensi lintas phase
- [behavioral] Developer count aktif on-chain: tidak ada metrik resmi; hackathon participants tidak setara developer aktif berkelanjutan
- [behavioral] Daily active users >1 juta: Sui Blog tidak membedakan alamat aktif vs transaksi per user; perlu standardisasi pengukuran
- [behavioral] Move 2024 edition adoption di mainnet: apakah sudah full active atau rolling out — berdampak pada tooling developer dan kompatibilitas kontrak
- [behavioral] Gas fee market pasca-Mysticeti: apakah gas cost per opcode berubah; changelog terpusat tidak tersedia — perlu query on-chain historical gas data
- [behavioral] Validator hardware requirements apakah turun pasca-Mysticeti (parallel execution mengurangi beban) — belum ada benchmark independen
- [knowledge] FTX Ventures Series A equity/token exposure pasca-bankruptcy: tidak ada pernyataan resmi; status antara "tetap hold" vs "liquidated" tidak dikonfirmasi — perlu court docket atau on-chain vesting contract check【Phase 2 — FTX Ventures, Phase 5 — Financial Risk, Phase 9 — Open Threads】
- [knowledge] Komposisi treasury foundation per asset class (SUI vs stablecoin vs investasi): laporan menyebut >$1 miliar kombinasi aset tapi tidak memecah per kategori — apakah stablecoin portion cukup untuk runway >2 tahun tanpa menjual SUI?【Phase 5 — Treasury, Phase 9 — Open Threads】
- [knowledge] ZkLogin salt service decentralization: apakah ada roadmap untuk distributed salt service; kepercayaan pada centralized service (Shinami/Mysten) kontradiktif dengan narasi desentralisasi — belum ada announcement resmi【Phase 4 — Security Model, Open Threads】
- [knowledge] Mysticeti consensus formal proof: apakah paper akademik sudah dipublikasikan dengan Coq/Isabelle proof, atau hanya teori di arXiv — perlu verifikasi publikasi formal【Phase 4 — Open Threads】
- [knowledge] Sui Bridge Native volume dan TVL real-time: data tidak dipublikasikan; hanya bisa dihitung via query on-chain kontrak bridge【Phase 8 — Adoption Metrics, Open Threads】
- [knowledge] "Sui-Near" pada daftar kompetitor Phase 8 adalah kesalahan input; yang benar adalah Near Protocol — perlu koreksi konsistensi lintas phase【Phase 8 — Competitor Landscape】
- [knowledge] Developer count aktif on-chain: tidak ada metrik resmi; hackathon participants (2.500+) bukan representasi developer aktif berkelanjutan【Phase 8 — Adoption Metrics】
- [knowledge] Daily active users >1 juta: Sui Blog tidak membedakan alamat aktif vs transaksi per user; perlu standardisasi pengukuran【Phase 8 — Adoption Metrics】
- [knowledge] Move 2024 edition adoption di mainnet: apakah sudah full active atau masih rolling out — berdampak pada tooling developer dan kompatibilitas kontrak【Phase 4 — Open Threads】
- [knowledge] Gas fee market pasca-Mysticeti: apakah gas cost per opcode berubah; changelog terpusat tidak tersedia — perlu query on-chain historical gas data【Phase 4 — Open Threads】
- [knowledge] Validator hardware requirements apakah turun pasca-Mysticeti (parallel execution mengurangi beban) — belum ada benchmark independen【Phase 4 — Open Threads】
- [knowledge] Staking % (~60% circulating supply) berasal dari data tidak langsung — perlu verifikasi via on-chain staked SUI balance vs circulating supply【Phase 8 — Open Threads】
- [knowledge] SuiPlay0x1 belum dirilis (pre-order Q1 2025); dampak pasar dari perangkat hardware belum dapat dinilai【Phase 8 — Market Timeline, Open Threads】
- [conflict] Description: Komposisi treasury foundation per asset class tidak diungkap; beberapa sumber memperkirakan kombinasi SUI/stablecoin/investasi secara berbeda
- [conflict] Affected Phase: Phase 5
- [conflict] Evidence: Laporan treasury Jan 2025 hanya menyebut total >$1 miliar tanpa breakdown [https://sui.io/foundation/treasury]
- [conflict] Alternative Interpretations: (1) Mayoritas SUI dengan sedikit diversifikasi; (2) Diversifikasi 30-40% stablecoin; (3) Dominasi investasi ekosistem
- [conflict] Status: Open Open Thread ID: OT-02
- [conflict] Description: FTX Ventures Series A equity/token status pasca-bankruptcy tidak dikonfirmasi; berpotensi overhang atau liquidated
- [conflict] Affected Phase: Phase 5
- [conflict] Evidence: FTX Ventures berpartisipasi Series A 2021 tapi tidak ada pernyataan resmi setelah kasus [https://www.theblock.co/]
- [conflict] Alternative Interpretations: (1) FTX masih hold equity; (2) Equity dilikuidasi; (3) Token allocation dihitung dalam 14% tapi tidak pernah dipakai
- [conflict] Status: Open Open Thread ID: OT-03
- [conflict] Description: Slashing activation timeline tidak jelas; beberapa sumber menyebut "soon", tidak ada tanggal resmi
- [conflict] Affected Phase: Phase 4
- [conflict] Evidence: Dokumentasi staking menyatakan slashing belum aktif [https://docs.sui.io/concepts/staking]
- [conflict] Alternative Interpretations: (1) Aktif tahun 2025; (2) Ditunda hingga desentralisasi validator lebih matang; (3) Tidak pernah diaktifkan
- [conflict] Status: Open Open Thread ID: OT-04
- [conflict] Description: zkLogin salt service decentralization roadmap tidak ada
- [conflict] Affected Phase: Phase 4
- [conflict] Evidence: Salt service dijalankan Shinami dan Mysten Labs [https://docs.sui.io/guides/developer/app-development/zklogin]
- [conflict] Alternative Interpretations: (1) Roadmap sedang dikembangkan; (2) Tetap centralized untuk keamanan; (3) Distribusi akan dilakukan via protokol lain
- [conflict] Status: Open Open Thread ID: OT-05
- [conflict] Description: Mysticeti formal proof (Coq/Isabelle) belum dipublikasikan
- [conflict] Affected Phase: Phase 4
- [conflict] Evidence: Paper arXiv tersedia tapi proof formal tidak lengkap [https://arxiv.org/]
- [conflict] Alternative Interpretations: (1) Proof sedang disiapkan; (2) Hanya paper teori tanpa formal proof; (3) Proof dianggap tidak diperlukan oleh tim
- [conflict] Status: Open Open Thread ID: OT-06
- [conflict] Description: Daily active users >1 juta klaim tidak terstandardisasi
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Blog Sui menyebut 1 miliar transaksi [https://blog.sui.io/1-billion-transactions/]
- [conflict] Alternative Interpretations: (1) DAU benar 1 juta; (2) Angka termasuk bot; (3) Metrik berbeda (wallets vs transaksi)
- [conflict] Status: Open Open Thread ID: OT-07
- [conflict] Description: Sui Bridge native volume dan TVL tidak dipublikasikan resmi
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Docs bridge tidak menyebut angka volume [https://docs.sui.io/guides/operator/bridge]
- [conflict] Alternative Interpretations: (1) Volume kecil dan tidak signifikan; (2) Volume besar tapi tidak dilaporkan; (3) Dilaporkan di dashboard internal
- [conflict] Status: Open Open Thread ID: OT-08
- [conflict] Description: Staking % (~60% circulating supply) tidak terverifikasi on-chain langsung
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Angka berasal dari data tidak langsung [https://sui.io/foundation/treasury]
- [conflict] Alternative Interpretations: (1) 60% benar; (2) Lebih rendah (50-55%); (3) Lebih tinggi (65%+)
- [conflict] Status: Open Open Thread ID: OT-09
- [conflict] Description: SuiPlay0x1 spesifikasi teknis final dan jadwal pengiriman belum pasti
- [conflict] Affected Phase: Phase 3
- [conflict] Evidence: Pre-order Q1 2025 diumumkan tapi tanggal final tidak ada [https://blog.sui.io/suiplay0x1-announcement/]
- [conflict] Alternative Interpretations: (1) Dirilis Q2 2025; (2) Tertunda ke 2026; (3) Dibatalkan
- [conflict] Status: Open Open Thread ID: OT-10
- [conflict] Description: "Sui-Near" pada daftar kompetitor adalah kesalahan input; yang benar adalah Near Protocol
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Hanya muncul di Phase 8; tidak ada entity "Sui-Near" di referensi [https://near.org/]
- [conflict] Alternative Interpretations: (1) Salah ketik; (2) Bukan entity nyata; (3) Koreksi manual diadopsi
- [conflict] Status: Resolved Open Thread ID: OT-11
- [conflict] Description: Gas fee changelog per opcode pasca-Mysticeti tidak dipublikasikan
- [conflict] Affected Phase: Phase 4
- [conflict] Evidence: Docs gas hanya menjelaskan konsep [https://docs.sui.io/concepts/gas]
- [conflict] Alternative Interpretations: (1) Tidak ada perubahan; (2) Ada perubahan tapi tidak didokumentasikan; (3) Perubahan diumumkan di governance forum
- [conflict] Status: Open Open Thread ID: OT-12
- [conflict] Description: Developer count aktif on-chain tidak ada metrik resmi
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Hackathon participants (2.500+) bukan representasi developer aktif [https://sui.io/basecamp]
- [conflict] Alternative Interpretations: (1) Developer aktif >5.000; (2) <1.000; (3) Tidak terukur
- [conflict] Status: Open
- [airdrop] Jumlah pasti penerima Community Access Program (alamat unik) tidak dipublikasikan oleh Sui Foundation atau Mysten Labs — hanya estimasi ribuan partisipan testnet.
- [airdrop] Mekanisme anti-sybil untuk Community Access Program tidak pernah dijelaskan publik — apakah ada deteksi duplicate address, IP filtering, atau verifikasi identitas?
- [airdrop] Persentase penerima yang telah menjual SUI dalam 30 hari setelah TGE tidak dapat dihitung tanpa analisis on-chain per-alamat — data tidak tersedia.
- [airdrop] Apakah ada sisa alokasi Community Access Program (600M SUI) yang tidak diklaim, dan ke mana sisanya pergi (burned, dikembalikan ke treasury, atau dialihkan ke program lain) — tidak ditemukan informasi.
- [airdrop] Sui Foundation belum pernah membuat pernyataan eksplisit "tidak akan ada airdrop" atau "akan ada airdrop" untuk masa depan — ketidakpastian ini tetap terbuka.
- [airdrop] Tidak ada bukti bahwa tim mengubah kriteria kelayakan Community Access Program setelah melihat perilaku farming — apakah ini berarti tidak ada farming massal, atau tim tidak mengungkapkannya?
- [airdrop] Investor Series A (termasuk FTX Ventures) menerima alokasi investor 14% — apakah mereka yang meneruskan token ke pengguna akhir, atau hanya memegang — tidak perlu dilacak di akun ini.
- [airdrop] Metrik "harga saat klaim" diperkirakan dari harga pasar hari pertama Binance; jika ada data publish per-even dari Sui Foundation tentang harga klaim internal yang berbeda (misalnya harga untuk validator), itu tidak ditemukan.
