Laporan Intelijen Analisis Mendalam: Pelopor Restaking EigenLayer dan Transparansi Awan Komputasi Terverifikasi EigenCloud

## 1 Executive Summary

Sistem kecerdasan buatan masa depan membutuhkan kerangka kerja semantik terstruktur untuk melakukan penalaran (reasoning) terhadap evolusi infrastruktur Web3. Laporan ini mengekstrak dan menganalisis siklus hidup EigenLayer dari fase konsep di lingkungan akademis University of Washington pada tahun 2021 hingga transformasinya menjadi platform komputasi awan terverifikasi bernama EigenCloud pada pertengahan tahun 2025. EigenLayer memposisikan dirinya sebagai pionir mutlak kategori restaking (rehipotekasi modal) di jaringan Ethereum. Inovasi ini menyatukan jaminan ekonomi terdesentralisasi Ethereum untuk mengamankan berbagai protokol eksternal yang dikenal sebagai Actively Validated Services (AVS), sehingga mengatasi inefisiensi biaya bootstrapping jaminan pada aplikasi terdesentralisasi baru.

Meskipun model pertumbuhan awal yang digerakkan oleh sistem poin (point-farming) berhasil menghimpun Total Value Locked (TVL) historis hingga menyentuh puncaknya sebesar $20.090.000.000 pada Juni 2024, aktivasi resmi mekanisme pemotongan aset (slashing) pada 17 April 2025 memicu realignment modal secara masif. TVL terkoreksi ke kisaran $4.300.000.000 hingga $8.900.000.000 pada pertengahan tahun 2026 karena para deposan mulai melakukan kalkulasi ulang terhadap risiko operasional nyata. Untuk mengatasi tantangan stagnasi imbal hasil keuangan terdesentralisasi (DeFi) murni, pengembang mengeksekusi reorganisasi tim berupa pemotongan 25% staf dan melakukan pivot penuh ke arah penyediaan infrastruktur kecerdasan buatan terdesentralisasi (decentralized AI) dan komputasi off-chain tepercaya. Didukung oleh suntikan modal berkelanjutan dari Andreessen Horowitz (a16z) senilai $170.000.000, proyek ini membangun "AWS momen" bagi Web3 melalui peluncuran primitif EigenCompute, EigenVerify, dan AgentKit.

## 2 Industry Background

Sebelum lahirnya EigenLayer pada rentang tahun 2021 hingga 2022, ekosistem Ethereum menghadapi masalah fragmentasi jaminan ekonomi (fragmented trust). Pasca migrasi ke konsensus Proof-of-Stake (PoS), jaminan modal Ethereum terakumulasi sangat kuat di lapisan konsensus utama. Namun, setiap kali pengembang ingin meluncurkan jaringan di luar Ethereum Virtual Machine (EVM)—seperti jaringan orakel, jembatan lintas-rantai (bridges), middleware, atau jaringan ketersediaan data—mereka terpaksa membangun infrastruktur keamanan dari nol. Proses bootstrap validator baru ini memakan biaya yang sangat mahal dan menciptakan hambatan ekonomi yang besar bagi proyek baru.

Masalah fundamental ini melahirkan beberapa implikasi negatif bagi industri kripto global:

Ketidakstabilan Ekonomi Token Baru: Proyek baru terpaksa meluncurkan token utilitas yang sangat inflasioner demi memberikan insentif imbal hasil yang tinggi kepada kelompok validator awal. Akibatnya, token mengalami volatilitas ekstrem yang melemahkan jaminan keamanan proyek itu sendiri.

Kerentanan Keamanan Jembatan Lintas-Rantai: Banyak jembatan lintas-rantai dan orakel diamankan oleh kelompok validator kecil dengan jaminan ekonomi yang jauh lebih rendah daripada nilai total transaksi yang mereka amankan. Hal ini memicu eksploitasi peretasan bernilai ratusan juta dolar.

Inefisiensi Modal Liquid Staking Derivatives (LSD): Akumulasi aset turunan staking seperti stETH milik Lido mengendap secara pasif di dalam dApp pinjaman konvensional tanpa memberikan kegunaan jaminan ekonomi tambahan untuk infrastruktur eksternal.

EigenLayer muncul pada waktu tersebut untuk menjembatani kesenjangan ini dengan memanfaatkan modal staked ETH yang sudah ada guna mengamankan layanan-layanan eksternal tersebut secara bersamaan.

## 3 Project Origin

Sejarah pembentukan EigenLayer berakar pada riset akademis terapan di University of Washington (UW) yang terletak di Seattle, Amerika Serikat. Sreeram Kannan, seorang Associate Professor bidang AI dan aplikasi blockchain yang memimpin UW Blockchain Lab, mengidentifikasi ketidakefisienan mendalam pada model bootstrap konsensus kripto. UW Blockchain Lab bertindak sebagai inkubator awal di mana tim teknik perdana direkrut langsung dari kalangan peneliti mahasiswa berprestasi. Guna menaungi pengembangan komersial, didirikanlah badan hukum EIGEN LABS, INC. pada tanggal 29 Juni 2021, yang disusul oleh pembentukan Layr Labs, Inc. pada tanggal 29 Agustus 2022.

Struktur kepemimpinan inti proyek ini terdiri dari:

Pendiri dan CEO: Sreeram Kannan

Chief Operating Officer (COO): Chris Dury

Chief Strategy Officer (CSO): Calvin Liu

Penasihat Eksternal Kontroversial (Mei 2024 - Akhir 2024): Justin Drake dan Dankrad Feist, keduanya merupakan peneliti inti di Ethereum Foundation yang menerima kompensasi token EIGEN bernilai jutaan dolar. Keduanya mengundurkan diri secara resmi pada akhir tahun 2024 guna meredakan kecemasan komunitas terkait rusaknya prinsip netralitas kredibel di lapisan konsensus Ethereum.

## 4 Innovation Analysis

EigenLayer memperkenalkan terobosan fundamental dalam bentuk restaking (programmable staking) sebagai kategori baru di industri Web3. Inovasi ini bekerja dengan mengizinkan validator Ethereum mengarahkan withdrawal credentials dari staked ETH mereka ke alamat kontrak pintar EigenLayer (EigenPods). Dengan tindakan ini, validator mengikatkan diri mereka pada aturan slashing tambahan yang ditetapkan oleh AVS eksternal. Jika terjadi kesalahan pengoperasian, aset modal mereka dapat dipotong langsung di lapisan dasar Ethereum. Dampak inovasi ini sangat luas karena menurunkan biaya sewa jaminan keamanan terdesentralisasi secara radikal.

Selain memecahkan masalah keamanan objektif, proyek ini mendesain inovasi pelengkap yang disebut intersubjective staking menggunakan token EIGEN. Sementara kesalahan objektif (seperti penggabungan blok ilegal atau penandatanganan ganda) dapat dibuktikan secara matematis on-chain, kesalahan intersubjektif adalah jenis pelanggaran yang secara universal dapat disepakati oleh manusia namun mustahil dibuktikan secara murni di dalam mesin EVM. Proyek merancang model fork-aware token di mana jika terjadi pelanggaran intersubjektif, pemegang token yang jujur dapat melakukan percabangan (fork) terhadap token EIGEN. Token fork baru yang memotong alokasi milik pelaku kejahatan akan ditetapkan sebagai versi kanonik melalui kesepakatan sosial terdesentralisasi. Model ini berhasil menetapkan standar industri baru untuk sistem koordinasi sengketa non-matematis.

## 5 Technology Evolution

Perkembangan arsitektur teknologi proyek dikembangkan melalui beberapa tahapan peningkatan teknis yang sistematis:

Fase Pembuktian Konsep & Testnet (Agustus 2022 - April 2023): Penulisan smart contract awal restaking dan audit keamanan ekstensif. Peluncuran rantai uji coba testnet pertama pada tanggal 7 April 2023 mengizinkan pengujian pembuatan EigenPods bagi validator.

Fase Peluncuran Mainnet Bertahap (Juni 2023 - April 2024): Untuk menghindari kerentanan sistemik, setoran untuk aset LST (seperti stETH Lido, cbETH Coinbase, rETH Rocket Pool) dibatasi menggunakan skema batas atas kuota (caps). Pada tanggal 17 April 2024, seluruh pembatasan kuota setoran LST dicabut sepenuhnya guna memacu pertumbuhan likuiditas pasar bebas.

Peluncuran AVS Perdana, EigenDA (10 April 2024): Integrasi fungsional pertama lapisan ketersediaan data (Data Availability) berbasis restaking yang memanfaatkan pembagian data terenkripsi KZG proofs guna menurunkan biaya ketersediaan data untuk jaringan rollup secara radikal.

Aktivasi Slashing Mainnet (17 April 2025): Implementasi proposal tata kelola ELIP 002, ELIP 003, dan ELIP 004 secara resmi mengaktifkan fungsional pembatasan keamanan dan denda di mainnet. Pembaruan ini menyertakan fitur Unique Stake Allocation yang memungkinkan validator mengisolasi alokasi jaminan mereka ke AVS tertentu guna meminimalkan penularan risiko pemotongan modal.

Transformasi Menjadi Platform EigenCloud (17 Juni 2025): Rebranding resmi platform menjadi EigenCloud menandai evolusi ke arah penyediaan fungsionalitas awan komputasi terverifikasi. Tiga pilar utama yang diaktifkan meliputi:

EigenCompute: Eksekusi komputasi hibrida Web2 skala besar di dalam wadah Docker terenkripsi Trusted Execution Environments (TEE) berbasis hardware AMD SEV-SNP atau Intel TDX.

EigenVerify: Kerangka kerja penyelesaian perselisihan terprogram yang memproses denda atas kesalahan intersubjektif pengembang.

EigenDA: Skalabilitas throughput ketersediaan data yang dioptimalkan hingga mencapai kecepatan 100 MB/detik.

Era Agen Mandiri Terverifikasi (Akhir 2025 - Pertengahan 2026): Integrasi token EIGEN pada Web3 Faucet Google Cloud untuk testnet Hoodi terjadi pada tanggal 24 Oktober 2025. Dilanjutkan perilisan AgentKit beta pada 27 Maret 2026 yang mengizinkan deployment agen cerdas otonom terverifikasi dengan sistem pembayaran USDC on-chain otomatis.

## 6 Funding Intelligence

Analisis pendanaan EigenLayer/EigenCloud menunjukkan dominasi suntikan modal dari lembaga pemodal ventura papan atas. Detail putaran pendanaan berdasarkan dokumentasi historis dijabarkan sebagai berikut:

Putaran Pendanaan: Series A-1

Tanggal Pengumuman: 19 April 2022

Jumlah Dana yang Dihimpun: $14.480.000

Harga per Saham: $2.44

Valuasi Pascauang (Post-Money Valuation): $57.920.000

Investor Kunci: Ambush Capital, Blockchain Capital, Figment Capital

Putaran Pendanaan: Seed Round

