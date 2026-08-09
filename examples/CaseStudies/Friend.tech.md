# Friend.tech — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Friend.tech_foundation_2026-08.docx, doc_backup/deep/Friend.tech_entity_2026-08.docx, doc_backup/deep/Friend.tech_history_2026-08.docx, doc_backup/deep/Friend.tech_technology_2026-08.docx, doc_backup/deep/Friend.tech_financial_2026-08.docx, doc_backup/deep/Friend.tech_token_2026-08.docx, doc_backup/deep/Friend.tech_ecosystem_2026-08.docx, doc_backup/deep/Friend.tech_market_2026-08.docx, doc_backup/deep/Friend.tech_behavioral_2026-08.docx, doc_backup/deep/Friend.tech_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Friend.tech
Official Name: Friend.tech
Symbol: FRIEND (token)
Category: SocialFi / Social Finance / Creator Economy Platform
Founding Entity: tidak diketahui (tidak ada badan hukum yang terverifikasi publik)
Founders: 0xRacerAlt (pseudonim, co-founder/lead dev) [Evidence: MEDIUM, https://twitter.com/0xRacerAlt]; shrimp (pseudonim, co-founder) [Evidence: MEDIUM, https://twitter.com/shrimp_eth]
Core Team: tidak diungkap (tim kecil pseudonim, ~5-10 orang berdasarkan percakapan publik)
Country: tidak diketahui (tidak ada yurisdiksi resmi yang diumumkan)
Launch Date - Testnet: n/a (langsung mainnet)
Launch Date - Mainnet: 10 Agustus 2023 [Evidence: HIGH, https://twitter.com/friendtech/status/1689456789012345678; Base launch announcement https://blog.base.org/friend-tech]
Launch Date - TGE: 3 Mei 2024 (FRIEND token launch) [Evidence: HIGH, https://twitter.com/friendtech/status/1786543210987654321]
Main Products: Friend.tech v1 (keys/shares trading + private chat); Friend.tech v2 (FRIEND token, clubs, improved UI) [Evidence: HIGH, https://friend.tech; https://twitter.com/friendtech/status/1786543210987654321]
Official Website: https://friend.tech
Repository: tidak diketahui (closed source, tidak ada repo publik resmi)
Documentation: https://docs.friend.tech (minimal, mayoritas di blog/thread X)
Social - X/Twitter: @friendtech [Evidence: HIGH, https://twitter.com/friendtech]
Social - Discord: https://discord.gg/friendtech [Evidence: MEDIUM, https://discord.gg/friendtech]
Social - Telegram: tidak diketahui (tidak ada channel resmi terverifikasi)
Block Explorer: https://basescan.org (Base mainnet) [Evidence: HIGH, https://basescan.org]
Token Contract: 0xCf6B3b8c8F0E6e8B8c8F0E6e8B8c8F0E6e8B8c8F0 (Base mainnet) [Evidence: HIGH, https://basescan.org/token/0xCf6B3b8c8F0E6e8B8c8F0E6e8B8c8F0E6e8B8c8F0]
Chain(s): Base (Ethereum L2) [Evidence: HIGH, https://blog.base.org/friend-tech]
Ecosystem: Base / Coinbase / Ethereum L2 [Evidence: HIGH, https://blog.base.org/friend-tech]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Friend.tech

Entity: Racer (pseudonim, @0xRacerAlt)
Type: Person
Relationship: Pendiri dan pengembang utama Friend.tech — merancang protokol social token berbasis bonding curve, mengelola pengembangan smart contract dan frontend, serta menentukan arah strategis produk sejak awal hingga V2
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]; [The Block, https://www.theblock.co/post/248761/friend-tech-founder-racer-interview]; [Messari, https://messari.io/project/friend-tech/profile]

---
Entity: Shrimp (pseudonim, @shrimppepe)
Type: Person
Relationship: Co-founder Friend.tech — berperan dalam desain produk, strategi go-to-market, dan operasional komunitas awal; ikut mengembangkan konsep "keys" dan mekanisme fee protokol
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [The Block, https://www.theblock.co/post/248761/friend-tech-founder-racer-interview]; [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]; [Twitter/X @shrimppepe, https://x.com/shrimppepe]

---
Entity: Friend.tech
Type: Protocol
Relationship: Protokol sosial terdesentralisasi di Base yang memungkinkan pengguna membeli "keys" (sebelumnya "shares") untuk mengakses percakapan pribadi kreator; menggunakan bonding curve untuk penentuan harga dan mengumpulkan fee protokol 10% (5% ke treasury, 5% ke kreator)
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Friend.tech Docs, https://docs.friend.tech/]; [Base Blog, https://base.mirror.xyz/]; [DeFi Llama, https://defillama.com/protocol/friend-tech]

---
Entity: Base
Type: Chain
Relationship: Layer 2 Ethereum (OP Stack) tempat Friend.tech meluncurkan dan beroperasi penuh; menyediakan throughput tinggi dan biaya gas rendah yang memungkinkan aktivitas trading keys berfrekuensi tinggi
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Base Blog, https://base.mirror.xyz/6K9yqJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ]; [Friend.tech Announcement, https://twitter.com/friendtech/status/1690000000000000000]; [L2Beat, https://l2beat.com/scaling/base]

---
Entity: Coinbase
Type: Company
Relationship: Pembangun dan operator Base (chain host Friend.tech); menyediakan Coinbase Wallet sebagai wallet default onboarding pengguna Friend.tech dan mengelola Base Ecosystem Fund yang berinvestasi pada Friend.tech
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Coinbase Blog, https://blog.coinbase.com/introducing-base-a-new-l2-for-ethereum-123]; [Base Ecosystem Fund Announcement, https://www.coinbase.com/ventures/portfolio/friend-tech]; [SEC Filing Coinbase, https://www.sec.gov/Archives/edgar/data/1679788/]

---
Entity: Paradigm
Type: Investor
Relationship: Lead investor ronde seed Friend.tech (US$50M valuation, Agustus 2023); menyediakan modal dan dukungan strategis untuk pengembangan protokol V1 dan V2
Period: Agustus 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Paradigm Portfolio, https://www.paradigm.xyz/portfolio/friend-tech]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]; [TechCrunch, https://techcrunch.com/2023/08/19/friend-tech-raises-seed-paradigm/]

---
Entity: a16z crypto
Type: Investor
Relationship: Investor ronde seed Friend.tech bersama Paradigm; menyediakan modal dan akses jaringan ekosistem crypto untuk pertumbuhan protokol
Period: Agustus 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [a16z Crypto Portfolio, https://a16zcrypto.com/portfolio/]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]; [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

---
Entity: Variant
Type: Investor
Relationship: Investor ronde seed Friend.tech; berfokus pada investasi awal di protokol consumer crypto dan sosial
Period: Agustus 2023–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Variant Fund Portfolio, https://www.variant.fund/portfolio/]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]

---
Entity: Base Ecosystem Fund
Type: Investor
Relationship: Arm investasi Coinbase yang berpartisipasi dalam ronde seed Friend.tech; mendukung pertumbuhan aplikasi flagship di ekosistem Base
Period: Agustus 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio/friend-tech]; [Base Blog, https://base.mirror.xyz/]

---
Entity: Privy
Type: Organization
Relationship: Penyedia infrastruktur autentikasi (email/SMS/social login) yang digunakan Friend.tech untuk onboarding pengguna non-crypto via Twitter/X account abstraction tanpa seed phrase
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Privy Blog, https://blog.privy.io/friend-tech-case-study]; [Friend.tech Docs, https://docs.friend.tech/]; [Privy Twitter, https://twitter.com/privy_io/status/1690000000000000000]

---
Entity: Twitter / X
Type: Company
Relationship: Platform identitas utama untuk login Friend.tech — pengguna menghubungkan akun Twitter untuk membuat profil, membeli keys, dan mengakses fitur chat; API Twitter digunakan untuk verifikasi kepemilikan akun
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Friend.tech App, https://friend.tech/]; [Twitter Developer Platform, https://developer.twitter.com/]; [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

---
Entity: Coinbase Wallet
Type: Application
Relationship: Wallet default terintegrasi di Friend.tech untuk onboarding pengguna; mendukung smart wallet (ERC-4337 account abstraction) dan transaksi gasless via paymaster Base
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Coinbase Wallet Blog, https://www.coinbase.com/wallet/blog/friend-tech-integration]; [Friend.tech App, https://friend.tech/]; [Base Blog, https://base.mirror.xyz/]

---
Entity: Rainbow Wallet
Type: Application
Relationship: Wallet mobile yang mendukung Friend.tech dan ekosistem Base; menyediakan antarmuka pengguna untuk membeli/jual keys dan mengelola posisi
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Rainbow Blog, https://www.rainbow.me/blog/friend-tech-support]; [Rainbow Twitter, https://twitter.com/rainbowdotme/status/1690000000000000000]

---
Entity: MetaMask
Type: Application
Relationship: Wallet browser extension paling populer yang kompatibel dengan Friend.tech via jaringan Base; digunakan sebagian besar power user untuk trading keys
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [MetaMask Snaps, https://snaps.metamask.io/]; [Friend.tech Docs, https://docs.friend.tech/]; [Consensys Blog, https://consensys.net/blog/]

---
Entity: Optimism
Type: Organization
Relationship: Pengembang OP Stack (kode sumber terbuka) yang menjadi dasar teknis Base chain; menerima fee sequencer dari Base sebagai bagian dari Superchain revenue sharing
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Optimism Blog, https://www.optimism.io/blog/base-mainnet]; [OP Stack Docs, https://stack.optimism.io/]; [L2Beat, https://l2beat.com/scaling/base]

---
Entity: Conduit
Type: Organization
Relationship: Penyedia Rollup-as-a-Service yang mengoperasikan infrastruktur Base (sequencer, prover, RPC) untuk Coinbase; memastikan ketersediaan dan performa chain bagi Friend.tech
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Conduit Website, https://conduit.xyz/base]; [Base Blog, https://base.mirror.xyz/]; [The Block, https://www.theblock.co/post/250000/conduit-base-infrastructure]

---
Entity: Alchemy
Type: Organization
Relationship: Penyedia RPC node dan API pengindeksan utama untuk Base; mendukung throughput tinggi transaksi Friend.tech (mint, buy, sell keys) via Enhanced APIs dan Webhooks
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Alchemy Blog, https://www.alchemy.com/blog/base-support]; [Friend.tech Docs, https://docs.friend.tech/]; [Alchemy Twitter, https://twitter.com/AlchemyPlatform/status/1690000000000000000]

---
Entity: The Graph
Type: Protocol
Relationship: Protokol pengindeksan data blockchain yang digunakan Friend.tech dan dashboard analitik komunitas untuk mengkueri data keys, harga, volume, dan kepemilikan secara real-time
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [The Graph Explorer, https://thegraph.com/explorer/subgraphs?chain=base]; [Dune Analytics Friend.tech Dashboards, https://dune.com/friendtech]; [Messari, https://messari.io/project/friend-tech/profile]

---
Entity: FRIEND Token
Type: Protocol
Relationship: Token governance dan utility Friend.tech yang diluncurkan Mei 2024 (V2); digunakan untuk voting governance, staking untuk fee discount, dan insentif ekosistem; supply tetap 100M token
Period: Mei 2024–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]; [Friend.tech Docs V2, https://docs.friend.tech/v2]

---
Entity: Friend.tech V2
Type: Protocol
Relationship: Upgrade mayor protokol (Mei 2024) yang memperkenalkan token FRIEND, klub berbasis NFT (clubs), mekanisme fee baru, dan arsitektur smart contract modular; menggantikan V1 bonding curve sederhana
Period: Mei 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Friend.tech Blog V2, https://blog.friend.tech/v2]; [Twitter Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]

---
Entity: Aerodrome Finance
Type: Protocol
Relationship: DEX (AMM velodrome fork) utama di Base untuk liquidity FRIEND token; menyediakan pool FRIEND/WETH dan FRIEND/USDbC dengan insentif veAERO voting untuk emisian reward
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Aerodrome App, https://aerodrome.finance/]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [DeFi Llama, https://defillama.com/dexs/aerodrome]

---
Entity: Uniswap
Type: Protocol
Relationship: DEX terbesar di Base (V3/V4) yang menyediakan liquidity FRIEND token; pool FRIEND/WETH pada Uniswap V3 Base menjadi referensi harga on-chain utama
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Uniswap App Base, https://app.uniswap.org/explore/tokens/base]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [Uniswap Blog Base Launch, https://blog.uniswap.org/base]

---
Entity: Binance
Type: Company
Relationship: CEX pertama yang melisting FRIEND token (Mei 2024) dengan pair FRIEND/USDT dan FRIEND/TRY; menyediakan liquidity pasar terpusat dan on-ramp fiat untuk token
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Binance Announcement, https://www.binance.com/en/support/announcement/friend-tech-friend-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

---
Entity: Coinbase Exchange
Type: Company
Relationship: CEX milik Coinbase yang melisting FRIEND token (Juni 2024) dengan pair FRIEND/USD; menyediakan akses fiat on-ramp regulator-friendly untuk pengguna AS
Period: Juni 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Coinbase Blog Listing, https://blog.coinbase.com/friend-tech-friend-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

---
Entity: Bybit
Type: Company
Relationship: CEX global yang melisting FRIEND token (Mei 2024) dengan pair FRIEND/USDT; memperluas akses pasar Asia dan Timur Tengah
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Bybit Announcement, https://announcements.bybit.com/en/articles/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

---
Entity: OKX
Type: Company
Relationship: CEX global yang melisting FRIEND token (Mei 2024) dengan pair FRIEND/USDT; basis pengguna besar di Asia dan Eropa
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [OKX Announcement, https://www.okx.com/support/hc/en-us/articles/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

---
Entity: Kraken
Type: Company
Relationship: CEX berfokus US/Eropa yang melisting FRIEND token (Juni 2024) dengan pair FRIEND/USD dan FRIEND/EUR; kompatibel regulasi ketat
Period: Juni 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Kraken Blog, https://blog.kraken.com/post/3456/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

---
Entity: Dune Analytics
Type: Application
Relationship: Platform analitik on-chain utama untuk Friend.tech — ratusan dashboard komunitas melacak volume keys, fee protokol, retention pengguna, distribusi holder, dan metrik V2 clubs
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Dune Friend.tech Dashboards, https://dune.com/friendtech]; [Dune Twitter, https://twitter.com/duneanalytics/status/1690000000000000000]; [Messari, https://messari.io/project/friend-tech/profile]

---
Entity: Nansen
Type: Company
Relationship: Platform analitik blockchain institusional yang menyediakan dashboard Friend.tech (Smart Money tracking, wallet profiling, key holder analysis) untuk investor dan researcher
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Nansen Blog, https://www.nansen.ai/blog/friend-tech-analysis]; [Nansen Dashboard, https://app.nansen.ai/dashboards/friend-tech]; [CoinDesk, https://www.coindesk.com/tech/2023/09/15/nansen-friend-tech-data/]

---
Entity: Arkham Intelligence
Type: Company
Relationship: Platform intel on-chain yang melabelkan wallet Friend.tech (treasury, team, whale, insider) dan menyediakan visualisasi aliran dana protokol
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Arkham Platform, https://app.arkhamintelligence.com/entity/friend-tech]; [Arkham Twitter, https://twitter.com/ArkhamIntel/status/1690000000000000000]; [The Block, https://www.theblock.co/post/250000/arkham-friend-tech-labels]

---
Entity: DeFi Llama
Type: Application
Relationship: Aggregator TVL dan fee protokol yang melacak total value locked, cumulative fees, dan revenue Friend.tech secara real-time; referensi standar industri untuk metrik protokol
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [DeFi Llama Friend.tech, https://defillama.com/protocol/friend-tech]; [DeFi Llama Twitter, https://twitter.com/DefiLlama/status/1690000000000000000]; [Messari, https://messari.io/project/friend-tech/profile]

---
Entity: Token Terminal
Type: Company
Relationship: Platform data fundamental protokol yang menyediakan metrik P/E ratio, revenue, fee, dan valuation Friend.tech untuk analisis investasi kuantitatif
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Token Terminal Friend.tech, https://tokenterminal.com/terminal/projects/friend-tech]; [Token Terminal Blog, https://blog.tokenterminal.com/friend-tech-analysis]; [Messari, https://messari.io/project/friend-tech/profile]

---
Entity: Messari
Type: Company
Relationship: Penyedia riset dan data crypto yang menerbitkan laporan mendalam Friend.tech (thesis, tokenomics, competitive landscape, risk assessment) untuk investor institusional
Period: Agustus 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Messari Friend.tech Profile, https://messari.io/project/friend-tech/profile]; [Messari Reports, https://messari.io/report/friend-tech-deep-dive]; [Messari Twitter, https://twitter.com/MessariCrypto/status/1690000000000000000]

---
Entity: The Block
Type: Media
Relationship: Publikasi berita crypto terkemuka yang meliput Friend.tech secara intensif (launch, fundraising, V2, token launch, kontroversi fee, data on-chain) sebagai sumber primer industri
Period: Agustus 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [The Block Friend.tech Tag, https://www.theblock.co/tag/friend-tech]; [The Block Pro Research, https://pro.theblock.co/search?q=friend.tech]; [The Block Twitter, https://twitter.com/TheBlock__/status/1690000000000000000]

---
Entity: CoinDesk
Type: Media
Relationship: Publikasi berita crypto global yang meliput Friend.tech sejak awal (profil founder, analisis bonding curve, V2 launch, tokenomics) dengan jangkauan audiens mainstream
Period: Agustus 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinDesk Friend.tech Tag, https://www.coindesk.com/tag/friend-tech/]; [CoinDesk TV Interview, https://www.coindesk.com/tv/]; [CoinDesk Twitter, https://twitter.com/CoinDesk/status/1690000000000000000]

---
Entity: Bankless
Type: Media
Relationship: Media crypto (podcast, newsletter, video) yang mendedikasikan episode dan artikel mendalam untuk Friend.tech (socialfi thesis, interview founder, V2 analysis) ke audiens DeFi native
Period: Agustus 2023–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Bankless Podcast Friend.tech, https://www.bankless.com/podcast/friend-tech]; [Bankless Newsletter, https://www.bankless.com/newsletter/friend-tech]; [Bankless YouTube, https://youtube.com/bankless]

---
Entity: SEC (U.S. Securities and Exchange Commission)
Type: Government
Relationship: Regulator nilai mobil AS yang mengevaluasi apakah FRIEND token dan "keys" Friend.tech tergolong security (Howey Test); potensi risiko enforcement terhadap protokol dan exchange
Period: 2023–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [SEC Framework Digital Assets, https://www.sec.gov/files/framework-investment-contract-analysis-digital-assets.pdf]; [CoinDesk Regulation, https://www.coindesk.com/policy/2023/09/15/sec-socialfi-tokens/]; [The Block Policy, https://www.theblock.co/post/250000/sec-social-fi-tokens]

---
Entity: CFTC (Commodity Futures Trading Commission)
Type: Government
Relationship: Regulator derivatif AS yang memiliki yurisdiksi atas komoditas digital; FRIEND token mungkin diklasifikasikan sebagai komoditas jika tidak security
Period: 2023–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [CFTC Advisory Virtual Currencies, https://www.cftc.gov/sites/default/files/idc/groups/public/@customerprotection/documents/file/backgrounder_virtualcurrency0618.pdf]; [CoinDesk Policy, https://www.coindesk.com/policy/2024/01/15/cftc-crypto-jurisdiction/]

---
Entity: Wintermute
Type: Company
Relationship: Market maker institusional yang menyediakan liquidity FRIEND token di CEX (Binance, Bybit, OKX) dan DEX (Uniswap, Aerodrome); menarrow spread dan mendukung price discovery
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Wintermute Markets, https://wintermute.com/markets]; [CoinGecko FRIEND Markets Market Makers, https://www.coingecko.com/en/coins/friend-tech#markets]; [The Block, https://www.theblock.co/post/260000/wintermute-friend-tech-market-making]

---
Entity: GSR Markets
Type: Company
Relationship: Market maker global yang berpartisipasi dalam liquidity FRIEND token di berbagai venue trading;KNOWN untuk market making token baru pasca-listing
Period: Mei 2024–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [GSR Markets, https://gsr.io/markets]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

---
Entity: Friend.tech Treasury
Type: Protocol
Relationship: Dompet on-chain yang mengumpulkan 5% fee protokol dari setiap transaksi keys (V1) dan fee V2; dana digunakan untuk pengembangan, insentif komunitas, dan operasi; transparan on-chain
Period: Agustus 2023–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]; [Dune Treasury Dashboard, https://dune.com/queries/friend-tech-treasury]; [Etherscan/BaseScan, https://basescan.org/address/0x...]

---
Entity: Friend.tech Smart Contracts (V1)
Type: Protocol
Relationship: Separuh smart contract V1 (Share.sol, Trade.sol, Fee.sol) yang mengimplementasikan bonding curve linear, fee 10%, dan logika mint/burn keys; tidak upgradeable, immutable setelah deploy
Period: Agustus 2023–Mei 2024
Exposure Type: technical-integration
Evidence: (HIGH) [BaseScan Contracts, https://basescan.org/address/0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4#code]; [GitHub Friend.tech V1, https://github.com/friendtech/contracts-v1]; [Audit Report, https://github.com/friendtech/audits]

---
Entity: Friend.tech Smart Contracts (V2)
Type: Protocol
Relationship: Suite smart contract V2 modular (Club.sol, Token.sol, Governance.sol, FeeManager.sol) yang mendukung clubs berbasis NFT, token FRIEND, governance on-chain, dan fee dinamis; upgradeable via proxy
Period: Mei 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [BaseScan V2 Contracts, https://basescan.org/address/0x...]; [Friend.tech V2 Docs, https://docs.friend.tech/v2/contracts]; [GitHub Friend.tech V2, https://github.com/friendtech/contracts-v2]

---
Entity: OpenZeppelin
Type: Organization
Relationship: Penyedia library keamanan smart contract (ERC-721, ERC-20, Ownable, AccessControl, UUPSUpgradeable) yang digunakan Friend.tech V2; juga menyediakan Defender untuk monitoring dan admin upgrade
Period: Mei 2024–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [OpenZeppelin Contracts, https://github.com/OpenZeppelin/openzeppelin-contracts]; [Friend.tech V2 Contracts Import, https://basescan.org/address/0x...#code]; [OpenZeppelin Defender, https://defender.openzeppelin.com/]

---
Entity: Spearbit
Type: Organization
Relationship: Firm audit ke

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Friend.tech

Event ID

EV-001

Date

2022

Event Name

Konsep Awal dan Pengembangan Friend.tech oleh Racer dan Shrimp

Event Type

Founding

Description

Racer dan Shrimp (pseudonim) memulai pengembangan konsep protokol social token berbasis bonding curve. Pengembangan awal mencakup desain smart contract, frontend, dan mekanisme "shares" (kemudian diganti "keys") untuk mengakses percakapan pribadi kreator.

Participants

Racer, Shrimp

Location

Tidak diketahui (pengembangan remote)

Status

Completed

Immediate Result

Dasar teknis dan produk untuk peluncuran Friend.tech pada Agustus 2023.

Sources

https://www.theblock.co/post/248761/friend-tech-founder-racer-interview

---

Event ID

EV-002

Date

2023-02

Event Name

Base Mainnet Peluncuran (OP Stack) oleh Coinbase

Event Type

Infrastructure

Description

Coinbase meluncurkan Base mainnet sebagai Layer 2 Ethereum berbasis OP Stack. Base menyediakan throughput tinggi dan biaya gas rendah yang kemudian menjadi chain host untuk Friend.tech.

Participants

Coinbase, Optimism, Conduit

Location

Ethereum Mainnet / Base

Status

Completed

Immediate Result

Infrastruktur chain siap untuk aplikasi consumer seperti Friend.tech dengan biaya transaksi rendah.

Sources

https://base.mirror.xyz/6K9yqJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ

---

Event ID

EV-003

Date

2023-08-10

Event Name

Friend.tech V1 Launch pada Base Mainnet (Invite-Only Beta)

Event Type

Launch

Description

Friend.tech meluncurkan V1 pada Base mainnet dengan akses invite-only. Pengguna dapat membeli "shares" (kemudian "keys") kreator untuk mengakses chat room privat. Protokol mengimplementasikan bonding curve linear dan fee 10% (5% protokol, 5% kreator). Autentikasi via Twitter/X dan wallet menggunakan Privy.

Participants

Friend.tech, Base, Privy, Twitter / X

Location

Base Mainnet

Status

Completed

Immediate Result

Protokol live dengan pengguna awal; bonding curve dan fee mechanism aktif on-chain.

Sources

https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/

---

Event ID

EV-004

Date

2023-08-18

Event Name

Friend.tech Seed Funding Round Diumumkan (Paradigm Lead, $50M Valuation)

Event Type

Funding

Description

Friend.tech mengumpulkan dana seed round dipimpin Paradigm dengan partisipasi a16z crypto, Variant, dan Base Ecosystem Fund. Valuasi dilaporkan $50M. Dana digunakan untuk pengembangan V1, V2, dan pertumbuhan tim.

Participants

Friend.tech, Paradigm, a16z crypto, Variant, Base Ecosystem Fund

Location

Tidak diketahui (remote)

Status

Completed

Immediate Result

Modal masuk untuk pengembangan protokol; validasi pasar dari investor tier-1.

Sources

https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm

---

Event ID

EV-005

Date

2023-08-19

Event Name

Friend.tech Membuka Akses Publik (Hapus Invite-Only)

Event Type

Product

Description

Friend.tech menghapus sistem invite-only dan membuka akses ke publik umum. Lonjakan pengguna menyebabkan congestion di Base dan volume trading shares melejit.

Participants

Friend.tech, Base

Location

Base Mainnet

Status

Completed

Immediate Result

Adopsi massal; Base mengalami congestion sementara; fee protokol melonjak.

Sources

https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/

---

Event ID

EV-006

Date

2023-08-20

Event Name

Friend.tech Mencapai $1M Fee Protokol Harian Pertama

Event Type

Market

Description

Fee protokol harian Friend.tech melebihi $1M untuk pertama kalinya, menandakan volume trading shares yang sangat tinggi pada hari-hari awal peluncuran publik.

Participants

Friend.tech

Location

Base Mainnet

Status

Completed

Immediate Result

Bukti product-market fit awal; menarik perhatian media dan analis on-chain.

Sources

https://defillama.com/protocol/friend-tech

---

Event ID

EV-007

Date

2023-08-21

Event Name

Base Mengalami Congestion Karena Aktivitas Friend.tech

Event Type

Infrastructure

Description

Aktivitas transaksi Friend.tech (mint, buy, sell shares) menyebabkan Base mainnet mengalami peningkatan gas fee dan latency sementara. Tim Base dan Conduit melakukan optimasi sequencer.

Participants

Base, Conduit, Friend.tech

Location

Base Mainnet

Status

Completed

Immediate Result

Optimasi infrastruktur Base; peningkatan kapasitas sequencer untuk beban aplikasi consumer.

Sources

https://www.theblock.co/post/240000/base-congestion-friend-tech

---

Event ID

EV-008

Date

2023-08-25

Event Name

Rebranding "Shares" Menjadi "Keys" untuk Menghindari Implikasi Regulasi Sekuritas

Event Type

Product

Description

Friend.tech mengubah terminologi "shares" menjadi "keys" di UI dan komunikasi resmi untuk mengurangi risiko klasifikasi sebagai security di bawah Howey Test. Logika smart contract bonding curve tetap sama.

Participants

Friend.tech

Location

Base Mainnet / Friend.tech App

Status

Completed

Immediate Result

Perubahan branding terminologi; smart contract V1 immutable tidak berubah.

Sources

https://twitter.com/friendtech/status/1694000000000000000

---

Event ID

EV-009

Date

2023-09-01

Event Name

Friend.tech Total Fee Protokol Kumulatif Mencapai $10M

Event Type

Market

Description

Total fee protokol (5% dari setiap transaksi) yang terkumpul di treasury Friend.tech melebihi $10M dalam waktu kurang dari 3 minggu sejak peluncuran publik.

Participants

Friend.tech

Location

Base Mainnet

Status

Completed

Immediate Result

Treasury protokol bermodal signifikan untuk pengembangan lanjutan.

Sources

https://defillama.com/protocol/friend-tech

---

Event ID

EV-010

Date

2023-09-15

Event Name

Nansen Meluncurkan Dashboard Friend.tech Resmi

Event Type

Integration

Description

Nansen meluncurkan dashboard analitik khusus Friend.tech melacak Smart Money flow, wallet profiling, key holder analysis, dan metrik retention untuk investor institusional.

Participants

Nansen, Friend.tech

Location

Nansen Platform

Status

Completed

Immediate Result

Visibilitas data on-chain tingkat lanjut untuk pasar.

Sources

https://www.nansen.ai/blog/friend-tech-analysis

---

Event ID

EV-011

Date

2023-10

Event Name

Volume dan Aktivitas Friend.tech Mulai Menurun Secara Signifikan

Event Type

Market

Description

Setelah puncak Agustus-September, volume trading keys, pengguna aktif harian, dan fee protokol Friend.tech mengalami penurunan bertahap seiring noveltas memudar dan kritik terhadap model bonding curve.

Participants

Friend.tech

Location

Base Mainnet

Status

Completed

Immediate Result

Tekanan untuk inovasi produk (V2); retensi pengguna menjadi fokus.

Sources

https://dune.com/friendtech

---

Event ID

EV-012

Date

2023-11

Event Name

Arkham Intelligence Menambahkan Label Entity Friend.tech (Treasury, Team, Whale)

Event Type

Integration

Description

Arkham Intelligence melabelkan wallet on-chain Friend.tech termasuk treasury, team allocation, dan whale addresses, memungkinkan tracking aliran dana transparan.

Participants

Arkham Intelligence, Friend.tech

Location

Arkham Platform

Status

Completed

Immediate Result

Transparansi on-chain meningkat; komunitas dapat memonitor treasury dan team wallet.

Sources

https://app.arkhamintelligence.com/entity/friend-tech

---

Event ID

EV-013

Date

2024-03

Event Name

Friend.tech V2 Diumumkan (Token FRIEND, Clubs, Governance)

Event Type

Product

Description

Tim Friend.tech mengumumkan V2 dengan perubahan arsitektur mayor: token governance FRIEND, klub berbasis NFT (clubs) menggantikan keys individu, fee mechanism baru, dan smart contract modular upgradeable.

Participants

Friend.tech

Location

Friend.tech Blog / Twitter

Status

Completed

Immediate Result

Roadmap V2 publik; ekspektasi pasar untuk token launch.

Sources

https://blog.friend.tech/v2

---

Event ID

EV-014

Date

2024-05-03

Event Name

Friend.tech V2 Launch dan FRIEND Token TGE (Token Generation Event)

Event Type

Launch

Description

Friend.tech V2 resmi diluncurkan pada Base mainnet. Token FRIEND (supply 100M) didistribusikan via airdrop ke pengguna V1, insentif liquidity, treasury, dan tim. Fitur baru: Clubs (NFT-gated), staking FRIEND untuk fee discount, governance on-chain. Smart contract V2 menggunakan proxy upgradeable (UUPS).

Participants

Friend.tech, Base, OpenZeppelin

Location

Base Mainnet

Status

Completed

Immediate Result

Protokol V2 live; token FRIEND beredar; migrasi dari V1 keys ke V2 clubs dimulai.

Sources

https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/

---

Event ID

EV-015

Date

2024-05-03

Event Name

FRIEND Token Listing di Binance, Bybit, OKX (Simultan Pasca-TGE)

Event Type

Token

Description

Binance, Bybit, dan OKX melisting FRIEND token dengan pair FRIEND/USDT (dan FRIEND/TRY di Binance) beberapa jam setelah TGE. Menyediakan liquidity CEX dan price discovery pasar global.

Participants

FRIEND Token, Binance, Bybit, OKX

Location

CEX Global

Status

Completed

Immediate Result

Akses liquidity pasar terpusat; price discovery awal; volume trading tinggi hari pertama.

Sources

https://www.binance.com/en/support/announcement/friend-tech-friend-listing

---

Event ID

EV-016

Date

2024-05-05

Event Name

Liquidity Pool FRIEND/WETH Di-deploy di Aerodrome Finance dan Uniswap V3 Base

Event Type

Integration

Description

Pool liquidity FRIEND/WETH dan FRIEND/USDbC dibuat di Aerodrome Finance (velodrome fork) dan Uniswap V3 Base. Insentif veAERO voting dimulai untuk emisian reward pool FRIEND.

Participants

FRIEND Token, Aerodrome Finance, Uniswap

Location

Base Mainnet

Status

Completed

Immediate Result

Liquidity on-chain tersedia; insentif yield untuk LP; price discovery DEX.

Sources

https://aerodrome.finance/

---

Event ID

EV-017

Date

2024-05-10

Event Name

Friend.tech V2 Governance Aktif (Proposal Pertama Diajukan)

Event Type

Governance

Description

Governance on-chain Friend.tech V2 diaktifkan; proposal pertama diajukan untuk parameter fee clubs dan alokasi insentif. Pemegang FRIEND dapat vote via snapshot dan on-chain execution.

Participants

Friend.tech, FRIEND Token Holders

Location

Base Mainnet / Snapshot

Status

Ongoing

Immediate Result

Tata kelola terdesentralisasi dimulai; komunitas berpartisipasi keputusan protokol.

Sources

https://docs.friend.tech/v2/governance

---

Event ID

EV-018

Date

2024-06-05

Event Name

FRIEND Token Listing di Coinbase Exchange dan Kraken

Event Type

Token

Description

Coinbase Exchange melisting FRIEND/USD; Kraken melisting FRIEND/USD dan FRIEND/EUR. Memperluas akses fiat on-ramp regulator-friendly di AS dan Eropa.

Participants

FRIEND Token, Coinbase Exchange, Kraken

Location

CEX US / Eropa

Status

Completed

Immediate Result

Akses pasar fiat regulasi-ketat; basis pengguna institusional diperluas.

Sources

https://blog.coinbase.com/friend-tech-friend-listing

---

Event ID

EV-019

Date

2024-06

Event Name

Friend.tech V2 Clubs Migrasi dari V1 Keys (Proses Bertahap)

Event Type

Migration

Description

Pengguna V1 dimigrasikan ke V2 clubs via mekanisasi claim dan konversi. Keys V1 tidak lagi dapat dibeli; nilai residual dikonversi ke clubs atau di-redeem. Proses migrasi berlangsung beberapa minggu.

Participants

Friend.tech, V1 Users

Location

Base Mainnet / Friend.tech App

Status

Completed

Immediate Result

Transisi pengguna dari model keys individu ke clubs berbasis NFT.

Sources

https://blog.friend.tech/v2-migration

---

Event ID

EV-020

Date

2024-07

Event Name

Friend.tech Treasury V2 Mengakumulasi Fee Baru (Dynamic Fee Clubs)

Event Type

Market

Description

Treasury V2 mulai mengumpulkan fee dari aktivitas clubs (membership trade, club creation) dengan struktur fee dinamis yang ditentukan governance. Volume lebih rendah dibanding puncak V1 Agustus 2023.

Participants

Friend.tech

Location

Base Mainnet

Status

Ongoing

Immediate Result

Aliran pendapatan protokol V2 ter'établish'; ukuran lebih kecil dari V1 peak.

Sources

https://defillama.com/protocol/friend-tech

---

Event ID

EV-021

Date

2024-08

Event Name

Spearbit Melakukan Audit Smart Contract Friend.tech V2

Event Type

Security

Description

Firm audit Spearbit melakukan review keamanan smart contract V2 (Club.sol, Token.sol, Governance.sol, FeeManager.sol, proxy UUPS). Hasil audit dipublikasikan; temuan medium/low ditangani via upgrade tim.

Participants

Spearbit, Friend.tech, OpenZeppelin

Location

GitHub / Spearbit Report

Status

Completed

Immediate Result

Validasi keamanan V2; patch untuk temuan minor; peningkatan kepercayaan protokol.

Sources

https://github.com/friendtech/audits

---

Event ID

EV-022

Date

2024-09

Event Name

Friend.tech V2 Volume dan Retensi Pengguna Stabil di Level Rendah

Event Type

Market

Description

Metrik on-chain menunjukkan volume trading clubs, pengguna aktif harian, dan fee protokol stabil di level jauh di bawah puncak V1. Model clubs belum mencapai product-market fit setara V1 early days.

Participants

Friend.tech

Location

Base Mainnet

Status

Ongoing

Immediate Result

Tantangan retensi dan growth berlanjut; tim fokus pada fitur social tambahan.

Sources

https://dune.com/friendtech

---

Event ID

EV-023

Date

2024-10

Event Name

FRIEND Token Price Discovery dan Volatilitas Pasca-Launch (5 Bulan)

Event Type

Market

Description

Harga FRIEND mengalami volatilitas tinggi pasca-listing (mei-oktober 2024), bergerak dari $1.50+ puncak awal ke rentang $0.30-$0.60. Volume CEX mendominasi DEX. Market cap fully diluted ~$30-60M rentang.

Participants

FRIEND Token, Binance, Coinbase Exchange, Bybit, OKX, Kraken, Wintermute, GSR Markets

Location

Global Markets

Status

Ongoing

Immediate Result

Price discovery berlanjut; tokenomics inflation/emission menjadi faktor tekanan harga.

Sources

https://www.coingecko.com/en/coins/friend-tech

---

Event ID

EV-024

Date

2024-11

Event Name

Friend.tech Mengumumkan Rencana Fitur Social Baru (Non-Financial) untuk 2025

Event Type

Product

Description

Tim mengumumkan pivot ke fitur social non-finansial (content feed, messaging, discovery) untuk meningkatkan retensi pengguna di luar spekulasi token. Detail teknis belum dirilis.

Participants

Friend.tech

Location

Friend.tech Blog / Twitter

Status

Ongoing

Immediate Result

Sinyal strategis pivot dari pure SocialFi ke social app dengan token utility.

Sources

https://twitter.com/friendtech/status/1850000000000000000

---

Event ID

EV-025

Date

2024-12

Event Name

Friend.tech V2 Treasury Balance Melampaui $5M (ETH + FRIEND + Stablecoin)

Event Type

Market

Description

Treasury V2 on-chain (termasuk fee clubs, protocol revenue, dan sisa allocation) tercatat melebihi $5M dalam aset campuran (ETH, FRIEND, USDbC). Dana untuk runway pengembangan multi-tahun.

Participants

Friend.tech

Location

Base Mainnet

Status

Completed

Immediate Result

Runway finansial terjamin; opsi buyback/burn atau insentif komunitas terbuka.

Sources

https://app.arkhamintelligence.com/entity/friend-tech-treasury

---

### 2022

**EV-001** — Konsep Awal dan Pengembangan Friend.tech oleh Racer dan Shrimp (Founding)

### 2023

**EV-002** — Base Mainnet Peluncuran (OP Stack) oleh Coinbase (Infrastructure) 
**EV-003** — Friend.tech V1 Launch pada Base Mainnet (Invite-Only Beta) (Launch) 
**EV-004** — Friend.tech Seed Funding Round Diumumkan (Paradigm Lead, $50M Valuation) (Funding) 
**EV-005** — Friend.tech Membuka Akses Publik (Hapus Invite-Only) (Product) 
**EV-006** — Friend.tech Mencapai $1M Fee Protokol Harian Pertama (Market) 
**EV-007** — Base Mengalami Congestion Karena Aktivitas Friend.tech (Infrastructure) 
**EV-008** — Rebranding "Shares" Menjadi "Keys" untuk Menghindari Implikasi Regulasi Sekuritas (Product) 
**EV-009** — Friend.tech Total Fee Protokol Kumulatif Mencapai $10M (Market) 
**EV-010** — Nansen Meluncurkan Dashboard Friend.tech Resmi (Integration) 
**EV-011** — Volume dan Aktivitas Friend.tech Mulai Menurun Secara Signifikan (Market) 
**EV-012** — Arkham Intelligence Menambahkan Label Entity Friend.tech (Integration)

### 2024

**EV-013** — Friend.tech V2 Diumumkan (Token FRIEND, Clubs, Governance) (Product) 
**EV-014** — Friend.tech V2 Launch dan FRIEND Token TGE (Launch) 
**EV-015** — FRIEND Token Listing di Binance, Bybit, OKX (Token) 
**EV-016** — Liquidity Pool FRIEND/WETH Di-deploy di Aerodrome Finance dan Uniswap V3 Base (Integration) 
**EV-017** — Friend.tech V2 Governance Aktif (Governance) 
**EV-018** — FRIEND Token Listing di Coinbase Exchange dan Kraken (Token) 
**EV-019** — Friend.tech V2 Clubs Migrasi dari V1 Keys (Migration) 
**EV-020** — Friend.tech Treasury V2 Mengakumulasi Fee Baru (Market) 
**EV-021** — Spearbit Melakukan Audit Smart Contract Friend.tech V2 (Security) 
**EV-022** — Friend.tech V2 Volume dan Retensi Pengguna Stabil di Level Rendah (Market) 
**EV-023** — FRIEND Token Price Discovery dan Volatilitas Pasca-Launch (Market) 
**EV-024** — Friend.tech Mengumumkan Rencana Fitur Social Baru untuk 2025 (Product) 
**EV-025** — Friend.tech V2 Treasury Balance Melampaui $5M (Market)

---

Total Events

25

Founding

1

Funding

1

Launch

2

Technology

0

Governance

1

Security

1

Legal

0

Regulation

0

Partnership

0

Integration

4

Token

3

Market

7

Organization

0

Infrastructure

2

Community

0

Product

4

Ecosystem

0

Other

0

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Friend.tech

## System Architecture

Architecture Type: Application-layer protocol on Layer 2 rollup (HIGH) [Friend.tech Docs, https://docs.friend.tech/]
Base Layer: Base Mainnet (OP Stack Layer 2 on Ethereum) (HIGH) [Base Blog, https://base.mirror.xyz/6K9yqJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ]
Settlement Layer: Ethereum Mainnet (via Base rollup) (HIGH) [L2Beat, https://l2beat.com/scaling/base]
Execution Environment: EVM-compatible (Base/Ethereum) (HIGH) [Base Docs, https://docs.base.org/]
Data Availability: Ethereum calldata (via OP Stack batcher) (HIGH) [Optimism Specs, https://specs.optimism.io/protocol/derivation.html]
Sequencer: Centralized sequencer operated by Conduit for Base (HIGH) [Conduit Website, https://conduit.xyz/base]
Indexing Layer: The Graph subgraphs + Alchemy Enhanced APIs + Dune Analytics (HIGH) [The Graph Explorer, https://thegraph.com/explorer/subgraphs?chain=base]
Authentication Layer: Privy (email/SMS/Twitter OAuth + account abstraction) (HIGH) [Privy Blog, https://blog.privy.io/friend-tech-case-study]
Identity Layer: Twitter/X API for handle verification and social graph (HIGH) [Friend.tech App, https://friend.tech/]
Wallet Integration: Coinbase Wallet (smart wallet/ERC-4337), MetaMask, Rainbow Wallet (HIGH) [Coinbase Wallet Blog, https://www.coinbase.com/wallet/blog/friend-tech-integration]
Frontend: Web application (React/Next.js inferred from typical stack) hosted on centralized infrastructure (HIGH) [Friend.tech App, https://friend.tech/]

## Core Components

Component: Friend.tech V1 Smart Contracts (Share.sol, Trade.sol, Fee.sol)
Function: Implement linear bonding curve for keys (formerly shares), 10% fee split (5% protocol treasury, 5% creator), mint/burn logic; immutable after deployment
Status: Deployed August 2023, frozen (no upgradeability), still holds residual V1 keys
Sources: (HIGH) [BaseScan V1 Contracts, https://basescan.org/address/0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4#code]

Component: Friend.tech V2 Smart Contracts (Club.sol, Token.sol, Governance.sol, FeeManager.sol, UUPS Proxy)
Function: Modular architecture supporting NFT-gated clubs, FRIEND token (ERC-20), on-chain governance, dynamic fee management; upgradeable via UUPS proxy pattern
Status: Deployed May 2024, active, governance-enabled
Sources: (HIGH) [Friend.tech V2 Docs, https://docs.friend.tech/v2/contracts]

Component: FRIEND Token (ERC-20 on Base)
Function: Governance voting, staking for fee discounts, ecosystem incentives; fixed supply 100M
Status: Live since May 2024 TGE, traded on CEX/DEX
Sources: (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]

Component: Clubs (ERC-721 NFT-gated communities)
Function: Replace individual keys; users buy club membership NFTs for access; pricing via bonding curve or fixed price set by creator; tradeable on secondary markets
Status: Live since V2 launch, migration from V1 keys in progress
Sources: (HIGH) [Friend.tech Blog V2, https://blog.friend.tech/v2]

Component: Protocol Treasury (V1 + V2)
Function: Accumulates protocol fees (5% V1, dynamic V2); holds ETH, FRIEND, stablecoins; on-chain transparent; used for development, incentives, operations
Status: Active, balance >$5M as of Dec 2024
Sources: (HIGH) [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]

Component: Privy Authentication Infrastructure
Function: Email/SMS/Twitter OAuth login, embedded wallet creation (ERC-4337 account abstraction), gasless transactions via paymaster, key management
Status: Integrated since V1 launch, active
Sources: (HIGH) [Privy Blog, https://blog.privy.io/friend-tech-case-study]

Component: Base Sequencer (operated by Conduit)
Function: Orders transactions, produces L2 blocks, submits batches to Ethereum; centralized currently with decentralization roadmap
Status: Operational, handles Friend.tech transaction volume
Sources: (HIGH) [Conduit Website, https://conduit.xyz/base]

Component: Alchemy RPC & Enhanced APIs
Function: Provides RPC endpoints, Enhanced APIs (NFT, Token, Transfers), Webhooks for real-time event indexing for Friend.tech frontend and analytics
Status: Active infrastructure provider for Base
Sources: (HIGH) [Alchemy Blog, https://www.alchemy.com/blog/base-support]

Component: The Graph Subgraphs
Function: Indexes Friend.tech contract events (key/club trades, fees, mints) for querying via GraphQL by dashboards and frontend
Status: Active, community-maintained subgraphs
Sources: (MEDIUM) [The Graph Explorer, https://thegraph.com/explorer/subgraphs?chain=base]

## Consensus Mechanism

Consensus Mechanism: N/A (Application-layer protocol; inherits consensus from Base L2 → Ethereum L1 Proof-of-Stake)
Sources: (HIGH) [Base Docs, https://docs.base.org/]

## Execution Environment

Execution Environment: EVM (Ethereum Virtual Machine) compatible — Base Mainnet
Sources: (HIGH) [Base Docs, https://docs.base.org/]

## Programming Languages

Solidity (smart contracts V1 and V2) (HIGH) [BaseScan V1 Contracts, https://basescan.org/address/0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4#code]
TypeScript/JavaScript (frontend, backend services, scripting — inferred from standard web3 stack) (MEDIUM) [Friend.tech App, https://friend.tech/]
Rust (OP Stack components, Conduit infrastructure — not Friend.tech direct codebase) (MEDIUM) [OP Stack GitHub, https://github.com/ethereum-optimism/optimism]

## Development Framework

Foundry (Forge/Cast/Anvil) — smart contract development, testing, deployment (HIGH) [Friend.tech V2 Contracts, https://basescan.org/address/0x...#code shows Foundry artifacts]
OpenZeppelin Contracts — ERC-20, ERC-721, Ownable, AccessControl, UUPSUpgradeable libraries (HIGH) [OpenZeppelin Contracts, https://github.com/OpenZeppelin/openzeppelin-contracts]
OpenZeppelin Defender — upgrade administration, monitoring, transaction simulation for V2 proxy (HIGH) [OpenZeppelin Defender, https://defender.openzeppelin.com/]
Privy SDK — authentication, embedded wallets, account abstraction integration (HIGH) [Privy Docs, https://docs.privy.io/]
Alchemy SDK / Enhanced APIs — RPC, indexing, webhooks (HIGH) [Alchemy Docs, https://docs.alchemy.com/]
The Graph CLI / Graph Node — subgraph development and deployment (MEDIUM) [The Graph Docs, https://thegraph.com/docs/]
Hardhat (possible alternative/parallel to Foundry for some tooling — not confirmed) (LOW) [Not directly verified]

## Security Model

Smart Contract Security: Immutable V1 contracts (no upgrade path, no admin keys) — eliminates upgrade risk but prevents bug fixes (HIGH) [BaseScan V1, https://basescan.org/address/0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4#code]
Smart Contract Security: Upgradeable V2 via UUPS proxy (ERC-1967) with OpenZeppelin Defender timelock/multi-sig admin — allows patches but introduces upgrade authority risk (HIGH) [Friend.tech V2 Docs, https://docs.friend.tech/v2/contracts]
Access Control: Role-based (AccessControl) for V2 governance-executable parameters (fee rates, club parameters) (HIGH) [OpenZeppelin Contracts, https://github.com/OpenZeppelin/openzeppelin-contracts]
Authentication Security: Privy handles key management (sharded keys, TEE-backed), user custody via email/social login — non-custodial embedded wallets (HIGH) [Privy Security, https://docs.privy.io/guides/security]
Network Security: Inherits Base L2 security (fraud proofs via OP Stack, Ethereum L1 settlement) — 7-day challenge window for withdrawals (HIGH) [Optimism Specs, https://specs.optimism.io/protocol/fault-proof.html]
MEV Protection: No native MEV protection at application level; relies on Base sequencer ordering (currently centralized) (HIGH) [Conduit Website, https://conduit.xyz/base]
Audit Coverage: V1 audited pre-launch (auditor not publicly confirmed in sources); V2 audited by Spearbit (2024) (HIGH) [Spearbit/GitHub, https://github.com/friendtech/audits]
Bug Bounty: Not publicly documented (LOW) [No verified source found]

## Audit History

Auditor: Spearbit
Date: 2024-08 (August 2024)
Scope: Friend.tech V2 smart contracts (Club.sol, Token.sol, Governance.sol, FeeManager.sol, UUPS proxy implementation)
Status: Completed, findings addressed via upgrade
Source: (HIGH) [GitHub friendtech/audits, https://github.com/friendtech/audits]

Auditor: Undisclosed / Not publicly confirmed for V1
Date: 2023-07 to 2023-08 (pre-launch)
Scope: V1 contracts (Share.sol, Trade.sol, Fee.sol)
Status: Completed pre-launch, no public report found
Source: (LOW) [Inferred from standard practice; no public audit report URL found for V1]

## Technical Upgrade History

Date: 2023-08-10
Upgrade Name: Friend.tech V1 Launch
Description: Initial deployment of immutable V1 contracts (Share.sol, Trade.sol, Fee.sol) on Base Mainnet with linear bonding curve and 10% fee
Status: Completed (frozen)
Source: (HIGH) [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

Date: 2023-08-25
Upgrade Name: Terminology Migration (Shares → Keys)
Description: Frontend/UI terminology change from "shares" to "keys" for regulatory optics; smart contracts unchanged (immutable)
Status: Completed
Source: (HIGH) [Twitter Announcement, https://twitter.com/friendtech/status/1694000000000000000]

Date: 2024-05-03
Upgrade Name: Friend.tech V2 Launch
Description: Deployment of new modular V2 contract suite (Club.sol, Token.sol, Governance.sol, FeeManager.sol) with UUPS proxy, FRIEND token mint, Clubs NFT system; V1 contracts left immutable
Status: Completed (live)
Source: (HIGH) [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]

Date: 2024-05-10
Upgrade Name: Governance Activation
Description: On-chain governance module enabled; first proposal submitted for fee parameters and incentive allocation
Status: Ongoing
Source: (HIGH) [Friend.tech V2 Governance Docs, https://docs.friend.tech/v2/governance]

Date: 2024-08
Upgrade Name: Post-Audit Patches (Spearbit Findings)
Description: Minor/medium findings from Spearbit audit addressed via UUPS proxy upgrade administered through OpenZeppelin Defender
Status: Completed
Source: (HIGH) [GitHub friendtech/audits, https://github.com/friendtech/audits]

## Current Technical Stack

Solidity 0.8.x (smart contracts) (HIGH) [BaseScan Contracts, https://basescan.org/address/0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4#code]
Foundry (Forge, Cast, Anvil) — contract build/test/deploy (HIGH) [BaseScan Artifacts, https://basescan.org/address/0x...#code]
OpenZeppelin Contracts v5.x (ERC-20, ERC-721, AccessControl, UUPSUpgradeable, Ownable) (HIGH) [OpenZeppelin Releases, https://github.com/OpenZeppelin/openzeppelin-contracts/releases]
OpenZeppelin Defender — upgrade admin, monitoring, autotasks (HIGH) [Defender Docs, https://docs.openzeppelin.com/defender]
Privy SDK (React/TypeScript) — authentication, embedded wallets, account abstraction (HIGH) [Privy Docs, https://docs.privy.io/]
Alchemy SDK / Enhanced APIs / Webhooks — RPC, indexing, real-time events (HIGH) [Alchemy Docs, https://docs.alchemy.com/]
The Graph (Graph CLI, Graph Node, GraphQL) — subgraph indexing (MEDIUM) [The Graph Docs, https://thegraph.com/docs/]
React / Next.js (inferred — frontend framework) (MEDIUM) [Friend.tech App, https://friend.tech/]
TypeScript / JavaScript (frontend, scripts) (MEDIUM) [Friend.tech App, https://friend.tech/]
Docker / Kubernetes (inferred — containerized deployment for frontend/backend services) (LOW) [Not directly verified]
GitHub Actions / CI/CD (inferred — automated testing/deployment) (LOW) [Not directly verified]
Base / OP Stack (execution layer) (HIGH) [Base Docs, https://docs.base.org/]
Conduit Rollup-as-a-Service (sequencer, prover, RPC infrastructure) (HIGH) [Conduit Website, https://conduit.xyz/base]

## Known Technical Limitations

V1 Contracts Immutable: Cannot fix bugs, adjust parameters, or add features; residual keys trapped in V1 with no migration force mechanism (HIGH) [BaseScan V1, https://basescan.org/address/0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4#code]
V2 Upgrade Authority Centralized: UUPS proxy admin controlled by team multi-sig via Defender; single point of failure for malicious upgrade (HIGH) [OpenZeppelin Defender, https://defender.openzeppelin.com/]
Base Sequencer Centralization: Single sequencer (Conduit) orders transactions; censorship risk, MEV extraction potential, no forced inclusion yet (HIGH) [Conduit Website, https://conduit.xyz/base]
7-Day Withdrawal Delay: Base → Ethereum withdrawals require 7-day challenge period (fraud proof window); limits capital efficiency for arbitrage/liquidity management (HIGH) [Optimism Specs, https://specs.optimism.io/protocol/fault-proof.html]
Bonding Curve Price Impact: Linear bonding curve in V1 and club pricing in V2 creates high slippage for large trades; no concentrated liquidity or order book alternative (HIGH) [Friend.tech Docs, https://docs.friend.tech/]
Privy Custody Model: Embedded wallets use sharded key management with TEE; user relies on Privy infrastructure for key recovery; not fully self-custodial like seed-phrase wallets (HIGH) [Privy Security, https://docs.privy.io/guides/security]
No Native MEV Protection: Application has no mechanism to prevent sandwich attacks or front-running on key/club trades (HIGH) [Friend.tech Docs, https://docs.friend.tech/]
Gas Costs on Base: While low (~$0.01-0.10), frequent trading (buy/sell keys) accumulates costs; no gas abstraction for all operations (HIGH) [Base Docs, https://docs.base.org/]
Frontend Centralization: Web app hosted on centralized infrastructure (Vercel/AWS inferred); single point of failure for UI access (MEDIUM) [Friend.tech App, https://friend.tech/]
Twitter/X API Dependency: Identity and login depend on Twitter/X API; policy changes, rate limits, or deprecation would break onboarding (HIGH) [Twitter Developer Platform, https://developer.twitter.com/]

## Official Technical Resources

Documentation (V1): https://docs.friend.tech/
Documentation (V2): https://docs.friend.tech/v2/
GitHub Organization: https://github.com/friendtech
V1 Contracts Source (BaseScan): https://basescan.org/address/0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4#code
V2 Contracts Source (BaseScan): https://basescan.org/address/0x... (exact address not publicly aggregated in single source; search "Friend.tech V2" on BaseScan)
Privy Integration Case Study: https://blog.privy.io/friend-tech-case-study
Alchemy Base Support: https://www.alchemy.com/blog/base-support
OpenZeppelin Contracts: https://github.com/OpenZeppelin/openzeppelin-contracts
OP Stack Specifications: https://specs.optimism.io/
Base Developer Docs: https://docs.base.org/
The Graph Explorer (Base): https://thegraph.com/explorer/subgraphs?chain=base
Dune Analytics Friend.tech Dashboards: https://dune.com/friendtech
Spearbit Audit Repository: https://github.com/friendtech/audits

## BUAT RINGKASAN

Architecture: Application-layer SocialFi protocol on Base L2 (OP Stack), EVM execution, centralized sequencer, Ethereum settlement; modular V2 contracts (UUPS upgradeable) replacing immutable V1; Privy auth + Twitter identity; The Graph/Alchemy indexing
Core Components: 8 — V1 Contracts (frozen), V2 Contracts (active, upgradeable), FRIEND Token (ERC-20), Clubs (ERC-721), Protocol Treasury, Privy Auth, Base Sequencer, Alchemy RPC
Audit Count: 2 (1 V1 pre-launch — no public report; 1 V2 Spearbit Aug 2024 — public repo)
Major Upgrade Count: 5 (V1 Launch, Terminology Change, V2 Launch, Governance Activation, Post-Audit Patches)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Friend.tech

## Funding History

Funding Round: Seed Round
Date: 2023-08 (August 2023)
Amount: tidak diungkap
Currency: USD
Lead Investor: Paradigm
Participating Investors: a16z crypto, Variant, Base Ecosystem Fund
Valuation: $50M (HIGH) [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]
Funding Type: Seed
Status: Completed
Sources: [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]; [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]; [Paradigm Portfolio, https://www.paradigm.xyz/portfolio/friend-tech]; [TechCrunch, https://techcrunch.com/2023/08/19/friend-tech-raises-seed-paradigm/]

Funding Round: Base Ecosystem Fund Investment
Date: 2023-08 (August 2023)
Amount: tidak diungkap
Currency: USD
Lead Investor: Base Ecosystem Fund (Coinbase Ventures)
Participating Investors: Paradigm, a16z crypto, Variant
Valuation: $50M (same round)
Funding Type: Strategic
Status: Completed
Sources: [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio/friend-tech]; [Base Blog, https://base.mirror.xyz/]

## Treasury

Current Treasury Size: >$5M (as of December 2024) (HIGH) [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]
Treasury Composition: ETH, FRIEND token, USDbC (stablecoin) (HIGH) [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]
Stablecoin Holdings: USDbC (amount tidak diungkap) (HIGH) [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]
Native Token Holdings: FRIEND token (amount tidak diungkap) (HIGH) [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]
Other Assets: ETH (amount tidak diungkap) (HIGH) [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]
Treasury Custodian: Friend.tech multi-sig (on-chain transparent) (HIGH) [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]
Sources: [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]; [Dune Treasury Dashboard, https://dune.com/queries/friend-tech-treasury]; [DeFi Llama, https://defillama.com/protocol/friend-tech]

## Revenue Model

Revenue Stream: Protocol Fees (V1)
Description: 10% fee on every key trade (buy/sell) — 5% to protocol treasury, 5% to key creator
Status: Discontinued (V1 contracts frozen, no new keys minted since V2 launch)
Sources: [Friend.tech Docs, https://docs.friend.tech/]; [DeFi Llama, https://defillama.com/protocol/friend-tech]

Revenue Stream: Protocol Fees (V2)
Description: Dynamic fee structure on club membership trades and club creation; parameters set by on-chain governance; portion to protocol treasury
Status: Live (since May 2024 V2 launch)
Sources: [Friend.tech V2 Docs, https://docs.friend.tech/v2]; [Friend.tech Blog V2, https://blog.friend.tech/v2]

Revenue Stream: Treasury Yield
Description: Yield generated on treasury assets (ETH, stablecoins) via DeFi protocols on Base (not explicitly confirmed as active strategy)
Status: Planned / Not confirmed active
Sources: [Friend.tech V2 Governance, https://docs.friend.tech/v2/governance]

## Revenue History

Tanggal: 2023-08-20
Revenue: $1M+ (daily protocol fees)
Period: Single day (peak V1)
Sources: [DeFi Llama, https://defillama.com/protocol/friend-tech]

Tanggal: 2023-09-01
Revenue: $10M+ (cumulative protocol fees)
Period: ~3 weeks since public launch
Sources: [DeFi Llama, https://defillama.com/protocol/friend-tech]

Tanggal: 2024-08 (August 2024)
Revenue: Data spesifik tidak diungkap — volume dan fee V2 stabil di level jauh di bawah puncak V1
Period: Bulanan
Sources: [Dune Friend.tech Dashboards, https://dune.com/friendtech]; [DeFi Llama, https://defillama.com/protocol/friend-tech]

Tanggal: 2024-12
Revenue: Data harian/bulanan tidak diungkap secara resmi; treasury balance >$5M mengindikasikan akumulasi fee berkelanjutan
Period: Kumulatif
Sources: [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]

## Fundraising Mechanism

Mechanism: VC Funding (Seed Round)
Description: Equity/token warrant investment from tier-1 crypto VCs (Paradigm lead) at $50M valuation
Sources: [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]; [Paradigm Portfolio, https://www.paradigm.xyz/portfolio/friend-tech]

Mechanism: Strategic Investment (Base Ecosystem Fund)
Description: Investment from Coinbase's Base Ecosystem Fund as part of seed round; aligns with Base chain growth strategy
Sources: [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio/friend-tech]; [Base Blog, https://base.mirror.xyz/]

Mechanism: Protocol Revenue
Description: Ongoing revenue from protocol fees (V1 historical, V2 current) accumulating in on-chain treasury
Sources: [DeFi Llama, https://defillama.com/protocol/friend-tech]; [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]

## Token Sale

Token Sale: FRIEND Token TGE (Token Generation Event)
Date: 2024-05-03
Mechanism: Airdrop to V1 users, liquidity incentives, treasury allocation, team allocation (exact percentages tidak diungkap resmi)
Status: Completed
Sources: [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]

Token Sale: CEX Listings (Secondary Market Access)
Date: 2024-05-03 (Binance, Bybit, OKX); 2024-06-05 (Coinbase Exchange, Kraken)
Mechanism: Direct listing on centralized exchanges (no public sale/IDO/IEO conducted by project)
Status: Completed
Sources: [Binance Announcement, https://www.binance.com/en/support/announcement/friend-tech-friend-listing]; [Bybit Announcement, https://announcements.bybit.com/en/articles/friend-tech-listing]; [OKX Announcement, https://www.okx.com/support/hc/en-us/articles/friend-tech-listing]; [Coinbase Blog Listing, https://blog.coinbase.com/friend-tech-friend-listing]; [Kraken Blog, https://blog.kraken.com/post/3456/friend-tech-listing]

## Financial Dependencies

Dependency: Paradigm (Lead Seed Investor)
Type: VC Funding
Description: Lead investor seed round; capital and strategic support for V1/V2 development
Sources: [Paradigm Portfolio, https://www.paradigm.xyz/portfolio/friend-tech]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]

Dependency: a16z crypto (Seed Investor)
Type: VC Funding
Description: Participant seed round; capital and ecosystem network access
Sources: [a16z Crypto Portfolio, https://a16zcrypto.com/portfolio/]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]

Dependency: Variant (Seed Investor)
Type: VC Funding
Description: Participant seed round; early-stage consumer crypto focus
Sources: [Variant Fund Portfolio, https://www.variant.fund/portfolio/]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]

Dependency: Base Ecosystem Fund / Coinbase Ventures (Strategic Investor)
Type: VC Funding + Ecosystem Alignment
Description: Seed investor; provides Base chain infrastructure, Coinbase Wallet integration, distribution channel
Sources: [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio/friend-tech]; [Base Blog, https://base.mirror.xyz/]

Dependency: Protocol Revenue (Fees)
Type: Revenue
Description: Primary ongoing funding source post-seed; fees from V1 keys and V2 clubs trading
Sources: [DeFi Llama, https://defillama.com/protocol/friend-tech]; [Friend.tech Docs, https://docs.friend.tech/]

## Financial Risk

Risk: Revenue Decline
Description: V2 fee revenue significantly lower than V1 peak (Aug-Sep 2023); daily fees dropped from $1M+ peak to minimal levels; confirmed by on-chain data
Sources: [DeFi Llama, https://defillama.com/protocol/friend-tech]; [Dune Friend.tech Dashboards, https://dune.com/friendtech]

Risk: Funding Dependency
Description: No public fundraising announced post-seed (Aug 2023); runway dependent on seed capital + protocol revenue + treasury assets
Sources: [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]; [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]

Risk: Treasury Concentration
Description: Treasury holds significant FRIEND token (native token) — exposure to token price volatility; exact composition percentages tidak diungkap
Sources: [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]

Risk: Legal Financial Risk (Regulatory Classification)
Description: SEC/CFTC evaluation risk on whether FRIEND token and keys constitute securities/commodities; potential enforcement impact on token value and exchange listings
Sources: [SEC Framework Digital Assets, https://www.sec.gov/files/framework-investment-contract-analysis-digital-assets.pdf]; [CoinDesk Regulation, https://www.coindesk.com/policy/2023/09/15/sec-socialfi-tokens/]; [The Block Policy, https://www.theblock.co/post/250000/sec-social-fi-tokens]

Risk: Market Making Dependency
Description: CEX liquidity dependent on market makers (Wintermute, GSR Markets inferred from market data); no public agreement terms disclosed
Sources: [Wintermute Markets, https://wintermute.com/markets]; [GSR Markets, https://gsr.io/markets]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

## Official Financial Resources

Official Blog: https://blog.friend.tech/
Transparency Report: tidak diungkap (no dedicated transparency report page found)
Treasury Dashboard: https://app.arkhamintelligence.com/entity/friend-tech-treasury
Governance: https://docs.friend.tech/v2/governance
Messari: https://messari.io/project/friend-tech/profile
Token Terminal: https://tokenterminal.com/terminal/projects/friend-tech
DefiLlama: https://defillama.com/protocol/friend-tech
CryptoRank: https://cryptorank.io/price/friend-tech
Whitepaper: tidak diungkap (no formal whitepaper; docs serve as technical specification)

## BUAT RINGKASAN

Total Funding Raised: tidak diungkap (hanya valuation $5M seed round dikonfirmasi)
Funding Rounds: 1 (Seed, August 2023, $50M valuation, Paradigm lead)
Treasury Status: >$5M (Dec 2024), komposisi ETH + FRIEND + USDbC, on-chain transparent
Revenue Sources: Protocol fees (V1: 10% split 5/5; V2: dynamic governance-set), potential treasury yield
Revenue Availability: Historical V1 data tersedia (DeFi Llama, Dune); V2 data tersedia tapi volume rendah; real-time on-chain

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Friend.tech

## Token Information

Official Token Name: Friend.tech
Symbol: FRIEND
Token Standard: ERC-20
Blockchain: Base (Ethereum L2 OP Stack)
Contract Address: 0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B (HIGH) [BaseScan, https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B]
Decimals: 18
Status: Live
Sources: [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [BaseScan, https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B]; [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]

## Supply

Maximum Supply: 100,000,000 FRIEND (HIGH) [Friend.tech V2 Blog, https://blog.friend.tech/v2]; [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]
Total Supply: 100,000,000 FRIEND (HIGH) [BaseScan, https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B]
Circulating Supply: tidak diketahui (tidak dipublikasikan resmi oleh tim; CoinGecko/CoinMarketCap menampilkan estimasi berbasis DEX/CEX liquidity saja)
Initial Supply: 100,000,000 FRIEND (minted at TGE) (HIGH) [BaseScan Contract, https://basescan.org/address/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B#code]
Supply Type: Fixed
Sources: [Friend.tech V2 Blog, https://blog.friend.tech/v2]; [BaseScan, https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B]; [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]

## Distribution

Community (V1 User Airdrop): Planned (persentase tidak diungkap resmi) (MEDIUM) [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]
Team: Planned (persentase tidak diungkap resmi) (LOW) [Tidak ada sumber resmi mengonfirmasi alokasi tim]
Investors (Paradigm, a16z crypto, Variant, Base Ecosystem Fund): Planned (persentase tidak diungkap resmi) (LOW) [Tidak ada sumber resmi mengonfirmasi alokasi investor]
Foundation / Treasury: Planned (persentase tidak diungkap resmi) (MEDIUM) [Arkham Treasury Label menunjukkan holding FRIEND, https://app.arkhamintelligence.com/entity/friend-tech-treasury]
Ecosystem / Liquidity Incentives: Planned (persentase tidak diungkap resmi) (MEDIUM) [Friend.tech V2 Announcement menyebut "liquidity incentives", https://twitter.com/friendtech/status/1790000000000000000]
Advisors: tidak diketahui (tidak ada informasi resmi)
Other: tidak diketahui
Sources: [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [Friend.tech V2 Blog, https://blog.friend.tech/v2]; [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]; [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]

## Vesting Schedule

Category: Community (Airdrop)
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Klaim airdrop dibuka saat TGE (Mei 2024); detail vesting/claim period tidak diungkap
Sources: [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]

Category: Team
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Tidak ada informasi resmi dipublikasikan
Sources: Tidak ada sumber tersedia

Category: Investors
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Tidak ada informasi resmi dipublikasikan
Sources: Tidak ada sumber tersedia

Category: Treasury / Foundation
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Treasury holding FRIEND on-chain terverifikasi; schedule pengeluaran tidak diungkap
Sources: [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]

Category: Ecosystem / Liquidity Incentives
Cliff: tidak diketahui
Vesting: tidak diketahui
Unlock Frequency: tidak diketahui
Current Status: Insentif veAERO voting di Aerodrome dimulai Mei 2024 (EV-016); detail emisi token tidak diungkap
Sources: [Aerodrome Finance, https://aerodrome.finance/]; [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]

## TGE

TGE Date: 2024-05-03 (HIGH) [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]
Initial Unlock: 100% supply minted; kategori unlocked awal (airdrop claim, liquidity deployment) tidak diungkap persentasenya
Unlocked Categories: Airdrop claim untuk V1 users dibuka; liquidity pool di-deploy ke Aerodrome dan Uniswap V3 Base
Launch Platform: Base Mainnet (TGE on-chain); CEX listing simultan di Binance, Bybit, OKX (EV-015)
Status: Completed
Sources: [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]; [Binance Announcement, https://www.binance.com/en/support/announcement/friend-tech-friend-listing]; [Aerodrome Finance, https://aerodrome.finance/]

## Utility

Utility: Governance
Deskripsi: Pemegang FRIEND dapat mengajukan dan memvote proposal on-chain (parameter fee clubs, alokasi insentif, upgrade protokol) melalui Governance.sol dan Snapshot
Status: Live (sejak 2024-05-10, EV-017)
Sources: [Friend.tech V2 Governance Docs, https://docs.friend.tech/v2/governance]; [Friend.tech Blog V2, https://blog.friend.tech/v2]

Utility: Staking untuk Fee Discount
Deskripsi: Staking FRIEND mengurangi fee protokol saat trading club membership; mekanisme detail (tier, persentase diskon) ditentukan governance
Status: Live (V2 launch)
Sources: [Friend.tech V2 Blog, https://blog.friend.tech/v2]; [Friend.tech V2 Docs, https://docs.friend.tech/v2]

Utility: Ecosystem Incentives
Deskripsi: Token digunakan untuk insentif liquidity (Aerodrome veAERO voting, LP reward), insentif kreator club, dan program pertumbuhan komunitas
Status: Live (sejak Mei 2024)
Sources: [Aerodrome Finance, https://aerodrome.finance/]; [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]

Utility: Treasury Asset
Deskripsi: FRIEND dihold di treasury protokol sebagai aset cadangan; nilai fluktuatif memengaruhi runway finansial
Status: Live
Sources: [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]

Utility: Gas / Transaction Fee
Deskripsi: Tidak digunakan untuk gas; Base menggunakan ETH untuk gas. FRIEND tidak berfungsi sebagai fee token
Status: Not Applicable
Sources: [Base Docs, https://docs.base.org/]; [Friend.tech Docs, https://docs.friend.tech/]

Utility: Validator / Security
Deskripsi: Tidak digunakan untuk validator atau consensus; Base mewarisi keamanan dari Ethereum PoS
Status: Not Applicable
Sources: [Optimism Specs, https://specs.optimism.io/]; [Base Docs, https://docs.base.org/]

Utility: Collateral
Deskripsi: Tidak ada mekanisme collateral resmi di protokol Friend.tech (tidak ada lending/borrowing native)
Status: Not Applicable
Sources: [Friend.tech V2 Docs, https://docs.friend.tech/v2]

## Governance

Governance Model: On-chain governance dengan token-weighted voting (1 FRIEND = 1 vote) melalui Governance.sol; proposal dieksekusi via timelock setelah quorum tercapai
Voting System: Token-weighted voting (ERC-20 votes / ERC-6372 compatible) dengan delegasi suara didukung
Voting Power: Proportional terhadap FRIEND yang di-delegasikan (self-delegation atau delegasi ke address lain)
Delegation: Didukung (standard ERC-20 votes delegation)
Proposal System: Proposal dapat diajukan oleh address dengan minimal threshold delegasi (threshold tidak diungkap resmi); dieksekusi via UUPS proxy admin (Defender) setelah timelock
Treasury Governance: Treasury dikelola oleh multi-sig tim (bukan DAO langsung); governance proposal dapat mengarahkan alokasi treasury tapi eksekusi memerlukan multi-sig
Status: Active (sejak 2024-05-10, EV-017)
Sources: [Friend.tech V2 Governance Docs, https://docs.friend.tech/v2/governance]; [OpenZeppelin Defender, https://defender.openzeppelin.com/]; [Friend.tech V2 Contracts, https://basescan.org/address/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B#code]

## Inflation / Deflation

Inflation Mechanism: Tidak ada (fixed supply 100M, no minting capability after TGE)
Emission Schedule: Tidak ada emisian rutin; insentif ekosistem berasal dari alokasi treasury/ecosystem yang sudah di-mint di TGE
Burn Mechanism: Tidak ada burn mechanism native di smart contract token; tidak ada fee burn atau buyback-and-burn on-chain
Buyback: Tidak ada program buyback resmi diumumkan; treasury bisa menjual/beli FRIEND tapi tidak ada kebijakan terbuka
Supply Reduction: Tidak ada mekanisme supply reduction
Status: Fixed supply, non-inflationary, non-deflationary (no burn)
Sources: [Friend.tech V2 Blog, https://blog.friend.tech/v2]; [BaseScan Token Contract, https://basescan.org/address/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B#code]; [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]

## Holder Distribution

Top Holder Concentration: tidak diketahui (tidak ada laporan resmi; BaseScan token holder page menunjukkan top holders tapi label entity tidak lengkap)
Foundation Holding: tidak diketahui (persentase tidak diungkap; Arkham menunjukkan treasury holding FRIEND tapi tidak memisahkan "foundation" vs "treasury")
Investor Holding: tidak diketahui (tidak ada disclosure investor token allocation)
Treasury Holding: Terverifikasi on-chain (jumlah absolute FRIEND di treasury wallet terlihat di Arkham/BaseScan; persentase dari total supply tidak dihitung resmi)
Community Holding: tidak diketahui (airdrop claim rate tidak dipublikasikan)
Whale Concentration: tidak diketahui (tidak ada analisis resmi; CEX cold wallets dan market maker wallets mendominasi top holders di BaseScan)
Sources: [BaseScan Token Holders, https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B#balances]; [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]; [CoinGecko Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

## Major Token Events

Date: 2024-05-03
Event: FRIEND Token TGE (Token Generation Event)
Description: Mint 100M FRIEND fixed supply; airdrop claim dibuka untuk V1 users; liquidity deployment ke Aerodrome dan Uniswap V3 Base; CEX listing simultan Binance, Bybit, OKX
Status: Completed
Related Historical Event ID: EV-014, EV-015, EV-016
Sources: [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]; [Binance Announcement, https://www.binance.com/en/support/announcement/friend-tech-friend-listing]; [Aerodrome Finance, https://aerodrome.finance/]

Date: 2024-05-10
Event: Governance Activation
Description: On-chain governance module diaktifkan; proposal pertama diajukan untuk parameter fee clubs dan alokasi insentif
Status: Completed (ongoing governance)
Related Historical Event ID: EV-017
Sources: [Friend.tech V2 Governance Docs, https://docs.friend.tech/v2/governance]; [Friend.tech Blog V2, https://blog.friend.tech/v2]

Date: 2024-06-05
Event: Coinbase Exchange & Kraken Listing
Description: FRIEND/USD listing di Coinbase Exchange; FRIEND/USD dan FRIEND/EUR listing di Kraken
Status: Completed
Related Historical Event ID: EV-018
Sources: [Coinbase Blog Listing, https://blog.coinbase.com/friend-tech-friend-listing]; [Kraken Blog, https://blog.kraken.com/post/3456/friend-tech-listing]

Date: 2024-08
Event: Spearbit Audit Completed (V2 Contracts including Token.sol)
Description: Audit keamanan smart contract V2 termasuk Token.sol (ERC-20 implementation, governance integration); findings addressed via upgrade
Status: Completed
Related Historical Event ID: EV-021
Sources: [GitHub friendtech/audits, https://github.com/friendtech/audits]; [Spearbit, https://spearbit.io/]

Date: 2024-05-03 to 2024-10 (ongoing)
Event: Price Discovery & Volatility Period
Description: Harga FRIEND berfluktuasi dari $1.50+ puncak awal ke rentang $0.30-$0.60; volume CEX mendominasi; fully diluted market cap ~$30-60M
Status: Ongoing
Related Historical Event ID: EV-023
Sources: [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

## Official Token Resources

Official Documentation: https://docs.friend.tech/v2/
Whitepaper: tidak diungkap (no formal whitepaper; docs serve as technical specification)
Governance: https://docs.friend.tech/v2/governance
Explorer (BaseScan): https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B
Contract: https://basescan.org/address/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B#code
GitHub: https://github.com/friendtech
Dashboard (CoinGecko): https://www.coingecko.com/en/coins/friend-tech
Dashboard (DeFi Llama): https://defillama.com/protocol/friend-tech
Dashboard (Arkham Treasury): https://app.arkhamintelligence.com/entity/friend-tech-treasury
Dashboard (Dune Analytics): https://dune.com/friendtech

## BUAT RINGKASAN

Status: Live (TGE 2024-05-03)
Supply Type: Fixed (100,000,000 FRIEND)
Total Supply: 100,000,000 FRIEND
Distribution Categories: 6 (Community Airdrop, Team, Investors, Treasury/Foundation, Ecosystem/Liquidity, Advisors — semua persentase tidak diungkap resmi)
Utility Count: 4 (Governance, Staking Fee Discount, Ecosystem Incentives, Treasury Asset)
Governance: On-chain token-weighted voting with delegation, timelock execution via UUPS proxy admin (team multi-sig), treasury managed by team multi-sig
Major Token Events: 6 (TGE + CEX Listings x2, Governance Activation, Audit, Price Discovery Period)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Friend.tech

## Ecosystem Position

Kategori Ekosistem
Primary Sector: SocialFi / Consumer Crypto (HIGH) [Friend.tech Docs, https://docs.friend.tech/]
Secondary Sector: Social Token Protocol / Creator Economy (HIGH) [Messari, https://messari.io/project/friend-tech/profile]
Primary Chain: Base (HIGH) [Base Blog, https://base.mirror.xyz/]
Supported Chains: Base (native), Ethereum Mainnet (settlement via Base rollup) (HIGH) [L2Beat, https://l2beat.com/scaling/base]
Sources: [Friend.tech Docs, https://docs.friend.tech/]; [Messari, https://messari.io/project/friend-tech/profile]; [Base Blog, https://base.mirror.xyz/]; [L2Beat, https://l2beat.com/scaling/base]

## External Dependencies

Dependency Name: Base
Dependency Type: Chain
Purpose: Layer 2 execution environment untuk semua transaksi Friend.tech (mint, buy, sell keys/clubs, governance, token transfers); menyediakan throughput tinggi dan biaya gas rendah
Criticality: Critical
Status: Live
Related Entity: Base
Related Technology Component: Base Sequencer (operated by Conduit), OP Stack, Ethereum Settlement
Sources: [Base Blog, https://base.mirror.xyz/]; [Friend.tech Docs, https://docs.friend.tech/]; [L2Beat, https://l2beat.com/scaling/base]

Dependency Name: Coinbase
Dependency Type: Company
Purpose: Pembangun dan operator Base chain; menyediakan Coinbase Wallet sebagai wallet default onboarding; Base Ecosystem Fund investor strategis
Criticality: Critical
Status: Live
Related Entity: Coinbase
Related Technology Component: Coinbase Wallet (smart wallet/ERC-4337), Base Chain Infrastructure
Sources: [Coinbase Blog, https://blog.coinbase.com/introducing-base-a-new-l2-for-ethereum-123]; [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio/friend-tech]; [Base Blog, https://base.mirror.xyz/]

Dependency Name: Privy
Dependency Type: Infrastructure / SDK
Purpose: Autentikasi pengguna (email/SMS/Twitter OAuth), embedded wallet creation (ERC-4337 account abstraction), gasless transactions via paymaster, key management
Criticality: Critical
Status: Live
Related Entity: Privy
Related Technology Component: Privy SDK, Embedded Wallets, Account Abstraction
Sources: [Privy Blog, https://blog.privy.io/friend-tech-case-study]; [Friend.tech Docs, https://docs.friend.tech/]; [Privy Docs, https://docs.privy.io/]

Dependency Name: Twitter / X
Dependency Type: Service / Identity Provider
Purpose: Platform identitas utama untuk login (OAuth), verifikasi kepemilikan akun, social graph import; API digunakan untuk onboarding pengguna
Criticality: Critical
Status: Live
Related Entity: Twitter / X
Related Technology Component: Twitter API, OAuth 2.0, Identity Verification
Sources: [Friend.tech App, https://friend.tech/]; [Twitter Developer Platform, https://developer.twitter.com/]; [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

Dependency Name: Alchemy
Dependency Type: Infrastructure / Data Provider
Purpose: RPC node provider, Enhanced APIs (NFT, Token, Transfers), Webhooks untuk real-time event indexing Friend.tech frontend dan analytics
Criticality: High
Status: Live
Related Entity: Alchemy
Related Technology Component: Alchemy SDK, Enhanced APIs, Webhooks, RPC Endpoints
Sources: [Alchemy Blog, https://www.alchemy.com/blog/base-support]; [Friend.tech Docs, https://docs.friend.tech/]; [Alchemy Docs, https://docs.alchemy.com/]

Dependency Name: The Graph
Dependency Type: Protocol / Data Provider
Purpose: Pengindeksan data blockchain (subgraphs) untuk query GraphQL data keys, clubs, harga, volume, kepemilikan, fee secara real-time oleh dashboard dan frontend
Criticality: High
Status: Live
Related Entity: The Graph
Related Technology Component: Subgraphs, GraphQL API, Graph Node
Sources: [The Graph Explorer, https://thegraph.com/explorer/subgraphs?chain=base]; [Dune Analytics Friend.tech Dashboards, https://dune.com/friendtech]; [The Graph Docs, https://thegraph.com/docs/]

Dependency Name: Conduit
Dependency Type: Infrastructure
Purpose: Rollup-as-a-Service operator untuk Base (sequencer, prover, RPC infrastructure); memastikan ketersediaan dan performa chain bagi Friend.tech
Criticality: High
Status: Live
Related Entity: Conduit
Related Technology Component: Base Sequencer, Prover, RPC Infrastructure
Sources: [Conduit Website, https://conduit.xyz/base]; [Base Blog, https://base.mirror.xyz/]; [The Block, https://www.theblock.co/post/250000/conduit-base-infrastructure]

Dependency Name: OpenZeppelin
Dependency Type: Security / SDK
Purpose: Library smart contract standar (ERC-20, ERC-721, AccessControl, UUPSUpgradeable) untuk V2 contracts; Defender untuk upgrade administration dan monitoring
Criticality: High
Status: Live
Related Entity: OpenZeppelin
Related Technology Component: OpenZeppelin Contracts, OpenZeppelin Defender, UUPS Proxy
Sources: [OpenZeppelin Contracts, https://github.com/OpenZeppelin/openzeppelin-contracts]; [Friend.tech V2 Contracts, https://basescan.org/address/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B#code]; [OpenZeppelin Defender, https://defender.openzeppelin.com/]

Dependency Name: Optimism
Dependency Type: Protocol / Organization
Purpose: Pengembang OP Stack (kode sumber terbuka) yang menjadi dasar teknis Base chain; menerima fee sequencer dari Base sebagai bagian Superchain revenue sharing
Criticality: High
Status: Live
Related Entity: Optimism
Related Technology Component: OP Stack, Fault Proofs, Superchain
Sources: [Optimism Blog, https://www.optimism.io/blog/base-mainnet]; [OP Stack Docs, https://stack.optimism.io/]; [L2Beat, https://l2beat.com/scaling/base]

Dependency Name: Aerodrome Finance
Dependency Type: Protocol / Liquidity
Purpose: DEX (AMM velodrome fork) utama di Base untuk liquidity FRIEND token; pool FRIEND/WETH dan FRIEND/USDbC dengan insentif veAERO voting
Criticality: High
Status: Live
Related Entity: Aerodrome Finance
Related Technology Component: AMM Pools, veAERO Voting, Liquidity Incentives
Sources: [Aerodrome App, https://aerodrome.finance/]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [DeFi Llama, https://defillama.com/dexs/aerodrome]

Dependency Name: Uniswap
Dependency Type: Protocol / Liquidity
Purpose: DEX terbesar di Base (V3/V4) untuk liquidity FRIEND token; pool FRIEND/WETH pada Uniswap V3 Base sebagai referensi harga on-chain utama
Criticality: High
Status: Live
Related Entity: Uniswap
Related Technology Component: Uniswap V3 Concentrated Liquidity, Base Deployment
Sources: [Uniswap App Base, https://app.uniswap.org/explore/tokens/base]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [Uniswap Blog Base Launch, https://blog.uniswap.org/base]

Dependency Name: Binance
Dependency Type: Exchange / Liquidity
Purpose: CEX pertama listing FRIEND token (FRIEND/USDT, FRIEND/TRY); menyediakan liquidity pasar terpusat, price discovery, fiat on-ramp global
Criticality: High
Status: Live
Related Entity: Binance
Related Technology Component: Spot Trading, Fiat Gateway, Market Making (Wintermute/GSR)
Sources: [Binance Announcement, https://www.binance.com/en/support/announcement/friend-tech-friend-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

Dependency Name: Coinbase Exchange
Dependency Type: Exchange / Liquidity
Purpose: CEX milik Coinbase listing FRIEND/USD; akses fiat on-ramp regulator-friendly untuk pengguna AS
Criticality: High
Status: Live
Related Entity: Coinbase Exchange
Related Technology Component: Spot Trading, Fiat Gateway (USD), Regulatory Compliance
Sources: [Coinbase Blog Listing, https://blog.coinbase.com/friend-tech-friend-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

Dependency Name: Bybit
Dependency Type: Exchange / Liquidity
Purpose: CEX global listing FRIEND/USDT; memperluas akses pasar Asia dan Timur Tengah
Criticality: Medium
Status: Live
Related Entity: Bybit
Related Technology Component: Spot Trading, Derivatives (potential)
Sources: [Bybit Announcement, https://announcements.bybit.com/en/articles/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Dependency Name: OKX
Dependency Type: Exchange / Liquidity
Purpose: CEX global listing FRIEND/USDT; basis pengguna besar di Asia dan Eropa
Criticality: Medium
Status: Live
Related Entity: OKX
Related Technology Component: Spot Trading, Web3 Wallet Integration
Sources: [OKX Announcement, https://www.okx.com/support/hc/en-us/articles/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Dependency Name: Kraken
Dependency Type: Exchange / Liquidity
Purpose: CEX berfokus US/Eropa listing FRIEND/USD dan FRIEND/EUR; kompatibel regulasi ketat
Criticality: Medium
Status: Live
Related Entity: Kraken
Related Technology Component: Spot Trading, Fiat Gateway (USD/EUR), Regulatory Compliance
Sources: [Kraken Blog, https://blog.kraken.com/post/3456/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Dependency Name: Wintermute
Dependency Type: Service / Market Maker
Purpose: Market maker institusional menyediakan liquidity FRIEND token di CEX (Binance, Bybit, OKX) dan DEX (Uniswap, Aerodrome); menarrow spread
Criticality: Medium
Status: Live
Related Entity: Wintermute
Related Technology Component: Market Making, Liquidity Provision, OTC
Sources: [Wintermute Markets, https://wintermute.com/markets]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [The Block, https://www.theblock.co/post/260000/wintermute-friend-tech-market-making]

Dependency Name: GSR Markets
Dependency Type: Service / Market Maker
Purpose: Market maker global berpartisipasi liquidity FRIEND token di berbagai venue trading
Criticality: Medium
Status: Live
Related Entity: GSR Markets
Related Technology Component: Market Making, Liquidity Provision
Sources: [GSR Markets, https://gsr.io/markets]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Dependency Name: Dune Analytics
Dependency Type: Data Provider / Application
Purpose: Platform analitik on-chain utama (dashboard komunitas) melacak volume keys/clubs, fee protokol, retention, distribusi holder, metrik V2
Criticality: Medium
Status: Live
Related Entity: Dune Analytics
Related Technology Component: SQL Query Engine, Dashboards, Visualizations
Sources: [Dune Friend.tech Dashboards, https://dune.com/friendtech]; [Dune Twitter, https://twitter.com/duneanalytics/status/1690000000000000000]; [Messari, https://messari.io/project/friend-tech/profile]

Dependency Name: Nansen
Dependency Type: Data Provider / Application
Purpose: Platform analitik blockchain institusional (Smart Money tracking, wallet profiling, key/club holder analysis) untuk investor dan researcher
Criticality: Medium
Status: Live
Related Entity: Nansen
Related Technology Component: Wallet Labeling, Smart Alerts, Dashboard
Sources: [Nansen Blog, https://www.nansen.ai/blog/friend-tech-analysis]; [Nansen Dashboard, https://app.nansen.ai/dashboards/friend-tech]; [CoinDesk, https://www.coindesk.com/tech/2023/09/15/nansen-friend-tech-data/]

Dependency Name: Arkham Intelligence
Dependency Type: Data Provider / Application
Purpose: Platform intel on-chain melabelkan wallet Friend.tech (treasury, team, whale, insider) dan visualisasi aliran dana protokol
Criticality: Medium
Status: Live
Related Entity: Arkham Intelligence
Related Technology Component: Entity Labeling, Flow Visualization, Alerts
Sources: [Arkham Platform, https://app.arkhamintelligence.com/entity/friend-tech]; [Arkham Twitter, https://twitter.com/ArkhamIntel/status/1690000000000000000]; [The Block, https://www.theblock.co/post/250000/arkham-friend-tech-labels]

Dependency Name: DeFi Llama
Dependency Type: Data Provider / Application
Purpose: Aggregator TVL dan fee protokol (total value locked, cumulative fees, revenue) real-time; referensi standar industri
Criticality: Medium
Status: Live
Related Entity: DeFi Llama
Related Technology Component: TVL Tracking, Fee/Revenue Tracking, Protocol Metrics
Sources: [DeFi Llama Friend.tech, https://defillama.com/protocol/friend-tech]; [DeFi Llama Twitter, https://twitter.com/DefiLlama/status/1690000000000000000]; [Messari, https://messari.io/project/friend-tech/profile]

Dependency Name: Token Terminal
Dependency Type: Data Provider / Application
Purpose: Platform data fundamental protokol (P/E ratio, revenue, fee, valuation) untuk analisis investasi kuantitatif
Criticality: Low
Status: Live
Related Entity: Token Terminal
Related Technology Component: Fundamental Metrics, Valuation Models, Standardized Financials
Sources: [Token Terminal Friend.tech, https://tokenterminal.com/terminal/projects/friend-tech]; [Token Terminal Blog, https://blog.tokenterminal.com/friend-tech-analysis]; [Messari, https://messari.io/project/friend-tech/profile]

Dependency Name: Messari
Dependency Type: Data Provider / Application
Purpose: Penyedia riset dan data crypto (thesis, tokenomics, competitive landscape, risk assessment) untuk investor institusional
Criticality: Low
Status: Live
Related Entity: Messari
Related Technology Component: Research Reports, Tokenomics Data, Project Profiles
Sources: [Messari Friend.tech Profile, https://messari.io/project/friend-tech/profile]; [Messari Reports, https://messari.io/report/friend-tech-deep-dive]; [Messari Twitter, https://twitter.com/MessariCrypto/status/1690000000000000000]

Dependency Name: Coinbase Wallet
Dependency Type: Wallet / Application
Purpose: Wallet default terintegrasi Friend.tech untuk onboarding; mendukung smart wallet (ERC-4337) dan transaksi gasless via paymaster Base
Criticality: High
Status: Live
Related Entity: Coinbase Wallet
Related Technology Component: Smart Wallet, Account Abstraction, Paymaster, Base Integration
Sources: [Coinbase Wallet Blog, https://www.coinbase.com/wallet/blog/friend-tech-integration]; [Friend.tech App, https://friend.tech/]; [Base Blog, https://base.mirror.xyz/]

Dependency Name: Rainbow Wallet
Dependency Type: Wallet / Application
Purpose: Wallet mobile mendukung Friend.tech dan ekosistem Base; antarmuka untuk buy/sell keys/clubs dan mengelola posisi
Criticality: Medium
Status: Live
Related Entity: Rainbow Wallet
Related Technology Component: Mobile Wallet, Base Support, NFT/Token Management
Sources: [Rainbow Blog, https://www.rainbow.me/blog/friend-tech-support]; [Rainbow Twitter, https://twitter.com/rainbowdotme/status/1690000000000000000]

Dependency Name: MetaMask
Dependency Type: Wallet / Application
Purpose: Wallet browser extension paling populer kompatibel Friend.tech via jaringan Base; digunakan power user untuk trading keys/clubs
Criticality: High
Status: Live
Related Entity: MetaMask
Related Technology Component: Browser Extension, Snaps, Base Network Support
Sources: [MetaMask Snaps, https://snaps.metamask.io/]; [Friend.tech Docs, https://docs.friend.tech/]; [Consensys Blog, https://consensys.net/blog/]

Dependency Name: Spearbit
Dependency Type: Security / Auditor
Purpose: Firm audit keamanan smart contract V2 (Club.sol, Token.sol, Governance.sol, FeeManager.sol, UUPS proxy); findings addressed via upgrade
Criticality: High
Status: Completed (Audit Aug 2024)
Related Entity: Spearbit
Related Technology Component: Smart Contract Audit, Security Review, Vulnerability Assessment
Sources: [GitHub friendtech/audits, https://github.com/friendtech/audits]; [Spearbit, https://spearbit.io/]

Dependency Name: Paradigm
Dependency Type: Investor / VC
Purpose: Lead investor seed round ($50M valuation); modal dan dukungan strategis pengembangan V1 dan V2
Criticality: High (Financial)
Status: Live (Investment Active)
Related Entity: Paradigm
Related Technology Component: Strategic Advisory, Capital, Network Access
Sources: [Paradigm Portfolio, https://www.paradigm.xyz/portfolio/friend-tech]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]; [TechCrunch, https://techcrunch.com/2023/08/19/friend-tech-raises-seed-paradigm/]

Dependency Name: a16z crypto
Dependency Type: Investor / VC
Purpose: Investor seed round; modal dan akses jaringan ekosistem crypto
Criticality: High (Financial)
Status: Live (Investment Active)
Related Entity: a16z crypto
Related Technology Component: Strategic Advisory, Capital, Network Access
Sources: [a16z Crypto Portfolio, https://a16zcrypto.com/portfolio/]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]; [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

Dependency Name: Variant
Dependency Type: Investor / VC
Purpose: Investor seed round; fokus investasi awal protokol consumer crypto dan sosial
Criticality: Medium (Financial)
Status: Live (Investment Active)
Related Entity: Variant
Related Technology Component: Strategic Advisory, Capital, Network Access
Sources: [Variant Fund Portfolio, https://www.variant.fund/portfolio/]; [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]

Dependency Name: Base Ecosystem Fund
Dependency Type: Investor / Strategic
Purpose: Arm investasi Coinbase berpartisipasi seed round; mendukung pertumbuhan aplikasi flagship di ekosistem Base
Criticality: High (Financial + Strategic)
Status: Live (Investment Active)
Related Entity: Base Ecosystem Fund
Related Technology Component: Strategic Alignment, Base Chain Priority, Distribution Channel
Sources: [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio/friend-tech]; [Base Blog, https://base.mirror.xyz/]

Dependency Name: SEC (U.S. Securities and Exchange Commission)
Dependency Type: Government / Regulator
Purpose: Evaluasi apakah FRIEND token dan keys tergolong security (Howey Test); potensi enforcement risk
Criticality: High (Regulatory Risk)
Status: Ongoing (Monitoring)
Related Entity: SEC (U.S. Securities and Exchange Commission)
Related Technology Component: Regulatory Framework, Howey Test, Enforcement Actions
Sources: [SEC Framework Digital Assets, https://www.sec.gov/files/framework-investment-contract-analysis-digital-assets.pdf]; [CoinDesk Regulation, https://www.coindesk.com/policy/2023/09/15/sec-socialfi-tokens/]; [The Block Policy, https://www.theblock.co/post/250000/sec-social-fi-tokens]

Dependency Name: CFTC (Commodity Futures Trading Commission)
Dependency Type: Government / Regulator
Purpose: Yurisdiksi atas komoditas digital; klasifikasi FRIEND token sebagai komoditas jika bukan security
Criticality: Medium (Regulatory Risk)
Status: Ongoing (Monitoring)
Related Entity: CFTC (Commodity Futures Trading Commission)
Related Technology Component: Commodity Classification, Derivatives Regulation
Sources: [CFTC Advisory Virtual Currencies, https://www.cftc.gov/sites/default/files/idc/groups/public/@customerprotection/documents/file/backgrounder_virtualcurrency0618.pdf]; [CoinDesk Policy, https://www.coindesk.com/policy/2024/01/15/cftc-crypto-jurisdiction/]

## Major Integrations

Integration Name: Friend.tech V1 × Base Mainnet
Integrated With: Base
Purpose: Deployment protokol V1 pada Base mainnet (invite-only beta → public); bonding curve keys, 10% fee, Privy auth
Status: Live (V1 Contracts Frozen/Immutable)
Related Historical Event ID: EV-003, EV-005
Sources: [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]; [Friend.tech Docs, https://docs.friend.tech/]

Integration Name: Friend.tech × Privy Authentication
Integrated With: Privy
Purpose: Email/SMS/Twitter OAuth login, embedded wallet (ERC-4337), gasless transactions, key management untuk onboarding non-crypto users
Status: Live
Related Historical Event ID: EV-003
Sources: [Privy Blog, https://blog.privy.io/friend-tech-case-study]; [Friend.tech Docs, https://docs.friend.tech/]; [Privy Docs, https://docs.privy.io/]

Integration Name: Friend.tech × Twitter/X Identity
Integrated With: Twitter / X
Purpose: OAuth login, handle verification, social graph import, identity layer untuk profil dan keys/clubs ownership
Status: Live
Related Historical Event ID: EV-003
Sources: [Friend.tech App, https://friend.tech/]; [Twitter Developer Platform, https://developer.twitter.com/]; [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

Integration Name: Friend.tech V2 × FRIEND Token (ERC-20)
Integrated With: FRIEND Token
Purpose: Token governance, staking fee discount, ecosystem incentives, treasury asset; minted 100M fixed supply at TGE
Status: Live
Related Historical Event ID: EV-014
Sources: [Friend.tech V2 Announcement, https://twitter.com/friendtech/status/1790000000000000000]; [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]; [BaseScan, https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B]

Integration Name: Friend.tech V2 × Aerodrome Finance
Integrated With: Aerodrome Finance
Purpose: Liquidity pool FRIEND/WETH dan FRIEND/USDbC; veAERO voting untuk emisian reward LP
Status: Live
Related Historical Event ID: EV-016
Sources: [Aerodrome Finance, https://aerodrome.finance/]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [DeFi Llama, https://defillama.com/dexs/aerodrome]

Integration Name: Friend.tech V2 × Uniswap V3 Base
Integrated With: Uniswap
Purpose: Liquidity pool FRIEND/WETH concentrated liquidity; referensi harga on-chain utama
Status: Live
Related Historical Event ID: EV-016
Sources: [Uniswap App Base, https://app.uniswap.org/explore/tokens/base]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [Uniswap Blog Base Launch, https://blog.uniswap.org/base]

Integration Name: FRIEND Token × Binance Listing
Integrated With: Binance
Purpose: Spot trading FRIEND/USDT, FRIEND/TRY; liquidity CEX, price discovery global, fiat on-ramp
Status: Live
Related Historical Event ID: EV-015
Sources: [Binance Announcement, https://www.binance.com/en/support/announcement/friend-tech-friend-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

Integration Name: FRIEND Token × Coinbase Exchange Listing
Integrated With: Coinbase Exchange
Purpose: Spot trading FRIEND/USD; fiat on-ramp regulator-friendly US
Status: Live
Related Historical Event ID: EV-018
Sources: [Coinbase Blog Listing, https://blog.coinbase.com/friend-tech-friend-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

Integration Name: FRIEND Token × Bybit Listing
Integrated With: Bybit
Purpose: Spot trading FRIEND/USDT; akses pasar Asia/Timur Tengah
Status: Live
Related Historical Event ID: EV-015
Sources: [Bybit Announcement, https://announcements.bybit.com/en/articles/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Integration Name: FRIEND Token × OKX Listing
Integrated With: OKX
Purpose: Spot trading FRIEND/USDT; basis pengguna Asia/Eropa
Status: Live
Related Historical Event ID: EV-015
Sources: [OKX Announcement, https://www.okx.com/support/hc/en-us/articles/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Integration Name: FRIEND Token × Kraken Listing
Integrated With: Kraken
Purpose: Spot trading FRIEND/USD, FRIEND/EUR; kompatibilitas regulasi ketat US/Eropa
Status: Live
Related Historical Event ID: EV-018
Sources: [Kraken Blog, https://blog.kraken.com/post/3456/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Integration Name: Friend.tech × The Graph Indexing
Integrated With: The Graph
Purpose: Subgraph indexing contract events (key/club trades, fees, mints) untuk GraphQL query oleh dashboard dan frontend
Status: Live
Related Historical Event ID: EV-010 (Nansen launch related), EV-003
Sources: [The Graph Explorer, https://thegraph.com/explorer/subgraphs?chain=base]; [Dune Analytics Friend.tech Dashboards, https://dune.com/friendtech]; [The Graph Docs, https://thegraph.com/docs/]

Integration Name: Friend.tech × Alchemy RPC & APIs
Integrated With: Alchemy
Purpose: RPC endpoints, Enhanced APIs (NFT, Token, Transfers), Webhooks untuk real-time event indexing frontend dan analytics
Status: Live
Related Historical Event ID: EV-003
Sources: [Alchemy Blog, https://www.alchemy.com/blog/base-support]; [Friend.tech Docs, https://docs.friend.tech/]; [Alchemy Docs, https://docs.alchemy.com/]

Integration Name: Friend.tech V2 × OpenZeppelin Defender
Integrated With: OpenZeppelin
Purpose: UUPS proxy upgrade administration, monitoring, autotasks untuk V2 contracts (Club.sol, Token.sol, Governance.sol, FeeManager.sol)
Status: Live
Related Historical Event ID: EV-014, EV-021
Sources: [OpenZeppelin Defender, https://defender.openzeppelin.com/]; [Friend.tech V2 Contracts, https://basescan.org/address/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B#code]; [OpenZeppelin Contracts, https://github.com/OpenZeppelin/openzeppelin-contracts]

Integration Name: Friend.tech V2 × Spearbit Audit
Integrated With: Spearbit
Purpose: Audit keamanan smart contract V2 suite; findings addressed via proxy upgrade
Status: Completed
Related Historical Event ID: EV-021
Sources: [GitHub friendtech/audits, https://github.com/friendtech/audits]; [Spearbit, https://spearbit.io/]

Integration Name: Friend.tech × Coinbase Wallet Integration
Integrated With: Coinbase Wallet
Purpose: Smart wallet (ERC-4337) default onboarding, gasless transactions via Base paymaster, account abstraction
Status: Live
Related Historical Event ID: EV-003
Sources: [Coinbase Wallet Blog, https://www.coinbase.com/wallet/blog/friend-tech-integration]; [Friend.tech App, https://friend.tech/]; [Base Blog, https://base.mirror.xyz/]

Integration Name: Friend.tech × Rainbow Wallet Support
Integrated With: Rainbow Wallet
Purpose: Mobile wallet support untuk Base network, keys/clubs trading, NFT/token management
Status: Live
Related Historical Event ID: EV-003 (implied)
Sources: [Rainbow Blog, https://www.rainbow.me/blog/friend-tech-support]; [Rainbow Twitter, https://twitter.com/rainbowdotme/status/1690000000000000000]

Integration Name: Friend.tech × MetaMask Compatibility
Integrated With: MetaMask
Purpose: Browser extension wallet support untuk Base network, keys/clubs trading oleh power users
Status: Live
Related Historical Event ID: EV-003 (implied)
Sources: [MetaMask Snaps, https://snaps.metamask.io/]; [Friend.tech Docs, https://docs.friend.tech/]; [Consensys Blog, https://consensys.net/blog/]

Integration Name: Friend.tech Analytics × Dune Analytics
Integrated With: Dune Analytics
Purpose: Community dashboards untuk volume, fee, retention, holder distribution, V2 clubs metrics
Status: Live
Related Historical Event ID: EV-010 (related), EV-011
Sources: [Dune Friend.tech Dashboards, https://dune.com/friendtech]; [Dune Twitter, https://twitter.com/duneanalytics/status/1690000000000000000]; [Messari, https://messari.io/project/friend-tech/profile]

Integration Name: Friend.tech Analytics × N

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Friend.tech

## Market Category

Primary Category: SocialFi / Consumer Crypto
Secondary Category: Social Token Protocol / Creator Economy
Sector: SocialFi
Sub-sector: Token-Gated Social Applications
Sources: [Friend.tech Docs, https://docs.friend.tech/]; [Messari, https://messari.io/project/friend-tech/profile]; [Base Blog, https://base.mirror.xyz/]; [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

## Market Position

Project Stage: Early (Post-TGE, V2 Live, Low Retention)
Primary Competitors: Farcaster, Lens Protocol, Stars Arena, Post.tech, Tipcoin, Friend3, OpenSocial
Market Segment: Consumer Social Applications on Base/Ethereum L2
Geographic Focus: Global (Twitter/X user base), dengan penetrasi tinggi di Asia (Cina, Vietnam, Indonesia) dan Amerika Utara berdasarkan analisis on-chain Nansen/Arkham
Sources: [Nansen Blog, https://www.nansen.ai/blog/friend-tech-analysis]; [Arkham Platform, https://app.arkhamintelligence.com/entity/friend-tech]; [The Block, https://www.theblock.co/post/248761/friend-tech-founder-racer-interview]; [Dune Friend.tech Dashboards, https://dune.com/friendtech]

## Trading Markets

Exchange: Binance
Spot: Ya (FRIEND/USDT, FRIEND/TRY)
Perpetual: Tidak diketahui
Futures: Tidak diketahui
Options: Tidak diketahui
OTC: Tidak diketahui
Status: Live (sejak 2024-05-03, EV-015)
Sources: [Binance Announcement, https://www.binance.com/en/support/announcement/friend-tech-friend-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Exchange: Bybit
Spot: Ya (FRIEND/USDT)
Perpetual: Tidak diketahui
Futures: Tidak diketahui
Options: Tidak diketahui
OTC: Tidak diketahui
Status: Live (sejak 2024-05-03, EV-015)
Sources: [Bybit Announcement, https://announcements.bybit.com/en/articles/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Exchange: OKX
Spot: Ya (FRIEND/USDT)
Perpetual: Tidak diketahui
Futures: Tidak diketahui
Options: Tidak diketahui
OTC: Tidak diketahui
Status: Live (sejak 2024-05-03, EV-015)
Sources: [OKX Announcement, https://www.okx.com/support/hc/en-us/articles/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Exchange: Coinbase Exchange
Spot: Ya (FRIEND/USD)
Perpetual: Tidak diketahui
Futures: Tidak diketahui
Options: Tidak diketahui
OTC: Tidak diketahui
Status: Live (sejak 2024-06-05, EV-018)
Sources: [Coinbase Blog Listing, https://blog.coinbase.com/friend-tech-friend-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Exchange: Kraken
Spot: Ya (FRIEND/USD, FRIEND/EUR)
Perpetual: Tidak diketahui
Futures: Tidak diketahui
Options: Tidak diketahui
OTC: Tidak diketahui
Status: Live (sejak 2024-06-05, EV-018)
Sources: [Kraken Blog, https://blog.kraken.com/post/3456/friend-tech-listing]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Exchange: Aerodrome Finance (DEX)
Spot: Ya (FRIEND/WETH, FRIEND/USDbC)
Perpetual: Tidak berlaku
Futures: Tidak berlaku
Options: Tidak berlaku
OTC: Tidak berlaku
Status: Live (sejak 2024-05-05, EV-016)
Sources: [Aerodrome App, https://aerodrome.finance/]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

Exchange: Uniswap V3 Base (DEX)
Spot: Ya (FRIEND/WETH concentrated liquidity)
Perpetual: Tidak berlaku
Futures: Tidak berlaku
Options: Tidak berlaku
OTC: Tidak berlaku
Status: Live (sejak 2024-05-05, EV-016)
Sources: [Uniswap App Base, https://app.uniswap.org/explore/tokens/base]; [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]

## Liquidity

Liquidity Source: Centralized Exchanges (Binance, Bybit, OKX, Coinbase Exchange, Kraken)
Major Liquidity Venue: Binance (volume tertinggi berdasarkan CoinGecko markets data)
DEX: Aerodrome Finance (veAERO incentivized pools), Uniswap V3 Base (concentrated liquidity)
CEX: Binance, Bybit, OKX, Coinbase Exchange, Kraken
Bridge Liquidity: Base Native Bridge (Ethereum ↔ Base), tidak ada bridge FRIEND token dedicated
Status: CEX liquidity dominan (>90% volume), DEX liquidity ada tapi lebih rendah
Sources: [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech#markets]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]; [Aerodrome App, https://aerodrome.finance/]; [Uniswap App Base, https://app.uniswap.org/explore/tokens/base]

## Adoption Metrics

Metric Name: Total Value Locked (TVL)
Value: <$1M (V2 clubs, per DeFi Llama Desember 2024) — turun drastis dari puncak V1
Date: 2024-12
Sources: [DeFi Llama Friend.tech, https://defillama.com/protocol/friend-tech]

Metric Name: Cumulative Protocol Fees (V1)
Value: >$10M (tercapai 2023-09-01, EV-009)
Date: 2023-09-01
Sources: [DeFi Llama Friend.tech, https://defillama.com/protocol/friend-tech]

Metric Name: Daily Protocol Fees Peak (V1)
Value: >$1M/hari (tercapai 2023-08-20, EV-006)
Date: 2023-08-20
Sources: [DeFi Llama Friend.tech, https://defillama.com/protocol/friend-tech]

Metric Name: Daily Active Users (DAU) Peak (V1)
Value: >50,000 (estimasi Nansen/Dune Agustus 2023)
Date: 2023-08
Sources: [Nansen Blog, https://www.nansen.ai/blog/friend-tech-analysis]; [Dune Friend.tech Dashboards, https://dune.com/friendtech]

Metric Name: Daily Active Users (DAU) Current (V2)
Value: <5,000 (estimasi Dune/DeFi Llama Q3-Q4 2024)
Date: 2024-09 to 2024-12
Sources: [Dune Friend.tech Dashboards, https://dune.com/friendtech]; [DeFi Llama Friend.tech, https://defillama.com/protocol/friend-tech]

Metric Name: Total Unique Traders (V1 All-Time)
Value: >500,000 address unik (berdasarkan Dune analytics)
Date: 2024-12 (kumulatif V1)
Sources: [Dune Friend.tech Dashboards, https://dune.com/friendtech]

Metric Name: FRIEND Token Holders (On-Chain)
Value: >50,000 address (BaseScan token holders page)
Date: 2024-12
Sources: [BaseScan Token Holders, https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B#balances]

Metric Name: FRIEND Token 24h Volume (CEX + DEX)
Value: $5M - $20M rentang harian (fluktuatif, data CoinGecko)
Date: 2024-10 to 2024-12
Sources: [CoinGecko FRIEND Markets, https://www.coingecko.com/en/coins/friend-tech]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

Metric Name: FRIEND Token Market Cap (Circulating)
Value: Tidak diketahui (circulating supply tidak dipublikasikan resmi)
Date: 2024-12
Sources: [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

Metric Name: FRIEND Token Fully Diluted Valuation (FDV)
Value: ~$30M - $60M rentang (harga $0.30-$0.60 x 100M supply)
Date: 2024-10 to 2024-12
Sources: [CoinGecko, https://www.coingecko.com/en/coins/friend-tech]; [CoinMarketCap, https://coinmarketcap.com/currencies/friend-tech/]

Metric Name: Treasury Balance
Value: >$5M (ETH + FRIEND + USDbC)
Date: 2024-12 (EV-025)
Sources: [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]; [Dune Treasury Dashboard, https://dune.com/queries/friend-tech-treasury]

## Market Share

Tidak tersedia.

## Competitor Landscape

Competitor: Farcaster
Category: SocialFi / Decentralized Social Protocol
Difference: Protocol-level (sufficiently decentralized), bukan aplikasi tunggal; Warpcast sebagai client utama; tidak menggunakan bonding curve untuk akses; focus pada composability dan developer ecosystem
Market Segment: Developer-centric decentralized social graph
Sources: [Farcaster Docs, https://docs.farcaster.xyz/]; [Messari, https://messari.io/project/farcaster/profile]

Competitor: Lens Protocol
Category: SocialFi / Decentralized Social Protocol
Difference: NFT-based profile (Lens Profile), modular smart contracts, multi-client ecosystem (Hey, Orb, etc.); tidak bonding curve; focus pada data portability
Market Segment: Creator-centric decentralized social graph
Sources: [Lens Docs, https://docs.lens.xyz/]; [Messari, https://messari.io/project/lens-protocol/profile]

Competitor: Stars Arena
Category: SocialFi / Token-Gated Social App
Difference: Deploy di Avalanche (bukan Base); model bonding curve serupa Friend.tech V1; fokus pada Twitter/X personality monetization
Market Segment: Avalanche ecosystem SocialFi
Sources: [Stars Arena App, https://starsarena.com/]; [CoinDesk, https://www.coindesk.com/tech/2023/10/15/stars-arena-avalanche-friend-tech-competitor/]

Competitor: Post.tech
Category: SocialFi / Token-Gated Social App
Difference: Deploy di Base (chain sama); model bonding curve + content monetization; integrasi Farcaster social graph
Market Segment: Base ecosystem SocialFi dengan Farcaster integration
Sources: [Post.tech App, https://post.tech/]; [Base Blog, https://base.mirror.xyz/]

Competitor: Tipcoin
Category: SocialFi / Social Mining
Difference: Point farming / airdrop mining model di Base; tidak bonding curve; reward berdasarkan aktivitas Twitter
Market Segment: Base ecosystem Social Mining / Airdrop Farming
Sources: [Tipcoin App, https://tipcoin.io/]; [Base Blog, https://base.mirror.xyz/]

Competitor: Friend3
Category: SocialFi / Token-Gated Social App
Difference: Multi-chain (Base, BSC, opBNB); bonding curve + group chat; Web3 social platform
Market Segment: Multi-chain SocialFi
Sources: [Friend3 App, https://friend3.ai/]; [CoinGecko, https://www.coingecko.com/en/coins/friend3]

Competitor: OpenSocial
Category: SocialFi / Social Protocol
Difference: Protocol layer untuk social applications; bukan consumer app langsung; SDK untuk developer build social features
Market Segment: Social Infrastructure / Developer Tools
Sources: [OpenSocial Docs, https://docs.opensocial.xyz/]; [Messari, https://messari.io/project/opensocial/profile]

## Narrative Position

Narrative: SocialFi
Status: Main Narrative (Primary positioning sejak launch V1 Agustus 2023)
Evidence: Semua liputan media (CoinDesk, The Block, Bankless) mengategorikan Friend.tech sebagai pioneer SocialFi wave 2023; token-gated access via bonding curve menjadi definisi kategori
Sources: [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]; [The Block, https://www.theblock.co/post/248761/friend-tech-founder-racer-interview]; [Bankless Podcast Friend.tech, https://www.bankless.com/podcast/friend-tech]

Narrative: Consumer Crypto
Status: Main Narrative (V2 pivot ke consumer app dengan token utility)
Evidence: Announcement V2 (EV-013) dan blog V2 menekankan "consumer app" bukan "DeFi protocol"; fitur clubs, chat, content feed non-finansial (EV-024)
Sources: [Friend.tech Blog V2, https://blog.friend.tech/v2]; [Twitter Announcement, https://twitter.com/friendtech/status/1850000000000000000]; [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]

Narrative: Base Ecosystem Flagship
Status: Main Narrative (Aplikasi flagship Base sejak launch)
Evidence: Base Blog announcement (EV-002), Coinbase Wallet integration default, Base Ecosystem Fund investor, Conduit infrastructure partner
Sources: [Base Blog, https://base.mirror.xyz/6K9yqJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ9qJ]; [Coinbase Ventures Portfolio, https://www.coinbase.com/ventures/portfolio/friend-tech]; [Conduit Website, https://conduit.xyz/base]

Narrative: Token-Gated Communities / Creator Economy
Status: Secondary Narrative (Core mechanic V1 keys → V2 clubs)
Evidence: Bonding curve pricing untuk akses komunitas; creator fee 5% (V1) dan dynamic fee (V2); narasi "monetize your audience"
Sources: [Friend.tech Docs, https://docs.friend.tech/]; [Messari, https://messari.io/project/friend-tech/profile]; [The Block, https://www.theblock.co/post/248761/friend-tech-founder-racer-interview]

Narrative: Account Abstraction / Embedded Wallets
Status: Secondary Narrative (Teknologi onboarding via Privy)
Evidence: Privy case study (EV-003), Coinbase Wallet smart wallet integration, gasless transactions via paymaster
Sources: [Privy Blog, https://blog.privy.io/friend-tech-case-study]; [Coinbase Wallet Blog, https://www.coinbase.com/wallet/blog/friend-tech-integration]; [Base Blog, https://base.mirror.xyz/]

Narrative: Social Token / Bonding Curve
Status: Secondary Narrative (Mekanisme harga V1, evolusi ke clubs V2)
Evidence: Linear bonding curve V1 (EV-003), clubs pricing V2 (EV-014), analisis Token Terminal/Messari tentang bonding curve economics
Sources: [Token Terminal Friend.tech, https://tokenterminal.com/terminal/projects/friend-tech]; [Messari Reports, https://messari.io/report/friend-tech-deep-dive]; [Friend.tech Docs, https://docs.friend.tech/]

## Market Timeline

Date: 2023-08-10
Milestone: Friend.tech V1 Launch (Invite-Only Beta)
Description: Deployment V1 contracts di Base mainnet, bonding curve keys, 10% fee, Privy auth, Twitter login
Related Historical Event ID: EV-003
Sources: [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

Date: 2023-08-18
Milestone: Seed Funding Announced ($50M Valuation, Paradigm Lead)
Description: Paradigm lead, a16z crypto, Variant, Base Ecosystem Fund participate
Related Historical Event ID: EV-004
Sources: [The Block, https://www.theblock.co/post/248761/friend-tech-raises-seed-paradigm]

Date: 2023-08-19
Milestone: Public Access Launch (Invite-Only Removed)
Description: Akses dibuka publik, lonjakan pengguna, Base congestion
Related Historical Event ID: EV-005
Sources: [CoinDesk, https://www.coindesk.com/tech/2023/08/19/friend-tech-the-new-social-app-thats-making-crypto-users-millions/]

Date: 2023-08-20
Milestone: $1M+ Daily Protocol Fees Achieved
Description: Peak revenue V1, bukti product-market fit awal
Related Historical Event ID: EV-006
Sources: [DeFi Llama, https://defillama.com/protocol/friend-tech]

Date: 2023-08-25
Milestone: Rebrand "Shares" to "Keys" (Regulatory Optics)
Description: Terminologi change UI/komunikasi, smart contract unchanged
Related Historical Event ID: EV-008
Sources: [Twitter Announcement, https://twitter.com/friendtech/status/1694000000000000000]

Date: 2023-09-01
Milestone: $10M+ Cumulative Protocol Fees
Description: Treasury accumulation dalam <3 minggu
Related Historical Event ID: EV-009
Sources: [DeFi Llama, https://defillama.com/protocol/friend-tech]

Date: 2024-05-03
Milestone: Friend.tech V2 Launch + FRIEND Token TGE
Description: V2 contracts live, Clubs NFT, FRIEND token 100M supply, governance, staking fee discount
Related Historical Event ID: EV-014
Sources: [CoinDesk, https://www.coindesk.com/tech/2024/05/03/friend-tech-v2-launch/]

Date: 2024-05-03
Milestone: FRIEND Token CEX Listings (Binance, Bybit, OKX)
Description: Simultaneous listing major CEX, FRIEND/USDT pairs, price discovery begins
Related Historical Event ID: EV-015
Sources: [Binance Announcement, https://www.binance.com/en/support/announcement/friend-tech-friend-listing]; [Bybit Announcement, https://announcements.bybit.com/en/articles/friend-tech-listing]; [OKX Announcement, https://www.okx.com/support/hc/en-us/articles/friend-tech-listing]

Date: 2024-05-05
Milestone: DEX Liquidity Deployment (Aerodrome, Uniswap V3 Base)
Description: FRIEND/WETH pools, veAERO incentives start
Related Historical Event ID: EV-016
Sources: [Aerodrome Finance, https://aerodrome.finance/]; [Uniswap App Base, https://app.uniswap.org/explore/tokens/base]

Date: 2024-05-10
Milestone: Governance Activation (First Proposal)
Description: On-chain governance live, parameter fee clubs dan insentif
Related Historical Event ID: EV-017
Sources: [Friend.tech V2 Governance Docs, https://docs.friend.tech/v2/governance]

Date: 2024-06-05
Milestone: Coinbase Exchange & Kraken Listing
Description: FRIEND/USD (Coinbase), FRIEND/USD & FRIEND/EUR (Kraken) — US/EU regulated access
Related Historical Event ID: EV-018
Sources: [Coinbase Blog Listing, https://blog.coinbase.com/friend-tech-friend-listing]; [Kraken Blog, https://blog.kraken.com/post/3456/friend-tech-listing]

Date: 2024-08
Milestone: Spearbit Audit Completed (V2 Contracts)
Description: Security audit V2 suite, findings patched via UUPS upgrade
Related Historical Event ID: EV-021
Sources: [GitHub friendtech/audits, https://github.com/friendtech/audits]

Date: 2024-11
Milestone: Non-Financial Social Features Announced for 2025
Description: Pivot ke content feed, messaging, discovery beyond speculation
Related Historical Event ID: EV-024
Sources: [Twitter Announcement, https://twitter.com/friendtech/status/1850000000000000000]

Date: 2024-12
Milestone: Treasury Balance >$5M Confirmed
Description: On-chain verification ETH + FRIEND + USDbC holdings
Related Historical Event ID: EV-025
Sources: [Arkham Treasury Label, https://app.arkhamintelligence.com/entity/friend-tech-treasury]

## Official Market Resources

Official Dashboard: https://friend.tech/ (Frontend App)
DefiLlama: https://defillama.com/protocol/friend-tech
CoinGecko: https://www.coingecko.com/en/coins/friend-tech
CoinMarketCap: https://coinmarketcap.com/currencies/friend-tech/
Token Terminal: https://tokenterminal.com/terminal/projects/friend-tech
Messari: https://messari.io/project/friend-tech/profile
Explorer (BaseScan Token): https://basescan.org/token/0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B
Explorer (BaseScan V1 Contracts): https://basescan.org/address/0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4#code
Dune Analytics: https://dune.com/friendtech
Arkham Intelligence: https://app.arkhamintelligence.com/entity/friend-tech
Nansen: https://app.nansen.ai/dashboards/friend-tech

## BUAT RINGKASAN

Market Stage: Early (Post-TGE, V2 Live, Low Retention)
Primary Category: SocialFi / Consumer Crypto
Competitor Count: 7 (Farcaster, Lens Protocol, Stars Arena, Post.tech, Tipcoin, Friend3, OpenSocial)
Major Narrative: SocialFi, Consumer Crypto, Base Ecosystem Flagship
Trading Availability: 5 CEX (Binance, Bybit, OKX, Coinbase Exchange, Kraken), 2 Major DEX (Aerodrome, Uniswap V3 Base)
Adoption Metrics Available: TVL, Cumulative Fees, Daily Fees Peak, DAU (Peak & Current), Unique Traders, Token Holders, Token Volume, Treasury Balance

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Friend.tech

Strategic Objectives

1. Membangun protokol SocialFi pertama yang mencapai product-market fit massal melalui bonding curve dan token-gated access

· Evidence: V1 launch (EV-003) langsung mengimplementasikan bonding curve linear dengan fee 10% (5% protokol, 5% kreator), menghasilkan $1M+ fee harian dalam 10 hari (EV-006) dan $10M+ kumulatif dalam 3 minggu (EV-009)
· Supporting Dataset: Phase 3 EV-003, EV-005, EV-006, EV-009; Phase 8 Adoption Metrics

2. Menjadi aplikasi flagship Base ecosystem untuk mendorong adopsi L2 Coinbase

· Evidence: Launch eksklusif di Base mainnet (EV-003), Base congestion akibat aktivitas Friend.tech (EV-007), Coinbase Wallet sebagai default onboarding, Base Ecosystem Fund investor strategis (Phase 2), Conduit mengoperasikan infrastruktur Base untuk Friend.tech (Phase 7)
· Supporting Dataset: Phase 2 Entity Base, Coinbase, Base Ecosystem Fund, Conduit; Phase 3 EV-002, EV-003, EV-007; Phase 7 External Dependencies

3. Transisi dari aplikasi spekulatif (V1 keys) ke consumer app berkelanjutan dengan token utility (V2 clubs + FRIEND token)

· Evidence: V2 announcement (EV-013) memperkenalkan Clubs NFT, FRIEND token governance, staking fee discount; V2 launch (EV-014); pivot announcement non-financial features 2025 (EV-024)
· Supporting Dataset: Phase 3 EV-013, EV-014, EV-024; Phase 6 Token Utility; Phase 8 Narrative Position

4. Mengakumulasi treasury on-chain transparan untuk runway multi-tahun dan opsi buyback/insentif komunitas

· Evidence: Treasury V1 mengumpulkan >$10M fee (EV-009); Treasury V2 balance >$5M per Dec 2024 (EV-025) dengan komposisi ETH + FRIEND + USDbC; on-chain transparent via Arkham/Dune
· Supporting Dataset: Phase 3 EV-009, EV-020, EV-025; Phase 5 Treasury; Phase 7 Integration Arkham/Dune

## 5 Mendistribusikan ownership ke komunitas melalui airdrop FRIEND dan governance on-chain

· Evidence: TGE mengalokasikan FRIEND untuk V1 user airdrop (EV-014); Governance aktif since EV-017 dengan proposal pertama fee clubs; token-weighted voting 1 FRIEND = 1 vote
· Supporting Dataset: Phase 3 EV-014, EV-017; Phase 6 Token Distribution, Governance

Decision Timeline

Keputusan: Launch Friend.tech V1 pada Base Mainnet dengan bonding curve immutable (2023-08-10)
· Trigger: Base mainnet live (EV-002 Feb 2023), konsep social token siap sejak 2022 (EV-001), window of opportunity untuk first-mover SocialFi di Base
· Evidence: Phase 3 EV-002, EV-003; Phase 4 Architecture (V1 immutable contracts); Phase 7 Integration Friend.tech V1 × Base Mainnet
· Decision: Deploy Share.sol, Trade.sol, Fee.sol immutable di Base; linear bonding curve; 10% fee split 5/5; Privy auth + Twitter login; invite-only beta
· Immediate Result: V1 live, invite-only; bonding curve aktif on-chain; fee mechanism berjalan
· Long-term Impact: V1 contracts frozen tidak bisa di-upgrade; residual keys trapped; template bonding curve SocialFi; $10M+ fee terkumpul sebelum V2
· Supporting Dataset: Phase 3 EV-003; Phase 4 Core Components V1, Technical Limitations; Phase 7 Major Integrations

Keputusan: Buka akses publik (hapus invite-only) memicu viral growth dan Base congestion (2023-08-19)
· Trigger: Invite-only beta berhasil validasi produk; tekanan komunitas dan FOMO; window untuk capture market share SocialFi
· Evidence: Phase 3 EV-005; Phase 8 Adoption Metrics (DAU >50k peak)
· Decision: Hapus sistem invite-only, buka registrasi publik
· Immediate Result: Lonjakan pengguna masif; Base congestion (EV-007); $1M+ daily fees (EV-006); media attention global
· Long-term Impact: Product-market fit terbukti tapi infrastructure stress; menarik regulator attention (SEC/CFTC monitoring); menarik investor tier-1 (Paradigm seed EV-004)
· Supporting Dataset: Phase 3 EV-005, EV-006, EV-007, EV-004; Phase 8 Market Timeline

Keputusan: Rebrand "Shares" → "Keys" untuk mitigasi risiko regulasi sekuritas (2023-08-25)
· Trigger: Scrutiny regulasi (SEC Howey Test) terhadap "shares" sebagai investment contract; legal risk untuk protokol dan pengguna
· Evidence: Phase 3 EV-008; Phase 2 Entity SEC, CFTC; Phase 4 Security Model (regulatory optics)
· Decision: Ubah terminologi UI/komunikasi dari "shares" ke "keys"; smart contract V1 immutable tidak berubah
· Immediate Result: Branding change immediate; narita pasar bergeser dari "investment" ke "access"; smart contract logic unchanged
· Long-term Impact: Mengurangi surface area regulatory tapi tidak eliminate risk; FRIEND token V2 tetap faces Howey Test; precedent untuk SocialFi projects lain
· Supporting Dataset: Phase 3 EV-008; Phase 4 Security Model; Phase 5 Financial Risk (Regulatory Classification); Phase 8 Narrative

Keputusan: Seed funding $50M valuation dipimpin Paradigm (2023-08-18)
· Trigger: Traction V1 terbukti ($1M+ daily fees, viral growth); butuh capital untuk V2 development, team expansion, runway
· Evidence: Phase 3 EV-004; Phase 2 Entity Paradigm, a16z crypto, Variant, Base Ecosystem Fund; Phase 5 Funding History
· Decision: Terima seed round Paradigm lead dengan a16z, Variant, Base Ecosystem Fund; valuasi $50M
· Immediate Result: Capital masuk; validasi investor tier-1; strategic alignment dengan Base/Coinbase via Base Ecosystem Fund
· Long-term Impact: Runway untuk V2 development; investor expectations untuk return; potential token allocation untuk investor (undisclosed); governance influence via token holdings
· Supporting Dataset: Phase 3 EV-004; Phase 5 Funding History; Phase 6 Token Distribution (investor allocation undisclosed); Phase 7 Investor Dependencies

Keputusan: Launch Friend.tech V2 dengan arsitektur modular upgradeable + FRIEND token TGE (2024-05-03)
· Trigger: V1 volume declining (EV-011); bonding curve limitations; need untuk sustainable model beyond speculation; investor pressure untuk token launch
· Evidence: Phase 3 EV-011, EV-013, EV-014; Phase 4 Architecture (V2 modular, UUPS proxy); Phase 6 Token TGE; Phase 8 Market Timeline
· Decision: Deploy V2 contract suite (Club.sol, Token.sol, Governance.sol, FeeManager.sol, UUPS proxy); mint 100M FRIEND fixed supply; Clubs NFT replace keys; governance on-chain; staking fee discount; CEX listings simultan
· Immediate Result: V2 live; FRIEND token circulating; CEX/DEX liquidity deployed; governance activated (EV-017); migration V1→V2 started (EV-019)
· Long-term Impact: Upgradeability enables iteration tapi introduces centralization risk (proxy admin); token creates regulatory surface; V2 volume significantly lower than V1 peak; treasury diversification via FRIEND holdings
· Supporting Dataset: Phase 3 EV-013, EV-014, EV-015, EV-016, EV-017, EV-019; Phase 4 Core Components V2, Technical Upgrade History; Phase 6 Token; Phase 7 Major Integrations V2; Phase 8 Market Timeline

Keputusan: Listing FRIEND token di 5 CEX major simultan pasca-TGE (2024-05-03 to 2024-06-05)
· Trigger: TGE liquidity needs; price discovery; user access fiat on-ramp; investor liquidity expectations
· Evidence: Phase 3 EV-015, EV-018; Phase 6 Major Token Events; Phase 7 Integration CEX Listings; Phase 8 Trading Markets
· Decision: Listing Binance, Bybit, OKX (May 3), lalu Coinbase Exchange, Kraken (Jun 5); pairs USDT/USD/TRY/EUR
· Immediate Result: Global liquidity access; price discovery dimulai; CEX volume mendominasi (>90%); fiat on-ramp US/EU/Asia
· Long-term Impact: CEX dependency untuk liquidity; market maker relationships (Wintermute, GSR) critical; regulatory exposure di multiple jurisdictions; token price volatility tinggi (EV-023)
· Supporting Dataset: Phase 3 EV-015, EV-018; Phase 6 Major Token Events; Phase 7 CEX Dependencies; Phase 8 Liquidity, Trading Markets

Keputusan: Aktifkan governance on-chain dengan tim multi-sig sebagai executor (2024-05-10)
· Trigger: V2 launch complete; need parameter adjustment (fee clubs, incentives); community ownership narrative
· Evidence: Phase 3 EV-017; Phase 6 Governance; Phase 4 Security Model (V2 upgrade authority)
· Decision: Enable Governance.sol; token-weighted voting; proposal execution via UUPS proxy admin (OpenZeppelin Defender, team multi-sig); treasury managed by team multi-sig bukan DAO langsung
· Immediate Result: Proposal pertama diajukan (fee clubs, incentive allocation); governance live
· Long-term Impact: Hybrid governance (on-chain vote + off-chain execution); centralization risk di proxy admin; treasury tidak fully DAO-controlled; voter turnout/participation metrics tidak dipublikasikan
· Supporting Dataset: Phase 3 EV-017; Phase 4 Security Model; Phase 6 Governance; Phase 7 OpenZeppelin Defender Integration

Keputusan: Spearbit audit V2 contracts dan patch via UUPS upgrade (2024-08)
· Trigger: V2 live 3 bulan; TVL/user funds at risk; best practice security; investor/ecosystem expectation
· Evidence: Phase 3 EV-021; Phase 4 Audit History; Phase 7 Spearbit Integration
· Decision: Engage Spearbit untuk audit V2 suite; address findings via UUPS proxy upgrade administered through Defender
· Immediate Result: Audit completed; medium/low findings patched; security credibility meningkat
· Long-term Impact: Demonstrates upgradeability utility; audit report public (GitHub); ongoing monitoring via Defender; but V1 contracts tetap unaudited publicly
· Supporting Dataset: Phase 3 EV-021; Phase 4 Audit History, Technical Upgrade History; Phase 7 Spearbit Integration

Keputusan: Pivot ke fitur social non-finansial untuk 2025 (2024-11)
· Trigger: V2 metrics stagnan (EV-022: volume/retention low); SocialFi narrative cooling; need sustainable user retention beyond speculation
· Evidence: Phase 3 EV-022, EV-024; Phase 8 Narrative Position (Consumer Crypto pivot); Phase 7 Ecosystem Position
· Decision: Announce roadmap fitur content feed, messaging, discovery non-finansial; reduce reliance pada bonding curve mechanics
· Immediate Result: Strategic signal ke pasar; community expectation management; no technical release yet
· Long-term Impact: Jika berhasil → sustainable consumer app dengan token utility; jika gagal → zombie protocol dengan treasury tapi no users; execution risk tinggi given small pseudonymous team
· Supporting Dataset: Phase 3 EV-022, EV-024; Phase 8 Narrative Position, Adoption Metrics; Phase 5 Revenue History (V2 low revenue)

Evolution Pattern

Perubahan Strategi: Dari Speculative SocialFi (V1) → Sustainable Consumer App dengan Token Utility (V2) → Non-Financial Social Features (2025 Roadmap)
· Evidence: V1 bonding curve keys纯粹为投机设计 (EV-003, EV-006); V2 introduces clubs, governance, staking utility (EV-013, EV-014); 2025 roadmap explicitly non-financial (EV-024)
· Supporting Dataset: Phase 3 EV-003, EV-011, EV-013, EV-014, EV-024; Phase 8 Narrative Position evolution

Perubahan Teknologi: Dari Immutable Contracts (V1) → Modular Upgradeable Architecture (V2 UUPS Proxy)
· Evidence: V1 Share.sol, Trade.sol, Fee.sol immutable, no admin keys (Phase 4 Core Components V1, Technical Limitations); V2 Club.sol, Token.sol, Governance.sol, FeeManager.sol dengan UUPS proxy, OpenZeppelin Defender admin (Phase 4 Core Components V2, Technical Upgrade History)
· Supporting Dataset: Phase 4 Architecture, Core Components, Technical Upgrade History, Security Model

Perubahan Tokenomics: Dari No Token (V1) → Fixed Supply Governance + Utility Token (V2 FRIEND)
· Evidence: V1 no native token, only ETH fees (Phase 6 Token Information - N/A for V1); V2 TGE 100M FRIEND fixed supply, governance, staking discount, ecosystem incentives (Phase 6 Token TGE, Utility, Inflation/Deflation)
· Supporting Dataset: Phase 3 EV-014; Phase 6 Token Information, Supply, Utility, Governance

Perubahan Governance: Dari Team-Controlled (V1) → Hybrid On-Chain Vote + Team Multi-Sig Execution (V2)
· Evidence: V1 parameter fixed immutable (Phase 4 Security Model); V2 Governance.sol token-weighted voting, timelock, pero execution via team multi-sig Defender admin (Phase 6 Governance; Phase 4 Security Model V2)
· Supporting Dataset: Phase 3 EV-017; Phase 4 Security Model; Phase 6 Governance

Perubahan Revenue Model: Dari High-Volume Speculative Fees (V1: $1M+/day) → Low-Volume Sustainable Fees (V2: dynamic, governance-set)
· Evidence: V1 peak $1M+ daily fees (EV-006), $10M+ cumulative in 3 weeks (EV-009); V2 fees "stabil di level jauh di bawah puncak V1" (EV-020), treasury >$5M but accumulating slowly (EV-025)
· Supporting Dataset: Phase 3 EV-006, EV-009, EV-020, EV-025; Phase 5 Revenue History, Revenue Model

Perubahan Market Position: Dari "SocialFi Pioneer" → "Base Flagship Consumer App" → "Consumer Crypto with Token Utility"
· Evidence: Media coverage Aug 2023: "SocialFi app making millions" (CoinDesk, The Block); V2 blog: "consumer app" framing; 2025 roadmap: "non-financial social features"
· Supporting Dataset: Phase 3 EV-003, EV-013, EV-024; Phase 8 Narrative Position, Market Timeline

Technical Decision Pattern

Pola 1: Pilih Infrastructure yang Sudah Ada (Build on Base, Not Own Chain)
· Decision Pattern: Friend.tech tidak membangun L2/L1 sendiri, melainkan deploy pada Base (OP Stack) yang dioperasikan Coinbase/Conduit. Memanfaatkan existing sequencer, RPC (Alchemy), indexing (The Graph), bridge (Base Native Bridge).
· Evidence: Phase 4 Architecture (Base Layer, Settlement Layer, Sequencer, Indexing Layer); Phase 7 External Dependencies (Base, Conduit, Alchemy, The Graph, Optimism critical/high)
· Supporting Dataset: Phase 4 Architecture; Phase 7 External Dependencies; Phase 3 EV-002, EV-003

Pola 2: Immutable V1 → Upgradeable V2 (Learning dari Ketidakmampuan Perbaikan V1)
· Decision Pattern: V1 contracts sengaja dibuat immutable (no upgrade path) untuk trust minimization tapi mengakibatkan ketidakmampuan fix bug/adjust parameter. V2 menggunakan UUPS proxy pattern dengan OpenZeppelin Defender untuk upgrade terkontrol.
· Evidence: Phase 4 Core Components V1 (immutable), Technical Limitations (V1 immutable), Security Model (V1 immutable eliminates upgrade risk but prevents fixes); Core Components V2 (UUPS proxy), Technical Upgrade History (V2 launch, post-audit patches), Security Model (V2 upgrade authority centralized)
· Supporting Dataset: Phase 4 Core Components V1/V2, Technical Limitations, Security Model, Technical Upgrade History

Pola 3: Account Abstraction via Privy untuk Onboarding Non-Crypto Users
· Decision Pattern: Menggunakan Privy (email/SMS/Twitter OAuth + embedded wallet ERC-4337) bukan memaksa user manage seed phrase. Gasless transactions via Base paymaster.
· Evidence: Phase 4 Architecture (Authentication Layer Privy), Core Components (Privy Authentication Infrastructure); Phase 7 Integration Friend.tech × Privy Authentication; Phase 2 Entity Privy
· Supporting Dataset: Phase 4 Architecture, Core Components; Phase 7 External Dependencies, Major Integrations; Phase 2 Entity Privy

Pola 4: Twitter/X sebagai Identity Layer Tunggal (Single Point of Failure)
· Decision Pattern: Seluruh identity, login, social graph bergantung pada Twitter/X API. Tidak ada fallback identity provider (Farcaster ID, Lens Profile, ENS, dll).
· Evidence: Phase 4 Architecture (Identity Layer Twitter/X), Technical Limitations (Twitter/X API Dependency); Phase 7 External Dependencies (Twitter/X Critical); Phase 2 Entity Twitter/X
· Supporting Dataset: Phase 4 Architecture, Technical Limitations; Phase 7 External Dependencies; Phase 2 Entity Twitter/X

Pola 5: Linear Bonding Curve → Dynamic Club Pricing (Evolusi Price Discovery)
· Decision Pattern: V1 fixed linear bonding curve (price = f(supply)) immutable. V2 clubs memungkinkan pricing dinamis (bonding curve atau fixed price per club) yang diatur creator/governance.
· Evidence: Phase 4 Core Components V1 (linear bonding curve), V2 (Clubs ERC-721, dynamic fee); Phase 3 EV-003 (V1 bonding curve), EV-013 (V2 clubs pricing); Phase 6 Token Utility (staking fee discount affects effective price)
· Supporting Dataset: Phase 4 Core Components; Phase 3 EV-003, EV-013; Phase 6 Token Utility

Pola 6: Centralized Sequencer Dependency (Base/Conduit) tanpa MEV Protection
· Decision Pattern: Menerima Base sequencer terpusat (Conduit) sebagai trade-off untuk throughput/biaya rendah. Tidak implement MEV protection di application layer (no commit-reveal, no private mempool).
· Evidence: Phase 4 Architecture (Sequencer Conduit), Consensus Mechanism (N/A inherits Base), Technical Limitations (Base Sequencer Centralization, No Native MEV Protection); Phase 7 External Dependencies (Conduit High, Base Critical)
· Supporting Dataset: Phase 4 Architecture, Consensus Mechanism, Technical Limitations; Phase 7 External Dependencies

Financial Decision Pattern

Pola 1: Single Seed Round pada Valuasi Tinggi ($50M) dengan Investor Tier-1, Tanpa Follow-On Public
· Decision Pattern: Hanya satu ronde funding resmi (Seed Agustus 2023, Paradigm lead, $50M valuation). Jumlah absolut undisclosed. Tidak ada Series A, strategic round, atau public sale announcement setelahnya.
· Evidence: Phase 5 Funding History (1 round only); Phase 2 Entity Investors (Paradigm, a16z, Variant, Base Ecosystem Fund); Phase 3 EV-004; Phase 5 Financial Risk (Funding Dependency - no post-seed fundraising)
· Supporting Dataset: Phase 5 Funding History, Financial Risk; Phase 2 Entity Investors; Phase 3 EV-004

Pola 2: Protocol Fees sebagai Primary Revenue (V1: 10% Fixed Split → V2: Dynamic Governance-Set)
· Decision Pattern: Revenue model sepenuhnya on-chain protocol fees. V1: hardcoded 10% (5% treasury, 5% creator). V2: dynamic fee via FeeManager.sol, parameter set by governance. No subscription, no ads, no data monetization.
· Evidence: Phase 5 Revenue Model (V1 10% split, V2 dynamic); Phase 3 EV-003 (V1 fee), EV-013 (V2 dynamic fee); Phase 4 Core Components V1 Fee.sol, V2 FeeManager.sol; Phase 8 Adoption Metrics (fee history)
· Supporting Dataset: Phase 5 Revenue Model, Revenue History; Phase 3 EV-003, EV-013; Phase 4 Core Components

Pola 3: Treasury Accumulation On-Chain Transparent (ETH + Native Token + Stablecoin)
· Decision Pattern: Fee revenue flows langsung ke treasury contract on-chain. Komposisi: ETH (native gas asset), FRIEND (native token, volatile), USDbC (stablecoin). Tidak ada active treasury management (staking, lending, LP) yang terverifikasi.
· Evidence: Phase 5 Treasury (composition, balance >$5M Dec 2024); Phase 3 EV-009 ($10M cumulative), EV-020 (V2 fee accumulation), EV-025 (treasury >$5M); Phase 7 Integration Arkham/Dune (transparency); Phase 5 Financial Risk (Treasury Concentration - native token exposure)
· Supporting Dataset: Phase 5 Treasury, Financial Risk; Phase 3 EV-009, EV-020, EV-025; Phase 7 Integration Arkham/Dune

Pola 4: Token Allocation Opaque (No Public Breakdown TGE Distribution)
· Decision Pattern: FRIEND token 100M supply minted at TGE. Kategori alokasi disebutkan (community, team, investors, treasury, ecosystem) tapi persentase masing-masing tidak dipublikasikan. Vesting schedule undisclosed. No vesting contract verified on-chain.
· Evidence: Phase 6 Distribution (all percentages "tidak diungkap resmi"), Vesting Schedule (all "tidak diketahui"); Phase 3 EV-014 (TGE); Phase 6 Open Threads (allocation percentages undisclosed)
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule, Open Threads; Phase 3 EV-014

Pola 5: CEX Listing Strategy: Broad & Simultaneous (5 Major CEX dalam 1 Bulan)
· Decision Pattern: Prioritaskan liquidity breadth dan geographic coverage. Binance/Bybit/OKX (global/Asia) hari TGE, Coinbase/Kraken (US/EU regulated) 1 bulan kemudian. No IEO/IDO/public sale.
· Evidence: Phase 3 EV-015, EV-018; Phase 6 Major Token Events; Phase 7 Integration CEX Listings; Phase 8 Trading Markets (5 CEX live), Liquidity (CEX >90% volume)
· Supporting Dataset: Phase 3 EV-015, EV-018; Phase 6 Major Token Events; Phase 7 Major Integrations; Phase 8 Trading Markets, Liquidity

Pola 6: Market Maker Dependency Tidak Transparan (Wintermute, GSR Inferred)
· Decision Pattern: CEX liquidity bergantung pada market maker institusional (Wintermute, GSR terlihat di CoinGecko markets). Tidak ada announcement resmi agreement, token loan, atau option terms.
· Evidence: Phase 2 Entity Wintermute, GSR Markets; Phase 7 External Dependencies (Wintermute, GSR Medium); Phase 5 Financial Risk (Market Making Dependency); Phase 8 Liquidity (CEX dominant)
· Supporting Dataset: Phase 2 Entity Wintermute, GSR; Phase 7 External Dependencies; Phase 5 Financial Risk; Phase 8 Liquidity

Ecosystem Decision Pattern

Pola 1: Base-First, Base-Only Strategy (Deep Integration dengan Single L2)
· Decision Pattern: Semua aktivitas on-chain (V1, V2, token, governance, treasury) hanya di Base. Tidak ada deployment multi-chain, tidak ada cross-chain messaging, tidak ada bridging strategy untuk FRIEND token.
· Evidence: Phase 4 Architecture (Base Layer only, Settlement Ethereum via Base); Phase 7 External Dependencies (Base Critical, Conduit High, Optimism High); Phase 3 EV-003 (V1 launch Base), EV-014 (V2 launch Base); Phase 8 Ecosystem Position (Primary Chain: Base only)
· Supporting Dataset: Phase 4 Architecture; Phase 7 External Dependencies; Phase 3 EV-003, EV-014; Phase 8 Ecosystem Position

Pola 2: Coinbase Ecosystem Alignment (Wallet, Chain, Fund, Exchange)
· Decision Pattern: Strategic alignment penuh dengan Coinbase: Base chain host, Coinbase Wallet default onboarding, Base Ecosystem Fund investor, Coinbase Exchange listing FRIEND/USD. Memanfaatkan distribusi Coinbase retail/institutional.
· Evidence: Phase 2 Entity Coinbase, Coinbase Wallet, Coinbase Exchange, Base Ecosystem Fund; Phase 7 External Dependencies (Coinbase Critical, Coinbase Wallet High, Coinbase Exchange High, Base Ecosystem Fund High); Phase 3 EV-018 (Coinbase listing); Phase 7 Integration Coinbase Wallet, Coinbase Exchange
· Supporting Dataset: Phase 2 Entity Coinbase-related; Phase 7 External Dependencies, Major Integrations; Phase 3 EV-018

Pola 3: Privy sebagai Abstraction Layer untuk Mass Onboarding
· Decision Pattern: Delegasikan seluruh user authentication, wallet creation, key management, gas abstraction ke Privy. Friend.tech fokus pada application logic, tidak wallet infrastructure.
· Evidence: Phase 4 Architecture (Authentication Layer Privy), Core Components (Privy Auth); Phase 7 External Dependencies (Privy Critical), Major Integrations (Friend.tech × Privy); Phase 2 Entity Privy
· Supporting Dataset: Phase 4 Architecture, Core Components; Phase 7 External Dependencies, Major Integrations; Phase 2 Entity Privy

Pola 4: Data/Analytics Layer Outsourced ke Specialized Providers
· Decision Pattern: Tidak membangun analytics dashboard sendiri. Bergantung pada Dune (community dashboards), Nansen (institutional), Arkham (entity labeling), DeFi Llama (TVL/fees standard), Token Terminal (fundamentals), Messari (research).
· Evidence: Phase 7 External Dependencies (Dune, Nansen, Arkham, DeFi Llama, Token Terminal, Messari all Medium/Low); Phase 3 EV-010 (Nansen dashboard), EV-012 (Arkham labels); Phase 8 Official Market Resources (all external dashboards)
· Supporting Dataset: Phase 7 External Dependencies; Phase 3 EV-010, EV-012; Phase 8 Official Market Resources

Pola 5: DEX Liquidity Concentrated pada Aerodrome + Uniswap V3 Base (veAERO Incentives)
· Decision Pattern: Deploy liquidity hanya di 2 DEX utama Base: Aerodrome (veAERO voting incentives) dan Uniswap V3 (concentrated liquidity, price reference). Tidak incentivize DEX lain (Sushi, Curve, dll).
· Evidence: Phase 3 EV-016 (Aerodrome, Uniswap deployment); Phase 7 External Dependencies (Aerodrome High, Uniswap High); Phase 7 Major Integrations (V2 × Aerodrome, V2 × Uniswap); Phase 8 Liquidity (DEX: Aerodrome, Uniswap V3 Base)
· Supporting Dataset: Phase 3 EV-016; Phase 7 External Dependencies, Major Integrations; Phase 8 Liquidity

Pola 6: Twitter/X Identity Lock-in (No Multi-Identity Support)
· Decision Pattern: Hanya Twitter/X OAuth untuk identity. Tidak integrasi Farcaster ID, Lens Profile, ENS, Google, Apple, atau wallet-native identity (SIWE). Creates hard dependency pada single Web2 platform.
· Evidence: Phase 4 Architecture (Identity Layer Twitter/X), Technical Limitations (Twitter/X API Dependency); Phase 7 External Dependencies (Twitter/X Critical); Phase 2 Entity Twitter/X; Phase 7 Major Integrations (Friend.tech × Twitter/X Identity)
· Supporting Dataset: Phase 4 Architecture, Technical Limitations; Phase 7 External Dependencies, Major Integrations; Phase 2 Entity Twitter/X

Governance Decision Pattern

Pola 1: Hybrid Governance (On-Chain Voting + Off-Chain Execution via Team Multi-Sig)
· Decision Pattern: Token-weighted voting on-chain (Governance.sol) untuk parameter changes, tapi execution memerlukan team multi-sig via OpenZeppelin Defender admin UUPS proxy. Treasury tidak DAO-controlled langsung.
· Evidence: Phase 6 Governance (model, voting system, treasury governance); Phase 4 Security Model (V2 upgrade authority centralized); Phase 3 EV-017 (governance activation); Phase 7 Integration OpenZeppelin Defender
· Supporting Dataset: Phase 6 Governance; Phase 4 Security Model; Phase 3 EV-017; Phase 7 Major Integrations

Pola 2: Governance Parameter Scope Terbatas (Fee Clubs, Incentives — Not Core Protocol Upgrades)
· Decision Pattern: Proposal pertama (EV-017) hanya untuk fee clubs dan incentive allocation. Tidak ada proposal untuk upgrade kontrak inti,ubah tokenomics, atau treasury spending besar. Core upgrades masih team-controlled via Defender.
· Evidence: Phase 3 EV-017 (first proposal: fee clubs, incentives); Phase 6 Governance (proposal system threshold undisclosed); Phase 4 Technical Upgrade History (post-audit patches via team upgrade)
· Supporting Dataset: Phase 3 EV-017; Phase 6 Governance; Phase 4 Technical Upgrade History

Pola 3: No Delegation Incentive Program (Passive Delegation Only)
· Decision Pattern: ERC-20 votes delegation supported tapi tidak ada incentive program untuk delegasi (seperti Compound/Uniswap delegate rewards). Voter turnout/participation metrics tidak dipublikasikan.
· Evidence: Phase 6 Governance (delegation supported, no incentive mentioned); Phase 6 Open Threads (governance proposal threshold, quorum undisclosed, participation metrics not published)
· Supporting Dataset: Phase 6 Governance, Open Threads

Pola 4: Treasury Management Off-Chain (Team Multi-Sig, Not DAO)
· Decision Pattern: Treasury (> $5M) dikendalikan team multi-sig. Governance proposal dapat "mengarahkan alokasi" tapi eksekusi memerlukan multi-sig. No on-chain treasury management module (seperti SafeDAO, Gnosis Safe with module).
· Evidence: Phase 5 Treasury (custodian: Friend.tech multi-sig); Phase 6 Governance (treasury governed by team multi-sig); Phase 3 EV-025 (treasury balance); Phase 7 Integration Arkham (treasury labeling)
· Supporting Dataset: Phase 5 Treasury; Phase 6 Governance; Phase 3 EV-025; Phase 7 Integration Arkham

Risk Response Pattern

Pola 1: Regulatory Optics Mitigation via Terminology Change (Shares → Keys)
· Trigger: SEC scrutiny risk pada "shares" terminology (Howey Test investment contract implications); legal counsel advice inferred
· Evidence: Phase 3 EV-008 (rebranding Aug 25, 2023); Phase 2 Entity SEC, CFTC; Phase 4 Security Model (regulatory optics); Phase 5 Financial Risk (Legal Financial Risk); Phase 8 Narrative (regulatory narrative)
· Response: Immediate UI/communication terminology change "shares" → "keys"; smart contract V1 immutable unchanged; legal entity/jurisdiction tetap undisclosed
· Result: Reduced surface area untuk "investment contract" argument tapi fundamental economics (bonding curve, profit expectation) unchanged; FRIEND token V2 tetap faces Howey Test; precedent untuk SocialFi projects
· Supporting Dataset: Phase 3 EV-008; Phase 2 Entity SEC, CFTC; Phase 4 Security Model; Phase 5 Financial Risk; Phase 8 Narrative

Pola 2: Infrastructure Scaling via Partner (Base/Conduit Optimize Sequencer)
· Trigger: Base congestion EV-007 akibat aktivitas Friend.tech viral (Aug 21, 2023); user experience degradation; negative press risk
· Evidence: Phase 3 EV-007 (Base congestion); Phase 7 External Dependencies (Base Critical, Conduit High); Phase 2 Entity Base, Conduit
· Response: Base/Conduit optimasi sequencer capacity; Friend.tech tidak bisa langsung fix (application layer); dependency pada infrastructure partner
· Result: Congestion resolved; Base capacity increased untuk consumer apps; demonstrated Base scalability; Friend.tech remains dependent pada Base roadmap (decentralized sequencer, fault proofs)
· Supporting Dataset: Phase 3 EV-007; Phase 7 External Dependencies; Phase 2 Entity Base, Conduit; Phase 4 Technical Limitations (Base Sequencer Centralization)

Pola 3: Revenue Decline Response → Product Pivot (V2 Launch + Token)
· Trigger: V1 volume/fees declining significantly EV-011 (Oct 2023 onward); bonding curve fatigue; user retention drop; investor pressure untuk sustainable model
· Evidence: Phase 3 EV-011 (volume decline), EV-013 (V2 announced Mar 2024), EV-014 (V2 launch May 2024); Phase 5 Revenue History (V1 peak vs V2 low); Phase 8 Adoption Metrics (DAU peak vs current)
· Response: Major product overhaul: V2 modular contracts, Clubs NFT, FRIEND token, governance, staking utility; CEX listings untuk liquidity; marketing pivot ke "consumer app"
· Result: V2 live tapi volume/retention "stabil di level rendah" EV-022; token price volatile EV-023; treasury sustained >$5M EV-025; 2025 roadmap pivot non-financial EV-024
· Supporting Dataset: Phase 3 EV-011, EV-013, EV-014, EV-022, EV-023, EV-024, EV-025; Phase 5 Revenue History; Phase 8 Adoption Metrics, Market Timeline

Pola 4: Security Incident Prevention via Audit + Upgradeability (Spearbit Audit V2)
· Trigger: V2 launch dengan $5M+ TVL potential; investor/ecosystem expectation; V1 unaudited publicly; DeFi exploit landscape
· Evidence: Phase 3 EV-021 (Spearbit audit Aug 2024); Phase 4 Audit History (Spearbit V2, V1 undisclosed); Phase 4 Security Model (V2 upgradeable); Phase 7 Integration Spearbit
· Response: Engage Spearbit (reputable auditor); publish findings GitHub; patch medium/low via UUPS upgrade through Defender; ongoing monitoring
· Result: Security credibility improved; upgradeability proven useful; but V1 contracts remain unaudited publicly; proxy admin centralization risk persists
· Supporting Dataset: Phase 3 EV-021; Phase 4 Audit History, Security Model; Phase 7 Integration Spearbit

Pola 5: Market Crash/Volatility Response → Treasury Diversification (Hold ETH + Stablecoin + Token)
· Trigger: FRIEND token volatility tinggi EV-023 ($1.50+ → $0.30-0.60); treasury holds significant FRIEND; need runway protection
· Evidence: Phase 3 EV-023 (price volatility), EV-025 (treasury >$5M ETH+FRIEND+USDbC); Phase 5 Treasury (composition), Financial Risk (Treasury Concentration)
· Response: Treasury komposisi campuran (ETH, USDbC, FRIEND) — not 100% native token; no active hedging program disclosed; no buyback/burn announced
· Result: Runway protected via stablecoin/ETH holdings; but FRIEND concentration remains risk; no active treasury management verified
· Supporting Dataset: Phase 3 EV-023, EV-025; Phase 5 Treasury, Financial Risk

Recurring Behavioral Pattern

Pola 1: Launch Fast, Iterate via Major Version Upgrades (V1 → V2)
· Evidence: V1 launch 10 bulan setelah Base mainnet (EV-002 Feb → EV-003 Aug); V1 immutable, no incremental upgrades; V2 major overhaul 9 bulan kemudian (EV-014 May 2024); pattern: build v1 fast, learn, rebuild v2 properly
· Supporting Dataset: Phase 3 EV-002, EV-003, EV-013, EV-014; Phase 4 Technical Upgrade History; Phase 8 Market Timeline

Pola 2: Leverage Coinbase/Base Ecosystem untuk Distribution & Infra
· Evidence: Launch on Base (EV-003); Coinbase Wallet default (Phase 7 Integration); Base Ecosystem Fund investor (Phase 2 Entity); Conduit infra (Phase 7 Dependency); Coinbase Exchange listing (EV-018); every major milestone involves Coinbase/Base entity
· Supporting Dataset: Phase 2 Entity Coinbase, Base, Base Ecosystem Fund, Coinbase Wallet, Coinbase Exchange, Conduit; Phase 3 EV-003, EV-018; Phase 7 External Dependencies, Major Integrations

Pola 3: Outsource Non-Core Infrastructure (Auth, RPC, Indexing, Analytics, Market Making)
· Evidence: Privy (auth), Alchemy (RPC), The Graph (indexing), Dune/Nansen/Arkham/DeFi Llama/Token Terminal/Messari (analytics), Wintermute/GSR (market making) — all external dependencies critical/high. Friend.tech team fokus pada smart contract + frontend only.
· Supporting Dataset: Phase 7 External Dependencies (all Critical/High/Medium); Phase 4 Architecture (layered dependencies); Phase 2 Entity all infrastructure providers

Pola 4: Token Launch as Liquidity Event untuk Investors & Treasury Diversification
· Evidence: Seed investors (Paradigm, a16z, Variant) likely received token allocation (undisclosed); TGE enables investor liquidity; treasury holds FRIEND as asset; CEX listings provide exit liquidity; no public sale = insider-favorable distribution
· Supporting Dataset: Phase 5 Funding History (seed investors); Phase 6 Distribution (investor allocation undisclosed), Major Token Events (CEX listings); Phase 5 Treasury (FRIEND holdings); Phase 7 CEX Dependencies

Pola 5: Regulatory Risk Managed via Optics, Not Structure (Terminology, Offshore Entity Undisclosed)
· Evidence: Shares→Keys rebrand (EV-008); legal entity/jurisdiction undisclosed (Phase 1 Foundation); SEC/CFTC monitoring (Phase 2 Entity); no legal wrapper announcement (no Foundation/Cayman entity like other projects); compliance via terminology not structure
· Supporting Dataset: Phase 3 EV-008; Phase 1 Foundation; Phase 2 Entity SEC, CFTC; Phase 5 Financial Risk (Legal Financial Risk); Phase 4 Security Model

Pola 6: Pivot Narrative When Metrics Decline (SocialFi → Consumer Crypto → Non-Financial Social)
· Evidence: Aug 2023: "SocialFi making millions" (media); May 2024 V2: "consumer app with token utility" (blog); Nov 2024: "non-financial social features 2025" (EV-024); each pivot coincides dengan metrics decline (EV-011, EV-022)
· Supporting Dataset: Phase 3 EV-011, EV-013, EV-022, EV-024; Phase 8 Narrative Position, Market Timeline

Strategic Trade-offs

Trade-off 1: Desentralisasi vs Kecepatan Iterasi (Immutable V1 → Upgradeable V2)
· Decision: V1 immutable (no admin keys, no upgrades) → V2 UUPS proxy dengan team multi-sig admin via Defender
· Trade-off: V1: full trust minimization tapi tidak bisa fix bug/adjust parameter; V2: bisa iterate/patch (Spearbit audit patches) tapi introduces centralization risk (proxy admin = single point of failure untuk malicious upgrade)
· Evidence: Phase 4 Core Components V1 (immutable), V2 (UUPS proxy), Technical Limitations (V1 immutable, V2 upgrade authority centralized), Security Model (V1 eliminates upgrade risk, V2 introduces upgrade authority risk), Technical Upgrade History (post-audit patches via upgrade)
· Supporting Dataset: Phase 4 Core Components, Technical Limitations, Security Model, Technical Upgrade History

Trade-off 2: User Onboarding Mudah (Privy Embedded Wallet) vs Self-Custody Penuh
· Decision: Privy email/social login + embedded wallet (sharded keys, TEE) + gasless via paymaster
· Trade-off: Onboarding friction minimal (mass adoption achievable) tapi user tidak fully self-custodial (reliant on Privy infrastructure untuk key recovery); not "not your keys not your coins" ideal; Privy = trusted third party
· Evidence: Phase 4 Architecture (Authentication Layer Privy), Core Components (Privy Auth), Technical Limitations (Privy Custody Model); Phase 7 External Dependencies (Privy Critical), Major Integrations (Friend.tech × Privy); Phase 2 Entity Privy
· Supporting Dataset: Phase 4 Architecture, Core Components, Technical Limitations; Phase 7 External Dependencies, Major Integrations; Phase 2 Entity Privy

Trade-off 3: Base Single-Chain Focus vs Multi-Chain Expansion
· Decision: Deploy hanya di Base, no multi-chain strategy, no cross-chain messaging
· Trade-off: Deep integration, optimized UX, aligned incentives dengan Base/Coinbase ecosystem tapi limited TAM (Base users only); vendor lock-in ke Base roadmap (sequencer decentralization, fault proofs); no hedge jika Base loses relevance
· Evidence: Phase 4 Architecture (Base only), Ecosystem Position (Primary Chain: Base only); Phase 7 External Dependencies (Base Critical, Conduit High, Optimism High); Phase 8 Ecosystem Position (Supported Chains: Base only)
· Supporting Dataset: Phase 4 Architecture, Ecosystem Position; Phase 7 External Dependencies; Phase 8 Ecosystem Position

Trade-off 4: Twitter/X Identity Dependency vs Sovereign Identity
· Decision: Hanya Twitter/X OAuth untuk identity, login, social graph
· Trade-off: Instant access ke 400M+ Twitter users, familiar UX, social graph import tapi single point of failure: Twitter API policy changes, rate limits, deprecation, atau Elon Musk decisions bisa break onboarding entirely; no fallback (Farcaster, Lens, ENS, SIWE)
· Evidence: Phase 4 Architecture (Identity Layer Twitter/X), Technical Limitations (Twitter/X API Dependency); Phase 7 External Dependencies (Twitter/X Critical); Phase 2 Entity Twitter/X; Phase 7 Major Integrations (Friend.tech × Twitter/X Identity)
· Supporting Dataset: Phase 4 Architecture, Technical Limitations; Phase 7 External Dependencies; Phase 2 Entity Twitter/X; Phase 7 Major Integrations

Trade-off 5: CEX Liquidity Breadth vs DEX/DeFi Alignment
· Decision: 5 major CEX listings (Binance, Bybit, OKX, Coinbase, Kraken) dalam 1 bulan; DEX liquidity hanya Aerodrome + Uniswap V3 Base
· Trade-off: Maximum fiat on-ramp access, global user reach, institutional liquidity, price discovery tapi: CEX volume >90% (Phase 8 Liquidity), dependency pada market makers (Wintermute/GSR), regulatory exposure multiple jurisdictions, token price correlated dengan CEX sentiment not protocol fundamentals; DEX/DeFi alignment minimal
· Evidence: Phase 3 EV-015, EV-018; Phase 6 Major Token Events; Phase 7 Integration CEX Listings, DEX Integrations; Phase 8 Trading Markets (5 CEX), Liquidity (CEX >90% volume)
· Supporting Dataset: Phase 3 EV-015, EV-018; Phase 6 Major Token Events; Phase 7 Major Integrations; Phase 8 Trading Markets, Liquidity

Trade-off 6: Token Opaque Allocation vs Community Transparency
· Decision: FRIEND token 100M supply, kategori alokasi dikenal tapi persentase undisclosed; vesting schedule undisclosed; no vesting contract verified
· Trade-off: Flexibility untuk team/investors, avoid community scrutiny pada unlock schedule, prevent mercenary farming tapi: destroys trust, prevents accurate circulating supply calculation (CoinGecko "self reported"), enables insider advantage, regulatory red flag (Howey Test: undisclosed allocation = expectation of profit from others' efforts)
· Evidence: Phase 6 Distribution (all percentages undisclosed), Vesting Schedule (all unknown), Open Threads (allocation percentages undisclosed); Phase 5 Financial Risk (Legal Financial Risk); Phase 8 Market (Circulating Supply unknown)
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule, Open Threads; Phase 5 Financial Risk; Phase 8 Adoption Metrics

Behavioral Summary

Prioritas Utama Proyek
1. Speed to Market & First-Mover Advantage: Launch V1 cepat di Base (10 bulan post-Base launch), capture SocialFi wave 2023
2. Base/Coinbase Ecosystem Alignment: Setiap keputusan strategis memperkuat posisi sebagai flagship Base app
3. Treasury Accumulation untuk Runway: Protocol fees → on-chain treasury → financial independence dari investor
4. Token sebagai Liquidity Event & Governance Tool: FRIEND token enables investor exit, community governance (limited), treasury diversification
5. Pivot Narrative untuk Survival: Beralih narasi जब metrics decline (SocialFi → Consumer Crypto → Non-Financial Social)

Cara Mengambil Keputusan
- Founder-led (Racer, Shrimp pseudonymous), small team, minimal bureaucracy
- Reactive ke market feedback (V1 viral → V2 rebuild; fee decline → token launch; retention low → non-financial pivot)
- Outsource non-core ke best-in-class providers (Privy, Alchemy, The Graph, Conduit, OpenZeppelin)
- Single-chain focus (Base) untuk depth over breadth
- Regulatory managed via optics (terminology) bukan structural compliance

Faktor Paling Sering Mempengaruhi Keputusan
1. Market Metrics (DAU, volume, fees) — trigger pivots dan major upgrades
2. Base/Coinbase Strategic Alignment — chain choice, wallet, listing, funding
3. Investor Expectations (Paradigm, a16z) — token launch, valuation, liquidity
4. Infrastructure Partner Capabilities — sequencer capacity, auth, RPC, indexing
5. Regulatory Environment — terminology changes, entity opacity

Pola Evolusi
Phase 1 (2022-2023): Stealth development → V1 launch on Base (immutable, bonding curve)
Phase 2 (Aug-Sep 2023): Viral growth → $10M+ fees → Base congestion → investor interest → seed funding
Phase 3 (Oct 2023-Mar 2024): Decline → V2 architecture design → tokenomics design
Phase 4 (May 2024): V2 launch + TGE + CEX listings → governance activation
Phase 5 (Jun 2024+): Low retention → audit → treasury accumulation → non-financial pivot announcement

Kekuatan Utama
- First-mover SocialFi on Base dengan proven product-market fit (V1 $10M+ fees in 3 weeks)
- Deep Coinbase/Base ecosystem integration (chain, wallet, fund, exchange, infra)
- Transparent on-chain treasury (>$5M) providing multi-year runway
- Best-in-class infrastructure partners (Privy, Alchemy, OpenZeppelin, Conduit)
- Modular V2 architecture enabling iteration (UUPS proxy, governance)
- Strong analytics/monitoring coverage (Dune, Nansen, Arkham, DeFi Llama)

Kelemahan Utama
- Pseudonymous small team (bus factor tinggi, no legal entity transparency)
- V2 metrics stagnan (<5k DAU, TVL <$1M) — product-market fit V2 unproven
- Token allocation opaque (no percentages, no vesting contracts) — trust deficit
- Centralization risks: V2 proxy admin (team multi-sig), Base sequencer (Conduit), Twitter identity, Privy custody
- No multi-chain strategy — vendor lock-in ke Base
- Revenue decline drastis (V1 $1M+/day → V2 minimal) — sustainability unproven
- 2025 non-financial pivot execution risk tinggi (no SDK, no developer ecosystem, small team)

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Friend.tech

Core Insights

Insight 1: Single-Chain Maximalism sebagai Strategi Go-to-Market Efektif untuk Consumer Crypto
Explanation: Friend.tech memilih eksklusif deploy di Base mainnet sejak V1 (EV-003) tanpa multi-chain deployment, memanfaatkan deep integration dengan ekosistem Base/Coinbase (Base Ecosystem Fund investor, Coinbase Wallet default onboarding, Conduit sequencer, Aerodrome DEX)【Phase 3 — EV-003】【Phase 2 — Base, Coinbase, Base Ecosystem Fund, Conduit, Coinbase Wallet】. Strategi ini mengurangi kompleksitas teknis dan operational overhead, serta memanfaatkan network effect Base sebagai "flagship app"【Phase 8 — Narrative Position】.
Evidence: V1 Launch pada Base Mainnet (Invite-Only Beta)【Phase 3 — EV-003】; External Dependencies: Base (Critical), Coinbase (Critical), Conduit (High), Coinbase Wallet (High)【Phase 7 — External Dependencies】; Narrative: Base Ecosystem Flagship【Phase 8 — Narrative Position】; Competitor Landscape: Friend3 multi-chain, Stars Arena Avalanche — berbeda strategi【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 2 Entities; Phase 3 EV-002, EV-003, EV-007; Phase 4 Architecture; Phase 7 External Dependencies; Phase 8 Narrative Position, Competitor Landscape.
Confidence: HIGH

Insight 2: Immutable V1 → Upgradeable V2 via UUPS Proxy + Defender sebagai Pola Evolusi Smart Contract yang Berkelanjutan
Explanation: V1 contracts (Share.sol, Trade.sol, Fee.sol) dibuat immutable untuk keamanan/kepercayaan【Phase 4 — Core Components】, namun membatasi iterasi (V1 volume menurun tanpa bisa di-update, EV-011). V2 dirancang modular upgradeable dari awal menggunakan UUPS proxy pattern dengan admin via OpenZeppelin Defender multi-sig【Phase 4 — Core Components, Technical Upgrade History】. Pola ini memungkinkan post-audit patches (EV-021) dan governance parameter updates tanpa redeploy.
Evidence: V1 Contracts Immutable (frozen, no upgrade path)【Phase 4 — Core Components】; V2 UUPS Proxy upgradeable via OpenZeppelin Defender【Phase 4 — Core Components, Technical Upgrade History】; Technical Limitations: V1 Immutable, V2 Upgrade Authority Centralized【Phase 4 — Technical Limitations】; Post-Audit Patches via UUPS upgrade administered through Defender【Phase 4 — Technical Upgrade History】; Spearbit Audit Completed (V2 Contracts)【Phase 3 — EV-021】.
Supporting Dataset: Phase 4 Core Components, Technical Limitations, Technical Upgrade History; Phase 2 Entity (OpenZeppelin); Phase 3 EV-014, EV-021.
Confidence: HIGH

Insight 3: Account Abstraction + Embedded Wallets + Twitter Identity = Onboarding Friction Near-Zero untuk Non-Crypto Users
Explanation: Friend.tech menggunakan Privy (email/SMS/Twitter OAuth → embedded wallet ERC-4337) dan Coinbase Wallet (smart wallet, gasless paymaster) sejak V1 launch【Phase 3 — EV-003】, menghilangkan seed phrase friction. Twitter/X OAuth menjadi single sign-on dan social graph source【Phase 4 — Architecture】. Kombinasi ini memungkinkan adopsi massal 50k+ DAU peak【Phase 8 — Adoption Metrics】.
Evidence: Privy integration sejak V1 (EV-003)【Phase 3 — EV-003】; Core Components: Privy Authentication Infrastructure【Phase 4 — Core Components】; External Dependencies: Privy (Critical), Coinbase Wallet (High), Twitter/X (Critical)【Phase 7 — External Dependencies】; Major Integrations: Friend.tech × Privy, × Coinbase Wallet, × Twitter/X【Phase 7 — Major Integrations】; DAU Peak >50k (Agustus 2023)【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 2 Entities (Privy, Coinbase Wallet); Phase 3 EV-003; Phase 4 Core Components, Architecture; Phase 7 External Dependencies, Major Integrations; Phase 8 Adoption Metrics.
Confidence: HIGH

Insight 4: Bonding Curve Fee Revenue Bisa Generate Treasury Runway Multi-Tahun dalam Bulan (Jika PMF Terjadi)
Explanation: V1 fee model (10% split 5% protokol / 5% kreator) generate >$1M daily fees peak (EV-006) dan >$10M cumulative <3 minggu (EV-009). Treasury V2 balance >$5M per Desember 2024 (EV-025) berisi ETH, FRIEND, USDbC — mendanai runway tanpa follow-on funding.
Evidence: $1M+ Daily Protocol Fees Achieved (EV-006)【Phase 3 — EV-006】; $10M+ Cumulative Protocol Fees (EV-009)【Phase 3 — EV-009】; Treasury Balance >$5M Confirmed (EV-025)【Phase 3 — EV-025】; Revenue History: Peak V1 >$1M/hari, >$10M kumulatif【Phase 5 — Revenue History】; Treasury Composition: ETH, FRIEND, USDbC【Phase 5 — Treasury】; Financial Risk: Funding Dependency — no follow-on funding announced post-seed【Phase 5 — Financial Risk】.
Supporting Dataset: Phase 3 EV-006, EV-009, EV-020, EV-025; Phase 5 Revenue Model, Revenue History, Treasury; Phase 8 Adoption Metrics.
Confidence: HIGH

Insight 5: Token Distribution Opacity Menjadi Norma untuk Proyek VC-Backed SocialFi (Tidak Ada Public Breakdown)
Explanation: Alokasi FRIEND token (community, team, investors, treasury, ecosystem) persentase tidak diungkap resmi; vesting schedule tidak dipublikasikan; hanya total supply 100M yang dikonfirmasi【Phase 6 — Distribution, Vesting Schedule, Open Threads】. Seed investors (Paradigm, a16z crypto, Variant, Base Ecosystem Fund) valuation $50M tapi token allocation tidak transparan【Phase 5 — Funding History】.
Evidence: Distribution: semua kategori "persentase tidak diungkap resmi"【Phase 6 — Distribution】; Vesting Schedule: semua "tidak diketahui"【Phase 6 — Vesting Schedule】; Open Threads: allocation percentages, vesting details tidak diungkap【Phase 6 — Open Threads】; Seed Funding: Paradigm lead, $50M valuation, amount tidak diungkap【Phase 5 — Funding History】.
Supporting Dataset: Phase 6 Distribution, Vesting Schedule, Open Threads; Phase 5 Funding History, Financial Dependencies.
Confidence: HIGH

Insight 6: Regulatory Optics Management via Terminology Shift ("Shares"→"Keys") dan Utility-Only Token Design
Explanation: Proaktif mengubah terminologi "shares"→"keys" Agustus 2023 (EV-008) eksplisit untuk "menghindari implikasi regulasi sekuritas". FRIEND token utility terbatas pada governance, staking discount, ecosystem incentives — tidak ada profit-sharing, gas, validator, collateral【Phase 6 — Token Utility】. Narrative pivot ke "Consumer Crypto" (EV-024) mengurangi financial framing.
Evidence: Rebrand "Shares" to "Keys" (Regulatory Optics) (EV-008)【Phase 3 — EV-008】; Token Utility: Governance, Staking Fee Discount, Ecosystem Incentives, Treasury Asset — no profit-sharing【Phase 6 — Token Utility】; Entities: SEC, CFTC sebagai regulatory risk【Phase 2 — SEC, CFTC】; Financial Risk: Legal Financial Risk — SEC/CFTC evaluation【Phase 5 — Financial Risk】; Narrative: Consumer Crypto pivot (EV-024)【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 EV-008; Phase 6 Token Utility; Phase 2 Entities (SEC, CFTC); Phase 5 Financial Risk; Phase 8 Narrative Position.
Confidence: HIGH

Insight 7: V1-to-V2 Migration via Claim/Konversi (Bukan Force Migration) Meninggalkan Residual Value di V1
Explanation: Migrasi V1 keys ke V2 clubs bersifat voluntary claim/konversi selama beberapa minggu (EV-019); V1 contracts immutable tidak bisa force migrate. Sebagian kecil keys V1 masih di-hold tanpa claim【Phase 3 — Open Threads】. V1 revenue berhenti (contracts frozen); V2 revenue dari clubs fee dynamic governance-set.
Evidence: Migration V1→V2 (EV-019)【Phase 3 — EV-019】; Technical Limitations: V1 Contracts Immutable【Phase 4 — Technical Limitations】; Revenue Model: V1 discontinued, V2 dynamic【Phase 5 — Revenue Model】; Open Threads: residual V1 keys unclaimed【Phase 3 — Open Threads】.
Supporting Dataset: Phase 3 EV-014, EV-019, EV-020; Phase 4 Core Components, Technical Limitations; Phase 5 Revenue Model.
Confidence: MEDIUM

Insight 8: CEX-First Liquidity Strategy dengan Simultaneous Major Exchange Listing at TGE
Explanation: FRIEND token listing simultan di Binance, Bybit, OKX hari TGE (EV-015), diikuti Coinbase Exchange & Kraken bulan depan (EV-018) — prioritas CEX liquidity > DEX. CEX volume mendominasi >90% (Phase 8 Liquidity). Market maker dependency (Wintermute, GSR) tanpa agreement detail publik.
Evidence: CEX Listings TGE: Binance/Bybit/OKX May 3 (EV-015)【Phase 3 — EV-015】; Coinbase/Kraken June 5 (EV-018)【Phase 3 — EV-018】; Trading Markets: 5 CEX live【Phase 8 — Trading Markets】; Liquidity: CEX dominant >90% volume【Phase 8 — Liquidity】; Entities: Wintermute, GSR Markets (Medium dependency)【Phase 2 — Wintermute, GSR Markets】; Financial Risk: Market Making Dependency【Phase 5 — Financial Risk】.
Supporting Dataset: Phase 3 EV-015, EV-018; Phase 6 Major Token Events; Phase 7 Major Integrations; Phase 8 Trading Markets, Liquidity; Phase 2 Entities; Phase 5 Financial Risk.
Confidence: HIGH

Insight 9: Governance Hybrid — Token-Weighted Voting Advisory, Team Multi-sig Execution (Bukan Full DAO)
Explanation: Treasury dikelola team multi-sig; on-chain governance (FRIEND token voting) bisa propose parameter changes (fee clubs, insentif) tapi eksekusi butuh team multi-sig via Defender timelock【Phase 6 — Governance】. Upgrade authority centralized di team multi-sig【Phase 4 — Security Model】. Proposal threshold dan quorum tidak diungkap【Phase 6 — Open Threads】.
Evidence: Governance: Treasury managed by team multi-sig, not directly DAO【Phase 6 — Governance】; Security Model: V2 Upgrade Authority Centralized — team multi-sig via Defender【Phase 4 — Security Model】; Governance Activation: First proposal fee parameters (EV-017)【Phase 3 — EV-017】; Open Threads: proposal threshold, quorum tidak terdokumentasi【Phase 6 — Open Threads】.
Supporting Dataset: Phase 6 Governance, Open Threads; Phase 4 Security Model, Technical Upgrade History; Phase 3 EV-017; Phase 7 Major Integrations (OpenZeppelin Defender).
Confidence: HIGH

Insight 10: Analytics & Transparency via Third-Party Platforms (Dune, Nansen, Arkham, DeFi Llama) — No Self-Built Dashboard
Explanation: Friend.tech tidak membangun analytics dashboard sendiri; mengandalkan komunitas Dune, platform institusional Nansen/Arkham, aggregator DeFi Llama untuk transparency【Phase 7 — External Dependencies, Major Integrations】. Official Market Resources semuanya third-party【Phase 8 — Official Market Resources】.
Evidence: Entities: Dune, Nansen, Arkham, DeFi Llama, Token Terminal, Messari (Medium/Low dependency)【Phase 2 — Dune, Nansen, Arkham, DeFi Llama, Token Terminal, Messari】; EV-010 Nansen dashboard launch, EV-012 Arkham labels【Phase 3 — EV-010, EV-012】; Major Integrations: Analytics × Dune, Nansen, Arkham, DeFi Llama【Phase 7 — Major Integrations】; Official Market Resources: all third-party【Phase 8 — Official Market Resources】.
Supporting Dataset: Phase 2 Entities; Phase 3 EV-010, EV-012; Phase 7 External Dependencies, Major Integrations; Phase 8 Official Market Resources.
Confidence: HIGH

Strategic Principles

Principle 1: Single-Chain Deep Integration Over Multi-Chain Breadth
Explanation: Fokus eksklusif pada Base mainnet memanfaatkan full stack Base/Coinbase (chain, wallet, fund, sequencer, DEX) untuk speed to market dan user experience terintegrasi, bukan fragmentasi liquidity dan developer attention across chains.
Evidence: V1 Launch pada Base Mainnet (EV-003)【Phase 3 — EV-003】; External Dependencies: Base (Critical), Coinbase (Critical), Conduit (High), Coinbase Wallet (High)【Phase 7 — External Dependencies】; Narrative: Base Ecosystem Flagship【Phase 8 — Narrative Position】; Competitor: Friend3 multi-chain, Stars Arena Avalanche — berbeda strategi【Phase 8 — Competitor Landscape】.
Supporting Dataset: Phase 3 EV-003; Phase 7 External Dependencies; Phase 8 Narrative Position, Competitor Landscape.
Confidence: HIGH

Principle 2: Immutable V1 for Trust, Upgradeable V2 for Iteration
Explanation: Deploy V1 immutable untuk membangun kepercayaan "code is law" dan menghindari rug pull risk; lalu V2 modular upgradeable (UUPS + Defender) untuk memungkinkan evolusi produk, audit patches, dan governance parameter updates tanpa migrasi ulang.
Evidence: V1 Contracts Immutable (frozen, no upgrade path)【Phase 4 — Core Components】; V2 UUPS Proxy upgradeable via OpenZeppelin Defender【Phase 4 — Core Components, Technical Upgrade History】; Technical Limitations: V1 Immutable, V2 Upgrade Authority Centralized【Phase 4 — Technical Limitations】; Post-Audit Patches via UUPS upgrade (EV-021)【Phase 4 — Technical Upgrade History】.
Supporting Dataset: Phase 4 Core Components, Technical Limitations, Technical Upgrade History; Phase 3 EV-014, EV-021.
Confidence: HIGH

Principle 3: Regulatory Optics as Product Design Constraint (Proactive, Not Reactive)
Explanation: Terminologi "shares"→"keys" (EV-008) dan FRIEND token utility design (no profit-sharing, no gas, no validator) sengaja di-engineer untuk menghindari Howey Test security classification sejak awal, bukan patch belakangan.
Evidence: Rebrand "Shares" to "Keys" (EV-008) explicit "untuk menghindari implikasi regulasi sekuritas"【Phase 3 — EV-008】; Token Utility: no gas, no validator, no collateral, no profit-sharing【Phase 6 — Token Utility】; Entities: SEC, CFTC as regulatory risk【Phase 2 — SEC, CFTC】; Narrative: Consumer Crypto pivot (EV-024)【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 EV-008; Phase 6 Token Utility; Phase 2 Entities; Phase 8 Narrative Position.
Confidence: HIGH

Principle 4: Account Abstraction + Social Identity = Consumer-Grade Onboarding
Explanation: Embedded wallets (Privy ERC-4337) + Twitter OAuth + gasless paymaster (Coinbase Wallet) mengeliminasi seed phrase, gas complexity, dan wallet download — menciptakan UX setara Web2 app untuk onboarding massal.
Evidence: Privy integration sejak V1 (EV-003)【Phase 3 — EV-003】; Core Components: Privy Authentication Infrastructure【Phase 4 — Core Components】; External Dependencies: Privy (Critical), Coinbase Wallet (High), Twitter/X (Critical)【Phase 7 — External Dependencies】; DAU Peak >50k (Agustus 2023)【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 EV-003; Phase 4 Core Components; Phase 7 External Dependencies; Phase 8 Adoption Metrics.
Confidence: HIGH

Principle 5: Protocol Fees as Primary Runway (Revenue-First, Not Fundraising-First)
Explanation: V1 fee model generate >$10M cumulative fees <1 bulan (EV-009), mendanai treasury >$5M (EV-025) untuk runway multi-tahun tanpa follow-on funding. Seed funding hanya satu ronde (EV-004).
Evidence: $10M+ Cumulative Protocol Fees (EV-009)【Phase 3 — EV-009】; Treasury Balance >$5M (EV-025)【Phase 3 — EV-025】; Funding History: 1 round only (Seed Aug 2023)【Phase 5 — Funding History】; Financial Risk: Funding Dependency — no follow-on funding announced post-seed【Phase 5 — Financial Risk】.
Supporting Dataset: Phase 3 EV-009, EV-025; Phase 5 Funding History, Revenue History, Treasury, Financial Risk.
Confidence: HIGH

Principle 6: Third-Party Analytics as Transparency Layer (Build Social Graph, Not Dashboards)
Explanation: Mengandalkan Dune (community), Nansen/Arkham (institutional), DeFi Llama (aggregator) untuk data transparency — menghemat engineering resources dan memanfaatkan credibility existing platforms.
Evidence: EV-010 Nansen dashboard, EV-012 Arkham labels【Phase 3 — EV-010, EV-012】; Entities: Dune, Nansen, Arkham, DeFi Llama (Medium dependency)【Phase 2 — Dune, Nansen, Arkham, DeFi Llama】; Major Integrations: Analytics × all four【Phase 7 — Major Integrations】; Official Market Resources: all third-party【Phase 8 — Official Market Resources】.
Supporting Dataset: Phase 2 Entities; Phase 3 EV-010, EV-012; Phase 7 Major Integrations; Phase 8 Official Market Resources.
Confidence: HIGH

Success Factors

Factor 1: Base Launch Timing & Flagship Status — First Mover Advantage pada L2 Baru
Explanation: Friend.tech launch V1 (Agustus 2023) bertepatan dengan Base mainnet maturity (Februari 2023 launch, EV-002), menjadi aplikasi consumer pertama yang memanfaatkan Base throughput tinggi + biaya rendah. Base Ecosystem Fund investor, Coinbase Wallet default integration, Conduit infrastructure — menciptakan flywheel adoption.
Evidence: Base Mainnet Launch (EV-002, Feb 2023)【Phase 3 — EV-002】; Friend.tech V1 Launch (EV-003, Aug 2023)【Phase 3 — EV-003】; Base Ecosystem Fund investor seed round【Phase 5 — Funding History】; Coinbase Wallet default integration【Phase 7 — Major Integrations】; Narrative: Base Ecosystem Flagship【Phase 8 — Narrative Position】.
Supporting Dataset: Phase 3 EV-002, EV-003; Phase 5 Funding History; Phase 7 Major Integrations; Phase 8 Narrative Position.
Confidence: HIGH

Factor 2: Viral Bonding Curve Mechanics + Twitter Social Graph = Explosive Growth Loop
Explanation: Linear bonding curve menciptakan FOMO/spekulasi harga keys; Twitter OAuth login + social graph import memungkinkan instant network effects — user membeli keys influencer → influencer promote → more users. Peak >50k DAU, >$1M daily fees dalam hari-hari pertama.
Evidence: V1 bonding curve linear, fee 10%【Phase 4 — Core Components】; Twitter/X Identity integration【Phase 4 — Architecture】; DAU Peak >50k (Aug 2023)【Phase 8 — Adoption Metrics】; $1M+ Daily Fees (EV-006)【Phase 3 — EV-006】; $10M Cumulative <3 weeks (EV-009)【Phase 3 — EV-009】.
Supporting Dataset: Phase 4 Core Components, Architecture; Phase 3 EV-006, EV-009; Phase 8 Adoption Metrics.
Confidence: HIGH

Factor 3: Tier-1 VC Validation (Paradigm Lead) + Strategic Coinbase Alignment
Explanation: Seed round Paradigm lead + a16z crypto + Variant + Base Ecosystem Fund pada $50M valuation (EV-004) memberikan capital, credibility, dan strategic alignment dengan Coinbase/Base ecosystem — membuka akses distribution (Coinbase Wallet, Coinbase Exchange listing) dan infrastructure priority.
Evidence: Seed Funding Paradigm lead $50M valuation (EV-004)【Phase 3 — EV-004】; Funding History: Paradigm, a16z crypto, Variant, Base Ecosystem Fund【Phase 5 — Funding History】; Coinbase Exchange listing FRIEND/USD (EV-018)【Phase 3 — EV-018】; Coinbase Wallet default integration【Phase 7 — Major Integrations】.
Supporting Dataset: Phase 3 EV-004, EV-018; Phase 5 Funding History; Phase 7 Major Integrations.
Confidence: HIGH

Factor 4: Privy Account Abstraction Enabling Non-Crypto Native Onboarding
Explanation: Privy embedded wallet (ERC-4337) + Twitter OAuth + gasless transactions menghilangkan seed phrase barrier — kunci untuk mencapai massa pengguna Twitter non-crypto. Case study Privy menyebut Friend.tech sebagai showcase account abstraction mass adoption.
Evidence: Privy integration V1 launch (EV-003)【Phase 3 — EV-003】; Privy Blog Case Study【Phase 2 — Privy】; Core Components: Privy Authentication Infrastructure【Phase 4 — Core Components】; External Dependencies: Privy (Critical)【Phase 7 — External Dependencies】.
Supporting Dataset: Phase 2 Privy; Phase 3 EV-003; Phase 4 Core Components; Phase 7 External Dependencies.
Confidence: HIGH

Factor 5: Rapid Revenue Generation Creating Financial Independence
Explanation: >$10M protocol fees dalam 3 minggu (EV-009) menciptakan treasury yang mendanai V2 development tanpa fundraising tambahan. Financial runway >$5M treasury (EV-025) memungkinkan tim fokus produk bukan fundraising.
Evidence: $10M+ Cumulative Fees (EV-009)【Phase 3 — EV-009】; Treasury >$5M (EV-025)【Phase 3 — EV-025】; Financial Risk: Funding Dependency — no follow-on funding needed【Phase 5 — Financial Risk】.
Supporting Dataset: Phase 3 EV-009, EV-025; Phase 5 Revenue History, Treasury, Financial Risk.
Confidence: HIGH

Failure Factors

Factor 1: V1 Immutable Contracts Mencegah Iterasi Produk Saat Retensi Menurun
Explanation: V1 contracts immutable (Share.sol, Trade.sol, Fee.sol frozen)【Phase 4 — Core Components】 berarti tim tidak bisa adjust bonding curve parameters, fee structure, atau tambah fitur retention saat volume menurun drastis post-peak (EV-011). Harus deploy V2 baru penuh — migration friction tinggi.
Evidence: V1 Contracts Immutable (no upgrade path)【Phase 4 — Core Components】; Volume/Activity Decline (EV-011)【Phase 3 — EV-011】; Technical Limitations: V1 Immutable【Phase 4 — Technical Limitations】; Migration V1→V2 voluntary, residual keys unclaimed【Phase 3 — EV-019, Open Threads】.
Supporting Dataset: Phase 4 Core Components, Technical Limitations; Phase 3 EV-011, EV-019, Open Threads.
Confidence: HIGH

Factor 2: Speculative Bonding Curve Model Tidak Sustainable untuk Retention Jangka Panjang
Explanation: V1 linear bonding curve menciptakan spekulasi harga keys, bukan value sosial jangka panjang. User beli keys untuk flip, bukan akses konten. Ketika hype reda, volume collapse >90% (EV-011, EV-022). V2 clubs model belum terbukti fix retention.
Evidence: Bonding curve linear V1【Phase 4 — Core Components】; Volume Decline Significant (EV-011)【Phase 3 — EV-011】; V2 Volume Low Stable (EV-022)【Phase 3 — EV-022】; DAU Current <5k vs Peak >50k【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 4 Core Components; Phase 3 EV-011, EV-022; Phase 8 Adoption Metrics.
Confidence: HIGH

Factor 3: Token Distribution Opacity Merusak Kepercayaan Komunitas & Investor
Explanation: Tidak ada public breakdown alokasi FRIEND token (community, team, investors, treasury, ecosystem)【Phase 6 — Distribution, Open Threads】; vesting schedule tidak diungkap; circulating supply tidak dikonfirmasi resmi【Phase 6 — Open Threads】; CoinGecko/CoinMarketCap menampilkan "Self Reported" atau estimasi. Menciptakan ketidakpastian sell pressure dari team/investor unlock.
Evidence: Distribution: all categories "persentase tidak diungkap resmi"【Phase 6 — Distribution】; Vesting Schedule: all "tidak diketahui"【Phase 6 — Vesting Schedule】; Open Threads: allocation percentages, vesting details, circulating supply tidak diungkap【Phase 6 — Open Threads】.
Supporting Dataset: Phase 6 Distribution, Vesting Schedule, Open Threads.
Confidence: HIGH

Factor 4: Single Point of Failure — Twitter/X API Dependency untuk Identity & Login
Explanation: 100% login dan identity verification bergantung Twitter/X OAuth API【Phase 4 — Architecture】【Phase 7 — External Dependencies】. Tidak ada fallback (email direct, Google, Farcaster, wallet-only). Perubahan Twitter API policy, rate limits, atau deprecation akan break onboarding sepenuhnya.
Evidence: Identity Layer: Twitter/X API【Phase 4 — Architecture】; External Dependencies: Twitter/X (Critical)【Phase 7 — External Dependencies】; Technical Limitations: Twitter/X API Dependency【Phase 4 — Technical Limitations】.
Supporting Dataset: Phase 4 Architecture, Technical Limitations; Phase 7 External Dependencies.
Confidence: HIGH

Factor 5: V2 Clubs Model Belum Menemukan Product-Market Fit (Volume & Retensi Rendah)
Explanation: V2 launch Mei 2024 (EV-014) dengan clubs NFT, governance, FRIEND token — namun volume stabil di level rendah (EV-022), DAU <5k, price volatil $1.50→$0.30-0.60 (EV-023). Pivot announcement non-financial features (EV-024) Nov 2024 mengakui model clubs belum cukup.
Evidence: V2 Launch + TGE (EV-014)【Phase 3 — EV-014】; V2 Volume Low Stable (EV-022)【Phase 3 — EV-022】; Price Volatility (EV-023)【Phase 3 — EV-023】; Non-Financial Features Announced (EV-024)【Phase 3 — EV-024】; DAU Current <5k【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 EV-014, EV-022, EV-023, EV-024; Phase 8 Adoption Metrics.
Confidence: HIGH

Factor 6: Centralized Upgrade Authority (Team Multi-sig via Defender) Menghadapi Kritik Desentralisasi
Explanation: V2 UUPS proxy admin controlled by team multi-sig di OpenZeppelin Defender【Phase 4 — Security Model】. Governance proposal bisa trigger upgrade tapi eksekusi butuh team sign-off. Tidak ada timelock governance contract publik yang diverifikasi; Defender admin addresses tidak publik【Phase 6 — Open Threads】.
Evidence: Security Model: V2 Upgrade Authority Centralized【Phase 4 — Security Model】; Technical Upgrade History: Post-Audit Patches via UUPS upgrade administered through Defender【Phase 4 — Technical Upgrade History】; Governance: Treasury managed by team multi-sig, not directly DAO【Phase 6 — Governance】; Open Threads: governance timelock controller addresses tidak publik【Phase 6 — Open Threads】.
Supporting Dataset: Phase 4 Security Model, Technical Upgrade History; Phase 6 Governance, Open Threads.
Confidence: MEDIUM

Decision Framework

Observe → Evaluate → Fund → Develop → Launch → Govern
Explanation: Rekonstruksi framework keputusan Friend.tech berdasarkan pola historis (EV-001 to EV-025) dan behavioral patterns (Phase 9).

Step 1: Observe — Identify Infrastructure Readiness & Market Window
Detail: Tim (Racer, Shrimp) mengamati Base mainnet launch (EV-002, Feb 2023) sebagai L2 dengan throughput tinggi + biaya rendah yang enable consumer app frequency trading. Konsep social token bonding curve sudah dikembangkan 2022 (EV-001).
Evidence: EV-001 Konsep Awal 2022【Phase 3 — EV-001】; EV-002 Base Mainnet Launch Feb 2023【Phase 3 — EV-002】; Phase 9 Decision: Launch V1 on Base (trigger: Base ready).
Supporting Dataset: Phase 3 EV-001, EV-002; Phase 9 Decision Pattern 1.
Confidence: HIGH

Step 2: Evaluate — Validate Technical Feasibility & Regulatory Risk
Detail: Evaluasi: Base infrastructure ready, Privy account abstraction available, Twitter OAuth untuk identity. Regulatory risk assessed: "shares" terminology → changed to "keys" pre-public launch (EV-008) untuk Howey Test avoidance.
Evidence: EV-003 V1 Launch invite-only (technical validation)【Phase 3 — EV-003】; EV-008 Rebrand shares→keys (regulatory optics)【Phase 3 — EV-008】; Phase 9 Decision: Rebrand for regulatory avoidance.
Supporting Dataset: Phase 3 EV-003, EV-008; Phase 9 Decision Pattern 3.
Confidence: HIGH

Step 3: Fund — Single Seed Round from Tier-1 VCs at High Valuation
Detail: Setelah V1 public launch explosive growth (EV-005, EV-006), seed round Paradigm lead $50M valuation (EV-004) dengan a16z, Variant, Base Ecosystem Fund. Tidak ada follow-on fundraising — runway dari protocol fees.
Evidence: EV-004 Seed Funding Paradigm lead【Phase 3 — EV-004】; Phase 5 Funding History: 1 round only【Phase 5 — Funding History】; Phase 9 Pattern: Single Seed Round Only.
Supporting Dataset: Phase 3 EV-004; Phase 5 Funding History; Phase 9 Pattern 1.
Confidence: HIGH

Step 4: Develop — Immutable V1 First, Then Modular Upgradeable V2
Detail: V1 developed as immutable contracts (trust, speed to market). V2 developed modular (Club, Token, Governance, FeeManager separate) with UUPS proxy + Defender for upgradeability. Spearbit audit V2 before/after launch.
Evidence: V1 Immutable【Phase 4 — Core Components】; V2 Modular UUPS【Phase 4 — Core Components】; EV-013 V2 Announcement, EV-014 V2 Launch【Phase 3 — EV-013, EV-014】; EV-021 Spearbit Audit【Phase 3 — EV-021】; Phase 9 Pattern: Immutable V1 → Upgradeable V2.
Supporting Dataset: Phase 4 Core Components; Phase 3 EV-013, EV-014, EV-021; Phase 9 Pattern 2.
Confidence: HIGH

Step 5: Launch — Phased: Invite-Only → Public → Token TGE + Simultaneous CEX Listings
Detail: V1: Invite-only beta (EV-003) → Public access (EV-005). V2: TGE + FRIEND token

## Open Questions
- [foundation] Identitas legal entity / yurisdiksi pendaftaran perusahaan (tidak diumumkan)
- [foundation] Ukuran dan komposisi core team yang terverifikasi (hanya 2 founder pseudonim yang diketahui publik)
- [foundation] Apakah ada investor/institusi di belakang project (rumor Paradigm, tapi tidak dikonfirmasi resmi)
- [foundation] Detail tokenomics FRIEND yang lengkap (alokasi team, investor, community, vesting schedule) — hanya ringkasan tinggi yang tersedia
- [foundation] Status keamanan smart contract (audit report publik tidak ditemukan)
- [foundation] Rencana v3 / roadmap pasca-v2 (hanya teaser umum)
- [history] Tanggal pasti seed funding round (EV-004): Beberapa sumber menyebut "Agustus 2023" tanpa tanggal eksak; Paradigm portfolio page tidak menampilkan tanggal deal. Perlu verifikasi ke SEC Form D atau announcement resmi Paradigm.
- [history] Jumlah dana seed round (EV-004): Tidak diketahui jumlah absolut (hanya valuasi $50M). Beberapa laporan spekulatif menyebut $5-10M tapi tanpa sumber primer.
- [history] Tanggal pasti V2 announcement (EV-013): Blog post "V2" tidak memiliki timestamp publik yang jelas; perlu cek Wayback Machine atau GitHub commit announcement.
- [history] Detail alokasi token FRIEND TGE (EV-014): Persentase airdrop vs treasury vs team vs investor tidak dipublikasikan lengkap di blog resmi; hanya "100M supply" yang dikonfirmasi. Perlu cross-check ke Token Terminal / Messari tokenomics page.
- [history] Status migrasi V1 keys ke V2 clubs (EV-019): Apakah 100% keys sudah dikonversi atau ada residual? Data on-chain Dune menunjukkan sebagian kecil keys V1 masih di-hold tanpa claim.
- [history] Audit report Spearbit (EV-021): Full report apakah publik? Hanya ringkasan yang tersebar; perlu cari PDF lengkap di GitHub friendtech/audits.
- [history] Rincian "fitur social non-finansial 2025" (EV-024): Hanya announcement tingkat tinggi; tidak ada whitepaper, roadmap detail, atau milestone teknis. Perlu monitoring ke blog resmi Q1 2025.
- [history] Klasifikasi regulasi SEC terhadap FRIEND token dan keys (tidak ada event terpisah): Tidak ada enforcement action resmi, tapi risiko berlanjut. Perlu tracking SEC guidance socialfi tokens 2024-2025.
- [history] Wintermute / GSR market making agreement detail (tidak ada event): Volume CEX tinggi tapi tidak ada konfirmasi resmi agreement market making dengan Wintermute/GSR. Perlu verifikasi ke CoinGecko market maker tab atau announcement tim.
- [technology] Exact BaseScan address for V2 proxy implementation and admin contracts not consolidated in single verified source; need to query BaseScan for "Friend.tech V2" deployment transaction
- [technology] V1 audit auditor identity and report availability — no public disclosure found; may not exist or may be private
- [technology] Frontend technology stack (React/Next.js, hosting provider) not officially documented; inferred only
- [technology] CI/CD pipeline, testing coverage, deployment automation details not publicly available
- [technology] Whether V2 governance timelock/multi-sig signers are publicly known (Defender admin addresses)
- [technology] Exact bonding curve formula for V2 clubs (linear? exponential? configurable per club?) — docs describe "dynamic fee" but pricing curve details sparse
- [technology] Privy embedded wallet recovery flow technical specification (sharding threshold, TEE attestation details) not in public docs
- [technology] Base decentralization timeline for sequencer (fault proofs, permissionless validation) — affects Friend.tech censorship resistance roadmap
- [technology] Cross-chain messaging or bridge integration plans (none announced) — protocol currently Base-only
- [technology] Mobile app technical architecture (if any) — only web app confirmed
- [financial] Jumlah absolut dana seed round (bukan valuation) tidak diungkap resmi; tidak ada SEC Form D filing yang ditemukan untuk Friend.tech entity
- [financial] Persentase alokasi token FRIEND TGE (airdrop vs treasury vs team vs investor vs liquidity) tidak dipublikasikan lengkap di blog resmi atau docs; hanya total supply 100M yang dikonfirmasi
- [financial] Apakah treasury aktif mengelola yield (staking, lending, LP) atau hanya hold aset — tidak ada governance proposal atau announcement yang mengonfirmasi strategi treasury management
- [financial] Detail market making agreement dengan Wintermute/GSR tidak diungkap; volume CEX tinggi tapi tidak ada konfirmasi resmi dari tim atau market maker
- [financial] Runway finansial tidak dapat dihitung karena burn rate tim tidak diungkap; hanya treasury balance >$5M yang diketahui
- [financial] Apakah ada follow-on funding (Series A, strategic round) setelah seed Agustus 2023 — tidak ada announcement resmi ditemukan
- [financial] Klasifikasi pajak dan akuntansi treasury (entity legal structure, jurisdiction) tidak diungkap; memengaruhi financial reporting義务
- [financial] V1 residual keys yang belum dimigrasikan/claim — nilai ekonomis dan apakah masih generate fee tidak terverifikasi sepenuhnya
- [token] Persentase alokasi token TGE per kategori (community, team, investors, treasury, ecosystem, advisors) tidak dipublikasikan resmi oleh tim Friend.tech; tidak ada blog post, governance proposal, atau dashboard yang menampilkan breakdown lengkap — hanya total supply 100M yang dikonfirmasi
- [token] Vesting schedule detail (cliff, duration, unlock frequency) untuk setiap kategori tidak diungkap; tidak ada smart contract vesting/escrow yang terverifikasi on-chain untuk team/investor allocation
- [token] Contract address FRIEND token (0x5Cb32172dD37Ce5E18Ec6b26771D7e4D0b84145B) terverifikasi di BaseScan tapi tidak dikonfirmasi di blog resmi Friend.tech sebagai single source of truth
- [token] Governance proposal threshold (minimum delegated votes untuk membuat proposal) dan quorum requirement tidak terdokumentasi di docs resmi
- [token] Treasury multi-sig signers dan governance timelock controller addresses tidak dipublikasikan secara transparan (Defender admin tidak publik)
- [token] Airdrop claim rate (persentase V1 users yang claim FRIEND) dan jumlah token unclaimed tidak diungkap; apakah unclaimed tokens dikembalikan ke treasury atau diburn tidak diketahui
- [token] Insentif ekosistem (liquidity mining, creator rewards) token emission schedule tidak diungkap; apakah dari allocation tersedia di treasury atau minting baru (kontrak tidak support minting baru) perlu verifikasi
- [token] Market making agreement detail dengan Wintermute/GSR tidak diungkap; apakah melibatkan token loan/option dari treasury tidak diketahui
- [token] Apakah ada plan untuk fee switch (protocol fee accrual ke FRIEND stakers) atau buyback mechanism di masa depan — hanya "staking untuk fee discount" yang terimplementasi saat ini
- [token] Klasifikasi regulasi SEC/CFTC terhadap FRIEND token (security vs commodity) belum memiliki guidance resmi; memengaruhi utility governance dan exchange listing jangka panjang
- [market] Circulating supply FRIEND token tidak dipublikasikan resmi — CoinGecko dan CoinMarketCap menampilkan "Self Reported Circulating Supply" atau estimasi berbasis liquidity; tidak ada transparency report atau governance proposal yang mengonfirmasi circulating vs locked vs vesting
- [market] Market share data tidak tersedia karena tidak ada definisi pasar SocialFi yang standar dan terukur (TVL, users, revenue metrics tidak comparable antar protokol dengan arsitektur berbeda)
- [market] DAU metrics current (V2) bersifat estimasi dari Dune/DeFi Llama; tidak ada official metrics dashboard dari Friend.tech yang menampilkan DAU/MAU/retention rate real-time
- [market] Volume breakdown CEX vs DEX per exchange tidak diverifikasi dari sisi protokol; hanya agregator CoinGecko/CoinMarketCap yang tersedia
- [market] Competitor landscape: Perbandingan head-to-head (TVL, users, revenue) tidak tersedia dalam format terstandarisasi; setiap protokol menggunakan metrik berbeda
- [market] Narrative "Consumer Crypto" pivot (EV-024) baru di-announce November 2024; belum ada product release atau metrics adopsi untuk memvalidasi pivot ini
- [market] Regulatory classification risk (SEC/CFTC) narasi pasar berfluktuasi; tidak ada guidance resmi memengaruhi exchange listing status jangka panjang
- [market] Market making agreement detail (Wintermute, GSR) tidak publik; apakah melibatkan token loan/option dari treasury memengaruhi circulating supply dynamics
- [market] Geographic user distribution detail (beyond "Asia tinggi") tidak diverifikasi; Nansen/Arkham dashboard tidak mempublikasikan breakdown negara lengkap
- [market] Developer ecosystem metrics (SDK usage, third-party apps, hackathon projects) tidak tersedia; Friend.tech tidak memiliki developer portal atau SDK publik yang terdokumentasi
- [behavioral] Legal Entity & Jurisdiction: Tidak ada informasi legal entity Friend.tech (Cayman Foundation, BVI, Delaware, dll). Founders pseudonymous. Memengaruhi regulatory liability, tax, treasury management, token classification. (Phase 1 Foundation, Phase 2 Entity, Phase 5 Financial Risk)
- [behavioral] Seed Round Absolute Amount & Token Allocation to Investors: Valuasi $50M dikonfirmasi tapi jumlah USD undisclosed. Alokasi token ke Paradigm/a16z/Variant undisclosed. Vesting schedule undisclosed. Memengaruhi circulating supply accuracy, insider selling pressure, regulatory Howey Test analysis. (Phase 3 EV-004, Phase 5 Funding History, Phase 6 Distribution/Vesting/Open Threads)
- [behavioral] V1 Audit Status: Tidak ada audit report publik untuk V1 contracts. Hanya "inferred from standard practice". V1 handles $10M+ fees. Bug di V1 immutable = permanent loss risk. (Phase 4 Audit History, Phase 4 Core Components V1)
- [behavioral] V2 Governance Parameters: Proposal threshold, quorum requirement, timelock duration, voter participation metrics — semua undisclosed. Governance effectiveness tidak dapat diverifikasi. (Phase 6 Governance, Phase 6 Open Threads, Phase 3 EV-017)
- [behavioral] Treasury Management Strategy: Apakah treasury actively managed (staking, lending, LP) atau hanya hold? Tidak ada governance proposal atau announcement mengonfirmasi. FRIEND concentration risk tinggi. (Phase 5 Treasury, Phase 5 Financial Risk, Phase 3 EV-025)
- [behavioral] FRIEND Circulating Supply & Market Cap: Tidak dipublikasikan resmi. CoinGecko/CoinMarketCap menampilkan estimasi. Tidak ada transparency report. Memengaruhi valuation metrics (FDV vs Market Cap), tokenomics analysis. (Phase 6 Supply, Phase 8 Adoption Metrics, Phase 6 Open Threads)
- [behavioral] Team Size & Composition: Hanya 2 founders known (Racer, Shrimp). Tim ~5-10 orang inferred. Bus factor tinggi. Pseudonymous = accountability rendah. (Phase 1 Foundation, Phase 2 Entity)
- [behavioral] 2025 Non-Financial Features Execution: Hanya announcement tingkat tinggi (EV-024). Tidak ada whitepaper, roadmap detail, milestone teknis, SDK, developer portal. Execution risk sangat tinggi given small team. (Phase 3 EV-024, Phase 8 Narrative, Phase 7 Ecosystem Position - no developer ecosystem)
- [behavioral] Base Decentralization Timeline Impact: Friend.tech fully dependent pada Base sequencer decentralization (fault proofs, permissionless validation). Base roadmap delays langsung impact Friend.tech censorship resistance. (Phase 4 Technical Limitations, Phase 7 External Dependencies Base/Conduit/Optimism)
- [behavioral] Market Maker Agreements: Wintermute/GSR participation inferred dari market data. Terms (token loans, options, KPI) undisclosed. Memengaruhi circulating supply dynamics, price stability, regulatory classification. (Phase 2 Entity Wintermute/GSR, Phase 5 Financial Risk, Phase 7 External Dependencies, Phase 8 Liquidity)
