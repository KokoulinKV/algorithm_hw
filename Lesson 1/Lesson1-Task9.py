# Ссылка на алгоритмы: https://drive.google.com/file/d/1JAUZIPyL-3bvpw4xEZAGuQZx3pp8400y/view?usp=sharing

# Задание 9.
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три разных числа.')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b:
    if a > c:
        if b > c:
            print(f'Число {b} среднее по значению из введеных чисел.')
        else:
            print(f'Число {c} среднее по значению из введеных чисел.')
    else:
        print(f'Число {a} среднее по значению из введеных чисел.')
else:
    if a > c:
        print(f'Число {a} среднее по значению из введеных чисел.')
    else:
        if b > c:
            print(f'Число {c} среднее по значению из введеных чисел.')
        else:
            print(f'Число {b} среднее по значению из введеных чисел.')
