#  написать ф-ию some, принимает 2 парам. и вернет их произведение

def some(a, b):
    return a * b


print(some(2, 3))


#  написать ф-ию some2, принимает 3 парам. и вернет список по правилу:
#  1 эл-т  макс из них; 2 эл-т  их ср.ариф

def avg(a, b, c):
    return (a + b + c) / 3


def some2(a, b, c):
    return [max(a, b, c), avg(a, b, c)]


#  написать ф-ию some3, принимает 5 парам. и вернет сумму цифр их суммы

def sum_digits(x):
    '''
    Возвращает сумму цифр числа х (sum_digits.__doc__)
    '''
    y = 0
    while x != 0:
        y = y + x % 10
        x = x // 10
    return y


def some3(a, b, c, d, e):
    x = sum(a, b, c, d, e)
    return sum_digits(x)


print(some3(23, 12, 11, 44, 15))
