# Ссылка на алгоритмы: https://drive.google.com/file/d/1JAUZIPyL-3bvpw4xEZAGuQZx3pp8400y/view?usp=sharing

# Задание 1.
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


a = int(input('Введите трехзначное число: '))
b = a // 100  # Сотни
c = a // 10 - b * 10  # Десятки
d = a % 10  # Единицы

print(f'Сумма цифр, составляющих введенное число: {b + c + d}')
print(f'Произведение цифр, составляющих введенное число: {b * c * d}')
