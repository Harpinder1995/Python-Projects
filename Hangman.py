import random
import string

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

str = ["stones", "thrones", "destroyer"]
random_text = random.choice(str)
print(f"The Choosen Word is {random_text}")
display = []
for i in range(len(random_text)):
    display += "_"
print(display)
end_of_game = False
lives = len(random_text)
print(lives)
l = 6
while not end_of_game:
    user_input = input("Guess the letter").lower()
    for i in range(len(random_text)):

        letter = random_text[i]
        if letter == user_input:
            display[i] = letter
    for j in display:
        if user_input not in display:
            print(stages[l])
            l -= 1
            if l < 0:
                end_of_game = True
                print("Game Over Hangman")
            break
        else:
            continue
    print(display)
    if "_" not in display:
        end_of_game = True
