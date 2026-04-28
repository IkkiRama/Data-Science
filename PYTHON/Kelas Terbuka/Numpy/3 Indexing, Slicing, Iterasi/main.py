import numpy as np

a = np.arange(10)**2

print(a)

print(f"Element ke 1 itu {a[0]}")
print(f"Element ke 7 itu {a[6]}")
print(f"Element ke akhir itu {a[-1]}")

# Slicing
print(f"Element dari 1-6 {a[0:7]}") #eksklusif [start, end)
print(f"Element dari 4-akhir {a[3:]}") 
print(f"Element dari awal-6 {a[:7]}") 

# Iterasi
for i in a :
    print(f"Value = {i}")
