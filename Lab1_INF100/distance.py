import math

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

x = [x1,y1]
y = [x2,y2]

distance = math.dist(x,y)

print(f"Avstanden mellom ({x1}, {y1}) og ({x2}, {y2}) er {distance}")