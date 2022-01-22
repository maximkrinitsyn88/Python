# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

start_x = 0
start_y = 0
brick_width = 100
brick_height = 50

for y in range(20):
    if y % 2 == 0:
        shift = 50
    else:
        shift = 0
    for x in range(10):
        left_bottom_x = start_x + shift + brick_width * x
        left_bottom_y = start_y + brick_height * y
        left_bottom_point = simple_draw.get_point(left_bottom_x, left_bottom_y)
        right_top_x = left_bottom_x + brick_width
        right_top_y = left_bottom_y + brick_height
        right_top_point = simple_draw.get_point(right_top_x, right_top_y)
        simple_draw.rectangle(left_bottom=left_bottom_point, right_top=right_top_point, color='orange', width=1)

simple_draw.pause()

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

# зачет!
