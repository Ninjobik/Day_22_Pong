import time
from turtle import Turtle, Screen
import paddle
import ball
import score

HEIGHT = 600
WIDTH = 900

turtle = Turtle()
screen = Screen()
screen.tracer(0)


screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong by Ninjobik")

player1 = paddle.Paddle(1)
player2 = paddle.Paddle(2)
p2score = score.ScoreBoard(-100)
p1score = score.ScoreBoard(100)
ball = ball.Ball()

screen.listen()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")
screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")

horizontal = 1
vertical = 1

game_on = True
while game_on:
    if ball.y_pos >= (HEIGHT/2 - 10) or ball.y_pos <= -(HEIGHT/2 - 10):
        ball.bounce_vertical()

    if ball.x_pos >= (player1.x_pos - 20) and ball.distance(player1.x_pos, player1.y_pos) < 50 or\
            ball.x_pos <= (player2.x_pos + 20) and ball.distance(player2.x_pos, player2.y_pos) < 50:
        ball.bounce_horizontal()

    if ball.x_pos >= (WIDTH/2 - 10):
        ball.restart_ball()
        p2score.add_point()

    if ball.x_pos <= -(WIDTH/2 - 10):
        ball.restart_ball()
        p1score.add_point()

    ball.move()
    screen.update()
    time.sleep(ball.move_speed)


screen.exitonclick()
