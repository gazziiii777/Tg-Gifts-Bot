from tortoise import Tortoise, fields, run_async
from tortoise.models import Model
from core.config import settings



class DataSperm:
    @staticmethod
    async def init():
        await Tortoise.init(
            db_url=settings.DATABASE_URL_asyncpg,
            modules={"models": ["app.models.gifts"]}  # Указываем текущий модуль
        )
        await Tortoise.generate_schemas()  # Создает таблицы, если их нет
        
    @staticmethod
    async def close():
        await Tortoise.close_connections()

db_helper = DataSperm()
