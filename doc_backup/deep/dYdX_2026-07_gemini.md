Laporan Rekonstruksi Ekosistem dYdX: Analisis Arsitektur, Tokenomika Defensif, dan Pivot RWA Arcus

## 1 Executive Summary

dYdX memegang posisi yang sangat krusial dalam sejarah evolusi keuangan terdesentralisasi (DeFi) sebagai pionir platform perdagangan derivatif terdesentralisasi (DEX) berbasis buku order hibrida. Perjalanan teknologinya mencerminkan pencarian tanpa henti terhadap keseimbangan antara performa tinggi (throughput) setara bursa terpusat (CEX) dan kedaulatan non-kustodian yang menjadi fondasi dasar Web3. Dari awal beroperasi di Ethereum Layer 1, bermigrasi ke mesin zk-rollup StarkEx Layer 2, meluncurkan blockchain mandiri dYdX Chain (v4) berbasis Cosmos SDK, hingga melakukan pivot radikal dengan meluncurkan Arcus di Robinhood Chain pada tahun 2026, dYdX terus mendefinisikan ulang batas-batas operasional bursa on-chain.

Meskipun memegang keunggulan sebagai penggerak pertama (first mover) yang membawa volume perdagangan seumur hidup melampaui $1,55 triliun, dYdX menghadapi tantangan eksistensial yang sangat berat sepanjang tahun 2024 dan 2025. Desain tokenomika awal yang lemah—di mana kegunaan token DYDX terbatas pada hak tata kelola tanpa adanya mekanisme penangkapan nilai langsung—menyebabkan kerentanan struktural yang fatal. Celah ini dieksploitasi oleh kompetitor baru, khususnya Hyperliquid, yang berhasil merebut dominasi pasar melalui kombinasi arsitektur berlatensi sub-detik tanpa friksi jembatan lintas-rantai (bridging) dan tokenomika buyback harian yang sangat agresif. Akibatnya, pangsa pasar dYdX menyusut drastis dari 75% pada awal 2023 menjadi hanya sekitar 7% di akhir tahun 2024.

Menghadapi kemunduran ini, dYdX merespons dengan dua langkah strategis defensif yang masif. Pertama, melalui Proposal #313 pada November 2025, komunitas menyetujui rekayasa ulang tokenomika ekstrem dengan mengalokasikan 75% dari seluruh pendapatan bersih bursa untuk melakukan pembelian kembali (buyback) dan staking otomatis terhadap token DYDX. Kedua, dYdX Labs berkolaborasi dengan Robinhood meluncurkan Arcus pada Juli 2026, memindahkan fokus kompetisi dari pasar derivatif kripto murni yang jenuh ke segmen aset dunia nyata (RWA) dan saham terdigitalisasi yang patuh regulasi. Laporan ini menyajikan analisis mendalam mengenai seluruh siklus hidup proyek dYdX, dinamika tokenomika, penyebab kegagalan taktis, serta potensi pemulihan jangka panjang ekosistemnya.

## 2 Industry Background

Sebelum berdirinya dYdX pada pertengahan 2017, industri aset kripto berada dalam cengkeraman penuh bursa terpusat (CEX) seperti Mt. Gox, Poloniex, dan Coinbase. Dominasi mutlak model kustodian pihak ketiga ini mendatangkan risiko sistemik yang sangat tinggi, yang terbukti secara tragis lewat kasus kebangkrutan Mt. Gox pada tahun 2014 dengan kerugian mencapai 850.000 BTC. Di sisi lain, ekosistem bursa terdesentralisasi (DEX) generasi pertama seperti EtherDelta sangat tidak memadai untuk kebutuhan perdagangan aktif. Beroperasi langsung di atas Ethereum Layer 1, bursa-bursa awal ini lumpuh oleh latensi blok yang lambat (waktu pembuatan blok 12 hingga 15 detik) dan biaya gas yang sangat mahal untuk setiap pengiriman, pencocokan, bahkan pembatalan pesanan perdagangan.

Pada periode 2018-2020, industri menyaksikan lahirnya terobosan Automated Market Maker (AMM) yang dipelopori oleh Uniswap menggunakan rumus produk konstan x \times y = k. AMM berhasil menyelesaikan masalah likuiditas untuk perdagangan spot aset ekor panjang (long-tail assets), namun model ini terbukti sangat tidak efisien untuk perdagangan derivatif, margin, dan posisi berleverage tinggi karena tingginya dampak harga (price impact) dan slippage pada transaksi bernominal besar. Pedagang profesional dan institusional tetap bertahan di CEX karena mereka membutuhkan fungsionalitas buku order (order book) yang menyediakan order batas (limit orders) yang presisi, kedalaman likuiditas yang dapat diprediksi, dan spread yang ketat.

Kesenjangan pasar inilah yang melahirkan dYdX. Narasi yang berkembang di industri pada pertengahan 2017 adalah pencarian platform hibrida: sebuah bursa non-kustodian yang mampu menyajikan performa kecepatan transaksi sekelas bursa terpusat, namun tetap mengembalikan hak kontrol penuh atas dana (self-custody) kepada para pengguna. dYdX lahir tepat pada momentum krusial ini, memanfaatkan fase awal eksplorasi infrastruktur penskalaan Layer 2 untuk memecahkan dilema trilema skalabilitas bursa on-chain.

## 3 Project Origin

dYdX didirikan di San Francisco pada tahun 2017 oleh Antonio Juliano, seorang insinyur perangkat lunak dengan rekam jejak yang solid di beberapa raksasa teknologi Lembah Silikon. Setelah lulus dari Princeton University dengan gelar Computer Science pada tahun 2015, Juliano bekerja sebagai Software Engineer II di Coinbase, di mana ia bersentuhan langsung dengan arsitektur bursa kripto berskala besar. Pengalamannya di Coinbase, dikombinasikan dengan masa kerjanya di Uber dan MongoDB, memicu keyakinannya bahwa masa depan keuangan global harus dibangun di atas rel non-kustodian. Sebelum dYdX, Juliano sempat membangun Weipoint, sebuah mesin pencari terdesentralisasi, namun proyek tersebut dihentikan setelah 5 bulan karena sepinya adopsi.

Juliano kemudian menyusun tim inti (Core Team) yang didominasi oleh lulusan universitas elit dan mantan insinyur dari perusahaan teknologi terkemuka:

Antonio Juliano: Pendiri dan CEO, mantan Software Engineer di Coinbase, Uber, dan MongoDB.

Brendan Chou: Insinyur Utama (Lead Engineer), lulusan Princeton Computer Science tahun 2015, mantan Site Reliability Engineer di Google dan Financial Software Engineer di Bloomberg.

Bryce Neal: Staff Software Engineer, memiliki pengalaman backend dan DeFi di Square, NerdWallet, dan Amazon.

David Gogel: Growth Lead, pemegang gelar MBA dari Wharton School, bertugas memimpin ekspansi pasar dan kemitraan strategis.

Eddie Zhang: Bergabung sebagai President dYdX pada Agustus 2025 menyusul akuisisi aplikasi perdagangan sosial Telegram buatannya, Pocket Protector, oleh dYdX Labs. Zhang membawa pengalaman luas sebagai Product Manager di Facebook Messenger dan pendiri aplikasi sosial Fam yang didanai Founders Fund dan diakuisisi Eventbrite.

Untuk memperkuat kedudukan strategisnya di industri, dYdX menggaet sejumlah penasihat (advisors) berpengaruh:

Fred Ehrsam: Pendiri pendamping (Co-founder) Coinbase dan bursa investasi Paradigm.

Steve Jang: Pendiri dan investor malaikat di Uber, Coinbase, dan useheartbeat.

Barry Kwok: Penasihat skala operasional bisnis, mantan staf rekrutmen awal di Coinbase dan Airbnb.

Inspirasi dYdX bersumber dari keinginan untuk merancang instrumen keuangan yang bersih, aman, dan dapat dijalankan sepenuhnya melalui baris kode kontrak pintar tanpa perantara tepercaya. Masalah utama yang ingin diselesaikan sejak awal adalah ketiadaan likuiditas margin yang aman di atas Ethereum. Melalui reputasi Juliano dan jaringan Coinbase Mafia, proyek ini berhasil menarik minat investor ventura papan atas sejak putaran pendanaan paling awal.

## 4 Innovation Analysis

Inovasi dYdX berkembang melalui beberapa tahap yang meletakkan standar teknis baru bagi industri pertukaran derivatif terdesentralisasi. Secara kategoris, dYdX bertindak sebagai "Fast Follower" yang secara agresif menerapkan teknologi penskalaan termutakhir untuk mereplikasi model buku order (order book) bursa terpusat ke ranah on-chain.

Inovasi utama dYdX terbagi ke dalam tiga pilar arsitektur besar:

Desain Buku Order Hibrida L2 (v3 StarkEx) Pada dYdX v3, platform memelopori penggabungan performa off-chain dengan keamanan on-chain. Mesin pencocokan (matching engine) dan buku order dijalankan secara terpusat oleh server dYdX Labs demi kecepatan sub-detik. Namun, dYdX bekerja sama dengan StarkWare untuk menyelesaikan (settle) setiap transaksi yang cocok menggunakan mesin penskalaan StarkEx zk-rollup. Bukti kriptografi STARK dikirimkan ke Ethereum L1 untuk memverifikasi validitas transaksi secara non-kustodian. Langkah ini mengeliminasi gas fee bagi pengguna untuk setiap penempatan atau pembatalan order, sebuah masalah utama yang sebelumnya melumpuhkan DEX buku order L1.

Desentralisasi Total via Sovereign L1 Appchain (v4) Meskipun StarkEx menyelesaikan masalah performa, sistem v3 dinilai belum desentralisasi sepenuhnya karena mesin pencocokan masih dikendalikan satu pihak. Melalui dYdX v4, tim berinovasi dengan membangun blockchain berdaulat sendiri (dYdX Chain) menggunakan Cosmos SDK dan CometBFT. Dalam arsitektur ini, setiap validator menjalankan buku order off-chain di mempool mereka secara terdistribusi, dan pencocokan pesanan diselesaikan secara real-time langsung di setiap blok on-chain. Ini adalah standar baru di mana aplikasi DeFi berskala besar terbukti mampu mengoperasikan blockchain mandiri berkinerja tinggi tanpa bergantung pada validator L1 umum.

