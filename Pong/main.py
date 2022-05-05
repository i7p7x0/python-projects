from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("Pong")
screen.tracer(0)
ball_speed = 0.1

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True

while game_is_on:
    sleep(ball_speed)
    ball.move()
    screen.update()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 340 or ball.distance(paddle_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball_speed /= 10

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball_speed /= 10

screen.exitonclick()
