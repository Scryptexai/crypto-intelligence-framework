Laporan Analisis Sistematis Jaringan Cardano (ADA): Rekayasa Arsitektur, Evolusi Tata Kelola, dan Masa Transisi Infrastruktur Desentralisasi

## 1 Executive Summary

Jaringan Cardano berdiri sebagai salah satu proyek blockchain Layer 1 paling terkemuka yang dikembangkan dengan metodologi berbasis penelitian ilmiah terverifikasi (peer-reviewed) dan jaminan verifikasi formal. Laporan komprehensif ini menganalisis secara mendalam seluruh siklus hidup Jaringan Cardano, mulai dari konsepsi awal pada tahun 2015 oleh Charles Hoskinson dan Jeremy Wood, penggalangan dana berbasis voucher yang didominasi oleh partisipan dari Jepang, evolusi ledger melalui lima era utama (Byron, Shelley, Goguen, Basho, dan Voltaire), hingga restrukturisasi drastis arsitektur teknis dan tata kelola pada tahun 2026. Analisis ini menyoroti bagaimana transisi dari kepemimpinan Input Output Global (IOG) ke tata kelola komunitas on-chain yang diwakili oleh Intersect Member-Based Organization (MBO) dan penyerahan pengembangan node kepada entitas spesialis eksternal seperti Se7en Labs dan Teragone berfungsi sebagai reset struktural yang krusial bagi masa depan Cardano. Melalui Crypto Intelligence Framework (CIF), dokumen ini dirancang untuk menyediakan basis pengetahuan yang dapat digunakan kembali (reusable knowledge) guna menganalisis fungsionalitas, tokenomika, dinamika pasar, serta model konsensus pembuktian kepemilikan (Proof-of-Stake) dalam lanskap industri Web3 global.

## 2 Industry Background

Kondisi industri mata uang kripto sebelum Cardano lahir pada tahun 2015 dicirikan oleh keterbatasan arsitektur generasi pertama dan kedua. Jaringan Bitcoin sebagai representasi generasi pertama memiliki keterbatasan struktural berupa ketidakmampuan untuk menjalankan logika pemrograman yang kompleks (smart contracts) secara efisien akibat model Script yang terbatas. Lahirnya Ethereum pada tahun 2015 memperkenalkan mesin virtual global (Ethereum Virtual Machine/EVM) berbasis akun yang dinamis, namun model ini segera menghadapi tantangan skalabilitas yang berat, biaya transaksi yang tidak dapat diprediksi, serta kerentanan keamanan yang tinggi. Narasi industri saat itu didominasi oleh perdebatan mengenai Blockchain Trilemma—bagaimana menyeimbangkan keamanan, desentralisasi, dan skalabilitas tanpa mengorbankan salah satu pilar tersebut. Cardano muncul secara spesifik untuk memecahkan kelemahan Ethereum melalui pendekatan arsitektur berlapis yang memisahkan transaksi nilai dari eksekusi komputasi, sekaligus mengganti mekanisme konsensus Proof-of-Work (PoW) yang tidak efisien secara energi dengan Proof-of-Stake (PoS) berbasis pembuktian matematis yang kuat.

## 3 Project Origin

Gagasan mengenai Cardano lahir dari visi Charles Hoskinson dan Jeremy Wood yang mendirikan Input Output Hong Kong (IOHK, yang kemudian bertransisi menjadi Input Output Global atau IOG) pada tahun 2015. Hoskinson, yang merupakan salah satu pendiri awal Ethereum, meninggalkan proyek tersebut akibat perbedaan filosofis mengenai struktur entitas pengembangan, di mana ia menginginkan entitas komersial berorientasi profit sedangkan tim pendiri Ethereum lainnya memilih jalur non-profit. Menyadari kelemahan sistemis dalam pengembangan blockchain yang terburu-buru, Hoskinson dan Wood mengonseptualisasikan Cardano sebagai proyek blockchain pertama yang dibangun dari fondasi akademis murni menggunakan bahasa pemrograman fungsional Haskell. Untuk mengelola ekosistem yang kompleks ini, dibentuk struktur tripartit yang terdiri dari tiga organisasi dengan fungsi yang terpisah secara tegas:

Cardano Foundation (Zug, Swiss): Berfokus pada regulasi, standardisasi, edukasi, pengawasan komunitas, dan legalitas hukum.

IOHK/IOG: Bertanggung jawab atas penelitian kriptografi mendalam dan rekayasa perangkat keras serta perangkat lunak utama.

EMURGO: Bertindak sebagai lengan komersial dan ventura yang mendorong adopsi perusahaan serta investasi ekosistem.

## 4 Innovation Analysis

Cardano memperkenalkan serangkaian inovasi fundamental yang membedakannya secara struktural dari kompetitor utamanya dalam industri Web3, dengan rincian parameter inovasi sebagai berikut:

Mekanisme Konsensus Ouroboros: Protokol Proof-of-Stake (PoS) pertama yang terbukti aman secara matematis melalui metode peninjauan sejawat (peer-review). Ouroboros menghasilkan keacakan yang tidak bias (unbiased randomness) dalam pemilihan pemimpin slot (slot leader) tanpa memerlukan konsumsi energi yang masif seperti Proof-of-Work.

Model Extended UTXO (eUTXO): Berbeda dengan Ethereum yang menggunakan model berbasis akun (stateful account-based), Cardano mengadopsi dan memperluas model UTXO milik Bitcoin. Inovasi eUTXO terletak pada penambahan "datum" (state lokal yang melekat pada output), "redeemer" (argumen pembuktian untuk membelanjakan output), dan "script context" (pandangan menyeluruh dari transaksi). Hal ini memungkinkan eksekusi smart contract yang sepenuhnya deterministik, di mana biaya transaksi dan hasil eksekusi dapat dihitung secara pasti di tingkat lokal (off-chain) sebelum transaksi dikirim ke jaringan.

Arsitektur Berlapis (Layered Architecture): Pemisahan fisik dan logis antara Cardano Settlement Layer (CSL) yang bertugas memproses transfer nilai dasar (ADA) dan Cardano Computation Layer (CCL) yang mengelola logika smart contract dan aplikasi desentralisasi (dApps). Arsitektur ini meminimalkan kemacetan jaringan dan meningkatkan fleksibilitas peningkatan sistem.

Aiken Smart Contract Language: Sebuah bahasa pemrograman fungsional murni yang dikembangkan secara modular untuk menggantikan kompleksitas ekstrem penulisan validator smart contract berbasis Haskell Plutus. Aiken secara masif menurunkan hambatan masuk bagi pengembang mainstream dengan menawarkan sintaksis yang intuitif mirip TypeScript/Rust, eksekusi biaya yang sangat efisien, serta perangkat pengujian unit bawaan.

## 5 Technology Evolution

Evolusi teknologi Cardano tidak berlangsung secara monolitik, melainkan terbagi ke dalam roadmap lima era perkembangan yang berjalan melalui aktivasi percabangan keras (hard fork) yang terkoordinasi secara mulus:

Era Byron (Peluncuran Awal): Dimulai pada 27 September 2017. Beroperasi sebagai jaringan federasi tertutup yang dikelola oleh kunci genesis dari tiga entitas pendiri. Menggunakan konsensus Ouroboros Classic dan Ouroboros BFT untuk mengaktifkan fungsi dasar pengiriman nilai ADA tanpa inflasi (seluruh imbalan blok pada fase federasi ini dibakar). Daedalus dan Yoroi dirilis sebagai dompet referensi.

Era Shelley (Desentralisasi): Diaktifkan melalui hard fork pada 29 Juli 2020. Memperkenalkan Ouroboros Praos yang aman dari penyerang adaptif (adaptive attackers) menggunakan penandatanganan kunci yang berevolusi (Key-Evolving Signatures/KES). Shelley mentransisikan hak pembuatan blok dari federasi ke komunitas operator kolam pasak (Stake Pool Operators/SPOs). Shelley Incentivized Testnet (ITN) yang diluncurkan pada akhir 2019 membuktikan teori permainan insentif non-custodial staking tanpa penguncian (locking) dana.

Era Goguen (Smart Contracts): Diimplementasikan secara bertahap melalui tiga hard fork ledger utama:

Allegra (16 Desember 2020): Memperkenalkan fitur penguncian token (token locking) yang diperlukan untuk sistem tata kelola awal dan persiapan smart contract.

Mary (1 Maret 2021): Mengaktifkan multi-asset ledger, memungkinkan pembuatan dan pengiriman aset digital asli (native tokens dan NFTs) langsung di atas protokol tanpa perlu menulis kode smart contract yang rumit seperti standar ERC-20 di Ethereum.

Alonzo (12 September 2021): Membawa integrasi penuh Plutus smart contracts (UPLC), membuka gerbang bagi ekosistem DeFi dan dApps di Cardano.

