'''
дз

№1
напишите ф-ию,  котрая вернет список из первой буквы слов
пример 'hi world guy' => ['h', 'w', 'g']

№2
напишите ф-ию,  котрая вернет МАКС кол-во подряд идущих ЛОМ
пример 'ЛОМЛОМГОЛОМПОЛОМЛОМЛОМ' => 3
'''


def f(n):
  n = n.split()
  lst_1 = []
  for i in n:
    s = i[0]
    lst_1.append(s)
  return lst_1

print(f("leoeod eodo doo"))

