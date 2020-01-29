#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:07:08 2019
Updated on Tue Jan 28 2020
@author: brigthavardstun
"""
from tkinter import *


"""
Program settings
"""
WIDTH = 600
HEIGHT = 600

# Splitting into three verticals zones
b_rute = WIDTH/3  #bredde for en rute
h_rute = HEIGHT/3  #høyde for en rute

"""
Setting up Canvas
"""
main = Tk()

CANVAS = Canvas(main, width=WIDTH, height=HEIGHT)
CANVAS.pack()

"""
Globals
"""
# Players
spillerX = "X"
spillerO = "O"
EMPTY = "#"

BOARD = [[EMPTY, spillerX, EMPTY],
         [spillerO, EMPTY, EMPTY],
         [EMPTY, EMPTY, spillerX]]


def ledig_plass(pos_x, pos_y):
    """
    Denne skal løses live.

    Gitt en x-posisjon og y-posisjon  finn ut om plassen er ledig, med å sjekke om den er "EMPTY" variabelen.
    :param pos_x:
    :param pos_y:
    :return: True hvis ledig, False hvis opptatt.
    """
    if BOARD[pos_y][pos_x] == EMPTY:
        return True
    else:
        return False


def check_victory():
    """
    DENNE KAN BLI GJORT LIVE

    Denne metoden sjekker om det er en vinner.
    :return: True hvis det er en vinner, False hvis ikke
    """
    X_vinn = spillerX + spillerX + spillerX
    O_vinn = spillerO + spillerO + spillerO


    # Horizontal
    for row in BOARD:
        if row == list(X_vinn):
            print("X er vinneren!")
            return True
        elif row == list(O_vinn):
            print("O er vinneren!")
            return True


    # Vertical
    for i in range(3):
        if BOARD[0][i] + BOARD[1][i] + BOARD[2][i] == X_vinn:
            print("X er vinneren!")
            return True
        elif BOARD[0][i] + BOARD[1][i] + BOARD[2][i] == O_vinn:
            print("O er vinneren!")
            return True

    # Diagonals
    if BOARD[0][0] + BOARD[1][1] + BOARD[2][2] == X_vinn:
        print("X er vinneren!")
        return True
    elif BOARD[0][0] + BOARD[1][1] + BOARD[2][2] == O_vinn:
        print("O er vinneren!")
        return True


    if BOARD[0][2] + BOARD[1][1]+BOARD[2][0] == X_vinn:
        print("X er vinneren!")
        return True
    elif BOARD[0][2] + BOARD[1][1]+BOARD[2][0] == O_vinn:
        print("O er vinneren!")
        return True

    return False


def check_draw():
    for row in BOARD:
        for element in row:
            if element == EMPTY:  # bruke ledig_plass()?
                return False

    return True


def victoryClick(mouseEvent):
    print("Game Done")


def draw_click(mouseEvent):
    print("Draw")


def victory_screen():
    CANVAS.bind("<Button-1>", victoryClick)  # rebinds a click so we cannot continue to play the game.


def draw_screen():
    CANVAS.bind("<Button-1>", draw_click)  # rebinds a click so we cannot continue to play the game.


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

    victory = check_victory()
    if victory:
        victory_screen()
    draw = check_draw()
    if draw:
        draw_screen()
    show_board()


def legg_brikke_til_i_brettet(player, mouse_x, mouse_y):
    """
    KODES LIVE!

    Skal bare legge til spiller i brett på den gitte posisjonen.

    :param player:
    :param mouse_x:
    :param mouse_y:
    :return:
    """
    BOARD[mouse_y][mouse_x] = player


def get_next_player():
    """
    Denne skal løses live.

    Gitt dette brettet, tell antall spillerX og spillerO, den med færrest blir valgt.

    Defualt til X.
    :return:
    """

    o_antall = 0
    x_antall = 0

    for row in BOARD:
        for element in row:
            if element == spillerX:
                x_antall = x_antall + 1
            elif element == spillerO:
                o_antall = o_antall + 1

    if o_antall < x_antall:
        return spillerO
    else:
        return spillerX



def show_board():
    """
    Uses the current BOARD to draw the GUI

    :return:
    """

    # Idea: hva om show_board ble importert gjennom en tic tac toe magic modul, så det ikke ble så rotet?
    global BOARD, CANVAS  # TODO: burde dette fjernes (gjør ingenting), men viser hva som er relevant.
    CANVAS.delete("all")  # re-draws everything


    CANVAS.create_line(b_rute, 0, b_rute, HEIGHT)  # First vertical line
    CANVAS.create_line(b_rute * 2, 0, b_rute * 2, HEIGHT)  # Second vertical line

    CANVAS.create_line(0, h_rute, WIDTH, h_rute)  # First horizontal line
    CANVAS.create_line(0, h_rute * 2, WIDTH, h_rute * 2)  # Second horizontal line

    for y in range(3):
        for x in range(3):
            player = BOARD[y][x]
            draw(player, x, y)


def draw(player, x_cord, y_cord):
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
    global CANVAS
    if player == spillerX:
        CANVAS.create_line(
            x_cord * b_rute, y_cord * h_rute,
            (x_cord + 1) * b_rute, (y_cord + 1) * h_rute
        )
        CANVAS.create_line(
            x_cord * b_rute, (y_cord + 1) * h_rute,
            (x_cord + 1) * b_rute, y_cord * h_rute
        )
    elif player == spillerO:
        CANVAS.create_oval(
            x_cord * b_rute, y_cord * h_rute,
            (x_cord + 1) * b_rute, (y_cord + 1) * h_rute
        )


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
    main_game_loop(pos_x, pos_y)

def canvas_to_grid(mouse_x, mouse_y):
    """
    Converts a mouse click to a position in our board
    :param mouse_click: a mouse click
    :return: x_pos, y_pos
    """
    x_pos = int(mouse_x / 200)
    y_pos = int(mouse_y / 200)
    return x_pos, y_pos

CANVAS.bind("<Button-1>", click)  # This makes a "click" on the canvas board call the method "click()"

if __name__ == '__main__':
    show_board()
    mainloop()
