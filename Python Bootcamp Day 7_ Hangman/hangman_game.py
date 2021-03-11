#Hangman Game

#Step 4

import random
import hangman_words
from hangman_art import logo, stages 
import os
print(logo)

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
lives = 6

display = []
guesses = []
for x in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print(f"You've already guessed {guess}")
    guesses.append(guess)
    
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        

    if guess not in chosen_word:
        print(f"You guessed {guess} which is not in the word. You have {lives} lives remaining")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Game over.")
            exit

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
  
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    print(stages[lives])