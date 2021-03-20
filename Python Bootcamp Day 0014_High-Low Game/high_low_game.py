#Higher Lower Game

import art
from game_data import data
import random
from replit import clear

def select_choice():
  choice = random.choice(data)
  data.remove(choice)
  return choice 

def format(choice):
  return f"{choice['name']}, {choice['description']}, {choice['country']}"
  
def compare(guess, afoll, bfoll):
  if afoll>bfoll:
    return guess == "a"
  else:
    return guess == "b"  

  ########################

def game():
  print(art.logo)
  score = 0
  cont_game = True
  a = select_choice()
  b = select_choice()

  while cont_game:
    a = b
    b = select_choice()

    while a == b:
      b = select_choice()
    
    followers_a = a["follower_count"]
    followers_b = b["follower_count"]
    
    while followers_a == followers_b:
      b=select_choice()  

    print(f"Compare A: {format(a)}.")
    print(art.vs)
    print(f"Compare B: {format(b)}.")
   
    guess = input("Who has more followers? a/b: ")
    correct = compare(guess, followers_a, followers_b)
  
    clear()
    print(art.logo)
    if correct:
      score +=1
      print(f"Correct! Current score: {score}")
    else:
      cont_game = False
      print(f"Sorry, that's wrong. Final score: {score}")
      again = input("Play again? y/n: ")
      if again == "y":
        clear()
        game()
      else:
        print("Goodbye!")

game()

  
