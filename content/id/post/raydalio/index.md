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
    
    


<div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.0.1.min.js" integrity="sha256-oy6Be7Eh6eiQFs5M7oXuPxxm9qbJXEtTpfSI93dW16Q=" crossorigin="anonymous"></script>                <div id="9a159779-78b1-44b5-876a-2a00523daf2d" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("9a159779-78b1-44b5-876a-2a00523daf2d")) {                    Plotly.newPlot(                        "9a159779-78b1-44b5-876a-2a00523daf2d",                        [{"hovertemplate":"country=Argentina\u003cbr\u003eyear=%{x}\u003cbr\u003emargin=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"Argentina","line":{"color":"#3366CC","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"Argentina","orientation":"v","showlegend":true,"x":[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],"xaxis":"x","y":[17.560431952584402,7.1586993831904,8.59229120621217,6.488586778309299,1.1322986462257,-10.6229549474007,-12.1266284021988,6.6447916241502,-7.1118721196937,-9.8440660330513,-11.664225933858098,-5.5572632545496,-15.8479204852182,0.10156735574160036,-3.7874038054853,-27.3890054029768,-41.9234900973542,-17.6781711690842,10.50645826390853,-3.4302979170447,-37.9423511440318],"yaxis":"y","type":"scatter"},{"hovertemplate":"country=Indonesia\u003cbr\u003eyear=%{x}\u003cbr\u003emargin=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"Indonesia","line":{"color":"#DC3912","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"Indonesia","orientation":"v","showlegend":true,"x":[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],"xaxis":"x","y":[-0.3474627005268003,0.6703516374924003,2.5334402585897,8.4268143241569,2.6472089498911,5.4208540448422,-0.5554132559046003,3.9124300990250003,5.48810434472793,4.8181270857678005,3.5154091717722005,3.6098599600974994,2.2437231823365,0.5900002059583,2.5579302456578,0.4405057358961999,0.7783202466445998,-5.9200552776919,-1.1182118510104,2.5060625948005,2.2806057706729],"yaxis":"y","type":"scatter"},{"hovertemplate":"country=Japan\u003cbr\u003eyear=%{x}\u003cbr\u003emargin=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"Japan","line":{"color":"#FF9900","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"Japan","orientation":"v","showlegend":true,"x":[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],"xaxis":"x","y":[0.267219209926,0.6679876931684001,0.12414347822399985,-0.11681772368650001,-0.14999621392430007,-1.33458740607391,-8.3763337178831,2.1711984953384995,-1.3784401360820762,0.46810259242884,1.6209613759347998,2.5002375892107604,1.99971483898296,0.681215365836731,2.11171462058188,1.5639504865843201,0.16253056083982997,-4.200003769196527,2.4095695350650503,3.4238646970277005,4.3773137545388],"yaxis":"y","type":"scatter"},{"hovertemplate":"country=T\u00fcrkiye, Republic of\u003cbr\u003eyear=%{x}\u003cbr\u003emargin=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"T\u00fcrkiye, Republic of","line":{"color":"#109618","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"T\u00fcrkiye, Republic of","orientation":"v","showlegend":true,"x":[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],"xaxis":"x","y":[-15.272876885419702,-6.346841433862,0.7943833404480003,8.0771322776176,4.9806753126024,1.72850071599506,-8.0221774238622,7.44332392351844,8.1665537231043,4.97863969242743,7.91190732827083,4.38460657146864,4.4435224698952,0.8968637390472001,7.523535083911572,3.5163116892652098,0.37395391600632005,1.763314612901108,14.0900249461662,60.3414573516573,33.121017733263],"yaxis":"y","type":"scatter"},{"hovertemplate":"country=United States\u003cbr\u003eyear=%{x}\u003cbr\u003emargin=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"United States","line":{"color":"#990099","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"United States","orientation":"v","showlegend":true,"x":[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],"xaxis":"x","y":[1.0793005113632002,2.2457662378350003,2.55906832506581,1.2132430168596,0.2520359401847001,0.27053553398437,-6.1769133468902,1.1312342743358001,1.91801500988058,2.55995817342839,1.2329205085911799,1.5983251238400398,0.9308128058225997,1.2452804636816102,2.2590407455885497,2.49566295189328,2.25266597565186,-1.80795613900575,9.2948040991434,7.5524916844071,3.05812760853076],"yaxis":"y","type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermap":[{"type":"scattermap","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"year"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"margin"}},"legend":{"title":{"text":"country"},"tracegroupgap":0},"title":{"text":"margin antara growth minus yield"}},                        {"responsive": true}                    )                };            </script>        </div>

awkoawkodkaodkwaodk

## Kesimpulan

mantap ges

mantap

[^1]: Ekonom, terutama ekonom makro, biasanya akan mengatakan bahwa indikator untuk individual firms tidak berlaku untuk negara. Hal ini gak salah sih, tapi akan saya kesampingkan dulu karena nanti blogpostnya jadi kemana-mana.
[^2]: Mauro, P., Romeu, R., Binder, A., & Zaman, A. (2015). A modern history of fiscal prudence and profligacy. Journal of Monetary Economics, 76, 55-70. https://doi.org/https://doi.org/10.1016/j.jmoneco.2015.07.003 
