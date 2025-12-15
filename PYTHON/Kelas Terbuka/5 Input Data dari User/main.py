# Input User

# Data yang dimasukkan pasti string
data = input("Masukkan data : ")
print("Data : ", data, ", tipe : ", type(data))

# Jika ingin mengambil int
angka = int(input("Masukkan angka : "))
angka = float(input("Masukkan angka : "))
print("Data : ", angka, ", tipe : ", type(angka))


# Boolean
biner = bool(int(input("Masukkan nilai boolean : ")))
print("Data : ", biner, ", tipe : ", type(biner))