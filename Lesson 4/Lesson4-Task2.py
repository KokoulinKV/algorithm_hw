# Задание 2.
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import timeit
import cProfile


# 1. Решето
def sieve_func(in_num):
    hole = 0
    n = 1000
    sieve = [i for i in range(n)]

    sieve[1] = hole
    for i in range(2, n):
        if sieve[i] != hole:
            j = i + i
            while j < n:
                sieve[j] = hole
                j += i

    res = [item for item in sieve if item != hole]
    return res[in_num]


print(timeit.timeit('sieve_func(2)', number=1000, globals=globals()))  # 0.1919475
print(timeit.timeit('sieve_func(4)', number=1000, globals=globals()))  # 0.19248379999999998
print(timeit.timeit('sieve_func(8)', number=1000, globals=globals()))  # 0.192067
print(timeit.timeit('sieve_func(16)', number=1000, globals=globals()))  # 0.18859009999999998
print(timeit.timeit('sieve_func(32)', number=1000, globals=globals()))  # 0.19019260000000004
print(timeit.timeit('sieve_func(64)', number=1000, globals=globals()))  # 0.19008119999999995
print(timeit.timeit('sieve_func(132)', number=1000, globals=globals()))  # 0.1923349000000001

cProfile.run('sieve_func(167)')
#           6 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Lesson4-Task2.py:18(sieve_func)
#        1    0.000    0.000    0.000    0.000 Lesson4-Task2.py:21(<listcomp>)
#        1    0.000    0.000    0.000    0.000 Lesson4-Task2.py:31(<listcomp>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 2. Без решето

def classic(n):
    res = [2]  # число 2 является простым и четным
    for i in range(3, 1000, 2):  # "шаг = 2" исключает все четные числа
        count = 0
        for k in range(3, i, 2):  # "шаг = 2" исключает все четные числа
            if i % k == 0:
                count += 1
                break
        if count == 0:
            res.append(i)
    return res[n]


print(timeit.timeit('classic(2)', number=100, globals=globals()))  # 0.18115520000000007
print(timeit.timeit('classic(4)', number=1000, globals=globals()))  # 1.7581825000000002
print(timeit.timeit('classic(8)', number=1000, globals=globals()))  # 1.7457385000000003
print(timeit.timeit('classic(16)', number=1000, globals=globals()))  # 1.7464887999999998
print(timeit.timeit('classic(32)', number=1000, globals=globals()))  # 1.7854667999999991
print(timeit.timeit('classic(64)', number=1000, globals=globals()))  # 1.7574178000000007
print(timeit.timeit('classic(132)', number=1000, globals=globals()))  # 1.7689397000000007

cProfile.run('classic(167)')
#   171 function calls in 0.002 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#        1    0.002    0.002    0.002    0.002 Lesson4-Task2.py:59(classic)
#        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      167    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод:
# Вариант 1, использующий "Решето Эратосфена" работает примерно в 10 раз быстрее,
# нежели метод представленный в варианте 2. Вариант 2 производит 171 вызов ф-ии против 6 у варианта 1.
# В варианте 2 метод ".append()" вызывается 167 раз.
# Таким образом, вариант 1 (вариант использующий "Решето Эратосфена") является самым быстрым и оптимальным
# из 2-х предложенных.
