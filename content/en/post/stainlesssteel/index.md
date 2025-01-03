---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Nickel ore export ban and the export performance of the downstream industries"
subtitle: ""
summary: ""
authors: [admin]
tags: [ekonomi, perdagangan, industri]
categories: [ekonomi, perdagangan, industri]
date: 2022-01-12T23:50:30+07:00
lastmod: 2022-01-12T23:50:30+07:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "https://unsplash.com/photos/SLIFI67jv5k?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink"
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

This post is inspired by this tweet (in Indonesian).

<blockquote class="twitter-tweet"><p lang="in" dir="ltr">Baru nyadar dampak pelarangan bijih nikel ternyata *sebesar* itu. Indonesia sekarang jadi eksportir stainless steel terbesar dunia, salah satu produk turunan feronikel.<a href="https://t.co/qonkL4o33d">https://t.co/qonkL4o33d</a></p>&mdash; Faris Abdurrachman (@faris_sina) <a href="https://twitter.com/faris_sina/status/1480903046397714432?ref_src=twsrc%5Etfw">January 11, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

That tweet's quoting [artikel dari investor.id](https://investor.id/business/276165/indonesia-eksportir-stainless-steel-terbesar-dunia) basically sez that Indonesia has now become the top global export of stainless steel. The export value is 1,6 billion USD. Amazing stuff!

Moreover, that article mentioned the cause. It is the nickel ore export ban. Indeed, nickel is one of the most important component in the production of stainless steel. In fact, most of exported nickel is used by the steel industry.

Let's check out the data.

## Ekspor Stainless Steel

