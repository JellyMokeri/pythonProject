# Пусть дана некоторая директория (папка). Посчитайте количество файлов в данной директории (папке) и выведите на экран.
# Пусть дан файл data.csv, в котором содержится информация в соответствии с вариантом:
# Считайте информацию из файла в соответствующую структуру (словарь):
# 2.1. Выведите информацию об объектах, отсортировав их по одному полю (строковому).
# 2.2. Выведите информацию об объектах, отсортировав их по одному полю (числовому).
# 2.3. Выведите информацию, соответствующую какому-либо критерию (например, для студентов - тех, у кого возраст больше какого-либо значения)
# Добавьте к программе возможность сохранения новых данных обратно в файл.
# Временная шкала показаний осадков (прямоугольная область): №, широта, долгота, ширина, длина, мм/ч, дата и время

import os
import csv

directory_path = "C:\\Users\\User\\PycharmProjects\\pythonProject"
items = os.listdir(directory_path)
file_count = 0
# Проходим по каждому элементу в списке
for item in items:
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path):
        file_count += 1
# Выводим количество файлов на экран
print(f"Количество файлов в директории '{directory_path}': {file_count}")

def read_precipitation_data(filename):
    # Читаем данные из CSV-файла и возвращаем список словарей
    data = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Преобразуем числовые значения
                row['№'] = int(row['№'])
                row['широта'] = float(row['широта'])
                row['долгота'] = float(row['долгота'])
                row['ширина'] = float(row['ширина'])
                row['длина'] = float(row['длина'])
                row['мм/ч'] = float(row['мм/ч'])
                data.append(row)
            except ValueError as e:
                print(f"Пропущен некорректный ряд: {row}. Ошибка: {e}")
    return data

def print_data(data):
    # Выводим исходную информацию
    for row in data:
        print(row)

def save_precipitation_data(filename, data):
    # Сохраняем данные в CSV-файл
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['№', 'широта', 'долгота', 'ширина', 'длина', 'мм/ч', 'дата и время']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    filename = "data.csv"
    new_filename = "processed_data.csv"
    precipitation_data = read_precipitation_data(filename)

    print("Сортировка по строковому полю (дата и время)")
    sorted_by_date = sorted(precipitation_data, key=lambda x: x['дата и время'])
    print_data(sorted_by_date)

    print("Сортировка по числовому полю (мм/ч)")
    sorted_by_mm = sorted(precipitation_data, key=lambda x: x['мм/ч'])
    print_data(sorted_by_mm)

    print("Сортировка по критерию (мм/ч > 2.5)")
    filtered_data = [row for row in precipitation_data if row['мм/ч'] > 2.5]
    print_data(filtered_data)

    # Сохранение обработанных данных в новый файл
    processed_data = {
        "Сортировка по дате": sorted_by_date,
        "Сортировка по мм/ч": sorted_by_mm,
        "Осадки с мм/ч больше 2.5": filtered_data
    }

    with open(new_filename, 'w', newline='', encoding='utf-8') as csvfile:
        for title, data in processed_data.items():
            csvfile.write(f"{title}\n")
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys() if data else [])
            writer.writeheader()
            writer.writerows(data)
    print(f"Новые данные сохранены в файл '{new_filename}'")
