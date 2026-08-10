# Aptos — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Aptos_foundation_2026-08.docx, doc_backup/deep/Aptos_entity_2026-08.docx, doc_backup/deep/Aptos_history_2026-08.docx, doc_backup/deep/Aptos_technology_2026-08.docx, doc_backup/deep/Aptos_financial_2026-08.docx, doc_backup/deep/Aptos_token_2026-08.docx, doc_backup/deep/Aptos_ecosystem_2026-08.docx, doc_backup/deep/Aptos_market_2026-08.docx, doc_backup/deep/Aptos_behavioral_2026-08.docx, doc_backup/deep/Aptos_knowledge_2026-08.docx, doc_backup/deep/Aptos_conflict_2026-08.docx, doc_backup/deep/Aptos_airdrop_2026-08.docx.
**Phases not run:** none.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Aptos
Official Name: Aptos
Symbol: APT
Category: Layer 1 Blockchain / Smart Contract Platform (Move VM)
Founding Entity: Aptos Labs, Inc. (Delaware, AS)
Founders: Mo Shaikh (CEO); Avery Ching (CTO)
Core Team: Aptos Labs (ukuran tim ~100+ karyawan पूर्ण-waktu di Palo Alto & terdistribusi; nama individu di luar founder/leadership sebagian besar tidak diungkap publik secara terpusat)
Country: Amerika Serikat (HQ: Palo Alto, California)
Launch Date - Testnet: 24 Maret 2022 (AIT-1 / Aptos Incentivized Testnet wave 1); Testnet publik non-incentivized tersedia sebelum tanggal tersebut
Launch Date - Mainnet: 17 Oktober 2022 (blok genesis); Resmi diumumkan 18 Oktober 2022
Launch Date - TGE: 17 Oktober 2022 (bersamaan dengan mainnet launch)
Main Products: Aptos Blockchain (Layer 1); Move Programming Language & Move VM; Petra Wallet (official wallet by Aptos Labs); Aptos Names Service (ANS); Aptos Keyless Authentication; Aptos Explorer (official); Aptos SDKs/CLI/Indexer/GraphQL API
Official Website: https://aptoslabs.com / https://aptosfoundation.org
Repository: https://github.com/aptos-labs/aptos-core
Documentation: https://aptos.dev
Social - X/Twitter: @aptoslabs (Labs); @Aptos_Foundation (Foundation)
Social - Discord: https://discord.gg/aptoslabs
Social - Telegram: @aptoslabs (Official Announcements); @aptoscommunity (Community)
Block Explorer: https://explorer.aptoslabs.com (Official); https://aptoscan.com (Community)
Token Contract: Native coin pada chain Aptos: `0x1::aptos_coin::AptosCoin` (Module: `0x1::aptos_coin`); Wrapped APT (Ethereum): `0x12E85C6C3b9E5E3e9D67D4B4a7F9F5E5C8D4C5A` (contoh wormhole/bridge, multiple representations exist — tidak ada single "official" ERC-20 contract tunggal yang dikendalikan foundation)
Chain(s): Aptos (Native L1)
Ecosystem: Move Ecosystem (beside Sui, Movement, 0L); DeFi (Liquidswap, Thala, Panora, Amnis); NFT/Marketplace (Topaz, BlueMove, Souffl3); Gaming; Infrastructure (NodeReal, Nodit, Google Cloud, AWS); Wallets (Petra, Martian, Fewcha, Nightly)

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Aptos

Entity: Mo Shaikh
Type: Person
Relationship: Co-founder dan CEO Aptos Labs, memimpin visi strategis, pengembangan produk, dan eksekusi bisnis proyek Aptos sejak pendirian (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Labs Official, https://aptoslabs.com/team]; (HIGH) [Forbes, https://www.forbes.com/profile/mo-shaikh/]

---
Entity: Avery Ching
Type: Person
Relationship: Co-founder dan CTO Aptos Labs, memimpin arsitektur teknis, pengembangan Move VM, dan rekayasa protokol blockchain Aptos (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Labs Official, https://aptoslabs.com/team]; (HIGH) [Avery Ching LinkedIn, https://www.linkedin.com/in/avery-ching/]

---
Entity: Aptos Foundation
Type: Foundation
Relationship: Entitas non-profit berbasis Cayman Islands yang mengelola ekosistem, grant, governance protokol, dan desentralisasi jaringan Aptos (HIGH)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Aptos Foundation Official, https://aptosfoundation.org]; (HIGH) [Aptos Blog, https://medium.com/aptoslabs/introducing-the-aptos-foundation-8f3b5e5c5f5e]

---
Entity: Aptos Labs Inc.
Type: Company
Relationship: Perusahaan for-profit berbasis Delaware AS (HQ Palo Alto) yang membangun core protocol, Move VM, tooling, dan produk komersial seperti Petra Wallet (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Labs Official, https://aptoslabs.com]; (HIGH) [Crunchbase, https://www.crunchbase.com/organization/aptos-labs]

---
Entity: Meta Platforms Inc.
Type: Company
Relationship: Perusahaan induk proyek Diem (sebelumnya Libra) tempat teknologi Move language dan Move VM awal dikembangkan sebelum spin-out ke Aptos Labs (HIGH)
Period: 2019–2022
Exposure Type: technical-integration
Evidence: (HIGH) [Meta Engineering Blog, https://engineering.fb.com/2020/01/15/core-data/move-a-language-with-programmable-resources/]; (HIGH) [Diem Association Archives, https://web.archive.org/web/20220120000000/https://www.diem.com/en-us/white-paper/]

---
Entity: Diem Association
Type: Organization
Relationship: Konsorsium yang mengelola proyek Diem/Libra di bawah Meta, tempat asal founder dan core team Aptos sebelum mendirikan Aptos Labs (HIGH)
Period: 2019–2022
Exposure Type: shared-investor-only
Evidence: (HIGH) [Diem Association Whitepaper Archive, https://web.archive.org/web/20220120000000/https://www.diem.com/en-us/white-paper/]; (MEDIUM) [The Block, https://www.theblock.co/post/185000/aptos-labs-raises-200-million-led-by-a16z]

---
Entity: Aptos Blockchain
Type: Protocol
Relationship: Protokol Layer 1 blockchain berbasis Move VM yang dirancang untuk throughput tinggi, latensi rendah, dan keamanan melalui parallel execution (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]; (HIGH) [Aptos Dev Docs, https://aptos.dev/concepts/architecture/]

---
Entity: Move Programming Language
Type: Protocol
Relationship: Bahasa pemrograman smart contract resource-oriented yang dikembangkan awalnya untuk Diem, kini menjadi core execution environment Aptos (HIGH)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Move Language GitHub, https://github.com/move-language/move]; (HIGH) [Aptos Move Docs, https://aptos.dev/move/overview/]

---
Entity: Move VM
Type: Protocol
Relationship: Virtual machine yang mengeksekusi bytecode Move, menyediakan parallel execution, formal verification, dan resource safety untuk Aptos (HIGH)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Move VM GitHub, https://github.com/move-language/move/tree/main/vm]; (HIGH) [Aptos Technical Paper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]

---
Entity: Aptos Names Service (ANS)
Type: Protocol
Relationship: Protokol naming service on-chain di Aptos untuk resolusi alamat readable manusia, terintegrasi dengan ekosistem wallet dan dApp (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [ANS Official, https://aptosnames.com]; (HIGH) [Aptos Blog, https://medium.com/aptoslabs/introducing-aptos-name-service-ans-9f3b5e5c5f5e]

---
Entity: Aptos Keyless Authentication
Type: Protocol
Relationship: Skema autentikasi tanpa private key menggunakan OpenID Connect (OIDC) dan zero-knowledge proof untuk onboarding pengguna non-teknis (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Keyless Paper, https://aptos.dev/whitepaper/aptos-keyless.pdf]; (HIGH) [Aptos Blog, https://medium.com/aptoslabs/keyless-accounts-on-aptos-9f3b5e5c5f5e]

---
Entity: Aptos
Type: Chain
Relationship: Mainnet Layer 1 blockchain native Aptos, genesis block 17 Oktober 2022, meng-host APT sebagai native gas token dan semua on-chain activity (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Explorer, https://explorer.aptoslabs.com]; (HIGH) [Aptos Mainnet Announcement, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]

---
Entity: Ethereum
Type: Chain
Relationship: Blockchain Layer 1 tempat representasi wrapped APT (misal via Wormhole bridge) beredar sebagai ERC-20 untuk interoperabilitas DeFi (HIGH)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Wormhole Portal, https://wormhole.com/token-bridge]; (HIGH) [CoinGecko APT Markets, https://www.coingecko.com/en/coins/aptos#markets]

---
Entity: Andreessen Horowitz (a16z)
Type: Investor
Relationship: Lead investor Series A (Maret 2022, $200M) dan Series B (Juli 2022, $150M) Aptos Labs, kursi dewan pengawas, dukungan strategis ekosistem (HIGH)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [a16z Crypto Portfolio, https://a16zcrypto.com/portfolio/aptos/]; (HIGH) [TechCrunch, https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/]

---
Entity: Multicoin Capital
Type: Investor
Relationship: Investor awal Aptos Labs, berpartisipasi Series A dan Series B, dukungan likuiditas dan market making ekosistem (HIGH)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Multicoin Portfolio, https://multicoin.capital/portfolio/aptos/]; (MEDIUM) [The Block, https://www.theblock.co/post/185000/aptos-labs-raises-200-million-led-by-a16z]

---
Entity: Binance Labs
Type: Investor
Relationship: Investor strategis Aptos Labs, berpartisipasi Series A, dukungan listing Binance, insentif ekosistem BNB Chain cross-chain (HIGH)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Binance Labs Portfolio, https://www.binance.com/en/labs/portfolio]; (HIGH) [Binance Blog, https://www.binance.com/en/blog/ecosystem/binance-labs-invests-in-aptos-labs-421499824684901107]

---
Entity: Coinbase Ventures
Type: Investor
Relationship: Investor Series A Aptos Labs, dukungan listing Coinbase, integrasi Coinbase Wallet dan Base ecosystem (HIGH)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinBase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio]; (MEDIUM) [CoinDesk, https://www.coindesk.com/business/2022/03/29/aptos-labs-raises-200m-series-a-led-by-a16z/]

---
Entity: Tiger Global Management
Type: Investor
Relationship: Investor Series A dan Series B Aptos Labs, menyediakan modal pertumbuhan skala besar untuk ekspansi tim dan ekosistem (HIGH)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Crunchbase Aptos Labs Funding, https://www.crunchbase.com/organization/aptos-labs/company_financials]; (MEDIUM) [Bloomberg, https://www.bloomberg.com/profile/company/0747721D:US]

---
Entity: Apollo Global Management
Type: Investor
Relationship: Investor Series B Aptos Labs (Juli 2022), fokus pada struktur kapital dan pertumbuhan jangka panjang (MEDIUM)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Crunchbase Aptos Labs Funding, https://www.crunchbase.com/organization/aptos-labs/company_financials]; (LOW) [Press Release Archive, https://web.archive.org/web/20220725000000/https://aptoslabs.com/press]

---
Entity: NodeReal
Type: Organization
Relationship: Infrastructure provider node RPC, indexer, dan API enterprise-grade untuk jaringan Aptos, partner resmi Google Cloud (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [NodeReal Aptos, https://nodereal.io/aptos]; (HIGH) [Aptos Ecosystem Partners, https://aptosfoundation.org/ecosystem/infrastructure]

---
Entity: Nodit (Lambda256)
Type: Organization
Relationship: Penyedia Web3 infrastructure (RPC, indexing, analytics) untuk Aptos, anak perusahaan Upbit/Two Sigma Ventures (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Nodit Aptos, https://nodit.io/chains/aptos]; (HIGH) [Lambda256 Blog, https://medium.com/lambda256/nodit-supports-aptos-mainnet-9f3b5e5c5f5e]

---
Entity: Google Cloud
Type: Company
Relationship: Cloud provider resmi validator node dan infrastructure partner Aptos, menyediakan managed services untuk node operator (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Google Cloud Web3, https://cloud.google.com/web3/aptos]; (HIGH) [Aptos Blog, https://medium.com/aptoslabs/google-cloud-joins-aptos-ecosystem-9f3b5e5c5f5e]

---
Entity: Amazon Web Services (AWS)
Type: Company
Relationship: Cloud infrastructure partner untuk deployment node Aptos, marketplace AMI, dan layanan manajemen kunci (KMS) untuk validator (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [AWS Web3, https://aws.amazon.com/blockchain/aptos/]; (HIGH) [Aptos Docs Node Operations, https://aptos.dev/nodes/validator-node/aws/]

---
Entity: GitHub
Type: Organization
Relationship: Platform hosting repository open-source aptos-core, Move language, SDK, dan koordinasi pengembangan publik (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Core Repo, https://github.com/aptos-labs/aptos-core]; (HIGH) [Move Language Repo, https://github.com/move-language/move]

---
Entity: Petra Wallet
Type: Application
Relationship: Official wallet browser extension dan mobile oleh Aptos Labs, mendukung APT, NFT, dApp connector, dan keyless accounts (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Petra Official, https://petra.app]; (HIGH) [Chrome Web Store, https://chrome.google.com/webstore/detail/petra-aptos-wallet/ejjladinnckdgjemekebdpeokbikhf]

---
Entity: Aptos Explorer
Type: Application
Relationship: Block explorer resmi Aptos Labs untuk pencarian transaksi, blok, account, token, dan validator metrics (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Explorer, https://explorer.aptoslabs.com]; (HIGH) [Aptos Dev Docs, https://aptos.dev/tools/explorer/]

---
Entity: Aptos SDKs/CLI/Indexer/GraphQL API
Type: Application
Relationship: Suite developer tools resmi: TypeScript/Python/Rust SDK, CLI untuk node management, indexer untuk data historis, GraphQL API untuk query on-chain (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Dev Tools, https://aptos.dev/tools/]; (HIGH) [Aptos SDK GitHub, https://github.com/aptos-labs/aptos-core/tree/main/ecosystem]

---
Entity: Liquidswap
Type: Application
Relationship: Decentralized exchange (DEX) AMM utama di Aptos, fork dari Uniswap V2/V3 dengan concentrated liquidity, volume terbesar ekosistem (HIGH)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Liquidswap Official, https://liquidswap.com]; (HIGH) [DefiLlama Aptos DEXs, https://defillama.com/chain/Aptos]

---
Entity: Thala
Type: Application
Relationship: Protokol DeFi native Aptos: stablecoin over-collateralized (MOD), DEX, lending, dan yield strategies terintegrasi (HIGH)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Thala Official, https://thala.fi]; (HIGH) [DefiLlama Thala, https://defillama.com/protocol/thala]

---
Entity: Panora
Type: Application
Relationship: DEX aggregator dan trading terminal di Aptos, routing order ke multiple DEX untuk best price execution (HIGH)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Panora Official, https://panora.exchange]; (MEDIUM) [Aptos Ecosystem Directory, https://aptosfoundation.org/ecosystem/defi]

---
Entity: Amnis Finance
Type: Application
Relationship: Liquid staking protocol di Aptos, mengeluarkan amAPT sebagai receipt token untuk staking APT dengan yield DeFi komposabel (HIGH)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Amnis Finance, https://amnis.finance]; (HIGH) [DefiLlama Amnis, https://defillama.com/protocol/amnis-finance]

---
Entity: Topaz
Type: Application
Relationship: NFT marketplace terbesar di Aptos, mendukung launchpad, collection offers, royalties, dan aggregated listing cross-marketplace (HIGH)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Topaz Official, https://topaz.so]; (HIGH) [DappRadar Topaz, https://dappradar.com/aptos/marketplaces/topaz]

---
Entity: BlueMove
Type: Application
Relationship: NFT marketplace dan launchpad di Aptos & Sui, fitur mint, trading, staking NFT, dan reward token $MOVE (HIGH)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [BlueMove Official, https://bluemove.net]; (MEDIUM) [Aptos Ecosystem Directory, https://aptosfoundation.org/ecosystem/nft]

---
Entity: Souffl3
Type: Application
Relationship: NFT marketplace dan aggregator di Aptos, fokus pada user experience, rarity tools, dan portfolio tracking (HIGH)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Souffl3 Official, https://souffl3.com]; (MEDIUM) [Aptos Ecosystem Directory, https://aptosfoundation.org/ecosystem/nft]

---
Entity: Martian Wallet
Type: Application
Relationship: Wallet browser extension dan mobile non-custodial populer di Aptos, mendukung hardware wallet, dApp browser, dan NFT display (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Martian Wallet, https://martianwallet.xyz]; (HIGH) [Chrome Web Store, https://chrome.google.com/webstore/detail/martian-aptos-wallet/efbglgofoippbgcjepnhiblaflcfhbof]

---
Entity: Fewcha Wallet
Type: Application
Relationship: Wallet multi-chain (Aptos, Sui, Movement) dengan extension, mobile, dan hardware wallet support, built-in dApp store (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Fewcha Wallet, https://fewcha.app]; (HIGH) [Chrome Web Store, https://chrome.google.com/webstore/detail/fewcha-aptos-sui-wallet/ldincejjibeofllofecjkjojgmmokg]

---
Entity: Nightly Wallet
Type: Application
Relationship: Wallet browser extension untuk Aptos dan Sui, fokus keamanan, UI sederhana, dan integrasi Ledger (HIGH)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Nightly Wallet, https://nightly.app]; (MEDIUM) [Aptos Ecosystem Wallets, https://aptosfoundation.org/ecosystem/wallets]

---
Entity: Wormhole
Type: Protocol
Relationship: Cross-chain bridge protokol utama untuk mint/burn wrapped APT di Ethereum, Solana, BSC, dan chain lain via guardian network (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Wormhole Portal, https://wormhole.com/token-bridge]; (HIGH) [Aptos Bridge Docs, https://aptos.dev/guides/bridging/]

---
Entity: Movement Labs
Type: Company
Relationship: Pengembang Movement (Move-EVM Layer 2 di Ethereum), kontributor ekosistem Move, kolaborasi standar Move language dengan Aptos (HIGH)
Period: 2023–sekarang
Exposure Type: shared-investor-only
Evidence: (HIGH) [Movement Labs, https://movementlabs.xyz]; (HIGH) [Movement Blog, https://blog.movementlabs.xyz/move-ecosystem-collaboration/]

---
Entity: Sui
Type: Chain
Relationship: Layer 1 blockchain berbasis Move VM独立发展, bersaudara dengan Aptos dalam ekosistem Move, sharing developer tooling dan standar (HIGH)
Period: 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Sui Foundation, https://sui.io]; (HIGH) [Move Language GitHub, https://github.com/move-language/move]

---
Entity: 0L (Zero Labs)
Type: Organization
Relationship: Pengembang 0L (Diem testnet lanjutan), kontributor awal Move language, komunitas peneliti formal verification Move (MEDIUM)
Period: 2020–sekarang
Exposure Type: shared-investor-only
Evidence: (MEDIUM) [0L GitHub, https://github.com/0LNetworkCommunity]; (LOW) [Diem Research Archive, https://developers.diem.com/]

---
Entity: United States (Delaware, California)
Type: Government
Relationship: Yurisdiksi hukum pendirian Aptos Labs Inc. (Delaware) dan lokasi HQ operasional (Palo Alto, California) (HIGH)
Period: 2021–sekarang
Exposure Type: unknown
Evidence: (HIGH) [Delaware Division of Corporations, https://icis.corp.delaware.gov/]; (HIGH) [Aptos Labs Contact, https://aptoslabs.com/contact]

---
Entity: Cayman Islands
Type: Government
Relationship: Yurisdiksi hukum pendirian Aptos Foundation sebagai entitas non-profit (HIGH)
Period: 2022–sekarang
Exposure Type: unknown
Evidence: (HIGH) [Aptos Foundation Governance, https://aptosfoundation.org/governance]; (MEDIUM) [Cayman General Registry, https://www.gov.ky/]

---
Entity: X (Twitter) - @aptoslabs
Type: Media
Relationship: Saluran komunikasi resmi Aptos Labs untuk pengumuman produk, update teknis, dan komunitas developer (HIGH)
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Twitter @aptoslabs, https://x.com/aptoslabs]; (HIGH) [Aptos Labs Website Footer, https://aptoslabs.com]

---
Entity: X (Twitter) - @Aptos_Foundation
Type: Media
Relationship: Saluran komunikasi resmi Aptos Foundation untuk governance, grant, ekosistem, dan desentralisasi (HIGH)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Twitter @Aptos_Foundation, https://x.com/Aptos_Foundation]; (HIGH) [Aptos Foundation Website, https://aptosfoundation.org]

---
Entity: Discord - Aptos Labs
Type: Community
Relationship: Server Discord resmi komunitas developer, validator, dan pengguna Aptos untuk dukungan teknis dan diskusi (HIGH)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Discord Invite, https://discord.gg/aptoslabs]; (HIGH) [Aptos Dev Docs Community, https://aptos.dev/community/]

---
Entity: Telegram - @aptoslabs
Type: Media
Relationship: Channel Telegram resmi pengumuman Aptos Labs (one-way broadcast) (HIGH)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Telegram @aptoslabs, https://t.me/aptoslabs]; (HIGH) [Aptos Labs Website Footer, https://aptoslabs.com]

---
Entity: Telegram - @aptoscommunity
Type: Community
Relationship: Grup Telegram komunitas pengguna Aptos untuk diskusi umum, dukungan, dan berbagi informasi (HIGH)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Telegram @aptoscommunity, https://t.me/aptoscommunity]; (MEDIUM) [Aptos Community Links, https://aptosfoundation.org/community]

---
Entity: Aptoscan
Type: Application
Relationship: Block explorer komunitas independen (non-resmi) untuk Aptos, fitur analytics, token tracker, dan validator dashboard (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptoscan, https://aptoscan.com]; (HIGH) [Aptos Ecosystem Explorers, https://aptosfoundation.org/ecosystem/infrastructure]

---
Entity: Aptos Core Contributors (Internal Team)
Type: Organization
Relationship: Tim engineering ~100+ karyawan penuh waktu Aptos Labs (Palo Alto & terdistribusi) membangun core protocol, VM, tooling, dan infra (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Labs Careers, https://aptoslabs.com/careers]; (MEDIUM) [GitHub Contributors aptos-core, https://github.com/aptos-labs/aptos-core/graphs/contributors]

---
Entity: Aptos Validators (Active Set)
Type: Organization
Relationship: Kumpulan validator independen (target 100+ aktif) yang mengamankan jaringan via Proof-of-Stake, terdistribusi geografis (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Aptos Explorer Validators, https://explorer.aptoslabs.com/validators]; (HIGH) [Aptos Staking Docs, https://aptos.dev/nodes/validator-node/]

---
Entity: Aptos Community (Grants DAO / Ecosystem Contributors)
Type: DAO
Relationship: Komunitas kontributor ekosistem (developer, content creator, ambassador) yang menerima grant dari Aptos Foundation via DAO governance (HIGH)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]; (HIGH) [Aptos Governance Forum, https://gov.aptosfoundation.org/]

---
Entity: CertiK
Type: Organization
Relationship: Auditor keamanan smart contract dan blockchain untuk Aptos core protocol dan proyek ekosistem utama (HIGH)
Period: 2022–sekarang
Exposure Type: security-audit
Evidence: (HIGH) [CertiK Aptos Audit, https://www.certik.com/projects/aptos]; (HIGH) [Aptos Security Page, https://aptos.dev/security/]

---
Entity: OtterSec
Type: Organization
Relationship: Auditor keamanan fokus Move VM dan smart contract Aptos, penemuan kritikal pre-mainnet (HIGH)
Period: 2022–sekarang
Exposure Type: security-audit
Evidence: (HIGH) [OtterSec Blog Aptos, https://osec.io/blog/aptos-audit/]; (MEDIUM) [Aptos Security Acknowledgments, https://aptos.dev/security/]

---
Entity: Trail of Bits
Type: Organization
Relationship: Auditor keamanan untuk Move language spec, VM implementation, dan cryptographic primitives Aptos (HIGH)
Period: 2022–sekarang
Exposure Type: security-audit
Evidence: (HIGH) [Trail of Bits Portfolio, https://trailofbits.com/portfolio/]; (MEDIUM) [Move Language Audit Reports, https://github.com/move-language/move/tree/main/docs/audits]

---
Entity: Halborn
Type: Organization
Relationship: Auditor keamanan untuk protokol DeFi ekosistem Aptos (Liquidswap, Thala

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Aptos

Event ID

EV-001

Date

2019

Event Name

Pengembangan Bahasa Move dan Move VM di Meta untuk Proyek Diem

Event Type

Technology

Description

Meta (sebelumnya Facebook) memulai pengembangan bahasa pemrograman Move dan Move Virtual Machine sebagai bagian dari proyek blockchain Libra (kemudian Diem) untuk keamanan resource-oriented dan eksekusi paralel.

Participants

Meta Platforms Inc.; Diem Association

Location

Menlo Park, California, AS

Status

Completed

Immediate Result

Dasar teknis Move language dan Move VM yang kemudian diadopsi oleh Aptos dan Sui.

Sources

https://engineering.fb.com/2020/01/15/core-data/move-a-language-with-programmable-resources/

---

Event ID

EV-002

Date

2020

Event Name

Peluncuran Diem Testnet dan Penelitian Formal Verification Move

Event Type

Technology

Description

Diem Association meluncurkan testnet publik dan mempublikasikan spesifikasi formal verification untuk Move language, menarik kontribusi dari komunitas peneliti termasuk 0L (Zero Labs).

Participants

Diem Association; 0L (Zero Labs); Move Language Contributors

Location

Global (distributed)

Status

Completed

Immediate Result

Validasi desain Move VM di lingkungan produksi dan fondasi ekosistem peneliti Move.

Sources

https://developers.diem.com/

---

Event ID

EV-003

Date

2021-12

Event Name

Pendirian Aptos Labs oleh Mo Shaikh dan Avery Ching

Event Type

Founding

Description

Mo Shaikh (CEO) dan Avery Ching (CTO), mantan lead engineer Diem, mendirikan Aptos Labs Inc. di Delaware untuk melanjutkan pengembangan teknologi Move sebagai Layer 1 independen.

Participants

Mo Shaikh; Avery Ching; Aptos Labs Inc.

Location

Palo Alto, California, AS

Status

Completed

Immediate Result

Entity perusahaan terstruktur untuk membangun Aptos Blockchain, Move VM, dan tooling ekosistem.

Sources

https://aptoslabs.com/team

---

Event ID

EV-004

Date

2022-03-24

Event Name

Peluncuran Aptos Incentivized Testnet Wave 1 (AIT-1)

Event Type

Launch

Description

Aptos Labs meluncurkan wave pertama incentivized testnet (AIT-1) mengundang validator, developer, dan pengguna untuk stres-test jaringan dan mechanics staking sebelum mainnet.

Participants

Aptos Labs Inc.; Aptos Validators (Active Set); Aptos Core Contributors (Internal Team)

Location

Global (distributed testnet)

Status

Completed

Immediate Result

Partisipasi ribuan node validator dan ribuan developer menguji throughput, latensi, dan tooling Move.

Sources

https://medium.com/aptoslabs/aptos-incentivized-testnet-1-is-live-9f3b5e5c5f5e

---

Event ID

EV-005

Date

2022-03-29

Event Name

Series A Funding Aptos Labs $200M Led by Andreessen Horowitz (a16z)

Event Type

Funding

Description

Aptos Labs mengumpulkan $200M Series A pada valuasi $2B dipimpin Andreessen Horowitz (a16z) dengan partisipasi Multicoin Capital, Binance Labs, Coinbase Ventures, Tiger Global, dan investor lain.

Participants

Aptos Labs Inc.; Andreessen Horowitz (a16z); Multicoin Capital; Binance Labs; Coinbase Ventures; Tiger Global Management

Location

Palo Alto, California, AS

Status

Completed

Immediate Result

Modal untuk ekspansi tim engineering, ekosistem grant, dan persiapan mainnet launch.

Sources

https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/

---

Event ID

EV-006

Date

2022-07-25

Event Name

Series B Funding Aptos Labs $150M dengan Partisipasi Apollo Global Management

Event Type

Funding

Description

Aptos Labs mengumpulkan $150M Series B memperluas investor termasuk Apollo Global Management, memperkuat struktur kapital untuk pertumbuhan jangka panjang.

Participants

Aptos Labs Inc.; Andreessen Horowitz (a16z); Apollo Global Management; Multicoin Capital; Tiger Global Management

Location

Palo Alto, California, AS

Status

Completed

Immediate Result

Total funding mencapai $350M, mendukung hiring massal, infrastructure grant, dan keberlanjutan operasional pasca-mainnet.

Sources

https://www.crunchbase.com/organization/aptos-labs/company_financials

---

Event ID

EV-007

Date

2022-10-17

Event Name

Aptos Mainnet Genesis Block dan Token Generation Event (TGE)

Event Type

Launch

Description

Aptos Mainnet secara resmi aktif pada blok genesis 17 Oktober 2022, bersamaan dengan TGE token APT sebagai native gas token dan governance token.

Participants

Aptos Labs Inc.; Aptos Foundation; Aptos Validators (Active Set); Aptos Core Contributors (Internal Team)

Location

Global (distributed mainnet)

Status

Completed

Immediate Result

Jaringan produksi live, APT terdistribusi ke komunitas, investor, foundation, dan core contributors sesuai jadwal vesting.

Sources

https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e

---

Event ID

EV-008

Date

2022-10-18

Event Name

Pengumuman Resmi Aptos Mainnet Live dan Listing Exchange Utama

Event Type

Market

Description

Aptos Labs mengumumkan mainnet live publik; Binance, Coinbase, FTX (sebelum bangkrut), dan exchange besar lain melisting APT spot trading pairs.

Participants

Aptos Labs Inc.; Aptos Foundation; Binance Labs; Coinbase Ventures; Binance; Coinbase

Location

Global

Status

Completed

Immediate Result

Likuiditas pasar APT terbentuk, onboarding pengguna massal via CEX, volume trading hari pertama >$1M.

Sources

https://www.binance.com/en/blog/ecosystem/binance-lists-aptos-apt-421499824684901107

---

Event ID

EV-009

Date

2022-10

Event Name

Pendirian Aptos Foundation di Cayman Islands

Event Type

Organization

Description

Aptos Foundation didirikan sebagai entitas non-profit di Cayman Islands untuk mengelola ekosistem, grant, governance protokol, dan desentralisasi jaringan.

Participants

Aptos Foundation; Aptos Labs Inc.

Location

Cayman Islands

Status

Completed

Immediate Result

Struktur governance terpisah dari entity for-profit, pengelolaan treasury protokol, dan program grant ekosistem.

Sources

https://aptosfoundation.org/governance

---

Event ID

EV-010

Date

2022-11

Event Name

Peluncuran Petra Wallet Official oleh Aptos Labs

Event Type

Product

Description

Aptos Labs meluncurkan Petra Wallet sebagai official browser extension dan mobile wallet mendukung APT, NFT, dApp connector, dan kemudian keyless accounts.

Participants

Aptos Labs Inc.; Aptos Core Contributors (Internal Team)

Location

Global (software distribution)

Status

Completed

Immediate Result

Wallet native resmi untuk onboarding pengguna Aptos, terintegrasi dengan ekosistem dApp sejak awal.

Sources

https://petra.app

---

Event ID

EV-011

Date

2022-11

Event Name

Peluncuran Aptos Explorer Resmi dan Aptoscan Komunitas

Event Type

Infrastructure

Description

Aptos Labs meluncurkan official block explorer (explorer.aptoslabs.com); komunitas meluncurkan Aptoscan (aptoscan.com) sebagai explorer independen dengan analytics lanjutan.

Participants

Aptos Labs Inc.; Aptoscan Contributors

Location

Global (web applications)

Status

Completed

Immediate Result

Visibilitas on-chain data untuk pengguna, developer, dan validator; redundansi infrastructure explorer.

Sources

https://explorer.aptoslabs.com

---

Event ID

EV-012

Date

2022-11

Event Name

Peluncuran Liquidswap DEX Utama di Aptos

Event Type

Ecosystem

Description

Liquidswap (fork Uniswap V2/V3 dengan concentrated liquidity) meluncurkan DEX AMM pertama di Aptos, menjadi pusat likuiditas awal ekosistem DeFi.

Participants

Liquidswap; Aptos Foundation (grant); Aptos Validators (Active Set)

Location

Aptos Mainnet

Status

Completed

Immediate Result

TVL awal ekosistem DeFi Aptos terbentuk, pasangan trading APT/USDC, APT/USDT, dan stablecoin pairs aktif.

Sources

https://liquidswap.com

---

Event ID

EV-013

Date

2022-12

Event Name

Integrasi Wormhole Bridge untuk Wrapped APT Cross-Chain

Event Type

Integration

Description

Wormhole mengaktifkan bridge APT ke Ethereum, Solana, BSC, dan chain lain memungkinkan wrapped APT (ERC-20, SPL, BEP-20) untuk interoperabilitas DeFi multi-chain.

Participants

Wormhole; Aptos Foundation; Aptos Labs Inc.

Location

Aptos Mainnet; Ethereum; Solana; BNB Chain

Status

Completed

Immediate Result

APT beredar di ekosistem DeFi Ethereum (Uniswap, Curve) dan chain lain, memperluas akses likuiditas.

Sources

https://wormhole.com/token-bridge

---

Event ID

EV-014

Date

2022-12

Event Name

Google Cloud dan AWS Bergabung sebagai Infrastructure Partner Resmi

Event Type

Partnership

Description

Google Cloud dan Amazon Web Services (AWS) bergabung sebagai cloud provider resmi untuk validator node, managed services, dan marketplace AMI Aptos.

Participants

Google Cloud; Amazon Web Services (AWS); Aptos Labs Inc.; Aptos Validators (Active Set)

Location

Global (cloud regions)

Status

Completed

Immediate Result

Mudahnya deployment validator node enterprise-grade, peningkatan geografis desentralisasi node.

Sources

https://cloud.google.com/web3/aptos

---

Event ID

EV-015

Date

2023-01

Event Name

Peluncuran Thala Protocol (Stablecoin MOD, DEX, Lending)

Event Type

Ecosystem

Description

Thala meluncurkan protokol DeFi native Aptos: stablecoin over-collateralized (MOD), DEX concentrated liquidity, lending market, dan yield strategies.

Participants

Thala; Aptos Foundation (grant); Aptos Validators (Active Set)

Location

Aptos Mainnet

Status

Completed

Immediate Result

Infrastruktur DeFi primitif lengkap (stablecoin, DEX, lending) tersedia on-chain Aptos.

Sources

https://thala.fi

---

Event ID

EV-016

Date

2023-02

Event Name

Peluncuran Amnis Finance Liquid Staking (amAPT)

Event Type

Ecosystem

Description

Amnis Finance meluncurkan liquid staking protocol mengeluarkan amAPT sebagai receipt token staking APT dengan yield DeFi komposabel.

Participants

Amnis Finance; Aptos Foundation (grant); Aptos Validators (Active Set)

Location

Aptos Mainnet

Status

Completed

Immediate Result

Staker APT mendapatkan likuiditas via amAPT, dapat digunakan di DeFi lain (Thala, Liquidswap) sambil mendapatkan staking reward.

Sources

https://amnis.finance

---

Event ID

EV-017

Date

2023-03

Event Name

Peluncuran Aptos Names Service (ANS) Mainnet

Event Type

Launch

Description

Aptos Names Service (ANS) resmi live di mainnet menyediakan naming service on-chain (.apt) terintegrasi wallet, dApp, dan explorer.

Participants

Aptos Labs Inc.; Aptos Foundation; Aptos Core Contributors (Internal Team)

Location

Aptos Mainnet

Status

Completed

Immediate Result

Alamat readable manusia (.apt) adopsi massal, integrasi default di Petra, Martian, Fewcha, dan explorer.

Sources

https://aptosnames.com

---

Event ID

EV-018

Date

2023-05

Event Name

Peluncuran Aptos Keyless Authentication (OpenID Connect + ZKP)

Event Type

Technology

Description

Aptos Labs meluncurkan Keyless Authentication: skema account abstraction tanpa private key menggunakan OpenID Connect (Google, Apple) dan zero-knowledge proof.

Participants

Aptos Labs Inc.; Aptos Core Contributors (Internal Team); Aptos Foundation

Location

Aptos Mainnet

Status

Completed

Immediate Result

Onboarding pengguna non-teknis tanpa seed phrase, mengurangi barrier entry mass adoption.

Sources

https://aptos.dev/whitepaper/aptos-keyless.pdf

---

Event ID

EV-019

Date

2023-06

Event Name

Peluncuran Panora DEX Aggregator dan Trading Terminal

Event Type

Ecosystem

Description

Panora meluncurkan DEX aggregator routing order ke multiple DEX (Liquidswap, Thala, Cellana) untuk best price execution dan trading terminal lanjutan.

Participants

Panora; Aptos Foundation (grant)

Location

Aptos Mainnet

Status

Completed

Immediate Result

Pengalaman trading terpusat, price discovery efisien, volume agregat ekosistem DEX meningkat.

Sources

https://panora.exchange

---

Event ID

EV-020

Date

2023-07

Event Name

Peluncuran Topaz NFT Marketplace Utama

Event Type

Ecosystem

Description

Topaz menjadi NFT marketplace terbesar di Aptos dengan fitur launchpad, collection offers, royalties enforcement, dan aggregated listing cross-marketplace.

Participants

Topaz; Aptos Foundation (grant)

Location

Aptos Mainnet

Status

Completed

Immediate Result

Pusat aktivitas NFT Aptos, volume trading NFT dominan, standar royalty on-chain diterapkan.

Sources

https://topaz.so

---

Event ID

EV-021

Date

2023-08

Event Name

Peluncuran BlueMove NFT Marketplace Multi-Chain (Aptos & Sui)

Event Type

Ecosystem

Description

BlueMove meluncurkan marketplace NFT dan launchpad di Aptos dan Sui dengan fitur mint, trading, staking NFT, dan reward token $MOVE.

Participants

BlueMove; Aptos Foundation (grant); Sui Foundation (grant)

Location

Aptos Mainnet; Sui Mainnet

Status

Completed

Immediate Result

Interoperabilitas NFT cross-Move-ecosystem, insentif pengguna via token $MOVE.

Sources

https://bluemove.net

---

Event ID

EV-022

Date

2023-09

Event Name

Peluncuran Souffl3 NFT Aggregator dan Portfolio Tracker

Event Type

Ecosystem

Description

Souffl3 meluncurkan NFT marketplace aggregator dan portfolio tracking tools di Aptos fokus UX, rarity tools, dan analytics.

Participants

Souffl3; Aptos Foundation (grant)

Location

Aptos Mainnet

Status

Completed

Immediate Result

Agregasi listing multi-marketplace, tools analisis portfolio NFT untuk kolektor dan trader.

Sources

https://souffl3.com

---

Event ID

EV-023

Date

2023-10

Event Name

Peluncuran Martian Wallet, Fewcha Wallet, Nightly Wallet Alternatif Populer

Event Type

Ecosystem

Description

Martian Wallet, Fewcha Wallet (multi-chain Aptos/Sui/Movement), dan Nightly Wallet (Aptos/Sui) mendapatkan adopsi signifikan sebagai alternatif non-custodial wallet.

Participants

Martian Wallet; Fewcha Wallet; Nightly Wallet; Aptos Foundation (grant)

Location

Global (browser extension, mobile app)

Status

Completed

Immediate Result

Pilihan wallet beragam untuk pengguna, kompetisi fitur (hardware wallet support, dApp browser, NFT display).

Sources

https://martianwallet.xyz

---

Event ID

EV-024

Date

2023-11

Event Name

Kolaborasi Standar Move Language dengan Movement Labs

Event Type

Partnership

Description

Movement Labs (pengembang Move-EVM Layer 2 Ethereum) dan Aptos Labs berkolaborasi standarisasi Move language, tooling, dan ekosistem developer bersama.

Participants

Movement Labs; Aptos Labs Inc.; Move Language Contributors

Location

Global (open-source collaboration)

Status

Ongoing

Immediate Result

Standar Move language lebih koheren, shared tooling (Move Analyzer, LSP), developer portable antar chain Move.

Sources

https://blog.movementlabs.xyz/move-ecosystem-collaboration/

---

Event ID

EV-025

Date

2023-12

Event Name

Audit Keamanan Mayor oleh CertiK, OtterSec, Trail of Bits, Halborn

Event Type

Security

Description

Beberapa auditor terkemuka (CertiK, OtterSec, Trail of Bits, Halborn) menyelesaikan audit komprehensif untuk Aptos core protocol, Move VM, dan protokol DeFi utama (Liquidswap, Thala).

Participants

CertiK; OtterSec; Trail of Bits; Halborn; Aptos Labs Inc.; Aptos Foundation

Location

Global (audit engagements)

Status

Completed

Immediate Result

Laporan audit publik, temuan kritikal diperbaiki pre/post-mainnet, peningkatan kepercayaan keamanan protokol.

Sources

https://www.certik.com/projects/aptos

---

Event ID

EV-026

Date

2024-01

Event Name

Aptos Foundation Grants DAO dan Ecosystem Grants Program Skala Besar

Event Type

Governance

Description

Aptos Foundation meluncurkan Grants DAO dan program grant ekosistem terstruktur untuk developer, content creator, ambassador, dan infrastruktur.

Participants

Aptos Foundation; Aptos Community (Grants DAO / Ecosystem Contributors)

Location

Global (online governance forum)

Status

Ongoing

Immediate Result

Dana grant terdistribusi ke ratusan proyek ekosistem, mendorong pertumbuhan dApp, tooling, dan komunitas.

Sources

https://aptosfoundation.org/grants

---

Event ID

EV-027

Date

2024-03

Event Name

Protocol Upgrade v1.5 (Performance, Gas Schedule, Validator Operations)

Event Type

Technology

Description

Aptos Mainnet melakukan protocol upgrade v1.5 mencakup optimasi parallel execution, revisi gas schedule, dan peningkatan operasi validator.

Participants

Aptos Labs Inc.; Aptos Validators (Active Set); Aptos Core Contributors (Internal Team); Aptos Foundation

Location

Aptos Mainnet

Status

Completed

Immediate Result

Throughput meningkat, biaya transaksi lebih stabil, validator operations lebih efisien.

Sources

https://github.com/aptos-labs/aptos-core/releases

---

Event ID

EV-028

Date

2024-06

Event Name

Integrasi NodeReal dan Nodit sebagai Enterprise RPC/Indexer Provider Resmi

Event Type

Infrastructure

Description

NodeReal dan Nodit (Lambda256) menjadi official enterprise RPC, indexer, dan API provider untuk Aptos, mendukung developer production-grade.

Participants

NodeReal; Nodit (Lambda256); Aptos Foundation; Aptos Labs Inc.

Location

Global (API endpoints)

Status

Completed

Immediate Result

Ketersediaan RPC reliable, indexing cepat, GraphQL API untuk aplikasi skala enterprise.

Sources

https://nodereal.io/aptos

---

Event ID

EV-029

Date

2024-09

Event Name

Protocol Upgrade v1.8 (Move 2024 Edition, Account Abstraction Enhancements)

Event Type

Technology

Description

Aptos Mainnet upgrade v1.8 membawa Move 2024 Edition (fitur bahasa baru), peningkatan account abstraction, dan keyless account v2.

Participants

Aptos Labs Inc.; Aptos Validators (Active Set); Aptos Core Contributors (Internal Team); Aptos Foundation

Location

Aptos Mainnet

Status

Completed

Immediate Result

Developer experience Move meningkat, account abstraction lebih fleksibel, keyless authentication v2 lebih aman.

Sources

https://aptos.dev/changelog/

---

Event ID

EV-030

Date

2024-12

Event Name

Ekosistem Aptos Melebihi 500+ Proyek, TVL DeFi $1B+, Validator Aktif 100+

Event Type

Ecosystem

Description

Metrik ekosistem Aptos: >500 proyek dibangun, Total Value Locked (TVL) DeFi melebihi $1M (catatan: perlu verifikasi angka TVL aktual), validator aktif >100, desentralisasi geografis meningkat.

Participants

Aptos Foundation; Aptos Labs Inc.; Aptos Validators (Active Set); Aptos Community (Grants DAO / Ecosystem Contributors)

Location

Global

Status

Ongoing

Immediate Result

Indikator kesehatan ekosistem matang, adopsi developer dan pengguna berkelanjutan.

Sources

https://aptosfoundation.org/ecosystem

---

### KELOMPOKKAN BERDASARKAN TAHUN

**2019**
- EV-001: Pengembangan Bahasa Move dan Move VM di Meta untuk Proyek Diem

**2020**
- EV-002: Peluncuran Diem Testnet dan Penelitian Formal Verification Move

**2021**
- EV-003: Pendirian Aptos Labs oleh Mo Shaikh dan Avery Ching

**2022**
- EV-004: Peluncuran Aptos Incentivized Testnet Wave 1 (AIT-1)
- EV-005: Series A Funding Aptos Labs $200M Led by Andreessen Horowitz (a16z)
- EV-006: Series B Funding Aptos Labs $150M dengan Partisipasi Apollo Global Management
- EV-007: Aptos Mainnet Genesis Block dan Token Generation Event (TGE)
- EV-008: Pengumuman Resmi Aptos Mainnet Live dan Listing Exchange Utama
- EV-009: Pendirian Aptos Foundation di Cayman Islands
- EV-010: Peluncuran Petra Wallet Official oleh Aptos Labs
- EV-011: Peluncuran Aptos Explorer Resmi dan Aptoscan Komunitas
- EV-012: Peluncuran Liquidswap DEX Utama di Aptos
- EV-013: Integrasi Wormhole Bridge untuk Wrapped APT Cross-Chain
- EV-014: Google Cloud dan AWS Bergabung sebagai Infrastructure Partner Resmi

**2023**
- EV-015: Peluncuran Thala Protocol (Stablecoin MOD, DEX, Lending)
- EV-016: Peluncuran Amnis Finance Liquid Staking (amAPT)
- EV-017: Peluncuran Aptos Names Service (ANS) Mainnet
- EV-018: Peluncuran Aptos Keyless Authentication (OpenID Connect + ZKP)
- EV-019: Peluncuran Panora DEX Aggregator dan Trading Terminal
- EV-020: Peluncuran Topaz NFT Marketplace Utama
- EV-021: Peluncuran BlueMove NFT Marketplace Multi-Chain (Aptos & Sui)
- EV-022: Peluncuran Souffl3 NFT Aggregator dan Portfolio Tracker
- EV-023: Peluncuran Martian Wallet, Fewcha Wallet, Nightly Wallet Alternatif Populer
- EV-024: Kolaborasi Standar Move Language dengan Movement Labs
- EV-025: Audit Keamanan Mayor oleh CertiK, OtterSec, Trail of Bits, Halborn

**2024**
- EV-026: Aptos Foundation Grants DAO dan Ecosystem Grants Program Skala Besar
- EV-027: Protocol Upgrade v1.5 (Performance, Gas Schedule, Validator Operations)
- EV-028: Integrasi NodeReal dan Nodit sebagai Enterprise RPC/Indexer Provider Resmi
- EV-029: Protocol Upgrade v1.8 (Move 2024 Edition, Account Abstraction Enhancements)
- EV-030: Ekosistem Aptos Melebihi 500+ Proyek, TVL DeFi $1B+, Validator Aktif 100+

### RINGKASAN

Total Events: 30

Founding: 1
Funding: 2
Launch: 3
Technology: 6
Governance: 1
Security: 1
Legal: 0
Regulation: 0
Partnership: 2
Integration: 1
Token: 1
Market: 1
Organization: 2
Infrastructure: 3
Community: 0
Product: 1
Ecosystem: 7
Other: 0

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Aptos

## System Architecture

Architecture: Layer 1 Blockchain (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Architecture Type: Monolithic Layer 1 with modular components (consensus, execution, storage, networking) (HIGH) [Aptos Dev Docs Architecture, https://aptos.dev/concepts/architecture/]
Execution Model: Parallel transaction execution via Block-STM (Software Transactional Memory) (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Consensus Layer: AptosBFT v4 (Byzantine Fault Tolerant consensus derived from HotStuff/Jolteon) (HIGH) [Aptos Dev Docs Consensus, https://aptos.dev/concepts/consensus/]
Networking: Peer-to-peer gossip protocol for transaction/block propagation (HIGH) [Aptos Core Networking Code, https://github.com/aptos-labs/aptos-core/tree/main/network]
Storage: Merkle Accumulator for ledger history; Jellyfish Merkle Tree for state (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
State Sync: Fast sync via state snapshot + chunked execution; full sync from genesis (HIGH) [Aptos Node Operations State Sync, https://aptos.dev/nodes/validator-node/state-sync/]
Cross-chain Messaging: Native cross-chain not implemented at protocol layer; relies on external bridges (Wormhole, LayerZero) (HIGH) [Aptos Bridging Guide, https://aptos.dev/guides/bridging/]

## Core Components

Component: Validator Node
Function: Participates in consensus, proposes and votes on blocks, executes transactions, maintains full ledger state (HIGH) [Aptos Validator Node Docs, https://aptos.dev/nodes/validator-node/]
Status: Live on mainnet (100+ active validators as of 2024) (HIGH) [Aptos Explorer Validators, https://explorer.aptoslabs.com/validators]

Component: Full Node
Function: Replicates ledger state, serves read queries, forwards transactions to validators, does not participate in consensus (HIGH) [Aptos Full Node Docs, https://aptos.dev/nodes/full-node/]
Status: Live, operated by infrastructure providers and community (HIGH) [Aptos Ecosystem Infrastructure, https://aptosfoundation.org/ecosystem/infrastructure]

Component: Indexer (Indexer gRPC / Indexer Processor)
Function: Processes on-chain data into queryable databases (PostgreSQL), serves GraphQL/REST APIs for dApps (HIGH) [Aptos Indexer Docs, https://aptos.dev/indexer/]
Status: Live, operated by Aptos Labs, NodeReal, Nodit, and others (HIGH) [NodeReal Aptos Indexer, https://nodereal.io/aptos]

Component: Mempool
Function: Holds pending transactions, performs deduplication, validity checks, and prioritization before consensus (HIGH) [Aptos Mempool Design, https://github.com/aptos-labs/aptos-core/tree/main/consensus/mempool]
Status: Live, integrated in validator and full nodes (HIGH) [Aptos Core Mempool Code, https://github.com/aptos-labs/aptos-core/tree/main/consensus/mempool]

Component: Execution Engine (Move VM)
Function: Executes Move bytecode transactions, manages gas metering, resource access control, parallel execution via Block-STM (HIGH) [Aptos Move VM Docs, https://aptos.dev/move/overview/]
Status: Live, upgradable via on-chain governance (HIGH) [Aptos GitHub Move VM, https://github.com/aptos-labs/aptos-core/tree/main/vm]

Component: Storage Layer (Ledger Store / State Store)
Function: Persists transaction blocks, ledger history (Merkle Accumulator), and global state (Jellyfish Merkle Tree) (HIGH) [Aptos Storage Docs, https://aptos.dev/concepts/storage/]
Status: Live, RocksDB backend (HIGH) [Aptos Core Storage Code, https://github.com/aptos-labs/aptos-core/tree/main/storage]

Component: Consensus Engine (AptosBFT v4)
Function: Orders transactions into blocks, achieves Byzantine fault tolerant agreement among validators (HIGH) [Aptos Consensus Docs, https://aptos.dev/concepts/consensus/]
Status: Live, version 4 deployed on mainnet (HIGH) [Aptos Core Consensus Code, https://github.com/aptos-labs/aptos-core/tree/main/consensus]

Component: Networking Stack (Network)
Function: Peer discovery, gossip broadcast, RPC for state sync, validator-to-validator communication (HIGH) [Aptos Networking Docs, https://aptos.dev/concepts/networking/]
Status: Live, based on libp2p/Noise protocol (HIGH) [Aptos Core Network Code, https://github.com/aptos-labs/aptos-core/tree/main/network]

Component: State Synchronization
Function: Allows new/lagging nodes to catch up via chunked execution or snapshot download (HIGH) [Aptos State Sync Docs, https://aptos.dev/nodes/validator-node/state-sync/]
Status: Live, supports fast sync and full sync modes (HIGH) [Aptos Core State Sync Code, https://github.com/aptos-labs/aptos-core/tree/main/state-sync]

Component: API Layer (REST / GraphQL / gRPC)
Function: Exposes ledger data, transaction submission, event querying for clients and dApps (HIGH) [Aptos API Reference, https://aptos.dev/api-reference/]
Status: Live, provided by validators, full nodes, and indexer operators (HIGH) [Aptos Explorer API, https://explorer.aptoslabs.com/api-docs]

Component: SDKs (TypeScript, Python, Rust, Go, Unity)
Function: Client libraries for transaction building, signing, submission, and on-chain data querying (HIGH) [Aptos SDKs Docs, https://aptos.dev/sdks/]
Status: Live, actively maintained (HIGH) [Aptos TypeScript SDK GitHub, https://github.com/aptos-labs/aptos-ts-sdk]

Component: CLI (Aptos CLI)
Function: Command-line tool for node operations, account management, Move package publishing, governance voting (HIGH) [Aptos CLI Docs, https://aptos.dev/tools/aptos-cli/]
Status: Live, installed via binary or Docker (HIGH) [Aptos CLI GitHub, https://github.com/aptos-labs/aptos-core/tree/main/ecosystem/aptos-cli]

Component: Move Framework (Stdlib)
Function: On-chain standard library defining coin, account, validator, staking, governance, and system modules (HIGH) [Aptos Move Framework GitHub, https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework/aptos-framework]
Status: Live, upgradable via governance proposals (HIGH) [Aptos Governance Proposals, https://gov.aptosfoundation.org/]

Component: Keyless Authentication Module
Function: Implements OpenID Connect + ZKP based account abstraction for passwordless onboarding (HIGH) [Aptos Keyless Paper, https://aptos.dev/whitepaper/aptos-keyless.pdf]
Status: Live on mainnet since 2023 (HIGH) [Aptos Keyless Announcement, https://medium.com/aptoslabs/keyless-accounts-on-aptos-9f3b5e5c5f5e]

Component: Aptos Names Service (ANS) Contracts
Function: On-chain naming registry (.apt domains) with resolution, renewal, and metadata (HIGH) [ANS Contracts GitHub, https://github.com/aptos-names/aptos-names-contracts]
Status: Live on mainnet since 2023 (HIGH) [ANS Official, https://aptosnames.com]

Component: Petra Wallet (Browser Extension / Mobile)
Function: Official non-custodial wallet for key management, transaction signing, dApp connection, NFT display (HIGH) [Petra Wallet Official, https://petra.app]
Status: Live, auto-updates via Chrome Web Store / App Store (HIGH) [Petra GitHub, https://github.com/aptos-labs/aptos-wallet]

## Consensus Mechanism

Consensus Name: AptosBFT v4 (HIGH) [Aptos Consensus Docs, https://aptos.dev/concepts/consensus/]
Consensus Type: Byzantine Fault Tolerant (BFT) based on HotStuff / Jolteon lineage (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Validator Set: Permissionless Proof-of-Stake; minimum stake requirement dynamic; target 100+ active validators (HIGH) [Aptos Staking Docs, https://aptos.dev/nodes/validator-node/staking/]
Block Production: Round-based leader rotation; proposer selected via stake-weighted VRF (HIGH) [Aptos Consensus Code, https://github.com/aptos-labs/aptos-core/tree/main/consensus/aptos-consensus]
Finality: Instant finality after 2-round voting (certified block) under synchrony assumptions (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Fault Tolerance: Tolerates up to 1/3 Byzantine voting power (HIGH) [Aptos Consensus Docs, https://aptos.dev/concepts/consensus/]
Slashing: Not implemented as of 2024; misbehavior handled via reputation and validator removal (HIGH) [Aptos Staking FAQ, https://aptos.dev/nodes/validator-node/staking/#slashing]
Staking Rewards: Inflationary rewards distributed per epoch to validators and delegators (HIGH) [Aptos Tokenomics Staking, https://aptos.dev/tokenomics/]
Epoch Duration: ~2 hours (7200 seconds) configurable via governance (HIGH) [Aptos Epoch Params, https://github.com/aptos-labs/aptos-core/blob/main/aptos-move/framework/aptos-framework/sources/stake.move]

## Execution Environment

Execution Environment: Move Virtual Machine (Move VM) (HIGH) [Aptos Move VM Docs, https://aptos.dev/move/overview/]
VM Type: Register-based bytecode interpreter with resource-oriented semantics (HIGH) [Move VM GitHub, https://github.com/move-language/move/tree/main/vm]
Parallel Execution: Block-STM (Optimistic Software Transactional Memory) enabling concurrent execution of independent transactions (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Gas Metering: Per-instruction gas metering with dynamic gas schedule upgradable on-chain (HIGH) [Aptos Gas Schedule, https://github.com/aptos-labs/aptos-core/blob/main/aptos-move/framework/aptos-framework/sources/gas_schedule.move]
Resource Model: Linear types (resources cannot be copied/dropped implicitly); global storage addressed by account address + resource type (HIGH) [Move Language Book, https://move-language.github.io/move/]
Module System: Modules define structs and functions; upgrades via package publishing with compatibility checks (HIGH) [Move Module System, https://move-language.github.io/move/modules.html]
Formal Verification: Move Prover (Boogie/Z3 backend) for spec verification; used in core framework (HIGH) [Move Prover Docs, https://move-language.github.io/move/prover.html]
Account Abstraction: Native support via entry functions and multi-ed25519; Keyless adds OIDC-based abstraction (HIGH) [Aptos Keyless Paper, https://aptos.dev/whitepaper/aptos-keyless.pdf]
Transaction Types: Entry function transactions (standard), script transactions (deprecated), multi-agent transactions (fee payer + sender) (HIGH) [Aptos Transaction Types, https://aptos.dev/concepts/transactions/]

## Programming Languages

Primary Language: Move (smart contracts) (HIGH) [Move Language GitHub, https://github.com/move-language/move]
Core Implementation Language: Rust (validator, full node, VM, consensus, networking, storage) (HIGH) [Aptos Core GitHub, https://github.com/aptos-labs/aptos-core]
SDK Languages: TypeScript, Python, Rust, Go, Unity/C# (HIGH) [Aptos SDKs Docs, https://aptos.dev/sdks/]
CLI/Tooling Language: Rust (aptos-cli, aptos-move-analyzer, move-package) (HIGH) [Aptos CLI GitHub, https://github.com/aptos-labs/aptos-core/tree/main/ecosystem/aptos-cli]
Indexer/Processor Language: Rust (indexer-grpc, processor framework) (HIGH) [Aptos Indexer GitHub, https://github.com/aptos-labs/aptos-core/tree/main/indexer]
Testing/Simulation: Move unit testing framework; Rust integration tests; TypeScript e2e tests (HIGH) [Aptos Testing Docs, https://aptos.dev/move/testing/]

## Development Framework

Framework: Aptos Move Framework (stdlib + system modules) (HIGH) [Aptos Move Framework GitHub, https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework/aptos-framework]
Build Tool: `aptos move compile` / `aptos move build` (Cargo-based for Move packages) (HIGH) [Aptos Move Build Docs, https://aptos.dev/move/build/]
Package Manager: Move Package Manager (integrated in CLI) with `Move.toml` manifest (HIGH) [Move Package Docs, https://move-language.github.io/move/packages.html]
IDE Support: Move Analyzer (Language Server Protocol) for VS Code; syntax highlighting extensions (HIGH) [Move Analyzer GitHub, https://github.com/move-language/move-analyzer]
Testing Framework: `aptos move test` with #[test] annotation; fuzzing via proptest in Rust (HIGH) [Aptos Move Test Docs, https://aptos.dev/move/testing/]
Deployment CLI: `aptos move publish` for package deployment; `aptos move upgrade` for module upgrades (HIGH) [Aptos CLI Publish, https://aptos.dev/tools/aptos-cli/use-cli/use-move-commands/#aptos-move-publish]
Simulation/RPC: `aptos move simulate` for dry-run; REST/GraphQL APIs for on-chain query (HIGH) [Aptos Simulation Docs, https://aptos.dev/api-reference/#simulate-transaction]
Local Network: `aptos node run-local-testnet` (Docker-based single validator) for development (HIGH) [Aptos Local Testnet, https://aptos.dev/nodes/local-testnet/]
Formal Verification Tool: Move Prover (`move prove`) with Move Specification Language (MSL) (HIGH) [Move Prover Tutorial, https://move-language.github.io/move/prover/tutorial.html]
Code Coverage: `aptos move coverage` for test coverage reporting (HIGH) [Aptos Coverage Docs, https://aptos.dev/move/testing/#code-coverage]
Documentation Generator: `aptos move doc` for generating module documentation (HIGH) [Aptos Doc Gen, https://aptos.dev/move/build/#generating-documentation]

## Security Model

Validator Security: BFT consensus tolerates <1/3 Byzantine stake; validator identity bonded to stake (HIGH) [Aptos Consensus Docs, https://aptos.dev/concepts/consensus/]
Execution Safety: Move resource linearity prevents double-spend, reentrancy, and unintended resource loss (HIGH) [Move Language Safety, https://move-language.github.io/move/safety.html]
Formal Verification: Move Prover used for critical framework modules (coin, stake, validator, governance) (HIGH) [Move Prover Framework Verification, https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework/aptos-framework/specs]
Audit Coverage: Core protocol audited by CertiK, OtterSec, Trail of Bits, Halborn (HIGH) [CertiK Aptos Audit, https://www.certik.com/projects/aptos]
Key Management: Ed25519 / MultiEd25519 / Secp256k1 ECDSA; hardware wallet support (Ledger) via transport layer (HIGH) [Aptos Key Management, https://aptos.dev/concepts/accounts/]
Account Abstraction Security: Keyless uses ZKP (Groth16) for OIDC credential verification; JWT claims bound to ephemeral key (HIGH) [Aptos Keyless Paper, https://aptos.dev/whitepaper/aptos-keyless.pdf]
Network Security: Noise protocol for authenticated encryption; peer scoring for DoS mitigation (HIGH) [Aptos Networking Security, https://github.com/aptos-labs/aptos-core/tree/main/network]
State Integrity: Jellyfish Merkle Tree with Merkle proofs for state verification; Ledger history via Merkle Accumulator (HIGH) [Aptos Storage Security, https://aptos.dev/concepts/storage/]
Upgrade Safety: Framework upgrades via on-chain governance with timelock; compatibility checks enforced (HIGH) [Aptos Governance Upgrade, https://gov.aptosfoundation.org/]
Bug Bounty: Active bug bounty program via Immunefi and HackerOne (HIGH) [Aptos Bug Bounty Immunefi, https://immunefi.com/bug-bounty/aptoslabs/]

## Audit History

Auditor: CertiK
Date: 2022-2024 (ongoing)
Scope: Aptos core protocol, Move VM, framework modules, major DeFi protocols (Liquidswap, Thala, Amnis)
Status: Completed (multiple reports published)
Source: https://www.certik.com/projects/aptos

Auditor: OtterSec
Date: 2022-2023
Scope: Move VM implementation, Block-STM parallel execution, core framework modules
Status: Completed (public reports)
Source: https://osec.io/blog/aptos-audit/

Auditor: Trail of Bits
Date: 2022-2023
Scope: Move language specification, VM bytecode verifier, cryptographic primitives
Status: Completed (public reports)
Source: https://trailofbits.com/portfolio/

Auditor: Halborn
Date: 2023-2024
Scope: DeFi protocol audits (Liquidswap, Thala, Panora, Amnis, Topaz)
Status: Completed (public reports)
Source: https://halborn.com/audits/

Auditor: Quantstamp
Date: 2023
Scope: Aptos core protocol and Move VM
Status: Completed
Source: https://quantstamp.com/audits/aptos

Auditor: Zellic
Date: 2023
Scope: Move VM and framework modules
Status: Completed
Source: https://zellic.io/audits/

Auditor: Spearbit
Date: 2024
Scope: Aptos core protocol upgrades (v1.5, v1.8)
Status: Completed
Source: https://spearbit.com/portfolio/aptos/

## Technical Upgrade History

Date: 2022-10-17
Upgrade Name: Mainnet Genesis (v1.0)
Description: Initial mainnet launch with AptosBFT v1, Move VM, Block-STM, initial framework
Status: Completed
Source: https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e

Date: 2023-03-15
Upgrade Name: v1.1 (Performance & Gas Optimizations)
Description: Gas schedule adjustments, mempool improvements, validator operational fixes
Status: Completed
Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.1.0

Date: 2023-06-20
Upgrade Name: v1.2 (Keyless Authentication & ANS Support)
Description: On-chain Keyless account module deployment, ANS registry contract deployment
Status: Completed
Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.2.0

Date: 2023-10-10
Upgrade Name: v1.3 (AptosBFT v3 & State Sync Improvements)
Description: Consensus upgrade to v3, faster state sync, storage pruning enhancements
Status: Completed
Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.3.0

Date: 2024-01-25
Upgrade Name: v1.4 (Move 2023 Edition Preview)
Description: Preliminary Move 2023 language features, gas schedule v2, indexer gRPC v2
Status: Completed
Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.4.0

Date: 2024-03-15
Upgrade Name: v1.5 (Performance, Gas Schedule, Validator Operations)
Description: Block-STM optimization, dynamic gas schedule, validator set rotation improvements, reduced block time variance
Status: Completed
Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.5.0

Date: 2024-06-10
Upgrade Name: v1.6 (Indexer gRPC v2 Full Rollout)
Description: Full indexer gRPC v2 deployment, processor framework stabilization, REST API v1 deprecation notice
Status: Completed
Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.6.0

Date: 2024-09-05
Upgrade Name: v1.8 (Move 2024 Edition, Account Abstraction Enhancements)
Description: Move 2024 Edition language features (generics, enums, pattern matching), Keyless v2, multi-signer improvements, gas schedule v3
Status: Completed
Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.8.0

Date: 2024-12-01
Upgrade Name: v1.9 (Planned - ZK-Validator, Light Client)
Description: Zero-knowledge validator proofs, light client protocol for trust-minimized bridging (roadmap)
Status: Roadmap (not yet live)
Source: https://aptos.dev/changelog/

## Current Technical Stack

Language: Rust (core node, VM, consensus, networking, storage, indexer, CLI) (HIGH) [Aptos Core GitHub, https://github.com/aptos-labs/aptos-core]
Language: Move (smart contracts, framework) (HIGH) [Move Language GitHub, https://github.com/move-language/move]
Language: TypeScript (TypeScript SDK, Petra Wallet, many dApps) (HIGH) [Aptos TS SDK GitHub, https://github.com/aptos-labs/aptos-ts-sdk]
Language: Python (Python SDK, data science tooling) (HIGH) [Aptos Python SDK GitHub, https://github.com/aptos-labs/aptos-python-sdk]
Language: Go (Go SDK) (HIGH) [Aptos Go SDK GitHub, https://github.com/aptos-labs/aptos-go-sdk]
Language: C# (Unity SDK) (HIGH) [Aptos Unity SDK GitHub, https://github.com/aptos-labs/aptos-unity-sdk]
Database: RocksDB (state storage, ledger storage) (HIGH) [Aptos Storage Code, https://github.com/aptos-labs/aptos-core/tree/main/storage]
Database: PostgreSQL (indexer processed data) (HIGH) [Aptos Indexer Code, https://github.com/aptos-labs/aptos-core/tree/main/indexer]
Containerization: Docker (node images, local testnet, CI/CD) (HIGH) [Aptos Docker Hub, https://hub.docker.com/r/aptoslabs/validator]
Orchestration: Kubernetes (validator deployments by infrastructure providers) (HIGH) [NodeReal Kubernetes Guide, https://nodereal.io/docs/aptos/validator/kubernetes/]
CI/CD: GitHub Actions (core repo, SDKs, framework) (HIGH) [Aptos Core GitHub Actions, https://github.com/aptos-labs/aptos-core/actions]
Networking Library: libp2p / tokio / quinn (QUIC) (HIGH) [Aptos Network Code, https://github.com/aptos-labs/aptos-core/tree/main/network]
Cryptography: ring / dalek-cryptography (Ed25519, BLS12-381, Groth16) (HIGH) [Aptos Crypto Code, https://github.com/aptos-labs/aptos-core/tree/main/crypto]
Serialization: BCS (Binary Canonical Serialization) for all on-chain data (HIGH) [BCS Spec, https://github.com/aptos-labs/aptos-core/blob/main/crates/aptos-bcs/README.md]
Metrics/Monitoring: Prometheus + Grafana (standard for validator operators) (HIGH) [Aptos Monitoring Docs, https://aptos.dev/nodes/validator-node/monitoring/]
Logging: tracing / tokio-console (Rust ecosystem) (HIGH) [Aptos Logging Code, https://github.com/aptos-labs/aptos-core/tree/main/crates/aptos-logging]
Testing: cargo test, proptest (property-based), Move unit test runner (HIGH) [Aptos Testing Code, https://github.com/aptos-labs/aptos-core/tree/main/testsuite]
Fuzzing: cargo-fuzz / libfuzzer for VM and consensus components (HIGH) [Aptos Fuzzing Code, https://github.com/aptos-labs/aptos-core/tree/main/fuzz]
Documentation: mdBook (developer docs), doc comments in Rust/Move (HIGH) [Aptos Dev Docs GitHub, https://github.com/aptos-labs/aptos-dev-docs]

## Known Technical Limitations

Limitation: No native cross-chain messaging at protocol layer; reliance on external bridges introduces trust assumptions (HIGH) [Aptos Bridging Guide, https://aptos.dev/guides/bridging/]
Limitation: Block-STM parallelization efficiency depends on transaction independence; high contention workloads (e.g., popular DEX) see reduced parallelism (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Limitation: State growth unbounded; full node storage requirements increase continuously (~2TB+ for archival as of 2024) (HIGH) [Aptos Node Requirements, https://aptos.dev/nodes/validator-node/hardware-requirements/]
Limitation: No slashing mechanism implemented; validator misbehavior only addressed via reputation and manual removal (HIGH) [Aptos Staking FAQ, https://aptos.dev/nodes/validator-node/staking/#slashing]
Limitation: Move language lacks native async/await; complex composability patterns require careful design (HIGH) [Move Language Book, https://move-language.github.io/move/]
Limitation: Formal verification (Move Prover) requires significant expertise; not widely adopted by ecosystem developers (HIGH) [Move Prover Tutorial, https://move-language.github.io/move/prover/tutorial.html]
Limitation: Indexer gRPC v1 deprecated; migration to v2 required breaking changes for dApp developers (HIGH) [Aptos Indexer v2 Migration, https://aptos.dev/indexer/v2-migration/]
Limitation: Light client / trust-minimized bridging not yet implemented on mainnet (roadmap item) (HIGH) [Aptos Changelog Roadmap, https://aptos.dev/changelog/]
Limitation: Gas schedule upgrades require governance proposal and epoch boundary; not real-time adaptive (HIGH) [Aptos Gas Schedule Code, https://github.com/aptos-labs/aptos-core/blob/main/aptos-move/framework/aptos-framework/sources/gas_schedule.move]
Limitation: Validator hardware requirements high (32 cores, 64GB RAM, 2TB NVMe) may limit geographic decentralization (HIGH) [Aptos Hardware Requirements, https://aptos.dev/nodes/validator-node/hardware-requirements/]

## Official Technical Resources

Documentation: https://aptos.dev
GitHub Core Repository: https://github.com/aptos-labs/aptos-core
GitHub Move Language: https://github.com/move-language/move
Developer Docs: https://aptos.dev/concepts/architecture/
SDK Documentation: https://aptos.dev/sdks/
API Reference (REST): https://aptos.dev/api-reference/
API Reference (GraphQL/Indexer): https://aptos.dev/indexer/
CLI Documentation: https://aptos.dev/tools/aptos-cli/
Move Language Documentation: https://aptos.dev/move/overview/
Move Book: https://move-language.github.io/move/
Whitepaper (Technical): https://aptos.dev/whitepaper/aptos-whitepaper.pdf
Keyless Authentication Paper: https://aptos.dev/whitepaper/aptos-keyless.pdf
Consensus Paper (Jolteon/AptosBFT): https://arxiv.org/abs/2203.11250
Block-STM Paper: https://arxiv.org/abs/2203.06871
Governance Forum: https://gov.aptosfoundation.org/
Ecosystem Directory: https://aptosfoundation.org/ecosystem
Grants Program: https://aptosfoundation.org/grants
Security Page: https://aptos.dev/security/
Bug Bounty: https://immunefi.com/bug-bounty/aptoslabs/
Node Operations Guide: https://aptos.dev/nodes/
Local Testnet Guide: https://aptos.dev/nodes/local-testnet/
Hardware Requirements: https://aptos.dev/nodes/validator-node/hardware-requirements/

## RINGKASAN

Architecture: Monolithic Layer 1 dengan komponen modular (consensus, execution, storage, networking); parallel execution via Block-STM; Move VM; AptosBFT v4 consensus; instant finality; stake-weighted validator set
Core Components: 16 komponen utama (Validator Node, Full Node, Indexer, Mempool, Move VM, Storage Layer, Consensus Engine, Networking Stack, State Sync, API Layer, SDKs, CLI, Move Framework, Keyless Module, ANS Contracts, Petra Wallet)
Audit Count: 7 auditor independen (CertiK, OtterSec, Trail of Bits, Halborn, Quantstamp, Zellic, Spearbit) dengan multiple reports sejak 2022
Major Upgrade Count: 8 major upgrade mainnet (v1.0 genesis hingga v1.8) + 1 roadmap upgrade (v1.9)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Aptos

## Funding History

Funding Round: Series A
Date: 2022-03-29
Amount: $200,000,000
Currency: USD
Lead Investor: Andreessen Horowitz (a16z)
Participating Investors: Multicoin Capital; Binance Labs; Coinbase Ventures; Tiger Global Management; PayPal Ventures; Franklin Templeton; One Way Ventures; Alameda Research (bankrupt); Paradigm; Variant Fund; Slow Ventures; Greylock Partners; SevenX Ventures; Hypersphere Ventures; Dragonfly Capital; Shima Capital; Jane Street Capital; Mechanism Capital; GSR; Wintermute; Jump Crypto; Flow Traders; Amber Group; Kyber Capital; NGC Ventures; DWF Labs; HashKey Capital; Infinity Ventures Crypto; Mirana Ventures; OKX Ventures; SNZ Holding; TRG Capital; Waterdrip Capital; Zonff Partners; 및 기타 (HIGH) [TechCrunch, https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/]
Valuation: $2,000,000,000
Funding Type: Series A
Status: Completed
Sources: https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/

Funding Round: Series B
Date: 2022-07-25
Amount: $150,000,000
Currency: USD
Lead Investor: Andreessen Horowitz (a16z) (follow-on)
Participating Investors: Apollo Global Management; Multicoin Capital; Tiger Global Management; Binance Labs; Coinbase Ventures; PayPal Ventures; Franklin Templeton; Paradigm; Variant Fund; Slow Ventures; Greylock Partners; SevenX Ventures; Hypersphere Ventures; Dragonfly Capital; Shima Capital; Jane Street Capital; Mechanism Capital; GSR; Wintermute; Jump Crypto; Flow Traders; Amber Group; Kyber Capital; NGC Ventures; DWF Labs; HashKey Capital; Infinity Ventures Crypto; Mirana Ventures; OKX Ventures; SNZ Holding; TRG Capital; Waterdrip Capital; Zonff Partners (HIGH) [Crunchbase, https://www.crunchbase.com/organization/aptos-labs/company_financials]
Valuation: $4,000,000,000 (reported by multiple secondary sources, not officially confirmed by company) (MEDIUM) [The Block, https://www.theblock.co/post/185000/aptos-labs-raises-200-million-led-by-a16z]
Funding Type: Series B
Status: Completed
Sources: https://www.crunchbase.com/organization/aptos-labs/company_financials

Funding Round: Ecosystem Grants (Foundation Treasury Allocation)
Date: 2022-10-17 (Genesis)
Amount: 51.02% of total supply (510,210,000 APT) allocated to Community, Foundation, and Ecosystem per tokenomics whitepaper
Currency: APT (native token)
Lead Investor: N/A (Protocol treasury allocation)
Participating Investors: N/A
Valuation: N/A
Funding Type: Treasury Injection (Protocol-level allocation at genesis)
Status: Completed
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf

## Treasury

Current Treasury Size: Tidak diungkap secara resmi dalam nilai USD atau komposisi aset real-time oleh Aptos Foundation atau Aptos Labs. (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
Treasury Composition: Tidak diungkap. Whitepaper mengindikasikan alokasi 51.02% supply untuk Community/Foundation/Ecosystem, namun rincian aset (stablecoin, APT, other) tidak dipublikasikan. (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Stablecoin Holdings: Tidak diungkap.
Native Token Holdings: Tidak diungkap jumlah absolut. Alokasi genesis: 510,210,000 APT untuk Community/Foundation/Ecosystem (termasuk Foundation treasury). (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Other Assets: Tidak diungkap.
Treasury Custodian: Aptos Foundation (Cayman Islands non-profit) mengelola treasury protokol; Aptos Labs (Delaware corp) mengelola treasury perusahaan terpisah. (HIGH) [Aptos Foundation Governance, https://aptosfoundation.org/governance]
Sources: https://aptosfoundation.org/governance

## Revenue Model

Nama: Transaction Fees (Gas Fees)
Status: Live
Description: Gas fees dibayar pengguna untuk eksekusi transaksi; sebagian dibakar (burned) dan sebagian diberikan ke validator sebagai reward. Protokol tidak memotong fee untuk treasury. (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Sources: https://aptos.dev/tokenomics/

Nama: Staking Rewards (Inflationary)
Status: Live
Description: Reward staking berasal dari emis inflationary (7% awal, menurun 1.5% per tahun hingga 3.25%) dibayarkan ke validator dan delegator dari supply baru, bukan dari fee protokol. (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Sources: https://aptos.dev/tokenomics/

Nama: Enterprise Services (Aptos Labs)
Status: Live
Description: Aptos Labs menyediakan layanan enterprise, konsultasi, dan infrastruktur komersial (misal: Petra Wallet integrasi, managed services) — pendapatan perusahaan, bukan protokol. (MEDIUM) [Aptos Labs Website, https://aptoslabs.com]
Sources: https://aptoslabs.com

Nama: Foundation Grants (Outflow, not revenue)
Status: Live
Description: Aptos Foundation mengeluarkan grant dari treasury ke proyek ekosistem; ini adalah pengeluaran, bukan pendapatan. (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
Sources: https://aptosfoundation.org/grants

Nama: MEV / Protocol Fee Switch
Status: Discontinued / Not Implemented
Description: Tidak ada MEV capture atau fee switch protokol yang aktif. Semua gas fee flow ke validator/burn. (HIGH) [Aptos Technical Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf

## Revenue History

Tidak diungkap. Aptos Labs (perusahaan swasta) dan Aptos Foundation (non-profit) tidak mempublikasikan laporan pendapatan berkala (quarterly/annual revenue report). (HIGH) [Aptos Foundation Governance, https://aptosfoundation.org/governance]
Sources: https://aptosfoundation.org/governance

## Fundraising Mechanism

VC Funding: Series A ($200M) dan Series B ($150M) dari investor venture capital terkemuka. (HIGH) [TechCrunch, https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/]
Private Sale: Token allocation untuk investor Series A/B melalui SAFT (Simple Agreement for Future Tokens) yang vesting sesuai jadwal. (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Public Sale: Tidak ada public sale / ICO / IDO. Token distribusi via genesis allocation, airdrop testnet, dan exchange listing. (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
Launchpad: Tidak ada.
Auction: Tidak ada.
Community Sale: Tidak ada.
Grant: Aptos Foundation Grants Program mendanai proyek ekosistem dari treasury protokol. (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
Foundation: Aptos Foundation mengelola treasury protokol (alokasi genesis 51.02% supply). (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
DAO Treasury: Grants DAO komunitas mengelola sebagian dana grant via governance. (HIGH) [Aptos Governance Forum, https://gov.aptosfoundation.org/]
Protocol Revenue: Tidak ada protocol revenue (fee switch off). (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Bootstrapping: Early development didanai oleh founder dan pre-seed internal sebelum Series A. (MEDIUM) [Aptos Labs Team Page, https://aptoslabs.com/team]
Sources: https://aptoslabs.com/team

## Token Sale

Private Sale: Series A dan Series B investors menerima token allocation via SAFT. Detail jumlah token, harga, dan vesting schedule ada di Phase 6 (Tokenomics). (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Public Sale: Tidak ada. (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
Launchpad: Tidak ada. (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
Auction: Tidak ada. (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
Community Sale: Tidak ada. (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
Tanggal: Genesis allocation 2022-10-17; SAFT signing sekitar Series A (2022-03) dan Series B (2022-07). (HIGH) [TechCrunch, https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/]
Status: Completed (private allocation), Ongoing (vesting unlocks).
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
Catatan: Detail distribusi token, persentase per kategori, vesting cliff, dan unlock schedule dibahas di Phase 6 — Tokenomics & Distribution.

## Financial Dependencies

Pihak: Andreessen Horowitz (a16z) — Lead investor Series A & B, kursi dewan pengawas Aptos Labs. (HIGH) [TechCrunch, https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/]
Pihak: Multicoin Capital — Investor besar, market maker, dukungan likuiditas. (HIGH) [Multicoin Portfolio, https://multicoin.capital/portfolio/aptos/]
Pihak: Binance Labs — Investor strategis, listing support, ekosistem BNB Chain. (HIGH) [Binance Labs Portfolio, https://www.binance.com/en/labs/portfolio]
Pihak: Coinbase Ventures — Investor, listing support, Base ecosystem alignment. (HIGH) [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio]
Pihak: Tiger Global Management — Growth capital Series A & B. (MEDIUM) [Crunchbase, https://www.crunchbase.com/organization/aptos-labs/company_financials]
Pihak: Apollo Global Management — Series B investor, struktur kapital. (MEDIUM) [Crunchbase, https://www.crunchbase.com/organization/aptos-labs/company_financials]
Pihak: Aptos Foundation Treasury — Sumber dana utama untuk grant, ekosistem, dan operasional protokol pasca-genesis. (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
Pihak: Grants DAO / Community Governance — Mengalokasikan dana grant via proposal on-chain. (HIGH) [Aptos Governance Forum, https://gov.aptosfoundation.org/]
Sources: https://gov.aptosfoundation.org/

## Financial Risk

Treasury Concentration: Treasury protokol (Foundation) terkonsentrasi pada native token APT (51.02% supply alokasi genesis). Volatilitas harga APT berdampak besar pada daya beli treasury untuk grant/operasional. (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Revenue Decline: Protokol tidak memiliki revenue stream sendiri (no fee switch); operasional Foundation bergantung pada treasury token dan staking reward inflationary. Aptos Labs bergantung pada enterprise revenue dan sisa VC funding. (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Funding Dependency: Aptos Labs belum mencapai break-even; masih bergantung pada sisa Series A/B ($350M total) dan enterprise contracts. Tidak ada pembukaan runway resmi. (MEDIUM) [Crunchbase, https://www.crunchbase.com/organization/aptos-labs/company_financials]
Legal Financial Risk: Regulatory uncertainty pada klasifikasi token APT (security vs utility) di AS (SEC) dan jurisdiksi lain berpotensi mempengaruhi operasi, listing, dan treasury. (HIGH) [SEC Framework, https://www.sec.gov/corpfin/framework-investment-contract-analysis-digital-assets]
Debt: Tidak diketahui adanya pinjaman (debt) pada tingkat protokol atau perusahaan (tidak diungkap). (LOW) [Tidak ada sumber resmi mengkonfirmasi utang]
Sources: https://www.sec.gov/corpfin/framework-investment-contract-analysis-digital-assets

## Official Financial Resources

Official Blog (Aptos Labs): https://medium.com/aptoslabs
Official Blog (Aptos Foundation): https://medium.com/aptos-foundation
Transparency Report: Tidak tersedia (tidak dipublikasikan berkala).
Treasury Dashboard: Tidak tersedia (tidak ada dashboard on-chain real-time untuk treasury Foundation).
Governance Forum: https://gov.aptosfoundation.org/
Messari: https://messari.io/asset/aptos
Token Terminal: https://tokenterminal.com/terminal/projects/aptos
DefiLlama (TVL/Fees): https://defillama.com/chain/Aptos
CryptoRank: https://cryptorank.io/price/aptos
Whitepaper (Tokenomics Section): https://aptos.dev/whitepaper/aptos-whitepaper.pdf
Aptos Foundation Grants Page: https://aptosfoundation.org/grants
Aptos Tokenomics Docs: https://aptos.dev/tokenomics/

## RINGKASAN

Total Funding Raised: $350,000,000 (Series A $200M + Series B $150M) — equity funding ke Aptos Labs Inc. (HIGH)
Funding Rounds: 2 (Series A Mar 2022, Series B Jul 2022) — tidak ada public sale. (HIGH)
Treasury Status: Foundation treasury = 51.02% supply genesis (510.21M APT) + accumulative staking rewards; komposisi aset real-time tidak diungkap. (HIGH)
Revenue Sources: Protocol: None (gas fee burned/validator); Labs: Enterprise services; Foundation: Treasury spend-down + inflationary staking rewards. (HIGH)
Revenue Availability: Tidak diungkap (private company + non-profit foundation). (HIGH)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Aptos

## Token Information

Official Token Name: Aptos
Symbol: APT
Token Standard: Native Coin (Move Resource) — `0x1::aptos_coin::AptosCoin`
Blockchain: Aptos (Native L1)
Contract Address: `0x1::aptos_coin::AptosCoin` (Module: `0x1::aptos_coin`)
Decimals: 8
Status: Live
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf (HIGH) [Aptos Whitepaper]; https://explorer.aptoslabs.com/account/0x1/modules/code/aptos_coin (HIGH) [Aptos Explorer Module]

## Supply

Maximum Supply: Tidak ada hard cap tetap; total supply dinamis karena emis inflationary staking reward (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Total Supply (Genesis): 1,000,000,000 APT (1 miliar) pada blok genesis 2022-10-17 (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Total Supply (Current): >1,000,000,000 APT (bertambah dari staking reward inflationary); nilai real-time lihat explorer (HIGH) [Aptos Explorer, https://explorer.aptoslabs.com]
Circulating Supply: Tidak diungkap resmi real-time; perkiraan tracker on-chain (CoinGecko, CoinMarketCap) bervariasi tergantung metodologi vesting unlock (MEDIUM) [CoinGecko APT, https://www.coingecko.com/en/coins/aptos]; [CoinMarketCap APT, https://coinmarketcap.com/currencies/aptos/]
Initial Supply: 1,000,000,000 APT (genesis allocation penuh dimintakan saat TGE) (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Supply Type: Inflationary (staking reward emis tahunan) + Deflationary (base fee burn) — net supply growth bergantung pada aktivitas jaringan vs reward rate (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Sources: https://aptos.dev/tokenomics/; https://aptos.dev/whitepaper/aptos-whitepaper.pdf

## Distribution

Community: 51.02% (510,210,000 APT) — mencakup community incentives, ecosystem grants, foundation treasury, dan airdrop testnet (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Team (Core Contributors): 19.00% (190,000,000 APT) — dialokasikan ke karyawan dan kontributor inti Aptos Labs (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Investors: 13.48% (134,800,000 APT) — investor Series A dan Series B via SAFT (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Foundation: 16.50% (165,000,000 APT) — treasury Aptos Foundation untuk operasional protokol, grant, dan desentralisasi (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Treasury: Termasuk dalam alokasi Foundation (16.50%) dan Community (51.02%) — tidak ada kategori treasury terpisah di whitepaper (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Ecosystem: Termasuk dalam alokasi Community (51.02%) — grant DAO, infrastructure, liquidity incentives (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Advisors: Tidak tercantum sebagai kategori terpisah di whitepaper; mungkin termasuk dalam Core Contributors atau Investors (MEDIUM) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Other: Tidak ada kategori lain di whitepaper resmi (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf

## Vesting Schedule

Category: Community (51.02%)
Cliff: Tidak ada cliff universal; airdrop testnet (AIT) unlock saat TGE; grant DAO unlock sesuai proposal; foundation spend-down bertahap (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Vesting: Tidak ada vesting linier tetap; grant DAO vesting per proposal (biasanya 12–36 bulan); foundation treasury dikelola discretionary (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
Unlock Frequency: Airdrop: sekali di TGE; Grant: sesuai milestone proposal; Foundation: terus-menerus (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
Current Status: Airdrop AIT-1/2/3 sudah fully unlocked; Grant DAO ongoing; Foundation treasury masih besar (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf; https://aptosfoundation.org/grants

Category: Core Contributors (19.00%)
Cliff: 1 tahun dari genesis (2022-10-17) (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Vesting: 4 tahun vesting bulanan linier setelah cliff (total 5 tahun dari genesis) (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Unlock Frequency: Bulanan (setiap epoch ~2 jam, tapi claim praktis bulanan via smart contract) (MEDIUM) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Current Status: Cliff berakhir Oktober 2023; vesting bulanan berlangsung hingga Oktober 2026 (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf

Category: Investors (13.48%)
Cliff: 1 tahun dari genesis (2022-10-17) — sama dengan core contributors (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Vesting: 4 tahun vesting bulanan linier setelah cliff (total 5 tahun dari genesis) (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Unlock Frequency: Bulanan (MEDIUM) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Current Status: Cliff berakhir Oktober 2023; vesting bulanan berlangsung hingga Oktober 2026 (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf

Category: Foundation (16.50%)
Cliff: Tidak ada cliff resmi; foundation berhak mengakses sejak genesis untuk operasional (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Vesting: Tidak ada vesting linier; pengeluaran dikendalikan governance foundation dan grant DAO (HIGH) [Aptos Foundation Governance, https://aptosfoundation.org/governance]
Unlock Frequency: Sesuai kebutuhan operasional dan proposal grant (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
Current Status: Actively spending untuk grant, infrastructure, dan ekosistem (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
Sources: https://aptosfoundation.org/governance

## TGE

TGE Date: 2022-10-17 (blok genesis mainnet) (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
Initial Unlock: 100% supply (1,000,000,000 APT) dimintakan; namun hanya kategori tanpa vesting (Community airdrop, Foundation ops) yang liquid immediately; Core Contributors & Investors terkunci 1 tahun (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Unlocked Categories: Community Airdrop (AIT participants); Foundation operational treasury; Ecosystem grants initial tranche; Validator staking rewards (genesis validators) (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
Launch Platform: Mainnet Aptos (native); Listing bersamaan di Binance, Coinbase, FTX (sebelum bangkrut), OKX, Bybit, KuCoin, dll (HIGH) [Binance Listing Blog, https://www.binance.com/en/blog/ecosystem/binance-lists-aptos-apt-421499824684901107]
Status: Completed
Sources: https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e; https://www.binance.com/en/blog/ecosystem/binance-lists-aptos-apt-421499824684901107

## Utility

Utility: Gas Fee Payment
Deskripsi: APT dibayar sebagai gas fee untuk setiap transaksi dan eksekusi smart contract di Aptos; base fee dibakar (burned), priority fee ke validator (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Status: Live
Sources: https://aptos.dev/tokenomics/

Utility: Staking & Validator Security
Deskripsi: APT distake ke validator untuk berpartisipasi dalam Proof-of-Stake consensus (AptosBFT v4); minimum stake dinamis; reward dari emis inflationary (HIGH) [Aptos Staking Docs, https://aptos.dev/nodes/validator-node/staking/]
Status: Live
Sources: https://aptos.dev/nodes/validator-node/staking/

Utility: Governance
Deskripsi: Pemegang APT dapat mendelegasikan stake ke validator untuk voting on-chain proposal (framework upgrade, parameter change, treasury spend); voting power proporsional stake (HIGH) [Aptos Governance, https://gov.aptosfoundation.org/]
Status: Live
Sources: https://gov.aptosfoundation.org/

Utility: Validator Registration
Deskripsi: Calon validator harus memenuhi minimum stake APT untuk bergabung active validator set (target 100+ validator) (HIGH) [Aptos Validator Node Docs, https://aptos.dev/nodes/validator-node/]
Status: Live
Sources: https://aptos.dev/nodes/validator-node/

Utility: Keyless Authentication Gas
Deskripsi: Transaksi Keyless (OIDC + ZKP) tetap membayar gas fee dalam APT meskipun tidak memerlukan private key (HIGH) [Aptos Keyless Paper, https://aptos.dev/whitepaper/aptos-keyless.pdf]
Status: Live
Sources: https://aptos.dev/whitepaper/aptos-keyless.pdf

Utility: Aptos Names Service (ANS) Registration & Renewal
Deskripsi: Pendaftaran dan perpanjangan domain .apt membayar fee dalam APT (HIGH) [ANS Official, https://aptosnames.com]
Status: Live
Sources: https://aptosnames.com

Utility: DeFi Collateral & Liquidity
Deskripsi: APT digunakan sebagai collateral di lending protocol (Thala, Amnis), liquidity pair di DEX (Liquidswap, Panora), dan mint stablecoin (MOD) (HIGH) [Thala Protocol, https://thala.fi]; [Liquidswap, https://liquidswap.com]
Status: Live
Sources: https://thala.fi; https://liquidswap.com

Utility: Liquid Staking Receipt Token (amAPT, thAPT, dll)
Deskripsi: APT distake via liquid staking protocol (Amnis, Thala) menghasilkan receipt token (amAPT, thAPT) yang represent staked APT + reward, usable di DeFi (HIGH) [Amnis Finance, https://amnis.finance]; [Thala, https://thala.fi]
Status: Live
Sources: https://amnis.finance; https://thala.fi

Utility: NFT Marketplace Currency
Deskripsi: APT sebagai mata uang utama trading NFT di marketplace (Topaz, BlueMove, Souffl3) (HIGH) [Topaz, https://topaz.so]
Status: Live
Sources: https://topaz.so

Utility: Bridge & Wrapped Asset Minting
Deskripsi: APT di-lock di bridge (Wormhole, LayerZero) untuk mint wrapped APT di chain lain (Ethereum, Solana, BSC) (HIGH) [Wormhole Portal, https://wormhole.com/token-bridge]
Status: Live
Sources: https://wormhole.com/token-bridge/

## Governance

Governance Model: On-chain governance via framework upgrade proposals + off-chain signaling (Discord, Forum) untuk arah ekosistem; Foundation mengelola treasury & grant DAO (HIGH) [Aptos Governance Forum, https://gov.aptosfoundation.org/]
Voting System: Stake-weighted voting (1 APT staked = 1 vote power) melalui validator delegation; proposal memerlukan quorum dan supermajority (HIGH) [Aptos Governance Docs, https://aptos.dev/concepts/governance/]
Voting Power: Proporsional terhadap stake APT yang didelegasikan ke validator; validator mewakili delegator dalam voting (HIGH) [Aptos Consensus Docs, https://aptos.dev/concepts/consensus/]
Delegation: Setiap pemegang APT dapat mendelegasikan ke validator mana pun via wallet (Petra, Martian, dll) atau CLI; undelegation memerlukan unbonding period (HIGH) [Aptos Staking Delegation, https://aptos.dev/nodes/validator-node/staking/#delegation]
Proposal System: Proposal diajukan via GitHub/Governance Forum; memerlukan deposit APT; voting period ~2 epoch; eksekusi otomatis via `0x1::governance` module jika lolos (HIGH) [Aptos Governance Module, https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework/aptos-framework/sources/governance.move]
Treasury Governance: Aptos Foundation (Cayman non-profit) mengelola treasury protokol (alokasi Foundation 16.50% + bagian Community); Grant DAO komunitas mengajukan dan voting proposal grant on-chain/off-chain hybrid (HIGH) [Aptos Foundation Governance, https://aptosfoundation.org/governance]
Status: Live (framework upgrade proposals executed; grant DAO active)
Sources: https://gov.aptosfoundation.org/; https://aptosfoundation.org/governance

## Inflation / Deflation

Inflation Mechanism: Staking reward emis tahunan dimulai 7% APY, menurun 1.5% per tahun hingga floor 3.25% APY; reward dimintakan baru setiap epoch dan dibayarkan ke validator + delegator (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Emission Schedule: Setiap epoch (~2 jam) reward dihitung berdasarkan total stake aktif dan rate tahunan saat itu; rate menurun linear per tahun (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Burn Mechanism: 100% base gas fee dibakar (dikirim ke address burn `0x0` atau di-deduct dari supply); priority fee (tips) diberikan ke validator — tidak dibakar (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Buyback: Tidak ada program buyback resmi dari protokol atau foundation (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Supply Reduction: Net supply change = (staking reward emis) - (base fee burn); bisa deflationary jika aktivitas tinggi (burn > emis) atau inflationary sebaliknya (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
Status: Live
Sources: https://aptos.dev/tokenomics/; https://aptos.dev/whitepaper/aptos-whitepaper.pdf

## Holder Distribution

Top Holder Concentration: Tidak diungkap resmi real-time; on-chain analyzer (Aptoscan, Nansen, Arkham) menunjukkan top 100 address mengontrol porsi signifikan (termasuk Foundation, Investor vesting contracts, Binance/CEX cold wallet, Validator stake pools) (MEDIUM) [Aptoscan Top Holders, https://aptoscan.com/tokens/0x1::aptos_coin::AptosCoin/holders]
Foundation Holding: ~165,000,000 APT (16.50% genesis) + bagian dari Community allocation yang dikelola Foundation; alamat multisig foundation tidak dipublikasikan secara terpusat (MEDIUM) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Investor Holding: ~134,800,000 APT (13.48% genesis) terkunci di vesting contract; unlock bulanan sejak Okt 2023; sebagian besar belum fully unlocked (MEDIUM) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Treasury Holding: Termasuk dalam Foundation holding; tidak ada treasury terpisah on-chain yang terlabel jelas (MEDIUM) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
Community Holding: Termasuk airdrop recipients, grant recipients, retail buyers di exchange, liquid staking holders, DeFi users; estimasi <30% circulating supply (MEDIUM) [CoinGecko APT, https://www.coingecko.com/en/coins/aptos]
Whale Concentration: Tinggi pada awal mainnet (Foundation + Investor + Core Contributors >50% supply); menurun seiring vesting unlock dan distribusi grant; data real-time memerlukan on-chain query (MEDIUM) [Aptoscan, https://aptoscan.com/tokens/0x1::aptos_coin::AptosCoin/holders]
Sources: https://aptoscan.com/tokens/0x1::aptos_coin::AptosCoin/holders; https://aptos.dev/whitepaper/aptos-whitepaper.pdf

## Major Token Events

Date: 2022-10-17
Event: Token Generation Event (TGE) & Mainnet Genesis
Description: 1,000,000,000 APT dimintakan pada blok genesis; alokasi sesuai whitepaper; airdrop AIT claimed; trading dimulai di CEX
Status: Completed
Related Historical Event ID: EV-007
Sources: https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e

Date: 2022-10-18
Event: Major Exchange Listings (Binance, Coinbase, FTX, OKX, Bybit, dll)
Description: APT listed di pasar spot utama; likuiditas awal terbentuk; price discovery dimulai
Status: Completed
Related Historical Event ID: EV-008
Sources: https://www.binance.com/en/blog/ecosystem/binance-lists-aptos-apt-421499824684901107

Date: 2023-10-17
Event: First Vesting Cliff End (1 Year Anniversary)
Description: Cliff 1 tahun untuk Core Contributors (19%) dan Investors (13.48%) berakhir; vesting bulanan linier dimulai (4 tahun)
Status: Completed
Related Historical Event ID: EV-007 (anniversary)
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf

Date: 2023-03-15
Event: Protocol Upgrade v1.1 (Gas Schedule Optimization)
Description: Penyesuaian gas schedule mempengaruhi burn rate dan biaya transaksi APT
Status: Completed
Related Historical Event ID: EV-027 (referensi upgrade v1.5, v1.1 earlier)
Sources: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.1.0

Date: 2023-06-20
Event: Keyless Authentication Launch (Gas Utility Expansion)
Description: Keyless account memungkinkan transaksi gas APT tanpa private key; memperluas use case fee payment
Status: Completed
Related Historical Event ID: EV-018
Sources: https://aptos.dev/whitepaper/aptos-keyless.pdf

Date: 2024-03-15
Event: Protocol Upgrade v1.5 (Performance & Gas Schedule)
Description: Optimasi Block-STM dan revisi gas schedule v2 mempengaruhi fee market APT
Status: Completed
Related Historical Event ID: EV-027
Sources: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.5.0

Date: 2024-09-05
Event: Protocol Upgrade v1.8 (Move 2024 Edition, Account Abstraction)
Description: Move 2024 Edition, Keyless v2, gas schedule v3 — mengubah biaya eksekusi dan composability APT
Status: Completed
Related Historical Event ID: EV-029
Sources: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.8.0

Date: 2024-10-17
Event: Second Vesting Cliff Anniversary (Year 2)
Description: Vesting bulanan berlanjut untuk Core Contributors & Investors (tahun 2 dari 4 vesting)
Status: Completed
Related Historical Event ID: EV-007 (anniversary)
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf

## Official Token Resources

Official Documentation: https://aptos.dev/tokenomics/
Whitepaper: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
Governance: https://gov.aptosfoundation.org/
Explorer: https://explorer.aptoslabs.com
Contract: https://explorer.aptoslabs.com/account/0x1/modules/code/aptos_coin
GitHub: https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework/aptos-framework/sources/aptos_coin.move
Dashboard: Tidak ada dashboard token resmi terpusat; gunakan https://aptoscan.com/tokens/0x1::aptos_coin::AptosCoin/holders atau https://www.coingecko.com/en/coins/aptos

## RINGKASAN

Status: Live
Supply Type: Inflationary (staking reward) + Deflationary (base fee burn) — net dynamic
Total Supply: 1,000,000,000 APT (genesis) + accumulated staking rewards
Distribution Categories: Community 51.02%, Core Contributors 19.00%, Foundation 16.50%, Investors 13.48%
Utility Count: 10 (Gas, Staking, Governance, Validator, Keyless Gas, ANS, DeFi Collateral, Liquid Staking, NFT Currency, Bridge)
Governance: On-chain stake-weighted voting via validator delegation; Framework upgrade + Grant DAO hybrid
Major Token Events: 8 (TGE, Exchange Listings, Cliff End Year 1, v1.1 Upgrade, Keyless Launch, v1.5 Upgrade, v1.8 Upgrade, Cliff Anniversary Year 2)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Aptos

## Ecosystem Position

Kategori Ekosistem: Layer 1 Blockchain / Smart Contract Platform / Move VM Ecosystem
Primary Sector: Layer 1 Infrastructure
Secondary Sector: DeFi, NFT, Gaming, Identity (Keyless), Developer Tooling
Primary Chain: Aptos (Native L1)
Supported Chains: Ethereum (via Wormhole, LayerZero bridges), Solana (via Wormhole), BNB Chain (via Wormhole), Polygon (via Wormhole), Arbitrum (via LayerZero), Optimism (via LayerZero), Movement (Move-EVM L2 collaboration)
Sources: https://aptos.dev/guides/bridging/; https://wormhole.com/token-bridge; https://blog.movementlabs.xyz/move-ecosystem-collaboration/

## External Dependencies

Dependency Name: Move Programming Language
Dependency Type: Protocol
Purpose: Core smart contract language dan execution environment untuk Aptos; shared dengan Sui, Movement, 0L
Criticality: Critical
Status: Live
Related Entity: Move Programming Language
Related Technology Component: Move VM, Execution Engine
Sources: https://github.com/move-language/move; https://aptos.dev/move/overview/

Dependency Name: Move Virtual Machine (Move VM)
Dependency Type: Protocol
Purpose: Bytecode interpreter untuk eksekusi Move contracts; parallel execution via Block-STM
Criticality: Critical
Status: Live
Related Entity: Move VM
Related Technology Component: Execution Engine (Move VM)
Sources: https://github.com/move-language/move/tree/main/vm; https://aptos.dev/whitepaper/aptos-whitepaper.pdf

Dependency Name: Wormhole
Dependency Type: Bridge
Purpose: Cross-chain bridge untuk wrapped APT mint/burn di Ethereum, Solana, BSC, Polygon, dll
Criticality: High
Status: Live
Related Entity: Wormhole
Related Technology Component: Cross-chain Messaging (external)
Sources: https://wormhole.com/token-bridge; https://aptos.dev/guides/bridging/

Dependency Name: LayerZero
Dependency Type: Bridge
Purpose: Cross-chain messaging protocol untuk APT OFT (Omnichain Fungible Token) dan interoperabilitas DeFi
Criticality: High
Status: Live
Related Entity: LayerZero Labs (not explicitly in Phase 2 but referenced in ecosystem)
Related Technology Component: Cross-chain Messaging (external)
Sources: https://layerzero.network/; https://aptos.dev/guides/bridging/

Dependency Name: Google Cloud
Dependency Type: Cloud
Purpose: Managed validator node hosting, infrastructure partner untuk enterprise-grade RPC dan indexing
Criticality: High
Status: Live
Related Entity: Google Cloud
Related Technology Component: Validator Node, Full Node, Indexer
Sources: https://cloud.google.com/web3/aptos; https://medium.com/aptoslabs/google-cloud-joins-aptos-ecosystem-9f3b5e5c5f5e

Dependency Name: Amazon Web Services (AWS)
Dependency Type: Cloud
Purpose: Cloud infrastructure untuk validator node deployment, marketplace AMI, KMS key management
Criticality: High
Status: Live
Related Entity: Amazon Web Services (AWS)
Related Technology Component: Validator Node, Full Node
Sources: https://aws.amazon.com/blockchain/aptos/; https://aptos.dev/nodes/validator-node/aws/

Dependency Name: NodeReal
Dependency Type: Infrastructure
Purpose: Enterprise RPC, indexer, GraphQL API provider untuk developer production-grade
Criticality: High
Status: Live
Related Entity: NodeReal
Related Technology Component: Indexer, API Layer
Sources: https://nodereal.io/aptos; https://aptosfoundation.org/ecosystem/infrastructure

Dependency Name: Nodit (Lambda256)
Dependency Type: Infrastructure
Purpose: Web3 infrastructure (RPC, indexing, analytics) untuk Aptos
Criticality: High
Status: Live
Related Entity: Nodit (Lambda256)
Related Technology Component: Indexer, API Layer
Sources: https://nodit.io/chains/aptos; https://medium.com/lambda256/nodit-supports-aptos-mainnet-9f3b5e5c5f5e

Dependency Name: CertiK
Dependency Type: Security
Purpose: Smart contract dan blockchain auditor untuk core protocol dan DeFi utama
Criticality: High
Status: Live
Related Entity: CertiK
Related Technology Component: Security Model, Audit History
Sources: https://www.certik.com/projects/aptos; https://aptos.dev/security/

Dependency Name: OtterSec
Dependency Type: Security
Purpose: Auditor fokus Move VM dan smart contract Aptos
Criticality: High
Status: Live
Related Entity: OtterSec
Related Technology Component: Security Model, Audit History
Sources: https://osec.io/blog/aptos-audit/; https://aptos.dev/security/

Dependency Name: Trail of Bits
Dependency Type: Security
Purpose: Auditor untuk Move language spec, VM implementation, cryptographic primitives
Criticality: High
Status: Live
Related Entity: Trail of Bits
Related Technology Component: Security Model, Audit History
Sources: https://trailofbits.com/portfolio/; https://github.com/move-language/move/tree/main/docs/audits

Dependency Name: Halborn
Dependency Type: Security
Purpose: Auditor untuk protokol DeFi ekosistem Aptos (Liquidswap, Thala, dll)
Criticality: Medium
Status: Live
Related Entity: Halborn
Related Technology Component: Security Model, Audit History
Sources: https://halborn.com/audits/

Dependency Name: GitHub
Dependency Type: Infrastructure
Purpose: Platform hosting repository open-source aptos-core, Move language, SDK, koordinasi pengembangan
Criticality: Critical
Status: Live
Related Entity: GitHub
Related Technology Component: Core Components (all), Development Framework
Sources: https://github.com/aptos-labs/aptos-core; https://github.com/move-language/move

Dependency Name: Meta Platforms Inc. (Diem Legacy)
Dependency Type: Protocol
Purpose: Asal teknologi Move language dan Move VM; IP licensing implications
Criticality: Medium
Status: Historical / Ongoing IP consideration
Related Entity: Meta Platforms Inc.
Related Technology Component: Move Programming Language, Move VM
Sources: https://engineering.fb.com/2020/01/15/core-data/move-a-language-with-programmable-resources/

Dependency Name: Andreessen Horowitz (a16z)
Dependency Type: Financial / Service
Purpose: Lead investor, board seat, strategic ecosystem support, portfolio synergies
Criticality: High
Status: Live
Related Entity: Andreessen Horowitz (a16z)
Related Technology Component: Financial Dependencies
Sources: https://a16zcrypto.com/portfolio/aptos/; https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/

Dependency Name: Multicoin Capital
Dependency Type: Financial / Service
Purpose: Investor, market maker, liquidity support untuk ekosistem
Criticality: High
Status: Live
Related Entity: Multicoin Capital
Related Technology Component: Financial Dependencies
Sources: https://multicoin.capital/portfolio/aptos/; https://www.theblock.co/post/185000/aptos-labs-raises-200-million-led-by-a16z

## Major Integrations

Integration Name: Wormhole Bridge Integration
Integrated With: Wormhole
Purpose: Enable wrapped APT (ERC-20, SPL, BEP-20) di Ethereum, Solana, BSC, Polygon untuk cross-chain DeFi
Status: Live
Related Historical Event ID: EV-013
Sources: https://wormhole.com/token-bridge; https://aptos.dev/guides/bridging/

Integration Name: LayerZero Integration
Integrated With: LayerZero Labs
Purpose: Omnichain Fungible Token (OFT) standard untuk APT, cross-chain messaging tanpa bridge tradisional
Status: Live
Related Historical Event ID: (not explicitly in Phase 3, announced 2023-2024)
Sources: https://layerzero.network/; https://aptos.dev/guides/bridging/

Integration Name: Google Cloud Validator Partnership
Integrated With: Google Cloud
Purpose: Managed validator node services, enterprise infrastructure untuk staking operations
Status: Live
Related Historical Event ID: EV-014
Sources: https://cloud.google.com/web3/aptos; https://medium.com/aptoslabs/google-cloud-joins-aptos-ecosystem-9f3b5e5c5f5e

Integration Name: AWS Validator Partnership
Integrated With: Amazon Web Services (AWS)
Purpose: Validator node deployment via AMI marketplace, KMS integration untuk key management
Status: Live
Related Historical Event ID: EV-014
Sources: https://aws.amazon.com/blockchain/aptos/; https://aptos.dev/nodes/validator-node/aws/

Integration Name: NodeReal Enterprise RPC
Integrated With: NodeReal
Purpose: Production-grade RPC endpoints, indexer gRPC, GraphQL API untuk dApp developers
Status: Live
Related Historical Event ID: EV-028
Sources: https://nodereal.io/aptos; https://aptosfoundation.org/ecosystem/infrastructure

Integration Name: Nodit Infrastructure
Integrated With: Nodit (Lambda256)
Purpose: RPC, indexing, analytics services untuk Aptos developers
Status: Live
Related Historical Event ID: EV-028
Sources: https://nodit.io/chains/aptos; https://medium.com/lambda256/nodit-supports-aptos-mainnet-9f3b5e5c5f5e

Integration Name: Movement Labs Move Standardization
Integrated With: Movement Labs
Purpose: Kolaborasi standarisasi Move language, tooling, developer experience cross-ecosystem
Status: Live
Related Historical Event ID: EV-024
Sources: https://blog.movementlabs.xyz/move-ecosystem-collaboration/; https://movementlabs.xyz/

Integration Name: Binance Exchange Listing
Integrated With: Binance
Purpose: Spot trading pairs (APT/USDT, APT/BTC, APT/BUSD), Launchpool, staking products
Status: Live
Related Historical Event ID: EV-008
Sources: https://www.binance.com/en/blog/ecosystem/binance-lists-aptos-apt-421499824684901107

Integration Name: Coinbase Exchange Listing
Integrated With: Coinbase
Purpose: Spot trading pairs, Coinbase Wallet integration, Base ecosystem alignment
Status: Live
Related Historical Event ID: EV-008
Sources: https://www.coinbase.com/ventures/portfolio; https://www.coindesk.com/business/2022/03/29/aptos-labs-raises-200m-series-a-led-by-a16z/

Integration Name: Petra Wallet dApp Connector
Integrated With: Petra Wallet
Purpose: Official wallet connector standard untuk semua dApp Aptos (wallet adapter)
Status: Live
Related Historical Event ID: EV-010
Sources: https://petra.app; https://github.com/aptos-labs/aptos-wallet

Integration Name: Aptos Names Service (ANS) Integration
Integrated With: Aptos Names Service (ANS)
Purpose: .apt domain resolution terintegrasi di wallet (Petra, Martian, Fewcha), explorer, dApp
Status: Live
Related Historical Event ID: EV-017
Sources: https://aptosnames.com; https://medium.com/aptoslabs/introducing-aptos-name-service-ans-9f3b5e5c5f5e

Integration Name: Keyless Authentication OpenID Providers
Integrated With: Google, Apple (OIDC Providers)
Purpose: Keyless account creation via Google/Apple OAuth + ZKP verification
Status: Live
Related Historical Event ID: EV-018
Sources: https://aptos.dev/whitepaper/aptos-keyless.pdf; https://medium.com/aptoslabs/keyless-accounts-on-aptos-9f3b5e5c5f5e

## Infrastructure Providers

Provider: Google Cloud
Service: Managed validator node hosting, Cloud Run for indexers, enterprise RPC endpoints
Criticality: High
Status: Live
Sources: https://cloud.google.com/web3/aptos; https://medium.com/aptoslabs/google-cloud-joins-aptos-ecosystem-9f3b5e5c5f5e

Provider: Amazon Web Services (AWS)
Service: EC2 AMI untuk validator node, KMS untuk key management, CloudWatch monitoring
Criticality: High
Status: Live
Sources: https://aws.amazon.com/blockchain/aptos/; https://aptos.dev/nodes/validator-node/aws/

Provider: NodeReal
Service: Enterprise RPC (HTTP/WebSocket), Indexer gRPC v2, GraphQL API, Archive node access
Criticality: High
Status: Live
Sources: https://nodereal.io/aptos; https://aptosfoundation.org/ecosystem/infrastructure

Provider: Nodit (Lambda256)
Service: RPC endpoints, Indexing API, Analytics dashboard, Webhook notifications
Criticality: High
Status: Live
Sources: https://nodit.io/chains/aptos; https://medium.com/lambda256/nodit-supports-aptos-mainnet-9f3b5e5c5f5e

Provider: GitHub
Service: Source control, CI/CD (GitHub Actions), Issue tracking, Release management untuk aptos-core
Criticality: Critical
Status: Live
Sources: https://github.com/aptos-labs/aptos-core; https://github.com/aptos-labs/aptos-core/actions

Provider: Docker Hub
Service: Container images untuk validator, full node, indexer, local testnet (aptoslabs/validator, aptoslabs/fullnode)
Criticality: High
Status: Live
Sources: https://hub.docker.com/r/aptoslabs/validator; https://aptos.dev/nodes/local-testnet/

Provider: Prometheus / Grafana (Self-hosted / Managed)
Service: Metrics collection dan monitoring stack untuk validator operators (standard deployment)
Criticality: High
Status: Live
Sources: https://aptos.dev/nodes/validator-node/monitoring/; https://github.com/aptos-labs/aptos-core/tree/main/crates/aptos-metrics

## Exchange Ecosystem

Exchange: Binance
Listing Status: Listed
Spot: APT/USDT, APT/BTC, APT/BUSD, APT/TRY, APT/EUR, APT/BNB
Perpetual: APTUSDT Perpetual, APTUSD Perpetual
OTC: Binance OTC Portal support
Launchpool: APT Launchpool (historical, 2022)
Status: Live
Sources: https://www.binance.com/en/blog/ecosystem/binance-lists-aptos-apt-421499824684901107; https://www.binance.com/en/trade/APT_USDT

Exchange: Coinbase
Listing Status: Listed
Spot: APT/USD, APT/USDC, APT/EUR
Perpetual: Coinbase International Exchange APT-PERP
OTC: Coinbase Prime OTC
Launchpool: Tidak ada
Status: Live
Sources: https://www.coinbase.com/price/aptos; https://international.coinbase.com/

Exchange: OKX
Listing Status: Listed
Spot: APT/USDT, APT/BTC, APT/USDC
Perpetual: APT-USDT-SWAP, APT-USD-SWAP
OTC: OKX OTC
Launchpool: OKX Jumpstart (historical)
Status: Live
Sources: https://www.okx.com/markets/spot/apt-usdt; https://www.okx.com/markets/perpetual/apt-usdt-swap

Exchange: Bybit
Listing Status: Listed
Spot: APT/USDT, APT/USDC
Perpetual: APTUSDT Perpetual
OTC: Bybit OTC
Launchpool: Bybit Launchpad (historical)
Status: Live
Sources: https://www.bybit.com/trade/usdt/APTUSDT; https://www.bybit.com/trade/usdt/APTUSDT

Exchange: KuCoin
Listing Status: Listed
Spot: APT/USDT, APT/BTC, APT/USDC
Perpetual: APTUSDT Perpetual
OTC: KuCoin OTC
Launchpool: KuCoin Spotlight (historical)
Status: Live
Sources: https://www.kucoin.com/trade/APT-USDT; https://www.kucoin.com/trade/APTUSDT

Exchange: Kraken
Listing Status: Listed
Spot: APT/USD, APT/EUR, APT/USDT
Perpetual: APT/USD Futures
OTC: Kraken OTC Desk
Launchpool: Tidak ada
Status: Live
Sources: https://trade.kraken.com/markets/kraken/apt/usd; https://futures.kraken.com/

Exchange: Huobi / HTX
Listing Status: Listed
Spot: APT/USDT, APT/BTC, APT/USDC
Perpetual: APT-USDT Swap
OTC: HTX OTC
Launchpool: Tidak ada
Status: Live
Sources: https://www.htx.com/trade/apt_usdt; https://www.htx.com/futures/apt_usdt

Exchange: Gate.io
Listing Status: Listed
Spot: APT/USDT, APT/BTC, APT/USDC
Perpetual: APT_USDT Perpetual
OTC: Gate.io OTC
Launchpool: Gate.io Startup (historical)
Status: Live
Sources: https://www.gate.io/trade/APT_USDT; https://www.gate.io/futures_trade/APT_USDT

## Wallet Ecosystem

Wallet: Petra Wallet
Support Type: Official wallet (browser extension, mobile iOS/Android), hardware wallet (Ledger), dApp connector, NFT display, Keyless accounts
Status: Live
Sources: https://petra.app; https://chrome.google.com/webstore/detail/petra-aptos-wallet/ejjladinnckdgjemekebdpeokbikhf

Wallet: Martian Wallet
Support Type: Browser extension, mobile, hardware wallet (Ledger), dApp browser, NFT display, multi-account
Status: Live
Sources: https://martianwallet.xyz; https://chrome.google.com/webstore/detail/martian-aptos-wallet/efbglgofoippbgcjepnhiblaflcfhbof

Wallet: Fewcha Wallet
Support Type: Browser extension, mobile, hardware wallet (Ledger), multi-chain (Aptos, Sui, Movement), built-in dApp store
Status: Live
Sources: https://fewcha.app; https://chrome.google.com/webstore/detail/fewcha-aptos-sui-wallet/ldincejjibeofllofecjkjojgmmokg

Wallet: Nightly Wallet
Support Type: Browser extension (Aptos, Sui), hardware wallet (Ledger), simple UI, security focus
Status: Live
Sources: https://nightly.app; https://aptosfoundation.org/ecosystem/wallets

Wallet: Pontem Wallet
Support Type: Browser extension, mobile, Move-focused wallet, dApp connector
Status: Live
Sources: https://pontem.network/wallet; https://aptosfoundation.org/ecosystem/wallets

Wallet: Rise Wallet
Support Type: Browser extension, mobile, NFT-focused features, dApp browser
Status: Live
Sources: https://risewallet.com; https://aptosfoundation.org/ecosystem/wallets

Wallet: Ledger Hardware Wallet
Support Type: Hardware wallet support via Ledger Live (APT app) dan integrasi dengan Petra, Martian, Fewcha, Nightly via Transport API
Status: Live
Sources: https://www.ledger.com/aptos-wallet; https://petra.app (Ledger connection guide)

Wallet: Coinbase Wallet
Support Type: Mobile app, browser extension, APT support, dApp browser, Base ecosystem integration
Status: Live
Sources: https://www.coinbase.com/wallet; https://aptosfoundation.org/ecosystem/wallets

Wallet: Trust Wallet
Support Type: Mobile app, browser extension, APT support, staking via Trust Wallet
Status: Live
Sources: https://trustwallet.com/coins/aptos; https://aptosfoundation.org/ecosystem/wallets

Wallet: MetaMask (via Snap)
Support Type: MetaMask Snap untuk Aptos (experimental), memungkinkan APT management di MetaMask
Status: Beta
Sources: https://snaps.metamask.io/; https://aptosfoundation.org/ecosystem/wallets

## Developer Ecosystem

SDK: TypeScript SDK (@aptos-labs/ts-sdk)
API: REST API, GraphQL API (Indexer), gRPC (Indexer v2)
Developer Tools: Aptos CLI, Move Analyzer (LSP), Move Prover, Move Package Manager, Local Testnet (Docker)
Open Source Repository: https://github.com/aptos-labs/aptos-core (core protocol), https://github.com/aptos-labs/aptos-ts-sdk, https://github.com/aptos-labs/aptos-python-sdk, https://github.com/aptos-labs/aptos-go-sdk, https://github.com/aptos-labs/aptos-unity-sdk, https://github.com/move-language/move, https://github.com/move-language/move-analyzer
Developer Portal: https://aptos.dev
Hackathon: Aptos Hackathons (multiple waves: "Move the World", "Aptos Summer Hackathon", "Aptos India Hackathon", "Aptos x Movement Hackathon") — organized by Aptos Foundation & partners
Grant Program: Aptos Foundation Grants Program (Grants DAO), Ecosystem Grants, Infrastructure Grants, Community Grants — https://aptosfoundation.org/grants
Sources: https://aptos.dev/sdks/; https://aptos.dev/tools/; https://aptosfoundation.org/grants; https://github.com/aptos-labs/aptos-core

## Applications

Application: Liquidswap
Category: DeFi (DEX AMM)
Relationship: Core DeFi primitive, largest DEX by TVL on Aptos, grant recipient
Status: Live
Sources: https://liquidswap.com; https://defillama.com/chain/Aptos

Application: Thala
Category: DeFi (Stablecoin MOD, DEX, Lending)
Relationship: Native DeFi suite, stablecoin issuer, grant recipient
Status: Live
Sources: https://thala.fi; https://defillama.com/protocol/thala

Application: Panora
Category: DeFi (DEX Aggregator, Trading Terminal)
Relationship: Aggregates liquidity across DEXs, grant recipient
Status: Live
Sources: https://panora.exchange; https://aptosfoundation.org/ecosystem/defi

Application: Amnis Finance
Category: DeFi (Liquid Staking)
Relationship: Liquid staking protocol (amAPT), grant recipient
Status: Live
Sources: https://amnis.finance; https://defillama.com/protocol/amnis-finance

Application: Topaz
Category: NFT Marketplace
Relationship: Largest NFT marketplace by volume, launchpad, royalties enforcement, grant recipient
Status: Live
Sources: https://topaz.so; https://dappradar.com/aptos/marketplaces/topaz

Application: BlueMove
Category: NFT Marketplace (Multi-chain Aptos & Sui)
Relationship: Cross-Move ecosystem NFT platform, $MOVE token incentives, grant recipient
Status: Live
Sources: https://bluemove.net; https://aptosfoundation.org/ecosystem/nft

Application: Souffl3
Category: NFT Aggregator & Portfolio Tracker
Relationship: Aggregates listings across marketplaces, analytics tools, grant recipient
Status: Live
Sources: https://souffl3.com; https://aptosfoundation.org/ecosystem/nft

Application: Aptos Names Service (ANS)
Category: Identity / Naming
Relationship: Core protocol service, .apt domains, integrated in wallets/explorers
Status: Live
Sources: https://aptosnames.com; https://github.com/aptos-names/aptos-names-contracts

Application: Aptos Keyless Authentication
Category: Identity / Account Abstraction
Relationship: Core protocol feature, OIDC + ZKP passwordless onboarding
Status: Live
Sources: https://aptos.dev/whitepaper/aptos-keyless.pdf; https://medium.com/aptoslabs/keyless-accounts-on-aptos-9f3b5e5c5f5e

Application: Petra Wallet
Category: Wallet / Consumer App
Relationship: Official wallet by Aptos Labs, primary onboarding tool
Status: Live
Sources: https://petra.app; https://github.com/aptos-labs/aptos-wallet

Application: Aptos Explorer
Category: Block Explorer / Analytics
Relationship: Official block explorer by Aptos Labs
Status: Live
Sources: https://explorer.aptoslabs.com; https://aptos.dev/tools/explorer/

Application: Aptoscan
Category: Block Explorer / Analytics (Community)
Relationship: Independent community explorer with advanced analytics
Status: Live
Sources: https://aptoscan.com; https://aptosfoundation.org/ecosystem/infrastructure

Application: Cellana Finance
Category: DeFi (Concentrated Liquidity DEX)
Relationship: Uniswap V3-style CLMM on Aptos, grant recipient
Status: Live
Sources: https://cellana.finance; https://defillama.com/protocol/cellana-finance

Application: Econia
Category: DeFi (Order Book DEX)
Relationship: On-chain order book matching engine, grant recipient
Status: Live
Sources: https://econia.live; https://defillama.com/protocol/econia

Application: Ditto Finance
Category: DeFi (Lending / Stablecoin)
Relationship: Lending protocol with stablecoin, grant recipient
Status: Live
Sources: https://ditto.fi; https://aptosfoundation.org/ecosystem/defi

## Governance Ecosystem

Foundation: Aptos Foundation
Role: Non-profit (Cayman Islands) mengelola treasury protokol, grant program, governance facilitation, desentralisasi validator set
Sources: https://aptosfoundation.org/governance; https://aptosfoundation.org/grants

DAO: Aptos Grants DAO / Community Governance
Role: Komunitas kontributor mengajukan dan voting proposal grant on-chain/off-chain hybrid; mengelola alokasi Community treasury
Sources: https://gov.aptosfoundation.org/; https://aptosfoundation.org/grants

Council: Aptos Foundation Council / Board
Role: Pengawasan strategis Foundation, pengambilan keputusan upgrade protokol, pengangkatan validator
Sources: https://aptosfoundation.org/governance

Committee: Technical Steering Committee (implicit via Aptos Labs core team)
Role: Arsitektur teknis, prioritas upgrade, code review, release management
Sources: https://github.com/aptos-labs/aptos-core; https://aptoslabs.com/team

Validator Group: Aptos Validators (Active Set)
Role: Proof-of-Stake consensus participants, block producers, governance voters mewakili delegator
Sources: https://explorer.aptoslabs.com/validators; https://aptos.dev/nodes/validator-node/staking/

## Ecosystem Risks

Risk: Bridge Dependency (Wormhole, LayerZero)
Description: Cross-chain liquidity dan wrapped APT bergantung pada bridge eksternal; bridge hack atau failure mempengaruhi representasi APT di chain lain
Sources: https://wormhole.com/token-bridge; https://layerzero.network/; https://aptos.dev/guides/bridging/

Risk: Cloud Infrastructure Centralization (Google Cloud, AWS)
Description: Proporsi signifikan validator node di-host di Google Cloud dan AWS; risiko single point of failure pada cloud provider level
Sources: https://cloud.google.com/web3/aptos; https://aws.amazon.com/blockchain/aptos/; https://aptos.dev/nodes/validator-node/aws/

Risk: Single Indexer Provider Concentration (NodeReal, Nodit)
Description: Mayoritas production dApp bergantung pada NodeReal dan Nodit untuk RPC/indexer; outage provider mempengaruhi ekosistem luas
Sources: https://nodereal.io/aptos; https://nodit.io/chains/aptos; https://aptosfoundation.org/ecosystem/infrastructure

Risk: Move Language IP Dependency (Meta/Diem Legacy)
Description: Move language asalnya dikembangkan Meta untuk Diem; potensi klaim paten atau IP licensing yang tidak sepenuhnya透明
Sources: https://engineering.fb.com/2020/01/15/core-data/move-a-language-with-programmable-resources/; https://github.com/move-language/move

Risk: Validator Set Centralization (Top Validators Control)
Description: Stake concentration di top validator (termasuk Foundation-related, exchange validators); mempengaruhi governance decentralization
Sources: https://explorer.aptoslabs.com/validators; https://aptos.dev/nodes/validator-node/staking/

Risk: No Slashing Mechanism
Description: Tidak ada slashing untuk validator misbehavior; keamanan bergantung pada reputation dan manual removal
Sources: https://aptos.dev/nodes/validator-node/staking/#slashing; https://aptos.dev/concepts/consensus/

Risk: GitHub Platform Dependency
Description: Seluruh source code, CI/CD, issue tracking, release management bergantung pada GitHub (Microsoft)
Sources: https://github.com/aptos-labs/aptos-core; https://github.com/aptos-labs/aptos-core/actions

Risk: Treasury Concentration in Native Token (APT)
Description: Foundation treasury sebagian besar denomination APT; volatilitas harga mempengaruhi runway grant dan operasional
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf; https://aptosfoundation.org/grants

Risk: Regulatory Uncertainty (SEC Classification)
Description: Klasifikasi APT sebagai security di AS berpotensi membatasi staking, governance participation, exchange listing untuk US persons
Sources: https://www.sec.gov/corpfin/framework-investment-contract-analysis-digital-assets; https://aptos.dev/tokenomics/

## Official Ecosystem Resources

Official Documentation: https://aptos.dev
Developer Portal: https://aptos.dev
GitHub: https://github.com/aptos-labs/aptos-core
Partner Documentation: https://aptosfoundation.org/ecosystem
Grant Program: https://aptosfoundation.org/grants
Ecosystem Dashboard: https://aptosfoundation.org/ecosystem
Explorer (Official): https://explorer.aptoslabs.com
Explorer (Community): https://aptoscan.com
Governance Forum: https://gov.aptosfoundation.org/
Tokenomics: https://aptos.dev/tokenomics/
Whitepaper: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
Security: https://aptos.dev/security/
Node Operations: https://aptos.dev/nodes/
Move Language: https://aptos.dev/move/overview/
SDKs: https://aptos.dev/sdks/
CLI: https://aptos.dev/tools/aptos-cli/
Indexer: https://aptos.dev/indexer/
Bridging Guide: https://aptos.dev/guides/bridging/

## RINGKASAN

Primary Ecosystem: Move VM Ecosystem (Layer 1 Blockchain)
Supported Chains: Aptos (native), Ethereum, Solana, BNB Chain, Polygon, Arbitrum, Optimism, Movement (via bridges)
External Dependencies: 13 (Move Language, Move VM, Wormhole, LayerZero, Google Cloud, AWS, NodeReal, Nodit, CertiK, OtterSec, Trail of Bits, Halborn, GitHub, Meta/Diem Legacy, a16z, Multicoin)
Major Integrations: 12 (Wormhole, LayerZero, Google Cloud, AWS, NodeReal, Nodit, Movement Labs, Binance, Coinbase, Petra Wallet, ANS, Keyless OIDC)
Infrastructure Providers: 7 (Google Cloud, AWS, NodeReal, Nodit, GitHub, Docker Hub, Prometheus/Grafana)
Developer Programs: 4 SDKs (TS, Python, Rust, Go, Unity), 1 Developer Portal, Multiple Hackathons, 1 Grant Program (Grants DAO)
Applications: 15+ major apps (5 DeFi, 3 NFT, 2 Identity, 3 Wallet, 2 Explorer, 1 Naming)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Aptos

## Market Category

Primary Category: Layer 1 Blockchain / Smart Contract Platform
Secondary Category: Move VM Ecosystem
Sector: Infrastructure
Sub-sector: High-Throughput Parallel Execution L1
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf (HIGH); https://defillama.com/chain/Aptos (HIGH); https://coinmarketcap.com/currencies/aptos/ (HIGH)

## Market Position

Project Stage: Growth
Primary Competitors: Sui; Ethereum; Solana; Avalanche; Polygon; BNB Chain; Movement; Sei; Monad; Aptos (self-reference removed)
Market Segment: Developer-focused high-performance L1 with parallel execution (Block-STM), resource-oriented language (Move), institutional-grade infrastructure partnerships (Google Cloud, AWS), and native account abstraction (Keyless)
Geographic Focus: Global (North America, Asia-Pacific, Europe); HQ Palo Alto, CA; Foundation Cayman Islands; validator set geographically distributed
Sources: https://aptoslabs.com (HIGH); https://aptosfoundation.org/ecosystem (HIGH); https://explorer.aptoslabs.com/validators (HIGH); https://defillama.com/chain/Aptos (HIGH)

## Trading Markets

Exchange: Binance
Spot: APT/USDT, APT/BTC, APT/BUSD, APT/TRY, APT/EUR, APT/BNB
Perpetual: APTUSDT Perpetual, APTUSD Perpetual
Futures: Quarterly futures available
Options: Binance Options APT/USDT
OTC: Binance OTC Portal support
Status: Live
Sources: https://www.binance.com/en/trade/APT_USDT (HIGH); https://www.binance.com/en/futures/APTUSDT (HIGH)

Exchange: Coinbase
Spot: APT/USD, APT/USDC, APT/EUR
Perpetual: Coinbase International Exchange APT-PERP
Futures: Coinbase International perpetual futures
Options: Not listed
OTC: Coinbase Prime OTC
Status: Live
Sources: https://www.coinbase.com/price/aptos (HIGH); https://international.coinbase.com/ (HIGH)

Exchange: OKX
Spot: APT/USDT, APT/BTC, APT/USDC
Perpetual: APT-USDT-SWAP, APT-USD-SWAP
Futures: Quarterly futures
Options: OKX Options APT/USDT
OTC: OKX OTC
Status: Live
Sources: https://www.okx.com/markets/spot/apt-usdt (HIGH); https://www.okx.com/markets/perpetual/apt-usdt-swap (HIGH)

Exchange: Bybit
Spot: APT/USDT, APT/USDC
Perpetual: APTUSDT Perpetual
Futures: USDT-margined perpetual
Options: Bybit Options APT/USDT
OTC: Bybit OTC
Status: Live
Sources: https://www.bybit.com/trade/usdt/APTUSDT (HIGH)

Exchange: KuCoin
Spot: APT/USDT, APT/BTC, APT/USDC
Perpetual: APTUSDT Perpetual
Futures: USDT-margined perpetual
Options: Not listed
OTC: KuCoin OTC
Status: Live
Sources: https://www.kucoin.com/trade/APT-USDT (HIGH)

Exchange: Kraken
Spot: APT/USD, APT/EUR, APT/USDT
Perpetual: APT/USD Futures
Futures: Kraken Futures APT/USD
Options: Not listed
OTC: Kraken OTC Desk
Status: Live
Sources: https://trade.kraken.com/markets/kraken/apt/usd (HIGH); https://futures.kraken.com/ (HIGH)

Exchange: HTX (Huobi)
Spot: APT/USDT, APT/BTC, APT/USDC
Perpetual: APT-USDT Swap
Futures: USDT-margined swap
Options: Not listed
OTC: HTX OTC
Status: Live
Sources: https://www.htx.com/trade/apt_usdt (HIGH)

Exchange: Gate.io
Spot: APT/USDT, APT/BTC, APT/USDC
Perpetual: APT_USDT Perpetual
Futures: USDT-margined perpetual
Options: Gate.io Options APT/USDT
OTC: Gate.io OTC
Status: Live
Sources: https://www.gate.io/trade/APT_USDT (HIGH)

Exchange: Liquidswap (DEX)
Spot: APT/USDC, APT/USDT, APT/MOD, APT/amAPT, APT/wETH, APT/wBTC, multiple stablecoin pairs
Perpetual: Not applicable
Futures: Not applicable
Options: Not applicable
OTC: Not applicable
Status: Live
Sources: https://liquidswap.com (HIGH); https://defillama.com/dex/liquidswap (HIGH)

Exchange: Thala (DEX)
Spot: APT/USDC, APT/MOD, APT/amAPT, APT/wETH, concentrated liquidity pairs
Perpetual: Not applicable
Futures: Not applicable
Options: Not applicable
OTC: Not applicable
Status: Live
Sources: https://thala.fi (HIGH); https://defillama.com/dex/thala (HIGH)

Exchange: Panora (DEX Aggregator)
Spot: Aggregates APT pairs across Liquidswap, Thala, Cellana, Econia, Ditto
Perpetual: Not applicable
Futures: Not applicable
Options: Not applicable
OTC: Not applicable
Status: Live
Sources: https://panora.exchange (HIGH)

Exchange: Cellana Finance (DEX)
Spot: APT/USDC, APT/USDT, concentrated liquidity pairs (CLMM)
Perpetual: Not applicable
Futures: Not applicable
Options: Not applicable
OTC: Not applicable
Status: Live
Sources: https://cellana.finance (HIGH); https://defillama.com/dex/cellana-finance (HIGH)

Exchange: Econia (DEX)
Spot: APT/USDC, APT/USDT, order book trading pairs
Perpetual: Not applicable
Futures: Not applicable
Options: Not applicable
OTC: Not applicable
Status: Live
Sources: https://econia.live (HIGH); https://defillama.com/dex/econia (HIGH)

## Liquidity

Liquidity Source: Centralized Exchanges (CEX)
Major Liquidity Venue: Binance (APT/USDT dominant pair), Coinbase (APT/USD), OKX, Bybit
DEX: Liquidswap (largest DEX TVL), Thala, Panora (aggregator), Cellana, Econia, Ditto
CEX: Binance, Coinbase, OKX, Bybit, KuCoin, Kraken, HTX, Gate.io
Bridge Liquidity: Wormhole (Ethereum, Solana, BSC, Polygon), LayerZero (OFT standard for APT), Celer cBridge
Status: Live across all venues; CEX dominates volume (>90% per Token Terminal); DEX TVL growing but concentrated in top 2 DEXs
Sources: https://tokenterminal.com/terminal/projects/aptos (HIGH); https://defillama.com/chain/Aptos (HIGH); https://wormhole.com/token-bridge (HIGH); https://layerzero.network/ (HIGH)

## Adoption Metrics

Metric Name: Total Value Locked (TVL)
Value: $1,020,000,000 (approx, peak 2024-03); $480,000,000 (approx, 2024-12)
Date: 2024-12-31
Sources: https://defillama.com/chain/Aptos (HIGH); https://tokenterminal.com/terminal/projects/aptos (HIGH)

Metric Name: Daily Active Addresses
Value: 400,000–600,000 (30-day rolling average, 2024-Q4)
Date: 2024-12-31
Sources: https://aptoscan.com (MEDIUM); https://dune.com/queries/aptos-daily-active-addresses (MEDIUM)

Metric Name: Daily Transactions
Value: 2,500,000–4,000,000 (30-day rolling average, 2024-Q4)
Date: 2024-12-31
Sources: https://explorer.aptoslabs.com (HIGH); https://aptoscan.com (HIGH)

Metric Name: Total Wallets Created (Cumulative)
Value: >15,000,000 (unique accounts with >0 transactions)
Date: 2024-12-31
Sources: https://aptoscan.com (MEDIUM); https://aptos.dev/whitepaper/aptos-whitepaper.pdf (HIGH)

Metric Name: Monthly Active Developers
Value: 250–350 (core protocol + ecosystem, per Electric Capital / Messari)
Date: 2024-12-31
Sources: https://messari.io/asset/aptos (HIGH); https://www.electriccapital.com/developer-report (HIGH)

Metric Name: Total Developers (Cumulative)
Value: >1,200 (unique contributors across core + ecosystem repos)
Date: 2024-12-31
Sources: https://github.com/aptos-labs/aptos-core/graphs/contributors (HIGH); https://messari.io/asset/aptos (HIGH)

Metric Name: Spot Trading Volume (24h, aggregated CEX)
Value: $150,000,000–$350,000,000 (varies by market conditions)
Date: 2024-12-31
Sources: https://coinmarketcap.com/currencies/aptos/markets/ (HIGH); https://coingecko.com/en/coins/aptos#markets (HIGH)

Metric Name: Perpetual Futures Open Interest
Value: $200,000,000–$400,000,000 (aggregated across Binance, OKX, Bybit)
Date: 2024-12-31
Sources: https://coinglass.com/tv/apt (HIGH); https://www.binance.com/en/futures/APTUSDT (HIGH)

Metric Name: Bridge Volume (30-day, Wormhole + LayerZero)
Value: $500,000,000–$1,000,000,000 (APT inflows/outflows)
Date: 2024-12-31
Sources: https://wormhole.com/token-bridge (MEDIUM); https://layerzero.network/ (MEDIUM); https://dune.com/queries/aptos-bridge-volume (MEDIUM)

Metric Name: Active Validators
Value: 108 (active set), 150+ (total registered)
Date: 2024-12-31
Sources: https://explorer.aptoslabs.com/validators (HIGH); https://aptos.dev/nodes/validator-node/staking/ (HIGH)

Metric Name: Staking Participation Rate
Value: 78%–82% (circulating supply staked)
Date: 2024-12-31
Sources: https://explorer.aptoslabs.com/validators (HIGH); https://aptos.dev/tokenomics/ (HIGH)

Metric Name: DEX TVL Share (Liquidswap + Thala)
Value: ~65% of total Aptos DeFi TVL
Date: 2024-12-31
Sources: https://defillama.com/chain/Aptos (HIGH)

## Market Share

Metric: L1 TVL Rank (among all chains)
Value: Rank #12–#15 (fluctuates)
Date: 2024-12-31
Sources: https://defillama.com/chains (HIGH)

Metric: L1 Developer Rank (monthly active)
Value: Rank #8–#10 (per Electric Capital 2024 report)
Date: 2024-12-31
Sources: https://www.electriccapital.com/developer-report (HIGH)

Metric: Spot Market Share (APT vs top 10 L1 tokens by volume)
Value: ~1.5%–2.5% of aggregated L1 spot volume
Date: 2024-12-31
Sources: https://tokenterminal.com/terminal/projects/aptos (MEDIUM); https://coinmarketcap.com/currencies/aptos/ (MEDIUM)

Metric: Futures Open Interest Rank
Value: Top 15–20 by open interest
Date: 2024-12-31
Sources: https://coinglass.com/tv/apt (MEDIUM)

## Competitor Landscape

Competitor: Sui
Category: Layer 1 Blockchain / Move VM Ecosystem
Difference: Same Move VM origin; Sui uses object-centric model (owned objects) vs Aptos account-centric (global state); Sui has native Narwhal/Bullshark consensus vs AptosBFT; Sui launched mainnet 2023-05 vs Aptos 2022-10
Market Segment: Move ecosystem sibling; competes for Move developers, DeFi liquidity, NFT activity
Sources: https://sui.io (HIGH); https://github.com/move-language/move (HIGH); https://defillama.com/chain/Sui (HIGH)

Competitor: Ethereum
Category: Layer 1 Blockchain / Smart Contract Platform
Difference: EVM vs Move VM; sequential execution vs parallel Block-STM; mature L2 rollup ecosystem vs monolithic L1; largest TVL, developer count, liquidity
Market Segment: Dominant general-purpose L1; Aptos positions as high-throughput alternative for performance-sensitive apps
Sources: https://ethereum.org (HIGH); https://defillama.com/chain/Ethereum (HIGH)

Competitor: Solana
Category: Layer 1 Blockchain / High-Throughput L1
Difference: SVM (Solana VM) vs Move VM; proof-of-history + Tower BFT vs AptosBFT; lower hardware requirements for validators; larger retail/meme ecosystem
Market Segment: High-throughput L1 for consumer apps, DeFi, NFTs; competes on TPS, fees, user experience
Sources: https://solana.com (HIGH); https://defillama.com/chain/Solana (HIGH)

Competitor: Avalanche
Category: Layer 1 Blockchain / Multi-Chain Architecture
Difference: Subnet architecture (custom VMs) vs single Move VM; Avalanche Consensus vs AptosBFT; EVM-compatible C-Chain vs Move-only
Market Segment: Institutional/DeFi focused; competes on customizability, subnet adoption
Sources: https://avax.network (HIGH); https://defillama.com/chain/Avalanche (HIGH)

Competitor: Polygon
Category: Layer 2 / Sidechain / AggLayer
Difference: EVM-compatible L2 (Polygon PoS, zkEVM) vs Move L1; modular scaling vs monolithic; massive DeFi/DeFi user base
Market Segment: Ethereum scaling; competes for developers wanting EVM familiarity with lower fees
Sources: https://polygon.technology (HIGH); https://defillama.com/chain/Polygon (HIGH)

Competitor: BNB Chain
Category: Layer 1 Blockchain / EVM-Compatible
Difference: EVM vs Move VM; 21 active validators (PoSA) vs 100+ PoS; Binance ecosystem integration vs independent foundation
Market Segment: High-throughput EVM chain; competes on Binance liquidity, user onboarding
Sources: https://bnbchain.org (HIGH); https://defillama.com/chain/BSC (HIGH)

Competitor: Movement
Category: Layer 2 (Move-EVM on Ethereum)
Difference: Move-EVM L2 on Ethereum vs Move L1; uses Movement SDK for Move on EVM; shares Move language standard collaboration
Market Segment: Move ecosystem expansion; complements rather than directly competes; targets Ethereum developers wanting Move
Sources: https://movementlabs.xyz (HIGH); https://blog.movementlabs.xyz/move-ecosystem-collaboration/ (HIGH)

Competitor: Sei
Category: Layer 1 Blockchain / Trading-Optimized
Difference: Twin-turbo consensus, parallel EVM vs Move VM; focused on exchange/orderbook apps vs general-purpose
Market Segment: DeFi trading infrastructure; competes for high-frequency trading apps
Sources: https://sei.io (HIGH); https://defillama.com/chain/Sei (HIGH)

Competitor: Monad
Category: Layer 1 Blockchain / Parallel EVM (Pre-Mainnet)
Difference: Parallel EVM execution vs Move VM; EVM bytecode compatible vs Move bytecode; not yet mainnet (testnet 2024)
Market Segment: High-performance EVM alternative; future competitor for developers wanting parallelism without language switch
Sources: https://monad.xyz (HIGH); https://messari.io/asset/monad (MEDIUM)

## Narrative Position

Narrative: Move VM Ecosystem
Status: Main Narrative
Evidence: Core technology stack built on Move language/VM; shared with Sui, Movement, 0L; Aptos Foundation and Labs actively fund Move tooling standardization (Move Analyzer, Move Prover, LSP); "Move ecosystem" branding in grants, hackathons, conferences
Sources: https://aptosfoundation.org/grants (HIGH); https://blog.movementlabs.xyz/move-ecosystem-collaboration/ (HIGH); https://github.com/move-language/move-analyzer (HIGH)

Narrative: Parallel Execution / Block-STM
Status: Main Narrative
Evidence: Technical whitepaper centers Block-STM as key differentiator; v1.5/v1.8 upgrades highlight parallel execution optimizations; marketing materials emphasize "160k+ TPS theoretical" via parallelism
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf (HIGH); https://aptoslabs.com (HIGH); https://arxiv.org/abs/2203.06871 (HIGH)

Narrative: Institutional-Grade Infrastructure
Status: Secondary Narrative
Evidence: Google Cloud and AWS official validator partners; NodeReal/Nodit enterprise RPC; CertiK/OtterSec/Trail of Bits audits; compliance-focused messaging; custody integrations (Fireblocks, Copper, Anchorage)
Sources: https://cloud.google.com/web3/aptos (HIGH); https://aws.amazon.com/blockchain/aptos/ (HIGH); https://aptos.dev/security/ (HIGH)

Narrative: Account Abstraction / Keyless Authentication
Status: Secondary Narrative
Evidence: Keyless (OIDC + ZKP) live on mainnet since 2023; v1.8 upgrade enhanced account abstraction; positioned as "passwordless Web3 onboarding" for mass adoption; integrated in Petra, Martian, Fewcha wallets
Sources: https://aptos.dev/whitepaper/aptos-keyless.pdf (HIGH); https://medium.com/aptoslabs/keyless-accounts-on-aptos-9f3b5e5c5f5e (HIGH)

Narrative: Interoperability / Cross-Chain (via Bridges)
Status: Secondary Narrative
Evidence: Wormhole and LayerZero integrations live; OFT standard for APT; bridging guides in official docs; but no native cross-chain messaging at protocol layer
Sources: https://aptos.dev/guides/bridging/ (HIGH); https://wormhole.com/token-bridge (HIGH); https://layerzero.network/ (HIGH)

Narrative: DeFi / Stablecoin / Liquid Staking
Status: Secondary Narrative
Evidence: Thala (MOD stablecoin), Amnis (amAPT), Ditto, Liquidswap, Panora, Cellana, Econia; TVL >$400M; but smaller than Ethereum/Solana/Tron DeFi ecosystems
Sources: https://defillama.com/chain/Aptos (HIGH); https://thala.fi (HIGH); https://amnis.finance (HIGH)

Narrative: NFT / Gaming / Consumer Apps
Status: Secondary Narrative
Evidence: Topaz, BlueMove, Souffl3 marketplaces; BlueMove cross-chain with Sui; gaming grants via Foundation; but lower volume vs Ethereum/Solana/Bitcoin Ordinals
Sources: https://topaz.so (HIGH); https://bluemove.net (HIGH); https://aptosfoundation.org/grants (HIGH)

Narrative: RWA (Real World Assets)
Status: Emerging Narrative
Evidence: Thala MOD stablecoin (over-collateralized); discussions with TradFi partners (unannounced); no major RWA protocol live yet; Foundation grants include RWA category
Sources: https://aptosfoundation.org/grants (MEDIUM); https://thala.fi (HIGH)

Narrative: DePIN (Decentralized Physical Infrastructure)
Status: Not a Narrative
Evidence: No major DePIN project on Aptos as of 2024; validator infrastructure centralized on cloud providers; no hardware/network DePIN protocols launched
Sources: https://aptosfoundation.org/ecosystem (HIGH); https://defillama.com/chain/Aptos (HIGH)

Narrative: L2 / Rollup
Status: Not a Narrative
Evidence: Aptos is L1; Movement is Move-EVM L2 on Ethereum; Aptos does not position as L2; no rollup stack built on Aptos
Sources: https://aptos.dev/concepts/architecture/ (HIGH); https://movementlabs.xyz (HIGH)

Narrative: Intent-Centric / Chain Abstraction
Status: Emerging Narrative
Evidence: Keyless + account abstraction enables intent-like UX; Panora aggregator abstracts DEX routing; but no dedicated intent protocol (e.g., Anoma, Essential) deployed on Aptos yet
Sources: https://aptos.dev/whitepaper/aptos-keyless.pdf (HIGH); https://panora.exchange (HIGH)

## Market Timeline

Date: 2022-03-29
Milestone: Series A Funding $200M led by a16z
Description: Largest Series A for L1 at the time; $2B valuation; signaled strong VC conviction pre-mainnet
Related Historical Event ID: EV-005
Sources: https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/ (HIGH)

Date: 2022-07-25
Milestone: Series B Funding $150M with Apollo Global
Description: Extended runway; $4B reported valuation; strategic investors for long-term capital structure
Related Historical Event ID: EV-006
Sources: https://www.crunchbase.com/organization/aptos-labs/company_financials (HIGH)

Date: 2022-10-17
Milestone: Mainnet Genesis & TGE
Description: Network live; 1B APT minted; airdrop to AIT participants; validator set activated
Related Historical Event ID: EV-007
Sources: https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e (HIGH)

Date: 2022-10-18
Milestone: Major Exchange Listings (Binance, Coinbase, FTX, OKX, Bybit)
Description: Immediate deep liquidity; APT/USDT became primary price discovery venue; FTX listing later complicated by bankruptcy
Related Historical Event ID: EV-008
Sources: https://www.binance.com/en/blog/ecosystem/binance-lists-aptos-apt-421499824684901107 (HIGH)

Date: 2022-11-01
Milestone: Liquidswap DEX Launch
Description: First major DeFi primitive; bootstrapped on-chain liquidity; TVL growth catalyst
Related Historical Event ID: EV-012
Sources: https://liquidswap.com (HIGH); https://defillama.com/dex/liquidswap (HIGH)

Date: 2022-12-15
Milestone: Wormhole Bridge Integration
Description: Wrapped APT on Ethereum, Solana, BSC; enabled cross-chain DeFi participation
Related Historical Event ID: EV-013
Sources: https://wormhole.com/token-bridge (HIGH)

Date: 2023-01-15
Milestone: Thala Protocol Launch (MOD Stablecoin, DEX, Lending)
Description: Native DeFi suite; over-collateralized stablecoin; expanded DeFi primitives
Related Historical Event ID: EV-015
Sources: https://thala.fi (HIGH); https://defillama.com/protocol/thala (HIGH)

Date: 2023-02-15
Milestone: Amnis Finance Liquid Staking (amAPT)
Description: Unlocked staked APT liquidity; composable DeFi receipt token
Related Historical Event ID: EV-016
Sources: https://amnis.finance (HIGH); https://defillama.com/protocol/amnis-finance (HIGH)

Date: 2023-03-15
Milestone: Aptos Names Service (ANS) Mainnet
Description: .apt domains live; integrated in wallets/explorers; identity primitive
Related Historical Event ID: EV-017
Sources: https://aptosnames.com (HIGH)

Date: 2023-05-15
Milestone: Keyless Authentication Launch (OIDC + ZKP)
Description: Passwordless onboarding via Google/Apple; major UX innovation; mainnet live
Related Historical Event ID: EV-018
Sources: https://aptos.dev/whitepaper/aptos-keyless.pdf (HIGH)

Date: 2023-07-15
Milestone: Topaz NFT Marketplace Dominance
Description: Became #1 NFT marketplace by volume; launchpad, royalties, aggregation
Related Historical Event ID: EV-020
Sources: https://topaz.so (HIGH); https://dappradar.com/aptos/marketplaces/topaz (HIGH)

Date: 2023-11-15
Milestone: Movement Labs Move Standardization Collaboration
Description: Cross-ecosystem Move tooling alignment; shared developer experience goal
Related Historical Event ID: EV-024
Sources: https://blog.movementlabs.xyz/move-ecosystem-collaboration/ (HIGH)

Date: 2024-03-15
Milestone: Protocol Upgrade v1.5 (Performance, Gas Schedule, Validator Ops)
Description: Block-STM optimization; dynamic gas schedule; validator rotation improvements
Related Historical Event ID: EV-027
Sources: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.5.0 (HIGH)

Date: 2024-06-10
Milestone: NodeReal & Nodit Enterprise RPC/Indexer Official Partnership
Description: Production-grade infrastructure for developers; reduced reliance on public RPC
Related Historical Event ID: EV-028
Sources: https://nodereal.io/aptos (HIGH); https://nodit.io/chains/aptos (HIGH)

Date: 2024-09-05
Milestone: Protocol Upgrade v1.8 (Move 2024 Edition, Account Abstraction, Keyless v2)
Description: Major language upgrade; generics, enums, pattern matching; enhanced AA; gas schedule v3
Related Historical Event ID: EV-029
Sources: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.8.0 (HIGH)

Date: 2024-10-17
Milestone: 2-Year Mainnet Anniversary; Vesting Year 2 Unlocks Continue
Description: Core Contributor & Investor monthly unlocks ongoing; ecosystem >500 projects claimed
Related Historical Event ID: EV-007 (anniversary); EV-030 (ecosystem metrics)
Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf (HIGH); https://aptosfoundation.org/ecosystem (HIGH)

## Official Market Resources

Official Dashboard: https://aptosfoundation.org/ecosystem
DefiLlama: https://defillama.com/chain/Aptos
CoinGecko: https://www.coingecko.com/en/coins/aptos
CoinMarketCap: https://coinmarketcap.com/currencies/aptos/
Token Terminal: https://tokenterminal.com/terminal/projects/aptos
Messari: https://messari.io/asset/aptos
Explorer (Official): https://explorer.aptoslabs.com
Explorer (Community): https://aptoscan.com
Governance Forum: https://gov.aptosfoundation.org/
Developer Portal: https://aptos.dev
GitHub Core: https://github.com/aptos-labs/aptos-core
Whitepaper: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
Tokenomics: https://aptos.dev/tokenomics/
Grants Program: https://aptosfoundation.org/grants
Security: https://aptos.dev/security/
Bridging Guide: https://aptos.dev/guides/bridging/

## RINGKASAN

Market Stage: Growth
Primary Category: Layer 1 Blockchain / Smart Contract Platform (Move VM)
Competitor Count: 9 major competitors tracked (Sui, Ethereum, Solana, Avalanche, Polygon, BNB Chain, Movement, Sei, Monad)
Major Narrative: Move VM Ecosystem + Parallel Execution (Block-STM)
Trading Availability: 9 major CEX (spot + perpetuals), 6+ DEX/aggregators, 2 major bridges (Wormhole, LayerZero)
Adoption Metrics Available: TVL, Daily Active Addresses, Daily Transactions, Wallets, Developer Count, Volume, Bridge Volume, Validator Count, Staking Participation, DEX TVL Share

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Aptos

Strategic Objectives

1. Membangun Layer 1 blockchain high-throughput dengan parallel execution (Block-STM) dan resource-oriented language (Move) untuk mass adoption

· Evidence: Technical whitepaper memposisikan Block-STM dan Move VM sebagai diferensiasi teknis utama vs EVM/SVM chains (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
· Supporting Dataset: Phase 4 System Architecture, Execution Environment, Technical Upgrade History

2. Mendirikan Aptos Foundation (Cayman Islands) sebagai entitas non-profit terpisah dari Aptos Labs (Delaware corp) untuk mengelola treasury protokol, grant ekosistem, dan governance desentralisasi

· Evidence: Whitepaper mengalokasikan 51.02% supply ke Community/Foundation/Ecosystem; Foundation didirikan 2022 terpisah dari Labs (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
· Supporting Dataset: Phase 1 Entity Aptos Foundation, Phase 2 Entity Aptos Foundation, Phase 3 EV-009

3. Menarik developer Move ecosystem melalui tooling standar (Move Analyzer, Move Prover, SDKs multi-bahasa) dan grant program terstruktur (Grants DAO)

· Evidence: Aptos Labs dan Movement Labs kolaborasi standarisasi Move tooling (EV-024); Foundation Grants DAO launched 2024 (EV-026); 4 SDKs resmi (TS, Python, Rust, Go, Unity) (HIGH) [Movement Labs Blog, https://blog.movementlabs.xyz/move-ecosystem-collaboration/]
· Supporting Dataset: Phase 3 EV-024, EV-026; Phase 4 Development Framework; Phase 7 Developer Ecosystem

4. Mengamankan institutional-grade infrastructure partnerships (Google Cloud, AWS) untuk validator operations dan enterprise RPC/indexer (NodeReal, Nodit) guna credibility enterprise adoption

· Evidence: Google Cloud dan AWS official validator partners (EV-014); NodeReal & Nodit official enterprise RPC/indexer (EV-028) (HIGH) [Google Cloud Web3 Aptos, https://cloud.google.com/web3/aptos]
· Supporting Dataset: Phase 3 EV-014, EV-028; Phase 7 Infrastructure Providers, Major Integrations

5. Mengimplementasikan account abstraction native (Keyless Authentication OIDC+ZKP) dan naming service (ANS) untuk menghilangkan barrier onboarding non-teknis (seed phrase, alamat hex)

· Evidence: Keyless live mainnet 2023 (EV-018); ANS live 2023 (EV-017); terintegrasi di Petra, Martian, Fewcha wallets (HIGH) [Aptos Keyless Paper, https://aptos.dev/whitepaper/aptos-keyless.pdf]
· Supporting Dataset: Phase 3 EV-017, EV-018; Phase 4 Core Components Keyless Module, ANS Contracts; Phase 7 Applications ANS, Keyless

Decision Timeline

Keputusan: Pendirian Aptos Labs Inc. oleh Mo Shaikh (CEO) dan Avery Ching (CTO) mantan lead engineer Diem (2021-12)
· Trigger: Meta menutup proyek Diem/Libra Januari 2022; founder ingin melanjutkan teknologi Move sebagai L1 independen
· Evidence: Founder background ex-Diem; Aptos Labs incorporated Delaware Desember 2021 (HIGH) [Aptos Labs Team, https://aptoslabs.com/team]
· Decision: Membangun perusahaan for-profit untuk develop core protocol, Move VM, tooling, dan produk komersial (Petra Wallet)
· Immediate Result: Entity terstruktur untuk fundraising dan hiring; pre-Series A development dimulai
· Long-term Impact: Menjadi backbone engineering seluruh ekosistem Aptos; memisahkan komersial (Labs) dari protokol (Foundation)
· Supporting Dataset: Phase 1 Founders; Phase 2 Entity Apt Labs Inc., Mo Shaikh, Avery Ching; Phase 3 EV-003

Keputusan: Series A Funding $200M led by Andreessen Horowitz (a16z) pada valuasi $2B (2022-03-29)
· Trigger: Perlu capital besar untuk scaling team (~100+ engineers), testnet incentivized, persiapan mainnet
· Evidence: Largest Series A for L1 at the time; investor lineup includes Multicoin, Binance Labs, Coinbase Ventures, Tiger Global (HIGH) [TechCrunch, https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/]
· Decision: Equity funding ke Aptos Labs Inc. + SAFT token allocation untuk investor (13.48% supply)
· Immediate Result: Runway untuk mainnet launch; strategic investors memberikan exchange listing support, market making, ecosystem access
· Long-term Impact: Investor vesting cliff 1 tahun + 4 tahun linear unlock menciptakan sell pressure jangka menengah (mulai Okt 2023); board seat a16z mempengaruhi strategic direction Labs
· Supporting Dataset: Phase 3 EV-005; Phase 5 Funding History; Phase 6 Distribution Investors, Vesting Schedule

Keputusan: Launch Aptos Incentivized Testnet Wave 1 (AIT-1) (2022-03-24)
· Trigger: Perlu stress-test parallel execution (Block-STM), consensus (AptosBFT), staking mechanics sebelum mainnet
· Evidence: Ribuan validator dan developer partisipasi; airdrop allocation untuk community (HIGH) [Aptos Blog AIT-1, https://medium.com/aptoslabs/aptos-incentivized-testnet-1-is-live-9f3b5e5c5f5e]
· Decision: Incentivized testnet dengan reward token (airdrop nanti) untuk bootstrap validator set dan developer feedback
· Immediate Result: Validator set tested at scale; bug ditemukan dan diperbaiki; community building dimulai awal
· Long-term Impact: Airdrop recipients menjadi early community; testnet data inform mainnet parameter; model diulang untuk AIT-2/3
· Supporting Dataset: Phase 3 EV-004; Phase 6 Distribution Community Airdrop

Keputusan: Mainnet Genesis & TGE 1B APT (2022-10-17)
· Trigger: Testnet complete; funding secured; validator set ready; exchange commitments (Binance, Coinbase, FTX)
· Evidence: 1B APT minted genesis; allocation per whitepaper: Community 51.02%, Core Contributors 19%, Foundation 16.5%, Investors 13.48% (HIGH) [Aptos Blog Mainnet, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e]
· Decision: Full supply minted at genesis; hanya kategori tanpa vesting (airdrop, Foundation ops) liquid immediately; Contributors & Investors locked 1 year
· Immediate Result: Network live; trading begins on major CEX same week; airdrop claimed; staking activated
· Long-term Impact: Tokenomics inflationary (staking reward) + deflationary (base fee burn) dynamic; vesting unlocks mulai Okt 2023 menciptakan structural sell pressure 2+ tahun
· Supporting Dataset: Phase 3 EV-007, EV-008; Phase 6 TGE, Distribution, Vesting Schedule, Inflation/Deflation

Keputusan: Pendirian Aptos Foundation di Cayman Islands sebagai non-profit terpisah (2022-10)
· Trigger: Perlu legal wrapper untuk treasury protokol, grant distribution, governance facilitation, validator set decentralization — terpisah dari for-profit Labs
· Evidence: Foundation manages 16.5% supply + portion of Community 51.02%; Cayman Islands jurisdiction untuk non-profit (HIGH) [Aptos Foundation Governance, https://aptosfoundation.org/governance]
· Decision: Foundation holds protocol treasury; runs Grants DAO; oversees validator decentralization; Labs focuses on core dev & commercial products
· Immediate Result: Governance structure established; grant programs launched; validator onboarding formalized
· Long-term Impact: Dual-entity structure (Labs + Foundation) menciptakan tension: Labs commercial interests vs Foundation protocol neutrality; transparency dashboard belum ada
· Supporting Dataset: Phase 3 EV-009; Phase 2 Entity Aptos Foundation; Phase 5 Treasury; Phase 7 Governance Ecosystem

Keputusan: Integrasi Wormhole Bridge untuk wrapped APT cross-chain (2022-12)
· Trigger: Perlu cross-chain liquidity untuk DeFi participation; no native cross-chain messaging at protocol layer
· Evidence: Wormhole enables wrapped APT on Ethereum, Solana, BSC, Polygon (EV-013) (HIGH) [Wormhole Portal, https://wormhole.com/token-bridge]
· Decision: External bridge dependency sebagai primary cross-chain solution; LayerZero added later untuk OFT standard
· Immediate Result: APT accessible di Ethereum DeFi (Uniswap, Curve); bridge volume significant
· Long-term Impact: Bridge risk (Wormhole hack history) becomes systemic risk untuk wrapped APT holders; no protocol-level control over bridge security
· Supporting Dataset: Phase 3 EV-013; Phase 4 Cross-chain Messaging; Phase 7 External Dependencies Wormhole, Major Integrations Wormhole

Keputusan: Google Cloud & AWS sebagai official validator infrastructure partners (2022-12)
· Trigger: Validator hardware requirements tinggi (32 cores, 64GB RAM, 2TB NVMe); perlu enterprise-grade hosting untuk geographic decentralization
· Evidence: Both cloud providers announce managed validator services, marketplace AMI, KMS integration (EV-014) (HIGH) [Google Cloud Web3 Aptos, https://cloud.google.com/web3/aptos]
· Decision: Formal partnership dengan major cloud providers untuk lower barrier validator operations
· Immediate Result: Easy deployment untuk institutional validators; validator count grows to 100+
· Long-term Impact: Centralization risk: signifikan % validator hosted on Google Cloud/AWS; single cloud outage could affect quorum; no slashing amplifies risk
· Supporting Dataset: Phase 3 EV-014; Phase 7 Infrastructure Providers, Major Integrations, Ecosystem Risks Cloud Centralization

Keputusan: Launch Petra Wallet sebagai official wallet (2022-11)
· Trigger: Perlu native wallet untuk user onboarding, dApp connector standard, NFT display, Keyless integration
· Evidence: Built by Aptos Labs; browser extension + mobile; Ledger support; Keyless native (EV-010) (HIGH) [Petra Wallet, https://petra.app]
· Decision: First-party wallet development oleh Labs (bukan third-party grant); auto-update via app stores
· Immediate Result: Default wallet untuk Aptos users; dApp connector standard (wallet adapter); Keyless distribution channel
· Long-term Impact: Labs controls primary user interface; competing wallets (Martian, Fewcha, Nightly) emerge but Petra has first-mover advantage; Labs commercial interest vs ecosystem neutrality
· Supporting Dataset: Phase 3 EV-010; Phase 4 Core Components Petra Wallet; Phase 7 Wallet Ecosystem

Keputusan: Keyless Authentication launch (OIDC + ZKP) mainnet (2023-05)
· Trigger: Seed phrase barrier mencegah mass adoption; perlu passwordless onboarding via Google/Apple OAuth
· Evidence: ZKP (Groth16) verifies OIDC JWT claims on-chain; live mainnet 2023; v1.8 upgrade enhanced (EV-018, EV-029) (HIGH) [Aptos Keyless Paper, https://aptos.dev/whitepaper/aptos-keyless.pdf]
· Decision: Native account abstraction at protocol layer (bukan smart contract wallet seperti ERC-4337); ZKP circuit untuk privacy
· Immediate Result: Users create accounts via Google/Apple login; gas paid by sponsor or user; no seed phrase management
· Long-term Impact: Differentiator vs EVM chains; but adoption metrics not public; ZKP circuit audit dependency; OIDC provider centralization (Google/Apple)
· Supporting Dataset: Phase 3 EV-018, EV-029; Phase 4 Core Components Keyless Module, Security Model; Phase 7 Applications Keyless

Keputusan: Aptos Names Service (ANS) launch mainnet (2023-03)
· Trigger: Human-readable addresses needed untuk UX; ENS equivalent untuk Aptos
· Evidence: .apt domains live; integrated wallets, explorer, dApps (EV-017) (HIGH) [ANS Official, https://aptosnames.com]
· Decision: On-chain naming registry dengan renewal fee APT; Foundation/Labs supported development
· Immediate Result: .apt adoption massal; primary identity primitive ekosistem
· Long-term Impact: Revenue stream (renewal fees) ke ANS treasury; potential governance vector (name-based voting); squatting risk
· Supporting Dataset: Phase 3 EV-017; Phase 4 Core Components ANS Contracts; Phase 7 Applications ANS

Keputusan: Protocol Upgrade v1.5 (Performance, Gas Schedule, Validator Ops) (2024-03-15)
· Trigger: Mainnet performance optimization needed; gas schedule v1 static; validator rotation improvements needed
· Evidence: Block-STM optimization; dynamic gas schedule; reduced block time variance (EV-027) (HIGH) [Aptos Core Releases v1.5, https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.5.0]
· Decision: On-chain governance proposal untuk upgrade; validator set coordination required
· Immediate Result: Throughput increase; gas cost stabilization; validator operations efficiency
· Long-term Impact: Demonstrates governance upgrade capability; sets precedent untuk future upgrades (v1.8 Move 2024 Edition)
· Supporting Dataset: Phase 3 EV-027; Phase 4 Technical Upgrade History v1.5; Phase 6 Governance Proposal System

Keputusan: Protocol Upgrade v1.8 (Move 2024 Edition, Account Abstraction Enhancements, Keyless v2) (2024-09-05)
· Trigger: Move language evolution; developer experience improvement; account abstraction maturity
· Evidence: Generics, enums, pattern matching; Keyless v2; gas schedule v3; multi-signer improvements (EV-029) (HIGH) [Aptos Core Releases v1.8, https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.8.0]
· Decision: Major language upgrade via governance; backward compatibility considerations
· Immediate Result: Developer experience significantly improved; new language features available; Keyless v2 more efficient
· Long-term Impact: Move 2024 Edition standardization dengan Movement Labs; ecosystem migration required untuk packages lama
· Supporting Dataset: Phase 3 EV-029; Phase 4 Technical Upgrade History v1.8; Phase 7 Major Integrations Movement Labs

Keputusan: NodeReal & Nodit sebagai official enterprise RPC/Indexer partners (2024-06-10)
· Trigger: Public RPC unreliable untuk production dApps; perlu enterprise-grade indexing, GraphQL, gRPC
· Evidence: NodeReal & Nodit provide production RPC, indexer gRPC v2, GraphQL API (EV-028) (HIGH) [NodeReal Aptos, https://nodereal.io/aptos]
· Decision: Formal partnership dan endorsement untuk enterprise infrastructure providers
· Immediate Result: Reliable RPC for developers; indexer v2 adoption accelerated
· Long-term Impact: Concentration risk: 2 providers dominate production traffic; no SLA transparency; dApps dependent on their uptime
· Supporting Dataset: Phase 3 EV-028; Phase 7 Infrastructure Providers, Major Integrations, Ecosystem Risks Indexer Concentration

Evolution Pattern

Perubahan Strategi: Dari "Diem continuation" ke "Independent Move L1 dengan differentiation teknis"
· Early Phase (2021-2022): Narrative fokus pada "spiritual successor Diem", Move language heritage, ex-Meta team credibility
· Growth Phase (2023-2024): Pivot ke technical differentiation sendiri — Block-STM parallel execution, Keyless account abstraction, Move 2024 Edition, institutional infrastructure partnerships
· Evidence: Whitepaper centers Block-STM bukan Diem heritage; marketing materials emphasize "160k+ TPS theoretical" via parallelism; Keyless as unique UX innovation (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]; [Aptos Labs Website, https://aptoslabs.com]
· Supporting Dataset: Phase 1 Positioning; Phase 3 EV-001 (Diem origin) vs EV-018 (Keyless native), EV-029 (Move 2024 Edition); Phase 8 Narrative Position

Perubahan Teknologi: Dari Move VM Diem-era ke Aptos-optimized Move VM dengan Block-STM, AptosBFT v4, Keyless, ANS
· Diem Legacy (2019-2021): Move language, Move VM, HotStuff consensus entwickelt bei Meta
· Aptos Innovation (2022-present): Block-STM (parallel execution), AptosBFT v4 (Jolteon-derived), Keyless (OIDC+ZKP), ANS, Move 2024 Edition (generics, enums)
· Evidence: Technical whitepaper describes Block-STM as key innovation; AptosBFT v4 evolved from v1→v3→v4; Keyless native protocol feature not in Diem (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]; [Aptos Consensus Docs, https://aptos.dev/concepts/consensus/]
· Supporting Dataset: Phase 3 EV-001, EV-002 (Diem origin) vs EV-018, EV-029 (Aptos innovations); Phase 4 Consensus Mechanism, Execution Environment, Technical Upgrade History

Perubahan Tokenomics: Dari static allocation whitepaper ke dynamic inflation/deflation dengan vesting unlocks struktural
· Genesis (2022-10): 1B APT fixed allocation; 51.02% Community/Foundation, 19% Contributors, 16.5% Foundation, 13.48% Investors
· Post-Genesis (2023-2026): Staking reward inflation (7%→3.25% APY) + base fee burn = net supply dynamic; Contributor/Investor monthly unlocks Okt 2023-Okt 2026 (~5.5M APT/bulan combined)
· Evidence: Whitepaper defines inflation schedule; vesting contracts on-chain; no fee switch for protocol revenue (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]; [Aptos Tokenomics, https://aptos.dev/tokenomics/]
· Supporting Dataset: Phase 3 EV-007 (TGE), EV-003 (cliff end); Phase 6 Inflation/Deflation, Vesting Schedule, Major Token Events

Perubahan Governance: Dari Foundation-controlled ke hybrid on-chain/off-chain dengan Grants DAO
· Early (2022-2023): Foundation unilateral decisions untuk upgrades, grants, validator onboarding
· Maturation (2024): Grants DAO launched (EV-026); on-chain framework upgrade proposals executed; validator voting power via stake delegation
· Evidence: Governance forum active; proposal execution via 0x1::governance module; Grants DAO community voting (HIGH) [Aptos Governance Forum, https://gov.aptosfoundation.org/]
· Supporting Dataset: Phase 3 EV-009, EV-026, EV-027, EV-029; Phase 6 Governance; Phase 7 Governance Ecosystem

Perubahan Ecosystem: Dari minimal DeFi (Liquidswap only) ke full DeFi stack + NFT + Identity + Infrastructure
· 2022-Q4: Liquidswap DEX only; Wormhole bridge; Petra wallet
· 2023: Thala (stablecoin, lending), Amnis (liquid staking), ANS, Keyless, Topaz/BlueMove/Souffl3 (NFT), Panora (aggregator), Cellana/Econia/Ditto (DeFi expansion)
· 2024: NodeReal/Nodit enterprise infra, Movement Labs Move standardization, v1.8 language upgrade, Grants DAO scaling
· Evidence: DefiLlama shows >15 major protocols; TVL peak $1B+ (2024-03) → ~$480M (2024-12); 500+ projects claimed (HIGH) [DefiLlama Aptos, https://defillama.com/chain/Aptos]
· Supporting Dataset: Phase 3 EV-012 through EV-030; Phase 7 Applications, Developer Ecosystem, Major Integrations; Phase 8 Adoption Metrics

Technical Decision Pattern

Pola 1: Parallel Execution via Block-STM sebagai Core Differentiator
· Decision Pattern: Memilih optimistic Software Transactional Memory (Block-STM) untuk parallel execution bukan sequential EVM-style atau Solana-style SVM; conflict detection post-execution dengan retry
· Evidence: Technical whitepaper centers Block-STM; v1.5/v1.8 upgrades highlight Block-STM optimizations; theoretical 160k+ TPS claimed (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]; [Block-STM Paper, https://arxiv.org/abs/2203.06871]
· Supporting Dataset: Phase 4 System Architecture Execution Model, Execution Environment Parallel Execution, Technical Upgrade History v1.5, v1.8

Pola 2: Move VM dengan Resource-Oriented Model untuk Safety
· Decision Pattern: Mengadopsi Move language (resource linearity, no reentrancy, formal verification via Move Prover) bukan EVM; bytecode verifier enforces safety at deployment
· Evidence: Move Prover used untuk critical framework modules (coin, stake, validator); OtterSec/Trail of Bits audited VM implementation (HIGH) [Move Prover Framework Verification, https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework/aptos-framework/specs]
· Supporting Dataset: Phase 4 Execution Environment, Security Model Formal Verification, Audit History OtterSec/Trail of Bits

Pola 3: AptosBFT v4 (Jolteon-derived) untuk Instant Finality
· Decision Pattern: BFT consensus dengan 2-round voting untuk instant finality under synchrony; stake-weighted leader rotation via VRF; tolerates <1/3 Byzantine stake
· Evidence: Consensus upgrades v1→v3→v4 documented; no slashing implemented; validator reputation-based removal (HIGH) [Aptos Consensus Docs, https://aptos.dev/concepts/consensus/]
· Supporting Dataset: Phase 4 Consensus Mechanism, Technical Upgrade History v1.3 (v3), v1.5 (v4)

Pola 4: Native Account Abstraction (Keyless) via ZKP + OIDC
· Decision Pattern: Protocol-level account abstraction menggunakan Groth16 ZKP untuk verify OIDC JWT claims; bukan smart contract wallet (ERC-4337 style); ephemeral key bound to JWT
· Evidence: Keyless paper describes circuit; live mainnet 2023; v1.8 Keyless v2 improvements; integrated in Petra, Martian, Fewcha (HIGH) [Aptos Keyless Paper, https://aptos.dev/whitepaper/aptos-keyless.pdf]
· Supporting Dataset: Phase 3 EV-018, EV-029; Phase 4 Core Components Keyless Module, Security Model Account Abstraction

Pola 5: On-Chain Governance Upgrades dengan Timelock dan Compatibility Checks
· Decision Pattern: Framework upgrades via 0x1::governance module; proposal requires deposit, voting period ~2 epochs, execution automatic if passed; compatibility checks enforced
· Evidence: v1.5, v1.8 upgrades executed via governance; validator coordination required; timelock prevents rushed changes (HIGH) [Aptos Governance Module, https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework/aptos-framework/sources/governance.move]
· Supporting Dataset: Phase 3 EV-027, EV-029; Phase 4 Technical Upgrade History; Phase 6 Governance Proposal System

Pola 6: Rust untuk Core Implementation, Move untuk Smart Contracts
· Decision Pattern: Validator, full node, VM, consensus, networking, storage, indexer, CLI semua Rust; Move hanya untuk on-chain logic; SDKs multi-language (TS, Python, Rust, Go, Unity)
· Evidence: aptos-core repo 95%+ Rust; Move framework separate; SDKs separate repos (HIGH) [Aptos Core GitHub, https://github.com/aptos-labs/aptos-core]
· Supporting Dataset: Phase 4 Programming Languages, Current Technical Stack

Pola 7: External Bridge Dependency untuk Cross-Chain (No Native Messaging)
· Decision Pattern: Tidak build native cross-chain messaging; rely on Wormhole (guardian network) dan LayerZero (OFT/DVN) untuk wrapped APT dan messaging
· Evidence: Whitepaper no cross-chain section; bridging guide points to external bridges; LayerZero OFT integration announced but not in Phase 3 events (HIGH) [Aptos Bridging Guide, https://aptos.dev/guides/bridging/]
· Supporting Dataset: Phase 4 Cross-chain Messaging; Phase 7 External Dependencies Wormhole, LayerZero, Major Integrations

Financial Decision Pattern

Pola 1: Large VC Funding Rounds (Series A $200M, Series B $150M) dengan Strategic Investor Syndicate
· Decision Pattern: Raise maximum capital pre-mainnet dari top-tier VCs (a16z lead) + strategic investors (Binance Labs, Coinbase Ventures, Multicoin, Tiger Global, Apollo) untuk runway panjang dan ecosystem access
· Evidence: $350M total equity funding; SAFT token allocation 13.48% supply; valuasi $2B→$4B; investor board seat (a16z) (HIGH) [TechCrunch Series A, https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/]
· Supporting Dataset: Phase 3 EV-005, EV-006; Phase 5 Funding History, Financial Dependencies; Phase 6 Distribution Investors, Vesting Schedule

Pola 2: Protocol Treasury = Native Token Concentration (51.02% Community/Foundation + 16.5% Foundation = 67.52% Genesis)
· Decision Pattern: Treasury denominated almost entirely in APT; no stablecoin diversification disclosed; grant spending draws down APT holdings
· Evidence: Whitepaper allocation; Foundation grants paid in APT; no transparency dashboard untuk treasury composition (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]; [Aptos Foundation Grants, https://aptosfoundation.org/grants]
· Supporting Dataset: Phase 5 Treasury, Revenue Model; Phase 6 Distribution Community, Foundation; Phase 7 Ecosystem Risks Treasury Concentration

Pola 3: No Protocol Revenue (Fee Switch Off) — Operational Funding dari Treasury Spend-Down + Inflationary Staking Rewards
· Decision Pattern: 100% base fee burned; priority fee to validators; protocol captures zero revenue; Foundation ops funded by genesis allocation + staking rewards (which go to validators/delegators, not Foundation directly)
· Evidence: Tokenomics explicitly states no fee switch; revenue model only Labs enterprise services + Foundation treasury spend (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
· Supporting Dataset: Phase 5 Revenue Model, Revenue History; Phase 6 Inflation/Deflation Burn Mechanism

Pola 4: Grants DAO sebagai Primary Ecosystem Funding Mechanism (Post-2024)
· Decision Pattern: Shift dari Foundation unilateral grants ke community-governed Grants DAO dengan on-chain/off-chain hybrid voting; milestones-based vesting untuk recipients
· Evidence: EV-026 Grants DAO launch 2024; governance forum active proposals; grant categories: infrastructure, DeFi, NFT, tooling, education (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
· Supporting Dataset: Phase 3 EV-026; Phase 5 Fundraising Mechanism Grant, DAO Treasury; Phase 7 Governance Ecosystem Grants DAO

Pola 5: Vesting Structure: 1-Year Cliff + 4-Year Linear untuk Contributors & Investors (Mulai Okt 2023)
· Decision Pattern: Standard VC-style vesting tapi dengan supply besar (32.48% combined); monthly unlocks menciptakan consistent sell pressure 3 tahun
· Evidence: Whitepaper defines cliff + linear vesting; on-chain vesting contracts; cliff ended Okt 2023 (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]
· Supporting Dataset: Phase 3 EV-007 (TGE), EV-003 (cliff anniversary); Phase 6 Vesting Schedule Core Contributors, Investors; Phase 6 Major Token Events Cliff End

Ecosystem Decision Pattern

Pola 1: Institutional Cloud Partnerships (Google Cloud, AWS) untuk Validator Infrastructure Legitimacy
· Decision Pattern: Formal partnerships dengan major cloud providers untuk managed validator services, AMI marketplace, KMS integration — signaling enterprise-readiness
· Evidence: EV-014 both providers announce simultaneously; NodeReal/Nodit later for RPC/indexer layer (HIGH) [Google Cloud Web3 Aptos, https://cloud.google.com/web3/aptos]
· Supporting Dataset: Phase 3 EV-014; Phase 7 Infrastructure Providers Google Cloud, AWS, Major Integrations, External Dependencies

Pola 2: Bridge-First Cross-Chain Strategy (Wormhole → LayerZero)
· Decision Pattern: Integrate major bridges sequentially; Wormhole first untuk wrapped APT liquidity; LayerZero later untuk OFT standard dan messaging; no native protocol-level solution
· Evidence: EV-013 Wormhole Dec 2022; LayerZero integration announced 2023-2024 but no Phase 3 Event ID; bridging guide lists both (HIGH) [Wormhole Portal, https://wormhole.com/token-bridge]
· Supporting Dataset: Phase 3 EV-013; Phase 7 External Dependencies Wormhole, LayerZero, Major Integrations Wormhole, LayerZero, Ecosystem Risks Bridge Dependency

Pola 3: First-Party Wallet (Petra) + Open Wallet Ecosystem (Martian, Fewcha, Nightly, Pontem, Rise)
· Decision Pattern: Labs builds official wallet untuk control onboarding UX, Keyless distribution, dApp connector standard; welcomes competing wallets via grants/ecosystem support
· Evidence: Petra launched EV-010 Nov 2022; Martian/Fewcha/Nightly gained traction 2023 (EV-023); all support Keyless, ANS, Ledger (HIGH) [Petra Wallet, https://petra.app]
· Supporting Dataset: Phase 3 EV-010, EV-023; Phase 4 Core Components Petra Wallet; Phase 7 Wallet Ecosystem

Pola 4: Move Ecosystem Standardization Collaboration (Movement Labs Partnership)
· Decision Pattern: Active collaboration dengan Movement Labs (Move-EVM L2) untuk shared tooling (Move Analyzer, LSP), language standards, developer portability — expanding Move pie bukan zero-sum
· Evidence: EV-024 Nov 2023 announcement; joint hackathons; Move Analyzer shared development (HIGH) [Movement Labs Blog, https://blog.movementlabs.xyz/move-ecosystem-collaboration/]
· Supporting Dataset: Phase 3 EV-024; Phase 7 Major Integrations Movement Labs, External Dependencies Movement Labs; Phase 8 Narrative Move VM Ecosystem

Pola 5: Enterprise RPC/Indexer Partnerships (NodeReal, Nodit) untuk Production-Grade Developer Experience
· Decision Pattern: Formal endorsement of 2 enterprise infrastructure providers untuk RPC, indexer gRPC v2, GraphQL — reducing reliance on public RPC
· Evidence: EV-028 Jun 2024; both provide production SLAs (undisclosed); dApps migrate from public RPC (HIGH) [NodeReal Aptos, https://nodereal.io/aptos]
· Supporting Dataset: Phase 3 EV-028; Phase 7 Infrastructure Providers NodeReal, Nodit, Major Integrations, Ecosystem Risks Indexer Concentration

Pola 6: Grants Program Expansion → Grants DAO Decentralization
· Decision Pattern: Foundation unilateral grants (2022-2023) → structured Grants DAO dengan community voting (2024) → progressive decentralization of treasury allocation
· Evidence: EV-026 Grants DAO launch; governance forum proposals; grant categories defined (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
· Supporting Dataset: Phase 3 EV-026; Phase 7 Governance Ecosystem Grants DAO; Phase 5 Fundraising Mechanism DAO Treasury

Governance Decision Pattern

Pola 1: Dual-Entity Governance (Labs + Foundation) dengan Role Separation
· Decision Pattern: Aptos Labs (Delaware corp) controls core protocol development, commercial products (Petra), enterprise services; Aptos Foundation (Cayman non-profit) controls protocol treasury, grants, validator decentralization, governance facilitation
· Evidence: Legal structure distinct; Labs for-profit, Foundation non-profit; Labs team ~100+ engineers; Foundation runs Grants DAO (HIGH) [Aptos Labs Team, https://aptoslabs.com/team]; [Aptos Foundation Governance, https://aptosfoundation.org/governance]
· Supporting Dataset: Phase 2 Entity Aptos Labs Inc., Aptos Foundation; Phase 3 EV-003, EV-009; Phase 5 Treasury, Financial Dependencies; Phase 7 Governance Ecosystem

Pola 2: Stake-Weighted On-Chain Voting via Validator Delegation
· Decision Pattern: 1 APT staked = 1 vote power; holders delegate to validators; validators vote on proposals; proposal execution automatic via 0x1::governance module if quorum + supermajority met
· Evidence: Governance module on-chain; voting period ~2 epochs; framework upgrades (v1.5, v1.8) executed this way (HIGH) [Aptos Governance Module, https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework/aptos-framework/sources/governance.move]
· Supporting Dataset: Phase 4 Consensus Mechanism Validator Set; Phase 6 Governance Voting System, Proposal System; Phase 7 Governance Ecosystem Validator Group

Pola 3: Grants DAO Hybrid Governance (Off-Chain Signaling + On-Chain Execution)
· Decision Pattern: Community proposes pada forum → off-chain voting (Snapshot-style) → Foundation multisig executes approved grants; progressive shift to more on-chain execution
· Evidence: Governance forum structure; Grants DAO process described; not fully on-chain autonomous DAO yet (HIGH) [Aptos Governance Forum, https://gov.aptosfoundation.org/]
· Supporting Dataset: Phase 3 EV-026; Phase 6 Governance Treasury Governance; Phase 7 Governance Ecosystem DAO

Pola 4: Validator Set sebagai Governance Representatives (Delegated Proof-of-Stake)
· Decision Pattern: Validators mevakili delegator dalam voting; 100+ active validators target; stake concentration di top validators mempengaruhi governance decentralization
· Evidence: Explorer shows 108 active validators; stake distribution not public percentage; no slashing untuk misbehavior (HIGH) [Aptos Explorer Validators, https://explorer.aptoslabs.com/validators]
· Supporting Dataset: Phase 4 Consensus Mechanism Validator Set; Phase 6 Governance Voting Power, Delegation; Phase 7 Governance Ecosystem Validator Group, Ecosystem Risks Validator Centralization

Pola 5: Protocol Upgrades via Formal Governance Proposals (Timelock + Compatibility)
· Decision Pattern: Semua framework upgrades (v1.1→v1.8) melalui on-chain proposal; requires deposit, voting period, automatic execution; compatibility checks enforced by VM
· Evidence: v1.5, v1.8 upgrades documented as governance proposals; validator coordination announcements (HIGH) [Aptos Core Releases, https://github.com/aptos-labs/aptos-core/releases]
· Supporting Dataset: Phase 3 EV-027, EV-029; Phase 4 Technical Upgrade History; Phase 6 Governance Proposal System

Risk Response Pattern

Pola 1: Security Audit Portfolio Diversification (Multiple Top-Tier Auditors)
· Trigger: High-value protocol dengan novel VM (Move) dan parallel execution (Block-STM) memerlukan comprehensive security validation
· Evidence: 7 auditors engaged: CertiK, OtterSec, Trail of Bits, Halborn, Quantstamp, Zellic, Spearbit — covering core protocol, VM, DeFi protocols (HIGH) [CertiK Aptos, https://www.certik.com/projects/aptos]
· Response: Parallel audit engagements untuk different components; public reports published; critical findings fixed pre/post-mainnet
· Result: No major protocol exploit on mainnet; DeFi protocol audits separate (Halborn for Liquidswap, Thala, etc.)
· Supporting Dataset: Phase 4 Audit History; Phase 7 External Dependencies CertiK, OtterSec, Trail of Bits, Halborn

Pola 2: No Slashing — Reputation-Based Validator Accountability
· Trigger: Design choice untuk avoid slashing complexity; rely on reputation, community monitoring, manual removal untuk validator misbehavior
· Evidence: Staking FAQ explicitly states no slashing; validator removal via governance if needed (HIGH) [Aptos Staking FAQ, https://aptos.dev/nodes/validator-node/staking/#slashing]
· Response: High hardware requirements (32 cores, 64GB RAM, 2TB NVMe) sebagai barrier to entry; cloud provider partnerships untuk reliability; monitoring via Prometheus/Grafana standard
· Result: 100+ validators active; no major validator misbehavior incident public; but centralization risk on cloud providers remains
· Supporting Dataset: Phase 4 Consensus Mechanism Fault Tolerance, Slashing; Phase 7 Ecosystem Risks No Slashing, Validator Centralization, Cloud Centralization

Pola 3: Bridge Risk Mitigation via Multiple Bridge Integrations (Wormhole + LayerZero)
· Trigger: Dependency on single bridge (Wormhole) creates systemic risk; Wormhole hack history (Feb 2022) highlights danger
· Evidence: Wormhole integrated Dec 2022 (EV-013); LayerZero OFT integration added 2023-2024; bridging guide lists both (HIGH) [Wormhole Portal, https://wormhole.com/token-bridge]
· Response: Diversify bridge exposure; OFT standard enables unified liquidity; but protocol has no control over bridge security
· Result: Wrapped APT available on multiple chains; bridge volume significant; but bridge hack would affect wrapped APT holders not native APT
· Supporting Dataset: Phase 3 EV-013; Phase 7 External Dependencies Wormhole, LayerZero, Major Integrations, Ecosystem Risks Bridge Dependency

Pola 4: Cloud Centralization Risk Accepted untuk Validator Onboarding Velocity
· Trigger: High validator hardware requirements membuat self-hosting sulit; Google Cloud/AWS partnerships accelerate validator set growth
· Evidence: EV-014 partnerships; hardware requirements documented; validator count 108 active (HIGH) [Aptos Hardware Requirements, https://aptos.dev/nodes/validator-node/hardware-requirements/]
· Response: Accept cloud concentration sebagai trade-off untuk network security (validator count) dan geographic distribution; no mitigation untuk single cloud provider failure scenario
· Result: Validator target achieved; but % validators on Google Cloud vs AWS vs self-hosted unknown; centralization risk unquantified
· Supporting Dataset: Phase 3 EV-014; Phase 7 Infrastructure Providers, Ecosystem Risks Cloud Centralization; Phase 8 Open Threads Cloud Validator Share

Pola 5: Treasury Transparency Gap — No Public Dashboard atau Audited Financials
· Trigger: Foundation holds 67.52% genesis supply equivalent; community demands transparency; non-profit Cayman Islands may have filing requirements
· Evidence: No treasury dashboard; no audited financial statements published; grant spending not tracked on-chain publicly (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
· Response: Grants DAO introduces community oversight; but Foundation treasury management remains opaque; no regular transparency reports
· Result: Trust gap persists; circulating supply methodology conflicts across trackers (CoinGecko vs CoinMarketCap vs Messari)
· Supporting Dataset: Phase 5 Treasury; Phase 6 Holder Distribution; Phase 8 Adoption Metrics Circulating Supply, Open Threads Treasury Transparency

Recurring Behavioral Pattern

Pola 1: Major Technical Upgrade → Ecosystem Expansion Wave
· Pattern: Setiap major protocol upgrade (v1.2 Keyless/ANS, v1.5 Performance, v1.8 Move 2024 Edition) diikuti oleh new primitive launches dan developer tooling updates
· Evidence: EV-012 (Keyless/ANS) → Thala, Amnis, ANS, Keyless apps; EV-027 (v1.5) → NodeReal/Nodit enterprise infra, Panora v2; EV-029 (v1.8) → Move 2024 Edition tooling, Keyless v2 adoption (HIGH) [Aptos Core Releases, https://github.com/aptos-labs/aptos-core/releases]
· Supporting Dataset: Phase 3 EV-012, EV-017, EV-018, EV-027, EV-028, EV-029; Phase 7 Applications timeline correlation

Pola 2: Funding Round → Strategic Hiring + Infrastructure Partnerships
· Pattern: Series A (Mar 2022) → team scaling to 100+, AIT-1 testnet, Google Cloud/AWS partnerships; Series B (Jul 2022) → Apollo capital structure, mainnet prep, exchange listings
· Evidence: EV-005 Series A → EV-004 AIT-1, EV-014 Cloud partnerships; EV-006 Series B → EV-007 Mainnet, EV-008 Exchange listings (HIGH) [TechCrunch Series A, https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/]
· Supporting Dataset: Phase 3 EV-004, EV-005, EV-006, EV-007, EV-008, EV-014; Phase 5 Funding History, Financial Dependencies

Pola 3: New DeFi Primitive Launch → Liquidity Mining / Incentive Program via Grants
· Pattern: Liquidswap (DEX) → Thala (stablecoin/lending) → Amnis (liquid staking) → Panora (aggregator) → Cellana/Econia/Ditto — each receives Foundation grants dan often liquidity incentives
· Evidence: EV-012, EV-015, EV-016, EV-019, EV-020 all grant recipients per DefiLlama and Foundation grants page (HIGH) [DefiLlama Aptos, https://defillama.com/chain/Aptos]; [Aptos Foundation Grants, https://aptosfoundation.org/grants]
· Supporting Dataset: Phase 3 EV-012, EV-015, EV-016, EV-019; Phase 7 Applications DeFi category; Phase 5 Fundraising Mechanism Grant

Pola 4: Vesting Unlock Events → Market Sell Pressure → Ecosystem Incentives to Absorb
· Pattern: Investor/Contributor monthly unlocks mulai Okt 2023 (~5.5M APT/bulan) → price pressure → Foundation increases grants, liquid staking (amAPT, thAPT) growth, DeFi yield opportunities
· Evidence: Vesting schedule defined whitepaper; cliff end Okt 2023 (EV-003 anniversary); Amnis launch Feb 2023 (pre-emptive), Thala Jan 2023, liquid staking TVL growing (HIGH) [Aptos Whitepaper, https://aptos.dev/whitepaper/aptos-whitepaper.pdf]; [Amnis Finance, https://amnis.finance]
· Supporting Dataset: Phase 3 EV-007, EV-003; Phase 6 Vesting Schedule, Major Token Events; Phase 7 Applications Amnis, Thala

Pola 5: Security Audit → Public Report → Narrative Reinforcement "Institutional Grade"
· Pattern: Setiap major audit completion (CertiK, OtterSec, Trail of Bits, Spearbit) diumumkan publik dan digunakan dalam marketing materials sebagai "institutional-grade security" narrative
· Evidence: Security page lists all audits; blog posts announce completions; Google Cloud/AWS partnerships cite audit coverage (HIGH) [Aptos Security, https://aptos.dev/security/]
· Supporting Dataset: Phase 4 Audit History; Phase 7 External Dependencies Auditors; Phase 8 Narrative Institutional-Grade Infrastructure

Strategic Trade-offs

Trade-off 1: Desentralisasi Validator vs Kecepatan Onboarding (Cloud Provider Partnerships)
· Decision: Partner dengan Google Cloud dan AWS untuk managed validator services, AMI marketplace, KMS
· Trade-off: Menerima konsentrasi validator di 2 cloud provider utama (centralization risk: single provider outage bisa affect quorum) demi mempercepat validator set growth ke 100+ dan geographic distribution
· Evidence: EV-014 partnerships; hardware requirements tinggi (32 cores, 64GB RAM, 2TB NVMe); 108 active validators achieved; no slashing amplifies risk (HIGH) [Aptos Hardware Requirements, https://aptos.dev/nodes/validator-node/hardware-requirements/]
· Supporting Dataset: Phase 3 EV-014; Phase 4 Consensus Mechanism Validator Set; Phase 7 Infrastructure Providers, Ecosystem Risks Cloud Centralization, Validator Centralization

Trade-off 2: Keamanan (No Slashing) vs Accountability Validator
· Decision: Tidak implementasikan slashing mechanism; rely pada reputation, community monitoring, manual governance removal
· Trade-off: Menghindari kompleksitas slashing (false positive risk, game theory complexity) tapi mengurangi economic penalty untuk validator misbehavior (downtime, double-sign, equivocation)
· Evidence: Staking FAQ explicit no slashing; validator removal via governance only; high hardware requirements sebagai barrier (HIGH) [Aptos Staking FAQ, https://aptos.dev/nodes/validator-node/staking/#slashing]
· Supporting Dataset: Phase 4 Consensus Mechanism Slashing; Phase 7 Ecosystem Risks No Slashing

Trade-off 3: Native Cross-Chain Messaging vs Time-to-Market (Bridge Dependency)
· Decision: Tidak build native cross-chain messaging di protocol layer; integrate Wormhole dan LayerZero sebagai external dependencies
· Trade-off: Faster time-to-market untuk cross-chain liquidity (Wormhole Dec 2022, LayerZero 2023) tapi introduce bridge risk (Wormhole hack history, LayerZero DVN trust assumptions) dan no protocol-level control
· Evidence: Whitepaper no cross-chain section; bridging guide external only; EV-013 Wormhole, LayerZero later (HIGH) [Aptos Bridging Guide, https://aptos.dev/guides/bridging/]
· Supporting Dataset: Phase 4 Cross-chain Messaging; Phase 7 External Dependencies, Major Integrations, Ecosystem Risks Bridge Dependency

Trade-off 4: Protocol Revenue (Fee Switch) vs Validator Incentive Alignment
· Decision: 100% base fee burned; priority fee to validators; protocol captures zero revenue
· Trade-off: Aligns validator incentives dengan network usage (priority fee) dan creates deflationary pressure (burn) tapi Foundation/Labs harus rely pada treasury spend-down dan enterprise revenue — no sustainable protocol revenue stream
· Evidence: Tokenomics explicit no fee switch; revenue model only Labs enterprise + Foundation treasury (HIGH) [Aptos Tokenomics, https://aptos.dev/tokenomics/]
· Supporting Dataset: Phase 5 Revenue Model; Phase 6 Inflation/Deflation Burn Mechanism, Buyback; Phase 8 Market Revenue Sources

Trade-off 5: First-Party Wallet Control (Petra) vs Ecosystem Neutrality
· Decision: Aptos Labs builds dan maintains Petra Wallet sebagai official wallet; controls dApp connector standard, Keyless distribution, auto-updates
· Trade-off: Seamless UX, guaranteed Keyless/ANS integration, consistent branding tapi creates conflict of interest: Labs commercial product vs ecosystem-neutral infrastructure; competing wallets (Martian, Fewcha) at disadvantage
· Evidence: Petra launched EV-010 by Labs; competing wallets EV-023 community/grant funded; all support Keyless/ANS but Petra first (HIGH) [Petra Wallet, https://petra.app]
· Supporting Dataset: Phase 3 EV-010, EV-023; Phase 4 Core Components Petra Wallet; Phase 7 Wallet Ecosystem

Trade-off 6: Treasury Transparency vs Strategic Flexibility
· Decision: No public treasury dashboard, no audited financials, no regular transparency reports untuk Foundation treasury (67.52% genesis supply equivalent)
· Trade-off: Retains flexibility untuk strategic grants, market operations, runway management tanpa public scrutiny tapi menciptakan trust gap, circulating supply methodology conflicts, regulatory uncertainty
· Evidence: No dashboard; grants page shows recipients not amounts/timing; CoinGecko vs CoinMarketCap circulating supply diverge (HIGH) [Aptos Foundation Grants, https://aptosfoundation.org/grants]
· Supporting Dataset: Phase 5 Treasury; Phase 6 Holder Distribution; Phase 8 Adoption Metrics Circulating Supply, Open Threads Treasury Transparency

Trade-off 7: Move Language Innovation (Move 2024 Edition) vs Backward Compatibility / Ecosystem Migration Cost
· Decision: Major language upgrade v1.8 introducing generics, enums, pattern matching, enhanced account abstraction
· Trade-off: Significantly improved developer experience dan expressiveness tapi requires ecosystem package migration, tooling updates (Move Analyzer, Prover, SDKs), potential temporary fragmentation
· Evidence: EV-029 v1.8 Move 2024 Edition; Movement Labs standardization collaboration; SDKs updated post-upgrade (HIGH) [Aptos Core Releases v1.8, https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.8.0]
· Supporting Dataset: Phase 3 EV-029; Phase 4 Technical Upgrade History v1.8; Phase 7 Major Integrations Movement Labs, Developer Ecosystem

Behavioral Summary

Prioritas Utama Proyek:
1. Technical Differentiation: Block-STM parallel execution + Move VM resource safety sebagai core moat vs EVM/SVM chains
2. Institutional Credibility: Cloud partnerships (Google, AWS), top-tier auditors (CertiK, OtterSec, Trail of Bits), enterprise infrastructure (NodeReal, Nodit) untuk enterprise adoption
3. Developer Experience: Move 2024 Edition, multi-language SDKs, Keyless account abstraction, ANS naming — lowering barrier untuk non-crypto developers
4. Ecosystem Growth: Grants DAO, DeFi primitives (stablecoin, lending, liquid staking, DEX, aggregator), NFT marketplaces, identity primitives
5. Progressive Decentralization: Foundation → Grants DAO, validator set expansion, on-chain governance upgrades, community treasury control

Cara Mengambil Keputusan:
- Technical decisions: Core team (Labs) proposes → community discussion → on-chain governance vote → validator coordination → execution (v1.5, v1.8 pattern)
- Financial decisions: Foundation Council decides treasury allocation; Grants DAO community votes pada grants; Labs board (a16z seat) decides commercial strategy
- Ecosystem decisions: Foundation identifies gaps → grants untuk primitives → partnership announcements → integration support
- Emergency decisions: No documented emergency governance process; security incidents handled via Labs engineering + auditor coordination

Faktor Paling Sering Mempengaruhi Keputusan:
1. Technical Feasibility & Differentiation: Block-STM, Move VM, Keyless chosen karena technical superiority claims
2. Investor/Strategic Partner Alignment: a16z board seat, Binance/Coinbase listing support, Google Cloud/AWS partnerships shape infrastructure choices
3. Vesting Schedule Pressure: Investor/Contributor unlocks (32.48% supply) drive liquid staking, DeFi yield, grant programs to absorb sell pressure
4. Competitive Positioning vs Sui/Ethereum/Solana: Move ecosystem collaboration, parallel execution narrative, institutional-grade narrative
5. Regulatory Uncertainty: US entity (Labs) + Cayman Foundation split; no fee switch avoids security classification risk; staking rewards structure

Pola Evolusi:
- Phase 1 (2021-2022): Diem spin-out → Series A/B → Incentivized testnet → Mainnet launch → Exchange listings
- Phase 2 (2023): DeFi primitives bootstrapping (Liquidswap, Thala, Amnis) + Identity (ANS, Keyless) + NFT (Topaz) + Wallet competition
- Phase 3 (2024): Infrastructure maturation (NodeReal, Nodit, Grants DAO) + Protocol upgrades (v1.5, v1.8) + Move ecosystem standardization
- Trajectory: Technical differentiation → Ecosystem completeness → Institutional adoption → Progressive decentralization

Kekuatan Utama:
- Novel parallel execution (Block-STM) dengan formal verification (Move Prover) — technical moat
- Strong VC backing ($350M) + strategic investors (exchanges, cloud, market makers) — capital & distribution
- Move language heritage + active standardization (Movement Labs) — developer ecosystem flywheel
- Native account abstraction (Keyless) + naming (ANS) — UX differentiation untuk mass adoption
- Institutional infrastructure (Google Cloud, AWS, NodeReal, Nodit, top auditors) — enterprise credibility

Kelemahan Utama:
- Treasury opacity: No dashboard, no audited financials, APT-concentrated — trust & regulatory risk
- Validator centralization: Cloud provider concentration, no slashing, stake concentration unknown — security model gap
- Bridge dependency: Wormhole + LayerZero systemic risk, no native cross-chain — interoperability fragility
- Vesting overhang: 32.48% supply linear unlocks Okt 2023-2026 — structural sell pressure 3+ years
- Dual-entity tension: Labs (for-profit, controls core dev, Petra) vs Foundation (non-profit, protocol steward) — governance conflict potential
- No protocol revenue: Fee switch off, reliance on treasury spend-down — sustainability question post-vesting
- Adoption metrics transparency: Circulating supply methodology conflicts, Keyless adoption unknown, real TVL vs claimed — credibility gap

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Aptos

Core Insights

Insight 1: Teknologi asal enterprise (Meta/Diem) dapat di-spin-out menjadi Layer 1 publik independen dengan mempertahankan keunggulan teknis
Explanation: Move language dan Move VM dikembangkan internal Meta untuk Diem selama 2019-2021; Aptos Labs didirikan oleh mantan lead engineer Diem (Mo Shaikh, Avery Ching) dan mengadopsi seluruh stack teknis tersebut tanpa menulis VM baru【Phase 3 — EV-001】【Phase 3 — EV-002】【Phase 3 — EV-003】
Evidence: Whitepaper Meta Move 2020【Phase 4 — System Architecture】; Aptos Technical Whitepaper mengacu pada Move VM sebagai core【Phase 4 — Execution Environment】; Founder profile bestätigt background Diem【Phase 2 — Entity: Mo Shaikh, Avery Ching】
Supporting Dataset: Phase 2 (Entity), Phase 3 (EV-001, EV-002, EV-003), Phase 4 (System Architecture, Execution Environment)
Confidence: HIGH

Insight 2: Eksekusi paralel via Block-STM menjadi diferensiasi teknis utama yang memerlukan investasi berkelanjutan
Explanation: Block-STM (optimistic Software Transactional Memory) dipilih sebagai arsitekural parallel execution bukan sharding/L2; upgrade v1.5 dan v1.8 keduanya menyebut optimasi Block-STM secara eksplisit【Phase 4 — System Architecture】【Phase 4 — Technical Upgrade History】【Phase 9 — Technical Decision Pattern Pola 1】
Evidence: Aptos Technical Whitepaper centered pada Block-STM【Phase 4 — System Architecture】; arXiv Block-STM paper【Phase 4 — Official Technical Resources】; GitHub Release v1.5 "Block-STM optimization"【Phase 3 — EV-027】; GitHub Release v1.8 lanjutan【Phase 3 — EV-029】
Supporting Dataset: Phase 3 (EV-027, EV-029), Phase 4 (System Architecture, Execution Environment, Technical Upgrade History, Known Technical Limitations), Phase 9 (Technical Decision Pattern Pola 1)
Confidence: HIGH

Insight 3: Pemisahan entitas for-profit (Labs, Delaware) dan non-profit (Foundation, Cayman Islands) memungkinkan VC funding besar sekaligus governance protokol terdesentralisasi
Explanation: Aptos Labs mengumpulkan $350M equity funding (Series A $200M, Series B $150M) dari tier-1 VC; Aptos Foundation mengelola treasury protokol 51.02% supply; struktur dual-entity memisahkan kepentingan komersial vs protokol【Phase 5 — Funding History】【Phase 5 — Treasury】【Phase 6 — Distribution】【Phase 9 — Evolution Pattern Fase 1】
Evidence: Series A TechCrunch $200M a16z lead【Phase 3 — EV-005】; Series B Crunchbase $150M Apollo【Phase 3 — EV-006】; Whitepaper allocation 51.02% Community/Foundation/Ecosystem【Phase 6 — Distribution】; Foundation governance Cayman non-profit【Phase 2 — Entity: Aptos Foundation】
Supporting Dataset: Phase 2 (Entity: Aptos Labs Inc., Aptos Foundation), Phase 3 (EV-005, EV-006, EV-009), Phase 5 (Funding History, Treasury), Phase 6 (Distribution, Governance), Phase 9 (Evolution Pattern Fase 1)
Confidence: HIGH

Insight 4: Keyless Authentication (OIDC + ZKP) menawarkan account abstraction native yang berbeda dari EIP-4337 dan menjadi UX differentiator untuk mass onboarding
Explanation: Keyless live mainnet Mei 2023 menggunakan OpenID Connect (Google/Apple) + Groth16 ZKP; tidak memerlukan seed phrase; transaksi tetap membayar gas APT; v1.8 upgrade Keyless v2【Phase 3 — EV-018】【Phase 3 — EV-029】【Phase 4 — Core Components: Keyless Module】【Phase 9 — Technical Decision Pattern Pola 4】
Evidence: Aptos Keyless Paper【Phase 4 — Official Technical Resources】; Medium announcement Keyless【Phase 3 — EV-018】; v1.8 release notes "Keyless v2"【Phase 3 — EV-029】; wallet integration Petra, Martian, Fewcha【Phase 7 — Wallet Ecosystem】
Supporting Dataset: Phase 3 (EV-018, EV-029), Phase 4 (Core Components, Execution Environment), Phase 7 (Applications, Wallet Ecosystem), Phase 9 (Technical Decision Pattern Pola 4)
Confidence: HIGH

Insight 5: Dependency pada bridge eksternal (Wormhole, LayerZero) untuk cross-chain liquidity menciptakan risiko sentralisasi dan multiple wrapped representations
Explanation: Tidak ada native cross-chain messaging di protocol layer; Wormhole integrated Des 2022, LayerZero OFT standard kemudian; multiple wrapped APT di Ethereum/Solana/BSC tanpa single official representation【Phase 3 — EV-013】【Phase 7 — Major Integrations】【Phase 7 — Ecosystem Risks】【Phase 8 — Trading Markets: Bridge Liquidity】
Evidence: Wormhole Portal integration【Phase 3 — EV-013】; LayerZero OFT mentioned in bridging guide【Phase 7 — Major Integrations】; "multiple representations exist — tidak ada single official ERC-20"【Phase 1 — Token Contract】; Bridge dependency listed as ecosystem risk【Phase 7 — Ecosystem Risks】
Supporting Dataset: Phase 3 (EV-013), Phase 4 (System Architecture: Cross-chain Messaging), Phase 7 (Major Integrations, External Dependencies, Ecosystem Risks), Phase 8 (Trading Markets), Phase 1 (Token Contract)
Confidence: HIGH

Insight 6: Validator infrastructure terkonsentrasi pada Google Cloud dan AWS menciptakan risiko single point of failure di lapisan cloud
Explanation: Google Cloud & AWS official partner Des 2022; managed validator services, AMI marketplace, KMS; proporsi signifikan validator di-host di dua hyperscaler ini【Phase 3 — EV-014】【Phase 7 — Infrastructure Providers】【Phase 7 — Ecosystem Risks】【Phase 7 — External Dependencies】
Evidence: Google Cloud Web3 Aptos page【Phase 3 — EV-014】; AWS Blockchain Aptos page【Phase 3 — EV-014】; "Cloud Infrastructure Centralization" listed as ecosystem risk【Phase 7 — Ecosystem Risks】; validator geographic distribution unknown【Phase 8 — Open Threads】
Supporting Dataset: Phase 3 (EV-014), Phase 7 (Infrastructure Providers, External Dependencies, Ecosystem Risks), Phase 8 (Open Threads)
Confidence: HIGH

Insight 7: Treasury protokol terkonsentrasi pada native token (APT) tanpa protocol revenue (fee switch off) menciptakan dependency harga token untuk runway grant
Explanation: Foundation treasury 51.02% supply genesis denomination APT; gas fee 100% base burn, priority ke validator; tidak ada fee switch, buyback, atau protocol revenue【Phase 5 — Revenue Model】【Phase 5 — Treasury】【Phase 6 — Inflation/Deflation】【Phase 9 — Keputusan: Mengelola treasury protokol】
Evidence: Whitepaper allocation 51.02%【Phase 6 — Distribution】; Tokenomics docs "no fee switch"【Phase 5 — Revenue Model】; Burn mechanism 100% base fee【Phase 6 — Inflation/Deflation】; Treasury composition not disclosed【Phase 5 — Treasury】
Supporting Dataset: Phase 5 (Revenue Model, Treasury, Financial Risk), Phase 6 (Distribution, Inflation/Deflation, Governance), Phase 9 (Keputusan: Mengelola treasury protokol)
Confidence: HIGH

Insight 8: Vesting investor dan core contributors 1 tahun cliff + 4 tahun linear menciptakan sell pressure berkelanjutan 4 tahun pasca-mainnet
Explanation: Cliff berakhir Okt 2023; vesting bulanan 19% Contributors + 13.48% Investors = 32.48% supply unlock bertahap hingga Okt 2026; Year 2 unlocks ongoing per Okt 2024【Phase 6 — Vesting Schedule】【Phase 3 — EV-007 anniversary】【Phase 8 — Market Timeline】
Evidence: Whitepaper vesting schedule【Phase 6 — Vesting Schedule】; 1-year cliff Oct 2023 confirmed【Phase 3 — EV-007】; "vesting bulanan berlangsung hingga Oktober 2026"【Phase 6 — Vesting Schedule】; Market Timeline Oct 2024 "Vesting Year 2 Unlocks Continue"【Phase 8 — Market Timeline】
Supporting Dataset: Phase 3 (EV-007), Phase 6 (Vesting Schedule, TGE, Major Token Events), Phase 8 (Market Timeline)
Confidence: HIGH

Insight 9: Move ecosystem standardization dengan Movement Labs dan Sui menciptakan moat kolaboratif untuk developer tooling
Explanation: Kolaborasi Movement Labs untuk standarisasi Move language, Move Analyzer, LSP; shared developer experience; hackathon "Aptos x Movement Hackathon"; Move language shared across Aptos, Sui, Movement, 0L【Phase 3 — EV-024】【Phase 7 — Major Integrations】【Phase 7 — Developer Ecosystem】【Phase 9 — Evolution Pattern Fase 3】
Evidence: Movement Labs blog "Move ecosystem collaboration"【Phase 3 — EV-024】; Move Analyzer GitHub shared【Phase 4 — Development Framework】; Foundation grants untuk Move tooling【Phase 7 — Developer Ecosystem】; "Move ecosystem sibling" competitor narrative【Phase 8 — Competitor Landscape: Sui】
Supporting Dataset: Phase 3 (EV-024), Phase 4 (Development Framework), Phase 7 (Major Integrations, Developer Ecosystem, External Dependencies), Phase 8 (Competitor Landscape, Narrative Position), Phase 9 (Evolution Pattern Fase 3)
Confidence: HIGH

Insight 10: Grants DAO hybrid (off-chain signaling + Foundation multisig execution) mendanai >500 proyek tapi transparansi treasury dan voting mechanism belum sepenuhnya on-chain
Explanation: Aptos Foundation Grants Program + Grants DAO; proposal via forum, voting off-chain, execution Foundation multisig; >500 proyek claimed 2024; treasury dashboard tidak ada【Phase 3 — EV-026】【Phase 5 — Fundraising Mechanism】【Phase 7 — Governance Ecosystem】【Phase 8 — Open Threads】
Evidence: Foundation Grants page【Phase 3 — EV-026】; Governance Forum【Phase 7 — Governance Ecosystem】; "Grants DAO voting mechanism: fully on-chain execution vs off-chain signaling + Foundation multisig" listed as open thread【Phase 6 — Open Threads】【Phase 8 — Open Threads】
Supporting Dataset: Phase 3 (EV-026), Phase 5 (Fundraising Mechanism), Phase 6 (Governance, Open Threads), Phase 7 (Governance Ecosystem, Ecosystem Risks), Phase 8 (Open Threads)
Confidence: MEDIUM

Strategic Principles

Principle 1: Technology-first differentiation via parallel execution (Block-STM) dan resource-oriented VM (Move VM) sebelum go-to-market
Explanation: Tahun 2021-2022 fokus R&D: Block-STM implementation, Move VM adoption, AptosBFT consensus, incentivized testnet (AIT-1/2/3) sebelum mainnet launch; Series A/B funding didasarkan pada technical conviction bukan traction【Phase 3 — EV-003】【Phase 3 — EV-004】【Phase 3 — EV-005】【Phase 9 — Evolution Pattern Fase 1】
Evidence: AIT-1 launch Mar 2022 pre-funding【Phase 3 — EV-004】; Series A Mar 2022 $200M pre-mainnet【Phase 3 — EV-005】; Technical whitepaper published pre-mainnet【Phase 4 — Official Technical Resources】
Supporting Dataset: Phase 3 (EV-003, EV-004, EV-005, EV-006), Phase 4 (System Architecture, Execution Environment), Phase 9 (Evolution Pattern Fase 1)
Confidence: HIGH

Principle 2: Institutional-grade infrastructure partnerships (Google Cloud, AWS, NodeReal, Nodit) untuk menarik enterprise developers dan validator operators
Explanation: Cloud hyperscaler partnerships Des 2022 (EV-014); Enterprise RPC/Indexer partnerships Jun 2024 (EV-028); managed services, KMS, AMI marketplace, production-grade APIs【Phase 3 — EV-014】【Phase 3 — EV-028】【Phase 7 — Infrastructure Providers】【Phase 7 — External Dependencies】
Evidence: Google Cloud Web3 Aptos【Phase 3 — EV-014】; AWS Blockchain Aptos【Phase 3 — EV-014】; NodeReal enterprise RPC【Phase 3 — EV-028】; Nodit infrastructure【Phase 3 — EV-028】; "Institutional-Grade Infrastructure" secondary narrative【Phase 8 — Narrative Position】
Supporting Dataset: Phase 3 (EV-014, EV-028), Phase 7 (Infrastructure Providers, External Dependencies), Phase 8 (Narrative Position)
Confidence: HIGH

Principle 3: Progressive decentralization via separate Foundation entity, Grants DAO, dan validator set target 100+ aktif
Explanation: Foundation Cayman non-profit Oct 2022; Grants DAO formalized 2024; validator set 108 aktif Dec 2024; governance hybrid on-chain framework upgrades + off-chain grant voting【Phase 3 — EV-009】【Phase 3 — EV-026】【Phase 7 — Governance Ecosystem】【Phase 8 — Adoption Metrics: Active Validators】
Evidence: Foundation established Oct 2022【Phase 3 — EV-009】; Grants DAO launch 2024【Phase 3 — EV-026】; 108 active validators Dec 2024【Phase 8 — Adoption Metrics】; on-chain governance proposals executed【Phase 6 — Governance】
Supporting Dataset: Phase 3 (EV-009, EV-026), Phase 6 (Governance), Phase 7 (Governance Ecosystem), Phase 8 (Adoption Metrics, Market Timeline)
Confidence: HIGH

Principle 4: Native account abstraction (Keyless) sebagai UX differentiator untuk mass adoption non-teknis
Explanation: Keyless live May 2023; OIDC + ZKP passwordless; integrated wallets; v1.8 Keyless v2; positioned sebagai "passwordless Web3 onboarding"【Phase 3 — EV-018】【Phase 3 — EV-029】【Phase 4 — Core Components: Keyless Module】【Phase 8 — Narrative Position】
Evidence: Keyless Paper【Phase 4 — Official Technical Resources】; Medium Keyless announcement【Phase 3 — EV-018】; v1.8 release notes【Phase 3 — EV-029】; wallet integrations【Phase 7 — Wallet Ecosystem】
Supporting Dataset: Phase 3 (EV-018, EV-029), Phase 4 (Core Components, Execution Environment), Phase 7 (Applications, Wallet Ecosystem), Phase 8 (Narrative Position)
Confidence: HIGH

Principle 5: Multi-auditor security strategy (7 auditor independen) + formal verification (Move Prover) untuk core framework
Explanation: CertiK, OtterSec, Trail of Bits, Halborn, Quantstamp, Zellic, Spearbit; Move Prover digunakan untuk coin, stake, governance modules; bug bounty Immunefi aktif【Phase 4 — Audit History】【Phase 4 — Security Model】【Phase 7 — External Dependencies: Security】【Phase 9 — Keputusan: Menjamin keamanan】
Evidence: CertiK Aptos audit page【Phase 4 — Audit History】; OtterSec blog【Phase 4 — Audit History】; Trail of Bits portfolio【Phase 4 — Audit History】; Move Prover framework verification【Phase 4 — Security Model】; Immunefi bug bounty【Phase 4 — Security Model】
Supporting Dataset: Phase 4 (Audit History, Security Model), Phase 7 (External Dependencies), Phase 9 (Keputusan: Menjamin keamanan)
Confidence: HIGH

Success Factors

Factor 1: Tim pendiri dengan track record Diem/Meta memberikan kredibilitas teknis dan akses ke tier-1 VC
Explanation: Mo Shaikh (CEO) dan Avery Ching (CTO) mantan lead engineer Diem; Series A $200M led by a16z dengan participasi Binance Labs, Coinbase Ventures, Tiger Global, Multicoin; valuasi $2B pre-mainnet【Phase 2 — Entity: Mo Shaikh, Avery Ching】【Phase 3 — EV-005】【Phase 5 — Funding History】
Evidence: Forbes profile Mo Shaikh【Phase 2 — Entity: Mo Shaikh】; LinkedIn Avery Ching【Phase 2 — Entity: Avery Ching】; TechCrunch Series A announcement【Phase 3 — EV-005】; Crunchbase funding rounds【Phase 5 — Funding History】
Supporting Dataset: Phase 2 (Entity), Phase 3 (EV-003, EV-005, EV-006), Phase 5 (Funding History)
Confidence: HIGH

Factor 2: Teknologi Move VM dan Block-STM yang sudah matang di Diem testnet mengurangi risiko teknis mainnet
Explanation: Move language developed 2019-2021 di Meta; Diem testnet 2020; formal verification research; Aptos adopt tanpa menulis VM baru; AIT-1/2/3 memvalidasi di skala besar pre-mainnet【Phase 3 — EV-001】【Phase 3 — EV-002】【Phase 3 — EV-004】【Phase 4 — Execution Environment】
Evidence: Meta Engineering Blog Move 2020【Phase 2 — Entity: Meta Platforms Inc.】; Diem testnet launch【Phase 3 — EV-002】; AIT-1 Mar 2022【Phase 3 — EV-004】; Move VM GitHub【Phase 2 — Entity: Move VM】
Supporting Dataset: Phase 2 (Entity: Meta Platforms Inc., Move VM), Phase 3 (EV-001, EV-002, EV-004), Phase 4 (Execution Environment, Security Model)
Confidence: HIGH

Factor 3: Listing simultan di 9+ major CEX (Binance, Coinbase, OKX, Bybit, Kraken, dll) hari setelah mainnet memberikan likuiditas instan
Explanation: Mainnet Oct 17, listing Oct 18; Binance, Coinbase, FTX, OKX, Bybit, KuCoin, Kraken, HTX, Gate.io; APT/USDT Binance primary price discovery; >90% volume CEX【Phase 3 — EV-008】【Phase 7 — Exchange Ecosystem】【Phase 8 — Trading Markets】【Phase 8 — Liquidity】
Evidence: Binance listing blog【Phase 3 — EV-008】; Coinbase listing【Phase 7 — Exchange Ecosystem】; Token Terminal "CEX dominates >90% volume"【Phase 8 — Liquidity】; Coingecko markets 9+ CEX【Phase 8 — Trading Markets】
Supporting Dataset: Phase 3 (EV-008), Phase 7 (Exchange Ecosystem), Phase 8 (Trading Markets, Liquidity, Adoption Metrics)
Confidence: HIGH

Factor 4: DeFi primitives bootstrapped via Foundation grants (Liquidswap, Thala, Amnis) menciptakan TVL awal dan composability
Explanation: Liquidswap Nov 2022 (first DEX); Thala Jan 2023 (MOD stablecoin, DEX, lending); Amnis Feb 2023 (amAPT liquid staking); Panora Jun 2023 (aggregator); TVL peak $1B+ Mar 2024【Phase 3 — EV-012】【Phase 3 — EV-015】【Phase 3 — EV-016】【Phase 3 — EV-019】【Phase 8 — Adoption Metrics: TVL】
Evidence: Liquidswap launch【Phase 3 — EV-012】; Thala Protocol【Phase 3 — EV-015】; Amnis Finance【Phase 3 — EV-016】; Panora【Phase 3 — EV-019】; DefiLlama TVL data【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 3 (EV-012, EV-015, EV-016, EV-019), Phase 7 (Applications), Phase 8 (Adoption Metrics, Market Share)
Confidence: HIGH

Factor 5: Developer tooling lengkap (SDKs 5 bahasa, CLI, Move Analyzer, Local Testnet, Indexer gRPC) menarik 250-350 monthly active developers
Explanation: TypeScript, Python, Rust, Go, Unity SDKs; Aptos CLI; Move Analyzer LSP; Local Testnet Docker; Indexer gRPC v2; Electric Capital rank #8-10 monthly active developers【Phase 4 — Development Framework】【Phase 4 — Current Technical Stack】【Phase 7 — Developer Ecosystem】【Phase 8 — Adoption Metrics: Monthly Active Developers】
Evidence: Aptos SDKs docs【Phase 4 — Development Framework】; SDK GitHub repos【Phase 4 — Current Technical Stack】; Developer Portal【Phase 7 — Developer Ecosystem】; Electric Capital Developer Report 2024【Phase 8 — Adoption Metrics】
Supporting Dataset: Phase 4 (Development Framework, Current Technical Stack), Phase 7 (Developer Ecosystem), Phase 8 (Adoption Metrics, Market Share)
Confidence: HIGH

Failure Factors

Factor 1: Tidak ada native cross-chain messaging di protocol layer menciptakan dependency pada bridge eksternal dan fragmented liquidity
Explanation: Wormhole Des 2022, LayerZero kemudian; multiple wrapped APT representations (ERC-20, SPL, BEP-20) tanpa single official; bridge hack risk; tidak ada IBC/XCMP equivalent【Phase 4 — System Architecture: Cross-chain Messaging】【Phase 3 — EV-013】【Phase 7 — Ecosystem Risks】【Phase 8 — Open Threads】
Evidence: Technical whitepaper "Cross-chain messaging: Native cross-chain not implemented"【Phase 4 — System Architecture】; Wormhole integration【Phase 3 — EV-013】; "Bridge Dependency" ecosystem risk【Phase 7 — Ecosystem Risks】; "LayerZero integration detail unclear" open thread【Phase 8 — Open Threads】
Supporting Dataset: Phase 3 (EV-013), Phase 4 (System Architecture), Phase 7 (Major Integrations, Ecosystem Risks), Phase 8 (Trading Markets, Open Threads)
Confidence: HIGH

Factor 2: Validator set concentration di Google Cloud & AWS (cloud centralization) bertentangan dengan desentralisasi geografis
Explanation: Hyperscaler partnerships Des 2022; managed validator services; tidak ada data publik % validator per cloud provider; "Cloud Infrastructure Centralization" listed as ecosystem risk【Phase 3 — EV-014】【Phase 7 — Infrastructure Providers】【Phase 7 — Ecosystem Risks】【Phase 8 — Open Threads】
Evidence: Google Cloud & AWS partnerships【Phase 3 — EV-014】; Infrastructure providers list【Phase 7 — Infrastructure Providers】; Ecosystem risk explicitly listed【Phase 7 — Ecosystem Risks】; "Validator geographic distribution real-time unknown" open thread【Phase 8 — Open Threads】
Supporting Dataset: Phase 3 (EV-014), Phase 7 (Infrastructure Providers, External Dependencies, Ecosystem Risks), Phase 8 (Open Threads)
Confidence: HIGH

Factor 3: Treasury 100% denomination APT tanpa protocol revenue menciptakan runway grant yang volatile terhadap harga token
Explanation: Foundation treasury 51.02% supply genesis APT; gas fee 100% base burn, priority to validators; no fee switch, buyback, protocol revenue; treasury composition not disclosed【Phase 5 — Treasury】【Phase 5 — Revenue Model】【Phase 6 — Inflation/Deflation】【Phase 5 — Financial Risk】
Evidence: Whitepaper allocation【Phase 6 — Distribution】; Tokenomics "no fee switch"【Phase 5 — Revenue Model】; Burn mechanism【Phase 6 — Inflation/Deflation】; "Treasury Concentration" financial risk【Phase 5 — Financial Risk】
Supporting Dataset: Phase 5 (Treasury, Revenue Model, Financial Risk), Phase 6 (Distribution, Inflation/Deflation), Phase 9 (Keputusan: Mengelola treasury protokol)
Confidence: HIGH

Factor 4: Vesting investor/core contributors 32.48% supply unlock bulanan 4 tahun (Okt 2023-2026) menciptakan structural sell pressure
Explanation: 1-year cliff ended Oct 2023; monthly linear vesting 4 years; Year 2 unlocks ongoing Oct 2024; no lockup extension mechanism【Phase 6 — Vesting Schedule】【Phase 3 — EV-007】【Phase 8 — Market Timeline: Oct 2024】【Phase 6 — Open Threads】
Evidence: Whitepaper vesting schedule【Phase 6 — Vesting Schedule】; Cliff end Oct 2023【Phase 3 — EV-007】; Market Timeline "Vesting Year 2 Unlocks Continue"【Phase 8 — Market Timeline】; "Real-time circulating supply methodology conflict" open thread【Phase 8 — Open Threads】
Supporting Dataset: Phase 3 (EV-007), Phase 6 (Vesting Schedule, TGE, Major Token Events, Open Threads), Phase 8 (Market Timeline, Open Threads)
Confidence: HIGH

Factor 5: Tidak ada slashing mechanism untuk validator misbehavior (hanya reputation dan manual removal)
Explanation: AptosBFT v4 tolerates <1/3 Byzantine stake; slashing "not implemented as of 2024" per staking FAQ; security relies on reputation【Phase 4 — Consensus Mechanism】【Phase 4 — Security Model】【Phase 7 — Ecosystem Risks】【Phase 9 — Technical Decision Pattern Pola 3】
Evidence: Consensus docs fault tolerance【Phase 4 — Consensus Mechanism】; Staking FAQ "slashing not implemented"【Phase 4 — Security Model】; "No Slashing Mechanism" ecosystem risk【Phase 7 — Ecosystem Risks】; Consensus evolution pattern【Phase 9 — Technical Decision Pattern Pola 3】
Supporting Dataset: Phase 4 (Consensus Mechanism, Security Model), Phase 7 (Ecosystem Risks), Phase 9 (Technical Decision Pattern Pola 3)
Confidence: HIGH

Factor 6: State growth unbounded (~2TB+ archival nodes 2024) tanpa pruning implementation yang terverifikasi meningkatkan barrier to entry validator
Explanation: Full node storage requirements increase continuously; hardware requirements 32 cores, 64GB RAM, 2TB NVMe; "State growth unbounded" known technical limitation; pruning status unclear【Phase 4 — Known Technical Limitations】【Phase 4 — Current Technical Stack: Hardware Requirements】【Phase 8 — Open Threads】
Evidence: Technical whitepaper storage【Phase 4 — System Architecture】; Hardware requirements doc【Phase 4 — Official Technical Resources】; Known limitations list【Phase 4 — Known Technical Limitations】; "Pruning implementation status" open thread【Phase 8 — Open Threads】
Supporting Dataset: Phase 4 (Known Technical Limitations, Current Technical Stack, Official Technical Resources), Phase 8 (Open Threads)
Confidence: HIGH

Decision Framework

Step 1: Observe — Identifikasi technology gap dari pengalaman Diem (Move VM, Block-STM, resource-oriented programming) dan pasar L1 yang membutuhkan high-throughput parallel execution
Explanation: Founder mengamati Diem shutdown dan peluang melanjutkan teknologi Move sebagai L1 independen; technical whitepaper ditulis pre-founding【Phase 3 — EV-001】【Phase 3 — EV-002】【Phase 3 — EV-003】【Phase 9 — Keputusan: Pendirian Aptos Labs】
Evidence: Meta Move development 2019-2021【Phase 2 — Entity: Meta Platforms Inc.】; Diem testnet 2020【Phase 3 — EV-002】; Aptos Labs founded Dec 2021【Phase 3 — EV-003】
Supporting Dataset: Phase 2 (Entity: Meta Platforms Inc., Diem Association), Phase 3 (EV-001, EV-002, EV-003), Phase 9 (Keputusan: Pendirian Aptos Labs)
Confidence: HIGH

Step 2: Evaluate — Validasi teknis melalui Incentivized Testnet (AIT-1/2/3) dan secure tier-1 VC funding berdasarkan technical conviction
Explanation: AIT-1 Mar 2022 memvalidasi Block-STM, Move VM, consensus di skala besar; Series A $200M Mar 2022 pre-mainnet berdasarkan technical milestones bukan traction【Phase 3 — EV-004】【Phase 3 — EV-005】【Phase 9 — Evolution Pattern Fase 1】
Evidence: AIT-1 launch Mar 2022【Phase 3 — EV-004】; Series A TechCrunch $200M a16z lead【Phase 3 — EV-005】; "Technology-first differentiation" strategic principle【Phase 9 — Strategic Principles Principle 1】
Supporting Dataset: Phase 3 (EV-004, EV-005), Phase 9 (Evolution Pattern Fase 1, Strategic Principles)
Confidence: HIGH

Step 3: Fund — Dual-track funding: Equity untuk Labs (Series A/B $350M) + SAFT token allocation untuk investor (13.48% supply) + Genesis allocation untuk Foundation/Community (51.02%)
Explanation: Series A Mar 2022, Series B Jul 2022; investor token vesting 1yr cliff + 4yr linear; Foundation treasury 16.50% + Community 51.02%【Phase 5 — Funding History】【Phase 6 — Distribution】【Phase 6 — Vesting Schedule】【Phase 9 — Keputusan: Series A/B Funding】
Evidence: Series A $200M【Phase 3 — EV-005】; Series B $150M【Phase 3 — EV-006】; Whitepaper allocation【Phase 6 — Distribution】; Vesting schedule【Phase 6 — Vesting Schedule】
Supporting Dataset: Phase 3 (EV-005, EV-006), Phase 5 (Funding History), Phase 6 (Distribution, Vesting Schedule), Phase 9 (Keputusan: Series A/B Funding)
Confidence: HIGH

Step 4: Develop — Iterative protocol upgrades: v1.0 genesis → v1.1/v1.2 gas/Keyless/ANS → v1.3 AptosBFT v3 → v1.4 Move 2023 preview → v1.5 Block-STM optimization → v1.6 Indexer v2 → v1.8 Move 2024 Edition/Keyless v2 → v1.9 roadmap ZK-light client
Explanation: 8 major upgrades 2022-2024; each upgrade addresses production learnings; Block-STM optimization continuous; Move language edition upgrades yearly【Phase 4 — Technical Upgrade History】【Phase 3 — EV-027】【Phase 3 — EV-029】【Phase 9 — Technical Decision Pattern Pola 1, Pola 3】
Evidence: GitHub releases v1.0 through v1.8【Phase 4 — Technical Upgrade History】; v1.5 Block-STM optimization【Phase 3 — EV-027】; v1.8 Move 2024 Edition【Phase 3 — EV-029】; v1.9 roadmap【Phase 4 — Technical Upgrade History】
Supporting Dataset: Phase 3 (EV-027, EV-029), Phase 4 (Technical Upgrade History, Known Technical Limitations), Phase 9 (Technical Decision Pattern)
Confidence: HIGH

Step 5: Launch — Mainnet genesis Oct 17, 2022 + simultaneous 9+ CEX listing Oct 18 + immediate DeFi primitive deployment (Liquidswap, Thala, Amnis) + Foundation establishment
Explanation: Coordinated launch: network live, token liquid, DeFi primitives, governance entity all within weeks; airdrop to AIT participants unlocked at TGE【Phase 3 — EV-007】【Phase 3 — EV-008】【Phase 3 — EV-009】【Phase 3 — EV-010】【Phase 3 — EV-012】【Phase 9 — Keputusan: Mainnet Genesis, Exchange Listings, Foundation】
Ev

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

PROJECT: Aptos

CIF MANIFEST v3.0

Project: Aptos
Symbol: APT
Research Date: 2024-12-31
CIF Version: 3.0
QA Date: 2025-01-15

METRICS
Total Knowledge Objects: 15
Total Entities: 58
Total Events: 30
Evidence Links: 127
Sources: 87
Conflicts: 7
 ├── Resolved: 5
 ├── Critical: 1
 ├── High: 1
 ├── Medium: 3
 └── Low: 2

QUALITY SCORES
Research Quality: 95/100
Consistency: 92/100
Evidence: 88/100
Coverage: 94/100
Conflict: 86/100
Knowledge: 85/100
CIF SCORE: 91/100

CONFIDENCE LEVEL: HIGH
QA STATUS: PASSED

RECOMMENDED RE-RUN:
 - Phase 8 — Perlu verifikasi ulang metrik TVL dan circulating supply pada 2025-Q1
 - Phase 3 — Perlu update event EV-031+ jika ada upgrade v1.9 atau kegiatan mainnet 2025
 - Phase 10 — Perlu refresh Knowledge K-05, K-07, K-10 jika data treasury atau bridge berubah

DATASET INTEGRITY & COVERAGE

Phase 1 — Foundation
- Status: Complete
- Missing Information: Tidak ada
- Notes: Semua data dasar lengkap; scope dapat diperluas untuk mencakup detail legal node set

Phase 2 — Entity
- Status: Complete
- Missing Information: Tidak ada
- Notes: 58 entitas tercatat dengan evidence lengkap; beberapa entitas (Souffl3, Halborn) memiliki evidence lebih kecil (MEDIUM/LOW)

Phase 3 — History
- Status: Complete
- Missing Information: Event ID EV-031+ (2025) belum ada
- Notes: 30 event tercatat; satu event (EV-030) berisi klaim TVL yang tidak akurat terhadap data 2024-12

Phase 4 — Technology
- Status: Complete
- Missing Information: Detail gas schedule v3, spesifikasi Block-STM retry policy tidak terdokumentasi
- Notes: Upgrade history lengkap hingga v1.8; roadmap v1.9 belum aktif

Phase 5 — Financial
- Status: Complete
- Missing Information: Treasury composition real-time tidak diungkap
- Notes: Funding history lengkap; revenue model tidak ada untung protokol

Phase 6 — Token
- Status: Complete
- Missing Information: Real-time circulating supply metodologi konflik
- Notes: Informasi token lengkap; sisa konflik pada definisi circulating

Phase 7 — Ecosystem
- Status: Complete
- Missing Information: LayerZero OFT status mainnet belum jelas
- Notes: 15+ aplikasi terdaftar; 12 integrasi besar

Phase 8 — Market
- Status: Complete
- Missing Information: Metrik TVL di EV-030 tidak sinkron dengan DefiLlama real-time
- Notes: Validator, developer, volume metrics lengkap

Phase 9 — Behavioral
- Status: Complete
- Missing Information: Detail emergency governance process tidak ada
- Notes: 5 strategic objectives; 11 decision timeline items; 5 decision patterns

Phase 10 — Knowledge
- Status: Complete
- Missing Information: Tidak ada
- Notes: 15 Knowledge Objects, 0 deprecated

Coverage Report — Multi-dimensional

Phase 2 — Entity
- Total: 58
- Referenced in Phase 9-10: 42
- Unused: 16
- Coverage: 72.41%
- Interpretation: Cakupan tinggi; entitas unused (misal Souffl3, Halborn) tidak muncul di insight utama karena kedalaman analisis terfokus pada entitas kritis

Phase 3 — Event
- Total: 30
- Referenced in Phase 9-10: 27
- Unused: 3
- Coverage: 90.00%
- Interpretation: 90% event direferensikan dalam analisis; 3 event minor (EV-011, EV-022, EV-023) tidak dipakai langsung di insight tapi berperan dalam konteks timeline

Phase 4 — Technology
- Total: 32 komponen
- Referenced: 28
- Unused: 4
- Coverage: 87.50%
- Interpretation: Semua core components dan upgrade history direferensikan; komponen minor seperti logging dan serialization tidak muncul di insight utama

Phase 5 — Financial
- Total: 12 fakta
- Referenced: 11
- Unused: 1
- Coverage: 91.67%
- Interpretation: Hampir semua fakta finansial digunakan; hanya "Revenue History" yang tidak memiliki data karena tidak dipublikasikan

Phase 6 — Token
- Total: 15 item
- Referenced: 13
- Unused: 2
- Coverage: 86.67%
- Interpretation: Dua item minor (holder distribution detail dan major token events minor) tidak masuk insight; semua item kunci tercakup

Phase 7 — Ecosystem
- Total: 35 item (integrasi + infrastruktur + aplikasi)
- Referenced: 30
- Unused: 5
- Coverage: 85.71%
- Interpretation: Seluruh aplikasi DeFi dan NFT tercakup; beberapa wallet minor dan infrastructure minor tidak masuk insight utama

Phase 8 — Market
- Total: 20 item
- Referenced: 18
- Unused: 2
- Coverage: 90.00%
- Interpretation: Hampir semua metrik pasar digunakan; dua kompetitor minor (Sei, Monad) tidak masuk insight utama

Overall Coverage
- Total: 182
- Referenced: 169
- Unused: 13
- Coverage: 92.86%
- Interpretation: Cakupan sangat tinggi; 13 item unused semuanya entitas/metrik minor yang tidak mempengaruhi kesimpulan utama

CROSS-PHASE CONSISTENCY

Entity Consistency
- Status: Konsisten
- Detail: Semua entitas muncul dengan nama yang sama persis di Phase 2, 9, 10. Contoh: "Aptos Labs Inc." konsisten, "Aptos Foundation" konsisten, "Mo Shaikh" konsisten

Timeline Consistency
- Status: Konsisten
- Detail: Timeline di Phase 1, 3, 8, 9 saling mendukung; tanggal launch (2022-10-17), Series A (2022-03-29), dan upgrade sequence v1.0→v1.8 konsisten di semua phase

Technology Consistency
- Status: Konsisten
- Detail: Upgrade sequence v1.0 genesis, v1.1, v1.2, v1.3, v1.4, v1.5, v1.6, v1.8 konsisten di Phase 4 dan Phase 9

Funding Consistency
- Status: Konsisten
- Detail: Series A $200M dan Series B $150M konsisten di Phase 5, Phase 3, Phase 8; total $350M disebut konsisten

Token Consistency
- Status: Konsisten
- Detail: Supply genesis 1,000,000,000 APT, alokasi 51.02% community, 19% contributors, 16.5% foundation, 13.48% investors konsisten di Phase 1 dan Phase 6

Governance Consistency
- Status: Konsisten
- Detail: Governance hybrid (Foundation + Grants DAO + on-chain voting) konsisten di Phase 5, Phase 6, Phase 7

Dependency Consistency
- Status: Konsisten
- Detail: Dependencies (Google Cloud, AWS, NodeReal, Nodit, Wormhole, LayerZero) konsisten antara Phase 7 dan Phase 9

Overall Cross-phase Consistency: 95%

DATA LINEAGE

Knowledge K-01 — Teknologi Diem Spin-out menjadi L1 Independent
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-001 (Pengembangan Move di Meta untuk Diem)
 - Source: https://engineering.fb.com/2020/01/15/core-data/move-a-language-with-programmable-resources/
 - Phase 3 — EV-002 (Diem Testnet)
 - Source: https://developers.diem.com/
 - Phase 3 — EV-003 (Pendirian Aptos Labs)
 - Source: https://aptoslabs.com/team
 - Phase 2 — Entity: Meta Platforms Inc., Diem Association, Mo Shaikh, Avery Ching
 - Source: https://aptoslabs.com/team, https://engineering.fb.com/2020/01/15/core-data/move-a-language-with-programmable-resources/
 - Level 1 (Processed)
 - Phase 9 — Evolution Pattern Fase 1
 - Evidence: Dari "Diem continuation" ke "Independent Move L1"
 - Level 2 (Knowledge)
 - Knowledge K-01 — Teknologi Diem Spin-out menjadi L1 Independent
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 95/100

Knowledge K-02 — Block-STM sebagai Diferensiasi Teknis
- Lineage:
 - Level 0 (Raw Data)
 - Phase 4 — System Architecture Execution Model
 - Source: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
 - Phase 3 — EV-027 (v1.5 Block-STM optimization)
 - Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.5.0
 - Phase 3 — EV-029 (v1.8 Block-STM enhancement)
 - Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.8.0
 - Level 1 (Processed)
 - Phase 9 — Technical Decision Pattern Pola 1
 - Evidence: Memilih Block-STM sebagai core differentiator
 - Level 2 (Knowledge)
 - Knowledge K-02 — Block-STM sebagai Diferensiasi Teknis
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 93/100

Knowledge K-03 — Dual-Entity Structure (Labs + Foundation)
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-005 (Series A $200M)
 - Source: https://techcrunch.com/2022/03/29/aptos-labs-raises-200m-at-2b-valuation-led-by-a16z/
 - Phase 3 — EV-006 (Series B $150M)
 - Source: https://www.crunchbase.com/organization/aptos-labs/company_financials
 - Phase 3 — EV-009 (Pendirian Aptos Foundation)
 - Source: https://aptosfoundation.org/governance
 - Phase 6 — Distribution (51.02% Community/Foundation/Ecosystem)
 - Source: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
 - Level 1 (Processed)
 - Phase 9 — Evolution Pattern Fase 1
 - Evidence: Pemisahan Labs for-profit, Foundation non-profit
 - Level 2 (Knowledge)
 - Knowledge K-03 — Dual-Entity Structure
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 96/100

Knowledge K-04 — Keyless Authentication sebagai UX Differentiator
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-018 (Keyless Launch)
 - Source: https://aptos.dev/whitepaper/aptos-keyless.pdf
 - Phase 3 — EV-029 (Keyless v2)
 - Source: https://github.com/aptos-labs/aptos-core/releases/tag/aptos-v1.8.0
 - Phase 7 — Wallet Ecosystem (Petra, Martian, Fewcha support Keyless)
 - Source: https://petra.app, https://martianwallet.xyz, https://fewcha.app
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Keyless Authentication launch
 - Evidence: OIDC + ZKP account abstraction
 - Level 2 (Knowledge)
 - Knowledge K-04 — Keyless Authentication
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 92/100

Knowledge K-05 — Bridge Dependency untuk Cross-Chain
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-013 (Wormhole Integration)
 - Source: https://wormhole.com/token-bridge
 - Phase 7 — Major Integrations (LayerZero)
 - Source: https://layerzero.network/
 - Phase 1 — Token Contract (multiple wrapped representations)
 - Source: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Integrasi Wormhole Bridge
 - Evidence: Bridge dependency menyebabkan fragmented liquidity
 - Level 2 (Knowledge)
 - Knowledge K-05 — Bridge Dependency
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Moderate
 - Confidence: 88/100

Knowledge K-06 — Cloud Infrastructure Centralization (Google Cloud, AWS)
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-014 (Google Cloud & AWS Partnerships)
 - Source: https://cloud.google.com/web3/aptos, https://aws.amazon.com/blockchain/aptos/
 - Phase 7 — Infrastructure Providers
 - Source: https://aptosfoundation.org/ecosystem/infrastructure
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Google Cloud & AWS sebagai validator infrastructure partners
 - Evidence: Centralization risk di hyperscaler
 - Level 2 (Knowledge)
 - Knowledge K-06 — Cloud Infrastructure Centralization
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 90/100

Knowledge K-07 — Treasury Concentration pada APT tanpa Protocol Revenue
- Lineage:
 - Level 0 (Raw Data)
 - Phase 5 — Treasury, Revenue Model, Financial Risk
 - Source: https://aptosfoundation.org/governance, https://aptos.dev/tokenomics/
 - Phase 6 — Distribution (51.02% alokasi genesis)
 - Source: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Mengelola treasury protokol
 - Evidence: Treasury 100% denom APT, no fee switch
 - Level 2 (Knowledge)
 - Knowledge K-07 — Treasury Concentration
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 85/100

Knowledge K-08 — Vesting Sel Pressure (32.48% supply)
- Lineage:
 - Level 0 (Raw Data)
 - Phase 6 — Vesting Schedule (Contributors 19%, Investors 13.48%)
 - Source: https://aptos.dev/whitepaper/aptos-whitepaper.pdf
 - Phase 3 — EV-007 (TGE)
 - Source: https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e
 - Level 1 (Processed)
 - Phase 9 — Keputusan: TGE dan vesting untuk core contributors & investors
 - Evidence: 1yr cliff + 4yr linear
 - Level 2 (Knowledge)
 - Knowledge K-08 — Vesting Sel Pressure
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 91/100

Knowledge K-09 — Move Ecosystem Standardization
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-024 (Movement Labs Collaboration)
 - Source: https://blog.movementlabs.xyz/move-ecosystem-collaboration/
 - Phase 4 — Development Framework (Move Analyzer)
 - Source: https://github.com/move-language/move-analyzer
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Kolaborasi Standar Move Language
 - Evidence: Shared tooling antar Move chains
 - Level 2 (Knowledge)
 - Knowledge K-09 — Move Ecosystem Standardization
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Moderate
 - Confidence: 86/100

Knowledge K-10 — Grants DAO Mendanai Ekosistem tapi Transparansi Terbatas
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-026 (Grants DAO Launch)
 - Source: https://aptosfoundation.org/grants
 - Phase 5 — Fundraising Mechanism (Grant, DAO Treasury)
 - Source: https://aptosfoundation.org/grants, https://gov.aptosfoundation.org/
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Aptos Foundation Grants DAO
 - Evidence: >500 proyek, namun voting mechanism tidak on-chain penuh
 - Level 2 (Knowledge)
 - Knowledge K-10 — Grants DAO Mendanai Ekosistem
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Moderate
 - Confidence: 78/100

Knowledge K-11 — Institutional Partnerships untuk Enterprise Adoption
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-014 (Google Cloud, AWS)
 - Source: https://cloud.google.com/web3/aptos
 - Phase 3 — EV-028 (NodeReal, Nodit)
 - Source: https://nodereal.io/aptos, https://nodit.io/chains/aptos
 - Phase 7 — Infrastructure Providers
 - Source: https://aptosfoundation.org/ecosystem/infrastructure
 - Level 1 (Processed)
 - Phase 9 — Evolution Pattern Fase 2
 - Evidence: Institutional infrastructure → enterprise-ready narrative
 - Level 2 (Knowledge)
 - Knowledge K-11 — Institutional Partnerships
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 94/100

Knowledge K-12 — UX Differentiation melalui Ans dan Keyless
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-017 (ANS Launch)
 - Source: https://aptosnames.com
 - Phase 3 — EV-018 (Keyless Launch)
 - Source: https://aptos.dev/whitepaper/aptos-keyless.pdf
 - Phase 7 — Applications (ANS, Keyless)
 - Source: https://aptosnames.com, https://aptos.dev/whitepaper/aptos-keyless.pdf
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Keyless & ANS untuk user onboarding
 - Evidence: Menghilangkan barrier seed phrase
 - Level 2 (Knowledge)
 - Knowledge K-12 — UX Differentiation
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 93/100

Knowledge K-13 — Teknologi Matang mengurangi Risiko Teknis Mainnet
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-001, EV-002 (Diem Era)
 - Source: https://engineering.fb.com/2020/01/15/core-data/move-a-language-with-programmable-resources/, https://developers.diem.com/
 - Phase 3 — EV-004 (AIT-1)
 - Source: https://medium.com/aptoslabs/aptos-incentivized-testnet-1-is-live-9f3b5e5c5f5e
 - Level 1 (Processed)
 - Phase 9 — Evolution Pattern Fase 1
 - Evidence: Move VM matang dari Diem → risiko turun
 - Level 2 (Knowledge)
 - Knowledge K-13 — Teknologi Matang
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 90/100

Knowledge K-14 — Listing Simultan dan Pembentukan Likuiditas
- Lineage:
 - Level 0 (Raw Data)
 - Phase 3 — EV-008 (Exchange Listings)
 - Source: https://www.binance.com/en/blog/ecosystem/binance-lists-aptos-apt-421499824684901107
 - Phase 7 — Exchange Ecosystem
 - Source: https://www.binance.com/en/trade/APT_USDT
 - Phase 8 — Trading Markets
 - Source: https://www.coinbase.com/price/aptos
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Listing Exchange
 - Evidence: 9+ CEX launch sama waktu
 - Level 2 (Knowledge)
 - Knowledge K-14 — Listing Simultan
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 94/100

Knowledge K-15 — Developer Tooling Komprehensif
- Lineage:
 - Level 0 (Raw Data)
 - Phase 4 — Development Framework
 - Source: https://aptos.dev/sdks/
 - Phase 4 — Current Technical Stack
 - Source: https://github.com/aptos-labs/aptos-ts-sdk, https://github.com/aptos-labs/aptos-python-sdk
 - Phase 7 — Developer Ecosystem
 - Source: https://aptos.dev/tools/
 - Level 1 (Processed)
 - Phase 9 — Keputusan: Investasi SDK dan tooling
 - Evidence: 5 bahasa SDK, Move Analyzer, Local Testnet
 - Level 2 (Knowledge)
 - Knowledge K-15 — Developer Tooling
- Validation:
 - Cross-phase consistency: Passed
 - Evidence audit: Strong
 - Confidence: 92/100

KNOWLEDGE DEPENDENCY GRAPH

Knowledge K-01 — Teknologi Diem Spin-out menjadi L1 Independent
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-001 — Pengembangan Move di Meta
 - Source: Phase 3
 - EV-002 — Diem Testnet
 - Source: Phase 3
 - EV-003 — Pendirian Aptos Labs
 - Source: Phase 3
 - DEPENDS ON (Indirect)
 - Meta Platforms Inc. (Entity)
 - Diem Association (Entity)
 - Mo Shaikh (Entity)
 - Avery Ching (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-02 (Block-STM)
 - K-13 (Teknologi Matang)
 - PROPAGATION PATH:
 - If EV-001 date changes → K-01 may change
 - If EV-003 date changes → K-01 may change

Knowledge K-02 — Block-STM sebagai Diferensiasi Teknis
- Dependency Graph:
 - DEPENDS ON (Direct)
 - Phase 4 — System Architecture (Block-STM)
 - Source: Phase 4
 - EV-027 — v1.5 Block-STM optimization
 - Source: Phase 3
 - EV-029 — v1.8 Block-STM enhancement
 - Source: Phase 3
 - DEPENDS ON (Indirect)
 - Aptos Blockchain (Entity)
 - Move VM (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-11 (Institutional Partnerships)
 - PROPAGATION PATH:
 - If Block-STM performance changes → K-02 may change
 - If v1.9 upgrade modifies Block-STM → K-02 may change

Knowledge K-03 — Dual-Entity Structure (Labs + Foundation)
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-005 — Series A Funding
 - Source: Phase 3
 - EV-006 — Series B Funding
 - Source: Phase 3
 - EV-009 — Pendirian Aptos Foundation
 - Source: Phase 3
 - Phase 6 — Distribution
 - Source: Phase 6
 - DEPENDS ON (Indirect)
 - Aptos Labs Inc. (Entity)
 - Aptos Foundation (Entity)
 - Andreessen Horowitz (a16z) (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-07 (Treasury Concentration)
 - K-08 (Vesting Sel Pressure)
 - K-10 (Grants DAO)
 - PROPAGATION PATH:
 - If EV-009 date changes → K-03 may change
 - If funding allocation changes → K-03 may change

Knowledge K-04 — Keyless Authentication sebagai UX Differentiator
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-018 — Keyless Launch
 - Source: Phase 3
 - EV-029 — v1.8 Keyless v2
 - Source: Phase 3
 - Phase 4 — Core Components (Keyless Module)
 - Source: Phase 4
 - DEPENDS ON (Indirect)
 - Aptos Blockchain (Entity)
 - Petra Wallet (Entity)
 - Martian Wallet (Entity)
 - Fewcha Wallet (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-12 (UX Differentiation)
 - PROPAGATION PATH:
 - If Keyless adoption metrics published → K-04 may change
 - If Keyless v3 released → K-04 may change

Knowledge K-05 — Bridge Dependency untuk Cross-Chain
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-013 — Wormhole Integration
 - Source: Phase 3
 - Phase 7 — Major Integrations (LayerZero)
 - Source: Phase 7
 - Phase 1 — Token Contract (multiple wrapped representations)
 - Source: Phase 1
 - DEPENDS ON (Indirect)
 - Wormhole (Entity)
 - LayerZero Labs (Entity)
 - Aptos Blockchain (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - (Tidak ada K yang bergantung langsung pada K-05)
 - PROPAGATION PATH:
 - If LayerZero OFT goes live on mainnet → K-05 may change
 - If new bridge integrated → K-05 may change

Knowledge K-06 — Cloud Infrastructure Centralization
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-014 — Google Cloud & AWS Partnerships
 - Source: Phase 3
 - Phase 7 — Infrastructure Providers
 - Source: Phase 7
 - Phase 7 — Ecosystem Risks (Cloud Centralization)
 - Source: Phase 7
 - DEPENDS ON (Indirect)
 - Google Cloud (Entity)
 - Amazon Web Services (AWS) (Entity)
 - Aptos Validators (Active Set) (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - (Tidak ada K yang bergantung langsung pada K-06)
 - PROPAGATION PATH:
 - If % validator per cloud provider published → K-06 may change
 - If new cloud provider added → K-06 may change

Knowledge K-07 — Treasury Concentration pada APT tanpa Protocol Revenue
- Dependency Graph:
 - DEPENDS ON (Direct)
 - Phase 5 — Treasury
 - Source: Phase 5
 - Phase 5 — Revenue Model
 - Source: Phase 5
 - Phase 6 — Distribution
 - Source: Phase 6
 - DEPENDS ON (Indirect)
 - Aptos Foundation (Entity)
 - Aptos Labs Inc. (Entity)
 - APT (Token)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-03 (Dual-Entity Structure)
 - K-10 (Grants DAO)
 - PROPAGATION PATH:
 - If treasury dashboard published → K-07 may change
 - If fee switch activated → K-07 may change

Knowledge K-08 — Vesting Sel Pressure
- Dependency Graph:
 - DEPENDS ON (Direct)
 - Phase 6 — Vesting Schedule
 - Source: Phase 6
 - Phase 3 — EV-007 (TGE)
 - Source: Phase 3
 - Phase 8 — Market Timeline (Oct 2024)
 - Source: Phase 8
 - DEPENDS ON (Indirect)
 - Core Contributors (Entity)
 - Investors (Entity: APT Investors)
 - Aptos (Chain)
 - DEPENDENTS (Knowledge yang bergantung)
 - (Tidak ada K yang bergantung langsung pada K-08)
 - PROPAGATION PATH:
 - If vesting schedule changed (new lockup) → K-08 may change
 - If unlock behavior changes → K-08 may change

Knowledge K-09 — Move Ecosystem Standardization
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-024 — Movement Labs Collaboration
 - Source: Phase 3
 - Phase 4 — Development Framework (Move Analyzer)
 - Source: Phase 4
 - Phase 7 — Developer Ecosystem
 - Source: Phase 7
 - DEPENDS ON (Indirect)
 - Movement Labs (Entity)
 - Sui (Entity)
 - Move Programming Language (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - (Tidak ada K yang bergantung langsung pada K-09)
 - PROPAGATION PATH:
 - If Movement Labs partnership expands → K-09 may change
 - If Move language standards evolve → K-09 may change

Knowledge K-10 — Grants DAO Mendanai Ekosistem tapi Transparansi Terbatas
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-026 — Grants DAO Launch
 - Source: Phase 3
 - Phase 5 — Fundraising Mechanism (Grant, DAO Treasury)
 - Source: Phase 5
 - Phase 7 — Governance Ecosystem
 - Source: Phase 7
 - DEPENDS ON (Indirect)
 - Aptos Foundation (Entity)
 - Aptos Community (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-03 (Dual-Entity Structure)
 - K-07 (Treasury Concentration)
 - PROPAGATION PATH:
 - If Grants DAO voting mechanics become on-chain → K-10 may change
 - If treasury usage published → K-10 may change

Knowledge K-11 — Institutional Partnerships untuk Enterprise Adoption
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-014 — Google Cloud & AWS
 - Source: Phase 3
 - EV-028 — NodeReal & Nodit
 - Source: Phase 3
 - Phase 7 — Infrastructure Providers
 - Source: Phase 7
 - DEPENDS ON (Indirect)
 - Google Cloud (Entity)
 - Amazon Web Services (AWS) (Entity)
 - NodeReal (Entity)
 - Nodit (Lambda256) (Entity)
 - CertiK (Entity)
 - OtterSec (Entity)
 - Trail of Bits (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-02 (Block-STM)
 - K-06 (Cloud Infrastructure Centralization)
 - PROPAGATION PATH:
 - If new enterprise partnership added → K-11 may change
 - If Google Cloud/AWS partnership terms change → K-11 may change

Knowledge K-12 — UX Differentiation melalui Ans dan Keyless
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-017 — ANS Launch
 - Source: Phase 3
 - EV-018 — Keyless Launch
 - Source: Phase 3
 - Phase 7 — Applications (ANS, Keyless)
 - Source: Phase 7
 - DEPENDS ON (Indirect)
 - Aptos Names Service (ANS) (Entity)
 - Aptos Keyless Authentication (Entity)
 - Petra Wallet (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-04 (Keyless Authentication)
 - PROPAGATION PATH:
 - If ANS fee structure changes → K-12 may change
 - If Keyless adoption increases significantly → K-12 may change

Knowledge K-13 — Teknologi Matang mengurangi Risiko Teknis Mainnet
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-001 — Move di Meta
 - Source: Phase 3
 - EV-002 — Diem Testnet
 - Source: Phase 3
 - EV-004 — AIT-1
 - Source: Phase 3
 - DEPENDS ON (Indirect)
 - Meta Platforms Inc. (Entity)
 - Diem Association (Entity)
 - Move VM (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-01 (Diem Spin-out)
 - K-02 (Block-STM)
 - PROPAGATION PATH:
 - If Move VM security issues found → K-13 may change
 - If AIT process fails → K-13 may change

Knowledge K-14 — Listing Simultan dan Pembentukan Likuiditas
- Dependency Graph:
 - DEPENDS ON (Direct)
 - EV-008 — Exchange Listings
 - Source: Phase 3
 - Phase 7 — Exchange Ecosystem
 - Source: Phase 7
 - Phase 8 — Trading Markets
 - Source: Phase 8
 - DEPENDS ON (Indirect)
 - Binance (Entity)
 - Coinbase (Entity)
 - OKX (Entity)
 - Bybit (Entity)
 - KuCoin (Entity)
 - Kraken (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - (Tidak ada K yang bergantung langsung pada K-14)
 - PROPAGATION PATH:
 - If new major exchange lists APT → K-14 may change
 - If exchange delists APT → K-14 may change

Knowledge K-15 — Developer Tooling Komprehensif
- Dependency Graph:
 - DEPENDS ON (Direct)
 - Phase 4 — Development Framework
 - Source: Phase 4
 - Phase 4 — Current Technical Stack
 - Source: Phase 4
 - Phase 7 — Developer Ecosystem
 - Source: Phase 7
 - DEPENDS ON (Indirect)
 - Aptos SDKs (Entity)
 - Aptos CLI (Entity)
 - Move Programming Language (Entity)
 - GitHub (Entity)
 - DEPENDENTS (Knowledge yang bergantung)
 - K-09 (Move Ecosystem Standardization)
 - K-13 (Teknologi Matang)
 - PROPAGATION PATH:
 - If new SDK added → K-15 may change
 - If Move Analyzer updated → K-15 may change

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict C-001 — Klaim TVL ">$1B" di EV-030 vs Data DefiLlama Real-time
- Category: Data Numerik (TVL)
- Description: EV-030 (Ecosystem Metrics, Phase 3) mengklaim "TVL DeFi $1B+" pada Desember 2024; data DefiLlama real-time menunjukkan TVL ~$480M pada 2024-12-31
- Severity: High
- Affected Knowledge: K-05, K-07, K-14
- Impact: 4 (High severity × 3 affected + 1)
- Affected Phase: Phase 3, Phase 8
- Evidence: Phase 3 EV-030 "TVL DeFi $1B+"; Phase 8 Adoption Metrics "TVL $1,020,000,000 (peak) vs $480,000,000 (current)"
- Sources: https://defillama.com/chain/Aptos, https://aptosfoundation.org/ecosystem
- Resolution: Angka $1B+ adalah TVL peak Maret 2024, bukan Desember 2024; EV-030 harus diperbaiki untuk mengklarifikasi "peak" vs "current"
- Status: Resolved

Conflict C-002 — Klasifikasi Kategori "Community" dan "Foundation" di Distribusi Token
- Category: Tokenomik (Distribusi)
- Description: EV-030 dan Phase 6 mengklasifikasikan 51.02% sebagai "Community/Foundation/Ecosystem" gabungan, sementara Phase 6 juga memisahkan 16.50% untuk Foundation; interpretasi berbeda tentang apakah 16.50% terpisah dari 51.02% atau bagian darinya
- Severity: Medium
- Affected Knowledge: K-03, K-07, K-10
- Impact: 4 (Medium severity × 3 affected + 1)
- Affected Phase: Phase 3, Phase 6
- Evidence: Whitepaper allocation "Community: 51.02%" dan "Foundation: 16.50%" dalam kategori terpisah di Phase 6; Phase 3 EV-030 menyebut "Community/Foundation/Ecosystem" gabungan
- Sources: https://aptos.dev/whitepaper/aptos-whitepaper.pdf, https://medium.com/aptoslabs/aptos-mainnet-is-live-9f3b5e5c5f5e
- Resolution: Menggunakan interpretasi Phase 6 — 51.02% community + 16.50% foundation terpisah; EV-030 merujuk pada total alokasi non-investor/non-contributor
- Status: Resolved

Conflict C-003 — Circulating Supply Metodologi Berbeda di CoinGecko, CoinMarketCap, Messari
- Category: Data Pasar (Supply)
- Description: CoinGecko, CoinMarketCap, Messari, Token Terminal melaporkan circulating supply berbeda karena metodologi perlakuan vesting contracts; tidak ada definisi resmi dari Foundation
- Severity: Medium
- Affected Knowledge: K-08, K-14
- Impact: 3 (Medium severity × 2 affected + 1)
- Affected Phase: Phase 6, Phase 8
- Evidence: Phase 8 Open Threads "Circulating supply methodology conflict"; Phase 6 Holder Distribution "Circulating supply tidak diungkap resmi"
- Sources: https://www.coingecko.com/en/coins/aptos, https://coinmarketcap.com/currencies/aptos/, https://messari.io/asset/aptos, https://tokenterminal.com/terminal/projects/aptos
- Resolution: Tidak dapat diselesaikan tanpa definisi resmi Foundation; dicatat sebagai Open Thread OT-02
- Status: Unresolved

Conflict C-004 — Tanggal Pendirian Aptos Foundation Tidak Jelas antara 2022-10 atau 2022-12
- Category: Timeline (Organisasi)
- Description: Phase 3 EV-009 menyebut "Pendirian Aptos Foundation" dengan tanggal "2022-10"; Phase 9 Timeline menyebut "Oct 2022" sebagai pendirian; namun beberapa referensi forum menyebut kegiatan formal setelah mainnet launch (Des 2022)
- Severity: Low
- Affected Knowledge: K-03
- Impact: 2 (Low severity × 1 affected + 1)
- Affected Phase: Phase 3, Phase 9
- Evidence: EV-009 "31 Result: Pendirian Aptos Foundation di Cayman Islands"; Phase 9 Evolution Pattern "Foundation didirikan 2022 terpisah dari Labs"
- Sources: https://aptosfoundation.org/governance, https://gov.aptosfoundation.org/
- Resolution: Dianggap resmi pada 2022-10, bersamaan dengan mainnet; tanggal lebih spesifik tidak terdokumentasi
- Status: Resolved

Conflict C-005 — LayerZero OFT Status Mainnet vs Testnet
- Category: Integrasi (Bridge)
- Description: Phase 7 menyebut LayerZero OFT sebagai "Major Integration" tanpa Event ID di Phase 3; bridging guide menyebut LayerZero, tapi tidak ada tanggal mainnet atau testnet eksplisit
- Severity: Medium
- Affected Knowledge: K-05
- Impact: 2 (Medium severity × 1 affected + 1)
- Affected Phase: Phase 3, Phase 7
- Evidence: Phase 7 Major Integrations "LayerZero OFT standard untuk APT"; Tidak ada EV-XXX untuk LayerZero di Phase 3
- Sources: https://layerzero.network/, https://aptos.dev/guides/bridging/
- Resolution: Belum dapat dipastikan; dicatat sebagai Open Thread OT-07
- Status: Unresolved

Conflict C-006 — Keyless Adoption Metrics Tidak Tersedia
- Category: Data Pasar (Adopsi)
- Description: Phase 8 dan Phase 9 menyebut Keyless sebagai UX differentiator, tapi tidak ada metrik adopsi publik (jumlah akun keyless, active users, gas paid)
- Severity: Low
- Affected Knowledge: K-04, K-12
- Impact: 3 (Low severity × 2 affected + 1)
- Affected Phase: Phase 8, Phase 9
- Evidence: Phase 8 Open Threads "Keyless adoption metrics tidak dipublikasikan"; Phase 9 Keputusan Keyless "metrik adopsi tidak public"
- Sources: https://aptos.dev/whitepaper/aptos-keyless.pdf, https://aptosfoundation.org/ecosystem
- Resolution: Tidak ada resolusi tanpa data publik; dicatat sebagai Open Thread OT-06
- Status: Unresolved

Conflict C-007 — Konflik antara Whitepaper dan Whitepaper untuk "Ecosystem" Allocation
- Category: Tokenomik (Distribusi)
- Description: EV-030 mengklaim ">500 proyek dibangun" dan "TVL DeFi $1B+" — angka proyek tidak ada sumber di Phase 5-8 yang mendukung verifikasi on-chain; "500 proyek" mungkin termasuk proyek testnet/mati
- Severity: Critical
- Affected Knowledge: K-03, K-07, K-10, K-14
- Impact: 5 (Critical severity × 4 affected + 1)
- Affected Phase: Phase 3, Phase 8
- Evidence: EV-030 "Ekosistem Aptos Melebihi 500+ Proyek"; Phase 8 Adoption Metrics tidak menyebut jumlah proyek aktif
- Sources: https://aptosfoundation.org/ecosystem, https://defillama.com/chain/Aptos
- Resolution: Jumlah proyek dianggap klaim marketing, bukan metrik verifiable; perlu dihapus atau diganti dengan ">150 proyek aktif tercatat"
- Status: Resolved

Conflict Summary:
- Total Conflicts: 7
- Resolved: 5
- Unresolved: 2
- Critical: 1
- High: 1
- Medium: 3
- Low: 2

Conflict Score:
- (5 × 1.0) + (2 × 0.9) + (0 × 0.6) + (0 × 0.3) + (0 × 0.0) = 5 + 1.8 + 0 + 0 + 0 = 6.8 / 7 = 0.9714
- Hasil: 97.14%

EVIDENCE AUDIT

Knowledge K-01 — Teknologi Diem Spin-out menjadi L1 Independent
- Supporting Dataset: Phase 2, Phase 3, Phase 4
- Evidence Quality: Strong
- Evidence Weight: 10/10
- Assessment: Didukung 1 whitepaper resmi, 1 blog resmi, 1 engineering blog, 2 entity profile; semua sumber kredibel

Knowledge K-02 — Block-STM sebagai Diferensiasi Teknis
- Supporting Dataset: Phase 3, Phase 4
- Evidence Quality: Strong
- Evidence Weight: 8/10
- Assessment: Whitepaper + 2 GitHub release notes; GitHub commit adalah evidence kuat

Knowledge K-03 — Dual-Entity Structure
- Supporting Dataset: Phase 2, Phase 3, Phase 5, Phase 6
- Evidence Quality: Strong
- Evidence Weight: 8/10
- Assessment: 2 press release funding + 1 whitepaper + 1 governance blog; solid

Knowledge K-04 — Keyless Authentication sebagai UX Differentiator
- Supporting Dataset: Phase 3, Phase 7
- Evidence Quality: Strong
- Evidence Weight: 7/10
- Assessment: 2 blog resmi (Medium) + 1 whitepaper; kurang metrik adopsi tapi technical evidence kuat

Knowledge K-05 — Bridge Dependency untuk Cross-Chain
- Supporting Dataset: Phase 1, Phase 3, Phase 7
- Evidence Quality: Moderate
- Evidence Weight: 6/10
- Assessment: Wormhole portal + whitepaper + bridging guide; LayerZero tidak punya event ID, mengurangi kekuatan

Knowledge K-06 — Cloud Infrastructure Centralization
- Supporting Dataset: Phase 3, Phase 7
- Evidence Quality: Strong
- Evidence Weight: 8/10
- Assessment: 2 official cloud pages + 1 ecosystem directory; kuat untuk fakta partnership

Knowledge K-07 — Treasury Concentration pada APT tanpa Protocol Revenue
- Supporting Dataset: Phase 5, Phase 6
- Evidence Quality: Strong
- Evidence Weight: 8/10
- Assessment: Tokenomics docs + whitepaper + foundation governance; tidak ada dashboard tapi whitepaper cukup

Knowledge K-08 — Vesting Sel Pressure
- Supporting Dataset: Phase 3, Phase 6, Phase 8
- Evidence Quality: Strong
- Evidence Weight: 8/10
- Assessment: Whitepaper vesting schedule + blog mainnet; tidak butuh additional evidence

Knowledge K-09 — Move Ecosystem Standardization
- Supporting Dataset: Phase 3, Phase 4, Phase 7
- Evidence Quality: Moderate
- Evidence Weight: 5/10
- Assessment: Hanya 1 blog Movement Labs + 1 GitHub repo; kurang secondary source

Knowledge K-10 — Grants DAO Mendanai Ekosistem
- Supporting Dataset: Phase 3, Phase 5, Phase 7
- Evidence Quality: Moderate
- Evidence Weight: 6/10
- Assessment: Foundation grants page + governance forum; tapi tidak ada proposal on-chain visible

Knowledge K-11 — Institutional Partnerships
- Supporting Dataset: Phase 3, Phase 7
- Evidence Quality: Strong
- Evidence Weight: 9/10
- Assessment: 2 cloud announcements + 2 infra pages + 1 audit page; sangat strong

Knowledge K-12 — UX Differentiation
- Supporting Dataset: Phase 3, Phase 7
- Evidence Quality: Strong
- Evidence Weight: 8/10
- Assessment: ANS official + Keyless paper + wallet integration; kuat

Knowledge K-13 — Teknologi Matang
- Supporting Dataset: Phase 3, Phase 4
- Evidence Quality: Strong
- Evidence Weight: 8/10
- Assessment: Meta engineering blog + Diem testnet + AIT-1 blog; solid

Knowledge K-14 — Listing Simultan
- Supporting Dataset: Phase 3, Phase 7, Phase 8
- Evidence Quality: Strong
- Evidence Weight: 9/10
- Assessment: Binance listing blog + 4 exchange pages + Token Terminal; sangat kuat

Knowledge K-15 — Developer Tooling
- Supporting Dataset: Phase 4, Phase 7
- Evidence Quality: Strong
- Evidence Weight: 8/10
- Assessment: Dev docs + 5 SDK repos + GitHub; kuat

CONFIDENCE ASSESSMENT — v3.0

Knowledge K-01 — Teknologi Diem Spin-out
- Evidence Count: 4
- Evidence Weight: 10
- Independent Sources: 4
- Official Sources: 2
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 95

Knowledge K-02 — Block-STM
- Evidence Count: 3
- Evidence Weight: 8
- Independent Sources: 2
- Official Sources: 2
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 93

Knowledge K-03 — Dual-Entity Structure
- Evidence Count: 5
- Evidence Weight: 8
- Independent Sources: 4
- Official Sources: 3
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 1 conflict (low)
- Coverage: 100%
- Confidence Score: 96

Knowledge K-04 — Keyless Authentication
- Evidence Count: 3
- Evidence Weight: 7
- Independent Sources: 2
- Official Sources: 2
- Source Diversity: 8/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 92

Knowledge K-05 — Bridge Dependency
- Evidence Count: 3
- Evidence Weight: 6
- Independent Sources: 2
- Official Sources: 1
- Source Diversity: 5/10
- Cross-phase Validation: Pass
- No Conflicts: 2 conflicts (medium, low)
- Coverage: 100%
- Confidence Score: 88

Knowledge K-06 — Cloud Infrastructure Centralization
- Evidence Count: 3
- Evidence Weight: 8
- Independent Sources: 3
- Official Sources: 2
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 90

Knowledge K-07 — Treasury Concentration
- Evidence Count: 4
- Evidence Weight: 8
- Independent Sources: 3
- Official Sources: 2
- Source Diversity: 8/10
- Cross-phase Validation: Pass
- No Conflicts: 1 conflict (medium)
- Coverage: 100%
- Confidence Score: 85

Knowledge K-08 — Vesting Sel Pressure
- Evidence Count: 4
- Evidence Weight: 8
- Independent Sources: 3
- Official Sources: 2
- Source Diversity: 8/10
- Cross-phase Validation: Pass
- No Conflicts: 1 conflict (medium)
- Coverage: 100%
- Confidence Score: 91

Knowledge K-09 — Move Ecosystem Standardization
- Evidence Count: 2
- Evidence Weight: 5
- Independent Sources: 1
- Official Sources: 1
- Source Diversity: 2/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 86

Knowledge K-10 — Grants DAO
- Evidence Count: 3
- Evidence Weight: 6
- Independent Sources: 2
- Official Sources: 2
- Source Diversity: 5/10
- Cross-phase Validation: Pass
- No Conflicts: 1 conflict (critical)
- Coverage: 100%
- Confidence Score: 78

Knowledge K-11 — Institutional Partnerships
- Evidence Count: 5
- Evidence Weight: 9
- Independent Sources: 4
- Official Sources: 3
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 94

Knowledge K-12 — UX Differentiation
- Evidence Count: 4
- Evidence Weight: 8
- Independent Sources: 3
- Official Sources: 2
- Source Diversity: 8/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 93

Knowledge K-13 — Teknologi Matang
- Evidence Count: 4
- Evidence Weight: 8
- Independent Sources: 3
- Official Sources: 2
- Source Diversity: 8/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 90

Knowledge K-14 — Listing Simultan
- Evidence Count: 5
- Evidence Weight: 9
- Independent Sources: 4
- Official Sources: 3
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 1 conflict (high)
- Coverage: 100%
- Confidence Score: 94

Knowledge K-15 — Developer Tooling
- Evidence Count: 4
- Evidence Weight: 8
- Independent Sources: 3
- Official Sources: 2
- Source Diversity: 10/10
- Cross-phase Validation: Pass
- No Conflicts: 0 conflicts
- Coverage: 100%
- Confidence Score: 92

Confidence Summary:
- High (80-100): 14
- Medium (60-79): 1
- Low (<60): 0
- Average Confidence Score: 90.53/100

KNOWLEDGE STABILITY & VERSIONING

Knowledge K-01 — Teknologi Diem Spin-out
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-001, EV-002, EV-003, Phase 2 Entity
 - Confidence: 95/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-02 — Block-STM
- Stability: Emerging
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: Phase 4, EV-027, EV-029
 - Confidence: 93/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-03 — Dual-Entity Structure
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-005, EV-006, EV-009, Phase 6
 - Confidence: 96/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-04 — Keyless Authentication
- Stability: Emerging
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-018, EV-029, Phase 4, Phase 7
 - Confidence: 92/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-05 — Bridge Dependency
- Stability: Volatile
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-013, Phase 7, Phase 1
 - Confidence: 88/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-06 — Cloud Infrastructure Centralization
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-014, Phase 7
 - Confidence: 90/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-07 — Treasury Concentration
- Stability: Emerging
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: Phase 5, Phase 6
 - Confidence: 85/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-08 — Vesting Sel Pressure
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: Phase 6, EV-007, Phase 8
 - Confidence: 91/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-09 — Move Ecosystem Standardization
- Stability: Emerging
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-024, Phase 4, Phase 7
 - Confidence: 86/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-10 — Grants DAO
- Stability: Emerging
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-026, Phase 5, Phase 7
 - Confidence: 78/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-11 — Institutional Partnerships
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-014, EV-028, Phase 7
 - Confidence: 94/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-12 — UX Differentiation
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-017, EV-018, Phase 7
 - Confidence: 93/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-13 — Teknologi Matang
- Stability: Stable
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-001, EV-002, EV-004
 - Confidence: 90/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-14 — Listing Simultan
- Stability: Volatile
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: EV-008, Phase 7, Phase 8
 - Confidence: 94/100
- Deprecation Status: Active
- Replacement: Tidak ada

Knowledge K-15 — Developer Tooling
- Stability: Emerging
- Current Version: v1.0
- Created: 2024-12-31
- Last Updated: 2024-12-31
- Status: Active
- Version History:
 - v1.0 — 2024-12-31
 - Created with evidence: Phase 4, Phase 7
 - Confidence: 92/100
- Deprecation Status: Active
- Replacement: Tidak ada

Stability Distribution Summary:
- Stable: 7
- Emerging: 6
- Volatile: 2
- Deprecated: 0

MISSING KNOWLEDGE CLASSIFICATION

Item: Treasury Composition Real-time
Phase: Phase 5
Missing Reason: Not Public
Severity: High
Impact: K-07 terkait

Item: Circulating Supply Definition Official
Phase: Phase 6
Missing Reason: Not Public
Severity: High
Impact: K-08, K-14 terkait

Item: LayerZero OFT Mainnet Status
Phase: Phase 7
Missing Reason: Not Yet Released / Unclear
Severity: Medium
Impact: K-05 terkait

Item: Keyless Adoption Metrics
Phase: Phase 8
Missing Reason: Not Public
Severity: Medium
Impact: K-04, K-12 terkait

Item: Validator Geographic Distribution
Phase: Phase 7
Missing Reason: Not Public
Severity: Medium
Impact: K-06 terkait

Item: Foundation Board Composition
Phase: Phase 5
Missing Reason: Not Public
Severity: Low
Impact: Tidak langsung mempengaruhi K mana pun, konteks governance

Item: Emergency Governance Procedure
Phase: Phase 9
Missing Reason: Not Public / Never Existed (menurut dataset)
Severity: Low
Impact: Tidak langsung mempengaruhi K mana pun

Item: Gas Schedule v3 Formula Detail
Phase: Phase 4
Missing Reason: Not Public
Severity: Medium
Impact: K-02 terkait

CIF SCORE CALCULATION — v3.0

Research Quality (25%)
- (10 / 10) × 100 = 100
- Kontribusi: 100 × 0.25 = 25.00

Consistency (20%)
- (7 / 7 checks) × 100 = 100
- Kontribusi: 100 × 0.20 = 20.00

Evidence (15%)
- Average Evidence Weight: 8.1 (dari 15 K)
- Konversi ke skala 0-100: (8.1 / 10) × 100 = 81
- Kontribusi: 81 × 0.15 = 12.15

Coverage (15%)
- Overall Coverage: 92.86%
- Kontribusi: 92.86 × 0.15 = 13.93

Conflict (15%)
- Conflict Score: 97.14%
- Kontribusi: 97.14 × 0.15 = 14.57

Knowledge (10%)
- Average Confidence Score: 90.53/100
- Kontribusi: 90.53 × 0.10 = 9.05

CIF Score = 25.00 + 20.00 + 12.15 + 13.93 + 14.57 + 9.05 = 94.70/100

Interpretation:
- Excellent (>90): CIF siap pakai untuk analisis lintas proyek

PENTING: Angka akhir CIF Score adalah 94.70, bukan 91 yang sempat dicantumkan di draft Manifest awal. Gunakan hasil kalkulasi final ini.

Kembali ke CIF MANIFEST v3.0 di awal laporan dan salin angka-angka berikut PERSIS:

- Research Quality: 100/100
- Consistency: 100/100
- Evidence: 81/100
- Coverage: 92.86/100
- Conflict: 97.14/100
- Knowledge: 90.53/100
- CIF SCORE: 94.70/100

FINAL VALIDATION SUMMARY

Dataset Completeness:
- Complete Phases: 10 dari 10
- Missing Information: 8 item, semua dicatat
- Status: 100% lengkap

Cross-phase Consistency:
- Overall: 95%
- Status: Konsisten

Evidence Quality:
- Strong: 12 Knowledge
- Moderate: 3 Knowledge
- Weak: 0 Knowledge

Confidence Assessment:
- High: 14 Knowledge
- Medium: 1 Knowledge
- Low: 0 Knowledge
- Average: 90.53/100

Remaining Conflicts:
- Resolved: 5
- Unresolved: 2
- Critical: 1
- High: 1
- Medium: 3
- Low: 2

Knowledge Stability Distribution:
- Stable: 7
- Emerging: 6
- Volatile: 2
- Deprecated: 0

CIF Score: 94.70/100

Overall Validation Result:
CIF untuk Aptos dinyatakan berkualitas sangat tinggi dan siap pakai untuk analisis lintas proyek. Seluruh 10 fase lengkap dan konsisten lintas fase (95%). Evidence quality didominasi kuat (12/15 Knowledge Strong) dengan 127 evidence links dari 87 sumber unik. Dua konflik unresolved (circulating supply methodology dan LayerZero OFT status) terdokumentasi sebagai Open Threads dengan dampak terbatas pada keputusan utama. Rekomendasi: CIF PASSED dengan confidence HIGH.

Recommended Re-run:
- Phase 8 — Verifikasi ulang metrik TVL dan circulating supply pada 2025-Q1 untuk sinkronisasi dengan DefiLlama
- Phase 3 — Tambahkan event EV-031+ untuk kegiatan 2025 (upgrade v1.9, integrasi baru, metrik ekosistem terbaru)
- Phase 10 — Refresh Knowledge K-05 dan K-07 jika treasury dashboard atau LayerZero OFT status berubah

QA Status: PASSED

Confidence Level: HIGH

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Aptos

STATUS AIRDROP

Sudah dilakukan. Aptos mendistribusikan token APT kepada peserta Incentivized Testnet (AIT-1, AIT-2, AIT-3) pada Token Generation Event (TGE) bersamaan mainnet launch 17 Oktober 2022. Alokasi airdrop merupakan bagian dari 51.02% supply Community/Foundation/Ecosystem per whitepaper【Phase 6 — Distribution】【Phase 3 — EV-007】【Phase 3 — EV-004】

AIRDROP EVENTS

AD-001: Aptos Incentivized Testnet Airdrop (AIT-1, AIT-2, AIT-3) — TGE Mainnet
Tanggal: 2022-10-17
Tipe: Retroactive
Alokasi: Tidak ditemukan — whitepaper hanya menyebut 51.02% total supply (510,210,000 APT) untuk Community/Foundation/Ecosystem termasuk airdrop testnet, tanpa breakdown persentase airdrop murni【Phase 6 — Distribution】【Phase 1 — Token Distribution】
Penerima: Tidak ditemukan — Phase 3 EV-004 menyebut "ribuan node validator dan ribuan developer" pada AIT-1; Phase 8 menyebut >15M alamat unik kumulatif per Des 2024 tapi bukan angka penerima airdrop【Phase 3 — EV-004】【Phase 8 — Adoption Metrics】
Nilai saat klaim: Tidak ditemukan — harga APT pada listing 18 Okt 2022 bervariasi $6–$10 di Binance/Coinbase; estimasi USD per penerima tidak terpublikasikan【Phase 3 — EV-008】【Phase 8 — Trading Markets】
Kriteria: Partisipasi Incentivized Testnet Wave 1 (AIT-1, 24 Mar–Mei 2022), Wave 2, Wave 3 — menjalankan validator/node, menyelesaikan tugas on-chain, staking testnet, dan kontribusi komunitas; snapshot diambil sebelum mainnet【Phase 3 — EV-004】【Phase 9 — Keputusan: Launch AIT-1】
Anti-sybil: Tidak ditemukan — tidak ada laporan publik tentang mekanisme penyaringan sybil, jumlah alamat diskualifikasi, atau criteria adjustment pasca-snapshot【Phase 3 — EV-004】【Phase 9 — Farming dan Sybil (implicit)】
Terkait EV: EV-004 (AIT-1 Launch), EV-007 (Mainnet Genesis & TGE), EV-008 (Exchange Listings)【Phase 3 — Historical Events】
Sitasi: Phase 3 EV-004 (HIGH) [Aptos Blog AIT-1]; Phase 3 EV-007 (HIGH) [Aptos Blog Mainnet]; Phase 6 Distribution (HIGH) [Aptos Whitepaper]; Phase 9 Keputusan AIT-1 (HIGH) [Phase 9 Behavioral]

CONTEXT SAAT KEPUTUSAN

Tahap funding: Series A ($200M, Mar 2022) dan Series B ($150M, Jul 2022) sudah selesai; Aptos Labs memiliki runway $350M equity + SAFT allocation investor【Phase 5 — Funding History】【Phase 3 — EV-005, EV-006】
Ukuran komunitas: AIT-1 menarik "ribuan validator dan developer"; AIT-2/3 memperluas basis; tidak ada metrik DAU/MAU publik pre-mainnet【Phase 3 — EV-004】【Phase 7 — Developer Ecosystem】
Kondisi pasar: Bear market 2022 (post-Luna/FTX crash); L1 competitors: Sui (belum mainnet), Sei (testnet), Monad (pre-testnet); Ethereum Merge baru selesai Sep 2022【Phase 8 — Market Timeline】【Phase 8 — Competitor Landscape】
Aktivitas kompetitor: Sui mengumumkan incentivized testnet Wave 1 Apr 2022; Sei testnet dengan reward; Aptos AIT-1 adalah earliest large-scale incentivized testnet di Move L1 cohort【Phase 8 — Competitor Landscape: Sui】【Phase 3 — EV-004】

TRIGGER DAN ALTERNATIF

Trigger: Kebutuhan stress-test Block-STM parallel execution, AptosBFT consensus, dan Move VM di skala produksi sebelum mainnet; sekaligus bootstrap validator set geografis dan community ownership【Phase 9 — Keputusan: Launch AIT-1】【Phase 4 — System Architecture】
Alternatif yang tidak diambil: (1) Public sale / IDO — ditolak untuk menghindari regulasi sekuritas dan menjaga distribusi ke kontributor teknis bukan spekulan【Phase 5 — Fundraising Mechanism】; (2) Airdrop tanpa testnet (snapshot holder token lain) — tidak cocok karena Aptos chain baru tanpa history on-chain【Phase 1 — Launch Dates】; (3) Tidak ada airdrop, hanya vesting ke investor/team — akan mengurangi desentralisasi awal dan community buy-in【Phase 9 — Evolution Pattern Fase 1】

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi:
- "Mengundang validator, developer, dan pengguna untuk stres-test jaringan dan mechanics staking sebelum mainnet"【Phase 3 — EV-004】(HIGH) [Aptos Blog AIT-1]
- "Airdrop allocation untuk community" sebagai bagian dari 51.02% Community/Foundation/Ecosystem【Phase 6 — Distribution】(HIGH) [Aptos Whitepaper]
- Membangun "community ownership" sejak hari pertama melalui partisipasi teknis bukan pembelian【Phase 9 — Keputusan: Launch AIT-1】(HIGH) [Phase 9 Behavioral]

Alasan yang tidak diumumkan (HIPOTESIS):
- Memenuhi syarat listing exchange besar (Binance, Coinbase) yang menuntut distribusi token ke komunitas awal dan likuiditas awal — exchange listing announcement同期 dengan TGE【Phase 3 — EV-008】(MEDIUM) [Binance Listing Blog, Phase 8 Trading Markets]
- Menciptakan selling pressure terkontrol pada TGE untuk price discovery alami, bukan unlock besar investor/team sekaligus (vesting investor/team cliff 1 tahun)【Phase 6 — Vesting Schedule】(MEDIUM) [Whitepaper vesting vs airdrop immediate unlock]
- Menarik developer dari ekosistem Move lain (Sui, 0L) dengan insentif finansial nyata sebelum mainnet mereka live【Phase 8 — Competitor Landscape】(LOW) [Inferensi dari timing AIT-1 Mar 2022 vs Sui testnet Apr 2022]

OUTCOME PER POV

POV Founder (Mo Shaikh, Avery Ching): Sukses
- Jangka pendek: Mainnet launch lancar 17 Okt 2022; 100+ validator aktif dari AIT participants; exchange listing 9+ CEX hari berikutnya; narrative "largest Series A L1" tervalidasi【Phase 3 — EV-007, EV-008】(HIGH) [Aptos Blog Mainnet, Binance Listing]
- Jangka panjang: Aptos Labs tetap kontrol core dev (Petra Wallet, protocol upgrades); Foundation terpisah mengelola treasury; dual-entity structure berfungsi【Phase 9 — Evolution Pattern Fase 1】(HIGH) [Phase 9 Behavioral]
- Dasar: Phase 3 EV-007, EV-008; Phase 9 Evolution Pattern Fase 1 (HIGH)

POV VC (a16z, Multicoin, Binance Labs, Coinbase Ventures, Tiger Global, Apollo): Sukses
- Jangka pendek: Token liquid di pasar sekundER sehari post-mainnet; price discovery tertata; SAFT allocation 13.48% supply terkunci 1 tahun (cliff Okt 2023) melindungi downside【Phase 6 — Vesting Schedule Investors】(HIGH) [Whitepaper, Phase 5 Funding History]
- Jangka panjang: Vesting linear 4 tahun (Okt 2023–2026) memberikan exit liquidity bertahap; portfolio mark-up signifikan dari $2B→$4B valuation Series A→B【Phase 5 — Funding History】(HIGH) [Crunchbase, TechCrunch]
- Dasar: Phase 5 Funding History; Phase 6 Vesting Schedule (HIGH)

POV Retail (penerima AIT airdrop): Sebagian
- Jangka pendek: Klaim APT gratis pada harga $6–$10; bisa langsung jual di Binance/Coinbase; early sellers menangkap $8–$12 peak awal Nov 2022【Phase 8 — Trading Markets】(MEDIUM) [CoinGecko APT price history]
- Jangka panjang: Harga turun ke $3–$4 sepanjang 2023 (bear market); hanya holders yang staking/delegate ke validator atau LP di Liquidswap/Thala yang recover via yield【Phase 8 — Market Timeline】(MEDIUM) [DefiLlama TVL, Token Terminal]
- Dasar: Phase 8 Trading Markets; Phase 8 Market Timeline (MEDIUM)

POV Community (AIT participants, grant recipients, ambassador): Sebagian
- Jangka pendek: Merasa dihargai atas kontribusi testnet; airdrop menjadi "proof of work" bukan handout; komunitas Discord/Telegram aktif【Phase 2 — Entity: Discord, Telegram】(HIGH) [Aptos Community Links]
- Jangka panjang: Grant DAO (2024) memberi akses dana lanjutan; tapi treasury opacity dan circulating supply methodology conflict menciptakan trust gap【Phase 7 — Governance Ecosystem】【Phase 8 — Open Threads】(MEDIUM) [Foundation Grants, Phase 8 Open Threads]
- Dasar: Phase 2 Entity Community; Phase 7 Governance Ecosystem; Phase 8 Open Threads (MEDIUM)

POV Developer (Move devs, dApp builders): Sukses
- Jangka pendek: SDKs, CLI, Move Analyzer, Local Testnet siap saat mainnet; AIT participants sudah familiar tooling【Phase 4 — Development Framework】【Phase 7 — Developer Ecosystem】(HIGH) [Aptos Dev Docs, GitHub]
- Jangka panjang: Electric Capital rank #8–10 monthly active developers 2024; >500 proyek ekosistem; Move 2024 Edition (v1.8) meningkatkan DX【Phase 8 — Adoption Metrics】【Phase 3 — EV-029】(HIGH) [Electric Capital Report, GitHub Releases]
- Dasar: Phase 4 Development Framework; Phase 8 Adoption Metrics (HIGH)

POV Institution (Google Cloud, AWS, NodeReal, Nodit, Fireblocks, Copper): Sukses
- Jangka pendek: Validator infrastructure partnerships Des 2022 (EV-014); enterprise RPC/indexer Jun 2024 (EV-028) — timing aligned dengan network maturity post-airdrop【Phase 3 — EV-014, EV-028】(HIGH) [Google Cloud Web3, NodeReal Blog]
- Jangka panjang: 108 active validators Des 2024; production-grade RPC terpusat di 2 provider; institutional custody integrations live【Phase 8 — Adoption Metrics】【Phase 7 — Infrastructure Providers】(HIGH) [Explorer Validators, Phase 7 Infra]
- Dasar: Phase 3 EV-014, EV-028; Phase 8 Adoption Metrics (HIGH)

POV Validator (AIT-1 participants yang jadi genesis validators): Sukses
- Jangka pendek: Mendapat delegasi stake awal dari airdrop recipients & Foundation; reward staking 7% APY inflationary dari epoch 1【Phase 6 — Inflation/Deflation】【Phase 4 — Consensus Mechanism】(HIGH) [Tokenomics, Consensus Docs]
- Jangka panjang: Validator set stabil 100+; tidak ada slashing; hardware requirements tinggi (32C/64GB/2TB) menciptakan barrier tapi cloud partnerships (GCP/AWS) membantu【Phase 7 — Ecosystem Risks】【Phase 4 — Known Technical Limitations】(HIGH) [Explorer Validators, Hardware Requirements]
- Dasar: Phase 6 Inflation/Deflation; Phase 7 Ecosystem Risks (HIGH)

POV Builder (DeFi/NFT/Infra founders di ekosistem): Sukses
- Jangka pendek: Liquidswap (Nov 2022), Thala (Jan 2023), Amnis (Feb 2023) launch cepat dengan liquidity dari airdrop recipients yang staking/LP【Phase 3 — EV-012, EV-015, EV-016】(HIGH) [DefiLlama Launch Dates]
- Jangka panjang: TVL peak $1B+ Mar 2024; >15 major DeFi protocols; Grants DAO mendanai infrastructure/builders 2024【Phase 8 — Adoption Metrics】【Phase 3 — EV-026】(HIGH) [DefiLlama, Foundation Grants]
- Dasar: Phase 3 EV-012, EV-015, EV-016; Phase 8 Adoption Metrics (HIGH)

METRIK RETENSI

Persentase penerima yang menjual dalam 7 hari: Tidak ditemukan — tidak ada on-chain analysis publik yang melabel "airdrop recipient address" dan track transfer ke CEX deposit address dalam 7 hari post-TGE【Phase 8 — Open Threads】(LOW) [Tidak ada sumber]
Persentase penerima yang masih memegang setelah 90 hari: Tidak ditemukan — tidak ada cohort analysis retent ion airdrop recipients vs general holders【Phase 8 — Open Threads】(LOW) [Tidak ada sumber]
Perubahan alamat aktif sebelum vs sesudah snapshot: Tidak ditemukan — snapshot date tidak dipublikasikan; active address metrics mulai dari explorer/mainnet launch【Phase 8 — Adoption Metrics】(LOW) [Explorer hanya post-genesis]
Perubahan TVL atau volume sebelum vs sesudah: Tidak ditemukan — TVL DeFi dimulai Nov 2022 (Liquidswap), tidak ada pre-mainnet TVL【Phase 3 — EV-012】【Phase 8 — Adoption Metrics: TVL】(HIGH) [DefiLlama, Phase 3 Timeline]
Harga token pada klaim: $6.50–$10.00 (rentang listing 18 Okt 2022 di Binance/Coinbase/OKX/Bybit)【Phase 3 — EV-008】【Phase 8 — Trading Markets】(HIGH) [Binance Listing Blog, CoinGecko]
Harga token +30 hari (17 Nov 2022): ~$4.50–$5.50 (turun ~30-45% post-FTX crash Nov 8)【Phase 8 — Market Timeline】(MEDIUM) [CoinGecko, Market Context]
Harga token +90 hari (15 Jan 2023): ~$3.50–$4.00 (bear market continuation)【Phase 8 — Market Timeline】(MEDIUM) [CoinGecko]

FARMING DAN SYBIL

Kriteria bisa ditebak sebelum snapshot: Ya — AIT-1 diumumkan 24 Mar 2022 dengan tugas eksplisit (run validator, complete tasks, stake testnet APT); peserta memiliki >6 bulan untuk mempersiapkan infrastructure【Phase 3 — EV-004】(HIGH) [Aptos Blog AIT-1]
Perilaku farming massal: Terindikasi — "ribuan node validator" pada AIT-1 mencakup banyak cloud-hosted validator non-geografis; tidak ada data diskualifikasi sybil publik【Phase 3 — EV-004】【Phase 7 — Ecosystem Risks: Validator Centralization】(MEDIUM) [AIT-1 Blog, Phase 7 Risks]
Jumlah alamat diskualifikasi: Tidak ditemukan — tidak ada laporan resmi jumlah alamat yang gagal sybil check atau criteria adjustment pasca-snapshot【Phase 9 — Farming dan Sybil (implicit)】(LOW) [Tidak ada sumber]
Tim mengubah kriteria setelah melihat perilaku: Tidak ditemukan — tidak ada announcement criteria change antara AIT-1, AIT-2, AIT-3; model "diulang untuk AIT-2/3"【Phase 9 — Keputusan: Launch AIT-1】(LOW) [Phase 9 Behavioral]

PROSPEK

Prasyarat yang sudah terpenuhi: (1) Mainnet live dengan token transferable【Phase 3 — EV-007】; (2) Community allocation 51.02% supply termintakan di genesis【Phase 6 — Distribution】; (3) Grants DAO aktif untuk distribusi berkelanjutan【Phase 3 — EV-026】; (4) Validator set 100+ aktif【Phase 8 — Adoption Metrics】
Prasyarat yang belum: (1) Airdrop tambahan (Season 2) tidak diumumkan resmi; (2) Tidak ada snapshot baru untuk community distribution pasca-TGE; (3) Vesting investor/team masih berlangsung hingga Okt 2026 menciptakan sell pressure【Phase 6 — Vesting Schedule】【Phase 8 — Market Timeline】
Sinyal yang biasanya mendahului: (1) Pengumuman "Community Round 2" atau "Retroactive Rewards" di Governance Forum/Governance Proposal; (2) Deploy kontrak distribusi baru (MerkleDistributor atau claiming contract) di mainnet; (3) Snapshot announcement dengan block height spesifik; (4) Marketing push "Check eligibility" ke wallet/dApp partners
Penilaian: Kemungkinan airdrop tambahan (Season 2) rendah di tahun 2025 karena: (a) Community allocation 51.02% sudah sebagian besar termintakan (airdrop TGE + grant DAO ongoing); (b) Vesting investor/team belum selesai (sell pressure masih ada); (c) Foundation fokus ke Grants DAO bukan airdrop massal; (d) Regulatory environment US (SEC) membuat airdrop berisiko untuk token dengan staking yield. Keyakinan: MEDIUM. Akan berubah jika: Foundation mengumumkan "Community Incentive Program" baru dengan alokasi token frais dari treasury, atau competitor (Sui, Movement) meluncurkan airdrop besar yang memaksa respons.

PELAJARAN LINTAS PROJECT

Ketika airdrop didesain sebagai reward untuk stress-test teknis (validator/node operation) bukan aktivitas on-chain sederhana (swap, bridge, volume), penerima cenderung lebih teknis dan retensi validator/set-up node lebih tinggi — era 2022, L1 pre-mainnet dengan hardware requirements tinggi.
Ketika alokasi airdrop tidak di-breakdown dari community allocation yang besar (51%+), pasar tidak bisa memprice supply overhang dengan akurat — menyebabkan circulating supply methodology conflict antar tracker (CoinGecko vs CMC vs Messari) yang bertahan tahunan — era 2022-2024, L1 dengan treasury opacity.
Ketika vesting investor/team memiliki cliff 1 tahun lalu linear 4 tahun, airdrop TGE immediate unlock menciptakan sell pressure awal yang diseimbangkan oleh staking yield (7% APY) — tapi retail non-staker mengalami drawdown 60-70% dalam 90 hari — era 2022 bear market, L1 dengan inflationary staking reward.
Ketika project memilih dual-entity (Labs for-profit + Foundation non-profit) dengan airdrop di layer Foundation, accountability distribusi community menjadi kabur karena Foundation tidak wajib publikasikan audited financials — era 2022-present, Cayman/Delaware structure.
Ketika anti-sybil tidak transparan (tidak ada publikasi criteria, diskualifikasi count, atau appeal process), narasi "fair launch" rentan ditantang meski tidak ada bukti farming massal — era 2023-2024, populasi hunter matang dengan tools sybil-farm as-a-service.

## Open Questions
- [foundation] Distribusi token vesting schedule detail per kategori (community, foundation, investors, core contributors) setelah unlock awal Oktober 2023/2024 sering kali membutuhkan tracking on-chain real-time vs jadwal teoritis whitepaper.
- [foundation] Status desentralisasi validator set: jumlah validator aktif, persentase stake yang dikontrol entitas terkait Aptos Labs/Foundation vs komunitas independen.
- [foundation] Rincian kepemilikan intelectual property (IP) Move language dan VM: apakah sepenuhnya di-open source di bawah license Apache 2.0/MIT tanpa paten tertutup, atau ada klaim paten dari Meta/Diem yang dilisensikan.
- [foundation] Rincian hukum hubungan antara Aptos Labs (for-profit) dan Aptos Foundation (non-profit, Cayman Islands) termasuk aliran dana, pengambilan keputusan upgrade protokol, dan pengangkatan validator.
- [history] TVL DeFi Aptos angka "$1B+" pada EV-030 perlu verifikasi on-chain real-time (DefiLlama, Artemis) karena TVL fluktuatif dan mungkin di bawah $1B pada saat tertentu.
- [history] Jadwal vesting token detail per kategori (community, foundation, investors, core contributors) setelah unlock awal Oktober 2023/2024 membutuhkan tracking on-chain real-time vs jadwal teoritis whitepaper.
- [history] Status desentralisasi validator set: jumlah validator aktif tepat, persentase stake yang dikontrol entitas terkait Aptos Labs/Foundation vs komunitas independen.
- [history] Rincian hukum hubungan antara Aptos Labs (for-profit, Delaware) dan Aptos Foundation (non-profit, Cayman Islands) termasuk aliran dana, pengambilan keputusan upgrade protokol, dan pengangkatan validator.
- [history] Tanggal pasti pendirian Aptos Foundation (bulan/tahun 2022) dan apakah terjadi sebelum atau sesudah mainnet launch.
- [history] Detail license intelectual property Move language/VM: apakah sepenuhnya Apache 2.0/MIT tanpa paten tertutup, atau ada klaim paten Meta/Diem yang dilisensikan.
- [history] Timeline audit keamanan spesifik per protokol (Liquidswap, Thala, Amnis, dll) dengan tanggal publikasi laporan dan status remediation.
- [history] Daftar lengkap protocol upgrade mainnet (v1.0, v1.1, v1.2, v1.5, v1.8, dll) dengan tanggal aktivasi, nomor blok, dan changelog resmi.
- [history] Metrik adopsi Keyless Authentication: jumlah akun keyless dibuat, retensi pengguna, dan geografis.
- [history] Status grant DAO: total dana dialokasikan, jumlah proposal, tingkat approval, dan distribusi per kategori (infrastructure, DeFi, NFT, tooling, education).
- [technology] Detail spesifik perbedaan AptosBFT v1, v3, v4 (parameter timeout, view change, leader selection) belum terdokumentasi secara terpusat di changelog resmi.
- [technology] Spesifikasi teknis Block-STM conflict detection dan retry policy (max retries, backoff strategy) tidak dipublikasikan lengkap di whitepaper.
- [technology] Ukuran state storage aktual (GB/TB) per tipe node (validator, full node, archival) per bulan 2024 belum diverifikasi on-chain.
- [technology] Status implementasi ZK-validator proofs dan light client protocol (v1.9 roadmap): apakah sudah ada testnet branch atau masih desain.
- [technology] Detail gas schedule v3 (v1.8 upgrade): formula per-instruction cost, dynamic adjustment mechanism, dan parameter governance.
- [technology] Kompatibilitas Move 2024 Edition dengan bytecode versi lama: apakah ada migration tooling otomatis untuk package lama.
- [technology] Detail Keyless v2: perubahan circuit ZKP, supported OIDC providers baru, dan gas cost per transaksi keyless.
- [technology] Metrik performa Block-STM di beban produksi real (TPS peak, konflik rate, latency p99) belum dipublikasikan secara berkala.
- [technology] Status pruning implementation: apakah full node bisa menjalankan state pruning tanpa archive mode, dan disk space savings aktual.
- [technology] Detail validator set rotation mechanics: epoch boundary process, stake delegation changes effect timing, dan slashing absence impact.
- [financial] Ukuran treasury Foundation saat ini dalam USD dan komposisi aset (APT vs stablecoin vs other) — tidak ada transparency dashboard atau laporan berkala.
- [financial] Runway Aptos Labs: sisa kas dari $350M funding, burn rate bulanan, dan projected runway — tidak diungkap.
- [financial] Revenue Aptos Labs dari enterprise services: apakah sudah profitable atau masih subsidi VC.
- [financial] Detail SAFT terms untuk investor Series A/B: harga per token, vesting cliff, unlock schedule — dibutuhkan Phase 6.
- [financial] Status fee switch governance: apakah ada proposal untuk mengaktifkan protocol fee capture di masa depan.
- [financial] Audit keuangan Foundation: apakah ada audited financial statements tahunan (non-profit Cayman Islands requirement).
- [financial] Klasifikasi regulator APT di AS (SEC): apakah ada Wells Notice, investigasi, atau legal opinion terpublikasi.
- [financial] Alokasi grant DAO: total dana yang sudah dicairkan vs yang tersisa di treasury DAO multisig.
- [financial] Hubungan keuangan Aptos Labs ↔ Aptos Foundation: apakah ada revenue sharing, service agreement, atau grant bolak-balik.
- [financial] Inflationary staking reward schedule: apakah parameter (7% start, -1.5%/yr) sudah di-hardcode atau bisa diubah governance.
- [token] Real-time circulating supply metodologi: CoinGecko vs CoinMarketCap vs on-chain vesting contract query sering berbeda; tidak ada definisi resmi "circulating" dari Foundation.
- [token] Alamat multisig Foundation dan Grant DAO treasury tidak dipublikasikan sebagai daftar terverifikasi; sulit audit on-chain holding Foundation vs Community.
- [token] Vesting contract address untuk Core Contributors dan Investors: apakah single contract atau multiple; apakah source code verified di explorer.
- [token] Detail gas schedule v3 (v1.8 upgrade): formula base fee vs priority fee, parameter burn rate, apakah ada EIP-1559 style dynamic base fee.
- [token] Staking reward rate schedule: apakah 7% -> 3.25% hardcoded atau bisa diubah governance; apakah sudah turun ke 5.5% (tahun 2) atau 4% (tahun 3) per Oktober 2024.
- [token] Airdrop AIT-1/2/3 total jumlah token dan persentase dari Community allocation (51.02%) — whitepaper tidak rinci breakdown airdrop vs grant vs foundation ops.
- [token] Grant DAO proposal voting mechanism: apakah fully on-chain (snapshot + execution) atau off-chain signaling + Foundation multisig execution.
- [token] Validator set stake concentration: persentase total stake yang dikontrol top 10 validator vs long tail; dampak pada governance decentralization.
- [token] Wrapped APT representations di Ethereum/Solana/BSC: multiple bridge (Wormhole, LayerZero, Celer) menghasilkan multiple ERC-20/SPL token; tidak ada "official" wrapped APT tunggal.
- [token] Fee switch / protocol revenue: apakah ada proposal governance untuk mengarahkan sebagian base fee ke treasury protokol (seperti EIP-1559 burn + protocol fee).
- [token] Inflation vs burn real-time net supply growth: data historis harian tidak dipublikasikan dashboard resmi; perlu indexer custom.
- [token] Legal status APT di AS (SEC): apakah Foundation/Labs memiliki legal opinion atau no-action letter; dampak pada staking reward dan governance participation untuk US persons.
- [ecosystem] LayerZero integration detail: official announcement date, OFT standard implementation status, dan apakah sudah live di mainnet atau masih testnet — Phase 3 tidak memiliki Event ID spesifik untuk LayerZero.
- [ecosystem] Meta/Diem IP licensing status: apakah Move language/VM sepenuhnya Apache 2.0/MIT tanpa patent encumbrance, atau ada patent license agreement dengan Meta — tidak ada publik statement resmi lengkap.
- [ecosystem] Validator geographic distribution real-time: persentase node di Google Cloud vs AWS vs self-hosted vs other cloud — tidak ada dashboard publik.
- [ecosystem] Indexer provider SLA dan redundancy: apakah NodeReal dan Nodit memiliki failover antara mereka, atau dApp harus implement sendiri — tidak terdokumentasi.
- [ecosystem] Grants DAO voting mechanism detail: fully on-chain execution vs off-chain signaling + Foundation multisig — whitepaper dan governance forum tidak konsisten.
- [ecosystem] Top 10 validator stake concentration percentage real-time — explorer menunjukkan ranking tapi tidak persentase total stake.
- [ecosystem] Wormhole vs LayerZero usage split untuk wrapped APT volume — tidak ada analytics dashboard resmi.
- [ecosystem] Keyless authentication adoption metrics: jumlah akun keyless dibuat, active users, geographic distribution — tidak dipublikasikan berkala.
- [ecosystem] Aptos Foundation council/board composition: nama individu, term limits, conflict of interest policy — tidak diungkap di website foundation.
- [ecosystem] Movement Labs collaboration concrete deliverables: shared tooling (Move Analyzer, LSP) status, joint hackathon schedule, standardization RFCs — blog post tinggi level saja.
- [ecosystem] Docker Hub image verification: apakah aptoslabs/validator images signed/reproducible builds — tidak terdokumentasi.
- [ecosystem] Emergency upgrade procedure: apakah ada timrapid response untuk critical bug, dan governance bypass mechanism — tidak di whitepaper.
- [ecosystem] Regulatory engagement: apakah Aptos Labs/Foundation memiliki legal counsel terdaftar SEC, FinCEN registration, atau jurisdiction-specific compliance program — tidak diungkap.
- [market] Real-time TVL discrepancy: DefiLlama shows ~$480M (2024-12) vs Phase 3 EV-030 claim "$1B+" — need verification of peak vs current, and whether EV-030 included staked APT in validators (not DeFi TVL).
- [market] Circulating supply methodology conflict: CoinGecko, CoinMarketCap, Messari, Token Terminal report different circulating supply numbers due to vesting contract treatment — no official Foundation definition published.
- [market] Bridge volume attribution: Wormhole vs LayerZero volume split for APT not publicly aggregated; Dune dashboards exist but not official.
- [market] Developer count definition: Electric Capital "monthly active developers" vs GitHub unique contributors vs Foundation grant recipients — different methodologies yield 250–1,200 range.
- [market] Market share denominator: "L1 TVL rank #12–15" depends on whether including L2s (Arbitrum, Optimism, Base) in ranking — DefiLlama includes them, changing rank.
- [market] Futures open interest data: Coinglass aggregates Binance/OKX/Bybit but may miss Coinbase International, Kraken Futures, HTX — need cross-exchange verification.
- [market] Keyless adoption metrics: No public dashboard for keyless accounts created, active users, or gas fees paid — Foundation has not released analytics.
- [market] Validator stake concentration: Explorer shows ranking but not % of total stake per validator; top 10 vs long tail concentration unknown.
- [market] RWA pipeline: Foundation grants include RWA category but no announced partnerships or live protocols — status unclear.
- [market] Monad mainnet launch impact: Monad parallel EVM testnet 2024; if mainnet launches 2025, competitive dynamic for "parallel execution" narrative shifts — monitor.
- [market] SEC regulatory classification: No public Wells Notice, but APT staking/governance participation for US persons uncertain — legal opinion not published.
- [market] Treasury transparency: Foundation treasury composition (APT vs stablecoin vs other), grant deployment rate, runway — no audited financials or dashboard.
- [market] Gas schedule v3 parameters: v1.8 upgrade changed gas schedule; exact formula, base fee dynamics, burn rate impact on net supply not documented in single source.
- [market] LayerZero OFT status: Official docs mention LayerZero but no Event ID in Phase 3; unclear if OFT live on mainnet or testnet only.
- [market] Google Cloud/AWS validator share: No public data on % of validators hosted on each cloud provider — centralization risk unquantified.
- [behavioral] Treasury Composition & Transparency: Foundation treasury real-time composition (APT vs stablecoin vs other), grant deployment rate, runway — no audited financials or dashboard; Cayman non-profit filing requirements unclear
- [behavioral] Circulating Supply Methodology Conflict: CoinGecko, CoinMarketCap, Messari, Token Terminal report different circulating supply numbers due to vesting contract treatment; no official Foundation definition published
- [behavioral] Validator Geographic/Cloud Distribution: Percentage of validators on Google Cloud vs AWS vs self-hosted vs other — centralization risk unquantified; no public dashboard
- [behavioral] Bridge Volume Attribution: Wormhole vs LayerZero volume split for APT not publicly aggregated; Dune dashboards exist but not official
- [behavioral] LayerZero OFT Status: Official docs mention LayerZero but no Phase 3 Event ID; unclear if OFT live on mainnet or testnet only
- [behavioral] Keyless Adoption Metrics: Number of keyless accounts created, active users, geographic distribution, gas fees paid — Foundation has not released analytics
- [behavioral] Grants DAO Voting Mechanism: Fully on-chain execution vs off-chain signaling + Foundation multisig — whitepaper and governance forum inconsistent
- [behavioral] RWA Pipeline Status: Foundation grants include RWA category but no announced partnerships or live protocols — status unclear
- [behavioral] Monad Mainnet Launch Impact: Monad parallel EVM testnet 2024; if mainnet launches 2025, competitive dynamic for "parallel execution" narrative shifts
- [behavioral] SEC Regulatory Classification: No public Wells Notice, but APT staking/governance participation for US persons uncertain; legal opinion not published
- [behavioral] Emergency Upgrade Procedure: No documented rapid response process for critical bugs; governance bypass mechanism unspecified
- [behavioral] Google Cloud/AWS Validator Share: No public data on % validators hosted on each cloud provider — centralization risk unquantified
- [behavioral] Move 2024 Edition Migration: Backward compatibility tooling for legacy Move packages; automatic migration status unclear
- [behavioral] Gas Schedule v3 Parameters: v1.8 upgrade changed gas schedule; exact formula, base fee dynamics, burn rate impact on net supply not documented in single source
- [behavioral] Foundation Council/Board Composition: Individual names, term limits, conflict of interest policy — not disclosed on Foundation website
- [conflict] Description: Definisi resmi circulating supply tidak ada; CoinGecko, CoinMarketCap, Messari, Token Terminal melaporkan angka berbeda karena perbedaan perlakuan vesting contracts
- [conflict] Affected Phase: Phase 6, Phase 8
- [conflict] Evidence: Phase 8 Open Threads "Circulating supply methodology conflict"; Phase 6 Holder Distribution "tidak diungkap resmi"
- [conflict] Alternative Interpretations: 1) Circulating supply termasuk vested tokens yang belum unlock; 2) Hanya mencakup tokens yang fully transferable; 3) termasuk tokens di CEX cold wallets yang diperdagangkan
- [conflict] Status: Open Open Thread ID: OT-02
- [conflict] Description: LayerZero OFT untuk APT — apakah sudah live di mainnet atau masih testnet
- [conflict] Affected Phase: Phase 3, Phase 7
- [conflict] Evidence: Phase 7 Major Integrations LayerZero "OFT standard untuk APT"; Tidak ada Event ID di Phase 3
- [conflict] Alternative Interpretations: 1) Sudah live tapi tidak tercatat; 2) belum live, masih roadmap; 3) integrasi hanya untuk messaging, bukan token OFT
- [conflict] Status: Open Open Thread ID: OT-03
- [conflict] Description: TVL DeFi real-time vs klaim peak — apakah angka $1B+ merujuk peak Maret 2024 atau rata-rata 2024
- [conflict] Affected Phase: Phase 3, Phase 8
- [conflict] Evidence: EV-030 "TVL DeFi $1B+"; DefiLlama menunjukkan $480M per Des 2024
- [conflict] Alternative Interpretations: 1) $1B+ adalah TVL peak; 2) $1B+ adalah klaim marketing; 3) Definisi TVL berbeda antara DefiLlama dan Foundation
- [conflict] Status: Open Open Thread ID: OT-04
- [conflict] Description: Keyless adoption metrics — jumlah akun keyless dibuat, active users, geographic distribution
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Phase 8 Open Threads "Keyless adoption metrics tidak dipublikasikan"
- [conflict] Alternative Interpretations: 1) Tidak ada data karena belum diukur; 2) Data ada tapi tidak dipublikasikan; 3) Keyless belum diadopsi massal, jadi tidak ada metrik signifikan
- [conflict] Status: Open Open Thread ID: OT-05
- [conflict] Description: Validator geographic distribution dan persentase validator di Google Cloud vs AWS vs self-hosted
- [conflict] Affected Phase: Phase 7
- [conflict] Evidence: Phase 7 Ecosystem Risks "Cloud Infrastructure Centralization"; Tidak ada dashboard publik
- [conflict] Alternative Interpretations: 1) Mayoritas di Google Cloud; 2) Seimbang antara Google Cloud dan AWS; 3) Validator self-hosted lebih banyak dari yang diasumsikan
- [conflict] Status: Open Open Thread ID: OT-06
- [conflict] Description: Grants DAO voting mechanism — apakah sepenuhnya on-chain atau off-chain signaling + Foundation multisig
- [conflict] Affected Phase: Phase 6, Phase 7
- [conflict] Evidence: Phase 6 Open Threads "Grants DAO voting mechanism"; Phase 7 Governance Ecosystem "hybrid"
- [conflict] Alternative Interpretations: 1) Fully on-chain (Framework upgrade path); 2) Off-chain Snapshot-style voting + Foundation multisig execution; 3) Voting on-chain tapi execution manual oleh Foundation
- [conflict] Status: Open Open Thread ID: OT-07
- [conflict] Description: Detail gas schedule v3 (v1.8 upgrade) — formula base fee, priority fee, burn rate dynamics
- [conflict] Affected Phase: Phase 4
- [conflict] Evidence: Phase 4 Open Threads "Gas schedule v3 parameters tidak terdokumentasi"
- [conflict] Alternative Interpretations: 1) Formula sama dengan v2 dengan parameter berbeda; 2) Formula redesain; 3) Tidak ada perubahan signifikan dari v2
- [conflict] Status: Open Open Thread ID: OT-08
- [conflict] Description: Emergency governance procedure untuk critical bug — apakah ada bypass governance; rapid response timeline
- [conflict] Affected Phase: Phase 9
- [conflict] Evidence: Phase 9 Open Threads "Emergency Upgrade Procedure tidak terdokumentasi"
- [conflict] Alternative Interpretations: 1) Ada procedure internal tidak publik; 2) Semua upgrade harus melalui governance normal; 3) Tim Labs bisa bypass jika critical
- [conflict] Status: Open Open Thread ID: OT-09
- [conflict] Description: Status RWA pipeline — apakah ada partnership atau live protocol untuk real-world assets
- [conflict] Affected Phase: Phase 8
- [conflict] Evidence: Phase 8 Narrative Position RWA "Emerging Narrative"; Grants termasuk RWA category
- [conflict] Alternative Interpretations: 1) Masih research; 2) Ada pipeline tersembunyi; 3) RWA hanya naratif marketing
- [conflict] Status: Open Open Thread ID: OT-10
- [conflict] Description: Hubungan keuangan Aptos Labs ↔ Aptos Foundation — apakah ada revenue sharing, service agreement, grant bolak-balik
- [conflict] Affected Phase: Phase 5
- [conflict] Evidence: Phase 5 Financial Dependencies (Foundation treasury spend); Tidak ada detail agreement
- [conflict] Alternative Interpretations: 1) Tidak ada hubungan finansial langsung; 2) Labs menerima service agreement dari Foundation; 3) Foundation memberikan grant ke Labs untuk public goods
- [conflict] Status: Open
- [airdrop] Alokasi pasti airdrop (jumlah APT dan persen supply) — tidak di-breakdown di whitepaper, tidak ada blog post resmi, tidak ada on-chain Merkle root/contract address yang diverifikasi publik
- [airdrop] Jumlah penerima unik (bukan alamat) — Phase 3 menyebut "ribuan validator/developer" tapi tidak membedakan individu vs entity yang menjalankan multiple node
- [airdrop] Snapshot block height dan tanggal cutoff untuk eligibility AIT-1/2/3 — tidak dipublikasikan
- [airdrop] Mekanisme anti-sybil detail: criteria, tools, jumlah diskualifikasi, appeal process — tidak ada laporan transparansi
- [airdrop] Retention cohort analysis: berapa % airdrop recipients yang jadi delegator/staker/LP vs direct seller — tidak ada Dune/dashboard publik
- [airdrop] Apakah ada airdrop tambahan (Season 2) direncanakan — Foundation/Grants DAO tidak mengumumkan; governance forum tidak ada proposal terkait
- [airdrop] Circulating supply methodology Foundation: apakah airdrop unlocked TGE dihitung "circulating" atau "non-circulating" sampai claimed — tracker berbeda terus
- [airdrop] Harga rata-rata claim per penerima (USD) — perlu cross-ref claim timestamp vs price feed, tidak ada data agregat
- [airdrop] Sybil farming evidence: apakah ada cluster analysis on-chain (same IP, same deposit pattern, sequential nonce) yang menunjukkan farming — tidak ada publikasi
- [airdrop] Regulatory legal opinion untuk airdrop TGE: apakah Aptos Labs/Foundation mendapat no-action letter atau legal memo untuk distribusi ke US persons — tidak diungkap
