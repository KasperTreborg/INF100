import decimal
from decimal import Decimal

sideA = Decimal(input("sideA = "))
sideB = Decimal(input("sideB = "))
sideC = Decimal(input("sideC = "))

if sideA + sideB == sideC or sideA + sideC == sideB or sideB + sideC == sideA:
    print("Noen vil si det er en trekant, andre vil si det bare er en strek.")

if sideA + sideB < sideC or sideA + sideC < sideB or sideB + sideC < sideA:
    print("Umulig å lage en slik trekant.")

if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA:
    print("Mulig trekant.")