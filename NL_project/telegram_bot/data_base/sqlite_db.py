import sqlite3 as sq
import types 
from create_bot import dp, bot
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def sql_start():
    global base, cur
    base = sq.connect('C:/Users/NickT/Desktop/PY_code/site/NL_project/db.sqlite3')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.commit()

#--------------------------заполняем базу данных--------------------------
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO news_articles (title, anons, full_text) VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()

#--------------------------выводим содержимое базы---------------------------------
#заголовки статей
async def sql_read_title(message):
    for ret in cur.execute('SELECT * FROM news_articles').fetchall():
        inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text=ret[1], callback_data='RFT {ret[2]}'))
        await bot.send_message(message.from_user.id, f'ID статьи - ' + (str(ret[0])), reply_markup=inkb)
        print(ret[0], ret[1])

#текст статей
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('RFT '))
async def sql_read_full_text(message: types.CallbackQuery):
    for ret in cur.execute('SELECT * FROM news_articles WHERE title == (?)').fetchall():
        await bot.send_message(message.from_user.id, ret[2])

#--------------------------удаление статей--------------------------        
async def sql_read2():
    return cur.execute('SELECT * FROM news_articles').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM news_articles WHERE title == (?)', [data])
    base.commit()