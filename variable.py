# variabel adalah tempat untuk menyimpan sebuah data di python

# contoh kecil, variabel dapat menyimpan sebuah string dengan menggunakan string
nama = "agus" # isi variabel "nama" adalah "agus"
print(nama) # memunculkan variabel cukup panggil dengan nama variabelnya
            # python merupakan bahasa yang sensitif, jadi perhatikan spasi dan tandanya

# untuk menyimpan interger(int) cukup tulis angka nya saja
umur = 37
print(umur)

# variabel juga bisa dipakai untuk operasi matematika
x = 30
y = 20
hasil = x + y
print(hasil)

# variabel list 
# variabel list adalah variabel yang dapat diisi lebih dari 1 data
# gunakan [] untuk variabel list
isi = ["agus", "didin", "arip"] # indeks dimulai dari 0
isi.append("budi") # append untuk menambahkan elemen lain di akhir
print(isi) # disini akan memanggil nama agus

letters = list("python")
print(letters) # ini mengeja kata

angka = list(range(5))
print(angka) # print angka, yang hitungannya dari 0

# kita bisa masukkan isi list dengan list lainnya
matrix = [[1, 3 , 4],
          [4, 5, 9]]
print(matrix)