Era Basho (Skalabilitas & Interoperabilitas): Berfokus pada optimasi kinerja ledger. Ditandai oleh Vasil hard fork (22 September 2022) yang menghadirkan Plutus v2, pipelining referensi input, dan optimasi skrip untuk mengurangi ukuran transaksi dan meningkatkan throughput. Diikuti oleh Valentine hard fork (14 Februari 2023) untuk dukungan kriptografi tanda tangan ECDSA dan Schnorr guna kompatibilitas lintas rantai. Era Basho terus dikembangkan melalui penelitian saluran off-chain Hydra dan arsitektur peningkatan throughput Ouroboros Leios.

Era Voltaire (Tata Kelola Desentralisasi): Berfokus pada penyerahan kendali parameter jaringan dan perbendaharaan langsung kepada komunitas. Diaktifkan melalui Chang #1 hard fork pada 1 September 2024 yang mengimplementasikan kerangka kerja CIP-1694 dengan konstitusi interim. Dilanjutkan dengan Plomin hard fork pada 29 Januari 2025 untuk mengaktifkan fungsi penuh perwakilan delegasi (DReps). Fase ini mencapai puncaknya pada 18 Juli 2026 melalui aktivasi Van Rossem hard fork (Protokol Versi 11), peningkatan sistem pertama yang sepenuhnya diratifikasi secara on-chain oleh pemungutan suara komunitas tanpa ketergantian kendali IOG.

## 6 Funding Intelligence

Proses pendanaan awal Cardano dilakukan melalui penjualan voucher token yang sangat terstruktur, dengan rincian penggalangan dana dan distribusinya sebagai berikut:

Funding Round: Pre-Sale (Token Voucher Distribution)

Start Date: September 2015

End Date: Januari 2017

Total Gross Sales BTC: 108,844.48 BTC

Equivalent USD Value: $62,236,134.00 USD

Average Price per BTC: $571.79 USD

Redeemable Vouchers: 25,927,070,538.00 ADA

Tranche 1 Ticket Count: 277

Tranche 1 Percentage: 1.92%

Tranche 2 Ticket Count: 4,100

Tranche 2 Percentage: 28.4%

Tranche 3 Ticket Count: 3,204

Tranche 3 Percentage: 22.2%

Tranche 4 Ticket Count: 6,821

Tranche 4 Percentage: 47.3%

Personal Owners Count: 9,835

Company Owners Count: 77

Total Unique Owners: 9,912

Swiss-based Cardano Foundation Allocation BTC: 7,168.00 BTC

Isle of Man Entity Allocation BTC: 1,090.00 BTC

Audit Service Payment requested in March 2016 BTC: 1,096.00 BTC

Bitcoin Price in March 2016: $414.00 USD

Estimated IOHK Allocation BTC: 54,000.00 BTC

Dalam perkembangan tata kelola keuangan jangka panjang, akuntabilitas pengelolaan dana awal ini menghadapi tantangan transparansi. Pada pertengahan tahun 2025 hingga awal 2026, muncul gelombang tuntutan transparansi atas keberadaan kurang lebih 1,096 BTC dari dana penjualan voucher awal yang dialokasikan pada struktur awal organisasi. Charles Hoskinson memberikan klarifikasi publik bahwa dana 1,096 BTC tersebut telah dicairkan pada Maret 2016 seharga $414.00 per BTC (total sekitar $400,000.00 USD pada saat itu) untuk membayar biaya audit crowdsale awal kepada Michael Parsons, John Maguire, dan Bruce Milligan. Namun, komunitas dan investor kritis mempertanyakan rincian alamat on-chain yang membuktikan penerimaan akhir dari transaksi tersebut. Di samping itu, pengungkapan bahwa IOHK menerima sekitar 54,000 BTC dari total pengumpulan dana crowdsale (sekitar 50% dari hasil penjualan voucher) memicu diskusi kritis mengenai asimetri alokasi modal awal di antara pendiri.

## 7 Community Intelligence

Strategi awal Cardano untuk mengakuisisi pengguna pertama didorong secara unik melalui model pemasaran luring (offline) terfokus di wilayah Asia Timur, khususnya Jepang, menggunakan jaringan agen penjualan fisik terstruktur. Langkah ini berhasil mengumpulkan basis pemegang ritel awal yang sangat loyal yang disebut sebagai "ADA Army." Seiring berjalannya transisi teknis ke era Shelley, Cardano menggunakan mekanisme insentif non-custodial staking sebagai alat pertumbuhan komunitas. Delegasi staking yang tidak mengunci token dan tidak membebankan penalti pemotongan dana (slashing) terbukti sangat efektif menahan tekanan jual karena ADA tetap memiliki likuiditas penuh di dompet pengguna saat menghasilkan hasil tahunan (APY) sekitar 3% hingga 5%. Shelley Incentivized Testnet (ITN) pada tahun 2019 berhasil memobilisasi partisipasi komunitas secara ekstrem dengan mencatatkan sekitar 40% dari total pasokan beredar didelegasikan pada node uji coba.

Untuk mendanai inovasi tingkat komunitas, Cardano mendirikan Project Catalyst, yang bertransformasi menjadi salah satu dana inovasi terdesentralisasi terbesar di dunia. Namun, seiring waktu, Project Catalyst menghadapi kritik tajam terkait tata kelola voting berbasis kepemilikan aset ("one Lovelace = one vote") yang dinilai menciptakan sistem plutokrasi. Analisis data voting Fund 10 menunjukkan ketimpangan partisipasi komunitas:

Total Wallets Terdaftar: 57,118 dompet dengan total 4.50 miliar ADA terdaftar

Rasio Partisipasi: Hanya 13.70% dari total ADA beredar yang berpartisipasi dalam voting

Konsentrasi Kekuatan: Golongan pemegang 1.00 juta hingga 5.00 juta ADA (hanya 1.35% partisipan) menguasai 33.00% total suara

Dominasi Institusi: Intervensi Cardano Foundation di Fund 13 dengan menyalurkan hak suara sebesar 180,000,000.00 ADA memicu kontroversi besar karena secara sepihak menentukan lolosnya 185 proposal dari 1,800 proposal terdaftar, mengesampingkan suara organik komunitas. Menanggapi kekecewaan massal tersebut, pada Fund 14 (September 2025), Cardano Foundation secara drastis membatasi kekuatan suaranya menjadi satu dompet senilai 20,000,000.00 ADA dan membatasi partisipasi voting hanya pada jalur khusus "Partners & Products".

## 8 Narrative Intelligence

Lanskap naratif Cardano senantiasa bergerak dinamis mengikuti pergeseran tren pasar kriptografi global:

Fase Pembentukan (2015-2017): Narasi berpusat pada "Academic Peer-Reviewed Blockchain" dan bahasa pemrograman "Haskell" sebagai standar keamanan tertinggi yang kebal terhadap bug kontrak pintar.

Fase Desentralisasi (2018-2020): Cardano menguasai narasi sebagai pionir mekanisme PoS yang demokratis dan tanpa penguncian likuiditas melalui Shelley ITN dan mainnet launch.

Fase DeFi dan Integrasi Dunia Nyata (2021-2023): Cardano berusaha menggabungkan narasi DeFi fungsional (pasca Alonzo hard fork) dengan narasi utilitas identitas digital terdesentralisasi (Decentralized Identity/DID) di negara berkembang, ditandai dengan proyek perintis Atala PRISM bersama Kementerian Pendidikan Ethiopia untuk menyediakan identitas digital bagi 5,000,000.00 siswa dan 750,000.00 guru.

Fase On-Chain Governance (2024-2025): Narasi beralih ke kedaulatan mutlak komunitas melalui implementasi penuh Voltaire (CIP-1694), memposisikan Cardano sebagai eksperimen demokrasi digital terdesentralisasi terbesar.

Era Multi-Client dan Rantai Kemitraan (2026): Cardano memposisikan dirinya di dalam narasi desentralisasi infrastruktur rekayasa dengan membagi pengembangan node tunggal (Haskell Node) ke model multi-implementasi berbasis Haskell, Rust, dan Go. Di samping itu, peluncuran rantai kemitran (partner chain) berfokus privasi, Midnight Network, dengan token ganda (NIGHT dan DUST) serta bahasa pemrograman Compact (berbasis TypeScript), memperluas kegunaan fungsional Cardano di sektor kepatuhan data komersial.

## 9 Competitive Landscape

Dalam peta persaingan blockchain Layer 1 global, Cardano memposisikan dirinya sebagai platform berorientasi integritas struktural, berhadapan langsung dengan pendekatan kompetitif yang kontras:

Versus Ethereum: Ethereum memegang keunggulan mutlak dalam efek jaringan (network effects), ketersediaan stablecoin, integrasi Layer 2 (L2), serta likuiditas DeFi yang melimpah. Namun, model akun dinamis EVM Ethereum memiliki kelemahan berupa kerentanan keamanan transaksi (seperti reentrancy attacks), biaya gas yang tidak terprediksi saat kemacetan, serta ketergantungan pada pembaruan off-chain yang dikoordinasikan secara informal. Cardano membalas dengan determinisme transaksi eUTXO, biaya transaksi tetap yang ramah pengguna, dan penolakan keras terhadap fungsionalitas pembakaran biaya gas (gas burning) agar ADA tetap memiliki kepastian pasokan emisi.

