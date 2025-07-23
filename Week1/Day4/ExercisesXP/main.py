# 1
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.

from reprlib import aRepr


my_fav_numbers = {0, 1, 2, 3, 5, 8, 13, 21}
my_fav_numbers.add(34)
my_fav_numbers.add(55)

friend_fav_numbers = {1, 4, 9, 16}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# 2
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

tuple = (0, 1)
# tuple.add(2)

# 3
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

# 4
# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.

array = [n / 2 if n % 2 == 1 else n // 2 for n in range(3, 11)]
print(array)

# 5
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for n in range(1, 21):
    print(n)

for n in range(1, 21):
    if n % 2 == 1:
        print(n)

# 6
# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.

while True:
    name = input("Write a name: ")
    if name == "Anton":
        print("That's my name")
        break

# 7
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

fruits = input("Write your favourite fruits: ").split(" ")
fruit = input("Write any fruit: ")
if fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# 8
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
#     The base price is $10, and each topping adds $2.50.

toppings = []
while True:
    new = input("Write another topping: ")
    if new == "quit":
        break
    toppings.append(new)
for t in toppings:
    print(f"Adding {t} to your pizza.")

print(f"{', '.join(toppings)}: ${10 + 2.5 * len(toppings)}")

# 9
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
#     Free for people under 3.
#     $10 for people aged 3 to 12.
#     $15 for anyone over 12.
# Print the total ticket cost.

ages = map(int, input("Write your ages: ").split())
total = 0
for age in ages:
    if age > 12:
        total += 15
    elif age >= 3:
        total += 10
print(f"Your total is ${total}")

# 10
# Using the list:
# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
# The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
# Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
# Print a message for each sandwich made, such as: "I made your Tuna sandwich."
# Print the final list of all finished sandwiches.

sandwich_orders = [
    "Tuna",
    "Pastrami",
    "Avocado",
    "Pastrami",
    "Egg",
    "Chicken",
    "Pastrami",
]

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

finished_sandwiches = []
for s in sandwich_orders:
    print(f"I made your {s} sandwich.")
    finished_sandwiches.append(s)
print(finished_sandwiches)
