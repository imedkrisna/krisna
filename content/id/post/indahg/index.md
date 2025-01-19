---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Mengecek data tingkat pengangguran terbuka BPS"
subtitle: ""
summary: ""
authors: [admin]
tags: [pengangguran,podcast]
categories: [pengangguran,podcast]
date: 2025-01-18T14:06:59+11:00
lastmod: 2025-01-18T14:06:59+11:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

Beberapa waktu yang lalu, saya dan mas Anton diundang tim Indah G Show ngobrol-ngobrol di platform tersebut. Di situ sih kami ngobrol-ngobrolnya santai ya dan mostly spontan karena impromptu. Sayangnya, di event ngobrol santai / spontan gini, seringkali saya tidak begitu hapal data, dan kesempatan untuk ngecek data tentu saja tidak ada atau setidaknya akan merusak momen gitu, agak beda dengan ngobrol di twitter yang tidak langsung / tidak tatap muka.

Nah, salah satu momen ini adalah ketika kami ngomongin soal tingkat pengangguran (unemployment rate). Waktu itu (waktu itu tapingnya kalo tidak salah bulan Oktober apa November gitu ya, 2024) berita tentang deflasi dan pengangguran sedang marak, dan sedang ramai dikatakan bahwa pengangguran lagi banyak. Saya mengatakan bahwa tingkat pengangguran ketika itu mungkin tidak berbeda jauh dari sebelum-sebelumnya. Nah kebetulan saya ngomong bahwa tingkat pengangguran setiap daerah bisa saja berbeda. Sayangnya ngecek angka pengangguran berbagai provinsi butuh sedikit waktu.

Nah sekarang saatnya mengecek data itu. Jadi saya mengatakan bisa jadi pengangguran tidak lebih tinggi dari biasanya di 2024, dan saya bilang bisa saja di Aceh tinggi tapi di Jakarta rendah, so it's not so bad (or at least not worse than typical).

