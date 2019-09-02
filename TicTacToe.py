#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:07:08 2019

@author: brigthavardstun
"""

from tkinter import *
import sys  # used to exit game

END_SCREEN = False
CANVAS = None
BOARD = None

CROSSES = "X"
CIRCLE = "O"


def draw(symbol_to_place, x_pos, y_pos):
    """
    Draws a circle or cross on the canvas based the symbol given.
    Translates x_pos and y_pos to canvas coordinates.
    :param symbol_to_place:
    :param x_pos: grid coordinate
    :param y_pos: grid coordinate
    :return:
    """
    global CANVAS, BOARD, CROSSES, CIRCLE

    # CIRCLES
    if symbol_to_place == CIRCLE:
        CANVAS.create_oval(
            x_pos * 200, y_pos * 200,
            (x_pos + 1) * 200, (y_pos + 1) * 200
        )
        BOARD[y_pos][x_pos] = symbol_to_place

    # CROSSES
    else:
        CANVAS.create_line(
            x_pos * 200, y_pos * 200,
            (x_pos + 1) * 200, (y_pos + 1) * 200
        )
        CANVAS.create_line(
            x_pos * 200, (y_pos + 1) * 200,
            (x_pos + 1) * 200, y_pos * 200
        )
        BOARD[y_pos][x_pos] = symbol_to_place


def click(mouse_click):
    """
    This fucntion is run whenever we click on the canvas

    Handles the input from the user, and tries to make a move.

    In the end checks if there is a winner.
    :param event:
    :return: None
    """
    global CANVAS, BOARD, CROSSES, CIRCLE, END_SCREEN
    if END_SCREEN:
        handle_end(mouse_click)
        return None
    symbol_to_place = whose_turn_is_it(BOARD)
    (x_pos, y_pos) = canvas_to_grid(mouse_click)

    # if there already is a symbol where we try to place we can't and have to find a new one.
    if BOARD[y_pos][x_pos] == CROSSES or BOARD[y_pos][x_pos] == CIRCLE:
        print("That square is taken!\nTry again.")
        return None
    else:
        draw(symbol_to_place, x_pos, y_pos)
        if check_for_victory(BOARD):
            END_SCREEN = True

        elif check_for_full_board(BOARD):
            winner_screen(None, True)
            END_SCREEN = True


def setup_game():
    """
    Creates a canvas and a board to be used in the program.


    :return:
    """
    print("new game")
    set_up_globals()
    set_up_canvas()
    set_up_board()


def set_up_globals():
    """
    Sets globals
    :return:
    """
    global END_SCREEN, CROSSES, CIRCLE
    END_SCREEN = False

    CROSSES = "X"
    CIRCLE = "O"


def set_up_board():
    """
    Creates a board for us to save information in.
    :return:
    """
    global BOARD

    BOARD = [["00", "10", "20"],
             ["01", "11", "21"],
             ["02", "12", "22"]]


def set_up_canvas():
    """
    Sets up the canvas
    :return:
    """
    global CANVAS

    # First time running
    if CANVAS is None:
        main = Tk()
        CANVAS = Canvas(main, width=600, height=600)
        CANVAS.pack()

        # tells the canvas to run "click"-function when we click the canvas
        CANVAS.bind("<Button-1>", click)

    CANVAS.create_polygon(0, 0, 0, 600, 600, 600, 600, 0, fill="white")

    CANVAS.create_line(200, 0, 200, 600)
    CANVAS.create_line(400, 0, 400, 600)

    CANVAS.create_line(0, 200, 600, 200)
    CANVAS.create_line(0, 400, 600, 400)


def whose_turn_is_it(board):
    """
    Function to figure out if its CROSSES OR CIRCLES TURN

    :param board: a 2D list of strings
    :return: either CROSSES OR CIRCLES depending on whose turn it is.
    """
    global CROSSES, CIRCLE
    nr_crosses = 0
    nr_circles = 0
    for line in board:
        for cell in line:
            if cell == CROSSES:
                nr_crosses += 1
            elif cell == CIRCLE:
                nr_circles += 1

    if nr_crosses >= nr_circles:
        return CIRCLE
    else:
        return CROSSES


def check_for_full_board(board):
    """
    Checks if the board is full
    :param board:
    :return: True if the board is full
    """
    global CROSSES, CIRCLE
    nr_crosses = 0
    nr_circles = 0
    for line in board:
        for cell in line:
            if cell == CROSSES:
                nr_crosses += 1
            elif cell == CIRCLE:
                nr_circles += 1

    return nr_circles + nr_crosses == 9


def check_for_victory(board):
    """
    Checking if one of the players has won
    :param board:
    :return:
    """
    global CIRCLE, CROSSES, CANVAS
    crosses_line = CROSSES + CROSSES + CROSSES
    circles_line = CIRCLE + CIRCLE + CIRCLE

    # Horizontal victory
    for row in range(3):
        line = board[row][0] + board[row][1] + board[row][2]
        if line == crosses_line:
            CANVAS.create_line(0, 100 + (row * 200), 600, 100 + (row * 200), fill="red",
                               width=2)  # Create line showing winning line
            winner_screen(CROSSES)
            return True
        elif line == circles_line:
            CANVAS.create_line(0, 100 + (row * 200), 600, 100 + (row * 200), fill="red",
                               width=2)  # Create line showing winning line
            winner_screen(CIRCLE)
            return True

    # Vertical victory
    for vertical in range(3):
        line =  board[0][vertical] + board[1][vertical] + board[2][vertical]
        if line == crosses_line:
            CANVAS.create_line(100 + (vertical * 200), 0, 100 + (vertical * 200), 600, fill="red", width=2)
            winner_screen(CROSSES)
            return True
        elif line == circles_line:
            CANVAS.create_line(100 + (vertical * 200), 0, 100 + (vertical * 200), 600, fill="red", width=2)
            winner_screen(CIRCLE)
            return True

    # Diagonal
    left_right_diagonal_line = board[0][0] + board[1][1] + board[2][2]
    if left_right_diagonal_line == crosses_line:
        CANVAS.create_line(0, 0, 600, 600, fill="red", width=2)
        winner_screen(CROSSES)
        return True
    elif left_right_diagonal_line == circles_line:
        CANVAS.create_line(0, 0, 600, 600, fill="red", width=2)
        winner_screen(CIRCLE)
        return True

    right_left_diagonal_line = board[0][2] + board[1][1] + board[2][0]
    if right_left_diagonal_line == crosses_line:
        CANVAS.create_line(0, 600, 600, 0, fill="red", width=2)
        winner_screen(CROSSES)
        return True
    elif right_left_diagonal_line == circles_line:
        CANVAS.create_line(0, 600, 600, 0, fill="red", width=2)
        winner_screen(CIRCLE)
        return True

    return False


def handle_end(mouse_click):
    """
    Handles mouse clicks when in "end screen" mode.
    Either restarts the game, quits, or ignores click if not in area.
    :param mouse_click:
    :return:
    """
    global CANVAS
    x_pos = CANVAS.canvasx(mouse_click.x)
    y_pos = CANVAS.canvasy(mouse_click.y)
    if 400 < y_pos < 500:
        if 250 > x_pos > 50:
            setup_game()
        elif 350 < x_pos < 550:
            sys.exit()


def canvas_to_grid(mouse_click):
    """
    Converts a mouse click to a position in our board
    :param mouse_click: a mouse click
    :return: x_pos, y_pos
    """
    global CANVAS
    x_pos = int(CANVAS.canvasx(mouse_click.x) / 200)
    y_pos = int(CANVAS.canvasy(mouse_click.y) / 200)
    return x_pos, y_pos


def winner_screen(winner, draw=False):
    """
    Creates a winner screen, or draw screen, outputting the winner.
    Also ask the user if he wants to play again or quit.
    :param winner:
    :param draw:
    :return:
    """
    global CANVAS, CROSSES, CIRCLE
    if not draw:
        if winner == CROSSES:
            shape = "Crosses"
        else:
            shape = "Circles"
        CANVAS.create_text(300, 200,fill="darkblue", font="Times 40 italic bold",
                            text=("The winner is " + shape))
    else:
        CANVAS.create_text(300, 200, fill="darkblue", font="Times 40 italic bold",
                           text="It's a draw!")

    CANVAS.create_text(175, 450, fill="darkblue", font="Times 20 italic bold",
                  text=("New Game"))
    CANVAS.create_text(425, 450, fill="darkblue", font="Times 20 italic bold",
                  text=("Quit game"))


setup_game()
mainloop()
