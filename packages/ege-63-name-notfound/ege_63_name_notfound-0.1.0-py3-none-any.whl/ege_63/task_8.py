from itertools import *

# Под каким номером в списке идёт первое слово, которое начинается с буквы С
# counter = 1
# for i in product(sorted('ПАРУС'), repeat=3):
#     if i[0] == 'С':
#         print(counter)
#         quit()
#     counter += 1

# Повторяющиеся символы, но ограниченное кол-во оперделенных знаков
# counter = 0
# for elem in product('НАСТЯ', repeat=6):
#     if elem.count("А") <= 1 and elem.count("Я") <= 1:
#         counter += 1
#
# print(counter)

# Буква X может появиться на первом месте или не появиться вовсе
# counter = 0
# for elem in product('ABCX', repeat=5):
#     if elem.count("X") == 0 or (elem[0] == 'X' and elem.count("X") == 1):
#         print(elem)
#         counter += 1
#
# print(counter)

# Слово, которое стоит под номером
# counter = 1
# for i in product(sorted('ВИНТ'), repeat=5):
#     if counter == 1020:
#         print(''.join(i))
#         quit()
#     counter += 1

