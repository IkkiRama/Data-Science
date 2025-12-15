# Tuple itu ngga bisa diganti dan ngga bisa di hapus
x = (40, 41, 42)
print(x)
print(x[1])

# Kalau bikin var baru yang berisi banyak data itu otomatis jadi tuple
y = 50, 51, 52
print(y)

# tuple assignment
a, b, c = 1, 2, 4
print(c)

# Method tuple dan range
print(tuple(range(10)))

# tuple masukin ke list
tuplist = [x,y]
print(tuplist)

data = (age, years_of_school) = "10,4".split(",")
print(data)
print(age)
print(years_of_school)

nama, kelamin = "Rifki Romadhan,Laki-laki".split(",")
print(nama)
print(kelamin)

# Func can provide tuple as return value
def squareInfo (x) :
    a = x ** 2
    p = 4 ** x 
    print("Area and perimeter")
    return a,p

print(squareInfo(10))


