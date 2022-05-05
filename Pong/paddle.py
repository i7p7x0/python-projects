from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self,coordinates):
        super().__init__()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(coordinates)
        self.shape("square")
        self.color("white")
        self.x_coordinate=coordinates[0]

    def up(self):
        self.penup()
        self.goto(self.x_coordinate, self.ycor()+20)

    def down(self):
        self.penup()
        self.goto(self.x_coordinate, self.ycor() - 20)
