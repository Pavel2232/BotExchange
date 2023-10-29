from aiogram.filters.callback_data import CallbackData


class Usd(CallbackData, prefix='currency'):
    name: str
