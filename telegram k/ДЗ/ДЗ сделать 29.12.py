"""
вводят n, затем  n чисел, вывести  числа без дублей
"""

n = int(input())
s = set()

for i in range(n):
    x = int(input())
    s.add(x)
for e in s:
    print(e)
