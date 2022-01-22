# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(600, 300)
radius = 30
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color)


point = sd.get_point(600, 300)
bubble(point=point, step=15, color='red')

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=0, color='purple')

# Нарисовать три ряда по 10 пузырьков
for x in range(100, 1001, 100):
    for y in range(100, 301, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=0, color='purple')

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step, color='white')

sd.pause()

# зачет!
