from uib_inf100_graphics.simple import canvas, display

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

width = x2 - x1
print(f'Flag width is {width}')

height = y2 - y1
print(f'Flag height is {height}')

color_length = width/3

print(f'Black stripe starts at x = {x1} and ends at x = {x1 + color_length}')
print(f'Yellow stripe starts at x = {x1 + color_length} and ends at x = {x1 + (color_length*2)}')
print(f'Red stripe starts at x = {x1 + color_length*2} and ends at x = {x1 + color_length*3}')

def createFlag(x1,y1,x2,y2):
    canvas.create_rectangle(x1,x1+height,x1+color_length,x1, fill="black")
    canvas.create_rectangle(x1+color_length, x1+height, x1+(color_length*2), x1, fill="yellow")
    canvas.create_rectangle(x1+(color_length*2), x1+height, x1+(color_length*3), x1, fill="red")

    display(canvas)

createFlag(x1,y1,x2,y2)