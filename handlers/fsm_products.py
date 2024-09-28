from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import staff
from db import db_main


class FSMProduct(StatesGroup):
    name_product = State()
    category_product = State()
    size_product = State()
    price_product = State()
    product_id = State()
    photo_product = State()


async def start_reg(message: types.Message):
    if message.from_user.id not in staff:
        await message.answer("У вас нет доступа к этой команде.")
        return

    await message.answer('Введите название товара:')
    await FSMProduct.name_product.set()


async def name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text
        await message.answer('Введите категорию товара:')
    await FSMProduct.next()

async def category_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category_product'] = message.text
        await message.answer('Введите размер товара:')
    await FSMProduct.next()

async def size_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size_product'] = message.text
        await message.answer('Введите цену товара:')
    await FSMProduct.next()

async def price_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_product'] = message.text
        await message.answer('Введите артикул товара:')
    await FSMProduct.next()

async def product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text
        await message.answer('Добавьте фото товара:')
    await FSMProduct.next()


async def photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

        await message.answer_photo(photo=data['photo'],
                                   caption='Ваш товар\n\n'
                                           f'Название товара: {data["name_product"]}\n'
                                           f'Категория товара: {data["category_product"]}\n'
                                           f'Размер товара: {data["size_product"]}\n'
                                           f'Стоимость: {data["price_product"]}\n'
                                           f'Артикул товара: {data["product_id"]}\n'
                                   )

        await db_main.insert_products(
            name_product=data['name_product'],
            category_product=data['category_product'],
            size_product=data['size_product'],
            price_product=data['price_product'],
            product_id=data['product_id'],
            photo=data['photo']
        )
        await message.answer('Отлично, данные в базе!')
        await state.finish()


def register_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(start_reg, commands=['product_add'], state=None)
    dp.register_message_handler(name_product, state=FSMProduct.name_product)
    dp.register_message_handler(category_product, state=FSMProduct.category_product)
    dp.register_message_handler(size_product, state=FSMProduct.size_product)
    dp.register_message_handler(price_product, state=FSMProduct.price_product)
    dp.register_message_handler(product_id, state=FSMProduct.product_id)
    dp.register_message_handler(photo, state=FSMProduct.photo_product,
                                content_types=['photo'])
