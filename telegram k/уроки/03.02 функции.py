"""Напишите функцию, которая принимает целочисленные значения часов (hours) и минут (minutes),
конвертирует эти значения в секунды, а затем суммирует и возвращает в качестве результата."""

def seconds(hours, minutes):
    sec = (hours * 60 * 60) + (minutes * 60)
    return sec

print(seconds(1, 30))

"""Напишите функцию, которая принимает количество побед, ничейных игр и поражений
и возвращает количество очков, которая набрала команда."""

def points(w, d, l):
    w = w * 3
    d = d * 1
    l = 0
    p = w + d + l
    return p
print(points(3,2,1))

'''Напишите функцию, которая принимает число number, 
и возвращает слово Google с количеством букв o, равным number.'''

def word(number):
    return "G" + 'o' * number + 'gle'

print(word(4))

'''Напишите функцию, которая высчитывает размер прибыли по заданным параметрам cost_price (себестоимости)
и sales_price (цена товара). Функция должна вернуть результат в процентах в виде строке.'''

def margin(cost_price, sales_price):
    mar = ((sales_price - cost_price) / sales_price) * 100
    return round(mar, 1)

print(margin(28, 39))