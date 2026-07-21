Laporan Intelijen Kripto: Analisis Komprehensif Protokol Aave (Crypto Intelligence Framework - CIF)

## 1 Executive Summary

Entitas Utama: Aave (sebelumnya ETHLend)

Pendiri Utama: Stani Kulechov

Tanggal TGE LEND: 31 Desember 2017

Tanggal Migrasi AAVE: Oktober 2020

Akumulasi Deposit Historis: $3,460,000,000,000

Akumulasi Pinjaman Historis: $1,000,000,000,000

Pangsa Pasar Pinjaman DeFi (Maret 2026): 59.79%

Pendapatan Bersih Protokol (Tahun 2025): $141,800,000

Status Keamanan: Pemulihan sukses pasca-eksploitasi rsETH Kelp DAO April 2026

Aave merupakan salah satu protokol keuangan terdesentralisasi (DeFi) terbesar dan paling dominan di dunia dalam sektor pinjam-meminjam aset kripto non-kastodian. Berawal dari platform peer-to-peer (P2P) bernama ETHLend pada tahun 2017, proyek ini melakukan pivot arsitektur fundamental menuju model kolam likuiditas bersama (pooled liquidity) peer-to-contract (P2C) pada tahun 2020 yang melahirkan nama Aave. Dengan memperkenalkan primitif terobosan seperti Flash Loans, pergantian suku bunga dinamis, eMode, dan struktur modular Hub-and-Spoke pada Aave V4, protokol ini berhasil mengamankan pangsa pasar mayoritas di atas 59% dalam segmen pasar uang on-chain. Kinerja keuangan Aave menunjukkan lintasan pertumbuhan eksponensial, didukung oleh arus kas riil dari biaya pinjaman, reserve factors, pencetakan stablecoin GHO, dan pasar institusional Aave Horizon.

Terlepas dari stres sistemik yang dialami akibat eksploitasi jembatan rsETH Kelp DAO senilai $292,000,000 pada 18 April 2026, sistem proteksi modular Aave yang dikombinasikan dengan inisiatif DeFi United berhasil memulihkan solvabilitas penuh tanpa kerugian depositor jangka panjang. Pengesahan proposal tata kelola transformatif "Aave Will Win" pada April 2026 yang mengalokasikan 100% pendapatan produk ke perbendaharaan DAO dan mengaktifkan program pembelian kembali (buyback) otomatis senilai $50,000,000 per tahun memantapkan posisi token AAVE sebagai salah satu aset produktif dengan mekanisme penangkapan nilai paling matang di industri.

## 2 Industry Background

Kondisi industri kripto pada periode 2017 didominasi oleh spekulasi liar yang didorong oleh Initial Coin Offering (ICO). Sebagian besar proyek yang menggalang dana triliunan rupiah berada pada tahap pra-produk dengan model bisnis yang belum diuji secara teknis maupun ekonomis. Pada fase ini, infrastruktur dasar keuangan terdesentralisasi (DeFi) hampir tidak ada; pemegang aset kripto tidak memiliki opsi untuk mendapatkan likuiditas selain menjual aset mereka langsung ke pasar, yang memicu konsekuensi pajak yang merugikan dan hilangnya eksposur pasar.

Narasi utama yang berkembang saat itu adalah penciptaan "disintermediasi perbankan" menggunakan desentralisasi P2P. Menanggapi kebutuhan ini, platform pinjam-meminjam generasi pertama mencoba mereplikasi interaksi perbankan konvensional secara kaku. Di bawah model P2P murni, pemberi pinjaman dan peminjam harus menyepakati secara manual jumlah pinjaman, suku bunga, jangka waktu, dan jaminan. Hal ini mengakibatkan inefisiensi pencocokan yang ekstrem, likuiditas yang terfragmentasi, dan biaya gas transaksi yang sangat besar karena setiap interaksi membutuhkan beberapa langkah transaksi on-chain.

Aave (sebagai ETHLend) lahir pada waktu ini untuk memecahkan kebuntuan likuiditas tersebut. Namun, seiring runtuhnya gelembung ICO pada tahun 2018 dan munculnya konsep pembuat pasar otomatis (AMM) serta kolam likuiditas peer-to-contract (P2C) yang dipelopori oleh Compound, model P2P murni terbukti tidak dapat berskala. Kesadaran akan keterbatasan teknologi ini mendorong tim pengembang di bawah Stani Kulechov untuk melakukan rekayasa ulang protokol secara radikal guna membangun kolam likuiditas bersama yang dapat diakses secara instan.

## 3 Project Origin

Gagasan awal pembentukan proyek ini berasal dari Stani Kulechov, seorang mahasiswa hukum di University of Helsinki, Finlandia. Kulechov telah mempelajari pemrograman sejak usia 12 tahun menggunakan PHP dan kemudian Ruby on Rails, yang memberikannya pemahaman mendalam mengenai pengembangan aplikasi web. Di tengah studinya, ketertarikan Kulechov pada regulasi keuangan dan hukum komersial membawanya meneliti efisiensi perjanjian kontrak. Penemuan dokumen Ethereum Whitepaper mengkristalkan kesadarannya bahwa teknologi smart contract dapat digunakan untuk mengeksekusi perjanjian keuangan yang tidak dapat diubah (immutable) tanpa membutuhkan faktor kepercayaan pada pihak ketiga.

Proyek ini resmi didirikan di London, Inggris, pada 1 Mei 2017 dengan nama awal ETHLend. Whitepaper pertama dirilis pada 15 Juni 2017. Untuk membangun proyek ini, Kulechov mengumpulkan sekelompok tim pengembang, desainer, dan pemasar awal:

Stani Kulechov: Pendiri dan CEO, yang memimpin visi strategis dan teknis protokol.

Jordan Lazaro Gustave: Chief Operating Officer (COO), bergabung pada Mei 2017, memiliki latar belakang pendidikan sosiologi politik internasional dan manajemen risiko dari Paris Nanterre University.

Nolvia Serrano: Chief Marketing Officer (CMO), yang mengarahkan strategi komunikasi pemasaran dan keterlibatan komunitas awal.

Anastasija Plotnikova: Pengembang Bisnis (Business Developer), yang mengelola kemitraan ekosistem awal.

Martin Wichmann: Manajer Pertumbuhan (Growth Manager).

Jitendra Chittoda: Arsitek Blockchain (Blockchain Architect).

Anthony Akentiev: Insinyur Blockchain (Blockchain Engineer).

Tujuan awal mereka adalah menciptakan pasar pinjam-meminjam global yang menghilangkan sekat batas negara. Namun, setelah model P2P awal mereka hanya memproses volume pinjaman yang sangat kecil di tengah bear market 2018-2019, tim memutuskan untuk bermigrasi sepenuhnya ke model kolam likuiditas bersama (liquidity pool model). Pada akhir tahun 2018, proyek ini resmi melakukan rebranding menjadi Aave (berarti "hantu" dalam bahasa Finlandia, mencerminkan likuiditas transparan yang tak terlihat namun selalu hadir).

## 4 Innovation Analysis

Aave merupakan inovator garda depan (first mover) yang secara konsisten memperkenalkan fungsionalitas baru yang kemudian diadopsi sebagai standar industri pasar uang terdesentralisasi. Keberhasilan Aave didorong oleh inovasi-inovasi berikut:

Penemuan Flash Loans (Januari 2020): Aave memelopori mekanisme pinjaman tanpa jaminan pertama di dunia yang memanfaatkan atomisitas transaksi blockchain. Dengan mengandalkan sifat eksekusi Ethereum yang akan membatalkan seluruh transaksi jika pengembalian pinjaman gagal dilakukan dalam satu blok smart contract yang sama, Flash Loans mendemokratisasi akses ke modal arbitrase tanpa batas bagi siapa saja.

Fitur Rate Switching (Desember 2020): Aave memperkenalkan fungsionalitas unik yang memungkinkan peminjam secara fleksibel berpindah antara suku bunga variabel (berubah dinamis berdasarkan kegunaan kolam) dan suku bunga stabil (yang dijamin kepastian biayanya dalam jangka waktu tertentu), memberikan alat perlindungan risiko suku bunga bagi para pedagang leverage.

Struktur Interest-Bearing aTokens (Januari 2020): Berbeda dengan model Compound yang menggunakan cTokens (di mana bunga ditambahkan ke nilai tukar aset), aTokens Aave selalu dipatok dengan rasio 1:1 terhadap aset dasar di dompet pengguna. Saldo aToken bertambah secara real-time langsung di alamat dompet penyetor, menyederhanakan perhitungan bunga dan mempermudah integrasi dApp pihak ketiga.

Delegasi Kredit (Credit Delegation): Diperkenalkan pada V2, fitur ini memungkinkan pengguna mengunci jaminan mereka di Aave, lalu mendelegasikan batas kredit mereka ke alamat pihak ketiga tepercaya untuk ditarik tanpa jaminan tambahan, membuka jembatan pertama pinjaman tanpa jaminan bagi korporasi.

Meskipun konsep kolam likuiditas dipopulerkan lebih dulu oleh Compound, eksekusi inovasi Aave yang agresif menjadikannya pemimpin pasar sejati yang mengubah lanskap DeFi dari sekadar spekulasi ritel menjadi pasar uang berbasis kegunaan riil.

## 5 Technology Evolution

Arsitektur smart contract Aave dikembangkan dalam empat iterasi besar untuk merespons kebutuhan keamanan, biaya gas, dan skalabilitas lintas rantai (multi-chain):

Era ETHLend (2017): Beroperasi menggunakan sekumpulan smart contract P2P yang terdesentralisasi namun kaku, di mana dana jaminan dikunci langsung dalam alamat escrow kontrak untuk dicocokkan dengan pemberi pinjaman tunggal.

