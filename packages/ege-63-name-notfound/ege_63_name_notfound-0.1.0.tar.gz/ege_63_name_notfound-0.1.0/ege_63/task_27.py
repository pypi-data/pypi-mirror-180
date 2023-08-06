data = [line.strip().split(' ') for line in open('27-B_demo.txt').readlines()]
sum = 0
min_difference = 1000000
for i in data:
    a = int(i[0])
    b = int(i[1])
    sum += max(a, b)
    difference = abs(a - b)
    if difference < min_difference and difference % 3 != 0:
        min_difference = difference

print(sum - min_difference)

