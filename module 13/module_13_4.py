import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from pycparser.ply.yacc import token

API_TOKEN = 'token'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Отправляем приветственное сообщение в чат
    await message.answer("Привет! Я бот, помогающий твоему здоровью. Введите команду /start, чтобы начать общение.")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Напишите 'Calories', чтобы начать вычисление нормы калорий.")

@dp.message_handler(lambda message: message.text == 'Calories')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    # Получаем данные из состояния
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула Миффлина - Сан Жеора для мужчин
    # BMR = 10 * weight + 6.25 * growth - 5 * age + 5
    # Для женщин формула будет: BMR = 10 * weight + 6.25 * growth - 5 * age - 161
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5  # для мужчин
    # bmr = 10 * weight + 6.25 * growth - 5 * age - 161  # для женщин

    await message.answer(f"Ваша норма калорий: {bmr} ккал в день.")
    await state.finish()  # Завершение состояния

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
