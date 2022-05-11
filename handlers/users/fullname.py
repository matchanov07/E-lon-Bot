
from loader import dp
from aiogram import types

@dp.message_handler(text="full_name")
async def full(message: types.Message):
    fn = message.from_user.full_name
    await message.answer(f"sizning toliq ismingiz {fn}")
