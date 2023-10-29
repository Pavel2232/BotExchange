import datetime
import os
from aiogram import Bot
import django
from Bot.working_with_exchange.get_rate_dollar import DollarExchangeFixer
from src.settings import env

os.environ['DJANGO_SETTINGS_MODULE'] = 'src.settings'
django.setup()
from exchange_rate.models import SubscriptionUser


async def on_subscription(bot: Bot, chat_id: int):
    if await SubscriptionUser.objects.filter(user_id_tg=chat_id).afirst():
        if await SubscriptionUser.objects.filter(
                user_id_tg=chat_id,
                subscription_on=True).afirst():
            await bot.send_message(chat_id, 'Вы уже подписаны')
        await SubscriptionUser.objects.aupdate(
            user_id_tg=chat_id,
            subscription_on=True)
    else:
        await SubscriptionUser.objects.acreate(
            user_id_tg=chat_id,
            subscription_on=True
        )

    exchange = DollarExchangeFixer(
        currency='USD',
        to='RUB',
        api_key=env('TOKEN_FIXER')
    )

    dollar = exchange.get_exchange_rate()
    await bot.send_message(
        chat_id=chat_id,
        text='доллар {} {} на {} момент времени. Селедующее уведомление через {}'.format(
  dollar, 'руб', datetime.datetime.now(), env.int('NOTIFICATION_INTERVAL_TIME') / 60)
    )
