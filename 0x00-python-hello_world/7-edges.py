#!/user/bin/python3
word = "Holberton"
word_first_3, *_ , word_last_2 = word
middle_word = "".join(list(word)[2:-2])
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
