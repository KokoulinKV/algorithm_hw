from collections import Counter


def ch_code(in_str):
    s = Counter(in_str)
    spam = []
    for key in s.keys():
        spam.append([key, ''])
    while len(s) > 1:
        k = s.most_common()[:-3:-1]
        for i in spam:
            if i[0] in k[0][0].split(','):
                i[1] += '0'
            if i[0] in k[1][0].split(','):
                i[1] += '1'

        del s[k[0][0]]
        del s[k[1][0]]

        s[f'{k[1][0]},{k[0][0]}'] = k[0][1] + k[1][1]
    for i in spam:
        i[1] = i[1][::-1]
    return spam


def coding(code_lst, str_for_code):
    lst = []
    for ch in str_for_code:
        for el in code_lst:
            if ch == el[0]:
                lst.append(el[1])
    return ''.join(lst)


def check(code_lst, coding_str):
    lst = []
    z = 0
    for i in range(len(coding_str) + 1):
        for el in code_lst:
            if coding_str[z:i] == el[1]:
                lst.append(el[0])
                z = i

    return ''.join(lst)


user_str = input('Введите текст: ')
code_str = coding(ch_code(user_str), user_str)
check_str = check(ch_code(user_str), code_str)
print(f'Текст был закодирован по алгоритму Хаффмана: {code_str}')
print(f'Для проверки работы алгоритма код был декодирован, получилось следующее: {check_str}')
