import sqlite3

# Подключаемся к базе данных (если файла не существует, он будет создан)
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создаем таблицу Users, если она ещё не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполняем таблицу 10 записями
users_data = [
    ('User 1', 'example1@gmail.com', 10, 1000),
    ('User 2', 'example2@gmail.com', 20, 1000),
    ('User 3', 'example3@gmail.com', 30, 1000),
    ('User 4', 'example4@gmail.com', 40, 1000),
    ('User 5', 'example5@gmail.com', 50, 1000),
    ('User 6', 'example6@gmail.com', 60, 1000),
    ('User 7', 'example7@gmail.com', 70, 1000),
    ('User 8', 'example8@gmail.com', 80, 1000),
    ('User 9', 'example9@gmail.com', 90, 1000),
    ('User 10', 'example10@gmail.com', 100, 1000),
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)
conn.commit()

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500
cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')
conn.commit()

# Удаляем каждую 3ю запись начиная с 1ой
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
conn.commit()

# Выборка всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
results = cursor.fetchall()

# Выводим результаты в консоль
for username, email, age, balance in results:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Закрываем соединение с базой данных
conn.close()
