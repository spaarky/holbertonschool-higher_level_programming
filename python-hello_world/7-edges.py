#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3].format()
word_last_2 = word[-2:].format()
middle_word = word[1:8].format()
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
