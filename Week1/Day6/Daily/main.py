# 1
# 1. User Input:
#
#     Ask the user to enter a word.
#     Store the input word in a variable.
#
# 2. Creating the Dictionary:
#
#     Iterate through each character of the input word using a loop.
#     And check if the character is already a key in the dictionary.
#         If it is, append the current index to the list associated with that key.
#         If it is not, create a new key-value pair in the dictionary.
#     Ensure that the characters (keys) are strings.
#     Ensure that the indices (values) are stored in lists.
#

word = input("Write a word: ")

characters = {}
for i, c in enumerate(word):
    if c in characters:
        characters[c].append(i)
    else:
        characters[c] = [i]

print(characters)

# 2
# 1. Store Data:
#
#     You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign).
#     You will also be given a string (wallet) representing the amount of money you have.
#
# 2. Data Cleaning:
#
# 3. Determining Affordable Items:
#
# 4. Sorting and Output:
#
#     Sort the list of affordable items in alphabetical order.
#     If the list is empty (no items can be afforded), return the string “Nothing”.
#     Otherwise, return the sorted list.


def money_to_int(money):
    if money[0] == "$":
        return int(money[1:].replace(",", ""))
    raise Exception("Doesn't start with '$'")


def affordable_items(items, wallet):
    wallet = money_to_int(wallet)
    items = {key: money_to_int(cost) for (key, cost) in items.items()}
    return sorted([key for key, cost in items.items() if cost <= wallet])
