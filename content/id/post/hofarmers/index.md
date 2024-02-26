---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Substitusi buruh dan mesin di industri pertanian'
subtitle: "melihat bedanya petani AS dan Indonesia"
summary: ""
authors: [admin]
tags: [ekonomi, perdagangan, model, HecksherOhlin]
categories: [ekonomi, perdagangan, model, HecksherOhlin]
date: 2024-02-25T15:10:34+07:00
lastmod: 2024-02-25T15:10:34+07:00
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

Hari ini tanggal 25 Februari 2024 sedang ramai di jagat maya tentang harga pangan Indonesia yang semakin tinggi. Beberapa orang membandingkan harga beras di luar negeri vs di Indonesia, kenapa di negara lain bisa murah. Tentu saja jawabannya karena di luar negeri (at least di negara barat) bisa impor dengan bebas tanpa intervensi pemerintah. Pertanyaan berikutnya, jika kita negara agraris, kok bisa tanem sendiri lebih mahal daripada impor? Sebenernya jawabannya banyak dan udah dijawab juga, misalnya di [sini](https://www.cips-indonesia.org/post/intensifikasi-pertanian-kebijakan-prioritas-untuk-penyediaan-pangan-nasional?lang=id).

Postingan kali ini ada hubungannya dengan itu, tapi saya mau fokus ke pembahasan soal jumlah dan produktivitas petani. Kenapa? Karena saya lagi ngajar ekonomi internasional dan ini postingan kali ini sangat pas buat menjelaskan substitusi faktor produksi yang dicontohkan di model bernama Hecksher-Ohlin (HO) wwkkwk. Anyway,Di Indonesia, jumlah petaninya banyak tapi lahannya sedikit. Indonesia adalah importir kedelai dari AS, padahal petani di AS lebih dikit lagi daripada di Indonesia.

<iframe src="https://data.worldbank.org/share/widget?indicators=SL.AGR.EMPL.ZS&locations=ID-US" width='900' height='600' frameBorder='1' scrolling="yes" ></iframe>

TLDR: ujung2nya ini adalah diskusi tentang intensif buruh vs intensif kapital di industri pertanian, di mana di USA, permesinan berperan jauh lebih besar daripada buruh, sementara Indonesia sebaliknya. Buat anda yang pingin tau gimana ekonom melihat intensitas faktor produksi, lihat appendix di paling bawah.

Oke lanjut ke diskusi factor intensity.

## Hecksher-Ohlin dan factor intensity

Dalam teori perdagangan Hecksher-Ohlin (HO) dianalisis akan adanya substitusi antara tenaga kerja dan modal (mesin). Jumlah petani boleh sedikit asalkan diganti dengan jumlah permesinan yang sesuai.

Andaikan ada 2 pilihan produksi yang outputnya sama:

1. 10 petani dengan 10 cangkul
2. 1 petani dengan 1 traktor

Jika kita lihat struktur biaya di kasus 1, sudah pasti mayoritas belanja akan ada di gaji karena harus menggaji 10 orang. Untuk kasus ke-2, gaji akan menjadi bagian kecil dari total biaya karena cuma membiayai gaji 1 orang petani. Akan tetapi, belanja modal untuk kasus 1 akan jauh lebih sedikit, apalagi cangkul harganya murah (meski kata Pak Jokowi ["stop importing hoes"](https://jakartaglobe.id/business/stop-importing-hoes-jokowi)).

Dan inilah perbedaan utama antara struktur biaya petani Indonesia dengan negara maju. Bisa dilihat jika kasus 2 petani minta naik gaji, maka kenaikan itu tidak akan meningkatkan total biaya produksi secara signifikan. Sementara itu untuk kasus 1, kenaikan gaji akan membebani ongkos produksi karena ada 10 orang yang gajinya harus naik.

Saya coba membandingkan antara _share_ biaya produksi Indonesia vs Amerika Serikat. Saya mengambil data ongkos produksi Kedelai (karena ditanam di kedua negara) di 2017 (karena di BPS, Indonesia cuma ada data sampai 2017). Data [AS dari USDA](https://www.ers.usda.gov/data-products/commodity-costs-and-returns.aspx) sementara data [Indonesia dari BPS](https://www.bps.go.id/id/statistics-table/1/MjA1NSMx/nilai-produksi-dan-biaya-produksi-per-musim-tanam-per-hektar-budidaya-tanaman-padi-sawah--padi-ladang--jagung--dan-kedelai--2017.html). Tidak semua item biaya saya tampilkan. Cuma yang ada di 2 2 nya aja.

| Item | USA  (%) | IDN (%) |
| ------- | ---- | ---- | 
| Seed	| 9.25 |	6.53 |
| Fertilizer |	3.99 |	4.97 |
| Chemicals |	4.28 |	4.02 |
| Labor |	3.61 |	47.23 |
| sewa/bunga |	0.13 |	0.12 |
| lahan |	22.77 |	28.89 |
| pajak & asuransi |	1.70 |	0.86 |
| penyusutan |	14.50 |	1.98 |
| Energi dll |	2.16 |	1.26 |

Bisa kita lihat perbedaan yang sangat kontras di labor (belanja pegawai) dan di penyusutan. Untuk petani kedelai Indonesia di 2017, 47% biaya produksi adalah di belanja pegawai. Bagi petani AS, belanja pegawai cuma 3.61% dari total ongkos produksi. Padahal kita tau bahwa level gaji di AS lebih mahal ketimbang di Indonesia. Hal ini berarti di AS, meski gaji pegawai nya mahal, hal ini relatif kecil karena mereka menggunakan sedikit petani ketimbang di Indonesia.

Penyusutan juga cukup kontras. Penyusutan modal di AS dihitung setara dengan 14.5% total produksi, sementara di Indoonesia cuma 2%. Berarti petani Indonesia menggunakan lebih sedikit permesinan ketimbang di AS. Apalagi ketika kita lihat bahwa biaya untuk sewa/bunga di kedua struktur biaya itu sama, padahal kita tau dari penyusutan bahwa di AS, mesinnya lebih banyak dari di Indonesia. Artinya, bunga di AS tuh murah.

Artinya, untuk menanam kedelai, anda bisa saja menggunakan banyak petani dengan permesinan yang sedikit (manual), atau sedikit petani tapi dengan mesin yang mahal (semi-otomatisasi). Strategi yang mana yang dilakukan? Hal inin tentu tergantung dari _relative abundance of factor_. Alias, di Indonesia, pegawai yang profilnya cocok jadi petani ada banyak, sementara modal buat beli mesin relatif sedikit (suku bunga produksi di Indonesia mahal banget). Di AS sebaliknya, pegawai yang cocok jadi petani lebih sedikit (makanya gajinya mahal), tapi modal ada banyak (suku bunga di AS pre-COVID itu murah banget). Inilah efek substitusi yang ada di model HO.

## Intinya & disclaimer

Oke jadi intinya kesimpulan postingan ini adalah:

1. Untuk menjalankan pertanian yang efisien, penggunaan faktor produksi harus sesuai dengan intensitas faktor produksinya. Bisa jadi ada tanaman yang perlu banyak mesin dan sedikit buruh. Negara yang tetap memakai banyak buruh di industri yang aslinya lebih efisien dengan banyak mesin akan lebih tidak efisien dibandingkan yang pakai banyak mesin.

2. Negara yang buruhnya murah dibandingkan mesin akan kesulitan bersaing harga dengan negara yang mesinnya relatif lebih murah, di industri yang lebih _capital intensive_. Kenapa? Karena negara yang buruhnya murah cenderung akan pakai lebih banyak buruh, bahkan di industri yang sejatinya _capital intensive_. Jadinya gak efisien.

3. Lebih efisien sebenernya adalah ekspor produk-produk yang intensif buruh, lalu duitnya dipake buat impor produk-produk yang intensif kapital.

Disclaimer: permasalahan di pertanian Indonesia itu rumit. Ga sesederhana cuma gara-gara mekanisasi aja. Bisa diliat juga di tabel di atas bahwa lahan termasuk bagian yang gede di production cost untuk kedua negara. Artinya, tanah memang gak ada substitusinya baik di AS maupun Indonesia. Bedanyanya opkors di AS tanahnya luas dibandingkan di Indonesia. Ada juga prooblem pengairan di mana negara-negara sungai mekong (Vietnam, Thailand) punya advantage dibanding Indonesia, meskipun struktur tenaga kerjanya mirip dengan Indonesia. Dan lain-lain.

Ketika kami ekonom menganalisis dunia nyata, tentu saja pertimbangannya banyak, gak cuma ini doang. Misalnya bahwa faktor produksi itu gak cuma buruh dan kapital. Bahkan, Indonesia sebenernya ngekspor barang-barang yang intensif lahan seperti tambang dan perkebunan. Buruh pun bisa dibagi jadi low skill high skill. Cuma kalo diketik diblog ntar ga habis2 wkwkwkwk.

Demikian sedikit contoh kasus di HO semoga bermanfaat terutama bagi yang lagi belajar ekonomi internasional.

## Appendix: Kursus singkat tentang intensitas faktor produksi

Dalam teori produksi standar di pelajaran mikro dan makroekonomi dasar, kita biasanya memulai mempelajari produksi sebuah negara / perusahaan dengan fungsi umum

$$Q=f(K,L)$$

di mana $K$ adalah jumlah kapital yang digunakan dan $L$ adalah jumlah pegawai yang digunakan untuk produksi barang dan jasa sebanyak $Q$. Alias, di mikro/makro dasar tuh faktor produksi digambarkan ada dua: kapital dan tenaga kerja[^1].

Ekonomi yang kompetitif akan memberikan imbalan yang setara dengan produktivitasnya[^2], atau:

$$\frac{df(K,L)}{dL}=w$$

$$\frac{df(K,L)}{dK}=r$$

di mana $w$ adalah upah/gaji dan $r$ adalah sewa/nilai penyusutan.

Jika sebuah aktivitas produksi punya struktur biaya seperti ini:

$$TC=w \times L+r \times K$$

di mana total cost (TC) adalah upah dikali jumlah buruh tambah sewa dikali jumlah kapital, maka sebuah ekonomi dikatakan intensif buruh jika sumbangsih buruh dalam total cost mendominasi sumbangsih kapital. Alias, sebuah ekonomi dikatakan intensif buruh jika:

$$
\frac{w \times L}{TC} > \frac{r \times K}{TC}
$$

Mengobservasi produksi marjinal tuh gak praktis, sementara cost masih bisa dihitung. Dengan mengandalkan pegawngan bahwa _cost share_ gak jauh beda dari _productivity share_, maka kita lihat intensitas faktor produksi dari _cost share_-nya.

[^1]: Kepemilikan faktor produksi inilah yang dulu sering diperdebatkan, yaitu antara kapitalis (pemilik K) dan buruh (pemilik L). Strugglenya adalah siapa yang lebih banyak dapat bagian dari Q.

[^2]: Secara teoretis, produktivitas dihitung dengan menggunakan produksi marjinal atau turunan pertama dari Q terhadap faktor. Secara praktik, hal ini sulit banget untuk dilakukan. Perlu kondisi yg sangat ketat.