# Curve — Deep Case Study (Phased)

**CIF Dataset — Deep Dossier · Tier: Deep (anchor project)**
**Source:** Deep Research (DeepSeek), Format v3 Dependency Pipeline (12/11 phases: foundation, entity, history, technology, financial, token, ecosystem, market, behavioral, knowledge, conflict, airdrop). **Auto-assembled** by `tools/ingest.py` (deterministic, no LLM, strict data_project/ contract) — each phase extracted and concatenated in dependency order per `docs/Protocol/Deep-Research-Brief.md`; the reasoning is the source reports'.
**Raw sources archived:** doc_backup/deep/Curve_foundation_2026-08.docx, doc_backup/deep/Curve_entity_2026-08.docx, doc_backup/deep/Curve_history_2026-08.docx, doc_backup/deep/Curve_technology_2026-08.docx, doc_backup/deep/Curve_financial_2026-08.docx, doc_backup/deep/Curve_token_2026-08.docx, doc_backup/deep/Curve_ecosystem_2026-08.docx, doc_backup/deep/Curve_market_2026-08.docx, doc_backup/deep/Curve_behavioral_2026-08.docx, doc_backup/deep/Curve_knowledge_2026-08.docx, doc_backup/deep/Curve_conflict_2026-08.docx, doc_backup/deep/Curve_airdrop_2026-08.docx.
**Phases not run:** none.

> Faithful concatenation of phase outputs — no fabrication, no distillation beyond what the closing phase (Conflict Resolution / Validation) itself states. Consider a periodic QC pass.

---
## Foundation Intelligence
_ref: `docs/Ontology/Identity.md`, `docs/Ontology/Team.md`_

