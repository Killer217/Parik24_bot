from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# 🔑 Твій токен бота
BOT_TOKEN = "8227383457:AAHskX1GQRZ9hmoytkMHiNf1lTxVvxNLHYc"

# 🔹 Створюємо бота і диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 🔹 Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    username = message.from_user.first_name or "друже"

    # Кнопка з посиланням
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎁 Забрати бонус", url="https://trackmyaff.com/?serial=61332575&creative_id=5873")]
        ]
    )

    # Фото + підпис
    photo = FSInputFile("1080x1080-1.jpg")
    caption = f"👋 Привіт, {username}!\n\nРеєструйся за посиланням нижче та забирай круті бонуси від Parik24! 🎁"

    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=caption, reply_markup=keyboard)

# 🔹 Запуск бота
async def main():
    print("✅ Бот запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())