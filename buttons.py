from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)




info_button = KeyboardButton('info')
start.add( info_button)