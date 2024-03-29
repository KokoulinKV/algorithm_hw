# Ссылка на алгоритмы: https://drive.google.com/file/d/1iA0xd6TVr4Jvg6Vk6Qgr1GIDF8s2r84g/view?usp=sharing

# Задание 6.
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random


def guess_the_number(m, k=10):
    if k == 0:
        return "Вы проиграли!"
    print(f'У Вас осталось {k} попыток.')
    v = int(input('Введите предполагаемое число: '))
    if v == m:
        return 'Вы угадали!'
    elif v > m:
        print('Вы указали число больше загаданного')
        return f'{guess_the_number(m, k - 1)}'
    print('Вы указали число меньше загаданного')
    return f'{guess_the_number(m, k - 1)}'


s = random.randint(0, 100)
print('Компьютер загадал натуральное число от 0 до 100. Попробуйте угадать это число.')
res = guess_the_number(s)
print(f'{res}')
