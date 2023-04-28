for i in range(7):
    for j in range(7):
        print(i, j)

'''
для каждого i j пробегает от 0 до 6
0 0
0 1
0 2
...
0 6
1 0
1 1
1 2
1 3
...
6 6
'''

for letter in 'abc':
    for j in range(2):
        print(letter, j)

"""
a 0
a 1
b 0
b 1
c 0 
c 1
"""

for letter in 'a':
    for j in range(2):
        for num in [1, 4.1, -74]:
            print(letter, j, num)

"""
a 0 1
a 0 4.1
a 0 -74
a 1 1
a 1 4.1
a 1 -74
"""