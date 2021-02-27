---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Ekspor sebagai strategi economic recovery pasca COVID-19"
event: "IDM Co-op FGD: Badai Pandemi, Vaksinasi dan Harapan Pemulihan Ekonomi"
event_url:
location:
address:
  street:
  city:
  region:
  postcode:
  country:
summary: I share a possible recovery through export. There seem to be a trade-off between going ahead with commodity export with an import substitution policy.
abstract: I share a possible recovery through export. There seem to be a trade-off between going ahead with commodity export with an import substitution policy.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2021-02-27T14:00:00+11:00
date_end: 2021-02-27T15:30:00+11:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2021-02-26T20:41:11+11:00

authors: [admin]
tags: [economics, trade, coronavirus COVID-19]

# Is this a featured event? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
links:
 - name: IDM
   url: https://www.facebook.com/idmcooperatives/photos/?ref=page_internal
   icon_pack: fab
   icon: facebook
 - name: IDM
   url: https://twitter.com/idmcoop/status/1365231406180233218?s=20
   icon_pack: fab
   icon: facebook
 - name: IDM
   url: https://www.instagram.com/p/CLwS7SuA2Mt/?utm_source=ig_web_copy_link
   icon_pack: fab
   icon: instagram

# Optional filename of your slides within your event's folder or a URL.
url_slides: 

url_code:
url_pdf:
url_video:

# Markdown Slides (optional).
#   Associate this event with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: "idm"

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

## Pendahuluan

