# -*- coding: utf-8 -*-
import argparse
from PIL import Image, ImageDraw, ImageFont


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


def make_ticket(fio, from_, to, date):
    ticket = Image.open("./images/ticket_template.png")
    draw = ImageDraw.Draw(ticket)
    font = ImageFont.truetype("fonts/Prata.ttf", size=16)
    x = 45
    draw.text((x, 122), f'{fio}', font=font, fill='black')
    draw.text((x, 191), f'{from_}', font=font, fill='black')
    draw.text((x, 257), f'{to}', font=font, fill='black')
    draw.text((287, 257), f'{date}', font=font, fill='black')
    ticket.show()
    ticket.save('ticket_FIO.png')


make_ticket(fio='Иванов Иван Иванович', from_='Москва', to='Лондон', date='20.02.2022')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

parser = argparse.ArgumentParser(description='Completed ticket')
parser.add_argument('fio', type=str, help='FIO')
parser.add_argument('from_', type=str, help='from')
parser.add_argument('to', type=str, help='to')
parser.add_argument('date', type=str, help='Date')
args = parser.parse_args()


def make_ticket(fio, from_, to, date):
    ticket = Image.open("./images/ticket_template.png")
    draw = ImageDraw.Draw(ticket)
    font = ImageFont.truetype("fonts/Prata.ttf", size=16)
    x = 45
    draw.text((x, 122), f'{fio}', font=font, fill='magenta')
    draw.text((x, 191), f'{from_}', font=font, fill='magenta')
    draw.text((x, 257), f'{to}', font=font, fill='magenta')
    draw.text((287, 257), f'{date}', font=font, fill='magenta')
    ticket.show()
    ticket.save('ticket_FIO.png')


make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date)
