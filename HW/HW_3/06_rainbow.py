# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.background_color = (0, 127, 127)
sd.resolution = (1200, 600)
sd.caption = 'My APP'

point_x = sd.get_point(100, 100)
point_y = sd.get_point(1000, 500)


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
step_x = 0
step_y = 0
for color in rainbow_colors:
    step_x += 25
    step_y += 25
    point_x = sd.get_point(100+step_x, 100)
    point_y = sd.get_point(1000+step_y, 500)

    sd.line(start_point=point_x, end_point=point_y, width=10, color=color)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

# point = sd.get_point(600, -300)
# rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
#                   sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
# radius = 600
# for color in rainbow_colors:
#     radius += 15
#     sd.circle(center_position=point, radius=radius, width=14, color=color)

sd.pause()
