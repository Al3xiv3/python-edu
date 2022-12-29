"""
вводят n, затем  n чисел, вывести  числа без дублей
"""

n = int(input())
lst1 = list()

for i in range(n):
    x = int(input())
    if x not in lst1:
        lst1.append(x)
for e in lst1:
    print(e)
