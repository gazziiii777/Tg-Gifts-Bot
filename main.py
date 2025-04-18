import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
# from app.bot.handlers import router
from core.config import settings
from core.database import db_helper
from multiprocessing import Process
from app.utils.parser_gifts import parse_new_gifts

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode='HTML')
)
dp = Dispatcher()
# dp.include_router(router)  # Раскомментируйте, когда добавите роутер

async def repeat_parse_new_gifts(bot: Bot):
    """Парсинг новых монет"""
    while True:
        try:
            await parse_new_gifts(bot)
        except Exception as e:
            logging.error(f"Ошибка в repeat_parse_new_coin: {e}")
        await asyncio.sleep(3600)


async def background_main(bot: Bot):
    """Запуск фоновых задач"""
    await asyncio.gather(
        repeat_parse_new_gifts(bot),
    )

def run_background_tasks(bot: Bot):
    """Запуск фоновых задач в отдельном процессе"""
    try:
        asyncio.run(background_main(bot))
    except Exception as e:
        logging.error(f"Ошибка в run_background_tasks: {e}")
        
async def on_startup():
    """Функция, которая выполняется при запуске бота."""
    logging.info("Бот запущен.")
    Process(target=run_background_tasks, args=(bot,), daemon=True).start()


async def on_shutdown():
    """Функция, которая выполняется при остановке бота."""
    logging.info("Завершение работы бота...")
    await bot.session.close()
    logging.info("Бот остановлен.")


async def main():
    """Основная функция, которая запускает бота."""
    await on_startup()
    try:
        await db_helper.init()
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logging.info("Получен сигнал прерывания (Ctrl+C)")
    finally:
        await on_shutdown()


if __name__ == "__main__":
    asyncio.run(main())