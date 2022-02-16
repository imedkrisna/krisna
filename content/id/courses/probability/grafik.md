---
title: Grafik
date: '2021-01-01'
type: book
weight: 30
---

Menarik file yang di-host di google drive:

```r
id <- "0B-wuZ2XMFIBUd09Ob0pKVkRzQTA" # google file ID
read.csv(sprintf("https://docs.google.com/uc?id=%s&export=download", id))
```