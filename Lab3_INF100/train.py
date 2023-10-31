from uib_inf100_graphics.simple import canvas, display



padding = 33
inner_margin = 5
n = int(input("Hvor mange vinduer skal toget ha? "))
width_of_all_rects = (400 - 2 * padding) - (n-1) * inner_margin
width_of_one_rect = 5

for i in range(n):
    x_left = padding + i * (width_of_one_rect + inner_margin)
    x_right = x_left + width_of_one_rect
    canvas.create_rectangle(x_left, 380, x_right, 400 - padding)

x_left = padding + n * (width_of_one_rect + inner_margin)
x_right = x_left + width_of_one_rect

canvas.create_rectangle(28, 385, x_right-5, 395 - padding)

display(canvas)