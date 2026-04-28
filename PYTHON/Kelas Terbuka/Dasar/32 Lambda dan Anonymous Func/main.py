# lambda parameter: ekspresi

tambah = lambda a, b: a + b

print(tambah(3, 5))  # 8


# MAP
angka = [1, 2, 3, 4]

hasil = list(map(lambda x: x * 2, angka))
print(hasil)  # [2, 4, 6, 8]


# SORTING
data = [("Ikki", 21), ("Budi", 19), ("Andi", 23)]

# Sort berdasarkan umur
data_sorted = sorted(data, key=lambda x: x[1])

print(data_sorted)


# FILTER
angka = [1, 2, 3, 4, 5, 6, 7, 8]

genap = list(filter(lambda x: x % 2 == 0, angka))

print(genap)  # [2, 4, 6, 8]



# Anonym Func
def pangkat(n) :
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"Pangkat 2 dari 5 : {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"Pangkat 3 dari 5 : {pangkat3(5)}")

print(f"Pangkat bebas : {pangkat(2)(5)}")