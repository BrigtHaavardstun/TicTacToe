#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:07:08 2019
Updated on Tue Jan 28 2020
@author: brigthavardstun
"""
from tkinter import *
from ttt_magic import show_board, victory_screen,draw_screen

"""
Program settings
"""
WIDTH = 600  # Bredden på skjermen
HEIGHT = 600  # Høyden på skjermen

# Splitting into three verticals zones
b_rute = WIDTH/3  #bredde for en rute
h_rute = HEIGHT/3  #høyde for en rute



"""
Setting up Canvas

Canvas er det vi bruker til å tegne i python
"""
main = Tk()

CANVAS = Canvas(main, width=WIDTH, height=HEIGHT)

CANVAS.pack()






"""
Globale variabler
"""

# Players
spillerX = "X"
spillerO = "O"
EMPTY = "#"

BOARD = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]


def ledig_plass(pos_x, pos_y):
    """
    #TODO

    Gitt en x-posisjon og y-posisjon  finn ut om plassen er ledig, med å sjekke om den er "EMPTY" variabelen.
    :param pos_x:
    :param pos_y:
    :return: True hvis ledig, False hvis opptatt.
    """
    return True


def check_victory():
    """
   #TODO

    Denne metoden sjekker om det er en vinner.
    :return: True hvis det er en vinner, False hvis ikke
    """
    X_vinn = spillerX + spillerX + spillerX
    O_vinn = spillerO + spillerO + spillerO


    # Horizontal
    """
    for row in BOARD:
        if row == list(X_vinn):
            return True
        elif row == list(O_vinn):
            return True


    # Vertical
    for i in range(3):
        if BOARD[0][i] + BOARD[1][i] + BOARD[2][i] == X_vinn:
            return True
        elif BOARD[0][i] + BOARD[1][i] + BOARD[2][i] == O_vinn:
            return True

    # Diagonals
    if BOARD[0][0] + BOARD[1][1] + BOARD[2][2] == X_vinn:
        return True
    elif BOARD[0][0] + BOARD[1][1] + BOARD[2][2] == O_vinn:
        return True
    """

    # TODO: diagonal

    return False


def check_draw():
    """
    Gir True hvis hele brettet er fullt.
    :return:
    """
    return False









def legg_brikke_til_i_brettet(player, x, y):
    """
    #TODO

    Skal bare legge til spiller i brett på den gitte posisjonen.

    :param player:
    :param mouse_x:
    :param mouse_y:
    :return:
    """
    BOARD[x][y] = player


def get_next_player():
    """
    #TODO.

    Gitt dette brettet, tell antall spillerX og spillerO, den med færrest blir valgt.

    Default til X.
    :return:
    """

    return EMPTY





# GAME LOGIC / GUI LOGIC
def main_game_loop(pos_x, pos_y):
    """
    Hovedmetoden til spillet, binder sammen selve logikken.

    Denne skal være gitt.
    :param pos_x:
    :param pos_y:
    :return:
    """
    next_player = get_next_player()

    if ledig_plass(pos_x, pos_y):
        legg_brikke_til_i_brettet(next_player, pos_x, pos_y)

    show_board(CANVAS, BOARD, spillerX=spillerX, spillerO=spillerO)

    if check_victory():
        victory_screen(BOARD, CANVAS, b_rute, h_rute)

    if check_draw():
        draw_screen(CANVAS)

    show_board(CANVAS, BOARD, spillerX=spillerX, spillerO=spillerO)

# tells the canvas to run "click"-function when we click the canvas
def click(mouse_event):
    """
    Whenever a mouse click happens this methods gets called.

    :param mouse_event:
    :return:
    """
    mouse_x = mouse_event.x
    mouse_y = mouse_event.y
    print("X: " + str(mouse_x) + " Y: " + str(mouse_y))
    pos_x, pos_y = canvas_to_grid(mouse_x, mouse_y)
    # print("X: " + str(pos_x) + " Y: " + str(pos_y)) #TODO:

    main_game_loop(pos_x, pos_y)

def canvas_to_grid(mouse_x, mouse_y):
    """
    Converts a mouse click to a position in our board
    :param mouse_click: a mouse click
    :return: x_pos, y_pos
    """
    x_pos = int(mouse_x / b_rute)
    y_pos = int(mouse_y / h_rute)
    return x_pos, y_pos





if __name__ == '__main__':
    CANVAS.bind("<Button-1>", click)  # This makes a "click" on the canvas board call the method "click()"
    show_board(CANVAS, BOARD, spillerX, spillerO)

    mainloop()
