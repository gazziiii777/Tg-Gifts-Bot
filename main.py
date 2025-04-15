import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
# from app.bot.handlers import router
from core.config import settings



# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s - %(levelname)s - %(message)s")

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN,
          default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()


async def on_startup():
    logging.info("Бот запущен.")



async def on_shutdown():
    """Функция, которая выполняется при остановке бота."""
    logging.info("Бот остановлен.")
    await bot.close()


async def main():
    """Основная функция, которая запускает бота и планировщик."""
    await on_startup()  
    # dp.include_router(router)
    await dp.start_polling(bot)  


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Бот остановлен вручную.")
    finally:
        asyncio.run(on_shutdown())  
