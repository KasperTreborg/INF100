from uib_inf100_graphics.event_app import run_app

def app_started(app):
    app.text = 'Hello world!'

def key_pressed(app, event):
    if(key_pressed): 
        if(event.key == 'BackSpace' or event.key == 'Backspace'): app.text = app.text[:-1]
        elif(event.key == 'Space'): app.text += ' '
        elif(event.key == 'Return' or event.key == 'Enter'): app.text += '\n'
        else: app.text += event.key

def redraw_all(app, canvas):
    # tegn teksten
    canvas.create_text(
        20, 20,
        anchor='nw',
        text=app.text,
        font='Arial 14',
    )

run_app(width=400, height=400)
