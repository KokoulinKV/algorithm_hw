# Задание 3.
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
import random


def median(data):
    for i in range(len(data)):
        spam = 0
        for j in range(len(data)):
            if data[j] >= data[i] and i != j:
                spam += 1
            if spam > (len(data) - 1) / 2:
                break
        if spam == (len(data) - 1) / 2:
            return data[i]


SIZE = 10
array = [random.randint(0, 100) for i in range(2 * SIZE + 1)]
print(array)
print(median(array))
