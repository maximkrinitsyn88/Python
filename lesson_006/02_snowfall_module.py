# -*- coding: utf-8 -*-
from snowfall import snowflake_creation, draw_snowflakes, move_snowflakes, start_snowfall_again
import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
# создать_снежинки(N)
N = 20
snowflake_creation(N)
while True:
    draw_snowflakes(color=sd.background_color)
    move_snowflakes()
    draw_snowflakes(color='magenta')
    start_snowfall_again()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
