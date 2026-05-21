import random

board = [" " for i in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(symbol):

    if board[0] == board[1] == board[2] == symbol:
        return True
    if board[3] == board[4] == board[5] == symbol:
        return True
    if board[6] == board[7] == board[8] == symbol:
        return True

    if board[0] == board[3] == board[6] == symbol:
        return True
    if board[1] == board[4] == board[7] == symbol:
        return True
    if board[2] == board[5] == board[8] == symbol:
        return True

    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True

    return False


def check_draw():
    return " " not in board


def player_move():

    while True:

        move = int(input("Enter position (1-9): ")) - 1

        if move >= 0 and move <= 8 and board[move] == " ":
            board[move] = "X"
            break

        else:
            print("Invalid move!")


def ai_move():

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            if check_winner("O"):
                return

            board[i] = " "

    for i in range(9):

        if board[i] == " ":

            board[i] = "X"

            if check_winner("X"):
                board[i] = "O"
                return

            board[i] = " "

    empty = []

    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    move = random.choice(empty)
    board[move] = "O"

print("TIC TAC TOE")
print("You are X")
print("AI is O")

while True:

    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if check_draw():
        print_board()
        print("Match Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if check_draw():
        print_board()
        print("Match Draw!")
        break
