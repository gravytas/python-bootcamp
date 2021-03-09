#Rock Paper Scissors Game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

choices = ["rock", "paper", "scissors"]
user = int(input("Type 0 for rock, 1 for paper, or 2 for scissors.\n"))
comp = random.randint(0,2)

user_choice = choices[user]
comp_choice = choices[comp]

print(f"User chose: {images[user]}")
print(f"Opponent chose: {images[comp]}")

if user==0 and comp==2:
  print("You Win!")
elif user==2 and comp==0:
  print("You lose!") 
elif user == comp:
  print("The game is a draw!")
elif user>comp:
   print("You Win!")
else:
  print("You lose!")


  