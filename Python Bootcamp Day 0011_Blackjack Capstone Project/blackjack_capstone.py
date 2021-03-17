#Blackjack Project

from replit import clear
import random
import art

# Our Blackjack House Rules #

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

user_hand = []
dealer_hand = []

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(hand):
  if sum(hand) == 21 and len(hand) == 2:
    return 0 
  if 11 in hand and sum(hand) >21:
    hand.remove[11]
    hand.append[1]
  return sum(hand)

def compare(user, dealer):
  if user == dealer:
    return "Draw"
  elif user == 0:
    return "User wins!"
  elif dealer == 0: 
    return "Dealer wins!"
  elif user > dealer:
    return "User wins!"
  elif dealer > user:
    return "Dealer wins!"

def blackjack():
  print(art.logo)
  playing = True
  user_hand = []
  dealer_hand = []
  
  x = 0
  while x < 2: 
    user_hand.append(deal_card())
    dealer_hand.append(deal_card())
    x += 1
  
  print(f"The user's card are {user_hand[0]}, {user_hand[1]}")
  print(f"Dealer holds the cards _ ,{dealer_hand[1]}")

  while playing:
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)
    
    if user_score == 0 or dealer_score == 0 or user_score > 21:
      playing = False
    else:
      hit = input("Do you want another card? y/n: ")
      if hit == "y":
        user_hand.append(deal_card()) 
        user_score = calculate_score(user_hand)
        print(f"Your hand is {user_hand} and your score is {user_score}")
      if hit == "n":
        playing = False

  while calculate_score(dealer_hand) != 0 and calculate_score(dealer_hand) < 17:
    dealer_hand.append(deal_card())
    dealer_score = calculate_score(dealer_hand)
  
  print(f"Your final hand is {user_hand} and your final score is {user_score}")

  print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
  
  print(compare(user_score, dealer_score))

  again = input("Would you like to play again? y/n: ")
  if again == "y":
    clear()
    blackjack()
  else:
    clear()
    print("Thanks for playing!")

blackjack()

