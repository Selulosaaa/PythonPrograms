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
print("45".zfill(5)) # iis nol ke kiri dengan indeks terntetu
print("      halo     ".strip()) # menghilangkan spasi di kedua ujung
print("      halo     ".lstrip()) # menghilangkan spasi di kiri
print("      halo     ".rstrip()) # menghilangkan spasi di kanan
print("www.codegrammer.com".strip("cmowz.")) # hapus karakter ujung
print("banana".replace("na", "NA")) # menggnati "na" menjadi "NA"
print("banana".replace("na", "NA", 1)) #mengganti "na" makimal 1
print("unhappy".removeprefix("un")) # mengganti huruf tertentu
print("kucing.txt".removesuffix(".txt"))

# cari dan hitung
kalimat = "pisang dan pisang"
print(kalimat.count("pisang")) # menghitung jumlah kemunculan pisang
print(kalimat.find("dan")) # mencari posisi
print(kalimat.rfind("pisang")) # posisi kemunculam terakhir
print(kalimat.index("dan")) #  mengedcek adanya kata tersebut apa tidak
print("laporan.pdf".startswith("lap")) # True = jika mengandung kata kunci itu
print("laporan.pdf".endswith(".pdf"))    # True = jika mengandung kata dalam akhir kalimat
#print("foto.jpeg".endswith(".png", ".jpeg")) # True = bisa memakai tupple

# MEMECAH DAN MENGGABUNGKAN
print("jambu,mannga,kelapa,jeruk".split(",")) # mengubah mereka menjadi list
print("satu dua\t tiga".split()) # pisah dari satu/lebih whitespace
print("satu,dua,tiga".rsplit(",", 1)) # pecah dari kanan makismal 1 kali
print("a\nb\nc".splitlines())              # ['a', 'b', 'c']
print("nama: Ayu".partition(": "))          # ('nama', ': ', 'Ayu')
print("folder/file.txt".rpartition("/"))   # pisah pada pemisah terakhir
print(", ".join(["apel", "jeruk", "mangga"]))  # apel, jeruk, mangga

# 5. MEMERIKSA ISI STRING
print("abc123".isalnum())       # True: semua karakter huruf atau angka
print("abc".isalpha())          # True: semua karakter huruf(hanya mengandung huruf tanpa angka)
print("123".isascii())          # True: semua karakter ASCII
print("123".isdecimal())        # True: semua karakter angka desimal
print("²".isdigit())            # True: cakupannya lebih luas dari isdecimal
print("⅕".isnumeric())          # True: cakupannya paling luas untuk angka
print("nama_saya".isidentifier())  # True: dapat menjadi identifier Python
print("halo".islower())         # True: huruf cased semuanya kecil
print("Halo Dunia".istitle())   # True: tiap kata mengikuti kapitalisasi title
print("   ".isspace())          # True: string berisi whitespace saja
print("HALO".isupper())         # True: huruf cased semuanya besar
print("teks\n".isprintable())   # False: newline bukan karakter printable

# Daftar lengkap 47 method publik str:
# capitalize, casefold, center, count, encode, endswith, expandtabs, find,
# format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit,
# isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper,
# join, ljust, lower, lstrip, maketrans, partition, removeprefix,
# removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip,
# split, splitlines, startswith, strip, swapcase, title, translate, upper,
# zfill.
