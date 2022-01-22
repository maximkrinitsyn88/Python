# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_point_x = 50
start_point_y = 50
end_point_x = 350
end_point_y = 450
width = 4
step = 5

for _ in rainbow_colors:
    start_point_x = start_point_x + step
    end_point_x = end_point_x + step
    sd.line(start_point=sd.get_point(start_point_x, start_point_y), end_point=sd.get_point(end_point_x, end_point_y),
            color=_, width=width)

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
start_point_x = -100
start_point_y = -100
step = 10

for color in rainbow_colors:
    start_point_x = start_point_x + step
    start_point_y = start_point_y + step
    sd.circle(center_position=sd.get_point(start_point_x, start_point_y), radius=750, color=color, width=15)
sd.pause()

# зачет!
