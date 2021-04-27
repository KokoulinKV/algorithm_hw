# Задание 1.
# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

# Урок 2 - Задание 2:
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import timeit
import cProfile


# 1. Рекурсия

def even_odd(n, e=0, o=0):
    if n == 0:
        return f'Количество четных цифр в числе - {e}, нечетных - {o}.'
    elif n % 2 == 0:
        return f'{even_odd(n // 10, e + 1, o)}'
    return f'{even_odd(n // 10, e, o + 1)}'


print(timeit.timeit('even_odd(1212)', number=1000, globals=globals()))  # 0.0010307999999999984
print(timeit.timeit('even_odd(121212)', number=1000, globals=globals()))  # 0.001349900000000001
print(timeit.timeit('even_odd(12121212)', number=1000, globals=globals()))  # 0.0017376999999999983
print(timeit.timeit('even_odd(1212121212)', number=1000, globals=globals()))  # 0.0020822999999999987
print(timeit.timeit('even_odd(121212121212)', number=1000, globals=globals()))  # 0.0024916
print(timeit.timeit('even_odd(12121212121212)', number=1000, globals=globals()))  # 0.0029525000000000003
print(timeit.timeit('even_odd(1212121212121212)', number=1000, globals=globals()))  # 0.0033894000000000007
print(timeit.timeit('even_odd(121212121212121212121212121212121212121212121212121212121212121'
                    '21212121212121212121212121212121212121212121212121212121212121212)', number=1000,
                    globals=globals()))  # 0.0342117

cProfile.run('even_odd(1212121212121212121212121212121212121212121212121212121212121'
             '2121212121212121212121212121212121212121212121212121212121212121212)')


#   132 function calls (4 primitive calls) in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     129/1    0.000    0.000    0.000    0.000 Lesson4-Task1.py:15(even_odd)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 2. For с num-строка

def for_num(n, e=0, o=0):
    for item in n:
        if int(item) % 2 == 0:
            e += 1
        else:
            o += 1
    return e, o


print(timeit.timeit('for_num(str(1212))', number=1000, globals=globals()))  # 0.0008821999999999997
print(timeit.timeit('for_num(str(121212))', number=1000, globals=globals()))  # 0.0010933999999999944
print(timeit.timeit('for_num(str(12121212))', number=1000, globals=globals()))  # 0.0014008000000000076
print(timeit.timeit('for_num(str(1212121212))', number=1000, globals=globals()))  # 0.0016291999999999973
print(timeit.timeit('for_num(str(121212121212))', number=1000, globals=globals()))  # 0.0018855000000000122
print(timeit.timeit('for_num(str(12121212121212))', number=1000, globals=globals()))  # 0.0022009000000000056
print(timeit.timeit('for_num(str(1212121212121212))', number=1000, globals=globals()))  # 0.002451700000000001
print(timeit.timeit('for_num(str(121212121212121212121212121212121212121212121212121212121212121'
                    '21212121212121212121212121212121212121212121212121212121212121212))', number=1000,
                    globals=globals()))  # 0.018087699999999984

cProfile.run('for_num(str(12121212121212121212121212121212121212121212121212121212121212'
             '121212121212121212121212121212121212121212121212121212121212121212))')


# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4-Task1.py:51(for_num)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 3. While с целочисленным num

def while_num(n, e=0, o=0):
    while True:
        if n == 0:
            return e, o
            # break
        elif n % 2 == 0:
            e += 1
        else:
            o += 1
        n //= 10


print(timeit.timeit('while_num(1212)', number=1000, globals=globals()))  # 0.0005532000000000037
print(timeit.timeit('while_num(121212)', number=1000, globals=globals()))  # 0.000804100000000002
print(timeit.timeit('while_num(12121212)', number=1000, globals=globals()))  # 0.0010441999999999951
print(timeit.timeit('while_num(1212121212)', number=1000, globals=globals()))  # 0.001333600000000018
print(timeit.timeit('while_num(121212121212)', number=1000, globals=globals()))  # 0.001598199999999994
print(timeit.timeit('while_num(12121212121212)', number=1000, globals=globals()))  # 0.0019498999999999767
print(timeit.timeit('while_num(1212121212121212)', number=1000, globals=globals()))  # 0.002229800000000004
print(timeit.timeit('while_num(121212121212121212121212121212121212121212121212121212121212121'
                    '21212121212121212121212121212121212121212121212121212121212121212)', number=1000,
                    globals=globals()))  # 0.024713700000000005

cProfile.run('while_num(121212121212121212121212121212121212121212121212121212121212121'
             '21212121212121212121212121212121212121212121212121212121212121212)')
# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4-Task1.py:88(while_num)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод:
# Вариант №2 и №3 отрабатывают быстрее и осуществляют меньшее кол-во вызовов ф-ий, чем вариант №1.
# Вариант №2 немного уступает варианту №3 по времени выполнения для входных данных малой длины,
# но выигрывает при входных данных большой длины.
# Таким образом, самым быстрым и оптимальным явлется вариант №2 - использование цикла for,
# работающего со строчным типом данных.
