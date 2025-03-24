---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Menyikapi input-output analysis Dewan Ekonomi Nasional untuk menunjukkan dampak makroekonomi program Makan Bergizi Gratis"
subtitle: ""
summary: ""
authors: [admin]
tags: [CGE, ekonomi]
categories: [CGE, ekonomi]
date: 2025-03-23T12:06:59+07:00
lastmod: 2025-03-23T12:06:59+07:00
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

Cukup mengejutkan tapi menarik waktu saya lihat [konferensi pers](https://www.youtube.com/watch?v=YapJrjVDYpY) Dewan Ekonomi Nasional (DEN) beberapa waktu lalu. Alasannya adalah karena Pak Luhut Binsar Panjaitan (LBP), ketua DEN, memberikan _spotlight_ untuk Profesor Arif Anshory Yusuf (AAY) untuk memberikan _teaser_ hasil model _ex=ante_ beliau tentang dampak program Makan Bergizi Gratis (MBG) terhadap perekonomian. Menurut AAY, MBG berpotensi menambah pekerjaan untuk 1.9 juta orang dan menurunkan kemiskinan sampai 5.8%. MBG, menurutnya, setara dengan memberikan uang 600 ribu per keluarga jika rata-rata anak-anak di keluarga miskin ada 3 orang. Angka ini 3x lipat dari PKH! Dia juga menambahkan bahwa untuk merealisasikan dampak maksimal MBG, maka "Kebocoran" permintaan bahan pangan "yang tidak perlu diimpor" dengan mengutamakan produk dalam negeri.

Kemudian pada tanggal 23 Maret 2025 malam waktu Jakarta, saya menyaksikan presentasi Profesor Arief Anshory Yusuf (AAY) tentang paper terbaru yang ia tulis untuk Dewan Ekonomi Nasional (DEN). Acara ini diselenggarakan oleh Doctrine UK, sebuah perkumpulan mahasiswa Indonesia di Inggris. Di sana, ia menyampaikan paper tentang analisis dampak makroekonomi program Makan Bergizi Gratis (MBG). Papernya sendiri dibagikan di chat acara tersebut.

Setelah melihat baik papernya maupun presentasinya, saya merasa perlu untuk menulis beberapa catatan tentang papernya. Tujuan utamanya sih sebenernya buat diri saya sendiri, karena model ini cukup seru untuk dikulik dan direplikasi. Selain itu, di acara tersebut, Pak AAY juga membawa nama DEN, yang berarti kebijakan yang munjul dari paper ini dapat dianggap datang dari pemerintah dan kemungkinan akan menjadi kebijakan publik. Saya juga nulis ini buat teman-teman belum begitu paham CGE[^1], tapi pengen belajar. Terakhir, sukur-sukur postingan ini dibaca oleh beliau dan DEN, tapi saya yakin sih orang dengan kaliber beliau pasti udah dapat banyak masukan dari orang-orang yang lebih keren dari saya, jadi tujuan ini ga begitu penting. Mostly, postingan ini untuk belajar dan berbagi.

Saya sangat menghormati beliau sebagai akademisi karena AAY adalah satu dari sedikit ekonom Indonesia yang sangat vokal terhadap isu-isu ekonomi di Indonesia, terutama tentang Pendidikan Tinggi dan program pro-poor dan pro-job. Beliau tidak segan-segan mengkritik pemerintah. Bahkan paper beliau yang menjadi justifikasi _ex-ante_ MBG dibagikan ke semua dan ia juga rajin presentasi dan minta pendapat dari banyak sekali orang di berbagai kalangan. Level transparansi ini tidak saya temukan di kebijakan pemerintah yang lain.

_Having said that_, saya punya beberapa catatan yang menurut saya sangat penting dan _worth_ ditulis di blog. Saya akan fokus ke 2 caveats yang ia sampaikan di paparannya. Untuk bagian lain, bisa jadi kesempatan dan untuk teman-teman yang lain yang mau sumbang komen ke beliau awokwokwok.

Saya akan mulai dengan sedikit merangkup hal-hal yang saya sepakat, baru move on ke hal-hal yang saya kurang paham/tidak setuju.

## Hal penting menurut saya

Di papernya, AAY merangkum berbagai studi tentang program semacam MBG di negara lain. Di negara lain, menurutnya, MBG cukup sukses. Dia juga bilang bahwa MBG adalah program yang sangat progresif. Saya rasa agak sulit untuk tidak setuju bahwa MBG, sebagai konsep, adalah program yang progresif.

Di paper itu juga dijelaskan sedikit detil tentang MBG yang juga konsisten dengan penjelasan dari tempat lain (misalnya CISDI). Ia menyebut budget 171 triliun rupiah, _one of the largest welfare program in the world_, dengan target penerima sekitar 82,9 juta masyarakat.

Tidak kalah penting: AAY menyebutkan beberapa tujuan resmi MBG: better nutrition, job creation, supporting local food systems, and improving student attendance and health.

Akhirnya, AAY menggunakan analisis input-output (IO) dan mikrosimulasi untuk menunjukkan dampak ekonomi berupa peningkatan output, value added, dan lapangan kerja, serta penurunan kemiskinan dari program ini. Ada berbagai simulasi dengan skenario yang dilakukan, tapi hasilnya konsisten positif secara umum.

## Large caveats

Hanya saja, Di paparannya, AAY mengatakan dua caveats yang sangat heroik dan otomatis mendismiss banyak sekali diskusi tentang MBG:

1. Model ini adalah skenario _ex-ante_ dengan asumsi pelaksanaannya berjalan dengan ideal. Semua kritikan terkait aspek operasional tidak dapat dijawab dengan paper ini.
2. Tidak ada aspek aspek general equilibrium, sehingga perubahan harga tidak ada di model ini.

Menurut saya pribadi, dua hal tersebut justru dua hal yang _arguably_ paling berpengaruh terhadap hasil simulasi yang dilakukan di paper tersebut. Di acara Doctrine UK tempo hari, mungkin mayoritas pertanyaan dan diskusi peserta justru adalah tentang best practice dan kesiapan institusi.

Di postingan ini, saya akan fokus ke no.2 dulu, yaitu bahwa ia berargumen IO analysis $\neq$ Computable General Equilibrium (CGE), dan IO tidak memperhitungkan adanya perubahan harga. Saya akan nerding out a bit soal CGE untuk menjawab caveat no.2.

## Aspek General Equilibrium

### Adding context: Tentang Input-Output Analysis (IO)

Di paper tersebut, AAY menjelaskan IO di 3.1.1., wicis di halaman 4 di papernya. Bagian ini akan jadi terlalu _geeky_. Baca dengan risiko masing-masing. You've been warned.

Ada 3 istilah penting yang dipakai AAY ketika menjelaskan IO analysis, yaitu output, value added, dan employment. Output pada prinsipnya adalah produksi total dari suatu industri. Value added adalah total produksi dikurangi dengan input / bahan baku. Jadi value added isinya adalah faktor produksi, _mainly_ pekerja (labor) dan modal (capital). nah, labor ini sama dengan employment.

Struktur IO di paper AAY sama persis dengan typical IO model yang lebih kurang begini:

$$x=Ax+y // 
(I-A)x=y // 
x=(I-A)^{-1}y$$

di mana hasil akhir vektor x melambangkan input demand untuk sektor $i$. artinya, input demand dari vektor $i$ tergantung dari shift-share $A$ dari setiap industri di $x$ untuk setiap industri di $x$, dan demand akhir $y$.

Dalam tabel Input-Output, kita bisa tunjukkan output dan value added jika anda buka actual tabel IO dari BPS.

| wew | s1 | s2 ... sj | y | sum |
| --- | --- | -------- | --- | --- |
| s1 | $q_{1,1}$ | $q_{1,2} \dots q_{1,j}$ | $y_1$ | $x_1$ |
| s2 | $q_{2,1}$ | $q_{2,2} \dots q_{2,j}$ | $y_2$ | $x_2$ |
| $\vdots$ | $\ddots$ | $\ddots$ | $\vdots$ | $\vdots$ |
| si | $q_{i,1}$ | $q_{i,2} \dots q_{i,j}$ | $y_i$ |
| va | $va_1$ | $va_2 \dots va_j$ | - | GDP |
| sum | $x_1$ | $ x_2 \dots x_j$ | GDP | - |

Di sini, $q_{i,j}$ bisa dibentuk menjadi matrix yang sama dengan $Ax$ dengan mengeset $q_{i,j}=a_{i,j}x_i$. Moga-moga kebayang ya. ha ha ha.

Biasanya, matrix $Ax$ diset dengan suatu optimisasi (you know, lagrange and stuff). Nah, typically, matrix A di analisis IO itu exogen. Dengan kata lain, elemen dari matrix A sudah tidak bergerak, dan hanya expansi seiring dengan output $x$. Karena itu, semua perubahan eksogen di ekonomi (dalam hal ini pada $y$) dianggap hannya expand sesuai matrix A.

Sebenernya IO itu ya CGE juga. Cuma, IO adalah _special case_ dari CGE, yaitu fungsi permintaan outputnya punya sifat _perfect complement_. Perfect complement ini asumsi yang sangat berguna karena optimisasinya jadi linear. Secara komputasi jadi jauh lebih mudah karena kita cukup pake linear algebra tanpa ada optimisasi non-linear apapun.

Di samping itu, Leontief itu enak karena optimisasinya hanya ekspansi sesuai share optimal masing-masing komponennya.

Misalnya, Sebuah input function $U=min(a_1x_1,a2_x2)$ akan memiliki titik optimal di $a_1x_1=a_2x_2$ sehingga demand function dari si $x_1$ akan berupa $x_1=\frac{a_2}{a_1}x_2$ dan $\frac{a_2}{a_1}$ ini akan konstan dan fixed sepanjang komposit barang konsumsinya.

Metode ini relatif tidak sulit dilakukan di Python, selama matriks IO-nya ada. Saya coba pake versi lite, [yang 17 sektor](https://www.bps.go.id/en/statistics-table/1/MjI2OSMx/tabel-input-output-indonesia-transaksi-domestik-atas-dasar-harga-dasar--17-produk---2020--juta-rupiah-.html). Saya coba replikasi skenario A1 di papernya.




```python
import numpy as np
A=np.loadtxt('A.csv',delimiter=',') # matrix A
#y=np.loadtxt('y.csv',delimiter=',') ini final demand yang ada final importnya
u=np.loadtxt('x.csv',delimiter=',') # output
y=u-np.dot(A,u) # final demand tanpa final import
ia=np.identity(17)-A
invA=np.linalg.inv(ia)
np.savetxt('invA.csv', invA,delimiter=",") # save the change matrix result to a new file
x=np.dot(invA,y) ## Make sure replikasi final output di tabel.
x-u
```




    array([ 0.00000000e+00,  4.76837158e-07,  9.53674316e-07,  1.19209290e-07,
           -1.49011612e-08, -4.76837158e-07,  4.76837158e-07,  0.00000000e+00,
            2.38418579e-07,  0.00000000e+00,  0.00000000e+00, -1.19209290e-07,
            0.00000000e+00, -1.19209290e-07,  1.19209290e-07, -1.19209290e-07,
           -1.19209290e-07])




```python
## Simulasi MBG A1 di paper AAY
yy=y+np.array([0,0,0,0,0,0,0,0,171e6,0,0,0,0,-171e6,0,0,0]) ## + MBG shock - budget shock
xx=np.dot(invA,yy)
print(f'perubahan %output sektoral setelah +MBG-penghematan:\n {(xx-x)/x*100}') ## Percent change of sectoral output
```

    perubahan %output sektoral setelah +MBG-penghematan:
     [  1.08864224   0.03824485   0.57615184  -0.79322713  -0.71996072
      -0.27533884   0.34350708  -0.80514386  13.29429074  -1.13615204
       0.0553673   -0.13483742  -1.60608706 -22.73385632  -0.14187647
      -0.18583608  -0.23295487]
    


```python
print(f'pertumbuhan output nasional adalah {(np.sum(xx)-np.sum(x))/np.sum(x)*100} persen') ## Percent change of total output
```

    pertumbuhan output adalah 0.046445748306372714
    

| indikator | ori | kawe |
| ------ | --- | --- |
| Output nasional | 0.06 | 0.046 |
| Agriculture | 1.37 | 1.08 |
| manufacture | 0.12 | 0.57 |

Hasil simulasi A1, yang ori punya pak AAY, yang kawe punya saya. yah ga beda jauh sih jadi keknya lumayan bener wkwkwk.

Langsung terlihat ada setidaknya 3 keterbatasan terhadap penggunaan model ini.

Pertama adalah keterbatasan asumsi _constant shift-share_ a la Leontief. Hal ini langsung terlihat dari sumber pertumbuhan. realokasi _balance budget_ memberikan tambahan output positif karena sektor jasa penyedia makanan memiliki "total multiplier" (kalo di papernya term $m_{ij}$ dan $m_{ik}$, pp.6) yang lebih besar daripada jasa pemerintahan. Masalahnya si total multiplier ini konstan regardless mau ditambahin atau dikurangin berapapun. Tanpa adanya perubahan marginal return, maka jika yang diincar adalah pertumbuhan output, ya sekalian aja SEMUA output di jasa government kita pindahin ke sektor jasa penyedia makanan (aka corner solution). Tapi di dunia nyata kan ga terjadi, karena seiring suatu sektor kekurangan output, marginal productivity di situ akan naik, sementara sektor yang sudah bloated akan diminishing, menghilangkan gain seiring semakin banyaknya resources yang masuk ke situ. Plus, di demand juga ada merginal utility yang berubah seiring pola konsumsi cendering konsentrasi ke satu layanan. Hal ini tidak jadi masalah jika shocknya relatif kecil. Tapi mengingat shock MBG ini sampe naikin sektor jasa makanan sampai 13.3% dan motong sektor jasa pemerintah sampe -22.73%, kayaknya constant marginal return ini bakal jadi masalah.

Kedua adalah bahwa vektor $y$ dianggap final demand terakhir, tanpa mempertimbangkan ekspor impor. Indeed, di kolom $y$ di tabel IO BPS tuh aslinya ada pembentuk modal dan ekspor, yang di sini diagregasi ke dalam $y$. Sementara itu, di kolom pertama harusnya ada baris impor bahan baku. Di CGE, kita sering kali menambah sebuah fungsi substitusi dengan elastisitas armington antara input impor dan domestik untuk setiap sektor. Tentu saja ketiadaan perdagangan internasional (atau lebih tepatnya menganggap shift-share international trade as exogeneous/constant) mengakibatkan sulitnya meramal dampak MBG terhadap ekspor impor. Karena itu, Pak AAY di acara [ini](https://www.youtube.com/watch?v=YapJrjVDYpY) bilang something like MBG akan berdampak baik selama tidak ada "kebocoran", bahwa "bahan yang tidak perlu diimpor" sebaiknya tidak diimpor. I think this is not the best way to conclude from the model.

More importantly, di paper AAY, saya tidak menemukan info tentang tabel mana yang ia gunakan untung melakukan analisis. Hal ini penting karena di BPS tuh IO table-nya ada 2 jenis, yaitu menggunakan [total transaksi](https://www.bps.go.id/en/statistics-table/1/MjI3MSMx/indonesia-input-output-table-for-total-transactions-at-basic-prices--17-products---2020.html) dan [transaksi domestik](https://www.bps.go.id/en/statistics-table/1/MjI2OSMx/tabel-input-output-indonesia-transaksi-domestik-atas-dasar-harga-dasar--17-produk---2020--juta-rupiah-.html). Di tabel domestik tu hanya ada angka input domestik untuk matrix $Ax$, dan impor semua dipool di baris 2000. Di total, matriks $Ax$-nya udah termasuk impor sehingga baris 2000-nya kosong. Tidak ada info di papernya apakah dilakukan kalibrasi armington untuk pilihan produk domestik vs impor.

Jika tabel transaksi domestik yang digunakan, berarti matriks $Ax$ tidak mencerminkan keseluruhan input (cenderung bias), implicitly menganggap impornya fixed sehingga muncul "jangan bocor" tadi dan bisa jadi sesuai dengan apa yang modelnya katakan. Tapi jika transaksi total yang digunakan, maka matriks $Ax$ sudah _include_ barang impor juga di dalamnya dan mungkin saja sebenernya "bocor" di model dan ga ada konsekuensi jelek apapun. Atau bisa aja saya yang gak bener bacanya dan sebenernya dikasih tau prosedur ngeluarin imported input ini wkkwkw. Tapi ya mestinya bisa dipertegas di papernya.

Tapi kritik soal neraca perdagangan yang eksogen sebenarnya terkait sangat dengan kritik ke-2: tidak adanya prices. Ketiadaan prices sebenarnya menjadi super relevan ketika kita menggunakan model dengan optimisasi dan _constraint_. Tanpa constraint, tentu seolah-olah produksi di sektor yang ketimpaan MBG akan bisa berkembang sejauh $Ax$. Padahal, constraint dari sisi supply lah yang akan mengakibatkan inflasi. Ketika ada (budget) constraint, maka optimisasi harus dilakukan dan akibatnya akan muncul _income effect_ dan _substitution effect_ (jika pake asumsi selain leontief). In particular, _income effect_ ini akan sangat ngaruh ke perlunya ekspor/impor, tapi lebih penting lagi ke konsumsi total dan perhitungan kemiskinan.

Let me explain.

### Constraint and prices

Di Leontief assumption, ketika kita melakukan _shock_ terhadap final demand (di kolom $y_i$ di mana $i=$ sektor yang dishock), output dari sektor yang di-_shock_ akan meningkat, dan input demand dari sektor tersebut akan meningkat, terlihat di kolom $s_j$ di mana $j=$ sektor yang mengalami perubahan $y$.

misalnya demand di sektor $k$ meningkat jadi $y_k+1$ sehingga vektor $y$ berbentuk kayak gini:

$$
  y+\begin{bmatrix}
  0 \newline
  \vdots \newline
  1 \newline
  \vdots \newline
  0 
  \end{bmatrix}
  
$$

mari kita namakan dia vektor $d$ sehingga $y_n=y+d$

$$x_n=(I-A)^{-1}(y+d)$$

$$x_n=(I-A)^{-1}y+(I-A)^{-1}d$$

$$x_n=x+(I-A)^{-1}d$$

perubahan yang terjadi pada input demand dari sektor $k$ adalah exactly $(I-A)^{-1}$. Pak AAY menjelaskan ini di halaman 6 di papernya. Nah, term tersebut mengandung matriks identitas dan matriks $A$, yang sudah kita buat eksogen. Artinya, perubahan input demand dari sektor tersebut hanya bergantung pada $\Delta y$ dan tidak tergantung sama sekali dengan perubahan harga.

Consider optimisasi di CGE. tuh kita bikin production function pake model nesting. Misalnya _suppose_ Kita punya $x_i=$ output industri $i$ dengan fungsi produksi seperti ini:

$$
x_i=f(va_i,g_i)
$$

Di mana $va_i$ adalah production nest untuk value-added yang essentially datang dari faktor produksi (typically labor dan capital tapi bisa lebih, misalnya land dan natural resource deposit). Sementara itu, $g_i$ adalah komposit untuk input material. Nah, kedua produk komposit tersebut dapat diturunkan lagi di production nest lain:

$$
va_i=v(K,L)
$$

$$
g_i=g(q^j_i)
$$

Si $q^j_i$ adalah input material dari industri $j$ ke industri $i$. Nah, di CGE, kita bisa bikin fungsi produksi ini jadi non-linear, misalnya dengan Cobb-Douglas atau Leontief. Tapi di IO, kita menggunakan fungsi produksi Leontief, sehingga:

$$
g_i=\min \left( q^1_i,q^2_i,\ldots , q^j_i \right)
$$

Di mana $q^j_i$ adalah komposit material input dari industri $j$ ke industri $i$. Si fungsi komposit ini diterjemahkan sebagai sebuah matrix $A$ yang disebut input-output matrix. Di matrix IO, $q^j_i$ dianggap proporsional dengan $x_j$ (output industri $j$). Jadi kita bisa tulis:


$$
  \begin{align*}
  q^j_i=a^j_ix_j \newline
  0<a^j_i<1
  \end{align*}
$$


Tentu saja jika fungsi produksi komposit $f$ juga kita asumsikan sebagai leontief, maka semua nest produksi menjadi sangat simpel:


$$
  x_i=\min \left(a_{va}va_i,g_i \right) \newline
  \text{Leontief implies kita bisa buka gi in terms of its component} \newline
  x_i=\min \left(a_{va}va_i,a^1_ix_1,\dots,a^j_ix_i) \newline
  \text{optimization implies:} \newline
  x_i=a_{va}va_i=a^j_ix_j \forall j
$$


Dari _exercise_ di atas, kita bisa lihat bahwa supply dari industri $i$ harus sama dengan _composite product of value added_ yang didapat dari optimisasi faktor produksi dan _composite product of materials_ yang didapat dari matriks $Ax$ di atas. Karena itu, _composite demand of materials_ aja nggak bisa expand tinggi-tinggi jika tertahan oleh faktor produksi. Jika _composite demand material_ coba dipush dengan belanja pemerintah tapi produksinya ketahan dari sisi faktor produksi, maka hal tersebut hanya akan mengakibatkan inflasi, tanpa berhasil mendorong actual output.

Problem datang dari penggunaan tabel IO BPS 2020 yang notabene adalah matriks transaksi. Transaksi _implies current prices_, di mana ada kuantitas dan harga di situ. Nah, exercise IO sederhana biasanya menganggap matrix nilai tersebut sebagai kuantitas. Sehingga jika elemen dari matriks tersebut (yang sejatinya adalah nilai) bergerak, maka gerakannya akan dianggap sebagai gerakan kuantitas.

Problemnya adalah, dengan _constraint_, kita dapat menunjukkan bahwa _input demand_ biasanya akan tergantung dari harga! Typical Leontief production:

$$
\max min(a_1q_1,a_2q_2) \ \text{subject to} \ p_1 q_1+p_2 q_2 \leq I
$$

Optimisasi implies $a_1q_1=a_2q_2$, sehingga $q_1=\frac{a_2}{a_1}q_2$. Masukin ke constraint:

$$
p_1 \frac{a_2}{a_1}q_2+p_2 q_2 = I \\
q_2=\frac{I}{\frac{a_2}{a_2}p_2+\frac{a_2}{a_i}p_1}
$$

Jika kita ganti income $I$ sebagai harga dari output 1 dikali jumlah output 1 $p_1x_1$, maka demand output 2 jadi:

$$
q_2=\frac{p_1x_1}{a_1p_2+a_2p_1}
$$

dan bisa generalisasi persamaan di atas menjadi:

$$
q^j_i=\frac{p_ix_i}{\sum_{s=1}^S \frac{a^s_i}{a^j_i}p_s}
$$

di mana $q^j_i$ adalah input material dari industri $j$ ke industri $i$, $p_i$ adalah harga output industri $i$, $x_i$ adalah output industri $i$. $q^j_i$ adalah fungsi dari isocost industri $i$ (yang sama dengan total revenue) serta harga barang input untuk masing-masing industri $s$ termasuk $s=j$.

Poinnya adalah pergerakan harga akan sangat mempengaruhi input demand dari setiap industri. Karena itu, tanpa memperhitungkan harga (relatif), maka akan sangat sulit menganggap perubahan atas matrix Ax sebagai perubahan quantitas saja.

### Back to the IO table

Kita dapat menggunakan semua elemen di tabel IO sebagai kuantitas dikali dengan sebuah indeks harga $p=1$. Dengan menahan $p=1$ untuk semua elemen di dalam tabel IO, maka ya, semua perubahan dari _shock_ MBG hanya menggerakkan kuantitas.



## Problem pelaksanaan

Problem pelaksanaan menjadi masalah paling fundamental dalam mengatakan bahwa program ini pro-poor.

Saya sepakat bahwa jika SEMUA sekolah mendapatkan program ini, maka bisa jadi program ini progresif, dengan asumsi anggaran yang dikorbankan untuk MBG adalah pos yang biasanya dinikmati oleh [bagian masyarakat yang relatif lebih kaya](https://www.krisna.or.id/post/consumption/) (hence lower marginal propensity to consume[^2]). Tapi ada beberapa kemungkinan penerapan bahwa ini belum tentu terjadi di lapangan.

Pertama soal sebaran sekolah penerima. Sepemahaman saya, tidak semua sekolah menerima program ini secara serentak. Ada sekolah yang mendapat MBG (treatment) dan ada yang tidak (control). Problem muncul jika treatment tidak terjadi secara random/eksogen. Misalnya, jika secara umum sekolah yang menerima duluan adalah sekolah yang cenderung lebih siap secara infrastruktur. Sekolah seperti ini notabene terletak di daerah yang relatif lebih kaya. Jika ini yang terjadi, meski AAY memberikan beberapa anekdot kelompok masyarakat miskin sebagai penerima manfaat, bisa jadi banyak peserta sebenarnya berada di daerah yang sebenarnya cukup mampu.

Kedua adalah soal korupsi. Jika program ini dikorupsi, koruptornya most likely adalah orang yang tajir melintir dibandingkan dengan penerima manfaat. Artinya MBG akan berbahaya kalau menjadi sarana transfer income dari pihak yang kena potong anggaran ke pihak yang mengkorupsi MBG. 

[^1]: Sejujurnya saya juga nggak jago-jago banget sih CGE, so please take this post with a grain of salt.
[^2]: BTW MPC <1 inilah yang bikin bantuan secara in-kind kayak MBG bisa jadi lebih efektif naikin konsumsi daripada cash transfer. Worth discussion sendiri.
