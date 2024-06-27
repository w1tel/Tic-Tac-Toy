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
    info = file.readline().split()
    if password == info[1]:
        print('Пароль найден!')
        return True
    else:
        print('Пароль не найден!')
    return False

