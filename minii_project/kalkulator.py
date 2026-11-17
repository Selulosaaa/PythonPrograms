print("*" * 30)
print("SELAMAT DATANG DI KALKULATOR SEDERHANA")
print("*" * 30)

angka_1 = int(input("masukkan angka pertamamu"))
angka_2 = int(input("masukkan angka kedua "))

print("terimakasih telah memasukkan angka")
print("sekarang kami butuh operasi yang diinginkan")
print("1. pertambahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")
print("*" * 30)
operasi = int(input("masukkan operasi yang diinginkan(1/2/3/4) "))

if operasi == 1:
    hasil = angka_1 + angka_2
    print(f"hasil dari pertambahan antara {angka_1} dan {angka_2} adalah {hasil}")
elif operasi == 2:
    hasil = angka_1 - angka_2
    print(f"hasil dari pengurangan antara {angka_1} dan {angka_2} adalah {hasil}")
elif operasi == 3:
    hasil = angka_1 * angka_2
    print(f"hasil dari perkalian antara {angka_1} dan {angka_2} adalah {hasil}")
elif operasi == 4:
    if angka_2 == 0:
        print("Pembagi tak bisa nol!")
    else:
        hasil = angka_1 / angka_2
        print(f"hasil dari pembagian antara {angka_1} dan {angka_2} adalah {hasil}")