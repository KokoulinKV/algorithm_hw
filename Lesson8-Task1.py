# Задание 1.
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.


def hash_substring(s):
    lst = []
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if hash(s[i:j]) not in lst and s[i:j] != '' and s[i:j] != s:
                lst.append(hash(s[i:j]))
    return len(lst)


in_str = input('Ввведите текст: ')
print(f'Количество уникальных подстрок в веденной строке: {hash_substring(in_str)}')
