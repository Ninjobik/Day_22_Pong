from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.player = player
        if player == 1:
            self.x_pos = 350
        else:
            self.x_pos = -350
        self.y_pos = 0
        self.update_pos()

    def up(self):
        self.y_pos += 20
        self.update_pos()
        pass

    def down(self):
        self.y_pos -= 20
        self.update_pos()
        pass

    def update_pos(self):
        self.setposition(self.x_pos, self.y_pos)
