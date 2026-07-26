Laporan Intelijen Celestia: Dekonstruksi Komprehensif Arsitektur Modular, Dinamika Tokenomik, dan Evolusi Pasar (2019-2026)

## 1 Executive Summary

Celestia memelopori pergeseran paradigma arsitektur blockchain melalui pemisahan fungsi konsensus dan ketersediaan data (Data Availability - DA) dari fungsionalitas eksekusi transaksi. Konsep ini memungkinkan skalabilitas tanpa membebani simpul jaringan (nodes) dengan pertumbuhan ukuran data state. Sejak didirikan dengan nama LazyLedger pada tahun 2019 dan melakukan rebranding menjadi Celestia pada 15 Juni 2021, tim pendiri berhasil menerjemahkan riset teoritis akademis tentang Data Availability Sampling (DAS) menjadi sistem produksi berskala besar. Peluncuran Mainnet Beta pada 31 Oktober 2023 menandai era komersialisasi pertama solusi ketersediaan data alternatif (Alt-DA) yang menawarkan efisiensi biaya hingga 99% dibandingkan memposting data langsung ke basis Ethereum L1.

Perjalanan ekonomi token asli Celestia, TIA, mencerminkan siklus reflexivity ekstrem. TIA mengalami reli spekulatif masif dari harga debut bursa di kisaran $2,00 hingga mencapai All-Time High (ATH) historis di angka $20,85 pada 10 Februari 2024, didorong oleh eforia kampanye airdrop lintas ekosistem. Namun, pembukaan kunci (unlock) token kontributor awal serta aksi eksploitasi arbitrase staking rewards oleh investor institusional memicu jatuhnya harga bursa hingga 97% ke tingkat All-Time Low (ATL) di kisaran $0,2792 pada 6 Juni 2026. Menanggapi krisis depresiasi nilai tersebut, jaringan Celestia merancang reformasi tokenomik melalui serangkaian peningkatan konsensus radikal, khususnya Lotus (v4) dan Matcha (v6), yang berhasil memotong tingkat inflasi dari 8,00% menjadi ~2,50% sekaligus menghentikan eksploitasi likuiditas. Di pertengahan tahun 2026, Celestia mematangkan posisinya melalui visi "Every Market Onchain" (Vision 2.0) dengan meluncurkan protokol Fibre Blockspace berkemampuan 1 Terabit per detik (1 Tb/s) untuk mendukung operasional pasar finansial dan agen kecerdasan buatan (AI) secara berdaulat.

## 2 Industry Background

Sebelum lahirnya arsitektur modular Celestia, lanskap industri kripto didominasi oleh blockchain monolitik generasi pertama dan kedua seperti Bitcoin dan Ethereum. Pada sistem monolitik, setiap validator dan full node diwajibkan untuk menjalankan empat fungsi fungsionalitas inti secara simultan: mengeksekusi komputasi transaksi, menyepakati urutan transaksi (konsensus), menjamin ketersediaan data (data availability), dan menyelesaikan sengketa status (settlement). Desain ini melahirkan Trilema Blockchain yang parah, di mana peningkatan desentralisasi secara langsung membatasi throughput jaringan. Ketika throughput transaksi dinaikkan, ukuran blok membengkak secara eksponensial, memicu penumpukan data state (state bloat) yang memaksa operator node menggunakan perangkat keras berspesifikasi tinggi. Akibatnya, desentralisasi runtuh karena hanya sedikit operator profesional yang mampu mendanai operasional node penuh.

Sebagai tanggapan atas skalabilitas Ethereum L1 yang tersendat, industri melahirkan narasi penskalaan off-chain melalui Layer 2 (L2) rollups, baik berbasis Optimistic maupun Zero-Knowledge. Rollup mengeksekusi komputasi transaksi di luar rantai utama, kemudian mengirimkan kompresi data transaksi kembali ke Ethereum L1 untuk konsensus dan jaminan ketersediaan data. Meskipun strategi ini berhasil menurunkan biaya transaksi bagi pengguna akhir di tingkat eksekusi, rollup membentur pembatas ekonomi baru yang dikenal sebagai hambatan biaya ketersediaan data (Data Availability bottleneck). Memposting calling data ke Ethereum L1 sangat mahal dan menyerap hingga lebih dari 90% total pengeluaran operasional rollup sebelum implementasi EIP-4844. Kondisi ini membatasi skalabilitas rollup untuk aplikasi berkinerja tinggi seperti permainan on-chain, pembayaran mikro, dan platform buku order limit terpusat (CLOB).

Celestia diluncurkan tepat pada titik krisis infrastruktur ini. Konsep ketersediaan data modular yang diusulkan Celestia menyajikan jalur alternatif: memutus ketergantungan rollup pada Ethereum L1 untuk pengunggahan data transaksi. Dengan mendirikan rantai berdaulat khusus yang hanya bertugas mengurutkan data tanpa menjalankan komputasi kontrak pintar, Celestia menyajikan ruang blok melimpah dengan biaya sangat murah. Solusi ini sangat dinanti industri karena memberikan kelonggaran finansial bagi rollup, yang pada gilirannya mendorong ledakan lahirnya penyedia infrastruktur Rollup-as-a-Service (RaaS) seperti Conduit, AltLayer, dan Caldera.

## 3 Project Origin

Akar historis Celestia bermula pada tahun 2018 ketika salah satu pendirinya, Mustafa Al-Bassam, memformulasikan konsep matematis Data Availability Sampling (DAS) selama menempuh riset pascasarjana. Al-Bassam kemudian menerbitkan dokumen penelitian akademis seminal berjudul "LazyLedger" pada tahun 2019. Dokumen tersebut menggambarkan sebuah rantai konsensus minimalis yang tidak mengeksekusi transaksi (lazy execution), melainkan hanya menjamin bahwa data transaksi tersedia untuk diunduh dan diverifikasi oleh siapa saja di luar rantai utama. Desain ini menjadi antitesis radikal bagi komputer global monolitik.

Nama Pendiri Inti: Mustafa Al-Bassam

Latar Belakang: Memiliki gelar PhD dalam bidang Blockchain Scaling dari University College London (UCL), salah satu pendiri Chainspace yang diakuisisi oleh Facebook pada tahun 2019. Berperan sebagai Chief Executive Officer (CEO) Celestia Labs.

Nama Pendiri Inti: John Adler

Latar Belakang: Mantan peneliti terapan di ConsenSys dan perancang spesifikasi teknis pertama sistem Optimistic Rollup di ekosistem Ethereum. Berperan sebagai Chief Research Officer (CRO).

Nama Pendiri Inti: Ismail Khoffi

Latar Belakang: Insinyur perangkat lunak berpengalaman yang sebelumnya menjabat sebagai pengembang senior di Tendermint dan Interchain Foundation. Berperan sebagai Chief Technology Officer (CTO).

Eksekutif Kunci Lainnya: Nick White

Latar Belakang: Co-founder Harmony Protocol dan menjabat sebagai Chief Operating Officer (COO) Celestia Labs untuk mengarahkan strategi ekspansi pasar.

Entitas Hukum Resmi: United Kingdom Entity

Nama Registrasi: CIN: 12391157

Tanggal Inkorporasi: 7 Januari 2020

Status Hukum: Aktif, berkedudukan di Inggris Raya dengan jumlah karyawan 28 orang per 30 Maret 2024.

Entitas Hukum Resmi: Vaduz Entity

Nama Registrasi: Strange Loop Labs AG

Lokasi: Vaduz, Liechtenstein, didirikan untuk mengelola operasi yayasan dan struktur tokenomik bursa.

Dewan Penasihat Strategis: Zaki Manian, Ethan Buchman

Peran: Tokoh pelopor ekosistem Cosmos yang memberikan panduan strategis dalam adopsi Cosmos SDK dan arsitektur IBC pada awal perancangan protokol Celestia.

Pada 15 Juni 2021, tim secara resmi melakukan rebranding dari nama LazyLedger menjadi Celestia untuk membangun identitas visual yang lebih profesional menjelang peluncuran uji coba publik pertama mereka.

## 4 Innovation Analysis

Celestia memperkenalkan serangkaian inovasi fundamental yang mengubah lanskap desain arsitektur blockchain global:

Data Availability Sampling (DAS): Inovasi ini mematahkan batas linier skalabilitas blockchain tradisional. Menggunakan skema Two-Dimensional Reed-Solomon Erasure Coding, Celestia membagi data blok menjadi matriks berdimensi dua dan menyisipkan data redundansi (erasure code). Keberadaan erasure code memastikan bahwa jika produsen blok mencoba menyembunyikan meskipun hanya satu byte data, mereka secara matematis harus menyembunyikan lebih dari 50.00% bagian dari keseluruhan blok. Hal ini memungkinkan light node di jaringan untuk melakukan pengambilan sampel acak (sampling) secara acak terhadap potongan kecil blok tersebut. Hanya dengan mengunduh sebagian kecil data (beberapa kilobyte), light node dapat membuktikan dengan akurasi statistik di atas 99.99% bahwa seluruh data blok telah dipublikasikan ke jaringan.

Namespaced Merkle Trees (NMT): Celestia menggunakan struktur data pohon Merkle yang dimodifikasi di mana daun Merkle diurutkan dan dikelompokkan berdasarkan penanda unik yang disebut "Namespace ID". Setiap rollup yang menggunakan Celestia memiliki Namespace ID tersendiri. Dengan menggunakan NMT, node rollup dapat mengunduh dan memverifikasi hanya data transaksi yang relevan bagi rantai mereka sendiri, tanpa perlu memproses data dari puluhan rollup lain yang berbagi blok di Celestia. Hal ini sangat menghemat bandwidth komunikasi node.

Light Node Tanpa Asumsi Mayoritas Jujur: Pada blockchain tradisional, light node harus memercayai bahwa mayoritas validator (2/3) bertindak jujur. Namun, light node Celestia yang dilengkapi DAS dapat memverifikasi ketersediaan data secara independen. Jika validator berbuat curang dengan menyembunyikan data, light node akan mendeteksinya secara langsung tanpa memerlukan asumsi kejujuran mayoritas validator.

