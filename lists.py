# lists adalah kondisi dimana variabel memiliki lebih dari 1 data
lists = ["bibi", "kakek", "nenek"]
print(lists) # print seluruh isi list
print(lists[0]) # indeks dimulai dari nol(0) outputnya adalah bibi

# ada beberapa command khusus di lists ini yaitu
# append = untuk menambahkan data
buah = ["apel", "alpukat", "kiwi"]
buah.append("jeruk")
print(buah)

# index = mengganti data di indeks tertentu dengan data baru
orang = ["agus", "didin", "eko"] # INDEKS DIMULAI DARI NOL
orang.insert(0, "Narji")
print(orang)

# reverse = membalikkan urutan list
hewan = ["badak", "kucing", "ayam"]
hewans = hewan.reverse()
print(hewan)

# sort = mengurutkan interger(angka) dari yang terkecil ke yang terbesar
angka = [1, 6, 9, 0, -4, -2, -6]
angka.sort()
print(angka)

# menggabungkan 2 list, hanya dengan menambahkan tanda "+"
gabungan = angka + hewan
print(gabungan)