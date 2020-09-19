---
date: "2020-08-20T00:00:00+01:00"
draft: false
linktitle: Pandas
menu:
  example:
    parent: Memulai dengan Python 
    weight: 3
title: Menggunakan Pandas
toc: true
type: docs
weight: 3
editable: false
commentable: false
---

Pandas adalah *library* atau paket yang kita gunakan untuk mengutik-utik data. Beberapa hal sederhana yang anda dapat lakukan di pandas, dapat juga dilakukan dengan menggunakan Google Sheet atau Microsoft Excel. Jika anda lebih familiar dengan tools seperti tersebut, gunakan sheets juga nda papa. Lebih lagi, nge-print seluruh isi dataset di Pandas bisa makan memori jika data anda sangat besar. Anda dapat gunakan sheets untuk melihat datanya, tapi dimanipulasi di python juga bisa. *Whatever works for you*. Di sini, kita akan coba memanipulasi dengan pandas.

Zaman sekarang sih fitur-fitur di Microsoft Excel dan Google Sheet sudah sangat canggih, terlebih dalam hal menyedot data secara real-time dari internet. Tentu saja kedua aplikasi di atas kurang canggih kalau dipakai untuk programming atau statistik yang agak lebih canggih daripada OLS. Karena itu, menggunakan Pandas lebih disarankan. 

Memang memanipulasi data di Sheet lebih intuitif dan bisa jadi lebih cepet, terutama kalau datanya tidak terlalu besar. Namun kelebihan Pandas diantaranya adalah ketika anda harus berurusan dengan *time-series* atau *panel data*, melakukan *sorting* / *grouping* dan semacamnya juga lebih cepat dengan Pandas. Anda juga nanti akan berurusan dengan mengecek dan memanipulasi *missing values*, yang lebih cepat jika menggunakan Pandas. Kelebihan lainnya, semua manipulasi yang anda lakukan akan terdokumentasi di Notebook anda. Anda tidak perlu (bahkan sebaiknya tidak) mengubah data aslinya. Tinggal re-run saja kode di Notebook jika ingin melihat kembali hasil analisis anda

Untuk menggunakan Pandas, Kita memanggilnya dengan:


```python
import pandas as pd
```

