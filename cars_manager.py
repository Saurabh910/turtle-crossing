from turtle import Turtle
import random

COLORS = ["red", "yellow", "green", "blue", "orange", "aquamarine", "purple"]

class Cars_Manager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.generate_car()

    def generate_car(self):
        x_new = 300
        y_new = random.randint(-200, 200)
        self.goto(x_new, y_new)

    def move(self, move_distance = 5):
       self.forward(move_distance)



