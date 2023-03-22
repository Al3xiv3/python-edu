#файлы 
#синтаксис: open(path_to_file, mode) путь или абсолютный или относительно файла питона
f = open('file.txt', 'w') # откроет на запись (w - write) file.txt около файла-скрипта. Если файл не существует, он создастся. Если в файле что-то есть, оно удалится
f.write('hi') # пишем hi в файл
f.close() # закроем файл

# теперь считаем
f = open('file.txt', 'r') # откроет на чтение (r - read) file.txt около файла-скрипта. Если файл не существует, будет ошлибка
s = f.readline() # читаем 1ю строку
print(s)
f.close() # закроем файл 

f = open('file.txt', 'a') # откроет на добавление (a - append) file.txt около файла-скрипта. Если файл не существует, он создастся. Если в файле что-то есть, новое добавится в конец
f.write(' world') # пишем world в файл
f.close() # закроем файл

# задача: в файл  task1.txt вписать своё имя на английском, и вывести "я - {имя}". Без  скобок

f = open('task1.txt', 'w')
f.write('Alexander')
f.close()

f = open('task1.txt', 'r')
s = f.readline() # читаем 1ю строку
f.close() 
print('я -', s)

# задача: в файл  task2.txt вписать 2 числа через пробел, и вывести их сумму

f = open('task2.txt', 'w')
f.write('2 2')
f.close()

f = open('task2.txt', 'r')
s = f.readline() # читаем 1ю строку
f.close()
print(sum(map(int, s.split())))


# кодировка файла. По умолчанию питон не  видит кирилицу, Для этого используется кодировка  utf8
#синтаксис: open(path_to_file, mode, encoding)   при передачи кодировки лучше явно указать этот аргумент

# пример
#f = open("file.txt", "r", encoding="utf8")

# задача: в файл  task3.txt вписать своё имя на русском, и вывести "я - {имя}". Без  скобок

f = open('task3.txt', 'w', encoding="utf8")
f.write('Александр')
f.close()

f = open('task3.txt', 'r', encoding="utf8")
s = f.readline() # читаем 1ю строку
f.close() 
print('я -', s)
