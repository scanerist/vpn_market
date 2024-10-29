from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import back_button
from app.bot.state_manager import Form

information_router = Router()

@information_router.message(F.text == "📖Информация")
async def information_handler(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer("🤝 Мы всегда на связи:\n"
                         "📧 Для любых вопросов:\n "
                         "📢 Новости и обновления:\n", reply_markup=back_button())

