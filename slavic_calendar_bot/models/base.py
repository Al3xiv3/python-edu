from peewee import *

db = SqliteDatabase('models/users.db')


class Base(Model):
    class Meta:
        database = db


class Calendar(Base):
    username = CharField(unique=True, null=True)
    name = CharField()
    date_of_birth = DateField(null=True)
    zodiac = CharField(null=True)