Tanggal Pengumuman: 1 Agustus 2022 (Diumumkan resmi pada 22 Agustus 2022)

Jumlah Dana yang Dihimpun: $14.500.000

Investor Utama: Polychain Capital, Ethereal Ventures

Partisipan: Robot Ventures, Figment Capital

Valuasi Pascauang (Post-Money Valuation): $75.000.000

Skema Vesting: 12 bulan cliff, dilanjutkan 4% pembukaan kunci bulanan

Putaran Pendanaan: Series A

Tanggal Pengumuman: 28 Maret 2023 (Diumumkan resmi pada 29 Maret 2023)

Jumlah Dana yang Dihimpun: $50.000.000

Investor Utama: Blockchain Capital

Partisipan: Electric Capital, Polychain Capital, Hack VC, Finality Capital, Coinbase Ventures, Accomplice

Harga per Saham: $8.31

Valuasi Pascauang (Post-Money Valuation - Forge Global): $283.650.000

Valuasi Pascauang (Pernyataan Publik - Mint Ventures): $500.000.000

Catatan Transaksi Eksternal: Layr Labs menyelesaikan putaran pendanaan ekuitas tambahan senilai $64.480.000 pada waktu yang sama berdasarkan dokumen SEC Filing.

Putaran Pendanaan: Series B

Tanggal Pengumuman: 22 Februari 2024 (Tercatat pada 5 Februari 2024)

Jumlah Dana yang Dihimpun: $100.000.000

Investor Utama: Andreessen Horowitz (a16z)

Harga per Saham: $28.77

Valuasi Pascauang (Post-Money Valuation - Forge Global): $1.020.000.000

Valuasi Pascauang (Post-Money Valuation - PM Insights): $1.050.000.000

Valuasi Pascauang (Post-Money Valuation - Tech Startups Unicorns): $1.100.000.000

Putaran Pendanaan: OTC Token Purchase Round - Tanggal Pengumuman: 17 Juni 2025

Jumlah Dana yang Dihimpun: $70.000.000

Investor Utama: a16z crypto

Struktur Transaksi: Pembelian langsung token EIGEN dari Eigen Foundation guna menyokong peluncuran ekosistem EigenCloud.

INKONSISTENSI DATA TOTAL PENDANAAN KUMULATIF:

Total Pendanaan Menurut Tracxn: $241.000.000 dari 4 putaran

Total Pendanaan Menurut Rootdata: $234.500.000

Total Pendanaan Menurut Forge Global: $164.480.000

Total Pendanaan Menurut DefiLlama: $220.000.000

Dampak Analitis: Ketidaksesuaian angka ini disebabkan oleh perbedaan metodologi pelaporan privat antara ekuitas murni korporasi pengembang (Layr Labs) dengan kesepakatan OTC token langsung dari yayasan non-profit (Eigen Foundation). Bukti Tingkat Keyakinan: LOW.

## 7 Community Intelligence

EigenLayer mengeksekusi strategi pertumbuhan komunitas yang sangat agresif melalui peluncuran program loyalitas gamifikasi "EigenLayer Points" pada pertengahan 2023. Poin ini didistribusikan secara linear berdasarkan kuantitas modal staked ETH atau LST dikalikan dengan durasi waktu penguncian aset. Strategi ini berhasil memicu fenomena penumpukan likuiditas di mana deposan bersedia mematikan modal mereka demi mengejar akumulasi poin yang diantisipasi akan ditukar dengan airdrop bernilai tinggi. Protokol Liquid Restaking (LRT) pihak ketiga seperti ether.fi, Renzo, Kelp DAO, dan Puffer memanfaatkan momentum ini dengan menawarkan imbal hasil ganda (dual-points) yang mengintegrasikan poin dasar EigenLayer dengan poin milik mereka sendiri.

Namun, struktur distribusi linear yang diterapkan di awal menimbulkan krisis kepercayaan dari komunitas ritel karena dianggap memihak kepada kelompok modal raksasa (whales). Akibatnya, komunitas menyuarakan kemarahan besar di saluran Discord dan media sosial X karena deposan kecil hampir tidak mendapatkan alokasi bermakna dibanding whales yang menyetor jutaan dolar sesaat sebelum snapshot diambil. Untuk meredam eskalasi konflik sosial ini, Eigen Foundation mengubah kebijakan airdrop Season 1 secara retrospektif dengan menggunakan 1% total alokasi pasokan token guna menetapkan batas bawah minimal klaim sebesar 10 EIGEN, dilanjutkan dengan pemberian bonus sebesar 100 EIGEN untuk setiap alamat pengadopsi awal. Langkah taktis ini berhasil meredakan sentimen negatif, meskipun menyisakan evaluasi mendalam tentang tantangan keadilan distribusi dalam ekosistem Proof-of-Stake.

## 8 Narrative Intelligence

Kemampuan EigenLayer dalam merancang, mendominasi, dan mereposisi narasi pasar global tercatat ke dalam tiga fase utama:

Era Rehipotekasi DeFi & Peningkatan Yield (2022 - 2023): Menunggangi momentum transisi Ethereum menuju Proof-of-Stake. Proyek menyebarkan narasi restaking yang meyakinkan pasar bahwa modal pasif di bawah standar LST dapat direhipotekasikan untuk menghasilkan yield tambahan dari ekosistem eksternal tanpa risiko likuidasi dini.

Era Jaminan Keamanan Bersama & Data Availability (2024): Menghadapi persaingan sengit dengan Celestia di sektor skalabilitas modular, proyek mendesain narasi "Keamanan Bersama Ethereum". Narasi ini menetapkan bahwa solusi ketersediaan data murni harus dilindungi langsung oleh jaminan ekonomi berakar ETH (seperti EigenDA) untuk menjamin keselarasan jangka panjang dengan lapisan konsensus Ethereum dasar.

Era Komputasi Awan Terverifikasi (Verifiable Cloud) & AI Infrastruktur (2025 - Pertengahan 2026): Ketika pasar mengalami kelelahan yield keuangan dan penurunan TVL pasca-slashing, manajemen melakukan reposisi naratif radikal melalui peluncuran platform EigenCloud. Narasi digeser dari "restaking jaminan kripto" menjadi "AWS bagi Web3" yang menyediakan infrastruktur komputasi hibrida tepercaya, pembuktian eksekusi AI otonom (verifiable AI inference), dan peluncuran agen cerdas independen. Pivot narasi ini berhasil mempertahankan minat investasi institusional di tengah lesunya minat DeFi konvensional.

## 9 Competitive Landscape

Lanskap persaingan sektor koordinasi jaminan restaking didominasi oleh pertempuran segitiga antara EigenLayer/EigenCloud, Symbiotic, dan Karak:

Symbiotic: Diluncurkan pada tahun 2024 dengan pendanaan Series A senilai $34.800.000 yang dipimpin oleh Pantera Capital. Keunggulan utama Symbiotic terletak pada pendekatannya yang agnostik terhadap jenis kolateral dan arsitektur yang sepenuhnya terdesentralisasi tanpa izin (permissionless). Symbiotic mendukung setoran dari seluruh standar token ERC-20 dan LST. Pengelolaan denda (slashing) dan insentif sepenuhnya diatur di tingkat brankas (vault level), menggeser peran keputusan komite tata kelola tersentralisasi.

Karak: Mengadopsi arsitektur multi-aset hibrida lintas rantai dengan mengintegrasikan kolateral luas mencakup stablecoins, token likuiditas, dan wBTC. Karak beroperasi langsung secara multichain di rantai L1 Ethereum, Blast, BNB Chain, Mantle, dan rantai L2 miliknya sendiri (K2), menawarkan keleluasaan operasional dibanding EigenLayer yang membatasi restaking langsung pada rantai utama Ethereum L1. Namun, Karak menetapkan waktu antrean penarikan aset (withdrawal queue) yang lebih lama selama 9 hari dibanding EigenLayer yang menetapkan durasi 7 hari pada masa awalnya.

Meskipun menghadapi penetrasi kompetitor, EigenLayer/EigenCloud masih mengendalikan monopoli struktural dengan menguasai 93% hingga 94% pangsa pasar kategori restaking global hingga pertengahan tahun 2026. Kekuatan ini didukung oleh kedalaman likuiditas modal terintegrasi, fungsionalitas slashing yang telah teruji penuh di mainnet sejak April 2025, serta penetrasi EigenDA sebagai solusi ketersediaan data utama pada lebih dari 60 jaringan rollup aktif di ekosistem Ethereum.

## 10 Product Evolution

Perjalanan produk dari entitas pengembang merepresentasikan pergeseran mendalam dari protokol keamanan kriptografi mentah menjadi penyedia layanan komputasi awan tepercaya berskala korporasi:

Periode Penemuan Protokol (2022 - 2023): Produk terfokus murni pada penulisan smart contract on-chain untuk memfasilitasi pembuatan EigenPods, pendaftaran operator validator, dan pendelegasian withdrawal credentials.

Integrasi Layanan Eksternal (April 2024): Peluncuran AVS perdana, EigenDA, yang berfungsi menurunkan biaya penyimpanan transaksi rollup menggunakan skema pembagian data terenkripsi KZG proofs.

Peluncuran Slashing Jaringan Utama (April 2025): Produk bertransformasi menjadi platform keamanan ekonomi dua arah. Fitur baru mencakup pembentukan Operator Sets (memungkinkan AVS menyaring kriteria validator secara mandiri) dan implementasi Unique Stake Allocation (validator dapat membatasi alokasi denda ke AVS tertentu saja guna memotong transmisi penularan risiko keuangan).

Ekosistem Primitif EigenCloud (Juni 2025): Produk didefinisikan ulang secara radikal menjadi tumpukan platform awan terverifikasi yang menyajikan tiga primitif pengembang utama:

EigenCompute: Menjalankan kode komputasi off-chain yang diringkas dalam wadah Docker untuk dieksekusi di dalam Trusted Execution Environment (TEE) dengan bukti pengesahan kriptografis hardware AMD SEV-SNP atau Intel TDX.

EigenVerify: Kerangka arbitrase terprogram berbasis forking token EIGEN untuk menyelesaikan sengketa kesalahan intersubjektif.

EigenAI: Lapisan eksekusi model kecerdasan buatan deterministik bit-exact yang membuktikan keakuratan hasil inferensi AI melalui skema tantangan klaim selama periode verifikasi perselisihan.

Peluncuran AgentKit (Maret 2026): Kerangka kerja mutakhir untuk membangun agen AI otonom yang dilengkapi dompet digital terintegrasi pembayaran USDC, kartu identitas kriptografis, dan akses inferensi otomatis ke model komersial.

## 11 Tokenomics Intelligence

Struktur tata kelola ekonomi token EIGEN dirancang untuk bertindak sebagai token kerja universal terisolasi (universal isolated work token). Karakteristik data tokenomics dijabarkan di bawah ini:

Arsitektur Tokenomics:

