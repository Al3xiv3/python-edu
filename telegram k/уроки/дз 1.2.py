"""Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
если год високосный, и False иначе."""

def is_year_leap(y):
    x = 0
    if y % 4 == 0:
        x = True
    else:
        x = False
    return x


print(is_year_leap(2019))
