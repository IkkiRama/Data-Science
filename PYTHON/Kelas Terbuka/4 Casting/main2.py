# Casting -> merubah dari satu tipe data ke tipe data yang lain
from ctypes import c_double, c_long, c_char


## Int to every data type
print("====INTEGER====")

data_int = 10
print("Data : ", data_int, ", tipe data : ", type(data_int))


data_float = float(data_int)
print("Data : ", data_float, ", tipe data : ", type(data_float))

data_str = str(data_int)
print("Data : ", data_str, ", tipe data : ", type(data_str))

data_bool = bool(data_int) # akan false jika int = 0
print("Data : ", data_bool, ", tipe data : ", type(data_bool))


data_c_double = c_double(data_int)
print("Data : ", data_c_double, ", tipe data : ", type(data_c_double))



## Float to every data type
print("====FLOAT====")

data_float = 10.5
print("Data : ", data_float, ", tipe data : ", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
print("Data : ", data_int, ", tipe data : ", type(data_int))

data_str = str(data_float)
print("Data : ", data_str, ", tipe data : ", type(data_str))

data_bool = bool(data_float) # akan false jika int = 0
print("Data : ", data_bool, ", tipe data : ", type(data_bool))

data_c_double = c_double(data_float)
print("Data : ", data_c_double, ", tipe data : ", type(data_c_double))


## Boolean
print("====BOOLEAN====")

data_bool = True
print("Data : ", data_bool, ", tipe data : ", type(data_bool))

data_int = int(data_bool) # akan dibulatkan ke bawah
print("Data : ", data_int, ", tipe data : ", type(data_int))

data_str = str(data_bool)
print("Data : ", data_str, ", tipe data : ", type(data_str))

data_float = float(data_bool) # akan false jika int = 0
print("Data : ", data_float, ", tipe data : ", type(data_float))

data_c_double = c_double(data_bool)
print("Data : ", data_c_double, ", tipe data : ", type(data_c_double))


# Stirng akan false ketika dikasih petik kosong ("")
# Tidak bisa mengubah int ke str (akan eror kalau dijalankan)
# nama = "Rifki Romadhan"
# change_nama = int(nama)
# print("Data : ", change_nama, ", tipe data : ", type(change_nama))
