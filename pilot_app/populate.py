import mlab
from models.service import Service
from models.customer import Customer
from models.order import Order
from models.admin import Admin
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()


# for i in range(50):
#     ran_image = []
#     ran_description = sample(["ngoan hiền", "dễ thương", "lễ phép với gia đình"], 2)
#     ran_measurement = [randint(80,100), randint(50,70), randint(80,100)]
#     new_service = Service(
#         name = fake.name(),
#         yob = randint(1990,2000),
#         gender = randint(0,1),
#         height = randint(150,190),
#         phone = fake.phone_number(),
#         address = fake.address(),
#         status = choice([True,False]),
#         description = "{0}, {1}".format(*ran_description),
#         measurements = "{0} - {1} - {2}".format(*ran_measurement),
#         image = image
#     )

# for i in range(50):
#     new_customer = Customer(
#         name = fake.name(),
#         gender = randint(0, 1),
#         email = fake.email(),
#         phone = fake.phone_number(),
#         job = fake.job(),
#         company = fake.company()
#     )
#     # new_customer.save()

new_admin = Admin(
    name = "admin",
    password = "admin"
)

new_admin.save()