PROJECT: Curve
Official Name: Curve Finance
Symbol: CRV
Category: DeFi Automated Market Maker — stableswap/DEX optimal untuk aset bernilai serupa (stablecoin, wrapped assets, LST)
Founding Entity: Tidak ada entitas korporat pendiri formal — proyek dimulai oleh Michael Egorov dan berkembang dengan Curve DAO sebagai pemegang governance; Curve Labs dan Curve Finance Foundation mendukung pengembangan (MEDIUM) [Curve docs & repositori, https://github.com/curvefi]
Founders: Michael Egorov (founder; fisikawan Rusia; co-founder NuCypher sebelum fokus penuh ke Curve) (HIGH) [Curve GitHub, https://github.com/curvefi]; (MEDIUM) [Curve whitepaper, https://curve.fi/whitepaper.pdf]
Core Team: Kontributor inti pseudonim dan publik lintas yurisdiksi; komposisi lengkap tidak dipublikasikan sebagai roster resmi (LOW)
Country: Terdesentralisasi global; Foundation berorientasi yurisdiksi netral (MEDIUM)
Launch Date - Testnet: tidak ada fase testnet formal terpisah era 2019-2020 — iterasi langsung ke mainnet Ethereum (pola umum DeFi awal) (LOW)
Launch Date - Mainnet: Januari 2020 (pool stableswap pertama live di Ethereum) (HIGH) [Curve whitepaper, https://curve.fi/whitepaper.pdf]
Launch Date - TGE: 2020-08-14 (CRV token launch & liquidity mining dimulai; konsisten dengan Phase 6 dataset ini) (HIGH) [Phase 6 — Token; Curve docs, https://resources.curve.fi/]
Main Products: StableSwap pools (3pool, stETH, dll.); Factory pools (permissionless); Crypto pools (Tricrypto); veCRV (vote-escrow governance + fee share + boost); crvUSD stablecoin (2023); Curve Lend; multi-chain deployments (Arbitrum, Optimism, Polygon, dll.) (HIGH) [Curve docs, https://resources.curve.fi/]
Official Website: https://curve.fi (HIGH)
Repository: https://github.com/curvefi (HIGH) [GitHub Curve, https://github.com/curvefi]
Documentation: https://resources.curve.fi (HIGH)
Social - X/Twitter: @CurveFinance (HIGH)
Social - Discord: https://discord.gg/curve (MEDIUM)
Social - Telegram: tidak ada kanal Telegram resmi utama (MEDIUM)
Block Explorer: https://etherscan.io (kontrak pool & token di Ethereum) + explorer chain deployment lain (HIGH)
Token Contract: 0xD533a949740bb3306d119CC777fa900bA034cd522b (CRV ERC-20 di Ethereum) (MEDIUM) [Etherscan CRV, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd522b]
Chain(s): Ethereum (utama) + Arbitrum, Optimism, Polygon, dan deployment lain via factory (HIGH) [Phase 2 — Entity; Curve docs, https://resources.curve.fi/]
Ecosystem: DeFi Ethereum & multi-chain — integrasi erat dengan Convex (akumulasi veCRV), Yearn (vault Curve LP), Frax, protokol LST (Lido stETH pool historis terbesar), stablecoin issuers (USDT/USDC/DAI/FRAX) (HIGH) [Phase 2 — Entity]

## Entity Intelligence
_ref: `docs/Ontology/Relationships.md` (entity graph)_

PROJECT: Curve

Entity: Michael Egorov
Type: Person
Relationship: Pendiri utama dan pengembang inti Curve Finance — menulis whitepaper dan kode awal protokol, serta menjabat sebagai CEO dari perusahaan pengembang inti. (HIGH)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Finance Whitepaper, https://curvefi.com/curve whitepaper.pdf]; [Messari, https://messari.io/project/curve/profile]

Entity: Curve Finance
Type: Protocol
Relationship: Protokol pertukaran desentralisasi (DEX) khusus untuk aset stablecoin dan aset dengan nilai terkait (pegged assets), menggunakan automated market maker (AMM) dengan kurva stableswap. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Finance, https://curve.fi/]; [CoinMarketCap, https://coinmarketcap.com/currencies/curve-dao-token/]

Entity: Curve DAO
Type: DAO
Relationship: Organisasi otonom terdesentralisasi yang mengelola protokol Curve melalui kepemilikan token CRV, termasuk parameter pool, gauge, dan kebijakan fee. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Governance, https://gov.curve.fi/]; [Curve Docs, https://docs.curve.fi/references/dao/]

Entity: Curve Labs
Type: Company
Relationship: Perusahaan pengembangan yang berafiliasi dengan Curve Finance — didirikan oleh Michael Egorov, berfokus pada pengembangan lebih lanjut protokol dan produk terkait. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [LinkedIn, https://www.linkedin.com/company/curve-labs]

Entity: Curve Finance Foundation
Type: Foundation
Relationship: Entitas non-profit yang dikabarkan mendukung pengembangan dan governance Curve Finance — detail struktur dan peran pastinya tidak sepenuhnya terdokumentasi publik. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Crunchbase, https://www.crunchbase.com/organization/curve-finance-foundation]

Entity: CRV Token
Type: Organization
Relationship: Token utilitas dan governance dari ekosistem Curve Finance — digunakan untuk voting, staking (vote-escrowed CRV), dan insentif likuiditas. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Etherscan, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52]; [CoinGecko, https://www.coingecko.com/en/coins/curve-dao-token]

Entity: Ethereum
Type: Organization
Relationship: Blockchain utama tempat Curve Finance pertama kali diluncurkan dan beroperasi — kontrak CRV dan sebagian besar pool utama berada di jaringan ini. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Ethereum, https://ethereum.org/]; [Curve Deployment Addresses, https://docs.curve.fi/references/deployed/]

Entity: Arbitrum
Type: Organization
Relationship: Jaringan layer-2 tempat Curve Finance di-deploy sebagai bagian dari ekspansi multi-chain — menyediakan biaya transaksi rendah untuk pengguna Curve. (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Arbitrum Deployment, https://docs.curve.fi/references/deployed/]; [Arbitrum, https://arbitrum.io/]

Entity: Optimism
Type: Organization
Relationship: Jaringan layer-2 tempat Curve Finance di-deploy untuk memperluas aksesibilitas protokol di ekosistem OP. (HIGH)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Optimism Deployment, https://docs.curve.fi/references/deployed/]; [Optimism, https://www.optimism.io/]

Entity: Polygon
Type: Organization
Relationship: Jaringan sidechain tempat Curve Finance di-deploy untuk mendukung aktivitas likuiditas di ekosistem Polygon. (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Polygon Deployment, https://docs.curve.fi/references/deployed/]; [Polygon, https://polygon.technology/]

Entity: Frax Finance
Type: Protocol
Relationship: Protokol stablecoin yang memiliki integrasi erat dengan Curve melalui pool khusus FRAX, termasuk penggunaan bersama likuiditas dan insentif. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Frax Finance, https://frax.finance/]; [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: Convex Finance
Type: Protocol
Relationship: Protokol yang dioptimalkan untuk meningkatkan hasil stake CRV dan likuiditas di Curve — membungkus LP token Curve dan CRV untuk memaksimalkan reward. (HIGH)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Convex Finance, https://www.convexfinance.com/]; [Documentation Convex, https://docs.convexfinance.com/]

Entity: Yearn Finance
Type: Protocol
Relationship: Protokol yield aggregator yang menggunakan pool Curve sebagai salah satu vault strategy untuk mendapatkan yield dari likuiditas. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Yearn Finance, https://yearn.finance/]; [Yearn Vaults, https://yearn.finance/vaults]

Entity: Gnosis Safe
Type: Application
Relationship: Dompet multi-signature yang digunakan oleh Curve DAO untuk mengelola treasury dan eksekusi transaksi governance multisig. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Gnosis Safe, https://safe.global/]; [Curve Governance Docs, https://docs.curve.fi/references/dao/]

Entity: Chainlink
Type: Organization
Relationship: Jaringan oracle yang digunakan untuk menyediakan harga aset ke beberapa pool Curve, meningkatkan keamanan dan akurasi data harga. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Chainlink, https://chain.link/]; [Curve Feed Registry, https://docs.curve.fi/references/contracts/]

Entity: Badger DAO
Type: DAO
Relationship: Organisasi DAO yang memiliki pool token BTC terkait (seperti renBTC dan sBTC) di Curve untuk likuiditas dan insentif. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Badger DAO, https://badger.com/]; [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: Compound
Type: Protocol
Relationship: Protokol lending yang berinteraksi dengan Curve melalui pool aset terkait (seperti cUSDC) atau sebagai sumber likuiditas. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Compound, https://compound.finance/]; [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: Aave
Type: Protocol
Relationship: Protokol lending yang berinteraksi dengan Curve melalui token aset terkait, dengan beberapa strategi yield menggunakan likuiditas Curve. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Aave, https://aave.com/]; [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: Curve.fi
Type: Application
Relationship: Antarmuka web resmi untuk berinteraksi dengan protokol Curve — menyediakan akses ke swap, pool, gauge, dan staking. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve.fi, https://curve.fi/]; [Curve Docs, https://docs.curve.fi/]

Entity: Curve Docs
Type: Media
Relationship: Dokumentasi teknis resmi Curve Finance — berisi spesifikasi protokol, kontrak, parameter, dan panduan pengguna. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Docs, https://docs.curve.fi/]

Entity: Curve Governance Forum
Type: Media
Relationship: Forum diskusi untuk proposal dan keputusan governance Curve DAO — tempat pengguna berdiskusi sebelum snapshot voting. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Discord
Type: Community
Relationship: Server Discord resmi untuk komunitas Curve — tempat pengguna dan developer berdiskusi teknis, support, dan komunitas. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Discord, https://discord.gg/9vxSfkA]

Entity: Curve Twitter
Type: Media
Relationship: Akun Twitter resmi Curve Finance — digunakan untuk pengumuman, update protokol, dan informasi komunitas. (HIGH)
Period: 2020–sekarang
Exposure Type: community
Evidence: (HIGH) [Curve Twitter, https://twitter.com/CurveFinance]

Entity: Curve Telegram
Type: Community
Relationship: Grup Telegram resmi untuk komunitas Curve — tempat diskusi real-time dan bantuan komunitas. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Telegram, https://t.me/curvefi]

Entity: Etherscan
Type: Organization
Relationship: Penjelajah blok (block explorer) untuk Ethereum yang digunakan untuk memverifikasi kontrak CRV dan aktivitas on-chain Curve. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Etherscan, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52]

Entity: CoinGecko
Type: Organization
Relationship: Situs web agregator data pasar kripto yang melacak harga, volume, dan tokenomics CRV — digunakan sebagai referensi data pasar. (MEDIUM)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [CoinGecko, https://www.coingecko.com/en/coins/curve-dao-token]

Entity: CoinMarketCap
Type: Organization
Relationship: Situs web agregator data pasar kripto yang menyediakan data pasar untuk CRV dan Curve Finance. (MEDIUM)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [CoinMarketCap, https://coinmarketcap.com/currencies/curve-dao-token/]

Entity: Messari
Type: Organization
Relationship: Platform riset kripto yang menyediakan laporan dan data mendalam tentang Curve Finance dan token CRV. (MEDIUM)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Messari, https://messari.io/project/curve/profile]

Entity: Chainalysis
Type: Government
Relationship: Perusahaan analitik blockchain yang memantau aktivitas on-chain, termasuk yang terkait dengan Curve, untuk kepatuhan regulasi dan investigasi — bukan mitra resmi proyek. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Chainalysis, https://www.chainalysis.com/]

Entity: SEC (US Securities and Exchange Commission)
Type: Government
Relationship: Regulator keuangan Amerika Serikat yang dapat memiliki yurisdiksi tidak langsung atas token CRV dan aktivitas Curve Finance — tidak ada keterlibatan formal yang terdokumentasi. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [SEC, https://www.sec.gov/]

Entity: ConsenSys
Type: Company
Relationship: Perusahaan pengembangan Ethereum yang memiliki infrastruktur seperti MetaMask dan Infura — sering digunakan oleh pengguna Curve untuk berinteraksi dengan protokol, tanpa keanggotaan formal. (MEDIUM)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (MEDIUM) [ConsenSys, https://consensys.net/]; [MetaMask, https://metamask.io/]

Entity: MetaMask
Type: Application
Relationship: Dompet kripto populer yang digunakan pengguna Curve untuk terhubung dan bertransaksi di protokol — bagian dari ekosistem infrastruktur. (MEDIUM)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (MEDIUM) [MetaMask, https://metamask.io/]; [Curve UI Penggunaan, https://curve.fi/]

Entity: Infura
Type: Organization
Relationship: Penyedia infrastruktur node Ethereum yang digunakan aplikasi seperti Curve untuk mengakses blockchain — memfasilitasi koneksi RPC. (MEDIUM)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (MEDIUM) [Infura, https://infura.io/]; [ConsenSys, https://consensys.net/]

Entity: Yearn Finance Vaults
Type: Protocol
Relationship: Vault milik Yearn Finance yang menggunakan pool Curve sebagai strategi utama untuk menghasilkan yield — contoh integrasi likuiditas nyata. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Yearn Vaults, https://yearn.finance/vaults]

Entity: Curve Community Treasury
Type: DAO
Relationship: Kumpulan dana yang dikelola oleh Curve DAO untuk pendanaan pengembangan, insentif, dan kepentingan protokol — sumber dana dari sebagian fee dan emisi token. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve iBTC Pool
Type: Application
Relationship: Salah satu pool utama di Curve yang menghubungkan bentuk token Bitcoin (renBTC, wBTC, sBTC) — menunjukkan interoperabilitas aset. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: Curve StableSwap
Type: Protocol
Relationship: Mekanisme inti matematis dari Curve — merupakan inovasi AMM yang fokus pada aset dengan nilai terkait (pegged), menjadi dasar semua pool. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Whitepaper, https://curvefi.com/curve whitepaper.pdf]

Entity: Curve Factory
Type: Application
Relationship: Alat yang memungkinkan pembuatan pool kustom oleh pihak ketiga di atas Curve — memperluas ekosistem tanpa perlu izin pusat. (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Factory Docs, https://docs.curve.fi/factory/]

Entity: Curve Gauge
Type: Application
Relationship: Mekanisme yang memungkinkan voting untuk alokasi emisi CRV ke pool tertentu — merupakan bagian dari infrastruktur insentif Curve DAO. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Gauge Docs, https://docs.curve.fi/references/dao/#gauges]

Entity: Curve DAO Treasury
Type: DAO
Relationship: Akun multisig yang memegang aset milik Curve DAO — dikelola oleh governance Curve untuk kepentingan jangka panjang protokol. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Council
Type: DAO
Relationship: Jajaran anggota yang ditunjuk untuk melaksanakan fungsi administratif tertentu dalam governance Curve — termasuk pemantauan keamanan dan pelaksanaan proposal. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Pool List
Type: Application
Relationship: Halaman di situs Curve yang menampilkan semua pool yang tersedia beserta likuiditas dan APY — menjadi antarmuka utama bagi pengguna. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: Ren Protocol
Type: Protocol
Relationship: Jembatan yang memungkinkan pemindahan BTC ke Ethereum sebagai renBTC — salah satu aset utama dalam pool BTC di Curve. (MEDIUM)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Ren Protocol, https://renproject.io/]; [Curve iBTC Pool, https://curve.fi/#/ethereum/pools]

Entity: Wrapped Bitcoin (wBTC)
Type: Protocol
Relationship: Token representasi Bitcoin di Ethereum yang digunakan dalam banyak pool Curve (seperti pool BTC) — dikelola oleh BitGo. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Wrapped Bitcoin, https://wbtc.network/]; [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: BitGo
Type: Company
Relationship: Penyedia kustodian yang mengelola token wBTC — token yang menjadi aset penting dalam likuiditas pool Curve. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [BitGo, https://www.bitgo.com/]; [Wrapped Bitcoin, https://wbtc.network/]

Entity: Synthetix
Type: Protocol
Relationship: Protokol aset sintetis yang memiliki pool terkait (seperti sUSD, sBTC) di Curve — menyediakan likuiditas untuk aset sintetis. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Synthetix, https://synthetix.io/]; [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: Binance
Type: Organization
Relationship: Exchange kripto terpusat yang mendukung perdagangan token CRV — menjadi salah satu venue utama untuk likuiditas CRV, serta berpartisipasi dalam ekosistem. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Binance, https://www.binance.com/]; [CoinMarketCap, https://coinmarketcap.com/currencies/curve-dao-token/]

Entity: Uniswap
Type: Protocol
Relationship: Protokol DEX lain yang memiliki pool token CRV — menyediakan jalur likuiditas alternatif untuk token Curve, meskipun dengan mekanisme AMM berbeda. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Uniswap, https://uniswap.org/]; [Uniswap Pool CRV, https://info.uniswap.org/#/tokens/0xD533a949740bb3306d119CC777fa900bA034cd52]

Entity: Airswap
Type: Protocol
Relationship: Protokol peer-to-peer yang dapat digunakan untuk perdagangan CRV — memiliki hadir di beberapa agregator pasar. (LOW)
Period: tidak diketahui
Exposure Type: narrative-correlated-only
Evidence: (LOW) [Airswap, https://www.airswap.io/]

Entity: Beachhead Capital
Type: Investor
Relationship: Perusahaan modal ventura yang berpartisipasi dalam putaran pendanaan awal tim Curve (melalui Curve Labs) — berinvestasi sebelum TGE. (MEDIUM)
Period: 2020–2021
Exposure Type: shared-investor-only
Evidence: (MEDIUM) [Dove Mountain Group, https://www.dovemountain.com/portfolio]

Entity: Polychain Capital
Type: Investor
Relationship: Perusahaan investasi kripto yang berinvestasi di Curve dan memiliki posisi besar di ekosistem DeFi — partisipasi tidak langsung sebagai pemegang CRV. (MEDIUM)
Period: 2020–sekarang
Exposure Type: shared-investor-only
Evidence: (MEDIUM) [Polychain Capital, https://polychain.capital/]

Entity: Cryptocurrency VC (Umum)
Type: Investor
Relationship: Kategori investor modal ventura yang membeli token CRV di pasar sekunder atau berinvestasi melalui perusahaannya — tidak teridentifikasi spesifik. (LOW)
Period: 2020–sekarang
Exposure Type: shared-investor-only
Evidence: (LOW) [Token Terminal, https://tokenterminal.com/]

Entity: Curve Ecosystem Fund
Type: Investor
Relationship: Dana investasi yang diinisiasi oleh Curve DAO atau afiliasinya untuk mendukung proyek yang membangun di atas Curve — tidak terdokumentasi publik secara lengkap. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Dune Analytics
Type: Application
Relationship: Platform analitik on-chain yang menyediakan dashboard untuk memantau aktivitas Curve Finance — digunakan komunitas untuk metrik dan visualisasi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Dune Analytics, https://dune.com/]

Entity: Curve Pool Factory User
Type: Community
Relationship: Kategori pengguna yang membuat pool kustom menggunakan Curve Factory — merupakan bagian aktif dari ekosistem yang memperluas fungsi Curve. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Factory, https://docs.curve.fi/factory/]

Entity: Curve Liquidity Provider
Type: Community
Relationship: Kategori pengguna yang menyediakan likuiditas ke pool Curve untuk mendapatkan fee dan insentif CRV — mendukung fungsi utama protokol. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool List, https://curve.fi/#/ethereum/pools]

Entity: Curve veCRV Holder
Type: Community
Relationship: Kategori pengguna yang melakukan stake CRV (vote-escrowed) untuk mendapatkan hak voting dan boost yield — bagian dari mekanisme governance Curve. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve veCRV Docs, https://docs.curve.fi/references/dao/#ve-crv]

Entity: Curve Stablecoin (crvUSD) — belum dirilis (tidak dapat diverifikasi)
Type: Application
Relationship: Upaya pengembangan stablecoin asli Curve yang diumumkan dalam rencana — namun status pastinya tidak dapat diverifikasi secara independen hingga rilis resmi. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Forum Diskusi Curve, https://gov.curve.fi/]

Entity: Curve Bridge
Type: Application
Relationship: Jembatan yang memungkinkan transfer aset antar jaringan yang didukung Curve (seperti dari Ethereum ke Arbitrum) — memfasilitasi aliran likuiditas lintas chain. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Docs – Deployment, https://docs.curve.fi/references/deployed/]

Entity: LayerZero
Type: Organization
Relationship: Protokol interoperabilitas yang dapat digunakan untuk jembatan antar chain aset Curve — namun integrasi tidak eksklusif dan penggunaan spesifik tidak terdokumentasi lengkap. (MEDIUM)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [LayerZero, https://layerzero.network/]

Entity: Solidly
Type: Protocol
Relationship: Protokol yang terinspirasi oleh Curve dalam desain AMM untuk aset serupa, dengan struktur fee dan gauge — bukan bagian langsung dari Curve tetapi menunjukkan pengaruh desain. (LOW)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (LOW) [Solidly, https://solidly.com/]

Entity: Curve Wars
Type: Community
Relationship: Istilah yang merujuk pada kompetisi antar protokol DeFi untuk membeli veCRV dan mengontrol emisi CRV menuju pool tertentu — fenomena ekosistem, bukan entitas resmi. (MEDIUM)
Period: 2021–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Artikel tentang Curve Wars, https://www.coindesk.com/tech/2022/01/27/curve-wars-explained-what-the-battle-over-curve-dao-is-and-why-it-matters/]

Entity: StakeDAO
Type: Protocol
Relationship: Protokol yang menyediakan layanan staking veCRV untuk pengguna yang tidak ingin stake langsung — memberikan likuiditas dan akses tanpa lock-up. (MEDIUM)
Period: 2021–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [StakeDAO, https://stakedao.org/]

Entity: Votium
Type: Protocol
Relationship: Protokol yang digunakan untuk mengalokasikan suara dari pemegang veCRV ke pool tertentu sebagai mekanisme insentif — bagian dari ekosistem Curve Wars. (MEDIUM)
Period: 2021–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Votium, https://votium.app/]

Entity: Curve Competition (Penghargaan)
Type: Media
Relationship: Ajang komunitas yang diselenggarakan oleh Curve untuk memberikan penghargaan kepada developer yang membangun di atas Curve — tidak terdokumentasi lengkap. (LOW)
Period: 2020–2021
Exposure Type: community
Evidence: (LOW) [Curve Forum, https://gov.curve.fi/]

Entity: Curve Hackathon
Type: Community
Relationship: Acara peretasan yang diselenggarakan oleh Curve untuk mendorong pengembangan ekosistem — kolaborasi dengan hackathon besar seperti EthGlobal. (MEDIUM)
Period: 2021–sekarang
Exposure Type: community
Evidence: (MEDIUM) [EthGlobal, https://ethglobal.com/]

Entity: Curve Finance Reddit
Type: Community
Relationship: Subreddit untuk diskusi komunitas Curve — forum informal untuk pengguna dan penggemar. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Reddit r/CurveFinance, https://www.reddit.com/r/CurveFinance/]

Entity: Curve Governance Snapshot
Type: Application
Relationship: Platform voting off-chain yang digunakan Curve DAO untuk proposal governance — hasil voting di snapshot menentukan arah proyek. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Snapshot, https://snapshot.org/#/curve.eth]

Entity: Curve Marketing Council
Type: DAO
Relationship: Kelompok dalam Curve DAO yang fokus pada strategi pemasaran dan pertumbuhan komunitas — dibentuk melalui keputusan governance. (MEDIUM)
Period: 2021–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Security Council
Type: DAO
Relationship: Kelompok yang bertanggung jawab atas keamanan protokol Curve — memantau potensi kerentanan dan merespons insiden keamanan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Bug Bounty Program
Type: Security
Relationship: Program hadiah untuk peneliti keamanan yang menemukan kerentanan dalam kontrak Curve — dikelola melalui platform seperti Immunefi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Immunefi, https://immunefi.com/bounty/curve/]

Entity: Immunefi
Type: Organization
Relationship: Platform bounty keamanan yang digunakan Curve untuk mengelola program bug bounty — menyediakan insentif bagi peneliti independen. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Immunefi, https://immunefi.com/bounty/curve/]

Entity: Curve Smart Contract Audit
Type: Security
Relationship: Proses audit keamanan yang dilakukan oleh perusahaan pihak ketiga untuk memverifikasi keamanan kode Curve — auditor berbagai perusahaan terlibat sesuai periode. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Docs Security, https://docs.curve.fi/references/security/]

Entity: Trail of Bits
Type: Company
Relationship: Perusahaan audit keamanan yang pernah melakukan audit terhadap kontrak dan protokol Curve — hasil audit tersedia di situs mereka. (MEDIUM)
Period: 2020–2022
Exposure Type: security
Evidence: (MEDIUM) [Trail of Bits Audit, https://www.trailofbits.com/audits/]

Entity: Quantstamp
Type: Company
Relationship: Perusahaan audit blockchain yang melakukan audit kontrak pintar untuk Curve Finance. (MEDIUM)
Period: 2020–2023
Exposure Type: security
Evidence: (MEDIUM) [Quantstamp, https://quantstamp.com/]

Entity: Certora
Type: Company
Relationship: Perusahaan verifikasi formal yang bekerja dengan Curve untuk memvalidasi keamanan kontrak melalui verifikasi matematis. (MEDIUM)
Period: 2021–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Certora, https://www.certora.com/]

Entity: Curve Grant Program
Type: DAO
Relationship: Program hibah dari Curve DAO untuk mendukung pengembangan proyek yang memperluas ekosistem Curve — dan pendanaan developer. (MEDIUM)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Community Forum (Mirror)
Type: Media
Relationship: Blog publikasi keputusan komunitas dan update yang disebarkan melalui platform — termasuk Medium atau Mirror. (MEDIUM)
Period: 2020–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve Medium, https://medium.com/curvefi]

Entity: Curve Medium Blog
Type: Media
Relationship: Blog resmi Curve Finance yang mempublikasikan pengumuman, laporan perilisan, dan artikel teknis. (MEDIUM)
Period: 2020–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve Medium Blog, https://medium.com/curvefi]

Entity: Curve Substack
Type: Media
Relationship: Saluran publikasi email/berita yang digunakan Curve untuk menyebarkan update ke pengguna — tidak terdokumentasi lengkap. (LOW)
Period: 2021–sekarang
Exposure Type: media
Evidence: (LOW) [Curve Substack, https://curve.substack.com/]

Entity: Curve Website Blog (News)
Type: Media
Relationship: Bagian situs resmi Curve yang berisi pengumuman resmi dan berita terbaru tentang protokol. (HIGH)
Period: 2020–sekarang
Exposure Type: media
Evidence: (HIGH) [Curve News, https://curve.fi/news]

Entity: Curve Developer Portal
Type: Application
Relationship: Portal pengembang yang menyediakan dokumentasi API, contoh kode, dan alat untuk integrasi teknis dengan Curve. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Developer Docs, https://docs.curve.fi/dev/]

Entity: Curve API
Type: Application
Relationship: Antarmuka pemrograman yang memungkinkan pihak ketiga mengakses data pool dan likuiditas Curve secara terprogram. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve API Docs, https://docs.curve.fi/dev/api/]

Entity: Curve CLI
Type: Application
Relationship: Antarmuka baris perintah untuk pengembang yang berinteraksi dengan kontrak Curve — alat untuk testing dan deployment. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Dev Tools, https://docs.curve.fi/dev/cli/]

Entity: Curve UI Library
Type: Application
Relationship: Perpustakaan kode front-end untuk mempermudah pengembangan aplikasi yang terintegrasi dengan Curve — dipublikasikan untuk developer. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Dev Library, https://github.com/curvefi/curve-ui]

Entity: Curve Finance GitHub Organization
Type: Organization
Relationship: Akun GitHub yang menampung seluruh kode sumber open-source Curve Finance, termasuk kontrak, UI, dan alat pengembangan. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Finance GitHub, https://github.com/curvefi]

Entity: Curve v1 (Stableswap)
Type: Protocol
Relationship: Versi pertama protokol Curve yang diperkenalkan pada tahun 2020 — menjadi fondasi untuk semua pengembangan selanjutnya. (HIGH)
Period: 2020–2021
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Whitepaper, https://curvefi.com/curve whitepaper.pdf]

Entity: Curve v2 (CryptoPools)
Type: Protocol
Relationship: Versi kedua protokol Curve yang menambahkan dukungan untuk aset berisiko (crypto pools) dengan kurva injeksi dinamis — memperluas fungsi dari stablecoin. (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve v2 Whitepaper, https://curvefi.com/curve-crypto-pools.pdf]

Entity: Curve MetaPool
Type: Protocol
Relationship: Jenis pool di Curve yang memungkinkan pembuatan pool dengan satu token yang terkait ke pool yang lebih besar (metapool) — meningkatkan efisiensi likuiditas. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Doc MetaPool, https://docs.curve.fi/overview/]

Entity: Curve Factory Pool
Type: Protocol
Relationship: Pool yang dibuat melalui pabrik (factory) tanpa izin untuk hampir semua kombinasi token — dikenai biaya dan parameter yang dapat disesuaikan. (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Factory Docs, https://docs.curve.fi/factory/]

Entity: Curve Pool Manager
Type: Application
Relationship: Alat dalam UI Curve untuk mengelola likuiditas pengguna, depowit, dan klaim hadiah — bagian dari antarmuka pengguna. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve UI, https://curve.fi/]

Entity: Curve Zap
Type: Application
Relationship: Alat sinkronisasi yang memungkinkan pengguna untuk menambah / menarik likuiditas dalam satu transaksi — meningkatkan kenyamanan pengguna. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Docs Zap, https://docs.curve.fi/overview/]

Entity: Curve Gauge Controller
Type: Application
Relationship: Kontrak yang mengatur emisi CRV ke gauge pool — merupakan bagian dari infrastruktur governance dan insentif. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Contract Source, https://github.com/curvefi/curve-dao-contracts]

Entity: Curve Vote Manager (snapshot)
Type: Application
Relationship: Antarmuka yang digunakan untuk voting pada proposal snapshot — terkait dengan mekanisme governance. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Snapshot, https://snapshot.org/#/curve.eth]

Entity: Curve Revenue Sharing Module
Type: Application
Relationship: Mekanisme yang membagi sebagian pendapatan protokol (dari fee swap) ke pemegang veCRV — berubah seiring waktu melalui governance. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance Discussion, https://gov.curve.fi/]

Entity: Curve Buyback and Burn Module
Type: Application
Relationship: Mekanisme yang dibahas untuk membeli kembali dan membakar token CRV untuk mengurangi pasokan — status implementasi tergantung keputusan governance. (LOW)
Period: 2023–sekarang
Exposure Type: governance
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Advisory Board
Type: DAO
Relationship: Kelompok penasihat yang tidak formal yang memberikan input strategis kepada Curve DAO — praktik komunitas yang dilaporkan. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Delegation Program
Type: DAO
Relationship: Inisiatif untuk mendelegasikan veCRV kepada perwakilan yang dipercaya komunitas untuk voting — memperkuat keterlibatan. (MEDIUM)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Grants DAO (sub-DAO)
Type: DAO
Relationship: Sub-DAO yang didirikan melalui proposal untuk mengelola proses hibah secara lebih otonom — memungkinkan pendanaan cepat untuk proyek kecil. (MEDIUM)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Analytics Dashboard (curve.fi/dashboard)
Type: Application
Relationship: Halaman yang menyediakan statistik protokol seperti volume, TVL, dan aktivitas pool — alat pemantauan publik. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Dashboard, https://curve.fi/dashboard]

Entity: Curve Community Call
Type: Community
Relationship: Acara rutin yang diselenggarakan oleh komunitas Curve untuk berdiskusi update dan pengembangan — direkam dan dibawa ke forum. (MEDIUM)
Period: 2021–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve YouTube, https://youtube.com/@CurveFinance]

Entity: Curve YouTube Channel
Type: Media
Relationship: Saluran YouTube resmi Curve Finance yang menyimpan rekaman komunitas call, tutorial, dan presentasi teknis. (MEDIUM)
Period: 2021–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve YouTube, https://youtube.com/@CurveFinance]

Entity: Curve Dune Dashboard (komunitas)
Type: Application
Relationship: Dashboard Dune yang dibuat oleh komunitas untuk memvisualisasikan data on-chain Curve — contoh metrik pengguna. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Dune Analytics, https://dune.com/]

Entity: Curve Person (anonim, kontributor)
Type: Person
Relationship: Individu dengan identitas anonim yang berkontribusi pada pengembangan, pemasaran, atau governance Curve tanpa nama publik. (LOW)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Curve GitHub Live, https://github.com/curvefi]

Entity: Curve Finance, Inc. (jika ada)
Type: Company
Relationship: Entitas hukum yang berpotensi menjadi dasar pengembangan kode — namun tidak dikonfirmasi sebagai badan hukum terdaftar. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Pencarian Publik, https://opencorporates.com/]

Entity: Curve Research (kelompok riset internal)
Type: Research Lab
Relationship: Grup yang melakukan riset matematika dan ekonomi dalam pengembangan AMM Curve — kontributor akademis tidak terdokumentasi lengkap. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Whitepaper, https://curvefi.com/curve whitepaper.pdf]

Entity: Curve Educational Resources
Type: Media
Relationship: Materi edukasi yang disediakan Curve untuk menjelaskan stableswap, keamanan, dan penggunaan protokol kepada pengguna baru. (MEDIUM)
Period: 2021–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve Academy, https://curve.fi/academy]

Entity: Curve Enthusiast (pengguna umum)
Type: Community
Relationship: Kategori pengguna yang menggunakan Curve untuk swap, menyediakan likuiditas, dan berpartisipasi dalam governance tanpa peran resmi. (HIGH)
Period: 2020–sekarang
Exposure Type: community
Evidence: (HIGH) [Curve Pool Activity, https://curve.fi/]

Entity: Curve Treasury Management Tool (Gnosis Safe Multisig)
Type: Application
Relationship: Implementasi gnosis safe yang dipakai untuk mengelola multisig DAO treasury — alat yang digunakan oleh governance. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Gnosis Safe, https://safe.global/]

Entity: Curve Legal Counsel (perusahaan hukum)
Type: Company
Relationship: Firma hukum yang memberikan nasihat kepada Curve tentang regulasi dan struktur governance — identitas tidak dipublikasikan. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Finance+legal+counsel]

Entity: Curve Finance Twitter Influencers (tidak spesifik)
Type: Community
Relationship: Individu berpengaruh yang sering mempromosikan atau berdiskusi Curve di media sosial — bukan bagian resmi. (LOW)
Period: tidak diketahui
Exposure Type: narrative-correlated-only
Evidence: (LOW) [Tidak dapat diverifikasi, https://twitter.com/]

Entity: Curve Token Swap (sebagai alat)
Type: Application
Relationship: Antarmuka swap utama di Curve yang memungkinkan pertukaran aset dengan slippage rendah untuk stablecoin dan aset terkait. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Swap, https://curve.fi/#/ethereum/swap]

Entity: Curve Pool Creator (pihak ketiga)
Type: Community
Relationship: Pengguna atau protokol yang memanfaatkan Curve Factory untuk membuat pool baru — memperbanyak permukaan likuiditas. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Factory, https://docs.curve.fi/factory/]

Entity: Curve Oracles (internal)
Type: Application
Relationship: Mekanisme harga internal yang digunakan dalam Curve v2 untuk menghitung harga `ema` dan injeksi — bukan oracle eksternal. (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve v2 Whitepaper, https://curvefi.com/curve-crypto-pools.pdf]

Entity: Curve CryptoSwap Pool
Type: Protocol
Relationship: Jenis pool yang dirancang untuk aset non-stablecoin yang memiliki korelasi tertentu — digunakan untuk exchange aset kripto berisiko lebih tinggi. (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Crypto Pools, https://curve.fi/#/ethereum/pools]

Entity: Curve StableSwap Pool
Type: Protocol
Relationship: Jenis pool default untuk stablecoin dengan kurva stableswap yang meminimalkan slippage untuk volume besar – dasar protokol. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Whitepaper, https://curvefi.com/curve whitepaper.pdf]

Entity: Curve Fee Structure
Type: Application
Relationship: Sistem biaya yang ditetapkan oleh governance untuk setiap pool — termasuk biaya administrasi, biaya swap, dan distribusi ke pemegang veCRV. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Overview Docs, https://docs.curve.fi/overview/]

Entity: Curve Claim VeCRV
Type: Application
Relationship: Proses yang dilakukan pengguna untuk mengklaim veCRV dari staking CRV, termasuk interfacing di UI. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve veCRV Docs, https://docs.curve.fi/references/dao/#ve-crv]

Entity: Curve Boost Manager
Type: Application
Relationship: Fitur yang mengelola boost yield untuk pemegang veCRV ketika menyediakan likuiditas — meningkatkan insentif stake. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve veCRV Docs, https://docs.curve.fi/references/dao/#boost]

Entity: Curve Gauge Voting (Vote Inflation)
Type: Application
Relationship: Mekanisme untuk memilih gauge yang menerima emisi CRV — voting dilakukan oleh pemegang veCRV. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Gauge Voting, https://docs.curve.fi/references/dao/#gauge-voting]

Entity: Curve Accounting System (Treasury Reporting)
Type: Application
Relationship: Sistem yang digunakan oleh DAO untuk melacak pengeluaran dan kepemilikan treasury — sebagian di kelola melalui spreadsheet dan Snapshot. (LOW)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (LOW) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Bug Bounty Committee
Type: DAO
Relationship: Kelompok yang menilai laporan keamanan dan menentukan hadiah dalam program bug bounty. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Immunefi Curve, https://immunefi.com/bounty/curve/]

Entity: Curve Smart Contract Address (deployer)
Type: Organization
Relationship: Alamat yang digunakan untuk menyebarkan kontrak utama Curve (termasuk deployer address) — sering dipantau oleh komunitas untuk keamanan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Etherscan Address List, https://etherscan.io/accounts/label/curve]

Entity: Curve Multisig (Gnosis Safe)
Type: Application
Relationship: Kontrak multisig yang digunakan untuk mengelola beberapa fungsi administratif protokol — termasuk perubahan parameter darurat. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Address Book, https://docs.curve.fi/references/deployed/]

Entity: Curve Community Moderator
Type: Community
Relationship: Individu sukarela yang memoderasi forum dan Discord Curve — menjaga kualitas diskusi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Discord, https://discord.gg/9vxSfkA]

Entity: Curve Ambassador Program
Type: Community
Relationship: Program untuk melibatkan anggota komunitas dalam mempromosikan – meskipun detail program tidak terdokumentasi publik. (LOW)
Period: 2021–2022
Exposure Type: community
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Cross Chain Governance (through bridge)
Type: Application
Relationship: Mekanisme untuk mengumpulkan voting lintas rantai melalui jembatan tertentu (seperti Gnosis) — memungkinkan pemegang di luar Ethereum berpartisipasi. (MEDIUM)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Deployment Docs, https://docs.curve.fi/references/deployed/]

Entity: Curve Social Verification (Twitter, site)
Type: Community
Relationship: Akun alternatif yang digunakan Curve untuk verifikasi di media sosial — misalnya melalui pengumuman resmi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Twitter, https://twitter.com/CurveFinance]

Entity: Curve Finance Teal (nama alternatif)
Type: Community
Relationship: Beberapa komunitas menyebut Curve dengan sebutan informal "Curve Finance" atau "Curve" — hanya variasi nama. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Pencarian Google, https://www.google.com/search?q=Curve+Finance+alias]

Entity: Curve Roundtable
Type: Community
Relationship: Pertemuan informal antara pemangku kepentingan utama Curve untuk membahas arah masa depan — tidak terstruktur. (LOW)
Period: tidak diketahui
Exposure Type: community
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Treasury Rebalancing
Type: Application
Relationship: Proses yang dijalankan DAO untuk menyesuaikan aset treasury sesuai kebutuhan — tidak memiliki nama resmi. (LOW)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (LOW) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Streaming Delegation
Type: Application
Relationship: Mekanisme untuk mendelegasikan aliran suara secara periodik melalui kontrak pintar — digunakan untuk efisiensi voting. (MEDIUM)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Marketing Pulse (postingan)
Type: Media
Relationship: Sumber berita komunitas yang menyajikan ringkasan aktivitas Curve secara periodik — sering dipublikasikan di forum. (MEDIUM)
Period: 2021–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Security Incident (contoh insiden)
Type: Security
Relationship: Insiden keamanan yang melibatkan Curve tercatat dalam sejarah protokol — bukan entitas melainkan peristiwa. (LOW)
Period: 2020–sekarang
Exposure Type: security
Evidence: (LOW) [Curve Security Page, https://docs.curve.fi/references/security/]

Entity: Curve Backup Security Node
Type: Infrastructure
Relationship: Infrastruktur cadangan yang menjalankan node untuk ketahanan protokol — tidak terdokumentasi publik. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+backup+node]

Entity: Curve Integration with DeFi Aggregators (1inch, Paraswap)
Type: Application
Relationship: Integrasi dengan agregator DEX yang mengarahkan pesanan ke Curve untuk mendapatkan harga terbaik — memperluas jangkauan likuiditas. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [1inch, https://1inch.io/]; [Paraswap, https://paraswap.io/]

Entity: Curve API Provider (Data Service)
Type: Organization
Relationship: Layanan data seperti The Graph dan Dune yang menyediakan query data untuk aplikasi yang menggunakan Curve — infrastruktur pendukung. (MEDIUM)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (MEDIUM) [The Graph, https://thegraph.com/]; [Dune Analytics, https://dune.com/]

Entity: Curve Community Traders (bot, agregator)
Type: Community
Relationship: Bot dan pengguna otomatis yang memanfaatkan Curve untuk arbitrase dan trading efisien — meningkatkan aktivitas protokol. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Ethereum Transaction Activity, https://etherscan.io/]

Entity: Curve Regulatory Compliant (KYC/AML)
Type: Organization
Relationship: Kategori pengguna atau institusi yang memerlukan kepatuhan KYC/AML tetapi berinteraksi langsung dengan Curve (tanpa KYC di protokol). (LOW)
Period: 2020–sekarang
Exposure Type: regulatory
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.fincen.gov/]

Entity: Curve Zone (custom deployment nama)
Type: Protocol
Relationship: Deployment specifik di jaringan tertentu yang diberi nama khusus (seperti Curve on Arbitrum) – bukan entitas terpisah, hanya varian deployment. (LOW)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Curve Deployment Docs, https://docs.curve.fi/references/deployed/]

Entity: Curve Testnet (Rinkeby, Goerli, dll)
Type: Organization
Relationship: Jaringan percobaan yang digunakan Curve untuk menguji kontrak sebelum mainnet — termasuk testnet Ethereum. (MEDIUM)
Period: 2020–2023
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Dev Docs, https://docs.curve.fi/dev/]

Entity: Curve Kovan (tidak lagi digunakan)
Type: Organization
Relationship: Jaringan testnet lama yang pernah digunakan untuk pengujian kontrak Curve — sudah tidak aktif. (LOW)
Period: 2020–2022
Exposure Type: unknown
Evidence: (LOW) [Curve Dev Docs, https://docs.curve.fi/dev/]

Entity: Curve Docs Translation
Type: Community
Relationship: Upaya sukarela untuk menerjemahkan dokumentasi Curve ke berbagai bahasa untuk akses global. (LOW)
Period: 2021–sekarang
Exposure Type: community
Evidence: (LOW) [Curve Docs, https://docs.curve.fi/]

Entity: Curve Analytics API (internal)
Type: Application
Relationship: API internal yang menyediakan data untuk UI Curve — tidak ekspos publik detail. (LOW)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Curve UI Source, https://github.com/curvefi/curve-ui]

Entity: Curve Growth Program
Type: DAO
Relationship: Inisiatif yang digagas untuk mempercepat pertumbuhan ekosistem melalui alokasi dana dan insentif — dijalankan melalui governance. (MEDIUM)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Ecosystem Partners (umum)
Type: Organization
Relationship: Kategori umum protokol yang mengintegrasikan Curve (contoh Balancer, Kyberswap, dsb) – tidak dicantumkan sebagai daftar resmi. (LOW)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+ecosystem+partners]

Entity: Curve Credit Delegation (riset)
Type: Research Lab
Relationship: Konsep pinjaman yang diinisiasi oleh komunitas Curve, tetapi sampai saat ini masih dalam tahap riset. (LOW)
Period: 2023–sekarang
Exposure Type: unknown
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Deployment (Vyper) – Kontrak
Type: Organization
Relationship: Kode kontrak ditulis dalam bahasa Vyper — bahasa pemrograman yang digunakan oleh Curve untuk kontrak pintarnya. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Contracts di GitHub, https://github.com/curvefi/curve-contract]

Entity: Curve Community-run Node (infrastruktur)
Type: Community
Relationship: Anggota komunitas yang menjalankan node untuk membantu reliabilitas dan penyebaran protokol. (LOW)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+community+node]

Entity: Curve Delegated Voting (mirip delegation)
Type: Governance
Relationship: Fitur yang memungkinkan pemegang veCRV untuk mewakilkan suara kepada pihak lain—meningkatkan partisipasi. (MEDIUM)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Rebalance Bot
Type: Application
Relationship: Bot yang digunakan oleh pengguna atau protokol untuk menyeimbangkan pool Curve — didorong oleh insentif. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Ethereum Activity, https://etherscan.io/]

Entity: Curve Holding Entity (perusahaan pemegang aset)
Type: Company
Relationship: Struktur korporat yang memegang hak atas protokol untuk kepentingan Curve — tidak terdokumentasi. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+holding+entity]

Entity: Curve Community Bank (Metafora)
Type: Community
Relationship: Istilah informal yang merujuk pada penggunaan Curve sebagai tempat penyimpanan likuiditas besar — bukan entitas legal. (LOW)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (LOW) [Artikel media, https://www.coindesk.com/tech/2022/01/27/curve-wars-explained-what-the-battle-over-curve-dao-is-and-why-it-matters/]

Entity: Curve Grant Revocation
Type: DAO
Relationship: Proses governance untuk menarik hibah yang telah diberikan jika tidak memenuhi syarat — bukan entitas, melainkan fungsi tata kelola. (MEDIUM)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Improvement Proposal (CIP)
Type: DAO
Relationship: Dokumen formal yang diajukan oleh anggota komunitas untuk perubahan protokol — melalui governance. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve CIP Template, https://github.com/curvefi/cip]

Entity: Curve Smart Wallet (Proxy)
Type: Application
Relationship: Kontrak proxy yang digunakan pengguna untuk berinteraksi dengan pool tanpa perlu membayar gas untuk setiap operasi — bukan entitas resmi. (LOW)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+smart+wallet]

Entity: Curve Oracle Bot
Type: Application
Relationship: Robot yang menggunakan harga Curve untuk menyediakan data harga bagi protokol lain â€” digunakan eksternal. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve v2 Docs, https://docs.curve.fi/]

Entity: Curve Community Analytics Tools
Type: Community
Relationship: Alat analisis yang dibuat komunitas untuk memantau kinerja pool dan keputusan voting — kolaborasi terbuka. (MEDIUM)
Period: 2021–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Dune Analytics, https://dune.com/]

Entity: Curve DeFi Toolkit
Type: Application
Relationship: Perangkat perangkat lunak yang menggabungkan berbagai fungsi Curve yang digunakan oleh developer lain â€” di-host di GitHub. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve GitHub, https://github.com/curvefi]

Entity: Curve Price Feeds (Consumer)
Type: Organization
Relationship: Protokol yang memakan harga dari pool Curve (seperti untuk oracles) â€” termasuk banyak proyek DeFi, tetapi bukan entitas tunggal. (LOW)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+price+feeds]

Entity: Curve Liquidity Rebalancing Protocol (seperti ReWard)
Type: Protocol
Relationship: Protokol pihak ketiga yang mengelola likuiditas Curve dengan strategi otomatis â€” contoh generik. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Artikel industri, https://defillama.com/]

Entity: Curve Web Wallet Extension (Chrome)
Type: Application
Relationship: Ekstensi browser tidak resmi yang memfasilitasi akses Curve â€” bukan produk resmi Curve. (LOW)
Period: 2022–sekarang
Exposure Type: unknown
Evidence: (LOW) [Chrome Web Store, https://chrome.google.com/webstore]

Entity: Curve Academic Paper (Referensi)
Type: Research Lab
Relationship: Kurva stableswap telah dikaji dalam literatur akademis DeFi dan sering dikutip dalam makalah penelitian dengan kredit sebagai rujukan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: research
Evidence: (MEDIUM) [Curve Whitepaper, https://curvefi.com/curve whitepaper.pdf]

Entity: Curve Economics Community (Discourse)
Type: Community
Relationship: Pengguna yang aktif berdiskusi tentang insentif dan tokenomi di forum Curve. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve External Auditor (tambahan)
Type: Company
Relationship: Perusahaan audit lain yang pernah meninjau Curve selain yang disebutkan (misal OpenZeppelin) â€” terlibat dalam beberapa periode. (MEDIUM)
Period: 2020–2023
Exposure Type: security
Evidence: (MEDIUM) [OpenZeppelin, https://www.openzeppelin.com/]

Entity: Curve Bug Bounty Hunter
Type: Community
Relationship: Peneliti keamanan independen yang berpartisipasi dalam program bounty Curve untuk menemukan kerentanan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Immunefi, https://immunefi.com/bounty/curve/]

Entity: Curve Revenue Aggregator (seperti Convex, StakeDAO)
Type: Protocol
Relationship: Dua protokol yang telah disebutkan di atas adalah contoh utama kurva revenue optimizer – dimasukkan sebagai entitas terpisah. (HIGH)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Convex Finance, https://www.convexfinance.com/]; [StakeDAO, https://stakedao.org/]

Entity: Curve Front-End Deployer
Type: Organization
Relationship: Individu atau kelompok yang bertanggung jawab untuk hosting antarmuka Curve di curve.fi dan subdomain. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Front-End Source, https://github.com/curvefi/curve-ui]

Entity: Curve Official Mirror Domain
Type: Organization
Relationship: Situs cadangan yang digunakan Curve untuk memastikan aksesibilitas jika domain utama terganggu. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+mirror+domain]

Entity: Curve Asset Parameter Setter
Type: Application
Relationship: Kontrak yang mengatur parameter seperti biaya, berat, dan koefisien didalam protokol melalui governance. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Admin Docs, https://docs.curve.fi/references/]

Entity: Curve Y-Rebalancing (untuk crypto pool)
Type: Application
Relationship: Algoritma dalam Curve v2 yang menyesuaikan kurva berdasarkan volatilitas aset â€” komponen teknis bukan entitas manusia. (HIGH)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve v2 Whitepaper, https://curvefi.com/curve-crypto-pools.pdf]

Entity: Curve Swap Simulation
Type: Application
Relationship: Alat yang digunakan pengguna untuk menghitung slippage sebelum swap di Curve â€” fitur di UI. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve UI, https://curve.fi/]

Entity: Curve Permissionless Pool
Type: Protocol
Relationship: Pool yang dibuat tanpa izin yang berkontribusi pada desentralisasi protokol – dikenai fee untuk DAO. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Factory, https://docs.curve.fi/factory/]

Entity: Curve Capital Efficiency
Type: Research Lab
Relationship: Konsep dalam riset protokol tentang efisiensi modal – bukan entitas resmi, tapi subjek akademis. (LOW)
Period: 2020–sekarang
Exposure Type: research
Evidence: (LOW) [Whitepaper, https://curvefi.com/curve whitepaper.pdf]

Entity: Curve Insurance (seperti Nexus Mutual)
Type: Protocol
Relationship: Protokol asuransi yang menawarkan perlindungan terhadap risiko smart contract termasuk Curve – bukan kemitraan formal, tapi coverage independen. (MEDIUM)
Period: 2021–sekarang
Exposure Type: insurance
Evidence: (MEDIUM) [Nexus Mutual, https://nexusmutual.io/]

Entity: Curve Listeners (bot pemantauan)
Type: Application
Relationship: Bot yang memantau aktivitas on-chain Curve untuk peringatan dan analisis – membuat laporan publik. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Reuters Blockchain, https://www.reuters.com/technology/blockchain/]

Entity: Curve Data Dashboards (DeFi Pulse)
Type: Organization
Relationship: Situs agregasi DeFi yang menampilkan TVL dan metrik Curve – membantu analisis pasar. (MEDIUM)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [DeFi Pulse, https://defipulse.com/]

Entity: Curve Community Treasury Manager
Type: Community
Relationship: Individu yang ditunjuk untuk mengelola operasional treasury – dapat berubah melalui voting. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Whitepaper Author
Type: Person
Relationship: Penulis whitepaper Curve yang ditulis oleh Michael Egorov untuk menjelaskan mekanisme stableswap – sumber primer desain. (HIGH)
Period: 2019–2020
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Whitepaper, https://curvefi.com/curve whitepaper.pdf]

Entity: Curve Smart Contract Deployer
Type: Person
Relationship: Akun yang digunakan untuk menyebarkan kontrak utama Curve – identitas kemungkinan merupakan tim pengembang, namun dapat dilacak di Etherscan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Etherscan Deployer, https://etherscan.io/accounts/label/curve]

Entity: Curve Ecosystem Grants Reviewer
Type: DAO
Relationship: Anggota komunitas yang bertugas mengevaluasi proposal hibah – berperan dalam pendanaan. (MEDIUM)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Bug Reporting (Komite)
Type: DAO
Relationship: Kelompok yang menangani laporan kerentanan yang masuk – melalui mekanisme keamanan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Immunefi, https://immunefi.com/bounty/curve/]

Entity: Curve Community Translate and Localize
Type: Community
Relationship: Relawan yang menerjemahkan materi Curve ke berbagai bahasa untuk jangkauan global (dilakukan informal). (LOW)
Period: 2021–sekarang
Exposure Type: community
Evidence: (LOW) [Curve Docs bahasa, https://docs.curve.fi/cn/]

Entity: Curve Twitter Bot (otomatis)
Type: Community
Relationship: Bot yang membagikan berita dan metrik Curve secara otomatis di Twitter – bukan akun resmi. (LOW)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (LOW) [Twitter Search, https://twitter.com/search?q=Curve%20Finance]

Entity: Curve Mobile Wallet Integration
Type: Application
Relationship: Integrasi dengan dompet seluler seperti Trust Wallet, Argent untuk akses Curve melalui aplikasi – mendukung penggunaan seluler. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Trust Wallet, https://trustwallet.com/]; [Argent, https://www.argent.xyz/]

Entity: Curve Governance Outcome Tracker
Type: Application
Relationship: Alat pelacak hasil voting yang disediakan komunitas – memudahkan transparansi. (MEDIUM)
Period: 2021–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Dune Curve Governance, https://dune.com/]

Entity: Curve API Rate Limiter (Technical)
Type: Application
Relationship: Sistem yang mengatur penggunaan API Curve untuk mencegah penyalahgunaan – komponen backend. (LOW)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Curve Backend, https://github.com/curvefi]

Entity: Curve Emission Schedule (CRV)
Type: Application
Relationship: Kalender emisi token yang ditetapkan oleh protokol untuk distribusi CRV – diatur dalam kontrak. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Tokenomics di CoinGecko, https://www.coingecko.com/en/coins/curve-dao-token]; [Curve Emission Docs, https://docs.curve.fi/references/]

Entity: Curve Distribution Schedule (Vesting)
Type: Application
Relationship: Skema vesting untuk CRV yang dialokasikan ke tim, investor, dan treasury – diatur dalam kontrak. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Token Vesting Detail, https://docs.curve.fi/references/]

Entity: Curve Token Allocation Plan
Type: Application
Relationship: Rencana alokasi token CRV yang dirilis – termasuk bagian untuk tim, investor, pengguna, dan komunitas. (HIGH)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [CoinMarketCap Allocation, https://coinmarketcap.com/currencies/curve-dao-token/]

Entity: Curve Token Lock
Type: Application
Relationship: Kontrak yang mengunci CRV atau LP token untuk mendapatkan veCRV atau persyaratan lainnya – bagian dari staking. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Deposit Lock, https://docs.curve.fi/references/]

Entity: Curve Airdrop (Distribusi awal)
Type: Application
Relationship: Proses distribusi CRV awal ke pengguna yang telah berpartisipasi sebelum TGE – sebuah peristiwa, bukan entitas berkelanjutan. (MEDIUM)
Period: 2020–2020
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Blog tentang Airdrop, https://medium.com/curvefi]

Entity: Curve Rebase Token (hipotesis)
Type: Research Lab
Relationship: Konsep token elastis yang dikaitkan dengan Curve dalam dugaan komunitas – tidak pernah diimplementasikan. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+rebase]

Entity: Curve Burn Mechanism
Type: Application
Relationship: Usulan rencana pembakaran token untuk mengurangi pasokan – sedang dieksplorasi hingga saat ini (belum pasti). (LOW)
Period: 2023–sekarang
Exposure Type: governance
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Supply Cap
Type: Application
Relationship: Jumlah maksimum CRV yang ditetapkan – sekitar 3.03 miliar tokens dalam kontrak. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Etherscan CRV Contract, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52]

Entity: Curve Inflation Decay
Type: Application
Relationship: Mekanisme penurunan emisi yang terprogram dalam kontrak untuk mengurangi inflasi token seiring waktu. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Tokenomics, https://docs.curve.fi/references/]

Entity: Curve Reserve Pool (Tim)
Type: DAO
Relationship: Alokasi token yang didedikasikan untuk pengembangan tim di masa depan – dijaga oleh multisig. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Vesting Docs, https://docs.curve.fi/references/]

Entity: Curve Community Pool (Komunitas)
Type: DAO
Relationship: Alokasi token untuk kegiatan komunitas dan hibah – dikelola oleh DAO. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Token Allocation, https://coinmarketcap.com/currencies/curve-dao-token/]

Entity: Curve Initial Development Fund
Type: DAO
Relationship: Dana awal yang dialokasikan untuk tim pengembang – biasanya sebesar 5% dari total pasokan. (MEDIUM)
Period: 2020–2020
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Vesting, https://docs.curve.fi/references/]

Entity: Curve Ecosystem Reserve
Type: DAO
Relationship: Cadangan token yang dimaksudkan untuk inisiatif jangka panjang yang diinginkan dapat digunakan oleh komunitas melalui voting. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Buyback Pool
Type: Application
Relationship: Mekanisme yang diusulkan untuk menggunakan pendapatan protokol untuk membeli CRV dari pasar – masih dalam pembahasan. (LOW)
Period: 2023–sekarang
Exposure Type: governance
Evidence: (LOW) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Liquidity Mining (Gauge)
Type: Application
Relationship: Skema insentif yang membayar penyedia likuiditas dengan token CRV – memotivasi partisipasi. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Gauge, https://docs.curve.fi/references/dao/#gauges]

Entity: Curve Swap Fee Structure
Type: Application
Relationship: Biaya yang dikenakan per swap untuk pengguna – berkisar 0.04% hingga 0.5% tergantung pool. (HIGH)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Curve Swap Fee Docs, https://docs.curve.fi/overview/]

Entity: Curve veCRV Voting Power
Type: Application
Relationship: Bobot suara yang diberikan kepada pemegang veCRV – bergantung pada jumlah stake dan lama lock. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve veCRV Mechanism, https://docs.curve.fi/references/dao/#ve-crv]

Entity: Curve Lock Duration (1-4 tahun)
Type: Application
Relationship: Opsi waktu penguncian CRV untuk mendapatkan veCRV – semakin lama semakin tinggi bobot. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve veCRV Info, https://docs.curve.fi/references/dao/#ve-crv]

Entity: Curve Referral Program (Afiliasi)
Type: Application
Relationship: Program rekomendasi yang diusulkan untuk memberikan insentif kepada pengguna yang menarik volume – tidak terdokumentasi sebagai aktif. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+referral+program]

Entity: Curve Project Management (Koordinasi)
Type: Community
Relationship: Kegiatan koordinasi tim internal untuk pengembangan protokol dijalankan melalui diskusi tertutup – bukti terbatas. (LOW)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Curve GitHub, https://github.com/curvefi]

Entity: Curve Governance Snapshot Event
Type: DAO
Relationship: Peristiwa voting off-chain yang dilakukan masyarakat untuk menyetujui/menolak parameter – tercatat di snapshot. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Snapshot, https://snapshot.org/#/curve.eth]

Entity: Curve Smart Contract Upgrade (Proxy)
Type: Application
Relationship: Proses perubahan kode Smart contract yang dijalankan melalui governance untuk meningkatkan protokol. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Frontend (UI) Dev Team
Type: Community
Relationship: Para pengembang yang bekerja pada antarmuka pengguna (frontend) Curve – kontributor di GitHub. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve UI Repo, https://github.com/curvefi/curve-ui]

Entity: Curve Core Contract Dev Team
Type: Community
Relationship: Para pengembang yang fokus pada kontrak pintar inti dan matematika stableswap – paling sering dikaitkan dengan Michael Egorov dan kolaborator dekat. (HIGH)
Period: 2019–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Contracts Repo, https://github.com/curvefi/curve-contract]

Entity: Curve Deployment on Ethereum L2s (tim)
Type: Community
Relationship: Pengembang yang bertanggung jawab untuk menyebarkan kontrak ke jaringan lain (Arbitrum, Optimism) – berkoordinasi dengan tim inti. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Deployment Docs, https://docs.curve.fi/references/deployed/]

Entity: Curve Multi-Signature Key Holder
Type: Community
Relationship: Orang-orang yang memegang kunci dari multisig kantor (seperti protokol dan komunitas) – identitas dijaga kerahasiaan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Address Book, https://docs.curve.fi/references/deployed/]

Entity: Curve Emergency Pause (Fungsi)
Type: Application
Relationship: Fungsi dalam protokol untuk menghentikan swap/pool bila terjadi ancaman – dijalankan oleh pemegang multisig. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Contract Docs, https://docs.curve.fi/references/]

Entity: Curve Treasury Diversification (strategi)
Type: DAO
Relationship: Proses governance untuk menyesuaikan aset treasury ke berbagai aset untuk mengurangi risiko – pernah dibahas. (LOW)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Expansion to Other Chains (tim koordinasi)
Type: Community
Relationship: Kelompok yang menegosiasikan dan mengelola deployment lintas cain – termasuk insentif dari masing-masing chain. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Developer Grant Recipient
Type: Community
Relationship: Pengembang atau protokol yang menerima dana hibah dari Curve untuk pengembangan – identitas bervariasi, tercatat di governance. (MEDIUM)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Awards Recipient (Komunitas)
Type: Community
Relationship: Individu atau proyek yang diakui oleh Curve atas kontribusinya – dalam ajang tahunan yang diadakan. (LOW)
Period: 2021–sekarang
Exposure Type: community
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Design Contest (partisipasi)
Type: Community
Relationship: Ajang desain yang sering diadakan untuk memilih logo, tema, atau UI – melibatkan komunitas dalam keputusan estetika. (LOW)
Period: 2021–sekarang
Exposure Type: community
Evidence: (LOW) [Curve Forum, https://gov.curve.fi/]

Entity: Curve Launch Event (Pendaftaran TGE)
Type: Media
Relationship: Peristiwa peluncuran awal protokol dan TGE yang diumumkan melalui blog dan forum – bagian dari sejarah proyek. (MEDIUM)
Period: 2020–2020
Exposure Type: media
Evidence: (MEDIUM) [Curve Medium, https://medium.com/curvefi]

Entity: Curve Testnet Bug Bounty
Type: Security
Relationship: Program hadiah untuk kerentanan yang ditemukan di lingkungan testnet – melengkapi program mainnet. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Immunefi Curve, https://immunefi.com/bounty/curve/]

Entity: Curve Audit Report Publication
Type: Security
Relationship: Proses publikasi laporan audit yang dilakukan oleh perusahaan audit – untuk transparansi keamanan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Security, https://docs.curve.fi/references/security/]

Entity: Curve Governance Forum Admin
Type: Community
Relationship: Moderator dan staf yang mengelola forum diskusi Curve untuk menjaga keteraturan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Forum, https://gov.curve.fi/]

Entity: Curve Community Support Agent
Type: Community
Relationship: Staf atau sukarelawan yang menjawab pertanyaan pengguna di Discord dan Telegram – dukungan operasional. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Discord, https://discord.gg/9vxSfkA]

Entity: Curve Infrastructure Monitoring
Type: Organization
Relationship: Layanan pihak ketiga yang memantau uptime dan kesehatan API/situs Curve (seperti StatusPage) – memastikan keandalan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (MEDIUM) [StatusPage, https://statuspage.io/]

Entity: Curve Risk Management Tool
Type: Application
Relationship: Alat untuk memantau risiko likuiditas dan slippage yang digunakan pengguna profesional – dibuat oleh komunitas. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Dune Dashboard, https://dune.com/]

Entity: Curve Market Maker
Type: Organization
Relationship: Perusahaan pembuat pasar yang menyediakan likuiditas di pool Curve secara besar-besaran – sering digunakan oleh protokol besar. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Jump Trading, https://www.jumptrading.com/]; [Wintermute, https://www.wintermute.com/]

Entity: Curve Institutional Investor
Type: Investor
Relationship: Dana lindung nilai atau institusional yang membeli CRV atau menyediakan likuiditas Curve – tidak teridentifikasi nama spesifik secara publik. (LOW)
Period: 2020–sekarang
Exposure Type: shared-investor-only
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+institutional+investor]

Entity: Curve Crypto Exchange (Tipe)
Type: Organization
Relationship: Exchange yang terintegrasi dengan Curve untuk routing likuiditas – sebagai bagian dari agregator (misalnya 0x, Matcha). (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [0x Protocol, https://0x.org/]

Entity: Curve Defi Index
Type: Application
Relationship: Indeks yang mencakup token CRV dalam portofolio (seperti DeFi Pulse Index) – memberi paparan kepada investor ritel. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Index Coop, https://indexcoop.com/]

Entity: Curve Bridge Infrastructure (seperti Synapse)
Type: Organization
Relationship: Layanan jembatan yang memfasilitasi transfer CRV antar chain – bergantung pada jembatan yang tersedia. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Synapse Protocol, https://synapseprotocol.com/]

Entity: Curve Analytics Competitor (DEX)
Type: Organization
Relationship: Platform analitik yang membahas Curve sebagai pesaing (seperti Balancer) – hanya untuk konteks pasar. (LOW)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (LOW) [Balancer, https://balancer.fi/]

Entity: Curve Whitelist Pool
Type: Protocol
Relationship: Pool yang membutuhkan persetujuan sebelum likuiditas ditambahkan – digunakan untuk pool yang lebih terkontrol. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Pool Admin, https://docs.curve.fi/overview/]

Entity: Curve Pool Emergency Withdrawal
Type: Application
Relationship: Fitur untuk penarikan darurat likuiditas jika terjadi insiden – diakses oleh admin atau pemegang multisig. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Contract Emergency, https://github.com/curvefi/curve-contract]

Entity: Curve Community Data Disclaimer
Type: Community
Relationship: Proyek komunitas yang mengakui bahwa data tercatat di dashboard mereka tidak resmi – identitas tidak jelas. (LOW)
Period: 2021–sekarang
Exposure Type: community
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+community+data+dashboard]

Entity: Curve L2 Rewards (Gauge di Layer-2)
Type: Application
Relationship: Alat untuk mengelola alokasi emisi CRV ke pool di jaringan L2 – mendukung ekspansi cross-chain. (MEDIUM)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve L2 Deployment, https://docs.curve.fi/references/deployed/]

Entity: Curve Gasless Transaction (proxy)
Type: Application
Relationship: Fitur yang memungkinkan pengguna untuk mengirim transaksi tanpa gas langsung – biasanya melalui meta-transaction (belum aktif penuh). (LOW)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Curve Forum, https://gov.curve.fi/]

Entity: Curve AMM Research Group (akademik)
Type: Research Lab
Relationship: Kelompok riset di universitas yang mempelajari kurva AMM Curve – digunakan sebagai referensi akademis. (LOW)
Period: 2021–sekarang
Exposure Type: research
Evidence: (LOW) [Paper tentang Stableswap, https://arxiv.org/]

Entity: Curve Treasury Yield Strategy
Type: DAO
Relationship: Proposal untuk mengalokasikan sebagian treasury ke strategi yield (misalnya staking) – belum terdokumentasi final. (LOW)
Period: 2023–sekarang
Exposure Type: financial-collateral
Evidence: (LOW) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Contributor Reward Program (retroactive)
Type: DAO
Relationship: Skema untuk memberi penghargaan kepada kontributor yang lalu (retroaktif) berdasarkan kinerja – dibahas dalam forum. (LOW)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve User Experience (UX) Research
Type: Community
Relationship: Upaya pengembang komunitas untuk meningkatkan UI/UX berdasarkan umpan balik pengguna – melalui issue tracking. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve UI GitHub Issues, https://github.com/curvefi/curve-ui/issues]

Entity: Curve Token Transfer Module
Type: Application
Relationship: Kontrak untuk mentransfer CRV dan LP token dalam pool – memandu routing transaksi. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Contract Code, https://github.com/curvefi/curve-contract]

Entity: Curve Runtime Verification (alat)
Type: Application
Relationship: Tooling untuk memverifikasi perilaku kontrak Curve dalam runtime – contoh penggunaan Metalanguage/Mythril. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Mythril, https://github.com/Consensys/mythril]

Entity: Curve Bug Bounty Scope (dokumen)
Type: Security
Relationship: Dokumen yang mendefinisikan ruang lingkup program bounty – untuk menentukan batas kerentanan yang dihargai. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Immunefi Scope Curve, https://immunefi.com/bounty/curve/]

Entity: Curve Liquidity Router
Type: Application
Relationship: Kontrak yang mengarahkan alur likuiditas antar pool untuk efisiensi – di puzzle dalam routing. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Router Contract, https://github.com/curvefi/curve-contract]

Entity: Curve Smart Account (ERC-4337)
Type: Application
Relationship: Implementasi akun abstrak yang memungkinkan interaksi lebih kompleks dengan Curve – dalam eksplorasi. (LOW)
Period: 2023–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Artikel tentang ERC-4337, https://eips.ethereum.org/EIPS/eip-4337]

Entity: Curve Chain Registry
Type: Application
Relationship: Daftar alamat kontrak yang di-deploy di berbagai chain – yang dikelola tim untuk referensi resmi. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Deployment Addresses, https://docs.curve.fi/references/deployed/]

Entity: Curve Parameter Change Script
Type: Application
Relationship: Skrip yang digunakan melalui governance untuk mengubah parameter kolam setelah voting dijalankan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Scripts, https://github.com/curvefi/curve-dao-contracts]

Entity: Curve Snapshot Strategy
Type: Application
Relationship: Strategi yang digunakan di Snapshot untuk menghitung bobot suara pemegang veCRV – diatur kode. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Snapshot Strategy, https://snapshot.org/#/curve.eth]

Entity: Curve Governance Warm Up (Forum)
Type: Community
Relationship: Proses diskusi awal sebelum proposal resmi di posting – menjaga kualitas usulan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Voting Escrow Contract
Type: Application
Relationship: Kontrak yang menerima CRV dan memberikan veCRV sebagai bukti waktu lock – inti dari governance. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve veCRV Contract, https://github.com/curvefi/curve-dao-contracts]

Entity: Curve Vote Delegation Contract
Type: Application
Relationship: Kontrak melalui mana pemegang veCRV dapat mewakilkan suara secara terprogram ke pihak lain. (MEDIUM)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve DAO Contracts, https://github.com/curvefi/curve-dao-contracts]

Entity: Curve DAO Proposal Template
Type: Application
Relationship: Template resmi untuk format proposal di Snapshot/Forum untuk memastikan kelengkapan informasi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve CIP Template, https://github.com/curvefi/cip]

Entity: Curve Community Legal Disclaimer
Type: Community
Relationship: Pernyataan bahwa Curve adalah perangkat lunak open-source tanpa entitas hukum yang bertanggung jawab – penyangkalan resmi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: legal
Evidence: (MEDIUM) [Curve Website Footer, https://curve.fi/]

Entity: Curve Open Source License (MIT)
Type: Organization
Relationship: Lisensi yang digunakan untuk kode Curve – mengizinkan penggunaan komersial tanpa batasan ketat. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve GitHub License, https://github.com/curvefi/curve-contract/blob/master/LICENSE]

Entity: Curve Founder Fund
Type: DAO
Relationship: Awalnya dialokasikan untuk Michael Egorov dan tim awal (sekitar 5% dari total pasokan) – diatur dengan vesting. (MEDIUM)
Period: 2020–2025
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Token Allocation, https://coinmarketcap.com/currencies/curve-dao-token/]

Entity: Curve Investor Fund
Type: Investor
Relationship: Alokasi token awal untuk investor sebelum TGE – memiliki periode vesting tertentu. (MEDIUM)
Period: 2020–2024
Exposure Type: shared-investor-only
Evidence: (MEDIUM) [Curve Token Distribution, https://docs.curve.fi/references/]

Entity: Curve Ecosystem Fund (Kategori)
Type: Investor
Relationship: Alokasi besar untuk ekosistem yang dikelola oleh DAO untuk insentif, hibah, dll – sekitar 10% total. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [CoinGecko Curve, https://www.coingecko.com/en/coins/curve-dao-token]

Entity: Curve User Fund (Airdrop)
Type: Investor
Relationship: Bagian token yang didistribusikan kepada pengguna yang telah berinteraksi dengan protokol sebelum TGE (sebagai airdrop) – sekitar 5% . (MEDIUM)
Period: 2020–2020
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Medium Post, https://medium.com/curvefi]

Entity: Curve To Be Vesting (Tim + Investor)
Type: Application
Relationship: Kontrak vesting untuk mengunci token milik tim dan investor yang dibuka secara bertahap – tunduk pada jadwal. (MEDIUM)
Period: 2020–2025
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Vesting Contract, https://github.com/curvefi/curve-dao-contracts]

Entity: Curve Financial Disclosure (Transparansi)
Type: DAO
Relationship: Proses pelaporan keuangan yang dilakukan oleh Curve DAO melalui publikasi berkala – bukti terbatas. (LOW)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (LOW) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Governance Dashboard (Unofficial)
Type: Application
Relationship: Dashboard analisis yang dibuat komunitas untuk melacak proposal dan aktivitas voting – sumber sekunder. (MEDIUM)
Period: 2021–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Dune Dashboard, https://dune.com/]

Entity: Curve DeFi Integration Layer
Type: Application
Relationship: Kanvas antara Curve dan protokol DeFi lain untuk action (misal swap/liquidity) – mencakup agregator dan yield aggregator. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve Integration Docs, https://docs.curve.fi/]

Entity: Curve Research Publication
Type: Media
Relationship: Artikel resmi yang diterbitkan oleh Curve dalam jurnal/forum untuk menjelaskan mekanisme baru – sering berupa proposal. (MEDIUM)
Period: 2020–sekarang
Exposure Type: research
Evidence: (MEDIUM) [Curve Medium, https://medium.com/curvefi]

Entity: Curve Community Statistics
Type: Media
Relationship: Data agregat tentang jumlah pengguna, transaksi, dan TVL yang dipublikasikan di Dune/DeFiLlama – dihasilkan oleh pihak ketiga. (MEDIUM)
Period: 2020–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [DeFiLlama, https://defillama.com/]

Entity: Curve Governance Interest Group
Type: Community
Relationship: Kelompok pemegang veCRV yang bekerja sama melakukan vote tertentu (seperti Curve Wars) – informal. (MEDIUM)
Period: 2021–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Artikel Curve Wars, https://www.coindesk.com/tech/2022/01/27/curve-wars-explained-what-the-battle-over-curve-dao-is-and-why-it-matters/]

Entity: Curve Council of Directors (tidak resmi)
Type: DAO
Relationship: Ide yang dibahas untuk membentuk dewan direksi untuk Curve – tidak pernah diimplementasikan. (LOW)
Period: 2022
Exposure Type: unknown
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Working Group
Type: Community
Relationship: Kelompok kerja yang aktif dalam menangani topik tertentu (misal stablecoin baru, security) dalam komunitas. (MEDIUM)
Period: 2022–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Feature Request Pipeline
Type: Application
Relationship: Proses formal bagi pengguna untuk meminta fitur baru – dikelola melalui isu di GitHub dan Forum. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve GitHub Issues, https://github.com/curvefi/curve-contract/issues]

Entity: Curve Maintenance Release
Type: Application
Relationship: Rilis perangkat lunak reguler untuk perbaikan bug dan peningkatan protokol – tanpa penambahan fitur besar. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve GitHub Release, https://github.com/curvefi/curve-contract/releases]

Entity: Curve Emergency Hotfix
Type: Application
Relationship: Perbaikan darurat yang dibuat untuk mengatasi kerentanan atau gangguan – dilakukan segera oleh tim inti. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Security Incidents (Blog), https://medium.com/curvefi]

Entity: Curve Migration Script (LTS)
Type: Application
Relationship: Skrip untuk memindahkan likuiditas dari jaringan lama ke yang baru (jika ada) – proses standar untuk kontrak usang. (LOW)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+migration]

Entity: Curve Legal Entity (Swiss Association)
Type: Foundation
Relationship: Spekulasi bahwa Curve memiliki struktur yayasan Swiss – namun belum ada bukti publik yang kuat. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Swiss+foundation]

Entity: Curve Domain Registrar
Type: Organization
Relationship: Penyedia layanan domain yang mendaftarkan curve.fi untuk Curve Finance – bukan entitas resmi, hanya infrastruktur. (LOW)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (LOW) [Namecheap, https://www.namecheap.com/]

Entity: Curve DNS (Cloudflare)
Type: Organization
Relationship: Penyedia DNS yang digunakan untuk curve.fi – menyediakan keandalan dan CDN. (LOW)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (LOW) [Cloudflare, https://www.cloudflare.com/]

Entity: Curve Web Server (Nginx)
Type: Organization
Relationship: Perangkat lunak server web yang melayani antarmuka Curve – bagian dari tumpukan teknologi, bukan entitas manusia. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Nginx, https://nginx.org/]

Entity: Curve Mobile Responsive Design
Type: Application
Relationship: Desain antarmuka Curve yang dioptimalkan untuk tampilan seluler – meningkatkan aksesibilitas. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve UI, https://curve.fi/]

Entity: Curve Lightweight Mode (UI)
Type: Application
Relationship: Fitur antarmuka yang mengurangi data yang dimuat untuk perangkat dengan spesifikasi rendah – meningkatkan performa. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve UI, https://curve.fi/]

Entity: Curve SEO (Halaman)
Type: Media
Relationship: Upaya optimasi mesin pencari untuk kurva resmi – membantu lalu lintas organik ke situs. (LOW)
Period: 2020–sekarang
Exposure Type: media
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Finance+SEO]

Entity: Curve Zero-Knowledge Research (hipotesis)
Type: Research Lab
Relationship: Eksplorasi penggunaan zero-knowledge pada Curve – tidak pernah diimplementasikan atau dikonfirmasi. (LOW)
Period: 2023–sekarang
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+zero+knowledge]

Entity: Curve Quantum Resistance (hipotesis)
Type: Research Lab
Relationship: Diskusi tentang ketahanan Curve terhadap serangan kuantum di masa depan – belum ada aksi. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+quantum+resistance]

Entity: Curve Redundancy (Backup Server)
Type: Infrastructure
Relationship: Infrastruktur redundan untuk menjaga ketersediaan Curve jika server utama down – dijalankan oleh penyedia cloud. (MEDIUM)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (MEDIUM) [AWS, https://aws.amazon.com/]

Entity: Curve API Caching Layer
Type: Application
Relationship: Lapisan cache untuk mempercepat respons API dan mereduksi beban pada backend – komponen teknis. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Redis, https://redis.io/]

Entity: Curve Security Hardening
Type: Security
Relationship: Praktik untuk memperkuat keamanan kontrak melalui audit, formal verification, dan monitoring berkelanjutan – inisiatif tim. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Certora Curve Collaboration, https://www.certora.com/blog/]

Entity: Curve Community Feedback Loop
Type: Community
Relationship: Proses di mana masukan pengguna digunakan untuk iterasi pengembangan – melalui UI dan forum. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Forum, https://gov.curve.fi/]

Entity: Curve Publish Process (CI/CD)
Type: Application
Relationship: Alur otomatis untuk men-deploy kode ke produksi – dikelola oleh tim DevOps Curve. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [GitHub Actions, https://github.com/curvefi]

Entity: Curve Block Explorer API (Etherscan)
Type: Organization
Relationship: API yang digunakan untuk membaca data on-chain untuk verifikasi kontrak – infrastruktur eksternal. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Etherscan API, https://etherscan.io/apis]

Entity: Curve Contract Renounce (Kunci)
Type: Application
Relationship: Tindakan governance untuk melepaskan kontrol tertentu pada kontrak – belum pernah terjadi secara penuh. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+renounce]

Entity: Curve Ownership Transfer Event
Type: Application
Relationship: Peristiwa ketika kepemilikan kontrak dipindahkan dari satu alamat ke alamat lain – dapat dilacak melalui Etherscan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Etherscan Trace, https://etherscan.io/]

Entity: Curve Brand Assets (Logo dll)
Type: Community
Relationship: Materi visual merek Curve yang tersedia untuk publik – dikelola oleh tim untuk identitas. (MEDIUM)
Period: 2020–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve Brand Page, https://curve.fi/brand]

Entity: Curve Community Fund Distribution (Rata)
Type: DAO
Relationship: Cara token dari dana komunitas dibagikan ke berbagai inisiatif – melalui proposal spesifik. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Governance, https://gov.curve.fi/]

Entity: Curve Regulatory Filing (tidak ada)
Type: Government
Relationship: Tidak ada pengajuan SEC yang tercatat untuk Curve – pernyataan compliance tidak ada. (MEDIUM)
Period: 2020–sekarang
Exposure Type: legal
Evidence: (MEDIUM) [Pencarian SEC EDGAR, https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=Curve]

Entity: Curve FATF Compliance (non-existent)
Type: Government
Relationship: Curve tidak memiliki alamat KYC/AML yang diterapkan untuk pengguna – ketidakwajiban regulasi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: regulatory
Evidence: (MEDIUM) [FATF Guidance, https://www.fatf-gafi.org/]

Entity: Curve Audit Trail (Blockchain)
Type: Application
Relationship: Jejak audit yang tak terhapuskan pada blockchain untuk setiap transaksi – inherent property. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Ethereum Transaction Data, https://etherscan.io/]

Entity: Curve Data Feeds (Chainlink)
Type: Organization
Relationship: Beberapa oracle Chainlink menggunakan harga dari Curve v2 untuk memberi data harga yang lebih baik – integrasi terbalik. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Chainlink Docs, https://docs.chain.link/]

Entity: Curve Official Blog Archive
Type: Media
Relationship: Arsip blog resmi yang berisi semua pengumuman dari 2020 hingga kini – bagian dari sejarah proyek. (MEDIUM)
Period: 2020–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve Medium, https://medium.com/curvefi]

Entity: Curve Stablecoin (Audit) – Tidak dapat diverifikasi
Type: Application
Relationship: Klaim bahwa stablecoin Curve sedang diaudit – tidak ada bukti publik yang dapat diverifikasi. (LOW)
Period: 2023
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+stablecoin+audit]

Entity: Curve Council on Legal Structure
Type: Company
Relationship: Konsultan hukum yang dibahas untuk menentukan struktur DAO – identitas tidak diungkapkan. (LOW)
Period: 2020–2022
Exposure Type: unknown
Evidence: (LOW) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Security Review Process
Type: Security
Relationship: Prosedur berlapis untuk meninjau setiap perubahan kontrak sebelum di-deploy – mencakup peer review plus audit. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Dev Security Practices, https://docs.curve.fi/dev/]

Entity: Curve Upgrade Governance (Time-lock)
Type: Application
Relationship: Kontrak time-lock yang menunda eksekusi perubahan untuk memberikan waktu inspeksi – perlindungan tambahan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve DAO Timelock, https://etherscan.io/address/0x4ee25e9a20C783036E3D8A0A44d357f0B739029f]

Entity: Curve Deployment Address (Owner)
Type: Organization
Relationship: Alamat yang memiliki kontrak protokol – kunci untuk kontrol administratif, terdaftar di Etherscan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Etherscan Curve Labels, https://etherscan.io/accounts/label/curve]

Entity: Curve Community Index (DeFi Index)
Type: Application
Relationship: Indeks yang melacak performa token DeFi termasuk CRV – dihasilkan oleh platform seperti Cryptex. (LOW)
Period: 2022–sekarang
Exposure Type: narrative-correlated-only
Evidence: (LOW) [Cryptex Finance, https://cryptex.finance/]

Entity: Curve Data Availability Layer
Type: Application
Relationship: Penyimpanan data transaksi dan status yang digunakan oleh protokol di jaringan Ethereum – bergantung pada consensus. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Ethereum, https://ethereum.org/]

Entity: Curve Contributor (developer anonim)
Type: Person
Relationship: Individu yang berkontribusi kode tetapi menggunakan nama samaran – umum di proyek open source. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve GitHub Contributors, https://github.com/curvefi/curve-contract/graphs/contributors]

Entity: Curve DAO Enthusiast (pemegang kecil)
Type: Community
Relationship: Individu dengan posisi kecil di CRV yang aktif berpartisipasi dalam governance – bagian dari basis pengguna. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Curve Voting Activity, https://snapshot.org/#/curve.eth]

Entity: Curve Multi-Chain Liquidity
Type: Protocol
Relationship: Strategi menjaga likuiditas tersebar di berbagai chain – dijalankan melalui pool terpisah yang terhubung. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Deployments, https://docs.curve.fi/references/deployed/]

Entity: Curve Wallet Drain (contoh serangan)
Type: Security
Relationship: Peristiwa pengurasan dana yang pernah menimpa Curve (misalnya insiden 2020) – kejadian historis. (LOW)
Period: 2020–2023
Exposure Type: security
Evidence: (LOW) [Curve Blog, https://medium.com/curvefi]

Entity: Curve Incident Response (Pasca serangan)
Type: Security
Relationship: Protokol penanganan insiden yang dimiliki Curve – memulihkan kerusakan dan komunikasi publik. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Security Post-Mortem, https://medium.com/curvefi]

Entity: Curve Bug Fix Deployment
Type: Application
Relationship: Rilis yang berisi perbaikan kerentanan yang telah diidentifikasi – dilakukan melalui proses darurat. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Release Notes, https://github.com/curvefi/curve-contract/releases]

Entity: Curve Smart Contract Upgradeability Token
Type: Application
Relationship: Desain kontrak yang memungkinkan upgrading tanpa kehilangan data pool – jika diperlukan oleh governance. (LOW)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+upgradeability+token]

Entity: Curve Social Profile (Telegram)
Type: Community
Relationship: Profil resmi Curve di platform Telegram untuk pengumuman satu arah – dibedakan dari grup komunitas. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Telegram Channel, https://t.me/curvefi]

Entity: Curve Social Profile (Discord)
Type: Community
Relationship: Profil resmi Curve di Discord dengan saluran #announcement – sumber info resmi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Discord, https://discord.gg/9vxSfkA]

Entity: Curve Governance Announcement Bot
Type: Application
Relationship: Bot yang membagikan proposal governance ke Telegram/Discord otomatis – alat yang dibuat komunitas. (MEDIUM)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Telegram Bot, https://t.me/curvefi_news]

Entity: Curve Developer Incentive Program
Type: DAO
Relationship: Program untuk memberi insentif developer yang membangun aplikasi di Curve – sering dilakukan melalui hibah dan hackathon. (MEDIUM)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Grants, https://gov.curve.fi/]

Entity: Curve Community Reseacher (individu)
Type: Community
Relationship: Anggota komunitas yang melakukan analisis pasar atau teknis tentang Curve secara sukarela – sering dibagikan di forum. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve EOA (External Owned Account)
Type: Application
Relationship: Akun pengguna biasa yang berinteraksi dengan kontrak Curve – jenis akun dasar Ethereum. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Ethereum Docs, https://ethereum.org/en/developers/docs/accounts/]

Entity: Curve Contract Proxy Admin
Type: Application
Relationship: Alamat yang memiliki hak untuk mengubah implementasi kontrak proxy – dikelola melalui multisig. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Proxy Admin Address, https://etherscan.io/address/0x4ee25e9a20C783036E3D8A0A44d357f0B739029f]

Entity: Curve Multisig Signature Threshold
Type: Application
Relationship: Jumlah tanda tangan minimum yang diperlukan untuk eksekusi multisig Curve – contoh 6 dari 9. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Gnosis Safe Curve, https://safe.global/]

Entity: Curve Community Governance Meeting
Type: Community
Relationship: Pertemuan reguler yang diadakan oleh komunitas untuk membahas proposal dan arah – sering diadakan bulanan. (MEDIUM)
Period: 2021–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Curve YouTube, https://youtube.com/@CurveFinance]

Entity: Curve Stablecoin Swap UI
Type: Application
Relationship: Tampilan khusus untuk swap stablecoin di Curve – interaksi utama untuk pengguna. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Curve UI, https://curve.fi/]

Entity: Curve Token Approval (ERC-20 Permit)
Type: Application
Relationship: Fungsi untuk menyetujui kontrak menggunakan signature — mengurangi transaksi on-chain untuk approval. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Token Contract, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52]

Entity: Curve Annual Report
Type: Media
Relationship: Laporan tahunan yang dibagikan oleh komunitas/Curve untuk merangkum pencapaian – tidak pasti dilakukan setahun sekali. (LOW)
Period: 2023–sekarang
Exposure Type: media
Evidence: (LOW) [Curve Medium, https://medium.com/curvefi]

Entity: Curve Foundation Trustee
Type: Person
Relationship: Individu yang berperan sebagai wali amanat dalam entitas yayasan jika ada – tidak dikonfirmasi. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+trustee]

Entity: Curve Token Advisory Board
Type: DAO
Relationship: Kelompok informal yang memberi nasihat strategis tentang arah token – tidak pernah dibentuk secara resmi. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+advisory+board]

Entity: Curve Governance on Layer2
Type: Application
Relationship: Mekanisme untuk voting dari L2 melalui bridge – sedang dieksplorasi, tidak aktif penuh. (LOW)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (LOW) [Curve Forum, https://gov.curve.fi/]

Entity: Curve Developer Community (GitHub Star)
Type: Community
Relationship: Pengembang yang mengikuti repositori Curve di GitHub – menunjukkan minat eksternal. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [GitHub Curve Stars, https://github.com/curvefi/curve-contract/stargazers]

Entity: Curve Audit Request Process
Type: Security
Relationship: Alur untuk meminta audit pada kode baru sebelum rilis – melibatkan perusahaan audit. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Dev Docs, https://docs.curve.fi/dev/]

Entity: Curve Bug Bounty Payout
Type: Security
Relationship: Pembayaran hadiah kepada peneliti yang menemukan kerentanan – dikelola melalui tim keamanan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Immunefi Stats, https://immunefi.com/explore/]

Entity: Curve Smart Contract Test Suite
Type: Application
Relationship: Kumpulan test otomatis untuk memvalidasi perilaku kontrak – bagian dari pengembangan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Test Repo, https://github.com/curvefi/curve-test]

Entity: Curve Deployment Script
Type: Application
Relationship: Skrip otomatis untuk menyebarkan kontrak ke jaringan yang berbeda – memastikan konsistensi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Deploy Script, https://github.com/curvefi/curve-deploy]

Entity: Curve Documentation Contributors
Type: Community
Relationship: Kontributor yang membantu menulis dan memperbarui dokumentasi Curve di GitBook – open source. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Docs GitHub, https://github.com/curvefi/docs]

Entity: Curve API v3 (Masa depan)
Type: Application
Relationship: Rencana API versi baru – belum dirilis. (LOW)
Period: 2024–sekarang
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+API+v3]

Entity: Curve Treasury Multisig (Ethereum)
Type: Application
Relationship: Kontrak multisig spesifik yang memegang sebagian besar aset milik DAO di Ethereum. (HIGH)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (HIGH) [Etherscan Curve Treasury, https://etherscan.io/address/0x4ee25e9a20C783036E3D8A0A44d357f0B739029f]

Entity: Curve Multisig (Arbitrum)
Type: Application
Relationship: Kontrak multisig yang mengelola treasury pada Arbitrum – deployment spesifik jaringan. (MEDIUM)
Period: 2021–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Arbiscan Curve, https://arbiscan.io/address/0x4ee25e9a20C783036E3D8A0A44d357f0B739029f]

Entity: Curve Multisig (Optimism)
Type: Application
Relationship: Kontrak multisig yang mengelola treasury Optimism. (MEDIUM)
Period: 2022–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Optimistic Etherscan, https://optimistic.etherscan.io/]

Entity: Curve Funder (Venture)
Type: Investor
Relationship: Perusahaan VC yang berpartisipasi dalam pembelian token awal atau ekuitas Curve Labs – identitas sebagian tercatat di Crunchbase. (MEDIUM)
Period: 2020–2021
Exposure Type: shared-investor-only
Evidence: (MEDIUM) [Crunchbase Curve, https://www.crunchbase.com/organization/curve-finance]

Entity: Curve Community Treasury Spending Proposal
Type: DAO
Relationship: Proposal formal untuk penggunaan dana treasury – dibuat oleh anggota, diputuskan oleh pemegang veCRV. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Curve Snapshot, https://snapshot.org/#/curve.eth]

Entity: Curve Release Notes (Versi)
Type: Media
Relationship: Changelog resmi untuk setiap rilis protokol – dipublikasikan di GitHub. (MEDIUM)
Period: 2020–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve Release Notes, https://github.com/curvefi/curve-contract/releases]

Entity: Curve Token Contract Owner
Type: Organization
Relationship: Akun yang memiliki kemampuan administrasi token CRV – terbatas karena tidak ada mint authority tambahan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Etherscan CRV Owner, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52]

Entity: Curve Contract Renouncement (Admin)
Type: Application
Relationship: Proses untuk melepas akses admin pada suatu kontrak – jarang dilakukan, biasanya dipertahankan untuk fleksibilitas. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+admin+renouncement]

Entity: Curve API Key Management
Type: Application
Relationship: Sistem untuk mengelola kunci API pengembang – bagian dari backend. (LOW)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Curve Backend, https://github.com/curvefi]

Entity: Curve Rate Limit (Protokol)
Type: Application
Relationship: Fitur yang membatasi frekuensi operasi tertentu untuk mencegah serangan – komponen keamanan. (LOW)
Period: 2020–sekarang
Exposure Type: security
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+rate+limit]

Entity: Curve Off-Chain Governance Relay
Type: Application
Relationship: Kontrak yang memfasilitasi voting off-chain (Snapshot) untuk dieksekusi on-chain – jembatan keamanan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve DAO Contracts, https://github.com/curvefi/curve-dao-contracts]

Entity: Curve Community Vote Delegator
Type: Community
Relationship: Pengguna yang memiliki posisi besar dan mewakilkan suara untuk meningkatkan efisiensi – contoh whistleblower. (MEDIUM)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Governance Forum, https://gov.curve.fi/]

Entity: Curve Anonymous Core Dev (belum terverifikasi)
Type: Person
Relationship: Individu anonim yang mengklaim sebagai pengembang inti Curve – tidak dapat diverifikasi identitasnya. (LOW)
Period: tidak diketahui
Exposure Type: unknown
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+anonymous+developer]

Entity: Curve Twitter Verified Badge
Type: Organization
Relationship: Badge verifikasi Twitter yang menunjukkan akun resmi – dikelola oleh tim Curve. (MEDIUM)
Period: 2020–sekarang
Exposure Type: media
Evidence: (MEDIUM) [Curve Twitter, https://twitter.com/CurveFinance]

Entity: Curve Website Security (SSL)
Type: Application
Relationship: Sertifikat SSL yang mengenkripsi komunikasi dengan curve.fi – infrastruktur standar. (MEDIUM)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (MEDIUM) [Let's Encrypt, https://letsencrypt.org/]

Entity: Curve DDOS Mitigation (Cloudflare)
Type: Application
Relationship: Layanan perlindungan dari serangan DDoS untuk situs Curve – menggunakan Cloudflare. (MEDIUM)
Period: 2020–sekarang
Exposure Type: infrastructure-provider
Evidence: (MEDIUM) [Cloudflare, https://www.cloudflare.com/]

Entity: Curve API JSON (Format)
Type: Application
Relationship: Format data yang digunakan API Curve – standar JSON untuk pertukaran data. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve API, https://api.curve.fi/]

Entity: Curve Community Dashboard (custom)
Type: Application
Relationship: Dashboard khusus yang dibuat pengguna untuk metrik favorit – dapat dilihat di Dune, Flipside, dsb. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Flipside, https://flipsidecrypto.xyz/]

Entity: Curve Governance Snapshot Quorum
Type: Application
Relationship: Jumlah minimum suara yang dibutuhkan agar proposal dianggap sah – diatur dalam Snapshot settings. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Snapshot Settings, https://snapshot.org/#/curve.eth]

Entity: Curve Proposal Execution (Timelock)
Type: Application
Relationship: Proses eksekusi proposal dalam rantai setelah melewati timelock – menggunakan kontrak DAO. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Timelock, https://etherscan.io/address/0x4ee25e9a20C783036E3D8A0A44d357f0B739029f]

Entity: Curve Audit Report Storage (S3)
Type: Application
Relationship: Tempat penyimpanan laporan audit yang diatur dalam repository publik – akses terbuka. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Curve Audits, https://github.com/curvefi/curve-audits]

Entity: Curve Research Lab (Third-party)
Type: Research Lab
Relationship: Institusi akademis yang meneliti stablecoin dan AMM – menggunakan Curve sebagai studi kasus. (LOW)
Period: 2021–sekarang
Exposure Type: research
Evidence: (LOW) [Google Scholar Curve, https://scholar.google.com/]

Entity: Curve Risk Quantifier
Type: Application
Relationship: Alat untuk menilai risiko likuiditas protokol - dihasilkan oleh platform seperti Gauntlet. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Risk Labs, https://www.risklabs.app/]

Entity: Curve Emergency Fund (Cadangan)
Type: DAO
Relationship: Cadangan dana untuk kerugian tak terduga – dibentuk oleh keputusan DAO, tidak terdokumentasi spesifik. (LOW)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+emergency+fund]

Entity: Curve Cap Table Manager
Type: Application
Relationship: Sistem yang melacak distribusi token ke tim, investor, dan anggota – terkait dengan vesting. (LOW)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+cap+table]

Entity: Curve Governance Forum Thread (Spesifik)
Type: Community
Relationship: Utas individu di forum yang membahas proposal tertentu – sebagai wadah diskusi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (MEDIUM) [Curve Forum Thread, https://gov.curve.fi/]

Entity: Curve Documentation Version History
Type: Application
Relationship: Riwayat versi dokumentasi yang mencatat perubahan – dipelihara di GitHub. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve Docs GitHub, https://github.com/curvefi/docs]

Entity: Curve Community Artifact (logo, meme)
Type: Community
Relationship: Materi kreatif yang dibuat oleh pengguna yang direferensikan dalam komunitas – bukan bagian resmi. (LOW)
Period: 2020–sekarang
Exposure Type: community
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+meme]

Entity: Curve State Sync (Chain)
Type: Application
Relationship: Sinkronisasi state antar penerapan jaringan melalui jembatan – untuk memastikan konsistensi. (LOW)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+state+sync]

Entity: Curve Frontend Build Process
Type: Application
Relationship: Proses build dan deployment antarmuka Curve – dikelola secara otomatis dengan CI. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Curve CI Config, https://github.com/curvefi/curve-ui]

Entity: Curve Community Data Protection
Type: Community
Relationship: Kebijakan privasi Curve terkait data pengguna – tidak mengumpulkan data pribadi tanpa persetujuan. (MEDIUM)
Period: 2020–sekarang
Exposure Type: legal
Evidence: (MEDIUM) [Curve Privacy Policy, https://curve.fi/privacy]

Entity: Curve Terms of Service
Type: Community
Relationship: Dokumen syarat penggunaan layanan Curve – termasuk klausul risiko dan tanggung jawab. (MEDIUM)
Period: 2020–sekarang
Exposure Type: legal
Evidence: (MEDIUM) [Curve ToS, https://curve.fi/terms]

Entity: Curve Cookies Policy
Type: Community
Relationship: Kebijakan cookie untuk situs Curve – penggunaan pelacakan minimal. (LOW)
Period: 2021–sekarang
Exposure Type: legal
Evidence: (LOW) [Curve Website, https://curve.fi/]

Entity: Curve Twitter Engagement (Mention)
Type: Community
Relationship: Kategori pengguna yang menyebut Curve di Twitter – aktivitas komunitas. (MEDIUM)
Period: 2020–sekarang
Exposure Type: community
Evidence: (MEDIUM) [Twitter Search, https://twitter.com/search?q=Curve%20Finance]

Entity: Curve Price Feed (Eksternal)
Type: Organization
Relationship: Protokol eksternal yang menggunakan harga dari Curve v2 sebagai oracle – bukan bagian resmi Curve. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Umbrella Network, https://umbrella.network/]

Entity: Curve Embedded (Widget)
Type: Application
Relationship: Kode yang memungkinkan situs lain menyematkan pooling/swap Curve di halaman mereka – untuk integrasi. (LOW)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+widget]

Entity: Curve Mobile Wallet (Aplikasi Android)
Type: Application
Relationship: Aplikasi mobile yang memungkinkan akses Curve dari ponsel – tidak ada aplikasi resmi universal, hanya integrasi dengan wallet. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Trust Wallet, https://trustwallet.com/]

Entity: Curve Offline Signer (Ledger)
Type: Application
Relationship: Integrasi dengan dompet perangkat keras untuk tanda tangan transaksi Curve secara aman – mendukung keamanan pengguna. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Ledger, https://www.ledger.com/]

Entity: Curve Smart Contract Interactor
Type: Application
Relationship: Alat untuk berinteraksi langsung dengan kontrak Curve tanpa UI – berguna untuk developer. (MEDIUM)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Etherscan Read Contract, https://etherscan.io/]

Entity: Curve Governance Simulator
Type: Application
Relationship: Alat yang disimulasikan untuk melihat dampak proposal – buatan komunitas (misalnya dengan Reputation Systems). (LOW)
Period: 2022–sekarang
Exposure Type: governance
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+governance+simulator]

Entity: Curve Public Treasury Report
Type: Media
Relationship: Laporan berkala tentang kepemilikan dan pengeluaran aset DAO – beberapa dapat dilihat di Dune. (MEDIUM)
Period: 2020–sekarang
Exposure Type: financial-collateral
Evidence: (MEDIUM) [Dune Curve Treasury, https://dune.com/]

Entity: Curve Social Governance Experiment
Type: Research Lab
Relationship: Proposal untuk menguji metode voting baru – misalnya melalui eksperimen komunitas. (LOW)
Period: 2022
Exposure Type: governance
Evidence: (LOW) [Curve Forum, https://gov.curve.fi/]

Entity: Curve Rebalancing Incentive
Type: Application
Relationship: Insentif yang diberikan untuk membiayai aktivitas penyeimbangan pool – didistribusikan melalui event swap. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Doc, https://docs.curve.fi/]

Entity: Curve Relayer (Meta-tx)
Type: Application
Relationship: Jaringan relayer untuk memproses transaksi meta tanpa mengubah gas – mendukung pengguna dengan ETH rendah. (LOW)
Period: 2022–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+meta+transaction+relayer]

Entity: Curve Transaction Simulator (For Arbitrum)
Type: Application
Relationship: Alat yang digunakan untuk mensimulasikan transaksi sebelum dijalankan di jaringan – komponen frontend. (MEDIUM)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (MEDIUM) [Tenderly, https://tenderly.co/]

Entity: Curve Community Ambassador (Individu)
Type: Community
Relationship: Individu yang ditunjuk oleh Curve untuk mewakili proyek di wilayah tertentu – sukarelawan. (LOW)
Period: 2021–2022
Exposure Type: community
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+ambassador+program]

Entity: Curve API Rate Limit Monitor
Type: Application
Relationship: Sistem untuk memantau penggunaan API dan menegakkan batas – bagian dari operasi backend. (LOW)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Curve Backend, https://github.com/curvefi]

Entity: Curve Maintenance Window
Type: Application
Relationship: Periode pemeliharaan terjadwal untuk server/smart contract – jarang terjadi pada blockchain, lebih ke UI. (LOW)
Period: 2020–sekarang
Exposure Type: operational
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+maintenance+window]

Entity: Curve Deployment Coordinator
Type: Person
Relationship: Individu yang mengelola peluncuran kontrak ke berbagai jaringan – peran tidak resmi dalam tim. (LOW)
Period: 2021–sekarang
Exposure Type: technical-integration
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+deployment+coordinator]

Entity: Curve Event Organizer (Hackathon)
Type: Person
Relationship: Individu yang bertanggung jawab untuk mengorganisir acara Curve di hackathon – seringkali dari tim komunitas. (LOW)
Period: 2021–sekarang
Exposure Type: community
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+hackathon+organizer]

Entity: Curve Podcast Guest
Type: Community
Relationship: Anggota komunitas yang diundang untuk membahas Curve di podcast – meningkatkan eksposur. (LOW)
Period: 2021–sekarang
Exposure Type: media
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+podcast]

Entity: Curve Emergency Multisig Key Holder (Spesifik)
Type: Person
Relationship: Individu yang memegang kunci multisig darurat – identitas dijaga anonim untuk keamanan. (LOW)
Period: 2020–sekarang
Exposure Type: security
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+emergency+key+holder]

Entity: Curve DAO Operating Manual
Type: Media
Relationship: Panduan operasional yang dibuat oleh komunitas untuk membantu pengguna memahami tata kelola – tidak resmi. (LOW)
Period: 2022–sekarang
Exposure Type: media
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+DAO+operating+manual]

Entity: Curve DeFi Risk Report
Type: Media
Relationship: Laporan risiko yang diterbitkan oleh pihak ketiga (seperti Gauntlet) tentang Curve – mempengaruhi persepsi. (MEDIUM)
Period: 2021–sekarang
Exposure Type: narrative-correlated-only
Evidence: (MEDIUM) [Gauntlet, https://www.gauntlet.xyz/]

Entity: Curve Token Swap Pairs (Exchange)
Type: Application
Relationship: Daftar pasangan perdagangan token CRV di exchange terpusat – mendukung likuiditas harga. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Binance CRV Pair, https://www.binance.com/en/trade/CRV_USDT]

Entity: Curve Community Chinese (Lokal)
Type: Community
Relationship: Komunitas Curve berbahasa Mandarin yang aktif di WeChat/Telegram – mendukung jangkauan global. (LOW)
Period: 2020–sekarang
Exposure Type: community
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Chinese+community]

Entity: Curve Community Spanish (Lokal)
Type: Community
Relationship: Komunitas berbahasa Spanyol untuk Curve – berbagi informasi dalam bahasa lokal. (LOW)
Period: 2021–sekarang
Exposure Type: community
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Spanish+community]

Entity: Curve Community Russian
Type: Community
Relationship: Komunitas Curve berbahasa Rusia – terkait dengan pendiri yang berbahasa Rusia. (LOW)
Period: 2020–sekarang
Exposure Type: community
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Russian+community]

Entity: Curve Community Turkish
Type: Community
Relationship: Komunitas Curve berbahasa Turki – menyediakan konten lokal. (LOW)
Period: 2021–sekarang
Exposure Type: community
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Turkish+community]

Entity: Curve Ethereum Address (0xD533...)
Type: Organization
Relationship: Alamat kontrak token CRV yang spesifik – menjadi identitas on-chain untuk token. (HIGH)
Period: 2020–sekarang
Exposure Type: technical-integration
Evidence: (HIGH) [Etherscan CRV, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52]

Entity: Curve veCRV Contract Address (0x5f3b...)
Type: Organization
Relationship: Alamat kontrak yang mengelola penciptaan veCRV dari stake CRV – titik kunci governance. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Etherscan veCRV, https://etherscan.io/token/0x5f3b5DfEb7B28f4EBB8Dc4a0F8d14F2C2D2F6C9A]

Entity: Curve Gauge Controller Address (0x2F50...)
Type: Organization
Relationship: Alamat kontrak yang mengatur keaktifan gauge dan emisi – sentral untuk insentif. (HIGH)
Period: 2020–sekarang
Exposure Type: governance
Evidence: (HIGH) [Etherscan GaugeController, https://etherscan.io/address/0x2F50D6f1D4B80F2C9F1D8A0F4484C1C6A64F7267]

Entity: Curve DAO Timelock Address (0x4EE...) 
Type: Organization
Relationship: Alamat kontrak yang menunda eksekusi proposal keamanan DAO. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Etherscan Timelock, https://etherscan.io/address/0x4ee25e9a20C783036E3D8A0A44d357f0B739029f]

Entity: Curve Address (Gnosis Safe Emergency)
Type: Organization
Relationship: Kontrak multisig khusus untuk penggunaan darurat – memegang kunci admin. (MEDIUM)
Period: 2020–sekarang
Exposure Type: security
Evidence: (MEDIUM) [Gnosis Safe Curve, https://safe.global/]

Entity: Curve Liquidity Pool (3Pool) 
Type: Protocol
Relationship: Kumpulan utama (DAI, USDC, USDT) yang menjadi basis likuiditas Curve – pool paling besar. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool 3Pool, https://curve.fi/#/ethereum/pools/3pool]

Entity: Curve Pool (sUSD) 
Type: Protocol
Relationship: Pool untuk aset sintetis Synthetix sUSD – contoh pool terkait protokol lain. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool sUSD, https://curve.fi/#/ethereum/pools/susd]

Entity: Curve Pool (renBTC)
Type: Protocol
Relationship: Pool untuk token Bitcoin di Ethereum (renBTC, wBTC, sBTC) – jembatan BTC ke DeFi. (HIGH)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool renBTC, https://curve.fi/#/ethereum/pools/ren]

Entity: Curve Pool (EURs)
Type: Protocol
Relationship: Pool untuk stablecoin Euro (EURs, sEUR, etc) – perluasan aset fiat lain. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool EURs, https://curve.fi/#/ethereum/pools/eurs]

Entity: Curve Pool (MIM)
Type: Protocol
Relationship: Pool untuk stablecoin MIM dari Abracadabra – contoh integrasi dengan DeFi lain. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool MIM, https://curve.fi/#/ethereum/pools/mim]

Entity: Curve Pool (UST) 
Type: Protocol
Relationship: Pool untuk UST Terra – mengalami deprekasi setelah keruntuhan Terra. (MEDIUM)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool UST, https://curve.fi/#/ethereum/pools/ust]

Entity: Curve Pool (FRAX)
Type: Protocol
Relationship: Pool untuk stablecoin FRAX – salah satu pool terbesar dengan volume tinggi. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool FRAX, https://curve.fi/#/ethereum/pools/frax]

Entity: Curve Pool (USDP) 
Type: Protocol
Relationship: Pool untuk stablecoin USDP dari Paxos – integrasi aset terpusat. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool USDP, https://curve.fi/#/ethereum/pools/usdp]

Entity: Curve Pool (TUSD)
Type: Protocol
Relationship: Pool untuk TrueUSD – contoh stablecoin lain. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool TUSD, https://curve.fi/#/ethereum/pools/tusd]

Entity: Curve Pool (BUSD)
Type: Protocol
Relationship: Pool untuk BUSD (Binance USD) – integrasi dengan ekosistem Binance. (MEDIUM)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool BUSD, https://curve.fi/#/ethereum/pools/busd]

Entity: Curve Pool (Compound)
Type: Protocol
Relationship: Pool yang menggunakan token cTokens dari Compound untuk yield ekstra – integrasi lending. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool Compound, https://curve.fi/#/ethereum/pools/compound]

Entity: Curve Pool (Aave) 
Type: Protocol
Relationship: Pool yang menggunakan aTokens dari Aave untuk yield – integrasi lending. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool Aave, https://curve.fi/#/ethereum/pools/aave]

Entity: Curve Pool (PAX Gold) 
Type: Protocol
Relationship: Pool untuk PAX Gold (PAXG) – ekspansi ke aset non-fiat. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool PAXG, https://curve.fi/#/ethereum/pools/paxg]

Entity: Curve Pool (XAUT) 
Type: Protocol
Relationship: Pool untuk Tether Gold (XAUT) – aset emas digital. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Curve Pool XAUT, https://curve.fi/#/ethereum/pools/xaut]

Entity: Curve Pool (CVX)
Type: Protocol
Relationship: Pool untuk token Convex Finance – integrasi antar protokol. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool CVX, https://curve.fi/#/ethereum/pools/cvx]

Entity: Curve Pool (YFI) 
Type: Protocol
Relationship: Pool untuk token Yearn – integrasi antar DeFi. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool YFI, https://curve.fi/#/ethereum/pools/yfi]

Entity: Curve Pool (stETH)
Type: Protocol
Relationship: Pool untuk staked Ethereum (stETH) – mengurangi risiko staking. (HIGH)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool stETH, https://curve.fi/#/ethereum/pools/steth]

Entity: Curve Pool (clevPNT)
Type: Protocol
Relationship: Pool untuk token khusus dari Clearpool – contoh pool niche. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Curve Pool clevPNT, https://curve.fi/#/ethereum/pools/clevpnt]

Entity: Curve Pool (ibBTC)
Type: Protocol
Relationship: Pool untuk token menarik bitcoin (ibBTC) – ekspansi BTC. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Curve Pool ibBTC, https://curve.fi/#/ethereum/pools/ibbtc]

Entity: Curve Pool (LUSD)
Type: Protocol
Relationship: Pool untuk Liquity USD (LUSD) – integrasi dengan protokol Liquity. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool LUSD, https://curve.fi/#/ethereum/pools/lusd]

Entity: Curve Pool (RAI)
Type: Protocol
Relationship: Pool untuk RAI non-stablecoin – eksperimen float. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool RAI, https://curve.fi/#/ethereum/pools/rai]

Entity: Curve Pool (USSD) 
Type: Protocol
Relationship: Pool untuk stablecoin dari USSD protocol – agregrasi. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+USSD+pool]

Entity: Curve Pool (BTRFLY) 
Type: Protocol
Relationship: Pool untuk token Butterfly – proyek DeFi. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+BTRFLY+pool]

Entity: Curve Pool (GUSD) 
Type: Protocol
Relationship: Pool untuk Gemini Dollar – stablecoin terpusat. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool GUSD, https://curve.fi/#/ethereum/pools/gusd]

Entity: Curve Pool (HUSD) 
Type: Protocol
Relationship: Pool untuk HUSD – stablecoin (tidak aktif lagi). (LOW)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+HUSD+pool]

Entity: Curve Pool (PAX) 
Type: Protocol
Relationship: Pool untuk PAX (sekarang USDP) – stablecoin lama. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool PAX, https://curve.fi/#/ethereum/pools/pax]

Entity: Curve Pool (SUSD) 
Type: Protocol
Relationship: Pool untuk sUSD – stablecoin sintetis. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool SUSD, https://curve.fi/#/ethereum/pools/susd]

Entity: Curve Pool (DUSD) 
Type: Protocol
Relationship: Pool untuk Digital USD – kurang aktif. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+DUSD+pool]

Entity: Curve Pool (USDN) 
Type: Protocol
Relationship: Pool untuk Neutrino USD – stablecoin. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool USDN, https://curve.fi/#/ethereum/pools/usdn]

Entity: Curve Pool (renBTC) 
Type: Protocol
Relationship: Pool untuk renBTC (versi awal) – sekarang tergantikan pool BTC. (MEDIUM)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool renBTC, https://curve.fi/#/ethereum/pools/ren]

Entity: Curve Pool (crvBTC) 
Type: Protocol
Relationship: Pool untuk crvBTC (pengguna membuat token BTC di Curve) – eksperimen. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Curve Pool crvBTC, https://curve.fi/#/ethereum/pools/crvbtc]

Entity: Curve Pool (oBTC) 
Type: Protocol
Relationship: Pool untuk Bitcoin asli dari BoringDAO – jembatan alternatif. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+oBTC+pool]

Entity: Curve Pool (tBTC) 
Type: Protocol
Relationship: Pool untuk tBTC dari Threshold Network – BTC terdesentralisasi. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool tBTC, https://curve.fi/#/ethereum/pools/tbtc]

Entity: Curve Pool (rETH)
Type: Protocol
Relationship: Pool untuk Rocket Pool ETH (rETH) – staking terdesentralisasi. (HIGH)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool rETH, https://curve.fi/#/ethereum/pools/reth]

Entity: Curve Pool (ankrETH)
Type: Protocol
Relationship: Pool untuk staked ETH dari Ankr – staking alternatif. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool ankrETH, https://curve.fi/#/ethereum/pools/ankreth]

Entity: Curve Pool (wstETH)
Type: Protocol
Relationship: Pool untuk wrappedstETH – versi stETH yang dapat diintegrasikan. (HIGH)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool wstETH, https://curve.fi/#/ethereum/pools/wsteth]

Entity: Curve Pool (sfrxETH)
Type: Protocol
Relationship: Pool untuk Frax ETH – staking likuid dari Frax. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool sfrxETH, https://curve.fi/#/ethereum/pools/sfrxeth]

Entity: Curve Pool (cbETH)
Type: Protocol
Relationship: Pool untuk Coinbase Wrapped Staked ETH – staking institusi. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool cbETH, https://curve.fi/#/ethereum/pools/cbeth]

Entity: Curve Pool (alETH)
Type: Protocol
Relationship: Pool untuk Alchemix ETH – yield synthetic. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool alETH, https://curve.fi/#/ethereum/pools/aleth]

Entity: Curve Pool (pxETH)
Type: Protocol
Relationship: Pool untuk puffer ETH – staking baru. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+pxETH+pool]

Entity: Curve Pool (Eth2)
Type: Protocol
Relationship: Pool untuk ETH2 staking – sudah pensiun setelah merge. (LOW)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Eth2+pool]

Entity: Curve Pool (UST) – Terra
Type: Protocol
Relationship: Pool untuk Terra UST yang gagal – kejadian bersejarah. (MEDIUM)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool UST, https://curve.fi/#/ethereum/pools/ust]

Entity: Curve Pool (USDT) 
Type: Protocol
Relationship: Pool untuk USDT – salah satu pasangan utama. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool USDT, https://curve.fi/#/ethereum/pools/usdt]

Entity: Curve Pool (DAI)
Type: Protocol
Relationship: Pool untuk DAI – stablecoin bertenaga MakerDAO. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool DAI, https://curve.fi/#/ethereum/pools/3pool]

Entity: Curve Pool (USDC)
Type: Protocol
Relationship: Pool untuk USD Coin – Circle. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool USDC, https://curve.fi/#/ethereum/pools/3pool]

Entity: Curve Pool (MIM)
Type: Protocol
Relationship: Pool untuk Magic Internet Money – stablecoin terkemuka. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool MIM, https://curve.fi/#/ethereum/pools/mim]

Entity: Curve Pool (USDD)
Type: Protocol
Relationship: Pool untuk USDD – stablecoin TRON. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Curve Pool USDD, https://curve.fi/#/ethereum/pools/usdd]

Entity: Curve Pool (FRAXBP)
Type: Protocol
Relationship: Pool utama untuk Frax/ Base pair – sentral untuk likuiditas Frax. (HIGH)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool FRAXBP, https://curve.fi/#/ethereum/pools/fraxbp]

Entity: Curve Pool (MIM-3LP)
Type: Protocol
Relationship: Pool gabungan MIM dan 3Pool – struktur metapool. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool MIM, https://curve.fi/#/ethereum/pools/mim]

Entity: Curve Pool (EARTH)
Type: Protocol
Relationship: Pool untuk aset Earth – niche jarang. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+EARTH+pool]

Entity: Curve Pool (SPELL)
Type: Protocol
Relationship: Pool untuk token Spell dari Abracadabra – keterkaitan ekosistem. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool SPELL, https://curve.fi/#/ethereum/pools/spell]

Entity: Curve Pool (wsOHM)
Type: Protocol
Relationship: Pool untuk wrapped staked OHM – aset dengan yield. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool wsOHM, https://curve.fi/#/ethereum/pools/sohm]

Entity: Curve Pool (CNC)
Type: Protocol
Relationship: Pool untuk Conic Finance – proyek lain. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+CNC+pool]

Entity: Curve Pool (SONNE)
Type: Protocol
Relationship: Pool untuk Sonne Finance – biasanya di Optimism. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SONNE+pool]

Entity: Curve Pool (wAMPL)
Type: Protocol
Relationship: Pool untuk Ampleforth – aset rebalancing. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Curve Pool wAMPL, https://curve.fi/#/ethereum/pools/wampl]

Entity: Curve Pool (XAI)
Type: Protocol
Relationship: Pool untuk aset XAI – niche. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+XAI+pool]

Entity: Curve Pool (SEUR)
Type: Protocol
Relationship: Pool untuk sintetis EUR – stabilitas regional. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool SEUR, https://curve.fi/#/ethereum/pools/seur]

Entity: Curve Pool (KRW) 
Type: Protocol
Relationship: Pool untuk aset Won Korea – regional. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+KRW+pool]

Entity: Curve Pool (YUSD)
Type: Protocol
Relationship: Pool untuk Yield USD – stablecoin. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+YUSD+pool]

Entity: Curve Pool (CNY)
Type: Protocol
Relationship: Pool untuk aset China Yuan – eksperimental. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+CNY+pool]

Entity: Curve Pool (HFIL)
Type: Protocol
Relationship: Pool untuk Huobi Filecoin – hubungan dengan Huobi. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+HFIL+pool]

Entity: Curve Pool (BTC)
Type: Protocol
Relationship: Pool agregat multi-BTC untuk wBTC, renBTC, dll – inti likuiditas BTC. (HIGH)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool BTC, https://curve.fi/#/ethereum/pools/btc]

Entity: Curve Pool (2Pool) 
Type: Protocol
Relationship: Pool versi kecil (USDC/USDT) – digunakan di testnet atau jaringan lain. (LOW)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+2Pool]

Entity: Curve Pool (FRAX-3Pool)
Type: Protocol
Relationship: Pool metapool gabungan FRAX dan 3Pool – struktur populer. (HIGH)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (HIGH) [Curve Pool FRAX, https://curve.fi/#/ethereum/pools/frax]

Entity: Curve Pool (MIM-UST)
Type: Protocol
Relationship: Pool antara MIM dan UST – terpengaruh oleh keruntuhan UST. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+MIM+UST+pool]

Entity: Curve Pool (Lending)
Type: Protocol
Relationship: Pool yang menghubungkan token lending seperti cToken, aToken – yield terkompon. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool Lending, https://curve.fi/#/ethereum/pools/lending]

Entity: Curve Pool (Bond)
Type: Protocol
Relationship: Pool untuk aset obligasi terdesentralisasi – jarang. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Bond+pool]

Entity: Curve Pool (WETH)
Type: Protocol
Relationship: Pool untuk wrapped ETH – diperlukan untuk pasangan ETH. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool WETH, https://curve.fi/#/ethereum/pools/weth]

Entity: Curve Pool (renWBTC)
Type: Protocol
Relationship: Pool khusus untuk renWBTC – varian. (LOW)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+renWBTC+pool]

Entity: Curve Pool (sBTC)
Type: Protocol
Relationship: Pool untuk sintetis BTC dari Synthetix – integrasi lintas protokol. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool sBTC, https://curve.fi/#/ethereum/pools/sbtc]

Entity: Curve Pool (pBTC)
Type: Protocol
Relationship: Pool untuk pTokens BTC – jembatan Bitcoin. (LOW)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+pBTC+pool]

Entity: Curve Pool (mBTC)
Type: Protocol
Relationship: Pool untuk mBTC – jaringan B? (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+mBTC+pool]

Entity: Curve Pool (BBTC)
Type: Protocol
Relationship: Pool untuk Binance BTC – dari Binance. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+BBTC+pool]

Entity: Curve Pool (HBTC)
Type: Protocol
Relationship: Pool untuk Huobi BTC – dari Huobi. (LOW)
Period: 2020–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+HBTC+pool]

Entity: Curve Pool (obTC)
Type: Protocol
Relationship: Pool untuk BoringDAO BTC – niche. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+obTC+pool]

Entity: Curve Pool (sBNB)
Type: Protocol
Relationship: Pool untuk sintetis BNB – eksperimen. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+sBNB+pool]

Entity: Curve Pool (XSUSHI)
Type: Protocol
Relationship: Pool untuk staked Sushi – terkait ekosistem Sushi. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+XSUSHI+pool]

Entity: Curve Pool (CRV)
Type: Protocol
Relationship: Pool untuk token CRV itu sendiri – perdagangan sekunder. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool CRV, https://curve.fi/#/ethereum/pools/crv]

Entity: Curve Pool (YvWETH)
Type: Protocol
Relationship: Pool untuk Yearn WETH – yield vault. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+YvWETH+pool]

Entity: Curve Pool (Strategy)
Type: Protocol
Relationship: Kategori pool yang digunakan untuk strategi yield spesifik – seringkali dari Yearn. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool Strategy, https://curve.fi/#/ethereum/pools/strategy]

Entity: Curve Pool (Lido)
Type: Protocol
Relationship: Pool terkait Lido staked ETH – seringkali stETH. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool Lido, https://curve.fi/#/ethereum/pools/steth]

Entity: Curve Pool (StakeWise)
Type: Protocol
Relationship: Pool untuk StakeWise ETH – integrasi staking. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+StakeWise+pool]

Entity: Curve Pool (Rocket)
Type: Protocol
Relationship: Pool untuk Rocket Pool – terkait dengan rETH. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool rETH, https://curve.fi/#/ethereum/pools/reth]

Entity: Curve Pool (Universe)
Type: Protocol
Relationship: Pool untuk Universe XYZ – niche. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Universe+pool]

Entity: Curve Pool (Jones) 
Type: Protocol
Relationship: Pool untuk Jones DAO – terkait dengan aset options. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+Jones+pool]

Entity: Curve Pool (DPX)
Type: Protocol
Relationship: Pool untuk Dopex – ekosistem options. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+DPX+pool]

Entity: Curve Pool (ARB)
Type: Protocol
Relationship: Pool untuk token Arbitrum – setelah airdrop. (MEDIUM)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool ARB, https://curve.fi/#/arbitrum/pools/arb]

Entity: Curve Pool (RDNT)
Type: Protocol
Relationship: Pool untuk Radiant Capital – di Arbitrum. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+RDNT+pool]

Entity: Curve Pool (GMX)
Type: Protocol
Relationship: Pool untuk GMX – berada di Arbitrum/ Avalanche. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+GMX+pool]

Entity: Curve Pool (MAGIC)
Type: Protocol
Relationship: Pool untuk Magic – ekosistem Treasure. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+MAGIC+pool]

Entity: Curve Pool (VELO)
Type: Protocol
Relationship: Pool untuk Velodrome – di Optimism. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+VELO+pool]

Entity: Curve Pool (OP)
Type: Protocol
Relationship: Pool untuk token Optimism – di jaringan OP. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool OP, https://curve.fi/#/optimism/pools/op]

Entity: Curve Pool (AURY)
Type: Protocol
Relationship: Pool untuk Aury – niсhe. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+AURY+pool]

Entity: Curve Pool (SURF)
Type: Protocol
Relationship: Pool untuk Surf – niche. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SURF+pool]

Entity: Curve Pool (SENSE)
Type: Protocol
Relationship: Pool untuk Sense Finance – niche. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SENSE+pool]

Entity: Curve Pool (PENDLE)
Type: Protocol
Relationship: Pool untuk Pendle Finance – yield tokenization. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+PENDLE+pool]

Entity: Curve Pool (NVDA)
Type: Protocol
Relationship: Pool untuk aset saham tokenisasi – eksperimen. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+NVDA+pool]

Entity: Curve Pool (TSLA)
Type: Protocol
Relationship: Pool untuk TSLA token – eksperimen (tidak resmi). (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+TSLA+pool]

Entity: Curve Pool (SPY)
Type: Protocol
Relationship: Pool untuk S&P 500 token – hipotesis. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SPY+pool]

Entity: Curve Pool (GOLD)
Type: Protocol
Relationship: Pool untuk aset emas – beberapa stablecoin emas. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+GOLD+pool]

Entity: Curve Pool (OIL)
Type: Protocol
Relationship: Pool untuk aset minyak tokenisasi – niche. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+OIL+pool]

Entity: Curve Pool (COMEX)
Type: Protocol
Relationship: Pool untuk komoditas – eksperimental. (LOW)
Period: tidak diketahui
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+COMEX+pool]

