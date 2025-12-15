# Dictionaries represent another way of storing data
# (KAYA OBJEK DALAM JAVA SCRIPT, TAPI DALAM PEMANGGILANNYA NGGA BISA PAKAI METODE DOT NOTATION)

contohDict = {"nama" : "Rifki Romadhan", "umur" : 20, "hobi":"Tidur"}
print(contohDict) 

# Cara manggil nya
print(contohDict["nama"]) 
print(contohDict.get("nama")) 

# Cara ubah value nya
contohDict["hobi"] = "Ngoding"
print(contohDict) 

# Another contoh
contohDict["semester"] = 7
contohDict["hobi"] = ["Ngoding", "Tidur", "Makan", "Makan Lagi", "Makan Terus"]
print(contohDict) 

team = {}
team["Front End"] = "Rifki"
team["Back End"] = "Ikki"
team["DevOps"] = "Rama"
team["Full Stack"] = "Romadhan"

print(team)




# Excercise UDEMY
Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna', 'meal_5':'Soup'}

Price_list = {}
Price_list["Spaghetti"] = 10
Price_list["Fries"] = 5
Price_list["Cheeseburger"] = 8
Price_list["Lasagna"] = 12
Price_list["Soup"] = 5

