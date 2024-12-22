import sqlite3

connections = sqlite3.connect('Products.db')
cursor = connections.cursor()


def initiate_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
);
''')

    connections.commit()


def get_all_products():
    all_db = cursor.execute('SELECT * FROM Products').fetchall()
    return all_db