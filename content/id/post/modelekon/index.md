---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Bagaimana cara ekonom berpikir:membuat sebuah Model Ekonomi Sederhana"
subtitle: ""
summary: ""
authors: [admin] 
tags: [perdagangan, ekonomi, python,general equilibrium]
categories: []
date: 2025-01-27T11:00:00+07:00
lastmod: 2025-01-27T11:00:00+07:00
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

Semakin maraknya pembicaraan soal swasembada dan anti-impor semakin kuat aja. Terakhir yang saya sering baca adalah soal [impor paksa sapi](https://www.youtube.com/watch?v=-G2EjOriAjY&t=1s) dan lebih serem lagi, soal [deklarasi tidak akan impor pangan](https://www.tempo.co/ekonomi/zulkifli-hasan-tegaskan-komitmen-soal-swasembada-pangan-stop-impor-beras-hingga-gula-mulai-tahun-ini-1195061). Ntah bagaimana cara pemerintah meningkatkan produktivitas pertanian, yang mana merupakan satu-satunya cara agar bisa memenuhi kebutuhan pangan domestik tanpa impor. Tapi sepertinya sih ketika harga terlihat mulai naik, kemungkinan besar impor bakal tetap dibuka.

Kayaknya perdagangan internasional adalah salah satu subyek yang banyak orang tuh susah banget nangkepnya. Bagi saya sendiri, perdagangan internasional ini ya memang subyek yang susah banget menjelaskannya. Padahal sebenarnya insightnya sangat straight-forward, simple, tapi kayaknya emang susah banget disampaikannya. Ga semua orang tuh langsung nangkep. Padahal tools di international trade itu sebenernya sama aja dengan tools di econ lain seperti di makro dan development. Tapi kenapa ya kayaknya susah banget ditangkep orang. Mungkin karena kontekstual? Ntahlah.

Tapi terlepas dari itu semua, saya memang sudah lama pengen bikin postingan soal bagaimana ekonom diajarkan permodelan. Seperti halnya anak teknik, anak ekonomi juga belajar model ekonomi dari simplifikasi matematika. Sebenernya tools buat anak-anak econ mirip-mirip kok sama anak teknik, yaitu tools-tools yang terpakai di optimal control. Ya, kalkulus, linear algebra, real analysis, set theorem, topologi gitu2 belajarnya. Kita juga biasanya memulai dengan memodelkan sesuatu yang simple dengan penuh restriksi (at times, far from reality). Nah, seiring perjalanan, asumsi-asumsi ini mulai dilepas satu-satu sehingga kita paham implikasinya di dunia nyata.

Hari ini saya coba ajak temen-temen "menyicip" apa yang diajarin di ekonomi di semester 1. Sukur-sukur pada tertarik jadi ekonom wkwkwkwkw.

## Ekonomi tertutup

Tidak seperti pemahaman populer, matematika sangat sentral perannya di ilmu ekonomi. Kita menggunakan matematika utamanya untuk bikin problem optimisasi model general equilibrium, dan untuk mencari hubungan kausalitas antar-variabel. Makanya sebenernya salah banget kalo ada orang yang masuk ekonomi dengan alasan gak suka matematika. Lagipula sebenernya matematika itu seru kok. Bisa kepake banget buat beresin masalah-masalah kehidupan. Well to a degree wkkw.

Mari kita buat sebuah model kecil untuk ekonomi sebuah negara dengan aturan main sebagai berikut:

1. Penduduk negara ini hanya mengonsumsi 2 jenis barang, yaitu pangan (A) dan sandang (B). Kombinasi konsumsi penduduknya mengikuti fungsi $U={A^D}^{\alpha}{B^D}^{\beta}$. Artinya, kombinasi konsumsi A dan B mana yang akan memaksimalkan kebahagiaan penduduknya, itulah yang dipilih. Pemilihan ini sensitif terhadap parameter kesukaan, yaitu $\alpha$ (seberapa cinta negara ini dengan pangan) dan $\beta$ (sandang).
2. Faktor produksi di negara ini adalah pekerja (L), di mana $L_A$ adalah pekerja di industri pangan dan $L_B$ adalah pekerja di industri sandang. Fungsi produksinya linear aja, seperti di ricardian economy, yaitu $A^S=f\times L_A$ dan $B^S=g\times L_B$, di mana $f dan g$ adalah parameter positif yang menunjukkan produktivitas industri masing-masing.
3. Jumlah total tenaga kerja di negara ini adalah $L$ dan pekerja di 2 industri tidak boleh lebih banyak dari ini, jadinya $L_A+L_B=L$.
4. ekonomi tertutup berarti demand harus sama dengan supply, atau $A^S=A^D$ dan $B^S=B^D$ karena kelebihan produksi yang tidak dikonsumsi tidak bisa diekspor, dan kekurangan konsumsi yang tidak diproduksi tidak bisa diimpor[^1].

Dengan kata lain, objective function dari ekonomi kecil kita ini adalah:



$$
\max_{A^D,B^D} \ {A^D}^{\alpha}{B^D}^{\beta}
$$

$$
\text{subject to } \ A^S=f\times L_A
$$

$$
B^S=g \times L_B
$$

$$
L_A+L_B=L
$$

$$
A^S=A^D, B^S=B^D
$$



Alias, sebuah negara ada untuk memaksimalkan kebahagiaan warganya, yang di persamaan ini diwakilkan oleh $U$. si $U$ sendiri akan makin besar seiring naiknya konsumsi barang dan jasa, yang di model ini cuma diwakili 2 barang, yaitu $A$ dan $B$. Satu-satunya alasan kenapa kita tidak bisa semena-mena naikin $A$ dan $B$ adalah karena keterbatasan sumber daya, dalam hal ini diwakilkan oleh $L$ atau sumber daya manusia. Nah, nanti lama-lama semakin banyak barang dan sumber daya yang bisa kita tambahkan ke persamaan ini. Tapi untuk sekarang, kita mulai dari yang simpel dulu.

Kita bisa langsung mengaplikasikan substitusi dengan memanfaatkan fakta bahwa permintaan sama dengan penawaran $e.g., \ (A^S=A^D=A)$, sehingga kita akan punya reduced form seperti ini:

$$
\max_{L_A,L_B} \ (fL_A)^{\alpha}(gL_B)^{\beta}
$$

$$
\text{subject to } \ L_A+L_B=L
$$



dan problemnya jadi jauh lebih simple, serta essentially problem kita di atas adalah soal **alokasi tenaga kerja**. Problem di atas cukup trivial untuk diselesaikan dengan lagrange untuk kasus tertentu.

Setelah kita kerjain lagrange-nya, kita akan mendapatkan solusi alokasi tenaga kerja sebagai berikut:

$$
L_A=\frac{\alpha}{\alpha+\beta} L
$$

$$
L_B=\frac{\beta}{\alpha+\beta} L
$$

Dengan kata lain, jumlah penduduk negara ini akan bekerja di sektor pangan akan tergantung dengan 3 hal:

1. seberapa besar kecintaan penduduk negara ini dengan produk pangan relatif terhadap sandang ${\alpha}{\alpha+\beta}$. semakin besar $\alpha$ relatif terhadap $\beta$, maka semakin banyak juga penduduk yang kerja di sektor tersebut karena permintaan akan produknya besar.
2. Seberapa besar ukuran tenaga kerjanya $(L)$. cukup jelas.

Bagaimana dengan harga dan upah? Bagi awam yang selama ini menjalani kehidupan sehari-hari dengan menggunakan level harga dan upah untuk mengambil keputusan, mungkin tidak begitu familiar dengan konsep bahwa harga relatif. Bahwa harga dan upah, atau lebih tepatnya mata uang sebagai "barang" yang fungsinya cuma menjembatani transaksi. Artinya, harga cuma sebuah "jembatan". Pada hakekatnya, kita membeli barang dan jasa bukan dengan uang, tapi dengan jam kerja. Alias, berapa jam kerja yang harus saya berikan untuk mendapatkan barang sejumlah X. Uang hanyalah jembatan.

Misalnya, kita kerja seminggu 40 jam dengan gaji 2 juta. 2 juta itu dipakai untuk 1 unit pangan 1,5 juta dan 1 unit sandang 500 ribu. Dengan kata lain, untuk beli 1 unit sandang dan 1 unit pangan, kita butuh 2 juta. Untuk dapat 2 juta, kita butuh kerja 40 jam. Kalau 2 juta-nya di-bypass, sebenernya "harga" dari membeli 1 unit sandang dan pangan adalah 40 jam kerja. Di dunia matematika, kita ga butuh tuh harga pangan dan upah. Kita ga butuh $L \rightarrow w \rightarrow p \rightarrow A+B$ karena ya langsung aja $L \rightarrow A+B$.

Tapi let's say kita mau punya harga dan gaji buat ancer-ancer. Kita bisa gunakan pendekatan dari sisi produksi.

Kita kudu nambah asumsi untuk hitung harga dan gaji. Asumsi berikutnya adalah pekerja bisa pindah industri. Jadi jika gaji di industri A lebih tinggi dari di industri B, maka orang akan pindah ke industri A. Seiring dengan orang pindah ke industri A, industri A bisa nurunin upah karena sekarang banyak yang mau ke A, sementara upah di B akan naik karena mereka kekurangan tenaga kerja. Dinamika ini akan terus terjadi sampai upah di kedua industri mencapai ekuilibrium di angka yang sama.

jadi kita tambah parameter at least 3, yaitu $p_A, p_B \text{ dan } w$ alias harga barang A, harga barang B, dan gaji. Asumsi berikutnya yang perlu ditambahin adalah perfect competition di mana kedua industri akan menghabiskan semua profitnya untuk menggaji pegawai. Artinya, revenue dari hasil penjualan barang A akan sama dengan belanja pegawai, atau upah kali jumlah tenaga kerja:

$$
p_A\times A = w \times L_A
$$

$$
p_A \times fL_A = w \times L_A
$$

$$
p_A\times f=w
$$

$$
\frac{w}{p_A}=f
$$


Ini adalah kondisi di mana gaji dibayar secara fair sesuai dengan produktivitas. Karena $f$ adalah produktivitas pekerja di industri $A$, maka mereka dibayar sebesar $w/p_A$ atau upah riil untuk barang A.

Nah karena industri B juga punya karakteristik yang sama, maka kondisi di B juga bakal kayak gitu (alias, $p_B \times g=w$). Nah karena 2 2 nya membayar upah yang sama-sama $w$, maka kita bisa lakukan substitusi untuk mendapatkan $fp_A=gp_B$ yang artinya relatif price untuk kedua industri adalah:

$$
\frac{p_A}{p_B}=\frac{g}{f}
$$

Artinya, harga barang keduanya tergantung produktivitas relatif kedua barang tersebut. Di negara dengan produktivitas pangan lebih tinggi relatif terhadap produktivitas sandang (alias, $\frac{g}{f}<1$), maka harga pangan akan cenderung murah relatif terhadap harga sandang (atau, $\frac{p_A}{p_B}<1$). Sebaliknya juga sama, jika produktivitas relatif suatu negara lebih tinggi di sandang, maka harga sandang di negara tersebut akan lebih rendah.

Nah, kita juga bisa kalkulasi jumlah barang yang diproduksi dengan:

$$
A=fL_A=fL \frac{\alpha}{\alpha+\beta}
$$

$$
B=gL_B=gL \frac{\beta}{\alpha+\beta}
$$

Sementara itu utility atau kebahagiaan di negara ini juga bisa kita hitung dengan:

$$
U=A^{\alpha}B^{\beta}
$$

$$U=\left(\frac{\alpha}{\alpha+\beta}\right)^\alpha (fL)^{\alpha}\left(\frac{\beta}{\alpha+\beta}\right)^{\beta} (gL)^{\beta}$$

$$U={\alpha^\alpha}{\beta^\beta}\left({\alpha+\beta}\right)^{-\left(\alpha+\beta\right)}L^{\alpha+\beta}f^\alpha g^\beta$$


Selanjutnya kita tinggal hitung. Karena saya pemalas, saya malas hitung secara manual. Karena itu mari kita buat `class` python sederhana untuk menulis contoh model di atas. Saya akan sekalian pasang beberapa parameter _default_ untuk jumlah total labor, produktivitas, dan preferensi warga. Di sini saya pasang _default_-nya 200 untuk jumlah pekerja (anggeplah diukur dalam juta orang). Lalu untuk teknologi, saya pasang kondisi di mana negara ini lebih produktif bikin sandang daripada pangan. Preferensi dibuat seimbang dengan restriksi $\alpha+\beta=1$. Terakhir, gaji di sini dipasang 1. Tapi kalau mau dibuat 5 juta misalnya, juga bisa sih.


```python
# Bikin class dulu
# Optimisasi sudah dilakukan dengan tangan di atas, jadi class-nya ga perlu optimisasi lagi. tinggal kalkulasi biasa.
import pandas as pd
import numpy as np

class ekon:
  r"""
  
  toy model of a closed economy with fixed number of labor, fixed productivity, 2 goods A and B, 1 factor of production.

  

  """
  
  def __init__(self, L=200,
                     f=0.25,
                     g=0.75,
                     alpha=0.5,
                     beta=0.5,
                     w=1,

                     
                     ):
    self.L,self.f,self.g,self.alpha,self.beta,self.w=L,f,g,alpha,beta,w
    
  def hasil(self):
    L,f,g,alpha,beta,w=self.L,self.f,self.g,self.alpha,self.beta,self.w
    LA=alpha/(alpha+beta)*L
    LB=beta/(alpha+beta)*L
    A=f*LA
    B=g*LB
    U=(A**alpha)*(B**beta)
    pa=w/f
    pb=w/g
    p=pa*(A/(A+B))+pb*(B/(A+B))
    npdb=pa*A+pb*B
    pdb=npdb/p
    return print(f'Goods market: \n harga A adalah {pa:,.2f} dan harga B adalah {pb:,.2f} \n Jumlah produksi (A,B) adalah {(A,B)} \nLabor market: \n gaji adalah {w:,.2f} \n dari total {L:,.2f} pekerja, sebanyak {LA:,.2f} bekerja di industri A dan {LB:,.2f} di industri B \nmakro: \n PDB nominal adalah {npdb:,.2f} \n PDB riil adalah {pdb:,.2f} \n level harga adalah {p:,.2f} \n welfare di negara ini adalah {U:,.2f}')
```

Kita tes modelnya yuk. Pertama, run kode di atas, lalu run default parameters dengan cara di bawah ini.


```python
ekon().hasil()
```

    Goods market: 
     harga A adalah 4.00 dan harga B adalah 1.33 
     Jumlah produksi (A,B) adalah (25.0, 75.0) 
    Labor market: 
     gaji adalah 1.00 
     dari total 200.00 pekerja, sebanyak 100.00 bekerja di industri A dan 100.00 di industri B 
    makro: 
     PDB nominal adalah 200.00 
     PDB riil adalah 100.00 
     level harga adalah 2.00 
     welfare di negara ini adalah 43.30
    

Sesuai prediksi, harga A (pangan) lebih tinggi daripada harga B (sandang) karena ekonomi negara ini lebih produktif membuat sandang daripada pangan.

Tentu saja kita bisa coba pakai angka lain. Let's say kita punya negara lain dengan karakteristik jumlah tenaga kerja 400 juta orang dan relatif lebih produktif agrikulturnya daripada pakaian jadi-nya. Oh, kita juga bisa misalkan wage level di negara ini lebih tinggi 3x lipat daripada negara sebelah.


```python
ekon(L=400,w=3,f=0.8,g=0.2).hasil()
```

    Goods market: 
     harga A adalah 3.75 dan harga B adalah 15.00 
     Jumlah produksi (A,B) adalah (160.0, 40.0) 
    Labor market: 
     gaji adalah 3.00 
     dari total 400.00 pekerja, sebanyak 200.00 bekerja di industri A dan 200.00 di industri B 
    makro: 
     PDB nominal adalah 1,200.00 
     PDB riil adalah 200.00 
     level harga adalah 6.00 
     welfare di negara ini adalah 80.00
    

Katakanlah negara pertama kita sebut Home (H) sementara negara ke-2 kita sebut Foreign (F). Ciri utama adalah negara F lebih besar (400 pekerja dibanding 200) dan lebih produktif di agrikultur ketimbang garmen. Kita langsung lihat bahwa negara H membuat A=25 dan B=75, lebih condong banyak bikin B. Sementara itu, negara F lebih berat ke A, membuat A sebanyak 160 sementara B sebanyak 40, atau perbedaan 4 kali lipat.

Kita juga bisa bereksperimen dengan karakteristik lain, misalnya negara F lebih suka garmen sehingga $\beta=0.7$ sementara $\alpha=0.3$, dan lain sebagainya.

Nah pertanyaan lebih menariknya adalah, apa yang terjadi kalau kedua negara ini melakukan trade? Ntar ya saya bikinin lagi kalo postingan ini rame wkwk.
