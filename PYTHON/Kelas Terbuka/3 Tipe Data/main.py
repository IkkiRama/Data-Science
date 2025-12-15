# a = 10, a adalah var dengan nilai 10

# tipe data : angka satuan (integer)
data_integer = 1
print("data : ",data_integer, ", bertipe data : ", type(data_integer))

# tipe data : angka dengan koma (float) 
data_float = 10.9
print("data : ",data_float, ", bertipe data : ", type(data_float))

# tipe data : biner atau true false (boolean)
data_biner = True
print("data : ",data_biner, ", bertipe data : ", type(data_biner))



## tipe data khusus

# bilangan kompleks
data_kompleks = complex(5,6)
print("data : ",data_kompleks, ", bertipe data : ", type(data_kompleks))

# tipe data dari bahasa C
from ctypes import c_double
data_C = c_double(10.6)
print("data : ",data_C, ", bertipe data : ", type(data_C))

