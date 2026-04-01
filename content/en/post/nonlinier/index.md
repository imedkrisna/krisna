---
layout: post
title: "Learning non-linear estimation of Constant Elasticity of Substitution (CES) with ADMB"
categories: [Economics]
tags: [economics]
date: '2020-02-27'
author: admin
---

I recently discovered a free software called ADMB. Its function is to estimate non-linear regressions. I need non-linear regression estimation to get an elasticity parameter that is not equal to 1.

The example that ADMB uses for Robust Linear Regression is the (von Bertalanffy) growth curve model:

$$
s(a)=L_{\infty} \left(1-exp\left(-K(a-t_0)\right)\right) \label{1}
$$

where the parameters to be estimated are $$L_{\infty}$$, $$K$$, and $$t_0$$. Suppose the observed data are $$O_i$$ and $$a_i$$, and we want to predict $$O_i$$ using $$s(a_i)$$, then ADMB needs to minimize the distance between $$O_i$$ and $$s(a_i)$$:

$$
\min_{L_{\infty}, K, t_0} \sum_{i} (O_i-s(a_i))^{2} \label{2}
$$

What I need to do is replace model \ref{1} with the Constant Elasticity of Substitution function:

$$
Y = \gamma \left(\sum_{i=1}^n \delta_i X_i^{\rho}\right)^{-\frac{\upsilon}{\rho}} \label{3}
$$

but of course the natural-log version:

$$
\ln Y = \ln \gamma - \left(\frac{\upsilon}{\rho}\right) \ln \left(\sum_{i=1}^n \delta_i X_i^{\rho}\right) \label{4}
$$

So I need to alter equation \ref{1} in the ADMB example to the equation I want, namely \ref{4}. In \ref{4}, the observables are $$\ln Y$$ and $$x_i$$. Everything else -- the Greek letters -- are parameters. I probably need to start with initial guesses. The safest guess would be $$\rho=1$$ to get Cobb-Douglas, heh. Also, I think I need to impose the restriction $$\sum_i \delta_i = 1$$.

Since I am already tired today, I will continue tomorrow.
