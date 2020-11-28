---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Statistik ekspor impor Indonesia di 2018 dengan negara-negara RCEP"
subtitle: ""
summary: ""
authors: [admin]
tags: [python, perdagangan, rcep]
categories: [python, perdagangan, rcep]
date: 2020-11-28T13:39:10+11:00
lastmod: 2020-11-28T13:39:10+11:00
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

Sedikit statistik tentang RCEP. Untuk menghubung-hubungkan dengan [Global Value Chain](https://theconversation.com/kebijakan-untuk-meningkatkan-partisipasi-perusahaan-perusahaan-indonesia-dalam-rantai-pasok-global-150062), saya akan menggunakna klasifikasi Stage of Production (SoP) dari UNCTAD. Klasifikasinya antara lain:


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
      <th>productcode</th>
      <th>isgroup</th>
      <th>nomenclaturecode</th>
      <th>grouptype</th>
      <th>productdescription</th>
      <th>notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>27</th>
      <td>UNCTAD-SoP1</td>
      <td>Yes</td>
      <td>H0</td>
      <td>Stages-Of-Processing</td>
      <td>Raw materials</td>
      <td></td>
    </tr>
    <tr>
      <th>28</th>
      <td>UNCTAD-SoP2</td>
      <td>Yes</td>
      <td>H0</td>
      <td>Stages-Of-Processing</td>
      <td>Intermediate goods</td>
      <td></td>
    </tr>
    <tr>
      <th>29</th>
      <td>UNCTAD-SoP3</td>
      <td>Yes</td>
      <td>H0</td>
      <td>Stages-Of-Processing</td>
      <td>Consumer goods</td>
      <td></td>
    </tr>
    <tr>
      <th>30</th>
      <td>UNCTAD-SoP4</td>
      <td>Yes</td>
      <td>H0</td>
      <td>Stages-Of-Processing</td>
      <td>Capital goods</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




Statistiknya sebagai berikut:





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
      <th>Trade Value</th>
      <th>All goods</th>
      <th>Raw materials</th>
      <th>intermediate goods</th>
      <th>Consumption goods</th>
      <th>Capital Goods</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>export RCEP</td>
      <td>$101,578,213.46</td>
      <td>$29,583,083.81</td>
      <td>$28,876,371.04</td>
      <td>$32,692,137.50</td>
      <td>$10,003,962.16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>export World</td>
      <td>$180,215,034.44</td>
      <td>$45,863,376.29</td>
      <td>$49,419,462.61</td>
      <td>$68,578,923.17</td>
      <td>$15,547,001.92</td>
    </tr>
    <tr>
      <th>2</th>
      <td>import RCEP</td>
      <td>$125,215,957.00</td>
      <td>$7,859,326.12</td>
      <td>$40,495,720.49</td>
      <td>$33,166,747.09</td>
      <td>$42,937,992.48</td>
    </tr>
    <tr>
      <th>3</th>
      <td>import World</td>
      <td>$188,711,171.62</td>
      <td>$24,893,192.22</td>
      <td>$61,575,534.29</td>
      <td>$44,976,972.35</td>
      <td>$56,497,488.96</td>
    </tr>
  </tbody>
</table>
</div>



Saya membandingkan juga dengan total perdagangan Indonesia dengan dunia. Ada RCEP countries di `World` jadi tentu saja angka-angkanya lebih banyak. Jadi `World`-nya tidak saya kurangkan dengan `RCEP`. `World` itu total ekspor impor Indonesia. Oh ya, data-data ini berdasarkan statistik perdagangan tahun 2018 yang dikumpulkan oleh World Bank.

Sepertinya saya sudah pernah menulis pentingnya peran impor bagi produksi Indonesia karena [sebagian besar impor Indonesia adalah produk-produk penunjuang produksi](https://krisna.netlify.app/post/imporinput/). Hal ini terefleksi juga di perdagangan Indonesia di tahun 2018 ini, di mana `Consumption goods` hanya sekitar 23% dari total Impor Indonesia, yaitu


```python
print(str(df2.loc[3,'Consumption goods']/df2.loc[3,'All goods']*100)+' %')
```

    23.83376244573637 %
    

yang sebenernya agak penurunan.

Sedangkan untuk ekspor, klasifikasi yang paling tinggi adalah barang konsumsi. Kita impor barang kebutuhan industri, dan mengekspor barang konsumsi. Sesuatu yang sebenarnya baik dan menghadirkan nilai tambah. Jadi agak aneh sebenarnya kalau pemerintah begitu anti dengan impor, karena tanpa impor, agak sulit untuk mempertahankan performa ekspor kita.

Tapi tentu saja dalam konteks RCEP, yang paling penting adalah seberapa penting ekonomi negara-negara RCEP bagi Indonesia, bik secara ekspor maupun impor. Hal ini dapat terefleksikan dari tabel di bawah ini.




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
      <th>importance</th>
      <th>All goods</th>
      <th>Raw materials</th>
      <th>intermediate goods</th>
      <th>Consumption goods</th>
      <th>Capital Goods</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>export</td>
      <td>0.563650</td>
      <td>0.645026</td>
      <td>0.584312</td>
      <td>0.476708</td>
      <td>0.643466</td>
    </tr>
    <tr>
      <th>1</th>
      <td>import</td>
      <td>0.663532</td>
      <td>0.315722</td>
      <td>0.657659</td>
      <td>0.737416</td>
      <td>0.759998</td>
    </tr>
  </tbody>
</table>
</div>



Dapat dilihat bahwa hubungan Indonesia terhadap negara-negara RCEP begitu erat, bahkan sebelum RCEP diberlakukan. Hal ini utamanya adalah di impor. Indonesia mengimpor sangat banyak barang konsumsi dan kapital dari negara-negara RCEP. Untuk Raw materials, sepertinya wajar ya karena barang-barang agrikultur seperti kedelai, gula, dan gandum diimpor dari negara-negara maju. Sementara itu untuk ekspor, peran RCEP agak lebih lemah, terutama untuk produk konsumsi. Produk konsumsi memang banyak lari ke negara maju, yang duitnya juga lebih banyak. Inilah pentingnya [GSP Indonesia diperpanjang](https://theconversation.com/mengapa-perpanjangan-gsp-dari-amerika-serikat-penting-untuk-ekonomi-indonesia-150481) oleh Amerika Serikat.

Sekian postingan kali ini. Cuma mau update sedikit statistik tentang RCEP. Kalo soal bagus dan jeleknya sepertinya sudah banyak yang update. bye.
