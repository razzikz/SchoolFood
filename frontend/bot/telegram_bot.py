import dotenv
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("start")

@dp.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer("help")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
