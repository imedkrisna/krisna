---
title: Memulai
date: '2021-01-01'
type: book
weight: 10
---

## Paling gampang

```r
W<-6
N<-9
p<-seq(from=0,to=1,len=1000)
prW<-dbinom(W,N,p)
prp<-dunif(p,0,1)
posterior<-prW*prp
```

## Easy generative model

for $Y_i ~ Normal(\mu_i,\sigma)$ where $\mu_i=\alpha+\beta X_i$

```r
alpha<-0
beta<-0.5
sigma<-5
n_id<-100

X<-runif(n_id,130,170)

mu<-alpha+beta*X

Y<-rnorm(n_id,mu,sigma)
```