---
title: "Melihat Indonesia lewat kacamata Ray Dalio: Bagaimana Negara Bankrut"
subtitle: ""
summary: ""
authors: [admin]
tags: [buku,ekonomi,utang]
categories: [buku, ekonomi,utang]
date: 2025-06-28T12:06:59+07:00
lastmod: 2025-06-28T12:06:59+07:00
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

## Tentang Buku Ray Dalio

Saya baru saja selesai membaca buku Ray Dalio yang berjudul "How Countries Go Broke", sebuah buku yang menggambarkan tentang bagaimanas ebuah negara mengalami krisis utang. Premis awalnya adalah Amerika Serikat (AS) yang saat ini tengah mengalami gejolak utang yang cukup besar yang memasuki stadium akhir dari apa yang ia sebut dengan "The Big Debt Cycle". Utang tersebut didorong oleh tidak hanya defisit anggaran, namun juga tingkat suku bunga dan inflasi yang sejak 2000an selalu sangat rendah sehingga utangnya bisa dengan mudah di-_rollover_. Gara-gara suku bunga yang terlalu rendah tersebut, AS (dan negara maju lain) menjadi terlalu santai dan jadi keranjingan utang. Namun setelah COVID-19, level suku bunga di negara maju mulai meningkat, sehingga membuat AS berpikir kembali tentang keberlanjutan utangnya.

Beberapa ekonom seperti Rogoff juga sudah mewanti-wanti utang AS, pun saya rasa Ray Dalio. Tapi di saat inflasi yang rendah lebih jadi masalah daripada inflasi yang tinggi, utang terus diberlakukan.

