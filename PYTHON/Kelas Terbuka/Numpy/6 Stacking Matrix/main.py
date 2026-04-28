import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

aMath = np.zeros((2,2))
bMath = np.ones((2,2))

c = np.hstack((a,b))
d = np.vstack((a,b))

cMath = np.hstack((aMath,bMath))
dMath = np.vstack((aMath,bMath))

print("Contoh 1")
print(c)
print(d)

print("Contoh 2")
print(cMath)
print(dMath)
