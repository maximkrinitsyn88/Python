# -*- coding: utf-8 -*-
import random

from termcolor import cprint, colored
from random import randint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='cyan')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.house.money += 150
        self.fullness -= 10

    def watch_TV(self):
        cprint('{} смотрел TV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='blue')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('У {}а деньги кончились'.format(self.name), color='red')

    def go_into_the_house(self, house):
        self.house = house
        cprint('{} заехал в дом'.format(self.name), color='grey')
        self.fullness -= 10

    def pick_up_a_cat(self, cat):
        self.cat = cat
        self.cat.house = self.house
        cprint('{} подобрал кота {}'.format(self.name, self.cat.name), color='grey')

    def buy_food_for_the_cat(self):
        if self.house.money >= 150:
            cprint('{} сходил в магазин за едой для котов'.format(self.name, self.cat.name), color='blue')
            self.house.food_cat += 150
            self.house.money -= 150
        else:
            cprint('У {}а не хватает денег, чтоб купить еды для котов'.format(self.name), color='red')

    def clean_the_house(self):
        cprint('{} убрался в доме'.format(self.name), color='green')
        self.house.dirt -= 100
        self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            return cprint('{} умер...'.format(self.name), color='red')
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money <= 150:
            self.work()
        elif self.house.food_cat <= 50:
            self.buy_food_for_the_cat()
        elif self.house.dirt >= 100:
            self.clean_the_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_TV()


class House:

    def __init__(self):
        self.food = 10
        self.money = 100
        self.food_cat = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме осталось еды - {}, денег - {}, еды для котов - {}, грязи - {}'.format(self.food, self.money,
                                                                                             self.food_cat, self.dirt)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = random.randint(40, 70)
        self.house = None

    def __str__(self):
        return 'Я - кот {}, сытость - {}'.format(self.name, self.fullness)

    def sleep(self):
        cprint('{} спал весь день'.format(self.name), color='magenta')
        self.fullness -= 10

    def eat(self):
        if self.house.food_cat >= 10:
            cprint('{} поел'.format(self.name), color='cyan')
            self.fullness += 20
            self.house.food_cat -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def tears_wallpaper(self):
        cprint('{} драл обои весь день'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            return cprint('{} умер...'.format(self.name), color='red')
        dice = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.tears_wallpaper()
        else:
            self.sleep()


my_sweet_home = House()
man = Man(name='Олег')
man.go_into_the_house(house=my_sweet_home)

cats = [
    Cat(name='Мурзик'),
    Cat(name='Цветик'),
    Cat(name='Кексик')
]

for cat in cats:
    man.pick_up_a_cat(cat=cat)

for day in range(1, 366):
    cprint('======================= день {} =========================='.format(day), color='yellow')
    man.act()
    for cat in cats:
        cat.act()
    cprint('===================== в конце дня ========================', color='yellow')
    print(man)
    for cat in cats:
        print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

# зачет!