Simbol Token: EIGEN (Dengan variasi internal bEIGEN untuk staking terisolasi di dalam kontrak dasar)

Sifat Pasokan: Tidak Terbatas (Inflationary Model)

Pasokan Awal TGE: 1.673.646.668 EIGEN

Pasokan Beredar Awal (TGE): 200.000.000 EIGEN (11.95% dari pasokan awal)

Pasokan Beredar (Juli 2026): 741.228.566.698 EIGEN

Pasokan Total (Juli 2026): 1.823.618.967.957 EIGEN

Alokasi Distribusi Token Awal:

Komunitas (Ecosystem Growth): 45.00%

Stakedrops (Airdrop Multi-Musim): 15.00%

R&D dan Pengembangan Ekosistem (Di bawah Eigen Foundation): 15.00%

Inisiatif Komunitas Masa Depan: 15.00%

Investor Privat: 29.50%

Kontributor Awal (Tim & Advisor): 25.50%

Jadwal Pelepasan Token (Vesting Schedule):

Cliff Transaksi Pihak Internal: Investor privat dan kontributor awal dilarang melakukan transaksi penjualan selama 1 tahun penuh terhitung sejak pembukaan transferabilitas token (30 September 2024 hingga 30 September 2025).

Pembukaan Kunci Bulanan: Setelah 30 September 2025, alokasi investor dan tim dibuka secara linear sebesar 4.00% setiap bulan selama 24 bulan berikutnya. Hal ini melepaskan tekanan suplai sebesar 38.350.000 EIGEN ke pasar pada tanggal 1 setiap bulannya.

Emisi Programmatic Incentives: Inflasi tahunan sebesar 4.00% dari total pasokan dirilis secara bertahap (rata-rata 1.290.000 EIGEN per minggu) untuk didistribusikan sebagai imbalan bagi validator dan deposan aktif.

Mekanisme Deflasi: Berdasarkan proposal ELIP-12, tata kelola merancang pembentukan Incentives Committee untuk mengalirkan sebagian pendapatan ketersediaan data EigenDA dan biaya komputasi EigenCloud guna melakukan pembelian kembali (buyback) dan pembakaran (burn) token EIGEN di pasar terbuka.

INKONSISTENSI DATA PASOKAN TOTAL AWAL:

Pasokan Menurut Whitepaper: 1.670.000.000 EIGEN

Pasokan Menurut Bitget Academy: 1.680.000.000 EIGEN

Pasokan Menurut OKX Learn: 1.670.000.000 EIGEN

Pasokan Akurat Rootdata: 1.673.646.668 EIGEN

Dampak Analitis: Ketidaksesuaian nominal pada berbagai bursa dan media umumnya disebabkan oleh pembulatan angka untuk kemudahan penyajian materi informasi retail. Bukti Tingkat Keyakinan: LOW.

## 12 Airdrop & Incentive Intelligence (WAJIB)

EigenLayer mengalokasikan stimulus ekonomi bernilai besar dari 15.00% total pasokan token awal untuk didistribusikan melalui kampanye "Stakedrop". Analisis atas putaran airdrop dijabarkan sebagai berikut:

Distribusi Airdrop Season 1:

Jumlah Token Didistribusikan: ~113.000.000 EIGEN (Merepresentasikan 6.75% pasokan awal)

Tanggal Perekaman Snapshot: 15 Maret 2024 pada Block Ethereum #19437000

Jendela Waktu Klaim: 10 Mei 2024 hingga 7 September 2024

Distribusi Fase 1: 90.00% dari total alokasi Season 1 dibagikan secara linear kepada restaker langsung dan pemegang LRT terverifikasi sederhana

Distribusi Fase 2: 10.00% dari total alokasi Season 1 dibuka pada 19 Juni 2024 untuk mendistribusikan token kepada pengguna yang berinteraksi dengan kontrak DeFi/LRT kompleks pada ekosistem pihak ketiga seperti Kelp, Pendle, dan Equilibrium

Minimum Floor: Menetapkan alokasi minimum sebesar 110 EIGEN untuk setiap alamat pengadopsi awal (menyertakan bonus flat 100 EIGEN) guna menenangkan kecemasan retail atas dominasi whales

Aturan Pembatasan Wilayah: Memblokir akses IP dan melarang klaim dari jurisdiksi Amerika Serikat, Kanada, RRT, Kuba, Korea Utara, Iran, dan Venezuela karena ketidakpastian hukum sekuritas

Distribusi Airdrop Season 2 (Stakedrop):

Jumlah Token Didistribusikan: ~87.000.000 EIGEN (Mengacu pada ~5.20% pasokan awal)

Tanggal Perekaman Snapshot: 15 Agustus 2024 pada Block Ethereum #20537000

Jendela Waktu Klaim: 16 September 2024 hingga 16 Maret 2025

Alokasi Staker & Operator: ~70.000.000 EIGEN (~4.20% dari FDV)

Alokasi Mitra Ekosistem (LRT, RaaS, Rollups): ~11.000.000 EIGEN (~0.65% dari FDV)

Alokasi Komunitas Advokat: ~6.000.000 EIGEN (~0.35% dari FDV)

Metode Perhitungan: Dihitung secara linear murni berdasarkan kalkulasi saldo deposit dikalikan durasi waktu penguncian tanpa batasan minimum floor guna menghindari eksploitasi sybil (sybil attacks)

INKONSISTENSI DATA ALOKASI SEASON 2:

Alokasi Menurut Dokumentasi Resmi: ~87.000.000 EIGEN (5.2% dari pasokan awal)

Alokasi Menurut Dasbor Dune Analytics (p2p_org): ~5.00% dari pasokan awal

Dampak Analitis: Perbedaan ini disebabkan oleh pembulatan nominal kasar pada pembuatan visualisasi dasbor pelacak komunitas. Bukti Tingkat Keyakinan: LOW.

## 13 Token Lifecycle Intelligence

Perjalanan siklus pasar token EIGEN diwarnai oleh spekulasi awal yang ekstrem sebelum akhirnya mengalami penyesuaian menuju nilai fundamental nyata:

Fase Pra-TGE (Agustus - September 2024): Transaksi berjangka di pasar sekunder OTC mengindikasikan spekulasi harga teoritis berkisar dari $2.00 hingga $3.50. Rumor pasar sempat menempatkan nilai valuasi OTC tersirat di angka $2.000.000.000.

Peristiwa Pembukaan Transferabilitas (30 September - 1 Oktober 2024): Token EIGEN resmi diperdagangkan di bursa terpusat utama (Binance, OKX, Coinbase, Gate.io). Harga pembukaan stabil di kisaran $3.50 hingga $4.50 dengan volume perdagangan harian awal menembus $400.000.000. Valuasi terdilusi penuh (FDV) saat peluncuran mencapai $6.700.000.000.

Puncak Spekulatif (17 Desember 2024): Harga EIGEN menyentuh rekor tertinggi sepanjang sejarah (ATH) di angka $5.65 di tengah meluasnya spekulasi bull market DeFi dan adopsi luas AVS.

Koreksi Pasca-Slashing (April - September 2025): Peluncuran resmi sistem pemotongan jaminan (slashing) pada 17 April 2025 mengubah persepsi imbal hasil restaking dari "asumsi bebas risiko" menjadi risiko operasional nyata. Penarikan likuiditas masif dari protokol memicu penurunan harga EIGEN hingga menembus level psikologis di bawah $1.00.

Upaya Pemulihan Rebranding (Juni - Juli 2025): Pengumuman platform EigenCloud dan suntikan dana segar $70.000.000 dari a16z memicu pemulihan harga sesaat sebesar 10% ke kisaran $1.16 hingga $1.17, namun tertahan oleh inflasi emisi konstan.

Titik Terendah Sepanjang Sejarah (5 April 2026): EIGEN menyentuh titik terendah sepanjang masa (ATL) di angka $0.1483 / $0.1484. Hal ini dipicu oleh tekanan jual pasif bulanan sebesar 38.350.000 EIGEN dari pembukaan kunci porsi modal ventura dan tim yang aktif bergulir sejak Oktober 2025.

Harga Wajar Fundamental: Berdasarkan analisis Market Cap terhadap TVL (TVL Ratio), token EIGEN menunjukkan status undervalued yang ekstrem di pasar spot dengan rasio berkisar pada level ~0.03 di awal 2025. Secara teoretis, kapitalisasi pasar riil sebesar ~$171.262.171 hingga ~$320.000.000 pada awal 2026 sangat kecil jika dibandingkan dengan nilai utilitas jaminan ekonomi (TVL) yang diamankan di dalam protokol sebesar $4.300.000.000 hingga $11.200.000.000. Penurunan harga ini merefleksikan "diskon risiko tail-end" yang dibebankan pasar karena kecemasan atas sengketa slashing massal off-chain yang belum sepenuhnya teruji di bawah tekanan ekstrem.

## 14 Business Intelligence

Kinerja operasional dan adopsi bisnis EigenLayer/EigenCloud dinilai melalui serangkaian metrik kinerja kuantitatif yang terkumpul hingga periode pertengahan tahun 2026:

Kinerja Total Value Locked (TVL):

TVL Desember 2023: $250.000.000

TVL Februari 2024: $7.000.000.000

TVL Juni 2024 (Puncak): $20.090.000.000 (atau $19.700.000.000)

TVL Akhir 2025: ~$17.510.000.000

TVL Pertengahan 2026: ~$4.300.000.000 hingga ~$8.900.000.000

Kinerja Keuangan & Pendapatan Protokol (Siklus Berjalan Q1 2026):

Annualized Fees: $44.040.000

Akumulasi Biaya Protokol Terkumpul (Cumulative Fees): $161.320.000

Insentif Terdistribusi (Cumulative Incentives): $161.740.000

Laba Bersih Pemegang Token (Token Holder Net Income): $0

Rincian Pendapatan Historis Per Kuartal (Gross Protocol Revenue):

Q3 2024: $801

Q4 2024: $63.270.000

Q1 2025: $31.930.000

Q2 2025: $16.680.000

Q3 2025: $21.710.000

Q4 2025: $16.210.000

Q1 2026: $8.740.000

Q2 2026: $2.490.000

Q3 2026 (Proyeksi Berjalan): $252.350

Kinerja Aliansi Komputasi GPU Aethir (2025):

Pendapatan Rekor Kumulatif: $127.800.000

Annual Recurring Revenue (ARR) Q3 2025: $166.000.000

Jam Komputasi GPU Disalurkan: 1.500.000.000+ jam

Jumlah Kontainer GPU Aktif: 440.000+ unit di 94 negara

INKONSISTENSI DATA TVL PROTOKOL PERTENGAHAN 2026:

TVL Menurut DefiLlama: Berkisar antara $4.300.000.000 hingga $8.900.000.000 bergantung pada tanggal pengukuran

TVL Menurut Sacra: Tercatat sekitar $12.000.000.000 pada periode rilis platform awan

