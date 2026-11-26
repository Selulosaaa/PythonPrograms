# STRING METHODS
# Method adalah fungsi milik objek string. String tidak berubah (immutable);
# method biasanya mengembalikan string baru, bukan mengubah string asal.

# 1. UBAH HURUF BESAR/KECIL
teks = "hELlo woRLD"
print(teks.capitalize())  # Hello world: kapital di awal, sisanya kecil
print(teks.casefold())    # hello world: normalisasi untuk perbandingan teks
print(teks.lower())       # hello world: semua huruf kecil
print(teks.upper())       # HELLO WORLD: semua huruf besar
print(teks.swapcase())    # HelLO WOrld: tukar besar/kecil
print("selamat pagi".title())  # Selamat Pagi: huruf awal setiap kata besar

# 2. RAPIKAN, TAMBAH ISI, DAN GANTI TEKS
print("judul".center(15, "-"))  # -----judul-----: rata tengah
print("judul".ljust(10, "."))   # judul.....: rata kiri
print("judul".rjust(10, "."))   # .....judul: rata kanan
print("42".zfill(5))            # 00042: isi sisi kiri dengan nol
print("  halo  ".strip())       # "halo": hapus spasi di kedua ujung
print("  halo  ".lstrip())      # "halo  ": hapus spasi di kiri
print("  halo  ".rstrip())      # "  halo": hapus spasi di kanan
print("www.example.com".strip("cmowz."))  # "example": hapus karakter ujung
print("banana".replace("na", "NA"))       # baNANA
print("banana".replace("na", "NA", 1))    # baNAna: ganti maksimal 1 kali
print("unhappy".removeprefix("un"))       # happy
print("cat.txt".removesuffix(".txt"))     # cat

# strip(chars) menghapus kumpulan karakter di ujung, bukan potongan kata.
# Untuk membuang prefix/suffix tertentu, gunakan removeprefix/removesuffix.

# 3. CARI DAN HITUNG
kalimat = "pisang dan pisang"
print(kalimat.count("pisang"))       # 2: jumlah kemunculan
print(kalimat.find("dan"))           # 7: posisi pertama, -1 jika tidak ada
print(kalimat.rfind("pisang"))       # posisi kemunculan terakhir
print(kalimat.index("dan"))          # seperti find(), tetapi error jika tak ada
print(kalimat.rindex("pisang"))       # seperti rfind(), tetapi error jika tak ada
print("laporan.pdf".startswith("lap"))  # True: diawali teks tertentu
print("laporan.pdf".endswith(".pdf"))   # True: diakhiri teks tertentu
print("foto.jpeg".endswith((".png", ".jpeg")))  # True: bisa memakai tuple

# count/find/index menerima start dan end opsional, misalnya:
print("banana".find("a", 2, 5))  # cari hanya pada rentang indeks 2 sampai 4

# 4. MEMECAH DAN MENGGABUNGKAN
print("merah,hijau,biru".split(","))       # ['merah', 'hijau', 'biru']
print("satu  dua\t tiga".split())          # pisah pada satu/lebih whitespace
print("satu,dua,tiga".rsplit(",", 1))      # pecah dari kanan, maksimal 1 kali
print("a\nb\nc".splitlines())              # ['a', 'b', 'c']
print("nama: Ayu".partition(": "))          # ('nama', ': ', 'Ayu')
print("folder/file.txt".rpartition("/"))   # pisah pada pemisah terakhir
print(", ".join(["apel", "jeruk", "mangga"]))  # apel, jeruk, mangga

# split(sep) mempertahankan bagian kosong: "a,,b".split(",") -> ['a', '', 'b']
# join dipanggil pada pemisah dan semua anggota iterable harus berupa string.

# 5. MEMERIKSA ISI STRING
print("abc123".isalnum())       # True: semua karakter huruf atau angka
print("abc".isalpha())          # True: semua karakter huruf
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

# isdecimal() lebih ketat daripada isdigit(), dan isnumeric() paling luas.
# Semua method is...() menghasilkan True/False.

# 6. FORMAT TEKS DAN TAB
print("Halo, {}!".format("Dina"))             # Halo, Dina!
print("{nama} berumur {umur}".format_map({"nama": "Dina", "umur": 20}))
print("A\tB".expandtabs(4))  # perluas tab menjadi jarak tab-stop 4 kolom

# f-string sering menjadi pilihan termudah untuk variabel:
nama = "Dina"
umur = 20
print(f"{nama} berumur {umur}")

# 7. ENCODING DAN PENGGANTIAN KARAKTER
print("halo".encode("utf-8"))  # b'halo': ubah string menjadi bytes

tabel = str.maketrans("aeiou", "12345")
print("selamat".translate(tabel))  # s2l1m1t: terapkan tabel karakter

# maketrans() membuat tabel untuk translate(); keduanya sering dipakai bersama.

# Daftar lengkap 47 method publik str:
# capitalize, casefold, center, count, encode, endswith, expandtabs, find,
# format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit,
# isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper,
# join, ljust, lower, lstrip, maketrans, partition, removeprefix,
# removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip,
# split, splitlines, startswith, strip, swapcase, title, translate, upper,
# zfill.
