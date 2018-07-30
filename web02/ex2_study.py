from mongoengine import *
from models.customer import Customer
import mlab

mlab.connect()

id_to_find = "5b5c7b2eb38f670be8d02707"
obj = Customer.objects.get(id=id_to_find)
print(obj.name)

print("* " * 20)

print("Delete data")
obj.delete()