Ekosistem MegaVault dan Listing Tanpa Izin (dYdX Unlimited) Diperkenalkan pada akhir tahun 2024, peningkatan dYdX Unlimited meluncurkan MegaVault. MegaVault berfungsi sebagai kolam likuiditas induk (master liquidity pool) otomatis yang mengalokasikan likuiditas secara dinamis ke seluruh pasar di platform. Pengguna dapat menjadi penyedia likuiditas pasif dengan menyetorkan USDC ke MegaVault untuk mendapatkan yield otomatis dari strategi pembuatan pasar. Bersamaan dengan ini, fitur Instant Market Listings diaktifkan, memungkinkan pengguna meluncurkan pasangan pasar perpetual baru secara instan dengan hanya menyetor jaminan awal 10.000 USDC tanpa perlu melewati proses persetujuan tata kelola yang lambat.

Keberhasilan dYdX memvalidasi arsitektur appchain menginspirasi lahirnya kompetitor generasi baru seperti Hyperliquid, Vertex, dan Aevo yang semuanya mengadopsi model blockchain khusus bursa derivatif. Langkah dYdX membuktikan bahwa untuk mempertahankan kedaulatan operasional, struktur appchain berkinerja tinggi jauh lebih unggul dibandingkan dengan beroperasi sebagai dApp di atas rollup umum.

## 5 Technology Evolution

Perkembangan teknologi dYdX mencerminkan pergeseran paradigma infrastruktur DeFi dari Layer 1 Ethereum menuju kedaulatan penuh multi-chain.

Era Ethereum Layer 1 (dYdX v1 & v2):

v1 (Solo): Diluncurkan pada Oktober 2018, mendukung margin trading dasar, peminjaman, dan peninjauan saldo akun terintegrasi di L1 Ethereum.

v2: Diluncurkan pada awal 2020, memperkenalkan kontrak pintar untuk margin terisolasi (isolated margin) yang lebih efisien dari sisi gas fee. Namun, seluruh sistem ini lumpuh ketika Ethereum mengalami kemacetan parah dan biaya gas melambung tinggi selama DeFi Summer.

Era Layer 2 zk-Rollup (dYdX v3):

v3 (Februari 2021): Memindahkan mesin penyelesaian transaksi ke StarkEx zk-rollup L2. Sistem ini menggunakan off-chain matching engine terpusat dan on-chain settlement berbasis bukti STARK. throughput melesat tinggi, memungkinkan leverage hingga 20x dengan biaya transaksi yang sangat murah. dYdX v3 resmi dihentikan layanannya (sunset) pada 28 Oktober 2024 guna menyatukan likuiditas ke rantai utama v4.

Era Sovereign Appchain Cosmos (dYdX v4):

v4 (Oktober 2023): Bermigrasi penuh menjadi blockchain Layer 1 mandiri (dYdX Chain) berbasis Cosmos SDK dan CometBFT. Sistem ini menerapkan buku order terdesentralisasi penuh di mana setiap validator mengelola transaksi langsung di mempool lokal mereka, mampu mengeksekusi hingga 20.000 operasi per detik (orders, cancels, liquidations).

Era Optimasi Latensi dan Integrasi Ritel (2025-2026):

Designated Proposer Model: Diperkenalkan lewat tata kelola pada September 2025, fitur ini memilih validator tertentu untuk memproposisikan blok demi stabilitas dan pemotongan latensi blok.

Order Entry Gateway Services (OEGS): Membuka rute satu-langkah (one-hop) langsung antara pedagang dan validator pengusul blok guna mereduksi kompleksitas perutean order.

Arcus (Juli 2026): dYdX Labs mengambil langkah evolusi di luar ekosistem Cosmos dengan meluncurkan Arcus di Robinhood Chain (Arbitrum EVM-compatible Layer 2). Arcus dirancang untuk memproses perdagangan spot saham AS terdigitalisasi tanpa biaya transaksi dan melayani pasar perpetual instrumen RWA dengan leverage hingga 50x.

## 6 Funding Intelligence

Sejak awal berdirinya, dYdX telah didukung oleh konsorsium pemodal ventura papan atas yang memberikan landasan modal yang sangat kuat untuk penelitian, rekayasa teknologi, dan akuisisi strategis.

Funding Round: Seed

Date: 19 Desember 2017

Amount: $2,000,000

Lead Investor: Polychain Capital, Andreessen Horowitz

Participants: Brian Armstrong, Fred Ehrsam, Scott Belsky, Christopher Golda, Avichal Garg, 1confirmation, Kindred Ventures, Abstract Ventures, Cota Capital, Vy Capital, Craft Ventures

Estimated Valuation: ~$20,000,000

Funding Round: Series A

Date: 19 Oktober 2018

Amount: $10,000,000

Lead Investor: Andreessen Horowitz (a16z)

Participants: Bain Capital Ventures, Polychain Capital, 1confirmation, Dragonfly Capital, Naval Ravikant, Kevin Hartz, Alexander Pack, Abstract Ventures, Kindred Ventures

Estimated Valuation: ~$100,000,000

Funding Round: Series B

Date: 26 Januari 2021

Amount: $10,000,000

Lead Investor: Three Arrows Capital, DeFiance Capital

Participants: Andreessen Horowitz, Paradigm, 1confirmation, Hashed, GSR, Spartan Group, SCP, Right Side Capital Management, Wintermute, Scalar Capital

Estimated Valuation: ~$100,000,000

Funding Round: Series C

Date: 15 Juni 2021

Amount: $65,000,000

Lead Investor: Paradigm

Participants: Andreessen Horowitz, Polychain Capital, Three Arrows Capital, Wintermute, QCP Capital, CMS Holdings, CMT Digital, Finlink Capital, Sixtant, Menai Financial Group, MGNR, Kronos Research, HashKey, Electric Capital, Delphi Digital, StarkWare

Estimated Valuation: ~$650,000,000

Funding Round: Foundation Strategic Grant

Date: 11 Agustus 2025

Amount: $8,000,000

Funder: dYdX Foundation (Penggalangan mandiri untuk mendanai ekosistem dan riset hibah dYdX Grants Ltd)

INKONSISTENSI:

Detail: Laporan PitchBook mencatat penggalangan dana Seed dYdX sebesar $1,960,000 pada 19 Desember 2017, sementara Wellfound dan Dropstab mencatat angka pembulatan sebesar $2,000,000. Selain itu, akumulasi total pendanaan dilaporkan sebesar $87,000,000 di Wellfound, tetapi diindeks sebesar $85,000,000 di database RootData. Perbedaan ini diidentifikasi sebagai akibat perbedaan pelaporan administratif pasca-merger atau kontribusi tertutup.

Evidence Level: LOW

Keterlibatan VC papan atas seperti Andreessen Horowitz dan Paradigm membawa berkah ganda sekaligus tantangan politik bagi dYdX. Di satu sisi, pendanaan berlimpah ini mengamankan landasan pengembangan teknologi dYdX di tengah siklus pasar beruang yang ekstrem. Hubungan erat investor dengan pembuat pasar global (seperti GSR dan Wintermute) menjamin likuiditas awal yang tebal di buku order dYdX. Namun, dominasi VC (investor awal menguasai 27,73% suplai genesis) menciptakan hambatan struktural dalam menarik minat kelompok desentralisasi murni. Hal ini menjadi kelemahan utama dYdX yang dieksploitasi oleh Hyperliquid, yang meluncurkan bursa buku order saingannya tanpa pendanaan VC dan tanpa beban tekanan unlock token orang dalam.

## 7 Community Intelligence

Strategi dYdX untuk mengakuisisi pengguna awal berpusat pada penargetan kelompok pedagang aktif, spekulan volume besar, dan penyedia likuiditas institusional. dYdX merintis sistem pembagian hadiah berkala berdurasi 28 hari yang disebut "Epoch". Melalui Epoch, platform membagikan token DYDX secara berkala kepada pedagang berdasarkan kombinasi rumit dari total biaya transaksi yang dibayarkan dan minat terbuka (open interest). Langkah ini sukses besar dalam melakukan bootstrap awal terhadap volume perdagangan on-chain, namun menarik sekelompok "Yield Farmers" oportunistik yang langsung melikuidasi token hadiah mereka ke pasar, menekan kinerja harga token secara berkepanjangan.

Sebagai bagian dari strategi pertumbuhan taktis, dYdX meluncurkan beberapa program insentif lanjutan:

Program Afiliasi Booster (Januari 2026): Menawarkan komisi berbasis USDC seumur hidup untuk rujukan rujukan, dengan komisi berkisar antara 15% (standar afiliasi hingga batas $3.000 sebulan) hingga 50% (affiliate VIP dengan batas pembayaran hingga $10.000 sebulan).

dYdX Surge (Awal 2025): Kompetisi perdagangan lintas-musim bernilai $20.000.000 untuk meningkatkan aktivitas perdagangan.

Trading Leagues (Q4 2025): Liga kompetisi berbasis performa keuntungan (P&L-adjusted leaderboard) untuk memicu kompetisi organik di kalangan pengguna ritel non-API, mendistribusikan hadiah hingga $1.000.000.

Fee Holidays (Akhir 2025): Penghapusan sementara biaya transaksi untuk pasar berkinerja tinggi (BTC-USD dan SOL-USD).

Meskipun program-program ini berhasil mencatatkan rekor keaktifan berkala, dYdX gagal mempertahankan loyalitas komunitas jangka panjang ketika dihadapkan dengan taktik kompetitif baru. Hyperliquid merebut minat komunitas melalui skema airdrop poin yang dinilai lebih adil bagi pengguna ritel berskala kecil, serta menawarkan pembagian hasil biaya transaksi langsung yang jauh lebih transparan kepada pemegang token asli mereka tanpa adanya bias kepemilikan pemegang modal ventura.

## 8 Narrative Intelligence