Celestia bertindak sebagai First Mover murni dalam kategori alt-DA berdaulat. Sebelum peluncuran Celestia, tidak ada infrastruktur publik yang didedikasikan sepenuhnya untuk menjamin ketersediaan data. Dampak inovasi ini sangat mendalam karena berhasil melembagakan pemisahan lapisan (modularitas) sebagai standar industri baru, memaksa ekosistem monolitik seperti Ethereum untuk beradaptasi dengan meluncurkan peningkatan EIP-4844.

## 5 Technology Evolution

Perjalanan evolusi teknologi Celestia terdokumentasi dari fase uji coba hingga implementasi peningkatan tata kelola Mainnet Beta secara dinamis:

Mamaki Testnet (Mei 2022): Merupakan fase pengujian publik pertama dari fungsionalitas pengiriman data blob dan operasi sampling oleh light node ritel secara terdistribusi di seluruh dunia.

Mainnet Beta (31 Oktober 2023): Celestia meluncurkan mainnet pertamanya dengan konfigurasi aman, membatasi ukuran blok pada kisaran 2 MB hingga 8 MB untuk memastikan kestabilan konsensus awal Tendermint.

Upgrade Lemongrass (v2, September 2024): Diterapkan melalui CIP-17, peningkatan ini menetapkan mekanisme in-protocol signaling berdasarkan CIP-10. Dengan sistem ini, transisi peningkatan binary perangkat lunak berikutnya diaktifkan secara otomatis satu minggu setelah 5/6 kekuatan voting validator memberikan sinyal persetujuan secara on-chain, menghentikan ketergantungan pada koordinasi manual.

Upgrade Ginger (v3, Desember 2024): Diterapkan melalui CIP-25, peningkatan ini menghadirkan "The Doubling" yang memangkas waktu pembuatan blok dari 12 detik menjadi 6 detik untuk mempercepat finalitas transaksi. Ginger menyertakan CIP-21 (Authored Blobs) yang memverifikasi alamat pengirim langsung di dalam metadata blob, CIP-24 yang memindahkan parameter biaya gas ke tingkat sistem untuk stabilisasi biaya, CIP-27 yang membatasi transaksi PayForBlobs maksimal 600 per blok, dan CIP-28 yang membatasi ukuran transaksi maksimal pada 2 MiB.

mamo-1 Testnet (April 2025): Celestia sukses menyelenggarakan stress-testing skala produksi menggunakan 21 validator terdistribusi di Amsterdam, Paris, dan Warsaw. Jaringan berhasil memproses ukuran blok 128 MB dengan throughput berkelanjutan sebesar 21.33 MB/s. Keberhasilan ini didukung oleh protokol "Vacuum!" yang mengimplementasikan pemulihan data lewat Pull-Based Broadcast Tree (PBBT) untuk efisiensi transfer data antar-validator.

Upgrade Lotus (v4, Juli 2025): Diaktifkan pada tinggi blok 6,680,339 di Mainnet Beta. Lotus mengimplementasikan CIP-29 untuk memotong emisi tahunan, CIP-30 untuk menonaktifkan klaim otomatis imbal hasil staking, dan CIP-31 yang secara wajib mengunci hadiah staking (staking rewards) yang dihasilkan dari token vesting agar tidak dapat dicairkan sebelum masa kunci token induk berakhir.

Upgrade Matcha (v6, November 2025): Diaktifkan pada tinggi blok 8,662,012 di Mainnet Beta. Matcha menghadirkan CIP-38 yang memperluas kapasitas ukuran blok fisik hingga 128 MB, ukuran square maksimum ke 512, dan batas ukuran transaksi individual ke 8 MiB. Upgrade ini juga menurunkan periode unbonding staking menjadi 14 hari 1 jam (CIP-37) serta menurunkan trusting period light node menjadi 7 hari (CIP-36).

Protokol Fibre Blockspace (Januari 2026): Celestia merilis protokol ketersediaan data alternatif berkemampuan 1 Terabit per detik (1 Tb/s) berbasis ZODA encoding. Protokol ini berjalan secara paralel dengan protokol L1 Celestia. Fibre mengizinkan pengiriman blob data berukuran minimum 256 KB hingga maksimal 128 MB langsung ke validator, memproses data 881x lebih cepat daripada komitmen KZG.

## 6 Funding Intelligence

Berikut adalah rincian data historis putaran pendanaan Celestia berdasarkan catatan bursa dan intelijen modal ventura:

Funding Round: Seed Round

Date: Maret 2021

Amount: $1,500,000

Token Price: $0.00943

Implied Valuation: $9,430,000

Tokens Sold: 159,000,000 TIA

Allocation Percentage: 15.90% of genesis supply

Lead Investor: YZi Labs (sebelumnya Binance Labs), Interchain Foundation

Participants: Maven 11 Capital, KR1, Divergence Ventures

Vesting Period: 1-year cliff, 33% unlocked at Year 1, remaining 67% linear release over Year 1 to Year 2

Funding Round: Series A & B Combined Round

Date: 19 Oktober 2022

Amount: $55,000,000

Token Price: $0.30

Implied Valuation: $300,000,000

Tokens Sold: 197,000,000 TIA

Allocation Percentage: 19.70% of genesis supply

Lead Investor: Bain Capital Crypto, Polychain Capital - Participants: Coinbase Ventures, OKX Ventures, Robot Ventures, Placeholder Ventures, 1kx, Spartan Group, Galaxy Digital, Blockchain Capital, IOSG Ventures

Vesting Period: 1-year cliff, 33.33% unlocked at Year 1 (30 Oktober 2024), remaining 66.67% linear release over Year 1 to Year 2

Funding Round: Secondary Market Round

Date: Agustus 2023

Amount: Not publicly disclosed

Lead Investor: Not publicly disclosed

Funding Round: Series B Third Round / Strategic OTC Round

Date: 23 September 2024

Amount: $100,000,000

Implied Valuation: $3,500,000,000

Lead Investor: Bain Capital Crypto

Participants: Syncracy Capital, 1kx, Robot Ventures, Placeholder Ventures

Funding Round: Strategic Repurchase (Polychain Capital TIA Exit)

Date: 24 Juli 2025

Amount: $62,500,000

Token Price: ~$1.44 per TIA

Tokens Purchased: 43,451,616.09 TIA

Buyer: Celestia Foundation

Redistribution Plan: Dialokasikan kembali ke investor strategis baru dengan rolling unlock dari 16 Agustus hingga 14 November 2025

INKONSISTENSI: Terdapat pertentangan data mengenai total pengumpulan dana kumulatif Celestia. Database Tracxn mencatat total pendanaan mencapai $204,000,000 dalam 10 putaran, sedangkan laporan Clay, RootData, dan dokumen historis mencatat pengumpulan modal sebesar $156,500,000. Selisih sebesar ~$47,500,000 ini mengindikasikan adanya transaksi sekunder atau OTC privat yang tidak didokumentasikan secara rinci ke publik. Evidence: LOW.

INKONSISTENSI: Terkait pembagian Seri A & B Oktober 2022, beberapa database mendaftarkan putaran tersebut sebagai satu kesatuan senilai $55,000,000 pada harga token rata-rata $0.30, sementara database Chainbroker mendaftarkan Seri A sebesar $15,000,000 pada harga $0.0955 (valuasi $95,500,000) dan Seri B sebesar $40,000,000 pada harga $1.00 (valuasi $1,000,000,000). Perbedaan ini mencerminkan struktur internal diskon yang bervariasi bagi investor awal. Evidence: LOW.

## 7 Community Intelligence

Pada masa awal pendiriannya, Celestia mengabaikan kampanye pemasaran ritel konvensional dan berfokus sepenuhnya pada penarikan minat kelompok pengembang inti. Strategi ini diwujudkan melalui program "Modular Fellows" yang mendidik puluhan insinyur blockchain secara intensif mengenai perancangan rollup berdaulat menggunakan Celestia SDK. Dukungan teknis ini diperkuat lewat penyelenggaraan "Modular Summits" di Amsterdam (2022) dan Paris (2023), yang sukses membangun reputasi Celestia sebagai pusat pemikiran (thought leadership) gerakan blockchain modular.

Pilar pertumbuhan desentralisasi node Celestia digerakkan oleh keringnya spesifikasi perangkat keras untuk menjalankan light node. Karena light node Celestia dapat beroperasi di latar belakang komputer jinjing menggunakan DAS, Celestia berhasil menarik partisipasi ribuan operator node amatir di seluruh dunia untuk mengamankan jaringan testnet.

Keberhasilan komunitas yang paling masif sekaligus memicu ketidakstabilan jangka panjang adalah maraknya fenomena "Airdrop Staking Meta". Setelah mainnet diluncurkan, pengembang rantai modular baru (seperti Dymension, Saga, dan AltLayer) mengadopsi taktik pemasaran dengan membagikan token gratis secara eksklusif bagi pemegang TIA yang melakukan staking di validator Celestia. Narasi ini memicu gelombang FOMO (Fear Of Missing Out) di platform media sosial X (Twitter) dan Discord, mendorong rasio staking TIA melesat hingga 72.00% dari total sirkulasi. Siklus ini sukses memicu eforia pembelian token, namun ketika pasar rollup mengalami koreksi tajam sepanjang tahun 2025, berkurangnya imbal hasil airdrop memicu unbonding massal yang menghancurkan nilai bursa token TIA.

## 8 Narrative Intelligence

Narasi Celestia berkembang secara dinamis melintasi empat fase industri yang berbeda dari tahun 2021 hingga 2026:

Fase Eksperimental (2021-2023): Narasi "Modular vs Monolithic". Celestia berhasil mendikte perbincangan industri dengan mengampanyekan gagasan bahwa blockchain monolitik L1 adalah kegagalan desain yang tidak efisien karena menggabungkan seluruh fungsi di satu tempat. Konsep "ruang blok yang murah dan melimpah" diposisikan sebagai satu-satunya solusi logis penskalaan massal.

