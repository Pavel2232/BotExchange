from aiogram.types import Message
from Bot.keyboards.inline import get_catalog_buttons


async def start(message: Message):
    await message.answer('Добро Пожаловать!!!',
                         reply_markup=get_catalog_buttons()
                         )
