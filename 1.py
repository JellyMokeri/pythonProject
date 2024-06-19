# Из списка удалить четные элементы, стоящие между максимальным и минимальным элементами.
# Пример: из списка A[7]: 1 8 8 4 7 0 5 должен получиться список A[5]: 1 8 7 0 5.

import random as r

def get_list():
    # Запрашиваем у пользователя способ ввода списка и возвращаем список чисел
    choice = input("Выберите способ ввода списка:\n"
                   "1. Ввести вручную\n"
                   "2. Сгенерировать автоматически\n"
                   "Ваш выбор: ")
    if choice == '1':
        # Ввод списка вручную
        numbers_str = input("Введите элементы списка через пробел: ")
        try:
            lst = [int(x) for x in numbers_str.split()]
        except ValueError:
            print("Некорректный ввод. Введите числа через пробел.")
            return get_list()
    elif choice == '2':
        # Автоматическая генерация списка
        n = int(input("Введите количество элементов списка: "))
        min_value = 0
        max_value = 9
        lst = [r.randint(min_value, max_value) for _ in range(n)]
    else:
        print("Неверный выбор. Попробуйте снова.")
        return get_list()
    return lst

def remove(lst):
  # Удаляем четные элементы, стоящие между максимальным и минимальным элементами списка
  min_index = lst.index(min(lst))
  max_index = lst.index(max(lst))
  start, end = min(min_index, max_index) + 1, max(min_index, max_index)
  lst[start:end] = [x for x in lst[start:end] if x % 2 != 0]

# Основная программа
lst = get_list()
print(f"Исходный список: {lst}")
result = remove(lst)
print(f"Результат: {lst}")


