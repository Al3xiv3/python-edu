# map
# дан список строк-чисел. преобразовать в  int
# способ 1 (цикл)

a = ['123', '234', '345']
c = []

for i in a:
    c.append(int(i))

a = ['123', '234', '345']
c = [int(i) for i in a]

# способ 2 (map)

# map(func, iter)  применяет func к эл-там iter. вернет mapObject
a = ['123', '234', '345']
b = list(map(int, a))  # лист меняет mapObject в список

# lambda, лямбда функции (анонимные)
a = lambda: print('anonim')  # обьявление функи
a()  # выведит  anonim

b = lambda x: print(x + 5)
b(556341)  # 556346

b = lambda x, y: print(x + y)
c = b(55, 1)  # вывод 56   c=None

b = lambda x, y: x + y  # вернет не None, а сумму
c = b(55, 1)  # c=56
print(c)
# 56

# дан список строк-чисел. преобразовать в  int в 2р больших
# в мап можно свои функи

a = ['123', '234', '345']

b = list(map(lambda x: int(x) * 2, a))

# дан список кортежей. увеличить на 10 второй элемент

a = [(5, 4), (10, 54141), (15, 14)]

b = list(map(lambda x: (x[0], x[1] + 10), a))
print(b)

# дан словарь, ключи которого слова. сделать первую букву заглавной

a = {'key': 'value', 'word': 'word2'}
p = lambda x: (x[0].capitalize(), x[1])
b = dict(map(p, a.items()))  # кортежи (ключ, значение)
print(b)