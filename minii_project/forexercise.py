for i in range(5):
    print(f"*" * (i+1))

for k in range(10):
    nilai = 7 * (k+1)
    print(f"7 x {k+1} = {nilai}")

list = []
skor = 0

for j in range(5):
    skors = int(input(f"input nilai untuk orang ke {j+1} orang "))
    list.append(skors)
    skor += skors
    print(f"nilai untuk orang ke {j+1} adalah {skors}")
print(f"nilai keseluruhan tercatat {list}")
print(f"total keseluruhan adalah {skor}")