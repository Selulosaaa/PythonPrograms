print("Selamat datang di kasir!")
print("-" * 30)

# daftar list yang akan dipakai
barang = []
jumlah = []
harga = []
total = []

# input

while True:
    int_barang = input("input barang belanjaan! ")
    int_jumlah = int(input("input jumlah barang "))
    int_harga = int(input("input harga barang "))


    #Penambahan list
    barang.append(int_barang)
    jumlah.append(int_jumlah)
    harga.append(int_harga)

    # Penjumlahan barang
    total_harga = int_jumlah * int_harga
    total.append(total_harga)

    # Selesai
    selesai = input("apakah masih ada barang yang harus ditambahkan(Y/N)? ")
    if selesai.lower() == "y":
        continue
    elif selesai.lower() == "n":
        break
    else:
        print("INPUT HANYA BISA Y ATAU N")    

# STRUK PEMBELIAN
print("TERIMAKASIH TELAH BERBELANJA!")
print("STRUK BELANJA")

for nama, banyak, harga_satuan, subtotal in zip(barang, jumlah, harga, total):
    print(f"{nama} dengan jumlah {banyak} serta harga satuan {harga_satuan} dengan total {subtotal}")
    print("-" * 30)