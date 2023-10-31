def draw_belgian_flag(canvas, x1,y1,x2,y2):
    width = x2 - x1
    height = y2 - y1
    color_length = width/3

    canvas.create_rectangle(x1,y1+height,x1+color_length,y1, fill="black")
    canvas.create_rectangle(x1+color_length, y1+height, x1+(color_length*2), y1, fill="yellow")
    canvas.create_rectangle(x1+(color_length*2), y1+height, x1+(color_length*3), y1, fill="red")