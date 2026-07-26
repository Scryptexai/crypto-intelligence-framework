Analisis Komprehensif Protokol ether.fi (ETHFI): Arsitektur Non-Custodial, Keuangan On-Chain, Strategi Tokenomika, dan Evolusi Bank Neo DeFi

## 1 Executive Summary

ether.fi (ETHFI) adalah protokol restaking likuid (LRT) terbesar di jaringan Ethereum yang mengelola nilai total terkunci (TVL) rata-rata sebesar $7,31 miliar pada kuartal pertama tahun 2026. Protokol ini berdiri sebagai perintis infrastruktur staking terdelegasi yang sepenuhnya bersifat non-custodial, di mana deposan mempertahankan kendali penuh atas kunci privat validator dan kredensial penarikan mereka. Melalui tiga lini produk utamanya—Stake, Liquid, dan Cash—ether.fi mengintegrasikan fungsionalitas yield on-chain secara vertikal dengan utilitas dunia nyata.

Kemampuan pertahanan protokol diuji secara ekstrem selamaWave Redemption April-Mei 2026, di mana ether.fi berhasil memproses penarikan sebesar 542.792 ETH atau setara dengan 19.6% dari total TVL-nya dalam waktu 33 hari tanpa menyebabkan antrean keluar (exit queue) pada jaringan konsensus Ethereum. Melalui integrasi Distributed Validator Technology (DVT) bersama SSV Network dan kolaborasi strategi brankas otomatis (BoringVault) bersama Veda Labs, ether.fi memposisikan dirinya tidak hanya sebagai protokol restaking biasa, melainkan sebagai mesin utama dalam transformasi neobank kripto. Laporan intelijen ini dirancang sebagai basis pengetahuan terstruktur untuk memfasilitasi penalaran kecerdasan buatan (AI reasoning) dalam mengevaluasi ekosistem keuangan terdesentralisasi masa depan.

## 2 Industry Background

Kondisi industri kripto sebelum lahirnya ether.fi didominasi oleh pergeseran konsensus Ethereum dari Proof of Work (PoW) menuju Proof of Stake (PoS) melalui peristiwa "The Merge". Transisi ini memicu lonjakan permintaan yang masif terhadap staking Ethereum untuk mengamankan jaringan sekaligus memperoleh imbalan hasil (yield) konsensus harian. Namun, model staking awal menghadirkan friksi likuiditas yang tinggi bagi pelaku pasar. Protokol Liquid Staking (LST) generasi pertama seperti Lido Finance memecahkan hambatan likuiditas ini dengan menerbitkan token representasi (seperti stETH).

Meskipun model LST sukses mengakumulasi modal, arsitekturnya menyimpan kelemahan struktural yang signifikan. Pengguna diwajibkan menyerahkan kontrol kunci validator dan kredensial penarikan (withdrawal credentials) sepenuhnya kepada operator node terpusat atau kolam pengelola protokol. Hal ini menciptakan risiko peretasan, kolusi operator, dan pemotongan saldo (slashing) yang tidak dapat dimitigasi secara langsung oleh staker. Kondisi industri semakin kompleks dengan kemunculan konsep "restaking" yang dipelopori oleh EigenLayer. Restaking memungkinkan staker Ethereum untuk menyalurkan jaminan modal mereka guna mengamankan Active Verification Services (AVS) pihak ketiga demi melipatgandakan perolehan hasil. Sayangnya, opsi restaking awal sangat tidak likuid dan memaksa pengguna mengunci modal mereka secara spekulatif tanpa kejelasan penarikan jangka pendek.

ether.fi hadir pada titik balik historis ini untuk menjembatani kedaulatan kepemilikan kunci privat staker, likuiditas instan melalui pencetakan token restaking likuid eETH, dan akses otomatis ke yield multi-layer tanpa friksi.

## 3 Project Origin

Sejarah berdirinya ether.fi berakar dari ketidakpuasan operasional para pendirinya saat mengelola Gadze Finance, sebuah dana lindung nilai (hedge fund) DeFi kuantitatif yang berfokus pada staking Ethereum pada tahun 2021. Selama mengelola dana tersebut, Mike Silagadze dan timnya mencari solusi infrastruktur staking yang memungkinkan mereka menyetor ETH dalam jumlah besar tanpa kehilangan kendali atas kunci privat mereka. Setelah mengevaluasi seluruh opsi staking terdelegasi di pasar, mereka menyimpulkan bahwa tidak ada satu pun protokol yang memenuhi standar keamanan non-custodial yang aman untuk modal institusional.

Kesadaran akan kesenjangan pasar ini mendorong keputusan untuk meluncurkan ether.fi pada Oktober 2022. Tim inti proyek ini dibentuk dengan menggabungkan keahlian kewirausahaan teknologi tradisional berskala besar dan kompetensi rekayasa blockchain:

Mike Silagadze (Founder dan CEO): Pengusaha teknologi lulusan University of Waterloo (2007) bidang Insinyur Listrik. Ia sebelumnya mendirikan Top Hat, platform keterlibatan mahasiswa (edtech) yang ia kembangkan dari startup Toronto hingga memiliki 500 karyawan dan menghasilkan pendapatan tahunan $60.000.000 sebelum dijual.

Rok Kopp (Co-Founder dan Chief Growth Officer): Eksekutif penjualan dengan pengalaman lebih dari 15 tahun di industri teknologi SaaS. Ia sebelumnya menjabat sebagai VP Enterprise Sales di Top Hat dan Chief Revenue Officer di Obsidian HR.

Tim Frost (Co-Founder): Insinyur perangkat lunak senior yang mengkhususkan diri pada pengembangan arsitektur blockchain.

Chuck Morris (Vice President and Project Engineering): Mengarahkan rekayasa perangkat lunak dan pengembangan tim teknis sejak berkarier di industri kripto pada 2018.

Tim ini memilih mendaftarkan badan hukum proyek di Cayman Islands untuk mengamankan kepastian regulasi Virtual Asset Service Provider (VASP) yang lebih bersahabat dibanding yurisdiksi Amerika Serikat atau Kanada.

## 4 Innovation Analysis

Inovasi utama ether.fi yang mengubah standar industri staking terdelegasi adalah arsitektur non-custodial ujung-ke-ujung (end-to-end non-custodial delegated staking). Alih-alih bertindak sebagai kustodian kunci validator, ether.fi memisahkan peran kepemilikan aset dengan operasional node melalui kriptografi kunci publik/privat:

Pembuatan Kunci Terdesentralisasi: Staker menggunakan aplikasi desktop ether.fi yang dijalankan secara lokal di komputer mereka untuk menghasilkan kunci publik/privat validator.

Enkripsi Kunci Aman: Staker mengenkripsi kunci validator privat tersebut dengan kunci publik operator node terpilih dari daftar registrasi protokol, lalu mengirimkannya secara on-chain.

Dekripsi Terisolasi: Operator node mengunduh data terenkripsi dan mendekripsinya secara lokal menggunakan kunci privat mereka untuk menjalankan validator pada rantai Beacon Ethereum, tanpa pernah memiliki akses ke kredensial penarikan (withdrawal credentials) staker.

Untuk mengotomatisasi dan mengamankan kepemilikan ini secara on-chain, ether.fi memperkenalkan inovasi Token Non-Fungible (NFT) Ganda untuk setiap peluncuran validator 32 ETH:

T-NFT (Transferable NFT): Merepresentasikan hak klaim atas 30 ETH dari total deposit. T-NFT bersifat likuid, dapat dipindahtangankan, dan didepositokan ke liquidity pool untuk dicetak menjadi eETH.

B-NFT (Bond NFT): Merepresentasikan 2 ETH sisanya dan bersifat soul-bound (tidak dapat ditransfer). B-NFT berfungsi sebagai jaminan asuransi pemotongan (slashing deductible) jika terjadi insiden pemotongan saldo di node. Karena mengemban risiko kepatuhan operasional, pemegang B-NFT berhak atas yield 50% lebih tinggi dibandingkan pemegang T-NFT.

Inovasi ini berdampak signifikan pada industri karena berhasil menekan risiko pihak ketiga (counterparty risk) secara total. Ketika protokol LRT pesaing memaksa pengguna berspekulasi pada satu arah deposit tanpa opsi keluar instan, ether.fi menjadi protokol pertama yang meluncurkan fungsionalitas penarikan (redemptions) langsung 1:1 secara on-chain, menetapkan standar keamanan baru di pasar restaking global.

## 5 Technology Evolution

Evolusi teknologi ether.fi dirancang secara bertahap untuk menyesuaikan kematangan teknis Ethereum dan kemunculan teknologi validator terdistribusi:

Tahap 1: Delegated Staking (Mei 2023): Peluncuran mainnet bertepatan dengan pemutakhiran Shanghai Ethereum. Arsitektur difokuskan pada fungsionalitas deposit kelipatan 32 ETH yang aman menggunakan kerangka kerja NFT ganda (T-NFT & B-NFT) dan brankas penarikan aman mandiri (Withdrawal Safe).

Tahap 2: Liquidity Pool dan eETH (Q2/Q3 2023): Pengenalan kolam likuiditas terpadu yang memfasilitasi deposit pecahan (di bawah 32 ETH). Pengguna menyetor ETH dan menerima token eETH (dan weETH non-rebasing) yang secara otomatis mengakumulasi imbalan konsensus staking Ethereum dan restaking EigenLayer.

Integrasi SSV Network DVT (2024): Penerapan teknologi Distributed Validator Technology (DVT) untuk membagi operasi validator tunggal ke dalam kluster multi-operator terdesentralisasi. Hal ini meningkatkan toleransi kesalahan sistem dan menekan tingkat offline validator ke tingkat mendekati nol persen.

Redesain Arsitektur Keamanan (Pertengahan 2026): ether.fi mengimplementasikan perombakan keamanan terbesar dalam sejarahnya dengan mengompilasi doktrin pertahanan aktif langsung ke dalam smart contract pintar. Pembaruan ini memastikan:

Nilai tukar eETH/ETH terlindung secara permanen oleh invarian on-chain agar tidak dapat terdepresiasi (deflate) akibat kesalahan oracle.

weETH terlindung dari under-backing melalui persamaan invariant pasokan suplai.

Fungsi klaim penarikan yang telah selesai difinalisasi dibuat permissionless dan tidak dapat dijeda (unpausable) bahkan dalam kondisi darurat sekalipun, mencegah kontrol sepihak dari tim pengembang.

Pembatasan laju sirkuit global (circuit breakers) membatasi kecepatan pencetakan dan pembakaran token untuk meminimalisasi dampak eksploitasi jembatan lintas rantai.

## 6 Funding Intelligence

Peningkatan modal venture (VC) ether.fi merepresentasikan kepercayaan tinggi lembaga keuangan institusional terhadap Mike Silagadze dan keandalan sistem staking non-custodial.

Funding Round: Seed Round

Date: 28 Februari 2023

Amount: $5,300,000

Lead Investors: North Island Ventures, Chapter One, Node Capital

Participants: Arthur Hayes, Arrington Capital, Maelstrom, Purpose Investments, Version One Ventures, Jack Lipstone, Travis Scher

INKONSISTENSI: Beberapa basis data investasi komersial mencatat jumlah Seed Round sebesar $5.000.000 dengan tanggal pengumuman 1 Februari 2023. Tingkat Keyakinan Bukti: LOW.

Funding Round: Series A

Date: 28 Februari 2024

Amount: $23,000,000

Lead Investors: Bullish Capital, CoinFund

Participants: OKX Ventures, Foresight Ventures, Consensys, Amber Group, Selini Capital, Draper Dragon, Bankless Ventures, 10T Holdings, Animoca Brands, Draper Associates, Felix Capital, FirstMark Capital, Greylock, Menlo Ventures, Polygon Labs, Tribe Capital, White Loop Capital, XAnge, Alasdair Foster, Chuck Eesley, Furqan Rydhan, Jean Baptiste Rudelle, Nicolas Pinto, Pascal Gauthier, RON Pragides, serta para pendiri protokol ternama seperti Aave, Polygon, Kraken, Curve, Ethena, dan DeFi Llama. - INKONSISTENSI: PitchBook mencatat tanggal penyelesaian Series A pada 13 Maret 2024 dengan total perolehan dana tercatat sebesar $27.000.000. Perbedaan angka $4.000.000 ini diduga berasal dari konversi alokasi pendanaan sekunder atau opsi utang konvertibel yang tidak dipublikasikan dalam rilis pers resmi Bullish Capital. Tingkat Keyakinan Bukti: LOW.

Funding Round: Public Strategic Allocation (Binance Launchpool - Proyek ke-49)

Date: 14 Maret 2024

Farming Period: 4 hari

BNB Pool Reward Allocation: 16,000,000 ETHFI

FDUSD Pool Reward Allocation: 4,000,000 ETHFI

## 7 Community Intelligence

Strategi awal penyerapan pengguna ether.fi bertumpu pada gamifikasi intensif on-chain yang dirancang untuk mengungguli para pesaing secara masif. Protokol ini merancang program loyalitas poin yang mengonversi volume dan durasi staking menjadi nilai kuantitatif untuk kualifikasi distribusi airdrop di masa depan:

Sistem Loyalitas Harian: Pengguna memperoleh 1.000 poin loyalitas untuk setiap 1 ETH yang disetor per hari.

Pengenalan StakeRank: Sistem peringkat loyalitas berjenjang 8 tingkat yang secara progresif meningkatkan laju perolehan poin dari 1x hingga 2x lipat. Pengguna naik satu peringkat untuk setiap 100 jam (atau 240 jam — lihat inkonsistensi) durasi staking kumulatif yang tidak terputus. Penarikan modal instan sebelum snapshot secara otomatis mengembalikan level pengguna ke tingkat terendah, sebuah strategi yang sukses mengunci loyalitas TVL.

Kampanye Perks Passport (Season 3): Program gamifikasi paspor digital on-chain. Pengguna memperoleh stempel digital ("stamps") setelah menyelesaikan aktivitas DeFi lintas protokol seperti menyetor modal di brankas Liquid ether.fi atau menyediakan likuiditas weETH di mitra seperti Pendle dan Karak. Mengumpulkan stamps memberikan tambahan pengali poin harian hingga maksimal 5x lipat, menstimulasi perputaran modal weETH secara organik di seluruh jaringan L2.

Pemanfaatan Kampanye Kemitraan (Staking Frens): Kolaborasi bersama SSV Network dan jaringan L2 lainnya untuk mendistribusikan insentif ganda guna menyerap komunitas dari ekosistem eksternal.

Strategi ini terbukti sangat berhasil, di mana ether.fi mencatat pertumbuhan jumlah pemegang eETH hingga mencapai 71.000 alamat unik hanya dalam waktu dua bulan pertama tahun 2024, mengamankan posisi teratas dalam pangsa pasar LRT.

## 8 Narrative Intelligence

Keberhasilan kapitalisasi pasar ether.fi didorong oleh kelincahan tim dalam menyerap, menciptakan, dan mendominasi narasi terdepan di setiap siklus industri kripto:

Narasi Sovereign Liquid Staking (LST) (Pertengahan 2023): Memanfaatkan kelelahan komunitas terhadap risiko sentralisasi Lido dengan menyebarkan narasi kedaulatan kunci privat dan non-custodial sejati.

Narasi Native Restaking & LRT (Awal 2024): Menjadi protokol pertama yang meluncurkan eETH sebagai LRT native ter-restaking otomatis di EigenLayer. Kampanye restaking points terbukti menjadi katalis pertumbuhan TVL terbesar pada paruh pertama 2024.

Narasi Real World Assets (RWA) (Akhir 2025 - 2026): Berkolaborasi secara agresif dengan Plume Network untuk menyalurkan likuiditas on-chain ke aset dunia nyata yang menghasilkan yield stabil. Kolaborasi ini mencakup alokasi langsung modal sebesar $100.000.000 ke dalam Plume RWA Vault dan penyetoran strategis $25.000.000 ke Nest Vault Plume.

Narasi Crypto Neobank & Pembayaran Ritel (2026): Ketika hasil yield DeFi murni mulai mengalami jenuh, ether.fi memimpin transisi industri menuju konsep "Crypto Neobank". Dengan meluncurkan kartu kredit Cash, protokol ini menghubungkan hasil on-chain weETH secara langsung dengan jaringan pembayaran fisik dunia nyata, secara cerdas memindahkan fokus performa proyek dari sekadar penyedia jaminan spekulatif menjadi penyedia infrastruktur utilitas harian.

## 9 Competitive Landscape

Lanskap kompetitif ether.fi mencakup persaingan intensif dengan protokol staking mapan dan LRT generasi baru:

Lido Finance (LST Terbesar): Memiliki keunggulan likuiditas stETH yang mendominasi integrasi DeFi. ether.fi bersaing dengan menawarkan hasil restaking native tambahan di atas yield staking murni dan menjamin hak kedaulatan kunci staker yang tidak ditawarkan oleh model kustodian terpusat Lido.