Aave V1 (Januari 2020): Peluncuran arsitektur kolam likuiditas bersama (shared liquidity pool) di Ethereum Mainnet. Logika smart contract mengandalkan kolam tunggal terpadu untuk mendistribusikan bunga proporsional kepada semua penyetor melalui pencetakan aTokens perdana dan implementasi logika Flash Loans dasar.

Aave V2 (Desember 2020): Optimalisasi arsitektur penghematan biaya gas transaksi sebesar 15% hingga 20%. Fitur baru diintegrasikan di tingkat smart contract untuk mendukung "Flash Liquidation" (likuidasi dalam satu transaksi menggunakan jaminan yang dilelang) dan swap jaminan langsung tanpa perlu menarik aset terlebih dahulu.

Aave V3 (Maret 2022 / Januari 2023): Membawa desain multi-chain terintegrasi. V3 memperkenalkan "Efficiency Mode" (eMode) yang memungkinkan LTV hingga 98% untuk aset dengan korelasi harga tinggi (seperti stETH terhadap ETH). V3 juga menyertakan "Isolation Mode" untuk memisahkan risiko likuidasi aset baru yang belum stabil ke dalam wadah terisolasi, serta "Portals" yang memfasilitasi minting/burning aTokens lintas rantai menggunakan jembatan tepercaya.

Aave V4 (Maret 2026): Peluncuran arsitektur modular "Hub-and-Spoke" di Ethereum Mainnet. Logika kontrak memisahkan "Core Liquidity Hub" (yang menangani penyimpanan likuiditas terpadu, pencegahan fragmentasi, dan akuntansi on-chain global) dari "Spokes" pengguna (kontrak antarmuka modular khusus untuk pasar ritel, institusi, atau eMode tertentu). Struktur V4 diatur oleh komponen smart contract utama sebagai berikut:

Hub (Hub.sol): Kontrak inti tanpa penyimpanan status (stateless) yang bertindak sebagai mesin kalkulasi utama protokol.

HubStorage (HubStorage.sol): Kontrak abstrak khusus yang mendefinisikan tata letak memori penyimpanan global.

HubConfigurator (HubConfigurator.sol): Kontrak admin untuk menyesuaikan konfigurasi parameter aset global.

Spoke (Spoke.sol): Gerbang transaksi pengguna yang terhubung langsung ke Hub pusat.

SpokeStorage (SpokeStorage.sol): Menyimpan peta jaminan, utang, dan indeks cadangan spesifik spoke.

SpokeConfigurator (SpokeConfigurator.sol): Kontrak admin untuk memodifikasi parameter parameter risiko spoke.

GiverPositionManager.sol: Mengontrol penyetoran jaminan dan pelunasan utang.

TakerPositionManager.sol: Menangani penarikan dan peminjaman berbasis tanda tangan izin EIP-712.

SignatureGateway.sol: Gerbang eksekusi transaksi tanpa gas (meta-transactions) menggunakan maksud pengguna yang ditandatangani (signed intents).

NativeTokenGateway.sol: Menangani pembungkusan (wrapping) otomatis ETH asli menjadi WETH untuk interaksi dengan kolam Hub.

## 6 Funding Intelligence

Struktur pendanaan Aave bertransisi dari pengumpulan dana publik ritel (ICO) pada tahun 2017 ke keterlibatan institusi modal ventura papan atas yang membantu memperkuat posisi tawar protokol di kalangan korporasi. Seluruh sejarah putaran pendanaan Aave dirinci di bawah ini:

Funding Round: Initial Coin Offering (ICO)

Start Date: 25 November 2017

End Date: 30 November 2017

Amount Raised: $17,860,000

Discrepancy: Beberapa database mencantumkan angka penggalangan dana sebesar $16,200,000 atau $17,000,000

ICO Price: $0.0173 per LEND (0.000043 ETH)

Presale Discount: 20% bonus alokasi

Funding Round: Series A (Over-the-Counter Round)

Date: 9 Juli 2020

Amount Raised: $4,500,000 (diikuti putaran tambahan sebesar $3,000,000 pada 15 Juli 2020, menghasilkan total Series A sebesar $7,500,000)

Lead Investors: ParaFi Capital, Framework Ventures

Participants: Three Arrows Capital

Funding Round: Series B

Date: 12 Oktober 2020

Amount Raised: $25,000,000 (beberapa pelacak modal ventura mencatat akumulasi putaran ekuitas senilai $29,500,000)

Lead Investors: Standard Crypto, Blockchain Capital, Blockchain.com Ventures

Participants: Three Arrows Capital, SWS Venture Capital, 2020 Ventures, Blockchain Coinvestors

Funding Round: Later Stage VC (Multiple Strategic Placements)

Date: 18 Desember 2024

Amount Raised: $31,000,000

Participants: Apollo Crypto dan sekelompok manajer investasi swasta

Total Capital Raised to Date: $75,500,000

INKONSISTENSI: Terdapat data yang saling bertentangan mengenai status hukum perolehan dana awal. Dokumen resmi aavenomics menyatakan bahwa 13,000,000 AAVE diberikan kepada pemegang LEND (81.25%) dan 3,000,000 AAVE disimpan dalam Ecosystem Reserve (18.75%). Namun, visualisasi data alokasi publik dari CryptoRank mencatat pembagian berupa Private Sale 72.3%, Ecosystem Reserve 23.1%, dan Public Sale 4.6%. Evidence Level: LOW.

## 7 Community Intelligence

Pada masa rintisan ETHLend, Stani Kulechov secara personal membangun basis pengguna pertamanya dengan hadir langsung di saluran obrolan Telegram untuk menjawab keraguan teknis dan hukum komunitas. Namun, strategi pertumbuhan massal Aave tercapai ketika protokol mengintegrasikan program insentif pertambangan likuiditas (liquidity mining) berskala besar yang didanai bersama oleh jaringan blockchain pihak ketiga:

Kampanye Skalabilitas Polygon PoS (Mei 2021): Aave menyebarkan pasarnya di Polygon didukung oleh alokasi hadiah token MATIC senilai $200,000,000 selama satu tahun. Kampanye ini berhasil menarik ribuan pengguna ritel baru karena biaya transaksi yang hampir nol, memicu lonjakan TVL hingga di atas $1,000,000,000 dalam tempo tiga bulan.

Program Avalanche Rush (Oktober 2021): Aave bekerja sama dengan Avalanche Foundation untuk mendistribusikan hadiah penambangan likuiditas berupa token AVAX senilai $20,000,000 kepada para pengguna protokol. Dampaknya sangat instan; TVL pasar Avalanche Aave melesat melewati angka $3,300,000,000 dalam waktu kurang dari satu minggu pasca-peluncuran.

Konsolidasi Komunitas lewat ACI (30 November 2022): Komunitas Aave mengoordinasikan suara dan strategi operasionalnya melalui peluncuran Aave Chan Initiative (ACI) yang dipimpin oleh delegat utama Marc Zeller. ACI mengelola integrasi harian dApp, pengusulan parameter risiko baru, dan kampanye loyalitas berbasis Merit yang menyederhanakan onboarding integrasi mitra.

## 8 Narrative Intelligence

Keunggulan sistemik Aave terletak pada kelincahan protokol untuk mendominasi, mengadopsi, bahkan menciptakan tren narasi baru di industri kripto:

Narasi FinTech & Disintermediasi Kredit (2017-2018):ETHlend mengikuti narasi inklusi keuangan global menggunakan teknologi desentralisasi P2P. Saat menyadari bahwa model ini terlalu lambat, tim dengan cepat beralih menghindari kepunahan akibat kegagalan narasi.

Narasi DeFi Blue Chip & Yield Farming (2020-2021): Memperkenalkan aTokens dan Flash Loans yang menjadi fondasi komposabilitas DeFi, menetapkan standar nilai TVL sebagai tolok ukur kesuksesan ekosistem.

Narasi Ekosistem Multi-chain & L2 Expansion (2021-2022): Menjadi dApp pertama yang memicu adopsi massal jaringan Polygon dan Avalanche, mendistribusikan likuiditas secara cerdas tanpa bergantung murni pada Ethereum Mainnet.

Narasi Real-World Assets (RWA) & Institusi (2025-2026): Aave mendirikan platform Horizon RWA pada Agustus 2025. Horizon mengizinkan institusi tepercaya menyetor Treasuries AS yang ditokenisasi (seperti sUSG, USTB, dan JAAA) sebagai jaminan untuk meminjam stablecoin berizin. Langkah ini berhasil menyerap miliaran dolar modal institusional.

Narasi Token Produktif Didukung Arus Kas Riil (2026): Melalui implementasi kerangka kerja tata kelola "Aave Will Win" (AWW) pada April 2026, Aave mematikan narasi bahwa token tata kelola DeFi tidak memiliki hak ekonomi atas protokol dasar. Dengan menyalurkan 100% pendapatan operasional produk ke kas DAO untuk mendanai buyback, Aave menetapkan babak baru narasi utilitas token terdesentralisasi.

## 9 Competitive Landscape

Lanskap kompetitif Aave terus berkembang di setiap siklus DeFi, ditandai oleh pergeseran keunggulan kompetitif yang dinamis:

Persaingan Compound vs. Aave (2020-2021): Compound adalah pemimpin awal berkat inisiasi yield farming COMP pada pertengahan 2020. Namun, manajemen Compound sangat konservatif dalam penambahan daftar aset baru dan lambat mengeksekusi migrasi multi-chain. Aave merebut posisi nomor satu berkat penambahan jaminan inovatif yang cepat, peluncuran Flash Loans perdana, serta integrasi multi-chain yang sangat agresif. Pada awal 2026, pinjaman aktif Compound menyusut menjadi hanya $547,900,000, berbanding terbalik dengan Aave yang mendominasi di angka $16,550,000,000.

