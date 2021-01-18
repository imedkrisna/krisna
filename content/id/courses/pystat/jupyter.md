---
date: "2020-08-20T00:00:00+01:00"
draft: false
linktitle: Python di Jupyter
menu:
  example:
    parent: Memulai dengan Python 
    weight: 1
title: Menjalankan Python di Jupyter Notebook
toc: true
type: book
weight: 1
editable: false
commentable: false
---
## Tentang Jupyter Notebook
Python adalah program yang dapat dijalankan dengan berbagai cara. Namun sampai saat ini Jupyter Notebook menurut saya masih paling user friendly dibandingkan cara-cara lain. Jupyter Notebook membuat penulisan python dapat didokumentasikan dengan mudah. Jupyter Notebook digunakan oleh banyak perusahaan besar seperti Google, Microsoft, dan IBM. Ada banyak fitur yang ditawarkan, tapi kita pakai yang gratis-gratis saja untuk sekarang.

## Jupyter Notebook dapat dibuka dengan dua cara:

Di kolom search, ketik “Anaconda” lalu klik “Anaconda Navigator” yang logonya bulat hijau. Setelah ia jalan, klik “Jupyter Notebook”. Ketika selesai dengan menggunakan Jupyter Notebook, jangan lupa disilang
Di kolom search, ketika “Anaconda” lalu klik “Anaconda Prompt” yang logonya kotak hitam. Ketik “Jupyter Notebook” di Anaconda Prompt.
Jika Anaconda diinstall dengan settingan default, Jupyter Notebook akan jalan di komputer anda di working directory “C:\Users<your-username>\Anaconda3”. File Jupyter Notebook akan memiliki ekstensi .ipynb (ekstensi tuh yang titik setelah nama file. Sebagai perbandingan, Kalau excel .xlsx, kalau word .docx dll). Jika anda tidak mengubah-ubah lokasi apapun, maka setiap kali menjalankan Jupyter Notebook, anda akan berada di lokasi yang sama yaitu “C:\Users<your-username>” jadi file anda akan ada di sana secara otomatis. Tidak perlu terlalu dipusingkan.

Tampilan Jupyter Notebook
Jupyter Notebook akan jalan di browser default anda.

## Tampilan di Jupyter Notebook

Jupyter Notebook berbentuk seperti ini:
{{< figure library="true" src="jjupyter.PNG" title="Tampilan Jupyter Notebook" >}}

Beberapa bagian yang paling penting di Jupyter Notebook yang kita akan pakai di buku ini adalah menu dan cell. Di Menu ada beberapa tombol untuk membantu kita melakukan macem-macem hal seperti save, restart session, convert, insert cell dan lain-lainnya. Jika anda sudah sering pakai Jupyter Notebook lama-lama akan lebih sering pakai *short-cut* daripada menu. Namun untuk awal-awal, ada baiknya sering lihat fungsi-fungsi yang ada di menu.

Di Jupyter Notebook, anda akan mengetik kode-kode yang diperlukan di sebuah kotak yang bernama "cell". Di buku ini, kita hanya memerlukan dua tipe cell yaitu "code" dan "markdown". Anda memerlukan tipe cell "code" untuk mengetik kode yang akan dijalankan oleh python. Jika kode yang anda masukkan dapat dibaca oleh pyton, maka hasilnya akan muncul di output. Output itu bukan sesuatu yang anda ketik, tapi sesuatu yang muncul setelah anda menjalankan (*run*) kode anda di cell code.

Untuk menjalankan sebuah kode, anda ketik kode-nya di cell , lalu klik tombol {{< icon name="play" pack="fas" >}} run, atau dengan *short-cut* `ctrl+enter` atau `shift+enter`.

Sementara itu, anda dapat menggunakan cell "markdown" untuk tujuan mengetik. Cell markdown tidak bisa di-jalankan dan tidak akan mengeluarkan output apapun.

