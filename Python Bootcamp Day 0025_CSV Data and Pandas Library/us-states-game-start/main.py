import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

'''
#pull x, y coor from clicking on screen (already in csv file)
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor())
turtle.mainloop()
'''

x=0
states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()

guesses = []

while len(guesses) < 50:
    guess = screen.textinput(title=f"States correct: {len(guesses)}/50", prompt="Guess a state").title()

    if guess == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guesses:
                missing_states.append(state)
                unknown_states = {
                    "States Missed": [missing_states]
                }
        missed = pandas.DataFrame(unknown_states)
        missed.to_csv("missed_states.csv")
        break
    if guess in states_list:
        guesses.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row_info = states_data[states_data.state == guess]
        xcor = int(row_info["x"])
        ycor = int(row_info["y"])
        t.goto(xcor, ycor)
        t.write(guess)
    if len(guesses) == 50:
        print("You win!")

#states unable to guess; generate csv of these state








screen.exitonclick()