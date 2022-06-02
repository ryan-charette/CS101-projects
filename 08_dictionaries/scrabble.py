#In this project, you will process some data from a group of friends playing scrabble.
#You will use dictionaries to organize players, words, and points.

#Initial variables
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

#Combine letters and points into a dictionary that maps a lettter to its point value
letters_to_points = {key:value for key, value in zip(letters, points)}
letters_to_points[" "] = 0

#Function that takes in a word and returns how many points that word is worth
def score_word(word):
  point_total = 0
  word_upper = word.upper()
  for letter in word_upper:
      point_total += letters_to_points.get(letter, 0)
  return point_total

#Function that maps players to how many points they've scored
def calculate_point_totals():
  for item in player_to_words.items():
    player = item[0]
    words = item[1]
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

#Function that takes in a player and a word and adds that word to the list of words they've played
def play_word(player, word):
  player_to_words[player].append(word)
  return
