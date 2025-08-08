# Step 1: Install the faker module
#
# Step 2: Import the faker module
#
# Step 3: Create an empty list of users
#
# Step 4: Create a function to add users
#
#     Create a function that takes the number of users to generate as an argument.
#     Inside the function, use a loop to generate the specified number of users.
#     For each user, create a dictionary with the keys name, address, and language_code.
#     Use the faker instance to generate fake data for each key:
#         name: faker.name()
#         address: faker.address()
#         language_code: faker.language_code()
#     Append the user dictionary to the users list.
#
# Step 5: Call the function and print the users list

import faker

global_faker = faker.Faker()
users = []


def new_user():
    user = {
        "name": global_faker.name(),
        "address": global_faker.address(),
        "language_code": global_faker.language_code(),
    }
    return user


def add_users(users, amount):
    for _ in range(amount):
        users.append(new_user())
    return users


add_users(users, 5)
print(users)