Di saat pandemi, kebijakan ekonomi yang terbaik adalah kebijakan kesehatan. Vaksin seringkali dikatakan akan menjadi penyelamat ekonomi Indonesia. Seandainya hal itu benar pun, kecepatan vaksinasi akan menentukan seberapa cepat ekonomi bisa pulih. Data dari [our world in data](https://ourworldindata.org/coronavirus-data-explorer?zoomToSelection=true&time=2020-03-01..latest&country=IDN~BRA~TUR~IND&region=World&vaccinationsMetric=true&interval=total&perCapita=true&smoothing=0&pickerMetric=total_vaccinations_per_hundred&pickerSort=desc) menunjukkan bahwa kecepatan vaksinasi Indonesia masih perlu ditingkatkan, setidaknya jika dibandingkan dengan Brazil dan Turki.

{{< figure library="true" src="/idm/gambar1.svg" title="" numbered="" width=630 >}}

Namun, sepertinya vaksinasi tidak memiliki korelasi dengan pertumbuhan ekonomi. Meskipun Indonesia tertinggal jauh daripada Turki dalam hal vaksinasi, pertumbuhan PDB cukup seimbang. Menurut data weekly tracker dari OECD, pertumbuhan ekonomi Indonesia, Turki, Brazil dan India cukup seimbang. Bahkan ketika awal terjadinya pandemi, Indonesia termasuk negara yang jatuhnya paling kecil.

Sedikit catatan mengenai weekly tracker dari OECD, data ini adalah sebuah estimasi berdasarkan algoritma _machine learning_ dan data dari Google Trends. OECD menggunakan beberapa term pencarian yang berkorelasi dengan aktivitas ekonomi seperti mencari harga rumah dan mobil. Keunggulannya adalah Google Trends dapat dikumpulkan secara real time sehingga weekly tracker ini sifatnya lebih ke _nowcasting_ daripada _forecasting_. Saya rasa narasumber lain sudah cukup memaparkan data yang lebih valid daripada weekly tracker.

## Recovery dari Ekspor

Ekspor juga merupakan salah satu aktivitas ekonomi yang sepertinya tidak terlalu terdampak dengan pandemi. Bahkan, nilai ekspor Indonesia pada bulan November dan Desember 2020 lebih tinggi daripada ekspor Indonesia di [bulan yang sama tahun lalu](https://www.bps.go.id/website/materi_ind/materiBrsInd-20210115093516.pdf). Selain itu, ekspor adalah strategi beberapa negara ASEAN untuk _recover_ dari krisis ekonomi 1998.

Memang ada beberapa perbedaan antara resesi kali ini dengan krisis 1998. Ketika itu, krisis hanya terjadi di wilayah Asia Timur dan ASEAN. Ditambah dengan depresiasi mata uang negara-negara ASEAN yang dalam, tiba-tiba produk negara-negara ini menjadi lebih kompetitif dibandingkan dengan negara berpendapatan tinggi. Saat ini, depresiasi mata uang belum terjadi. Di samping itu, krisis COVID-19 kali ini merata di seluruh dunia, bahkan ekonomi di negara berpendapatan tinggi yang ekonominya bergantung pada sektor jasa mengalami pengecilan yang lebih dalam dibandingkan Indonesia. Namun demikian, stimulus yang ada di negara tersebut dapat menjadi peluang untuk meningkatkan permintaan internasional.

Ada dua hal yang saya angkat. Saya seringkali mendapatkan pertanyaan dari beberapa pihak, "produk apa yang harus kita dorong untuk _export recovery_". Pertanyaannya mudah, tapi menjawabnya cukup sulit. Saya akan coba _approach_ standar yaitu menggunakan _Revealed Comparative Advantage_ (RCA).

## RCA

RCA adalah salah satu metrik untuk melihat produk ekspor andalan suatu negara. RCA dihitung dari seberapa penting suatu produk di pasar global, dan seberapa penting suatu negara dalam produksi produk tersebut. Semakin sulit suatu produk diproduksi di negara lain, semakin kompetitif negara tersebut dalam menghasilkan produk tersebut. Dalam term RCA, semakin besar RCA suatu negara di satu produk, semakin penting ia. 

Definisi formal RCA oleh UNCTAD dapat dibaca di [sini](https://unctadstat.unctad.org/en/RcaRadar.html). Buat yang suka rumus, silakan lihat di [akhir post ini](#rumus).

Agregasi yang saya gunakan di paparan kali ini dapat dilihat di [akhir post ini](#agregasi).

Gambar 4 (lihat slides) menunjukkan dinamika RCA Indonesia untuk beberapa produk dari tahun 2000 sampai tahun 2018. Data bersumber dari UNCTAD yang saya tarik dari WITS. Berdasarkan gambar 4, kita dapat lihat bahwa Indonesia memiliki RCA yang tinggi di produk-produk pertambangan dan perkebunan. pertumbuhan yang tinggi di `vegetable` didorong oleh kelapa sawit. Di dalam `fuels` terdapat minyak bumi, gas alam dan batubara. Kita juga cukup kompetitif di produk karet. RCA di `minerals` mengalami penurunan yang cukup signifikan terutama sejak 2009. Spekulasi saya ini akibat simpang siur soal larangan ekspor mineral yang dimulai di sekitar tahun tersebut.

{{< figure library="true" src="/idm/gambar4.png" title="" numbered="" width=630 >}}

Gambar 5 (lihat slides) menunjukkan hal yang sama untuk beberapa produk lain. Indonesia punya RCA yang tinggi di persepatuan, TPT, dan KPK. Seperti diduga, Indonesia kurang kompetitif dalam produksi barang modal. Kendaraan pun sepertinya hanya besar di dalam negeri saja untuk saat ini.

{{< figure library="true" src="/idm/gambar5.png" title="" numbered="" width=630 >}}

## Harga-harga komoditas

Secara natural, negara tropis umumnya memiliki RCA yang tinggi di komoditas perkebunan dan pertambangan. Di samping itu, Indonesia juga cukup unggul di industri padat karya. Saat ini, peluang _recovery_ dari komoditas cukup baik karena harga-harga internasional sedang terkerek naik akibat permintaan yang cukup tinggi dari pasar global.

{{< figure library="true" src="/idm/gambar6.png" title="" numbered="" width=630 >}}

Hal ini menambahkan keunggulan ekstra dari _recovery_ dari ekspor, yaitu dapat dilakukan dengan cepat karena komoditas di atas adalah ekspor yang sudah dilakukan Indonesia selama ini dan memang merupakan unggulan.

## Kinerja ekspor

Data menunjukkan bahwa kinerja ekspor tidak terlalu terpengaruh secara signifikan akibat COVID-19.

Dominasi CPO, migas dan batubara sangat terlihat. CPO bahkan tumbuh di 2020 dibandingkan dengan 2019 meskipun produk lain menurun. Tahun-tahun ini juga saat dimulainya larangan ekspor mineral. Sementara energi jelas terpukul oleh jatuhnya harga energi dengan dipimpin oleh harga minyak. COVID-19 mengurangi permintaan energi secara signifikan seiring dengan pembatasan mobilisasi di mana-mana.

{{< figure library="true" src="/idm/gambar7.png" title="" numbered="" width=630 >}}

Sebagian besar komoditas melemah di 2020. Ekspor mobil sangat terdampak, karena itu pemerintah mencoba memanfaatkan pasar domestik melalui pembebasan pajak. Sementara ekspor metal meningkat seiring peningkatan kapasitas smelter. Tekstil dan produk tekstil sepertinya juga mengalami pukulan yang cukup tinggi, diduga karena GVC yang terhambat oleh COVID-19. Banyak produk TPT yang bahan bakunya diimpor dari negara lain, dan APD dan masker adalah salah satunya.

{{< figure library="true" src="/idm/gambar8.png" title="" numbered="" width=630 >}}


## RCA bukan segalanya

RCA adalah sesuatu yang dinamis. Seperti kita lihat bahwa RCA Indonesia berubah-ubah di beberapa sektor. Tambah lagi, Indonesia saat ini tengah berupaya meningkatkan nilai tambah dalam negeri melalui kebijakan substitusi impor. Sempat saya singgung adanya larangan ekspor mineral, yang sepertinya berkontribusi terhadap menurunnya kinerja ekspor komoditas pertambangan, dan meningkatnya ekspor metal. Meskipun saat ini ekspor CPO sepertinya dapat menjadi motor pendorong ekspor, Pemerintah sepertinya juga berupaya memberi insentif untuk industri turunan CPO.

Di samping itu, beberapa negara lain semakin gencar mendorong _go green_ dan mengeset target _zero emission_ yang semakin agresif. Tentunya hal ini dapat memukul prospek ekspor energi kotor seperti batubara dalam jangka panjang.

Memanfaat GVC, terutama _backward participation_ bisa jadi jalan keluar terbaik. Konsekuensinya, impor bahan baku menjadi tidak terhindarkan. Hal ini bukan sesuatu yang baru sebenarnya, karena memang sebagian besar impor Indonesia adalah bahan baku, energi dan barang modal. Artinya, kinerja impor Indonesia dapat menjadi indikator kinerja industri dalam negeri.

## Kinerja impor

Impor cenderung stagnan. Menurunnya permintaan energi merupakan dampak menurunnya mobilitas dan aktivitas manufaktur. Namun selain bahan pangan (yang mungkin meningkat karena harganya naik), sebagian besar menunjukkan penurunan impor pada 2020.

{{< figure library="true" src="/idm/gambar9.png" title="" numbered="" width=630 >}}

Penurunan impor barang modal (mchinery & electronics) dan bahan baku (terutama baja) juga indikator melemahnya produksi.

{{< figure library="true" src="/idm/gambar10.png" title="" numbered="" width=630 >}}

## Strategi Pemerintah

GVC dapat meningkatkan impor karena untuk kompetitif di pasar global, perusahaan harus mendapatkan akses bahan baku yang juga kompetitif. Banyak bahan baku murah harus dipasok dari luar negeri. beberapa contohnya adalah

- kedelai untuk tahu, tempe dan pakan ternak;
- besi baja dan bahan kimia;
- serat sintetis, dll

Di samping itu, strategi nilai tambah melalui larangan ekspor mineral mungkin butuh waktu sebelum dapat dituai berupa ekspor barang dengan nilai tambah lebih tinggi. Salah satu contohnya adalah investasi industri sel baterai yang mungkin membutuhkan waktu setidaknya 2 tahun. Vaksin memiliki peran yang mungkin lebih tinggi dalam melancarkan investasi asing dan produksi dalam negeri ketimbang ekspor. Sementara itu, mengandalkan fiskal menjadi sebuah keharusan.

Yang jelas, saat ini permintaan dunia yang tinggi akan komoditas meberikan peluang. Pemerintah perlu mencermati kebijakan lartasnya. PP turunan UU Cipta Kerja berorientasi ke penambahan nilai tambah dalam negeri dan investasi asing. Namun hal ini berpeluang menekan neraca pembayaran, setidaknya dalam waktu dekat. Hasilnya mungkin akan dituai agak lama. Dukungan fiskal yang cukup dapat menjadi solusi jangka pendek, sambil memantau peningkatan daya saing industri dalam negeri.

Permasalahan lain menggunakan lartas:Waspada bahaya retaliasi. Negara lain masih bisa mengakses mineral dari negara lain, sehingga daya tawar mereka sebenarnya tidak terlalu rendah. Jika negara lain melakukan retaliasi, hal ini dapat berpotensi membatasi skala ekonomis.

Meningkatkan nilai tambah dalam negeri tentunya adalah hal yang baik. Mungkin pertanyaannya lebih ke apakah sekarang saat yang tepat untuk melakukannya?

## Tanya jawab

1. 

1. 


## rumus

$$
RCA_{Ai}=\frac{\frac{X_{Ai}}{\sum_{j \in P} X_{Aj}}}{\frac{X_{wi}}{\sum_{j \in P} X_{wj} }} \geq 1
$$

RCA negara $A$ untuk barang $i$ tergantung pentingnya ekspor barang $i$ untuk negara $A$, dibandingkan dengan pentingnya barang $i$ di seluruh dunia $w$.

kembali ke [RCA](#rca)

## Agregasi

{{< figure library="true" src="/idm/kelompok.png" title="" numbered="true" width=600 >}}

kembali ke [RCA](#rca)