Fase Spekulasi Ekstrem (TGE hingga Pertengahan 2024): Narasi "Airdrop Engine". TIA tidak lagi dinilai sebagai token gas infrastruktur murni, melainkan sebagai "indeks modal ekosistem modular". Membeli dan men-stake TIA diasosiasikan dengan hak memperoleh pendapatan pasif berkelanjutan dari airdrop proyek L2/L3 yang diluncurkan di atas Celestia.

Fase Realisme Finansial (Late 2024-2025): Narasi "Modular Reset" dan "Value-Revenue Gap". Ketika harga TIA longsor 97% dari puncaknya, kritik tajam mengemuka terkait metrik pendapatan jaringan yang sangat rendah (hanya ~$60 per hari pada awal 2025). Pasar menyadari adanya jurang pemisah yang lebar antara valuasi spekulatif miliaran dolar dengan kegagalan protokol mengonversi efisiensi ruang blok menjadi aliran pendapatan riil bagi pemegang token.

Fase Infrastruktur Berkinerja Tinggi (2026): Narasi "Vision 2.0" dan era "Terabit-scale Blockspace". Celestia mengubah narasinya untuk tidak lagi sekadar menjadi basis rollup spekulatif, melainkan menjadi fondasi pasar finansial on-chain berkecepatan tinggi, sistem pembayaran mikro antar-agen kecerdasan buatan (AI), dan ruang blok konfidensial institusional.

## 9 Competitive Landscape

Lanskap persaingan lapisan Ketersediaan Data (DA) pada tahun 2026 terdokumentasi melalui perbandingan metrik dan keunggulan taktis masing-masing kompetitor utama:

Competitor: Ethereum Blob Space (EIP-4844)

Throughput: 0.67 MB/s

Cost per MB: ~$3.83 (Maret 2025)

Security Model: Native Ethereum L1 PoS Consensus dengan jaminan keamanan ekonomi tertinggi

Finality Time: 12 - 15 menit

Verification Method: Full Replication (seluruh node mengunduh data secara penuh)

Pros: Aliansi ekosistem Ethereum yang mendalam, likuiditas terkonsentrasi, keamanan ekonomi superior

Cons: Kapasitas terbatas, biaya pengunggahan data yang mahal saat terjadi kemacetan jaringan

Competitor: EigenDA (EigenLayer Restaking)

Throughput: 15.00 MB/s

Cost per MB: Sangat murah

Security Model: Restaked ETH validator set dengan jaminan modal ~$1,600,000,000

Finality Time: 12 - 15 menit (mengikuti Ethereum L1)

Verification Method: Off-chain Data Availability Committee (DAC), tidak mendukung verifikasi sampling publik (DAS)

Pros: Keamanan ekonomi bersandar langsung pada ekosistem Ethereum tanpa memerlukan jembatan token baru, throughput tinggi

Cons: Risiko tersentralisasi karena data dikendalikan oleh komite operator terbatas, ketergantungan pada struktur kontrak pintar kompleks

Competitor: Avail (Polygon Spin-out)

Throughput: 0.20 MB/s (uji coba mencapai 128.00 MB/s)

Cost per MB: Lebih murah daripada Celestia

Security Model: Nominated Proof of Stake (NPoS) dengan jaminan modal ~$100,000,000

Finality Time: ~40 detik menggunakan komitmen KZG tanpa challenge period - Verification Method: Data Availability Sampling (DAS) terintegrasi dengan Validity Proofs (KZG)

Pros: Finalitas sangat cepat, desentralisasi validator yang tangguh melalui model NPoS

Cons: Ekosistem pengembang yang lebih muda, traksi rollup komersial yang lebih rendah dibandingkan Celestia

Celestia berhasil memenangkan persaingan dari segi pangsa pasar komersial (menguasai ~50.00% pasar alt-DA) karena statusnya sebagai First Mover yang didukung secara agresif oleh jaringan RaaS global. Namun, Celestia memiliki kelemahan inheren pada waktu finalitas DA yang lama (~10 menit akibat challenge window pembuktian kecurangan) jika dibandingkan dengan Avail yang mampu membuktikan validitas pengkodean data secara instan (~40 detik) menggunakan komitmen matematis KZG.

## 10 Product Evolution

Iterasi dan evolusi produk Celestia mencerminkan perubahan prioritas tim pengembang untuk menjawab tantangan fragmentasi ekosistem modular:

Pivot dari LazyLedger ke Celestia (2019-2021): Transformasi dari sekadar proposal arsitektur penyimpanan minimalis menjadi kerangka kerja pengembang terintegrasi yang menyertakan Sovereign SDK. Hal ini mempermudah peluncuran rollup yang berdaulat secara hukum tanpa ketergantungan pada rantai settlement Ethereum.

Pengenalan Blobstream (2023-2024): Awalnya dirancang dengan nama Quantum Gravity Bridge (QGB). Blobstream berfungsi sebagai jembatan pembuktian ketersediaan data Celestia ke rantai settlement EVM. Produk ini mengizinkan rollup berbasis Arbitrum Orbit atau OP Stack untuk menyimpan data transaksi mereka di Celestia dengan biaya murah, sementara bukti ketersediaannya dikirimkan secara instan ke Ethereum L1.

Pivot ke Interoperabilitas "Lazybridging" (2025): Menghadapi masalah fragmentasi likuiditas yang parah di antara puluhan rollup modular, Celestia merilis arsitektur jembatan Zero-Knowledge (ZK) bawaan yang disebut "Lazybridging". Produk ini mengizinkan transfer aset lintas-rollup secara langsung di tingkat ketersediaan data, meminimalkan latensi dan biaya sengketa jembatan tradisional.

Peluncuran Fibre Blockspace (2026): Celestia merancang Fibre sebagai perluasan platform untuk menyediakan jalur tol (express lane) khusus. Produk ini dirancang khusus untuk memenuhi kebutuhan pasar bervolume tinggi yang membutuhkan latensi pengiriman blob dalam milidetik.

Akuisisi Sovereign Labs (Juli 2026): Celestia Labs secara resmi mengakuisisi Sovereign Labs untuk mengintegrasikan tim insinyur ZK terbaik ke dalam arsitektur intinya. Langkah strategis ini bertujuan mempercepat peluncuran kerangka kerja blockchain kustom berkinerja tinggi yang memiliki pembuktian ZK asli di atas ruang blok Celestia.

## 11 Tokenomics Intelligence

Sistem moneter TIA dirancang untuk mendukung operasional keamanan jaringan Proof of Stake (PoS) berbasis Cosmos SDK:

Token Name: TIA

Genesis Supply: 1,000,000,000 TIA

Max Supply: Unlimited (Sistem inflasi tanpa batas atas)

Token Allocation at Genesis:

Public Allocation: 20.00% (200,000,000 TIA)

Genesis Drop and Incentivized Testnet: 7.41%

Future Initiatives: 12.59%

R&D & Ecosystem: 26.79% (267,900,000 TIA)

Early Backers: Series A & B: 19.67% (196,700,000 TIA) (DropsTab mencatat 19.70% / 197,000,000 TIA)

Early Backers: Seed: 15.90% (159,000,000 TIA)

Initial Core Contributors: 17.64% (176,400,000 TIA) (DropsTab mencatat 17.60% / 176,000,000 TIA)

Precise Vesting and Unlock Schedules:

Public Allocation: 100.00% terbuka secara instan pada saat peluncuran TGE (31 Oktober 2023).

R&D & Ecosystem: 25.00% terbuka saat TGE. Sisa 75.00% rilis linier berkelanjutan dari akhir tahun ke-1 (30 Oktober 2024) hingga tahun ke-4.

Initial Core Contributors: 33.33% terbuka pada tebing akhir tahun ke-1 (30 Oktober 2024). Sisa 66.67% rilis linier berkelanjutan dari akhir tahun ke-1 hingga tahun ke-3.

Early Backers: Seed: 33.33% terbuka pada tebing akhir tahun ke-1. Sisa 66.67% rilis linier berkelanjutan dari akhir tahun ke-1 hingga tahun ke-2.

Early Backers: Series A & B: 33.33% terbuka pada tebing akhir tahun ke-1. Sisa 66.67% rilis linier berkelanjutan dari akhir tahun ke-1 hingga tahun ke-2.

History of Inflation Schedule Modifications:

Initial Inflation Schedule (At Genesis): Inflasi dimulai pada angka 8.00% di tahun pertama, berkurang 10.00% setiap tahun berikutnya hingga stabil pada batas bawah target (floor target) sebesar 1.50%.

Lotus Upgrade (v4, Juli 2025): Akibat tingginya kekhawatiran dilusi modal, komunitas menyetujui CIP-29. Peningkatan ini memotong emisi tahunan sebesar 33% secara instan (mengurangi tingkat inflasi dari ~7.20% menjadi ~5.00% di tahun 1.75). Skedul pengurangan emisi disesuaikan menjadi 6.70% per tahun menuju batas bawah stabil 1.50%.

Matcha Upgrade (v6, November 2025): Didorong oleh proposal CIP-41, inflasi tahunan dipotong secara radikal untuk kedua kalinya, jatuh langsung ke tingkat ~2.50%. Skedul pengurangan emisi tahunan tetap dikunci pada penurunan 6.70% per tahun hingga menyentuh batas bawah 1.50%.

Aturan Penguncian Hadiah Staking (Lotus Upgrade):

Sebelum peningkatan Lotus, validator dan investor awal dapat melakukan penarikan otomatis atas imbal hasil staking (staking rewards) harian mereka secara penuh ke bursa sekunder meskipun token pokok mereka masih dikunci (vesting). Hal ini dimanfaatkan oleh Polychain Capital untuk melikuidasi koin senilai total ~$179,000,000. Melalui implementasi CIP-31, Lotus menutup celah ini dengan mengunci perolehan hadiah staking secara proporsional dengan persentase sisa penguncian token pokok di dompet vesting mereka. Jika dompet investor memiliki 50.00% token terkunci, maka 50.00% imbal hasil staking yang dihasilkannya wajib tetap dikunci hingga tanggal buka kunci resmi tiba.

