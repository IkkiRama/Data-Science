list_range = list(range(1,10,2)) # range(start, stop, step(increment/decrement))
print(list_range)

# List pakai for
# i**2 itu di kuadratin
list_for = [i**10 for i in range(0,10)]
print(list_for)

# List Pakai For dan if
list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)

list_for_if_ganjil = [i**2 for i in range(0,10) if (i % 2)]
print(list_for_if_ganjil)

list_for_if_genap = [i**3 for i in range(0,10) if (i % 2) == 0]
print(list_for_if_genap)