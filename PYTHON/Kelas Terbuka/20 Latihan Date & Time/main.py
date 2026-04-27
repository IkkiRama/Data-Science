import datetime as dt

hari_ini = dt.date.today()

# tahun, bulan, tanggal
tanggal = dt.date(2024, 6, 20)

print(hari_ini)
print(f"hari ini adalah hari {hari_ini:%A}, tanggal {hari_ini.day}, bulan {hari_ini.month}, tahun {hari_ini.year}")
print(f"tanggal yang diinginkan adalah hari {tanggal:%A}, tanggal {tanggal.day}, bulan {tanggal.month}, tahun {tanggal.year}")



print("Silahkan masukkan tanggal lahir Anda")
tanggal = int(input("Tanggal lahir \t: "))
bulan = int(input("Bulan lahir \t: "))
tahun = int(input("Tahun lahir \t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"\nTanggal lahir Anda adalah: {tanggal_lahir}")
print(f"Hari lahir Anda adalah: {tanggal_lahir:%A}")

# Menghitung umur tahun
umur = hari_ini.year - tanggal_lahir.year

# Cek apakah sudah berulang tahun di tahun ini atau belum
# Jika bulan hari ini < bulan lahir, ATAU bulan sama tapi tanggal hari ini < tanggal lahir
if (hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day):
    umur -= 1

# Menghitung selisih bulan (opsional/tambahan)
bulan_sekarang = hari_ini.month
bulan_lahir = tanggal_lahir.month
selisih_bulan = (bulan_sekarang - bulan_lahir) % 12

print(f"Saat ini, umur kamu adalah: {umur} tahun {selisih_bulan} bulan")