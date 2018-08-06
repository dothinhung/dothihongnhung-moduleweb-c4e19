import mlab
from mongoengine import *

mlab.connect()

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()


river = River.objects(continent ='Africa')
for i in river:
    print(i.name)

print("*"*20)

river_2 = River.objects(continent="S. America", length__lt=2000)
for i in river_2:
    print(i.name)