setelah itu, semua fungsi yang terkait dengan pandas dapat kita gunakan dengan awalan `pd`. Dokumentasi lengkap soal fungsi apa saja yang ada di `pandas` dapat dibaca di [dokumentasi resmi di sini](https://pandas.pydata.org/pandas-docs/stable/index.html). Tentu saja anda juga bisa menggunakan gugel.

#### Data Frame
Data Frame bentuknya seperti ini:


```python
# menulis data dari awal. 
data = {'Nama':['imed', 'krisna', 'wisnu', 'gupta'], 'pekerjaan':['Ekonom', 'kontraktor', 'pelajar', 'tukang baso'], 'usia':[30, 27, 19, 25]} 

# print
data
```




    {'Nama': ['imed', 'krisna', 'wisnu', 'gupta'],
     'pekerjaan': ['Ekonom', 'kontraktor', 'pelajar', 'tukang baso'],
     'usia': [30, 27, 19, 25]}



Seperti anda lihat, data di atas bentuknya kurang enak dilihat. Datanya sih jadi, tapi kurang intuitif. Jika kita gunakan panda data frame, hasilnya lebih enak dilihat dan lebih ada artinya.


```python
# jadikan data ke dalam dataframe
data = pd.DataFrame(data) 
  
# Print df. 
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
      <th>Nama</th>
      <th>pekerjaan</th>
      <th>usia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>imed</td>
      <td>Ekonom</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>krisna</td>
      <td>kontraktor</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wisnu</td>
      <td>pelajar</td>
      <td>19</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gupta</td>
      <td>tukang baso</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



Tabel di atas memiliki 1 header (baris paling atas), 4 baris (rows), dan 3 kolom (columns). Angka [0,1,2,3] disebut juga dengan index. Index ini juga ada di aplikasi Microsoft Excel maupun Google Sheet, yaitu nomor rows. Ingat kalau di excel kolom diberi index huruf sementara baris diberi index angka. Di Pandas, kolom tidak diberi index spesifik.

Kolom merepresentasikan nama variabel (atau disebut juga dengan *series*), sementara baris merepresentasikan observasi. Ada 3 variabel di tabel di atas, yaitu Nama, Pekerjaan, dan Usia. Sementara itu, ada 4 observasi. Pokoknya Pandas tuh persis banget lah sama Microsoft Excel maupun Google Sheet.

#### Membuat series baru

Sekarang kita punya sebuah jenis data, yaitu `data` yang sudah berbentuk DataFrame. Mari kita coba buat series baru yang berisi angka acak (random). Untuk menghasilkan angka acak, kita butuh paket `Numpy`


```python
import numpy as np
series=pd.Series(np.random.randn(4), name='gaji')
series
```




    0    0.434327
    1   -0.355109
    2   -0.229159
    3    0.865556
    Name: gaji, dtype: float64



data di `series` bisa kita manipulasi seperti di excel dengan mengalikan atau membagi dengan angka lain. Jika kita kali dengan sebuah angka, maka seluruh anggota series tersebut akan dikali dengan angka tersebut. (catatan: bedakan series dengan matrix!)


```python
series+10 # setiap anggota series kita tambahkan 10
```




    0    10.434327
    1     9.644891
    2     9.770841
    3    10.865556
    Name: gaji, dtype: float64




```python
series/10 # setiap anggota series kita bagi 10
```




    0    0.043433
    1   -0.035511
    2   -0.022916
    3    0.086556
    Name: gaji, dtype: float64




```python
np.log(series+10) # setiap anggota series kita transformasi natural log 10
```




    0    2.345101
    1    2.266428
    2    2.279403
    3    2.385598
    Name: gaji, dtype: float64



kita juga bisa menempelkan series menjadi anggota baru dari df


```python
data['gaji']=series
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
      <th>Nama</th>
      <th>pekerjaan</th>
      <th>usia</th>
      <th>gaji</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>imed</td>
      <td>Ekonom</td>
      <td>30</td>
      <td>0.434327</td>
    </tr>
    <tr>
      <th>1</th>
      <td>krisna</td>
      <td>kontraktor</td>
      <td>27</td>
      <td>-0.355109</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wisnu</td>
      <td>pelajar</td>
      <td>19</td>
      <td>-0.229159</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gupta</td>
      <td>tukang baso</td>
      <td>25</td>
      <td>0.865556</td>
    </tr>
  </tbody>
</table>
</div>



dapat anda lihat di atas bahwa saya membuat sebuah kolom baru dengan menggunakan kurung siku. kode `data['gaji']` berarti saya membuat sebuah kolom baru bernama gaji, yang anggotanya saya ambil dari series. Dengan kata lain, kode `<data.frame>[nama.kolom]` kita gunakan untuk memanggil kolom tersebut.

Contoh penggunaan:


```python
data['usia'] # memanggil hanya kolom usia
```




    0    30
    1    27
    2    19
    3    25
    Name: usia, dtype: int64



Gajinya kok kecil banget ya. ada yang negatif lagi. mari kita ganti angka-angka di gaji tersebut dengan angka yang lebih masuk akal


```python
data['gaji']=(data['gaji']+1)*10000 # apakah anda bisa menebak apa yang terjadi?
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
      <th>Nama</th>
      <th>pekerjaan</th>
      <th>usia</th>
      <th>gaji</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>imed</td>
      <td>Ekonom</td>
      <td>30</td>
      <td>14343.266315</td>
    </tr>
    <tr>
      <th>1</th>
      <td>krisna</td>
      <td>kontraktor</td>
      <td>27</td>
      <td>6448.905246</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wisnu</td>
      <td>pelajar</td>
      <td>19</td>
      <td>7708.407117</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gupta</td>
      <td>tukang baso</td>
      <td>25</td>
      <td>18655.559599</td>
    </tr>
  </tbody>
</table>
</div>



Masih kecil?? oh gampang. Yang perlu saya ganti hanyalah nama kolom saja


```python
data=data.rename(columns={'gaji':'gaji (USD)'})
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
      <th>Nama</th>
      <th>pekerjaan</th>
      <th>usia</th>
      <th>gaji (USD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>imed</td>
      <td>Ekonom</td>
      <td>30</td>
      <td>14343.266315</td>
    </tr>
    <tr>
      <th>1</th>
      <td>krisna</td>
      <td>kontraktor</td>
      <td>27</td>
      <td>6448.905246</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wisnu</td>
      <td>pelajar</td>
      <td>19</td>
      <td>7708.407117</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gupta</td>
      <td>tukang baso</td>
      <td>25</td>
      <td>18655.559599</td>
    </tr>
  </tbody>
</table>
</div>



gimana? Jadi gede ya gajinya? Wkwkw. begitulah cara mengganti nama kolom.

Anda juga bisa melihat deskripsi statistik dari data anda dengan menggunakan `nama.describe`


```python
data.describe()
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
      <th>usia</th>
      <th>gaji (USD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>25.250000</td>
      <td>11789.034569</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.645787</td>
      <td>5739.970017</td>
    </tr>
    <tr>
      <th>min</th>
      <td>19.000000</td>
      <td>6448.905246</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>23.500000</td>
      <td>7393.531649</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>26.000000</td>
      <td>11025.836716</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>27.750000</td>
      <td>15421.339636</td>
    </tr>
    <tr>
      <th>max</th>
      <td>30.000000</td>
      <td>18655.559599</td>
    </tr>
  </tbody>
</table>
</div>



describe hanya memunculkan informasi `float` maupun `integer` tapi tidak `string`. Count berarti jumlah observasi (atau jumlah baris), sisanya sudah pada tau ya?

#### Latihan lanjutan
Untuk latihan berikutnya, mari kita gunakan data yang sudah saya siapkan untuk latihan. Datanya bisa ditarik dari website saya.


```python
# menarik data dari internet dengan menggunakan read_csv dan diassign ke `lat`
lat=pd.read_csv('https://krisna.netlify.app/courses/pystat/latihan.csv')
lat
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
      <th>Country Name</th>
      <th>ARI treatment (% of children under 5 taken to a health provider)</th>
      <th>Access to clean fuels and technologies for cooking (% of population)</th>
      <th>Access to electricity (% of population)</th>
      <th>Access to electricity, rural (% of rural population)</th>
      <th>Access to electricity, urban (% of urban population)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, female (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, male (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, older adults (% of population ages 25+)</th>
      <th>...</th>
      <th>Women participating in the three decisions (own health care, major household purchases, and visiting family) (% of women age 15-49)</th>
      <th>Women who believe a husband is justified in beating his wife (any of five reasons) (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she argues with him (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she burns the food (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she goes out without telling him (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she neglects the children (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she refuses sex with him (%)</th>
      <th>Women who were first married by age 15 (% of women ages 20-24)</th>
      <th>Women who were first married by age 18 (% of women ages 20-24)</th>
      <th>Women's share of population ages 15+ living with HIV (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>97.700000</td>
      <td>97.091973</td>
      <td>99.500000</td>
      <td>14.893312</td>
      <td>7.160685</td>
      <td>22.536495</td>
      <td>18.016499</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>40.015171</td>
      <td>38.102959</td>
      <td>42.043503</td>
      <td>42.513248</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>42.776627</td>
      <td>29.268730</td>
      <td>56.254936</td>
      <td>48.747078</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>45.9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Samoa</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andorra</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>212</th>
      <td>Virgin Islands (U.S.)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>213</th>
      <td>West Bank and Gaza</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.700000</td>
      <td>99.070331</td>
      <td>99.900000</td>
      <td>25.022177</td>
      <td>15.910773</td>
      <td>34.436001</td>
      <td>33.076920</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>214</th>
      <td>Yemen, Rep.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>79.200000</td>
      <td>68.766799</td>
      <td>97.735039</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22.8</td>
    </tr>
    <tr>
      <th>215</th>
      <td>Zambia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.300000</td>
      <td>13.997699</td>
      <td>75.200000</td>
      <td>45.863258</td>
      <td>40.278877</td>
      <td>51.680923</td>
      <td>48.338139</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.3</td>
    </tr>
    <tr>
      <th>216</th>
      <td>Zimbabwe</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.482048</td>
      <td>19.152600</td>
      <td>85.317101</td>
      <td>55.285137</td>
      <td>51.664925</td>
      <td>59.227501</td>
      <td>58.877064</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.7</td>
    </tr>
  </tbody>
</table>
<p>217 rows × 1432 columns</p>
</div>



Seperti anda lihat pada tabel di atas, data ini jauh lebih besar daripada `data` yang cuma 4 baris dan 4 kolom. Kali ini, ada total 217 baris dan 1432 kolom! Data diatas merupakan basis data [World Bank World Development Indicators](http://datatopics.worldbank.org/world-development-indicators/) yang diunduh secara bulk. Data tersebut terdiri dari 217 negara yang masing-masing terdapat angka untuk 1432 indikator.

Dengan tabel sebesar itu, anda hanya dapat melihat beberapa saja. Jupyter Notebook hanya akan menampilkan 5 data teratas, 5 terbawah, 10 paling kiri dan 10 paling kanan. Jika dilihat semua, maka akan kegedean dan tidak cukup Jupyter Notebooknya. Jika anda ingin melihat semuanya, lebih baik didownload dalam bentuk csv dan dibuka pakai google sheet atau microsoft excel.

Untuk download data ini, gunakan fungsi:
```python
lat.to_csv("latihan.csv")
```
Data tersebut akan tersimpan di tempan anda menginstall `Anaconda`. Biasanya akan ada di `C:\Users\nama\`.

Untuk lanjut sih kita tidak perlu download datanya. Untuk sekarang, kita akan bermain-main dengan `lat`

Pertama, Coba kita pilih beberapa negara saja, misalnya negara-negara ASEAN dan RRT. kita akan menggunakan fungsi `loc`. Langkah pertama untuk menggunakan loc adalah ngeset nama negara menjadi index, lalu menggunakan nama negara untuk membuat dataframe baru sesuai dengan nama-nama negara yang kita pilih.


```python
lat=lat.set_index('Country Name') # menjadikan nama negara sebagai index
# memilih negara-negara yang mau disimpan
countries=['Indonesia','China','Malaysia','Singapore','Thailand','Vietnam','Brunei Darussalam','Lao PDR','Cambodia','Myanmar','Philippines']
lat2=lat.loc[countries]           # menggunakan fungsi loc[index] dan menempelkannya ke dataframe baru bernama lat2
lat2                              # ngeprint data baru lat2
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
      <th>ARI treatment (% of children under 5 taken to a health provider)</th>
      <th>Access to clean fuels and technologies for cooking (% of population)</th>
      <th>Access to electricity (% of population)</th>
      <th>Access to electricity, rural (% of rural population)</th>
      <th>Access to electricity, urban (% of urban population)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, female (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, male (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, older adults (% of population ages 25+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, poorest 40% (% of population ages 15+)</th>
      <th>...</th>
      <th>Women participating in the three decisions (own health care, major household purchases, and visiting family) (% of women age 15-49)</th>
      <th>Women who believe a husband is justified in beating his wife (any of five reasons) (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she argues with him (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she burns the food (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she goes out without telling him (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she neglects the children (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she refuses sex with him (%)</th>
      <th>Women who were first married by age 15 (% of women ages 20-24)</th>
      <th>Women who were first married by age 18 (% of women ages 20-24)</th>
      <th>Women's share of population ages 15+ living with HIV (%)</th>
    </tr>
    <tr>
      <th>Country Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Indonesia</th>
      <td>92.1</td>
      <td>NaN</td>
      <td>98.140000</td>
      <td>96.030359</td>
      <td>99.890000</td>
      <td>48.857452</td>
      <td>51.354919</td>
      <td>46.245716</td>
      <td>49.497471</td>
      <td>36.595760</td>
      <td>...</td>
      <td>68.2</td>
      <td>32.0</td>
      <td>4.4</td>
      <td>1.7</td>
      <td>19.0</td>
      <td>27.2</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35.6</td>
    </tr>
    <tr>
      <th>China</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>80.229118</td>
      <td>76.364731</td>
      <td>83.966637</td>
      <td>79.261734</td>
      <td>68.350258</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Malaysia</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>85.343750</td>
      <td>82.478539</td>
      <td>87.916290</td>
      <td>85.817039</td>
      <td>80.504547</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>17.8</td>
    </tr>
    <tr>
      <th>Singapore</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>97.931168</td>
      <td>96.312927</td>
      <td>99.682663</td>
      <td>97.947220</td>
      <td>96.378250</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.4</td>
    </tr>
    <tr>
      <th>Thailand</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.900000</td>
      <td>99.900000</td>
      <td>99.900000</td>
      <td>81.594002</td>
      <td>79.780106</td>
      <td>83.691376</td>
      <td>83.174179</td>
      <td>77.546707</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>44.1</td>
    </tr>
    <tr>
      <th>Vietnam</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>30.795792</td>
      <td>30.419701</td>
      <td>31.205099</td>
      <td>29.921171</td>
      <td>20.277523</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.7</td>
    </tr>
    <tr>
      <th>Brunei Darussalam</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Lao PDR</th>
      <td>39.8</td>
      <td>NaN</td>
      <td>93.600000</td>
      <td>90.510483</td>
      <td>99.500000</td>
      <td>29.056417</td>
      <td>31.874203</td>
      <td>26.115883</td>
      <td>31.726784</td>
      <td>17.370375</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>44.7</td>
    </tr>
    <tr>
      <th>Cambodia</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.070000</td>
      <td>86.089343</td>
      <td>99.060000</td>
      <td>21.671783</td>
      <td>21.526394</td>
      <td>21.845457</td>
      <td>22.586687</td>
      <td>14.304063</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>52.9</td>
    </tr>
    <tr>
      <th>Myanmar</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>69.814837</td>
      <td>59.919135</td>
      <td>92.554521</td>
      <td>25.992298</td>
      <td>25.978712</td>
      <td>26.007711</td>
      <td>30.841911</td>
      <td>22.543983</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>38.2</td>
    </tr>
    <tr>
      <th>Philippines</th>
      <td>67.3</td>
      <td>NaN</td>
      <td>93.000000</td>
      <td>90.023167</td>
      <td>96.400000</td>
      <td>34.498409</td>
      <td>38.854164</td>
      <td>30.019701</td>
      <td>38.828045</td>
      <td>18.026352</td>
      <td>...</td>
      <td>85.0</td>
      <td>10.9</td>
      <td>2.2</td>
      <td>1.3</td>
      <td>3.4</td>
      <td>8.6</td>
      <td>1.3</td>
      <td>2.2</td>
      <td>16.5</td>
      <td>6.1</td>
    </tr>
  </tbody>
</table>
<p>11 rows × 1431 columns</p>
</div>



Setelah kita sukses punya 11 row saja langkah berikutnya adalah memilih variabel yang mau kita simpan. Tabel di atas punya 1431 kolom (atau 1431 indikator). Tentu tidak semuanya kita perlukan. Kita bisa pilih beberapa indikator pilihan. Misalnya mari kita pilih `GDP (current US$)`, `Official exchange rate (LCU per US$, period average)`, dan `Merchandise trade (% of GDP)`.


```python
var=['GDP (current US$)','Official exchange rate (LCU per US$, period average)','Merchandise trade (% of GDP)']
lat2=lat2[var]
lat2
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
      <th>GDP (current US$)</th>
      <th>Official exchange rate (LCU per US$, period average)</th>
      <th>Merchandise trade (% of GDP)</th>
    </tr>
    <tr>
      <th>Country Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Indonesia</th>
      <td>1.015619e+12</td>
      <td>13380.833879</td>
      <td>32.072665</td>
    </tr>
    <tr>
      <th>China</th>
      <td>1.231041e+13</td>
      <td>6.758755</td>
      <td>33.363133</td>
    </tr>
    <tr>
      <th>Malaysia</th>
      <td>3.189582e+11</td>
      <td>4.300441</td>
      <td>129.655533</td>
    </tr>
    <tr>
      <th>Singapore</th>
      <td>3.418633e+11</td>
      <td>1.380925</td>
      <td>205.160629</td>
    </tr>
    <tr>
      <th>Thailand</th>
      <td>4.562947e+11</td>
      <td>33.939811</td>
      <td>100.407477</td>
    </tr>
    <tr>
      <th>Vietnam</th>
      <td>2.237799e+11</td>
      <td>22370.086667</td>
      <td>191.229447</td>
    </tr>
    <tr>
      <th>Brunei Darussalam</th>
      <td>1.212810e+10</td>
      <td>1.380891</td>
      <td>71.371415</td>
    </tr>
    <tr>
      <th>Lao PDR</th>
      <td>1.685309e+10</td>
      <td>8244.843189</td>
      <td>62.540469</td>
    </tr>
    <tr>
      <th>Cambodia</th>
      <td>2.217720e+10</td>
      <td>4050.579986</td>
      <td>118.653389</td>
    </tr>
    <tr>
      <th>Myanmar</th>
      <td>6.894587e+10</td>
      <td>1360.358707</td>
      <td>48.055092</td>
    </tr>
    <tr>
      <th>Philippines</th>
      <td>3.284807e+11</td>
      <td>50.403720</td>
      <td>51.940336</td>
    </tr>
  </tbody>
</table>
</div>



Nah sekarang kita punya 11 negara

#### Menggunakan Pandas Datareader
Pertama, install dulu di anaconda prompt dengan menggunakan kode:
```
conda install -c anaconda pandas-datareader
```
Setelah selesai, kita bisa panggil dengan menggunakan impor
```
import pandas_datareader as pdr
```
Mari kita coba

#### Contoh: Mempersiapkan data untuk latihan

Kita akan menggunakan contoh bagaimana saya mempersiapkan data untuk latihan. Data yang saya gunakan adalah [World Development Indicators (bulk download)](http://datatopics.worldbank.org/world-development-indicators/) bikinan [The World Bank](https://www.worldbank.org/). Tentu saja anda tidak perlu mendownloadnya sendiri karena saya sudah mendownloadnya. muehehe. 

Datanya gede banget, sehingga tidak saya upload di website. Namun anda dapat dengan bebas mendownloadnya. Jika anda ingin mempraktikkan kode-kode yang digunakan di contoh ini, anda perlu download sendiri datanya dari link bulk download di atas.

Data utamanya memiliki ukuran 193,5 MB. Kalau dibuka pakai excel bisa memakan waktu lumayan lama. Datanya memiliki ekstensi .csv sehingga kita import dengan `pd.read_csv`.


```python
df=pd.read_csv('C:/data WDI/WDIData.csv') # mengimpor data dari lokasi saya menyimpan data tersebut
df                                        # print
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
      <th>Country Name</th>
      <th>Country Code</th>
      <th>Indicator Name</th>
      <th>Indicator Code</th>
      <th>1960</th>
      <th>1961</th>
      <th>1962</th>
      <th>1963</th>
      <th>1964</th>
      <th>1965</th>
      <th>...</th>
      <th>2011</th>
      <th>2012</th>
      <th>2013</th>
      <th>2014</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
      <th>2018</th>
      <th>2019</th>
      <th>Unnamed: 64</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Access to clean fuels and technologies for coo...</td>
      <td>EG.CFT.ACCS.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>82.783289</td>
      <td>83.120303</td>
      <td>83.533457</td>
      <td>83.897596</td>
      <td>84.171599</td>
      <td>84.510171</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Access to electricity (% of population)</td>
      <td>EG.ELC.ACCS.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>87.199474</td>
      <td>87.512260</td>
      <td>88.129881</td>
      <td>87.275323</td>
      <td>88.720097</td>
      <td>89.308602</td>
      <td>90.283638</td>
      <td>89.286856</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Access to electricity, rural (% of rural popul...</td>
      <td>EG.ELC.ACCS.RU.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>75.958878</td>
      <td>77.251714</td>
      <td>78.165706</td>
      <td>75.512153</td>
      <td>78.211000</td>
      <td>79.065508</td>
      <td>81.102134</td>
      <td>79.248100</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Access to electricity, urban (% of urban popul...</td>
      <td>EG.ELC.ACCS.UR.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>96.466418</td>
      <td>96.435957</td>
      <td>96.772853</td>
      <td>96.466705</td>
      <td>96.936319</td>
      <td>97.290083</td>
      <td>97.467915</td>
      <td>97.063959</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Account ownership at a financial institution o...</td>
      <td>FX.OWN.TOTL.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>22.260538</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.277130</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.165211</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>377779</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>Women who believe a husband is justified in be...</td>
      <td>SG.VAW.NEGL.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>21.400000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21.400000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377780</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>Women who believe a husband is justified in be...</td>
      <td>SG.VAW.REFU.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>16.900000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14.500000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377781</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>Women who were first married by age 15 (% of w...</td>
      <td>SP.M15.2024.FE.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>3.900000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.700000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377782</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>Women who were first married by age 18 (% of w...</td>
      <td>SP.M18.2024.FE.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>30.500000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>33.500000</td>
      <td>32.400000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377783</th>
      <td>Zimbabwe</td>
      <td>ZWE</td>
      <td>Women's share of population ages 15+ living wi...</td>
      <td>SH.DYN.AIDS.FE.ZS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>59.100000</td>
      <td>59.300000</td>
      <td>59.500000</td>
      <td>59.600000</td>
      <td>59.600000</td>
      <td>59.700000</td>
      <td>59.700000</td>
      <td>59.800000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>377784 rows × 65 columns</p>
</div>



Seperti anda lihat, data di atas aslinya besar sekali, mengandung lebih dari 370ribu baris dan 65 kolom. Setiap baris terdiri dari nama negara dan nama indikator, sementara kolomnya menandakan waktu. Bentuk seperti ini disebut juga dengan **Panel Data**, yaitu sebuah data yang memiliki struktur **cross section** (negara dan indikator) dan **time series** (tahun) sekaligus.

Untuk latihan, saya menggunakan data yang sifatnya **cross section**, yaitu terdiri atas nama negara dan nama indikator saja. Saya akan mengambil tahun 2017. Karena hanya menangkap indikator di satu tahun saja, makanya disebut **cross section**.

Gunakan `pd.info` untuk melihat tipe elemen dan ukuran (memori) data.


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 377784 entries, 0 to 377783
    Data columns (total 65 columns):
     #   Column          Non-Null Count   Dtype  
    ---  ------          --------------   -----  
     0   Country Name    377784 non-null  object 
     1   Country Code    377784 non-null  object 
     2   Indicator Name  377784 non-null  object 
     3   Indicator Code  377784 non-null  object 
     4   1960            37085 non-null   float64
     5   1961            41471 non-null   float64
     6   1962            43673 non-null   float64
     7   1963            43553 non-null   float64
     8   1964            44098 non-null   float64
     9   1965            46608 non-null   float64
     10  1966            46314 non-null   float64
     11  1967            48032 non-null   float64
     12  1968            47594 non-null   float64
     13  1969            49477 non-null   float64
     14  1970            70456 non-null   float64
     15  1971            76771 non-null   float64
     16  1972            79536 non-null   float64
     17  1973            79135 non-null   float64
     18  1974            80551 non-null   float64
     19  1975            84584 non-null   float64
     20  1976            86656 non-null   float64
     21  1977            90100 non-null   float64
     22  1978            89719 non-null   float64
     23  1979            90588 non-null   float64
     24  1980            95296 non-null   float64
     25  1981            97177 non-null   float64
     26  1982            98454 non-null   float64
     27  1983            98272 non-null   float64
     28  1984            99067 non-null   float64
     29  1985            100337 non-null  float64
     30  1986            101118 non-null  float64
     31  1987            102475 non-null  float64
     32  1988            102052 non-null  float64
     33  1989            103850 non-null  float64
     34  1990            127202 non-null  float64
     35  1991            132640 non-null  float64
     36  1992            136741 non-null  float64
     37  1993            137957 non-null  float64
     38  1994            139967 non-null  float64
     39  1995            148014 non-null  float64
     40  1996            147733 non-null  float64
     41  1997            148909 non-null  float64
     42  1998            150831 non-null  float64
     43  1999            156211 non-null  float64
     44  2000            181781 non-null  float64
     45  2001            172155 non-null  float64
     46  2002            176998 non-null  float64
     47  2003            177612 non-null  float64
     48  2004            182912 non-null  float64
     49  2005            195795 non-null  float64
     50  2006            194394 non-null  float64
     51  2007            198393 non-null  float64
     52  2008            197756 non-null  float64
     53  2009            197733 non-null  float64
     54  2010            213972 non-null  float64
     55  2011            204254 non-null  float64
     56  2012            207054 non-null  float64
     57  2013            202080 non-null  float64
     58  2014            208672 non-null  float64
     59  2015            205706 non-null  float64
     60  2016            204739 non-null  float64
     61  2017            187824 non-null  float64
     62  2018            166196 non-null  float64
     63  2019            84963 non-null   float64
     64  Unnamed: 64     0 non-null       float64
    dtypes: float64(61), object(4)
    memory usage: 187.3+ MB
    

kolom memiliki tipe `object` sementara nilainya memiliki tipe `float64` seperti yang telah diduga. Dengan info, kita juga dapat mengetahui `index` data kita, jikalau kita butuh memanggil-manggil mereka dengan menggunakan index.

Untuk saat ini, saya akan membuang kolom yang tidak perlu, antara lain `'Country Code'`, `'Indicator Code'`, dan semua tahun selain 2017. Sebuah catatan, jika anda sedang melakukan penelitian serius, kode negara dan kode indikator sangatlah penting. Selalu simpan data master yang tidak disentuh sama sekali sebagai *back-up*!!

Kembali ke laptop, kita drop kolom yang tidak perlu untuk latihan:


```python
df=df.drop(columns=['Country Code','Indicator Code']) # menghapus variabel country code dan indicator code
```


```python
# menghapus kolom 1960 - 2016
for i in range(1960,2017):
    a=str(i)
    df=df.drop(columns=a)
```


```python
# menghapus kolom 2018 dan 2019
df=df.drop(columns=['2018','2019','Unnamed: 64'])
df
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
      <th>Country Name</th>
      <th>Indicator Name</th>
      <th>2017</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arab World</td>
      <td>Access to clean fuels and technologies for coo...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arab World</td>
      <td>Access to electricity (% of population)</td>
      <td>90.283638</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arab World</td>
      <td>Access to electricity, rural (% of rural popul...</td>
      <td>81.102134</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arab World</td>
      <td>Access to electricity, urban (% of urban popul...</td>
      <td>97.467915</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arab World</td>
      <td>Account ownership at a financial institution o...</td>
      <td>37.165211</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>377779</th>
      <td>Zimbabwe</td>
      <td>Women who believe a husband is justified in be...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377780</th>
      <td>Zimbabwe</td>
      <td>Women who believe a husband is justified in be...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377781</th>
      <td>Zimbabwe</td>
      <td>Women who were first married by age 15 (% of w...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377782</th>
      <td>Zimbabwe</td>
      <td>Women who were first married by age 18 (% of w...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377783</th>
      <td>Zimbabwe</td>
      <td>Women's share of population ages 15+ living wi...</td>
      <td>59.700000</td>
    </tr>
  </tbody>
</table>
<p>377784 rows × 3 columns</p>
</div>



Kita telah sukses menghapus kolom-kolom yang tidak diperlukan. Data diatas seharusnya memiliki ukuran yang jauh lebih kecil dibandingkan sebelumnya.


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 377784 entries, 0 to 377783
    Data columns (total 3 columns):
     #   Column          Non-Null Count   Dtype  
    ---  ------          --------------   -----  
     0   Country Name    377784 non-null  object 
     1   Indicator Name  377784 non-null  object 
     2   2017            187824 non-null  float64
    dtypes: float64(1), object(2)
    memory usage: 8.6+ MB
    

Dapat anda lihat di atas, sekarang ukuran data kita tinggal sekitar 8,6 MB saja. Jauh dibandingkan sebelumnya ya?

Nah, sekarang kita telah memiliki data yang sifatnya cross section, tapi cross sectionnya masih menurun ke bawah. Yang saya inginkan adalah data yang bentuknya kira-kira seperti ini:

|nama_negara|indikator_1|indikator_2|....|indikator_n|
|-----------|-----------|-----------|----|-----------|
|Afghanistan|angka_1|angka_2|....|angka_n|
|Australia|angka_1|angka_2|....|angka_n|
|....|....|....|....|....|
|Zimbabwe|angka_1|angka_2|....|angka_n|

Beberapa langkah harus kita lakukan

Pertama, anda dapat lihat bahwa observasi paling atas memiliki nama negara "Arab World". Tentu saja ini bukan nama sebuah negara, tapi nama sebuah regional. Jika kita panggil semua nama unik dari nama negara, anda akan mendapati bahwa nama-nama teratas adalah nama regional, bukan nama negara.


```python
df.set_index(['Country Name','Indicator Name']) # set index
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
      <th></th>
      <th>2017</th>
    </tr>
    <tr>
      <th>Country Name</th>
      <th>Indicator Name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Arab World</th>
      <th>Access to clean fuels and technologies for cooking (% of population)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Access to electricity (% of population)</th>
      <td>90.283638</td>
    </tr>
    <tr>
      <th>Access to electricity, rural (% of rural population)</th>
      <td>81.102134</td>
    </tr>
    <tr>
      <th>Access to electricity, urban (% of urban population)</th>
      <td>97.467915</td>
    </tr>
    <tr>
      <th>Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)</th>
      <td>37.165211</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Zimbabwe</th>
      <th>Women who believe a husband is justified in beating his wife when she neglects the children (%)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Women who believe a husband is justified in beating his wife when she refuses sex with him (%)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Women who were first married by age 15 (% of women ages 20-24)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Women who were first married by age 18 (% of women ages 20-24)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Women's share of population ages 15+ living with HIV (%)</th>
      <td>59.700000</td>
    </tr>
  </tbody>
</table>
<p>377784 rows × 1 columns</p>
</div>



Sekarang, data kita sudah dibuat sedemikian sehingga index-nya adalah Country Name dan Indicator Name. Namun 


```python
df['Country Name'].unique()
```




    array(['Arab World', 'Caribbean small states',
           'Central Europe and the Baltics', 'Early-demographic dividend',
           'East Asia & Pacific',
           'East Asia & Pacific (excluding high income)',
           'East Asia & Pacific (IDA & IBRD countries)', 'Euro area',
           'Europe & Central Asia',
           'Europe & Central Asia (excluding high income)',
           'Europe & Central Asia (IDA & IBRD countries)', 'European Union',
           'Fragile and conflict affected situations',
           'Heavily indebted poor countries (HIPC)', 'High income',
           'IBRD only', 'IDA & IBRD total', 'IDA blend', 'IDA only',
           'IDA total', 'Late-demographic dividend',
           'Latin America & Caribbean',
           'Latin America & Caribbean (excluding high income)',
           'Latin America & the Caribbean (IDA & IBRD countries)',
           'Least developed countries: UN classification',
           'Low & middle income', 'Low income', 'Lower middle income',
           'Middle East & North Africa',
           'Middle East & North Africa (excluding high income)',
           'Middle East & North Africa (IDA & IBRD countries)',
           'Middle income', 'North America', 'Not classified', 'OECD members',
           'Other small states', 'Pacific island small states',
           'Post-demographic dividend', 'Pre-demographic dividend',
           'Small states', 'South Asia', 'South Asia (IDA & IBRD)',
           'Sub-Saharan Africa', 'Sub-Saharan Africa (excluding high income)',
           'Sub-Saharan Africa (IDA & IBRD countries)', 'Upper middle income',
           'World', 'Afghanistan', 'Albania', 'Algeria', 'American Samoa',
           'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
           'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The',
           'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
           'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
           'Bosnia and Herzegovina', 'Botswana', 'Brazil',
           'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria',
           'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon',
           'Canada', 'Cayman Islands', 'Central African Republic', 'Chad',
           'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros',
           'Congo, Dem. Rep.', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire",
           'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic',
           'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
           'Egypt, Arab Rep.', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
           'Estonia', 'Eswatini', 'Ethiopia', 'Faroe Islands', 'Fiji',
           'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia, The',
           'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland',
           'Grenada', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau',
           'Guyana', 'Haiti', 'Honduras', 'Hong Kong SAR, China', 'Hungary',
           'Iceland', 'India', 'Indonesia', 'Iran, Islamic Rep.', 'Iraq',
           'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan',
           'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
           'Korea, Dem. People’s Rep.', 'Korea, Rep.', 'Kosovo', 'Kuwait',
           'Kyrgyz Republic', 'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho',
           'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
           'Macao SAR, China', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
           'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius',
           'Mexico', 'Micronesia, Fed. Sts.', 'Moldova', 'Monaco', 'Mongolia',
           'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
           'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
           'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia',
           'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
           'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
           'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania',
           'Russian Federation', 'Rwanda', 'Samoa', 'San Marino',
           'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
           'Seychelles', 'Sierra Leone', 'Singapore',
           'Sint Maarten (Dutch part)', 'Slovak Republic', 'Slovenia',
           'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan',
           'Spain', 'Sri Lanka', 'St. Kitts and Nevis', 'St. Lucia',
           'St. Martin (French part)', 'St. Vincent and the Grenadines',
           'Sudan', 'Suriname', 'Sweden', 'Switzerland',
           'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 'Thailand',
           'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia',
           'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu',
           'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
           'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu',
           'Venezuela, RB', 'Vietnam', 'Virgin Islands (U.S.)',
           'West Bank and Gaza', 'Yemen, Rep.', 'Zambia', 'Zimbabwe'],
          dtype=object)



Nama individu negara baru dimulai setelah "world", tepat di Afghanistan ke bawah. Untuk itu, semua observasi di atas Afghanistan harus kita buang. Pertama cari tau dulu Afghanistan dimulai di observasi nomor berapa.


```python
df['Country Name'][0:67260] # Dapat dimulai dari 0:1000 lalu angka di belakang ditambahkan jika belum ketemu Afghanistan
                            # dikurangi jika sudah kelewatan. 
```




    0         Arab World
    1         Arab World
    2         Arab World
    3         Arab World
    4         Arab World
                ...     
    67255          World
    67256          World
    67257    Afghanistan
    67258    Afghanistan
    67259    Afghanistan
    Name: Country Name, Length: 67260, dtype: object



Dapat dilihat bahwa Afghanistan dimulai di baris ke-67257. Mari kita drop semua baris sebelum 67257.


```python
df=df[67258:377784] # jangan lupa bahwa indexing di python dimulai di 0.
df                  # ngecek data kita setelah dibuang semua non-negara
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
      <th>Country Name</th>
      <th>Indicator Name</th>
      <th>2017</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>67258</th>
      <td>Afghanistan</td>
      <td>Access to electricity (% of population)</td>
      <td>97.700000</td>
    </tr>
    <tr>
      <th>67259</th>
      <td>Afghanistan</td>
      <td>Access to electricity, rural (% of rural popul...</td>
      <td>97.091973</td>
    </tr>
    <tr>
      <th>67260</th>
      <td>Afghanistan</td>
      <td>Access to electricity, urban (% of urban popul...</td>
      <td>99.500000</td>
    </tr>
    <tr>
      <th>67261</th>
      <td>Afghanistan</td>
      <td>Account ownership at a financial institution o...</td>
      <td>14.893312</td>
    </tr>
    <tr>
      <th>67262</th>
      <td>Afghanistan</td>
      <td>Account ownership at a financial institution o...</td>
      <td>7.160685</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>377779</th>
      <td>Zimbabwe</td>
      <td>Women who believe a husband is justified in be...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377780</th>
      <td>Zimbabwe</td>
      <td>Women who believe a husband is justified in be...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377781</th>
      <td>Zimbabwe</td>
      <td>Women who were first married by age 15 (% of w...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377782</th>
      <td>Zimbabwe</td>
      <td>Women who were first married by age 18 (% of w...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377783</th>
      <td>Zimbabwe</td>
      <td>Women's share of population ages 15+ living wi...</td>
      <td>59.700000</td>
    </tr>
  </tbody>
</table>
<p>310526 rows × 3 columns</p>
</div>



Sudah tampak cantik yah. Setelah itu, yang perlu kita lakukan adalah tinggal melakukan unstack data berdasarkan indicator name. kita harus set index terlebih dahulu terhadap dua `object` kita untuk menjadikannya cross section. 


```python
df=df.set_index(['Country Name','Indicator Name']) # set index
df
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
      <th></th>
      <th>2017</th>
    </tr>
    <tr>
      <th>Country Name</th>
      <th>Indicator Name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Afghanistan</th>
      <th>Access to electricity (% of population)</th>
      <td>97.700000</td>
    </tr>
    <tr>
      <th>Access to electricity, rural (% of rural population)</th>
      <td>97.091973</td>
    </tr>
    <tr>
      <th>Access to electricity, urban (% of urban population)</th>
      <td>99.500000</td>
    </tr>
    <tr>
      <th>Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)</th>
      <td>14.893312</td>
    </tr>
    <tr>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, female (% of population ages 15+)</th>
      <td>7.160685</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Zimbabwe</th>
      <th>Women who believe a husband is justified in beating his wife when she neglects the children (%)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Women who believe a husband is justified in beating his wife when she refuses sex with him (%)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Women who were first married by age 15 (% of women ages 20-24)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Women who were first married by age 18 (% of women ages 20-24)</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Women's share of population ages 15+ living with HIV (%)</th>
      <td>59.700000</td>
    </tr>
  </tbody>
</table>
<p>310526 rows × 1 columns</p>
</div>



Nah, sekarang susunannya sudah sesuai dengan index yang kita inginkan. Terakhir, yang kita lakukan adalah `unstack` data berdasarkan nama indikator. Inilah yang agak susah dilakukan pakai sheets. (susah buat saya soalnya saya kurang jago microsoft excel).


```python
latihan=df.unstack(['Indicator Name'])          # mindahin nama indikator sebagai kolom
latihan
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="21" halign="left">2017</th>
    </tr>
    <tr>
      <th>Indicator Name</th>
      <th>ARI treatment (% of children under 5 taken to a health provider)</th>
      <th>Access to clean fuels and technologies for cooking (% of population)</th>
      <th>Access to electricity (% of population)</th>
      <th>Access to electricity, rural (% of rural population)</th>
      <th>Access to electricity, urban (% of urban population)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, female (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, male (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, older adults (% of population ages 25+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, poorest 40% (% of population ages 15+)</th>
      <th>...</th>
      <th>Women participating in the three decisions (own health care, major household purchases, and visiting family) (% of women age 15-49)</th>
      <th>Women who believe a husband is justified in beating his wife (any of five reasons) (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she argues with him (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she burns the food (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she goes out without telling him (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she neglects the children (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she refuses sex with him (%)</th>
      <th>Women who were first married by age 15 (% of women ages 20-24)</th>
      <th>Women who were first married by age 18 (% of women ages 20-24)</th>
      <th>Women's share of population ages 15+ living with HIV (%)</th>
    </tr>
    <tr>
      <th>Country Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>97.700000</td>
      <td>97.091973</td>
      <td>99.500000</td>
      <td>14.893312</td>
      <td>7.160685</td>
      <td>22.536495</td>
      <td>18.016499</td>
      <td>13.802503</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.3</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>40.015171</td>
      <td>38.102959</td>
      <td>42.043503</td>
      <td>42.513248</td>
      <td>22.751028</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>42.776627</td>
      <td>29.268730</td>
      <td>56.254936</td>
      <td>48.747078</td>
      <td>34.970802</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>45.9</td>
    </tr>
    <tr>
      <th>American Samoa</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Virgin Islands (U.S.)</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>West Bank and Gaza</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.700000</td>
      <td>99.070331</td>
      <td>99.900000</td>
      <td>25.022177</td>
      <td>15.910773</td>
      <td>34.436001</td>
      <td>33.076920</td>
      <td>11.981574</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Yemen, Rep.</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>79.200000</td>
      <td>68.766799</td>
      <td>97.735039</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22.8</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.300000</td>
      <td>13.997699</td>
      <td>75.200000</td>
      <td>45.863258</td>
      <td>40.278877</td>
      <td>51.680923</td>
      <td>48.338139</td>
      <td>31.244963</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.3</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.482048</td>
      <td>19.152600</td>
      <td>85.317101</td>
      <td>55.285137</td>
      <td>51.664925</td>
      <td>59.227501</td>
      <td>58.877064</td>
      <td>43.601181</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.7</td>
    </tr>
  </tbody>
</table>
<p>217 rows × 1431 columns</p>
</div>



Masih ada sedikit masalah di data ini, yaitu kita punya 2 headers, yaitu `2017` dan `Indicator Name`. Masalahnya adalah, kita tidak bisa langsung memanggil nama variabelnya. memanggil:
```python
latihan['Access to electricity (% of population)']
```
akan menghasilkan eror. Sementara itu, kita bisa panggil 2017, tapi nama kolom lainnya ikutan terpanggil. Coba kode ini:
```python
latihan['2017']
```

Cara yang terbaik adalah memanggil keduanya, di mana 2017 adalah nama kolom pertama, diikuti nama kolom yang kita inginkan.


```python
latihan['2017']['Access to electricity (% of population)']
```




    Country Name
    Afghanistan               97.700000
    Albania                  100.000000
    Algeria                  100.000000
    American Samoa                  NaN
    Andorra                  100.000000
                                ...    
    Virgin Islands (U.S.)    100.000000
    West Bank and Gaza        99.700000
    Yemen, Rep.               79.200000
    Zambia                    40.300000
    Zimbabwe                  40.482048
    Name: Access to electricity (% of population), Length: 217, dtype: float64



Jadi kita perlu membuang row paling atas yang berisi 2017. kita gunakan [fungsi](https://stackoverflow.com/questions/36529636/delete-second-row-of-header-in-pandas) `droplevel`


```python
latihan.columns=latihan.columns.droplevel(0)
latihan
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
      <th>Indicator Name</th>
      <th>ARI treatment (% of children under 5 taken to a health provider)</th>
      <th>Access to clean fuels and technologies for cooking (% of population)</th>
      <th>Access to electricity (% of population)</th>
      <th>Access to electricity, rural (% of rural population)</th>
      <th>Access to electricity, urban (% of urban population)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, female (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, male (% of population ages 15+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, older adults (% of population ages 25+)</th>
      <th>Account ownership at a financial institution or with a mobile-money-service provider, poorest 40% (% of population ages 15+)</th>
      <th>...</th>
      <th>Women participating in the three decisions (own health care, major household purchases, and visiting family) (% of women age 15-49)</th>
      <th>Women who believe a husband is justified in beating his wife (any of five reasons) (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she argues with him (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she burns the food (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she goes out without telling him (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she neglects the children (%)</th>
      <th>Women who believe a husband is justified in beating his wife when she refuses sex with him (%)</th>
      <th>Women who were first married by age 15 (% of women ages 20-24)</th>
      <th>Women who were first married by age 18 (% of women ages 20-24)</th>
      <th>Women's share of population ages 15+ living with HIV (%)</th>
    </tr>
    <tr>
      <th>Country Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>97.700000</td>
      <td>97.091973</td>
      <td>99.500000</td>
      <td>14.893312</td>
      <td>7.160685</td>
      <td>22.536495</td>
      <td>18.016499</td>
      <td>13.802503</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>29.3</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>40.015171</td>
      <td>38.102959</td>
      <td>42.043503</td>
      <td>42.513248</td>
      <td>22.751028</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>42.776627</td>
      <td>29.268730</td>
      <td>56.254936</td>
      <td>48.747078</td>
      <td>34.970802</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>45.9</td>
    </tr>
    <tr>
      <th>American Samoa</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Virgin Islands (U.S.)</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>West Bank and Gaza</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.700000</td>
      <td>99.070331</td>
      <td>99.900000</td>
      <td>25.022177</td>
      <td>15.910773</td>
      <td>34.436001</td>
      <td>33.076920</td>
      <td>11.981574</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Yemen, Rep.</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>79.200000</td>
      <td>68.766799</td>
      <td>97.735039</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22.8</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.300000</td>
      <td>13.997699</td>
      <td>75.200000</td>
      <td>45.863258</td>
      <td>40.278877</td>
      <td>51.680923</td>
      <td>48.338139</td>
      <td>31.244963</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.3</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>40.482048</td>
      <td>19.152600</td>
      <td>85.317101</td>
      <td>55.285137</td>
      <td>51.664925</td>
      <td>59.227501</td>
      <td>58.877064</td>
      <td>43.601181</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.7</td>
    </tr>
  </tbody>
</table>
<p>217 rows × 1431 columns</p>
</div>



mari kita coba panggil kolom `latihan['Access to electricity (% of population)']`


```python
latihan['Access to electricity (% of population)']
```




    Country Name
    Afghanistan               97.700000
    Albania                  100.000000
    Algeria                  100.000000
    American Samoa                  NaN
    Andorra                  100.000000
                                ...    
    Virgin Islands (U.S.)    100.000000
    West Bank and Gaza        99.700000
    Yemen, Rep.               79.200000
    Zambia                    40.300000
    Zimbabwe                  40.482048
    Name: Access to electricity (% of population), Length: 217, dtype: float64



Yup! Sudah bisa. Tidak eror lagi. Nanti, di proyek kalian, tentu akan males menulis berkali-kali nulis `latihan['Access to electricity (% of population)']` karena kepanjangan. Nanti anda bisa menamakan kembali kolom tersebut dengan nama yang lebih pendek dan gampang diambil. Tentu saja untuk proyek anda nanti, anda nggak harus memakai semua kolom yang ada di dataset ini. Itu dipikirkan nanti saja yah!

Terakhir, yang perlu kita lakukan adalah mengexport si `latihan` ke bentuk sheets supaya enak dilihat. Selalu gunakan ekstensi `.csv` yah! 


```python
latihan.to_csv("latihan.csv")
```


    ---------------------------------------------------------------------------

    PermissionError                           Traceback (most recent call last)

    <ipython-input-31-50df1f6bddd1> in <module>
    ----> 1 latihan.to_csv("latihan.csv")
    

    C:\Users\DELL\Anaconda3\lib\site-packages\pandas\core\generic.py in to_csv(self, path_or_buf, sep, na_rep, float_format, columns, header, index, index_label, mode, encoding, compression, quoting, quotechar, line_terminator, chunksize, date_format, doublequote, escapechar, decimal, errors)
       3165             decimal=decimal,
       3166         )
    -> 3167         formatter.save()
       3168 
       3169         if path_or_buf is None:
    

    C:\Users\DELL\Anaconda3\lib\site-packages\pandas\io\formats\csvs.py in save(self)
        188                 encoding=self.encoding,
        189                 errors=self.errors,
    --> 190                 compression=dict(self.compression_args, method=self.compression),
        191             )
        192             close = True
    

    C:\Users\DELL\Anaconda3\lib\site-packages\pandas\io\common.py in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors)
        491         if encoding:
        492             # Encoding
    --> 493             f = open(path_or_buf, mode, encoding=encoding, errors=errors, newline="")
        494         elif is_text:
        495             # No explicit encoding
    

    PermissionError: [Errno 13] Permission denied: 'latihan.csv'


Seperti yang anda lihat, sebenarnya agak ribet ngutik-ngutik data dengan `Pandas`, apalagi jika anda paham menggunakan pivot table di excel atau google sheet. Salah satu cara terbaik ya tentu saja mengutik-utik datanya di excel atau google sheet, lalu di-save as dengan extensi `csv` sebelum dibaca di python. Tidak ada masalah. *Whatever works for you!*
