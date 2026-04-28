# angka = 100
# while ( angka >= 0 ) :
#     print(angka)
#     angka-=1


angka = 0
while angka < 5:
    angka+=1
    print(f"angka sekarang : {angka}")
    
    if angka == 3 : 
        pass # ini tidak akan dieksekusi

    if angka == 4 :
        break

    if angka == 2 :
        print("Ollaaa")
        continue # perintah di bawah nya tidak akan di eksekusi

    print("allo")