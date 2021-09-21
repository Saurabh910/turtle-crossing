from turtle import Screen
from player import Player
from cars_manager import Cars_Manager
from scoreboard import ScoreBoard
import time

# Creating a screen
screen = Screen()
screen.title("Turtle Crossing")
screen.screensize(600, 600)
screen.listen()
screen.tracer(0)

player = Player()
score = ScoreBoard()
cars = []

screen.onkey(player.move, "Up")

count = 0
speed = 5
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    if count == 6:
        cars.append(Cars_Manager())
        count = 0
    count += 1

    for _ in cars:
        _.move(speed)
        if player.distance(_) < 20:
            score.gameover()
            is_game_on = False

    if player.ycor() > 220:
        score.increase_level()
        speed += 5
        player.generate_player()

screen.exitonclick()
