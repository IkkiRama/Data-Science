# Template awal
data_dict = {
    "nama": "Rifki Romadhan",
    "jurusan": "IESP",
    "semester": 8,
    "matkul": ["Ekonomi Makro", "Ekonomi Mikro", "Ekonomi Moneter"],
}

# Buat dict kosong dari keys
new_dict = dict.fromkeys(data_dict.keys())

# Input per key
for key in new_dict:
    if key == "matkul":
        matkul_list = []
        jumlah = int(input("Masukkan jumlah matkul: "))
        for i in range(jumlah):
            matkul = input(f"Matkul ke-{i+1}: ")
            matkul_list.append(matkul)
        new_dict[key] = matkul_list

    elif key == "semester":
        new_dict[key] = int(input(f"Masukkan {key}: "))

    else:
        new_dict[key] = input(f"Masukkan {key}: ")

# Output
print("\nHasil dictionary:")
print(new_dict)