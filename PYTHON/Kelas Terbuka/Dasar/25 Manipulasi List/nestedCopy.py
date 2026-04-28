from copy import deepcopy

# Data awal
list_data = [["Rifki", "Yudi"], [2, 3, 5]]

# Gunakan deepcopy untuk memutus hubungan total
list_aman = deepcopy(list_data)

# Ubah data di list asli
list_data[0][0] = "Warmad"

print("=== Hasil Deep Copy ===")
print(f"List Asli (berubah): {list_data}")
print(f"List Aman (tetap)  : {list_aman}") 
# Sekarang list_aman tetap ["Rifki", "Yudi"] karena disalin total sampai ke dalam.