def draw_sun(width=5):
    import simple_draw as sd
    angle = 0
    y = 150
    x = 700
    point = sd.get_point(y, x)
    for i in range(15):
        v1 = sd.get_vector(start_point=point, angle=angle, length=100, width=width)
        v1.draw()
        angle += 30
