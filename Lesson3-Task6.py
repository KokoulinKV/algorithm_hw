# Задание 6.
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

MAX_ITEM = 20
MIN_ITEM = -20
SIZE = 10
m = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

max_neg = MIN_ITEM

for i in range(len(m)):
    if m[i] < 0:
        num = m[i]
        if num > max_neg:
            max_neg = num

print(f'Сгенерированный массив: {m}')
print(f'Максимальный отрицательный элемент в массиве: {max_neg}')