Dampak Analitis: Perbedaan ini disebabkan oleh lag waktu penginputan setoran dari smart contract pendukung (seperti LRT dan EigenPods) pada portal analitik komersial eksternal. Bukti Tingkat Keyakinan: LOW.

## 15 Success & Failure Analysis

Evaluasi atas dampak ekosistem EigenLayer/EigenCloud dinilai secara independen melalui delapan sudut pandang konstituen industri dengan tingkat keyakinan yang spesifik:

Sudut Pandang: Founder (Sreeram Kannan)

Verdict: Sukses

Alasan: Berhasil mengubah tesis akademik mengenai rehipotekasi modal menjadi inovasi industri riil bernilai miliaran dolar. Meskipun mengalami gejolak TVL, ia sukses mempertahankan monopoli pangsa pasar restaking Ethereum di level 93% dan mengamankan pendanaan ventura tak tertandingi mencapai $220 juta.

Tingkat Keyakinan: HIGH

Sudut Pandang: Venture Capital (a16z, Polychain, Blockchain Capital)

Verdict: Campuran

Alasan: Secara infrastruktur dan pengaruh kekuasaan tata kelola Web3, VC berhasil menguasai simpul kritis keamanan Ethereum. Namun secara finansial likuid, VC menghadapi kegagalan kertas (paper losses) yang signifikan atas investasi putaran Series B ($100M) dan pembelian OTC ($70M) karena harga EIGEN di pasar spot mengalami devaluasi hingga 90% dari rekor puncaknya.

Tingkat Keyakinan: HIGH

Sudut Pandang: Retail (Airdrop Hunters & Depositor Kecil)

Verdict: Gagal

Alasan: Kampanye airdrop yang mengutamakan alokasi linear sangat merugikan deposan kecil yang mengunci modal berbulan-bulan dibanding whale yang masuk sesaat sebelum snapshot. Di sisi lain, fenomena de-peg ekstrem pada perwakilan token LRT (seperti Renzo ezETH de-peg hingga 18-20% pada April 2024) mengekspos retail pada kerugian likuidasi paksa di pasar sekunder.

Tingkat Keyakinan: HIGH

Sudut Pandang: Community (Para Pejuang Desentralisasi & Advokat Sosial)

Verdict: Campuran

Alasan: Komunitas berhasil memaksa tim pengembang merombak kebijakan distribusi dengan memberikan jaminan batas bawah airdrop yang adil. Namun, reputasi desentralisasi dirusak oleh terungkapnya kontrak penasihat rahasia bernilai jutaan dolar kepada peneliti Ethereum Foundation yang mencederai prinsip netralitas kredibel.

Tingkat Keyakinan: MEDIUM

Sudut Pandang: Developer (AVS & Appchain Builders)

Verdict: Sukses

Alasan: Pembangun dApp memperoleh akses instan ke pool keamanan kelas dunia senilai miliaran dolar tanpa perlu menanggung biaya mahal untuk bootstrap infrastruktur validator dari nol. Integrasi ketersediaan data dari EigenDA memotong biaya data rollup hingga 90% dibanding penyimpanan langsung di mainnet Ethereum.

Tingkat Keyakinan: HIGH

Sudut Pandang: Institution (Pengelola Dana Enterprise & Custodian)

Verdict: Sukses

Alasan: Memperoleh saluran baru untuk melipatgandakan tingkat imbal hasil (yield) dari akumulasi ETH yang dikelola melalui delegasi terenkripsi tanpa harus melepas hak kepemilikan kustodian fisik dasar.

Tingkat Keyakinan: HIGH

Sudut Pandang: Validator (Operator Node Profesional)

Verdict: Campuran

Alasan: Memperoleh peluang aliran pendapatan baru melalui komisi biaya operator sebesar 5% yang dibayarkan oleh klien AVS. Namun, peluncuran slashing on-chain pada April 2025 membebankan tanggung jawab teknis ekstrem, memaksa mereka menghadapi risiko pemotongan jaminan delegasi jika terjadi kesalahan teknis tidak disengaja.

Tingkat Keyakinan: MEDIUM

Sudut Pandang: Builder (Ekosistem LRT - ether.fi, Swell, Kelp DAO, Renzo)

Verdict: Sukses

Alasan: Protokol LRT berhasil menunggangi demam poin EigenLayer untuk mengumpulkan TVL hingga miliaran dolar. Keberhasilan ini dimanfaatkan untuk meluncurkan tata kelola token mereka sendiri (seperti TGE ETHFI dan REZ) dengan valuasi premium.

Tingkat Keyakinan: HIGH

## 16 Historical Timeline

Kronologi terperinci evolusi proyek disajikan secara runtut berdasarkan tanggal terjadinya peristiwa beserta analisis hubungan sebab-akibatnya:

29 Juni 2021 — Pendirian EIGEN LABS, INC. — Sreeram Kannan meresmikan badan hukum di Seattle untuk meluncurkan riset formal restaking Ethereum.

19 April 2022 — Pendanaan Series A-1 — Mengamankan modal $14.480.000 untuk memperluas tim pengembang inti.

1 Agustus 2022 — Penutupan Putaran Pendanaan Seed — Polychain Capital memimpin penyuntikan dana $14.500.000 untuk membangun fondasi kontrak pintar restaking pertama.

29 Agustus 2022 — Pendirian Layr Labs, Inc. — Pendirian entitas hukum korporasi tambahan untuk mengelola pengembangan komersial.

28 Maret 2023 — Penutupan Putaran Pendanaan Series A — Menghimpun dana $50.000.000 dari Blockchain Capital untuk mempercepat perancangan AVS perdana.

7 April 2023 — Peluncuran Testnet Publik Perdana — Pengembang merilis lingkungan uji coba bagi validator untuk menyimulasikan restaking.

Juni 2023 — Pembukaan Jaringan Utama (Mainnet) Terbatas — Peluncuran bertahap dengan membatasi setoran LST stETH Lido guna mencegah penumpukan likuiditas berlebih.

5 Februari 2024 — Penghapusan Batasan Caps Deposit LST — Membuka akses bebas setoran LST yang memicu aliran masuk modal senilai $1.000.000.000 dalam waktu 24 jam.

22 Februari 2024 — Pengumuman Seri Pendanaan B — Andreessen Horowitz menyuntikkan modal tunggal sebesar $100.000.000 untuk mengamankan hak pengembangan komersial.

15 Maret 2024 — Perekaman Snapshot Airdrop Season 1 — Penguncian aktivitas restaking pada Block Ethereum #19437000 untuk penentuan kriteria distribusi token.

10 April 2024 — Peluncuran Mainnet Jaringan Keamanan Bersama — Peresmian integrasi resmi lapisan ketersediaan data EigenDA di mainnet Ethereum.

10 Mei 2024 — Pembukaan Klaim Stakedrop Season 1 — Pengguna dapat mulai mengklaim alokasi token EIGEN perdana mereka.

19 Mei 2024 — Pengungkapan Peran Penasihat Justin Drake — Peneliti EF memublikasikan kontrak penasihat berbayar bernilai jutaan dolar, memicu kontroversi etika di komunitas.

19 Juni 2024 — Pembukaan Klaim Season 1 Fase 2 — Pendistribusian sisa 10% alokasi token kepada alamat pengguna platform DeFi sekunder.

15 Agustus 2024 — Perekaman Snapshot Season 2 — Penguncian aktivitas "ETH-hours" pada Block Ethereum #20537000.

16 September 2024 — Pembukaan Klaim Stakedrop Season 2 — Distribusi token EIGEN Season 2 resmi dibuka untuk para kontributor ekosistem.

30 September 2024 — Pembukaan Transferabilitas Token EIGEN — Penonaktifan kondisi penguncian transfer sehingga EIGEN resmi diperdagangkan bebas di bursa.

5 Oktober 2024 — Eksploitasi Peretasan Jaringan — Protokol kehilangan dana senilai $5.700.000 akibat insiden keamanan eksternal terisolasi.

17 Desember 2024 — Pencapaian ATH EIGEN — Harga token spot EIGEN mencapai puncak rekor tertinggi sepanjang sejarah di level $5.65.

Akhir 2024 — Pengunduran Diri Penasihat EF — Justin Drake dan Dankrad Feist mengakhiri kerja sama penasihat formal demi memulihkan netralitas kredibel.

17 April 2025 — Pengaktifan Slashing di Mainnet — Pelaksanaan ELIP 002-004 menandai status fitur lengkap yang secara langsung memicu penyusutan TVL dari $15 miliar ke $7 miar.

17 Juni 2025 — Rebranding dan Peningkatan Pendanaan OTC — Pengumuman peluncuran platform EigenCloud yang didukung suntikan dana OTC token senilai $70.000.000 dari a16z.

8 Juli 2025 — Reorganisasi Tim Kerja — Eigen Labs memangkas 29 orang karyawan (25% dari total staf) demi merampingkan operasi pembangunan EigenCloud.

24 Oktober 2025 — Integrasi Google Cloud Faucet — Pengembang mulai dapat mengklaim EIGEN testnet pada Google Cloud Faucet untuk rantai uji Hoodi.

27 Maret 2026 — Rilis AgentKit Beta — Membuka akses publik bagi pengembang untuk membangun agen AI otonom yang berjalan di atas EigenCloud.

5 April 2026 — Pencapaian ATL EIGEN — Harga token EIGEN menyentuh rekor terendah sepanjang sejarah di level $0.1483 / $0.1484 akibat kejenuhan suplai unlocks bulanan.

## 17 Current Status

Keadaan proyek pada pertengahan tahun 2026 berada dalam fase pemulihan terarah yang berfokus pada transisi utilitas nyata (utility-driven recovery phase). Secara finansial, masa keemasan penumpukan TVL spekulatif berbasis farming poin gratis telah berakhir. Protokol mengalami penurunan TVL yang stabil dari puncaknya $20,09 miliar menjadi berkisar pada angka $4,3 miliar hingga $8,9 miliar. Penurunan ini mencerminkan pembersihan modal spekulatif berdaya ungkit tinggi (leverage wash-out) yang menyisakan para staker institusional jangka panjang yang siap menghadapi risiko slashing on-chain yang aktif berjalan sejak April 2025.

Meskipun harga token EIGEN tertekan di level ATL berkisar antara $0.23 hingga $0.60 akibat inflasi bulanan dari pembukaan kunci porsi modal ventura, secara fundamental teknologi dan ekosistem proyek berada pada posisi monopoli absolut. EigenCloud masih mempertahankan 93% hingga 94% pangsa pasar kategori restaking global. Peluncuran fungsionalitas komputasi terverifikasi EigenCompute dan kit pengembangan AI AgentKit telah mulai membuahkan hasil, di mana puluhan proyek DePIN dan agen AI terdesentralisasi mulai membayar biaya sewa keamanan riil menggunakan token EIGEN. Proyek tidak lagi bergantung pada narasi DeFi sirkular, melainkan bertransaksi langsung sebagai penyedia infrastruktur "AWS terverifikasi" untuk ekosistem AI terdesentralisasi.

