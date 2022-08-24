import time
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=275)
        self.update_scorer()

    def get_high_score(self):
        with open("High_score.txt", mode = 'r') as file:
            self.high_score = int(file.read())

    def update_scorer(self):
        self.write(arg=f"Score : {self.score}\tHigh Score : {self.high_score}", move=False, align="center",
                   font=("Verdana", 15, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High_score.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.clear()
        self.update_scorer()

    def scorer(self):
        self.score += 1
        self.clear()
        self.update_scorer()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over (continuing in 3 seconds)", move=False, align="center",
                   font=("Verdana", 15, "normal"))
        time.sleep(3)
        self.clear()
        self.goto(x=0, y=275)