Puffer Finance: Protokol restaking likuid berbasis anti-slashing perangkat keras (Secure Enclaves). ether.fi mengalahkan keunggulan teknologi Puffer dengan memenangkan pangsa pasar pertama melalui penyediaan fitur redemptions (penarikan) langsung 1:1, mengurangi ketakutan deposan atas likuiditas modal yang macet.

Kelp DAO & Renzo Protocol: Pesaing LRT multi-aset. Keunggulan ether.fi terbukti saat rsETH Kelp DAO menderita insiden manipulasi pesan lintas rantai senilai $292.000.000 pada April 2026. ether.fi tidak memiliki eksposur langsung terhadap rsETH, dan keamanan jembatan weETH miliknya yang kokoh (menggunakan skema DVN 4-dari-4) berhasil membentengi protokol dari efek penularan kegagalan.

FinTech Tradisional & Neobank Finansial: Menjadi kompetitor baru setelah rilis kartu Cash. ether.fi memenangkan persaingan di segmen pengguna kripto native karena memungkinkan pembelanjaan kredit langsung berbasis agunan aset produktif (yield-bearing) tanpa memicu peristiwa pajak penjualan aset kripto.

## 10 Product Evolution

Evolusi produk ether.fi merepresentasikan integrasi vertikal layanan keuangan terdesentralisasi yang terbagi ke dalam tiga divisi operasional utama:

Stake (Infrastruktur Basis): Produk dasar yang memfasilitasi deposan untuk mencetak weETH, eBTC, dan eUSD melalui staking terdelegasi non-custodial. weETH berfungsi sebagai jaminan bernilai tinggi di seluruh pasar pinjaman DeFi papan atas seperti Aave.

Liquid (Strategi Otomatis): Brankas taktis yang dibangun di atas kemitraan Veda Labs menggunakan arsitektur BoringVault. Pengguna menyetor modal (ETH, BTC, USD) dan sistem brankas akan secara otomatis merebalance dan mengalokasikan modal tersebut ke berbagai strategi DeFi yang menghasilkan yield tertinggi secara dinamis (misalnya strategi delta-neutral, Morpho Lending, atau penyediaan likuiditas terkonsentrasi Uniswap V3).

Cash (Pembayaran & Utilitas Konsumen): Kartu kredit Visa terdesentralisasi yang terintegrasi dengan dompet kustodian mandiri. Cash bertindak sebagai jembatan off-ramp kripto, di mana pengguna dapat meminjam dana belanja langsung dengan jaminan portofolio weETH produktif mereka. Layanan ini menyediakan nomor akun IBAN/SWIFT pribadi untuk pengiriman uang global dan pengurusan pajak instan.

## 11 Tokenomics Intelligence

Token tata kelola ETHFI dirancang sebagai pengatur desentralisasi parameter ekonomi proyek. Struktur tokenomika dipaparkan secara mendalam sebagai berikut:

Max Token Supply: 1,000,000,000 ETHFI

Initial Circulating Supply: 115,200,000 ETHFI (11.52% dari pasokan maksimum)

Est. Outstanding Supply (Pertengahan 2026): 762,635,999 ETHFI (Mencapai tingkat kejenuhan sirkulasi 93% pasca pembukaan kunci vesting utama)

Token Allocation (Official Documentation):

Investors: 33.74%

Vesting Schedule: Dilepaskan secara berkala dalam jadwal vesting selama 2 tahun

DAO Treasury: 21.63%

Purpose: Didistribusikan sebagai Ecosystem Fund, stimulus pengembangan komunitas, dengan 1% dikomitmenkan langsung untuk Protocol Guild

Core Contributors: 21.47%

Vesting Schedule: Dilepaskan secara berkala dalam jadwal vesting selama 3 tahun

User Airdrops: 17.57%

Purpose: Distribusi program insentif loyalitas pengguna multi-musim

Partnerships: 5.60%

Purpose: Alokasi strategis oleh yayasan untuk perluasan ekosistem jangka panjang

INKONSISTENSI: Terdapat ketidaksesuaian klasifikasi alokasi antara dokumentasi yayasan internal dengan data agregator on-chain publik:

Alokasi Agregator Publik:

Investors: 33.74%

Treasury (TBD): 21.62%

Core Contributors: 21.47%

User Airdrops: 17.30%

Partnerships & Liquidity: 3.90%

User Airdrops (TBD): 1.97%

Tingkat Keyakinan Bukti: LOW.

Mekanisme Penyerapan Pasokan (Token Sinks):

Sistem Keanggotaan Klub: Pengguna mengunci ETHFI untuk meraih tingkatan Club (Luxe pada batas minimal 15.000 ETHFI, Pinnacle pada batas 100.000 ETHFI) guna mendapatkan alokasi bonus regular dan keringanan biaya belanja Cash.

Pembelian Kembali Kas (Buyback): Sebagian pendapatan biaya penarikan protokol dialokasikan secara otomatis untuk membeli kembali token ETHFI di pasar sekunder demi mengimbangi inflasi insentif.

## 12 Airdrop & Incentive Intelligence

ether.fi merancang kampanye distribusi airdrop agresif multi-fase yang terbukti menjadi tulang punggung retensi TVL selama siklus koreksi pasar:

Season 1 Airdrop (Maret 2024): Distribusi sebesar 6% dari total suplai. Kelayakan dihitung berdasarkan keiksuertaan EAP, pemegang NFT, dan referensi teman.

Penyelesaian Sengketa Justin Sun: Menanggapi keberatan komunitas atas alokasi raksasa kepada Justin Sun (akun institusi skala whale), ether.fi memodifikasi aturan dengan menerapkan vesting paksa selama 3 bulan untuk akun kategori whale, sementara akun ritel diizinkan mengklaim 100% alokasi instan di TGE.

Season 2 Airdrop (Mei 2024): Distribusi sebesar 5% dari total suplai. Memperkenalkan batas minimal loyalitas yang jauh lebih tinggi sebesar 150.000 poin dan sanksi diskualifikasi instan jika staker menarik dana 5 hari sebelum snapshot.

Season 3 Airdrop (September 2024): Distribusi sebesar 2.7% (atau 2.5% — lihat inkonsistensi). Memperkenalkan sistem Perks Passport yang menggamifikasi aktivitas DeFi. Penerima airdrop di bawah 3 ETHFI dianulir secara otomatis melalui filter debu (dust filter) untuk mengamankan efisiensi biaya gas distribusi.

INKONSISTENSI: Dokumen proposal tata kelola awal mencantumkan alokasi Season 3 sebesar 25.000.000 ETHFI, sedangkan rilis tutorial pelacakan eksternal mencatat angka pembagian sebesar 27.000.000 ETHFI (2.7% pasokan). Tingkat Keyakinan Bukti: LOW.

Season 4 & 5 (Akhir 2024 - Pertengahan 2025): Skema transisi ke program musiman permanen setiap 4 bulan dengan emisi maksimal 2.000.000 ETHFI per musim. Imbalan mulai digabungkan dengan token tata kelola mitra DeFi eksternal dan token konsolidasi LRT².

Member Rewards (Juni - Agustus 2025): Kampanye khusus alokasi 7.500.000 ETHFI untuk mempercepat penetrasi ritel produk Cash dan Brankas Liquid di kalangan anggota Club.

## 13 Token Lifecycle Intelligence

Analisis siklus pasar sekunder token ETHFI menunjukkan volatilitas harga pasca-TGE yang dipengaruhi oleh dinamika emisi insentif dan intervensi likuiditas terencana:

Pembukaan Pasar (18 Maret 2024): Perdagangan perdana spot dibuka pasca kampanye Binance Launchpool, didukung oleh likuiditas market maker utama.

All-Time High (ATH): Menyentuh level $8.53 pada tanggal 27 Maret 2024, didorong oleh demam restaking awal.

All-Time Low (ATL): Merosot hingga level terendah $0.2665 (atau $0.2688 — lihat inkonsistensi) pada 5 Juni 2026. Penurunan ini dipicu oleh jenuhnya pasar altcoin, tekanan jual konstan dari pelepasan vesting investor/tim kontributor, dan emisi poin restaking berkelanjutan.

INKONSISTENSI: Pangkalan data CoinGecko mencatat harga ATL sebesar $0.2665 pada 5 Juni 2026 di satu bagian laporannya, namun mencantumkan angka $0.2688 di bagian tabel riwayat sejarah yang sama. Tingkat Keyakinan Bukti: LOW.

Intervensi Kas Stabilitas (Oktober 2025): Ketika harga ETHFI merosot hingga $0.93 (turun lebih dari 89% dari ATH), komunitas meluncurkan proposal pembelian kembali (buyback) darurat. DAO menyetujui otorisasi yayasan untuk mengalokasikan hingga $50.000.000 dari cadangan kas guna menyerap suplai ETHFI di pasar terbuka setiap kali harga spot berada di bawah ambang batas $3.00. Inisiatif ini berhasil menciptakan lantai harga (price floor) dan menahan kepanikan aksi jual di pasar.

