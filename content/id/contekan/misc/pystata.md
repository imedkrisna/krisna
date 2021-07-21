---
title: Menjalankan Stata di rmarkdown dan jupyter notebook
linktitle: bye do file
summary: Saatnya meninggalkan do file karena Stata bisa dirun di RStudio dan di Jupyter
date: '2021-01-01'
type: book
weight: 10
---

Stata adalah software pertama yang pernah saya pakai. Beberapa paket di Stata sangat penting utk penelitian ku, yang sayangnya ga available di python dan r. Saya juga bukan ahli $\LaTeX$ dan lebih suka nulis dengan format *markdown*, yang mana ga bisa dirender oleh Stata lewat do file. Di samping itu, sebagian besar kolega saya juga masih pake Stata, jadinya saya sering kolep pake Stata. Semua hal-hal tersebut membuat saya Kadang-kadang masih suka pake Stata.

Untungnya Stata bisa dijalankan dari rmarkdown dan Jupyter. Sekarang saya kalo nulis sesuatu yang harus pake Stata bisa langsung di Rstudio atau Jupyter, ga harus run do filenya stata dulu. Enak deh pokoknya. Hehe.

Oh iya, ini ga berarti kita jadi bisa pake Stata di r dan python ya. Tida tida tida. Ini tuh cuma kaya pengganti do file aja. Jadi sebenernya buat naroh *script* aja dan bisa *seamless* dengan jurus-jurus lain di Jupyter dan r. Tetep aja yang menjalankan itu semua adalah Stata.exe. Jadi jangan lupa untuk membeli Stata yha!

## Stata dengan RStudio

Saya dapat cara ini dari [sini](https://rstudio-pubs-static.s3.amazonaws.com/357344_1da6bbd1723a4cb8a59722fa5422af79.html). Bisa nyalain Stata lewat rmarkdown tuh enak bangettt dan caranya ternyata mudah.

Pertama, kita harus cari lokasi Stata kita di komputer ada di mana. Kalo saya ada di `C:/Program Files/Stata16/StataMP-64.exe"`. Ini kita simpen dulu di suatu variabel biar gampang.

```r
statapath<-"C:/Program Files/Stata16/StataMP-64.exe"
```

abis itu, setiap chunk-nya Stata harus punya identitas `` ```{stata, engine.path=statapath, comment=""} CODE ``` ``

Perhatikan bahwa si `engine.path` harus diisi lokasi Stata di komputer kita. Jadinya aslinya tuh pas rmarkdown nge-render rmarkdownnya, pas di bagian si code chunk yang kita kasi identitas Stata, RStudio akan ngirim isi dari code chunknya ke Stata untuk di run dengan Stata.exe, lalu resultnya dibalikin ke RStudio untuk di-knit.

Intinya, code chunk yang dikasih identitas Stata bertindak sebagaimana do file.

misalnya:

```Stata
sysuse auto
summarize
```
  <pre><code>
. sysuse auto

. summarize

    Variable |        Obs        Mean    Std. Dev.       Min        Max
-------------+---------------------------------------------------------
        make |          0
       price |         74    6165.257    2949.496       3291      15906
         mpg |         74     21.2973    5.785503         12         41
       rep78 |         69    3.405797    .9899323          1          5
    headroom |         74    2.993243    .8459948        1.5          5
-------------+---------------------------------------------------------
       trunk |         74    13.75676    4.277404          5         23
      weight |         74    3019.459    777.1936       1760       4840
      length |         74    187.9324    22.26634        142        233
        turn |         74    39.64865    4.399354         31         51
displacement |         74    197.2973    91.83722         79        425
-------------+---------------------------------------------------------
  gear_ratio |         74    3.014865    .4562871       2.19       3.89
     foreign |         74    .2972973    .4601885          0          1
  </code></pre>




## Stata di Jupyter

Stata di Jupyter agak lebih tricky. Tapi dengan Stata 17, semua itu bukanlah ilusi semata!