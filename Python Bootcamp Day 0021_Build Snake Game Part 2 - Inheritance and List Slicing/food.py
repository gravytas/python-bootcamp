from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        #multiplies 20x20 widxlen by provided float
        self.shapesize(stretch_wid=.625, stretch_len=.625)
        self.color("yellow")
        self.speed("fastest")
        #600x600 square space (
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)