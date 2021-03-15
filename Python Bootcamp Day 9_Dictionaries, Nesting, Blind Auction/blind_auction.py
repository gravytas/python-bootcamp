#blind auction program

from replit import clear
import art

print(art.logo)

print("Welcome to the secret auction program")

bidders = True
bids = {}
def find_winner():
  high_bid = 0
  winner = ""
  for bidder in bids:
    if bids[bidder] > high_bid:
      high_bid = bids[bidder]
      winner = bidder
  print(f"The winner of the auction is {winner} with a bid of ${bid}")    

while bidders:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))
  others = input("Are there any other bidders? y/n: ")
  bids[name] = bid
  if others == "n":
    bidders = False
  else:
    clear()  
find_winner()






