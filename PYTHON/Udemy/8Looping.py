# For Loops

data = [1,2,3,4,5,6,7,8,9,10]

for n in data :
    print(n, end = " ")

for n in data :
    print(n)

for n in range(10) :
    print(2 ** n, end = " ")

print("\n")

for n in range(30) :
    if n % 2 == 0 :
        print(n, end = " ")
    else :
        print("Odd", end = " ")

print("\n")

x = [4,5,6]
for item in range(len(x)):
    print(x[item], end = " ")



# While loop
print("\n")
x = 0
while x <= 20 :
    print(x, end = " ")
    # x = x + 1
    x += 1



nums = [1,35,12,24,31,51,70,100]

def count (numbers) :
    total = 0
    for number in numbers :
        if number <= 20 :
            total += 1
    return total

print(count(nums))


# loop with dictionary(OBJEK)
price = {
    "spageti" : 4,
    "lasagna" : 5,
    "hamburger" : 2
}

quantity = {
    "spageti" : 6,
    "lasagna" : 10,
    "hamburger" : 15
}

money_spend = 0

for idx, (key, value) in enumerate(price.items()):
    print(idx, key, value)


for i in price :
    money_spend += price[i] * quantity[i]
    print(money_spend)