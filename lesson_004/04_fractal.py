# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (800, 600)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

point_0 = sd.get_point(600, 5)

# Рандомный угол отклонения ветки
c = 30
b = c + (c * 0.4)
a = c + (c * (-0.4))


def random_number_angle(a, b):
    return random.randint(a, b)


# Рандомная длина ветки
k = 0.75
to_k = int((k + (k * 0.2)) * 100)
from_k = int((k + (k * (-0.2))) * 100)


def random_number_length(from_k, to_k):
    return random.randint(from_k, to_k)


# Отрисовка дерева
def draw_branches(point, angle, length):
    if length < 4:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color='green')
    random_angle = random_number_angle(a=a, b=b)
    random_length = (random_number_length(from_k=from_k, to_k=to_k) / 100)
    print(random_angle, random_length)
    next_point = v1.end_point
    next_angle_1 = angle - random_angle
    next_angle_2 = angle + random_angle
    next_length = length * random_length
    draw_branches(point=next_point, angle=next_angle_1, length=next_length)
    draw_branches(point=next_point, angle=next_angle_2, length=next_length)


root_point = sd.get_point(400, 30)
draw_branches(point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции


sd.pause()

# зачет!
