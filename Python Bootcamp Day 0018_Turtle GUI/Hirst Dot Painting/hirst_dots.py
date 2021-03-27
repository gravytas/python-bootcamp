import colorgram
import turtle as t
import random


#extract colors from image and create color list.
#colorgram extracts colors by order of most color to least color.

# colors = colorgram.extract('image.jpg', 12)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

#took out first color as it is background of the image b/c most frequently used int he image
color_list = [
    (233, 222, 228),
    (190, 172, 0),
    (208, 0, 103),
    (0, 148, 60),
    (253, 69, 0),
    (217, 229, 234),
    (167, 0, 0),
    (0, 128, 205),
    (89, 0, 95),
    (254, 223, 0),
    (232, 234, 232)
]

#print 10x10 dots; spaced by 50; circle size 20
t.colormode(255)
timmy = t.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.setheading(270)
timmy.forward(225)
timmy.setheading(180)
timmy.forward(225)
timmy.setheading(0)


def make_dots():
    for x in range (10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)

def turn_up():
    timmy.back(50)
    timmy.setheading(90)
    timmy.forward(50)


for x in range(10):
    make_dots()
    turn_up()
    if (x+2)%2 == 0:
        timmy.setheading(180)
    else:
        timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()