
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
