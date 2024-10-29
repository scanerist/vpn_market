import os

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from app.database.user_dao import get_user_by_id
from app.bot.keyboards import back_button

profile_router = Router()


@profile_router.message(F.text == "👤Профиль")
async def profile_handler(message: types.Message, state: FSMContext):
    await message.delete()
    user = await get_user_by_id(user_id=message.from_user.id)
    photo_path = FSInputFile(path=os.path.join(os.getcwd(), "imgs", "prolife.png"))
    await message.answer_photo(photo=photo_path, caption=f"Ваш профиль:\n\n Ваш ID: {message.from_user.id}\n Всего покупок: {user.number_of_buys}\n Всего активных ключей: {user.number_of_active_keys}",
        reply_markup=back_button())
    await state.clear()

