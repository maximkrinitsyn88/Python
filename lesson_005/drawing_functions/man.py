import simple_draw
import random


def draw_man(x, y, color):
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
    # тело
    y_body = y - radius_head
    y_body2 = y - radius_head - 100
    start_point_body = simple_draw.get_point(x, y_body)
    end_point_body = simple_draw.get_point(x, y_body2)
    simple_draw.line(start_point=start_point_body, end_point=end_point_body, color="purple")
    # левая нога
    x_leg_left = x - 30
    y_leg = y_body2 - 50
    end_point_leg_left = simple_draw.get_point(x=x_leg_left, y=y_leg)
    simple_draw.line(start_point=end_point_body, end_point=end_point_leg_left, color='purple')
    # правая нога
    x_leg_right = x + 30
    end_point_leg_right = simple_draw.get_point(x=x_leg_right, y=y_leg)
    simple_draw.line(start_point=end_point_body, end_point=end_point_leg_right, color='purple')
    # левая рука
    x_hand_left = x - 40
    y_hand_start_point = (y_body + y_body2) / 2
    y_hand_end_point = y_hand_start_point + 15
    start_point_hand = simple_draw.get_point(x, y=y_hand_start_point)
    end_point_hand_left = simple_draw.get_point(x=x_hand_left, y=y_hand_end_point)
    simple_draw.line(start_point=start_point_hand, end_point=end_point_hand_left, color='purple')
    # правая рука
    x_hand_right = x + 40
    start_point_hand = simple_draw.get_point(x, y=y_hand_start_point)
    end_point_hand_right = simple_draw.get_point(x=x_hand_right, y=y_hand_end_point)
    simple_draw.line(start_point=start_point_hand, end_point=end_point_hand_right, color='purple')
