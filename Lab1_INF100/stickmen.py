from uib_inf100_graphics.simple import canvas, display

canvas.create_oval(60, 80, 140, 160)   # Head
canvas.create_line(100, 160, 100, 280) # Body
canvas.create_line(50, 180, 150, 180)  # Arms
canvas.create_line(100, 280, 50, 330)  # Left leg
canvas.create_line(100, 280, 150, 330) # Right leg


canvas.create_oval(220, 80, 300, 160)   # Head
canvas.create_line(260, 160, 260, 280) # Body
canvas.create_line(210, 180, 310, 180)  # Arms
canvas.create_line(260, 280, 210, 330)  # Left leg
canvas.create_line(260, 280, 310, 330) # Right leg

display(canvas)
