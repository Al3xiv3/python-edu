from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('Дата рождения')
b2 = KeyboardButton('Поделиться номером', request_contact=True)
b3 = KeyboardButton('Отправить где я', request_location=True)


keyboard_button_user = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

keyboard_button_user.add(b1).row(b2, b3)
