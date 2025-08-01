from random import randint

# 2
# Step 1: Create the Dog Class
#
#     Create a class called Dog.
#     In the __init__ method, take name and height as parameters and create corresponding attributes.
#     Create a bark() method that prints “ goes woof!”.
#     Create a jump() method that prints “ jumps cm high!”, where x is height * 2.
#
#
# Step 2: Create Dog Objects
#
#     Create davids_dog and sarahs_dog objects with their respective names and heights.
#
#
# Step 3: Print Dog Details and Call Methods
#
#     Print the name and height of each dog.
#     Call the bark() and jump() methods for each dog.


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {2 * self.height} cm hight!")


davids_dog = Dog("Truffle", randint(20, 80))
sarahs_dog = Dog("Archibald", randint(30, 100))

for dog in (davids_dog, sarahs_dog):
    print(f"This dog's name is {dog.name} and it's {dog.height} cm high.")
    dog.bark()
    dog.jump()
