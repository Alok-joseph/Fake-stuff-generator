from faker import *

faker = Faker()
for x in range(10):
    print(faker.phone_number)