Versus Solana: Solana menawarkan eksekusi transaksi terparalelisasi berkinerja ekstrem (HFT-chain) dengan biaya di bawah satu sen. Kelemahan utama Solana terletak pada kerentanan pemadaman jaringan (network outages) secara berulang dan kebutuhan perangkat keras validator yang sangat mahal. Cardano menandingi dengan rekor waktu aktif (uptime) jaringan yang hampir tanpa cela sejak 2017 berkat rekayasa perangkat lunak yang formal. Meskipun demikian, model paralel eUTXO Cardano terhambat oleh masalah konkurensi data (concurrency) yang kompleks, di mana satu output transaksi tidak dapat diakses oleh beberapa pengguna secara bersamaan tanpa bantuan infrastruktur penggabung (batchers/concurrency state machines). Hal ini mengakibatkan TVL DeFi Cardano pada pertengahan 2026 hanya berada di kisaran $137,000,000.00 USD, tertinggal sangat jauh dibandingkan TVL Solana yang melebihi $4,000,000,000.00 USD.

## 10 Product Evolution

Evolusi produk di tingkat aplikasi dan peralatan pengembang di dalam ekosistem Cardano mencerminkan perubahan taktis dari idealisme akademis menuju utilitas praktis:

Peralatan Pemrograman (Developer Tooling): Dari Plutus/Plinth awal berbasis Haskell yang memiliki kurva pembelajaran sangat curam dan tingkat kesulitan debug yang tinggi, ekosistem beralih ke Aiken. Aiken berhasil merevolusi produktivitas pengembang, di mana lebih dari 75.00% responden survei pengembang Cardano 2025 melaporkan penggunaan Aiken untuk menulis kontrak pintar mereka.

Infrastruktur Dompet (Wallet Infrastructure): Daedalus Wallet yang dirilis pada era Byron sebagai dompet full-node resmi terbukti kurang ramah pengguna karena membutuhkan waktu sinkronisasi data ledger lokal hingga beberapa jam serta konsumsi RAM komputer yang tinggi. EMURGO meluncurkan Yoroi sebagai alternatif dompet ringan. Pada April 2023, IOG meluncurkan Lace Wallet 1.0 sebagai produk dompet ringan Web3 generasi baru dengan fitur bundling transaksi multi-aset dalam satu biaya. Puncaknya pada Juni 2026, pembaruan Lace v1.17 merombak total arsitektur interaksi blockchain, mengurangi latensi sinkronisasi saldo secara near-instant serta mengintegrasikan manajemen multi-alamat di bawah satu frasa pemulihan.

## 11 Tokenomics Intelligence

Sistem ekonomi Cardano dirancang sebagai basis moneter yang terbatas dengan emisi yang terprogram secara ketat, dijabarkan melalui metrik pembagian alokasi berikut:

Max Supply Capped: 45,000,000,000.00 ADA

Initial Supply at Launch: 31,112,484,646.00 ADA

Public Voucher Sales Allocation: 25,927,070,538.00 ADA

IOHK Genesis Allocation: 2,463,071,701.00 ADA

EMURGO Genesis Allocation: 2,074,165,644.00 ADA

Cardano Foundation Genesis Allocation: 648,176,761.00 ADA

Reserves for Staking and Treasury: 13,887,515,354.00 ADA

Monetary Expansion Rate per Epoch (rho): 0.3%

Treasury Funding Cut: 20%

Staking Operator and Delegator Cut: 80%

Unclaimed Voucher Reversion to Reserves (Allegra Hard Fork): 318,200,000.00 ADA

Transfer of Unclaimed Voucher to Staking Addresses (October 2021): 318,200,000.00 ADA

Protokol Cardano melepaskan emisi dari sisa cadangan (Reserve) untuk imbalan staking dan pendanaan kas negara (treasury) setiap epoch (siklus 5 hari) melalui fungsi peluruhan eksponensial dengan parameter inflasi ρ (rho) yang ditetapkan sebesar 0.3% per epoch. Dari total keluaran emisi dan biaya transaksi yang dikumpulkan per epoch, 20% secara otomatis dialirkan ke kas negara (treasury) untuk mendanai pengembangan ekosistem, sedangkan 80% sisanya didistribusikan sebagai imbalan kepada operator kolam pasak (SPOs) dan para delegator.

INKONSISTENSI DATA ALOKASI: Terdapat inkonsistensi minor dalam pencatatan alokasi Cardano Foundation di beberapa sumber data terkemuka. Dokumentasi resmi Genesis Cardano mencatat alokasi sebesar 648,176,761.00 ADA, sedangkan data yang dirilis oleh Figment Insights mencatat alokasi sebesar 640,000,000.00 ADA. Analisis teknis CIF mengesampingkan angka Figment karena tidak memperhitungkan presisi unit Lovelace pada pencatatan ledger genesis awal. Evidence Level: HIGH (berdasarkan verifikasi silang langsung pada file konfigurasi blok genesis Cardano).

Dalam hal penanganan voucher awal yang tidak diklaim oleh pembeli pada periode 2015-2017 (berjumlah sekitar 318,200,000.00 ADA atau ~1.00% dari total voucher penjualan), Cardano mengaktifkan modifikasi sistem pada Allegra hard fork (Desember 2020) untuk memindahkan dana tidak terklaim tersebut kembali ke cadangan sistem. Pada Oktober 2021, sisa dana sebesar 318,200,000.00 ADA tersebut akhirnya dialokasikan ke dalam enam alamat staking yang ditentukan di bawah kontrol sistem.

## 12 Airdrop & Incentive Intelligence

Cardano secara konsisten menghindari model insentif airdrop spekulatif berisiko tinggi yang umum dilakukan oleh jaringan Layer 1 EVM guna mencegah inflasi buatan dan manipulasi kapitalisasi pasar. Sebagai gantinya, Cardano menggunakan dua strategi insentif fundamental:

Shelley Incentivized Testnet (ITN) 2019: Pengguna didorong untuk memindahkan saldo ADA mereka ke jaringan uji coba Rust-jormungandr dengan jaminan bahwa imbalan tADA yang dikumpulkan dari aktivitas staking dan menjalankan pool selama fase uji coba akan secara otomatis dikonversi menjadi ADA nyata di jaringan utama (mainnet) saat era Shelley diluncurkan. Strategi ini sangat sukses membangun kebiasaan desentralisasi kolam pasak tanpa risiko kehilangan modal.

Skema Glacier Drop (Midnight Network): Sebagai rantai privasi mitra, Midnight mendistribusikan token NIGHT pertamanya melalui mekanisme distribusi lintas rantai yang mencakup delapan ekosistem besar, termasuk pemegang ADA, BTC, ETH, SOL, XRP, BNB, AVAX, dan BAT. Tujuan dari program ini adalah memperluas basis validator dan pengguna awal Midnight ke luar batas internal ekosistem Cardano.

## 13 Token Lifecycle Intelligence

Perjalanan siklus hidup token ADA dari fase pembentukan hingga era kematangan tata kelola:

Fase Pra-TGE dan Redemption: Token ADA diluncurkan secara on-chain pada September 2017 bertepatan dengan mulainya era Byron. Pemegang voucher awal dapat mencairkan token mereka menggunakan dompet desktop Daedalus dengan memasukkan kode penebusan voucher fisik mereka. Sekitar 99.00% voucher berhasil ditebus dalam fase awal ini. Namun, setelah peningkatan Shelley pada Juli 2020, pencairan otomatis dihentikan sementara karena ketiadaan infrastruktur yang kompatibel, sebelum akhirnya dibangun mekanisme penebusan manual pada November 2021.

Tren Harga Awal (30/60/90/180 Hari Pasca TGE): ADA mulai diperdagangkan di bursa global (seperti Bittrex) pada Oktober 2017 di kisaran harga $0.030000 USD. Dalam periode 60-90 hari pasca TGE, bertepatan dengan gelembung spekulatif pasar kripto akhir 2017, harga ADA melonjak tajam ke angka $0.720000 USD pada Desember 2017 hingga mencapai kisaran $0.520000 - $1.300000 USD pada Januari 2018. Namun, setelah satu tahun (akhir 2018), harga mengalami koreksi ekstrem (dump) ke kisaran $0.040000 USD akibat badai pasar beruang (bear market) global.

Siklus Ekstrem (ATH & ATL):

All-Time High ATH Price: $3.09 USD (atau dicatat $3.10 USD di beberapa bursa) dicapai pada 1 September 2021, didorong oleh spekulasi peluncuran Alonzo smart contracts.

All-Time Low ATL Price: $0.01925 USD dicapai pada 12 Maret 2020 bertepatan dengan likuidasi massal global akibat krisis likuiditas awal pandemi COVID-19.

