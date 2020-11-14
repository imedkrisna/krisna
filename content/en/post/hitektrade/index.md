---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "FDI, Industri, dan kebijakan perdagangan"
subtitle: ""
summary: ""
authors: [admin]
tags: [ekonomi, python, perdagangan, industri]
categories: [ekonomi, python, perdagangan, industri]
date: 2020-11-11T21:17:11+11:00
lastmod: 2020-11-11T21:17:11+11:00
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

Postingan kali ini akan membahas sedikit tentang perkembangan FDI di Indonesia.

## Perkembangan FDI Sejak 1970

Grafik di bawah ini menunjukkan net inflows FDI Indonesia dalam % PDB. Sumber data yang saya gunakan adalah World Bank World Development Indicators.


![png](./index_2_0.png)


Gambar di atas juga dibarengi dengan narasi yang disampaikan oleh Linblad (2015). Menurut beliau, ada paling tidak tiga pembagian besar narasi FDI di Indonesia. Pertama adalah sebelum tahun 1985 (oil boom), sesudah 1985 sampai pada saat krisis, dan reformasi.

## FDI dan industri teknologi tinggi

Sekali lagi saya menggunakan data World Development Indicator. Saya coba cari indikator yang ada kata kunci high-tech, dan WDI memunculkan empat indikator di bawah ini:




    id                 name
    -----------------  ------------------------------------------------------------------------------------
    NV.MNF.TECH.ZS.UN  Medium and high-tech Industry (including construction) (% manufacturing value added)
    TX.MNF.TECH.ZS.UN  Medium and high-tech exports (% manufactured exports)
    TX.VAL.TECH.CD     High-technology exports (current US$)
    TX.VAL.TECH.MF.ZS  High-technology exports (% of manufactured exports)



Saya menggunakan yang pertama untuk visualisasi di bawah ini. 


![png](./index_6_0.png)


Sepertinya FDI dan pertumbuhan teknologi tinggi di industri manufaktur tidak begitu ada hubungannya. Malah kayaknya kebalik: ketika ada FDI naik sebagai persen PDB, manufaktur teknologi tinggi malah berkurang. Tentu saja di manufaktur juga ada konstruksi dan juga pengolahan CPO. Selain itu, FDI-nya juga masuk ke industri pertambangan dan servis seperti e-commerce dan perbankan. Bisa jadi FDI-nya bukannya masuk ke industri teknologi tinggi, malah masuk ke industri-industri yang nilai tambah teknologi tinggi-nya rendah. Wajar, FDI akan masuk ke industri yang paling menguntungkan, dan ketika industri tersebut maju, faktor produksi akan masuk ke sana. Pertumbuhan industri teknologi tinggi jatuh pada 2005 dan tidak naik-naik lagi. 2005-an inilah puncak-puncaknya commodity boom dan so-called 'sunset industry'.

## Dua Non-Tariff Measures (NTM): TKDN dan Export Ban

TKDN adalah (Tingkat Komponen Dalan Negeri). Salah satu TKDN yang sangat ramai adalah soal Smartphone.

Gambar di bawah ini menunjukkan realisasi FDI (sumber: BKPM) di industri elektronika, piranti lunak, dan IT. TKDN untuk smartphone diwajibkan pada tahun 2016. Dapat kita lihat, FDI di tiga industri ini tiba-tiba meroket setelah 2016. 


    <Figure size 504x360 with 0 Axes>



![png](./index_8_1.png)


Di bawah ini adalah larangan ekspor mineral. Pada 2014 ekspor ini dilarang, meskipun direlaksasi pada 2017. Investasi logam dasar meningkat, sementara pertambangan bijih logam berkurang. Investor sepertinya masuk ke pengolahan mineral gara-gara larangan ekspor barang mentah.




    Text(2017-01-01 00:00:00, 300000, 'Relaxed')




![png](./index_10_1.png)


## Bagaimana dengan FDI dan pertumbuhan industri?

kali ini saya pake World Bank Global Economic Monitor (GEM) untuk mendapatkan pertumbuhan industri di Indonesia. Karena dalam constant USD, saya ubah jadi growth aja ($\Delta log$), meskipun masih tidak ideal.




    id         name
    ---------  -----------------------------------------------
    IPTOTNSKD  Industrial Production, constant US$
    IPTOTSAKD  Industrial Production, constant US$, seas. adj.






    <function matplotlib.pyplot.show(*args, **kw)>




![png](./index_13_1.png)


pertumbuhan industri, seperti kita lihat di atas, sempat negatif pada 2006. Selanjutnya cukup stagnan di sekitaran 4-5%. Sepertinya tidak ada hubungannya dengan FDI. Balik lagi, bisa jadi FDI-nya masuk bukan di industri manufaktur.
