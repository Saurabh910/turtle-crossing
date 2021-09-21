from turtle import Turtle
STARTING_POSITION = (0, -250)
FINAL_POSITION = (0, 250)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.generate_player()

    def generate_player(self):
        self.clear()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(10)
