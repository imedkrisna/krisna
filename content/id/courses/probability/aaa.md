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