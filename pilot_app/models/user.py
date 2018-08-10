from mongoengine import *

class User(Document):
    full_name = StringField()
    username = StringField()
    email = EmailField()
    password = StringField()