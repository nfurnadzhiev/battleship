#!/usr/bin/python
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

guess_row = ""
guess_col = ""
while not (guess_row.isdigit() and guess_col.isdigit()):
    guess_row = raw_input("Guess Row:")
    guess_col = raw_input("Guess Col:")

    if guess_row.isdigit() and guess_col.isdigit():
        guess_row = guess_row
        guess_col = guess_col
    else:
       print "Thats not a number! Try again!" 

guess_row = int(guess_row)
guess_col = int(guess_col)

if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
elif guess_row >= 5 and guess_col >= 5:
    print_board(board) 
    print "Oops, that's not even in the ocean."
elif board[int(guess_row)][int(guess_col)] == "X":
    print "You guessed that one already."
else:
    print "You missed my battleship!"
    board[int(guess_row)][int(guess_col)] = "X"
    print_board(board)

for turn in range(4):

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            break
    else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                    print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                    print "You guessed that one already."
            else:
                    print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    print(turn + 1)
    if turn == 3:
            print "Game Over"



