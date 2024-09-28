from aiogram import types, Dispatcher
import os.path
from buttons import start
from config import bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f"Здравствуйте {message.from_user.full_name}",
                           reply_markup=start,)
async def info_command(message: types.Message):
    await message.answer(f"в этом боте вы можете заказать товары\n"
                         f"используйте команды '/products', чтобы посмотреть все товары"
                         f"для заказа используйте команду"
                         )

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_command, commands=['info'])
