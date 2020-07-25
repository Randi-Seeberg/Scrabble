letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_lowercase = []
for letter in letters:
  letters_lowercase += letter.lower()
  
letter_lower_to_points = {key:value for key, value in zip(letters_lowercase, points)}

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
# Find en måde at lægge dictionaries sammen

letter_to_points.update(letter_lower_to_points)

print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    try:
      point_total += letter_to_points[letter]
    except KeyError:
      point_total += 0
  return point_total

brownie_points = score_word("BROWNIE")
#print(brownie_points)

player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
  
#print(player_to_points)

def play_word(player, word):
  player_to_words[player] += [word]
  return player_to_words

#print(play_word("Prof Reader", "COCONUT"))

def update_point_totals(player, word):
  player_to_words[player] += [word]
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
  player_to_points[player] = player_points
  return player_to_points

#print(update_point_totals("Prof Reader", "COCONUT"))






      
    