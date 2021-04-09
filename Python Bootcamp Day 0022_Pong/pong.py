from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

RIGHT = (350, 0)
LEFT = (-350, 0)

r_paddle = Paddle(RIGHT)
l_paddle = Paddle(LEFT)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.update_scoreboard()
    ball.move()

    #detect collision with top/bottom of screen
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect collision with sides of screen, i.e. point scored
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()