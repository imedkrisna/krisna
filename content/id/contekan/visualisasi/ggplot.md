---
title: Contekan Visualisasi
linktitle: Styling / theming
summary: Beberapa contekan untuk styling/theming/format grafik.
date: '2021-01-01'
type: book
weight: 10
---

Contekan dasar set styling seaborn [dari sini](http://seaborn.pydata.org/tutorial/aesthetics.html) dan [dari sini](https://seaborn.pydata.org/generated/seaborn.set_style.html)


Style grafik saya di buku PPID.

```python
jtplot.reset()
custom_params = {"axes.spines.right": False, "axes.spines.top": False} ## ngilangin kotak sudut kanan atas
sns.set_theme(style="ticks", context='paper',font_scale=1,rc=custom_params) ## Kadang pake style "white" juga bisa
# plt.figure(figsize=(5,4),dpi=80, facecolor='w', edgecolor='k') biasanya ga perlu. context aja udah cukup
```

## Control x and y axis in matplotlib
```python
ax.set_xlabel(‘angle’)
ax.set_title('sine')
ax.set_xticks([0,2,4,6])
ax.set_xticklabels(['zero','two','four','six'])
ax.set_yticks([-1,0,1])
```