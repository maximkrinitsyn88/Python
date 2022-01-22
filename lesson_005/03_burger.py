# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
from burger import add_bun, add_mayonnaise, add_cheese, add_cutlet, add_cucumber, add_tomato, add_onion, add_ketchup


def double_cheeseburger():
    print('Рецепт двойного чизбургера:')
    add_bun()
    add_cutlet()
    add_cheese()
    add_cutlet()
    add_cheese()
    add_cucumber()
    add_onion()
    add_tomato()
    add_ketchup()
    add_mayonnaise()
    add_bun()
    print('Двойной чизбургер готов')


double_cheeseburger()
