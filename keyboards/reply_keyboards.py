from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Книги")],
            [KeyboardButton(text="Музика")],
            [KeyboardButton(text="Рекомендації")],
            [KeyboardButton(text="Пошук")],
            [KeyboardButton(text="Налаштування")]
        ],
        resize_keyboard=True
    )
    return keyboard
