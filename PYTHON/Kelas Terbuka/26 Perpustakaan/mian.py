list_buku = [
    ["Laskar Pelangi", "Andrea Hirata", 2005],
    ["Bumi Manusia", "Pramoedya Ananta Toer", 1980],
    ["Negeri 5 Menara", "Ahmad Fuadi", 2009],
    ["Pulang", "Leila S. Chudori", 2012],
    ["Cantik Itu Luka", "Eka Kurniawan", 2002]
]

def lihatBuku():
    print("===============List Koleksi Buku===============")

    nomer = 1
    for buku in list_buku :
        print(f"{nomer}. {buku[0]} | {buku[1]} | {buku[2]}")
        nomer +=1
    
    print("===============================================")

def tambahBuku():
    namaBuku = input("Masukan nama buku :")
    authorBuku = input("Masukan pengarang buku :")
    yearBuku = input("Masukan tahun terbit buku :")

    list_buku.append([namaBuku,authorBuku,yearBuku])
    print("Buku berhasil di tambahkan!!")
    lihatBuku()

def ubahBuku():
    lihatBuku()
    indexBuku = int(input("Masukan nomer buku yang mau di edit : "))

    if type(indexBuku) != int: print("Maaf yang anda masukan bukan nomer buku")

    namaBuku = input("Masukan nama buku :")
    authorBuku = input("Masukan pengarang buku :")
    yearBuku = input("Masukan tahun terbit buku :")

    list_buku[indexBuku+1][0] = namaBuku
    list_buku[indexBuku+1][1] = authorBuku
    list_buku[indexBuku+1][2] = yearBuku

    print("Buku berhasil di ubah!!")
    lihatBuku()

def hapusBuku():
    lihatBuku()
    indexBuku = int(input("Masukan nomer buku yang mau di ubah : "))

    if type(indexBuku) != int: print("Maaf yang anda masukan bukan nomer buku")

    list_buku.remove(list_buku[indexBuku+1])

    print("Buku berhasil di hapus!!")
    lihatBuku()

printMenu = """Silahkan pilih menu :
1. Lihat Koleksi Buku 
2. Menambah Koleksi Buku 
3. Ubah Koleksi Buku 
4. Hapus Buku dalam Koleksi 
5. Keluar program \n
note : cukup inputkan angka saja !!!
"""


def menu():
    
    while True:
        print("===============PERPUSTAKAAN RIFKI ROMADHAN===============")
        print(printMenu)

        pilih = input("\nJawaban Anda : ")
        
        if pilih == "1": lihatBuku()
        elif pilih == "2": tambahBuku()
        elif pilih == "3": ubahBuku()
        elif pilih == "4": hapusBuku()
        elif pilih == "5":
            print("Terima kasih!")
            break # Ini untuk menghentikan loop dan keluar program
        else:
            print("Maaf, input salah.")
            
        # Tanya setelah fitur selesai dijalankan
        lanjut = input("Mau lanjut pakai fitur lain? (y/n): ")
        if lanjut.lower() == "n":
            print("Sampai jumpa!")
            break

menu()