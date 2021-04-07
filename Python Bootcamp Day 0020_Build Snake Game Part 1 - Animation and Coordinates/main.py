from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
snake = Snake()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.05)

    snake.move()





















screen.exitonclick()