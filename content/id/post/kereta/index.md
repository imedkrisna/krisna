---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "TKDN kereta: gratis buat APBN, mahal buat anker"
subtitle: ""
summary: "TKDN di pengadaan KRL sering dianggap kebijakan industri yang gratis. Ongkosnya ternyata dibayar penumpang KRL, dalam bentuk kereta yang kurang dan gerbong yang makin sesak."
authors: [admin]
tags: [TKDN, industri, kereta, KRL, INKA, KAI, kebijakan industri]
categories: [Industri, Perdagangan, Data & Kode]
date: 2026-10-10T18:00:00+07:00
lastmod: 2026-10-10T18:00:00+07:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

Barusan saya nonton [video ini](https://www.youtube.com/watch?v=7Kgv8JXxyGE) soal KRL, INKA, dan KAI. Isinya padat: armada KRL yang kurang, INKA yang produksinya lambat dan utangnya numpuk, sampai rencana merger KAI–INKA. Buat saya, ini contoh yang pas banget buat ngobrolin satu instrumen kebijakan industri favorit pemerintah kita: **TKDN**, alias _local content requirement_ (LCR).

Dulu saya pernah [bikin model TKDN sederhana]({{< relref "/post/TKDN" >}}). Kesimpulannya: TKDN itu tidak gratis, cuma ongkosnya tidak kelihatan di APBN. Kasus KRL ini enak buat dibedah karena ongkosnya bisa (kira-kira) dihitung, dan kita bisa lihat siapa yang bayar.

Spoiler: yang bayar anker, alias anak kereta.

## TKDN di kasus INKA

Strukturnya begini. Di Indonesia, produsen sarana kereta ya cuma INKA (BUMN), jadi dari sisi penjual ini monopoli. Pembeli utamanya KAI dan anak usahanya, KAI Commuter (KCI), yang mengoperasikan KRL. Selama ini KCI menambal kebutuhan armada dengan **KRL bekas dari Jepang**, yang murah dan cepat datang.

Tahun 2023, jalur itu ditutup. KCI mengajukan impor 348 unit KRL bekas seri E217. Kemenperin menolak memberi rekomendasi teknis karena barang modal bukan baru itu tidak memenuhi syarat TKDN dan tidak sejalan dengan program Peningkatan Penggunaan Produk Dalam Negeri (P3DN)[^1]. BPKP lalu mengaudit dan juga tidak merekomendasikan impor. Opsi yang tersisa adalah retrofit KRL lama di INKA dan menunggu KRL baru buatan INKA[^2]. Akhirnya KCI memesan 16 rangkaian (_trainset_) baru dan retrofit dari INKA. Belakangan KCI juga diizinkan mengimpor KRL **baru** dari CRRC (Tiongkok)[^3].

Jadi aturan mainnya kurang lebih: **beli dari INKA. Kalau terpaksa impor, harus baru, bekas tidak boleh.**

Tujuannya apa? Ini yang tidak pernah jelas. Membesarkan INKA? Ukurannya apa: aset, produksi, tenaga kerja, laba, atau _know-how_? Kalau memang tujuannya membesarkan INKA, pemerintah sebenarnya bisa memilih **subsidi**. Bedanya, subsidi butuh APBN dan kelihatan di Nota Keuangan, jadi harus dipertanggungjawabkan ke DPR. TKDN kelihatannya tidak butuh APBN sama sekali. Gratis.

Tapi beneran gratis?

## Siapa yang nanggung?

Yang pertama kena tentu KAI/KCI sebagai pembeli. Mereka harus membeli barang yang lebih mahal per tahun pakainya (dihitung di bawah) dan yang datangnya lebih lambat. Tapi KCI tidak bisa begitu saja meneruskan ongkos ini ke harga, karena **tarif KRL diatur pemerintah** dan disubsidi lewat PSO. Tarifnya masih Rp3.000 untuk 25 km pertama ditambah Rp1.000 per 10 km berikutnya, dan [rencana tarif berbasis NIK](https://finance.detik.com/berita-ekonomi-bisnis/d-7513056/subsidi-krl-berbasis-nik-di-2025-tarifnya-bakal-naik) pun belum jalan.

Kalau harga tidak bisa naik, penyesuaiannya lewat **kuantitas**. Menurut video tadi:

- KRL Jabodetabek melayani sekitar **1 juta penumpang per hari** dengan sekitar 1.065 perjalanan per hari. Sempat turun ke 1.048 perjalanan pada September.
- Untuk operasi normal dibutuhkan sekitar **105 trainset**, tapi yang beroperasi hanya sekitar **89**.
- INKA menargetkan 8 trainset per tahun, tapi realisasinya sekitar **3 per tahun**. Dari 16 trainset yang dipesan, baru 4 yang beroperasi per Januari 2026, dan sisanya dijanjikan tiba Juni 2026[^4].

Jadi ongkosnya muncul sebagai kereta yang kurang, jadwal yang dipangkas, dan gerbong yang makin sesak. Ongkos ini tidak tercatat di APBN, tapi tetap ditanggung oleh penumpang.

## Hitungan 1: berapa yang dibayar KAI?

Tabel 1 menyajikan harga per trainset untuk tiap opsi pengadaan, dalam miliar Rupiah, beserta asumsi umur pakainya. Harga INKA dan retrofit dihitung dari nilai kontrak KCI: 16 trainset baru senilai Rp3,83 triliun dan 19 trainset retrofit senilai Rp2,23 triliun[^3]. Angka per trainset hasil pembagian ini sama dengan yang disebut di video (menit 17:45–18:15). Harga KRL bekas Jepang diambil dari video. Angka ini sejalan dengan anggaran KAI 2023 sebesar Rp150 miliar untuk 10 rangkaian bekas[^2]. Harga CRRC adalah Rp783 miliar dibagi 3 trainset[^3].

| Opsi | Harga per trainset (Rp M) | Asumsi umur pakai (tahun) |
|---|---:|---:|
| KRL bekas Jepang | 19,2 | 10 |
| Retrofit di INKA | 117,6 | 15 |
| KRL baru INKA | 239,3 | 30 |
| KRL baru CRRC | 261,0 | 30 |

Video juga menyebut "KRL baru dari Jepang" seharga Rp25,6 miliar per trainset. Angka ini tidak saya pakai karena tidak masuk akal untuk 12 gerbong baru (bandingkan dengan CRRC) dan saya tidak menemukan sumber lain yang mengonfirmasinya.

Ada satu hal yang menarik: **harga KRL baru INKA ternyata tidak lebih mahal dari CRRC**. Jadi masalahnya bukan "INKA lebih mahal dari impor baru". Masalahnya ada di dua hal: (1) larangan impor **bekas**, dan (2) INKA **lambat** mengirim.

Tentu tidak adil membandingkan langsung harga kereta bekas dengan kereta baru, karena kereta bekas lebih cepat diganti. Supaya _apple to apple_, kita hitung biaya per tahun pakai atau _equivalent annual cost_ (EAC):

$$
EAC = P \cdot \frac{r}{1-(1+r)^{-T}}
$$

di mana $P$ adalah harga beli per trainset, $T$ adalah umur pakai dalam tahun, dan $r$ adalah tingkat diskonto. Saya pakai $r$ = 7%, kira-kira setara imbal hasil SBN. Asumsi umur pakai di Tabel 1 sengaja saya buat merugikan opsi bekas: E217 buatan 1994–1999 saya kasih sisa umur cuma 10 tahun, padahal KRL bekas Jepang di Jabodetabek biasanya dipakai lebih lama.


```python
def eac(P, T, r=0.07):
    return P * r / (1 - (1 + r) ** -T)

opsi = {"KRL bekas Jepang": (19.2, 10), "Retrofit INKA": (117.6, 15),
        "KRL baru INKA": (239.3, 30), "KRL baru CRRC": (261.0, 30)}
for k, (P, T) in opsi.items():
    print(f"{k:18s} EAC = {eac(P, T):6.2f} miliar/tahun")
```

    KRL bekas Jepang   EAC =   2.73 miliar/tahun
    Retrofit INKA      EAC =  12.91 miliar/tahun
    KRL baru INKA      EAC =  19.28 miliar/tahun
    KRL baru CRRC      EAC =  21.03 miliar/tahun
    

Walaupun bekas cuma dipakai 10 tahun, per tahun pakainya KRL bekas **sekitar 7 kali lebih murah** daripada KRL baru INKA. Retrofit, yang digadang-gadang sebagai solusi "dalam negeri", per tahunnya hampir 5 kali lebih mahal dari bekas.

Sekarang kita terapkan ke kekurangan armada sebanyak 105 − 89 = 16 trainset. Kebetulan jumlahnya sama dengan pesanan KCI ke INKA:

- **Belanja di muka:** 16 × Rp239,3 M ≈ **Rp3,83 T** dari INKA, dibanding 16 × Rp19,2 M ≈ **Rp0,31 T** kalau bekas. Selisihnya sekitar **Rp3,5 T**.
- **Per tahun pakai:** selisihnya sekitar **Rp265 miliar per tahun**. Kalau sisa umur bekas 15 tahun, selisihnya malah sedikit lebih besar, sekitar Rp275 miliar per tahun.

Ada beberapa catatan biar adil. Kereta bekas biasanya butuh biaya tambahan sebelum bisa dipakai (misalnya ganti AC), dan perawatannya bisa lebih mahal. Spare part juga bisa jadi masalah. KAI sendiri bilang harga bukan satu-satunya pertimbangan: ada sisa umur, teknologi, ketersediaan suku cadang, perawatan, dan konsumsi energi. Tapi dengan selisih 7 kali lipat, biaya perawatan KRL bekas harus luar biasa mahal untuk menutup gap sebesar itu.

Lalu dari mana uang Rp3,83 T itu? Sebagian dari **PMN**: Rp2 T pada 2024, Rp1,8 T pada 2025, dan Rp1,5 T pada 2026[^4]. Tapi hati-hati, ini **bukan** bukti bahwa TKDN makan APBN. KCI tetap butuh kereta dan tetap akan dapat PMN, mau belinya dari INKA atau bekas dari Jepang. Sumber dananya tidak relevan. Yang relevan adalah **tambahan** ongkos akibat aturan TKDN, dan ini tergantung bagaimana PMN merespons:

1. **PMN tetap.** Dengan uang yang sama, harga per tahun pakai yang lebih mahal berarti kereta yang dibeli lebih sedikit. Seluruh ongkosnya jatuh ke penumpang, dan ini yang dihitung di bagian berikutnya.
2. **PMN ikut membesar menutup harga INKA.** Selisih belanjanya (sekitar Rp3,5 T di muka, atau Rp265 miliar per tahun pakai) secara efektif adalah **subsidi APBN ke INKA yang dititipkan lewat KAI**. Ongkosnya sama-sama ditanggung pembayar pajak seperti subsidi langsung, tapi tidak tercatat sebagai subsidi ke INKA dan tidak dikaitkan dengan target kinerja INKA apa pun. Lebih buruk dari subsidi langsung, karena tidak transparan.

Kenyataannya mungkin campuran keduanya. Lalu bagaimana dengan INKA sendiri, yang utangnya sekitar **Rp4,7 T** dan akan direstrukturisasi plus disuntik modal lewat Danantara dalam rangka merger dengan KAI[^5]? Suntikan ini tidak lewat APBN, jadi bukan subsidi langsung negara. Tapi ini trik lain untuk menopang INKA tanpa APBN, mirip yang terjadi pada BUMN Karya, dan sama buruknya dari sisi transparansi. Di post ini, ketika bilang "tidak butuh APBN", yang dimaksud adalah subsidi langsung negara. Jadi suntikan Danantara tidak saya hitung sebagai ongkos TKDN, meskipun ini menunjukkan kebijakan yang katanya gratis itu bahkan tidak berhasil membuat INKA sehat.

## Hitungan 2: berapa yang dibayar penumpang?

Ini bagian yang paling sering dilupakan. Karena tarif dipatok, kekurangan kereta tidak muncul sebagai kenaikan harga, tapi sebagai **penjatahan** (_rationing_): sebagian orang tidak kebagian layanan yang layak, sisanya berdesakan.

Pendekatannya mirip dengan [post JORR saya]({{< relref "/post/jorr" >}}) dulu: pakai kurva permintaan lalu hitung surplus konsumen yang hilang. Ada dua perbaikan dibanding post itu. Pertama, luasnya dihitung pakai integral, bukan didekati dengan segitiga. Kedua, saya kasih **batas bawah dan batas atas**, karena cara penumpang "membayar" penjatahan itu menentukan besar kecilnya ongkos.

Kurva permintaan perjalanan KRL diasumsikan berelastisitas konstan:

$$
Q(p) = A p^{\varepsilon}
$$

di mana $Q$ adalah jumlah perjalanan per hari, $p$ adalah tarif per perjalanan, $\varepsilon < 0$ adalah elastisitas harga permintaan, dan $A$ adalah konstanta skala. Elastisitas angkutan umum biasanya inelastis. Rule of thumb literatur jangka pendek adalah sekitar −0,3, dengan rentang −0,2 sampai −0,5[^6]. Saya tidak menemukan estimasi elastisitas KRL yang kredibel, jadi saya pakai rentang ini.

Asumsi-asumsinya:

- Tarif rata-rata $\bar{p}$ = Rp4.000 per perjalanan. Ini asumsi kasar: 25 km pertama Rp3.000 ditambah sedikit jarak tambahan.
- Pada tarif $\bar{p}$, permintaan $Q_0$ = 1 juta perjalanan per hari, dan 105 trainset adalah armada yang dibutuhkan untuk melayaninya dengan standar normal.
- Dengan 89 trainset, kapasitas layanan standar hanya $K = \frac{89}{105} Q_0 \approx 848$ ribu perjalanan per hari.

Pada tarif $\bar{p}$, orang mau naik $Q_0$, tapi kapasitas cuma $K$. Harga bayangan (_shadow price_) $p^{*}$ adalah tarif yang membuat permintaan pas sama dengan kapasitas:

$$
p^{*} = \bar{p}\left(\frac{K}{Q_0}\right)^{1/\varepsilon}
$$

Dengan $\varepsilon = -0{,}3$, kita dapat $p^{*} \approx$ Rp6.900. Artinya, di margin ada penumpang yang sebenarnya rela bayar hampir dua kali tarif resmi, tapi tetap tidak kebagian layanan yang layak.

**Batas bawah: _deadweight loss_.** Kalau yang kebagian kursi adalah orang-orang yang paling butuh (penjatahan efisien), kerugiannya cuma surplus dari perjalanan yang hilang:

$$
DWL = \int_{K}^{Q_0} \left[P(q) - \bar{p}\right] dq
$$

di mana $P(q) = \bar{p}\,(q/Q_0)^{1/\varepsilon}$ adalah kurva permintaan inversnya.

**Batas atas: rente yang terbuang.** Di dunia nyata, KRL tidak dijatah ke yang paling butuh. KRL dijatah lewat siapa yang kuat berdiri dan desak-desakan, siapa yang datang paling pagi, dan siapa yang rela nunggu kereta berikutnya. Barzel (1974)[^7] menunjukkan bahwa kalau penjatahan dilakukan lewat antre atau waktu, selisih $(p^{*} - \bar{p})$ untuk setiap perjalanan yang terlayani bisa habis "dibayar" dalam bentuk waktu dan kenyamanan yang hilang. Literatur juga menunjukkan penjatahan non-harga membuat barang jatuh ke orang yang salah (_misallocation_)[^8], dan kesesakan di kereta memang punya nilai rupiah yang nyata bagi penumpang[^9]. Jadi batas atasnya adalah:

$$
L^{atas} = DWL + (p^{*} - \bar{p})\,K
$$


```python
def biaya(eps, p=4000, Q0=1e6, x=89/105):
    K = x * Q0
    pstar = p * x ** (1 / eps)
    a = 1 + 1 / eps
    integral = p * Q0 * (1 - x ** a) / a      # ∫_K^Q0 P(q) dq
    dwl = integral - p * (Q0 - K)
    rente = (pstar - p) * K
    return pstar, dwl * 365 / 1e9, (dwl + rente) * 365 / 1e9

for e in (-0.2, -0.3, -0.5):
    ps, bawah, atas = biaya(e)
    print(f"eps={e}: p*=Rp{ps:,.0f}  bawah=Rp{bawah:,.0f} M/thn  atas=Rp{atas:,.0f} M/thn")
```

    eps=-0.2: p*=Rp9,142  bawah=Rp120 M/thn  atas=Rp1,711 M/thn
    eps=-0.3: p*=Rp6,941  bawah=Rp72 M/thn  atas=Rp982 M/thn
    eps=-0.5: p*=Rp5,567  bawah=Rp40 M/thn  atas=Rp525 M/thn
    

Jadi kekurangan 16 trainset ini kira-kira membebani penumpang **Rp40 miliar sampai Rp1,7 triliun per tahun**, dengan skenario tengah (ε = −0,3) di **Rp70 miliar sampai Rp1 triliun per tahun**. Rentangnya lebar, dan memang harus lebar karena asumsinya banyak. Saya lebih percaya angkanya lebih dekat ke batas atas, karena siapa pun yang pernah naik KRL jam 7 pagi dari Bogor tahu penjatahannya jelas bukan penjatahan efisien.

Berapa lama kekurangan ini berlangsung? Impor bekas ditolak awal 2023. KRL bekas bisa masuk dalam hitungan bulan, sedangkan pesanan INKA baru mulai berdatangan 2025–2026 dan masih ada yang terlambat. Ambil saja kira-kira 3 tahun. Totalnya berarti sekitar **Rp0,2 T sampai Rp3 T** untuk skenario tengah. Itu semua ditanggung anker, bukan APBN.

Bandingkan dengan selisih belanja KAI di atas, sekitar Rp265 miliar per tahun. **Ongkos di sisi penumpang bisa beberapa kali lipat lebih besar dari ongkos di sisi pembeli.** Inilah yang tidak tertangkap model TKDN saya yang lama. Di model itu kuantitas dianggap tetap dan ongkosnya cuma margin produsen. Di dunia nyata, TKDN yang mengikat dan pemasok yang lambat juga memangkas **kuantitas**.

## Jadi, worth it ga?

Beberapa poin penting:

1. **TKDN tidak gratis.** Ia tidak muncul sebagai pos subsidi di APBN, tapi ongkosnya pindah ke pembeli (KAI/KCI) dan akhirnya ke penumpang lewat layanan yang lebih buruk. Kalau PMN ke KCI ikut membesar untuk menutup harga INKA, sebagian ongkos itu sebenarnya subsidi APBN ke INKA yang tersamar. Ditambah suntikan Danantara di luar APBN, dukungan ke INKA jadi tersebar di banyak kantong dan sulit dihitung totalnya.
2. **Ongkosnya tidak dibagi rata.** Kalau INKA disubsidi lewat APBN, ongkos industrialisasinya ditanggung semua pembayar pajak. Lewat TKDN, ongkosnya dipusatkan ke sekitar sejuta penumpang KRL per hari, yang sebagian besar naik kereta untuk **berangkat kerja**. Waktu dan tenaga yang habis di peron dan gerbong sesak adalah produktivitas yang hilang di kantor, pabrik, dan toko di Jabodetabek. Jadi kita memajaki aktivitas ekonomi paling produktif di negeri ini demi satu pabrik di Madiun.
3. **Bisa worth it, dengan syarat.** Literatur _infant industry_ cukup jelas: proteksi hanya bisa dibenarkan kalau ada pembelajaran yang tidak bisa didapat pasar sendiri, kalau industrinya benar-benar jadi efisien, dan kalau proteksinya punya **batas waktu**[^10]. Literatur kebijakan industri yang lebih baru juga menekankan disiplin, ukuran keberhasilan yang jelas, dan kesiapan menghentikan program yang gagal[^11]. Jadi pertanyaannya: apakah "surplus" yang dipindahkan dari anker ke INKA benar-benar dipakai untuk membangun kapasitas produksi dan _know-how_? Kalau INKA masih memproduksi 3 trainset per tahun dari target 8, terlambat mengirim, dan utangnya Rp4,7 T, buktinya sejauh ini belum ada. Lalu sampai kapan? Selama itu, anker mungkin bisa lebih produktif di sektor lain, sektor yang kebetulan sedang terhambat oleh transportasi.

Hitungan di post ini kasar, dan saya sudah berusaha jujur soal asumsinya. Kodenya ada di atas, silakan ganti angkanya sendiri. Tapi **hitungan harus tetap dilakukan**. Setiap intervensi pemerintah pasti ada ongkosnya. Yang berbeda cuma siapa yang bayar dan bagaimana caranya. Pembuat kebijakan yang mengabaikan ini dan merasa TKDN itu gratis sedang mempertontonkan buta huruf ekonomi.

Mention saya di [twitter](https://www.twitter.com/imedkrisna) jika ada komen, kritik, atau saran. Thanks.

[^1]: CNN Indonesia (2023). Alasan Kemenperin Tolak Beri Rekomendasi Izin Impor KRL Bekas Jepang. https://www.cnnindonesia.com/ekonomi/20230302082911-92-919704/alasan-kemenperin-tolak-beri-rekomendasi-izin-impor-krl-bekas-jepang
[^2]: Wikipedia bahasa Indonesia. Polemik impor KRL bekas tahun 2023. https://id.wikipedia.org/wiki/Polemik_impor_KRL_bekas_tahun_2023 ; lihat juga Liputan6 (2023). Tok! Impor KRL Bekas Jepang Resmi Ditolak. https://www.liputan6.com/bisnis/read/5253748/tok-impor-krl-bekas-jepang-resmi-ditolak
[^3]: Tempo (2024). KAI Klaim 92 Persen Pengadaan KRL Bekerja Sama dengan INKA, Total Investasi Rp6,06 Triliun. https://www.tempo.co/ekonomi/kai-klaim-92-persen-pengadaan-krl-bekerja-sama-dengan-inka-total-investasi-rp6-06-triliun-89355
[^4]: Investortrust (2026). KAI Commuter Pastikan 12 Trainset Inka Tiba Juni 2026, Operasi Mulai Juli. https://investortrust.id/business/92535/kai-commuter-pastikan-12-trainset-inka-tiba-juni-2026-operasi-mulai-juli
[^5]: Kontan (2026). Merger KAI–INKA Makin Dekat, Akuisisi Ditargetkan Tuntas November 2026. https://industri.kontan.co.id/news/merger-kai-inka-makin-dekat-akuisisi-ditargetkan-tuntas-november-2026 ; KabarBursa. INKA terbelit utang Rp4,7 triliun. https://www.kabarbursa.com/makro/besok-danantara-mulai-lagi-lrt-city-inka-terbelit-utang-rp47-triliun
[^6]: Litman, T. (2004). Transit Price Elasticities and Cross-Elasticities. *Journal of Public Transportation*, 7(2), 37–58. https://doi.org/10.5038/2375-0901.7.2.3
[^7]: Barzel, Y. (1974). A Theory of Rationing by Waiting. *The Journal of Law and Economics*, 17(1), 73–95. https://doi.org/10.1086/466785
[^8]: Glaeser, E. L., & Luttmer, E. F. P. (2003). The Misallocation of Housing Under Rent Control. *American Economic Review*, 93(4), 1027–1046. https://doi.org/10.1257/000282803769206197
[^9]: Wardman, M., & Whelan, G. (2011). Twenty Years of Rail Crowding Valuation: Methods, Evidence and Lessons from British Experience. *Transport Reviews*, 31(3), 379–398. https://doi.org/10.1080/01441647.2010.519127
[^10]: Melitz, M. J. (2005). When and How Should Infant Industries Be Protected? *Journal of International Economics*, 66(1), 177–196. https://doi.org/10.1016/j.jinteco.2004.07.001
[^11]: Juhász, R., Lane, N., & Rodrik, D. (2024). The New Economics of Industrial Policy. *Annual Review of Economics*, 16, 213–242. https://doi.org/10.1146/annurev-economics-081023-024638
