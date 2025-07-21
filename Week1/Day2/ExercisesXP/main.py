# 1
# Print the following output in one line of code:
#
# Hello world
# Hello world
# Hello world
# Hello world

print("Hello world\n" * 4)

# 2
# Write code that calculates the result of:
#
# (99^3)*8 (meaning 99 to the power of 3, times 8).
print(8 * 99**3)

# 3
# Predict the output of the following code snippets:
#
# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

print(False, True, False, "Error", False, sep="\n")

# 4
#     Create a variable called computer_brand which value is the brand name of your computer.
#     Using the computer_brand variable, print a sentence that states the following:
#
# "I have a <computer_brand> computer."

computer_brand = "custom"
print(f"I have a {computer_brand} computer.")

# 5
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = "Anton"
age = 25
shoe_size = 42
info = f"My name is {name}. I'm {age}. My shoe size is {shoe_size}."
print(info)

# 6
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

from random import randint

a, b = randint(1, 100), randint(1, 100)
if a > b:
    print("Hello World")

# 7
# Write code that asks the user for a number and determines whether this number is odd or even.

n = int(input("Write a number: "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

# 8
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

name = input("Write your name: ")
my_name = "Anton"
if name == my_name:
    print("This is a joke about us having the same names.")
else:
    print("We have different names. There is no joke.")

# 9
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

height = int(input("Write your height in centimeters: "))
if height > 145:
    print("You are tall enough to ride here.")
else:
    print("Grow up!")
