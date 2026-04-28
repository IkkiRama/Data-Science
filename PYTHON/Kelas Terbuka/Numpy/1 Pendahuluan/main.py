import numpy as np

# Membuat vector
a = np.array([1,2,3,4,5])
b = np.array([6.5,7.3,8.9,9,10])


# Membuat vector pakai range
c = np.arange(1,10,2) # start, stop, step

# membuat linear space (linscape)
# akan menampilkan 4 angka dan membagi antara 1-10 menjadi 4 bagian sama besar
d = np.linspace(1,10,4)

# Array multidimensi / matrik
e = np.array([ (1,2,3), (4,5,6), (7,8,9) ])

f = np.zeros((3,2))
g = np.zeros(3)

h = np.ones((3,2))
i = np.ones(2)

j = np.identity(3)
# k = np.identity((3,4))
k = np.eye(3)

print(a)
print(b)
print(c)
print(d)
print(e)
print(e+1)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)