## 18 Lessons Learned

Analisis mendalam terhadap siklus hidup EigenLayer/EigenCloud memberikan beberapa pelajaran berharga bagi pembangunan arsitektur Web3 masa depan:

Poin Spekulatif Menciptakan Kebisingan Data: Penggunaan sistem poin (points system) sangat efektif untuk mengumpulkan likuiditas instan (bootstrapping TVL), namun menciptakan permintaan palsu yang sangat rentan runtuh pasca-TGE. Ketika insentif poin hilang dan risiko sistemik (slashing) muncul, modal murni spekulatif akan langsung keluar mencari imbal hasil tanpa risiko di tempat lain. Proyek masa depan harus menyeimbangkan insentif dengan realitas risiko operasional sejak hari pertama.

Skandal Netralitas Menghancurkan Konsensus Sosial: Kasus penunjukan peneliti Ethereum Foundation sebagai advisor berbayar menunjukkan bahwa dalam ekosistem blockchain, netralitas sosial (social consensus) jauh lebih berharga daripada hubungan kedekatan politik. Upaya menyerap pengaruh figur otoritas menggunakan paket token bernilai jutaan dolar justru memicu krisis kepercayaan yang merusak kredibilitas proyek di mata pengadopsi awal.

Rebranding Harus Didukung Fleksibilitas Teknologi: Kemampuan tim Eigen Labs untuk mendeteksi kejenuhan sektor restaking murni dan langsung melakukan reorganisasi tim (memotong 25% staf operasional non-inti) demi fokus penuh pada infrastruktur awan verifikasi (EigenCloud) menunjukkan kelincahan eksekusi yang wajib ditiru. Transformasi produk dari sekadar jaminan ekonomi menjadi wadah komputasi berbasis TEE menyelamatkan proyek dari kepunahan narasi.

## 19 Knowledge Extraction Candidate (BAGIAN PALING PENTING)

Seksi ini menyusun representasi pengetahuan formal yang terstruktur secara semantik untuk digunakan oleh mesin penalaran kecerdasan buatan dalam mengekstrak fakta dan hubungan kausalitas dari proyek EigenLayer:

Kandidat Entitas Baru (New Entities):

Nama Entitas: EIGEN LABS, INC. (Badan usaha rekayasa teknologi pertama)

Nama Entitas: Layr Labs, Inc. (Entitas komersial induk)

Nama Entitas: EigenCloud (Nama baru platform awan hibrida terverifikasi)

Nama Entitas: EigenDA (Infrastruktur ketersediaan data tepercaya)

Nama Entitas: EigenCompute (Sistem eksekusi off-chain terenkripsi TEE)

Nama Entitas: AgentKit (Perangkat pengembangan kecerdasan buatan otonom)

Nama Entitas: Ion Protocol (Sistem peminjaman restaking berbasis konsensus)

Nama Entitas: Lagrange Labs (Penyedia bukti verifikasi ZK on-chain)

Kandidat Hubungan Ontologi (Ontology Mappings):

[Sreeram Kannan] -> founded -> [EIGEN LABS, INC.]

[EIGEN LABS, INC.] -> launched -> [EigenLayer]

[EigenLayer] -> rebranded_to -> [EigenCloud]

[EigenCloud] -> deploys_data_via -> [EigenDA]

[EigenCloud] -> runs_secure_compute_via -> [EigenCompute]

[AgentKit] -> executes_tasks_on -> [EigenCloud]

[a16z crypto] -> purchased_tokens_from -> [Eigen Foundation]

[Justin Drake] -> accepted_fees_from -> [Eigen Foundation]

Identifikasi Pola (Patterns Discovery):

Nama Pola: Slashing-Induced Capital Realignment

Rantai Sebab-Akibat: Aktivasi pemotongan jaminan (slashing) di mainnet Ethereum -> memicu kekhawatiran validator atas pemotongan modal tidak disengaja -> menginduksi penarikan modal spekulatif besar-besaran -> mendorong penyesuaian total likuiditas (TVL) turun hingga menyisakan pelaku kustodian institusional jangka panjang.

Nama Pola: Point-farming Circular Leverage Loop

Rantai Sebab-Akibat: Peluncuran program poin loyalitas linear -> memicu pembentukan protokol LRT sekunder -> melahirkan sistem leverage sirkular (deposito LST ganda untuk mencetak LRT baru) -> inflasi artifisial TVL -> memicu de-peg ekstrem jaminan sekunder saat likuiditas terkunci di antrean penarikan.

Nama Pola: Infrastructure-to-Enterprise Platform Pivot

Rantai Sebab-Akibat: Penurunan imbal hasil sektor keuangan terdesentralisasi -> harga token spot mengalami depresiasi tajam -> tim melakukan PHK massal pada tim non-teknis dan rebranding -> merancang primitif komputasi awan hibrida menggunakan Trusted Execution Environments (TEE) -> mengamankan suntikan modal baru untuk menyasar vertikal Decentralized AI dan DePIN.

## 20 Transferable Intelligence

Apabila sistem kecerdasan buatan di masa depan mengevaluasi proyek infrastruktur baru, beberapa aturan umum (rules) dan indikator khusus (heuristics) dari laporan ini harus dijadikan tolok ukur:

Aturan Umum Evaluasi Rasio Kapitalisasi Pasar Terhadap Jaminan (Circulating Market Cap to TVL Ratio):

Aturan: Untuk proyek infrastruktur jaminan ekonomi (seperti restaking/PoS), rasio sirkulasi pasar beredar terhadap total nilai terkunci (TVL) pada tahun pertama perdagangan token tidak boleh melebihi level 0.15. Jika rasio berada di atas batas ini, aset dikategorikan sebagai overvalued yang sangat rentan mengalami depresiasi harga akibat ketidakseimbangan pasokan setoran.

Aturan Deteksi Tekanan Penjualan Pasif (Passive Sell-Pressure Rule):

Aturan: Jaringan yang memiliki pembukaan kunci bulanan untuk investor dalam jumlah besar (melebihi 4% dari pasokan sirkulasi pasar per bulan) wajib menunjukkan rasio volume transaksi harian bursa (Average Daily Volume) minimal 15 kali lebih besar dari nilai nominal dolar token yang dilepaskan bulanan. Ketidakseimbangan ini akan mendorong devaluasi token secara konstan ke level ATL baru.

Indikator Khusus Kasus Fork-aware Staking (Forkability Premium Heuristic):

Aturan: Proyek yang menerapkan model token forking (seperti EIGEN) memiliki ketahanan koordinasi sosial yang lebih tinggi dibanding token utilitas murni. Premium valuasi harus diberikan pada sistem ini karena kemampuan penyelesaian sengketa kesalahan subjektif yang tidak dapat diselesaikan oleh logika smart contract on-chain biasa.

## 21 Open Questions

Beberapa misteri mendasar dan celah riset yang masih menyelimuti proyek ini meliputi:

Eksperimen Kegagalan Koordinasi Forking Intersubjektif: Bagaimana sistem forking EIGEN akan bertahan jika terjadi sengketa dengan faksi penyerang bernilai tinggi di mana pelaku kejahatan memegang lebih dari 40% pasokan token terdistribusi? Apakah koordinasi sosial tetap mampu menyaring pemegang jujur tanpa mengorbankan likuiditas token secara permanen?

Hambatan Biaya Adopsi Komputasi TEE: Apakah pengembang Web2 bersedia menanggung overhead biaya operasional hardware TEE komputasi awan tepercaya EigenCompute dibanding menggunakan infrastruktur komputasi konvensional tersentralisasi yang secara operasional jauh lebih efisien?

Keberlanjutan Finansial Model Imbal Hasil Dua Arah: Bagaimana protokol akan memelihara insentif staker di masa depan saat tingkat inflasi emisi tahunan sebesar 4% melambat, sedangkan arus pendapatan dari biaya operasional riil AVS masih belum mencukupi untuk menutup biaya operasional operator?

## 22 Evidence Level

Tingkat keyakinan atas kesimpulan-kesimpulan penting dalam laporan intelijen ini dinilai secara metodis di bawah ini:

Kesimpulan: Rebranding menjadi platform EigenCloud merupakan taktik untuk menyasar sektor AI terdesentralisasi pasca-koreksi sektor DeFi restaking.

Tingkat Keyakinan: HIGH

Alasan: Didukung rilis resmi AgentKit, deployment komputasi hibrida berbasis AMD SEV-SNP/Intel TDX, reorganisasi pemotongan 25% staf operasional, serta akuisisi pendanaan token OTC senilai $70 juta dari a16z khusus untuk akselerasi EigenCloud.

Kesimpulan: Peluncuran slashing di jaringan utama pada 17 April 2025 merupakan penyebab langsung dari guncangan penyusutan TVL protokol.

Tingkat Keyakinan: HIGH

Alasan: Kronologi data dari DefiLlama dan dokumen analisis Llama Risk menunjukkan pola penarikan modal deposan yang terjadi persis pasca-aktivasi ELIP 002-004 karena validator mulai menghindari ancaman pemotongan jaminan modal nyata.

Kesimpulan: Akumulasi pendanaan keseluruhan proyek bernilai tepat sebesar $241.000.000 secara kumulatif.

Tingkat Keyakinan: LOW

Alasan: Basis data terkemuka dunia memuat pencatatan yang saling bertolak belakang (Tracxn mencantumkan $241M, Rootdata mencantumkan $234.5M, Forge Global mencantumkan $164.48M, dan DefiLlama mencantumkan $220M), mengonfirmasi adanya wilayah transaksi privat ekuitas dan token yang tidak dipublikasikan secara seragam kepada publik.

## 23 Karya yang dikutip

PM Insights: EigenLayer Valuation and Overview — https://www.pminsights.com/companies/eigenlayer

Tracxn: EigenLayer Profile — https://tracxn.com/d/companies/eigenlayer/__UtNZZ1HaUloGhpV-hgFxJbwxCZZbrbTpRVOnfqvviqc

Forge Global: EigenLayer IPO and Financing History — https://forgeglobal.com/eigenlayer_ipo/

Forge Global: Buy And Sell EigenLayer Stock — https://forgeglobal.com/eigenlayer_stock/

Mint Ventures: Pioneer of Restaking Business Logic and Valuation — https://mint-ventures.medium.com/a-quick-look-at-the-pioneer-of-restaking-understanding-eigenlayers-business-logic-and-valuation-604f00a13e50

Chain Broker: EigenLayer Token Funding Allocation — https://chainbroker.io/projects/eigenlayer/

CoinGecko: EigenCloud (EIGEN) Statistics and Pricing — https://www.coingecko.com/en/coins/eigencloud

Coinmonks: All Things Eigen — https://medium.com/coinmonks/all-things-eigen-1615142b004b

