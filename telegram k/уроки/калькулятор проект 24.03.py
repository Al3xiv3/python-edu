# 1.

def float_input_numbers():
    return map(float, input("Введите два числа через пробел:").split())

a, b = float_input_numbers()

# 2.

x = input('Введите операцию:')

def operations():
    if x == '+':
        return a+b
    elif x == '-':
        return a-b
    elif x == '*':
        return a*b
    elif x == '/' and b != 0:
        return a/b
    else:
        return 'Ошибка ввода'

# 3

print(operations())

