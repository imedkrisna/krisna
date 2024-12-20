---
layout: post
title: "Jumlah tes COVID-19 per hari di Indonesia"
categories: [coronavirus COVID-19]
tags: [coronavirus COVID-19,python]
author: admin
date: '2020-05-31'
slug: tesharian
---

Sepertinya pemerintah semakin semangat menyongsong “New Normal” dan mulai membuka ekonominya. Telah beredar buku pedoman bagaimana menghadapi “New Normal” [dari BPOM](https://investor.id/lifestyle/bpom-menerbitkan-buku-panduan-lengkap-covid19). Berita bahwa mal akan dibuka santer beredar di mana-mana (tapi katanya [summarecon mal bekasi gak jadi buka](https://metro.tempo.co/read/1346375/ini-agenda-presiden-jokowi-ke-bekasi-siang-ini-bukan-buka-mal) ntahlah akupun bingung). Ekonomi akan kembali bergeliat!

Kalo menurut banyak sumber ([misalnya salah satunya ini](https://www.abc.net.au/indonesian/2020-05-27/who-mengatakan-gelombang-pertama-covid-19-masih-tinggi/12291202)), kunci sukses membuka ekonomi yang berhasil adalah pertumbuhan tes per hari yang banyak, alias, massive testing. Tapi apakah kita udah berhasil bikin massive testing yang cukup?


```python
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
c=pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
c['date']=pd.to_datetime(c['date'])
y=c['new_tests'][c['iso_code']=='IDN']
y1=c['new_tests_smoothed'][c['iso_code']=='IDN']
x=c['date'][c['iso_code']=='IDN']
plt.figure(figsize=(15,5))
#nt=sns.load_dataset("c")
sns.lineplot(x=x, y=y, data=c)
sns.lineplot(x=x, y=y1, data=c)
```

![png](/images/output_1_1.png)


Gambar di atas menunjukkan jumlah “new test” per hari. saya ambil datanya dari [our world in data](https://ourworldindata.org/coronavirus-data). Datanya di-update setiap hari sesuai dengan laporan pemerintah. di sumbu x saya kasih tanggal, sementara di sumbu y adalah variabel yang namanya “new_tests” kalo di dataset aslinya. Intinya mah ini adalah tes harian CMIIW.

jumlah tes hariannya adalah titik-titik dan garis item, sementara garis biru menunjukkan smoothed new tests, alias yang diperhalus.

Intermezzo dikit, kode di atas dirun pake python versi 3.7. Data langsung dibaca dari portal online-nya our world in data, jadinya setiap di-run, bakal langsung update data terbaru. Kalo anda punya python di komputer masing-masing, bisa langsung dikopas tuh kode di atas kalo penasaran data terbaru kayak apa.

Jumlah tes harian Indonesia keliatan banget bolong-bolongnya, dan keliatannya sampai 26 Mei 2020, jumlah tes harian kita masih volatil banget. Naik turunnya agak ga jelas. Beberapa pendapat yang saya lihat di twitter sih bilangnya jumlah tes harian emang sulit diperkirakan karena faktornya nggak cuma jumlah swab yang dilakukan, tapi juga antrian sampel-sampel tersebut di lab. Jadi bisa jadi angka yang muncul itu sebenernya hasil swab kemaren yang baru di-tes hari ini.

Saya nggak terlalu ngikutin sih perdebatan testing COVID-19 hahaha maaf. Dah lama nggak update COVID-19, cuma gara-gara tiba-tiba ada rame-rame pembukaan ekonomi kembali, jadinya penasaran. Selain itu, katanya Bio Farma sudah berhasil bikin PCR test kit sendiri, [bahkan diklaim sanggup bikin 100,000 per hari](https://tirto.id/jokowi-klaim-indonesia-produksi-alat-rapid-tes-pcr-100-ribu-hari-fzhZ). Dengan asumsinya logistik ke lab dan proses di lab-nya lancar dan cukup kapasitas, sepertinya masif testing dapat dilakukan. Mudah-mudahan peningkatan ini berlanjut terus dan bisa *sustainable* di masa *new normal* ini.

Oh iya, datanya dari pemerintah pusat, sementara data pemerintah pusat adalah hasil tes mereka plus tes yang dilakukan oleh pemerintah daerah (dan mungkin swasta?). Meskipun kita nggak tau data selain dari pemerintah pusat, setidaknya pemerintah daerah tau data daerahnya sendiri. hehe.

BTW, negara lain juga “new tests”-nya agak aneh. New Zealand dan Malaysia juga volatil sementara Jepang nggak report new tests nya (tapi totalnya ada). Vietnam malah mendadak turun trus ilang di tengah jalan. Jadi mungkin ini sebabnya Pak Jokowi sangat percaya diri he he he he.


```python
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
c=pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
c['date']=pd.to_datetime(c['date'])
plt.figure(figsize=(15,10))
#cn=c.drop(c[(c['iso_code'] != 'IDN')| c[(c['iso_code'] != 'VNM') | c[(c['iso_code'] != 'SGP') | c[(c['iso_code'] != 'AUS') | c[(c['iso_code'] != 'MYS')].index)
cn=c[(c['iso_code'] == 'IDN') | (c['iso_code'] == 'VNM') | (c['iso_code'] == 'MYS') | (c['iso_code'] == 'JPN') | (c['iso_code'] == 'NZL')]
sns.lineplot(x="date", y="new_tests", hue="iso_code", style="iso_code",data=cn)
```

![png](/images/output_3_1.png)


Ini saya pake tes harian, bukan tes harian per 1,000 penduduk. soalnya kalo pake tes harian, negara laen jauh bgt di atas. Indo jadi kayak garis lurus doang hahaha. Eniwe sebenernya di sini saya mau coba pake argumen “berani open karena kapasitas testing sudah ditingkatkan”. Kalau pake argumen ini kayaknya lumayan, secara tren kita udah naik. Tentu saja apakah itu dah cukup atau belum, masih subyek debat yang saya yakin udah banyak yang bahas.

Akhir kata, alasan dibalik keputusan membuka kembali ekonomi tentu ada banyak, tidak hanya tes aja. Saya tidak coba membahas alasan-alasan yang lain selain peningkatan kapasitas testing. Postingan kali ini simply cuma untuk ngasi liat gambaran singkat bagaimana perkembangan testing harian kita. Cukup lah yang lain biar menjadi perdebatan orang-orang yang lebih ahli hehe.
