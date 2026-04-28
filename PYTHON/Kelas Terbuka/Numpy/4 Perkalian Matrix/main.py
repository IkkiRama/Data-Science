import numpy as np

a = np.array(([1,2,5],
              [3,4,6]))
# a = np.array(([1,2],
#               [3,4]))

b = np.ones([3,1])
# b = np.ones([2,2])

print("Matriks a :")
print(a)
print("Matriks b :")
print(b)

c = np.dot(a,b)
d = a.dot(b)
print("Perkalian Matrik : ")
print(c)
print(d)
