"""
    Десятичное число в двоичное      'f"{x:b}"'
    Десятичное число в двоичное 8bit 'f"{x:08b}"'
    Двоичное в десятичное            'int(x, 2)'
    Убрать цифру из числа            'str(x)[:-1]'
    Четное число                     'x % 2 == 0'
    Числа от x до y                  'range(x, y)'
    Сортировка списка (↑)            'data.sort()'
    Сортировка списка (↓)            'data.sort(reverse=True)'
    Модуль числа                     'abs(x)
    Остановить код                   'break'
"""


# Противоположоное восьмибитное

# for i in range(0, 255):
#     a = int(f"{i:08b}".replace('0', '#').replace('1', '0').replace('#', '1'),2)
#     if a - i == 111:
#         print(i)


# каждая цифра числа нечетная

# counter = 0
# for i in range(1000, 10000):
#     num = str(i)
#     i_1 = int(num[0])
#     i_2 = int(num[1])
#     i_3 = int(num[2])
#     i_4 = int(num[3])
#     i_sum = (i_1 + i_2, i_3 + i_4)
#
#     counter += 1 if i_1 *i_2 * i_3 * i_4 % 2 == 1 and f'{min(i_sum)}{max(i_sum)}' == '616' else 0
# print(counter)

# четное не четное двоичное число

# for i in range(9999):
#     num = int(f'{"1" if i % 2 == 0 else "11"}{i:b}{"0" if i % 2 == 0 else "11"}', 2)
#     if num > 52:
#         print(i)
#         break


# Сумма цифр в двоичных числах

# for i in range(9999):
#     num = f'{i:b}'
#     zero = 0
#     one = 0
#
#     for index in range(1, len(num)+1):
#         if index % 2 == 0:
#             one += 1 if num[index-1] == '1' else 0
#         else:
#             zero += 1 if num[index-1] == '0' else 0
#
#     if abs(one - zero) == 5:
#         print(i)
#         break


# Произведение 1-2 2-3 и т.д. чисел
#
# for i in range(100, 999):
#     num = str(i)
#     data = [int(num[0]) * int(num[1]), int(num[1]) * int(num[2])]
#     data.sort()
#     res = str(data[0]) + str(data[1])
#     if res == '621':
#         print(i)
#         break
