# Задание 1.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

"""
Вариант 1. Без функций

"""

from collections import namedtuple

FactoryNew = namedtuple('FactoryNew', 'name, first, second, third, fourth, aver')
num = int(input('Введите кол-во предприятий: '))
factories = []

for i in range(num):
    f_name = input(f'Введите название {i + 1}-го предприятия: ')
    fst = int(input('Введите сумму прибыли за 1-ый квартал: '))
    snd = int(input('Введите сумму прибыли за 2-ый квартал: '))
    trd = int(input('Введите сумму прибыли за 3-ый квартал: '))
    frth = int(input('Введите сумму прибыли за 4-ый квартал: '))
    aver = (fst + snd + trd + frth) / 4
    factories.append(FactoryNew(f_name, fst, snd, trd, frth, aver))

total_aver = 0

for item in factories:
    total_aver += item.aver
total_aver /= num
print(f'Среднегодовая прибыль для {num} предприятий составила: {total_aver:.2f}')

profitable = []
lossless = []

for item in factories:
    if item.aver > total_aver:
        profitable.append(item.name)
    else:
        lossless.append(item.name)

print(f'Прибыльные предприятия (прибыль выше среднего) - {", ".join(profitable)}')
print(f'Убыльные (прибыль ниже среднего) - {", ".join(lossless)}')

"""
Вариант 2. Добавил создание экземпляров класса FactoryNew, созданного с помощью namedtuple, с помощью ф-ии.

"""

# from collections import namedtuple
#
#
# def fact(n):
#     FactoryNew = namedtuple('FactoryNew', 'name, first, second, third, fourth, aver')
#     f_name = input(f'Введите название {n + 1}-го предприятия: ')
#     fst = int(input('Введите сумму прибыли за 1-ый квартал: '))
#     snd = int(input('Введите сумму прибыли за 2-ый квартал: '))
#     trd = int(input('Введите сумму прибыли за 3-ый квартал: '))
#     frth = int(input('Введите сумму прибыли за 4-ый квартал: '))
#     aver = (fst + snd + trd + frth) / 4
#     return FactoryNew(f_name, fst, snd, trd, frth, aver)
#
#
# num = int(input('Введите кол-во предприятий: '))
# factories = []
#
# for i in range(num):
#     factories.append(fact(i))
#
# total_aver = 0
#
# for item in factories:
#     total_aver += item.aver
#
# total_aver /= num
# print(f'Среднегодовая прибыль для {num} предприятий составила: {total_aver:.2f}')
#
# profitable = []
# lossless = []
#
# for item in factories:
#     if item.aver > total_aver:
#         profitable.append(item.name)
#     else:
#         lossless.append(item.name)
#
# print(f'Прибыльные предприятия (прибыль выше среднего) - {", ".join(profitable)}')
# print(f'Убыльные (прибыль ниже среднего) - {", ".join(lossless)}')
