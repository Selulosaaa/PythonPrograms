# pada sebuah hari kerja, satu orang bekerja setiap hari namun dia akan libur pada weekend.

hari = ['senin','selasa', 'rabu', 'kamis', 'jumat']
weekend = ['sabtu', 'minggu']
for kerja in hari:
    if kerja == weekend:
        continue
    print(f"hari kerja: {kerja}")