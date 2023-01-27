# 1. Синтаксис объявления функции 
# def <name>(<parameters>):
#     <body>
#   ^ 4 spaces
# 2. Возврат значений(с помощью return)
# example 
'''
def sum(a, b):
    return a+b
'''

# task 1: Написать функцию, которая возвращает абсолютную разность аргументов

def f(a, b):
    return abs(a - b)

abssum = f(10, 20)
print(abssum)

'''
питон смотрит сверху вниз. На 14стр видит def (ага обьявление функции) и кладет её  в оперативку. 

в стр 17 видит вызов f. питон обращается в ту область памяти где ее обьявление(грубо в стр14) вместо a, b ставит 10, 20 и возвращает  результат.
и с результатом обратно возвращается туда откуда вызывали(то бишь стр 17)
'''

# example 1
def f(a):
    return a+2

def g(b):
    return b//7

print(g(f(40))) # 6

# example 2
def z(a):
    return a*3

def f(a):
    return z(a)+6

def g(b):
    return f(b)-4

print(g(44)) # 134
print(f(44)) # 138
print(z(44)) # 132

# example 3
def fun1(n):
    if n<1:
        return 0
    else:
		return fun2(n-1)

def fun2(n):
    if n<5:
        return 4
	else:
		return fun1(n-3)

print(fun2(6)) # 4

'''
fun2(6)
fun1(3)
fun2(2) 
порядок вызова: сверху вниз

скрутка:
fun2(2) вернул 4
fun2(2) родитель для fun1(3) значит fun1(3) вернет 4
fun1(3) родитель для fun2(6) значит fun2(6) вернет 4

fun2(6)-->fun1(3)-->fun2(2)=4
fun2(6)=4 <-- fun1(3)=4 <-- fun2(2)=4

'''

#task напиши функцию, которая примет 2 параметра и вернет их среднее арифметрическое

def avg(a, b):
    return (a + b) / 2

print(avg(6, 8))

'''
print(avg(a = 6, b = 8))
print(avg(6, b = 8))
можно и так
'''

#3. Параметры по-умолчанию
def avg(a = 1, b = 5):
    return (a + b) / 2

print(avg()) # 3
print(avg(2)) # (2+5)/2=3.5
print(avg(6, 8)) # 7
print(avg(b = 10)) # (1 + 10) / 2 = 5.5


#4. Смешанные параметры
# a - обязательный(позиционный) параметр
def avg(a, b = 5):
    return (a + b) / 2

#общий синтаксис 
# def <name>(<positional parameters>, <parameters with default>):
#     <body>
#   ^ 4 spaces

#task напиши функцию, которая примет 3 параметра и вернет их среднее по значению

def f(a, b = 100, c = 1):
    lst1 = [a, b, c]
    lst1.sort()
    return lst1[1]

print(f(10))
print(f(10, 5541, 5)) #тоже можно