## 12 Airdrop & Incentive Intelligence (WAJIB)

Kampanye kualifikasi "Genesis Drop" Celestia mendistribusikan total 60,000,000 TIA (6.00% dari total suplai genesis) kepada lima kelompok kontributor dan pengguna on-chain:

Category: Research and Public Goods

Total Allocation: 6,000,000 TIA

Sub-category: Protocol Public Goods and Infrastructure

Allocation: 4,600,000 TIA

Eligible Accounts: 3,838

Minimum Reward: 1,198.54 TIA per alamat

Criteria: Kontributor GitHub publik untuk repositori Bitcoin, Ethereum, Cosmos Hub, Osmosis, spesifikasi EIP/BIP, dan kontributor dependensi inti Celestia (kecuali tim internal Celestia Labs).

Sub-category: Eth Research

Allocation: 1,400,000 TIA

Eligible Accounts: 1,947

Minimum Reward: 719.05 TIA per akun

Criteria: Anggota aktif forum Eth Research yang mempublikasikan minimal satu topik atau posting diskusi sebelum tanggal snapshot 5 Juli 2023.

Category: Early Modular Ecosystem

Total Allocation: 8,350,000 TIA

Eligible Accounts: 3,371

Minimum Reward: 2,477.01 TIA per alamat

Criteria: Kontributor repositori GitHub organisasi yang terdaftar di peta ekosistem Modular Summit 1 (Amsterdam, 2022) dan Modular Summit 2 (Paris, 2023), serta anggota terdaftar Modular Fellows Cohort 1.

Category: GitHub Super-Contributors

Total Allocation: 5,650,000 TIA

Sub-category: Contributor, ≥ 23 Total Commits

Allocation: 4,000,000 TIA

Eligible Accounts: 1,210

Minimum Reward: 3,305.79 TIA per alamat

Criteria: Kontributor dari kriteria Research dan Modular Ecosystem yang memiliki jumlah total riwayat komit (commits) minimal 23 kali di repositori terkait.

Sub-category: Contributor, ≥ 4 Total Commits - Allocation: 1,650,000 TIA

Eligible Accounts: 1,604

Minimum Reward: 1,028.68 TIA per alamat

Criteria: Kontributor dari kriteria terkait dengan jumlah komit minimal 4 kali.

Category: Early Adopters of Ethereum Rollups

Total Allocation: 20,000,000 TIA

Snapshot Date: 1 Januari 2023 (Tinggi Blok Ethereum: 16308181)

Criteria: Pengguna tergolong dalam 50.00% alamat paling aktif dari 10 rollup Ethereum teratas berdasarkan peringkat TVL L2Beat per 20 April 2023 (Arbitrum One, Arbitrum Nova, OP Mainnet, Starknet, zkSync Lite, dYdX, ImmutableX, SoRare, Loopring, Metis) dengan saldo minimal $50 saat snapshot. Pembagian didasarkan pada skor aktivitas komposit (skala 23):

Top 10% (Score ≥ 17): Alokasi 7,150,000 TIA untuk 78,793 alamat, dengan hadiah minimum 90.74 TIA.

Top 20% (Score ≥ 15): Alokasi 4,250,000 TIA untuk 60,186 alamat, dengan hadiah minimum 70.61 TIA.

Top 50% (Score ≥ 9.5): Alokasi 8,600,000 TIA untuk 171,317 alamat, dengan hadiah minimum 50.20 TIA.

Sybil Filter: Alamat yang terdaftar dalam daftar Sybil Hop Protocol, OP Airdrop #1, dan alamat berisiko tinggi yang teridentifikasi oleh visualisasi graf Trusta Labs dikeluarkan sepenuhnya dari kualifikasi.

Category: Stakers and IBC Relayers (Cosmos Hub & Osmosis)

Total Allocation: 20,000,000 TIA

Snapshot Date: Hub block 13482205 dan Osmosis block 7592794 (1 Januari 2023)

Sub-category: Stakers on Cosmos Hub & Osmosis

Allocation: 18,500,000 TIA

Criteria: Delegator dengan kepemilikan staking minimal $75 saat snapshot, dikalikan dengan skor aktivitas jaringan (skor komposit skala 15):

Top 10% (Stake × Activity): Alokasi 3,250,000 TIA untuk 29,630 alamat, hadiah minimum 109.69 TIA.

Top 50% (Stake × Activity): Alokasi 9,250,000 TIA untuk 116,552 alamat, hadiah minimum 79.36 TIA.

Bottom 50% (Stake × Activity): Alokasi 6,000,000 TIA untuk 119,635 alamat, hadiah minimum 50.15 TIA.

Sub-category: IBC Relayers

Allocation: 1,500,000 TIA

Eligible Accounts: 540

Minimum Reward: 2,777.78 TIA per alamat

Criteria: Alamat yang memproses transaksi MsgRecvPacket secara on-chain sebelum tanggal snapshot.

Tujuan utama dari distribusi taktis Genesis Drop adalah menghindari dominasi bot pertanian (farming sybil) dan memastikan token mengalir ke komunitas pengembang terdidik yang secara praktis akan mengoperasikan ekosistem modular. Metode ini sukses membentuk fondasi pengembang yang solid pada awal peluncuran jaringan. Namun, alokasi ritel murni yang dinilai terlalu kecil (hanya 2.00% dari total suplai genesis dialokasikan bagi pengguna L2 reguler) sempat menuai kekecewaan ritel karena dinilai menguntungkan kelompok insider dan pengembang berkemampuan komit tinggi saja.

## 13 Token Lifecycle Intelligence

Siklus kehidupan token TIA mencerminkan dinamika spekulasi awal yang diikuti oleh koreksi pasar sekunder akibat pelepasan pasokan berkala:

Fase Pra-TGE & Debut TGE (Oktober 2023): TIA diluncurkan secara resmi pada 31 Oktober 2023 dengan pasokan sirkulasi awal yang tipis, yaitu berkisar antara 141,000,000 TIA (14.10%) hingga 15.70% dari total suplai genesis. Hal ini memicu kelangkaan pasokan bursa sekunder yang signifikan.

Reli Pasca-TGE (30 hingga 90 Hari): Memasuki awal tahun 2024, didorong oleh merebaknya narasi airdrop staking lintas-ekosistem di media sosial, TIA memulai tren naik parabola. Harga token melesat dari harga awal di kisaran $2.00 hingga berhasil menembus All-Time High (ATH) historis sebesar $20.85 pada 10 Februari 2024 (atau $20.91 sesuai rincian alternatif CoinEx).

Penurunan dan Efek Tebing Token Unlock (180 Hari hingga 1 Tahun): Menjelang peristiwa unlock cliff pertama bagi kontributor awal dan investor swasta pada 30 Oktober 2024—yang membebaskan 17.68% dari total pasokan (senilai $1,100,000,000)—harga TIA mulai terperosok. Jaringan mengalami tekanan jual harian konstan dari investor besar yang mencairkan hadiah staking mereka secara instan di bursa sekunder.

Fase Kapitulasi "Modular Reset" (Akhir 2025 - Pertengahan 2026): Aksi dump dari alamat pengumpulan staking rewards VC seperti Polychain yang dituding menjual koin senilai up to $242,000,000, menekan harga TIA jatuh ke bawah tingkat psikologis $1.00.

All-Time Low (ATL) Jaringan: Jaringan mencatatkan ATL pada harga $0.2796 pada 5 April 2026 berdasarkan data RootData, sementara CoinGecko mencatat harga terendah historis di kisaran $0.2792 pada 6 Juni 2026.

INKONSISTENSI: Terkait tanggal pencatatan ATL, RootData mendaftarkan harga terendah di angka $0.2796 pada 5 April 2026, sedangkan database CoinGecko mendaftarkan rekor terendah di kisaran $0.2792 pada 6 Juni 2026. Ini mencerminkan perbedaan data umpan harga (price feed) bursa pada puncak kepunahan kapitulasi ritel. Evidence: LOW.

Berdasarkan analisis fundamental mendalam di pertengahan tahun 2026, harga TIA saat ini di kisaran $0.35 hingga $0.45 dinilai Undervalued (di bawah nilai wajarnya). Hal ini disebabkan karena pembongkaran kepemilikan bursa oleh investor besar yang telah selesai sepenuhnya melalui aksi buyback strategis Celestia Foundation senilai $62,500,000, penurunan dramatis emisi inflasi ke tingkat 2.50% via upgrade Matcha, serta dominasi Celestia yang menguasai 50% pasar DA global dengan memproses 160 GB data rollup. Dengan perbaikan struktur moneter ini, kapitalisasi pasar sirkulasi TIA sebesar ~$285,100,000 hingga ~$373,000,000 menyajikan potensi pemulihan yang sangat asimetris ketika adopsi pasar bervolume tinggi di atas Fibre mulai beroperasi penuh.

## 14 Business Intelligence

Dinamika operasional komersial Celestia sebagai infrastruktur ketersediaan data terdokumentasi melalui indikator kinerja utama (KPI) berikut:

Financial & Staking Dynamics:

Circulating Market Capitalization: $285,100,000 (per Maret 2026) hingga $373,000,000 (per pertengahan 2026)

Fully Diluted Valuation (FDV): $370,800,000 (per Maret 2026) hingga $468,000,000 (per pertengahan 2026)

Real Economic Value (REV) Q2 2025: $79,503

Real Economic Value (REV) Q3 2026 Forecasted: $14,533

Daily Network Fees (Juli 2026): $89.26

Daily Network Revenue (Juli 2026): $1.79

Staking Ratio: 64.00% hingga 65.00% dari total koin sirkulasi

Staking APY (Mei 2026 Peak): 14.67%

Network Activity & Capacity Metrics:

Active Production Rollups: 100+ rantai produksi aktif

Active General Rollups: 35+ rollup komersial

Total Rollup Data Processed: 160.00 GB sejak peluncuran mainnet

Average Daily Data Volume: 2.50 GB

Daily Blob Fees end of 2024: ~$225 per hari

