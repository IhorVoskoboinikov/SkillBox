def draw_smile():
    import simple_draw as sd
    color = sd.COLOR_RED
    y = 1100
    x = 700
    point = sd.get_point(y, x)
    eyes_point_1 = sd.get_point(y - 25, x + 25)
    eyes_point_2 = sd.get_point(y + 25, x + 25)
    smile_point_1 = sd.get_point(y - 50, x - 25)
    smile_point_2 = sd.get_point(y + 50, x - 25)

    sd.circle(center_position=point, radius=75, width=2, color=color)
    sd.circle(center_position=eyes_point_1, radius=10, width=1, color=color)
    sd.circle(center_position=eyes_point_2, radius=10, width=1, color=color)
    sd.line(start_point=smile_point_1, end_point=smile_point_2, color=color)
