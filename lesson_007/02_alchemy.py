# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Steam(part1=self, part2=other)
        elif isinstance(other, Land):
            return Dirt(part1=self, part2=other)
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Land):
            return Dust(part1=self, part2=other)
        elif isinstance(other, Water):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Steam):
            return Cloud(part1=self, part2=other)
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Land):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Water):
            return Steam(part1=self, part2=other)
        elif isinstance(other, Air):
            return Lightning(part1=self, part2=other)
        else:
            return None


class Land:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Water):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Air):
            return Dust(part1=self, part2=other)
        else:
            return None


class Storm:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм'


class Dirt:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь'


class Steam:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __add__(self, other):
        if isinstance(other, Air):
            return Cloud(part1=self, part2=other)

    def __str__(self):
        return 'Пар'


class Lightning:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __add__(self, other):
        if isinstance(other, Rain):
            return Thunderstorm(part1=self, part2=other)

    def __str__(self):
        return 'Молния'


class Dust:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль'


class Lava:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава'


class Cloud:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __add__(self, other):
        if isinstance(other, Water):
            return Rain(part1=self, part2=other)

    def __str__(self):
        return 'Облако'


class Rain:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Дождь'


class Thunderstorm:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Гроза'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Land(), '=', Water() + Land())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Land(), '=', Air() + Land())
print(Fire(), '+', Land(), '=', Fire() + Land())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
print('========================================================')
print(Water() + Fire(), '+', Air(), '=', Water() + Fire() + Air())
print(Water() + Fire() + Air(), '+', Water(), '=', Water() + Fire() + Air() + Water())
print(Air() + Fire(), '+', Water() + Fire() + Air() + Water(), '=',
      Air() + Fire() + (Water() + Fire() + Air() + Water()))

# зачет!