Kondisi Harga 2025-2026: Pada pertengahan 2026, ADA berkonsolidasi di kisaran $0.160000 - $0.350000 USD, berada pada posisi penurunan terdalam sekitar 95.00% dari rekor puncaknya.

ANALISIS PENILAIAN FUNDAMENTAL (Fair Value Analysis): Berdasarkan metrik nilai wajar fundamental, token ADA dikategorikan dalam posisi jenuh jual (undervalued) dari perspektif infrastruktur desentralisasi namun dinilai terlalu tinggi (overvalued) dari sudut pandang pemanfaatan modal DeFi. Rasio Kapitalisasi Pasar terhadap TVL (Market Cap to TVL Ratio) Cardano berada di angka ekstrem 66.49x (kapitalisasi pasar ~$6,194,000,000.00 USD berbanding TVL ~$137,000,000.00 USD). Angka ini sangat tinggi jika dibandingkan dengan Ethereum yang memiliki rasio di bawah 10x. Ketimpangan ini menunjukkan bahwa valuasi ADA sebagian besar ditopang oleh loyalitas pemegang jangka panjang dan sistem non-custodial staking, bukan oleh aktivitas transaksi dApps harian. Namun, kepastian hukum pasca keputusan SEC yang secara resmi mengklarifikasi bahwa ADA bukan merupakan aset sekuritas (security), menghilangkan risiko hukum bagi manajer dana besar.

## 14 Business Intelligence

Kinerja operasional dan aktivitas komersial Cardano dicatat berdasarkan data historis dan berjalan pada semester pertama tahun 2026, dijabarkan melalui metrik numerik berikut:

DeFi TVL (April 2026): $133,800,000.00 USD

TVL Native Token Peak 2026: 520,410,000.00 ADA

Daily DEX and Perps Trading Volume: $374,000,000.00 USD

Circulating Market Cap (May 2026): $10,500,000,000.00 USD

ADA Price (May 2026): $0.30 USD

Circulating Market Cap (April 2026): $6,316,364,886.00 USD

Circulating Market Cap (July 2026): ~$6,000,000,000.00 USD

ADA Price (July 2026): $0.16 USD

Daily Trading Volume (July 2026): $371,262,845.00 USD

Project Catalyst Cumulative Distributed Funding: $131,899,536.00 USD

Project Catalyst Total Funded Proposals: 2,221

Project Catalyst Completed Proposals: 1,673

Project Catalyst In Progress Proposals: 290

Project Catalyst Did Not Finish Proposals: 253

Total Votes Cast across all funds: 3,257,805

Fund 14 Total Budget: 18,591,246.00 ADA (converted to $12,610,442.00 USD) - Fund 14 Proposals Funded: 131 out of 1,283

Fund 14 Votes Cast: 174,737

Minswap DEX TVL (April 2026): $33,300,000.00 USD

Danogo DEX TVL (April 2026): $16,300,000.00 USD

WingRiders DEX TVL (April 2026): $5,000,000.00 USD

Indigo Protocol CDP TVL (April 2026): $6,210,000.00 USD

Liqwid Finance Lending TVL (April 2026): ~$10,000,000.00 to $15,000,000.00 USD

Circle USDCx Stablecoin Market Share: 36.00%

Non-USD Stablecoin Market Cap Global: $1,400,000,000.00 USD

USD Stablecoin Market Cap Global: $300,000,000,000.00 USD

## 15 Success & Failure Analysis

Evaluasi keberhasilan dan kegagalan Cardano dari delapan sudut pandang pemangku kepentingan yang berbeda:

Founder Viewpoint

Verdict: Sukses

Alasan: Charles Hoskinson berhasil merealisasikan visi jangka panjang untuk menciptakan protokol yang dapat bertahan secara mandiri tanpa ketergantungan pada penciptanya. Penyerahan repositori kode utama ke Intersect MBO pada 2026 merupakan pembuktian akhir dari desentralisasi rekayasa yang dikonseptualisasikan sejak 2015.

Tingkat Keyakinan: HIGH.

Venture Capital (VC) Viewpoint

Verdict: Gagal

Alasan: Model riset akademis Cardano yang lambat membatasi peluang investasi VC untuk menghasilkan pengembalian modal cepat (fast-yield exit). Ketiadaan EVM-composability yang mudah ditiru mencegah penciptaan proyek-proyek spekulatif yang dapat dimanipulasi melalui skema pompa-dan-buang (pump-and-dump) likuiditas.

Tingkat Keyakinan: HIGH.

Retail Investor Viewpoint

Verdict: Campuran

Alasan: Investor ritel menikmati kenyamanan sistem staking tanpa risiko slashing dan kemudahan menjaga kepemilikan aset secara mandiri. Namun, depresiasi harga ADA yang mendalam hingga 95.00% dari ATH pada pertengahan 2026 memberikan tekanan finansial yang sangat berat bagi mereka yang masuk pada puncak siklus 2021.

Tingkat Keyakinan: MEDIUM.

Community Viewpoint

Verdict: Sukses

Alasan: Komunitas memiliki kendali mutlak atas arah jaringan melalui CIP-1694. Aktivasi Van Rossem hard fork membuktikan kekuatan koordinasi politik on-chain komunitas tanpa intervensi korporasi.

Tingkat Keyakinan: HIGH.

Developer Viewpoint

Verdict: Campuran

Alasan: Pada awalnya, kurva pembelajaran Haskell Plutus yang ekstrem memicu frustrasi massal dan menghambat inovasi. Kehadiran Aiken pada tahun 2023-2025 berhasil menyelamatkan pengalaman pengembang, mengubah lanskap penulisan kode dApps menjadi jauh lebih ramah dan efisien.

Tingkat Keyakinan: HIGH.

Institution Viewpoint

Verdict: Sukses

Alasan: Keputusan pengadilan dan kejelasan regulasi dari SEC bahwa ADA diklasifikasikan sebagai komoditas dan bukan sekuritas menghilangkan risiko hukum bagi manajer dana besar. Keamanan arsitektur eUTXO yang deterministic sangat diminati untuk penyelesaian transaksi bernilai besar di sektor publik.

Tingkat Keyakinan: MEDIUM.

Validator Viewpoint

Verdict: Sukses

Alasan: Operator kolam pasak (SPOs) menikmati arsitektur konsensus yang stabil, kebutuhan konsumsi energi yang rendah, serta sistem delegasi non-custodial yang menyerap loyalitas pengguna secara otomatis.

Tingkat Keyakinan: HIGH.

Builder Viewpoint - Verdict: Gagal

Alasan: Tim proyek yang membangun dApps di atas Cardano harus menghadapi tantangan teknis konkurensi eUTXO yang membutuhkan desain batching kompleks. Hal ini diperparah dengan jeda pendanaan akibat penutupan sementara Project Catalyst Fund 15 & 16 pada awal 2026. - Tingkat Keyakinan: HIGH.

## 16 Historical Timeline

Kronologi lengkap sejarah perkembangan Cardano, diurutkan berdasarkan tanggal terjadinya peristiwa:

September 2015 hingga Januari 2017 — Distribusi voucher ADA dimulai di Asia — Menjaring pemegang ritel awal terutama di Jepang dan mengumpulkan dana operasional awal sebesar 108,844.48 BTC.

Maret 2016 — Pengajuan audit pra-penjualan oleh Michael Parsons — Cardano Foundation mengeluarkan 1,096.00 BTC untuk biaya audit crowdsale awal.

27 September 2017 — Peluncuran Jaringan Utama (Mainnet) Byron — Pengguna dapat mentransaksikan ADA asli secara terdesentralisasi menggunakan Daedalus wallet.

10 Januari 2018 — Perilisan Yoroi Light Wallet oleh EMURGO — Menyediakan alternatif dompet ringan bagi pengguna harian untuk mengatasi kelambatan sinkronisasi Daedalus.

Juni 2019 — Uji Coba Shelley Testnet — Memulai fase eksperimen teknologi staking dan desentralisasi pembuatan blok.

12 November 2019 — Uji Coba Snapshot Pertama Shelley ITN — Melakukan kloning awal basis data blockchain untuk pengujian dompet dan stabilitas jaringan.

29 November 2019 — Snapshot Resmi Shelley Incentivized Testnet (ITN) — Merekam saldo pemegang ADA untuk ditransfer sebagai tADA dalam program uji coba insentif staking.

13 Desember 2019 — Peluncuran Shelley ITN — Pengguna mulai mendelegasikan dana uji coba dan mendapatkan imbalan riil yang dapat ditransfer ke mainnet.

29 Juli 2020 — Aktivasi Shelley Hard Fork — Cardano resmi bertransisi dari jaringan federasi tertutup ke sistem pembuatan blok terdesentralisasi oleh SPOs.

Agustus/September 2020 — Peluncuran Project Catalyst Fund 1 — Eksperimen awal pendanaan inovasi berbasis komunitas diluncurkan.

