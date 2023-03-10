# ввод числа p, является ли оно простым  (ФУНКЦИЯ)

def f(p):
  for i in range(2, int(p ** (1 / 2)) + 1):
    if p % i == 0: #  если кратно, то не простое 
       return False # return выходит из функций 
  return True

"""
а теперь оптимизация 

предстааввь огромное простое число 
2**23-1 вродь

будет долго

распишем делители 25
1 5 25
  ^
распишм делители 100
1 2 4 5 10 20 25 50 100
        ^
1*100
2*50
4*25
5*20
10*10

10
1 2 5 10
   ^
10**0.5=3....

"""