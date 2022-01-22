import random
import simple_draw as sd

sd.resolution = (1000, 1000)
N = 40
list_snowflakes = []
# Создание списка координат:
for _ in range(N):
    x = random.randint(0, 1050)
    y = random.randint(1500, 2000)
    length = random.randint(30, 50)
    list_coordinates = [x, y, length]
    list_snowflakes.append(list_coordinates)


def draw_snow():
    for i, index in enumerate(list_snowflakes):
        point_0 = sd.get_point(index[0], index[1])
        background_color = (0, 8, 98)
        sd.background_color = background_color
        sd.snowflake(center=point_0, length=index[2], color=background_color)
        index[1] -= 5
        index[0] += random.randint(-10, 10)
        point = sd.get_point(index[0], index[1])
        sd.snowflake(center=point, length=index[2])
        if index[1] < 800:
            index[1] += 1000
            index[0] += random.randint(0, 0)
            sd.snowflake(center=point, length=index[2], color=background_color)
            sd.snowflake(center=point_0, length=index[2])