16 Desember 2020 — Aktivasi Allegra Hard Fork — Mengaktifkan penguncian token (token locking) dan pemulihan dana voucher tak terklaim ke cadangan.

1 Maret 2021 — Aktivasi Mary Hard Fork — Mengizinkan penciptaan aset asli (native tokens) dan NFTs secara langsung pada ledger tanpa smart contract.

April 2021 — Pengumuman Kemitraan Atala PRISM di Ethiopia — IOHK bermitra dengan Kementerian Pendidikan Ethiopia untuk menerbitkan ID digital bagi 5,000,000.00 siswa.

12 September 2021 — Aktivasi Alonzo Hard Fork — Mengintegrasikan smart contract Plutus Core secara resmi dan membuka ekosistem dApps.

Oktober 2021 — Pemindahan Dana Voucher Tidak Terklaim — Protokol mengalokasikan 318,200,000.00 ADA tidak terklaim ke dalam enam alamat staking terpilih.

November 2021 — Pembukaan Kembali Mekanisme Penebusan Manual — Memulihkan jalur penebusan voucher yang terhenti pasca migrasi Shelley.

22 September 2022 — Aktivasi Vasil Hard Fork — Menyajikan optimalisasi performa Plutus v2 dan fitur pipelining untuk meningkatkan throughput.

18 November 2022 — Pengumuman Midnight Privacy Chain — IOG mengenalkan proyek rantai mitra privasi selektif berbasis zero-knowledge cryptography.

14 Februari 2023 — Aktivasi Valentine Hard Fork — Dukungan kriptografi eliptik SECP diaktifkan untuk interaksi lintas rantai yang mulus.

11 April 2023 — Peluncuran Lace Wallet 1.0 oleh IOG — Menyediakan platform dompet ringan Web3 modern dengan bundling transaksi multi-aset.

Desember 2023 — Migrasi Kode Sumber Pertama ke Intersect MBO — IOG menyerahkan 25 repositori kode utama untuk kemandirian rekayasa ekosistem.

16 Maret 2024 — Peluncuran Stablecoin USDM oleh Mehen — Memperkenalkan stablecoin patokan fiat dolar pertama yang tahan terhadap penyensoran akun.

1 September 2024 — Aktivasi Chang #1 Hard Fork — Menginisiasi era Conway untuk tata kelola on-chain berbasis CIP-1694.

4 Desember hingga 6 Desember 2024 — Konvensi Konstitusional Cardano — Delegasi global merancang draf Konstitusi Cardano.

9 Desember 2024 — Kontroversi Pemungutan Suara Fund 13 — Cardano Foundation menggunakan hak suara sebesar 180,000,000.00 ADA, memicu kecaman plutokrasi.

29 Januari 2025 — Aktivasi Plomin Hard Fork — Tata kelola penuh diaktifkan menggunakan sistem DReps dan tindakan tata kelola formal.

Februari 2025 — Peluncuran Stablecoin USDA oleh EMURGO/Anzens — Memperkenalkan stablecoin alternatif berpatokan dolar dalam ekosistem.

23 Februari 2025 — Pengesahan Konstitusi Cardano di Atas Rantai — Pemegang ADA meratifikasi konstitusi permanen melalui mekanisme voting on-chain. - Februari 2026 — Peluncuran Circle USDCx di Mainnet — Menghubungkan likuiditas Cardano ke lebih dari 50 blockchain melalui Circle CCTP.

Maret 2026 — Penangguhan Project Catalyst Fund 15 & 16 — Peralihan operator ke Cardano Foundation memaksa builders menghadapi jeda pendanaan mendadak.

4 April 2026 — Pengesahan Kerangka Kerja Anggaran 2026 — Info Action pengkoordinasian proses anggaran disetujui supermayoritas oleh DReps.

Juni 2026 — Pembaruan Dompet Lace v1.17 oleh IOG — Merombak arsitektur komunikasi ledger untuk sinkronisasi saldo instan.

13 Juli 2026 — Ratifikasi On-Chain Van Rossem Hard Fork — DReps, SPOs, dan CC menyetujui pembaruan Protokol Versi 11.

18 Juli 2026 — Aktivasi Van Rossem Hard Fork di Mainnet — Protokol Versi 11 resmi berjalan tanpa downtime, menandai pembaruan pertama tanpa kendali penuh IOG.

Agustus 2026 — Mulainya Transisi Rekayasa Inti Eksternal — IOG mentransfer kendali Haskell Node, Plutus, Daedalus, dan Hydra ke Se7en Labs dan Teragone.

## 17 Current Status

Keadaan proyek Cardano saat ini dikategorikan ke dalam fase "Transisi Struktural dan Pemulihan Sistemik". Secara fundamental keuangan, harga ADA mengalami penurunan sedalam 95.00% dari harga tertingginya (ATH), dengan aktivitas DeFi on-chain yang berkonsolidasi di angka TVL sekitar $137,000,000.00 USD. Hal ini mencerminkan kelesuan minat spekulatif ritel jangka pendek.

Namun, di balik angka keuangan tersebut, tingkat ketahanan protokol Cardano berada pada tingkat tertinggi dalam sejarahnya. Sistem tata kelola Voltaire kini beroperasi secara penuh melalui perwakilan DReps dan Komite Konstitusional. Intersect MBO telah aktif mengelola perbendaharaan ekosistem senilai lebih dari 345,000,000.00 ADA serta memimpin migrasi kode ke sistem multi-klien independen (Haskell, Rust, dan Go) yang dijadwalkan matang pada tahun 2027. Hal ini menandakan transisi dari ketergantungan historis terhadap IOG menuju jaringan mandiri yang tangguh.

## 18 Lessons Learned

Pelajaran terbesar yang dapat dipetik dari perjalanan sejarah rekayasa dan tata kelola Cardano:

Prioritas Keseimbangan Keamanan Formal Versus Kecepatan Adopsi: Pendekatan akademis Cardano yang mengandalkan fungsionalitas murni Haskell berhasil melahirkan blockchain dengan rekor uptime mendekati sempurna tanpa pemadaman sistemis. Namun, kurva pembelajaran pengembang yang ekstrem membatasi efek jaringan DeFi awal. Industri harus memprioritaskan penyediaan peralatan pengembang (SDK) yang ergonomis sejak hari pertama peluncuran mainnet.

Bahaya Plutokrasi dalam Desentralisasi Hak Suara: Sistem pendanaan komunitas Project Catalyst yang didasarkan pada kepemilikan token murni membuktikan bahwa segelintir pemegang aset besar (whales) dapat secara sepihak mengendalikan masa depan alokasi modal ekosistem. Transformasi ke pilar representatif (DReps) di bawah CIP-1694 adalah koreksi desain yang wajib diintegrasikan oleh proyek baru.

Urgensi Keragaman Klien (Client Diversity): Mengandalkan satu varian node tunggal (Haskell Node) menempatkan jaringan pada risiko titik kegagalan tunggal (single point of failure). Transisi multi-implementasi node secara paralel (Haskell, Rust, Go) merupakan langkah defensif terbaik untuk memastikan keamanan sistem secara global.

## 19 Knowledge Extraction Candidate (BAGIAN PALING PENTING)

Bagian ini menyajikan candidate entitas, hubungan, serta pola tata kelola yang diekstraksi dari arsitektur intelijen Cardano untuk digunakan kembali oleh sistem penalaran kecerdasan buatan (AI reasoning) di masa depan:

Entitas Baru:

Intersect MBO

Se7en Labs

Teragone

Amaru / Acropolis Rust Node

Dingo Go Node

Compact Language

Hubungan Ontologi (Ontology Graph):

[IOHK/IOG] -> dikontrak_oleh -> [Cardano Community Treasury]

[Intersect MBO] -> mengawasi -> [Se7en Labs & Teragone]

[Aiken Language] -> mengompilasi_ke -> [Untyped Plutus Core (UPLC)]

[Lace Wallet] -> dikembangkan_oleh -> [Input Output Global]

[Midnight Network] -> menggunakan -> [Cardano Stake Pool Operators (SPOs)]

Pola Rekayasa & Tata Kelola (Patterns Candidates):

Nama Pola: Pola Transisi Tata Kelola Pendiri (Founder Governance Divestment Pattern)

Rantai sebab-akibat: Protokol mencapai kematangan teknis dasar -> repositori kode diserahkan ke organisasi berbasis anggota independen (Intersect MBO) -> entitas pendiri memotong pengajuan anggaran kas negaranya secara sengaja -> tanggung jawab pemeliharaan diserahkan kepada pihak eksternal khusus (Se7en Labs & Teragone) -> kedaulatan teknis jaringan terdistribusi secara penuh.

Nama Pola: Pola Pemulihan Hambatan Pengembang (Developer Friction Recovery Pattern)

