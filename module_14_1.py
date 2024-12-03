import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for u in users:
    print(f'Имя: {u[1]} | Почта: {u[2]} | Возраст: {u[3]} | Баланс: {u[4]}')

connection.commit()
connection.close()