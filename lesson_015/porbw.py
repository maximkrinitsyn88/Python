import re
mob_pattern = r'Location_([a-wA-W]\d+|\d+)\_tm((\d+\.\d+)|(\d+))'
# mob_pattern = r'Location_(\d+)\_tm((\d+\.\d+)|(\d+))'
x = "Location_B2_tm2000"
# x = 'Location_9_tm26000'
matched = re.search(mob_pattern, x)
print(f'Найдена подстрока >{matched[0]}< с позиции {matched.start(0)} до {matched.end(0)}')
#               Найдена подстрока >   Опять45   < с позиции 3 до 16
print(f'Группа букв >{matched[1]}< с позиции {matched.start(1)} до {matched.end(1)}')
#               Группа букв >Опять< с позиции 6 до 11
print(f'Группа цифр >{matched[2]}< с позиции {matched.start(2)} до {matched.end(2)}')