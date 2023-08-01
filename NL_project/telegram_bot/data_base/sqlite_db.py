import sqlite3 as sq
import types 
from create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def sql_start():
    global base, cur
    base = sq.connect('C:/Users/NickT/Desktop/PY_code/site/NL_project/db.sqlite3')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.commit()

#заполняем базу данных
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO news_articles (title, anons, full_text) VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()

#выводим содержимое базы
#заголовки статей
async def sql_read_title(message):
    for ret in cur.execute('SELECT * FROM news_articles').fetchall():
        inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text=ret[1], callback_data='www'))
        await bot.send_message(message.from_user.id, f'ID статьи - ' + (str(ret[0])), reply_markup=inkb)
        print(ret[0], ret[1])

#текст статей
@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    for ret in cur.execute('SELECT id FROM news_articles').fetchone():
        await bot.send_message(chat_id=callback_query.from_user.id, text=ret[0])

# async def sql_read_full_text(message):
#     for ret in cur.execute('SELECT * FROM news_articles').fetchall():
#         inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='следующая', callback_data='www'))
#         await bot.send_message(message.from_user.id, ret[2], reply_markup=inkb)
        
