print("================SELAMAT DATANG DI PROGRAM KALKULATOR================")
angka_satu = int(input("Masukan angka ke 1 \t:"))
operator = str(input("Masukan operator (+,-,*,:) \t:"))
angka_dua = int(input("Masukan angka ke 2 \t:"))
hasil = 0

if(operator == "+") :
    hasil = angka_satu + angka_dua
elif (operator == "-") :
    hasil = angka_satu - angka_dua
elif (operator == "*") :
    hasil = angka_satu * angka_dua
elif (operator == "/") :
    hasil = angka_satu / angka_dua
else :
    print("Anda salah memasukan operator")

if hasil!=0 : print(f"Hasil dari perhitungan : {hasil}")