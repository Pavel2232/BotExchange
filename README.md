# 🤖💹⁉️ Телеграм бот курса USD🇺🇸💵

## Функционал бота:
* Пользователь может зайти в него и узнать курс доллара на текущий момент.
* Может подписаться на получение этого курса периодически.
* Бот помнит и хранит историю получения курса пользователя, и пользователь может ее в любой момент просмотреть.

## Как запустить:
1. Склонируйте репозиторий
```shell
git clone https://github.com/Pavel2232/BotExchange   
```
2. Установите зависимости
```shell
poetry install
```
3. Установите зависимости
```dotenv
SECRET_KEY=секретный ключь
DATABASE_URL=url для подключения postgres psql://test:test@localhost:5432/test
NOTIFICATION_INTERVAL_TIME=Время в секундах(с какой переодичностью отправлять ваши уведомления подписчикам)
REDIS_URL=url для подключения redis redis://localhost:6379/0
REDIS_HOST=localhost(замените на ваш хост редиса)
REDIS_PORT=6379(замените на порт на котором работает ваш редис)
TG_BOT_KEY=ваш ключ бота
TOKEN_FIXER=ваш токен
```

- Можно получить здесь [TG_BOT_KEY](https://t.me/BotFather)
- Можно получить здесь [API_TOKEN](https://fixer.io/)

4. Для запуска Postgres и Redis выполните:
```shell
docker-compose up -d
```

5. Запустите проект
```shell
./manage.py makemigrations
./manage.py migrate
python3 Bot/tg_bot.py
```
