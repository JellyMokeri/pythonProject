# Из списка удалить четные элементы, стоящие между максимальным и минимальным элементами.
# Пример: из списка A[7]: 1 8 8 4 7 0 5 должен получиться список A[5]: 1 8 7 0 5.

import random as r

def get_list():
    # Запрашиваем у пользователя данные
    choice = input("Выберите способ ввода списка:\n"
                   "1. Ввести вручную\n"
                   "2. Сгенерировать автоматически\n"
                   "Ваш выбор: ")
    if choice == '1':
        # Ввод списка вручную
        numbers_str = input("Введите элементы списка через пробел: ")
        try:
            lst = [a for a in numbers_str.split()]
        except ValueError:
            print("Некорректный ввод. Введите числа через пробел.")
            return get_list()
    elif choice == '2':
        # Ввод списка автоматически
        n = int(input("Введите количество элементов списка: "))
        lst = [r.randint(0, 9) for _ in range(n)]
    else:
        print("Неверный выбор. Попробуйте снова.")
        return get_list()
    return lst

def remove(lst):
    # Удаляем четные элементы, стоящие между максимальным и минимальным элементами списка
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    start, end = min(min_index, max_index) + 1, max(min_index, max_index)
    lst[start:end] = [х for х in lst[start:end] if х % 2 != 0]
    return lst

# Основная программа
lst = get_list()
print(f"Исходный список: {lst}")
lst = remove(lst)
print(f"Результат: {lst}")