Fundamental Nilai Wajar: Dengan volume pendapatan biaya protokol terakumulasi tahunan sebesar $231.32 juta, token ETHFI dinilai berstatus undervalued secara fundamental di bawah harga $1.00 jika diukur menggunakan rasio Price-to-Fees (P/F ratio) pengubah industri. Namun, apresiasi nilainya dibayangi oleh laju inflasi emisi dan risiko regulasi global terhadap token tata kelola staking.

## 14 Business Intelligence

Infrastruktur pengumpulan data on-chain menyajikan ringkasan kinerja keuangan ether.fi di bawah ini:

Periode Bisnis: Q4 2025

Total Value Locked (TVL) Average: $9,510,000,000

Total Protocol Fees Accumulated: $67,240,000

Net Protocol Revenue Generated: $13,020,000

ether.fi Cash Card Quarterly Spend Volume: $126,130,000

Monthly Active Users (MAU) Average: 19,900

Periode Bisnis: Q1 2026

Total Value Locked (TVL) Average: $7,310,000,000 (Mengalami kontraksi 23.20% secara kuartalan akibat merosotnya harga dasar ETH, bukan karena arus keluar penarikan massal)

Total Protocol Fees Accumulated: $56,780,000

Net Protocol Revenue Generated: $11,430,000

ether.fi Cash Card Quarterly Spend Volume: $170,060,000 (Mengalami peningkatan pesat 34.83% secara kuartalan)

Monthly Active Users (MAU) Average: 24,900 (Meningkat 25.13% secara kuartalan)

Division Share of Q1 2026 TVL: Stake menguasai 91.21% pangsa aset platform

Division Share of Q1 2026 Fees: Stake menyumbang 86.92% pangsa pendapatan biaya

Division Share of Q1 2026 Revenue: Stake menyumbang 71.43%, sementara divisi Cash melonjak hingga menyumbang 26.04% pangsa pendapatan platform

Division Share of Q1 2026 MAU: Divisi Cash menguasai 96.98% pangsa pengguna aktif bulanan

Laporan Neraca Yayasan (As of 30 September 2025):

Total Fair Market Value of Treasury Assets: $306,000,000

Treasury Assets held in native ETHFI: $285,000,000

Treasury Assets held in diversified tokens (USDC, stablecoins, ETH, weETH, WBTC, cbBTC): $21,000,000

Total External Debt Obligations: $0 (Bebas dari liabilitas utang pihak ketiga)

## 15 Success & Failure Analysis

Analisis keberhasilan dan kegagalan protokol dinilai dari 8 sudut pandang pemangku kepentingan yang berbeda:

Founder

Verdict: SUKSES

Alasan: Mike Silagadze dan tim inti berhasil mentransformasi ether.fi dari sekadar protokol staking menjadi entitas DeFi Neobank terbesar, memposisikan weETH sebagai LRT dominan, dan mengamankan kas yayasan senilai $306.000.000 untuk operasional jangka panjang.

Tingkat Keyakinan: HIGH

Venture Capital (VC)

Verdict: SUKSES

Alasan: Investor awal (North Island, Chapter One, Bullish, CoinFund) meraih likuiditas penuh pasca-TGE dengan valuasi TVL puncak di atas $9 miliar, mengonfirmasi pengembalian investasi (ROI) berbasis ekuitas dan token yang sangat menguntungkan.

Tingkat Keyakinan: HIGH

Retail User (Retail)

Verdict: CAMPURAN

Alasan: Pengguna ritel beroleh keuntungan besar dari kelancaran proses airdrop Season 1-3 dan yield restaking ganda yang aman. Namun, ritel yang membeli token ETHFI di pasar sekunder dekat wilayah ATH mengalami depresiasi aset kertas hingga 89%.

Tingkat Keyakinan: HIGH

Community Member (Community)

Verdict: CAMPURAN

Alasan: Program gamifikasi StakeRank dan Perks Passport sangat diminati dan interaktif. Namun, sempat timbul kemarahan komunitas atas insiden alokasi "Justin Sun" yang dinilai mencederai prinsip keadilan desentralisasi awal.

Tingkat Keyakinan: MEDIUM

Protocol Developer (Developer)

Verdict: SUKSES

Alasan: Pengembang sukses merilis serangkaian smart contract non-upgradeable yang tangguh bersama Veda Labs, mengintegrasikan DVT secara aman, serta meminimalkan risiko slashing pada tingkat validator Beacon Chain.

Tingkat Keyakinan: HIGH

Institution (Institution)

Verdict: SUKSES

Alasan: Depositor institusi skala besar (seperti Amber Group, Arrington Capital) berhasil mengoptimalkan yield modal jutaan dolar mereka secara non-custodial sejati dengan hak kontrol kunci penuh dan perlindungan kustodian tepercaya Anchorage Digital.

Tingkat Keyakinan: HIGH

Node Operator & Validator

Verdict: SUKSES

Alasan: Operator beroleh aliran jaminan delegasi modal 32 ETH secara otomatis, didukung oleh asuransi pemotongan (slashing deductible) gratis yang ditanggung oleh pemegang B-NFT.

Tingkat Keyakinan: HIGH

Ecosystem Builder (Builder)

Verdict: SUKSES

Alasan: weETH menjadi standar LRT paling komposit di industri DeFi, diadopsi di lebih dari 400 protokol lintas rantai, dan terbukti aman diuji melewati krisis industri rsETH April 2026.

Tingkat Keyakinan: HIGH

## 16 Historical Timeline

Kronologi lengkap urutan sejarah ekosistem ether.fi dari gagasan awal hingga status operasional terkini:

Oktober 2022 — Pendirian Resmi ether.fi — Mike Silagadze dan Rok Kopp mendirikan ether.fi di Cayman Islands setelah menyadari ketiadaan solusi delegated staking non-custodial untuk dana lindung nilai internal mereka.

1 Februari 2023 — Pengumuman Alternatif Penutupan Putaran Seed — Beberapa catatan pelacak mencatat penutupan putaran benih awal sebesar $5.000.000. (Sebab/Akibat: Kebutuhan dana pengembangan awal protokol).

28 Februari 2023 — Penutupan Putaran Seed Resmi Senilai $5,3 Juta — Pendanaan yang dipimpin oleh North Island Ventures, Chapter One, dan Node Capital resmi diumumkan dengan partisipasi Arthur Hayes. (Sebab/Akibat: Mempercepat kesiapan teknis tim menuju peluncuran mainnet).

April 2023 — Pengumuman Peta Jalan Mainnet Tahap 1 — Tim mengumumkan rencana aktivasi mainnet delegated staking pasca Shanghai Upgrade Ethereum. (Sebab/Akibat: Menyelaraskan rilis produk dengan pembukaan antrean keluar validator Beacon Chain).

Mei 2023 — Peluncuran Aplikasi Desktop ether.fi — Alat penghasil kunci validator offline lokal resmi dirilis ke publik. (Sebab/Akibat: Memungkinkan staker mengontrol kunci secara non-custodial sebelum delegasi operator).

November 2023 — Peluncuran weETH Lintas Rantai — Pembungkus token non-rebasing weETH dirilis. (Sebab/Akibat: Meningkatkan kegunaan aset restaking di ekosistem DeFi Layer 2).

28 Februari 2024 — Penutupan Putaran Series A Senilai $23 Juta — Pendanaan yang dipimpin oleh Bullish Capital dan CoinFund berhasil diamankan. (Sebab/Akibat: Lonjakan TVL melewati $1,6 miliar memicu kebutuhan peningkatan skala operasional dan infrastruktur keamanan).

13 Maret 2024 — Catatan Alternatif Series A Senilai $27 Juta — Catatan PitchBook mendaftarkan penutupan transaksi Series A dengan nominal berbeda. (Sebab/Akibat: Penyesuaian opsi utang konvertibel).

14 Maret 2024 — Peluncuran Program Binance Launchpool — ether.fi menyalurkan 2% pasokan ETHFI untuk aktivitas farming staking BNB/FDUSD. (Sebab/Akibat: Distribusi publik global sebelum pembukaan bursa).

18 Maret 2024 — Token Generation Event (TGE) & Klaim Airdrop Season 1 — Token ETHFI resmi diperdagangkan di Gate, OKX, dan Binance, didukung pembukaan klaim 6% airdrop. (Sebab/Akibat: Memulai desentralisasi tata kelola DAO).

