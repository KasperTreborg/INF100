def draw_grid(canvas, x1, y1, x2, y2, colors):

    num_rows = len(colors)
    num_cols = len(colors[0]) if num_rows > 0 else 0


    cell_width = (x2 - x1) / num_cols
    cell_heigth = (y2 - y1) / num_rows

    for row in range(num_rows):
        for col in range(num_cols):
            color = colors[row][col]

            rect_x1 = x1 + col * cell_width
            rect_y1 = y1 + row * cell_heigth
            rect_x2 = rect_x1 + cell_width
            rect_y2 = rect_y1 + cell_heigth

            canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill=color)