dYdX terbukti sangat lincah dalam memanfaatkan berbagai narasi industri kripto dari waktu ke waktu, dan dalam banyak kasus, bertindak sebagai pencipta tren naratif itu sendiri.

Fase DeFi Summer (2020-2021): dYdX memimpin narasi penskalaan Layer 2 di Ethereum. Melalui integrasi StarkEx zk-rollup, dYdX memposisikan dirinya sebagai jawaban atas masalah gas fee Ethereum yang mahal, mengusung narasi "CEX-Killer" yang menawarkan pengalaman bertransaksi tanpa biaya gas dengan keamanan non-custodial penuh.

Fase Kedaulatan Appchain (2023-2024): Ketika narasi "Appchain" dan ekosistem modular Cosmos mulai menguat, dYdX menciptakan momentum baru dengan mengumumkan transisi penuh ke dYdX Chain. Narasinya bergeser dari sekadar aplikasi di atas rollup pihak ketiga menjadi blockchain L1 terspesialisasi yang dikendalikan penuh oleh komunitas.

Fase Telegram Mini-App & Social Trading (2025): Merespons ledakan aktivitas perdagangan berbasis Telegram, dYdX mengakuisisi Pocket Protector pada Juli 2025 dan meluncurkan perdagangan terintegrasi Telegram di bulan September. Langkah ini merebut perhatian pasar lewat narasi penyederhanaan akses DeFi ritel langsung di aplikasi perpesanan massal.

Fase Aset Dunia Nyata (RWA) dan Saham Tokenisasi (2026): Kolaborasi dYdX Labs dalam meluncurkan Arcus di Robinhood Chain pada Juli 2026 menandai adopsi penuh terhadap narasi RWA. Mengingat pasar derivatif kripto murni yang semakin jenuh, dYdX memposisikan dirinya di garis depan konvergensi pasar saham tradisional 24/7 dan DeFi patuh regulasi.

## 9 Competitive Landscape

Lanskap kompetisi dYdX dicirikan oleh transisi dari posisi monopoli pasar bursa derivatif on-chain menjadi pertarungan sengit melawan bursa khusus berkinerja tinggi yang memiliki desain ekonomi lebih berpihak pada pengguna ritel.

Pada fase awal (2021-2023), kompetitor terdekat dYdX adalah GMX dan Synthetix (Kwenta). GMX menawarkan kenyamanan model kolam likuiditas multi-aset (GLP), namun dYdX memenangkan persaingan mutlak dalam hal volume transaksi harian dan efisiensi biaya bagi pembuat pasar profesional karena arsitektur buku order hibridanya yang jauh lebih ramah terhadap institusi. Puncak TVL dYdX menyentuh $1,1 miliar pada Oktober 2021.

Peta persaingan berubah secara ekstrem dengan peluncuran Hyperliquid. Analisis komparatif mendalam mengidentifikasi tiga kelemahan struktural utama dYdX yang berhasil dieksploitasi oleh kompetitornya:

Efisiensi Akumulasi Nilai Token: Selama masa kejayaan v3, 100% dari biaya transaksi dYdX mengalir langsung ke kas perusahaan terpusat dYdX Trading Inc. Meskipun v4 mengalihkan biaya tersebut ke validator dan staker dalam bentuk USDC, sistem ini tidak menghasilkan tekanan beli langsung pada token asli DYDX. Sebaliknya, Hyperliquid merancang mekanisme "Assistance Fund" yang sangat agresif di mana 97% hingga 99% dari seluruh biaya perdagangan harian digunakan untuk membeli kembali (buyback) token HYPE di pasar terbuka, memberikan kepastian pertumbuhan nilai yang terikat langsung pada volume operasional bursa.

Friksi Antarmuka dan Kecepatan Transaksi: Transisi dYdX ke Cosmos Appchain mengharuskan pengguna melewati proses bridging lintas-rantai yang lambat dan memakan biaya. Pada saat yang sama, latensi blok dYdX Chain berada di kisaran ~1 detik. Di sisi lain, Hyperliquid menawarkan rantai L1 kustom berlatensi sub-detik dengan integrasi deposit USDC instan yang mulus.

Tekanan Jual Investor (VC Pressure): dYdX terbebani oleh jadwal emisi token yang mendistribusikan porsi besar kepada investor awal (27,73%) dan tim (15,27%). Sementara itu, Hyperliquid meluncurkan token HYPE dengan distribusi komunitas murni (31% alokasi airdrop genesis) tanpa adanya alokasi investor swasta/VC.

Dampak dari kekalahan taktis ini sangat dramatis. Pangsa pasar volume perdagangan dYdX anjlok dari 75% pada awal tahun 2023 menjadi hanya sekitar 7% di akhir 2024, di mana volume bulanan dYdX menyusut hingga $20 miliar dibandingkan Hyperliquid yang melesat ke level $200 billion.

Pivot taktis dYdX Labs meluncurkan Arcus di Robinhood Chain pada Juli 2026 adalah langkah keluar dari persaingan berdarah pasar derivatif kripto murni. Di ranah Robinhood Chain, Arcus berhadapan dengan bursa L2 terdedikasi seperti Lighter, Meridian, dan SynFutures. Keunggulan kompetitif Arcus terletak pada kepemilikan jalur distribusi langsung ke 25 juta pengguna ritel Robinhood, memberi perlindungan likuiditas kokoh dari ancaman kompetitor kripto-asli.

## 10 Product Evolution

Evolusi produk dYdX membuktikan kelenturan arah strategis tim pengembang dalam merespons keterbatasan teknologi dan pergeseran selera pedagang.

dYdX Solo (v1): Berfokus pada instrumen spot dan margin terpusat di atas Ethereum L1. Sangat terhambat oleh lambatnya throughput Ethereum.

dYdX v3 (Februari 2021): Pivot total meninggalkan perdagangan spot murni untuk berfokus pada produk kontrak perpetual cross-margin berbasis StarkEx zk-rollup L2. Produk ini menjadi standar emas bursa derivatif DeFi selama bertahun-tahun.

dYdX Chain (v4): Meluncurkan blockchain Layer 1 mandiri untuk mendesentralisasikan buku order hibrida di tingkat konsensus validator Cosmos.

dYdX Unlimited (November 2024): Integrasi fitur Instant Market Listings, kolam likuiditas otomatis MegaVault, login sosial, swap instan USDC-DYDX via Osmosis, dan program afiliasi instan.

Telegram Trading Mini-App (September 2025): Pengenalan antarmuka perdagangan sosial langsung dari aplikasi Telegram menyusul akuisisi Pocket Protector.

Solana Spot Trading (Desember 2025): Ekspansi jangkauan aset perdagangan spot di luar ekosistem EVM dan Cosmos.

Arcus (Juli 2026): Pivot produk terbesar dYdX Labs yang memindahkan infrastruktur perdagangan ke Robinhood Chain L2. Arcus fokus menyediakan instrumen perdagangan spot untuk 95 saham AS terdigitalisasi tanpa biaya transaksi bagi ritel, serta rintisan 35 pasar perpetual berbasis RWA (komoditas, indeks global, dan saham pra-IPO) dengan leverage hingga 50x.

## 11 Tokenomics Intelligence

Struktur ekonomi token dYdX telah didefinisikan ulang secara fundamental sepanjang sejarahnya untuk memperbaiki kelemahan desain awal dan menahan laju penurunan harga.

Initial Token Minting:

Total Minted Supply: 1,000,000,000 DYDX

Mint Date: 3 August 2021

Target Release Duration: 5 years (concluding by June 2026)

Initial Five-Year Allocation:

Community Allocation: 50.00% (500,000,000 DYDX)

Trading Rewards: 25.00% (250,000,000 DYDX)

Retroactive Mining Rewards: 7.50% (75,000,000 DYDX)

Liquidity Provider Rewards: 7.50% (75,000,000 DYDX)

Community Treasury: 5.00% (50,000,000 DYDX)

Liquidity Staking Pool (USDC): 2.50% (25,000,000 DYDX)

Safety Staking Pool (DYDX): 2.50% (25,000,000 DYDX)

Past Investors of dYdX Trading: 27.73% (277,295,070 DYDX)

Founders, Employees, Advisors, Consultants: 15.27% (152,704,930 DYDX)

Future Employees and Consultants: 7.00% (70,000,000 DYDX)

Insider Vesting Schedule:

Date 1 December 2023: 30% unlocked

Period January 2024 to June 2024: 40% unlocked in equal monthly installments - Period July 2024 to June 2025: 20% unlocked in equal monthly installments

Period July 2025 to June 2026: 10% unlocked in equal monthly installments

Emission Reduction:

Reduction Percentage: 50%

Effective Date: June 2025

Perpetual Inflation Policy:

Maximum Perpetual Inflation Rate: 2.00% per year

Earliest Activation Date: 3 August 2026

wethDYDX Bridge Sunset Details:

Sub-DAO Developer: dYdX Operations subDAO

Submission of Proposal: 9 June 2025 - Bridge Deprecation Date: 13 June 2025

Bridged Tokens Ratio: 1:1 migration

Bridged Percentage: >94% of tokens migrated

Unbridged Supply Left on Ethereum: ~14% (approx. 41,657,249 DYDX)

Affected Wallets: ~13,800 addresses

Current Fee and Revenue Distribution (dYdX Chain v4):

Staking Rewards Allocation: 15% of Net Protocol Revenue distributed automatically per block in USDC

MegaVault Allocation: 5% of Net Protocol Revenue

Treasury subDAO Allocation: 5% of Net Protocol Revenue

Buyback Program Allocation: 75% of Net Protocol Revenue

Buyback Escapes Timeline:

Launch Date of Buyback Program: 23 April 2025

Proposal #225 Allocation: 12.5%

Proposal #231 Allocation: 25%

Proposal #313 Allocation: 75% (Passed on 13 November 2025)

