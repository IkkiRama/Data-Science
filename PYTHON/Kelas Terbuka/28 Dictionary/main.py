# Dictionary (Dict) -> assosiative array (mirip objek dalam JS)
# aksesnya pakai indentifier (key)

data_dict = {
    "nama" : "Rifki Romadhan",
    "jurusan" : "IESP",
    "semester" : 8,
    "matkul" : ["Ekonomi Makro", "Ekonomi Mikro", "Ekonomi Moneter"]
}
print(data_dict['nama'])
print(data_dict['jurusan'])
print(data_dict['semester'])
print(data_dict['matkul'])

print(data_dict.get("jurusan"))

# Ubah data
data_dict["jurusan"] = "Manajemen"
print(data_dict)
data_dict["fakultas"] = "Ekonomi dan Bisnis"

# Update bisa untuk ubah data
# apabila key nya ngga ada maka akan secara otomatis menambahkan data ke objeknya
data_dict.update({"jurusan" : "IESP"})
data_dict.update({"lulus" : True})
print(data_dict)

# delete data
del data_dict["fakultas"]
print(data_dict)