Persaingan Generasional Modern (Morpho & Fluid vs. Aave): Memasuki 2025-2026, Morpho menantang dominasi Aave dengan menawarkan efisiensi modal pencocokan peer-to-peer di atas kolam likuiditas Aave. Aave membalas ancaman ini dengan eMode pada V3, dan akhirnya merilis V4 modular yang menyatukan seluruh likuiditas di satu Hub untuk menyamai efisiensi modal Morpho sekaligus melindungi depositor dari risiko korelasi aset tunggal.

Persaingan Berbasis Arsitektur Ekonomi (Dolomite vs. Aave): Dolomite bersaing menawarkan imbal hasil yang lebih efisien bagi pemegang token melalui pemisahan arsitektur tiga token (3-token model). Meskipun demikian, Aave mempertahankan dominasi mutlak berkat reputasi merek, likuiditas yang sangat dalam, integrasi dengan puluhan jaringan blockchain, serta jaminan keselamatan asuransi on-chain yang matang.

## 10 Product Evolution

Lini produk Aave bertransformasi dari platform pinjam-meminjam sederhana menjadi ekosistem solusi likuiditas terintegrasi:

Platform Pasar Uang Inti (Core Lending Market): Pivot dari platform pencocokan P2P ETHLend ke kolam likuiditas bersama di V1, V2, dan V3. Menyediakan pasar pinjaman umum dan pasar terisolasi untuk aset berisiko.

Native Stablecoin GHO: Diluncurkan pada Juli 2023, GHO dicetak langsung oleh pengguna terhadap posisi jaminan yang didepositkan di Aave V3/V4. Keunikan mekanis GHO adalah tidak adanya pihak penyedia likuiditas pasif; seluruh bunga pinjaman yang dibayarkan oleh peminjam GHO mengalir 100% sebagai pendapatan bersih ke kas perbendaharaan DAO.

Modul Keselamatan Umbrella (Umbrella Safety Module): Diluncurkan pada 5 June 2025 untuk merombak sistem asuransi Safety Module konvensional. Umbrella menerapkan sistem brankas ERC-4626 terisolasi yang mengizinkan pengguna menyetor aset produktif mereka (seperti aUSDC, aUSDT, aWETH) untuk bertindak sebagai pelapis jaminan kerugian pertama (first-loss backstop) terhadap bad debt pada aset spesifik. Slashing pada Umbrella dipicu secara otomatis oleh smart contract jika bad debt on-chain terdeteksi melebihi batas offset tanpa membutuhkan persetujuan manual voting tata kelola.

sGHO Savings Vault: Dirilis pada 3 April 2026, produk tabungan berbasis standar ERC-4626 ini menawarkan Aave Savings Rate (ASR) tetap sebesar 4.25% APR (stabil 50 basis poin di atas Sky Savings Rate) guna menarik depositor ritel.

Aave Horizon: Diluncurkan pada 27 Agustus 2025, pasar pinjaman stablecoin berizin khusus untuk lembaga finansial terakreditasi yang menyetor Treasuries AS yang ditokenisasi sebagai jaminan.

Aave App: Aplikasi mobile konsumen terpadu yang menggabungkan fitur fiat ramp, self-custody, dan lending untuk menyasar adopsi satu juta pengguna baru.

## 11 Tokenomics Intelligence

Sistem tata kelola dan ekonomi token Aave direstrukturisasi untuk memaksimalkan akumulasi nilai bagi pemegang token:

Konversi Pasokan Awal: Migrasi token LEND ke AAVE pada Oktober 2020 membatasi jumlah pasokan keras maksimal sebesar 16,000,000 AAVE (rasio konversi penukaran 100:1 dari pasokan asli 1,3 miliar LEND).

Alokasi Pasokan Token Asli (Aave Document):

Penukaran Pemegang LEND: 13,000,000 AAVE (81.25%)

Ecosystem Reserve (Protocol Incentives): 3,000,000 AAVE (18.75%)

Alokasi Internal Alternatif (Aave Utility Token Document):

Core Development Investment: 30%

Enhancing User Experience: 20%

Management and Legal: 20%

Marketing: 20%

Reserve Fund: 10%

Struktur Suku Bunga dan Emisi Harian:

Hadiah stkAAVE: Diturunkan dari 315 AAVE/hari menjadi 260 AAVE/hari (imbal hasil dasar setara 3.25% APY)

Hadiah stkABPT: Diturunkan dari 216 AAVE/hari menjadi 130 AAVE/hari (imbal hasil dasar setara 6.10% APY)

Hadiah stkGHO Legacy SM: 0 AAVE/hari (dinonaktifkan pasca-peluncuran Umbrella)

Suku Bunga sGHO (ASR): 4.25% APR

Struktur Pengurangan Risiko Slashing:

Batas Slashing Maksimal stkAAVE: Diturunkan dari 20% menjadi 10%

Batas Slashing Maksimal stkABPT: Diturunkan dari 20% menjadi 10%

Batas Slashing Maksimal stkGHO Legacy SM: 0% (tidak berisiko)

Mekanisme Buyback Terpadu (Aavenomics 3.0):

Komitmen Pembelian Kembali Tahunan: $50,000,000

Tanggal Aktivasi Permanen: 9 April 2025

Hasil Pembelian Kembali Fase Uji Coba: 94,000+ AAVE token ditarik dari sirkulasi pasar (menggunakan dana sekitar $22,000,000)

## 12 Airdrop & Incentive Intelligence

Aave tidak menerapkan strategi airdrop token gratis retroaktif yang biasa dipraktikkan oleh dApp generasi baru. Kampanye insentif Aave diarahkan secara ilmiah untuk memobilisasi likuiditas on-chain pada rute-rute strategis:

Program Insentif Polygon PoS (Mei 2021): Pembagian hadiah penambangan likuiditas berupa token MATIC senilai $200,000,000 selama satu tahun penuh. Berhasil mendorong TVL di rantai samping melampaui $1 miliar hanya dalam hitungan bulan.

Program Avalanche Rush (Oktober 2021): Alokasi token AVAX senilai $20,000,000 untuk menyokong depositor Aave di Avalanche C-Chain. Berhasil memicu aliran masuk likuiditas yang melampaui $3,3 miliar dalam satu minggu pertama.

Struktur Emisi Umbrella (Juni 2025): Insentif dialokasikan berdasarkan Model Kurva-S dinamis. Jika nilai setoran asuransi staker berada di bawah target likuiditas (targetLiquidity), emisi hadiah akan meningkat hingga maksimal dua kali lipat untuk menarik modal penjamin. Sebaliknya, jika setoran melebihi target, emisi diturunkan secara bertahap demi menekan inflasi token.

Insentif Likuiditas V4 Avalanche (Juli 2026): Penyediaan insentif modal penunjang senilai $15,000,000 dari kas Avalanche untuk mempercepat adopsi struktur modular spoke V4 perdana di luar Ethereum.

## 13 Token Lifecycle Intelligence

Dinamika siklus hidup token AAVE ditandai oleh pergeseran dari volatilitas spekulatif murni menuju penemuan harga berbasis arus kas fundamental:

Fase LEND & Migrasi TGE: LEND mulai ditransaksikan di bursa kripto pada 31 Desember 2017 pasca-ICO. Mengalami volatilitas ekstrem selama bear market 2018-2019 sebelum akhirnya dikonversi menjadi token tata kelola AAVE pada Oktober 2020.

Titik Harga Terendah (All-Time Low): Tercatat di level $26.02 pada 5 November 2020.

Titik Harga Tertinggi (All-Time High): Mencapai rekor tertinggi di level $661.69 (beberapa bursa mencatat $666.86) pada 18 Mei 2021, didorong oleh demam leverage looping yield di era DeFi Summer.

Siklus Koreksi Bearish (2022-2023): Harga runtuh di bawah $70 seiring runtuhnya ekosistem Terra-UST, penutupan Celsius, dan deleveraging paksa pasar. Penghentian darurat pasar V2 pada November 2023 juga sempat memicu koreksi jangka pendek.

Pemulihan & Konsolidasi (2025-2026): Berada di kisaran $89 hingga $100 pada pertengahan 2026. Kepemilikan token terkonsentrasi di mana 100 alamat dompet teratas mengendalikan sekitar 80% pasokan (termasuk kontrak stkAAVE dan Ecosystem Reserve). Walau konsentrasi ini melahirkan risiko monopoli tata kelola, kedalaman likuiditas di pasar CEX teratas (Bybit, Coinbase, BingX, OKX) menyaring efek volatilitas liar.

Valuasi Fundamental Nilai Wajar: Dengan rasio Market Cap terhadap TVL (MC/TVL) yang sangat rendah di level 0.059 (Kapitalisasi Pasar $1.45 miliar berbanding TVL $24.46 miliar) pada April 2026, jaminan nilai intrinsik AAVE dinilai sangat undervalued. Transisi tata kelola "Aave Will Win" memungkinkan analis keuangan menerapkan kerangka Discounted Cash Flow (DCF) tradisional, menyokong analisis institusional dari Standard Chartered yang memproyeksikan target harga $3,500 pada tahun 2030.

## 14 Business Intelligence

Dinamika pertumbuhan operasional bisnis Aave direkam secara rinci melalui serangkaian metrik historis berikut:

Total Value Locked (TVL) Regional:

Peak September 2025: $70,100,000,000

Peak TVL 2025 (Keseluruhan): $75,000,000,000

Akhir Desember 2025: $55,000,000,000

Januari 2026: $57,330,000,000

Februari 2026: $44,940,000,000

Maret 2026 (Token Terminal): $42,340,000,000

Mei 2026 (Koreksi post-rsETH Hack): ~$14,000,000,000

Juni 2026 (Rata-rata): $22,000,000,000

Active Loans (Volume Pinjaman Aktif):

Januari 2026: $23,250,000,000

