# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as central_street_house1_room1
from district.central_street.house1.room2 import folks as central_street_house1_room2
from district.central_street.house2.room1 import folks as central_street_house2_room1
from district.central_street.house2.room2 import folks as central_street_house2_room2
from district.soviet_street.house1.room1 import folks as soviet_street_house1_room1
from district.soviet_street.house1.room2 import folks as soviet_street_house1_room2
from district.soviet_street.house2.room1 import folks as soviet_street_house2_room1
from district.soviet_street.house2.room2 import folks as soviet_street_house2_room2

central_street = central_street_house1_room1 + central_street_house1_room2 + central_street_house2_room1 \
                 + central_street_house2_room2
soviet_street = soviet_street_house1_room1 + soviet_street_house1_room2 + soviet_street_house2_room1 \
                + soviet_street_house2_room2
district = central_street + soviet_street
print('Центральная улица:', ', '.join(central_street))
print('Советская улица:', ', '.join(soviet_street))
print('На районе живут:', ', '.join(district))
print('На районе живут:', str(district)[1:-1])
