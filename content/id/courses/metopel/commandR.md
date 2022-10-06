---
date: "2022-10-04T00:00:00Z"
draft: false
lastmod: "2022-10-04T00:00:00Z"
linktitle: install
menu:
  example:
    name: install
    weight: 20
summary: cara menginstall R
title: install R
toc: true
type: book
weight: 20
editable: false
commentable: false
---

Di laman ini, anda akan diantarkan ke step-by-step menginstall r di komputer anda. Prosesnya mudah kok, apalagi kalau anda sudah pernah install aplikasi di komputer sebelumnya. Hal-hal yang perlu anda install antara lain adalah R, RStudio dan package-package yang diperlukan. Jika anda mengalami masalah dalam melakukan instalasi, silakan datang ke ruangan Pak Imed atau Bu Tere.

Minimal saya harap anda paham bagaimana cara berselancar di internet. Kami harapkan anda juga memahami struktur folder di komputer anda. Anda tau di mana lokasi file yang anda download, gimana cara bikin new folder, dan bagaimana cara navigasi my computer di Operating System masing-masing.

Jangan lupa restart komputer setelah install dan jangan lupa download [data-data latihannya](https://drive.google.com/drive/u/1/folders/1exmFFbe7Ons-0nQ_arqtp0N9ZzG1Cozk) sebelum masuk kelas. Charge laptop anda sampai 100% karena ga ada colokan di kelas.

## Install R

R adalah program yang digunakan untuk menghitung. Dia sendiri bentuknya agak gak jelas. Jika anda cuma punya R, anda harus ngerun R pake console gitu. Sangat tidak intuitif. Nulis scriptnya juga bisa, tapi pake text editor yang juga kurang intuitif. Tapi bagaimanapun juga, programnya harus ada di komputer anda.

### Cari installernya pakai google

Cara paling gampang install r adalah dengan menggunakan google search, lalu ketik `install r for windows` jika laptop anda windows. Anda akan diantarkan ke installer r untuk versi windows 64 bit. Komputer jaman sekarang rata-rata 64 bit. Jika komputer anda adalah 32-bit, maka harus install versi r yang jadul. Google aja `install r for windows 32-bit`.

Sebagian besar komputer jaman sekarang pasti pake 64-bit. Tapi jika anda gak yakin, cara ngecek bit anda bisa dilihat di [sini](https://support.microsoft.com/en-us/windows/32-bit-and-64-bit-windows-frequently-asked-questions-c6ca9541-8dce-4d48-0415-94a3faa2e13d).

### Datang langsung ke website r-nya

Tanpa google juga bisa kok. langsung aja datang ke websitenya. Ada beberapa mirror download yang bisa dipilih, tapi untuk Indonesia, lebih baik pakai servernya Universitas Syiah Kuala yang bisa diakses di [sini](https://cran.usk.ac.id/). Anda cukup download `base`. Saat tulisan ini dibuat, versi R yang terbaru adalah R-4.2.1 for windows. Ini adalah versi r untuk windows 64-bit.

Cara manapun yang anda pilih, anda akan diantarkan ke lokasi yang kurang lebih sama. Anda akan download installernya yang besarnya sekitar 78 Megabyte. Tunggu aja sampai selesai. Nanti nama file-nya `R-4.2.1-win.exe`. Pastikan anda familiar dengan lokasi file yang anda download ini di folder anda.

Kalau sudah ada installernya, anda tinggal dobel klik file-nya lalu next-next sampe selesai. Selamat, anda sudah berhasil menginstall r

## Install RStudio

RStudio ini bukan program yang anda pakai untuk hitung. RStudio disebut juga dengan IDE (Integrated Development Environment). Dia ini lebih ke software yang anda gunakan untuk mengakses R dengan lebih intuitif. Di RStudio anda akan bisa memanage package lebih mudah dan menulis script r dengan lebih intuitif. Intinya, RStudio adalah software yang anda pakai untuk berinteraksi dengan R. Ketika anda regres, anda menulis kodenya di RStudio, akan tetapi yang nge-run regresi anda adalah R.

### Cari Installernya pakai google

Yup, anda juga bisa download installernya lewat google dulu. langusng aja google `download RStudio`, maka pilihan pertamanya adalah si RStudio ini. Pilih pilihan yang tulisannya "Download RStudio IDE" (pilihan paling atas) untuk ke laman RStudio, lalu pilih RStudio desktop yang free. RStudio akan memilihkan installer yang pas untuk anda. Langsung aja tekan tombol biru besar yang tulisannya "Download RStudio for Windows".

![](RStudio.png "Pencet yg biru itu")

RStudio filenya lebih gede dari R, sekitar 182 MB. Installernya namanya `RStudio-2022.07.2-576.exe`. angka-angka itu nama versinya. Jika anda download lagi di masa depan, mungkin nama versinya berubah karena ada update.

Setelah anda sudah selesai download, double klik installernya lalu next-next aja sampe beres. Jangan lupa create shortcut jika anda lebih suka pakai shortcut di desktop untuk mengakses program anda.

![](start.png "shortcutnya yang dilingkarin merah itu")

## Interaksi dengan RStudio

RStudio punya tampilan seperti di bawah ini:

![](tampilan.png "4 kuadran RStudio")

Jangan kaget jika tampilan RStudio anda tidak persis seperti ini. Tampilan saya keliatan seperti ini karena saya sedang mengerjakan sesuatu di RStudio saya. Jika anda baru buka pertama kali, pasti masih kosong. Yang penting adalah anda bisa lihat ada 4 kuadran di RStudio.

1. Kuadran 1 (kiri atas) akan saya sebut script. Ini adalah tempat anda menulis script untuk kode anda. Coba arahkan mouse anda ke kiri atas, ada tulisan `file`, lalu pilih `new file` lalu pilih `R Script`. Anda juga bisa pakai shortcut `ctrl+shift+n`. Hal ini akan memunculkan file namannya `Untitled1` yang mana adalah R Script anda. Nanti kita bahas di kelas bagaimana mengisi R Script anda. Gampang kok. Tinggal kopas aja. 

1. Kuadran 2 (kanan atas) adalah environment window. Di kuadran ini anda bisa lihat file-file yang sudah anda buat dengan R, seperti data dan grafik. Nanti kuadran 2 ini akan penuh sendiri seiring anda berinteraksi dengan RStudio.

1. Kuadran 3 (Kanan bawah) adalah File window. Di sini anda bisa lihat struktur folder anda maupun membuka file-file gambar. Nanti kita akan bahas di kelas.

1. Kuadran 4 (kiri bawah) disebut juga dengan console. Di sinilah command-command R anda akan diketik. Ada beberapa hal yang anda bisa coba. 
  - coba anda ketik `version` lalu enter. Apa yang anda lihat?
  - Kemudian, ketik `getwd()` lalu enter. Apakah anda mengerti apa yang dihasilkan oleh command ini? Apakah anda tau lokasi yang dimaksud?
  - Anda juga bisa jadikan console seperti kalkulator. coba ketik `1+1` lalu enter.
  - R juga bisa store values. misalnya anda coba ketik `a<-1+1` lalu enter. kemudian ketik `a` lalu enter.
  - Ketik `b<-3*3` lalu enter. lalu ketik `a+b`, enter.

Ada banyak yang bisa anda coba, ada banyak sekali command yang anda bisa masukan di console. Namun seperti anda lihat, console lebih digunakan jika anda perlu memasukkan kode yang pendek-pendek. Untuk kode yang panjang, kita akan lebih sering menggunakan R Script. 

Nah, contoh kode yang ada di kelas itu semua dapat di-run di RScript ini. kopas aja kode yang ada di kelas ke R Script anda, lalu tekan ctrl+a untuk ngeblok seisi r script lalu tekan `run` (ada di kanan atas dari area r script). Atau pake `ctrl+enter` untuk shortcutnya.

Nanti kita bahas di kelas bagaimana menulis kode di R Script. Namun untuk sekarang, mari kita persiapkan komputer anda untuk penggunaan di kelas. Anda memerlukan beberapa package yang harus diinstall.

## Install package

R sendiri adalah sebuah software komputasi yang elegan namun fungsinya cukup terbatas. Untuk menggunakan R dengan lebih mudah, banyak peneliti membuat packages atau tambahan software agar R bisa digunakan dengan lebih intuitif. Beberapa packages ini perlu diinstall 1x saja, tapi untuk setiap penggunaannya perlu dipanggil dengan command `library`.

Sebelum kita mulai di kelas, ada beberapa packages yang perlu anda install. Cukup kopas kode berikut ini ke console anda:

```r
install.packages(c("tidyverse","WDI","readxl","kableExtra"))
```
Jangan lupa tekan enter dan pastikan ada sambungan internet.

Ada 4 packages yang diinstall di atas: `tidyverse` adalah package yang digunakan untuk data cleaning. `WDI` adalah package yang digunakan untuk menarik database-nya World Bank yang namanya World Development Indicators. `readxl` adalah package yang kita perlukan untuk membaca data excel ke r. `kableExtra` adalah package untuk membuat tabel.

Untuk sekarang, cukup kita install dulu. Nanti pakainya pas di kelas.

## Download data latihan

Jangan lupa untuk download file-file excel yang akan kita pakai untuk latihan. File-file tersebut dapat diakses di [sini](https://drive.google.com/drive/u/1/folders/1exmFFbe7Ons-0nQ_arqtp0N9ZzG1Cozk).

