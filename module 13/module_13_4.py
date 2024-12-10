import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

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
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью. Напишите 'Calories', чтобы начать.")


@dp.message_handler(lambda message: message.text.lower() == "привет")
async def greet_user(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


@dp.message_handler(lambda message: message.text.lower() == "calories")
async def set_age(message: types.Message):
    await UserState.age.set()  # Переход к состоянию ввода возраста
    await message.answer("Введите свой возраст:")

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await UserState.next()  # Переход к следующему состоянию (рост)
    await message.answer("Введите свой рост (в см):")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await UserState.next()  # Переход к следующему состоянию (вес)
    await message.answer("Введите свой вес (в кг):")

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес
    data = await state.get_data()  # Получаем все введенные данные

    # Пример формулы для расчета калорий (Миффлин - Сан Жеор)
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Пример для мужчин
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал в день.")
    await state.finish()  # Завершаем состояние


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

