---
layout: post
title: "Looking for the relationship between ministry budgets and industrial growth"
categories: [Economics]
tags: [Economics]
date: '2020-03-05'
author: admin
---

Hi everyone. In this post, I will continue from my previous post [on Industrial Policy](imedkrisna.github.io/evaluasi/) which argued that to advance the manufacturing sector, Indonesia needs more than just the Ministry of Industry. Could it be that the targets set by the Ministry of Industry are too macro -- not specific enough?

If those targets are indeed too macro, then the Ministry of Industry's programs likely will not have a significant effect on the very targets they set for themselves. There are two main problems with trying to regress this. First, the Ministry of Industry has many targets -- 8 in total. The solution is simple: I will just pick one. Lazy, I know. So I will use **Non-Oil-and-Gas Manufacturing Industry Growth**. This data can be [downloaded from BPS](https://bps.go.id/subject/11/produk-domestik-bruto--lapangan-usaha-.html#subjekViewTab3). Please check my previous post on industrial policy for context.

The second problem: what variable should represent "programs and activities carried out by the Ministry of Industry"? This is trickier because a government institution does many things -- issues (and maintains) regulations, provides subsidies perhaps, etc. Since it is complicated, I will use the simplest indicator: **the Ministry's budget (APBN)**. Fortunately, the Ministry of Industry is one of the most transparent ministries, so [its budget is easy to find](https://kemenperin.go.id/dipa).

## Data

As I mentioned above, the data sources are the Ministry of Industry's website and BPS. I have compiled the data, and if you want to replicate this, you can download it [here (.csv)](https://1drv.ms/u/s!AjelszXKKcms6T94R-qq7bKPQWKT?e=YEAbCy). I have embedded it at the bottom of this page for browsing. The time span is 2012-2018.

From BPS we get 15 types of industry. I only used 14 because the 15th is a residual "other industries" category. Why drop it? Because I don't know which ministry program it maps to.

From the Ministry of Industry's budget data, we can get fairly detailed information about budget allocations for each program. There are several programs listed, such as support programs, research, human resource development, etc., but only 3 appear to directly target industrial sectors. These 3 programs are agro-based industry, textiles/leather/etc., and metals/technology-based industry. I then mapped these 3 programs to the 14 industry groups from BPS.

Since the other programs are surely also important, I included them in the regression as well.

## Correlation Between Non-Oil Manufacturing Growth and Total Ministry Budget

First, we can check the relationship between the Ministry of Industry's total budget and non-oil manufacturing growth. For this regression, I use overall non-oil manufacturing growth (the average across 15 industries) against the Ministry's total budget (not by program). Here is the plotted data:

![alt](/images/reg.png)

The blue line (left scale) is industrial growth, the orange line (right scale) is the Ministry of Industry's budget in rupiah. Do you see a pattern? Negative? Positive? No connection? Using the `cor.test()` function gives $-0.55$. But to be sure, let me run a regression. The results are in table 1. The model:

$$
GROWTH_t = \alpha + \beta log(TOTAL APBN KEMENPERIN_t) + \epsilon_t
$$

###### Table 1: Correlation between log(total Ministry budget) and industrial growth
<table>
  <thead>
  <tr>
    <th>Variable</th>
    <th>coef.</th>
    <th>S.E.</th>
    <th>t</th>
    <th>Pr(>|t|)</th>
  </tr>
  </thead>
<tbody>
<tr>
  <td>log(total)</td>
  <td>-5.29</td>
  <td>3.43</td>
  <td>-1.54</td>
  <td>0.183</td>
</tr>
</tbody>
</table>

Looking at table 1, the correlation appears weak. Though the sign is negative. The coefficient says that if the Ministry of Industry's budget **increases by 100%**, industrial growth would **fall by 5.29** percentage points. That is big. A 5.29 pp drop from 2018 levels means negative growth. Conversely, if the Ministry's budget were zeroed out -- i.e., the Ministry abolished -- growth would rise by 5.29 pp. Please double-check in case I am misinterpreting! But relax, the t-value is small, so the correlation is weak. The result is **not significant**. Phew.

If I regress with $X=\text{(total Ministry budget)}$ and $Y=\text{industrial growth}$, the plot looks like this:

![alt](/images/logreg.png)

