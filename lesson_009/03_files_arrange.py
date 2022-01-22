# -*- coding: utf-8 -*-

import os
import time
import shutil
import zipfile

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:

# os.walk - показывает вложенность директории
#   dir = 'icons'
#   for i in os.walk(dir):
#     print(i)

# os.path.dirname - показывает в какой директории находится файл
#   dirname = os.path.dirname(dir)
#   print(dirname)

# os.path.join - соединяет пути
#   path = 'C://'
#   print(os.path.join(path, '/icons/actions'))

# os.path.normpath - нормализует путь
#   dir = '/icons/actions/./appointment-new.png'
#   print(os.path.normpath(dir))

# os.path.getmtime - возвращает время последней модификации файла
#   dir = './icons/actions/appointment-new.png'
#   mtime = os.path.getmtime(dir)
#   print(mtime)

# time.gmtime - преобразует время, выраженное в секундах с момента последней модификации файла
#   dir = './icons/actions/appointment-new.png'
#   mtime = os.path.getmtime(dir)
#   time = time.gmtime(mtime)
#   print(time)

# os.makedirs - создание новой директории (new_dir) в python_snippets
#   dir = 0o777 (0о777 - создание новой директории)
#   parent_dir = './python_snippets/new_dir'
#   os.makedirs(parent_dir, dir)

# shutil.copy2 - делает копию файла в dir2
#   dir1 = 'icons/actions/appointment-new.png'
#   dir2 = './python_snippets/'
#   shutil.copy2(dir1, dir2)
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
from pprint import pprint


class ArrangePhotos:

    def __init__(self, directory):
        self.directory = directory
        self.content_dir = []
        self.files = []

    def run(self):
        self.walk_dir()
        self.collect_files()
        self.copy_files()

    def walk_dir(self):
        for _ in os.walk(self.directory):
            self.content_dir.append(_)

    def collect_files(self):
        for content in self.content_dir[1:]:
            for filename in content[2]:
                file_path = (os.path.join(content[0], filename))
                self.files.append(file_path)

    def copy_files(self):
        for file in self.files:
            mtime = os.path.getmtime(file)
            result_time = time.gmtime(mtime)
            year = result_time.tm_year
            month = result_time.tm_mon
            year_month_dir = '../lesson_009/icons_by_year/{year}/{month}'.format(year=year, month=month)
            os.makedirs(year_month_dir, 0o777, exist_ok=True)
            if result_time.tm_year == year:
                if result_time.tm_mon == month:
                    shutil.copy2(file, year_month_dir)


class ArrangePhotosZip(ArrangePhotos):

    def walk_dir(self):
        zip_file = zipfile.ZipFile(self.directory, 'r')
        for directory in zip_file.namelist():
            zip_file.extract(directory)
            for _ in os.walk(directory):
                self.content_dir.append(_)
        return self.content_dir


# arrange = ArrangePhotos(directory='icons')
arrange = ArrangePhotosZip(directory='icons.zip')
arrange.run()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
