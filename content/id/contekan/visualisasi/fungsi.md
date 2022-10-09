---
title: Contekan Visualisasi
linktitle: Fungsi.
summary: Menggunuakan fungsi untuk bikin grafik.
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

## nulis-nulis

Memakai `annotate` bisa liat di [sini](https://ggplot2.tidyverse.org/reference/annotate.html) dan di [sini](https://ggplot2-book.org/annotations.html)

```r
## Text
annotate("text", x = 4, y = 25, label = "Some text")
annotate("text", x = 4, y = 25, label = "italic(R) ^ 2 == 0.75",
  parse = TRUE)
annotate("text", x = 4, y = 25,
  label = "paste(italic(R) ^ 2, \" = .75\")", parse = TRUE)

## Garis
annotate("segment", x = 2.5, xend = 4, y = 15, yend = 25,
  colour = "blue",linetype="dashed")

## Titik
annotate("segment", x = 2.5, y = 15, colour = "blue",size=1.1)

## Garis ada titiknya
annotate("pointrange", x = 3.5, y = 20, ymin = 12, ymax = 28,
  colour = "red", size = 1.5)

## Kurva
annotate("curve", x = 4, y = 35, xend = 2.65, yend = 27, 
    curvature = .3, arrow = arrow(length = unit(2, "mm")))

```