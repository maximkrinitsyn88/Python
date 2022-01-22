import simple_draw
from .wall import draw_wall

simple_draw.resolution = (1000, 1000)


def draw_brick_house(x, y):
    # углы
    first_point_angle_x = x
    first_point_angle_y = y
    first_point_angle = simple_draw.get_point(first_point_angle_x, first_point_angle_y)
    for _ in range(0, 360, 90):
        if (_ == 0) or (_ == 180):
            v1 = simple_draw.get_vector(first_point_angle, angle=_, length=425, width=2)
            v1.draw(color='orange')
            first_point_angle = v1.end_point
        else:
            v1 = simple_draw.get_vector(first_point_angle, angle=_, length=200, width=2)
            v1.draw(color='orange')
            first_point_angle = v1.end_point
    # крыша
    first_point_x = x - 50
    first_point_y = y + 200
    first_point = simple_draw.get_point(first_point_x, first_point_y)
    second_point_x = x + 475
    second_point = simple_draw.get_point(second_point_x, first_point_y)
    third_point_x = (first_point_x + second_point_x) / 2
    third_point_y = first_point_y + 100
    third_point = simple_draw.get_point(third_point_x, third_point_y)
    point_list = (first_point, second_point, third_point, first_point)
    simple_draw.polygon(point_list=point_list, color='orange', width=0)
    # стена
    draw_wall(x, y)
    # окно
    first_point_window_x = x + 100
    first_point_window_y = y + 76
    first_point_window = simple_draw.get_point(first_point_window_x, first_point_window_y)
    second_point_window_x = x + 325
    second_point_window_y = y + 174
    second_point_window = simple_draw.get_point(second_point_window_x, second_point_window_y)
    background_color = (0, 8, 98)
    simple_draw.rectangle(left_bottom=first_point_window, right_top=second_point_window, color=background_color,
                          width=0)
