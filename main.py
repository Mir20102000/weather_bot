import datetime
import time
import Constanst as keys
from telegram.ext import *
from config import open_weather_token
import requests
from pprint import pprint
import Responses as R

print("Bot started...")


def get_weather(city, open_weather_token):

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
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={open_weather_token}"
        )
        data = r.json()
        # pprint(data)

        # weather_main = data["weather"][0]["main"]
        # if weather_main in code_to_smile:
        #     wd = code_to_smile[weather_main]
        # else:
        #     wd = "Посмотри в окно, не пойму что за погода"

        weather_description = data["weather"][0]["description"]
        temp = int(data["main"]["temp"])
        min_temp = int(data["main"]["temp_min"])
        max_temp = int(data["main"]["temp_max"])
        pressure = int(data["main"]["pressure"] / 1.333)
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise = time.strftime("%H:%M:%S", time.gmtime(data["sys"]["sunrise"] + 10800))
        sunset = time.strftime("%H:%M:%S", time.gmtime(data["sys"]["sunset"] + 10800))

        print(f"***{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}***\nПогода в городе: {city}"
              f"\nТемпература: {temp} °C {weather_description} {wd}"
              f"\nМаксимальная температура: {max_temp} °C\nМинимальная температура: {min_temp} °C"
              f"\nДавление: {pressure} мм.рт.ст\nВлажность: {humidity} %\nВетер: {wind} м/с\nВосход: {sunrise}"
              f"\nЗакат: {sunset}")


    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
#
# def start_command(update, context):
#     update.message.reply_text("Давай по-общаемся. Напиши мне что-нибудь.")
#
#
# def help_command(update, context):
#     update.message.reply_text("Я бот для общения. Если ты хочешь по-общаться, то просто напиши мне. "
#                               "Если я пойму твой текст, то обязательно отвечу) А ещё я могу показывать точное время."
#                               "Только спроси у меня.")
#
#
# def handle_message(update, context):
#     text = str(update.message.text).lower()
#     response = R.sample_responses(text)
#
#     update.message.reply_text(response)
#
#
# def error(update, context):
#     print(f"Update {update} caused error {context.error}")
#
#
# def main():
#     updater = Updater(keys.API_KEY, use_context=True)
#     dp = updater.dispatcher
#
#     dp.add_handler(CommandHandler("start", start_command))
#     dp.add_handler(CommandHandler("help", help_command))
#
#     dp.add_handler(MessageHandler(Filters.text, handle_message))
#
#     dp.add_error_handler(error)
#
#     updater.start_polling()
#     updater.idle()
#
#
# main()
