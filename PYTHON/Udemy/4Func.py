def simple() :
    print("cek")

simple()

def plusTen(x) :
    return print(x + 10)

plusTen(10)

def plus_ten (x) :
    result = x + 10
    print("Output")
    return result

print(plus_ten(2))
print(plus_ten(9))


def wage (hours) :
    return hours * 25

def with_bonus (hours) :
    return wage(hours) + 50

print(wage(8))
print(with_bonus(8))


def tabungan(uang) :
    if(uang >= 1000):
        return uang + 10
    elif(uang >= 100 | uang < 1000) :
        return uang
    else :
        return "Save More!"

print(tabungan(1000))
print(tabungan(100))
print(tabungan(99))

def substract_bc (a,b,c) :
    result = a - b * c
    return result

print(substract_bc(100,20,3))


def distance_from_zero(x):

    if type(x) in (int, float, complex):

        return abs(x)

    else:

        print('Not possible')

        return

distance_from_zero(-10)
distance_from_zero("cat")