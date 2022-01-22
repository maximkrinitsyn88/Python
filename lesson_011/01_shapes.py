# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.

sd.resolution = (800, 800)


def get_polygon(n):
    def draw_figure(point, angle, length, width):
        point_first = point
        angle_max = 360 + angle
        angle_step = int(360 / n)
        for _ in range(angle, angle_max, angle_step):
            v1 = sd.get_vector(start_point=point_first, angle=_, length=length, width=width)
            v1.draw()
            point_first = v1.end_point
            if _ == angle_max - angle_step:
                v1 = sd.line(start_point=point, end_point=v1.end_point)

    return draw_figure


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(300, 300), angle=0, length=100, width=1)
draw_square = get_polygon(n=4)
draw_square(point=sd.get_point(500, 500), angle=0, length=100, width=1)

sd.pause()

# зачет!
