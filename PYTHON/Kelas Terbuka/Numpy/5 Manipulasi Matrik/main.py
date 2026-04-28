import numpy as np

a = np.array((
    [1,2,3],
    [4,5,6]
))

print(f"Matriks a dengan ukuran : {a.shape}")
print(a)

# transpose matriks
# matrik A ngga berubah, meskipun sudah di transpose 
print("Transpose matriks dari a : ")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flatten array, vector baris
print("Flatten matriks a : ")
print(a.ravel())
print(np.ravel(a))

# reshape
print("Reshape matriks a : ")
print(a.reshape(3,2))

# Resize
# akan mengubah matriks a
print("Resize matriks a : ")
a.resize(3,2)
print(a)
