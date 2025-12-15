# a = 10, a adalah variabel dengan nilai 10

# tipe data : Angka satuan yang gak ada komanya(integer)
data_integer = 11
print("Data : ", data_integer, ", bertipe : ", type(data_integer))


# tipe data : Angka satuan yang ada komanya(float)
data_float = 1.5
print("Data : ", data_float, ", bertipe : ", type(data_float))

# tipe data : Kumpulan karakter (string)
data_string = "Rifki Romadhan"
print("Data : ", data_string, ", bertipe : ", type(data_string))

# tipe data : Biner true/false (boolean)
data_bool = True
print("Data : ", data_bool, ", bertipe : ", type(data_bool))


## Tipe data khusus

# Bilangan komplek
data_complex = complex(10,6)
print("Data : ", data_complex, ", bertipe : ", type(data_complex))


# Tipe data dari bahasa C
from ctypes import c_double, c_long

data_c_bouble = c_double(100)
print("Data : ", data_c_bouble, ", bertipe : ", type(data_c_bouble))


data_c_long = c_long(10000000)
print("Data : ", data_c_long, ", bertipe : ", type(data_c_long))