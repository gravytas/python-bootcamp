from turtle import Turtle, Screen
import clear_screen

timmy = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def right():
    timmy.right(5)

def left():
    timmy.left(5)

def clear():
    timmy.setpos((0, 0))
    timmy.setheading(0)
    timmy.clear()


#tell GUI to listen for user inputs on the screen
#key: the screen object will listen for the user to hit the space key. On doing so the function (fun) is set to
#the previously defined function 'move_forward' but the '()' are not used. () tells the function to run at that time.
#instead, without '()' it waits for the input to run. Function being used as an input

#when passing function as an argument or parameter to another function, it is passed without '()'
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
