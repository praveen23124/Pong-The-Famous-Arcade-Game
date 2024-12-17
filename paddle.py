from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(coordinates)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
