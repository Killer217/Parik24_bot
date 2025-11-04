import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import threading
from flask import Flask

# 🔑 Отримуємо токен із секретів GitHub
BOT_TOKEN = os.getenv("8227383457:AAFgWQhkJpbCvYT-nJEI8r01UTaGlkxMFWQ")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 🔹 Flask сервер для Render
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# 🔹 Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    username = message.from_user.first_name or "друже"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Забрати бонус", url="https://trackmyaff.com/?serial=61332575&creative_id=5873")]
    ])
    photo = FSInputFile("1080x1080-1.jpg")
    caption = f"👋 Привіт, {username}!\n\nРеєструйся за посиланням нижче та забирай круті бонуси від Parik24! 🎁"
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=caption, reply_markup=keyboard)

# 🔹 Головний запуск
async def main():
    print("✅ Бот запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(main())
