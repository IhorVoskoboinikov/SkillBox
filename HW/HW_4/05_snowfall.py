import simple_draw as sd

sd.resolution = (1200, 800)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
snowflakes = [
    [700, 100, 10],
    [750, 150, 20],
    [800, 200, 30],
    [650, 50, 40],
    [700, 300, 50]
]


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
# y = snowflakes[0][0]
# x = snowflakes[0][1]
#
# y1 = snowflakes[1][0]
# x1 = snowflakes[1][1]
#
# y2 = snowflakes[2][0]
# x2 = snowflakes[2][1]

while True:
    sd.clear_screen()

    for point in snowflakes:
            next_point = sd.get_point(point[1], point[0])
            sd.snowflake(center=next_point, length=point[2])
            point[0] -= 10
            point[1] += 10

    if point[0] < 50:
        break

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
