import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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

# Создание обычной клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

# Создание Inline-клавиатуры
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text.lower() == "привет")
async def greet_user(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

@dp.message_handler(lambda message: message.text not in ['Рассчитать', 'Информация'])
async def all_messages(message: types.Message):
    await message.answer("Пожалуйста, используйте кнопки 'Рассчитать' или 'Информация'.")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Нажмите 'Рассчитать', чтобы начать вычисление нормы калорий.",
                         reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора:\n\n"
                              "Для мужчин: BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
                              "Для женщин: BMR = 10 * вес + 6.25 * рост - 5 * возраст - 161")
    await call.answer()  # Убираем индикатор загрузки

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()  # Убираем индикатор загрузки

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
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5  # для мужчин
    # bmr = 10 * weight + 6.25 * growth - 5 * age - 161  # для женщин

    await message.answer(f"Ваша норма калорий: {bmr} ккал в день.")
    await state.finish()  # Завершение состояния

@dp.message_handler(lambda message: message.text == 'Информация')
async def send_info(message: types.Message):
    await message.answer("Это бот для расчета нормы калорий. Нажмите 'Рассчитать', чтобы начать.")
# Обработчик для всех остальных сообщений
@dp.message_handler()
async def handle_all_messages(message: types.Message):
    await message.answer("Извините, я не понимаю. Пожалуйста, введите команду /start или напишите 'Calories'.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

