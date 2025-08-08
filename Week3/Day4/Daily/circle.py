# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#
#     Compute the circle’s area
#     Print the attributes of the circle - use a dunder method
#     Be able to add two circles together, and return a new circle with the new radius - use a dunder method
#     Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
#     Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
#     Be able to put them in a list and sort them
#     Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles


import math
from typing import override


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius != None:
            self.__radius = radius
        elif diameter != None:
            self.__radius = diameter / 2
        else:
            raise ValueError("Haven't specified radius nor diameter for a circle")

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    radius = property(get_radius, set_radius)

    def get_diameter(self):
        return self.__radius * 2

    def set_diameter(self, diameter):
        self.__radius = diameter / 2

    diameter = property(get_diameter, set_diameter)

    def area(self):
        return math.pi * self.radius**2

    @override
    def __str__(self) -> str:
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError(f"Can't add a Circle and a {type(other)}")

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius
