import simple_draw
import random


def draw_smile(x, y, color):
    # голова
    point = simple_draw.get_point(x, y)
    radius_head = 30
    simple_draw.circle(center_position=point, radius=radius_head, color=color)
    first_eye_x = x - 15
    second_eye_x = x + 15
    eye_y = y + 5
    first_eye = simple_draw.get_point(first_eye_x, eye_y)
    simple_draw.circle(center_position=first_eye, radius=5, color=color)
    second_eye = simple_draw.get_point(second_eye_x, eye_y)
    simple_draw.circle(center_position=second_eye, radius=5, color=color)
    point_list_start_x = x - 7
    point_list_start_y = y - 10
    point_list_start = simple_draw.get_point(point_list_start_x, point_list_start_y)
    point_list_middle_x = x
    point_list_middle_y = y - 12
    point_list_middle = simple_draw.get_point(point_list_middle_x, point_list_middle_y)
    point_list_end_x = x + 7
    point_list_end_y = y - 10
    point_list_end = simple_draw.get_point(point_list_end_x, point_list_end_y)
    simple_draw.lines(point_list=(point_list_start, point_list_middle, point_list_end), color=color, closed=False,
                      width=2)
    eye = random.randint(0, 1)
    background_color = (0, 8, 98)
    if eye == 0:
        simple_draw.circle(center_position=first_eye, radius=5, color=color, width=0)
        simple_draw.circle(center_position=second_eye, radius=5, color=color, width=0)
    else:
        simple_draw.circle(center_position=first_eye, radius=5, color=background_color, width=0)
        simple_draw.circle(center_position=second_eye, radius=5, color=background_color, width=0)
