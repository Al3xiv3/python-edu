""" напишите функцию sum_range(start, end), которая суммирует все целые числа
от значения start до значения end включительно. если первое число больше второго- поменять местами"""


def sum_range(start, end):

    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))

print(sum_range(10, 1))