Setiap cell sendiri memiliki dua mode, yaitu command mode dan edit mode. ketika cell anda berwarna hijau, artinya anda sedang di mode edit. Anda dapat mengetik di cell yang sedang aktif. Ketika cell berwarna biru, artinya anda sedang di mode command. Mode command membuat *keyboard* anda mengaktifkan *shortcut* dan bukan mengetik. 

Untuk masuk ke edit mode, anda cukup me-klik cell yang ingin anda edit. Jika anda klik area lain di luar cell, maka anda akan masuk ke command mode. *Short-cut* untuk masuk ke edit mode adalah `enter`, sementara untuk ke command mode adalah `escape`.

## menyimpan jupyter notebook

#### .ipnyb
File jupyter notebook akan secara otomatis tersimpan dengan ekstensi <nama>.ipnyb. Anda baru bisa buka file dengan ekstensi .ipynb jika anda memulai anaconda. Jadi jangan lupa untuk membuka jupyter notebook melalui anaconda navigation atau anaconda prompt terlebih dahulu.
    
#### pdf
Untuk menyimpannya dalam bentuk pdf, gunakan

`file -> download as -> .html`

anda akan memiliki file <nama>.html. Buka file tersebut dengan browser anda (chrome, edge, safari, mozila) lalu tekan `ctrl+p` lalu pilih "print to pdf".
    
