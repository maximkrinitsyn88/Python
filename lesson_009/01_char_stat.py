# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
import operator
import zipfile


class Statistic:
    sum_char = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def run(self):
        self.collect()
        self.print()

    def unzip(self):
        zip_file = zipfile.ZipFile(self.file_name, 'r')
        for filename in zip_file.namelist():
            zip_file.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_line(line)

    def collect_line(self, line):
        for char in line:
            if char.isalpha():
                self.sum_char += 1
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def print(self):
        print('+{txt:-^22}+'.format(txt='+'))
        print('|{txt1:^9} | {txt2:^10}|'.format(txt1='Буква', txt2='Частота'))
        print('+{txt:-^22}+'.format(txt='+'))
        self.sort()
        print('+{txt:-^22}+'.format(txt='+'))
        print('|{txt1:^9} | {txt2:^10}|'.format(txt1='Итого', txt2=self.sum_char))
        print('+{txt:-^22}+'.format(txt='+'))

    def sort(self):
        for key, value in sorted(self.stat.items()):
            print('|{txt1:^9} | {txt2:^10}|'.format(txt1=key, txt2=value))


class ReverseAlphabetSort(Statistic):

    def sort(self):
        for key, value in reversed(sorted(self.stat.items())):
            print('|{txt1:^9} | {txt2:^10}|'.format(txt1=key, txt2=value))


class ByFrequencyAscending(Statistic):

    def sort(self):
        sorted_dict = self.sorted_dict()
        for key, value in sorted_dict.items():
            print('|{txt1:^9} | {txt2:^10}|'.format(txt1=key, txt2=value))

    def sorted_dict(self):
        sorted_dict = {}
        for key in sorted(self.stat, key=self.stat.get):
            sorted_dict[key] = self.stat[key]
        return sorted_dict


class ByFrequencyDescending(ByFrequencyAscending):

    def sort(self):
        sorted_dict = self.sorted_dict()
        for key, value in reversed(sorted_dict.items()):
            print('|{txt1:^9} | {txt2:^10}|'.format(txt1=key, txt2=value))


filename = './python_snippets/voyna-i-mir.txt.zip'
statistic_sort = input('Какая сортировка вам нужна? (По умолчанию: По алфавиту по возрастанию) \n'
                       '1. По алфавиту по убыванию \n'
                       '2. По частоте по возрастанию \n'
                       '3. По частоте по убыванию \n')

if statistic_sort == '1':
    statistic = ReverseAlphabetSort(file_name=filename)
elif statistic_sort == '2':
    statistic = ByFrequencyAscending(file_name=filename)
elif statistic_sort == '3':
    statistic = ByFrequencyDescending(file_name=filename)
else:
    statistic = Statistic(file_name=filename)
statistic.run()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