Rantai sebab-akibat: Jaringan menggunakan bahasa pemrograman akademis yang rumit (Haskell/Plutus) -> pengembang mengalami kesulitan dan retensi pengembang dApps menurun -> komunitas melahirkan bahasa pemrograman alternatif yang ergonomis (Aiken) -> yayasan resmi mendukung dan mengadopsi bahasa baru tersebut -> aktivitas penulisan smart contract meningkat secara masif.

## 20 Transferable Intelligence

Apabila AI bertugas mengevaluasi proyek blockchain Layer 1 baru di masa mendatang, model penilaian dapat ditransfer menggunakan parameter aturan berikut:

Aturan Umum (General Rules - Reusable):

Aturan Indeks Keragaman Klien (Client Diversity Index Rule): Nilai ketahanan sistemik Layer 1 berkorelasi langsung dengan ketersediaan minimal tiga versi klien node berbeda yang dirawat oleh organisasi komersial yang terpisah secara independen.

Aturan Kedaulatan Kas Negara (Treasury Autonomy Rule): Proyek tidak dapat dianggap terdesentralisasi apabila entitas pendiri awal menyerap lebih dari 50.00% alokasi perbendaharaan kas negara untuk biaya operasional internal mereka.

Indikator Khusus (Specific Rules - Hanya Berlaku untuk Cardano):

Indikator Delegasi Bebas Tanpa Hukuman (Non-Custodial Slashing-Free Delegation Indicator): Sistem staking Cardano yang tidak menyita modal (non-custodial) dan tidak menerapkan pemotongan dana (slashing) menciptakan daya ikat loyalitas ritel yang sangat tinggi. Parameter ini menjaga stabilitas konsensus meskipun harga token mengalami depresiasi ekstrem di bursa spekulatif.

## 21 Open Questions

Beberapa pertanyaan penting dan celah penelitian yang memerlukan pemantauan sistemik berkelanjutan:

Hipotesis Kemampuan Pemeliharaan Eksternal: Apakah Se7en Labs, yang didominasi oleh portofolio rekayasa berkinerja tinggi (HFT-chain) milik Solana, dapat mengadopsi disiplin ketat spesifikasi formal yang dibutuhkan untuk memelihara dan memperbarui Haskell Node milik Cardano secara andal?

Uji Batas Kapasitas Ouroboros Leios: Apakah rancangan pembagian node antara produsen blok dan validator dalam Ouroboros Leios mampu mengatasi tantangan konkurensi data eUTXO tanpa mengorbankan sifat deterministik biaya transaksi?

Dampak Jeda Kas Negara Project Catalyst: Bagaimana dampak dari jeda penyaluran dana inovasi Project Catalyst Fund 15 & 16 terhadap stabilitas dan pertumbuhan ekosistem builders dApps skala menengah sepanjang sisa tahun 2026?

## 22 Evidence Level

Tingkat keyakinan (Confidence Level) terhadap kesimpulan penting dalam laporan ini dijabarkan sebagai berikut:

Kesuksesan Pembaruan On-Chain Van Rossem Hard Fork: HIGH

Alasan: Terverifikasi langsung pada ledger utama Cardano dan catatan koordinasi pemungutan suara on-chain di platform Intersect MBO.

Adopsi Aiken sebagai Bahasa Utama Pengembang: HIGH

Alasan: Berdasarkan hasil kuantitatif sensus pengembang Cardano 2025 yang mencatatkan tingkat penggunaan di atas 75.00%.

Forensik Keberadaan Aliran Dana Crowdsale BTC (1,096 BTC & 54,000 BTC): MEDIUM

Alasan: Meskipun Charles Hoskinson memberikan klarifikasi email bersejarah dalam siaran langsungnya, analisis forensik on-chain yang membuktikan penandatanganan transaksi dan konfirmasi penerima akhir dari entitas Isle of Man serta para auditor belum dipublikasikan dalam bentuk laporan audit eksternal independen.

## 23 Karya yang dikutip

TokenInsight Cardano Tokenomics — https://tokeninsight.com/en/coins/cardano/tokenomics

Cardano Genesis — https://cardano.org/genesis/

Binance Square Article on 1000 BTC — https://www.binance.com/es-MX/square/post/332163117403474

Bitcoin Magazine IOHK Launches Cardano — https://bitcoinmagazine.com/markets/iohk-launches-cardano-blockchain-ada-now-trading-bittrex

CCN News on Cardano's Missing BTC — https://www.ccn.com/news/crypto/cardano-missing-1096-bitcoin-hoskinson-explains-70m-btc-mystery/

The Coin Republic on Cardano Voucher News — https://www.thecoinrepublic.com/2025/05/23/cardano-news-everything-to-know-about-the-hottest-ada-topic-right-now/

Findas Tokenomics Review of Cardano — https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-cardano-ada/r/Quvd2ZeAVzoLuu7i2qawVN

IOG News on Cardano Tokenomics Design — https://www.iog.io/news/cardano-tokenomics-design-incentives-and-stablecoins-1

Figment Insights ADA Tokenomics — https://www.figment.io/insights/cardano-ada-tokenomics/

Cardano Forum on Initial BTC Raising — https://forum.cardano.org/t/what-did-iohk-emurgo-cf-do-with-the-initial-btc-funds-raised/17679

Changelly Blog History of Cardano — https://changelly.com/blog/what-is-cardano-ada-2/ 12. Intersect MBO on Cardano Governance History — https://www.intersectmbo.org/news/the-evolution-of-cardano-governance-a-brief-history

Wikipedia Cardano Entry — https://en.wikipedia.org/wiki/Cardano_(blockchain_platform)

Cardano Foundation Academy on Development Milestones — https://cardanofoundation.org/academy/video/cardano-development-milestones

Cardano Docs on Eras and Phases — https://docs.cardano.org/about-cardano/evolution/eras-and-phases

Cropty App on Cardano Eras — https://cropty.app/ada-wallet

CoinGecko Cardano Price & Markets — https://www.coingecko.com/en/coins/cardano

Binance Square on Van Rossem Hard Fork Activation — https://www.binance.com/en/square/hashtag/CardanoHardForkUpgradeSetForJuly18

CoinMarketCap on Van Rossem Fork & Decentralization — https://coinmarketcap.com/top-stories/6a5b260520c60410ddf05b93/

The Coin Republic on Van Rossem Approval — https://www.thecoinrepublic.com/2026/07/16/cardano-news-cardano-approves-first-major-hard-fork-since-voltaire-era/

CryptoWave on Community Voting Hard Fork — https://cryptowave.co.id/articles/cardano-sukses-eksekusi-hard-fork-pertama-berdasarkan-voting-komunitas

DeFiLlama Cardano Chain Dashboard — https://defillama.com/chain/cardano

EarnPark on L1 Head-to-Head Comparison — https://earnpark.com/en/posts/xrp-vs-sol-vs-ada-head-to-head-comparison/

MEXC Learn on Cardano DeFi TVL — https://www.mexc.co/en-IN/learn/article/top-cardano-defi-projects-in-2026-where-is-the-tvl-going-/1

Medium on Project Catalyst and Plutocracy — https://medium.com/@cem.karaca/cardano-catalyst-when-decentralized-governance-becomes-plutocracy-cb726e21d697

Project Catalyst Funds Portal — https://projectcatalyst.io/funds

CryptoSlate on Project Catalyst Funding Pause — https://cryptoslate.com/cardanos-project-catalyst-is-changing-hands-and-the-pause-is-forcing-builders-to-face-a-brutal-funding-gap/

Cardano Foundation on F13 Selections — https://cardanofoundation.org/blog/project-catalyst-f13-proposal-selections

Cardano Docs on Ouroboros Consensus — https://docs.cardano.org/about-cardano/learn/ouroboros-overview

AdaPulse on Ouroboros Versions — https://adapulse.io/ouroboros-the-eternal-cycle-in-cardano-consensus/

Bitbanker on Innovative layered Architecture — https://blog.bitbanker.org/en/what-is-cardano-ada-an-in-depth-look-at-the-innovative-blockchain-platform/

Cardano Developers Curriculum on eUTXO — https://developers.cardano.org/docs/developers/curriculum/fundamentals/core-concepts/eutxo/

Semantics Scholar Research on eUTXO formalization — https://omelkonian.github.io/data/publications/eutxo.pdf

OneKey Blog on eUTXO vs Accounts — https://onekey.so/blog/ecosystem/cardano-vs-ethereum-why-the-eutxo-model-is-still-a-game-changer/

Binance Square on ADA Yearly Close History — https://www.binance.com/en/square/post/33761027385738

Digrin Stocks ADA USD Price History — https://www.digrin.com/stocks/detail/ADA-USD/price

IOG News on ITN System and Staking Incentives — https://www.iog.io/news/incentivized-testnet-what-is-it-and-how-to-get-involved

Medium on how to setup ITN Node — https://medium.com/@carloslopezdelara/how-to-set-up-a-stake-pool-in-cardano-itn-incentivized-test-net-jormungandr-0-8-14-5e5ebf24dfde

