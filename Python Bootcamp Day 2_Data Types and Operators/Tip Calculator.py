#Tip Calculator

#ask bill total; input delivered as string format
bill = input("What is the total of the bill?\n"))

#ask num people
people = input("Between how many people will the bill be split?\n")

#ask tip percentage
tip = input("What percentage tip would you like to give?\n")

# generate bill and tip together. convert percentage to decimal
total = int(bill) * (1+(int(tip)/100))

#divide total bill by number of people and round to 2 decimal
per_person = round((total / int(people)),2)

#print result; add variable within quotes via: ${var}
print(f"Each person will pay ${per_person}")

