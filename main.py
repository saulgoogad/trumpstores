from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor
import asyncio
from utils.fortnite_api import get_shop_data
from utils.image_generator import generate_shop_image

import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["shop"])
async def send_shop_image(message: types.Message):
    shop_items = get_shop_data()
    image_path = generate_shop_image(shop_items)
    await message.answer_photo(InputFile(image_path))
    os.remove(image_path)

if __name__ == "__main__":
    executor.start_polling(dp)