Saya sempat melihat paradigma yang sama di Australia, di mana Australia sangat santai dengan defisit neraca berjalannya yang sudah berjalan lebih dari 30 tahun tanpa sekalipun mengalami krisis. Dosen makro saya, [Timo Henckel](https://researchportalplus.anu.edu.au/en/persons/timo-henckel), pernah mengatakan bahwa hal ini bisa jadi berbahaya, tapi perdebatan ketika itu di Australia masih di arah santai. Dari Timo-lah saya belajar bahwa kita harus hati-hati dengan utang yang di permukaan tampak mudah. Politisi memperparah kondisi ini, karena meningkatkan belanja adalah apa yang memenangkan pemilu. Karena itu, mendisiplinkan utang adalah hal yang baru dilakukan ketika sudah terlambat.

Apakah AS sudah terlambat? Menurut Ray Dalio belum. AS sebenarnya masih bisa mulai melakukan apa yang ia sebut dengan "beautiful deleveraging", yaitu mengurangi utang dengan cara yang tidak menyakitkan. Hal ini bisa dilakukan dengan cara menaikkan pajak, mengurangi pengeluaran, dan sambil menurunkan suku bunga. Alias, menurut dia, perlu ada .Namun, jika hal ini tidak dilakukan, maka AS akan mengalami krisis utang yang lebih parah.

Masalahnya, kondisi saat ini dibarengi dengan ketidakpastian politik yang tinggi, baik di dalam negeri maupun geopolitik. Ditambah dengan masalah natural seperti krisis iklim dan ketidakpastian akan bagaimana teknologi akan mengubah ekonomi, membuat situasi semakin rumit. Ya, di bukunya, Ray juga membahas soal hal-hal non-utang seperti tensi geopolitik dan dorongan natural akibat iklim.

Buat saya, prinsip keberlangsungan utang yang diangkat Ray Dalio di buku itu bukanlah hal baru. Di kuliahnya Timo udah dibahas soal keberlangsungan utang ini. Bahkan yang ia sebut "beautiful deleveraging" itu juga sebenarnya cukup standar: di mana pemerintah dan bank sentral harus berkolaborasi, ketika pemerintah mengurangi utangnya (dengan cara motong anggaran sedikit + naikin pajak), sementara bank sentral menolong dengan menurunkan tingkat suku bunga. Tapi cara Ray Dalio menjelaskan hal ini sangat mudah dan mengalir, ibaratnya versi "bahasa bayi" dari kuliah makro.

Ray Dalio menurut saya adalah contoh seseorang yang belajar makro dengan cara otodidak. Dia tentu sudah ngobrol dengan banyak orang-orang yang jago makro, dan terjun langsung dalam praktiknya menjadi investor global, yang otomatis harus mempelajari kondisi makroekonomi berbagai negara yang menjadi portfolionya. Dari contoh-contoh yang dia sampaikan, negara mana di tahun berapa yang berhasil beautiful deleveraging dan mana yang tidak berhasil, membuat saya sangat menghargai bagaimana ia belajar.

## Mengaplikasikan indikator Ray Dalio

Di buku itu dia memberikan beberapa indikator dan contoh perhitungan kestabilan utang suatu negara. Beberapa indikator yang ia sebut adalah rasio utang terhadap pendapatan (dia bilang utang per PDB adalah indikator yang bisa misleading). Versi growth-nya juga bisa dihitung untuk melihat present value dari suatu utang. So far indikator yang ia pakai untuk negara sebenarnya sangat mainstream untuk investor dalam melihat fundamental[^1].

Saya mencoba melihat inidkator-indikator ini tapi pake versi gampang, alias ngandalin data historis aja tanpa saya coba proyeksikan ke depan seperti di buku Ray Dalio. Tentu karena malas. WKkwk. Data historis yang akan saya pakai adalah dari dataset IMF yang namanya Public Finances in Modern History[^2] yang bisa [diakses dengan mudah di sini](https://www.imf.org/external/datamapper/datasets/FPP). Karena datanya bentuknya menyebalkan, saya gabung dulu secara manual di excel. Dataset ini punya indikator-indikator seperti di bawah ini:

| Code   | Description                                                     |
|--------|-----------------------------------------------------------------|
| prim   | Government primary expenditure, percent of GDP (% of GDP)      |
| rev    | Government revenue, percent of GDP (% of GDP)                  |
| exp    | Government expenditure, percent of GDP (% of GDP)              |
| ie     | Interest paid on public debt, percent of GDP (% of GDP)        |
| pb     | Government primary balance, percent of GDP (% of GDP)          |
| d      | Gross public debt, percent of GDP (% of GDP)                   |
| rltir  | Real long term government bond yield, percent                  |
| rgc    | Real GDP growth rate, percent                                  |

Kita akan pakai yang standar-standar aja. Pertama adalah rasio utang terhadap pendapatan. Di tabel di atas, rasio utang terhadap PDB adalah "d", sementara rasio pendapatan negara terhadap PDB adalah "rev". Jadi kita bisa menghitung rasio utang terhadap pendapatan dengan mengambil rasio d/rev, di mana PDB nya akan kecoret karena ada di d dan di rev.

Di samping itu, saya akan mengambil selisih antara bunga utang dengan pertumbuhan PDB. Jika bunga yang dibayar lebih tinggi daripada pertumbuhan pendapatan, maka di jangka panjang, utangnya akan semakin mahal dan berpotensi tidak terkendali nantinya. Nah, kita asumsikan bahwa seiring dengan PDB bertambah, kemampuan negara dalam meningkatkan pendapatan juga bertambah, sehingga pertumbuhan revenue saya _proxy_ dengan pertumbuhan PDB. _Rough_, but still useful.


```python
import pandas as pd
import plotly.express as px
```


```python
## Preparing data.
negara=['Indonesia','Argentina','Türkiye, Republic of','United States','Japan'] ## Pilih negara yang mau dilihat
rev=pd.read_excel('imfdata.xlsx', sheet_name='rev').melt(id_vars=['country'], var_name='year', value_name='rev')
rev=rev.query('country in @negara & year>=1972')
prim=pd.read_excel('imfdata.xlsx', sheet_name='prim').melt(id_vars=['country'], var_name='year', value_name='prim')
prim=prim.query('country in @negara & year>=1972')
exp=pd.read_excel('imfdata.xlsx', sheet_name='exp').melt(id_vars=['country'], var_name='year', value_name='exp')
exp=exp.query('country in @negara & year>=1972')
ie=pd.read_excel('imfdata.xlsx', sheet_name='ie').melt(id_vars=['country'], var_name='year', value_name='ie')
ie=ie.query('country in @negara & year>=1972')
pb=pd.read_excel('imfdata.xlsx', sheet_name='pb').melt(id_vars=['country'], var_name='year', value_name='pb')
pb=pb.query('country in @negara & year>=1972')
d=pd.read_excel('imfdata.xlsx', sheet_name='d').melt(id_vars=['country'], var_name='year', value_name='d')
d=d.query('country in @negara & year>=1972')
rltir=pd.read_excel('imfdata.xlsx', sheet_name='rltir').melt(id_vars=['country'], var_name='year', value_name='rltir')
rltir=rltir.query('country in @negara & year>=1972')
rgc=pd.read_excel('imfdata.xlsx', sheet_name='rgc').melt(id_vars=['country'], var_name='year', value_name='rgc')
rgc=rgc.query('country in @negara & year>=1972')
gab=rev.merge(prim, on=['country','year'], how='inner')
gab=gab.merge(exp, on=['country','year'], how='inner')
gab=gab.merge(ie, on=['country','year'], how='inner')
gab=gab.merge(pb, on=['country','year'], how='inner')
gab=gab.merge(d, on=['country','year'], how='inner')
gab=gab.merge(rltir, on=['country','year'], how='inner')
gab=gab.merge(rgc, on=['country','year'], how='inner')
gab['wew']=gab['d']/gab['rev']
```


```python
fig = px.line(gab, x="year", y="wew", title='rasio antara utang dan pendapatan negara', color='country',
              color_discrete_sequence=px.colors.qualitative.G10)
fig.write_html('wew.html', full_html=False, include_plotlyjs='cdn')

gab2 = gab.query('year>=2003')
gab2['margin']=gab2['rgc']-gab2['rltir']

fig = px.line(gab2, x="year", y="margin", title='margin antara growth minus yield', color='country',
              color_discrete_sequence=px.colors.qualitative.G10)
fig.write_html('margin.html', full_html=False, include_plotlyjs='cdn')
```

    C:\Users\PC\AppData\Local\Temp\ipykernel_20008\3399404730.py:6: SettingWithCopyWarning:
    
    
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    
    

{{% include_relative "wew.html" %}}

ikikikik

{{% include_relative="wew.html" %}}

ehehehhe

{{% include_relative wew.html %}}

awokwokowkowkokw

{{< include_relative margin.html >}} 

lalala yeyeye

{{< include_relative="margin.html" >}}


awkoawkodkaodkwaodk

## Kesimpulan

mantap ges

mantap

[^1]: Ekonom, terutama ekonom makro, biasanya akan mengatakan bahwa indikator untuk individual firms tidak berlaku untuk negara. Hal ini gak salah sih, tapi akan saya kesampingkan dulu karena nanti blogpostnya jadi kemana-mana.
[^2]: Mauro, P., Romeu, R., Binder, A., & Zaman, A. (2015). A modern history of fiscal prudence and profligacy. Journal of Monetary Economics, 76, 55-70. https://doi.org/https://doi.org/10.1016/j.jmoneco.2015.07.003 
