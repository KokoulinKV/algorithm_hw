# Ссылка на алгоритмы: https://drive.google.com/file/d/1iA0xd6TVr4Jvg6Vk6Qgr1GIDF8s2r84g/view?usp=sharing

# Задание 2.
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def even_odd(n, e=0, o=0):
    if n == 0:
        return f'Количество четных цифр в числе - {e}, нечетных - {o}.'
    elif n % 2 == 0:
        return f'{even_odd(n//10, e+1, o)}'
    return f'{even_odd(n // 10, e, o+1)}'


num = int(input("Введите натуральное число: "))
res = even_odd(num)
print(res)