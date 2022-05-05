# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (600, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

brig_x, brig_y = 100, 50
row = 0
for y in range(0, sd.resolution[1], brig_y):
    row += 1
    for x in range(0, sd.resolution[0], brig_x):
        x0 = x if row % 2 else x + brig_x // 2
        left_bottom = sd.get_point(x0, y)
        right_top = sd.get_point(x0+brig_x, y+brig_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)


sd.pause()
