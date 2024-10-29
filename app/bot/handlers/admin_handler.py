from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from app.bot.keyboards import admin_panel_keyboard
from app.bot.state_manager import AdminForm
from app.database.key_dao import set_key, get_key
from app.shared.config import Config
from aiogram import filters


admins = [Config.ADMIN_ID]

admin_router = Router()


@admin_router.message((F.text == "⚙️Админ панель") & (F.from_user.id.in_(admins)))
async def admin_panel(message: types.Message, state: FSMContext):

    await message.answer("Вы выбрали админ панель", reply_markup=admin_panel_keyboard())
    await state.clear()


@admin_router.callback_query(F.data == "add_keys")
async def add_keys(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("введите ключ")
    await state.set_state(AdminForm.add_keys)


@admin_router.message(AdminForm.add_keys)
async def process_add_keys(message: types.Message, state: FSMContext):
        key = await set_key(message.text, "active", message.from_user.id)
        await message.answer(f"Ключ {key.key} добавлен")
        await state.clear()


@admin_router.callback_query(F.data == "find_keys")
async def find_keys(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("введите ключ")
    await state.set_state(AdminForm.admin)

@admin_router.message(AdminForm.admin)
async def process_find_keys(message: types.Message, state: FSMContext):
    key = await get_key(message.text)
    if key:
        await message.answer(f"Ключ {key.key} активен")
    else:
        await message.answer("Ключ не найден")
    await state.clear()

