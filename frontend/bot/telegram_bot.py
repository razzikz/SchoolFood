import dotenv
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
url = "url"


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Открыть приложение",
                    web_app=types.WebAppInfo(url=f"{url}?user_id={message.from_user.id}&name={message.from_user.first_name}")
                )
            ]
        ]
    )
    await message.reply(
        f"start",
        reply_markup=keyboard
    )


@dp.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer("help")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
