from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.setposition(x, 250)
        self.write(self.score, False, "center", ("Ariel", 15, "normal"))

    def add_point(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score, False, "center", ("Ariel", 15, "normal"))
