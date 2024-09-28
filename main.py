import logging
from aiogram.utils import executor

from  db import db_main
from config import bot, dp, staff
from handlers import commands, fsm_products,fsm_order,send_products

async def on_startup(_):
    for i in staff:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               )
        await db_main.sql_create()

fsm_products.register_fsm_reg(dp)
commands.register_commands(dp)
fsm_order.register_handlers_order(dp)
send_products.register_send_products_handler(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)