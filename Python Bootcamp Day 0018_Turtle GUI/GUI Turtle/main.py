import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# from turtle import *
# tom = Turtle()
# import turtle
# bill = turtle.Turtle()


timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)

# challenge 1
# for x in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# challenge 2
# for x in range(10):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

# challenge 3
# for x in range(3, 11):
#     timmy.pencolor(random_color())
#     timmy.color(random_color())
#     angle = 360/x
#     timmy.forward(60)
#     for i in range(0, x-1):
#         timmy.right(angle)
#         timmy.forward(60)
#     timmy.right(angle)

# challenge 4
# colors = ["red", "blue", "green", "yellow", "purple", "violet", "black", "grey", "orange"]
# turns = [0, 90, 180, 270]
#
# timmy.pensize(5)
# for x in range(100):
#     timmy.color(random.choice(colors))
#     timmy.setheading(random.choice(turns))
#     timmy.forward(15)

# challenge 5
# python tuples (1, 3, 8) - ordered tuple. Like a list, but cannot change/edit the values within it
#my_tuple = (1, 3, 8)
#print(my_tuple[1])
# turn tuple into a list
#list(my_tuple)


#challenge 6 spirograph
timmy.speed("fastest")

def draw_circle(size):
    size = size
    for x in range(int(360 / size)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.left(size)

draw_circle(5)


screen = t.Screen()
screen.exitonclick()


