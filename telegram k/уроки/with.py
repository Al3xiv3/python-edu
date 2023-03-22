# контекстный менеджер with в связке с файлами
with open('test.txt', 'w') as f: #открыть как f. аналогично f=open(...)
  f.write('hi human')
# в конце сам закроет файл

"""
по факту без with это канон   и понятнее
как без with
"""

try:
  f=open(...)
  1/0
except:
  ...
finally: # в любом случае
  f.close()