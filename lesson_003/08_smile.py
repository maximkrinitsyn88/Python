# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw

simple_draw.resolution = (1200, 600)


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def paint_smile(x, y, color):
    point = simple_draw.get_point(x, y)
    simple_draw.circle(center_position=point, radius=30, color=color)
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


for _ in range(10):
    coord_x = random.randint(100, 1150)
    coord_y = random.randint(100, 550)
    paint_smile(coord_x, coord_y, 'purple')

simple_draw.pause()

# зачет!
