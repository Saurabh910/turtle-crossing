from turtle import Turtle

X_COR, Y_COR = -280, 290


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.generate_level()

    def generate_level(self):
        self.clear()
        self.goto(X_COR, Y_COR)
        self.write(f"Level: {self.level}", align="left", font=("courier", 14, "normal"))

    def increase_level(self):
        self.level += 1
        self.generate_level()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("courier", 30, "normal"))
