#напишите функцию которую вернет квадрат n

def f(n):
  return n ** 2
#GOOD)

#напишите функцию fun, которая принимает строку (имя) и вернет приветствие
#fun('sasha') => 'hi, sasha'
#название  параметр
def fun(name):
  return 'hi,' + name

'''
дан список, вывести длину
'''
x = [8, 45]
x.append(7)
x += [1, 4] 
 #           /
# [8, 45, 7, 1, 4]

print(len(x)) # 5

t =x.pop()
'''удалит 4
t=4 
pop удалит последний и возращает его'''

print(x.index(1)) #что даст? 3?+  это только для нас есть отриц индексы)
print(x.index(10)) # если нету даст -1
print(x.index(4)) #4


#f-strings
name = "ilya"
greet = f"hi, {name}" #hi, ilya

#так просто) с питон 3,6 можно


name = "ilya"
age=18
from_ = "rus"
greet = f"hi, {name}. {age} y.o. From {from_}" # УДОБНЕЕ

greet = 'hi,' + name + '.' + str(age) + 'y.o.' + 'From' + from_

#напишите функцию fun, которая принимает строку (имя) и вернет приветствие. f-строка 
#fun('sasha') => 'hi, sasha'
#название  параметр
def fun(name):
  return f"hi, {name}"
#=)

#.split()
s = 'oookuuf'
print(s.split('ku')) #['ooo', 'uf']
#делит по символу/группе символов 
#если без параметра, делит по пробелам

#                V два пробела
s = 'hi sasha and  ilya'
print(s.split()) #['hi', 'sasha', 'and', 'ilya']


#                V два пробела 
s = 'hi sasha and  ilya'                   # V пробел  <=
print(s.split(' ')) #['hi', 'sasha', 'and', ' ilya']


"""
задача
вводим строку и делим по пробелу
"""
s = input()
print(s.split())

#2 способ
s = input().split() #в s list
print(s)
#вводим и сразу делим

"""
задача
вводим строку и делим по пробелу и выводим построчно

пример ввода
привет медвед

вывод 
привет
медвед
"""
# ввод
s = input()

# делим по пробелу
lst = s.split()

# выводим построчно
for word in lst: # в word слово
  print(word)

# решение в 3 этапа

print(*input().split(), sep='\n')
#;)

# смотри
print("hi", 'ilya0', 189, sep='-') #hi-ilya0-189
#между ними -
# по умолчанию sep=' '
# пробел

'''
	map
  
синтаксис
	map(function, collection)

применяет function к эл-там collection
'''

#example
lst = ['20', '867']
m = map(int, lst) # m - map object

lst2 = list(m) # lst2 = [20, 867]

# можно любую функцию, даже свою

# напиши подробнее что значит map object, это не переменная просто? 
# нет, это особая структура. Пожожа на кортеж, но без индексов, там эл-ты хранятся по-особенному


#unpacking  (распаковка)
# пусть есть список.
lst = [12, 234, 23.2, '123']

# теперь например я не хочу обращаться по индексам 
a, b, c, d = lst # a = 12, b = 234, c = 23.2, d = '123'

# распаковка в for
# пусть дан список кортежей из 2х эл-тов.
lst = [(8, 2), (54, 6890), (87, -44.12)]

'''
for t in lst: # в t кортежи из 2х эл-тов
'''

for a, b in lst:
  print(a, b)

'''
вывод
8 2
54 6890
87 -44.12
'''

'''
задача
дан словарь. вывести в форме ключ значение 

пример
дано
{"name":"sasha", "from":"russia"}

вывод
name sasha
from russia
'''

#задаем словарь.
d = {"name":"sasha", "from":"russia", "age":25}

#.items()
#возвращает список кортежекй (ключ, значение)

for a, b in d.items():
  print(a, b)
