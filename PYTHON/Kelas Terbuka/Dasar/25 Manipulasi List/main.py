listNama = ["Rifki", "Yudi", "Kiki"]
listNamaTambahan = ["Ikki", "Rama"]

# --- Akses Data ---
print(listNama[1])    # Output: Yudi (Index dimulai dari 0)
print(listNama[-1])   # Output: Kiki (Index -1 mengambil data paling belakang)



# Mengambil panjang karakter dari string di dalam list
panjang_data = len(listNama[0]) # "Rifki" ada 5 karakter
print(f"Panjang nama {listNama[0]}: {panjang_data}")

print("\n=== Menambah Data ===")
# Menambah data ke posisi paling akhir
listNama.append("Athar")
print(f"Setelah append: {listNama}")

# Menambah data ke index spesifik (index, "nama_data")
listNama.insert(1, "Rizki")
print(f"Setelah insert di index 1: {listNama}")

# Menggabungkan dua list menjadi satu
listNama.extend(listNamaTambahan)
print(f"Setelah extend: {listNama}")



print("\n=== Mengubah & Menghapus Data ===")
# Menghapus data berdasarkan nama (Value)
listNama.remove("Kiki")
print(f"Setelah remove 'Kiki': {listNama}")



# Mengubah data berdasarkan index
listNama[1] = "Mikel"
print(f"Index 1 diubah jadi Mikel: {listNama}")



# Menghapus data paling belakang dengan pop()
listNama.pop() # Menghapus data terakhir ("Rama")
data_terakhir = listNama.pop() # Menghapus "Ikki" dan menyimpannya di variabel
print(f"Data yang diambil lewat pop: {data_terakhir}")
print(f"List setelah pop: {listNama}")




print("\n=== Operasi Angka & Pencarian ===")
listAngka = [1,2,3,4,5,4,3,2,4,1,5,6,7,3,4,4,4,4]

# Menghitung berapa kali sebuah nilai muncul
jumlahAngka4 = listAngka.count(4)
print(f"Jumlah angka 4 muncul: {jumlahAngka4} kali")

# Mencari posisi index dari suatu data
posisiRifki = listNama.index("Rifki")
print(f"Rifki ada di index ke: {posisiRifki}")

print("\n=== Mengurutkan Data (Sorting) ===")
# Mengurutkan (Angka kecil ke besar, String sesuai abjad A-Z)
listAngka.sort()
listNama.sort()
print(f"Sort Angka: {listAngka}")
print(f"Sort Nama: {listNama}")

print("\n=== Membalik Urutan (Reverse) ===")
# Membalik urutan (bukan berdasarkan nilai, tapi posisi)
listNama.reverse()
listAngka.reverse()
print(f"Reverse Angka: {listAngka}")
print(f"Reverse Nama: {listNama}")

print("\n=== List Multidimensi ===")
# Membuat list di dalam list (seperti matriks atau tabel)
list_gabungan = [listNama, listNamaTambahan]
print(list_gabungan)

print(list_gabungan[0][1])
