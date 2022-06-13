# Python Code Challenges involving Strings

# 1. Count Letters
# Write a function called unique_english_letters that takes the string word as a parameter. 
# The function should return the total number of unique letters in the string. 
# Uppercase and lowercase letters should be counted as different letters.

from typing import Counter


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

# Difficult Python Code Challenges Involving Strings

# 1. Check Name
# Write a function called check_for_name that takes two strings as parameters named sentence and name. 
# The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. 
# The function should return False otherwise.
# For example, the following three calls should all return True:
# check_for_name("My name is Jamie", "Jamie")
# check_for_name("My name is jamie", "Jamie")
# check_for_name("My name is JAMIE", "Jamie")

def check_for_name(sentence, name):
    return name.lower() in sentence.lower()

# 2. Every Other Letter
# Create a function named every_other_letter that takes a string named word as a parameter. 
# The function should return a string containing every other letter in word.

def every_other_letter(word):
    even_index_letters = ""
    for i in range(0, len(word), 2):
        even_index_letters += word[i]
    return even_index_letters

# 3. Reverse
# Write a function named reverse_string that has a string named word as a parameter. 
# The function should return word in reverse.

def reverse_string(word):
    return "".join(reversed(word))

# 4. Make Spoonerism
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. 
# Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. 
# Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
    word1_swapped = word2[0] + word1[1:]
    word2_swapped = word1[0] + word2[1:]
    return "{} {}".format(word1_swapped, word2_swapped)

# 5. Add Exclamation
# Create a function named add_exclamation that has one parameter named word. 
# This function should add exclamation points to the end of word until word is 20 characters long. 
# If word is already at least 20 characters long, just return word.

def add_exclamation(word):
    exclam = word
    if len(exclam) < 20:
        exclam += "!" * (20 - len(exclam))
    return exclam

# Python Code Challenges Involving Dictionaries

# 1. Sum Values
# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
    sum = 0
    for value in my_dictionary.values():
        sum += value
    return sum

# 2. Even Keys
# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. 
# This function should return the sum of the values of all even keys.

def sum_even_keys(my_dictionary):
    sum_of_evens = 0
    for item in my_dictionary.items():
        if item[0] % 2 == 0:
            sum_of_evens += item[1]
    return sum_of_evens

# 3. Add Ten
# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
# The function should add 10 to every value in my_dictionary and return my_dictionary

def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary

# 4. Values That Are Keys
# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
# This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):
    list_of_values_that_are_also_keys = []
    for key in my_dictionary:
        for value in my_dictionary.values():
            if key == value:
                list_of_values_that_are_also_keys.append(value)
    return list_of_values_that_are_also_keys

# 5. Largest Value
# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
# The function should return the key associated with the largest value in the dictionary.

def max_key(my_dictionary):
    largest_value = (0, float("-inf"))
    for item in my_dictionary.items():
        if item[1] > largest_value[1]:
            largest_value = item
    return largest_value[0]

# Difficult Python Code Challenges Involving Dictionaries

# 1. Word Length Dict
# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
# The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

def word_length_dictionary(words):
    my_dictionary = {}
    for word in words:
        my_dictionary[word] = len(word)
    return my_dictionary

# 2. Frequency Count
# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. 
# The function should return a dictionary containing the frequency of each element in words.

def frequency_dictionary(words):
    my_dictionary = {}
    for word in words:
        my_dictionary[word] = words.count(word)
    return my_dictionary

# 3. Unique Values
# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the number of unique values in the dictionary.

def unique_values(my_dictionary):
    uniques = []
    for value in my_dictionary.values():
        if value not in uniques:
            uniques.append(value)
    return len(uniques)

# 4. Count First Letter
# Create a function named count_first_letter that takes a dictionary named names as a parameter. 
# names should be a dictionary where the key is a last name and the value is a list of first names. 
# For example, the dictionary might look like this:
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.
# So in example above, the function would return:
# {"S" : 4, "L": 3}

def count_first_letter(names):
    letter_count = {key[0]:0 for (key, value) in names.items()}
    for key, value in names.items():
        letter_count[key[0]] += len(value)
    return letter_count

# Python Code Challenges Involving Classes

# 1. Setting Up Our Robot
# Create a python class called DriveBot. 
# Within this class, create instance variables for motor_speed, sensor_range, and direction. 
# All of these should be initialized to 0 by default. 
# After setting up the class, create an object from the class called robot_1. 
# Set the motor_speed to 5, the direction to 90, and the sensor_range to 10. 

class DriveBot:
    
    def __init__(self, motor_speed=0, sensor_range=0, direction=0):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction

robot_1 = DriveBot(motor_speed=5, direction=90, sensor_range=10)

# 2. Adding Robot Logic
# In the DriveBot class, add a method called control_bot which accepts parameters: new_speed and new_direction. 
# These should replace the associated instance variables. 
# Create another method called adjust_sensor which accepts a parameter called new_sensor_range which replaces the sensor_range instance variable. 
# Afterwards, use these methods to rotate the robot 180 degrees at 10 miles per hour with a sensor range of 20 feet.

class DriveBot:
    
    def __init__(self, motor_speed=0, sensor_range=0, direction=0):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot(motor_speed=5, direction=90, sensor_range=10)
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

# 3. Enhanced Constructor
# Upgrade the constructor in the DriveBot class in order to accept three optional parameters. 
# The constructor can accept motor_speed (which defaults to 0 if not provided), direction (which defaults to 180 if not provided, and sensor_range (which defaults to 10 if not provided). 
# These parameters should replace the associated instance variables. 
# Test out the upgraded constructor by initializing a new robot called robot_2 with a speed of 35, a direction of 75, and a sensor range of 25.

class DriveBot:
    
    def __init__(self, motor_speed=0, sensor_range=10, direction=180):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_2 = DriveBot(motor_speed=35, direction=75, sensor_range=25)

# 4. Controlling Them All
# Create a class variable called all_disabled which is set to False. 
# Next, create two more class variables called latitude and longitude. 
# Set both of those variables to equal -999999. 
# A third robot has been created below the first two robots. 
# Set the latitude of all of the robots to -50.0 at once. 
# Additionally, set the longitude of the robots to 50.0 and set all_disabled to True. 
# You should be able to set those values using three lines of code.

class DriveBot:

    all_disabled = False
    latitude = -999999
    longitude = -999999
    
    def __init__(self, motor_speed=0, sensor_range=10, direction=180):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
        
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot(motor_speed=5, direction=90, sensor_range=10)
robot_2 = DriveBot(motor_speed=35, direction=75, sensor_range=25)
robot_3 = DriveBot(motor_speed=20, direction=60, sensor_range=10)

DriveBot.latitude = -50.0
DriveBot.longitude = 50.0
DriveBot.all_disabled = True

# 5. Identifying Robots
# Within the DriveBot class, create an instance variable called id which will be assigned to the robot when the object is created. 
# Every time a robot is created, increment a counter (stored as a class variable) so that the next robot will have a different id. 
# For example, if three robots were created: first_robot, next_robot, and last_robot; first_robot will have an id of 1 next_robot will have an id of 2 and last_robot will have an id of 3.

class DriveBot:

    all_disabled = False
    latitude = -999999
    longitude = -999999
    id_counter = 1
    
    def __init__(self, motor_speed=0, sensor_range=10, direction=180):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
        self.id = DriveBot.id_counter
        DriveBot.id_counter += 1
        
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
