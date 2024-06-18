# Сделать телеграм бота, который выводит данные из базы данных и позволяет их добавлять

import telebot
import sqlite3

# Токен
bot = telebot.TeleBot('7488382741:AAE8N7JvcjZkqTobvkI_iRn7W3msCphOtcw')

# Подключение к базе данных
conn = sqlite3.connect('notes.db', check_same_thread=False)
cursor = conn.cursor()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Привет! Вот список доступных команд:\n'
                     '/add - добавить данные\n'
                     '/delete - удалить данные\n'
                     '/show - показать все данные')

# Обработчик команды /add
@bot.message_handler(commands=['add'])
def add_data(message):
    msg = bot.reply_to(message, "Введите данные в формате:\n"
                               "широта, долгота, ширина, длина, мм/ч, дата (гггг-мм-дд)")
    bot.register_next_step_handler(msg, process_adding_data)

def process_adding_data(message):
    try:
        data = message.text.split(",")
        latitude = float(data[0].strip())
        longitude = float(data[1].strip())
        width = float(data[2].strip())
        length = float(data[3].strip())
        mm_per_hour = float(data[4].strip())
        datetime_str = data[5].strip()

        cursor.execute("INSERT INTO notes (latitude, longitude, width, length, mm_per_hour, datetime) "
                       "VALUES (?, ?, ?, ?, ?, ?)",
                       (latitude, longitude, width, length, mm_per_hour, datetime_str))
        conn.commit()
        bot.reply_to(message, "Данные успешно добавлены!")
    except (IndexError, ValueError):
        bot.reply_to(message, "Неверный формат данных. Попробуйте снова.")

# Обработчик команды /delete
@bot.message_handler(commands=['delete'])
def delete_data(message):
    msg = bot.reply_to(message, "Введите ID строки для удаления:")
    bot.register_next_step_handler(msg, process_deleting_data)

def process_deleting_data(message):
    try:
        row_id = int(message.text)
        cursor.execute("DELETE FROM notes WHERE id=?", (row_id,))
        conn.commit()
        bot.reply_to(message, f"Строка с ID {row_id} удалена.")
    except ValueError:
        bot.reply_to(message, "Неверный формат ID. Введите число.")

# Обработчик команды /show
@bot.message_handler(commands=['show'])
def show_data(message):
    cursor.execute("SELECT * FROM notes")
    data = cursor.fetchall()
    if data:
        response = "Данные в базе:\n\n"
        for row in data:
            response += f"ID: {row[0]}, Широта: {row[1]}, Долгота: {row[2]}, " \
                       f"Ширина: {row[3]}, Длина: {row[4]}, " \
                       f"мм/ч: {row[5]}, Дата: {row[6]}\n\n"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "База данных пуста.")


# Запуск бота
bot.polling(none_stop=True)
