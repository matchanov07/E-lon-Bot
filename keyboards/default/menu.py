from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="full_name"),KeyboardButton(text="username")],
        [KeyboardButton(text="📱Phone number", request_contact=True), KeyboardButton(text="Lacation", request_location=True)]
    ],
    resize_keyboard=True
)