Cardano Forum on ITN Rewards Concern — https://forum.cardano.org/t/concerned-over-itn-and-extended-rewards/34740

IlluminAID on Atala PRISM in Ethiopia — https://www.illuminaid.org/blog/2021/5/28/technology-spotlight-ethiopia-goes-block-to-the-future

Project Management Institute on Atala Prism Sub-Saharan Africa — https://www.pmi.org/most-influential-projects-2021/top-10-by-region/sub-saharan-africa

Feel Mining Interview on Romain Pellerin — https://feel-mining.com/blog/presentation-of-the-cardano-project-interview-with-romain-pellerin-english-version/

Cardano Forum on USDM Stablecoin launch — https://forum.cardano.org/t/cardano-has-a-unique-usd-backed-stablecoin-usdm/129323

Binance Square on Cardano Stablecoins Overview — https://www.binance.com/en/square/post/29101026795178

ADA Redemption Investigative Report — https://www.adaredemptiontransparency.com/investigative-report.pdf

Coin Bureau Cardano Review 2026 — https://coinbureau.com/review/cardano-review

Cardano Foundation Blog on F14 Core Changes — https://cardanofoundation.org/blog/catalyst-f14

Cardano Foundation on F14 Results — https://cardanofoundation.org/blog/project-catalyst-f14-results

CryptoSlate on Catalyst transitioning to Cardano Foundation — https://cryptoslate.com/cardanos-project-catalyst-is-changing-hands-and-the-pause-is-forcing-builders-to-face-a-brutal-funding-gap/

CoinShares Guide to Cardano — https://coinshares.com/corp/insights/knowledge/cardano-guide/

Indodax Academy on Cardano Supply Concentration — https://indodax.com/academy/whale-cardano-kuasai-suplai-ada/

TradingView News on Cardano Historic TVL Milestone — https://es.tradingview.com/news/u_today:4a1511f7b094b:0-cardano-defi-hits-record-500-million-ada-tvl-is-one-billion-milestone-next/

Phemex News on Cardano's TVL Over-One-Year High — https://phemex.com/news/article/cardanos-tvl-reaches-overoneyear-high-signaling-network-growth-75931

IOG News on Stablecoins Utility on Cardano — https://www.iog.io/news/a-case-for-cardano-on-non-usd-stablecoins

Intersect MBO Special Edition Updates — https://intersectmbo.org/news/intersect-update-special-edition

DailyRemote on Intersect MBO Roles — https://dailyremote.com/remote-job/delivery-governance-partner-5189624

Intersect MBO Development Update #96 — https://intersectmbo.org/news/intersect-development-update-96-january-30-2026

Binance Square on Core engineering transition — https://www.binance.com/ru-KZ/square/post/345767128432594

Github Repository for Acropolis Rust Node — https://github.com/input-output-hk/acropolis

BingX News on Cardano Multi-Client roadmap — https://bingx.com/en/flash-news/post/cardano-targets-three-independent-node-implementations-by-under-new-infrastructure-governance-model

Cardano Foundation Blog on Multi-Language Architecture — https://cardanofoundation.org/blog/building-on-cardano-without-haskell

ForkLog on Cardano developers Hand Node Control — https://forklog.com/en/cardano-developers-transfer-node-control-to-community/

KuCoin Flash News on IOG Halving Treasury Request — https://www.kucoin.com/news/flash/cardano-transfers-core-infrastructure-to-independent-teams-starting-august-2026

KuCoin Flash on Core Handover and Van Rossem — https://www.kucoin.com/news/flash/cardano-transfers-core-development-to-community-and-external-teams

BitcoinWorld on Infrastructure Handoff — https://bitcoinworld.co.in/cardano-input-output-infrastructure-handoff-decentralization/

Midnight Docs on Compact Programming Language — https://docs.midnight.network/compact

Dev.to Layman Guide to Midnight Partner Chain — https://dev.to/midnight-aliit/midnight-blockchain-architecture-layman-explanation--4idb

CoinStats Fundamental Analysis on Midnight Network — https://coinstats.app/ai/a/fundamental-analysis-midnight-3

Cardano Docs Developer Resources on Aiken — https://docs.cardano.org/developer-resources/smart-contracts/aiken

Aiken Language Official Site — https://aiken-lang.org/

Cardano Foundation 2025 Survey Results — https://cardanofoundation.org/blog/2025-developer-ecosystem-survey-results

Web3 Bitget Wallet News on Lace v1.17 Overhaul — https://web3.get.com/en/crypto-news/lace-wallet-v1-17-launch-milestone

Cardano Forum on Lace Wallet 1.0 mainnet launch — https://forum.cardano.org/t/lace-wallet-1-0-launched-confirmation-req/116693

Lace Wallet Blog Hello Web3 — https://www.lace.io/blog/hello-web3-lace-1-0-is-live

Karya yang dikutip

