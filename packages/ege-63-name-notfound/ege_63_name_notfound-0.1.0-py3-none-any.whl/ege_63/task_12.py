# great = ''
# great_i = 0
#
# for i in range(90):
#     print(i)
#     a = '1' * (200+i)
#     while '111' in a or '222' in a:
#         a = a.replace('111', '22', 1)
#         a = a.replace('222', '1', 1)
#     if not '2' in a:
#         print(200+i)
#         break

a = ('8' * 99) + '1'
while '133' in a or '881' in a:
    if '133' in a:
        a = a.replace('133', '81', 1)
    else:
        a = a.replace('881', '13', 1)
print(a)
