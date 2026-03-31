---
title: "Daily COVID-19 Testing in Indonesia"
categories: [coronavirus COVID-19]
tags: [coronavirus COVID-19, python]
authors: [admin]
date: '2020-05-31'
---

The government seems increasingly eager to usher in the "New Normal" and start reopening the economy. A guidebook on how to handle the "New Normal" [from BPOM](https://investor.id/lifestyle/bpom-menerbitkan-buku-panduan-lengkap-covid19) has already been circulated. News about malls reopening was everywhere (though apparently [Summarecon Mal Bekasi did not open after all](https://metro.tempo.co/read/1346375/ini-agenda-presiden-jokowi-ke-bekasi-siang-ini-bukan-buka-mal)). The economy was set to bounce back!

According to many sources ([for example, this one](https://www.abc.net.au/indonesian/2020-05-27/who-mengatakan-gelombang-pertama-covid-19-masih-tinggi/12291202)), the key to a successful economic reopening is a high growth rate of daily testing -- in other words, massive testing. But have we actually achieved sufficient massive testing?


```python
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
c=pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
c['date']=pd.to_datetime(c['date'])
y=c['new_tests'][c['iso_code']=='IDN']
y1=c['new_tests_smoothed'][c['iso_code']=='IDN']
x=c['date'][c['iso_code']=='IDN']
plt.figure(figsize=(15,5))
#nt=sns.load_dataset("c")
sns.lineplot(x=x, y=y, data=c)
sns.lineplot(x=x, y=y1, data=c)
```

![png](/images/output_1_1.png)


The chart above shows the number of "new tests" per day. The data is taken from [Our World in Data](https://ourworldindata.org/coronavirus-data). It is updated daily based on government reports. The x-axis shows the date, while the y-axis represents the variable "new_tests" from the original dataset. In short, this is the daily test count.

The dots and the thin line show the raw daily test numbers, while the blue line shows the smoothed new tests.

As a brief aside, the code above was run on Python 3.7. The data is read directly from Our World in Data's online portal, so every time you run it, you get the latest figures. If you have Python on your machine, feel free to copy the code above to see the most current data.

Indonesia's daily testing clearly has a lot of gaps, and up until 26 May 2020, the daily test count was still very volatile. The ups and downs are somewhat random. Some opinions I have seen on Twitter suggest that daily test counts are hard to predict because they depend not only on the number of swabs conducted but also on the queue of samples at laboratories. So the numbers reported on a given day may actually be the results of swabs taken the day before.

I have not followed the COVID-19 testing debate too closely, to be honest. I had not updated on COVID-19 in a while, but the sudden buzz around reopening the economy piqued my curiosity. Also, Bio Farma reportedly succeeded in producing its own PCR test kits, [claiming it can produce 100,000 per day](https://tirto.id/jokowi-klaim-indonesia-produksi-alat-rapid-tes-pcr-100-ribu-hari-fzhZ). Assuming smooth logistics to labs and sufficient lab capacity, massive testing should be achievable. Hopefully this upward trend continues and remains sustainable during the New Normal.

By the way, the data comes from the central government, and the central government's data reflects its own testing plus tests conducted by regional governments (and perhaps private entities). Although we do not have data beyond the central government's reports, at least regional governments know their own numbers.

Also, other countries have somewhat erratic "new tests" data as well. New Zealand and Malaysia are also volatile, while Japan does not report daily new tests (though cumulative totals are available). Vietnam's data suddenly drops and disappears midway. So perhaps this is why President Jokowi felt so confident.


```python
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
c=pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
c['date']=pd.to_datetime(c['date'])
plt.figure(figsize=(15,10))
#cn=c.drop(c[(c['iso_code'] != 'IDN')| c[(c['iso_code'] != 'VNM') | c[(c['iso_code'] != 'SGP') | c[(c['iso_code'] != 'AUS') | c[(c['iso_code'] != 'MYS')].index)
cn=c[(c['iso_code'] == 'IDN') | (c['iso_code'] == 'VNM') | (c['iso_code'] == 'MYS') | (c['iso_code'] == 'JPN') | (c['iso_code'] == 'NZL')]
sns.lineplot(x="date", y="new_tests", hue="iso_code", style="iso_code",data=cn)
```

![png](/images/output_3_1.png)


Here I used raw daily tests, not daily tests per 1,000 population. If I used the per-capita measure, other countries would be so far above that Indonesia would look like a flat line. Anyway, I was trying to use the argument that "we are confident enough to reopen because testing capacity has been ramped up." Using this argument, Indonesia's upward trend does look reasonable. Whether it is sufficient or not, of course, is still a matter of debate -- and I am sure many others have already weighed in.

In closing, there are of course many reasons behind the decision to reopen the economy, not just testing. I am not trying to discuss those other reasons. This post was simply meant to provide a brief snapshot of how Indonesia's daily testing has been progressing. I will leave the rest to the experts.
