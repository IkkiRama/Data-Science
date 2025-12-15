# Operasi bitwise atau operasi biner

a = 9
b = 5

# bitwise or(|)
c = a | b
print("===OR===")
print("nilai a = ", a, "binary = ", format(a, "08b"))
print("nilai b = ", b, "binary = ", format(b, "08b"))
print("-----------------------------------------------(|)")
print("nilai c = ", c, "binary = ", format(c, "08b"))


# bitwise and(&)
c = a & b
print("===AND===")
print("nilai a = ", a, "binary = ", format(a, "08b"))
print("nilai b = ", b, "binary = ", format(b, "08b"))
print("-----------------------------------------------(&)")
print("nilai c = ", c, "binary = ", format(c, "08b"))


# bitwise XOR(^)
c = a ^ b
print("===XOR===")
print("nilai a = ", a, "binary = ", format(a, "08b"))
print("nilai b = ", b, "binary = ", format(b, "08b"))
print("-----------------------------------------------(^)")
print("nilai c = ", c, "binary = ", format(c, "08b"))


# bitwise NOT(~)
c = ~ a
print("===NOT===")
print("nilai a = ", a, "binary = ", format(a, "08b"))
print("-----------------------------------------------(~)")
print("nilai c = ", c, "binary = ", format(c, "08b"))
print("-----------------------------------------------(^)")
d = 0b00001001
e = 0b11111111
print("nilai = ", d^e, "binary = ", format(d^e, "08b"))



# Shifting

# Shift right (>>)
c = a >> 1
print("===Shift right===")
print("nilai a = ", a, "binary = ", format(a, "08b"))
print("-----------------------------------------------(>>)")
print("nilai c = ", c, "binary = ", format(c, "08b"))


# Shift left (<<)
c = a << 1
print("===Shift left===")
print("nilai a = ", a, "binary = ", format(a, "08b"))
print("-----------------------------------------------(<<)")
print("nilai c = ", c, "binary = ", format(c, "08b"))