27 Maret 2024 — Harga ETHFI Menyentuh ATH Sebesar $8.53 — Spekulasi puncak restaking mendorong valuasi token ke titik tertinggi historis. (Sebab/Akibat: Euforia pasar sekunder terhadap narasi restaking).

Juli 2024 — Peluncuran Program Perks Passport di Season 3 — Kampanye gamifikasi stamps on-chain resmi diaktifkan. (Sebab/Akibat: Mendorong sirkulasi weETH ke protokol mitra DeFi guna meredam aksi penarikan).

15 September 2024 — Transisi ke Poin Berulang Season 4+ — DAO mengadopsi model musim 4 bulanan yang berkelanjutan dengan suplai emisi terkontrol. (Sebab/Akibat: Mengakhiri era spekulasi emisi tidak terbatas).

30 September 2025 — Konsolidasi Kas Keuangan Yayasan — Audit mencatat kas yayasan memegang aset senilai $306.000.000. (Sebab/Akibat: Menjamin landasan operasional jangka panjang yang sehat).

31 Oktober 2025 — Pengajuan Proposal Buyback Darurat Senilai $50 Juta — Komunitas merilis proposal untuk melakukan pembelian kembali ETHFI di pasar sekunder jika harga di bawah $3.00. (Sebab/Akibat: Depresiasi harga ETHFI hingga $0.93 memicu kebutuhan intervensi likuiditas stabilitas).

18 April – 21 Mei 2026 — Krisis Likuiditas rsETH Kelp DAO & Pembuktian Stress-Test — Menyusul eksploitasi Kelp DAO, ether.fi memproses penarikan massal sebesar 542.792 ETH (19.6% dari TVL) dalam waktu 33 hari secara lancar. (Sebab/Akibat: Penggunaan 12.315 konsolidasi validator internal mencegah kemacetan antrean Beacon Chain Ethereum).

5 Juni 2026 — Harga ETHFI Menyentuh ATL Sebesar $0.2665 — Akibat jenuhnya pasar altcoin dan tekanan emisi periodik. (Sebab/Akibat: Puncak aksi jual sekunder).

Juni 2026 — Integrasi Kustodian Kualifikasi Anchorage Digital — ether.fi bermitra dengan Anchorage untuk membuka gerbang deposan institusional. (Sebab/Akibat: Menjaring likuiditas korporat pasca krisis rsETH).

## 17 Current Status

ether.fi saat ini (pertengahan tahun 2026) berada pada fase transisi kritis pasca-koreksi pasar. Secara operasional, protokol terbukti sangat tangguh setelah sukses melewati stress-test penarikan massal 19.6% dari total TVL-nya pada krisis rsETH April 2026 tanpa mengalami kegagalan sistemik. Namun, depresiasi nilai Ethereum global telah mengontraksi TVL denominasi fiat platform sebesar 23.20% secara kuartalan menjadi $7,31 miliar pada Q1 2026.

Untuk memitigasi penurunan pendapatan dari sektor staking murni, proyek ini secara agresif mendiversifikasi operasinya menuju neobank digital konsumen. Lini bisnis pembayaran ritel (ether.fi Cash) kini menjadi lokomotif utama pertumbuhan pengguna dengan menguasai 96.98% pangsa MAU aktif bulanan dan memproses volume belanja kartu kredit konsumen yang melonjak menjadi $170.06 juta secara kuartalan. Tim juga memfokuskan perluasan wilayah jangkauan produk Liquid Vaults ke ranah RWA melalui investasi di Plume Network dan merilis brankas berbasis Bitcoin (eBTC) serta stablecoin multi-chain.

## 18 Lessons Learned

Pelajaran terbesar dan kesalahan operasional dari perjalanan sejarah ether.fi meliputi:

Kedaulatan Kunci Adalah Nilai Jual Mutlak: Komitmen awal untuk tidak memegang kunci privat staker (non-custodial delegated staking) terbukti menjadi daya tarik utama bagi deposan institusi besar yang menghindari risiko pihak ketiga. Protokol baru harus mengadopsi model non-custodial sejak hari pertama.

Membangun Jalur Likuiditas Darurat (Spillover Exits): Pengalaman memproses klaim penarikan 542.792 ETH membuktikan bahwa mengandalkan antrean keluar standar (exit queue) Ethereum sangat berbahaya saat krisis pasar. Keputusan teknik ether.fi untuk menggunakan mekanisme konsolidasi validator internal (sweeps) terbukti menyelamatkan sistem dan industri dari bencana kemacetan likuiditas.

Bahaya Toksifikasi Emisi Tokenomics Rendah Sirkulasi (Low-Float): Kesalahan terbesar dalam desain token awal adalah merilis suplai beredar TGE yang terlalu rendah (11.52%) di tengah derasnya emisi program insentif harian. Ketika pasar beralih ke fase bearish, kombinasi emisi yang tinggi dan jadwal pembukaan kunci (vesting) investor menekan harga token hingga jatuh 89% dari ATH. Protokol baru wajib menyeimbangkan laju emisi dengan utilitas penyerapan (token sinks) yang kuat sejak awal.

Diversifikasi Ke Keuangan Riil: Transisi cepat ether.fi ke kartu belanja Cash membuktikan bahwa masa depan DeFi terletak pada integrasi utilitas dunia nyata. Menghubungkan aset produktif on-chain secara langsung dengan jaringan Visa merupakan strategi retensi TVL terbaik saat imbal hasil yield on-chain merosot.

## 19 Knowledge Extraction Candidate

Struktur ekstraksi pengetahuan dari ekosistem ether.fi untuk pemodelan basis data graf CIF didefinisikan di bawah ini:

Entity baru:

ether.fi (Protocol)

ETHFI (Governance Token)

weETH (Liquid Restaking Token)

BoringVault (Smart Contract Architecture)

Veda Labs (Infrastructure Provider)

ether.fi Cash (Consumer Payment Platform)

OP Mainnet (L2 Host Network)

Plume Network (RWA Chain Partner)

SSV Network (DVT Partner)

Relationship:

[ether.fi] -> issues -> [weETH]

[weETH] -> secures_AVS_on -> [EigenLayer]

[ether.fi] -> partners_with -> [Veda Labs]

[Veda Labs] -> secures_contracts_for -> [BoringVault]

[ether.fi] -> operates -> [ether.fi Cash]

[ether.fi Cash] -> migrates_to -> [OP Mainnet]

[ether.fi] -> integrates -> [SSV Network]

[ether.fi] -> deploys_capital_to -> [Plume Network]

Pattern:

Pola Penyelamatan Bank Run (Spillover Execution): rsETH incident -> panic redemptions -> execute 12,315 consolidation operations -> sweep Beacon Chain balances -> bypass exit queue -> 100% claimable within 17 days.

Pola Pertumbuhan Neobank DeFi: spekulasi yield DeFi menurun -> integrasi BoringVault multi-aset -> peluncuran neobank Visa (Cash) -> migrasi ke Layer 2 murah (OP Mainnet) -> peningkatan MAU berbasis utilitas riil -> pergeseran pendapatan ke divisi Cash.

Pola Mitigasi Inflasi Token (Oportunistik Buyback): harga token jatuh di bawah batas fundamental -> otorisasi DAO untuk alokasi kas yayasan -> aktifkan buyback di pasar terbuka di bawah $3.00 -> kurangi sirkulasi suplai -> ciptakan lantai dukungan harga.

## 20 Transferable Intelligence

Apabila kecerdasan buatan CIF mengevaluasi proyek DeFi baru di masa depan, pengetahuan yang dapat digunakan kembali (reusable rules) meliputi:

Aturan Umum (General Rules):

Aturan Kedaulatan Kunci (Key Sovereignty Rule): Jika sebuah protokol staking terdelegasi mengharuskan deposan menyerahkan kunci kredensial penarikan (withdrawal credentials) ke operator atau kolam terpusat, berikan peringkat risiko "HIGH" karena kerentanan sistemik sentralisasi. Model non-custodial berbasis enkripsi offline adalah standar minimum kepatuhan institusi.

Aturan Pengukuran Retensi TVL (LRT Composability Rule): Keberlangsungan protokol LRT tidak boleh diukur dari nilai TVL statis. Evaluasi persentase pemanfaatan token LRT tersebut di pasar uang eksternal (Aave, Pendle). LRT yang memiliki kegunaan kolateral di atas 400+ DeFi memiliki tingkat kelengketan (stickiness) modal yang jauh lebih tinggi saat terjadi penurunan suku bunga.

Aturan Pertahanan Aktif Kode (Active Defense Rule): Protokol bernilai miliaran dolar wajib memiliki invariant kode on-chain yang membekukan transaksi otomatis jika nilai tukar tokenized (eETH) jatuh di bawah rasio 1:1 terhadap aset pendukung. Menunda tindakan penyelamatan darurat hanya pada koordinasi multi-sig manual adalah kesalahan fatal.

