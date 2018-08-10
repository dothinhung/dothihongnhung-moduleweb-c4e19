from mongoengine import *


# design database
class Video(Document):
    title = StringField()
    link = StringField()
    views = IntField()
    thumbnail = StringField()
    youtube_id = StringField()