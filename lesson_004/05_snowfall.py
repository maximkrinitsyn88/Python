# -*- coding: utf-8 -*-
import random
import simple_draw as sd

sd.resolution = (1000, 1000)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

list_snowflakes = []
# Создание списка координат:
for _ in range(N):
    x = random.randint(100, 900)
    y = random.randint(300, 1000)
    length = random.randint(30, 50)
    list_coordinates = [x, y, length]
    list_snowflakes.append(list_coordinates)
    print(list_snowflakes)

while True:
    sd.start_drawing()
    for i, index in enumerate(list_snowflakes):
        point_0 = sd.get_point(index[0], index[1])
        background_color = (0, 8, 98)
        sd.background_color = background_color
        sd.snowflake(center=point_0, length=index[2], color=background_color)
        index[1] -= 5
        index[0] += random.randint(-10, 10)
        point = sd.get_point(index[0], index[1])
        sd.snowflake(center=point, length=index[2])
        if index[1] < 0:
            index[1] += 1000
            index[0] += random.randint(0, 0)
            sd.snowflake(center=point, length=index[2], color=background_color)
            sd.snowflake(center=point_0, length=index[2])
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


#эталонный пример реализации
# -*- coding: utf-8 -*-
#
# import simple_draw as sd
#
# sd.resolution = (1080, 720)
#
# # число снежинок
# N = 20
#
# # создаём список данных для отрисовки N снежинок
# snowflakes = []
#
# # Фунцкия создания новой рандомной снежинки
#
#
# def new_snowflake(n):
#
#     # выбираем рандомную стартовую точку для создания снежинки
#     random_point = sd.random_point()
#
#     # выбираем рандомно скорость и направление ветра для снежинки
#     wind = sd.random_number(-20, 20)
#
#     # добавляем в список снежинок рандомные длины лучей снежинок (от 10 до 100) и все снежинки будут разные
#     length = sd.random_number(10, 100)
#
#     snowflake = {
#         'x': random_point.x,
#         'y': random_point.y,
#         'length': length,
#         'wind': wind,
#         'draw': True
#     }
#
#     if n == -1:  # в случае если мыв создаём список снежинок
#         snowflakes.append(snowflake)  # добавляем в список новую
#     else:  # в случае уже созданной снежинки
#         snowflakes[n] = snowflake  # заменяем значения на новые
#
#
# # Функция рисования снежинки
#
#
# def draw_snowflake(n):
#
#     if snowflakes[n]['draw']:
#         point = sd.get_point(snowflakes[n]['x'], snowflakes[n]['y'])
#
#         #  ускоряем отрисовку снежинок через её же на старом месте снежинки отрисовку, но цветом sd.background_color
#         sd.snowflake(center=point, length=snowflakes[n]['length'], color=sd.background_color)
#
#         #  двигаем снежинку вправо и влево
#         snowflakes[n]['x'] += snowflakes[n]['wind']
#
#         # двигаем снежинку вниз
#         snowflakes[n]['y'] -= 1
#
#         # - сделать рандомные отклонения вправо/влево при каждом шаге
#         snowflakes[n]['wind'] = sd.random_number(-20, 20)
#
#         point = sd.get_point(snowflakes[n]['x'], snowflakes[n]['y'])
#
#         #  отрисовываем снежинку цветом sd.COLOR_WHITE на новом месте
#         sd.snowflake(center=point, length=snowflakes[n]['length'], color=sd.COLOR_WHITE)
#
#         # делаем сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#         #  и добавляем новую снежинку
#         if snowflakes[n]['y'] <= snowflakes[n]['length']:
#             new_snowflake(n)
#
# # создаём список N новых снежинок
#
#
# for _ in range(N):
#
#     new_snowflake(-1)
#
# # рисуем падение этих N снежинок
#
#
# while True:
#
#     #  ускоряем отрисовку рисования всех снежинок через вызов sd.start_drawing()
#     sd.start_drawing()
#
#     for n in range(N):
#         draw_snowflake(n)
#
#     # 4) Усложненное задание (сделал по желанию)
#     # после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()
#     sd.finish_drawing()
#
#     # задержка на 0.1 секунды
#     sd.sleep(0.1)
#
#     # по жеданию - выход из программы
#     if sd.user_want_exit():
#         break

# конец отрисовки
sd.pause()

