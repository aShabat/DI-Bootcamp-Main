# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

from random import randint

a, b = randint(1, 100), randint(1, 100)
if a > b:
    print("Hello World")
