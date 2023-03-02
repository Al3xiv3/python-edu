a = [3, 10, -19, 123, 222, -300]
b = 'hello world'
c = ('hi', 'hello')

"""
a.sort() # только для списков (сортирует по возрастанию)
print(a)
"""
sorted возвращает список
"""
print(sorted(a)) # список
print(sorted(b)) # строка
print(sorted(c)) # картеж
"""
a = sorted(a, reverse=False) #по умолчанию (по возрастанию)
print(a)
a = sorted(a, reverse=True) #по убыванию
print(a)