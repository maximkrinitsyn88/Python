# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1500, 1000)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

point = sd.get_point(0, 100)

COLOR_RED = 'red'
COLOR_ORANGE = 'orange'
COLOR_YELLOW = 'yellow'
COLOR_GREEN = 'green'
COLOR_CYAN = 'cyan'
COLOR_BLUE = 'blue'
COLOR_PURPLE = 'purple'

colors = {
    0: COLOR_RED,
    1: COLOR_ORANGE,
    2: COLOR_YELLOW,
    3: COLOR_GREEN,
    4: COLOR_CYAN,
    5: COLOR_BLUE,
    6: COLOR_PURPLE,
}

print('Возможные цвета:')
for keys, values in colors.items():
    print('     ', keys, ':', values)

while True:
    user_input = input('Введите, пожалуйста, цвет фигур: ')
    color = int(user_input)
    if color in colors.keys():
        color = colors[color]
        print('Вы ввели', color)
        break
    else:
        print('Выберите от 0 до 6')


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
# Отрисовка треугольника
step_triangle = 120
point_0_triangle = sd.get_point(200, 100)


def triangle(point, step, length, width, angle, color):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


triangle(point=point_0_triangle, step=step_triangle, length=length, width=width, angle=angle, color=color)

# Отрисовка квадрата
step_square = 90
point_0_square = sd.get_point(1000, 100)


def square(point, step, length, width, angle, color):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


square(point=point_0_square, step=step_square, length=length, width=width, angle=angle, color=color)

# Отрисовка пятиугольника
step_pentagon = 72
point_0_pentagon = sd.get_point(250, 600)


def pentagon(point, step, length, width, angle, color):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


pentagon(point=point_0_pentagon, step=step_pentagon, length=length, width=width, angle=angle, color=color)

# Отрисовка шестиугольника
step_hexagon = 60
point_0_hexagon = sd.get_point(1000, 570)


def hexagon(point, step, length, width, angle, color):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


hexagon(point=point_0_hexagon, step=step_hexagon, length=length, width=width, angle=angle, color=color)

# Отрисовка десятиугольника
step_decagon = 36
point_0_decagon = sd.get_point(650, 350)


def decagon(point, step, length, width, angle, color):
    figure(point=point, step=step, length=length, width=width, angle=angle, color=color)


decagon(point=point_0_decagon, step=step_decagon, length=100, width=1, angle=angle, color=color)

sd.pause()
