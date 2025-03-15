from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_book() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Сортування", callback_data="test_btn_1"),
         InlineKeyboardButton(text="Рекомендації", callback_data="test_btn_2"),
         InlineKeyboardButton(text="Додаткові", callback_data="test_btn_3")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_inline_music() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Сортування", callback_data="test_btn_1"),
         InlineKeyboardButton(text="Рекомендації", callback_data="test_btn_2"),
         InlineKeyboardButton(text="Додаткові", callback_data="test_btn_3")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_inline_recommendations() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Затишний вечір (меланхолійна музика + книга для натхнення)", callback_data="test_btn_1")],
        [InlineKeyboardButton(text="Енергійний день (динамічні треки + мотиваційна література)", callback_data="test_btn_2")],
        [InlineKeyboardButton(text="Роздуми про життя (глибокі книги + атмосферна музика)", callback_data="test_btn_3")],
        [InlineKeyboardButton(text="Щось нове (експериментальні треки + нестандартні книги)", callback_data="test_btn_4")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_inline_search() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="Шукати книгу", callback_data="test_btn_1")],
        [InlineKeyboardButton(text="Шукати музику", callback_data="test_btn_2")],
        [InlineKeyboardButton(text="Знайти щось від конкретного автора/виконавця", callback_data="test_btn_3")],
        [InlineKeyboardButton(text="Знайти книги або музику за настрієм (ключові слова)", callback_data="test_btn_4")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)