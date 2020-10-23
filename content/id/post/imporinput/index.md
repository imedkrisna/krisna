---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Melihat neraca pembayaran dan neraca perdagangan Indonesia menggunakan data World Bank dengan Python"
subtitle: ""
summary: ""
authors: [admin]
tags: [python, ekonomi]
categories: [python, ekonomi]
date: 2020-10-21T21:07:25+11:00
lastmod: 2020-10-21T21:07:25+11:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "neraca pembayaran Indonesia"
  focal_point: "smart"
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

Pasar financial Indonesia sering dikatakan masih dangkal dan sederhana. Perbankan masih memainkan peranan yang sangat penting dan proporsi *consumer banking*-nya masih tinggi. Karena itu, peran investasi asing menjadi semakin penting bagi program-program Pemerintah Indonesia. Pembangunan infrastruktur dan penyamaan harga bensin dibiayai dengan utang BUMN. Pemerintah juga sering menyampaikan pentingnya Penanaman Modal Asing (PMA) untuk meningkatkan lapangan kerja dan pertumbuhan ekonomi. Peningkatan investasi asing tentu saja akan memberi tekanan ke neraca pembayaran.

Menariknya, mengurangi defisit neraca pembayaran juga adalah program pemerintah. Menjaga neraca pembayaran mungkin penting untuk menjaga stabilitas, tapi dapat mengekang pertumbuhan ekonomi. Di blog ini, saya mencoba melihat neraca pembayaran Indonesia. Visualisasi di blog ini akan menggunakan seaborn dan [World Bank's API manager](https://github.com/OliverSherouse/wbdata), `wbdata`. Saya belajar dari [Abdul Baqi's blog](http://abdulbaqi.io/2017/09/13/Wdi/) dan World Bank's [blog](https://blogs.worldbank.org/opendata/accessing-world-bank-data-apis-python-r-ruby-stata) dan [documentation](https://wbdata.readthedocs.io/en/stable/).

## Menggunakan wbdata

Install dengan:

```
pip install -U wbdata
```

Jangan lupa diimpor, dan mengecek isi databases di World Bank databank:


```python
import wbdata as wb

wb.get_source()
```




      id  name
    ----  --------------------------------------------------------------------
       1  Doing Business
       2  World Development Indicators
       3  Worldwide Governance Indicators
       5  Subnational Malnutrition Database
       6  International Debt Statistics
      11  Africa Development Indicators
      12  Education Statistics
      13  Enterprise Surveys
      14  Gender Statistics
      15  Global Economic Monitor
      16  Health Nutrition and Population Statistics
      18  IDA Results Measurement System
      19  Millennium Development Goals
      20  Quarterly Public Sector Debt
      22  Quarterly External Debt Statistics SDDS
      23  Quarterly External Debt Statistics GDDS
      24  Poverty and Equity
      25  Jobs
      27  Global Economic Prospects
      28  Global Financial Inclusion
      29  The Atlas of Social Protection: Indicators of Resilience and Equity
      30  Exporter Dynamics Database – Indicators at Country-Year Level
      31  Country Policy and Institutional Assessment
      32  Global Financial Development
      33  G20 Financial Inclusion Indicators
      34  Global Partnership for Education
      35  Sustainable Energy for All
      36  Statistical Capacity Indicators
      37  LAC Equity Lab
      38  Subnational Poverty
      39  Health Nutrition and Population Statistics by Wealth Quintile
      40  Population estimates and projections
      41  Country Partnership Strategy for India (FY2013 - 17)
      43  Adjusted Net Savings
      44  Readiness for Investment in Sustainable Energy
      45  Indonesia Database for Policy and Economic Research
      46  Sustainable Development Goals
      50  Subnational Population
      54  Joint External Debt Hub
      57  WDI Database Archives
      58  Universal Health Coverage
      59  Wealth Accounts
      60  Economic Fitness
      61  PPPs Regulatory Quality
      62  International Comparison Program (ICP) 2011
      63  Human Capital Index
      64  Worldwide Bureaucracy Indicators
      65  Health Equity and Financial Protection Indicators
      66  Logistics Performance Index
      67  PEFA 2011
      68  PEFA 2016
      69  Global Financial Inclusion and Consumer Protection Survey
      70  Economic Fitness 2
      71  International Comparison Program (ICP) 2005
      72  PEFA_Test
      73  Global Financial Inclusion and Consumer Protection Survey (Internal)
      75  Environment, Social and Governance (ESG) Data
      76  Remittance Prices Worldwide (Sending Countries)
      77  Remittance Prices Worldwide (Receiving Countries)
      78  ICP 2017
      79  PEFA_GRPFM
      80  Gender Disaggregated Labor Database (GDLD)
      81  International Debt Statistics: DSSI



Ada banyak ya, Tapi kita cuma butuh World Development Indicators (WDI), yaitu nomer 2 di list di atas. Sekarang, coba kita cari neraca pembayaran di database tersebut:


```python
wb.search_indicators('current account balance',source=2)
```




    id                 name
    -----------------  ------------------------------------------
    BN.CAB.XOKA.CD     Current account balance (BoP, current US$)
    BN.CAB.XOKA.GD.ZS  Current account balance (% of GDP)



Saya akan pakai yang proporsional dengan PDB. Saya akan tarik data dari World Bank hanya untuk Indonesia di tahun 1981 sampai 2019. Jangan lupa untuk membuat tuple untuk membatasi tahun yang kita sedot.


```python
import pandas as pd
import datetime
tanggal=(datetime.datetime(1981,1,1), datetime.datetime(2019,1,1))
a=wb.get_dataframe({"BN.CAB.XOKA.GD.zS" : "Current account balance (% of GDP)"}, country=["IDN"], data_date=tanggal, convert_date=True, keep_levels=True)
a=a.reset_index()
a.head()
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
      <th>country</th>
      <th>date</th>
      <th>Current account balance (% of GDP)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Indonesia</td>
      <td>2019-01-01</td>
      <td>-2.714101</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Indonesia</td>
      <td>2018-01-01</td>
      <td>-2.939161</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Indonesia</td>
      <td>2017-01-01</td>
      <td>-1.594657</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Indonesia</td>
      <td>2016-01-01</td>
      <td>-1.819151</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Indonesia</td>
      <td>2015-01-01</td>
      <td>-2.035042</td>
    </tr>
  </tbody>
</table>
</div>



Let's visualize it with seaborn


```python
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
plt.figure(figsize=(13.5,8))
graph1=sns.lineplot(x="date", y="Current account balance (% of GDP)",data=a)
graph1.axhline(0, color='black')
graph1.axvline(datetime.datetime(1998,1,1), color='red')
graph1.text(datetime.datetime(1999,1,1),-6, "Asian Financial Crisis",color='red',size='x-large')
plt.show()
```


![png](./featured.png)


Grafik di atas menampilkan current account Indonesia. Indonesia mengalami defisit current account (CAD) sejak jatuhnya harga minyak dunia di awal tahun 1980-an. Pemerintah berusaha menarik investasi asing dengan liberalisasi financial di tahun ini untuk diversifikasi ekonomi dari minyak. Defisit ini terus terjadi sampai krisis finansial di 1998. Memang meningkatkan dana asing di neraca dapat meningkatkan risiko apabila pinjaman tersebut tidak digunakan dengan efisien. Investasi yang tidak produktif tidak menghasilkan lapangan kerja dan pertumbuhan ekonomi yang berkelanjutan. Bayangkan jika anda ngutang untuk beli *handphone* bukannya bikin pabrik. Atau kalau bikin pabrik, pengelolaannya jelek sehingga rugi terus. Fenomena ini mungkin yang menyebabkan kita sangat anti terhadap defisit current account: krisis 98 masih menghantui para pembuat kebijakan.

Sejak krisis, current account Indonesia selalu positif. Namun pada 2011, defisit kembali terjadi sampai hari ini. Sentimen anti-impor pun kembali, dan Pemerintah Indonesia bereaksi dengan meningkatkan Non-Tariff Measures (NTMs). Menurut publikasi [ERIA](https://www.eria.org/uploads/media/10.ERIA_Book_2019_NTM_Update_Chapter_3.pdf), NTMs bertambah banyak hampir 30% di antara 2015 sampai 2018.

## Apa penyebab CAD?

Lucunya, neraca perdagangan (export - import) Indonesia biasanya positif. Penyebab defisit ternyata adalah dari negative net primary income. Ini adalah akun yang berisi (*mostly*) pembayaran bunga utang ke luar negeri. Dengan kata lain, investasi yang masuk selama ini sebagian besar digunakan untuk membayar bunga utang sebelumnya, bukan untuk meningkatkan impor. Hal ini tidak masalah jika Indonesia dapat bertumbuh dengan cepat, dengan *rate* lebih tinggi daripada bunga utang. Sayangnya, Ekonom Faisal Basri berulang kali mengatakan bahwa investasi Indonesia tidak produktif dan tidak efisien.

Artinya, perdagangan seharusnya bukan problem di sini. Tapi bisa saja kita *offset* dengan meningkatkan expor atau menurunkan impor.


```python
b=wb.get_dataframe({"BN.GSR.FCTY.CD" : "Net Primary Account (Current USD)"}, country=["IDN"], data_date=tanggal, convert_date=True, keep_levels=True)
b=b.reset_index()
b.head()
c=wb.get_dataframe({"BN.GSR.MRCH.CD" : "Net Trade in goods (Current USD)"}, country=["IDN"], data_date=tanggal, convert_date=True, keep_levels=True)
c=c.reset_index()
b["Net Trade in goods (Current USD)"]=c["Net Trade in goods (Current USD)"]/1000000
b["Net Primary Account (Current USD)"]=b["Net Primary Account (Current USD)"]/1000000
b=b.set_index('date')
del b['country']
plt.figure(figsize=(13.5,8))
graph2=sns.lineplot(data=b)
graph2.axhline(color='black')
graph2.set(ylabel='Juta USD',xlabel='Tahun')
plt.show()
```


![png](./Untitled_9_0.png)


## Menaikan ekspor atau menurunkan impor?

Menurut grafik di bawah ini, ekspor dan impor Indonesia nampak jalan secara beriringan.


```python
b=wb.get_dataframe({"BX.GSR.MRCH.CD" : "Goods Export (Current USD)"}, country=["IDN"], data_date=tanggal, convert_date=True, keep_levels=True)
b=b.reset_index()
b.head()
c=wb.get_dataframe({"BM.GSR.MRCH.CD" : "Goods Import (Current USD)"}, country=["IDN"], data_date=tanggal, convert_date=True, keep_levels=True)
c=c.reset_index()
b["Goods Export (Current USD)"]=b["Goods Export (Current USD)"]/1000000
b["Goods Import (Current USD)"]=c["Goods Import (Current USD)"]/1000000
b=b.set_index('date')
del b['country']
plt.figure(figsize=(13.5,8))
graph2=sns.lineplot(data=b)
graph2.set(ylabel='Juta USD',xlabel='Tahun')
plt.show()
```


![png](./Untitled_11_0.png)


Di jangka pendek, meningkatkan ekspor bisa jadi sangat sulit, terutama mengingat situasi global yang semakin tidak pasti. Industri andalan Indonesia, pertambangan dan perkebunan, masih lumayan produktif. Namun mengandalkan komoditas agak sulit mengingat harganya sangat fluktuatif. [COVID-19 makes it worse](https://www.eastasiaforum.org/2020/07/16/covid-19-punishes-indonesian-commodity-exporters/).

Kalau begitu, nurunin impor? Sayangnya, menurunkan impor juga tidak ideal. Impor Indonesia sebagian besar isinya adalah bahan baku industri dan barang modal. Bagi perusahaan yang beroprasi dengan memanfaatkan Global Value Chain (GVC), impor bahan baku merupakan hal yang sangat penting untuk berkompetisi di pasar global (alias naikin ekspor). Mungkin ini alasannya impor dan ekspor Indonesia berjalan beriringan. Kita tidak bisa meningkatkan ekspor tanpa meningkatkan impor. Mengurangi impor bisa berbahaya di jangka pendek (karena bahan baku dibutuhkan untuk produksi) dan jangka panjang (karena barang modal seperti mesin dibutuhkan untuk berkembang).


```python
# This one's not using WBdata. I use UNCOMTRADE i used for my other project
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
c=pd.read_csv('data.csv')
c=c.rename(columns = {'Trade Value (US$)' : 'Trade Value (Million US$)'})
c['Commodity']=c['Commodity'].replace({'Capital goods (except transport equipment), and parts and accessories thereof':'Capital goods'})
c['Commodity']=c['Commodity'].replace({'Transport equipment, and parts and accessories thereof':'Transport eq & parts'})
c['Trade Value (Million US$)']=c['Trade Value (Million US$)']/1000000
plt.figure(figsize=(13.5,8))
g=sns.lineplot(x="Period", y="Trade Value (Million US$)", hue="Commodity",data=c)
g.legend(loc='upper left', ncol=1)
```




    <matplotlib.legend.Legend at 0x1be0560a148>




![png](./Untitled_13_1.png)


Kembali Indonesia dihadapkan dengan tantangan yang tidak mudah. Saya rasa mengurangi impor bukan jalan keluar yang baik. Yang paling penting adalah memastikan bahwa investasi Indonesia semakin produktif dan menjaga agar [kepercayaan investor global tetap tinggi](https://www.eastasiaforum.org/2020/10/19/can-bank-indonesia-protect-its-independence/).
