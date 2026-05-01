import numpy as np

A = np.array([(2,3), (1,2)])
Y = np.array([23,14])

print(A)
print(Y)

A_inv = np.linalg.inv(A)

# Menggunakan invers matriks untuk menyelesaikan persamaan linear
X1 = A_inv.dot(Y)
print(X1)

# Menggunakan fungsi solve untuk menyelesaikan persamaan linear
X2 = np.linalg.solve(A, Y)
