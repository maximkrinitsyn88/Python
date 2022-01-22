# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class Parser:

    def __init__(self, filename, filename_result):
        self.filename = filename
        self.filename_result = filename_result
        self.NOK = []
        self.result = {}

    def run(self):
        self.read_file()
        self.write_nok()

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

    def write_nok(self):
        group = self.group()
        with open(self.filename_result, 'w') as file_result:
            for key, value in group.items():
                nok_result = '[{txt1}] - {txt2}{txt3}'.format(txt1=key, txt2=value, txt3='\n')
                file_result.write(nok_result)


class GroupingByYears(Parser):

    def group(self):
        group = {}
        for key, value in self.result.items():
            key = key[0:4]
            if key in group:
                group[key] += value
            else:
                group[key] = value
        return group


class GroupingByDays(Parser):

    def group(self):
        group = {}
        for key, value in self.result.items():
            key = key[0:10]
            if key in group:
                group[key] += value
            else:
                group[key] = value
        return group


class GroupingByHours(Parser):

    def group(self):
        group = {}
        for key, value in self.result.items():
            key = key[0:13]
            if key in group:
                group[key] += value
            else:
                group[key] = value
        return group


# pars = GroupingByYears(filename='events.txt', filename_result='log_parser.txt')
# pars = GroupingByDays(filename='events.txt', filename_result='log_parser.txt')
pars = GroupingByHours(filename='events.txt', filename_result='log_parser.txt')
pars.run()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
