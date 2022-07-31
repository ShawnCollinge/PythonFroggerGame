from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
REFRESH_SPEED = 0.1
REFRESH_STEPS = 0.01

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.refresh_speed = REFRESH_SPEED
        self.speed("fastest")
        self.color("black")
        self.ht()
        self.level = 1
        self.goto(-290,270)
        self.print_score()
    
    def print_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.refresh_speed -= REFRESH_STEPS
        self.print_score()

