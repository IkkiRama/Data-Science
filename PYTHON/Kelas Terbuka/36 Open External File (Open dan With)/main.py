# Membaca file txt

file = open("data.txt",mode="r")

print(file.readable())
print(file.writable())

# print(file)
print(file.readline(), end="") # Baca line ke 1
print(file.readline(), end="") # Baca line ke 2

# Langsung baca semua
# print(file.read())
# print(file.readlines())

print(f"Apakah file sudah di close : {file.closed}")
file.close()
print(f"Apakah file sudah di close : {file.closed}")



with open("data.txt", mode="r", encoding="utf-8") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file)
    print(f"Apakah file sudah di close : {file.closed}")

print(f"Apakah file sudah di close : {file.closed}")



# dia akan membuat file baru kalau ngga ada,
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt", mode="w", encoding="utf-8") as file :
    file.write("Kimak")

with open("data_1.txt", mode="w", encoding="utf-8") as file :
    file.write("Ikki")

with open("data_1.txt", mode="w", encoding="utf-8") as file :
    file.write("Ketimpa")


# Metode append -> nambah tanpa hapus

# with open("data_2.txt", mode="a", encoding="utf-8") as file :
#     file.write("Rifki Romadhan\n")

# with open("data_2.txt", mode="a", encoding="utf-8") as file :
#     file.write("Athar Rizky\n")

# with open("data_2.txt", mode="a", encoding="utf-8") as file :
#     file.write("Nambah lagi\n")


# Metode r+ -> akan menimpa baris di atas sendiri sesuai dengan jumlah kata
with open("data_3.txt", mode="r+", encoding="utf-8") as file :
    file.write("Baris ke 1\n")
    file.write("Baris ke 2\n")

with open("data_3.txt", mode="r+", encoding="utf-8") as file :
    print(file.read())

with open("data_3.txt", mode="r+", encoding="utf-8") as file :
    file.write("Baris ke 3\n")
