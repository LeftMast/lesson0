import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

API_TOKEN = 'token'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Отправляем приветственное сообщение в чат
    await message.answer("Привет! Я бот, помогающий твоему здоровью. Введите команду /start, чтобы начать общение.")

@dp.message_handler()
async def all_messages(message: types.Message):
    # Отправляем ответ в чат, используя текст сообщения пользователя
    await message.answer(f"Он мне ответил! Вы написали: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





