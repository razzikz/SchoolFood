import dotenv
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
import requests
import json

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

url_page = "https://195e-149-34-244-163.ngrok-free.app"
url_catalog = "https://d127-2001-41d0-700-80cc-00.ngrok-free.app"

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    response = requests.get(url=f"http://127.0.0.1:8000/check/{user_id}/")

    login = False
    if response.status_code == 200:
        decode_data = response.content.decode()
        data = json.loads(decode_data)
        login = data.get("login")

    if login:
        url = url_catalog
    else:
        url = f"{url_page}?user_id={user_id}&name={message.from_user.first_name}"

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Открыть приложение📱",
                    web_app=types.WebAppInfo(url=url)
                )
            ]
        ]
    )
    await message.answer(
        "<b>Привет! 👋 Это бот для веб-приложения школьная еда!\nЗапусти приложение, чтобы начать работу 👇</b>",
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
