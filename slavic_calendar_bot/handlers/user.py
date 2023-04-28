from aiogram import types,  Dispatcher
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

@dp.message_handler(commands=['Дата рождения'])
async def command_date(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Введи дату рождения')
        await message.delete()
    except:
        await message.reply('Дата введена')

def register_handlers_user(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])



