import pandas as pd
import numpy as np
import random
from data import nama_list, gender_list, matkul_list, jurusan_list

np.random.seed(42)



data = []

for i in range(550):
    nama = random.choice(nama_list)
    umur = np.random.choice([18, 19, 20, 21, 22, None])  # ada missing
    gender = random.choice(gender_list)
    matkul = random.choice(matkul_list)
    sks = np.random.choice([2, 3, 4])
    
    # nilai dengan outlier
    nilai = np.random.choice(list(range(50, 100)) + [999])
    
    semester = np.random.choice([1,2,3,4,5,6,7,8])
    jurusan = random.choice(jurusan_list)
    
    ipk = round(np.random.uniform(2.0, 4.0), 2)
    
    status_lulus = np.random.choice(["Lulus", "Tidak"])
    
    data.append([
        nama, umur, gender, matkul, sks, nilai,
        semester, jurusan, ipk, status_lulus
    ])

df = pd.DataFrame(data, columns=[
    "nama", "umur", "gender", "matkul", "sks",
    "nilai", "semester", "jurusan", "ipk", "status_lulus"
])

# duplikat data (biar belajar drop duplicates)
df = pd.concat([df, df.sample(5)], ignore_index=True)

# simpan ke CSV
df.to_csv("data_mahasiswa.csv", index=False)

print(df.head())
print("\nDataset berhasil dibuat dengan", len(df), "rows")