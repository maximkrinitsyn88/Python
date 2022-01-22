# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random

from termcolor import cprint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):

    def __str__(self):
        return 'Я бог'


class DrunkError(Exception):

    def __str__(self):
        return 'Напился'


class CarCrashError(Exception):

    def __str__(self):
        return 'Разбился на машине'


class GluttonyError(Exception):

    def __str__(self):
        return 'Объелся'


class DepressionError(Exception):

    def __str__(self):
        return 'В депрессии'


class SuicideError(Exception):

    def __str__(self):
        return 'Самоубийство'


exception_list = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]


def one_day():
    numbers_of_exc = 0
    try:
        random_karma = random.randint(1, 7)
        cube = random.randint(1, 13)
        if cube == 13:
            exception = random.choice(exception_list)
            raise exception
    except exception as exc:
        cprint('Поймано исключение: {exc}'.format(exc=exc), color='red')
        random_karma = 0
        numbers_of_exc += 1
    return [random_karma, numbers_of_exc]


amount_of_karma = 0
days = 0
numbers_of_exc = 0

while True:
    groundhog_day = one_day()
    amount_of_karma += groundhog_day[0]
    numbers_of_exc += groundhog_day[1]
    days += 1
    cprint('День - {days}, Карма - {amount_of_karma}'.format(days=days, amount_of_karma=amount_of_karma))
    if amount_of_karma >= ENLIGHTENMENT_CARMA_LEVEL:
        break
cprint('Количество дней - {days}, потребовавшихся для поднятия кармы до - {amount_of_karma}, количество исключений - '
       '{numbers_of_exc}'.format(days=days, amount_of_karma=amount_of_karma, numbers_of_exc=numbers_of_exc),
       color='magenta')

# https://goo.gl/JnsDqu
# зачет!
