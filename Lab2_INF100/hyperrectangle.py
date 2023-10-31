x1 = input("x1 = ")
y1 = input("y1 = ")
x2 = input("x2 = ")
y2 = input("y2 = ")
xp = input("xp = ")
yp = input("yp = ")

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

if xpinne == True and ypinne == True: print("inne")
else: print("ute")