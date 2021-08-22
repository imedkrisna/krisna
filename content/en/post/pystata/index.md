---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Awesome Stata 17 Upgrade: Trying Pystata by using PPML on USITC and WITS database"
subtitle: ""
summary: "Finally I got to upgrade my stata to Stata 17! I was looking forward to using Stata in my Python environment. This post is just me trying a PPML package (Stata, not the USITC one)"
authors: [admin]
tags: [trade, econometrics, python, Stata]
categories: [trade, econometrics, python, Stata]
date: 2021-08-22T20:39:04+10:00
lastmod: 2021-08-22T20:39:04+10:00
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

Finally got my hand on [Stata 17](https://www.stata.com/stata-news/news36-2/). When I got my email about Stata 17, I was very excited on the new PyStata feature. It allows for calling python from Stata and calling Stata from Python. There are many other cool upgrades on Stata 17 especially for Macroeconometrician, but the PyStata is especially interesting for me!

It doesn't take long for me to try using PyStata on my Jupyter Lab. While using Python on Stata is certainly super interesting, I of course like better using Stata on Jupyter. I write things from Jupyter (like this post), so running things straight from Jupyter would be super awesome. While there are many things we can do with Python, it's still hard for me to say goodbye to Stata. For one, I use packages like [Levinsohn-Petrin](https://www.stata-journal.com/article.html?article=st0060) algorithm for my research. Moreover, Stata still has plenty of familiarity for my own compared with Pandas. Lastly, most of my colleagues don't even speak python or r, so Stata remains to be my main tool for collaboration.

So this post is dedicated to myself being super excited to Trying PyStata for the first time! As a trade economist, what's best but to start with some trade data? In this post, I take data from the internet with Pandas, then transfer it to Stata database (you know, the .dta), and then run a PPML a la [Silva and Tenreyro](https://ideas.repec.org/c/boc/bocode/s458102.html). Yes there is a PPML package for Python called [GME](https://www.usitc.gov/data/gravity/gme.htm) (I even [blogged about it](https://www.krisna.or.id/en/post/ppml/)) but come on I am having fun with PyStata here!

There is of course a better [starting place to read](https://www.stata.com/python/pystata/notebook/Quick%20Start0.html) if you really want to go on with playing with your PyStata, but I hope this post is fun and useful enuff four you.

Since this post is all about using Stata command in Python environment (and not the other way around), I mainly use Stata Magic. Maybe if I manage to use Mata Magic and PyStata Magic I will blog about it as well but the Stata Magic is what I am super excited about for now.

Okay lets go on to the show!

## Installing PyStata

obviously the first thing you should do is to have Stata 17 installed on your computer. Remember where it is installed (it will be used later) but if you just click `next` like I do then it's gonna be in `C:/Program Files/Stata17/`. When we're done installing Stata 17, then all we need to do is to install PyStata in our env using

```Python
pip install --upgrade --user stata_setup
```
Then we're good to go!

## Collecting the data (in Pandas)

I am using publicly available data for this post so everyone can try this. No, not car, don't worry.

Since this will be about gravity regression, I will need gravity data. Let's get it from [USITC Dynamic Gravity Dataset](https://www.usitc.gov/data/gravity/dgd.htm) for our trial here. Be mindful of the size, this dataset is suuuuuuuuuper huge!


```python
weqs=pd.read_csv('https://www.usitc.gov/data/gravity/dgd_docs/release_2.1_2000_2016.zip')
weqs.columns # checking its variables
```




    Index(['year', 'country_o', 'iso3_o', 'dynamic_code_o', 'country_d', 'iso3_d',
           'dynamic_code_d', 'colony_of_destination_ever', 'colony_of_origin_ever',
           'colony_ever', 'common_colonizer', 'common_legal_origin', 'contiguity',
           'distance', 'member_gatt_o', 'member_wto_o', 'member_eu_o',
           'member_gatt_d', 'member_wto_d', 'member_eu_d', 'member_gatt_joint',
           'member_wto_joint', 'member_eu_joint', 'lat_o', 'lng_o', 'lat_d',
           'lng_d', 'landlocked_o', 'island_o', 'region_o', 'landlocked_d',
           'island_d', 'region_d', 'agree_pta_goods', 'agree_pta_services',
           'agree_fta', 'agree_eia', 'agree_cu', 'agree_psa', 'agree_fta_eia',
           'agree_cu_eia', 'agree_pta', 'capital_const_d', 'capital_const_o',
           'capital_cur_d', 'capital_cur_o', 'gdp_pwt_const_d', 'gdp_pwt_const_o',
           'gdp_pwt_cur_d', 'gdp_pwt_cur_o', 'pop_d', 'pop_o', 'hostility_level_o',
           'hostility_level_d', 'common_language', 'polity_o', 'polity_d',
           'sanction_threat', 'sanction_threat_trade', 'sanction_imposition',
           'sanction_imposition_trade', 'gdp_wdi_cur_o', 'gdp_wdi_cap_cur_o',
           'gdp_wdi_const_o', 'gdp_wdi_cap_const_o', 'gdp_wdi_cur_d',
           'gdp_wdi_cap_cur_d', 'gdp_wdi_const_d', 'gdp_wdi_cap_const_d'],
          dtype='object')



Since this is a test, I will use just some of the variable. First, I will only use Indonesia as a country of origin. Secondly, I will only use cross-section in the year 2016. Next, only several variable will be used, namely, export partner's population, GDP and distance, as well as FTA with Indonesia. Obviously there are more stuff needs to be added if you want to do a real gravity analysis but this is just a test come on.


```python
grav=weqs.query('country_o == "Indonesia"') # take only Indonesia as a country of origin
grav=grav.query('year==2016') # take only year 2016
grav=grav[['country_d','pop_d', 'agree_fta', 'gdp_wdi_cur_d', 'distance']] # take some variables only
grav=grav.rename(columns={'country_d':'Partner'})
grav.head() # check content
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
      <th>Partner</th>
      <th>pop_d</th>
      <th>agree_fta</th>
      <th>gdp_wdi_cur_d</th>
      <th>distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>455937</th>
      <td>Aruba</td>
      <td>0.104822</td>
      <td>0.0</td>
      <td>2.646927e+09</td>
      <td>18924.247763</td>
    </tr>
    <tr>
      <th>455954</th>
      <td>Afghanistan</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1.936264e+10</td>
      <td>6158.679225</td>
    </tr>
    <tr>
      <th>455971</th>
      <td>Angola</td>
      <td>28.813463</td>
      <td>0.0</td>
      <td>1.011239e+11</td>
      <td>10483.002562</td>
    </tr>
    <tr>
      <th>455988</th>
      <td>Anguilla</td>
      <td>0.014764</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>18167.048245</td>
    </tr>
    <tr>
      <th>456005</th>
      <td>Aland Islands</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>10410.128664</td>
    </tr>
  </tbody>
</table>
</div>



Now that i have the gravity variables, let's get the trade data. I will need Indonesia's export value to partners as well as their import tariff. Again, we normally need to do more rigorous check on the export and tariff, but since this is just a test, I will use total export as well as MFN weighted average tariff.

To get from WITS i use [world_trade_data](https://mwouts.github.io/world_trade_data/) package in python.


```python
import world_trade_data as wits
```


```python
# Grabbing Indonesia's export value to partners in 2016
exports = wits.get_indicator('XPRT-TRD-VL', reporter='idn',partner='all', year='2016',product='Total')
```


```python
exports=exports.reset_index()
exports=exports[['Partner','Value']] # Take only necessary columns
exports=exports.rename(columns={'Value':'Export_Value'}) # rename to merge later
```


```python
# Grabbing tariff from Indonesia's partners
tariff=wits.get_indicator('MFN-WGHTD-AVRG',reporter='all',year='2016',datasource='tradestats-tariff',product='Total')
tariff=tariff.reset_index()
tariff=tariff[['Reporter','Value']] # take only necessary columns
tariff=tariff.rename(columns={"Reporter": "Partner","Value":"Tariff"}) # rename to merge later
```


```python
trade=pd.merge(exports,tariff,how='left',on='Partner') # merge the two dataset
```

now that I have my trade,tariff and gravity data, lets merge them to get the final data to feed to our Stata PPML.


```python
idntrade=pd.merge(grav,trade,how='left',on='Partner')
idntrade['Export']=idntrade['Export_Value']/1000000
idntrade.head()
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
      <th>Partner</th>
      <th>pop_d</th>
      <th>agree_fta</th>
      <th>gdp_wdi_cur_d</th>
      <th>distance</th>
      <th>Export_Value</th>
      <th>Tariff</th>
      <th>Export</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aruba</td>
      <td>0.104822</td>
      <td>0.0</td>
      <td>2.646927e+09</td>
      <td>18924.247763</td>
      <td>878.469</td>
      <td>10.158305</td>
      <td>0.000878</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afghanistan</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1.936264e+10</td>
      <td>6158.679225</td>
      <td>16220.103</td>
      <td>NaN</td>
      <td>0.016220</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Angola</td>
      <td>28.813463</td>
      <td>0.0</td>
      <td>1.011239e+11</td>
      <td>10483.002562</td>
      <td>57713.955</td>
      <td>9.379807</td>
      <td>0.057714</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Anguilla</td>
      <td>0.014764</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>18167.048245</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aland Islands</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>10410.128664</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Well, obviously we can merge and cook our data ini Stata as well but as you can see it's kinda faster to do it in Pandas unless I need to generate anything new.

## Run a PPML in Stata

Now that the data's ready, we can begin running PPML in Stata! Now, we need to call Stata to our Python environment with the `import` command. This is where we need our Stata location.


```python
import stata_setup
stata_setup.config("C:/Program Files/Stata17/", "mp")
```

    
      ___  ____  ____  ____  ____ ©
     /__    /   ____/   /   ____/      17.0
    ___/   /   /___/   /   /___/       MP—Parallel Edition
    
     Statistics and Data Science       Copyright 1985-2021 StataCorp LLC
                                       StataCorp
                                       4905 Lakeway Drive
                                       College Station, Texas 77845 USA
                                       800-STATA-PC        https://www.stata.com
                                       979-696-4600        stata@stata.com

    

Next, we load the dataset to Stata! I use Stata magic to do this. there is also a possibility calling Stata with API like [this one](https://www.stata.com/python/pystata/notebook/Example5.html#) and [this one](https://www.stata.com/new-in-stata/pystata/), but in Jupyter, using magic is somewhat easier for me.

Now lets call the data and describe it.


```python
%%stata -d idntrade -force
describe
```

    
    Contains data
     Observations:           255                  
        Variables:             8                  
    -------------------------------------------------------------------------------
    Variable      Storage   Display    Value
        name         type    format    label      Variable label
    -------------------------------------------------------------------------------
    Partner         str45   %45s                  
    pop_d           double  %10.0g                
    agree_fta       double  %10.0g                
    gdp_wdi_cur_d   double  %10.0g                
    distance        double  %10.0g                
    Export_Value    double  %10.0g                
    Tariff          double  %10.0g                
    Export          double  %10.0g                
    -------------------------------------------------------------------------------
    Sorted by: 
         Note: Dataset has changed since last saved.
    

Wooohoo cool! Let's try summarize


```python
%%stata
su
```

    
        Variable |        Obs        Mean    Std. dev.       Min        Max
    -------------+---------------------------------------------------------
         Partner |          0
           pop_d |        183    42.87855    150.9889    .005152     1403.5
       agree_fta |        255    .0588235    .2357568          0          1
    gdp_wdi_cu~d |        206    5.25e+11    2.26e+12   3.65e+07   1.87e+13
        distance |        253    10594.37    4663.103   951.1062   19190.28
    -------------+---------------------------------------------------------
    Export_Value |        192    676920.4     2420380       .101   1.68e+07
          Tariff |        119    6.739741    4.004538          0   18.73486
          Export |        192    .6769204     2.42038   1.01e-07   16.78559
    

Awesome!! Now let's do our ppml command. 


```python
%%stata
ppml Export Tariff pop_d agree_fta gdp_wdi_cur_d distance
```

    note: checking the existence of the estimates
    WARNING: Tariff has very large values, consider rescaling  or recentering
    WARNING: pop_d has very large values, consider rescaling  or recentering
    WARNING: gdp_wdi_cur_d has very large values, consider rescaling  or recenterin
    > g
    WARNING: distance has very large values, consider rescaling  or recentering
    note: starting ppml estimation
    note: Export has noninteger values
    
    Iteration 1:   deviance =  118.6375
    Iteration 2:   deviance =  101.5413
    Iteration 3:   deviance =  101.0093
    Iteration 4:   deviance =  101.0082
    Iteration 5:   deviance =  101.0082
    
    Number of parameters: 6
    Number of observations: 114
    Number of observations dropped: 0
    Pseudo log-likelihood: -102.58858
    R-squared: .75786551
    ------------------------------------------------------------------------------
                 |               Robust
          Export | Coefficient  std. err.      z    P>|z|     [95% conf. interval]
    -------------+----------------------------------------------------------------
          Tariff |  -.0906943   .0542772    -1.67   0.095    -.1970757     .015687
           pop_d |  -.0002608   .0004712    -0.55   0.580    -.0011843    .0006626
       agree_fta |    2.28588   .5362387     4.26   0.000     1.234871    3.336888
    gdp_wdi_cu~d |   2.04e-13   3.58e-14     5.69   0.000     1.33e-13    2.74e-13
        distance |  -.0000199    .000065    -0.31   0.760    -.0001473    .0001075
           _cons |   -.488918   .7264721    -0.67   0.501    -1.912777    .9349412
    ------------------------------------------------------------------------------
    Number of regressors dropped to ensure that the estimates exist: 0
    Option strict is off
    

woohoo! The result is also great considering how under-specified the model is! High $R^2$ , Tariff is negative and strong, FTA and GDP are both highly important in determining foreign demand!

Now one thing I can't quite work out is to extract the information from the regression back to pandas. I usually just go with outreg and do it manually, but it's no fun if I can't integrate the regression result in my notebook.

What I can do is to export the result to csv and read it thru Pandas.


```python
%%stata
eststo
esttab using hehe.csv, plain replace wide
```

    
    . eststo
    (est1 stored)
    
    . esttab using hehe.csv, plain replace wide
    (output written to hehe.csv)
    
    . 
    


```python
dff=pd.read_csv('hehe.csv')
dff
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
      <th>Unnamed: 0</th>
      <th>est1</th>
      <th>Unnamed: 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>b</td>
      <td>t</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tariff</td>
      <td>-.0906943</td>
      <td>-1.670947</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pop_d</td>
      <td>-.0002608</td>
      <td>-.5535483</td>
    </tr>
    <tr>
      <th>3</th>
      <td>agree_fta</td>
      <td>2.28588</td>
      <td>4.262802</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gdp_wdi_cur_d</td>
      <td>2.04e-13</td>
      <td>5.688106</td>
    </tr>
    <tr>
      <th>5</th>
      <td>distance</td>
      <td>-.0000199</td>
      <td>-.3056529</td>
    </tr>
    <tr>
      <th>6</th>
      <td>_cons</td>
      <td>-.488918</td>
      <td>-.6730031</td>
    </tr>
    <tr>
      <th>7</th>
      <td>N</td>
      <td>114</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



The result is not the best so this is kinda bummer. But at least I have something. haha. There may be a better way to do this but let me look for it and post it later on. If you have a suggestion please mention me on twitter!

Anyway, that's it for now. I hope this post is enjoyable!
