# 1. Приветствие

def greeting():
    print('Добро пожаловать!')

# 2. Приглашение к вводу длины пароля

def input_len_password():
    len_password = int(input('Введите длину пароля: '))
    if len_password > 0:
        return len_password
    else:
        return input_len_password()

# 3. Генерация случайного пароля

import random
import string

symbols = string.ascii_letters + string.digits + string.punctuation
greeting()
count = input_len_password()
password = ''.join(random.choices(symbols, k=count))

print(password)


