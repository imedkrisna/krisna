---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Melihat pertumbuhan konsumsi Indonesia"
subtitle: ""
summary: ""
authors: [admin]
tags: [ekonomi]
categories: [ekonomi]
date: 2025-03-23T12:06:59+07:00
lastmod: 2025-03-23T12:06:59+07:00
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

Belakangan ini banyak reportase tentang lemahnya kelas menengah Indonesia saat ini. Kelas menengah Indonesia terus berkurang sejak 2018 hingga saat ini [tinggal 17% total penduduk](https://databoks.katadata.co.id/infografik/2024/09/05/populasi-kelas-menengah-indonesia-kian-berkurang). Padahal, pertumbuhan konsumsi acapkali mengandalkan kelas menengah. Benar saja, pertumbuhan konsumsi Indonesia memang telah lama berada di bawah kecepatan negara-negara lain di kawasan, kecuali Thailand.






```python
import seaborn as sns
import matplotlib as plt
import pandas as pd
import wbdata as wb

indi={"NE.CON.TOTL.KD.ZG":"Consumption"}

data=wb.get_dataframe(indi,country=["IDN","MYS","THA","VNM","PHL"],date=("2010","2024"),parse_dates=True)
sns.lineplot(data=data,x="date",y="Consumption",hue="country")
```




    <Axes: xlabel='date', ylabel='Consumption'>




    
![png](index_files/index_1_1.png)
    


Pertumbuhan konsumsi Indonesia telah cukup lama berada di bawah kecepatan pertumbuhan ekonomi secara umum. Kok bisa ya pertumbuhan ekonomi bisa lebih cepat dari pertumbuhan konsumsi?

Salah satu penjelasannya adalah karena pertumbuhan ekonomi ini dinikmati oleh pihak-pihak yang tidak terlalu tinggi _consumption share_-nya. Consumption share adalah bagian dari pendapatan seseorang yang digunakan untuk konsumsi. Biasanya, pihak-pihak ini adalah antara orang kaya atau perusahaan. Pihak-pihak ini sudah memiliki konsumsi yang tinggi. Pertambahan pendapatan untuk pihak-pihak ini lebih banyak digunakan untuk meningkatkan asetnya (menabung), atau meningkatkan konsumsinya di luar negeri. Saya sempat membahas permasalahan ini di [The Conversation Indonesia](https://theconversation.com/jokowi-resah-tabungan-mengendap-rp-690-triliun-di-bank-betulkah-masyarakat-yang-harus-belanja-200929).

Saya akan mencoba eksplorasi teori ini dengan menunjukkan 2 hal: (1) saving rate Indoensia semakin meningkat, dan (2) menurunnya labor share. Kedua hal ini saya tunjukkan dengan menggunakan [Total Ekonomi - Neraca Institusi Terintegrasi ( triliun rupiah), 2016 - 2023](https://www.bps.go.id/id/statistics-table/1/MjE4MSMx/total-ekonomi---neraca-institusi-terintegrasi---triliun-rupiah---2016---2023.html) dari BPS. Neraca ini adalah data yang sangat berguna dan menarik karena memiliki perhitungan semua 3 metode perhitungan Produk Domestik Bruto (PDB). Datanya saya olah sedikit dan dapat dilihat di akhir postingan ini.

## Saving rate yang meningkat

Saving rate menunjukkan seberapa besar pendapatan yang disimpan oleh masyarakat. Saving rate yang tinggi menunjukkan masyarakat lebih banyak menabung daripada mengkonsumsi. Seperti diskusi di atas, neraca ekonomi tidak membedakan siapa pemilik saving rate tersebut, tapi biasanya kenaikan saving rate yang sangat tinggi menunjukkan semakin tingginya _income share_ dari pihak yang lebih mungkin menabung, seperti orang kaya atau perusahaan.



```python
data=pd.read_excel("neraca.xlsx",sheet_name="Sheet3")
dat=data[["tahun","LS","KS"]]
dat=dat.melt("tahun",var_name="jenis",value_name="nilai")
det=data[["tahun","srhh"]]
```


```python
ax=sns.lineplot(data=det,x="tahun",y="srhh")
ax.set(xlabel="",ylabel="(%)",title="Saving rate (i.e., disposable income minus consumption),\nfrom Neraca Ekonomi BPS")
```




    [Text(0.5, 0, ''),
     Text(0, 0.5, '(%)'),
     Text(0.5, 1.0, 'Saving rate (i.e., disposable income minus consumption),\nfrom Neraca Ekonomi BPS')]




    
![png](index_files/index_4_1.png)
    


Sejak 2016, saving rate Indonesia terus meningkat. COVID-19 memaksa semua pihak mengurangi saving-nya, bahkan meningkatkan utang untuk menjaga konsumsi. Namun sejak itu, saving rate kembali naik bahkan lebih tinggi daripada biasanya. Sepertinya COVID-19 benar-benar memberi pukulan untuk kaum konsumen Indonesia.

Lebih jauh, saya nemu data menarik dari [Sistem Neraca Sosial Ekonomi (SNSE)](https://www.bps.go.id/id/publication/2024/10/31/9976e1b3df32ba9d98d76768/sistem-neraca-sosial-ekonomi-indonesia-2022.html) Indonesia 2022, courtesy of Prof AAY. Data disposable income dan gross saving dari situ sangat sangat menarik.

| No  | Institusi                                      | Disposable Income | Gross Saving |
| --- | ---------------------------------------------- | ----------------- | ------------------ |
| 1   | Rumah Tangga                                   | 11.368,51         | 1.231,47          |
|     | - Rumah Tangga 20%-1                           | 414,11            | -96,21            |
|     | - Rumah Tangga 20%-2                           | 924,70            | 34,63             |
|     | - Rumah Tangga 20%-3                           | 1.782,32          | 189,10            |
|     | - Rumah Tangga 20%-4                           | 2.657,59          | 326,76            |
|     | - Rumah Tangga 20%-5                           | 5.589,80          | 777,18            |
| 2   | Lembaga Non Profit yang Melayani Rumah Tangga  | 294,48            | 65,48             |
| 3   | Pemerintah                                     | 1.620,85          | 115,84            |
| 4   | Korporasi Non Finansial                        | 5.498,78          | 5.498,78          |
| 5   | Korporasi Finansial                            | 554,52            | 529,83            |
|     | **Total**                                      | **19.337,14**     | **7.441,39**      |

Gw coba bikin tabel pake pandas untuk ngitung saving rate dan benar saja opkors, makin kaya kelompok masyarakat, makin gede saving ratenya. Tentu ini minus orang ultra kaya yah. Dan ya, bottom 20% makan tabungan / utang di 2022. Pinjol?


```python
wew=pd.read_csv("snse.txt")
wew['saving rate']=wew['Gross saving']/wew['Disposable Income']*100
wew
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>No</th>
      <th>Institusi</th>
      <th>Disposable Income</th>
      <th>Gross saving</th>
      <th>saving rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>Rumah Tangga</td>
      <td>11368.51</td>
      <td>1231.47</td>
      <td>10.832290</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>Rumah Tangga 20%-1</td>
      <td>414.11</td>
      <td>-96.21</td>
      <td>-23.232957</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>Rumah Tangga 20%-2</td>
      <td>924.70</td>
      <td>34.63</td>
      <td>3.744998</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>Rumah Tangga 20%-3</td>
      <td>1782.32</td>
      <td>189.10</td>
      <td>10.609767</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Rumah Tangga 20%-4</td>
      <td>2657.59</td>
      <td>326.76</td>
      <td>12.295350</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>Rumah Tangga 20%-5</td>
      <td>5589.80</td>
      <td>777.18</td>
      <td>13.903539</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.0</td>
      <td>Lembaga Non Profit yang Melayani Rumah Tangga</td>
      <td>294.48</td>
      <td>65.48</td>
      <td>22.235805</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3.0</td>
      <td>Pemerintah</td>
      <td>1620.85</td>
      <td>115.84</td>
      <td>7.146867</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.0</td>
      <td>Korporasi Non Finansial</td>
      <td>5498.78</td>
      <td>5498.78</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5.0</td>
      <td>Korporasi Finansial</td>
      <td>554.52</td>
      <td>529.83</td>
      <td>95.547501</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>Total</td>
      <td>19337.14</td>
      <td>7441.39</td>
      <td>38.482371</td>
    </tr>
  </tbody>
</table>
</div>



## Labor share yang menurun

Beberapa analis mengatakan bahwa salah satu problemnya adalah lemahnya pertumbuhan upah. Reed, Pasha dan Gonzales dalam [reportnya untuk World Bank Group](https://documents1.worldbank.org/curated/en/099754312062434827/pdf/IDU11c5662011a9eb14aee18baa1e0efad04ad35.pdf) menuliskan tentang lemahnya pertumbuhan upah dan profit di perusahaan manufaktur dengan kepemilikan asing yang tinggi. Cuplikan gambar di bawah ini berasal dari report tersebut.

![](Picture1.png)

Di neraca ekonomi, kita juga dapat menghitung seberapa besar _primary income_ dibayarkan untuk banyak keperluan. Saya membaginya menjadi 3: pajak, biaya pegawai, dan profit. Profit sendiri isinya adalah income yang sudah dikurangi pajak dan pegawai. Saya plot di bawah, tapi pajak saya keluarkan karena angkanya kecil banget, sekitar 5% total neraca[^1].

[^1]: Angka 5% ini cukup menarik karena pph badan Indonesia angkanya jauh di atas itu. Ini bisa jadi 1 posting sendiri lagi. mungkin kapan-kapan deh.


```python
ax=sns.lineplot(data=dat,x="tahun",y="nilai",hue="jenis",palette="tab10")
ax.set(xlabel="",ylabel="(%)",title="Labor share (LS) and profit share (KS) of income, from Neraca Ekonomi BPS")
```




    [Text(0.5, 0, ''),
     Text(0, 0.5, '(%)'),
     Text(0.5, 1.0, 'Labor share (LS) and profit share (KS) of income, from Neraca Ekonomi BPS')]




    
![png](index_files/index_8_1.png)
    



Dan cukup telrihat progresifnya peningkatan bagian pendapatan yang diserap oleh perusahaan. Seperti hipotesis di atas, peningkatan income share perusahaan lebih mungkin ditabung sementara peningkatan income share pegawai lebih mungkin dikonsumsi. Jadi setidaknya dari hasil ini, cukup wajar.

Anyway, sebenernya post ini cuma buat kasi liat grafik. Diskusi bisa kita lakukan di luar post ini. Let me know what you think.

Anyway, di bawah ini data yang saya pake. semua diunduh dari [Total Ekonomi - Neraca Institusi Terintegrasi ( triliun rupiah), 2016 - 2023](https://www.bps.go.id/id/statistics-table/1/MjE4MSMx/total-ekonomi---neraca-institusi-terintegrasi---triliun-rupiah---2016---2023.html) dengan sedikit olahan.


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tahun</th>
      <th>L</th>
      <th>K</th>
      <th>T</th>
      <th>va/output</th>
      <th>LS</th>
      <th>TS</th>
      <th>KS</th>
      <th>srhh</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>40.576885</td>
      <td>55.127270</td>
      <td>4.295845</td>
      <td>52.877975</td>
      <td>41.728750</td>
      <td>4.435895</td>
      <td>53.835356</td>
      <td>30.864658</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017</td>
      <td>41.472019</td>
      <td>53.934836</td>
      <td>4.593145</td>
      <td>53.108782</td>
      <td>42.704020</td>
      <td>4.746633</td>
      <td>52.549347</td>
      <td>31.795110</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018</td>
      <td>39.977940</td>
      <td>55.237447</td>
      <td>4.784614</td>
      <td>52.986106</td>
      <td>41.343331</td>
      <td>4.965863</td>
      <td>53.690807</td>
      <td>32.159447</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019</td>
      <td>39.252272</td>
      <td>55.950651</td>
      <td>4.797077</td>
      <td>52.971298</td>
      <td>40.403369</td>
      <td>4.954449</td>
      <td>54.642181</td>
      <td>31.793236</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2020</td>
      <td>37.304707</td>
      <td>58.410155</td>
      <td>4.285138</td>
      <td>53.170697</td>
      <td>38.341668</td>
      <td>4.418889</td>
      <td>57.239443</td>
      <td>30.021169</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2021</td>
      <td>37.283856</td>
      <td>58.021987</td>
      <td>4.694157</td>
      <td>53.484228</td>
      <td>38.272325</td>
      <td>4.833429</td>
      <td>56.894245</td>
      <td>33.807914</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2022</td>
      <td>35.453018</td>
      <td>59.557783</td>
      <td>4.989199</td>
      <td>53.799988</td>
      <td>36.094115</td>
      <td>5.095040</td>
      <td>58.810845</td>
      <td>38.504459</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2023</td>
      <td>34.970118</td>
      <td>60.019108</td>
      <td>5.010774</td>
      <td>53.400921</td>
      <td>36.068580</td>
      <td>5.184493</td>
      <td>58.746927</td>
      <td>36.506632</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
