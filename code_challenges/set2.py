# Python Code Challenges involving Strings

# 1. Count Letters
# Write a function called unique_english_letters that takes the string word as a parameter. 
# The function should return the total number of unique letters in the string. 
# Uppercase and lowercase letters should be counted as different letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
    unique_letter_count = 0
    for letter in letters:
        if letter in word:
            unique_letter_count += 1
    return unique_letter_count

# 2. Count X
# Write a function named count_char_x that takes a string named word and a single character named x as parameters. 
# The function should return the number of times x appears in word.

def count_char_x(word, x):
    x_count = 0
    for letter in word:
        if letter == x:
            x_count += 1
    return x_count

# 3. Count Multi X
# Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. 
# However, this time, make sure your function works when x is multiple characters long.
# For example, count_multi_char_x("Mississippi", "iss") should return 2

def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits) - 1)

# 4. Substring Between
# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. 
# This function should return the substring between the first occurrence of start and end in word. 
# If start or end are not in word, the function should return word.
# For example, substring_between_letters("apple", "p", "e") should return "pl".

def substring_between_letters(word, start, end):
    try:
        start_index = word.index(start) + 1
        end_index = word.index(end)
    except: 
        ValueError
        return word
    return word[start_index:end_index]

# 5. X Length
# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. 
# This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
    words = sentence.split()
    for word in words:
        if len(word) < x:
            return False
    return True
