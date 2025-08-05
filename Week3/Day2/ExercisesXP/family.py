# Step 1: Create the Person Class
#
#     Define a Person class with the following attributes:
#     first_name
#     age
#     last_name (string, should be initialized as an empty string)
#     Add a method called is_18():
#     It should return True if the person is 18 or older, otherwise False.
#
#
# Step 2: Create the Family Class
#
#     Define a Family class with:
#         A last_name attribute
#         A members list that will store Person objects (should be initialized as an empty list)
#
#
#     Add a method called born(first_name, age):
#         It should create a new Person object with the given first name and age.
#         It should assign the family’s last name to the person.
#         It should add this new person to the members list.
#
#
#     Add a method called check_majority(first_name):
#         It should search the members list for a person with that first_name.
#             If the person exists, call their is_18() method.
#         If the person is over 18, print:
#             "You are over 18, your parents Jane and John accept that you will go out with your friends"
#         Otherwise, print:
#             "SSorry, you are not allowed to go out with your friends.orry, you are not allowed to go out with your friends."
#
#
#     Add a method called family_presentation():
#         It should print the family’s last name.
#         Then, it should print each family member’s first name and age.


class Person:
    def __init__(self, first_name, age, last_name):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        self.members.append(Person(first_name, age, self.last_name))

    def check_majority(self, first_name):
        for p in self.members:
            if p.first_name == first_name:
                if p.is_18():
                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"Couldn't find {first_name} among members of the family")

    def family_presentation(self):
        print(f"This is {self.last_name} family:")
        for member in self.members:
            print(f"{member.first_name} is {member.age}.")
