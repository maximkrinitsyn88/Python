# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно изменить правила подсчета очков в игре.
# "Выходим на внешний рынок, а там правила игры другие!" - сказал он.
#
# Правила подсчета очков изменяются так:
#
# Если во фрейме страйк, сумма очков за этот фрейм будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за два следующих броска шара (в одном или двух фреймах,
# в зависимости от того, был ли страйк в следующем броске).
# Например: первый бросок шара после страйка - тоже страйк, то +10 (сбил 10 кеглей)
# и второй бросок шара - сбил 2 кегли (не страйк, не важно как закончится этот фрейм - считаем кегли) - то еще +2.
#
# Если во фрейме сбит спэр, то сумма очков будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за первый бросок шара в следующем фрейме.
#
# Если фрейм остался открытым, то сумма очков будет равна количеству сбитых кеглей в этом фрейме.
#
# Страйк и спэр в последнем фрейме - по 10 очков.
#
# То есть для игры «Х4/34» сумма очков равна 10+10 + 10+3 + 3+4 = 40,
# а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92

# Необходимые изменения сделать во всех модулях. Тесты - дополнить.

# "И да, старые правила должны остаться! для внутреннего рынка..." - уточнил менеджер напоследок.
#
#
# # # а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92
# # # X-X-X-34X-65236X-36
# game_score = '223/14535222-2122121'
# game = get_score(game_score)
# print(game)

from termcolor import cprint
from bowling import GetScore

game_result = 'X138-7/X11-89/X1/'

try:
    cprint('*' * 100, color='red')
    get_score = GetScore(game_result=game_result, new_rules=False)
    get_score = get_score.run()
    cprint(f'Количество очков для результата (старые правила): `{game_result}` - {get_score}', color='magenta')
    cprint('*' * 100, color='red')
    get_score_new_rules = GetScore(game_result=game_result, new_rules=True)
    get_score_new_rules = get_score_new_rules.run()
    cprint(f'Количество очков для результата (новые правила): `{game_result}` - {get_score_new_rules}', color='magenta')
    cprint('*' * 100, color='red')
except Exception as exc:
    cprint('Невалидный счёт:', exc)
