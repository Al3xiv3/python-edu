'''
8. Вводим n,m. Вывести наибольшее из них
9. Вводим n,m. Вывести сумму квадратов
10. Вводим n,m. Вывести факториал суммы
11. Вводим n, затем n чисел. Потом x. Вывести позицию х (нумерация с 1)
'''

# 8.
n = int(input())
m = int(input())


def f(n, m):
    if n > m:
        return n
    else:
        return m


print(f(n, m))

n = int(input())
m = int(input())

if n > m:
    print(n)
else:
    print(m)

n = int(input())
m = int(input())

print(max(n, m))

print(max(int(input()), int(input())))

# 9

n = int(input())
m = int(input())

print(n ** 2 + m ** 2)

print(int(input()) ** 2 + int(input()) ** 2)

# 10 Вводим n,m. Вывести факториал суммы

n = int(input())
m = int(input())

x = 1
for i in range(1, n + m + 1):
    x *= i

print(x)

# 11. Вводим n, затем n чисел. Потом вводим х.Вывести позицию х (нумерация с 1)

n = int(input())
lst1 = []

for i in range(1, n + 1):
    m = int(input)
    lst1.append(m)

x = int(input())

print(lst1.index(x) + 1)