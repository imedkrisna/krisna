---
layout: post
title: "drama larangan ekspor dan relaksasi standar di pasar APD Indonesia"
categories: [industri]
tags: [coronavirus COVID-19, perdagangan, industri]
date: '2020-06-10'
author: admin
---

Rasanya sudah bukan rahasia lagi kalau saya agak kritis terhadap larangan ekspor Kementerian Perdagangan, tepatnya Permendag 34 Tahun 2020 tentang larangan ekspor anti-septik, APD, masker, dan bahan baku APD. Peraturan ini mungkin niatnya baik, akan tetapi [dapat berdampak negatif](https://imedkrisna.github.io/covtrade/) karena mengganggu supply chain, mengurangi kredibilitas pemerintah maupun perusahaan kita, dan tidak menolong dalam hal meningkatkan kapasitas produksi. Apalagi kita sangat tergantung impor di hampir segala *item* yang berhubungan dengan COVID-19 (lihat tabel 1 dan tabel 2). Kita bisa saja membantu dunia memerangi COVID-19 dengan memberikan sumbangan tenaga penjahit APD, sambil mendapatkan barang-barang impor tersebut. Ekspor juga akan membantu mengamankan stok dolar untuk impor.

**Tabel 1.** impor barang-barang terkait penanganan COVID-19 (1,000 $)
<table>
  {% for row in site.data.coronaimpor %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>
<span style="font-size:0.8em"> *sumber: diolah dari Kementerian Perindustrian dari BPS* </span>

<span style="font-size:0.8em">catatan: klasifikasi WCO/WHO dapat dilihat di [sini](http://www.wcoomd.org/en/media/newsroom/2020/june/new-edition-of-the-wco-who-hs-classification-list-for-covid-19-medical-supplies-now-available). Saya masih pake edisi 2, yang paling baru adalah edisi 3</span>

**Tabel 2.** expor barang-barang terkait penanganan COVID-19 (1,000 $)
<table>
  {% for row in site.data.coronaekspor %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>
<span style="font-size:0.8em"> *sumber: diolah dari Kementerian Perindustrian dari BPS*</span>

<span style="font-size:0.8em">catatan: klasifikasi WCO/WHO dapat dilihat di [sini](http://www.wcoomd.org/en/media/newsroom/2020/june/new-edition-of-the-wco-who-hs-classification-list-for-covid-19-medical-supplies-now-available). Saya masih pake edisi 2, yang paling baru adalah edisi 3</span>

## Gangguan pada rantai pasok
Apa yang saya khawatirkan terjadi: [Swasta mampu menghasilkan cukup banyak APD, tapi tidak semua terserap oleh pasar dalam negeri](https://tirto.id/apd-lokal-melimpah-dan-kemenkes-enggan-menyerapnya-fETf). Penyebabnya adalah, Kementerian Kesehatan tidak mau meresikokan barang buatan dalam negeri yang kualitasnya tidak terjamin, bukan dari bahan non-woven. Yha, bahan non-woven spun bond ini adalah bahan impor, kita belum sanggup memproduksi massal bahan spun bond ini di dalam negeri. Sebagian besar APD produksi dalam negeri adalah berbahan dasar katun yang menurut Kemenkes tidak cukup baik, meskipun menurut produsen, APD karya mereka sudah memenuhi standar WHO.

Yang menurut saya cukup menarik adalah alasan dari perusahaan-perusahaan tersebut dapat memproduksi APD adalah karena [Kemenkes melakukan relaksasi ijin edar terhadap perusahaan yang menghasilkan APD](https://republika.co.id/berita/q8xdu7396/kemenkes-permudah-penerbitan-izin-edar-industri-produksi-apd). Bahkan, Kemenkes membanggakan pertumbuhan pesat perusahaan pemasok APD *berkat* inisiatif mereka merelaksasi ijin edar industri. Benar, berkat relaksasi tersebut, perusahaan pemasok APD bertambah banyak. Tetapi mereka sendiri yang menolak membeli karena tidak ada stadar, sesuatu yang mereka sendiri relaksasi melalui kebijakan. Wow!

Pelarangan ekspor APD Indonesia memaksa pengekspor bahan dasar harus berpikir ulang. Selama ini mereka mengandalkan negara seperti Indonesia untuk mengolah produk mereka. Peraturan ini memunculkan adanya risiko terhadap supply chain mereka, bahwa bahan baku yang mereka kirim ke Indonesia untuk dibikin APD mungkin tidak balik lagi secara utuh. Lebih baik bikin sendiri daripada risiko. Sebuah perusahaan 3d printing di Australia, 3DMEDiTech, [biasanya tidak sanggup berkompetisi APD dengan negara seperti Indonesia sebelumnya karena 3d printing jatohnya lebih mahal](https://www.abc.net.au/news/2020-04-14/inside-australias-race-to-prepare-for-the-worst-of-coronavirus/12140878?nw=0). Berkat adanya *excess demand* internasional (*partly thanks to countries baning export!*), harga APD mereka jadi masuk akal.

Tidak hanya Australia, berbagai negara lain di seluruh dunia mengalih-fungsikan usaha mereka menjadi pembuat masker dan APD. Jatohnya lebih mahal, tapi jelas lebih baik daripada tidak ada sama sekali. Pemerintah di negara-negara seperti Australia, RRT dan Amerika Serikat [membantu dengan berbagai cara untuk melancarkan usaha alih-usaha tersebut](https://www.vox.com/the-goods/2020/4/6/21207135/factories-face-masks-ventilators-hand-sanitizer-coronavirus-manufacturing). Hal-hal seperti *cheap loan*, *purchasing guarantee*, dan *active coordination* dilakukan untuk membantu perusahaan alih-fungsi, membeli alat dan bahan yang diperlukan, membantu perusahaan mengestimasi hitung-hitungan bisnis untuk ekspansi, dan *sharing know-how* serta standardisasi antar lembaga domestik bahkan internasional. Pernahs saya bahas di [tulisan saya yang lain](https://imedkrisna.github.io/covin/).

Sementara itu, sepanjang pengetahuan saya yang terbatas ini, hal-hal selain melarang ekspor, melancarkan impor, dan menghilangkan standar tampak belum terlihat diinisiasi oleh Pemerintah Indonesia. Setidaknya ada berbagai usaha dari tim gugus tugas meningkatkan *self-sufficiency* barang-barang COVID-19. Tapi ntahlah. Gugus tugas mendapatkan privilege untuk mengimpor secara langsung sih. Jadi sepertinya *self-sufficiency*-nya tetap akan bergantung impor. Bukan hal yang buruk, cuma agak-agak hipokrit aja.

## Tren ke depan
Pada akhir Juni, aturan larangan ekspor akan tidak berlaku lagi. Kemungkinan besar, larangan ekspor ini tidak akan diperpanjang oleh Kemendag. Mungkin hal berikutnya yang harus dipikirkan adalah bagaimana agar APD-APD yang terlanjur sudah dibuat ini, dapat diekspor ke luar negeri dengan harga yang cukup kompetitif, sesuai dengan standar yang diikuti oleh pasar internasional. Dengan adanya normal baru, mestinya permintaan APD juga akan meningkat secara berkesinambungan, sehingga ada ruang bagi produsen APD kita. Sekarang yang terpenting adalah membuat APD kita diakui oleh dunia internasional. Standar ini jadi penting banget apalagi setelah [kisruh APD RRT ditolak di mana-mana gara-gara tidak sesuai standar](https://www.google.com/url?sa=t&source=web&rct=j&url=http://amp.abc.net.au/article/12105110&ved=2ahUKEwjurv6UoffpAhXv7HMBHcPpCe0QFjAAegQIBhAC&usg=AOvVaw3ZmZyZLff4mhzRTol_vSm2&ampcf=1). Apalagi sekaramg negara-negara ini sudah dapat membuat APD sendiri dalam jumlah banyak (meski mungkin masih lebih mahal daripada APD *made in Indonesia*)

BTW di Indo kok ga ada kabar APD *faulty* dari RRT ya? Padahal kita dapat banyak banget APD dari negeri tirai bbu tersebut. Moga2 ga ada yang masalah dan saya cuma overthinking aja.

Hal lain yang dapat dilakukan mungkin adalah dengan mengandalkan demand dalam negeri. Kemenkes boleh menolak beli, mungkin swadaya masyarakat bisa diarahkan ke sini. Biar kita aja yang beli, lalu kita sumbangin ke Rumah Sakit. Tapi perlu kembali diingat, Rumah Sakit juga mungkin punya standar sendiri. Tidak adanya koordinasi demand-supply memang costly. Biasanya ini diatasi dengan institusi yang menjembatani *asymmetric information*, yaitu ya tukang cek standar, dalam hal ini Kemenkes. Tapi standarnya direlaksasi kemenkes sendiri, jadinya RS dan supplier harus komunikasi sendiri. Sekarang mungkin terlambat. Mudah-mudahan saya salah.

Tanpa solusi, maka perusahaan APD ini melakukan hal yang sia-sia. Cost yang sudah dikeluarkan bisa jadi tidak menghasilkan revenue. dampaknya? perusahaan tutup. tenaga kerja dipecat. ekonomi underutilise. Semoga ketika sudah kembali ke new normal, kita masih punya cukup perusahaan dan tenaga kerja.

## Pelajaran dari perspekif kebijakan publik
Bagi teman-teman yang menggeluti kebijakan publik atau perdagangan internasional, ada sebuah pelajaran berharga yang dapat diambil di sini: membuat kebijakan tidak semudah memencet tombol *on*-*off*. Nyalakan hambatan ketika dirasa butuh proteksi, kurangi hambatan ketika merasa butuh impor. Sembarangan matiin ekspor ternyata tidak terlalu berguna: kita tetap ngandelin impor APD *bahkan* ketika domestik bisa bikin sendiri. Sembarangan matiin standar juga ternyata menghasilkan barang yang kualitasnya tidak dapat diterima oleh Kemenkes sendiri. Jurus *on-off* ini sudah lama dipraktikkan oleh Kementerian Perdagangan untuk mengendalikan harga barang-barang terutama sembako. Biasanya sih berhasil. Tapi COVID-19 bukanlah fenomena biasa. Jurus *on-off* memang lebih mudah, tapi kita butuh kebijakan yang agak kreatif kali ini. Sesuatu yang tidak sesederhana *on-off*.

Pelajaran lainnya lagi: impor bukan sesuatu yang buruk. Seperti halnya saya membeli beras dari petani, Indonesia mengimpor alat-alat kesehatan juga bukan sesuatu yang jelek, *kok*. Dengan menggunakan analogi beli beras, alih-alih berpikir "bagaimana caranya bikin beras sendiri", saya lebih ke "bagaimana saya bisa berguna bagi petani sehingga mereka mau jual beras ke saya". Kompleksitas ekonomi adalah salah satu sumber kemakmuran. Kerja sama antar-profesi,antara petani dan non-petani, justru baik. Apalagi Indonesia sudah kenyang lah dengan segala percobaan swa-sembada yang hasilnya sangat boros dan tidak berkelanjutan.

Justru yang haris kita pikirkan adalah bagaimana kita bisa terlibat di ekonomi dunia. Jika kita tidak bisa bikin alkes, kita bisanya bikin apa? Sudah lama Indonesia berkontribusi melalui komoditas seperti minyak bumi (dulu banget), batu bara, dan kelapa sawit, sesuatu yang mudah dilakukan. Masih ada ruang untuk kontribusi di manufaktur, apalagi di tengah kebutuhan dunia untuk diversifikasi dari RRT. Ini juga butuh kebijakan yang lebih kreatif daripada sekedar *on-off*.

Lucu juga kalo dipikir-pikir. Emangnya kenapa sih kalo negara lain bisa bikin sesuatu yang kita butuhkan? Emangnya negara lain ga boleh berguna dan keren? Kita aja yang boleh keren? Wkwkw. Yasudahlah. Mudah-mudahan ini menjadi pelajaran yang baik bagi kita semua.