Daily Blob Fees H1 2025: ~$60 per hari (menurun sementara akibat peningkatan efisiensi data kompresi)

Daily Blob Fees Growth Rate (Late 2024 to Mid-2026): Meningkat 10x lipat seiring adopsi massal rollup komersial

Active Validator Set Size: Maksimal 100 validator

Validator Commission Cap: Maksimal 25.00% (Lotus), operasional efektif dibatasi pada 20.00% (Matcha)

Unbonding Period: 14 hari 1 jam (Matcha)

Trusting Period / Sampling Window: 7 hari (Matcha)

Maximum Physical Block Size: 128 MB (Matcha)

Maximum Transaction Size: 8 MiB (Matcha) (sebelumnya 2 MiB pada Ginger)

## 15 Success & Failure Analysis

Evaluasi komprehensif atas tingkat pencapaian sasaran Celestia dianalisis dari delapan perspektif pemangku kepentingan dalam ekosistem:

Perspective: Founder

Verdict: Sukses

Alasan: Berhasil membuktikan kelayakan hipotesis modular secara global, mendirikan standar pasar baru, dan meluncurkan mainnet yang beroperasi stabil memproses gigabyte data.

Confidence Level: HIGH

Perspective: Venture Capital (VC)

Verdict: Sukses

Alasan: Investor awal seperti Polychain merealisasikan keuntungan berlipat ganda ($242.000.000) dari ekstraksi staking rewards likuid sejak TGE dari modal awal yang relatif sangat kecil ($20.000.000).

Confidence Level: HIGH

Perspective: Retail Users

Verdict: Campuran

Alasan: Penerima airdrop awal mengumpulkan keuntungan empat digit bebas risiko. Namun, pembeli ritel di pasar sekunder mengalami kerugian modal yang parah (hingga 97%) akibat membeli pada masa puncak gelembung spekulasi staking.

Confidence Level: HIGH

Perspective: Community

Verdict: Campuran

Alasan: Staker menikmati aliran hadiah airdrop beruntun dari ekosistem rollup di awal, tetapi struktur insentif jangka panjang hancur ketika nilai koin pokok mereka terdepresiasi tajam akibat overhang penjualan bursa.

Confidence Level: HIGH

Perspective: Developer

Verdict: Sukses

Alasan: Mendapatkan kebebasan berekspresi secara teknis menggunakan Sovereign SDK tanpa hambatan aturan settlement, serta menikmati biaya DA termurah di industri (hanya ~$0.07 per MB).

Confidence Level: HIGH

Perspective: Institution

Verdict: Campuran

Alasan: Memperoleh peluang masuk yang aman melalui OTC putaran September 2024 dengan harga masuk yang terdiskon. Namun, akumulasi modal mereka terhambat oleh realitas bahwa model ekonomi Celestia memiliki tingkat akumulasi nilai pendapatan (fee capture) yang sangat lemah saat ini.

Confidence Level: MEDIUM

Perspective: Validator

Verdict: Sukses

Alasan: validator menikmati stabilitas operasi karena persentase koin yang didelegasikan tetap tinggi (>60.00%), dibarengi kelonggaran margin biaya server melalui peningkatan batas komisi validator hingga 20.00% pada Matcha. - Confidence Level: HIGH

Perspective: Builder (RaaS & Rollup Frameworks)

Verdict: Sukses - Alasan: Celestia terintegrasi secara mulus di dalam seluruh repositori framework industri utama seperti OP Stack, Arbitrum Orbit, dan Polygon CDK, memposisikan Celestia sebagai fondasi yang sangat lengket (sticky).

Confidence Level: HIGH

## 16 Historical Timeline

Berikut adalah kronologi lengkap perjalanan historis Celestia yang disusun berdasarkan urutan tanggal peristiwa penting beserta analisis sebab-akibatnya:

2018 — Mustafa Al-Bassam memformulasikan konsep Data Availability Sampling (DAS) dalam makalah riset akademisnya — Menjadi landasan teoritis utama bagi pembuatan blockchain khusus ketersediaan data modular.

2019 — Proyek dimulai dengan nama LazyLedger dan dokumen whitepaper diterbitkan — Memperkenalkan pemisahan konsensus dan eksekusi transaksi ke industri blockchain global.

7 Januari 2020 — Pendirian badan hukum resmi Inggris Raya (CIN: 12391157) — Menyediakan dasar hukum formal untuk merekrut tim pengembang inti dan menandatangani perjanjian lisensi komersial.

4 Maret 2021 — Penggalangan dana putaran Seed senilai $1,500,000 diselesaikan — Dipimpin oleh Interchain Foundation dan Binance Labs (YZi Labs) untuk mendanai awal kode protokol.

15 Juni 2021 — LazyLedger secara resmi berganti nama menjadi Celestia — Penyesuaian nama brand untuk persiapan rilis devnet dan interaksi publik.

Desember 2021 — Peluncuran Devnet pertama Celestia — Memungkinkan sekelompok kecil pengembang menguji coba modul pengiriman blob awal.

25 Mei 2022 — Peluncuran Mamaki Testnet — Memulai uji coba publik ketersediaan data sampling berinsentif untuk validator dan light node.

20 Oktober 2022 — Penggalangan dana putaran Seri A & B senilai $55,000,000 diumumkan — Dipimpin oleh Bain Capital Crypto dan Polychain Capital untuk memperluas tim rekayasa.

Agustus 2023 — Penggalangan dana putaran pasar sekunder selesai — Menyediakan likuiditas tambahan sebelum peluncuran mainnet komersial.

26 September 2023 — Pengumuman resmi kampanye Genesis Drop — Mengalokasikan 60 juta TIA ke komunitas open-source, developer, dan stakers Cosmos/Osmosis.

17 Oktober 2023 — Penutupan klaim Genesis Drop — Menyaring alamat sybil untuk memastikan distribusi token awal yang adil.

31 Oktober 2023 — Peluncuran Mainnet Beta Celestia dan pembukaan perdagangan bursa token TIA — Menandai tonggak sejarah beroperasinya rantai DA modular komersial pertama di dunia.

1 November 2023 — Binance mencatatkan perdagangan pasar TIA — Mendorong likuiditas instan ke basis ritel global.

2 November 2023 — Coinbase mencatatkan perdagangan pasar TIA — Membuka akses masuk bagi modal terikat regulasi Amerika Serikat.

10 Februari 2024 — Harga bursa TIA menyentuh ATH historis sebesar $20.85 — Terjadi akibat eforia spekulasi massal seputar airdrop staking meta.

19 Agustus 2024 — Peningkatan Lemongrass (v2) diaktifkan di testnet Arabica — Memulai transisi sistem tata kelola peningkatan ke mekanisme in-protocol signaling (CIP-10).

28 Agustus 2024 — Lemongrass (v2) diaktifkan di testnet Mocha — Menyelesaikan uji coba integrasi validator sebelum migrasi mainnet.

18 September 2024 — Peningkatan Lemongrass (v2) resmi mengudara di Mainnet Beta — Upgrade konsensus pertama yang menstabilkan koordinasi peningkatan perangkat lunak.

23 September 2024 — Pengumuman putaran strategis OTC senilai $100,000,000 — Dipimpin oleh Bain Capital Crypto dengan valuasi pasca-pendanaan sebesar $3.500.000.000 untuk mempercepat riset penskalaan gigabyte.

30 Oktober 2024 — Peristiwa unlock token investor dan kontributor awal senilai $1.100.000.000 pertama kali dibuka — Memulai peningkatan pesat pasokan sirkulasi dan tekanan jual sekunder.

5 November 2024 — Peningkatan Ginger (v3) diaktifkan di testnet Arabica — Uji coba waktu blok 6 detik di bawah beban kompresi tinggi.

14 November 2024 — Ginger (v3) diaktifkan di testnet Mocha — Membuka jalur integrasi validator profesional.

12 Desember 2024 — Peningkatan Ginger (v3) resmi mengudara di Mainnet Beta — Mengaktifkan emisi waktu blok 6 detik dan authored blobs di tingkat produksi.

Januari 2025 — Jaringan melipatgandakan ukuran blok fisik menjadi 8 MB via pemungutan suara on-chain — Memperluas kapasitas tampung untuk menampung integrasi rollup baru.

April 2025 — Penyelenggaraan uji coba testnet mamo-1 — Membuktikan kelayakan blok 128 MB dengan throughput 21.33 MB/s secara permissionless.

8 Mei 2025 — Upbit mencatatkan perdagangan pasar TIA — Mendorong likuiditas ritel Korea Selatan ke dalam pasar sekunder.

16 Mei 2025 — Peningkatan Lotus (v4) diaktifkan di testnet Arabica — Uji coba sistem pencegahan ekstraksi staking rewards.

23 Juni 2025 — Co-founder merespons FUD dengan menyatakan yayasan memiliki kas cadangan di atas $100.000.000 — Menjaga kepercayaan komunitas di tengah anjloknya pasar sekunder.

26 Juni 2025 — Publikasi data on-chain bahwa Polychain Capital mencatatkan profit $80.000.000 dari staking rewards — Memicu perdebatan komunitas dan reformasi regulasi moneter.

1 Juli 2025 — Lotus (v4) diaktifkan di testnet Mocha — Menyatukan kesiapan validator menjelang upgrade mainnet.

24 Juli 2025 — Celestia Foundation mengumumkan pembelian kembali (buyback) sisa TIA milik Polychain senilai $62.500.000 — Dilakukan pada harga pasar $1,44 per token untuk meredam kritik atas dumping rewards Polychain di bursa sekunder.

28 Juli 2025 — Peningkatan Lotus (v4) resmi mengudara di Mainnet Beta — Menurunkan inflasi ke tingkat ~5,00% dan secara wajib mengunci staking rewards dari dompet vesting (CIP-31).

16 Agustus 2025 — Awal jadwal pengalokasian kembali koin Polychain ke investor baru — Memulai rolling unlock bertahap selama tiga bulan untuk mengembalikan likuiditas yang terdistribusi.

