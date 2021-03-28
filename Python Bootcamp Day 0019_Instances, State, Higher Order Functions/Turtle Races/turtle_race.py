from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which  "
        "turtle will win the race? \nEnter a color blue/red/green/yellow/orange/purple: ")
colors = ["blue", "red", "green", "yellow", "orange", "purple"]
race_in_progress = False


y = -125
turtles = []
for x in range(len(colors)):
    #instantiate new object
    new_turtle = Turtle(shape="turtle")

    #lift pen
    new_turtle.penup()

    #set object color
    new_turtle.color(colors[x])

    #set turtle postion
    new_turtle.goto(x=-225, y=y)

    #add object to list
    turtles.append(new_turtle)
    y += 50

if user_bet:
    race_in_progress = True

while race_in_progress == True:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race_in_progress = False
            winner = turtle.pencolor()
            if user_bet.lower() == winner:
                print(f"You won! The winner is {winner}!")
            else:
                print(f"Sorry, you lost. The winner is {winner}!")

        distance = random.randint(0,10)
        turtle.forward(distance)















screen.exitonclick()