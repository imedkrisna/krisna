---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Perspektif tes hipotesis dari diskursus sertifikasi halal vs sertifikasi haram"
subtitle: ""
summary: ""
authors: [admin]
tags: [CGE, ekonomi,MBG]
categories: [CGE, ekonomi,MBG]
date: 2025-05-25T12:06:59+07:00
lastmod: 2025-05-25T12:06:59+07:00
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

Di suatu pagi, saya melihat sebuah cuitan di twitter tentang produk makanan yang ternyata tidak halal:

<blockquote class=e"twitter-tweet"><p lang="in" dir="ltr">Ayam Widuran Solo, fix Haram <a href="https://t.co/7AyIhEaOMQ">pic.twitter.com/7AyIhEaOMQ</a></p>&mdash; Halal Corner Indonesia Foundation (@halalcorner) <a href="https://twitter.com/halalcorner/status/1926185599779668374?ref_src=twsrc%5Etfw">May 24, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Jadi ceritanya uth si tempat makan ini naruh tulisan "halal" (bukan logo MUI) dan ternyata ada kandungan babi-nya di makanan yang mereka jual. Saya juga gak tau sih awalnya kenapa bisa ketahuan, tapi bagaimanapun juga, si tempat makan mengakui bahwa emang makanan mereka ngga halal. Makanya di foto yang ada di cuitan itu, si resto bilang mereka akan nulis "non-halal". Ini kan berarti emang bener makanannya nggak halal.

Nah menariknya, inisiatif pencantuman "non-halal" tersebut membuat diskusi di cuitan itu berkembang menjadi "harusnya Indonesia bikin sertifikasi haram aja, bukan sertifikasi halal" mengingat di Indonesia, kemungkinan besar memang produk yang dijual itu halal, mengingat mayoritas penduduknya adalah muslim.

Diskusi ini menarik. Tes haram kemungkinan besar lebih praktikal karena ya itu tadi, mayoritas market produk pangan adalah muslim. Sebuah produsen produk makanan lebih punya insentif bikin produk halal anyway, sehingga jumlah produsen produk halal akan jauh lebih banyak dibandingkan produsen produk haram.

## Uji hipotesis

Uji hipotesis adalah metode statistik yang digunakan untuk menguji klaim atau hipotesis tentang suatu populasi berdasarkan sampel data. Dalam konteks sertifikasi halal dan haram, kita dapat menggunakan tes hipotesis untuk menentukan apakah suatu produk dapat dikategorikan sebagai halal atau haram berdasarkan data yang tersedia.

Type-I dan type-II error adalah konsep penting dalam teori peluang. Type-I error adalah kesalahan yang terjadi ketika kita menolak/reject H0 yang sebenarnya benar. Type-II error adalah sebaliknya, yaitu kesalahan ketika kita tidak menolak/reject H0 yang sebenarnya salah. 

Dalam diskursus sertifikasi halal, sebenarnya sertifikasi halal dapat kita anggap sebagai sebuah tes untuk memastikan kehalalan suatu produk. Dengan kata lain, suatu produk dites dengan asumsi:

> H0: Produk tersebut tidak halal
> H1: Produk tersebut halal

sertifikasi halal dilakukan dengan tujuan menolak H0. Jika setelah tes ditemukan bahwa suatu produk tidak ada unsur non-halal, maka surveyor memutuskan bahwa H0 ditolak dan memberikan sertifikasi halal untuk produk yang sedang dites.

Situasi sertifikasi halal di atas dapat kita representasikan dalam tabel berikut:

| kenyataaan $\backslash$ hasil tes | reject | fail to reject |
|----------------------------------|-------|-------|
| halal                            | benar | Type-II error |
| haram                            | Type-I error | benar |

Ingat, kita mendesain tes di atas untuk memberikan sertifikat pada barang yang halal. Untuk itu, H0-nya adalah sebaliknya, "produk tersebut tidak halal", lalu dites, lalu kita tolak jika produknya ternyata halal.

Nah, type-I error berarti adalah ketika barangnya aslinya haram, tapi ternyata H0-nya ditolak. Artinya, kita memberikan sertifikat halal pada barang yang aslinya haram. Type-I error sering kali disebut _false positive_ (dapet sertifikat padahal aslinya haram). Sedangkan type-II error adalah ketika barangnya aslinya halal, tapi kita tidak menolak H0, yang berarti kita menyimpulkan barangnya tidak bisa mendapat sertifikat halal. Nah, type-II error sering kali disebut _false negative_ (tidak dapet sertifikat padahal aslinya halal).

Jika kita tidak tau aslinya barang tersebut halal atau haram, maka kita dapat meletakkan probabilitas/peluang di dalam masing-masing kesimpulan. peluang terjadinya Type-I error biasanya diekspresikan dengan $\alpha$, sedangkan peluang terjadinya Type-II error diekspresikan dengan $\beta$. Biasanya, tes hipotesis yang diajarkan di kelas-kelas statistika pengantar adalah t-tes, yang didesain dengan asumsi meminimalkan Type-I error. Karena itu, kita seringkali melakukan tes hipotesis dengan $\alpha$ yang kecil, biasanya $\alpha = 0.05$. Sering denger ungkapan "signifikan pada level 5 persen", kan?

$$
P(halal|ada)=\frac{P(halal)P(ada|halal)}{P(ada)}
$$

$$
P(haram|ada)=\frac{P(haram)P(ada|haram)}{P(ada)}
$$