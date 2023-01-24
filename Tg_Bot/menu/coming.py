from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from ..bot import bot, dp
from ..decors import admin
from ..states import AddComing, AddExpenditure
from ..keyboards import kbd
from DB import ComingDb, SessionDb
import traceback


@dp.callback_query_handler(text='coming')
@admin
async def coming(cq: CallbackQuery, state:FSMContext):
    msg = cq.message
    user_id = msg.chat.id
    await state.update_data(page=0)
    await bot.edit_message_text(chat_id=user_id, message_id=msg.message_id, text='Выбери продукт:', reply_markup=kbd.all_products())
    await AddComing.product.set()


@dp.callback_query_handler(Text(startswith='select_product_'), state=AddComing.product)
@admin
async def select_product_(cq: CallbackQuery, state: FSMContext):
    msg = cq.message
    user_id = msg.chat.id
    product = cq.data.split('select_product_')[1]
    await state.update_data(product=product, msg=msg)
    await bot.edit_message_text(chat_id=user_id, message_id=msg.message_id, text='Введи количество:', reply_markup=kbd.single_back())
    await AddComing.next()


@dp.message_handler(state=AddComing.count)
@admin
async def count(msg: Message, state: FSMContext):
    user_id = msg.chat.id
    count = msg.text
    await bot.delete_message(chat_id=user_id, message_id=msg.message_id)
    data = await state.get_data()
    try:
        count = float(count)
        com = ComingDb(user_id=user_id, product =data['product'], count = count)
        SessionDb.add(com)
        SessionDb.commit()
        await bot.edit_message_text(chat_id=user_id, message_id=data['msg'].message_id, text='Приход записан.', reply_markup=kbd.all_products(page=data['page'] if 'page' in data.keys() else 0))
        await AddComing.product.set()
    except:
        await bot.edit_message_text(chat_id=user_id, message_id=data['msg'].message_id,  text=f'Неверный формат. "{msg.text}" - не число', reply_markup=kbd.single_back())


@dp.callback_query_handler(Text(startswith='replace_page_'), state=[AddComing.product, AddExpenditure.product])
@admin
async def replace_page_(cq: CallbackQuery, state:FSMContext):
    msg = cq.message
    user_id = msg.chat.id
    page_new = int(cq.data.split('replace_page_')[1])
    await state.update_data(page=page_new)
    await bot.edit_message_reply_markup(chat_id=user_id, message_id=msg.message_id, reply_markup=kbd.all_products(page=page_new))
