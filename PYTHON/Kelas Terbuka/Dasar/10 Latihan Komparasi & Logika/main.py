# Latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++++3--------------10+++++++

inputUser = int(input("Masukkan angka >3 & <10: "))

# Memeriksa angka kurang dari 3
isKurangDari = inputUser < 3

# Memeriksa angka lebih dari 10
isLebihDari = inputUser > 10

# Cek apakah angka yang dimasukkan >3 & <10
hasil = isKurangDari and isLebihDari
print(hasil)
