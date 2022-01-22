import simple_draw as sd


def draw_ground(x, y):
    first_point_ground_x = x
    first_point_ground_y = y
    first_point_ground = sd.get_point(first_point_ground_x, first_point_ground_y)
    second_point_ground_x = x + 2000
    second_point_ground_y = y + 799
    second_point_ground = sd.get_point(second_point_ground_x, second_point_ground_y)
    color_ground = (127, 127, 0)
    sd.rectangle(left_bottom=first_point_ground, right_top=second_point_ground, color=color_ground, width=0)
