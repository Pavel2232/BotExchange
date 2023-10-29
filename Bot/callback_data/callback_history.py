from aiogram.filters.callback_data import CallbackData


class HistoryCurrency(CallbackData, prefix='history'):
    name: str
