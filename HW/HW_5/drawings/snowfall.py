import simple_draw as sd
from random import seed, randint

seed(0)

sd.resolution = (1200, 800)

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
    coordinates, length, speed = create_snowflake()
    snowflakes_coordinates.append(coordinates)
    snowflakes_sizes.append(length)
    snowflakes_speed.append(speed)

while True:
    sd.clear_screen()

    for i in range(N):
        point = snowflakes_coordinates[i]
        length = snowflakes_sizes[i]
        speed = snowflakes_speed[i]

        next_point = sd.get_point(point[1], point[0])
        sd.snowflake(center=next_point, length=length)
        point[0] -= speed
        point[1] += speed

        if point[0] < 50:
            new_point, new_length, new_speed = create_snowflake()
            snowflakes_coordinates[i] = new_point
            snowflakes_sizes[i] = length
            snowflakes_speed[i] = speed

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
