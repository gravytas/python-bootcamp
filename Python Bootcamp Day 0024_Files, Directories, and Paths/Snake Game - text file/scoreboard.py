from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.get_highscore()
        self.write(f"Score: {self.score} High Score: {self.highscore}",  align=ALIGNMENT, font=FONT)

    def get_highscore(self):
        with open("Score.txt") as file:
            self.highscore = file.read()

    def reset(self):
        if self.score > int(self.highscore):
            new_score = str(self.score)
            with open("Score.txt", mode="w") as file:
                file.write(new_score)
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
