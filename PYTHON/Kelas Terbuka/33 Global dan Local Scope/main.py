def contoh_local():
    x = 10  # local variable
    print("Di dalam fungsi:", x)

contoh_local()
# print(x)  ERROR (x tidak dikenal di luar fungsi)

x = 20  # global variable

def contoh_global():
    print("Di dalam fungsi:", x)

contoh_global()
print("Di luar fungsi:", x)



x = 5
def ubah_global():
    global x
    x = 100

ubah_global()
print(x)  # 100


x = 10
def test():
    x = 50  # ini local, bukan ubah global
    print("Dalam fungsi:", x)

test()
print("Luar fungsi:", x)


# Di Python, for tidak bikin scope baru
for i in range(3):
    angka = i * 2

print(i)      # 2
print(angka)  # 4



def contoh_loop():
    for i in range(3):
        hasil = i + 1
    print("Di dalam fungsi:", hasil)

contoh_loop()
# print(hasil) ERROR (karena local ke fungsi)


total = 0  # global
def tambah_loop():
    global total
    for i in range(5):
        total += i

tambah_loop()
print(total)  # 10


# Contoh yang sering bikin bingung
for i in range(3):
    pass
print(i)  # tetap ada!