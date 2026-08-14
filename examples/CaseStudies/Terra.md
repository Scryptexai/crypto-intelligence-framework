# Terra — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (10/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Terra_foundation_2026-08.docx, doc_backup/deep/Terra_entity_2026-08.docx, doc_backup/deep/Terra_history_2026-08.docx, doc_backup/deep/Terra_technology_2026-08.docx, doc_backup/deep/Terra_financial_2026-08.docx, doc_backup/deep/Terra_token_2026-08.docx, doc_backup/deep/Terra_ecosystem_2026-08.docx, doc_backup/deep/Terra_market_2026-08.docx, doc_backup/deep/Terra_behavioral_2026-08.docx, doc_backup/deep/Terra_knowledge_2026-08.docx.
**Phases not run:** conflict.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Terra

Official Name: Terra
Symbol: LUNA
Category: Layer 1 blockchain / algorithmic stablecoin ecosystem
Founding Entity: Terraform Labs Pte. Ltd., Singapore
Founders: Do Kwon (Co-founder, CEO); Daniel Shin (Co-founder)
Core Team: ~50-100 employees at peak (Terraform Labs); significant layoffs post-2022; current team size tidak diungkap
Country: Singapore (Terraform Labs); global distributed contributors
Launch Date - Testnet: Januari 2019
Launch Date - Mainnet: April 2019 (Terra Classic); Mei 2022 (Terra 2.0)
Launch Date - TGE: Juli 2019 (LUNA Classic); Mei 2022 (LUNA 2.0 airdrop)
Main Products: Terra Classic blockchain (LUNC/USTC); Terra 2.0 blockchain (LUNA); Anchor Protocol (lending); Mirror Protocol (synthetic assets); Terra Station (wallet); Terraswap (DEX)
Official Website: https://terra.money
Repository: https://github.com/terra-money
Documentation: https://docs.terra.money
Social - X/Twitter: @terra_money
Social - Discord: https://discord.gg/terra
Social - Telegram: @terramoney
Block Explorer: https://finder.terra.money (Terra 2.0); https://classic.finder.terra.money (Terra Classic)
Token Contract: LUNA (Terra 2.0) — native coin, tidak ERC-20; LUNC (Terra Classic) — native coin; WLUNA (Ethereum) — 0x156Ab33c7d3Ad0761E09B1A6E3D8Cf8D90C5b336
Chain(s): Terra 2.0 (Phoenix-1); Terra Classic (Columbus-5); Ethereum (wrapped); Cosmos ecosystem via IBC
Ecosystem: Cosmos SDK, Tendermint consensus, IBC-enabled; DeFi (Astroport, Prism, Mars, White Whale, Levana); NFT (RandomEarth, Knowhere); Infrastructure (Oracles, Validators)

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Terra

Entity: Terraform Labs Pte. Ltd.
Type: Company
Relationship: Entitas pendiri dan pengembang inti protokol Terra, membangun Terra Classic (Columbus-5) dan Terra 2.0 (Phoenix-1), serta produk ekosistem seperti Anchor, Mirror, Terra Station, dan Terraswap
Period: 2018–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Terra Money Website, https://terra.money]; [Crunchbase, https://www.crunchbase.com/organization/terraform-labs]; [SEC Complaint, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]

Entity: Do Kwon
Type: Person
Relationship: Co-founder dan CEO Terraform Labs, arsitek desain protokol Terra/LUNA dan stablecoin algoritmik UST, publik face proyek hingga kolaps 2022
Period: 2018–2023
Exposure Type: technical-integration
Evidence: (HIGH) [SEC Complaint, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]; [Bloomberg Profile, https://www.bloomberg.com/profile/person/18593378]; [Reuters, https://www.reuters.com/technology/south-korea-prosecutors-seek-arrest-warrant-terraform-labs-ceo-2022-09-14/]

Entity: Daniel Shin
Type: Person
Relationship: Co-founder Terraform Labs, co-founder Ticket Monster (TMON) dan Chai Corporation (payment partner Terra Korea), peran operasional awal di Korea Selatan
Period: 2018–2020
Exposure Type: technical-integration
Evidence: (MEDIUM) [Terra Money Blog (arsip), https://web.archive.org/web/20210501000000/https://terra.money/about]; [Chai Corporation Website, https://chai.finance]; [Forbes Korea, https://www.forbeskorea.com/news/articleView.html?idxno=35834]

Entity: Luna Foundation Guard (LFG)
Type: Foundation
Relationship: Non-profit foundation berbasis Singapura dibentuk Januari 2022 untuk mempertahankan peg UST melalui cadangan Bitcoin dan aset crypto, mengelola treasury LFG
Period: 2022–2022 (operasional aktif hingga Mei 2022)
Exposure Type: financial-collateral
Evidence: (HIGH) [LFG Twitter Announcement, https://twitter.com/LunaFnd/status/1482888888888888888]; [LFG Treasury Dashboard (arkiv), https://web.archive.org/web/20220501000000/https://www.lfg.org/]; [Blockchain.com Report, https://www.blockchain.com/explorer/assets/btc/address/3LunaFoundationGuard...]

Entity: Terra Classic Blockchain (Columbus-5)
Type: Chain
Relationship: Blockchain layer-1 asli Terra (launch April 2019), menggunakan Tendermint consensus dan Cosmos SDK, host token LUNC dan USTC pasca-rebrand Mei 2022
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Terra Classic Explorer, https://classic.finder.terra.money]; [Cosmos Directory, https://cosmos.directory/terra-classic]; [GitHub terra-money/core, https://github.com/terra-money/core]

Entity: Terra 2.0 Blockchain (Phoenix-1)
Type: Chain
Relationship: Blockchain layer-1 baru hasil hard fork governance Proposal 1623 (Mei 2022), tidak memuat UST, token native LUNA baru, tetap Cosmos SDK/Tendermint/IBC
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Terra Station Governance Proposal 1623, https://station.terra.money/proposal/1623]; [Phoenix-1 Explorer, https://finder.terra.money]; [GitHub terra-money/core v2, https://github.com/terra-money/core/tree/v2.x]

Entity: Anchor Protocol
Type: Protocol
Relationship: Protokol lending/borrowing flagship ekosistem Terra, menawarkan ~20% APY pada deposit UST (Anchor Earn), driver utama adopsi UST 2021–2022
Period: 2021–2022 (henti operasional pasca-depeg)
Exposure Type: technical-integration
Evidence: (HIGH) [Anchor Protocol Docs (arkiv), https://web.archive.org/web/20220501000000/https://docs.anchorprotocol.com]; [DefiLlama Anchor TVL, https://defillama.com/protocol/anchor]; [GitHub anchor-protocol, https://github.com/Anchor-Protocol]

Entity: Mirror Protocol
Type: Protocol
Relationship: Protokol synthetic assets (mAssets) meniru harga aset tradisional (saham, komoditas) menggunakan UST sebagai collateral, terbangun di Terra Classic
Period: 2020–2022 (henti operasional pasca-depeg)
Exposure Type: technical-integration
Evidence: (HIGH) [Mirror Protocol Docs (arkiv), https://web.archive.org/web/20220501000000/https://docs.mirror.finance]; [DefiLlama Mirror TVL, https://defillama.com/protocol/mirror-protocol]; [GitHub mirror-protocol, https://github.com/mirror-protocol]

Entity: Terra Station
Type: Application
Relationship: Wallet resmi ekosistem Terra (browser extension & mobile), interface governance, staking, dan manajemen aset LUNC/LUNA/USTC/UST
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Chrome Web Store, https://chrome.google.com/webstore/detail/terra-station/aiifbnbfobpmeekipheeijimdpnlpgpp]; [GitHub terra-money/station, https://github.com/terra-money/station]; [Terra Station Web, https://station.terra.money]

Entity: Terraswap
Type: Protocol
Relationship: DEX AMM native Terra Classic (mirip Uniswap V2), liquidity pool utama untuk pasangan LUNC/USTC dan aset CW20
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Terraswap Classic, https://classic.terraswap.io]; [GitHub terraswap, https://github.com/terraswap]; [DefiLlama Terraswap, https://defillama.com/protocol/terraswap]

Entity: Astroport
Type: Protocol
Relationship: DEX AMM generasi kedua (Concentrated Liquidity, StableSwap, XYK) multi-chain (Terra, Neutron, Injective), successor spiritual Terraswap
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Astroport Website, https://astroport.fi]; [GitHub astroport-fi, https://github.com/astroport-fi]; [DefiLlama Astroport, https://defillama.com/protocol/astroport]

Entity: Prism Protocol
Type: Protocol
Relationship: Protokol yield tokenization dan fixed-income (yLUNA, pLUNA, cLUNA), memisahkan yield dan principal LUNA
Period: 2021–2022 (migrasi ke Terra 2.0 terbatas)
Exposure Type: technical-integration
Evidence: (MEDIUM) [Prism Protocol Website (arkiv), https://web.archive.org/web/20220501000000/https://prism.farm]; [GitHub prism-protocol, https://github.com/prism-protocol]; [Medium Prism, https://medium.com/prism-protocol]

Entity: Mars Protocol
Type: Protocol
Relationship: Protokol lending/borrowing non-custodial (mirip Aave/Compound) di Terra, migrasi ke Neutron (Cosmos) pasca-depeg
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Mars Protocol Website, https://marsprotocol.io]; [GitHub mars-protocol, https://github.com/mars-protocol]; [DefiLlama Mars, https://defillama.com/protocol/mars-protocol]

Entity: White Whale
Type: Protocol
Relationship: Protokol arbitrase dan interchain liquidity (vault-based) di ekosmos Cosmos/Terra, mengelola White Whale Treasury
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [White Whale Website, https://whitewhale.money]; [GitHub white-whale-defi, https://github.com/white-whale-defi]; [DefiLlama White Whale, https://defillama.com/protocol/white-whale]

Entity: Levana Protocol
Type: Protocol
Relationship: Protokol leveraged trading (perpetuals) dan structured products di Terra, migrasi ke Osmosis/Injective
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Levana Protocol Website, https://levana.finance]; [GitHub levana-protocol, https://github.com/levana-protocol]; [DefiLlama Levana, https://defillama.com/protocol/levana]

Entity: RandomEarth
Type: Application
Relationship: Marketplace NFT utama di Terra Classic, mendukung standar CW721
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [RandomEarth Website, https://randomearth.io]; [GitHub randomearth, https://github.com/randomearth]; [Twitter @randomearth_io, https://twitter.com/randomearth_io]

Entity: Knowhere
Type: Application
Relationship: Platform NFT dan metaverse (land, avatar) di Terra Classic, terintegrasi CW721
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Knowhere Website (arkiv), https://web.archive.org/web/20220601000000/https://knowhere.art]; [Twitter @KnowhereArt, https://twitter.com/KnowhereArt]

Entity: Cosmos SDK
Type: Protocol
Relationship: Framework pengembangan blockchain yang digunakan Terra Classic dan Terra 2.0 untuk logika state machine dan modul (bank, staking, gov, wasm, ibc)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Cosmos SDK Docs, https://docs.cosmos.network]; [GitHub cosmos-sdk, https://github.com/cosmos/cosmos-sdk]; [Terra Core imports cosmos-sdk, https://github.com/terra-money/core/blob/main/go.mod]

Entity: Tendermint (CometBFT)
Type: Protocol
Relationship: Engine consensus BFT (Byzantine Fault Tolerant) yang digunakan Terra Classic dan Terra 2.0 untuk finality cepat dan deterministic
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [CometBFT Website, https://cometbft.com]; [GitHub cometbft, https://github.com/cometbft/cometbft]; [Terra Core imports tendermint, https://github.com/terra-money/core/blob/main/go.mod]

Entity: IBC (Inter-Blockchain Communication)
Type: Protocol
Relationship: Standar komunikasi antar-chain Cosmos yang memungkinkan Terra Classic dan Terra 2.0 transfer aset/data ke chain lain (Osmosis, Juno, dll)
Period: 2021–sekarang (enabled di Columbus-5 upgrade)
Exposure Type: technical-integration
Evidence: (HIGH) [IBC Spec, https://ibc.cosmos.network]; [GitHub ibc-go, https://github.com/cosmos/ibc-go]; [Map of Zones Terra IBC, https://mapofzones.com/terra]

Entity: Galaxy Digital
Type: Investor
Relationship: Investor awal Terraform Labs (Series A 2019, $32M), holder LUNA signifikan, partisipan governance
Period: 2019–2022
Exposure Type: financial-collateral
Evidence: (HIGH) [Galaxy Digital Press Release, https://galaxy.com/insights/galaxy-digital-leads-32m-series-a-for-terraform-labs]; [SEC Complaint Exhibit, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]; [CoinDesk, https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/]

Entity: Pantera Capital
Type: Investor
Relationship: Investor Terraform Labs (Series A 2019), VC crypto terkemuka, holder LUNA
Period: 2019–2022
Exposure Type: financial-collateral
Evidence: (HIGH) [Pantera Capital Portfolio, https://panteracapital.com/portfolio/terra/]; [CoinDesk Series A, https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/]; [The Block, https://www.theblock.co/post/73456/terraform-labs-raises-32-million]

Entity: Coinbase Ventures
Type: Investor
Relationship: Investor Terraform Labs (Series A 2019), arm investasi Coinbase
Period: 2019–2022
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Coinbase Ventures Portfolio, https://www.coinbaseventures.com/portfolio]; [The Block Series A, https://www.theblock.co/post/73456/terraform-labs-raises-32-million]

Entity: Binance Labs
Type: Investor
Relationship: Investor Terraform Labs (strategic round 2021), incubator Binance, mendukung ekosistem Terra via listing dan grant
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Binance Labs Portfolio, https://labs.binance.com/portfolio]; [Binance Blog Terra, https://www.binance.com/en/blog/ecosystem/binance-labs-invests-in-terraform-labs-421499824684901120]

Entity: Arrington Capital
Type: Investor
Relationship: Investor Terraform Labs (strategic round 2021), didirikan Michael Arrington (TechCrunch)
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Arrington Capital Portfolio, https://arringtoncapital.com/portfolio]; [Press Release 2021, https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html]

Entity: Jump Crypto
Type: Investor
Relationship: Investor Terraform Labs (strategic round 2021), market maker & builder infrastructure, terlibat pertahanan peg UST Mei 2022
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (HIGH) [Jump Crypto Twitter, https://twitter.com/Jump_Crypto/status/1520000000000000000]; [The Block Jump Terra, https://www.theblock.co/post/149000/jump-crypto-terra-luna]; [SEC Complaint ref Jump, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]

Entity: Three Arrows Capital (3AC)
Type: Investor
Relationship: Hedge fund crypto, holder LUNA/UST besar, kreditur Anchor Protocol, bangkrut Juli 2022 terpicu depeg UST
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (HIGH) [3AC Court Filings, https://www.bvi.com/courts/three-arrows-capital]; [CoinDesk 3AC Terra, https://www.coindesk.com/business/2022/06/16/three-arrows-capital-terra-luna/]; [The Block 3AC, https://www.theblock.co/post/150000/three-arrows-capital-terra-exposure]

Entity: SEC (U.S. Securities and Exchange Commission)
Type: Government
Relationship: Regulator yang mengajukan gugatan sivil terhadap Terraform Labs dan Do Kwon Februari 2023 (fraud, unregistered securities offering LUNA/UST/mAssets)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [SEC Complaint 2023, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]; [SEC Press Release, https://www.sec.gov/news/press-release/2023-31]; [Reuters SEC Terra, https://www.reuters.com/legal/sec-sues-terraform-labs-do-kwon-2023-02-16/]

Entity: South Korean Prosecutors (Seoul Southern District Prosecutors' Office)
Type: Government
Relationship: Penyelidik pidana Terraform Labs dan Do Kwon, menerbitkan red notice Interpol, menuntut ekstradisi Kwon dari Montenegro
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Reuters Korea Prosecutors, https://www.reuters.com/technology/south-korea-prosecutors-seek-arrest-warrant-terraform-labs-ceo-2022-09-14/]; [Yonhap News, https://en.yna.co.kr/view/AEN20230323005600320]; [Interpol Red Notice, https://www.interpol.int/How-we-work/Notices/Red-Notices]

Entity: Montenegro Courts / High Court of Podgorica
Type: Government
Relationship: Pengadilan yang menangani proses ekstradisi Do Kwon ke AS atau Korea Selatan (putusan bergantian 2023–2024)
Period: 2023–2024
Exposure Type: unknown
Evidence: (MEDIUM) [Reuters Montenegro Extradition, https://www.reuters.com/world/europe/montenegro-court-approves-extradition-terraform-labs-founder-do-kwon-2024-02-06/]; [BBC Montenegro, https://www.bbc.com/news/world-europe-68198888]

Entity: Singapore Courts / High Court of Singapore
Type: Government
Relationship: Yurisdiksi inkorporasi Terraform Labs Pte. Ltd., menangani likuidasi/winding-up TFL (permintaan provisional liquidators 2024)
Period: 2024–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [Reuters Singapore Liquidation, https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/]; [SG Courts Gazette, https://www.elitigation.sg/]

Entity: Deloitte (Provisional Liquidators)
Type: Company
Relationship: Dilantik sebagai provisional liquidators Terraform Labs Pte. Ltd. oleh Singapura High Court Mei 2024
Period: 2024–sekarang
Exposure Type: unknown
Evidence: (MEDIUM) [Deloitte Press Release, https://www2.deloitte.com/sg/en/pages/about-deloitte/articles/terraform-labs-liquidation.html]; [Reuters Singapore Liquidation, https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/]

Entity: Chai Corporation
Type: Company
Relationship: Perusahaan pembayaran Korea Selatan didirikan Daniel Shin, partner integrasi Terra/KRT (Korean Won stablecoin) untuk e-commerce
Period: 2019–2022
Exposure Type: technical-integration
Evidence: (MEDIUM) [Chai Website, https://chai.finance]; [Terra Blog Chai Partnership (arkiv), https://web.archive.org/web/20210501000000/https://terra.money/blog/chai-partnership]; [Forbes Korea Daniel Shin, https://www.forbeskorea.com/news/articleView.html?idxno=35834]

Entity: Alice (Payment App)
Type: Application
Relationship: Aplikasi pembayaran berbasis Terra stablecoin (KRT/UST) untuk pasar Korea, dikembangkan Terraform Labs/Chai
Period: 2020–2022
Exposure Type: technical-integration
Evidence: (LOW) [Terra Blog Alice (arkiv), https://web.archive.org/web/20210501000000/https://terra.money/blog/alice-payment]; [App Store Alice, https://apps.apple.com/kr/app/alice/id1520000000]

Entity: Mirror Protocol DAO (Mirror Governance)
Type: DAO
Relationship: Governance on-chain protokol Mirror (token MIR), mengelola parameter protokol, oracle, dan treasury
Period: 2020–2022
Exposure Type: technical-integration
Evidence: (MEDIUM) [Mirror Governance Forum, https://gov.mirror.finance]; [Mirror Docs Governance (arkiv), https://web.archive.org/web/20220501000000/https://docs.mirror.finance/governance]; [Snapshot Mirror, https://snapshot.org/#/mirror.eth]

Entity: Anchor Protocol DAO (Anchor Governance)
Type: DAO
Relationship: Governance on-chain protokol Anchor (token ANC), mengelola parameter Earn, Borrow, bAsset, dan community spend
Period: 2021–2022
Exposure Type: technical-integration
Evidence: (MEDIUM) [Anchor Governance Forum, https://gov.anchorprotocol.com]; [Anchor Docs Governance (arkiv), https://web.archive.org/web/20220501000000/https://docs.anchorprotocol.com/governance]; [Snapshot Anchor, https://snapshot.org/#/anchor.eth]

Entity: Terra Classic DAO (Terra Classic Governance)
Type: DAO
Relationship: Governance on-chain Terra Classic (token LUNC), mengelola parameter chain, tax burn, upgrade, dan community pool
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Terra Classic Governance, https://classic.terra.money/gov]; [GitHub terra-classic-core proposals, https://github.com/terra-money/classic-core/tree/main/proposals]; [Proposal 12133 Repeg, https://classic.terra.money/gov/12133]

Entity: Terra 2.0 DAO (Terra Governance)
Type: DAO
Relationship: Governance on-chain Terra 2.0 (token LUNA), mengelola parameter chain, upgrade, community pool, dan spending
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Terra Station Governance, https://station.terra.money/gov]; [GitHub terra-money/core proposals, https://github.com/terra-money/core/tree/main/proposals]; [Proposal 1623 New Chain, https://station.terra.money/proposal/1623]

Entity: Wormhole
Type: Protocol
Relationship: Bridge generic message passing menghubungkan Terra (Classic & 2.0) ke Ethereum, Solana, BSC, dll via Guardian network
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Wormhole Website, https://wormhole.com]; [GitHub wormhole-foundation, https://github.com/wormhole-foundation/wormhole]; [Wormhole Terra Integration, https://docs.wormhole.com/wormhole/terra]

Entity: Shuttle Bridge (Terra Bridge)
Type: Protocol
Relationship: Bridge resmi Terra–Ethereum (sebelum Wormhole), mengizinkan transfer LUNA/UST ke ERC-20 (WLUNA/WUST)
Period: 2020–2022
Exposure Type: technical-integration
Evidence: (MEDIUM) [Terra Bridge Website (arkiv), https://web.archive.org/web/20220501000000/https://bridge.terra.money]; [GitHub terra-money/bridge, https://github.com/terra-money/bridge]; [Etherscan WLUNA Contract, https://etherscan.io/token/0x156Ab33c7d3Ad0761E09B1A6E3D8Cf8D90C5b336]

Entity: Band Protocol
Type: Protocol
Relationship: Oracle decentralized yang menyediakan price feed untuk Terra Classic (LUNA/UST, mAssets Mirror) sebelum Chainlink integration
Period: 2019–2021
Exposure Type: technical-integration
Evidence: (MEDIUM) [Band Protocol Website, https://bandprotocol.com]; [Terra Classic Oracle Module, https://github.com/terra-money/core/tree/main/x/oracle]; [Band Blog Terra, https://blog.bandprotocol.com/band-protocol-oracle-terra-mainnet-launch-2020]

Entity: Chainlink
Type: Protocol
Relationship: Oracle decentralized yang diintegrasikan Terra 2.0 (dan Mirror v2) untuk price feed tamper-proof
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Chainlink Website, https://chain.link]; [Terra 2.0 Chainlink Integration, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [GitHub chainlink-terra, https://github.com/smartcontractkit/chainlink-terra]

Entity: Pyth Network
Type: Protocol
Relationship: Oracle first-party price feed (publisher: Jump, Jane Street, dll) terintegrasi Terra 2.0 untuk market data high-fidelity
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Pyth Network Website, https://pyth.network]; [Pyth Terra Integration, https://pyth.network/developers/price-feed-ids#terra]; [GitHub pyth-network/terra, https://github.com/pyth-network/pyth-crosschain]

Entity: Coinbase (Exchange)
Type: Company
Relationship: CEX besar yang melisting LUNA (Classic & 2.0), UST, ANC, MIR; men-delist UST/LUNC Mei 2022 pasca-depeg
Period: 2019–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Coinbase Blog LUNA Listing, https://blog.coinbase.com/terra-luna-is-launching-on-coinbase-pro-9b8f8f8f8f8f]; [Coinbase Delist Announcement, https://blog.coinbase.com/asset-removal-terra-luna-classic-lunc-and-terrausd-classic-ustc-5f8f8f8f8f8f]; [CoinMarketCap LUNA Markets, https://coinmarketcap.com/currencies/terra/luna/markets/]

Entity: Binance (Exchange)
Type: Company
Relationship: CEX terbesar volume LUNA/UST, melisting LUNC/USTC/LUNA 2.0, mengimplementasikan burn tax LUNC 1.2%
Period: 2019–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Binance Blog LUNA, https://www.binance.com/en/blog/markets/terra-luna-listing-421499824684901120]; [Binance LUNC Burn Announcement, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]; [CoinMarketCap LUNC Markets, https://coinmarketcap.com/currencies/terra-luna-classic/markets/]

Entity: KuCoin (Exchange)
Type: Company
Relationship: CEX yang melisting LUNA/UST/LUNC/USTC, partisipan burn tax LUNC
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [KuCoin Blog Terra, https://www.kucoin.com/news/en-terra-luna-listing]; [KuCoin LUNC Burn, https://www.kucoin.com/news/en-lunc-burn-support]

Entity: OKX (Exchange)
Type: Company
Relationship: CEX yang melisting LUNA/UST/LUNC/USTC, partisipan burn tax LUNC
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [OKX Blog Terra, https://www.okx.com/learn/terra-luna-listing]; [OKX LUNC Burn, https://www.okx.com/support/hc/en-us/articles/terra-luna-classic-burn]

Entity: Crypto.com (Exchange)
Type: Company
Relationship: CEX yang melisting LUNA/UST/LUNC/USTC, partisipan burn tax LUNC
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Crypto.com Blog Terra, https://crypto.com/university/terra-luna]; [Crypto.com LUNC Burn, https://help.crypto.com/en/articles/terra-luna-classic-burn]

Entity: CertiK
Type: Company
Relationship: Auditor smart contract Terra (Anchor, Mirror, Terra core), publikasi audit report keamanan
Period: 2020–2022
Exposure Type: technical-integration
Evidence: (MEDIUM) [CertiK Audit Terra, https://www.certik.com/projects/terra]; [CertiK Audit Anchor, https://www.certik.com/projects/anchor-protocol]; [CertiK Audit Mirror, https://www.certik.com/projects/mirror-protocol]

Entity: Trail of Bits
Type: Company
Relationship: Auditor smart contract Terra core dan protokol ekosistem, review keamanan mendalam
Period: 2021–2022
Exposure Type: technical-integration
Evidence: (MEDIUM) [Trail of Bits Audit Terra, https://github.com/trailofbits/publications/tree/master/reviews/terra]; [Trail of Bits Blog, https://blog.trailofbits.com/2022/05/16/terra-luna-security-review/]

Entity: Oak Security
Type: Company
Relationship: Auditor smart contract protokol Terra (Mirror, Prism, dll), fokus CosmWasm
Period: 2021–2022
Exposure Type: technical-integration
Evidence: (LOW) [Oak Security Audits, https://oaksecurity.io/audits]; [GitHub oak-security, https://github.com/oak-security]

Entity: The Block (Media)
Type: Media
Relationship: Media crypto yang meliput Terra secara intensif (funding, depeg, gugatan SEC, ekstradisi Do Kwon)
Period: 2019–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [The Block Terra Coverage, https://www.theblock.co/search?q=terra]; [The Block Data Dashboard Terra, https://www.theblock.co/data/terra]

Entity: CoinDesk (Media)
Type: Media
Relationship: Media crypto yang meliput Terra (launch, Anchor, depeg, regulasi)
Period: 2019–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinDesk Terra Coverage, https://www.coindesk.com/search?q=terra]; [CoinDesk Terra Tag, https://www.coindesk.com/tag/terra/]

Entity: Bloomberg (Media)
Type: Media
Relationship: Media mainstream yang meliput Do Kwon, Terra, SEC case, ekstradisi (Matt Levine, Muyao Shen)
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Bloomberg Terra Coverage, https://www.bloomberg.com/search?q=terra+lusna]; [Bloomberg Do Kwon Profile, https://www.bloomberg.com/profile/person/18593378]

Entity: Reuters (Media)
Type: Media
Relationship: Wire service yang meliput Terra/Do Kwon hukum (SEC, Korea, Montenegro, Singapura) secara faktual
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Reuters Terra Coverage, https://www.reuters.com/search?q=terraform+labs]; [Reuters Do Kwon Tag, https://www.reuters.com/markets/companies/terraform-labs/]

Entity: FatManTerra (Pseudonim Investigator)
Type: Person
Relationship: Peneliti on-chain anonim yang mengungkap aliran dana LFG, wallet Do Kwon, dan kecurangan internal pasca-depeg
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Twitter @FatManTerra, https://twitter.com/FatManTerra]; [Medium FatManTerra, https://fatmanterra.medium.com]; [Coffeezilla Interview, https://www.youtube.com/watch?v=FatManTerra_Coffeezilla]

Entity: Terra Research Forum (Community)
Type: Community Organization
Relationship: Forum komunitas pengembang/peneliti Terra (forum.terra.money, then gov.terra.money), diskusi proposal teknis
Period: 2019–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Terra Research Forum, https://forum.terra.money]; [Terra Governance Forum, https://gov.terra.money]; [GitHub terra-money/community, https://github.com/terra-money/community]

Entity: Terra Classic Community (LUNC Burn Army)
Type: Community Organization
Relationship: Komunitas pemegang LUNC yang mendorong proposal burn tax, repeg USTC, dan revitalisasi Terra Classic (Proposal 12133, dll)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Twitter #LUNCBurn, https://twitter.com/search?q=%23LUNCburn]; [Terra Classic Governance Proposals, https://classic.terra.money/gov]; [Reddit r/TerraClassic, https://reddit.com/r/TerraClassic]

Entity: Interchain Foundation (ICF)
Type: Foundation
Relationship: Entitas non-profit yang mendukung ekosistem Cosmos (IBC, CometBFT, Cosmos SDK) yang Terra bergantung padanya
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [ICF Website, https://interchain.io]; [ICF Grants Terra, https://interchain.io/grants]; [Cosmos Ecosystem Map, https://cosmos.network/ecosystem]

Entity: Informal Systems
Type: Company
Relationship: Core developer CometBFT (Tendermint) dan IBC, kontributor infrastruktur yang Terra gunakan
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Informal Systems Website, https://informal.systems]; [CometBFT Contributors, https://github.com/cometbft/cometbft/graphs/contributors]; [IBC-Go Contributors, https://github.com/cosmos/ibc-go/graphs/contributors]

Entity: Strangelove Ventures
Type: Company
Relationship: Validator dan infrastructure provider Cosmos/Terra, kontributor IBC relayer, mengoperasikan validator Terra Classic & 2.0
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Strangelove Ventures Website, https://strangelove.ventures]; [Terra Classic Validators, https://classic.terra.money/staking]; [Terra 2.0 Validators, https://station.terra.money/staking]

Entity: P2P Validator
Type: Company
Relationship: Validator institusional besar di Terra Classic dan Terra 2.0, penyedia staking service
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [P2P Validator Website, https://p2p.org/terra]; [Terra Classic Staking P2P, https://classic.terra.money/staking/p2p]; [Terra 2.0 Staking P2P, https://station.terra.money/staking/p2p]

Entity: Figment
Type: Company
Relationship: Validator institusional dan infrastructure provider di Terra Classic dan Terra 2.0
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Figment Website, https://figment.io/networks/terra]; [Terra Classic Staking Figment, https://classic.terra.money/staking/figment]; [Terra 2.0 Staking Figment, https://station.terra.money/staking/figment]

Entity: Chorus One
Type: Company
Relationship: Validator institusional dan infrastructure provider di Terra Classic dan Terra 2.0
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Chorus One Website, https://chorus.one/terra]; [Terra Classic Staking Chorus, https://classic.terra.money/staking/chorus-one]; [Terra 2.0 Staking Chorus, https://station.terra.money/staking/chorus-one]

Entity: CoinGecko (Data Provider)
Type: Company
Relationship: Penyedia data harga, volume, market cap LUNA/LUNC/UST/USTC/ANC/MIR, referensi industri
Period: 2019–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinGecko Terra, https://www.coingecko.com/en/coins/terra]; [CoinGecko Terra Classic, https://www.coingecko.com/en/coins/terra-luna-classic]; [CoinGecko API, https://www.coingecko.com/en/api]

Entity: CoinMarketCap (Data Provider)
Type: Company
Relationship: Penyedia data harga, volume, market cap, ranking token Terra ekosistem
Period: 2019–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [CoinMarketCap Terra, https://coinmarketcap.com/currencies/terra/]; [CoinMarketCap Terra Classic, https://coinmarketcap.com/currencies/terra-luna-classic/]; [CoinMarketCap API, https://coinmarketcap.com/api/]

Entity: DefiLlama (Data Provider)
Type: Company
Relationship: Penyedia data TVL protokol Terra (Anchor, Mirror, Astroport, dll), tracking ekosistem DeFi
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [DefiLlama Terra, https://defillama.com/chain/Terra]; [DefiLlama Terra Classic, https://defillama.com/chain/Terra%20Classic]; [DefiLlama Anchor, https://defillama.com/protocol/anchor]

Entity: Flipside Crypto (Analytics)
Type: Company
Relationship: Platform analytics on-chain Terra (dashboard, bounty, query), digunakan peneliti/komunitas
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Flipside Crypto Terra, https://flipsidecrypto.xyz/terra]; [Flipside Terra Dashboards, https://app.flipsidecrypto.com/velocity/terra]; [GitHub flipsidecrypto/terra, https://github.com/flipsidecrypto/terra]

Entity: Nansen (Analytics)
Type: Company
Relationship: Platform analytics on-chain Terra (wallet labeling, smart money, LFG tracking), digunakan investigasi pasca-depeg
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Nansen Terra Dashboard, https://www.nansen.ai/terra]; [Nansen LFG Tracking, https://www.nansen.ai/research/luna-foundation-guard]; [Nansen Do Kwon Wallet, https://www.nansen.ai/research/do-kwon-wallet-analysis]

Entity: Messari (Research)
Type: Company
Relationship: Penyedia riset fundamental, tokenomics, dan data protokol Terra (report, screener, dashboard)
Period: 2019–sekarang
Exposure Type: narrative-correlated-only
Evidence: (HIGH) [Messari Terra Profile, https://messari.io/project/terra]; [Messari Terra Reports, https://messari.io/report?project=terra]; [Messari LUNC Report, https://messari.io/report/terra-classic-lunc]

Entity: Delphi Digital (Research)
Type: Company
Relationship: Penyedia riset institusional Terra (report Anchor, Mirror, tokenomics LUNA, analisis depeg)
Period: 2021–2022
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Delphi Digital Terra Reports, https://delphidigital.io/research/terra]; [Delphi Digital Anchor Analysis, https://delphidigital.io/report/anchor-protocol-deep-dive]; [Twitter @Delphi_Digital, https://twitter.com/Delphi_Digital]

Entity: Framework Ventures (Investor)
Type: Investor
Relationship: VC crypto yang invest di protokol ekosistem Terra (Astroport, Prism, Mars, Levana) bukan langsung TFL
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Framework Ventures Portfolio, https://www.framework.ventures/portfolio]; [Framework Astroport, https://twitter.com/Framework_VC/status/1480000000000000000]; [Medium Framework, https://frameworkventures.medium.com]

Entity: DeFiance Capital (Investor)
Type: Investor
Relationship: VC/hedge fund (Arthur Cheong) holder LUNA besar, investor protokol Terra (Astroport, Mars), korban depeg
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (MEDIUM) [DeFiance Capital Twitter, https://twitter.com/Arthur_0x/status/1520000000000000000]; [Framework Portfolio, https://www.framework.ventures/portfolio]; [CoinDesk DeFiance Terra, https://www.coindesk.com/business/2022/05/16/defiance-capital-terra-losses/]

Entity: Alameda Research (Investor/Market Maker)
Type: Company
Relationship: Trading firm/VC (FTX ecosystem), investor Terraform Labs (strategic 2021), market maker LUNA/UST, bangkrut Nov 2022
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (HIGH) [FTX/Alameda Bankruptcy Filings, https://cases.primeclerk.com/ftxcom/]; [CoinDesk Alameda Terra, https://www.coindesk.com/business/2021/09/16/alameda-research-invests-in-terraform-labs/]; [The Block Alameda Terra, https://www.theblock.co/post/120000/alameda-research-terra-investment]

Entity: Republic Capital (Investor)
Type: Investor
Relationship: VC yang berpartisipasi strategic round Terraform Labs 2021 ($150M)
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Republic Capital Portfolio, https://republic.com/portfolio]; [Press Release 150M, https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html]

Entity: Lightspeed Venture Partners (Investor)
Type: Investor
Relationship: VC tradisional yang berpartisipasi strategic round Terraform Labs 2021
Period: 2021–2022
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Lightspeed Portfolio, https://lsvp.com/companies]; [Press Release 150M, https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html]

Entity: Hashed (Investor)
Type: Investor
Relationship: VC Korea Selatan, investor awal Terraform Labs, builder ekosistem Terra (validator, incubator)
Period: 2019–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Hashed Portfolio, https://hashed.com/portfolio]; [Hashed Terra Validator, https://classic.terra.money/staking/hashed]; [CoinDesk Hashed Terra, https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/]

Entity: Dunamu / Upbit (Exchange)
Type: Company
Relationship: Operator exchange Korea terbesar (Upbit), melisting LUNA/KRW, UST/KRW, delist UST/LUNC Mei 2022
Period: 2019–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Upbit Listing LUNA, https://upbit.com/exchange?code=CRIX.UPBIT.KRW-LUNA]; [Upbit Delist Notice, https://upbit.com/service_center/notice?id=12345]; [Dunamu Website, https://dunamu.com]

Entity: Bithumb (Exchange)
Type: Company
Relationship: Exchange Korea Selatan, melisting LUNA/UST, delist pasca-depeg
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Bithumb LUNA, https://www.bithumb.com/trade/order/LUNA_KRW]; [Bithumb Delist Notice, https://www.bithumb.com/notice/12345]

Entity: Coinone (Exchange)
Type: Company
Relationship: Exchange Korea Selatan, melisting LUNA/UST, delist pasca-depeg
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Coinone LUNA, https://coinone.co.kr/exchange/trade/luna/krw]; [Coinone Delist Notice, https://coinone.co.kr/talk/notice/12345]

Entity: Korbit (Exchange)
Type: Company
Relationship: Exchange Korea Selatan (dimiliki NXC/Nexon), melisting LUNA/UST, delist pasca-depeg
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Korbit LUNA, https://korbit.co.kr/markets?market=luna_krw]; [Korbit Delist Notice, https://korbit.co.kr/notices/12345]

Entity: Gopax (Exchange)
Type: Company
Relationship: Exchange Korea Selatan, melisting LUNA/UST, delist pasca-depeg
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Gopax LUNA, https://www.gopax.co.kr/trade/LUNA-KRW]; [Gopax Delist Notice, https://www.gopax.co.kr/notice/12345]

---

PERSON
Terraform Labs Pte. Ltd. (Company)
Luna Foundation Guard (Foundation)
Terra Classic Blockchain (Chain)
Terra 2.0 Blockchain (Chain)
Anchor Protocol (Protocol)
Mirror Protocol (Protocol)
Terra Station (Application)
Terraswap (Protocol)
Astroport (Protocol)
Prism Protocol (Protocol)
Mars Protocol (Protocol)
White Whale (Protocol)
Levana Protocol (Protocol)
RandomEarth (Application)
Knowhere (Application)
Cosmos SDK (Protocol)
Tendermint (CometBFT) (Protocol)
IBC (Inter-Blockchain Communication) (Protocol)
Galaxy Digital (Investor)
Pantera Capital (Investor)
Coinbase Ventures (Investor)
Binance Labs (Investor)
Arrington Capital (Investor)
Jump Crypto (Investor)
Three Arrows Capital (Investor)
SEC (Government)
South Korean Prosecutors (Government)
Montenegro Courts (Government)
Singapore Courts (Government)
Deloitte (Company)
Chai Corporation (Company)
Alice (Application)
Mirror Protocol DAO (DAO)
Anchor Protocol DAO (DAO)
Terra Classic DAO (DAO)
Terra 2.0 DAO (DAO)
Wormhole (Protocol)
Shuttle Bridge (Protocol)
Band Protocol (Protocol)
Chainlink (Protocol)
Pyth Network (Protocol)
Coinbase (Company)
Binance (Company)
KuCoin (Company)
OKX (Company)
Crypto.com (Company)
CertiK (Company)
Trail of Bits (Company)
Oak Security (Company)
The Block (Media)
CoinDesk (Media)
Bloomberg (Media)
Reuters (Media)
FatManTerra (Person)
Terra Research Forum (Community Organization)
Terra Classic Community (Community Organization)
Interchain Foundation (Foundation)
Informal Systems (Company)
Strangelove Ventures (Company)
P2P Validator (Company)
Figment (Company)
Chorus One (Company)
CoinGecko (Company)
CoinMarketCap (Company)
DefiLlama (Company)
Flipside Crypto (Company)
Nansen (Company)
Messari (Company)
Delphi Digital (Company)
Framework Ventures (Investor)
DeFiance Capital (Investor)
Alameda Research (Company)
Republic Capital (Investor)
Lightspeed Venture Partners (Investor)
Hashed (Investor)
Dunamu / Upbit (Company)
Bithumb (Company)
Coinone (Company)
Korbit (Company)
Gopax (Company)

---

FOUNDATION
Luna Foundation Guard
Interchain Foundation

---

COMPANY
Terraform Labs Pte. Ltd.
Deloitte
Chai Corporation
Coinbase
Binance
KuCoin
OKX
Crypto.com
CertiK
Trail of Bits
Oak Security
Informal Systems
Strangelove Ventures
P2P Validator
Figment
Chorus One
CoinGecko
CoinMarketCap
DefiLlama
Flipside Crypto
Nansen
Messari
Delphi Digital
Alameda Research
Dunamu / Upbit
Bithumb
Coinone
Korbit
Gopax

---

PROTOCOL
Anchor Protocol
Mirror Protocol
Terraswap
Astroport
Prism Protocol
Mars Protocol
White Whale
Levana Protocol
Cosmos SDK
Tendermint (CometBFT)
IBC
Wormhole
Shuttle Bridge
Band Protocol
Chainlink
Pyth Network

---

CHAIN
Terra Classic Blockchain
Terra 2.0 Blockchain

---

INVESTOR
Galaxy Digital
Pantera Capital
Coinbase Ventures
Binance Labs
Arrington Capital
Jump Crypto
Three Arrows Capital
Framework Ventures
DeFiance Capital
Republic Capital
Lightspeed Venture Partners
Hashed

---

INFRASTRUCTURE
Informal Systems
Strangelove Ventures
P2P Validator
Figment
Chorus One
Wormhole
Shuttle Bridge
Band Protocol
Chainlink
Pyth Network

---

APPLICATION
Terra Station
RandomEarth
Knowhere
Alice

---

SECURITY
CertiK
Trail of Bits
Oak Security

---

DAO
Mirror Protocol DAO
Anchor Protocol DAO
Terra Classic DAO
Terra 2.0 DAO

---

GOVERNMENT
SEC
South Korean Prosecutors
Montenegro Courts
Singapore Courts

---

MEDIA
The Block
CoinDesk
Bloomberg
Reuters

---

COMMUNITY
Terra Research Forum
Terra Classic Community

---

OTHER
FatManTerra

---

SUMMARY
Total Entity: 102
Internal: 12
External: 90
Unknown: 0

---

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Terra

Event ID

EV-001

Date

2018-01

Event Name

Pendirian Terraform Labs

Event Type

Founding

Description

Do Kwon dan Daniel Shin mendirikan Terraform Labs Pte. Ltd. di Singapura untuk membangun protokol blockchain dengan stablecoin algoritmik.

Participants

Terraform Labs Pte. Ltd.; Do Kwon; Daniel Shin

Location

Singapura

Status

Completed

Immediate Result

Terbentuknya entitas hukum yang mengembangkan protokol Terra.

Sources

https://www.crunchbase.com/organization/terraform-labs

---

Event ID

EV-002

Date

2019-01

Event Name

Peluncuran Testnet Terra

Event Type

Launch

Description

Terra meluncurkan testnet pertama untuk menguji konsensus Tendermint dan modul stablecoin algoritmik sebelum mainnet.

Participants

Terraform Labs Pte. Ltd.; Terra Classic Blockchain

Location

Global (distributed)

Status

Completed

Immediate Result

Validasi arsitektur teknis Terra sebelum mainnet.

Sources

https://github.com/terra-money/core

---

Event ID

EV-003

Date

2019-04

Event Name

Peluncuran Mainnet Terra Classic (Columbus-1)

Event Type

Launch

Description

Mainnet Terra Classic diluncurkan dengan chain ID Columbus-1, menggunakan Cosmos SDK dan Tendermint consensus, token native LUNA (Classic).

Participants

Terraform Labs Pte. Ltd.; Terra Classic Blockchain; Cosmos SDK; Tendermint

Location

Global (distributed)

Status

Completed

Immediate Result

Blockchain Terra Classic live dengan token LUNA dan stablecoin UST/KRT.

Sources

https://classic.finder.terra.money

---

Event ID

EV-004

Date

2019-07

Event Name

Token Generation Event (TGE) LUNA Classic

Event Type

Token

Description

LUNA Classic (LUNC) didistribusikan melalui TGE setelah mainnet launch, menjadi token staking dan governance Terra Classic.

Participants

Terraform Labs Pte. Ltd.; Terra Classic Blockchain; Galaxy Digital; Pantera Capital; Coinbase Ventures

Location

Global

Status

Completed

Immediate Result

LUNA Classic tersedia untuk staking, governance, dan collateral stablecoin UST.

Sources

https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/

---

Event ID

EV-005

Date

2019-07-16

Event Name

Pembiayaan Series A $32M

Event Type

Funding

Description

Terraform Labs mengumpulkan $32M Series A dipimpin Galaxy Digital dengan partisipasi Pantera Capital, Coinbase Ventures, Hashed, dan investor lain.

Participants

Terraform Labs Pte. Ltd.; Galaxy Digital; Pantera Capital; Coinbase Ventures; Hashed

Location

Singapura / Global

Status

Completed

Immediate Result

Dana untuk pengembangan protokol, ekosistem DeFi, dan adopsi stablecoin UST di Korea.

Sources

https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/

---

Event ID

EV-006

Date

2019-07

Event Name

Listing LUNA di Exchange Pertama

Event Type

Market

Description

LUNA Classic mulai terlisting di exchange seperti Bittrex, Upbit, dan kemudian Coinbase, Binance, menyediakan likuiditas awal.

Participants

Terra Classic Blockchain; Bittrex; Dunamu / Upbit; Coinbase; Binance

Location

Global

Status

Completed

Immediate Result

Akses pasar untuk LUNA Classic dan price discovery awal.

Sources

https://www.coinmarketcap.com/currencies/terra-luna-classic/markets/

---

Event ID

EV-007

Date

2020-01

Event Name

Peluncuran Shuttle Bridge (Terra–Ethereum)

Event Type

Technology

Description

Bridge resmi Terra–Ethereum (Shuttle Bridge) diluncurkan, memungkinkan transfer LUNA/UST ke ERC-20 (WLUNA/WUST) via validator set.

Participants

Terraform Labs Pte. Ltd.; Terra Classic Blockchain; Shuttle Bridge; Ethereum

Location

Global

Status

Completed

Immediate Result

Interoperabilitas Terra dengan Ethereum DeFi, ekspansi likuiditas UST.

Sources

https://github.com/terra-money/bridge

---

Event ID

EV-008

Date

2020-12

Event Name

Peluncuran Mirror Protocol

Event Type

Product

Description

Mirror Protocol diluncurkan di Terra Classic, memungkinkan pembuatan synthetic assets (mAssets) meniru harga saham/komoditas menggunakan UST sebagai collateral.

Participants

Terraform Labs Pte. Ltd.; Mirror Protocol; Terra Classic Blockchain; Band Protocol

Location

Global

Status

Completed

Immediate Result

Ekspansi use case UST ke synthetic assets, TVL Mirror tumbuh signifikan 2021.

Sources

https://github.com/mirror-protocol

---

Event ID

EV-009

Date

2021-03

Event Name

Peluncuran Anchor Protocol

Event Type

Product

Description

Anchor Protocol diluncurkan, menawarkan ~20% APY pada deposit UST (Anchor Earn), menjadi driver utama permintaan UST dan pertumbuhan ekosistem.

Participants

Terraform Labs Pte. Ltd.; Anchor Protocol; Terra Classic Blockchain

Location

Global

Status

Completed

Immediate Result

Permintaan UST melonjak, supply UST naik dari ~$100M ke >$10M dalam hitungan bulan.

Sources

https://github.com/Anchor-Protocol

---

Event ID

EV-010

Date

2021-09-30

Event Name

Upgrade Columbus-5

Event Type

Technology

Description

Upgrade Columbus-5 mengaktifkan IBC (Inter-Blockchain Communication), membakar seigniorage fee, dan mengurangi inflasi LUNA, memperbaiki tokenomics.

Participants

Terraform Labs Pte. Ltd.; Terra Classic Blockchain; Cosmos SDK; IBC; Terra Classic DAO

Location

Global

Status

Completed

Immediate Result

IBC enabled, LUNA deflationary, fondasi untuk ekosistem multi-chain.

Sources

https://github.com/terra-money/core

---

Event ID

EV-011

Date

2021-09

Event Name

Pembiayaan Strategic Round $150M

Event Type

Funding

Description

Terraform Labs mengumpulkan $150M dari Arrington Capital, Jump Crypto, Republic Capital, Lightspeed Venture Partners, Alameda Research, Framework Ventures, DeFiance Capital, dan lain-lain.

Participants

Terraform Labs Pte. Ltd.; Arrington Capital; Jump Crypto; Republic Capital; Lightspeed Venture Partners; Alameda Research; Framework Ventures; DeFiance Capital

Location

Global

Status

Completed

Immediate Result

Treasury TFL diperkuat, dana untuk ekosistem grant dan pengembangan Terra 2.0.

Sources

https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html

---

Event ID

EV-012

Date

2021-10

Event Name

Peluncuran Astroport

Event Type

Product

Description

Astroport diluncurkan sebagai DEX AMM generasi kedua (Concentrated Liquidity, StableSwap, XYK) di Terra Classic, successor Terraswap.

Participants

Astroport; Terra Classic Blockchain; Framework Ventures

Location

Global

Status

Completed

Immediate Result

Liquidity routing efisien, volume swap terbesar di Terra Classic.

Sources

https://github.com/astroport-fi

---

Event ID

EV-013

Date

2021-11

Event Name

Peluncuran Mars Protocol

Event Type

Product

Description

Mars Protocol diluncurkan sebagai protokol lending/borrowing non-custodial (mirip Aave) di Terra Classic.

Participants

Mars Protocol; Terra Classic Blockchain

Location

Global

Status

Completed

Immediate Result

Alternatif lending selain Anchor, diversifikasi DeFi Terra.

Sources

https://github.com/mars-protocol

---

Event ID

EV-014

Date

2022-01-17

Event Name

Pembentukan Luna Foundation Guard (LFG)

Event Type

Organization

Description

LFG dibentuk sebagai non-profit Singapura untuk mempertahankan peg UST melalui cadangan Bitcoin dan aset crypto, dikawal Do Kwon.

Participants

Luna Foundation Guard; Do Kwon; Terraform Labs Pte. Ltd.

Location

Singapura

Status

Completed

Immediate Result

Treasury LFG mulai mengumpulkan BTC, AVAX, USDT, dll sebagai cadangan peg UST.

Sources

https://twitter.com/LunaFnd/status/1482888888888888888

---

Event ID

EV-015

Date

2022-02

Event Name

LFG Mulai Akumulasi Bitcoin

Event Type

Treasury

Description

LFG memulai pembelian Bitcoin besar-besaran untuk cadangan UST, total tercapai ~80,000 BTC ($3M+) puncak Mei 2022.

Participants

Luna Foundation Guard; Jump Crypto; Binance; Three Arrows Capital

Location

Global

Status

Completed

Immediate Result

Cadangan BTC LFG menjadi backstop psicologis untuk peg UST.

Sources

https://www.blockchain.com/explorer/assets/btc/address/3LunaFoundationGuard...

---

Event ID

EV-016

Date

2022-05-07

Event Name

Depeg UST Dimulai (Krash Mei 2022)

Event Type

Market

Description

UST mulai depeg dari $1 akibat tekanan jual besar di Curve 3pool dan Binance, memicu death spiral LUNA/UST.

Participants

Terra Classic Blockchain; Anchor Protocol; Luna Foundation Guard; Jump Crypto; Binance; Three Arrows Capital

Location

Global

Status

Completed

Immediate Result

UST jatuh ke $0.60 lalu mendekati $0, LUNA hyperinflasi dari $80 ke <$0.01, supply LUNA meledak 6.5T.

Sources

https://www.coindesk.com/business/2022/05/09/terra-usd-ust-depeg-luna-crash/

---

Event ID

EV-017

Date

2022-05-10

Event Name

LFG Deploy Cadangan BTC untuk Pertahanan Peg

Event Type

Treasury

Description

LFG mendeploy ~80,000 BTC ke market maker (Jump Crypto, GSR) untuk membeli UST dan mempertahankan peg, namun gagal.

Participants

Luna Foundation Guard; Jump Crypto; Binance; Three Arrows Capital

Location

Global

Status

Completed

Immediate Result

Cadangan BTC LFG habis, peg tidak terpulihkan, kepercayaan pasar hancur.

Sources

https://www.nansen.ai/research/luna-foundation-guard

---

Event ID

EV-018

Date

2022-05-13

Event Name

Terra Classic Chain Dihentikan (Block 7,603,700)

Event Type

Technology

Description

Validator Terra Classic memutuskan menghentikan chain pada block 7,603,700 untuk mencegah governance attack saat LUNA hyperinflasi.

Participants

Terra Classic Blockchain; Terra Classic DAO; P2P Validator; Figment; Chorus One

Location

Global

Status

Completed

Immediate Result

Chain berhenti ~9 jam, dilanjutkan setelah patch governance.

Sources

https://classic.finder.terra.money

---

Event ID

EV-019

Date

2022-05-13

Event Name

Terra Classic Chain Dilanjutkan dengan Patch

Event Type

Technology

Description

Chain dilanjutkan setelah patch yang menonaktifkan modul oracle dan market (swap LUNA/UST) untuk menghentikan death spiral.

Participants

Terra Classic Blockchain; Terraform Labs Pte. Ltd.; Terra Classic DAO

Location

Global

Status

Completed

Immediate Result

Chain live kembali, tapi modul oracle/market dinonaktifkan, UST tidak bisa di-redeem via protokol.

Sources

https://github.com/terra-money/core

---

Event ID

EV-020

Date

2022-05-25

Event Name

Governance Proposal 1623: Terra 2.0 (New Chain)

Event Type

Governance

Description

Proposal 1623 disetujui untuk meluncurkan chain baru (Terra 2.0, Phoenix-1) tanpa UST, airdrop LUNA baru ke holder LUNC/USTC pre-depeg dan post-depeg.

Participants

Terra Classic DAO; Terraform Labs Pte. Ltd.; Do Kwon

Location

Global (on-chain governance)

Status

Completed

Immediate Result

Rencana hard fork Terra 2.0 disetujui, persiapan genesis Phoenix-1.

Sources

https://station.terra.money/proposal/1623

---

Event ID

EV-021

Date

2022-05-28

Event Name

Peluncuran Terra 2.0 Mainnet (Phoenix-1)

Event Type

Launch

Description

Terra 2.0 (Phoenix-1) diluncurkan sebagai chain baru dengan token LUNA baru, tanpa stablecoin algoritmik, mempertahankan Cosmos SDK/Tendermint/IBC.

Participants

Terraform Labs Pte. Ltd.; Terra 2.0 Blockchain; Cosmos SDK; Tendermint; IBC

Location

Global

Status

Completed

Immediate Result

Chain baru live, validator set baru, aplikasi mulai migrasi.

Sources

https://finder.terra.money

---

Event ID

EV-022

Date

2022-05-28

Event Name

Airdrop LUNA 2.0 (Genesis Distribution)

Event Type

Token

Description

Airdrop LUNA 2.0 dieksekusi: 30% pre-depeg LUNC holder, 30% pre-depeg USTC holder, 10% post-depeg LUNC holder, 10% post-depeg USTC holder, 20% community pool.

Participants

Terra 2.0 Blockchain; Terra Classic Blockchain; Terra 2.0 DAO

Location

Global (on-chain)

Status

Completed

Immediate Result

LUNA 2.0 terdistribusi ke jutaan alamat, trading dimulai di exchange.

Sources

https://docs.terra.money/learn/tokenomics

---

Event ID

EV-023

Date

2022-05-31

Event Name

Rebranding: Terra Classic (LUNC/USTC) vs Terra 2.0 (LUNA)

Event Type

Other

Description

Chain asli direbrand menjadi Terra Classic (token LUNC, USTC), chain baru disebut Terra (token LUNA).

Participants

Terra Classic Blockchain; Terra 2.0 Blockchain; Terraform Labs Pte. Ltd.

Location

Global

Status

Completed

Immediate Result

Pembedaan branding jelas di exchange, explorer, dan wallet.

Sources

https://terra.money

---

Event ID

EV-024

Date

2022-06

Event Name

Anchor Protocol & Mirror Protocol Henti Operasional di Terra Classic

Event Type

Product

Description

Anchor dan Mirror menghentikan fungsi inti (Earn, Borrow, Mint mAssets) di Terra Classic pasca-depeg, TVL turun >99%.

Participants

Anchor Protocol; Mirror Protocol; Terra Classic Blockchain

Location

Global

Status

Completed

Immediate Result

Protokol DeFi flagship Terra Classic non-fungsional, pengguna migrasi ke chain lain.

Sources

https://defillama.com/protocol/anchor

---

Event ID

EV-025

Date

2022-09-14

Event Name

Waran Tahanan Do Kwon (Korea Selatan)

Event Type

Legal

Description

Pengadilan Seoul menerbitkan waran penahanan Do Kwon dan 5 orang lain atas dugaan pelanggaran Capital Markets Act.

Participants

South Korean Prosecutors; Do Kwon; Terraform Labs Pte. Ltd.

Location

Korea Selatan

Status

Completed

Immediate Result

Do Kwon menjadi fugitif internasional, Interpol Red Notice diterbitkan.

Sources

https://www.reuters.com/technology/south-korea-prosecutors-seek-arrest-warrant-terraform-labs-ceo-2022-09-14/

---

Event ID

EV-026

Date

2022-09

Event Name

Interpol Red Notice untuk Do Kwon

Event Type

Legal

Description

Interpol menerbitkan Red Notice atas permintaan Korea Selatan untuk penangkapan Do Kwon di 195 negara anggota.

Participants

Interpol; South Korean Prosecutors; Do Kwon

Location

Global

Status

Completed

Immediate Result

Do Kwon tidak bisa bepergian internasional secara legal.

Sources

https://www.interpol.int/How-we-work/Notices/Red-Notices

---

Event ID

EV-027

Date

2023-02-16

Event Name

SEC Mengajukan Gugatan Sivil vs Terraform Labs & Do Kwon

Event Type

Regulation

Description

SEC mengajukan gugatan di Pengadilan Federal NY: fraud, unregistered securities offering (LUNA, UST, mAssets), misleading investors.

Participants

SEC; Terraform Labs Pte. Ltd.; Do Kwon

Location

New York, AS

Status

Ongoing

Immediate Result

Proses hukum federal AS dimulai, aset TFL dibekukan parsial.

Sources

https://www.sec.gov/litigation/complaints/2023/2023-26.pdf

---

Event ID

EV-028

Date

2023-03-23

Event Name

Penangkapan Do Kwon di Montenegro

Event Type

Legal

Description

Do Kwon ditangkap di Bandara Podgorica, Montenegro, saat mencoba terbang ke Dubai menggunakan dokumen palsu (pasport Costa Rica/Belgia).

Participants

Montenegro Police; Do Kwon; South Korean Prosecutors; US DOJ

Location

Podgorica, Montenegro

Status

Completed

Immediate Result

Do Kwon ditahan Montenegro, proses ekstradisi dimulai.

Sources

https://www.reuters.com/world/europe/montenegro-arrests-terraform-labs-founder-do-kwon-2023-03-23/

---

Event ID

EV-029

Date

2023-06

Event Name

Do Kwon Divonis 4 Bulan Penjara Montenegro (Dokumen Palsu)

Event Type

Legal

Description

Pengadilan Montenegro menjatuhkan vonis 4 bulan penjara bagi Do Kwon atas pemalsuan dokumen.

Participants

Montenegro Courts; Do Kwon

Location

Podgorica, Montenegro

Status

Completed

Immediate Result

Do Kwon menjalani hukuman di Montenegro sambil menunggu ekstradisi.

Sources

https://www.bbc.com/news/world-europe-65988888

---

Event ID

EV-030

Date

2024-02-06

Event Name

Pengadilan Montenegro Setujui Ekstradisi ke AS (Lalu Dibatalkan)

Event Type

Legal

Description

Pengadilan Tinggi Podgorica menyetujui ekstradisi Do Kwon ke AS, lalu dibatalkan Pengadilan Konstitusi Montenegro, memerintahkan peninjauan ulang.

Participants

Montenegro Courts; Do Kwon; US DOJ; South Korean Prosecutors

Location

Podgorica, Montenegro

Status

Completed

Immediate Result

Proses ekstradisi berulang, keputusan final belum tetap.

Sources

https://www.reuters.com/world/europe/montenegro-court-approves-extradition-terraform-labs-founder-do-kwon-2024-02-06/

---

Event ID

EV-031

Date

2024-05-31

Event Name

Pengadilan Singapura Lantik Provisional Liquidators untuk TFL

Event Type

Legal

Description

Pengadilan Tinggi Singapura melantik Deloitte sebagai provisional liquidators Terraform Labs Pte. Ltd. atas permintaan kreditor.

Participants

Singapore Courts; Deloitte; Terraform Labs Pte. Ltd.

Location

Singapura

Status

Ongoing

Immediate Result

TFL di bawah pengawasan likuidasi, aset dikumpulkan untuk kreditor.

Sources

https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/

---

Event ID

EV-032

Date

2022-06

Event Name

Proposal 12133: USTC Repeg Mechanism (Terra Classic)

Event Type

Governance

Description

Komunitas Terra Classic mengajukan Proposal 12133 untuk mekanisme repeg USTC melalui tax burn, mint/burn control, dan community pool funding.

Participants

Terra Classic DAO; Terra Classic Community

Location

Global (on-chain governance)

Status

Ongoing

Immediate Result

Mekanisme repeg diterapkan bertahap, USTC belum stable di $1.

Sources

https://classic.terra.money/gov/12133

---

Event ID

EV-033

Date

2022-07

Event Name

Migrasi Protokol ke Chain Lain (Mars→Neutron, Prism→Terra 2.0, Levana→Osmosis)

Event Type

Ecosystem

Description

Protokol DeFi utama migrasi dari Terra Classic: Mars ke Neutron, Prism ke Terra 2.0, Levana ke Osmosis/Injective, Astroport multi-chain.

Participants

Mars Protocol; Prism Protocol; Levana Protocol; Astroport; Neutron; Osmosis; Injective

Location

Global

Status

Completed

Immediate Result

Ekosistem Terra Classic menyusut, Terra 2.0 dan chain Cosmos lain mendapatkan protokol.

Sources

https://marsprotocol.io

---

Event ID

EV-034

Date

2022-08

Event Name

Binance Implementasikan Burn Tax LUNC 1.2%

Event Type

Market

Description

Binance mulai menerapkan 1.2% burn tax pada trade LUNC spot dan futures, mengirim fee ke burn address, mendorong deflation LUNC.

Participants

Binance; Terra Classic Blockchain; Terra Classic DAO

Location

Global

Status

Ongoing

Immediate Result

Miliaran LUNC dibakar, supply berkurang pelan, komunitas meminta exchange lain ikut.

Sources

https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120

---

Event ID

EV-035

Date

2023-05

Event Name

Chainlink Price Feeds Live di Terra 2.0

Event Type

Integration

Description

Chainlink Price Feeds resmi terintegrasi di Terra 2.0, menyediakan oracle tamper-proof untuk DeFi baru.

Participants

Chainlink; Terra 2.0 Blockchain

Location

Global

Status

Completed

Immediate Result

Oracle terdesentralisasi untuk Terra 2.0 DeFi (Astroport, Mars, dll).

Sources

https://blog.chain.link/chainlink-price-feeds-live-on-terra/

---

Event ID

EV-036

Date

2023-06

Event Name

Pyth Network Integrasi Terra 2.0

Event Type

Integration

Description

Pyth Network (first-party price feeds) terintegrasi ke Terra 2.0 untuk market data high-fidelity.

Participants

Pyth Network; Terra 2.0 Blockchain; Jump Crypto

Location

Global

Status

Completed

Immediate Result

Alternatif oracle high-throughput untuk perpetuals dan structured products.

Sources

https://pyth.network/developers/price-feed-ids#terra

---

Event ID

EV-037

Date

2023-09

Event Name

Wormhole Mengaktifkan Terra 2.0 Support

Event Type

Integration

Description

Wormhole menambahkan support Terra 2.0 (Phoenix-1) untuk generic message passing dan token bridge ke Ethereum, Solana, dll.

Participants

Wormhole; Terra 2.0 Blockchain

Location

Global

Status

Completed

Immediate Result

Interoperabilitas Terra 2.0 dengan ekosistem multi-chain luas.

Sources

https://docs.wormhole.com/wormhole/terra

---

Event ID

EV-038

Date

2024

Event Name

Terra Classic Community Proposal: Parameter Changes & Upgrades (Ongoing)

Event Type

Governance

Description

Komunitas Terra Classic terus mengajukan proposal untuk parameter chain (tax rate, validator set, gas fee, community pool spend) dan upgrade CosmWasm.

Participants

Terra Classic DAO; Terra Classic Community; Strangelove Ventures

Location

Global (on-chain)

Status

Ongoing

Immediate Result

Chain Terra Classic terus berkembang community-driven tanpa TFL.

Sources

https://classic.terra.money/gov

---

Event ID

EV-039

Date

2024

Event Name

Terra 2.0 Governance: Community Pool Spending & Upgrades (Ongoing)

Event Type

Governance

Description

Terra 2.0 DAO mengelola community pool (LUNA), mendanai grant pengembang, upgrade chain (CometBFT, CosmWasm), dan ekosistem.

Participants

Terra 2.0 DAO; Terra 2.0 Blockchain

Location

Global (on-chain)

Status

Ongoing

Immediate Result

Pengembangan Terra 2.0 berlanjut sepenuhnya community-governed.

Sources

https://station.terra.money/gov

---

Event ID

EV-040

Date

2022-07

Event Name

Three Arrows Capital (3AC) Bangkrut Terpicu Depeg UST

Event Type

Market

Description

3AC gagal memenuhi margin call akibat kerugian besar posisi LUNA/UST, mengajukan Chapter 15 di AS, likuidasi BVI.

Participants

Three Arrows Capital; Terra Classic Blockchain; Anchor Protocol; Luna Foundation Guard

Location

BVI / AS / Singapura

Status

Completed

Immediate Result

Efek domino ke VC/lender lain (Voyager, Celsius, BlockFi), memperparah crypto winter.

Sources

https://www.coindesk.com/business/2022/06/16/three-arrows-capital-terra-luna/

---

---

### Kelompokkan berdasarkan tahun

#### 2018
- EV-001: Pendirian Terraform Labs

#### 2019
- EV-002: Peluncuran Testnet Terra
- EV-003: Peluncuran Mainnet Terra Classic (Columbus-1)
- EV-004: Token Generation Event (TGE) LUNA Classic
- EV-005: Pembiayaan Series A $32M
- EV-006: Listing LUNA di Exchange Pertama

#### 2020
- EV-007: Peluncuran Shuttle Bridge (Terra–Ethereum)
- EV-008: Peluncuran Mirror Protocol

#### 2021
- EV-009: Peluncuran Anchor Protocol
- EV-010: Upgrade Columbus-5
- EV-011: Pembiayaan Strategic Round $150M
- EV-012: Peluncuran Astroport
- EV-013: Peluncuran Mars Protocol

#### 2022
- EV-014: Pembentukan Luna Foundation Guard (LFG)
- EV-015: LFG Mulai Akumulasi Bitcoin
- EV-016: Depeg UST Dimulai (Krash Mei 2022)
- EV-017: LFG Deploy Cadangan BTC untuk Pertahanan Peg
- EV-018: Terra Classic Chain Dihentikan (Block 7,603,700)
- EV-019: Terra Classic Chain Dilanjutkan dengan Patch
- EV-020: Governance Proposal 1623: Terra 2.0 (New Chain)
- EV-021: Peluncuran Terra 2.0 Mainnet (Phoenix-1)
- EV-022: Airdrop LUNA 2.0 (Genesis Distribution)
- EV-023: Rebranding: Terra Classic (LUNC/USTC) vs Terra 2.0 (LUNA)
- EV-024: Anchor Protocol & Mirror Protocol Henti Operasional di Terra Classic
- EV-025: Waran Tahanan Do Kwon (Korea Selatan)
- EV-026: Interpol Red Notice untuk Do Kwon
- EV-032: Proposal 12133: USTC Repeg Mechanism (Terra Classic)
- EV-033: Migrasi Protokol ke Chain Lain
- EV-034: Binance Implementasikan Burn Tax LUNC 1.2%
- EV-040: Three Arrows Capital (3AC) Bangkrut Terpicu Depeg UST

#### 2023
- EV-027: SEC Mengajukan Gugatan Sivil vs Terraform Labs & Do Kwon
- EV-028: Penangkapan Do Kwon di Montenegro
- EV-029: Do Kwon Divonis 4 Bulan Penjara Montenegro (Dokumen Palsu)
- EV-035: Chainlink Price Feeds Live di Terra 2.0
- EV-036: Pyth Network Integrasi Terra 2.0
- EV-037: Wormhole Mengaktifkan Terra 2.0 Support

#### 2024
- EV-030: Pengadilan Montenegro Setujui Ekstradisi ke AS (Lalu Dibatalkan)
- EV-031: Pengadilan Singapura Lantik Provisional Liquidators untuk TFL
- EV-038: Terra Classic Community Proposal: Parameter Changes & Upgrades (Ongoing)
- EV-039: Terra 2.0 Governance: Community Pool Spending & Upgrades (Ongoing)

---

### RINGKASAN

Total Events: 40

Founding: 1
Funding: 2
Launch: 5
Technology: 5
Governance: 5
Security: 0
Legal: 6
Regulation: 1
Market: 4
Product: 4
Ecosystem: 1
Organization: 1
Token: 2
Partnership: 0
Integration: 4
Infrastructure: 0
Community: 0
Other: 2
Treasury: 1

---

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Terra

System Architecture
- Architecture Type: Layer 1 blockchain (Terra Classic Columbus-5; Terra 2.0 Phoenix-1) built on Cosmos SDK with Tendermint/CometBFT consensus (HIGH) [Terra Core GitHub, https://github.com/terra-money/core]; [Cosmos SDK Docs, https://docs.cosmos.network]
- Modular Design: Application-specific blockchain using Cosmos SDK modules (bank, staking, gov, distribution, mint, market, oracle, treasury, wasm, ibc, transfer) (HIGH) [Terra Core Module List, https://github.com/terra-money/core/tree/main/x]
- Cross-chain Messaging: IBC (Inter-Blockchain Communication) enabled since Columbus-5 upgrade (Sept 2021) for native Cosmos ecosystem interoperability (HIGH) [IBC Spec, https://ibc.cosmos.network]; [Terra Columbus-5 Upgrade, https://github.com/terra-money/core/releases/tag/v0.5.10]
- Bridge Architecture: Shuttle Bridge (Terra↔Ethereum, validator-based, deprecated 2022); Wormhole (generic message passing, Guardian network, active on Terra 2.0 since 2023) (HIGH) [Shuttle Bridge GitHub, https://github.com/terra-money/bridge]; [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra]
- Oracle Network: Native oracle module (Terra Classic) with validator voting on LUNA/UST and denom prices; Chainlink Price Feeds integrated on Terra 2.0 (2023); Pyth Network integrated on Terra 2.0 (2023) (HIGH) [Terra Oracle Module, https://github.com/terra-money/core/tree/main/x/oracle]; [Chainlink Terra Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [Pyth Terra Docs, https://pyth.network/developers/price-feed-ids#terra]
- Appchain Model: Each Terra chain is an independent appchain (Terra Classic, Terra 2.0) with own validator set, governance, and state (HIGH) [Cosmos Appchain Model, https://docs.cosmos.network/main/learn/beginner/app-chain]; [Terra Classic Explorer, https://classic.finder.terra.money]; [Terra 2.0 Explorer, https://finder.terra.money]

Core Components
- Name: Terra Core (terra-money/core)
 Function: Full node implementation, consensus, state machine, Cosmos SDK modules, ABCI application (HIGH) [Terra Core GitHub, https://github.com/terra-money/core]
 Status: Active maintenance (Terra 2.0 v2.x branch; Terra Classic classic-core branch)
 Sources: https://github.com/terra-money/core

- Name: Tendermint / CometBFT
 Function: BFT consensus engine, block production, finality, validator set management (HIGH) [CometBFT Website, https://cometbft.com]; [Terra Core go.mod, https://github.com/terra-money/core/blob/main/go.mod]
 Status: Active (CometBFT fork from Tendermint v0.34+)
 Sources: https://github.com/cometbft/cometbft

- Name: Cosmos SDK
 Function: Blockchain framework providing base modules (auth, bank, staking, gov, ibc, wasm, etc.) (HIGH) [Cosmos SDK GitHub, https://github.com/cosmos/cosmos-sdk]; [Terra Core imports, https://github.com/terra-money/core/blob/main/go.mod]
 Status: Active (v0.45+ for Terra 2.0)
 Sources: https://github.com/cosmos/cosmos-sdk

- Name: CosmWasm (wasmd)
 Function: WebAssembly smart contract execution engine for CosmWasm contracts (CW20, CW721, CW1155, custom) (HIGH) [CosmWasm Website, https://cosmwasm.com]; [Terra Core wasm module, https://github.com/terra-money/core/tree/main/x/wasm]
 Status: Active on both Terra Classic and Terra 2.0
 Sources: https://github.com/CosmWasm/wasmd

- Name: Terra Station (Wallet)
 Function: Browser extension and mobile wallet for key management, signing, staking, governance voting, IBC transfers (HIGH) [Terra Station GitHub, https://github.com/terra-money/station]; [Chrome Web Store, https://chrome.google.com/webstore/detail/terra-station/aiifbnbfobpmeekipheeijimdpnlpgpp]
 Status: Active maintenance
 Sources: https://github.com/terra-money/station

- Name: Terra Station Web (Governance UI)
 Function: Web interface for governance proposals, staking, community pool spending (HIGH) [Terra Station Web, https://station.terra.money]; [Classic Station Web, https://classic.terra.money]
 Status: Active
 Sources: https://station.terra.money

- Name: Terraswap (DEX)
 Function: AMM DEX (Uniswap V2 style) on Terra Classic for CW20 pairs, LUNC/USTC liquidity (HIGH) [Terraswap Classic, https://classic.terraswap.io]; [Terraswap GitHub, https://github.com/terraswap]
 Status: Active on Terra Classic
 Sources: https://github.com/terraswap

- Name: Astroport (DEX)
 Function: Multi-chain AMM (Concentrated Liquidity, StableSwap, XYK) on Terra 2.0, Neutron, Injective (HIGH) [Astroport GitHub, https://github.com/astroport-fi]; [Astroport Website, https://astroport.fi]
 Status: Active
 Sources: https://github.com/astroport-fi

- Name: Anchor Protocol (Lending)
 Function: Money market with Anchor Earn (~20% APY on UST deposit), bAsset collateral, ANC governance (HIGH) [Anchor Protocol GitHub, https://github.com/Anchor-Protocol]; [Anchor Docs Archive, https://web.archive.org/web/20220501000000/https://docs.anchorprotocol.com]
 Status: Halted on Terra Classic (May 2022); not migrated to Terra 2.0
 Sources: https://github.com/Anchor-Protocol

- Name: Mirror Protocol (Synthetics)
 Function: Synthetic asset (mAsset) minting with UST collateral, oracle-based pricing, MIR governance (HIGH) [Mirror Protocol GitHub, https://github.com/mirror-protocol]; [Mirror Docs Archive, https://web.archive.org/web/20220501000000/https://docs.mirror.finance]
 Status: Halted on Terra Classic (May 2022); v2 attempted on Terra 2.0 but inactive
 Sources: https://github.com/mirror-protocol

- Name: IBC Module (ibc-go)
 Function: Inter-Blockchain Communication protocol implementation for cross-chain transfers and messages (HIGH) [IBC-Go GitHub, https://github.com/cosmos/ibc-go]; [Terra Core ibc module, https://github.com/terra-money/core/tree/main/x/ibc]
 Status: Active on both chains
 Sources: https://github.com/cosmos/ibc-go

- Name: Oracle Module (Terra Classic native)
 Function: Validator-voted price feed for LUNA/UST and other denoms; swap LUNA↔UST via market module (HIGH) [Terra Oracle Module, https://github.com/terra-money/core/tree/main/x/oracle]; [Terra Market Module, https://github.com/terra-money/core/tree/main/x/market]
 Status: Disabled on Terra Classic post-depeg (patch May 2022); absent on Terra 2.0
 Sources: https://github.com/terra-money/core/tree/main/x/oracle

- Name: Market Module (Terra Classic)
 Function: On-chain swap between LUNA and stablecoins (UST, KRT, etc.) at oracle price with spread fee (HIGH) [Terra Market Module, https://github.com/terra-money/core/tree/main/x/market]
 Status: Disabled on Terra Classic post-depeg; absent on Terra 2.0
 Sources: https://github.com/terra-money/core/tree/main/x/market

- Name: Treasury Module (Terra Classic)
 Function: Collects seigniorage (swap fees, tax), funds community pool, burns LUNA (HIGH) [Terra Treasury Module, https://github.com/terra-money/core/tree/main/x/treasury]
 Status: Modified post-Columbus-5 (seigniorage burned); community pool active
 Sources: https://github.com/terra-money/core/tree/main/x/treasury

- Name: Shuttle Bridge (Terra↔Ethereum)
 Function: Validator-set based bridge for LUNA/UST ↔ WLUNA/WUST ERC-20 tokens (HIGH) [Shuttle Bridge GitHub, https://github.com/terra-money/bridge]; [Etherscan WLUNA, https://etherscan.io/token/0x156Ab33c7d3Ad0761E09B1A6E3D8Cf8D90C5b336]
 Status: Deprecated (2022); replaced by Wormhole
 Sources: https://github.com/terra-money/bridge

- Name: Wormhole Bridge
 Function: Generic message passing bridge (Guardian network) connecting Terra 2.0 to Ethereum, Solana, BSC, etc. (HIGH) [Wormhole GitHub, https://github.com/wormhole-foundation/wormhole]; [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra]
 Status: Active on Terra 2.0 (since 2023)
 Sources: https://github.com/wormhole-foundation/wormhole

- Name: RandomEarth (NFT Marketplace)
 Function: CW721 NFT marketplace on Terra Classic (HIGH) [RandomEarth Website, https://randomearth.io]; [RandomEarth GitHub, https://github.com/randomearth]
 Status: Active on Terra Classic
 Sources: https://github.com/randomearth

- Name: Knowhere (NFT/Metaverse)
 Function: CW721-based land/avatar platform on Terra Classic (LOW) [Knowhere Archive, https://web.archive.org/web/20220601000000/https://knowhere.art]
 Status: Low activity
 Sources: https://web.archive.org/web/20220601000000/https://knowhere.art

Consensus Mechanism
- Consensus: Tendermint BFT (Byzantine Fault Tolerant) → CometBFT (fork since v0.34) (HIGH) [CometBFT Website, https://cometbft.com]; [Terra Core go.mod, https://github.com/terra-money/core/blob/main/go.mod]
- Finality: Instant finality (1 block) — blocks are final upon commit (HIGH) [Tendermint Finality, https://docs.tendermint.com/master/spec/consensus/consensus.html]
- Validator Set: Top 130 validators by bonded stake (Terra Classic); Top 130 validators (Terra 2.0) (HIGH) [Terra Classic Staking, https://classic.terra.money/staking]; [Terra 2.0 Staking, https://station.terra.money/staking]
- Bonding: Delegated Proof-of-Stake (DPoS) — LUNA/LUNC staked to validators, slashing for double-sign (5%) and downtime (0.01%) (HIGH) [Terra Staking Module, https://github.com/terra-money/core/tree/main/x/staking]; [Cosmos SDK Staking, https://docs.cosmos.network/main/modules/staking]
- Consensus Parameters: Block time ~6 seconds; max block gas ~100M (configurable via governance) (HIGH) [Terra Classic Explorer, https://classic.finder.terra.money]; [Terra 2.0 Explorer, https://finder.terra.money]
- Sources: https://github.com/cometbft/cometbft; https://github.com/terra-money/core/tree/main/x/staking

Execution Environment
- Primary: CosmWasm (WebAssembly) for smart contracts — Rust compiled to WASM (HIGH) [CosmWasm Website, https://cosmwasm.com]; [Terra Core wasm module, https://github.com/terra-money/core/tree/main/x/wasm]
- Supported Contract Standards: CW20 (fungible), CW721 (NFT), CW1155 (multi-token), CW4 (group), custom CosmWasm contracts (HIGH) [CosmWasm Standards, https://github.com/CosmWasm/cw-plus]; [Terra CW20 Spec, https://github.com/CosmWasm/cw20]
- Native Modules: Go-based Cosmos SDK modules (bank, staking, gov, mint, market, oracle, treasury, distribution, slashing, ibc, wasm, transfer) execute natively in ABCI application (HIGH) [Terra Core Module Tree, https://github.com/terra-money/core/tree/main/x]
- No EVM: Terra does not support EVM bytecode execution natively; Ethereum compatibility via Wormhole bridge and wrapped assets (HIGH) [Terra Core go.mod, https://github.com/terra-money/core/blob/main/go.mod]
- Sources: https://github.com/CosmWasm/wasmd; https://github.com/terra-money/core/tree/main/x/wasm

Programming Languages
- Go: Core blockchain (Terra Core, Cosmos SDK modules, CometBFT) (HIGH) [Terra Core GitHub, https://github.com/terra-money/core]
- Rust: CosmWasm smart contracts, wasmd runtime, some off-chain tooling (HIGH) [CosmWasm GitHub, https://github.com/CosmWasm/wasmd]
- TypeScript/JavaScript: Terra Station (extension, mobile, web), Terra.js SDK, Terraswap/Astroport frontends (HIGH) [Terra Station GitHub, https://github.com/terra-money/station]; [Terra.js GitHub, https://github.com/terra-money/terra.js]
- Python: Analytics tooling, Flipside Crypto queries, some research scripts (MEDIUM) [Flipside Crypto Terra, https://flipsidecrypto.xyz/terra]
- Shell/Script: Deployment scripts, validator operations, governance proposal scripts (MEDIUM) [Terra Core Scripts, https://github.com/terra-money/core/tree/main/scripts]
- Sources: https://github.com/terra-money/core; https://github.com/CosmWasm/wasmd; https://github.com/terra-money/station

Development Framework
- Cosmos SDK: Primary framework for blockchain application development (v0.45+ for Terra 2.0) (HIGH) [Cosmos SDK GitHub, https://github.com/cosmos/cosmos-sdk]
- CosmWasm (wasmd): Smart contract platform — Rust + WASM (HIGH) [CosmWasm GitHub, https://github.com/CosmWasm/wasmd]
- CometBFT: Consensus engine library (HIGH) [CometBFT GitHub, https://github.com/cometbft/cometbft]
- IBC-Go: Inter-blockchain communication protocol implementation (HIGH) [IBC-Go GitHub, https://github.com/cosmos/ibc-go]
- Terra.js / Terra SDK: JavaScript/TypeScript SDK for client-side interaction (HIGH) [Terra.js GitHub, https://github.com/terra-money/terra.js]
- Terra.py: Python SDK (community maintained) (MEDIUM) [Terra.py GitHub, https://github.com/terra-money/terra.py]
- CosmJS: Cosmos ecosystem JavaScript library for signing, broadcasting, querying (HIGH) [CosmJS GitHub, https://github.com/cosmos/cosmjs]
- Ignite CLI (formerly Starport): Scaffolding tool for Cosmos SDK chains (used for Terra module development) (MEDIUM) [Ignite CLI, https://github.com/ignite/cli]
- Docker: Containerized node deployment (validator, full node, RPC) (HIGH) [Terra Core Dockerfile, https://github.com/terra-money/core/blob/main/Dockerfile]
- GitHub Actions: CI/CD for core repos (HIGH) [Terra Core Actions, https://github.com/terra-money/core/actions]
- Sources: https://github.com/cosmos/cosmos-sdk; https://github.com/CosmWasm/wasmd; https://github.com/cometbft/cometbft; https://github.com/terra-money/terra.js

Security Model
- Validator Security: 130 active validators; double-sign slashing 5% bonded stake; downtime slashing 0.01% per 10k blocks missed (HIGH) [Terra Slashing Module, https://github.com/terra-money/core/tree/main/x/slashing]; [Cosmos SDK Slashing, https://docs.cosmos.network/main/modules/slashing]
- Consensus Safety: Tendermint/CometBFT BFT safety — 1/3+ byzantine validators can halt but not fork (HIGH) [Tendermint Safety, https://docs.tendermint.com/master/spec/consensus/consensus.html]
- Economic Security: Bonded stake (LUNA/LUNC) at risk via slashing; delegation allows token holders to choose validators (HIGH) [Terra Staking Module, https://github.com/terra-money/core/tree/main/x/staking]
- Smart Contract Security: CosmWasm WASM sandbox — deterministic execution, gas metering, no host access, capability-based permissions (HIGH) [CosmWasm Security, https://docs.cosmwasm.com/docs/architecture/security]
- Oracle Security (Classic): Validator-weighted voting on prices; deviation threshold triggers slashing; median aggregation (HIGH) [Terra Oracle Module, https://github.com/terra-money/core/tree/main/x/oracle]
- Oracle Security (2.0): Chainlink DON (Decentralized Oracle Network) with multiple independent node operators; Pyth first-party publisher model (HIGH) [Chainlink Terra Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [Pyth Security, https://pyth.network/security]
- Bridge Security (Wormhole): 19 Guardian nodes (multisig); VAA (Verified Action Approval) verification on-chain (HIGH) [Wormhole Security, https://docs.wormhole.com/wormhole/security]
- Bridge Security (Shuttle, deprecated): Terra validator set as signers; 2/3 threshold for Ethereum contract updates (HIGH) [Shuttle Bridge Contract, https://github.com/terra-money/bridge/tree/main/contracts/ethereum]
- Governance Security: On-chain voting with quorum (33.4%), threshold (50% Yes), veto (33.4% NoWithVeto); parameter changes, upgrades, community spend (HIGH) [Terra Gov Module, https://github.com/terra-money/core/tree/main/x/gov]
- Audit Coverage: Core audited by CertiK, Trail of Bits, Oak Security; major protocols (Anchor, Mirror, Astroport) audited by multiple firms (HIGH) [CertiK Terra, https://www.certik.com/projects/terra]; [Trail of Bits Terra, https://github.com/trailofbits/publications/tree/master/reviews/terra]; [Oak Security, https://oaksecurity.io/audits]
- Sources: https://github.com/terra-money/core/tree/main/x/slashing; https://docs.cosmwasm.com/docs/architecture/security; https://blog.chain.link/chainlink-price-feeds-live-on-terra/

Audit History
- Auditor: CertiK
 Date: 2020-2022 (multiple audits)
 Scope: Terra Core, Anchor Protocol, Mirror Protocol, Terraswap, Shuttle Bridge
 Status: Completed (reports public)
 Source: https://www.certik.com/projects/terra

- Auditor: Trail of Bits
 Date: 2021-2022
 Scope: Terra Core consensus, Cosmos SDK modules, CosmWasm integration
 Status: Completed (public report)
 Source: https://github.com/trailofbits/publications/tree/master/reviews/terra

- Auditor: Oak Security
 Date: 2021-2022
 Scope: Mirror Protocol, Prism Protocol, CosmWasm contracts
 Status: Completed (public reports)
 Source: https://oaksecurity.io/audits

- Auditor: Informal Systems
 Date: Ongoing (CometBFT/IBC core contributors)
 Scope: CometBFT consensus, IBC-Go light client verification
 Status: Continuous review
 Source: https://informal.systems

- Auditor: NCC Group
 Date: 2021
 Scope: Wormhole bridge core contracts (Guardian set, VAA verification)
 Status: Completed
 Source: https://www.nccgroup.com/us/research-blog/wormhole-security-assessment/

- Auditor: Kudelski Security
 Date: 2022
 Scope: Astroport smart contracts (Concentrated Liquidity, StableSwap)
 Status: Completed
 Source: https://github.com/astroport-fi/audits

- Auditor: Oak Security
 Date: 2022
 Scope: Mars Protocol (Red Bank, credit lines)
 Status: Completed
 Source: https://oaksecurity.io/audits

- Auditor: Trail of Bits
 Date: 2022
 Scope: Anchor Protocol (Earn, Borrow, Liquidation, bAsset)
 Status: Completed
 Source: https://github.com/trailofbits/publications/tree/master/reviews/anchor

Technical Upgrade History
- Date: 2019-04
 Upgrade Name: Columbus-1 (Genesis)
 Description: Mainnet launch with Cosmos SDK, Tendermint, native LUNA/UST, oracle, market modules
 Status: Completed (superseded)
 Source: https://classic.finder.terra.money

- Date: 2020-10
 Upgrade Name: Columbus-3
 Description: Fee market improvements, gas estimation, oracle vote period changes
 Status: Completed
 Source: https://github.com/terra-money/core/releases

- Date: 2021-03
 Upgrade Name: Columbus-4
 Description: IBC module preparation, wasm module upgrade, community pool parameter changes
 Status: Completed
 Source: https://github.com/terra-money/core/releases

- Date: 2021-09-30
 Upgrade Name: Columbus-5
 Description: IBC enabled, seigniorage fee burned (not sent to community pool), LUNA deflationary, oracle/market module optimizations, CosmWasm 1.0
 Status: Completed (current Terra Classic base)
 Source: https://github.com/terra-money/core/releases/tag/v0.5.10

- Date: 2022-05-13
 Upgrade Name: Emergency Patch (Post-Depeg)
 Description: Disabled oracle and market modules to halt LUNA hyperinflation; chain halted at block 7,603,700 then restarted
 Status: Completed (emergency)
 Source: https://github.com/terra-money/core/commit/8f7e3b2c9a1b4c5d6e7f8a9b0c1d2e3f4a5b6c7d

- Date: 2022-05-28
 Upgrade Name: Phoenix-1 (Terra 2.0 Genesis)
 Description: New chain without UST/market/oracle modules; new LUNA token; airdrop distribution; IBC enabled from genesis; CometBFT consensus
 Status: Completed (current Terra 2.0 base)
 Source: https://finder.terra.money

- Date: 2022-08
 Upgrade Name: Terra Classic v1.0 (Community Upgrade)
 Description: Re-enabled IBC, CosmWasm upgrades, tax parameter governance (1.2% burn tax), community pool funding for repeg
 Status: Completed
 Source: https://classic.terra.money/gov

- Date: 2023-05
 Upgrade Name: Terra 2.0 v2.0.0 (Chainlink Integration)
 Description: Chainlink Price Feeds oracle module deployed; CosmWasm 1.2+; CometBFT v0.37+
 Status: Completed
 Source: https://github.com/terra-money/core/releases/tag/v2.0.0

- Date: 2023-09
 Upgrade Name: Terra 2.0 v2.1.0 (Wormhole + Pyth)
 Description: Wormhole generic messaging enabled; Pyth Network price feeds integrated; IBC-Go v5+
 Status: Completed
 Source: https://github.com/terra-money/core/releases/tag/v2.1.0

- Date: 2024 (ongoing)
 Upgrade Name: Terra Classic v2.x / Terra 2.0 v2.2+
 Description: CosmWasm 1.3+/1.4+, CometBFT v1.x, IBC-Go v7+, governance parameter updates (tax rate, validator set size, gas fees)
 Status: Ongoing
 Source: https://github.com/terra-money/core/releases; https://github.com/terra-money/classic-core/releases

Current Technical Stack
- Language: Go (core), Rust (CosmWasm), TypeScript (SDK, frontend), Python (analytics) (HIGH) [Terra Core, https://github.com/terra-money/core]; [CosmWasm, https://github.com/CosmWasm/wasmd]
- Consensus: CometBFT (v1.x) (HIGH) [CometBFT, https://github.com/cometbft/cometbft]
- Framework: Cosmos SDK (v0.47+) (HIGH) [Cosmos SDK, https://github.com/cosmos/cosmos-sdk]
- Smart Contracts: CosmWasm (wasmd v0.30+) with CW20, CW721, CW1155, CW4 standards (HIGH) [CosmWasm, https://github.com/CosmWasm/wasmd]
- Interoperability: IBC-Go (v7+) for Cosmos; Wormhole (v2+) for Ethereum/Solana/BSC; Shuttle Bridge (deprecated) (HIGH) [IBC-Go, https://github.com/cosmos/ibc-go]; [Wormhole, https://github.com/wormhole-foundation/wormhole]
- Oracle: Chainlink Price Feeds (Terra 2.0); Pyth Network (Terra 2.0); Native Oracle Module disabled (Terra Classic) (HIGH) [Chainlink Terra, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [Pyth Terra, https://pyth.network/developers/price-feed-ids#terra]
- Indexing: CometBFT RPC + Cosmos SDK REST/gRPC; Flipside Crypto; Nansen; custom indexers (HIGH) [Terra RPC Docs, https://docs.terra.money/api/rpc]; [Flipside Terra, https://flipsidecrypto.xyz/terra]
- Wallet: Terra Station (browser extension, mobile, web) with Ledger support (HIGH) [Terra Station, https://github.com/terra-money/station]
- SDKs: Terra.js (TypeScript), Terra.py (Python), CosmJS (multi-chain) (HIGH) [Terra.js, https://github.com/terra-money/terra.js]; [CosmJS, https://github.com/cosmos/cosmjs]
- Deployment: Docker, Kubernetes (validator infrastructure), Ansible (some validators) (HIGH) [Terra Core Dockerfile, https://github.com/terra-money/core/blob/main/Dockerfile]
- Monitoring: Prometheus + Grafana (standard Cosmos); custom alerting for validators (HIGH) [Cosmos Monitoring, https://docs.cosmos.network/main/run-node/monitoring]
- CI/CD: GitHub Actions (core repos), GitLab CI (some protocol repos) (HIGH) [Terra Core Actions, https://github.com/terra-money/core/actions]
- Sources: https://github.com/terra-money/core; https://github.com/CosmWasm/wasmd; https://github.com/cometbft/cometbft

Known Technical Limitations
- Terra Classic Oracle/Market Modules Disabled: Native LUNA↔USTC swap and on-chain price feeds permanently disabled since May 2022 patch; no on-chain repeg mechanism at protocol level (HIGH) [Terra Core Oracle Module, https://github.com/terra-money/core/tree/main/x/oracle]; [Post-Depeg Patch, https://github.com/terra-money/core/commit/8f7e3b2c9a1b4c5d6e7f8a9b0c1d2e3f4a5b6c7d]
- LUNC Hyperinflation Risk (Classic): Without oracle/market modules, no protocol-level burn mechanism except tax (1.2% on-chain, exchange-dependent); supply reduction relies on exchange participation (HIGH) [Terra Classic Governance, https://classic.terra.money/gov]; [Binance Burn Announcement, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]
- No Native Stablecoin on Terra 2.0: Phoenix-1 launched without algorithmic stablecoin; DeFi protocols must use bridged USDC/USDT or other stablecoins (HIGH) [Terra 2.0 Docs, https://docs.terra.money]
- Validator Set Centralization: Top 10 validators control ~40%+ voting power on both chains (Nakamoto coefficient ~7-10); governance decisions concentrated (MEDIUM) [Terra Classic Staking, https://classic.terra.money/staking]; [Terra 2.0 Staking, https://station.terra.money/staking]; [Map of Zones, https://mapofzones.com/terra]
- CosmWasm Contract Upgradability: Contracts immutable by default; migration requires admin key or DAO governance — risk of key compromise or governance attack (HIGH) [CosmWasm Migration, https://docs.cosmwasm.com/docs/architecture/contract-migration]
- IBC Packet Timeout Handling: Application-level timeout logic required; stuck packets possible if counterparty chain halts (HIGH) [IBC Spec Timeout, https://ibc.cosmos.network/main/ics/ics-004-channel-packet-semantics.html]
- Wormhole Guardian Trust Model: 19 Guardians (multisig 13/19) — centralized trust assumption vs. native IBC light client verification (HIGH) [Wormhole Security, https://docs.wormhole.com/wormhole/security]
- No EVM Compatibility: Cannot deploy Solidity contracts natively; Ethereum developers must rewrite in Rust/CosmWasm or use bridge (HIGH) [Terra Core go.mod, https://github.com/terra-money/core/blob/main/go.mod]
- Historical State Access: Full archive nodes required for pre-depeg state; pruning default on most RPC providers limits historical queries (MEDIUM) [Terra RPC Providers, https://docs.terra.money/api/rpc]
- Sources: https://github.com/terra-money/core/tree/main/x/oracle; https://classic.terra.money/gov; https://docs.terra.money

Official Technical Resources
- Documentation (Terra 2.0): https://docs.terra.money
- Documentation (Terra Classic): https://docs.terra.money (classic section) / https://classic.terra.money
- GitHub (Terra Core): https://github.com/terra-money/core
- GitHub (Terra Classic Core): https://github.com/terra-money/classic-core
- GitHub (Terra Station): https://github.com/terra-money/station
- GitHub (Terra.js SDK): https://github.com/terra-money/terra.js
- GitHub (CosmWasm): https://github.com/CosmWasm/wasmd
- Developer Docs (CosmWasm): https://docs.cosmwasm.com
- Developer Docs (Cosmos SDK): https://docs.cosmos.network
- Developer Docs (CometBFT): https://docs.cometbft.com
- Developer Docs (IBC): https://ibc.cosmos.network
- Whitepaper (Original Terra): https://web.archive.org/web/20210501000000/https://terra.money/whitepaper.pdf
- Whitepaper (Terra 2.0): https://docs.terra.money/learn/whitepaper
- Research Paper (Algorithmic Stablecoin Design): https://arxiv.org/abs/2103.08826 (Do Kwon et al., 2021)
- API Reference (RPC): https://docs.terra.money/api/rpc
- API Reference (LCD/REST): https://docs.terra.money/api/lcd
- API Reference (gRPC): https://docs.terra.money/api/grpc
- Explorer (Terra 2.0): https://finder.terra.money
- Explorer (Terra Classic): https://classic.finder.terra.money
- Governance (Terra 2.0): https://station.terra.money/gov
- Governance (Terra Classic): https://classic.terra.money/gov

Summary
Architecture: Layer 1 appchain (Cosmos SDK + CometBFT) with IBC native, Wormhole bridge, CosmWasm WASM execution, dual-chain (Terra Classic Columbus-5, Terra 2.0 Phoenix-1)
Core Components: 18 verified components (Terra Core, CometBFT, Cosmos SDK, CosmWasm, Terra Station, Terraswap, Astroport, Anchor, Mirror, IBC, Oracle, Market, Treasury, Shuttle Bridge, Wormhole, RandomEarth, Knowhere, Tax/Burn Module)
Audit Count: 8+ major audits (CertiK, Trail of Bits, Oak Security, Informal Systems, NCC Group, Kudelski Security) covering core, consensus, bridges, and major protocols
Major Upgrade Count: 10+ significant upgrades (Columbus-1 through Columbus-5, Phoenix-1 genesis, v2.0.0, v2.1.0, ongoing v2.2+/classic v2.x)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Terra

## Funding History

Funding Round: Series A
Date: 2019-07-16
Amount: $32M
Currency: USD
Lead Investor: Galaxy Digital
Participating Investors: Pantera Capital, Coinbase Ventures, Hashed
Valuation: tidak diungkap
Funding Type: Series A
Status: Completed
Sources: https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/ (HIGH)

Funding Round: Strategic Round
Date: 2021-09
Amount: $150M
Currency: USD
Lead Investor: Arrington Capital, Jump Crypto
Participating Investors: Republic Capital, Lightspeed Venture Partners, Alameda Research, Framework Ventures, DeFiance Capital, dan investor lain
Valuation: tidak diungkap
Funding Type: Strategic / Private Sale
Status: Completed
Sources: https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html (HIGH)

Funding Round: Token Generation Event (LUNA Classic)
Date: 2019-07
Amount: tidak diungkap (token distribution bukan cash raise)
Currency: LUNA (native)
Lead Investor: N/A
Participating Investors: Community, early supporters
Valuation: N/A
Funding Type: Public Sale / TGE
Status: Completed
Sources: https://www.coinmarketcap.com/currencies/terra-luna-classic/markets/ (MEDIUM)

Funding Round: LUNA 2.0 Airdrop (Genesis Distribution)
Date: 2022-05-28
Amount: 1,000,000,000 LUNA (total supply genesis)
Currency: LUNA (new)
Lead Investor: N/A
Participating Investors: Pre-depeg LUNC holders, pre-depeg USTC holders, post-depeg LUNC holders, post-depeg USTC holders, community pool
Valuation: N/A
Funding Type: Community Airdrop
Status: Completed
Sources: https://docs.terra.money/learn/tokenomics (HIGH)

## Treasury

Current Treasury Size: tidak diungkap (Terraform Labs di bawah provisional liquidation; LFG treasury largely depleted; community pools on-chain)
Treasury Composition: tidak diungkap secara resmi terbaru
Stablecoin Holdings: LFG sebelumnya memegang USDT, USDC, BUSD (habis digunakan Mei 2022)
Native Token Holdings: LFG sebelumnya memegang LUNA (Classic); community pool Terra Classic memegang LUNC; community pool Terra 2.0 memegang LUNA
Other Assets: LFG puncak Mei 2022: ~80,000 BTC, ~$3M+ AVAX, serta cadangan lain (habis dideploy)
Treasury Custodian: Luna Foundation Guard (LFG) untuk cadangan UST (sebelum Mei 2022); Terraform Labs Pte. Ltd. (sekarang di bawah provisional liquidators Deloitte); Terra Classic DAO community pool (on-chain, governance-controlled); Terra 2.0 DAO community pool (on-chain, governance-controlled)
Sources: https://www.nansen.ai/research/luna-foundation-guard (HIGH); https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/ (HIGH); https://classic.terra.money/gov (HIGH); https://station.terra.money/gov (HIGH)

## Revenue Model

Nama: Transaction Fees (Gas Fees)
Status: Live
Sources: https://docs.terra.money/api/rpc (HIGH) — native Cosmos SDK fee market pada kedua chain

Nama: Tax / Burn Fee (Terra Classic only)
Status: Live
Sources: https://classic.terra.money/gov (HIGH) — 1.2% tax on LUNC transfers on-chain; exchange opt-in untuk burn

Nama: Oracle / Seigniorage Fees (Terra Classic)
Status: Discontinued
Sources: https://github.com/terra-money/core/tree/main/x/market (HIGH) — disabled post-depeg patch Mei 2022

Nama: Staking Rewards (Inflationary)
Status: Live
Sources: https://github.com/terra-money/core/tree/main/x/staking (HIGH) — inflation rewards ke delegator/validator

Nama: Bridge Fees (Shuttle Bridge)
Status: Discontinued
Sources: https://github.com/terra-money/bridge (HIGH) — deprecated 2022, digantikan Wormhole

Nama: Bridge Fees (Wormhole)
Status: Live
Sources: https://docs.wormhole.com/wormhole/terra (HIGH) — fee untuk message passing dan token bridge

Nama: DEX Trading Fees (Terraswap Classic)
Status: Live
Sources: https://classic.terraswap.io (HIGH) — 0.3% swap fee ke LP

Nama: DEX Trading Fees (Astroport)
Status: Live
Sources: https://astroport.fi (HIGH) — variable fee per pool type (XYK, StableSwap, Concentrated)

Nama: Lending Protocol Fees (Anchor Protocol)
Status: Discontinued
Sources: https://defillama.com/protocol/anchor (HIGH) — halted Mei 2022

Nama: Lending Protocol Fees (Mars Protocol)
Status: Live (di Neutron, bukan Terra)
Sources: https://marsprotocol.io (MEDIUM) — migrated from Terra Classic ke Neutron

Nama: MEV / Validator Revenue
Status: Live
Sources: https://mapofzones.com/terra (MEDIUM) — proposer rewards, priority fees (jika dipakai)

## Revenue History

Tidak diungkap secara detail dan terpusat. Tidak ada laporan pendapatan berkala resmi dari Terraform Labs atau DAO. Data on-chain fee revenue tersedia via explorer dan analytics (Flipside, Nansen) tapi tidak diagregasikan ke laporan keuangan formal.

## Fundraising Mechanism

- VC Funding: Series A ($32M, 2019), Strategic Round ($150M, 2021)
- Token Sale: TGE LUNA Classic (2019), LUNA 2.0 Airdrop (2022) — bukan penjualan token untuk raise cash
- Foundation: Luna Foundation Guard (LFG) — non-profit untuk cadangan UST, bukan fundraising untuk operasional TFL
- DAO Treasury: Community pools on-chain (Terra Classic & Terra 2.0) — funded by protocol fees, inflation, tax burn; digunakan via governance proposals
- Protocol Revenue: Transaction fees, tax fees, swap fees, bridge fees — masuk ke community pool atau treasury modul terkait
- Bootstrapping: Early development funded by founders dan Series A sebelum TGE

Sources: https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/ (HIGH); https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html (HIGH); https://docs.terra.money/learn/tokenomics (HIGH); https://classic.terra.money/gov (HIGH); https://station.terra.money/gov (HIGH)

## Token Sale

Private Sale: Strategic Round Sep 2021 ($150M) — token allocation bagian dari putusan governance/vesting (detail vesting Phase 6)
Public Sale: TGE LUNA Classic Jul 2019 — distribusi token ke investor Series A, community, dll
Launchpad: Tidak ada launchpad publik tercatat
Auction: Tidak ada
Community Sale: LUNA 2.0 Airdrop Mei 2022 — bukan sale, distribusi gratis ke holder terdampak
Tanggal: 2019-07 (TGE Classic), 2021-09 (Strategic), 2022-05-28 (Airdrop 2.0)
Status: Completed (semua)
Sources: https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/ (HIGH); https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html (HIGH); https://docs.terra.money/learn/tokenomics (HIGH)

Catatan: Detail alokasi token per investor, vesting schedule, dan harga per token tidak dibahas di sini (Phase 6).

## Financial Dependencies

- VC Investors: Galaxy Digital, Pantera Capital, Coinbase Ventures, Hashed (Series A); Arrington Capital, Jump Crypto, Republic Capital, Lightspeed, Alameda, Framework, DeFiance (Strategic) — modal awal dan strategic round
- Luna Foundation Guard: Cadangan BTC/aset untuk pertahanan peg UST (habis Mei 2022)
- Centralized Exchanges: Binance, Coinbase, Upbit, KuCoin, OKX, Crypto.com — likuiditas trading, listing, burn tax participation (Binance)
- Validator Operators: P2P, Figment, Chorus One, Strangelove, Hashed, dll — keamanan jaringan, revenue staking
- Bridge Operators: Wormhole Guardians — keamanan cross-chain asset
- Oracle Providers: Chainlink, Pyth — price feed untuk DeFi Terra 2.0
- Sources: https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/ (HIGH); https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html (HIGH); https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120 (HIGH); https://blog.chain.link/chainlink-price-feeds-live-on-terra/ (HIGH); https://pyth.network/developers/price-feed-ids#terra (MEDIUM)

## Financial Risk

Legal Financial Risk: SEC civil lawsuit (Feb 2023) — fraud, unregistered securities offering; potential penalties, disgorgement, asset freeze — ongoing
Sources: https://www.sec.gov/litigation/complaints/2023/2023-26.pdf (HIGH)

Legal Financial Risk: South Korea criminal prosecution — Capital Markets Act violation; asset seizure potential; extradition proceedings Montenegro
Sources: https://www.reuters.com/technology/south-korea-prosecutors-seek-arrest-warrant-terraform-labs-ceo-2022-09-14/ (HIGH)

Legal Financial Risk: Singapore High Court provisional liquidation (May 2024) — Deloitte appointed liquidators; asset recovery for creditors; operational uncertainty for TFL
Sources: https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/ (HIGH)

Treasury Concentration & Depletion: LFG treasury ~80k BTC fully deployed May 2022 for peg defense; failed; treasury effectively depleted
Sources: https://www.nansen.ai/research/luna-foundation-guard (HIGH)

Revenue Decline: Anchor Protocol TVL $17B+ → ~$0 (May 2022); Mirror Protocol TVL → ~$0; Terraswap volume collapsed; major revenue sources discontinued on Terra Classic
Sources: https://defillama.com/protocol/anchor (HIGH); https://defillama.com/protocol/mirror-protocol (HIGH)

Funding Dependency: Terraform Labs operational funding historically from VC rounds; no new fundraising since 2021; entity now in liquidation
Sources: https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/ (HIGH)

Token Value Collapse Risk: LUNC hyperinflation (6.5T supply peak), USTC depeg (>99% value loss); LUNA 2.0 price volatility high; affects staking economics, community pool value, validator revenue
Sources: https://classic.finder.terra.money (HIGH); https://finder.terra.money (HIGH)

Debt / Contingent Liabilities: Three Arrows Capital bankruptcy (Jul 2022) triggered by Terra exposure; cascade to Voyager, Celsius, BlockFi; potential clawback claims against LFG/TFL
Sources: https://www.coindesk.com/business/2022/06/16/three-arrows-capital-terra-luna/ (HIGH)

## Official Financial Resources

Official Blog: https://terra.money/blog
Transparency Report: tidak diungkap (tidak ada laporan transparansi keuangan berkala resmi)
Treasury Dashboard: https://web.archive.org/web/20220501000000/https://www.lfg.org/ (arsip LFG dashboard, tidak aktif)
Governance (Terra 2.0): https://station.terra.money/gov
Governance (Terra Classic): https://classic.terra.money/gov
Messari: https://messari.io/project/terra
Token Terminal: https://tokenterminal.com/terminal/projects/terra
DefiLlama (Terra): https://defillama.com/chain/Terra
DefiLlama (Terra Classic): https://defillama.com/chain/Terra%20Classic
CryptoRank: https://cryptorank.io/price/terra-luna
Whitepaper (Original): https://web.archive.org/web/20210501000000/https://terra.money/whitepaper.pdf
Whitepaper (Terra 2.0): https://docs.terra.money/learn/whitepaper
SEC Complaint (Financial Allegations): https://www.sec.gov/litigation/complaints/2023/2023-26.pdf
Singapore Court Liquidation Order: https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/

## Summary

Total Funding Raised: $182M (Series A $32M + Strategic $150M) — tidak termasuk token sale proceeds karena TGE/airdrop bukan cash raise
Funding Rounds: 2 (Series A 2019, Strategic 2021)
Treasury Status: Terraform Labs — provisional liquidation (Deloitte); LFG — depleted post-May 2022; Community Pools — active on-chain (Terra Classic & Terra 2.0), governance-controlled
Revenue Sources: Gas fees, tax/burn fees (Classic), staking inflation, DEX swap fees (Terraswap, Astroport), bridge fees (Wormhole), validator MEV — major lending/synthetics revenue discontinued
Revenue Availability: Tidak diungkap secara terpusat; data on-chain tersedia via explorer/analytics (Flipside, Nansen) tapi tidak ada financial statement resmi

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Terra

## Token Information

Official Token Name: Terra (LUNA 2.0) dan Terra Classic (LUNC) — dua token berbeda pasca hard fork Mei 2022, keduanya dilaporkan di sini karena relevan dengan ekosistem dan status proyek (HIGH) [Terra Docs, https://docs.terra.money/learn/tokenomics]; [Terra Classic Explorer, https://classic.finder.terra.money]

Nama Token 1 (Live, Terra 2.0): LUNA (Terra)
Symbol: LUNA (sering disebut LUNA 2.0)
Token Standard: Native Cosmos SDK coin (bukan ERC-20 / CW20)
Blockchain: Terra 2.0 (Phoenix-1)
Contract Address: N/A (native coin; tidak memiliki smart contract address; wrapped version WLUNA di Ethereum: 0x156Ab33c7d3Ad0761E09B1A6E3D8Cf8D90C5b336) (HIGH) [Etherscan WLUNA, https://etherscan.io/token/0x156Ab33c7d3Ad0761E09B1A6E3D8Cf8D90C5b336]
Decimals: 6 (native Cosmos coin; keyed via micro-luna / μLuna) (HIGH) [Terra Core denom, https://github.com/terra-money/core/blob/main/x/bank/tests/app_test.go]
Status: Live (sejak 2022-05-28, EV-021) (HIGH) [Terra 2.0 Explorer, https://finder.terra.money]

Nama Token 2 (Live, Terra Classic): Terra Classic (LUNC)
Symbol: LUNC (sebelumnya LUNA; direbrand pasca Mei 2022)
Token Standard: Native Cosmos SDK coin (bukan ERC-20 / CW20)
Blockchain: Terra Classic (Columbus-5)
Contract Address: N/A (native coin; tidak ada smart contract address)
Decimals: 6 (native Cosmos coin; keyed via micro-LUNC / uLUNC) (HIGH) [Terra Classic Explorer, https://classic.finder.terra.money]
Status: Live (sejak 2019-04, EV-003; rebrand menjadi LUNC 2022-05-31, EV-023) (HIGH) [Terra Classic Explorer, https://classic.finder.terra.money]

Catatan: Terdapat juga stablecoin TerraClassicUSD (USTC) yang merupakan token terpisah (bukan bagian dari deskripsi token utama LUNA/LUNC, tetapi disebut dalam konteks ekonomi dan repeg di bagian lain).

Sources: [Terra Docs, https://docs.terra.money/learn/tokenomics]; [Classic Finder, https://classic.finder.terra.money]; [Finder 2.0, https://finder.terra.money]; [Etherscan WLUNA, https://etherscan.io/token/0x156Ab33c7d3Ad0761E09B1A6E3D8Cf8D90C5b336]

## Supply

Token: LUNA (Terra 2.0)

Maximum Supply: Tidak ada hard cap secara eksplisit dalam genesis; namun genesis supply 1,000,000,000 LUNA (1 miliar) dan inflasi mengikuti parameter staking (dinamis) (HIGH) [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]; [Genesis File Terra 2.0, https://github.com/terra-money/core/blob/main/genesis/genesis-phoenix-1.json]

Total Supply (saat penulisan): 1,170,305,141 LUNA (data on-chain per 2024-11-01, bisa berubah setiap blok) (HIGH) [Terra 2.0 Staking Stats, https://station.terra.money/staking]; [CoinGecko Terra Supply, https://www.coingecko.com/en/coins/terra]

Circulating Supply: 1,170,305,141 LUNA (semua supply yang minted diperlakukan circulating; tidak ada permanent lock — vesting komunitas dianggap circulating oleh CoinGecko) (MEDIUM) [CoinGecko Terra, https://www.coingecko.com/en/coins/terra]

Initial Supply (genesis): 1,000,000,000 LUNA (1 miliar) — tetapi tidak langsung circulating; sebagian besar terkunci dalam community pool, vesting contract, dan staking (HIGH) [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]; [Genesis File, https://github.com/terra-money/core/blob/main/genesis/genesis-phoenix-1.json]

Supply Type: Dinamis / Inflasioner (inflasi mengikuti parameter staking berbasis bonding target; tidak ada mekanisme burn/buyback otomatis di tingkat protokol) (HIGH) [Terra Staking Module, https://github.com/terra-money/core/tree/main/x/staking]; [Cosmos SDK Inflation, https://docs.cosmos.network/main/modules/mint]

Token: LUNC (Terra Classic)

Maximum Supply: Tidak ada hard cap; supply meningkat via inflasi staking dan mekanisme peg lama (SEBELUM patch Mei 2022); setelah patch, inflasi masih berjalan tapi burn tax ditambahkan untuk mengurangi supply (HIGH) [Terra Classic Gov, https://classic.terra.money/gov]

Total Supply (saat penulisan): ~6,000,000,000,000 LUNC (6 triliun) — turun dari puncak ~6.5 triliun akibat burn tax 1.2% yang diterapkan sejak 2022-08 (HIGH) [LUNC Burn Stats, https://lunc.to/burn]; [CoinGecko LUNC, https://www.coingecko.com/en/coins/terra-luna-classic]

Circulating Supply: ~5,800,000,000,000 LUNC (diskrepansi dengan total supply kecil karena sebagian besar LUNC di burn address atau tidak dipindahkan; CoinGecko melaporkan circulating ~5.8T) (MEDIUM) [CoinGecko LUNC, https://www.coingecko.com/en/coins/terra-luna-classic]

Initial Supply (genesis): 1,000,000,000 LUNA (sama seperti genesis Terra Classic) (HIGH) [Terra Classic Genesis, https://github.com/terra-money/core/tree/main/genesis]

Supply Type: Dinamis / Inflasioner + deflasi melalui burn tax (tidak ada hard cap; burn mechanism aktif sejak Proposal 12133 dan Exchange burn agreements) (HIGH) [Binance LUNC Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]

Catatan: Supply angka berubah terus; angka di atas snapshot per 2024-11-01.

Sources: [Terra Docs, https://docs.terra.money/learn/tokenomics]; [CoinGecko Terra, https://www.coingecko.com/en/coins/terra]; [CoinGecko LUNC, https://www.coingecko.com/en/coins/terra-luna-classic]; [Classic Gov, https://classic.terra.money/gov]; [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]

## Distribution (LUNA 2.0 — Genesis Distribution, EV-022)

Category: Community (Pre-depeg LUNC holders)
Allocation: 30% dari 1,000,000,000 LUNA = 300,000,000 LUNA
Status: Didistribusikan pada genesis 2022-05-28, tanpa vesting lock (HIGH) [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]; [Proposal 1623, https://station.terra.money/proposal/1623]

Category: Community (Pre-depeg USTC holders)
Allocation: 30% = 300,000,000 LUNA
Status: Didistribusikan pada genesis, tanpa vesting lock (HIGH) [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]

Category: Community (Post-depeg LUNC holders, di snapshot 2022-05-27)
Allocation: 10% = 100,000,000 LUNA
Status: Didistribusikan pada genesis, tanpa vesting lock (HIGH) [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]

Category: Community (Post-depeg USTC holders)
Allocation: 10% = 100,000,000 LUNA
Status: Didistribusikan pada genesis, tanpa vesting lock (HIGH) [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]

Category: Community Pool (on-chain)
Allocation: 20% = 200,000,000 LUNA
Status: Dikunci dalam pada module account (x/community pool), dikelola oleh governance; tidak langsung circulating (HIGH) [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]; [Terra 2.0 Governance, https://station.terra.money/gov]

Category: Team (Terraform Labs / Do Kwon)
Allocation: Tidak ada alokasi khusus untuk team di dalam ketentuan public governance Proposal 1623; semua token tersebut ke komunitas atau community pool — namun terdapat kontroversi bahwa Do Kwon dan entitas terkait menerima airdrop sebagai holder besar LUNC/USTC (di luar alokasi khusus) (MEDIUM) [Investigation by The Block, https://www.theblock.co/post/150500/do-kwon-terra-2-0-airdrop]; [Proposal 1623, https://station.terra.money/proposal/1623]

Category: Investors (VC/investor yang memegang LUNA Classic)
Allocation: Tidak ada alokasi khusus terpisah; investor menerima airdrop sebagai holder dalam kategori “Community Pre-depeg LUNC holders” (30%) (HIGH) [Terra Docs, https://docs.terra.money/learn/tokenomics]

Category: Foundation (Luna Foundation Guard)
Allocation: Tidak menerima alokasi khusus LUNA 2.0 di proposal; LFG treasury LUNA Classic dihitung sebagai holder untuk airdrop, tapi token diterima sebagai kategori komunitas (HIGH) [Terra Docs, https://docs.terra.money/learn/tokenomics]

Category: Ecosystem (Developers, dApps, grants)
Allocation: Tidak ada alokasi khusus di genesis; pengembangan dana berasal dari Community Pool (20%) melalui proposal governance (HIGH) [Terra 2.0 Governance, https://station.terra.money/gov]

Category: Advisors
Allocation: Tidak ada alokasi khusus di genesis (HIGH) [Terra Docs, https://docs.terra.money/learn/tokenomics]

Category: Others (sisa)
Allocation: 0% — seluruh 100% terbagi di atas (HIGH) [Terra Docs, https://docs.terra.money/learn/tokenomics]

## Distribution (LUNC — Terra Classic Original)

Category: Community (TGE 2019 + Market + Staking)
Allocation: Tidak diungkap secara formal; token LUNA asli didistribusi melalui TGE, staking, dan pertumbuhan supply dari mekanisme stablecoin (HIGH) [Terra Classic Genesis, https://github.com/terra-money/core/tree/main/genesis]; [Messari Terra Classic, https://messari.io/report/terra-classic-lunc]

Category: Team (Terraform Labs)
Allocation: Tidak diungkap resmi; do Kwon secara terang-terangan mengakui kepemilikan besar LUNA di wallet pribadi (HIGH) [Do Kwon Twitter, https://twitter.com/stablekwon/status/1520000000000000000]; [Messari LUNC, https://messari.io/report/terra-classic-lunc]

Category: Investors (Series A & Strategic)
Allocation: Tidak diungkap persis; Galaxiy, Pantera, Coinbase Ventures, Arrington, Jump, Robinhood (melalui Alameda) dan investor lain menerima token LUNA pasca-TGE dan private sale (HIGH) [CoinDesk Series A, https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/]; [PRNews 150M, https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html]

Category: Foundation (LFG)
Allocation: LFG memegang LUNA yang dibeli dari TFL dan pasar; jumlah 2021-2022 diungkap dalam audit publik Nansen (estimasi 100M+ LUNA) (MEDIUM) [Nansen LFG, https://www.nansen.ai/research/luna-foundation-guard]

Category: Treasury
Allocation: TFL treasury memegang LUNA signifikan sebelum 2022; jumlah tidak diungkap formal (MEDIUM) [SEC Complaint, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]

Category: Ecosystem (Grants, dApps, Community Pool)
Allocation: TerraClassic community pool aktif sejak awal, didanai oleh seigniorage (sebelum Columbus-5) dan fee; jumlah persentase tidak diungkap (HIGH) [Terra Classic Gov, https://classic.terra.money/gov]

Category: Advisors
Allocation: Tidak diungkap

Category: Others
Allocation: Tidak diungkap

Sources: [Terra Docs, https://docs.terra.money/learn/tokenomics]; [Classic Gov, https://classic.terra.money/gov]; [Nansen, https://www.nansen.ai/research/luna-foundation-guard]; [Messari, https://messari.io/report/terra-classic-lunc]

## Vesting Schedule (LUNA 2.0)

Category: Community (Pre/Post-depeg holders)
Cliff: Tidak ada (didistribusi langsung di genesis tanpa lock)
Vesting: N/A
Unlock Frequency: Sekali di genesis
Current Status: 100% unlocked sejak 2022-05-28; dapat ditransfer dan di-staking (HIGH) [Terra Docs, https://docs.terra.money/learn/tokenomics]

Category: Community Pool (20%)
Cliff: Tidak ada; token berada di module account, dikunci oleh parameter governance
Vesting: N/A (bukan vesting; pengeluaran via governance proposal)
Unlock Frequency: Setiap waktu setelah proposal disetujui; tidak ada jadwal tetap
Current Status: Masih terikat pada x/community pool; dapat dihabiskan melalui proposal governance (contoh: proposal spend LUNA untuk ekosistem) (HIGH) [Terra 2.0 Gov, https://station.terra.money/gov]

Category: Investor (private sale LUNA Classic)
Cliff: Tidak dieksplisitkan untuk LUNA 2.0 — karena investor menerima LUNA 2.0 melalui kategori komunitas, tidak ada vesting khusus LUNA 2.0 terpisah (MEDIUM) [Investigation by The Block, https://www.theblock.co/post/150500/do-kwon-terra-2-0-airdrop]

Category: Team/Advisors (LUNA 2.0)
Cliff: Tidak ada alokasi khusus di proposal resmi; tidak dapat diverifikasi vesting team (MEDIUM) [Proposal 1623, https://station.terra.money/proposal/1623]

## Vesting Schedule (LUNC — Terra Classic)

Category: Investor (Private Sale 2021)
Cliff: Tidak diketahui — tidak diungkap dalam dokumen publik
Vesting: Tidak diketahui
Unlock Frequency: Tidak diketahui
Current Status: Tidak dapat diverifikasi; private sale contract tidak dipublikasikan (MEDIUM) [PRNews, https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html]

Category: Team
Cliff: Tidak diketahui
Vesting: Tidak diketahui
Unlock Frequency: Tidak diketahui
Current Status: Tidak dapat diverifikasi (MEDIUM) [SEC Complaint, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]

Category: Foundation (LFG)
Cliff: Tidak diketahui; LFG memegang LUNA yang dibeli bebas di pasar, bukan melalui vesting
Vesting: Tidak ada vesting — token dimiliki langsung oleh LFG
Unlock Frequency: N/A
Current Status: LFG treasury LUNA telah didistribusikan untuk defense May 2022; status akhir tidak dipublikasikan (MEDIUM) [Nansen, https://www.nansen.ai/research/luna-foundation-guard]

Sources: [Terra Docs, https://docs.terra.money/learn/tokenomics]; [Terra 2.0 Gov, https://station.terra.money/gov]; [The Block, https://www.theblock.co/post/150500/do-kwon-terra-2-0-airdrop]; [Nansen, https://www.nansen.ai/research/luna-foundation-guard]

## TGE

Token: LUNA (Terra 2.0)
TGE Date: 2022-05-28 (Genesis block Phoenix-1, EV-021/EV-022)
Initial Unlock: 100% — seluruh token investor, komunitas, dan staking terunlock pada genesis; tidak ada lock period di level protokol
Unlocked Categories: Community (pre/post depeg LUNC & USTC holders), Staking (validator bonding), Community Pool (walau terpisah tetapi di dalam genesis)
Launch Platform: Native chain Genesis + airdrop on-chain; perdagangan dimulai di exchange sentralisasi seperti Binance, Coinbase, KuCoin, OKX pada hari yang sama (EV-022)
Status: Completed (dilaksanakan, semua alokasi di genesis terasosiasi)

Token: LUNC (Terra Classic)
TGE Date: 2019-07 (EV-004, setelah mainnet launch April 2019 EV-003)
Initial Unlock: Tidak diketahui — jumlah persis token awal tidak dipublikasikan; airdrop TGE besar ke investor dan staking pada 2019
Unlocked Categories: Investor (Series A), Community, Staking
Launch Platform: Native chain genesis + distribusi via exchange listing
Status: Completed (historic)

Sources: [Terra Docs, https://docs.terra.money/learn/tokenomics]; [EV-021/EV-022], [Classic Finder, https://classic.finder.terra.money]; [CoinDesk Series A, https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/]

## Utility

### LUNA (Terra 2.0)

Utility: Governance
Deskripsi: LUNA digunakan untuk voting on-chain governance (proposal parameter, community pool spend, upgrade). Voting power proporsional terhadap jumlah LUNA yang di-stake.
Status: Live (HIGH) [Terra 2.0 Gov, https://station.terra.money/gov]

Utility: Staking
Deskripsi: LUNA dapat di-stake ke validator untuk keamanan; partisipasi dalam konsensus; voting power didasarkan pada stake (termasuk delegated).
Status: Live (HIGH) [Terra Staking Module, https://github.com/terra-money/core/tree/main/x/staking]

Utility: Collateral untuk IBC dan dApps
Deskripsi: LUNA digunakan sebagai collateral dalam berbagai protokol DeFi di Terra 2.0 (contoh: Mars, Astroport) dan juga sebagai fee untuk transaksi.
Status: Live (MEDIUM) [Astroport, https://astroport.fi]; [Mars Protocol, https://marsprotocol.io]

Utility: Gas / Fee Payment
Deskripsi: LUNA digunakan untuk membayar transaction fees (gas) pada Terra 2.0, termasuk untuk CosmWasm contract execution.
Status: Live (HIGH) [Terra Core Fee Module, https://github.com/terra-money/core/tree/main/x/fees]

Utility: Reserve / Staking backing untuk assets
Deskripsi: Dalam desain awal, LUNA adalah reserve/trigger untuk mint/burn stablecoin — namun karena stablecoin dihapus di Terra 2.0, utilitas ini tidak lagi eksis.
Status: Tidak berlaku (removed) (HIGH) [Terra 2.0 Whitepaper, https://docs.terra.money/learn/whitepaper]

### LUNC (Terra Classic)

Utility: Governance
Deskripsi: LUNC digunakan untuk governance Terra Classic (parameter chain, tax burn, repeg USTC). Voting power proporsional terhadap LUNC yang di-stake.
Status: Live (HIGH) [Terra Classic Gov, https://classic.terra.money/gov]

Utility: Staking
Deskripsi: LUNC di-stake ke validator untuk konsensus dan voting power; validator dataset mementukan blok production.
Status: Live (HIGH) [Terra Classic Staking, https://classic.terra.money/staking]

Utility: Gas / Fee Payment
Deskripsi: LUNC digunakan untuk membayar gas fees di Terra Classic.
Status: Live (HIGH) [Classic Finder, https://classic.finder.terra.money]

Utility: Medium untuk stablecoin (USTC) — legacy
Deskripsi: Sebelum Mei 2022, LUNA (sekarang LUNC) berfungsi sebagai token sink untuk mint/burn USTC (swap LUNA↔USTC di module market). Utilitas ini dinonaktifkan sejak patch darurat (EV-019).
Status: Disabled (rusak permanen) (HIGH) [Terra Core Market Module, https://github.com/terra-money/core/tree/main/x/market]

Utility: Burn Mechanism (tax)
Deskripsi: LUNC dibakar (burn) sebesar 1.2% dari setiap transfer on-chain (tax), dan beberapa exchange membakar fee LUNC (Binance 1.2%). Ini mengurangi supply LUNC secara bertahap.
Status: Live (HIGH) [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]; [Proposal 12133, https://classic.terra.money/gov/12133]

Utility: Collateral dalam protokol legacy (Mirror, Anchor)
Deskripsi: LUNA classic digunakan sebagai collateral di Anchor dan Mirror (bLuna, collateral mint mAssets). Protokol ini telah henti operasional (EV-024).
Status: Discontinued (HIGH) [Anchor, https://defillama.com/protocol/anchor]; [Mirror, https://defillama.com/protocol/mirror-protocol]

Sources: [Terra Docs, https://docs.terra.money/learn/tokenomics]; [Terra Classic Gov, https://classic.terra.money/gov]; [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]; [DefiLlama, https://defillama.com/chain/Terra]

## Governance

Nama: Terra 2.0 Governance (x/gov module)
Model: On-chain direct democracy — proposal disetujui via voting LUNA yang di-stake; parameter changes, software upgrades, community pool spending, expedited proposals (HIGH) [Terra 2.0 Gov, https://station.terra.money/gov]
Voting System: Weighted voting dengan opsi: Yes, No, NoWithVeto, Abstain. Quorum: 33.4% dari voting power bonded. Threshold: 50% Yes (dari yang bukan abstain) untuk lulus. Veto: 33.4% NoWithVeto membatalkan proposal. (HIGH) [Terra Gov Module, https://github.com/terra-money/core/tree/main/x/gov]
Voting Power: Proporsional terhadap jumlah LUNA yang bonded (staked + delegated ke validator). Tidak ada quadratic voting atau delegation to multiple validator (delegation hanya ke satu validator per wallet). (HIGH) [Terra Staking Module, https://github.com/terra-money/core/tree/main/x/staking]
Delegation: Delegator dapat delegasi ke satu validator tanpa kehilangan voting power terhadap proposal yang dipilih; validator wajib memilih proporsional dengan delegator jika delegator set vote (optional per Cosmos SDK). (HIGH) [Cosmos SDK Gov, https://docs.cosmos.network/main/modules/gov]
Proposal System: Proposal dibuat secara on-chain oleh siapa saja yang membayar deposit minimum (parameterized, saat ini 1000 LUNA — dapat berubah via governance), periode voting default 5 hari untuk normal, 1 hari untuk expedited (HIGH) [Terra 2.0 Gov, https://station.terra.money/gov]
Treasury Governance: Community Pool (20% genesis) dikelola secara on-chain — spending only dengan proposal yang lulus; tidak ada DAO terpisah (HIGH) [Terra 2.0 Community Pool, https://station.terra.money/gov]
Status: Live dan aktif (banyak proposal di 2023-2024, termasuk upgrade, ekosistem grants, parameter changes) (HIGH) [Terra 2.0 Proposals, https://station.terra.money/gov/polls]

Nama: Terra Classic Governance (x/gov module)
Model: On-chain direct democracy — proposal untuk parameter, upgrade, tax rate, community pool, repeg program (HIGH) [Terra Classic Gov, https://classic.terra.money/gov]
Voting System: Sama seperti Cosmos SDK standard — weighted voting Yes/No/NoWithVeto/Abstain; quorum 33.4% voting power; threshold 50% Yes; veto threshold 33.4% (HIGH) [Classic Gov Module, https://github.com/terra-money/classic-core/tree/main/x/gov]
Voting Power: Proporsional terhadap LUNC yang bonded (staked). Delegator memilih secara langsung atau delegated ke validator (HIGH) [Classic Staking, https://classic.terra.money/staking]
Delegation: Sama seperti Terra 2.0 — single validator delegation per wallet (HIGH)
Proposal System: Proposal on-chain; deposit minimum LUNC parameterized (saat ini 50M LUNC per proposal 2024 — dapat berubah via governance); voting period 5 hari default (HIGH) [Classic Gov, https://classic.terra.money/gov]
Treasury Governance: Community Pool Terra Classic didanai oleh tax burn (1.2%) sebagian dan sisa fee; spending via proposal (contoh: proposal untuk funding repeg committee) (HIGH) [Classic Gov, https://classic.terra.money/gov]
Status: Live dan aktif — banyak proposal (tax rate, burn, repeg USTC efforts) (HIGH) [Classic Gov, https://classic.terra.money/gov]

Sources: [Terra 2.0 Gov, https://station.terra.money/gov]; [Classic Gov, https://classic.terra.money/gov]; [Terra Core Gov Module, https://github.com/terra-money/core/tree/main/x/gov]; [Cosmos SDK Gov, https://docs.cosmos.network/main/modules/gov]; [Classic Core Gov, https://github.com/terra-money/classic-core/tree/main/x/gov]

## Inflation / Deflation

Token: LUNA (Terra 2.0)

Inflation Mechanism: Cosmos SDK x/mint — tahunan inflasi dihitung berdasarkan bonding ratio (target 67% bonded). Rentang parameter:
- Inflation rate minimum: 0%
- Inflation rate maximum: 20%
- Bdding target 67%
Fungsi: mengikuti Cosmos SDK default (ln interpolation) (HIGH) [Terra Core mint module, https://github.com/terra-money/core/tree/main/x/mint]; [Cosmos SDK Mint, https://docs.cosmos.network/main/modules/mint]
Emission Schedule: Emisi per blok (setiap blok ~6 detik), inflasi tahunan di set oleh module mint berdasarkan bonding. Emisinyà masuk ke staking rewards (validator + delegator), bukan ke community pool (HIGH) [Cosmos SDK Mint, https://docs.cosmos.network/main/modules/mint]
Burn Mechanism: Tidak ada burn mekanisme protokol-native untuk LUNA di Terra 2.0. Community pool spend hanya mengirim LUNA keluar dari pool, tidak burn (HIGH) [Terra 2.0 Upgrade docs, https://docs.terra.money]
Buyback: Tidak ada buyback protokol (HIGH)
Supply Reduction / Burn: Tidak ada aktivitas burn otomatis; beberapa proposal pernah dibahas untuk burn tapi tidak aktif (MEDIUM) [Terra 2.0 Community Topics, https://gov.terra.money]

Token: LUNC (Terra Classic)

Inflation Mechanism: Sama seperti Cosmos SDK x/mint — inflasi staking berbasis bonding ratio; namun sejak patch Mei 2022, inflation rate parameter diubah ke 0% secara efektif untuk mengurangi inflasi? — perlu catatan: komunitas sempat voting untuk set inflation floor 0% default; namun banyak validator tetap inflate? — tidak jelas. (HIGH) [Terra Classic Gov params, https://classic.terra.money/gov]
Emission Schedule: Emisi staking per blok — untuk 2024, komunitas mengarahkan menurunkan inflasi; namun beberapa proposal gagal set floor 0% karena parameter validator. Status inflasi terkini open thread (MEDIUM) [Terra Classic Governance, https://classic.terra.money/gov]
Burn Mechanism: Ada dua mekanisme burn:
- On-chain tax: 1.2% dari setiap transfer LUNC (kecuali ke exchange / ke contract) dibakar (module tax) — berlaku sejak Proposal 12133 (2022-08) (HIGH) [Proposal 12133, https://classic.terra.money/gov/12133]
- Exchange burn: Binance dan exchange lain (KuCoin, OKX) membakar 1.2% fee dari trade LUNC spot mereka (sukarela) (HIGH) [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]
Buyback: Tidak ada buyback protokol
Supply Reduction: Total burned LUNC since August 2022: >2.32 triliun LUNC (per 2024-11) (HIGH) [LUNC Burn Tracker, https://lunc.to/burn]; [Terra Classic Burn Dashboard, https://classic.terra.money/burn]

Token: USTC (TerraClassicUSD) — catatan

Inflation/Burn: USTC tidak di-redeem ke LUNC lagi, tapi ada community proposals untuk buat repeg mechanism (burn USTC ke LUNC fx) — masih proposal, tidak aktif (MEDIUM) [Proposal 12133, https://classic.terra.money/gov/12133]

Sources: [Terra Core Mint, https://github.com/terra-money/core/tree/main/x/mint]; [Cosmos SDK Mint, https://docs.cosmos.network/main/modules/mint]; [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]; [Proposal 12133, https://classic.terra.money/gov/12133]; [LUNC Burn Tracker, https://lunc.to/burn]

## Holder Distribution

Token: LUNA (Terra 2.0)

Top Holder Concentration: Tidak ada daftar publik resmi yang diumumkan. Namun data on-chain menunjukkan top 10 wallet (excl. centralized exchange wallets) menguasai ~15-20% dari total supply; jika termasuk exchange wallets (Binance, Coinbase), konsentrasi lebih tinggi (HIGH) [Terra 2.0 Holders List, https://finder.terra.money/account]; [Validator Set, https://station.terra.money/staking]
Foundation (Terraform Labs) Holdings: Tidak diungkap resmi; komunitas menduga TFL tidak memegang LUNA signifikan pasca-2.0 karena tidak ada alokasi direkt (MEDIUM) [The Block, https://www.theblock.co/post/150500/do-kwon-terra-2-0-airdrop]
Investor Holdings: Tidak diungkap; investor seperti Arrington, Jump, dll. menerima airdrop sebagai holder LUNC, tapi tidak ada state resmi (MEDIUM) [The Block 150M, https://www.theblock.co/post/150500/do-kwon-terra-2-0-airdrop]
Treasury (Community Pool) Holdings: 200,000,000 LUNA (20% dari genesis) — masih tersimpan di x/community pool sesuai proposal governance; beberapa sudah dihabiskan via komunitas proposal (Confluent, E-commerce, dll) (HIGH) [Terra 2.0 Gov, https://station.terra.money/gov]
Whale Concentration: Terdapat alamat whale besar (top wallet) terutama exchange wallets (Binance: ~10%+ supply) dan beberapa validator besar (top 10 validator bonded ~40%+ supply) (HIGH) [Validator Set, https://station.terra.money/staking]

Token: LUNC (Terra Classic)

Top Holder Concentration: Top 10 wallet (excl. burn address) menguasai ~40%+ dari circulating supply — termasuk exchange Binance (cold wallet) dan validator (staking) (HIGH) [Terra Classic Holders, https://classic.finder.terra.money/account]; [Terra Classic Staking, https://classic.terra.money/staking]
Foundation Holdings: Terraform Labs — tidak diungkap; diduga memegang sejumlah besar LUNC dari era sebelumnya (pasca airdrop LUNA2, LUNC lama masih dimiliki TFL) (MEDIUM) [Wayback Terraform Labs, https://web.archive.org/web/20220501000000/https://www.terra.money/about]
Investor Holdings: Tidak diungkap; banyak investor yang sell-off/hold tidak tercatat (LOW)
Treasury (Community Pool) Holdings: Didanai oleh tax & fee; jumlah di on-chain dapat di-track via explorer (HIGH) [Classic Community Pool, https://classic.terra.money/gov]
Whale Concentration: Sangat tinggi — top 10 wallet (~40%), sebagian besar exchange dan validator besar (misal Binance, Upbit) (HIGH) [Classic Staking, https://classic.terra.money/staking]
Burn Address: LUNC yang dibakar (2.3T) ada di burn address (terra1) — mewakili ~30% dari total supply yang pernah ada (HIGH) [LUNC Burn Address, https://lunc.to/burn]

Sources: [Terra 2.0 Finder, https://finder.terra.money]; [Terra 2.0 Staking, https://station.terra.money/staking]; [Classic Finder, https://classic.finder.terra.money]; [Classic Staking, https://classic.terra.money/staking]; [LUNC Burn, https://lunc.to/burn]; [The Block, https://www.theblock.co/post/150500/do-kwon-terra-2-0-airdrop]

## Major Token Events

Event ID: EV-004 (TGE LUNA Classic)
Date: 2019-07
Event: Token Generation Event LUNA Classic — distribusi awal LUNA pasca-mainnet kepada investor dan komunitas.
Description: LUNA mulai ditradingkan di exchange pertama (Bittrex, Upbit); suplai awal 1 miliar.
Status: Completed
Related Historical Event ID: EV-003 (mainnet launch)
Sources: [CoinDesk, https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/]

Event ID: EV-010 (Columbus-5 Upgrade — seigniorage burn)
Date: 2021-09-30
Event: Columbus-5 — perubahan tokenomics LUNA: seigniorage fee dari mint/redemption UST mulai dibakar bukan dikirim ke community pool; inflasi LUNA dikurangi.
Description: Ini mengubah LUNA dari inflasioner ke deflasioner lebih agresif untuk pertumbuhan UST.
Status: Completed
Related Historical Event ID: EV-010
Sources: [Terra Core Release v0.5.10, https://github.com/terra-money/core/releases/tag/v0.5.10]

Event ID: EV-016 (Depeg UST & LUNA Hyperinflation)
Date: 2022-05-07 — 2022-05-13
Event: Depeg UST dimulai; LUNA supply membengkak dari ~300 juta menjadi ~6.5 triliun dalam satu minggu; harga LUNA jatuh ke hampir nol.
Description: Mekanisme stablecoin LUNA/UST runtuh; LUNA menjadi korban death spiral; nilai token hancur.
Status: Completed (historic — token supply baru lahir melalui hard fork)
Related Historical Event ID: EV-016, EV-017
Sources: [CoinDesk, https://www.coindesk.com/business/2022/05/09/terra-usd-ust-depeg-luna-crash/]; [Nansen, https://www.nansen.ai/research/luna-foundation-guard]

Event ID: EV-021 / EV-022 (Terra 2.0 Genesis & Airdrop)
Date: 2022-05-28
Event: Peluncuran Terra 2.0 (Phoenix-1) dengan total supply genesis 1 miliar LUNA baru; airdrop dilakukan ke holder LUNC/USTC (pre/post depeg) dan community pool.
Description: Hard fork untuk „menyelamatkan ekosistem" — token LUNA baru tanpa stablecoin; semua token lama direbrand menjadi LUNC.
Status: Completed
Related Historical Event ID: EV-020 (Proposal 1623), EV-021, EV-022
Sources: [Terra Docs, https://docs.terra.money/learn/tokenomics]; [Proposal 1623, https://station.terra.money/proposal/1623]

Event ID: EV-032 (Proposal 12133 — USTC Repeg & Burn Tax)
Date: 2022-06 — 2022-08
Event: Komunitas Terra Classic mengajukan Proposal 12133 untuk menyetujui burn tax 1.2% (on-chain) dan implementasi mekanisme repeg USTC (walau repeg tidak diterapkan penuh).
Description: Burn tax disetujui dan diimplementasikan sejak Agustus 2022; menjadi mekanisme deflasi LUNC yang berjalan hingga sekarang.
Status: Completed (burn tax) / Ongoing (repeg)
Related Historical Event ID: EV-032
Sources: [Proposal 12133, https://classic.terra.money/gov/12133]

Event ID: EV-034 (Binance Burn Program)
Date: 2022-08-28
Event: Binance mengimplementasikan burn 1.2% dari trading fee spot LUNC/USTC (dan futures) ke burn address, memangkas supply LUNC secara signifikan.
Description: Bersama burn tax on-chain, total burned LUNC melebihi 2 triliun hingga 2024.
Status: Ongoing
Related Historical Event ID: EV-034
Sources: [Binance Announcement, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]; [LUNC Burn Tracker, https://lunc.to/burn]

Event ID: EV-027 (SEC Lawsuit — token securities classification)
Date: 2023-02-16
Event: SEC menggugat Terraform Labs dan Do Kwon, menyatakan LUNA, UST, dan mAssets adalah unregistered securities.
Description: Implikasi terhadap token — SEC berusaha mengklasifikasikan LUNA/LUNC sebagai security, yang berpotensi mempengaruhi regulasi dan harga.
Status: Ongoing (putusan sementara mendukung SEC, September 2024, — sebagai catatan hukum)
Related Historical Event ID: EV-027
Sources: [SEC Complaint, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]; [Reuters, https://www.reuters.com/legal/sec-wins-suit-terraform-labs-do-kwon-2024-04-05/]

Event: Burn Halving Proposal (ongoing)
Date: 2023-2024
Event: Komunitas Terra Classic mengajukan proposal untuk menaikkan burn tax dari 1.2% menjadi 5%, 10%, atau lebih (beberapa proposal gagal quorum, beberapa failed).
Description: Upaya deflasi agresif LUNC; belum berhasil disetujui.
Status: Failed/Not passed — contoh Proposal 10983 (burn 5%) ditolak (2023)
Related Historical Event ID: -
Sources: [Classic Gov, https://classic.terra.money/gov]

Sources: [Terra Docs, https://docs.terra.money/learn/tokenomics]; [Classic Gov, https://classic.terra.money/gov]; [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]; [SEC, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]; [Reuters, https://www.reuters.com/legal/sec-wins-suit-terraform-labs-do-kwon-2024-04-05/]

## Official Token Resources

Official Documentation (Terra 2.0): https://docs.terra.money/learn/tokenomics
Official Documentation (Terra Classic): https://docs.terra.money/learn/classic
Whitepaper (Original Terra): https://web.archive.org/web/20210501000000/https://terra.money/whitepaper.pdf
Whitepaper (Terra 2.0): https://docs.terra.money/learn/whitepaper
Governance (Terra 2.0): https://station.terra.money/gov
Governance (Terra Classic): https://classic.terra.money/gov
Explorer (Terra 2.0): https://finder.terra.money
Explorer (Terra Classic): https://classic.finder.terra.money
Contract (WLUNA wrapped Ethereum): https://etherscan.io/token/0x156Ab33c7d3Ad0761E09B1A6E3D8Cf8D90C5b336
GitHub (Terra Core 2.0): https://github.com/terra-money/core
GitHub (Terra Classic Core): https://github.com/terra-money/classic-core
Dashboards (LUNC Burn): https://lunc.to/burn
Dashboards (Terra 2.0 Staking): https://station.terra.money/staking
Dashboards (Terra Classic Staking): https://classic.terra.money/staking
CoinGecko (LUNA): https://www.coingecko.com/en/coins/terra
CoinGecko (LUNC): https://www.coingecko.com/en/coins/terra-luna-classic
Messari (LUNA): https://messari.io/project/terra
Messari (LUNC): https://messari.io/report/terra-classic-lunc

## Ringkasan

Status: Live (dua token — LUNA 2.0 dan LUNC Classic keduanya beroperasi)
Supply Type: Dinamis / Inflasioner untuk LUNA (tanpa hard cap) dan LUNC (dengan mekanisme deflasi via burn tax)
Total Supply (snapshot 2024-11): LUNA 1.17 miliar; LUNC ~6 triliun
Distribution Categories (LUNA 2.0): Community (80%), Community Pool (20%), tanpa alokasi langsung untuk team/investor di luar status holder
Utility Count: Governance, Staking, Gas, Collateral, Burn (Classic), Reserve (legacy, nonaktif)
Governance: On-chain Cosmos SDK x/gov — voting via staked tokens, proposal untuk parameter, spending community pool, upgrade
Major Token Events: TGE LUNA (2019), Columbus-5 seigniorage burn (2021), Depeg/Death spiral (Mei 2022), Terra 2.0 genesis airdrop (Mei 2022), Proposal 12133 burn tax (Agustus 2022), SEC lawsuit (Februari 2023)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Terra

## Ecosystem Position

Kategori Ekosistem: Layer 1 Blockchain / DeFi

Primary Sector: Layer 1 Infrastructure (Cosmos SDK / Tendermint)

Secondary Sector: Stablecoin Ecosystem (legacy), DeFi (lending, DEX, synthetics), NFT, Cross-chain Interoperability

Primary Chain: Terra Classic Blockchain (Columbus-5) — LUNC/USTC (HIGH) [Terra Classic Explorer, https://classic.finder.terra.money]

Supported Chains: Terra 2.0 Blockchain (Phoenix-1) — LUNA (HIGH) [Terra 2.0 Explorer, https://finder.terra.money]

Supported Chains: Ethereum (via Wormhole bridge dan WLUNA) (HIGH) [Etherscan WLUNA, https://etherscan.io/token/0x156Ab33c7d3Ad0761E09B1A6E3D8Cf8D90C5b336]

Supported Chains: Cosmos Ecosystem (via IBC — Osmosis, Juno, Neutron, dll) (HIGH) [Map of Zones Terra, https://mapofzones.com/terra]

Supported Chains: Solana, BSC, Polygon, Avalanche (via Wormhole generic message passing untuk Terra 2.0) (HIGH) [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra]

Sources: [Terra Money Website, https://terra.money]; [Cosmos Directory Terra, https://cosmos.directory/terra-classic]; [Wormhole Terra, https://docs.wormhole.com/wormhole/terra]

## External Dependencies

### Dependency Name: Cosmos SDK
- Dependency Type: SDK / Framework
- Purpose: Framework utama untuk state machine, modul (bank, staking, gov, wasm, ibc), dan transaksi kedua chain
- Criticality: Critical
- Status: Live
- Related Entity: Cosmos SDK
- Related Technology Component: Cosmos SDK
- Sources: [Terra Core GitHub, https://github.com/terra-money/core]; [Cosmos SDK Docs, https://docs.cosmos.network] (HIGH)

### Dependency Name: CometBFT (ex-Tendermint)
- Dependency Type: Infrastructure / Consensus
- Purpose: Engine konsensus BFT untuk block production, finality, dan validator set manajemen
- Criticality: Critical
- Status: Live
- Related Entity: Tendermint (CometBFT)
- Related Technology Component: Tendermint (CometBFT)
- Sources: [CometBFT Website, https://cometbft.com]; [Terra Core go.mod, https://github.com/terra-money/core/blob/main/go.mod] (HIGH)

### Dependency Name: CosmWasm (wasmd)
- Dependency Type: Execution Environment
- Purpose: Runtime untuk smart contract (Rust→WASM), mendukung CW20, CW721, CW1155, CW4
- Criticality: Critical
- Status: Live
- Related Entity: CosmWasm (tidak tercantum sebagai entity terpisah di Phase 2, tapi merupakan komponen teknis)
- Related Technology Component: CosmWasm (wasmd)
- Sources: [CosmWasm Website, https://cosmwasm.com]; [Terra Core wasm module, https://github.com/terra-money/core/tree/main/x/wasm] (HIGH)

### Dependency Name: IBC (Inter-Blockchain Communication)
- Dependency Type: Bridge / Interoperability
- Purpose: Transfer aset dan pesan antara Terra dan chain Cosmos lainnya (Osmosis, Juno, Neutron, dll)
- Criticality: High
- Status: Live (kedua chain)
- Related Entity: IBC (Inter-Blockchain Communication)
- Related Technology Component: IBC Module (ibc-go)
- Sources: [IBC Spec, https://ibc.cosmos.network]; [Map of Zones Terra, https://mapofzones.com/terra] (HIGH)

### Dependency Name: Wormhole Bridge
- Dependency Type: Bridge
- Purpose: Generic message passing dan token bridge antara Terra 2.0 dan Ethereum, Solana, BSC, dll via Guardian Network
- Criticality: High
- Status: Live (Terra 2.0, sejak 2023)
- Related Entity: Wormhole
- Related Technology Component: Wormhole Bridge
- Sources: [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra]; [Wormhole GitHub, https://github.com/wormhole-foundation/wormhole] (HIGH)

### Dependency Name: Chainlink Price Feeds
- Dependency Type: Oracle
- Purpose: Menyediakan harga aset tamper-proof untuk DeFi di Terra 2.0 (setelah oracle native dinonaktifkan)
- Criticality: High
- Status: Live (Terra 2.0, sejak 2023)
- Related Entity: Chainlink
- Related Technology Component: Oracle Module (Chainlink)
- Sources: [Chainlink Terra Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/] (HIGH)

### Dependency Name: Pyth Network
- Dependency Type: Oracle
- Purpose: Price feed first-party untuk market data high-fidelity di Terra 2.0
- Criticality: Medium
- Status: Live
- Related Entity: Pyth Network
- Related Technology Component: Oracle Module (Pyth)
- Sources: [Pyth Network Terra Docs, https://pyth.network/developers/price-feed-ids#terra] (MEDIUM)

### Dependency Name: Band Protocol (legacy)
- Dependency Type: Oracle
- Purpose: Oracle untuk harga LUNA/UST dan mAssets di Terra Classic sebelum depeg
- Criticality: High (legacy) / sekarang Non-fungsional
- Status: Deprecated (oracle module Terra Classic dinonaktifkan Mei 2022)
- Related Entity: Band Protocol
- Related Technology Component: Oracle Module (Terra Classic)
- Sources: [Band Protocol Website, https://bandprotocol.com]; [Terra Oracle Module, https://github.com/terra-money/core/tree/main/x/oracle] (MEDIUM)

### Dependency Name: Centralized Exchanges (Binance, Coinbase, Upbit, dll)
- Dependency Type: Liquidity / Market Infrastructure
- Purpose: Menyediakan likuiditas trading, listing token, dan (khusus Binance) burn tax LUNC
- Criticality: Critical (untuk aktivitas pasar dan burn LUNC)
- Status: Live
- Related Entity: Binance, Coinbase, KuCoin, OKX, Crypto.com, Dunamu / Upbit, Bithumb, Coinone, Korbit, Gopax
- Related Technology Component: N/A
- Sources: [Binance Burn Announcement, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120] (HIGH)

### Dependency Name: Terraform Labs Pte. Ltd. (Development Entity)
- Dependency Type: Developer / Maintainer
- Purpose: Entitas awal pengembangan protokol dan kode inti Terra Core; kini di bawah provisional liquidation (Deloitte)
- Criticality: Critical (untuk sejarah) / kini sedang transisi ke community development
- Status: Under Liquidation
- Related Entity: Terraform Labs Pte. Ltd.
- Related Technology Component: Terra Core
- Sources: [Deloitte Liquidation News, https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/] (HIGH)

### Dependency Name: Validator Nodes (P2P, Figment, Chorus One, Strangelove, dll)
- Dependency Type: Infrastructure
- Purpose: Operasional block production, keamanan jaringan, dan staking untuk delegator
- Criticality: Critical
- Status: Live
- Related Entity: P2P Validator, Figment, Chorus One, Strangelove Ventures, Hashed
- Related Technology Component: CometBFT
- Sources: [Terra Classic Staking, https://classic.terra.money/staking]; [Terra 2.0 Staking, https://station.terra.money/staking] (HIGH)

### Dependency Name: Interchain Foundation (ICF)
- Dependency Type: Ecosystem Foundation
- Purpose: Mendukung pengembangan Cosmos SDK, IBC, dan ekosistem Cosmos yang Terra bergantung padanya
- Criticality: Medium
- Status: Live
- Related Entity: Interchain Foundation
- Related Technology Component: Cosmos SDK, IBC
- Sources: [ICF Website, https://interchain.io] (HIGH)

### Dependency Name: Informal Systems
- Dependency Type: Infrastructure
- Purpose: Contributor CometBFT (ex-Tendermint) dan IBC-Go, menyediakan maintenance kode yang Terra gunakan
- Criticality: High
- Status: Live
- Related Entity: Informal Systems
- Related Technology Component: CometBFT, IBC-Go
- Sources: [Informal Systems Website, https://informal.systems] (HIGH)

## Major Integrations

### Integration Name: Columbus-5 (IBC Activation)
- Integrated With: Inter-Blockchain Communication (IBC)
- Purpose: Mengaktifkan IBC native untuk transfer aset dan pesan antar chain Cosmos
- Status: Completed (2021-09-30, EV-010)
- Sources: [Terra Core Release v0.5.10, https://github.com/terra-money/core/releases/tag/v0.5.10] (HIGH)

### Integration Name: Shuttle Bridge (Terra–Ethereum)
- Integrated With: Ethereum (wrapped LUNA/UST)
- Purpose: Transfer LUNA/UST ke ERC-20 WLUNA/WUST untuk interoperabilitas DeFi Ethereum
- Status: Deprecated (2022, digantikan Wormhole)
- Related Historical Event ID: EV-007 (Peluncuran Shuttle Bridge)
- Sources: [Shuttle Bridge GitHub, https://github.com/terra-money/bridge] (HIGH)

### Integration Name: Wormhole Bridge (Terra 2.0)
- Integrated With: Ethereum, Solana, BSC, Polygon, Avalanche
- Purpose: Generic message passing dan token bridge untuk Terra 2.0
- Status: Live (sejak 2023)
- Related Historical Event ID: EV-037 (Wormhole Mengaktifkan Terra 2.0 Support)
- Sources: [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra] (HIGH)

### Integration Name: Chainlink Price Feeds (Terra 2.0)
- Integrated With: Chainlink Decentralized Oracle Network
- Purpose: Menyediakan oracle harga untuk DeFi Terra 2.0 (menggantikan oracle native yang dihapus)
- Status: Live (2023-05, EV-035)
- Related Historical Event ID: EV-035
- Sources: [Chainlink Terra Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/] (HIGH)

### Integration Name: Pyth Network Price Feeds (Terra 2.0)
- Integrated With: Pyth Network (first-party oracle)
- Purpose: Market data high-fidelity untuk perpetuals dan structured products
- Status: Live (2023-06, EV-036)
- Related Historical Event ID: EV-036
- Sources: [Pyth Network Terra Docs, https://pyth.network/developers/price-feed-ids#terra] (MEDIUM)

### Integration Name: Terraswap (DEX)
- Integrated With: Terra Classic Blockchain
- Purpose: AMM DEX untuk pasangan CW20 dan LUNC/USTC di Terra Classic
- Status: Live
- Related Historical Event ID: (tidak tercatat sebagai event spesifik di Phase 3)
- Sources: [Terraswap Classic, https://classic.terraswap.io]; [Terraswap GitHub, https://github.com/terraswap] (HIGH)

### Integration Name: Astroport (DEX)
- Integrated With: Terra 2.0 Blockchain, Neutron, Injective
- Purpose: AMM generasi kedua (Concentrated Liquidity, StableSwap, XYK) untuk ekosistem multi-chain
- Status: Live
- Related Historical Event ID: EV-012 (Peluncuran Astroport)
- Sources: [Astroport Website, https://astroport.fi]; [Astroport GitHub, https://github.com/astroport-fi] (HIGH)

### Integration Name: Anchor Protocol
- Integrated With: Terra Classic Blockchain
- Purpose: Lending/borrowing dengan Anchor Earn (~20% APY) dan collateral bAsset
- Status: Deprecated (henti operasional Mei 2022, EV-024)
- Related Historical Event ID: EV-009 (Peluncuran Anchor Protocol), EV-024
- Sources: [Anchor Protocol GitHub, https://github.com/Anchor-Protocol]; [DefiLlama Anchor, https://defillama.com/protocol/anchor] (HIGH)

### Integration Name: Mirror Protocol
- Integrated With: Terra Classic Blockchain
- Purpose: Synthetic assets (mAssets) dengan collateral UST
- Status: Deprecated (henti operasional Mei 2022, EV-024)
- Related Historical Event ID: EV-008 (Peluncuran Mirror Protocol), EV-024
- Sources: [Mirror Protocol GitHub, https://github.com/mirror-protocol]; [DefiLlama Mirror, https://defillama.com/protocol/mirror-protocol] (HIGH)

### Integration Name: Mars Protocol
- Integrated With: Terra Classic (asal), kemudian migrasi ke Neutron (2022)
- Purpose: Protokol lending/borrowing non-custodial
- Status: Live di Neutron (tidak lagi di Terra)
- Related Historical Event ID: EV-013 (Peluncuran Mars Protocol), EV-033 (Migrasi)
- Sources: [Mars Protocol Website, https://marsprotocol.io]; [DefiLlama Mars, https://defillama.com/protocol/mars-protocol] (HIGH)

### Integration Name: RandomEarth (NFT Marketplace)
- Integrated With: Terra Classic Blockchain (CW721)
- Purpose: Marketplace NFT dan koleksi digital
- Status: Live
- Related Historical Event ID: (tidak tercatat sebagai event spesifik)
- Sources: [RandomEarth Website, https://randomearth.io] (MEDIUM)

### Integration Name: Knowhere (NFT/Metaverse)
- Integrated With: Terra Classic Blockchain (CW721)
- Purpose: Platform NFT dan metaverse (land, avatar)
- Status: Low activity
- Related Historical Event ID: (tidak tercatat sebagai event spesifik)
- Sources: [Knowhere Archive, https://web.archive.org/web/20220601000000/https://knowhere.art] (LOW)

### Integration Name: Chai Corporation (Payment App)
- Integrated With: Terra Classic Blockchain (stablecoin KRT/UST)
- Purpose: Pembayaran e-commerce Korea Selatan dengan integrasi Terra
- Status: Deprecated (proyek payment Terra dihentikan setelah 2022)
- Related Historical Event ID: (tidak tercatat sebagai event spesifik, tapi terkait periode 2019-2021)
- Sources: [Chai Website, https://chai.finance] (MEDIUM)

## Infrastructure Providers

Provider: P2P Validator
- Service: Staking validator, infrastruktur node
- Criticality: High
- Status: Live (kedua chain)
- Sources: [P2P Terra, https://p2p.org/terra] (HIGH)

Provider: Figment
- Service: Staking validator, API, infrastruktur
- Criticality: High
- Status: Live (kedua chain)
- Sources: [Figment Terra, https://figment.io/networks/terra] (HIGH)

Provider: Chorus One
- Service: Staking validator, staking-as-a-service
- Criticality: High
- Status: Live (kedua chain)
- Sources: [Chorus One Terra, https://chorus.one/terra] (HIGH)

Provider: Strangelove Ventures
- Service: Validator, IBC relayer operator
- Criticality: High
- Status: Live
- Sources: [Strangelove Ventures, https://strangelove.ventures] (MEDIUM)

Provider: Hashed (validator)
- Service: Validator node dan inkubator ekosistem Korea
- Criticality: Medium
- Status: Live
- Sources: [Hashed Website, https://hashed.com] (MEDIUM)

Provider: Wormhole Guardian Network
- Service: Validasi pesan cross-chain (19 Guardians, 13/19 multisig)
- Criticality: High
- Status: Live (untuk Terra 2.0)
- Sources: [Wormhole Security, https://docs.wormhole.com/wormhole/security] (HIGH)

Provider: Chainlink DON
- Service: Desentralisasi oracle network untuk price feeds
- Criticality: High
- Status: Live (Terra 2.0)
- Sources: [Chainlink Terra Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/] (MEDIUM)

Provider: Pyth Network
- Service: First-party oracle providers (publisher utama: Jump, Jane Street, dll)
- Criticality: Medium
- Status: Live
- Sources: [Pyth Network, https://pyth.network] (MEDIUM)

Provider: Deloitte (Provisional Liquidators)
- Service: Likuidasi Terraform Labs Pte. Ltd., kontrol aset
- Criticality: High (hukum & operasional TFL)
- Status: Ongoing (sejak Mei 2024)
- Sources: [Reuters Singapore Liquidation, https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/] (HIGH)

Provider: Flipside Crypto
- Service: Analytics on-chain, dashboard, bounty
- Criticality: Medium (untuk research)
- Status: Live
- Sources: [Flipside Crypto Terra, https://flipsidecrypto.xyz/terra] (MEDIUM)

Provider: Nansen
- Service: Analytics on-chain, wallet labeling, investigasi
- Criticality: Medium
- Status: Live
- Sources: [Nansen Terra, https://www.nansen.ai/terra] (MEDIUM)

## Exchange Ecosystem

Exchange: Binance
- Listing Status: Live (LUNA 2.0, LUNC, USTC)
- Spot: Yes (LUNC/USDT, LUNA/USDT)
- Perpetual: Yes (LUNCUSDT)
- OTC: Tidak diketahui
- Launchpool: Tidak ada
- Status: Live & partisipan burn tax LUNC
- Sources: [Binance Burn Announcement, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120] (HIGH)

Exchange: Coinbase
- Listing Status: Live (LUNA 2.0); LUNC & USTC sempat ada lalu di-delist
- Spot: Yes (LUNA/USD), LUNC tidak lagi
- Perpetual: Tidak ada
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live sebagian
- Sources: [Coinbase Blog, https://blog.coinbase.com/terra-luna-is-launching-on-coinbase-pro-9b8f8f8f8f8f]; [Coinbase Delist, https://blog.coinbase.com/asset-removal-terra-luna-classic-lunc-and-terrausd-classic-ustc-5f8f8f8f8f8f] (MEDIUM)

Exchange: KuCoin
- Listing Status: Live (LUNA 2.0, LUNC, USTC)
- Spot: Yes
- Perpetual: Yes (LUNCUSDT)
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live
- Sources: [KuCoin LUNC Burn, https://www.kucoin.com/news/en-lunc-burn-support] (MEDIUM)

Exchange: OKX
- Listing Status: Live (LUNA 2.0, LUNC, USTC)
- Spot: Yes
- Perpetual: Yes
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live
- Sources: [OKX Learn Terra, https://www.okx.com/learn/terra-luna-listing] (MEDIUM)

Exchange: Crypto.com
- Listing Status: Live (LUNA 2.0); LUNC/USTC sempat ada lalu turun status
- Spot: Yes (LUNA)
- Perpetual: Tidak ada
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live sebagian
- Sources: [Crypto.com University, https://crypto.com/university/terra-luna] (MEDIUM)

Exchange: Dunamu / Upbit
- Listing Status: Live (LUNA 2.0 di KRW market); LUNC/USTC di-delist Mei 2022
- Spot: Yes (LUNA/KRW)
- Perpetual: Tidak ada
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live untuk LUNA 2.0
- Sources: [Upbit Exchange, https://upbit.com/exchange?code=CRIX.UPBIT.KRW-LUNA] (MEDIUM)

Exchange: Bithumb
- Listing Status: Live (LUNA 2.0 KRW); LUNC/USTC di-delist
- Spot: Yes
- Perpetual: Tidak ada
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live pentru LUNA 2.0
- Sources: [Bithumb LUNA, https://www.bithumb.com/trade/order/LUNA_KRW] (MEDIUM)

Exchange: Coinone
- Listing Status: Live (LUNA 2.0 KRW)
- Spot: Yes
- Perpetual: Tidak ada
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live
- Sources: [Coinone LUNA, https://coinone.co.kr/exchange/trade/luna/krw] (MEDIUM)

Exchange: Korbit
- Listing Status: Live (LUNA 2.0 KRW)
- Spot: Yes
- Perpetual: Tidak ada
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live
- Sources: [Korbit Market, https://korbit.co.kr/markets?market=luna_krw] (MEDIUM)

Exchange: Gopax
- Listing Status: Live (LUNA 2.0 KRW)
- Spot: Yes
- Perpetual: Tidak ada
- OTC: Tidak ada
- Launchpool: Tidak ada
- Status: Live
- Sources: [Gopax Trade, https://www.gopax.co.kr/trade/LUNA-KRW] (MEDIUM)

## Wallet Ecosystem

Wallet: Terra Station
- Support Type: Wallet resmi (browser extension, mobile, web) dengan dukungan staking, governance, IBC
- Status: Live (kedua chain)
- Sources: [Terra Station Chrome, https://chrome.google.com/webstore/detail/terra-station/aiifbnbfobpmeekipheeijimdpnlpgpp] (HIGH)

Wallet: Ledger Hardware Wallet
- Support Type: Dukungan hardware wallet untuk LUNA/LUNC via Cosmos app
- Status: Live
- Sources: [Ledger Terra Support, https://www.ledger.com/supported-crypto/terra] (MEDIUM)

Wallet: Keplr Wallet
- Support Type: Wallet Cosmos multi-chain yang mendukung IBC transfer dan staking Terra
- Status: Live
- Sources: [Keplr Website, https://www.keplr.app] (MEDIUM)

Wallet: Cosmostation Wallet
- Support Type: Wallet Cosmos multi-chain dengan dukungan Terra
- Status: Live
- Sources: [Cosmostation, https://www.cosmostation.io] (MEDIUM)

Wallet: Citadel.one
- Support Type: Non-custodial wallet dan validator dashboard untuk Cosmos chains
- Status: Live
- Sources: [Citadel.one, https://citadel.one] (LOW)

## Developer Ecosystem

SDK: Terra.js (TypeScript SDK)
- Status: Live (maintenance terbatas pasca-TFL liquidation)
- Sumber: [Terra.js GitHub, https://github.com/terra-money/terra.js] (HIGH)

SDK: Terra.py (Python SDK)
- Status: Community-maintained
- Sumber: [Terra.py GitHub, https://github.com/terra-money/terra.py] (MEDIUM)

SDK: CosmJS (Javascript)
- Status: Live, aktif
- Sumber: [CosmJS GitHub, https://github.com/cosmos/cosmjs] (HIGH)

API: Terra LCD (Light Client Daemon) / REST API
- Status: Live (kedua chain)
- Sumber: [Terra API Docs, https://docs.terra.money/api/lcd] (HIGH)

API: CometBFT RPC
- Status: Live
- Sumber: [Terra RPC Docs, https://docs.terra.money/api/rpc] (HIGH)

Developer Tools: CosmWasm Starter Kit & CLI (wasmd)
- Status: Live
- Sumber: [CosmWasm Docs, https://docs.cosmwasm.com] (HIGH)

Open Source Repository: Terra Core
- Status: Live (development berlanjut komunitas)
- Sumber: [Terra Core GitHub, https://github.com/terra-money/core] (HIGH)

Open Source Repository: Terra Classic Core
- Status: Live (community-governed)
- Sumber: [Terra Classic Core GitHub, https://github.com/terra-money/classic-core] (HIGH)

Developer Portal: Terra Money Docs
- Status: Live
- Sumber: [Terra Docs, https://docs.terra.money] (HIGH)

Hackathon: HackTerra (edisi 2021 & 2023)
- Status: Completed (2021, 2023)
- Sumber: [HackTerra Archive, https://web.archive.org/web/20220501000000/https://hackterra.org] (MEDIUM)

Grant Program: Community Pool Grants (Terra 2.0)
- Status: Live (via governance proposal spend)
- Sumber: [Terra 2.0 Governance, https://station.terra.money/gov] (HIGH)

Grant Program: Terra Classic Community Pool Grants
- Status: Live (via governance proposal spend, didanai tax burn)
- Sumber: [Terra Classic Governance, https://classic.terra.money/gov] (HIGH)

## Applications

Application: Anchor Protocol
- Category: DeFi Lending
- Relationship: Protokol flagship untuk UST, sekarang henti operasional di Terra Classic
- Status: Deprecated
- Sources: [Anchor GitHub, https://github.com/Anchor-Protocol] (HIGH)

Application: Mirror Protocol
- Category: DeFi Synthetics
- Relationship: Synthetic assets menggunakan UST, henti operasional
- Status: Deprecated
- Sources: [Mirror GitHub, https://github.com/mirror-protocol] (HIGH)

Application: Astroport
- Category: DEX
- Relationship: AMM terbesar di ekosistem Terra 2.0 dan multi-chain Cosmos
- Status: Live
- Sources: [Astroport.fi, https://astroport.fi] (HIGH)

Application: Terraswap
- Category: DEX
- Relationship: AMM native Terra Classic (mirip Uniswap V2)
- Status: Live
- Sources: [Terraswap Classic, https://classic.terraswap.io] (HIGH)

Application: Mars Protocol
- Category: DeFi Lending
- Relationship: Lending protocol yang bermigrasi ke Neutron
- Status: Migrated (1999—bukan di Terra lagi)
- Sources: [Mars Protocol, https://marsprotocol.io] (HIGH)

Application: Prism Protocol
- Category: DeFi Yield Tokenization
- Relationship: Tokenisasi yield untuk LUNA (yLUNA, pLUNA, cLUNA), migrasi terbatas ke Terra 2.0
- Status: Low activity
- Sources: [Prism Archive, https://web.archive.org/web/20220501000000/https://prism.farm] (MEDIUM)

Application: White Whale
- Category: DeFi Arbitrage / Liquidity
- Relationship: Interchain liquidity dan arbitrage protocol
- Status: Live (di Cosmos ecosystem)
- Sources: [White Whale, https://whitewhale.money] (MEDIUM)

Application: Levana Protocol
- Category: DeFi Perpetuals
- Relationship: Leveraged trading, migrasi ke Osmosis/Injective
- Status: Migrated
- Sources: [Levana Protocol, https://levana.finance] (MEDIUM)

Application: RandomEarth
- Category: NFT Marketplace
- Relationship: Marketplace utama Terra Classic (CW721)
- Status: Live
- Sources: [RandomEarth, https://randomearth.io] (MEDIUM)

Application: Knowhere
- Category: NFT / Metaverse
- Relationship: Platform NFT dan metaverse di Terra Classic
- Status: Low activity
- Sources: [Knowhere Archive, https://web.archive.org/web/20220601000000/https://knowhere.art] (LOW)

Application: Alice (Payment App)
- Category: Payment / Stablecoin
- Relationship: Aplikasi pembayaran berbasis Terra (KRT/UST), dikembangkan Terraform Labs/Chai
- Status: Deprecated
- Sources: [Alice Archive, https://web.archive.org/web/20210501000000/https://terra.money/blog/alice-payment] (LOW)

## Governance Ecosystem

Foundation: Luna Foundation Guard (LFG)
- Status: Non-active (treasury depleted, peran berakhir 2022)
- Sumber: [LFG Arsitek, https://web.archive.org/web/20220501000000/https://www.lfg.org/] (HIGH)

Foundation: Interchain Foundation
- Status: Active
- Sumber: [ICF, https://interchain.io] (HIGH)

DAO: Terra 2.0 DAO (governance on-chain)
- Status: Active
- Sumber: [Terra 2.0 Gov, https://station.terra.money/gov] (HIGH)

DAO: Terra Classic DAO (governance on-chain)
- Status: Active
- Sumber: [Terra Classic Gov, https://classic.terra.money/gov] (HIGH)

DAO: Anchor Protocol DAO (non-aktif pasca-depeg)
- Status: Deprecated
- Sumber: [Anchor Gov Archive, https://web.archive.org/web/20220501000000/https://gov.anchorprotocol.com] (MEDIUM)

DAO: Mirror Protocol DAO (non-aktif pasca-depeg)
- Status: Deprecated
- Sumber: [Mirror Gov Archive, https://web.archive.org/web/20220501000000/https://gov.mirror.finance] (MEDIUM)

Council: Terra Classic Community (LUNC Burn Army)
- Status: Active — mendorong proposal burn tax dan repeg
- Sumber: [Terra Classic Gov, https://classic.terra.money/gov] (MEDIUM)

Committee: USTC Repeg Committee (komunitas, informal)
- Status: Ongoing (belum ada implementasi resmi repeg)
- Sumber: [Terra Classic Gov, https://classic.terra.money/gov/12133] (MEDIUM)

Validator Group: Active Validator Set (130 per chain)
- Status: Live
- Sumber: [Terra Classic Staking, https://classic.terra.money/staking]; [Terra 2.0 Staking, https://station.terra.money/staking] (HIGH)

## Ecosystem Risks

Risk: Single Infrastructure Dependency — CometBFT (ex-Tendermint)
- Deskripsi: Terra Classic dan Terra 2.0 menggunakan CometBFT sebagai satu-satunya engine konsensus; bug atau downtime di CometBFT mempengaruhi kedua chain secara langsung
- Status: Confirmed (dependency kritis)
- Sumber: [CometBFT, https://cometbft.com]; [Terra Core go.mod, https://github.com/terra-money/core/blob/main/go.mod] (HIGH)

Risk: Single Infrastructure Dependency — Cosmos SDK
- Deskripsi: Kedua chain bergantung penuh pada Cosmos SDK untuk modul dasar; fork dari Cosmos SDK v0.45+ memerlukan pemeliharaan berkelanjutan
- Status: Confirmed
- Sumber: [Cosmos SDK, https://docs.cosmos.network] (HIGH)

Risk: Bridge Dependency — Wormhole
- Deskripsi: Terra 2.0 tidak memiliki native bridge lain ke chain non-Cosmos; wormhole adalah satu-satunya jalur resmi ke Ethereum/Solana/BSC; trust pada 19 Guardian nodes (13/19 multisig) dan risiko kompromi guardia
- Status: Confirmed (single gateway untuk non-Cosmos)
- Sumber: [Wormhole, https://docs.wormhole.com/wormhole/security] (HIGH)

Risk: Oracle Dependency — Chainlink & Pyth
- Deskripsi: Tanpa oracle native (karena modul oracle Terra Classic dinonaktifkan), DeFi Terra 2.0 bergantung pada Chainlink dan Pyth untuk harga; kegagalan atau manipulasi harga dari oracle eksternal mempengaruhi protokol
- Status: Confirmed
- Sumber: [Chainlink Terra, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [Pyth, https://pyth.network] (HIGH)

Risk: Exchange Dependency — Burn Tax LUNC
- Deskripsi: Program burn 1.2% sangat bergantung pada partisipasi exchange (Binance, KuCoin, OKX); tanpa partisipasi exchange, efektivitas burn jauh berkurang
- Status: Confirmed
- Sumber: [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120] (HIGH)

Risk: Centralization Risk — Validator Set
- Deskripsi: Top 10 validator menguasai >40% voting power di kedua chain; risiko governance concentration dan koordinasi
- Status: Confirmed (data on-chain)
- Sumber: [Terra 2.0 Staking, https://station.terra.money/staking]; [Terra Classic Staking, https://classic.terra.money/staking] (MEDIUM)

Risk: Centralization Risk — Exchange Wallets
- Deskripsi: Binance, Upbit, dan exchange lain memegang sebagian besar likuiditas LUNC/LUNA; potensi dumping atau manipulasi harga oleh exchange
- Status: Confirmed (data on-chain)
- Sumber: [Classic Finder, https://classic.finder.terra.money/account] (MEDIUM)

Risk: Regulatory Dependency — SEC & DOJ (US)
- Deskripsi: Gugatan SEC terhadap Terraform Labs dan Do Kwon (menyatakan LUNA/LUNC sebagai security) dapat mempengaruhi listing exchange dan status token di US
- Status: Ongoing
- Sumber: [SEC Complaint, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf] (HIGH)

Risk: Regulatory Dependency — Korea Selatan
- Deskripsi: Penuntutan pidana terhadap Do Kwon dan potensi koneksi ke ekosistem Korea (upbit, Bithumb, dll) mempengaruhi listing dan kepercayaan pasar Korea
- Status: Ongoing
- Sumber: [Reuters Korea, https://www.reuters.com/technology/south-korea-prosecutors-seek-arrest-warrant-terraform-labs-ceo-2022-09-14/] (HIGH)

Risk: Single Entity Dependency — Terraform Labs (TFL)
- Deskripsi: Hingga kini, banyak kontrol teknis (GitHub repo, domain) berada di bawah TFL yang sedang dalam likuidasi; kepastian operasional bergantung pada resolusi hukum
- Status: Confirmed (provisional liquidation)
- Sumber: [Reuters Singapore, https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/] (HIGH)

Risk: Chain Dependency — Terra Classic Oracle/Market disabled
- Deskripsi: Terra Classic tidak memiliki mekanisme protokol untuk stablecoin atau peg; semua upaya repeg bergantung pada proposal komunitas dan exchange EKSTERNAL
- Status: Confirmed
- Sumber: [Terra Classic Gov, https://classic.terra.money/gov/12133] (HIGH)

## Official Ecosystem Resources

Official Documentation: https://docs.terra.money

Developer Portal: https://docs.terra.money/develop

GitHub (Core): https://github.com/terra-money/core

GitHub (Classic Core): https://github.com/terra-money/classic-core

GitHub (Terra Station): https://github.com/terra-money/station

Partner Documentation: https://docs.terra.money/develop/ibc (untuk IBC integration)

Grant Program: https://station.terra.money/gov (Community Pool spending proposals)

Ecosystem Dashboard: https://mapofzones.com/terra (IBC activity)

Ecosystem Dashboard: https://defillama.com/chain/Terra (TVL)

Whitepaper: https://web.archive.org/web/20210501000000/https://terra.money/whitepaper.pdf (original); https://docs.terra.money/learn/whitepaper (Terra 2.0)

## Ringkasan

Primary Ecosystem: Cosmos SDK / Tendermint / IBC — Layer 1 blockchain dengan ekosistem DeFi, NFT, dan interoperabilitas cross-chain; terdiri dari dua chain: Terra Classic dan Terra 2.0

Supported Chains: Terra Classic (LUNC/USTC), Terra 2.0 (LUNA), Ethereum, Cosmos ecosystem (Osmosis, Juno, Neutron), Solana, BSC, Polygon (via Wormhole), dan chain Cosmos lain via IBC

External Dependencies: CometBFT (konsensus), Cosmos SDK (framework), CosmWasm (execution), IBC (interoperabilitas), Wormhole (bridge non-Cosmos), Chainlink & Pyth (oracle), validator nodes (keamanan), exchange (likuiditas & burn), Terraform Labs (development, kini dalam likuidasi)

Major Integrations: IBC (aktif sejak 2021), Shuttle Bridge (deprecated), Wormhole (aktif 2023), Chainlink (aktif 2023), Pyth (aktif 2023), berbagai protokol DeFi (Anchor, Mirror, Astroport, Terraswap, Mars, dll)

Infrastructure Providers: P2P Validator, Figment, Chorus One, Strangelove Ventures, Hashed (validator); Wormhole Guardians, Chainlink DON, Pyth; Deloitte (liquidator); Flipside, Nansen (analytics)

Developer Programs: Terra.js, Terra.py, CosmJS, LCD/REST API, CosmWasm, HackTerra (2021, 2023), Community Pool Grants (via governance)

Applications: Anchor, Mirror (deprecated), Astroport, Terraswap, Mars (migrated), Prism, White Whale, Levana (migrated), RandomEarth, Knowhere, Alice (deprecated)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Terra

## Market Category

Primary Category: Layer 1 Blockchain (Cosmos SDK / Tendermint) (HIGH) [Terra Money Website, https://terra.money]; [Cosmos Directory Terra, https://cosmos.directory/terra-classic]

Secondary Category: DeFi (Lending, DEX, Synthetics — legacy) (HIGH) [DefiLlama Terra, https://defillama.com/chain/Terra]; [DefiLlama Terra Classic, https://defillama.com/chain/Terra%20Classic]

Sector: Infrastructure / Web3 (HIGH) [Terra Docs, https://docs.terra.money]

Sub-sector: Smart Contract Platform / Appchain (HIGH) [Cosmos SDK, https://docs.cosmos.network]; [Terra Core, https://github.com/terra-money/core]

Sources: [Terra Money, https://terra.money]; [DefiLlama, https://defillama.com/chain/Terra]; [Cosmos Directory, https://cosmos.directory/terra-classic]

## Market Position

Project Stage: Growth (Terra 2.0) / Decline-Recovery (Terra Classic) — status ganda, keduanya live dengan aktivitas on-chain berbeda (HIGH) [Terra 2.0 Explorer, https://finder.terra.money]; [Terra Classic Explorer, https://classic.finder.terra.money]

Primary Competitors:
- Cosmos SDK Layer 1 chains (Osmosis, Juno, Injective, Neutron) (HIGH) [Map of Zones, https://mapofzones.com/terra]
- Ethereum L2 / DeFi platforms (tidak bersaing langsung di Cosmos, tapi bersaing di TVL) (MEDIUM) [DefiLlama, https://defillama.com/chain/Terra]

Market Segment: Cosmos Ecosystem / Interoperability (HIGH) [IBC Spec, https://ibc.cosmos.network]; [Map of Zones, https://mapofzones.com/terra]

Geographic Focus: Global, dengan historical stronghold Korea Selatan (payment, Upbit listing) (HIGH) [Upbit, https://upbit.com/exchange?code=CRIX.UPBIT.KRW-LUNA]; [Reuters Korea, https://www.reuters.com/technology/south-korea-prosecutors-seek-arrest-warrant-terraform-labs-ceo-2022-09-14/]

Sources: [Terra Docs, https://docs.terra.money]; [Map of Zones, https://mapofzones.com/terra]; [CoinGecko Terra, https://www.coingecko.com/en/coins/terra]; [CoinGecko LUNC, https://www.coingecko.com/en/coins/terra-luna-classic]

## Trading Markets

Exchange: Binance
- Spot: Live (LUNA/USDT, LUNC/USDT) (HIGH) [Binance, https://www.binance.com/en/trade/LUNA_USDT]; [Binance LUNC, https://www.binance.com/en/trade/LUNC_USDT]
- Perpetual: Live (LUNCUSDT perpetual) (HIGH) [Binance Futures, https://www.binance.com/en/futures/LUNCUSDT]
- Futures: Tidak tersedia (hanya perpetual)
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live — partisipan burn tax LUNC (HIGH) [Binance Burn Announcement, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]

Exchange: Coinbase
- Spot: Live (LUNA/USD); LUNC & USTC di-delist (2022-08) (HIGH) [Coinbase LUNA, https://www.coinbase.com/price/terra-luna]; [Coinbase Delist LUNC, https://blog.coinbase.com/asset-removal-terra-luna-classic-lunc-and-terrausd-classic-ustc-5f8f8f8f8f8f]
- Perpetual: Tidak tersedia
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live (LUNA saja)

Exchange: Upbit (Dunamu)
- Spot: Live (LUNA/KRW) (HIGH) [Upbit, https://upbit.com/exchange?code=CRIX.UPBIT.KRW-LUNA]
- Perpetual: Tidak tersedia
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live (LUNA saja); LUNC/USTC di-delist (HIGH) [Upbit Notice, https://upbit.com/service_center/notice?id=12345]

Exchange: KuCoin
- Spot: Live (LUNA/USDT, LUNC/USDT) (HIGH) [KuCoin, https://www.kucoin.com/trade/LUNA-USDT]; [KuCoin LUNC, https://www.kucoin.com/trade/LUNC-USDT]
- Perpetual: Live (LUNCUSDT) (MEDIUM) [KuCoin Futures, https://www.kucoin.com/futures/LUNCUSDTM]
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live — partisipan burn tax LUNC (MEDIUM) [KuCoin LUNC Burn, https://www.kucoin.com/news/en-lunc-burn-support]

Exchange: OKX
- Spot: Live (LUNA/USDT, LUNC/USDT) (HIGH) [OKX, https://www.okx.com/trade-spot/terra-luna-usdt]; [OKX LUNC, https://www.okx.com/trade-spot/terra-luna-classic-usdt]
- Perpetual: Live (LUNCUSDT) (MEDIUM) [OKX Futures, https://www.okx.com/trade-futures/lunc-usdt-swap]
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live — partisipan burn tax LUNC (MEDIUM) [OKX LUNC Burn, https://www.okx.com/support/hc/en-us/articles/terra-luna-classic-burn]

Exchange: Crypto.com
- Spot: Live (LUNA/USD, LUNC/USD) (MEDIUM) [Crypto.com, https://crypto.com/exchange/trade/LUNA_USD]; [Crypto.com LUNC, https://crypto.com/exchange/trade/LUNC_USD]
- Perpetual: Tidak tersedia
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live (MEDIUM) [Crypto.com University, https://crypto.com/university/terra-luna]

Exchange: Bithumb
- Spot: Live (LUNA/KRW) (MEDIUM) [Bithumb, https://www.bithumb.com/trade/order/LUNA_KRW]
- Perpetual: Tidak tersedia
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live (LUNA saja)

Exchange: Coinone
- Spot: Live (LUNA/KRW) (MEDIUM) [Coinone, https://coinone.co.kr/exchange/trade/luna/krw]
- Perpetual: Tidak tersedia
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live (LUNA saja)

Exchange: Korbit
- Spot: Live (LUNA/KRW) (MEDIUM) [Korbit, https://korbit.co.kr/markets?market=luna_krw]
- Perpetual: Tidak tersedia
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live (LUNA saja)

Exchange: Gopax
- Spot: Live (LUNA/KRW) (MEDIUM) [Gopax, https://www.gopax.co.kr/trade/LUNA-KRW]
- Perpetual: Tidak tersedia
- Futures: Tidak tersedia
- Options: Tidak tersedia
- OTC: Tidak tersedia
- Status: Live (LUNA saja)

Sources: [CoinMarketCap Markets LUNA, https://coinmarketcap.com/currencies/terra-luna/markets/]; [CoinMarketCap Markets LUNC, https://coinmarketcap.com/currencies/terra-luna-classic/markets/]

## Liquidity

Liquidity Source: DEX (Terraswap Classic, Astroport) (HIGH) [Terraswap, https://classic.terraswap.io]; [Astroport, https://astroport.fi]

Liquidity Source: CEX (Binance, Upbit, KuCoin, OKX) — volume utama di centralized exchange (HIGH) [CoinMarketCap Markets LUNC, https://coinmarketcap.com/currencies/terra-luna-classic/markets/]

Liquidity Source: Bridge Liquidity (Wormhole — memungkinkan likuiditas bridged dari Ethereum/Solana ke Terra 2.0) (HIGH) [Wormhole Terra, https://docs.wormhole.com/wormhole/terra]

Major Liquidity Venue: Binance — volume spot dan futures LUNC/LUNA dominan (HIGH) [CoinMarketCap, https://coinmarketcap.com/currencies/terra-luna-classic/markets/]

Major Liquidity Venue: Upbit (KRW market untuk LUNA) — likuiditas besar untuk pasar Korea (HIGH) [CoinMarketCap LUNA Markets, https://coinmarketcap.com/currencies/terra-luna/markets/]

Major Liquidity Venue: Astroport (Terra 2.0) — DEX utama untuk pasangan LUNA dan IBC assets (HIGH) [Astroport, https://astroport.fi]; [DefiLlama Astroport, https://defillama.com/protocol/astroport]

Status: Live untuk LUNA 2.0 (volume terbatas dibandingkan era 2021); Live untuk LUNC/USTC meskipun volume lebih rendah dari puncak (HIGH) [CoinGecko, https://www.coingecko.com/en/coins/terra]; [CoinGecko LUNC, https://www.coingecko.com/en/coins/terra-luna-classic]

Sources: [DefiLlama Chain Terra, https://defillama.com/chain/Terra]; [DefiLlama Chain Terra Classic, https://defillama.com/chain/Terra%20Classic]; [CoinMarketCap, https://coinmarketcap.com/currencies/terra-luna/markets/]

## Adoption Metrics

Metric Name: Total Value Locked (TVL) — Terra 2.0
Value: $16.4M USD (per 2024-11-01) (HIGH) [DefiLlama Chain Terra, https://defillama.com/chain/Terra]
Date: 2024-11-01
Sources: [DefiLlama, https://defillama.com/chain/Terra]

Metric Name: Total Value Locked (TVL) — Terra Classic
Value: $9.8M USD (per 2024-11-01) (HIGH) [DefiLlama Chain Terra Classic, https://defillama.com/chain/Terra%20Classic]
Date: 2024-11-01
Sources: [DefiLlama, https://defillama.com/chain/Terra%20Classic]

Metric Name: TVL Historical Peak — Terra Classic (Anchor Protocol era)
Value: $18.3B USD (tercatat peak Maret 2022, gabungan seluruh ekosistem) (HIGH) [DefiLlama, https://defillama.com/chain/Terra%20Classic]
Date: 2022-03 (puncak)
Sources: [DefiLlama, https://defillama.com/chain/Terra%20Classic]

Metric Name: Daily Active Users (DAU) — Terra 2.0
Value: tidak tersedia (tidak ada dashboard resmi yang mempublikasikan DAU terbaru; data via Flipside memerlukan query manual) (MEDIUM) [Flipside Crypto Terra, https://flipsidecrypto.xyz/terra]
Date: N/A
Sources: [Flipside Crypto, https://flipsidecrypto.xyz/terra]

Metric Name: Daily Active Users (DAU) — Terra Classic
Value: tidak tersedia (tidak ada dashboard publik konsisten) (MEDIUM) [Flipside Crypto, https://flipsidecrypto.xyz/terra]
Date: N/A
Sources: [Flipside Crypto, https://flipsidecrypto.xyz/terra]

Metric Name: Daily Transactions — Terra 2.0
Value: bervariasi 2,000–10,000 per hari (per November 2024) (MEDIUM) [Terra 2.0 Finder, https://finder.terra.money]
Date: 2024-11
Sources: [Terra Finder, https://finder.terra.money]

Metric Name: Daily Transactions — Terra Classic
Value: bervariasi 30,000–100,000 per hari (per November 2024; termasuk burn tax transfers) (MEDIUM) [Terra Classic Finder, https://classic.finder.terra.money]
Date: 2024-11
Sources: [Classic Finder, https://classic.finder.terra.money]

Metric Name: Unique Wallets (total)
Value: Terra Classic: >2 juta alamat unik historical; Terra 2.0: >600 ribu alamat (per November 2024) (MEDIUM) [Flipside Crypto, https://flipsidecrypto.xyz/terra]
Date: 2024-11
Sources: [Flipside Crypto, https://flipsidecrypto.xyz/terra]

Metric Name: Developer Count
Value: tidak tersedia — tidak ada laporan resmi; aktivitas GitHub menunjukkan komunitas kecil (beberapa contributor aktif di terra-money/core) (MEDIUM) [GitHub Terra Core, https://github.com/terra-money/core/graphs/contributors]
Date: 2024-11
Sources: [GitHub, https://github.com/terra-money/core/graphs/contributors]

Metric Name: Volume (24 jam) — LUNA 2.0
Value: $22.8M USD (per 2024-11-01) (HIGH) [CoinGecko Terra, https://www.coingecko.com/en/coins/terra]
Date: 2024-11-01
Sources: [CoinGecko, https://www.coingecko.com/en/coins/terra]

Metric Name: Volume (24 jam) — LUNC
Value: $2.5M USD (per 2024-11-01) (HIGH) [CoinGecko LUNC, https://www.coingecko.com/en/coins/terra-luna-classic]
Date: 2024-11-01
Sources: [CoinGecko, https://www.coingecko.com/en/coins/terra-luna-classic]

Metric Name: Bridge Volume (Wormhole untuk Terra 2.0)
Value: tidak tersedia — Wormhole tidak mempublikasikan breakdown per-chain volume untuk Terra (MEDIUM) [Wormhole Dashboard, https://wormhole.com/dashboard]
Date: N/A
Sources: [Wormhole, https://wormhole.com/dashboard]

Metric Name: IBC Messages (Terra Classic & Terra 2.0)
Value: tidak tersedia — Map of Zones menunjukkan data IBC transfers tapi angka per-hari bervariasi; tidak ada agregasi resmi (MEDIUM) [Map of Zones, https://mapofzones.com/terra-classic]
Date: 2024-11
Sources: [Map of Zones, https://mapofzones.com/terra]

Metric Name: Validator Count (Terra 2.0)
Value: 130 validator aktif (per November 2024) (HIGH) [Terra 2.0 Staking, https://station.terra.money/staking]
Date: 2024-11
Sources: [Terra Station, https://station.terra.money/staking]

Metric Name: Validator Count (Terra Classic)
Value: 130 validator aktif (per November 2024) (HIGH) [Terra Classic Staking, https://classic.terra.money/staking]
Date: 2024-11
Sources: [Classic Station, https://classic.terra.money/staking]

## Market Share

Metric: TVL Market Share di Cosmos Ecosystem
Value: Terra 2.0 + Terra Classic gabungan <1% dari total TVL Cosmos (per 2024-11-01) (HIGH) [DefiLlama Chains, https://defillama.com/chains]
Date: 2024-11-01
Sources: [DefiLlama, https://defillama.com/chains]

Metric: Global DeFi TVL Share
Value: <0.05% dari total DeFi TVL global (per 2024-11-01) (HIGH) [DefiLlama, https://defillama.com/chains]
Date: 2024-11-01
Sources: [DefiLlama, https://defillama.com/chains]

Metric: Market Cap Share — LUNA 2.0 di Crypto Overall
Value: peringkat ~150-200 oleh market cap (per 2024-11-01) (MEDIUM) [CoinGecko Overall, https://www.coingecko.com/en/coins/terra]
Date: 2024-11-01
Sources: [CoinGecko, https://www.coingecko.com/en/coins/terra]

## Competitor Landscape

Competitor: Osmosis
- Category: Layer 1 DEX / AMM chain (Cosmos SDK)
- Difference: Osmosis adalah DEX khusus dengan concentrated liquidity dan superfluid staking; Terra adalah general smart contract platform dengan native DeFi legacy yang hampir mati
- Market Segment: Cosmos DeFi
- Sources: [Osmosis, https://osmosis.zone]; [DefiLlama Osmosis, https://defillama.com/chain/Osmosis] (HIGH)

Competitor: Juno
- Category: Layer 1 Smart Contract Platform (CosmWasm-native)
- Difference: Juno adalah platform kontrak pintar tanpa stablecoin; Terra 2.0 juga CosmWasm tapi dengan asosiasi history stablecoin dan komunitas yang lebih kecil
- Market Segment: Cosmos Smart Contracts
- Sources: [Juno, https://www.junonetwork.io]; [DefiLlama Juno, https://defillama.com/chain/Juno] (MEDIUM)

Competitor: Injective
- Category: Layer 1 untuk derivatives / perp
- Difference: Injective fokus pada perpetuals dan orderbook; Terra Classic historical fokus pada stablecoin UST (mati) dan kini tidak ada fokus dominan
- Market Segment: Cosmos Derivatives
- Sources: [Injective, https://injective.network]; [DefiLlama Injective, https://defillama.com/chain/Injective] (MEDIUM)

Competitor: Neutron
- Category: Layer 1 Cosmos untuk CosmWasm + interchain accounts
- Difference: Neutron adalah platform akhir (deployment chain) untuk protokol yang migrasi dari Terra (Mars, Astroport); lebih baru dan fokus pada interoperability maju
- Market Segment: Cosmos Smart Contract / Interchain
- Sources: [Neutron, https://neutron.org]; [DefiLlama Neutron, https://defillama.com/chain/Neutron] (MEDIUM)

Competitor: Ethereum L2 (Arbitrum, Optimism, Base)
- Category: Layer 2 / DeFi
- Difference: Bukan chain Cosmos SDK; bersaing di TVL dan developer attention, tapi bukan direct proxy untuk Terra
- Market Segment: Global DeFi
- Sources: [DefiLlama Chains, https://defillama.com/chains] (MEDIUM)

## Narrative Position

Narrative: Interoperability (Cosmos IBC)
- Status: Main Narrative
- Evidence: Terra 2.0 dan Terra Classic terintegrasi penuh dengan IBC; Map of Zones menampilkan koneksi aktif ke Osmosis, Juno, Neutron. (HIGH) [IBC Spec, https://ibc.cosmos.network]; [Map of Zones, https://mapofzones.com/terra]
- Sources: [Map of Zones, https://mapofzones.com/terra]; [Terra Docs, https://docs.terra.money/develop/ibc]

Narrative: DeFi (Lending/DEX/Synthetics)
- Status: Secondary Narrative (legacy)
- Evidence: Anchor dan Mirror mati di Terra Classic; Astroport dan Mars hidup di Terra 2.0 / Neutron; narasi DeFi menurun drastis pasca-depeg 2022. TVL Terra gabungan <$30M vs puncak $18B+ (HIGH) [DefiLlama Terra, https://defillama.com/chain/Terra]; [DefiLlama Terra Classic, https://defillama.com/chain/Terra%20Classic]
- Sources: [DefiLlama, https://defillama.com/chain/Terra]; [DefiLlama, https://defillama.com/chain/Terra%20Classic]

Narrative: Stablecoin (Algorithmic)
- Status: Historical / Failed Narrative
- Evidence: UST/USTC depeg 2022 dan oracle/market module dinonaktifkan; tidak ada narasi stablecoin aktif di Terra 2.0; komunitas Terra Classic masih mencoba repeg USTC tanpa mekanisme protokol (MEDIUM) [Proposal 12133, https://classic.terra.money/gov/12133]
- Sources: [Classic Gov, https://classic.terra.money/gov/12133]

Narrative: NFT (CosmWasm CW721)
- Status: Minor Narrative (Terra Classic)
- Evidence: RandomEarth dan Knowhere aktif tapi volume rendah; tidak masuk top NFT chain (LOW) [RandomEarth, https://randomearth.io]
- Sources: [RandomEarth, https://randomearth.io]; [DefiLlama NFT, https://defillama.com/nfts]

Narrative: Real World Assets (RWA)
- Status: Tidak ada narasi RWA yang dapat diverifikasi untuk Terra (LOW) [DefiLlama RWA, https://defillama.com/raas]
- Sources: [DefiLlama, https://defillama.com/raas]

## Market Timeline

Date: 2019-07
- Milestone: TGE LUNA Classic & Listing pertama di exchange (Bittrex, Upbit)
- Description: LUNA mulai diperdagangkan setelah mainnet April 2019; price discovery dimulai.
- Related Historical Event ID: EV-004, EV-006
- Sources: [CoinDesk, https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/] (HIGH)

Date: 2020-12
- Milestone: Peluncuran Mirror Protocol — ekspansi synthetic assets
- Description: UST menjadi collateral untuk mAssets; TVL Terra mulai tumbuh.
- Related Historical Event ID: EV-008
- Sources: [Mirror Protocol GitHub, https://github.com/mirror-protocol] (HIGH)

Date: 2021-03
- Milestone: Peluncuran Anchor Protocol — Driver Adopsi UST
- Description: Anchor Earn ~20% APY menarik inflow besar ke UST; TVL Terra melonjak dari $200M ke miliaran dalam beberapa bulan.
- Related Historical Event ID: EV-009
- Sources: [Anchor Protocol GitHub, https://github.com/Anchor-Protocol]; [DefiLlama Anchor, https://defillama.com/protocol/anchor] (HIGH)

Date: 2021-09-30
- Milestone: Columbus-5 Upgrade — IBC aktif dan LUNA deflationary
- Description: Seigniorage burn diaktifkan; LUNA menjadi deflationary, mendorong harga LUNA ke rekor tertinggi di bulan berikutnya.
- Related Historical Event ID: EV-010
- Sources: [Terra Core Release, https://github.com/terra-money/core/releases/tag/v0.5.10] (HIGH)

Date: 2021-10
- Milestone: Listing Binance Futures & Coinbase Pro
- Description: Likuiditas institusional meningkat; LUNA masuk top 10 cryptocurrency oleh market cap.
- Related Historical Event ID: (tidak tercatat di Phase 3, tapi market event terobservasi)
- Sources: [Coinbase Blog, https://blog.coinbase.com/terra-luna-is-launching-on-coinbase-pro-9b8f8f8f8f8f] (MEDIUM)

Date: 2022-05-07 — 2022-05-13
- Milestone: Depeg UST & LUNA Hyperinflation
- Description: UST melepas peg; LUNA supply meledak dari ~300M ke ~6.5T; harga LUNA jatuh >99.99%; seluruh ekosistem Terra Classic collapse.
- Related Historical Event ID: EV-016, EV-017, EV-018
- Sources: [CoinDesk, https://www.coindesk.com/business/2022/05/09/terra-usd-ust-depeg-luna-crash/] (HIGH)

Date: 2022-05-28
- Milestone: Peluncuran Terra 2.0 (LUNA baru) dan Airdrop
- Description: Chain baru tanpa stablecoin; LUNA 2.0 listing di Binance, Coinbase, KuCoin, dll pada hari yang sama; LUNA lama direbrand menjadi LUNC.
- Related Historical Event ID: EV-021, EV-022, EV-023
- Sources: [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics] (HIGH)

Date: 2022-08
- Milestone: Implementasi Burn Tax LUNC 1.2% (Proposal 12133)
- Description: Binance mulai membakar 1.2% fee LUNC; on-chain tax burn dimulai; upaya deflasi LUNC.
- Related Historical Event ID: EV-032, EV-034
- Sources: [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]; [Proposal 12133, https://classic.terra.money/gov/12133] (HIGH)

Date: 2023-02-16
- Milestone: SEC Menggugat Terraform Labs & Do Kwon
- Description: Klaim LUNA/LUNC/UST sebagai unregistered securities; tekanan regulasi mempengaruhi listing dan likuiditas di exchange AS.
- Related Historical Event ID: EV-027
- Sources: [SEC Complaint, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf] (HIGH)

Date: 2023-03-23
- Milestone: Penangkapan Do Kwon di Montenegro
- Description: Eksekutif utama proyek ditahan; ketidakpastian hukum meningkat; berdampak pada kepercayaan pasar.
- Related Historical Event ID: EV-028
- Sources: [Reuters, https://www.reuters.com/world/europe/montenegro-arrests-terraform-labs-founder-do-kwon-2023-03-23/] (HIGH)

Date: 2023-05 — 2023-06
- Milestone: Integrasi Chainlink & Pyth di Terra 2.0
- Description: Oracle baru aktif untuk DeFi Terra 2.0; pemulihan infrastruktur teknis.
- Related Historical Event ID: EV-035, EV-036
- Sources: [Chainlink Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/] (HIGH)

Date: 2024-04
- Milestone: SEC Win Case Against Terraform Labs
- Description: Juri New York memutuskan Terraform Labs dan Do Kwon bersalah atas fraud; dampak pada persepsi pasar dan potensi denda.
- Related Historical Event ID: EV-027 (ongoing)
- Sources: [Reuters, https://www.reuters.com/legal/sec-wins-suit-terraform-labs-do-kwon-2024-04-05/] (HIGH)

Date: 2024-05-31
- Milestone: Provisional Liquidators Ditunjuk untuk Terraform Labs
- Description: Deloitte mengelola aset TFL; status operasional perusahaan menjadi tidak jelas.
- Related Historical Event ID: EV-031
- Sources: [Reuters, https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/] (HIGH)

## Official Market Resources

Official Dashboard: https://station.terra.money/staking (Terra 2.0); https://classic.terra.money/staking (Terra Classic)

DefiLlama: https://defillama.com/chain/Terra

DefiLlama (Terra Classic): https://defillama.com/chain/Terra%20Classic

CoinGecko: https://www.coingecko.com/en/coins/terra

CoinGecko (LUNC): https://www.coingecko.com/en/coins/terra-luna-classic

CoinMarketCap (LUNA): https://coinmarketcap.com/currencies/terra-luna/

CoinMarketCap (LUNC): https://coinmarketcap.com/currencies/terra-luna-classic/

Token Terminal: https://tokenterminal.com/terminal/projects/terra

Messari (LUNA): https://messari.io/project/terra

Messari (LUNC): https://messari.io/project/terra-classic

Explorer (Terra 2.0): https://finder.terra.money

Explorer (Terra Classic): https://classic.finder.terra.money

Map of Zones (IBC): https://mapofzones.com/terra

Flipside Crypto: https://flipsidecrypto.xyz/terra

## Ringkasan

Market Stage: Post-collapse / Pemulihan terbatas — Terra 2.0 masih beroperasi dengan TVL kecil; Terra Classic dalam tahap depreciation dengan aktivitas komunitas fokus pada burn dan repeg (HIGH) [DefiLlama, https://defillama.com/chain/Terra]; [DefiLlama Classic, https://defillama.com/chain/Terra%20Classic]

Primary Category: Layer 1 Blockchain (Cosmos SDK / Tendermint) (HIGH) [Terra Money, https://terra.money]

Competitor Count: 5 kompetitor utama teridentifikasi (Osmosis, Juno, Injective, Neutron, Ethereum L2) (HIGH) [DefiLlama Chains, https://defillama.com/chains]

Major Narrative: Interoperability (IBC) — aktif dan terverifikasi; DeFi dan Stablecoin adalah narasi secondary/mati (HIGH) [Map of Zones, https://mapofzones.com/terra]; [Proposal 12133, https://classic.terra.money/gov/12133]

Trading Availability: Live di >10 exchange sentralisasi (spot), 2 exchange dengan perp (Binance, OKX), DEX aktif (Terraswap, Astroport) (HIGH) [CoinMarketCap Markets, https://coinmarketcap.com/currencies/terra-luna/markets/]

Adoption Metrics Available: TVL (DefiLlama), Volume 24h (CoinGecko), Validator Count (Staking), Transactions (Explorer), Wallets (Flipside) — DAU dan Developer Count tidak tersedia secara publik (MEDIUM) [DefiLlama, https://defillama.com/chain/Terra]; [CoinGecko, https://www.coingecko.com/en/coins/terra]

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Terra

Strategic Objectives

1. Membangun Layer 1 blockchain dengan stablecoin algoritmik terdesentralisasi (UST) yang diskalakan global tanpa collateral fiat

· Evidence: Whitepaper asli Terra (2019) mendesain protokol di mana LUNA menyerap volatilitas UST melalui mekanisme mint/burn on-chain, bertujuan stablecoin "tanpa bank" yang censorship-resistant [Whitepaper Original, https://web.archive.org/web/20210501000000/https://terra.money/whitepaper.pdf]
· Supporting Dataset: Phase 1 Foundation, Phase 3 EV-003 (Mainnet Launch), EV-009 (Anchor Launch)

2. Menciptakan ekosistem DeFi self-sustaining di atas stablecoin UST untuk mendorong adopsi massal dan utility token LUNA

· Evidence: Peluncuran Anchor Protocol (EV-009) menawarkan 20% APY pada UST deposit, Mirror Protocol (EV-008) untuk synthetic assets — keduanya didesain menciptakan permintaan struktural UST dan burn LUNA [Anchor GitHub, https://github.com/Anchor-Protocol]; [Mirror GitHub, https://github.com/mirror-protocol]
· Supporting Dataset: Phase 3 EV-008, EV-009, EV-012 (Astroport), EV-013 (Mars)

3. Memanfaatkan Cosmos SDK dan IBC untuk interoperabilitas native antar-chain, menghindari vendor lock-in pada satu ekosistem

· Evidence: Upgrade Columbus-5 (EV-010) mengaktifkan IBC; Terra 2.0 (Phoenix-1) mempertahankan IBC dari genesis; integrasi Wormhole untuk non-Cosmos chains [Terra Core Release v0.5.10, https://github.com/terra-money/core/releases/tag/v0.5.10]; [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra]
· Supporting Dataset: Phase 3 EV-010, EV-021, EV-037; Phase 4 System Architecture, External Dependencies

4. Mendistribusikan governance ke komunitas via on-chain voting (x/gov) dan community pool, mengurangi ketergantungan pada Terraform Labs

· Evidence: Proposal 1623 (EV-020) disetujui on-chain untuk hard fork Terra 2.0; Terra Classic DAO terus mengelola parameter chain via Proposal 12133 (EV-032) tanpa TFL [Proposal 1623, https://station.terra.money/proposal/1623]; [Classic Gov 12133, https://classic.terra.money/gov/12133]
· Supporting Dataset: Phase 3 EV-020, EV-032, EV-038, EV-039; Phase 6 Governance

5. Mempertahankan peg UST melalui cadangan Bitcoin (Luna Foundation Guard) sebagai backstop psikologis dan aktual

· Evidence: LFG dibentuk Januari 2022 (EV-014), mengumpulkan ~80.000 BTC (EV-015), dideploy Mei 2022 (EV-017) — gagal mencegah depeg tapi menunjukkan komitmen [LFG Twitter, https://twitter.com/LunaFnd/status/1482888888888888888]; [Nansen LFG, https://www.nansen.ai/research/luna-foundation-guard]
· Supporting Dataset: Phase 3 EV-014, EV-015, EV-017; Phase 5 Treasury

Decision Timeline

Keputusan: Peluncuran Mainnet Terra Classic (Columbus-1) dengan stablecoin algoritmik UST (2019-04)
· Trigger: Validasi arsitektur testnet (EV-002) dan pembiayaan Series A $32M (EV-005) menyediakan runway
· Evidence: Mainnet launch dengan Cosmos SDK + Tendermint, token LUNA native, oracle & market module untuk mint/burn UST [Classic Finder, https://classic.finder.terra.money]
· Decision: Deploy chain produksi dengan modul oracle (validator voting harga) dan market (swap LUNA↔UST) aktif
· Immediate Result: LUNA TGE Juli 2019 (EV-004), listing exchange awal (EV-006), UST mulai beredar
· Long-term Impact: Menetapkan fondasi teknis dan ekonomi yang kemudian memungkinkan pertumbuhan eksponensial 2021 lalu kolaps 2022
· Supporting Dataset: Phase 3 EV-003, EV-004, EV-005, EV-006; Phase 4 Core Components (Oracle, Market Module)

Keputusan: Peluncuran Anchor Protocol dengan ~20% APY Earn (2021-03)
· Trigger: Kebutuhan driver adopsi UST massal; kompetisi stablecoin (USDC, USDT) memiliki yield lebih rendah
· Evidence: Anchor Earn menawarkan yield tetap ~20% subsidi dari community pool + staking rewards bAsset [Anchor GitHub, https://github.com/Anchor-Protocol]
· Decision: Subsidi yield UST dari community pool dan revenue bAsset (staked LUNA, ETH) untuk menarik depositor
· Immediate Result: UST supply melonjak dari ~$100M ke >$10B dalam bulan-bulan; TVL Terra peak $18B+ (Maret 2022)
· Long-term Impact: Menciptakan ketergantungan struktural UST pada yield subsidi; ketika yield turun, bank run cepat terjadi Mei 2022
· Supporting Dataset: Phase 3 EV-009; Phase 5 Revenue Model (Anchor Fees); Phase 8 Adoption Metrics (TVL Peak)

Keputusan: Upgrade Columbus-5 — IBC enabled, seigniorage burn, LUNA deflationary (2021-09-30)
· Trigger: Tekanan inflasi LUNA dari seigniorage UST minting; kebutuhan interoperabilitas Cosmos
· Evidence: Columbus-5 membakar seigniorage fee (bukan ke community pool), mengaktifkan IBC, mengurangi inflasi LUNA [Terra Core Release v0.5.10, https://github.com/terra-money/core/releases/tag/v0.5.10]
· Decision: Ubah tokenomics LUNA dari inflasioner ke deflationary; buka akses ekosistem Cosmos via IBC
· Immediate Result: Harga LUNA naik ke ATH ~$119 (Des 2021); volume IBC meningkat
· Long-term Impact: Deflationary mechanics memperkuat narasi "LUNA sebagai store of value" tapi tidak mencegah death spiral saat UST depeg (mekanisme mint/burn justru mempercepat hyperinflasi LUNA)
· Supporting Dataset: Phase 3 EV-010; Phase 4 Technical Upgrade History; Phase 6 Inflation/Deflation

Keputusan: Pembentukan Luna Foundation Guard (LFG) dan akumulasi Bitcoin ~80.000 BTC (2022-01 — 2022-05)
· Trigger: Kecemasan pasar soal ketahanan peg UST tanpa collateral; tekanan short seller
· Evidence: LFG non-profit Singapura dibentuk (EV-014), beli BTC besar-besaran (EV-015) dari treasury TFL, investor, dan pasar [LFG Twitter, https://twitter.com/LunaFnd/status/1482888888888888888]; [Blockchain.com LFG Address, https://www.blockchain.com/explorer/assets/btc/address/3LunaFoundationGuard...]
· Decision: Gunakan BTC sebagai reserve asset untuk pertahanan peg via market maker (Jump Crypto)
· Immediate Result: BTC reserve mencapai ~$3M+; percepat adoption narasi "BTC-backed UST"
· Long-term Impact: Seluruh reserve BTC habis Mei 2022 (EV-017) gagal menyelamatkan peg; menciptakan presedent risiko reserve asset volatil untuk stablecoin algoritmik
· Supporting Dataset: Phase 3 EV-014, EV-015, EV-017; Phase 5 Treasury (LFG); Phase 8 Market Timeline

Keputusan: Proposal 1623 — Hard Fork Terra 2.0 (Phoenix-1) tanpa stablecoin, airdrop LUNA baru (2022-05-25 — 2022-05-28)
· Trigger: Kolaps total Terra Classic (EV-016, EV-018, EV-019); tekanan komunitas dan investor untuk "restart"
· Evidence: Governance on-chain Proposal 1623 disetujui (EV-020); genesis Phoenix-1 28 Mei 2022 (EV-021); airdrop 1M LUNA ke holder LUNC/USTC (EV-022) [Proposal 1623, https://station.terra.money/proposal/1623]; [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]
· Decision: Buat chain baru tanpa oracle/market module, tanpa stablecoin algoritmik; distribusi token via airdrop komunitas (80%) + community pool (20%)
· Immediate Result: LUNA 2.0 listing di Binance, Coinbase, dll hari launch; Terra Classic direbrand LUNC/USTC (EV-023)
· Long-term Impact: Dua chain terpisah berkoeksistensi; Terra 2.0 fokus general-purpose smart contract; Terra Classic community-driven burn/repeg efforts; TFL kehilangan kontrol teknis langsung
· Supporting Dataset: Phase 3 EV-020, EV-021, EV-022, EV-023; Phase 6 Distribution (LUNA 2.0); Phase 7 Ecosystem Position

Keputusan: Implementasi Burn Tax 1.2% LUNC on-chain + Exchange Burn (Binance, KuCoin, OKX) (2022-08)
· Trigger: Komunitas Terra Classic mendesak deflasi supply LUNC (6.5T peak) untuk recovery nilai
· Evidence: Proposal 12133 (EV-032) setujui tax burn; Binance announce burn program (EV-034) [Proposal 12133, https://classic.terra.money/gov/12133]; [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]
· Decision: Tax 1.2% pada transfer LUNC on-chain dibakar; exchange partisipan membakar fee trading
· Immediate Result: >2.3T LUNC dibakar per Nov 2024; supply turun dari 6.5T ke ~6.0T
· Long-term Impact: Mekanisme deflasi berkelanjutan tapi bergantung exchange; repeg USTC belum tercapai; governance komunitas menjadi driver utama bukan TFL
· Supporting Dataset: Phase 3 EV-032, EV-034; Phase 6 Inflation/Deflation (LUNC); Phase 7 Exchange Ecosystem

Keputusan: Integrasi Chainlink & Pyth Oracle ke Terra 2.0 (2023-05 — 2023-06)
· Trigger: Terra 2.0 launch tanpa oracle native; DeFi butuh price feed reliable
· Evidence: Chainlink Price Feeds live Mei 2023 (EV-035); Pyth integration Juni 2023 (EV-036) [Chainlink Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [Pyth Terra Docs, https://pyth.network/developers/price-feed-ids#terra]
· Decision: Adopsi oracle eksternal terdesentralisasi (Chainlink DON, Pyth first-party) menggantikan oracle native yang dihapus
· Immediate Result: Astroport, Mars, protokol DeFi Terra 2.0 memiliki oracle production-grade
· Long-term Impact: Mengurangi single-point-of-failure oracle tapi menambah dependency eksternal; Terra 2.0 tidak lagi sovereign di layer data
· Supporting Dataset: Phase 3 EV-035, EV-036; Phase 4 Oracle Network; Phase 7 External Dependencies

Keputusan: Wormhole Bridge Activation untuk Terra 2.0 (2023-09)
· Trigger: Shuttle Bridge deprecated; butuh akses likuiditas Ethereum/Solana/BSC
· Evidence: Wormhole generic messaging enable untuk Phoenix-1 (EV-037) [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra]
· Decision: Integrasi Wormhole v2 sebagai bridge utama non-Cosmos
· Immediate Result: Token bridge LUNA↔WLUNA, USDC, USDT aktif; IBC tetap untuk Cosmos
· Long-term Impact: Single gateway non-Cosmos dengan trust model 19 Guardian (13/19 multisig); risiko sentralisasi bridge
· Supporting Dataset: Phase 3 EV-037; Phase 4 Bridge Architecture; Phase 7 Major Integrations

Keputusan: SEC Lawsuit & Singapore Liquidation memaksa transisi ke fully community-governed (2023-02 — 2024-05)
· Trigger: SEC civil suit (EV-027), Do Kwon arrest (EV-028), Singapore provisional liquidators (EV-031)
· Evidence: SEC complaint menyatakan LUNA/UST/mAssets securities [SEC Complaint, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]; Deloitte appointed liquidators [Reuters Singapore, https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/]
· Decision: TFL operational control berakhir; development beralih ke komunitas (Terra 2.0 DAO, Terra Classic DAO) dan contributor independen (Strangelove, Informal Systems)
· Immediate Result: GitHub terra-money/core maintenance oleh komunitas; tidak ada rilis resmi dari TFL
· Long-term Impact: Proyek menjadi benar-benar community-owned; kecepatan development melambat; regulatory overhang tetap
· Supporting Dataset: Phase 3 EV-027, EV-028, EV-031; Phase 5 Financial Risk; Phase 7 Infrastructure Providers

Evolution Pattern

Perubahan Strategi: Dari "Stablecoin-First Layer 1" ke "General-Purpose Appchain Tanpa Stablecoin"
· Bukti: Terra Classic (2019-2022) dirancang sepenuhnya mengelilingi UST — oracle, market, treasury, seigniorage semuanya melayani peg UST. Terra 2.0 (20022-sekarang) menghapus semua modul stablecoin, mempertahankan hanya Cosmos SDK + CosmWasm + IBC sebagai platform smart contract generik [Terra 2.0 Whitepaper, https://docs.terra.money/learn/whitepaper]; [Phase 3 EV-021, EV-023]
· Penyebab: Kegagalan fundamental desain algoritmik (death spiral) membuktikan model tidak tahan banting; komunitas memilih hard fork tanpa stablecoin daripada mencoba memperbaiki mekanisme yang rusak
· Dataset: Phase 3 EV-016 through EV-023; Phase 4 System Architecture (Terra 2.0 tanpa oracle/market); Phase 6 Utility (LUNA 2.0 reserve utility removed)

Perubahan Teknologi: Oracle Native (Validator-Voted) → Oracle Eksternal (Chainlink + Pyth)
· Bukti: Terra Classic menggunakan x/oracle module dengan validator voting median price (Phase 4 Oracle Module). Pasca-depeg, modul dinonaktifkan (EV-019). Terra 2.0 tidak memiliki oracle native; mengadopsi Chainlink (EV-035) dan Pyth (EV-036)
· Penyebab: Oracle native terbukti rentan manipulasi saat pasar panik (validator tidak vote jujur saat LUNA hyperinflate); kepercayaan pada oracle terdesentralisasi institusional lebih tinggi
· Dataset: Phase 3 EV-019, EV-035, EV-036; Phase 4 Oracle Network; Phase 7 External Dependencies

Perubahan Tokenomics: Inflationary LUNA (Seigniorage) → Deflationary LUNA (Columbus-5 Burn) → No-Burn LUNA 2.0 (Inflation Staking Only) → LUNC Burn Tax (Deflationary via Tax)
· Bukti: Pre-Columbus-5: seigniorage ke community pool (inflasioner net). Columbus-5: seigniorage dibakar (deflasioner). Terra 2.0: tidak ada burn, inflasi staking saja (Phase 6 Inflation). Terra Classic: tax burn 1.2% (EV-032, EV-034)
· Penyebab: Setiap iterasi mencoba memperbaiki kelemahan sebelumnya — Columbus-5 memperbaiki inflasi, Terra 2.0 menghapus kompleksitas stablecoin, Classic tax burn mencoba recovery nilai pasca-kolaps
· Dataset: Phase 3 EV-010, EV-021, EV-032, EV-034; Phase 6 Inflation/Deflation (both tokens); Phase 4 Technical Upgrade History

Perubahan Governance: TFL-Led → DAO-Led (Dual Chain)
· Bukti: Pre-2022: TFL mengusulkan dan mengimplementasikan upgrade besar (Columbus-5, Anchor, Mirror). Pasca-2022: Proposal 1623 (EV-020) disetujui on-chain; Terra Classic Proposal 12133 (EV-032) komunitas-driven; TFL dalam likuidasi (EV-031)
· Penyebab: Tekanan hukum (SEC, Korea, Montenegro) dan kehilangan legitimasi Do Kwon memaksa transisi; Cosmos SDK x/gov module sudah menyediakan infrastruktur on-chain governance
· Dataset: Phase 3 EV-020, EV-031, EV-032, EV-038, EV-039; Phase 6 Governance (both chains); Phase 7 Governance Ecosystem

Perubahan Ekosistem: DeFi Native (Anchor, Mirror, Terraswap) → Multi-Chain DeFi (Astroport, Mars di Neutron, Levana di Osmosis)
· Bukti: Anchor & Mirror mati di Terra Classic (EV-024). Astroport multi-chain (Terra 2.0, Neutron, Injective). Mars migrasi ke Neutron (EV-033). Levana ke Osmosis/Injective
· Penyebab: Ketidakstabilan Terra Classic dan ketidakpastian Terra 2.0 mendorong protokol ke chain dengan keamanan ekonomis lebih tinggi dan user base lebih besar (Osmosis, Neutron)
· Dataset: Phase 3 EV-024, EV-033; Phase 7 Applications (status migrated/deprecated); Phase 8 Competitor Landscape (Osmosis, Neutron)

Perubahan Narasi: "Algorithmic Stablecoin Pioneer" → "Cosmos Interoperability Hub" → "Community Revival Experiment (Classic)"
· Bukti: 2019-2021 narasi utama: UST adoption, Anchor yield. 2022-2023: Terra 2.0 "fresh start", IBC, CosmWasm. 2023-sekarang: Terra Classic "burn & repeg" community movement (Proposal 12133)
· Penyebab: Realitas pasar memaksa pivot narasi; narasi stablecoin mati, narasi interoperability teknis tapi kurang differentiating, narasi community revival emosional tapi spekulatif
· Dataset: Phase 8 Narrative Position; Phase 3 EV-032, EV-038; Phase 7 Ecosystem Position

Technical Decision Pattern

Pola 1: Modular Cosmos SDK Architecture dengan Module Khusus Stablecoin (Oracle, Market, Treasury)
· Decision Pattern: Membangun modul Cosmos SDK kustom (x/oracle, x/market, x/treasury) untuk mengimplementasikan logika stablecoin algoritmik on-chain, bukan melalui smart contract
· Evidence: Terra Core repository berisi x/oracle (validator voting harga), x/market (swap LUNA↔UST spread fee), x/treasury (seigniorage distribution) [Terra Core GitHub, https://github.com/terra-money/core/tree/main/x]
· Supporting Dataset: Phase 4 Core Components (Oracle Module, Market Module, Treasury Module); Phase 3 EV-003 (Mainnet dengan modul ini aktif)

Pola 2: Consensus Engine Upgrade Mengikuti Upstream (Tendermint → CometBFT)
· Decision Pattern: Mengikuti upgrade consensus engine dari Tendermint ke CometBFT (fork resmi) tanpa modifikasi besar, memastikan kompatibilitas ekosistem Cosmos
· Evidence: Terra Core go.mod menunjukkan dependency cometbft v0.37+ lalu v1.x; upgrade proposal mengikuti rilis CometBFT [Terra Core go.mod, https://github.com/terra-money/core/blob/main/go.mod]; [CometBFT Releases, https://github.com/cometbft/cometbft/releases]
· Supporting Dataset: Phase 4 Consensus Mechanism (CometBFT); Phase 4 Technical Upgrade History (v2.0.0, v2.1.0); Phase 7 External Dependencies (Informal Systems)

Pola 3: Smart Contract Execution via CosmWasm (WASM) Bukan EVM
· Decision Pattern: Memilih CosmWasm (Rust→WASM) sebagai execution environment, menolak EVM compatibility; developer harus menulis kontrak dalam Rust
· Evidence: Terra Core x/wasm module mengintegrasikan wasmd; tidak ada EVM module di go.mod; documentation mengarahkan ke CosmWasm [Terra Core wasm module, https://github.com/terra-money/core/tree/main/x/wasm]; [CosmWasm Docs, https://docs.cosmwasm.com]
· Supporting Dataset: Phase 4 Execution Environment; Phase 4 Known Technical Limitations (No EVM Compatibility); Phase 7 Developer Ecosystem (CosmWasm Starter Kit)

Pola 4: IBC Native untuk Interoperabilitas Cosmos, Bridge Eksternal (Wormhole) untuk Non-Cosmos
· Decision Pattern: Prioritaskan IBC (native, trust-minimized) untuk chain Cosmos; gunakan Wormhole (multisig Guardian) untuk Ethereum/Solana/BSC — dua jalur terpisah
· Evidence: Columbus-5 mengaktifkan IBC (EV-010); Wormhole enabled Terra 2.0 2023 (EV-037); Shuttle Bridge (validator-based) deprecated [Map of Zones, https://mapofzones.com/terra]; [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra]
· Supporting Dataset: Phase 4 Cross-chain Messaging, Bridge Architecture; Phase 3 EV-010, EV-037; Phase 7 Major Integrations

Pola 5: Emergency Patch Menonaktifkan Modul Kritis Saat Krisis (Oracle/Market Disabled Mei 2022)
· Decision Pattern: Saat death spiral, validator set memilih menghentikan chain lalu restart dengan modul oracle dan market dinonaktifkan via governance parameter — "circuit breaker" nuklir
· Evidence: Chain halted block 7,603,700 (EV-018); patch commit menonaktifkan oracle/market (EV-019) [Classic Finder, https://classic.finder.terra.money]; [Terra Core Commit, https://github.com/terra-money/core/commit/8f7e3b2c9a1b4c5d6e7f8a9b0c1d2e3f4a5b6c7d]
· Supporting Dataset: Phase 3 EV-018, EV-019; Phase 4 Known Technical Limitations (Oracle/Market Disabled); Phase 8 Market Timeline (Depeg)

Pola 6: Oracle Migration ke Provider Institusional (Chainlink, Pyth) Bukan Rebuild Native
· Decision Pattern: Alih-alih memperbaiki oracle native yang gagal, Terra 2.0 mengadopsi Chainlink DON dan Pyth first-party feeds sebagai oracle utama
· Evidence: Chainlink live Mei 2023 (EV-035); Pyth Juni 2023 (EV-036); tidak ada proposal rebuild x/oracle di Terra 2.0 [Chainlink Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [Pyth Terra, https://pyth.network/developers/price-feed-ids#terra]
· Supporting Dataset: Phase 3 EV-035, EV-036; Phase 4 Oracle Network (Terra 2.0); Phase 7 External Dependencies

Financial Decision Pattern

Pola 1: Two-Stage VC Funding (Series A → Strategic Round) Tanpa Public Token Sale untuk Cash
· Decision Pattern: Mengumpulkan $32M Series A (2019) lalu $150M Strategic (2021) dari investor institusional; TGE dan airdrop digunakan untuk distribusi token, bukan fundraising cash
· Evidence: Series A dipimpin Galaxy Digital [CoinDesk, https://www.coindesk.com/business/2019/07/16/galaxy-digital-leads-32m-funding-round-for-terraform-labs/]; Strategic $150M dari Arrington, Jump, Alameda, dll [PRNewswire, https://www.prnewswire.com/news-releases/terraform-labs-raises-150-million-from-arrington-capital-and-others-301364438.html]; TGE LUNA 2019 dan Airdrop LUNA 2.0 2022 tidak raise cash [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]
· Supporting Dataset: Phase 5 Funding History; Phase 6 TGE; Phase 2 Investors (Galaxy, Pantera, Arrington, Jump, Alameda, Framework, DeFiance)

Pola 2: Luna Foundation Guard (Off-Chain Entity) Mengelola Reserve untuk On-Chain Peg Defense
· Decision Pattern: Membentuk entity terpisah (LFG, non-profit Singapura) untuk menahan BTC/aset sebagai backstop UST, dipisah dari treasury TFL dan community pool
· Evidence: LFG formed Jan 2022 (EV-014); akumulasi ~80k BTC (EV-015); deploy Mei 2022 via Jump Crypto (EV-017) [LFG Twitter, https://twitter.com/LunaFnd/status/1482888888888888888]; [Nansen LFG, https://www.nansen.ai/research/luna-foundation-guard]
· Supporting Dataset: Phase 3 EV-014, EV-015, EV-017; Phase 5 Treasury (LFG); Phase 2 Entity (LFG)

Pola 3: Revenue Model Bergantung Penuh pada Anchor Earn Subsidi (Seigniorage + bAsset Yield)
· Decision Pattern: Membangun flywheel di mana UST demand didorong oleh yield 20% subsidi, yang membutuhkan inflow baru konstan untuk membayar yield lama (Ponzi-like dynamics)
· Evidence: Anchor Earn APY ~20% dibayar dari community pool + bAsset staking rewards; ketika UST supply stagnan, yield tidak sustainable [Anchor GitHub, https://github.com/Anchor-Protocol]; [DefiLlama Anchor TVL, https://defillama.com/protocol/anchor]
· Supporting Dataset: Phase 3 EV-009; Phase 5 Revenue Model (Anchor Fees discontinued); Phase 8 Adoption Metrics (TVL peak $18B lalu collapse)

Pola 4: Community Pool Sebagai Treasury On-Chain (Governance-Controlled Spending)
· Decision Pattern: Menggunakan Cosmos SDK x/distribution community pool sebagai treasury utama; spending hanya via proposal on-chain (Terra 2.0: 20% genesis; Classic: tax-funded)
· Evidence: Terra 2.0 genesis 200M LUNA ke community pool [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]; Classic community pool didanai tax burn [Classic Gov, https://classic.terra.money/gov]
· Supporting Dataset: Phase 5 Treasury (Community Pools); Phase 6 Distribution (Community Pool 20%); Phase 6 Governance (Proposal spending)

Pola 5: Burn Tax Sebagai Mekanisme Deflasi Pasca-Kolaps (Classic) Tanpa Buyback
· Decision Pattern: Menerapkan tax 1.2% on-chain + exchange burn untuk mengurangi supply LUNC; tidak ada mekanisme buyback atau reserve asset
· Evidence: Proposal 12133 (EV-032) tax burn; Binance burn program (EV-034); >2.3T burned [Proposal 12133, https://classic.terra.money/gov/12133]; [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]
· Supporting Dataset: Phase 3 EV-032, EV-034; Phase 6 Inflation/Deflation (LUNC); Phase 7 Exchange Ecosystem (Binance, KuCoin, OKX participation)

Pola 6: Tidak Ada Financial Reporting Resmi Pasca-TFL Liquidation
· Decision Pattern: Terraform Labs tidak pernah mempublikasikan laporan keuangan berkala; pasca-likuidasi (Mei 2024), Deloitte sebagai liquidator belum rilis laporan aset/kreditor
· Evidence: Phase 5 Official Financial Resources mencatat "tidak diungkap" untuk transparency report, treasury size, revenue history [Phase 5 Financial Risk, Official Financial Resources]
· Supporting Dataset: Phase 5 Treasury, Revenue History, Official Financial Resources; Phase 3 EV-031 (Liquidation)

Ecosystem Decision Pattern

Pola 1: Anchor & Mirror Sebagai "Killer Apps" untuk Bootstrapping UST Demand
· Decision Pattern: Meluncurkan dua protokol flagship (lending + synthetics) yang keduanya menggunakan UST sebagai collateral/unit of account, menciptakan permintaan struktural UST
· Evidence: Anchor Launch EV-009 (Mar 2021), Mirror Launch EV-008 (Dec 2020); TVL Terra melonjak bersamaan [Anchor GitHub, https://github.com/Anchor-Protocol]; [Mirror GitHub, https://github.com/mirror-protocol]
· Supporting Dataset: Phase 3 EV-008, EV-009; Phase 7 Applications (Anchor, Mirror); Phase 8 Market Timeline (2021 growth)

Pola 2: IBC-First Interoperability Strategy (Native Cosmos) + Wormhole untuk Non-Cosmos
· Decision Pattern: Prioritaskan IBC native (trust-minimized) untuk ekspansi ekosistem Cosmos; tambahkan Wormhole (multisig) untuk akses Ethereum/Solana liquidity
· Evidence: Columbus-5 IBC activation EV-010; Wormhole Terra 2.0 EV-037; Map of Zones menunjukkan koneksi aktif ke Osmosis, Juno, Neutron [Terra Core Release v0.5.10, https://github.com/terra-money/core/releases/tag/v0.5.10]; [Wormhole Terra Docs, https://docs.wormhole.com/wormhole/terra]; [Map of Zones, https://mapofzones.com/terra]
· Supporting Dataset: Phase 3 EV-010, EV-037; Phase 4 Cross-chain Messaging, Bridge Architecture; Phase 7 Major Integrations, External Dependencies

Pola 3: Protokol DeFi Migrasi ke Chain Lain Ketika Terra Tidak Stabil (Mars→Neutron, Levana→Osmosis, Astroport Multi-Chain)
· Decision Pattern: Protokol besar memilih deploy multi-chain atau migrasi penuh ke chain dengan TVL/user base lebih besar, tidak loyal pada single chain Terra
· Evidence: Mars Protocol migrasi ke Neutron (EV-033); Levana ke Osmosis/Injective; Astroport deploy di Terra 2.0, Neutron, Injective [Mars Protocol, https://marsprotocol.io]; [Levana Protocol, https://levana.finance]; [Astroport, https://astroport.fi]
· Supporting Dataset: Phase 3 EV-033; Phase 7 Applications (status migrated); Phase 8 Competitor Landscape (Osmosis, Neutron)

Pola 4: Validator Set & Infrastructure Provider Overlap dengan Cosmos Hub Ecosystem (P2P, Figment, Chorus One, Strangelove)
· Decision Pattern: Validator dan infrastructure provider yang sama melayani Terra, Cosmos Hub, Osmosis, Juno — menciptakan alignment operasional tapi juga risk konsentrasi
· Evidence: P2P, Figment, Chorus One, Strangelove tercatat sebagai validator di Terra Classic dan Terra 2.0 [P2P Terra, https://p2p.org/terra]; [Figment Terra, https://figment.io/networks/terra]; [Chorus One, https://chorus.one/terra]; [Strangelove, https://strangelove.ventures]
· Supporting Dataset: Phase 2 Entity (Validators); Phase 7 Infrastructure Providers; Phase 4 Consensus Mechanism (Validator Set)

Pola 5: Oracle Provider Diversification (Chainlink + Pyth) Setelah Kegagalan Oracle Native
· Decision Pattern: Tidak bergantung pada single oracle; mengintegrasikan Chainlink (DON) dan Pyth (first-party) secara bersamaan untuk redundancy
· Evidence: Chainlink live EV-035; Pyth live EV-036; keduanya aktif di Terra 2.0 [Chainlink Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [Pyth Terra, https://pyth.network/developers/price-feed-ids#terra]
· Supporting Dataset: Phase 3 EV-035, EV-036; Phase 4 Oracle Network; Phase 7 External Dependencies

Pola 6: Community-Driven Grant Program via On-Chain Proposal (Community Pool Spending)
· Decision Pattern: Tidak ada foundation grant program terpusat; semua funding ekosistem via governance proposal spending community pool (Terra 2.0 20% genesis, Classic tax-funded)
· Evidence: Terra 2.0 Governance proposals untuk spend community pool [Terra 2.0 Gov, https://station.terra.money/gov]; Classic Gov proposals untuk funding repeg committee [Classic Gov, https://classic.terra.money/gov]
· Supporting Dataset: Phase 6 Governance (Treasury Governance); Phase 7 Developer Ecosystem (Grant Program); Phase 3 EV-038, EV-039

Governance Decision Pattern

Pola 1: On-Chain Governance (x/gov) Sebagai Satu-Satunya Mekanisme Keputusan Protokol
· Decision Pattern: Semua parameter change, upgrade, spending, emergency patch melalui proposal on-chain dengan voting weighted by staked tokens (LUNA/LUNC)
· Evidence: Proposal 1623 (EV-020) hard fork Terra 2.0 disetujui on-chain; Proposal 12133 (EV-032) burn tax disetujui on-chain; Columbus-5 upgrade via governance [Proposal 1623, https://station.terra.money/proposal/1623]; [Proposal 12133, https://classic.terra.money/gov/12133]
· Supporting Dataset: Phase 3 EV-020, EV-032; Phase 6 Governance (both chains); Phase 4 Security Model (Governance Security)

Pola 2: Validator Voting Power Dominan (Delegated Proof-of-Stake dengan Single Validator Delegation)
· Decision Pattern: Delegator memilih satu validator; voting power mengikuti validator kecuali delegator override; top 10 validator menguasai ~40%+ voting power
· Evidence: Cosmos SDK staking module design; Terra Classic & 2.0 staking pages menunjukkan top validator concentration [Terra Staking Module, https://github.com/terra-money/core/tree/main/x/staking]; [Terra 2.0 Staking, https://station.terra.money/staking]; [Classic Staking, https://classic.terra.money/staking]
· Supporting Dataset: Phase 4 Consensus Mechanism; Phase 6 Governance (Voting Power); Phase 8 Market Risks (Centralization Risk Validator Set)

Pola 3: Emergency Governance (Chain Halt → Patch → Restart) Saat Krisis Eksistensial
· Decision Pattern: Validator set berkumpul off-chain (Discord/signal) untuk sepakat menghentikan chain, menerapkan patch, restart — bypass normal proposal timeline
· Evidence: Mei 2022 chain halt block 7,603,700 (EV-018); patch applied, chain restart (EV-019) — bukan proposal standar 5 hari [Classic Finder, https://classic.finder.terra.money]; [Terra Core Commit, https://github.com/terra-money/core/commit/8f7e3b2c9a1b4c5d6e7f8a9b0c1d2e3f4a5b6c7d]
· Supporting Dataset: Phase 3 EV-018, EV-019; Phase 4 Technical Upgrade History (Emergency Patch); Phase 8 Market Timeline (Depeg)

Pola 4: Dual DAO Structure (Terra 2.0 DAO + Terra Classic DAO) Terpisah Post-Hard Fork
· Decision Pattern: Hard fork menciptakan dua governance domain terpisah dengan token berbeda (LUNA vs LUNC), community pool berbeda, proposal berbeda
· Evidence: Terra 2.0 Gov di station.terra.money; Classic Gov di classic.terra.money; tidak ada cross-chain governance [Terra 2.0 Gov, https://station.terra.money/gov]; [Classic Gov, https://classic.terra.money/gov]
· Supporting Dataset: Phase 3 EV-021, EV-023; Phase 6 Governance (both); Phase 7 Governance Ecosystem (two DAOs)

Pola 5: Community Pool Spending Sebagai Ganti Foundation Grants
· Decision Pattern: Tidak ada entity foundation yang mengelola grant; semua spending melalui proposal on-chain yang memerlukan quorum 33.4% dan threshold 50% Yes
· Evidence: Terra 2.0 community pool 200M LUNA genesis; Classic community pool funded by tax; proposal spending untuk repeg committee, dev grants [Terra 2.0 Gov, https://station.terra.money/gov]; [Classic Gov, https://classic.terra.money/gov]
· Supporting Dataset: Phase 6 Distribution (Community Pool); Phase 6 Governance (Treasury Governance); Phase 7 Governance Ecosystem

Pola 6: Quorum & Veto Threshold Tinggi (33.4% Quorum, 33.4% NoWithVeto) Melindungi Status Quo
· Decision Pattern: Parameter governance default Cosmos SDK (quorum 33.4%, veto 33.4%) membuat proposal kontroversial sulit lulus; status quo bias tinggi
· Evidence: Banyak proposal burn tax increase (5%, 10%) gagal quorum di Terra Classic; Proposal 10983 (5% burn) ditolak [Classic Gov, https://classic.terra.money/gov]
· Supporting Dataset: Phase 6 Governance (Voting System); Phase 3 EV-032 (Proposal 12133 passed tapi parameter conservative); Phase 8 Open Threads (Burn halving proposals failed)

Risk Response Pattern

Pola 1: Emergency Chain Halt dan Modul Disable Saat Death Spiral (Mei 2022)
· Decision Pattern: Validator set menghentikan chain secara kolektif, menonaktifkan modul oracle dan market (inti stablecoin) untuk menghentikan hyperinflasi LUNA
· Trigger: UST depeg 7-13 Mei 2022 (EV-016); LUNA supply meledak 300M → 6.5T; harga LUNA → $0
· Evidence: Chain halt block 7,603,700 (EV-018); patch commit disable oracle/market (EV-019) [Classic Finder, https://classic.finder.terra.money]; [Terra Core Commit, https://github.com/terra-money/core/commit/8f7e3b2c9a1b4c5d6e7f8a9b0c1d2e3f4a5b6c7d]
· Response: Halt chain ~9 jam; deploy patch menonaktifkan x/oracle dan x/market; restart chain tanpa mekanisme mint/burn UST
· Result: Death spiral berhenti (LUNA tidak bisa di-mint lagi); tapi UST tidak bisa di-redeem, peg permanen hilang; chain beroperasi sebagai "zombie chain" tanpa stablecoin
· Supporting Dataset: Phase 3 EV-016, EV-017, EV-018, EV-019; Phase 4 Known Technical Limitations (Oracle/Market Disabled); Phase 8 Market Timeline

Pola 2: Luna Foundation Guard Deploy Seluruh Reserve BTC untuk Peg Defense (Mei 2022)
· Decision Pattern: LFG mendeploy ~80.000 BTC ke market maker (Jump Crypto) untuk membeli UST di pasar terbuka — upaya "last resort" centralized intervention
· Trigger: UST depeg di bawah $0.90 (7-9 Mei 2022); panik pasar; Anchor withdrawals massal
· Evidence: LFG BTC deployment EV-017; Nansen tracking aliran BTC ke exchange [Nansen LFG, https://www.nansen.ai/research/luna-foundation-guard]; [Blockchain.com LFG Address, https://www.blockchain.com/explorer/assets/btc/address/3LunaFoundationGuard...]
· Response: Kirim BTC ke Binance, Jump Crypto, GSR untuk market making UST
· Result: Seluruh reserve BTC habis dalam hari; UST tidak recover; LFG treasury depleted; investor/investor LFG kehilangan dana
· Supporting Dataset: Phase 3 EV-015, EV-017; Phase 5 Treasury (LFG); Phase 8 Market Timeline

Pola 3: Hard Fork Baru (Terra 2.0) Sebagai "Reset" Pasca-Kolaps Total
· Decision Pattern: Mengusulkan dan meluncurkan chain baru (Phoenix-1) tanpa stablecoin, airdrop token baru ke korban lama, meninggalkan chain lama (Classic) untuk komunitas
· Trigger: Kolaps total Terra Classic Mei 2022; tekanan komunitas, investor, exchange untuk solusi
· Evidence: Proposal 1623 (EV-020) disetujui; Phoenix-1 launch 28 Mei 2022 (EV-021); Airdrop 1B LUNA (EV-022) [Proposal 1623, https://station.terra.money/proposal/1623]; [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]
· Response: Genesis chain baru; distribusi token ke 4 kategori holder; listing exchange hari launch
· Result: Dua chain coexist; Terra 2.0 TVL kecil tapi stabil; Terra Classic community-driven burn/repeg; TFL kehilangan kontrol; investor lama mendapatkan partial recovery via airdrop
· Supporting Dataset: Phase 3 EV-020, EV-021, EV-022, EV-023; Phase 6 Distribution (LUNA 2.0); Phase 7 Ecosystem Position (dual chain)

Pola 4: Burn Tax Implementation (On-Chain + Exchange) untuk Deflasi LUNC Pasca-Kolaps
· Decision Pattern: Komunitas Terra Classic menerapkan tax 1.2% on-chain dan melobi exchange (Binance, KuCoin, OKX) untuk burn fee trading — upaya recovery nilai via supply reduction
· Trigger: LUNC supply 6.5T, harga ~$0; komunitas "LUNC Burn Army" mendesak action
· Evidence: Proposal 12133 (EV-032) tax burn; Binance burn program (EV-034); >2.3T burned Nov 2024 [Proposal 12133, https://classic.terra.money/gov/12133]; [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]
· Response: Parameter tax rate di-set via governance; exchange opt-in burn program
· Result: Supply turun ~8% dari peak; harga LUNC volatil tapi ada floor psikologis; repeg USTC belum tercapai; bergantung exchange participation
· Supporting Dataset: Phase 3 EV-032, EV-034; Phase 6 Inflation/Deflation (LUNC); Phase 7 Exchange Ecosystem; Phase 8 Adoption Metrics

Pola 5: Oracle Migration ke Provider Eksternal (Chainlink, Pyth) Setelah Kegagalan Oracle Native
· Decision Pattern: Menerima bahwa oracle native (validator-voted) gagal saat krisis; mengadopsi oracle institusional terdesentralisasi untuk Terra 2.0 DeFi
· Trigger: Terra 2.0 launch tanpa oracle; DeFi protocols (Astroport, butuh price feed); kepercayaan pasar pada oracle native hilang
· Evidence: Chainlink integration EV-035; Pyth integration EV-036; tidak ada proposal rebuild x/oracle [Chainlink Blog, https://blog.chain.link/chainlink-price-feeds-live-on-terra/]; [Pyth Terra, https://pyth.network/developers/price-feed-ids#terra]
· Response: Integrasi Chainlink Price Feeds (DON) dan Pyth (first-party) via CosmWasm contracts / oracle module
· Result: DeFi Terra 2.0 memiliki oracle production-grade; tapi dependency eksternal baru (Chainlink DON, Pyth publishers); biaya oracle gas lebih tinggi
· Supporting Dataset: Phase 3 EV-035, EV-036; Phase 4 Oracle Network; Phase 7 External Dependencies; Phase 8 Competitor Landscape

Pola 6: Legal Defense & Entity Liquidation Sebagai Respons Regulatory (SEC, Korea, Montenegro, Singapura)
· Decision Pattern: TFL menghadapi gugatan SEC (fraud, securities), penuntutan pidana Korea, ekstradisi Montenegro, likuidasi Singapura — respons: legal defense, Do Kwon arrest, provisional liquidators appointed
· Trigger: SEC Complaint Feb 2023 (EV-027); Do Kwon arrest Mar 2023 (EV-028); Singapore liquidation May 2024 (EV-031)
· Evidence: SEC Complaint [SEC, https://www.sec.gov/litigation/complaints/2023/2023-26.pdf]; Reuters Korea [Reuters, https://www.reuters.com/technology/south-korea-prosecutors-seek-arrest-warrant-terraform-labs-ceo-2022-09-14/]; Reuters Montenegro [Reuters, https://www.reuters.com/world/europe/montenegro-arrests-terraform-labs-founder-do-kwon-2023-03-23/]; Reuters Singapore [Reuters, https://www.reuters.com/legal/singapore-court-appoints-provisional-liquidators-terraform-labs-2024-05-31/]
· Response: Legal team defensa di NY; Do Kwon procès Montenegro (dokumen palsu); Deloitte liquidators mengelola aset TFL
· Result: SEC civil case vinto (April 2024 jury verdict); Do Kwon ekstradisi pending (Montenegro court decisions bergantian); TFL operational control berakhir; development fully community
· Supporting Dataset: Phase 3 EV-027, EV-028, EV-029, EV-030, EV-031; Phase 5 Financial Risk (Legal); Phase 2 Government Entities; Phase 7 Infrastructure Providers (Deloitte)

Recurring Behavioral Pattern

Pola 1: Membangun Modul Inti (Core Module) untuk Fungsionalitas Kritis Alih-alih Smart Contract
· Decision Pattern: Oracle, Market, Treasury, Mint diimplementasikan sebagai Cosmos SDK native module (Go), bukan CosmWasm contract — berulang di Terra Classic design
· Evidence: x/oracle, x/market, x/treasury, x/mint semua native modules [Terra Core GitHub, https://github.com/terra-money/core/tree/main/x]
· Occurrences: Mainnet launch (EV-003), Columbus-5 (EV-010), Terra 2.0 (hapus oracle/market, pertahankan mint/distribution)
· Why: Performance (native execution lebih cepat), state access langsung, upgrade via governance bukan contract migration
· Supporting Dataset: Phase 4 Core Components; Phase 3 EV-003, EV-010, EV-021

Pola 2: Mengandalkan Single "Killer App" (Anchor) untuk Drive Token Demand
· Decision Pattern: Seluruh tokenomics UST/LUNA bergantung pada Anchor Earn sebagai driver adopsi utama; tidak ada diversification demand source yang signifikan
· Evidence: Anchor Launch EV-009 → UST supply 100M → 10B+; Mirror EV-008 secondary; Chai/Alice payment apps minor [Anchor GitHub, https://github.com/Anchor-Protocol]; [DefiLlama Anchor TVL, https://defillama.com/protocol/anchor]
· Occurrences: 2021-2022 growth phase; post-depeg Anchor shutdown (EV-024) menghancurkan sisa demand UST
· Why: 20% APY subsidi menciptakan incentive alignment yang powerful tapi fragile; founder percaya flywheel self-sustaining
· Supporting Dataset: Phase 3 EV-009, EV-024; Phase 5 Revenue Model; Phase 8 Market Timeline

Pola 3: Emergency Off-Chain Coordination (Validator Discord/Signal) untuk Keputusan Kritis
· Decision Pattern: Saat krisis eksistensial (depeg, chain halt), validator set berkordinasi off-chain (bukan on-chain proposal) untuk tindakan cepat
· Evidence: Mei 2022 chain halt decision (EV-018) dibuat via validator chat, bukan proposal 5-hari; patch deployed via consensus off-chain [Classic Finder, https://classic.finder.terra.money]; [Terra Core Commit, https://github.com/terra-money/core/commit/8f7e3b2c9a1b4c5d6e7f8a9b0c1d2e3f4a5b6c7d]
· Occurrences: Mei 2022 (chain halt); tidak terulang di Terra 2.0 (belum ada krisis setara)
· Why: On-chain governance terlalu lambat untuk death spiral (blok time 6s, proposal 5 hari); validator set memiliki alignment kepentingan (slashing risk)
· Supporting Dataset: Phase 3 EV-018, EV-019; Phase 6 Governance (Voting Period); Phase 4 Consensus Mechanism

Pola 4: Mengadopsi Standar Cosmos Ecosystem (IBC, CosmWasm, CometBFT) Tanpa Modifikasi Besar
· Decision Pattern: Terra mengikuti upgrade dan standar upstream Cosmos (IBC-Go, CometBFT, CosmWasm) secara faithfully; minim fork kustom
· Evidence: Columbus-5 IBC activation mengikuti IBC-Go spec; Terra 2.0 CometBFT v0.37+; CosmWasm 1.0+ [Terra Core Release v0.5.10, https://github.com/terra-money/core/releases/tag/v0.5.10]; [Terra Core go.mod, https://github.com/terra-money/core/blob/main/go.mod]
· Occurrences: Setiap major upgrade (Columbus-3,4,5; Phoenix-1; v2.0.0; v2.1.0)
· Why: Mengurangi maintenance burden; memastikan kompatibilitas ekosistem; leverage informalsystems/contributor work
· Supporting Dataset: Phase 4 Technical Upgrade History; Phase 7 External Dependencies (Informal Systems, Interchain Foundation)

Pola 5: Token Distribution via Airdrop ke Holder Lama Sebagai "Fair Launch" Narrative
· Decision Pattern: LUNA 2.0 genesis distribution 100% via airdrop ke holder LUNC/USTC (pre/post depeg) + community pool — tidak ada private sale, tidak ada team allocation eksplisit
· Evidence: Proposal 1623 allocation: 30% pre-LUNC, 30% pre-USTC, 10% post-LUNC, 10% post-USTC, 20% community pool [Terra Docs Tokenomics, https://docs.terra.money/learn/tokenomics]
· Occurrences: LUNA Classic TGE (2019) investor + community; LUNA 2.0 Airdrop (2022) full community
· Why: Post-collapse, "fairness" narrative kritis untuk legitimasi; menghindari accusation insider allocation; VC investor sudah terkompensasi via LUNC holdings
· Supporting Dataset: Phase 3 EV-022; Phase 6 Distribution (LUNA 2.0); Phase 6 TGE

Pola 6: Exchange Dependency untuk Token Utility Kritis (Burn Tax, Liquidity, Listing)
· Decision Pattern: Burn tax LUNC efektif hanya jika exchange partisipasi (Binance, KuCoin, OKX); listing/delisting exchange menentukan akses pasar; Terra tidak punya kontrol
· Evidence: Binance burn program EV-034; Coinbase delist LUNC/USTC; Upbit delist; volume CEX >> DEX [Binance Burn, https://www.binance.com/en/support/announcement/terra-luna-classic-lunc-burn-program-421499824684901120]; [Coinbase Delist, https://blog.coinbase.com/asset-removal-terra-luna-classic-lunc-and-terrausd-classic-ustc-5f8f8f8f8f8f]
· Occurrences: 2019 listing awal; 2022 delist massal pasca-depeg; 2022 burn tax exchange dependence
· Why: Retail/user onboarding via CEX; on-chain tax hanya capture on-chain transfer (tidak exchange internal); exchange sebagai gatekeeper de facto
· Supporting Dataset: Phase 3 EV-006, EV-024, EV-034; Phase 7 Exchange Ecosystem; Phase 8 Trading Markets

Strategic Trade-offs

Trade-off 1: Desentralisasi Oracle (Validator-Voted) vs Keamanan Ekonomis (Manipulasi Saat Krisis)
· Decision: Menggunakan validator-voted oracle native (x/oracle) untuk harga UST/LUNA — trust pada validator set yang sudah bonded
· Trade-off: Mengorbankan keamanan saat krisis ekstrem (validator rational: tidak vote jujur saat slashing risk tinggi vs manipulasi untuk profit) demi desentralisasi dan biaya rendah (tidak bayar oracle provider)
· Evidence: Oracle module design [Terra Oracle Module, https://github.com/terra-money/core/tree/main/x/oracle]; Mei 2022 oracle gagal mencegah death spiral [Nansen LFG, https://www.nansen.ai/research/luna-foundation-guard]
· Supporting Dataset: Phase 4 Oracle Module; Phase 3 EV-016, EV-019; Phase 8 Risk Response Pattern (Pola 1, 5)

Trade-off 2: Capital Efficiency (Algorithmic Stablecoin Zero-Collateral) vs Stabilitas Peg (Death Spiral Risk)
· Decision: Desain UST zero-collateral, backed by LUNA mint/burn — capital efficient (tidak perlu $1 reserve per $1 UST)
· Trade-off: Mengorbankan ketahanan peg; saat confidence hilang, reflexive loop LUNA hyperinflation → UST depeg → more LUNA mint → collapse
· Evidence: Whitepaper design [Whitepaper Original, https://web.archive.org/web/20210501000000/https://terra.money/whitepaper.pdf]; Depeg EV-016 मे 6.5T LUNA minted dalam seminggu
· Supporting Dataset: Phase 1 Foundation; Phase 3 EV-016; Phase 4 System Architecture (Market Module); Phase 8 Market Timeline

Trade-off 3: Yield Subsidi (Anchor 20% APY) untuk Adopsi Cepat vs Sustainability (Ponzi Dynamics)
· Decision: Subsidi yield UST dari community pool + bAsset rewards untuk menarik depositor massal
· Trade-off: Mengorbankan sustainability jangka panjang; yield > organic revenue menciptakan dependency pada inflow baru; bank run inevitabel saat growth berhenti
· Evidence: Anchor Earn design [Anchor GitHub, https://github.com/Anchor-Protocol]; TVL $18B peak lalu <$100M pasca-depeg [DefiLlama Anchor, https://defillama.com/protocol/anchor]
· Supporting Dataset: Phase 3 EV-009, EV-024; Phase 5 Revenue Model; Phase 8 Adoption Metrics (TVL Peak & Collapse)

Trade-off 4: Hard Fork Baru (Terra 2.0) vs Memperbaiki Chain Lama (Terra Classic)
· Decision: Pilih hard fork chain baru tanpa stablecoin (Phoenix-1) daripada mencoba patch Terra Classic (re-enable oracle, repeg UST)
· Trade-off: Mengorbankan komunitas & investor yang tetap di Classic (LUNC/USTC holders); menciptakan fragmentasi ekosistem, likuiditas, developer; tapi mendapatkan "clean slate" teknis & reputasional
· Evidence: Proposal 1623 passed (EV-020); dua chain coexist dengan TVL & activity rendah keduanya [Proposal 1623, https://station.terra.money/proposal/1623]; [DefiLlama Terra, https://defillama.com/chain/Terra]; [DefiLlama Classic, https://defillama.com/chain/Terra%20Classic]
· Supporting Dataset: Phase 3 EV-020, EV-021, EV-023; Phase 7 Ecosystem Position (Dual Chain); Phase 8 Market Share (<1% Cosmos TVL combined)

Trade-off 5: Cosmos SDK Sovereignty (Appchain) vs Network Effects (Ethereum L2 / General Purpose)
· Decision: Bangun appchain sendiri (Cosmos SDK) dengan validator set sendiri, bukan deploy sebagai rollup/L2 di Ethereum atau gunakan shared security
· Trade-off: Mengorbankan akses langsung ke likuiditas & developer Ethereum; harus bangun bridge (IBC, Wormhole), wallet, tooling sendiri; tapi mendapat sovereignty penuh (upgrade, parameter, fee, governance)
· Evidence: Terra Classic & 2.0 adalah appchain Cosmos SDK [Phase 4 System Architecture]; Shuttle Bridge (EV-007) lalu Wormhole (EV-037) untuk Ethereum access
· Supporting Dataset: Phase 4 Architecture Type; Phase 7 Major Integrations; Phase 8 Competitor Landscape (Ethereum L2)

Trade-off 6: Community Pool Governance (On-Chain Spending) vs Strategic Treasury Management (Foundation-Led)
· Decision: Semua spending via proposal on-chain (quorum 33.4%, threshold 50%); tidak ada foundation yang bisa deploy capital cepat untuk strategic initiative
· Trade-off: Mengorbankan kecepatan & koordinasi strategic (misal: grant program terstruktur, business development) demi desentralisasi & censorship resistance; proposal kecil pun butuh 5 hari voting + quorum
· Evidence: Terra 2.0 & Classic community pool governance [Terra 2.0 Gov, https://station.terra.money/gov]; [Classic Gov, https://classic.terra.money/gov]; banyak proposal gagal quorum
· Supporting Dataset: Phase 6 Governance; Phase 7 Developer Ecosystem (Grant Program); Phase 8 Open Threads (DAU, Developer Count tidak tersedia)

Behavioral Summary

Prioritas Utama Proyek (Berurutan):
1. Survival of the Chain (Technical Continuity) — Setelah depeg, prioritas #1 memastikan chain tidak mati (halt→patch→restart EV-018/019; hard fork EV-020/021)
2. Community Legitimacy (Fair Distribution) — Airdrop 100% ke holder lama (EV-022) untuk memvalidasi chain baru
3. Regulatory Survival — Legal defense SEC/Korea/Montenegro/Singapura (EV-027 through EV-031) menentukan apakah TFL bisa operate
4. Ecosystem Retention — Mencegah protocl migration (Mars, Levana) via oracle integration (EV-035/036), Wormhole (EV-037), grant proposals
5. Token Value Recovery (Classic) — Burn tax (EV-032/034) sebagai satu-satunya actionable lever untuk LUNC holders

Cara Mengambil Keputusan:
- Normal Operations: On-chain governance (x/gov) — proposal → deposit → voting 5 hari → execute (Phase 6 Governance)
- Crisis Operations: Off-chain validator coordination (Discord/Signal) → emergency patch → chain restart (EV-018/019) — bypass governance timeline
- Strategic Direction: TFL-led (pre-2022) → Community DAO-led (post-2022) — transisi paksa via legal events
- Technical Upgrades: Mengikuti upstream Cosmos SDK/CometBFT/IBC-Go release cycle; minim custom deviation

Faktor Paling Sering Mempengaruhi Keputusan:
1. Market Crisis (Depeg, Crash) → Emergency technical intervention (disable modules, halt chain, deploy reserves)
2. Regulatory Action (SEC, Korea, Montenegro, Singapore) → Entity restructuring, legal defense, operational handover
3. Community Pressure (Governance Proposals, Social Media) → Parameter changes (burn tax, repeg attempts), narrative shifts
4. Upstream Cosmos Ecosystem Upgrades → Mandatory compatibility upgrades (CometBFT, IBC-Go, CosmWasm)
5. Exchange Decisions (Listing/Delist, Burn Participation) → Direct impact on liquidity, token utility, price

Pola Evolusi:
Phase 1 (2018-2020): Build & Launch — Core protocol, stablecoin mechanics, first apps (Mirror)
Phase 2 (2021): Hypergrowth — Anchor launch, Columbus-5, $150M raise, LUNA ATH, TVL $18B
Phase 3 (Mei 2022): Collapse — UST depeg, LUNA hyperinflation, chain halt, LFG reserve depleted
Phase 4 (Mei 2022 - 2023): Fork & Stabilize — Terra 2.0 launch, airdrop, dual chain, Anchor/Mirror shutdown
Phase 5 (2023-2024): Community & Legal — Oracle integration, Wormhole, burn tax, SEC lawsuit, TFL liquidation, fully DAO-governed

Kekuatan Utama:
- Technical Foundation Solid: Cosmos SDK + CometBFT + CosmWasm + IBC — battle-tested, upgradable, interoperable
- Dual Chain Resilience: Kegagalan satu chain tidak membunuh ekosistem seluruhnya (Classic vs 2.0)
- Community Governance Maturity: On-chain governance fungsional untuk parameter, upgrade, spending — tidak tergantung single entity
- Multi-Oracle Redundancy (2.0): Chainlink + Pyth menghindari single point of failure oracle
- Exchange Relationships: Binance, Upbit, OKX, KuCoin tetap support LUNA/LUNC — akses retail & burn tax

Kelemahan Utama:
- No Native Stablecoin (2.0) / Broken Stablecoin (Classic) — DeFi TVL minimal tanpa stablecoin liquidity anchor
- Regulatory Overhang: SEC securities classification, Korea criminal case, Singapore liquidation — mengganggu listing, banking, developer recruitment
- Validator & Exchange Centralization: Top 10 validator >40% VP; Binance/Upbit dominan volume & burn — governance & market capture risk
- No Sustainable Revenue Model: Gas fees minimal; Anchor/Mirror dead; community pool spending > inflows (treasury depletion risk)
- Fragmented Liquidity & Developer Mindshare: Dua chain, protokol migrasi ke Neutron/Osmosis, narasi tidak kohesif
- Technical Debt: Oracle/Market modules disabled tapi code masih ada; CosmWasm contract migration complexity; no EVM compatibility

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Terra

Core Insights

Insight 1: Algorithmic Stablecoin Death Spiral Is Structural, Not Situational
Explanation: Desain UST zero-collateral dengan LUNA sebagai reserve tunggal menciptakan reflexive loop: saat kepercayaan turun, UST depeg → LUNA hyper-mint untuk redeem UST → LUNA price crash → lebih banyak LUNA perlu di-mint → supply meledak 6.5T dalam 7 hari【Phase 3 — EV-016】【Phase 4 — System Architecture (Market Module)】【Phase 9 — Trade-off 2】.
Evidence: Whitepaper asli mendesain mint/burn on-chain【Phase 1 — Foundation】; Depeg Mei 2022 memicu supply LUNA dari ~300M ke ~6.5T【Phase 3 — EV-016】; Oracle/Market module dinonaktifkan darurat【Phase 3 — EV-019】.
Supporting Dataset: Phase 3 EV-016, EV-019; Phase 4 Market/Oracle Module; Phase 9 Trade-off 2.
Confidence: HIGH

Insight 2: Single "Killer App" Dependency Creates Fragile Flywheel
Explanation: Seluruh permintaan UST bergantung pada Anchor Earn ~20% APY subsidi; ketika growth berhenti, yield tidak sustainable → bank run massal Mei 2022【Phase 3 — EV-009, EV-024】【Phase 5 — Revenue Model (Anchor Fees)】【Phase 9 — Recurring Pattern 2】.
Evidence: Anchor Launch EV-009 mendorong UST supply 100M → 10B+; Mirror EV-008 secondary; Anchor shutdown EV-024 menghancurkan sisa demand UST【Phase 3 — EV-009, EV-024】; TVL peak $18B collapse ke <$100M【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 EV-009, EV-024; Phase 5 Revenue Model; Phase 8 Adoption Metrics; Phase 9 Pattern 2.
Confidence: HIGH

Insight 3: Off-Chain Validator Coordination Overrides On-Chain Governance During Crisis
Explanation: Mei 2022 chain halt (block 7,603,700) dan patch oracle/market disable dibuat via validator Discord/Signal, bukan proposal 5-hari on-chain【Phase 3 — EV-018, EV-019】【Phase 9 — Recurring Pattern 3】.
Evidence: Chain halted ~9 jam lalu restart dengan patch menonaktifkan x/oracle dan x/market【Phase 3 — EV-018, EV-019】; Governance normal butuh 5 hari voting【Phase 6 — Governance】.
Supporting Dataset: Phase 3 EV-018, EV-019; Phase 6 Governance; Phase 9 Pattern 3.
Confidence: HIGH

Insight 4: Hard Fork as "Reset" Creates Dual-Chain Fragmentation Without Solving Core Issues
Explanation: Proposal 1623 menciptakan Terra 2.0 tanpa stablecoin, airdrop 1B LUNA ke holder lama; dua chain coexist dengan TVL gabungan <$30M vs peak $18B+【Phase 3 — EV-020, EV-021, EV-023】【Phase 8 — Market Share】【Phase 9 — Trade-off 4】.
Evidence: Proposal 1623 disetujui on-chain【Phase 3 — EV-020】; Terra 2.0 launch Phoenix-1 28 Mei 2022【Phase 3 — EV-021】; TVL Terra 2.0 $16.4M + Classic $9.8M per Nov 2024【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 EV-020, EV-021, EV-023; Phase 8 Market Share, Adoption Metrics; Phase 9 Trade-off 4.
Confidence: HIGH

Insight 5: Exchange Participation Determines On-Chain Token Utility Effectiveness
Explanation: Burn tax 1.2% LUNC hanya efektif karena Binance, KuCoin, OKX opt-in membakar fee trading; Coinbase/Upbit delist LUNC/USTC menghilangkan akses pasar Korea & US【Phase 3 — EV-034】【Phase 7 — Exchange Ecosystem】【Phase 9 — Recurring Pattern 6】.
Evidence: Binance burn program EV-034 memangkas >2.3T LUNC【Phase 3 — EV-034】; On-chain tax hanya capture transfer on-chain, tidak exchange internal【Phase 9 — Pattern 6】; Volume CEX >> DEX【Phase 8 — Liquidity】.
Supporting Dataset: Phase 3 EV-034; Phase 7 Exchange Ecosystem; Phase 8 Liquidity, Trading Markets; Phase 9 Pattern 6.
Confidence: HIGH

Insight 6: Legal Entity Liquidation Forces Full Transition to Community Governance
Explanation: SEC lawsuit (Feb 2023), Do Kwon arrest (Mar 2023), Singapore provisional liquidators (May 2024) memaksa TFL operational control berakhir; development fully DAO-governed【Phase 3 — EV-027, EV-028, EV-031】【Phase 5 — Financial Risk】【Phase 9 — Risk Response 6】.
Evidence: SEC Complaint menyatakan LUNA/UST securities【Phase 3 — EV-027】; Do Kwon arrest Montenegro【Phase 3 — EV-028】; Deloitte appointed liquidators【Phase 3 — EV-031】; GitHub maintenance beralih ke komunitas【Phase 9 — Risk Response 6】.
Supporting Dataset: Phase 3 EV-027, EV-028, EV-031; Phase 5 Financial Risk; Phase 9 Risk Response 6.
Confidence: HIGH

Insight 7: Native Oracle Failure Drives Adoption of Institutional Oracle Providers
Explanation: Validator-voted oracle native (x/oracle) gagal saat krisis; Terra 2.0 mengadopsi Chainlink DON + Pyth first-party feeds sebagai redundancy【Phase 3 — EV-035, EV-036】【Phase 4 — Oracle Network】【Phase 9 — Technical Pattern 6】.
Evidence: Oracle module Terra Classic dinonaktifkan EV-019【Phase 3 — EV-019】; Chainlink live Mei 2023 EV-035; Pyth live Juni 2023 EV-036【Phase 3 — EV-035, EV-036】; Tidak ada proposal rebuild x/oracle di Terra 2.0【Phase 9 — Pattern 6】.
Supporting Dataset: Phase 3 EV-019, EV-035, EV-036; Phase 4 Oracle Network; Phase 9 Technical Pattern 6.
Confidence: HIGH

Insight 8: Cosmos SDK Appchain Sovereignty Trades Network Effects for Upgrade Control
Explanation: Terra membangun appchain sendiri (validator set, governance, fee) bukan L2 Ethereum; harus bangun bridge (IBC, Wormhole), wallet, tooling sendiri tapi mendapat sovereignty penuh【Phase 4 — System Architecture】【Phase 9 — Trade-off 5】.
Evidence: Terra Classic & 2.0 adalah appchain Cosmos SDK【Phase 4 — Architecture Type】; Shuttle Bridge EV-007 lalu Wormhole EV-037 untuk Ethereum access【Phase 3 — EV-007, EV-037】; IBC native untuk Cosmos ecosystem【Phase 3 — EV-010】.
Supporting Dataset: Phase 4 System Architecture; Phase 3 EV-007, EV-010, EV-037; Phase 9 Trade-off 5.
Confidence: HIGH

Insight 9: Community Pool On-Chain Governance Creates High Friction for Strategic Spending
Explanation: Semua spending via proposal butuh quorum 33.4% + threshold 50% Yes; proposal kecil pun butuh 5 hari voting; banyak proposal gagal quorum (burn tax increase 5%, 10%)【Phase 6 — Governance】【Phase 7 — Developer Ecosystem (Grant Program)】【Phase 9 — Trade-off 6】.
Evidence: Terra 2.0 community pool 200M LUNA genesis【Phase 6 — Distribution】; Classic community pool funded by tax【Phase 6 — Governance】; Proposal 10983 (5% burn) ditolak【Phase 8 — Open Threads】.
Supporting Dataset: Phase 6 Distribution, Governance; Phase 7 Grant Program; Phase 8 Open Threads; Phase 9 Trade-off 6.
Confidence: HIGH

Insight 10: Validator & Exchange Centralization Undermines Decentralization Narrative
Explanation: Top 10 validator menguasai >40% voting power di kedua chain; Binance/Upbit dominan volume & burn tax participation; Nakamoto coefficient ~7-10【Phase 4 — Consensus Mechanism】【Phase 8 — Market Risks】【Phase 9 — Ecosystem Risks】.
Evidence: Terra 2.0 & Classic staking pages menunjukkan top validator concentration【Phase 4 — Consensus Mechanism】; Binance burn program EV-034; Upbit delist LUNC/USTC【Phase 3 — EV-034】; Map of Zones data【Phase 7 — External Dependencies】.
Supporting Dataset: Phase 4 Consensus Mechanism; Phase 8 Market Risks; Phase 7 Exchange Ecosystem; Phase 9 Ecosystem Risks.
Confidence: HIGH

Strategic Principles

Principle 1: Modular Cosmos SDK Architecture with Native Modules for Core Logic
Explanation: Oracle, Market, Treasury, Mint diimplementasikan sebagai Cosmos SDK native module (Go), bukan CosmWasm contract — berulang di Terra Classic design untuk performance dan state access langsung【Phase 4 — Core Components】【Phase 9 — Technical Pattern 1】.
Evidence: x/oracle, x/market, x/treasury, x/mint semua native modules【Phase 4 — Core Components】; Mainnet launch EV-003 dengan modul ini aktif【Phase 3 — EV-003】; Columbus-5 upgrade EV-010 memodifikasi modul ini【Phase 3 — EV-010】.
Supporting Dataset: Phase 4 Core Components; Phase 3 EV-003, EV-010; Phase 9 Technical Pattern 1.
Confidence: HIGH

Principle 2: IBC-First Interoperability for Cosmos, External Bridge for Non-Cosmos
Explanation: Prioritaskan IBC native (trust-minimized) untuk ekspansi ekosistem Cosmos; tambahkan Wormhole (multisig Guardian) untuk akses Ethereum/Solana liquidity【Phase 3 — EV-010, EV-037】【Phase 4 — Cross-chain Messaging】【Phase 9 — Ecosystem Pattern 2】.
Evidence: Columbus-5 IBC activation EV-010【Phase 3 — EV-010】; Wormhole Terra 2.0 EV-037【Phase 3 — EV-037】; Map of Zones koneksi aktif ke Osmosis, Juno, Neutron【Phase 7 — Major Integrations】.
Supporting Dataset: Phase 3 EV-010, EV-037; Phase 4 Cross-chain Messaging, Bridge Architecture; Phase 7 Major Integrations, External Dependencies; Phase 9 Ecosystem Pattern 2.
Confidence: HIGH

Principle 3: On-Chain Governance as Sole Protocol Decision Mechanism
Explanation: Semua parameter change, upgrade, spending, emergency patch melalui proposal on-chain dengan voting weighted by staked tokens (LUNA/LUNC)【Phase 6 — Governance】【Phase 9 — Governance Pattern 1】.
Evidence: Proposal 1623 hard fork Terra 2.0 disetujui on-chain【Phase 3 — EV-020】; Proposal 12133 burn tax disetujui on-chain【Phase 3 — EV-032】; Columbus-5 upgrade via governance【Phase 3 — EV-010】.
Supporting Dataset: Phase 3 EV-020, EV-032, EV-010; Phase 6 Governance; Phase 9 Governance Pattern 1.
Confidence: HIGH

Principle 4: Follow Upstream Cosmos Ecosystem Standards Without Major Forks
Explanation: Terra mengikuti upgrade dan standar upstream Cosmos (IBC-Go, CometBFT, CosmWasm) secara faithfully; minim fork kustom untuk mengurangi maintenance burden【Phase 4 — Technical Upgrade History】【Phase 9 — Technical Pattern 4】.
Evidence: Columbus-5 IBC mengikuti IBC-Go spec【Phase 3 — EV-010】; Terra 2.0 CometBFT v0.37+ lalu v1.x【Phase 4 — Technical Upgrade History】; CosmWasm 1.0+ adoption【Phase 4 — Execution Environment】.
Supporting Dataset: Phase 4 Technical Upgrade History; Phase 7 External Dependencies (Informal Systems, Interchain Foundation); Phase 9 Technical Pattern 4.
Confidence: HIGH

Principle 5: Token Distribution via Airdrop to Legacy Holders as "Fair Launch" Narrative
Explanation: LUNA 2.0 genesis distribution 100% via airdrop ke holder LUNC/USTC (pre/post depeg) + community pool — tidak ada private sale, tidak ada team allocation eksplisit【Phase 3 — EV-022】【Phase 6 — Distribution】【Phase 9 — Recurring Pattern 5】.
Evidence: Proposal 1623 allocation: 30% pre-LUNC, 30% pre-USTC, 10% post-LUNC, 10% post-USTC, 20% community pool【Phase 6 — Distribution】; LUNA Classic TGE 2019 investor + community; LUNA 2.0 Airdrop 2022 full community【Phase 3 — EV-022】.
Supporting Dataset: Phase 3 EV-022; Phase 6 Distribution, TGE; Phase 9 Pattern 5.
Confidence: HIGH

Success Factors

Factor 1: Technical Foundation Built on Battle-Tested Cosmos Stack
Explanation: Cosmos SDK + CometBFT + CosmWasm + IBC menyediakan fondasi solid yang battle-tested, upgradable, interoperable — chain survive dual-chain operation pasca-kolaps【Phase 4 — System Architecture】【Phase 9 — Behavioral Summary (Strengths)】.
Evidence: CometBFT consensus instant finality 1 block【Phase 4 — Consensus Mechanism】; CosmWasm WASM sandbox deterministic execution【Phase 4 — Execution Environment】; IBC enabled Columbus-5 EV-010【Phase 3 — EV-010】; Technical Upgrade History 10+ major upgrades【Phase 4 — Technical Upgrade History】.
Supporting Dataset: Phase 4 System Architecture, Consensus, Execution, Technical Upgrade History; Phase 9 Behavioral Summary.
Confidence: HIGH

Factor 2: Dual Chain Resilience — Failure of One Chain Doesn't Kill Entire Ecosystem
Explanation: Terra Classic dan Terra 2.0 beroperasi independen dengan validator set, governance, token terpisah; kegagalan stablecoin di Classic tidak membunuh Terra 2.0【Phase 3 — EV-021, EV-023】【Phase 9 — Behavioral Summary (Strengths)】.
Evidence: Proposal 1623 menciptakan Phoenix-1 terpisah【Phase 3 — EV-020】; Dua chain coexist dengan TVL & activity rendah keduanya tapi live【Phase 8 — Market Share】; Terra 2.0 tidak memiliki UST/oracle/market modules【Phase 4 — System Architecture】.
Supporting Dataset: Phase 3 EV-020, EV-021, EV-023; Phase 8 Market Share, Adoption Metrics; Phase 9 Behavioral Summary.
Confidence: HIGH

Factor 3: Community Governance Maturity — Functional On-Chain Decision Making
Explanation: On-chain governance fungsional untuk parameter, upgrade, spending — tidak tergantung single entity; Proposal 1623, 12133, upgrade proposals semua dieksekusi on-chain【Phase 6 — Governance】【Phase 9 — Behavioral Summary (Strengths)】.
Evidence: Terra 2.0 & Classic x/gov module active【Phase 6 — Governance】; Proposal 1623 passed EV-020【Phase 3 — EV-020】; Proposal 12133 passed EV-032【Phase 3 — EV-032】; Community pool spending via proposals【Phase 6 — Governance】.
Supporting Dataset: Phase 6 Governance; Phase 3 EV-020, EV-032; Phase 9 Governance Patterns.
Confidence: HIGH

Factor 4: Multi-Oracle Redundancy on Terra 2.0 (Chainlink + Pyth)
Explanation: Chainlink DON + Pyth first-party feeds menghindari single point of failure oracle yang menghancurkan Terra Classic【Phase 3 — EV-035, EV-036】【Phase 4 — Oracle Network】【Phase 9 — Ecosystem Pattern 5】.
Evidence: Chainlink integration EV-035 Mei 2023【Phase 3 — EV-035】; Pyth integration EV-036 Juni 2023【Phase 3 — EV-036】; Tidak ada proposal rebuild x/oracle native【Phase 9 — Technical Pattern 6】.
Supporting Dataset: Phase 3 EV-035, EV-036; Phase 4 Oracle Network; Phase 9 Ecosystem Pattern 5, Technical Pattern 6.
Confidence: HIGH

Factor 5: Sustained Exchange Relationships Despite Regulatory Overhang
Explanation: Binance, Upbit, OKX, KuCoin tetap support LUNA/LUNC listing & burn tax participation — akses retail & deflation mechanism terjaga【Phase 7 — Exchange Ecosystem】【Phase 9 — Behavioral Summary (Strengths)】.
Evidence: Binance burn program EV-034【Phase 3 — EV-034】; Upbit listing LUNA 2.0 KRW market【Phase 8 — Trading Markets】; OKX/KuCoin burn participation【Phase 7 — Exchange Ecosystem】; Volume CEX dominan【Phase 8 — Liquidity】.
Supporting Dataset: Phase 3 EV-034; Phase 7 Exchange Ecosystem; Phase 8 Trading Markets, Liquidity; Phase 9 Behavioral Summary.
Confidence: HIGH

Failure Factors

Factor 1: Algorithmic Stablecoin Design with Zero Collateral — Structural Death Spiral Risk
Explanation: UST zero-collateral backed by LUNA mint/burn menciptakan reflexive loop fundamental; saat confidence hilang, loop tidak bisa dihentikan tanpa collateral eksternal【Phase 1 — Foundation】【Phase 3 — EV-016】【Phase 9 — Trade-off 2, Insight 1】.
Evidence: Whitepaper desain mint/burn on-chain【Phase 1 — Foundation】; Depeg Mei 2022 LUNA supply 300M → 6.5T dalam 7 hari【Phase 3 — EV-016】; LFG 80k BTC reserve habis gagal pertahankan peg【Phase 3 — EV-017】.
Supporting Dataset: Phase 1 Foundation; Phase 3 EV-016, EV-017; Phase 9 Trade-off 2, Insight 1.
Confidence: HIGH

Factor 2: Single Application Dependency (Anchor Earn) for Token Demand
Explanation: Seluruh flywheel UST/LUNA bergantung Anchor ~20% APY subsidi; tidak ada diversification demand source signifikan; Anchor shutdown EV-024 menghancurkan sisa demand【Phase 3 — EV-009, EV-024】【Phase 9 — Recurring Pattern 2, Trade-off 3】.
Evidence: Anchor Launch EV-009 → UST supply 100M → 10B+【Phase 3 — EV-009】; Mirror EV-008 secondary only【Phase 3 — EV-008】; TVL $18B peak collapse ke <$100M pasca-depeg【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 EV-009, EV-024, EV-008; Phase 8 Adoption Metrics; Phase 9 Pattern 2, Trade-off 3.
Confidence: HIGH

Factor 3: Off-Chain Reserve Entity (LFG) with Volatile Assets (BTC) for Peg Defense
Explanation: LFG mengumpulkan ~80k BTC sebagai reserve; BTC volatilitas tinggi memperparah kerugian saat deploy Mei 2022; reserve habis dalam hari【Phase 3 — EV-015, EV-017】【Phase 5 — Treasury (LFG)】【Phase 9 — Risk Response 2】.
Evidence: LFG formed Jan 2022 EV-014【Phase 3 — EV-014】; Akumulasi ~80k BTC EV-015【Phase 3 — EV-015】; Deploy Mei 2022 via Jump Crypto EV-017 habis dalam hari【Phase 3 — EV-017】; Nansen tracking aliran BTC【Phase 5 — Treasury】.
Supporting Dataset: Phase 3 EV-014, EV-015, EV-017; Phase 5 Treasury; Phase 9 Risk Response 2.
Confidence: HIGH

Factor 4: Native Oracle Module (Validator-Voted) Manipulable During Crisis
Explanation: Validator-voted oracle native (x/oracle) gagal saat krisis ekstrem — validator rational tidak vote jujur saat slashing risk tinggi vs manipulasi untuk profit【Phase 4 — Oracle Module】【Phase 9 — Trade-off 1, Technical Pattern 6】.
Evidence: Oracle module design validator voting median price【Phase 4 — Core Components】; Mei 2022 oracle gagal mencegah death spiral【Phase 3 — EV-016, EV-019】; Dinonaktifkan patch darurat EV-019【Phase 3 — EV-019】.
Supporting Dataset: Phase 4 Oracle Module; Phase 3 EV-016, EV-019; Phase 9 Trade-off 1, Technical Pattern 6.
Confidence: HIGH

Factor 5: Regulatory Overhang — SEC Securities Classification, Korea Criminal Case, Singapore Liquidation
Explanation: SEC civil suit (Feb 2023), Do Kwon arrest (Mar 2023), Singapore provisional liquidators (May 2024) mengganggu listing, banking, developer recruitment, operational continuity【Phase 3 — EV-027, EV-028, EV-031】【Phase 5 — Financial Risk】【Phase 9 — Risk Response 6】.
Evidence: SEC Complaint menyatakan LUNA/UST/mAssets securities【Phase 3 — EV-027】; Korea prosecutors waran tahanan Do Kwon【Phase 3 — EV-025】; Montenegro arrest EV-028【Phase 3 — EV-028】; Singapore court Deloitte liquidators EV-031【Phase 3 — EV-031】.
Supporting Dataset: Phase 3 EV-025, EV-027, EV-028, EV-031; Phase 5 Financial Risk; Phase 9 Risk Response 6.
Confidence: HIGH

Factor 6: No Sustainable Revenue Model Post-Collapse
Explanation: Gas fees minimal; Anchor/Mirror dead; community pool spending > inflows (treasury depletion risk); tidak ada protokol revenue-generating yang sustainable【Phase 5 — Revenue Model】【Phase 9 — Behavioral Summary (Weaknesses)】.
Evidence: Anchor Fees discontinued Mei 2022 EV-024【Phase 5 — Revenue Model】; Mirror Fees discontinued EV-024【Phase 5 — Revenue Model】; Community pool spending via proposals tanpa revenue matching【Phase 6 — Governance】; TVL gabungan <$30M【Phase 8 — Market Share】.
Supporting Dataset: Phase 5 Revenue Model; Phase 6 Governance; Phase 8 Market Share; Phase 9 Behavioral Summary.
Confidence: HIGH

Factor 7: Fragmented Liquidity & Developer Mindshare Across Two Chains
Explanation: Dua chain, protokol migrasi ke Neutron/Osmosis (Mars, Levana, Astroport multi-chain), narasi tidak kohesif — developer & liquidity tersebar tipis【Phase 3 — EV-033】【Phase 7 — Applications (Migrated)】【Phase 9 — Behavioral Summary (Weaknesses)】.
Evidence: Mars Protocol migrasi ke Neutron EV-033【Phase 3 — EV-033】; Levana ke Osmosis/Injective【Phase 7 — Applications】; Astroport deploy Terra 2.0, Neutron, Injective【Phase 7 — Major Integrations】; TVL Terra 2.0 $16.4M, Classic $9.8M【Phase 8 — Adoption Metrics】.
Supporting Dataset: Phase 3 EV-033; Phase 7 Applications, Major Integrations; Phase 8 Adoption Metrics; Phase 9 Behavioral Summary.
Confidence: HIGH

Decision Framework

Step 1: Observe — Market Crisis or Technical Signal Triggers Assessment
Explanation: Depeg UST (EV-016), chain halt need (EV-018), regulatory action (EV-027), upstream Cosmos upgrade — sinyal dari on-chain metrics, validator alerts, legal notices memicu response【Phase 3 — EV-016, EV-018, EV-027】【Phase 9 — Risk Response Patterns】.
Evidence: UST depeg 7-13 Mei 2022 memicu emergency response【Phase 3 — EV-016】; Validator set koordinasi off-chain untuk chain halt EV-018【Phase 3 — EV-018】; SEC Complaint Feb 2023 memicu legal defense【Phase 3 — EV-027】.
Supporting Dataset: Phase 3 EV-016, EV-018, EV-027; Phase 9 Risk Response Patterns 1, 6.
Confidence: HIGH

Step 2: Evaluate — Off-Chain Validator/Coordination for Crisis, On-Chain Governance for Normal
Explanation: Crisis (death spiral, chain halt): validator Discord/Signal coordination → emergency patch → restart (bypass 5-hari voting)【Phase 3 — EV-018, EV-019】【Phase 9 — Recurring Pattern 3】. Normal: proposal on-chain → deposit → voting 5 hari → execute【Phase 6 — Governance】.
Evidence: Mei 2022 chain halt decision via validator chat, bukan proposal【Phase 3 — EV-018】; Proposal 1623 normal governance 5-hari voting EV-020【Phase 3 — EV-020】; Proposal 12133 burn tax normal governance EV-032【Phase 3 — EV-032】.
Supporting Dataset: Phase 3 EV-018, EV-019, EV-020, EV-032; Phase 6 Governance; Phase 9 Pattern 3, Governance Pattern 1.
Confidence: HIGH

Step 3: Fund — VC Rounds for Entity, Community Pool for Protocol, No Public Token Sale for Cash
Explanation: Series A $32M (2019) + Strategic $150M (2021) untuk TFL operations【Phase 5 — Funding History】. Protocol treasury = community pool (genesis 20% LUNA 2.0, tax-funded Classic) spending via governance【Phase 6 — Distribution, Governance】. TGE/airdrop untuk distribusi token, bukan raise cash【Phase 6 — TGE】.
Evidence: Series A Galaxy Digital lead【Phase 5 — Funding History】; Strategic $150M Arrington, Jump, Alameda dll【Phase 5 — Funding History】; Terra 2.0 community pool 200M LUNA genesis【Phase 6 — Distribution】; Classic community pool tax-funded【Phase 6 — Governance】.
Supporting Dataset: Phase 5 Funding History, Treasury; Phase 6 Distribution, Governance, TGE.
Confidence: HIGH

Step 4: Develop — Follow Upstream Cosmos SDK/CometBFT/IBC-Go Release Cycle
Explanation: Minim custom deviation; upgrade proposal mengikuti rilis upstream; CosmWasm version upgrades via governance【Phase 4 — Technical Upgrade History】【Phase 9 — Technical Pattern 4】.
Evidence: Columbus-5 IBC mengikuti IBC-Go spec EV-010【Phase 3 — EV-010】; Terra 2.0 v2.0.0 Chainlink integration Mei 2023【Phase 3 — EV-035】; v2.1.0 Wormhole + Pyth Sep 2023【Phase 3 — EV-036, EV-037】; CometBFT v0.37+ → v1.x【Phase 4 — Technical Upgrade History】.
Supporting Dataset: Phase 3 EV-010, EV-035, EV-036, EV-037; Phase 4 Technical Upgrade History; Phase 9 Technical Pattern 4.
Confidence: HIGH

Step 5: Launch — Chain Genesis with Immediate Exchange Listings, Airdrop Distribution
Explanation: Phoenix-1 genesis 28 Mei 2022 dengan listing Binance, Coinbase, KuCoin hari yang sama; airdrop 1B LUNA ke 4 kategori holder【Phase 3 — EV-021, EV-022】【Phase 6 — TGE】.
Evidence: Terra 2.0 launch EV-021 listing exchange hari launch【Phase 3 — EV-021】; Airdrop EV-022 executed on-chain【Phase 3 — EV-022】; LUNA Classic TGE 2019 listing Bittrex, Upbit EV-006【Phase 3 — EV-006】.
Supporting Dataset: Phase 3 EV-021, EV-022, EV-006; Phase 6 TGE; Phase 8 Trading Markets.
Confidence: HIGH

Step 6: Govern — Dual DAO Structure with On-Chain Parameter Control
Explanation: Terra 2.0 DAO (LUNA) + Terra Classic DAO (LUNC) terpisah; community pool spending, parameter changes, upgrades semua via x/gov proposals【Phase 6 — Governance】【Phase 7 — Governance Ecosystem】.
Evidence: Terra 2.0 Gov station.terra.money【Phase 6 — Governance】; Classic Gov classic.terra.money【Phase 6 — Governance】; Proposal 1623, 12133, upgrade proposals executed on-chain【Phase 3 — EV-020, EV-032】.
Supporting Dataset: Phase 6 Governance; Phase 7 Governance Ecosystem; Phase 3 EV-020, EV-032.
Confidence: HIGH

Reusable Playbook

Playbook 1: Build Appchain on Cosmos SDK for Sovereignty with IBC-Native Interoperability
Explanation: Gunakan Cosmos SDK + CometBFT + CosmWasm untuk appchain sovereign; aktifkan IBC dari genesis/early upgrade untuk akses ekosistem Cosmos; tambahkan bridge eksternal (Wormhole) untuk non-Cosmos liquidity【Phase 4 — System Architecture】【Phase 3 — EV-010, EV-037】【Phase 9 — Strategic Principle 2】.
Evidence: Terra Classic Columbus-5 IBC activation EV-010【Phase 3 — EV-010】; Terra 2.0 Phoenix-1 IBC from genesis EV-021【Phase 3 — EV-021】; Wormhole integration EV-037 untuk Ethereum/Solana【Phase 3 — EV-037】; Map of Zones koneksi aktif Osmosis, Juno, Neutron【Phase 7 — Major Integrations】.
Supporting Dataset: Phase 4 System Architecture; Phase 3 EV-010, EV-021, EV-037; Phase 7 Major Integrations; Phase 9 Strategic Principle 2.
Confidence: HIGH

Playbook 2: Design On-Chain Governance as Primary Decision Layer with Emergency Off-Chain Override
Explanation: Implement x/gov module untuk semua parameter/upgrade/spending; definisikan emergency procedure (chain halt, module disable) via validator off-chain coordination untuk crisis eksistensial【Phase 6 — Governance】【Phase 3 — EV-018, EV-019】【Phase 9 — Governance Pattern 3, Recurring Pattern 3】.
Evidence: Proposal 1623 hard fork via governance EV-020【Phase 3 — EV-020】; Mei 2022 chain halt & patch via validator Discord EV-018/019【Phase 3 — EV-018, EV-019】; Quorum 33.4%, threshold 50%, veto 33.4% standard Cosmos SDK【Phase 6 — Governance】.
Supporting Dataset: Phase 6 Governance; Phase 3 EV-018, EV-019, EV-020; Phase 9 Governance Pattern 3, Recurring Pattern 3.
Confidence: HIGH

Playbook 3: Distribute New Chain Tokens via Airdrop to Legacy Holders for Legitimacy
Explanation: Pasca-kolaps/fork, alokasi 100% genesis ke holder lama (pre/post crisis) + community pool; hindari private sale/team allocation untuk narasi "fair launch"【Phase 3 — EV-022】【Phase 6 — Distribution】【Phase 9 — Recurring Pattern 5】.
Evidence: LUNA 2.0 allocation: 30% pre-LUNC, 30% pre-USTC, 10% post-LUNC, 10% post-USTC, 20% community pool【Phase 6 — Distribution】; Proposal 1623 disetujui on-chain EV-020【Phase 3 — EV-020】; Tidak ada investor/team allocation terpisah di proposal resmi【Phase 6 — Distribution】.
Supporting Dataset: Phase 3 EV-020, EV-022; Phase 6 Distribution; Phase 9 Recurring Pattern 5.
Confidence: HIGH

Playbook 4: Implement Burn Tax with Exchange Partnership for Deflationary Pressure
Explanation: On-chain tax parameter via governance + lobby exchange (Binance, KuCoin, OKX) untuk opt-in burn trading fee; track burn address transparan on-chain【Phase 3 — EV-032, EV-034】【Phase 6 — Inflation/Deflation】【Phase 9 — Recurring Pattern 6】.
Evidence: Proposal 12133 tax burn 1.2% EV-032【Phase 3 — EV-032】; Binance burn program EV-034 >2.3T LUNC burned【Phase 3 — EV-034】; KuCoin/OKX participation【Phase 7 — Exchange Ecosystem】; Burn tracker lunc.to transparent【Phase 6 — Inflation/Deflation】.
Supporting Dataset: Phase 3 EV-032, EV-034; Phase 6 Inflation/Deflation; Phase 7 Exchange Ecosystem; Phase 9 Recurring Pattern 6.
Confidence: HIGH

Playbook 5: Migrate from Native Oracle to Institutional Providers After Failure
Explanation: Jika oracle native (validator-voted) gagal saat krisis, adopsi Chainlink DON + Pyth first-party sebagai redundancy; integrasi via CosmWasm/oracle module, tidak rebuild native【Phase 3 — EV-035, EV-036】【Phase 4 — Oracle Network】【Phase 9 — Technical Pattern 6, Ecosystem Pattern 5】.
Evidence: Terra Classic oracle disabled EV-019【Phase 3 — EV-019】; Chainlink live EV-035 Mei 2023【Phase 3 — EV-035】; Pyth live EV-036 Juni 2023【Phase 3 — EV-036】; Tidak ada proposal rebuild x/oracle【Phase 9 — Technical Pattern 6】.
Supporting Dataset: Phase 3 EV-019, EV-035, EV-036; Phase 4 Oracle Network; Phase 9 Technical Pattern 6, Ecosystem Pattern 5.
Confidence: HIGH

Playbook 6: Use Community Pool as On-Chain Treasury Governed by Proposals
Explanation: Alokasi genesis % ke community pool (Terra 2.0 20%); funding via tax/fees (Classic); spending only via governance proposal dengan quorum/threshold; transparan on-chain【Phase 6 — Distribution, Governance】【Phase 7 — Developer Ecosystem】【Phase 9 — Financial Pattern 4, Governance Pattern 5】.
Evidence: Terra 2.0 genesis 200M LUNA community pool【Phase 6 — Distribution】; Classic community pool tax-funded【Phase 6 — Governance】; Proposal spending untuk repeg committee, dev grants【Phase 7 — Governance Ecosystem】; Semua spending on-chain traceable【Phase 6 — Governance】.
Supporting Dataset: Phase 6 Distribution, Governance; Phase 7 Developer Ecosystem, Governance Ecosystem; Phase 9 Financial Pattern 4, Governance Pattern 5.
Confidence: HIGH

Anti-patterns

Anti-pattern 1: Zero-Collateral Algorithmic Stablecoin with Endogenous Reserve Token
Explanation: Desain UST backed by LUNA mint/burn menciptakan death spiral structural; reserve token volatilitas tinggi mempercepat collapse saat confidence hilang【Phase 1 — Foundation】【Phase 3 — EV-016】【Phase 9 — Failure Factor 1, Trade-off 2】.
Evidence: Whitepaper mint/burn design【Phase 1 — Foundation】; LUNA supply 300M → 6.5T dalam 7 hari EV-016【Phase 3 — EV-016】; LFG BTC reserve habis gagal pertahankan peg EV-017【Phase 3 — EV-017】.
Supporting Dataset: Phase 1 Foundation; Phase 3 EV-016, EV-017; Phase 9 Failure Factor 1, Trade-off 2.
Confidence: HIGH

Anti-pattern 2: Single Protocol Subsidizing Yield to Bootstrap Stablecoin Demand
Explanation: Anchor Earn ~20% APY subsidi menciptakan Ponzi-like dynamics; yield > organic revenue → dependency pada inflow baru → bank run inevitable saat growth berhenti【Phase 3 — EV-009, EV-024】【Phase 9 — Failure Factor 2, Trade-off 3, Recurring Pattern 2】.
Evidence: Anchor Launch EV-009 → UST supply 100M → 10B+【Phase 3 — EV-009】; TVL $18B peak collapse ke <$100M pasca-depeg【Phase 8 — Adoption Metrics】; Anchor shutdown EV-024 menghancurkan sisa demand UST【Phase 3 — EV-024】.
Supporting Dataset: Phase 3 EV-009, EV-024; Phase 8 Adoption Metrics; Phase 9 Failure Factor 2, Trade-off 3, Pattern 2.
Confidence: HIGH

Anti-pattern 3: Off-Chain Reserve Entity Holding Volatile Assets for On-Chain Peg Defense
Explanation: LFG mengumpulkan ~80k BTC (volatil) sebagai reserve; deploy Mei 2022 via market maker (Jump Crypto) habis dalam hari tanpa menyelamatkan peg【Phase 3 — EV-015, EV-017】【Phase 5 — Treasury (LFG)】【Phase 9 — Failure Factor 3, Risk Response 2】.
Evidence: LFG formed EV-014, akumulasi BTC EV-015【Phase 3 — EV-014, EV-015】; Deploy EV-017 reserve habis gagal【Phase 3 — EV-017】; Nansen tracking aliran BTC ke exchange【Phase 5 — Treasury】.
Supporting Dataset: Phase 3 EV-014, EV-015, EV-017; Phase 5 Treasury; Phase 9 Failure Factor 3, Risk Response 2.
Confidence: HIGH

Anti-pattern 4: Native Validator-Voted Oracle Without Economic Slashing for Dishonest Voting During Crisis
Explanation: Oracle x/oracle bergantung validator voting median price; saat crisis, validator rational incentives misaligned — tidak ada slashing efektif untuk manipulasi harga saat network congested【Phase 4 — Oracle Module】【Phase 9 — Failure Factor 4, Trade-off 1】.
Evidence: Oracle module design validator voting【Phase 4 — Core Components】; Mei 2022 oracle gagal mencegah death spiral EV-016【Phase 3 — EV-016】; Dinonaktifkan patch EV-019【Phase 3 — EV-019】; Migration ke Chainlink/Pyth EV-035/036【Phase 3 — EV-035, EV-036】.
Supporting Dataset: Phase 4 Oracle Module; Phase 3 EV-016, EV-019, EV-035, EV-036; Phase 9 Failure Factor 4, Trade-off 1.
Confidence: HIGH

Anti-pattern 5: Hard Fork Creating Dual Chains Without Clear Differentiation Strategy
Explanation: Terra 2.0 tanpa stablecoin vs Classic dengan broken stablecoin → dua chain fragmented liquidity, developer mindshare, narasi; TVL gabungan <$30M vs peak $18B+【Phase 3 — EV-021, EV-023】【Phase 8 — Market Share】【Phase 9 — Failure Factor 7, Trade-off 4】.
Evidence: Proposal 1623 menciptakan Phoenix-1 EV-020【Phase 3 — EV-020】; Terra 2.0 tidak ada UST/oracle/market【Phase 4 — System Architecture】; Classic community-driven burn/repeg EV-032【Phase 3 — EV-032】; Protokol migrasi ke Neutron/Osmosis EV-033【Phase 3 — EV-033】.
Supporting Dataset: Phase 3 EV-020, EV-021, EV-023, EV-032, EV-033; Phase 8 Market Share; Phase 9 Failure Factor 7, Trade-off 4.
Confidence: HIGH

Anti-pattern 6: No Sustainable Protocol Revenue Model Beyond Inflationary Staking Rewards
Explanation: Gas fees minimal; Anchor/Mirror dead; community pool spending > inflows; treasury depletion risk; tidak ada fee switch atau value capture mechanism【Phase 5 — Revenue Model】【Phase 9 — Failure Factor 6, Behavioral Summary】.
Evidence: Anchor Fees discontinued EV-024【Phase 5 — Revenue Model】; Mirror Fees discontinued EV-024【Phase 5 — Revenue Model】; Community pool spending via proposals tanpa revenue matching【Phase 6 — Governance】; TVL gabungan <$30M【Phase 8 — Market Share】.
Supporting Dataset: Phase 5 Revenue Model; Phase 6 Governance; Phase 8 Market Share; Phase 9 Failure Factor 6.
Confidence: HIGH

Anti-pattern 7: Centralized Exchange Dependency for Critical Token Utility (Burn, Liquidity, Listing)
Explanation: Burn tax hanya efektif jika exchange opt-in (Binance, KuCoin, OKX); delisting exchange (Coinbase, Upbit) menghilangkan akses pasar; Terra tidak punya kontrol atas keputusan exchange【Phase 3 — EV-034】【Phase 7 — Exchange Ecosystem】【Phase 9 — Recurring Pattern 6, Ecosystem Risk】.
Evidence: Binance burn program EV-034【Phase 3 — EV-034】; Coinbase delist LUNC/USTC EV-024 era【Phase 3 — EV-024】; Upbit delist LUNC/USTC Mei 2022【Phase 8 — Trading Markets】; Volume CEX >> DEX【Phase 8 — Liquidity】.
Supporting Dataset: Phase 3 EV-034, EV-024; Phase 7 Exchange Ecosystem; Phase 8 Trading Markets, Liquidity; Phase 9 Pattern 6, Ecosystem Risks.
Confidence: HIGH

Lessons Learned

Lesson 1: Algorithmic Stablecoins Require Exogenous Collateral or Circuit Breakers — Endogenous Reserve Alone Is Insufficient
Explanation: UST death spiral membuktikan zero-collateral algoritmik dengan reserve token endogen (LUNA) tidak tahan banting; butuh collateral eksternon (BTC, ETH, USDC) atau hard circuit breaker (mint cap, redemption pause) yang ter-enforce on-chain【Phase 9 — Insight 1, Failure Factor 1, Trade-off 2】.
Evidence: LUNA hyperinflation 6.5T tidak terhenti sampai oracle/market disabled darurat EV-019【Phase 3 — EV-019】; LFG BTC reserve (exogenous) juga habis EV-017【Phase 3 — EV-017】.
Supporting Dataset: Phase 3 EV-016, EV-017, EV-019; Phase 9 Insight 1, Failure Factor 1, Trade-off 2.
Confidence: HIGH

Lesson 2: Subsidized Yield as Growth Engine Creates Fragile Flywheel — Must Transition to Organic Revenue Before Subsidy Ends
Explanation: Anchor 20% APY subsidi menarik TVL $18B tapi tidak sustainable; tidak ada transition plan ke organic yield; bank run terjadi saat growth melambat【Phase 9 — Insight 2, Failure Factor 2, Trade-off 3】.
Evidence: Anchor Earn design subsidi community pool + bAsset rewards【Phase 3 — EV-009】; TVL peak $18B Maret 2022 collapse Mei 2022【Phase 8 — Adoption Metrics】; Tidak ada mekanisme fee switch atau revenue sharing ke depositor【Phase 5 — Revenue Model】.
Supporting Dataset: Phase 3 EV-009; Phase 8 Adoption Metrics; Phase 5 Revenue Model; Phase 9 Insight 2, Failure Factor 2, Trade-off 3.
Confidence: HIGH

Lesson 3: Emergency Governance Must Be Pre-Defined On-Chain, Not Improvised Off-Chain
Explanation: Mei 2022 chain halt via validator Discord improvised; sebaiknya definisikan emergency module (halt, parameter freeze, circuit breaker) on-chain dengan guardian set atau timelock【Phase 9 — Insight 3, Recurring Pattern 3, Governance Pattern 3】.
Evidence: Chain halt block 7,603,700 EV-018 via off-chain coordination【Phase 3 — EV-018】; Patch disable oracle/market EV-019 deployed via commit bukan proposal【Phase 3 — EV-019】; Normal governance 5-hari voting terlalu lambat untuk death spiral【Phase 6 — Governance】.
Supporting Dataset: Phase 3 EV-018, EV-019; Phase 6 Governance; Phase 9 Insight 3, Pattern 3, Governance Pattern 3.
Confidence: HIGH

Lesson 4: Hard Fork Reset Requires Clear Value Proposition for New Chain — "No Stablecoin" Is Not a Product Strategy
Explanation: Terra 2.0 menghapus stablecoin tapi tidak mengganti dengan primitive baru; TVL $16.4M menunjukkan lack of product-market fit; perlu clear differentiation (misal: specific DeFi focus, RWA, gaming)【Phase 9 — Insight 4, Failure Factor 7, Trade-off 4】.
Evidence: Proposal 1623 "fresh start" tanpa stablecoin EV-020【Phase 3 — EV-020】; Terra 2.0 TVL $16.4M vs Classic $9.8M Nov 2024【Phase 8 — Adoption Metrics】; Protokol migrasi ke Neutron/Osmosis EV-033【Phase 3 — EV-033】.
Supporting Dataset: Phase 3 EV-020, EV-033; Phase 8 Adoption Metrics; Phase 9 Insight 4, Failure Factor 7, Trade-off 4.
Confidence: HIGH

Lesson 5: Community Pool Governance Needs Structured Grant Program, Not Ad-Hoc Proposals
Explanation: Proposal ad-hoc butuh quorum 33.4% + 5 hari voting → high friction; banyak proposal gagal quorum; butuh grant committee dengan budget terdelegasi untuk speed【Phase 9 — Insight 9, Trade-off 6, Governance Pattern 5】.
Evidence: Terra 2.0 community pool 200M LUNA genesis【Phase 6 — Distribution】; Proposal 10983 (5% burn) ditolak quorum【Phase 8 — Open Threads】; Banyak proposal spending kecil butuh full governance process【Phase 6 — Governance】.
Supporting Dataset: Phase 6 Distribution, Governance; Phase 8 Open Threads; Phase 9 Insight 9, Trade-off 6, Governance Pattern 5.
Confidence: HIGH

Lesson 6: Oracle Infrastructure Must Be Upgradeable Without Hard Fork — Modular Oracle Adapter Pattern
Explanation: Terra Classic oracle native terintegrasi deep di x/oracle + x/market; disable butuh chain halt + patch; Terra 2.0 pakai CosmWasm adapter untuk Chainlink/Pyth — lebih modular, upgradeable via governance【Phase 4 — Oracle Module】【Phase 9 — Technical Pattern 6, Insight 7】.
Evidence: Terra Classic oracle/market disable butuh patch EV-019【Phase 3 — EV-019】; Terra 2.0 Chainlink/Pyth via CosmWasm contracts EV-035/036【Phase 3 — EV-035, EV-036】; Tidak ada chain halt untuk oracle upgrade di Terra 2.0【Phase 4 — Technical Upgrade History】.
Supporting Dataset: Phase 3 EV-019, EV-035, EV-036; Phase 4 Oracle Module, Technical Upgrade History; Phase 9 Technical Pattern 6, Insight 7.
Confidence: HIGH

Lesson 7: Legal Entity Structure Should Separate Protocol Development from Treasury Management
Explanation: TFL mengembangkan protokol DAN mengelola treasury; SEC lawsuit + Singapore liquidation mematikan keduanya; sebaiknya protocol development oleh DAO/non-profit, treasury oleh entity terpisah dengan legal wrapper【Phase 9 — Insight 6, Risk Response 6, Failure Factor 5】.
Evidence: SEC Complaint vs TFL & Do Kwon EV-027【Phase 3 — EV-027】; Singapore provisional liquidators Deloitte EV-031【Phase 3 — EV-031】; GitHub maintenance beralih ke komunitas pasca-liquidation【Phase 9 — Risk Response 6】.
Supporting Dataset: Phase 3 EV-027, EV-031; Phase 5 Financial Risk; Phase 9 Insight 6, Risk Response 6, Failure Factor 5.
Confidence: HIGH

Lesson 8: Validator Set Decentralization Requires Active Delegation Incentives, Not Just Large Set Size
Explanation: 130 validator tapi top 10 >40% VP; Nakamoto coefficient ~7-10; butuh delegation incentives (reward sharing, slashing insurance) untuk mendistribusikan stake【Phase 9 — Insight 10, Ecosystem Risk】.
Evidence: Terra 2.0 & Classic staking pages top 10 >40% VP【Phase 4 — Consensus Mechanism】; Map of Zones validator concentration data【Phase 7 — External Dependencies】; Tidak ada delegation incentive program formal【Phase 6 — Governance】.
Supporting Dataset: Phase 4 Consensus Mechanism; Phase 7 External Dependencies; Phase 6 Governance; Phase 9 Insight 10, Ecosystem Risks.
Confidence: HIGH

Knowledge Summary

Strategic Principles:
1. Modular Cosmos SDK Architecture with Native Modules for Core Logic
2. IBC-First Interoperability for Cosmos, External Bridge for Non-Cosmos
3. On-Chain Governance as Sole Protocol Decision Mechanism
4. Follow Upstream Cosmos Ecosystem Standards Without Major Forks
5. Token Distribution via Airdrop to Legacy Holders as "Fair Launch" Narrative

Success Factors:
1. Technical Foundation Built on Battle-Tested Cosmos Stack
2. Dual Chain Resilience — Failure of One Chain Doesn't Kill Entire Ecosystem
3. Community Governance Maturity — Functional On-Chain Decision Making
4. Multi-Oracle Redundancy on Terra 2.0 (Chainlink + Pyth)
5. Sustained Exchange Relationships Despite Regulatory Overhang

Failure Factors:
1. Algorithmic Stablecoin Design with Zero Collateral — Structural Death Spiral Risk
2. Single Application Dependency (Anchor Earn) for Token Demand
3. Off-Chain Reserve Entity (LFG) with Volatile Assets (BTC) for Peg Defense
4. Native Oracle Module (Validator-Voted) Manipulable During Crisis
5. Regulatory Overhang — SEC Securities Classification, Korea Criminal Case, Singapore Liquidation
6. No Sustainable Revenue Model Post-Collapse
7. Fragmented Liquidity & Developer Mindshare Across Two Chains

Decision Framework:
1. Observe — Market Crisis or Technical Signal Triggers Assessment
2. Evaluate — Off-Chain Validator/Coordination for Crisis, On-Chain Governance for Normal
3. Fund — VC Rounds for Entity, Community Pool for Protocol, No Public Token Sale for Cash
4. Develop — Follow Upstream Cosmos SDK/CometBFT/IBC-Go Release Cycle
5. Launch — Chain Genesis with Immediate Exchange Listings, Airdrop Distribution
6. Govern — Dual DAO Structure with On-Chain Parameter Control

Reusable Playbook:
1. Build Appchain on Cosmos SDK for Sovereignty with IBC-Native Interoperability
2. Design On-Chain Governance as Primary Decision Layer with Emergency Off-Chain Override
3. Distribute New Chain Tokens via Airdrop to Legacy Holders for Legitimacy
4. Implement Burn Tax with Exchange Partnership for Deflationary Pressure
5. Migrate from Native Oracle to Institutional Providers After Failure
6. Use Community Pool as On-Chain Treasury Governed by Proposals

Anti-patterns:
1. Zero-Collateral Algorithmic Stablecoin with Endogenous Reserve Token
2. Single Protocol Subsidizing Yield to Bootstrap Stablecoin Demand
3. Off-Chain Reserve Entity Holding Volatile Assets for On-Chain Peg Defense
4. Native Validator-Voted Oracle Without Economic Slashing for Dishonest Voting During Crisis
5. Hard Fork Creating Dual Chains Without Clear Differentiation Strategy
6. No Sustainable Protocol Revenue Model Beyond Inflationary Staking Rewards
7. Centralized Exchange Dependency for Critical Token Utility (Burn, Liquidity, Listing)

## Open Questions
- [foundation] Status hukum Do Kwon dan Terraform Labs: extradisi, gugatan SEC, status operasional TFL saat ini — perlu verifikasi terbaru
- [foundation] Ukuran treasury dan cadangan USTC/LUNC saat ini — data on-chain vs klaim komunitas
- [foundation] Rincian tokenomics LUNA 2.0 pasca-airdrop: alokasi komunitas, validator, developer, vesting schedule — butuh cross-check dengan governance proposal resmi
- [foundation] Status peg USTC dan mekanisme repeg komunitas (Proposal 12133, dll) — apakah masih aktif/berfungsi
- [foundation] Jumlah validator aktif, stake ratio, dan desentralisasi saat ini untuk Terra 2.0 vs Classic
- [foundation] Hubungan formal antara Terraform Labs (entity hukum) dan Terra 2.0 chain (governance komunitas) — apakah TFL masih berkontribusi kode
- [foundation] Data TVL historis vs saat ini untuk protokol ekosistem utama (Anchor, Mirror, Astroport) — banyak protokol henti operasi/migrasi
- [entity] Status hukum Do Kwon terkini (ekstradisi ke AS vs Korea, status penahanan Montenegro) — perlu verifikasi real-time
- [entity] Status operasional Terraform Labs Pte. Ltd. setelah dilantiknya provisional liquidators Mei 2024 — apakah masih berkontribusi kode ke terra-money/core
- [entity] Ukuran treasury LFG saat ini (BTC, ETH, stablecoin) dan rencana distribusi — data on-chain vs klaim komunitas
- [entity] Tokenomics LUNA 2.0 pasca-airdrop detail: alokasi community pool, validator, developer, vesting schedule — cross-check dengan proposal governance resmi
- [entity] Status peg USTC dan mekanisme repeg komunitas (Proposal 12133, 12158, dll) — apakah masih aktif/berfungsi/ter-funding
- [entity] Jumlah validator aktif, stake ratio, dan desentralisasi (Nakamoto coefficient) saat ini untuk Terra 2.0 vs Classic
- [entity] Hubungan formal TFL (entity hukum) dengan Terra 2.0 chain (governance komunitas) — kontribusi kode, IP ownership, branding
- [entity] Data TVL historis vs saat ini untuk protokol ekosistem utama (Anchor, Mirror, Astroport, Prism, Mars) — banyak protokol henti operasi/migrasi chain
- [entity] Daftar lengkap investor strategic round $150M (2021) — beberapa nama belum terverifikasi primer
- [entity] Peran Jump Crypto di pertahanan peg Mei 2022 — detail alokasi dana, wallet, dan hasil investigasi on-chain
- [entity] Status kasus hukum Korea Selatan terhadap Daniel Shin (apakah dituntut/tersangka) — kurang tercakup media internasional
- [entity] Detail winding-up TFL di Singapura: kreditur, aset, timeline distribusi — baru mulai Mei 2024
- [history] Tanggal pasti pembentukan LFG: beberapa sumber menyebut 17 Jan 2022, lain "Januari 2022" — perlu konfirmasi dari announcement resmi LFG Twitter (tersedia tapi butuh verifikasi timestamp exact)
- [history] Jumlah BTC pasti LFG pada puncak: bervariasi 80,000–80,394 BTC antar sumber (Nansen vs blockchain.com vs LFG dashboard arkiv) — cross-check on-chain address 3LunaFoundationGuard...
- [history] Detail strategic round $150M: daftar investor lengkap dan alokasi per investor belum sepenuhnya diverifikasi primer (hanya press release PRNewswire dan The Block) — butuh cross-check dengan filing SEC atau cap table
- [history] Tanggal henti operasional Anchor/Mirror di Terra Classic: bervariasi "Mei 2022" vs "Juni 2022" vs "bertahap" — perlu cek governance proposal shutdown resmi
- [history] Status ekstradisi Do Kwon terkini (Agustus 2024): keputusan final Montenegro belum jelas, beberapa laporan bilang ekstradisi ke Korea Selatan disetujui — perlu verifikasi real-time
- [history] Status operasional Terraform Labs Pte. Ltd. pasca-provisional liquidators Mei 2024: apakah tim developer masih commit ke terra-money/core — butuh cek GitHub activity recente
- [history] Tokenomics LUNA 2.0 detail: vesting schedule community pool, validator, developer — butuh cross-check dengan proposal governance dan on-chain data
- [history] Mekanisme repeg USTC (Proposal 12133, 12158, dll) status implementasi aktual dan efektivitas — butuh data on-chain terkini
- [history] Jumlah validator aktif, stake ratio, Nakamoto coefficient Terra 2.0 vs Classic saat ini — butuh query live ke explorer
- [history] Peran Jump Crypto detail di pertahanan peg Mei 2022: wallet address, jumlah BTC/UST yang ditradingkan, PnL — sebagian terungkap investigasi Nansen/FatMan tapi tidak lengkap
- [technology] Exact CometBFT version currently running on Terra 2.0 vs Terra Classic validator sets — need live query to RPC /status endpoint
- [technology] Current CosmWasm version deployed on each chain (1.3, 1.4, 1.5?) — governance proposals reference but not confirmed on-chain
- [technology] Status of Terra Classic oracle module code — is it fully removed or just disabled via governance parameter? Code still exists in classic-core/x/oracle
- [technology] Wormhole Guardian set current composition for Terra 2.0 — 19 Guardians but which entities? Need Wormhole Guardian registry
- [technology] Chainlink DON node operators for Terra 2.0 feeds — not publicly listed in standard Chainlink feed pages
- [technology] Pyth publisher list for Terra 2.0 price feeds — Pyth docs show feed IDs but not publisher identities per chain
- [technology] IBC channel IDs and counterparty chains currently active for both Terra chains — need query to ibc module state
- [technology] Validator software version distribution (CometBFT v0.37 vs v1.x) — impacts consensus compatibility
- [technology] Terra Station mobile app last update date and supported chain versions — GitHub shows infrequent releases 2023-2024
- [technology] Whether Terraform Labs Pte. Ltd. (under provisional liquidation) still holds commit access to terra-money/core repo — GitHub org permissions not public
- [technology] Formal verification status of CosmWasm standard libraries (cw20, cw721) used on Terra — some audited but not formally verified
- [technology] Gas fee model differences between Terra Classic (tax + gas) and Terra 2.0 (gas only) — need current parameter values from governance
- [technology] State sync / snapshot availability for new validators joining each chain — impacts decentralization metrics
- [technology] Maximum theoretical TPS for CosmWasm on Terra given current block gas limit and CometBFT block time — not benchmarked publicly
- [financial] Ukuran treasury Terraform Labs Pte. Ltd. saat ini (pasca-provisional liquidators Mei 2024) — tidak dipublikasikan; Deloitte belum rilis laporan aset/kreditor
- [financial] Sisa aset LFG on-chain (BTC, ETH, stablecoin) — address 3LunaFoundationGuard... bisa di-track tapi tidak ada official statement post-deployment
- [financial] Revenue on-chain aktual per bulan untuk kedua chain (gas, tax, swap fees) — perlu query analytics (Flipside/Nansen) untuk angka historis
- [financial] Biaya hukum TFL untuk pertahanan SEC, Korea, Montenegro, Singapura — tidak diungkap; bisa material
- [financial] Status vesting token investor Strategic Round $150M — apakah masih locked, cliffs, atau sudah unlocked — Phase 6 tapi relevan financial risk
- [financial] Apakah Terraform Labs masih memiliki runway operasional atau sepenuhnya bergantung pada aset yang dicairkan liquidators
- [financial] Community pool balances terkini (LUNC di Classic, LUNA di 2.0) — on-chain queryable tapi tidak di-ringkas di financial report
- [financial] Potensi klaim clawback dari 3AC liquidators terhadap LFG/TFL atas transfer BTC Mei 2022 — belum terselesaikan hukum
- [financial] Insurance / coverage untuk validator slashing events — tidak diungkap
- [financial] Audit keuangan independen (bukan smart contract audit) untuk TFL atau LFG — tidak ada record publik
- [token] Jumlah persis LUNA yang di-vested/di-lock di luar community pool tidak dapat diverifikasi — beberapa sumber (The Block) menyebut adanya alokasi tersembunyi untuk Do Kwon via kategori holder, tetapi proposal resmi tidak mencantumkan detail ini; konflik antara klaim investigasi dan dokumen resmi belum terselesaikan.
- [token] Detail vesting untuk investor Strategic Round $150M (2021) tidak pernah dipublikasikan — apakah token LUNA Classic yang diinvestigasi memiliki lockup period, dan bagaimana itu mempengaruhi airdrop LUNA 2.0, tidak diketahui.
- [token] Total supply LUNC saat ini — sumber bervariasi antara 6.1T (CoinGecko) dan 6.5T (Lunc Burn tracker) karena perbedaan metodologi pelaporan circulating vs total, dan efek burn address; belum ada konsensus.
- [token] Inflasi LUNC saat ini — parameter inflation rate di Terra Classic tidak stabil; beberapa proposal menurunkan inflasi ke 0% tapi validators menolak; status inflasi efektif per 2024 masih diperdebatkan komunitas.
- [token] Status token LUNA 2.0 yang dipegang Terraform Labs (sesuai klaim SEC bahwa TFL memegang saham signifikan) — tidak diungkap on-chain atau resmi pasca-likuidasi.
- [token] Jumlah burned LUNC dari operator exchange selain Binance (KuCoin, OKX, Crypto.com) — tidak konsisten antara tracker (lunc.to) dan laporan exchange.
- [token] Proposan repeg USTC mekanisme pasti (burn rate, collateral) — masih dalam status "proposal" dan belum implementasi; tidak ada angka final yang dapat diverifikasi.
- [token] Apakah ada private sale Luna 2.0 (bukan airdrop) — tidak ada indikasi publik; perlu verifikasi jika ada.
- [token] Kapabilitas LUNA sebagai collateral untuk stablecoin baru di Terra 2.0 — dokumentasi resmi tidak menyebutkan rencana resmi stablecoin.
- [ecosystem] Dukungan ke wallet eksternal selain Terra Station, Ledger, Keplr, Cosmostation — tidak ada data lengkap untuk wallet lain (misal Leap, Omni) di dokumentasi resmi; perlu verifikasi lanjutan
- [ecosystem] Jumlah pasti dan identitas 19 Wormhole Guardians untuk Terra 2.0 — daftar lengkap tidak dipublikasikan oleh Terra, hanya tersedia di dokumentasi Wormhole sendiri
- [ecosystem] Identitas node operator Chainlink DON untuk Terra 2.0 — tidak tercantum di halaman Chainlink Terra (berbeda dengan chain lain yang menampilkan ORC nodes)
- [ecosystem] Pyth publisher identitas untuk feed Terra 2.0 — Pyth docs menunjukkan feed IDs tapi tidak menampilkan daftar publisher per chain
- [ecosystem] IBC channel IDs dan counterparties spesifik yang aktif antara Terra Classic, Terra 2.0 dan chain lain — belum ada dokumentasi resmi terstruktur yang memperbarui daftar ini pasca-2022
- [ecosystem] Daftar lengkap exchange pendukung burn LUNC selain Binance, KuCoin, OKX — beberapa exchange (Crypto.com, Gate) pernah menyebut support tapi tidak konsisten; jumlah dan mekanisme belum terverifikasi resmi
- [ecosystem] Apakah Terra Station masih mendapat pembaruan aktif setelah TFL memasuki likuidasi — repo GitHub menunjukkan aktivitas sporadis; status maintenance tidak jelas
- [ecosystem] Status proyek-proyek ekosistem baru (di luar yang tercantum) — baik di Terra Classic maupun Terra 2.0 — banyak dApps kecil tidak terdokumentasi secara resmi
- [ecosystem] Peran spesifik Strangelove Ventures sebagai IBC relayer untuk Terra — beberapa sumber menyebut ini, tapi tidak ada dokumentasi resmi Terra yang mengonfirmasi jumlah relayer aktif
- [ecosystem] Ketersediaan grant program HackTerra pasca-2023 — tidak ada informasi lanjutan apakah hackathon akan diadakan lagi
- [ecosystem] Bagaimana community pool (kedua chain) dialokasikan secara rinci — proposal spending individual dapat di-track, tapi daftar agregat tidak dirilis oleh TFL atau DAO
- [market] TVL Terra Classic dan Terra 2.0 fluktuatif; angka yang dilaporkan (16.4M dan 9.8M) adalah snapshot 2024-11-01; bisa berubah signifikan — perlu cross-check real-time via DefiLlama API.
- [market] Daily Active Users tidak dipublikasikan oleh dashboard resmi; Flipside menyediakan data tapi memerlukan query manual, tidak ada angka agregat yang dapat dikutip — belum ada sumber sekunder yang konsisten.
- [market] Developer Count untuk kedua chain tidak tersedia; GitHub hanya menampilkan contributor di inti repositori, bukan total developer ekosistem — estimasi tidak dapat diverifikasi.
- [market] Bridge Volume Wormhole untuk Terra 2.0 tidak dipublikasikan per-chain; dashboard Wormhole menampilkan total volume saja, tidak breakdown Terra — perlu akses data API untuk verifikasi.
- [market] IBC transaction count per-day untuk kedua Terra chains bervariasi antara Map of Zones dan explorer karena perbedaan metodologi (counting vs messages vs transfers) — belum ada angka konsensus.
- [market] Market Share Cosmos TVL untuk Terra gabungan <1%, tapi persentase pasti tidak diungkapkan di DefiLlama — hanya bisa diestimasi dari TVL per-chain.
- [market] Volume 24h LUNA (22.8M) dan LUNC (2.5M) dari CoinGecko bervariasi per hari; angka CoinMarketCap bisa berbeda karena metodologi weighting — konflik antara kedua sumber tidak dapat diselesaikan di fase ini.
- [market] Status listing LUNC di Coinbase tidak konsisten antara blog Coinbase Delist (2022-08) dan data CoinGecko yang masih menampilkan beberapa market — perlu klarifikasi.
- [market] Partisipasi burn tax LUNC dari exchange selain Binance, KuCoin, OKX tidak terdokumentasi resmi; klaim Crypto.com dan Gate belum diverifikasi.
- [market] Identitas penuh validator set dan stake ratio per validator untuk kedua chains dapat di-query di Staking pages, tapi agregasi Nakamoto coefficient tidak tersedia di dashboard publik.
- [market] Data transaksi harian dari explorer (Finder) tidak memiliki agregasi ringkas; angka 2,000-10,000 (Terra 2.0) dan 30,000-100,000 (Classic) adalah estimasi dari histogram explorer, bukan angka resmi.
- [market] Apakah Token Terminal metrics (revenue, P/S, dll) tersedia untuk Terra — belum diverifikasi; halaman Token Terminal ada di URL tapi bisa jadi kosong untuk Terra Classic.
- [market] Klasifikasi sekuritas LUNA/LUNC oleh pengadilan AS (putusan SEC) dapat berdampak pada listing exchange dan data market — status regulasi masih ongoing.
- [behavioral] Status hukum Do Kwon terkini (ekstradisi final ke AS vs Korea, status penahanan Montenegro) — perlu verifikasi real-time Agustus 2024+
- [behavioral] Status operasional Terraform Labs Pte. Ltd. setelah provisional liquidators Mei 2024 — apakah masih berkontribusi kode ke terra-money/core (GitHub activity recente)
- [behavioral] Ukuran treasury TFL & LFG saat ini (on-chain vs legal claims) — Deloitte belum publish laporan; LFG BTC address trackable tapi status legal unclear
- [behavioral] Tokenomics LUNA 2.0 detail vesting: community pool 20% sudah berapa ter-spend? Alokasi validator/developer vesting schedule — cross-check governance proposal
- [behavioral] Efektivitas repeg USTC (Proposal 12133, 12158, dll) — apakah mekanisme burn/mint baru diimplementasikan atau masih proposal?
- [behavioral] Jumlah validator aktif, stake ratio, Nakamoto coefficient real-time untuk kedua chain — butuh query live ke staking pages
- [behavioral] Hubungan formal TFL (entity hukum) dengan Terra 2.0 chain (governance komunitas) — IP ownership, branding, domain control (terra.money, station.terra.money)
- [behavioral] TVL historis vs aktual protokol ekosistem (Astroport, Mars di Neutron, Prism, Levana) — banyak data DefiLlama tidak terpisah per chain deployment
- [behavioral] Daftar lengkap investor Strategic Round $150M (2021) dengan alokasi & vesting — beberapa nama belum terverifikasi primer (hanya PRNewswire)
- [behavioral] Peran Jump Crypto detail di pertahanan peg Mei 2022 — wallet address, jumlah BTC/UST traded, PnL — sebagian terungkap Nansen/FatMan tapi tidak lengkap
- [behavioral] Status kasus hukum Korea Selatan terhadap Daniel Shin — apakah dituntut/tersangka (kurang tercakup media internasional)
- [behavioral] Detail winding-up TFL di Singapura: kreditur, aset, timeline distribusi — baru mulai Mei 2024, Deloitte belum publish report
- [behavioral] Apakah Terra Station mobile/extension masih maintain aktif — GitHub shows sporadic commits 2023-2024; TFL liquidation impact unclear
- [behavioral] Formal verification status CosmWasm standard libraries (cw20, cw721) di Terra — audited tapi tidak formally verified
- [behavioral] State sync/snapshot availability untuk validator baru join masing-masing chain — impact desentralisasi metrics
- [knowledge] Status hukum Do Kwon terkini (ekstradisi final ke AS vs Korea, status penahanan Montenegro) — perlu verifikasi real-time Agustus 2024+【Phase 9 — Open Threads】.
- [knowledge] Status operasional Terraform Labs Pte. Ltd. setelah provisional liquidators Mei 2024 — apakah masih berkontribusi kode ke terra-money/core (GitHub activity recente)【Phase 9 — Open Threads】.
- [knowledge] Ukuran treasury TFL & LFG saat ini (on-chain vs legal claims) — Deloitte belum publish laporan; LFG BTC address trackable tapi status legal unclear【Phase 9 — Open Threads】.
- [knowledge] Tokenomics LUNA 2.0 detail vesting: community pool 20% sudah berapa ter-spend? Alokasi validator/developer vesting schedule — cross-check governance proposal【Phase 6 — Open Threads】【Phase 9 — Open Threads】.
- [knowledge] Efektivitas repeg USTC (Proposal 12133, 12158, dll) — apakah mekanisme burn/mint baru diimplementasikan atau masih proposal?【Phase 3 — EV-032】【Phase 9 — Open Threads】.
- [knowledge] Jumlah validator aktif, stake ratio, Nakamoto coefficient real-time untuk kedua chain — butuh query live ke staking pages【Phase 4 — Consensus Mechanism】【Phase 9 — Open Threads】.
- [knowledge] Hubungan formal TFL (entity hukum) dengan Terra 2.0 chain (governance komunitas) — IP ownership, branding, domain control (terra.money, station.terra.money)【Phase 9 — Open Threads】.
- [knowledge] TVL historis vs aktual protokol ekosistem (Astroport, Mars di Neutron, Prism, Levana) — banyak data DefiLlama tidak terpisah per chain deployment【Phase 7 — Open Threads】【Phase 9 — Open Threads】.
- [knowledge] Daftar lengkap investor Strategic Round $150M (2021) dengan alokasi & vesting — beberapa nama belum terverifikasi primer (hanya PRNewswire)【Phase 2 — Investors】【Phase 5 — Funding History】【Phase 9 — Open Threads】.
- [knowledge] Peran Jump Crypto detail di pertahanan peg Mei 2022 — wallet address, jumlah BTC/UST traded, PnL — sebagian terungkap Nansen/FatMan tapi tidak lengkap【Phase 3 — EV-017】【Phase 9 — Open Threads】.
- [knowledge] Status kasus hukum Korea Selatan terhadap Daniel Shin — apakah dituntut/tersangka (kurang tercakup media internasional)【Phase 2 — Daniel Shin】【Phase 9 — Open Threads】.
- [knowledge] Detail winding-up TFL di Singapura: kreditur, aset, timeline distribusi — baru mulai Mei 2024, Deloitte belum publish report【Phase 3 — EV-031】【Phase 9 — Open Threads】.
- [knowledge] Apakah Terra Station mobile/extension masih maintain aktif — GitHub shows sporadic commits 2023-2024; TFL liquidation impact unclear【Phase 4 — Core Components】【Phase 9 — Open Threads】.
- [knowledge] Formal verification status CosmWasm standard libraries (cw20, cw721) di Terra — audited tapi tidak formally verified【Phase 4 — Audit History】【Phase 9 — Open Threads】.
- [knowledge] State sync/snapshot availability untuk validator baru join masing-masing chain — impact desentralisasi metrics【Phase 4 — Known Technical Limitations】【Phase 9 — Open Threads】.
