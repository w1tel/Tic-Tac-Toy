import os

# проверка существует ли такой логиy

def check_login(name):
    items = os.listdir("data")
    for i in items:
        if name == i.replace('.txt',''):
            print('Пеользоватль найден!!!')
            return True
    else:
        print('Пользователь не найден!')
    return False

def check_password(file_name, password):
    file = open(file=f'data/{file_name}.txt', mode='r', encoding='UTF-8')
    info_from_file = file.read()

    user_info = format_to_dict(info_from_file)

    print(user_info)
    if password == user_info['password']:
        print('Пароль найден!')
        return True
    else:
        print('Пароль не найден!')
    return False

def save_game_result(name: str, result_game) -> None:
    file = open(file='player_progress.txt', mode='rt', encoding='UTF-8')

def format_to_dict(info_from_file: str) -> dict:
    user_info = {}
    for i in info_from_file.split():
        key, value = i.split("-")
        user_info[key] = value
    return user_info

