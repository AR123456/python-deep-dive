# Simple Python tic tac toe game
from IPython.display import clear_output
# welcome
print("Welcome to Python-Tic-Tac-To")
# draw game board
def display_board(board):
    clear_output()
    print(board[7]+"|" + board[8]+"|"+ board[9])
    print(board[4]+"|" + board[5]+"|"+ board[6])
    print(board[1]+"|" + board[2]+"|"+ board[3])
starting_board = [" __ "]*10
display_board(starting_board)
# test_board = ['__','1','O','X','O','X','O','X','O','9']
# display_board(test_board)
test_board = ['__','1','O','X','O','X','O','X','O','9']
# have players choose their playing piece
def player_input():
    """Tupal who's output will be (Player 1 marker, Player 2 marker ) """
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1 :  Pick X or O").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")
# tupal unpacking
player1_marker , player2_marker = player_input()

def place_marker(board, marker, position):

    board[position] = marker
place_marker(starting_board," $ ", 8)

display_board(starting_board)
