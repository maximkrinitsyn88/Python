#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Мама', 'Папа', 'Брат', 'Бабушка', 'Дедушка']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 175],
    [my_family[1], 185],
    [my_family[2], 190],
    [my_family[3], 165],
    [my_family[4], 170]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print('Рост отца -', my_family_height[0][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print('Общий рост моей семьи -', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1], 'см')


# зачет!
