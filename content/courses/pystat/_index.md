---
date: "2020-08-20T00:00:00Z"
draft: false
lastmod: "2020-08-20T00:00:00Z"
linktitle: Statistika dengan Python
menu:
  example:
    name: Pembukaan
    weight: 1
summary: Melakukan analisis statistika sederhana dengan menggunakan Python
title: Overview
toc: true
type: docs
weight: 1
editable: false
commentable: false
---

## Tentang buku ini
Di masa di mana sebagian besar institusi penting dan berpengaruh menggunakan data sebagai analisis (dan bukan perasaan belaka), skill menggunakan *software* untuk analisis data semakin tinggi peminatnya. Indonesia termasuk negara yang tidak banyak punya *programmer*, padahal belajar *programming* bukan sesuatu yang maha sulit dan dapat dipelajari semenjak dini.

Untuk itu buku ini dibuat. Sebagai seorang yang mendapatkan manfaat dari mempelajari bahasa pemrograman, saya ingin mencoba mempermudah akses belajar bahasa pemrograman bagi teman-teman di Indonesia.

Buku ini sekaligus menjadi dokumentasi saya pribadi dalam belajar menggunakan bahasa pemrograman Python. Saya akan terus meng-update buku ini sesuai input-input yang didapat. Dengan dibuatnya buku ini, saya tinggal buka buku ini aja kalau ada beberapa *command* yang lupa.

Mohon maaf apabila ada beberapa istilah yang keliru atau kesalahan lainnya secara umum. Saya sendiri bukan programmer dan tidak terlalu mengerti tentang istilah-istilah programmer. Saran dan kritik akan ditampung dan kesalahan di buku ini akan langsung di-update jika memang ada laporan.

Buku ini gratis dan dapat disebar-luaskan ke siapapun. Namun tolong jangan mengambil konten di buku ini sembarangan apalagi mencetaknya untuk tujuan komersil tanpa persetujuan dari penulis.

Semoga buku ini berguna untuk anda.

## Asumsi
- Anda punya laptop/komputer yang memperbolehkan akses admin. Jika laptop/komputer punya anda sendiri, harusnya sih aman. Kalau punya kantor, harus minta tukang IT-nya menginstallkan.

- Anda menggunakan windows. buku ini dapat dijalankan di MacOS maupun Linux, namun berhubung saya menjalankannya dengan windows, maka ada beberapa langkah di buku ini akan dijelaskan dengan logika windows.

- Anda telah memahami teori statistika. Di buku ini tidak dijelaskan panjang lebar mengenai teori statistika seperti probabilitas, sampel, kurtosis dan lain-lain. buku ini akan mengutamakan praktik dengan menggunakan python.

- Anda tidak punya pengalaman apapun tentang *coding*, tapi pernah menggunakan *spreadsheet* seperti Microsoft Excel atau Google Sheet.

- Anda punya kuota internet.

## Capaian pembelajaran
- Dapat menggunakan python untuk hal-hal sederhana seperti mengimpor data, manipulasi tabel, visualisasi grafik, dan analisis statistika seperti regresi linear sederhana

## Tentang Python
Python adalah *open source software* yang didevelop ramai-ramai. Untuk menjalankan fungsional Python secara utuh, anda perlu memanggil beberapa paket-paket yang dikembangkan oleh banyak pihak. Dan karena *open source*, software-nya dapat diunduh secara gratis. Karena gratis itu juga jadinya banyak yang pakai.

Python adalah *software* serba bisa. Tidak secara spesial didesain untuk analisis statistik. Karena itu bahasa python agak kurang intuitif untuk statistisi. Namun demikian, skill python justru banyak yang cari karena pengguna python bisa menggunakan skill-nya tidak hanya untuk statistik.

Di buku ini, anda hanya akan mempelajari python yang esensial untuk menjalankan analisis statistik sederhana. Tapi anda akan punya modal untuk belajar menggunakan python lebih jauh lagi untuk perkembangan karir anda.

Python sendiri adalah bahasa yang sangat general dan *user interface*-nya sama sekali tidak friendly. Untungnya ada yang disebut Jupyter Notebook, sebuah *software* yang bikin ngetik kode Python lebih intuitif dan sangat mudah mendokumentasikan kode Python yang anda miliki. Python dan Jupyter Notebook tidak perlu diinstall secara terpisah, tapi diinstall sekaligus dalam *environment control* bernama Anaconda.

## Menginstall Anaconda
Anaconda dapat di-unduh di [anaconda.com/products/individual](https://www.anaconda.com/products/individual). Klik sesuai OS yang anda miliki. Jika anda di windows dan tidak tau apakah windows anda 32-bit atau 64-bit, klik kanan di @icon-windows start, lalu klik "system". lihat di system type, akan keliatan 32-bit atau 64-bit.

Setelah selesai diunduh, install dengan menggunakan *recommended settings*. Jika anda menginstall dengan menggunakan *recommended settings* (alias pencet next-next terus sampai capek), maka anda Anaconda anda akan terinstall di C:\Users\<nama-user>\Anaconda3.

Anda juga perlu rajin-rajin mengupdate anaconda