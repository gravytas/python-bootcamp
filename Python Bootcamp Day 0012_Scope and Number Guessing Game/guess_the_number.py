#Number guessing game

import random
import art

print(art.logo)

def check_answer(guess, answer, turns):
  """checks answer against guess. Returns number of turns remaining"""
  if guess > answer:
    print("Too high.")
    turns -= 1
  elif guess < answer:
    print("Too low.")
    turns -= 1
  else:
    print(f"You got it! the answer was {answer}")

def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return 10
  elif level == "hard":
    return 5    

def game():
  #generate number between 1 and 100
  print("Welcome to Guess the Number!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1,100)

  turns = difficulty()
  print(f"You have {turns} turns remaining")


  guess = 0
  while guess != answer: 
  #user guesses number
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)

game()