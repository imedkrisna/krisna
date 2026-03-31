---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "A Simple Model of Local Content Requirements"
subtitle: ""
summary: ""
authors: [admin]
tags: [TKDN, trade, industry, python]
categories: [TKDN, trade, industry, python]
date: 2022-03-29T14:09:58+07:00
lastmod: 2022-03-29T14:09:58+07:00
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

Discussions about increasing the use of domestic products and anti-import sentiments have long echoed among public officials. Lately, these conversations seem to be growing ever more frequent. Of course, using domestically produced goods is not inherently a bad thing. The problem arises when it is forced. Like any other kind of love, love for domestic products is no fun when it is coerced. One of the instruments Indonesia is currently pushing hard is TKDN.

# What is TKDN?
[TKDN](http://tkdn.kemenperin.go.id/), or Tingkat Kandungan Dalam Negeri (Local Content Requirement), has become increasingly popular in Indonesia[^1]. When mandated for a given industry, TKDN requires that a minimum share of a final product contains domestic content. This content can include labour, machinery, and raw materials. For example, [5G devices](https://inet.detik.com/consumer/d-5782359/kata-samsung-tentang-ketentuan-tkdn-4g-dan-5g-jadi-35), as of April 2022, must meet a 35% TKDN threshold, meaning all 5G devices on the market must have at least 35% local content (or, equivalently, at most 65% imported components).

TKDN effectively prevents firms from simply selling imported goods. Products must be manufactured domestically. Imported components are allowed but capped. The idea is that TKDN will encourage producers to set up factories in Indonesia. I wrote a bit about this effect in [another post]({{< relref "/post/hitektrade" >}}). The resulting investment would create jobs. In a country with high informality like Indonesia, formal employment can be a good avenue for improving welfare[^2]. TKDN is also expected to build production capacity and technological capability among domestic suppliers of intermediate goods.

TKDN is popular with governments partly because it is "free" (unlike subsidies, it does not require budget outlays). Moreover, anti-import policies tend to be popular with the public, potentially boosting politicians' approval.

At first glance, raising TKDN does seem beneficial. If investment flows in, there should be additional value added. However, it is important to understand that the concept of value is neither static nor exogenous. The value of a product can rise or fall depending on its inputs. For instance, does a 5G device with high domestic content perform as well as a fully imported one? Can a high-TKDN product compete in global markets? Does building a smelter really capture more value [than just exporting raw nickel](https://theconversation.com/klaim-sukses-hilirisasi-nikel-berbasis-larangan-ekspor-masih-memiliki-segudang-masalah-177735)?

The answer is not necessarily yes. Several theoretical papers dissect how value and productivity shift between intermediate-input producers and final-good producers[^3] [^4] [^5]. There is indeed a trade-off, and TKDN does not automatically produce outcomes as optimal as they may appear, especially if TKDN fails to raise productivity in the sector it aims to protect.

In this post, I try to illustrate this trade-off using a very simple model.

# The Model
Suppose there is a final-good producer that often needs imported inputs. These inputs could in principle be substituted domestically, but for the firm, imports are cheaper and offer higher value added. Real-world examples might include [soybeans](https://ekonomi.bisnis.com/read/20180829/99/832660/ini-alasan-kedelai-impor-lebih-digemari-produsen-tempe) or [salt](https://bisnis.tempo.co/read/1071682/kenapa-kualitas-garam-lokal-untuk-industri-kalah-dibanding-impor).

If we focus solely on the input-sourcing decision, the firm has the production function:

$$F(M,N) = \alpha M + N$$

where $M$ is the quantity of imported inputs and $N$ is the quantity of domestically sourced inputs. Meanwhile, $\alpha$ represents the quality of imported raw materials relative to domestic ones. If $\alpha > 1$, then imported goods are of higher quality. We also assume imported inputs are cheaper ($P_M<P_N$).

The firm is required to purchase a minimum share $k$ of domestic raw materials:

$$
P_NN \geq kP(\alpha M + N)
$$
$$
\text{where } k \in (0,1)
$$

The firm wants to meet demand $F(M,N)=Q$ at the lowest possible cost. That is, the firm solves:

$$
\min P_MM+P_NN
$$
$$
s.t. \ \alpha M+ N \geq Q
$$
$$
P_NN \geq kP(\alpha M + N)
$$
$$
k \in (0,1)
$$

Since the problem is linear, we can use `linprog`. I will use the following parameters:

$$
P_M=1
$$
$$
P_N=3
$$
$$
α=1.5
$$
$$
k=0
$$
$$
P=9
$$
$$
Q=30
$$

First, let us define the function:

```python
from scipy.optimize import linprog
def TKDN(Pm=1,Pn=3,α=1.5,δ=1,k=0,P=9,Q=30):
    c_ex1 = np.array([Pm, Pn])
    A_ex1 = np.array([[-α,-1],[k*P*α, k*P-Pn]])
    b_ex1 = np.array([-δ*Q,0])
    res_ex1 = linprog(c_ex1, A_ub=A_ex1, b_ub=b_ex1, method='revised simplex')
    names=[f'imported inputs = {res_ex1["x"][0]}',
    f'domestic inputs = {res_ex1["x"][1]}',
    f'production cost = {Pm*res_ex1["x"][0]+Pn*res_ex1["x"][1]}',
    f'firm profit = {Q*P-Pm*res_ex1["x"][0]-Pn*res_ex1["x"][1]}']
    for i in names:
        print(i)
    
    
```

The default numbers above should not be taken literally -- $P_M=1$ is simply a *numeraire*, or base price. Because the problem is linear (and therefore invariant to affine transformations), $P_N=3$ can be interpreted as meaning domestic raw materials are three times more expensive than imported ones.

# Winners and Losers
Now let us use the function we just defined. Remember the `linprog` dependency from `scipy`. For the no-TKDN case, we set $k=0$:

```python
TKDN()
```

    imported inputs = 20.0
    domestic inputs = 0.0
    production cost = 20.0
    firm profit = 250.0
    

What about a TKDN where domestic content must be at least 20% of total final-product value?

```python
TKDN(k=0.2)
```

    imported inputs = 8.0
    domestic inputs = 18.0
    production cost = 62.0
    firm profit = 208.0
    

As we can see, TKDN causes the final-good producer's profit to fall and total cost to rise. However, the domestic input supplier gains additional revenue of $18 \times P_N$. In other words, TKDN tends to benefit domestic raw material sellers but hurts final-good producers.

When TKDN is set to 40%, the model crashes -- the final-good producer is better off not producing at all.

If we tabulate TKDN from 0 to 30% (in 10% increments):

| k | M | N | C | $\pi$ |
| --- | --- | --- | --- | --- |
| 0 | 20 | 0 | 20 | 250 |
| 10% | 14 | 9 | 41 | 229 |
| 20% | 8 | 18 | 62 | 208 |
| 30% | 2 | 27 | 83 | 187 |

What about total domestic value added? Although TKDN raises value added for the input producer, it reduces value added for the final-good producer. With TKDN=0, the input producer's value added is 0, while the final-good producer's profit is 250. At TKDN=10%, the input supplier gains 9 but the final-good producer loses $250-229=21$. So total value added actually declines.

What about the government? Assuming duty-free imports, government revenue comes from corporate income tax. With TKDN=0, the input supplier pays no tax. The final-good producer pays corporate income tax of $t \pi$ where $t$ is the tax rate. If we assume the domestic input supplier's cost is 0, then the supplier's income is $P_N \times N$. Total government revenue becomes:

$$GR=t(P_N-c)N+t \pi$$

where c is the marginal cost, linear in output. I use c=2 so the domestic firm needs to charge $P_N=3$ to earn a margin of 1, the same as the importer. If domestic costs were low, they could sell at a lower price and win orders from the final-good producer.

Let us calculate government revenue at a 20% tax rate:

```python
t=0.2 # corporate income tax
Pn=3 # domestic input price
c=2 # so firms can't sell below 3
brp=('0%','10%','20%','30%')
taxs=((Pn-c)*0*t+250*t,
(Pn-c)*9*t+229*t,
(Pn-c)*18*t+208*t,
(Pn-c)*27*t+187*t)
for x,y in zip(brp,taxs):
    print(f'At TKDN={x}, total GR = {y}')
```

    At TKDN=0%, total GR = 50.0
    At TKDN=10%, total GR = 47.6
    At TKDN=20%, total GR = 45.2
    At TKDN=30%, total GR = 42.8
    

The higher the TKDN, the lower the total income tax from the two firms. Although tax from the domestic firm rises, tax paid by the final-good producer falls because profits shrink. So even though TKDN appears not to require fiscal expenditure like subsidies, the inefficiency it generates carries a hidden cost to the state budget as well.

This is on top of the budget spent on enforcing TKDN rules. For instance, to verify that a firm complies with TKDN, it must be surveyed for a TKDN certificate. The first two product certificates are paid for by the government, funded from the state budget. This does not include the systems and human resources the government must allocate for TKDN enforcement. Moreover, for the third product onward, the firm must bear the certification cost itself, further reducing profits and consequently the corporate income tax paid.

# So Is TKDN Good or Bad?

The issues above illustrate potential problems created by TKDN. This linear model, while somewhat arbitrary, does a reasonable job of explaining TKDN's short-run effects. More representative (but more complex) models can be found in the footnotes.

One important caveat is that we cannot simply assume $Q$ and $P, P_M, P_N$ remain constant under TKDN. It is possible that instead of becoming more efficient, domestic input producers become complacent under protection and show no improvement at all. Rather than improving, they may even raise prices because the final-good producer has no alternative as long as TKDN binds.

Furthermore, TKDN makes domestic final-good producers less competitive against foreign ones. Why? Because foreign producers can access cheap, high-quality inputs without TKDN constraints. As a result, domestic final-good producers cannot compete in global markets and are forced to rely on the domestic market. Unable to compete with imported finished goods either, they will demand protection too.

This is why IMEI blocking exists. Domestic phone manufacturers do not want to compete with imported phones that are not subject to TKDN. Has the public ever been told how much of the state budget is spent on implementing IMEI blocking?

Finally, once TKDN is in place, it is very hard to roll back. Firms that have already made large investments to comply with TKDN would suffer significant losses if the policy were suddenly removed and firms that did not invest could enter the previously protected market. Therefore, firms that have already invested to meet TKDN have a strong incentive to lobby the government to maintain and enforce TKDN rules.

TKDN can be considered successful if domestic input producers actually learn and improve. For example, if their industry grows and becomes efficient enough to match import prices ($P_N \leq P_M$), or improves quality to surpass imports ($\alpha \in (0,1)$). If this happens, $k$ is no longer binding and TKDN can be declared a success, depending on how large and how fast the domestic industry's improvement is.

Therefore, policymakers who have already adopted TKDN should continuously monitor $\alpha$ and $P_N$ (or more precisely $\frac{P_N}{P_M}$). If there is no progress, it is hard to expect domestic industry to become efficient and competitive, and the desired advantages will not materialise. Coercion alone is unlikely to succeed. The government may need to complement TKDN with other policies that promote efficiency. So yes, the regulatory burden just keeps growing.

# Alternatives to TKDN

There are several alternatives to TKDN[^6]:
1. **Improve the business climate.** This one seems obvious. But nothing beats this approach. It is hard for industry to advance when upstream sectors are protected, and both importing and exporting carry high administrative costs. Customs officials still engage in [corruption](https://regional.kompas.com/read/2022/03/25/171720578/berkas-perkara-korupsi-dilimpahkan-ke-pengadilan-2-eks-pejabat-bea-cukai).
1. **Leverage CSR.** Ask multinational companies whether they can help develop local firms as suppliers.
1. Provide **training** for workers and component suppliers. Training is essential for improving the quality of local businesses and workers. A government that understands industry should be able to identify what training is needed and deliver it. This also costs money, but it is far better spent than on enforcing TKDN.
1. Improve **logistics processes and physical infrastructure.** This too seems obvious.
1. If all else fails, using **tariffs and subsidies**, though not ideal, is still better than TKDN. Of course, the main problem with tariffs is trade agreements and retaliation. Tariffs are easier to quantify than TKDN, making them more likely to face challenges at the WTO. Subsidies burden the budget directly, unlike TKDN which burdens the budget and the economy indirectly. Such is life when your policymakers and politicians cannot calculate hidden costs.

## Update

A new book on TKDN has just been released for those who want to learn more. It is an edited volume by Lili Yan Ing and Grossman[^7]. One particularly interesting chapter is by Yessi Vadila[^8].

I will discuss it further some other time. Mention me on [twitter](https://www.twitter.com/imedkrisna) if you have comments, criticisms, or suggestions. Thanks.

[^1]: Fernando, O., & Ing, L. Y. (2022). Indonesia's Local Content Requirements: An Assessment on Consistency with Free Trade Agreement Commitments. *ERIA Discussion Paper Series*, 420. https://www.eria.org/publications/indonesias-local-content-requirements-an-assessment-on-consistency-with-free-trade-agreement-commitments/ 
[^2]: Gupta, K., & Mardjono, E. (2021). Indonesia Emas Berkelanjutan 2045: Kumpulan Pemikiran Pelajar Indonesia Sedunia Seri 01 Ekonomi. LIPI Press. https://doi.org/10.14203/press.357 
[^3]: Grossman, G. M. (1981). The Theory of Domestic Content Protection and Content Preference. *The Quarterly Journal of Economics*, 96(4), 583-603. https://doi.org/10.2307/1880742 
[^4]: Veloso, F. M. (2006). Understanding Local Content Decisions: Economic Analysis and an Application to the Automotive Industry. *Journal of Regional Science*, 46(4), 747-772. https://doi.org/https://doi.org/10.1111/j.1467-9787.2006.00476.x 
[^5]: Lin, S.-H., & Weng, Y. (2020). Can strengthening the local content requirements meet a government's need to raise industrial productivity and production? *Journal of Applied Economics*, 23(1), 316-328. https://doi.org/10.1080/15140326.2020.1753468
[^6]: Hufbauer, G., Schott, J. J., Wada, E., Cimino, C., & Vieiroand, M. (2013). Local Content Requirements : A Global Problem. Peterson Institute for International Economics. http://ebookcentral.proquest.com/lib/anu/detail.action?docID=3385696 
[^7]: Ing, L. Y., & Grossman, G. M. (2023). Local content requirements: promises and pitfalls. Routledge. https://doi.org/10.4324/9781003415794 
[^8]: Vadila, Y., & Christian, D. (2023). Effects of Local Content Requirements on Trade. In B. Hoekman & K. Saggi (Eds.), The Political Economy of Trade Policy: Theory, Evidence and Applications. Routledge. https://doi.org/10.4324/9781003415794-7 


