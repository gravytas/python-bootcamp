from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        #self.write(f"Score: {str(self.score)}", align="center", font=("Arial", 24, "normal"))
        self.write(f"Score: {str(self.score)}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1

