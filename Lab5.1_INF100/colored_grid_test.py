from uib_inf100_graphics.simple import canvas, display
from colored_grid import draw_grid

# Et 3x3 rutenett med innebygde farger
draw_grid(canvas, 40, 100, 120, 180, [
        ["red", "green", "blue"],
        ["yellow", "pink", "cyan"],
        ["black", "gray", "orange"],
    ])

# Et sjakkbrett
draw_grid(canvas, 170, 30, 370, 250, [
        ["white", "black"] * 4,
        ["black", "white"] * 4,
    ] * 4)

# En 2D-liste med kun én rad
draw_grid(canvas, 50, 310, 350, 370, [
    ['#00c', '#01c', '#02c', '#03c', '#04c', '#05c', '#06c', '#07c',
     '#08c', '#09c', '#0ac', '#0bc', '#0cc', '#0dc', '#0ec', '#0fc']
])

display(canvas)