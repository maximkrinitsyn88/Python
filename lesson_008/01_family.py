# -*- coding: utf-8 -*-
import random

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    total_money = 0
    total_food = 0

    def __init__(self):
        self.money = 100
        self.food = 100
        self.dirt = 0
        self.food_cat = 30

    def __str__(self):
        return 'В доме осталось еды - {}, еды для кота - {}, денег - {}, грязи - {}'.format(self.food, self.food_cat,
                                                                                            self.money, self.dirt)

    def act(self):
        self.dirt += 5
        cprint('Грязи стало на 5 больше', color='yellow')


class Man:

    def __init__(self, name, salary):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.cat = None
        self.salary = salary

    def __str__(self):
        return '{}, сытость - {}, счастье - {}'.format(self.name, self.fullness, self.happiness)

    def go_into_the_house(self, house):
        self.house = house
        cprint('{} заехал в дом'.format(self.name), color='grey')
        self.fullness -= 10

    def eat(self):
        if self.house.food >= 10:
            rand = random.randint(10, 30)
            cprint('{} поел'.format(self.name), color='magenta')
            self.fullness += rand
            self.happiness += rand
            self.house.food -= rand
            House.total_food += rand
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 10

    def pick_up_a_cat(self, cat):
        self.cat = cat
        self.cat.house = self.house
        cprint('{} подобрал кота {}'.format(self.name, self.cat.name), color='grey')

    def buy_food_for_the_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='blue')
            self.house.food_cat += 50
            self.house.money -= 50
        else:
            cprint('У {} не хватает денег, чтоб купить еды для котов'.format(self.name), color='red')

    def pet_the_cat(self):
        cprint('{} гладил кота весь день'.format(self.name), color='green')
        self.happiness += 5
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0 or self.happiness < 10:
            return True


