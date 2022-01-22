import random
import simple_draw as sd

sd.resolution = (1000, 1000)
list_snowflakes = []


def snowflake_creation(N):
    for _ in range(N):
        x = random.randint(100, 900)
        y = random.randint(500, 1000)
        length = random.randint(20, 40)
        list_coordinates = [x, y, length]
        list_snowflakes.append(list_coordinates)


def draw_snowflakes(color):
    sd.start_drawing()
    for i, index in enumerate(list_snowflakes):
        point_0 = sd.get_point(index[0], index[1])
        sd.snowflake(center=point_0, length=index[2], color=color)
    sd.finish_drawing()


def move_snowflakes():
    sd.start_drawing()
    for i, index in enumerate(list_snowflakes):
        index[1] -= 5
        index[0] += random.randint(-10, 10)
    sd.finish_drawing()


def start_snowfall_again():
    for i, index in enumerate(list_snowflakes):
        if index[1] < 0:
            index[0] = random.randint(100, 900)
            index[1] += 1000
            index[2] = random.randint(10, 60)
