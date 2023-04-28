import sqlite3 # Встроеннный модуль

connection = sqlite3.connect('mydatabase.db') # Подключение к бд

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM Table_1""")

data = cursor.fetchall()

for record in data:
    print(record)
connection.commit() # Применение запроса