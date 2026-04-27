data_dict = {
    "nama" : "Rifki Romadhan",
    "jurusan" : "IESP",
    "semester" : 8,
    "matkul" : ["Ekonomi Makro", "Ekonomi Mikro", "Ekonomi Moneter"]
}


data_dict2 = data_dict.copy()

print(data_dict)
print(data_dict2)
data_dict2.update({"jurusan" : "Manajemen"})
print(data_dict)
print(data_dict2)

# Pop Dictionary (berdasarkan key) sekaligus menghapus dari dict
jurusan = data_dict2.pop("jurusan")
print(f"Data jurusan : {jurusan}")
print(data_dict2)

# Pop items (mengambil data paling terakhir) sekaligus menghapus dari dict

matkul = data_dict2.popitem()
print(f"Data matkul : {matkul}")
print(data_dict2)

