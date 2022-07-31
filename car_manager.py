from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.setx(300)
        self.sety(random.randint(-240,260))
        self.shapesize(1,2)
        self.seth(180)

    def move(self):
        self.forward(MOVE_INCREMENT)

    