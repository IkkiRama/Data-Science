data_dict = {
    "nama" : "Rifki Romadhan",
    "jurusan" : "IESP",
    "semester" : 8,
    "matkul" : ["Ekonomi Makro", "Ekonomi Mikro", "Ekonomi Moneter"]
}


for data in data_dict :
    print(data)
    # print(data_dict[data])


keys = data_dict.keys()
for key in keys :
    print(data_dict.get(key))


values = data_dict.values()
for value in values :
    print(value)

# Menghasilakn tuple
items = data_dict.items()
for item in items :
    print(item)

for (key, value) in items :
    print(f"Key = {key}, Value = {value}")