# 1
# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.
words = input().split(",")
words.sort()
print(",".join(words))

# 2
# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.
words = input().split(" ")
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)