Untuk mengeceknya saya menggunakan tabel [tingkat pengangguran terbuka menurut provinsi](https://www.bps.go.id/id/statistics-table/2/NTQzIzI=/tingkat-pengangguran-terbuka-menurut-provinsi--persen-.html) dari BPS. BPS menggunakan survey Sakernas yang dilakukan di 2 bulan yang berbeda yaitu Februrari dan Agustus. Saya coba plot 10 tahun terakhir, masing-masing di Februari dan Agustus. Saya ambil beberapa provinsi aja, yaitu Aceh dan Jakarta (karena 2 daerah tersebut saya sebut di podcast), lalu Yogyakarta, Bali dan Maluku Utara (ga ada alasan khusus). Datanya ada di bawah ini.


```python
import seaborn as sns
import matplotlib as plt
import pandas as pd
```


```python
data=pd.read_excel("ur.xlsx")
feb=data.query("bulan=='Februari'")
aug=data.query("bulan=='Agustus'")
```


```python
ax=sns.lineplot(data=feb,x="tahun",y="ur",hue='daerah',palette='Paired')
sns.move_legend(ax,loc='lower right',bbox_to_anchor=(1.35,.5))
ax.set(xlabel="",ylabel="Tingkat pengangguran (%)",title="tingkat pengangguran tahunan bulan Februari")
```




    [Text(0.5, 0, ''),
     Text(0, 0.5, 'Tingkat pengangguran (%)'),
     Text(0.5, 1.0, 'tingkat pengangguran tahunan bulan Februari')]




    
![png](index_files/index_3_1.png)
    



```python
ax=sns.lineplot(data=aug,x="tahun",y="ur",hue='daerah',palette='Paired')
sns.move_legend(ax,loc='lower right',bbox_to_anchor=(1.35,.5))
ax.set(xlabel="",ylabel="Tingkat pengangguran (%)",title="tingkat pengangguran tahunan bulan Agustus")
```




    [Text(0.5, 0, ''),
     Text(0, 0.5, 'Tingkat pengangguran (%)'),
     Text(0.5, 1.0, 'tingkat pengangguran tahunan bulan Agustus')]




    
![png](index_files/index_4_1.png)
    


Obviously 2020 ada pandemi COVID-19 sehingga tingkat pengangguran langsung melonjak. Bali dan Jakarta mengalami problem yang jauh lebih tinggi dari daerah lain dan nasional (garis merah), sangat wajar mengingat 2 daerah ini sangat tinggi sektor jasa-nya.

Secara keseluruhan, bisa kita lihat bahwa 2024 Agustus dan Februari, tingkat pengangguran sudah mulai kembali ke tren awal. Di samping itu, Jakarta selama ini memang memiliki tingkat pengangguran yang tinggi, di atas rata-rata nasional, seperti halnya Aceh. Bahkan bisa dikatakan Jakarta seringkali lebih tinggi tingkat penganggurannya dibanding Aceh.

Singkatnya:

> (1) kemungkinan tingkat pengangguran memang tidak lebih buruk seperti yang di berita-berita, karena sudah mendekati tren 10 tahun terakhir, dan generally membaik sejak dikacaukan COVID. (2) Jakarta memiliki tingkat pengangguran yang setara dengan Aceh, dan tingkat pengangguran keduanya berada di atas rata-rata nasional.

Penting juga untuk diingat bahwa angka pengangguran saja tidak cukup untuk melakukan analisis terhadap lapangan kerja karena banyak indikator lain yang juga perlu diperhatikan. Pertama adalah pentingnya mengetahui **jumlah angkatan kerja**, yang bisa saja naik karena berbagai faktor (misalnya orang yang biasanya lanjut kuliah memutuskan tidak kuliah sehingga masuk angkatan kerja), atau bahkan turun (saking desperate-nya ga dapet kerja, sehingga memutuskan nyerah nyari kerja dan memilih nganggur). Berapa **jam kerja**-nya (orang bekerja menurut BPS adalah jika kerjanya setidaknya 1 jam seminggu. jadi bisa saja masih kerja tapi jam kerjanya berkurang, yang menunjukkan lesu-nya pasar tenaga kerja). Dan yang terpenting adalah berapa **upah** yang dibayarkan untuk jam kerja tersebut. Saya pernah bahas sedikit tentang potensi dampak UMK ke pasar tenaga kerja di [sini](https://www.krisna.or.id/post/umk/).

Dengan kata lain, sangat mungkin tingkat pengangguran tidak berbeda jauh, tapi sebenarnya yang terjadi adalah pengurangan jam kerja atau upah. Ini tuh mirip dengan harga _snack_ gak turun tapi isinya berkurang.

So yeah, menganalisis pasar tenaga kerja tidak semudah itu, makanya di kami ekonom pun bahkan pasar tenaga kerja bisa menjadi sebuah spesialisasi sendiri. Mudah-mudahan bapak ibu dan teman-teman lebih kritis ke depannya jika melihat angka-angka ini.

BTW, BPS mulai banyak diseminasi data soal upah, sebuah progres yang sangat perlu diapresiasi. Ini salah satu data soal upah yang ada di [website BPS](https://www.bps.go.id/id/statistics-table/2/MTE3MiMy/upah-rata---rata-per-jam-pekerja-menurut-provinsi--rupiah-jam-.html). Oh iya hati-hati juga melihat rata-rata yah karena rata-rata akan di-skew ke kiri dan terinflate oleh orang kaya, to some degree.

Mudah-mudahan postingan ini membantu klarifikasi.


```python
## This is a copilot generated code.
import pandas as pd
from io import StringIO

# Tab-delimited data
data = """daerah\t2015\t2016\t2017\t2018\t2019\t2020\t2021\t2022\t2023
ACEH\t11226\t13627\t14809\t13814\t15065\t18099\t17037\t16772\t17585
DKI JAKARTA\t17012\t23181\t23826\t25238\t25236\t28420\t30662\t32685\t42354
DI YOGYAKARTA\t10440\t12070\t12281\t12554\t13275\t15771\t15098\t14916\t16478
BALI\t11038\t14852\t15624\t15889\t16408\t17775\t17662\t16857\t18521
MALUKU UTARA\t13607\t15226\t15760\t15864\t17425\t23338\t21131\t18278\t27078
INDONESIA\t11434\t14068\t14731\t15275\t15823\t17696\t18089\t17542\t19027"""

# Use StringIO to read the string data into a pandas dataframe
df = pd.read_csv(StringIO(data), delimiter='\t')
df_long = pd.melt(df, id_vars=['daerah'], var_name='year', value_name='value')

## Seaborn
ax=sns.lineplot(data=df_long,x="year",y="value",hue='daerah',palette='Paired')
sns.move_legend(ax,loc='lower right',bbox_to_anchor=(1.35,.5))
ax.set(xlabel="",ylabel="Rp",title="Upah per jam, provinsi, Rupiah/jam")
```




    [Text(0.5, 0, ''),
     Text(0, 0.5, 'Rp'),
     Text(0.5, 1.0, 'Upah per jam, provinsi, Rupiah/jam')]




    
![png](index_files/index_6_1.png)
    