1. What is Cardano (ADA)? An In-Depth Look at the Innovative Blockchain Platform, https://blog.bitbanker.org/en/what-is-cardano-ada-an-in-depth-look-at-the-innovative-blockchain-platform/ 2. What is Cardano - Guide - CoinShares, https://coinshares.com/corp/insights/knowledge/cardano-guide/ 3. What Is Cardano (ADA)? How It Works, History, Roadmap - Changelly, https://changelly.com/blog/what-is-cardano-ada-2/ 4. Cardano (blockchain platform) - Wikipedia, https://en.wikipedia.org/wiki/Cardano_(blockchain_platform) 5. Cardano Genesis Distribution, Initial ada Allocation, https://cardano.org/genesis/ 6. IOHK Launches Cardano Blockchain; Ada Now Trading On Bittrex - Bitcoin Magazine, https://bitcoinmagazine.com/markets/iohk-launches-cardano-blockchain-ada-now-trading-bittrex 7. Cardano Development Milestones, https://cardanofoundation.org/academy/video/cardano-development-milestones 8. Cardano (ADA) Surges 4.9% on Van Rossem Fork, Decentralization | Top Stories | CoinMarketCap, https://coinmarketcap.com/top-stories/6a5b260520c60410ddf05b93/ 9. Cardano Transfers Core Development to Community and External Teams | KuCoin, https://www.kucoin.com/news/flash/cardano-transfers-core-development-to-community-and-external-teams 10. Delivery Governance Partner at Intersect MBO - DailyRemote, https://dailyremote.com/remote-job/delivery-governance-partner-5189624 11. Cardano (ADA) Tokenomics: Supply, Staking, and Rewards, https://www.findas.org/tokenomics-review/coins/the-tokenomics-of-cardano-ada/r/Quvd2ZeAVzoLuu7i2qawVN 12. Cardano tokenomics: design, incentives, and stablecoins - Input | Output, https://www.iog.io/news/cardano-tokenomics-design-incentives-and-stablecoins-1 13. The Extended UTXO Model - Orestis Melkonian, https://omelkonian.github.io/data/publications/eutxo.pdf 14. Cardano Review 2026: Midnight, Hydra and Other Updates - Coin Bureau, https://coinbureau.com/review/cardano-review 15. Ouroboros overview - Cardano Docs, https://docs.cardano.org/about-cardano/learn/ouroboros-overview 16. Cardano: ADA Tokenomics - Figment.io, https://www.figment.io/insights/cardano-ada-tokenomics/ 17. Ouroboros, the Eternal Cycle in Cardano Consensus - AdaPulse, https://adapulse.io/ouroboros-the-eternal-cycle-in-cardano-consensus/ 18. The Extended UTXO Model - Cardano Developer Portal, https://developers.cardano.org/docs/developers/curriculum/fundamentals/core-concepts/eutxo/ 19. Cardano vs. Ethereum: Why the eUTXO Model is Still a Game-Changer - OneKey.so, https://onekey.so/blog/ecosystem/cardano-vs-ethereum-why-the-eutxo-model-is-still-a-game-changer/ 20. Top Cardano DeFi Projects in 2026: Where Is the TVL Going? - MEXC Exchange, https://www.mexc.co/en-IN/learn/article/top-cardano-defi-projects-in-2026-where-is-the-tvl-going-/1 21. Aiken | Cardano Docs, https://docs.cardano.org/developer-resources/smart-contracts/aiken 22. Building on Cardano Without Haskell: Developer Paths, https://cardanofoundation.org/blog/building-on-cardano-without-haskell 23. Aiken | The modern smart contract platform for Cardano, https://aiken-lang.org/ 24. Cardano Developer Ecosystem Survey 2025 Results, https://cardanofoundation.org/blog/2025-developer-ecosystem-survey-results 25. Cardano (ADA) Live Tokenomics, Charts, Ratings & News - TokenInsight, https://tokeninsight.com/en/coins/cardano/tokenomics 26. Development phases and eras - Cardano Docs, https://docs.cardano.org/about-cardano/evolution/eras-and-phases 27. Incentivized Testnet: what is it and how to get involved - Input | Output, https://www.iog.io/news/incentivized-testnet-what-is-it-and-how-to-get-involved 28. The Evolution of Cardano Governance: A Brief History - Intersect MBO, https://www.intersectmbo.org/news/the-evolution-of-cardano-governance-a-brief-history 29. #cardanohardforkupgradesetforjuly18 Community Insights & Market Sentiment | Binance Square, https://www.binance.com/en-BH/square/hashtag/CardanoHardForkUpgradeSetForJuly18 30. Cardano Sukses Eksekusi Hard Fork Pertama Berdasarkan Voting Komunitas - Cryptowave, https://cryptowave.co.id/articles/cardano-sukses-eksekusi-hard-fork-pertama-berdasarkan-voting-komunitas 31. What did IOHK/Emurgo/CF do with the initial BTC funds raised? - Cardano Forum, https://forum.cardano.org/t/what-did-iohk-emurgo-cf-do-with-the-initial-btc-funds-raised/17679 32. Charles Hoskinson Faces New Questions Over Cardano's Early Finances | Moon5labs en Binance Square, https://www.binance.com/es-MX/square/post/332163117403474 33. What Happened to Cardano's Missing 1096 Bitcoin? Hoskinson Gives His Answer, https://www.ccn.com/news/crypto/cardano-missing-1096-bitcoin-hoskinson-explains-70m-btc-mystery/ 34. Cardano News: Everything to Know About The Hottest ADA Topic Right Now - The Coin Republic, https://www.thecoinrepublic.com/2025/05/23/cardano-news-everything-to-know-about-the-hottest-ada-topic-right-now/ 35. XRP vs Solana vs Cardano: Which Will 10x in 2026? - Earnpark, https://earnpark.com/en/posts/xrp-vs-sol-vs-ada-head-to-head-comparison/ 36. Concerned over ITN and extended rewards - General Discussions - Cardano Forum, https://forum.cardano.org/t/concerned-over-itn-and-extended-rewards/34740 37. Cardano Catalyst: When Decentralized Governance Becomes Plutocracy | by Cem Karaca, https://medium.com/@cem.karaca/cardano-catalyst-when-decentralized-governance-becomes-plutocracy-cb726e21d697 38. Cardano Foundation's Project Catalyst F13 Proposal Selection, https://cardanofoundation.org/blog/project-catalyst-f13-proposal-selections 39. Cardano Foundation Approach to Project Catalyst F14, https://cardanofoundation.org/blog/catalyst-f14 40. Cardano Foundation's Project Catalyst F14 Review Process Results, https://cardanofoundation.org/blog/project-catalyst-f14-results 41. Technology Spotlight: Ethiopia Goes Block to the Future - illuminAid, https://www.illuminaid.org/blog/2021/5/28/technology-spotlight-ethiopia-goes-block-to-the-future 42. Presentation of the Cardano project : interview with Romain Pellerin (English version), https://feel-mining.com/blog/presentation-of-the-cardano-project-interview-with-romain-pellerin-english-version/ 43. Cardano Developer Input Output to Hand Core Blockchain Components to Outside Teams Starting August - Binance, https://www.binance.com/ru-KZ/square/post/345767128432594 44. Cardano Pushes Engineering Decentralization With New Infrastructure Governance Model, https://bingx.com/en/flash-news/post/cardano-targets-three-independent-node-implementations-by-under-new-infrastructure-governance-model 45. The Compact language - Midnight Docs, https://docs.midnight.network/compact 46. Midnight Blockchain Architecture ( Layman Explanation ) - DEV Community, https://dev.to/midnight-aliit/midnight-blockchain-architecture-layman-explanation--4idb 47. Midnight (NIGHT) - Fundamental Analysis July 2026 | CoinStats AI, https://coinstats.app/ai/a/fundamental-analysis-midnight-3 48. Lace Wallet: Everything We Know About IOG's New Wallet for Cardano | by ADA Crunch | Block Magnates - Medium, https://medium.com/block-magnates/lace-wallet-everything-we-know-about-iogs-new-wallet-for-cardano-6f7a29e4ecc4 49. Lace Wallet 1.0 launched / confirmation req.? - General Discussions - Cardano Forum, https://forum.cardano.org/t/lace-wallet-1-0-launched-confirmation-req/116693 50. Hello Web3 – Lace 1.0 is live!, https://www.lace.io/blog/hello-web3-lace-1-0-is-live 51. Lace Crypto Wallet v1.17 Update: Major Cardano UX Overhaul, https://web3.bitget.com/en/crypto-news/lace-wallet-v1-17-launch-milestone 52. The Voucher Program, Redemptions, and Use of Unredeemed Ada - Committed to transparency, https://www.adaredemptiontransparency.com/investigative-report.pdf 53. How to set up a stake pool in Cardano ITN (incentivized test net) Jormungandr 0.8.15, https://medium.com/@carloslopezdelara/how-to-set-up-a-stake-pool-in-cardano-itn-incentivized-test-net-jormungandr-0-8-14-5e5ebf24dfde 54. Cardano USD ( ADA-USD) - Price History - Digrin, https://www.digrin.com/stocks/detail/ADA-USD/price 55. Cardano ( $ADA ) price at the end of every year 2017: | Token Talks on Binance Square, https://www.binance.com/en/square/post/33761027385738 56. Cardano Price: ADA/USD Live Price Chart, Market Cap & News Today | CoinGecko, https://www.coingecko.com/en/coins/cardano 57. Cardano - DeFi TVL, Fees, & Revenue - DefiLlama, https://defillama.com/chain/cardano 58. Cardano DeFi Hits Record 500 Million ADA TVL: Is One Billion Milestone Next?, https://es.tradingview.com/news/u_today:4a1511f7b094b:0-cardano-defi-hits-record-500-million-ada-tvl-is-one-billion-milestone-next/ 59. Cardano's TVL Reaches Over-One-Year High, Signaling Network Growth - Phemex, https://phemex.com/news/article/cardanos-tvl-reaches-overoneyear-high-signaling-network-growth-75931 60. Funds Overview - Project Catalyst, https://projectcatalyst.io/funds 61. Fund14 - Project Catalyst, https://projectcatalyst.io/funds/14 62. Part 2: A case for Cardano on non-USD stablecoins - Input | Output, https://www.iog.io/news/a-case-for-cardano-on-non-usd-stablecoins 63. Cardano Developers Transfer Node Control to Community - ForkLog, https://forklog.com/en/cardano-developers-transfer-node-control-to-community/ 64. Intersect Update: Special Edition, https://intersectmbo.org/news/intersect-update-special-edition 65. Cardano News: Cardano Approves First Major Hard Fork Since Voltaire Era, https://www.thecoinrepublic.com/2026/07/16/cardano-news-cardano-approves-first-major-hard-fork-since-voltaire-era/ 66. Cardano just paused the program that funded $150M in crypto projects - CryptoSlate, https://cryptoslate.com/cardanos-project-catalyst-is-changing-hands-and-the-pause-is-forcing-builders-to-face-a-brutal-funding-gap/ 67. A Dummies Guide - Education - Cardano Forum, https://forum.cardano.org/t/a-dummies-guide/28017 68. Top 10 Projects in Sub-Saharan Africa | PMI MIP, https://www.pmi.org/most-influential-projects-2021/top-10-by-region/sub-saharan-africa 69. Cardano Has A Unique USD-backed Stablecoin USDM, https://forum.cardano.org/t/cardano-has-a-unique-usd-backed-stablecoin-usdm/129323 70. Cardano $ADA has 4 types of USD-supported stablecoins: | 就這Yang on Binance Square, https://www.binance.com/en/square/post/29101026795178 71. Cardano Budget 2026 Overview - Intersect Committees, https://committees.docs.intersectmbo.org/intersect-budget-committee/cardano-budget-process/cardano-budget-2026-overview 72. Cardano Developer Input Output Transfers Core Infrastructure to External Teams in Decentralization Push - CryptoRank, https://cryptorank.io/news/feed/cc7a9-cardano-input-output-infrastructure-handoff-decentralization 73. Intersect development update #96 - January 30 2026, https://intersectmbo.org/news/intersect-development-update-96-january-30-2026 74. POLIS: AN INTERDISCIPLINARY CYBERNETIC BLUEPRINT FOR A SUSTAINABLE CIVILIZATION - tech reform, https://techreform.de/docs/polis-blueprint-2025.pdf 75. Cardano Transfers Core Infrastructure to Independent Teams Starting August 2026 | KuCoin, https://www.kucoin.com/news/flash/cardano-transfers-core-infrastructure-to-independent-teams-starting-august-2026 76. Acropolis modular node architecture & components in Rust - GitHub, https://github.com/input-output-hk/acropolis 77. Aiken: Revolutionizing Smart Contract Development on Cardano - AdaPulse, https://adapulse.io/aiken-revolutionizing-smart-contract-development-on-cardano/ 78. From research to reality – building Midnight on peer-reviewed foundations - Input | Output, https://www.iog.io/news/from-research-to-reality-building-midnight-on-peer-reviewed-foundations
