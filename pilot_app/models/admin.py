from mongoengine import *


class Admin(Document):
    name = StringField()
    password = StringField()



