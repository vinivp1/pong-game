from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        '''To direct the paddle up'''
        new_y = self.ycor() + 40
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        '''To direct the paddle down'''
        new_y = self.ycor() - 40
        self.goto(x=self.xcor(), y=new_y)
