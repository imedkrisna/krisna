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

## sampling prior (Gaussian approximation)

harus pake **rethinking** package

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

```r
n<-10
alpha<-rnorm(n,60,10)
beta<-rlnorm(n,0,10)
Hbar<-150
Hseq<-seq(from=130,to=170,len=30)
plot(NULL,xlim=c(130,170),ylim=c(10,100),
    xlab="height (cm)",ylab="weight (kg)")
for (i in 1:n)
    lines(Hseq,alpha[i]+beta[i]*(Hseq-Hbar),
    lwd=3,col=2)
```

## Simulation with quadratic approximation (page 41 in the book)

```r
# Simulation part
alpha<-70
beta<-0.5
sigma<-5
n_id<-100
H<-runif(n_individuals,130,170)
mu<-alpha+beta*(H-mean(H))
W<-rnorm(n_individuals,mu,sigma)
dat<-list(H=H,W=W,Hbar=mean(H))

#validation part
m_validate<-quap(
    alist(
        W ~ dnorm(mu,sigma),
        mu<-a+b*(H-Hbar),
        a~dnorm(60,10),
        b~dlnorm(0,1),
        sigma~dunif(0,10)
    ),data=dat
)

#get validation summary
precis(m_validate)
```

## Validation with quadratic approximation using real data

```r
# still using package rethinking
data(Howell1)
d<-Howell1
d<-d[d$age>=18,]

dat<-list(
    W=d$weight,
    H=d$height,
    Hbar=mean(d$height)
)

m_adults<-quap(
    alist(
        W ~ dnorm(mu,sigma),
        mu<-a+b*(H-Hbar),
        a~dnorm(60,10),
        b~dlnorm(0,1),
        sigma~dunif(0,10)
    ),data=dat
)
```

## Graph
```r
#plot sample
col2<-col.alpha(2,0.8)
plot(d$height,d$weight,col=col2,lwd=3,
    cex=1.2,xlab="height (cm)",ylab="weight (kg)")
# Expectation with 99% ompatibility interval
xseq<-seq(from=130,to=190,len=50)
mu<-link(m0,data=list(H=xseq,Hbar=mean(d$height)))
lines(xseq,apply(mu,2,mean),lwd=4)
shade(apply(mu,2,PI,prob=0.99),xseq,col=col.alpha(2,.5))
# 89% predictive interval
W_sim<-sim(m0,data=list(H=xseq,Hbar=mean(d$height)))
shade(apply(W_sim,2,PI,prob=0.89),xseq,col=col.alpha(1,.3))
```

