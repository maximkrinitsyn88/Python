# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from drawing_functions.rainbow import draw_rainbow
from drawing_functions.tree import draw_branches
from drawing_functions.man import draw_man
from drawing_functions.sun import draw_sun
from drawing_functions.brick_house import draw_brick_house
from drawing_functions.smile import draw_smile
from drawing_functions.snow import draw_snow
from drawing_functions.ground import draw_ground

sd.resolution = (2000, 2000)

draw_branches(point=sd.get_point(1500, 800), angle=90, length=100)
while True:
    sd.start_drawing()
    draw_rainbow()
    draw_brick_house(800, 800)
    draw_man(600, 985, 'purple')
    draw_ground(0, 0)
    draw_sun(1000, 1400, 'yellow')
    draw_smile(1012, 925, 'yellow')
    draw_snow()
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
