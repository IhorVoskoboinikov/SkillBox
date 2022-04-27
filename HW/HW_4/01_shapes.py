# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 900)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


point_0 = sd.get_point(750, 200)
point_1 = sd.get_point(750, 500)
point_2 = sd.get_point(200, 500)
point_3 = sd.get_point(200, 200)
#
#
# def triangle(point, angle=0, length=0, width=3):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     v1.draw(color=sd.COLOR_RED)
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=width)
#     v2.draw(color=sd.COLOR_RED)
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + 120, length=length, width=width)
#     v3.draw(color=sd.COLOR_RED)
#
#
# def square(point, angle=0, length=0, width=3):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=width)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + 90, length=length, width=width)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=v3.angle + 90, length=length, width=width)
#     v4.draw()
#
#
# def pentagon(point, angle=0, length=0, width=3):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     v1.draw(sd.COLOR_GREEN)
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=width)
#     v2.draw(sd.COLOR_GREEN)
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + 72, length=length, width=width)
#     v3.draw(sd.COLOR_GREEN)
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=v3.angle + 72, length=length, width=width)
#     v4.draw(sd.COLOR_GREEN)
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=v4.angle + 72, length=length, width=width)
#     v5.draw(sd.COLOR_GREEN)
#
#
# def hexagon(point, angle=0, length=0, width=3):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     v1.draw(sd.COLOR_DARK_ORANGE)
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=width)
#     v2.draw(sd.COLOR_DARK_ORANGE)
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + 60, length=length, width=width)
#     v3.draw(sd.COLOR_DARK_ORANGE)
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=v3.angle + 60, length=length, width=width)
#     v4.draw(sd.COLOR_DARK_ORANGE)
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=v4.angle + 60, length=length, width=width)
#     v5.draw(sd.COLOR_DARK_ORANGE)
#
#     v5 = sd.get_vector(start_point=v5.end_point, angle=v5.angle + 60, length=length, width=width)
#     v5.draw(sd.COLOR_DARK_ORANGE)
#
#
# triangle(point=point_0, angle=0, length=200)
# square(point=point_1, angle=0, length=100)
# pentagon(point=point_2, angle=0, length=200)
# hexagon(point=point_3, angle=0, length=100)

# for angl in range(0, 361, 30):
#     triangle(point=point_0, angle=angl, )


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

def triangle(point, angle, lenght):
    for _ in range(3):
        v1 = sd.get_vector(start_point=point, angle=angle, length=lenght)
        v1.draw()
        angle = angle + 120
        point = v1.end_point

def square(point, angle, lenght):
    for _ in range(4):
        v1 = sd.get_vector(start_point=point, angle=angle, length=lenght)
        v1.draw()
        angle = angle + 90
        point = v1.end_point

def pentagon(point, angle, lenght):
    for count in range(4):
        count += 1
        v1 = sd.get_vector(start_point=point, angle=angle, length=lenght)
        v1.draw()
        if count == 1:
            v2 = sd.get_vector(start_point=point, angle=angle, length=lenght)
            v2.draw()
        if count == 4:
            sd.line(start_point=v1.end_point, end_point=v2.start_point)
        angle = angle + 72
        point = v1.end_point

def hexagon(point, angle, lenght):
    for count in range(5):
        count += 1
        v1 = sd.get_vector(start_point=point, angle=angle, length=lenght)
        v1.draw()
        if count == 1:
            v2 = sd.get_vector(start_point=point, angle=angle, length=lenght)
            v2.draw()
        if count == 5:
            sd.line(start_point=v1.end_point, end_point=v2.start_point)
        angle = angle + 60
        point = v1.end_point

triangle_point = point_0
square_point = point_1
pentagon_point = point_2
hexagon_point = point_3

triangle(point=triangle_point, angle=0, lenght=200)
square(point=square_point, angle=0, lenght=150)
pentagon(point=pentagon_point, angle=0, lenght=200)
hexagon(point=hexagon_point, angle=0, lenght=150)




sd.pause()
