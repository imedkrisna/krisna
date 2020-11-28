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

Just a bit of stats on RCEP. To connect it a bit with the [Global Value Chain](https://theconversation.com/kebijakan-untuk-meningkatkan-partisipasi-perusahaan-perusahaan-indonesia-dalam-rantai-pasok-global-150062), I am using Stage of Production (SoP) UNCTAD:




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



Just a very long code to aggregate RCEP. Sorry too lazy to make it DRY. Skip these if you don't need it to go straight to the stats.

The stats is:




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



This is, by the way, in 2018. There are `RCEP` countries in the `World` cuz i am too lazy to substract them. Also, I think it is useful to see how much Indonesians are trading with the rest of the world.

I wrote once on my blog about [how important imports are for Indonesian production](https://krisna.netlify.app/en/post/imporinput/). It is indeed reflected in this 2018 stat where the fraction of consumption goods in Indonesian import is just mere:

    23.83376244573637 %
    

which actually a decrease.

As for export, the other way around is true. That is, most exports are consumption goods. Even with this simple stat, it is so hard to convince Indonesian government that it is important to keep a free flow of goods not just export but also imports, to participate in the GVC. Indeed, increasing imports to help exports may seem very counter-intuitive for a country so used to exporting natural resources.

But of course, back to RCEP, what's important is how big is the fraction of RCEP to Indonesia's total trade.




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



And as you can see, RCEP countries are indeed very important to Indonesia's export and import. more than 70% Indonesia's consumption goods and capital goods came from RCEP countries in 2018.  Notably, Indonesian consumption goods export to RCEP countries is rather small, which makes sense because Indonesia's export destination for consumption goods also consist of plenty of developed nations like US, which reflects the importance of the extended [GSP tariff preference from the US]((https://theconversation.com/mengapa-perpanjangan-gsp-dari-amerika-serikat-penting-untuk-ekonomi-indonesia-150481)). The small importance of raw materials import is probably due to agriculture stuffs such as beef, soybean and wheat which many come from the US and Latin America.

That's all for this post and I hope it's useful.