Februari 2026: $17,790,000,000

Maret 2026: $16,550,000,000

Juni 2026 (Rata-rata): $9,400,000,000

Akumulasi Deposit Aset Historis: $3,460,000,000,000 (per Q2 2026)

Akumulasi Pinjaman Historis: $1,000,000,000,000 (per Q2 2026)

Distribusi Aliran Dana GHO Stablecoin:

Pasokan GHO Februari 2026: $467,530,000 (beberapa pelacak merekam $527,000,000) - Pasokan GHO Mei 2026: $584,000,000

Pasokan GHO Juni 2026: $547,900,000

Akumulasi Pendapatan Bersih GHO (sejak peluncuran): $22,000,000+

Pendapatan Bersih Protokol (DAO Revenue):

Pendapatan Tahunan 2022: $5,220,000

Pendapatan Tahunan 2023: $22,540,000 (+331.54% YoY)

Pendapatan Tahunan 2024: $90,190,000 (+300.15% YoY)

Pendapatan Tahunan 2025: $141,800,000 (+57.25% YoY)

Pendapatan YTD 2026 (Hingga pertengahan Juni): $333,000,000

Aliran Deposit Pasar Institusi Aave Horizon:

Net Deposits Oktober 2025: $250,000,000

Net Deposits Januari 2026: $600,000,000

Net Deposits Februari 2026: $1,000,000,000

Active Loans Juni 2026: $500,000,000

Akumulasi Deposito V4 Ethereum Mainnet:

Maret 2026 (Bulan Rilis): $4,500,000

April 2026: $25,400,000

Mei 2026: $68,300,000

Juni 2026 (Rata-rata): $170,500,000

Akhir Juni 2026: Berhasil melampaui $200,000,000

## 15 Success & Failure Analysis

Evaluasi keberhasilan dan kegagalan operasional Aave dianalisis secara objektif dari perspektif 8 pemangku kepentingan industri:

Viewpoint: Founder (Stani Kulechov)

Verdict: Sukses

Alasan: Berhasil mengubah platform P2P ETHLend yang gagal menjadi pilar utama likuiditas DeFi global dengan akumulasi kekayaan pribadi diperkirakan mencapai $300,000,000 hingga $500,000,000.

Tingkat Keyakinan: HIGH

Viewpoint: VC (ParaFi, Framework, Standard Crypto)

Verdict: Sukses

Alasan: Mengamankan hak kontrol suara tata kelola yang sangat besar (diperkirakan menguasai 25-35% tata kelola per 2023) didukung oleh pertumbuhan nilai token jaminan investasi awal yang sangat masif.

Tingkat Keyakinan: HIGH

Viewpoint: Retail (Depositor & Peminjam Ritel)

Verdict: Campuran

Alasan: Menikmati akses pinjaman non-kastodian yang transparan dan aman. Namun, ketidakpahaman atas mekanisme suku bunga variabel dan rasio kesehatan LTV sering kali membuat posisi mereka terlikuidasi instan dengan penalti 5% hingga 10%.

Tingkat Keyakinan: MEDIUM

Viewpoint: Community (Aave DAO & ACI)

Verdict: Campuran

Alasan: DAO Aave memiliki sistem pengambilan keputusan paling aktif di dunia. Namun, gesekan keras tata kelola pada Februari-Maret 2026 atas proposal pendanaan "Aave Will Win" mengekspos pemusatan kekuasaan voting (governance drift) oleh whale dan pendiri, memaksa ACI menarik diri dari penanganan harian tata kelola.

Tingkat Keyakinan: HIGH

Viewpoint: Developer (Pengembang Smart Contract)

Verdict: Sukses

Alasan: Memperoleh pustaka kode sumber terbuka (open-source) yang sangat matang dan teruji waktu untuk membangun yield aggregator tanpa memulai dari nol. Walau demikian, kepergian paksa kontributor teknis utama BGD Labs pada April 2026 sempat merugikan pengembangan harian jangka pendek.

Tingkat Keyakinan: HIGH

Viewpoint: Institution (Asset Managers & Fintechs)

Verdict: Sukses

Alasan: Platform Aave Horizon memfasilitasi penempatan dana Treasuries AS yang ditokenisasi untuk mengakses pembiayaan stablecoin berizin secara instan, transparan, dan patuh regulasi.

Tingkat Keyakinan: HIGH

Viewpoint: Validator (Node Operators L2 & Sidechains)

Verdict: Sukses

Alasan: Integrasi ekspansif Aave membawa volume transaksi on-chain yang sangat besar ke rantai-rantai kompatibel EVM, meningkatkan perolehan gas fee bagi validator lokal.

Tingkat Keyakinan: HIGH

Viewpoint: Builder (DeFi Integrators)

Verdict: Campuran

Alasan: Integrasi yield otomatis mempermudah penyerapan likuiditas. Namun, kejadian rsETH Hack April 2026 membuktikan bahwa kelemahan protokol jembatan pihak ketiga yang terintegrasi dapat menyebarkan risiko bad debt sistemik langsung ke pasar pembangun.

Tingkat Keyakinan: HIGH

## 16 Historical Timeline

Berikut adalah garis waktu lengkap perjalanan Aave dari ide awal hingga integrasi multi-chain V4:

1 Mei 2017 — Pendirian Proyek ETHLend oleh Stani Kulechov di London — Eksplorasi pertama pemanfaatan smart contract untuk disintermediasi perbankan.

15 Juni 2017 — Perilisan Dokumen Whitepaper ETHLend — Peletakan dasar konsep peminjaman aset kripto P2P on-chain.

25 November 2017 — Pembukaan Penjualan ICO Publik Token LEND — Penggalangan dana awal yang sukses menghimpun $17,860,000.

September 2018 — Keputusan Rebranding ETHLend Menjadi Aave — Pivot radikal dari arsitektur P2P yang terhambat skalabilitas ke model likuiditas bersama P2C.

8 Januari 2020 — Peluncuran Jaringan Utama (Mainnet) Aave V1 — Pengenalan model kolam bersama, aTokens, serta penciptaan Flash Loans pertama di dunia.

9 Juli 2020 — Pendanaan Seri A OTC Senilai $4.5 Juta Dipimpin ParaFi — Masuknya suntikan modal institusional untuk mempercepat pengembangan fitur V2.

Oktober 2020 — Pelaksanaan Migrasi Token LEND ke AAVE dengan Rasio 100:1 — Konsolidasi pasokan token guna mematangkan struktur nilai tokenomics.

12 Oktober 2020 — Pendanaan Seri B OTC Senilai $25 Juta dari Standard Crypto dkk — Penguatan kepemilikan modal institusional pada tata kelola on-chain Aave.

16 Desember 2020 — Aktivasi Upgrade Protokol Aave V2 di Ethereum — Pengenalan fitur penghematan biaya gas, swap jaminan langsung, dan delegasi kredit.

14 April 2021 — Peluncuran Aave V2 di Jaringan Samping Polygon PoS — Langkah ekspansi multi-chain perdana didukung penambangan likuiditas MATIC senilai $200 juta.

4 Oktober 2021 — Deploi Aave V2 di Avalanche Melalui Program Avalanche Rush — Pendistribusian insentif AVAX senilai $20 juta yang mengamankan TVL $3,3 miliar dalam hitungan hari.

Maret 2022 — Peluncuran Perdana Aave V3 di Enam Jaringan L2 — Pengenalan fitur E-mode, Isolation Mode, dan cross-chain Portal.

30 November 2022 — Pendirian Aave Chan Initiative (ACI) oleh Marc Zeller — Konsolidasi kekuatan tata kelola komunitas untuk mengoordinasikan parameter harian.

27 Januari 2023 — Deploi Resmi Aave V3 di Ethereum Mainnet — Integrasi fungsionalitas efisiensi modal eMode ke dalam kolam likuiditas terbesar.

15 Juli 2023 — Peluncuran Native Stablecoin GHO di Ethereum Mainnet — Integrasi stablecoin terdesentralisasi berbasis jaminan kolam Aave.

5 Juni 2025 — Penerapan Sukses Modul Keselamatan "Umbrella" Secara Global — Penggantian Safety Module lama dengan staking otomatis aToken untuk proteksi bad debt otomatis.

27 Agustus 2025 — Rilis Perdana Pasar RWA Aave Horizon — Kerja sama institusional untuk mengizinkan pembiayaan stablecoin berjaminan dana Treasuries AS yang ditokenisasi.

Desember 2025 — Penutupan Penyelidikan Regulator SEC AS Terhadap Aave — Penghentian investigasi empat tahun oleh SEC AS tanpa denda hukum.

16 Februari 2026 — Pengajuan Konversi ETF Trust Aave oleh Grayscale — Grayscale mendaftarkan konversi produk investasi Aave Trust ke ETF ke regulator SEC AS.

Februari 2026 — Pengajuan Proposal Kerangka Kerja "Aave Will Win" — Proposal kontroversial untuk menyalurkan 100% pendapatan produk ke DAO dan mendanai Labs.

2 Maret 2026 — Proposal "Aave Will Win" Lolos Verifikasi Temp Check — Pemungutan suara awal berhasil disetujui dengan perolehan suara mayoritas tipis 52.58%.

30 Maret 2026 — Aktivasi Aave V4 di Ethereum Mainnet — Transisi resmi ke arsitektur modular Hub-and-Spoke terpadu.

3 April 2026 — Peluncuran sGHO Savings Vault dengan Standar ERC-4626 — Penyediaan imbal hasil tabungan tetap (ASR) sebesar 4.25% APR untuk menarik depositor ritel.

13 April 2026 — Pengesahan Resmi Proposal "Aave Will Win" di Tata Kelola — Persetujuan mayoritas ~75% untuk mentransfer seluruh pendapatan operasional ke kas DAO.

