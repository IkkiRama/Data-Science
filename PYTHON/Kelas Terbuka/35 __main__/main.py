# __main__ adalah top level code environment

# __name = "__main__"
print(f"isi dari __name__ = {__name__}")
import fungsi


# Contoh penggunaan __main__ 

# deklarasi
def fungsi_tambah(a:int, b:int) -> int :
    return a + b

if __name__ == "__main__" :
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1 , angka2)
    print(f"hasil tambah = {hasil}")