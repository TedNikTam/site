from aiogram import Bot, types
from create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



btn1 = KeyboardButton('/Articles')
btn2 = KeyboardButton('/Weather')
btn3 = KeyboardButton('/DWNLD')
btn4 = KeyboardButton('/DLT')
btn5 = KeyboardButton('/start')



kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(btn1, btn2)
kb_client_admin.row(btn3, btn4, btn5)


# inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='читать', callback_data='www'))

# #Кнопки ссылки
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='ссылка', url='https://www.menslife.com/')
urlButton2 = InlineKeyboardButton(text='ссылка2', url='https://mensby.com/')
urlkb.add(urlButton, urlButton2)

@dp.message_handler(commands='ssilki')
async def url_commands(message : types.Message):
    await message.answer('Ссылочки', reply_markup=urlkb)
#==================================