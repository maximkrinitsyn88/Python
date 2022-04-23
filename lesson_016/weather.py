# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
from pprint import pprint
from sqlite3 import connect
import argparse
import cv2
import requests
import re
import datetime
import models
from bs4 import BeautifulSoup
from playhouse.db_url import connect


class WeatherMaker:

    def __init__(self):
        self.html = requests.get('https://peterburg2.ru/pogoda/')
        self.day_pattern = r'\d+\s(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)'
        self.date_pattern = r'\d+'
        self.temp_pattern = r'[+|-]\d+'
        self.weather_pattern = 'Ясно|Пасмурно|Облачно|Малооблачно|Дождь|Снег'
        self.storage = []

    def getting_forecast(self):
        html_doc = BeautifulSoup(self.html.text, features="html.parser")
        list_doc = html_doc.find_all('tr', {'class': 'weather-show'})
        for i in list_doc:
            date = re.search(self.date_pattern, str(i))
            temp = re.search(self.temp_pattern, str(i))
            weather = re.search(self.weather_pattern, str(i))
            date = datetime.datetime.strptime(str(date.group()), '%Y%m%d').date()
            weather_dict = dict(weather_type=weather.group(), temperature=temp.group(), weather_date=date)
            self.storage.append(weather_dict)
        return self.storage


class ImageMaker:

    def __init__(self, weekly_forecast):
        self.img_background = cv2.imread('../lesson_016/python_snippets/external_data/probe.jpg')
        self.img_snow = cv2.imread('../lesson_016/python_snippets/external_data/weather_img/snow.jpg')
        self.img_rain = cv2.imread('../lesson_016/python_snippets/external_data/weather_img/rain.jpg')
        self.img_sun = cv2.imread('../lesson_016/python_snippets/external_data/weather_img/sun.jpg')
        self.img_cloud = cv2.imread('../lesson_016/python_snippets/external_data/weather_img/cloud.jpg')
        self.weekly_forecast = weekly_forecast

    def postcard_drawing(self):
        self.drawing_back_and_pict()

    def picture_overlay(self, img, img_back):
        img_back[(img_back.shape[0] // 2) - img.shape[0] // 2:(img_back.shape[0] // 2) + img.shape[0] // 2,
        img_back.shape[1] - img.shape[1] - 30:(img_back.shape[1] - 30)] = img[:img.shape[0], 0:img.shape[1]]

    def put_text(self, y, data):
        cv2.putText(img=self.img_background, color=(0, 0, 0), fontFace=cv2.FONT_HERSHEY_COMPLEX,
                    fontScale=1, org=(50, y), text=data)

    def view_image(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def drawing_back_and_pict(self):
        for day in self.weekly_forecast:
            for data in day.values():
                if isinstance(data, datetime.date):
                    data = str(data)
                    self.put_text(y=160, data=data)
                    self.view_image(self.img_background, 'Picture')
                if '+' or '-' in data:
                    self.put_text(y=120, data=data)
                p = 0
                i = 0
                k = 0
                z = 0
                if data == 'Ясно':
                    for _ in range(50):
                        self.img_background[:, 0 + i:50 + i] = (40 + k, 255, 255)
                        i += 7
                        k += 4
                        self.picture_overlay(img=self.img_sun, img_back=self.img_background)
                        self.put_text(y=80, data=data)
                elif data == 'Пасмурно' or data == 'Дождь':
                    for _ in range(54):
                        self.img_background[:, 0 + i:50 + i] = (255, 40 + k, 40 + k)
                        i += 7
                        k += 4
                        self.picture_overlay(img=self.img_rain, img_back=self.img_background)
                        self.put_text(y=80, data=data)
                elif data == 'Снег':
                    for _ in range(56):
                        self.img_background[:, 0 + i:50 + i] = (255, 140 + k, 30 + z)
                        i += 7
                        k += 2
                        z += 4
                        self.picture_overlay(img=self.img_snow, img_back=self.img_background)
                        self.put_text(y=80, data=data)
                elif data == 'Малооблачно' or data == 'Облачно':
                    for _ in range(56):
                        self.img_background[:, 0 + i:50 + i] = (144 + k, 128 + p, 112 + z)
                        i += 7
                        p += 2.2
                        z += 2.5
                        k += 2
                        self.picture_overlay(img=self.img_cloud, img_back=self.img_background)
                        self.put_text(y=80, data=data)


class DatabaseUpdater:
    def __init__(self, start_date, end_date, db_url='sqlite:///weather.db'):

        self.database = connect(db_url)
        models.db.initialize(self.database)
        self.weather = models.Weather
        self.weather.create_table()
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    def update_db(self, weekly_forecast):
        for day in weekly_forecast:
            if self.start_date <= day['weather_date'] <= self.end_date:
                self.weather.get_or_create(date=day['weather_date'],
                                           temperature=day['temperature'], weather=day['weather_type'])

    def get_forecast(self):
        for forecast in self.weather.select():
            date = datetime.datetime.strptime(forecast.date, '%Y-%m-%d').date()
            if self.start_date <= date <= self.end_date:
                print(f'{forecast.date} {forecast.temperature} {forecast.weather}')


def weather_forecast():
    parser = argparse.ArgumentParser(description='Completed ticket')
    parser.add_argument('start_date', type=str, help='start_date')
    parser.add_argument('end_date', type=str, help='end_date')
    args = parser.parse_args()
    try:
        while True:
            weather_maker = WeatherMaker()
            weekly_forecast = weather_maker.getting_forecast()
            action = int(input('Выберите действие:\n'
                  '1. Добавить прогнозы в БД \n'
                  '2. Получить прогнозы из БД \n'
                  '3. Создать открытки \n'
                  '4. Вывод прогнозов на консоль \n'
                  '5. Выход \n'))
            if action == 1:
                database_upd = DatabaseUpdater(args.start_date, args.end_date)
                database_upd.update_db(weekly_forecast)
                print('Добавление прогнозов за диапазон дат в базу данных успешно завершено')
            elif action == 2:
                database_get_forecast = DatabaseUpdater(args.start_date, args.end_date)
                database_get_forecast.get_forecast()
            elif action == 3:
                image = ImageMaker(weekly_forecast)
                image.postcard_drawing()
            elif action == 4:
                for date in weekly_forecast:
                    print(list(date.values()))
            elif action == 5:
                break
            else:
                print('Выберите цифру от 1 до 5')
    except Exception as exc:
        print('Ошибка:', exc)


weather_forecast()
