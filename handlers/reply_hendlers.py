from aiogram import types, Router
from keyboards.inline_keyboards import get_inline_book, get_inline_music, get_inline_recommendations, get_inline_search

router = Router()


@router.message(lambda message: message.text == "Книги")
async def test_handler(message: types.Message):
    print(message)
    await message.answer("""It's test message!""", reply_markup=get_inline_book())

@router.message(lambda message: message.text == "Музика")
async def test_handler(message: types.Message):
    print(message)
    await message.answer("""It's test message!""", reply_markup=get_inline_music())


@router.message(lambda message: message.text == "Рекомендації")
async def test_handler(message: types.Message):
    print(message)
    await message.answer("""It's test message!""", reply_markup=get_inline_recommendations())


@router.message(lambda message: message.text == "Пошук")
async def test_handler(message: types.Message):
    print(message)
    await message.answer("""It's test message!""", reply_markup=get_inline_search())