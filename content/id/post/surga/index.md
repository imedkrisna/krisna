---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Model konsumsi intertemporal 3 periode: bekerja, pensiun, dan akhirat."
subtitle: ""
summary: ""
authors: [admin]
tags: [ekonomi, surga, iseng]
categories: [ekonomi, surga, iseng]
date: 2020-12-02T10:48:50+11:00
lastmod: 2020-12-02T10:48:50+11:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "https://unsplash.com/photos/V3DokM1NQcs"
  focal_point: "Smart"
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

Dulu jaman saya masih ngeblog di medium, saya pernah menulis tentang model intertemporal [3-periode](https://medium.com/@imedkrisna/extending-a-simple-2-period-consumption-problem-the-third-period-afterlife-9223cf5467d): bekerja, pensiun, meninggal. Kali ini saya mau coba menulis ulang tapi di blog yang baru di mana saya bisa pakai jupyter notebook jadinya bisa diitungin secara otomatis. gak harus pakek tulis tangan.

## Bekerja dan pensiun.

Model intertemporal ini biasa diajarkan di makroekonomi level S1 tahun akhir atau di level master. Intinya, model ini mau kasih liat rasionalitas _consumption smoothing_, yaitu fenomena di mana anda akan menjaga konsumsi agar tidak fluktuatif. Misalnya hari ini kejatuhan duren, daripada semua dikonsumsi, orang akan cenderung menabung supaya konsumsi esok gak terlalu jomplang. Pun sebaliknya, jika seseorang tau di masa depan akan dapat uang banyak, maka orang tersebut akan meminjam dan mengembalikan pinjamannya setelah uangnya datang. Inilah salah satu fungsi penting sektor perbankan, meminjamkan ke yang butuh duit, menyediakan tabungan buat yang belum butuh duit. Setidaknya begitu menurut teori.

Kalo di makro, salah satu model yang penting adalah soal pensiun. Yha penting karena banyak negara maju sudah mencapai _ageing population_ jadi kudu dipikir dari sekarang. Ini salah satu model _entry level_ yang cukup sederhana. Ketika seseorang mengambil keputusan untuk konsumsi atau menabung, ia dihadapkan ke dalam pilihan untuk menentukan 2 periode konsumsi. Periode 1 adalah ketika ia masih bekerja dan menerima gaji sebesar $Y$. Gaji tersebut dapat ia gunakan untuk konsumsi sebesar $C_1$, dan/atau menabung sebanyak $s$.

Di periode 2, ia akan pensiun dan kehilangan pemasukannya. Namun demikian, ia masih harus konsumsi. Duitnya dari mana? Ya dari tabungan dongs! Ia akan menghabiskan tabungannya dan konsumsi sebanyak $C_2=(1+r)s$ di mana $r$ adalah bunga yang ia dapat dari tabungannya. Problem yang ia hadapi adalah sebagai berikut:

$$
\begin{equation}
\max_{C_1,C_2} u(C_1)+\beta u(C_2) \\
\begin{split}
s.t.: \ & C_1 = Y - s \\
& C_2 = s(1+r)
\end{split}
\end{equation}
$$

Persamaan di atas dapat diselesaikan dengan menggunakan Lagrange dan euler equation. Seluruh tabungannya akan dihabiskan di  periode 2 karena setelah periode 2 ia akan mati dan tidak perlu lagi memikirkan optimisasi apapun.

Tapi apakah benar demikian? Tentu saja persamaan itu hanya (sebagian) benar jika dia adalah atheis!

## Bekerja, pensiun dan masuk surga.

Sebagai bagian dari masyarakat yang agamis, tentu saja saya agak tertarik memperhitungkan soal kehidupan setelah mati. Bagaimana saya bisa pergi ke surga jika semasa hidup hanya berfoya-foya memikirkan konsumsi? Tentu saja semasa hidup kita harus menyisihkan sebagian pemasukan kita untuk bersedekah menjalankan perintah agama. Model sederhana di atas saya tambah jadi 3 periode, di mana di periode ke-3 kita akan mengonsumsi amal perbuatan kita ketika di dunia. Seberapa banyak kita bisa konsumsi di surga? Tergantung seberapa banyak kita menyisihkan sebagian rejeki kita untuk amal.

Modelnya diekstensi jadi:

$$
\max_{C_1,C_2} u(C_1)+\beta u(C_2)+\delta u(C_3)
$$
$$s.t.: C_1 = Y -s -p$$
$$C_2 = s(1+r)$$
$$C_3 = p(1+x)$$
$$s \geq 0$$


Seperti dapat dilihat, kali ini kita punya 3 $C$, di mana $C_3$ adalah konsumsi di akherat. Ketika masih di periode satu, kita punya opsi tidak hanya menyisihkan pendapatan $Y$ untuk menabung sebanyak $s$, tapi juga beramal sebanyak $p$. Tidak seperti tabungan, amal tersebut tidak dapat kita gunakan untuk konsumsi di periode 2. Akan tetapi, kita akan menikmati hasil amal kita ketika sudah meninggal. Di akherat, kita akan konsumsi sebanyak $p(1+x)$ di mana $x$ adalah seberapa besar amalam kita berlipat ganda di surga nanti.

dengan substitusi, constraintnya bisa disederhanakan menjadi:

$$
C_1 + \frac{C_2}{(1+r)} + \frac{C_3}{1+x} = Y
$$

Optimisasinya tidak berbeda jauh dengan dua periode:

$$
\mathcal{L}(C_t)=u(C_1)+\beta u(C_2)+\delta u(C_3)+\lambda \left(Y-C_1-\frac{C_2}{(1+r)}-\frac{C_3}{1+x}\right)
$$
$$F.O.C.: \frac{d\mathcal{L}}{dC_1}=u'(C_1)-\lambda=0$$
$$\frac{d\mathcal{L}}{dC_2}=\beta u'(C_2)-\lambda \frac{1}{(1+r)}=0$$
$$\frac{d\mathcal{L}}{dC_3}=\delta u'(C_3)-\lambda \frac{1}{(1+x)}=0$$


Dari `F.O.C.` yang pertama didapat:

$$
u'(C_1) = \lambda
$$

Ganti semua $\lambda$:

$$u'(C_2)=\frac{u'(C_1)}{\beta (1+r)}$$
$$u'(C_3)=\frac{u'(C_1)}{\delta (1+x)}$$