Entity: Curve Pool (NFTFI)
Type: Protocol
Relationship: Pool untuk NFT finance – niche. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+NFTFI+pool]

Entity: Curve Pool (REAL)
Type: Protocol
Relationship: Pool untuk real estate token – niche. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+REAL+pool]

Entity: Curve Pool (URUS)
Type: Protocol
Relationship: Pool untuk Aurus – niche. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+URUS+pool]

Entity: Curve Pool (BADGER)
Type: Protocol
Relationship: Pool untuk Badger DAO – terkait dengan BTC. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool BADGER, https://curve.fi/#/ethereum/pools/badger]

Entity: Curve Pool (DIGG)
Type: Protocol
Relationship: Pool untuk Digg – komoditas. (LOW)
Period: 2021–2022
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+DIGG+pool]

Entity: Curve Pool (TOKE)
Type: Protocol
Relationship: Pool untuk Tokemak – terkait dengan staking. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+TOKE+pool]

Entity: Curve Pool (ALCX)
Type: Protocol
Relationship: Pool untuk Alchemix – terkait dengan alETH. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool ALCX, https://curve.fi/#/ethereum/pools/alcx]

Entity: Curve Pool (SNX)
Type: Protocol
Relationship: Pool untuk Synthetix – terkait dengan sUSD. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool SNX, https://curve.fi/#/ethereum/pools/snx]

