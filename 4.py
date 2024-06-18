# Необходимо переделать лабораторную работу №3 с использованием классов, описывающих предметную область,
# заданную вариантом, с реализацией следующих особенностей (вполне возможно,
# что предлагаемое в 3 лабе задание для этого нужно будет расширить):

import os
import csv

def set_attributes(obj, attributes):
    for key, value in attributes.items():
        if isinstance(obj, dict):
            obj[key] = value
        else:
            setattr(obj, key, value)

class DataProcessor:
    def __init__(self, directory_path, filename, new_filename):
        set_attributes(self, locals())
        self.file_count = 0

    def __iter__(self):
        # Возвращает итератор для данных об осадках
        self.current_index = 0
        return self

    def __next__(self):
        # Возвращает следующий элемент данных об осадках
        if self.current_index >= len(self.data):
            raise StopIteration
        result = self.data[self.current_index]
        self.current_index += 1
        return result

    def __repr__(self):
        # Возвращает строковое представление объекта
        return f"DataProcessor(data={self._data})"

    def __getitem__(self, index):
        # Возвращает элемент данных об осадках по индексу
        return self.data[index]

    @staticmethod
    def validate_coordinates(latitude, longitude):
        """Проверяет, находятся ли координаты в допустимых диапазонах.
        Args:
            latitude: Широта.
            longitude: Долгота.
        Returns:
            True, если координаты допустимы, иначе False.
        """
        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            return True
        return False

    @staticmethod
    def calculate_average_precipitation(data):
        """Вычисляет среднее количество осадков.
        Args:
            data: Список словарей с данными об осадках.
        Returns:
            Среднее количество осадков.
        """
        total_precipitation = sum(row['мм/ч'] for row in data)
        return total_precipitation / len(data) if data else 0

    def count_files(self):
        for item in os.listdir(self.directory_path):
            item_path = os.path.join(self.directory_path, item)
            if os.path.isfile(item_path):
                self.file_count += 1
        print(f"Количество файлов в директории '{self.directory_path}': {self.file_count}")

    def read_precipitation_data(self):
        self.data = []
        for row in self.csv_reader(self.filename):  # Используем генератор
            try:
                set_attributes(row, {
                    '№': int(row['№']),
                    'широта': float(row['широта']),
                    'долгота': float(row['долгота']),
                    'ширина': float(row['ширина']),
                    'длина': float(row['длина']),
                    'мм/ч': float(row['мм/ч'])
                })
                self.data.append(row)
            except ValueError as e:
                print(f"Пропущен некорректный ряд: {row}. Ошибка: {e}")

    def csv_reader(self, filename):
        # Генератор для чтения данных из CSV файла
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row

    def print_data(self, data):
        for row in data:
            print(row)

    def save_precipitation_data(self, filename, data):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['№', 'широта', 'долгота', 'ширина', 'длина', 'мм/ч', 'дата и время']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def process_data(self):
        self.read_precipitation_data()

        set_attributes(self, {
            'sorted_by_date': sorted(self.data, key=lambda x: x['дата и время']),
            'sorted_by_mm': sorted(self.data, key=lambda x: x['мм/ч']),
            'filtered_data': [row for row in self.data if row['мм/ч'] > 2.5]
        })

        print("Сортировка по строковому полю (дата и время)")
        self.print_data(self.sorted_by_date)

        print("Сортировка по числовому полю (мм/ч)")
        self.print_data(self.sorted_by_mm)

        print("Осадки с мм/ч больше 2.5")
        self.print_data(self.filtered_data)

        processed_data = {
            "Сортировка по дате": self.sorted_by_date,
            "Сортировка по мм/ч": self.sorted_by_mm,
            "Осадки с мм/ч больше 2.5": self.filtered_data
        }

        with open(self.new_filename, 'w', newline='', encoding='utf-8') as csvfile:
            for title, data in processed_data.items():
                csvfile.write(f"{title}\n")
                writer = csv.DictWriter(csvfile, fieldnames=data[0].keys() if data else [])
                writer.writeheader()
                writer.writerows(data)
        print(f"Новые данные сохранены в файл '{self.new_filename}'")

class ExtendedPrecipitationData(DataProcessor):
    # Расширенный класс с генератором, наследующий DataProcessor

    def __init__(self, data=None):
        super().__init__(data)

    def get_data_by_date_range(self, start_date, end_date):
        # Генератор для получения данных в заданном диапазоне дат
        for item in self._data:
            if start_date <= item['дата и время'] <= end_date:
                yield item


if __name__ == "__main__":
    processor = DataProcessor("C:\\Users\\User\\PycharmProjects\\pythonProject", "data2.csv", "processed_data2.csv")
    processor.count_files()
    processor.process_data()

    # Пример использования статических методов
    valid_coordinates = DataProcessor.validate_coordinates(55.75, 37.62)  # Москва
    print(f"Координаты допустимы: {valid_coordinates}")

    average_mm = DataProcessor.calculate_average_precipitation(processor.data)
    print(f"Среднее количество осадков: {average_mm}")

