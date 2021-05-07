# Задание 2.
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge(left, right):
    res = []
    spam = 0
    eggs = 0
    while spam < len(left) and eggs < len(right):
        if left[spam] > right[eggs]:
            res.append(right[eggs])
            eggs += 1
        else:
            res.append(left[spam])
            spam += 1
    if eggs < len(right):
        res.extend(right[eggs:])
    else:
        res.extend(left[spam:])
    return res


def merge_sort(data):
    if len(data) == 1:
        return data
    return merge(merge_sort(data[:len(data) // 2]), merge_sort(data[len(data) // 2:]))


MIN_ITEM = 0
MAX_ITEM = 50
SIZE = 10
array = [random.uniform(MIN_ITEM, MAX_ITEM - 1) for i in range(SIZE)]
print(f'Сгенерированный массив: {array}')
print(f'Отсортированный массив: {merge_sort(array)}')
