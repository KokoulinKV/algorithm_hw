# Задание 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

MAX_ITEM = 10
MIN_ITEM = 0
SIZE = 10
m = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

max_num = MIN_ITEM
max_pos = 0
min_num = MAX_ITEM
min_pos = 0

for i in range(len(m)):
    if m[i] > max_num:
        max_num = m[i]
        max_pos = i
    if m[i] < min_num:
        min_num = m[i]
        min_pos = i

print(f'Сгенерированный массив: {m}')
m[max_pos], m[min_pos] = m[min_pos], m[max_pos]
print(f'Максимальное число в массиве: {max_num}, минимальное: {min_num}')
print(f'Массив после перестановки местами максимального и минимального чисел: {m}')
print(f'Местами поменяны числа на позициях {min_pos} и {max_pos} (нумерация с нуля).')
