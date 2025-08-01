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

# 3
# Step 1: Create the Song Class
#
#     Create a class called Song.
#     In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
#     Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# 4
# Step 1: Define the Zoo Class
#
# 1. Create a class called Zoo.
#
# 2. Implement the __init__() method:
#
#     It takes a string parameter zoo_name, representing the name of the zoo.
#     Initialize an empty list called animals to keep track of animal names.
#
# 3. Add a method add_animal(new_animal):
#
#     This method adds a new animal to the animals list.
#     Do not add the animal if it is already in the list.
#
# 4. Add a method get_animals():
#
#     This method prints all animals currently in the zoo.
#
# 5. Add a method sell_animal(animal_sold):
#
#     This method checks if a specified animal exists on the animals list and if so, remove from it.
#
# 6. Add a method sort_animals():
#
#     This method sorts the animals alphabetically.
#     It also groups them by the first letter of their name.
#     The result should be a dictionary where:
#         Each key is a letter.
#         Each value is a list of animals that start with that letter.
# 7. Add a method get_groups():
#
#     This method prints the grouped animals as created by sort_animals().


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.__animals_by_letter = None

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("In the zoo there are " + ", ".join(self.animals) + ".")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        self.__animals_by_letter = {}
        for animal in self.animals:
            if animal[0] in self.__animals_by_letter:
                self.__animals_by_letter[animal[0]].append(animal)
            else:
                self.__animals_by_letter[animal[0]] = [animal]
        return self.__animals_by_letter

    def get_groups(self):
        return self.__animals_by_letter


# Step 2: Create a Zoo Object
#
#     Create an instance of the Zoo class and pass a name for the zoo.

zoo = Zoo("Grand zoo")

# Step 3: Call the Zoo Methods
#
#     Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.

zoo.add_animal("goat")
zoo.add_animal("lion")
zoo.get_animals()
zoo.add_animal("lion")
zoo.get_animals()
zoo.add_animal("monkey")
zoo.sell_animal("goat")
zoo.get_animals()
zoo.add_animal("leopard")
zoo.add_animal("mouse")
zoo.add_animal("horse")
zoo.sort_animals()
zoo.get_animals()
print(zoo.get_groups())
