# Step 1: Import the Dog Class
#
#     In a new Python file, import the Dog class from the previous exercise.
#
#
# Step 2: Create the PetDog Class
#
#     Create a class called PetDog that inherits from the Dog class.
#     Add a trained attribute to the __init__ method, with a default value of False.
#     trained means that the dog is trained to do some tricks.
#     Implement a train() method that prints the output of bark() and sets trained to True.
#     Implement a play(*args) method that prints “ all play together”.
#     *args on this method is a list of dog instances.
#     Implement a do_a_trick() method that prints a random trick if trained is True.
#     Use this list for the ramdom tricks:
#     tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#     Choose a rendom index from it each time the method is called.
#
#
# Step 3: Test PetDog Methods
#
#     Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.

from dog import Dog  # pyright: ignore[reportImplicitRelativeImport]
from random import randint


class PetDog(Dog):
    def __init__(self, dog_name, dog_age, dog_weight, dog_trained=False):
        super().__init__(dog_name, dog_age, dog_weight)
        self.trained = dog_trained

    def train(self):
        self.trained = True
        return self.bark()

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        dog_names.insert(0, self.name)
        return (
            ", ".join(dog_names[:-1]) + " and " + dog_names[-1] + " all play together"
        )

    def do_a_trick(self):
        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead",
        ]
        trick = tricks[randint(0, len(tricks) - 1)]
        return self.name + " " + trick


dog_a = PetDog("Arnold", 15, 100)
dog_b = PetDog("Ben", 21, 5, True)
dog_c = PetDog("Charlie", 2, 50, False)

print(dog_a.train())
print(dog_a.play(dog_b, dog_c))
print(dog_a.do_a_trick())
