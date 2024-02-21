import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.main.routers import router

logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_routers(router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
