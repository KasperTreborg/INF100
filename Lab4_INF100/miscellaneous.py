from math import isclose
from math import sqrt

def multiply_5_minus_pi(my_number):
    return (my_number*5) - 3.14

def shout(text):
    return text + "!"

def name_age(name, gender, age):
    return f'{name} er {gender} og er {age} år gammel.'

def kinetic_energy(m, v):
    return 0.5*m*v**2

def count_letters(s,t):
    total = 0
    for i in s:
        for j in t:
            if (i == j): 
                total += 1
                break
    return total

def distance(x1,y1,x2,y2):
    return sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

def point_in_rectangle(x1,y1,x2,y2,xp,yp):
    xpinne = False
    ypinne = False

    if x1 > x2:
        if xp >= x2 and xp <= x1: xpinne = True
    else:
        if xp <= x2 and xp >= x1: xpinne = True

    if y1 > y2:
        if yp >= y2 and yp <= y1: ypinne = True
    else:
        if yp <= y2 and yp >= y1: ypinne = True

    if xpinne == True and ypinne == True: return True
    else: return False

print("Tester multiply_5_minus__pi... ", end="")
assert isclose(1.86, multiply_5_minus_pi(1))
assert isclose(56.86, multiply_5_minus_pi(12))
assert isclose(611.86, multiply_5_minus_pi(123))
print("OK")

print("Tester shout... ", end="")
assert "I love programming!" == shout("I love programming") 
assert "Adventure awaits!" == shout("Adventure awaits") 
assert "Ikke print noe!" == shout("Ikke print noe") 
print("OK")

print("Tester name_age... ", end="")
assert "Alex er kvinne og er 7 år gammel." == name_age("Alex", "kvinne", 7) 
assert "Sam er mann og er 20 år gammel." == name_age("Sam", "mann", 20) 
print("OK")

from math import isclose
print("Tester kinetic_energy... ", end="")
assert isclose(4.0, kinetic_energy(2,2))
assert isclose(128.0, kinetic_energy(4,8))
assert isclose(2.5, kinetic_energy(5,1))
print("OK")

print("Tester count_letters... ", end="")
assert  8 == count_letters("Ouagadougou", "aeiouAEIOU")
assert  0 == count_letters("hei", "x")
assert  1 == count_letters("hei", "h")
assert  2 == count_letters("heihei", "h")
assert  4 == count_letters("heihei", "ei")
assert  1 == count_letters("hei", "hhh")
print("OK")

from math import isclose
print("Tester distance... ", end="")
assert isclose(1.414213562373, distance(0, 0, 1, 1))
print("OK")

print("Tester point_in_rectangle... ", end="")
assert point_in_rectangle(0, 0, 5, 5, 3, 3)  # Midt i
assert point_in_rectangle(0, 5, 5, 0, 5, 3) # På kanten
assert not point_in_rectangle(0, 0, 5, 5, 6, 3)  # Utenfor
print("OK")