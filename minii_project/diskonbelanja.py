print("halo selamat datang! Dikasir andalan ini")
print("-" * 20)

print("pada perhari ini ada promo bagi yang memiliki member!")
print("1. Diskon 5% untuk total belanjaan lebih 20.000")
print("2. Diskon 8% untuk total belanjaan lebih s50.000")
print("3. Diskon 10% unutk total belanjaan lebih dari 100.000")
print("3 hanya berlaku untuk yang mempunyai member!")

total_harga = int(input("Masukkan total belanjaan yang sudah dihitung "))
member = input("apakah pelanggan memiliki member(Y/N)? ")
if member.lower() == "y":
    member = True
else:
    member = False

if member and total_harga > 100000:
    promo = 10
elif total_harga > 50000:
    promo = 8
elif total_harga > 20000:
    promo = 5
else:
    promo = 0
    print("Tidak ada ketentuan diskon!")

diskon = total_harga * promo / 100
total = total_harga - diskon
print(f"total barang belanjaanmu adalah {total:,.0f}")