Aturan Khusus Kasus (Specialized Indicators):

Aturan Rasio Kas-Terhadap-Buyback (Treasury Buyback Threshold): Keputusan membeli kembali token di bawah harga $3.00 dengan batas $50.000.000 hanya dapat dinilai rasional jika kas yayasan memiliki minimal 7% aset likuid terdiversifikasi ($21.000.000 non-ETHFI) dan tingkat sirkulasi token sekunder sudah mencapai di atas 90%. Tanpa kondisi ini, buyback hanya akan berfungsi sebagai pintu keluar gratis bagi investor awal.

## 21 Open Questions

Pengaruh Penurunan Emisi Terhadap Keberlangsungan Cash: Apakah volume transaksi belanja harian kartu Cash ($170.06 juta/kuartal) akan terus bertumbuh secara organik jika program emisi poin loyalitas dihentikan secara total oleh DAO?

Risiko Sistemik Jembatan weETH Multi-Provider: Bagaimana implikasi keamanan operasional dari transisi rencana integrasi jembatan multi-provider (seperti Chainlink CCIP/Wormhole) dalam menghilangkan ketergantungan tunggal pada satu tumpukan pengirim pesan LayerZero?

Ketahanan Regulasi Cayman di bawah Aturan MiCA Eropa: Sejauh mana kepatuhan dokumen putih ETHFI di bawah undang-undang MiCA mampu membentengi yayasan dari gugatan regulasi sekuritas di luar yurisdiksi Cayman Islands?

## 22 Evidence Level

Klaim Kinerja Keuangan Q1 2026 (TVL, Pendapatan, MAU, Volume Belanja Cash): HIGH. Angka bersumber dari laporan keuangan triwulanan on-chain di platform data institusional Token Terminal.

Klaim Keandalan Penarikan 542.792 ETH Selama Krisis rsETH: HIGH. Proses diverifikasi secara transparan melalui catatan transaksi on-chain 12.315 operasi konsolidasi validator Beacon Chain.

Keefektifan Program Buyback $50 Juta Untuk Pemulihan Harga Jangka Panjang: LOW. Meskipun terbukti menahan kejatuhan harga secara psikologis, program ini dinilai oleh sebagian besar analis riset belum mampu mengatasi hambatan struktural inflasi emisi dan pembukaan kunci vesting tim secara berkelanjutan.

## 23 Karya yang dikutip

Technical Documentation | ether.fi — https://etherfi.gitbook.io/etherfi/resources/ether.fi-whitepaper/technical-documentation

ETHFI Crypto-Asset Whitepaper complies with MiCA — https://www.cairnspoint.com/whitepapers/ETHFI.xhtml

Safe Staking, From Doctrine to Code — https://www.ether.fi/

OKX Learn: ether.fi (ETHFI) White Paper — https://www.okx.com/learn/ether-fi-white-paper

Liquid Technical Documentation Veda BoringVault — https://etherfi.gitbook.io/etherfi/liquid/technical-documentation

Technical Guides and References Help Desk — https://help.ether.fi/en/articles/232881-technical-documentation

ether.fi Organization Financial Profile — https://startupintros.com/orgs/ether-fi

ether.fi Funding Intelligence Competitors — https://tracxn.com/d/companies/etherfi/__ybuswctFLX6Yyk0tndtj8aoDimNowhN3z_XQDPgnARo

Pluang Token Compare and Holding Metrics — https://pluang.com/en/compare/ethfi-idr-vs-fdusd-idr

Bullish Capital and CoinFund Lead $23M Series A Funding Round — https://www.bullish.com/news-insights/etherfi-announces-23m-in-funding-led-by-bullish-capital-and-coinfund

Signalbase Funding and Strategic Growth News — https://www.trysignalbase.com/news/funding/etherfi-raises-23m-series

ether.fi Official Tokenomics Allocation — https://www.ether.fi/ethfi

ether.fi Stake Integrations across DeFi — https://www.ether.fi/stake

Terms of Use Ether.Fi SEZC — https://www.ether.fi/app/ethfi

The Club Membership Levels and Card Spend — https://www.ether.fi/the-club

Binance Square: Token Allocation Adjusted on Community Feedback — https://www.binance.com/en/square/post/5494365424538

BitDegree: Comprehensive Tutorial on ETHFI Airdrop Seasons — https://www.bitdegree.org/crypto/tutorials/ethfi-airdrop

ether.fi DAO Proposal: Season 3 Token Allocation — https://governance.ether.fi/t/2-ethfi-dao-proposal-season-3-and-airdrop-token-allocation/1145

Medium: Announcing ETHFI Governance Token Launch — https://etherfi.medium.com/announcing-ethfi-the-ether-fi-governance-token-8cae7327763a

ether.fi DAO Proposal: Seasonal Rewards and LRT² — https://governance.ether.fi/t/5-ethfi-dao-proposal-seasonal-rewards-and-lrt/2314

ether.fi DAO Proposal: Member Rewards Framework — https://governance.ether.fi/t/ether-fi-member-rewards/2974

Mike Silagadze Background and Top Hat Entrepreneurship Profile — https://grokipedia.com/page/mike-silagadze

IQ Wiki: Mike Silagadze Biography and Founder Vision Interview — https://iq.wiki/wiki/mike-silagadze

Blockworks Speaker: Mike Silagadze Profile — https://blockworks.com/speaker/mike-silagadze

Consensus Hong Kong Speaker: Mike Silagadze — https://consensus-hongkong2025.coindesk.com/agenda/speaker/-michael-silagadze

Cayman Enterprise City: Meet Mike Silagadze of ether.fi — https://www.caymanenterprisecity.com/blog/meet-mike-silagadze

OurCryptoTalk: Founder's Corner Mike Silagadze Explained — https://ourcryptotalk.com/founders-corner/mike-silagadze

Token Terminal: Financial Dashboard for ether.fi — https://tokenterminal.com/explorer/projects/etherfi

DefiLlama: Protocol Rankings and Yield Database — https://defillama.com/

CoinGecko Lighter (LIT) Token Lifecycle Comparison — https://www.coingecko.com/en/coins/lighter

Token Terminal Studio: Q1 2026 Executive Financial Report Dashboard — https://tokenterminal.com/explorer/studio/dashboards/cd5ce740-1ced-46eb-b6e6-7e46799f6df2

CoinGecko Bonk (BONK) Tokenomics Allocation — https://www.coingecko.com/en/coins/bonk

Token Terminal Studio: Q4 2025 Financial Performance Dashboard — https://tokenterminal.com/explorer/studio/dashboards/fb3ed701-4ede-4828-ad27-7064b54cb2ee

ether.fi DAO Proposal: Treasury Deployment for ETHFI Buyback Program — https://governance.ether.fi/t/ether-fi-dao-proposal-treasury-deployment-for-ethfi-buy-back-program/3178

TradingView: ether.fi DAO proposes $50M buyback as DeFi repurchase wave tops $1.4B — https://www.tradingview.com/news/the_block:c5a699d99094b:0-ether-fi-dao-proposes-50-million-ethfi-buyback-as-defi-s-repurchase-wave-tops-1-4-billion/

Binance Square: PANews report on ether.fi Buyback — https://www.binance.com/en-AE/square/post/31739719933097

Binance Square: Odaily News on Treasury Allocation for Buybacks — https://www.binance.com/en/square/post/10-31-2025-ether-fi-community-proposes-treasury-fund-allocation-for-ethfi-buyback-31740940217170

Coinmonks: DeFi Protocols spent $800M on Buybacks — https://medium.com/coinmonks/defi-protocols-just-spent-800m-on-buybacks-heres-why-memecoin-traders-should-care-d3a3be34e670

Oak Research: Alpha Recap on ether.fi Buyback and Vesting Pressures — https://oakresearch.io/en/analyses/investigations/alpha-recap-3-terminal-finance-promise-ether-fi-buyback-maple-strategic-pivot

Supported Cryptocurrencies List A-Z — https://cryptocurrencyalerting.com/coins.html?07SQZkTmpMW=zYmzK9fDvt

Supported Cryptocurrencies List - wrapped eETH — https://cryptocurrencyalerting.com/coins.html?nGUOmp=Q4FonGjOzyVyGvK

Supported Cryptocurrencies List - ether.fi — https://cryptocurrencyalerting.com/coins.html

Binance Square Creator b38d3993dc24 Profile — https://www.binance.com/en-NG/square/profile/square-creator-b38d3993dc24

Blockworks Speaker: Rok Kopp Profile — https://blockworks.com/speaker/rok-kopp