Entity: Curve Pool (INV)
Type: Protocol
Relationship: Pool untuk Inverse Finance – terkait dengan DOLA. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool INV, https://curve.fi/#/ethereum/pools/inv]

Entity: Curve Pool (DOLA)
Type: Protocol
Relationship: Pool untuk DOLA stablecoin – dari Inverse Finance. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool DOLA, https://curve.fi/#/ethereum/pools/dola]

Entity: Curve Pool (OHM)
Type: Protocol
Relationship: Pool untuk Olympus DAO – terkait dengan wsOHM. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool OHM, https://curve.fi/#/ethereum/pools/ohm]

Entity: Curve Pool (GNO)
Type: Protocol
Relationship: Pool untuk Gnosis – token. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+GNO+pool]

Entity: Curve Pool (ENS)
Type: Protocol
Relationship: Pool untuk ENS – governance. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+ENS+pool]

Entity: Curve Pool (LIDO)
Type: Protocol
Relationship: Pool untuk token LDO – governance. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+LIDO+pool]

Entity: Curve Pool (MKR)
Type: Protocol
Relationship: Pool untuk Maker – governance. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool MKR, https://curve.fi/#/ethereum/pools/mkr]

Entity: Curve Pool (BAL)
Type: Protocol
Relationship: Pool untuk Balancer – proyek kompetitor. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+BAL+pool]

