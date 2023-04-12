---
title: Contekan Visualisasi
linktitle: Styling / theming grafik
summary: Beberapa contekan untuk styling/theming/format grafik.
date: '2021-01-01'
type: book
weight: 20
---

Contekan dasar set styling seaborn [dari sini](http://seaborn.pydata.org/tutorial/aesthetics.html) dan [dari sini](https://seaborn.pydata.org/generated/seaborn.set_style.html)


## Seaborn

#### Dark
```python
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)
```

#### Light

```python
jtplot.reset() ## I use dark mode by default hence needs to turn it off for books and stuff
custom_params = {"axes.spines.right": False, "axes.spines.top": False} ## ngilangin kotak sudut kanan atas
sns.set_theme(style="ticks", context='paper',font_scale=1,rc=custom_params) ## Kadang pake style "white" juga bisa
# plt.figure(figsize=(5,4),dpi=80, facecolor='w', edgecolor='k') ## biasanya ga perlu. context aja udah cukup
```

## ggplot

#### Dark

```r
library('ggplot2')
library('ggdark')
graph<-ggplot()+
  dark_theme_bw(base_size=18)+
  theme(text = element_text(color='#e0e0e0'),
        panel.border = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.line = element_line(colour = "#e0e0e0"))
```

##### With function

```r
library('ggplot2')
library('ggdark')
graph<-function(dataset, ...) {
  dataset |>
    ggplot(aes(...))+
    dark_theme_bw(base_size=18)+
    theme(text = element_text(color='#e0e0e0'),
          panel.border = element_blank(),
          panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          axis.line = element_line(colour = "#e0e0e0"))
}
```

#### Light

```r
theme_classic() +
  theme(panel.background = element_rect(fill = "#f0f1eb",
                                        colour = "#f0f1eb"),
        plot.background = element_rect(fill = "#f0f1eb"),
        legend.key = element_rect(fill = "#f0f1eb",linetype = "blank"),
        legend.background = element_rect(fill="#f0f1eb"))
```

light tapi untuk buat grafik utk ngajar.

```r
theme_classic()+
  theme(axis.title.x = element_text(hjust=1),
        axis.title.y = element_text(angle=0,hjust=1,vjust=1),
        panel.grid=element_blank(),
        axis.text.x=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.x=element_blank(),
        axis.ticks.y=element_blank(),
        legend.position=c(1,1),
        legend.justification = c(1,1),
        legend.spacing=unit(0,"cm"),
        legend.margin=margin(0,0,0,0))
```