from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=-50, y=270)
        self.refresh()

    def add_up(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(x=-50, y=0)
        self.write(f"Game Over!", font=("Verdana", 15, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Verdana", 15, "normal"))
