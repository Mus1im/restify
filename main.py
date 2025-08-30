import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота (замените на свой)
BOT_TOKEN = "7882205686:AAEhWPfQ7ToP0PkRSkz2-EUmpNE0MKdqi9s"

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🤖 Бот работает! Привет!")

# Обработчик команды /test
@dp.message(Command("test"))
async def cmd_test(message: types.Message):
    await message.answer("✅ Тест пройден! Бот отвечает!")

# Обработчик любого текста
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")

# Функция запуска
async def main():
    logger.info("Запускаем бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
