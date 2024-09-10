from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle_1 = Turtle("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(x=350, y=0)

paddle_2 = Turtle("square")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(x=-350, y=0)

def go_up(paddle):
    new_y = paddle.ycor() + 20
    paddle.goto(x=paddle.xcor(), y=new_y)

def go_down(paddle):
    new_y = paddle.ycor() - 20
    paddle.goto(x=paddle.xcor(), y=new_y)

screen.listen()
screen.onkey(go_up(paddle_1),"Up")
screen.onkey(go_down(paddle_1),"Down")
screen.onkey(go_up(paddle_2),"w")
screen.onkey(go_down(paddle_2), "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()