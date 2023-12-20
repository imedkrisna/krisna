---
date: "2022-10-04T00:00:00Z"
draft: false
lastmod: "2022-10-04T00:00:00Z"
linktitle: Tugas
menu:
  example:
    name: Tugas
    weight: 30
summary: Tugas
title: Tugas
toc: true
type: book
weight: 30
editable: false
commentable: false
---

## Tugas Metodologi Penelitian

Tugas metodologi penelitian kali ini adalah membuat sebuah _policy brief_ singkat (sekitar 1500 kata / 3 halaman A4). Tugas ini dikerjakan berkelompok. _Policy brief_ yang ditulis adalah tentang pertumbuhan PDB, inflasi, dan tingkat pengangguran.

Pada mata kuliah ilmu ekonomi, anda belajar hubungan antara pertumbuhan PDB, inflasi dan tingkat pengangguran. Bagaimana perubahan di salah satu indikator akan mengubah indikator yang lain. Tugas anda adalah membahas perubahan-perubahan ini berdasarkan data tahunan yang tersedia, dan menuliskannya dalam sebuah risalah singkat. Risalah singkat ini diperkirakan akan terdiri dari sekitar 1500-2000 kata (atau sekitar 3 halaman A4 tanpa tabel dan gambar). Format penulisan dapat dibagi ke dalam 4 bagian:

1. Pendahuluan (simple context aja ga usa panjang-panjang)
2. Data (gunakan grafik untuk melakukan visualisasi 3 indikator makro yang ditugaskan, lalu bahas sedikit masing-masing indikator tersebut)
3. Pembahasan (gunakan _framework_ ilmu ekonomi dalam membahas data yang ada)
4. Kesimpulan (no new info. Inget kerangka penelitian di meeting 12)

## Data yang digunakan

Anda dapat menggunakan [World Development Indicators](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG) untuk mendapatkan data yang diperlukan. Anda dapat mengunduh sendiri dengan browser, namun menggunakan R package `WDI` sangat disarankan.

Kelompok anda SAMA dengan kelompok di mata kuliah ILMU EKONOMI. Ada total 7 kelompok, di mana setiap kelompok harus menggunakan data pertumbuhan PDB, inflasi, dan tingkat pengangguran. Negara yang dibahas adalah sebagai berikut:

| kelompok | negara |
| --- | ------ |
| 1 | Indonesia |
| 2 | China |
| 3 | Singapura |
| 4 | Jepang |
| 5 | Amerika Serikat |
| 6 | Malaysia |
| 7 | Thailand |

Anda harus membahas 3 indikator tersebut secara tahunan dalam rentang waktu antara 2002-sekarang. Indikator yang anda perlukan adalah:

| indikator | kode WDI | link |
| ------ | --- | --- |
| GDP growth (annual %) | NY.GDP.MKTP.KD.ZG | [link](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG) |
| Inflation, consumer prices (annual %) | FP.CPI.TOTL.ZG | [link](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG) |
| Unemployment, total (% of total labor force) (national estimate) | SL.UEM.TOTL.NE.ZS | [link](https://data.worldbank.org/indicator/SL.UEM.TOTL.NE.ZS) |

Jika anda menggunakan package WDI, anda bisa pake 

## Pengumpulan

1. Format yang digunakan boleh word maupun pdf.
2. Gunakan halaman cover yang memuat informasi setidaknya judul tulisan, kelompok, kelas, tanggal, dan NIM dan nama anggota kelompok.
3. File dapat diupload di [link ini](https://forms.gle/rbS2dYsborq58b4Q7)
4. Deadline tugas ini sama dengan UAS yaitu tanggal 26 Januari 2024.