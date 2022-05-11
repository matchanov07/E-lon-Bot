from loader import dp
from aiogram import types

@dp.message_handler(text="username")
async def full(message: types.Message):
    us = message.from_user.username
    await message.answer(f"sizning username: @{us}")
