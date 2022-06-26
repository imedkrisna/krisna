---
title: Contekan Visualisasi
linktitle: Berbagai grafik.
summary: Contekan untuk berbagai grafik.
date: '2022-06-26'
type: book
weight: 10
---

## Pie chart di r

#### Pie chart dengan ggrepel

Contoh sample dataset:

```r
df <- data.frame(value = c(15, 25, 32, 28),
                 group = paste0("G", 1:4))
```

Bikin pie chart-nya

```r
# install.packages("ggplot2")
# install.packages("ggrepel")
# install.packages("tidyverse")
library(ggplot2)
library(ggrepel)
library(tidyverse)

# Get the positions
df2 <- df %>% 
  mutate(csum = rev(cumsum(rev(value))), 
         pos = value/2 + lead(csum, 1),
         pos = if_else(is.na(pos), value/2, pos))

ggplot(df, aes(x = "" , y = value, fill = fct_inorder(group))) +
  geom_col(width = 1, color = 1) +
  coord_polar(theta = "y") +
  scale_fill_brewer(palette = "Pastel1") +
  geom_label_repel(data = df2,
                   aes(y = pos, label = paste0(value, "%")),
                   size = 4.5, nudge_x = 1, show.legend = FALSE) +
  guides(fill = guide_legend(title = "Group")) +
  theme_void() 
``` 
 
Part paling pentingnya adalah bikin urutan (direfleksikan oleh pembuatan df2) dan juga kode `geom_label_repel`. Teknik ini saya dapet dari [sini](https://r-charts.com/part-whole/pie-chart-labels-outside-ggplot2/).