RootData: Rok Kopp Member Profile Details — https://www.rootdata.com/member/Rok%20Kopp?k=MTgxNDE%3D

Flipster Blog: What is ether.fi (ETHFI) Founders — https://flipster.io/blog/what-is-etherfi-ethfi

Reku: About ETHFI, Technology, and Team Score — https://reku.id/information/about-ethfi

Consensus Hong Kong Speaker: Rok Kopp — https://consensus-hongkong.coindesk.com/agenda/speaker/-rok-kopp

StartupIntros: Financial History of ether.fi — https://startupintros.com/orgs/ether-fi

Tracxn: Competitors and Investments Profile of ether.fi — https://tracxn.com/d/companies/etherfi/__ybuswctFLX6Yyk0tndtj8aoDimNowhN3z_XQDPgnARo

Binance Square: Weekly Venture Capital Rounds Summary — https://www.binance.com/en/square/post/268175

Binance Square: ether.fi $5.3M seed round details — https://www.binance.com/en/square/post/274898

Cryptohead Author Profile - Ethereum Institutional Push — https://cryptohead.io/author/adam/

Messari: Crypto Theses for 2024 Report PDF — https://resources.messari.io/pdf/crypto-theses-for-2024.pdf

Preqin: Asset Profile and Venture Funding for ether.fi — https://www.preqin.com/data/profile/asset/ether-fi/533163

PitchBook: Profile and Competitors of ether.fi — https://pitchbook.com/profiles/company/520903-54

Bullish Capital: Announcement of $23M Series A — https://www.bullish.com/news-insights/etherfi-announces-23m-in-funding-led-by-bullish-capital-and-coinfund

Financial IT: Fundraising News on ether.fi — https://financialit.net/news/fundraising-news/etherfi-announces-23m-funding-led-bullish-capital-and-coinfund

Binance Launchpool: Detailed Launch Mechanism for ETHFI — https://www.binance.com/en/square/post/5351962650921

OKX Convert: Factors influencing ETHFI Rate — https://www.okx.com/convert/ethfi-to-omr

Binance Square: Token Unlock Risk and minimal unlock tokens — https://www.binance.com/en/square/profile/wendyr9

MetaMask Price History and Token Unlock Schedules — https://metamask.io/en-GB/price/arbitrum

OKX Convert: ETHFI to USD — https://www.okx.com/convert/ethfi-to-usd

OKX Convert: ETHFI to KYD exchange rates — https://www.okx.com/convert/ethfi-to-kyd

Pluang Compare: ETHFI vs PUMP Metrics — https://pluang.com/en/compare/ethfi-idr-vs-pump-idr

StartupIntros: Complete Funding Round Track — https://startupintros.com/orgs/ether-fi

Binance Square: AEVO mining transition to ETHFI — https://www.binance.com/en/square/post/5951205336305

Drosera Network Hello World Blog — https://drosera-network.github.io/blog/hello-world/

Flipster Blog: Who Created ether.fi? — https://flipster.io/blog/what-is-etherfi-ethfi

ether.fi Product Documentation: Katana ETH Veda Vault — https://etherfi.gitbook.io/etherfi/liquid/liquid-katana-eth-vault

ether.fi Product Documentation: How Liquid automated DeFi strategies work — https://etherfi.gitbook.io/etherfi/products/liquid

Veda Documentation: BoringVault smart contract security audits — https://docs.veda.tech/security-and-risk-controls/smart-contract-security

Token Terminal Studio: Q1 2026 Executive Financial Report Dashboard — https://tokenterminal.com/explorer/studio/dashboards/cd5ce740-1ced-46eb-b6e6-7e46799f6df2

Gate Learn: Veda as the First Native Yield Layer — https://www.gate.com/learn/articles/veda-the-first-native-yield-layer/4537

Cork Tech: Onchain Vault Ecosystem Integration — https://www.cork.tech/blog/onchain-vault-ecosystem

CoinGecko: Ether.fi (ETHFI) Price Chart, ATH and ATL Metrics — https://www.coingecko.com/en/coins/ether-fi

DefiLlama: Liquid Staking TVL and Fees Matrix — https://defillama.com/

Binance Square: TVL Exceeds 4 Billion USD and SSV Network Partnership — https://www.binance.com/en/square/post/7906500431938

CoinGecko Learn: Solana Staking Ecosystem Sanctum and Solayer — https://www.coingecko.com/learn/top-solana-projects

CoinTracking Info: Supported Coin Charts Database — https://cointracking.info/coin_charts.php?cur=ENC

Supported Cryptocurrencies List — https://cryptocurrencyalerting.com/coins.html?07SQZkTmpMW=zYmzK9fDvt

Supported Cryptocurrencies List - wrapped weETH — https://cryptocurrencyalerting.com/coins.html?nGUOmp=Q4FonGjOzyVyGvK

Cryptocurrency Alerting: Price Alerts for ETHFI — https://cryptocurrencyalerting.com/coins.html

Binance Square: US Trading Master technical updates — https://www.binance.com/en-NG/square/profile/square-creator-b38d3993dc24

Finder: Best Crypto to Buy Now Comparison — https://www.finder.com/cryptocurrency/coins/best-crypto-to-buy-now

ether.fi Blog: How ether.fi redeemed 20% of TVL smoothly — https://beta.ether.fi/blog/how-ether-fi-redeemed-20-percent-of-tvl-without-adding-to-exit-queue

ether.fi Blog: Safe Staking, From Doctrine to Code — https://www.ether.fi/blog/safe-staking-from-doctrine-to-code

ether.fi Blog: Non-custodial, actively defended doctrine — https://www.ether.fi/blog/non-custodial-actively-defended

ether.fi Blog: weETH Bridge Security Hardening and DVN Configuration — https://www.ether.fi/blog/weeth-bridge-security-hardening

ether.fi Official Site and Staking rewards — https://www.ether.fi/?ref=berachain.ghost.io

ether.fi Official Site and OP Mainnet Migration — https://www.ether.fi/?ref=research.despread.io

ether.fi DAO Governance Forum Introduction — https://governance.ether.fi/t/ether-fi-governance/13

DVS Stakers: Kenya Node Phase 2 Project — https://github.com/DVStakers/docs/blob/main/kenya-node-phase-2.md

RootData: Puffer Finance Project Timeline and Competitors — https://www.rootdata.com/projects/detail/Puffer%20Finance?k=NzkwNA%3D%3D

Medium: ether.fi A Decentralized and Non-custodial Staking Protocol — https://medium.com/@masihsajadi7557/ether-fi-a-decentralized-and-non-custodial-staking-protocol-fc61bfdb5331

Binance Square: ether.fi Mainnet launch timelines — https://www.binance.com/en/square/post/450004

Binance Square: T-NFT, B-NFT and Validator Minting Details — https://www.binance.com/en/square/post/9818698698426

Binance Square: Detailed Exit Mechanism and comparison of ether.fi — https://www.binance.com/en/square/post/9228997944673

Binance Square: Deep Dive into Restaking track projects and key control — https://www.binance.com/en/square/post/9103657911138

Blockchain App Factory: Decentralizing Staking with ether.fi — https://www.blockchainappfactory.com/blog/decentralizing-staking-guide-to-liquid-restaking-tokens-with-etherfi/

Medium: Introducing ether.fi Node Services Phase 3 — https://medium.com/etherfi/introducing-ether-fi-4346d6243d01

Binance Square: Profit distribution mechanism and points logic of ether.fi — https://www.binance.com/en/square/post/3468185159921

BitDegree: Earning Loyalty Points step-by-step for ETHFI — https://www.bitdegree.org/crypto/tutorials/ethfi-airdrop

ether.fi DAO Proposal: Season 3 Perks Passport Explained — https://governance.ether.fi/t/2-ethfi-dao-proposal-season-3-and-airdrop-token-allocation/1145

Karya yang dikutip

