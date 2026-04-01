---
layout: post
title: Amiti and Konings 2007
author: admin
category: [Review]
tags: [economics, econometrics]
categories: [Economics, Data & Code]
date: '2020-02-25'
---
This is a long-overdue blog review of Amiti and Konings' paper. This paper has been widely cited, and when it came out, the issue was really hot: how tariff reductions could help Indonesia join Global Value Chains (GVCs) and become more productive.

The article begins by summarizing the debate over the role of trade liberalization for industry. Most of the articles they cite show that trade liberalization has a positive impact on domestic industries. They emphasize the importance of examining the role of input import liberalization, which at the time still had a *gap* in the literature. The article continues with the dynamics of import duties in Indonesia and Indonesia's involvement in the World Trade Organization (WTO) in 1995.

The most interesting part of the article is of course the methodology. They conduct 2 stages of econometric estimation and one deterministic stage of productivity calculation (TFP). Assuming a *Cobb-Douglas* production function, they estimate factor return parameters on output.

$$ y_{it} = \beta_0 + \sum_{Z={k,l,m}} \beta_Z Z_{it} + e_{it} \label{1} $$

After obtaining the *estimated parameters*, they compute log TFP with

$$ tfp_{it}^k = y_{it} - \sum_{Z={k,l,m}} \hat{\beta}_Z Z_{it} \label{2} $$

where k, l, m are capital, labor and materials respectively. After obtaining TFP values for each firm, TFP is then regressed on input tariffs and output tariffs. Simple.

The interesting part is that equation \ref{1} is estimated by accounting for the fact that within $e_{it}$ there is a *time-varying productivity shock*, which will affect the firm's input purchasing decisions. This problem is accommodated by the *Olley-Pakes* method, which they discuss in the appendix. Additionally, because they care about imported materials, they modify the *Olley-Pakes* method so that import decisions are also accounted for in the firm's optimization process. It's fascinating how they connect trade and the optimization process of imported material inputs into TFP without going through the standard *gravity equation* approach.

This paper really showcases their hard work in processing data. Aggregating and disaggregating tariffs into the Indonesian Statistics (SI) data they used was no easy task. Many parts had to be done manually. Imagine mapping HS 9-digit codes to ISIC, then building an input-output table from SI on your own. Not to mention they had to calculate tariffs for both inputs and outputs.

One more thing: a paper published in AER typically has extensive robustness checks. They performed various robustness checks, such as examining sensitivity to alternative TFP metrics, endogeneity of *trade policy shocks*, alternative tariff measures, and Non-Tariff Measures.

In conclusion, this is a fascinating article. For the TFP estimation method specifically, if you're curious you'd still need to look at the other papers they cite. But nonparametric estimation like this is always interesting, as it doesn't rely entirely on the assumptions required by standard econometrics. A very engaging paper to read, especially if you're interested in Indonesian trade issues. This paper also serves as an excellent introduction to Lili Yan Ing's article in the book World Trade Evolution.
