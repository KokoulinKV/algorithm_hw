# Задание 1.
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random


def bubble_sort(data):
    n = 1
    while n < len(data):
        spam = 0
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                spam += 1
        if spam == 0:
            break
        n += 1


MIN_ITEM = -100
MAX_ITEM = 100
SIZE = 10
array = [random.randint(MIN_ITEM, MAX_ITEM - 1) for i in range(SIZE)]
print(f'Сгенерированный массив: {array}')
bubble_sort(array)
print(f'Отсортированный массив: {array}')
