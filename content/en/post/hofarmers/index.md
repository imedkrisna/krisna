---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Labor-machine substitution in agriculture'
subtitle: "comparing US and Indonesian farmers"
summary: ""
authors: [admin]
tags: [economics, trade, model, HecksherOhlin]
categories: [Economics, Trade, Research]
date: 2024-02-25T15:10:34+07:00
lastmod: 2024-02-25T15:10:34+07:00
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

Today, February 25, 2024, there's a lively online discussion about Indonesia's increasingly high food prices. Some people are comparing rice prices abroad vs. in Indonesia, asking why other countries can keep prices low. The answer, of course, is that abroad (at least in Western countries) rice can be imported freely without government intervention. The follow-up question: if we're an agrarian country, how can domestic production be more expensive than imports? There are many answers to this, and they've been addressed elsewhere -- for instance in [this CIPS publication](https://www.cips-indonesia.org/post/intensifikasi-pertanian-kebijakan-prioritas-untuk-penyediaan-pangan-nasional?lang=id) or [Arianto Patunru's blog](https://medium.com/@acopatunru/beras-dan-mitos-762cf88b7bd9). Excellent reads, both of them.

This post is related but focuses specifically on farmer numbers and productivity. Why? Because I'm currently teaching international economics and this is a perfect illustration of factor substitution as described in the Heckscher-Ohlin (HO) model. In Indonesia, there are many farmers but little farmland. Indonesia imports soybeans from the US, even though the US has even fewer farmers than Indonesia.

<iframe src="https://data.worldbank.org/share/widget?indicators=SL.AGR.EMPL.ZS&locations=ID-US" width='900' height='600' frameBorder='1' scrolling="yes" ></iframe>

TLDR: This ultimately comes down to a discussion of labor intensity vs. capital intensity in agriculture, where in the US, machinery plays a far greater role than labor, while Indonesia is the opposite. For those who want to understand how economists analyze factor intensity, see the appendix at the bottom.

Let's continue with the factor intensity discussion.

## Heckscher-Ohlin and factor intensity

In Heckscher-Ohlin (HO) trade theory, there is substitution between labor and capital (machinery). Having fewer farmers is fine as long as they're replaced with an appropriate amount of machinery.

Suppose there are 2 production options with the same output:

1. 10 farmers with 10 hoes
2. 1 farmer with 1 tractor

In case 1, most expenditure clearly goes to wages since you're paying 10 people. In case 2, wages are a small share of total costs since you're only paying 1 farmer. However, capital expenditure in case 1 is much smaller, especially since hoes are cheap (though as President Jokowi once said, ["stop importing hoes"](https://jakartaglobe.id/business/stop-importing-hoes-jokowi)).

This is the key difference between the cost structure of Indonesian farmers and those in developed countries. In case 2, if the farmer asks for a raise, it won't significantly increase total production costs. But in case 1, a wage increase burdens production costs heavily because 10 people need raises.

I compare the production cost structure of Indonesia vs. the United States. I use soybean production cost data for 2017 (because BPS only has Indonesian data through 2017). [US data from USDA](https://www.ers.usda.gov/data-products/commodity-costs-and-returns.aspx); [Indonesian data from BPS](https://www.bps.go.id/id/statistics-table/1/MjA1NSMx/nilai-produksi-dan-biaya-produksi-per-musim-tanam-per-hektar-budidaya-tanaman-padi-sawah--padi-ladang--jagung--dan-kedelai--2017.html). Not all cost items are shown -- only those present in both datasets.

| Item | USA  (%) | IDN (%) |
| ------- | ---- | ---- | 
| Seed	| 9.25 |	6.53 |
| Fertilizer |	3.99 |	4.97 |
| Chemicals |	4.28 |	4.02 |
| Labor |	3.61 |	47.23 |
| Rent/interest |	0.13 |	0.12 |
| Land |	22.77 |	28.89 |
| Taxes & insurance |	1.70 |	0.86 |
| Depreciation |	14.50 |	1.98 |
| Energy etc. |	2.16 |	1.26 |

The contrast in labor and depreciation is stark. For Indonesian soybean farmers in 2017, 47% of production costs went to labor. For US farmers, labor was only 3.61% of total costs -- even though we know US wage levels are much higher than Indonesia's. This means that in the US, despite expensive wages, labor costs are a small share because they use far fewer farmers than Indonesia does.

Depreciation is also strikingly different. Capital depreciation in the US accounts for 14.5% of total production costs, while in Indonesia it's only 2%. This means Indonesian farmers use far less machinery than US farmers. Moreover, the rental/interest share is identical in both cost structures, despite the US having much more machinery. This implies that interest rates in the US are cheap.

In other words, to grow soybeans, you can either use many farmers with minimal machinery (manual), or few farmers with expensive machines (semi-automation). Which strategy is adopted depends on the _relative abundance of factors_. In Indonesia, there are many workers suitable for farming while capital for buying machines is relatively scarce (production interest rates in Indonesia are very high). In the US it's the opposite: suitable farm workers are fewer (hence expensive) but capital is abundant (pre-COVID interest rates in the US were very low). This is the substitution effect at the heart of the HO model.

## Key takeaways & disclaimer

The main conclusions of this post:

1. For efficient agriculture, factor usage must match factor intensity. Some crops may need more machinery and fewer workers. A country that persists in using many workers in an industry that would be more efficient with machinery will have higher production costs than a country using machinery.

2. A country where labor is cheap relative to machinery will struggle to compete on price with a country where machinery is relatively cheaper, in _capital intensive_ industries. Why? Because the labor-cheap country tends to use more labor even in industries that are inherently _capital intensive_, leading to inefficiency.

3. It's actually more efficient to export _labor intensive_ products and use the proceeds to import _capital intensive_ products.

Disclaimer: the problems in Indonesian agriculture are complex. It's not just about mechanization. The table above also shows that land constitutes a large share of production costs in both countries -- land has no substitute in either the US or Indonesia. The difference is obviously that the US has far more land. There are also irrigation issues where Mekong River countries (Vietnam, Thailand) have advantages over Indonesia, even though their labor structures are similar (discussed in [Arianto Patunru's blog](https://medium.com/@acopatunru/beras-dan-mitos-762cf88b7bd9) linked above). And more.

When we economists analyze the real world, there are of course many more considerations. For instance, factors of production aren't limited to just labor and capital. In fact, Indonesia exports land-intensive products like mining and plantation commodities. Labor can also be divided into low-skill and high-skill categories. But if I kept going this post would never end.

Hope this HO case study is useful, especially for those studying international economics.

## Appendix: A crash course on factor intensity

In standard micro and macroeconomics, we typically begin studying production with the general function:

$$Q=f(K,L)$$

where $K$ is the amount of capital used and $L$ is the number of workers employed to produce output $Q$. In introductory courses, production factors are described as two: capital and labor[^1].

In a competitive economy, factors are compensated equal to their marginal productivity[^2]:

$$\frac{df(K,L)}{dL}=w$$

$$\frac{df(K,L)}{dK}=r$$

where $w$ is the wage and $r$ is rental/depreciation cost.

If production has a cost structure like:

$$TC=w \times L+r \times K$$

where total cost (TC) equals wages times workers plus rental times capital, then an economy is said to be labor intensive if labor's share of total cost dominates capital's share. That is, an economy is labor intensive if:

$$
\frac{w \times L}{TC} > \frac{r \times K}{TC}
$$

Observing marginal productivity directly is impractical, while costs can still be calculated. Relying on the assumption that _cost shares_ approximate _productivity shares_, we assess factor intensity through _cost shares_.

[^1]: Ownership of factors of production was historically a major source of debate, pitting capitalists (owners of K) against workers (owners of L). The struggle was over who gets a larger share of Q.

[^2]: Theoretically, productivity is calculated using marginal product or the first derivative of Q with respect to each factor. In practice, this is extremely difficult. Very strict conditions are required.