Bitget Academy: EigenLayer Airdrop Guide and Price Prediction — https://web3.bitget.com/en/academy/eiegn-layer-airdrop-guide-qualify-claim-price-prediction

Animoca Brands Research: ZRO Tokenomics Analysis — https://research.animocabrands.com/post/cm4m6vb6u9atb07mo3xi1ku1q

Bitget Academy: Vertus (VERT) Airdrop Guide and Vesting — https://web3.bitget.com/en/academy/vertus-vert-airdrop-guide-listing-dates-price-prediction-how-to-qualify

Hugging Face Dataset: caia-0927 — https://huggingface.co/datasets/cyberco/caia-0927

Eigen Foundation FAQ: Season 2 Stakedrop Details — https://docs.eigenfoundation.org/faq-s-2/season-2

Dune Analytics: EigenLayer Airdrop Season 2 Dashboard — https://dune.com/p2p_org/eigenlayer-airdrops

Dune Analytics: Eigen Airdrop Season 1 & Season 2 Claim Dynamics — https://dune.com/yulia_is_here/eigen-token

Eigen Foundation FAQ: Season 1 Eligibility Criteria — https://docs.eigenfoundation.org/faq/season-1

Binance Square: Explore the EigenLayer Airdrops Campaign — https://www.binance.com/en/square/post/10129876250866

CoinMarketCap Academy: Eigen Foundation Announces EIGEN Airdrop — https://coinmarketcap.com/academy/article/eigen-foundation-announces-eigen-airdrop-for-ethereum-restaking-protocol-eigenlayer

Tokenomics.com: How EIGEN Captures Restaking Revenue — https://tokenomics.com/articles/eigenlayer-tokenomics-how-eigen-captures-restaking-revenue

Llama Risk Research: Current State of Symbiotic — https://www.llamarisk.com/research/current-state-of-symbiotic

BlockEden: EigenLayer $18B TVL, Vertical AVS Specialization and Restaking Evolution — https://blockeden.xyz/blog/2026/03/20/eigenlayer-18b-tvl-vertical-avs-specialization-restaking-evolution/

Ether.fi Governance: EigenLayer vs Symbiotic Risk Analysis — https://governance.ether.fi/t/eigenlayer-vs-symbiotic-risk-analysis/2246

Imperator Resources: EigenLayer vs Symbiotic Restaking War — https://www.imperator.co/resources/blog/eigenlayer-vs-symbiotic-restaking-war

Ether.fi Governance: Chaos Labs Karak Risk Analysis — https://governance.ether.fi/t/chaos-labs-karak-risk-analysis/2625

Bitget: What is Eigen (EIGEN) Core Founders — https://www.bitget.com/price/eigen/what-is

Zero Knowledge Podcast: Pairings and Quantum Leap — https://feeds.captivate.fm/zeroknowledge/

Llama Risk Research: AVS Risk Assessment EigenDA — https://llamarisk.com/research/avs-risk-assessment-eigenda

Parity Tech Github: Matrix Archiver Polkadot Timeline — https://paritytech.github.io/matrix-archiver/archive/_21wBOJlzaOULZOALhaRh_3Apolkadot.io/index.html

Sensors Portal: Cryptographic Multi-signatures and Blockchain Proceedings — https://sensorsportal.com/B2C/B2C_2025_Proceedings.pdf

EigenCloud Docs: EIGEN Token Whitepaper converted HTML — https://docs.eigencloud.xyz/html/EIGEN_Token_Whitepaper-converted-xodo.html

EigenCloud Assets: EIGEN Token Whitepaper PDF — https://docs.eigencloud.xyz/assets/files/EIGEN_Token_Whitepaper-0df8e17b7efa052fd2a22e1ade9c6f69.pdf

Bitkub Support: What is EigenLayer and EIGEN Token — https://support.bitkub.com/en/solutions/articles?id=151000219617

Figment Insights: EIGEN Tokenomics and Intersubjective Staking — https://www.figment.io/insights/eigen-tokenomics-eigenlayers-token-for-intersubjective-staking-and-forking/

Nethermind Blog: EigenLayer and EIGEN Token Explained — https://www.nethermind.io/blog/eigenlayer-and-eigen-token-explained

Blockworks: Eigen Labs Drops Whitepaper Debuting EIGEN Token — https://blockworks.com/news/eigen-labs-eigen-token

Business Stats: Crypto Market Statistics and Facts 2026 — https://businesstats.com/crypto-market-statistics-facts/

Simply Staking: Restaking and Liquid Restaking Tokens Overview — https://simplystaking.com/restaking-and-liquid-restaking-tokens-lrt

Fibo Crypto: DeFi total value locked and Liquid Staking 2026 — https://fibo-crypto.fr/en/blog/defi-decentralized-finance-guide/

Binance Research: Full Year 2025 & Themes for 2026 — https://public.bnbstatic.com/static/files/research/full-year-2025-and-themes-for-2026.pdf

ResearchGate: Ethereum Tokenomics Quantitative Longitudinal Study — https://www.researchgate.net/publication/399825353_Ethereum_Tokenomics_Insights_for_Web3_Entrepreneurs_a_Quantitative_Longitudinal_Study

Blockworks: EigenLayer Lines Up $50M in Bear Market Fundraise — https://blockworks.com/news/eigenlayer-lines-up-50m-in-bear-market-fundraise

Chain Broker: EigenCloud Funding History — https://chainbroker.io/projects/eigenlayer/

Mint Ventures: Pioneer of Restaking Business Logic and Valuation Strategy — https://mint-ventures.medium.com/a-quick-look-at-the-pioneer-of-restaking-understanding-eigenlayers-business-logic-and-valuation-604f00a13e50

The Block: a16z Crypto Invests $70 Million in Direct EIGEN Token Deal — https://www.theblock.co/post/358511/a16z-crypto-eigen-token-eigencloud

Forge Global: EigenLayer Stock Valuation details — https://forgeglobal.com/eigenlayer_ipo/

TechBible AI: Tech Startups That Became Unicorns in 2024 — https://www.techbible.ai/learn/tech-startups-unicorns-2024

Blockworks: a16z Injects $100M into EigenLayer Series B — https://blockworks.com/news/a16z-series-b-eigenlayer-investment

The Defiant: EigenLayer Reveals EigenCloud and $70 Million Investment from A16z — https://thedefiant.io/news/defi/eigenlayer-reveals-eigencloud-and-usd70-million-investment-from-a16z

ForkLog: Eigen Labs Reduces Workforce by 25% to Focus on EigenCloud — https://forklog.com/en/eigen-labs-reduces-workforce-by-25-to-focus-on-eigencloud/

The Block: a16z Crypto Invests $70 Million in Direct EigenLayer Token Deal to Back EigenCloud Developer Platform — https://www.theblock.co/post/358511/a16z-crypto-eigen-token-eigencloud

CryptoSlate: A16z Backs EigenLayer's EigenCloud Rollout with $70 Million EIGEN Investment — https://cryptoslate.com/a16z-backs-eigenlayers-eigencloud-rollout-with-70-million-eigen-investment/

Architect Partners: Weekly Crypto Financing Snapshot — https://architectpartners.com/wp-content/uploads/2025/06/06-25-25-Weekly-Crypto-Financing-Snapshot.pdf

Cryptorank News: A16z Backs EigenLayer's EigenCloud Rollout with $70 Million EIGEN Investment — https://cryptorank.io/news/feed/ef2da-a16z-backs-eigenlayers-eigencloud-rollout-with-70-million-eigen-investment

Blockworks: EigenCloud Launches Aiming to Bring Verifiability to Everything — https://blockworks.com/news/eigencloud-launch-a16z-eigenlayer

StartupIntros: Lagrange Labs ZK Prover Network on EigenLayer — https://startupintros.com/orgs/lagrange-labs

Acquire.fi: What is a Seed Round and How to Prepare — https://www.acquire.fi/blog/what-is-a-seed-round-and-how-to-prepare-for-it

VCBacked: Blockchain Capital Directory — https://www.vcbacked.co/directory/investors/blockchain-capital

Forge Global: Buy And Sell Private EigenLayer Stock — https://forgeglobal.com/eigenlayer_stock/

Rootdata: EigenLayer Project Detail and Event Calendar — https://www.rootdata.com/projects/detail/EigenLayer?k=Mjk4MA%3D%3D

CCN: EigenLayer (EIGEN) Price Prediction and CCN Index — https://www.ccn.com/analysis/crypto/eigenlayer-eigen-price-prediction/

DefiLlama: Income Statement for EigenCloud — https://defillama.com/protocol/eigencloud

DefiLlama: Puffer Stake Information and TVL — https://defillama.com/protocol/puffer-stake

DefiLlama: Zircuit Staking Methodology and Income Statement — https://defillama.com/protocol/zircuit-staking

DefiLlama: Swell Liquid Restaking Income Statement — https://defillama.com/protocol/swell-liquid-restaking

DefiLlama: Ether.fi TVL and SSV/EigenLayer Staking Rewards — https://defillama.com/protocol/ether.fi

The Defiant: EigenLayer Activates Mainnet Slashing on April 17 — https://thedefiant.io/news/blockchains/eigenlayer-activates-mainnet-slashing-on-april-17-implementing-elips-002-004-ecb683e0

Medium: EigenLayer's $15B to $7B Crash Nobody Saw Coming — https://medium.com/@pycheng9/eigenlayer-the-15b-to-7b-crash-nobody-saw-coming-d8e73f7b3169

EigenCloud Blog: Intro to Slashing on EigenLayer (AVS Edition) — https://blog.eigencloud.xyz/intro-to-slashing-on-eigenlayer-avs-edition/

TradingView News: Eigenlayer (EIGEN) Mainnet Slashing 17 Apr 2025 — https://www.tradingview.com/news/coinmarketcal:9c9a473d9094b:0-eigenlayer-eigen-mainnet-slashing-17-apr-2025/

EigenCloud Blog: Slashing on Mainnet is Coming Soon - What You Need to Know — https://blog.eigencloud.xyz/slashing-on-mainnet-is-coming-soon-what-you-need-to-know/

EigenCloud Blog: Intro to Slashing on EigenLayer (Stakers Edition) — https://blog.eigencloud.xyz/intro-to-slashing-on-eigenlayer-stakers-edition/

Eigen Foundation: EIGEN Token Stakedrop Details and Allocations — https://blog.eigenfoundation.org/announcement/

Linea Build: Linea Tokenomics and Consensys Treasury — https://linea.build/blog/linea-tokenomics

Unchained Crypto: 5 Reasons E-Beggars Are Not Happy with EigenLayer's Airdrop — https://unchainedcrypto.com/5-reasons-e-beggars-are-not-happy-with-eigenlayers-airdrop/

Kraken Assets: Crypto Asset Risk Disclosure for EigenLayer (EIGEN) — https://assets-cms.kraken.com/files/51n36hrp/facade/7593ffbfd55f61af1555ea8e738a514369131fd4.pdf