9 September 2025 — Peningkatan Matcha (v6) diaktifkan di testnet Arabica — Uji coba skalabilitas blok raksasa 128 MB.

3 Oktober 2025 — Matcha (v6) diaktifkan di testnet Mocha — Penyelarasan operator validator sebelum peluncuran mainnet.

14 November 2025 — Penyelesaian rolling unlock bertahap sisa koin Polychain — Menutup overhang penjualan investor awal secara penuh.

24 November 2025 — Peningkatan Matcha (v6) resmi mengudara di Mainnet Beta — Mengaktifkan kapasitas blok fisik 128 MB dan memotong inflasi tahunan ke tingkat ~2,50%.

13 Januari 2026 — Pengumuman resmi protokol Fibre Blockspace — Membuka jalan menuju kapasitas blok gigabyte scale berbasis ZODA encoding.

22 Januari 2026 — Pengenalan Celestia Private Blockspace — Menawarkan privasi transaksi on-chain khusus untuk pasar institusional.

14 Februari 2026 — Hibiscus (v7) diaktifkan di testnet Arabica — Uji coba kompresi data tingkat lanjut.

23 Februari 2026 — Hibiscus (v7) diaktifkan di testnet Mocha — Pengujian finalitas sebelum integrasi v8.

4 April 2026 — Peningkatan v8 diaktifkan di testnet Arabica — Memulai integrasi gabungan fitur Hibiscus.

6 Juni 2026 — Harga pasar TIA menyentuh ATL historis di titik $0,2792 — Menandai puncak kapitulasi bursa ritel akibat eforia spekulasi modular yang mendingin.

15 Juli 2026 — Celestia Labs mengakuisisi Sovereign Labs — Mengintegrasikan tim insinyur ZK untuk meluncurkan blockchain kustom berkinerja tinggi.

## 17 Current Status

Saat ini di pertengahan tahun 2026, Celestia berada dalam fase pemulihan struktural yang tenang pasca-peristiwa "Modular Reset". Dari sisi pasar, volatilitas harga TIA telah terkompresi secara signifikan, bergerak stabil di kisaran $0,31 hingga $0,45 dengan volume transaksi harian sekitar $20.000.000. Spekulan ritel sebagian besar telah meninggalkan ekosistem, menyisakan jaringan yang kini dihargai berdasarkan utilitas murninya.

Kondisi teknologi Celestia berada pada level puncaknya. Matcha upgrade telah berjalan dengan stabil di Mainnet Beta, membuktikan kemampuan jaringan memproses blok hingga 128 MB tanpa mengorbankan desentralisasi validator. Dari sisi bisnis, Celestia mendominasi ceruk pasar ketersediaan data modular dengan melayani lebih dari 100 rantai produksi aktif. Pengenalan inisiatif Fibre Blockspace dan teknologi "Lazybridging" menempatkan Celestia pada jalur transformasi menuju L1 khusus pasar on-chain performa tinggi. Kerangka moneter juga jauh lebih sehat, di mana pemangkasan inflasi ke angka 2,50% sukses menekan emisi tahunan secara berkelanjutan.

## 18 Lessons Learned

Perjalanan Celestia memberikan empat pelajaran berharga bagi evolusi industri blockchain di masa depan:

Pemisahan Fungsi (Modularity) Berhasil Secara Teknis, Namun Menantang Secara Finansial: Celestia membuktikan secara empiris bahwa memisahkan DA dari eksekusi melahirkan efisiensi biaya luar biasa (99% lebih murah daripada L1 monolitik). Namun, pelajaran terbesarnya adalah: jika ruang blok dibuat terlalu murah dan melimpah, jaringan akan kesulitan mengumpulkan nilai moneter riil (Real Economic Value) ke dalam token aslinya. Tanpa adanya mekanisme burn yang agresif atau permintaan transaksi yang luar biasa masif, murahnya biaya transaksi justru akan memicu krisis depresiasi nilai token akibat tekanan emisi tahunan.

Celah Hukum Vesting Hadiah Staking Harus Ditutup Sejak Genesis: Kesalahan struktural terbesar Celestia adalah membiarkan investor awal (seperti Polychain Capital) untuk melakukan klaim dan penjualan instan atas staking rewards yang dihasilkan oleh token terkunci mereka. Hal ini menciptakan rute keluar dini (synthetic exit) bagi investor modal besar, melahirkan penjualan harian bernilai ratusan juta dolar yang merusak kepercayaan ritel dan menekan pasar bursa. Peningkatan Lotus (CIP-31) yang mewajibkan hadiah staking mengikuti jadwal vesting token induknya adalah aturan baku yang wajib diimplementasikan oleh setiap proyek kripto baru sejak hari pertama.

Pendekatan Bootstrapping Berbasis Pengembang Melahirkan Retensi Tinggi: Keberhasilan Celestia meluncurkan program Modular Fellows dan menyelenggarakan Modular Summits membuktikan bahwa membangun ekosistem pengembang yang loyal jauh lebih bernilai jangka panjang daripada membelanjakan modal jutaan dolar untuk kampanye airdrop ritel yang tidak lengket.

Keamanan DAS Bergantung pada Keberadaan Light Node: Arsitektur DAS hanya aman jika ada jaringan light node yang cukup luas untuk melakukan sampling acak secara kolektif. Mengasumsikan keberadaan setidaknya satu node jujur tanpa merancang integrasi light node langsung di dalam dompet pengguna (user wallet) adalah celah risiko keamanan potensial yang harus dihindari di masa depan.

## 19 Knowledge Extraction Candidate (BAGIAN PALING PENTING)

Laporan intelijen ini mengekstrak entitas, hubungan ontologi, dan pola perilaku sistemik Celestia untuk digunakan kembali sebagai data pengetahuan:

Entity Baru: Mustafa Al-Bassam, John Adler, Ismail Khoffi, Celestia Labs, Celestia Foundation, Polychain Capital, Bain Capital Crypto, Lotus Upgrade, Matcha Upgrade, Fibre Blockspace, ZODA Encoding, Data Availability Sampling, Namespaced Merkle Trees, Lazybridging.

Relationship (Ontology):

[Mustafa Al-Bassam] -> co-founded -> [Celestia Labs]

[John Adler] -> co-founded -> [Celestia Labs]

[Ismail Khoffi] -> co-founded -> [Celestia Labs]

[Celestia Labs] -> developed -> [Celestia Protocol]

[Celestia Foundation] -> repurchased -> [Polychain Capital TIA Stake]

[Lotus Upgrade] -> implemented -> [CIP-31 Vesting Lock]

[Matcha Upgrade] -> expanded -> [Block capacity to 128MB]

[Fibre Blockspace] -> utilizes -> [ZODA Encoding]

[Celestia Protocol] -> optimized -> [Rollup Data Availability Cost]

Pattern (Causal Chains):

Nama Pola: Airdrop Reflexivity Meta Loop

Rantai Sebab-Akibat: Peluncuran mainnet berpasokan sirkulasi rendah -> Protokol rollup baru memutuskan memberikan airdrop eksklusif bagi stakers TIA -> Pengguna ritel berbondong-bondong membeli dan men-stake koin demi mengincar kualifikasi drop -> Rasio staking meroket di atas 70% -> Harga token terpompa secara tidak wajar ke ATH akibat kelangkaan pasokan bursa -> Siklus hype mendingin akibat kejenuhan pasar rollup -> Likuiditas menipis diikuti unbonding massal yang merusak harga bursa.

Nama Pola: Vesting Loophole Capital Extraction

Rantai Sebab-Akibat: Token alokasi VC dikunci di bawah jadwal vesting tebing satu tahun -> Sistem membolehkan koin terkunci untuk didelegasikan/di-stake -> Hadiah staking terdistribusi secara harian dalam bentuk token liquid penuh -> VC secara sistematis menjual hadiah staking harian tersebut ke pasar sekunder untuk merealisasikan keuntungan awal -> Terjadi tekanan jual konstan tanpa tandingan dari investor dalam (insiders) -> Ritel mengalami kerugian modal parah dan memicu kemarahan komunitas -> Yayasan terpaksa mengeksekusi pembelian balik (buyback) darurat dan meluncurkan upgrade konsensus untuk mengunci paksa hadiah staking (Lotus Upgrade).

## 20 Transferable Intelligence

Jika AI di masa depan bertugas mengevaluasi proyek infrastruktur kripto baru, pelajaran dan indikator berikut dapat dijadikan aturan umum (rules):

Aturan Evaluasi Vesting VC (Rule Umum): "Staking Reward Lockstep Rule." AI harus memeriksa apakah kontrak pintar proyek mengizinkan token terkunci menghasilkan hadiah staking yang likuid. Jika ya, AI wajib mengidentifikasi proyek tersebut memiliki risiko tekanan jual insider tinggi sejak awal peluncuran. Aturan baku: Hadiah staking dari token terkunci wajib tunduk pada jadwal pembukaan kunci proporsional yang sama dengan token induknya.

Aturan Evaluasi Akrual Nilai Infrastruktur (Rule Umum): "Cost-Revenue Divergence Trap." AI tidak boleh langsung menyimpulkan bahwa penghematan biaya transaksi yang disajikan oleh sebuah rantai baru (misalnya memotong biaya hingga 99%) akan otomatis meningkatkan harga token aslinya. AI harus menghitung elastisitas permintaan ruang blok: jika biaya dibuat terlalu murah, proyek membutuhkan volume adopsi ratusan juta transaksi harian agar biaya pembakaran (burn rate) mampu mengimbangi tingkat inflasi token. Rantai yang memiliki utilitas tinggi namun tidak dilengkapi mekanisme penangkapan nilai (value capture) yang kuat akan berakhir sebagai barang komoditas murah dengan kinerja token yang buruk. - Aturan Evaluasi Desentralisasi DAS (Rule Khusus - Hanya berlaku untuk rantai berbasis DAS): "Client-side Light Node Feasibility." Keamanan matematis sampling data hanya valid jika light node dijalankan secara aktif oleh pengguna akhir di perangkat konsumen mereka sendiri. AI wajib menginvestigasi apakah proyek menyediakan SDK ringan yang mudah diintegrasikan langsung ke dalam wallet ponsel atau browser extension. Jika verifikasi data masih harus bergantung pada server hosting (cloud) milik pihak ketiga, klaim desentralisasi dan keamanan rantai modular tersebut harus dinilai dengan penalti keyakinan tinggi.

