---
layout: post
title: "Running a PPML regression in python using GME package from USITC"
categories: [blog, English]
tags: [Economics]
date: '2020-08-12'
author: admin
---


A couple of month ago, I just learned from a professor from my course about the new gravity dataset made by the [United States International Trade Commission (USITC)](https://www.usitc.gov/). Turns out, the USITC has not only a gravity dataset, but a dedicated page called ["gravity portal"](https://www.usitc.gov/data/gravity/dgd.htm) which contain some other data and software related to gravity estimation. And boy how excited I was when I just learned that they have made a python package to run a PPLM regression.

For non-economics bunch, us trade people called international trade estimation models as ["gravity model"](https://en.wikipedia.org/wiki/Gravity_model_of_trade). According to wikipedia, this model first introduced by Walter Isard, an American economist, in 1954, it is a model constructed to mimic a gravity. It takes the form of:

$$
Trade_{ij}=\frac{GDP_{i}*GDP_{j}}{Distance_{ij}} \label{eq1}
$$

That is, the amount of bilateral trade made by two countries $i$ and $j$ is related to their economic size (mass in the normal gravity equation) and their distance, as a proxy for trade cost. Obviously these days there are many extension to this model, but I won't dwell on it for now. For now, let's focus on the PPML extension.

Normally, we linearised equation \ref{eq1} by log transformation. That way, it is easy to estimate equation \ref{eq1} (or it's extensions) with OLS. Silva and Tenreyro (2006) critised the use of log-log OLS by showing that it is very hard to treat heteroskedasticity, common in trade data, with OLS extensions. In the paper, they show that non-linear regression especially PPLM performs much better. The paper became wildly popular among trade modeler. These days, it is hard to find a gravity modeler not using this method.

Running PPLM is pretty easy in STATA. Specialised packages such as this really makes it hard for me to switch to other language like R or python. As an international trade scholar, I have to rely on this package so I can focus on my research context. But now that I know PPLM package is out there, moving to python full-time become extra compelling!

So let's try how this works. First, import needed packages and grab the data that I used to run my thesis:


```python
import os
import pandas as pd
import numpy as np
import gme as gme
os.chdir('C:\github')
trade=pd.read_stata('gravitytest.dta')
trade
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
      <th>DISIC508</th>
      <th>psid</th>
      <th>HS2012</th>
      <th>hs10</th>
      <th>country</th>
      <th>imk</th>
      <th>imu</th>
      <th>year</th>
      <th>hs6</th>
      <th>imu6</th>
      <th>...</th>
      <th>entry_tp_d</th>
      <th>eu_o</th>
      <th>eu_d</th>
      <th>iso</th>
      <th>lgdp_o</th>
      <th>lgdp_d</th>
      <th>ldistw</th>
      <th>lmt</th>
      <th>lntma</th>
      <th>lntmb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15497</td>
      <td>47623.0</td>
      <td>9029109000</td>
      <td>9.029109e+09</td>
      <td></td>
      <td>4.0</td>
      <td>187.0</td>
      <td>2008.0</td>
      <td>902910</td>
      <td>24568.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>master only (1)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>29270</td>
      <td>17530.0</td>
      <td>9306900000</td>
      <td>9.306900e+09</td>
      <td></td>
      <td>1112.0</td>
      <td>8030.0</td>
      <td>2008.0</td>
      <td>930690</td>
      <td>563383.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>master only (1)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28113</td>
      <td>9703.0</td>
      <td>8483109000</td>
      <td>8.483109e+09</td>
      <td>REUNION</td>
      <td>172.0</td>
      <td>2369.0</td>
      <td>2008.0</td>
      <td>848310</td>
      <td>532539.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>master only (1)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>26202</td>
      <td>54660.0</td>
      <td>8538901900</td>
      <td>8.538902e+09</td>
      <td>REUNION</td>
      <td>1.0</td>
      <td>24.0</td>
      <td>2008.0</td>
      <td>853890</td>
      <td>12746.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>master only (1)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26202</td>
      <td>54660.0</td>
      <td>8413811000</td>
      <td>8.413811e+09</td>
      <td>REUNION</td>
      <td>738.0</td>
      <td>18487.0</td>
      <td>2008.0</td>
      <td>841381</td>
      <td>20723.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>master only (1)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.0</td>
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
      <th>416912</th>
      <td></td>
      <td>13085.0</td>
      <td>5201000000</td>
      <td>5.201000e+09</td>
      <td>ZIMBABWE</td>
      <td>4208425.0</td>
      <td>8388479.0</td>
      <td>2012.0</td>
      <td>520100</td>
      <td>183987968.0</td>
      <td>...</td>
      <td>58.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>matched (3)</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>9.056228</td>
      <td>0.000000</td>
      <td>1.098612</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>416913</th>
      <td></td>
      <td>13805.0</td>
      <td>5201000000</td>
      <td>5.201000e+09</td>
      <td>ZIMBABWE</td>
      <td>306143.0</td>
      <td>732298.0</td>
      <td>2012.0</td>
      <td>520100</td>
      <td>19769164.0</td>
      <td>...</td>
      <td>58.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>matched (3)</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>9.056228</td>
      <td>0.000000</td>
      <td>1.098612</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>416914</th>
      <td></td>
      <td>64381.0</td>
      <td>2401201000</td>
      <td>2.401201e+09</td>
      <td>ZIMBABWE</td>
      <td>10830.0</td>
      <td>87615.0</td>
      <td>2012.0</td>
      <td>240120</td>
      <td>6828994.0</td>
      <td>...</td>
      <td>58.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>matched (3)</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>9.056228</td>
      <td>1.791759</td>
      <td>1.098612</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>416915</th>
      <td></td>
      <td>27480.0</td>
      <td>2401201000</td>
      <td>2.401201e+09</td>
      <td>ZIMBABWE</td>
      <td>57600.0</td>
      <td>77760.0</td>
      <td>2012.0</td>
      <td>240120</td>
      <td>77760.0</td>
      <td>...</td>
      <td>58.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>matched (3)</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>9.056228</td>
      <td>1.791759</td>
      <td>1.098612</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>416916</th>
      <td></td>
      <td>27475.0</td>
      <td>2401101000</td>
      <td>2.401101e+09</td>
      <td>ZIMBABWE</td>
      <td>495000.0</td>
      <td>3019500.0</td>
      <td>2012.0</td>
      <td>240110</td>
      <td>68412784.0</td>
      <td>...</td>
      <td>58.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>matched (3)</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>9.056228</td>
      <td>1.791759</td>
      <td>1.098612</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>416917 rows × 107 columns</p>
</div>



I construct that dataset from Indonesian Bureau of Statistics. It has information on import made by firms in Indonesia in 2008-2012. As you can see, that dataset has 107 columns. I won't use them all for this test. let's kick the rest out and keep only what we need.


```python
trade=trade[['DISIC508','psid','country','imu6','lmt','lntma','lntmb','contig','comlang_off','ldistw','lgdp_o','lgdp_d','fta_wto','year']]
trade
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
      <th>DISIC508</th>
      <th>psid</th>
      <th>country</th>
      <th>imu6</th>
      <th>lmt</th>
      <th>lntma</th>
      <th>lntmb</th>
      <th>contig</th>
      <th>comlang_off</th>
      <th>ldistw</th>
      <th>lgdp_o</th>
      <th>lgdp_d</th>
      <th>fta_wto</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15497</td>
      <td>47623.0</td>
      <td></td>
      <td>24568.0</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>29270</td>
      <td>17530.0</td>
      <td></td>
      <td>563383.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28113</td>
      <td>9703.0</td>
      <td>REUNION</td>
      <td>532539.0</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>26202</td>
      <td>54660.0</td>
      <td>REUNION</td>
      <td>12746.0</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26202</td>
      <td>54660.0</td>
      <td>REUNION</td>
      <td>20723.0</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.0</td>
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
    </tr>
    <tr>
      <th>416912</th>
      <td></td>
      <td>13085.0</td>
      <td>ZIMBABWE</td>
      <td>183987968.0</td>
      <td>0.000000</td>
      <td>1.098612</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.056228</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>0.0</td>
      <td>2012.0</td>
    </tr>
    <tr>
      <th>416913</th>
      <td></td>
      <td>13805.0</td>
      <td>ZIMBABWE</td>
      <td>19769164.0</td>
      <td>0.000000</td>
      <td>1.098612</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.056228</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>0.0</td>
      <td>2012.0</td>
    </tr>
    <tr>
      <th>416914</th>
      <td></td>
      <td>64381.0</td>
      <td>ZIMBABWE</td>
      <td>6828994.0</td>
      <td>1.791759</td>
      <td>1.098612</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.056228</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>0.0</td>
      <td>2012.0</td>
    </tr>
    <tr>
      <th>416915</th>
      <td></td>
      <td>27480.0</td>
      <td>ZIMBABWE</td>
      <td>77760.0</td>
      <td>1.791759</td>
      <td>1.098612</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.056228</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>0.0</td>
      <td>2012.0</td>
    </tr>
    <tr>
      <th>416916</th>
      <td></td>
      <td>27475.0</td>
      <td>ZIMBABWE</td>
      <td>68412784.0</td>
      <td>1.791759</td>
      <td>1.098612</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.056228</td>
      <td>23.246786</td>
      <td>27.499453</td>
      <td>0.0</td>
      <td>2012.0</td>
    </tr>
  </tbody>
</table>
<p>416917 rows × 14 columns</p>
</div>



Much better. But let's make a two-digit ISIC code for fixed effect, and then show summary statistics of my data.


```python
pd.options.mode.chained_assignment = None  # default='warn', dapat dari stackoverflow
trade['isic2']=trade['DISIC508'].str[:2] # bikin isic 2 digit
trade.describe(include='all')
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
      <th>DISIC508</th>
      <th>psid</th>
      <th>country</th>
      <th>imu6</th>
      <th>lmt</th>
      <th>lntma</th>
      <th>lntmb</th>
      <th>contig</th>
      <th>comlang_off</th>
      <th>ldistw</th>
      <th>lgdp_o</th>
      <th>lgdp_d</th>
      <th>fta_wto</th>
      <th>year</th>
      <th>isic2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>416917</td>
      <td>416917.000000</td>
      <td>416917</td>
      <td>4.169170e+05</td>
      <td>416917.000000</td>
      <td>416917.000000</td>
      <td>416917.000000</td>
      <td>416528.000000</td>
      <td>416528.0</td>
      <td>416528.000000</td>
      <td>416334.000000</td>
      <td>416528.000000</td>
      <td>416156.000000</td>
      <td>416917.000000</td>
      <td>416917</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>251</td>
      <td>NaN</td>
      <td>207</td>
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
      <td>NaN</td>
      <td>24</td>
    </tr>
    <tr>
      <th>top</th>
      <td></td>
      <td>NaN</td>
      <td>JAPAN</td>
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
      <td>NaN</td>
      <td></td>
    </tr>
    <tr>
      <th>freq</th>
      <td>346920</td>
      <td>NaN</td>
      <td>78312</td>
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
      <td>NaN</td>
      <td>346920</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>NaN</td>
      <td>39929.765625</td>
      <td>NaN</td>
      <td>1.578270e+06</td>
      <td>1.640825</td>
      <td>0.046497</td>
      <td>0.069130</td>
      <td>0.039210</td>
      <td>0.0</td>
      <td>8.407879</td>
      <td>28.012295</td>
      <td>27.228710</td>
      <td>0.626592</td>
      <td>2003.304932</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>NaN</td>
      <td>19671.726562</td>
      <td>NaN</td>
      <td>1.813418e+07</td>
      <td>0.921622</td>
      <td>0.250223</td>
      <td>0.280148</td>
      <td>0.194094</td>
      <td>0.0</td>
      <td>0.755016</td>
      <td>1.452945</td>
      <td>0.225774</td>
      <td>0.483710</td>
      <td>7.055770</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>NaN</td>
      <td>1892.000000</td>
      <td>NaN</td>
      <td>1.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>6.194654</td>
      <td>17.226353</td>
      <td>26.958157</td>
      <td>0.000000</td>
      <td>2008.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>NaN</td>
      <td>17958.000000</td>
      <td>NaN</td>
      <td>2.010000e+03</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>8.184400</td>
      <td>26.498676</td>
      <td>27.014057</td>
      <td>0.000000</td>
      <td>2009.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>NaN</td>
      <td>44835.000000</td>
      <td>NaN</td>
      <td>2.078600e+04</td>
      <td>1.791759</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>8.532608</td>
      <td>28.262346</td>
      <td>27.287390</td>
      <td>1.000000</td>
      <td>2010.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>NaN</td>
      <td>56871.000000</td>
      <td>NaN</td>
      <td>1.993940e+05</td>
      <td>2.397895</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>8.609140</td>
      <td>29.334930</td>
      <td>27.463705</td>
      <td>1.000000</td>
      <td>2011.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>NaN</td>
      <td>72930.000000</td>
      <td>NaN</td>
      <td>1.450820e+09</td>
      <td>11.736077</td>
      <td>3.401197</td>
      <td>2.639057</td>
      <td>1.000000</td>
      <td>0.0</td>
      <td>9.871479</td>
      <td>30.413757</td>
      <td>27.499453</td>
      <td>1.000000</td>
      <td>2012.000000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



looks good. So many empty cells lol. Anyway, this data set has only 1 importing country, that is, Indonesia. Of course I have varied firms, so instead of a country, let's make these firms as the importer. I have many exporting countries, including tariff asociated with their purchase (varies with country of origin, type of goods in HS-6-digit code, and year) which I dubbed 'lmt' in the dataset. I also have the number of SPS (lntma) and TBT (lntmb) associated with goods purchased by those firms.

so first of all, we set the environment to prepare the data for the regression. This is like using `xtset` in STATA for `xtreg`, I think.


```python
gme_data=gme.EstimationData(data_frame=trade,
                           imp_var_name='psid',
                           exp_var_name='country',
                           trade_var_name='imu6',
                           sector_var_name='isic2',
                            year_var_name='year')
print(gme_data)
```

    number of countries: 2463 
    number of exporters: 207 
    number of importers: 2256 
    number of years: 5 
    number of sectors: 24 
    dimensions: (416917, 15)
    
    

Now that it all set, let's let the machine go brrrr. Don't forget to set your fixed effects.


```python
gme_model=gme.EstimationModel(estimation_data=gme_data,
                             lhs_var='imu6',
                             rhs_var=['lmt','lntma','lntmb','lgdp_o','lgdp_d','ldistw','fta_wto','contig','comlang_off'],
                             fixed_effects=['country','isic2'])
estimates=gme_model.estimate()
```

    select specification variables: ['lmt', 'lntma', 'lntmb', 'lgdp_o', 'lgdp_d', 'ldistw', 'fta_wto', 'contig', 'comlang_off', 'imu6', 'psid', 'country', 'year', 'isic2'], Observations excluded by user: {'rows': 0, 'columns': 1}
    drop_intratrade: no, Observations excluded by user: {'rows': 0, 'columns': 0}
    drop_imp: none, Observations excluded by user: {'rows': 0, 'columns': 0}
    drop_exp: none, Observations excluded by user: {'rows': 0, 'columns': 0}
    keep_imp: all available, Observations excluded by user: {'rows': 0, 'columns': 0}
    keep_exp: all available, Observations excluded by user: {'rows': 0, 'columns': 0}
    drop_years: none, Observations excluded by user: {'rows': 0, 'columns': 0}
    keep_years: all available, Observations excluded by user: {'rows': 0, 'columns': 0}
    drop_missing: yes, Observations excluded by user: {'rows': 955, 'columns': 0}
    Estimation began at 12:39 PM  on Aug 12, 2020
    Omitted Columns: ['comlang_off', 'country_fe_PAPUA NEW GUINEA', 'country_fe_ZIMBABWE', 'isic2_fe_37', 'country_fe_MALAYSIA', 'country_fe_ZAMBIA', 'isic2_fe_36']
    Estimation completed at 12:40 PM  on Aug 12, 2020
    


```python
result=gme.combine_sector_results(estimates)
result.head(8)
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
      <th>all_coeff</th>
      <th>all_stderr</th>
      <th>all_pvalue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>lmt</th>
      <td>-0.639771</td>
      <td>0.021540</td>
      <td>7.396863e-194</td>
    </tr>
    <tr>
      <th>lntma</th>
      <td>0.561644</td>
      <td>0.033192</td>
      <td>3.152121e-64</td>
    </tr>
    <tr>
      <th>lntmb</th>
      <td>0.364746</td>
      <td>0.036307</td>
      <td>9.556518e-24</td>
    </tr>
    <tr>
      <th>lgdp_o</th>
      <td>0.393253</td>
      <td>0.191870</td>
      <td>4.040557e-02</td>
    </tr>
    <tr>
      <th>lgdp_d</th>
      <td>0.946128</td>
      <td>0.157832</td>
      <td>2.040966e-09</td>
    </tr>
    <tr>
      <th>ldistw</th>
      <td>-2.106424</td>
      <td>0.409394</td>
      <td>2.671980e-07</td>
    </tr>
    <tr>
      <th>fta_wto</th>
      <td>0.073430</td>
      <td>0.100158</td>
      <td>4.634703e-01</td>
    </tr>
    <tr>
      <th>contig</th>
      <td>-6.504605</td>
      <td>1.125489</td>
      <td>7.498616e-09</td>
    </tr>
  </tbody>
</table>
</div>



And there you go. Table above shows coefficients from the PPLM. I think the python ran this thing a bit faster than STATA but I have to check again since my PPLM in STATA has more stuff in it.

The result is very close to my STATA result I think (again I never really ran it with only these number of variables for my thesis). tariff (lmt) and Indonesian GDP (lgdp_d) have an expected sign and somewhat expected magnitude Distance has an expected sign but it looks very high indeed (remember this is firm's purchase). FTA has no significance which is expected (must be absorbed by FE and tariff).

NTM still shows a positive and significant result, which is a bit intriguing. One argument that make sense is reverse causality. That is, the government seems to be wary of Current Account Deficit (CAD). The higher the observed import, the more likely it is willing to raise Non-Tariff Measures.

Of course this is just a quick thought. I am treating this causality problem a bit more serious on my paper with some ways or the other. Bottom line is, PPLM is now working on python and I have one less reason to stick with STATA. Now when the whole ANU switch to R and python, I think I will be ready. Ha ha ha ha!

Thanks for reading this post, I hope it's useful. Happy to reply to any comments. Here's a longer result of the regression.


```python
# long result
estimates.keys()
results=estimates['all']
results.summary()
```




<table class="simpletable">
<caption>Generalized Linear Model Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>     <td>imu6</td>   <th>  No. Iterations:    </th>     <td>12</td>     
</tr>
<tr>
  <th>Model:</th>              <td>GLM</td>   <th>  Df Residuals:      </th>   <td>415640</td>   
</tr>
<tr>
  <th>Model Family:</th>     <td>Poisson</td> <th>  Df Model:          </th>     <td>191</td>    
</tr>
<tr>
  <th>Link Function:</th>      <td>log</td>   <th>  Scale:             </th>  <td>  1.0000</td>  
</tr>
<tr>
  <th>Method:</th>            <td>IRLS</td>   <th>  Log-Likelihood:    </th> <td>-1.5906e+12</td>
</tr>
<tr>
  <th>Covariance Type:</th>    <td>HC1</td>   <th>  Deviance:          </th> <td>3.1813e+12</td> 
</tr>
<tr>
  <th>No. Observations:</th> <td>415832</td>  <th>  Pearson chi2:      </th>  <td>3.96e+13</td>  
</tr>
</table>
<table class="simpletable">
<tr>
                   <td></td>                      <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>lmt</th>                                 <td>   -0.6398</td> <td>    0.022</td> <td>  -29.701</td> <td> 0.000</td> <td>   -0.682</td> <td>   -0.598</td>
</tr>
<tr>
  <th>lntma</th>                               <td>    0.5616</td> <td>    0.033</td> <td>   16.921</td> <td> 0.000</td> <td>    0.497</td> <td>    0.627</td>
</tr>
<tr>
  <th>lntmb</th>                               <td>    0.3647</td> <td>    0.036</td> <td>   10.046</td> <td> 0.000</td> <td>    0.294</td> <td>    0.436</td>
</tr>
<tr>
  <th>lgdp_o</th>                              <td>    0.3933</td> <td>    0.192</td> <td>    2.050</td> <td> 0.040</td> <td>    0.017</td> <td>    0.769</td>
</tr>
<tr>
  <th>lgdp_d</th>                              <td>    0.9461</td> <td>    0.158</td> <td>    5.995</td> <td> 0.000</td> <td>    0.637</td> <td>    1.255</td>
</tr>
<tr>
  <th>ldistw</th>                              <td>   -2.1064</td> <td>    0.409</td> <td>   -5.145</td> <td> 0.000</td> <td>   -2.909</td> <td>   -1.304</td>
</tr>
<tr>
  <th>fta_wto</th>                             <td>    0.0734</td> <td>    0.100</td> <td>    0.733</td> <td> 0.463</td> <td>   -0.123</td> <td>    0.270</td>
</tr>
<tr>
  <th>contig</th>                              <td>   -6.5046</td> <td>    1.125</td> <td>   -5.779</td> <td> 0.000</td> <td>   -8.711</td> <td>   -4.299</td>
</tr>
<tr>
  <th>country_fe_AFGHANISTAN</th>              <td>    0.4090</td> <td>    0.466</td> <td>    0.877</td> <td> 0.380</td> <td>   -0.505</td> <td>    1.323</td>
</tr>
<tr>
  <th>country_fe_ALBANIA</th>                  <td>   -0.6846</td> <td>    0.795</td> <td>   -0.862</td> <td> 0.389</td> <td>   -2.242</td> <td>    0.873</td>
</tr>
<tr>
  <th>country_fe_ALGERIA</th>                  <td>    1.4254</td> <td>    1.025</td> <td>    1.391</td> <td> 0.164</td> <td>   -0.583</td> <td>    3.434</td>
</tr>
<tr>
  <th>country_fe_ANGOLA</th>                   <td>    0.5248</td> <td>    0.607</td> <td>    0.865</td> <td> 0.387</td> <td>   -0.664</td> <td>    1.714</td>
</tr>
<tr>
  <th>country_fe_ANTIGUA DNA BARBUDA</th>      <td>    1.7079</td> <td>    0.911</td> <td>    1.875</td> <td> 0.061</td> <td>   -0.078</td> <td>    3.494</td>
</tr>
<tr>
  <th>country_fe_ARGENTINA</th>                <td>   -0.2130</td> <td>    0.746</td> <td>   -0.286</td> <td> 0.775</td> <td>   -1.676</td> <td>    1.249</td>
</tr>
<tr>
  <th>country_fe_ARMENIA</th>                  <td>   -2.6577</td> <td>    0.859</td> <td>   -3.095</td> <td> 0.002</td> <td>   -4.340</td> <td>   -0.975</td>
</tr>
<tr>
  <th>country_fe_AUSTRALIA</th>                <td>   -3.7090</td> <td>    0.991</td> <td>   -3.741</td> <td> 0.000</td> <td>   -5.652</td> <td>   -1.766</td>
</tr>
<tr>
  <th>country_fe_AUSTRIA</th>                  <td>   -3.4246</td> <td>    0.725</td> <td>   -4.725</td> <td> 0.000</td> <td>   -4.845</td> <td>   -2.004</td>
</tr>
<tr>
  <th>country_fe_BAHAMAS</th>                  <td>    3.1000</td> <td>    0.629</td> <td>    4.930</td> <td> 0.000</td> <td>    1.868</td> <td>    4.332</td>
</tr>
<tr>
  <th>country_fe_BAHRAIN</th>                  <td>    0.3896</td> <td>    0.659</td> <td>    0.592</td> <td> 0.554</td> <td>   -0.901</td> <td>    1.680</td>
</tr>
<tr>
  <th>country_fe_BANGLADESH</th>               <td>   -2.7922</td> <td>    0.787</td> <td>   -3.549</td> <td> 0.000</td> <td>   -4.334</td> <td>   -1.250</td>
</tr>
<tr>
  <th>country_fe_BARBADOS</th>                 <td>    2.9386</td> <td>    0.751</td> <td>    3.912</td> <td> 0.000</td> <td>    1.466</td> <td>    4.411</td>
</tr>
<tr>
  <th>country_fe_BELARUS</th>                  <td>    1.4382</td> <td>    0.532</td> <td>    2.705</td> <td> 0.007</td> <td>    0.396</td> <td>    2.480</td>
</tr>
<tr>
  <th>country_fe_BELGIUM</th>                  <td>   -2.0392</td> <td>    0.744</td> <td>   -2.741</td> <td> 0.006</td> <td>   -3.497</td> <td>   -0.581</td>
</tr>
<tr>
  <th>country_fe_BELIZE</th>                   <td>    1.1173</td> <td>    1.105</td> <td>    1.011</td> <td> 0.312</td> <td>   -1.048</td> <td>    3.282</td>
</tr>
<tr>
  <th>country_fe_BENIN</th>                    <td>    1.7086</td> <td>    0.593</td> <td>    2.883</td> <td> 0.004</td> <td>    0.547</td> <td>    2.870</td>
</tr>
<tr>
  <th>country_fe_BOLIVIA</th>                  <td>   -1.5380</td> <td>    0.663</td> <td>   -2.319</td> <td> 0.020</td> <td>   -2.838</td> <td>   -0.238</td>
</tr>
<tr>
  <th>country_fe_BOSNIA AND HERZEGOVINA</th>   <td>    0.4275</td> <td>    1.082</td> <td>    0.395</td> <td> 0.693</td> <td>   -1.693</td> <td>    2.548</td>
</tr>
<tr>
  <th>country_fe_BOTSWANA</th>                 <td>   -7.9549</td> <td>    0.479</td> <td>  -16.601</td> <td> 0.000</td> <td>   -8.894</td> <td>   -7.016</td>
</tr>
<tr>
  <th>country_fe_BRAZIL</th>                   <td>   -0.6946</td> <td>    0.935</td> <td>   -0.743</td> <td> 0.458</td> <td>   -2.528</td> <td>    1.139</td>
</tr>
<tr>
  <th>country_fe_BRUNEI DARUSSALAM</th>        <td>   -5.0344</td> <td>    0.860</td> <td>   -5.851</td> <td> 0.000</td> <td>   -6.721</td> <td>   -3.348</td>
</tr>
<tr>
  <th>country_fe_BULGARIA</th>                 <td>   -0.8735</td> <td>    0.579</td> <td>   -1.508</td> <td> 0.132</td> <td>   -2.009</td> <td>    0.262</td>
</tr>
<tr>
  <th>country_fe_BURKINA FASO</th>             <td>    0.7212</td> <td>    0.604</td> <td>    1.194</td> <td> 0.232</td> <td>   -0.462</td> <td>    1.905</td>
</tr>
<tr>
  <th>country_fe_CAMBODIA</th>                 <td>   -2.6752</td> <td>    0.871</td> <td>   -3.073</td> <td> 0.002</td> <td>   -4.382</td> <td>   -0.969</td>
</tr>
<tr>
  <th>country_fe_CAMEROON</th>                 <td>    0.0639</td> <td>    0.578</td> <td>    0.111</td> <td> 0.912</td> <td>   -1.069</td> <td>    1.197</td>
</tr>
<tr>
  <th>country_fe_CANADA</th>                   <td>   -0.9668</td> <td>    0.924</td> <td>   -1.046</td> <td> 0.295</td> <td>   -2.778</td> <td>    0.844</td>
</tr>
<tr>
  <th>country_fe_CAPE VERDE</th>               <td>    3.3896</td> <td>    0.832</td> <td>    4.075</td> <td> 0.000</td> <td>    1.759</td> <td>    5.020</td>
</tr>
<tr>
  <th>country_fe_CENTRAL AFRICAN REPUBLIC</th> <td>    0.6676</td> <td>    0.796</td> <td>    0.839</td> <td> 0.402</td> <td>   -0.892</td> <td>    2.228</td>
</tr>
<tr>
  <th>country_fe_CHAD</th>                     <td>    1.4187</td> <td>    0.739</td> <td>    1.919</td> <td> 0.055</td> <td>   -0.030</td> <td>    2.868</td>
</tr>
<tr>
  <th>country_fe_CHILE</th>                    <td>   -0.7792</td> <td>    0.664</td> <td>   -1.174</td> <td> 0.241</td> <td>   -2.080</td> <td>    0.522</td>
</tr>
<tr>
  <th>country_fe_CHINA</th>                    <td>   -5.9689</td> <td>    1.306</td> <td>   -4.571</td> <td> 0.000</td> <td>   -8.528</td> <td>   -3.410</td>
</tr>
<tr>
  <th>country_fe_COLOMBIA</th>                 <td>    0.5011</td> <td>    0.764</td> <td>    0.656</td> <td> 0.512</td> <td>   -0.997</td> <td>    1.999</td>
</tr>
<tr>
  <th>country_fe_COMOROS</th>                  <td>   -4.4323</td> <td>    1.051</td> <td>   -4.217</td> <td> 0.000</td> <td>   -6.492</td> <td>   -2.372</td>
</tr>
<tr>
  <th>country_fe_COSTA RICA</th>               <td>    1.3587</td> <td>    0.671</td> <td>    2.024</td> <td> 0.043</td> <td>    0.043</td> <td>    2.674</td>
</tr>
<tr>
  <th>country_fe_COTE D'IVOIRE</th>            <td>    0.7333</td> <td>    0.552</td> <td>    1.329</td> <td> 0.184</td> <td>   -0.348</td> <td>    1.815</td>
</tr>
<tr>
  <th>country_fe_CROATIA</th>                  <td>   -0.8040</td> <td>    0.744</td> <td>   -1.080</td> <td> 0.280</td> <td>   -2.263</td> <td>    0.655</td>
</tr>
<tr>
  <th>country_fe_CUBA</th>                     <td>    1.4541</td> <td>    0.761</td> <td>    1.911</td> <td> 0.056</td> <td>   -0.037</td> <td>    2.946</td>
</tr>
<tr>
  <th>country_fe_CYPRUS</th>                   <td>    0.2204</td> <td>    0.596</td> <td>    0.370</td> <td> 0.712</td> <td>   -0.948</td> <td>    1.389</td>
</tr>
<tr>
  <th>country_fe_CZECH REPUBLIC</th>           <td>   -2.0958</td> <td>    0.645</td> <td>   -3.251</td> <td> 0.001</td> <td>   -3.359</td> <td>   -0.832</td>
</tr>
<tr>
  <th>country_fe_DENMARK</th>                  <td>   -2.8564</td> <td>    0.701</td> <td>   -4.074</td> <td> 0.000</td> <td>   -4.231</td> <td>   -1.482</td>
</tr>
<tr>
  <th>country_fe_DJIBOUTI</th>                 <td>    1.6503</td> <td>    0.755</td> <td>    2.187</td> <td> 0.029</td> <td>    0.171</td> <td>    3.129</td>
</tr>
<tr>
  <th>country_fe_ECUADOR</th>                  <td>    0.2109</td> <td>    0.792</td> <td>    0.266</td> <td> 0.790</td> <td>   -1.341</td> <td>    1.763</td>
</tr>
<tr>
  <th>country_fe_EGYPT</th>                    <td>   -0.7402</td> <td>    0.680</td> <td>   -1.089</td> <td> 0.276</td> <td>   -2.073</td> <td>    0.592</td>
</tr>
<tr>
  <th>country_fe_EL SALVADOR</th>              <td>    2.7996</td> <td>    0.642</td> <td>    4.363</td> <td> 0.000</td> <td>    1.542</td> <td>    4.057</td>
</tr>
<tr>
  <th>country_fe_ESTONIA</th>                  <td>    0.6244</td> <td>    0.550</td> <td>    1.135</td> <td> 0.256</td> <td>   -0.454</td> <td>    1.703</td>
</tr>
<tr>
  <th>country_fe_ETHIOPIA</th>                 <td>   -1.1273</td> <td>    0.722</td> <td>   -1.561</td> <td> 0.118</td> <td>   -2.542</td> <td>    0.288</td>
</tr>
<tr>
  <th>country_fe_FIJI</th>                     <td>   -0.4756</td> <td>    0.866</td> <td>   -0.549</td> <td> 0.583</td> <td>   -2.174</td> <td>    1.222</td>
</tr>
<tr>
  <th>country_fe_FINLAND</th>                  <td>   -2.3117</td> <td>    0.668</td> <td>   -3.460</td> <td> 0.001</td> <td>   -3.621</td> <td>   -1.002</td>
</tr>
<tr>
  <th>country_fe_FRANCE</th>                   <td>   -3.2455</td> <td>    1.010</td> <td>   -3.213</td> <td> 0.001</td> <td>   -5.225</td> <td>   -1.266</td>
</tr>
<tr>
  <th>country_fe_GABON</th>                    <td>    0.9253</td> <td>    0.591</td> <td>    1.566</td> <td> 0.117</td> <td>   -0.233</td> <td>    2.083</td>
</tr>
<tr>
  <th>country_fe_GAMBIA</th>                   <td>    3.0057</td> <td>    0.869</td> <td>    3.459</td> <td> 0.001</td> <td>    1.303</td> <td>    4.709</td>
</tr>
<tr>
  <th>country_fe_GEORGIA</th>                  <td>    0.7857</td> <td>    0.535</td> <td>    1.469</td> <td> 0.142</td> <td>   -0.263</td> <td>    1.834</td>
</tr>
<tr>
  <th>country_fe_GERMANY</th>                  <td>   -4.1535</td> <td>    1.053</td> <td>   -3.944</td> <td> 0.000</td> <td>   -6.217</td> <td>   -2.090</td>
</tr>
<tr>
  <th>country_fe_GHANA</th>                    <td>    1.0493</td> <td>    0.552</td> <td>    1.899</td> <td> 0.058</td> <td>   -0.033</td> <td>    2.132</td>
</tr>
<tr>
  <th>country_fe_GREECE</th>                   <td>   -1.0759</td> <td>    0.695</td> <td>   -1.547</td> <td> 0.122</td> <td>   -2.439</td> <td>    0.287</td>
</tr>
<tr>
  <th>country_fe_GUATEMALA</th>                <td>    2.7991</td> <td>    0.699</td> <td>    4.007</td> <td> 0.000</td> <td>    1.430</td> <td>    4.168</td>
</tr>
<tr>
  <th>country_fe_GUINEA</th>                   <td>    2.4787</td> <td>    0.655</td> <td>    3.782</td> <td> 0.000</td> <td>    1.194</td> <td>    3.763</td>
</tr>
<tr>
  <th>country_fe_GUINEA BISSAU</th>            <td>    3.0531</td> <td>    0.832</td> <td>    3.669</td> <td> 0.000</td> <td>    1.422</td> <td>    4.684</td>
</tr>
<tr>
  <th>country_fe_GUYANA</th>                   <td>    3.3098</td> <td>    0.896</td> <td>    3.693</td> <td> 0.000</td> <td>    1.553</td> <td>    5.066</td>
</tr>
<tr>
  <th>country_fe_HAITI</th>                    <td>    4.4323</td> <td>    0.876</td> <td>    5.060</td> <td> 0.000</td> <td>    2.715</td> <td>    6.149</td>
</tr>
<tr>
  <th>country_fe_HONDURAS</th>                 <td>    2.4895</td> <td>    0.642</td> <td>    3.879</td> <td> 0.000</td> <td>    1.232</td> <td>    3.747</td>
</tr>
<tr>
  <th>country_fe_HONG KONG</th>                <td>   -4.9675</td> <td>    0.869</td> <td>   -5.713</td> <td> 0.000</td> <td>   -6.672</td> <td>   -3.263</td>
</tr>
<tr>
  <th>country_fe_HUNGARY</th>                  <td>   -1.8897</td> <td>    0.607</td> <td>   -3.116</td> <td> 0.002</td> <td>   -3.078</td> <td>   -0.701</td>
</tr>
<tr>
  <th>country_fe_ICELAND</th>                  <td>   -0.5570</td> <td>    0.855</td> <td>   -0.652</td> <td> 0.515</td> <td>   -2.232</td> <td>    1.118</td>
</tr>
<tr>
  <th>country_fe_INDIA</th>                    <td>   -4.5392</td> <td>    1.069</td> <td>   -4.247</td> <td> 0.000</td> <td>   -6.634</td> <td>   -2.444</td>
</tr>
<tr>
  <th>country_fe_INDONESIA</th>                <td>   -7.4981</td> <td>    1.514</td> <td>   -4.951</td> <td> 0.000</td> <td>  -10.466</td> <td>   -4.530</td>
</tr>
<tr>
  <th>country_fe_IRAN</th>                     <td>   -0.3197</td> <td>    0.805</td> <td>   -0.397</td> <td> 0.691</td> <td>   -1.898</td> <td>    1.259</td>
</tr>
<tr>
  <th>country_fe_IRELAND</th>                  <td>   -0.4954</td> <td>    0.650</td> <td>   -0.762</td> <td> 0.446</td> <td>   -1.770</td> <td>    0.779</td>
</tr>
<tr>
  <th>country_fe_ISRAEL</th>                   <td>   -3.9824</td> <td>    0.702</td> <td>   -5.676</td> <td> 0.000</td> <td>   -5.358</td> <td>   -2.607</td>
</tr>
<tr>
  <th>country_fe_ITALY</th>                    <td>   -3.9412</td> <td>    0.977</td> <td>   -4.034</td> <td> 0.000</td> <td>   -5.856</td> <td>   -2.026</td>
</tr>
<tr>
  <th>country_fe_JAMAICA</th>                  <td>    2.6006</td> <td>    0.640</td> <td>    4.062</td> <td> 0.000</td> <td>    1.346</td> <td>    3.856</td>
</tr>
<tr>
  <th>country_fe_JAPAN</th>                    <td>   -5.5958</td> <td>    1.237</td> <td>   -4.525</td> <td> 0.000</td> <td>   -8.019</td> <td>   -3.172</td>
</tr>
<tr>
  <th>country_fe_JORDAN</th>                   <td>    1.1906</td> <td>    0.522</td> <td>    2.282</td> <td> 0.023</td> <td>    0.168</td> <td>    2.213</td>
</tr>
<tr>
  <th>country_fe_KAZAKHSTAN</th>               <td>   -1.2164</td> <td>    0.867</td> <td>   -1.403</td> <td> 0.160</td> <td>   -2.915</td> <td>    0.482</td>
</tr>
<tr>
  <th>country_fe_KENYA</th>                    <td>   -1.0302</td> <td>    0.635</td> <td>   -1.622</td> <td> 0.105</td> <td>   -2.275</td> <td>    0.214</td>
</tr>
<tr>
  <th>country_fe_KIRIBATI</th>                 <td>   -0.2963</td> <td>    1.067</td> <td>   -0.278</td> <td> 0.781</td> <td>   -2.388</td> <td>    1.795</td>
</tr>
<tr>
  <th>country_fe_KOREA SELATAN</th>            <td>   -4.9764</td> <td>    0.980</td> <td>   -5.076</td> <td> 0.000</td> <td>   -6.898</td> <td>   -3.055</td>
</tr>
<tr>
  <th>country_fe_KUWAIT</th>                   <td>    0.1261</td> <td>    0.703</td> <td>    0.179</td> <td> 0.858</td> <td>   -1.252</td> <td>    1.504</td>
</tr>
<tr>
  <th>country_fe_KYRGYZSTAN</th>               <td>   -0.4947</td> <td>    0.661</td> <td>   -0.748</td> <td> 0.454</td> <td>   -1.790</td> <td>    0.801</td>
</tr>
<tr>
  <th>country_fe_LAOS</th>                     <td>   -3.7586</td> <td>    0.655</td> <td>   -5.736</td> <td> 0.000</td> <td>   -5.043</td> <td>   -2.474</td>
</tr>
<tr>
  <th>country_fe_LATVIA</th>                   <td>    0.8944</td> <td>    0.549</td> <td>    1.628</td> <td> 0.104</td> <td>   -0.182</td> <td>    1.971</td>
</tr>
<tr>
  <th>country_fe_LEBANON</th>                  <td>    0.2168</td> <td>    0.615</td> <td>    0.352</td> <td> 0.725</td> <td>   -0.989</td> <td>    1.422</td>
</tr>
<tr>
  <th>country_fe_LESOTHO</th>                  <td>   -1.5089</td> <td>    0.658</td> <td>   -2.295</td> <td> 0.022</td> <td>   -2.798</td> <td>   -0.220</td>
</tr>
<tr>
  <th>country_fe_LIBERIA</th>                  <td>    3.2042</td> <td>    0.788</td> <td>    4.067</td> <td> 0.000</td> <td>    1.660</td> <td>    4.748</td>
</tr>
<tr>
  <th>country_fe_LIBYAN ARAB JAMAHIRIYA</th>   <td>    1.4757</td> <td>    0.576</td> <td>    2.562</td> <td> 0.010</td> <td>    0.347</td> <td>    2.605</td>
</tr>
<tr>
  <th>country_fe_LITHUANIA</th>                <td>    1.1799</td> <td>    0.560</td> <td>    2.107</td> <td> 0.035</td> <td>    0.082</td> <td>    2.277</td>
</tr>
<tr>
  <th>country_fe_LUXEMBURG</th>                <td>   -1.7115</td> <td>    0.626</td> <td>   -2.734</td> <td> 0.006</td> <td>   -2.939</td> <td>   -0.484</td>
</tr>
<tr>
  <th>country_fe_MACAU</th>                    <td>   -3.3526</td> <td>    0.697</td> <td>   -4.810</td> <td> 0.000</td> <td>   -4.719</td> <td>   -1.987</td>
</tr>
<tr>
  <th>country_fe_MADAGASKAR</th>               <td>    0.3656</td> <td>    0.669</td> <td>    0.547</td> <td> 0.585</td> <td>   -0.945</td> <td>    1.676</td>
</tr>
<tr>
  <th>country_fe_MALAWI</th>                   <td>    1.1928</td> <td>    0.604</td> <td>    1.974</td> <td> 0.048</td> <td>    0.008</td> <td>    2.377</td>
</tr>
<tr>
  <th>country_fe_MALI</th>                     <td>    1.5867</td> <td>    0.683</td> <td>    2.323</td> <td> 0.020</td> <td>    0.248</td> <td>    2.925</td>
</tr>
<tr>
  <th>country_fe_MALTA</th>                    <td>    0.3692</td> <td>    0.667</td> <td>    0.554</td> <td> 0.580</td> <td>   -0.938</td> <td>    1.676</td>
</tr>
<tr>
  <th>country_fe_MAROCCO</th>                  <td>    0.9948</td> <td>    0.625</td> <td>    1.591</td> <td> 0.112</td> <td>   -0.231</td> <td>    2.220</td>
</tr>
<tr>
  <th>country_fe_MARSHALL ISLANDS</th>         <td>    1.4335</td> <td>    0.995</td> <td>    1.440</td> <td> 0.150</td> <td>   -0.517</td> <td>    3.384</td>
</tr>
<tr>
  <th>country_fe_MAURITANIA</th>               <td>    2.7633</td> <td>    0.674</td> <td>    4.103</td> <td> 0.000</td> <td>    1.443</td> <td>    4.083</td>
</tr>
<tr>
  <th>country_fe_MAURITIUS</th>                <td>   -0.2280</td> <td>    0.620</td> <td>   -0.368</td> <td> 0.713</td> <td>   -1.444</td> <td>    0.988</td>
</tr>
<tr>
  <th>country_fe_MEXICO</th>                   <td>   -1.1895</td> <td>    0.871</td> <td>   -1.365</td> <td> 0.172</td> <td>   -2.898</td> <td>    0.519</td>
</tr>
<tr>
  <th>country_fe_MOLDOVA, REPUBLIC OF</th>     <td>   -1.1614</td> <td>    0.833</td> <td>   -1.395</td> <td> 0.163</td> <td>   -2.793</td> <td>    0.470</td>
</tr>
<tr>
  <th>country_fe_MONGOLIA</th>                 <td>   -3.6615</td> <td>    1.155</td> <td>   -3.169</td> <td> 0.002</td> <td>   -5.926</td> <td>   -1.397</td>
</tr>
<tr>
  <th>country_fe_MOZAMBIQUE</th>               <td>    0.5349</td> <td>    0.503</td> <td>    1.063</td> <td> 0.288</td> <td>   -0.452</td> <td>    1.521</td>
</tr>
<tr>
  <th>country_fe_MYANMAR</th>                  <td>   -2.7854</td> <td>    0.774</td> <td>   -3.600</td> <td> 0.000</td> <td>   -4.302</td> <td>   -1.269</td>
</tr>
<tr>
  <th>country_fe_NAMIBIA</th>                  <td>    0.8391</td> <td>    0.551</td> <td>    1.524</td> <td> 0.128</td> <td>   -0.240</td> <td>    1.918</td>
</tr>
<tr>
  <th>country_fe_NEPAL</th>                    <td>   -3.5180</td> <td>    1.352</td> <td>   -2.602</td> <td> 0.009</td> <td>   -6.168</td> <td>   -0.869</td>
</tr>
<tr>
  <th>country_fe_NETHERLANDS</th>              <td>   -2.6678</td> <td>    0.822</td> <td>   -3.244</td> <td> 0.001</td> <td>   -4.280</td> <td>   -1.056</td>
</tr>
<tr>
  <th>country_fe_NEW ZEALAND</th>              <td>   -2.1391</td> <td>    0.611</td> <td>   -3.502</td> <td> 0.000</td> <td>   -3.337</td> <td>   -0.942</td>
</tr>
<tr>
  <th>country_fe_NICARAGUA</th>                <td>    2.4747</td> <td>    0.814</td> <td>    3.039</td> <td> 0.002</td> <td>    0.879</td> <td>    4.071</td>
</tr>
<tr>
  <th>country_fe_NIGERIA</th>                  <td>   -0.8554</td> <td>    0.758</td> <td>   -1.129</td> <td> 0.259</td> <td>   -2.340</td> <td>    0.630</td>
</tr>
<tr>
  <th>country_fe_NORWAY</th>                   <td>   -1.8189</td> <td>    0.759</td> <td>   -2.396</td> <td> 0.017</td> <td>   -3.307</td> <td>   -0.331</td>
</tr>
<tr>
  <th>country_fe_OMAN</th>                     <td>    0.0868</td> <td>    0.727</td> <td>    0.119</td> <td> 0.905</td> <td>   -1.338</td> <td>    1.511</td>
</tr>
<tr>
  <th>country_fe_PAKISTAN</th>                 <td>   -1.9681</td> <td>    0.753</td> <td>   -2.613</td> <td> 0.009</td> <td>   -3.444</td> <td>   -0.492</td>
</tr>
<tr>
  <th>country_fe_PANAMA</th>                   <td>    1.8940</td> <td>    0.606</td> <td>    3.125</td> <td> 0.002</td> <td>    0.706</td> <td>    3.082</td>
</tr>
<tr>
  <th>country_fe_PARAGUAY</th>                 <td>    1.9121</td> <td>    0.626</td> <td>    3.053</td> <td> 0.002</td> <td>    0.684</td> <td>    3.140</td>
</tr>
<tr>
  <th>country_fe_PERU</th>                     <td>   -1.0463</td> <td>    0.649</td> <td>   -1.612</td> <td> 0.107</td> <td>   -2.319</td> <td>    0.226</td>
</tr>
<tr>
  <th>country_fe_PHILIPPINES</th>              <td>   -3.7168</td> <td>    0.900</td> <td>   -4.128</td> <td> 0.000</td> <td>   -5.482</td> <td>   -1.952</td>
</tr>
<tr>
  <th>country_fe_POLAND</th>                   <td>   -1.6215</td> <td>    0.761</td> <td>   -2.130</td> <td> 0.033</td> <td>   -3.114</td> <td>   -0.130</td>
</tr>
<tr>
  <th>country_fe_PORTUGAL</th>                 <td>   -1.5515</td> <td>    0.699</td> <td>   -2.219</td> <td> 0.026</td> <td>   -2.922</td> <td>   -0.181</td>
</tr>
<tr>
  <th>country_fe_PUERTO RICO</th>              <td>    1.0642</td> <td>    0.644</td> <td>    1.653</td> <td> 0.098</td> <td>   -0.197</td> <td>    2.326</td>
</tr>
<tr>
  <th>country_fe_QATAR</th>                    <td>    0.0772</td> <td>    0.680</td> <td>    0.113</td> <td> 0.910</td> <td>   -1.256</td> <td>    1.411</td>
</tr>
<tr>
  <th>country_fe_REP. OF MACEDONIA</th>        <td>   -0.6957</td> <td>    0.630</td> <td>   -1.105</td> <td> 0.269</td> <td>   -1.930</td> <td>    0.539</td>
</tr>
<tr>
  <th>country_fe_RUSSIA</th>                   <td>   -1.5519</td> <td>    0.973</td> <td>   -1.595</td> <td> 0.111</td> <td>   -3.459</td> <td>    0.356</td>
</tr>
<tr>
  <th>country_fe_RWANDA</th>                   <td>   -0.6205</td> <td>    1.122</td> <td>   -0.553</td> <td> 0.580</td> <td>   -2.819</td> <td>    1.578</td>
</tr>
<tr>
  <th>country_fe_SAINT KITTS AND NEVIS</th>    <td>    3.7861</td> <td>    0.970</td> <td>    3.903</td> <td> 0.000</td> <td>    1.885</td> <td>    5.687</td>
</tr>
<tr>
  <th>country_fe_SAINT LUCIA</th>              <td>    2.4708</td> <td>    0.888</td> <td>    2.782</td> <td> 0.005</td> <td>    0.730</td> <td>    4.212</td>
</tr>
<tr>
  <th>country_fe_SAMOA</th>                    <td>    0.7636</td> <td>    1.075</td> <td>    0.710</td> <td> 0.477</td> <td>   -1.343</td> <td>    2.870</td>
</tr>
<tr>
  <th>country_fe_SAO TOME AND PRINCIPE</th>    <td>   -3.4500</td> <td>    1.057</td> <td>   -3.265</td> <td> 0.001</td> <td>   -5.521</td> <td>   -1.379</td>
</tr>
<tr>
  <th>country_fe_SAUDI ARABIA</th>             <td>   -0.8471</td> <td>    0.802</td> <td>   -1.056</td> <td> 0.291</td> <td>   -2.420</td> <td>    0.726</td>
</tr>
<tr>
  <th>country_fe_SENEGAL</th>                  <td>    1.7053</td> <td>    0.581</td> <td>    2.933</td> <td> 0.003</td> <td>    0.566</td> <td>    2.845</td>
</tr>
<tr>
  <th>country_fe_SEYCHELLES</th>               <td>   -7.1690</td> <td>    0.736</td> <td>   -9.737</td> <td> 0.000</td> <td>   -8.612</td> <td>   -5.726</td>
</tr>
<tr>
  <th>country_fe_SIERRA LEONE</th>             <td>    2.6239</td> <td>    0.715</td> <td>    3.668</td> <td> 0.000</td> <td>    1.222</td> <td>    4.026</td>
</tr>
<tr>
  <th>country_fe_SINGAPORE</th>                <td>   -7.8383</td> <td>    1.210</td> <td>   -6.478</td> <td> 0.000</td> <td>  -10.210</td> <td>   -5.467</td>
</tr>
<tr>
  <th>country_fe_SLOVAKIA</th>                 <td>   -1.9957</td> <td>    0.576</td> <td>   -3.465</td> <td> 0.001</td> <td>   -3.124</td> <td>   -0.867</td>
</tr>
<tr>
  <th>country_fe_SLOVENIA</th>                 <td>   -2.4731</td> <td>    0.550</td> <td>   -4.500</td> <td> 0.000</td> <td>   -3.550</td> <td>   -1.396</td>
</tr>
<tr>
  <th>country_fe_SOLOMON ISLANDS</th>          <td>   -1.6206</td> <td>    0.828</td> <td>   -1.956</td> <td> 0.050</td> <td>   -3.244</td> <td>    0.003</td>
</tr>
<tr>
  <th>country_fe_SOUTH AFRICA</th>             <td>   -1.3349</td> <td>    0.718</td> <td>   -1.860</td> <td> 0.063</td> <td>   -2.742</td> <td>    0.072</td>
</tr>
<tr>
  <th>country_fe_SPAIN</th>                    <td>   -2.3184</td> <td>    0.904</td> <td>   -2.563</td> <td> 0.010</td> <td>   -4.091</td> <td>   -0.546</td>
</tr>
<tr>
  <th>country_fe_SRI LANKA</th>                <td>   -4.6596</td> <td>    0.689</td> <td>   -6.764</td> <td> 0.000</td> <td>   -6.010</td> <td>   -3.309</td>
</tr>
<tr>
  <th>country_fe_SUDAN</th>                    <td>    0.4152</td> <td>    0.551</td> <td>    0.754</td> <td> 0.451</td> <td>   -0.665</td> <td>    1.495</td>
</tr>
<tr>
  <th>country_fe_SURINAME</th>                 <td>    3.2029</td> <td>    0.764</td> <td>    4.192</td> <td> 0.000</td> <td>    1.705</td> <td>    4.700</td>
</tr>
<tr>
  <th>country_fe_SWAZILAND</th>                <td>   -1.0519</td> <td>    0.623</td> <td>   -1.689</td> <td> 0.091</td> <td>   -2.272</td> <td>    0.169</td>
</tr>
<tr>
  <th>country_fe_SWEDEN</th>                   <td>   -2.2875</td> <td>    0.762</td> <td>   -3.001</td> <td> 0.003</td> <td>   -3.781</td> <td>   -0.794</td>
</tr>
<tr>
  <th>country_fe_SWITZERLAND</th>              <td>   -2.9224</td> <td>    0.796</td> <td>   -3.672</td> <td> 0.000</td> <td>   -4.482</td> <td>   -1.362</td>
</tr>
<tr>
  <th>country_fe_TAIWAN</th>                   <td>   -5.3211</td> <td>    0.931</td> <td>   -5.717</td> <td> 0.000</td> <td>   -7.145</td> <td>   -3.497</td>
</tr>
<tr>
  <th>country_fe_TAJIKISTAN</th>               <td>    2.8975</td> <td>    0.638</td> <td>    4.540</td> <td> 0.000</td> <td>    1.647</td> <td>    4.148</td>
</tr>
<tr>
  <th>country_fe_TANZANIA, UNITED REP. OF</th> <td>   -0.0753</td> <td>    0.528</td> <td>   -0.143</td> <td> 0.887</td> <td>   -1.110</td> <td>    0.960</td>
</tr>
<tr>
  <th>country_fe_THAILAND</th>                 <td>   -4.9906</td> <td>    0.983</td> <td>   -5.079</td> <td> 0.000</td> <td>   -6.916</td> <td>   -3.065</td>
</tr>
<tr>
  <th>country_fe_TOGO</th>                     <td>    2.5262</td> <td>    0.702</td> <td>    3.598</td> <td> 0.000</td> <td>    1.150</td> <td>    3.902</td>
</tr>
<tr>
  <th>country_fe_TRINIDAD AND TOBAGO</th>      <td>    1.7423</td> <td>    0.885</td> <td>    1.969</td> <td> 0.049</td> <td>    0.008</td> <td>    3.477</td>
</tr>
<tr>
  <th>country_fe_TUNISIA</th>                  <td>   -0.1215</td> <td>    0.554</td> <td>   -0.219</td> <td> 0.826</td> <td>   -1.207</td> <td>    0.964</td>
</tr>
<tr>
  <th>country_fe_TURKEY</th>                   <td>   -2.4305</td> <td>    0.831</td> <td>   -2.926</td> <td> 0.003</td> <td>   -4.058</td> <td>   -0.803</td>
</tr>
<tr>
  <th>country_fe_TURKMENISTAN</th>             <td>   -0.1843</td> <td>    0.718</td> <td>   -0.257</td> <td> 0.797</td> <td>   -1.592</td> <td>    1.224</td>
</tr>
<tr>
  <th>country_fe_TUVALU</th>                   <td>    1.5304</td> <td>    1.344</td> <td>    1.139</td> <td> 0.255</td> <td>   -1.103</td> <td>    4.164</td>
</tr>
<tr>
  <th>country_fe_UGANDA</th>                   <td>    0.2314</td> <td>    0.566</td> <td>    0.409</td> <td> 0.683</td> <td>   -0.878</td> <td>    1.341</td>
</tr>
<tr>
  <th>country_fe_UKRAINE</th>                  <td>   -0.7418</td> <td>    0.624</td> <td>   -1.189</td> <td> 0.235</td> <td>   -1.965</td> <td>    0.481</td>
</tr>
<tr>
  <th>country_fe_UNITED ARAB EMIRAT</th>       <td>   -1.1745</td> <td>    0.775</td> <td>   -1.515</td> <td> 0.130</td> <td>   -2.694</td> <td>    0.345</td>
</tr>
<tr>
  <th>country_fe_UNITED KINGDOM</th>           <td>   -3.1306</td> <td>    1.010</td> <td>   -3.100</td> <td> 0.002</td> <td>   -5.110</td> <td>   -1.151</td>
</tr>
<tr>
  <th>country_fe_UNITED STATES</th>            <td>   -3.0327</td> <td>    1.279</td> <td>   -2.370</td> <td> 0.018</td> <td>   -5.540</td> <td>   -0.525</td>
</tr>
<tr>
  <th>country_fe_URUGUAY</th>                  <td>    0.5274</td> <td>    0.788</td> <td>    0.669</td> <td> 0.504</td> <td>   -1.018</td> <td>    2.072</td>
</tr>
<tr>
  <th>country_fe_UZBEKISTAN</th>               <td>   -1.8922</td> <td>    0.563</td> <td>   -3.363</td> <td> 0.001</td> <td>   -2.995</td> <td>   -0.789</td>
</tr>
<tr>
  <th>country_fe_VENEZUELA</th>                <td>    1.8393</td> <td>    0.785</td> <td>    2.344</td> <td> 0.019</td> <td>    0.301</td> <td>    3.377</td>
</tr>
<tr>
  <th>country_fe_VIET NAM</th>                 <td>   -4.4794</td> <td>    0.880</td> <td>   -5.091</td> <td> 0.000</td> <td>   -6.204</td> <td>   -2.755</td>
</tr>
<tr>
  <th>country_fe_YEMEN</th>                    <td>   -2.2397</td> <td>    0.604</td> <td>   -3.705</td> <td> 0.000</td> <td>   -3.424</td> <td>   -1.055</td>
</tr>
<tr>
  <th>isic2_fe_</th>                           <td>    0.6834</td> <td>    0.094</td> <td>    7.247</td> <td> 0.000</td> <td>    0.499</td> <td>    0.868</td>
</tr>
<tr>
  <th>isic2_fe_15</th>                         <td>    1.0921</td> <td>    0.131</td> <td>    8.337</td> <td> 0.000</td> <td>    0.835</td> <td>    1.349</td>
</tr>
<tr>
  <th>isic2_fe_16</th>                         <td>    0.9401</td> <td>    0.236</td> <td>    3.981</td> <td> 0.000</td> <td>    0.477</td> <td>    1.403</td>
</tr>
<tr>
  <th>isic2_fe_17</th>                         <td>    1.0258</td> <td>    0.121</td> <td>    8.456</td> <td> 0.000</td> <td>    0.788</td> <td>    1.264</td>
</tr>
<tr>
  <th>isic2_fe_18</th>                         <td>    0.2840</td> <td>    0.102</td> <td>    2.790</td> <td> 0.005</td> <td>    0.085</td> <td>    0.483</td>
</tr>
<tr>
  <th>isic2_fe_19</th>                         <td>   -0.7478</td> <td>    0.117</td> <td>   -6.404</td> <td> 0.000</td> <td>   -0.977</td> <td>   -0.519</td>
</tr>
<tr>
  <th>isic2_fe_20</th>                         <td>   -1.8403</td> <td>    0.131</td> <td>  -14.100</td> <td> 0.000</td> <td>   -2.096</td> <td>   -1.584</td>
</tr>
<tr>
  <th>isic2_fe_21</th>                         <td>    0.4099</td> <td>    0.121</td> <td>    3.380</td> <td> 0.001</td> <td>    0.172</td> <td>    0.648</td>
</tr>
<tr>
  <th>isic2_fe_22</th>                         <td>   -0.3420</td> <td>    0.165</td> <td>   -2.070</td> <td> 0.038</td> <td>   -0.666</td> <td>   -0.018</td>
</tr>
<tr>
  <th>isic2_fe_23</th>                         <td>   -0.8543</td> <td>    0.269</td> <td>   -3.174</td> <td> 0.002</td> <td>   -1.382</td> <td>   -0.327</td>
</tr>
<tr>
  <th>isic2_fe_24</th>                         <td>    0.9828</td> <td>    0.107</td> <td>    9.222</td> <td> 0.000</td> <td>    0.774</td> <td>    1.192</td>
</tr>
<tr>
  <th>isic2_fe_25</th>                         <td>    0.2573</td> <td>    0.118</td> <td>    2.181</td> <td> 0.029</td> <td>    0.026</td> <td>    0.489</td>
</tr>
<tr>
  <th>isic2_fe_26</th>                         <td>   -0.0824</td> <td>    0.126</td> <td>   -0.653</td> <td> 0.514</td> <td>   -0.330</td> <td>    0.165</td>
</tr>
<tr>
  <th>isic2_fe_27</th>                         <td>    2.1734</td> <td>    0.108</td> <td>   20.078</td> <td> 0.000</td> <td>    1.961</td> <td>    2.386</td>
</tr>
<tr>
  <th>isic2_fe_28</th>                         <td>    0.7762</td> <td>    0.133</td> <td>    5.842</td> <td> 0.000</td> <td>    0.516</td> <td>    1.037</td>
</tr>
<tr>
  <th>isic2_fe_29</th>                         <td>    0.6114</td> <td>    0.122</td> <td>    5.000</td> <td> 0.000</td> <td>    0.372</td> <td>    0.851</td>
</tr>
<tr>
  <th>isic2_fe_30</th>                         <td>   -0.9750</td> <td>    0.339</td> <td>   -2.874</td> <td> 0.004</td> <td>   -1.640</td> <td>   -0.310</td>
</tr>
<tr>
  <th>isic2_fe_31</th>                         <td>    0.7240</td> <td>    0.106</td> <td>    6.822</td> <td> 0.000</td> <td>    0.516</td> <td>    0.932</td>
</tr>
<tr>
  <th>isic2_fe_32</th>                         <td>    0.8617</td> <td>    0.152</td> <td>    5.659</td> <td> 0.000</td> <td>    0.563</td> <td>    1.160</td>
</tr>
<tr>
  <th>isic2_fe_33</th>                         <td>    2.6663</td> <td>    0.165</td> <td>   16.129</td> <td> 0.000</td> <td>    2.342</td> <td>    2.990</td>
</tr>
<tr>
  <th>isic2_fe_34</th>                         <td>    0.7941</td> <td>    0.107</td> <td>    7.407</td> <td> 0.000</td> <td>    0.584</td> <td>    1.004</td>
</tr>
<tr>
  <th>isic2_fe_35</th>                         <td>    0.4387</td> <td>    0.107</td> <td>    4.089</td> <td> 0.000</td> <td>    0.228</td> <td>    0.649</td>
</tr>
</table>




```python

```
