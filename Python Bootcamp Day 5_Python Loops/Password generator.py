#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letter= int(input("How many letters would you like in your password?\n")) 
num_symbol = int(input(f"How many symbols would you like?\n"))
num_number = int(input(f"How many numbers would you like?\n"))

chosen_letters =[]
chosen_symbols = []
chosen_numbers = []

for x in range(0, num_letter):
  pick = random.randint(0,52)
  chosen_letters.append(letters[pick])

for x in range(0, num_symbol):
  pick = random.randint(0,8)
  chosen_symbols.append(symbols[pick])

for x in range(0, num_number):
  pick = random.randint(0,9)
  chosen_numbers.append(numbers[pick])

pass_list = chosen_letters + chosen_symbols + chosen_numbers

### hard version

random.shuffle(pass_list)

password = ""
for x in pass_list:
  password += x

print(f"Your password is: {password}")
