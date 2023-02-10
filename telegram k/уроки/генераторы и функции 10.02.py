# функция принимает n, m. вернуть сумму простых чисел между ними

def simple(y):
    for i in range(2, int(y ** 0.5) + 1):
        if y % i == 0:
            return False
    return True


def simple_sum(n, m):
    if n > m:
        n, m = m, n
    s = 0
    for x in range(n, m + 1):
        if simple(x):
            s += x
    return s


# sum(x for x in range(n, m + 1) if simple(x))  в 1стр =)
# для х в  диапозоне ... если оно простое, то добавить к сумме

# генераторы списков
# task1 сделать список квадратов от 0 до 200

# способ1
def list_square_long():
    ls = []
    for i in range(0, 201):
        t = i ** 2
        ls.append(t)
    return ls


# способ2
def list_square_short():
    return [i ** 2 for i in range(0, 201)]


# [<что класть> for ...]


# task2 сделать список четных от 0 до 200


# способ1
def list_chetnih():
    ls = []
    for i in range(0, 201):
        if i % 2 == 0:
            ls.append(i)
    return ls


# способ2
def list_chetnih_short():
    return [i for i in range(0, 201) if i % 2 == 0]


# [<что класть> for ... if ...]
# читается    для ... если ..., то клади в список <что класть>

# task3 сделать список пар из l1 l2
l1 = [1, 2, 3, 6, 10, 54, 0, 47]
l2 = [4, 5, 6, 5, 85, 89, 9, 8]

# [(1, 4), (2, 5), (3, 6), ...]

# способ 1 (короткий)
l3 = [(l1[i], l2[i]) for i in range(0, len(l1))]

# способ 2 (длинный)
l3 = []
for i in range(0, len(l1)):
    t = (l1[i], l2[i])
    l3.append(t)

# task4 сделать список пар из l1 l2 по закону  l1[i]*8, l2[i]-4  если l2[i] четно
l1 = [1, 2, 3, 6, 10, 54, 0, 47]
l2 = [4, 5, 6, 5, 85, 89, 9, 8]
# [(8, 0), (24, 2), (47*8, 4)]
l3 = []

for i in range(0, len(l1)):
    if l2[i] % 2 == 0:
        t = (l1[i] * 8, l2[i] - 4)
        l3.append(t)

l3 = [(l1[i] * 8, l2[i] - 4) for i in range(0, len(l1)) if l2[i] % 2 == 0]

# генераторы словарей
# {ключ : значение for ... if ...}

# task5 сделать словарь, ключ из l1, значение из l2

# способ 1
l1 = [1, 2, 3, 6, 10, 54, 0, 47]
l2 = [4, 5, 6, 5, 85, 89, 9, 8]

d = dict()

for i in range(0, len(l1)):
    d[l1[i]] = l2[i]  # d[key] = val
print(d)

# print(d) {1: 4, 2: 5, 3: 6, 6: 5, 10: 85, 54: 89, 0: 9, 47: 8}


# способ 2
l1 = [1, 2, 3, 6, 10, 54, 0, 47]
l2 = [4, 5, 6, 5, 85, 89, 9, 8]

d = {l1[i]: l2[i] for i in range(0, len(l1))}

print(d)
# print(d) {1: 4, 2: 5, 3: 6, 6: 5, 10: 85, 54: 89, 0: 9, 47: 8}