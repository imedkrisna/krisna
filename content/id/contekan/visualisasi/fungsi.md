---
title: Contekan Visualisasi
linktitle: Berbagai grafik.
summary: Contekan untuk berbagai grafik.
date: '2022-06-26'
type: book
weight: 40
---

## berbagai fungsi buat grafik

```r
bola<-function(q) (16-q^2)^(0.5)
demand<-function(q) 5-5*q
demand<-function(q) q
demand1 <- function(q) (q/433)^(-1/0.5)
supply1 <- function(q) (q/41.3)^(1/0.5)

x<-120:150
equi <- uniroot(function(x) demand(x) - supply(x), range(x))$root


# Equilibrium price
ps <- supply(equi)
```