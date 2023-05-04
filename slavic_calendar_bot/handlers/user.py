from aiogram import types,  Dispatcher
from aiogram.dispatcher import filters
from magic_filter import F

from create_bot import dp, bot
from keyboards.button import keyboard_button_user
from models.base import Calendar
from models.base import db

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        db.connect()
        query = Calendar.select().where(Calendar.name == message.from_user.first_name)
        if not query.exists():
            user = Calendar.create(name=message.from_user.first_name)
            if message.from_user.username is not None:
                user.username = message.from_user.username
            user.save()
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! \n'
f'Введи дату рождения (нажми на кнопку).', reply_markup=keyboard_button_user)
        await message.delete()
    except Exception as e:
        print(e)
    finally:
        db.close()

@dp.message_handler(F.text == 'Дата рождения')
async def command_date(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Введи дату рождения')
        await message.delete()
    except:
        await message.reply('Дата введена')


@dp.message_handler(filters.Regexp(r"(\d+.\d+.\d+)"))
async def regexp_example(message: types.Message):
    try:
        lst = list(map(int, message.text.split('.')))
        if 1 <= lst[0] <= 31 and 1 <= lst[1] <= 12 and 1923 <= lst[2] <= 2023:
            db.connect()
            query = Calendar.update(date_of_birth=message.text).where(Calendar.name == message.from_user.first_name)
            query.execute()
            await message.answer('Дата введена')
        else:
            await message.answer('Введите корректную дату рождения в формате дд.мм.гггг')
    except Exception as e:
        print(e)
    finally:
        db.close()


@dp.message_handler(F.text == 'Знак зодиака')
async def zodiac_handler(message: types.Message):
    try:
        db.connect()
        query = Calendar.select().where(Calendar.name == message.from_user.first_name)
        date = None
        for r in query:
            date = r.date_of_birth
        day, month, year = map(int, date.split('.'))
        zodiac = get_zodiac(month, day)
        query = Calendar.update(zodiac=zodiac).where(Calendar.name == message.from_user.first_name)
        query.execute()
        await message.answer(zodiac)
    except Exception as e:
        print(e)
    finally:
        db.close()


def get_zodiac(month, day):

    if month == 12:
        astro_sign = 'Стрелец' if (day < 22) else 'Козерог'
    elif month == 1:
        astro_sign = 'Козерог' if (day < 20) else 'Водолей'
    elif month == 2:
        astro_sign = 'Водолей' if (day < 19) else 'Рыбы'
    elif month == 3:
        astro_sign = 'Рыбы' if (day < 21) else 'Овен'
    elif month == 4:
        astro_sign = 'Овен' if (day < 20) else 'Телец'
    elif month == 5:
        astro_sign = 'Телец' if (day < 21) else 'Близнецы'
    elif month == 6:
        astro_sign = 'Близнецы' if (day < 21) else 'Рак'
    elif month == 7:
        astro_sign = 'Рак' if (day < 23) else 'Лев'
    elif month == 8:
        astro_sign = 'Лев' if (day < 23) else 'Дева'
    elif month == 9:
        astro_sign = 'Дева' if (day < 23) else 'Весы'
    elif month == 10:
        astro_sign = 'Весы' if (day < 23) else 'Скорпион'
    elif month == 11:
        astro_sign = 'Скорпион' if (day < 22) else 'Стрелец'
    return astro_sign


@dp.message_handler(F.text == 'Таблица участников')
async def zodiac_handler(message: types.Message):
    try:
        db.connect()
        query = Calendar.select()
        s = ''
        for r in query:
            s = s + str(r.id) + '. ' + str(r.name) + ', ' + '@' + str(r.username) + ', ' + str(r.date_of_birth) + ', ' + str(r.zodiac) + '\n'
        await message.answer(s)
    except Exception as e:
        print(e)
    finally:
        db.close()


def register_handlers_user(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])



