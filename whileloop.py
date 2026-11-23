# while loop adalah loop yang bekerja ketika suatu kondisi True
# untuk mengehentikannya harus ada kondisi yang menjadikannya False
# While loops bekerja selamanya sampai ada kondisi False

nama= input("input nama mu ")

while nama == "":
    print("input nama mu!")
    nama= input("input nama mu ")
print(f"{nama}") # kondisi yang melepaska while loop

