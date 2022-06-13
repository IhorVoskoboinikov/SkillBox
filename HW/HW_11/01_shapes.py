# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    if n == 3:
        def draw_triangle(point, angle, length):
            for _ in range(n):
                v1 = sd.get_vector(start_point=point, angle=angle, length=length)
                v1.draw()
                angle = angle + 120
                point = v1.end_point

        return draw_triangle
    elif n == 4:
        def square(point, angle, length):
            for _ in range(n):
                v1 = sd.get_vector(start_point=point, angle=angle, length=length)
                v1.draw()
                angle = angle + 90
                point = v1.end_point

        return square
    elif n == 5:
        def pentagon(point, angle, length):
            for count in range(n):
                count += 1
                v1 = sd.get_vector(start_point=point, angle=angle, length=length)
                v1.draw()
                if count == 1:
                    v2 = sd.get_vector(start_point=point, angle=angle, length=length)
                    v2.draw()
                if count == 4:
                    sd.line(start_point=v1.end_point, end_point=v2.start_point)
                angle = angle + 72
                point = v1.end_point

        return pentagon
    elif n == 6:
        def hexagon(point, angle, length):
            for count in range(n):
                count += 1
                v1 = sd.get_vector(start_point=point, angle=angle, length=length)
                v1.draw()
                if count == 1:
                    v2 = sd.get_vector(start_point=point, angle=angle, length=length)
                    v2.draw()
                if count == 5:
                    sd.line(start_point=v1.end_point, end_point=v2.start_point)
                angle = angle + 60
                point = v1.end_point

        return hexagon

    else:
        raise TypeError('Нет такой фигуры для рисования!!!')


try:
    draw_triangle = get_polygon(n=2)
    draw_triangle(point=sd.get_point(200, 200), angle=0, length=100)
except TypeError as exc:
    print(exc)

sd.pause()
