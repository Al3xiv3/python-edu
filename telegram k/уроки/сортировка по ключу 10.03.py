# сортировка по ключу
# sorted(iterable, key=func)

lst = ['abb', 'bb', 'avhnb']
print(sorted(lst, key=len))  # отсортирует список по длине элементов (по возрастанию)

print(sorted(lst, key=len, reverse=True))  # reverse=True сортирует список (по убыванию)

print(sorted(lst, key=lambda x: x[0]))  # отсортирует по первому символу (по возрастанию)

print(sorted(lst, key=lambda s: -len(s)))  # отсортирует список по длине элементов (по убыванию)

lst2 = [(1, 5), (4, -1), (2, 4411)]
print(sorted(lst2, key=lambda t: t[0]))

lst3 = [(1, 5, 45), (4, -1, 45), (1, 5, 1)]
print(sorted(lst3, key=lambda t: (
-t[2], t[1])))  # отсортирует список сначала по -t[2] (по убыванию 3 эл), потом по возрастанию 2 эл-ту

tup = (
    [1.4, 1, 50, 84],
    [5411, 540252, -784, -1.767],
    [45, -5, 10.68, -1],
)

# сортани по: первому и третьему по убыванию, второму по возрастанию

print(sorted(tup, key=lambda t: (-t[0], -t[2], t[1])))