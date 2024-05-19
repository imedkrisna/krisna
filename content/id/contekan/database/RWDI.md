---
title: R WDI
linkTitle: RWDI
summary: Narik data WDI dari R
categories: [r]
tags: [r]
author: admin
date: '2024-05-19'
type: book
weight: 25
---

### Download data pake package WDI
```r
indi<-c(            # membuat dictionary
  "PDB"="NY.GDP.MKTP.CD",
  "import"="NE.IMP.GNFS.CD"
)

dat<-WDI(           # Menarik data World Bank
  country="all",
  indicator=indi,
  start=2019,end=2019,
)
```

### Gambar

```r
library(ggrepel)
weleh<-subset(dat,iso2c%in%c("ID","KR","CN","US","GB","EU","SG",
                             "TL","BN","KH","MY","TH","JP"))
www<-dat %>% ggplot(aes(x=Limport,y=LPDB)) + geom_point() + geom_smooth(method="lm")
www+geom_label_repel(data=weleh,box.padding   = 0.35, point.padding = 0.5, segment.color = 'grey50',label=weleh$country,min.segment.length = 0,nudge_y = -4) + theme_classic()
```

## Typical graph

```r
graph<-function(dataset, ...) {
  dataset |>
    ggplot(aes(...))+
    theme_classic() +
    theme(panel.background = element_rect(fill = "#f0f1eb",
                                        colour = "#f0f1eb"),
        plot.background = element_rect(fill = "#f0f1eb"),
        legend.key = element_rect(fill = "#f0f1eb",linetype = "blank"),
        legend.background = element_rect(fill="#f0f1eb"))
}
```

## Saving