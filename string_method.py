# STRING METHODS adalah fungsi bawaan yang merlekat pada tipe data sttring(teks)
# Dalam bahasa pemrograman ini untuk memanipulasi, memeriksa, atau memproses teks

# capitalize() --> untuk mengubah huruf pertama pada suatu kata menjadi huruf kapital
teks = str("hELlo") # --> h awalnya merupakan huruf non kapital
print(teks.capitalize())

# casfolds() --> untuk mengubah teks menjadi huruf non kapital
print(teks.casefold())

# center(number, 'element lain yang ingin ditambahkan di antara teks') --> untuk membuat display teks pada terminal menjdi ke tengah
print(teks.center(30, "."))

teks_2 = str("hallo_hallo_hallo")
# count() --> untuk menghitung jumlah huruf pada string
print(teks_2.count("ll")) # jumlahnya ada 3 "ll"


