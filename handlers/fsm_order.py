from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import staff



class FSMorder(StatesGroup):
    id = State()
    size = State()
    quantity = State()
    contact = State()



async def start_order(message: types.Message):
    await FSMorder.id.set()
    await message.answer("Введите артикул товара:")


async def id_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_product'] = message.text
    await FSMorder.next()
    await message.answer("Введите размер товара:")



async def size_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await FSMorder.next()
    await message.answer("Введите количество товара:")



async def quantity_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text
    await FSMorder.next()


    await message.answer("Введите ваш номер телефона:")


async def contact_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text

    await message.answer(f"Заказ принят! Детали:\n"
                         f"Артикул: {data['id_product']}\n"
                         f"Размер: {data['size']}\n"
                         f"Количество: {data['quantity']}\n"
                         f"Телефон: {data['contact']}")

    for user_id in staff:
        try:
            await message.bot.send_message(user_id, f"Новый заказ!\n"
                                                    f"Артикул: {data['id_product']}\n"
                                                    f"Размер: {data['size']}\n"
                                                    f"Количество: {data['quantity']}\n"
                                                    f"Телефон: {data['contact']}")
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")

    await state.finish()


def register_handlers_order(dp: Dispatcher):
    dp.register_message_handler(start_order, commands=['order'], state=None)
    dp.register_message_handler(id_order, state=FSMorder.id)
    dp.register_message_handler(size_order, state=FSMorder.size)
    dp.register_message_handler(quantity_order, state=FSMorder.quantity)
    dp.register_message_handler(contact_order, state=FSMorder.contact)
