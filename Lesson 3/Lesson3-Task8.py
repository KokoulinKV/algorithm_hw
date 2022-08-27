# Задание 8.
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

LINE = 5
COLUMN = 4

m = []
for i in range(LINE):
    line = []
    sum_line = 0
    for j in range(COLUMN):
        if j == COLUMN - 1:
            line.append(sum_line)
            m.append(line)
        else:
            new_num = int(input(f'Введите {j + 1}-е значение {i + 1}-й строки: '))
            line.append(new_num)
            sum_line += new_num

print('Получившаяся матрица:')
for i in range(LINE):
    for j in range(COLUMN):
        m[i][j] = str(m[i][j])
    print("  ".join(m[i]))
