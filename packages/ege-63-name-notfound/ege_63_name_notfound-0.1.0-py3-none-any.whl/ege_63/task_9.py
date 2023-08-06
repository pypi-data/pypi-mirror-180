import pandas as pd

excel_data = pd.read_excel('107_9.xlsx')
data = pd.DataFrame(excel_data).values.tolist()

# max_difference = 0
#
# print(sum(data, []))
# for row in data:
#     for elem_index in range(2, len(row)):
#         difference = row[elem_index] - row[elem_index-1]
#         max_difference = difference if difference > max_difference else max_difference
#
# print(round(max_difference))

counter = 0
for elem in data:
    print(elem)
    num = sorted(elem)
    if (num[4] + num[0])**2 > (num[1]**2 + num[2]**2 + num[3]**2):
        counter +=1
print(counter)
