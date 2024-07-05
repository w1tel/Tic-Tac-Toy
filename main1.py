import work_with_files
import random

GAME_TITLE = "Tic-Tac"
win_conditions = [
    # Rows
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    # Columns
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    # Diagonals
    [0, 4, 8], [2, 4, 6]]


def menu():
    print('Режимы \n 1 - Режим для двоих игроков \n 2 - Режис игры с искуственным интелектом(слабый)')
    user_mode = int(input('Введите режим игры:'))
    return user_mode


def register():
    games_played = 0
    victories = 0
    defeats = 0
    ties = 0
    name = input('Введите имя пользователя:')
    password = input("Введите пароль:")
    file = open(file=f'data/{name}.txt', mode='w', encoding='UTF-8')
    file.write(f'{name} {password} {games_played}')
    file.close()
    return {"is_logged": True, "name": name, "games_played": games_played, "victories": victories, "defeats": defeats,
            "ties": ties}


def log_in():
    user_name = input('Введите имя зарегестрируемого пользователя:')
    if work_with_files.check_login(user_name):
        user_password = input('Введите пароль от выбранного аккаунта:')
    else:

        return
    if work_with_files.check_password(user_name, user_password):
        print('Пользователь авторизирован!')
        return True


def two_player_mode():
    greeting()
    board = create_field()
    show_field(board)
    player_token = "X"
    game_over = False
    while not game_over:
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
        game_over = check_winner(board)


def vs_computer_mode(player="player"):
    if player != "player":
        pass
    greeting()
    board = create_field()
    show_field(board)
    player_token = "X"
    game_over = False
    while not game_over:
        print(f"The move is {player_token}")
        if player_token == "X":
            player_move = get_player_move()
            board = change_board(board, player_token, player_move)
        elif player_token == "0":
            board = computer_move(board)
            show_field(board)
            game_over = check_winner(board)
        if player_token == "X":
            player_token = "0"
        elif player_token == "0":
            player_token = "X"
        elif player_token != "X" or player_token != "0":
            return


def computer_move(board):
    '''Функция возвращает измененную доску с сделанными ходами компьютера'''
    # possible_moves = [index for index, cell in enumerate(board) if cell not in "X0"]
    possible_moves = []
    for cell in board:
        if cell not in 'X0':
            index = board.index(cell)
            possible_moves.append(index)
    computer_choice = random.choice(possible_moves)
    board[computer_choice] = "0"
    return board


def greeting(name='player'):
    print(f'Hey {name}!')
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
    is_logged_in = False
    player1_name = None
    player2_name = None
    player1_victories = None
    player2_victories = None
    player1_defeats = None
    player2_defeats = None
    player1_ties = None
    player2_ties = None
    player1_game_played = None
    player2_game_played = None
    while True:
        if not is_logged_in:

            print('1 - Хотите зарегестрироваться')
            print('2 - Хотите авторизироваться и продолжить игру ')
            print('3 - Одиночная игра без регестрации')
            print('0 - Выход из игры')
            answer = input('Выбранное действие: ')

            if answer == '1':
                # is_logged_in = register()
                player_info = register()
                is_logged_in = player_info['is_logged']
                player1_name = player_info['name']
                player1_victories = player_info['victories']
                player1_defeats = player_info['defeats']
                player1_ties = player_info['ties']
                player1_game_played = player_info['games_played']
            elif answer == '2':
                is_logged_in = log_in()

            elif answer == '3':
                user_mode = menu()
                if user_mode == 1:
                    two_player_mode()
                elif user_mode == 2:
                    vs_computer_mode()
            elif answer == '0':
                break
        else:
            print('1 - Игра для двоих игроков')
            print('2 - Игра с компьютером')
            print('3 - Лидеры')
            print('4 - Статистика игрока')
            print('0 - Выход из игры')
            answer = input('Выбранное действие: ')

            if answer == '1':
                print('Для игры с двумя игроками необходимо Войти или Зарегестрироваться второму игроку')
                ans = int(input('1 - Войти \n2 - Зарегестрироваться'))

                if ans == '1':
                    log_in()
                elif ans == "2":
                    player_info = register()
                    is_logged_in = player_info['is_logged']
                    player2_name = player_info['name']
                    player2_victories = player_info['victories']
                    player2_defeats = player_info['defeats']
                    player2_ties = player_info['ties']
                    player2_game_played = player_info['games_played']


                    player_vs_player_mode()

            elif answer == '2':
                vs_computer_mode()

            elif answer == '3':
                pass
            elif answer == '4':
                pass
            elif answer == '0':
                break


def player_vs_player_mode(player1, player2):

    result_game = {}
    return result_game


def check_winner(board):
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            print(f"{board[condition[0]]} wins")
            return True

    TIE = True
    for i in board:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            TIE = False
            break

    if TIE:
        print('Tie')
        return True

    return False


if __name__ == "__main__":
    main()
