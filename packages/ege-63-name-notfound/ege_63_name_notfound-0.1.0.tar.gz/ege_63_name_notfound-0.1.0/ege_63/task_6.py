# Решение красивым кодом блэт, без вот этого всего вашего. сурово и по нашему

from PIL import Image, ImageDraw
import math

im = Image.new('RGBA', (8000, 8000), 'white')
draw = ImageDraw.Draw(im)


def angle2line(length, ang, color='red'):
    global x, y, angle

    x_2 = x + length * 100 * math.cos(math.radians(angle))
    y_2 = y + length * 100 * math.sin(math.radians(angle))
    draw.line((x, y, x_2, y_2), fill=color, width=3)

    angle += ang
    x = x_2
    y = y_2


for i in range(0, 8000, 100):
    draw.line((i, 0, i, 8000), fill=128)
    draw.line((0, i, 8000, i), fill=128)

x = 2000
y = 2000
angle = 0


for i in range(8):
    angle += 25
    angle2line(5, 25)

# angle += 30
# for i in range(4):
#     angle2line(7, 90)
#     angle2line(8, 90)

im.show()


# Решение какой-то там черепашкой гребаной. неудобно. блэт.

# import turtle as t  # Подключим модуль черепашка
#
# k = 30
# t.left(90)
# t.speed(10000)
# for i in range(10):  # пропишем алгоритм построения фигуры по условию
#     t.forward(5 * k)
#     t.right(60)
# t.up()
# t.speed(10000)  # Увеличим скорость черепашки
# for x in range(10, -5, - 1):  # Алгоритм построения точек
#     for y in range(10, -10, - 1):
#         t.goto(x * k, y * k)
#         t.dot(3)  # точки размером 4 пикселя
# t.done()