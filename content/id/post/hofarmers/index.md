--
# Documentation: https://wowchemy.com/docs/managing-content/

title: ' Is farming Labor or capital intensive?'
subtitle: "sebuah contoh substitusi di model Hecksher-Ohlinn"
summary: ""
authors: [admin]
tags: [macem-macem]
categories: [macem-macem]
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

<iframe src="https://data.worldbank.org/share/widget?indicators=SL.AGR.EMPL.ZS&locations=ID-US" width='900' height='600' frameBorder='0' scrolling="no" ></iframe>

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

Penyusutan juga cukup kontras. Penyusutan modal di AS dihitung setara dengan 14.5% total produksi, sementara di Indoonesia cuma 2%. Berarti petani Indonesia menggunakan lebih sedikit permesinan ketimbang di AS.

Artinya, untuk menanam kedelai, anda bisa saja menggunakan banyak petani dengan permesinan yang sedikit (manual), atau sedikit petani tapi dengan mesin yang mahal (semi-otomatisasi). Strategi yang mana yang dilakukan? Hal inin tentu tergantung dari _relative abundance of factor_. Alias, di Indonesia, pegawai yang profilnya cocok jadi petani ada banyak, sementara modal buat beli mesin relatif sedikit (suku bunga produksi di Indonesia mahal banget). Di AS sebaliknya, pegawai yang cocok jadi petani lebih sedikit (makanya gajinya mahal), tapi modal ada banyak (suku bunga di AS pre-COVID itu murah banget). Inilah efek substitusi yang ada di model HO.

Disclaimer lagi deh: permasalahan di pertanian Indonesia itu rumit. Ga sesederhana cuma mekanisasi aja. Bisa diliat juga di tabel di atas bahwa lahan termasuk bagian yang gede di production cost. Artinya, tanah memang gak ada substitusinya baik di AS maupun Indonesia. Problemnya opkors di AS tanahnya luas. Ada juga prooblem pengairan di mana negara-negara sungai mekong (Vietnam, Thailand) punya advantage dibanding Indonesia, meskipun struktur tenaga kerjanya mirip dengan Indonesia. Dan lain-lain.

Demikian sedikit contoh kasus di HO semoga bermanfaat bagi yang lagi belajar ekonomi internasional.