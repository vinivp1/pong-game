from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard_r = Scoreboard((40, 240))
scoreboard_l = Scoreboard((-40, 240))

screen.listen()
screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down")
screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with both paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Collision with the right wall and add point to the left side
    if ball.xcor() > 390:
        ball.restart()
        scoreboard_l.plus_point()

    # Collision with the left wall and add point to the right side
    if ball.xcor() < -390:
        ball.restart()
        scoreboard_r.plus_point()

screen.exitonclick()