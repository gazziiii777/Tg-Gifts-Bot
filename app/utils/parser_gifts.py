from telethon.sync import TelegramClient
from telethon.tl.functions.payments import GetStarGiftsRequest
from aiogram import Bot
import time
from aiogram.types import FSInputFile
from config import PATH_TO_IMG
from core.config import settings

SESSION_NAME = "my_session"

async def parse_new_gifts(bot: Bot):
    async with TelegramClient(SESSION_NAME, settings.API_ID, settings.API_HASH) as client:
        result = await client(GetStarGiftsRequest(hash=0))
        
        for gift in result.gifts:
            print(f"🎁 ID: {gift.id}, Стоимость: {gift.stars} Stars")
            print(dir(gift))
            if gift.limited:
                print (gift.upgrade_stars)
                await bot.send_message(chat_id='-1002620487977', text='🌟 Новый подарок!')
                
                # Скачиваем стикер как файл (будем отправлять как фото)
                image_path = f"{PATH_TO_IMG}/gift_{gift.id}.tgs"
                await client.download_media(gift.sticker, file=image_path)
                
                # Отправляем как фото
                await bot.send_document(chat_id='-1002620487977', document=FSInputFile(image_path))
                print(f"Файл отправлен как фото: {image_path}")
                
                time.sleep(2)
