import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from Bot.callback_data.callback_history import HistoryCurrency
from Bot.callback_data.callback_subscription import Subscription
from Bot.callback_data.callback_usd import Usd
from Bot.handlers.callback import (get_usd_rate,
                                   get_history_exchange, get_subscription)
from Bot.handlers.start import start
from Bot.middleware.apched_middleware import SchedulerMiddleware
from src.settings import env
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator


async def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    bot = Bot(env('TG_BOT_KEY'))
    storage = RedisStorage.from_url(env('REDIS_URL'))
    dp = Dispatcher(storage=storage)

    jobstores = {
        'default': RedisJobStore(

            host=env('REDIS_HOST'),

            port=env.int('REDIS_PORT')
        )
    }

    scheduler = ContextSchedulerDecorator(
        AsyncIOScheduler(
            timezone="Europe/Moscow",
            jobstores=jobstores
        )
    )

    scheduler.ctx.add_instance(bot, declared_class=Bot)

    scheduler.start()

    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.message.register(start, CommandStart())
    dp.callback_query.register(get_usd_rate, Usd.filter())
    dp.callback_query.register(get_history_exchange, HistoryCurrency.filter())
    dp.callback_query.register(get_subscription, Subscription.filter())
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
