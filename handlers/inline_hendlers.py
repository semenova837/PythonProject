from aiogram import types, Router

router = Router()


@router.callback_query(lambda c: c.data.startswith("test_btn_"))
async def test_callback_handlers(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data == "test_btn_1":
        await callback_query.message.answer("You pressed first Inline Button")
    elif data == "test_btn_2":
        await callback_query.message.answer("You pressed second Inline Button")
    elif data == "test_btn_3":
        await callback_query.message.answer("You pressed third Inline Button")