class Husband(Man):

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if super().act():
            cprint('{} умер...'.format(self.name), color='red')
        else:
            dice = randint(1, 6)
            if self.fullness <= 20:
                self.eat()
            elif self.house.food_cat <= 50:
                self.buy_food_for_the_cat()
            elif self.house.money <= 150:
                self.work()
            elif self.happiness <= 20:
                self.gaming() or self.pet_the_cat()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.pet_the_cat()
            elif dice == 3:
                self.eat()
            else:
                self.gaming()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.house.money += salary
        self.fullness -= 10
        House.total_money += 150

    def gaming(self):
        cprint('{} играл в WoT целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20


class Wife(Man):
    total_coat = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        if super().act():
            cprint('{} умер...'.format(self.name), color='red')
        else:
            dice = randint(1, 6)
            if self.fullness <= 20:
                self.eat()
            elif self.house.food <= 50:
                self.shopping()
            elif self.happiness <= 20:
                self.buy_fur_coat() or self.pet_the_cat()
            elif self.house.food_cat <= 50:
                self.buy_food_for_the_cat()
            elif self.house.dirt > 100:
                self.clean_house()
            elif dice == 2:
                self.eat()
            elif dice == 3:
                self.pet_the_cat()
            elif dice == 4:
                self.buy_fur_coat()
            else:
                self.shopping()

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='blue')
            self.house.money -= 50
            self.house.food += 50
            self.fullness -= 10
        else:
            cprint('В доме кончились деньги', color='red')

    def buy_fur_coat(self):
        if self.house.money > 350:
            cprint('{} купила себе шубу'.format(self.name), color='red')
            self.happiness += 60
            self.fullness -= 10
            Wife.total_coat += 1
        else:
            cprint('{} не хватает денег на шубу :('.format(self.name), color='yellow')

    def clean_house(self):
        self.house.dirt -= random.randint(10, 100)
        self.fullness -= 10
        cprint('{} убралась в доме'.format(self.name), color='blue')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость - {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return False
        dice = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.soil()
        elif dice == 3:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food_cat >= 10:
            rand = random.randint(1, 10)
            cprint('{} поел'.format(self.name), color='magenta')
            self.fullness += rand * 2
            self.house.food_cat -= rand
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 10

    def sleep(self):
        cprint('{} спал весь день'.format(self.name), color='magenta')
        self.fullness -= 10

    def soil(self):
        cprint('{} драл обои весь день'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.dirt += 5


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.house.food >= 10:
            rand = random.randint(1, 10)
            cprint('{} поел'.format(self.name), color='magenta')
            self.fullness += rand
            self.house.food -= rand
            House.total_food += rand
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 10

    def sleep(self):
        cprint('{} спал весь день'.format(self.name), color='green')
        self.fullness -= 10

    def act(self):
        if super().act():
            cprint('{} умер...'.format(self.name), color='red')
        else:
            dice = randint(1, 6)
            if self.fullness <= 30:
                self.eat()
            elif dice == 1:
                self.eat()
            else:
                self.sleep()


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов


class Simulation:
    home = House()

    def __init__(self, money_incidents, food_incidents):
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents
        self.salary = None

    def loss_of_food(self):
        Simulation.home.food = int(Simulation.home.food / 2)
        cprint('Из холодильника пропала половина еды', color='red')

    def loss_of_money(self):
        Simulation.home.money = int(Simulation.home.money / 2)
        cprint('Из тумбочки пропала половина денег', color='red')

    def experiment(self, salary):
        self.salary = salary
        Simulation.home.money = 100
        Simulation.home.food = 100
        Simulation.home.dirt = 0
        Simulation.home.food_cat = 30
        serge = Husband(name='Сережа', salary=salary)
        katya = Wife(name='Катя', salary=self.salary)
        kolya = Child(name='Коля', salary=self.salary)
        people = [katya, serge, kolya]
        for man in people:
            man.go_into_the_house(Simulation.home)
            man.fullness = 30
            man.happiness = 100
        cats = []
        for cat in range(5):
            cat = Cat(name='Кот ' + str(cat + 1))
            serge.pick_up_a_cat(cat=cat)
            cat.fullness = 30
            cats.append(cat)
        cprint('=============================================', color='red')
        random_days_loss_money = []
        for random_day_loss_money in range(money_incidents):
            random_day_loss_money = random.randint(1, 365)
            random_days_loss_money.append(random_day_loss_money)
        random_days_loss_money.sort()
        print('Дни, в которые пропадает половина денег: ', str(random_days_loss_money)[1: -1])
        random_days_loss_food = []
        for random_day_loss_food in range(food_incidents):
            random_day_loss_food = random.randint(1, 365)
            random_days_loss_food.append(random_day_loss_food)
        random_days_loss_food.sort()
        print('Дни, в которые пропадает половина еды:', str(random_days_loss_food)[1: -1])
        for day in range(1, 366):
            cprint('================== День {} =================='.format(day), color='red')
            if day in random_days_loss_food:
                self.loss_of_food()
            if day in random_days_loss_money:
                self.loss_of_money()
            serge.act()
            katya.act()
            kolya.act()
            for cat in cats:
                cat_act = cat.act()
                if not cat_act:
                    len(cats) - 1
            Simulation.home.act()
            cprint('=============================================', color='red')
            cprint(serge, color='cyan')
            cprint(katya, color='cyan')
            cprint(kolya, color='cyan')
            for cat in cats:
                cprint(cat, color='cyan')
            cprint(Simulation.home, color='cyan')
        return len(cats)


for food_incidents in range(6):
    for money_incidents in range(6):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            max_cats = life.experiment(salary)
            cprint('=============================================', color='red')
            cprint(
                'При зарплате - {}, при {} инцидентах с пропажей половины денег из тумбочки и {} инцидентах пропажи '
                'половины еды из холодильника максимально можно прокормить - {} котов'.format(
                    salary, money_incidents, food_incidents, max_cats), color='magenta')
            cprint('=============================================', color='red')

cprint('За все время было заработано денег: {}'.format(House.total_money), color='yellow')
cprint('За все время было съедено еды людьми: {}'.format(House.total_food), color='yellow')
cprint('За все время было куплено шуб: {}'.format(Wife.total_coat), color='yellow')
