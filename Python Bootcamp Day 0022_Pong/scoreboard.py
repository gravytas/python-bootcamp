from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0




    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("courier", 75, "normal"))
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("courier", 75, "normal"))

    def r_point(self):
        self.right_score += 1
        self.update_scoreboard()


    def l_point(self):
        self.left_score += 1
        self.update_scoreboard()



