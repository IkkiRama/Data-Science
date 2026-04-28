# Operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b   
print(a,"+",b,"=",hasil)

# operasi pengurangan -
hasil = a - b   
print(a,"-",b,"=",hasil)

# operasi perkalian *
hasil = a * b   
print(a,"*",b,"=",hasil)

# operasi pembagian /
hasil = a / b   
print(a,"/",b,"=",hasil)

# operasi eksponen(perpangkatan) **
hasil = a ** b   
print(a,"**",b,"=",hasil)

# operasi modulus(sisa bagi) %
hasil = a % b   
print(a,"%",b,"=",hasil)

# operasi floor division(dibulatkan ke bawah) //
hasil = a // b   
print(a,"//",b,"=",hasil)


# Prioritas operasi, opeational precedence
# ()
# Eksponen (**)
# Perkalian, pembagian, modulus, floor division (*, /, %, //)
# Penjumlahan & pengurangan (+, -)

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=",hasil)