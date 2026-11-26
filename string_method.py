# STRING METHOD!
# METHOD adalah fungsi milik objek string.
# method biasanya mengembalikan string baru, bukan mengubah asal

# 1. MENGUBAH HURUF
teks = "HallO WoRlD" # contoh teks yang akan dipakai
print(teks.capitalize()) # Hello world = hanya kapital di awal
print(teks.casefold()) # hello world = menormalkan teks untuk perbandingan tanpa membedakan kapital
print(teks.lower()) # hello world = mengubah seluruh teks menjadi huruf kecil
print(teks.upper()) # HELLO WORLD = mengubah seluruh teks menjadi huruf kapital
print(teks.swapcase()) # hALLo wOrLd = menukar huruf besar dan kecil
print("selamat pagi".title()) # Selamat Pagi = menjadikan awal setiap kata huruf besar

# Merapikan, mengisi, atau mengganti teks
print("judul".center(10, "-")) # meratakan teks ke tengah (size, [elemen])
print("judul".ljust(10, "-")) # meratakan teks ke kiri
print("judul".rjust(10, "-")) # meratakan teks ke kanan
print("45".strip(5)) # iis nol ke kiri dengan indeks terntetu
print("      halo     ".strip()) # menghilangkan spasi di kedua ujung
print("      halo     ".lstrip()) # menghilangkan spasi di kiri
print("      halo     ".rtrip()) # menghilangkan spasi di kanan
