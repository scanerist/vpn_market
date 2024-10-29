from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    buy = State()
    select_number_of_keys = State()
    payment_method = State()

class AdminForm(StatesGroup):
    admin = State()
    add_keys = State()
    find_key = State()

