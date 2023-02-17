x = int(input('Введите число: '))

kol = 0
kol_ch = 0
maximum = 0
minimum = 9
summ = 0
pr = 1
while x > 0:
    last = x % 10
    kol = kol + 1
    if last % 2 == 0:
        kol_ch = kol_ch + 1
    if last > maximum:
        maximum = last
    if last < minimum:
        minimum = last
    summ = summ + last
    pr = pr * last
    x = x // 10

print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)
print('Наибольшая цифра:', maximum)
print('Наименьшая цифра:', minimum)
print('Сумма цифр числа:', summ)
print('Произведение цифр числа:', pr)

