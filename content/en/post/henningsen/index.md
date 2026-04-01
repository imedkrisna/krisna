---
layout: post
title: Henningsen and Henningsen 2011
category: [Economics]
tags: [economics]
categories: [Economics]
date: '2020-02-25'
author: admin
---

I read this paper because I needed to estimate a Constant Elasticity of Substitution (CES) production function. Typically, when estimating Total Factor Productivity (TFP), economists prefer the Cobb-Douglas function because it's easy to linearize and its parameters have useful real-world interpretations. Unfortunately, for structural models like Computable General Equilibrium (CGE), estimating with Cobb-Douglas has the drawback that the substitution parameter is always 1. No modern CGE model uses a substitution elasticity of 1.

Unfortunately, CES estimation is quite difficult. Linearization is possible using [Taylor series](https://en.wikipedia.org/wiki/Taylor_series) and its extensions, but if you want to use it for economic models, many restrictions are needed. The alternative is non-linear estimation, which comes in various algorithmic flavors. Plus, I needed step-by-step instructions for implementing it computationally.

{% assign author = site.data.article[page.author] %}
<a rel="author"
  href="{{ author.link }}"
  title="{{ author.name }}">
    {{ author.name }} {{ author.year}}
</a> is the perfect paper for me. They developed an R package called [micEconCES](https://cran.r-project.org/web/packages/micEconCES/index.html). This package can perform CES estimation and documents the various algorithms available. They also survey the history of CES estimation from when CES was first proposed by [Arrow](https://en.wikipedia.org/wiki/Kenneth_Arrow) and colleagues through to recent developments. Comprehensive stuff.

A quick refresher on CES: in general, the CES function takes the form:

$$
y = \gamma \left(\sum_{i=1}^n \delta_i x_i^{\rho}\right)^{-\frac{\upsilon}{\rho}} \label{1}
$$

where x represents factors of production (capital, labor, materials, etc.). Ideally, we want different substitution parameters for each pair of factors. <a rel="author"
  href="{{ author.link }}"
  title="{{ author.name }}">
    {{ author.name }} {{ author.year}}
</a> uses an approach pioneered by Sato (1967) employing *nested CES*. For example, with 3 factors of production, instead of putting all factors into model \ref{1} with a single substitution parameter $\rho$, Sato structures it as follows:

$$
y = \gamma \left[\: \delta \: (\delta_1 x_1^{-\rho_1} + (1-\delta_1) x_2^{-\rho_1})^{\rho/\rho_1} + (1-\delta) \delta_2 x_3^{-\rho/\rho_2}\right]^{-\frac{\upsilon}{\rho}} \label{2}
$$

With this *nested CES* method, we can have multiple substitution parameters, including the substitution between $x_1$ and $x_2$ (given by ${\rho/\rho_1}$), and the parameter between the *nested $x_1$ and $x_2$* and $x_3$. Depending on your needs as a *researcher*, the model can be configured. If you're satisfied with a single $\rho$ for all factors, you can use model \ref{1} directly. Sometimes we feel that among 3 factors, two have a different substitution relationship with the third. For instance, if your factors are *capital*, *skilled labor*, and *unskilled labor*, you might use model \ref{2} where $x_1=skilled\ labor, x_2=unskilled\ labor$, and $x_3 = capital$.
