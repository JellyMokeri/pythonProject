# Выполнить обработку элементов прямоугольной матрицы A, имеющей N строк и M столбцов. Все элементы имеют целый тип.
# Дано целое число H. Определить, какие столбцы имеют хотя бы одно такое число, а какие не имеют.

import numpy as np

# Задаем размер матрицы
N = int(input("Введите количество строк матрицы (N): "))
M = int(input("Введите количество столбцов матрицы (M): "))
# Генерируем матрицу A со случайными целыми числами
A = np.random.randint(0, 9, size=(N, M))
# Вводим число H для поиска
H = int(input("Введите число H: "))
# Находим столбцы, содержащие число H
columns_with_H = np.any(A == H, axis=0)
# Находим столбцы, не содержащие число H
columns_without_H = np.logical_not(columns_with_H)

# Сохраняем результаты в файл
with open("result.txt", "w") as file:
    file.write("Исходная матрица A:\n")
    file.write(str(A))
    file.write("\nЧисло H: ")
    file.write(str(H))
    file.write("\nНомера столбцов, содержащих H:\n")
    file.write(str(np.where(columns_with_H)[0]))
    file.write("\nНомера столбцов, не содержащих H:\n")
    file.write(str(np.where(columns_without_H)[0]))

# Выводим результаты на экран
print("Исходная матрица A:\n", A)
print("Число H:", H)
print("Номера столбцов, содержащих H:", np.where(columns_with_H)[0])
print("Номера столбцов, не содержащих H:", np.where(columns_without_H)[0])