By the way, I ran this in [R](https://www.r-project.org/). Please check the code too in case I made a mistake. Here is the code:
```
library(car)
## load data
panel<-read.csv("C:/regperin/regperin.csv")
all<-read.csv("C:/regperin/regtotal.csv")

## regression
lsols<-lm(GROWTH~log(TOTAL),data=all)
summary(lsols)

## plot
plot(log(all$TOTAL),all$GROWTH,pch=19,xlab = "LOG MINISTRY BUDGET",ylab = "GROWTH NON OIL MANUFACTURING")
abline(lm(all$GROWTH~log(all$TOTAL)),lwd=3,col="red")
```

## Fixed Effects by Industry

This time we regress by individual industry. BPS divides manufacturing into about 14 types, overseen by 3 Directorates General of the Ministry of Industry (each DG runs 1 program). Since there are many DGs at the Ministry, I included budgets from the programs overseeing these 14 industries, as well as the Ministry's total budget. Results are in table 2. The model:

$$
GROWTH_{it} = \alpha + \beta log(program_{it}) + \gamma log(total_{t}) + \eta_i + \mu_{it} \label{2}
$$

There are 3 `log(program)` values for each year, mapped to 14 industry sectors $i$. The mapping is in the Excel file at the bottom. I created the mapping based on the program types in the Ministry's budget data. My mapping may not be entirely valid.

###### Table 2: Correlation by industry
<table>
  <col>
  <colgroup span="3"></colgroup>
  <colgroup span="3"></colgroup>
  <thead>
  <tr>
    <th>Variable</th>
    <th colspan="4" scope="colgroup">Pooled ($\eta_i=0 \: \forall \: i$)</th>
    <th colspan="4" scope="colgroup">Fixed effect</th>
  </tr>
  <tr>
    <th></th>
    <th scope="col">coef.</th>
    <th scope="col">S.E.</th>
    <th scope="col">t</th>
    <th scope="col">Pr(>|t|)</th>
    <th scope="col">coef.</th>
    <th scope="col">S.E.</th>
    <th scope="col">t</th>
    <th scope="col">Pr(>|t|)</th>
    </tr>
</thead>
<tbody>
<tr>
  <td>Log(program)</td>
  <td>-0.55</td>
  <td>0.33</td>
  <td>-1.64</td>
  <td>0.10</td>
  <td>-0.53</td>
  <td>1.15</td>
  <td>-0.46</td>
  <td>0.64</td>
</tr>
<tr>
  <td>Log(total)</td>
  <td>-1.14</td>
  <td>5.08</td>
  <td>-0.23</td>
  <td>0.82</td>
  <td>-1.15</td>
  <td>4.95</td>
  <td>-0.23</td>
  <td>0.82</td>
</tr>
</tbody>
</table>

I used 2 models: pooled and fixed effects. For the pooled panel data regression, the result is negative and significant at $\alpha=10\%$. The magnitude is much smaller than the aggregate regression. If the program were **eliminated** (budget cut by 100%), the industry it oversees would **grow** by 0.55 percentage points. But when controlling for individual effects (adding fixed effects), **significance disappears**. Phew. This means the effect varies substantially across industries. Something industry-specific matters more, but it is not the Ministry's budget.

Code:
```
### pooled
lols<-lm(growth~log(APBN)+log(TOTAL),data=panel)

### fixed effect
library(plm)
lfixed<-plm(growth~log(APBN)+log(TOTAL),data=panel, index=c("id","year"),method="within")
```

Is the code correct? Anyway, this was pretty fun and did not take long. It is a nice exercise if you want to play around with regressions. Maybe you could try it with another ministry's data.

## Why This Cannot Be Directly Interpreted

By the way, this model has a LOT of caveats. It cannot be directly interpreted, especially for those of you who are anti-big-government pro-neoliberal types. Does a negative correlation mean abolishing the Ministry would boost industry? Does insignificance mean giving money to the Ministry is useless?

If you are playing with a model to make policy recommendations, you need to be very, very, very **very careful**. Before blaming others (the government? SJWs? labor? capitalism?), make sure you (and your model) are correct! And of course, my model needs to be critiqued first before I can critique anyone else.

This regression is extremely simple. The problems are surely numerous. If it were this easy, I would have nominated myself for minister by now. For statisticians, the problems with this simple model are immediately apparent. First, there is *endogeneity* (the budget is almost certainly not exogenous), and second, the error term probably is not normally distributed. If you dig further you will find more problems, but at least I can say two things.

First, this experiment does not appear to disprove my hypothesis. What hypothesis? That industrial growth is perhaps not the right indicator for the Ministry of Industry to target. The Ministry certainly has more specific indicators in its strategic plan, but there should be studies linking those specific indicators to the macro targets, and this link should be proven.

Second, what I have done in this blog post could serve as an opening chapter for an economics thesis. Impact studies of government programs on performance indicators seem to be rare at the Ministry of Industry, and they have strong potential as thesis topics. The Ministry has joint master's programs with several domestic and international universities, some in economics. If done as a master's thesis, the methods would surely be more sophisticated, with more and better-chosen variables.

For now, this post is good for learning basic regression or for speculation. Here is one response from my friend Risetio about this regression:

<blockquote class="twitter-tweet"><p lang="in" dir="ltr">Kalau liat dari model ekonometriknya, residualnya mungkin justru yg punya pengaruh terbesar ke pdb industri non migas, bukan anggaran kemenperin. Pertanyaannya, variabel apakah itu yg seharusnya bukan di residual?</p>&mdash; Risetioz (@risetioz) <a href="https://twitter.com/risetioz/status/1235521681889693698?ref_src=twsrc%5Etfw">March 5, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

What do you think? Drop in the comments!

<iframe src="https://onedrive.live.com/embed?cid=ACC929CA35B3A537&resid=ACC929CA35B3A537%2113504&authkey=AMLP8uST9gRkPWY&em=2" width="402" height="346" frameborder="0" scrolling="no"></iframe>
