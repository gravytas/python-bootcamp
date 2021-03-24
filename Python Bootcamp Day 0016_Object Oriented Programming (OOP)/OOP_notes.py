#import another_module
#print(another_module.another_variable)
#instantiate object from a class

# from turtle import Turtle, Screen
#
# #Turtle() is the class; setting var to class creates an object with characteristics of the class
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green1")
# timmy.forward(100)
#
# #object exists in memory, prints mem address
# print(timmy)
#
# #Screen() is another class from the library; canvheight is an attribute associated with the class
# my_screen = Screen()
# print(my_screen.canvheight)
#
# #methods
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table.align)
print(table)

