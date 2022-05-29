# Отечественный Телеграм-бот на Yandex REST API.

- Язык - Python 3.9
- Библиотека - aiogram
- Yandex Geocoder API
- Yandex Weather API

Телеграм-бот для отображения погоды в городе, который запрашивает пользователь.
[Ссылка на бота](https://t.me/Mir2010200_bot)

## Зависимости проекта
- [pymorphy2](https://pymorphy2.readthedocs.io/en/stable/)
- [python-telegram-bot](https://python-telegram-bot.org/)
- [yarl](https://pypi.org/project/yarl/)
- [aiogram](https://docs.aiogram.dev/en/latest/)
- [Yandex-API](https://yandex.ru/dev/)
## Способ запуска проекта

**Шаг 1**

В корне проекта подтягиваем необходимые зависимости с помощью docker.

```bash
docker build .
```

**Шаг 2**

Заполняем необходимые API-токены.

```bash
MAPS_APIKEY = "####"
WEATHER_APIKEY = "####"
TOKEN = "####"
```

**Шаг 3**

Запускаем бота.

```bash
python3 ./bot.py
```

## Развертывание в докере

**Source**
```bash
# Add python env to the build
FROM python:3.9-slim

# Add PYTHONPATH system param
WORKDIR $HOME/code

# Add required files for the project
ADD requirements.txt .
ADD functions ./functions
ADD other ./other
ADD tgfunks ./tgfunks
ADD main.py .

# Install required packages
RUN pip install --user -r ./requirements.txt

# Run application
CMD ["python", "bot.py"]
#CMD ["sh", "-c", "python", "bot.py"]
```

**Команда для сборки образа:**
```bash
docker build -t dockerfile .
```

**Команда для запуска образа:**
```bash
docker run --rm -it dockerfile
```

## User Story

|                  |        |                                      |
| ---------------- | ------ | ------------------------------------ |
| Заказчик (actor) | Как    | Пользователь                         |
| Примечание       | Я хочу | Увидеть погоду в заданном городе     |
| Цель             | Чтобы  | Получить немедленный доступ к погоде |