Supaya bisa diitung dengan mudah, kita kasihkan standard CRRA [_utility function_ ](https://brilliant.org/wiki/utility-functions/#:~:text=A%20utility%20function%20is%20a,something%2C%20and%20it%20is%20relative.) $$u(C_t)=\frac{C_t^{1-\gamma}}{1-\gamma}$$. Dengan begini, problem 3 periode di atas dapat kita selesaikan. Kita bisa saja selesaikan dengan tidak terlalu sulit menggunakan pensil dan kertas, tapi kali ini mari kita manfaatkan Python untuk menghitung kelanjutan dari persamaan di atas. Pertama definisikan fungsi utilitas dan turunannya:


```python
# kodenya boleh ngopas dari quantecon
def u(c, γ):
    '''utility function'''
    if γ ==1:
        return np.log(c)
    else:
        return c**(1-γ)/(1-γ)

def u_prime(c, γ):
    '''Derivative of utility'''
    if γ == 1:
        return 1 / c
    else:
        return c**(-γ)
```

Kemudian kita dapat manfaatkan `SciPy` untuk menghitung persamaan konsumsi 3 periode di atas. Ada beberapa parameter yang digunakan di problem ini, berikut artinya:

$\gamma$ = kadar takut risiko kita
$\delta$ = faktor diskon surga. semakin besar, semakin agamis
$\beta$ = faktor diskon periode dua. Semakin besar, semakin penyabar. Kalo kecil berarti tipe YOLO.
$Y$ = _Income_ / penghasilan semasa muda.
$r$ = tingkat suku bunga
$z$ = seberapa besar amalan kita dilipat-gandakan oleh Yang Maha Kuasa.

Saya pake parameter-parameter di bawah ini karena iseng aja. Tentu saja anda bisa install python, kopas kodenya dan utik-utik sendiri parameternya sesuai karakteristik anda.


```python
from scipy.optimize import fsolve
γ=2.00001
δ=0.95
β=0.9
Y=150
r=0.1
z=0.1

def func(c):
    return[u_prime(c[1],γ)-u_prime(c[0],γ)/β/(1+r),
          u_prime(c[2],γ)-u_prime(c[0],γ)/δ/(1+z),
          c[0]+c[1]/(1+r)+c[2]/(1+z)-Y]
```


```python
root=fsolve(func,[1,1,1])
data = [root, u(root,γ),(root/sum(root))]
tabel=pd.DataFrame(data, columns=["Masa muda", "Pensiun","Surga"])
tabel['Variabel']=['C','U','Share']
tabel = tabel[['Variabel', "Masa muda", "Pensiun","Surga"]]
tabel
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Variabel</th>
      <th>Masa muda</th>
      <th>Pensiun</th>
      <th>Surga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C</td>
      <td>52.931443</td>
      <td>52.666122</td>
      <td>54.109290</td>
    </tr>
    <tr>
      <th>1</th>
      <td>U</td>
      <td>-0.018891</td>
      <td>-0.018987</td>
      <td>-0.018480</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Share</td>
      <td>0.331429</td>
      <td>0.329767</td>
      <td>0.338804</td>
    </tr>
  </tbody>
</table>
</div>



Dengan parameter di atas, dapat dilihat bahwa model ini mengarah ke orang yang sangat-sangat menjunjung tinggi _comsumption smoothing_. Penghasilan yang ia dapatkan $(Y)$ dibagi rata untuk konsumsi, menabung dan juga beramal. Kombinasi ini memiliki total utility yang so pasti maksimal. Ingat, yang dimaksimalkan bukanlah $u$ untuk masing-masing periode tetapi $u(C_1)+\beta u(C_2)+ \delta u(C_3)$.

Angka ini bisa berubah tidak hanya berdasarkan karakteristik si individu (alias parameter $\beta$ dan $\delta$) tetapi juga tergantung dengan kondisi di luar seperti besarnya tingkat suku bunga $r$. seandainya saya naikin suku bunga, _ceteris paribus_, kira-kira apa yang akan terjadi?


```python
r=0.4
root=fsolve(func,[1,1,1])
data = [root, u(root,γ),(root/sum(root))]
tabel=pd.DataFrame(data, columns=["Masa muda", "Pensiun","Surga"])
tabel['Variabel']=['C','u','Share']
tabel = tabel[['Variabel', "Masa muda", "Pensiun","Surga"]]
tabel
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Variabel</th>
      <th>Masa muda</th>
      <th>Pensiun</th>
      <th>Surga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C</td>
      <td>54.922854</td>
      <td>61.650715</td>
      <td>56.145014</td>
    </tr>
    <tr>
      <th>1</th>
      <td>u</td>
      <td>-0.018206</td>
      <td>-0.016220</td>
      <td>-0.017810</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Share</td>
      <td>0.317990</td>
      <td>0.356943</td>
      <td>0.325066</td>
    </tr>
  </tbody>
</table>
</div>



Secara umum semua naik karena kali ini tabungannya menghasilkan lebih banyak uang untuk konsumsi. Namun dapat dilihat bahwa share-nya jadi banyakan tabungan dibandingkan konsumsi ("Masa muda") ataupun beramal ("Surga"). Hasilnya akan lebih kelihatan jika misalnya kita naikkan suku bunga tapi menurunkan $Y$. Ia akan punya total _lifetime income_ yang sepadan, tapi akan lebih banyak mengalokasikan ke menabung karena dengan suku bunga yang tinggi, _opportunity cost_ dari konsumsi jadi tinggi.

Nah sekarang bagaimana jika ada argumen bahwa amal kita akan dibayarkan dengan berkali lipat bahkan sampai tidak terhingga?  Artinya, parameter yang harus kita utik-utik adalah $z$. Yuk dicoba.


```python
z=99
root=fsolve(func,[1,1,1])
data = [root, u(root,γ),(root/sum(root))]
tabel=pd.DataFrame(data, columns=["Masa muda", "Pensiun","Surga"])
tabel['Variabel']=['C','u','Share']
tabel = tabel[['Variabel', "Masa muda", "Pensiun","Surga"]]
tabel
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Variabel</th>
      <th>Masa muda</th>
      <th>Pensiun</th>
      <th>Surga</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C</td>
      <td>78.978540</td>
      <td>88.653140</td>
      <td>769.778825</td>
    </tr>
    <tr>
      <th>1</th>
      <td>u</td>
      <td>-0.012661</td>
      <td>-0.011279</td>
      <td>-0.001299</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Share</td>
      <td>0.084252</td>
      <td>0.094572</td>
      <td>0.821176</td>
    </tr>
  </tbody>
</table>
</div>



Menurut model ini, maka yang terjadi adalah kita akan menghabiskan tabungan kita untuk amal. Seperti anda lihat di tabel di atas, _share_ amal tiba-tiba naik jadi 83% dari total pendapatan. Yang lucu adalah total income yang dihabiskan di dunia jadi ikut naik. Tentu saja ini mustahil ha ha ha. Tapi jelas naiknya gara-gara "bunga" yang didapatkan dari amal. Bukannya mustahil sih. Bisa saja kan amalan kita di dunia dinikmati sebagian ketika kita masih hidup? Makanya guys jangan lupa berbuat baik.

## Tentu saja model ini ngaco

Jangan lupa bahwa ini model yang sangat sederhana sekali dan banyak _caveat_-nya. Saya sudah tuliskan beberapa di blog medium di atas. Bagaimanapun juga, banyak juga peluang untuk memperlebarnya. Misalnya, dibikin $p$ boleh negatif dengan konsekuensi $Y$ naik, yang bisa kita terjemahkan sebagai perilaku korupsi: Berdosa demi meningkatkan pendapatan dan akan dibayar di neraka nanti. Ini cuma satu contoh. Ada banyak aplikasi lain dengan model yang lebih ribet yang bisa kita buat. hahha.

Yaudah segini dulu. semoga tulisan ini menghibur dan menginspirasi anda untuk beramal dan berbuat kebajikan bagi masyarakat!
