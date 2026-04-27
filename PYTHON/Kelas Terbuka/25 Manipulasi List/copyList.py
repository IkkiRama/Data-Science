a = ["Rifki", "Yudi", "Kiki"]
a2 = [2,3,5,6]


# b = a

# Gunakan copy supaya kalau a diubah datanya, b ngga akan berubah datanya
b = a.copy()

print(a)
print(b)

a[1] = "Athar"

print(a)
print(b)