## 21 Open Questions

Beberapa pertanyaan penelitian penting dan hipotesis terbuka yang perlu terus dipantau di masa depan meliputi:

Apakah inisiatif "Every Market Onchain" (Vision 2.0) dan peluncuran Fibre Blockspace berkemampuan 1 Tb/s benar-benar mampu menarik minat industri non-kripto (seperti penayangan iklan real-time dan pembayaran mikro antar-agen AI) untuk menggunakan Celestia sebagai infrastruktur inti, atau apakah inisiatif ini akan kembali berakhir sebagai ruang blok kosong yang tidak terutilisasi secara komersial?

Bagaimana dinamika kompetisi jangka panjang antara Celestia dan EigenDA, khususnya setelah EigenDA mengaktifkan pemotongan modal (slashing) di Ethereum L1 dan apakah integrasi restaking ETH terbukti lebih stabil daripada model jaminan keamanan DPoS independen milik Celestia?

Akankah model pemangkasan inflasi bertahap Celestia (Lotus dan Matcha) yang menargetkan inflasi terminal sebesar 1,50% cukup kuat untuk mengimbangi emisi token sekunder, ataukah Celestia pada akhirnya membutuhkan mekanisme pembakaran token (token burn) paksa pada tingkat pengiriman blob untuk melahirkan ekosistem tokenomik yang deflasioner?

## 22 Evidence Level

Berikut adalah penilaian tingkat keyakinan (Evidence Level) atas kesimpulan-kesimpulan penting yang ditarik dalam laporan intelijen ini:

Kesimpulan: Celah ekstraksi staking rewards dari token terkunci milik Polychain Capital adalah pemicu utama kejatuhan ekstrem harga TIA di tahun 2024-2025.

Level Keyakinan: HIGH

Alasan: Terkonfirmasi secara on-chain oleh analis data indeks independen yang mengestimasi penjualan liquid rewards Polychain mencapai ~$179.000.000 hingga ~$242.000.000, serta fakta bahwa Celestia Foundation segera mengerahkan Lotus Upgrade khusus untuk menutup celah ini dan melakukan buyback sisa TIA milik Polychain senilai $62.500.000.

Kesimpulan: Upgrade Matcha sukses meningkatkan kapasitas blok operasional harian hingga 128 MB tanpa mengorbankan stabilitas konsensus atau desentralisasi validator.

Level Keyakinan: HIGH

Alasan: Tercatat di dalam spesifikasi peningkatan resmi (CIP-38), rilis binary celestia-app v6, keberhasilan pengujian mamo-1 testnet berkapasitas 128 MB, dan rilis stabil di Mainnet Beta sejak November 2025.

Kesimpulan: Protokol Fibre Blockspace mampu mempertahankan kapasitas data throughput sebesar 1 Tb/s secara stabil di bawah kondisi lingkungan operasional dunia nyata (bukan sekadar lingkungan pengujian terkontrol).

Level Keyakinan: MEDIUM

Alasan: Tolok ukur (benchmarking) 1 Tb/s berhasil dicapai dalam lingkungan pengujian terkontrol menggunakan 498 mesin server berkinerja tinggi di GCP dengan tautan bandwidth 34-45 Gbps. Di dunia nyata, validator Celestia tersebar di berbagai wilayah dengan spesifikasi koneksi internet lokal yang bervariasi, sehingga degradasi kinerja akibat latensi transit antar-negara masih mungkin terjadi.

## 23 Karya yang dikutip

Celestia on Tracxn — https://tracxn.com/d/companies/celestia/__e9lFtoe2JngZ2Ws_0uK2xeTpXSMEiWtTAKGnUkbpcCc

Celestia Funding and Key Investors on Clay — https://www.clay.com/dossier/celestia-funding

Celestia Profile on ICO Drops — https://icodrops.com/celestia/

Celestia Project Details on RootData — https://www.rootdata.com/projects/detail/Celestia?k=MTk4NA%3D%3D

Celestia Token Metrics and Vesting on Chainbroker — https://chainbroker.io/projects/celestia/

Celestia Fundraising History on DropsTab — https://dropstab.com/coins/celestia/fundraising

Celestia (TIA) Utility and Upgrades on SunCrypto — https://suncrypto.in/price/celestia

Celestia Staking, Governance, and Supply Docs — https://docs.celestia.org/learn/TIA/staking-governance-supply/

CIP-029: Decrease Inflation and Disinflation — https://github.com/celestiaorg/CIPs/blob/main/cips/cip-029.md

Celestia (TIA) Price and Volume on CoinGecko — https://www.coingecko.com/en/coins/celestia

Celestia Tokenomics Analysis on Binance Square — https://www.binance.com/en/square/post/2821174689577

How Celestia Used Modular Blockchain Messaging on BlockchainAppFactory — https://www.blockchainappfactory.com/blog/how-celestia-tia-used-modular-blockchain-messaging/

Celestia Genesis Airdrop in TIA on CoinPri — https://coinpri.com/news/cryptocurrency/celestia-genesis-airdrop-in-tia/

What is Celestia (TIA) Modular Blockchains on OKX — https://www.okx.com/learn/what-is-celestia-tia-modular-blockchains-for-a-scalable-future

Celestia Retroactive Airdrop Guide on AirdropAlert — https://airdropalert.com/airdrops/celestia-retroactive/

Celestia Genesis Drop official details — https://blog.celestia.org/genesis-drop/

Celestia Ecosystem Overview on Bitget — https://www.bitget.com/airdrop/celestia-ecosystem

Saga Genesis Drop Claiming Criteria on Binance Square — https://www.binance.com/en/square/post/5118462553609

Celestia (TIA) Price Prediction on CoinEx Academy — https://www.coinex.com/en/academy/detail/4070-celestia-tia-price-prediction

Celestia Latest Updates on CoinMarketCap — https://coinmarketcap.com/cmc-ai/celestia/latest-updates/

Foundation Delegation Program for Validators — https://docs.celestia.org/operate/consensus-validators/foundation-delegation-program/

Celestia Price Prediction Through 2030 on CryptoRank — https://cryptorank.io/news/feed/d3801-celestia-tia-price-prediction-2030

Celestia Blob Economics and Rollup Costs on BlockEden — https://blockeden.xyz/blog/2026/01/16/celestia-blob-economics-data-availability-rollup-costs/

Celestia, Polychain, and the Unlock Strategy on OKX — https://www.okx.com/learn/celestia-polychain-unlock-governance-market

Polychain Exits Celestia with Token Sale on CryptoNews — https://cryptonews.com.au/news/polychain-exits-celestia-with-us62-5m-token-sale-amid-investor-scrutiny-130064/

Polychain sells TIA stake to Celestia Foundation on The Block — https://www.theblock.co/post/364155/polychain-sells-remaining-62-5-million-tia-stake-to-celestia-foundation-amid-criticism-of-staking-reward-sales

Celestia Redeems TIA from Polychain on CryptoRank — https://cryptorank.io/news/feed/7cd0d-celestia-redeems-tia-from-polychain-revamps-staking-rewards

Layer 1 Blockchains Performance and Unlocks in 2025 on Bitget — https://www.bitget.com/news/detail/12560605126855

Celestia Improvement Proposals Directory — https://github.com/celestiaorg/CIPs/blob/main/cips/README.md

Celestia Vision 2.0: Every Market Onchain — https://blog.celestia.org/celestia-vision-2-0-every-market-onchain/

Choosing Your Data Availability Layer on Eclipse Labs — https://www.eclipselabs.io/blogs/choosing-your-data-availability-layer-celestia-avail-eigenda-compared

Alt-DA Solutions Spotlights on Zeeve — https://www.zeeve.io/blog/alt-da-solutions-changing-the-cost-game-for-l2-rollups-spotlight-on-key-players/

Modular DA Battle on ChainCatcher — https://www.chaincatcher.com/en/article/2112218

Token Distribution and Fundraising Models on BCAS — https://blog.bcas.io/token-distribution-and-fundraising-models

Celestia Overview on BusinessModelCanvasTemplate — https://businessmodelcanvastemplate.com/blogs/owners/celestia-who-owns

History of Celestia on Binance Square — https://www.binance.com/en/square/post/20152748418002

Brief History of Celestia — https://businessmodelcanvastemplate.com/blogs/brief-history/celestia-brief-history

Celestia Profile on StartupIntros — https://startupintros.com/orgs/celestia

Celestia Modular Network Guide on CoinEx — https://www.coinex.com/en/academy/detail/1390-celestia-the-worlds-first-modular-blockchain-networka-game-changer-for-blockchain-development

What is Celestia on CoinLedger — https://coinledger.io/learn/what-is-celestia

Celestia Raises $100M Funding on SiliconANGLE — https://siliconangle.com/2024/09/24/celestia-foundation-nabs-100m-modular-blockchain-network/

Celestia Foundation Raises $100M on The Block — https://www.theblock.co/post/317768/celestia-foundation-raises-100-million-in-a-round-led-by-bain-capital-crypto

Celestia Raises $100M and TIA Jumps on CryptoRank — https://cryptorank.io/news/feed/b7c5f-celestia-raises-100m-tia-token-jumps-17-overnight

Celestia Raises $100 Million Ahead of Unlock on The Defiant — https://thedefiant.io/news/blockchains/celestia-raises-usd100-million-ahead-of-usd1-billion-token-unlock

Network Upgrades Guide on Celestia Docs — https://docs.celestia.org/operate/maintenance/network-upgrades/

Matcha Upgrade Announcement on Celestia Blog — https://blog.celestia.org/matcha/

Shwap Protocol Specification on Celestia Blog — https://blog.celestia.org/shwap/

mamo-1 128MB Testnet on Celestia Blog — https://blog.celestia.org/mamo-1/

