import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

users_data = [
    ('User  1', 'example1@gmail.com', 10, 1000),
    ('User  2', 'example2@gmail.com', 20, 1000),
    ('User  3', 'example3@gmail.com', 30, 1000),
    ('User  4', 'example4@gmail.com', 40, 1000),
    ('User  5', 'example5@gmail.com', 50, 1000),
    ('User  6', 'example6@gmail.com', 60, 1000),
    ('User  7', 'example7@gmail.com', 70, 1000),
    ('User  8', 'example8@gmail.com', 80, 1000),
    ('User  9', 'example9@gmail.com', 90, 1000),
    ('User  10', 'example10@gmail.com', 100, 1000),
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)
conn.commit()

cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')
conn.commit()

cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
conn.commit()

# Удаляем запись с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')
conn.commit()

# Подсчет общего количества записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вычисляем средний баланс
if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0

print(average_balance)
conn.close()
