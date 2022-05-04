def draw_rainbow():
    import simple_draw as sd
    point = sd.get_point(1100, -200)
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    radius = 600
    for color in rainbow_colors:
        radius += 20
        sd.circle(center_position=point, radius=radius, width=19, color=color)
