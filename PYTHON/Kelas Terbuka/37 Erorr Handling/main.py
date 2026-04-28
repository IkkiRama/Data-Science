# exception akan terjadi saat program mengalami eror saat runtime

# input_user = int(input("Masukan angka : "))
# hasil = 0

# try :
#     hasil = 10/input_user
#     print(hasil)
# except :
#     print("Jangan memasukan noll")


# while(True) :
#     angka = int(input("Masukan angka : "))
#     try :
#         hasil = 10/angka
#         print(hasil)

#         isdone = input("lanjutkan y/n : ")
#         if isdone == "n" :
#             break

#     except :
#         print("Jangan memasukan noll")
#         break



# try :
#     with open("data.txt", mode="r", encoding="utf-8") as file:
#         print(file.read())
# except :
#     with open("data.txt", mode="w", encoding="utf-8") as file:
#         print("Data tidak ditemukan, membuat file baru")
#         print(file.write("COBAAA"))
    
from numbers import Number

def tambah(a,b) :
    if not isinstance(a, Number) or not isinstance(b, Number) :
        raise "Yang anda masukan bukan angka"
    return a+b

print(tambah(10,33))
print(tambah(10,22))
# print(tambah(10,"aaaa"))

angka = 0
try:
    hasil = 10/angka
except Exception as erorMessage :
    print(erorMessage)

# try:
#     hasil = 10/angka
# except ZeroDivisionError as erorMessage :
#     print(erorMessage)