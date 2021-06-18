---
title: Memulai
date: '2021-01-01'
type: book
weight: 10
---

## Installing tinytex

TinyTeX adalah paket untuk nge-run $\LaTeX$ di rmarkdown sehingga kita bisa _knit_ pdf. Ga harus punya miktex atau tex live kalau mau nulis $\LaTeX$ di RStudio. Cukup install TinyTeX aja. Instalasinya cuma dua line aja:

```r
install.packages('tinytex')
tinytex::install_tinytex()
```

lalu ganti di global option->sweave->xelatex atau pdflatex

Kerennya tinytex adalah, dia akan otomatis downloadin paket latex yg diperlukan utk ngerun kode kita. Jeleknya, ini artinya ketika kita ngerun kode baru yg butuh paket tertentu, kita butuh koneksi internet. Saya sendiri biasanya cuma pake beberapa paket latex aja jadi biasanya cuma pertama kali _knitting_ aja butuh internet. abis itu aman. Tapi ya setiap ada kode baru yang butuh paket baru, otomatis harus ada internet untuk donwload paket untuk nge-run kode baru tersebut.

Salah satu jalan keluar supaya kita selalu punya paket lengkap adalah dengan ngedownload lengkap semua paket latex yang ada. Ini sebenernya dari sisi efisiensi agak jelek karena orang-orang pada umumnya mungkin cuma pake 95% dari total paket yg ada. Tapi ini sangat berguna kalau anda sering kerja di tempat yang internetnya jelek dan punya kapasitas _storage_ yang cukup lega. 

Gunakan kode di bawah ini untuk menginstall secara penuh paket-paket latex yang ada di tinytex. Lakukan pas anda ada di tempat yg internetnya gratis dan lumayan kenceng karena yang didownload mungkin ada 4 giga-an.

```r
tinytex::tlmgr_install('scheme-full')
```

Setelah kode di atas selesai di run, tinytex anda akan aman kerja di tempat offline sekalipun.