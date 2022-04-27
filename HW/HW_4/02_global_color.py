import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
# вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

colors = {1: sd.COLOR_RED,
          2: sd.COLOR_ORANGE,
          3: sd.COLOR_YELLOW,
          4: sd.COLOR_GREEN,
          5: sd.COLOR_CYAN,
          6: sd.COLOR_BLUE,
          7: sd.COLOR_PURPLE}
x = input(
    "1 - красный\n2 - оранжевый\n3 - жёлтый\n4 - зеленый\n5 = циан\n6 - синий\n7 - фиолетовый\n\nВведите свой номер: ")

def figure(figure_point, length_tri, angle_tri, angles):
    n = angles
    angle = (n - 2) / n * 180
    new_angle = 0 + angle_tri
    point1 = figure_point
    for _ in range(0, n - 1):
        v1 = sd.get_vector(start_point=figure_point, angle=new_angle, length=length_tri, width=2)
        v1.draw(color=colors[int(x)])
        new_angle += 180 - angle
        figure_point = v1.end_point
    sd.line(point1, figure_point, color=colors[int(x)], width=2)


def triangle():
    t_point = sd.get_point(100, 450)
    figure(t_point, 100, 25, 3)


def square():
    s_point = sd.get_point(100, 100)
    figure(figure_point=s_point, length_tri=100, angle_tri=25, angles=4)


def pentagon():
    p_point = sd.get_point(400, 110)
    figure(p_point, 65, 25, 5)


def hexagon():
    h_point = sd.get_point(400, 450)
    figure(h_point, 65, 25, 7)


# Информация о цветах хранится в словаре colors и строке в функции input
#  Будет лучше хранить в значениях словаря не цвет, а список или словарь,
#  содержащий цвет и его название. Это позволит перед запросом цвета
#  вывести в цикле ключ словаря и цвет, а после выбора пользователя
#  по ключу получить нужный цвет.

if x.isdigit():
    if 1 <= int(x) <= 7:
        point = sd.get_point(100, 350)
        triangle()
        square()
        pentagon()
        hexagon()
        sd.pause()
    else:
        print('Вы ввели неправильное значение. Повторите попытку!')
else:
    print('Вы ввели неправильное значение. Повторите попытку!')
sd.pause()
