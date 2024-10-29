from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile
from app.bot.keyboards import  shop_menu_keyboard, create_rat, back_button
from app.bot.state_manager import Form
import os
from aiogram.utils import keyboard
buy_router = Router()



@buy_router.message(F.text == "🛒Магазин")
async def buy_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    photo_path = FSInputFile(path=os.path.join(os.getcwd(), "imgs", "shop.png"))
    msg = await message.answer_photo(photo=photo_path ,caption="🛍 Магазин NeOtval - ваша цифровая витрина свободы:\n"
                        "🌟 Разблокируйте звезды интернета: Instagram, YouTube, Discord и многие другие.\n"
                        "🎮 Геймеры, объединяйтесь! Ваши любимые игры ждут вас без ограничений.\n"
                        "📱 Просто выберите, купите и наслаждайтесь свободным интернетом!\n", reply_markup=shop_menu_keyboard())

    await state.update_data(previous_message_id=msg.message_id)
    await state.set_state(Form.buy)



@buy_router.callback_query(F.data == "buy")
async def number_of_keys(callback: types.CallbackQuery, state: FSMContext):
    await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    msg = await callback.message.answer("Выберите количество ключей, или введите свое, сли хотите больше", reply_markup=create_rat())
    await state.update_data(previous_message_id=msg.message_id)
    await state.set_state(Form.select_number_of_keys)
    await callback.answer()



@buy_router.message(Form.select_number_of_keys)
async def select_payment_method( message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.bot.delete_message(message.chat.id, message.message_id)
    await message.bot.delete_message(message.chat.id, message_id=data.get("previous_message_id"))
    if message.text.isdigit() and int(message.text) > 0:
        await state.update_data(number_of_keys=int(message.text))
        msg = await message.answer_invoice(
            title="Покупка ключей",
            description=f"Количество ключей: {int(message.text)}",
            provider_token="",
            currency="XTR",
            prices=[types.LabeledPrice(label="XTR", amount=int(message.text) * 10)],
            payload="demo",
            start_parameter="demo",
            reply_markup=back_button(pay=True))
    else:
        await message.answer("Вы ввели некорректное значение, повторите снова")



@buy_router.pre_checkout_query()
async def on_pre_checkout_query(query: types.PreCheckoutQuery):
    await query.answer(ok=True)



@buy_router.message(F.successful_payment)
async def successful_payment(message: types.Message, state: FSMContext):
    await message.answer(text= "Спасибо за покупку!", message_effect_id="5104841245755180586", reply_markup=back_button())
    await state.clear()