1. Dashboard - Ether.fi Q1 2026 Report - Token Terminal, https://tokenterminal.com/explorer/studio/dashboards/cd5ce740-1ced-46eb-b6e6-7e46799f6df2 2. Technical Documentation - ether.fi - GitBook, https://etherfi.gitbook.io/etherfi/resources/ether.fi-whitepaper/technical-documentation 3. Decentralizing Staking: A Guide to Liquid Restaking Tokens with EtherFi, https://www.blockchainappfactory.com/blog/decentralizing-staking-guide-to-liquid-restaking-tokens-with-etherfi/ 4. How ether.fi Redeemed 20% of TVL Without Adding a Day to Ethereum's Exit Queue, https://beta.ether.fi/blog/how-ether-fi-redeemed-20-percent-of-tvl-without-adding-to-exit-queue 5. Rok Kopp | Speaker | Consensus Hong Kong 2026 - CoinDesk, https://consensus-hongkong.coindesk.com/agenda/speaker/-rok-kopp 6. ether.fi: Funding, Team & Investors - Startup Intros, https://startupintros.com/orgs/ether-fi 7. Mike Silagadze - People in crypto - IQ.wiki, https://iq.wiki/wiki/mike-silagadze 8. ether.fi - 2026 Company Profile, Team, Funding & Competitors - Tracxn, https://tracxn.com/d/companies/etherfi/__ybuswctFLX6Yyk0tndtj8aoDimNowhN3z_XQDPgnARo 9. ETHFI: The leading Restaking product underestimated by the market | Odaily星球日报 on Binance Square, https://www.binance.com/en/square/post/9228997944673 10. Using DVT technology and validator management NFT, is the staking leader ether.fi underestimated by the market? | PANews on Binance Square, https://www.binance.com/en/square/post/9103657911138 11. Ether.Fi Announces $23M in Funding Led By Bullish Capital and CoinFund, https://www.bullish.com/news-insights/etherfi-announces-23m-in-funding-led-by-bullish-capital-and-coinfund 12. Compare ether.fi (ETHFI) vs First Digital USD (FDUSD) Price & Performance - Pluang, https://pluang.com/en/compare/ethfi-idr-vs-fdusd-idr 13. Mike Silagadze - Grokipedia, https://grokipedia.com/page/mike-silagadze 14. Mike Silagadze Speaker Profile - Blockworks, https://blockworks.com/speaker/mike-silagadze 15. Mike Silagadze | Speaker - Consensus Hong Kong 2025, https://consensus-hongkong2025.coindesk.com/agenda/speaker/-michael-silagadze 16. Rok Kopp Speaker Profile - Blockworks, https://blockworks.com/speaker/rok-kopp 17. Rok Kopp Introduction and Work History_RootData | RootData, https://www.rootdata.com/member/Rok%20Kopp?k=MTgxNDE%3D 18. What Is ether.fi (ETHFI)? | Flipster Blog, https://flipster.io/blog/what-is-etherfi-ethfi 19. Why does the ether.fi (ETHFI) Project on Binance Launchpool have a x10 asset opportunity?, https://www.binance.com/en/square/post/5351962650921 20. Meet Mike Silagadze, Founder and CEO of EtherFi - Cayman Enterprise City, https://www.caymanenterprisecity.com/blog/meet-mike-silagadze 21. What is ether.fi (ETHFI)? | 加密百科 on Binance Square, https://www.binance.com/en/square/post/9818698698426 22. Analysis of the super potential of decentralized staking star Ether.FI | 朱老师区块链 on Binance Square, https://www.binance.com/en/square/post/3468185159921 23. Introducing ether.fi. A new kind of liquid staking protocol - Medium, https://medium.com/etherfi/introducing-ether-fi-4346d6243d01 24. Apa itu Ether.fi? - Reku, https://reku.id/information/about-ethfi 25. Non-custodial liquidity staking platform ether.fi will launch mainnet in the first week of May | Odaily星球日报 on Binance Square, https://www.binance.com/en/square/post/450004 26. Stake your assets and get rewards - Ether.fi, https://www.ether.fi/stake 27. TVL exceeds 4 billion US dollars, a brief analysis of Ether.fi, the leader in liquidity re-staking | MarsBit News on Binance Square, https://www.binance.com/en/square/post/7906500431938 28. Safe Staking, From Doctrine to Code - ether.fi Blog, https://www.ether.fi/blog/safe-staking-from-doctrine-to-code 29. Non-custodial, actively defended: how ether.fi thinks about security, https://www.ether.fi/blog/non-custodial-actively-defended 30. weETH Bridge Security Hardening - ether.fi Blog, https://www.ether.fi/blog/weeth-bridge-security-hardening 31. decentralized mobile network service provider REALLY completed $18 million seed round of financing, led by Polychain | PANews on Binance Square, https://www.binance.com/en/square/post/274898 32. Ether.Fi Announces $23M in Funding Led by Bullish Capital and CoinFund | Financial IT, https://financialit.net/news/fundraising-news/etherfi-announces-23m-funding-led-bullish-capital-and-coinfund 33. ether.fi 2026 Company Profile: Valuation, Funding & Investors | PitchBook, https://pitchbook.com/profiles/company/520903-54 34. Explore All of ETHFI Airdrop Seasons and Its Newest One - BitDegree.org, https://www.bitdegree.org/crypto/tutorials/ethfi-airdrop 35. Ether.fi: Token allocation will be adjusted based on community feedback | 金色财经 on Binance Square, https://www.binance.com/en/square/post/5494365424538 36. 2 - ETHFI DAO Proposal: Season 3 and airdrop token allocation, https://governance.ether.fi/t/2-ethfi-dao-proposal-season-3-and-airdrop-token-allocation/1145 37. Ether.fi Price: ETHFI/USD Live Price Chart, Market Cap & News Today | CoinGecko, https://www.coingecko.com/en/coins/ether-fi 38. Join The Club | Unlock Exclusive Rewards with ether.fi Membership, https://www.ether.fi/the-club 39. Ether.fi overview - Token Terminal, https://tokenterminal.com/explorer/projects/etherfi 40. Puffer Finance - RootData, https://www.rootdata.com/projects/detail/Puffer%20Finance?k=NzkwNA%3D%3D 41. DeFi Protocols Just Spent $800M on Buybacks: Here's Why Memecoin Traders Should Care, https://medium.com/coinmonks/defi-protocols-just-spent-800m-on-buybacks-heres-why-memecoin-traders-should-care-d3a3be34e670 42. Save, Grow, Spend. Do more with your crypto | ether.fi, https://www.ether.fi/?ref=research.despread.io 43. Liquid - ether.fi - GitBook, https://etherfi.gitbook.io/etherfi/products/liquid 44. Inside the Onchain Vault Ecosystem: Asset Issuers, Protocols, and Risk Curators - cork.tech, https://www.cork.tech/blog/onchain-vault-ecosystem 45. ETHFI Token MiCA Whitepaper, https://www.cairnspoint.com/whitepapers/ETHFI.xhtml 46. Ether.fi(ETHFI) Whitepaper - OKX, https://www.okx.com/learn/ether-fi-white-paper 47. Save, Grow, Spend. Do more with your crypto - Ether.fi, https://www.ether.fi/ethfi 48. Announcing ETHFI: The ether.fi Governance Token - Medium, https://etherfi.medium.com/announcing-ethfi-the-ether-fi-governance-token-8cae7327763a 49. Wendy 's Profile | Binance Square, https://www.binance.com/en/square/profile/wendyr9 50. Ether.Fi Member Rewards - Protocol & Proposals, https://governance.ether.fi/t/ether-fi-member-rewards/2974 51. Ether.Fi DAO Proposal: Treasury Deployment for ETHFI Buy-Back Program, https://governance.ether.fi/t/ether-fi-dao-proposal-treasury-deployment-for-ethfi-buy-back-program/3178 52. 5 - ETHFI DAO Proposal: Seasonal Rewards and LRT², https://governance.ether.fi/t/5-ethfi-dao-proposal-seasonal-rewards-and-lrt/2314 53. Alpha Recap #3: Terminal Finance's Promise, Ether.fi's Buyback, and Maple's Strategic Pivot | OAK Research, https://oakresearch.io/en/analyses/investigations/alpha-recap-3-terminal-finance-promise-ether-fi-buyback-maple-strategic-pivot 54. ETHFI to OMR | Convert ether.fi to Omani Rial - OKX, https://www.okx.com/convert/ethfi-to-omr 55. Ether.fi DAO proposes $50 million ETHFI buyback as DeFi's repurchase wave tops $1.4 billion - TradingView, https://www.tradingview.com/news/the_block:c5a699d99094b:0-ether-fi-dao-proposes-50-million-ethfi-buyback-as-defi-s-repurchase-wave-tops-1-4-billion/ 56. DefiLlama - DeFi Dashboard & Crypto Analytics, https://defillama.com/ 57. ETHFI to KYD | Convert ether.fi to Cayman Islands Dollar - OKX, https://www.okx.com/convert/ethfi-to-kyd 58. Dashboard - Ether.fi Q4 2025 Report - Token Terminal, https://tokenterminal.com/explorer/studio/dashboards/fb3ed701-4ede-4828-ad27-7064b54cb2ee 59. Veda: The First Native Yield Layer for DeFi Explained | Gate Learn, https://www.gate.com/learn/articles/veda-the-first-native-yield-layer/4537 60. Smart Contract Security | Veda, https://docs.veda.tech/security-and-risk-controls/smart-contract-security
