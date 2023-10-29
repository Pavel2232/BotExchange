import datetime
import os
from aiogram.types import CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from Bot.handlers.apched import on_subscription
from Bot.working_with_exchange.get_rate_dollar import DollarExchangeFixer

import django

from src.settings import env

os.environ['DJANGO_SETTINGS_MODULE'] = 'src.settings'
django.setup()
from exchange_rate.models import HistoryExchange


async def get_usd_rate(call: CallbackQuery):
    exchange = DollarExchangeFixer(
        currency='USD',
        to='RUB',
        api_key=env('TOKEN_FIXER')
    )
    user_id = call.from_user.id
    dollar = exchange.get_exchange_rate()
    await HistoryExchange.objects.acreate(
        user_id_tg=user_id,
        rate=dollar)

    await call.message.answer('доллар {} {} на {} момент времени'.format(
        dollar, 'руб',
        datetime.datetime.now()
    )
    )


async def get_history_exchange(call: CallbackQuery):
    user_id = call.from_user.id
    history = ''
    async for history_obj in HistoryExchange.objects.filter(user_id_tg=user_id):
        history += ('{} рублей {}\n'.format(
            history_obj.rate,
            history_obj.created.strftime('%H:%M %d.%m.%Y')
        )
        )
    await call.message.answer('{}'.format(history))


async def get_subscription(call: CallbackQuery, apscheduler: AsyncIOScheduler):
    user_id = call.from_user.id

    await call.message.answer('вы успешно подписались')
    apscheduler.add_job(
        on_subscription,
        trigger='interval',
        seconds=env.int('NOTIFICATION_INTERVAL_TIME'),
        kwargs={'chat_id': user_id},
        replace_existing=True)
