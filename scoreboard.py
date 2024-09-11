from turtle import Turtle
FONT = ("Arial", 30, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.update_score()

    def update_score(self):
        '''Actualize the scoreboard write'''
        self.write(self.score, font= FONT)

    def plus_point(self):
        '''Add a point to the scoreboard and update'''
        self.score += 1
        self.clear()
        self.update_score()