As usual, my go to trade database is the [UN COMTRADE](https://comtrade.un.org/data/). The HS-Code is guessed. Lol

```python
wew=pd.read_csv('stainlesssteel.csv')
wew.query('Year == 2020 & `Commodity Code`>7200')
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
      <th>Year</th>
      <th>Commodity Code</th>
      <th>Commodity</th>
      <th>Netweight (kg)</th>
      <th>Trade Value (US$)</th>
      <th>USD/ton</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>2020</td>
      <td>720260</td>
      <td>Ferro-alloys; ferro-nickel</td>
      <td>2874022704</td>
      <td>4739112331</td>
      <td>1648.947423</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2020</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>1087854208</td>
      <td>1630911693</td>
      <td>1499.200611</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2020</td>
      <td>7219</td>
      <td>Stainless steel; flat-rolled products of width...</td>
      <td>1801937373</td>
      <td>2993037641</td>
      <td>1661.010913</td>
    </tr>
  </tbody>
</table>
</div>



1.6 billion USD indeed! Let's plot its time series.

```python
sns.lineplot(data=wew.query('`Commodity Code` == 7218'),x="Year",y="Trade Value (US$)",color="green")
sns.lineplot(data=wew.query('`Commodity Code` == 7219'),x="Year",y="Trade Value (US$)",color="orange")
sns.lineplot(data=wew.query('`Commodity Code` == 720260'),x="Year",y="Trade Value (US$)",color="magenta")
plt.legend(labels=['7218','7219','ferro-nickel'])
```




    <matplotlib.legend.Legend at 0x220e4898ca0>




    
![png](./index_3_1.png)
    


Whoa seems so clear as day that the two goods' export skyrocketed in 2016. 

```python
wew.query('(Year == 2016 | Year == 2020) & `Commodity Code`>7200')
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
      <th>Year</th>
      <th>Commodity Code</th>
      <th>Commodity</th>
      <th>Netweight (kg)</th>
      <th>Trade Value (US$)</th>
      <th>USD/ton</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>2020</td>
      <td>720260</td>
      <td>Ferro-alloys; ferro-nickel</td>
      <td>2874022704</td>
      <td>4739112331</td>
      <td>1648.947423</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2020</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>1087854208</td>
      <td>1630911693</td>
      <td>1499.200611</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2020</td>
      <td>7219</td>
      <td>Stainless steel; flat-rolled products of width...</td>
      <td>1801937373</td>
      <td>2993037641</td>
      <td>1661.010913</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>720260</td>
      <td>Ferro-alloys; ferro-nickel</td>
      <td>411438077</td>
      <td>571298623</td>
      <td>1388.540961</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>24614238</td>
      <td>30434580</td>
      <td>1236.462408</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2016</td>
      <td>7219</td>
      <td>Stainless steel; flat-rolled products of width...</td>
      <td>49912515</td>
      <td>74135846</td>
      <td>1485.315777</td>
    </tr>
  </tbody>
</table>
</div>




## Berkat Ekspor Nikel?

Salah satu hal yang menjadi penunjang kenaikan ekspor stainless steel tersebut adalah, katanya, adalah pelarangan ekspor nikel. Nikel adalah barang mentah. Adalah keinginan Pemerintah Indonesia untuk menghasilkan nilai tambah di dalam negeri. Daripada ekspor nikel mentah lalu negara lain yang menikmati jualan baja, kenapa tidak kita saja yang bikin baja? Berdasarkan logika tersebut, maka dilaranglah ekspor nikel agar penghasil baja Indonesia dapat meningkatkan produksinya dan menghasilkan nilai tambah ekstra di dalam negeri. Secara natural, pertanyaan berikutnya adalah berapakah nilai ekspor nikel yang turun? Apakah sebanding dengan naiknya ekspor baja?

Lagi-lagi untuk menjawabnya, saya menggantungkan diri pada data dari UNCOMTRADE dan juga tebak-tebakan kode HS. Menurut penerawangan saya, Nikel adalah barang yang dikasih kode HS 2604 yaitu *nickel ores and concentrates*. Langsung saja kita coba ilustrasikan dengan grafik. 

```python
sns.lineplot(data=wew.query('`Commodity Code` == 2604'),x="Year",y="Trade Value (US$)")
plt.axhline(color='grey')
```




    <matplotlib.lines.Line2D at 0x220e495deb0>




    
![png](./index_7_1.png)
    


*Trade value* nikel naik secara signifikan sejak commodity boom dimulai sekitar 2005an, dan sempat berkurang saat krisis global 2008. Kemudan, nilai ekspor dari nikel mendadak mendekati nol pada tahun 2014 dan baru naik lagi menjelas 2017-an. Sebenarnya larangan ekspor ini sudah pernah diberlakukan pada tahun 2014, namun pada 2017 dibolehkan lagi. Kita bisa lihat kenaikan kapasitas ekspor yang luar biasa mendekati larangan ekspor tersebut. Sekali lagi ketika dilarang lagi di 2020, para produsen meningkatkan ekspor besar-besaran pada 2019-nya.

Kalau dilihat dari grafik nikel dan stainless steel, sepertinya emang kelihatan ya dampak dari pelarangan ekspor bijih nikel. Ekspor produk turunannya langsung meningkat pesat. Apalagi memang saat ini [sebagian besar nikel dunia](https://nickelinstitute.org/about-nickel-and-its-applications/stainless-steel/) digunakan untuk produksi stainless steel. Apalagi, kenaikan nilai ekspor 3 produk nikel di atas jauh melebihi kehilangan nilai ekspor nikel akibat larangan ekspor. Nilai ekspor bijih nikel saat lagi di puncak paling sekitar 1,7 milyar Dolar AS. angka ini jauh lebih kecil daripada naiknya nilai ekspor tiga produk stainless steel di atas sejak 2016. Dilihat dari data ini, sepertinya memang penambahan nilai tambah di dalam negeri telah berhasil dilakukan.

## Produksi yang berpindah

 Larangan ekspor Indonesia tentunya membuat produsen stainless steel di negara lain kesulitan. Indonesia adalah pemasok bijih nikel terbesar dunia. Tentunya larangan ekspor nikel oleh Indonesia akan memiliki dampak yang besar terhadap pasar global nikel. Mungkin ada 2 cara mainstream menghadapi larangan ekspor nikel Indonesia. Pertama adalah protes baik secara langsung maupun lewat World Trade Organization (WTO), seperti yang [dilakukan oleh Uni Eropa](https://trade.ec.europa.eu/doclib/press/index.cfm?id=2235). Tapi cara ini kurang efektif, pertama selain karena rentan untuk dicuekin, protes ke WTO bisa makan waktu bertahun-tahun. 
 
 Cara kedua adalah dengan memindahkan pabrik ke Indonesia sekalian, beli nikelnya secara domestik, dan mengekspor stainless steelnya balik ke negara masing-masing. Inilah yang [dilakukan oleh Republik Rakyat Tiongkok (RRT)](https://www.woodmac.com/press-releases/tsingshan-indonesia-shakes-up-stainless-steel-markets-in-south-east-asia/). Bahkan Taiwan pun memutuskan untuk mengurangi produksi stainless steel mereka dan membelinya dari Indonesia. 

 Hal ini membuat saya kepingin ngelihat peta ekspor stainless steel dunia, yang lagi-lagi bisa kita dapat dari UNCOMTRADE. Saya akan coba lihat beberapa negara yang katanya big player di stainless steel. Saya coba masukin Amerika Serikat, Inggris, Uni Eropa (termasuk inggris wkkw), Indonesia, China, India dan Swedia. Saya cuma pake stainless steel yang 7218 yak karena ini yang jadi pemantik di twit di atas.

```python
waks=pd.read_csv('stainlesssteel2.csv').sort_values(by=['Year','Trade Value (US$)'])
pd.set_option('display.max_rows', None)
b=[]
ctr=('IDN','GBR','EU2','CHN','IND','SWE')
for i in ctr:
    bmii=waks.loc[(waks['Reporter ISO'] == i)]
    b.append(bmii)
b=pd.concat(b)
b.query('Year == 2020')
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
      <th>Year</th>
      <th>Reporter</th>
      <th>Reporter ISO</th>
      <th>Commodity Code</th>
      <th>Commodity</th>
      <th>Netweight (kg)</th>
      <th>Trade Value (US$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>642</th>
      <td>2020</td>
      <td>Indonesia</td>
      <td>IDN</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>1.087854e+09</td>
      <td>1630911693</td>
    </tr>
    <tr>
      <th>897</th>
      <td>2020</td>
      <td>United Kingdom</td>
      <td>GBR</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>1.408406e+08</td>
      <td>326187431</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020</td>
      <td>EU-28</td>
      <td>EU2</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>4.993958e+07</td>
      <td>179001341</td>
    </tr>
    <tr>
      <th>550</th>
      <td>2020</td>
      <td>China</td>
      <td>CHN</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>2.600670e+05</td>
      <td>1247579</td>
    </tr>
    <tr>
      <th>819</th>
      <td>2020</td>
      <td>India</td>
      <td>IND</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>6.883925e+06</td>
      <td>14563591</td>
    </tr>
    <tr>
      <th>683</th>
      <td>2020</td>
      <td>Rep. of Korea</td>
      <td>KOR</td>
      <td>7218</td>
      <td>Stainless steel in ingots or other primary for...</td>
      <td>2.022914e+06</td>
      <td>2851620</td>
    </tr>
  </tbody>
</table>
</div>



```python
fig, ax =plt.subplots(1,2,figsize=(15,7))
sns.lineplot(data=b,x="Year",y="Trade Value (US$)",hue="Reporter", ax=ax[0])
sns.lineplot(data=b,x="Year",y="Netweight (kg)",hue="Reporter", ax=ax[1])
```




    <AxesSubplot:xlabel='Year', ylabel='Netweight (kg)'>




    
![png](./index_10_1.png)
    


Gambar di atas, sebelah kiri adalah dalam Dolar Amerika sementara sebelah kanan dalam kilogram. Nilai ekspor ngedrop pada 2016 kayaknya gara-gara Presiden AS memberlakukan tariff terhadap baja. Tapi sekotar 2017 Uni Eropa berhasil nego dikit. Tapi jelas kelihatan bahwa seiring kenaikan ekspor Indonesia, ekspor negara lain menurun, terutama negara-negara barat. India dan RRT merupakan produsen, namun mereka menggunakan sebagian besar produknya untuk kepentingan domestik sehingga ekspornya kurang banyak. 

Kalo RRT wajar sih, karena memang perusahaan China lah yang pindah ke Indonesia. Jadi sebenernya produsennya dia lagi dia lagi tapi pindah lokasi aja ke Indonesia. [India](https://economictimes.indiatimes.com/industry/indl-goods/svs/steel/import-of-stainless-steel-from-indonesia-grows-nearly-nine-times/articleshow/67852205.cms?from=mdr) dan Uni Eropa sama-sama lagi mengatur strategi bagaimana mengurangi impor dari Indonesia, sementara Taiwan memilih untuk mengikuti arus dan beli aja dari Indonesia daripada proteksi. Sementara itu, Produsen di Korea Selatan memilih untuk mengubah jenis baja yang mereka produksi, mengurangi stainless steel grade rendah dan meningkatkan produksi stainless steel yang lebih tinggi.

Kalau lihat strateginya korsel, berarti sepertinya stainless steel sendiri memiliki banyak grade meski ada di HS-Code yang sama. Berhubung saya sendiri bukan pemerhati nikel dan stainless steel yang berdedikasi, saya ga punya cukup info untuk menggali hal ini. Tapi kita dapat kira-kira kualitas stainless steelnya dari harga. Kita asumsikan aja kalo harganya mahal berarti stainless steelnya lebih bagus. BTW Korsel ga saya masukin karena produksi mereka juga kebanyakan dipakai sendiri jadi ekspornya dikit.

Harga juga kayaknya macem-macem ya, tapi kita proksi aja pakai $\frac{\text{Nilai Ekspor}}{\text{Berat}}$

```python
b['price']=b['Trade Value (US$)']/b['Netweight (kg)']
sns.lineplot(data=b,x="Year",y="price",hue="Reporter")
plt.legend(bbox_to_anchor=(1,0.5))
```




    <matplotlib.legend.Legend at 0x220e47ede50>




    
![png](./index_12_1.png)
    


Daaan memang Stainless Steel Indonesia bisa dibilang yang paling murah diantara negara-negara di atas. Tentunya kita harus berhati-hati menggunakan harga ini ya. Kalau produknya sama, berarti Indonesia justru hebat karena bisa produksi dengan harga miring. Tapi wajar sih ya yang lain kan harus akses Nikel yang harga internasionalnya mahal, sementara produsen di Indonesia pakai produk sendiri yang ekspornya dilarang, jadi harga bahan baku bisa ditekan. Di samping itu, bisa saja di negara yang lebih maju, *concern* tentang emisi mengakibatkan biaya produksi yang lebih tinggi daripada negara yang tidak terlalu mengutamakan isu lingkungan.

Yaudah sih sekian dulu postingan hari ini. Masih banyak info yang perlu digali, tapi bisa jadi ini adalah contoh sukses penggunaan larangan ekspor untuk menarik investasi asing dan tenaga kerja untuk meningkatkan nilai tambah di dalam negeri. Gimana menurut anda? Apakah ini adalah hal yang baik? Mensen saya di [@twitter](https://twitter.com/imedkrisna) ya buat berdiskusi!