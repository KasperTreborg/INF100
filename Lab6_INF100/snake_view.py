def draw_board(canvas, x1, y1, x2, y2, board, debug_mode):
    
    num_rows = len(board)
    num_cols = len(board[0]) if num_rows > 0 else 0

    cell_width = (x2 - x1) / num_cols
    cell_heigth = (y2 - y1) / num_rows

    for row in range(num_rows):
        for col in range(num_cols):
            if(board[row][col] == 0): color = 'lightgray'
            elif(board[row][col] < 0): color = 'cyan'
            elif(board[row][col] > 0): color = 'orange'

            rect_x1 = x1 + col * cell_width
            rect_y1 = y1 + row * cell_heigth
            rect_x2 = rect_x1 + cell_width
            rect_y2 = rect_y1 + cell_heigth

            canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill=color)

            if(debug_mode):
                text_x = (rect_x1 + rect_x2) / 2
                text_y = (rect_y1 + rect_y2) / 2

                canvas.create_text(
                text_x, text_y,
                anchor='center',
                text=f"{row}, {col}\n{board[row][col]}",
                font='Arial 14',
                fill='black'
                )