# Step 1: Create the Dog Class
#
#     Create a class called Dog with name, age, and weight attributes.
#     Implement a bark() method that returns “ is barking”.
#     Implement a run_speed() method that returns weight / age * 10.
#     Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.
#
#
# Step 2: Create Dog Instances
#
#     Create three instances of the Dog class with different names, ages, and weights.
#
#
# Step 3: Test Dog Methods
#
#     Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.


class Dog:
    def __init__(self, dog_name, dog_age, dog_weight):
        self.name = dog_name
        self.age = dog_age
        self.weight = dog_weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / (self.age * 10)

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f"{self.name} won against {other_dog.name}!"
        else:
            return f"{other_dog.name} won against {self.name}!"


if __name__ == "__main__":
    dog_a = Dog("Arnold", 15, 100)
    dog_b = Dog("Ben", 21, 5)
    dog_c = Dog("Charlie", 2, 50)

    dogs = [dog_a, dog_b, dog_c]
    for dog in dogs:
        print(dog.bark())
        for other_dog in dogs:
            if dog != other_dog:
                print(dog.fight(other_dog))
