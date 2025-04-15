from tortoise import Tortoise, fields, run_async
from tortoise.models import Model
from core.config import settings



class DataSperm:
    async def init_db():
        await Tortoise.init(
            db_url="postgres://user:password@localhost:5432/db_name",
            modules={"models": ["__main__"]}  # Указываем текущий модуль
        )
        await Tortoise.generate_schemas()  # Создает таблицы, если их нет

db_helper = DataSperm()
