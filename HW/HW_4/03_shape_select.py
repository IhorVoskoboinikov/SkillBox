# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код


x = input(
    "1 - труегольник\n2 - квадрат\n3 - пятиугольник\n4 - шестиугольник\n\nВведите свой номер: ")


def figure(length_tri, angle_tri, angles):
    n = angles
    angle = (n - 2) / n * 180
    new_angle = 0 + angle_tri
    start_point = sd.get_point(300, 300)
    next_point = start_point
    for _ in range(0, n - 1):
        v1 = sd.get_vector(start_point=start_point, angle=new_angle, length=length_tri, width=2)
        v1.draw()
        new_angle += 180 - angle
        start_point = v1.end_point
    sd.line(next_point, start_point, width=2)


def triangle():
    figure(100, 25, 3)


def square():
    figure(length_tri=100, angle_tri=25, angles=4)


def pentagon():
    figure(65, 25, 5)


def hexagon():
    figure(65, 25, 7)


if int(x) == 1:
    triangle()
elif int(x) == 2:
    square()
elif int(x) == 3:
    pentagon()
elif int(x) == 4:
    hexagon()
else:
    print("Не правильный ввод, введите цифры от 1 до 4")

# if x.isdigit():
#     if 1 <= int(x) <= 4:
#         triangle()
#         # square()
#         # pentagon()
#         # hexagon()
#         sd.pause()
#     else:
#         print('Вы ввели неправильное значение. Повторите попытку!')
# else:
#     print('Вы ввели неправильное значение. Повторите попытку!')

sd.pause()
