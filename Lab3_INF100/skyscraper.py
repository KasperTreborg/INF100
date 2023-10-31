from uib_inf100_graphics.simple import canvas, display

padding = 33
inner_margin = 5
n = int(input("Hvor mange etasjer skal skyskraperen ha? "))
m = int(input("Hvor mange vinduer skal det være oer etasje? "))
width_of_all_rects = (400 - 2 * padding) - (n-1) * inner_margin
width_of_one_rect = 5
window_height = 10
total_høyde = n * (window_height + 5)

for i in range(n):
    for j in range(m):
        x_venstre = padding + j * (width_of_one_rect + inner_margin)
        x_høyre = x_venstre + width_of_one_rect
        y_topp = 400 - padding - (i * (window_height + 5) + window_height)
        y_ned = 400 - padding - (i * (window_height + 5))
        canvas.create_rectangle(x_venstre, y_topp, x_høyre, y_ned)

yttre_x_left = padding - 5
yttre_x_right = padding + m * (width_of_one_rect + inner_margin)
yttre_y_top = 400 - padding - total_høyde
yttre_y_bottom = 400 - padding + 5



canvas.create_rectangle(yttre_x_left, yttre_y_top, yttre_x_right, yttre_y_bottom)

display(canvas)