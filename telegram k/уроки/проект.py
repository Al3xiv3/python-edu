"""
игра  угадай число
комп загадал число
человек угадывает
недолет/перелет

Шаги:
1. приветствие+
2. меню+
3. игр.логика+
4. ввод пользователя+
5. рандом+
"""
from random import randint


# из random импортируем функцию randint
# randint(a, b) => даст случайное целое от а до b


def greeting():
    print('Привет, пользователь. Добро пожаловать в игру "Угадай число"')


def game():
    comp_num = randint(1, 100)

    while True:
        print("Введите число")

        try:  # пробуй
            n = int(input())  # съинтовать ввод
            if n == comp_num:
                print("Ура, Вы победили! Пока..")
                break

            if n < comp_num:
                print("Очень жаль, недолет")
            elif n > comp_num:
                print("Очень жаль, перелет")

        except ValueError:  # если получится ValueError
            print("Ты не русский? Сказано число")


    menu()


def menu():
    print('Главное меню: введите "1", чтобы начать играть; "0", чтобы выйти')

    while True:
        try:
            x = int(input())  # ввод числа

            # проверка x
            if x == 0:
                print("Досвидания")
                break
            elif x == 1:
                game()
            else:
                print("Введите 0 или 1")
        except ValueError:  # если получится ValueError
            print("Ты не русский? Сказано число")


def main():
    greeting()
    menu()


main()  # вызываем main