18 April 2026 — Kejadian Eksploitasi rsETH Kelp DAO Senilai $292,000,000 — Kerentanan verifikasi 1-of-1 jembatan LayerZero Unichain-Ethereum memicu pencetakan rsETH tanpa jaminan dasar, yang didepositkan ke Aave untuk membobol pinjaman $190 juta dalam WETH, memicu pembekuan pasar darurat.

6 Mei 2026 — Eksekusi Likuidasi Paksa Posisi Penyerang rsETH Melalui Payload AIP Khusus — Pemulihan sebanyak 106,993 rsETH ke tangan Recovery Guardian guna meminimalisir akumulasi bad debt sistemik.

15 Juli 2026 — Peluncuran Aave V4 di Jaringan Avalanche — Ekspansi multi-chain modular perdana V4 didukung oleh komitmen insentif Avalanche senilai $15 juta untuk pasar kredit RWA.

## 17 Current Status

Protokol Aave saat ini berada dalam kondisi pemulihan yang sangat kuat (recovery) sekaligus ekspansi teknologi yang dinamis pasca-krisis rsETH. Meskipun kepanikan eksploitasi jembatan Kelp DAO pada April 2026 sempat merugikan stabilitas likuiditas harian dan menurunkan TVL kumulatif, kepatuhan teknis penutupan bad debt berjalan sukses. DeFi United (koalisi kontributor papan atas termasuk Lido, Ethena, dan Mantle) berhasil menghimpun cadangan pemulihan senilai lebih dari $318,000,000.

Posisi utang penyerang telah sepenuhnya dilikuidasi pada 6 Mei 2026, memulihkan cadangan sebesar 106,993 rsETH ke dalam Recovery Guardian. Di samping itu, tuntutan hukum federal di New York telah menyepakati transfer dana sitaan jaminan penyerang sebesar 30,765 ETH dari Arbitrum DAO ke entitas Aave untuk mempercepat stabilisasi pasar WETH. Parameter LTV pasar WETH L2 kini telah dinormalisasi penuh ke tingkat pra-eksploitasi.

Di sisi perluasan produk, transisi ke Aave V4 berjalan tanpa hambatan. Peluncuran spoke V4 di Avalanche pada 15 Juli 2026, didukung oleh insentif likuiditas senilai $15,000,000 dan migrasi dana Progmat Jepang senilai ¥452 miliar, memperkokoh kehadiran institusional Aave di luar ekosistem utama Ethereum. Dengan pendapatan YTD 2026 mencapai $333,000,000 dan pengesahan penuh skema buyback $50,000,000 per tahun, posisi neraca keuangan Aave DAO berada pada kondisi paling likuid sepanjang sejarahnya.

## 18 Lessons Learned

Analisis histori pertumbuhan Aave menyisakan beberapa evaluasi mendalam yang berguna bagi perancangan dApp keuangan masa depan:

Batas Keamanan Komposabilitas (Composability Thresholds): Kasus rsETH Hack April 2026 membuktikan bahwa audit smart contract internal tidak menjamin keamanan absolut jika protokol mengizinkan aset sintetis lintas jembatan sebagai jaminan. Mengintegrasikan wrapped-assets membuat ketahanan pasar uang secara tidak langsung bergantung pada kualitas pengoperasian jembatan pihak ketiga. Penggunaan konfigurasi tanda tangan tunggal (1-of-1 DVN) di Kelp Bridge adalah titik kegagalan tunggal yang mengekspos pasar WETH Aave pada risiko bad debt instan. Pelajaran: Jaminan berbasis token jembatan wajib diisolasi menggunakan limit LTV nol secara default sebelum diverifikasi berlapis.

Kebutuhan Proteksi Kerugian Otomatis (Automated Loss Protection): Keberhasilan modul Umbrella membuktikan keunggulan asuransi otomatis on-chain dibandingkan dengan Safety Module lama yang rentan terdepresiasi akibat volatilitas harga token asli. Dengan memanfaatkan setoran aToken produktif yang dikunci langsung sesuai jenis pasar, protokol dapat memotong (slashing) jaminan secara instan saat bad debt terdeteksi di tingkat smart contract tanpa menunggu negosiasi tata kelola.

Mekanisme Penangkapan Nilai yang Enforceable: Mengganti utilitas tata kelola spekulatif dengan hak arus kas operasional protokol secara penuh (seperti skema buyback $50 juta per tahun lewat proposal AWW) terbukti menjadi penangkal utama devaluasi token di tengah bear market, sekaligus membangun reputasi fundamental yang dapat dimodelkan secara matematis oleh lembaga keuangan konvensional.

## 19 Knowledge Extraction Candidate

Bagian ini menyajikan ekstraksi pengetahuan terstruktur untuk memfasilitasi penalaran (reasoning) sistem AI di masa depan:

Daftar Entitas Baru:

Aave V4

Core Liquidity Hub

Specialty Spokes

sGHO Savings Vault

Umbrella Safety Module

Aave Horizon

DeFi United

Kelp rsETH LayerZero Bridge

Ontologi Representasi Pengetahuan (Knowledge Graph Ontology):

[Stani Kulechov] -> founder of -> [ETHLend]

[ETHLend] -> rebranded to -> [Aave]

[Aave] -> developed -> [Aave V4]

[Aave V4] -> implements -> [Hub-and-Spoke Architecture]

[Core Liquidity Hub] -> aggregates -> [Global Liquidity]

[Specialty Spokes] -> isolate -> [Collateral Risk]

[Umbrella Safety Module] -> utilizes -> [aToken Staking]

[Aave Will Win] -> redirects -> [100% Product Revenue]

[sGHO Savings Vault] -> complies with -> [ERC-4626]

[Kelp rsETH Bridge] -> utilized -> [1-of-1 DVN Configuration]

[1-of-1 DVN Configuration] -> enabled -> [rsETH Exploit]

[rsETH Exploit] -> generated -> [Aave Bad Debt]

[DeFi United] -> collateralized -> [Aave Bad Debt Recovery]

Pola Perilaku Finansial & Teknis (Pattern Discovery):

Nama Pola: Transisi Nilai Tata Kelola ke Arus Kas

Rantai Sebab-Akibat: Ketidakpuasan komunitas atas token tata kelola murni -> Penurunan utilitas token akibat emisi jaminan -> Persetujuan fee switch 100% ke kas DAO -> Eksekusi program pembelian kembali (buyback) otomatis -> Penurunan pasokan sirkulasi pasar -> Peningkatan kepercayaan penilaian fundamental berbasis DCF.

Nama Pola: Kerentanan Asosiasi Komposabilitas LST/LRT

Rantai Sebab-Akibat: Penerimaan jaminan token restaking dari rantai sekunder -> Ketergantungan tidak langsung pada infrastruktur jembatan -> Serangan eksploitasi verifikator tunggal jembatan -> Pencetakan token sintetis tanpa jaminan -> Penyetoran token palsu sebagai jaminan pinjaman -> Pembobolan likuiditas aset nyata -> Pembekuan darurat pasar oleh Guardian.

Nama Pola: Penyelamatan Solvabilitas Koalisi DeFi

Rantai Sebab-Akibat: Akumulasi bad debt besar akibat kegagalan eksternal -> Potensi kejatuhan sistemik pasar pinjaman utama -> Pembentukan koalisi protokol terkait (DeFi United) -> Penghimpunan dana talangan dari penerbit jaminan terkait (Lido, Ethena) -> Likuidasi paksa penyerang via payload smart contract khusus -> Pemulihan solvabilitas penuh tanpa kerugian penarikan ritel.

## 20 Transferable Intelligence

Berikut adalah indikator evaluasi umum (rules) yang dapat ditransfer oleh AI untuk mengukur kelayakan protokol pasar uang baru:

Aturan Evaluasi Umum (General Rules):

Aturan Batas MC/TVL DeFi: Setiap protokol pasar uang matang yang menguasai pangsa pasar >40\% di ekosistemnya, dengan rasio Market Cap terhadap TVL di bawah 0,10, serta memiliki komitmen aliran dana operasional riil ke kas DAO, dapat diklasifikasikan sebagai undervalued.

Aturan Filter Verifikasi Jembatan: AI wajib mendeteksi semua aset jaminan yang diperoleh melalui jembatan lintas rantai. Jika verifikasi jembatan tersebut mengandalkan skema multisig di bawah 3-of-5 atau menggunakan validator tunggal (1-of-1 DVN), jaminan tersebut wajib dibatasi nilai LTV-nya sebesar 0\% untuk mencegah risiko bad debt instan.

Aturan Desentralisasi Asuransi Jaminan: Protokol asuransi keselamatan yang efisien dilarang mengandalkan fluktuasi harga token asli protokol sebagai satu-satunya jembatan likuiditas. Perlindungan bad debt wajib beralih menggunakan brankas asuransi terisolasi ERC-4626 berbasis staking aset produktif (aTokens) dengan parameter pemotongan otomatis.

Aturan Khusus (Aave-Specific Metric Rules):

Pengawasan Suku Bunga GHO: AI wajib memantau penyesuaian diskresioner suku bunga pinjaman GHO oleh komite tata kelola Aave, karena laju pembakaran dan pencetakan GHO tidak diatur secara algoritma murni melainkan untuk bersaing dengan suku bunga pasar Sky (SSR).

## 21 Open Questions

Regulasi dan Kepatuhan RWA Lintas Negara: Bagaimana Aave Horizon dapat memitigasi benturan hukum regulasi MiCA Eropa dengan regulasi SEC AS di masa depan saat jaminan RWA yang didepositkan berasal dari yurisdiksi yang saling berseberangan secara hukum?

Enforceabilitas Hukum Kasus "Aave Will Win": Apakah pengalihan pendapatan 100% dari produk komersial Aave Labs memiliki jaminan hukum konvensional yang mengikat (enforceable) bagi pemegang token tata kelola jika terjadi sengketa komersial di tingkat perusahaan induk (Avara)?

