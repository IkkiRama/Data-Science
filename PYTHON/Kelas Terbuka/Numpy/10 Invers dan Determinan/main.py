import numpy as np

a = np.array([(1,-1), (1,1)])
print(a)

# invers matriks
a_inv = np.linalg.inv(a)
print(a_inv)

# determinan matriks
a_det = np.linalg.det(a)
print(a_det)
a_det_inv = np.linalg.det(a_inv)
print(a_det_inv)
