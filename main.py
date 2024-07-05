from tkinter import *

GAME_TITLE = "Tic-Tac"
win_conditions = [
    # Rows
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    # Columns
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    # Diagonals
    [0, 4, 8], [2, 4, 6]]


def greeting():
    print(f"Welcome to {GAME_TITLE}")


def get_player_move():
    while True:
        try:
            choose = int(input('Choose a number:'))
            return choose
        except:
            print("Write only number! -_-")


def create_field():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board


def show_field(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def change_board(board, player_token, player_move):
    if player_move in range(0, 10):
        index_board = player_move - 1
        if board[index_board] in "X0":
            print("Select another cell")
        else:
            board[index_board] = player_token
    else:
        print("Please choose a number between 1 and 9.")
    return board


def main():
    greeting()
    board = create_field()
    show_field(board)
    player_token = "X"
    while True:
        print(f"The move is {player_token}")
        player_move = get_player_move()
        board = change_board(board, player_token, player_move)
        if player_token == "X":
            player_token = "0"
        elif player_token == "0":
            player_token = "X"
        elif player_token != "X" or player_token != "0":
            return
        show_field(board)
        check_winner(board)


def check_winner(board):
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            print(f"{board[condition[0]]} wins")
            return
    TIE = True
    for i in board:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            TIE = False
            break

    if TIE:
        print('Tie')



if __name__ == "__main__":
    main()
