"""Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень)."""

def season(m):

    if m == 12 or m == 1 or m == 2:
        return "Зима"
    elif m == 3 or m == 4 or m == 5:
        return "Весна"
    elif m == 6 or m == 7 or m == 8:
        return "Лето"
    elif m == 9 or m == 10 or m == 11:
        return "Осень"
    else:
        return "Такого месяца нет"

print(season(11))

