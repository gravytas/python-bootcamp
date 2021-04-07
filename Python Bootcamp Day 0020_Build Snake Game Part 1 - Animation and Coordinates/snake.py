from turtle import Turtle
#constants
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake = Turtle()
            new_snake.shape("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.snakes.append(new_snake)

    def move(self):
        # range(start=x, stop=0, step=-1)
        # get snake to automatically follow itself. each subsequent segment moves to coordinates of the one ahead of it
        for x in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[x - 1].xcor()
            new_y = self.snakes[x - 1].ycor()
            self.snakes[x].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)