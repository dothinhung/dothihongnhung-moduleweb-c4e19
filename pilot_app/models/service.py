from mongoengine import *

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = IntField()
    description = StringField()
    image = URLField()
    measurements = ListField(IntField())