from aiogram.filters.callback_data import CallbackData


class Subscription(CallbackData, prefix='subscription'):
    name: str
