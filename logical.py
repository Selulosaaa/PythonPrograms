# operator logika. Operator ini menggabungkan atau membalik hasil kondisi, 
# yang biasanya berupa True atau False.

# ada 3: and, or, not.

# logika and = digunakan untuk dua kondisi secara bersamaan
# True --> kedua kondisi benar
# False --> salah satu atau dua dua kondisi salah
x = 40
y = 30
z = 10
if x > y and y > z: # jika angka x lebih besar dari y dan y lebih besar dari z
    print("x adalah angka paling besar") 
else:
    print("x bukanlah angka yang paling besar")
# semua kondisi benar jadi akhirnya True

umur = 16
punya_tiket = True
if umur >= 17 and punya_tiket:
    print("boleh masuk")
else:
    print("Tidak boleh masuk")
# pengecekan pertama tidak lolos karena umur 16 tahun
# pada pengecekan dua lolos karena punya tiket
# output tetap False karena 1 kondisi tidak valid

# logika or = digunakan untuk 2 kondisi yang minimal salah satu kondisi benar
# True --> keuda kondisi atau salah satu kondisi benar
# False --> kedua kondisi salah
if x > y or y > z: # kedua kondisi benar maka hasilnya True
    print("x adalah angka paling besar")
else:
    print("x bukanlah angka yang paling besar")

if umur >= 17 or punya_tiket:
    print("boleh masuk")
else:
    print("Tidak boleh masuk")
# hasil True karena salah satu kondisi benar
# tiket bernilai True maka dia punya tiket jadi True

# logika not = not adalh logika untuk membalikkan keadaan
# True --> kondisi bernilai False
# False --> Kondisi bernilai True
if not(x > y and y > z): 
    print("x adalah angka terbesar")
else:
    print("x adalah angka terkecil")
# kondisi sebenarnya semua True, namun karena ada not maka kondisi dibalikkan

# contoh lain
panas = False

if not panas: # membalikkan panas menjadi True 
    print("Udaranya PANASSS") # OUTPUTNYA adalah baris ini
else:
    print("Ohh tidak panas")