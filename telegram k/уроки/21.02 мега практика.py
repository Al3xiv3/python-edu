#1. Вводим n. найти  (n+5)! #факториал (n+5)
"""
n = int(input())
x = 1
if n + 5 <= 0:
    print('Факториала нет')
else:
    for i in range(1, n + 5 + 1):
        x = x * i
    print(x)
"""

#2. Вводим n, m. найти n^m-1 без **
"""
n = int(input())
m = int(input())
x = 1

for i in range(1, m + 1):
    x = x * n
x = x - 1
print(x)
"""

#3. Дан список. Получить другой список по правилу a**(a-1), где а - эл-т исходного списка

#способ 1
"""
lst1 = [1, 2, 3, 4]
lst2 = []

for i in lst1:
    t = i ** (i - 1)
    lst2.append(t)
print(lst2)
"""
#способ 2 (генератором)
"""
lst1 = [1, 2, 3, 4]
lst2 = [i ** (i - 1) for i in lst1]

print(lst2)
"""

#4. Даны списки A, B. Получить другой список по правилу a!+b*(a-1), где а- эл-т списка A, b- эл-т списка B

def factorial(f):
    x = 1
    for i in range(1, f + 1):
        x = x * i
    return x

#способ 1
"""
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = []

for i in range(0, len(A)):
    t = factorial(A[i]) + B[i] * (A[i] - 1)
    C.append(t)
print(C)
"""

#способ 2 (генератором)
"""
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = [factorial(A[i]) + B[i] * (A[i] - 1) for i in range(0, len(A))]

print(C)
"""

#5. Даны списки A, B. Получить словарь: {a*8 : b-a}, где а - эл-т  списка A, b - эл-т  списка B

#способ 1
"""
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
d = dict()

for i in range(0, len(A)):
    k = A[i] * 8
    v = B[i] - A[i]
    d[k] = v
print(d)
"""

#способ 2 (генератором)
"""
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
d = dict()

d = {A[i] * 8: B[i] - A[i] for i in range(0, len(A))}

print(d)
"""

#6. Дано число в виде двоичного числа, Преобразовать в десятичное.
"""
a = 1010
i = 0
s = 0

while a != 0:
    b = a % 10
    s = s + b * 2 ** i
    i = i + 1
    a = a // 10
print(s)
"""
"""
#7. Дано число в виде восьмеричного числа, Преобразовать в десятичное.

a = 16
i = 0
s = 0

while a != 0:
    b = a % 10
    s = s + b * 8 ** i
    i = i + 1
    a = a // 10
print(s)
"""

#8. Дано число в виде шестнадцатиричной строки, Преобразовать в десятичное.
"""
alph = '0123456789abcdef'

a = '10'
i = 0
s = 0

while a != '':
    b = alph.index(a[-1])
    s = s + b * 16 ** i
    i = i + 1
    a = a[:-1]
print(s)
"""

#9. Дано число в виде восемнадцатиричной строки, Преобразовать в десятичное.

alph = '0123456789abcdefghijklmnopqrstuvwxyz'
base = 25

a = '1000'
i = 0
s = 0

while a != '':
    b = alph.index(a[-1])
    s = s + b * base ** i
    i = i + 1
    a = a[:-1]
print(s)