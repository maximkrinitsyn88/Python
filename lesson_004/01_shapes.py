# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1500, 1000)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# Функция отрисовки фигуры
def figure(point, step, length, width, angle):
    point_first = point
    angle_max = 360 + angle
    for _ in range(angle, angle_max, step):
        v1 = sd.get_vector(start_point=point_first, angle=_, length=length, width=width)
        v1.draw()
        point_first = v1.end_point
        if _ == angle_max - step:
            v1 = sd.line(start_point=point, end_point=v1.end_point)


# Вводные
length = 200
width = 2
angle = 30
# Отрисовка треугольника
step_triangle = 120
point_0_triangle = sd.get_point(200, 100)


def triangle(point, step, length, width, angle):
    figure(point=point, step=step, length=length, width=width, angle=angle)


triangle(point=point_0_triangle, step=step_triangle, length=length, width=width, angle=angle)

# Отрисовка квадрата
step_square = 90
point_0_square = sd.get_point(1000, 100)


def square(point, step, length, width, angle):
    figure(point=point, step=step, length=length, width=width, angle=angle)


square(point=point_0_square, step=step_square, length=length, width=width, angle=angle)

# # Отрисовка пятиугольника
step_pentagon = 72
point_0_pentagon = sd.get_point(250, 600)


def pentagon(point, step, length, width, angle):
    figure(point=point, step=step, length=length, width=width, angle=angle)


pentagon(point=point_0_pentagon, step=step_pentagon, length=length, width=width, angle=angle)

# Отрисовка шестиугольника
step_hexagon = 60
point_0_hexagon = sd.get_point(1000, 570)


def hexagon(point, step, length, width, angle):
    figure(point=point, step=step, length=length, width=width, angle=angle)


hexagon(point=point_0_hexagon, step=step_hexagon, length=length, width=width, angle=angle)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
