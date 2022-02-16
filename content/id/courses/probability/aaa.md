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

$$Y_i ~ Normal(\mu_i,\sigma)$$ 

where

$$\mu_i=\alpha+\beta X_i$$

```r
alpha<-0
beta<-0.5
sigma<-5
n_id<-100

X<-runif(n_id,130,170)

mu<-alpha+beta*X

Y<-rnorm(n_id,mu,sigma)
```

## sampling prior

```r
n_samples<-10
alpha<-rnorm(n_samples,0,1)
beta<-rnorm(n_samples,0,1)
plot(NULL,xlim=c(-2,2),ylim=c(-2,2),
    xlab="x",ylab="y")
for ( i in 1:n_samples )
    abline(alpha[i],beta[i],lwd=4,col=2)
```

We sample prior first. Scale the observation as relative to mean. ie,

$$Y_i ~ Normal(\mu_i,\sigma)$$

di mana

$$\mu_i=\alpha+\beta (X_i - \bar{X}$$