from turtle import Screen

class Screen():
    def __init__(self):
        screen = Screen()

    def create_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("The Snake")
        self.screen.tracer(0)
