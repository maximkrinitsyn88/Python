import simple_draw as sd


def draw_sun(x, y, color):
    for ray, angle in enumerate(range(0, 360, 30)):
        point = sd.get_point(x, y)
        sd.vector(start=point, angle=angle, length=135, color=sd.background_color, width=8)
        random_length = sd.random_number(115, 135)
        sd.vector(start=point, angle=angle, length=random_length, color=color, width=6)
    sd.circle(center_position=point, color=color, width=0)
