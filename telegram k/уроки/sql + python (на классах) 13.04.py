from peewee import *  # pip install peewee <-----------

db = SqliteDatabase('app.db')


class BaseModel(Model):  # Базовый класс для таблиц. Таблицы == модели
    class Meta:
        database = db


class User(BaseModel):  # Таблица User с полем username. Поле id сам создаст
    username = CharField(unique=True)


# Connect to database.
db.connect()

# Create the table.
# db.create_tables([User])
'''
user = User(username='Charlie')
user.save()  # Добавили запись
print(user.id) # 1

в принт аналог
SELECT id FROM User WHERE username='Charlie'

user = User(username='Вася')
user.save()  # Добавили запись
print(user.id) # 2

user = User(username='Петя')
user.save()  # Добавили запись
print(user.id) # 3
'''
_id = User.get(User.username == 'Charlie').id  # Получим Id  для Charlie
# Да но тут у нас нет user  Так получаем только одну запись

for user in User.select():
    print(user.username)

print("-"*30)
# where https://www.tutorialspoint.com/peewee/peewee_filters.htm
rows = User.select().where(User.username.contains('я'))

for user in rows:
    print(user.username)
