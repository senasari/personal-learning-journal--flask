from peewee import *


import datetime

db = SqliteDatabase('journal.db')


class Post(Model):
    title = CharField()
    date = DateField()  # what am i going to store date as?
    timespent = CharField()
    content = TextField()
    resources = TextField()

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Post], safe=True)
    db.close()