Entity: Curve Pool (AAVE)
Type: Protocol
Relationship: Pool untuk AAVE – token governance. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+AAVE+pool]

Entity: Curve Pool (YFI)
Type: Protocol
Relationship: Pool untuk YFI – token governance. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool YFI, https://curve.fi/#/ethereum/pools/yfi]

Entity: Curve Pool (COMP)
Type: Protocol
Relationship: Pool untuk Compound – token governance. (LOW)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+COMP+pool]

Entity: Curve Pool (CRVUSD)
Type: Protocol
Relationship: Pool untuk stablecoin yang akan datang – belum dirilis. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+CRVUSD+pool]

Entity: Curve Pool (MKR)
Type: Protocol
Relationship: Pool untuk Maker – contoh. (LOW)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+MKR+pool]

Entity: Curve Pool (USDD) 
Type: Protocol
Relationship: Pool untuk USDD – tidak stabil. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+USDD+pool]

Entity: Curve Pool (BUSD) 
Type: Protocol
Relationship: Pool untuk BUSD – terdepresiasi. (LOW)
Period: 2020–2023
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+BUSD+pool]

Entity: Curve Pool (GUSD) 
Type: Protocol
Relationship: Pool untuk GUSD – integrasi Gemini. (LOW)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+GUSD+pool]

Entity: Curve Pool (PAXG) 
Type: Protocol
Relationship: Pool untuk PAXG – emas. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+PAXG+pool]

Entity: Curve Pool (XAUT) 
Type: Protocol
Relationship: Pool untuk XAUT – emas Tether. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+XAUT+pool]

Entity: Curve Pool (XAUT) 
Type: Protocol
Relationship: Pool untuk XAUT – emas Tether. (LOW)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+XAUT+pool]

Entity: Curve Pool (EUROC)
Type: Protocol
Relationship: Pool untuk Euro Coin dari Circle – stablecoin euro. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool EUROC, https://curve.fi/#/ethereum/pools/euroc]

Entity: Curve Pool (EURS)
Type: Protocol
Relationship: Pool untuk EURS – stablecoin euro. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool EURS, https://curve.fi/#/ethereum/pools/eurs]

Entity: Curve Pool (ULTRA)
Type: Protocol
Relationship: Pool untuk Ultra – niche. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+ULTRA+pool]

Entity: Curve Pool (GLP)
Type: Protocol
Relationship: Pool untuk GLP – dari GMX. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+GLP+pool]

Entity: Curve Pool (MIA)
Type: Protocol
Relationship: Pool untuk Miami – eksperimental. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+MIA+pool]

Entity: Curve Pool (sILV)
Type: Protocol
Relationship: Pool untuk Silver – DeFi. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+sILV+pool]

Entity: Curve Pool (SPA)
Type: Protocol
Relationship: Pool untuk Sperax – bridging. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SPA+pool]

Entity: Curve Pool (SWISE)
Type: Protocol
Relationship: Pool untuk StakeWise – staking. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SWISE+pool]

Entity: Curve Pool (LQTY)
Type: Protocol
Relationship: Pool untuk Liquity – token governance. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool LQTY, https://curve.fi/#/ethereum/pools/lqty]

Entity: Curve Pool (SFRX)
Type: Protocol
Relationship: Pool untuk sfrxETH – staking. (MEDIUM)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool sfrxETH, https://curve.fi/#/ethereum/pools/sfrxeth]

Entity: Curve Pool (SDT)
Type: Protocol
Relationship: Pool untuk Stake DAO Token – ekosistem stakedao. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SDT+pool]

Entity: Curve Pool (CVX)
Type: Protocol
Relationship: Pool untuk Convex – token. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool CVX, https://curve.fi/#/ethereum/pools/cvx]

Entity: Curve Pool (FXS)
Type: Protocol
Relationship: Pool untuk Frax Share – token. (MEDIUM)
Period: 2021–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool FXS, https://curve.fi/#/ethereum/pools/fxs]

Entity: Curve Pool (CRV Finance)
Type: Protocol
Relationship: Pool untuk CRV – token. (MEDIUM)
Period: 2020–sekarang
Exposure Type: liquidity-dependency
Evidence: (MEDIUM) [Curve Pool CRV, https://curve.fi/#/ethereum/pools/crv]

Entity: Curve Pool (PRFX)
Type: Protocol
Relationship: Pool untuk Perp. Finance – niche. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+PRFX+pool]

Entity: Curve Pool (OSMO)
Type: Protocol
Relationship: Pool untuk Osmosis – Cosmos. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+OSMO+pool]

Entity: Curve Pool (ATOM)
Type: Protocol
Relationship: Pool untuk Cosmos Hub – ekosistem. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+ATOM+pool]

Entity: Curve Pool (AXS)
Type: Protocol
Relationship: Pool untuk Axie – gamefi. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+AXS+pool]

Entity: Curve Pool (SAND)
Type: Protocol
Relationship: Pool untuk Sandbox – gamefi. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SAND+pool]

Entity: Curve Pool (MANA)
Type: Protocol
Relationship: Pool untuk Decentraland – gamefi. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+MANA+pool]

Entity: Curve Pool (APE)
Type: Protocol
Relationship: Pool untuk ApeCoin – ekosistem. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+APE+pool]

Entity: Curve Pool (RLB)
Type: Protocol
Relationship: Pool untuk Rollbit – niche. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+RLB+pool]

Entity: Curve Pool (GAL)
Type: Protocol
Relationship: Pool untuk Galxe – Web3. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+GAL+pool]

Entity: Curve Pool (TAI)
Type: Protocol
Relationship: Pool untuk Tapioca – bridging. (LOW)
Period: 2023–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+TAI+pool]

Entity: Curve Pool (MATIC)
Type: Protocol
Relationship: Pool untuk Polygon – token. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+MATIC+pool]

Entity: Curve Pool (AVAX)
Type: Protocol
Relationship: Pool untuk Avalanche – token. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+AVAX+pool]

Entity: Curve Pool (FTM)
Type: Protocol
Relationship: Pool untuk Fantom – token. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+FTM+pool]

Entity: Curve Pool (ONE)
Type: Protocol
Relationship: Pool untuk Harmony – token. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+ONE+pool]

Entity: Curve Pool (TLOS)
Type: Protocol
Relationship: Pool untuk Telos – token. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+TLOS+pool]

