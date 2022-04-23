from peewee import *

db = DatabaseProxy()


class Weather(Model):
    date = DateField(formats='%Y-%m-%d')
    temperature = CharField()
    weather = CharField()

    class Meta:
        database = db