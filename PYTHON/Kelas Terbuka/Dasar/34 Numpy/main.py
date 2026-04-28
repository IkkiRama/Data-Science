import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"List a = {list_a}")
print(f"Vector a = {vector_a}")

# Vector bisa di tambah, kurang, bagi, kali. Sementara list ngga bisa
kuadrat = vector_a**2
kali3 = vector_a*3

print(kuadrat)
print(kali3)

matrikZero = np.zeros((2,2))
matrikSatu = np.ones((2,2))
matrikIdentitas = np.identity(4)

print(matrikZero)
print(matrikSatu)
print(matrikIdentitas)

matrik_b = np.array([(1,2) , (3,4)])
print(matrik_b)

jumlah = matrik_b + matrik_b**2 + matrikSatu
print(jumlah)