Binance Square: The Lineup - A Concentrated Wave of Supply Unlock — https://www.binance.com/en/square/post/31578053739066

Acquire.fi: What is Linea Crypto and Token Allocations — https://www.acquire.fi/blog/what-is-linea-crypto

Tracxn: Aligned Layer Competitors and Funding — https://tracxn.com/d/companies/aligned-layer/__b-KH7l-KsvcDuHmYme81lSMRGySIQwm9WW9KV219UXo

StartupIntros: Espresso Systems Key People and Funding — https://startupintros.com/orgs/espresso-systems

Hexens: Cybersecurity Team Profile and Audits — https://hexens.io/team

Envelop: ETHFI Smart Contract Audit Report — https://index.envelop.is/reports/ethfi_audit.html

Eigen Foundation Protocol Governance: Technical Architecture — https://docs.eigenfoundation.org/protocol-governance/technical-architecture

Medium: Restaking 101 - A Primer on EigenLayer Problems and Team — https://medium.com/@benhwx/restaking-101-a-primer-on-eigenlayer-ad9bc69875bc

BitcoinWorld: Bithumb to Rename EigenLayer (EIGEN) to EigenCloud — https://cryptorank.io/news/feed/4d98e-bithumb-eigenlayer-rename-eigencloud

Upay Blog: Liquid Restaking - More Yield, More Risk — https://blog.upay.com/crypto-terminology/liquid-restaking/

Cryptorank News: Category EigenLayer and Token Rebranding — https://cryptorank.io/news/tag/eigenlayer

Rootdata: EigenCloud (formerly EigenLayer) Profile — https://www.rootdata.com/projects/detail/EigenLayer?k=Mjk4MA%3D%3D

BlockEden: EigenCloud - Rebuilding Web3's Trust Foundation Through Verifiable Cloud Infrastructure — https://blockeden.xyz/blog/2025/12/03/eigencloud-rebuilding-web3-s-trust-foundation-through-verifiable-cloud-infrastructure/

KuCoin Blog: a16z Crypto Fund 5 Betting on EigenCloud — https://www.kucoin.com/blog/a16z-crypto-fund-5-what-its-means-for-eigencloud-stablecoins-and-asset-tokenization

ForkLog: Eigen Labs Reduces Workforce by 25% to Focus on EigenCloud — https://forklog.com/en/eigen-labs-reduces-workforce-by-25-to-focus-on-eigencloud/

Binance Square: Eigen Labs Restructures Workforce to Focus on EigenCloud Growth — https://www.binance.com/en/square/post/26703809425522

Blockworks: Eigen Labs Lays Off 25% of Employees, Turns Focus to EigenCloud — https://blockworks.com/news/eigen-layoffs-25-eigencloud

Unchained: Eigen Labs Cuts 25% of Workforce to Prioritize EigenCloud Report — https://unchainedcrypto.com/eigen-labs-cuts-25-of-workforce-to-prioritize-eigencloud-report/

Rootdata News: Web3 Winter Mass Exodus - Layoffs and Closures — https://www.rootdata.com/news/564115

KuCoin News: Web3 Winter Layoffs, Closures, Transitions, and Acquisitions — https://www.kucoin.com/news/flash/web3-winter-layoffs-closures-transitions-and-acquisitions

Spark Money: Liquid Staking Platform Comparison and EigenLayer Staking — https://www.spark.money/tools/liquid-staking-platform-comparison

Nethermind Blog: Optimizing Restaking Yields - A Hybrid Quantitative Qualitative Model — https://www.nethermind.io/blog/optimizing-restaking-yields-a-hybrid-quantitative-qualitative-model

Galaxy Digital Insights: The Risks and Rewards of Restaking — https://www.galaxy.com/insights/research/the-risks-and-rewards-of-restaking

KuCoin: Eigen (EIGEN) Live Price Data and Utility — https://www.kucoin.com/price/EIGEN

Tokenomics.com: How EigenLayer Captures Restaking Revenue and Allocation — https://tokenomics.com/articles/eigenlayer-tokenomics-how-eigen-captures-restaking-revenue

Binance Square: EIGEN Token Circulating Supply Concerns and Unlock — https://www.binance.com/en/square/post/14316948776633

OKX Learn: EIGEN Unlocking Dilution and Market Impacts — https://www.okx.com/en-sg/learn/eigen-unlocking-dilution-market-impacts

TokenInsight Research: EigenLayer EIGEN Token Analysis, Allocation and Vesting — https://tokeninsight.com/en/research/analysts-pick/eigenlayer-s-eigen-token-analysis

The Block: EigenLayer Foundation Formed and Introduces Native Token — https://www.theblock.co/post/291383/eigenlayer-foundation-formed-introduces-native-token-with-multi-season-stakedrop

The Defiant: Community Erupts as Key Players From EF Become Advisors to EigenLayer — https://thedefiant.io/news/blockchains/community-erupts-as-key-players-from-ethereum-foundation-become-advisors-to-eigenlayer

The Block: EF Researcher Justin Drake Discloses Advisor Role at Eigen Foundation — https://www.theblock.co/post/295314/ethereum-foundation-researcher-eigenlayer-incentive

Bitget News: EF Faces Trust Crisis Over Advisor Role — https://www.binance.com/en/square/post/26703809425522

Investing.com: Ethereum Researcher's Side Hustle Sparks Conflict Concerns — https://ng.investing.com/news/cryptocurrency-news/ethereum-researchers-side-hustle-sparks-conflict-concerns-1362902

BlockEden: EF 70k ETH Staking and Advisory Resignation Timeline — https://blockeden.xyz/blog/2026/04/20/ethereum-foundation-70k-eth-staking-treasury-governance-neutrality/

Binance Square: Ethereum Foundation Considering Formal Conflict of Interest Policy — https://www.binance.com/en/square/post/8566883181577

Kiln Blog: Major Contributors and Ecosystem Overview — https://www.kiln.fi/blog

Sacra: EigenCloud Platform, Primitives and Valuation — https://sacra.com/c/eigencloud/

Aethir Blog: Powering Enterprise Compute Services with the EigenLayer ATH Vault — https://aethir.com/blog-posts/aethirs-2025-wrap-up-decentralized-gpu-cloud-milestones

Cryptorank News: EIGEN Goes Live on Google Cloud's Web3 Faucet — https://cryptorank.io/news/feed/fdd00-eigen-goes-live-on-google-clouds-web3-faucet-to-boost-developer-testing

BlockEden: EigenCloud Rebuilding Web3's Trust Foundation Deep Dive — https://blockeden.xyz/blog/2025/12/03/eigencloud-rebuilding-web3-s-trust-foundation-through-verifiable-cloud-infrastructure/

Arxiv Paper: Restaking Protocol Taxonomy and Regressions — https://arxiv.org/html/2604.03274v1

SlideShare: CoinGecko Q1 2024 Crypto Industry Report — https://www.slideshare.net/slideshow/2024-q1-crypto-industry-report-coingecko/267288839

SlideShare: CoinGecko Q2 2024 Crypto Industry Report — https://www.slideshare.net/slideshow/2024-q2-crypto-industry-report-coingecko-ee7d/270271673

Gate.com: Q1 2024 Liquid Restaking Token (LRT) Market Overview — https://www.gate.com/learn/articles/q1-2024-lrt-market-overview/2094

Karya yang dikutip

