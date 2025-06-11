from faker import Faker
faker = Faker()

# Generate dummy data for a user profile
print(faker.name())
print(faker.email())
print(faker.address())
print(faker.phone_number())
print(faker.text(max_nb_chars=200))
print(faker.date_of_birth(minimum_age=18, maximum_age=90))
print(faker.job())
print(faker.company())
print(faker.country())



