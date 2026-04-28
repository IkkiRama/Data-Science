# Operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# Lebih besar dari (>)
print("===Lebih besar dari (>)===")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# Kurang besar dari (<)
print("===Kurang besar dari (<)===")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih besar dari sama dengan (>=)
print("===Lebih besar dari sama dengan (>=)===")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# Kurang besar dari sama dengan (<=)
print("===Kurang besar dari sama dengan (<=)===")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)


# Sama dengan(==)
print("===Sama dengan (==)===")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = a == "4"
print(a,"== string",4,"=",hasil)
hasil = b == "4"
print(b,"==",4,"=",hasil)

# Tidak sama dengan(!=)
print("===Tidak sama dengan (!=)===")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = a != "4"
print(a,"!= string",4,"=",hasil)
hasil = b != "4"
print(b,"!=",4,"=",hasil)


# is sebagai komparasi object identity
print("===is sebagai komparasi object identity===")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x = ",x,"id = ", hex(id(x)))
print("nilai y = ",y,"id = ", hex(id(y)))
hasil = x is y
print(x,"is",y,"=",hasil)


# is not sebagai komparasi object identity
print("===is not sebagai komparasi object identity===")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x = ",x,"id = ", hex(id(x)))
print("nilai y = ",y,"id = ", hex(id(y)))
hasil = x is not y
print(x,"is not",y,"=",hasil)