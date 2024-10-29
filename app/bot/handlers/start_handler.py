from typing import Optional

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import main_menu_keyboard, admins
from app.database.user_dao import set_user
from app.shared.logger import setup_logger

logger = setup_logger(__name__)
start_router = Router()






@start_router.callback_query(F.data == "back")
async def start_callback_handler(callback: types.CallbackQuery, state: FSMContext):

    await callback.message.answer("Вы вернулись на главную", reply_markup=main_menu_keyboard(callback.from_user.id))
    await state.clear()
    await callback.answer()
    await callback.message.bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)





@start_router.message(F.text == "/start")
async def start_message_handler(message: types.Message, state: FSMContext):
    await message.delete()
    user = await set_user(user_id=message.from_user.id, number_of_buys=0, number_of_active_keys=0)
    logger.info(f"User {message.from_user.id} created")
    await message.answer("🌍 Откройте двери в безграничный интернет! NeOtval - ваш ключ к свободному доступу. 🌐\n\n"
                         "Забудьте о блокировках и наслаждайтесь любимыми сервисами без ограничений. Мы поможем вам оставаться на связи с миром!",
                         reply_markup=main_menu_keyboard(message.from_user.id))
    await state.clear()