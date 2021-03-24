from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from clear_screen import clear

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


remain_on = True
while remain_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        remain_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"Your {choice} costs ${drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                clear()



