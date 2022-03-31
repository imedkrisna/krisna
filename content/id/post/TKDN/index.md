---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Memodelkan TKDN secara sederhana"
subtitle: ""
summary: ""
authors: [admin]
tags: [TKDN, perdagangan, industri, python]
categories: [TKDN, perdagangan, industri, python]
date: 2022-03-29T14:09:58+07:00
lastmod: 2022-03-29T14:09:58+07:00
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

Perbincangan tentang peningkatan penggunaan produk dalam negeri dan anti impor sudah sering bergaung di kalangan pejabat publik. Bahkan, belakangan ini rasanya perbincangan ini terdengar semakin sering. Tentu saja menggunakan barang-barang produksi dalam negeri adalah sesuatu yang tidak jelek. Yang jadi masalah adalah kalau dipaksa. Cinta produk dalam negeri, seperti halnya cinta pada yang lain, sangat ga asik jika dipaksa. Nah, salah satu instrumen yang sedang marak digunakan oleh Indonesia adalah TKDN.

# Apa itu TKDN?
[TKDN](http://tkdn.kemenperin.go.id/), atau Tingkat Kandungan Dalam Negeri, mulai marak digunakan oleh Indonesia[^1]. TKDN, jika diwajibkan untuk suatu industri, mengamanatkan batas minimal dari suatu produk akhir memiliki kandungan dalam negeri. Kandungan ini bisa berupa tenaga kerja, permesinan, sampai ke penggunaan bahan baku. Contohnya, [perangkat 5G](https://inet.detik.com/consumer/d-5782359/kata-samsung-tentang-ketentuan-tkdn-4g-dan-5g-jadi-35), pada April 2022, diwajibkan memenuhi TKDN 35%, yang artinya semua perangkat 5G yang beredar harus memiliki kandungan lokal minimal 35% (atau maksimal komponen impor maksimal 65%).

TKDN mengakibatkan perusahaan tidak boleh lagi menjual barang impor. Barang tersebut harus diproduksi di dalam negeri. Komponennya boleh impor tapi tidak boleh banyak-banyak. Dengan TKDN, maka produsen diharapkan mendatangkan pabriknya ke Indonesia. Saya pernah menulis sedikit tentang efek ini di postingan saya [yang lain]({{< relref "/post/hitektrade" >}}). Dengan adanya investasi, maka lapangan kerja akan bertambah. Di negara yang informalitasnya tinggi seperti di Indonesia, lapangan pekerjaan formal dapat menjadi pilihan yang baik untuk meningkatkan kesejahteraan masyarakat[^2]. TKDN juga diharapkan dapat meningkatkan kapasitas produksi dan teknologi perusahaan domestik yang menjadi _supplier_ industri barang jadi.

Beberapa alasan kenapa TKDN cukup populer terutama bagi pemerintahan adalah karena dia gratis (gak kaya subsidi yang memerlukan APBN). Selain itu, kebijakan anti impor biasanya sangat disukai oleh masyarakat, dan berpotensi meningkatkan popularitas politisi.

Secara sepintas, memang sepertinya meningkatkan TKDN itu baik ya. Jika investasi datang ke Indonesia, maka akan ada value tambahan. Namun perlu dipahami bahwa konsep value itu tidaklah statik dan tidak _eksogen_. Value sebuah barang bisa naik dan bisa turun tergantung dari inputnya juga. Apakah, misalnya, perangkat 5G yang punya kandungan domestik tinggi ini sama bagusnya dengan jika perangkat tersebut diimpor? Apakah perangkat dengan TKDN tinggi bisa bersaing di pasar global? Apakah ada smelter berarti kita dapat value yang lebih tinggi [dari ekspor nikel saja](https://theconversation.com/klaim-sukses-hilirisasi-nikel-berbasis-larangan-ekspor-masih-memiliki-segudang-masalah-177735)?

Jawabannya belum tentu. Beberapa artikel teoritis membedah konsep perubahan value dan produktivitas dari perusahaan intermediate input dan perusahaan final good[^3] [^4] [^5]. Memang ada tarik menarik antara keduanya, dan TKDN tidak otomatis menghasilkan keluaran yang seoptimal kelihatannya, apalagi jika TKDN tidak berhasil meningkatkan produktivitas sektor yang ia coba proteksi.

Di postingan kali ini, saya mencoba ngasih gambaran dengan model yang sangat simpel tentang tarik-menarik value ini.

# Model
Anggaplah ada sebuah perusahaan produsen produk akhir yang seringkali membutuhkan barang impor. Barang impor ini sebenarnya bisa disubstitusi di dalam negeri, akan tetapi bagi si perusahaan, barang impor lebih murah dan memberikan nilai tambah yang lebih tinggi. Contoh dunia nyatanya mungkin seperti [kedelai](https://ekonomi.bisnis.com/read/20180829/99/832660/ini-alasan-kedelai-impor-lebih-digemari-produsen-tempe) atau [garam](https://bisnis.tempo.co/read/1071682/kenapa-kualitas-garam-lokal-untuk-industri-kalah-dibanding-impor).

Jika kita cuma lihat keputusan produk input saja, maka si perusahaan punya fungsi produksi:

$$F(M,N) = \alpha M + N$$

di mana $M$ adalah jumlah input yang diimpor dan $N$ adalah jumlah input yang dibeli di pasar domestik. Sementara itu, $\alpha$ adalah kualitas bahan baku impor relatif terhadap bahan baku domestik. Jika $\alpha > 1$ berarti barang impor punya kualitas lebih bagus. Kita juga akan mengasumsikan bahwa harga barang impor lebih murah daripada domestik ($P_M<P_N$). 

Si perusahaan ini diwajibkan untuk membeli barang mentah dari dalam negeri sebesar $k$:

$$
P_NN \geq kP(\alpha M + N)
$$
$$
\text{di mana } k \in (0,1)
$$

Si perusahaan bermaksud memenuhi permintaan sebesar $F(M,N)=Q$ dengan biaya serendah mungkin. Artinya, si perusahaan memiliki problem:

$$
\min P_MM+P_NN
$$
$$
s.t. \ \alpha M+ N \geq Q
$$
$$
P_NN \geq kP(\alpha M + N)
$$
$$
k \in (0,1)
$$

Berhubung masalahnya linear, kita bisa pake `linprog`. Saya akan menggunakan parameter sebagai berikut:

$$
P_M=1
$$
$$
P_N=3
$$
$$
α=1.5
$$
$$
k=0
$$
$$
P=9
$$
$$
Q=30
$$

Kita buat dulu fungsinya:

```python
from scipy.optimize import linprog
def TKDN(Pm=1,Pn=3,α=1.5,δ=1,k=0,P=9,Q=30):
    c_ex1 = np.array([Pm, Pn])
    A_ex1 = np.array([[-α,-1],[k*P*α, k*P-Pn]])
    b_ex1 = np.array([-δ*Q,0])
    res_ex1 = linprog(c_ex1, A_ub=A_ex1, b_ub=b_ex1, method='revised simplex')
    names=[f'impor bahan baku = {res_ex1["x"][0]}',
    f'bahan baku domestik = {res_ex1["x"][1]}',
    f'biaya produksi = {Pm*res_ex1["x"][0]+Pn*res_ex1["x"][1]}',
    f'profit perusahaan = {Q*P-Pm*res_ex1["x"][0]-Pn*res_ex1["x"][1]}']
    for i in names:
        print(i)
    
    
```

Angka default di atas tidak perlu diartikan secara harfiah bahwa harga impor adalah 1. Si $P_M=1$ disebut juga _numeraire_, atau harga dasar. Karena problemnya linear yang berarti bebas _affine transformation_. Harga domestik $P_N=3$ bisa kita artikan bahwa harga bahan baku domestik lebih mahal tiga kali lipat daripada harga bahan baku impor.

# Siapa yang untung siapa yang buntung
Sekarang mari kita gunakan fungsi yang barusan kita bikin. Jangan lupa ada dependency `linprog` dari `scipy`. Untuk kasus tanpa TKDN, berarti kita set $k=0$:

```python
TKDN()
```

    impor bahan baku = 20.0
    bahan baku domestik = 0.0
    biaya produksi = 20.0
    profit perusahaan = 250.0
    

Bagaimana dengan TKDN di mana konten domestik harus ada di angka 20% dari total nilai produk jadi?

```python
TKDN(k=0.2)
```

    impor bahan baku = 8.0
    bahan baku domestik = 18.0
    biaya produksi = 62.0
    profit perusahaan = 208.0
    

Seperti dapat kita lihat di atas, TKDN mengakibatkan perusahaan produk jadi mengalami penurunan profit dan kenaikan total cost. Namun demikian, penjual bahan baku domestik mendapatkan tambahan pemasukan sebanyak $18 \times P_N$. Artinya, TKDN berpotensi menyenangkan penjual bahan baku domestik, akan tetapi merugikan penjual barang jadi.

Ketika TKDN diset jadi 40%, modelnya crash alias si produk jadi mendingan ga produksi sama sekali wkwkw.

Jika kita tabelkan, maka TKDN mulai dari 0 sampai 30% (untuk setiap tambahan 10% TKDN) dapat dilihat di tabel di bawah

| k | M | N | C | $\pi$ |
| --- | --- | --- | --- | --- |
| 0 | 20 | 0 | 20 | 250 |
| 10% | 14 | 9 | 41 | 229 |
| 20% | 8 | 18 | 62 | 208 |
| 30% | 2 | 27 | 83 | 187 |

Bagaimana dengan nilai tambah dalam negeri secara total? Walaupun TKDN berhasil menaikkan nilai tambah dari produsen bahan baku, namun nilai tambah dari produsen barang jadi berkurang. Dalam kasus TKDN=0, maka nilai tambah produsen bahan baku adalah 0, sementara profit produsen barang jadi adalah 250. Untuk TKDN 10%, bahan baku dapat nilai tambah 9 tetapi barang jadi kehilangan $250-229=21$. jadi secara total terjadi kekurangan nilai tambah.

Bagaimana dengan pemerintah? Seandainya impor bebas bea, maka pemasukan pemerintah akan datang dari PPh badan atau *Corporate Income Tax*. Tentunya dengan TKDN=0 maka produsen bahan baku ga bayar pajak. Sementara itu, produsen barang jadi akan membayar PPh badan sebesar $t \pi$ di mana $t$ adalah *tax rate*. Kalau kita asumsikan bahwa _cost_ produsen bahan baku domestik adalah 0, maka produsen bahan baku punya income sebesar $P_N \times N$. Artinya, Total government revenue menjadi:

$$GR=t(P_N-c)N+t \pi$$

di mana c adalah marginal cost yang linear terhadap produksi. Saya menggunakan c=2 sehingga perusahaan lokal harus ngecharge harga $P_N=3$ supaya punya revenue 1, sama dengan importir. Jika cost domestik rendah, tentunya mereka bisa menjual dengan harga lebih murah supaya dibeli oleh perusahaan produsen barang jadi.

Coba kita hitung jika tax rate adalah 20%, maka total penghasilan pemerintah adalah:

```python
t=0.2 # corporate income tax
Pn=3 # harga barang domestik
c=2 # sehingga firms ga bisa jual dgn lebih murah daripada 3
brp=('0%','10%','20%','30%')
taxs=((Pn-c)*0*t+250*t,
(Pn-c)*9*t+229*t,
(Pn-c)*18*t+208*t,
(Pn-c)*27*t+187*t)
for x,y in zip(brp,taxs):
    print(f'Ketika TKDN={x}, total GR = {y}')
```

    Ketika TKDN=0%, total GR = 50.0
    Ketika TKDN=10%, total GR = 47.6
    Ketika TKDN=20%, total GR = 45.2
    Ketika TKDN=30%, total GR = 42.8
    

Semakin tinggi TKDN, semakin rendah total _income tax_ dari 2 perusahaan tersebut. Meskipun pajak dari perusahaan domestik naik, akan tetapi pajak yang dibayar oleh perusahaan barang jadi berkurang karena profit yang berkurang. Karena itu, meskipun sekilas TKDN tidak memerlukan persiapan fiskal seperti subsidi, tetapi potensi inefisiensi yang dihasilkan memiliki 'ongkos' terhadap APBN juga.

Hal ini tentunya di luar APBN yang digunakan untuk menegakkan aturan TKDN. Misalnya, untuk memastikan sebuah perusahaan mengikuti aturan TKDN, perusahaan tersebut harus disurvey dulu untuk dapat sertifikat lolos TKDN. Sertifikat 2 barang pertama dibayarin oleh Pemerintah, yang tentunya pakai APBN. Ini belum termasuk pembangunan sistem dan sumberdaya yang harus dialokasikan untuk penegakan TKDN oleh pemerintah. Di samping itu, untuk barang ke-3 yang perlu TKDN, maka perusahaan harus menanggung biaya sertifikat, yang akan mengurangi lebih jauh profit mereka, dan otomatis pajak penghasilan yang dibayarkan.

# Jadi TKDN baik atau buruk?

Beberapa hal di atas merupakan kemungkinan problem yang ditimbulkan oleh TKDN. Model linear ini, meskipun agak _arbitrary_, cukup mampu menjelaskan dampak jangka pendek TKDN. Model yang lebih representatif (tapi lebih ribet) bisa dicek di footnote.

Satu hal penting dari model di atas adalah tidak bisa mentah-mentah terima bahwa $Q$ dan $P,P_M,P_N$ sama sekali tidak bergerak ketika ada TKDN. Bisa saja alih-alih semangat menjadi efisien, produsen bahan baku dalam negeri malah keenakan diproteksi dan ga ada _improvement_ sama sekali. Bukannya improve, mereka malah naikin harga karena produsen barang jadi ga punya opsi lain selama TKDN _binds_.

Disamping itu, TKDN membuat produsen barang jadi di dalam negeri jadi sulit berkompetisi dengan produsen barang jadi di negara lain. Kenapa? Karena produsen luar negeri bisa akses bahan baku murah dan bagus tanpa kena TKDN. Akibatnya, produsen barang jadi dalam negeri tidak bisa bersaing di pasar global dan terpaksa memanfaatkan pasar domestik. Produsen barang jadi di dalam negeri jadi tidak bisa bersaing dengan impor barang jadi, sehingga akan minta proteksi juga.

Inilah kenapa ada blokir IMEI. Produsen ponsel dalam negeri ga mau saingan dengan ponsel impor karena ponsel impor ga harus mengikuti TKDN. Apakah publik pernah dikasih tau berapa APBN yang dikeluarkan untuk implementasi blokir IMEI?

Terakhir, TKDN itu sekalinya digunakan, maka akan sulit untuk dibatalkan. Perusahaan yang sudah terlanjur investasi besar demi memenuhi TKDN akan rugi besar kalau tiba-tiba TKDN dicabut dan perusahaan yang tidak investasi bisa masuk ke pasar yang tadinya diproteksi dengan TKDN. Karena itu, perusahaan yang sudah keburu invest demi memenuhi TKDN akan punya insentif untuk terus meminta pemerintah menjalankan TKDN dan menerapkan aturan-aturan yang diperlukan untuk menegakkan TKDN.

TKDN bisa dianggap berhasil kalau ternyata terdapat pembelajaran bagi produsen bahan baku dalam negeri. Misalnya, karena sekarang ada klien, industri mereka tumbuh dan makin efisien sehingga menekan cost sehingga bisa semurah produk impor (alias $P_N \leq P_M$), atau meningkatkan kualitas sehingga bisa lebih baik dari produk impor (alias $\alpha \in (0,1)$). Jika ini yang terjadi, maka $k$ tidak lagi binding dan TKDN bisa dikatakan berhasil, tergantung seberapa besar dan seberapa cepat _improvement_ industri dalam negeri terjadi.

Karena itu, pembuat kebijakan yang sudah terlanjur menggunakan TKDN seyogyanya terus memantau si $\alpha$ dan si $P_N$ ini (atau tepatnya $\frac{P_N}{P_M}). Jika tidak ada kemajuan, maka sulit mengharapkan industri nasional untuk bisa efisien dan kompetitif, dan akhirnya keunggulan-keunggulan yang diinginkan malah tidak tercapai. Pemaksaan saja akan sulit diharapkan untuk berhasil. Ada kemungkinan pemerintah mesti mengkomplemen aturan ini dengan aturan lain. Jadi makin banyak ya aturannya wkwk.

# Alternatif TKDN

Ada beberapa alternatif dari TKDN[^6] :
1. **Perbaiki iklim bisnis**. Ini kayaknya obvious banget ya : lol : . Tapi memang jurus ini ga ada yang ngalahin kebijakan lain. Susah industri mau maju kalau hulu-nya diproteksi, mau beli barang impor maupun ekspor _administrative cost_-nya tinggi. Aparatnya masih suka [korupsi](https://regional.kompas.com/read/2022/03/25/171720578/berkas-perkara-korupsi-dilimpahkan-ke-pengadilan-2-eks-pejabat-bea-cukai).
1. **Manfaatkan CSR**. Tanyain apakah pengusaha multi nasional bisa mencoba membantu perusahaan lokal sebagai suppliernya.
1. Lakuukan **pelatihan** bagi pegawai maupun perusahaan pemasok komponen. Training merupakan hal yang penting untuk meningkatkan kualitas pengusaha dan karyawan lokal. Pemerintah yang paham industri tentunya akan bisa mengidentifikasi pelatihan apa yang diperlukan, dan menyelenggarakannya. Ini juga makan APBN, tapi jauh lebih baik daripada dipake buat menegakkan TKDN.
1. Perbaiki **proses dan infrastruktur fisik logistik**. Ini juga rasanya cukup jelas :lol: .
1. Jika semua masih gagal juga, menggunakan **tarif dan subsidi**, meski tidak ideal, masih lebih baik daripada TKDN. Tapi balik lagi ya, problem utama dari tariff tentunya adalah perjanjian dagang dan retaliasi. Tariff lebih mudah dihitung daripada TKDN, sehingga lebih munggkin kena masalah di WTO. Sementara itu, subsidi membebani APBN secara langsung, ga seperti TKDN yang membebani APBN dan ekonomi secara tidak langsung. Yah beginilah kalau punya policy makers & politisi yang ga ngerti cara ngitung _hidden cost_.

Nanti saya bahas lagi kapan-kapan wkwk. Mention saya di [twitter](https://www.twitter.com/imedkrisna) jika ada komen, kritik, atau saran. Thanks.

[^1]: Fernando, O., & Ing, L. Y. (2022). Indonesia's Local Content Requirements: An Assessment on Consistency with Free Trade Agreement Commitments. *ERIA Discussion Paper Series*, 420. https://www.eria.org/publications/indonesias-local-content-requirements-an-assessment-on-consistency-with-free-trade-agreement-commitments/ 
[^2]: Gupta, K., & Mardjono, E. (2021). Indonesia Emas Berkelanjutan 2045: Kumpulan Pemikiran Pelajar Indonesia Sedunia Seri 01 Ekonomi. LIPI Press. https://doi.org/10.14203/press.357 
[^3]: Grossman, G. M. (1981). The Theory of Domestic Content Protection and Content Preference. *The Quarterly Journal of Economics*, 96(4), 583-603. https://doi.org/10.2307/1880742 
[^4]: Veloso, F. M. (2006). Understanding Local Content Decisions: Economic Analysis and an Application to the Automotive Industry. *Journal of Regional Science*, 46(4), 747-772. https://doi.org/https://doi.org/10.1111/j.1467-9787.2006.00476.x 
[^5]: Lin, S.-H., & Weng, Y. (2020). Can strengthening the local content requirements meet a government’s need to raise industrial productivity and production? *Journal of Applied Economics*, 23(1), 316-328. https://doi.org/10.1080/15140326.2020.1753468
[^6]: Hufbauer, G., Schott, J. J., Wada, E., Cimino, C., & Vieiroand, M. (2013). Local Content Requirements : A Global Problem. Peterson Institute for International Economics. http://ebookcentral.proquest.com/lib/anu/detail.action?docID=3385696 

