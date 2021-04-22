# Задание 4.
#  Определить, какое число в массиве встречается чаще всего.

import random

MAX_ITEM = 10
MIN_ITEM = 0
SIZE = 10
m = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

num = 0
max_count = 0

for j in range(len(m)):
    count = 1
    for k in range(j + 1, len(m)):
        if m[j] == m[k]:
            count += 1
    if count > max_count:
        max_count = count
        num = m[j]
print(f'Сгенерированный массив: {m}')
print(f'В сгенерированном массиве число "{num}" встречается чаще всего: {max_count} раз(а).')
