from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.x_pos = 0
        self.y_pos = 0
        self.vertical = 10
        self.horizontal = 10
        self.move_speed = 0.09

    def move(self):
        self.x_pos += self.horizontal
        self.y_pos += self.vertical
        self.goto(self.x_pos, self.y_pos)

    def bounce_vertical(self):
        self.vertical *= -1

    def bounce_horizontal(self):
        self.horizontal *= -1
        self.move_speed *= 0.8

    def restart_ball(self):
        self.x_pos = 0
        self.y_pos = 0
        self.bounce_horizontal()
        self.move_speed = 0.09