Keputusan tata kelola pada pertengahan 2025 untuk menghentikan dukungan jembatan lintas-rantai (bridge) wethDYDX pada 13 Juni 2025 menimbulkan gejolak politik yang parah. Langkah ini diinisiasi oleh dYdX Operations subDAO untuk memaksa konsolidasi total likuiditas ke dalam rantai berdaulat dYdX Chain. Namun, karena minimnya sosialisasi langsung di kalangan pengguna non-aktif, sekitar 14% pasokan (mencakup 41,657,249 DYDX hingga 140.000.000 ethDYDX) terdampar selamanya di Ethereum tanpa memiliki opsi migrasi resmi langsung. Kerugian ini dialami oleh sekitar 13.800 pemegang dompet lama yang terlambat bertindak.

Di sisi lain, reformasi tokenomika buyback melalui Proposal #313 pada 13 November 2025 merupakan langkah penyelamatan nilai yang sangat agresif. Dengan mengalihkan 75% pendapatan operasional bersih langsung ke program pembelian kembali otomatis di pasar sekunder (yang kemudian di-stake ke validator), dYdX berhasil mengubah fungsi DYDX dari sekadar token tata kelola kosong menjadi aset penangkap nilai ekonomi yang sangat kuat. Pembelian kembali terkumpul sebanyak 8,46 juta DYDX senilai $1,72 juta per 1 Januari 2026.

## 12 Airdrop & Incentive Intelligence (WAJIB)

dYdX mengukir sejarah industri DeFi dengan menyelenggarakan salah satu kampanye retroactive airdrop paling dinamis sekaligus kontroversial pada September 2021.

Tujuan utama dari kampanye ini adalah mendesentralisasikan kepemilikan bursa kepada basis pengguna aktif historisnya, sekaligus mendorong migrasi volume perdagangan dari Ethereum L1 ke platform Layer 2 StarkEx yang baru dirilis.

Strategi distribusi airdrop dan insentif dYdX meliputi beberapa pilar:

Alokasi Retroactive Airdrop: 7,50% dari pasokan maksimal (75.000.000 DYDX) dialokasikan untuk pengguna historis.

Tanggal Snapshot: 26 Juli 2021 pukul 00:00:00 UTC.

Struktur Milestone Perdagangan (Epoch 0): Untuk dapat melakukan klaim secara utuh, penerima manfaat diwajibkan melakukan perdagangan aktif di L2 dYdX dan mencapai target volume transaksi tertentu dalam Epoch 0 (28 hari pertama). Jika penerima hanya memenuhi sebagian target volume, sisa token mereka dianggap hangus dan otomatis dialihkan ke kas Treasury komunitas.

Boikot Wilayah Amerika Serikat: Akibat ketidakpastian regulasi sekuritas AS, program airdrop retroactive ini dilarang keras bagi pengguna yang berada di bawah yurisdiksi hukum Amerika Serikat.

Kolam Staking USDC dan Pengaman (Safety Pool): dYdX menyisihkan masing-masing 2,50% pasokan (25.000.000 DYDX per kolam) sebagai insentif bagi pengguna yang bersedia menyetor jaminan likuiditas USDC atau menaruh pengaman staking untuk menutupi risiko kegagalan sistemik platform.

Taktik mewajibkan transaksi aktif di Epoch 0 adalah keputusan pertumbuhan yang sangat cerdas. Langkah ini memaksa ribuan pengguna mengadopsi platform L2 StarkEx secara instan, menghasilkan kedalaman buku order yang luar biasa tebal di DeFi kala itu. Namun, keputusan ini memicu fenomena manipulasi volume (wash trading) berskala besar karena pengguna mengejar pemenuhan kuota target transaksi masing-masing. Di samping itu, ketiadaan mekanisme penguncian (vesting) jangka panjang untuk pengguna ritel pasca-Epoch 0 memicu aksi jual masif yang melumpuhkan performa harga token di pasar sekunder.

Pada fase pasca-migrasi Cosmos (2025-2026), dYdX merombak total model insentifnya:

dYdX Surge: Program kompetisi perdagangan berhadiah total $20.000.000 yang mengontrol pemberian emisi berdasarkan kesehatan kedalaman buku order.

Fee Holidays: Kebijakan penghapusan biaya transaksi sementara pada pasangan BTC-USD dan SOL-USD di akhir 2025, yang sukses mendongkrak keaktifan volume transaksi hingga 2-3 kali lipat.

MegaVault Giveaways: Undian senilai 100.000 USDC untuk memikat penyedia likuiditas pasif ritel menyetorkan dana ke MegaVault.

## 13 Token Lifecycle Intelligence

Token dYdX menjalani siklus hidup yang sangat fluktuatif, dipengaruhi oleh transisi arsitektur teknologi bursa, emisi token insider, serta persaingan memperebutkan likuiditas dengan bursa lain.

Siklus hidup token dYdX dirangkum dalam rangkaian data operasional berikut:

All-Time High Price (Variant A): $2.7291 (Date: 6 December 2024)

All-Time High Price (Variant B): $4.52 (Date: 7 March 2024)

All-Time High Price (INR Variant): ₹400.75 (Coinbase listing)

All-Time Low Price: $0.07881 (Date: 8 March 2026)

Under-200-day SMA Threshold: ~$0.276 (April 2026)

50-day SMA level: ~$0.098

Market Maker Agreement (Pulsar):

Loan Committed: 250,000 DYDX (~0.025% of total supply)

Agreement Term: 12 months (expiring 14 May 2026)

Execution Model: Loan-option structure with strike prices set at premiums

INKONSISTENSI:

Detail: Terjadi perbedaan pelaporan rekor ATH dYdX yang sangat tajam dalam basis data pasar. Sumber analitik altfins mencatatkan ATH berada di level $2,7291 pada 6 Desember 2024, sementara database RootData mencatatkan ATH di level $4,52 pada 7 Maret 2024. Coinbase mencatatkan ATH dalam rupee India (INR) sebesar ₹400,75 (setara ~$4,80). Perbedaan ekstrem ini disebabkan oleh pemisahan pelacakan antara token ethDYDX lama (Ethereum ERC-20) dengan token native DYDX (Cosmos L1) pasca-migrasi, di mana banyak sistem analitik gagal mengonsolidasikan data harga kedua rantai.

Evidence Level: LOW

Kondisi harga pada April 2026 menunjukkan keputusasaan pasar yang mendalam, di mana token DYDX diperdagangkan di kisaran ~$0,10 hingga $0,12, jauh di bawah SMA 200 harinya di level $0,276. Penurunan tajam lebih dari 95% dari ATH mencerminkan kombinasi sentimen negatif dari kekalahan volume perdagangan bulanan oleh Hyperliquid serta kemarahan komunitas ritel atas penghentian paksa bridge wethDYDX.

Namun, secara fundamental, token DYDX saat ini berada dalam kondisi sangat dinilai murah (undervalued) secara operasional. Kebijakan alokasi 75% pendapatan bursa untuk buyback otomatis harian memberikan jaminan penyerapan pasokan beredar secara konstan di pasar terbuka. Hal ini menempatkan DYDX pada posisi defensif yang sangat kuat untuk mengalami pembalikan arah positif yang tajam jika bursa mampu meningkatkan aktivitas transaksi on-chain.

## 14 Business Intelligence

Performa bisnis dYdX diukur melalui volume perdagangan kumulatif, pendapatan biaya bursa, efisiensi penyerapan staker, serta aktivitas rantai baru Arcus di Robinhood L2.

Seluruh metrik operasional bisnis dYdX dirangkum dalam rangkaian data berikut:

Lifetime Trading Volume (Oct 2025): Over $1.52 Trillion ($1.52T+)

Lifetime Trading Volume (Jan 2026): Over $1.55 Trillion ($1.55T+)

Cumulative Protocol Fees Generated (Oct 2025): ~$62,000,000

Cumulative Protocol Fees Generated (Jan 2026): $64,700,000

Staking Rewards Distributed in USDC (Oct 2025): Almost $50,000,000

Staking Rewards Distributed in USDC (Jan 2026): $48,000,000

Total DYDX Holders (Oct 2025): Over 92,000

Total DYDX Holders (Jan 2026): 98,200

Staked DYDX across Validators: Over 240,000,000 DYDX

Total DYDX Bought and Staked: 8,460,000 DYDX

Cumulative Buyback USD Market Value: $1.72M

MegaVault Total Value Locked (TVL) (Early 2025): >$79,000,000 USDC

Protocol Net Earnings (Q2 2024): $20,100,000

Protocol Net Earnings (Q2 2025): $3,200,000

Protocol Total Value Locked (TVL) (Oct 2021 Peak): $1,100,000,000

Protocol Total Value Locked (TVL) (Mid 2025): $312,000,000

Arcus TVL on Robinhood Chain (July 2026): $14,300,000

Robinhood Chain Metrics (July 2026):

Rantai TVL Total: $193,000,000

Morpho TVL: $116,000,000

Uniswap TVL: $61,000,000

Spark TVL: $8,000,000

Noxa TVL: $6,000,000

Cumulative DEX Volume: >$750,000,000

Total Chain Fees Collected: $1,140,000

Total App Fees Generated: ~$40,000,000

Uniswap Generated Fees: >$26,800,000

Stock Tokens Total Market Cap: $17,700,000

Stock Tokens in DeFi Ecosystem: $721,000

Stock Tokens Varieties Supported: 95 assets

Real World Asset Perpetual Markets: 35 markets

Metrik keuangan menunjukkan dinamika penurunan pendapatan operasional yang sangat masif sebesar 84,07% YoY dari $20,1 juta di Q2 2024 menjadi hanya $3,2 juta di Q2 2025. Hal ini merefleksikan pelarian likuiditas ke bursa pesaing. Namun, kemitraan strategis dYdX Labs dengan Robinhood lewat Arcus mulai menunjukkan potensi penyerapan modal baru yang signifikan. Di tengah dominasi aktivitas spekulatif memecoin di Robinhood Chain (di mana Uniswap menguasai 66,4% biaya aplikasi), Arcus berhasil menduduki peringkat ketiga bursa terbesar dengan TVL awal $14,3 juta. Meskipun adopsi saham terdigitalisasi masih berada di tahap awal (hanya $721.000 saham tokenisasi yang digunakan aktif dalam ekosistem DeFi), keberadaan Arcus di ekosistem RWA patuh regulasi memperluas jalan pemulihan bisnis dYdX di luar batas pengguna kripto murni.

## 15 Success & Failure Analysis

