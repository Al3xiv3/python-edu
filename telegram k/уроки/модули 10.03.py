# модуль - совокупность функ, классов, переменных

# рассмотрим модуль math
import math

print(math.sqrt(16)) # корень 16
print(math.pi) # число пи 
print(math.e) # число e
# еще больше тут https://www.w3schools.com/python/module_math.asp

# также можно 
from math import sqrt, pi, floor

print(sqrt(16)) # то бишь без math. но другие не доступны
print(pi)
print(floor(2.56)) # 2  округл.вниз (пол)


# рассмотрим модуль random
import random # https://www.w3schools.com/python/module_random.asp

print(random.randint(1, 1000)) #случайное целое число от 1 до 1000

lst = [1, 44, 545, 4512]
print(random.choises(lst, k=2)) #выбор двух эл-тов списка 

# задача: заполнить список случайным количеством  чисел и сами числа в диапозоне [4, 1000]

import random

lst = []
kolvo = random.randint(1, 10)

for i in range(1, kolvo + 1):
    random_num = random.randint(4, 1000)
    lst.append(random_num)
print(lst)

print([random.randint(4, 1000) for i in range(1, kolvo + 1)])

# задача: заполнить словарь случайным количеством  чисел и сами числа в диапозоне [4, 1000]

import random

dikiy = dict()
kolvo = random.randint(1, 10)

for i in range(1, kolvo + 1):
    random_num = random.randint(4, 1000)
    dikiy[i]= random_num
print(dikiy)
