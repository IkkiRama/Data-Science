# Latihan konversi satuan temperature

# program konversi satuan dari celcius ke yang lainnya

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan angka suhu dalam celcius :"))
print("Suhu adalah :", celcius, "celcius")


# Reamur
reamur = (4/5) * celcius
print("Suhu dalam temperature reamur adalah :", reamur, "reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam temperature fahrenheit adalah :", fahrenheit, "fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam temperature kelvin adalah :", kelvin, "kelvin")


print("\nPROGRAM KONVERSI TEMPERATUR FAHRENHEIT KE KELVIN\n")

fahrenheit = float(input("Masukkan angka suhu dalam fahrenheit :"))
print("Suhu adalah :", fahrenheit, "fahrenheit")


# Fahrenheit - Kelvin
kelvin = ( (5/9) * (fahrenheit - 32) ) + 273
print("Suhu dalam temperature kelvin adalah :", kelvin, "kelvin")


fahrenheit = ( (9/5) * (kelvin - 273) ) + 32 
print("Suhu dalam temperature fahrenheit adalah :", fahrenheit, "fahrenheit")