Evaluasi keberhasilan dan kegagalan dYdX dianalisis melalui delapan perspektif aktor ekosistem secara terpisah:

Perspective: Founder (Antonio Juliano)

Verdict: Campuran (Mixed)

Reasons: Berhasil membina bursa perp terdesentralisasi perintis bernilai triliunan dolar. Namun, pendiri mengalami kelelahan kepemimpinan yang berujung pada keputusan pengunduran dirinya sebagai CEO pada Mei 2024, sebelum akhirnya terpaksa kembali menjabat pada Oktober 2024 untuk memimpin restrukturisasi darurat dan melakukan PHK massal terhadap 35% karyawannya di dYdX Labs. Kemitraan Arcus pada 2026 adalah bukti kecerdikan taktisnya untuk keluar dari tekanan persaingan langsung.

Confidence Level: HIGH

Perspective: VC (a16z, Paradigm)

Verdict: Sukses (Success)

Reasons: Memperoleh porsi token besar dengan valuasi sangat rendah ($20M-$100M) dan sukses mencairkan sebagian besar modal mereka sebelum devaluasi besar pasca-2024.

Confidence Level: HIGH

Perspective: Retail (Ritel)

Verdict: Gagal (Failure)

Reasons: Mengalami kerugian modal parah karena harga jatuh >95% dari ATH, ditambah dengan sanksi penghentian jembatan wethDYDX yang mengunci token mereka.

Confidence Level: HIGH

Perspective: Community

Verdict: Campuran (Mixed)

Reasons: Program hibah berjalan stabil, namun terjadi perpecahan politik parah akibat dominasi voting validator dalam menutup akses bridge.

Confidence Level: HIGH

Perspective: Developer

Verdict: Sukses (Success)

Reasons: dYdX berhasil membuktikan kedaulatan appchain L1 Cosmos berkinerja tinggi, menerapkan designated proposer model, dan OEGS.

Confidence Level: HIGH

Perspective: Institution

Verdict: Campuran (Mixed)

Reasons: Fitur Permissioned Keys dan simplifikasi tingkat fee disambut baik, namun penurunan likuiditas dan volume pasar menghambat penyerapan komisi pembuatan pasar mereka.

Confidence Level: MEDIUM

Perspective: Validator

Verdict: Sukses (Success)

Reasons: Validator memegang peranan mutlak dalam mengamankan rantai dYdX Chain dan menarik komisi pembagian hasil USDC dari staker.

Confidence Level: HIGH

Perspective: Builder

Verdict: Sukses (Success)

Reasons: Integrasi lancar dengan IBC, Osmosis, dan platform oracle.

Confidence Level: HIGH

## 16 Historical Timeline

Perjalanan waktu pembangunan, kejayaan, kejatuhan, hingga restrukturisasi dYdX dirangkum dalam kronologi berikut:

19 Desember 2017 — dYdX menutup putaran Seed senilai $2.000.000 — Polychain Capital memimpin investasi awal bersama a16z untuk mendanai riset margin trading terdesentralisasi.

3 Oktober 2018 — Protokol dYdX v1 resmi diluncurkan di Ethereum mainnet — Memungkinkan transaksi margin dan spot non-kustodian pertama.

19 Oktober 2018 — Penutupan Seri A senilai $10.000.000 dipimpin a16z — Pendanaan bagi ekspansi struktur tim inti dYdX Labs.

26 Januari 2021 — dYdX mengamankan Seri B senilai $10.000.000 — Dipimpin Three Arrows Capital dan DeFiance Capital untuk mempersiapkan transisi ke StarkEx Layer 2.

Februari 2021 — Peluncuran L2 Perpetuals menggunakan teknologi StarkEx zk-rollup — Menghapus hambatan gas fee Ethereum dan mempercepat konfirmasi transaksi.

15 Juni 2021 — Putaran Seri C senilai $65.000.000 dipimpin oleh Paradigm — Penggalangan modal besar untuk memperkuat likuiditas di tengah ketidakstabilan pasar kripto.

3 Agustus 2021 — Blok genesis pencetakan 1 miliar token DYDX — Memulai peluncuran kampanye rewards bertahap selama 5 tahun.

September 2021 — Pembukaan klaim retroactive airdrop dan pengaktifan transferabilitas token — Mengakibatkan lonjakan volume transaksi besar karena keharusan pencapaian target aktivitas perdagangan.

November 2022 — Kolapsnya bursa terpusat FTX — Mendorong migrasi massal pedagang ke platform non-kustodian, menghasilkan lonjakan pengguna dYdX sebesar 39%.

26 Oktober 2023 — Pembuatan blok genesis dYdX Chain (v4) di ekosistem Cosmos — Memulai pengalihan fungsi utilitas token dari sekadar hak tata kelola menjadi instrumen konsensus rantai mandiri.

31 Oktober 2023 — Blockchain dYdX Chain resmi beroperasi penuh di mainnet — Memulai migrasi likuiditas lintas rantai dari StarkEx Ethereum ke Cosmos L1.

13 Mei 2024 — Antonio Juliano mundur sebagai CEO dYdX — Transisi kepemimpinan ke Ivo Crnkovic-Rubsamen akibat kejenuhan pribadi pendiri.

Agustus 2024 — Hyperliquid resmi melompati volume perdagangan bulanan dYdX — Menandai berakhirnya era dominasi dYdX akibat kelemahan insentif tokenomika.

10 Oktober 2024 — Antonio Juliano kembali menjabat sebagai CEO dYdX — Restorasi kepemimpinan pendiri untuk menavigasi krisis daya saing platform.

28 Oktober 2024 — Penutupan permanen platform dYdX v3 StarkEx — Memusatkan seluruh likuiditas dan operasional pembangunan ke dYdX Chain v4.

30 Oktober 2024 — PHK massal terhadap 35% staf dYdX — Restrukturisasi drastis untuk menyeimbangkan pengeluaran di tengah kemerosotan volume operasional.

19 November 2024 — Peningkatan besar dYdX Unlimited dirilis di mainnet — Meluncurkan fungsionalitas Instant Market Listings dan pembuatan pasar MegaVault USDC.

23 April 2025 — Inisiasi program buyback token dYdX pertama — Pembelian kembali otomatis dengan mengalokasikan 12,5% pendapatan operasional bursa.

13 Juni 2025 — Penonaktifan resmi jembatan lintas-rantai wethDYDX — Menyebabkan kepanikan karena 14% suplai terdampar di Ethereum, merugikan sekitar 13.800 alamat pemegang.

18 Juli 2025 — dYdX mengakuisisi aplikasi sosial Telegram Pocket Protector — Eddie Zhang resmi diangkat menjadi President dYdX Labs untuk memimpin divisi ritel Telegram.

September 2025 — Integrasi fungsionalitas perdagangan langsung di Telegram — Langkah diversifikasi distribusi akses sosial media massal.

13 November 2025 — Komunitas menyetujui pemungutan suara Proposal #313 — Mengatrol alokasi program buyback hingga tingkat ekstrem 75% pendapatan protokol.

11 Desember 2025 — dYdX meluncurkan produk spot trading Solana — Membuka akses likuiditas di luar jaringan EVM dan Cosmos.

1 Juli 2026 — dYdX Labs bersama Robinhood mengumumkan platform bursa terdesentralisasi Arcus di atas Robinhood Chain — Pivot strategis raksasa yang menandai perluasan operasional menuju komoditas tradisional dan saham tokenisasi RWA.

## 17 Current Status

Saat ini, dYdX berada pada kondisi bifurkasi operasional yang sangat kontras. Di satu sisi, rantai utama dYdX Chain berbasis Cosmos (v4) mengalami fase stagnasi aktivitas perdagangan sekunder akibat migrasi masif modal ritel menuju bursa derivatif kripto-asli berkinerja tinggi. Hal ini terlihat jelas dari penurunan pendapatan bersih triwulanan bursa v4 yang hanya membukukan $3,2 juta pada pertengahan 2025. Kendati demikian, infrastruktur rantai Cosmos tersebut beroperasi sangat stabil di bawah pengawasan komunitas, didukung oleh tingkat keamanan konsensus yang kokoh dengan lebih dari 240 juta koin DYDX di-stake aktif. Program buyback agresif 75% yang berjalan harian juga memberikan bantalan beli otomatis yang menjaga token asli dari kejatuhan harga lebih dalam.

Di sisi lain, masa depan pertumbuhan ekosistem dYdX kini bertumpu pada Arcus di Robinhood Chain. Dirilis pada 1 Juli 2026 bersamaan dengan peluncuran mainnet rantai L2 berlisensi tersebut, Arcus langsung memimpin segmen bursa terdesentralisasi khusus aset dunia nyata (RWA) dengan TVL awal mencapai $14,3 juta. Arcus memosisikan dYdX Labs di garis depan inovasi keuangan terdigitalisasi 24/7 yang patuh aturan, membuka akses bagi bursa untuk menarik basis likuiditas non-kripto milik jutaan nasabah tradisional Robinhood.

## 18 Lessons Learned

Siklus hidup dYdX menyajikan sejumlah pelajaran berharga yang mendasar bagi pembangunan ekosistem DeFi masa depan:

Pentingnya Keselarasan Akumulasi Nilai Riil Token (Value Accrual Over Governance): Salah satu kesalahan terbesar dYdX v3 adalah mengisolasi seluruh keuntungan biaya bursa ke kas perusahaan terpusat, menyisakan token DYDX sebagai instrumen tata kelola kosong yang mengalami tekanan inflasi emisi konstan. Sebuah proyek DeFi akan selalu kalah bersaing dari kompetitor yang membagi hasil operasional bursa secara langsung dan agresif kepada pemegang token asli mereka.

Friksi Pengguna Adalah Pembunuh Tersembunyi (The User Friction Trap): Keputusan dYdX memindahkan bursa dari Ethereum L2 ke Cosmos L1 memaksa pengguna melewati rantai jembatan manual yang rumit dan lambat, bertepatan dengan lahirnya kompetitor sub-detik yang menyederhanakan deposit. Kemudahan antarmuka pengguna (UI/UX) dan efisiensi waktu penyelesaian transaksi adalah benteng pertahanan pertama dalam persaingan memperebutkan likuiditas pedagang frekuensi tinggi.

