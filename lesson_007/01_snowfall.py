# -*- coding: utf-8 -*-
import random
import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

sd.resolution = (1000, 1000)


class Snowflake:

    def __init__(self):
        self.x = random.randint(sd.resolution[0] * 0.1, sd.resolution[0] * 0.9)
        self.y = random.randint(sd.resolution[1] / 2, sd.resolution[1])
        self.length = random.randint(20, 40)

    def clear_previous_picture(self):
        point_0 = sd.get_point(self.x, self.y)
        sd.snowflake(center=point_0, length=self.length, color=sd.background_color)

    def move(self):
        self.x += random.randint(-10, 10)
        self.y -= random.randint(2, 10)

    def draw(self, color):
        point_0 = sd.get_point(self.x, self.y)
        sd.snowflake(center=point_0, length=self.length, color=color)

    def can_fall(self):
        return self.y > 0


# flake = Snowflake()

# while True:
#     sd.start_drawing()
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


def creating_snowflakes(number_of_snowflakes):
    flakes = []
    for _ in range(number_of_snowflakes):
        snowflake = Snowflake()
        flakes.append(snowflake)
    return flakes


def get_fallen_flakes(flakes):
    snowflake_counter = 0
    for snowflake in flakes:
        if not snowflake.can_fall():
            flakes.remove(snowflake)
            snowflake_counter += 1
    return [snowflake_counter, flakes]


def append_flakes(count, flakes):
    for _ in range(count):
        snowflake = Snowflake()
        flakes.append(snowflake)


flakes = creating_snowflakes(number_of_snowflakes=10)
while True:
    for flake in flakes:
        sd.start_drawing()
        flake.clear_previous_picture()
        flake.move()
        flake.draw(color='magenta')
        fallen_flake_count, flakes = get_fallen_flakes(flakes=flakes)  # с распаковкой словаря так проще
        if fallen_flake_count:
            append_flakes(count=fallen_flake_count, flakes=flakes)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
#
sd.pause()

# зачет!
