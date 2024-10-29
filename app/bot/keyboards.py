from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardMarkup, \
    InlineKeyboardButton, ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton
from app.shared.config import Config

admins = [Config.ADMIN_ID]


def main_menu_keyboard(user_id: int):
    start_kb = [
        [
            KeyboardButton(text="🛒Магазин")
        ],
        [
            KeyboardButton(text="👤Профиль"),
            KeyboardButton(text="📖Информация")
        ]
    ]


    if user_id in admins:
        start_kb.append([KeyboardButton(text="⚙️Админ панель")])

    return ReplyKeyboardMarkup(keyboard=start_kb, resize_keyboard=True)


def back_button(pay=False):
    if pay:
        inline_kb_list = [[InlineKeyboardButton(text="Оплатить", pay=True)],
                          [InlineKeyboardButton(text="🔙Назад", callback_data="back")]]

    else:
        inline_kb_list = [[InlineKeyboardButton(text="Назад", callback_data="back")]]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def shop_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="💵Покупка", callback_data="buy")
    builder.button(text="🔙Назад", callback_data="back")
    return builder.as_markup()


def create_rat():
    builder = ReplyKeyboardBuilder()
    for item in ["1", "2", "3", "5", "10"]:
        builder.button(text=item, callback_data=f"rat_time")
    return builder.as_markup(resize_keyboard=True)


def admin_panel_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="➕добавить ключи", callback_data="add_keys")
    builder.button(text="🧐поиск ключей", callback_data="find_keys")
    builder.button(text="🔙Назад", callback_data="back")
    return builder.as_markup()
