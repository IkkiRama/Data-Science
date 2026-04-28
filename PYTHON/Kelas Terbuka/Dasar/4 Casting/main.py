# merubah tipe data satu ke tipe data lainnya
# tipe data : int, float, str, bool

data_int = 9
print("data : ",data_int, ", bertipe data : ", type(data_int))

data_string = str(data_int)
print("data : ",data_string, ", bertipe data : ", type(data_string))

data_float = float(data_int)
print("data : ",data_float, ", bertipe data : ", type(data_float))

data_bool = bool(data_int)
print("data : ",data_bool, ", bertipe data : ", type(data_bool))

data_bool1 = bool(0)
print("data : ",data_bool1, ", bertipe data : ", type(data_bool1))

data_bool2 = bool(-1)
print("data : ",data_bool2, ", bertipe data : ", type(data_bool2))
