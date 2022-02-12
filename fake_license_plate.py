from faker import *

faker = Faker()
for x in range(10):
    print(faker.license_plate)
