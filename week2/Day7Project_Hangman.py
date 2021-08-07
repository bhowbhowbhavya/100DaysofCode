import random
import Day7_module_logo


print(Day7_module_logo.logo)

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

lives = 6

from Day7_module_word_list import word_list
chosen_word = random.choice(word_list)
   
blanks_list = list()
for i in range(len(chosen_word)):
    blanks_list += "_"
print(blanks_list)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in blanks_list:
        print(f"You have already guessed {guess}")
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if guess == letter:
            blanks_list[i] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you lose a life!")
        lives -= 1
        
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(blanks_list)       
    if "_" not in blanks_list:
        end_of_game = True
        print("You win.")
    
print(f"The word is {chosen_word}")


