# Fungsi dengan return dan default parameter
def hitung_total(harga, jumlah=1, diskon=0):
    total = harga * jumlah
    total_setelah_diskon = total - (total * diskon)
    return total_setelah_diskon


# Pemakaian
print(hitung_total(10000))                 # pakai default jumlah=1, diskon=0
print(hitung_total(10000, 3))              # jumlah=3, diskon=0
print(hitung_total(10000, 3, 0.1))        # jumlah=3, diskon=10%


# Type Hints
def sapa(nama: str, umur: int = 18) -> str:
    return f"Halo {nama}, umur kamu {umur} tahun."

print(sapa("Ikki"))
print(sapa(21, "Ikki"))

def sapa2(nama: str) -> str:
    return f"Halo {nama}."

print(sapa2("Ikki"))
print(sapa2(3))


# Fungsi dengan *args
def jumlahkan_semua(*angka: float) -> float:
    total: float = 0
    for a in angka:
        total += a
    return total

# Pemakaian
print(jumlahkan_semua(1, 2, 3))          # 6
print(jumlahkan_semua(10, 20, 30, 40))   # 100
print(jumlahkan_semua())                 # 0
# print(jumlahkan_semua("AKU"))            # eror



# Fungsi dengan **kwargs
def tampilkan_data(**data: str) -> None:
    for key, value in data.items():
        print(f"{key} = {value}")

# Pemakaian
tampilkan_data(nama="Ikki", jurusan="IESP", kampus="ABC")




# Fungsi gabungan *args dan **kwargs
def proses_data(*args: int, **kwargs: str) -> None:
    print("Args (tuple):")
    for i, value in enumerate(args, start=1):
        print(f"Arg {i}: {value}")
    
    print("\nKwargs (dict):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Pemakaian
proses_data(10, 20, 30, nama="Ikki", jurusan="IESP")