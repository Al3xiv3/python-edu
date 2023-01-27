# вводится строка. Перевернуть её. пример: test -> tset

string = input()

print(string[::-1])  # [0: len(string): -1]

# вводится строка. Проверка на палиндром. пример: assa -> True; fds -> False

string = input()

# 1 способ
if string[::-1] == string:
    print(True)
else:
    print(False)

# 2 способ
string = input()

print(string[::-1] == string)

# вводим числа n, m. Возвести минимальное из них в степень максимального

# 1 способ
n = int(input())
m = int(input())

if n > m:
    print(m ** n)
else:
    print(n ** m)

# 2 способ
n = int(input())
m = int(input())

print(min(n, m) ** max(n, m))

# вводим числа n, m. Выдать сумму чисел между ними, не гарантируется порядок ввода

n = int(input())
m = int(input())

print(sum(range(min(n, m) + 1, max(n, m))))

#2 способ

n = int(input())
m = int(input())
x = 0

for i in range(min(n, m) + 1, max(n, m)):
    x += i

print(x)