Kebijakan Pemutusan Bridge Tanpa Kompensasi Merusak Integritas Jangka Panjang: Penutupan tergesa-gesa jembatan wethDYDX pada Juni 2025 yang mengabaikan kepemilikan 13.800 dompet lama adalah preseden buruk. Tindakan ini menghancurkan loyalitas pendukung awal ekosistem Ethereum, menunjukkan bahwa kedaulatan validator dalam pemungutan suara on-chain dapat merugikan pemegang koin pasif.

Ketangkasan Poros Pendiri Adalah Kunci Kelangsungan Hidup (Founder Pivot Agility): Kemampuan Antonio Juliano untuk mengenali pergeseran persaingan, melakukan restrukturisasi PHK 35% di dYdX Labs untuk efisiensi modal, mengintegrasikan platform Telegram trading, dan akhirnya menjalin kemitraan raksasa dengan Robinhood untuk beralih ke ranah saham tokenisasi RWA lewat Arcus adalah contoh kepemimpinan adaptif. Kelenturan taktis ini menjauhkan ekosistem dari kepunahan akibat persaingan pasar kripto murni yang jenuh.

## 19 Knowledge Extraction Candidate (BAGIAN PALING PENTING)

Bagian ini menyajikan ekstraksi Candidate Ontology, Hubungan, dan Pola Kejadian terstruktur untuk sistem kecerdasan buatan (Crypto Intelligence Framework):

Candidate Entities:

dYdX Labs (Organization)

dYdX Foundation (Organization)

dYdX Chain (L1 Blockchain)

Antonio Juliano (Person/Founder)

Eddie Zhang (Person/CEO of Arcus)

Arcus (DEX/Protocol)

Robinhood Crypto (Organization)

Robinhood Chain (L2 Blockchain)

Pocket Protector (Application)

MegaVault (Protocol Component)

Candidate Relationships (Ontology):

[Antonio Juliano] -> mendirikan -> [dYdX Labs]

[dYdX Labs] -> mengembangkan -> [dYdX Chain]

[dYdX Labs] -> mengakuisisi -> [Pocket Protector]

[Eddie Zhang] -> menjabat sebagai -> [CEO of Arcus]

[dYdX Labs] -> mengembangkan -> [Arcus]

[Arcus] -> bermitra dengan -> [Robinhood Crypto]

[Arcus] -> beroperasi di atas -> [Robinhood Chain]

[dYdX Chain] -> mengintegrasikan -> [MegaVault]

Candidate Patterns:

Nama Pola: Pola Kerentanan Tokenomika Tata Kelola Kosong (Governance Token Vulnerability Pattern)

Rantai Sebab-Akibat: Peluncuran bursa dengan total biaya mengalir ke kas terpusat -> Token hanya memiliki fungsi tata kelola dan emisi insentif harian tinggi -> Tekanan jual ritel konstan tanpa penyerapan beli pasar riil -> Kinerja harga merosot tajam -> Kehilangan loyalitas komunitas saat kompetitor meluncurkan sistem buyback dari biaya bursa.

Nama Pola: Pola Penyelematan Nilai Defensif (Buyback Accrual Redesign Pattern)

Rantai Sebab-Akibat: Terjadinya penurunan volume transaksi akibat kalah saing -> Komunitas merancang ulang fungsi token asli -> Meningkatkan porsi alokasi pendapatan operasional bursa hingga tingkat ekstrem (>70%) untuk melakukan buyback harian otomatis -> Terjadi penyerapan suplai beredar di pasar sekunder secara konstan.

Nama Pola: Pola Pivot Kanal Distribusi Ritel Tradisional (Traditional Broker Integration Pivot Pattern)

Rantai Sebab-Akibat: Kejenuhan pasar perdagangan derivatif kripto murni -> Memilih rantai khusus patuh hukum -> Meluncurkan bursa khusus saham terdigitalisasi dan perpetual RWA -> Mengintegrasikan bursa langsung ke jalur distribusi broker berlisensi dengan jutaan nasabah aktif -> Mengamankan likuiditas di luar ekosistem kripto-asli.

## 20 Transferable Intelligence

Jika AI harus mengevaluasi proyek bursa derivatif terdesentralisasi (DEX) baru, beberapa indikator evaluasi dari kasus dYdX dapat dijadikan pedoman analisis umum:

Aturan Evaluasi Akumulasi Nilai Jaringan (Value Capture Distribution Rule):

Aturan Umum (General Rule): AI wajib memberikan penilaian risiko tinggi pada proyek bursa terdesentralisasi yang menyalurkan biaya transaksi riil hanya ke dompet tim atau memberikan insentif staker dalam bentuk emisi token inflasi baru. Bursa berkinerja tinggi hanya layak mendapatkan penilaian superior jika menyalurkan >50% dari pendapatan riil harian (dalam koin stabil/USDC) untuk melakukan pembelian kembali (buyback) otomatis di pasar sekunder secara on-chain.

Aturan Hambatan Pengguna Maksimal (Max User Friction Threshold Rule):

Aturan Umum (General Rule): Setiap keputusan proyek memindahkan basis transaksinya dari bursa L2 terintegrasi menuju rantai L1 berdaulat yang mengharuskan pengguna melakukan jembatan lintas-rantai (bridge) manual >2 langkah akan memicu penyusutan volume perdagangan sebesar minimal 40%. AI harus mendepresiasi penilaian potensi pertumbuhan bursa appchain Cosmos jika bursa tersebut tidak mengintegrasikan deposit satu-klik langsung dari bursa L1 besar.

Indikator Khusus Kemitraan RWA (Specific RWA Partnership Metric):

Indikator Khusus dYdX (Special Indicator): Penilaian bursa RWA Arcus tidak dapat disamakan dengan DEX biasa karena Arcus bergantung pada lisensi hukum dan distribusi tertutup Robinhood. AI wajib menilai performa Arcus berdasarkan rasio konversi nasabah broker Robinhood menjadi pelaku transaksi derivatif on-chain.

## 21 Open Questions

Apakah Arcus mampu mengonversi basis pedagang ritel tradisional Robinhood menjadi pelaku transaksi RWA perpetual yang aktif secara berkelanjutan, mengingat sifat instrumen leverage 50x yang membutuhkan tingkat literasi manajemen risiko keuangan yang jauh lebih tinggi daripada perdagangan spot saham biasa?

Adakah rencana kompensasi struktural yang disiapkan oleh dYdX Operations subDAO untuk mengembalikan nilai ekonomis dari 14% pasokan koin (termasuk 41,657,249 DYDX) milik 13.800 alamat pengguna yang terdampar secara permanen di Ethereum setelah penutupan bridge wethDYDX pada Juni 2025?

Bagaimana kelangsungan status hukum kepatuhan dYdX Labs dalam menawarkan perdagangan spot dan perpetual di yurisdiksi Amerika Serikat pada akhir 2025 di bawah dinamika regulasi komoditas dan sekuritas terbaru?

## 22 Evidence Level

Setiap kesimpulan analitis utama dalam laporan ini didasarkan pada tingkat kekuatan bukti (evidence levels) berikut:

Struktur Pendanaan dYdX (Seed hingga Seri C): HIGH. Didukung oleh dokumen penggalangan dana resmi dYdX Labs, data cap table PitchBook, blog Paradigm, dan siaran pers sekuritas CoinDesk.

Analisis Kekalahan Pangsa Pasar dYdX terhadap Hyperliquid: HIGH. Dibuktikan secara rinci oleh perbandingan data on-chain volume bulanan, struktur biaya bursa komparatif, dan penelusuran sejarah tokenomika di GitHub.

Detail Dampak Penutupan Jembatan wethDYDX: MEDIUM. Jumlah dompet terdampak (~13.800) bersumber langsung dari forum diskusi tata kelola dYdX Chain, namun nilai nominal kumulatif dompet tidak aktif tersebut belum diaudit secara publik oleh akuntan eksternal.

Prospek Masa Depan Arcus RWA di Robinhood: LOW. Layanan baru diresmikan pada Juli 2026, sehingga data tren retensi pengguna murni dan volume komoditas masih berada di tahap interpretasi spekulatif awal.

## 23 Karya yang dikutip

People at dYdX — https://wellfound.com/company/dydx/people

About DYDX — https://www.coinbase.com/en-in/price/dydxv4

Rain Management Risk Disclosures — https://www.rain.com/legal/rain-management-wll-risk-disclosures

Central Clearing of Crypto-Derivatives in DeFi — https://www.researchgate.net/publication/361390600_CENTRAL_CLEARING_OF_CRYPTO-DERIVATIVES_IN_A_DECENTRALIZED_FINANCE_DeFi_FRAMEWORK_AN_EXPLORATORY_REVIEW

Crypto Influencers Colour — https://artgee6.medium.com/crypto-influencers-colour-ba8ca054c7f5

Solana Solend Solislend Save Protocol — https://www.binance.com/en/square/post/11724625210042

dYdX Funding Rounds — https://wellfound.com/company/dydx/funding

dYdX Fundraising Details — https://dropstab.com/coins/dydx/fundraising

Token Transparency dYdX Filing — https://blockworks.com/token-transparency/filing/dydx--2

dYdX Caplight Comps — https://www.caplight.com/company/dydx-1

dYdX Project Detail RootData — https://www.rootdata.com/projects/detail/dYdX?k=MTI2Mw%3D%3D

dYdX Labs Valuation and Funding History PitchBook — https://pitchbook.com/profiles/company/223497-19

Perpetual DEX Security Evolution — https://hacken.io/discover/perpetual-dex-security-evolution/

Diving Deep into Decentralised Perpetual Futures — https://www.dwf-labs.com/research/373-diving-deep-into-decentralised-perpetual-futures-an-ecosystem-overview-and-strategic-analysis

Liquidity Pools vs Order Books in DeFi — https://medium.com/@gwrx2005/liquidity-pools-vs-order-books-in-defi-a-comparative-analysis-88be9118ab80

