def draw_multicolored_flag(canvas, x1, y1, x2, y2, colors):
    width = x2 - x1
    color_length = width/len(colors)

    for i in range(len(colors)):

        rect_x1 = x1 + (color_length * i)
        rect_x2 = x1 + (color_length * (i + 1))
        canvas.create_rectangle(rect_x1, y1, rect_x2, y2, fill=colors[i], outline="")