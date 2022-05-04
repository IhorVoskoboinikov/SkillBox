def draw_wood(point, angle, length):
    import simple_draw as sd
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
    draw_wood(point=next_point_1, angle=angle_1, length=next_length_1)
    draw_wood(point=next_point_2, angle=angle_2, length=next_length_2)
