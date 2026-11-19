# if else adalah sebuah command kondisi di polython
# if adalah jika, jika itu benar maka true, jika salah maka false

suhu = 25
if suhu >= 28:
    print("panas cok?") # suhu lebih dari 28, maka dia true dan akan print
elif suhu <= 28: # elif digunakan jika ada lebih dari satu kondisi
    print("normal deh")
else: # kondisi yangg tidak ada di atas
    print("dingin")
    print("brrrrrr") # error betew gw

# jika ingin membandingkan dari input string maka
input = input("masukkan antara dua kata (iya/tidak) ")

if input.lower() == "iya": # lower memaksa hasil input menjadi huruf kecil semua
    print("ya kamu boleh masuk")
elif input.lower() == "tidak":
    print("keluar aja")
else:
    print("input tidak valid")