# for loops adaalh jenis perualangan yangh berdasarkan jumlah iterasi yang diketahui

# for i in (1, 2, 3)
# i adalah loops variabel dan setelah o adalah iterasi yang diketahui

for i in (1, 2, 3, 4, 5, 6): # Kita punya 6 data dan data itu akan harus dijalankan oleh python
    print(f"ronde ke {i}")

# kita juga bisa memanggil lewat variabel
items = [1, 2, 3, 4, 5, 6]
for a in (items):
    print(f"barang ada di nomor: {a}")

# pakai fungsi range yang menghasilka deretan bilangan bulat
# formatnya berupa range(start, stop, step)

# stop = angka wajib
for k in range(5): # indeks dimulai dari nol
    print(k)

# start = angka opsional --> angka awal urutan
for j in range(1, 5): # indeks tetap nol namun dimulai dari 1
    print(j)

#step = angka opsional --> selisih atau langkah antar angka
for h in range(1, 11, 2): # jadinya 1, 3, dst
    print(h)