Introducing Fibre 1Tb/s Blockspace — https://blog.celestia.org/introducing-fibre-1tb-s-of-blockspace/

Celestia Price Prediction 2026-2030 on KuCoin — https://www.kucoin.com/blog/celestia-tia-price-prediction-2026-2030-modular-future

Celestia Price Prediction on Coincub — https://coincub.com/price-prediction/celestia-price-prediction/

Celestia Financials on Blockworks Analytics — https://blockworks.com/analytics/celestia/celestia-financials/celestia-token-holder-income-statement

Karya yang dikutip

1. TIA to INR: Live Celestia Price Chart - SunCrypto, https://suncrypto.in/price/celestia 2. How Celestia ($TIA) Captured Attention Through Modular Blockchain Messaging, https://www.blockchainappfactory.com/blog/how-celestia-tia-used-modular-blockchain-messaging/ 3. Celestia: Funding, Team & Investors | Startup Intros, https://startupintros.com/orgs/celestia 4. 1 GB blocks to Build Whatever - Celestia Blog, https://blog.celestia.org/roadmap/ 5. What is Celestia (TIA): A Beginner's Guide - 99Bitcoins, https://99bitcoins.com/cryptocurrency/celestia-review/ 6. Celestia Project Introduction, Team, Financing and News_RootData | RootData, https://www.rootdata.com/projects/detail/Celestia?k=MTk4NA%3D%3D 7. What is Brief History of Celestia Company? - Business Model Canvas Templates, https://businessmodelcanvastemplate.com/blogs/brief-history/celestia-brief-history 8. $TIA Mustafa Al-Bassam and Ismail Khoffi are the | I SEE YOU 1 on Binance Square, https://www.binance.com/en/square/post/20152748418002 9. Celestia: The World's First Modular Blockchain Network—A Game Changer for Blockchain Development | CoinEx Academy, https://www.coinex.com/en/academy/detail/1390-celestia-the-worlds-first-modular-blockchain-networka-game-changer-for-blockchain-development 10. Celestia (TIA) Price Prediction 2026, 2027–2030 | CoinEx Academy, https://www.coinex.com/en/academy/detail/4070-celestia-tia-price-prediction 11. Choosing Your Data Availability Layer - Celestia, Avail, and EigenDA Compared, https://www.eclipselabs.io/blogs/choosing-your-data-availability-layer-celestia-avail-eigenda-compared 12. An overview of the five factors in modular DA design: Celestia, Avail, and EigenDA - Who is the winner? - ChainCatcher, https://www.chaincatcher.com/en/article/2112218 13. Celestia (TIA) Price Prediction 2026-2030: Can Modular Scaling Recover? - Coincub, https://coincub.com/price-prediction/celestia-price-prediction/ 14. Celestia Price: TIA/USD Live Price Chart, Market Cap & News Today | CoinGecko, https://www.coingecko.com/en/coins/celestia 15. Unstoppable Celestia: everything you need to know about the TIA cryptocurrency tokenomics | The Cryptonomist on Binance Square, https://www.binance.com/en/square/post/2821174689577 16. Polychain sells remaining $62.5 million TIA stake to Celestia Foundation ahead of staking reward changes | The Block, https://www.theblock.co/post/364155/polychain-sells-remaining-62-5-million-tia-stake-to-celestia-foundation-amid-criticism-of-staking-reward-sales 17. Celestia, Polychain, and the Unlock Strategy: What It Means for Governance and Market Stability | OKX, https://www.okx.com/learn/celestia-polychain-unlock-governance-market 18. Polychain Exits Celestia with US$62.5M Token Sale Amid Investor Scrutiny, https://cryptonews.com.au/news/polychain-exits-celestia-with-us62-5m-token-sale-amid-investor-scrutiny-130064/ 19. Network upgrade coordination - Celestia Documentation, https://docs.celestia.org/operate/maintenance/network-upgrades/ 20. Introducing the Matcha upgrade: towards 128MB blocks - Celestia Blog, https://blog.celestia.org/matcha/ 21. Staking, governance, & supply - Celestia Documentation, https://docs.celestia.org/learn/TIA/staking-governance-supply/ 22. Celestia Vision 2.0: every market onchain, https://blog.celestia.org/celestia-vision-2-0-every-market-onchain/ 23. Introducing Fibre: 1Tb/s of blockspace - Celestia Blog, https://blog.celestia.org/introducing-fibre-1tb-s-of-blockspace/ 24. What is Celestia? (Beginner's Guide 2026) - CoinLedger, https://coinledger.io/learn/what-is-celestia 25. Celestia Genesis Airdrop In TIA - Coinpri, https://coinpri.com/news/cryptocurrency/celestia-genesis-airdrop-in-tia/ 26. Celestia's Competitive Edge in Data Availability: A Deep Dive - BlockEden.xyz, https://blockeden.xyz/blog/2026/01/16/celestia-blob-economics-data-availability-rollup-costs/ 27. Understanding the 'DA Competition' that will determine Ethereum's future in one article: Who will be the ultimate winner among Celestia, EigenDA, and Avail? - BlockBeats, https://m.theblockbeats.info/en/news/50338 28. Who Owns Celestia Company? - Business Model Canvas Templates, https://businessmodelcanvastemplate.com/blogs/owners/celestia-who-owns 29. Celestia - 2026 Company Profile, Team, Funding & Competitors - Tracxn, https://tracxn.com/d/companies/celestia/__e9lFtoe2JngZ2Ws_0uK2xeTpXSMEiWtTAKGnUkbpcCc 30. Token distribution and fundraising models: an overview - Blog, https://blog.bcas.io/token-distribution-and-fundraising-models 31. What is Celestia (TIA) : A Comprehensive Overview - Imperator.co, https://www.imperator.co/resources/blog/celestia-blockchain-presentation 32. Alt DA Solutions Changing the Cost Game for L2 Rollups: Spotlight on Key Players - Zeeve, https://www.zeeve.io/blog/alt-da-solutions-changing-the-cost-game-for-l2-rollups-spotlight-on-key-players/ 33. Celestia Ecosystem Airdrop - Bitget, https://www.bitget.com/airdrop/celestia-ecosystem 34. Celestia (TIA) Price Prediction 2026, 2027-2030 - KuCoin, https://www.kucoin.com/blog/celestia-tia-price-prediction-2026-2030-modular-future 35. Mainnet Beta - Celestia Documentation, https://docs.celestia.org/operate/networks/mainnet-beta/ 36. Introducing the Ginger upgrade: faster finality, higher throughput - Celestia Blog, https://blog.celestia.org/ginger/ 37. Announcing mamo-1: Celestia's 128MB block testnet, https://blog.celestia.org/mamo-1/ 38. Celestia Blog (Page 2), https://blog.celestia.org/page/2/ 39. CIPs/cips/README.md at main · celestiaorg/CIPs - GitHub, https://github.com/celestiaorg/CIPs/blob/main/cips/README.md 40. How Much Did Celestia Raise? Funding & Key Investors | Clay, https://www.clay.com/dossier/celestia-funding 41. Celestia (TIA) - All information about Celestia ICO (Token Sale) - ICO Drops, https://icodrops.com/celestia/ 42. Celestia TIA Fundraising, Investors & Funding Rounds | DropsTab, https://dropstab.com/coins/celestia/fundraising 43. Celestia (None) Price, Investors & Funding, Charts, Market Cap | Chain Broker, https://chainbroker.io/projects/celestia/ 44. Celestia Foundation nabs $100M for modular blockchain network - SiliconANGLE, https://siliconangle.com/2024/09/24/celestia-foundation-nabs-100m-modular-blockchain-network/ 45. Celestia Foundation raises $100 million in a round led by Bain Capital Crypto | The Block, https://www.theblock.co/post/317768/celestia-foundation-raises-100-million-in-a-round-led-by-bain-capital-crypto 46. Celestia Raises $100M, TIA Token Jumps 17% Overnight - CryptoRank, https://cryptorank.io/news/feed/b7c5f-celestia-raises-100m-tia-token-jumps-17-overnight 47. Celestia Redeems TIA from Polychain, Revamps Staking Rewards - CryptoRank, https://cryptorank.io/news/feed/7cd0d-celestia-redeems-tia-from-polychain-revamps-staking-rewards 48. Worst Performing Altcoins of 2025: What Went Wrong | Bitget News, https://www.bitget.com/news/detail/12560605126855 49. What is Celestia (TIA): modular blockchains for a scalable future | OKX, https://www.okx.com/learn/what-is-celestia-tia-modular-blockchains-for-a-scalable-future 50. Initiating Genesis Drop - Celestia Blog, https://blog.celestia.org/genesis-drop/ 51. Celestia Ecosystem - Airdrop Alert, https://airdropalert.com/airdrops/celestia-retroactive/ 52. Saga Genesis Drop is Here, How To Claim Your Free Tokens | Techandtips123 on Binance Square, https://www.binance.com/en/square/post/5118462553609 53. CIPs/cips/cip-029.md at main · celestiaorg/CIPs - GitHub, https://github.com/celestiaorg/CIPs/blob/main/cips/cip-029.md 54. John Adler - Celestia Blog, https://blog.celestia.org/author/john/ 55. The Shwap upgrade: 12x faster DA sampling - Celestia Blog, https://blog.celestia.org/shwap/ 56. Celestia Raises $100 Million Ahead of $1 Billion Token Unlock | The Defiant, https://thedefiant.io/news/blockchains/celestia-raises-usd100-million-ahead-of-usd1-billion-token-unlock 57. Celestia: Token Holder Income Statement - Analytics Dashboard - Blockworks, https://blockworks.com/analytics/celestia/celestia-financials/celestia-token-holder-income-statement 58. Latest Celestia News - (TIA) Future Outlook, Trends & Market Insights - CoinMarketCap, https://coinmarketcap.com/cmc-ai/celestia/latest-updates/ 59. Solana Ecosystem Report (H1 2025) — Earnings & Growth - Helius, https://www.helius.dev/blog/solana-ecosystem-report-h1-2025
