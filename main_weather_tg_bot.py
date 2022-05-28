from Constanst import API_KEY
from config import open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
import datetime
import time

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет!\U0001F642 Напиши мне название города и я пришлю сводку погоды \U00002602")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear: \U00002600",
        "Clouds: \U00002601",
        "Rain: \U00002614",
        "Drizzle: \U00002614",
        "Thunderstorm: \U000026A1",
        "Snow: \U0001F328",
        "Mist: \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&units=metric&lang=ru&appid={open_weather_token}"
        )
        data = r.json()
        weather_main = data["weather"][0]["main"]
        if weather_main in code_to_smile:
            wd = code_to_smile[weather_main]
        else:
            wd = ""
        weather_description = data["weather"][0]["description"]
        temp = int(data["main"]["temp"])
        min_temp = int(data["main"]["temp_min"])
        max_temp = int(data["main"]["temp_max"])
        pressure = int(data["main"]["pressure"] / 1.333)
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise = time.strftime("%H:%M:%S", time.gmtime(data["sys"]["sunrise"] + 10800))
        sunset = time.strftime("%H:%M:%S", time.gmtime(data["sys"]["sunset"] + 10800))

        await message.reply(f"***{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}***\n\n"
                            f"Погода в городе: {message.text}\n"
                            f"\nТемпература: {temp} °C {weather_description} {wd}\n"
                            f"\nМаксимальная температура: {max_temp}°C\n\n"
                            f"Минимальная температура: {min_temp}°C\n"
                            f"\nДавление: {pressure} мм.рт.ст\n\n"
                            f"Влажность: {humidity}%\n\n"
                            f"Ветер: {wind} м/с\n\n"
                            f"Восход в {sunrise}\n\n"
                            f"Закат в {sunset}\n\n\n"
                            f"Хорошего вам дня! \U0001F60E")

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")


if __name__ == "__main__":
    executor.start_polling(dp)
