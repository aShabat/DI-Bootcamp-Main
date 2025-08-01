# 1
# Step 1: Create Cat Objects
#
#     Use the Cat class to create three cat objects with different names and ages.
#
#
# Step 2: Create a Function to Find the Oldest Cat
#
#     Create a function that takes the three cat objects as input.
#     Inside the function, compare the ages of the cats to find the oldest one.
#     Return the oldest cat object.
#
#
# Step 3: Print the Oldest Cat’s Details
#
#     Call the function to get the oldest cat.
#     Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
#     Replace <cat_name> and <cat_age> with the oldest cat’s name and age.
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


from random import randint

first = Cat("Tom", randint(1, 15))
second = Cat("Simon", randint(1, 15))
third = Cat("Boris", randint(1, 15))


def oldest_cat(first, second, third):
    if first.age >= second.age and first.age >= third.age:
        return first
    elif second.age >= first.age and second.age >= third.age:
        return second
    else:
        return third


oldest = oldest_cat(first, second, third)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")
