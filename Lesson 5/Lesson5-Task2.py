# Задание 2.
# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

hexadecimal_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
decimal_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_(n1, n2):
    if len(n1) > len(n2):  # проверяем чтобы первое переданное число было больше второго
        n1_sum = n1.copy()
        n2_sum = n2.copy()
    else:
        n1_sum = n2.copy()
        n2_sum = n1.copy()
    result = deque([])
    spam = 0
    while len(n1_sum) != 0:
        if len(n2_sum) != 0:
            res = hexadecimal_dict[n1_sum.pop()] + hexadecimal_dict[n2_sum.pop()] + spam
        else:
            res = hexadecimal_dict[n1_sum.pop()] + spam
        spam = 0
        if res > 16:
            result.appendleft(decimal_dict[res - 16])
            spam = 1
        else:
            result.appendleft(decimal_dict[res])
    return result


'''
Функция mult_() постороена по принципу перемножения дву- или более значных чисел в столбик.

'''


def mult_(n1, n2):
    if len(n1) > len(n2):  # проверяем чтобы первое переданное число было больше второго
        n1_mult = n1.copy()
        n2_mult = n2.copy()
    else:
        n1_mult = n2.copy()
        n2_mult = n1.copy()
    result_ex = deque()
    spam = 0  # переменная отслеживает какое по счету число получилось для сложения в столбик
    while len(n2_mult) != 0:
        result = deque()
        n1_copy = n1_mult.copy()
        eggs = 0
        while len(n1_copy) != 0:  # цикл перемножающий по разряду числа 2 на все число 1 (пример: 2*С4F, A*C4F)
            mid_res = (hexadecimal_dict[n1_copy.pop()] * hexadecimal_dict[n2_mult[len(n2_mult) - 1]] + eggs)
            res = mid_res % 16  # число
            eggs = mid_res // 16  # в уме
            result.appendleft(decimal_dict[res])
        else:
            if eggs != 0:  # дописываем, что осталось после перемножения 2*С или A*C
                result.appendleft(decimal_dict[eggs])
            n2_mult.pop()  # уменьшаем число для дальнейшей работы A2 -> A
            if len(result_ex) == 0:  # если результат пустой - добавляем в очередь новое число
                result_ex.append(result)
            else:
                for i in range(spam):  # имитируем сложение в столбик при умножении двух двухзначных(или больших) чисел
                    result.append('0')
                result_ex.append(sum_(result_ex.pop(), result))  # выполняем промежуточное сложение двух чисел в столбик
            spam += 1
    return result_ex.pop()


num1 = deque(input('Введите первое число в 16-ой системе счисления: ').upper())
num2 = deque(input('Введите второе число в 16-ой системе счисления: ').upper())

print(f'Сумма введенных чисел: {"".join(sum_(num1, num2))}')
print(f'Произведение введенных чисел: {"".join(mult_(num1, num2))}')
