from uib_inf100_graphics.event_app import run_app
from snake_view import draw_board
import random

def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.direction = 'east'
    app.debug_mode = True
    app.board = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0,-1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 2, 3, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
    app.snake_size = 3
    app.head_pos = (3,4)
    app.state = 'active'
    app.timer_delay = 200

def move_snake(app):
    if(app.direction == 'east'): app.head_pos = (app.head_pos[0], app.head_pos[1]+1)
    elif(app.direction == 'north'): app.head_pos = (app.head_pos[0]-1, app.head_pos[1])
    elif(app.direction == 'south'): app.head_pos = (app.head_pos[0]+1, app.head_pos[1])
    elif(app.direction == 'west'): app.head_pos = (app.head_pos[0], app.head_pos[1]-1)

    if(is_legal_move(app.head_pos, app.board)):
        if(app.board[app.head_pos[0]][app.head_pos[1]] == -1): 
            app.snake_size += 1
            add_apple_at_random_location(app.board)
        else:
            for row in range(len(app.board)):
                for col in range(len(app.board[0])):
                    if(app.board[row][col] > 0): app.board[row][col] -= 1
        
        app.board[app.head_pos[0]][app.head_pos[1]] = app.snake_size
    else:
        app.state = 'gameover'
        return

def is_legal_move(pos, board):
    if(pos[0] < len(board) and pos[0] >= 0):
        if(pos[1] < len(board[0]) and pos[1] >= 0):
            if(board[pos[0]][pos[1]] <= 0):
                return True
    else: return False

def add_apple_at_random_location(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == -1): grid[row][col] += 1
    
    randomRow = random.randint(0, len(grid)-1)
    randomCol = random.randint(0, len(grid[0])-1)

    while(grid[randomRow][randomCol] != 0):
        randomRow = random.randint(0, len(grid)-1)
        randomCol = random.randint(0, len(grid[0])-1)
    
    grid[randomRow][randomCol] = -1

def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if(app.debug_mode == False and app.state == 'active'):
        move_snake(app)


def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if(key_pressed):
        if(event.key == 'd'):
            if(app.debug_mode): app.debug_mode = False
            else: app.debug_mode = True
        if(app.state == 'active'):
            if(event.key == 'Up'): app.direction = 'north'
            elif(event.key == 'Down'): app.direction = 'south'
            elif(event.key == 'Left'): app.direction = 'west'
            elif(event.key == 'Right'): app.direction = 'east'
            elif(event.key == 'Space'): move_snake(app)

def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    if(app.debug_mode): 
        canvas.create_text(
        5, 5,
        anchor='nw',
        text=f"app.head_pos='{app.head_pos}'app.snake_size='{app.snake_size}'app.direction='{app.direction}'app.state='{app.state}'",
        font='Arial 14',
    )
    if(app.state == 'active'):
        draw_board(canvas, 25, 25, 475, 375, app.board, app.debug_mode)
    else:
        canvas.create_text(
        110, 100,
        anchor='nw',
        text="Game Over",
        font='Arial 54',
        )

run_app(width=500, height=400, title="Snake")
