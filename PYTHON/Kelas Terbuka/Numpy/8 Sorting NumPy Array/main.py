import numpy as np

a = np.floor(np.random.rand(2,3)*100)
# a = np.floor(np.random.rand(1,10)*100)

# kalau punya lebih dari 1 dimensi, maka akan diurutkan berdasarkan baris, kalau punya 1 dimensi maka akan diurutkan berdasarkan nilai
# kalau pnya lebih dari 1 dimensi, maka indexnya akan di hitung dari row 1 dari kiri ke kanan, lalu row 2 dari kiri ke kanan, dst


print(a)

# max
print("Nilai max : ", np.max(a))
print("Posisi nilai max : ", np.argmax(a))
      
# min
print("Nilai min : ", np.min(a))
print("Posisi nilai min : ", np.argmin(a))
print("Posisi nilai min : ", np.argmin(a))

# mengurutkann nilai 
print("Mengurutkan nilai : ", np.sort(a))
print("Posisi nilai : ", np.argsort(a))


dtipe = [("nama", "S255"),("umur", int), ("tinggi", float)]

data = [("Andi", 25, 170.5), ("Cici", 20, 165.3), ("Budi", 22, 180.2)]
b = np.array(data, dtype=dtipe)
print("Mengurutkan berdasarkan nama : ", np.sort(b, order="nama"))
print("Mengurutkan berdasarkan umur : ", np.sort(b, order="umur"))
print("Mengurutkan berdasarkan tinggi : ", np.sort(b, order="tinggi"))