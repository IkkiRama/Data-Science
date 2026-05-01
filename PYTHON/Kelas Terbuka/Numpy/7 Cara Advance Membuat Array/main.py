import numpy as np

# membuat matriks dengan tipe data tertentu
a = np.array((
    [1,2,3],
    [4,5,6]
), dtype=float )

# a = np.array((
#     [1,2,3],
#     [4,5,6]
# ), dtype=int )

# a = np.array((
#     [1,2,3],
#     [4,5,6]
# ), dtype=bool )

print(a)


# Membuat matrik dengan fuction
# b = np.fromfunction(nama fungsi, ukuran matriks, tipe datanya)

def kuadrat(baris, kolom) :
    return kolom**2;

def jumlah(baris, kolom) :
    return baris + kolom;

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (3,4), dtype = float)

print(b)
print(c)


# membuat matriks menggunakan iterasi
# x nya di kali x di setiap iterasi, jadi hasilnya adalah kuadrat dari x
iterable = (x*x for x in range(5))
iterable2 = (x+2 for x in range(5))

d = np.fromiter(iterable, dtype= int)
e = np.fromiter(iterable2, dtype= int)
print(d)
print(e)


# multitype array

dtipe = [("nama", "S255"),("umur", int), ("tinggi", float)]

data = [("Andi", 20, 170.5), ("Budi", 25, 180.2), ("Cici", 22, 165.3)]
f = np.array(data, dtype=dtipe)
print(f)

