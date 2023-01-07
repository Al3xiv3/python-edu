# task
# function for calculate factorial

# def <name>(<params>):
def factorial(n):
    if n <= 0:
        return None

    x = 1
    for i in range(2, n + 1):
        x *= i
    return x


print(factorial(5))  # 120
print(factorial(-5))  # None


# это динамическое решение)

# рекурсия - это вызов функции самой себя

# база факториала
# f(1)=1

# переход
# f(n)=n*f(n-1)

def factorial(n):
    if n <= 0:
        return None

    if n == 1:  # база
        return 1
    return n * factorial(n - 1)


'''
пусть мы хотим f(3)
3 <= 0? нет
3 == 1? нет

вернуть 3*f(2)

вызов f(2)
2 <= 0? нет
2 == 1? нет

вернуть 2*f(1)

вызов f(1)
1 <= 0? нет
1 == 1? да, вернуть 1

теперь скрутка
строка 48 примет вид вернуть 2*1
							  ^ f(2)

строка 42 примет вид вернуть 3*2
							  ^ f(3)                              
итог 6

если проще f(3)=3*f(2)=3*2*f(1)=3*2*1=6
'''