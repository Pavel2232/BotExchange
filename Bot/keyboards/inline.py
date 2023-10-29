from aiogram.utils.keyboard import InlineKeyboardBuilder
from Bot.callback_data.callback_history import HistoryCurrency
from Bot.callback_data.callback_subscription import Subscription
from Bot.callback_data.callback_usd import Usd


def get_catalog_buttons():
    markup = InlineKeyboardBuilder()

    markup.button(
        text='Узнать сколько сейчас доллар',
        callback_data=Usd(name='USD')
        )
    markup.button(
        text='Подписатья на уведомления',
        callback_data=Subscription(name='USD')
    )
    markup.button(
        text='⭐история запросов курса',
        callback_data=HistoryCurrency(name='USD')
    )

    markup.adjust(1)

    return markup.as_markup()