Ketahanan Sistem Hub-and-Spoke Terhadap Fragmentasi Non-EVM: Apakah implementasi Spoke modular pada rantai non-EVM berkecepatan tinggi seperti Solana dapat mempertahankan latensi sinkronisasi akuntansi global Hub tanpa menimbulkan risiko tabrakan transaksi (race conditions)?

## 22 Evidence Level

Kinerja Finansial & Neraca Kas DAO (Tingkat Keyakinan: HIGH): Statistik pendapatan tahunan (5,22M pada 2022, 22,54M pada 2023, 90,19M pada 2024, 141,8M pada 2025, dan 333M YTD mid-2026) diperoleh langsung dari data ledger on-chain Token Terminal dan laporan tahunan resmi komite tata kelola.

Rekayasa Teknis rsETH Hack & Pemulihan (Tingkat Keyakinan: HIGH): Kronologi eksploitasi jembatan Kelp DAO, pencurian rsETH, pembobolan pinjaman $190 juta WETH, dan aksi likuidasi paksa penyerang terdokumentasi lengkap melalui verifikasi post-mortem Metrika, Blockonomi, dan draf denda di forum tata kelola.

Status Kepatuhan Investigasi SEC (Tingkat Keyakinan: MEDIUM): Penutupan penyelidikan SEC atas Aave pada Desember 2025 dilaporkan oleh Bloomberg dan database internal, namun dokumen penutupan formal (No-Action Letter) sering kali membawa klausul diskresioner yang dapat dibuka kembali di bawah rezim kepemimpinan regulator yang baru.

Proyeksi Harga AAVE $3,500 pada Tahun 2030 (Tingkat Keyakinan: LOW): Walaupun Standard Chartered menggunakan kerangka model DCF formal, proyeksi ini mengasumsikan pertumbuhan industri DeFi global sebanyak 37 kali lipat tanpa mempertimbangkan risiko black swan makroekonomi eksternal.

## 23 Karya yang dikutip

RootData: Aave Project Calendar and Event Details — https://www.rootdata.com/projects/detail/Aave?k=MTA2

NCBI PMC: Analysis of ICO and Secondary Market Returns — https://pmc.ncbi.nlm.nih.gov/articles/PMC8591750/

Sygnum Research: Learn More About Aave History and Tokenomics — https://www.sygnum.com/research/no-research_topic/learn-more-about-aave/

CoinGecko: Aave (AAVE) Historical Price and Supply — https://www.coingecko.com/en/coins/aave

Coinhouse: Understanding Aave Team and Platform Dynamics — https://www.coinhouse.com/aave

MDPI: Scientific Study on Initial Coin Offerings — https://www.mdpi.com/1911-8074/14/6/232

Tracxn: Aave Company Competitors and Overview — https://tracxn.com/d/companies/aave/__JiXfiPZKVkx7021dCR937XH3M5d2vj-Cy3z3dnIPJ00

Tracxn: Aave Funding and VC Investors Details — https://tracxn.com/d/companies/aave/__JiXfiPZKVkx7021dCR937XH3M5d2vj-Cy3z3dnIPJ00/funding-and-investors

CryptoRank: Aave ICO Token Sale Review — https://cryptorank.io/ico/aave

Sygnum Bank: Digital Asset Banking Group Aave — https://www.sygnum.com/digital-asset-banking/aave/

Business Model Canvas: Aave Ownership Concentration Data — https://businessmodelcanvastemplate.com/blogs/owners/aave-who-owns

PitchBook: Aave Profile, Funding and Valuations — https://pitchbook.com/profiles/company/224491-60

CryptoCompare: LEND to AAVE Migration Guide & SI Rewards — https://resources.cryptocompare.com/asset-management/1724/1713432223585.pdf

CEX.IO Spotlight: Aave V1, V2 and V3 Features — https://blog.cex.io/spotlight/cex-io-spotlight-aave-30225

GitHub: Aavenomics Documentation — https://github.com/aave/aavenomics

Gate Learn: Evolution of Aave from V1 to V3 — https://www.gate.com/learn/articles/aaves-road-to-expansion/293

RootData News: Aave Protocol Modular Evolution — https://www.rootdata.com/news/611373

Gate Learn: From ETHLend to Aave V4 Ecosystem Roadmap — https://www.gate.com/learn/articles/from-ethlend-to-aave-v4-the-building-plan-of-the-leading-lending-ecosystem/3115

ChainCatcher: Aave's Architectural Evolution Panorama — https://www.chaincatcher.com/en/article/2259984

Medium: Understanding Aave, the DeFi Lending Giant — https://medium.com/coinmonks/understanding-aave-the-defi-lending-giant-that-changed-everything-39da0ebdba52

Aave Governance: Aave Labs Contributions Report — https://governance.aave.com/t/aave-labs-contributions-report/24155

Finance Magnates: ETHLend LEND Token ICO Launch — https://www.financemagnates.com/thought-leadership/ethlends-lend-token-raises-10-million-30-minutes/

Caproasia: Aave Founder Mansion and Estonia/Finland Background — https://www.caproasia.com/2026/02/05/uk-2-billion-crypto-lending-platform-aave-founder-stani-kulechov-buys-london-5-level-mansion-in-nottinghill-for-29-9-million-22-million-founded-aave-in-2017-as-ethlend-stani-kulechov-born-in-est/

Coin Bureau: ETHLend LEND Token Review — https://coinbureau.com/review/ethlend-lend

Circle: The Money Movement Episode 33 with Stani Kulechov — https://www.circle.com/the-money-movement/the-money-movement-episode-33-defi-in-2021-an-interview-with-stani-kulechov

CryptoRank: Standard Chartered Aave Price Prediction 2030 — https://cryptorank.io/news/feed/f3dfe-standard-chartered-aave-price-prediction-2030

Gate Blog: Aave V4 Hub-and-Spoke Architecture Reshapes DeFi — https://www.gate.com/blog/aave-v4-how-the-hub-spoke-architecture-reshapes-defi-lending-infrastructure

CryptoRank: Aave V4 Ethereum Mainnet Launch — https://cryptorank.io/news/feed/99f5b-aave-v4-ethereum-mainnet-launch

CoinMarketCap AI: Aave Latest Updates and V4 Security Blueprint — https://coinmarketcap.com/cmc-ai/aave/latest-updates/

KuCoin: Aave V4 Launches on Avalanche and RWA metrics — https://www.kucoin.com/blog/th-aave-v4-launches-on-avalanche-how-the-new-hub-spoke-defi-architecture-and-13-7b-institutional-rwa-influx-impact-avax-price

Aave Governance: Aave V4 Adoption Paths 2026-2028 — https://governance.aave.com/t/aave-v4-adoption-paths/24237

Aave Governance: Aave Labs Development Update April 2026 — https://governance.aave.com/t/al-development-update-april-2026/24821

CoinStats AI: Aave Investment Analysis July 2026 — https://coinstats.app/ai/a/investment-analysis-aave

DefiLlama: Protocol Rankings and Core Metrics — https://defillama.com/

CryptoRank: Aave Surpasses 1 Trillion in DeFi Lending Milestone — https://cryptorank.io/news/feed/dd3af-aave-surpasses-1t-in-defi-lending-milestone

Token Terminal: Aave February 2026 Performance Dashboard — https://tokenterminal.com/explorer/studio/dashboards/f04e3c69-c3a1-47d2-8578-72ddca75d265

Aave Governance: ARFC Aave Will Win Framework — https://governance.aave.com/t/arfc-aave-will-win-framework/24352

Aave Governance: Temp Check Aave Will Win Framework Discussion — https://governance.aave.com/t/temp-check-aave-will-win-framework/24055?page=3

Bitget News: Aave DAO and Aave Labs Governance Dispute Details — https://www.bitget.com/news/detail/12560605219073

21Shares: Update on Aave Governance Crisis & Alignment — https://www.21shares.com/en-eu/insights/update-on-aaves-governance-crisis-alignment-is-on-the-table-enforceability-is-not-yet

Binance Square: Aave Will Win Proposal Passes Temp Check — https://www.binance.com/es-MX/square/post/297343060218225

Metrika Blog: Post-Mortem Kelp DAO Bridge and Aave rsETH Incident — https://www.metrika.co/blog/post-mortem-kelp-aave

DefiPrime: KelpDAO rsETH Exploit and Aave Impact Analysis — https://defiprime.com/kelpdao-rseth-exploit

Bitcoin Foundation: Kelp DAO and Aave Resume rsETH Operations — https://bitcoinfoundation.org/news/defi/kelp-is-back/

Binance Square: Blockonomi Post-Mortem of April 2026 rsETH Incident — https://www.binance.com/en/square/post/329113617407265

The Defiant: Aave Partially Unfreezes WETH After Kelp Bridge Exploit — https://thedefiant.io/news/defi/aave-partially-unfreezes-weth-after-kelp-bridge-exploit

Aave Governance: Restore WETH Loan-to-Value on Aave V3 Markets — https://app.aave.com/governance/v3/proposal/?proposalId=482

Pluang News: Aave Revenue and Standard Chartered Coverage — https://pluang.com/en/news-feed/aave-laporkan-pendapatan-907juta-2025-dan-333juta-ytd-2026-dengan-standar

KuCoin News: Aave Reports 2025/2026 Revenue & Standard Chartered Coverage — https://www.kucoin.com/news/flash/aave-reports-907m-revenue-in-2025-333m-ytd-2026-as-standard-chartered-initiates-coverage

Bitget News: Aave Overall Status & V4 Integration in April 2026 — https://www.bitget.com/news/detail/12560605334565

Binance Square: Aave June 2026 Performance and TVL Analysis — https://www.binance.com/en/square/post/343377067336786

