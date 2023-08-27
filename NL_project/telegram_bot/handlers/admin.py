from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from create_bot import bot, dp
from data_base import sqlite_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.buttons import urlkb, kb_client_admin



class FSMAdmin(StatesGroup):
    title = State()
    anons = State()
    full_text = State()
    # date = State()
    
ID = None

#получаем ID текущего модератора
# @dp.message_handler(commands='moderator', is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяит надо?', reply_markup=kb_client_admin)
    # await message.delete()


#начало загрузки статьи
# @dp.message_handler(commands='DWNLD', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.title.set()
        await message.reply('Название статьи')

# выход из машино-состояний(состояний загрузки)
# @dp.message_handler(commands='отмена', state="*")
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Отмена создания статьи!')

#вводим название статьи
# @dp.message_handler(content_types=['text'], state=FSMAdmin.title)
async def load_title(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['title'] = message.text#.file_id
            await FSMAdmin.next()
            await message.reply('Анонс статьи')

#вводим анонс статьи
# @dp.message_handler(content_types=['text'], state=FSMAdmin.anons)
async def load_anons(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['anons'] = message.text
            await FSMAdmin.next()
            await message.reply('Текст статьи')

#вводим текст статьи
# @dp.message_handler(content_types=['text'], state=FSMAdmin.full_text)
async def load_full_text(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['full_text'] = message.text
            # await FSMAdmin.next()
            # await message.reply('Дата публикации статьи')
        await sqlite_db.sql_add_command(state)
        await state.finish()

# #вводим дату
# # @dp.message_handler(content_types=['text'], state=FSMAdmin.date)
# async def load_date(message: types.Message, state: FSMContext):
#     if message.from_user.id == ID:
#         async with state.proxy() as data:
#             data['date'] = message.text            
#         await sqlite_db.sql_add_command(state)
#         await state.finish()

# удаление статьи
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)

# @dp.message_handler(commands='DLT')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_message(message.from_user.id, f'{ret[1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить', callback_data=f'del {ret[1]}')))



#регистрация хендлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['DWNLD'], state=None)
    dp.register_message_handler(delete_item, commands=['DLT'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_title, content_types=['text'], state=FSMAdmin.title)
    dp.register_message_handler(load_anons, content_types=['text'], state=FSMAdmin.anons)
    dp.register_message_handler(load_full_text, content_types=['text'], state=FSMAdmin.full_text)
    # dp.register_message_handler(load_date, content_types=['text'], state=FSMAdmin.date)
    dp.register_message_handler(make_changes_command, commands='moderator', is_chat_admin=True)