# Step 1: Import the string and random modules
#
#     Import the string and random modules.
#
#
# Step 2: Create a string of all letters
#
# Read about the strings methods HERE to find the best methods for this step
#
#
# Step 3: Generate a random string
#
#     Use a loop to select 5 random characters from the combined string.
#     Concatenate the characters to form the random string.

import string
import random

result = ""
letters = string.ascii_letters
for _ in range(5):
    result += random.choice(letters)

print(result)
