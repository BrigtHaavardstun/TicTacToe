

def got_draw(board):
    draw = True
    for row in board:
        for cell in row:
            if cell == " ":
                draw = False
    
    if draw:
        print("Its a draw!")
    return draw
def got_winner(board):

    # Vertical
    for y in range(3):
        if board[0][y] == board[1][y] and board[1][y] == board[2][y] and board[0][y] != " ":
            print("we have a winner!")
            return True
    #  Horizaontal
    for x in range(3):
        if board[x][0] == board[x][1] and board[x][1] == board[x][2] and board[x][0] != " ":
            print("we have a winner!")
            return True

    # Top left to bottom right 
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != " ":
        print("we have a winner!")
        return True

    # Top right to bottom left
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != " ":
        print("we have a winner!")
        return True


    return False


w,h = 3,3
# set board
board = [[" " for x in range(w) ] for y in range(h) ]


# X-es start
player = "X"

# Print the board
print("    0    1    2")
for i in range(len(board)-1, -1, -1):
    print(str(i) + " " + str(board[i]))

while not got_winner(board) and not got_draw(board):
    print(f"It's {player}s turn!")
    target = input("Where do you want to place your pice? give input like '1 1': ")
    x_pos, y_pos = target.split()

    # Convert the input text to numbers
    x_pos = int(x_pos)
    y_pos = int(y_pos)


    if board[y_pos][x_pos] != " ":
        print("That tile is taken, try agian")
    else:
        board[y_pos][x_pos] = player

        # Change player
        if player == "X":
            player = "O"
        else:
            player = "X"


        # Print the board
        print("    0    1    2")
        for i in range(len(board)-1, -1, -1):
            print(str(i) + " " + str(board[i]))
