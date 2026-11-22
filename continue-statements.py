# continue statement adalah bagian dari control statement

# continue  adalah pernyataan kontrol dalam perulangan pemrograman
# gunanya untuk mengehentikan iterasi saat ini, melewati sisa kode setelahnya pada putaran tersebut
# lalu langsung melompat ke iterasi berikutnya

for i in range(1, 6):
    if i == 3: # kondisi benar dan akan dilewati
        continue # ini akan melewati print angka 3
    print(i)

# continue kadang bisa untuk mendeteksi data yang kosong tanpa mengehentikan programnya secara langsung

nama = ['agus', 'heri', '', 'hendra']

for a in nama:
    if a == '':
        print("ada nama yang kosong")
        continue # dia skip data yang kosong dan melanjutkan program
    print(f"nama yang ada: {a}")

