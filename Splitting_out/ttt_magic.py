from tkinter import *
def show_board(canvas, board, spillerX, spillerO):
    """
    Uses the current BOARD to draw the GUI

    :return:
    """


    canvas.delete("all")  # re-draws everythings
    width = int(canvas["width"])
    height = int(canvas["height"])

    b_rute = width / 3  # bredde for en rute
    h_rute = height / 3  # høyde for en rute


    canvas.create_line(b_rute, 0, b_rute, height)  # First vertical line
    canvas.create_line(b_rute * 2, 0, b_rute * 2, height)  # Second vertical line

    canvas.create_line(0, h_rute, width, h_rute)  # First horizontal line
    canvas.create_line(0, h_rute * 2, width, h_rute * 2)  # Second horizontal line

    for y in range(3):
        for x in range(3):
            player = board[y][x]
            draw(canvas, player, x, y, spillerX, spillerO, b_rute, h_rute)


def draw(canvas, player, x_cord, y_cord, spillerX, spillerO, b_rute, h_rute):
    """
    Draws in one element in the canvas.

    NOTE: This method should be given.

    :param player:
    :param x_cord:
    :param y_cord:
    :param w_part:
    :param h_part:
    :return:
    """
    if player == spillerX:
        canvas.create_line(
            x_cord * b_rute, y_cord * h_rute,
            (x_cord + 1) * b_rute, (y_cord + 1) * h_rute
        )
        canvas.create_line(
            x_cord * b_rute, (y_cord + 1) * h_rute,
            (x_cord + 1) * b_rute, y_cord * h_rute
        )
    elif player == spillerO:
        canvas.create_oval(
            x_cord * b_rute, y_cord * h_rute,
            (x_cord + 1) * b_rute, (y_cord + 1) * h_rute
        )


def winning_area(board):
    # Horizontal
    for i in range(3):
        if board[i][0]*3 == board[i][0]+board[i][1]+board[i][2] and board[i][2] != "#":
            return [0,i+0.5],[3,i+0.5]

    # Vertical
    for i in range(3):
        if board[0][i] + board[1][i] + board[2][i] == board[0][i]*3 and board[0][i] != "#":
            return [i+0.5,0], [i+0.5,3]

    # Diagonals
    if board[0][0] + board[1][1] + board[2][2] == board[0][0]*3:
        return [0,0],[3,3]

    if board[0][2] + board[1][1] + board[2][0] == board[0][2]*3:
        return [3,0],[0,3]


def victory_click(mouseEvent):
    print("Game Done")


def victory_screen(board, canvas, bredde, høyde):
    start, end = winning_area(board)
    canvas.create_line(start[0]*bredde, start[1]*høyde, end[0]*bredde, end[1]*høyde, fill="red", width=2)

    canvas.bind("<Button-1>", victory_click)  # rebinds a click so we cannot continue to play the game.
    mainloop()


def draw_click(mouseEvent):
    print("Draw")


def draw_screen(canvas):
    canvas.bind("<Button-1>", draw_click)  # rebinds a click so we cannot continue to play the game.



