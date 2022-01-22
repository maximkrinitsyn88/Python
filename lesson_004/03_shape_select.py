# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 500)

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

COLOR_RED = 'red'
COLOR_ORANGE = 'orange'
COLOR_YELLOW = 'yellow'
COLOR_GREEN = 'green'
COLOR_CYAN = 'cyan'
COLOR_BLUE = 'blue'
COLOR_PURPLE = 'purple'

figures = {
    0: 'треугольник',
    1: 'квадрат',
    2: 'пятиугольник',
    3: 'шестиугольник',
}

print('Возможные фигуры:')
for keys, values in figures.items():
    print('     ', keys, ':', values)


# Функция отрисовки фигуры
def figure(point, step, length, width, angle, color):
    point_first = point
    angle_max = 360 + angle
    for _ in range(angle, angle_max, step):
        v1 = sd.get_vector(start_point=point_first, angle=_, length=length, width=width)
        v1.draw(color=color)
        point_first = v1.end_point
        if _ == angle_max - step:
            v1 = sd.line(start_point=point, end_point=v1.end_point, color=color)


length = 200
width = 2
angle = 30
point = sd.get_point(500, 50)
# Отрисовка треугольника
step_triangle = 120


def triangle(point, step, length, width, angle, color):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


# Отрисовка квадрата
step_square = 90


def square(point, step, length, width, angle, color):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


# Отрисовка пятиугольника
step_pentagon = 72


def pentagon(point, step, length, width, angle, color):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


# Отрисовка шестиугольника
step_hexagon = 60


def hexagon(point, step, length, width, angle, color=COLOR_GREEN):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


while True:
    user_input = input('Введите, пожалуйста, фигуру: ')
    input_figure = int(user_input)
    if input_figure in figures.keys():
        input_figure = figures[input_figure]
        print('Вы ввели', input_figure)
        if input_figure == 'треугольник':
            triangle(point=point, step=step_triangle, length=length, width=width, angle=angle,
                     color=COLOR_YELLOW)
            break
        elif input_figure == 'квадрат':
            square(point=point, step=step_square, length=length, width=width, angle=angle, color=COLOR_GREEN)
            break
        elif input_figure == 'пятиугольник':
            pentagon(point=point, step=step_pentagon, length=length, width=width, angle=angle,
                     color=COLOR_BLUE)
            break
        elif input_figure == 'шестиугольник':
            hexagon(point=point, step=step_hexagon, length=length, width=width, angle=angle,
                    color=COLOR_ORANGE)
            break
    else:
        print('Вы ввели некорректный номер')

sd.pause()
