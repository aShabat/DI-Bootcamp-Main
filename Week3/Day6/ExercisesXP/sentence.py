# Step 1: Create the get_words_from_file function
#
#     Create a function named get_words_from_file that takes the file path as an argument.
#     Open the file in read mode ("r").
#     Read the file content.
#     Split the content into a list of words.
#     Return the list of words.
#
#
# Step 2: Create the get_random_sentence function
#
#     Create a function named get_random_sentence that takes the sentence length as an argument.
#     Call get_words_from_file to get the list of words.
#     Select a random word from the list length times.
#     Create a sentence with the selected words.
#     Convert the sentence to lowercase.
#     Return the sentence.
#
#
# Step 3: Create the main function
#
#     Create a function named main.
#     Print a message explaining the program’s purpose.
#     Ask the user for the desired sentence length.
#     Validate the user input:
#         Check if it is an integer.
#         Check if it is between 2 and 20 (inclusive).
#     If the input is invalid, print an error message and exit.
#     If the input is valid, call get_random_sentence with the length and print the generated sentence.

from random import choice


def get_words_from_file(file):
    return [line.strip() for line in open(file, "r")]


def get_random_sentence(length):
    words = get_words_from_file("words.txt")
    sentence = []
    for _ in range(length):
        sentence.append(choice(words))
    sentence = " ".join(sentence)
    sentence = sentence.lower()

    return sentence


def main():
    print("This programm will generate a random sentence.")
    length = input("Please write the length of the sentence between 2 and 20: ")
    try:
        length = int(length)
    except:
        raise ValueError("Expected a number")
    if length < 2 or length > 20:
        raise ValueError("Expected a number between 2 and 20")
    print(get_random_sentence(length))


if __name__ == "__main__":
    main()
