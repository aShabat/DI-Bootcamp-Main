# 1. Ask for User Input:
#
#     The string must be exactly 10 characters long.
#
# 2. Check the Length of the String:
#
#     If the string is less than 10 characters, print: "String not long enough."
#     If the string is more than 10 characters, print: "String too long."
#     If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
#
# 3. Print the First and Last Characters:
#
#     Once the string is validated, print the first and last characters.
#
# 4. Build the String Character by Character:
#
#     Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
#
# Hint: You can create a loop that goes through the string, adding one character at a time, and print it progressively.
#
# 5. Bonus: Jumble the String (Optional)
#
#     As a bonus, try shuffling the characters in the string and print the newly jumbled string.
#
# Hint: You can use the random.shuffle function to shuffle a list of characters.

text = input("Write a string 10 characters long: ")
while len(text) != 10:
    if len(text) > 10:
        print("String too long.")
    else:
        print("String not long enough.")

print("Perfect string.")

print(text[0], text[-1])

text_rebuilt = ""
for char in text:
    text_rebuilt += char
    print(text_rebuilt)

from random import shuffle

text_list = list(text)
shuffle(text_list)
print("".join(text_list))
