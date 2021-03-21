MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

def check_resources(avail, needed):
    for x in range(0,len(needed)):
        if avail[x] < needed[x]:
            print("Not enough resources. Please choose another option")
            return False
        else:
            return True

def calculate_payment(quarters, dimes, nickels, pennies):
    amt_paid = quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01
    return amt_paid

def obtain_resources(drink):
    needed_resources = []
    avail_resources = []
    for x in MENU[drink]["ingredients"]:
        needed_resources.append(MENU[drink]["ingredients"][x])
        avail_resources.append(resources[x])
    return avail_resources, needed_resources

remain_on = True
while remain_on:
    drink = input('What would you like? espresso/latte/cappuccino: ')
    if drink == "report":
        print(f"Water: {resources['water']} ml.\nCoffee: {resources['coffee']}\nMilk: {resources['milk']}ml.")
    elif drink == "off":
        remain_on = False
    else:
        obtain_resources(drink)
        enough_resources = check_resources(obtain_resources(drink)[0], obtain_resources(drink)[1])

        if enough_resources:
           cost = MENU[drink]["cost"]
           print(f"This choice costs ${cost}. Please insert payment.\n")
           quarters = int(input("Quarters: "))
           dimes = int(input("Dimes: "))
           nickels = int(input("Nickels: "))
           pennies = int(input("Pennies: "))
           paid = calculate_payment(quarters, dimes, nickels, pennies)

        if paid < cost:
            print("Not enough money you broke weenie")
        else:
            if paid > cost:
                print(f"Thank you for your payment. Your change is ${round(paid-cost,2)}")
            i = 0
            print(resources)
            for x in MENU[drink]["ingredients"]:
                resources[x] = obtain_resources(drink)[0][i] - obtain_resources(drink)[1][i]
                i += 1
            print(resources)













