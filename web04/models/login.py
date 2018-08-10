from mongoengine import *


# design database
class Login(Document):
    username = StringField()
    password = StringField()