from string import ascii_letters
from anagram_checker import AnagramChecker


ac = AnagramChecker()
while True:
    command = input(
        "\nDo you want to (W)rite a word and look for it's anagrams or (e)xit?\n"
    )
    if command == "" or command.lower().strip() == "w":
        word = input("Write a word: ")
        word = word.strip()

        valid = True
        for c in word:
            if c not in ascii_letters:
                print("Your word should only contain english letters.")
                valid = False
                break
        if not valid:
            continue
        print(f'\nYOUR WORD: "{word.upper()}"')
        if ac.is_valid_word(word):
            print("this is a valid english word.")
        else:
            print("this is not a valid english word.")

        anagrams = ac.get_anagrams(word)
        if len(anagrams) == 0:
            print("There are no anagrams for your word.")
        else:
            print(f"Anagrams for your word: {", ".join(anagrams)}.")

    elif command.lower().strip() == "e":
        print("Stopping the programm...")
        break
    else:
        print(f"{command.lower().strip()} is not a valid option.")