1. What is Eigen (EIGEN)| How To Get & Use Eigen - Bitget, https://www.bitget.com/price/eigen/what-is 2. Restaking 101: A Primer on EigenLayer | by Ben Wee | Medium, https://medium.com/@benhwx/restaking-101-a-primer-on-eigenlayer-ad9bc69875bc 3. EigenCloud Project Introduction, Team, Financing and News_RootData | RootData, https://www.rootdata.com/projects/detail/EigenLayer?k=Mjk4MA%3D%3D 4. EigenCloud: Rebuilding Web3's Trust Foundation Through Verifiable Cloud Infrastructure, https://blockeden.xyz/blog/2025/12/03/eigencloud-rebuilding-web3-s-trust-foundation-through-verifiable-cloud-infrastructure/ 5. A Quick Look at the Pioneer of Restaking: Understanding EigenLayer's Business Logic and Valuation Analysis - Mint Ventures, https://mint-ventures.medium.com/a-quick-look-at-the-pioneer-of-restaking-understanding-eigenlayers-business-logic-and-valuation-604f00a13e50 6. Current State of Symbiotic | LlamaRisk Research, https://www.llamarisk.com/research/current-state-of-symbiotic 7. What is Liquid Restaking? Definition and Meaning - UPay Blog, https://blog.upay.com/crypto-terminology/liquid-restaking/ 8. EigenLayer vs Symbiotic Risk Analysis - Protocol & Proposals - ether.fi, https://governance.ether.fi/t/eigenlayer-vs-symbiotic-risk-analysis/2246 9. Eigenlayer (EIGEN) - 2024_08_08 - UK Crypto Asset Statement - Kraken, https://assets-cms.kraken.com/files/51n36hrp/facade/7593ffbfd55f61af1555ea8e738a514369131fd4.pdf 10. Restaking: Costs & Benefits - Galaxy, https://www.galaxy.com/insights/research/the-risks-and-rewards-of-restaking 11. EigenLayer: The Ethereum Protocol Redefining Blockchain Restaking | Bitkub Support, https://support.bitkub.com/en/solutions/articles?id=151000219617 12. EigenLayer Activates Mainnet Slashing on April 17, Implementing ELIPs 002–004 and Achieving Feature-Complete Status | The Defiant, https://thedefiant.io/news/blockchains/eigenlayer-activates-mainnet-slashing-on-april-17-implementing-elips-002-004-ecb683e0 13. EigenLayer: The $15B-to-$7B Crash Nobody Saw Coming | by Cynthia Cheng | Medium, https://medium.com/@pycheng9/eigenlayer-the-15b-to-7b-crash-nobody-saw-coming-d8e73f7b3169 14. Liquid Staking Platforms Compared: Lido, Rocket Pool & More - Spark, https://www.spark.money/tools/liquid-staking-platform-comparison 15. Eigen Labs Reduces Workforce by 25% to Focus on EigenCloud - ForkLog, https://forklog.com/en/eigen-labs-reduces-workforce-by-25-to-focus-on-eigencloud/ 16. Eigen Labs restructures workforce to focus on EigenCloud growth | Cryptopolitan on Binance Square, https://www.binance.com/en/square/post/26703809425522 17. Eigen Labs lays off 25% of employees, turns focus to EigenCloud - Blockworks, https://blockworks.com/news/eigen-layoffs-25-eigencloud 18. EigenLayer Crosses $18B in Restaked ETH — How Vertical AVS Specialization Is Reshaping Ethereum Security - BlockEden.xyz, https://blockeden.xyz/blog/2026/03/20/eigenlayer-18b-tvl-vertical-avs-specialization-restaking-evolution/ 19. A16z backs EigenLayer's EigenCloud rollout with $70 million EIGEN investment, https://cryptoslate.com/a16z-backs-eigenlayers-eigencloud-rollout-with-70-million-eigen-investment/ 20. EigenCloud launches aiming to bring verifiability to everything - Blockworks, https://blockworks.com/news/eigencloud-launch-a16z-eigenlayer 21. EigenCloud analysis - Sacra, https://sacra.com/c/eigencloud/ 22. EigenLayer - 2026 Company Profile, Team, Funding & Competitors - Tracxn, https://tracxn.com/d/companies/eigenlayer/__UtNZZ1HaUloGhpV-hgFxJbwxCZZbrbTpRVOnfqvviqc 23. EigenLayer Lines Up $50M In Bear Market Fundraise - Blockworks, https://blockworks.com/news/eigenlayer-lines-up-50m-in-bear-market-fundraise 24. EIGEN: The Universal Intersubjective Work Token - EigenCloud, https://docs.eigencloud.xyz/assets/files/EIGEN_Token_Whitepaper-0df8e17b7efa052fd2a22e1ade9c6f69.pdf 25. EigenLayer and EIGEN Token Explained - Nethermind, https://www.nethermind.io/blog/eigenlayer-and-eigen-token-explained 26. a16z crypto invests $70 million in direct EigenLayer token deal to back EigenCloud developer platform rollout | The Block, https://www.theblock.co/post/358511/a16z-crypto-eigen-token-eigencloud 27. Restaking Tokens | Liquid Staking Guide | What is Restaking? - Simply Staking, https://simplystaking.com/restaking-and-liquid-restaking-tokens-lrt 28. EigenLayer Valuation - PM Insights, https://www.pminsights.com/companies/eigenlayer 29. AVS Risk Assessment: EigenDA | LlamaRisk Research, https://llamarisk.com/research/avs-risk-assessment-eigenda 30. Community Erupts as Key Players From Ethereum Foundation Become Advisors to Eigenlayer - "The Defiant", https://thedefiant.io/news/blockchains/community-erupts-as-key-players-from-ethereum-foundation-become-advisors-to-eigenlayer 31. Ethereum Foundation researcher Justin Drake discloses advisor role at Eigen Foundation, https://www.theblock.co/post/295314/ethereum-foundation-researcher-eigenlayer-incentive 32. Ethereum Foundation Considers Formal Conflict of Interest Policy After Community Backlash | 奔跑财经-FinaceRun on Binance Square, https://www.binance.com/en/square/post/8566883181577 33. The Ethereum Foundation Just Became a Staker. Can It Still Be a Neutral Steward?, https://blockeden.xyz/blog/2026/04/20/ethereum-foundation-70k-eth-staking-treasury-governance-neutrality/ 34. EigenCloud (prev. EigenLayer) Price Chart (EIGEN) - CoinGecko, https://www.coingecko.com/en/coins/eigencloud 35. 239bbeff-15a2-4df0-aaa2-dacffd673b50 - EigenCloud, https://docs.eigencloud.xyz/html/EIGEN_Token_Whitepaper-converted-xodo.html 36. EIGEN Tokenomics: EigenLayer's Token for Intersubjective Staking and Forking - Figment.io, https://www.figment.io/insights/eigen-tokenomics-eigenlayers-token-for-intersubjective-staking-and-forking/ 37. Eigen Price - KuCoin, https://www.kucoin.com/price/EIGEN 38. Eigen Labs drops white paper debuting EIGEN token - Blockworks, https://blockworks.com/news/eigen-labs-eigen-token 39. Intro to Slashing on EigenLayer: AVS Edition - EigenCloud Blog, https://blog.eigencloud.xyz/intro-to-slashing-on-eigenlayer-avs-edition/ 40. Intro to Slashing on EigenLayer: Stakers' Edition - EigenCloud Blog, https://blog.eigencloud.xyz/intro-to-slashing-on-eigenlayer-stakers-edition/ 41. EIGEN goes live on Google Cloud's Web3 faucet to boost developer testing - CryptoRank, https://cryptorank.io/news/feed/fdd00-eigen-goes-live-on-google-clouds-web3-faucet-to-boost-developer-testing 42. A16z injects $100M into EigenLayer - Blockworks, https://blockworks.com/news/a16z-series-b-eigenlayer-investment 43. EigenLayer IPO: Investment Opportunities & Pre-IPO Valuations - Forge Global, https://forgeglobal.com/eigenlayer_ipo/ 44. Invest and Sell EigenLayer Stock - Forge Global, https://forgeglobal.com/eigenlayer_stock/ 45. EigenLayer (None) Price, Investors & Funding, Charts, Market Cap | Chain Broker, https://chainbroker.io/projects/eigenlayer/ 46. EigenCloud TVL, Fees & Revenue - DefiLlama, https://defillama.com/protocol/eigencloud 47. Tech Startups That Became Unicorns in 2024 - Techbible, https://www.techbible.ai/learn/tech-startups-unicorns-2024 48. EigenLayer Reveals EigenCloud and $70 Million Investment from A16z - The Defiant, https://thedefiant.io/news/defi/eigenlayer-reveals-eigencloud-and-usd70-million-investment-from-a16z 49. 06-25-25 Weekly Crypto Financing Snapshot - Architect Partners, https://architectpartners.com/wp-content/uploads/2025/06/06-25-25-Weekly-Crypto-Financing-Snapshot.pdf 50. Introducing the Eigen Foundation, EIGEN token and Season 1 stakedrop, https://blog.eigenfoundation.org/announcement/ 51. 5 Reasons E-Beggars Are Not Happy With EigenLayer's Airdrop - Unchained Crypto, https://unchainedcrypto.com/5-reasons-e-beggars-are-not-happy-with-eigenlayers-airdrop/ 52. Eligibility: Season 1 - Eigen Foundation, https://docs.eigenfoundation.org/faq/season-1 53. EigenLayer Tokenomics: How EIGEN Captures Restaking Revenue, https://tokenomics.com/articles/eigenlayer-tokenomics-how-eigen-captures-restaking-revenue 54. EigenLayer vs Symbiotic: Dive into The Restaking War - Imperator.co, https://www.imperator.co/resources/blog/eigenlayer-vs-symbiotic-restaking-war 55. [Chaos Labs] - Karak Risk Analysis - Protocol & Proposals - ether.fi, https://governance.ether.fi/t/chaos-labs-karak-risk-analysis/2625 56. a16z Crypto Fund 5: What Its $2.2B Bet Means for EigenCloud, Stablecoins, and Asset Tokenization - KuCoin, https://www.kucoin.com/blog/a16z-crypto-fund-5-what-its-means-for-eigencloud-stablecoins-and-asset-tokenization 57. EIGEN Unlocking Dilution: Key Insights and Market Impacts You Need to Know - OKX, https://www.okx.com/en-sg/learn/eigen-unlocking-dilution-market-impacts 58. Eigenlayer (EIGEN) - Mainnet Slashing - 17 Apr 2025 — TradingView News, https://www.tradingview.com/news/coinmarketcal:9c9a473d9094b:0-eigenlayer-eigen-mainnet-slashing-17-apr-2025/ 59. Slashing on Mainnet is Coming Soon - What You Need to Know - EigenCloud Blog, https://blog.eigencloud.xyz/slashing-on-mainnet-is-coming-soon-what-you-need-to-know/ 60. EigenLayer's EIGEN Token Analysis - TokenInsight, https://tokeninsight.com/en/research/analysts-pick/eigenlayer-s-eigen-token-analysis 61. #EIGENonBinance The total supply of the $EIGEN token, | Monstano on Binance Square, https://www.binance.com/en/square/post/14316948776633 62. EigenLayer reveals plan for token airdrop with 15% allocation to ecosystem participants, https://www.theblock.co/post/291383/eigenlayer-foundation-formed-introduces-native-token-with-multi-season-stakedrop 63. All Things $EIGEN. Hey folks, so the much anticipated… | by MWC | Coinmonks - Medium, https://medium.com/coinmonks/all-things-eigen-1615142b004b 64. A Trader's Guide to Next Week's Major Token Unlocks | Alidkm on Binance Square, https://www.binance.com/en/square/post/31578053739066 65. EigenLayer 1.29MM Token Unlock: $EIGEN Airdrop Guide, Price Prediction, and Clai, https://web3.bitget.com/en/academy/eiegn-layer-airdrop-guide-qualify-claim-price-prediction 66. Eigen Foundation Announces EIGEN Airdrop for Ethereum Restaking Protocol EigenLayer, https://coinmarketcap.com/academy/article/eigen-foundation-announces-eigen-airdrop-for-ethereum-restaking-protocol-eigenlayer 67. Explore the EigenLayer Airdrops - Binance, https://www.binance.com/en/square/post/10129876250866 68. Eligibility: Season 2 - Eigen Foundation, https://docs.eigenfoundation.org/faq-s-2/season-2 69. EigenLayer Airdrop [Season 2] | Dune, https://dune.com/p2p_org/eigenlayer-airdrops 70. Eigen Labs Cuts 25% of Workforce to Prioritize EigenCloud: Report - Unchained Podcast, https://unchainedcrypto.com/eigen-labs-cuts-25-of-workforce-to-prioritize-eigencloud-report/ 71. EigenLayer Price Prediction 2025: Recovery From All-Time Low Likely, https://www.ccn.com/analysis/crypto/eigenlayer-eigen-price-prediction/ 72. DeFi: What Is Decentralized Finance? Complete Guide 2026 | Fibo, https://fibo-crypto.fr/en/blog/defi-decentralized-finance-guide/ 73. Aethir's 2025 Wrap-Up: Decentralized GPU Cloud Milestones, https://aethir.com/blog-posts/aethirs-2025-wrap-up-decentralized-gpu-cloud-milestones 74. Ethereum Researcher Earns Millions in Advisory Fees for Working on EigenLayer, Ethereum Foundation Faces Trust Crisis | Bitget News, https://www.bitget.com/news/detail/12560604012518 75. Full-Year 2025 & Themes for 2026, https://public.bnbstatic.com/static/files/research/full-year-2025-and-themes-for-2026.pdf 76. ether.fi TVL, Fees, Revenue & Volume - DefiLlama, https://defillama.com/protocol/ether.fi 77. Ether.fi ($ETHFI) Web3 Project Audit Report - Envelop, https://index.envelop.is/reports/ethfi_audit.html 78. Optimizing Restaking Yields: A Hybrid Quantitative & Qualitative Model | Nethermind, https://www.nethermind.io/blog/optimizing-restaking-yields-a-hybrid-quantitative-qualitative-model 79. Liquid Restaking Tokens (LRT) Q1 2024 Market Overview | Gate Learn, https://www.gate.com/learn/articles/q1-2024-lrt-market-overview/2094 80. Lagrange Labs: Funding, Team & Investors - Startup Intros, https://startupintros.com/orgs/lagrange-labs
