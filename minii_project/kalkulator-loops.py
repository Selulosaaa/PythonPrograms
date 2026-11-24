print("*" * 30)
print("SELAMAT DATANG DI KALKULATOR DENGAN LOOPS!")
print("*" * 30)

hasil = 0
hasil_2 = 1
list_angka = []

print("kami membutuhkan input angka yang kamu inginkan")
print("semua angkayang kamu ketik akan berjalan pada SATU operasi yang kamu pilih")
print("ketik 'sudah' jika ingin mengakhiri")
while True:
    angka = input("input angka yang kamu inginkan ")
    if angka.lower() == "sudah":
        break
    try:
        angka_bulat = int(angka)
        list_angka.append(angka_bulat)
    except ValueError:
        print('input hanya angka bulat atau sudah')

print("MASUKKAN OPERASIMU!")
print("1. pertambahan")
print("2. pengurangan")
print("3. perkalian")
operasi = int(input("masukkan angka sesuai operasi yang diinginkan(1/2/3) "))

if operasi == 1:
    for angka in list_angka:
        hasil += angka
elif operasi == 2:
    hasil = list_angka[0]
    for angka in list_angka[1:]:
        hasil -= angka
elif operasi == 3:
    hasil = hasil_2
    for angka in list_angka:
        hasil *= angka
else:
    print("tidak ada input yang valid!")
print(f"hasil perhitunganmu adalah {hasil}")
