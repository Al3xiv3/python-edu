# write f function. Give four args and returns average min and max (average - ср. арифметическое) 
def avg(x, y):
    '''average of x, y'''
    return (x + y) / 2


def f(a, b, c, d):
    lst1 = [a, b, c, d]
    return avg(min(lst1), max(lst1))


# написать функу f2. принимает 2 параметра n, base. перевод n (из 10сс) в сист. счисления base
"""пример первести 4 в 2сс
y=''

4%2+y=0+''='0'
4//2=2
2%2+y=0+'0'='00'
2//2=1
1%2+y=1+'00'='100'
1//2=0

остатки 0 0 1
        <------ справа налево 100
4_10 = 100_2
  ^        ^  основание СС"""


def f2(n, base):
    y = ''  # сначала пусто

    while n != 0:
        y = str(n % base) + y  # всё, думай почему
        n = n // base
    return y