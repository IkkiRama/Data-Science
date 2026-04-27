angka = 1
while (angka <= 10) :
    print("*"*angka)
    angka+=1

angka2 = 10
while (angka2 >= 1) :
    print("*"*angka2)
    angka2-=1

tinggi = 5 
baris = 1

while baris <= tinggi:
    # 1. Hitung spasi (makin ke bawah makin sedikit)
    spasi = " " * (tinggi - baris)
    
    # 2. Hitung bintang (pola ganjil: 1, 3, 5, 7, ...)
    # Rumusnya: (2 * baris) - 1
    bintang = "*" * (2 * baris - 1)
    
    # 3. Gabungkan dan print
    print(spasi + bintang)
    
    baris += 1

kotak = 5
while (kotak >= 1) :
    print("*"*10)
    kotak-=1


kotak = 5
while (kotak >= 1) :
    print("*"*20)
    kotak-=1