MetaMask: Aave Token Mechanics and V4 Updates — https://metamask.io/price/aave

Eco Support: Aave V4 GHO Yield Borrow-Mint Mechanics Explained — https://eco.com/support/en/articles/15253998-aave-v4-gho-yield-2026-borrow-mint-mechanics-explained

SQ Magazine: Stablecoins Statistics and sGHO Yield 2026 — https://sqmagazine.co.uk/algorithmic-stablecoins-statistics/

Token Terminal: Aave January 2026 Performance Dashboard — https://tokenterminal.com/explorer/studio/dashboards/98aa697c-f0ea-40d5-aa54-3010166c54ab

Pluang News: Aave Revenue Growth and GHO Expansion Plans — https://pluang.com/en/news-feed/aave-rencanakan-pertumbuhan-pendapatan-dan-ekspansi-gho

Etherscan: LEND Token Details and ICO Dates — https://etherscan.io/token/0x80fb784b7ed66730e8b1dbd9820afd29931aab03

Coinchange Blog: Permissioned DeFi and Aave Origins — https://www.coinchange.io/blog/permissioned-defi-paving-the-way-for-exponential-growth

CheckSig: Aave Whitepaper and Roadmaps — https://www.checksig.com/whitepapers/2026-05-04-aave-whitepaper.pdf

Aave FAQ: Safety Module, Cooldown and Slashing details — https://aave.com/faq

Milk Road: Aave Review and Safety Module Risk Analysis — https://milkroad.com/reviews/aave/

Aave Governance: Safety Module Emissions and Shortfall Analysis — https://governance.aave.com/t/discussion-safety-module/12029

Aave Governance: ARFC Safety Module Emission Adjustments — https://app.aave.com/governance/v3/proposal/?proposalId=342

Gate Learn: Avara and Aave Funding Round Details — https://www.gate.com/learn/articles/from-ethlend-to-aave-v4-the-building-plan-of-the-leading-lending-ecosystem/3115

Aavegotchi Medium: Why We Chose Polygon — https://aavegotchi.medium.com/why-aavegotchi-chose-polygon-356238977fb2

CoinMarketCap Academy: Aave Avalanche Rush Incentive Details — https://coinmarketcap.com/academy/article/a-deep-dive-into-avalanche-avax

KuCoin Blog: Aave V3 vs V4 Architecture Comparison — https://www.kucoin.com/id/blog/id-aave-v4-launches-on-avalanche-how-the-new-hub-spoke-defi-architecture-and-13-7b-institutional-rwa-influx-impact-avax-price

Medium: Anatomy of Aave V4 Smart Contracts — https://jeancvllr.medium.com/anatomy-of-the-aave-v4-contracts-364fa3189d04

Pluang News: Aave V4 Ethereum Deposits Double in a Month — https://pluang.com/news-feed/deposit-aave-v4-di-ethereum-capai-200juta-dolar-dalam-sebulan

Aave Blog: Aave 2025 Recap and The Aave Effect — https://aave.com/blog/aave-2025-recap

Aave Governance: ARFC sGHO Launch Configuration & Parameters — https://governance.aave.com/t/arfc-sgho-launch-configuration/24346

Aave Main Website: Metrics and FAQs — https://aave.com/

Aave Governance: ARFC GHO CEX Earn Incentive Program — https://governance.aave.com/t/arfc-gho-cex-earn-incentive-program/22284

GitHub: Aave Umbrella Repository & Specifications — https://github.com/aave-dao/aave-umbrella

Aave Docs: Umbrella Security System & Safety Incentives — https://aave.com/docs/aave-v3/umbrella

Oak Research: Innovations What is Aave Umbrella — https://oakresearch.io/en/analyses/innovations/what-is-umbrella-new-product-from-aave

Aave Governance: ARFC Umbrella Emission Adjustments — https://governance.aave.com/t/arfc-umbrella-emission-adjustments/24415

Aave Docs: Resources Changelog and Deployments — https://aave.com/docs/resources/changelog

Aave Blog: Aave Horizon Institutional RWA Integration — https://aave.com/blog/horizon-built-for-institutions

Stablecoin Insider: Aave Horizon Complete Breakdown — https://stablecoininsider.org/aave-horizon-complete-breakdown-2025/

OKX Learn: How Horizon is Transforming Institutional DeFi — https://www.okx.com/learn/aave-rwa-market-horizon-defi-assets

Karya yang dikutip

