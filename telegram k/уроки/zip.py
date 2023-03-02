a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = 'abcde'

"""
for i in range(5):
    print(a[i], b[i]) #если в одном из списков меньше эл-тов чем в рендж- выдаст ошибку
"""
"""
rez = zip(a, b)
print(rez) #zip object
"""
'''
rez = zip(a, b)
print(list(rez)) #список картежей, если в одном из списков меньше эл-тов чем в рендж- берет по наим. знач
'''
"""
rez = list(zip(a, b, c)) #можно добавлять больше итнрабельных объектов
print(rez)
"""
"""
for t1, t2, t3 in zip(a, b, c):
    print(t1, t2, t3)
"""
rez = zip(a, b, c)

col1, col2, col3 = zip(*rez)

print(col1, col2, col3) #получить списки обратно. * выполняет распаковку элемента