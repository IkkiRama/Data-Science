import numpy as np

a = [1,2,3,4,5]
b = [6,7,8,9,10]

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ELEMENTwise operation !== operasi matrik

print(a + b)
print(anp + bnp)

# print(a - b)
print(anp - bnp)

# print(a / b)
print(anp / bnp)

# print(a * b)
print(anp * bnp)

# print(a**2)
print(anp**2)



# Multidimensi array
c = np.array([(1,2,3), (4,5,6)])
d = np.array([(7,8,9), (-1,-2,-3)])

print(c + d)
print(c - d)
print(c / d)
print(c * d)
print(c**2)