1. Aave - Sygnum Bank, https://www.sygnum.com/digital-asset-banking/aave/ 2. Aave Labs Contributions Report - Governance, https://governance.aave.com/t/aave-labs-contributions-report/24155 3. Who Owns Aave Company? - Business Model Canvas Templates, https://businessmodelcanvastemplate.com/blogs/owners/aave-who-owns 4. Aave - Wikipedia, https://en.wikipedia.org/wiki/Aave 5. Aave Project Introduction, Team, Financing and News_RootData | RootData, https://www.rootdata.com/projects/detail/Aave?k=MTA2 6. Aave Price: AAVE/USD Live Price Chart, Market Cap & News Today | CoinGecko, https://www.coingecko.com/en/coins/aave 7. CEX.IO Spotlight: Aave - Bitcoin & Crypto Trading Blog, https://blog.cex.io/spotlight/cex-io-spotlight-aave-30225 8. Aave, https://aave.com/ 9. Aave Surpasses $1T in DeFi Lending Milestone - CryptoRank, https://cryptorank.io/news/feed/dd3af-aave-surpasses-1t-in-defi-lending-milestone 10. Aave (AAVE) - Investment Analysis July 2026 | CoinStats AI, https://coinstats.app/ai/a/investment-analysis-aave 11. AAVE Price Prediction 2026, 2027 and 2030: Is Aave Ready to Skyrocket to ATH? - Bitget, https://www.bitget.com/news/detail/12560605334565 12. Kelp DAO, Aave Resume rsETH Operations After $292M Hack - Bitcoin Foundation, https://bitcoinfoundation.org/news/defi/kelp-is-back/ 13. Aave's April 2026 rsETH Incident Post Mortem: How a Forged Bridge Message Shook DeFi | Blockonomi on Binance Square, https://www.binance.com/en/square/post/329113617407265 14. Dashboard - Aave February 2026 Report - Token Terminal, https://tokenterminal.com/explorer/studio/dashboards/f04e3c69-c3a1-47d2-8578-72ddca75d265 15. From ETHLend to Aave V4: Evolution of the Leading DeFi Lending Protocol | Gate Learn, https://www.gate.com/learn/articles/from-ethlend-to-aave-v4-the-building-plan-of-the-leading-lending-ecosystem/3115 16. In-depth Exploration: The Evolution of Decentralized Lending: From Monolithic Capital Pools to Unified Liquidity Layers and Agnostic Primitives - ChainCatcher, https://www.chaincatcher.com/en/article/2259984 17. DeFi Weekly: Aave — The DeFi Lending Giant That Changed Everything | by Ferdi Kurt | Coinmonks | Medium, https://medium.com/coinmonks/understanding-aave-the-defi-lending-giant-that-changed-everything-39da0ebdba52 18. AAVE's Road to Expansion: Protocol Evolution from V1 to V3 | Gate Learn, https://www.gate.com/learn/articles/aaves-road-to-expansion/293 19. Aave V4: How the Hub-and-Spoke Architecture Is Reshaping DeFi Lending Infrastructure, https://www.gate.com/blog/aave-v4-how-the-hub-spoke-architecture-reshapes-defi-lending-infrastructure 20. Aave Reports $907M Revenue in 2025, $333M YTD 2026 as Standard Chartered Initiates Coverage | KuCoin, https://www.kucoin.com/news/flash/aave-reports-907m-revenue-in-2025-333m-ytd-2026-as-standard-chartered-initiates-coverage 21. The Kelp-Aave Incident: What the On-Chain Data Tells Us About DeFi's Risk Infrastructure Gap | Metrika Blog, https://www.metrika.co/blog/post-mortem-kelp-aave 22. The KelpDAO rsETH Exploit: $292M Minted From a 1-of-1 Bridge - DeFi Prime, https://defiprime.com/kelpdao-rseth-exploit 23. Aave Price is $89.55 today. See AAVE price chart and stats - MetaMask, https://metamask.io/price/aave 24. ICO investors - PMC - NIH, https://pmc.ncbi.nlm.nih.gov/articles/PMC8591750/ 25. STO vs. ICO: A Theory of Token Issues under Moral Hazard and Demand Uncertainty - MDPI, https://www.mdpi.com/1911-8074/14/6/232 26. Track token migrations - CoinTracker Personal, https://support.cointracker.io/hc/en-us/articles/4413071292433-Track-token-migrations 27. Who is Stani Kulechov? - Bitstamp, https://www.bitstamp.net/en-gb/learn/people-profiles/stani-kulechov/ 28. Aave (AAVE) Price Prediction 2026, 2027–2030 | CoinEx Academy, https://www.coinex.com/en/academy/detail/2838-aave-price-prediction 29. Learn more about Aave - Sygnum Bank, https://www.sygnum.com/research/no-research_topic/learn-more-about-aave/ 30. The Money Movement Ep 33: DeFi in 2021 with Stani Kulechov | Circle, https://www.circle.com/the-money-movement/the-money-movement-episode-33-defi-in-2021-an-interview-with-stani-kulechov 31. Permissioned DeFi: A Pathway to Exponential Growth in Decentralized Finance, https://www.coinchange.io/blog/permissioned-defi-paving-the-way-for-exponential-growth 32. ETHLend (LEND) Review: Worth It? Beginners Guide to Crypto Lending - Coin Bureau, https://coinbureau.com/review/ethlend-lend 33. Aave - 2026 Company Profile, Team, Funding, Competitors & Financials - Tracxn, https://tracxn.com/d/companies/aave/__JiXfiPZKVkx7021dCR937XH3M5d2vj-Cy3z3dnIPJ00 34. Stani Kulechov | Coinpedia User Profile, https://app.coinpedia.org/stanikulechov/ 35. jordan l gustave | Coinpedia User Profile, https://app.coinpedia.org/jordangustave/ 36. Jordan Lazaro Gustave - RootData, https://www.rootdata.com/member/Jordan%20Lazaro%20Gustave?k=MTA0OTg%3D 37. Aave: Founder, Leadership & Team - Wellfound, https://wellfound.com/company/aave/people 38. Nolvia Serrano Appointed Head Of Operations in El Salvador | by, https://medium.com/@AlexBlockBank/nolvia-serrano-appointed-head-of-operations-in-el-salvador-dc34d77de457 39. Ama Recap: GainDao. Date : September 9 Time : 3 PM UTC… | by, https://medium.com/@Crypto_Maxxis/ama-recap-gaindao-5c37c67f4a7 40. Documentation/ETHLendWhitePaper.md at master · ETHLend/Documentation - GitHub, https://github.com/ETHLend/Documentation/blob/master/ETHLendWhitePaper.md 41. Aave Review 2026: What To Know About The Pros, Cons, Features - Milk Road, https://milkroad.com/reviews/aave/ 42. The Power of Antifragility- Why OG DeFi Protocols Will Continue to Dominate - Medium, https://medium.com/@bagtalkmedia/the-power-of-lindy-why-og-defi-protocols-will-continue-to-dominate-7552904fba5f 43. In-depth Research Report on On-chain Lending Market: When Off-chain Credit Meets On-chain Settlement - RootData, https://www.rootdata.com/news/611373 44. Aave V4 Launches on Ethereum Mainnet: Revolutionary Hub & Spoke Architecture Unlocks Unprecedented Liquidity - CryptoRank, https://cryptorank.io/news/feed/99f5b-aave-v4-ethereum-mainnet-launch 45. Changelog | Aave Protocol Documentation, https://aave.com/docs/resources/changelog 46. Anatomy of the Aave v4 contracts - Jean Cvllr, https://jeancvllr.medium.com/anatomy-of-the-aave-v4-contracts-364fa3189d04 47. EthLend (LEND) - Tokens - Etherscan, https://etherscan.io/token/0x80fb784b7ed66730e8b1dbd9820afd29931aab03 48. White paper drafted under the European Markets in Crypto- Assets Regulation (EU) 2023/1114 for FFG H618RN577 - CheckSig, https://www.checksig.com/whitepapers/2026-05-04-aave-whitepaper.pdf 49. 2026 Funding Rounds & List of Investors - Aave - Tracxn, https://tracxn.com/d/companies/aave/__JiXfiPZKVkx7021dCR937XH3M5d2vj-Cy3z3dnIPJ00/funding-and-investors 50. Aave 2026 Company Profile: Valuation, Funding & Investors | PitchBook, https://pitchbook.com/profiles/company/224491-60 51. Aave (AAVE): key information on this crypto - Coinhouse, https://www.coinhouse.com/aave 52. Aave (AAVE) ICO Funding Rounds, Token Sale Review & Tokenomics Analysis | CryptoRank.io, https://cryptorank.io/ico/aave 53. ETHLend LEND Token Raises Over $10 Mil in 30 Min - Finance Magnates, https://www.financemagnates.com/thought-leadership/ethlends-lend-token-raises-10-million-30-minutes/ 54. What is Avalanche (AVAX)? Features, Tokenomics and Road Map | CoinMarketCap, https://coinmarketcap.com/academy/article/a-deep-dive-into-avalanche-avax 55. Update on Aave's governance crisis: Alignment is on the table, enforceability is not (yet), https://www.21shares.com/en-eu/insights/update-on-aaves-governance-crisis-alignment-is-on-the-table-enforceability-is-not-yet 56. The "Aave Will Win" proposal has passed Temp Check with 52.58% approval | Cryptopolitan en Binance Square, https://www.binance.com/es-MX/square/post/297343060218225 57. [ARFC] sGHO Launch Configuration - Aave - Governance Forum, https://governance.aave.com/t/arfc-sgho-launch-configuration/24346 58. DeFi Token Valuation: Key Metrics, Tokenomics, and Case Studies | CryptoEQ, https://www.cryptoeq.io/articles/defi-fundamentals-valuation 59. How Aave Horizon is Built to Support Institutions, https://aave.com/blog/horizon-built-for-institutions 60. Aave Horizon Complete Breakdown for 2025: How to Borrow Stablecoins Against Tokenized RWAs, https://stablecoininsider.org/aave-horizon-complete-breakdown-2025/ 61. Aave V4 Launches on Avalanche: How the New Hub & Spoke DeFi Architecture and $13.7B Institutional RWA Influx Impact AVAX Price - KuCoin, https://www.kucoin.com/blog/th-aave-v4-launches-on-avalanche-how-the-new-hub-spoke-defi-architecture-and-13-7b-institutional-rwa-influx-impact-avax-price 62. Comparison: Dolomite vs Aave vs Compound — Notable Differences from the Investor's Perspective | blogtienso on Binance Square, https://www.binance.com/en/square/post/30154707851145 63. Aave plans to boost revenue and expand its GHO stablecoin over the next year - Pluang, https://pluang.com/en/news-feed/aave-rencanakan-pertumbuhan-pendapatan-dan-ekspansi-gho 64. Aave V4 GHO Yield 2026: Borrow-Mint Mechanics Explained | Support - Eco, https://eco.com/support/en/articles/15253998-aave-v4-gho-yield-2026-borrow-mint-mechanics-explained 65. What is Umbrella, Aave's new security module (AAVE)? - OAK Research, https://oakresearch.io/en/analyses/innovations/what-is-umbrella-new-product-from-aave 66. aave-dao/aave-umbrella: Aave Umbrella smart contracts - GitHub, https://github.com/aave-dao/aave-umbrella 67. Algorithmic Stablecoins Statistics 2026: Market Cap, Survivors & Regulation - SQ Magazine, https://sqmagazine.co.uk/algorithmic-stablecoins-statistics/ 68. Latest Aave News - (AAVE) Future Outlook, Trends & Market Insights - CoinMarketCap, https://coinmarketcap.com/cmc-ai/aave/latest-updates/ 69. Aave posts $907M revenue in 2025, draws Standar... - Pluang, https://pluang.com/en/news-feed/aave-laporkan-pendapatan-907juta-2025-dan-333juta-ytd-2026-dengan-standar 70. aave/aavenomics - GitHub, https://github.com/aave/aavenomics 71. What is Aave? Detailed information about the Aave project and the AAVE Token | TinTucBitcoin on Binance Square, https://www.binance.com/en/square/post/27801385569337 72. FAQ - Aave, https://aave.com/faq 73. Safety Module Emission Update - Aave, https://app.aave.com/governance/v3/proposal/?proposalId=342 74. [ARFC] GHO CEX Earn Incentive Program - Governance - Aave, https://governance.aave.com/t/arfc-gho-cex-earn-incentive-program/22284 75. Umbrella | Aave Protocol Documentation, https://aave.com/docs/aave-v3/umbrella 76. The Wealth Code of AAVE Founder: The True DeFi Story from Protocol Cash Flow to a $30 Million Mansion | web3 程曦 on Binance Square, https://www.binance.com/en-AE/square/post/35986506974490 77. Standard Chartered Predicts 50x Upside for AAVE, Targeting $3,500 by 2030 - CryptoRank, https://cryptorank.io/news/feed/f3dfe-standard-chartered-aave-price-prediction-2030 78. Aave June 2026 Report | Token Terminal on Binance Square, https://www.binance.com/en/square/post/343377067336786 79. Dashboard - Aave January 2026 Report - Token Terminal, https://tokenterminal.com/explorer/studio/dashboards/98aa697c-f0ea-40d5-aa54-3010166c54ab 80. Aave 2025 Year in Review, https://aave.com/blog/aave-2025-recap 81. Best Decentralized Finance Projects (DeFi) for 2026 - Datawallet, https://www.datawallet.com/crypto/best-defi-projects 82. Deposito Aave v4 di Ethereum capai $200 juta, m... - Pluang, https://pluang.com/news-feed/deposit-aave-v4-di-ethereum-capai-200juta-dolar-dalam-sebulan 83. Why Aavegotchi Chose Polygon. Our DeFi-powered collectibles game… - Medium, https://aavegotchi.medium.com/why-aavegotchi-chose-polygon-356238977fb2 84. rsETH Incident: WETH LTV Restoration Across V3 Instances - Aave, https://app.aave.com/governance/v3/proposal/?proposalId=482 85. Aave V4 hadir di Avalanche, memperluas pinjaman... - Pluang, https://pluang.com/news-feed/aave-v4-meluncur-di-avalanche-ekspansi-protokol-terkini 86. Aave Partially Unfreezes WETH After Kelp Bridge Exploit - The Defiant, https://thedefiant.io/news/defi/aave-partially-unfreezes-weth-after-rseth-bridge-exploit 87. [Discussion] Safety Module - Aave - Governance Forum, https://governance.aave.com/t/discussion-safety-module/12029 88. Peluncuran Aave V4 di Avalanche: Bagaimana Arsitektur DeFi Hub & Spoke Baru dan Injeksi RWA Institusional Senilai $13,7 Miliar Mempengaruhi Harga AVAX - KuCoin, https://www.kucoin.com/id/blog/id-aave-v4-launches-on-avalanche-how-the-new-hub-spoke-defi-architecture-and-13-7b-institutional-rwa-influx-impact-avax-price 89. [ARFC] Aave Will Win Framework - Governance, https://governance.aave.com/t/arfc-aave-will-win-framework/24352
