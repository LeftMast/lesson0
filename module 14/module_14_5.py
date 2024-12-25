import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import State, StatesGroup
from crud_functions import initiate_db, get_all_products, add_user, is_included

API_TOKEN = 'YOUR_API_TOKEN_HERE'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных
initiate_db()


# Определение состояний для регистрации
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_register = types.KeyboardButton('Регистрация')
    button_buy = types.KeyboardButton('Купить')
    keyboard.add(button_register, button_buy)
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    user_data = await state.get_data()
    username = user_data['username']
    email = user_data['email']

    # Добавляем пользователя в базу данных
    add_user(username, email, age)
    await message.answer("Вы успешно зарегистрированы!")

    # Завершение состояний
    await state.finish()


@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()

    if not products:
        await message.answer("Нет доступных продуктов.")
        return

    for product in products:
        title, description, price = product
        await message.answer(f"Название: {title} | Описание: {description} | Цена: {price} ккал")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
