import simple_draw as sd
from random import seed, randint

seed(0)

sd.resolution = (1200, 800)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


snowflakes_coordinates = []
snowflakes_sizes = []
snowflakes_speed = []
N = 20
max_y = 800
min_y = 700
min_x = 50
max_x = 300
min_size = 10
max_size = 50
min_speed = 5
max_speed = 15


def create_snowflake():
    y = randint(min_y, max_y)
    x = randint(min_x, max_x)
    s = randint(min_size, max_size)
    sp = randint(min_speed, max_speed)

    return [y, x], s, sp


for i in range(N):
    param = create_snowflake()
    snowflakes_coordinates.append(param[0])
    snowflakes_sizes.append(param[1])
    snowflakes_speed.append(param[2])

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


while True:
    sd.clear_screen()
    for point, length, speed in zip(snowflakes_coordinates, snowflakes_sizes, snowflakes_speed):
        next_point = sd.get_point(point[1], point[0])
        sd.snowflake(center=next_point, length=length)
        point[0] -= 10
        point[1] += speed

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