#### Word (docx)
Jika anda sudah menginstall [pandoc](https://pandoc.org/installing.html), anda bisa menyimpan `<nama>.ipynb` dalam wujud word (docx). Anda pertama perlu file `<nama>.html` terlebih dahulu dengan melakukan

`file -> download as -> .html` (sama seperti mau membuat pdf).

Setelah punya file `<nama>.html`, anda tinggal membuka anaconda prompt atau cmd prompt, lalu ketik:

```
pandoc -s <nama>.html -o <nama>.docx 
```

#### $\LaTeX$ (.tex)
Untuk membuat tampilan pdf yang lebih cantik, anda membutuhkan $\LaTeX$. anda dapat mengubah `.ipynb` menjadi `.tex` dengan menu:

`file -> download as -> .TeX`

File `.tex` dapat dijalankan dengan menggunakan program khusus. Untuk windows, [MikTeX](https://miktex.org/download) adalah yang paling direkomendasikan. Untuk yang lain, bisa pakai [TeXLife](https://www.tug.org/texlive/acquire-netinstall.html).

## Kode-kode Sederhana
###### beberapa hal yang dapat anda lakukan
Silakan coba-cobain nge-run sembarangan. Anda dapat mendelete cell dengan tekan tombol d dua kali di command mode.


```python
# Menulis angka
1
```




    1




```python
# fungsi tambah-tambahan
1+1
```




    2




```python
# menulis kalimat harus menggunakan tanda petik
"apa kabar dunia?"
```




    'apa kabar dunia?'




```python
# tes logika (boolean)
1 > 2
```




    False



###### menempelkan informasi ke dalam sebuah obyek
Salah satu kelebihan python adalah betapa mudahnya melekatkan informasi (dalam bentuk kode/ekspresi/data) kepada sebuah obyek. Anda melekatkan informasi dengan menggunakan tanda `=`


```python
# lekatkan '1+1' kepada obyek bernama 'x'
x=1+1
```

seperti anda lihat di atas, jika 1+1 kita lekatkan ke sebuah obyek, maka outputnya tidak langsung dicetak. anda harus panggil dulu obyek tersebut dengan mengetik namanya, atau menggunakan fungsi `print()`


```python
# memunculkan output x
x
```




    2




```python
# memunculkan output x dengan fungsi print
print(x)
```

    2
    

Dalam hal ini, menggunakan fungsi `print()` menghasilkan output yang sama persis dengan mengetik langsung nama obyeknya. Tapi nanti kita akan melihat beberapa kegunaan `print()` yg lain ketika obyek kita isinya lebih ribet daripada sekedar `1+1`

Anda juga dapat memanipulasi obyek x dengan operasi matematika sepert `+` dan `-` dan lainnya.


```python
# Menambahkan x dengan 3
x+3
```




    5




```python
# menempelkan x+3 ke obyek lain dan langsung mencetaknya 
y=x+3
y
```




    5




```python
# menambahkan 2 obyek dan melekatkannya ke obyek ke-3
z = x + y
z
```




    6



ketikan setelah tanda `#`pagar akan diabaikan oleh python. Peneliti biasanya menggunakan tanda `#`pagar untuk memberi komentar atau keterangan tentang kode yang mereka jalankan. Jika anda menggunakan Jupyter Notebook untuk mengerjakan skripsi atau tugas kuliah, saya sangat merekomendasikan menggunakan tanda `#`pagar untuk memberi keterangan tentang kode anda kepada teman atau pemeriksa.

Jadi jika anda ingin menulis komentar atau keterangan tentang kode yang anda tulis, gunakan tanda `#`pagar


```python
z = z-6 # mengubah Z, sebelumnya z=5
z       # y sudah diupdate dengan mengurangkan dengan 6
```




    0



## Tentang fungsi

kita akan menggunakan banyak sekali fungsi ketika memanipulasi obyek di python, seperti `print()`. Seiring dengan mengikuti buku ini, kita akan melihat beberapa fungsi lain yang esensial untuk melakukan analisis statistika.

Jika anda tidak mengerti sebuah fungsi tuh sebenernya melakukan apa, anda dapat menggunakan tanda `?` setelah mengetik fungsi. Pastikan anda terhubung dengan internet.

Coba anda jalankan kode `print?` dan lihat apa yang terjadi.

## Tentang paket / modul

Di python ada yang disebut "package" atau "module", saya bahasa Indonesiakan menjadi paket atau modul. Paket-paket ini berisi fungsi-fungsi yang aslinya tidak ada di python, tapi setelah dipanggil / diimpor, jadi bisa kita gunakan. Beberapa paket ini sangat esensial untuk *data science*, seperti `pandas` dan `matplotlib`.

kita memanggil paket ini dengan kode import. Contoh, mari kita gunakan paket `sys` untuk melihat versi python yang kita gunakan di komputer kita


```python
import sys
sys.version
```




    '3.7.7 (default, Apr 15 2020, 05:09:04) [MSC v.1916 64 bit (AMD64)]'



fungsi `sys.version` tidak ada di python original. Kita harus memanggilnya terlebih dahulu dengan menggunakan `import sys` supaya dapat menggunakan fungsi-fungsi yang ada `sys`-nya. Import paket tidak perlu dilakukan di setiap cell. Cukup sekali saja untuk setiap sesi. Tapi jika anda buka python baru, anda harus import lagi untuk sesi tersebut.

## Tentang tipe (type) obyek

Obyek di python dapat digolongkan menjadi beberapa tipe. anda dapat mengetahui tipe sebuah obyek dengan menggunakan fungsi `type('obyek')`. Contohnya:


```python
type(x)
```




    int




```python
type([x,y,z])
```




    list




```python
type("apa kabar dunia?")
```




    str




```python
type(1<2)
```




    bool



seperti dapat anda lihat di atas, ada setidaknya 4 tipe obyek yang dikenali oleh python. X, sebuah obyek yang berisi sebuah angka 2, dikenali sebagai `int`, kependekan dari integer. susunan obyek yang terdiri dari x, y, dan z, dikenali sebagai `list`. Sementara itu, frasa "apa kabar dunia?" dikenali sebagai `str`, atau kependekan dari string. Sementara yang terakhir, `bool` kependekan dari boolean, adalah logika.

Tipe-tipe ini sangat penting untuk diketahui karena kita akan memanipulasi mereka dengan cara yang berbeda-beda.

#### Angka (integer dan float)

Di python, ada dua tipe untuk angka, yaitu integer (int) dan floating (float). Integer adalah bilangan cacah, yaitu bilangan yang terdiri dari angka tanpa koma koma. Float adalah bilangan bulat, yaitu bilangan yang ada koma-koma nya. 

Misalnya, Pak Tedjo punya tiga orang anak. artinya, anak pak tedjo adalah obyek bilangan cacah (integer). Di desa Pak Tedjo, kepala keluarganya memiliki rata-rata 2,3 orang anak. Rata-rata anak di desa Pak Tedjo adalah obyek bilangan bulat (float). Tipe yang akan kita gunakan akan tergantung dari jenis data yang kita miliki.

Di Python, kita akan gunakan `.` sebagai koma. Kenapa? Yah orang barat pakai titik sebagai koma jadi kita ikut aja. Kita gunakan `_` untuk pemisah ribuan.


```python
a=3
type(a)
```




    int




```python
b=2.3
type(b)
```




    float



interaksi antara integer dan float akan menjadi float


```python
type(a+b)
```




    float



#### Huruf (Strings)

Di python, obyek yang berisi huruf disebut `str` atau `string`. Misalnya data yang isinya nama, maka data tersebut akan dikategorikan sebagai string. Namun demikian, angka juga dapat dikategorikan sebagai `string` jika angka tersebut tidak memiliki makna hitung apapun. Maksudnya, nomor yang bertipe `str` tidak dapat dibandingkan maupun ditambah atau dikurangi. Misalnya, orang yang punya nomor rekening 1234 tidak berarti duitnya lebih banyak daripada orang yang nomor rekeningnya 1235. Untuk menyimpan data string, anda harus menggunakan tanda petik. Boleh `'`, boleh juga `"`.


```python
type(3)
```




    int




```python
type('3') # angka 3 akan menjadi string jika dikelilingi dengan tanda petik.
```




    str




```python
type("3")
```




    str




```python
3+3
```




    6




```python
"3" + 3 # angka bertipe string tidak dapat ditambah dengan angka bertipe integer.
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-43-a62ff2a7686c> in <module>
    ----> 1 "3" + 3
    

    TypeError: can only concatenate str (not "int") to str


Anda dapat menambahkan string dengan string di python. Tapi di R tidak bisa yaa


```python
"nama saya adalah" + "Pak Tedjo"
```




    'nama saya adalahPak Tedjo'



ups. harusnya dikasih spasi. anda juga bisa menambahkan dua obyek string


```python
a = "nama saya adalah " # lihat saya nambahin spasi setelah adalah
b = "Pak Tedjo"
a+b
```




    'nama saya adalah Pak Tedjo'



string dapat dikali dengan integer untuk mengulang string tersebut


```python
a+b*3 # apa yang terjadi kalau b yg isinya "Pak Tedjo" dikali 3?
```




    'nama saya adalah Pak TedjoPak TedjoPak Tedjo'




```python
(a+b)*3 # bagaimana jika (a+b) yang dikali 3?
```




    'nama saya adalah Pak Tedjonama saya adalah Pak Tedjonama saya adalah Pak Tedjo'



Manipulasi string bisa lebih keren lagi dengan contoh berikut ini:


```python
nama="Pak Tedjo"
usia=50
pekerjaan="Pak RT"

tentang_Tedjo=f"{nama} adalah seorang bapak-bapak berusia {usia} tahun yang bekerja sebagai {pekerjaan}"
print(tentang_Tedjo)
```

    Pak Tedjo adalah seorang bapak-bapak berusia 50 tahun yang bekerja sebagai Pak RT
    

dapatkah anda memahami apa yang terjadi di atas? Apa fungsi dari {}? di tahun depan, usia Pak Tedjo akan bertambah 1 tahun. Bagaimana mengubah "tentang_Tedjo" yang paling mudah dan cepat?

#### Boolean (logika)
Boolean adalah tipe yang bentuknya logika. Biasanya kita menggunakan ini untuk fungsi `if`, `else` dan kombinasinya.


```python
t=True
f=False
type(t)
```




    bool




```python
type(f)
```




    bool



Boolean hanya terdiri dari dua ekspresi, yaitu `True` dan `False`. Jangan lupa untuk **tidak** menggunakan tanda petik. Boolean dapat ditambahkan, di mana `True` bernilai 1 sementara `False` bernilai 0. Hasilnya akan menjadi `int` atau `float` Kita akan lebih jauh mengeksplorasi ini nanti.


```python
t+f
```




    1




```python
type(t+f)
```




    int




```python

```
