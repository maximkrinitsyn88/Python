# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.NOK = []
        self.result = {}

    def group(self):
        self.read_file()
        group = {}
        for key, value in self.result.items():
            key = key[0:16]
            if key in group:
                group[key] += value
            else:
                group[key] = value
            yield key, value
            # if value == 2:
            #     return

    def read_file(self):
        with open(self.filename, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    self.NOK.append(line[1:17])
            for char in self.NOK:
                if char in self.result:
                    self.result[char] += 1
                else:
                    self.result[char] = 1


pars = Parser(filename='events.txt')
grouped_events = pars.group()
print(grouped_events)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
# зачет!