Decentralized Finance Technologies — https://hkifoa.com/wp-content/uploads/2024/11/decentralized-finance-technologies-global-millennial-capital.pdf

Exploring the Cosmos Network — https://www.galaxy.com/insights/research/exploring-the-cosmos

Navigating DeFi Derivatives — https://research.binance.com/static/pdf/navigating-defi-derivatives-.pdf

How Crypto Works: Chapter 10 Hyperliquid — https://github.com/lawmaster10/howcryptoworksbook/blob/master/Chapters/ch10_hyperliquid.md

PoUW Blockchain Competitive Equilibrium Model — https://ic3research.org/projects/

Exploring Hyperliquid: Redefining Derivatives Trading — https://www.vaneck.com/nl/en/blog/digital-assets/exploring-hyperliquid-redefining-derivatives-trading/

The Tokenomics of dYdX (Detailed Review) — https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-dydx/r/Vm8xr9SHi31vNF6qQCiRv3

SoK: Comprehensive Analysis of Token Allocations — https://www.researchgate.net/publication/395390758_SoK_Comprehensive_Analysis_of_Token_Allocations_Distributions_and_their_Effect_on_Token_Value_and_User_Participation

Token Growth Valuation Index — https://www.binance.com/en/square/profile/mtcapital

Edward Zhang Official Path — https://www.edwardzhang.com/

dYdX Token Transparency Filing Blockworks — https://blockworks.com/token-transparency/filing/dydx--2

dYdX Plans US Market Entry Spot Trading — https://coinmarketcap.com/academy/article/dydx-plans-us-market-entry-by-year-end-with-spot-trading

dYdX Acquires Telegram Pocket Protector — https://www.latimes.com/b2b/banking-finance/story/2025-07-28/dydx-acquires-pocket-protector

dYdX Unveils 2025 Roadmap — https://www.binance.com/en/square/post/08-28-2025-dydx-unveils-2025-roadmap-amid-declining-earnings-28938351992714

dYdX Foundation October Analyst Call — https://www.dydx.foundation/blog/dydx-foundation-hosts-october-analyst-call-featuring-dydx-labs-metrics-milestones-and-whats-next

dYdX Chain: Community Owned, Unchanged — https://www.dydx.foundation/blog/dydx-chain-community-owned-unchanged

dYdX Collaborates with Robinhood to Launch Arcus — https://www.bitget.com/asia/amp/news/detail/12560605489681

dYdX Chain Updates and Roadmap — https://coinmarketcap.com/cmc-ai/dydx-chain/latest-updates/

Arcus Project Profile RootData — https://www.rootdata.com/projects/detail/Arcus?k=MjUxOTQ%3D

Robinhood links with dYdX Labs to launch Arcus — https://id.tradingview.com/news/cointelegraph:8ff4a296e094b:0-robinhood-links-with-dydx-labs-to-launch-new-dex-arcus/

Key Facts: dYdX Rebrands Arcus on Robinhood Chain — https://www.tradingview.com/news/tradingview:c0b6e5de43fac:0-key-facts-dydx-rebrands-arcus-on-robinhood-chain-hood-expands-crypto/

Chorus One Staking Networks — https://chorus.one/crypto-staking-networks/ethereum

SoK Analysis of Token Allocations and Distributions — https://www.researchgate.net/publication/395390758_SoK_Comprehensive_Analysis_of_Token_Allocations_Distributions_and_their_Effect_on_Token_Value_and_User_Participation

Auditor Book: Vulnerability Findings — https://www.scribd.com/document/689401992/The-Auditor-Book

Darcy W. E. Allen RMIT Blockchain Coevolutionary Theory of Airdrops — https://d-nb.info/1353482103/34

DEX Gas Refund Programs — https://www.nadcab.com/blog/gas-refund-in-dex

Reflexivity Research November 2025 in Review — https://coinmarketcap.com/academy/article/reflexivity-research-november-2025-in-review

dYdX 2025 Ecosystem Annual Report — https://www.dydx.xyz/annual-report/annual-report-2025

dYdX Allocates 75% Fees for Buyback — https://www.binance.com/en/square/post/11-13-2025-dydx-foundation-allocates-75-of-protocol-revenue-for-token-buyback-32336305438890

dYdX Landmark Buyback 75% Passed — https://99bitcoins.com/news/altcoins/dydx-pass-landmark-buyback-allocating-75-of-revenue-to-dydx-token-repurchases/

Tokenomics of dYdX Chain Analysis — https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-dydx/r/Vm8xr9SHi31vNF6qQCiRv3

dYdX Net Revenue Distribution Model — https://blockworks.com/token-transparency/filing/dydx--2

Crypto Airdrop Models: Retroactive Model Proliferation — https://blog.ueex.com/crypto-terms/crypto-airdrop/

Evolution of Token Distribution: Liquidity Mining and Retroactive Airdrops — https://public.bnbstatic.com/static/files/research/the-evolution-of-tokens-over-the-years.pdf

Introducing DYDX Governance Token — https://www.dydx.foundation/blog/introducing-dydx-token

Retroactive Mining Rewards Rules — https://www.dydx.foundation/blog/retroactive-mining

Best Crypto Airdrops in History: dYdX Volume Criteria — https://www.webopedia.com/crypto/learn/best-crypto-airdrops-in-history/

dYdX Launches Permissionless Listings on Unlimited Upgrade — https://thedefiant.io/news/defi/dydx-launches-permissionless-listings-with-unlimited-upgrade

dYdX Codebase Upgrades and Designated Proposers — https://coinmarketcap.com/cmc-ai/dydx-chain/latest-updates/

dYdX Foundation Blog and MegaVault Operator — https://www.dydx.foundation/blog

Exploring dYdX Unlimited Potential Impact — https://coingape.com/exploring-dydx-unlimiteds-potential-impact-on-the-decentralized-trading-market/

dYdX Buyback Program and Bridge Ending Announcement — https://www.dydx.xyz/blog/dydx-buyback-program

dYdX Mission Statement and Revenue Streams — https://businessmodelcanvastemplate.com/blogs/mission/dydx-mission

The On-Chain Trading Market: From Niche to Infrastructure — https://www.vaneck.com/nl/en/blog/digital-assets/the-on-chain-trading-market-from-niche-to-infrastructure/

Perpetual Futures Trading Engine and dYdX Clones — https://www.suffescom.com/development/dydx-clone-development

DeFi Market Stats and L2 Scaling — https://patentpc.com/blog/defi-market-stats-tvl-protocol-growth-user-trends

Institutional Adoption and Onchain Infrastructure — https://cryptorank.io/insights/research/institutional-adoption-and-onchain-infrastructure

dYdX Price Prediction and Technical Indicators — https://zipmex.com/blog/dydx-price-prediction/

DeFiLlama Protocol Fees and Revenue Tracker — https://defillama.com/revenue

dYdX CEO Layoffs and Buyback Debut — https://crypto.news/tag/dydx/

Founder Steps Down and Board Chair Roles — https://www.bitget.com/sitemap/news/4312

Polygon DeFi Head and Antonio Juliano Transitions — https://www.blocmates.com/news-posts/polygon-head-of-defi-joins-berachain-dydx-ceo-steps-down

Antonio Juliano Returns as CEO after 6 Months — https://www.theblock.co/post/320502/dydx-trading-founder-antonio-juliano-returns-as-ceo-after-stepping-away-for-six-months

DYDX Price Overview and MACD Indicator — https://altfins.com/crypto-screener/dydx-dydx

Crypto Bahamas Conference Highlights — https://gravityteam.co/blog/crypto-bahamas-conference-highlights/

Pulsar Token Loan and MM Agreements — https://blockworks.com/token-transparency/filing/dydx--2

Initial Allocation and Supply of DYDX — https://www.dydx.foundation/blog/introducing-dydx-token

Project Introduction and Commission — https://www.binance.com/en/square/post/1770614

The Crypto Masters Guide to Uniswap and VCs — https://medium.com/the-crypto-masters-guide-tcmg/top-10-crypto-projects-dexs-c3890c0fc788

Retroactive Mining Claim Milestones — https://www.dydx.foundation/blog/retroactive-mining

ethDYDX to Native DYDX Migration and Bridge Shut Down — https://www.weusecoins.com/what-is-dydx/

dYdX Foundation delegation and semi-annual reports — https://www.dydx.foundation/blog

Cryptoalerting List — https://cryptocurrencyalerting.com/coins.html?07SQZkTmpMW=zYmzK9fDvt

Forum dYdX Chain: Bridge Cease Support Discussions — https://dydx.forum/t/drc-cease-support-for-the-wethdydx-smart-contract-i-e-the-bridge-on-the-dydx-chain-side/3619

Cryptoalerting Index — https://cryptocurrencyalerting.com/coins.html?nGUOmp=Q4FonGjOzyVyGvK

Robinhood Chain Launch and Stock Tokens Metrics — https://oakresearch.io/en/analyses/investigations/who-is-biggest-winner-robinhood-chain-launch-uniswap-but-not-really

Robinhood links with dYdX Labs Arcus — https://www.binance.com/ar/square/post/340302305001602

Robinhood Crypto and Bitget Integration — https://www.binance.com/en-AE/square/post/340302305001602

Cointelegraph Arcus Launch — https://id.tradingview.com/news/cointelegraph:8ff4a296e094b:0

Robinhood Chain Mainnet Launch and RWA Projects — https://news.futunn.com/en/post/76109384/mainnet-launch-day-ignites-how-the-top-10-rwa-projects

RootData Perp Tag Projects — https://www.rootdata.com/projects?sd=138

Initial Mint and Supply Breakdown — https://www.dydx.foundation/blog/introducing-dydx-token

Volume and Fee Metrics dYdX 2025 Annual Report — https://www.dydx.xyz/annual-report/annual-report-2025

dYdX Raises Series C from Paradigm — https://www.dydx.xyz/blog/series-c

dYdX Funding rounds Wellfound Database — https://wellfound.com/company/dydx/funding

dYdX Staking Specifics and Team — https://www.figment.io/insights/dydx-first-look/

Chainbroker dYdX Token Distribution — https://chainbroker.io/projects/dydx/

Paradigm Venture Capital and Performance — https://coin98.net/what-is-paradigm

