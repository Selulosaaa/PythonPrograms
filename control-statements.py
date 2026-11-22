# control statement adalah instruksi yang mengatur alur atau urutan eksekusi berdasarkan kondisi tertentu

# control statement ada 3 jenis utama(yang akan dipelajari) break, continue, return.

# break adalah perintah untuk menghentikan atau mengistirahatkan program
# JIKA suatu kondisi terpenuhi dia akan langsung melompat ke program berikutnya
nama = []
for i in range(5):
    input_nama = input("input nama ")
    nama.append(input_nama)
    if nama == '':
        print("ada nama yang kosong!")
        break
print(nama)