import asyncio
from aiogram.types import BotCommand, BotCommandScopeDefault

from app.bot.bot import VpnStore
from app.bot.handlers import start_handler, buy_handler, information_handler, profile_handler, admin_handler
from app.shared.logger import setup_logger

logger = setup_logger(__name__)

store_bot = VpnStore()
dp = store_bot.get_dispatcher()
bot = store_bot.get_bot()

async def set_commands():
    commands = [
        BotCommand(command="start", description="Начало работы")
        ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


async def start_bot():
    await set_commands()
    dp.include_router(start_handler.start_router)
    dp.include_router(buy_handler.buy_router)
    dp.include_router(information_handler.information_router)
    dp.include_router(profile_handler.profile_router)
    dp.include_router(admin_handler.admin_router)


    await dp.start_polling(bot)
    logger.info("Bot started")

async def main():
    await start_bot()




if __name__ == "__main__":
    asyncio.run(main())
