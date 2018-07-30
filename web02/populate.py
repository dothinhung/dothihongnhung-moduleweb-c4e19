from models.service import Service
from models.customer import Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

# print(fake.address())
for i in range(50):
    print("Saving servive", i + 1)
    new_service = Service(
        name = fake.name(),
        yob = randint(1990, 2000),
        gender = randint(0, 1),
        height = randint(150, 190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True, False])
    )
    # new_service.save()

for j in range(50):
    print("Customer......", i + 1)
    new_customer = Customer(
        name = fake.name(),
        gender = randint(0, 1),
        phone = fake.phone_number(),
        email = fake.email(),
        job = fake.job()
    )
    # new_customer.save()



