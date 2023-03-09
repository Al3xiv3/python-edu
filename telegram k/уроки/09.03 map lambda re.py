# map - отображение. Синтакс: map(<func>, <it_obj>)
# Применяет <func> к !эл-там! <it_obj>. Вернет mapObject
m = map(int, '123')
print(list(m)) # [1, 2, 3]

m = map(int, ['1', '2', '3'])
print(list(m)) # [1, 2, 3]

# В качестве <func> можно и свою функу
def f(x):
    return x+1

m = map(f, [0, 1, 2])
print(list(m)) # [1, 2, 3]

# Task: дан список строк. Сделать список чисел умноженных на 9

s = ['123', '234', '345']

m = list(map(lambda x: int(x) * 9, s))


# Task: дан строка вещественных чисел  разделенными "%". Сделать кортеж  чисел умноженных на сумму цифр целой части

s = '12.2%14.2%12.9'

lst = s.split('%') #  вспомагательный список

def f(p):
  t = 0
  for i in p:
    t += int(i)
  return t

m = tuple(map(lambda x: float(x) * f(x.split('.')[0]), lst))

# рубрика мазохизм
m = tuple(map(lambda x: float(x) * sum(map(int, x.split('.')[0])), lst))


'''
задача с собеса в гугл)

дан словарь дерево папок. Пример
{

}


'''
