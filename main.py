from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down")
screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(0.05)
    screen.update()
    ball.move()

    #Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    # Collision with left paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()




screen.exitonclick()