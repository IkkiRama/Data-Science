peserta = ["Rifki", "Kiki", "Ikki", "Rama"]

print(peserta[0])
print(peserta[-1])
print(peserta[-2])

peserta[3] = "Yudi"
print(peserta)

del peserta[3]
print(peserta)


peserta.append(4)
print(peserta)

peserta.insert(1, 99)  # tambah 99 di indeks ke-1
print(peserta)

peserta.extend([4, 5, 6])
print("Extend")
print(peserta)

print(len(peserta))
print(len(peserta[0]))

# len hanya untuk string
# print(len(peserta[1]))


a = [1, 2]
b = [3, 4]
c = a + b
print(c)  # [1, 2, 3, 4]

angka = [1, 2]
angka = angka * 3
print(angka)  # [1, 2, 1, 2, 1, 2]


# SLICE LIST
angka = [10, 20, 30, 40, 50, 60]

print(angka[1:4])    # [20, 30, 40]   → ambil dari indeks 1 sampai sebelum 4
print(angka[:3])     # [10, 20, 30]   → dari awal sampai sebelum indeks 3
print(angka[3:])     # [40, 50, 60]   → dari indeks 3 sampai akhir
print(angka[::2])    # [10, 30, 50]   → ambil dengan step 2
print(angka[::-1])   # [60, 50, 40, 30, 20, 10] → list dibalik

teks = "Python"

print(teks[0:3])   # 'Pyt'
print(teks[:4])    # 'Pyth'
print(teks[2:])    # 'thon'
print(teks[::-1])  # 'nohtyP'


peserta = ["Rifki", "Kiki", "Ikki", "Rama"]
print(peserta.index("Ikki"))

print(peserta)
peserta.sort()
print(peserta)
peserta.sort(reverse=True)
print(peserta)

print(angka)
angka.sort()
print(angka)
angka.sort(reverse=True)
print(angka)

newPeserta = ["Yudi", "Athar", "Yudistira"]

biggerList = [newPeserta, peserta]
print(biggerList)
biggerList.sort()
print(biggerList)
biggerList.sort(reverse=True)
print(biggerList)


# List with range
# range(start, stop, step)

print(list(range(10)))
print(tuple(range(10)))

print(list(range(3,7)))
print(list(range(3,7,2)))