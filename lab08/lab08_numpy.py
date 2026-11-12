import numpy as np

hours = np.arange(0, 21, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)

print("Задание 1:")
print(f"hours: {hours}")
print(f"shape: {hours.shape}, ndim: {hours.ndim}, size: {hours.size}, dtype: {hours.dtype}")
print()

print("Задание 2:")
print(f"Третий элемент (индекс 2): {hours[2]}")
print(f"Последний элемент: {hours[-1]}")
print(f"Элементы с индексами 2–5: {hours[2:6]}")
print(f"Каждый второй элемент: {hours[::2]}")
print(f"Массив в обратном порядке: {hours[::-1]}")
print()

# --- Задание 3. Строки и столбцы таблицы ---
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Задание 3:")
print(f"Форма: {temperatures.shape}, ndim: {temperatures.ndim}, size: {temperatures.size}")
print(f"Значение из второй строки и третьего столбца: {temperatures[1, 2]}")
print(f"Первая строка: {temperatures[0]}")
print(f"Последний столбец: {temperatures[:, -1]}")
print(f"Первые две строки без первого столбца: {temperatures[:2, 1:]}")
print(f"Центральный фрагмент 2x2: {temperatures[0:2, 1:3]}")
print()

# --- Задание 4. Прямоугольные срезы ---
matrix = np.arange(1, 26).reshape(5, 5)

print("Задание 4:")
first_three_rows = matrix[:3]
print(f"Первые три строки:\n{first_three_rows}\nshape: {first_three_rows.shape}")

last_two_rows = matrix[-2:]
print(f"Последние две строки:\n{last_two_rows}\nshape: {last_two_rows.shape}")

first_two_cols = matrix[:, :2]
print(f"Первые два столбца:\n{first_two_cols}\nshape: {first_two_cols.shape}")

fragment = matrix[1:4, 2:5]
print(f"Фрагмент (строки 1–3, столбцы 2–4):\n{fragment}\nshape: {fragment.shape}")

corner_block = matrix[-2:, -2:]
print(f"Угловой блок 2x2 в правом нижнем углу:\n{corner_block}\nshape: {corner_block.shape}")
print()

# --- Задание 5. Изменение массива с помощью срезов ---
# Работа с вектором hours
hours_original = np.arange(0, 24, 3)
changed_hours = hours_original.copy()
# Замена элементов с индексами 2–4 на 99
changed_hours[2:5] = 99
# Замена каждого второго элемента, начиная с первого (индекс 1), на -1
changed_hours[1::2] = -1

print("Задание 5 (Вектор):")
print(f"changed_hours: {changed_hours}")
print(f"Исходный hours: {hours_original}")
# Комментарий: .copy() нужна, чтобы изменения в changed_hours не затронули исходный массив hours_original.
# Без копирования NumPy создает "вид" (view), и обе переменные указывали бы на одну область памяти.

# Работа с матрицей matrix
matrix_original = np.arange(1, 26).reshape(5, 5)
changed_matrix = matrix_original.copy()
# Замена всей второй строки (индекс 1) на нули
changed_matrix[1, :] = 0
# Замена последнего столбца на -1
changed_matrix[:, -1] = -1
# Замена центрального блока 3x3 (индексы 1–3) на 100
changed_matrix[1:4, 1:4] = 100

print(f"\nИтоговая changed_matrix:\n{changed_matrix}")
print(f"Исходная matrix:\n{matrix_original}")
print()

# --- Задание 6. Изменение формы ---
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Задание 6:")
print(f"numbers shape: {numbers.shape}")
print(f"table shape: {table.shape}")
print(f"transposed shape: {transposed.shape}")

# Объяснение reshape:
# reshape(3, 4) работает, так как 3 * 4 = 12, что совпадает с общим числом элементов в numbers.
# reshape(5, 3) вызовет ошибку ValueError, так как 5 * 3 = 15, а элементов всего 12. 
# Общее количество элементов при изменении формы должно оставаться неизменным.


