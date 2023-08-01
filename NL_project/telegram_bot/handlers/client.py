from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db
from keyboards.buttons import urlkb, inkb



# @dp.message_handler(commands=['Articles', 'Статьи'])
async def command_articles(message: types.Message):
    await bot.send_message(message.from_user.id, "СТАТЬИ ДЛЯ МУЖЧИН")
    await sqlite_db.sql_read_title(message)
    # await message.answer(f"СТАТЬИ ДЛЯ МУЖЧИН", reply_markup=inkb)
    

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_articles, commands=['Articles', 'Статьи'])