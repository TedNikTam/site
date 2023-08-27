from create_bot import bot, dp

from aiogram.utils import executor
from aiogram import types
from aiogram.dispatcher import Dispatcher

from .config import open_weather_token as OWT
import requests
import datetime

dp = Dispatcher(bot)


# @dp.message_handler(commands=['Weather', 'Погода'])
async def weather_command(message: types.Message):
    await message.reply("Укажи город!")

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&lang=ru&appid={OWT}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        
        weather_discription = data["weather"][0]['main']
        if weather_discription in code_to_smile:
            wd = code_to_smile[weather_discription]
        else:
            wd = 'Посмотри в окно, не пойму что там за погода!'


        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        pressure = data['main']['pressure']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise']) #изначально кол-во сек с 01.01.1970
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather} C° {wd}\n"
              f"Влажность: {humidity} %\nСкорость ветра: {wind} м.с\nДавление: {pressure} мм.рт.ст.\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\n"
              f"Продолжительность светового дня: {sunset_timestamp - sunrise_timestamp}\n"
              f"***Хорошего дня!***")

    except:
       await message.reply("\U00002620 Проверьте название города! \U00002620")


def register_handlers_main_weather_tg_bot(dp: Dispatcher):
    dp.register_message_handler(weather_command, commands=['Weather', 'Погода'], state=None)
    dp.register_message_handler(get_weather)


