import sqlite3

# Подключение к базе данных (создастся автоматически, если не существует)
conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

# Создание таблицы с указанными столбцами
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        latitude REAL,
        longitude REAL,
        width REAL,
        length REAL,
        mm_per_hour REAL,
        datetime TEXT
    )
''')

# Вставка данных в таблицу
notes_data = [
    (1, 56.85, 47.15, 0.23, 0.23, 5.0, '2024-06-02'),
    (2, 59.34, 32.31, 0.15, 0.25, 2.5, '2024-06-04'),
    (3, 79.95, 58.26, 0.24, 0.26, 3.0, '2024-06-03'),
    (4, 88.43, 69.37, 0.18, 0.34, 4.0, '2024-06-04'),
    (5, 54.94, 30.38, 0.15, 0.25, 3.5, '2024-06-05'),
    (6, 55.58, 37.62, 0.19, 0.31, 1.0, '2024-06-06'),
    (7, 40.71, 74.01, 0.05, 0.11, 1.2, '2024-06-07'),
    (8, 34.05, 18.24, 0.23, 0.32, 0.8, '2024-06-10'),
    (9, 51.51, 10.13, 0.12, 0.22, 2.0, '2024-06-11')
]
cursor.executemany('INSERT INTO notes VALUES (?, ?, ?, ?, ?, ?, ?)', notes_data)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных notes.db создана и заполнена данными!")