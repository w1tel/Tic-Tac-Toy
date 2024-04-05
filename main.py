GAME_TITLE = "Tic-Tac"


def greeting():
    print(f"Welcome to {GAME_TITLE}")


def get_player_move():
    choose = input('Choose a X or 0:')
    return choose


def create_field():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board


def show_field(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def change_board(board, player_token, player_move):
    return board


def main():
    greeting()
    board = create_field()
    show_field(board)
    player_token = "X"
    while True:
        player_move = get_player_move()
        board = change_board(board, player_token, player_move)
        if player_token == "X":
            player_token = "0"
        elif player_token == "0":
            player_token = "X"

        show_field(board)


if __name__ == "__main__":
    main()
