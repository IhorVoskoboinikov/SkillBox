# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def draw_bunches(point, angle, length):
    v_0 = sd.get_vector(start_point=point, angle=angle, length=length)
    v_0.draw()
    if length < 5:
        return
    angle_1 = angle - 30
    angle_2 = angle + 30
    v1 = sd.get_vector(start_point=v_0.end_point, angle=angle_1, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v_0.end_point, angle=angle_2, length=length)
    v2.draw()
    next_point_1 = v1.end_point
    next_point_2 = v2.end_point
    next_length_1 = length * 0.75
    next_length_2 = length * 0.75
    draw_bunches(point=next_point_1, angle=angle_1, length=next_length_1)
    draw_bunches(point=next_point_2, angle=angle_2, length=next_length_2)



point_0 = sd.get_point(600, 50)

draw_bunches(point=point_0, angle=90, length=100)

sd.pause()

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


