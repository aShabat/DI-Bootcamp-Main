# 1. Ask the user for two inputs
#     A number (integer).
#     A length (integer).
#
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

number = int(input("Write a number: "))
length = int(input("Write a length: "))
print([number * i for i in range(1, length + 1)])
