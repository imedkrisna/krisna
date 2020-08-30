---
date: "2020-08-20T00:00:00+01:00"
draft: false
linktitle: Numpy
menu:
  example:
    parent: Memulai dengan Python 
    weight: 2
title: Menggunakan Numpy
toc: true
type: docs
weight: 2
editable: false
commentable: false
---

## Apa itu Numpy?
Numpy adalah salah satu *library* atau paket yang berguna untuk melakukan manipulasi angka / matematika. Dengan Numpy, kita tidak harus mengetik dengan bahasa *native* python yang lumayan njelimet, dan cukup panggil fungsi-fungsi di Numpy dengan bahasa yang lebih simpel. Tidak hanya itu, Numpy sangat esensial untuk mempercepat computing anda. Jika anda serius ingin menjadi tukang model, maka anda akan menulis program yang panjang banget. Perbedaannya sangat terasa semakin panjang program yang anda tulis.

Untuk memanggil Numpy, biasanya kita menulis:

```python
import numpy as np
```
setelah itu, semua fungsi di numpy harus diketik didahului dengan `np`.

Konten dari bagian ini diambil dari situs belajar Python untuk ekonom gratisan, [Quantecon](https://python-programming.quantecon.org/). Saya hanya menulis yang penting-penting aja untuk praktis, tapi jika anda ingin belajar lebih jauh, sangat disarankan melirik kontek Quantecon.

#### Array processing
Salah satu yang membuat Numpy begitu cepat adalah apa yang disebut dengan *array processing*. Array-nya Numpy bentuknya agak mirip `list`-nya python, tapi dapat diproses dengan jauh lebih cepat. Dalam memproses matrix algrebra, pakai Numpy jelas lebih efisien.


```python
import numpy as np
# membuat array berisi 0
a = np.zeros(3)
a
```




    array([0., 0., 0.])




```python
type(a)
```




    numpy.ndarray



seperti anda lihat di atas, tipe dari $a$ adalah `numpy.ndarray`.

array di Numpy harus berbentuk sama semua. Jika `list` python dapat berupa macem-macem (misalnya 1 list bisa diisi integer, boolean maupun string), numpy array semuanya harus berbentuk sama. Integer semua, string semua, dst.

Coba kita cek tipe data dari setiap elemen di array $a$


```python
display(type(a[0]),
        type(a[1]),
        type(a[2]))
```


    numpy.float64



    numpy.float64



    numpy.float64


Seperti dapat dilihat di atas, semua elemen di array $a$ memiliki tipe `float64`. Jadi, $a$ adalah array dengan tipe `numpy.ndarray`, sementara elemen dari array $a$ adalah tiga 0 dengan tipe `float64`. Tipe `float64` adalah *default* jika kita tidak memberi tahu Numpy tipe apa yang kita inginkan.

Seperti kita ketahui, kita menggunakan `float` jika ingin menghitung bilangan bulat (ada koma-koma). Biasanya sih kita sering memakai tipe ini. Tapi jika anda ingin memodelkan sesuatu yang diskrit (bilangan asli), maka kita harus menjadikan anggota $a$ sebagai `int`. 


```python
b=np.zeros(3,dtype=int)
type(b[0])
```




    numpy.int32



#### Bentuk dan dimensi
Fungsi di atas tidak memberikan bentuk maupun dimensi pada array $a$ dan array $b$ kita. Tentu saja kita butuh mengutik-utik bentuk array kita jika kita mau melakukan manipulasi matrix algebra. Untuk memberi dimensi pada array anda, gunakan fungsi `shape`.


```python
# Membuat sembilan elemen 0
c=np.zeros(9)

# membentuk c menjadi vektor (9,1)
c.shape=(9,1)
c
```




    array([[0.],
           [0.],
           [0.],
           [0.],
           [0.],
           [0.],
           [0.],
           [0.],
           [0.]])




```python
# membentuk c menjadi vektor (1,9)
c.shape=(1,9)
c
```




    array([[0., 0., 0., 0., 0., 0., 0., 0., 0.]])




```python
# Membentuk c menjadi matrix n x n (sama sisi)
c.shape=(3,3)
c
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])



Selain `np.zeros`, kita juga dapat menciptakan array spesial dengan menggunakan metode lain. Misalnya, `np.ones` akan membuat array yang isinya satu semua. `np.empty` menciptakan array kosong yang nantinya harus kita isi sendiri. Untuk membuat matrix identitas, kita gunakan `np.identity(n)` atau `np.eye(n)` di mana n adalah dimensi matrix identitas yang diinginkan. `np.linspace(a,b,c)` akan membuat sebuah array lurus yang secara merata mengisi angka di antara a dan b, sebanyak c unit.


```python
np.linspace(1,5,5) # akan berisi array dengan 5 elemen di antara 1 dan 5
```




    array([1., 2., 3., 4., 5.])




```python
np.linspace(1,5,9) # akan berisi array dengan 9 elemen di antara 1 dan 5
```




    array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. ])




```python

```
