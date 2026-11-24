# While dapat memiliki sebuah kondisi True
# Kondisi dimana program akan berjalan terus menerus
# WAJIB ada kondisi yang membuatnya False atau pakai command break

percobaan = 0
while percobaan < 3 : # kondisi True
    jawaban = input("Kamu harus pilih iya(iya/tidak) ")
    if jawaban.lower() == "iya":
        print("selamat datang dari bagian kami")
        break # break untuk menghentikan loops
    percobaan += 1
else:
    print("Sudah kebanyakan percobaan, anda gagal!")