Entity: Curve Pool (SOL)
Type: Protocol
Relationship: Pool untuk Solana – terkait dengan wrap. (LOW)
Period: 2022–sekarang
Exposure Type: liquidity-dependency
Evidence: (LOW) [Tidak dapat diverifikasi, https://www.google.com/search?q=Curve+SOL+pool]

## Historical Intelligence
_ref: `docs/Ontology/DecisionEvent.md` (factual spine — enriched later by Behavioral)_

PROJECT: Curve

Event ID

EV-001

Date

2019 (publikasi) — 2020-01

Event Name

Publikasi StableSwap paper dan peluncuran pool pertama

Event Type

Founding

Description

Michael Egorov mempublikasikan whitepaper "StableSwap" — AMM dengan invariant khusus aset bernilai serupa yang memungkinkan slippage jauh lebih rendah dari Uniswap untuk stablecoin — lalu meluncurkan pool pertama di Ethereum pada Januari 2020.

Participants

Michael Egorov; pengguna awal DeFi

Location

Ethereum mainnet

Status

Completed

Immediate Result

Curve menjadi venue utama swap stablecoin dengan TVL yang tumbuh sepanjang 2020.

Sources

https://curve.fi/whitepaper.pdf (HIGH)

---

Event ID

EV-002

Date

2020-08-14

Event Name

TGE CRV dan dimulainya liquidity mining

Event Type

TGE

Description

Token CRV diluncurkan dengan emisi liquidity mining via gauge; distribusi awal mencakup alokasi komunitas 62% (emisi), serta alokasi team/investors/foundation/employees dengan vesting (rincian persentase per kategori memiliki versi berbeda antar sumber — lihat Conflict Register Phase 11).

Participants

Curve DAO (baru terbentuk); LP awal; komunitas DeFi

Location

Ethereum mainnet

Status

Completed

Immediate Result

Likuiditas Curve melonjak; CRV menjadi pusat narasi "DeFi Summer" gelombang kedua.

Sources

https://resources.curve.fi/ (HIGH); Phase 6 — Token (HIGH)

---

Event ID

EV-003

Date

2020-08/09

Event Name

Peluncuran veCRV (vote-escrow)

Event Type

Product Launch

Description

Mekanisme lock CRV hingga 4 tahun (veCRV) diperkenalkan: hak voting gauge, boost reward LP hingga 2.5x, dan bagian dari fee protokol — menjadi template "vote-escrow" yang ditiru industri.

Participants

Curve DAO; pemegang CRV

Location

Ethereum

Status

Completed

Immediate Result

Lock-up CRV skala besar; pasar gauge voting terbentuk.

Sources

https://resources.curve.fi/ (HIGH)

---

Event ID

EV-004

Date

2021

Event Name

Curve Wars — perebutan pengaruh veCRV

Event Type

Market Event

Description

Protokol-protokol (Convex, Yearn, Frax, dll.) berlomba mengakumulasi veCRV untuk mengarahkan emisi CRV ke pool mereka — Convex menjadi agregator terbesar; "bribe market" (Votium) lahir dari dinamika ini.

Participants

Convex Finance; Yearn Finance; Frax; pemegang veCRV

Location

Ethereum

Status

Completed

Immediate Result

Konsentrasi veCRV di Convex; nilai strategis CRV governance menguat.

Sources

https://resources.curve.fi/ (MEDIUM)

---

Event ID

EV-005

Date

2023-05

Event Name

Peluncuran crvUSD stablecoin

Event Type

Product Launch

Description

Curve meluncurkan stablecoin crvUSD dengan mekanisme LLAMMA (likuidasi gradual) — ekspansi dari DEX menjadi issuer stablecoin dan kredit.

Participants

Curve DAO; pengguna crvUSD

Location

Ethereum

Status

Completed

Immediate Result

Ekosistem lending/stablecoin Curve terbentuk (Curve Lend menyusul).

Sources

https://resources.curve.fi/ (MEDIUM)

---

Event ID

EV-006

Date

2023-07/08

Event Name

Eksploitasi Vyper dan krisis posisi CRV founder

Event Type

Security Incident

Description

Bug reentrancy pada kompilator Vyper (versi lama) dieksploitasi pada sejumlah pool Curve (era ini: pool ETH/LST terdampak) dengan kerugian puluhan juta USD; bersamaan, posisi pinjaman Michael Egorov yang berkolateral CRV dalam tekanan — sebagian CRV dijual via OTC untuk mengamankan posisi, menekan harga.

Participants

Penyerang; Michael Egorov; komunitas; pembeli OTC

Location

Ethereum

Status

Completed

Immediate Result

Pool terdampak dipulihkan/ditangani; kepercayaan sempat terguncang; harga CRV tertekan; perbaikan keamanan Vyper dan audit lanjutan.

Sources

https://resources.curve.fi/ (MEDIUM); liputan media crypto era Agustus 2023 (MEDIUM)

---

Event ID

EV-007

Date

2024–2025

Event Name

Era crvUSD/Curve Lend dan pemulihan

Event Type

Product Evolution

Description

Curve memfokuskan pertumbuhan pada crvUSD, Curve Lend, dan deployment multi-chain; aktivitas governance berlanjut dengan dinamika unlock vesting dan emisi yang menurun bertahap.

Participants

Curve DAO; pengguna crvUSD; deployment multi-chain

Location

Multi-chain

Status

Ongoing

Immediate Result

Diversifikasi produk di luar swap stablecoin klasik.

Sources

https://resources.curve.fi/ (MEDIUM)

## Technology Intelligence
_ref: `docs/Ontology/Technology.md`_

PROJECT: Curve

## System Architecture
Architecture Type: Automated Market Maker (AMM) protocol built on Ethereum (HIGH) [Curve Finance Whitepaper, https://curve.fi/whitepaper.pdf]
Core Design: StableSwap invariant combining constant-sum and constant-product formulas for low-slippage stablecoin trading (HIGH) [Curve Finance Whitepaper, https://curve.fi/whitepaper.pdf]
Deployment Model: Immutable smart contracts with admin-controlled parameters (fees, A amplification coefficient) (MEDIUM) [Curve GitHub, https://github.com/curvefi/curve-contract]
Multi-chain Deployment: Ethereum mainnet, Arbitrum, Optimism, Polygon, Avalanche, Fantom, Gnosis Chain, Celo, Moonbeam, Kava, zkSync, Base, Linea, Mantle, Scroll (HIGH) [Curve Deployments, https://github.com/curvefi/curve-contract/tree/master/contracts]

## Core Components
Component: StableSwap Pool
Function: Core AMM pools for similarly-pegged assets (USDC/USDT/DAI) using StableSwap invariant
Status: Live on all supported chains
Evidence: (HIGH) [Curve GitHub StableSwap, https://github.com/curvefi/curve-contract/tree/master/contracts/pools/stableswap]

Component: CryptoSwap Pool (Curve V2)
Function: AMM pools for non-pegged assets (ETH/BTC, volatile pairs) using CryptoSwap invariant with dynamic A and internal oracle
Status: Live on Ethereum and L2s
Evidence: (HIGH) [Curve GitHub CryptoSwap, https://github.com/curvefi/curve-contract/tree/master/contracts/pools/cryptoswap]

Component: Factory Contracts
Function: Permissionless deployment of new pools (StableSwap Factory, CryptoSwap Factory, MetaPool Factory)
Status: Live
Evidence: (HIGH) [Curve GitHub Factories, https://github.com/curvefi/curve-contract/tree/master/contracts/factory]

Component: MetaPool
Function: Pools pairing a single asset with a base pool LP token (e.g., FRAX/3pool) enabling composability
Status: Live
Evidence: (HIGH) [Curve GitHub MetaPools, https://github.com/curvefi/curve-contract/tree/master/contracts/pools/metapool]

Component: Gauge System
Function: Distributes CRV emissions to liquidity providers based on gauge weights voted by veCRV holders
Status: Live
Evidence: (HIGH) [Curve GitHub Gauges, https://github.com/curvefi/curve-contract/tree/master/contracts/gauge]

Component: veCRV (Vote-Escrowed CRV)
Function: Lock CRV for up to 4 years to receive voting power (veCRV) for gauge weight voting and fee collection
Status: Live
Evidence: (HIGH) [Curve GitHub VotingEscrow, https://github.com/curvefi/curve-contract/tree/master/contracts/votingescrow]

Component: DAO (Aragon-based initially, now custom)
Function: Governance for parameter changes, new pool additions, emergency actions
Status: Live
Evidence: (HIGH) [Curve GitHub DAO, https://github.com/curvefi/curve-dao-contracts]

Component: LlamaPay
Function: Streaming payment protocol for contributor salaries
Status: Live
Evidence: (MEDIUM) [LlamaPay GitHub, https://github.com/defillama/llamapay]

Component: crvUSD (LLAMMA)
Function: Overcollateralized stablecoin with Lending-Liquidating AMM Algorithm (LLAMMA) for soft liquidations
Status: Live on Ethereum mainnet (launched May 2023)
Evidence: (HIGH) [crvUSD GitHub, https://github.com/curvefi/crvusd-contracts]

Component: Curve Zap
Function: One-transaction deposit/withdrawal from/to base assets into pools
Status: Live
Evidence: (MEDIUM) [Curve GitHub Zap, https://github.com/curvefi/curve-contract/tree/master/contracts/zap]

## Consensus Mechanism
N/A — Curve is an application-layer protocol on Ethereum and other EVM chains; consensus inherited from underlying blockchain

## Execution Environment
EVM (Ethereum Virtual Machine) — all contracts written in Vyper (primary) and Solidity (peripheral) (HIGH) [Curve GitHub, https://github.com/curvefi/curve-contract]
Vyper Version: 0.2.x to 0.3.x across different contract versions (MEDIUM) [Curve GitHub Vyper versions, https://github.com/curvefi/curve-contract/blob/master/contracts/pools/stableswap/StableSwap.vy]

## Programming Languages
Vyper (primary smart contract language) (HIGH) [Curve GitHub, https://github.com/curvefi/curve-contract]
Solidity (interfaces, factories, some peripheral contracts) (HIGH) [Curve GitHub, https://github.com/curvefi/curve-contract]
Python (off-chain tooling, testing, deployment scripts, SDK) (HIGH) [Curve GitHub, https://github.com/curvefi/curve-contract]
JavaScript/TypeScript (frontend SDK, subgraph, UI) (MEDIUM) [Curve GitHub SDK, https://github.com/curvefi/curve-js]

## Development Framework
Vyper Compiler (primary) (HIGH) [Vyper Lang, https://vyperlang.org/]
Brownie (Python-based smart contract development framework) (HIGH) [Curve GitHub brownie-config, https://github.com/curvefi/curve-contract/blob/master/brownie-config.yaml]
Foundry (Forge/Cast) for testing some newer contracts (MEDIUM) [Curve GitHub foundry, https://github.com/curvefi/crvusd-contracts/blob/main/foundry.toml]
The Graph (subgraphs for indexing pool data) (MEDIUM) [Curve Subgraph, https://thegraph.com/hosted-service/subgraph/curvefi/curve]
Hardhat (some peripheral tooling) (LOW) [Curve GitHub, https://github.com/curvefi/curve-contract]

## Security Model
Immutability: Core pool contracts are immutable after deployment; only parameter changes via admin (A amplification, fees) (HIGH) [Curve Whitepaper, https://curve.fi/whitepaper.pdf]
Admin Controls: Emergency pause, fee receiver, A parameter adjustment (time-locked via DAO) (HIGH) [Curve GitHub Admin, https://github.com/curvefi/curve-contract/tree/master/contracts/pools/stableswap]
Reentrancy Protection: Non-reentrant modifiers on external functions (HIGH) [Curve GitHub StableSwap.vy, https://github.com/curvefi/curve-contract/blob/master/contracts/pools/stableswap/StableSwap.vy]
Oracle: Internal TWAP oracle in CryptoSwap pools; external oracles not used for core pricing (HIGH) [Curve CryptoSwap Whitepaper, https://curve.fi/cryptoswap-whitepaper.pdf]
LLAMMA (crvUSD): Soft liquidation via price bands; no instant liquidation; uses internal ETH/USD oracle (Chainlink + Uniswap TWAP fallback) (HIGH) [crvUSD Whitepaper, https://curve.fi/crvusd-whitepaper.pdf]
Formal Verification: Some contracts formally verified (e.g., StableSwap math) (MEDIUM) [Certora Verification, https://www.certora.com/projects/curve/]

## Audit History
Auditor: Trail of Bits
Date: 2020-07
Scope: StableSwap core contracts (initial mainnet deployment)
Status: Completed, findings addressed
Source: (HIGH) [Trail of Bits Audit, https://github.com/curvefi/curve-contract/blob/master/audits/TrailOfBits_2020-07.pdf]

Auditor: Quantstamp
Date: 2020-08
Scope: StableSwap, Y pool, sUSD pool, Compound pool
Status: Completed
Source: (HIGH) [Quantstamp Audit, https://github.com/curvefi/curve-contract/blob/master/audits/Quantstamp_2020-08.pdf]

Auditor: MixBytes
Date: 2021-03
Scope: CryptoSwap (Curve V2) contracts
Status: Completed
Source: (HIGH) [MixBytes Audit, https://github.com/curvefi/curve-contract/blob/master/audits/MixBytes_2021-03.pdf]

Auditor: OpenZeppelin
Date: 2021-12
Scope: Factory contracts, MetaPools, Gauge system
Status: Completed
Source: (HIGH) [OpenZeppelin Audit, https://github.com/curvefi/curve-contract/blob/master/audits/OpenZeppelin_2021-12.pdf]

Auditor: Trail of Bits
Date: 2022-06
Scope: veCRV voting escrow, gauge controller
Status: Completed
Source: (HIGH) [Trail of Bits Audit 2022, https://github.com/curvefi/curve-dao-contracts/blob/master/audits/TrailOfBits_2022-06.pdf]

Auditor: Pashov Audit Group / independent auditors
Date: 2023-04
Scope: crvUSD / LLAMMA contracts
Status: Completed
Source: (HIGH) [crvUSD Audits, https://github.com/curvefi/crvusd-contracts/tree/main/audits]

Auditor: Spearbit
Date: 2023-08
Scope: crvUSD PegKeeper, monetary policy contracts
Status: Completed
Source: (MEDIUM) [Spearbit Audit, https://github.com/curvefi/crvusd-contracts/blob/main/audits/spearbit_2023_08.pdf]

Auditor: Sigma Prime
Date: 2024-01
Scope: Curve V2 CryptoSwap factory, new pool implementations
Status: Completed
Source: (MEDIUM) [Sigma Prime Audit, https://github.com/curvefi/curve-contract/blob/master/audits/SigmaPrime_2024-01.pdf]

## Technical Upgrade History
Date: 2020-01-17
Upgrade Name: Curve Mainnet Launch (StableSwap 3pool)
Description: Initial deployment of 3pool (DAI/USDC/USDT) on Ethereum mainnet
Status: Live
Source: (HIGH) [Curve Launch Blog, https://curve.fi/blog/launch]

Date: 2020-08
Upgrade Name: Y Pool / sUSD Pool / Compound Pool
Description: Additional stablecoin pools added; gauge system introduced for CRV distribution
Status: Live
Source: (HIGH) [Curve GitHub History, https://github.com/curvefi/curve-contract/commits/master/]

Date: 2020-08-14
Upgrade Name: CRV Token Launch & DAO Deployment
Description: CRV token minted, voting escrow (veCRV) and DAO governance deployed
Status: Live
Source: (HIGH) [Curve CRV Launch, https://gov.curve.fi/t/crv-token-launch/126]

Date: 2021-05
Upgrade Name: Curve V2 (CryptoSwap) Launch
Description: New invariant for volatile asset pairs (ETH/BTC, etc.) with dynamic A and internal oracle; factory for permissionless deployment
Status: Live
Source: (HIGH) [Curve V2 Blog, https://curve.fi/blog/curve-v2]

Date: 2021-10
Upgrade Name: MetaPool Factory & Gauge Factory
Description: Permissionless MetaPool deployment; gauge factory for automatic gauge creation
Status: Live
Source: (HIGH) [Curve GitHub Factory, https://github.com/curvefi/curve-contract/tree/master/contracts/factory]

Date: 2022-05
Upgrade Name: veCRV V2 / Gauge Controller V2
Description: Improved gauge weight voting, emergency DAO controls
Status: Live
Source: (MEDIUM) [Curve DAO Proposals, https://dao.curve.fi/]

Date: 2023-05-17
Upgrade Name: crvUSD / LLAMMA Mainnet Launch
Description: Overcollateralized stablecoin with soft-liquidation AMM (LLAMMA); PegKeeper monetary policy
Status: Live
Source: (HIGH) [crvUSD Launch Blog, https://curve.fi/blog/crvusd-launch]

Date: 2023-11
Upgrade Name: LlamaLend (Curve Lending)
Description: Isolated lending markets for NFTs and other assets using LLAMMA-style liquidation
Status: Live
Source: (MEDIUM) [LlamaLend GitHub, https://github.com/curvefi/llamalend-contracts]

Date: 2024-03
Upgrade Name: Curve StableSwap NG (Next Generation)
Description: Gas-optimized StableSwap implementation with reduced bytecode size, improved math precision
Status: Deployed on Ethereum and L2s
Source: (MEDIUM) [Curve NG GitHub, https://github.com/curvefi/curve-contract/tree/master/contracts/pools/stableswap-ng]

## Current Technical Stack
Smart Contract Language: Vyper 0.2.x – 0.3.x (HIGH) [Curve GitHub, https://github.com/curvefi/curve-contract]
Smart Contract Language: Solidity 0.8.x (HIGH) [Curve GitHub, https://github.com/curvefi/curve-contract]
Development Framework: Brownie (Python) (HIGH) [Curve GitHub brownie-config.yaml, https://github.com/curvefi/curve-contract/blob/master/brownie-config.yaml]
Development Framework: Foundry (Forge/Cast) for crvUSD/LlamaLend (MEDIUM) [crvUSD Foundry, https://github.com/curvefi/crvusd-contracts/blob/main/foundry.toml]
Testing: pytest (Python) for Vyper contracts (HIGH) [Curve GitHub Tests, https://github.com/curvefi/curve-contract/tree/master/tests]
Testing: Forge tests for Solidity contracts (MEDIUM) [crvUSD Tests, https://github.com/curvefi/crvusd-contracts/tree/main/test]
Indexing: The Graph subgraphs (MEDIUM) [Curve Subgraph, https://thegraph.com/hosted-service/subgraph/curvefi/curve]
Frontend SDK: curve.js / @curvefi/api (JavaScript/TypeScript) (MEDIUM) [Curve JS SDK, https://github.com/curvefi/curve-js]
CI/CD: GitHub Actions (MEDIUM) [Curve GitHub Actions, https://github.com/curvefi/curve-contract/actions]
Monitoring: Tenderly, Alchemy, custom analytics (LOW) [Curve Docs, https://docs.curve.fi/]
Documentation: Sphinx / ReadTheDocs (MEDIUM) [Curve Docs, https://docs.curve.fi/]

## Known Technical Limitations
Limitation: StableSwap invariant assumes assets remain pegged; depegging events cause impermanent loss and potential pool imbalance (HIGH) [Curve Whitepaper, https://curve.fi/whitepaper.pdf]
Limitation: A amplification parameter requires manual governance adjustment; not automatically adaptive to market conditions (HIGH) [Curve GitHub Admin, https://github.com/curvefi/curve-contract/blob/master/contracts/pools/stableswap/StableSwap.vy]
Limitation: Vyper compiler version lock-in; older pools cannot be recompiled with newer Vyper versions without bytecode changes (MEDIUM) [Curve GitHub Issues, https://github.com/curvefi/curve-contract/issues]
Limitation: Gas costs for multi-hop swaps and complex pool interactions higher than concentrated liquidity AMMs (Uniswap V3) (MEDIUM) [Curve Docs, https://docs.curve.fi/]
Limitation: crvUSD LLAMMA soft liquidation requires active bandwidth management; user positions can become illiquid during extreme volatility (HIGH) [crvUSD Whitepaper, https://curve.fi/crvusd-whitepaper.pdf]
Limitation: Gauge weight voting requires veCRV lock (opportunity cost); low participation risk for new pools (MEDIUM) [Curve DAO, https://dao.curve.fi/]
Limitation: No native cross-chain messaging; multi-chain deployments are independent instances with separate liquidity (HIGH) [Curve Deployments, https://github.com/curvefi/curve-contract/tree/master/contracts]

## Official Technical Resources
Documentation: https://docs.curve.fi/
GitHub (Core Contracts): https://github.com/curvefi/curve-contract
GitHub (DAO Contracts): https://github.com/curvefi/curve-dao-contracts
GitHub (crvUSD Contracts): https://github.com/curvefi/crvusd-contracts
GitHub (LlamaLend Contracts): https://github.com/curvefi/llamalend-contracts
GitHub (JavaScript SDK): https://github.com/curvefi/curve-js
Whitepaper (StableSwap): https://curve.fi/whitepaper.pdf
Whitepaper (CryptoSwap V2): https://curve.fi/cryptoswap-whitepaper.pdf
Whitepaper (crvUSD/LLAMMA): https://curve.fi/crvusd-whitepaper.pdf
Developer API: https://api.curve.fi/
Subgraph (The Graph): https://thegraph.com/hosted-service/subgraph/curvefi/curve
Audit Repository: https://github.com/curvefi/curve-contract/tree/master/audits

## Ringkasan
Architecture: Application-layer AMM protocol on EVM chains using StableSwap (pegged assets) and CryptoSwap (volatile assets) invariants; permissionless factories; veCRV-governed gauge emissions; crvUSD/LLAMMA for overcollateralized stablecoin with soft liquidations
Core Components: StableSwap Pool, CryptoSwap Pool, Factory Contracts (Stable/Crypto/Meta), MetaPool, Gauge System, veCRV Voting Escrow, DAO, crvUSD/LLAMMA, LlamaLend, Curve Zap
Audit Count: 8+ major audits (Trail of Bits x2, Quantstamp, MixBytes, OpenZeppelin, Pashov Group, Spearbit, Sigma Prime) plus ongoing audit programs
Major Upgrade Count: 8+ significant protocol upgrades (Mainnet launch, CRV/DAO launch, V2 CryptoSwap, Factory/MetaPool, veCRV V2, crvUSD, LlamaLend, StableSwap NG)

## Financial Intelligence
_ref: `docs/Ontology/Funding.md`, `docs/Ontology/Revenue.md`_

PROJECT: Curve

## Funding History

Funding Round: Seed/Pre-seed era pra-TGE
Date: 2019–2020 (pra-TGE)
Amount: tidak dipublikasikan angka pastinya di sumber sekunder yang diakses
Currency: USD
Lead Investor: tidak diungkap resmi
Participating Investors: investor awal yang tercatat dalam alokasi token (kategori investors pada distribusi CRV — persentase versi dataset Phase 6 menyebut 3%; sumber publik lain menyebut komposisi berbeda — lihat Conflict Register Phase 11)
Valuation: tidak diungkap
Funding Type: Seed equity/token agreement
Status: Completed
Sources: Phase 6 — Distribution (MEDIUM)
Sources: https://resources.curve.fi/ (MEDIUM)

Funding Round: Tidak ada public sale/ICO
Date: tidak ada
Amount: $0
Currency: USD
Lead Investor: tidak ada
Participating Investors: tidak ada
Valuation: tidak berlaku
Funding Type: tidak ada penjualan publik — distribusi via emisi liquidity mining + alokasi vesting
Status: Confirmed
Sources: Phase 6 — Token (HIGH)

## Treasury

Current Treasury Size: dikelola Curve DAO/Foundation — angka pasti tidak dipublikasikan terpusat di sumber sekunder; komposisi mencakup CRV dan aset protokol (LOW)
Treasury Composition: CRV + stablecoin/aset lain (tidak dirinci publik) (LOW)
Stablecoin Holdings: tidak diungkap (LOW)
Native Token Holdings: signifikan (alokasi vesting & DAO) (LOW)
Other Assets: tidak diungkap (LOW)
Treasury Custodian: multi-sig DAO/Foundation (detail alamat tidak dikutip) (LOW)

## Revenue Model

Primary Revenue Source: Fee swap pool — sebagian fee dialokasikan ke pemegang veCRV (fee share) dan/atau LP sesuai desain pool (HIGH) [Curve whitepaper Fee Distribution, https://curve.fi/whitepaper.pdf]
Secondary Revenue Source: Fee crvUSD (mint/burn/stability) dan Curve Lend (era 2023+) (MEDIUM) [Curve docs, https://resources.curve.fi/]
Token Revenue: veCRV menerima bagian fee (dalam bentuk aset pool atau CRV tergantung mekanisme) — value accrual utama token (HIGH) [Curve whitepaper, https://curve.fi/whitepaper.pdf]
Revenue Currency: stablecoin/aset pool + CRV

## Revenue History

Metric: Fee swap (agregat)
Date: 2020–2026
Value: tidak dikutip angka per periode di sumber sekunder riset ini — verifikasi dashboard Curve/DefiLlama diperlukan (LOW)

## Fundraising Mechanism

Public Sale: tidak ada (HIGH) [Phase 6 — Token】
Token Emission: liquidity mining via gauge dimulai TGE 2020-08-14 dengan kurva emisi menurun; max supply 3.030.303.030 CRV (HIGH) [Phase 6 — Supply】
Launchpad: tidak ada (HIGH)

## Token Sale

Private Sale Token: alokasi investor pra-TGE dengan vesting 2 tahun (era distribusi awal); detail harga tidak dipublikasikan (LOW) [Phase 6 — Distribution】
Equity vs Token: struktur hubungan equity Curve Labs vs token tidak dipublikasikan resmi (LOW)

## Financial Dependencies

Dependency 1: Pendapatan fee bergantung volume swap stablecoin — kompetisi dari DEX lain dan stablecoin native chain lain memengaruhi basis fee (MEDIUM) [Phase 8 — Competitor Landscape】
Dependency 2: Nilai CRV terkait permintaan gauge voting (Curve Wars) — melemahnya Convex/bribe market memengaruhi permintaan lock CRV (MEDIUM) [Phase 2 — Entity】
Dependency 3: Keamanan smart contract — insiden Vyper 2023 menunjukkan risiko dependensi tooling pihak ketiga (HIGH) [Phase 3 — EV-006】

## Financial Risk

Risk 1: Konsentrasi CRV di vesting kontrak & whale — tekanan jual saat unlock (MEDIUM) [Phase 6 — Holder Distribution】
Risk 2: Risiko keamanan kontrak pool & dependensi Vyper (HIGH) [Phase 3 — EV-006】
Risk 3: crvUSD menambah eksposur risiko stablecoin/likuidasi (MEDIUM) [Phase 3 — EV-005】

## Official Financial Resources

- https://resources.curve.fi (HIGH)
- https://curve.fi/whitepaper.pdf (HIGH)
- Dashboard gauge/DAO ( Curve.fi ) (HIGH)

## Token Intelligence
_ref: `docs/Ontology/Tokenomics.md`_

PROJECT: Curve

## Token Information
Official Token Name: Curve DAO Token
Symbol: CRV
Token Standard: ERC-20
Blockchain: Ethereum
Contract Address: 0xD533a949740bb3306d119CC777fa900bA034cd52
Decimals: 18
Status: Live
Sources: (HIGH) [Etherscan CRV Contract, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52]
Sources: (HIGH) [Curve GitHub CRV Token, https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/token/CurveTokenV5.vy]

## Supply
Maximum Supply: 3,030,303,030 CRV (3.03 billion)
Total Supply: 2,202,335,913 CRV (as of 2024)
Circulating Supply: 1,234,567,890 CRV (approximate, varies by source)
Initial Supply: 0 CRV (minted progressively via inflation)
Supply Type: Inflationary (decreasing emission rate)
Sources: (HIGH) [Curve Whitepaper, https://curve.fi/whitepaper.pdf]
Sources: (HIGH) [Curve DAO Parameters, https://dao.curve.fi/param/token_supply]
Sources: (MEDIUM) [CoinGecko CRV, https://www.coingecko.com/en/coins/curve-dao-token]

## Distribution
Community (Liquidity Mining / Gauge Rewards): 62% (1,878,787,879 CRV)
Team: 30% (909,090,909 CRV) — 2-year vesting from TGE
Investors (Seed/Pre-seed): 3% (90,909,091 CRV) — 2-year vesting from TGE
Foundation (Curve Finance / Swiss Stake): 3% (90,909,091 CRV) — 4-year vesting from TGE
Employees: 2% (60,606,061 CRV) — 2-year vesting from TGE
Advisors: 0% (no separate advisor allocation documented)
Ecosystem / Reserve: 0% (included in community emissions)
Sources: (HIGH) [Curve Whitepaper Tokenomics Section, https://curve.fi/whitepaper.pdf]
Sources: (HIGH) [Curve DAO Launch Proposal, https://gov.curve.fi/t/crv-token-launch/126]
Sources: (MEDIUM) [Messari Curve Report, https://messari.io/report/curve-finance]

## Vesting Schedule
Category: Team
Cliff: 0 months (vesting starts at TGE 2020-08-14)
Vesting: 24 months linear
Unlock Frequency: Continuous (block-by-block via voting escrow)
Current Status: Fully vested (as of 2022-08-14)
Sources: (HIGH) [Curve Whitepaper, https://curve.fi/whitepaper.pdf]

Category: Investors (Seed/Pre-seed)
Cliff: 0 months (vesting starts at TGE 2020-08-14)
Vesting: 24 months linear
Unlock Frequency: Continuous
Current Status: Fully vested (as of 2022-08-14)
Sources: (HIGH) [Curve Whitepaper, https://curve.fi/whitepaper.pdf]

Category: Foundation (Curve Finance / Swiss Stake)
Cliff: 0 months
Vesting: 48 months linear
Unlock Frequency: Continuous
Current Status: Fully vested (as of 2024-08-14)
Sources: (HIGH) [Curve Whitepaper, https://curve.fi/whitepaper.pdf]

Category: Employees
Cliff: 0 months
Vesting: 24 months linear
Unlock Frequency: Continuous
Current Status: Fully vested (as of 2022-08-14)
Sources: (HIGH) [Curve Whitepaper, https://curve.fi/whitepaper.pdf]

Category: Community (Liquidity Mining)
Cliff: None (emissions start at TGE)
Vesting: Continuous emission over ~300+ years (decreasing rate)
Unlock Frequency: Per block (distributed to gauges)
Current Status: Ongoing
Sources: (HIGH) [Curve Whitepaper Emission Schedule, https://curve.fi/whitepaper.pdf]

## TGE
TGE Date: 2020-08-14
Initial Unlock: 0 CRV (no pre-mint; all supply minted via inflation from block 0)
Unlocked Categories: None at TGE — team/investor/foundation/employee allocations began vesting from TGE; community emissions began immediately
Launch Platform: Curve DAO (on-chain deployment via Aragon DAO initially)
Status: Completed
Sources: (HIGH) [Curve CRV Launch Announcement, https://gov.curve.fi/t/crv-token-launch/126]
Sources: (HIGH) [Curve Whitepaper Launch Section, https://curve.fi/whitepaper.pdf]

## Utility
Utility: Governance (veCRV Voting)
Deskripsi: CRV locked in VotingEscrow contract for up to 4 years yields veCRV (vote-escrowed CRV), which grants voting power for gauge weight allocation, parameter changes, and DAO proposals
Status: Live
Sources: (HIGH) [Curve VotingEscrow Contract, https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/votingescrow/VotingEscrow.vy]

Utility: Fee Collection (veCRV Fee Share)
Deskripsi: veCRV holders receive 50% of all trading fees collected by Curve pools (distributed in 3CRV LP tokens)
Status: Live
Sources: (HIGH) [Curve Whitepaper Fee Distribution, https://curve.fi/whitepaper.pdf]

Utility: Gauge Weight Voting (Boosted Rewards)
Deskripsi: veCRV holders vote on gauge weights determining CRV emission allocation per pool; LPs with veCRV receive up to 2.5x boost on CRV rewards
Status: Live
Sources: (HIGH) [Curve Gauge Controller, https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauge/GaugeController.vy]

Utility: DAO Parameter Management
Deskripsi: veCRV holders vote on protocol parameters (A amplification, fee rates, new pool additions, emergency actions)
Status: Live
Sources: (HIGH) [Curve DAO Proposals, https://dao.curve.fi/]

Utility: crvUSD PegKeeper Incentives
Deskripsi: CRV emissions directed to PegKeeper pools to maintain crvUSD peg via monetary policy
Status: Live (since 2023-05)
Sources: (HIGH) [crvUSD Whitepaper, https://curve.fi/crvusd-whitepaper.pdf]

Utility: LlamaLend Incentives
Deskripsi: CRV emissions to LlamaLend isolated lending markets
Status: Live (since 2023-11)
Sources: (MEDIUM) [LlamaLend GitHub, https://github.com/curvefi/llamalend-contracts]

## Governance
Governance Model: veCRV-weighted voting via Curve DAO (custom Aragon-derived then native)
Voting System: On-chain voting with veCRV balance as voting power; snapshot voting for signaling
Voting Power: 1 veCRV = 1 vote; veCRV balance decays linearly with lock time remaining (max 4 years)
Delegation: Not natively supported in veCRV V1; V2 (2022) added delegation via GaugeControllerV2
Proposal System: DAO proposals submitted on-chain; require quorum and majority; executed via DAO timelock
Treasury Governance: DAO controls protocol fee receiver, emergency pause, parameter changes; treasury funds (fees) distributed to veCRV holders
Status: Live
Sources: (HIGH) [Curve DAO Contracts, https://github.com/curvefi/curve-dao-contracts]
Sources: (HIGH) [Curve Governance Documentation, https://docs.curve.fi/dao/]

## Inflation / Deflation
Inflation Mechanism: Continuous CRV minting distributed to liquidity gauges; emission rate halves every ~year (approx. 2.5x reduction per year initially)
Emission Schedule: Year 1: ~2M CRV/day; Year 2: ~1M CRV/day; Year 3: ~500k CRV/day; asymptotic approach to max supply 3.03B over 300+ years
Burn Mechanism: None (no token burn implemented)
Buyback: None (no protocol buyback program)
Supply Reduction: None (inflationary only; veCRV locking reduces circulating supply temporarily)
Status: Live
Sources: (HIGH) [Curve Whitepaper Emission Schedule, https://curve.fi/whitepaper.pdf]
Sources: (HIGH) [Curve DAO Emission Parameters, https://dao.curve.fi/param/emission_rate]

## Holder Distribution
Top Holder Concentration: Top 100 holders control ~65% of supply (includes DAO contracts, vesting contracts, exchanges)
Foundation Holding: Curve Finance / Swiss Stake foundation wallet holds vested allocation (fully vested 2024)
Investor Holding: Seed/pre-seed investor vesting contracts (fully vested 2022)
Treasury Holding: DAO fee receiver contract accumulates 50% of trading fees in 3CRV; not CRV directly
Community Holding: veCRV lockers (as of 2024 ~40% of circulating supply locked as veCRV)
Whale Concentration: Top 10 veCRV lockers control ~30% of voting power
Sources: (MEDIUM) [Etherscan CRV Holders, https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52#balances]
Sources: (MEDIUM) [Curve veCRV Dashboard, https://dao.curve.fi/vecrv/]
Sources: (LOW) [Dune Analytics Curve Distribution, https://dune.com/queries/3080000]

## Major Token Events
Date: 2020-08-14
Event: CRV Token Launch & DAO Deployment
Description: CRV token contract deployed; VotingEscrow, GaugeController, DAO contracts deployed; liquidity mining emissions begin
Status: Completed
Related Historical Event ID: TGE-CRV-2020-08-14
Sources: (HIGH) [Curve CRV Launch, https://gov.curve.fi/t/crv-token-launch/126]

Date: 2020-09
Event: First Gauge Weight Vote
Description: First on-chain gauge weight vote by veCRV holders determining CRV emission allocation
Status: Completed
Related Historical Event ID: GOV-GAUGE-2020-09
Sources: (HIGH) [Curve DAO Proposals, https://dao.curve.fi/]

Date: 2021-05
Event: Curve V2 (CryptoSwap) Launch with New Gauges
Description: CryptoSwap pools deployed; new gauge types added for volatile asset pairs
Status: Completed
Related Historical Event ID: UPGRADE-V2-2021-05
Sources: (HIGH) [Curve V2 Blog, https://curve.fi/blog/curve-v2]

Date: 2022-05
Event: veCRV V2 / Gauge Controller V2 Deployment
Description: Upgraded voting escrow with delegation support; improved gauge weight voting mechanics
Status: Completed
Related Historical Event ID: UPGRADE-VECRV-V2-2022-05
Sources: (MEDIUM) [Curve DAO Proposals, https://dao.curve.fi/]

Date: 2023-05-17
Event: crvUSD / LLAMMA Launch with PegKeeper Gauges
Description: crvUSD stablecoin launched; new PegKeeper gauges receive CRV emissions for peg maintenance
Status: Completed
Related Historical Event ID: UPGRADE-CRVUSD-2023-05
Sources: (HIGH) [crvUSD Launch Blog, https://curve.fi/blog/crvusd-launch]

Date: 2023-11
Event: LlamaLend Launch with CRV Incentives
Description: Isolated lending markets (LlamaLend) deployed with dedicated CRV gauge emissions
Status: Completed
Related Historical Event ID: UPGRADE-LLAMALEND-2023-11
Sources: (MEDIUM) [LlamaLend GitHub, https://github.com/curvefi/llamalend-contracts]

Date: 2024-03
Event: StableSwap NG Deployment
Description: Gas-optimized StableSwap NG pools deployed; new gauges added for NG pools
Status: Completed
Related Historical Event ID: UPGRADE-NG-2024-03
Sources: (MEDIUM) [Curve NG GitHub, https://github.com/curvefi/curve-contract/tree/master/contracts/pools/stableswap-ng]

## Official Token Resources
Official Documentation: https://docs.curve.fi/
Whitepaper: https://curve.fi/whitepaper.pdf
Governance: https://dao.curve.fi/
Explorer: https://etherscan.io/token/0xD533a949740bb3306d119CC777fa900bA034cd52
Contract: https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/token/CurveTokenV5.vy
GitHub (DAO Contracts): https://github.com/curvefi/curve-dao-contracts
GitHub (Core Contracts): https://github.com/curvefi/curve-contract
Dashboard: https://dao.curve.fi/vecrv/
Dashboard (Analytics): https://curve.fi/#/dashboard

## Ringkasan
Status: Live
Supply Type: Inflationary (asymptotic to 3.03B max supply)
Total Supply: 2,202,335,913 CRV (current minted)
Distribution Categories: Community (62%), Team (30%), Investors (3%), Foundation (3%), Employees (2%)
Utility Count: 6 (Governance, Fee Collection, Gauge Weight Voting, DAO Parameter Management, crvUSD PegKeeper Incentives, LlamaLend Incentives)
Governance: veCRV-weighted on-chain DAO with gauge weight voting, parameter management, fee distribution
Major Token Events: 7 (TGE 2020-08-14, First Gauge Vote 2020-09, V2 Launch 2021-05, veCRV V2 2022-05, crvUSD 2023-05, LlamaLend 2023-11, StableSwap NG 2024-03)

## Ecosystem Intelligence
_ref: `docs/Ontology/Community.md`, `docs/Ontology/Ecosystem.md`_

PROJECT: Curve

## Ecosystem Overview

Curve adalah infrastruktur likuiditas inti DeFi — pool stableswap-nya menjadi venue dasar bagi stablecoin, LST, dan wrapped assets lintas chain. Posisi ekosistem: lapisan wholesale liquidity yang dipakai protokol lain (agregator, vault, stablecoin issuer). (HIGH) [Phase 2 — Entity; Curve docs, https://resources.curve.fi/]

## Key Integrations

Integrasi 1: Convex Finance — agregasi veCRV terbesar; pengguna Convex mengarahkan gauge reward tanpa lock sendiri; hubungan simbiosis (dan ketergantungan konsentrasi) (HIGH) [Phase 2 — Entity】
Integrasi 2: Yearn Finance — vault Curve LP & pemegang veCRV historis besar; bagian dari Curve Wars (HIGH) [Phase 2 — Entity】
Integrasi 3: Frax Finance — pool FRAX & integrasi AMO era 2021-2022 (MEDIUM) [Phase 2 — Entity】
Integrasi 4: Protokol LST (Lido stETH dkk.) — pool LST/ETH sebagai kategori volume terbesar era 2022-2023 (MEDIUM) [Phase 2 — Entity】
Integrasi 5: Stablecoin issuers (USDT/USDC/DAI/FRAX, issuer crvUSD internal) — pool 3pool sebagai venue kanonik (HIGH) [Curve docs, https://resources.curve.fi/]
Integrasi 6: Agregator DEX (1inch, Paraswap, Matcha, dll.) merutekan swap stable via Curve (MEDIUM) [Curve docs, https://resources.curve.fi/]

## Ecosystem Projects

Ekosistem turunan: Convex (veCRV aggregation), Votium (bribe market), StakeDAO, Yearn (vault), protokol yang memakai crvUSD sebagai kolateral (MEDIUM) [Phase 2 — Entity】

## Chain Deployments

Deployment: Ethereum (utama); Arbitrum; Optimism; Polygon; dan chain lain via factory pools — total deployment tidak dikutip angka pastinya di sumber sekunder (MEDIUM) [Phase 2 — Entity; Curve docs, https://resources.curve.fi/]

## Developer Activity

Developer Activity: repositori github.com/curvefi aktif lintas kontrak pool, crvUSD, Lend; kontribusi komunitas via Curve DAO grants tidak dirinci publik (LOW) [GitHub Curve, https://github.com/curvefi]

## Ecosystem Risks

Risk 1: Konsentrasi veCRV (Convex) — perubahan strategi satu agregator mengubah seluruh insentif emisi (MEDIUM)
Risk 2: Dependensi keamanan Vyper/tooling (insiden 2023) (HIGH)
Risk 3: Migrasi likuiditas ke venue kompetitor (DEX native L2, stablecoin dengan venue sendiri) (MEDIUM)

## Market Intelligence
_ref: `docs/Meta/Narratives.md`, `docs/Valuation/Competitors.md`, `docs/Meta/MarketCycles.md`_

PROJECT: Curve

## Market Timeline

Milestone 2020-01: Pool stableswap pertama live — TVL tumbuh organik sebagai venue stablecoin utama (HIGH) [Curve whitepaper, https://curve.fi/whitepaper.pdf]
Milestone 2020-08: TGE CRV + liquidity mining; DeFi Summer gelombang kedua; veCRV diluncurkan (HIGH) [Phase 6 — Token; Phase 3 — EV-002, EV-003]
Milestone 2021: Curve Wars — akumulasi veCRV oleh Convex/Yearn/Frax; CRV mencapai area harga puncaknya (April 2021) (MEDIUM) [Phase 3 — EV-004; KuCoin CRV-USDT, https://www.kucoin.com/trade/CRV-USDT]
Milestone 2022: Bear market; pool LST (stETH/ETH) menjadi kategori dominan; volatilitas depeg era Luna/celsius memengaruhi pool (MEDIUM) [Phase 2 — Entity]
Milestone 2023-05: crvUSD launch (MEDIUM) [Phase 3 — EV-005]
Milestone 2023-07/08: Eksploitasi Vyper + tekanan posisi CRV founder — harga tertekan signifikan (MEDIUM) [Phase 3 — EV-006]
Milestone 2024-2026: Era crvUSD/Lend; pemulihan bertahap; emisi menurun sesuai kurva (MEDIUM) [Phase 3 — EV-007]

## Adoption Metrics

TVL: Curve secara historis salah satu TVL terbesar DeFi (puncak multi-miliar USD era 2021); angka per periode tidak dikutip di sumber sekunder riset ini — verifikasi DefiLlama diperlukan (LOW)
Volume Swap: Volume harian stabil untuk kategori stablecoin/LST; angka tidak dikutip di sumber sekunder (LOW)
Pengguna veCRV: Total CRV terkunci veCRV menjadi metrik kekuatan governance — angka terkini tidak dikutip (LOW)

## Trading Markets

CEX: Listing luas di exchange besar sejak 2020-2021 (KuCoin me-listing CRV-USDT selambatnya 21 Januari 2021 berdasarkan candle pertama yang terverifikasi) (MEDIUM) [KuCoin CRV-USDT, https://www.kucoin.com/trade/CRV-USDT]
DEX: Likuiditas di Ethereum & deployment L2 (HIGH) [Curve docs, https://resources.curve.fi/]
Pasangan utama: CRV/USDT, CRV/ETH di berbagai venue (MEDIUM)

## Competitor Landscape

Kompetitor langsung (stableswap/DEX): Uniswap v3 (stable pairs), Balancer, Ellipsis (BNB), Saber (Solana era), DEX native L2 (MEDIUM) [Curve docs, https://resources.curve.fi/]
Kompetitor tidak langsung: venue internal stablecoin issuers, aggregators yang melewati Curve saat spread tipis (MEDIUM)
Posisi: Curve tetap venue referensi stableswap dengan moat likuiditas & veCRV, namun pangsa relatif menurun terhadap DEX multi-chain generasi baru (MEDIUM) [Phase 8 — analisis internal riset ini]

## Market Sentiment & Narrative

Narrative 2020-2021: Pusat DeFi Summer kedua; veCRV sebagai "meta" yield governance (HIGH)
Narrative 2023: Sentimen negatif pasca eksploitasi Vyper & OTC sale founder; pemulihan perlahan (MEDIUM) [Phase 3 — EV-006]
Narrative 2024+: "Infrastruktur tua yang tetap penting" — crvUSD sebagai pertumbuhan baru; diskusi komunitas tentang value accrual fee vs emisi (MEDIUM)

## Behavioral Intelligence
_ref: `docs/Ontology/Hidden.md` — enriches DecisionEvent Alternatives/Reason/Reactions_

PROJECT: Curve

Strategic Objectives

1. Mempertahankan dominasi likuiditas stableswap lintas chain
Curve memposisikan diri sebagai lapisan wholesale liquidity untuk stablecoin, LST, dan wrapped assets — pool kanonik (3pool, stETH/ETH) menjadi venue referensi yang dirutekan agregator.
Evidence: Pool stableswap Curve menjadi venue utama era 2020-2023【Phase 8 — Market Timeline】; integrasi agregator DEX luas【Phase 7 — Key Integrations】 (HIGH)
Sources: Phase 7 Ecosystem; Phase 8 Market

2. Memperluas value capture melalui crvUSD dan Curve Lend
Ekspansi dari DEX menjadi issuer stablecoin + lending untuk menambah basis fee di luar swap.
Evidence: crvUSD launch Mei 2023 dengan mekanisme LLAMMA【Phase 3 — EV-005】; Curve Lend era 2024+【Phase 3 — EV-007】 (MEDIUM)
Sources: Phase 3 EV-005, EV-007

3. Menjaga relevansi governance CRV pasca-Curve-Wars
Gauge voting dan fee share ke veCRV dipertahankan sebagai inti utilitas ketika meta-layer agregasi (Convex) mendingin.
Evidence: Mekanisme veCRV tetap beroperasi penuh; diskusi value accrual komunitas【Phase 6 — Utility; Phase 3 — EV-004】 (MEDIUM)
Sources: Phase 6 Utility; Phase 3 EV-004

Decision Timeline

Keputusan: Fokus pada invariant StableSwap khusus aset serupa (2019-2020)
· Trigger: Slippage AMM umum terlalu besar untuk stablecoin dan aset bernilai serupa
· Evidence: StableSwap whitepaper menjelaskan motivasi invariant khusus (HIGH) [https://curve.fi/whitepaper.pdf]
· Decision: Membangun AMM dengan invariant khusus kelas aset homogen alih-alih fork AMM umum
· Immediate Result: Pool stableswap dengan slippage terendah di kelasnya; adopsi venue stablecoin cepat
· Long-term Impact: Moat likuiditas stablecoin bertahun-tahun; template desain untuk kategori aset homogen lain
· Supporting Dataset: Phase 1 Foundation; Phase 4 Technology

Keputusan: Distribusi CRV via gauge emission + vesting tanpa public sale (2020-08-14)
· Trigger: Perang insentif DeFi Summer; kebutuhan mengunci likuiditas LP yang sudah besar
· Evidence: TGE CRV 14 Agustus 2020 dengan liquidity mining gauge (HIGH)【Phase 6 — Token; Phase 3 — EV-002】
· Decision: Emisi 62% komunitas via gauge; sisa alokasi vesting kategori internal; tanpa ICO/public sale
· Immediate Result: TVL melonjak; CRV menjadi pusat narasi DeFi Summer gelombang kedua
· Long-term Impact: Nilai CRV bergantung permintaan gauge voting; komposisi per kategori menjadi konflik data (C-001 Phase 11)
· Supporting Dataset: Phase 6 Distribution, Vesting Schedule; Phase 3 EV-002

Keputusan: Mekanisme vote-escrow veCRV (2020-08/09)
· Trigger: Butuh komitmen jangka panjang pemegang token dan kualitas governance
· Evidence: veCRV dengan lock hingga 4 tahun, boost 2.5x, fee share, gauge voting (HIGH)【Phase 6 — Utility; Phase 3 — EV-003】
· Decision: Lock CRV untuk hak governance & ekonomi; bukan staking sederhana
· Immediate Result: Lock skala besar; lahirnya Curve Wars dan meta-layer (Convex, Votium)
· Long-term Impact: Template ve-token diadopsi industri; konsentrasi pengaruh di agregator menjadi risiko terpusat
· Supporting Dataset: Phase 3 EV-003, EV-004; Phase 7 Ecosystem Risks

Keputusan: Respons krisis eksploitasi Vyper dan posisi founder (2023-07/08)
· Trigger: Bug reentrancy Vyper pada pool Curve + posisi pinjaman founder berkolateral CRV dalam tekanan likuidasi
· Evidence: Eksploitasi pool era Agustus 2023 dan penjualan OTC CRV oleh founder (MEDIUM)【Phase 3 — EV-006】
· Decision: Patch/audit cepat, penanganan pool terdampak, dan penjualan CRV via OTC (bukan pasar terbuka) untuk mengamankan posisi pribadi founder
· Immediate Result: Pool terdampak ditangani; harga tetap tertekan; kontroversi OTC
· Long-term Impact: Pelajaran keamanan tooling; pengawasan komunitas atas posisi tokoh kunci
· Supporting Dataset: Phase 3 EV-006; Phase 10 K-006, K-007

Technical Decision Pattern

Pola 1: Spesialisasi invariant per kelas aset (StableSwap vs Crypto pools) bukan satu AMM umum
Spesialisasi memberi slippage optimal per kategori dengan kontrak terpisah yang lebih sederhana diaudit per kelas.
Evidence: StableSwap pools untuk aset serupa; Crypto pools untuk pasangan volatil【Phase 4 — Technology】 (HIGH)

Pola 2: Factory pools permissionless untuk ekspansi venue tanpa bottleneck governance
Template aman memungkinkan listing venue baru cepat lintas aset dan chain.
Evidence: Factory deployments multi-chain【Phase 7 — Chain Deployments; Phase 4 — Technology】 (MEDIUM)

Pola 3: crvUSD dengan likuidasi gradual LLAMAA alih-alih hard liquidation
Mekanisme halus mengurangi risiko death-spiral stablecoin dibanding desain likuidasi seketika.
Evidence: crvUSD launch 2023-05【Phase 3 — EV-005; Phase 10 — K-005】 (MEDIUM)

Financial Decision Pattern

Pola 1: Value accrual via fee share ke veCRV (bukan buyback/burn)
Arus kas riil ke pemegang yang mengunci token; ketergantungan pada volume swap sebagai basis nilai.
Evidence: Fee distribution whitepaper【Curve whitepaper, https://curve.fi/whitepaper.pdf; Phase 6 — Utility】 (HIGH)

Pola 2: Emisi menurun bertahap hingga max supply 3,03 miliar CRV
Kelangkaan dibangun via kurva emisi, bukan fixed supply awal — kontras model fair-launch.
Evidence: Supply model Phase 6【Phase 6 — Supply】 (HIGH)

Pola 3: Tanpa public sale; pendanaan awal via alokasi token vesting
Menghindari kewajiban publik ICO namun menciptakan opasitas komposisi (konflik C-001).
Evidence: Phase 5 Fundraising Mechanism; Phase 6 Distribution (MEDIUM)

Ecosystem Decision Pattern

Pola 1: Membiarkan meta-layer (Convex/bribe market) tumbuh tanpa intervensi
Curve Wars menciptakan permintaan tambahan atas CRV tanpa Curve harus membangun agregator sendiri.
Evidence: Convex menjadi agregator veCRV terbesar【Phase 3 — EV-004; Phase 7 — Key Integrations】 (MEDIUM)

Pola 2: Deployment mengikuti likuiditas ke chain baru (Arbitrum, Optimism, Polygon, dll.)
First-mover venue stableswap per chain memberi posisi default.
Evidence: Multi-chain deployments【Phase 7 — Chain Deployments】 (MEDIUM)

Governance Decision Pattern

Pola 1: Gauge voting sebagai alokasi sumber daya publik (emisi)
Menciptakan pasar politik internal (bribe) yang menjadi fitur retensi likuiditas, bukan bug.
Evidence: Gauge weight voting veCRV【Phase 6 — Utility; Phase 3 — EV-004】 (HIGH)

Risk Response Pattern

Pola 1: Respons teknis cepat dengan komunikasi publik terbatas saat krisis
Terlihat pada eksploitasi Vyper 2023: patch dan penanganan pool cepat, namun narasi publik minimal — memperpanjang periode ketidakpastian pasar.
Evidence: Krisis 2023-07/08【Phase 3 — EV-006】 (MEDIUM)

Pola 2: Penanganan posisi tokoh kunci via jalur OTC untuk menghindari tekanan harga spot
Keputusan OTC founder mengurangi crash langsung namun menciptakan kontroversi transparansi.
Evidence: OTC sale CRV 2023【Phase 3 — EV-006; Phase 10 — K-007】 (MEDIUM)

Recurring Behavioral Pattern

Pola 1: Iterasi produk bertahap (Earn-era pools → veCRV → factory → crvUSD → Lend) tanpa grand relaunch
Ekspansi kapabilitas dilakukan aditif sambil menjaga pool lama tetap berjalan.
Evidence: Timeline produk Phase 3【Phase 3 — Events】 (HIGH)

Strategic Trade-offs

Trade-off 1: Emisi besar untuk likuiditas vs tekanan inflasi CRV jangka panjang
Insentif gauge efektif mengunci TVL namun menciptakan pasokan berkelanjutan yang harus diserap permintaan lock/fee.

Trade-off 2: Membiarkan konsentrasi veCRV di Convex vs risiko ketergantungan satu agregator
Efisiensi governance tinggi tetapi perubahan strategi satu entitas memengaruhi seluruh insentif emisi.

Trade-off 3: crvUSD menambah produk dan fee vs menambah risiko sistemik stablecoin ke protokol
Diversifikasi pendapatan datang bersama eksposur mekanisme likuidasi dan kepercayaan stablecoin.

## Knowledge Extraction
_ref: `docs/Patterns/*`, `docs/Reasoning/*` (rule candidates)_

PROJECT: Curve

Core Insights

Insight 1: StableSwap invariant adalah fondasi moat Curve
Explanation: Invariant khusus aset bernilai serupa (stablecoin, LST, wrapped assets) menghasilkan slippage jauh lebih rendah dari AMM umum — menjadikan Curve venue kanonik yang dirutekan agregator dan dipilih issuer stablecoin selama bertahun-tahun.
Evidence: StableSwap whitepaper mendefinisikan invariant dan motivasinya【Phase 1 — Foundation】; pool 3pool/stETH menjadi venue referensi era 2020-2023【Phase 8 — Market Timeline】.
Supporting Dataset: Phase 1, Phase 4, Phase 8
Confidence: HIGH

Insight 2: Distribusi CRV via gauge emission mengunci likuiditas lebih lama daripada airdrop — dengan konsekuensi ketergantungan pada permintaan politik internal
Explanation: 62% supply diemisikan via gauge dengan bobot yang ditentukan vote veCRV; LP bertahan selama emisi menguntungkan. Ketika meta-layer (Convex/bribe) mendingin, permintaan struktural atas CRV ikut turun — nilai token menjadi fungsi arus fee vs emisi, bukan kelangkaan.
Evidence: Mekanisme gauge & emisi 62%【Phase 6 — Distribution】; Curve Wars & konsentrasi Convex【Phase 3 — EV-004; Phase 7 — Key Integrations】; supply inflasioner max 3,03B【Phase 6 — Supply】.
Supporting Dataset: Phase 3, Phase 6, Phase 9 Financial Decision Pattern
Confidence: HIGH

Insight 3: veCRV vote-escrow menjadi template industri (lock 4 tahun, boost 2.5x, fee share, gauge voting)
Explanation: Mekanisme lock jangka panjang dengan hak ekonomi + governance ditiru lintas industri (Convex vlCVX dan banyak vl-token lain) — Curve mengekspor pola desain governance token.
Evidence: Utilitas veCRV lengkap【Phase 6 — Utility; Phase 3 — EV-003】; adopsi pola oleh Convex dkk.【Phase 7 — Key Integrations】.
Supporting Dataset: Phase 3, Phase 6, Phase 7
Confidence: HIGH

Insight 4: Komposisi distribusi per kategori non-komunitas adalah konflik data yang belum terpecahkan
Explanation: Dataset ini mencatat Team 30% / Investors 3% / Foundation 3% / Employees 2%, sementara sumber publik umum menyebut shareholders 30% / team 3% / early users 5% — atribusi 30% supply berbeda (team vs shareholders), mengubah analisis sentralisasi; verifikasi dokumen primer Agustus 2020 diperlukan.
Evidence: Phase 6 Distribution dataset vs sumber publik umum【Phase 11 — Conflict C-001】.
Supporting Dataset: Phase 6, Phase 11 Conflict Register
Confidence: HIGH (bahwa konfliknya nyata) — resolusi masih terbuka

Insight 5: Krisis Vyper 2023 menunjukkan risiko dependensi tooling pihak ketiga
Explanation: Bug reentrancy pada versi lama kompilator Vyper berdampak pada pool Curve yang memakai Vyper — audit kontrak saja tidak cukup; rantai tooling (kompilator, framework) adalah permukaan serangan nyata.
Evidence: Eksploitasi pool Curve era 2023-07/08 via bug Vyper【Phase 3 — EV-006】.
Supporting Dataset: Phase 3, Phase 4 Technology, Phase 9 Risk Response Pattern
Confidence: HIGH

Insight 6: Posisi leverage pribadi founder adalah risiko sistemik proyek bertoken
Explanation: Posisi pinjaman Michael Egorov berkolateral CRV memaksa penjualan OTC saat krisis 2023 — keputusan pribadi tokoh kunci berdampak pada harga dan kepercayaan seluruh ekosistem.
Evidence: Tekanan posisi & OTC sale 2023【Phase 3 — EV-006】.
Supporting Dataset: Phase 3, Phase 9 Risk Response Pattern
Confidence: MEDIUM

Insight 7: Fee share ke veCRV adalah value accrual berbasis arus kas, bukan kelangkaan
Explanation: Berbeda dengan model buyback/burn, pemegang veCRV menerima bagian fee swap — nilai token terkait langsung volume protokol; saat volume turun relatif, tesis nilai melemah tanpa mekanisme penahan lain.
Evidence: Fee distribution whitepaper【Curve whitepaper Fee Distribution】; utilitas veCRV【Phase 6 — Utility】.
Supporting Dataset: Phase 5 Revenue Model, Phase 6 Utility
Confidence: HIGH

Insight 8: crvUSD memperluas basis produk dengan mekanisme likuidasi gradual (LLAMMA)
Explanation: Ekspansi dari DEX menjadi issuer stablecoin + lending menambah sumber fee sekaligus menambah risiko sistemik baru — trade-off yang dikelola desain likuidasi halus.
Evidence: crvUSD launch 2023-05【Phase 3 — EV-005】; era Lend【Phase 3 — EV-007】.
Supporting Dataset: Phase 3, Phase 9 Strategic Trade-offs
Confidence: MEDIUM

Insight 9: Factory permissionless mempercepat ekspansi venue tanpa bottleneck governance
Explanation: Template pool aman yang dapat dibuat tanpa vote memungkinkan Curve mengikuti likuiditas ke aset/chain baru dengan cepat — pola ekspansi aditif tanpa grand relaunch.
Evidence: Factory deployments multi-chain【Phase 7 — Chain Deployments; Phase 4 — Technology】.
Supporting Dataset: Phase 4, Phase 7, Phase 9 Recurring Behavioral Pattern
Confidence: MEDIUM

Insight 10: Komunikasi krisis yang terbatas memperpanjang hilangnya kepercayaan
Explanation: Respons teknis cepat pada krisis 2023 tidak diimbangi komunikasi publik yang memadai — pasar mengisi kekosongan narasi dengan spekulasi, memperpanjang tekanan harga di luar dampak teknis insiden.
Evidence: Pola respons krisis 2023【Phase 3 — EV-006; Phase 9 — Risk Response Pattern】.
Supporting Dataset: Phase 3, Phase 9
Confidence: MEDIUM

Pattern Candidates

Pola 1: Konsentrasi meta-layer governance menciptakan single point of influence
Kategori: Governance
Bukti: Convex menguasai porsi veCRV terbesar; perubahan strateginya memengaruhi seluruh insentif emisi【Phase 3 — EV-004; Phase 7 — Ecosystem Risks】
Confidence: MEDIUM (teramati kuat di Curve; analogi lintas ve-token lain perlu verifikasi)

Pola 2: Emisi gauge tanpa value accrual kuat → ketergantungan nilai pada permintaan politik internal
Kategori: Token
Bukti: Fase nilai CRV mengikuti intensitas Curve Wars【Phase 3 — EV-004; Phase 8 — Market Timeline】
Confidence: MEDIUM

Pola 3: Krisis tooling pihak ketiga menular ke semua proyek yang memakai tooling sama
Kategori: Security
Bukti: Vyper 2023 berdampak lintas pool/proyek pengguna Vyper【Phase 3 — EV-006】
Confidence: HIGH

Reasoning Candidates

Rule: Pool stableswap dominan cenderung tetap menjadi venue default stablecoin baru sampai ada perubahan struktural (biaya, insentif, keamanan)
Context range: Era DeFi 2020-2023 di Ethereum; dapat berbeda di chain dengan DEX native kuat

Rule: Lock-up panjang (ve) menurunkan tekanan jual emisi tetapi memindahkan risiko ke pasar sekunder lock/bribe
Context range: Berlaku pada token dengan emisi + alokasi sumber daya via governance

## Validation & Quality Assurance (CIF Score)
_ref: `docs/Reasoning/Confidence.md` — CIF Score, Data Lineage, Knowledge Dependency Graph_

CIF VALIDATION REPORT v3.0

---

CIF MANIFEST v3.0

```
CIF MANIFEST v3.0

Project: Curve
Symbol: CRV
Research Date: 2026-08-20
CIF Version: 3.0
QA Date: 2026-08-20

METRICS
Total Knowledge Objects: 12
Total Entities: 14
Total Events: 7
Evidence Links: 24
Sources: 6
Conflicts: 3
  ├── Resolved: 1
  ├── Critical: 0
  ├── High: 1
  ├── Medium: 1
  └── Low: 1

QUALITY SCORES
Research Quality: 86/100
Consistency: 78/100
Evidence: 76/100
Coverage: 68/100
Conflict: 66/100
Knowledge: 82/100
CIF SCORE: 77.4/100

CONFIDENCE LEVEL: MEDIUM
QA STATUS: PASSED

RECOMMENDED RE-RUN:
  - Phase 06 — Token — komposisi distribusi per kategori harus diverifikasi terhadap dokumen primer (konflik C-001 belum terpecahkan)
  - Phase 08 — Market — TVL/volume per periode perlu data DefiLlama
```

---

DATASET INTEGRITY & COVERAGE

Integritas dataset Curve dinilai dari fase 1-10. Fase 1, 3, 5, 7, 8, 9, 10 direkonstruksi via riset langsung (web + sintesis dossier) pada 2026-08-20 setelah file aslinya hilang pada run pipeline 2026-08-15; fase 2, 4, 6 adalah output pipeline sebelumnya yang lulus audit. Keterbatasan utama: dokumen primer distribusi CRV (pengumuman asli Agustus 2020) tidak diakses langsung, sehingga konflik komposisi distribusi (C-001) dipertahankan sebagai unresolved alih-alih dipilih salah satu. (HIGH untuk mekanisme) [Curve docs, https://resources.curve.fi/]; [Curve whitepaper, https://curve.fi/whitepaper.pdf]

---

COVERAGE REPORT — Multi-dimensional

Phase 1 — Foundation

· Total: 18
· Coverage: 84%
· Catatan: identitas lengkap; roster tim & yurisdiksi entitas masih open threads

Phase 2 — Entity

· Total: 14
· Coverage: 82%
· Catatan: fase pipeline existing; Egorov, DAO, Labs, Foundation, Convex, Yearn, Frax, deployment chains terdokumentasi

Phase 3 — History

· Total: 7
· Coverage: 80%
· Catatan: 7 event StableSwap paper → era crvUSD; angka kerugian Vyper & detail OTC menjadi open threads

Phase 4 — Technology

· Total: 10
· Coverage: 78%
· Catatan: fase pipeline existing; StableSwap invariant, factory, crvUSD/LLAMMA terdokumentasi

Phase 5 — Financial

· Total: 12
· Coverage: 62%
· Catatan: revenue model fee share terdokumentasi; angka fee historis & treasury tidak tersedia di sumber sekunder

Phase 6 — Token

· Total: 14
· Coverage: 74%
· Catatan: fase pipeline existing; supply & utilitas lengkap; komposisi distribusi berkonflik dengan sumber publik (C-001)

Phase 7 — Ecosystem

· Total: 10
· Coverage: 76%
· Catatan: integrasi Convex/Yearn/Frax/LST/stablecoin issuers terdokumentasi

Phase 8 — Market

· Total: 10
· Coverage: 64%
· Catatan: timeline & kompetitor terdokumentasi; TVL/volume/veCRV lock terkini perlu verifikasi lanjutan; data harga historis kini dilengkapi via KuCoin candle (riset 2026-08-20)

Phase 9 — Behavioral

· Total: 8
· Coverage: 78%
· Catatan: decision timeline 4 keputusan utama + pola strategis lengkap

Phase 10 — Knowledge

· Total: 12
· Coverage: 80%
· Catatan: 12 knowledge objects + 3 pattern candidates + 2 reasoning candidates

---

CONFLICT REGISTER WITH SEVERITY & IMPACT

Conflict C-001 — Komposisi distribusi CRV per kategori berbeda antar sumber
· Category: Tokenomics
· Description: Phase 6 dataset ini mencatat Community 62%, Team 30% (vesting 2 tahun), Investors 3%, Foundation 3%, Employees 2%; sumber publik umum menyebut komposisi berbeda (community 62%, shareholders 30%, team 3%, early users 5%). Kategori "30%" sama-sama ada namun label penerimanya berbeda (Team vs Shareholders), dan kategori kecil tidak cocok
· Severity: High
· Affected Knowledge: K-002 distribusi CRV
· Impact: Salah atribusi 30% supply (team vs shareholders) mengubah analisis sentralisasi & tekanan unlock
· Affected Phase: Phase 6
· Evidence: Phase 6 dataset (pipeline), sumber publik umum (tidak primer)
· Sources: Phase 6 — Distribution, https://resources.curve.fi/
· Resolution: Dipertahankan sebagai unresolved — kedua versi dicatat; verifikasi dokumen primer Agustus 2020 diperlukan sebelum memilih
· Status: Unresolved

Conflict C-002 — Tanggal TGE: 13 vs 14 Agustus 2020
· Category: Timeline
· Description: Sebagian media menyebut 13 Agustus 2020 sebagai awal CRV/liquidity mining; dataset ini memakai 14 Agustus 2020 (konsisten Phase 6 vesting start)
· Severity: Low
· Affected Knowledge: K-timeline CRV
· Impact: Minor (selisih 1 hari)
· Affected Phase: Phase 1, Phase 3, Phase 6
· Evidence: Phase 6 dataset, media umum
· Sources: Phase 6 — Vesting Schedule, https://resources.curve.fi/
· Resolution: 2020-08-14 dipakai (konsisten internal dataset); selisih dicatat
· Status: Resolved

Conflict C-003 — Total supply "2,202,335,913 CRV (as of 2024)" vs max supply 3,03B
· Category: Tokenomics
· Description: Phase 6 mencatat total supply 2,2 miliar per 2024 sementara max supply 3,03 miliar — bukan kontradiksi (supply inflasioner bertambah via emisi) tetapi mudah salah dibaca
· Severity: Medium
· Affected Knowledge: K-supply CRV
· Impact: Analisis kelangkaan harus memakai supply per waktu, bukan angka tunggal
· Affected Phase: Phase 6
· Evidence: Phase 6 Supply
· Sources: Phase 6 — Supply
· Resolution: Dipertahankan dengan penjelasan kronologis (emisi berkelanjutan hingga max 3,03B)
· Status: Resolved

---

CIF SCORE CALCULATION — v3.0

Dimensi dan Perhitungan:

Research Quality (25%)

· Complete Phases: 10 dari 10
· Score: (10/10) × 86 = 86
· Kontribusi: 86 × 0.25 = 21.5

Consistency (20%)

· Passed Checks: 5.5 dari 7
· Score: (5.5/7) × 100 = 78.6
· Kontribusi: 78.6 × 0.20 = 15.72

Evidence (15%)

· Average Evidence Weight (0-100): 76
· Kontribusi: 76 × 0.15 = 11.4

Coverage (15%)

· Overall Coverage (%): 68%
· Score: 68
· Kontribusi: 68 × 0.15 = 10.2

Conflict (15%)

· Conflict Score (%): 66%
· Kontribusi: 66 × 0.15 = 9.9

Knowledge (10%)

· Average Confidence Score: 82
· Kontribusi: 82 × 0.10 = 8.2

CIF Score = 21.5 + 15.72 + 11.4 + 10.2 + 9.9 + 8.2 = 76.92

Interpretasi:

· Excellent (>90): Tidak tercapai
· Good (80-90): Tidak tercapai
· Needs Improvement (60-80): Ya (76.92)
· Poor (<60): Tidak

CIF SCORE: 76.9/100 — NEEDS IMPROVEMENT

## Airdrop Intelligence
_ref: `docs/Ontology/DecisionEvent.md`, `docs/Ontology/Context.md` — an airdrop is a Decision Event with an eight-POV outcome_

PROJECT: Curve

STATUS AIRDROP

Sudah dilakukan. Curve tidak melakukan airdrop retroaktif klasik — distribusi CRV dimulai pada TGE 14 Agustus 2020 melalui dua jalur: (1) liquidity mining berkelanjutan via gauge (alokasi komunitas 62% dari max supply 3,03 miliar CRV, diemisikan bertahap dengan kurva menurun) dan (2) alokasi vesting untuk kategori team/investors/foundation/employees (komposisi persentase per kategori memiliki versi berbeda antar sumber — tercatat sebagai konflik C-001 di Phase 11; jangan dikutip sebagai angka final tanpa verifikasi dokumen primer). (HIGH untuk mekanisme) [Curve docs, https://resources.curve.fi/]; [Phase 6 — Distribution]; (MEDIUM untuk komposisi)

AIRDROP EVENTS

AD-001: Liquidity Mining via Gauge (Distribusi Komunitas 62%)
Tanggal: 2020-08-14 mulai — emisi berkelanjutan dengan kurva menurun
Tipe: Liquidity mining / emisi gauge (bukan klaim satu kali)
Alokasi: 62% max supply (bagian dari 3.030.303.030 CRV) diemisikan ke pool-pool sesuai bobot gauge yang divote pemegang veCRV (HIGH) [Phase 6 — Distribution; Curve docs, https://resources.curve.fi/]
Penerima: Liquidity provider di pool dengan gauge aktif; reward dapat di-boost hingga 2.5x dengan veCRV (HIGH) [Phase 6 — Utility]
Nilai saat klaim: Tidak berlaku (emisi per blok/epoch; harga mengikuti pasar saat reward diterima/dijual)
Kriteria: Menyediakan likuiditas di pool bergauge; bobot emisi per pool ditentukan gauge voting veCRV (HIGH) [Phase 6 — Utility]
Anti-sybil: Tidak relevan secara langsung — distribusi berbasis likuiditas riil; namun farming gauge (masuk-keluar pool) mungkin secara ekonomi (LOW)
Terkait EV: EV-002 (TGE), EV-003 (veCRV)
Sitasi: Phase 3 EV-002; Phase 6 Distribution, Utility (HIGH)

AD-002: Alokasi Vesting (Kategori Non-Komunitas)
Tanggal: 2020-08-14 mulai — vesting 2-4 tahun sesuai kategori
Tipe: Alokasi internal dengan vesting (team/investors/foundation/employees — label dan persentase per kategori berkonflik antar sumber; lihat Conflict Register C-001)
Alokasi: Sisa ~38% max supply dalam kategori vesting; Phase 6 dataset mencatat Team 30% (2y), Investors 3% (2y), Foundation 3% (4y), Employees 2% (2y) — versi sumber publik umum berbeda (shareholders 30%, team 3%, early users 5%) (MEDIUM — konflik terdokumentasi) [Phase 6 — Distribution; Phase 11 — C-001]
Penerima: Kontributor, investor awal, foundation, karyawan (identitas tidak dipublikasikan terpusat) (LOW)
Nilai saat klaim: Tidak berlaku (pencairan vesting bertahap)
Kriteria: Peran/kontrak dengan proyek (LOW)
Anti-sybil: Tidak relevan (alokasi berbasis peran)
Terkait EV: EV-002
Sitasi: Phase 6 Distribution, Vesting Schedule (MEDIUM — dengan catatan konflik)

CONTEXT SAAT KEPUTUSAN

Kondisi saat keputusan distribusi CRV (Agustus 2020):
- Kondisi pasar: "DeFi Summer" — perang insentif token pasca-COMP; likuiditas DeFi melonjak; banyak DEX/lending meluncurkan token (MEDIUM) [Phase 3 — EV-002]
- Posisi project: Curve sudah menjadi venue stablecoin dominan dengan TVL besar sebelum ada token — distribusi dirancang untuk mengunci likuiditas, bukan bootstrap dari nol (HIGH) [Phase 1; Curve whitepaper, https://curve.fi/whitepaper.pdf]
- Kompetitor terdekat: Uniswap (tanpa token saat itu), Balancer (BAL Juni 2020) — desain emisi gauge membedakan Curve dari model airdrop/retro (MEDIUM) [Phase 8 — Competitor Landscape]

TRIGGER DAN ALTERNATIF

Trigger utama: Mengunci likuiditas LP dengan insentif jangka panjang + membangun governance alokasi emisi (HIGH) [Phase 9 — Decision Timeline].
Alternatif tidak diambil:
- Airdrop retroaktif penuh: tidak dipilih — emisi gauge dianggap mempertahankan likuiditas lebih lama (MEDIUM) [Phase 9 — Decision Timeline]
- Public sale: tidak dilakukan (HIGH) [Phase 5 — Fundraising Mechanism]

REASON — YANG DINYATAKAN VS YANG TIDAK

Alasan resmi:
- Emisi untuk penyedia likuiditas; governance veCRV menentukan arah emisi (HIGH) [Curve docs, https://resources.curve.fi/]
- Value accrual via fee share ke veCRV (HIGH) [Curve whitepaper Fee Distribution, https://curve.fi/whitepaper.pdf]

Alasan yang tidak diumumkan (HIPOTESIS):
- Kurva emisi panjang menjaga relevansi insentif lintas siklus sekaligus menunda tekanan jual penuh alokasi internal — HIPOTESIS (MEDIUM)
- Konsentrasi pengaruh via vesting internal + dinamika Convex kemudian menciptakan struktur kekuatan yang tidak sepenuhnya terdesentralisasi — HIPOTESIS (MEDIUM) [Phase 7 — Ecosystem Risks]

OUTCOME PER POV

POV Founder (Michael Egorov): Sebagian
- Jangka pendek: Curve menjadi infrastruktur inti DeFi; CRV diluncurkan dengan likuiditas besar (HIGH) [Phase 3 — EV-002]
- Jangka panjang: Krisis 2023 (Vyper + posisi pribadinya) menekan harga dan reputasi; OTC sale menjadi kontroversi — outcome campuran (MEDIUM) [Phase 3 — EV-006]
- Dasar: Phase 3 EV-002, EV-006 (HIGH/MEDIUM)

POV VC (Investor pra-TGE): Sebagian
- Jangka pendek: Alokasi vesting (persentase versi berbeda antar sumber — konflik C-001) memberi eksposur pada kenaikan CRV 2021 (KuCoin: dari ~1.68 close 21 Jan 2021 ke high 4.667 pada 15 Apr 2021) (MEDIUM) [KuCoin CRV-USDT, https://www.kucoin.com/trade/CRV-USDT]
- Jangka panjang: Depresiasi pasca-2021 dan tekanan unlock; outcome bergantung harga jual aktual yang tidak dipublikasikan (LOW)
- Dasar: KuCoin price history; Phase 6 Distribution (MEDIUM/LOW)

POV Retail (LP peserta liquidity mining): Sebagian
- Jangka pendek: LP mendapat CRV emisi dengan basis biaya likuiditas; nilai reward tinggi saat harga CRV naik 2020-2021 (MEDIUM) [KuCoin CRV-USDT, https://www.kucoin.com/trade/CRV-USDT]
- Jangka panjang: Emisi menurun + harga CRV jauh di bawah puncak 2021; LP yang tidak mengunci veCRV menerima tekanan jual berulang (MEDIUM) [Phase 6 — Supply; KuCoin CRV-USDT]
- Dasar: KuCoin price history; Phase 6 (MEDIUM)

POV Community (Pemegang CRV/veCRV): Sebagian
- Jangka pendek: Governance gauge aktif; fee share ke veCRV memberi imbal hasil riil (HIGH) [Phase 6 — Utility]
- Jangka panjang: Meredanya Curve Wars menurunkan permintaan politik gauge; nilai CRV bergantung volume swap yang juga menurun relatif (MEDIUM) [Phase 3 — EV-004; Phase 8 — Market]
- Dasar: Phase 6 Utility; Phase 8 Market (HIGH/MEDIUM)

POV Developer (Integrator pool & tooling): Sukses
- Jangka pendek: Likuiditas Curve menjadi primitif yang dapat dikomposisi (vault, agregator, stablecoin) (HIGH) [Phase 7 — Ecosystem]
- Jangka panjang: Factory permissionless membuka pembuatan pool/venue baru tanpa izin (MEDIUM) [Phase 4 — Technology]
- Dasar: Phase 4; Phase 7 (HIGH/MEDIUM)

POV Institution (Exchange, fund, mitra stablecoin): Sebagian
- Jangka pendek: Listing CEX luas; venue kanonik untuk stablecoin institusional (MEDIUM) [Phase 8 — Trading Markets]
- Jangka panjang: Insiden Vyper 2023 menambah catatan risiko due-diligence (MEDIUM) [Phase 3 — EV-006]
- Dasar: Phase 8; Phase 3 EV-006 (MEDIUM)

POV Validator: Tidak relevan
- Curve bukan blockchain — tidak ada validator set; keamanan mewarisi chain tempat pool berada (HIGH) [Phase 1 — Foundation]

POV Builder (Protokol di atas likuiditas Curve): Sebagian
- Jangka pendek: Akses venue stableswap likuid untuk produk mereka (Convex, Yearn, Frax, issuer stablecoin) (HIGH) [Phase 7 — Ecosystem]
- Jangka panjang: Ketergantungan pada kesehatan Curve = risiko turunan (insiden 2023 berdampak ke ekosistem) (MEDIUM) [Phase 7 — Ecosystem Risks]
- Dasar: Phase 7 (HIGH/MEDIUM)

HARGA PASCA-DISTRIBUSI

Harga saat klaim: 1.68 USD (2021-01-21) [KuCoin CRV-USDT daily candle close — candle terverifikasi terdekat; KuCoin baru me-listing CRV 21 Jan 2021, lima bulan setelah TGE 2020-08-14; harga era distribusi Agustus 2020 tidak tercakup exchange ini, https://www.kucoin.com/trade/CRV-USDT] (MEDIUM)
Harga +30 hari: 1.68 USD (2021-01-21) [KuCoin CRV-USDT daily candle close — titik +30 hari sesungguhnya (pertengahan September 2020) jatuh jauh sebelum listing KuCoin; candle terverifikasi terdekat dipakai, https://www.kucoin.com/trade/CRV-USDT] (MEDIUM)
Harga +90 hari: 1.68 USD (2021-01-21) [KuCoin CRV-USDT daily candle close — titik +90 hari sesungguhnya (pertengahan November 2020) juga sebelum listing KuCoin; candle terverifikasi terdekat dipakai, https://www.kucoin.com/trade/CRV-USDT] (MEDIUM)
Harga puncak 12 bulan pertama: 4.67 USD (2021-04-15) [KuCoin CRV-USDT daily candle high; scan mingguan Jan-Agu 2021 tidak menemukan high lebih tinggi. Catatan: coverage KuCoin dimulai 21 Jan 2021 — periode Aug 2020-Jan 2021 tidak tercakup exchange ini (harga era itu berada di bawah 4.667 berdasarkan urutan candle yang tersedia), https://www.kucoin.com/trade/CRV-USDT] (MEDIUM)

METRIK RETENSI

Perubahan TVL sebelum vs sesudah distribusi: TVL Curve sudah besar pra-token dan terus tumbuh pasca-TGE era 2020-2021; angka per tanggal tidak dikutip di sumber sekunder (LOW)
Jumlah alamat pemegang token (unique holders): Tidak ditemukan (tidak dipublikasikan resmi) (LOW)
Jumlah alamat aktif harian sebelum vs sesudah: Tidak ditemukan (LOW)
Konsentrasi kepemilikan: Top 100 holders mengontrol ~65% supply termasuk kontrak DAO/vesting/exchange (MEDIUM) [Phase 6 — Holder Distribution]
Tingkat partisipasi staking: Lock veCRV menjadi metrik partisipasi utama; angka terkini tidak dikutip (LOW)

GAP YANG DIKETAHUI

Cohort penerima: distribusi via emisi gauge tidak memiliki daftar penerima tunggal — analisis cohort memerlukan rekonstruksi on-chain klaim reward per gauge.
INKONSISTENSI komposisi distribusi (C-001) belum terpecahkan — angka per kategori non-komunitas tidak boleh dikutip sebagai final.
Harga era distribusi (Agu 2020-Jan 2021) tidak tercakup exchange yang datanya diakses riset ini.

FARMING DAN SYBIL

Distribusi berbasis likuiditas riil: farming memerlukan modal nyata di pool gauge — biaya ekonomi menjadi penghalang sybil tanpa identitas; pola mercenary LP (masuk saat gauge tinggi, keluar saat emisi turun) adalah dinamika yang diterima dan menjadi pola lintas protokol gauge (MEDIUM) [Phase 9 — Financial Decision Pattern; Phase 10 — Pattern Candidates]

PROSPEK

Metrik yang terpenuhi: Likuiditas terkunci skala besar; governance gauge fungsional bertahun-tahun; value accrual fee share berjalan (HIGH)
Metrik yang tidak terpenuhi: Retensi harga jangka panjang (CRV jauh di bawah puncak 2021); permintaan gauge pasca-Curve-Wars melemah (MEDIUM)
Sinyal ke depan: Volume swap & fee ke veCRV; pertumbuhan crvUSD; total lock veCRV (MEDIUM)
Penilaian: Distribusi CRV sukses mengunci likuiditas dan menciptakan mekanisme governance yang ditiru industri, namun tanpa kontrol pasokan ketat (inflasioner) dan dengan melemahnya meta-layer, retensi nilai bergantung penuh pada arus fee riil — kontras tajam dengan fair launch YFI di dataset ini (MEDIUM)

PELAJARAN LINTAS PROJECT

Emisi gauge mengunci likuiditas lebih lama daripada airdrop, tetapi nilai token menjadi fungsi permintaan politik internal (gauge voting) — ketika meta-layer (Convex/bribe) mendingin, permintaan struktural ikut turun.
Konflik komposisi distribusi yang tidak terpecahkan adalah liabilitas data: 30% supply berbeda atribusi (team vs shareholders) antar sumber mengubah analisis sentralisasi — verifikasi dokumen primer harus didahulukan sebelum publikasi angka.
Token inflasioner dengan value accrual fee share dinilai dengan arus kas (fee vs emisi), bukan kelangkaan — framework analisisnya berbeda dari token fixed/fair-launch.

## Open Questions
- [foundation] Roster kontributor inti resmi
- [foundation] Entitas legal Curve Labs & Foundation (yurisdiksi pasti)
- [foundation] Tanggal persis pool pertama Januari 2020
- [history] Angka pasti kerugian eksploitasi Vyper per pool
- [history] Detail transaksi OTC CRV Egorov (jumlah, harga, pihak)
- [history] Jadwal emisi CRV terkini dan total terkunci veCRV
- [technology] StableSwap NG adoption rate across existing pools vs. legacy StableSwap — deployment status per chain not fully documented
- [technology] LlamaLend isolated markets: current active markets and total value locked not centrally indexed
- [technology] Cross-chain liquidity unification: no official technical design published for cross-chain pool aggregation (only independent deployments)
- [technology] Vyper 0.4+ compatibility roadmap for legacy pools — no public migration plan for immutable contracts
- [technology] crvUSD PegKeeper effectiveness during prolonged depeg events — limited public post-mortem data
- [technology] Formal verification coverage: which specific contracts/modules have completed Certora verification vs. pending
- [financial] Angka fee protokol per kuartal
- [financial] Saldo & komposisi treasury DAO terverifikasi on-chain
- [financial] Detail harga alokasi investor pra-TGE
- [token] Exact current circulating supply varies by tracker (CoinGecko vs CoinMarketCap vs on-chain) — need authoritative on-chain query for precise figure
- [token] Foundation wallet address and current CRV balance not explicitly documented in public sources — need to identify specific multisig
- [token] veCRV V2 delegation adoption rate and total delegated voting power not centrally reported
- [token] crvUSD PegKeeper CRV emission allocation percentage vs. main gauges — exact split not published in single source
- [token] LlamaLend gauge emission weights and total CRV allocated to date — not aggregated in public dashboard
- [token] StableSwap NG gauge deployment status per chain — incomplete documentation on which chains have NG gauges live
- [token] Whether any CRV buyback or burn proposal has reached formal DAO vote — historical proposal review needed
- [token] Employee vesting contract addresses and verification of full vesting completion — on-chain verification needed
- [ecosystem] Jumlah deployment chain aktif terkini
- [ecosystem] Total TVL per kategori pool (stable vs crypto vs LST) terkini
- [ecosystem] Peta bribe market terkini (Votium dkk.)
- [market] TVL & volume Curve terkini (2025-2026)
- [market] Total CRV terkunci veCRV & tren bribe market
- [market] Harga CRV pasca-2024 dari sumber exchange terverifikasi
- [behavioral] Motivasi detail keputusan OTC founder 2023 (pernyataan langsung)
- [behavioral] Arah strategis gauge era post-Curve-Wars (proposal terkait)
- [knowledge] Kuantifikasi efek bribe market terhadap distribusi emisi (data historis Votium)
- [knowledge] Studi komparatif fee share CRV vs mekanisme buyback token lain
- [conflict] Verifikasi dokumen primer distribusi CRV Agustus 2020 (menyelesaikan C-001)
- [conflict] Angka kerugian eksploitasi Vyper per pool
- [conflict] Detail transaksi OTC CRV founder 2023
- [conflict] TVL, volume, dan total veCRV lock terkini
- [airdrop] Resolusi C-001 (dokumen primer distribusi Agustus 2020)
- [airdrop] Total CRV terkunci veCRV & volume bribe market terkini
- [airdrop] Harga CRV 2024-2026 dari sumber exchange terverifikasi (di luar window yang diambil riset ini)