Karya yang dikutip

1. DYDX Price, COSMOSDYDX Price, Live Charts, and Marketcap - Coinbase India, https://www.coinbase.com/en-in/price/dydxv4 2. A Security-Centric Analysis of Perpetual DEX Evolution and a Blueprint for Resilience, https://hacken.io/discover/perpetual-dex-security-evolution/ 3. Deep Look into a Space of Decentralized Perpetual Futures - DWF Labs, https://www.dwf-labs.com/research/373-diving-deep-into-decentralised-perpetual-futures-an-ecosystem-overview-and-strategic-analysis 4. dYdX Token Transparency Filing - Blockworks, https://blockworks.com/token-transparency/filing/dydx--2 5. Liquidity Pools vs. Order Books in DeFi: A Comparative Analysis | by Jung-Hua Liu - Medium, https://medium.com/@gwrx2005/liquidity-pools-vs-order-books-in-defi-a-comparative-analysis-88be9118ab80 6. What are Mission Vision & Core Values of dYdX Company? – businessmodelcanvastemplate.com - Business Model Canvas Templates, https://businessmodelcanvastemplate.com/blogs/mission/dydx-mission 7. The Tokenomics of dYdX: Supply, Staking, and Governance, https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-dydx/r/Vm8xr9SHi31vNF6qQCiRv3 8. DYdX collaborates with Robinhood to launch Arcus: Strategic upgrade or the marginalization of native public chains? | Bitget News, https://www.bitget.com/asia/amp/news/detail/12560605489681 9. howcryptoworksbook/Chapters/ch10_hyperliquid.md at master - GitHub, https://github.com/lawmaster10/howcryptoworksbook/blob/master/Chapters/ch10_hyperliquid.md 10. Annual Report 2025 - dYdX, https://www.dydx.xyz/annual-report/annual-report-2025 11. Exploring Hyperliquid: Redefining Derivatives Trading - VanEck, https://www.vaneck.com/nl/en/blog/digital-assets/exploring-hyperliquid-redefining-derivatives-trading/ 12. dYdX Pass Landmark Buyback Allocating 75% of Revenue to DYDX Token Repurchases, https://99bitcoins.com/news/altcoins/dydx-pass-landmark-buyback-allocating-75-of-revenue-to-dydx-token-repurchases/ 13. Who Is the Biggest Winner of the Robinhood Chain Launch? Uniswap, but Not Really, https://oakresearch.io/en/analyses/investigations/who-is-biggest-winner-robinhood-chain-launch-uniswap-but-not-really 14. The On-Chain Trading Market: From Niche to Infrastructure | VanEck, https://www.vaneck.com/nl/en/blog/digital-assets/the-on-chain-trading-market-from-niche-to-infrastructure/ 15. dYdX Price Prediction 2026–2030: Expert DYDX Forecast - Zipmex, https://zipmex.com/blog/dydx-price-prediction/ 16. CENTRAL CLEARING OF CRYPTO-DERIVATIVES IN A DECENTRALIZED FINANCE (DeFi) FRAMEWORK: AN EXPLORATORY REVIEW - ResearchGate, https://www.researchgate.net/publication/361390600_CENTRAL_CLEARING_OF_CRYPTO-DERIVATIVES_IN_A_DECENTRALIZED_FINANCE_DeFi_FRAMEWORK_AN_EXPLORATORY_REVIEW 17. dYdX Closes $65M Series C, https://www.dydx.xyz/blog/series-c 18. dYdX: Founder, Leadership & Team - Wellfound, https://wellfound.com/company/dydx/people 19. dYdX | Valuation, Funding Rounds & Stock Price - Caplight, https://www.caplight.com/company/dydx-1 20. Eddie Zhang, https://www.edwardzhang.com/ 21. West Hollywood Trading App Acquired to Expand Currency Technology - LA Times, https://www.latimes.com/b2b/banking-finance/story/2025-07-28/dydx-acquires-pocket-protector 22. dYdX DYDX Fundraising, Investors & Funding Rounds | DropsTab, https://dropstab.com/coins/dydx/fundraising 23. dYdX: First Look - Figment.io, https://www.figment.io/insights/dydx-first-look/ 24. What is Paradigm? A Crypto-native Venture Capital - Upside, https://coin98.net/what-is-paradigm 25. Decentralized Finance Technologies, https://hkifoa.com/wp-content/uploads/2024/11/decentralized-finance-technologies-global-millennial-capital.pdf 26. Retroactive Mining - dYdX Foundation, https://www.dydx.foundation/blog/retroactive-mining 27. dYdX Funding Rounds, Valuation & Investors - Wellfound, https://wellfound.com/company/dydx/funding 28. dYdX Project Introduction, Team, Financing and News_RootData | RootData, https://www.rootdata.com/projects/detail/dYdX?k=MTI2Mw%3D%3D 29. Latest dYdX News - (DYDX) Future Outlook, Trends & Market Insights - CoinMarketCap, https://coinmarketcap.com/cmc-ai/dydx-chain/latest-updates/ 30. DYdX Launches Permissionless Listings With Unlimited Upgrade - The Defiant, https://thedefiant.io/news/defi/dydx-launches-permissionless-listings-with-unlimited-upgrade 31. dYdX Foundation Blog, https://www.dydx.foundation/blog 32. Exploring dYdX Unlimited's Potential Impact on the Decentralized Trading Market, https://coingape.com/exploring-dydx-unlimiteds-potential-impact-on-the-decentralized-trading-market/ 33. navigating-defi-derivatives-.pdf - Binance Research, https://research.binance.com/static/pdf/navigating-defi-derivatives-.pdf 34. Exploring the Cosmos Blockchain | Inside the Cosmos Ecosystem - Galaxy, https://www.galaxy.com/insights/research/exploring-the-cosmos 35. dYdX Clone Development | Perpetual DEX in 4–8 Weeks, https://www.suffescom.com/development/dydx-clone-development 36. dYdX Foundation Hosts October Analyst Call Featuring dYdX Labs: Metrics, Milestones, and What's Next, https://www.dydx.foundation/blog/dydx-foundation-hosts-october-analyst-call-featuring-dydx-labs-metrics-milestones-and-whats-next 37. Key facts: dYdX Rebrands Arcus on Robinhood Chain; HOOD Expands Crypto, https://www.tradingview.com/news/tradingview:c0b6e5de43fac:0-key-facts-dydx-rebrands-arcus-on-robinhood-chain-hood-expands-crypto/ 38. Arcus Project Introduction, Team, Financing and News_RootData | RootData, https://www.rootdata.com/projects/detail/Arcus?k=MjUxOTQ%3D 39. dYdX Labs 2026 Company Profile: Valuation, Funding & Investors | PitchBook, https://pitchbook.com/profiles/company/223497-19 40. dYdX (DYDX) Price, Investors & Funding, Charts, Market Cap | Chain Broker, https://chainbroker.io/projects/dydx/ 41. Introducing DYDX | dYdX Foundation, https://www.dydx.foundation/blog/introducing-dydx-token 42. What Is a Crypto Airdrop? Complete Guide - UEEx Technology, https://blog.ueex.com/crypto-terms/crypto-airdrop/ 43. dYdX Unveils 2025 Roadmap Amid Declining Earnings - Binance, https://www.binance.com/en/square/post/08-28-2025-dydx-unveils-2025-roadmap-amid-declining-earnings-28938351992714 44. Learn about dYdX, the leading project in the on-chain derivatives market | 马力奥吃币 on Binance Square, https://www.binance.com/en/square/post/1770614 45. Mainnet Launch Day Ignites: How the Top 10 RWA Projects Are Dividing the Ecosystem's Upside, https://news.futunn.com/en/post/76109384/mainnet-launch-day-ignites-how-the-top-10-rwa-projects 46. The Projects with Perp Tag - RootData, https://www.rootdata.com/projects?sd=138 47. dYdX Community Launches First-Ever DYDX Buyback Program, https://www.dydx.xyz/blog/dydx-buyback-program 48. [DRC] Cease support for the wethDYDX Smart Contract (i.e., the Bridge) on the dYdX Chain side - Proposals, https://dydx.forum/t/drc-cease-support-for-the-wethdydx-smart-contract-i-e-the-bridge-on-the-dydx-chain-side/3619 49. What Is dYdX? - WeUseCoins, https://www.weusecoins.com/what-is-dydx/ 50. dYdX Foundation Allocates 75% of Protocol Revenue for Token Buyback - Binance, https://www.binance.com/en/square/post/11-13-2025-dydx-foundation-allocates-75-of-protocol-revenue-for-token-buyback-32336305438890 51. Crypto airdrops: An evolutionary approach, https://d-nb.info/1353482103/34 52. DYDX price - DYDX value, charts and news | Altfins, https://altfins.com/crypto-screener/dydx-dydx 53. Reflexivity Research: November 2025 in Review - CoinMarketCap, https://coinmarketcap.com/academy/article/reflexivity-research-november-2025-in-review 54. dYdX Chain: Community Owned, Unchanged, https://www.dydx.foundation/blog/dydx-chain-community-owned-unchanged 55. Latest dYdX News - Crypto News, https://crypto.news/tag/dydx/ 56. Polygon Head of DeFi Joins Berachain, dYdX CEO Steps Down - Blocmates, https://www.blocmates.com/news-posts/polygon-head-of-defi-joins-berachain-dydx-ceo-steps-down 57. DYdX Trading Founder Antonio Juliano returns as CEO after stepping away for six months, https://www.theblock.co/post/320502/dydx-trading-founder-antonio-juliano-returns-as-ceo-after-stepping-away-for-six-months 58. SoK: Comprehensive Analysis of Token Allocations, Distributions, and Their Effect on Token Value and User Participation - ResearchGate, https://www.researchgate.net/publication/395390758_SoK_Comprehensive_Analysis_of_Token_Allocations_Distributions_and_their_Effect_on_Token_Value_and_User_Participation 59. dYdX Plans U.S. Market Entry by Year-End With Spot Trading | CoinMarketCap, https://coinmarketcap.com/academy/article/dydx-plans-us-market-entry-by-year-end-with-spot-trading
