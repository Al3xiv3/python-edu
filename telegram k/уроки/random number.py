import random

random_num = random.randint(1, 5)

user_num = int(input('Угадай число от 1 до 10:'))


if user_num == random_num:
    print('Вы угадали число, поздравляем!')
else:
    while user_num != random_num:
        print('Попробуйте еще раз')
        user_num = int(input('Угадай число от 1 до 10:'))
    print("Вы угадали число, поздравляем!")

#print(f'Было загадано число {random_num}')