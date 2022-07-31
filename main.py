import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
t = Player()
score = Scoreboard()
screen.listen()
screen.onkey(t.up, "Up")
cars = []

game_is_on = True
while game_is_on:
    time.sleep(score.refresh_speed)
    screen.update()
    if t.ycor() >= 280:
        score.next_level()
        t.reset_position()
    if random.randint(0,2) == 1:
        cars.append(CarManager())
    for car in cars:
        car.move()
        if car.distance(t) <= 20:
            score.game_over()
            game_is_on = False
        if car.xcor() <= -200:
            car.ht()
            cars.remove(car)
        
screen.exitonclick()