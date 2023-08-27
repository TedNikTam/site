from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db
from keyboards.buttons import urlkb, kb_client


# @dp.message_handler(commands='start')
async def start_commands(message : types.Message):
    await message.answer('Приветствую!', reply_markup=kb_client)

# @dp.message_handler(commands=['Articles', 'Статьи'])
async def command_articles(message: types.Message):
    await bot.send_message(message.from_user.id, "СТАТЬИ ДЛЯ МУЖЧИН")
    await sqlite_db.sql_read_title(message)
    
    
@dp.callback_query_handler(text='www')
async def www_call(message: types.CallbackQuery):
    await sqlite_db.sql_read_full_text(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_commands, commands=['start'])
    dp.register_message_handler(command_articles, commands=['Articles', 'Статьи'])