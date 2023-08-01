from aiogram import Bot, types
from create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

from data_base import sqlite_db



inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='читать', callback_data='www'))

@dp.message_handler(commands='test')
async def test_commands(message : types.Message):
    await message.answer('СТАТЬИ ДЛЯ МУЖЧИН')
    await sqlite_db.sql_read(message)

# @dp.callback_query_handler(text='www')
# async def www_call(callback: types.CallbackQuery):
#     await callback.message.answer('нажата кнопка')
#     await callback.answer()
    
@dp.callback_query_handler(text='www')
async def www_call(message: types.CallbackQuery):
    await sqlite_db.sql_read_full_text(message)


# #Кнопки ссылки
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='ссылка', url='https://www.menslife.com/')
urlButton2 = InlineKeyboardButton(text='ссылка2', url='https://mensby.com/')
urlkb.add(urlButton, urlButton2)

@dp.message_handler(commands='ssilki')
async def url_commands(message : types.Message):
    await message.answer('Ссылочки', reply_markup=urlkb)
#==================================