"""дана строка.вывести часто встречаемый символ
если их несколько, вывести их все"""
"""
str1 = 'aaaa cc bb dddd'
counter = 0
empty_str = ''
for i in range(len(str1)):
    if str1.count(str1[i]) >= counter:
        counter = str1.count(str1[i])
        empty_str = str1[i]
print(empty_str)
"""


str1 = 'aaaa cc bb dddd'
d = dict()
m = 0

for i in str1:
    d[i] = d.get(i, 0) + 1
    m +=

print(d)

print(m)

x = max(d.items())

print(x)
