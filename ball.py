from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("white")
        self.goto(0,0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        '''Make the ball moves forward'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        '''Make the ball goes to the opposite side of the board in y'''
        self.y_move *= -1

    def bounce_x(self):
        '''Make the ball goes to the opposite side of the board in x'''
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        '''Restart the ball position'''
        self.goto(0, 0)
        self.move_speed = 0.07
        self.penup()
        self.x_move *= -1

