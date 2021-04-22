# Задание 2.
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

MAX_ITEM = 10
MIN_ITEM = 0
SIZE = 10
m_fst = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

m_snd = []

for i in range(len(m_fst)):
    if m_fst[i] % 2 == 0:
        m_snd.append(i)

print(f'Первый массив: {m_fst}')
print(f'Второй массив: {m_snd}')
