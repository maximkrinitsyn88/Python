import random
import simple_draw as sd

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
