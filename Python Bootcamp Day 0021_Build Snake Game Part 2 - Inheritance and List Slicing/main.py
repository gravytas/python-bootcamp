from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#instantiate objects
screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#setup screen
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("The Snake")

#turn screen delay off
screen.tracer(0)


#screen listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.08)
    snake.move()
    scoreboard.goto(0, 260)
    scoreboard.update_scoreboard()

    #detect snake collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.gameover()

    #detect collision with tail; if head collides with any segment of tail; trigger scoreboard.gameover()
    #slice list of snakes to avoid getting the snake head position so it doesn't gameover on the snake head
    #for position in snake.snakes[1:len(snake.snakes)-2]: OR omit second number and it goes to end of the list

    #snakes[1:6:2] (start, stop, increment)
    #snakes[::-1] - reverse how list is passed through

    # ^ also works with tuples

        for position in snake.snakes[1:]:
            if snake.head.distance(position) < 10:
                game_on = False
                scoreboard.gameover()

screen.exitonclick()