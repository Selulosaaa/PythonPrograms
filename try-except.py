# Try-except di python adalah mekanisme untuk menangani errir atau exception saat program berjalan, sehingga program
# Tidak langsung berhenti secara paksa
# intinya, exceotion akan terjadi jika program mengalami error(yang menghentikan program)

while True: # membuat loop agar try-except selalu terjadi
    try:
        angka = int(input("input angka yang bisa membagi 10: "))
        hasil = 10 / angka
    except ValueError: # Disini jika input tidak berisi sebuah angka
        print("input harus angka")
        continue
    except ZeroDivisionError: # jika input angka nol
        print("input tidak bisa nol")
        continue
    print(hasil) # jika input valid maka akan print hasil
    break

